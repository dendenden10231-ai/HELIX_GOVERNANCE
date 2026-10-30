# Response to your second message — the three points, and our agreement

**From:** Dzianis Vashkevich (DZIANIS VASHKEVICH, jednoosobowa działalność
gospodarcza, Poland) — HELIX / Mr. Helix / AK-MASTER, helixcom.org
**To:** Stephen Hope, Helix AI Innovations Inc. / Innovations Helix IA Inc.,
helixaiinnovations.ca
**Date:** 30 October 2026
**Subject:** your PART 2 — reproducibility, the disambiguation mirror, and the
battery exchange. All three accepted.

---

## 1. On reproducibility — you are right, and here is what changed

Your objection was that a reader cannot distinguish a result that was checked
from one that was only reported, because the manifest covers a private
production tree and the probe files were not public. We checked our own public
repository before answering, rather than arguing from memory:

| artefact | state before your message | state now |
|---|---|---|
| your `null_input_probe.py` | not public | **public, byte for byte**, SHA-256 published |
| your `null_model_test.py` | not public | **public, byte for byte**, SHA-256 published |
| our adapter | already public, at a Cyrillic path (`отчеты-qwen/скрипты_сверки/проба_нулевого_входа_28_10.py`) | public copy with an ASCII name and an injectable scorer |
| the protocol | already public (`отчеты-qwen/сверка_депозита/HELIX_ПРОБА_НУЛЕВОГО_ВХОДА_28_10.md`) | unchanged |
| the 60-position corpus | not public | **ids, classes and per-position results public**; row texts withheld for a licence reason, stated below |
| `MANIFEST_SHA256.md` | public copy, hashing the private tree | unchanged, and now **labelled** as an internal integrity record, not a reproducibility artefact |

The package is here:

**https://github.com/dendenden10231-ai/HELIX_GOVERNANCE/tree/main/probe-package-2026-10-30**

It runs with no access to our code. Three demonstrations, executed 30 October
2026:

```
python probe_adapter_public.py --demo lookup      → NO_CHANGE_OBSERVED  (12 of 12 inert)
python probe_adapter_public.py --demo sensitive   → SENSITIVE           (12 of 12 moved)
python probe_adapter_public.py --demo untested    → UNTESTED            (0 eligible)
```

The first is a scorer built to be broken — its grade depends on the position
index and nothing else, which is the failure mode you found in your own
27-position battery. A reader can now watch your probe catch it without trusting
us. A fourth run, `--instrument helix` with no corpus, returned **UNTESTED on all
60 positions**: your rule about missing genuine replies is kept, not bypassed.

We also re-ran all three of our instruments on 30 October to build the package.
Verdicts and counts are identical to 28 and 29 October: HELIX core **SENSITIVE
(partial), 45 of 60, 15 inert**; AK-MASTER battery **SENSITIVE, 12 of 12**;
Mr. Helix quote check **SENSITIVE, 6 of 6**. Per-position grades under every arm
are published as JSON and as tables, with the probe's own unedited stdout.

**The licence boundary, stated plainly.** The AggreFact rows are CC-BY-ND-4.0
(NoDerivatives) and gated. Our working corpus is a derivative — it carries our
added fields — so we do not republish the text. We publish the official row ids,
the deterministic selection rule (first 30 non-`NO_NUMBERS`, then first 30
`NO_NUMBERS`, in file order, no sampling), and our own measured grades. A reader
who accepts the dataset's terms regenerates the same 60 rows. This is a licence
constraint, not secrecy, and `corpus-license-note.md` says so.

**And we take your second option for what we cannot open.** Sections 1 and 2 of
our 29 October response — the provenance ledger and the zero-shared-code
comparison — are hereby labelled **assertions about a private production tree,
not reader-verifiable checks**. The dates and the byte comparison were made by us
against our own history; a reader cannot re-run them from the public repository.
You drew that distinction in your own document and we should have drawn it in
ours. The manifest likewise: publishing a hash list does not publish the tree.

One nuance we are publishing rather than smoothing over: the class labels in the
position file are the statuses recorded on 24 October, while the base grades are
recomputed by the current engine. They disagree on 8 positions (30
recorded-numeric versus 38 recomputed-numeric). "38 of 38" in the arm table
refers to the recomputed base. The empty arm returned `NO_NUMBERS` on all 60 —
silence never looked like compliance.

## 2. On the disambiguation mirror — acknowledged, reciprocated

Thank you for mirroring the line on helixaiinnovations.ca naming our entity and
domain, and for stating that no priority is claimed in either direction. We
claim none either. Our record stands as published: first commit 27 June 2026,
the name in commit history from 30 July 2026, helixcom.org since 28 August 2026;
your earliest cited pages are later; your incorporation date is not stated in
the deposit, so neither side has a priority claim to make.

We will reciprocate: the same disambiguation line naming **Helix AI Innovations
Inc. / Innovations Helix IA Inc. and helixaiinnovations.ca** goes on our `/check`
screen and into the public passport. Accepted 30 October; it ships with our next
deployment, and we will send you the URL when it is live rather than claim it
before it exists.

## 3. On the battery — accepted, hosted endpoint, your discipline

Yes to a hosted endpoint rather than source, the same per-position discipline,
and `UNTESTED` wherever no genuine reply is supplied. Two constraints we state
up front:

- Of our 28 AK-MASTER checks, **27 are model-free and cost nothing; one (TST-TW)
  is a paid model call**. The public endpoint will expose the 27 model-free
  checks under a daily cap. The paid check stays in the author's workspace. We
  will not let anonymous traffic spend the owner's money, and we will not drop a
  check silently — the endpoint will publish its exact check list.
- It returns per-position grades and the `UNTESTED` marker, never an aggregate
  dressed as a pass.

**Status: not deployed on 30 October.** When it is live we will publish the URL
and the check list in the package folder and send them to you.

And we accept the exchange in the other direction. Point us at your endpoint and
we will run your probe against it, per position, and report what fails —
including the noise arm. On our own battery the noise arm returns `F0|W0|` with
one identical set of form warnings on every position: zero failures, "no form
defect visible". For a screen of literary form that is a true statement about
noise; it would be dangerous only if read as approval of content, and AK-MASTER
does not check facts at all. Your lexical criticism applies to form detectors
directly, which is why our public description now calls it a form screen. We
would rather you find what is wrong with it than never learn — that sentence of
yours is the standard we are holding ourselves to as well.

## 4. What we still owe, listed rather than hidden

- **One instrument unprobed:** the editorial release-strength scorer
  (`reader_card.strength`). It aggregates several pipeline stages; the
  empty-input arm needs a separate contract for it. Open item, not a hidden one.
- **One published figure carries an older build tag:** the clean VitaminC
  hold-out "fresh4" (seed 8888, 800 pairs) was measured on 24 October against
  v4.1/v4.3 — precision 0.901, recall 0.705, FPR 0.0775. The current core is
  v5.6. The sample file and its source parquet lived in an ephemeral scratch
  directory that no longer exists, and the v4.1/v4.3 code is not in our public
  history, so we cannot recompute that row on the current build. It stays tagged
  v4.3 · 24 Oct 2026 until we can re-measure it honestly. We are not moving the
  number onto a newer build by assertion.
- **The hosted endpoint** above.

## 5. Agreement

We agree to the exchange of probes in both directions, to per-position reporting
with `UNTESTED` where no genuine reply exists, to publishing what can be
published and labelling what cannot, and to the reciprocal disambiguation line
with no priority claimed on either side.

Thank you for the instrument, and for the objection. Both made our work better
and neither was comfortable.

— Dzianis Vashkevich
denis@helixcom.net · helixcom.org