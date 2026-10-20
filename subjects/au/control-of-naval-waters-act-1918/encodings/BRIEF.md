# Encoding brief: the Control of Naval Waters Act 1918 (Cth), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Control of Naval Waters Act 1918** (No. 28, 1918), Commonwealth of Australia, compilation No. 6 of 21 October 2016, from the Federal Register of Legislation, deposited at `../registers/source-bundle/C1918A00028.txt` (CC BY 4.0).

## Seat

The encoding is written from the seat of **the master, person in charge, or owner of a vessel, aircraft or vehicle in naval waters or on their foreshore** (the repo's `CLAUDE.md` rule of 2026-10-18).

## Scope

Top level, in that person's words: *"Is my craft exempt? Is it an offence if I do not follow the superintendent's direction, and what is the most I can get? Must I pay for the superintendent moving or removing my property? If I do not pay, from when can it be sold, and what do I get back or still owe?"*

In scope: s 2 (exempt vessel, vessel), s 6(1)-(2A), s 6A(1)-(2), s 8. Out of scope: ss 1, 3-3C (Proclamations and appointments; whether waters are naval waters is an input), s 4 (regulations), s 5, s 6(3), s 6A(3), s 7 (the superintendent's powers, which are inputs to s 8), ss 9-10.

## Inputs

- My craft: a Commonwealth or Australian Navy vessel; a foreign naval vessel declared exempt; another vessel; an aircraft; a vehicle. Where it is: within naval waters; on their foreshore; elsewhere.
- Whether I am in command or charge; whether the superintendent gave me a direction; whether I complied.
- Whether the superintendent moved or removed it under s 6(3), 6A(3) or 7; the Commonwealth's expenses; the day the demand for payment was made; whether the expenses have been paid; the sale proceeds and the expenses of the sale.

## Rules that matter

- Calculate the dates as the Act gives them.
- Encode isomorphically, with an `@ref` on every rule; `@export default` on the top-level goal.
- A failing assertion is a finding. Never edit an expected value to match the code.

## Deliverables

`cnw-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
