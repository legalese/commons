# Scout Association Act 1924 (Cth) — encoding notes (row `legalese-aswathy`)

DRAFT. No Australian lawyer has read this encoding against the Act.

## What is encoded

There is one top-level goal, `the scout position for` (`scout-rules.l4`). It answers:

- whether there is an offence under s 2 or s 4;
- the maximum penalty in units;
- whether a prosecution may be instituted.

The encoded provisions are ss 2 and 4-6.

## Seat

The encoding is written from the seat of **the person who uses the Scout name or a Scout uniform or emblem**. This follows the repo's `CLAUDE.md` rule of 2026-10-18.

**The top-level question, in their words:** "Do I commit an offence by using this name or uniform; what is the penalty; and can I be prosecuted without the Minister's consent?"

## Coverage

| Provision | Disposition |
|---|---|
| ss 1-1A | applied: Chapter 2 of the Criminal Code (fault elements are folded into the inputs) |
| s 2 | encoded |
| s 3 | applied: s 4 covers only items registered under s 3 |
| s 4 | encoded |
| s 5 | encoded |
| s 6 | encoded |

## Forks (readings taken)

- **F1, s 4.** Proof of authority lies on the defendant (a legal burden). The input is whether authority was proved.
- **F2.** The maximum penalty is 1 penalty unit per offence. The value of a penalty unit is set elsewhere and is not computed.
- **Known limits (from the independent pass).**
  - Under s 4 only the Local Branch for the area of use can authorise; the single proved-authority input must be FALSE where another area's Branch gave it.
  - s 3 registration and the Criminal Code fault rules (s 1A) are inputs.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-20: 3 modules: 28 assertions satisfied, 0 failed, 0 other errors — 9 the encoder's (`scout-tests.l4`), 19 independent (`tests-independent.l4`). No assertion is expected to fail.

## Open questions for an Australian lawyer

- None of substance.
