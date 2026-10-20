# Encoding brief: the Adelaide Airport Curfew Act 2000 (Cth), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Adelaide Airport Curfew Act 2000** (No. 29, 2000), Commonwealth of Australia, compilation No. 7 of 14 October 2024, from the Federal Register of Legislation, deposited at `../registers/source-bundle/C2004A00621.txt` (CC BY 4.0). Times are legal time in South Australia (s 5).

## Seat

The encoding is written from the seat of **the operator of an aircraft** using Adelaide Airport, often a private owner-pilot (the repo's `CLAUDE.md` rule of 2026-10-18).

## Scope

Top level, in the operator's words: *"Is this take-off or landing in the curfew? Is it permitted? Is it an offence, and what is the most I can get? If I landed on a runway other than 05 because of the weather, by when must I lodge a return?"*

In scope: s 3 (curfew period, curfew shoulder period), s 6, ss 9, 11-14 (as permissions and aircraft kinds), s 15(3), ss 16-18 (as circumstances). Out of scope: ss 1-2, 4-5A, 7-8, 10, 15(1)-(2), (4), 19-onwards (definitions of aircraft classes, runways, quotas, information notices and false information, delegation, appointments, conduct of agents). Whether an aircraft meets a noise standard, has a permission, or is of a specified type is an input.

## Inputs

- The movement (take-off or landing) and its hour and minute.
- The aircraft: a propeller aircraft of 34,000 kg or less meeting the Annex noise standards; a jet of 34,000 kg or less of a type the regulations specify; an international aircraft with the Minister's shoulder-period permission; a low noise heavy freight aircraft with the Minister's curfew permission; another aircraft.
- Whether taxi clearance was received before 11 pm (s 14).
- Any special circumstance (the emergencies in s 17, resuming a flight interrupted by one, a dispensation kept to its conditions, a declared national emergency, none).
- The day of any landing on a runway other than 05 for the weather.

## Rules that matter

- Calculate the dates as the Act gives them.
- Encode isomorphically, with an `@ref` on every rule; `@export default` on the top-level goal.
- A failing assertion is a finding. Never edit an expected value to match the code.

## Deliverables

`aac-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
