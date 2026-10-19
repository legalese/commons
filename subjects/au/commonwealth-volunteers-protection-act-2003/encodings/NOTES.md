# Commonwealth Volunteers Protection Act 2003 (Cth) — encoding notes (row `legalese-aswathy`)

DRAFT. No Australian lawyer has read this encoding against the Act.

## What is encoded

There is one top-level goal, `the volunteer position for` (`cvp-rules.l4`). It answers:

- whether the work was done on a voluntary basis;
- whether I am protected from civil liability;
- who bears the liability;
- whether I must assist in defending the claim;
- whether an indemnity I gave has effect.

The operative Act is encoded: ss 4(2)-(4) and 5-9. The source is the compilation prepared on 19 April 2011 (C2011C00290).

## Seat

The encoding is written from the seat of **the volunteer**. This follows the repo's `CLAUDE.md` rule of 2026-10-18.

**The top-level question, in their words:** "Did I do the work on a voluntary basis; am I protected from civil liability for what I did; if not me, who bears it; must I help the Commonwealth defend the claim; and does an indemnity I gave have any effect?"

The facts it asks for are ones that person can state, or findings made about them: good faith, impairment, and knowledge of the limits of their authority.

## Coverage

| Provision | Disposition |
|---|---|
| ss 1-3 | out of scope: machinery and extension to external Territories |
| s 4(1) | definitions: "Commonwealth" and "Commonwealth authority" are folded into the input; "organised" includes directed and supervised |
| s 4(2)-(3) | encoded |
| s 4(4) | applied: an omission is a thing done |
| s 5 | encoded |
| s 6 | encoded |
| s 7 | encoded |
| s 8 | encoded |
| s 9 | encoded |
| s 10 | inert: the Damage by Aircraft Act 1999 is not overridden |
| s 11 | out of scope: regulations (the prescribed amount is an input) |

## Forks (readings taken)

- **F1, s 4(3).** "My usual pay from my employer only" counts as voluntary only where the work is of a kind usually done unpaid, or for less than the prescribed amount. Any extra payment beyond expenses (or below the prescribed amount) is treated as "more than that".
- **F2, s 6.** Every condition of s 6(1) must hold, and every exception in (2)-(4) must be absent. Good faith, impairment and knowledge are inputs.
- **F3, s 7.** Where s 6 protects the volunteer, the Commonwealth or the authority bears the liability. The exception is an authority that another Act already protects (s 7(2)): then no one bears it under this Act. Where s 6 does not protect the volunteer, the volunteer bears it, since this Act does not take it away.
- **F4, s 9.** An indemnity is void only against a liability the Commonwealth or authority incurs under this Act. In any other case this Act does not affect it, which is reported as "has effect".
- **Known limits (from the independent pass).**
  - There is no input for whether an indemnity was given. "My indemnity has effect" means only that s 9 would not void one; where the Act is silent, it gives no positive answer.
  - s 4(3)(a)(i)-(ii) are one pay option, and (b)(i)-(ii) one input.
  - "Organised", and "knew or ought to have known", are single inputs.
  - The prescribed amount is not in the deposited text, so it is a category, not a number.
  - s 8's "may incur" (a disputed liability) is not modelled; facts go in as settled.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-19: 4 modules: 65 assertions satisfied, 0 failed, 0 other errors — 30 the encoder's (`cvp-tests.l4`), 35 independent (`tests-independent.l4`). No assertion is expected to fail.

## Open questions for an Australian lawyer

- **F4:** does s 9 also void an indemnity given before the work was done, against a liability that later falls on the Commonwealth?
