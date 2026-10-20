# Encoding brief: the Protection of Word "Anzac" Act 1920 (Cth), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Protection of Word "Anzac" Act 1920** (No. 54, 1920), Commonwealth of Australia, compilation of 28 February 2014, from the Federal Register of Legislation, deposited at `../registers/source-bundle/C1920A00054.txt` (CC BY 4.0). Only s 1 and s 22 remain.

## Seat

The encoding is written from the seat of **the person using the word "Anzac"**, or a word resembling it (the repo's `CLAUDE.md` rule of 2026-10-18).

## Scope

Top level, in that person's words: *"If my use of 'Anzac' breaches the Regulations, what is the most I can get?"*

In scope: s 22(1)(g), (2) and (3). The Regulations themselves are not deposited: whether a use breaches subregulation 2(1), 3(1) or another regulation is an input.

## Inputs

- My use: in connection with a trade, business, calling or profession; with an entertainment, lottery or art union; as the name of a private residence, boat, vehicle, charitable or other institution, or a building connected with it; as the name of a street, road or park; another use.
- The breach: subregulation 2(1), subregulation 3(1), another regulation, or none.

## Rules that matter

- Encode isomorphically, with an `@ref` on every rule; `@export default` on the top-level goal.
- A failing assertion is a finding. Never edit an expected value to match the code.

## Deliverables

`anzac-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
