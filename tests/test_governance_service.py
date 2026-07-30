"""
tests/test_governance_service.py
=================================
Стресс-тест Module 2 (governance_service.py).

Использует фиктивные (mock) ответы классификатора — без сетевых вызовов.
Реальный ClaudeClassifierClient (Module 2b) не тестируется здесь: его
логика парсинга полностью покрыта через parse_classifier_response(),
а сетевой вызов anthropic.messages.create() не воспроизводим в песочнице
без доступа в интернет.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import json
from engine.governance_service import (
    GovernanceService,
    GovernanceRequest,
    ClassifierResponseError,
    parse_classifier_response,
    hallucinations_from_classifier,
)
from engine.gi_core import GICore


# ─── Fixtures: типовые ответы классификатора ─────────────────────────────────

def clean_response():
    return {
        "hallucinations": [],
        "ngi_dimensions": {
            "emotional": 0, "political": 0, "archetypal": 0, "industry": 0,
            "explanation": "Нейтральный технический текст без эмоциональной нагрузки.",
        },
        "eu_ai_act_signals": {"risk_tier": "minimal_risk", "violations": []},
        "business_rule_violations": [],
    }

def critical_hallucination_response():
    return {
        "hallucinations": [
            {
                "type": "TYPE-1",
                "severity_signal": "CRITICAL",
                "description": "Сослался на несуществующее судебное решение",
                "evidence": "Согласно решению Верховного суда №12345/2025",
                "rule_violated": None,
            }
        ],
        "ngi_dimensions": {
            "emotional": 1, "political": 0, "archetypal": 0, "industry": 2,
            "explanation": "Юридическая тема повышает отраслевую значимость.",
        },
        "eu_ai_act_signals": {"risk_tier": "high_risk", "violations": ["Article 9 non-compliance risk"]},
        "business_rule_violations": [],
    }

def markdown_fenced_response():
    """Классификатор иногда всё равно оборачивает JSON в ```json fences,
    несмотря на инструкцию 'только JSON'. Парсер должен это пережить."""
    return "```json\n" + json.dumps(clean_response()) + "\n```"


# ─── parse_classifier_response ────────────────────────────────────────────

def test_parse_valid_dict():
    """Валидный dict проходит без ошибок"""
    data = parse_classifier_response(clean_response())
    assert data["hallucinations"] == []

def test_parse_valid_json_string():
    """Валидная JSON-строка парсится"""
    raw = json.dumps(clean_response())
    data = parse_classifier_response(raw)
    assert data["ngi_dimensions"]["emotional"] == 0

def test_parse_strips_markdown_fences():
    """```json fences вокруг ответа — не ломают парсинг"""
    data = parse_classifier_response(markdown_fenced_response())
    assert data["hallucinations"] == []

def test_parse_invalid_json_raises():
    """Битый JSON → ClassifierResponseError, не JSONDecodeError наружу"""
    try:
        parse_classifier_response("{невалидный json")
        assert False, "должно было упасть"
    except ClassifierResponseError:
        pass

def test_parse_missing_required_key_raises():
    """Отсутствие обязательного ключа контракта → ошибка"""
    broken = clean_response()
    del broken["eu_ai_act_signals"]
    try:
        parse_classifier_response(broken)
        assert False, "должно было упасть"
    except ClassifierResponseError as e:
        assert "eu_ai_act_signals" in str(e)

def test_parse_invalid_hallucination_type_raises():
    """TYPE-99 (несуществующий тип) → ошибка"""
    broken = clean_response()
    broken["hallucinations"] = [{
        "type": "TYPE-99", "severity_signal": "LOW",
        "description": "d", "evidence": "e", "rule_violated": None,
    }]
    try:
        parse_classifier_response(broken)
        assert False, "должно было упасть"
    except ClassifierResponseError as e:
        assert "TYPE-99" in str(e)

def test_parse_contract_violation_confidence_number():
    """
    Критично: если классификатор нарушит контракт РАЗДЕЛ 16 и вернёт
    число 'confidence' сам (вместо того чтобы это считал Python) —
    это должно быть поймано, а не тихо проигнорировано.
    """
    broken = clean_response()
    broken["hallucinations"] = [{
        "type": "TYPE-3", "severity_signal": "LOW",
        "description": "d", "evidence": "e", "rule_violated": None,
        "confidence": 0.87,   # ← LLM самовольно посчитал число — запрещено
    }]
    try:
        parse_classifier_response(broken)
        assert False, "должно было упасть — контракт нарушен"
    except ClassifierResponseError as e:
        assert "confidence" in str(e)

def test_parse_ngi_out_of_range_raises():
    """NGI измерение вне диапазона 0-3 → ошибка"""
    broken = clean_response()
    broken["ngi_dimensions"]["emotional"] = 5
    try:
        parse_classifier_response(broken)
        assert False, "должно было упасть"
    except ClassifierResponseError:
        pass

def test_parse_invalid_eu_tier_raises():
    """Несуществующий EU AI Act tier → ошибка"""
    broken = clean_response()
    broken["eu_ai_act_signals"]["risk_tier"] = "extreme_risk"  # не существует
    try:
        parse_classifier_response(broken)
        assert False, "должно было упасть"
    except ClassifierResponseError:
        pass


# ─── hallucinations_from_classifier ───────────────────────────────────────

def test_hallucinations_conversion():
    """Корректная конвертация dict → Hallucination dataclass"""
    data = critical_hallucination_response()
    halls = hallucinations_from_classifier(data)
    assert len(halls) == 1
    assert halls[0].type == "TYPE-1"
    assert halls[0].severity == "CRITICAL"

def test_hallucinations_empty_list():
    """Пустой список галлюцинаций → пустой список объектов"""
    halls = hallucinations_from_classifier(clean_response())
    assert halls == []


# ─── GovernanceService.evaluate — интеграция ──────────────────────────────

def test_service_clean_input_passes():
    """Чистый вывод → PASS, OAS-запись создана"""
    gi = GICore("TEST-SVC-001")
    service = GovernanceService(gi)
    req = GovernanceRequest(ai_output="Столица Франции — Париж.")
    result = service.evaluate(req, clean_response())

    assert result.math_result.decision.decision == "PASS"
    assert result.oas_record is not None
    assert len(gi.oas.records) == 1

def test_service_critical_hallucination_blocks():
    """TYPE-1 CRITICAL в block_on_types → BLOCK"""
    gi = GICore("TEST-SVC-002")
    service = GovernanceService(gi)
    req = GovernanceRequest(
        ai_output="Согласно решению Верховного суда №12345/2025...",
        context_type="customer_facing",
        block_on_types=["TYPE-1", "TYPE-7"],
    )
    result = service.evaluate(req, critical_hallucination_response())

    assert result.math_result.decision.decision == "BLOCK"
    assert result.math_result.decision.block_source == "HALLUCINATION_BLOCK_RULE"
    assert "12345" in result.math_result.hallucinations[0].evidence

def test_service_not_in_block_list_does_not_block():
    """Та же TYPE-1 галлюцинация, но НЕ в block_on_types → не BLOCK по этой причине"""
    gi = GICore("TEST-SVC-003")
    service = GovernanceService(gi)
    req = GovernanceRequest(
        ai_output="...",
        block_on_types=["TYPE-7"],  # TYPE-1 не блокируется явно
    )
    result = service.evaluate(req, critical_hallucination_response())
    # CRITICAL severity всё равно даст низкий confidence → может уйти в HITL,
    # но НЕ через HALLUCINATION_BLOCK_RULE
    assert result.math_result.decision.block_source != "HALLUCINATION_BLOCK_RULE"

def test_service_oas_logged_with_correct_basis():
    """OAS-запись содержит реальные метрики решения, не пустышку"""
    gi = GICore("TEST-SVC-004")
    service = GovernanceService(gi)
    req = GovernanceRequest(ai_output="test")
    result = service.evaluate(req, clean_response())

    record = gi.oas.records[0]
    assert record.protocol_used == "GOVERNANCE-MATH"
    assert any("confidence=" in b for b in record.basis)
    assert any("ciri=" in b for b in record.basis)

def test_service_string_json_input_works():
    """evaluate() принимает как dict, так и сырую JSON-строку"""
    gi = GICore("TEST-SVC-005")
    service = GovernanceService(gi)
    req = GovernanceRequest(ai_output="test")
    raw_string = json.dumps(clean_response())
    result = service.evaluate(req, raw_string)
    assert result.math_result.decision.decision == "PASS"

def test_service_markdown_fenced_input_works():
    """evaluate() переживает markdown-fenced ответ классификатора"""
    gi = GICore("TEST-SVC-006")
    service = GovernanceService(gi)
    req = GovernanceRequest(ai_output="test")
    result = service.evaluate(req, markdown_fenced_response())
    assert result.math_result.decision.decision == "PASS"

def test_service_multiple_calls_accumulate_oas():
    """Несколько вызовов evaluate() на одном GICore → OAS растёт, не перезаписывается"""
    gi = GICore("TEST-SVC-007")
    service = GovernanceService(gi)
    req = GovernanceRequest(ai_output="test")
    service.evaluate(req, clean_response())
    service.evaluate(req, clean_response())
    service.evaluate(req, critical_hallucination_response())
    assert len(gi.oas.records) == 3

def test_service_eu_high_risk_surfaces_in_response():
    """EU AI Act high_risk из классификатора попадает в API-ответ"""
    gi = GICore("TEST-SVC-008")
    service = GovernanceService(gi)
    req = GovernanceRequest(ai_output="test")
    result = service.evaluate(req, critical_hallucination_response())
    api_resp = service.to_api_response(result)
    assert "Article 9 non-compliance risk" in api_resp["eu_ai_act_violations"]


# ─── to_api_response — сериализация ───────────────────────────────────────

def test_to_api_response_shape():
    """API-ответ содержит все обязательные поля для фронтенда"""
    gi = GICore("TEST-SVC-009")
    service = GovernanceService(gi)
    req = GovernanceRequest(ai_output="test")
    result = service.evaluate(req, clean_response())
    api_resp = service.to_api_response(result)

    required_keys = {
        "decision", "decision_reason", "block_source",
        "confidence_score", "confidence_level",
        "rpl_factor", "rpl_blocked_ect4",
        "ngi", "ciri", "hallucinations",
        "eu_ai_act_violations", "business_rule_violations",
        "oas_record_id", "context_type",
    }
    assert required_keys.issubset(api_resp.keys())

def test_to_api_response_json_serializable():
    """API-ответ должен быть json.dumps()-совместим без ошибок (для HTTP)"""
    gi = GICore("TEST-SVC-010")
    service = GovernanceService(gi)
    req = GovernanceRequest(ai_output="test")
    result = service.evaluate(req, critical_hallucination_response())
    api_resp = service.to_api_response(result)
    serialized = json.dumps(api_resp, ensure_ascii=False)  # не должно упасть
    assert "TYPE-1" in serialized


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
