## Procedure layer: compulsory acquisition after a takeover offer, the squeeze-out, the sell-out and the court application (ss 979 to 986)

The procedure that Companies Act 2006 ss 979 to 986 lays down once a takeover offer has been accepted widely enough: the offeror's notice to a holder who has not accepted (the squeeze-out, ss 979 to 982), the holder's right to require the offeror to buy (the sell-out, ss 983 to 985), and the court application of s 986.
It is written as regulative rules over the Boolean encoding in `coa21-ch3-squeeze-out.l4` and `coa21-ch3-sell-out.l4`.

Files: `coa-proc-takeover-notices.l4` (the rules) and `coa-proc-takeover-notices-tests.l4` (46 traces and 14 assertions).
Source lines 13612-13799 of `ukpga-2006-46.txt` (s 986 ends at line 13799; s 987 starts at 13800).
No existing module is edited; the new module imports `coa-core`, `coa21-ch3-squeeze-out` and `coa21-ch3-sell-out` and calls their functions as gates.

### The seat of each rule

| rule | seat | what it does |
| --- | --- | --- |
| `ss 979-986 the offeror is entitled to give notice to the holder of the shares` (Boolean helper) | s 979(2) and (4) (src:13612-13622) | the gate: calls the existing `s 979(2)` or `s 979(4)` function, according to whether the offer relates to shares of different classes |
| `ss 979-986 the last day on which a notice may be given` (helper that returns a date, missing only if the Schedule 1C answer were unknown) | s 980(2)-(3) (src:13650-13653) | calls the existing `s 980(2)` function with the offer's two dates and the Schedule 1C answer |
| `ss 979-986 section 979 allows a notice given on the day` (Boolean helper) | ss 979, 980(2) (src:13648-13653) | the entitlement gate and the in-time test together |
| `ss 979-986 section 981(6) has effect on the day` (Boolean helper) | s 981(6), s 986(2) (src:13679, 13777-13778) | six weeks from the notice (the existing `s 981(3)(a)` function), moved to the day an application is disposed of where one is pending at the end of the six weeks (the existing `s 986(2)` function); the test is AT LEAST, so any later day also passes and starts its own WITHIN 0, and the caller starts the trace on the first day on which the duty arises |
| `s 980(2) the offeror's power to give notice under section 979` | s 980(2) (src:13650-13652) | a MAY of the offeror, gated by s 979(2) or (4); on the lapse of the power a bar (SHANT) opens, so a late notice is a breach |
| `s 980(4) the offeror's duty to send the company a copy of the first notice and a statutory declaration` | s 980(4), (6)(a) (src:13654-13661) | two MUSTs side by side (RAND), each WITHIN 0 of the first notice; a miss is the breach and the offence of s 980(6)(a) |
| `s 980(6)(b) the offeror's duty not to make a false declaration` | s 980(6)(b) (src:13658-13660) | a prohibition (SHANT) with no clock |
| `s 981(3) the shareholder's six weeks to indicate a choice of consideration` | s 981(3)-(4) (src:13670-13674) | a MAY of the holder, gated on the terms giving a choice, WITHIN 42 days of the notice |
| `s 986(2) the shareholder's six weeks to apply to the court` | s 986(1)-(2) (src:13774-13778) | a MAY of the holder, gated by the existing `s 986(1)` function, WITHIN 42 days of the notice |
| `s 981(6) the offeror's duty at the end of six weeks` | s 981(6), s 986(1)-(2) (src:13679-13682, 13774-13778) | two MUSTs side by side (RAND), each WITHIN 0 of the day s 981(6) has effect; gated on a notice s 979 and s 980(2) allow, on the six weeks having run, on no pending application, and on no court order that the offeror is not bound |
| `s 981(9) the company's duty to hold the consideration on trust` | s 981(9) (src:13687-13688) | a MUST of the company, gated by the existing `s 981(9)` function; no clock |
| `s 982(2) the company's duty to pay into a separate bank account` | s 982(1)-(3) (src:13690-13696) | a MUST of the company once consideration has been paid to it; no clock |
| `s 982(4) the company's duty to pay the consideration into court` | s 982(4)-(6) (src:13697-13704) | a MUST of the company, gated by the existing `s 982(4)` and `s 982(5)` functions (the person cannot be found, enquiries, twelve years or winding up, not Scotland); no clock |
| `s 984(2) the shareholder's three months to require the offeror to acquire the shares` | ss 983, 984(1)-(2), 985(2) (src:13716-13719, 13743-13746, 13759-13760) | a MAY of the holder, gated by the answer of the existing `s 983(2)`, `(3)` or `(4)` function, WITHIN the three months of the existing `s 984(2)` function; the next step is the offeror's duty to acquire (s 985(2)), with no clock |
| `s 984(3) the offeror's duty to give the shareholder notice of his rights` | s 984(3)-(5) (src:13747-13751) | a MUST of the offeror WITHIN one month of the end of the acceptance period, gated by the s 983 answer and the existing `s 984(4)` function; a miss is the breach and the offence of s 984(5) |
| `s 984(5) the officer's duty not to be in default in the offeror company's failure` | s 984(5) (src:13752-13753) | a prohibition on an officer in default, gated by the existing `s 984(5)` function; no clock |

The rules are separate, not chained by HENCE (except the s 985(2) step after the holder's requirement), because each later step needs a fact the earlier one does not carry: the date of the notice, the day an application is disposed of, whether the holder has accepted.
Each rule has its own day 0, named on its TIMELINE line.
The offences are encoded as the breach of the duty the Act makes an offence (s 980(4), s 984(3)) or as a prohibition on the event (s 980(6)(b), s 984(5)), and they are separate rules from the clocks.

### TIMELINE lines

- `s 980(2) the offeror's power to give notice under section 979`: `TIMELINE: unit=calendar day; day 0=the date of the offer; counting="the period of three months beginning with the day after the last day on which the offer can be accepted", or "the period of six months beginning with the date of the offer, where that period ends earlier and the offer is one to which subsection (3) below applies"` (the number of days is computed from the offer's two dates by the existing s 980(2) function; a period "beginning with" a date ends the day before the corresponding date; in the tests, an offer made on 1 January and open until 30 April gives 180 days or, where Schedule 1C governs, 211).
- `s 980(4) the offeror's duty to send the company a copy of the first notice and a statutory declaration`: `TIMELINE: unit=calendar day; day 0=the day the offeror first gives a notice under section 979 in relation to the offer; counting="At the time when the offeror first gives a notice"` (WITHIN 0).
- `s 980(6)(b) the offeror's duty not to make a false declaration`: `TIMELINE: unit=none; day 0=not applicable; counting=silent`.
- `s 981(3) the shareholder's six weeks to indicate a choice of consideration`: `TIMELINE: unit=calendar day; day 0=the date of the notice; counting="within six weeks from the date of the notice"` (42 days, from the existing `s 981(3)(a)` function).
- `s 986(2) the shareholder's six weeks to apply to the court`: `TIMELINE: unit=calendar day; day 0=the date on which the notice was given; counting="within six weeks from the date on which the notice referred to in that subsection was given"` (42 days, from the existing `s 986(2)` function).
- `s 981(6) the offeror's duty at the end of six weeks`: `TIMELINE: unit=calendar day; day 0=the day section 981(6) has effect: the end of six weeks from the date of the notice (the date of the notice plus 42 days), or, where an application to the court under s 986(1) is pending at the end of the six weeks, the day the application is disposed of; counting="At the end of six weeks from the date of the notice ... must immediately" and "does not have effect until the application has been disposed of"` (WITHIN 0).
- `s 981(9) the company's duty to hold the consideration on trust`: `TIMELINE: unit=none; day 0=the day the company receives the consideration under s 981(6)(b); counting=silent`.
- `s 982(2) the company's duty to pay into a separate bank account`: `TIMELINE: unit=none; day 0=the day the offeror pays or transfers consideration to the company under s 981(6); counting=silent`.
- `s 982(4) the company's duty to pay the consideration into court`: `TIMELINE: unit=none; day 0=the day the gate is tested; counting=silent` for the duty (the twelve years of s 982(5)(b) are a condition tested from the day the consideration was received, not a deadline).
- `s 984(2) the shareholder's three months to require the offeror to acquire the shares`: `TIMELINE: unit=calendar day; day 0=the end of the period within which the offer can be accepted; counting="not exercisable after the end of the period of three months from (a) the end of the period within which the offer can be accepted, or (b) if later, the date of the notice that must be given under subsection (3)"` (from the existing `s 984(2)` function; the offeror's duty to acquire that follows has no clock).
- `s 984(3) the offeror's duty to give the shareholder notice of his rights`: `TIMELINE: unit=calendar day; day 0=the end of the period within which the offer can be accepted; counting="Within one month of the time specified"` (the time specified is read as the end of the acceptance period; the other reading, one month from the day the conditions of s 983 are first met, may be earlier, src:13719 and 13750; computed by the existing `s 984(3)` function; 30 days in the tests, for an acceptance period ending on 30 April).
- `s 984(5) the officer's duty not to be in default in the offeror company's failure`: `TIMELINE: unit=none; day 0=not applicable; counting=silent`.

### Forks

The rules carry these FORK lines, each with the answer taken and the other reading (the full lines are in the module):

- s 979(2) and (4) "he may give notice": the entitlement is the existing function's answer JUST TRUE; a shortfall is not a bar.
- s 980(2) "No notice may be given ... after the end of": a late notice is a breach of a bar opened by the lapse of the power (the Act makes it of no effect and no offence); the other reading is a simple lapse.
- s 980(2) day 0: the date of the offer; the other reading is the last day on which the offer can be accepted.
- s 980(3) "governed by rules under section 943(1)": a Boolean input of the offer, because Schedule 1C is not in the sources.
- s 980(4) "At the time when": the same day as the first notice.
- s 980(6)(a) and (7): a miss is the breach of the duty; the defence of reasonable steps is a matter for the charge.
- s 981(3)(a), s 986(2) "within six weeks from the date": day 42 is the last day; the other reading is day 41.
- s 981(3)(b): a holder who does not choose in the six weeks takes the consideration the notice names; the lapse is not a breach.
- s 986(2) a late application: the lapse is FULFILLED; whether the court may entertain a late application is not in the text.
- s 981(6) "At the end of six weeks", "immediately": the date of the notice plus 42 days, and the same day.
- s 981(6)(a) and (b): two duties side by side, each with its own breach.
- s 986(2) "does not have effect until the application has been disposed of": the duty arises on the day of disposal, unless the court has ordered that the offeror is not bound.
- s 982(4) "twelve years have elapsed": twelve years is `add years` 12, and the duty arises on that day or after.
- s 984(2) "three months from": the later of the two dates, and the last day is the corresponding date three months on.
- s 984(2) day 0 and a late requirement: the end of the acceptance period; a requirement before it is put on day 0; the lapse of the right is FULFILLED.
- s 985(2): the offeror's duty to acquire follows the holder's requirement and has no clock; the court's power to fix the terms (s 986(3)) is not encoded.
- s 983 gate: the answer of the existing s 983(2), (3) or (4) function is an input, so the share-count inputs of those functions are not repeated.
- s 984(3) "Within one month of": one month after the end of the acceptance period; an earlier notice (the last sentence of s 984(3) allows one) is put on day 0; the other reading is one month from the day the conditions of s 983 are first met, which may be earlier (src:13719 "at any time before the end of the period"), the month then running on both sides of the end of the period.
- s 980(2) the entitlement date: the entitlement is tested once, on the position's own date, and the power runs from the date of the offer, so a notice given before that date is not caught by the gate; the other reading tests the entitlement on the day of each notice, as the s 981(6) rule does.
- s 984(4): the duty arises unless the existing function answers JUST FALSE (the offeror has given a s 979 notice).
- s 984(5) and (6): a miss is the breach and the offence of the offeror; the officer has a prohibition of his own; the defence of reasonable steps is a matter for the charge.

### What the text leaves silent (no clock encoded)

- Any time for the company to hold the consideration on trust (s 981(9)), to pay into a separate account (s 982(2)), or to pay into court (s 982(4)).
- Any time for the offeror to acquire after the holder requires it (s 985(2)).
- Any time for a shareholder to give the offeror notice of an application (s 986(6)) or for the offeror to pass a copy on (s 986(7), (8)): not encoded.
- Whether the date of a notice counts in the six weeks, and whether "within one month of" looks forward or both ways.
- What "at the time when the offeror first gives a notice" allows (s 980(4)); the rule takes the same day.
- The date of the court's disposal of an application, and whether the court's order is made on that day.
- The prescribed manner of the notice (s 980(1)), the prescribed form of the declaration (s 980(4)(b)) and the fine's amount (s 980(8), s 984(7)): outside the rules, and the penalties stay the existing `s 980(8)` and `s 984(7)` functions.
- Whether Schedule 1C governs the acceptance time: an input.

### Which binary verified the traces

Both, from inside the encoding folder with `JL4_LIBRARY_PATH` unset: the unstable build `l4-unstable-20261125-a50cbd0` and the stable line, `~/.cache/l4-main/112/l4`.
On each, the module and the test module print no error and no warning other than the import-resolution warning that every module prints in this environment (an installed copy of the prelude and `daydate` in the XDG data directory is shadowed by the embedded one); all 14 assertions are satisfied.
Under `expect_check.py`, all 46 traces match their `-- EXPECT` line on unstable; 44 match on main (the two that do not are below).
The count is over the aim of 40 because each time-limited rule has an in-time, a last-day, a late-act and a gate trace where the text gives them; the late acts of s 981(3), s 986(2) and s 984(2) are real events on days 43, 43 and 92, not waits.
`srcrefs.py check --refs` reports 86 quoted source lines, 19 locators, no problem.
The expected outcomes and the day counts (180, 211, 42, 30, 91, 122) were written from the text before the first run.

Sensitivity: two scratch copies of the module, each with one change, were run against the test module on unstable and then deleted.
Counting the s 980(2) clock from the close of the offer instead of the offer's date turned two traces (the notice on the last day and the one under Schedule 1C) into BREACH.
Dropping the court-order gate of s 981(6) turned the trace for a court order into BREACH.

### READS-DIFFERENTLY-ON-MAIN

Two traces differ in class; the list is at the end of `coa-proc-takeover-notices-tests.l4`.
This note states what each binary printed, not why.

- The notice given on day 181 under `s 980(2) the offeror's power to give notice under section 979` (line 87) is BREACH on unstable and FULFILLED on main.
- The holder's requirement on day 91 followed by the offeror's acquisition on day 95 under `s 984(2) the shareholder's three months to require the offeror to acquire the shares` (line 268) is FULFILLED on unstable and RESIDUAL on main (main prints the offeror's duty to acquire still open).
  Two scratch traces, since deleted, matched on both binaries: the requirement on day 50 with the acquisition on day 95, and the requirement and the acquisition both on day 91.
  The traces with the requirement on day 110 and the acquisition on day 115 match on both.

Four open obligations print differently with the same class (RESIDUAL): line 97 (open s 980(2) power), line 131 (open s 980(6)(b) prohibition), line 301 (open s 984(3) duty), line 321 (open s 984(5) prohibition); unstable puts parentheses round the LEST with its BREACH, main does not.
The three late-act traces (the choice on day 43, the application on day 43, the requirement on day 92) are FULFILLED on both.

### Differences from the existing DEONTIC

The existing DEONTICs are `s 981(6) the offeror's duty to send a copy of the notice and pay the company` at `coa21-ch3-squeeze-out.l4:637` and `s 984(3) the offeror's duty to give notice` at `coa21-ch3-sell-out.l4:319`.
This module calls neither.

For s 981(6):

- **Gate.** The existing rule takes no input, so it binds whatever happened before. This module runs the duty only for a notice that s 979 and s 980(2) allow (src:13650-13652, src:13668 "applies where the offeror gives a shareholder a notice under section 979": the offeror's entitlement to give notice and the notice given by the last day), only on or after the end of six weeks from the date of the notice (src:13679), and not while an application under s 986(1) is pending at the end of those six weeks (src:13777-13778: "section 981(6) does not have effect until the application has been disposed of"), and not after a court order that the offeror is not entitled and bound (src:13774-13776).
- **Clock.** Both are WITHIN 0 at the end of the six weeks (src:13679 "must immediately"). The difference is the gate on day 0: the existing rule leaves the day to the caller; this module tests the day given against the date of the notice plus 42 days (the existing `s 981(3)(a)` function) and, where an application is pending, against the day of disposal. The test is AT LEAST, so a later day also passes and a caller starts the trace on the first day on which the duty arises.
- **Acts.** The existing rule has one act (send the copy and pay); this module has two, each with its own breach (src:13680 "(a) send a copy of the notice to the company", src:13681 "(b) pay or transfer to the company the consideration"), so that a copy sent on time and a payment a day late is a breach of (b) only.
- **Parties.** The existing rule uses its own party type with the offeror; this module's party type adds the shareholder, the company and an officer.

For s 984(3):

- **Gate.** The existing rule takes only the end of the acceptance period and binds the offeror whatever the holder's position. This module runs the duty only where the holder has a right under s 983 (the answer of the existing `s 983(2)`, `(3)` or `(4)` function; src:13719-13732) and not where the offeror has given the shareholder a s 979 notice in respect of the shares (src:13751).
- **Clock.** The same: both read "the time specified" (src:13747 "Within one month of the time specified in subsection (2), (3) or (4)") as the end of the acceptance period, one month on by the existing `s 984(3)` function; the other reading, one month from the day the conditions of s 983 are first met (src:13719 "at any time before the end of the period"), is in the fork. Neither encodes an earlier notice, which the last sentence of s 984(3) allows.
- **Offences.** The existing rule gives the reason for the breach only; this module's reason cites the offence of s 984(5) and adds a separate prohibition on an officer in default (src:13752-13753), gated by the existing `s 984(5)` function.
- **What follows.** Neither goes on from the notice. This module adds the holder's window (src:13744-13746) and the offeror's duty to acquire once the holder requires it (src:13760).

### What this module does not encode, and why

- The content of the notices (ss 980(1), 981(3), 984(3), 985(3)) and the prescribed manner and form: tested by the existing functions, not time limits.
- The share counting of ss 979 and 983 (the 90% tests, treasury shares, associates, conditional contracts): the existing functions; this module takes their answers as gates.
- s 980(5) (a director signs where the offeror is a company) and s 980(8), s 984(7) (the penalties): no duty with a time, and the penalties stay the existing functions.
- s 981(5) and s 985(5) (cash equivalent where the consideration cannot be provided), s 981(7) and (8) (the instrument of transfer and the warrants, and the company's registration or issue), s 985(3) and (4) (the choice on a requirement): no time limit, and the registration or issue is the company's step on receipt.
- s 982(6) to (9) (a company registered in Scotland, the Accountant of Court, the expenses of enquiries): the existing functions answer for them; for a Scottish company the s 982(4) rule here is FULFILLED.
- s 986(3) to (10) (the court's orders on terms and costs, the notices of an application, and the court's authority to allow notices where shareholders cannot be traced): the court's powers and the notice duties carry no time limit that the Act states; the Boolean functions stay in `coa21-ch3-sell-out.l4`.
- s 983(6) and (7) (a requirement made while conditional contracts are open) and the effect of a requirement made after the acceptance period under s 984(2)(b): inside the answer of the existing s 983 function and the existing s 984(2) function.
- Debentures treated as shares (s 990(1)): inside the existing s 983 function.
