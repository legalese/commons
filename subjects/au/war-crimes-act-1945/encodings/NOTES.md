# War Crimes Act 1945 (Cth) — encoding notes (row `legalese-aswathy`)

DRAFT. No Australian lawyer has read this encoding against the Act.

## What is encoded

There is one top-level goal, `the war crime position for` (`wc-rules.l4`). It answers:

- whether it is a serious crime, a war crime, and an offence under the Act;
- whether I may be charged;
- whether I may be imprisoned for life, or the maximum term otherwise;
- whether the laws of war are a defence.

The encoded provisions are ss 5 (war), 6, 7, 9(1), 10, 11, 16 and 17(2). The source is the compilation of 23 May 2018.

## Seat

The encoding is written from the seat of **the person accused of a war crime**. This follows the repo's `CLAUDE.md` rule of 2026-10-18.

**The top-level question, in their words:** "Is what I am said to have done a serious crime and a war crime under the Act; can I be charged; what is the most I can get; do I have a defence?"

## Coverage

| Provision | Disposition |
|---|---|
| ss 1-4 | out of scope |
| s 5 | war encoded (Europe, 1 September 1939 to 8 May 1945); occupation is folded into the connection |
| s 6 | encoded; whether an act was a listed offence under the law then in force is an input |
| s 7 | encoded; (4) (several crimes together) is out of scope |
| s 8 | applied |
| s 9 | (1) encoded; (2)-(3) are out of scope |
| s 10 | encoded |
| s 11 | encoded |
| ss 12-15 | out of scope |
| s 16 | applied: superior orders are not a defence |
| s 17 | (2) encoded; (3)-(5) (onus) are out of scope |
| ss 18 onwards | out of scope |

## Forks (readings taken)

- **F1, ss 5, 9(1).** Both ends of the period (1 September 1939 and 8 May 1945) are included.
- **F2, s 6(4)-(6).** Deportation or internment in a death or slave labour camp is a serious crime whatever the local law allowed.
- **F3, s 7(3).** Persecution or genocide must be in a country involved in a war, or occupied, as the Act defines war (in Europe in the period).
- **F4, s 10.** Life imprisonment where the offence involved wilful killing; otherwise up to 25 years.
- **Known limits (from the independent pass).**
  - Citizen and resident (s 11) are one input.
  - s 16 (superior orders) has no input; the encoding never gives it as a defence.
  - s 7(4) (several crimes together) is not modelled; s 7(3) is read as requiring Europe.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-20: 3 modules: 34 assertions satisfied, 0 failed, 0 other errors — 16 the encoder's (`wc-tests.l4`), 18 independent (`tests-independent.l4`). No assertion is expected to fail.

## Open questions for an Australian lawyer

- None of substance.
