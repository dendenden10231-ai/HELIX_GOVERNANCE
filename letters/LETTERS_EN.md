# Letters

Four ready-to-send letters for different recipients. Adapt the greeting and the
specifics; leave the numbers alone — they are measured, and their value is that
they are checkable.

Every letter is deliberately short. The dossier carries the weight; the letter
only has to earn the click.

**A note on these being public.** They are published here rather than kept
private because the same case is made to everyone, in the same words. There is
no version of this pitch that softens a number for one reader and hardens it for
another. If you are a recipient and you found this file, that is the point.

---

## 1 · Google Cloud — compute credits

> **Subject:** Deterministic AI verification engine, 6,504 tests — request for extended Gemini credit

Hello,

I have built a verification engine that audits AI output for the failure modes
that make it dangerous to trust: fabricated consensus, invented authority, and
confident language standing in for evidence.

It enforces one rule at the code level, not as a guideline: the language model
may only read and label. Every score, threshold, and verdict is computed by
deterministic Python. A classifier that tries to return its own confidence
number raises an exception before that number can reach a user.

It calls exactly one model provider: **Gemini**. That is a fixed architectural
decision recorded as irreversible, not a default I might drift away from.

Current state, measured against the repository on 21 August 2026:

- 152,080 lines of Python across 738 files; 6,504 tests passing, none failing
  (4,360 in the root suite, 2,144 in the HELIX suite — they run separately by
  design)
- All 70 files of `helix_pipeline/engine/` verified line by line against written
  specification (audit of 19.08; the directory holds 78 files today, the eight
  newer ones are outside that pass)
- 14 discrepancies between specification and code found and fixed, with tests
- Protocols compiled from published research: Popper's demarcation criterion
  runs as an executable test; the Loftus weapon-focus finding is a 0.30
  multiplier on identification trust; Dror's contextual-bias work sets a 0.70
  penalty on non-blind evidence

I am a retired engineer building this alone, on personal funds and the $300
Google Cloud starter credit, which is nearly spent. The expensive part is
exactly the part that makes the product real: live search-grounded Gemini calls
inside actual investigations, not a throttled demonstration.

**What I am asking for:** extended or renewed Google Cloud credit directed at
Gemini API usage, and — if this fits any startup or research-credit program —
a pointer to the right one.

The system is live — a deployed site, not a specification:
web-production-b540f.up.railway.app. You can log in and exercise it now.

The full technical dossier, with source excerpts and the audit record, is here:
[link]

It includes three documented cases where this system found defects inside
itself, including one where the checker committed the exact error it was built
to catch. I would rather show you those than a projection.

Thank you for reading this far.

Dzianis Vashkevich
dendenden043@gmail.com · +48 571 296 605
Luboń, Poland

---

## 2 · Microsoft Azure — infrastructure credits

> **Subject:** Verification engine for AI output — request for infrastructure credit

Hello,

I am building a deterministic verification layer that sits above large language
models and audits their output for fabricated consensus, invented authority, and
persuasiveness substituting for evidence. The architecture's founding rule is
that the model may extract semantics only — all arithmetic and every verdict
runs in auditable Python.

Measured on 21 August 2026: 152,080 lines of Python, 6,504 tests passing, all
70 engine files verified line by line against written specification (audit of 19.08), 14
specification-versus-code discrepancies found and fixed with tests.

In fairness, so you can weigh this accurately: the model calls themselves go to
Gemini, which is a fixed architectural decision. What I am asking Azure for is
different and separate — **hosting and infrastructure credit**, so the live
deployment stays reachable between working sessions rather than being rebuilt
from cold storage each time. The $200 Azure credit I have been running on is
nearly spent.

I am a retired engineer working alone, on personal funds, with no revenue plan.
The goal is not to monetise this but to keep it alive.

Full technical dossier, with source excerpts and the audit record: [link]
Live site: web-production-b540f.up.railway.app

If there is a program this profile fits — solo developer, self-funded, retirement
age, disabled, building infrastructure rather than a product to sell — I would be
grateful for a pointer to it.

Dzianis Vashkevich
dendenden043@gmail.com · +48 571 296 605
Luboń, Poland

---

## 3 · Model developers and research labs — technical review

> **Subject:** Deterministic verification layer above LLMs — asking for a technical read, not funding

Hello,

This is not a funding request. I am asking whether someone on your team would
spend twenty minutes looking at an architecture and telling me where it is
wrong.

I have spent this year building a verification engine that audits LLM output
deterministically. The design premise is that a model grading another model in
prose inherits the exact failure it is meant to catch, so this system does the
opposite: the model is trusted only to read and label — "this looks like a
claim", "this source is anonymous", "this document is dated three weeks after
the event it describes" — and every consequence of that label runs through
named, tested, versioned Python.

What may be of interest to people who build models:

- The system prompt forbids the model from returning any number except four
  0–3 dimension ratings. It cannot utter a confidence score or a verdict.
- A missing provider key yields an explicit `NOT-CONFIGURED` error, never an
  empty result — an empty violations list would assert "checked, clean" without
  having checked.
- Protocols are compiled from published research rather than intuition:
  Kahneman on System 2 depletion, Popper on falsifiability, Deffenbacher and
  Loftus on eyewitness memory, Cohen on moral panic, Dror on forensic
  contextual bias — each mapped to a specific patch, rule, and output marker.
- A separate math layer of 44 operators is governed by ten laws, including one
  that forbids the system from trusting its own computation over a verified
  fact.

And three documented cases where the system caught defects in itself — the most
instructive being a live incident where the classifier flagged real past events
as fabricated future ones, because it had substituted its training cutoff for
the current date. That is a general problem, not only mine, and the fix and its
limits are written up honestly.

Dossier with source excerpts: [link]
The live site where all of it runs: web-production-b540f.up.railway.app

I am one retired person doing this alone, so I have no team to check my
reasoning. An outside read from people who work on these systems professionally
would be worth more to me than most things I could buy.

Dzianis Vashkevich
dendenden043@gmail.com · +48 571 296 605
Luboń, Poland

---

## 4 · Grant programs and investors — general

> **Subject:** AI verification infrastructure, built solo — 6,504 tests, full audit record

Hello,

I am writing about a piece of infrastructure I have built alone and would like
to keep alive.

The problem it addresses: most guardrails around AI output are themselves AI —
one model grading another's answer in prose, with no fixed arithmetic
underneath. That inherits the exact failure it is meant to catch. A
confident-sounding classifier can be as wrong, and as fabricated, as the thing
it grades.

My system starts from a narrower promise. The model may read and label only.
Every number, threshold, and verdict is computed by deterministic Python that
can be inspected line by line. If a number in the code cannot be traced to an
explicit line of written specification, it is treated as a bug — a rule the
project has enforced against itself, removing four plausible-looking confidence
thresholds that turned out to exist nowhere in the specification.

State as of 21 August 2026, measured rather than recalled:

| | |
|---|---|
| Python | 152,080 lines, 738 files |
| Specifications | 51,348 lines HELIX + 31,453 Mr. Helix |
| Tests | 6,504 passing, 0 failing (two runs: 4,360 + 2,144) |
| Engine files audited line by line | 70 of 70 |
| Discrepancies found and fixed | 14, each with tests |

I am a pensioner. I work on this from retirement, on my own equipment, having
lost fingers on one hand along the way and continued regardless. I did not start
it to build a business, and I do not have a plan for profiting from it
personally. What I want is for it to survive past the point where my own
resources run out.

It has been built on personal funds and two small cloud grants — $300 from
Google Cloud and $200 from Azure — both nearly spent.

**What would help:** compute or infrastructure credit, a place in a
research-credit or accessibility-focused grant program, or an introduction to
one. I am not seeking investment in a company; there is no company.

The full technical dossier — with excerpts from the running source, the
formulas, the scientific sources compiled into executable rules, and three
documented cases where the system caught its own defects — is here: [link]

The system is deployed and running: web-production-b540f.up.railway.app — not a
specification and not a prototype; you can log in and check it by hand.

Everything in it is checkable within an hour given repository access, which I
will grant to any serious reviewer.

Dzianis Vashkevich
dendenden043@gmail.com · +48 571 296 605
Luboń, Poland

---

## Before you send

- Replace `[link]` with the dossier URL.
- Re-run the numbers if the code has changed since the date in each letter, and
  update the date with them. A stale number in a letter about verification
  discipline costs more than it saves.
- Attach `HELIX_DOSSIER_EN.html` directly where a link may be stripped by a
  form or a filter — the file is self-contained and opens in any browser.
