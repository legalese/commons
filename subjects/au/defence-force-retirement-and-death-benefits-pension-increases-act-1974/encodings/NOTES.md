# Defence Force Retirement and Death Benefits (Pension Increases) Act 1974 (Cth) — encoding notes (row `legalese-aswathy`)

DRAFT. No Australian lawyer has read this encoding against the Act.

## What is encoded

There is one goal, `my 1974 increase for` (`dfrdb74-rules.l4`). It gives the 1974 increase in a DFRB pension (Part II) or a DFRDB pension benefit (Part III). The encoded provisions are ss 3, 7-9, 13, 16-18 and 22. The source is the Act as made.

## Seat

The encoding is written from the seat of **the pensioner or pension-benefit recipient, or the widow or child**. This follows the repo's `CLAUDE.md` rule of 2026-10-18.

**The top-level question, in their words:** "By how much does my annual pension or pension benefit increase from the pay-day of 4 July 1974?"

## Coverage

| Provision | Disposition |
|---|---|
| ss 1-2, 4-6 | out of scope |
| s 3 | encoded: (1), (3); (2) (revised index numbers) is folded into the inputs |
| ss 7-9 | encoded; whether a pension falls in s 8 or s 9 is the case input |
| ss 10-12 | out of scope |
| s 13 | noted: from the pay-day of 4 July 1974 |
| ss 14-15 | out of scope |
| ss 16-18 | encoded |
| ss 19-21 | out of scope |
| s 22 | noted: from the pay-day of 4 July 1974 |

## Forks (readings taken)

- **F1, s 3(1).** The percentage rises are written in words in this Act ("A—B expressed as a percentage of B"). No formula is missing.
- **F2, ss 8(2)(a)(ii)-(iii), (b).** These adjust the 1973 base for reclassification, commutation or a widow's notional pension. The 1973 amount is the adjusted figure, and it is an input.
- **F3, ss 9(2), 18(3).** The counted period starts on the day the pension became payable (s 9), or the day after the retirement or death (s 18(1)(a)). The caller gives that first day. Months are counted by corresponding dates to 30 June 1974.
- **F4, s 18(3).** The period ends on 30 June 1974 and is divided by 12, as in s 9(2).

- **F5, ss 9(1), 18(1) (changed after the independent pass).** A pension or benefit that became payable after 15 June 1974 gets no increase. The start of the counted period stands for that date, which for s 18(1)(a) is the day after the retirement or death.
- **Known limits (from the independent pass).** The case is chosen by the caller, and its date conditions are not checked. The pay-day of 4 July 1974 is not an output.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-19: 3 modules: 35 assertions satisfied, 0 failed, 0 other errors — 10 the encoder's (`dfrdb74-tests.l4`), 25 independent (`tests-independent.l4`). No assertion is expected to fail.

## Open questions for an Australian lawyer

- None of substance.
