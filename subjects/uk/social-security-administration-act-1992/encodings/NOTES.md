# Social Security Administration Act 1992 (UK) — encoding notes (row `legalese-aswathy`)

DRAFT. No UK lawyer has read this encoding against the Act.

## What is encoded

There is one top-level goal, `the overpayment position for` (`ssaa-goal.l4`). After a benefit overpayment it answers:

- the amount recoverable under s 71;
- which offence, if any, is committed under s 111A or s 112, and its maximum sentence;
- the s 115A administrative penalty, and the last day to withdraw agreement to it.

The rules are in `ssaa-rules.l4`:

1. **Recoverable overpayments:** s 71(1), (3) and (5A).
2. **Offences:** ss 111A(1)-(1B), (3)-(4) and 112(1)-(1B), (2).
3. **Penalty as an alternative to prosecution:** s 115A(1), (1A), (2)-(3A) and (5).

## Seat

The encoding is written from the seat of **the claimant who has been overpaid**, the person the law is applied to (the repo's `CLAUDE.md` rule of 2026-10-18).

**The top-level question, in their words:** "I was overpaid benefit. Must I pay it back; could I be prosecuted, and for how long; and if I am offered a penalty instead, how much is it and how long do I have to change my mind?"

The facts it asks for are ones that person can state, or findings made about them.

The function names were written before the rule and have not been renamed.

## Coverage

| Provision | Disposition |
|---|---|
| ss 1-70 | out of scope: claims, interviews, adjudication (largely repealed) |
| s 71(1), (3), (5A) | encoded (goal 1); (2), (4), (6)-(11) are out of scope |
| ss 71ZA-111 | out of scope |
| s 111A | encoded (goal 2); the elements are one input; (1C)-(1H) on recipients are out of scope |
| s 112 | encoded (goal 2); the elements are one input |
| ss 113-115 | out of scope |
| s 115A(1), (1A), (2)-(3A), (5) | encoded (goal 3); (1B)-(1C), (4), (6)-(8) are out of scope |
| s 115B onwards | out of scope |

## Forks (readings taken)

- **F1, s 71(5A).** No amount is recoverable until the awarding decision has been revised, superseded or reversed on appeal. The "except where regulations otherwise provide" exception is not modelled.
- **F2, ss 111A and 112.** Where both are made out, s 111A (dishonesty) is reported, because it is the more serious. In Scotland, s 111A reads "knowingly" for "dishonestly", so knowing conduct in Scotland falls within s 111A.
- **F3, s 115A(3): "rounded down to the nearest whole penny".** The floor of 50% of the overpayment in pence. The £350 minimum applies to overpayments under £700, and the £5,000 maximum to those over £10,000.
- **F4, s 115A(1A).** Where no overpayment was made but one would have been recoverable, the penalty is £350.
- **F5, s 115A(5): "the period of 14 days beginning with the day on which he agrees".** It ends on that day + 13.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-18: 5 modules: 94 assertions satisfied, 0 failed, 0 other errors — 27 the encoder's (`ssaa-tests.l4`), 67 independent (`tests-independent.l4`). No assertion is expected to fail. The independent pass is incomplete: its assertions were written and pass, but its report is missing.

## Open questions for a UK lawyer

- **F2:** in Scotland, is every knowing failure to notify within s 111A rather than s 112?
