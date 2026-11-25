## Procedure layer: derivative claims in England and Wales and Northern Ireland (ss 260 to 264)

The procedure that Companies Act 2006 ss 260 to 264 lays down when a member applies for permission (in Northern Ireland, leave) to continue a derivative claim, written as regulative rules over the Boolean encoding in `coa5-derivative-claims.l4`.

Files: `coa-proc-derivative-claims.l4` (20 DEONTIC rules and 4 Boolean helpers) and `coa-proc-derivative-claims-tests.l4` (60 traces and 13 assertions).
Source lines 3379-3465 of `ukpga-2006-46.txt`; Chapter 2 (ss 265 to 269, Scotland) is not encoded here.
No existing module is edited; the new module imports `coa5-derivative-claims` and calls its functions as gates, and never calls its DEONTIC for s 261(1).

### The text states no time limit

Nothing in ss 261 to 264 gives a period: not for the application, not for the court's dismissal, directions, adjournment or hearing, and not for the company's evidence (the court's directions fix that).
The text states no consequence of a member's not applying, or of a court's inaction, either.
So no rule has a WITHIN, and no rule has a LEST that a clock would reach: a duty or power not yet used stays open (RESIDUAL) however long the trace waits, and an event on day 3 and the same event on day 1000 are alike.

### The seat of each rule

| rule | seat | what it does |
| --- | --- | --- |
| `s 261(1) the member's step of applying for permission to continue the derivative claim` | s 261(1) (src:3394-3395) | a MUST of the member who brings the claim, gated by the existing s 261(1) function; no clock, no breach clause |
| `s 261(2)(a) the court's step of dismissing an application that discloses no prima facie case` | s 261(2)(a) (src:3396-3398) | a MUST of the court, gated by the court's view that no prima facie case is disclosed (an input) |
| `s 261(2)(b) the court's power to make a consequential order after a dismissal` | s 261(2)(b) (src:3396-3398) | a MAY of the court, open only where the court must dismiss |
| `s 261(3)(a) the court's power to give directions as to the evidence to be provided by the company` | s 261(3)(a) (src:3399-3401) | a MAY of the court, open only where the application is not dismissed |
| `s 261(3)(b) the court's power to adjourn the proceedings to enable the evidence to be obtained` | s 261(3)(b) (src:3399-3401) | a MAY of the court, open only where the application is not dismissed |
| `s 261(4) the court's step on hearing the application` | s 261(4), s 263(1)-(2) (src:3402-3405, 3424-3431) | on a hearing, three MAYs in a ROR (give permission, refuse and dismiss, adjourn with directions); where s 263(2) requires refusal, a MUST to refuse instead |
| `s 263(2) the court's bar on giving permission (or leave) on an application under section 261` | s 263(2) (src:3424-3431) | a SHANT on the court giving permission, with a BREACH if it does, open only where s 263(2) requires refusal |
| `s 262(2) the member's power to apply for permission to continue the company's claim as a derivative claim` | s 262(1)-(2) (src:3406-3413) | a MAY of the member, gated by the existing s 262(1) and s 262(2) functions (the company has brought a claim; the three grounds) |
| `s 262(3)(a) / s 262(3)(b) / s 262(4)(a) / s 262(4)(b) / s 262(5) / s 263(2) bar (six rules)` | s 262(3)-(5), s 263(2) (src:3414-3423, 3424-3431) | the same five court steps and the bar as for s 261, gated by the s 262 functions |
| `s 264(2) another member's power to apply for permission to continue the claim` | s 264(1)-(2) (src:3447-3455) | a MAY of the other member, gated by the existing s 264(1) and s 264(2) functions (three ways the claimant came to hold the claim; the three grounds) |
| `s 264(3)(a) / s 264(3)(b) / s 264(4)(a) / s 264(4)(b) / s 264(5) (five rules)` | s 264(3)-(5) (src:3456-3465) | the same four court steps and the hearing as for s 261, with no s 263(2) refusal and no bar (see the fork on s 263(1)) |

Boolean helpers: `s 261(4)`, `s 262(5)` and `s 264(5)` `the court is hearing the application and each of its three courses is open` (the existing function answers for one course at a time), and `s 263(1)-(2) permission (or leave) must be refused on an application under section 261 or 262` (calls the existing s 263(1) and s 263(2) functions; the s 263(1) function gets the constant TRUE, because the helper is used only on applications under s 261 or 262).

The court's route is encoded as separate DEONTICs, one per step, each with its own day 0, and not as the next step of the member's rule.
The court's finding at each step is an input to that step's rule.
The reason is the one measured in `coa-proc-register-copy.l4`: the court's alternative outcomes written as MAY events in a ROR do not commit to the branch whose event happened.

### Why the bar on giving permission is its own rule

A MUST whose trace shows a different act stays open: in the trace where the court is satisfied under s 263(2)(a) and adjourns instead of refusing, the duty to refuse stays owed (RESIDUAL) on both binaries, so a court that gives permission when s 263(2) requires refusal would not show as a breach under the MUST alone.
In a scratch probe on both binaries (deleted), a RAND of `MUST refuse` and `SHANT give permission` printed `FULFILLED AND PARTY ... MUST NOT ...` once the court had refused, because a prohibition with no clock never completes; that reads as still open, not as fulfilled.
So the duty to refuse and the bar are two rules, and the trace of the bar shows BREACH when permission is given and RESIDUAL otherwise.

### TIMELINE lines

- `s 261(1) the member's step of applying for permission to continue the derivative claim`: `TIMELINE: unit=none; day 0=the day the member brings the derivative claim; counting=silent (s 261(1) says "must apply" and gives no time and no consequence, so no clock is encoded and the application stays owed until the trace shows it)`
- `s 261(2)(a) the court's step of dismissing an application that discloses no prima facie case`: `TIMELINE: unit=none; day 0=the day it appears to the court that the application and the evidence disclose no prima facie case; counting=silent (s 261(2) says "must dismiss" and gives no time, so no clock is encoded and the duty stays owed until the trace shows it done)`
- `s 261(2)(b) the court's power to make a consequential order after a dismissal`: `TIMELINE: unit=none; day 0=the day the court dismisses the application; counting=silent (s 261(2)(b) says "may make any consequential order it considers appropriate" and gives no time, so no clock is encoded and the power stays open until the trace shows it used)`
- `s 261(3)(a) the court's power to give directions as to the evidence to be provided by the company`: `TIMELINE: unit=none; day 0=the day the court decides not to dismiss the application; counting=silent (s 261(3)(a) says "may give directions" and gives no time, so no clock is encoded)`
- `s 261(3)(b) the court's power to adjourn the proceedings to enable the evidence to be obtained`: `TIMELINE: unit=none; day 0=the day the court decides not to dismiss the application; counting=silent (s 261(3)(b) says "may adjourn the proceedings" and gives no time, so no clock is encoded)`
- `s 261(4) the court's step on hearing the application`: `TIMELINE: unit=none; day 0=the day the court hears the application; counting=silent (s 261(4) says "On hearing the application, the court may" and gives no time, so no clock is encoded; an adjournment under (c) is followed by a fresh run of this rule from the day the hearing resumes)`
- `s 263(2) the court's bar on giving permission (or leave) on an application under section 261`: `TIMELINE: unit=none; day 0=the day the court hears the application; counting=silent (s 263(2) says "must be refused" and gives no time, so no clock is encoded: the bar is never lifted by waiting, and the trace stays open until the court gives permission, which is the breach)`
- `s 262(2) the member's power to apply for permission to continue the company's claim as a derivative claim`: `TIMELINE: unit=none; day 0=the day the company has brought a claim that could be pursued as a derivative claim; counting=silent (s 262(2) says "may apply" and gives no time, so no clock is encoded and the power stays open until the trace shows it used)`
- `s 262(3)(a) the court's step of dismissing an application that discloses no prima facie case`: `TIMELINE: unit=none; day 0=the day it appears to the court that the application and the evidence disclose no prima facie case; counting=silent (s 262(3) says "must dismiss" and gives no time, so no clock is encoded and the duty stays owed until the trace shows it done)`
- `s 262(3)(b) the court's power to make a consequential order after a dismissal`: `TIMELINE: unit=none; day 0=the day the court dismisses the application; counting=silent (s 262(3)(b) says "may make any consequential order it considers appropriate" and gives no time, so no clock is encoded and the power stays open until the trace shows it used)`
- `s 262(4)(a) the court's power to give directions as to the evidence to be provided by the company`: `TIMELINE: unit=none; day 0=the day the court decides not to dismiss the application; counting=silent (s 262(4)(a) says "may give directions" and gives no time, so no clock is encoded)`
- `s 262(4)(b) the court's power to adjourn the proceedings to enable the evidence to be obtained`: `TIMELINE: unit=none; day 0=the day the court decides not to dismiss the application; counting=silent (s 262(4)(b) says "may adjourn the proceedings" and gives no time, so no clock is encoded)`
- `s 262(5) the court's step on hearing the application`: `TIMELINE: unit=none; day 0=the day the court hears the application; counting=silent (s 262(5) says "On hearing the application, the court may" and gives no time, so no clock is encoded; an adjournment under (c) is followed by a fresh run of this rule from the day the hearing resumes)`
- `s 263(2) the court's bar on giving permission (or leave) on an application under section 262`: `TIMELINE: unit=none; day 0=the day the court hears the application; counting=silent (s 263(2) says "must be refused" and gives no time, so no clock is encoded: the bar is never lifted by waiting, and the trace stays open until the court gives permission, which is the breach)`
- `s 264(2) another member's power to apply for permission to continue the claim`: `TIMELINE: unit=none; day 0=the day the claimant has brought or continued the derivative claim; counting=silent (s 264(2) says "may apply" and gives no time, so no clock is encoded and the power stays open until the trace shows it used)`
- `s 264(3)(a) the court's step of dismissing an application that discloses no prima facie case`: `TIMELINE: unit=none; day 0=the day it appears to the court that the application and the evidence disclose no prima facie case; counting=silent (s 264(3) says "must dismiss" and gives no time, so no clock is encoded and the duty stays owed until the trace shows it done)`
- `s 264(3)(b) the court's power to make a consequential order after a dismissal`: `TIMELINE: unit=none; day 0=the day the court dismisses the application; counting=silent (s 264(3)(b) says "may make any consequential order it considers appropriate" and gives no time, so no clock is encoded and the power stays open until the trace shows it used)`
- `s 264(4)(a) the court's power to give directions as to the evidence to be provided by the company`: `TIMELINE: unit=none; day 0=the day the court decides not to dismiss the application; counting=silent (s 264(4)(a) says "may give directions" and gives no time, so no clock is encoded)`
- `s 264(4)(b) the court's power to adjourn the proceedings to enable the evidence to be obtained`: `TIMELINE: unit=none; day 0=the day the court decides not to dismiss the application; counting=silent (s 264(4)(b) says "may adjourn the proceedings" and gives no time, so no clock is encoded)`
- `s 264(5) the court's step on hearing the application`: `TIMELINE: unit=none; day 0=the day the court hears the application; counting=silent (s 264(5) says "On hearing the application, the court may" and gives no time, so no clock is encoded; an adjournment under (c) is followed by a fresh run of this rule from the day the hearing resumes)`

### Forks

- `FORK: s 263(1) "under section 261 or 262" | s 263 has effect on an application under s 261 or s 262 and, on the words of s 263(1), not on another member's application under s 264, so the refusal below is encoded for ss 261 and 262 only | s 263 governs the s 264 application as well`
- `FORK: s 261(1) "must apply" | a duty of the member with no clock and no breach clause: the text states neither a time nor a consequence, so the rule has no WITHIN and no LEST | the missed application is a breach (the existing rule for s 261(1) says so, but its LEST can never be reached without a deadline)`
- `FORK: s 261(2) "it appears to the court" | the court's view is an input to the rule, and the duty to dismiss arises when the input is true | the duty arises only once the court has stated its view in a decision`
- `FORK: s 261(2)(b) "may make any consequential order" | a separate power of the court, open only where the court must dismiss, and not a condition of the dismissal being complete | the consequential order is the next step of the dismissal, so a dismissal with no order is unfinished`
- `FORK: s 261(3)(a) "directions as to the evidence to be provided by the company" | only the court's power to give the direction is encoded: the text lays no duty on the company and no time for its evidence, which the court's own directions set | the company's duty to provide the evidence is a rule of this section`
- `FORK: s 261(3) (a) and (b) | two separate powers, each its own rule, so that using one does not finish the other | one rule offering both`
- `FORK: s 263(2) "must be refused" | where the court is satisfied of a matter in s 263(2) the only step the rule offers is the refusal of s 261(4)(b), as a duty (MUST), and giving permission is barred by the separate rule after this one; adjourning is not offered once the court is satisfied | the court may still adjourn under s 261(4)(c) and refuse later`
- `FORK: s 261(4)(a) "on such terms as it thinks fit" | the terms are not modelled: giving permission is one act | each term is a further step`
- `FORK: s 263(2) "must be refused" | the bar is its own rule (SHANT give permission), beside the duty to refuse in the rule above, because a prohibition with no clock never completes and would keep a RAND of the two open after the court had refused | one rule, the duty and the bar together`
- `FORK: s 262(2) "on the ground that (a) ..., (b) ..., and (c)" | all three grounds are needed, as the existing function reads the list joined by "and" | (a) or (b), together with (c)`
- `FORK: s 262(3) "it appears to the court" | the court's view is an input to the rule, and the duty to dismiss arises when the input is true | the duty arises only once the court has stated its view in a decision`
- `FORK: s 262(3)(b) "may make any consequential order" | a separate power of the court, open only where the court must dismiss, and not a condition of the dismissal being complete | the consequential order is the next step of the dismissal, so a dismissal with no order is unfinished`
- `FORK: s 262(4)(a) "directions as to the evidence to be provided by the company" | only the court's power to give the direction is encoded: the text lays no duty on the company and no time for its evidence, which the court's own directions set | the company's duty to provide the evidence is a rule of this section`
- `FORK: s 262(4) (a) and (b) | two separate powers, each its own rule, so that using one does not finish the other | one rule offering both`
- `FORK: s 263(2) "must be refused" | where the court is satisfied of a matter in s 263(2) the only step the rule offers is the refusal of s 262(5)(b), as a duty (MUST), and giving permission is barred by the separate rule after this one; adjourning is not offered once the court is satisfied | the court may still adjourn under s 262(5)(c) and refuse later`
- `FORK: s 262(5)(a) "on such terms as it thinks fit" | the terms are not modelled: giving permission is one act | each term is a further step`
- `FORK: s 263(2) "must be refused" | the bar is its own rule (SHANT give permission), beside the duty to refuse in the rule above, because a prohibition with no clock never completes and would keep a RAND of the two open after the court had refused | one rule, the duty and the bar together`
- `FORK: s 264(2) "on the ground that (a) ..., (b) ..., and (c)" | all three grounds are needed, as the existing function reads the list joined by "and" | (a) or (b), together with (c)`
- `FORK: s 264(3) "it appears to the court" | the court's view is an input to the rule, and the duty to dismiss arises when the input is true | the duty arises only once the court has stated its view in a decision`
- `FORK: s 264(3)(b) "may make any consequential order" | a separate power of the court, open only where the court must dismiss, and not a condition of the dismissal being complete | the consequential order is the next step of the dismissal, so a dismissal with no order is unfinished`
- `FORK: s 264(4)(a) "directions as to the evidence to be provided by the company" | only the court's power to give the direction is encoded: the text lays no duty on the company and no time for its evidence, which the court's own directions set | the company's duty to provide the evidence is a rule of this section`
- `FORK: s 264(4) (a) and (b) | two separate powers, each its own rule, so that using one does not finish the other | one rule offering both`
- `FORK: s 263(1) "under section 261 or 262" | on the words of s 263(1) the refusal of s 263(2) is not applied to an application under s 264, so the three courses are all open to the court | s 263(2) refuses permission on this application too`
- `FORK: s 264(5)(a) "on such terms as it thinks fit" | the terms are not modelled: giving permission is one act | each term is a further step`

### Differences from the existing DEONTIC

The existing DEONTIC is `s 261(1) the member's duty to apply for permission to continue the claim` (`coa5-derivative-claims.l4:131-137`; the other DEONTIC in that file, at :712, is s 266 and out of scope).
Section 261(1) is written again here from the text, without calling the existing rule, and the two were compared by reading the code and by running the existing rule on two traces in a scratch probe (deleted).

- **A gate.** The existing rule has no gate: the member MUST apply in every trace, even where no derivative claim is brought.
  The new rule opens only where the existing function says the member must apply (`a member of a company brings a derivative claim under this Chapter`), and otherwise is FULFILLED.
  The source line that decides it is src:3395, "A member of a company who brings a derivative claim under this Chapter must apply": the duty is limited by the relative clause.
- **A breach clause that cannot fire.** The existing rule ends `LEST BREACH BY Member BECAUSE "... (the text states no consequence)"` with no WITHIN, so time alone never reaches it; unstable's lint says so (`lint/lest-without-deadline`, at `coa5-derivative-claims.l4` lines 136 and 717, the second being s 266).
  The new rule has no LEST, because src:3395 states no consequence and no time.
  The behaviour does not differ where the gate holds: a trace in which the member has not applied stays open (RESIDUAL; waited to day 10 on the existing rule, to day 30 on the new rule), and a trace in which the member applies on day 3 is FULFILLED on both (measured on unstable a50cbd0 and main 112).
- **The party.** The existing rule uses `Member` from `coa-core`; the new rule uses its own party enum so that the court's steps, which the text gives in the same sections (src:3396-3405), are in one enum with the member's.
- **The reach.** The existing DEONTIC covers only the duty to apply; the court's steps (s 261(2) to (4)), s 262, s 263(2) and s 264 are new here (src:3396-3465).

The unstable build prints two `lint/lest-without-deadline` warnings, both from `coa5-derivative-claims.l4`, which is not edited here: its two LESTs (lines 136 and 717) cannot be reached without a deadline.
No warning comes from the new files.

### What the text leaves silent (no clock, no consequence encoded)

- Any time limit for the application (s 261(1), s 262(2), s 264(2)), for the court's dismissal, directions, adjournment or hearing (s 261(2) to (4) and their counterparts), and for the company's evidence.
- Any consequence of a member's not applying, and of the court's not acting.
- The company's duty to provide the evidence the court's directions ask for: s 261(3)(a) says only that the court may give the directions.
- The terms on which permission is given ("on such terms as it thinks fit"): giving permission is one act.
- What follows an adjournment: each resumed hearing is a fresh run of the hearing rule from its own day 0.

### What was not encoded, and why

- s 260 (what a derivative claim is, the routes by which one may be brought, the persons it may be against, who counts as a member or director): scope and definitions, not steps in a procedure; they stay Boolean in `coa5-derivative-claims.l4`, and whether a member brings a derivative claim under the Chapter is an input to the member's rule (the argument of the existing s 261(1) function).
- s 263(3) and (4) (matters the court must take into account, and particular regard to the views of disinterested members): the court's reasoning, with no act or party event to put in a trace.
- s 263(5) to (7) (the Secretary of State's power to amend s 263(2) and (3) by regulations, the duty to consult, the affirmative resolution procedure): machinery, no time, no step in a claim.
- s 260(2)(b) (a derivative claim brought in pursuance of an order under s 994): another section's procedure.
- Chapter 2, ss 265 to 269 (Scotland): outside the unit.

### Verification

- Both binaries: the unstable build `l4-unstable-20261125-a50cbd0` and main 112 (`~/.cache/l4-main/112/l4`), run from this folder with `JL4_LIBRARY_PATH` unset.
- Both check the module and the tests with no `DiagnosticSeverity_Error` and no warning from the new files; all 13 assertions are satisfied on both.
- `expect_check.py` matched 60 of 60 traces on unstable and 60 of 60 on main; every EXPECT was written from the text before the run, and every one of the 20 rules has at least one trace in which it acts and one in which its gate fails.
- Two mutated scratch copies, deleted afterwards, run on the first 40 traces (before the traces for the remaining rules of ss 262 and 264 were added): with the s 263(2) refusal switched off in the hearing rules, one trace changed class (the court adjourns although satisfied under s 263(2)(a): expected RESIDUAL, got FULFILLED), and with the bar's gate switched off, three did (both BREACH traces and the open bar trace).

### READS-DIFFERENTLY-ON-MAIN

No trace differs in class between the two binaries.
One Result block prints differently, with the same class on both: the open bar of s 263(2) on an application under s 261 (RESIDUAL); unstable prints the LEST with its BREACH in parentheses, main without.
