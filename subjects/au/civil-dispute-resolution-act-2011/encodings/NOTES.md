# Civil Dispute Resolution Act 2011 (Cth) — encoding notes (row `legalese-aswathy`)

DRAFT. No Australian lawyer has read this encoding against the Act.

## What is encoded

There is one top-level goal, `the dispute position for` (`cdr-rules.l4`). It answers:

- whether I must file a genuine steps statement;
- the last day to file it;
- whether it may leave out the excluded parts;
- that not filing does not invalidate the proceedings;
- whether the court may weigh my statement and steps, including on costs.

The encoded provisions are ss 5, 6(1), (3)-(4), 7(1), 10(2), 11, 12(1) and 15-17. The source is the compilation of 14 October 2024.

## Seat

The encoding is written from the seat of **a party to civil proceedings**. This follows the repo's `CLAUDE.md` rule of 2026-10-18.

**The top-level question, in their words:** "Must I file a genuine steps statement, by when, and what if I do not?"

## Coverage

| Provision | Disposition |
|---|---|
| ss 1-3 | out of scope: machinery and object |
| s 4 | out of scope: whether steps were genuine is for the court |
| s 5 | eligible court encoded; the other definitions are folded into the inputs |
| s 6 | (1), (3)-(4) encoded; (2) (content) is out of scope |
| s 7 | (1) encoded; (2) (content) is out of scope |
| s 8 | out of scope: Rules of Court |
| s 9 | out of scope: the lawyer's duty |
| s 10 | (2) encoded; (1) is out of scope |
| s 11 | encoded |
| s 12 | (1) encoded; (2)-(3) (lawyers) are out of scope |
| s 13 | out of scope |
| ss 15-17 | encoded as kinds of proceedings; the regulations' prescriptions are one kind |
| ss 17A-19 | out of scope |

## Forks (readings taken)

- **F1, s 6(1).** The applicant's statement is due "at the time of filing the application": the last day is the filing day.
- **F2, s 7(1).** "Before the hearing date" means the day before it at latest. A respondent who is not given a copy of the applicant's statement need not file.
- **F3, ss 6(3)-(4), 15-17.** Proceedings of an excluded kind in whole need no statement; in part, the statement is required but may leave out the excluded parts.
- **F5, s 7(1) (changed after the independent pass).** A respondent given a copy of the applicant's statement must file, even where the proceedings are wholly excluded: the s 6(3) exclusion speaks only of s 6(1). Section 6(4) lets only the applicant leave out excluded parts.
- **F6, s 2 (changed after the independent pass).** Part 2 commenced on 1 August 2011; an application filed before then needs no statement.
- **F4, ss 11-12.** Whether a statement was filed and genuine steps taken may be weighed only for a person required to file.
- **Known limits (from the independent pass).**
  - "Not filing invalidates the proceedings" is always FALSE (s 10(2)).
  - A case carries only one kind of excluded proceedings.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-20: 3 modules: 40 assertions satisfied, 0 failed, 0 other errors — 15 the encoder's (`cdr-tests.l4`), 25 independent (`tests-independent.l4`). No assertion is expected to fail.

## Open questions for an Australian lawyer

- None of substance.
