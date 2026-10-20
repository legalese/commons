# Encoding brief: the Maternity Leave (Commonwealth Employees) Act 1973 (Cth), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Maternity Leave (Commonwealth Employees) Act 1973** (No. 72, 1973), Commonwealth of Australia, compilation No. 10 of 1 September 2021, from the Federal Register of Legislation, deposited at `../registers/source-bundle/C2004A00024.txt` (CC BY 4.0).

## Seat

The encoding is written from the seat of **the pregnant Commonwealth employee** (the repo's `CLAUDE.md` rule of 2026-10-18).

## Scope

Top level, in the employee's words: *"When must I be away from work, and until when? How long may my maternity leave last? Which days of it are paid?"*

In scope: s 3 (confinement), s 5 (whether the Act applies, as an input), s 6(1)-(4), (4C), (4F) and s 7. Out of scope: ss 1-2, 4, 5A, 6(4A)-(4B), (4D)-(4E), (4G), (5)-(9), 7A-7B, 8-11 (the pay rate, other leave, resumption applications, continuity, temporary employees, discrimination, delegation).

## Inputs

- Whether the Act applies to me (s 5).
- The expected date of birth; the day I was confined (birth or other end of pregnancy), if any.
- Any date to which I have permission to continue duty (s 7(1)); any date on which I have permission to resume duty (s 7(3)).
- The day my continuous qualifying service first exceeds 12 months (s 6(4)).
- Whether I was on unauthorised absence just before, without extenuating circumstances (s 6(4C)); whether I am on unpaid leave of over 6 weeks and the Agency Head has not determined otherwise (s 6(4F)).

## Rules that matter

- Calculate the dates as the Act gives them.
- Encode isomorphically, with an `@ref` on every rule; `@export default` on the top-level goal.
- A failing assertion is a finding. Never edit an expected value to match the code.

## Deliverables

`ml-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
