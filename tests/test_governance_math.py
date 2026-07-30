"""
tests/test_governance_math.py
=============================
Полный стресс-тест HelixGovernanceMath (Module 0).

Покрывает:
  - все 6 публичных методов
  - граничные условия каждой формулы
  - приоритет решений (BLOCK > EU > NGI > LOW_CS > CIRI > PASS)
  - реальные сценарии из спецификации GOVERNANCE v1.3
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from engine.governance_math import (
    HelixGovernanceMath,
    Hallucination,
    HALLUCINATION_WEIGHTS,
    NGI_THRESHOLDS,
    RPL_BLOCK_THRESHOLD,
    CIRI_WARN_THRESHOLD,
    CONFIDENCE_HITL_THRESHOLD,
)

math = HelixGovernanceMath()


# ─── Helpers ─────────────────────────────────────────────────────────────────

def h(type="TYPE-1", severity="HIGH", desc="test", evidence="test evidence"):
    return Hallucination(type=type, severity=severity, description=desc, evidence=evidence)

def ngi_dims(e=0, p=0, a=0, i=0):
    return {"emotional": e, "political": p, "archetypal": a, "industry": i}


# ─── 1. RPL Factor ───────────────────────────────────────────────────────────

def test_rpl_no_pressure():
    """Если allocated >= required → RPL_Factor = 1.0"""
    assert math.calculate_rpl_factor(8.0, 8.0) == 1.0
    assert math.calculate_rpl_factor(8.0, 10.0) == 1.0
    assert math.calculate_rpl_factor(0.0, 5.0) == 1.0

def test_rpl_full_deficit():
    """Allocated = 0 при required > 0 → 1 - penalty_weight"""
    result = math.calculate_rpl_factor(8.0, 0.0, penalty_weight=0.5)
    assert result == 0.5

def test_rpl_partial_deficit():
    """50% дефицит × 0.5 penalty = 0.75"""
    result = math.calculate_rpl_factor(8.0, 4.0, penalty_weight=0.5)
    assert result == 0.75

def test_rpl_boundary_exactly_threshold():
    """RPL_Factor ровно на пороге блокировки"""
    factor = math.calculate_rpl_factor(required_hours=10.0, allocated_hours=4.0)
    assert factor == 0.70
    assert math.should_block_ect4(factor) is False  # >= threshold → не блокировать

def test_rpl_below_threshold_blocks():
    """RPL_Factor ниже 0.70 → should_block_ect4 = True"""
    factor = math.calculate_rpl_factor(10.0, 3.0)
    assert factor < RPL_BLOCK_THRESHOLD
    assert math.should_block_ect4(factor) is True


# ─── 2. Confidence Score ─────────────────────────────────────────────────────

def test_confidence_no_hallucinations():
    """Без галлюцинаций при RPL=1.0 → confidence = 1.0"""
    cs = math.calculate_confidence_score([], rpl_factor=1.0)
    assert cs == 1.0

def test_confidence_single_critical():
    """Одна CRITICAL (weight=0.80) → 1.0 × (1 - 0.80) = 0.20"""
    cs = math.calculate_confidence_score([h(severity="CRITICAL")])
    assert cs == 0.20

def test_confidence_multiplicative():
    """Две HIGH (weight=0.40 каждая) → 1.0 × 0.60 × 0.60 = 0.36"""
    cs = math.calculate_confidence_score([h(severity="HIGH"), h(severity="HIGH")])
    assert abs(cs - 0.36) < 0.001

def test_confidence_rpl_penalty():
    """RPL снижает итоговый score пропорционально"""
    cs_full = math.calculate_confidence_score([h(severity="LOW")])
    cs_rpl  = math.calculate_confidence_score([h(severity="LOW")], rpl_factor=0.8)
    assert cs_rpl < cs_full
    assert cs_rpl == round(cs_full * 0.8, 4)

def test_confidence_level_mapping():
    """Проверка всех 4 уровней"""
    assert math.confidence_level(1.00) == "HIGH"
    assert math.confidence_level(0.90) == "HIGH"
    assert math.confidence_level(0.89) == "MEDIUM"
    assert math.confidence_level(0.61) == "MEDIUM"
    assert math.confidence_level(0.60) == "LOW"
    assert math.confidence_level(0.31) == "LOW"
    assert math.confidence_level(0.30) == "CRITICAL"
    assert math.confidence_level(0.00) == "CRITICAL"

def test_confidence_many_hallucinations_approaches_zero():
    """Много галлюцинаций → confidence → 0"""
    many = [h(severity="CRITICAL")] * 10
    cs = math.calculate_confidence_score(many)
    assert cs < 0.001


# ─── 3. NGI Score ────────────────────────────────────────────────────────────

def test_ngi_all_zero():
    ngi = math.calculate_ngi_score(0, 0, 0, 0)
    assert ngi.total == 0
    assert ngi.level == "LOW"

def test_ngi_low_boundary():
    """total=3 → LOW"""
    ngi = math.calculate_ngi_score(1, 1, 1, 0)
    assert ngi.total == 3
    assert ngi.level == "LOW"

def test_ngi_moderate():
    """total=4 → MODERATE"""
    ngi = math.calculate_ngi_score(1, 1, 1, 1)
    assert ngi.total == 4
    assert ngi.level == "MODERATE"

def test_ngi_high():
    """total=7 → HIGH"""
    ngi = math.calculate_ngi_score(2, 2, 2, 1)
    assert ngi.total == 7
    assert ngi.level == "HIGH"

def test_ngi_critical():
    """total=10 → CRITICAL"""
    ngi = math.calculate_ngi_score(3, 3, 2, 2)
    assert ngi.total == 10
    assert ngi.level == "CRITICAL"

def test_ngi_max():
    """total=12 → CRITICAL (max возможный)"""
    ngi = math.calculate_ngi_score(3, 3, 3, 3)
    assert ngi.total == 12
    assert ngi.level == "CRITICAL"

def test_ngi_clamp_above_3():
    """Значения выше 3 зажимаются до 3"""
    ngi = math.calculate_ngi_score(5, 5, 5, 5)
    assert ngi.total == 12
    assert ngi.emotional == 3


# ─── 4. CIRI ─────────────────────────────────────────────────────────────────

def test_ciri_clean_input():
    """Чистый ввод → CIRI близок к 0"""
    ngi  = math.calculate_ngi_score(0, 0, 0, 0)
    ciri = math.calculate_ciri(1.0, ngi, [], rpl_factor=1.0)
    assert ciri.value == 0

def test_ciri_critical_hallucination_raises():
    """CRITICAL галлюцинация → значительный CIRI"""
    ngi  = math.calculate_ngi_score(0, 0, 0, 0)
    ciri = math.calculate_ciri(0.20, ngi, [h(severity="CRITICAL")], 1.0)
    assert ciri.value > 40

def test_ciri_max_is_100():
    """CIRI не превышает 100"""
    ngi  = math.calculate_ngi_score(3, 3, 3, 3)
    many = [h(severity="CRITICAL")] * 5
    ciri = math.calculate_ciri(0.0, ngi, many, rpl_factor=0.0)
    assert ciri.value <= 100

def test_ciri_components_sum():
    """Сумма компонентов равна итогу (до min-100 и int())"""
    ngi  = math.calculate_ngi_score(1, 1, 0, 0)
    hall = [h(severity="HIGH")]
    ciri = math.calculate_ciri(0.5, ngi, hall, rpl_factor=0.9)
    raw = ciri.base_risk + ciri.ngi_risk + ciri.hallucination_risk + ciri.rpl_risk
    assert ciri.value == min(100, int(raw))


# ─── 5. Article 9 ────────────────────────────────────────────────────────────

def test_article9_fully_compliant():
    """Все требования выполнены с доказательствами → COMPLIANT"""
    met = {f"A9-R{i}": True for i in range(1, 9)}
    ev  = {f"A9-R{i}": 3   for i in range(1, 9)}
    a9  = math.calculate_article9_score(met, ev)
    assert a9.score == 100
    assert a9.level == "COMPLIANT"

def test_article9_nothing_met():
    """Ничего не выполнено, нет доказательств → NON_COMPLIANT"""
    a9 = math.calculate_article9_score({}, {})
    assert a9.score == 0
    assert a9.level == "NON_COMPLIANT"

def test_article9_partial_evidence():
    """met=True но evidence=1 → 70% веса"""
    met = {"A9-R1": True}
    ev  = {"A9-R1": 1}
    a9  = math.calculate_article9_score(met, ev)
    expected = round(20 * 0.7)  # A9-R1 вес = 20
    assert a9.score == expected

def test_article9_partial_level():
    """score в 60–84 → PARTIAL. Нужно больше требований с полными доказательствами."""
    # R1(20)+R3(15)+R4(15)+R6(15)+R2(10)+R5(10) × 0.7 = 85×0.7 = 59.5 → нет
    # Берём: R1+R3+R4+R6 полностью (evidence=3) + R2+R5 частично
    met = {"A9-R1": True, "A9-R3": True, "A9-R4": True, "A9-R6": True,
           "A9-R2": True, "A9-R5": True}
    ev  = {"A9-R1": 3, "A9-R3": 3, "A9-R4": 3, "A9-R6": 3,
           "A9-R2": 1, "A9-R5": 1}
    a9  = math.calculate_article9_score(met, ev)
    # 20+15+15+15=65 × 1.0  +  (10+10)×0.7=14  = 79
    assert 60 <= a9.score < 85, f"Ожидали 60–84, получили {a9.score}"
    assert a9.level == "PARTIAL"


# ─── 6. Governance Decision (приоритет) ──────────────────────────────────────

def test_decision_pass_clean():
    """Чистый ввод → PASS"""
    ngi  = math.calculate_ngi_score(0, 0, 0, 0)
    ciri = math.calculate_ciri(1.0, ngi, [], 1.0)
    d = math.make_governance_decision(1.0, ciri, [], ngi, "minimal_risk", [])
    assert d.decision == "PASS"
    assert d.reason is None

def test_decision_block_by_hallucination_type():
    """TYPE-1 в block_on_types → BLOCK, не смотрим дальше"""
    hall = [h(type="TYPE-1", severity="LOW")]
    ngi  = math.calculate_ngi_score(0, 0, 0, 0)
    ciri = math.calculate_ciri(0.95, ngi, hall, 1.0)
    d = math.make_governance_decision(0.95, ciri, hall, ngi, "minimal_risk", ["TYPE-1"])
    assert d.decision == "BLOCK"
    assert d.block_source == "HALLUCINATION_BLOCK_RULE"

def test_decision_block_eu_unacceptable():
    """EU tier = unacceptable → BLOCK"""
    ngi  = math.calculate_ngi_score(0, 0, 0, 0)
    ciri = math.calculate_ciri(1.0, ngi, [], 1.0)
    d = math.make_governance_decision(1.0, ciri, [], ngi, "unacceptable", [])
    assert d.decision == "BLOCK"
    assert d.block_source == "EU_AI_ACT"

def test_decision_hitl_ngi():
    """NGI total >= 7 (threshold) → HITL_REQUIRED"""
    ngi  = math.calculate_ngi_score(2, 2, 2, 1)  # total=7
    ciri = math.calculate_ciri(0.8, ngi, [], 1.0)
    d = math.make_governance_decision(0.8, ciri, [], ngi, "minimal_risk", [], ngi_threshold=7)
    assert d.decision == "HITL_REQUIRED"
    assert d.block_source == "NGI_THRESHOLD"

def test_decision_hitl_low_confidence():
    """confidence < 0.30 → HITL_REQUIRED"""
    ngi  = math.calculate_ngi_score(0, 0, 0, 0)
    ciri = math.calculate_ciri(0.25, ngi, [], 1.0)
    d = math.make_governance_decision(0.25, ciri, [], ngi, "minimal_risk", [])
    assert d.decision == "HITL_REQUIRED"
    assert d.block_source == "LOW_CONFIDENCE"

def test_decision_warn_ciri():
    """
    CIRI > 70 (но confidence >= 0.30 и NGI < threshold) → WARN.

    Нужно добрать CIRI > 70 без ухода в HITL_REQUIRED:
      confidence = 0.45 → base_risk = (1-0.45)×50 = 27.5
      NGI total=6 → ngi_risk = 6×(20/12) = 10.0
      3×HIGH hall → hall_risk = min(3×5, 20) = 15
      raw = 27.5 + 10 + 15 = 52.5 → CIRI=52 — ещё мало

    Добавим RPL давление:
      rpl_factor=0.5 → rpl_risk = (1-0.5)×10 = 5
      raw = 57.5 → CIRI=57 — всё ещё мало

    Нужен более высокий base_risk: confidence=0.32
      base_risk = (1-0.32)×50 = 34
      NGI total=6 → 10
      hall_risk = 15
      rpl_risk = 5
      raw = 64 → CIRI=64 — ещё не хватает

    Добавим 2 CRITICAL hall → hall_risk = min(2×10+1×5,20) = 20:
      base = 34, ngi=10, hall=20, rpl=5 → raw=69 → CIRI=69 — близко

    confidence=0.31 → base = (0.69)×50 = 34.5 → raw=69.5 → CIRI=69 нет

    confidence=0.31, NGI=6, 2×CRITICAL+1×HIGH, rpl=0.4:
      base=34.5, ngi=10, hall=20, rpl=(0.6)×10=6 → raw=70.5 → CIRI=70 нет (не >70)

    confidence=0.31, NGI=6, 2×CRITICAL+2×HIGH, rpl=0.4:
      base=34.5, ngi=10, hall=min(20+10,20)=20, rpl=6 → raw=70.5 → CIRI=70

    Используем confidence=0.31, NGI=6, полный hall_risk=20, rpl=0.3:
      base=34.5, ngi=10, hall=20, rpl=(0.7)×10=7 → raw=71.5 → CIRI=71 ✅
    """
    ngi  = math.calculate_ngi_score(2, 2, 1, 1)   # total=6 MODERATE, не триггер NGI (< 7)
    hall = [
        h(severity="CRITICAL"),
        h(severity="CRITICAL"),
        h(severity="HIGH"),
        h(severity="HIGH"),
    ]
    cs   = 0.31                                     # >= 0.30 → не HITL_REQUIRED
    rpl  = 0.30                                     # rpl_risk = 0.7×10 = 7
    ciri = math.calculate_ciri(cs, ngi, hall, rpl)
    assert ciri.value > CIRI_WARN_THRESHOLD, f"CIRI должен быть > 70, получили {ciri.value}"
    d = math.make_governance_decision(cs, ciri, hall, ngi, "minimal_risk", [],
                                      ngi_threshold=7)
    assert d.decision == "WARN", f"Ожидали WARN, получили {d.decision}"
    assert d.block_source == "CIRI_THRESHOLD"

def test_decision_priority_block_before_eu():
    """
    BLOCK (hallucination) имеет приоритет перед EU unacceptable.
    Оба условия истинны — должен вернуть HALLUCINATION_BLOCK_RULE, не EU_AI_ACT.
    """
    hall = [h(type="TYPE-7", severity="CRITICAL")]
    ngi  = math.calculate_ngi_score(0, 0, 0, 0)
    ciri = math.calculate_ciri(0.20, ngi, hall, 1.0)
    d = math.make_governance_decision(0.20, ciri, hall, ngi, "unacceptable", ["TYPE-7"])
    assert d.decision == "BLOCK"
    assert d.block_source == "HALLUCINATION_BLOCK_RULE"


# ─── 7. Полный проход run() ──────────────────────────────────────────────────

def test_run_happy_path():
    """Чистый ввод через run() → PASS, все метрики в норме"""
    result = math.run(
        hallucinations=[],
        ngi_dimensions=ngi_dims(0, 0, 0, 0),
        eu_tier="minimal_risk",
        block_on_types=[],
    )
    assert result.decision.decision == "PASS"
    assert result.confidence_score == 1.0
    assert result.confidence_level == "HIGH"
    assert result.rpl_factor == 1.0
    assert result.rpl_blocked is False
    assert result.ngi.total == 0
    assert result.ciri.value == 0

def test_run_with_article9():
    """run() с Article 9 расчётом"""
    result = math.run(
        hallucinations=[],
        ngi_dimensions=ngi_dims(),
        eu_tier="high_risk",
        block_on_types=[],
        requirements_met={"A9-R1": True, "A9-R6": True},
        evidence_counts={"A9-R1": 3, "A9-R6": 3},
    )
    assert result.article9 is not None
    assert result.article9.score == 35  # 20 + 15

def test_run_critical_scenario():
    """
    Реальный сценарий: AI-агент даёт юридическую рекомендацию клиенту.
    TYPE-1 (выдуманный источник) в client-facing контексте.
    Ожидаем: BLOCK.
    """
    hall = [h(type="TYPE-1", severity="CRITICAL",
               desc="Сослался на несуществующее решение суда",
               evidence="Согласно решению Верховного суда №12345/2025...")]
    result = math.run(
        hallucinations=hall,
        ngi_dimensions=ngi_dims(1, 0, 0, 2),
        eu_tier="high_risk",
        block_on_types=["TYPE-1", "TYPE-7"],
        required_hours=4.0,
        allocated_hours=1.0,
    )
    assert result.decision.decision == "BLOCK"
    assert result.confidence_level == "CRITICAL"
    assert result.rpl_blocked is True


# ─── Запуск ──────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    tests = [
        (name, fn) for name, fn in globals().items()
        if name.startswith("test_") and callable(fn)
    ]
    passed = failed = 0
    for name, fn in tests:
        try:
            fn()
            print(f"  ✅ {name}")
            passed += 1
        except Exception as e:
            print(f"  ❌ {name}: {e}")
            failed += 1
    print(f"\n{'='*50}")
    print(f"Итого: {passed} прошли, {failed} упали из {passed+failed}")
    if failed:
        raise SystemExit(1)
