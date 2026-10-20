# Encoding brief: the Civil Dispute Resolution Act 2011 (Cth), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Civil Dispute Resolution Act 2011** (No. 17, 2011), Commonwealth of Australia, compilation No. 4 of 14 October 2024, from the Federal Register of Legislation, deposited at `../registers/source-bundle/C2011A00017.txt` (CC BY 4.0). Parts 2-5 commenced on 1 August 2011.

## Seat

The encoding is written from the seat of **a party to civil proceedings**: the applicant or the respondent (the repo's `CLAUDE.md` rule of 2026-10-18).

## Scope

Top level, in that person's words: *"Must I file a genuine steps statement, and by when? May it leave out the excluded parts? Does not filing invalidate my case, and can the court hold it against me?"*

In scope: s 5 (eligible court), s 6(1), (3)-(4), s 7(1), s 10(2), ss 11-12(1), ss 15-17. Out of scope: s 3 (object), s 4 (what genuine steps are: examples only), the content of the statements (ss 6(2), 7(2), 8), the lawyer's duty (ss 9, 12(2)-(3)), ss 13, 17A-19.

## Inputs

- My side (applicant or respondent); the court (the Federal Court, the Federal Circuit and Family Court (Division 2), or another); whether the proceedings are civil.
- The kind of proceedings: ordinary, or one of the excluded kinds in ss 15-17; whether only part of the proceedings is of that kind.
- The day the application is filed; for a respondent, whether I was given a copy of the applicant's statement and the hearing date specified in the application.

## Rules that matter

- Calculate the dates as the Act gives them.
- Encode isomorphically, with an `@ref` on every rule; `@export default` on the top-level goal.
- A failing assertion is a finding. Never edit an expected value to match the code.

## Deliverables

`cdr-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
