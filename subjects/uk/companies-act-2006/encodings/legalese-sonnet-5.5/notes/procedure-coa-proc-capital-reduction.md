## Procedure layer: reduction of share capital, the two routes and the offences (ss 641 to 653)

The procedure that Companies Act 2006 ss 641 to 653 lays down when a company reduces its share capital, written as regulative rules over the Boolean encoding in `coa14-ch10-reduction.l4`.
Route one is the private company's special resolution supported by a solvency statement (ss 642 to 644).
Route two is the application to the court, the creditors' objection, the court's order and the registration of the order (ss 645 to 649).
The offences are in ss 643(4), 644(7), 644(8) and 647.

Files: `coa-proc-capital-reduction.l4` (the rules) and `coa-proc-capital-reduction-tests.l4` (57 traces and 11 assertions).
Source lines 8529-8710 of `ukpga-2006-46.txt`.
No existing module is edited; the new module imports `coa-core`, `coa14-nouns` and `coa14-ch10-reduction` and calls their functions as gates wherever one answers the question.

### The seat of each rule

| rule | seat | what it does |
| --- | --- | --- |
| `ss 641-653 route one is open to the company` (Boolean helper) | s 641(1)(a), (2); s 642(1)(a) (src:8530-8533, 8553-8555) | the gate: a private company limited by shares, the s 641(2) bar not met (existing function), the statement made in accordance with s 643 (an input) |
| `ss 641-653 the resolution was passed within 15 days after the solvency statement` (Boolean helper) | s 642(1)(a) (src:8553-8554) | the window of limb (a), from two dates; the statement's day and the 15 days after it are in time |
| `ss 641-653 the deliveries of s 644 are owed` (Boolean helper) | s 644(1), (5) (src:8576-8593) | route one is open, the resolution is a special resolution (an input), and the window holds |
| `s 642(1)(a) the company's power to pass the resolution within 15 days of the solvency statement` | s 642(1)(a) (src:8553-8554) | MAY, WITHIN 15, LEST FULFILLED (a closed route, not a breach) |
| `s 644(1) the company's duty to deliver the solvency statement and the statement of capital, as a procedure` | s 644(1) (src:8575-8579) | MUST, WITHIN the number of days the existing date function gives, LEST BREACH BY the company |
| `s 644(5) the company's duty to deliver the directors' statement, as a procedure` | s 644(5) (src:8591-8593) | the same, for the directors' statement |
| `s 644 the company's two deliveries to the registrar` | s 644(1) and (5) (src:8576-8596) | the two duties side by side (RAND) |
| `s 644(3) the registrar's duty to register the documents, as a procedure` | s 644(3) (src:8589) | MUST, no clock |
| `s 643(4) the director's duty not to deliver a solvency statement made without reasonable grounds` | s 643(4) (src:8569) | SHANT, the director in default |
| `s 644(7) the officer's duty not to let the company deliver a solvency statement that was not provided to members` | s 644(7) (src:8597) | SHANT, the officer in default |
| `s 644(8)(b) the officer's duty not to be in default in complying with section 644` | s 644(8)(b) (src:8598-8600) | SHANT, the officer in default; the company's offence under s 644(8)(a) is the BREACH of the two delivery rules |
| `s 645(1) the company's power to apply to the court for an order confirming the reduction` | s 645(1) (src:8606) | MAY, no clock |
| `s 646(1) the creditor's power to object to the reduction of capital` | s 646(1) (src:8614-8617) | MAY, no clock, gated by the existing function on the creditor's debt and the real likelihood; what an objection does is the separate s 648(2) rule |
| `s 646(2) the court's duty to settle a list of creditors entitled to object` | s 646(2) (src:8618) | MUST, no clock |
| `s 646(3)(b) the creditor's power to claim to be entered on the list by the day fixed` | s 646(3)(b) (src:8619-8621) | MAY, WITHIN the days between two dates the court fixes, LEST FULFILLED (a closed route, not a breach) |
| `s 647(1) the officer's duty not to conceal or misrepresent a creditor's name, debt or claim` | s 647(1) (src:8627-8632) | three SHANTs side by side (RAND), one for each limb |
| `s 648(2) the court's duty not to confirm the reduction unless satisfied about every creditor entitled to object` | s 648(2) (src:8638-8640) | SHANT, the court, where the existing function says the bar applies |
| `s 648(1) the court's power to make an order confirming the reduction` | s 648(1) (src:8637) | MAY, no clock, where the bar does not apply |
| `s 649(1) the registrar's duty to register the order and the statement of capital, and then to certify the registration` | s 649(1), (5) (src:8645-8646, 8666) | MUST register, and the next step is MUST certify (a HENCE); no clock |

The statement of the facts of route one is one record, `ss 641-653 route one facts`, so that a trace states them once.

### TIMELINE lines

Copied from the module, one per rule, in the module's order.

- `s 642(1)(a) the company's power to pass the resolution within 15 days of the solvency statement`: unit=calendar day; day 0=the day the directors make the solvency statement; counting="not more than 15 days before the date on which the resolution is passed" (read forward: the resolution is passed on day 0 or within 15 days after it, so the last day is day 15; the Act does not say whether the day of the statement is counted)
- `s 644(1) the company's duty to deliver the solvency statement and the statement of capital, as a procedure`: unit=calendar day; day 0=the day the resolution for reducing share capital is passed; counting="Within 15 days after the resolution ... is passed" (the Act does not say whether the day of the resolution is counted; the existing function ends the period on the resolution's date plus 15, so day 15 is in time)
- `s 644(5) the company's duty to deliver the directors' statement, as a procedure`: unit=calendar day; day 0=the day the resolution for reducing share capital is passed; counting="within 15 days after the resolution is passed" (as for s 644(1) above: day 15 is in time)
- `s 644 the company's two deliveries to the registrar`: unit=calendar day; day 0=the day the resolution for reducing share capital is passed; counting="within 15 days after the resolution is passed" for both deliveries, each on its own clock from the same day 0
- `s 644(3) the registrar's duty to register the documents, as a procedure`: unit=none; day 0=the day the registrar receives the documents; counting=silent beyond "on receipt" (a clock is not encoded: the registration stays owed until the trace shows it)
- `s 643(4) the director's duty not to deliver a solvency statement made without reasonable grounds`: unit=none; day 0=not applicable; counting=silent (the offence is the event "makes a solvency statement without having reasonable grounds ... and the statement is delivered to the registrar"; the Act gives it no time limit, so no clock is encoded and the event is supplied by the trace)
- `s 644(7) the officer's duty not to let the company deliver a solvency statement that was not provided to members`: unit=none; day 0=not applicable; counting=silent (s 644(7) gives no time limit; the event is the delivery of the statement, supplied by the trace)
- `s 644(8)(b) the officer's duty not to be in default in complying with section 644`: unit=none; day 0=not applicable; counting=silent (the default is the breach of the delivery rules above, which carry the 15 days; the officer's offence is the event "default is made", supplied by the trace)
- `s 645(1) the company's power to apply to the court for an order confirming the reduction`: unit=none; day 0=not applicable; counting=silent (the Act gives the company no time to apply, so no clock is encoded: the power stays open until the trace shows it used)
- `s 646(2) the court's duty to settle a list of creditors entitled to object`: unit=none; day 0=not applicable; counting=silent (the Act gives the court no time to settle the list, so no clock is encoded)
- `s 646(1) the creditor's power to object to the reduction of capital`: unit=none; day 0=not applicable; counting=silent (s 646(1) gives the creditor no time to object, so no clock is encoded: the power stays open until the trace shows it used)
- `s 646(3)(b) the creditor's power to claim to be entered on the list by the day fixed`: unit=calendar day; day 0=the day the court publishes the notice; counting="a day or days within which creditors not entered on the list are to claim to be so entered" (the days are counted from the two dates the court fixes: the notice's date and the last day for claims, so the last day is the day fixed itself)
- `s 647(1) the officer's duty not to conceal or misrepresent a creditor's name, debt or claim`: unit=none; day 0=not applicable; counting=silent (s 647 gives no time limit; each of the three events is supplied by the trace)
- `s 648(2) the court's duty not to confirm the reduction unless satisfied about every creditor entitled to object`: unit=none; day 0=not applicable; counting=silent (the Act gives the court no time to make or refuse the order, so no clock is encoded on either rule)
- `s 648(1) the court's power to make an order confirming the reduction`: unit=none; day 0=not applicable; counting=silent (as above)
- `s 649(1) the registrar's duty to register the order and the statement of capital, and then to certify the registration`: unit=none; day 0=the day the order and the statement of capital are delivered to the registrar; counting="on the delivery" for the registration and silent for the certificate (no clock is encoded on either: each stays owed until the trace shows it)

### Forks

- s 642(1) "supported by a solvency statement" as a gate: the existing function cannot gate a duty to deliver, because its limb (b) (src:8555) asks that the resolution and statement "are registered in accordance with section 644", which is what the delivery brings about; the gate here asks limb (a) alone, from two dates.
  The other reading uses the existing function with the registration input set TRUE.
  The existing function is not wrong for its own question; it cannot serve as the precondition of the duty that produces its limb (b).
- s 642(1)(a) "not more than 15 days before": read forward as a power of the company with a LEST, whose last day is day 15.
  The other reading has no forward rule, only the Boolean test on two dates.
- s 642(1)(a) a lapsed power: a closed route, LEST FULFILLED, because s 642(1) defines when a resolution "is supported by a solvency statement" (src:8553-8554) and puts no duty on the company to pass a resolution.
  The other reading, the first draft's, is LEST BREACH BY the company; the independent review changed it, and no one is in breach.
- s 644(1) the gate: the duty arises on route one when the resolution is passed within 15 days of a statement made in accordance with s 643.
  The other reading: any resolution for reducing share capital of a private company, whether or not the statement is in time.
- s 644(8)(a) the company's offence is the BREACH of the delivery rules, named in the reason, and not a second rule.
- s 644(1) with s 644(5): two duties side by side, each with its own breach; the other reading is one rule with two acts.
- s 644(3) "on receipt" and s 649(1) "on the delivery": no clock; the other reading is WITHIN 0, the same day.
- s 643(4) "every director who is in default": the prohibition lies on the director, answering only where s 1121 (an input) is JUST TRUE; the other reading is any director.
- s 644(7): the prohibition lies on the officer in default and the act is the company's delivery; the other reading puts it on the company.
- s 644(8)(b): the officer's offence is a prohibition on being in default, gated by the existing function; the other reading makes it follow from the company's breach only.
- s 645(1): each later step is its own rule with its own day 0, because the court's outcome is an input to each; the other reading makes them the next steps of the application.
- s 646(1) "is entitled to object": the entitlement is a power of the creditor (MAY), gated by the existing function, and objecting is the act; the other reading has no rule and the entitlement is only a condition of s 648(2).
- s 646(3)(b) "within which": the day fixed is the last day for a claim; the other reading is that it is the first day that is too late.
- s 646(3)(b) a lapsed claim: a closed route, LEST FULFILLED: the creditor who does not claim by the day fixed "is to be excluded from the right of objecting" (src:8621), the loss of a right and no wrong.
  The other reading, the first draft's, is LEST BREACH BY the creditor; the independent review changed it.
- s 647(1): three prohibitions side by side, each gated by the existing function with its own event TRUE; the other reading is one prohibition with one act.
- s 648(2) "must not confirm ... unless": a prohibition on the court, the order in the barred case being the BREACH; the other reading is that the order is void or open to appeal, not a breach.
- s 649(5): the certificate is the next step of the registration; the other reading is a separate rule gated on the registration.

### What the text leaves silent (no clock encoded)

- ss 641 to 653 give no time for: the registrar to register (s 644(3), s 649(1)), the certificate (s 649(5)), the company to apply to the court (s 645(1)), a creditor to object (s 646(1)), the court to settle the list (s 646(2)) or to make or refuse the order (s 648), or for an officer to commit any of the offences.
- s 644(1) and (5) do not say whether the day of the resolution is counted; the encoding follows the existing function, which ends the period on the resolution's date plus 15.
- s 646(3)(b) does not say how many days the court gives: the court fixes the day, and the two dates are inputs.
- s 649(4) says notice of the registration "must be published in such manner as the court may direct" and names no one who must publish it.

### Which binary verified the traces

- Unstable build a50cbd0 (25 November 2026): 57 of 57 traces match their EXPECT, and all 11 assertions are satisfied; no `DiagnosticSeverity_Error`, no `DiagnosticSeverity_Warning`.
- Main build 112: 57 of 57 traces match, with none reading differently in class; all 11 assertions are satisfied; no `DiagnosticSeverity_Error`, no `DiagnosticSeverity_Warning`.
- The only warnings printed are the two import-resolution warnings about `prelude` and `daydate` (an installed copy under the XDG data directory differs from the embedded one); they come from the machine and not from the new files.
- A sensitivity check on two scratch copies, deleted afterwards: an off-by-one in the s 644(1) limit, in the s 642(1)(a) window and in the s 646(3)(b) days failed the day-15 delivery trace and the day-59 claim trace, and the assertions that sit on the window boundary; flipping the s 648(2) gate and dropping the "not entered on the list" condition failed the four traces that read them.

### READS-DIFFERENTLY-ON-MAIN

No trace differs in class between unstable and main.
Four traces did differ before the independent review (`s 642(1)(a)`: the resolution on day 16, and no resolution by day 20; `s 646(3)(b)`: the creditor claims on day 60, and the creditor does nothing): a power with a time limit written as MAY with a LEST reached BREACH on unstable and FULFILLED on main.
The module now ends those two windows with LEST FULFILLED, as a closed route, so both builds print FULFILLED.

Five traces print differently on main with the same class on both: the RAND of two breaches in `s 644` (main prints only the first), the three open prohibitions (`s 643(4)`, `s 647(1)`, `s 648(2)`: the LEST's BREACH is in parentheses on unstable only) and the nested HENCE of `s 649(1)`.
The test file lists each trace by line.

### Closed routes (not breaches)

Convention for all the procedure units (assumed, not ruled): `BREACH` is kept only for a duty or a prohibition that the text lays on a named party.
A power that lapses unused, a condition that is not met, a vote that fails and a route that has closed end `FULFILLED`, with the reason (what was lost, and the statute line) in a comment beside the LEST.
This unit has two, and four traces moved from BREACH to FULFILLED after the independent review:

- `s 642(1)(a)`: a resolution passed on day 16, or no resolution within the 15 days, ends the use of that solvency statement for route one; s 642(1) is a definition of when a resolution "is supported by a solvency statement" (src:8553-8554) and lays no duty on the company.
- `s 646(3)(b)`: a creditor who does not claim by the day fixed, or claims after it, is excluded from the right of objecting (src:8621), and has done no wrong.

The BREACHes that stay are the deliveries of `s 644(1)` and `s 644(5)` (the duty is the company's, src:8576, 8591) and the offences of ss 643(4), 644(7), 644(8) and 647.

### Differences from the existing DEONTIC

The existing rules are `s 644(1) the company's duty to deliver to the registrar a copy of the solvency statement and a statement of capital` (`coa14-ch10-reduction.l4:450`) and `s 644(5) the company's duty to deliver to the registrar a statement by the directors ...` (`:564`).
They were read, and the new rules were written from the text without calling them; they were not traced here, so the differences below are differences in form, which decide behaviour as stated.

- A gate.
  The existing rules have none: they take the number of days as an input and run for any number given.
  The new rules answer only where route one is open and the window holds (src:8553-8555), and otherwise end FULFILLED with no duty.
- The limit.
  The existing rules take the number of days from the caller (`GIVEN the number of days allowed IS A NUMBER`), so a caller can feed 14 or 20.
  The new rules compute it from the resolution's date with the existing function `s 644(1) the number of days allowed for the documents`, which gave 15 on the dates the traces use (src:8576, "Within 15 days after").
  Given 15, both rules end the period on day 15, and day 16 is the breach.
- The party and the act.
  The existing rules use the generic `Party` and `Action of a party` with a free-text description; the new rules use their own enums, so a trace can tell the two deliveries apart and a RAND of both is possible.
- The reason.
  The new rules name the company's offence under s 644(8)(a) in the BREACH reason (src:8598-8600); the existing reasons name only the missed delivery.

### What this module does not encode, and why

- s 642(2) and (3): the duty to send or make available a copy of the solvency statement "at or before" the time the resolution is sent, and "throughout" the meeting.
  A duty to act at or before an event cannot run forward from that event; the Boolean functions in `coa14-ch10-reduction.l4` answer them.
- s 642(4), s 644(4) and s 644(6): the validity of the resolution, and when it takes effect; they change neither a duty nor a time limit.
- s 643(5), s 644(9) and s 647(2): the penalties, which fix no time and are Boolean functions in the existing module.
- s 643(1) to (3): what a solvency statement is and says; the gate takes the answer as an input.
- s 645(2) to (4), s 648(3) and (4): the court's powers to apply or disapply section 646, to order publication and to add the words "and reduced"; each is a power of the court with no time and no duty on another party.
  They stay as Boolean functions.
- s 646(3)(a), (4) and (5): the court's duty to find the creditors without an application, and its power to dispense with a creditor's consent on the company securing payment.
  Dispensing depends on an act of the company (securing the payment) that the Act gives no time for and attaches no consequence to except through s 648(2), which reads the creditor's "secured" fact; they stay as Boolean functions.
- s 649(2) to (4) and (6): the contents of the statement of capital, when the resolution takes effect, the notice of registration (no party is named) and the certificate's effect.
- ss 650 to 653: public companies below the authorised minimum, the re-registration procedure, and members' liability.
  None gives a deadline or an offence; s 650(2) is read only as an input to the registrar's duty at s 649(1).
