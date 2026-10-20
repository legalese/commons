# Public and Educational Lending Rights (Better Income for Authors) Act 2026 (Cth) — encoding notes (row `legalese-aswathy`)

DRAFT. No Australian lawyer has read this encoding against the Act.

## What is encoded

There is one top-level goal, `the lending position for` (`plr-rules.l4`). It answers:

- whether I am an Australian creator, and whether I am an Australian publisher;
- the last day to request reconsideration;
- the last day for the Secretary's reconsideration, and whether the decision is taken to be affirmed;
- whether I may apply to the Administrative Review Tribunal;
- the earliest last day an overpayment notice may set.

The encoded provisions are ss 5, 33, 34(1) and 38(2)(c). The source is the Act as made (assent 20 May 2026).

## Seat

The encoding is written from the seat of **the author, illustrator, translator or publisher of a book**. This follows the repo's `CLAUDE.md` rule of 2026-10-18.

**The top-level question, in their words:** "Am I someone the Scheme pays; by when must I seek reconsideration, and when is the Secretary taken to have affirmed; how long must an overpayment notice give me?"

## Coverage

| Provision | Disposition |
|---|---|
| ss 1-4, 6 | out of scope: machinery and outlines |
| s 5 | Australian creator, Australian person and Australian publisher encoded; the other definitions are out of scope |
| ss 7-8 | out of scope: the Scheme is a legislative instrument (eligibility, amounts and claims are there) |
| ss 9-31 | out of scope: the Committee |
| s 32 | inert: outline |
| s 33 | encoded; (3)-(4), (6)-(7) are procedure |
| s 34 | (1) encoded; (2) is out of scope |
| ss 35-37 | out of scope: recovery after conviction or false information |
| s 38 | (2)(c) encoded; the rest is out of scope |
| ss 39-45 | out of scope (s 40 inalienability and s 41 payment to the legal personal representative are noted) |

## Forks (readings taken)

- **F1, s 5 Australian publisher (c).** A creator who publishes the book counts only if they are an Australian creator of it.
- **F2, s 33(2), (5).** "Before the end of the period of 28 (90) days beginning on" a day: the last day is that day + 27 (+ 89).
- **F3, s 33(8).** Notification of the decision on reconsideration after the 90 days means the decision is taken to have been affirmed.
- **F6, s 33(4).** Only a request made in time (s 33(2)) obliges the Secretary to reconsider. The encoding takes the day the Secretary received the request, not the day it was made, so it does not check timeliness: every received request starts the 90 days.
  - **Disagreement from the independent pass, left open.** The tester reads a request received after the 28 days as late, giving no deemed affirmation and no Tribunal review. A request posted in time may be received later, so receipt alone cannot settle it; those assertions (`tests-independent.l4` lines 75 and 78) are left failing.
- **F4, s 34(1).** A decision by the Secretary personally goes straight to the Tribunal; a delegate's decision goes first to reconsideration.
- **F5, s 38(2)(c).** "At least 28 days starting on the day on which the notice is given": the period cannot end before the notice day + 27.
- **Known limits (from the independent pass).**
  - The s 33(3) written reasons are not inputs.
  - The longer period the Secretary allows is entered as an end date and not checked.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-20: 3 modules: 44 assertions satisfied, 2 failed, 0 other errors — 17 the encoder's (`plr-tests.l4`), 29 independent (`tests-independent.l4`). Two assertions in `tests-independent.l4` (lines 75 and 78) are expected to fail: they treat a request received after the 28 days as late (F6).

## Open questions for an Australian lawyer

- **F3:** if the Secretary decides in time but notifies late, is the decision still taken to be affirmed?
