# Encoding brief: the Damage by Aircraft Act 1999 (Cth), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Damage by Aircraft Act 1999** (No. 107, 1999), Commonwealth of Australia. The source is the compilation in force on 31 March 2013 (amendments up to Act No. 191, 2012; register id C2013C00130), from the Federal Register of Legislation, deposited at `../registers/source-bundle/C2004A00498.txt` (CC BY 4.0).

## Seat

The encoding is written from the seat of **the person on the ground**: the person who suffered injury, loss or damage, or whose property did (the repo's `CLAUDE.md` rule of 2026-10-18).

## Scope

Top level, in that person's words: *"Does the Act apply to what happened to me; who is liable to me; can I recover without proving negligence; and by how much are my damages reduced if I was partly to blame?"*

In scope: ss 4 (aircraft excludes model aircraft), 5-7 (in flight, operator, employees), 9 (application), 10 (liability), 11 (no proof of fault), 11A (contributory negligence) and the application provisions in endnote 3 (items 7(3)-(4) of Act No. 191, 2012). Sections 1-3, 8, 11B (contribution between defendants) and 12 are out of scope.

## Inputs

- The aircraft: a Defence Force aircraft or not; a model aircraft or not; within Australian territory; one of the aircraft or kinds of air navigation in s 9(4).
- The cause: an impact with an aircraft in flight (or just before); with part of one damaged or destroyed in flight; with a person, animal or thing that dropped or fell from one in flight; a result of such an impact; or something else.
- Whether the only harm to me (or my property) is mental injury; the day it was suffered.
- The people: whether the operator was authorised to use the aircraft and had the exclusive right to use it for more than 14 consecutive days; whether the operator used it without the authority of the person entitled to control its navigation, and whether that person took all reasonable steps to prevent it; whether the owner had an active role in its operation, and whether someone else had the exclusive right to use it under a lease or other arrangement, or with the owner providing financial accommodation.
- The damages the court finds would be recoverable but for my negligence, and the share of responsibility it attributes to me.

## Dates

- s 10(1A) (mental injury alone) applies to mental injury suffered on or after 31 March 2013 (endnote 3, item 7(3)).
- s 11A applies to injury, loss, damage or destruction suffered on or after 31 March 2013 (item 7(4)). Before then the Act does not reduce damages; the answer is NOTHING.

## Rules that matter

- Encode isomorphically, with an `@ref` on every rule and the Act's words beside each limb.
- Where the source does not answer, give NOTHING (or `REFUSE`); never `FALSE`.
- `@export default` on the top-level goal.
- A failing assertion is a finding. Never edit an expected value to match the code.

## Deliverables

`dba-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
