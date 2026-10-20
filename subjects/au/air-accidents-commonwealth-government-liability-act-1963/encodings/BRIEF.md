# Encoding brief: the Air Accidents (Commonwealth Government Liability) Act 1963 (Cth), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Air Accidents (Commonwealth Government Liability) Act 1963** (No. 74, 1963), Commonwealth of Australia, compilation No. 9 of 17 June 2021, from the Federal Register of Legislation, deposited at `../registers/source-bundle/C1963A00074.txt` (CC BY 4.0).

## Seat

The encoding is written from the seat of **the passenger killed or injured in an air accident, or their dependants** (the repo's `CLAUDE.md` rule of 2026-10-18).

## Scope

Top level, in that person's words: *"Is the Commonwealth (or the ACT or Northern Territory) liable under this Act, under which Part? What is the most it can pay, and how much can I recover? Is my claim barred, or must it wait?"*

In scope: s 4 (passenger), ss 6, 8, 10(1), 11, 12, 14, 15(1), 16(1), 17. Out of scope: ss 1-2, 5, 7, 9, 10(2)-(3), 13, 15(2)-(3), 16(2)-(3), 18 (the incorporated Carriers' Liability Act provisions, substitution of liability, the Commonwealth's request procedure and regulations). The s 31(1AA) and prescribed s 31(1)(b) amounts of the Civil Aviation (Carriers' Liability) Act 1959 are inputs.

## Inputs

- The operator (the Commonwealth or a Commonwealth authority, or another); whether I was on board as working crew of a commercial operator.
- The connection with the Commonwealth (employee or seaman travelling in the course of employment; carriage paid for by it; travelling for its purposes under its arrangements; the same with the ACT or NT; none).
- Whether Part IV of the Carriers' Liability Act or a declared State Act applies; whether the death or injury entitles anyone to a Veterans' Entitlements pension.
- Whether the accident was on board or in embarking or disembarking.
- The two cap amounts; the damages assessed; insurance from Commonwealth-funded cover or allowance; damages or compensation from the carrier or others.
- Whether I recovered damages from the Commonwealth otherwise; whether I failed to pursue others, settled with another without written consent, or refused the Commonwealth's request; whether an action against another is pending.

## Rules that matter

- Encode isomorphically, with an `@ref` on every rule; `@export default` on the top-level goal.
- A failing assertion is a finding. Never edit an expected value to match the code.

## Deliverables

`aa-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
