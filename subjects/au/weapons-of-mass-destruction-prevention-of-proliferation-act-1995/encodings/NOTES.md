# Weapons of Mass Destruction (Prevention of Proliferation) Act 1995 (Cth) — encoding notes (row `legalese-aswathy`)

DRAFT. No Australian lawyer has read this encoding against the Act.

## What is encoded

There is one top-level goal, `the WMD position for` (`wmd-rules.l4`). It answers:

- whether I commit an offence under ss 9-11, and under s 14(6);
- the maximum imprisonment;
- whether goods are forfeited;
- the last day a s 14 notice is in force.

The encoded provisions are ss 6(3), 9-12, 14(2), (4), (6) and 17(1), with a permit (s 13) as an input. The source is the compilation of 6 November 2018.

## Seat

The encoding is written from the seat of **the person who supplies goods, exports goods or provides services**. This follows the repo's `CLAUDE.md` rule of 2026-10-18.

**The top-level question, in their words:** "Is what I do an offence; what is the most I can get; are my goods forfeited; until when does a Minister's prohibition notice bind me?"

## Coverage

| Provision | Disposition |
|---|---|
| ss 1-5 | out of scope: machinery; definitions folded into the inputs |
| s 6 | (3) encoded; the rest is out of scope |
| ss 7-8A | out of scope |
| ss 9-11 | encoded |
| s 12 | the Minister's written notice is an input |
| s 13 | a permit, and keeping its conditions, is an input |
| s 14 | (2), (4), (6) encoded; (1), (3), (5) are out of scope |
| ss 15-16 | out of scope |
| s 17 | (1) encoded; the rest is out of scope |

## Forks (readings taken)

- **F1, ss 9(2), 10(2), 11(2).** Only a conditional s 14 notice whose conditions are complied with removes the ss 9-11 offence.
- **F2, s 14(4) (changed after the independent pass).** "A period of 12 months beginning on the day when the notice is given": it ends on the day before the corresponding day 12 months later, or the month's last day where there is none (a notice of 29 February ends on 28 February).
- **F3, s 17(1).** Goods are forfeited when supplied or exported in contravention of the Act; services are not goods.
- **F4, ss 9-11 penalties.** Imprisonment for up to 8 years; the Crimes Act's fine alternatives are not computed.
- **Known limits (from the independent pass).**
  - "No permit" and "a permit with breached conditions" are one input.
  - Revocation is a yes/no, not a date.
  - Attempts (s 17(1)) are not an input; forfeiture is tied to an offence.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-20: 3 modules: 50 assertions satisfied, 0 failed, 0 other errors — 16 the encoder's (`wmd-tests.l4`), 34 independent (`tests-independent.l4`). No assertion is expected to fail.

## Open questions for an Australian lawyer

- None of substance.
