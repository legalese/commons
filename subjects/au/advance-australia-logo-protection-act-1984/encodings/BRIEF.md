# Encoding brief: the Advance Australia Logo Protection Act 1984 (Cth), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Advance Australia Logo Protection Act 1984** (No. 20, 1984), Commonwealth of Australia, compilation No. 2 of 10 December 2015, from the Federal Register of Legislation, deposited at `../registers/source-bundle/C2004A02884.txt` (CC BY 4.0).

## Seat

The encoding is written from the seat of **the trader who applies the logo's design to articles, or sells, hires or imports articles bearing it** (the repo's `CLAUDE.md` rule of 2026-10-18).

## Scope

Top level, in that person's words: *"Did I infringe the monopoly in the design of the logo? Does my dealing infringe the copyright in the logo? Can I be sued for using it before the Act, under a licence the Company purported to grant?"*

In scope: s 3(1) (prescribed period), s 11(1), s 15(2), s 19(2)-(3). Out of scope: ownership and dealings by the Company (ss 6-10, 14, 17-18), who may sue and remedies (s 11(2)-(6), s 12), jurisdiction (s 13), compensation (s 16), ss 19(1), (4), 20-21 and the Schedules.

## Inputs

- My dealing: applying the design to an article; selling or hiring an article to which the design was applied in infringement; importing for sale or trade an article to which the design was applied outside Australia; selling or hiring an imported article bearing the design.
- Whether the design or a fraudulent or obvious imitation of it is involved; whether I have the owner's licence; the day I do it; whether I acted under a purported licence (s 15(2)).

## Rules that matter

- Calculate the dates as the Act gives them.
- Encode isomorphically, with an `@ref` on every rule; `@export default` on the top-level goal.
- A failing assertion is a finding. Never edit an expected value to match the code.

## Deliverables

`aal-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
