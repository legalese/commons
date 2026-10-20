# Encoding brief: the Defence Forces Special Retirement Benefits Act 1960 (Cth), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Defence Forces Special Retirement Benefits Act 1960** (No. 68 of 1960), Commonwealth of Australia, the compilation prepared on 19 April 2001, from the Federal Register of Legislation, deposited at `../registers/source-bundle/C1960A00068.txt` (CC BY 4.0). It commenced on 1 February 1961 (the proclaimed date, endnote). Section 11 was repealed in 1965.

## Seat

The encoding is written from the seat of **the Regular Army soldier discharged in the 1961 reduction of establishment** (the repo's `CLAUDE.md` rule of 2026-10-18).

## Scope

Top level, in the soldier's words: *"Does this Act apply to me? What gratuity or pension do I get, and by when must I pay my contribution to get the higher pension?"*

In scope: s 4, ss 6-7, s 9(1)-(2), (4)-(5), s 10(1)-(2), (4)-(5), and the First Schedule. Out of scope: ss 1-3, s 5 (service for pension: the completed years are an input), s 8 (gratuity mechanics), ss 9(3), (6)-(7), 10(3), (6)-(7) (the Actuary, the statement's content, death before the prescribed day), s 12, and the Second Schedule (for repealed s 11).

## Inputs

- s 4: whether on 1 February 1961 I was a male Regular Army member contributing to the Fund; whether I was in the Royal Australian Army Ordnance Corps; when my engagement expires; whether I was an officer during the prescribed period; my date of birth; whether the Minister declared me to be discharged for the reduction; the day I was discharged and whether for that reason; whether I became a member again the next day.
- My completed years of service for pension; whether I would have completed 20 years by age 55; my category (101-109); my daily rate of active pay.
- The Board's figures: whether I am a reduced benefit contributor; the maximum pension rate (when the Board determines it); the minimum pension rate; the maximum additional pension contribution; for s 10, whether I was contributing for additional benefits, and the normal pension rate and normal additional contribution.
- The day the Board's statement was served; the day I paid a contribution and its amount.

## Rules that matter

- Amounts are in pounds, as printed; 10s 6d is £0.525.
- Calculate the dates as the Act gives them.
- Encode isomorphically, with an `@ref` on every rule; `@export default` on the top-level goal.
- A failing assertion is a finding. Never edit an expected value to match the code.

## Deliverables

`dfsrb-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
