## Procedure layer: the one-month wait before the court's order and before the first meeting of the transferor company (ss 915 to 918)

The procedure that Companies Act 2006 Part 27, Chapter 2 lays down for the routes that excuse a meeting of members of a merging company, written as regulative rules over the Boolean encoding in `coa20-part27-merger.l4`.
The unit is s 917 (the court's order that no meeting of any of the merging companies is required, where the transferee company holds all the relevant securities of the transferor company).
Sections 916 and 918 carry the same one-month wait counted from the first meeting of the transferor company, so they are encoded beside it.
Sections 915, 915A and 917A give no time and no step of their own, so nothing is added for them.

Files: `coa-proc-merger-court-wait.l4` (the rules) and `coa-proc-merger-court-wait-tests.l4` (26 traces and 15 assertions).
Source lines 12691-12784 of `ukpga-2006-46.txt`.
No existing module is edited.
The new module imports `coa-core`, `coa20-part26`, `coa20-part27-merger` and `coa-proc-merger`, and calls their functions as gates (the scheme record, `ss 902-918 Part 27 applies to a merger`, `ss 902-918 the scheme is a merger by absorption`, `s 917(1)`, `s 917(2)`, `s 917(3)`, and the calendar-month helpers `s 906(3) the date one month after` and `s 906(3) the date one month before`).
It does not call any rule of `coa-proc-merger.l4`.

### The seat of each rule

| rule | seat | what it does |
| --- | --- | --- |
| `s 917(2) the court's order that no meeting is required, not before the one-month wait` | s 917(2), (3), (3A), (3B), (4), (4C), (5) (src:12740-12759) | the court may not make the order before the first date that is one calendar month after the publication of the notice of receipt (SHANT, BREACH BY the court if it does); after that date the court MAY make the order if the other conditions are met and it is satisfied; no time after the wait |
| `ss 916(3A) and 918(2A) the first meeting of the transferor company, not before the one-month wait` | s 916(1)-(3A), s 918(1)-(2A) (src:12716-12719, 12765-12767) | the transferor company may not hold its first meeting before the first date that is one calendar month after the publication of the notice in respect of the transferee company (SHANT, BREACH BY the transferor company if it does); after that date it MAY hold the meeting; no time after the wait |

The helper functions are `ss 916(3A), 917(3A) and 918(2A) the day number of the earliest date` and `ss 916(3A), 917(3A) and 918(2A) the days from the publication to the earliest date`.
The gates `ss 915-918 section 917 applies to the scheme` (s 917(1), through the existing function) and `ss 915-918 section 918 applies to the scheme` (s 918(1): any merger by absorption) are Boolean.

### TIMELINE lines

- s 917: `-- TIMELINE: unit=calendar day; day 0=the day the registrar published the notice of receipt of the draft terms in respect of the last of the merging companies; counting="at least one month before the date of the court's order": counted backwards from the order, so the order may be dated on the first date that is one calendar month after day 0 or later (the date one month before it is not earlier than day 0, the test of the existing s 917(3A)); the number of days to that date is computed from the publication date; the court's order itself carries no time limit, so after the wait the step is silent`
- ss 916 and 918: `-- TIMELINE: unit=calendar day; day 0=the day the registrar published the notice of receipt of the draft terms in respect of the transferee company; counting="at least one month before the date of the first meeting of members, or any class of members, of the transferor company": counted backwards from the meeting, so the first meeting may be held on the first date that is one calendar month after day 0 or later (the same date arithmetic as s 917(3A) above); the number of days to that date is computed from the publication date; after the wait the step is silent`

What the one-month wait is counted from.
Section 917(3A) counts it backwards from the date of the court's order: the notice must have been published "at least one month before the date of the court's order" (src:12742).
Read forwards, the order cannot be dated before the first date that is one calendar month after the publication, so day 0 is the day of publication and the wait is a prohibition of that length on the court.
Sections 916(3A) and 918(2A) count the same month back from "the date of the first meeting of members ... of the transferor company" (src:12719, 12767), so there the prohibition falls on the meeting.
A prohibition of n days (`SHANT ... WITHIN n`) covers day 0 to day n inclusive, so the rules use the days to the earliest date minus one.
The earliest date is the first date whose date one calendar month before is not earlier than the publication date, which is the test of the existing `s 917(3A) subsection (3A) is satisfied` run forwards; two assertions on each side of the boundary for a 15 January and a 31 January publication tie the two together.

### Forks

- s 917(3A) "in respect of all the merging companies": day 0 is the publication date for the last of the merging companies, the latest of the dates | each company's date counted separately.
- s 917(3A) "at least one month before the date of the court's order": the earliest date is the first date whose date one calendar month before is not earlier than the publication date, so a notice published on 31 January 2026 allows an order from 1 March 2026 and not on 28 February (29 days, not 28) | the month ends on the last day of a shorter month, or a month is thirty days.
- s 917(3A) an order dated before the wait: shown as the court's breach so that a trace shows the route lost; the Act does not call it a breach: the first condition is not complied with, the court cannot be satisfied, and the meetings required by s 907(1) are still required | no one's breach, the exemption is merely unavailable.
- s 917(3B)(b) the website route: the same wait and the same day 0, taken from the Gazette notice mentioned in s 906A(4); the rest of (3B) (the conditions of s 906A(2) to (4) and the availability of the draft terms) is an input read after the wait | a separate rule for the website route.
- s 917(4), (4C), (5): the answers are inputs read at the date of the order, because they speak of "the period beginning one month before, and ending on" the order; an answer of NOTHING is treated as not met, so the court's power is not open until the answer is known | an unknown answer leaves the power open.
- s 917(2) "if the court is satisfied": a MAY of the court with no time limit | a duty of the court to make the order once the conditions are met.
- ss 916(3A) and 918(2A): one rule serves both sections, gated by s 918(1) (any merger by absorption), because s 916(1) (90% or more, not all) is a narrower case with the same clock and s 917 (all held) has its own anchor | a rule for each section.
- ss 916(3A) and 918(2A) the gate: the rule runs only where the transferee company relies on s 916(2) or s 918(1) (the scheme record's answer of either is JUST TRUE), because the month is a condition of that exemption (src:12765, 12767) and not a duty on the transferor company; the other reading, the first draft's, binds every merger by absorption, and the independent review changed it.
- ss 916(3A) and 918(2A) a meeting held before the wait: a closed route, FULFILLED: the first condition of the exemption is not met, the transferee company's meeting is required (s 907(1)), and the transferor company has done no wrong; the first draft showed it as the transferor company's breach.
- ss 916(3A) and 918(2A) "the first meeting": the earliest of the meetings of the transferor company (or of any of them) summoned to agree to the scheme | each class meeting counted separately.
- ss 916(3B)(b) and 918(2B)(b) the website route: the same wait, taken from the Gazette notice mentioned in s 906A(4) | a separate rule.

### What the text leaves silent

- The registrar's time to publish the notice of receipt: s 917 does not give one, and s 906(3) times it from a meeting, which may never be summoned under the exemption (src:12580, 12742).
  The publication is therefore day 0 of the rules and not a step in them.
- The court's time to make the order after the wait: s 917(2) says "if the court is satisfied" and gives no time (src:12740), so the step after the wait is a MAY with no clock and a trace that waits ends RESIDUAL.
- The transferor company's time to hold its first meeting after the wait (ss 916 and 918): no time is given, so the same.
- What happens when a later condition fails after the wait: the text says only that the meeting is not excused, so the rule ends FULFILLED with no step; the meetings required by s 907(1) are in `coa-proc-merger.l4`.

### Differences from the existing DEONTIC

There is no existing DEONTIC for the wait.
The one-month wait of s 917(3A) is a condition in the Boolean module, and `coa-proc-merger.l4` takes the answers of ss 916 to 918 as inputs and does not encode their clocks (its own comment at the end of the s 911 rule says so).
So the comparison is with the Boolean module and with the comments of the existing modules.

- The Boolean function `s 917(3A) subsection (3A) is satisfied` and `s 917(3B)` in `coa20-part27-merger.l4` run the one-month test against `date of the court's order` (lines 1289-1317), which agrees with src:12742 and src:12745.
  Their comments and one @ref title still say "the first meeting of members of the transferor company" (lines 1285-1288, the quotation at 1295 and the one at 1315), which is the wording of s 916(3A) and s 918(2A), not of s 917(3A).
  The code is right and the comments are stale; the module was not edited.
- `coa-proc-merger.l4` line 257 states the anchor of s 917(3A) correctly ("the date of the court's order").
- Behaviour that this module adds: a court's order dated before the earliest date, and a first meeting of the transferor company held before it, are shown as a BREACH on a trace; the Boolean module can only answer `JUST FALSE` for the first condition at a given pair of dates.
- The existing s 911 rule counts the availability of documents from one month before the first meeting through its date as a duty of the company.
  This module does not repeat that count for the court's order (see "What is not encoded").

### Verification

- Both files run with `l4 run` from inside the folder, with `JL4_LIBRARY_PATH` unset, on the unstable binary `l4-unstable-20261125-a50cbd0-darwin-arm64` and on the stable line the stable build 112: no `DiagnosticSeverity_Error` and no warning on either, and all 15 assertions satisfied on both.
- The traces were verified with `expect_check.py`: 26 of 26 match on the unstable binary.
  On the stable line 20 of 26 match; the other six are listed below.
- Two sensitivity checks on scratch copies (deleted afterwards): removing the "minus one" from the `WITHIN` of both rules flips four traces (the order on day 31, the website order on day 31, the 31 January order on day 29 and the meeting on day 31 each read BREACH); removing the extra day in the end-of-month case flips the 28 February trace and fails two assertions (the day counts for 31 January 2026 and 31 January 2028).
- `srcrefs.py check --strict` on the module: 22 quotation lines, 6 locators, 0 problems.

### Closed routes (not breaches)

Convention for all the procedure units (assumed, not ruled): `BREACH` is kept only for a duty or a prohibition that the text lays on a named party.
A power that lapses unused, a condition that is not met, a vote that fails and a route that has closed end `FULFILLED`, with the reason (what was lost, and the statute line) in a comment beside the LEST.
In this unit the ss 916(3A) and 918(2A) rule follows it: an early first meeting of the transferor company is the exemption of the transferee company lost, FULFILLED, and three traces moved from BREACH to FULFILLED after the independent review (a meeting on day 0, a meeting on day 30, and a meeting on day 10 where the transferee relies on neither section).
One trace was added, for a transferee that relies on s 918(1) with a first meeting on day 10, and the first-meeting traces now use a fixture in which the transferee relies on s 916(2).
The s 917(3A) rule keeps `BREACH BY the court` for an order made too early, by exception: the court may make the order only if it is "satisfied that the following conditions have been complied with" (src:12740), so an order made too early is a limit on the power of the court and a step that binds the court, not a lapsed power of a party; this is the reading the review accepted (UK-merger-court-wait-2).

### Where the readings differ: month-end counting

The one place in this unit where the English month-counting readings differ is the trace of a notice published on 31 January 2026 and a court's order on 28 February 2026 (`publication: 31 January 2026`, the order on day 28): the module treats the month as not yet run (31 January plus one calendar month clamps to 28 February, and the date one month before 28 February is 28 January, earlier than 31 January), so the order is a BREACH BY the court.
Under the corresponding-date rule (Dodds v Walker [1981] 1 WLR 1027) a month that has no corresponding date ends on its last day, so 31 January to 28 February is one month and the order would be in time; that is the other reading of the module's own fork, and this trace is the only one that blesses the stricter reading.

### READS-DIFFERENTLY-ON-MAIN

Six traces, all the same shape: an event arrives after the prohibition's window has run out, and the MAY that follows should take it.
Unstable reads FULFILLED; main leaves the MAY open and reads RESIDUAL.
- s 917(3A): the court's order on day 40 (route A, all conditions met).
- s 917(3A): the court's order on day 31, exactly one month after the publication.
- s 917(3B)(b): the court's order on day 31, the website route.
- s 917(3A): the notice published on 31 January 2026 and the court's order on day 29.
- s 918(2A): the first meeting of the transferor company on day 40.
- s 918(2A): the first meeting of the transferor company on day 31.

The BREACH traces, the traces that wait with no event, and the traces whose gate fails read the same on both.

### What is not encoded

- ss 915, 915A and 917A: they give no time and no step; they are gates, already called in `coa-proc-merger.l4`.
- The availability of the documents and of copies throughout the month before the order (s 917(4A), (4B), (4C), (4D)) and the 5% requisition (s 917(5)), and the corresponding conditions of ss 916 and 918: they are conditions of the exemption, not duties of anyone ("were able", "no such requirement was made"), so they enter as answers read at the date of the order (s 917) or through the scheme record (ss 916, 918).
  The same availability as a duty of the company, counted to the first meeting, is `s 911(1)` in `coa-proc-merger.l4`.
- The registrar's duty to publish (s 906(2)): in `coa-proc-merger.l4`, where with no meeting summoned it has no time.
- The content of the draft terms and the reports, and ss 918A onwards: outside the unit.
- Several merging companies with different publication dates: one date is taken, the latest (fork above); the day count for each company is not separate.
