# Parliamentary Privileges Act 1987 (Cth) — encoding notes (row `legalese-aswathy`)

DRAFT. No Australian lawyer has read this encoding against the Act.

## What is encoded

There is one top-level goal, `the privileges position for` (`pp-rules.l4`). It answers:

- whether a House may punish my conduct, and the most imprisonment and fine it may impose;
- whether I commit an offence under ss 12-13, and the most imprisonment and penalty units;
- whether I am immune that day from court attendance and civil arrest.

The encoded provisions are ss 4, 6, 7(1), (5), (7), 12, 13 and 14. The source is the compilation of 21 October 2016.

## Seat

The encoding is written from the seat of **the person dealing with the Commonwealth Parliament**. This follows the repo's `CLAUDE.md` rule of 2026-10-18.

**The top-level question, in their words:** "Can a House punish me for this, and how far; is it a crime under this Act; am I immune from court and civil arrest on this day?"

## Coverage

| Provision | Disposition |
|---|---|
| ss 1-3A | out of scope: machinery and definitions (folded into the inputs) |
| s 4 | encoded |
| s 5 | out of scope: the continuing powers |
| s 6 | encoded |
| s 7 | (1), (5), (7) encoded; (2)-(4), (6), (8) are out of scope |
| s 8 | out of scope: no expulsion |
| s 9 | out of scope: resolutions and warrants |
| ss 10-11 | out of scope: defences for reports and tabled papers |
| s 12 | encoded |
| s 13 | encoded |
| s 14 | encoded |
| ss 15-17 | out of scope |

## Forks (readings taken)

- **F1, s 4.** Whether conduct is an improper interference is the House's judgment; the encoding asks it as a fact and answers whether a House may punish, not whether it will.
- **F2, s 7.** A House may impose up to 6 months' imprisonment, or a fine, but not both for the same offence. A corporation is reported with no imprisonment.
- **F3, s 14(1)-(2).** "Within 5 days before or 5 days after" a sitting day is read as no more than 5 days either side: a sitting day on 10 March covers 5 to 15 March, and with a sitting on 11 March, to 16 March.
- **F4, s 13.** Publication by or with the authority of a House or committee ends the offence.
- **Known limits (from the independent pass).**
  - s 13's "without the authority" and "unless published or authorised" share one input.
  - s 7(7)'s not-both rule is not a computed output; a corporation's House imprisonment is 0.
  - The s 14 sitting days are one list the caller must choose correctly.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-20: 3 modules: 57 assertions satisfied, 0 failed, 0 other errors — 23 the encoder's (`pp-tests.l4`), 34 independent (`tests-independent.l4`). No assertion is expected to fail.

## Open questions for an Australian lawyer

- **F3:** is the fifth day before or after included?
