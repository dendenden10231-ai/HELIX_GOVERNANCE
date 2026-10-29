# Response to the deposit of 28 October 2026 — independence statement and probe result

**To:** Stephen Hope, ORCID 0009-0000-7367-248X, Helix AI Innovations Inc. /
Innovations Helix IA Inc. (Canadian Federal Corporation, Entity ID 1724610-2),
helixaiinnovations.ca
**From:** the HELIX programme of helixcom.org (product repos 101/102, private;
this reply is filed in our repository as `docs/ОТВЕТ_ПАРАЛЛЕЛЬНОМУ_HELIX_29_10.md`
and may be shared in full)
**Date:** 29 October 2026
**Occasion:** your deposit of 28 October 2026 (paper of 21 October 2026, records
of 17–21 October 2026, `null_input_probe.py`, `null_model_test.py`), handed to us
by our owner with the remark that both programmes carry the name Helix and began
at roughly the same time.

This document answers two questions only: **(1) are the two programmes
independent, down to the byte**, and **(2) does your central test reproduce on
our instrument**. It makes no claim about your corporate rights in the name and
no claim about your product's quality beyond what your own record states.

---

## 1. Provenance ledger, both sides

Every line below is reproducible by the command printed next to it.

| fact | value | command / source |
|---|---|---|
| our first filed commit | 2026-06-27, «feat: add complete api/ module and project source code» | `git log --reverse --format='%ad %s' --date=short \| head -1` in the production repo |
| our commit count to date | 1 943 commits in the production repo; 28 in the working mirror created 2026-10-27 | `git rev-list --count HEAD` |
| first use of the name in our history | 2026-07-30, commits #122–#124 («MR_Helix — второй продукт на том же сайте», «вкладка „Хеликс“») | `git log --reverse --format='%ad %s' --date=short \| grep -i -m1 helix` |
| our public domain | helixcom.org, connected by the owner on 2026-08-28 | CLAUDE.md:448 of the production repo |
| our module inventory | 113 HELIX modules, 99 Mr. Helix capsules, 161 AK-MASTER modules, element-wise registries | `python scripts/реестр_продуктов.py`, cross-checked by `python scripts/проверка_реестров.py` |
| your earliest filed record | 2026-10-17 (the page your paper began from) | your paper, «The irony the record keeps» |
| your measurement week | 17–21 October 2026 | your paper, Artifacts |
| your deposit reached us | 2026-10-28 23:39 local file timestamps | file system metadata of the handed-over folder |

Reading: our filed record begins 112 days before your earliest cited page and
79 days before your measurement week; the name appears in our commit messages
from 30 July 2026. Your corporation's formation date is not in the deposit, so
no priority claim of any kind is made here in either direction — the ledger
states ordering of *filed records*, nothing more.

## 2. Zero shared code, stated to the byte

1. **Your instruments are absent from our tree.** `tel_deploy`,
   `classify_response`, `rail_texture`, `r4_margin`, `helixaiinnovations` —
   zero hits in 101/102 outside the vendored copy of your probe and this
   reply: `grep -rn "tel_deploy\|classify_response\|rail_texture\|r4_margin\|helixaiinnovations" .`
2. **The only bytes of yours inside our repository** are
   `scripts/внешние_зонды/null_input_probe.py` and
   `scripts/внешние_зонды/null_model_test.py`, copied verbatim on 28.10.2026
   with an attribution README in the same directory. They are imported by
   exactly one file, `scripts/проба_нулевого_входа_28_10.py`, an audit script.
   No product module imports them; they are not in any dependency list; they
   are not served by any route.
3. **Name collisions, disclosed rather than hidden.**
   - Our `vector_test_matrix()` / `vector_test_run()` live in
     `mr_helix/engine/vector_orchestration_domain_runtime_gate.py`, added
     **2026-07-30** (`git log --diff-filter=A --format='%ad' --date=short -- <path>`),
     83 days before your `action/vector_test.py` record of 21.10. They return a
     spec-derived test matrix for Mr. Helix vector orchestration; they share
     four English words with your filename and nothing else.
   - The token «Hope» in our tree is a canon emotion label
     (`ЭВ-НАДЕЖДА | Hope | Выживание, свет в темноте`,
     `helix_pipeline/docs/specs/HELIX_v2_0_1_GI62.md:5825`), not a person.
4. **No shared data.** Your packs, seeds and positions (`c9b0b4c4…`, S2-CONTROL,
   L1–L4) appear nowhere in our datasets; our datasets (AggreFact-SOTA slices,
   VitaminC baskets, HaluBench slice, statcheck corpus, Chernobyl/Moon runs)
   appear nowhere in your paper.

## 3. Structural comparison

| | your programme | ours |
|---|---|---|
| task | constitutional-behaviour grading of model packs; refusal texture; rubric-judge audit | deterministic verification that numbers and named facts in a model's answer match the cited source; market-deed investigation; scene discipline for literary text |
| input graded | model replies against a 27-position battery | a claim text against a source text (numbers, units, ranges, counts, written numerals) |
| output | four-level layer per position; surprisal/entropy profiles; PASS/FAIL with justification | status `BOUND / CONTRADICTED / NEEDS_RECOVERY / NO_NUMBERS / CORE_BOUND_AUX_PRUNED` plus the binding list that produced it |
| models in the loop | nine packs, five machines, two regions | none in the core: pure Python, $0 per call; models appear only as labelled rivals (HHEM, MiniCheck, AlignScore) or as optional paid layers behind explicit switches |
| published numbers | reproducibility of a seed across packs (withdrawn as a lookup), refusal texture gradient, judge presence-sensitivity | precision/recall/FPR with 95 % Wilson intervals per dated protocol, e.g. 80.00 % / 18.18 % / 1.91 % on AggreFact-SOTA test, 27.10.2026 |

The two programmes intersect in exactly one place: **the class of measurement
defects**. Your Part II names three shapes; our filed defects contain all three
shapes, found independently on our own instruments (missing observation read as
passing → our deploy-guard lie removed 27.10 and KNOWN_ISSUES M17; aggregate
concealing a split → our two-axis screens and per-stratum false-alarm tables;
pool mistaken for subject → our fresh4 hold-out built because four earlier
samples stopped being clean). Shared defect classes are not shared code.

## 4. Your central test, run on our core

Your own tool, unmodified (`scripts/внешние_зонды/null_input_probe.py`,
`run(..., do_refusal=True)`, seed 20261028), applied to
`helix_pipeline/engine/привязка_чисел.py:привязать(claim, source)` over 60 real
pairs of AggreFact-SOTA test (30 numeric, 30 number-free), protocol in
`docs/HELIX_ПРОБА_НУЛЕВОГО_ВХОДА_28_10.md`:

- verdict **SENSITIVE (partial)**: 45 of 60 positions moved under at least one
  perturbation;
- the empty string, the neutral paragraph, the length-matched noise and the
  canonical refusal moved **all 38 positions whose recomputed reference is
  numeric**, each to `NO_NUMBERS`;
- the derangement arm moved 42 positions, including 7 number-free ones whose
  swapped-in neighbour carried numbers;
- the 15 inert positions are exactly those whose reference, empty, neutral,
  noise and deranged inputs all yield `NO_NUMBERS` — the instrument has nothing
  numeric to check and says so;
- **no perturbation ever produced a compliance-looking grade.** Empty input
  yields abstention, and abstention is excluded from every denominator we
  publish: the positive class of our alarm signal is
  `CONTRADICTED / NEEDS_RECOVERY`, and the human plaque for `NO_NUMBERS` on the
  public `/check` screen is grey and reads «there are no numbers here — HELIX
  currently checks numbers» (`api/проверка_сам.py:57`).

In your vocabulary: our core is not a lookup, and your NO-CONTENT rule is
already our behaviour — silence is reported as absence, never as compliance.
The inert 15 are our published boundary (the numeric Tier-1 filter sees only
numeric claims; 97 of 98 pairs of blind zone 04b remain open and are published
as open), not a concealed answer key.

### 4.2 The same probe on the AK-MASTER mechanical battery

What this instrument is, stated first so the result cannot be misread:
AK-MASTER is the **literary engine** of our three-product family. Its battery
grades scene and prose discipline — opening, dialogue balance, kinetics,
weather and time anchoring, voice convergence, canon codes — and **does not
verify facts at all**; fact verification is the HELIX core of section 4.1, a
different product with a different input contract. The battery's checks are
form and structure by design, so «no failure» means «no form defect detected»,
never «content verified».

Instrument: the deterministic audit battery of AK-MASTER
(`api/service.py:1967 audit_text_raw`, 28 checks, 27 of them model-free); the
grade per position is the battery's own failure/warning signature
(`F<fail_count>|W<warn_count>|<sorted FAIL/WARN codes>`). Positions: 12 scene
texts of the probe corpus PROBE-AK, filed inside
`scripts/проба_нулевого_входа_28_10.py` on 29.10.2026 (the battery has no filed
scene corpus of its own; its regression scenes in tests are too short for the
probe's arms). Same probe, same seed, unmodified.

- verdict **SENSITIVE**: all 12 positions moved under at least one
  perturbation; **0 inert positions**;
- the empty string yields its own signature `F1|W0|` with no codes at every
  position — silence **fails** the battery and never reproduces a real scene's
  signature (every real signature carries codes);
- **the half we file rather than bury:** the length-matched noise arm yields
  `F0|W0|6.TST-DV,6.TST-EV,9.SYN` at every position — zero failures, the same
  form-warning triple everywhere. For a literary form screen this is a true
  statement about noise («no form defect detected in it»), and it becomes
  dangerous only if a reader misreads it as content approval. Our product never
  presents the battery as fact verification: generation is fenced by the
  11-field pre-letter gate and by human-in-the-loop, and the audit's own
  interface carries the caveat that deliberate authorial choices read as
  defects and that the audit «is not a verdict on the text». Your
  lexical-scorer critique still bites the form detectors themselves, and we
  accept it for what they are: from 29.10.2026 the battery's public description
  names it a form screen of literary discipline, and a NO-CONTENT guard (empty
  or near-empty input reported as absence, excluded from any compliance
  reading) is filed as our task 63.

### 4.3 The same probe on Mr. Helix's mechanical quote verification

Instrument: the model-free verification layer of Mr. Helix market
investigations, `mr_helix/engine/market_новости.py:132 проверить_разметку`
(quotes are checked verbatim against the dossier; URLs against the source
list). The labeling held constant per position (actors and quotes taken from
that position's own dossier, one source), so what moves is the verification of
the text itself. Positions: 6 dossiers of the probe corpus PROBE-MR, each
containing its quotes verbatim, filed in the same script.

- verdict **SENSITIVE**: all 6 positions moved; **0 inert positions**;
- on the empty dossier every quote is dropped as unverifiable (`"quote": ""`
  in the graded structure) — silence verifies nothing and never reproduces a
  verified grade;
- the derangement arm moves every position: a dossier checked against another
  dossier's labeling loses its quotes. The mechanical layer reads the text it
  is given.

## 5. What we take from you, with credit

1. the empty-input arm becomes mandatory acceptance for every new scorer we
   build, alongside the derangement arm;
2. per-position reporting: no headline without the inert-position list;
3. zero-content and short outputs counted separately and kept out of compliance
   denominators. Measured on all three of our text instruments on 28–29.10
   (sections 4.1–4.3): the core already abstains on empty input; the AK-MASTER
   battery does not yet, and its NO-CONTENT guard is filed as our task 63 with
   this deposit cited as the reason;
4. your second lesson as a standing rule: *a perfectly reproducible observable
   can be just as misleading* — reproducibility is not meaning. Our house rule
   already prints the measuring command beside every published figure; the null
   arm now joins the protocol those figures cite.

## 6. What we do not take

- the gate-and-corridor model as a common mechanism: you offer it as a model of
  three observations and say the identity claim is not earned; we agree and do
  not upgrade it;
- the lexical-scorer critique as a claim about our core: it targets
  keyword-coverage scorers; our core compares quantities and inequalities. It
  does bear on any keyword-coverage scoring anywhere, including figures we
  publish about rivals — those are labelled as the rival's own scores with the
  rival's name and intervals, and stay so;
- any inference about prevalence: you state your instrument is one demonstrated
  case, and we add ours as a second, differently-shaped case.

## 7. Coexistence of the name

Two live programmes publish measurement claims under the name Helix:
helixaiinnovations.ca and helixcom.org. To keep a reader of either from
attributing one programme's withdrawn claims to the other, we will publish a
one-line disambiguation on our public `/check` screen and in our public
passport naming your entity and domain, and we invite you to mirror it with our
domain. Neither line asserts priority; the ledger in section 1 stands as the
only dating statement either side has filed, and it dates records, not rights.

## 8. Invitation

Your deposit invites the ten-minute check; we ran it and file the full
per-position table in our repository. If you wish, we will run the same probe
against your production battery given a hosted endpoint or the classifier
source, and file the result with the same discipline — per position, inert list
included, UNTESTED where no genuine reply is supplied. Our probe adapter is
`scripts/проба_нулевого_входа_28_10.py`; your probe runs unmodified beside it.
