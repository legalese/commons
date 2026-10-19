# Nationality and Borders Act 2022 (UK) — encoding notes (row `legalese-aswathy`)

DRAFT. No UK lawyer has read this encoding against the Act.

## What is encoded

Much of this Act amends other Acts. Its own operative rules for a person sit in Part 2, and those are encoded. There is one top-level goal, `the asylum position for` (`nba-goal.l4`). For one asylum seeker it answers:

- the refugee determination, as ss 30-35 require it to be made, including which test failed;
- whether the s 37 conditions for Article 31(1) immunity are met;
- if a priority removal or evidence notice was served: whether material was provided late, the last day a priority removal notice is in force, whether lateness must damage credibility, and whether minimal weight applies.

Three goals sit under it:

1. **Refugee status** (`nba-refugee.l4`): ss 30(1), (5), 31(1)-(2), 32, 33(2)-(4), 34 and 35(1).
2. **Article 31(1) immunity** (`nba-article-31.l4`): s 37(1)-(4).
3. **Notices and late evidence** (`nba-notices.l4`): ss 20(4)-(7), 21(1), (3)-(4), 22(1)-(4), (7), and 26(1)-(5).

Each finding of fact is an input. The encoding applies the order and structure the Act requires.

Dates are computed as the Act words them. The UK has no general next-working-day rule.

## Seat

The encoding is written from the seat of **the asylum seeker**, the person the law is applied to (the repo's `CLAUDE.md` rule of 2026-10-18).

**The top-level question, in their words:** "Am I a refugee as the decision-maker must decide it; can I rely on immunity from penalties for how I entered; and if I gave evidence late, will it count against me, and until when does a priority removal notice apply to me?"

The facts it asks for are ones that person can state, or findings made about them.

The refugee test is the decision-maker's structure. For the asylum seeker, it tells them which finding their claim turns on.

The function names were written before the rule and have not been renamed.

## Coverage

| Provision | Disposition |
|---|---|
| Part 1 (ss 1-11) | out of scope: nationality |
| ss 12-17 | out of scope: differential treatment, accommodation, inadmissibility |
| s 18 | input: an evidence notice and its date, used by s 26 |
| s 19 | out of scope: credibility for an evidence notice under s 8 of the 2004 Act |
| s 20(3)-(7) | encoded (goal 3) |
| s 21(1), (3)-(4) | encoded (goal 3); (5)-(7) are out of scope |
| s 22(1)-(4), (7) | encoded (goal 3); (5)-(6) are procedure rules |
| ss 23-25, 27-29 | out of scope: appeals, legal aid, removal |
| s 26(1)-(5) | encoded (goal 3) |
| s 30(1), (5) | encoded (goal 1); (2)-(4) are out of scope |
| ss 31-35 | encoded (goal 1); s 31(3) and s 33(1) are inert examples, and s 33(5) is folded into the reason input |
| s 36 | out of scope: Article 1(F) |
| s 37(1)-(4) | encoded (goal 2); (5) amends another Act |
| s 38 | out of scope: it amends s 72 of the 2002 Act |
| ss 39-86 | out of scope: Parts 3-6 and the general provisions |

## Forks (readings taken)

- **F1, s 30(5).** A claim made on the in-force date is "on or after", so ss 31-35 apply.
- **F2, the order of the tests.** The determination checks, in order: the Convention reason; stage one, on the balance of probabilities; stage two, on a reasonable likelihood (persecution by an actor of persecution, s 31); protection (s 34); and internal relocation (s 35). It reports the first test that fails. Section 32(4)-(5) requires all of them; the order only affects which failure is reported.
- **F3, s 31(1)(c).** Harm by a non-State actor counts as persecution only if the State and controlling parties are unable or unwilling to protect.
- **F4, s 34(2).** Protection is available only if both limbs are met: an effective legal system, and access to it.
- **F5, s 37(2).** The "without delay" test depends on where the person became a refugee and, if in the United Kingdom, on whether their presence was then lawful.
- **F6, "on or after the PRN cut-off date".** Material provided on the cut-off date is late.
- **F7, s 21(1).** The notice stays in force until the end of the 12 months beginning with the later of the cut-off date and the day appeal rights were exhausted. That period ends on the day before the corresponding date, or on the last day of the month where that month has no corresponding date.
- **F8, s 22 and s 26.** Credibility damage (s 22) applies only to priority removal notices and needs a relevant decision. Minimal weight (s 26) applies to both kinds of notice and needs the evidence to fall to be considered in a determination (the relevant-decision input; changed after the independent pass). Both yield to good reasons for the lateness.
- **Known limits (from the independent pass).**
  - Under a priority removal notice, s 26(5)(a) covers only evidence supporting the reasons-and-grounds statement; there is no input for what the material was.
  - The findings for s 31(1)(c) and s 34 are separate inputs and can be set inconsistently.
  - Material given to a tribunal (ss 20(6), 22(2)) uses the same lateness input.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-18: 7 modules: 139 assertions satisfied, 0 failed, 0 other errors — 45 the encoder's (`nba-tests.l4`), 94 independent (`tests-independent.l4`). No assertion is expected to fail.

## Open questions for a UK lawyer

- **F2:** is reporting the first failed test, in this order, a fair reading of s 32's structure?
