# Encoding brief: the Services Trust Funds Act 1947 (Cth), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Services Trust Funds Act 1947** (No. 23, 1947), Commonwealth of Australia, compilation of 1 July 2014, from the Federal Register of Legislation, deposited at `../registers/source-bundle/C1947A00023.txt` (CC BY 4.0).

## Seat

The encoding is written from the seat of **the serving or former member of the Defence Force, or a dependant, who seeks help from one of the relief trust funds** (the repo's `CLAUDE.md` rule of 2026-10-18).

## Scope

Top level, in that person's words: *"Am I among those the Navy, Army or Air Force relief fund is for? Am I barred because I am a trustee or a trustee's dependant? Who decides whether I get anything?"*

In scope: s 4 (member of the Defence Force, dependant), s 8(a), s 14, ss 26, 29 and 32. Out of scope: ss 1-2, 5-7, 8(b)-(f), 9-13 (trustees' constitution and powers), ss 24, 27, 30 (the funds' assets), ss 34, 36.

## Inputs

- The fund: the Royal Australian Navy Relief Trust Fund; the Australian Military Forces Relief Trust Fund; the Royal Australian Air Force Welfare Trust Fund.
- The member in whose right I apply: a member of the Navy, Army or Air Force; of a nursing or women's service attached or auxiliary to the Defence Force; of a Navy ship's canteen staff; a person accredited to the Defence Force who served officially on full-time paid duty; none of these. The arm the member served in or with.
- Whether I am the member, or whether the trustees consider me a dependant.
- Whether I am a trustee of the fund or a trustee's dependant.

## Rules that matter

- A trustees' opinion is asked as a fact; whether and how much is paid is for the trustees.
- Encode isomorphically, with an `@ref` on every rule; `@export default` on the top-level goal.
- A failing assertion is a finding. Never edit an expected value to match the code.

## Deliverables

`stf-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
