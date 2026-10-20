# Explosives Act 1961 (Cth) — encoding notes (row `legalese-aswathy`)

DRAFT. No Australian lawyer has read this encoding against the Act.

## What is encoded

There is one top-level goal, `the explosives position for` (`expl-rules.l4`). It answers:

- whether Part II reaches the explosives;
- whether I commit an offence;
- the maximum imprisonment and fine;
- whether a lesser prescribed penalty applies instead.

The encoded provisions are ss 9 and 20. The source is the compilation of 11 December 2024.

## Seat

The encoding is written from the seat of **the person who handles explosives, or is in or near a Commonwealth explosives area**. This follows the repo's `CLAUDE.md` rule of 2026-10-18.

**The top-level question, in their words:** "Do the Commonwealth's handling rules reach these explosives; if I break the regulations or an order, what is the most I can get?"

## Coverage

| Provision | Disposition |
|---|---|
| ss 1-8 | out of scope: machinery; definitions folded into the inputs |
| s 9 | encoded |
| ss 10-11A | out of scope: regulation- and order-making powers |
| s 12 | out of scope: indemnity at the Commonwealth's discretion |
| ss 13-19 | out of scope: Part III powers and orders |
| s 20 | encoded |
| s 21 | out of scope |

## Forks (readings taken)

- **F1, s 20(a).** The fine may be combined with imprisonment ("or both"); the daily fine of 2 penalty units is added for each day a continuing offence continues, and the encoding counts the days given.
- **F2, s 20(b).** Where the regulations prescribe a lesser penalty, it applies instead; the encoding reports that and gives no figure.
- **F3.** Whether a contravention occurred depends on the regulations or an order, which are not deposited: it is an input.
- **Known limits (from the independent pass).**
  - Where a lesser penalty is prescribed, the months and units show 0 beside the flag; they are not "no penalty".
  - Breaking an order and breaking the regulations are one input.
  - Foreign explosives without approval or not held for defence can only be entered as anyone else's.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-20: 3 modules: 29 assertions satisfied, 0 failed, 0 other errors — 10 the encoder's (`expl-tests.l4`), 19 independent (`tests-independent.l4`). No assertion is expected to fail.

## Open questions for an Australian lawyer

- **F1:** from when does a continuing offence's daily fine run?
