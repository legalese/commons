# Vigilante Corps Act 1967 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
conventions of the example rows and nothing else. No pipeline, no coverage table,
no independent test pass, no human gate. Not for public use.

**Edition:** 2020 Revised Edition, as deposited at
`../../registers/source-bundle/VCA1967.txt`. The deposit says it "incorporates all
amendments up to and including 1 December 2021 and comes into operation on
31 December 2021". No later amendment is annotated in the text; the meta file records
it as the current version as at 1 October 2026. The arrangement of sections at the
top of the deposit is one number out of step with the body (it lists "2. Short
title"); the encoding follows the body.

**Checks:** one module, one case file, 56 assertions satisfied, 0 errors, 0 warnings.

## Why this Act, and why scoped

This Act is requirement **REQ-0133** in `subjects/sg/requirements.jsonl`: Tier 2 of
the remaining Singapore Acts, ordered by everyday-life relevance. The requirement
asks what the Act decides for a person it applies to; no scenario has asked a sharper
question yet. The person it applies to is a member of the Corps, so this row takes
what a member meets: the oath and certificate (ss 10, 11), resignation and discharge
(ss 12, 23), returning and looking after Government property (ss 13, 26), desertion
(s 14), disciplinary punishments, compensation, prosecution and appeals (ss 16 to 18,
22, 24), threatening or insulting (s 25), witnesses (s 27), deductions from pay
(ss 29, 30) and outside work by a full-time member (Schedule item 27).

Not encoded: the raising, functions, units and disbandment of the Corps (ss 3 to 9),
the start and place of detention and persons unlawfully at large (ss 19 to 21), the
regulation-making power (s 31), the transitional provision (s 32), and the Schedule
offences other than item 27, which are taken as a single "Schedule offence" input.

## What the Act turns out to say

### 1. A national serviceman takes no oath, gets no certificate, and cannot resign

The oath section "shall not apply to members of the Corps who are national
servicemen" (s 10(3)); "No certificate shall be issued" to one (s 11(2)). The right to
resign on 14 days' written notice belongs to a member "enrolled as a volunteer"
(s 12(1)); the text gives a national serviceman no route to resign (an inference from
what s 12(1) leaves out). The Commandant may discharge a member unlikely to be useful
(s 12(2)), but a member called up for national service only with the prior approval
of the national-service authority (s 23). Refusing the oath is an offence only for
volunteers: $1,000 or 6 months or both. Asserted.

### 2. A Schedule offence goes one of two ways, and the court route needs a written sanction

A disciplinary officer may impose any one of detention up to 40 days, a fine up to
$200, stoppage of leave up to 28 days, restriction of privileges up to 14 days, extra
duty up to 7 days, reprimand or caution (s 16(1)), plus compensation up to $50
(s 16(4)); for an officer, a commanding officer has the same list plus reduction in
rank, and compensation up to $100 (s 17). Instead, the member may be prosecuted: $500
or 3 months or both, and compensation up to $1,000 (s 24(1), (2)) — but "No
prosecution under this section shall be instituted without the previous sanction in
writing of a commanding officer" (s 24(4)). Compensation never bars a civil claim for
damages beyond it (ss 22, 24(3)). Asserted.

### 3. A disciplinary officer cannot reduce a subordinate officer's rank

He must refer the case to the Commandant, who may reduce rank or impose any s 16(1)
punishment (s 16(2)). Asserted.

### 4. An appeal suspends the punishment and cannot make it worse

Appeal lies within 14 days to a commanding officer (subordinate officers, s 16(3)) or
to the Commissioner (officers, s 17(2)), and "any punishment imposed shall be
suspended pending the determination of the appeal". On appeal the punishment "shall
not in any event be greater or more severe than that originally imposed" (s 18). The
encoding compares severity only within one kind of punishment; the text gives no scale
across kinds. Asserted.

### 5. Desertion carries imprisonment only

Unlawful absence "under circumstances which show that he has the intention of not
returning" is deemed desertion, punishable by imprisonment up to 12 months with no fine
provided; any police officer may arrest without warrant (s 14). Asserted (the
deeming, not the penalty).

### 6. Pay deductions must leave the member $1 a day, and short absences do not count

Deductions for compensation, fines and sums awarded may not leave the member "less than
$1 a day", and may not exceed the sum awarded (s 29(2)). No one is treated as absent
or detained unless it lasted 6 hours or more or the absence prevented a duty
(s 30(2)(a)), and no period under 24 hours counts as more than one day (s 30(2)(d)).
Asserted.

### 7. Section 25 protects superiors and equals, not juniors

A member commits an offence by threatening or insulting "any police officer or member
of senior or equal rank" on duty or in connection with duty ($1,000 or 6 months or
both). Insulting a junior member is not a s 25 offence (Schedule item 13, ill-treating
a member of lower rank, may still reach it). The encoding reads "of senior or equal
rank" as qualifying "member" only, so any police officer is protected; this is an
inference, and the words can be read the other way. Asserted on the inference.

### 8. Smaller points

ss 13(2) and 26(1) punish unreturned or lost equipment with a $500 fine OR 3 months,
without the "or to both" found in ss 10, 24, 25 and 27, and add liability for the
value, recoverable as a fine (asserted as $500 plus value). A full-time member who
takes any trade or employment without the Commissioner's permission commits a Schedule
offence (item 27). Asserted. Members are affiliated to the Police Force but "shall not
be police officers" (s 7(1)) — not asserted.

## What would need doing before this is worth anything

- The regulations under s 31 (enrolment, discipline, pay, compensation for injury)
  were not retrieved; much of what a member meets day to day is there.
- The other 26 Schedule offences are not modelled individually.
- The reading of s 25 (finding 7) and the absence of a resignation route for national
  servicemen (finding 1) need a lawyer's view.
- No case law was searched.
