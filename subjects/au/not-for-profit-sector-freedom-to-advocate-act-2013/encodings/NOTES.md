# Not-for-profit Sector Freedom to Advocate Act 2013 (Cth) — encoding notes (row `legalese-aswathy`)

DRAFT. No Australian lawyer has read this encoding against the Act.

## What is encoded

There is one goal, `the clause position for` (`nfp-rules.l4`). For a clause in an agreement between a Commonwealth agency and a not-for-profit entity, it answers:

- whether the clause is prohibited content;
- from when it is void;
- whether the agency breached s 4(1);
- whether rights that accrued earlier survive.

The operative ss 3-5 and 7 are encoded. The source is the Act as made (No. 56, 2013).

## Seat

The encoding is written from the seat of **the not-for-profit entity** that signed the agreement, and its staff. This follows the repo's `CLAUDE.md` rule of 2026-10-18.

**The top-level question, in their words:** "Is this clause in our agreement with the Commonwealth prohibited content; is it void, and from when; did the agency break the Act by including it; and does voiding it disturb what accrued before 14 June 2013?"

## Coverage

| Provision | Disposition |
|---|---|
| ss 1-2 | applied: commencement on 14 June 2013, the day after assent |
| s 3 | the definitions are folded into the inputs |
| s 4 | encoded |
| s 5 | encoded |
| s 6 | out of scope: compensation for acquisition of property |
| s 7 | encoded |

## Forks (readings taken)

- **F1, s 5(2), "to the extent that".** A clause that only stops disclosure of confidential or personal information is not prohibited. A clause that goes further is prohibited, and is treated as void as a whole; the Act would void it only "to the extent" of the prohibited part.
- **F2, s 7(4).** An agreement made before 14 June 2013 has its prohibited content voided on that day, and what accrued under it before then survives. For a later agreement, the content is void from the start.

- **Known limits (from the independent pass).** The listed agency and acting for the Commonwealth, the two kinds of not-for-profit, and commenting, advocating and opposing (entity or staff) are each one input.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-19: 3 modules: 45 assertions satisfied, 0 failed, 0 other errors — 13 the encoder's (`nfp-tests.l4`), 32 independent (`tests-independent.l4`). No assertion is expected to fail.

## Open questions for an Australian lawyer

- **F1:** whether a mixed clause survives in part.
