# Commonwealth Motor Vehicles (Liability) Act 1959 (Cth) — encoding notes (row `legalese-aswathy`)

DRAFT. No Australian lawyer has read this encoding against the Act.

## What is encoded

There is one top-level goal, `the vehicle claim position for` (`cmvl-rules.l4`). It covers ss 3(2), 5 and 6 and answers two questions:

- whether the driver is conclusively presumed to be the Commonwealth's agent;
- whether the jury question is decided as for a like claim against an insured owner.

## Seat

The encoding is written from the seat of **the person killed or injured by a Commonwealth vehicle**, or their estate or dependants. This follows the repo's `CLAUDE.md` rule of 2026-10-18.

**The top-level question, in their words:** "In my claim against the Commonwealth for death or injury caused by its vehicle, is the driver presumed to be its agent; and is a jury question decided as if the vehicle had been insured?"

## Coverage

| Provision | Disposition |
|---|---|
| ss 1-2, 4, 7 | out of scope |
| s 3 | (1) folded into the inputs; (2) encoded |
| s 5 | encoded; (2) is inert |
| s 6 | encoded |

## Forks (readings taken)

- **F1, s 5(3).** The section reaches occurrences after 8 September 1958, which is taken as a lower bound for every claim.
- **F2, s 5(1)(b).** A claim for contribution is treated as "a claim against the Commonwealth or an authority".
- **Known limits (from the independent pass).**
  - A contribution claim (s 5(1)(b)) is not separated from a damages claim, so it also gets the s 6 answer.
  - s 6's condition of proceedings in a State or Territory court has no input.
  - The 8 September 1958 bound is applied to s 6 as well as s 5, though s 5(3) extends only s 5.
  - Whether a body is a Commonwealth authority (s 3(1)) is an input.

## Checks

`L4=~/.local/bin/l4 ./check.sh` (l4 built from l4-ide unstable at 7768812fa), run on 2026-10-20: 3 modules: 27 assertions satisfied, 0 failed, 0 other errors — 9 the encoder's (`cmvl-tests.l4`), 18 independent (`tests-independent.l4`). No assertion is expected to fail.

## Open questions for an Australian lawyer

- None of substance.
