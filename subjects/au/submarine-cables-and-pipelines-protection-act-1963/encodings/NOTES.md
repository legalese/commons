# Submarine Cables and Pipelines Protection Act 1963 (Cth) — encoding notes (row `legalese-aswathy`)

DRAFT. No Australian lawyer has read this encoding against the Act.

## What is encoded

There is one top-level goal, `the cable position for` (`scp-rules.l4`). It answers:

- whether I commit an offence;
- the maximum imprisonment and penalty units;
- whether I must bear the cost of repair;
- whether I am entitled to be indemnified by the owner of the cable or pipeline.

The encoded provisions are ss 5, 7, 8, 9 and 10(2). The source is the compilation of 21 October 2016.

## Seat

The encoding is written from the seat of **the person whose conduct on an Australian-registered ship damages a submarine cable or pipeline**, or the owner who laid a cable or sacrificed gear. This follows the repo's `CLAUDE.md` rule of 2026-10-18.

**The top-level question, in their words:** "Have I committed an offence, and what is the most I can get; must I pay for the repair; am I indemnified for the gear I sacrificed?"

## Coverage

| Provision | Disposition |
|---|---|
| ss 1-4 | out of scope: machinery and saving of other laws |
| s 5 | encoded |
| s 5A | out of scope: the Criminal Code's fault rules (negligence is an input) |
| s 6 | out of scope: the Crown is bound |
| s 7 | encoded |
| s 8 | encoded |
| s 9 | encoded |
| s 10 | (2) encoded; (1) (no double punishment) is out of scope |
| s 11 | out of scope: jurisdiction |

## Forks (readings taken)

- **F1, s 7(2) (changed after the independent pass).** It disapplies "the last preceding subsection", which since (1A) was inserted is (1A) alone. The encoding follows the words: the life-saving exception answers the negligence offence, not s 7(1). Before (1A) was inserted the exception reached the single offence, so Parliament may have meant both.
- **F2, s 7(1), (1A).** Where conduct resulted in the damage, (1) and its higher penalty apply; negligence alone gives (1A).
- **F3, s 10(2).** In summary proceedings the most is 3 months or 10 penalty units, whichever offence.
- **F4, ss 8-9.** They apply only where the Act applies (s 5).
- **Known limits (from the independent pass).**
  - The protection-zone limit is not tested for ss 8-9.
  - The Criminal Code's fault elements are out of scope.
  - No input separates the persons acting in s 7(2) from the accused.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-20: 3 modules: 47 assertions satisfied, 0 failed, 0 other errors — 19 the encoder's (`scp-tests.l4`), 28 independent (`tests-independent.l4`). No assertion is expected to fail.

## Open questions for an Australian lawyer

- **F1:** does s 7(2) still reach s 7(1) after the insertion of s 7(1A)?
