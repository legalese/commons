# Encoding brief: the Trade Union and Labour Relations (Consolidation) Act 1992 (UK), in L4

This brief is the whole specification. Read it fully before opening the source.

## The subject

**Trade Union and Labour Relations (Consolidation) Act 1992** (1992 c. 52), United Kingdom. The source is the revised text on legislation.gov.uk, point in time 25 August 2026, deposited at `../registers/source-bundle/ukpga-1992-52.txt` (Crown copyright, Open Government Licence v3.0). The revised text runs together some wording from before and after the Employment Rights Act 2025 (for example s 188(A1) and (1)); the version as amended is encoded.

## Seat

The encoding is written from the seat of **the worker or employee** (the repo's `CLAUDE.md` rule of 2026-10-18).

## Scope: a few goals, and only the sections they need

The user's instruction: "Keep very few meaningful top level goals and work out the contents related to it. You don't have to model irrelevant sections just because it is there in the Act. Calculate dates as it is given."

Top level, in the worker's words: *"I was treated badly, or dismissed, because of my union membership or activities (or for not joining). Am I protected; by when must I complain; can I apply for interim relief, and by when; what is the least basic award? My employer is making collective redundancies: when should consultation have begun, what protective award can I get, and by when must the complaints be made? I was dismissed for taking part in official industrial action: is that unfair, and by when must I complain?"*

1. **Union membership and activities** (ss 146(1)-(2), (5)-(5A), 147, 152(1)-(2), (3), 153, 154, 156(1), 161(1)-(3), (6), 292A):
   - whether a detriment (s 146) or a dismissal (ss 152-153) falls within the protection;
   - the last day for a s 146 complaint (s 147(1)(a), with s 292A);
   - whether an interim relief application (s 161) is in time, with the union certificate where needed;
   - that the qualifying period does not apply (s 154), and the minimum basic award of £9,157 (s 156(1)).
2. **Collective redundancies** (ss 188(A1), (1A), 189(4)-(5A), 190(2), 192(2)-(2A), 292A):
   - whether the duty to consult applies, and the last day by which consultation had to begin;
   - the protected period of an award (its start and end, at most 180 days) and the remuneration under it;
   - the last days for the s 189 and s 192 complaints.
3. **Protected industrial action** (ss 238A(1)-(2), 238(5), 239(1)-(2)):
   - whether the dismissal is unfair under s 238A;
   - the last day for the complaint (s 239(2)(a)), with the "date of dismissal" of s 238(5).

Left out on purpose: trade union government, elections, political funds and discipline of members (Parts I and II except as above); refusal of employment (ss 137-143); inducements (ss 145A-145F); time off (ss 168-173); recognition (Schedule A1); ballots and the law on industrial action itself (ss 219-235); the bodies (ACAS, CAC, Certification Officer).

## Inputs, not worked out

- The reason for the act or dismissal, as found; whether union activity was "at an appropriate time" (s 146(2), 152(2)); whether the worker is an employee; whether others in similar positions were not dismissed (s 153).
- Dates: the act (or the last of a series), the effective date of termination, the day notice was given, the interim relief application and certificate, ACAS Day A and Day B.
- Redundancies: the numbers proposed to be dismissed within 90 days, in all and at one establishment; the threshold number under s 195A regulations (at least 20); the dates of the first and last dismissals and of the start of consultation; the award date, the period the tribunal fixes, a week's pay and any days excluded by s 191; the last day of unpaid remuneration.
- Industrial action: whether the employee took protected industrial action (an act induced by an act protected by s 219) and whether that was the reason.
- The basic award as worked out under the Employment Rights Act 1996 before reductions.

## Dates, as the Act gives them

Compute every period exactly as the Act words it. The UK has no general next-working-day rule.

- **"before the end of the period of three months beginning with" a day (ss 147(1)(a), 192(2)(a)); "during the period of three months beginning with" (s 189(5)(b)); "six months beginning with" (s 239(2)(a))**: the last day is the day before the corresponding date, or the last day of the month where there is none.
- **s 292A(3)**: the days from the day after Day A to Day B, so far as they fall within the period, are not counted; the limit moves later by that many days. **(4)**: if the limit (as so extended) falls on or after Day A and on or before the day one month after Day B, it becomes that day.
- **s 161(2), "before the end of the period of seven days immediately following the effective date of termination"**: by the effective date of termination + 7.
- **s 188(1A), "at least 45 days" / "at least 30 days" "before the first of the dismissals takes effect"**: consultation must begin on or before the first dismissal day − 45 (or − 30).
- **s 189(4)**: the protected period begins with the earlier of the first dismissal and the award, and runs for the days the tribunal fixes, not more than 180; its last day is the first day + days − 1.
- **s 190(2)**: a week's pay for each week; part of a week pro rata (days ÷ 7).

## Rules that matter

- Encode isomorphically, with an `@ref` on every rule and the Act's words beside each limb.
- Where the source does not answer, use `REFUSE "…"`; never `FALSE` or `0`.
- `@export default` on the top-level goal; `@export` on each goal, with `@desc` on each parameter.
- A failing assertion is a finding. Never edit an expected value to match the code.

## Deliverables (in this `encodings/` directory)

`tulrca-*.l4` modules and tests, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `check.sh`.
