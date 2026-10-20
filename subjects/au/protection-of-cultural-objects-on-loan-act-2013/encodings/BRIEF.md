# Encoding brief: the Protection of Cultural Objects on Loan Act 2013 (Cth), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Protection of Cultural Objects on Loan Act 2013** (No. 12, 2013), Commonwealth of Australia, compilation No. 2 of 14 October 2024, from the Federal Register of Legislation, deposited at `../registers/source-bundle/C2013A00012.txt` (CC BY 4.0).

## Seat

The encoding is written from the seat of **the foreign lender of an object brought to Australia for exhibition** (the repo's `CLAUDE.md` rule of 2026-10-18).

## Scope

Top level, in the lender's words: *"Is my object protected while it is on loan in Australia, and until when? Can I be sued over it, or can a claim be brought against the object? Can it be seized or forfeited?"*

In scope: s 5 (lender), s 8, s 9(1)-(2), (4), s 10(1), (4), s 11, s 12. Out of scope: ss 1-4, 6-7, 9(3), (5), 10(2)-(3), 13-21 (heritage laws, approval and review, delegation, compensation, regulations). The approval of the institution, the constitutional connection and the exclusions are inputs.

## Inputs

- Who I am: an individual not ordinarily resident in Australia; a foreign corporation; a foreign body politic; another person.
- Whether it was imported on loan under a temporary loan arrangement with the exhibiting institution or a facilitator; only or mainly for temporary public exhibition; whether the institution was approved on import; whether one of the s 8(1)(d) connections exists; whether the import contravenes a prescribed law; whether it is a Class A object; whether the institution's notice excluded it.
- The import day; any export day; any later day the Minister declares; the day asked about.
- The proceeding (a claim against me personally about the object; a claim against the object itself; Proceeds of Crime or prescribed proceedings; none) and the power relied on (an ordinary statutory power; Crimes Act Part IAA; the Proceeds of Crime Act; a police-only seizure power; a prescribed law).

## Rules that matter

- Calculate the dates as the Act gives them.
- Encode isomorphically, with an `@ref` on every rule; `@export default` on the top-level goal.
- A failing assertion is a finding. Never edit an expected value to match the code.

## Deliverables

`pcol-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
