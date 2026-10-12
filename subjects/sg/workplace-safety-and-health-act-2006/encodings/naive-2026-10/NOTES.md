# Workplace Safety and Health Act 2006 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation ("version in force from
1/12/2025"), with amendments to Act 30 of 2024 (platform workers, in force 1 January
2025), Act 12 of 2020 (s 19(3), in force 1 October 2025) and S 754/2025 (in force
1 December 2025) shown.

**Checks:** two case files, 166 assertions satisfied (120 in `wsha-cases-duties.l4`, 46 in
`wsha-cases-occupier-and-employer.l4`), 0 errors, 0 warnings.

## Why this Act, and why scoped

**9 of the 527 Singapore Acts** deposited here cite it. This row takes what an
employer, principal, worker or company officer actually meets: who counts as an
employee (s 6(2), (3)), who is outside the Act (s 3(2), s 62(1), Sixth Schedule), the
principal's duty to contractors (ss 14(2), 14A(4)), the protections in s 18, the
scene of a fatal accident (s 25), remedial and stop-work orders and appeals (ss 21,
22), the onus on the accused and on officers (ss 47, 48), the maximum penalties (ss
15, 18, 20, 21, 23, 25, 26, 46, 50, 51, 53), composition (s 56) and civil liability (s
60).

Not encoded: the content of the general duties in ss 11-17 (standards "so far as is
reasonably practicable", not tests), Part 7 management arrangements, the Council and
codes of practice, inspectors' powers, and the Schedules of dangerous occurrences,
diseases and machinery. Which offences are compoundable, and what must be notified
under s 27, is in regulations not retrieved.

## What the Act turns out to say

### 1. A reckless worker faces up to $200,000; a negligent one up to $30,000

s 15(4) gives an expressly lower penalty for a *negligent* act endangering safety:
$30,000 or 2 years. s 15(3), the *wilful or reckless* act, states no penalty at all,
so it falls to the s 50 general penalty: $200,000 or 2 years for a natural person,
$500,000 for a body corporate, plus a daily fine if it continues. Asserted.

### 2. Defying a stop-work order costs ten times defying a remedial order

s 21(6): a remedial order, $50,000 or 12 months plus $5,000 a day. s 21(7): a
stop-work order, $500,000 or 12 months plus $20,000 a day. And an appeal (within 14
days of service, s 22(1)) suspends a remedial order but not a stop-work order, which
must be obeyed pending the appeal (s 22(2), (3)). Asserted.

### 3. The burden is on the accused, twice over

s 47: where a duty is "so far as is reasonably practicable", it is for the accused to
prove that nothing more was reasonably practicable. s 48: when a company offends,
every officer is guilty unless the officer proves *both* no consent or connivance
*and* all due diligence. Proving one is not enough. Asserted.

### 4. A contract term does not discharge a principal's duty

s 14A(4): it is not a defence for a principal to rely "solely" on a contract term that
the contractor has complied or will comply. The s 14(1) duty to contractors' workers
applies only when they work under the principal's direction as to manner (s 14(2)).
Asserted.

### 5. A second death from the same offence lifts the fine cap

s 51: on a second conviction of the same offence causing death, the maximum fine
becomes $400,000 (natural person) or $1 million (body corporate). The text is not
limited to s 50 offences, so the encoding applies it to any offence; **this is an
inference**. Asserted.

### 6. Regular volunteers and interns are employees; the Government cannot be prosecuted

s 6(2): a volunteer working regularly, with the other person's knowledge or consent,
in connection with that person's business is treated as an employee; a one-off
volunteer is not. s 6(3): so is a person on the job for training or work experience.
s 3(2): the Act binds the Government but does not make it liable to prosecution, and
s 3(3) denies that immunity to its contractors. On-duty uniformed services and
self-contained international crews are outside the Act (Sixth Schedule). Asserted.

### 7. Smaller points

An employer may not charge employees for safety measures (s 18(1)) or dismiss them
for helping an inspector, reporting in good faith, committee work or complying with
an order, or proposing to (s 18(2)): $5,000 or 6 months. Records must be kept at
least 5 years (s 18(4)). Altering the scene of a *fatal* accident, dangerous
occurrence or occupational disease without consent is an offence unless for rescue
(s 25); a non-fatal accident is not covered by s 25(1). Composition is capped at the
lower of half the maximum fine and $5,000 (s 56). The Act confers no civil right of
action (s 60). Asserted.

## What would need doing before this is worth anything

- The regulations (which offences are compoundable, what is notifiable under s 27,
  any other record-keeping period under s 18(4)) were not retrieved.
- Imprisonment terms stated in offence sections are returned whether or not the
  offender is a body corporate; the text does not say how they apply to one.
- The second-conviction rate for s 15(5) and the s 51 repeat rule are modelled as
  flags on the facts, not derived from a conviction history.
- No sentencing decisions or case law were searched.

## Occupier and employer (added 12 October 2026 for REQ-0288)

Module `wsha-occupier-and-employer.l4`, cases `wsha-cases-occupier-and-employer.l4` (46 assertions). Raised by the Haziq
scenario, event h080: an agency's security officer falls on a wet stairwell in an office tower leased by a software
company. Section numbers were read from the body of the deposit; its arrangement table runs out of step from s 14 on.

1. **The answer.** The company, if it has "charge, management or control" of the premises (s 4(1) "occupier", para (c)),
   must take reasonably practicable measures so that the workplace and "all means of access to or egress from the
   workplace" are "safe and without risks to health to every person within those premises, whether or not the person is at
   work or is an employee of the occupier" (s 11). The officer need not be its employee. The agency, as his employer, owes him
   the separate s 12(1) duty to ensure his safety and health "at work", which s 4(1) defines as wherever his work is carried
   out, so it follows him onto premises the agency does not occupy; s 12(3) lists what that includes (a safe work environment,
   protection from hazards in his workplace, emergency procedures, instruction, training and supervision). Asserted.
2. **Neither duty dilutes the other.** s 10(b), (c): the Act may put the same duty on two persons, and a duty "is not
   diminished or affected" by its being imposed on another. Each party is tested on its own facts. Asserted.
3. **The company is probably also the agency's principal**, which adds duties the question did not ask about. s 14(1) (the
   contractor's employees) applies only if the company directs "the manner in which the work is carried out" (s 14(2)); s 14A
   (ensuring the agency has the expertise and has taken adequate safety measures) applies to any contractor engaged on or after
   1 September 2011, whatever the direction (s 14A(6)). That hiring a guard for one's offices is "in connection with" the
   company's business, so that it is a "principal", is an **inference**. If its own staff (cleaners, say) wetted the stairs, s
   12(2) and s 14(3) add duties to persons affected by its undertaking. Asserted on variant facts.
4. **Leasing is not the test; control is.** The s 4(1) definition applies "whether or not the person is also the owner". A
   tenant of one floor whose stairwell the landlord or management controls may not be the occupier of the stairwell; whether a
   lessee has control is a question of fact the encoding takes as a flag. But s 11(b) reaches the means of access to the
   occupier's own workplace, so the encoding holds a tenant-occupier to s 11 for a stairwell it uses as access even if it does
   not control it (a **reading**; what is "reasonably practicable" for a tenant there is left open). Where the stairwell is
   strata common property used by persons at work, s 19 treats it as part of their workplace and puts the access-and-egress
   duty on the occupier of the common area, which includes the management corporation (s 19(3)). Asserted.
5. **The ledger's assumption is half right.** "The occupier must keep the premises safe" overstates s 11: the duty is to take
   measures "so far as is reasonably practicable", and s 47 puts the onus of proving that nothing more was practicable on the
   accused. "The employer's WICA liability is unaffected" is not something this Act says. It names the Work Injury
   Compensation Act 2019 only in s 27B(1) (learning reports inadmissible in WICA proceedings). The nearest it comes is s 59
   (nothing in it "derogates from the effect of any other written law") and s 60(1)(b) (it does not affect any right of
   action in civil proceedings). What WICA gives the officer, and against whom, needs that Act, which is not deposited here.
6. **Consequences.** A breach of s 11 or s 12 is an offence under s 20; no penalty is stated, so s 50 applies: up to $500,000
   for a company (plus $5,000 a day if it continues after conviction), $200,000 or 2 years or both for an individual. The
   Commissioner may serve a remedial or stop-work order on whoever controls the workplace, or owes a duty to a person at work
   in it, or poses a risk (s 21(2)), so on both parties here. Asserted.
7. **Needs other instruments.** Whether and how the fall must be reported (s 27 and the regulations under it, not
   retrieved; believed to be the Workplace Safety and Health (Incident Reporting) Regulations, a name not read in the deposit); the approved codes of practice that inform "reasonably practicable" (s
   40C); the Work Injury Compensation Act 2019 for compensation; and case law on who has "control" of premises and on what is
   reasonably practicable. None was retrieved.
