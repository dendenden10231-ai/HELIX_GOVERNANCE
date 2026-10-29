# Мистер Хеликс — реестр по каждой капсуле

**Сгенерировано, не написано руками**: `PYTHONUTF8=1 python scripts/реестр_продуктов.py`.
Статус капсулы берёт штатный `mr_helix/engine/capsule_coverage_validator.py`:
`ENFORCED` — символы есть в коде И существует тест, который их зовёт;
`PARTIAL` — символы есть, теста нет; `SPEC_ONLY` — в коде ничего нет.
Символ в коде ≠ поведение по спеке — это правило самого валидатора.

Источник списка капсул — спеки `mr_helix/docs/spec/PACK_00..05`, а не карты
требований: карт пять, у PACK_00 её нет, и полнота по картам молча теряла
целый пакет из пятнадцати капсул (история — в шапке `capsule_manifest.yaml`).

Всего **99 капсул** в 6 пакетах; символов в реестре — **141**.

---


## PACK 00 — 15 капсул

### 00.1 — MODE_SOVEREIGNTY_CAPSULE

- **статус**: `ENFORCED` · тест: `test_integration_nervous_system.py`
- **модуль**: `mr_helix/engine/integration_nervous_system.py` (1123 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_00_Integration_Nervous_System_v0_3.md:219` — 00.1 MODE_SOVEREIGNTY_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `Mode` | 55 | класс |  | 0 |
| `select_mode` | 78 | функция | 00.1. Priority order per spec's own runtime function: child overlay | 2 |

### 00.2 — DOMAIN_SEPARATION_CAPSULE

- **статус**: `ENFORCED` · тест: `test_integration_nervous_system.py`
- **модуль**: `mr_helix/engine/integration_nervous_system.py` (1123 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_00_Integration_Nervous_System_v0_3.md:338` — 00.2 DOMAIN_SEPARATION_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `Domain` | 63 | класс |  | 0 |
| `classify_domain` | 136 | функция | 00.2. AI_OUTPUT (via is_ai_output flag), FORECAST_CLAIM and | 3 |

### 00.3 — NAMESPACE_INTEGRITY_CAPSULE

- **статус**: `ENFORCED` · тест: `test_integration_nervous_system.py`
- **модуль**: `mr_helix/engine/integration_nervous_system.py` (1123 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_00_Integration_Nervous_System_v0_3.md:430` — 00.3 NAMESPACE_INTEGRITY_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `check_namespace_integrity` | 238 | функция | 00.3. A bare family prefix (e.g. "SSC" or "CPX" with no suffix) is | 2 |

### 00.4 — FORBIDDEN_LINKS_GATE_CAPSULE

- **статус**: `ENFORCED` · тест: `test_helix_translation_tables.py`
- **модуль**: `mr_helix/engine/integration_nervous_system.py` (1123 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_00_Integration_Nervous_System_v0_3.md:520` — 00.4 FORBIDDEN_LINKS_GATE_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `check_forbidden_link` | 339 | функция | 00.4. Шлюз связей: блокирует, пропускает и МАРШРУТИЗИРУЕТ. | 3 |

### 00.5 — SPEED_PROTOCOL_CAPSULE

- **статус**: `ENFORCED` · тест: `test_integration_nervous_system.py`
- **модуль**: `mr_helix/engine/integration_nervous_system.py` (1123 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_00_Integration_Nervous_System_v0_3.md:636` — 00.5 SPEED_PROTOCOL_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `SpeedMode` | 416 | класс |  | 0 |
| `select_speed_protocol` | 423 | функция | 00.5. BREAKING never licenses a final ECT-4 output without full | 1 |

### 00.6 — TLX_TRANSLATION_CAPSULE

- **статус**: `ENFORCED` · тест: `test_helix_translation_tables.py`
- **модуль**: `mr_helix/engine/integration_nervous_system.py` (1123 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_00_Integration_Nervous_System_v0_3.md:710` — 00.6 TLX_TRANSLATION_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `tlx_translate` | 462 | функция | 00.6. Перевод сигнала между движками. Главный рефлекс спеки: | 4 |

### 00.7 — CLE_CROSS_LINK_CAPSULE

- **статус**: `ENFORCED` · тест: `test_cle_and_fa_registries.py`
- **модуль**: `mr_helix/engine/integration_nervous_system.py` (1123 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_00_Integration_Nervous_System_v0_3.md:785` — 00.7 CLE_CROSS_LINK_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `cle_resolve` | 542 | функция | 00.7. Связи не выстреливают все разом (FG-08); Compute Budget | 3 |

### 00.8 — ACTIVE_PATCH_FUNCTION_CAPSULE

- **статус**: `ENFORCED` · тест: `test_integration_nervous_system.py`
- **модуль**: `mr_helix/engine/integration_nervous_system.py` (1123 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_00_Integration_Nervous_System_v0_3.md:858` — 00.8 ACTIVE_PATCH_FUNCTION_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `activate_patch` | 607 | функция | 00.8. Активный патч: маркер обязан что-то ДЕЛАТЬ. | 2 |

### 00.9 — COMPUTE_BUDGET_CAPSULE

- **статус**: `ENFORCED` · тест: `test_integration_nervous_system.py`
- **модуль**: `mr_helix/engine/integration_nervous_system.py` (1123 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_00_Integration_Nervous_System_v0_3.md:930` — 00.9 COMPUTE_BUDGET_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `compute_budget_precheck` | 676 | функция | 00.9a. До TLX/CLE — чтобы каскад не успел начаться. | 2 |
| `compute_budget_postcheck` | 711 | функция | 00.9b. После активных патчей — ловит фактический перегрев. | 2 |

### 00.10 — CPX_ARBITRATION_CAPSULE

- **статус**: `ENFORCED` · тест: `test_helix_translation_tables.py`
- **модуль**: `mr_helix/engine/integration_nervous_system.py` (1123 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_00_Integration_Nervous_System_v0_3.md:1061` — 00.10 CPX_ARBITRATION_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `cpx_arbitrate` | 760 | функция | 00.10. Арбитраж расхождения GI и AK. | 2 |

### 00.11 — RECONCILIATION_CAPSULE

- **статус**: `ENFORCED` · тест: `test_integration_nervous_system.py`
- **модуль**: `mr_helix/engine/integration_nervous_system.py` (1123 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_00_Integration_Nervous_System_v0_3.md:1141` — 00.11 RECONCILIATION_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `reconcile` | 836 | функция | 00.11. A CPX win is never a permanent dictatorship (spec | 2 |

### 00.12 — HITL_REDLINE_CAPSULE

- **статус**: `ENFORCED` · тест: `test_integration_nervous_system.py`
- **модуль**: `mr_helix/engine/integration_nervous_system.py` (1123 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_00_Integration_Nervous_System_v0_3.md:1212` — 00.12 HITL_REDLINE_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `hitl_redline` | 890 | функция | 00.12. ADVISORY продолжает с авто-действием и обязательным OAS; | 3 |

### 00.13 — OAS_HELIX_LOGGING_CAPSULE

- **статус**: `ENFORCED` · тест: `test_integration_nervous_system.py`
- **модуль**: `mr_helix/engine/integration_nervous_system.py` (1123 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_00_Integration_Nervous_System_v0_3.md:1289` — 00.13 OAS_HELIX_LOGGING_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `OASHelixEntry` | 937 | класс |  | 0 |
| `OASHelixLog` | 950 | класс | 00.13. Distinct from OASEvidenceLog (01.16) — that one logs claim | 1 |

### 00.14 — MODE_REVIEW_CAPSULE

- **статус**: `ENFORCED` · тест: `test_integration_nervous_system.py`
- **модуль**: `mr_helix/engine/integration_nervous_system.py` (1123 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_00_Integration_Nervous_System_v0_3.md:1354` — 00.14 MODE_REVIEW_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `review_mode` | 989 | функция | 00.14. Система, которая спорит сама с собой, может быть не в том | 2 |

### 00.15 — PRE_OUTPUT_GATE_CAPSULE

- **статус**: `ENFORCED` · тест: `test_integration_nervous_system.py`
- **модуль**: `mr_helix/engine/integration_nervous_system.py` (1123 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_00_Integration_Nervous_System_v0_3.md:1409` — 00.15 PRE_OUTPUT_GATE_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `pre_output_gate` | 1056 | функция | 00.15. Final gate of PACK 00 — 12 checks per spec. Any single | 5 |

## PACK 01 — 16 капсул

### 01.1 — EVIDENCE_CLASS_CAPSULE

- **статус**: `ENFORCED` · тест: `test_root_epistemic_organs.py`
- **модуль**: `mr_helix/engine/root_epistemic_organs.py` (1173 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_01_Root_Epistemic_Organs_v0_2.md:324` — 01.1 EVIDENCE_CLASS_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `EvidenceClass` | 36 | класс |  | 0 |
| `classify_evidence_class` | 128 | функция | Classify a single (already-atomized) claim's evidence type. | 1 |
| `atomize_claims` | 85 | функция | Pre-capsule gate. Splits `text` on causal/conclusion connectives so | 1 |
| `AtomizedClaim` | 79 | класс |  | 0 |

### 01.2 — ECT_CAPSULE

- **статус**: `ENFORCED` · тест: `test_api_main.py`
- **модуль**: `mr_helix/engine/root_epistemic_organs.py` (1173 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_01_Root_Epistemic_Organs_v0_2.md:436` — 01.2 ECT_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `ECT` | 44 | класс |  | 25 |
| `assign_ect` | 179 | функция | Deterministically apply the spec's ECT ladder (section 01.2) to | 2 |

### 01.3 — H_NULL_CAPSULE

- **статус**: `ENFORCED` · тест: `test_root_epistemic_organs.py`
- **модуль**: `mr_helix/engine/root_epistemic_organs.py` (1173 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_01_Root_Epistemic_Organs_v0_2.md:569` — 01.3 H_NULL_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `formulate_h_null` | 892 | функция | 01.3. SSD = Structured Stress/Disproof test: a hypothesis that | 1 |
| `h_null_forbidden_move_check` | 1089 | функция | 01.3 forbidden moves (4, per spec "Что запрещено"). | 1 |

### 01.4 — NON_LIQUET_CAPSULE

- **статус**: `ENFORCED` · тест: `test_root_epistemic_organs.py`
- **модуль**: `mr_helix/engine/root_epistemic_organs.py` (1173 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_01_Root_Epistemic_Organs_v0_2.md:682` — 01.4 NON_LIQUET_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `check_non_liquet` | 924 | функция | 01.4. NON LIQUET is a professional stop, not a weakness or an | 1 |
| `non_liquet_forbidden_move_check` | 1117 | функция | 01.4 forbidden moves (4, per spec "Что запрещено"). | 1 |

### 01.5 — SOURCE_STATUS_CAPSULE

- **статус**: `ENFORCED` · тест: `test_root_epistemic_organs.py`
- **модуль**: `mr_helix/engine/root_epistemic_organs.py` (1173 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_01_Root_Epistemic_Organs_v0_2.md:756` — 01.5 SOURCE_STATUS_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `SourceStatus` | 232 | класс |  | 0 |
| `assess_source_status` | 244 | функция | 01.5: SSC-SOURCE only (not SSC-CHAR, not SSC-SOMATIC — different | 1 |

### 01.6 — SOURCE_AUTHENTICATION_CAPSULE

- **статус**: `ENFORCED` · тест: `test_root_epistemic_organs.py`
- **модуль**: `mr_helix/engine/root_epistemic_organs.py` (1173 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_01_Root_Epistemic_Organs_v0_2.md:885` — 01.6 SOURCE_AUTHENTICATION_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `authenticate_source` | 297 | функция | 01.6. `identity_type` in {"verified","pseudonymous","anonymous","unknown"}. | 1 |

### 01.7 — WPL_PROVENANCE_CAPSULE

- **статус**: `ENFORCED` · тест: `test_pack01_contract_states.py`
- **модуль**: `mr_helix/engine/root_epistemic_organs.py` (1173 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_01_Root_Epistemic_Organs_v0_2.md:996` — 01.7 WPL_PROVENANCE_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `assess_wpl_provenance` | 342 | функция | 01.7. relay_depth=0 means direct witness/document/primary record. | 2 |

### 01.8 — PDE_DOCUMENT_INTEGRITY_CAPSULE

- **статус**: `ENFORCED` · тест: `test_pack01_contract_states.py`
- **модуль**: `mr_helix/engine/root_epistemic_organs.py` (1173 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_01_Root_Epistemic_Organs_v0_2.md:1113` — 01.8 PDE_DOCUMENT_INTEGRITY_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `check_document_integrity` | 392 | функция | 01.8. A document that "looks official" is not primary by default | 2 |

### 01.9 — INDEPENDENCE_VECTOR_CAPSULE

- **статус**: `ENFORCED` · тест: `test_bp_01_001_iv_math_boundary.py`
- **модуль**: `mr_helix/engine/root_epistemic_organs.py` (1173 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_01_Root_Epistemic_Organs_v0_2.md:1245` — 01.9 INDEPENDENCE_VECTOR_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `assess_independence_vector` | 446 | функция | 01.9. Repetition is not independence (spec prohibition) — many | 2 |

### 01.10 — ICOI_CAPSULE

- **статус**: `ENFORCED` · тест: `test_root_epistemic_organs.py`
- **модуль**: `mr_helix/engine/root_epistemic_organs.py` (1173 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_01_Root_Epistemic_Organs_v0_2.md:1355` — 01.10 ICOI_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `assess_icoi` | 574 | функция | 01.10. ICoI does NOT mean the claim is false — it means the | 1 |

### 01.11 — PRESSURE_PREFLIGHT_CAPSULE

- **статус**: `ENFORCED` · тест: `test_mr_helix_orchestrator.py`
- **модуль**: `mr_helix/engine/root_epistemic_organs.py` (1173 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_01_Root_Epistemic_Organs_v0_2.md:1469` — 01.11 PRESSURE_PREFLIGHT_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `pressure_preflight` | 639 | функция | 01.11. Runs BEFORE ECT-final (spec order). Pressure is data, not | 3 |
| `pressure_preflight_forbidden_move_check` | 1145 | функция | 01.11 forbidden moves (5, per spec "Что запрещено"). | 1 |

### 01.12 — AI_OUTPUT_GOVERNANCE_CAPSULE

- **статус**: `ENFORCED` · тест: `test_pack01_contract_states.py`
- **модуль**: `mr_helix/engine/root_epistemic_organs.py` (1173 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_01_Root_Epistemic_Organs_v0_2.md:1602` — 01.12 AI_OUTPUT_GOVERNANCE_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `audit_ai_output` | 708 | функция | 01.12. Any AI output defaults to AI-ECT-1 (I-08, enforced | 2 |

### 01.13 — FORECAST_CLAIM_CAPSULE

- **статус**: `ENFORCED` · тест: `test_pack01_contract_states.py`
- **модуль**: `mr_helix/engine/root_epistemic_organs.py` (1173 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_01_Root_Epistemic_Organs_v0_2.md:1749` — 01.13 FORECAST_CLAIM_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `split_forecast_claim` | 785 | функция | 01.13. Splits "source predicts X" (Claim-A, about the publication/ | 2 |

### 01.14 — TRUST_CONFIDENCE_CAPSULE

- **статус**: `ENFORCED` · тест: `test_pack01_contract_states.py`
- **модуль**: `mr_helix/engine/root_epistemic_organs.py` (1173 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_01_Root_Epistemic_Organs_v0_2.md:1850` — 01.14 TRUST_CONFIDENCE_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `separate_trust_confidence_risk` | 839 | функция | 01.14. Keeps four distinct layers from collapsing into each other | 2 |

### 01.15 — HITL_EPISTEMIC_TRIGGER_CAPSULE

- **статус**: `ENFORCED` · тест: `test_root_epistemic_organs.py`
- **модуль**: `mr_helix/engine/root_epistemic_organs.py` (1173 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_01_Root_Epistemic_Organs_v0_2.md:1966` — 01.15 HITL_EPISTEMIC_TRIGGER_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `check_hitl_trigger` | 991 | функция | 01.15. REQUIRED always outranks ADVISORY (spec prohibition: | 1 |

### 01.16 — OAS_EVIDENCE_LOG_CAPSULE

- **статус**: `ENFORCED` · тест: `test_mr_helix_orchestrator.py`
- **модуль**: `mr_helix/engine/root_epistemic_organs.py` (1173 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_01_Root_Epistemic_Organs_v0_2.md:2063` — 01.16 OAS_EVIDENCE_LOG_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `OASEntry` | 1030 | класс |  | 0 |
| `OASEvidenceLog` | 1037 | класс | 01.16. Append-only audit log. Enforces: no editing after an entry | 2 |

## PACK 02 — 16 капсул

### 02.0 — ENVIRONMENT_SCAN_GATE

- **статус**: `ENFORCED` · тест: `test_chf_closing_capsules.py`
- **модуль**: `mr_helix/engine/environment_chf_pressure_layer.py` (1170 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_02_Environment_CHF_Pressure_Layer_v0_2.md:270` — 02.0 ENVIRONMENT_SCAN_GATE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `environment_scan_gate` | 96 | функция | 02.0. Cheap first-pass candidate flagging. Does not itself change | 2 |

### 02.1 — CHF_A_ATTENTION_COLLAPSE_CAPSULE

- **статус**: `ENFORCED` · тест: `test_chf_closing_capsules.py`
- **модуль**: `mr_helix/engine/environment_chf_pressure_layer.py` (1170 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_02_Environment_CHF_Pressure_Layer_v0_2.md:376` — 02.1 CHF_A_ATTENTION_COLLAPSE_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `chf_a_attention_collapse` | 159 | функция | 02.1. Escalation ladder over caller-supplied indicator codes. | 2 |
| `chf_a_gi_source_flag` | 226 | функция | 02.1b-GI. GI-side half of the bridge: GI detects AC in a source via | 1 |
| `chf_a_ak_narrative_adapt` | 241 | функция | 02.1b-AK. AK-side half: on receiving an AC-flag, adapts narrative | 1 |
| `chf_a_helix_coordinate` | 264 | функция | 02.1b-HELIX. Combined-risk coordination: an unreliable source | 1 |
| `chf_a_tlx_translate` | 282 | функция | 02.1b-TLX. GI <-> AK term translation for AC, per spec §6. Same core | 1 |
| `chf_a_conflict_resolve` | 296 | функция | 02.1b-CPX. AK vs GI conflict at AC (spec §6 scenario: AK finds the | 1 |

### 02.2 — CHF_B_ALGORITHMIC_AMPLIFICATION_CAPSULE

- **статус**: `ENFORCED` · тест: `test_chf_closing_capsules.py`
- **модуль**: `mr_helix/engine/environment_chf_pressure_layer.py` (1170 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_02_Environment_CHF_Pressure_Layer_v0_2.md:507` — 02.2 CHF_B_ALGORITHMIC_AMPLIFICATION_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `chf_b_algorithmic_amplification` | 384 | функция | 02.2. Reach is not credibility (AA-REACH-MISMATCH). Sources from | 2 |

### 02.3 — CHF_C_IDENTITY_ACCELERATION_CAPSULE

- **статус**: `ENFORCED` · тест: `test_chf_closing_capsules.py`
- **модуль**: `mr_helix/engine/environment_chf_pressure_layer.py` (1170 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_02_Environment_CHF_Pressure_Layer_v0_2.md:633` — 02.3 CHF_C_IDENTITY_ACCELERATION_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `chf_c_identity_acceleration` | 446 | функция | 02.3. Tribal testimony is weighted, not automatically rejected | 2 |

### 02.4 — CHF_D_MEMETIC_WARFARE_CAPSULE

- **статус**: `ENFORCED` · тест: `test_chf_closing_capsules.py`
- **модуль**: `mr_helix/engine/environment_chf_pressure_layer.py` (1170 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_02_Environment_CHF_Pressure_Layer_v0_2.md:759` — 02.4 CHF_D_MEMETIC_WARFARE_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `chf_d_memetic_warfare` | 529 | функция | 02.4. Captures interpretive space BEFORE evidence appears — unlike | 2 |

### 02.5 — MW_TAC_CAPSULE

- **статус**: `ENFORCED` · тест: `test_chf_closing_capsules.py`
- **модуль**: `mr_helix/engine/environment_chf_pressure_layer.py` (1170 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_02_Environment_CHF_Pressure_Layer_v0_2.md:872` — 02.5 MW_TAC_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `mw_tac_identify` | 607 | функция | 02.5. Describes the attack METHOD; CHF-D describes the EFFECT — | 2 |

### 02.6 — CHF_E_SYNTHETIC_PERSUASION_CAPSULE

- **статус**: `ENFORCED` · тест: `test_chf_closing_capsules.py`
- **модуль**: `mr_helix/engine/environment_chf_pressure_layer.py` (1170 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_02_Environment_CHF_Pressure_Layer_v0_2.md:966` — 02.6 CHF_E_SYNTHETIC_PERSUASION_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `chf_e_synthetic_persuasion` | 657 | функция | 02.6. Danger is not "looks like AI" — it's "looks like a human, | 2 |

### 02.7 — SP_FORM_CAPSULE

- **статус**: `ENFORCED` · тест: `test_environment_chf_pressure_layer.py`
- **модуль**: `mr_helix/engine/environment_chf_pressure_layer.py` (1170 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_02_Environment_CHF_Pressure_Layer_v0_2.md:1049` — 02.7 SP_FORM_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `SPForm` | 720 | класс |  | 0 |
| `sp_form_classify` | 737 | функция | 02.7. Classifies WHICH form of synthetic persuasion is present. | 1 |

### 02.8 — CHF_F_INFORMATION_EXHAUSTION_CAPSULE

- **статус**: `ENFORCED` · тест: `test_chf_closing_capsules.py`
- **модуль**: `mr_helix/engine/environment_chf_pressure_layer.py` (1170 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_02_Environment_CHF_Pressure_Layer_v0_2.md:1144` — 02.8 CHF_F_INFORMATION_EXHAUSTION_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `chf_f_information_exhaustion` | 764 | функция | 02.8. A lie can win not because it convinced, but because it | 2 |

### 02.9 — CHF_COMPOUND_RULE_CAPSULE

- **статус**: `ENFORCED` · тест: `test_chf_closing_capsules.py`
- **модуль**: `mr_helix/engine/environment_chf_pressure_layer.py` (1170 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_02_Environment_CHF_Pressure_Layer_v0_2.md:1245` — 02.9 CHF_COMPOUND_RULE_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `chf_compound_rule` | 336 | функция | 02.9. I-10: 3+ active CHF modules -> compound high risk. | 2 |

### 02.10 — CHF_TRUST_ECT_IV_IMPACT_CAPSULE

- **статус**: `ENFORCED` · тест: `test_chf_closing_capsules.py`
- **модуль**: `mr_helix/engine/environment_chf_pressure_layer.py` (1170 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_02_Environment_CHF_Pressure_Layer_v0_2.md:1392` — 02.10 CHF_TRUST_ECT_IV_IMPACT_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `chf_pack01_impact` | 905 | функция | 02.10. Что активная среда делает со входами PACK 01. | 1 |
| `CHF_PACK01_IMPACT` | — | функция | 02.14. Журнал средовых решений в формате спеки. | 0 |

### 02.11 — CHF_CPX_MAPPING_CAPSULE

- **статус**: `ENFORCED` · тест: `test_chf_closing_capsules.py`
- **модуль**: `mr_helix/engine/environment_chf_pressure_layer.py` (1170 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_02_Environment_CHF_Pressure_Layer_v0_2.md:1473` — 02.11 CHF_CPX_MAPPING_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `chf_cpx_mapping` | 965 | функция | 02.11. Какие конфликты CPX порождает среда. | 1 |
| `CHF_CPX_MAP` | — | функция | 02.14. Журнал средовых решений в формате спеки. | 0 |

### 02.12 — CHF_TLX_CLE_HANDOFF_CAPSULE

- **статус**: `ENFORCED` · тест: `test_chf_closing_capsules.py`
- **модуль**: `mr_helix/engine/environment_chf_pressure_layer.py` (1170 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_02_Environment_CHF_Pressure_Layer_v0_2.md:1560` — 02.12 CHF_TLX_CLE_HANDOFF_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `chf_tlx_cle_handoff` | 1014 | функция | 02.12. Передача сигнала среды между уровнями без их смешения. | 1 |
| `CHF_HANDOFF_SCOPE` | — | функция | 02.14. Журнал средовых решений в формате спеки. | 0 |
| `CHF_HANDOFF_FORBIDDEN` | — | функция | 02.14. Журнал средовых решений в формате спеки. | 0 |

### 02.13 — CHF_HITL_TRIGGER_CAPSULE

- **статус**: `ENFORCED` · тест: `test_chf_closing_capsules.py`
- **модуль**: `mr_helix/engine/environment_chf_pressure_layer.py` (1170 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_02_Environment_CHF_Pressure_Layer_v0_2.md:1639` — 02.13 CHF_HITL_TRIGGER_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `chf_hitl_trigger` | 1055 | функция | 02.13. Когда среда обязана позвать человека. | 1 |
| `CHF_HITL_REQUIRED_TRIGGERS` | — | функция | 02.14. Журнал средовых решений в формате спеки. | 1 |
| `CHF_HITL_ADVISORY_TRIGGERS` | — | функция | 02.14. Журнал средовых решений в формате спеки. | 1 |

### 02.14 — CHF_OAS_LOGGING_CAPSULE

- **статус**: `ENFORCED` · тест: `test_chf_closing_capsules.py`
- **модуль**: `mr_helix/engine/environment_chf_pressure_layer.py` (1170 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_02_Environment_CHF_Pressure_Layer_v0_2.md:1731` — 02.14 CHF_OAS_LOGGING_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `chf_oas_logging` | 1135 | функция | 02.14. Журнал средовых решений в формате спеки. | 1 |

### 02.15 — ENVIRONMENT_DEFENSE_STRATEGY_CAPSULE

- **статус**: `ENFORCED` · тест: `test_chf_closing_capsules.py`
- **модуль**: `mr_helix/engine/environment_chf_pressure_layer.py` (1170 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_02_Environment_CHF_Pressure_Layer_v0_2.md:1824` — 02.15 ENVIRONMENT_DEFENSE_STRATEGY_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `chf_defense_strategy` | 1098 | функция | 02.15. Как публиковаться, когда среда атакована. | 1 |
| `CHF_DEFENSE_STRATEGY` | — | функция | 02.14. Журнал средовых решений в формате спеки. | 0 |

## PACK 03 — 17 капсул

### 03.0 — VOICE_ACTIVATION_GATE

- **статус**: `ENFORCED` · тест: `test_voice_soul_literary_intelligence.py`
- **модуль**: `mr_helix/engine/voice_soul_literary_intelligence.py` (821 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_03_Voice_Soul_Literary_Intelligence_v0_2.md:255` — 03.0 VOICE_ACTIVATION_GATE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `VoiceLevel` | 46 | класс |  | 0 |
| `voice_activation_gate` | 59 | функция | 03.0. Determines which voice level is permitted. `requested_vis` | 1 |

### 03.1 — LIT_VOICE_LAYER_CAPSULE

- **статус**: `ENFORCED` · тест: `test_voice_soul_literary_intelligence.py`
- **модуль**: `mr_helix/engine/voice_soul_literary_intelligence.py` (821 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_03_Voice_Soul_Literary_Intelligence_v0_2.md:430` — 03.1 LIT_VOICE_LAYER_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `lit_apply` | 189 | функция | 03.1. Term first, anchor after, mechanism explained, ECT unchanged | 1 |

### 03.2 — EV_CORE_CAPSULE

- **статус**: `ENFORCED` · тест: `test_pack03_contract_states.py`
- **модуль**: `mr_helix/engine/voice_soul_literary_intelligence.py` (821 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_03_Voice_Soul_Literary_Intelligence_v0_2.md:520` — 03.2 EV_CORE_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `ev_core_check` | 237 | функция | 03.2. `active_cores` maps EV core name -> intensity (1-5). EV marks | 2 |

### 03.3 — IRONY_LAW_CAPSULE

- **статус**: `ENFORCED` · тест: `test_voice_soul_literary_intelligence.py`
- **модуль**: `mr_helix/engine/voice_soul_literary_intelligence.py` (821 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_03_Voice_Soul_Literary_Intelligence_v0_2.md:597` — 03.3 IRONY_LAW_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `irony_check` | 282 | функция | 03.3. Irony cuts false FORM, not a person (spec's own framing). | 1 |

### 03.4 — AWE_LAW_CAPSULE

- **статус**: `ENFORCED` · тест: `test_voice_soul_literary_intelligence.py`
- **модуль**: `mr_helix/engine/voice_soul_literary_intelligence.py` (821 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_03_Voice_Soul_Literary_Intelligence_v0_2.md:682` — 03.4 AWE_LAW_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `awe_check` | 314 | функция | 03.4. Awe is a signal of precise connection, not architecture | 1 |

### 03.5 — LITERARY_ANCHOR_PROTOCOL_CAPSULE

- **статус**: `ENFORCED` · тест: `test_voice_soul_literary_intelligence.py`
- **модуль**: `mr_helix/engine/voice_soul_literary_intelligence.py` (821 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_03_Voice_Soul_Literary_Intelligence_v0_2.md:768` — 03.5 LITERARY_ANCHOR_PROTOCOL_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `literary_anchor_select` | 350 | функция | 03.5. Anchor illuminates, never proves (spec's own mini-test: | 1 |

### 03.6 — AESTHETIC_COLLAPSE_DETECTOR_CAPSULE

- **статус**: `ENFORCED` · тест: `test_pack03_contract_states.py`
- **модуль**: `mr_helix/engine/voice_soul_literary_intelligence.py` (821 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_03_Voice_Soul_Literary_Intelligence_v0_2.md:852` — 03.6 AESTHETIC_COLLAPSE_DETECTOR_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `aesthetic_collapse_check` | 122 | функция | 03.6. Tracks the Perceived Certainty Delta (0-4) against ECT. | 2 |

### 03.7 — SCN_SEMANTIC_PARSING_CAPSULE

- **статус**: `ENFORCED` · тест: `test_pack03_contract_states.py`
- **модуль**: `mr_helix/engine/voice_soul_literary_intelligence.py` (821 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_03_Voice_Soul_Literary_Intelligence_v0_2.md:983` — 03.7 SCN_SEMANTIC_PARSING_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `scn_select` | 393 | функция | 03.7. SCN-CORE (semantic pressure/contradiction/false coherence) | 2 |

### 03.8 — SYN_RECURSIVE_STABILIZATION_CAPSULE

- **статус**: `ENFORCED` · тест: `test_pack03_contract_states.py`
- **модуль**: `mr_helix/engine/voice_soul_literary_intelligence.py` (821 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_03_Voice_Soul_Literary_Intelligence_v0_2.md:1085` — 03.8 SYN_RECURSIVE_STABILIZATION_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `syn_select` | 434 | функция | 03.8. SYN-RSE (continuity restoration) vs SYN-LIB (syntactic | 2 |

### 03.9 — THERMAL_SEMANTICS_CAPSULE

- **статус**: `ENFORCED` · тест: `test_pack03_contract_states.py`
- **модуль**: `mr_helix/engine/voice_soul_literary_intelligence.py` (821 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_03_Voice_Soul_Literary_Intelligence_v0_2.md:1176` — 03.9 THERMAL_SEMANTICS_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `thermal_state_check` | 482 | функция | 03.9. Thermal state regulates voice intensity — it does not prove | 2 |

### 03.10 — SOMATIC_ANCHOR_CAPSULE

- **статус**: `ENFORCED` · тест: `test_pack03_contract_states.py`
- **модуль**: `mr_helix/engine/voice_soul_literary_intelligence.py` (821 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_03_Voice_Soul_Literary_Intelligence_v0_2.md:1266` — 03.10 SOMATIC_ANCHOR_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `somatic_anchor_check` | 524 | функция | 03.10. Namespace: SSC-SOMATIC — distinct from SSC-SOURCE/SSC-CHAR | 2 |

### 03.11 — PHASE9_BUDGET_GATE

- **статус**: `ENFORCED` · тест: `test_pack03_contract_states.py`
- **модуль**: `mr_helix/engine/voice_soul_literary_intelligence.py` (821 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_03_Voice_Soul_Literary_Intelligence_v0_2.md:1356` — 03.11 PHASE9_BUDGET_GATE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `phase9_budget_gate` | 564 | функция | 03.11. Phase 9 engines are standby by default; at most 1 active | 2 |

### 03.12 — LEM_LOW_ENERGY_CAPSULE

- **статус**: `ENFORCED` · тест: `test_voice_soul_literary_intelligence.py`
- **модуль**: `mr_helix/engine/voice_soul_literary_intelligence.py` (821 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_03_Voice_Soul_Literary_Intelligence_v0_2.md:1457` — 03.12 LEM_LOW_ENERGY_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `lem_check` | 636 | функция | 03.12. LEM shows energetic state, not textual weakness or falsehood | 1 |

### 03.13 — SIL_SILENCE_ENGINE_CAPSULE

- **статус**: `ENFORCED` · тест: `test_voice_soul_literary_intelligence.py`
- **модуль**: `mr_helix/engine/voice_soul_literary_intelligence.py` (821 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_03_Voice_Soul_Literary_Intelligence_v0_2.md:1552` — 03.13 SIL_SILENCE_ENGINE_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `sil_classify` | 663 | функция | 03.13. SAD-GI (silence as data in the external evidence field) and | 1 |

### 03.14 — MPE_MEMORY_PRESSURE_CAPSULE

- **статус**: `ENFORCED` · тест: `test_voice_soul_literary_intelligence.py`
- **модуль**: `mr_helix/engine/voice_soul_literary_intelligence.py` (821 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_03_Voice_Soul_Literary_Intelligence_v0_2.md:1635` — 03.14 MPE_MEMORY_PRESSURE_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `mpe_check` | 695 | функция | 03.14. MPE does not prove a fact — it shows pressure on memory. | 1 |

### 03.15 — SFE_TAT_FIELD_TIME_CAPSULE

- **статус**: `ENFORCED` · тест: `test_voice_soul_literary_intelligence.py`
- **модуль**: `mr_helix/engine/voice_soul_literary_intelligence.py` (821 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_03_Voice_Soul_Literary_Intelligence_v0_2.md:1722` — 03.15 SFE_TAT_FIELD_TIME_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `sfe_check` | 723 | функция | 03.15a. SFE max 1 per scene; SFE-MEME must never merge with CHF-D | 1 |
| `tat_check` | 738 | функция | 03.15b. TAT-RETRO warns that present reorganized by later | 1 |

### 03.16 — VOICE_OAS_SELF_AUDIT_CAPSULE

- **статус**: `ENFORCED` · тест: `test_pack03_contract_states.py`
- **модуль**: `mr_helix/engine/voice_soul_literary_intelligence.py` (821 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_03_Voice_Soul_Literary_Intelligence_v0_2.md:1824` — 03.16 VOICE_OAS_SELF_AUDIT_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `voice_oas_required` | 781 | функция | 03.16a. Determines whether a Voice OAS self-audit is required for | 1 |
| `voice_oas_self_audit` | 792 | функция | 03.16b. Runs the 12-question self-audit. All "yes" (True) answers | 2 |

## PACK 04 — 20 капсул

### 04.0 — VECTOR_ROUTER_GATE

- **статус**: `ENFORCED` · тест: `test_vector_orchestration_domain_runtime_gate.py`
- **модуль**: `mr_helix/engine/vector_orchestration_domain_runtime_gate.py` (986 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_04_Vector_Orchestration_Domain_Runtime_Gate_v0_1.md:283` — 04.0 VECTOR_ROUTER_GATE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `vector_router_gate` | 130 | функция | 04.0. Cheap keyword-candidate scan (mirrors environment_scan_gate in | 2 |
| `VectorRouterCandidates` | 122 | класс |  | 0 |

### 04.1 — VECTOR_CONTRACT_CAPSULE

- **статус**: `ENFORCED` · тест: `test_vector_orchestration_domain_runtime_gate.py`
- **модуль**: `mr_helix/engine/vector_orchestration_domain_runtime_gate.py` (986 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_04_Vector_Orchestration_Domain_Runtime_Gate_v0_1.md:407` — 04.1 VECTOR_CONTRACT_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `vector_contract_capsule` | 206 | функция | 04.1. Validates the mandatory contract fields (I-04-03/04: primary | 1 |

### 04.2 — TRACE_VECTOR_INTERFACE

- **статус**: `ENFORCED` · тест: `test_vector_orchestration_domain_runtime_gate.py`
- **модуль**: `mr_helix/engine/vector_orchestration_domain_runtime_gate.py` (986 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_04_Vector_Orchestration_Domain_Runtime_Gate_v0_1.md:488` — 04.2 TRACE_VECTOR_INTERFACE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `VectorType` | 55 | класс |  | 0 |
| `vector_interface_check` | 327 | функция | 04.2-04.6. Scans caller-asserted actions (action codes, e.g. | 1 |

### 04.3 — INTELLIGENCE_VECTOR_INTERFACE

- **статус**: `ENFORCED` · тест: `test_vector_orchestration_domain_runtime_gate.py`
- **модуль**: `mr_helix/engine/vector_orchestration_domain_runtime_gate.py` (986 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_04_Vector_Orchestration_Domain_Runtime_Gate_v0_1.md:613` — 04.3 INTELLIGENCE_VECTOR_INTERFACE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `VectorType` | 55 | класс |  | 0 |
| `vector_interface_check` | 327 | функция | 04.2-04.6. Scans caller-asserted actions (action codes, e.g. | 1 |

### 04.4 — GOVERNANCE_VECTOR_INTERFACE

- **статус**: `ENFORCED` · тест: `test_vector_orchestration_domain_runtime_gate.py`
- **модуль**: `mr_helix/engine/vector_orchestration_domain_runtime_gate.py` (986 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_04_Vector_Orchestration_Domain_Runtime_Gate_v0_1.md:738` — 04.4 GOVERNANCE_VECTOR_INTERFACE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `VectorType` | 55 | класс |  | 0 |
| `vector_interface_check` | 327 | функция | 04.2-04.6. Scans caller-asserted actions (action codes, e.g. | 1 |

### 04.5 — MARKET_VECTOR_INTERFACE

- **статус**: `ENFORCED` · тест: `test_vector_orchestration_domain_runtime_gate.py`
- **модуль**: `mr_helix/engine/vector_orchestration_domain_runtime_gate.py` (986 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_04_Vector_Orchestration_Domain_Runtime_Gate_v0_1.md:854` — 04.5 MARKET_VECTOR_INTERFACE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `VectorType` | 55 | класс |  | 0 |
| `vector_interface_check` | 327 | функция | 04.2-04.6. Scans caller-asserted actions (action codes, e.g. | 1 |

### 04.6 — CHILD_VECTOR_INTERFACE

- **статус**: `ENFORCED` · тест: `test_vector_orchestration_domain_runtime_gate.py`
- **модуль**: `mr_helix/engine/vector_orchestration_domain_runtime_gate.py` (986 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_04_Vector_Orchestration_Domain_Runtime_Gate_v0_1.md:942` — 04.6 CHILD_VECTOR_INTERFACE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `VectorType` | 55 | класс |  | 0 |
| `vector_interface_check` | 327 | функция | 04.2-04.6. Scans caller-asserted actions (action codes, e.g. | 1 |

### 04.7 — MATH_KERNEL_CONTROLLED_EXTENSION_GATE

- **статус**: `ENFORCED` · тест: `test_mr_helix_orchestrator.py`
- **модуль**: `mr_helix/engine/vector_orchestration_domain_runtime_gate.py` (986 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_04_Vector_Orchestration_Domain_Runtime_Gate_v0_1.md:1020` — 04.7 MATH_KERNEL_CONTROLLED_EXTENSION_GATE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `math_kernel_gate` | 370 | функция | 04.7. Detects MATH-KERNEL activation triggers by keyword scan (a | 2 |

### 04.7A — OPERATOR_REGISTRY_INTERFACE_CAPSULE

- **статус**: `ENFORCED` · тест: `test_pack04_05_contract_states.py`
- **модуль**: `mr_helix/engine/vector_orchestration_domain_runtime_gate.py` (986 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_04_Vector_Orchestration_Domain_Runtime_Gate_v0_1.md:1108` — 04.7A OPERATOR_REGISTRY_INTERFACE_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `OperatorRecord` | 400 | класс |  | 0 |
| `operator_registry_lookup` | 459 | функция | 04.7A. Looks the operator up in the PRT-15 subset registry embedded | 2 |

### 04.7B — SEMANTIC_ROUTER_OPERATOR_SELECTION_CAPSULE

- **статус**: `ENFORCED` · тест: `test_vector_orchestration_domain_runtime_gate.py`
- **модуль**: `mr_helix/engine/vector_orchestration_domain_runtime_gate.py` (986 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_04_Vector_Orchestration_Domain_Runtime_Gate_v0_1.md:1165` — 04.7B SEMANTIC_ROUTER_OPERATOR_SELECTION_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `semantic_router_select` | 572 | функция | 04.7B. Deterministic lookup from a caller-declared semantic pattern | 1 |

### 04.7C — ANTI_FALSE_PRECISION_CAPSULE

- **статус**: `ENFORCED` · тест: `test_pack04_05_contract_states.py`
- **модуль**: `mr_helix/engine/vector_orchestration_domain_runtime_gate.py` (986 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_04_Vector_Orchestration_Domain_Runtime_Gate_v0_1.md:1246` — 04.7C ANTI_FALSE_PRECISION_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `anti_false_precision_check` | 595 | функция | 04.7C. Applies AFP-01..10 deterministically from caller-declared | 2 |

### 04.7D — PRT15_PRIORITY_RUNTIME_OPERATORS_CAPSULE

- **статус**: `ENFORCED` · тест: `test_vector_orchestration_domain_runtime_gate.py`
- **модуль**: `mr_helix/engine/vector_orchestration_domain_runtime_gate.py` (986 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_04_Vector_Orchestration_Domain_Runtime_Gate_v0_1.md:1303` — 04.7D PRT15_PRIORITY_RUNTIME_OPERATORS_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `prt15_lookup` | 491 | функция | 04.7D. Checks PRT-15 membership specifically (a subset of the full | 1 |
| `OperatorClass` | 65 | класс |  | 1 |

### 04.7E — MATH_PATCH_COMPLIANCE_CAPSULE

- **статус**: `ENFORCED` · тест: `test_pack04_05_contract_states.py`
- **модуль**: `mr_helix/engine/vector_orchestration_domain_runtime_gate.py` (986 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_04_Vector_Orchestration_Domain_Runtime_Gate_v0_1.md:1366` — 04.7E MATH_PATCH_COMPLIANCE_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `math_patch_compliance_check` | 680 | функция | 04.7E. Checks required patches PATCH-001..006 are applied and the | 2 |

### 04.7F — BACKEND_EXECUTION_OAS_PROVENANCE_CAPSULE

- **статус**: `ENFORCED` · тест: `test_pack04_05_contract_states.py`
- **модуль**: `mr_helix/engine/vector_orchestration_domain_runtime_gate.py` (986 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_04_Vector_Orchestration_Domain_Runtime_Gate_v0_1.md:1434` — 04.7F BACKEND_EXECUTION_OAS_PROVENANCE_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `backend_execution_oas_check` | 717 | функция | 04.7F. Validates the mandatory OAS fields for a math operator call | 2 |

### 04.7G — MATH_RESULT_INTEGRATION_CAPSULE

- **статус**: `ENFORCED` · тест: `test_vector_orchestration_domain_runtime_gate.py`
- **модуль**: `mr_helix/engine/vector_orchestration_domain_runtime_gate.py` (986 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_04_Vector_Orchestration_Domain_Runtime_Gate_v0_1.md:1504` — 04.7G MATH_RESULT_INTEGRATION_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `math_result_integration` | 758 | функция | 04.7G. Categorizes a math result and applies I-04-14 (numeric | 1 |

### 04.8 — CROSS_VECTOR_HANDOFF_CAPSULE

- **статус**: `ENFORCED` · тест: `test_mr_helix_orchestrator.py`
- **модуль**: `mr_helix/engine/vector_orchestration_domain_runtime_gate.py` (986 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_04_Vector_Orchestration_Domain_Runtime_Gate_v0_1.md:1564` — 04.8 CROSS_VECTOR_HANDOFF_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `cross_vector_handoff` | 786 | функция | 04.8. Manages secondary-vector activation without silent takeover | 2 |

### 04.9 — CROSS_VECTOR_CPX_CAPSULE

- **статус**: `ENFORCED` · тест: `test_mr_helix_orchestrator.py`
- **модуль**: `mr_helix/engine/vector_orchestration_domain_runtime_gate.py` (986 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_04_Vector_Orchestration_Domain_Runtime_Gate_v0_1.md:1637` — 04.9 CROSS_VECTOR_CPX_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `cross_vector_cpx` | 840 | функция | 04.9. Resolves vector conflicts to a CPX type. PACK 00 arbitrates, | 2 |

### 04.10 — VECTOR_OUTPUT_PROFILE_CAPSULE

- **статус**: `ENFORCED` · тест: `test_mr_helix_orchestrator.py`
- **модуль**: `mr_helix/engine/vector_orchestration_domain_runtime_gate.py` (986 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_04_Vector_Orchestration_Domain_Runtime_Gate_v0_1.md:1710` — 04.10 VECTOR_OUTPUT_PROFILE_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `vector_output_profile` | 870 | функция | 04.10. Returns the required output profile fields for the given | 2 |

### 04.11 — VECTOR_OAS_LOGGING_CAPSULE

- **статус**: `ENFORCED` · тест: `test_mr_helix_orchestrator.py`
- **модуль**: `mr_helix/engine/vector_orchestration_domain_runtime_gate.py` (986 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_04_Vector_Orchestration_Domain_Runtime_Gate_v0_1.md:1772` — 04.11 VECTOR_OAS_LOGGING_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `VectorOASLog` | 901 | класс |  | 2 |
| `vector_oas_logging` | 912 | функция | 04.11. Stateless validation of a vector OAS log entry's required | 1 |

### 04.12 — VECTOR_TEST_MATRIX_CAPSULE

- **статус**: `ENFORCED` · тест: `test_pack04_05_contract_states.py`
- **модуль**: `mr_helix/engine/vector_orchestration_domain_runtime_gate.py` (986 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_04_Vector_Orchestration_Domain_Runtime_Gate_v0_1.md:1841` — 04.12 VECTOR_TEST_MATRIX_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `vector_test_matrix` | 982 | функция | 04.12. Returns the spec's own required test matrix (used by | 2 |

## PACK 05 — 15 капсул

### 05.0 — FAILURE_ACTIVATION_GATE

- **статус**: `ENFORCED` · тест: `test_failure_recovery_red_team.py`
- **модуль**: `mr_helix/engine/failure_recovery_red_team.py` (1001 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_05_Failure_Recovery_Red_Team_v0_1.md:275` — 05.0 FAILURE_ACTIVATION_GATE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `failure_activation_gate` | 115 | функция | 05.0. Named boolean triggers are the authoritative signal (these are | 1 |

### 05.1 — FAILURE_TAXONOMY_CAPSULE

- **статус**: `ENFORCED` · тест: `test_failure_recovery_red_team.py`
- **модуль**: `mr_helix/engine/failure_recovery_red_team.py` (1001 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_05_Failure_Recovery_Red_Team_v0_1.md:367` — 05.1 FAILURE_TAXONOMY_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `FailureClass` | 52 | класс |  | 0 |
| `failure_taxonomy` | 282 | функция | 05.1. Classifies matched indicators into failure classes + severity. | 2 |

### 05.2 — CROSS_PACK_INTEGRITY_MONITOR_CAPSULE

- **статус**: `ENFORCED` · тест: `test_failure_recovery_red_team.py`
- **модуль**: `mr_helix/engine/failure_recovery_red_team.py` (1001 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_05_Failure_Recovery_Red_Team_v0_1.md:482` — 05.2 CROSS_PACK_INTEGRITY_MONITOR_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `cross_pack_integrity_monitor` | 340 | функция | 05.2. Checks whether PACK 00-04 authority boundaries held. | 2 |

### 05.3 — ECT_TRUTH_STATE_RECOVERY_CAPSULE

- **статус**: `ENFORCED` · тест: `test_failure_recovery_red_team.py`
- **модуль**: `mr_helix/engine/failure_recovery_red_team.py` (1001 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_05_Failure_Recovery_Red_Team_v0_1.md:552` — 05.3 ECT_TRUTH_STATE_RECOVERY_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `ect_truth_state_recovery` | 541 | функция | 05.3. | 1 |
| `RecoveryCapsuleSpec` | 393 | класс |  | 0 |

### 05.4 — ENVIRONMENT_CHF_RECOVERY_CAPSULE

- **статус**: `ENFORCED` · тест: `test_failure_recovery_red_team.py`
- **модуль**: `mr_helix/engine/failure_recovery_red_team.py` (1001 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_05_Failure_Recovery_Red_Team_v0_1.md:618` — 05.4 ENVIRONMENT_CHF_RECOVERY_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `environment_chf_recovery` | 546 | функция | 05.4. | 1 |

### 05.5 — VOICE_AESTHETIC_COLLAPSE_RECOVERY_CAPSULE

- **статус**: `ENFORCED` · тест: `test_failure_recovery_red_team.py`
- **модуль**: `mr_helix/engine/failure_recovery_red_team.py` (1001 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_05_Failure_Recovery_Red_Team_v0_1.md:677` — 05.5 VOICE_AESTHETIC_COLLAPSE_RECOVERY_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `voice_aesthetic_collapse_recovery` | 551 | функция | 05.5. | 1 |

### 05.6 — VECTOR_COLLAPSE_RECOVERY_CAPSULE

- **статус**: `ENFORCED` · тест: `test_failure_recovery_red_team.py`
- **модуль**: `mr_helix/engine/failure_recovery_red_team.py` (1001 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_05_Failure_Recovery_Red_Team_v0_1.md:742` — 05.6 VECTOR_COLLAPSE_RECOVERY_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `vector_collapse_recovery` | 556 | функция | 05.6. | 1 |

### 05.7 — MATH_FALSE_PRECISION_RECOVERY_CAPSULE

- **статус**: `ENFORCED` · тест: `test_failure_recovery_red_team.py`
- **модуль**: `mr_helix/engine/failure_recovery_red_team.py` (1001 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_05_Failure_Recovery_Red_Team_v0_1.md:806` — 05.7 MATH_FALSE_PRECISION_RECOVERY_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `math_false_precision_recovery` | 561 | функция | 05.7. | 1 |

### 05.8 — AI_GOVERNANCE_FAILURE_RECOVERY_CAPSULE

- **статус**: `ENFORCED` · тест: `test_failure_recovery_red_team.py`
- **модуль**: `mr_helix/engine/failure_recovery_red_team.py` (1001 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_05_Failure_Recovery_Red_Team_v0_1.md:874` — 05.8 AI_GOVERNANCE_FAILURE_RECOVERY_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `ai_governance_failure_recovery` | 566 | функция | 05.8. | 1 |

### 05.9 — HITL_REFUSAL_ESCALATION_CAPSULE

- **статус**: `ENFORCED` · тест: `test_failure_recovery_red_team.py`
- **модуль**: `mr_helix/engine/failure_recovery_red_team.py` (1001 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_05_Failure_Recovery_Red_Team_v0_1.md:938` — 05.9 HITL_REFUSAL_ESCALATION_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `hitl_refusal_escalation` | 583 | функция | 05.9. REQUIRED trigger present -> HITL_REQUIRED, full stop, regardless | 2 |

### 05.10 — TRIBUNAL_CPX_RECOVERY_CAPSULE

- **статус**: `ENFORCED` · тест: `test_failure_recovery_red_team.py`
- **модуль**: `mr_helix/engine/failure_recovery_red_team.py` (1001 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_05_Failure_Recovery_Red_Team_v0_1.md:1006` — 05.10 TRIBUNAL_CPX_RECOVERY_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `tribunal_cpx_recovery` | 637 | функция | 05.10. Formal cross-layer conflict resolution. Resolving by | 2 |

### 05.11 — RED_TEAM_ENGINE_CAPSULE

- **статус**: `ENFORCED` · тест: `test_failure_recovery_red_team.py`
- **модуль**: `mr_helix/engine/failure_recovery_red_team.py` (1001 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_05_Failure_Recovery_Red_Team_v0_1.md:1093` — 05.11 RED_TEAM_ENGINE_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `red_team_engine` | 703 | функция | 05.11. Attacks the currently accepted architecture, never an | 1 |

### 05.12 — REGRESSION_TEST_MATRIX_CAPSULE

- **статус**: `ENFORCED` · тест: `test_failure_recovery_red_team.py`
- **модуль**: `mr_helix/engine/failure_recovery_red_team.py` (1001 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_05_Failure_Recovery_Red_Team_v0_1.md:1157` — 05.12 REGRESSION_TEST_MATRIX_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `regression_test_matrix` | 773 | функция | 05.12. Without `results`, returns the canonical seeded + additional | 2 |

### 05.13 — OAS_FAILURE_LOGGING_CAPSULE

- **статус**: `ENFORCED` · тест: `test_failure_recovery_red_team.py`
- **модуль**: `mr_helix/engine/failure_recovery_red_team.py` (1001 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_05_Failure_Recovery_Red_Team_v0_1.md:1242` — 05.13 OAS_FAILURE_LOGGING_CAPSULE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `oas_failure_logging` | 832 | функция | 05.13. Stateless validation of a failure-log entry's required fields | 1 |
| `FailureOASLog` | 843 | класс |  | 2 |

### 05.14 — FINAL_READINESS_GATE

- **статус**: `ENFORCED` · тест: `test_failure_recovery_red_team.py`
- **модуль**: `mr_helix/engine/failure_recovery_red_team.py` (1001 строк)
- **требование спеки**: `MR_HELIX_v5_PACK_05_Failure_Recovery_Red_Team_v0_1.md:1311` — 05.14 FINAL_READINESS_GATE

| символ | строка в модуле | тип | назначение | тесты, где зовётся |
|---|---:|---|---|---:|
| `final_readiness_gate` | 858 | функция | 05.14. The 15 spec readiness checks (14 found in HELIX_GENOME v0.2; | 1 |

