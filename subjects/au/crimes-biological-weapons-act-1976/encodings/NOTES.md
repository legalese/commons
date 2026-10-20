# Crimes (Biological Weapons) Act 1976 (Cth) — encoding notes (row `legalese-aswathy`)

DRAFT. No Australian lawyer has read this encoding against the Act.

## What is encoded

There is one top-level goal, `the weapons position for` (`cbw-rules.l4`). It answers:

- whether I commit an offence;
- whether I may be imprisoned for life, and the maximum fine in penalty units;
- whether the material is forfeited, and the last day it may be retained without a prosecution;
- whether I may be committed for trial;
- whether the analyst's certificate can be used against me, and the last day to notify the prosecutor to call the analyst.

The encoded provisions are ss 5, 8, 9(1)-(2), 10(3)-(4), 12(4) and 12(6)(a). The source is the compilation of 11 May 2018.

## Seat

The encoding is written from the seat of **the person who holds biological agents, toxins or weapons, or is charged**. This follows the repo's `CLAUDE.md` rule of 2026-10-18.

**The top-level question, in their words:** "Is what I do unlawful; what is the most I can get; can my material be taken, and for how long; what must happen before I can be committed for trial?"

## Coverage

| Provision | Disposition |
|---|---|
| ss 1-4 | out of scope: machinery |
| s 5 | encoded |
| ss 6-7 | out of scope |
| s 8 | encoded; whether a type and quantity has a peaceful justification is an input |
| s 9 | (1)-(2) encoded; (3)-(4) are out of scope |
| s 10 | (3)-(4) encoded; (1)-(2), (5) are out of scope |
| s 11 | out of scope: jurisdiction |
| s 12 | (4), (6)(a) encoded; the rest is out of scope |
| s 13 | out of scope: regulations |
| Schedule | inert: the Convention's terms carry their meaning into s 8 |

## Forks (readings taken)

- **F1, s 8(2)(b).** A natural person may be imprisoned "for a specified period or for life", fined up to 100 penalty units, or both.
- **F2, s 9(2).** "Until the expiration of a period of 60 days after the seizure": the last day is the seizure day + 60. Where a prosecution was instituted within that period, the material is held until it ends, so no day is given.
- **F5, s 9(1) (changed after the independent pass).** Material is forfeited only where s 8(1) is contravened, so not for a non-citizen acting outside Australia (s 5).
- **F3, s 10(3)-(4).** Without the Attorney-General's written consent, a person may be charged, arrested and remanded, but not committed for trial.
- **F4, s 12(6)(a).** "At least 5 days notice": the notice must be given no later than the hearing day − 5, as for the other notice periods read in this repo. The Court may allow it otherwise (s 12(6)(b)), which is not modelled.
  - **Disagreement from the independent pass, left open.** The tester reads the 5 days as clear days (hearing − 6); that assertion (`tests-independent.l4` line 62) is left failing. The tester's confidence is medium.
- **Known limits (from the independent pass).**
  - Whether the analyst can be required to attend (including a s 12(6)(b) order) and the day notice was given are not modelled.
  - s 10(4) (charge, arrest, remand without consent) has no output.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-20: 3 modules: 38 assertions satisfied, 1 failed, 0 other errors — 17 the encoder's (`cbw-tests.l4`), 22 independent (`tests-independent.l4`). One assertion in `tests-independent.l4` (line 62) is expected to fail: it reads the 5 days' notice as clear days (F4).

## Open questions for an Australian lawyer

- **F4:** are the 5 days clear days?
