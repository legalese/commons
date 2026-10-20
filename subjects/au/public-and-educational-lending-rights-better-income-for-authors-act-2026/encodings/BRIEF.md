# Encoding brief: the Public and Educational Lending Rights (Better Income for Authors) Act 2026 (Cth), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Public and Educational Lending Rights (Better Income for Authors) Act 2026** (No. 45, 2026), Commonwealth of Australia, as made (assent 20 May 2026), from the Federal Register of Legislation, deposited at `../registers/source-bundle/C2026A00045.txt` (CC BY 4.0). Sections 3 to 45 commence on a day fixed by Proclamation, or at the latest on the day after the 18 months beginning on assent. The Scheme itself is a legislative instrument, not deposited.

## Seat

The encoding is written from the seat of **the author, illustrator, translator or publisher of a book** (the repo's `CLAUDE.md` rule of 2026-10-18).

## Scope

Top level, in that person's words: *"Am I an Australian creator or publisher whom the Scheme pays? If a delegate decides against me, by when must I ask the Secretary to reconsider? By when must the Secretary decide, and is the decision taken to be affirmed if not? Can I go to the Administrative Review Tribunal? How long must an overpayment notice give me to pay?"*

In scope: s 5 (Australian creator, Australian person, Australian publisher), ss 33, 34(1), 38(2)(c). Out of scope: ss 1-4, 6-32 (the Scheme and the Committee), s 34(2), ss 35-37, 38(1), (3)-(4), 39-45.

## Inputs

- Whether I am an individual and an Australian citizen, a permanent resident or neither; my contribution to the book (author; illustrator or translator; contributor of a significant proportion of original content; none).
- As publisher: a company incorporated in Australia publishing in Australia; a registered charity publishing in Australia meeting any rules; an Australian creator also publishing the book in Australia; another person or body meeting the rules; not a publisher.
- Who made the reviewable decision (a delegate, or the Secretary personally); the day I was notified; any longer period the Secretary allowed; the day the Secretary received my request; the day the Secretary notified the reconsideration.
- The day an overpayment notice was given.

## Rules that matter

- Calculate the dates as the Act gives them.
- Encode isomorphically, with an `@ref` on every rule; `@export default` on the top-level goal.
- A failing assertion is a finding. Never edit an expected value to match the code.

## Deliverables

`plr-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
