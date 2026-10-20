# Defence (Parliamentary Candidates) Act 1969 (Cth) — encoding notes (row `legalese-aswathy`)

DRAFT. No Australian lawyer has read this encoding against the Act.

## What is encoded

There is one top-level goal, `the candidate position for` (`dpc-rules.l4`). It answers:

- my route out;
- the last day to apply for reinstatement, and whether my application is in time;
- the last day the Chief may serve notice requiring me to apply;
- the day I am deemed to have applied, and whether I am deemed re-enlisted;
- whether the time away counts for long service leave;
- the amount I must repay.

The encoded provisions are ss 6-14 and 17. The source is the compilation of 1 July 2016.

## Seat

The encoding is written from the seat of **the member of the Defence Force who wants to stand for election**. This follows the repo's `CLAUDE.md` rule of 2026-10-18.

**The top-level question, in their words:** "How do I leave to stand; by when must I apply to come back; what if I do not; must I repay my gratuity?"

## Coverage

| Provision | Disposition |
|---|---|
| ss 1-5 | out of scope: machinery and definitions |
| s 6 | the declared date is an input |
| ss 7-9 | encoded: the Chief's satisfaction is an input, and the power is discretionary |
| s 10 | (1) encoded; (2)-(4) applied: the time away counts for long service leave |
| s 11 | (1) encoded; (2)-(5) applied |
| s 12 | (1) encoded; (2)-(3) applied |
| s 13 | encoded |
| s 14 | encoded |
| s 16 | out of scope: travel and removals |
| s 17 | encoded |
| ss 18-22 | out of scope |

## Forks (readings taken)

- **F1, ss 10-12.** "Not later than two months after the date that is the declared date": the last day is the corresponding day two months later, or the month's last day where there is none.
- **F2, ss 13(1), 14(1).** "Before the expiration of a period of one month after" the declared date: the notice may be served up to the corresponding day one month later.
- **F3, ss 13(2), 14(2).** Without an application by the end of the two months, the member is deemed to apply on that day; an enlisted member is also deemed re-enlisted. An officer's deemed application leaves reinstatement to the Chief under s 10.
- **F4, s 17.** The gratuity is repaid whenever reinstatement under ss 10-12 takes effect, including a deemed re-enlistment.
- **F5, ss 13-14.** They do not reach a Reserve member whose continuous full-time service ended under s 9, nor a successful candidate.
- **Known limits (from the independent pass).**
  - The exclusion of the time away from an appointment or engagement (ss 10(3), 11(3)) is not an output.
  - The s 17(3) carve-out for DFRB Act gratuities is not modelled.
  - Inconsistent inputs (another member who has left under the Act) are accepted.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-20: 3 modules: 56 assertions satisfied, 0 failed, 0 other errors — 18 the encoder's (`dpc-tests.l4`), 38 independent (`tests-independent.l4`). No assertion is expected to fail.

## Open questions for an Australian lawyer

- None of substance.
