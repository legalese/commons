# Services Trust Funds Act 1947 (Cth) — encoding notes (row `legalese-aswathy`)

DRAFT. No Australian lawyer has read this encoding against the Act.

## What is encoded

There is one top-level goal, `the fund position for` (`stf-rules.l4`). It answers:

- whether I am within the class the fund serves;
- whether I am barred from benefiting;
- whether my benefit is then for the trustees to decide.

The encoded provisions are ss 4, 8(a), 14, 26, 29 and 32. The source is the compilation of 1 July 2014.

## Seat

The encoding is written from the seat of **the serving or former member of the Defence Force, or a dependant**. This follows the repo's `CLAUDE.md` rule of 2026-10-18.

**The top-level question, in their words:** "Am I among those the Navy, Army or Air Force relief fund is for; can I benefit?"

## Coverage

| Provision | Disposition |
|---|---|
| ss 1-2 | out of scope |
| s 4 | encoded: member of the Defence Force; dependant is the trustees' opinion, an input |
| ss 5-7 | out of scope: trustees |
| s 8 | (a) applied: the trustees determine entitlement and extent; (b)-(f) are out of scope |
| ss 9-13 | out of scope |
| s 14 | encoded |
| ss 24, 27, 30 | out of scope: the funds and their assets |
| ss 26, 29, 32 | encoded |
| ss 34, 36 | out of scope |

## Forks (readings taken)

- **F1, ss 26, 29, 32.** "Served in, or in association with" the Navy, Army or Air Force is one input: the arm.
- **F2, s 4 dependant.** A dependant is whoever the trustees consider one; the opinion is an input.
- **F3, s 8(a).** Being within the class does not entitle anyone to a benefit; whether, and how much, is for the trustees, subject to the regulations.
- **Known limits (from the independent pass).**
  - The last output means "I may be considered for a benefit"; the trustees decide.
  - A trustee of a different fund (not barred from this one) cannot be expressed.
  - s 9 delegation is not modelled.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-20: 3 modules: 40 assertions satisfied, 0 failed, 0 other errors — 11 the encoder's (`stf-tests.l4`), 29 independent (`tests-independent.l4`). No assertion is expected to fail.

## Open questions for an Australian lawyer

- None of substance.
