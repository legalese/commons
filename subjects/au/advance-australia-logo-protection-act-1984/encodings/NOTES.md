# Advance Australia Logo Protection Act 1984 (Cth) — encoding notes (row `legalese-aswathy`)

DRAFT. No Australian lawyer has read this encoding against the Act.

## What is encoded

There is one top-level goal, `the logo position for` (`aal-rules.l4`). It answers:

- whether I infringe the monopoly in the design;
- the day the prescribed period ended (12 October 1999);
- whether I infringe the copyright in the logo;
- whether no action lies against me for use before 13 October 1983.

The encoded provisions are ss 3(1), 11(1), 15(2) and 19(2)-(3). The source is the compilation of 10 December 2015.

## Seat

The encoding is written from the seat of **the trader dealing with articles bearing the logo**. This follows the repo's `CLAUDE.md` rule of 2026-10-18.

**The top-level question, in their words:** "Did I infringe the monopoly in the logo's design; does it infringe the copyright; can I be sued for use before the Act?"

## Coverage

| Provision | Disposition |
|---|---|
| ss 1-2 | out of scope: machinery |
| s 3 | (1) prescribed period encoded; the other definitions are folded into the inputs |
| ss 4-5 | out of scope |
| ss 6-10 | out of scope: ownership by the Company and the Commonwealth |
| s 11 | (1) encoded; (2)-(6) (who may sue, licensees' consent) are out of scope |
| s 12 | out of scope: remedies |
| s 13 | out of scope: jurisdiction |
| s 14 | out of scope: validation of the Company's licences |
| s 15 | (2) encoded; (1), (3) are out of scope |
| s 16 | out of scope: compensation |
| ss 17-18 | out of scope: directions and reports |
| s 19 | (2)-(3) encoded; (1), (4) are out of scope |
| ss 20-21, Schedules | out of scope |

## Forks (readings taken)

- **F1, s 11(1)(c)-(d).** Unlike (a) and (b), they carry no "without the licence of the owner"; they are read as written, so a licence does not excuse importing or dealing in imported articles.
- **F2, s 3(1).** "The period of 16 years that commenced on 13 October 1983" ends on 12 October 1999.
- **F3, s 19.** From 13 October 1983 (during the period, and after it for acts the owner would have had the exclusive right to do), the dealing does not infringe the copyright. Before that day the Copyright Act alone answers: NOTHING.
- **Known limits (from the independent pass).**
  - s 19 is applied to every dealing; selling, importing and imitations may fall outside the owner's exclusive right in the design.
  - The design and an imitation are one input.
  - s 11(1)(b)'s "in infringement" is taken from the kind of dealing and not checked.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-20: 3 modules: 36 assertions satisfied, 0 failed, 0 other errors — 15 the encoder's (`aal-tests.l4`), 21 independent (`tests-independent.l4`). No assertion is expected to fail.

## Open questions for an Australian lawyer

- **F1:** does a licence from the owner excuse importing under s 11(1)(c)?
