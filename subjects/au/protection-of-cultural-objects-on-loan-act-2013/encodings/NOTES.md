# Protection of Cultural Objects on Loan Act 2013 (Cth) — encoding notes (row `legalese-aswathy`)

DRAFT. No Australian lawyer has read this encoding against the Act.

## What is encoded

There is one top-level goal, `the loan position for` (`pcol-rules.l4`). It answers:

- whether Part 2 applies to my object;
- the day protection ends, and whether it is protected on the day asked about;
- whether the proceeding is barred;
- whether it can be seized, or forfeited.

The encoded provisions are ss 5 (lender), 8, 9(1)-(2), (4), 10(1), (4), 11 and 12. The source is the compilation of 14 October 2024.

## Seat

The encoding is written from the seat of **the foreign lender of an object on loan for exhibition**. This follows the repo's `CLAUDE.md` rule of 2026-10-18.

**The top-level question, in their words:** "Is my object protected while on loan in Australia, and until when; can I be sued over it; can it be seized or forfeited?"

## Coverage

| Provision | Disposition |
|---|---|
| ss 1-4 | out of scope |
| s 5 | lender (a) encoded; the rest of the definitions are folded into the inputs |
| ss 6-7 | out of scope |
| s 8 | encoded |
| s 9 | (1)-(2), (4) encoded; (3) (proceedings between protected persons) and (5) are out of scope |
| s 10 | (1), (4) encoded; (2)-(3) are out of scope |
| s 11 | encoded |
| s 12 | encoded |
| ss 13-21 | out of scope |

## Forks (readings taken)

- **F1, s 8(2)(a)(i).** "The end of 24 months starting on the day the object is imported": the day before the corresponding day 24 months later, or the month's last day where there is none.
- **F2, s 8(2).** Protection ends on export if that comes first; a ministerial declaration can only move the end later (at least 24 months).
- **F5, s 8(2)(a)(ii), (b).** Part 2 ceases "when" the object is exported, or at the declared time, part-way through that day; counting in whole days, the encoding treats the export or declared day as the last protected day.
- **F3, ss 9-10.** A claim against the lender, or against the object, is barred while Part 2 applies; Proceeds of Crime and prescribed proceedings are not.
- **F4, ss 11-12.** A police-only power may seize but not forfeit; Crimes Act Part IAA, the Proceeds of Crime Act and prescribed laws may do both.
- **Known limits (from the independent pass).**
  - Starting proceedings (s 9) and enforcing a judgment (s 10) are one input.
  - s 8(5) movements and the Proceeds of Crime Act's split by Part are not modelled.
  - The s 8(1) output ignores the day asked; the day-sensitive answer is the protection output.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-20: 3 modules: 55 assertions satisfied, 0 failed, 0 other errors — 18 the encoder's (`pcol-tests.l4`), 37 independent (`tests-independent.l4`). No assertion is expected to fail.

## Open questions for an Australian lawyer

- **F2:** is the object still protected on the day of its export?
