# Defence Forces Retirement Benefits (Pension Increases) Act 1967 (Cth) — encoding notes (row `legalese-aswathy`)

DRAFT. No Australian lawyer has read this encoding against the Act.

## What is encoded

There is one top-level goal, `my 1967 increase for` (`dfrb67-rules.l4`). It answers by how much my DFRB pension increases. The encoded provisions are ss 3 (eligible pensioner), 4-10 and 13. The Act commenced on 8 November 1967.

## Seat

The encoding is written from the seat of **the eligible DFRB pensioner, or the widow**. This follows the repo's `CLAUDE.md` rule of 2026-10-18.

**The top-level question, in their words:** "By how much does my pension increase under the 1967 Act?"

## Coverage

| Provision | Disposition |
|---|---|
| ss 1-2 | out of scope |
| s 3 | eligible pensioner: the 30 June 1967 limit is encoded; the entitlements and rates are inputs, worked out under the DFRB Act's scales |
| s 4 | encoded |
| s 5 | encoded |
| s 6 | encoded |
| s 7 | recognised: the Finance Minister determines the rate (NOTHING) |
| s 8 | encoded |
| s 9 | recognised: a determined rate (NOTHING) |
| s 10 | encoded: treated as an eligible pensioner |
| s 11 | out of scope: re-engagement under s 69 |
| s 12 | out of scope: reclassification |
| s 13 | encoded |
| ss 14-15 | out of scope: payment and the date of effect |

## Forks (readings taken)

- **F1, the order of ss 4, 5 and 6.** The s 4 increase is scaled for commutation or election (s 5), then reduced by the earlier increase (s 6), not below nil. Section 6 reduces "any increase ... under the preceding provisions", which include s 5. This follows the 1971 Act's reading.
- **F2, s 8(1).** The widow's share is taken of her husband's increase after s 6. Section 5 is disregarded only for a commutation under s 74; an election under ss 61A-61B still scales.
- **F3, ss 7, 9.** The rate is a ministerial determination, so the answer is NOTHING.
- **F4, s 3.** A pension that began to be payable on 30 June 1967 is not "before" that day, so it gets no increase (nil).
- **F5, s 13.** It bars the pensioner's own increase, not a widow's.
- **Known limits (from the independent pass).**
  - The s 3 definitions and deeming rules are inputs.
  - For a s 8(1)(a) widow (member died before retirement), the pension-began date stands for the widow's pension.
  - The class is a single choice, so overlapping classes (a s 7 pensioner with a Superannuation Act pension) cannot be expressed.
  - The guard against a nil uncommuted rate is not in the source.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-20: 3 modules: 37 assertions satisfied, 0 failed, 0 other errors — 16 the encoder's (`dfrb67-tests.l4`), 21 independent (`tests-independent.l4`). No assertion is expected to fail.

## Open questions for an Australian lawyer

- **F2:** does s 8(1) leave the scaling for an election in place?
