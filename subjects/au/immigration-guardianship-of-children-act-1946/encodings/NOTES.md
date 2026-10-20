# Immigration (Guardianship of Children) Act 1946 (Cth) — encoding notes (row `legalese-aswathy`)

DRAFT. No Australian lawyer has read this encoding against the Act.

## What is encoded

There is one top-level goal, `the child position for` (`igc-rules.l4`). It answers:

- whether the child is a non-citizen child;
- whether the Minister is the child's guardian, and the latest day that guardianship lasts;
- whether the child may leave only with the Minister's written consent;
- whether I commit an offence under s 6A or s 9;
- the last day to ask for reconsideration, and for the Minister to reconsider.

The encoded provisions are ss 4AAA, 4AA (as an input), 6, 6A, 9, 11 (as an input) and 11A(2)-(4). The source is the compilation of 14 October 2024.

## Seat

The encoding is written from the seat of **the child who enters Australia to settle, and the adult who brings, cares for or deals with them**. This follows the repo's `CLAUDE.md` rule of 2026-10-18.

**The top-level question, in their words:** "Is this child a non-citizen child; is the Minister the guardian, until when; can the child leave Australia; is what I do an offence; by when must I seek reconsideration?"

## Coverage

| Provision | Disposition |
|---|---|
| ss 1-3 | out of scope |
| s 4 | applied: relative, parent and intending adoptive parent are folded into the companion input |
| s 4AAA | encoded |
| ss 4AAB-4AAC | out of scope: declarations and Norfolk Island |
| s 4AA | the direction is an input |
| s 4A | out of scope: evidence |
| s 5 | out of scope: delegation |
| s 6 | encoded |
| s 6A | encoded |
| s 7 | out of scope: custody placements |
| s 8 | out of scope |
| s 9 | encoded |
| s 10 | out of scope |
| s 11 | the exemption is an input |
| s 11A | (2)-(4) encoded; (1), (5)-(6) are out of scope |
| s 12 | out of scope |

## Forks (readings taken)

- **F1, s 4AAA.** An 18th birthday is the anniversary of birth (28 February for 29 February in a common year); the child is a non-citizen child only before it.
- **F2, s 6 (changed after the independent pass).** The guardianship ends on reaching 18, so the encoding gives the 18th birthday as the day it ends (the Minister is no longer guardian on that day); it ends earlier on a permanent departure or an exemption.
- **F3, ss 6A(3), 9.** Helping the child leave without consent is an offence without any lawful-excuse defence; removing, enticing, harbouring or concealing is an offence only without lawful excuse (which the accused must prove).
- **F4, s 11A(3)-(4).** "Within the period of 28 days after" the decision comes to notice ends on that day + 28; "within 45 days after receipt" ends on the receipt day + 45.
- **Known limits (from the independent pass).**
  - s 4AAA(3)(b) and (c) are one input.
  - An adult or relative under 21 can only be entered as "no one".
  - s 11A(3)(a)(ii) (a further period) and arrival after commencement (s 6(1)) are not modelled.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-20: 3 modules: 48 assertions satisfied, 0 failed, 0 other errors — 18 the encoder's (`igc-tests.l4`), 30 independent (`tests-independent.l4`). No assertion is expected to fail.

## Open questions for an Australian lawyer

- None of substance.
