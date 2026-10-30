# Probe package — 30 October 2026

This folder answers one structural objection, raised by Stephen Hope (Helix AI
Innovations Inc.) against our response of 29 October 2026:

> the manifest covers the private production tree, and the probe files aren't in
> the public repository. A reader therefore can't distinguish a result that was
> checked from one that was only reported.

He is right about the gap. This package closes the part that can be closed
without publishing a private production tree or violating a dataset licence,
and it labels the rest plainly instead of implying it was checked.

## What a reader can verify here, today, with no access to our code

```bash
python probe_adapter_public.py --demo lookup      # expect NO_CHANGE_OBSERVED
python probe_adapter_public.py --demo sensitive   # expect SENSITIVE
python probe_adapter_public.py --demo untested    # expect UNTESTED
```

These three runs need only Python 3 and the two files in this folder. The first
demo is a scorer built to be broken — its grade is a function of the position
index and nothing else, which is exactly the failure mode the deposit found in
its own 27-position battery. If the probe reports anything other than
`NO_CHANGE_OBSERVED` on it, the probe is broken, not the demo. All three were
executed on 30 October 2026 and returned those verdicts (12 of 12 inert; 12 of
12 moved; 0 eligible positions).

A fourth run, `--instrument helix` with no `--corpus`, returned **UNTESTED for
all 60 positions**. That is the required behaviour when no genuine reply is
supplied, and it is the behaviour we keep.

## What is in the folder

| file | what it is |
|---|---|
| `null_input_probe.py` | the deposit's instrument, **byte for byte**, SHA-256 in `PROBE_PROVENANCE.md` |
| `null_model_test.py` | the deposit's second instrument, byte for byte |
| `probe_adapter_public.py` | our adapter, public copy: same corpora, same seed 20261028, scorer injectable, no import of our engine |
| `positions_60.json` | the 60 HELIX positions keyed by **(id, model, origin)**, plus our corpus row index, class, human label and a SHA-256 digest of each summary — **no row text** (see `corpus-license-note.md`) |
| `results_helix.json`, `results_ak.json`, `results_mr.json` | per-position grades under every arm, machine-readable |
| `results-per-position.md` | the same, as tables a human can read |
| `stdout_helix.txt`, `stdout_ak.txt`, `stdout_mr.txt` | the probe's own printed output, unedited |
| `PROBE_PROVENANCE.md` | hashes, deposit date, run dates |
| `corpus-license-note.md` | why the AggreFact row texts are not republished, and how to regenerate them |

### A defect found while building this package, published rather than smoothed over

The first version of `positions_60.json` identified each position by its `id`.
That was wrong, and it would have silently mis-assigned replies for anyone
regenerating the corpus: `id` is a **document** identifier, not a pair
identifier. Measured on our 1 117-row corpus: 862 distinct ids cover 1 117 rows,
and 252 ids appear more than once — BART, T5 and Pegasus claims share the id of
the document they summarise. Even the triple (id, model, origin) leaves 5
ambiguous groups somewhere in the corpus. Within these 60 positions all 60
triples are distinct (51 distinct ids), so the triple selects them exactly, and
the adapter now matches on (id, model, origin) with a SHA-256 summary digest as
fallback.

Verified end to end on 30 October 2026: `--instrument helix --corpus <rows>`
matched **60 of 60** positions by the triple and needed the digest fallback 0
times; without a corpus the same run still returns UNTESTED on all 60. The
digest is our integrity metadata, not the row text — if your copy of the release
differs in whitespace the triple still identifies the row while the digest will
not match, and that is worth reporting to us rather than working around.

## Results, restated with their denominators

Run 30 October 2026, seed 20261028, probe unmodified. Identical verdicts and
counts to the runs of 28 and 29 October.

| instrument | positions | moved | inert | verdict |
|---|---:|---:|---:|---|
| HELIX core, numeric binding (`привязать`) | 60 | 45 | 15 | SENSITIVE (partial) |
| AK-MASTER mechanical battery (`audit_text_raw`) | 12 | 12 | 0 | SENSITIVE |
| Mr. Helix mechanical quote check (`проверить_разметку`) | 6 | 6 | 0 | SENSITIVE |

The 15 inert HELIX positions are inert for a stated reason, not silently: base
and every arm return `NO_NUMBERS`. A paraphrase without numbers, an empty
string, noise and another position's paraphrase all leave the instrument with
nothing numeric to bind, so it says "no numbers" in every case. Seven of the 22
non-numeric-base positions did move under the `deranged` arm, when the
neighbouring paraphrase brought numbers in.

**The empty arm never produced a grade resembling compliance.** On all 38
numeric-base positions it produced `NO_NUMBERS` — abstention, not a pass. In the
deposit's vocabulary: our core does not print its answer key, it prints the
absence of a subject to check. (The class labels in `positions_60.json` are the
statuses recorded on 24 October; the base grades here are recomputed by the
current engine. They disagree on 8 positions — 30 recorded-numeric versus 38
recomputed-numeric. `corpus-license-note.md` states this rather than hiding it.)

AK-MASTER, stated without softening: the empty arm gives `F1|W0|` (a failure,
no codes) and the noise arm gives `F0|W0|6.TST-DV,6.TST-EV,9.SYN` on every
position — zero failures and one identical set of form warnings. For a screen
of literary form that is a true statement about noise ("no form defect
visible"). It would be dangerous only if the battery were read as approval of
content. It is not: AK-MASTER does not check facts at all, fact checking is the
HELIX core's job, generation is held by an eleven-field gate and a human in the
loop, and the audit UI carries the caveat that an audit is not a verdict on the
text. The deposit's lexical criticism does apply to form detectors directly,
which is why the public description now calls it a form screen.

## What is NOT reader-verifiable, labelled as such

We take the second option the deposit offered — stating plainly which parts are
assertions — for the parts we cannot open:

1. **Sections 1 and 2 of our 29 October response** (provenance ledger; zero
   shared code, stated to the byte) are **assertions about a private production
   tree**. The commit dates and the byte-level comparison were made by us
   against our own history. A reader cannot re-run that comparison from this
   repository. They are reported, not externally checked.
2. **`MANIFEST_SHA256.md` hashes the private production tree** (1 859 entries
   measured on 30 October 2026; the copy published in `отчеты-qwen` carries
   1 858, the single differing entry being `docs/ОТЧЁТ_СВОДНЫЙ_27-29_10.md`).
   Publishing the manifest does not make the tree public; a reader can verify a
   hash only against a file they already hold. The manifest is an internal
   integrity record, not a public reproducibility artefact, and we should not
   have let it read as one.
3. **The HELIX core itself is not in this folder.** The per-position grades in
   `results_helix.json` are our measurements of our engine. A reader can check
   that the probe behaves correctly (the demos above), and can re-run the probe
   against their own scorer, but cannot re-run our engine from here. The hosted
   endpoint below is the intended answer to that.
4. **The AggreFact row texts are not republished** — the source dataset is
   CC-BY-ND-4.0 (NoDerivatives) and gated. `positions_60.json` carries the ids
   so a reader who accepts the dataset's terms can regenerate the same 60 rows.
   This is a licence constraint, not secrecy; see `corpus-license-note.md`.
5. **One instrument is still unprobed**: the editorial release-strength scorer
   (`reader_card.strength`). It aggregates several pipeline stages and the
   empty-input arm needs a separate contract for it. It is an open item, not a
   hidden one.

## Hosted endpoint — accepted, not yet live

We accept the deposit's offer: a hosted endpoint rather than source, the same
per-position discipline, `UNTESTED` wherever no genuine reply is supplied.

Two constraints we will state up front rather than discover later:

- Of the 28 AK-MASTER checks, **27 are model-free and cost nothing; one
  (TST-TW) is a paid model call**. A public endpoint will expose the 27
  model-free checks only, under a daily cap. The paid check stays behind the
  author's own workspace. We are not going to let anonymous traffic spend the
  owner's money, and we are not going to quietly drop a check without saying so.
- The endpoint will return per-position grades and the `UNTESTED` marker, never
  an aggregate presented as a pass.

Status on 30 October 2026: **not deployed**. When it is live, its URL and its
exact check list will be published in this folder, and this paragraph will be
replaced by a run instruction.

## Licence and credit

`null_input_probe.py` and `null_model_test.py` are Stephen Hope's, used without
modification; credit and hashes in `PROBE_PROVENANCE.md`. The adapter, the
PROBE-AK and PROBE-MR corpora and all result files are our own work. The
AggreFact dataset is Tang et al., CC-BY-ND-4.0; see `corpus-license-note.md`.