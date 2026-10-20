# Encoding brief: the War Gratuity Act 1945 (Cth), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**War Gratuity Act 1945** (No. 16, 1945), Commonwealth of Australia, compilation No. 4 of 21 October 2016, from the Federal Register of Legislation, deposited at `../registers/source-bundle/C1945A00016.txt` (CC BY 4.0). Amounts are in decimal dollars as the compilation prints them.

## Seat

The encoding is written from the seat of **the Second World War member, or their dependants** (the repo's `CLAUDE.md` rule of 2026-10-18).

## Scope

Top level, in their words: *"How many months of my service count at the overseas rate and at the general rate, and how much war gratuity is to be credited? Can it be withheld?"*

In scope: s 2 (month), s 4, s 6, s 8, s 12, s 13, s 14(1), s 15 (as an input), s 16. Out of scope: ss 7, 9-11 (which days count as qualifying service: the day counts are inputs), s 14(2)-(3), ss 17 onwards (who receives it after death, the date of entitlement, administration) and the Schedule (disqualified classes, an input).

## Inputs

- The days of overseas qualifying service, and of general qualifying service (which includes the overseas days: s 9(1)(a)).
- Whether the member returned at their own request, for prescribed disciplinary reasons, or for an excepted injury or illness (s 8).
- Whether the member died of war service, and whether while in overseas qualifying service or other general qualifying service (s 13).
- Whether someone was totally dependent on a member who died of war service before 1 July 1947 (s 14).
- Whether the member is in a disqualified class (s 15); debts to deduct (s 16).

## Rules that matter

- Encode isomorphically, with an `@ref` on every rule; `@export default` on the top-level goal.
- A failing assertion is a finding. Never edit an expected value to match the code.

## Deliverables

`wg-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
