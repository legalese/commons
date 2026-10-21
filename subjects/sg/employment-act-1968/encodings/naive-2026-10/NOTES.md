# Employment Act 1968, Part 2 — naive encoding

**Method: naive.** Straight from the deposited text with the `writing-l4-rules`
skill and nothing else. No pipeline, no coverage table, no independent test
pass, no human gate.

**Edition:** 2020 Revised Edition, informal consolidation in force from
5 December 2025.

**Checks:** `l4 run` on each of `ea-part2-cases.l4`, `ea-parts-3-and-4-cases.l4`,
`ea-parts-5-to-12-cases.l4`, `ea-part12-retrenchment-cases.l4` and
`ea-retrenchment-reporting-notification-cases.l4` — 334 assertions
satisfied (52 + 116 + 78 + 43 + 45), 0 errors, 0 warnings (12 October 2026).

## Scope

Parts **2, 3, 4, 5, 6, 6A, 7, 8, 9, 10 and 12** — every operative Part except
Part 1 (preliminary), Part 11 (repealed) and Parts 13–16 (inspection, general
and final provisions).

**246 assertions**, 0 errors, 0 warnings.

Two limits to hold in mind:

- **Part 9 is the current law only.** s 76 carries three qualifying rules side
  by side — for confinements before 1 May 2013, between then and 22 August 2015,
  and after. Only the last is encoded. A confinement before 22 August 2015 is
  outside this encoding entirely and the rules for it differ.
- **Everything prescribed is a supplied fact.** Record retention periods, pay
  slip timing, the Fifth Schedule reckoning, the s 95A minimum period of
  service. The regulations were not retrieved.

Not encoded within the Parts covered: s 19, s 34, s 39, ss 41–41A, ss 47–53,
s 66, ss 70–75, ss 84–87A (including childcare leave), s 90, ss 97–101.

## Four observations

**1. The employee's entitlement to the statutory minimum notice is nowhere
stated in one place.** It emerges from three subsections read in order:

1. s 10(2) — the contract's notice period governs;
2. s 8 — but a term less favourable to the employee than the Act is "illegal and
   void to the extent that it is so less favourable";
3. s 10(2) again — and once the term is void there is no provision in the
   contract, so the subsection's own words, "in the absence of such provision",
   send the question to s 10(3).

So a contract saying "one day's notice" gives a ten-year employee 28 days. That
is almost certainly the intended result, and it is reached by a route that no
single provision describes. Asserted as the chain on `a mean contract of 1 day`
against `ten years in`.

The same one-day term is **perfectly lawful** for a new starter, because their
statutory minimum is also one day. Nothing about the term changes; what changes
is the service it is measured against. That pair is in the cases too.

**2. s 10(3) states its three thresholds in two different units.** The bands are
"less than 26 weeks", "26 weeks or more but less than 2 years", "2 years or more
but less than 5 years", and "5 years or more". Weeks and years, with no
conversion given. A system that reduced service to a single number would have to
decide how many days are in two years, which differs across leap years and which
the Act does not answer.

This encoding therefore does **not** compute the bands: it asks the three
questions the Act asks ("employed for 26 weeks or more", "for 2 years or more",
"for 5 years or more") and leaves them as facts. That is as precise as the Act
and no more, which is the right place to stop — but it means the encoding cannot
take a start date and tell you your band. Doing that would require a convention
the legislature has not supplied.

**3. s 13 treats the two parties very differently.** The employer is deemed to
have broken the contract on **one** element: failure to pay salary in accordance
with Part 3. The employee is deemed to have broken it on **three**: absence of
more than two days, continuously, without prior leave, *and* either no
reasonable excuse *or* no attempt to tell the employer.

The "or" in that last pair does real work. An employee with a genuinely
reasonable excuse who does not mention it is **still deemed to have broken the
contract** — limb (b) is made out on its own. Asserted as
`an absence of 10 FALSE TRUE FALSE`: reasonable excuse, never communicated,
deemed in breach.

**4. Worse treatment unlocks the wrongful-dismissal remedy sooner.** Under
s 14(2A), a manager or executive dismissed **with** notice (or without notice
but paid salary in lieu) is a "relevant employee" only after **6 months'**
service. A manager dismissed **without notice and without salary in lieu** —
the harsher treatment — is a relevant employee under limb (b) with **no service
qualification at all**.

So the manager sacked on the spot in week one may bring a claim, and the one
given proper notice in week one may not. There is a coherent policy reading
(summary dismissal with nothing in hand is the case that most needs a remedy),
but the drafting produces it as a side effect of two limbs rather than stating
it. Asserted as the pair in § `14(2A)`.

## The s 14(2A) point, completed

Limb (c) of s 14(2A) is the whole of its own text: "an employee not employed in
a managerial or an executive position." No service qualification, no condition
about notice. It is now encoded, and it sharpens observation 4 rather than
softening it:

- a **non-managerial** employee is a relevant employee from the first day,
  however they were dismissed;
- a **manager or executive** dismissed *with* notice must have served 6 months;
- a **manager or executive** dismissed *without* notice and *without* salary in
  lieu is a relevant employee from the first day, like the non-manager.

So the 6-month threshold applies to exactly one group — managers and executives
who were dismissed in the proper manner. Asserted as a pair on the same facts,
one a manager and one not.

## What would need doing before this is worth anything

- ss 15–19 of Part 2.
- Parts 3, 4, 9 and 10, which is where most of the Act's value to an employee is.
- The Employment Claims Act 2016, which s 14(2) routes the remedy through.
- No case law was searched.


---

# Added with Parts 3 to 12

## A harness trap worth recording

**`MODULO` does not return a fractional part on this toolchain.** `3.5 MODULO 1`
evaluates to **3.5**, not 0.5. A floor written as `n MINUS (n MODULO 1)` is
therefore the identity function, and a round-half-up built on it silently
returns its input — which is exactly what the first version of the s 88A(2)
proportioning did. It type-checked, ran clean, and gave wrong answers; only the
assertions caught it.

On integers `MODULO` behaves: `42 MODULO 12` is 6. The rule was rebuilt to stay
in integer arithmetic throughout — the entitlement in days and the months in the
year are both whole numbers, so the division is a numerator over 12 and the
rounding comes off the remainder. See `the proportion rounded half up` in
`ea-part10-leave.l4`.

## Observations, Part by Part

**s 16 yields to the contract in either direction.** "Subject to anything in the
contract of service to the contrary" — unlike s 8, which strikes down only terms
*less favourable* to the employee. So the measure of damages for breach can be
contracted below the statutory default.

**s 29's three requirements come apart.** A deduction for damage or loss is
capped at the actual loss, capped again at a quarter of a month's wages, and
forbidden until the employee has had an opportunity to show cause. The
Commissioner may lift the *second* ceiling only. Not the first, and not the
procedural one.

**Three heads escape the s 32 overall cap** — absence, recovery of advances and
loans, and cooperative society payments. An employee repaying a loan can be
deducted more than half their salary and s 32 has nothing to say; what limits it
is s 31(5)'s quarter per instalment. Note also the asymmetry inside s 31: the
12-month ceiling applies to *advances* only, and s 31(4) gives loans no period
limit at all.

**s 38(8)'s absolute 12-hour ceiling is excepted by s 38(2)(a) to (e) but not by
(f).** The economic and essential-services ground raises the s 38(1) limits and
leaves the 12-hour one standing.

**ss 45 and 46 are expressed negatively**, and so is s 76(2B). None of them
creates an entitlement; each bars one below a threshold. The Act nowhere says
what a retrenchment benefit *is* or how much it is.

**s 35 and s 33(1) are word for word identical** — same two paragraphs, same
$4,500 and $2,600, same exclusions, same substitution power — governing two
entirely different questions: who has a rest day and a right to overtime, and
who gets priority for unpaid salary in an insolvency. They are not
cross-referenced. The encoding uses one rule for both, so the duplication is
visible rather than mirrored; if an amendment moved one figure and not the
other, this encoding would give one answer where the Act gave two.

**s 54 voids the whole contract of service**, not merely the offending term.
Compare s 8, which voids a term "to the extent that it is so less favourable".
An employer who writes part of the salary as payable in goods destroys the
contract, not just that clause — on the face of it, including every term
protecting the workman.

**The maternity benefit period is shorter than the maternity absence.** Under
s 76(1)(a) and (b) the absence is 12 weeks; under s 76(1A) the paid benefit
period is 8 weeks in every case. Four weeks of the statutory absence are unpaid.

**s 76(3) pays a day worked inside the benefit period twice over** — the gross
rate for that day, *plus* either another day's pay or a day's absence at the end.

**s 95(3) and s 96(4) deem a failure regardless of knowledge.** An incomplete or
inaccurate employee record or pay slip is a breach "whether or not the employer
knew". Asserted as a pair on the knowledge fact, where the answer does not move.

**Part 7 is one sentence, and its effect is exclusion.** The Act does not apply
to a domestic worker at all unless the Minister has applied it by notification.
Nothing in the encoding can decide whether such a notification exists.

**s 69 bars a young person only from undertakings the Minister has named.**
Industrial work as such is not forbidden to a 15-year-old; a declaration is
needed. Contrast s 68, where the prohibition on employing a child is general and
the exceptions are narrow.

## Retrenchment information (added 12 October 2026 for REQ-0289)

`ea-part12-retrenchment.l4` and `ea-part12-retrenchment-cases.l4` (43 assertions).
The question (Haziq scenario, event h065): an employer with 40 employees retrenches
12 in one exercise — must it notify the Commissioner, within what time, and with what
particulars?

1. **The Act answers "only if a Gazette notification says so", and nothing more.**
   s 96A(1): the Commissioner "may, by notification in the Gazette, require any
   employer, or any employer in a class of employers" to furnish information on a
   retrenchment "at such time and in such form as may be specified in the
   notification". s 96A(2): every employer "to whom the notification applies must
   comply". With a notification that applies to the employer and covers the
   retrenchment, the 40/12 employer must report; without one, the Act alone imposes
   no duty. Both asserted.
2. **The ledger's expectation is not in the Act.** "5 or more retrenched within
   6 months" and "within 5 working days" appear nowhere in the deposit. Nor does any
   workforce size. If those figures are right they come from the Commissioner's
   notification (or from policy), which was not retrieved; the encoding reports that
   the time, the form, the particulars, and which employers and which retrenchments
   are covered are all fixed by the notification, and asserts that a covered
   4-person firm retrenching 1 owes the same duty as the 40-person firm. Hence
   "addresses", not "satisfies".
3. **Section number confirmed.** s 96A is where the ledger put it (body of the
   deposit, Part 12, annotated [55/2018]).
4. **A failure is a civil contravention, not an offence.** s 126A(aa) declares it a
   civil contravention; s 101(3) takes it out of the s 101 returns offence. s 126B(1)(aa)
   lets an authorised officer issue a contravention notice for "each occasion" of
   failure concerning "any one employee", so 12 unreported retrenchments are 12
   occasions. The amount is "prescribed" and was not retrieved; the cases use an
   illustrative 1,000 and say so.
5. **The returns secrecy rule does not protect it.** s 102(5) disapplies s 102(1)-(4)
   for information furnished under s 96A.
6. **The criminal route is one step removed.** An authorised officer may give
   directions under s 126D(1); disobeying one without reasonable excuse is an offence
   (fine up to $5,000, imprisonment up to 6 months, or both, s 126D(2)). Enforcement
   of a penalty is stayed during reconsideration or appeal (s 126C(6)).
7. **Seafarers and domestic workers are not "employees"** (s 2(1)), so their
   retrenchment is outside s 96A. Inference: whether the 12 count at all depends on
   that definition; the Act does not say whether a notification counts heads across
   them.
8. **Needs, for a full answer:** the Commissioner's Gazette notification under
   s 96A(1) (thresholds, deadline, form, particulars); the regulations prescribing the
   administrative penalty amounts and the s 126C periods. Retrenchment benefit is
   untouched here: s 45 (no entitlement under 2 years' continuous service) is in
   `ea-part4-hours.l4`, and this encoding found no provision fixing the amount of
   a benefit (not searched beyond s 45).

## Retrenchment reporting notification (added 12 October 2026 for REQ-0289)

`ea-retrenchment-reporting-notification.l4` and
`ea-retrenchment-reporting-notification-cases.l4` (45 assertions). The
Employment (Retrenchment Reporting) Notification 2019 (S 200/2019), version in
force from 1 November 2021, deposited at
`../../registers/source-bundle/EmA1968-S200-2019.txt`. It is the Gazette
notification under s 96A(1) that the section above found missing, and it fills
the supplied facts that `ea-part12-retrenchment.l4` left open.

1. **The answer: yes, within 5 working days, with the Schedule particulars.**
   An employer with 10 or more covered employees on the day it gives notice
   (para 2(1), 2(3)) must give the Commissioner a retrenchment report for every
   notice of retrenchment given on or after 1 November 2021 (para 3(1)),
   "not later than 5 working days after the day that the employer gives the
   notice" (para 4), in the form on the Ministry of Manpower website unless the
   Commissioner allows otherwise (para 5), containing the Schedule's
   particulars: seven about the employer (para 1(a)-(g), two of them
   conditional) and eight about each retrenched employee (para 2(a)-(h), one
   conditional). The 40/12 employer, assuming its staff are on open-ended
   contracts, must report all 12. Asserted first in the cases.
2. **The ledger's "5 or more retrenched within 6 months" is not in the deposited
   text.** The current para 3(1) is triggered by "any" one notice to one covered
   employee; there is no minimum number and no aggregation period. A 10-employee
   employer retrenching one person must report; a 9-employee employer
   retrenching anyone need not. The deposit shows one definition in para 2(1)
   "[Deleted by S 781/2021 wef 01/11/2021]" without its old words, and the
   version from 1 April 2019 to 31 October 2021 was not deposited; inference
   only: the ledger's figure may come from that earlier version or from MOM
   guidance. The "5 working days" in the expectation is right, but it runs from
   the day the notice is given, not from the day the retrenchment takes effect
   ("regardless when the notice takes effect or when the employment ends").
3. **Who counts is narrower than the Act's "employee".** Para 2(2) reads every
   reference to an employee as one on a contract with no end date or with a
   term of at least 6 months. Reading: that applies to the 10-employee count as
   well as to who must be reported, so short fixed-term staff count for
   neither. The person must also be an "employee" under s 2(1) of the Act (no
   seafarers or domestic workers), carried as a supplied fact.
4. **"Retrench" is narrow:** termination at the employer's initiative because of
   redundancy or reorganisation (para 2(1)). A resignation or a dismissal for
   misconduct is outside it.
5. **Working days:** para 2(1) excludes Saturdays, Sundays and public holidays.
   The encoding counts from the day after the notice and takes the report as in
   time on or before the 5th working day (a reading of "not later than ... after
   the day"). Public holidays are not in the deposit and are supplied as a list;
   the holidays in the cases are illustrative. Day numbers start at
   Monday 1 November 2021 = 0. The Interpretation Act 1965 provisions on
   computing time were not retrieved.
6. **Particulars:** the Schedule's lists are introduced by "including", so they
   are not closed on their face; only what is named is encoded. Para 1(b) (trade
   name) applies only if different; para 2(g) (reasons for paying no benefit)
   only if none was paid; para 1(d) (recognised trade union) is read as
   applying only where a union is recognised. The content of the MOM website
   form was not retrieved.
7. **Consequences** are as in the section above, now on the Notification's own
   facts: each unreported covered retrenchment is one s 126B(1)(aa) occasion.
   The prescribed penalty amount is still not retrieved.
8. **Needs, for a complete answer:** the pre-1 November 2021 text of S 200/2019
   (and S 781/2021, the amending notification) for retrenchments notified
   before that date; the Public Holidays Act gazettes for the actual holidays;
   the MOM retrenchment-reporting form; the regulations prescribing the
   s 126B administrative penalty; possibly the Interpretation Act 1965 on time.

## What would still need doing

- Parts 13–16, and Part 1.
- ss 84, 84A and 87A — dismissal before confinement, and childcare leave. s 87A
  is the one an employee is most likely to ask about of those left out.
- The historical limbs of s 76 and ss 84–84A, if anything before 22 August 2015
  matters.
- The regulations, which carry every prescribed period and the Fifth Schedule.
- The Employment Claims Act 2016, which s 14(2) routes the remedy through.
- No case law was searched, and no human gate has been sought.


## Seat

**Seat: the employee** -- one person, in one employment with one employer.
The Employment Act is applied, first and last, to the employee: it fixes the
notice they are owed, when they must be paid and what may be taken from their
pay, their rest days, hours, overtime and leave, their maternity protection,
and when they may be dismissed or suspended. The employer, the Commissioner and
the Minister appear only as the people who must act towards them.

`ea-seat.l4` phrases the existing rules as that person's questions --
"How many days of notice am I owed", "Can I claim for wrongful dismissal",
"Was I paid late", "How many days of annual leave do I get", "Must my employer
report my retrenchment to the Commissioner" -- 21 questions in six groups.
Each calls an existing rule with the same parameters; **no existing rule,
module or test was changed**. `ea-cases-seat.l4` asserts every question (59
assertions), with fixtures and expected values copied from the existing,
hand-checked case files.

The defaults ruled on 2026-10-18, and where this encoding stands:

- **The Act alone, with the instruments that set its numbers or dates.**
  Partly departs. The Employment (Retrenchment Reporting) Notification 2019 is
  brought in; the regulations that set record retention, pay slip timing, the
  Fifth Schedule reckoning and the s 95A minimum period were not retrieved, so
  those numbers are supplied facts.
- **The actors the text names.** Follows: employer, employee, workman,
  Commissioner, Minister, principal and contractor, as the Act names them.
- **A judgment handed to someone else answered conditionally, never guessed.**
  Departs. Judgments the Act leaves to the employer, the Commissioner or a
  court are taken as plain facts rather than stated as conditions: "reasonable
  excuse" (s 13(2)), "due inquiry" and "misconduct" (s 14(1)), "immediate"
  danger (s 15), "light work suited to the child's capacity" (s 68(3)). The
  Commissioner's permission under s 29 is a fact too, though there the result
  reads naturally as conditional on it.
- **The Act's own definitions worked out from facts, borrowed terms asked as
  facts.** Mostly follows. The exception is length of service for s 10(3),
  which is asked band by band rather than worked out from dates (observation 2
  above explains why).
- **One case is the text's natural unit.** Follows: one employment. The
  retrenchment reporting rules count notices across the workforce, which is
  the Notification's own unit.
- **The Act's own terms, each with a plain gloss.** Follows for the terms;
  the plain glosses were missing from the modules and are now given beside
  each question in `ea-seat.l4`.
- **The operative sections in, the machinery out.** Departs in part. Parts
  13 to 16 are out, but the s 96A administrative penalties, contravention
  notices, reconsideration and directions (ss 126A-126D), the secrecy rules in
  ss 101-102, and the s 82 offence are encoded beside the operative rules.
  Most rules in the modules are also phrased from the employer's side ("the
  employer has complied with section 95(1)", "section 38(1)(a) was
  contravened"); the seat layer re-phrases the main ones and leaves the rest.

Light pass, 19 October 2026.


## Seats

Two seat layers sit over the same modules (ruling of 21 October 2026, "More
than one seat"). Neither changes a rule; both IMPORT the modules and call
their decisions, so where they ask about the same facts they cannot disagree.

**1. The employee** -- `ea-seat.l4`, 21 questions, `ea-cases-seat.l4` (59
assertions). The required seat, described in the section above. On
21 October 2026 every question gained `@export` (the question in plain words,
with its section) and an `@desc` on every input; the GIVEN lists were laid out
one input to a line to carry them. No rule, name or test changed.

**2. The employer** -- `ea-seat-employer.l4`, 46 questions,
`ea-cases-seat-employer.l4` (60 assertions). Seat: the employer, an individual
or a company that employs someone under a contract of service, asking about one
employment (or, for retrenchment reporting, one exercise of giving notices).
It covers, in the employer's words ("How many days of notice must I give",
"May I make this deduction", "What is the most I can be fined"):

- whom the Act covers and which Parts apply: "employee" (s 2(1)), Part 4
  coverage by the workman and salary thresholds (s 35), employing a child
  (s 68);
- notice: the days I must give (ss 8, 10), pay in lieu (s 11(1)), whether the
  notice I gave is long enough (s 10), ending the contract for wilful breach
  (s 11(2)), the employee's deemed breach by absence (s 13(2)) and mine by not
  paying (s 13(1)), the employee leaving for danger (s 15);
- dismissal: summary dismissal after due inquiry (s 14(1)), suspension without
  pay (s 14(1)(b)), who can claim wrongful dismissal against me (s 14(2A)),
  continuity across a change of employer (ss 18, 18A);
- pay: the days I have to pay and whether I paid late (ss 21-23), salary for
  an incomplete month (s 20A);
- deductions: whether I may make one (ss 26-27), damage or loss (s 29), the
  most for absence (s 28(2)), accommodation (s 30), the 50% cap (s 32);
- rest days, hours and overtime: the rest day (s 36), rest day pay (s 37),
  overtime pay and the hours that attract it (s 38(1), (4)), the 6-hour and
  72-hour limits (s 38(1)(a), (5));
- holidays and leave: public holidays (s 88), annual leave (s 88A), sick leave
  (s 89), the s 45 bar on a retrenchment benefit;
- maternity: whether and how much I must pay (ss 76, 83), notice of dismissal
  around the absence (s 81), the s 82 offence;
- records: employee records (s 95(1), (3)), key employment terms (s 95A), pay
  slips (s 96);
- retrenchment reporting: whether I must report (s 96A, Notification para 3),
  the last day (para 4), compliance (s 96A(2));
- what I can be penalised for: the most the administrative penalties could
  total (ss 126A, 126B), the s 126D(2) offence, its maximum fine ($5,000) and
  imprisonment (6 months).

Every name in the employer layer begins "As the employer, ", so it cannot clash
with the employee layer's. `ea-cases-seat-employer.l4` imports both layers
together, which is the test that they define no name twice.

**Mirror cases.** 26 of the 60 employer assertions ask the same facts from both
seats and assert both hand-worked answers in one line (both true, both false,
or both equal to the same number). They pair 21 questions:

| Employer asks | Employee asks | Case |
|---|---|---|
| must I apply Part 4 | do the Part 4 rules cover me | workman at $4,500: both yes; manager at $1,000: both no |
| how many days of notice must I give | how many days am I owed | 1-day contract, 10 years: both 28 |
| how much in lieu must I pay | how much must I be paid in lieu | $200 x 28: both $5,600 |
| is my employee treated as having broken the contract by absence | am I | 3 days, no leave, no excuse: both yes |
| may my employee leave for danger | may I leave for danger | both yes |
| may I dismiss for misconduct | can my employer dismiss me | inquiry held: both yes |
| may I suspend without pay | is my suspension lawful | 7 days: both yes |
| can the employee I dismissed claim | can I claim | manager, under 6 months, with notice: both no |
| did I pay late | was I paid late | 4 days after dismissal: both yes |
| may I make this deduction (x2) | can my employer make it | withdrawn consent for accommodation: both no; absence: both yes |
| may I deduct for damage or loss | can my employer | $400 of $900, cause shown: both yes |
| what must I pay for rest day work (x2) | what must I be paid | 4 h own request: $50; 10 h employer's request: $237.50 |
| how much overtime must I pay | what is my overtime pay | 2 h at $12.50: $37.50 |
| how much annual leave must I give | how much do I get | first full year: 7 |
| how much sick leave must I allow | how much can I take | hospitalised 10 days: 24 |
| does short service bar a retrenchment benefit | am I barred | 1.5 years: both yes |
| must I pay maternity (x2) | am I entitled | 3 months: both yes; worked elsewhere: both no |
| how much maternity pay | how much do I get | $100 a day: $5,600 |
| would my s 81 notice be unlawful | is the notice I was given unlawful | expiring during the absence: both yes |
| have I failed to give key terms in time | has my employer | day 15: both yes |
| must I report this retrenchment (x2) | must my employer report it | 40 employees: both yes; 9: both no |

The agreement is guaranteed by construction, because both questions call one
rule; what the mirror cases guard is the layers, so that neither seat can drift
from the other by re-stating a rule instead of calling it.

**Left out of the employer seat for want of a decision.** The modules do not
decide these, so the seat layer does not answer them (writing them there would
be new law):

- the penalty for most offences: the Parts' own offence provisions (ss 19,
  53, 90 and 101 among them), the Act's general penalty for an offence with no
  penalty of its own (which is what s 82 would draw), and ss 72-75 for
  children and young persons; only s 126D(2) carries a maximum fine and term in
  the modules;
- the amount of an administrative penalty (prescribed; taken as a fact);
- how to work out the hourly basic rate of pay and the gross rate of pay for a
  day from a monthly salary (the Act's formulae are not encoded; both are taken
  as facts), so "at what rate" is answered only once the rate is supplied;
- whether I may require work beyond the hour limits (s 38(2) circumstances are
  taken as a fact) and the s 38(2)(f) exemptions;
- pay for working on a public holiday, and what annual leave must be paid or
  paid out on termination;
- childcare leave (s 87A), dismissal before confinement (ss 84, 84A), and
  confinements before 22 August 2015;
- the content of the key employment terms, the record particulars, the pay slip
  timing and the record retention period (all prescribed; taken as facts);
- the amount of any retrenchment benefit: s 45 only bars one under 2 years; the
  Act fixes none above it.

Decided by the modules but not asked in the employer seat, to keep it to the
main duties: the weekly overtime hours, the s 36(4) roster, s 37(1) compelled
rest day work, the s 38(8) 12-hour limit, s 40 shift averaging, s 46, s 69,
the s 10(2) equal-length rule, s 16, s 18A(5)-(6), s 20(2), s 25, s 31, s 33,
Parts 5 to 7, s 95(2), the report's form and particulars, s 126C(6), and
ss 101(3) and 102(5). Each can be added as a question without new law.
