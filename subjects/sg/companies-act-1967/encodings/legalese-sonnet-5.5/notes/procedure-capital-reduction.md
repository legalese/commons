## Procedure layer: the reduction of share capital (Companies Act 1967 ss 78B to 78K)

The module `sg-proc-capital-reduction.l4` is a regulative layer over the Boolean encodings in `sga3-78a-78c.l4` and `sga3-78d-78k.l4`; its tests are in `sg-proc-capital-reduction-tests.l4`.
It encodes the procedure the Act lays down for a company that reduces its share capital by special resolution, as one chain of steps, each clock measured from its own trigger because a HENCE starts the next clock when the earlier step is done.
The parties are the corpus's own `Party`; the acts are the constructors of `capital reduction act`.
The gates are the existing section functions, called and not restated: `s 78B(2)` and `s 78C(2)` (the dispensation from the solvency statement), `s 78D(3)` (which creditor may apply), `s 78F(2)` (when the Court must cancel), `s 78H(1)` (whether the Court settles a list), `s 78I(2)` (the bar on an order) and `s 78I(3) the last day ...` (the 90 days or the longer period the Registrar allows).
No existing module was edited and no existing function needed to change.

### The chain, in order

1. All the directors make the solvency statement (s 78B(3), s 78C(3)); the company passes the special resolution within the 20 days (private) or 30 days (public) the statement can serve (s 78B(1), s 78C(1)).
2. On the resolution date: the statement is available at the meeting (s 78B(4)(a), s 78C(4)(a)), and a public company lodges a copy of it with the Registrar within 15 days beginning with that date (s 78C(3)(c)).
3. Side by side from the resolution date: the statement is kept open to creditors throughout the 6 weeks (s 78B(4)(b), s 78C(4)(b)), and a creditor may apply to the Court during those 6 weeks (s 78D(2)).
4. If no creditor applies, the company lodges the documents after the end of 6 weeks and before the end of 8 weeks (s 78E(1)(d), (2)).
5. If a creditor applies: the creditor serves the application and the company notifies the Registrar, both "as soon as possible" (s 78D(4)); the Court cancels the resolution (s 78F(2)) and the company sends notice of the order within 15 days (s 78F(4)), or the Court dismisses it (s 78F(3)), or the creditor withdraws it, and then the company lodges within 15 days beginning with the end of the proceedings (s 78E(3), (4)).
6. The Court-approved route (ss 78G to 78I) is a second chain: the application, the Court's list (s 78H(2)), the Court's order (s 78I(1)) unless the bar of s 78I(2) stands, and the company's lodging within 90 days beginning with the order or the longer period the Registrar allows (s 78I(3)).
7. The offences are BREACH lines on the duties they follow (s 78B(5), s 78C(5), s 78F(5)) and two prohibitions: s 78H(5) (an officer conceals or misrepresents a qualifying creditor; the fine and the imprisonment the text states are in the BREACH line) and s 78J (a director's false statement; the text states no penalty).
8. Section 78K limits a member's liability on a sum; it is not a step, so it has no DEONTIC (the Boolean and number functions in `sga3-78d-78k.l4` answer it).

### The seat of each DEONTIC, its TIMELINE line and its forks

**`s 78B(4)(b) and s 78C(4)(b) the company must keep the solvency statement open to creditors throughout the 6 weeks`**

- Seat: the company MUST keep the statement open to creditors by day 41, LEST BREACH BY the company; gate: the dispensation of s 78B(2) or s 78C(2).
- TIMELINE: unit=calendar day; day 0=the resolution date; counting="throughout the 6 weeks beginning with the resolution date", the resolution date being day 1 of the 6 weeks, so the last day is day 41, computed from the DATE input `the resolution date` by sg-periods P10; the duty is done when the company has kept the statement open on every one of the 42 days, so the act is reported on or before day 41
- FORK: s 78B(4)(b) | the duty is one act ("has kept the statement available throughout the 6 weeks") due on or before day 41, so a company that opened it late or withdrew it early never does the act and the breach is found after day 41 | two acts as the existing rule has them (make it available on day 0, then not withdraw it until day 41)
- FORK: s 78B(6) | the revocation of the resolution, which ends the requirement, is not a step here: the text puts it in the passive and names no one who revokes | an act of the company that ends the duty

**`s 78F(4) and (5) the company must send notice of the order to the Registrar within 15 days beginning with the date the order is made`**

- Seat: the company MUST send the notice of the order within 14 days, LEST BREACH BY the company.
- TIMELINE: unit=calendar day; day 0=the day the Court makes the order cancelling the resolution; counting="within 15 days beginning with the date the order is made", the date being day 1, so the last day is day 14 (sg-periods P10)

**`s 78E(3)(e) and (4)(e) the company must lodge within 15 days beginning with the date the last proceedings end`**

- Seat: the company MUST lodge within 14 days, LEST BREACH BY the company.
- TIMELINE: unit=calendar day; day 0=the day the last of the proceedings on the creditors' applications is brought to an end (by dismissal under s 78F, or without determination, for example by withdrawal); counting="within 15 days beginning with the date on which the last such proceedings were brought to an end", that date being day 1, so the last day is day 14 (sg-periods P10)
- FORK: s 78E(3)(e) | one application is encoded; where there are several, this rule starts on the day the last proceedings end, which the caller reads off | a clock for each application
- FORK: s 78E(3)(e) | the lodging is a duty whose breach line says the reduction does not take effect; the text states no offence for it | a bare condition with no breach

**`s 78F and s 78E(3)(d): the Court decides, or the creditor withdraws`**

- Seat: where the creditor withdraws, the creditor MAY withdraw, HENCE the lodging rule; otherwise the gate `s 78F(2) the Court must make an order cancelling the resolution` chooses: the Court MUST cancel, HENCE the notice rule, or the Court MUST dismiss, HENCE the lodging rule.
- TIMELINE: unit=calendar day; day 0=the day the creditor applies to the Court; counting=silent for the Court's decision ("no time limit" in s 78F) and for the creditor's withdrawal; the clocks that follow are the two rules this one calls, whose day 0 is the day the order is made (s 78F(4)) or the day the proceedings end (s 78E(3), (4))
- FORK: s 78F(2) | where the gate does not answer JUST TRUE the Court MUST dismiss, because s 78F(3) says "Otherwise, the Court is to dismiss" | the Court MAY dismiss
- FORK: s 78E(3)(d)(ii) | the creditor's withdrawal is a MAY of the creditor, chosen by an input (`the creditor withdraws the application`) as the Court's order or dismissal is chosen by its gate, and not an alternative (ROR) to the Court's decision | a ROR of the Court's MUST and the creditor's MAY: measured, a late lodging after a withdrawal then leaves the Court's duty open and reads RESIDUAL where the text says the company is in breach

**`s 78D(4), s 78E(3), s 78F: the service, the notice to the Registrar and the Court's decision after a creditor applies`**

- Seat: the creditor MUST serve the application, RAND the company MUST give the Registrar notice of it (both with no clock), RAND the Court's decision rule.
- TIMELINE: unit=calendar day; day 0=the day the creditor applies to the Court; counting="as soon as possible" for the service and for the company's notice to the Registrar, which is silent on a day, so no clock is encoded for either; the Court's decision is the rule called, with its own TIMELINE
- FORK: s 78D(4) | "as soon as possible" is a duty with no day, so it is a MUST with no clock and no breach path | a clock of some days

**`s 78D(2) and s 78E: a creditor may apply to the Court during the 6 weeks, and otherwise the company must lodge after them`**

- Seat: a creditor MAY apply to the Court within day 41 (gate `s 78D(3) subsection (2) applies to the creditor`), HENCE the rule for what follows an application; LEST the company MUST lodge the documents, LEST BREACH BY the company, in the rest of the 8 weeks.
- TIMELINE: unit=calendar day; day 0=the resolution date; counting="at any time during the 6 weeks beginning with the resolution date" for the creditor (day 0 to day 41, computed from the DATE input by sg-periods P10) and "after the end of 6 weeks, and before the end of 8 weeks, beginning with the resolution date" for the company (day 42 to day 55); the lodging clock is the rest of the 8 weeks after the creditors' window lapses, which is day 55 less day 41
- FORK: s 78E(1)(d) | the last day is day 55, so a lodging on the last day of the 8 weeks is "before the end" of them | the last day is day 54
- FORK: s 78E(1)(c) | the copy of the resolution is lodged "in accordance with section 186", which is outside the sources, so it is no step here and the one act is the documents of paragraph (d) (and of s 78E(2)(c), (d)) | a second act with its own clock
- FORK: s 78D(3) | an application by a person who is not a creditor within s 78D(3) is not an application under s 78D(2), so s 78E(1)(b) is still met and the company's lodging is still owed; it is owed here as a MUST with no clock, because the HENCE restarts the clock on the day of that application, which the rule does not know, so the window to day 55 cannot be carried | the application as one that stops the lodging under s 78E(1)(b), the rule then FULFILLED

**`s 78B(4)(b) to s 78F: the statement open to creditors, and the creditors' period with the lodging after it`**

- Seat: the statement kept open to creditors, RAND the creditors' period with the lodging after it.
- TIMELINE: unit=calendar day; day 0=the resolution date; counting="the 6 weeks beginning with the resolution date" and "after the end of 6 weeks, and before the end of 8 weeks, beginning with the resolution date" as the two rules called here state; the two run side by side, so both must be done

**`s 78B(4)(a), s 78C(3)(c), s 78C(4)(a): what the company owes on the day the resolution is passed, and what follows`**

- Seat: the company MUST make the statement available on the resolution date (WITHIN 0; gated by the dispensation), RAND the public company MUST lodge a copy with the Registrar within 14 days (gated: public and not dispensed), RAND the rule for the 6 weeks.
- TIMELINE: unit=calendar day; day 0=the resolution date; counting="throughout that meeting" for the statement at the meeting (the same day as the resolution, so WITHIN 0) and "within 15 days beginning with the resolution date" for the public company's lodging of the copy of the statement (day 0 to day 14, sg-periods P10)
- FORK: s 78B(4)(a) | the written-means route (s 78B(4)(a)(i)) and the meeting route (s 78B(4)(a)(ii)) are one act, because the trace says only that the statement was made available as the paragraph requires on the resolution date | two acts, one for each route
- FORK: s 78C(3)(c) | the public company's lodging of the copy of the statement is a duty whose breach line says the company does not meet the solvency requirements; the text frames it as a condition | a bare condition with no breach

**`s 78B and s 78C: the solvency statement, the special resolution, and what the company owes from the resolution date`**

- Seat: the board of directors MAY make the solvency statement (no gate, no clock), HENCE the company MAY pass the special resolution within the days from the statement that the 20-day (private) or 30-day (public) period allows, LEST FULFILLED; where the helper for s 78B(2) and s 78C(2) says the statement is dispensed with, the company MAY pass the resolution at once; HENCE the rule for the day the resolution is passed.
- TIMELINE: unit=calendar day; day 0=the day all the directors make the solvency statement (where s 78B(2) or s 78C(2) dispenses with it, the day the company is free to pass the resolution); counting="not before the beginning of the period of 20 days ending with the resolution date" (private) and "30 days" (public): the resolution is passed within day 19 (private) or day 29 (public) of the statement day, computed from the DATE input `the date of the solvency statement` by sg-periods P10; the resolution date is day 0 of every clock that follows, because the HENCE restarts the clock when the resolution is passed
- FORK: s 78B(3)(b)(i) | "in time for subsection (4)(a) to be complied with" is read as: the statement is made on or before the day of the resolution, so the resolution is never earlier than day 0 | a stricter day, the day before the meeting
- FORK: s 78B(3) | the directors' statement is a MAY of the board as a body, with no clock, because the text makes it a condition of the company's power and never a duty; the 20 (or 30) days are the limit on the resolution that follows | the statement as a duty (MUST)
- FORK: s 78B(1) | where the statement's 20 or 30 days lapse before the resolution, the rule is FULFILLED at once: nothing is owed and the company may not rely on this route for that statement | a breach by the company
- FORK: s 78B(1), s 78C(1), s 78A(5) | the chain is not gated on who may use the route (a private company limited by shares for s 78B(1), a public company for s 78C(1); not an unlimited company, a redemption under s 70(1) or a purchase under ss 76B to 76G, s 78A(5); and not where the constitution excludes the power, s 78A(3)): the caller supplies the facts, because the existing `may` functions take inputs the chain itself produces (the special resolution passed, the solvency requirements met), so calling them whole here would be circular | a gate on `s 78A(1)` and `s 78B(1)` or `s 78C(1)` before the first step
- FORK: s 78B(1)(c) | the publicity requirements are "as may be prescribed by the Minister", which is outside the sources, so they are not a step | a step with a clock

**`s 78G to s 78I: the application to the Court, the list, the order and the lodging within 90 days`**

- Seat: the company MAY apply to the Court, HENCE the Court MUST settle the list where `s 78H(1) this section applies` holds, RAND the gate `s 78I(2) the Court must not make an order approving the reduction` chooses between the Court SHANT approve (LEST BREACH BY the Court) and the Court MAY approve, HENCE the company MUST lodge within the 90 days or the longer period (LEST BREACH BY the company).
- TIMELINE: unit=calendar day; day 0=the day the company applies to the Court under s 78G(1); counting=silent for the Court's list, its order and the application ("no time limit"); the one clock is the company's lodging, whose day 0 is the day the order is made: "within 90 days beginning with the date the order is made, or within such longer period as the Registrar may ... allow", computed by the existing `s 78I(3) the last day ...` from the DATE inputs (the order date, whether the Registrar allowed longer, the last day of the longer period), which must agree with the days of the trace; the order date is day 0 of the clock because the HENCE restarts it when the order is made
- FORK: s 78G(1) | the chain is not gated on the company being limited by shares, nor on s 78A(5); the caller supplies the facts (see the fork at s 78B(1)) | a gate on `s 78G(1) the company limited by shares may reduce ...`
- FORK: s 78I(1) | where a creditor on the list stands in the way (s 78I(2)), the Court is under a SHANT and an order is a breach by the Court | the order simply not open to the Court, with no breach
- FORK: s 78H(2) | the Court's duty to settle the list is a MUST with no clock (the text has none), and s 78H(4)(a) (ascertaining the creditors) is part of that one act | s 78H(4)(a) as a separate step
- FORK: s 78G(1)(c) | the Registrar's recording, on which the reduction's taking effect depends, is not a step: it is an effect, not a duty with a clock | a MAY of the Registrar
- FORK: s 78I(3) | the Registrar's allowance of a longer period is an input (a Boolean and the last day), not a step in the chain: the text gives no time for the company's application to the Registrar | a MAY of the Registrar

**`s 78H(5) an officer must not conceal or misrepresent a qualifying creditor's name, debt or claim`**

- Seat: an officer SHANT conceal or misrepresent, LEST BREACH BY the officer.
- TIMELINE: unit=calendar day; day 0=the day the Court begins to settle the list; counting=silent (a standing prohibition; the text puts no time on it)
- FORK: s 78H(5) | the prohibition is derived from the offence and its bearer is an officer of the company (ruling N2 of 2026-11-04) | no bearer

**`s 78J a director must not make a false statement which the director does not believe to be true`**

- Seat: a director SHANT make a false statement, LEST BREACH BY the director.
- TIMELINE: unit=calendar day; day 0=the day the director makes the statement under s 78E(1)(d)(ii), (2)(c), (3)(e)(i) or (4)(e)(i); counting=silent (no time); the text states no penalty
- FORK: s 78J | the offence has two elements (false, and not believed by the director to be true), and the act is one: making a statement which is both | two acts

### What the text leaves silent (no clock is encoded)

- The Court has no time limit to decide an application (s 78F(1) to (3)), to settle the list (s 78H(2)) or to make an order (s 78I(1)); those steps are MUST or MAY with no WITHIN, so they have no breach path.
- The service of the application and the company's notice to the Registrar are "as soon as possible" (s 78D(4)), which is no day.
- The directors' solvency statement has no time of its own: s 78B(3)(b) and s 78C(3)(b) limit it only by its distance from the resolution date and by "in time for subsection (4)(a)".
- The copy of the resolution under s 186 (s 78E(1)(c)) and the publicity requirements "prescribed by the Minister" (s 78B(1)(c), s 78C(1)(c)) are outside the sources; they are not steps.
- Sections 78B(5), 78C(5), 78F(5) and 78J say "guilty of an offence" and state no penalty; the BREACH lines say so and invent none. Section 78H(5) states a fine not exceeding $15,000 or imprisonment not exceeding 3 years, which its BREACH line repeats.
- Where the text says a company "must" lodge "for the reduction to take effect" (s 78E, s 78I(3)) or must lodge a copy for the solvency requirements to be met (s 78C(3)(c)), it states no offence; the duty is encoded with a BREACH line that says the reduction does not take effect (or the solvency requirements are not met), as a fork.

### Not encoded, and why

- Revocation of the resolution (s 78B(6), s 78C(6)): the text puts it in the passive and names no one who revokes; the existing function `s 78B(6) the last day ...` already answers the date.
- The Registrar's recording (s 78E(5), s 78G(1)(c)): it is an effect on which the reduction's taking effect depends, not a duty with a time.
- Several applications by creditors (s 78E(3)(d), (e)): one application is the chain; for several, the rule for the lodging after the proceedings end is called on the day the last proceedings end.
- The Registrar's allowance of a longer period (s 78I(3)): taken as inputs (a Boolean and the last day), because the text gives no time for the company's request.
- Who may use each route: the chains are not gated on the kind of company (s 78B(1), s 78C(1), s 78G(1)), on s 78A(5) or on a constitution that excludes the power (s 78A(3)); the caller supplies the facts, and the module records this as a fork. The existing `may` functions take inputs the chains themselves produce, so calling them whole would be circular.
- Sections 78H(3), 78H(4)(b) and 78H(6) (the Court's direction on classes of creditors, its notices, the definition of a qualifying creditor): these are powers and definitions with no party-and-time step beyond what s 78H(2) and s 78I(2) already carry; s 78H(4)(a) is folded into the act of settling the list.
- The written-means route and the meeting route of s 78B(4)(a)(i) and (ii) as two acts: one act stands for both, as a fork.
- The existing Boolean gate `s 78B(3) the company meets the solvency requirements` and `s 78C(3)` are not called: they judge a recorded `Solvency statement` against dates, whereas the chain encodes the 20-day and 30-day windows as the clock of the resolution step.

### Differences from the existing DEONTIC

- s 78B(4)(b) and s 78C(4)(b) (`sga3-78a-78c.l4`, the rules named `... throughout the 6 weeks beginning with the resolution date`): the existing rule is two steps (MUST make available WITHIN 0, then SHANT withdraw WITHIN 41), takes only the company's name, and has no gate for the dispensation "Unless subsection (2) applies" (src:9404). The new rule is one act due by day 41 (src:9420-9423), gated by s 78B(2) or s 78C(2), with the day count computed from the resolution date by the periods module, and its BREACH line names the officers' offence of s 78B(5) (src:9425-9427), which the existing line does not.
- s 78B(4)(a) and s 78C(4)(a) (the rules named `... must make the solvency statement available ...`): the existing rules are MUST ... HENCE FULFILLED with no WITHIN, so they cannot breach, and are ungated. The new step is WITHIN 0 from the resolution ("throughout that meeting", src:9415-9418, src:9483-9487), gated by s 78B(2) or s 78C(2), with a BREACH line; the written-means and meeting routes are one act (fork).
- s 78D(4)(a) and (b) (src:9517-9523): the same MUST with no clock as the existing rules; the new ones are steps inside the chain, owed only after a creditor who is within s 78D(3) applies, where the existing rules are free-standing.
- s 78F(4) (src:9723-9725): the same 15 days (WITHIN 14, counted from the day the order is made, src:9724-9725); the new rule starts when the Court makes the order, as the next step of the chain, and its BREACH line names the officers' offence of s 78F(5) (src:9727-9728), which the existing line does not.
- s 78H(4)(a) (src:9784-9787): the existing rule is a separate MUST of the Court; the new chain folds it into the act of settling the list (s 78H(2), src:9765-9766), as a fork.
- s 78H(5) (src:9793-9805): the existing rule is a SHANT for "the person" with HENCE FULFILLED and no LEST; the new rule is a SHANT of an `Officer` (the text says "Any officer of the company") with a LEST BREACH line that states the fine and the imprisonment of src:9803-9805.
- s 78J (src:9859-9865): the existing rule is a SHANT for "the person" with no LEST; the new rule is a SHANT of a `Director` with a LEST BREACH line, and states no penalty because the text states none.
- Added in the new module and absent as DEONTIC from the existing one: the solvency statement and the special resolution with the 20-day and 30-day windows (src:9399-9400, src:9470-9471); the public company's 15 days for lodging the copy of the statement (src:9473-9476); the creditors' 6 weeks and the lodging after the end of 6 weeks and before the end of 8 weeks (src:9508-9510, src:9547-9549, src:9579-9581); the Court's decision as a MUST with the gate s 78F(2) (src:9706-9718); the lodging within 15 days beginning with the end of the proceedings (src:9618-9621, src:9670-9674); the Court-approved route with the s 78I(2) bar as a SHANT of the Court and the 90 days (src:9824-9843, src:9845-9855).

### Verification

- Unstable binary `l4-unstable-20261125-a50cbd0-darwin-arm64`: both new modules check with zero `DiagnosticSeverity_Error` and zero warnings from the new files; the 10 `#ASSERT` lines are satisfied; all 58 traces match their `-- EXPECT` lines (checked with `expect_check.py`).
- Stable binary (`~/.cache/l4-main/112/l4`): both modules check with zero errors and zero warnings from the new files; the 10 asserts are satisfied; 44 of the 58 traces match and 14 read differently (below).
- The expectations were written from the text before the first run. Two traces mismatched on the first run: one was an arithmetic slip in the trace (a public company's lodging on day 85, which is 56 days after a resolution on day 29, so after the 8 weeks; the trace was corrected to day 84, the last day), and one exposed an encoding defect, which was fixed: with the creditor's withdrawal as a ROR beside the Court's decision, a late lodging after a withdrawal left the Court's duty open and read RESIDUAL where the text puts the company in breach, so the withdrawal is now chosen by an input (a fork).
- Sensitivity: two scratch mutants, deleted afterwards. Counting 15 days as 15 days after the first day instead of 14 flipped 6 traces. Lengthening the private company's 20 days by one flipped 1 trace.
- `srcrefs.py check --refs` over both files reports 0 problems; every `-- src:` line was copied from the source file by script.

### Reads differently on the stable line

On the stable binary a MAY that lapses unexercised continues into its HENCE branch, where the unstable binary takes its LEST branch (measured: at test-file line 180, where no creditor applies, the stable result is the application branch's open duties, the creditor's service of the application; at line 293, the stable result is the open duty after the resolution although the resolution came a day too late). In this test file every trace that reaches the lodging through the creditors' window, or ends a chain at the 20-day or 30-day window, therefore reads RESIDUAL there. The 14 traces:

- test-file line 180: expected FULFILLED, MAIN prints RESIDUAL: No application: the company lodges on day 42, the first day after the 6 weeks.
- test-file line 185: expected FULFILLED, MAIN prints RESIDUAL: No application: the company lodges on day 55, the last day before the end of the 8 weeks.
- test-file line 190: expected BREACH, MAIN prints RESIDUAL: No application: the company lodges on day 56, after the 8 weeks.
- test-file line 195: expected BREACH, MAIN prints RESIDUAL: The company lodges on day 41, the last day of the 6 weeks: not after the end of 6 weeks, so the lodging does not count, and none follows.
- test-file line 225: expected FULFILLED, MAIN prints RESIDUAL: An application on day 42 is after the 6 weeks: it is not an application "during the 6 weeks", so the company lodges on day 50 as if none had been made
- test-file line 247: expected FULFILLED, MAIN prints RESIDUAL: A private company: the statement at the meeting on day 0, kept open to day 41, the documents lodged on day 50.
- test-file line 261: expected FULFILLED, MAIN prints RESIDUAL: A public company: the copy of the statement is lodged with the Registrar on day 14, the last day of the 15 days beginning with the resolution date.
- test-file line 277: expected FULFILLED, MAIN prints RESIDUAL: Gate fails: no cash or assets and no release, so s 78B(2) applies; only the lodging after the creditors' 6 weeks is owed.
- test-file line 282: expected FULFILLED, MAIN prints RESIDUAL: Gate fails for a public company: s 78C(2) applies, so it owes no copy for the Registrar and no statement at the meeting.
- test-file line 291: expected FULFILLED, MAIN prints RESIDUAL: A private company: statement on day 0, resolution on day 19 (the last day of the period of 20 days beginning with the statement), the statement at the
- test-file line 300: expected FULFILLED, MAIN prints RESIDUAL: The resolution on day 20 is after the 20 days: the statement was made before the beginning of the period of 20 days ending with the resolution date, s
- test-file line 306: expected FULFILLED, MAIN prints RESIDUAL: A public company has 30 days: statement on day 0, resolution on day 29, the copy lodged with the Registrar on day 43, kept open to day 70, lodged on d
- test-file line 316: expected FULFILLED, MAIN prints RESIDUAL: A public company's resolution on day 30 is after the 30 days.
- test-file line 322: expected FULFILLED, MAIN prints RESIDUAL: Gate fails: no cash or assets and no release, so no statement is needed; the resolution on day 3, lodged on day 53 (the creditors' period needs no app

The module is therefore verified on the unstable binary; on the stable line, in these tests, the traces of the duties that do not rest on a lapsed MAY (the 6 weeks open to creditors, the 15-day notices and lodgings, the Court-approved route with its 90 days, the prohibitions, and a creditor's application in time) match, and the traces that rest on a lapsed MAY (the creditors' window and the 20-day and 30-day windows) do not.
