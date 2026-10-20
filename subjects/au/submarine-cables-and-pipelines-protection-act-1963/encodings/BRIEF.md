# Encoding brief: the Submarine Cables and Pipelines Protection Act 1963 (Cth), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Submarine Cables and Pipelines Protection Act 1963** (No. 61, 1963), Commonwealth of Australia, compilation No. 11 of 21 October 2016, from the Federal Register of Legislation, deposited at `../registers/source-bundle/C1963A00061.txt` (CC BY 4.0).

## Seat

The encoding is written from the seat of **the person whose conduct on an Australian-registered ship damages a submarine cable or pipeline**, the owner laying or repairing a cable, or the ship's owner who sacrificed gear (the repo's `CLAUDE.md` rule of 2026-10-18).

## Scope

Top level, in that person's words: *"Have I committed an offence by breaking or injuring a cable or pipeline, and what is the most I can get? Must I pay for the repair of a cable I damaged laying my own? Am I indemnified for the anchor or net I sacrificed to avoid one?"*

In scope: s 5, s 7, s 8, s 9 and s 10(2). Out of scope: ss 1-4, 5A, 6, s 10(1), s 11.

## Inputs

- Whether the cable or pipeline lies beneath the high seas or in the exclusive economic zone, and whether it is a Telecommunications Act cable in a protection zone (s 5).
- Whether the ship is registered in Australia or a Territory; what was damaged (a telegraph or telephone cable so as might interrupt communications, a pipeline, a high-voltage cable, or a telegraph or telephone cable not so); my fault (my conduct resulted in it; I was negligent as to whether it would; neither).
- Whether we acted solely to save our lives or our ship, and took all necessary precautions (s 7(2)).
- Whether I am prosecuted summarily or on indictment (s 10(2)).
- Whether I was laying or repairing my own cable or pipeline and broke another (s 8).
- Whether gear was sacrificed to avoid injuring the cable after all reasonable precautions (s 9).

## Rules that matter

- Encode isomorphically, with an `@ref` on every rule; `@export default` on the top-level goal.
- A failing assertion is a finding. Never edit an expected value to match the code.

## Deliverables

`scp-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
