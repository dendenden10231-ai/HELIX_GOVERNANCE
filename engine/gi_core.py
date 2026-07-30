"""
engine/gi_core.py
=================
HELIX Module 1 — GI v6.2 Core Engine

Источник: GI_v6_2_COMPLETE.docx
Реализует 7 базовых протоколов которые используют ОБА продукта:
  GOVERNANCE (через governance_math.py) и INTELLIGENCE (через intelligence_engine.py)

Протоколы:
  P33 — SSC: Source Status Change        (смена статуса источника)
  P34 — FRCP: Fact Reconciliation        (разрешение конфликта ECT-4)
  P35 — CDR: Cascade Downgrade Rules     (каскадное понижение ECT)
  P45 — SAD: Silence As Data             (молчание как данные)
  P46 — NGI: Narrative Gravity Index     (нарративная гравитация)
  P55 — PPS: Protocol Priority Stack     (приоритет при множественных триггерах)
  P56 — OAS: Operational Audit System    (журнал аудита решений)

Архитектурный принцип:
  gi_core.py = детерминированное ядро
  governance_math.py использует NGIResult из этого файла
  intelligence_engine.py (следующий модуль) использует SSC, FRCP, CDR, SAD
  Оба продукта пишут в OASJournal
"""

from __future__ import annotations

import uuid
from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Dict, List, Optional


# ─── ECT-уровни ──────────────────────────────────────────────────────────────

class ECTLevel(int, Enum):
    """
    Evidence Confidence Threshold.
    Значение как int позволяет сравнивать: ECTLevel.ECT3 > ECTLevel.ECT1
    """
    ECT1 = 1   # неверифицированное / AI-вывод по умолчанию
    ECT2 = 2   # верифицируемо из одного источника
    ECT3 = 3   # перекрёстно верифицировано
    ECT4 = 4   # задокументировано первичными источниками

    @classmethod
    def from_int(cls, n: int) -> "ECTLevel":
        n = max(1, min(4, n))
        return cls(n)

    def downgrade(self) -> "ECTLevel":
        """Понизить на 1 уровень, не ниже ECT1."""
        return ECTLevel.from_int(self.value - 1)

    def __str__(self) -> str:
        return f"ECT-{self.value}"


ECT_FROZEN = "ECT-FROZEN"   # особый статус при SSC-1/2


# ─── P33: SSC — Source Status Change ─────────────────────────────────────────

class SSCType(str, Enum):
    SSC1_RECANTATION        = "SSC-1"   # источник отозвал показания
    SSC2_COERCION           = "SSC-2"   # принуждение / арест
    SSC3_DEATH              = "SSC-3"   # смерть источника
    SSC4_HIDDEN_LINK        = "SSC-4"   # раскрыта скрытая связь
    SSC5_REACTIVATION       = "SSC-5"   # источник реактивирован


@dataclass
class Source:
    """Источник в расследовании."""
    source_id:   str
    name:        str
    ect_level:   ECTLevel = ECTLevel.ECT2
    frozen:      bool = False
    ssc_events:  List["SSCEvent"] = field(default_factory=list)
    ioi_score:   float = 0.0   # Index of Interest [0.0–1.0]


@dataclass
class SSCEvent:
    """Событие смены статуса источника (P33)."""
    event_type:   SSCType
    source_id:    str
    timestamp:    datetime
    description:  str
    affected_facts: List[str] = field(default_factory=list)  # список fact_id


@dataclass
class SSCResult:
    """Результат применения SSC-протокола к источнику."""
    source_id:        str
    event_type:       SSCType
    frozen:           bool
    previous_ect:     ECTLevel
    new_ect:          Optional[ECTLevel]   # None если frozen
    marker:           str
    trigger_frcp:     bool   # нужно ли запустить FRCP
    trigger_cdr:      bool   # нужно ли запустить CDR


class SSCProtocol:
    """
    P33 — Протокол смены статуса источника.

    При изменении статуса источника все ECT-маркеры опирающиеся
    на него подлежат пересмотру. Активирует CDR и/или FRCP.
    """

    def apply(self, source: Source, event: SSCEvent) -> SSCResult:
        prev_ect = source.ect_level
        frozen = False
        new_ect = prev_ect
        trigger_frcp = False
        trigger_cdr = False

        if event.event_type in (SSCType.SSC1_RECANTATION, SSCType.SSC2_COERCION):
            # Заморозить — показания могут быть скомпрометированы
            frozen = True
            new_ect = None
            trigger_frcp = True   # P34 разрешает конфликт
            marker = (f"[{event.event_type.value}: {event.timestamp.date()}, "
                      f"источник {source.source_id}, ECT-FROZEN]")

        elif event.event_type == SSCType.SSC3_DEATH:
            # Перекрёстная верификация невозможна → понизить на 1
            new_ect = prev_ect.downgrade()
            trigger_cdr = True    # P35 каскадирует понижение
            marker = (f"[SSC-3: {event.timestamp.date()}, "
                      f"источник {source.source_id}, CDR активирован, "
                      f"{prev_ect} → {new_ect}]")

        elif event.event_type == SSCType.SSC4_HIDDEN_LINK:
            # Скрытая связь → ICoI пересчитать, понизить ECT
            new_ect = prev_ect.downgrade()
            trigger_cdr = True
            marker = (f"[SSC-4: {event.timestamp.date()}, "
                      f"источник {source.source_id}, скрытая связь раскрыта, "
                      f"{prev_ect} → {new_ect}]")

        elif event.event_type == SSCType.SSC5_REACTIVATION:
            # Реактивация — снять заморозку если была
            frozen = False
            marker = (f"[SSC-5: {event.timestamp.date()}, "
                      f"источник {source.source_id}, реактивирован, "
                      f"требуется повторное интервью]")

        else:
            marker = f"[SSC: unknown event {event.event_type}]"

        # Применяем к источнику
        source.frozen = frozen
        if new_ect is not None:
            source.ect_level = new_ect
        source.ssc_events.append(event)

        return SSCResult(
            source_id=source.source_id,
            event_type=event.event_type,
            frozen=frozen,
            previous_ect=prev_ect,
            new_ect=new_ect,
            marker=marker,
            trigger_frcp=trigger_frcp,
            trigger_cdr=trigger_cdr,
        )


# ─── P34: FRCP — Fact Reconciliation & Conflict Protocol ─────────────────────

@dataclass
class Fact:
    """Факт в расследовании."""
    fact_id:     str
    description: str
    ect_level:   ECTLevel
    source_ids:  List[str] = field(default_factory=list)
    timestamp:   Optional[datetime] = None   # когда возник факт
    falsification_attempted: bool = False    # была ли попытка фальсификации


@dataclass
class FRCPResult:
    """Результат арбитража конфликта ECT-4 (P34)."""
    winner_fact_id:   str
    loser_fact_id:    str
    winner_criteria:  List[str]     # которые выиграл победитель
    loser_new_ect:    ECTLevel      # ECT-3 после проигрыша
    resolved:         bool
    marker:           str
    non_liquet:       bool = False  # True если неразрешимо


class FRCPProtocol:
    """
    P34 — Протокол разрешения конфликта ECT-4.

    Когда два факта ECT-4 прямо противоречат друг другу —
    4 критерия арбитража применяются последовательно.
    Ничья или неразрешимость → NON LIQUET.
    """

    def arbitrate(
        self,
        fact_a: Fact,
        fact_b: Fact,
        sources: Dict[str, Source],
    ) -> FRCPResult:
        """
        Арбитраж между двумя конфликтующими фактами ECT-4.

        Критерии (P34):
          1. ПЕРВИЧНОСТЬ  — ближе к событию по времени
          2. НЕЗАВИСИМОСТЬ — Independence Vector источника
          3. ФАЛЬСИФИЦИРУЕМОСТЬ — прошёл попытку фальсификации и устоял
          4. ФИЗИЧЕСКАЯ ВОЗМОЖНОСТЬ — хронологически возможен

        Победитель по большинству критериев → ECT-4 сохраняется.
        Проигравший → понижается до ECT-3.
        """
        scores = {fact_a.fact_id: 0, fact_b.fact_id: 0}
        winner_criteria_a = []
        winner_criteria_b = []

        # Критерий 1: Первичность (дата факта)
        if fact_a.timestamp and fact_b.timestamp:
            if fact_a.timestamp < fact_b.timestamp:
                scores[fact_a.fact_id] += 1
                winner_criteria_a.append("ПЕРВИЧНОСТЬ")
            elif fact_b.timestamp < fact_a.timestamp:
                scores[fact_b.fact_id] += 1
                winner_criteria_b.append("ПЕРВИЧНОСТЬ")

        # Критерий 2: Независимость (средний ICoI источников — ниже = независимее)
        def avg_independence(fact: Fact) -> float:
            src_list = [sources[sid] for sid in fact.source_ids if sid in sources]
            if not src_list:
                return 0.5
            return 1.0 - (sum(s.ioi_score for s in src_list) / len(src_list))

        ind_a = avg_independence(fact_a)
        ind_b = avg_independence(fact_b)
        if abs(ind_a - ind_b) > 0.05:
            if ind_a > ind_b:
                scores[fact_a.fact_id] += 1
                winner_criteria_a.append("НЕЗАВИСИМОСТЬ")
            else:
                scores[fact_b.fact_id] += 1
                winner_criteria_b.append("НЕЗАВИСИМОСТЬ")

        # Критерий 3: Фальсифицируемость
        if fact_a.falsification_attempted and not fact_b.falsification_attempted:
            scores[fact_a.fact_id] += 1
            winner_criteria_a.append("ФАЛЬСИФИЦИРУЕМОСТЬ")
        elif fact_b.falsification_attempted and not fact_a.falsification_attempted:
            scores[fact_b.fact_id] += 1
            winner_criteria_b.append("ФАЛЬСИФИЦИРУЕМОСТЬ")

        # Критерий 4: Физическая возможность — проверяем через временной порядок
        # (полная интеграция с TIE P48 — следующий модуль)
        # Здесь: базовая проверка что факт не опережает само событие
        # Placeholder — TIE будет подключён отдельно
        # scores не меняем если оба физически возможны

        # Итог
        score_a = scores[fact_a.fact_id]
        score_b = scores[fact_b.fact_id]

        if score_a == score_b:
            return FRCPResult(
                winner_fact_id=fact_a.fact_id,
                loser_fact_id=fact_b.fact_id,
                winner_criteria=[],
                loser_new_ect=fact_b.ect_level,
                resolved=False,
                non_liquet=True,
                marker=(f"[FRCP NON LIQUET: факты {fact_a.fact_id} и {fact_b.fact_id} "
                        f"неразрешимы ({score_a}:{score_b}), HITL обязателен]"),
            )

        if score_a > score_b:
            fact_b.ect_level = ECTLevel.ECT3
            return FRCPResult(
                winner_fact_id=fact_a.fact_id,
                loser_fact_id=fact_b.fact_id,
                winner_criteria=winner_criteria_a,
                loser_new_ect=ECTLevel.ECT3,
                resolved=True,
                marker=(f"[FRCP RESOLVED: {fact_a.fact_id} победил ({winner_criteria_a}), "
                        f"{fact_b.fact_id} → ECT-3]"),
            )
        else:
            fact_a.ect_level = ECTLevel.ECT3
            return FRCPResult(
                winner_fact_id=fact_b.fact_id,
                loser_fact_id=fact_a.fact_id,
                winner_criteria=winner_criteria_b,
                loser_new_ect=ECTLevel.ECT3,
                resolved=True,
                marker=(f"[FRCP RESOLVED: {fact_b.fact_id} победил ({winner_criteria_b}), "
                        f"{fact_a.fact_id} → ECT-3]"),
            )


# ─── P35: CDR — Cascade Downgrade Rules ──────────────────────────────────────

class CDRType(str, Enum):
    CDR1 = "CDR-1"    # прямая зависимость → понизить автоматически
    CDR2A = "CDR-2а"  # частичная зависимость с документом
    CDR2B = "CDR-2б"  # частичная зависимость, Exception Pathway
    CDR3 = "CDR-3"    # косвенная зависимость → мониторинг


@dataclass
class CDRResult:
    """Результат каскадного понижения (P35)."""
    fact_id:      str
    cdr_type:     CDRType
    previous_ect: ECTLevel
    new_ect:      ECTLevel
    source_removed: Optional[str]
    marker:       str
    monitor_only: bool   # True для CDR-3


class CDRProtocol:
    """
    P35 — Каскадное понижение ECT.

    При дисквалификации источника — трёхуровневый каскад
    для всех фактов которые на него опирались.
    """

    def apply(
        self,
        fact: Fact,
        disqualified_source_id: str,
        sources: Dict[str, Source],
        exception_group_size: int = 0,
    ) -> CDRResult:
        """
        Args:
            fact: факт который нужно пересмотреть
            disqualified_source_id: ID дисквалифицированного источника
            sources: все источники расследования
            exception_group_size: размер группы ECT-4 EXCEPTION (для CDR-2б)
        """
        prev = fact.ect_level
        depends_on_disq = disqualified_source_id in fact.source_ids
        other_sources = [sid for sid in fact.source_ids if sid != disqualified_source_id]
        has_document = any(
            sources.get(sid) and sources[sid].ioi_score < 0.2
            for sid in other_sources
        )

        if not depends_on_disq:
            # Косвенная зависимость — только мониторинг
            return CDRResult(
                fact_id=fact.fact_id,
                cdr_type=CDRType.CDR3,
                previous_ect=prev,
                new_ect=prev,
                source_removed=None,
                marker=f"[CDR-3: косвенная зависимость {fact.fact_id}, мониторинг]",
                monitor_only=True,
            )

        if len(fact.source_ids) == 1:
            # Единственный источник дисквалифицирован → CDR-1
            fact.ect_level = prev.downgrade()
            return CDRResult(
                fact_id=fact.fact_id,
                cdr_type=CDRType.CDR1,
                previous_ect=prev,
                new_ect=fact.ect_level,
                source_removed=disqualified_source_id,
                marker=(f"[CDR-1: прямая зависимость, источник {disqualified_source_id}, "
                        f"{prev} → {fact.ect_level}]"),
                monitor_only=False,
            )

        if has_document:
            # Есть документ-подтверждение → CDR-2а, убрать источник из цепочки
            fact.source_ids.remove(disqualified_source_id)
            return CDRResult(
                fact_id=fact.fact_id,
                cdr_type=CDRType.CDR2A,
                previous_ect=prev,
                new_ect=prev,  # ECT сохраняется если документ тянет
                source_removed=disqualified_source_id,
                marker=(f"[CDR-2а: SOURCE REMOVED FROM {fact.fact_id}, "
                        f"документ сохраняет {prev}]"),
                monitor_only=False,
            )

        # Exception Pathway — CDR-2б
        if exception_group_size > 0:
            remaining = exception_group_size - 1
            if remaining < 3:
                fact.ect_level = ECTLevel.ECT3
                return CDRResult(
                    fact_id=fact.fact_id,
                    cdr_type=CDRType.CDR2B,
                    previous_ect=prev,
                    new_ect=ECTLevel.ECT3,
                    source_removed=disqualified_source_id,
                    marker=(f"[CDR-2б: ОДИН ИСТОЧНИК УДАЛЁН, "
                            f"новый статус группы: {remaining}, "
                            f"ECT-4 EXCEPTION аннулирован → ECT-3]"),
                    monitor_only=False,
                )
            return CDRResult(
                fact_id=fact.fact_id,
                cdr_type=CDRType.CDR2B,
                previous_ect=prev,
                new_ect=prev,
                source_removed=disqualified_source_id,
                marker=(f"[CDR-2б: ОДИН ИСТОЧНИК УДАЛЁН, "
                        f"новый статус группы: {remaining}, ECT-4 сохранён]"),
                monitor_only=False,
            )

        # Нет документа и нет Exception группы → CDR-1
        fact.ect_level = prev.downgrade()
        return CDRResult(
            fact_id=fact.fact_id,
            cdr_type=CDRType.CDR1,
            previous_ect=prev,
            new_ect=fact.ect_level,
            source_removed=disqualified_source_id,
            marker=(f"[CDR-1: прямая зависимость, источник {disqualified_source_id}, "
                    f"{prev} → {fact.ect_level}]"),
            monitor_only=False,
        )


# ─── P45: SAD — Silence As Data ───────────────────────────────────────────────

class SADType(str, Enum):
    SAD0 = "SAD-0"   # случайное отсутствие — не значимо
    SAD1 = "SAD-1"   # техническое отсутствие
    SAD2 = "SAD-2"   # стратегическое молчание → ECT-3 INFERENTIAL


@dataclass
class SADResult:
    """Результат анализа молчания (P45)."""
    topic:        str
    sad_type:     SADType
    ect_signal:   Optional[str]   # "ECT-3 INFERENTIAL" для SAD-2, None для SAD-0
    marker:       str
    dv_answers:   Dict[str, bool] = field(default_factory=dict)  # ДВ-1..ДВ-5
    group_flag:   bool = False    # SAD-2 GROUP если ДВ-4
    topic_map:    bool = False    # SAD TOPIC MAP если ДВ-5


class SADProtocol:
    """
    P45 — Silence As Data.

    Типология молчания и 5 диагностических вопросов.
    SAD-2 → ECT-3 INFERENTIAL (не ECT-4, даже если паттерн очевиден).
    """

    def analyze(
        self,
        topic: str,
        dv1_obligation: bool,       # было ли обязательство документирования
        dv2_systematic: bool,       # системное отсутствие класса данных
        dv3_exists_elsewhere: bool, # в аналогичных контекстах данные существуют
        dv4_group_refusal: bool,    # ≥3 источника из одной среды отказали
        dv5_pattern: bool,          # паттерн уклонения на конкретный вопрос
        technical_reason: Optional[str] = None,
    ) -> SADResult:
        """
        5 диагностических вопросов определяют тип SAD.

        ДВ-1: обязательство документирования
        ДВ-2: системное (весь класс данных)
        ДВ-3: в аналогичных контекстах существует
        ДВ-4: групповое уклонение (≥3 источника)
        ДВ-5: паттерн на конкретный вопрос
        """
        dv = {
            "ДВ-1": dv1_obligation,
            "ДВ-2": dv2_systematic,
            "ДВ-3": dv3_exists_elsewhere,
            "ДВ-4": dv4_group_refusal,
            "ДВ-5": dv5_pattern,
        }

        # Нет обязательства и не системное → SAD-0
        if not dv1_obligation and not dv2_systematic:
            return SADResult(
                topic=topic,
                sad_type=SADType.SAD0,
                ect_signal=None,
                marker=f"[SAD-0: отсутствие данных по '{topic}' — не значимо]",
                dv_answers=dv,
            )

        # Техническая причина есть → SAD-1
        if technical_reason:
            return SADResult(
                topic=topic,
                sad_type=SADType.SAD1,
                ect_signal=None,
                marker=f"[SAD-1: техническое отсутствие '{topic}' — верифицировать: {technical_reason}]",
                dv_answers=dv,
            )

        # Обязательство + данные есть в аналогичных контекстах → SAD-2
        if dv1_obligation and dv3_exists_elsewhere:
            group_flag  = dv4_group_refusal
            topic_map   = dv5_pattern
            extra = ""
            if group_flag:
                extra += " [SAD-2 GROUP: групповое уклонение]"
            if topic_map:
                extra += f" [SAD TOPIC MAP: тема '{topic}']"
            return SADResult(
                topic=topic,
                sad_type=SADType.SAD2,
                ect_signal="ECT-3 INFERENTIAL",
                marker=f"[SAD-2: стратегическое молчание '{topic}' — ECT-3 INFERENTIAL]{extra}",
                dv_answers=dv,
                group_flag=group_flag,
                topic_map=topic_map,
            )

        # Системное отсутствие без технической причины → SAD-2
        if dv2_systematic:
            return SADResult(
                topic=topic,
                sad_type=SADType.SAD2,
                ect_signal="ECT-3 INFERENTIAL",
                marker=f"[SAD-2: системное молчание '{topic}' — ECT-3 INFERENTIAL]",
                dv_answers=dv,
            )

        # По умолчанию — SAD-1 (требует уточнения)
        return SADResult(
            topic=topic,
            sad_type=SADType.SAD1,
            ect_signal=None,
            marker=f"[SAD-1: неопределённое отсутствие '{topic}' — верифицировать]",
            dv_answers=dv,
        )


# ─── P46: NGI — Narrative Gravity Index ──────────────────────────────────────
# Математика NGI живёт в governance_math.py (HelixGovernanceMath.calculate_ngi_score)
# Здесь: действия которые NGI-уровень требует от GI Engine

@dataclass
class NGIAction:
    """Обязательные действия по уровню NGI (P46)."""
    level:                    str
    raise_verification_bar:   bool    # повысить стандарт верификации на 1 ECT
    require_h1_falsification: bool    # обязательная фальсификация H1
    ifm_checklist_days:       int     # сколько дней IFM-чеклист
    hitl_before_exit:         bool    # HITL перед публикацией
    declaration_required:     bool    # декларация о независимости

NGI_ACTIONS: Dict[str, NGIAction] = {
    "LOW": NGIAction(
        level="LOW",
        raise_verification_bar=False,
        require_h1_falsification=False,
        ifm_checklist_days=0,
        hitl_before_exit=False,
        declaration_required=False,
    ),
    "MODERATE": NGIAction(
        level="MODERATE",
        raise_verification_bar=True,   # +1 ECT-уровень требования
        require_h1_falsification=False,
        ifm_checklist_days=0,
        hitl_before_exit=False,
        declaration_required=False,
    ),
    "HIGH": NGIAction(
        level="HIGH",
        raise_verification_bar=True,
        require_h1_falsification=True,  # обязательна фальсификация H1
        ifm_checklist_days=7,
        hitl_before_exit=False,
        declaration_required=False,
    ),
    "CRITICAL": NGIAction(
        level="CRITICAL",
        raise_verification_bar=True,
        require_h1_falsification=True,
        ifm_checklist_days=7,
        hitl_before_exit=True,          # HITL перед EXIT PROTOCOL
        declaration_required=True,      # декларация о независимости в публикации
    ),
}


def get_ngi_actions(ngi_level: str) -> NGIAction:
    """Получить обязательные действия для данного NGI-уровня."""
    return NGI_ACTIONS.get(ngi_level.upper(), NGI_ACTIONS["LOW"])


# ─── P55: PPS — Protocol Priority Stack ──────────────────────────────────────

class PPSLevel(str, Enum):
    RED    = "RED"     # немедленная остановка
    ORANGE = "ORANGE"  # обработать сегодня
    YELLOW = "YELLOW"  # обработать на этой неделе


# Карта триггеров → уровень PPS
PPS_TRIGGER_MAP: Dict[str, PPSLevel] = {
    "EPISTEMIC_LOCK":          PPSLevel.RED,
    "IFM5_CRITICAL":           PPSLevel.RED,
    "ANI_CRITICAL":            PPSLevel.RED,
    "MPF_CRITICAL":            PPSLevel.RED,
    "TIE1_IMPOSSIBLE_WINDOW":  PPSLevel.RED,
    "ECT_CONFLICT_UNRESOLVED": PPSLevel.RED,

    "SSC1_RECANTATION":        PPSLevel.ORANGE,
    "SSC2_COERCION":           PPSLevel.ORANGE,
    "FRCP_ARBITRATION":        PPSLevel.ORANGE,
    "NGI_HIGH":                PPSLevel.ORANGE,
    "CHF_D_ACTIVE":            PPSLevel.ORANGE,
    "IFM3_WARNING":            PPSLevel.ORANGE,
    "TELP_ACTIVE":             PPSLevel.ORANGE,

    "CDR1_DOWNGRADE":          PPSLevel.YELLOW,
    "SAD2_STRATEGIC":          PPSLevel.YELLOW,
    "NGI_MODERATE":            PPSLevel.YELLOW,
    "SSC3_DEATH":              PPSLevel.YELLOW,
    "SSC4_HIDDEN_LINK":        PPSLevel.YELLOW,
    "PDE_DECAY":               PPSLevel.YELLOW,
}


@dataclass
class PPSResult:
    """Результат расстановки приоритетов (P55)."""
    triggers:   List[str]
    red:        List[str]
    orange:     List[str]
    yellow:     List[str]
    top_priority: Optional[str]     # первый RED если есть
    must_stop:    bool              # True если есть RED


def pps_prioritize(active_triggers: List[str]) -> PPSResult:
    """
    P55 — Расставить приоритеты при множественных триггерах.

    RED: немедленная остановка всего остального.
    ORANGE: обработать сегодня.
    YELLOW: обработать на этой неделе.
    """
    red    = [t for t in active_triggers if PPS_TRIGGER_MAP.get(t) == PPSLevel.RED]
    orange = [t for t in active_triggers if PPS_TRIGGER_MAP.get(t) == PPSLevel.ORANGE]
    yellow = [t for t in active_triggers if PPS_TRIGGER_MAP.get(t) == PPSLevel.YELLOW]
    unknown = [t for t in active_triggers if t not in PPS_TRIGGER_MAP]

    # Неизвестные триггеры → ORANGE по умолчанию (консервативно)
    orange.extend(unknown)

    return PPSResult(
        triggers=active_triggers,
        red=red,
        orange=orange,
        yellow=yellow,
        top_priority=red[0] if red else (orange[0] if orange else None),
        must_stop=len(red) > 0,
    )


# ─── P56: OAS — Operational Audit System ─────────────────────────────────────

@dataclass
class OASRecord:
    """
    Единица журнала аудита (P56).

    OAS фиксирует РЕШЕНИЯ и их основания — не статус фактов.
    'Факт ECT-4' — это результат.
    OAS-запись — это ПОЧЕМУ он ECT-4, КОГДА, и ЧТО может изменить решение.
    """
    record_id:         str
    timestamp:         datetime
    event_type:        str         # тип события (SSC, FRCP, CDR, SAD, NGI, DECISION...)
    investigation_id:  str

    decision:          str         # что именно решено
    basis:             List[str]   # на каком основании (факты, протоколы)
    protocol_used:     str         # P33, P34, P35, P45, P46, P55...
    ect_level:         Optional[int] = None

    can_be_challenged: bool = True
    challenge_condition: Optional[str] = None   # что нужно для пересмотра
    investigator_id:   Optional[str] = None


class OASJournal:
    """
    P56 — Журнал аудита решений.

    Оба продукта (GOVERNANCE и INTELLIGENCE) пишут сюда.
    Неизменяемый лог — только append.
    """

    def __init__(self, investigation_id: str):
        self.investigation_id = investigation_id
        self._records: List[OASRecord] = []

    def log(
        self,
        event_type:         str,
        decision:           str,
        basis:              List[str],
        protocol_used:      str,
        ect_level:          Optional[int] = None,
        challenge_condition: Optional[str] = None,
        investigator_id:    Optional[str] = None,
    ) -> OASRecord:
        """Добавить запись в журнал. Возвращает запись."""
        record = OASRecord(
            record_id=str(uuid.uuid4())[:8],
            timestamp=datetime.now(timezone.utc),
            event_type=event_type,
            investigation_id=self.investigation_id,
            decision=decision,
            basis=basis,
            protocol_used=protocol_used,
            ect_level=ect_level,
            challenge_condition=challenge_condition,
            investigator_id=investigator_id,
        )
        self._records.append(record)
        return record

    @property
    def records(self) -> List[OASRecord]:
        return list(self._records)

    def get_by_type(self, event_type: str) -> List[OASRecord]:
        return [r for r in self._records if r.event_type == event_type]

    def summary(self) -> Dict:
        return {
            "investigation_id": self.investigation_id,
            "total_records":    len(self._records),
            "by_protocol":      {
                p: len([r for r in self._records if r.protocol_used == p])
                for p in set(r.protocol_used for r in self._records)
            },
            "last_decision": self._records[-1].decision if self._records else None,
        }


# ─── GICore: единая точка входа для обоих продуктов ──────────────────────────

class GICore:
    """
    GI v6.2 Core — фасад над всеми протоколами.

    Используется как GOVERNANCE так и INTELLIGENCE.
    Каждый создаёт свой экземпляр с уникальным investigation_id.

    Пример:
        gi = GICore(investigation_id="INV-2026-001")
        ssc_result = gi.ssc.apply(source, event)
        if ssc_result.trigger_cdr:
            gi.oас.log("SSC→CDR", ...)
        pps = gi.pps(["SSC1_RECANTATION", "NGI_HIGH"])
    """

    def __init__(self, investigation_id: Optional[str] = None):
        self.investigation_id = investigation_id or str(uuid.uuid4())[:12]
        self.ssc  = SSCProtocol()
        self.frcp = FRCPProtocol()
        self.cdr  = CDRProtocol()
        self.sad  = SADProtocol()
        self.oas  = OASJournal(self.investigation_id)

    def pps(self, active_triggers: List[str]) -> PPSResult:
        """Расставить приоритеты протоколов (P55)."""
        result = pps_prioritize(active_triggers)
        self.oas.log(
            event_type="PPS_EVALUATION",
            decision=f"Приоритет: {result.top_priority or 'нет активных'}",
            basis=active_triggers,
            protocol_used="P55",
        )
        return result

    def ngi_actions(self, ngi_level: str) -> NGIAction:
        """Получить обязательные действия по уровню NGI (P46)."""
        return get_ngi_actions(ngi_level)
