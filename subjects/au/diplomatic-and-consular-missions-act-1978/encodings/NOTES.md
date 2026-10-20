# Diplomatic and Consular Missions Act 1978 (Cth) — encoding notes (row `legalese-aswathy`)

DRAFT. No Australian lawyer has read this encoding against the Act.

## What is encoded

There is one top-level goal, `the missions position for` (`dcm-rules.l4`). It answers:

- whether my conduct is caught by s 4;
- whether an injunction may be granted against me;
- whether a warrant to remove my sign may issue;
- the last day a removal warrant can be in force.

The encoded provisions are ss 4(1)-(2B), (5)-(6) and 5(1), (5). The source is the compilation of 21 October 2016.

## Seat

The encoding is written from the seat of **the person who displays a sign or makes a representation**. This follows the repo's `CLAUDE.md` rule of 2026-10-18.

**The top-level question, in their words:** "Is my sign or claim caught; can I be restrained; can my sign be taken down, and for how long?"

## Coverage

| Provision | Disposition |
|---|---|
| ss 1-3 | applied: the definitions are folded into the inputs |
| s 3A | out of scope: the Criminal Code |
| s 4 | (1)(a), (2), (2A), (2B), (5), (6) encoded; (1)(b)-(d) (aiding, inducing, being a party) are treated as the conduct itself; (3)-(4), (7) are out of scope |
| s 5 | (1), (5) encoded; (2)-(4), (6)-(7) are out of scope |
| s 6 | out of scope: certificates are evidence |
| s 7 | out of scope: jurisdiction |

## Forks (readings taken)

- **F1, s 4(2)(c)-(d), (2A)(e), (2B)(c).** The exceptions are one input each: acting for a designated overseas mission in its authorised capacity (or at its staff's request) excuses conduct about a consented mission; acting for a consented diplomatic or consular mission excuses conduct about a designated overseas mission.
- **F2, s 4(5)-(6).** An injunction may be granted if the Court is satisfied I have engaged in the conduct, or it appears I am likely to; the Court's findings are inputs, and the grant remains discretionary ("may").
- **F3, s 5(1).** A removal warrant needs a finding that displaying a sign is caught.
- **F4, s 5(5).** "A period not exceeding 6 months" is taken as beginning on the day of issue. It ends on the day before the corresponding day 6 months later, or at the end of that month where there is none.
- **Disagreement from the independent pass, left open (F4).** The tester reads a warrant issued on 15 January 2026 as in force through 15 July 2026; the encoding ends it on 14 July 2026, as for the other period-of-months readings in this repo. The tester's confidence is low to moderate.
- **Known limits (from the independent pass).**
  - The carve-outs in s 4(2)(c)-(d) and s 4(2A)(e)(i)-(ii) are single inputs.
  - The authorised-capacity correspondence (s 4(2A)(d), (2B)) is folded into the implication input.
  - s 4(1)(b)-(d) and interim injunctions are not separately modelled.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-20: 3 modules: 44 assertions satisfied, 1 failed, 0 other errors — 16 the encoder's (`dcm-tests.l4`), 29 independent (`tests-independent.l4`). One assertion in `tests-independent.l4` (line 48) is expected to fail: it reads the warrant's 6 months as running through the corresponding day (F4).

## Open questions for an Australian lawyer

- **F4:** does a warrant's period begin on the day of issue or on a day the Court specifies?
