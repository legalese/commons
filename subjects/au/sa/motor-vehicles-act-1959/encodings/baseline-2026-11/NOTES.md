# Motor Vehicles Act 1959 (SA), Part 4 (compulsory third party insurance) -- baseline encoding, the claimant and the insured owner or driver

> **Warning.** The texts encoded here are taken from the Open Australian Legal Corpus (South Australian legislation last
> collected on 10 March 2025): the Act as at 7 November 2024 and the Third Party Insurance Regulations as at 1 November
> 2021. They are unofficial and may be out of date: later amendments are missing. Check legislation.sa.gov.au before
> relying on anything here.

## Method

**Baseline.** Written straight from the deposited texts with the `writing-l4-rules` skill (and its
`references/regulative.md`), from the seat of the individual to whom the law is applied, with the design defaults ruled
on 2026-10-18. A seat-neutral core (`mva-core.l4`) holds every rule, with five regulative rules (s 126A(1) with reg
4(1)(b); s 127(2)(b); s 127(2)(c); s 126A(4); s 124AB(1) with its 95% rate); two seat layers restate none of them and
run the regulative rules by `EVALTRACE` inside exported questions that take only plain facts. No REFUSE, no
`#ASSERT REFUSED`, no BECAUSE except in `LEST BREACH`. Answers are named outcomes (enumerations) rather than
`MAYBE BOOLEAN`, so no `NOTHING-kind` tag is used; where the text does not answer, the outcome says so in words
("section 133 does not deal with ...", "s 114 does not deal with this ground"), and where the text says no in its own
words the outcome is a "no: ..." naming the provision, which follows the 2026-11-04 and 2026-11-05 rulings in substance.
No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

This is the first encoding of the Act; nothing existing was touched. The Victims of Crime Act 2001 baseline
(`subjects/au/sa/victims-of-crime-act-2001/encodings/baseline-2026-10/ctp-core.l4`) also encodes ss 99(3), 115, 116 and
126A of this Act, for its own s 17(5)(c) question; that encoding stays as it is, and this one was written separately
(the stable `l4` cannot IMPORT across subjects). The damages themselves are assessed under the Civil Liability Act 1936,
Part 8, which is not encoded here.

## Edition

- **Act:** Motor Vehicles Act 1959, corpus document `south_australian_legislation:2024-11-07/1959.53.un`, deposited at
  `../../registers/source-bundle/motor-vehicles-act-1959.txt` (sha256 50799117...78019a6e as committed), Part 4 from
  line 2693.
- **Regulations that set its numbers:** Motor Vehicles (Third Party Insurance) Regulations 2013, corpus document
  `south_australian_legislation:2021-11-01/2013.164.un`, deposited at
  `subjects/au/sa/motor-vehicles-third-party-insurance-regulations-2013/registers/source-bundle/motor-vehicles-third-party-insurance-regulations-2013.txt`
  (sha256 188bd073...4e7b022f as committed); regs 4, 5 and 6, quoted in `mva-core.l4`.
- **Not deposited, so inputs:** the CPI figures for s 124AB(4); the policy terms the CTP Regulator determines (s 104(1)(b));
  the Magistrates Court scale of costs (s 127C(4)); the forms the Minister and the CTP Regulator approve.
- **Coverage dates.** Accidents on or after 1 July 2013, the day ss 126A, 127B and 127C and the Regulations began
  (Lifetime Support Scheme Act 2013, Sch 2 cl 22(2), (4), (5), in the Act's deposit). An earlier accident answers
  `not covered: an accident before 1 July 2013`, asserted.

## Checks

Stable `l4` of VS Code extension 1.6.98 (`bin/win32-x64/l4.exe run <file>`), `JL4_LIBRARY_PATH` unset, run from this
folder, at most two processes at a time. `l4 run` exits 0 even when an assertion fails, so the diagnostics were read.

| File | Errors | Warnings | Assertions written | Satisfied |
|---|---|---|---|---|
| `mva-dates.l4` | 0 | 0 | 0 | 0 |
| `mva-core.l4` | 0 | 0 | 0 | 0 |
| `mva-seat.l4` | 0 | 0 | 0 | 0 |
| `mva-seat-insured.l4` | 0 | 0 | 0 | 0 |
| `mva-cases.l4` | 0 | 0 | 131 | 131 |
| `mva-cases-insured.l4` | 0 | 0 | 62 | 62 |

Three `#TRACE`s carry an `-- expect:` line (two breaches by the claimant, one residual full-excess obligation), each read
and as expected. Negative control: with the 30 days of grace changed to 31 and the $25 000 costs line to $25 001, the
claimant's cases failed exactly twice, as predicted; the constants were restored.

Every expected value was worked by hand from the text, with the edges: the last day of registration, of the 30-day grace
(30 July after a 30 June expiry) and the day after; 6 months from 31 August (28 February, and 29 February in a leap
year) and from 15 March (15 September, day 184) and the day after; 21 days across a month and a year end, and with 7
extra days; age 15 and 16; $25 000, $25 001, $100 000 and $100 001; a blood alcohol concentration of .1 and .099; fault
of 25% and 26%; payment on the last day of "1 month following" a first request (31 January to 28 February) and the day
after; a CPI-indexed $460 that rounds up ($599.15 to $600) and one that does not ($690).

## Seats

**1. The claimant (required): the person injured in a motor accident, or the person claiming for a death,** who brings
a compulsory third party claim under Part 4 (`mva-seat.l4`, 24 questions). Every question is one that person would ask:
"Does my injury count?", "Was the vehicle insured?", "Who answers my claim?", "By when must I give my notice of claim?",
"What must it include?", "Did I give it in time, and what follows?", "May I start court proceedings?", "Can I recover
from the insurer directly?", "Must the insurer pay my child's treatment and care?", "Can my legal costs be paid?",
"May this person act on my claim for a fee?". Provisions addressed to the insurer, the nominal defendant or the court
are encoded as what they mean for the claimant: a date, a bar on proceedings, a defence the insurer does not have.

**2. The insured owner or driver** against whom a claim is made, including the driver of an uninsured vehicle facing the
nominal defendant (`mva-seat-insured.l4`, 10 questions): the duties after an accident (s 124), the steps that need the
insurer's consent (s 126), what the insurer or the nominal defendant can recover (ss 116(7)-(7e), 123, 124A, 124AB), and
indemnity (s 113A). Part 4 puts these duties and liabilities on that person, and they are what a person answering a
claim meets. Mirror cases: the period of grace (s 99A(8)) and s 113A are asked from both seats, with answers that agree.

No seat for the insurer, the nominal defendant, the CTP Regulator, the Registrar, the Minister or the court.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed: the Third Party Insurance Regulations (regs 4-6)
  are brought in. The CPI figures, the CTP Regulator's policy terms and the Magistrates Court scale are not deposited and
  are inputs or named in the answer.
- **The actors the text names.** Followed: claimant, injured person, insurer, insured person, owner, driver, person in
  charge, nominal defendant, court, organiser of a road race.
- **Judgments answered conditionally.** Followed: "as soon as reasonably practicable", "substantially prejudiced",
  "reasonable cause", "exceptional circumstances", "prejudice of the insurer", "just and reasonable", "the justice of the
  case", "could not reasonably be expected to have known", "necessary and reasonable", "such longer period as may be
  reasonable" are inputs, or named in the answer as the court's to make.
- **The Act's definitions worked out; borrowed terms asked.** Followed: "caused by or arising out of the use of a motor
  vehicle" (s 99(3), (3a), (4)), "uninsured motor vehicle" (s 116(1)), the policy's period with its grace (s 99A(8)),
  the prescribed amount (s 124AB(3)-(5)) and the s 127C thresholds are worked out; "terrorist act", "road", "legal disability",
  "Lifetime Support Scheme participant", the Road Traffic Act s 43 offence and the CPI are asked.
- **One case.** One accident, one claim, one insured person.
- **The Act's terms with plain glosses.** Followed: the outcome names keep the Act's words; `@desc`s gloss them.
- **Machinery out.** Followed: approved insurers, premiums, the nominal defendant's funding, the Minister's and the CTP
  Regulator's powers.

## Scope

**In** (Part 4 of the Act, the provisions a claimant, or an insured person answering a claim, meets): s 99(1) (bodily
injury, participant, road race), (3), (3a), (4); s 99A(8), (10), (17), (19) with s 109; s 104(1)(a), (2); s 112; s 113
with s 117 (noted); s 113A; s 114; s 115(1), (3), (4); s 116(1)-(5), (7)-(7e); s 118A(3); s 118B (applies s 126A, s 127,
s 127B to nominal defendant claims: used, not encoded separately); s 123; s 124(1)-(6b) (the s 124(5) fine only); s 124A(1)-(4);
s 124AB; s 124AC; s 126; s 126A; s 127(2), (6), (6a), (7) (named); s 127B(2)-(4); s 127C; s 133; s 134. Regulations:
regs 4, 5, 6.

**Out, and why:**

- s 99A(1)-(7), (9)-(9c), (11)-(16), (18); ss 101, 105, 107, 116A, 119, 120, 121, 122, 128, 129A, 131: premiums, the
  choice and approval of insurers, policy machinery and funding -- machinery, not what a claimant meets.
- s 102 (the offence of driving or keeping an uninsured vehicle on a road): an offence for the owner or driver, not a
  claim provision; the encoding uses its consequence (no policy) through s 116.
- ss 110, 111, 111A: payments to the doctor, nurse or person who conveyed the injured person, to hospitals and to the
  Treasurer; s 110(3) reduces the liability by those payments (not encoded; it needs the payments as inputs and the
  prescribed fees in the Motor Vehicles Regulations 2010, not taken in).
- s 124AA (foreign awards): needs the court's comparison with a South Australian award; rare.
- ss 125, 125A, 125B: the insurer's conduct of the defence, joinder and compulsory acquisition of the vehicle.
- s 127A: control of medical charges, between the insurer and service providers.
- s 132: disqualification on an insurer's application, a court discretion.
- s 104(1)(b) and the policy's terms: not deposited.
- The Civil Liability Act 1936 (liability, damages, Part 8 limits) and the Lifetime Support Scheme Act 2013: other
  subjects.

## Forks (readings the text leaves open)

- **F1** "within 6 months after", "within 1 month following": the same day of the month that many months later, or that
  month's last day where it is shorter (31 August plus 6 months is 28 February or 29 February). `mva-dates.l4`.
- **F2** "within 21 days of", "a further period of grace of 30 days": counted from the day after, so the last day is the
  day plus 21 (plus 30); a payment, notice or copy on that last day is in time.
- **F3** s 99(3) "only if" states a necessary condition; it is read as the test, so meeting it (and (3a), (4)) answers yes.
- **F4** reg 4(1)(a) is "in the case of a notice of a claim in relation to an action against the nominal defendant", but
  its trigger names only an unidentified or uninsured vehicle. A claim against the nominal defendant in place of a failed
  insurer (s 118A) is taken under reg 4(1)(b): 6 months after the accident. The other reading leaves it with no time.
- **F5** s 124AC: damages "reduced by the amount so paid" -- not below nil.
- **F6** s 127B "has not attained the age of 16 years": the age on the day of the accident.
- **F7** s 133 "contracts in advance": made before the death or injury; a later agreement (a settlement) is outside s 133.
- **F8** Where several grounds of recovery hold, the widest is named: s 123 and s 124A(1) (all money paid) before
  s 124A(2) (just and reasonable); s 124A(3) (the road race organiser) only where no ground against the insured person is
  made out; for the uninsured driver, s 116(7) before s 116(7aa) before s 116(7b).
- **F9** s 124AB(1)(a)(ii): "received within 1 month following a first request": the day the insurer receives the money.
- **F10** s 127C(3) is applied only when the court has not found exceptional circumstances under s 127C(1)(a) (with
  them, party and party costs are open anyway).
- **F11** s 126: with the insurer's written consent, the step is allowed ("without the consent in writing" is the
  prohibition's own limit).

## What the Act turns out to say (findings)

1. **s 115 has no "on a road" limit; s 116(2) does.** A claim for an unidentified vehicle lies against the nominal
   defendant wherever the use of the vehicle occurred (subject to s 99(4) for conditionally registered machines); a claim
   for an uninsured vehicle lies only for its use "on a road". Asserted (an unidentified vehicle off a road answers the
   nominal defendant; an uninsured one answers no claim).
2. **A late notice of claim and "while the failure continues".** s 126A(6)(a) lets the insurer decline to deal with the
   claim "while the failure continues"; for a notice given late, the failure to give it in time can never end, so the
   text gives no point at which the insurer must deal with the claim. Reg 4(3) answers this only for court proceedings.
   The answer says "while the failure continues" and does not resolve it.
3. **Reg 4(3) overrides s 126A(6)(b) for any failure, once the (2)(c) and (d) material is given.** "Nothing in section
   126A ... affects the ability of a person to commence or continue proceedings once the person has provided the
   information and statements referred to in subsection (2)(c) and (d)". So a notice that was late, or not in the
   Minister's approved form (s 126A(2)(b)), does not stop proceedings once that material is provided. s 126A(7) authorises
   this. Asserted.
4. **s 116(7aa) and (7b) overlap for a s 43 Road Traffic Act offence.** (7b)(c) excludes only the (7)(c) conduct, so a
   driver found guilty under s 43 is within both (7aa) and (7b); (7d)(c) keeps the (7c) defence from them either way, so
   the overlap changes nothing in the result. The encoding names (7aa).
5. **s 127(2)(b) and (c) differ.** The time to tell the insurer of a consultation may be extended "as the insurer may
   allow"; the time to send a report may not be extended by the insurer, only where a longer period "may be reasonable".
   Both are one "extra days" input here; the `@desc` of each says which applies.
6. **Stale cross-references.** s 117 refers to "Part 3 of the Wrongs Act 1936" (now the Civil Liability Act 1936), and
   s 127A to the "Workers Rehabilitation and Compensation Act 1986" (replaced by the Return to Work Act 2014). Neither is
   relied on here; noted for the reader.
7. **s 99A(8)(a): the grace period and renewal.** The policy "falls due for renewal at the expiration of the former
   period" but "remains in force" for 30 more days; s 99A(10) ends the grace when a new policy comes into force. The
   vehicle is insured throughout, under one policy or the other; asserted for an accident before and after a renewal
   inside the grace.
8. **s 104(2) leaves road race cover to the policy terms.** The Act only says a policy "complies" though it does not
   extend to one participant injuring another. Whether the CTP Regulator's terms do extend to it is not in the deposited
   texts; the answer says so.
9. **s 124AB(4) rounds up; the Civil Liability Act rounds to the nearest.** The excess is "rounded up to the nearest
   multiple of $10"; asserted ($599.15 to $600).

## Before relying on it

- Check both texts against the current authorised versions on legislation.sa.gov.au (the Regulations deposit is as at
  1 November 2021; the Act as at 7 November 2024).
- An independent test pass, and a lawyer's review of forks F3, F4, F8 and findings 2 and 3.
- Encode the Civil Liability Act 1936 Part 8 limits and the Lifetime Support Scheme Act 2013 alongside, and bring in the
  CPI series so s 124AB needs no CPI input.
