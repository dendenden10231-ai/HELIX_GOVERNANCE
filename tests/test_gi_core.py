"""
tests/test_gi_core.py
=====================
Стресс-тест GI v6.2 Core Engine (Module 1).

Покрывает все 7 протоколов:
  P33 SSC / P34 FRCP / P35 CDR / P45 SAD / P46 NGI / P55 PPS / P56 OAS

Реальные сценарии из спецификации GI v6.2:
  - Уотергейт (анонимный источник, SSC)
  - МакМартинский процесс (принуждение, ECT-заморозка)
  - Ирак ОМУ (NGI CRITICAL, NON LIQUET)
  - Enron (SAD-2, стратегическое молчание)
  - Панамские документы (CDR, множественные источники)
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from datetime import datetime, timezone, timedelta
from engine.gi_core import (
    GICore, ECTLevel, ECT_FROZEN,
    Source, SSCType, SSCEvent,
    Fact, FRCPProtocol,
    CDRProtocol,
    SADProtocol, SADType,
    NGI_ACTIONS, get_ngi_actions,
    pps_prioritize, PPSLevel,
    OASJournal,
)

NOW = datetime.now(timezone.utc)


# ─── Helpers ──────────────────────────────────────────────────────────────────

def make_source(sid, ect=ECTLevel.ECT3, ioi=0.0):
    return Source(source_id=sid, name=f"Source-{sid}", ect_level=ect, ioi_score=ioi)

def make_fact(fid, ect=ECTLevel.ECT4, sources=None, ts=None, falsified=False):
    return Fact(
        fact_id=fid,
        description=f"Факт {fid}",
        ect_level=ect,
        source_ids=sources or [],
        timestamp=ts,
        falsification_attempted=falsified,
    )


# ─── P33: SSC ─────────────────────────────────────────────────────────────────

def test_ssc_recantation_freezes_source():
    """SSC-1: рекантация → источник заморожен, FRCP триггер"""
    gi = GICore("INV-SSC-001")
    src = make_source("W-001", ect=ECTLevel.ECT3)
    event = SSCEvent(
        event_type=SSCType.SSC1_RECANTATION,
        source_id="W-001",
        timestamp=NOW,
        description="Источник отозвал показания под давлением адвокатов",
    )
    result = gi.ssc.apply(src, event)
    assert result.frozen is True
    assert src.frozen is True
    assert result.new_ect is None   # заморожен, не понижен
    assert result.trigger_frcp is True
    assert result.trigger_cdr is False
    assert "ECT-FROZEN" in result.marker

def test_ssc_coercion_freezes():
    """SSC-2: принуждение → заморозка"""
    gi = GICore("INV-SSC-002")
    src = make_source("W-002", ect=ECTLevel.ECT4)
    event = SSCEvent(
        event_type=SSCType.SSC2_COERCION,
        source_id="W-002",
        timestamp=NOW,
        description="Источник арестован по статье о государственной тайне",
    )
    result = gi.ssc.apply(src, event)
    assert result.frozen is True
    assert result.trigger_frcp is True

def test_ssc_death_downgrades_one():
    """SSC-3: смерть → понизить на 1 ECT, CDR триггер"""
    gi = GICore("INV-SSC-003")
    src = make_source("W-003", ect=ECTLevel.ECT4)
    event = SSCEvent(
        event_type=SSCType.SSC3_DEATH,
        source_id="W-003",
        timestamp=NOW,
        description="Источник погиб в автокатастрофе",
    )
    result = gi.ssc.apply(src, event)
    assert result.frozen is False
    assert result.new_ect == ECTLevel.ECT3
    assert src.ect_level == ECTLevel.ECT3
    assert result.trigger_cdr is True
    assert result.trigger_frcp is False

def test_ssc_hidden_link_downgrades():
    """SSC-4: скрытая связь → понижение + CDR"""
    gi = GICore("INV-SSC-004")
    src = make_source("W-004", ect=ECTLevel.ECT3, ioi=0.1)
    event = SSCEvent(
        event_type=SSCType.SSC4_HIDDEN_LINK,
        source_id="W-004",
        timestamp=NOW,
        description="Обнаружено что источник — племянник обвиняемого",
    )
    result = gi.ssc.apply(src, event)
    assert result.new_ect == ECTLevel.ECT2
    assert result.trigger_cdr is True

def test_ssc_reactivation_unfreezes():
    """SSC-5: реактивация → снимает заморозку"""
    gi = GICore("INV-SSC-005")
    src = make_source("W-005", ect=ECTLevel.ECT3)
    src.frozen = True

    freeze_event = SSCEvent(SSCType.SSC1_RECANTATION, "W-005", NOW, "отказался")
    gi.ssc.apply(src, freeze_event)
    assert src.frozen is True

    reactivate_event = SSCEvent(SSCType.SSC5_REACTIVATION, "W-005",
                                NOW + timedelta(days=30), "адвокаты отозваны")
    result = gi.ssc.apply(src, reactivate_event)
    assert result.frozen is False
    assert src.frozen is False
    assert "реактивирован" in result.marker

def test_ssc_ect1_cannot_downgrade_below():
    """SSC-3 на ECT-1 → остаётся ECT-1 (не ниже)"""
    gi = GICore("INV-SSC-006")
    src = make_source("W-006", ect=ECTLevel.ECT1)
    event = SSCEvent(SSCType.SSC3_DEATH, "W-006", NOW, "умер")
    result = gi.ssc.apply(src, event)
    assert result.new_ect == ECTLevel.ECT1
    assert src.ect_level == ECTLevel.ECT1


# ─── P34: FRCP ────────────────────────────────────────────────────────────────

def test_frcp_primacy_wins():
    """Более ранний факт побеждает по критерию первичности"""
    sources = {"S1": make_source("S1"), "S2": make_source("S2")}
    fact_a = make_fact("FA", sources=["S1"], ts=NOW - timedelta(days=10))
    fact_b = make_fact("FB", sources=["S2"], ts=NOW - timedelta(days=2))
    frcp = FRCPProtocol()
    result = frcp.arbitrate(fact_a, fact_b, sources)
    assert result.winner_fact_id == "FA"
    assert "ПЕРВИЧНОСТЬ" in result.winner_criteria
    assert result.loser_new_ect == ECTLevel.ECT3
    assert fact_b.ect_level == ECTLevel.ECT3

def test_frcp_independence_wins():
    """Более независимый источник побеждает"""
    src_independent = make_source("SI", ioi=0.1)  # низкий ICoI = независимый
    src_affiliated  = make_source("SA", ioi=0.8)  # высокий ICoI = зависимый
    sources = {"SI": src_independent, "SA": src_affiliated}
    fact_a = make_fact("FA", sources=["SI"])
    fact_b = make_fact("FB", sources=["SA"])
    frcp = FRCPProtocol()
    result = frcp.arbitrate(fact_a, fact_b, sources)
    assert result.winner_fact_id == "FA"
    assert "НЕЗАВИСИМОСТЬ" in result.winner_criteria

def test_frcp_falsification_wins():
    """Факт прошедший попытку фальсификации побеждает"""
    sources = {"S1": make_source("S1"), "S2": make_source("S2")}
    fact_a = make_fact("FA", sources=["S1"], falsified=True)
    fact_b = make_fact("FB", sources=["S2"], falsified=False)
    frcp = FRCPProtocol()
    result = frcp.arbitrate(fact_a, fact_b, sources)
    assert result.winner_fact_id == "FA"
    assert "ФАЛЬСИФИЦИРУЕМОСТЬ" in result.winner_criteria

def test_frcp_non_liquet_on_tie():
    """Равенство критериев → NON LIQUET"""
    sources = {"S1": make_source("S1", ioi=0.5), "S2": make_source("S2", ioi=0.5)}
    # Одинаковое время, одинаковый ICoI, оба без фальсификации
    ts = NOW - timedelta(days=5)
    fact_a = make_fact("FA", sources=["S1"], ts=ts)
    fact_b = make_fact("FB", sources=["S2"], ts=ts)
    frcp = FRCPProtocol()
    result = frcp.arbitrate(fact_a, fact_b, sources)
    assert result.non_liquet is True
    assert result.resolved is False
    assert "NON LIQUET" in result.marker


# ─── P35: CDR ─────────────────────────────────────────────────────────────────

def test_cdr1_single_source_downgrades():
    """CDR-1: единственный источник дисквалифицирован → понизить"""
    sources = {"S1": make_source("S1")}
    fact = make_fact("F1", ect=ECTLevel.ECT4, sources=["S1"])
    cdr = CDRProtocol()
    result = cdr.apply(fact, "S1", sources)
    assert result.cdr_type.value == "CDR-1"
    assert result.new_ect == ECTLevel.ECT3
    assert fact.ect_level == ECTLevel.ECT3
    assert "CDR-1" in result.marker

def test_cdr2a_with_document_preserves_ect():
    """CDR-2а: документ остаётся → ECT сохраняется"""
    src_person   = make_source("S-PERSON", ioi=0.5)
    src_document = make_source("S-DOC",    ioi=0.1)  # документ: ioi < 0.2
    sources = {"S-PERSON": src_person, "S-DOC": src_document}
    fact = make_fact("F2", ect=ECTLevel.ECT4, sources=["S-PERSON", "S-DOC"])
    cdr = CDRProtocol()
    result = cdr.apply(fact, "S-PERSON", sources)
    assert result.cdr_type.value == "CDR-2а"
    assert result.new_ect == ECTLevel.ECT4   # сохранён
    assert "S-PERSON" not in fact.source_ids

def test_cdr2b_exception_group_drops_below_3():
    """
    CDR-2б: группа ECT-4 EXCEPTION < 3 → аннулировать до ECT-3

    ioi=0.5 (не 0.0 по умолчанию) — иначе источники ошибочно
    распознаются эвристикой has_document (ioi<0.2 = "похоже на документ")
    и тест уходит в ветку CDR-2а вместо Exception Pathway.
    """
    sources = {"S1": make_source("S1", ioi=0.5), "S2": make_source("S2", ioi=0.5),
               "S3": make_source("S3", ioi=0.5), "S4": make_source("S4", ioi=0.5)}
    fact = make_fact("F3", ect=ECTLevel.ECT4, sources=["S1","S2","S3","S4"])
    cdr = CDRProtocol()
    result = cdr.apply(fact, "S1", sources, exception_group_size=4)
    assert result.cdr_type.value == "CDR-2б"
    # 4-1=3 → ровно 3, НЕ ниже порога (< 3)
    assert result.new_ect == ECTLevel.ECT4

    # Ещё один дисквалифицирован → станет < 3
    fact2 = make_fact("F4", ect=ECTLevel.ECT4, sources=["S1","S2","S3"])
    result2 = cdr.apply(fact2, "S1", sources, exception_group_size=3)
    # 3-1=2 < 3 → ECT-3
    assert result2.new_ect == ECTLevel.ECT3

def test_cdr3_indirect_monitor_only():
    """CDR-3: косвенная зависимость → только мониторинг, ECT не меняется"""
    sources = {"S2": make_source("S2")}
    fact = make_fact("F5", ect=ECTLevel.ECT3, sources=["S2"])
    cdr = CDRProtocol()
    # S1 дисквалифицирован, но F5 на него не опирался напрямую
    result = cdr.apply(fact, "S1", sources)
    assert result.cdr_type.value == "CDR-3"
    assert result.monitor_only is True
    assert result.new_ect == ECTLevel.ECT3  # не изменился


# ─── P45: SAD ─────────────────────────────────────────────────────────────────

def test_sad0_no_obligation():
    """SAD-0: нет обязательства и не системное → не значимо"""
    sad = SADProtocol()
    result = sad.analyze("переписка CEO",
                         dv1_obligation=False, dv2_systematic=False,
                         dv3_exists_elsewhere=False, dv4_group_refusal=False,
                         dv5_pattern=False)
    assert result.sad_type == SADType.SAD0
    assert result.ect_signal is None

def test_sad1_technical_reason():
    """SAD-1: техническая причина есть → верифицировать"""
    sad = SADProtocol()
    result = sad.analyze("финансовые записи",
                         dv1_obligation=True, dv2_systematic=False,
                         dv3_exists_elsewhere=True, dv4_group_refusal=False,
                         dv5_pattern=False,
                         technical_reason="записи уничтожены при пожаре")
    assert result.sad_type == SADType.SAD1
    assert result.ect_signal is None

def test_sad2_strategic_silence():
    """
    SAD-2: Enron-сценарий.
    Обязательство раскрытия + данные есть в аналогичных компаниях +
    CFO уклоняется от вопроса о cash flow → ECT-3 INFERENTIAL
    """
    sad = SADProtocol()
    result = sad.analyze("cash flow от операций",
                         dv1_obligation=True,         # обязательство раскрытия по SEC
                         dv2_systematic=False,
                         dv3_exists_elsewhere=True,   # у конкурентов есть в отчётах
                         dv4_group_refusal=False,
                         dv5_pattern=True)            # CFO уклоняется при каждом вопросе
    assert result.sad_type == SADType.SAD2
    assert result.ect_signal == "ECT-3 INFERENTIAL"
    assert result.topic_map is True
    assert "SAD-2" in result.marker

def test_sad2_group_refusal():
    """SAD-2 GROUP: ≥3 источника отказали → групповое уклонение"""
    sad = SADProtocol()
    result = sad.analyze("показания сотрудников",
                         dv1_obligation=True, dv2_systematic=False,
                         dv3_exists_elsewhere=True,
                         dv4_group_refusal=True,   # 5 из 7 сотрудников отказали
                         dv5_pattern=False)
    assert result.sad_type == SADType.SAD2
    assert result.group_flag is True
    assert "GROUP" in result.marker

def test_sad2_systematic():
    """SAD-2: системное отсутствие → ECT-3 INFERENTIAL"""
    sad = SADProtocol()
    result = sad.analyze("все внутренние меморандумы",
                         dv1_obligation=False, dv2_systematic=True,
                         dv3_exists_elsewhere=False,
                         dv4_group_refusal=False, dv5_pattern=False)
    assert result.sad_type == SADType.SAD2
    assert result.ect_signal == "ECT-3 INFERENTIAL"


# ─── P46: NGI ─────────────────────────────────────────────────────────────────

def test_ngi_actions_low():
    """NGI LOW → никаких обязательных действий"""
    action = get_ngi_actions("LOW")
    assert action.raise_verification_bar is False
    assert action.hitl_before_exit is False
    assert action.declaration_required is False

def test_ngi_actions_moderate():
    """NGI MODERATE → повысить стандарт верификации"""
    action = get_ngi_actions("MODERATE")
    assert action.raise_verification_bar is True
    assert action.require_h1_falsification is False

def test_ngi_actions_high():
    """NGI HIGH → обязательная фальсификация H1 + IFM 7 дней"""
    action = get_ngi_actions("HIGH")
    assert action.require_h1_falsification is True
    assert action.ifm_checklist_days == 7
    assert action.hitl_before_exit is False

def test_ngi_actions_critical():
    """NGI CRITICAL (Ирак ОМУ-сценарий) → HITL перед EXIT + декларация"""
    action = get_ngi_actions("CRITICAL")
    assert action.hitl_before_exit is True
    assert action.declaration_required is True
    assert action.require_h1_falsification is True

def test_ngi_unknown_level_defaults_to_low():
    """Неизвестный уровень → LOW (безопасный дефолт)"""
    action = get_ngi_actions("UNKNOWN_LEVEL")
    assert action.level == "LOW"


# ─── P55: PPS ─────────────────────────────────────────────────────────────────

def test_pps_red_must_stop():
    """RED триггер → must_stop=True, top_priority = RED триггер"""
    result = pps_prioritize(["CDR1_DOWNGRADE", "EPISTEMIC_LOCK", "NGI_MODERATE"])
    assert result.must_stop is True
    assert result.top_priority == "EPISTEMIC_LOCK"
    assert "EPISTEMIC_LOCK" in result.red

def test_pps_orange_no_stop():
    """Только ORANGE триггеры → must_stop=False"""
    result = pps_prioritize(["SSC1_RECANTATION", "NGI_HIGH"])
    assert result.must_stop is False
    assert result.top_priority == "SSC1_RECANTATION"
    assert len(result.red) == 0

def test_pps_yellow_only():
    """Только YELLOW → обработать на неделе"""
    result = pps_prioritize(["SAD2_STRATEGIC", "CDR1_DOWNGRADE"])
    assert result.must_stop is False
    assert len(result.orange) == 0
    assert len(result.yellow) == 2

def test_pps_empty_triggers():
    """Нет триггеров → top_priority=None"""
    result = pps_prioritize([])
    assert result.top_priority is None
    assert result.must_stop is False

def test_pps_unknown_trigger_goes_orange():
    """Неизвестный триггер → ORANGE (консервативно)"""
    result = pps_prioritize(["SOME_FUTURE_PROTOCOL"])
    assert "SOME_FUTURE_PROTOCOL" in result.orange

def test_pps_multiple_red():
    """Несколько RED → первый в очереди становится top_priority"""
    triggers = ["ANI_CRITICAL", "EPISTEMIC_LOCK", "MPF_CRITICAL"]
    result = pps_prioritize(triggers)
    assert result.must_stop is True
    assert result.top_priority == "ANI_CRITICAL"


# ─── P56: OAS ─────────────────────────────────────────────────────────────────

def test_oas_log_creates_record():
    """OAS логирует запись с уникальным ID"""
    journal = OASJournal("INV-OAS-001")
    record = journal.log(
        event_type="SSC_EVENT",
        decision="Источник W-001 заморожен",
        basis=["SSC-1 рекантация", "показания адвоката"],
        protocol_used="P33",
        ect_level=None,
        challenge_condition="Если источник вернётся к исходным показаниям",
    )
    assert record.record_id is not None
    assert record.investigation_id == "INV-OAS-001"
    assert record.event_type == "SSC_EVENT"
    assert len(journal.records) == 1

def test_oas_multiple_records_append():
    """OAS — только append, порядок сохраняется"""
    journal = OASJournal("INV-OAS-002")
    for i in range(5):
        journal.log(f"EVENT-{i}", f"Решение {i}", [f"основание {i}"], f"P3{i}")
    assert len(journal.records) == 5
    assert journal.records[0].event_type == "EVENT-0"
    assert journal.records[4].event_type == "EVENT-4"

def test_oas_summary():
    """OAS summary возвращает корректную статистику"""
    journal = OASJournal("INV-OAS-003")
    journal.log("SSC", "заморожен", ["рекантация"], "P33")
    journal.log("FRCP", "арбитраж", ["критерий"], "P34")
    journal.log("SSC", "реактивирован", ["новые данные"], "P33")
    summary = journal.summary()
    assert summary["total_records"] == 3
    assert summary["by_protocol"]["P33"] == 2
    assert summary["by_protocol"]["P34"] == 1

def test_oas_get_by_type():
    """Фильтрация по типу события"""
    journal = OASJournal("INV-OAS-004")
    journal.log("SSC_EVENT", "д1", ["о1"], "P33")
    journal.log("NGI_CHECK", "д2", ["о2"], "P46")
    journal.log("SSC_EVENT", "д3", ["о3"], "P33")
    ssc_records = journal.get_by_type("SSC_EVENT")
    assert len(ssc_records) == 2


# ─── Интеграционный тест: GICore как фасад ────────────────────────────────────

def test_gicore_full_investigation_scenario():
    """
    Интеграционный сценарий: Уотергейт-паттерн.

    1. Источник "Глубокая глотка" даёт показания ECT-3
    2. SSC-2: он оказывается под давлением
    3. PPS расставляет приоритеты
    4. SAD-2: ключевые записи отсутствуют
    5. OAS фиксирует все решения
    """
    gi = GICore("INV-WATERGATE-2026")

    # 1. Источник
    deep_throat = make_source("DT-001", ect=ECTLevel.ECT3, ioi=0.1)

    # 2. SSC-2: арест / принуждение
    coercion = SSCEvent(
        event_type=SSCType.SSC2_COERCION,
        source_id="DT-001",
        timestamp=NOW,
        description="Агент ФБР получил предупреждение от Белого дома",
    )
    ssc_result = gi.ssc.apply(deep_throat, coercion)
    assert ssc_result.frozen is True
    assert ssc_result.trigger_frcp is True

    gi.oas.log(
        "SSC_COERCION",
        "DT-001 заморожен — возможное давление",
        ["SSC-2: предупреждение от Белого дома"],
        "P33",
        challenge_condition="Снять заморозку после повторного интервью без давления",
    )

    # 3. PPS: два триггера одновременно
    pps = gi.pps(["SSC2_COERCION", "NGI_HIGH"])
    assert pps.must_stop is False   # нет RED триггера
    assert "SSC2_COERCION" in pps.orange

    # 4. SAD: записи президента отсутствуют
    sad_result = gi.sad.analyze(
        topic="президентские диктофонные записи",
        dv1_obligation=True,          # конгресс потребовал
        dv2_systematic=False,
        dv3_exists_elsewhere=True,    # другие записи администрации есть
        dv4_group_refusal=False,
        dv5_pattern=True,             # Никсон уклоняется при каждом вопросе
    )
    assert sad_result.sad_type == SADType.SAD2
    assert sad_result.ect_signal == "ECT-3 INFERENTIAL"

    gi.oas.log(
        "SAD_ANALYSIS",
        "Отсутствие записей = ECT-3 INFERENTIAL",
        [sad_result.marker],
        "P45",
    )

    # 5. Проверяем OAS
    summary = gi.oas.summary()
    assert summary["total_records"] == 3   # SSC + PPS + SAD
    assert summary["by_protocol"]["P33"] == 1
    assert summary["by_protocol"]["P55"] == 1
    assert summary["by_protocol"]["P45"] == 1


# ─── Запуск ──────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    tests = [
        (name, fn) for name, fn in sorted(globals().items())
        if name.startswith("test_") and callable(fn)
    ]
    passed = failed = 0
    for name, fn in tests:
        try:
            fn()
            print(f"  ✅ {name}")
            passed += 1
        except Exception as e:
            import traceback
            print(f"  ❌ {name}: {e}")
            traceback.print_exc()
            failed += 1
    print(f"\n{'='*55}")
    print(f"Итого: {passed} прошли, {failed} упали из {passed+failed}")
    if failed:
        raise SystemExit(1)
