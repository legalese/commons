# Adelaide Airport Curfew Act 2000 (Cth) — encoding notes (row `legalese-aswathy`)

DRAFT. No Australian lawyer has read this encoding against the Act.

## What is encoded

There is one top-level goal, `the curfew position for` (`aac-rules.l4`). It answers:

- whether the movement is in the curfew period;
- whether it is permitted;
- whether I commit an offence under s 6, and the maximum penalty units;
- the last day to give the return after a weather landing off runway 05.

The encoded provisions are ss 3, 6, 9, 11-14, 15(3) and 16-18. The source is the compilation of 14 October 2024.

## Seat

The encoding is written from the seat of **the operator of an aircraft**. This follows the repo's `CLAUDE.md` rule of 2026-10-18.

**The top-level question, in their words:** "Is this movement in the curfew; is it allowed; is it an offence; if I landed off runway 05, by when must I lodge a return?"

## Coverage

| Provision | Disposition |
|---|---|
| ss 1-2, 4-5A | out of scope; time is South Australian legal time |
| s 3 | curfew period and shoulder period encoded; aircraft classes are inputs |
| s 6 | encoded |
| ss 7-8, 10 | out of scope: quotas |
| s 9 | a shoulder-period permission is an input, effective only in the shoulder hours |
| s 11 | a curfew permission for low noise heavy freight is an input |
| ss 12-13 | encoded as aircraft kinds |
| s 14 | encoded |
| s 15 | (3) encoded; (1)-(2), (4) are out of scope |
| ss 16-18 | encoded as circumstances |
| ss 19 onwards | out of scope |

## Forks (readings taken)

- **F1, s 3.** The curfew runs from 11:00 pm to before 6:00 am; the shoulder hours are 11:00 pm to midnight and 5:00 am to before 6:00 am.
- **F2, s 9.** An international aircraft's permission covers only the shoulder hours.
- **F3, s 14.** Taxi clearance before the curfew permits only a take-off.
- **F6, s 16(b) (changed after the independent pass).** Resuming a flight interrupted by an emergency permits only a take-off.
- **F4, s 15(3).** "Within 7 days after the landing": the last day is the landing day + 7.
- **F5, s 6.** The penalty is 200 penalty units; for a body corporate the Crimes Act multiplier is not computed.
- **Known limits (from the independent pass).**
  - The return deadline is given for any weather landing date, whether or not s 15(1)-(2) applies.
  - Runway and reverse-thrust permission conditions are not modelled.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-20: 3 modules: 40 assertions satisfied, 0 failed, 0 other errors — 15 the encoder's (`aac-tests.l4`), 25 independent (`tests-independent.l4`). No assertion is expected to fail.

## Open questions for an Australian lawyer

- None of substance.
