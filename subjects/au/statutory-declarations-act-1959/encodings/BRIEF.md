# Encoding brief: the Statutory Declarations Act 1959 (Cth), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Statutory Declarations Act 1959** (No. 52, 1959), Commonwealth of Australia, compilation No. 8 of 1 January 2024, from the Federal Register of Legislation, deposited at `../registers/source-bundle/C1959A00052.txt` (CC BY 4.0).

## Seat

The encoding is written from the seat of **the declarant**: the person making a Commonwealth statutory declaration (the repo's `CLAUDE.md` rule of 2026-10-18).

## Scope

Top level, in the declarant's words: *"Is my statutory declaration validly made? Does the Act let me use it for what I want? If I knowingly put a false statement in it, what is the most I can get?"*

In scope: s 6, s 7A, s 8, s 9, s 9A(1), s 11. Out of scope: ss 1-5A, 7, 9A(2)-(3), 9B, 10, 12-16 (machinery, references in other laws, approval of platforms and their obligations, declarations under other laws, jurisdiction, regulations, forms, review). Who is a prescribed person, which platforms and identity services are approved, and the approved form are inputs.

## Inputs

- Whether it is in the approved form.
- How it was made: signed under a prescribed person's observation; completed and signed on an approved online platform; neither.
- How I signed (by hand on a physical form; electronically on an electronic form; otherwise), and whether the method identifies me and shows my intention, and was appropriately reliable or proven in fact.
- For s 9: whether I was observed in person or by video link; whether the prescribed person signed the declaration, or signed a copy they were satisfied was a true copy.
- For s 9A: whether my identity was verified by an approved identity service as prescribed; whether it includes the prescribed platform information.
- The use I want (for a Commonwealth or Territory law; in a Commonwealth Department's administration; as evidence in court; another), and whether the law shows a contrary intention.
- Whether I intentionally made a false statement in it.

## Rules that matter

- Encode isomorphically, with an `@ref` on every rule; `@export default` on the top-level goal.
- A failing assertion is a finding. Never edit an expected value to match the code.

## Deliverables

`sd-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
