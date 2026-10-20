# Encoding brief: the Explosives Act 1961 (Cth), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Explosives Act 1961** (No. 65, 1961), Commonwealth of Australia, compilation No. 9 of 11 December 2024, from the Federal Register of Legislation, deposited at `../registers/source-bundle/C1961A00065.txt` (CC BY 4.0). The Act is mostly a power to make regulations; the regulations are not deposited.

## Seat

The encoding is written from the seat of **the person who handles explosives, or is in or near a Commonwealth explosives area** (the repo's `CLAUDE.md` rule of 2026-10-18).

## Scope

Top level, in that person's words: *"Do the Commonwealth's handling rules reach these explosives? If I break the regulations or an order made under them, what is the most I can get?"*

In scope: s 9 and s 20. Out of scope: the definitions (s 5, folded into the inputs), the regulation- and order-making powers (ss 10-11A, 13-19, 21), s 12 (indemnity, a Commonwealth discretion).

## Inputs

- Whose explosives: the Commonwealth's (or in its possession or control); Commonwealth-made and being exported under an arrangement; a foreign government's or forces', here with approval for defence; anyone else's.
- Whether I contravened the regulations or an order; the days the offence continues; whether the regulations prescribe a lesser penalty.

## Rules that matter

- Encode isomorphically, with an `@ref` on every rule; `@export default` on the top-level goal.
- A failing assertion is a finding. Never edit an expected value to match the code.

## Deliverables

`expl-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
