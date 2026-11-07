# Motor Vehicle Accidents (Lifetime Support Scheme) Act 2013 (SA) -- baseline encoding, the injured person (and the owner or driver the Authority recovers from)

> **Edition.** The text encoded is the register's current version of 2 December 2019, fetched from
> www.legislation.sa.gov.au on 6 November 2026 (the unauthorised RTF; the authorised version is the PDF). Unlike most
> South Australian texts in Commons it does **not** come from the Open Australian Legal Corpus (collected 10 March
> 2025), so that corpus's "may be out of date" warning does not apply; but the Act's own note warns that references to
> other legislation are not updated automatically, and the LSS Rules, which carry most of the Scheme's detail, are not
> deposited. Check legislation.sa.gov.au and the Lifetime Support Authority's current LSS Rules before relying on it.

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its
`references/regulative.md`), from the seat of the individual to whom the law is applied, with the design defaults ruled
on 2026-10-18. A small date module (`lss-dates.l4`, built-in date functions only, no daydate), a seat-neutral core
(`lss-core.l4`) that holds every rule, two seat layers that ask the questions and restate none of them
(`lss-seat.l4`, the injured person; `lss-seat-owner-driver.l4`, the person the Authority recovers from), and one cases
file per seat (`lss-cases.l4`, `lss-cases-owner-driver.l4`). Answers are named outcomes (enumerations), not
`MAYBE BOOLEAN`, so no `NOTHING-kind` tag is used: where the text says no in its own words ("is not eligible", "is not
liable", "cannot be made", "may only be made by", an "if" or "while" condition that fails, a period the text fixes) the
outcome begins "no:"; where the text limits a grant in its own wording ("any reasonable request", "necessary and
reasonable expenses", "necessary costs") or is silent, it begins "not covered:". That follows the 2026-11-04 and
2026-11-05 rulings in substance. No REFUSE, no `#ASSERT REFUSED`, no BECAUSE outside `LEST BREACH`. No pipeline, no
coverage table, no independent test pass, no human gate. Not for public use as advice.

**Three regulative rules.** ss 35(2) and 37(3) ("An application for review must be made within 28 days of the date of
the determination"), s 38(3) (within 28 days after notice of the assessment) and s 52(1) ("must, at least 28 days before
leaving Australia, give the Authority notice") are each a `DEONTIC` (`PARTY the person injured MUST ... WITHIN <the
last day's day number> LEST BREACH ... BECAUSE ...`), run by `EVALTRACE` through one helper, `the timing of`. The rules
count on the day-number timeline (`DATE_SERIAL`): the trace starts at 0 and `WITHIN` is the last day's number, so an act
on the last day fulfils the rule (asserted) and an act the day after breaches it (asserted). On the stable `l4` a
`CONSIDER` on an `EVALTRACE` matches `FULFILLED` only, so anything else is read as late. The exported questions take
plain dates and yes/no facts, never a DEONTIC or an EVENT.

This is the first encoding of the Act; nothing existing was touched.

## Edition

- **Act:** Motor Vehicle Accidents (Lifetime Support Scheme) Act 2013 (SA), version 2.12.2019 (the last amendment, the
  Statutes Amendment (SACAT) Act 2019 Pt 18, which moved the appeals in ss 35 and 37 from the District Court to the
  Tribunal), deposited at `../../registers/source-bundle/motor-vehicle-accidents-lifetime-support-scheme-act-2013.txt`
  (text sha256 0347276c...ac2c per its `.meta.json`). The Current Titles list of 22 September 2026 gave the same
  version.
- **Commencement.** ss 4 to 6, Parts 3 to 6 and Schedule 1 commenced on 1 July 2014 (legislative history: "1.7.2013
  except ss 4-6, Pts 3-6 & Sch 1 -- 1.7.2014"), so "the commencement of section 5" in ss 5 and 6 is 1 July 2014.
- **Regulations.** The Motor Vehicle Accidents (Lifetime Support Scheme) Regulations 2014 (version 30.5.2017) are
  deposited beside the Act and were read. They define "medical expert" for Schedule 1 (r 4) and authorise releases of
  information under s 48(1)(b) (r 5); they prescribe no s 4(1)(l) need, no s 33 relevant determination, no s 36(1)(e)
  matter and no cost excluded under ss 34(10)(b)(ii), 36(6)(b)(ii) or 38(11)(b)(ii). So nothing in them changes an
  answer here, and those regulation-making limbs are encoded as empty (a later regulation would change the answers).
- **The LSS Rules** (made by the Governor under s 56) are **not deposited**. They set the eligibility criteria
  (lifetime and interim), the application periods beyond the s 25(7) floor, the excluded needs, the payment limits, the
  approved-provider requirements and the s 38(3) extensions. Each is asked as a fact. A ledger entry for them would be
  a source to deposit, not an encoding; none was raised (South Australia has no requirement ledger).
- **Not encoded here, linked by subject:** the Civil Liability Act 1936 provisions this Act inserted (s 58A, damages
  for participants, and the others in Schedule 2 Part 2) live in that Act
  (`../../../civil-liability-act-1936/encodings/baseline-2026-11/`); the Motor Vehicles Act 1959 provisions it inserted
  (ss 126A, 127B, 127C) and the rights of recovery in ss 116 and 124A that s 46 borrows live in that Act
  (`../../../motor-vehicles-act-1959/encodings/baseline-2026-11/`); the Limitation of Actions Act 1936 s 36 that
  s 26(11) extends is deposited, not encoded. Cross-subject IMPORT is not possible on the stable `l4`.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, never more than one process at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were
read.

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `lss-dates.l4` | 0 | 0 | 0 | 0 |
| `lss-core.l4` | 0 | 0 | 0 | 0 |
| `lss-seat.l4` | 0 | 0 | 0 | 0 |
| `lss-seat-owner-driver.l4` | 0 | 0 | 0 | 0 |
| `lss-cases.l4` | 0 | 0 | 166 | 166 |
| `lss-cases-owner-driver.l4` | 0 | 0 | 27 | 27 |

Negative controls: with the Tribunal's 28 days changed to 27, `lss-cases.l4` failed exactly the 5 predicted assertions
(the two "by when" dates, the application on the last day, not yet applied on the last day, and the 2025 "still in
time" case); with s 45(2)'s reduction for contributory negligence removed, `lss-cases-owner-driver.l4` failed exactly
the 2 predicted (25% and 100%). Both were reverted and rechecked (164 and 27 satisfied). After the independent
verification of 2026-11-07 (ambulance and private hospital rates corrected, forks F11 and F12 recorded) all six files
were run again: 0 errors, 0 warnings, 166 and 27 satisfied.

Edges asserted: the commencement day (1 July 2014) and the day before; the last day of each 28-day period and the day
after, applied and not yet applied; a 28-day count across 29 February 2024; s 52's 28 days back across February in a
leap and a common year; 29 February plus three years (fork F1); interim days counted inclusively, including a one-day
period (fork F2); each limb of s 24(1), (3), (4), (5) and s 55(2)(a) in turn; each bar of ss 4, 27 and 28 in turn,
with age 17 and 18 for s 3(1) "child"; each defence in s 45(6), (7) for the role it serves and the role it does not;
contributory negligence at 0, 25 and 100 per cent.

## Seats

**The injured person (required).** The person injured in a motor vehicle accident who asks whether the Lifetime
Support Scheme covers them, how and by when to apply, whether they must be accepted, what it pays for and at what rate,
what they must do for an assessment, how to challenge a decision and at whose cost, what to do before leaving
Australia, and what they can be fined (`lss-seat.l4`, 23 questions). A person with lawful authority to act for them may
ask on their behalf (s 54).

**The owner or driver (second seat).** The owner or driver of an uninsured vehicle, or another person partly at fault,
from whom the Authority recovers the present value of its liabilities for a participant (ss 45, 46), with the defences
in s 45(6) and (7) (`lss-seat-owner-driver.l4`, 3 questions). No mirror cases: no question is asked from both seats.

No seat for the Authority, a review officer, an expert review panel, the Tribunal, an insurer or the Minister. The
insurer's and the nominal defendant's right to apply (s 25(1)(b)) appears only as what it means for the injured person.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed: the 2014 Regulations were read (they set
  nothing used here); the LSS Rules are not deposited, so their content is asked.
- **The actors the text names.** Followed: the injured person or participant, a person with lawful authority to act
  for them, the Authority, its assessors, review officers, expert review panels, the Tribunal, insurers, the nominal
  defendant, the owner and driver, a prescribed authority.
- **Judgments answered conditionally.** Followed: the Authority's satisfaction (s 26), its determination to accept a
  buy-in (s 6(1)(c)), its election to pay (s 28(2)), "reasonable" requests (s 31), "necessary and reasonable" needs and
  expenses (s 27), fault, contributory negligence and shares of responsibility (s 45), the defences "to the
  satisfaction of the court" (s 45(6), (7)), good faith (s 49), a reasonable excuse (s 34(6)).
- **The Act's definitions worked out; borrowed terms asked.** Followed: "child" (s 3(1)), "treatment, care and support
  needs" (s 4), "eligible person" (s 24), "threshold determination" and "relevant determination" (s 33), "present
  value" (s 45(4)) are worked out; "motor vehicle", "use", "road race", "work injury", "nominal defendant", "approved
  provider", the LSS Rules' criteria, the right of recovery under Motor Vehicles Act ss 116 and 124A are asked.
- **One case:** one injured person and one motor vehicle accident (for ss 45 and 46, one person from whom the Authority
  recovers).
- **The Act's terms with plain glosses:** in the `@desc`s and comments.
- **Machinery out:** Part 2, ss 56, 57, Schedule 1 except cl 6(7).

## Scope

**In:** s 3 (the definitions used), s 4, s 5, s 6, s 24, s 25, s 26, s 27, s 28, s 30 to s 32 (as they bind the
participant: the s 31 duty and the s 32(2)(e) suspension), s 33 to s 38 (all of Part 5), s 39 to s 41 (the rates), s 45,
s 46, s 49, s 51, s 52, s 54, s 55(2)(a) and (b), Schedule 1 cl 6(7). s 30(3) (the Authority must certify its
assessment, with reasons, and give the participant a copy) is reflected in the s 38(3) period, which runs from notice.

**Out, and why:**

- s 5(3) (the Act also applies, for a participant, to related injuries and to whatever other injuries, needs and
  expenses the LSS Rules cover): not a separate question; whether a need is covered is asked through the s 27
  assessment and the LSS Rules inputs of "Will the Scheme pay".
- s 40(3) (a provider the Authority has not paid may recover the payment from it as a debt): the provider's remedy,
  not the injured person's.
- Part 2 (ss 7 to 23: the Authority, its board, functions, staff, accounts, report, code of conduct): machinery. s 23's
  complaints process is named in the "how can I challenge" answer for a decision Part 5 does not reach.
- s 27(5) (the Authority may pay a participant an amount to cover expenses over a fixed period, by agreement): it rests
  wholly on an agreement; nothing for the person to work out.
- s 29 (approved providers): the provider's own approval and duties (s 29(4), $10 000); only its effect on payment
  (s 28(1)(c)) is in.
- s 30(1), (2), (4), s 32(1), (3): the Authority's duty and method to assess; no question for the person beyond ss 31,
  38.
- Part 7 except ss 45, 46 (the Fund, the Authority's determination of contributions, the LSS Fund levy collected on
  vehicle registration): the levy's amount is set by a Minister's scheme that is not deposited, and it is not a claims
  provision.
- s 47 (no contracting out), s 50 (Treasurer's guarantee), s 53 (extraterritorial intention): no fact to decide; s 53
  does not displace s 24(1)(c)'s South Australian accident.
- s 48 and regulation 5 (release of information by the Authority and insurers): a discretion over information, with no
  fact for the person to decide.
- s 55 except (2)(a), (b): the agreement and the payments between the Authority and the prescribed authority.
- ss 56, 57 (LSS Rules, regulations): machinery.
- Schedule 1 except cl 6(7) (the panels' constitution and procedure; cl 3(2), that a medical expert who treated or
  examined the person may not sit on their panel, is noted, not asked).
- Schedule 2 Parts 1 to 5 (amendments to the Civil Liability Act 1936, Motor Accident Commission Act 1992, Motor
  Vehicles Act 1959 and Stamp Duties Act 1923): they live in those Acts. Part 6 (transitional) concerns those Acts and
  the Motor Accident Commission's contribution; Part 7 (review by a Parliamentary committee) is spent. The 2019 SACAT
  transitional provision (unexercised District Court appeals) is spent.

## Forks (decided case by case, ruling of 2026-11-05; F11 and F12 recorded after the verification of 2026-11-07)

Each is the provision, the function, the answer taken, and the other reading, for a reviewer to overrule.

- **F1** s 25(7) and s 26(11), `moved on by months` (lss-dates.l4): "within 3 years from the date of the ... accident"
  and "the period of 3 years" end on the same day of the month three years later, or that month's last day where it is
  shorter (29 February 2016 gives 28 February 2019). The other reading takes the Acts Interpretation Act 1915 (SA) rule
  (not deposited) or ends the period on 1 March.
- **F2** ss 35(2), 37(3), 38(3), 52(1), 26(10), (11), `plus days` and `the days of the period from`: "within 28 days of"
  or "after" a day ends on that day plus 28; "at least 28 days before leaving" ends on the day of leaving less 28; a
  period of interim participation counts its first and last days. The other readings exclude the day of leaving ("clear
  days") or count the interim period exclusively (one day less).
- **F3** s 5(1)(b), `does the Act apply to the injury (s 5)`: a pre-commencement injury without s 6 acceptance answers
  "no", taking "where ... accepted into the Scheme under section 6" as a "where" condition (ruling of 2026-11-05 (b)).
  The other reading treats s 5(1) as an unclosed list and answers "not covered".
- **F4** s 6(1)(a), (3), `can the person buy in (s 6)` and `may this applicant apply (ss 25, 6)`: a person with lawful
  authority to act for the injured person may make the s 6 application (general law; s 54 speaks only of participants,
  "without limiting any other provision or law"); the nominal defendant may not, because s 6(1)(a) requires "the person"
  to apply and s 25 names the nominal defendant apart from insurers. The other readings bar the representative, or let
  the nominal defendant in because s 6(3) bars only "an insurer".
- **F5** s 4(2) and s 27(3)(c), `will the Authority pay (ss 4, 27, 28)`: an LSS Rules declaration of an excluded need
  does not reach a need the Authority determined under s 4(1)(m) ("subject to subsection (1)(m)"), but an LSS Rules
  exclusion from s 27 (s 27(3)(c)) still does. The other reading lets s 4(1)(m) override both.
- **F6** s 39, `at what rate does the Authority pay (ss 39 to 41)`: a bulk billing arrangement may cover any of the
  listed services (s 39(1)(c) "other treatment expenses" read widely). The other reading confines it to treatment,
  leaving attendant care and the like to s 41.
- **F7** s 45(3), `can the Authority recover from this person (s 45)`: a person other than an owner or driver who was
  partly at fault is liable for their share on s 45(3)'s own words, whether or not the vehicle was insured. The other
  reading confines s 45(3) to the section's subject (its heading: "vehicles not insured under State law") and s 45(1)'s
  conditions.
- **F8** s 26(2)(b), `must the Authority accept the person (s 26(1) to (3))`: an application not "duly made" frees the
  Authority from the duty to accept but not from its power to accept a person it is satisfied is eligible (s 26(1)).
  The other reading makes a duly made application a condition of any acceptance.
- **F9** s 27(1) "while the person is a participant" and s 28(6) "while ... suspended": read by the day the expense was
  incurred or the service provided, asked as a fact. The other reading looks to the day of payment.
- **F10** ss 35, 37, 38, 52, `the timing of`: a step taken before the day the period starts (an application dated before
  the determination) is in time; the encoding does not ask whether it was premature.
- **F11** s 25(7) and s 26(10), `is the application within the period the Act guarantees (ss 25(7), 26(10))` and
  `the last day the Act guarantees for applying (ss 25(7), 26(10))`: s 25(7)'s 3-year floor is for an "initial
  application"; s 26(10) only requires the LSS Rules to add interim participation to whatever period they set for an
  application to become a lifetime participant. The encoding takes that period to be at least the 3 years, so 3 years
  plus the interim days is treated as guaranteed, and the answer says it rests on this fork. The other reading: the Act
  guarantees nothing for a lifetime application after interim participation beyond adding the days to the Rules' own
  period, so only the plain 3 years is guaranteed.
- **F12** s 45(5) to (7), `can the Authority recover from this person (s 45)`: a person who was both owner and driver
  is treated as owner (s 45(5)) and has neither defence: not s 45(6), since no one else drove, and not s 45(7), taking
  the driver's defence as one for a driver who is not the owner. The other reading lets an owner-driver use s 45(7),
  since on its words they drove with the owner's authority and may have reasonably believed the vehicle was insured.

## What the Act turns out to say (findings)

1. **The Scheme is no-fault.** s 5(2): the Act applies "even if the injured person was at fault". Asserted (the
   application answer says so).
2. **The Act fixes almost none of the Scheme's numbers.** Eligibility criteria, application periods, excluded needs,
   payment limits and extensions of time are all left to the LSS Rules (not deposited). The Act's own floor is s 25(7):
   the Rules must let an initial application be made within 3 years of the accident. For a lifetime application after
   interim participation, s 26(10) adds the interim days to the Rules' own period; that the 3 years plus those days is
   guaranteed is fork F11. Asserted.
3. **s 26(11) changes the Limitation of Actions Act from outside it.** Any period of interim participation is added to
   the 3 years in s 36 of the Limitation of Actions Act 1936, "and that section will be taken to have been modified
   accordingly"; a reader of that Act alone would miss it. Asserted.
4. **Ambulance has a maximum fee only if the Minister names it.** s 40 covers conveying by ambulance, but s 41(1)(a)
   to (d) do not list it; a maximum can be fixed for it only after the Minister identifies it for s 41 by Gazette notice
   (s 41(1)(e)). Until then, unless bulk billed, ambulance is paid at the customary rate (s 40(2)(c)); after, at the
   maximum fixed (s 40(2)(b)). Asserted.
5. **s 45(3) reaches beyond uninsured vehicles on its words** (fork F7). Asserted.
6. **The Authority's discretion to pay anyway (s 28(2)) covers s 28(1) only**, not services provided while
   participation is suspended (s 28(6)). Asserted.
7. **A prior damages award does not bar a buy-in.** s 24(3) bars a person awarded damages for future care needs, but
   s 24(4) lifts the bar for a person who has applied under s 6. Asserted.
8. **s 52 carries no penalty.** Failing to give 28 days' notice of leaving Australia exposes the participant to
   suspension while absent (s 52(2)(b)), and so to s 28(6), not to a fine; the Authority may also waive or reduce the
   period. Asserted.
9. **Refusing an expert review panel's request carries no penalty for the injured person.** Schedule 1 cl 6(1) lets a
   panel ask the person to meet it, supply documents and submit to examination; the only penalty in cl 6 (cl 6(5),
   $5 000) is for a medical expert under cl 6(4). For a needs assessment, by contrast, s 31 is a duty and s 32(2)(e)
   lets the LSS Rules suspend participation.
10. **The owner is liable even when not driving**, jointly with the driver or alone (s 45(5)), unless the owner proves
    the driver had no authority (s 45(6)); the driver's defence (s 45(7)) needs both authority (or a reasonable belief
    in it) and a reasonable belief that the vehicle was insured. A person who was both owner and driver has neither
    defence (fork F12). Asserted.
11. **Numbering and renaming.** s 2 was omitted under the Legislation Revision and Publication Act 2002, so the Act runs
    s 1, s 3; ss 35 and 37 were substituted in 2019 to send reviews to the Tribunal rather than the District Court.

## Before relying on it

Deposit and encode the current LSS Rules (they decide eligibility, periods and limits); check the register for a
version later than 2 December 2019; have a lawyer review forks F1, F2, F4, F7, F11 and F12; encode the Limitation of Actions Act
1936 s 36 and link it; run an independent test pass.
