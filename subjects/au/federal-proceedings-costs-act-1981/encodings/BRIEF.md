# Encoding brief: the Federal Proceedings (Costs) Act 1981 (Cth), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Federal Proceedings (Costs) Act 1981** (No. 23, 1981), Commonwealth of Australia, compilation No. 15 of 10 June 2025, from the Federal Register of Legislation, deposited at `../registers/source-bundle/C2004A02401.txt` (CC BY 4.0).

## Seat

The encoding is written from the seat of **the litigant who seeks a costs certificate and payment from the Attorney-General** (the repo's `CLAUDE.md` rule of 2026-10-18).

## Scope

Top level, in the litigant's words: *"Can the court grant me a costs certificate? What is the most the Attorney-General can pay me on it? Is it vacated if the other side appeals and wins? Can the Attorney-General pay me now?"*

In scope: ss 6-10A (the routes, as one input), s 14, s 15, s 16(2), s 17(1)-(2), s 18 and the Schedule. Out of scope: ss 1-5, 11-13, 16(1), 17(3)-(4), 19-22 (definitions, earlier appeals, Chambers, no appeal from refusal, repayment, delegation, application, regulations). Whether the court grants the certificate, and whether the Attorney-General pays, are discretionary; the encoding answers whether they may.

## Inputs

- My route to a certificate: the ten routes in ss 6-10A, or none.
- Who I am: an individual; a company with paid-up capital under $200,000 not related to a larger one; the Commonwealth, a State, the NT, their authority, or a party suing for them; a company with $200,000 or more, or related to one.
- The court or tribunal; my costs; any higher amount prescribed by regulation.
- Whether the other side appealed further and succeeded; whether the other side has appealed or sought leave; whether a notice of no intended appeal was given.

## Rules that matter

- Encode isomorphically, with an `@ref` on every rule; `@export default` on the top-level goal.
- A failing assertion is a finding. Never edit an expected value to match the code.

## Deliverables

`fpc-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
