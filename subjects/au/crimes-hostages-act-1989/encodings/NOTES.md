# Crimes (Hostages) Act 1989 (Cth) — encoding notes (row `legalese-aswathy`)

DRAFT. No Australian lawyer has read this encoding against the Act.

## What is encoded

There is one top-level goal, `the hostage position for` (`ch-rules.l4`). It answers:

- whether it is hostage-taking, and an offence;
- whether I may be imprisoned for life;
- whether I may be charged, convicted, or committed for trial;
- the latest day to reappear after a change of venue.

The encoded provisions are ss 6(2), 7, 8, 9, 10(1)-(2) and 12(1), with Article 12 of the Convention. The source is the compilation of 10 March 2016.

## Seat

The encoding is written from the seat of **the person accused of hostage-taking**. This follows the repo's `CLAUDE.md` rule of 2026-10-18.

**The top-level question, in their words:** "Is what I did hostage-taking under the Act; can I be charged in Australia; can I be convicted given a foreign conviction; what must happen before trial?"

## Coverage

| Provision | Disposition |
|---|---|
| ss 1-5 | out of scope: machinery; definitions folded into the inputs |
| s 6 | (2) encoded; (1) is out of scope |
| s 6A | out of scope |
| s 7 | encoded |
| s 8 | encoded |
| s 9 | encoded |
| s 10 | (1)-(2) encoded; (3) is out of scope |
| s 11 | out of scope |
| s 12 | (1) encoded; the rest is out of scope |
| ss 13-15 | out of scope; the Convention's date in force is an input |
| Schedule | Article 12 applied through s 9(1); the rest is inert |

## Forks (readings taken)

- **F1, s 8(1) (changed after the independent pass).** "At any time after the Convention enters into force for Australia": it is in force from the start of that day, so an act on that day is covered.
- **F2, s 8(2).** The punishment is imprisonment for life or any lesser term.
- **F3, s 9(2)-(3).** The single-State exclusion is one input, which already excludes a person present only by extradition.
- **F4, s 12(1).** "Not later than 28 days after the day on which the order is made": the latest day is the order day + 28.
- **Known limits (from the independent pass).**
  - The single-State case and Article 12 are each one input.
  - The preconditions of a change of venue order are not inputs.
  - s 10(2) (charge and arrest without consent) has no output.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-20: 3 modules: 44 assertions satisfied, 0 failed, 0 other errors — 16 the encoder's (`ch-tests.l4`), 28 independent (`tests-independent.l4`). No assertion is expected to fail.

## Open questions for an Australian lawyer

- None of substance beyond F1.
