# Fair Work Act 1994 (SA) -- baseline encoding, the employee bringing a claim

> **Edition.** The text encoded is the register's current version of 22 August 2026, fetched from
> www.legislation.sa.gov.au on 6 November 2026 (the unauthorised RTF; the authorised version is the PDF). Unlike most
> South Australian texts in Commons it does **not** come from the Open Australian Legal Corpus (collected 10 March
> 2025), so that corpus's "may be out of date" warning does not apply. Amendments listed as uncommenced in the
> legislative history (Fair Work (Registered Associations) Amendment Act 2024, ss 3-8, 15, 17(2), 18, among them
> s 12(1) and s 32(1)) are not incorporated. Check legislation.sa.gov.au before relying on it.

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill (and its
`references/regulative.md`), from the seat of the individual to whom the law is applied, with the design defaults ruled
on 2026-10-18. A small date module (`safw-dates.l4`, built-in date functions only, no daydate import), a seat-neutral
core (`safw-core.l4`) that holds every rule, a seat layer (`safw-seat.l4`) that asks the questions and restates none,
and one case file (`safw-cases.l4`). Answers are named outcomes (enumerations), booleans where the text gives a "means"
definition or an "if" condition, numbers for amounts and weeks, dates for time limits, and one `MAYBE NUMBER` (back pay,
`NOTHING` where SAET has directed otherwise and the Act fixes no amount); no `MAYBE BOOLEAN`, so no `NOTHING-kind` tags.
Where the text says no in its own words ("means", "if", "only if", "may only", "must not", "does not apply", a period
it fixes) the outcome is a "no: ..." naming the provision; where a list is not closed or the text is silent the outcome
says "not covered", following the 2026-11-04 and 2026-11-05 rulings in substance. No REFUSE, no `#ASSERT REFUSED`, no
BECAUSE outside `LEST BREACH`. No pipeline, no coverage table, no independent test pass, no human gate. Not for public
use as advice.

**Seven regulative rules.** Every time limit is written as a `DEONTIC` (`PARTY ... MUST ... WITHIN` the days to the last
day, `HENCE FULFILLED`, `LEST BREACH ... BECAUSE`): s 31 (monetary claim, 6 years), s 72B(6)(b) (severance application,
21 days), s 99D(3) (outworker's claim, 6 months), s 104A(9) (civil penalty proceedings, 6 years), s 106(1) (unfair
dismissal application, 21 days), s 110(3) (the employer's costs application, 14 days) and s 235(2) (prosecution,
2 years). One helper runs any of them with `EVALTRACE` (`WAITUNTIL` the day, then the step on that day) and the seat's
questions take plain dates: no exported question takes a `DEONTIC` or `EVENT` input. The 14-day windows in ss 99E(2)
and 99F(1) are permissions (`may`), not duties, so they are plain comparisons.

This is the first encoding of the Act; nothing existing was touched.

## Edition

- **Act:** Fair Work Act 1994 (SA), register version 22.8.2026 (Chapter 3 as amended by the Nurse and Midwife to Patient
  Ratios Act 2025, Sch 2 cl 1; Chapters 1 and 2 as at 1.1.2026, after the Fair Work (Worker Entitlements) Amendment Act
  2025), deposited at `../../registers/source-bundle/fair-work-act-1994.txt` (text sha256 45c9be34...5b13d385d per its
  `.meta.json`).
- **Regulations not deposited**, so inputs: employment excluded by regulation (s 6(b)); outworkers brought in by
  regulation (s 5(4)(b)); the s 105A(2) exclusions (probation, short-term casuals and the rest); the Sch 8 cl 1(3)
  events disregarded in continuous service (assumed none) and the cl 3 rules.
- **Figures not in the Act:** the current indexed amounts for s 105A(1)(a) ($100 322 (indexed)) and s 109(3)
  ($33 100 (indexed)) are inputs; the s 4(4) formula is encoded (`safw the indexed amount (s 4(4))`) but the State
  earnings statistics it needs are not deposited. The SAET minimum standard for severance payments (s 72B(1)) is not
  deposited, so no severance amount is computed.
- **Borrowed, asked as facts:** "national system employer" and "excluded subject matter" (s 6(aa), Commonwealth Fair
  Work Act 2009 and the Fair Work (Commonwealth Powers) Act 2009 (SA)); "public sector employee" (Public Sector Act
  2009); "apprentice" (South Australian Skills Act 2008); "domestic partner" (Family Relationships Act 1975); a
  "workplace law" giving a court jurisdiction (s 9(2)); "industrial instrument" coverage. "Month" and "year" are calendar
  months and years (Acts Interpretation Act 1915, not deposited).

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, one process at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read.

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `safw-dates.l4` | 0 | 0 | 0 | 0 |
| `safw-core.l4` | 0 | 0 | 0 | 0 |
| `safw-seat.l4` | 0 | 0 | 0 | 0 |
| `safw-cases.l4` | 0 | 0 | 232 | 232 |

Negative control (on a scratch copy): with the s 106(1) period cut from 21 to 20 days the cases failed exactly the
3 predicted assertions (the two last-day dates and the application on the 21st day); with the s 110(3) period also cut
to 13 days, exactly 4 (adding the employer's costs application on day 14). The copy was discarded.

Edges asserted: the last day and the day after for every time limit (s 31 from 15 March and from 29 February; s 99D(3)
from 31 August into a common and a leap February; s 104A(9); s 106(1) from 1 March and across the year end; s 72B(6)
from the notice and from the termination, and with both windows; s 235(2) from 29 February; s 111 from 30 November);
an application on the event day itself and the day before it; the s 105A(1)(a) threshold exactly met and one dollar
under; the s 109(3) cap with both limbs equal and one just over; the designated employer paying on day 14 and day 15,
paying more than the claim, and not referred to; the s 104A(4), (5) count with none, some and all contraventions after
an earlier penalty; the Sch 8 notice periods on each anniversary and the day after, the 45th birthday itself, and two
years' service completed on the anniversary; every limb of every "or" (s 5, s 4 contract of employment, s 6, s 9(1),
s 32, s 104A(6), s 115, s 223(1)) and every conjunct of every "and" (s 5(1), s 99D(4), (5), s 104(4), s 109(4),
s 110, s 115(m), s 17(2)).

## Seat

**The employee (required): the employee or former employee who brings a claim under the Act** (`safw-seat.l4`,
36 questions): for unpaid money (as the employee, a minor, the association acting for them, or the personal
representative or a beneficiary of an employee who has died), for severance on redundancy, as an outworker against the
business that gave out the work, for a civil penalty for unpaid entitlements, for unfair dismissal relief, and for
redress after dismissal for a prohibited reason or for taking part in industrial proceedings. Every question is one
that person would ask: "Does the Act apply to me?", "Can the Court hear my claim?", "Is it in time?", "By what date?",
"Who can claim for me?", "Will I get interest?", "Can I be ordered to pay costs?", "What can SAET order?", "What is the
most compensation?", "How much notice must I get?", "Was it an offence?". Provisions addressed to SAET, the Court, the
President and inspectors are encoded as what they mean for the person; their judgments are inputs worded "SAET is
satisfied ...".

No seat for SAET, the Court, the President, an inspector or the Minister. No second party seat (the employer, the
responsible contractor) in this encoding; one could be added beside this one over the same core.

The 2026-10-18 defaults:

- **The Act alone.** Followed; regulations and SAET's standards are not deposited, so their content is asked as facts
  (see Edition).
- **The actors the text names.** Followed: the employee, the employer, the outworker, the apparent responsible
  contractor, the designated employer, an association, a registered association, an inspector, SAET, the South
  Australian Employment Court, the President, the personal representative and beneficiaries of a dead claimant.
- **Judgments answered conditionally.** Followed: "satisfied" (s 17(2), s 104A(2), s 109, s 110, s 99G(3)), "good
  reason" (s 34(1)), "considers" (s 109(1)(c)), "cogent reasons" (s 109(1a)), "reasonable grounds" (s 99D(1)),
  "deliberate" and "systematic pattern" (s 104(4)), "harsh, unjust or unreasonable" (s 108), "serious misconduct"
  (Sch 8 cl 1(1)(b)), "could not reasonably be expected" (Sch 8 cl 2(b)) are inputs.
- **The Act's definitions worked out; borrowed terms asked.** Worked out: outworker (s 5(1)-(3)), contract of employment
  and employee (s 4(1)), monetary claim (s 30), prohibited reason (s 115), deliberate for the Crown or a body corporate
  (s 104(5)), the s 4(4) indexation. Borrowed: listed above.
- **One case:** one employment, one claim.
- **The Act's terms with plain glosses:** in the `@desc`s and answers.
- **Machinery out:** see Scope.

## Scope

**In:** s 4(1) (contract of employment, employee, public employee), s 4(4); s 5; s 6; s 9; s 10(1), (6), (9) (as the
s 10 heads of a monetary claim); s 17(2); ss 30-36; s 72B(5)-(8); s 99B; ss 99D-99G; ss 104, 104A, 104B(3), 104C;
ss 105, 105A, 106, 108, 109, 110, 111; Sch 8 cll 1, 2; s 115; s 116B; s 223; s 233; s 235(2); the transitional clause of
the Fair Work (Worker Entitlements) Amendment Act 2025 (Sch 1 cl 4).

**Out, and why:**

- ss 1, 3, 4AA, 4A, 7, 8, 11-16, 18-29 (objects, the Crown, SAET's jurisdiction and processes, conferences,
  representation, registered agents, concurrent appointments): machinery or procedure the person cannot act on; s 25 on
  representation is a candidate for a later layer.
- s 10(2)-(5), (7), (8) (specific performance and injunctions): the Court's remedies in its discretion; a claim under
  s 10 is in.
- Chapter 3 Part 1 Divisions 1-2 (ss 66-72A: wages accrual, payment, the minimum standards and Schedules 3-5 on sick,
  bereavement, family and domestic violence, annual and parental leave): these are the entitlements a claim is for,
  not the claims machinery; they deserve their own encoding (s 67 accrual is not used to decide when a sum "became
  payable", which is asked as a date). s 72B(1)-(4) (setting the severance standard) is machinery.
- Chapter 3 Parts 2-4 (enterprise agreements, awards, wage principles), Part 3A Divisions 1-2 except s 99B (code of
  practice), s 99H (the contractor's recovery from others), s 99I (offences against the scheme, not the outworker's
  claim), s 99J (non-derogation, noted), Part 5 Division 1 (records; relevant only as a s 104(6) factor), Part 7
  (exemptions, licences for slow workers).
- s 105A(2)-(3) are taken only as "the regulations exclude you" (the regulations are not deposited); s 108(2) factors
  are SAET's judgment and are in only through the Sch 8 question.
- Chapter 4 except ss 115 and 116B (registration and rules of associations, entry powers), Chapter 6AA (the Consultative
  Council), Chapter 6 except ss 223, 233, 235(2) (inspectors' powers, compliance notices, other offences, proof,
  regulations), Schedules 1, 2, 2A (transitional and continuity), 6, 7, 9, 10, 11 (Conventions; s 108(2)(a) asks SAET
  to have regard to Schedule 7, which stays SAET's judgment), Sch 8 cl 3 (rules by regulation, not deposited).
- s 232 (general defence) and s 116A (offences against freedom of association): defences and offences in the
  employer's or another person's position, for an employer seat.

## Forks (decided case by case, ruling of 2026-11-05)

Each is the provision, the function, the answer taken, and the other reading, for a reviewer to overrule.

- **F1** all time limits, `safw-dates.l4`: a period of days "after" or "from" a day excludes that day (21 days from
  1 March ends on 22 March); months and years end on the corresponding day, or the month's last day where there is
  none (31 August plus 6 months is 28 or 29 February; 29 February plus 6 years is 28 February). A last day on a weekend
  or holiday is not moved. The other readings count the event day, or move a last day off a weekend.
- **F2** s 106(1), `safw the last day to apply for unfair dismissal relief (s 106(1))`: "before the end of a period of
  21 days from the date the dismissal takes effect" ends at the end of the 21st day after that date. The other reading
  counts the date of effect as day 1 (last day 21 March for a dismissal taking effect on 1 March).
- **F3** s 5(4), `safw does the Act apply to my employment (ss 4, 5(4), 6)` and `safw can I make an unpaid remuneration
  claim (ss 99B, 99D)`: read literally, so Part 3A (in Chapter 3) reaches an outworker only if an award or enterprise
  agreement provision relates to outworkers or a regulation extends the Act, and the limit applies to anyone who meets
  s 5, whatever their contract. The other reading treats Part 3A, which is written for outworkers, as an implied
  exception, or confines s 5(4) to people whose contract is one only under para (d) of the s 4 definition (finding 1).
- **F4** s 31, `safw is my monetary claim in time (s 31)`: "a claim for the non-payment of superannuation contributions"
  is the s 9(1)(c) claim against the employer; a s 9(1)(d) claim for a benefit against a trustee keeps the 6 years.
  The other reading frees both.
- **F5** s 109(1a), (1b), `safw what can SAET order for my dismissal (ss 108, 109)`: "re-employment" covers (a) and (b),
  so the "alternative remedy" needing cogent reasons is compensation under (c); with fewer than 50 employees (s 109(1b))
  compensation needs no cogent reasons. Where SAET considers no re-employment appropriate but has no cogent reasons and
  the business has 50 or more employees, the answer says no remedy is settled on the facts. The other reading treats
  (b) as an alternative remedy too.
- **F6** s 99D(3), `served in time`: a claim served before the work is completed is not out of time (the Act sets only
  an outer limit). The other reading holds such a claim premature.
- **F7** s 99D(6): "work performed after the commencement of this section" includes work on the commencement day,
  16 May 2005; the date asked is the first day of the work claimed for. The other reading starts the day after.
- **F8** 2025 amending Act Sch 1 cl 4 ("conduct occurring after the commencement"), the civil penalty and workplace-law
  questions: conduct on 1 January 2026 is after the commencement. The other reading starts on 2 January 2026.
- **F9** Sch 8 cl 1(2), `safw weeks of notice (Sch 8 cl 1)`: service is "more than N years" when the termination day is
  after the N-th anniversary of the start; "at least 2 years" are completed on the 2nd anniversary; a person is "over
  45 years old" after the 45th birthday (on the birthday they are 45, not over). The other readings count service
  inclusively, or treat "over 45" as 46 or older.
- **F10** ss 99E(4), 99F, `safw the amount the apparent responsible contractor is liable for (ss 99E, 99F)`: the
  contractor's statutory liability is reduced only by a payment under s 99F after a referral under s 99E(2), each
  within its 14 days, and only to the amount claimed. A payment outside that route may discharge the debt in fact, but
  the encoding does not net it. The other reading nets any payment by the employer.
- **F11** s 36, `safw can I recover my costs of my monetary claim (s 36)`: the s 36(1)(a) costs of valuing lost
  superannuation are answered for a superannuation claim at any stage; s 36(3) ("a claim under section 10") sends a
  s 10(1)(b) debt, though a "monetary claim" under s 30, to the s 10(6) costs rule.
- **F12** s 116B(1), s 223(1): an act or a reason the provision does not list answers "not covered" (the prohibition is
  limited in its own wording); s 115 is an "if" definition, so a reason outside it answers "no".
- **F13** s 32, `safw who may make the monetary claim (s 32)`: anyone not named answers "not covered" (s 32 enables and
  does not close the list).
- **F14** s 9(1)(a) workplace-law claims for conduct before 1 January 2026: "not covered", because the 2025 amendments
  apply only to later conduct and the text before them is not deposited.
- **F15** s 72B(6), `safw within 21 days after (s 72B(6)(b))`: an application made before the notice is given or the
  employment terminated is outside the window. The other reading treats it as premature but valid once the event
  occurs.

## What the Act turns out to say (findings)

1. **s 5(4) reaches further than it looks.** "Apart from this Chapter, the other provisions of this Act apply to
   outworkers if (and only if)" an award or enterprise agreement provision relates to outworkers or a regulation extends
   the Act. s 5 is in Chapter 1, and the outworker recovery scheme (Part 3A) is in Chapter 3, so read literally even the
   outworker's own unpaid remuneration claim needs that trigger (F3). Asserted.
2. **Most South Australian private sector employees are outside the Act.** s 6(aa) excludes employment with a national
   system employer except for an "excluded subject matter"; the Act's claims are in practice for State public sector,
   local government and other non-national-system employment. Asserted (as an input).
3. **The 2025 amendments look forward only.** The Fair Work (Worker Entitlements) Amendment Act 2025 put the civil
   penalty Division (ss 104-104C, deleted in 2017) back, added "workplace law" to s 9(1) and recast ss 34-36; its Sch 1
   cl 4 applies all of that only to conduct after 1 January 2026. A contravention on 31 December 2025 gets no civil
   penalty under s 104. Asserted.
4. **A whole course of conduct can cost only $25 000.** s 104A(4) makes contraventions from one course of conduct a
   single contravention, unless committed after an earlier civil penalty (s 104A(5)). Five unpaid fortnights in one
   course of conduct carry at most $25 000. Asserted.
5. **s 36(3) and s 30 pull apart.** s 30 counts a sum or debt under s 10 as a "monetary claim", but s 36 "does not apply
   in relation to a claim under section 10", whose costs follow s 10(6) (District or Magistrates Court rules). So the
   no-costs rule of s 36(1) protects award and agreement claimants but not a common law debt claimant. Asserted.
6. **No extension of the 21 days in Part 6.** s 106(1) fixes 21 days and the Part gives SAET no power to extend; any
   power would be in the South Australian Employment Tribunal Act 2014 (not deposited). A referral from another
   authority escapes the limit (s 106(3a)). Asserted.
7. **The indexed amounts are not in the text.** s 105A(1)(a) and s 109(3) state $100 322 and $33 100 "(indexed)"; the
   figures for the current year depend on State earnings statistics under s 4(4), so they are inputs. The year
   Parliament fixed each amount (needed for the s 4(4) divisor) is not stated in the section either.
8. **s 99E uses two names for one person.** s 99E(2) defines "the designated employer"; s 99E(3)(b) serves the copy "on
   the actual employer". Read as the designated employer.
9. **Gaps in numbering:** s 99G has (1) and (3) (s 99G(2) deleted by 63/2016); Part 6 has no Division 3 (deleted by
   3/2005, s 107 with it). Nothing turns on either.
10. **Who prosecutes under s 116B is not said.** s 223(3) lets the employee prosecute a s 223 offence; s 116B has no
    equivalent, so the employee's compensation and re-employment under s 116B(2) depend on a prosecution the Act does
    not give them. Both need a conviction first, within 2 years (s 235(2)).
11. **Schedule 8 has no remedy of its own in this Act.** Notice and the chance to respond are duties on the employer;
    their breach goes to whether a dismissal was harsh, unjust or unreasonable (s 108(2)(b)), or to a money claim for
    pay instead of notice (s 9(1)(a), a sum due under this Act), not to a separate penalty.
12. **No fee for an unfair dismissal application** (s 106(4)), and an award or agreement claimant at first instance
    cannot be ordered to pay costs (s 36(1)); the costs risks are on appeal (s 36(2)), in civil penalty proceedings
    (s 104C) and in unfair dismissal cases that are not settled or are discontinued late (s 110). Asserted.

## Before relying on it

Check the register for a version later than 22 August 2026; deposit the Fair Work Regulations and the current indexed
figures, and SAET's severance standard, and replace the inputs that stand for them; deposit the South Australian
Employment Tribunal Act 2014 for extensions of time and representation; have a lawyer review forks F2, F3, F5 and F9
and findings 1 and 5; add an employer seat; run an independent test pass.
