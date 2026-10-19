# Superannuation (Distribution of Surplus) Act 1974 (Cth) — encoding notes (row `legalese-aswathy`)

DRAFT. No Australian lawyer has read this encoding against the Act.

## What is encoded

There is one goal, `who is paid the share of` (`sds-rules.l4`). It answers whether a Fund member is an eligible contributor or eligible pensioner and who receives their share of the 1972 surplus. The source is the Act as made (assent 11 April 1974).

## Seat

The encoding is written from the seat of **the contributor or pensioner** of the Superannuation Fund, or their widow. This follows the repo's `CLAUDE.md` rule of 2026-10-18.

**The top-level question, in their words:** "Am I entitled to a share of the 1972 surplus; and if the person entitled has died, who is paid?"

## Coverage

| Provision | Disposition |
|---|---|
| ss 1-2 | applied: commencement on 11 April 1974 |
| s 3 | encoded: "eligible contributor" and "eligible pensioner" |
| s 4 | inert: the amounts available |
| s 5 | out of scope: the Treasurer's allocation of each share is not computable |
| s 6 | encoded |
| s 7 | out of scope: assignment and attachment |

## Forks (readings taken)

- **F1, s 3(1)(b)-(c), "after the commencement of the relevant period but before the date referred to in paragraph (a)" (changed after the independent pass).** That is from 1 July 1962, the period's first day, to before 11 April 1974.
- **Known limits (from the independent pass).** The s 4 amounts are not encoded. The obligation date, the s 119W test and "pension payable during the period" are inputs. Contradictory inputs are not rejected.
- **F2.** The amount of each share is not computable from the Act. The encoding answers entitlement and the payee only.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-19: 3 modules: 31 assertions satisfied, 0 failed, 0 other errors — 10 the encoder's (`sds-tests.l4`), 21 independent (`tests-independent.l4`). No assertion is expected to fail.

## Open questions for an Australian lawyer

- **F1:** whether an event on 1 July 1962 falls "after the commencement" of the period.
