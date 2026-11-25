## Procedure layer: register of members, requests to inspect or copy (ss 116 to 118)

The procedure that Companies Act 2006 ss 116 to 118 lays down when a person asks to inspect the register of members or to have a copy of it, written as regulative rules over the Boolean encoding in `coa3-part8-inspection.l4`.

Files: `coa-proc-register-copy.l4` (the rules) and `coa-proc-register-copy-tests.l4` (35 traces and 9 assertions).
Source lines 1557-1588 of `ukpga-2006-46.txt`.
No existing module is edited; the new module imports `coa-core`, `coa3-part8-members` and `coa3-part8-inspection` and calls their functions as gates.

### The seat of each rule

| rule | seat | what it does |
| --- | --- | --- |
| `ss 116-118 the company has received a request that section 116 allows` (a Boolean helper, not a DEONTIC) | s 116(1)-(4), s 117(1) "a request under section 116" (src:1557-1573) | the gate: the request carries what s 116(4) requires and the person has the right at s 116(1)(a), (1)(b) or (2); it calls the s 116 predicates and is the argument of the s 117(1) function |
| `s 117(1) the company's duty to comply with a request or apply to the court` | s 117(1) (src:1572-1575) | the company must within five working days comply or apply to the court; either alternative meets the duty (ROR); neither by day 6 is BREACH BY the company |
| `s 117(2) the company's duty to notify the person making the request` | s 117(2) (src:1576) | owed once the company has applied; no clock |
| `s 117(3)(a) the court's duty to direct the company not to comply` | s 117(3) (src:1577-1579) | a MUST of the court, gated on the court's finding of improper purpose; no clock |
| `s 117(5) the company's duty to comply immediately` | s 117(4)-(5) (src:1580-1582) | when the court has decided without directing the company not to comply, or the proceedings are discontinued, the company must comply WITHIN 0 of that day |
| `s 118(1)(a) the company's duty not to refuse an inspection or make default in providing a copy` | s 118(1)(a) (src:1583-1586) | a prohibition (SHANT) on the company, gated by the existing s 118(1) function, which excludes a refusal in accordance with an order of the court |
| `s 118(1)(b) the officer's duty not to be in default in a refusal or default` | s 118(1)(b) (src:1583-1586) | the same prohibition on an officer in default, the officer's default (s 1121) being an input |
| `s 118(1) the company and every officer in default` | s 118(1) (src:1583-1586) | the two prohibitions side by side (RAND) |
| `s 118(3) the court's power to compel an inspection or direct that the copy be sent` | s 118(3) (src:1588) | a MAY of the court, gated by the existing s 118(3) function and by the exclusion of a refusal in accordance with an order of the court; no clock |

The offence of s 118(1) is encoded as a prohibition on an event (the refusal or the default), as separate rules from the s 117(1) duty, and the court's power under s 118(3) as a separate rule.
The fine in s 118(2) stays the `Penalty` function of `coa3-part8-inspection.l4`.

### Why s 117(2) to (5) are three rules and not the next steps of s 117(1)

Measured on both binaries, in two attempts.
(1) With the court route as the HENCE of the apply branch of the ROR, a company that had applied on day 2 and was waiting for the court printed, once the trace waited past day 5, the lapsed comply alternative's breach beside the still-open court route (`DEONTIC BREACHED: BREACH BY ... OR PARTY ...`, the same on both binaries, shown with a prelude-only ROR of `MUST a WITHIN 5` and `MUST b WITHIN 5 HENCE MUST c`).
A reader that classes a block by the prefix `DEONTIC BREACHED` reads that as BREACH although the court route is still open.
(2) With the court's outcomes written as MAY events in a ROR (directs; decides without directing; proceedings discontinued), the ROR did not commit to the branch whose event happened: a late compliance after the decision printed as the still-open `court MAY direct` instead of BREACH.
So the court's outcome is an input to each rule, as the Boolean layer already takes it, and each rule has its own day 0: the day of receipt, the day of the application, or the day of the decision.

### TIMELINE lines

- `s 117(1) the company's duty to comply with a request or apply to the court`: `TIMELINE: unit=working day; day 0=the day the company receives the request; counting="within five working days" (the Act fixes the period but does not say whether the day of receipt is counted, so the trace is built with day 0 as the day of receipt and day 5 as the fifth working day after it)`
- `s 117(2) the company's duty to notify the person making the request`: `TIMELINE: unit=working day; day 0=the day the company applies to the court; counting=silent (s 117(2) gives no time for the notice, so no clock runs: the notice stays owed until the trace shows it)`
- `s 117(3)(a) the court's duty to direct the company not to comply`: `TIMELINE: unit=working day; day 0=the day the company applies to the court; counting=silent (the Act gives the court no time to decide, so no clock runs: the direction stays owed until the trace shows it)`
- `s 117(5) the company's duty to comply immediately`: `TIMELINE: unit=day of the event; day 0=the day the court gives its decision or the proceedings are discontinued; counting="immediately upon" (WITHIN 0: the company acts on that same day)`
- `s 118(1)(a) the company's duty not to refuse an inspection or make default in providing a copy`: `TIMELINE: unit=none; day 0=not applicable; counting=silent ("is refused or default is made": the Act gives no time limit and no day on which a default is made, so no clock is encoded and the refusal or default is an event the trace supplies)`
- `s 118(1)(b) the officer's duty not to be in default in a refusal or default`: `TIMELINE: unit=none; day 0=not applicable; counting=silent (as for the company's prohibition above: s 118(1)(b) gives the officer no time either)`
- `s 118(1) the company and every officer in default`: `TIMELINE: unit=none; day 0=not applicable; counting=silent (the two prohibitions above, side by side, with no clock)`
- `s 118(3) the court's power to compel an inspection or direct that the copy be sent`: `TIMELINE: unit=none; day 0=not applicable; counting=silent (the Act gives the court no time limit, so no clock is encoded: the power stays open until the trace shows it used)`

### Forks

- `FORK: s 117(1) "a request under section 116" | a request is one under s 116 only if it carries the information s 116(4) requires and the person has the right at s 116(1) or (2) (the fee paid, where one is due) | any request at all starts the five working days, and the missing information is a ground for the court to refuse`
- `FORK: s 120A | where a restriction under s 120A applies the helper answers FALSE and no duty is encoded | the duty is as in s 117 and the restriction only narrows what is shown`
- `FORK: s 117(1) "within five working days" | the last day is day 5, the fifth working day after the day of receipt | the day of receipt counts as day 1 and the last day is day 4`
- `FORK: s 117(1) "either (a) or (b)" | the two ways of answering are alternatives: either one meets the duty of s 117(1), and what follows an application is the three rules below (s 117(2), s 117(3)(a), s 117(5)), each run from its own day 0 | the company must also comply while the application is pending`
- `FORK: s 117(3)(a) "it shall direct" | the court's duty to direct is a MUST of the court, gated by the existing function on the court's own finding that the inspection or copy is not sought for a proper purpose (an input) | the direction is a power (MAY)`
- `FORK: s 117(5) "immediately" | the same day as the decision or the discontinuance | a short reasonable time after it`
- `FORK: s 117(5) "does not direct the company not to comply" | the court has not directed the company not to comply when it has not given the s 117(3)(a) direction; a discontinuance is read the same way (the court gives no direction) | the court's not directing means only that it found the purpose proper, and a discontinuance is a separate trigger`
- `FORK: s 118(1) "default is made" | the offence is encoded as a prohibition on the event "refuses the inspection or makes default in providing the copy", and the missed five working days of s 117(1) is a separate breach (it is not itself the event) | the missed five working days is the default`
- `FORK: s 118(1)(b) "every officer of the company who is in default" | a second prohibition on the officer, standing beside the company's (RAND), gated by the existing s 118(1) function with the officer's default as an input | the officer's liability is only a consequence of the company's breach`
- `FORK: s 118(3) "any such refusal or default" | "such" carries the words "otherwise than in accordance with an order of the court", so the power does not arise where the refusal is in accordance with an order (the existing function for s 118(3) does not read it so) | any refusal or default`

### What the text leaves silent (no clock encoded)

- Whether the day of receipt counts in the five working days (s 117(1)); the trace takes day 0 as the day of receipt and day 5 as the last day.
- Any time for the notice of s 117(2).
- Any time for the court to decide, to direct, or to make an order (ss 117(3) to (5), 118(3)).
- Any day on which a "default" under s 118(1) is made, and what a default is.
- The fee ("such fee as may be prescribed") and the restrictions of s 120A, which are outside the sources; both are inputs, and a restriction under s 120A takes the case outside the rules (no duty is encoded).
- Who discontinues the proceedings in s 117(5); the rule takes the discontinuance as an input and names no one.

### Which binary verified the traces

Both, from inside the encoding folder with `JL4_LIBRARY_PATH` unset: the unstable build `l4-unstable-20261125-a50cbd0` and the stable line, `~/.cache/l4-main/112/l4`.
On each, `coa-proc-register-copy.l4` and `coa-proc-register-copy-tests.l4` print no error; all 9 assertions are satisfied; all 35 traces match their `-- EXPECT` line (`expect_check.py`).
The unstable build prints three `lint/lest-without-deadline` warnings, none in these files: they are at `coa3-part8-members.l4` line 143 and `coa3-part8-inspection.l4` lines 74 and 494, which this unit imports and does not edit.
`srcrefs.py check --refs` reports 31 quoted source lines, 7 locators, no problem.

### READS-DIFFERENTLY-ON-MAIN

No trace differs in class between the two binaries.
Six print differently, with the same class (the list is at the end of `coa-proc-register-copy-tests.l4`): the three breaches of s 117(1) (the two alternatives' breaches are joined by BY on unstable and by OR DEONTIC BREACHED on main), the two open s 118(1) prohibitions (parentheses round the LEST on unstable), and the trace in which the company refuses and the officer is in default on the same day (unstable prints both breaches, main prints the company's only).

### Differences from the existing DEONTIC

The existing DEONTIC is `s 117(1) the company must within five working days comply with the request or apply to the court (duty)` at `coa3-part8-inspection.l4:312`.
This module does not call it.

- **Gate.** The existing rule takes no input, so it binds from day 0 whatever the request. This module runs the duty only for a request that s 116 allows (src:1573, "Where a company receives a request under section 116"; src:1564-1571 for what the request must contain; src:1558-1561 for the right and the fee): a request with no purpose stated, or from a person who is not a member and has not paid the fee, owes nothing and prints FULFILLED.
- **Limit and alternatives.** The same: five working days, day 0 the day of receipt, day 5 the last day, comply or apply as alternatives (src:1573-1575), BREACH BY the company if neither by day 6.
- **After applying to the court.** The existing rule ends FULFILLED at the application. This module also ends the s 117(1) duty there, and adds the notice (src:1576; no clock), the court's duty to direct (src:1578), and the company's duty to comply immediately when the court has not directed otherwise or the proceedings are discontinued (src:1582; WITHIN 0).
- **Court's costs order and the wider direction.** Not encoded in either (src:1579-1581).
- **Offences and the court's compulsion.** The existing DEONTIC has none; ss 116 and 118 are Boolean only there. This module adds the prohibition on the company and on every officer in default (src:1584-1586) and the court's power (src:1588), with the gate that excludes a refusal "in accordance with an order of the court" (src:1584); the existing `s 118(3)` function does not carry that exclusion, and this module's rule does (see the fork on "any such refusal or default").
- **Parties.** The existing rule uses `Party` from `coa-core` and names the company only; this module has its own party type with the company, the court and an officer in default.

### What this module does not encode, and why

- s 117(3)(b) (costs against the person who made the request) and s 117(4) (a direction covering other requests, and the order's contents): powers of the court that change neither this company's duty nor a time limit; they stay Boolean in `coa3-part8-inspection.l4`.
- s 118(2) (the penalty): a consequence of conviction, not a duty; it stays the `Penalty` function.
- s 116(3) (the duty to make a request): a condition of the right, folded into the gate through the s 116(4) predicate.
- s 119 (offences in connection with a request or its use): outside the unit.
- Whether an order under s 118(3) binds the company further: the Act says "compel", and no step after the order is encoded.
