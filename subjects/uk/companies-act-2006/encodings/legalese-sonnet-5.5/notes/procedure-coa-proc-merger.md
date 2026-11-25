## Procedure layer: mergers of public companies, from the draft terms to the inspection of documents (ss 902 to 918)

The procedure that Companies Act 2006 Part 27, Chapter 2 (ss 902 to 918) lays down for a merger of public companies, written as regulative rules over the Boolean encoding in `coa20-part27-merger.l4`.

Files: `coa-proc-merger.l4` (the rules) and `coa-proc-merger-tests.l4` (49 traces and 20 assertions).
Source lines 12530-12784 of `ukpga-2006-46.txt`.
No existing module is edited; the new module imports `coa-core`, `coa20-part26` and `coa20-part27-merger` and calls their functions as gates.
This is the merger procedure only: a division (Chapter 3) is outside it, so the answer for a division is passed to `s 902(1)` as `JUST FALSE`.

### The seat of each rule

| rule | seat | what it does |
| --- | --- | --- |
| `s 905(1) the directors' duty to draw up the draft terms and adopt them` | s 905(1) (src:12561) | the directors of each merging company must draw up and adopt the draft terms; no clock |
| `s 906(1) the directors' duty to deliver the draft terms or the website notice to the registrar` | s 906(1), s 906A(4) (src:12578, 12588) | the directors deliver a copy of the draft terms, or, for a company that relies on its website, a notice giving the website's details; no clock |
| `s 906(3) the registrar's duty to publish the notice at least one month before the meeting` | s 906(2)-(3), s 906A(5) (src:12579-12580, 12589) | the registrar publishes in the Gazette on or before the date one calendar month before the first meeting; day 0 is the day the registrar receives the copy (or the website notice); a copy that arrives after the last day is an immediate BREACH BY the directors |
| `s 906(2) the registrar's duty to publish the notice where no meeting is summoned` | s 906(2) (src:12579) | the same duty with no meeting date to count from, so no clock |
| `s 906A(6) the company's duty to keep the draft terms on its website throughout the period` | s 906A(6) (src:12590) | for a company that relies on its website: the terms are on the website on the first day of the period (MUST WITHIN 0) and are not taken off through the date of the meeting (SHANT) |
| `s 907(1) the company's duty to have the scheme approved at a meeting of its members` | s 907(1), (2) (src:12592-12593) | the meeting is held and the vote taken (MUST, no clock); the majority is counted by the existing `s 907(1)` function from the numbers in each class; a failed vote is BREACH BY the company |
| `s 908(1) the directors' duty to draw up and adopt the explanatory report` | s 908(1), (3) (src:12595, 12604) | gated by `s 908(3)`; no clock |
| `s 909(1) the company's duty to have an expert's report drawn up` | s 909(1)-(3), (7) (src:12606-12609, 12623) | gated by `s 909(7)`; with the court's approval of a joint expert one single report, otherwise a separate report for the company; no clock |
| `s 909(3) the court's power to approve the appointment of a joint expert` | s 909(3) (src:12608) | a MAY of the court, gated on the joint application of all the merging companies; no clock |
| `s 910(1A) the directors' duty to prepare a supplementary accounting statement` | s 910(1), (1A), (2)(a) (src:12625-12630) | gated by `s 910(1)` (the dates), `s 910(6)` and the half-yearly report; the statement's balance sheet must be made up as at a date not earlier than three calendar months before the draft terms were adopted, else BREACH BY the directors; no clock for preparing it |
| `s 911(1) the company's duty to keep the documents open to inspection throughout the period` | s 911(1), (2) (src:12637-12643) | gated by `s 911(7)`; the documents are open on the first day of the period (MUST WITHIN 0) and are not withdrawn through the date of the meeting (SHANT) |

The gates are Boolean helpers in the same module that call the existing functions: `ss 902-918 Part 27 applies to a merger` (calls `s 902(1)`, `s 902(3)`, `s 904(1)`, `s 904(1)(a)`, `s 904(1)(b)`), `section 908 requires the explanatory report` (calls `s 908(3)`, `s 915(4)`, `s 915(1)`, `s 915A(2)`, `s 915A(1)`), the same for s 909 (`s 909(7)`), s 910 (`s 910(6)`), s 911 (`s 911(7)`) and `section 907 requires a meeting of the members` (calls `s 907(2)` and `s 917A(1)`).
The answers of ss 916, 917 and 918 (each is a `MAYBE BOOLEAN` input of the scheme record, given for the company the duty is traced for), of `s 915A(3)` and `s 915A(4)` and of `s 918A(1)` are inputs, not calls.
The reason is the signatures: `s 916(2)`, `s 917(2)` and `s 918(1)` each take the answers of their own four conditions (five `MAYBE BOOLEAN`, with `s 916(1)` or `s 917(1)` or the merger-by-absorption answer) and a Boolean for the court's satisfaction, and each condition's function in turn asks for dates and the availability of documents; calling them would put about a dozen more facts in every trace for a result the Boolean module already computes.
`s 917A(1)` takes one Boolean and is called.
This is the one place where the brief's "exemptions of ss 915-918 as gates" is met by input and not by call: ss 915 and 915A and 917A are called, ss 916, 917 and 918 are answered by the trace.

### TIMELINE lines

- `s 905(1) the directors' duty to draw up the draft terms and adopt them`: `TIMELINE: unit=none; day 0=not applicable; counting=silent (s 905(1) gives no time for drawing up and adopting the draft terms, so no clock runs: the duty stays open until the trace shows it done)`
- `s 906(1) the directors' duty to deliver the draft terms or the website notice to the registrar`: `TIMELINE: unit=none; day 0=not applicable; counting=silent (neither s 906(1) nor s 906A(4) gives the directors a time for delivery; the only time in the Act is the registrar's: the notice is published at least one month before the meeting, see the rule for s 906(3) below, so a late delivery shows there)`
- `s 906(3) the registrar's duty to publish the notice at least one month before the meeting`: `TIMELINE: unit=calendar day; day 0=the day the registrar receives the copy of the draft terms (or the notice giving details of the website); counting="at least one month before the date of any meeting": the last day is the calendar date one month before the first meeting (the existing `s 906(3) the date one month before`, which clamps a day that the earlier month lacks), and the number of days to it is computed from the two dates`
- `s 906(2) the registrar's duty to publish the notice where no meeting is summoned`: `TIMELINE: unit=none; day 0=not applicable; counting=silent (s 906(3) measures the month from "the date of any meeting of that company summoned for the purpose of approving the scheme"; with no meeting summoned there is no date, so s 906(2) alone applies and gives no time. Section 917(3A) measures the same month from the date of the court's order, as a condition of that exemption, and is read in the Boolean module)`
- `s 906A(6) the company's duty to keep the draft terms on its website throughout the period`: `TIMELINE: unit=calendar day; day 0=the date one month before the first meeting (the first day of the period); counting="throughout the period beginning one month before, and ending on, the date of any such meeting": both ends are in the period, so the last day is the date of the meeting and the number of days to it is computed from the two dates`
- `s 907(1) the company's duty to have the scheme approved at a meeting of its members`: `TIMELINE: unit=none; day 0=not applicable; counting=silent (s 907(1) says "at a meeting" and gives no time for the approval beyond the meeting itself, so no clock runs: the duty stays open until the trace shows the meeting held; the date of the meeting is the anchor of the other rules above and below)`
- `s 908(1) the directors' duty to draw up and adopt the explanatory report`: `TIMELINE: unit=none; day 0=not applicable; counting=silent (s 908 gives no time for the report; section 911(3)(b) makes it a document the members must be able to inspect from one month before the first meeting, which is a limit on the availability of the document and is not read here as a time for drawing it up)`
- `s 909(1) the company's duty to have an expert's report drawn up`: `TIMELINE: unit=none; day 0=not applicable; counting=silent (s 909 gives no time for the report; the same limit through s 911(3)(c) as for the directors' report above)`
- `s 909(3) the court's power to approve the appointment of a joint expert`: `TIMELINE: unit=none; day 0=not applicable; counting=silent (s 909(3) gives the court no time, so no clock runs: the power stays open until the trace shows it used)`
- `s 910(1A) the directors' duty to prepare a supplementary accounting statement`: `TIMELINE: unit=none; day 0=not applicable; counting=silent (s 910 gives no time for preparing the statement; the date limit of s 910(2)(a) is a limit on the date AS AT WHICH its balance sheet is made up, "not more than three months before the draft terms were adopted", and is checked on the date input; section 911(3)(e) makes the statement a document to be open to inspection from one month before the first meeting)`
- `s 911(1) the company's duty to keep the documents open to inspection throughout the period`: `TIMELINE: unit=calendar day; day 0=the date one month before the first meeting (the first day of the period); counting="beginning one month before, and ending on, the date of the first meeting": both ends are in the period, so the last day is the date of the meeting and the number of days to it is computed from the two dates`

Every period in this procedure is in calendar days and is computed from dates: the registrar's last day is `s 906(3) the date one month before` the meeting (the existing helper, which clamps a day the earlier month lacks), and the two windows run from that date to the date of the meeting.
With the receipt on 1 February 2026 and the meeting on 2 April 2026 the last day is day 29 and the window is 31 days.

### Forks

All are in comment lines in `coa-proc-merger.l4`; the ones that change a result are:

- ss 908, 909, 910, 911: an exclusion answered `NOTHING` (not known) leaves the duty standing; the other reading is that no duty arises.
- ss 916 to 918: the four answers are given for the company the duty is traced for, so the scheme record is built per company.
- "the first meeting": the date input is the earliest of the meetings summoned; the other reading counts each class meeting separately.
- s 902(1)(b)(ii): a division is outside this module.
- s 905(1): one duty for each merging company's directors, not one joint duty.
- s 906A(1): whether a company relies on the website route is an input chosen at the start; the other reading makes the answer of `s 906A(1)` the gate, which is not known until the meeting.
- s 906(3) "at least one month before": the last day is the date one calendar month before the meeting and a notice on that date is in time; the other reading is thirty days.
- s 906(3), copy delivered after the last day: the failure is BREACH BY the directors at once on day 0; the other reading puts it on the registrar.
- s 906A(6) and s 911(1): the period's availability is a duty (open on day 0, not withdrawn through the meeting day), so a withdrawal shows as BREACH; the other reading is that s 906A(6) is only a condition of the exemption and s 911(1) is answered by the Boolean `s 911(2)`.
- s 907(1): the section names no bearer; the seat is the merging company, and a vote that misses the majority is BREACH BY the company; the other reading is that a failed vote is no one's breach.
- s 908(1), s 909(1): no clock; the other reading is that ss 911(3)(b) and (c) make the reports due one month before the first meeting.
- s 909(1): the merging company is the bearer, since the text names none; the other reading is the expert or the directors.
- s 909(3): the court's approval is an input that selects which report is owed.
- s 910(2)(a): a balance sheet dated exactly three calendar months before the adoption is in time, an earlier one is a breach, a later one (even after the adoption) is not.
- s 910(1)(a) and (b): the first-meeting date is a `MAYBE DATE`, `NOTHING` meaning no meeting is required, as in the existing function.
- s 911(1)(a) and s 911A: one rule, since section 911A uses the same period.

### What the text leaves silent

- s 905(1), s 906(1), s 906A(4): no time for adopting the draft terms or delivering them to the registrar.
- s 906(2) where no meeting is summoned: no date for the month to run from (section 917(3A) counts it from the court's order, as a condition of that exemption, not as a duty).
- s 907(1): no time for the meeting beyond the meeting itself.
- ss 908, 909, 910(1A): no time for the directors' report, the expert's report or the supplementary accounting statement; only s 911(3) makes them documents to be open to inspection from one month before the first meeting.
- s 909(3): no time for the court.
- s 906A(6) and s 911(2) where no meeting is required (ss 916 to 918): no meeting date to run to; the two rules take the first meeting's date as given and do not look at whether a meeting is required, and the same one-month availability counted from other dates in ss 916(3B), (4A)-(4C), 917(3B), (4A)-(4C) and 918(2B), (3A)-(3C) is a condition of those exemptions, read in the Boolean module.

### Differences from the existing DEONTIC

None. `coa20-part27-merger.l4` is Boolean only (no `DEONTIC` in it), and no other module in the folder has a DEONTIC for ss 902 to 918; the DEONTICs of `coa20-part26.l4` are for ss 895 to 901.
Where this layer differs from the Boolean answers, it is because a Boolean answer is "was it complied with" and this layer is "what is owed and by when": for example, the Boolean `s 906(3)` answers `NOTHING` when no meeting is summoned, and the rule for `s 906(2)` here says the duty to publish still stands with no clock.

### Verification

Both binaries read every module with no `DiagnosticSeverity_Error` and no `DiagnosticSeverity_Warning`; the `[Import Resolution]` warning about the embedded `prelude` and `daydate` copies appears for every module in the folder and is not from these files.
Unstable (`l4-unstable-20261125-a50cbd0`): 49 of 49 traces match their `-- EXPECT` line and 20 of 20 assertions are satisfied.
Stable line (`~/.cache/l4-main/112/l4`): the same, 49 of 49 and 20 of 20.
Source quotations: `srcrefs.py check --refs` reports 57 `src:` lines, 15 locators and 0 problems.
Two mutated copies were run and deleted: one changing the "last day" test of s 906(3) and removing the negation in the s 908 gate (4 traces mismatch), one changing the s 910(2)(a) comparison and the length of the two windows (5 traces mismatch).

### READS-DIFFERENTLY-ON-MAIN

None: no trace reads a different class on the stable line.
One difference in what the stable line accepts, which fails loudly (`check/unknown-identifier`) and is not a trace difference: a function call written as the act of a `MUST` (`MUST (f x)`) is read as an unknown identifier on the stable line; the unstable binary accepts it.
The module avoids it by writing the choice between the two routes of section 906A as an `IF` in each rule.
A function call as a clock (`WITHIN (f x)`) is accepted by both.

### What is not encoded

- s 905(2) and (3), s 908(2), s 909(4) to (6), s 910(2)(b) to (5): the content of the draft terms and of the reports, the expert's qualifications and rights, and the form of the statement; the Boolean module asks them.
- s 906A(2) and (3), s 911A and s 911(3) to (6): the conditions of publication on a website and the list of documents; the Boolean module asks them, and their dates are the periods used here.
- ss 916 to 918: the conditions of the exemptions (one-month notices, the 5% requisition) stay in the Boolean module and enter as the four answers of the scheme record; the registrar's duty to publish notice at least one month before the court's order (s 917(3A)) is a condition of that exemption, not a duty here.
- s 911B (the directors' report to the meeting), s 912 (articles of a new transferee company), ss 913 and 914 (what the scheme must provide): not in this module.
- s 918A (agreement to dispense with the reports) is outside the range; its answer is an input.
