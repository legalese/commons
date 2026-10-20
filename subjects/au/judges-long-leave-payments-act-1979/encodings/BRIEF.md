# Encoding brief: the Judges (Long Leave Payments) Act 1979 (Cth), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Judges (Long Leave Payments) Act 1979** (No. 90, 1979), Commonwealth of Australia, compilation No. 6 of 1 September 2021, from the Federal Register of Legislation, deposited at `../registers/source-bundle/C2004A02100.txt` (CC BY 4.0).

## Seat

The encoding is written from the seat of **the Judge**, or on the Judge's death the survivors (the repo's `CLAUDE.md` rule of 2026-10-18).

## Scope

Top level, in the Judge's words: *"When I stop being a Judge, is a long leave payment due; for how many weeks of judicial salary and how much; and to whom is it paid?"*

In scope: s 3 (Judge, judicial salary, retirement), ss 3A-3B, s 4, s 5(1)-(2) and s 7. Out of scope: s 5(2A)-(4) (the Attorney-General's directions on distribution and trustees), s 6 (appropriation).

## Inputs

- My office (a Judge of a federal court other than the High Court or the Federal Circuit and Family Court (Division 2); a person with the same status by virtue of an Act; an ACT Supreme Court Judge immediately before the 1992 transfer; or an excluded office).
- How I cease: resignation or end of term; reaching the age at which I must cease; removal under s 72 of the Constitution or a like provision; death. Whether a new appointment as a Judge takes effect immediately after.
- My years of service as a Judge, and of qualifying service (s 4(3)).
- My annual salary immediately before ceasing.
- Whether the Attorney-General certifies permanent disability or infirmity (s 4(2B)); whether the Governor-General directs payment on removal (s 7).
- Whether I leave a surviving spouse or de facto partner, or dependants.

## Rules that matter

- 5.2 weeks for each **completed** year of qualifying service; at most 52 weeks under s 4(1) only.
- Judicial salary is a weekly rate of one fifty-second of the annual salary.
- Encode isomorphically, with an `@ref` on every rule; `@export default` on the top-level goal.
- A failing assertion is a finding. Never edit an expected value to match the code.

## Deliverables

`jllp-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
