# HELIX — Reader's Guide to the Specifications

**For English-speaking reviewers.** The HELIX specifications are written in
Russian — they are the author's originals, and the code is verified against
their exact wording, so they are not translated: a translation would become a
second source of truth that could silently drift from the one the code is
tested against.

This guide exists so that an English reader can navigate them anyway. It maps
what lives where, names every protocol in English, and explains the concepts
and abbreviations you need to read a Russian section and know what it governs.

Prepared 19 August 2026. Figures from a live repository run on that date.

---

## 1. The shape of the whole thing

Five specification documents matter. Everything else is either a draft,
a deliberately unbuilt product, or a reference.

| Document | Lines | What it governs |
|---|---:|---|
| `GI_v6_2_COMPLETE.md` | 8,965 | **The shared core.** 45 tracked patches (33–71 plus six bridges) — the reasoning machinery all three products stand on. Also carries Appendix A: the verified scientific sources. |
| `HELIX_GOVERNANCE_v1_3_FINAL.md` | 2,565 | **GOVERNANCE.** Auditing a single piece of AI output. Contains the deterministic math (§14–15) and the classifier system prompt (§16). |
| `HELIX_INTELLIGENCE_v2_1.md` | 3,149 | **INTELLIGENCE.** Open-source investigation. 33 verification protocols in §3. |
| `HELIX_TRACE_MERGED.md` | 5,959 | **TRACE.** Adversarial / red-team layer, corporate document forensics. |
| `HELIX_Final_Stabilization_MERGED.md` | 7,724 | **Hardening.** Stress tests (ST-01…20) and a case archive. Reference, not a source of new protocols. |

Not part of the built system, listed so you know why you can ignore them:
`HELIX_MARKET_v1_0.md` (deliberately unbuilt — the spec has not settled),
`HELIX_VERIFY_API_v1_2.md` (author's decision not to build: it duplicates what
the three products already do, and assumes infrastructure that does not exist
here), `HELIX_v2_0_1_GI62.md` (an earlier, superseded version of the core),
`HELIX_Runtime_Spec_v1_1.md` (enterprise multi-tenant architecture, not yet
needed).

---

## 2. The vocabulary you need

Six terms carry most of the meaning. Learn these and Russian section headers
become readable.

**ECT — Evidence Credibility Tier.** The trust level of a fact, ECT-1 to ECT-4.
ECT-4 is publishable as established; ECT-1 is barely more than an allegation.
Almost every protocol's job is to decide whether something may hold its tier,
must be lowered, or must be frozen. `ECT-FROZEN` means a fact is suspended
pending re-verification, not merely downgraded.

**HITL — Human In The Loop.** The point where the machine stops and requires a
person. Split into `HITL_REQUIRED` (the system halts) and `HITL_ADVISORY`
(a human is recommended). Where the two lists overlap, the stricter reading
wins — that rule is explicit in the code.

**H1 / H-NULL.** The working hypothesis and its null. A conclusion that never
seriously constructed H-NULL is treated as unfinished, not as proven.

**Trust Score.** A per-source or per-claim numeric that protocols raise, lower,
multiply, or void. Distinct from ECT: Trust Score is continuous, ECT is a tier.

**Marker.** A bracketed tag the system emits into its report, e.g.
`[SL-4: weapon focus]` or `[AD HOC FLAG]`. Markers are the audit trail: every
consequential decision leaves one, and the report is readable as a chain of
them.

**NON LIQUET.** Latin, "it is not clear" — the verdict when the inputs do not
support any conclusion. A first-class outcome, not a failure state. Much of the
design exists to make the system willing to say this instead of producing a
confident number.

Two more you will meet constantly: **SAP** (Source Authentication Protocol,
nine steps, SAP-1…9) and **FRCP** (Fact Reconciliation & Conflict Protocol —
what happens when two well-attested facts contradict each other).

---

## 3. `GI_v6_2_COMPLETE.md` — the core

Patches 33 through 71, plus six bridges (M1–M6) that fire automatically when
one protocol's output should feed another's input. Of 45 tracked entries,
38 are executable and all 38 are behaviour-tested; the remaining 7 are
reference sections with no executable behaviour.

Highest-value sections for a reviewer:

**Appendix A — Verified Sources** (from roughly line 3,240). Six academic
sources, each with edition, URL, the patches it governs, and its key concepts.
Then an integration matrix: source → cognitive defect → patch → rule → marker.
This is the single most informative page in the entire corpus. It is the reason
the system's numbers are what they are:

| Source | Defect | Patch | Rule |
|---|---|---|---|
| Kahneman 2011 | WYSIATI, System 2 depletion | IFM-42, PPS-55 | Overload blocks System 1 |
| Kahneman 2011 | Attribute substitution | ACH block 5 | Forced decomposition |
| Popper 1959 | Conventionalist stratagems | SSD-51, FRCP-34 | Ad hoc modification banned |
| Deffenbacher & Loftus 1982 | Weapon focus | PDP-X-41 | Facial ID trust × 0.30 |
| Deffenbacher & Loftus 1982 | Photobiased lineup | PDP-X-41 | Identification voided |
| Loftus & Ketcham 1994 | Suggestive implantation | MDP-4 | Trust ceiling forced to ECT-1 |
| Cohen 1972 | Moral panic | MPF-52, SCoA-44 | Five-criteria filter |
| Dror 2006–2021 | Contextual bias in experts | SDF-49 | Non-blind evidence → ECT × 0.70 |

**Patch 51 (SSD)** — Popper's demarcation criterion as an executable test. An
unfalsifiable hypothesis is not a hypothesis; a conclusion resting on one is
"accusation without evidence" in the spec's own words. Includes the ad hoc
prohibition: you may not rescue a hypothesis with an exception that lowers its
falsifiability.

**Patch 41 (PDP-X)** — source memory drift, MDP-1…6. MDP-6 is the weapon-focus
factor: identification trust multiplied by 0.30 regardless of how certain the
witness feels, plus outright voiding of an identification if a photo was shown
first.

**Patch 33 (SSC)** — source status change, five event types: recantation,
coercion, death, hidden link revealed, and bought/turned by the subject. Each
has a distinct consequence; the fifth triggers SAP-7 FAILED.

**Patch 34 (FRCP)** — arbitration when two ECT-4 facts conflict. Can return
*non liquet* rather than forcing a winner.

---

## 4. `HELIX_GOVERNANCE_v1_3_FINAL.md` — auditing AI output

Structure, by Russian section number (`РАЗДЕЛ` = section):

- **§0** — regulatory context: EU AI Act Article 9 compliance mode, the
  *Moffatt v. Air Canada* precedent on AI liability, benchmarks.
- **§0.2** — the architectural security principle. This is where the hard rule
  is stated.
- **§2** — ECT rules specific to AI output, plus the four zones of AI output.
- **§3** — the hallucination map, TYPE-1…7.
- **§4** — the cognitive risk layer: ~18 protocols in AI-adapted form
  (SCA, PDE, NGI, CHF, GL-locks, Phase 9, MPF, ANI, SAD, ICoI, SSD, bridges).
- **§5** — additive confidence score (a separate scale from §14's).
- **§6** — HITL: 8 REQUIRED conditions, 12 ADVISORY.
- **§14–15** — the deterministic mathematics, including a reference Python
  implementation inside the spec itself. CIRI, RPL, NGI, Article 9 scoring,
  and the decision precedence order.
- **§16** — the classifier system prompt, verbatim. The code holds a
  character-for-character copy; divergence is a defect.

The rule in §0.2, which the whole product is built to honour: the language
model returns semantic signals only — labels, excerpts, and four 0–3 dimension
ratings. All arithmetic and the final verdict are computed in Python. A
classifier attempting to return its own confidence number is rejected before
that number can reach a user.

---

## 5. `HELIX_INTELLIGENCE_v2_1.md` — investigation

Section 3 holds 33 numbered protocols. Full English index:

| § | Code | English |
|---|---|---|
| 3.1 | SAP | Source authentication (9 steps) |
| 3.2 | WPL | Witness provenance layer |
| 3.3 | SSC | Source status change |
| 3.3b | SSC-CHAR | Narrator reliability type |
| 3.4 | CDR | Cascading ECT downgrade |
| 3.5 | FRCP | Fact conflict resolution |
| 3.6 | PDE | Document provenance degradation |
| 3.7 | PDP-X | Source memory drift |
| 3.8 | SCoA | Social cascade |
| 3.9 | SAD | Silence as data |
| 3.10 | IFM | Investigator fatigue |
| 3.11 | NGI | Narrative gravity index |
| 3.12 | ANI | Adversarial narrative injection |
| 3.13 | HIL | Hypothesis identity lock |
| 3.14 | RPL | Resource pressure layer |
| 3.15 | HMP | Hypothesis market protocol |
| 3.16 | CHF | Contemporary cognitive environment |
| 3.17 | TIE | Temporal integrity |
| 3.18 | SSD | Hypothesis unfalsifiability (Popper) |
| 3.19 | TELP | Terminal epistemic limit |
| 3.20 | APORIA | False causal-pattern check |
| 3.21 | SDF | Status distortion |
| 3.22 | ICoI | Source conflict of interest |
| 3.23 | STA/DYN | Outdated vs. changed fact |
| 3.24 | RDI-DD | Resolution debt index |
| 3.25 | RDI-DL | Deadline pressure |
| 3.26 | MPF | Moral panic filter |
| 3.27 | EFR | Epistemic fragmentation |
| 3.28 | PPEP | Post-publication evidence |
| 3.29 | CPX | Conflict priority matrix |
| 3.30 | RISK INDEX | Numeric aggregation, 0–100 |
| 3.31 | ST-18 | Recovery protocol |
| 3.32 | UC-5 | AI preflight / postflight |
| 3.33 | — | v6.1 critical combinations |

Then: **§3.M** bridges (automatic protocol-to-protocol links), **§4** protocol
prioritisation (PPS — which protocol runs first under load, and the overload
rule that escalates every trigger one level when five or more fire), **§5**
HITL, **§6** report structure, **§7** the complete marker table, **§8** ACH
(Analysis of Competing Hypotheses), **§9** the final publication protocol,
**§10** cross-product standards, **§12** glossary, **§14** architectural
principles.

§3.33's four named critical combinations are worth knowing: CHAIN DEGRADATION,
STRATEGIC DESTRUCTION, PERSONAL LOCK, RESOURCE-TELP. These are states dangerous
only in concert — no single signal is critical, but together they force the
trust ceiling down and call a human.

---

## 6. `HELIX_TRACE_MERGED.md` — the adversarial layer

TRACE asks a different question: not "is this true" but "who benefits if it is,
and does this document bear the fingerprints of a thing built to be found."

The file merges two documents. The first part carries cross-product standards
and five appendices; the second is the full TRACE master specification.

Appendices in part one:
- **A** — SSC-CHAR, four narrator reliability types.
- **B** — FRCP explicit protocol, including the audit log format.
- **C** — SAP, all nine steps.
- **D** — CDR, cascading downgrade.
- **E** — CHF extension, the tactical layer: MW-TAC (six memetic-warfare
  tactics), SP-FORM (five forms of synthetic persuasion), and the compound
  Trust Score formula.

In the master specification, TRACE-specific protocols worth noting: §4.11
corporate failure-analysis modes, §4.12 its own conflict priority matrix
(distinct from INTELLIGENCE's, a distinction the audit had to correct in code),
§4.18 document transmission depth, §4.19 document back-dating detection, §5 the
risk index.

**Out of scope:** Part II (Backend API — OpenAPI, Neo4j, PostgreSQL, Docker)
and Part III (React frontend) describe enterprise infrastructure that does not
exist in this repository and was never built. Documented explicitly as such.

---

## 7. The math kernel

Separate from the protocol specs: a library of **44 formalised mathematical
operators** across causality (do-operator, back-door adjustment, collider bias,
counterfactual), probability (Bayesian update, beta distribution), graphs
(centrality, clustering, modularity), information theory (transfer entropy),
vectors, statistics, and system dynamics.

Ten absolute laws govern it. The four that define its character:

1. **LLM selects, backend calculates.** The model chooses an operator ID and
   forms the call. It does not compute the value. The returned number is a
   protected fact the model may not modify.
3. **Incomplete inputs → range or NON LIQUET.** Substituting "average" or
   "default" values to make a formula run is forbidden outright.
8. **Independence not proven → sources collapse.** Until a provenance graph
   proves independence, sources count as one cluster. *Ten reprinted press
   releases equal one piece of evidence.*
10. **Formula contradiction → FRCP.** If the model predicts LOW risk while a
    verified fact signals a crisis, the fact always wins. *Mathematics cannot
    overrule a fact.*

A further rule states that a numeric result, however good, never raises an
evidence tier on its own.

---

## 8. How the code relates to the specification

One engine module per protocol, named after it: `ssd.py` implements Patch 51,
`pdp_x.py` implements Patch 41, `sap_protocol.py` implements Patch 71, and so
on — 71 modules, 19,003 lines. A facade class exposes them as one object.

Every constant carries the specification line that justifies it. Any number in
the code that cannot be traced to explicit specification text is treated as a
bug — a principle the project calls **P0-6**, and one it has enforced against
itself: four confidence thresholds that looked derived turned out to appear
nowhere in the specification and were removed.

Coverage is machine-checked, not asserted. A validator distinguishes "symbol
exists" from "behaviour is tested" and reports 38 of 38 executable patches at
100% behavioural coverage.

---

## 9. Where to go next

- **`dossier/HELIX_DOSSIER_EN.html`** — the technical dossier. Quotes the
  running system directly: the system prompt, the CIRI formula, the source
  matrix, four of the ten math-kernel laws, and three documented cases where
  the audit found a defect inside the system itself. Start here.
- **`audit/`** — the six closing reports from the August 2026 line-by-line
  audit. `HELIX_AUDIT_COMPLETE_FINAL.md` is the summary; the others cover
  GOVERNANCE, INTELLIGENCE, TRACE, the core, and file-level coverage.

The specifications themselves, and the code, are available for review on
request. See the contact details in the dossier.
