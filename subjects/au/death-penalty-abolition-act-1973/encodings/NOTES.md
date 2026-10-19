# Death Penalty Abolition Act 1973 (Cth) — encoding notes (row `legalese-aswathy`)

DRAFT. No Australian lawyer has read this encoding against the Act.

## What is encoded

There is one top-level goal, `the death penalty position for` (`dpa-rules.l4`). For one offence it answers:

- whether the Act applies;
- whether death may be imposed;
- where the law provides for death, the penalty in its place.

The whole operative Act is encoded: ss 3-6. The source is the compilation prepared on 19 April 2010.

## Seat

The encoding is written from the seat of **the person charged with, or convicted of, an offence**. This follows the repo's `CLAUDE.md` rule of 2026-10-18.

**The top-level question, in their words:** "Can I be sentenced to death for this offence; and if the law I am charged under provides for death, what is the penalty instead?"

The facts it asks for are ones that person can state: which law creates the offence, and whether it provides for death.

## Coverage

| Provision | Disposition |
|---|---|
| ss 1-2 | out of scope: machinery |
| s 3 | encoded: (2)-(3) as the kinds of law, (4) as the date being irrelevant; (1) (territorial reach) is assumed |
| s 4 | encoded |
| s 5 | encoded |
| s 6 | encoded |

## Forks (readings taken)

- **F1, s 5 and State laws.** Section 5 applies only to the laws in s 3(2). For a State offence, s 6 forbids the death penalty, but the Act does not say what penalty takes its place; that is for the State's own law. The encoding gives NOTHING, and does not invent one; this was changed after the independent pass.
- **F2, s 3(2), "to the extent to which the powers of the Parliament permit".** Whether an Imperial Act falls within those powers is an input.
- **F3, other laws.** For a law outside s 3(2)-(3), the Act does not answer, and the encoding gives NOTHING.

- **Known limits (from the independent pass).**
  - s 4 and s 6 are combined in one answer; nothing records separately that s 4's "not liable" does not reach State offences.
  - There is no input for the offence date, since s 3(4) makes it irrelevant.
  - An Imperial Act outside the Parliament's powers is entered as "some other law".
  - s 5's parenthesis is folded into "the law provides for death".

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-19: 4 modules: 93 assertions satisfied, 0 failed, 0 other errors — 18 the encoder's (`dpa-tests.l4`), 75 independent (`tests-independent.l4`). No assertion is expected to fail.

## Open questions for an Australian lawyer

- None of substance. The Act is short and its operation is plain on its face.
