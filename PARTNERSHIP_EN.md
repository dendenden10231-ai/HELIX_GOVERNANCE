# Taking part

This document exists because people asked how they could get involved and I had
no written answer. Now there is one.

The short version: **I am open to almost anything.** What interests me is not
control or revenue, but that the system keeps working and keeps developing —
including in the hands of people who will do it better than I can.

---

## 1. What this is, and its honest state

HELIX is a deterministic verification engine for AI output. The language model
is permitted to read and to label; computing and deciding are forbidden to it,
and that is enforced in code rather than stated in documentation. The details
and the evidence are in the [dossier](dossier/HELIX_DOSSIER_EN.html).

The state of it, plainly:

- **It runs.** This is not a specification or a prototype — it is a deployed
  site you can log into and exercise. Three products on one engine.
- **It is verified.** 3,946 tests; all 70 engine files read line by line
  against written specification; 14 discrepancies found and fixed.
- **It is one person.** No team, no investor, no manager. That is both the
  central weakness and the reason this document exists.
- **It does not sell.** There is no revenue and no business model, and I never
  built one. Not on principle — the time went into making the system correct.

---

## 2. Ways to take part

Listed by how easy they are to start, not by how much I want them. **Any of
these is open to discussion, and nobody needs to take on all of it.**

**Technical review.** Twenty minutes of your reading of the architecture and an
honest "this part is wrong." It costs nothing and it is the scarcest thing I
have: there is no one to check my reasoning.

**Compute and infrastructure.** Credits, hosting, API access. The current
bottleneck is exactly this — live grounded model calls inside real
investigations cost money a pensioner does not have.

**Funding.** A grant, a contract, commissioned work — any shape. I hold a
registered business in Poland (a sole proprietorship under my own name), so I
can invoice and sign contracts lawfully and immediately.

**Development.** Take a direction and run it. There are three products, and one
of them (MARKET) is deliberately unstarted because its specification has not
settled — a self-contained piece of work for anyone who wants it.

**Deployment and product.** I have no commercial experience and no wish to
acquire any. If you can see how this applies in practice and want to do that
part, I will help rather than get in the way.

**Partnership.** Running the project jointly, splitting directions, equity in a
future company. Everything is negotiable except one item in section 4.

**Continuity after me.** See section 6. That matters to me more than anything
else on this list.

---

## 3. What I bring

- **Full access.** Code, specifications, the record of decisions, the entire
  audit trail. The repository is private as a precaution around unfinished
  work, not against people. To a serious counterpart I open it without
  conditions.
- **Explanation.** Fifty-one thousand lines of specification is a lot, and
  nobody should have to face it alone. I will walk anyone through the system as
  many times as it takes.
- **Flexibility on terms.** Equity, licence, form of involvement, division of
  directions — I will not bargain hard. The project has been alone too long for
  me to dig in over percentages.
- **Speed.** I have nobody to consult. A decision on anything comes the same
  day.

---

## 4. The one thing that is not negotiable

**The verification discipline.** Rule P0-6: no number without a traceable
formula. The model does not assign scores. An empty result is never presented
as "checked, clean."

This is not stubbornness or taste. It is the only thing separating this system
from any other wrapper around an LLM, and the entire reason it was built. A
version that lets the model set its own confidence score for the sake of speed
stops being this product and becomes the thing it was made to catch.

**Authorship.** I remain the author of the system and take part in decisions
about its direction. This is not operational control and not a veto over
anyone's work — it is that my name stays attached to what I have spent these
years doing, and that I do not learn about a change of course after the fact.

Everything else is on the table.

---

## 5. The legal position, without promises

**What exists now:** a registered sole proprietorship in Poland
(*jednoosobowa działalność gospodarcza*) under the name Dzianis Vashkevich.
That is enough to:

- receive a grant or subsidy as the beneficiary;
- issue invoices and sign contracts, licensing agreements included;
- work jointly under a cooperation agreement.

**What it does not allow:** a sole proprietorship issues no shares — you cannot
become a shareholder in one. If a conversation reaches the point of taking
equity, converting to a *sp. z o.o.* is required. That is a standard, well-
documented procedure under Polish law and I am willing to go through it when
there is a reason. I will not do it pre-emptively: it means cost and reporting
in exchange for a hypothesis.

**The code licence** is currently undeclared, since the repository is private.
That is an unfinished decision rather than a position. I am open to any sensible
scheme: a closed commercial licence, an open core with a commercial layer, a
delayed-open licence. If your interest depends on a particular model, say which
— that may be the reason to settle it.

I am not a lawyer and none of this is legal advice. On any serious step I intend
to work with an accountant and a lawyer rather than rely on my own reading.

---

## 6. What happens if I stop

This is the most important part of the document, and I will write it plainly.

I am past sixty, I work alone, and some of the work is physically harder for me
than it used to be. As things stand, if I stop, all of this disappears with a
private repository — three years of work would simply cease to exist. That
worries me considerably more than money or equity does.

So: **continuity matters to me more than the terms of any deal.** If a
conversation reaches an agreement, I want it to record what happens to the code
and the specifications if I cannot continue. Source escrow, a named successor,
a licence that opens on a condition — the mechanism is negotiable; having one is
not.

The reverse holds too. If a person or a team appears who can carry this further
than I can, I will not clutch at it out of pride. A system that runs without me
is the success, not the defeat.

---

## 7. Starting a conversation

Write. No deck and no formal proposal is needed — a paragraph about what caught
your interest and what you are thinking of doing is enough.

**Dzianis Vashkevich**
dendenden043@gmail.com · +48 571 296 605
Luboń, Poland

I answer everything personally, usually the same day.

If you would rather look first: the [dossier](dossier/HELIX_DOSSIER_EN.html)
carries excerpts from the running source, the formulas, and three documented
cases where the system found defects inside itself. The live site is open — the
address is in the dossier. Full repository access is available on request,
without conditions.
