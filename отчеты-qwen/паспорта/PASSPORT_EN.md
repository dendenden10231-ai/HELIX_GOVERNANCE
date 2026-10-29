# Three AI products, one rule: the machine may not claim more than it can justify

**Public edition · 27 October 2026 · helixcom.org**
Author: Denis Vashkevich — writer (27 books), software builder, Poznań, Poland.
Contact: denis@helixcom.net · Open dossier: github.com/dendenden10231-ai/HELIX_GOVERNANCE

Every number below can be re-checked with a command; the command is given next to it. Source code and specifications are closed; read access is available to a serious reviewer on request.

---

## 1. In one page

One author built three software products on one website. They share a single design rule: **a language model may only read and label text. Every score, threshold and verdict is computed by ordinary Python code with written formulas, and each number is tied to a line of a written specification.** A number without a specification line is treated as a defect — and this rule was applied to the system itself: four plausible confidence thresholds were found in the code but not in the spec, and were removed.

| Product | What it does | Who it is for |
|---|---|---|
| **HELIX** | Audits an AI answer before a customer sees it: seven types of hallucination, sources, narrative pressure, EU AI Act relevance | Companies putting AI in front of customers; AI/ML teams; fact-checkers; compliance and audit |
| **Mr. Helix** | Investigates a claim or a news story: searches the open web and five scientific databases, weighs source independence, answers with a stated level of proof, writes a short first-person essay, a forecast with probabilities, and a market-link analysis | Journalists, OSINT analysts, researchers, lawyers, newsrooms |
| **AK-MASTER** | A literary engine: sets boundaries for the author before writing, audits chapters against a canon of 30+ protocols, voices books | Writers, publishers, audiobook authors |

Scale of the work (measured 27 October 2026): 243,927 lines of Python in 1,151 files; 124,091 lines of specifications (HELIX 51,876 in 23 files; Mr. Helix 16,113 in 19 files; AK canon 56,102 in 6 files); **8,034 automated tests collected — 5,107 in the main suite and 2,927 in the HELIX suite**, plus browser-level interface tests; 253 HTTP routes and 1 WebSocket route on the live entry point (252 in `api.main` plus `GET /healthz` in `api/railway_entry.py`; the route count was re-measured on 28 October after `GET /api/meta/counts` was added — the endpoint the landing page now reads instead of downloading the whole `/openapi.json` schema); 113 HELIX core modules and 161 AK-MASTER engine modules; 24 MCP tools (the site can be connected to Claude, Cursor and similar clients as a tool server). Models: Azure OpenAI; the AK-MASTER judge can also run on Google Gemini 3.1 Pro.

**What does not exist yet — said plainly:** there are no external users yet, no revenue (a subscription module is built but payments are not connected), and no independent review; all evidence lives in one repository.

---

## 2. HELIX — checking an AI answer

Ordinary protection against hallucination is a second model that grades the first one in prose. It inherits the same flaw: a confident-sounding checker is wrong just as confidently as the thing it checks. HELIX is built the other way round:

1. **The model only labels.** "This looks like a claim", "this source is anonymous", "this phrase is an unsupported amplification".
2. **Code decides.** Scores, thresholds and the final verdict (*block / human needed / allow*) are named Python functions with behavioural tests.
3. **The model is forbidden to return numbers.** The classifier prompt allows only labels, quotations and four 0–3 grades; an attempt to return its own number breaks parsing at code level.
4. **A skipped check is reported as skipped.** If a check did not run, the output says `NOT_RUN` or `SKIPPED` with a reason — never "clean".

In engineering terms: a neuro-symbolic system — a neural network extracts meaning, a symbolic layer makes decisions.

**Four vectors, in strict order:** INTELLIGENCE (live-search investigation, 33 protocols) → TRACE (risk index, analysis of competing hypotheses, "who benefits", traces of a planted document) → GOVERNANCE (audit of the model output) → MARKET (economic link; built for news inside Mr. Helix, not yet as a stand-alone HELIX vector).

**Why it matters.** A company answers for what its chatbot says: in *Moffatt v. Air Canada* (2024) a bot invented a discount and the court ordered it paid. EU AI Act Article 9 requires risk management for high-risk systems. GOVERNANCE checks the answer **before the customer sees it**.

**Seven hallucination types detected:** invented source · outdated presented as current · amplification without grounds ("may" → "is") · non-existent expert · invented consensus · coincidence as cause · circular citation (AI output used as the source for AI output).

**Verifiable numbers (27 October 2026):** 949 states declared by the HELIX specifications, 0 unreachable by code (`python3 -m helix_pipeline.engine.helix_contract_audit`); 38 of 45 instrument patches executable and behaviour-tested, 6 documentary anchors and 1 blueprint; 2,927 tests in the HELIX suite, 0 failures (`python3 -m pytest helix_pipeline/tests -q`); Mr. Helix — 99 capsules, 583 states, 0 unreachable, 99/99 capsules with behavioural tests and 99/99 reachable from the live site (`python3 -m mr_helix.engine.capsule_contract_audit`, `...capsule_coverage_validator`, `...live_path_audit`).

**Measurements on full corpora (27 October 2026).** *statcheck:* 144,631 test results from the reference set of the statcheck authors — false alarms 59,107 → 0, agreement with the reference program 0.548 → 0.9998 (recall 0.997; decisive errors 0.975). The protocol states the limit plainly: this is agreement with a reference program, not with truth. *Effect sizes from abstracts:* 2,000 fresh PubMed abstracts, 4,827 measures extracted by code, precision 100/100 on a random sample (95% lower bound 0.96), recall ≈0.94 for risk ratios. *"Chernobyl 4" live investigation:* 170 sources, 168 scientific papers (88 PubMed + 25 CyberLeninka), 118 with abstracts; 3 conclusions beyond Wikipedia and 12 papers with figures absent from the Wikipedia articles' reference list (22 references in those articles); 5 claims the search could not confirm — kept and marked, not deleted. *Number-multiplier detector v5.6:* AggreFact, 1,117 pairs — accuracy 0.7973 → 0.8000 (strict mode 0.7333 → 0.7419), false alarms did not rise. Protocols: `docs/HELIX_ЗАМЕР_СТАТИСТИКИ_24_10.md`, `docs/HELIX_ЧЕРНОБЫЛЬ_ПРОГОН_4_НАУКА_ОТЧЁТ.md`, `docs/HELIX_ЗАМЕР_МНОЖИТЕЛЬ_27_10.md`.

---

## 3. Mr. Helix — investigation with a voice

Mr. Helix is built on the HELIX architecture but is a separate engine with its own "organs" (99 capsules in six packages). It answers a question or a news story with a stated level of proof, and distinguishes **what is claimed** from **what is visible in deeds** (shipments, prices, licences, court filings, money).

### 3.1 What changed on 10–11 October 2026

| Capability | How it works |
|---|---|
| **A literary voice, not a dry system report** | The Mr. Helix persona leads every research round and the final synthesis. A one-image, first-person essay (2,000–4,500 characters) opens each result, with the full analysis below it. The essay is checked by meaning, not by headings, and rejected if it hides weakness behind style. |
| **"Deeds, not words"** | Every conclusion separates *claimed* from *visible in deeds*. A claim without a deed is marked as such. |
| **Source rules** | Reprints and relays (aggregators, wire copies) count as **one** source. Anonymous sources are capped at evidence level ECT-3. "Breaking" and the first 24 hours are treated as less reliable. A screenshot or post without its original is quarantined until the original is found. |
| **Who benefits — by Heuer's method (ACH)** | Three hypotheses are kept alive: H1 intent, H2 information asymmetry, H-NULL "the benefit appears only after the fact". The winner is the one with the fewest contradictions, not the most confirmations. No traces of preparation before the event → "intent not proven". |
| **Forecasts with a scoring system** | A "what happens next" section gives 2–3 scenarios, each with an ICD 203 probability word (almost certain 95–99% … almost impossible 1–5%), a sign to watch, a check date and a resolution criterion. Forecasts are extracted by code and stored. A blind-closing and **Brier-score** module (with Brier Skill Score against the base rate) is built; no forecast has been closed yet, so **no accuracy figure is claimed**. First reconciliations: 15 and 30 October. |
| **Market statistics** | For market stories the system downloads two years of daily prices and fits a **GJR-GARCH(1,1)** volatility model with a **Cornish-Fisher** tail correction: "did the news move the market beyond noise?", a 21-day band, shock half-life, a fear index (OVX/VIX). Futures roll days are excluded (a fake −14.8% "crash" on 2 Feb 2026 was found and removed). Moves are classified (basis shift / rumour / panic / noise) — **never as trading advice**. |
| **MARKET for news** | Actors, money flows, verbatim-checked quotations, a risk index, ACH, pre-event positioning, relay detection and an **answer-depth score 0–100** with named gaps. Not a trading signal and not financial advice. |
| **Organ loop** | After a draft, the Mr. Helix organs check the text; their findings go back to the model for repair; a repair that makes the text worse is rejected. |
| **Human decides** | The system never blocks a story by itself: every refusal becomes a list of causes, and the owner publishes — or does not — on his own responsibility. |

### 3.2 Live results (11 October 2026, first full run on the new method)

| Story | Reader card verdict | Strength of analysis (0–100, computed by code) | Cost |
|---|---|---|---|
| US–Russia deal on Russian diesel | Inflated | 75 | €1.34 |
| Russia promises more diesel to world markets | Partly true | 62 | €1.60 |
| OpenAI "revenue clarification" and AI-stock sell-off | Inflated | 83 | €1.12 |
| SpaceX allegedly raising $40bn for Nvidia chips | Not confirmed | 56 | €1.33 |
| Crew-12 returns from the ISS | Mostly true | 72 | €1.42 |
| Hurricane Simon off Mexico | Inflated | 69 | €1.23 |
| Trump, Zelensky and strikes on refineries | Inflated | 70 | €1.36 |
| "Claude gave police a false lead" | the model provider's own filter refused round 1; no analysis produced | — | €0.11 |

On the two samples checked end to end (diesel; Trump/refineries) the chain ran in full: essay of 3.8–4.2k characters, MARKET depth 85–91/100, volatility statistics, ICD 203 forecasts, organs PASS. One analysis is about 16 model calls and 20–30 web searches; web search is the main cost.

### 3.3 Reader-facing outputs

A short **reader card** without internal codes (verdict, one-line essence, what is true, where it is stretched, who benefits from the framing, a quotation of pressure with an explanation, two questions to ask yourself); an English version of the whole issue; a ready **LinkedIn post** (English only); a Telegram channel post in two languages; a Telegram bot that answers a forwarded claim in the user's language and refuses to hand out its own prompt.

---

## 4. AK-MASTER — a literary engine

It writes under discipline rather than "improving style". It checks whether a text holds as narrative: did the hero pay for what he got; is testimony distinguishable from guesswork; is a device passed off as an event; is a motive replaced by a pretty sentence. The canon (AK-6.7/6.8) has 30+ protocols, each with a trigger condition and a marker.

- **Discipline before writing.** Before a scene the author closes eleven fields (scene type, point of view, hero's price, two readings…). A field filled with generic words is graded WEAK, not CLOSED.
- **Free mechanical audit first.** 27 of 28 checks run without any model. On a full book the free audit matched the paid judge in **11 of 12 failure categories** — nearly all the value at zero cost.
- **Paid judge, by choice.** Azure OpenAI or **Gemini 3.1 Pro (Google Vertex)**, selected by one setting. A daily safeguard stops runaway use: every judge call carries the whole canon (≈250,000 tokens), and the system stops "heavy" calls at a daily limit instead of letting a forgotten loop run all night.
- **Library audit.** 29 books, 2,428 scenes, 7.2 million characters analysed.
- **Audiobooks.** Russian and Polish through Azure neural voices, English through Mistral; the missing "ё" is restored automatically where only one reading is possible.
- **MCP server.** 24 tools: the discipline can be plugged straight into Claude, Cursor and similar clients.

---

## 5. The method in one paragraph

Three habits run through all three products. **(1)** Models label; code counts. **(2)** Silence is explicit: `NOT_RUN` with a reason beats a false "clean". **(3)** The author's own mistakes are logged and become tests: a dated log of the agent's errors (what was claimed, what was true, the one-second command that would have caught it) is part of the repository, and each lesson is turned into a guard in code — for example the safeguard against paying for the whole canon on every call.

Methodology borrowed from published practice, with its limits stated: ICD 203 probability scale and Brier scoring (forecast accuracy); Heuer's Analysis of Competing Hypotheses; GJR-GARCH and Cornish-Fisher quantiles (volatility); source-reliability rules from media-verification practice. Trading rules ("buy", "short") found in the source research were **deliberately not adopted** — Mr. Helix gives no financial advice.

---

## 6. Honest limits

1. **No external users yet** — no reviews, no case studies, no accuracy figures on customer data. The only third-party measurements are the published benchmarks in §2 (the statcheck reference set and AggreFact's 1,117 pairs); no accuracy figure is claimed for live news beyond those.
2. **No independent review.** A reviewer is entitled to discount evidence that lives in one repository.
3. **The forecast scorecard has just started.** Forecasts with probabilities and dates are recorded; none has resolved. A proportion of correct calls will exist after the first reconciliations (15 and 30 October).
4. **Part of the product runs in economy mode:** news — one analysis a day; investigations on request; one setting lifts it.
5. **Statistics are context, not prediction.** Volatility bands describe what is statistically unusual; they are not trading signals.

---

## 7. Assets and ways to work together

1. **HELIX GOVERNANCE** as a "check the AI answer before the customer sees it" service — the core runs on the site; for B2B it still needs client API keys, quotas and an exportable report.
2. **Mr. Helix** as a fact-checking and "what stands behind the news" desk for newsrooms and analysts — the first full run reads like a careful editor's work, with deeds separated from claims.
3. **AK-MASTER** for authors — the free audit nearly matches the paid one at zero marginal cost; an MCP server for authors working in Claude or Cursor.
4. **The author's library:** 27 books, 21 voiced.
5. **Specifications and methodology** (124,091 lines): licensing, consulting, training teams on "how not to believe a model".
6. **Open dossier and passports** on GitHub. The author is open to collaboration, partnership, sponsorship, licensing or acquisition.

---

## 8. Where to look

| What | Where |
|---|---|
| Live site | https://helixcom.org |
| Open dossier and passports | github.com/dendenden10231-ai/HELIX_GOVERNANCE |
| Re-check HELIX contract | `python3 -m helix_pipeline.engine.helix_contract_audit` |
| Re-check Mr. Helix contract | `python3 -m mr_helix.engine.capsule_contract_audit` |
| Re-check AK-MASTER canon | `python3 -m engine.coverage_validator` |
| Tests | `python3 -m pytest -q` and `python3 -m pytest helix_pipeline/tests -q` |

Code and specifications are closed; read access is given to a serious reviewer on request. All numbers can be reproduced within an hour.
