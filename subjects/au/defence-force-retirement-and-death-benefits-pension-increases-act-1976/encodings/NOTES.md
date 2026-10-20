# Defence Force Retirement and Death Benefits (Pension Increases) Act 1976 (Cth) — encoding notes (row `legalese-aswathy`)

DRAFT. No Australian lawyer has read this encoding against the Act.

## What is encoded

There is one top-level goal, `my 1976 Act increase for` (`dfrdb76-rules.l4`). It answers by how much my annual DFRB pension (Part II, for 1973-74, 1974-75 or 1975-76) or DFRDB pension benefit (Part III, for 1975-76) increases. The encoded provisions are ss 5(4), 6, 7, 10, 11 and 18-21. Part II is deemed to have commenced on 1 July 1973, Part III on 1 July 1975.

## Seat

The encoding is written from the seat of **the pensioner, or the widow or child**. This follows the repo's `CLAUDE.md` rule of 2026-10-18.

**The top-level question, in their words:** "By how much did my annual pension increase under the 1976 Act?"

## Coverage

| Provision | Disposition |
|---|---|
| ss 1-4 | out of scope |
| s 5 | (4) encoded; (1)-(3) (definitions and substituted index numbers) are folded into the inputs |
| s 6 | encoded |
| s 7 | encoded; the "highest" earlier March figures are inputs |
| s 8 | the non-contributory portion is an input |
| s 9 | out of scope: suspended pensions |
| s 10 | encoded; (6) (re-engaged pensioners) is folded into the start day |
| s 11 | encoded |
| ss 12-16 | out of scope: modifications, reclassification, commutation, dates of effect, substitution |
| ss 17-18 | (2), (4) encoded |
| s 19 | encoded |
| s 20 | encoded |
| s 21 | encoded; who falls within (1) is the period input |
| ss 22-25 | out of scope |

## Forks (readings taken)

- **F1, ss 5(4), 18(4).** A fraction of a tenth of 1% under one-half is disregarded, otherwise treated as a tenth: rounding half up to one decimal place.
- **F2, ss 10(2), 11(2), 21(3).** A retirement or death period begins on the next day; a period from a pension becoming payable begins on that day. Both end on 30 June (1973 for s 10; the 30 June before the prescribed year for s 11; 1975 for s 21).
- **F3, ss 10(5), 11(5), 21(6).** The part month is measured against the month that begins on the corresponding day; at least half its days counts as a whole month.
- **F4, ss 10(3), 11(3), 21(1) (changed after the independent pass).** A pension that became payable after 15 June before the period's end gets no increase: in Part II only an s 82ZB pension (ss 10(3), 11(3)); in Part III any scaled benefit (s 21(1)). A Part II retirement after 15 June 1973 counts as 1 month (s 10(4)).
- **F5, s 6(1), 7(1).** Both the CPI and earnings must have risen; Part III needs only the CPI.
- **Known limits (from the independent pass).**
  - Whether s 10, s 11 or s 21 applies, and the start day, are the caller's choice; a wrong choice can give more than the full increase.
  - s 7's highest earlier March figures and the s 8 non-contributory portion are inputs.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-20: 3 modules: 45 assertions satisfied, 0 failed, 0 other errors — 13 the encoder's (`dfrdb76-tests.l4`), 32 independent (`tests-independent.l4`). No assertion is expected to fail.

## Open questions for an Australian lawyer

- None of substance beyond F4.
