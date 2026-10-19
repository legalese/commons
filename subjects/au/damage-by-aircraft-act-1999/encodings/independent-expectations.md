# Independent expectations: Damage by Aircraft Act 1999 (Cth)

Written from BRIEF.md and the source (`../registers/source-bundle/C2004A00498.txt`, compilation of 31 March 2013, with endnote 3) only, before any `.l4` file was opened.

Seat: the person on the ground (the sufferer).

Baseline facts ("the baseline") unless a scenario says otherwise: a civil aircraft (not Defence Force, not model), within Australian territory, engaged in international air navigation (s 9(4)(c)(i)), in flight; physical injury to a person on land, suffered 1 June 2014; operator authorised and holding exclusive right for more than 14 consecutive days; no unauthorised use; owner with an active role; no lease or financial accommodation arrangement.

## s 4 and s 9: does the Act apply?

| # | Scenario | Expected | Words of the Act |
|---|---|---|---|
| 1 | Baseline | Act applies | s 9(3) "applies to acts, omissions, matters and things within Australian territory"; s 9(4)(c)(i) "international air navigation" |
| 2 | Baseline, but a Defence Force aircraft | Does not apply | s 9(2) "does not apply in relation to a Defence Force aircraft"; s 9(4) is "Subject to subsection (2)" |
| 3 | Defence Force aircraft that is *also* on a s 9(4) category (e.g. landing at a Commonwealth place) | Does not apply | s 9(4) "Subject to subsection (2)" |
| 4 | Baseline, but a model aircraft | Does not apply (not an "aircraft") | s 4 "aircraft ... does not include model aircraft" |
| 5 | Baseline, but the events are outside Australian territory | Does not apply | s 9(3) |
| 6 | Baseline, but the aircraft falls in no s 9(4) category | Does not apply | s 9(4) lists the aircraft "in relation to" which the Act applies. **Possible difference from the brief:** the brief's NOTHING-not-FALSE rule might suggest NOTHING here; I read s 9(4) as an exhaustive statement of the Act's (constitutionally limited) reach, so the answer is "does not apply". If the encoding returns NOTHING/unknown I record it as a reading difference, not a bug. |
| 7 | Commonwealth aircraft only (no other category) | Applies | s 9(4)(a) |
| 8 | Aircraft only engaged in air navigation within a Territory | Applies | s 9(4)(c)(iv) |

## s 10(1): the causes

| # | Scenario | Expected | Words |
|---|---|---|---|
| 9 | Impact with the aircraft in flight | s 10 applies | s 10(1)(a) |
| 10 | Impact with part of an aircraft damaged or destroyed while in flight | s 10 applies | s 10(1)(b) |
| 11 | Impact with a thing that fell from an aircraft in flight | s 10 applies | s 10(1)(c) |
| 12 | Harm that is a result of a (a)/(b)/(c) impact (e.g. fire after crash) | s 10 applies | s 10(1)(d) |
| 13 | Some other cause (e.g. noise, no impact) | s 10 does not apply; no liability under s 10(2); no s 11 recovery | s 10(1) "caused by" (a)-(d) only |

## s 10(1A): mental injury alone

| # | Scenario | Expected | Words |
|---|---|---|---|
| 14 | Mental injury only, suffered 1 June 2014 | s 10 does not apply | s 10(1A) "does not apply ... unless the person ... suffers other personal injury, material loss, damage or destruction"; endnote 3 item 7(3) |
| 15 | Mental injury only, suffered 31 March 2013 (commencement day) | s 10 does not apply | item 7(3) "on or after the commencement" |
| 16 | Mental injury only, suffered 30 March 2013 | s 10 applies (the (1A) limit does not reach it) | item 7(3), read contrariwise |
| 17 | Mental injury plus other physical injury, 1 June 2014 | s 10 applies | s 10(1A) "unless" limb |

## s 10(2), (2A), (3): who is liable

| # | Scenario | Expected | Words |
|---|---|---|---|
| 18 | Baseline | Operator and owner liable; authoriser not; navigation controller not | s 10(2)(a), (b) |
| 19 | Operator authorised but exclusive right only 10 days (owner not on a lease) | Authoriser liable, as well as operator and owner | s 10(2)(c) |
| 20 | Operator authorised with exclusive right of exactly 14 days | Authoriser liable ("more than 14" not met) | s 10(2)(c) "more than 14 consecutive days" |
| 21 | Unauthorised use; controller did not take all reasonable steps | Navigation controller liable | s 10(2)(d) |
| 22 | Unauthorised use; controller took all reasonable steps | Navigation controller not liable (operator and owner still liable) | s 10(3) excludes only para (2)(d) |
| 23 | Owner with no active role, lease in force giving another the exclusive right | Owner not liable; operator still liable | s 10(2A)(a), (b), (c)(i) |
| 24 | Owner with no active role, another has exclusive right, and owner provides financial accommodation | Owner not liable | s 10(2A)(c)(ii) |
| 25 | Owner with an active role and a lease in force | Owner liable | s 10(2A)(b) not met |
| 26 | Owner with no active role, no lease and no finance arrangement | Owner liable | s 10(2A)(c) not met |

## s 11: no proof of fault

| # | Scenario | Expected | Words |
|---|---|---|---|
| 27 | Baseline | Recoverable without proof of intention, negligence or other cause of action | s 11 |
| 28 | Mental injury only, 1 June 2014 | Not recoverable under s 11 (s 10 does not apply) | s 11 "of the kind to which section 10 applies" |

## s 11A: contributory negligence

| # | Scenario | Expected | Words |
|---|---|---|---|
| 29 | Injury 1 June 2014; damages but for negligence $100,000; my share 25% | Reduced to $75,000 (reduction $25,000) | s 11A(2), (3). **Reading note:** the Act says "reduced to the extent the court thinks just and equitable having regard to the share"; it does not mandate a strictly proportional reduction. I take the brief's input ("the share of responsibility it attributes to me") as the court's just-and-equitable reduction share, so damages × (1 − share). |
| 30 | Same, share 0% | $100,000 | s 11A(3) |
| 31 | Same, share 100% | $0 | s 11A(3) |
| 32 | Same facts but injury suffered 30 March 2013 | NOTHING (the Act does not reduce) | endnote 3 item 7(4); brief "Dates" |
| 33 | Injury suffered 31 March 2013, share 50% of $100,000 | $50,000 | item 7(4) "on or after the commencement" |

## Other notes

- s 10(2A) removes a person from *all* of s 10(2) ("Subsection (2) does not apply to a person"), so an owner meeting (2A) who was also the authoriser under (2)(c) escapes (2)(c) as well. Tested only if the encoding models owner and authoriser as the same person.
- s 10(4) (multiple aircraft) and s 11B are out of scope per the brief.
