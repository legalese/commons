## Procedure layer: a director's interest in a transaction, and loans to directors (ss 177, 182 to 184, 197, 204, 207, 213 and 214)

The procedure that Companies Act 2006 ss 177, 182 to 184, 197, 213 and 214 lay down for a director who is interested in a transaction with the company and for a loan to a director, written as regulative rules over the Boolean encoding in `coa4-general-duties.l4`, `coa4-declaration.l4`, `coa4-approval-loans.l4` and `coa5-loans-exceptions.l4`.

Files: `coa-proc-director-interests.l4` (the rules) and `coa-proc-director-interests-tests.l4` (51 traces and 14 assertions).
Source lines 2364-2380, 2413-2445, 2570-2587, 2687-2696, 2729-2737 and 2796-2821 of `ukpga-2006-46.txt`.
No existing module is edited; the new module imports `coa-core`, `daydate` and the four modules above and calls their functions as gates.
The two regulative rules those modules already hold (`coa4-general-duties.l4` lines 551-555 for s 177, `coa4-declaration.l4` lines 164-168 for s 182) are neither called nor changed.
The comparison with those two is in the section "Differences from the existing DEONTIC" below.

### The seat of each rule

| rule | seat | what it does |
| --- | --- | --- |
| `s 177(4) the company has not yet entered into the transaction on the day the duty to declare arises` and `s 177(4) the last day for the declaration, counted from day 0` (helpers, not DEONTICs) | s 177(1) "proposed transaction", s 177(4) (src:2372) | turn the day of entry and day 0 into a yes/no and a number of days |
| `s 177(1) and (4) the director's duty to declare before the company enters into the transaction` | s 177(1), (4), gated by s 177(1) with the answers under s 177(5) and (6) (src:2364-2365, 2372) | MUST declare, WITHIN the days before the day of entry, LEST BREACH |
| `s 177(3) and (4) the director's duty to make a further declaration before the company enters into the transaction` | s 177(3), (4) (src:2371-2372) | the same limit for a further declaration, from the day the declaration proves inaccurate or incomplete |
| `s 182(4) the days allowed, counted from day 0` (helper) | s 182(4) (src:2421) | turns the caller's last day into a number of days; a last day before day 0 is read as day 0 |
| `s 182(4) and s 183(1) the director's duty to declare as soon as is reasonably practicable` | s 182(1), (2), (4), s 183(1) (src:2413-2419, 2421, 2431-2432) | MUST declare at a meeting, by notice in writing or by general notice (ROR), WITHIN the caller's days, LEST BREACH; the breach is the failure that s 183(1) makes an offence |
| `s 182(1) the director's underlying duty to declare, which a late declaration still discharges` | s 182(1), (2), (4) second sentence (src:2413-2419, 2422) | the same three ways, no clock: a late declaration still discharges it |
| `s 204 the exception for expenditure on company business disapplies the requirement of approval` and `s 207(1) the exception for a small loan disapplies the requirement of approval` (helpers, not DEONTICs) | s 204(1), (2), s 207(1) (src:2687-2696, 2729-2733) | turn the existing answers (JUST FALSE for s 204, JUST TRUE for s 207) into one plain yes/no, to feed the gate of s 197(1) |
| `s 197(1) the company's duty not to make or secure a loan to a director without the members' approval` | s 197(1), (2) (src:2570-2575) | SHANT on the company, gated by the existing bar of s 197(1) or by the answer under s 197(2); no clock |
| `s 197(3) the members' duty not to pass the resolution without the memorandum made available` | s 197(3), (4) (src:2576-2584) | SHANT on the members, gated by the existing s 197(3) function answering JUST FALSE |
| `s 213(2) the company's power to avoid the transaction or arrangement` | s 213(2) with s 214 (src:2798-2801, 2818-2821) | MAY (the company), gated by the existing s 213(2) function and by the answer under s 214; no clock |
| `s 213(3) the duty of each person liable to account for the gain and indemnify the company` | s 213(3) to (7) (src:2802-2815) | MUST account and MUST indemnify (RAND), each only where there is a gain or a loss; no clock |
| `s 214 the members' power to affirm the transaction or arrangement` | s 214 (src:2818-2821) | MAY (the members), WITHIN the caller's days, LEST FULFILLED |

Each time-limited rule carries a `-- TIMELINE:` line above it with the unit, day 0 and the counting rule.
The offence of s 183(1) is the BREACH of the timing rule of s 182(4), named in the BECAUSE; the penalty of s 183(2) stays the `Penalty` function in `coa4-declaration.l4`.
The consequences of a loan made in contravention (ss 213 and 214) are separate rules from the s 197(1) prohibition: the avoidance power, the liability, and the affirmation each stand alone, and the s 197(1) BECAUSE names them.

### The TIMELINE lines, verbatim from the module

- `s 177(1) and (4) the director's duty to declare before the company enters into the transaction`
  `-- TIMELINE: unit=calendar day; day 0=the day the director's duty to declare arises (the director is interested in the proposed transaction and aware of it, s 177(5)); counting="before the company enters into the transaction or arrangement" (the last day is the day before the day of entry, see the FORK above)`
- `s 177(3) and (4) the director's duty to make a further declaration before the company enters into the transaction`
  `-- TIMELINE: unit=calendar day; day 0=the day the declaration proves to be, or becomes, inaccurate or incomplete; counting="before the company enters into the transaction or arrangement" (s 177(4) says "any declaration required by this section", so the same limit applies to the further declaration)`
- `s 182(4) and s 183(1) the director's duty to declare as soon as is reasonably practicable`
  `-- TIMELINE: unit=calendar day; day 0=the day the director's duty to declare arises (the company has entered into the transaction and the director is, or is treated as, aware of the interest and of the transaction, s 182(5)); counting="as soon as is reasonably practicable" (the Act gives no number: the last day is a date the caller supplies as a judgment, and a declaration on that day is in time)`
- `s 182(1) the director's underlying duty to declare, which a late declaration still discharges`
  `-- TIMELINE: unit=none; day 0=the day the director's duty to declare arises; counting=silent (s 182(4) says that failure to declare as soon as is reasonably practicable "does not affect the underlying duty to make the declaration", so no clock ends this duty: it stays owed until the declaration is made, however late)`
- `s 197(1) the company's duty not to make or secure a loan to a director without the members' approval`
  `-- TIMELINE: unit=none; day 0=not applicable; counting=silent (s 197(1) says the company "may not" make the loan unless approved and gives no time: the prohibition is open until the trace shows the company acting)`
- `s 197(3) the members' duty not to pass the resolution without the memorandum made available`
  `-- TIMELINE: unit=calendar day; day 0=the first day on which the memorandum is available for inspection at the company's registered office (for a resolution at a meeting); counting="not less than 15 days ending with the date of the meeting" (counted inclusively, so a memorandum first available 14 days before the meeting has been available for 15 days ending with the meeting day; the existing function s 197(3) holds the count and is the gate)`
- `s 213(2) the company's power to avoid the transaction or arrangement`
  `-- TIMELINE: unit=none; day 0=the day the company enters into the transaction in contravention; counting=silent (s 213(2) gives the company no time in which to avoid it; the only limit is that s 214 ends the power on an affirmation "within a reasonable period", which enters here as an input and not as a clock)`
- `s 213(3) the duty of each person liable to account for the gain and indemnify the company`
  `-- TIMELINE: unit=none; day 0=the day the company enters into the transaction in contravention; counting="whether or not the transaction or arrangement has been avoided" (s 213(3) gives no time and says the liability does not depend on avoidance, so no clock runs and an affirmation under s 214 does not end it)`
- `s 214 the members' power to affirm the transaction or arrangement`
  `-- TIMELINE: unit=calendar day; day 0=the day the company enters into the transaction in contravention; counting="within a reasonable period" (the Act gives no number: the last day is a date the caller supplies as a judgment, and an affirmation on that day is in time)`

The s 214 day count (30 days from 1 March to a last day of 31 March) is checked by the `#ASSERT` on its helper and not by a trace at its edge: the trace that waits to day 10 shows the power still open (RESIDUAL, printed `WITHIN 20`), and an affirmation on day 31 and a wait to day 31 both end FULFILLED on both binaries, as an affirmation on day 30 does.

### The forks

Each is also a `-- FORK:` line in the module.

- s 177(4) "before the company enters into": a declaration on the day of entry is too late (the last day is the day before it); the other reading lets a declaration on the day of entry, before entry that day, be in time.
- s 177(1) "proposed transaction": s 177 applies only while the company has not yet entered into it, so where the day of entry is not later than day 0 the rule gives no duty and s 182 governs; the other reading treats that as a breach.
- s 177(3): a further declaration is owed before the day of entry; the other reading lets it be made after entry.
- s 182(4) "as soon as is reasonably practicable": the caller's last day is the clock; the other reading is that the text gives no day and the rule has no clock.
- s 183(1): the offence is the breach of the timing rule; the other reading is that it is committed only if the declaration is never made.
- s 204(2): the exception applies only while the aggregate does not exceed 50,000 pounds.
- s 197(2): the answer under s 197(2) is an input and either bar makes the company's act a breach; the other reading is a separate rule.
- s 197(3): the prohibition is on the members, and a resolution passed without the memorandum still counts as an approval for the company's rule (the Act states no other consequence); the other reading is that such a resolution is no approval.
- s 213(3): a limb is owed only where the trace states a gain or a loss; the other reading is that both are owed whatever the amount.
- s 214 "within a reasonable period": the members may affirm up to and including the caller's last day; the other reading is that the period is open-ended.
- s 214 "the members of the company": one rule for the company's members; the holding company's members (s 214(b)) are the same rule run again, the other reading is a second rule.

### What the text leaves silent

- No time for a declaration under s 182 in days, and no end to the underlying duty (src:2421, 2422).
- No time in which the company may avoid under s 213(2), and no time for the account or the indemnity under s 213(3) (src:2798-2804).
- No time for the company's prohibition under s 197(1) beyond "may not" (src:2571).
- Whether a resolution passed without the memorandum is valid (src:2576): the Act says only that it "must not be passed".
- The length of "a reasonable period" in s 214 (src:2818).
- No offence is stated for a breach of s 177; its BECAUSE says the consequences are those of the general duties (s 178).

### Differences from the existing DEONTIC

The existing rule for s 177 is `s 177(1) the director's duty to declare the interest to the other directors` (`coa4-general-duties.l4:551-555`): `PARTY Director MUST ... HENCE FULFILLED`, with the action's text "declare the nature and extent of the interest to the other directors before the company enters into the transaction or arrangement".
The existing rule for s 182 is `s 182 the director's duty to declare the interest to the other directors` (`coa4-declaration.l4:164-168`): the same shape, with the text "as soon as is reasonably practicable".
The new rules differ in these ways, each decided by the source line named.

| difference | existing rule | new rules | deciding source line |
| --- | --- | --- | --- |
| gate | none: the duty is owed in every case | s 177(1) and s 182(1) functions with the answers under (5) and (6): a director who is not aware, or need not declare, owes nothing | src:2373 (s 177(5)), src:2375-2380 (s 177(6)), src:2423-2430 |
| clock for s 177 | none: "before the company enters into" is in the text of the action only | a limit in days from day 0 to the day before the day of entry, from two dates | src:2372 |
| clock for s 182 | none: "as soon as is reasonably practicable" is in the text of the action only | the caller's last day, as a limit in days | src:2421 |
| a missed time | no BREACH | LEST BREACH BY the director; for s 182 the breach names the offence of s 183(1) | src:2431-2432 |
| the underlying duty after a late declaration | not modelled | a second rule for s 182 with no clock: a late declaration is a breach of the timing rule and still discharges the underlying duty; no declaration leaves the timing rule breached and this one open | src:2422 |
| manner of declaring, s 182 | one action | three alternatives (meeting, notice in writing, general notice), because s 182(2) says the declaration "must be made" in one of them | src:2416-2419 |
| manner of declaring, s 177 | one action | one action: s 177(2) says the declaration "may (but need not)" be made in those ways, so the manner does not matter | src:2366-2370 |
| s 177(3) further declaration | not modelled | a separate rule with its own day 0 | src:2371 |
| the person bound | `Director` | `ss 177-214 the director` | src:2365, 2414 |

### Which binary verified the traces

`expect_check.py` run with the unstable build (a50cbd0, 25 November 2026) and with main (112): all 51 traces match their `-- EXPECT` line on both.
Both binaries show zero errors and zero warnings on the module and on the test file, and all 14 assertions are satisfied on both.
A sensitivity check on one scratch copy of the module with three changes (the last day for the s 177 declaration moved by one day; the two limbs of s 213(3) joined by ROR instead of RAND; the s 214 limit set to 0 days) made four traces mismatch their EXPECT (the two s 177 entry-day traces, the s 213(3) one-limb trace, and the s 214 trace that waits to day 10); the copy is deleted.

### READS-DIFFERENTLY-ON-MAIN

No trace differs in class.
Four traces print differently on main with the same class on both: the two `s 182(4) and s 183(1)` traces that breach (three breaching alternatives of a ROR, joined with BY on unstable and with OR DEONTIC BREACHED on main), and the two traces with an open prohibition (`s 197(1)` and `s 197(3)`; unstable prints the LEST BREACH in parentheses, main without).
The list is also at the end of the test file.

### What is not encoded, and why

- s 184(5) (a notice in writing is deemed part of the proceedings of the next directors' meeting, and s 248 applies): a deeming rule that binds no person and runs no time; s 248 (minutes) is outside the lines of this unit. It stays Boolean in `coa4-declaration.l4`.
- s 182(3) (a further declaration after entry) and s 185 (general notice): no new time or party; s 177(3) is encoded as the model.
- s 183(2) (the penalty): stays the `Penalty` function.
- ss 205, 206, 208 and 209 (the other exceptions): one input to the s 197(1) rule says whether any of them applies; ss 204 and 207(1) are the two exceptions taken as gates here.
- s 207(2) and (3) and the rest of ss 198 to 203 (quasi-loans and credit transactions): outside this unit.
- The holding company's separate approval under s 197(2) beyond its answer taken as an input to the s 197(1) rule, and s 197(5) beyond the input the existing function takes.
- The amounts of the gain and the loss (s 213(3)(a), (b)): Boolean already in `coa5-loans-exceptions.l4`.
- ss 190 and 195 (substantial property transactions): not part of this layer.
