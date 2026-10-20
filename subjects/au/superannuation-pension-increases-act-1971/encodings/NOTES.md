# Superannuation (Pension Increases) Act 1971 (Cth) — encoding notes (row `legalese-aswathy`)

DRAFT. No Australian lawyer has read this encoding against the Act.

## What is encoded

There is one top-level goal, `my 1971 pension increase for` (`spi71-rules.l4`). It answers by how much my annual pension increases. The encoded provisions are ss 4-9, with the s 3 definitions as inputs. The Act commenced on 1 October 1971.

## Seat

The encoding is written from the seat of **the eligible pensioner, or the widow or widower**. This follows the repo's `CLAUDE.md` rule of 2026-10-18.

**The top-level question, in their words:** "By how much does my annual pension increase under the 1971 Act?"

## Coverage

| Provision | Disposition |
|---|---|
| ss 1-2 | out of scope |
| s 3 | the unit entitlements, salaries and the relevant time are inputs, worked out under the Superannuation Act's scales and the Treasurer's determinations |
| s 4 | encoded |
| s 5 | encoded; which pensioners are within s 5(1) is an input |
| s 6 | encoded; the s 6(2) deduction is folded into the units input |
| s 7 | encoded |
| s 8 | (1) encoded; (2)-(4) (later spouse pensions) are out of scope |
| s 9 | encoded as an input |
| s 10 | out of scope: pensions for the persons named in the Schedule |
| ss 11-13 | out of scope: payment, corrections, date of effect |

## Forks (readings taken)

- **F1, the order of ss 4-7.** The s 4 increase is scaled under s 5 or s 6, then reduced by earlier increases under s 7, not below nil, following the readings for the 1967 and 1971 DFRB Acts.
- **F2, s 8.** The spouse's share is taken of the late spouse's increase after ss 5-7.
- **F3, ss 5-6.** A scaling denominator of nil leaves the increase unscaled; the source does not contemplate it.
- **Known limits (from the independent pass).**
  - The s 3 unit entitlements are inputs.
  - Whether a case is within s 5(1)(a)-(e), whether the s 8 election was revoked, and the s 9(a) State Fund carve-out are the caller's choice.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-20: 3 modules: 25 assertions satisfied, 0 failed, 0 other errors — 10 the encoder's (`spi71-tests.l4`), 15 independent (`tests-independent.l4`). No assertion is expected to fail.

## Open questions for an Australian lawyer

- None of substance.
