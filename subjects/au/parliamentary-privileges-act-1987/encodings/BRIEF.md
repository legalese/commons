# Encoding brief: the Parliamentary Privileges Act 1987 (Cth), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Parliamentary Privileges Act 1987** (No. 21, 1987), Commonwealth of Australia, compilation No. 4 of 21 October 2016, from the Federal Register of Legislation, deposited at `../registers/source-bundle/C2004A03430.txt` (CC BY 4.0).

## Seat

The encoding is written from the seat of **the person dealing with the Commonwealth Parliament**: a member of the public whose conduct is in question, a witness, or a member or officer claiming immunity (the repo's `CLAUDE.md` rule of 2026-10-18).

## Scope

Top level, in that person's words: *"Can a House punish me for this, and what is the most it can impose? Do I commit an offence under the Act by what I did to a witness or with in camera evidence, and what is the most I can get? Am I immune on this day from being required to attend a court or tribunal, or arrested in a civil cause?"*

In scope: s 4, s 6, s 7(1), (5), (7), s 12, s 13, s 14. Out of scope: ss 1-3A, 5, 7(2)-(4), (6), (8), ss 8-11, 15-17 (machinery, expulsion, reports and tabled papers, the Bill of Rights in court proceedings, certificates).

## Inputs

- Whether I am a natural person or a corporation.
- Whether my conduct amounts, or is intended or likely to amount, to an improper interference (s 4); whether it is only defamatory or critical; whether it was in the presence of a House or committee (s 6).
- What I do, if anything, under ss 12-13; whether a House or committee has published or authorised the in camera evidence.
- My role (member, officer, person required to attend, none), the day asked about, and the relevant sitting or attendance days.

## Rules that matter

- Calculate the dates as the Act gives them.
- Encode isomorphically, with an `@ref` on every rule; `@export default` on the top-level goal.
- A failing assertion is a finding. Never edit an expected value to match the code.

## Deliverables

`pp-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
