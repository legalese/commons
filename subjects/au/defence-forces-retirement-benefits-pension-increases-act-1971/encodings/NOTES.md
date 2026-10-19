# Defence Forces Retirement Benefits (Pension Increases) Act 1971 (Cth) — encoding notes (row `legalese-aswathy`)

DRAFT. No Australian lawyer has read this encoding against the Act.

## What is encoded

There is one goal, `my 1971 increase for` (`dfrb71-rules.l4`). It gives the increase in an eligible DFRB pensioner's or widow's pension. The encoded provisions are ss 5, 8, 10 and 12, with ss 11 and 13 recognised as determinations. The source is the Act as made (No. 74 of 1971).

## Seat

The encoding is written from the seat of **the eligible DFRB pensioner, or the widow**. This follows the repo's `CLAUDE.md` rule of 2026-10-18.

**The top-level question, in their words:** "By how much does my pension increase under the 1971 Act?"

## Coverage

| Provision | Disposition |
|---|---|
| ss 1-2 | out of scope |
| s 3 | the entitlements and rates are inputs, worked out under the DFRB Act's scales |
| s 4 | out of scope: s 73 pensions (rates from the DFRB Act) |
| s 5 | encoded |
| s 6 | out of scope: it depends on the Superannuation (Pension Increases) Act 1971 |
| s 7 | out of scope: the formula is an image missing from the text |
| s 8 | encoded |
| s 9 | out of scope: later commutation |
| s 10 | encoded |
| s 11 | recognised: the Minister for Finance determines the rate (NOTHING) |
| s 12 | encoded |
| s 13 | recognised: a determined rate (NOTHING) |
| the rest of the Act | out of scope |

## Forks (readings taken)

- **F1, the order of ss 5, 8 and 10 (changed after the independent pass).** The s 5 increase is scaled for commutation (s 8), then reduced by earlier increases (s 10). Section 10 reduces "any increase ... under the preceding provisions", which include s 8.
- **F2, s 12(1).** The widow's share is taken of her husband's increase after s 10, disregarding s 8 for his commutation.
- **F3, ss 11, 13.** The rate is a ministerial determination, so the answer is NOTHING.

- **Known limits (from the independent pass).** Section 12 sets aside s 8 only for the husband's commutation under s 74; an election under ss 61A-61B is not distinguished. The date of effect is not modelled.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-19: 3 modules: 26 assertions satisfied, 0 failed, 0 other errors — 10 the encoder's (`dfrb71-tests.l4`), 16 independent (`tests-independent.l4`). No assertion is expected to fail.

## Open questions for an Australian lawyer

- **F1:** confirm the order of s 8 and s 10, and that s 10 stops at nil.
