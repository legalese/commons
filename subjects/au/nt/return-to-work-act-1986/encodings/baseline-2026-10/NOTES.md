# Return to Work Act 1986 (NT): baseline encoding for the injured worker and the employer

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18.
There is no REFUSE in it. A case the text does not answer returns an explicit `not covered` value, and tests assert it.
It was checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

It is written in layers:

- **`rtw-dates.l4`**: the calendar arithmetic (working days, months, ages), on the built-in date functions only, so that no module imports the slow daydate library.
- **`rtw-core.l4`**: the seat-neutral core, in the Act's own actors and terms ("the worker", "the employer", "the claimant"). Computations (normal weekly earnings, the weekly amount, the period, the lump sums, the deadlines) are functions. Where the text says "shall" or "must" or sets a period, there is a regulative rule (`DEONTIC`) with the worker and the employer as parties: 17 definitions, 15 rules and two consequences they share.
- **`rtw-seat.l4`**: the injured worker's seat (and the dependants' on a death). It asks 39 questions, each with `@export` and a `@desc` on every input, under `§§` headings. It builds the core's records from plain answers and restates no rule.
- **`rtw-seat-employer.l4`**: the employer's seat, 22 questions. Its names differ from the worker seat's, so a case file can import both.

No earlier encoding of this Act existed to keep. No requirement ledger covers the Northern Territory, so no ledger line is closed.

## Edition

- **Act:** Return to Work Act 1986 (NT), reprint **REPR050, as in force at 25 March 2024**, as deposited at `../../registers/source-bundle/Return-to-Work-Act-1986-NT-current-reprint-REPR050.txt` (converted from the register's Word reprint on 2026-10-19). This reprint is more than a year old: an amendment that commenced after 25 March 2024 is not in it. The register's history listing was not checked (no fetching in an encode step); check it before relying on a number.
- **Regulations:** Return to Work Regulations 1986, reprint **REPR050R2, as in force at 1 July 2024**, as deposited at `../../../return-to-work-regulations-1986/registers/source-bundle/Return-to-Work-Regulations-1986-NT-current-reprint-REPR050R2.txt`. They supply reg 3A (prescribed classes of worker), reg 4 (prescribed family members), regs 4A and 5 (the household and sports thresholds), reg 6 (the funeral benefit), reg 6AA (expert financial advice), reg 6A (declarations from abroad), reg 12 (who may issue a certificate, and how long it has effect), reg 13 (copies with a dispute statement) and reg 14 (the late-payment rate).

**Inputs, because the deposit does not hold them:**

- average weekly earnings (s 3(1): the Australian Statistician's NT full-time adult ordinary time earnings, last published before 1 January). The cases use an illustrative $2,000.
- the indexed normal weekly earnings (s 65(3)), because the s 65(3A) formula is missing (finding 1);
- the s 89 interest amount (finding 2), and the reg 14 rate, the Supreme Court judgment-debt rate;
- the future pension age (s 65(14), Social Security Act 1991 (Cth) s 23);
- the normal retiring age in the worker's industry;
- the number of weekday Territory public holidays in a working-day period;
- the value of a penalty unit: penalties are given in penalty units.

## Checks

| Module | Case file | Assertions | Traces |
|---|---|---|---|
| `rtw-dates.l4`, `rtw-core.l4` | `rtw-cases-core.l4` | 227 written, 227 satisfied | 17 |
| `rtw-seat.l4` | `rtw-cases-worker.l4` | 65 written, 65 satisfied | 0 |
| `rtw-seat-employer.l4` (with mirror cases against `rtw-seat.l4`) | `rtw-cases-employer.l4` | 58 written, 58 satisfied | 0 |

350 assertions in all, every one satisfied. `l4 run` on all seven files: 0 errors, 0 warnings (2026-10-24). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read.

The 17 `#TRACE`s each carry an `-- expect:` line: 15 breaches and two obligations still open (a deemed acceptance awaiting payment, and the permission to ask the Court to extend the mediation period). Each was read and matches its expectation. A breached trace satisfies neither `EQUALS FULFILLED` nor its negation, so breaches are checked this way.

Every expected value was written by hand from the deposited text, with the arithmetic in the comment above the assertion. The cases follow two illustrative people. Ana is a storeperson at a Darwin warehouse, injured on Monday 2 March 2026. Ben is a mechanic who dies of a work injury, leaving a dependent spouse and two children. The employer case file asks Ana's facts from her employer's side, and 28 **mirror cases** assert that the two seats give the same answer on the same facts.

The employer case file imports both seats and takes about two minutes to check with the stable `l4`.

## Seats

**1. The injured worker** (`rtw-seat.l4`), and on a death the worker's **dependants** and the person who pays for the funeral. They ask:

- "Am I a worker? Is my injury compensable?"
- "What will I be paid each week, and until when?"
- "What lump sum for my impairment, or for a death?"
- "What must my employer do, and by when, and what if it does not?"
- "When must I act?"

**2. The employer** (`rtw-seat-employer.l4`), read with its insurer. If the employer is uninsured, the Nominal Insurer takes its place for the claim decisions (s 85(10)). The text puts hard working-day deadlines on this party:

- forward the claim within 3 working days (s 84(1));
- decide within 10 working days (s 85(1));
- start weekly payments within 3 working days (s 85(2), (4)(b));
- or be taken to have accepted (s 87);
- pay each week within 7 days (s 88).

It also creates offences that only the employer can commit (ss 65C, 84(5), 85A, 86, 88). This is why the employer has a seat of its own here. Its questions are worded "Must I compensate this worker?", "By when must I decide this claim?", "Am I taken to have accepted this claim?", "Would dismissing this worker be an offence?", "What is the most I can be fined?".

No official has a seat. The Authority, the mediator, the Court and the registrar appear only as what they mean for the worker or the employer.

The 2026-10-18 defaults:

- **The Act alone, with the instrument that sets its numbers.** Followed: the Regulations set the household and sports thresholds, the funeral amount, the certificate period, the declarations from abroad and the late-payment rate, so they come in.
- **The actors the text names:** the worker, the claimant, the employer, its insurer, the Nominal Insurer; the Authority, the mediator and the Court only as above.
- **A judgment left to someone else is answered conditionally, as an input.** Examples:
  - "as soon as practicable" (s 80);
  - "reasonable cause" (ss 103D(5), 104(4), 182(2), (3));
  - whether employment "materially contributed" (s 58);
  - an "unreasonable" refusal of treatment (s 75B);
  - whether the s 60(2) presumption is rebutted;
  - "the employer is satisfied" of continued incapacity (s 65B(2)(b));
  - a Court order under s 65B(4);
  - where a worker "usually works" (s 53AA, as one fact per test).
- **The Act's own definitions are worked out from facts:**
  - worker (s 3B);
  - Territory worker (s 53AA);
  - normal weekly earnings (s 49A);
  - loss of earning capacity and total incapacity (s 65(2), (6));
  - prescribed child (ss 63(3), 65(13));
  - permanent impairment (s 70).

  Borrowed terms are asked as facts: PAYG employee, prescribed disease, serious misconduct, pension age.
- **One case:** one worker, one injury, one claim. On a death, one deceased worker and that worker's dependants.
- **The Act's own terms**, quoted in the comment above each rule.
- **Machinery out:** the Authority, the Council, inspectors, insurance and premiums, the Nominal Insurer's Fund.

**Departures:** the ship rule in s 53AA(2) and the s 4 deeming rules are taken as facts, not worked out.

## Scope

**In:**

- **Who is covered:**
  - s 3(1): the definitions of average weekly earnings and Territory worker;
  - s 3A: injury, with the management-action exclusion;
  - s 3B(1)-(6), (10), (11), (14), (15) and (17), with regs 3A, 4, 4A and 5;
  - s 4, as a fact, with s 4(2A) as a fact;
  - s 53(1), (2) and s 53AA(1), (3);
  - s 57, and s 58 as a fact;
  - s 60, with the 0.08 presumption.
- **Weekly payments:**
  - s 49A;
  - s 64;
  - s 65(1)-(3A) and (6)-(14): the 75% and 150% rule, the low-earner floor, prescribed children, relevant permanent impairment, pension and retiring ages;
  - s 65(1BA), (1D) and s 61A(2)(a): the 260 weeks and the end date;
  - s 65A (prison);
  - s 65B, with reg 6A (living abroad);
  - s 61B (notice of a statutory event).
- **Lump sums and death:**
  - s 70, s 71 and s 72(3), (5);
  - s 62, with regs 6 and 6AA;
  - s 63.
- **Overpayments:** s 74.
- **Claims, decisions and payment, as regulative rules and deadlines:**
  - s 80; s 82(1), (2), (6), with reg 12;
  - s 84(1), (3), (5);
  - s 85(1)-(4), (6)(c), (8)-(10), with reg 13;
  - s 85A; s 86; s 87; s 88;
  - s 89 (the weeks late only), with reg 14;
  - s 65C; s 75B, with s 69(1).
- **Disputes:** s 103D(1A), (4), (5); s 103J; s 104(3), (4); s 182.

**Out:**

- Parts 2-3 and 7: the Authority, the Council, inspectors, insurers, insurance, premiums, the Scheme Monitoring Committee, the Nominal Insurer and its Fund. Section 84(1)'s routing (insurer, Authority, Nominal Insurer) is in.
- s 50A firefighters and the prescribed-disease lists (Sch 2, regs 5AB, 5B, 5C), beyond the fact that the injury arose in the course of employment.
- Volunteers (s 3B(7)-(9), s 66, reg 8), labour hire (s 3B(16), ss 4A, 4B), community court orders, sailors (s 51).
- Other provisions:
  - s 52 (common-law actions); s 53A (bodily fluids); s 54 (other laws);
  - s 55 (disease and successive employers); s 56; s 61 (journey claims);
  - s 64(6) (retirement); s 65(4) (apprentices and juniors: inside the indexed-earnings input); s 68 (inside the earning-capacity input);
  - s 69, beyond its 14 days' notice and statement; s 72A; s 73 (medical and other costs, beyond the s 61A cut-off);
  - Division 4, except s 75B;
  - ss 78A-78B (settlements); ss 90-92;
  - the Court's procedure, apart from the time limits;
  - the transitional Parts.
- s 61A(2)(b)(ii) (finding 11).

## Regulative rules (in `rtw-core.l4`)

| Rule | Party | Clock starts | Consequence on failure |
|---|---|---|---|
| s 80(1) notice as soon as practicable | worker | the injury | no compensation, unless s 182(2) excuses it |
| s 82(2) remaining claim document within 28 days | worker | the first document | the claim is made only when the second arrives |
| ss 84(1), 85, 87: forward within 3 working days, and decide within 10; then pay within 3 on acceptance or deferral, and decide within the 56-day deferral | employer | receipt of the claim | s 84(3) lodging elsewhere; s 87 deemed acceptance, with weekly payments then owed |
| s 84(5) no refusing to receive a claim, no dismissal for claiming | employer | receipt of the claim | offence (85 / 25 penalty units) |
| s 85A(2) earnings information within 21 days | employer | the request | offence (85 / 17) |
| s 86 accept and pay at the new level, or reject with reasons, within 14 days | employer | the application | offence (25 / 8 or 3 months) |
| s 88(1) each weekly payment within 7 days after the week | employer | the end of the week | s 89 interest; offence (125 / 25) |
| s 61B notice of a statutory event before it occurs | employer | when the event is known | the change takes effect 14 days after notice |
| s 65C no dismissal of an incapacitated worker within 6 months | employer | the injury | offence (200); not for serious misconduct |
| s 75B reasonable treatment, training or assessment | worker | the requirement | deemed able to work; cut after s 69 notice |
| s 103D(1A) mediation within 90 days | worker | the s 85(8) or 69(1)(b) statement | only a Court extension remains (s 103D(4), (5)) |
| s 104(3) Court within 28 days | worker | the mediator's certificate | only the s 104(4) saving remains |
| s 72(3) reassessment within 28 days (a permission) | worker | notice of the assessment | none |
| s 71(4)(a), (b) pay the impairment compensation | employer | notice of the assessment or reassessment | s 72A certificate and Local Court judgment |

The clock counts calendar days. Working-day periods are given to a rule as the calendar days they span in that case. `rtw-dates.l4` works them out from dates for the seat questions.

A rule under `LEST` starts when the trace first notices that the deadline has passed. This is at the next event or `WAITUNTIL`, which can be a day after the deadline. The core cases allow for this in their arithmetic.

## What the Act turns out to say

1. **The s 65(3A) indexation formula did not survive conversion.** The deposited text reads "The formula for subsection (3)(a) is the following: where: N is amount of the normal weekly earnings of the worker immediately before the first compensation date; A is ...; C is ...". Only the "where" definitions remain. The deposit was not altered. The indexed normal weekly earnings are an input everywhere. N x A / C is encoded only as a flagged reading (`the indexed normal weekly earnings on the flagged reading N x A / C`), exported as "READING ONLY". Asserted ($1,500 x $2,100 / $2,000 = $1,575).
2. **The s 89(1) interest formula did not survive conversion either.** The text reads "an amount represented by the formula: A x the prescribed rate of interest x", followed by "where" definitions of A and of B. B is "the number of weeks (with a part of a week being counted as a whole week)" late, and no term that uses it survives. The deposit was not altered. The interest is an input. B is computed. Reg 14 sets the rate as the Supreme Court judgment-debt rate, which is not deposited. Asserted (B = 1 for 1 to 7 days late, 2 for 8 days).
3. **Section 65(1D) gives no period for some workers.** Take a worker whose normal retiring age is later than their future pension age, injured less than 2 years before pension age but 2 years or more before retiring age. Paragraphs (a) and (b) need an injury 2 years or more before pension age. (c)(i) and (ii) need one less than 2 years before retiring age, or after it. (c)(iii) and (iv) need retiring age not to be later. None applies. For example, born 1 July 1960, pension age 67, retiring age 70, injured 1 March 2026. The answer is `not covered`. Asserted.
4. **The figures hang on an undefined "annual equivalent".** Average weekly earnings are defined in s 3(1), not in s 49. Regs 4A, 5 and 6 take a percentage of "the annual equivalent of average weekly earnings", which nothing defines. It is read as 52 times the weekly figure:
   - funeral benefit cap (reg 6): 20%, or 10.4 x AWE, $20,800 on $2,000;
   - household worker threshold (reg 4A): 20%, also 10.4 x AWE;
   - sports contestant threshold (reg 5): 65%, or 33.8 x AWE.

   Of the regulations the brief names for s 3B, reg 3A prescribes classes of worker and reg 5 the 65%; the household 20% is reg 4A. Asserted.
5. **The lump sum jumps at 15% and at 85%, and the Table has holes.** 14% impairment gives 12% of 208 x AWE ($49,920), and 15% gives 15% ($62,400). 84% gives 84% ($349,440), and 85% gives the whole 208 x AWE ($416,000). The s 71(3) Table lists only whole percentages from 10% to 14%. An assessment of 14.5% has no row and answers `not covered`. Asserted.
6. **Drink- or drug-driving costs the weekly payments and the impairment lump sum, but not death benefits, medical costs or rehabilitation.** Section 60(3): "Nothing in this section affects an entitlement to compensation under Subdivision A or D of Division 3 or Division 4". Contribution is presumed at 0.08 unless the contrary is proved (s 60(2)). Section 60 reaches only a worker who was driving. Asserted. For the Motor Accidents (Compensation) Act encoding: its s 10A(a) excludes a motor accident injury that "is compensable under workers compensation legislation". A drink-driving worker whose injury is compensable here only for medical costs may get weekly benefits from neither scheme. That question belongs to the s 10A encoding.
7. **The low-earner floor pays up to 90% of the loss.** Where 75% of the loss falls below the s 65(12) amount, the worker gets the lesser of 90% of the loss and that amount (s 65(7), total incapacity). The s 65(12) amount is 50% of AWE, plus 12.5% for a dependent spouse and 6.25% for each prescribed child. For partial incapacity the s 65(8) test compares 75% of the indexed normal weekly earnings, not 75% of the loss. Where the floor applies, the worker gets the lesser of 90% of the loss and the (12) amount as a percentage of indexed earnings, applied to the loss (s 65(9)). Section 65(10) shuts the floor out entirely where the spouse earns 150% of AWE or more, at $3,000 but not at $2,999. Asserted ($1,080, $720, $964.29, $865.38, $900).
8. **Serious and wilful misconduct bars only an injury that heals.** Section 57(b) does not apply to "an injury resulting in his or her death or permanent or long-term incapacity". A deliberately self-inflicted injury is barred whatever its result (s 57(a)). For the Motor Accidents (Compensation) Act s 10A(b), `Would my injury be compensable but for s 57` answers whether one of these two bars is all that stands in the way. Asserted.
9. **Regulation 6A sets a minimum interval, not a maximum.** A worker abroad keeps weekly payments only by giving the employer "at intervals of not less than 3 months, a declaration". Read literally, this sets the shortest gap between declarations, not the longest. A worker could give one and then none for a year. The evident intent is "not more than 3 months". Whether the worker complies is a single input, and the `@desc` does not resolve the point.
10. **A second child adds nothing to the children's share of the death lump sum.** In the s 62(3) Table, one child with a spouse takes 10% of 364 x AWE. Two children with a spouse take 5% each, also 10% in all. The children's total rises only from the third child (15%) and reaches 25% at five, where it stays. With a spouse and six children each child gets 25% / 6. Asserted ($72,800 for one child; $36,400 each for two; $30,333.33 each for six).
11. **Section 61A(2)(b)(ii) counts from a point it does not fix.** For a worker under 15% whose payments end before 260 weeks because of retiring age or pension age, costs stay payable for "12 months after the end of the last of the relevant number of weeks". Section 61A(3) defines that number as 260 less the shorter period, but says nothing of where those weeks start. Not encoded. The 260-week case, s 61A(2)(a)(ii), is encoded: 12 months after the end of the 260th week. Asserted.
12. **Deemed acceptance sets no time for the payments it brings.** If the employer does not decide in time, it is "deemed to have accepted liability" for weekly payments and medical and other costs (s 87(1), (2)). Nothing says by when weekly payments must then start. The encoding reads in s 85(2)'s 3 working days. A dispute notified without the s 85(8) statement is not a notification at all (s 87(3)(b)), so it too leads to deemed acceptance. Section 87(1)(a) lets the deemed acceptance run until 14 days after a later notice. Section 87(4) makes the acceptance effective 10 working days after payments begin. Asserted (dates and traces).
13. **A medical certificate can lapse before the claim form is due.** Section 82(2) gives 28 days to give the second of the claim form and the medical certificate of capacity. Regulation 12(2) gives a certificate effect for only 14 days. A certificate from a nurse or Aboriginal and Torres Strait Islander health practitioner in an isolated place who did not consult a doctor has effect for 3 days. The brief's "reg 12 period" for the second document is the 28 days in s 82(2) itself. Regulation 12 sets how long a certificate lasts. Asserted.
14. **The 28 days to go to the Court are in s 104(3).** Section 85(8)(d) (and s 69(1)(b)(iv)) only require the employer's statement to tell the claimant about them. Both clocks have savings:
    - the 28 days for the Court: s 104(4), for "mistake, ignorance of a disease, absence from the Territory or other reasonable cause";
    - the 90 days for mediation: the Court may extend them (s 103D(4), (5)).

    In the rules, missing either deadline leaves only that saving, not a breach. Asserted (traces).
15. **"Working day" is not defined in the Act.** The Interpretation Act 1978 (NT), which may define it, is not deposited. It is read as a Monday to Friday that is not a public holiday. The Territory's public holidays are not deposited either, so the number of weekday public holidays in the period is an input. Asserted (claim received Monday 26 October 2026: forward by Thursday 29 October, decide by Monday 9 November).
16. **An overpayment often cannot be recovered.** Unless the Court orders otherwise, it cannot be recovered in two cases (s 74(2)):
    - the employer or insurer "incorrectly calculated" the benefit;
    - the payment was for a period more than 6 months before recovery was sought.

    The encoding reads the second as a period that ended more than 6 months before; exactly 6 months is not "more than". Asserted.
17. **There are two dismissal offences, not one.** Section 84(5)(b) punishes dismissal "for the reason only that the worker has given or attempted to give ... a claim", with no time limit (85 penalty units for a body corporate, 25 for an individual). Section 65C punishes dismissing a worker incapacitated by the injury within 6 months of it, for any reason except serious misconduct (200 penalty units). An unreasonable condition designed to make the worker leave counts as dismissal. Asserted (rules, dates and penalties).

## Read with

The stable `l4` cannot IMPORT across encoding folders, so these links are recorded here and not in code.

- **Social Security Act 1991 (Cth)**, `subjects/au/social-security-act-1991/encodings/baseline-2026-10/`:
  - **Pension age** (s 23(5A)-(5D)): `What is my pension age in months` in `ssa-claims.l4` answers this encoding's `my pension age in months` input (s 65(14) "future pension age").
  - **Compensation recovery** (Part 3.14, s 17), in the same encoding: `Is my payment compensation affected`, `Is what I received compensation`, `What is the compensation part of my lump sum`, `How many weeks is my lump sum preclusion period`, `By how much is my daily rate reduced for periodic compensation`.
  - Weekly payments under ss 64 and 65 are periodic compensation for lost earnings. Whether the s 71 permanent impairment lump sum is "compensation" depends on whether it is "in respect of lost earnings or lost capacity to earn" (s 17(2)). That encoding answers it.
- **Motor Accidents (Compensation) Act 1979 (NT)**, `subjects/au/nt/motor-accidents-compensation-act-1979/`:
  - Section 10A excludes benefits for an injury that "(a) is compensable under workers compensation legislation; or (b) would have been so compensable but for" self-infliction or serious and wilful misconduct. That encoding takes `Is my injury compensable under the Return to Work Act` and `Would my injury be compensable but for s 57` as inputs.
  - From this side, s 4(2A) sends most journey and recess motor accidents to that Act (asserted), and s 61 (not encoded) has that scheme pay while the question is disputed. See also finding 6.
- **Victims of Crime Assistance Act 2006 (NT)**, `subjects/au/nt/victims-of-crime-assistance-act-2006/`:
  - Under s 18(1), a worker injured by a violent act "is being paid, or has been paid, compensation under the Return to Work Act 1986 for the injury", or "is entitled to compensation" here even without a claim. That worker cannot get an interim payment or award for it.
  - Secondary and family victims are excluded too (s 18(3)), but counselling stays open (s 18(4)).
  - That encoding takes `Is my injury compensable under the Return to Work Act` as an input.
- **Income tax:** the tax treatment of weekly payments and lump sums is a question for `subjects/au/income-tax-assessment-act-1997/`, and was not checked here.

## Before relying on it

- Check REPR050 and REPR050R2 against the register's history for amendments after 25 March 2024 and 1 July 2024.
- Transcribe the s 65(3A) and s 89(1) formulas from the authorised PDF reprint into a `.formulas.md` sidecar beside the deposit. Then replace the indexed-earnings and interest inputs (findings 1 and 2).
- Fill these inputs from their published sources:
  - the published average weekly earnings figure for each year;
  - the Supreme Court judgment-debt rate;
  - the value of a penalty unit (Penalty Units Act 2009 (NT));
  - the Territory's public holidays;
  - the Interpretation Act's "working day".
- Resolve s 61A(2)(b)(ii) and the s 65(1D) gap (findings 3 and 11). Both may need the case law, which was not searched.
- Encode the rest of Part 5:
  - s 73 medical and other costs, and s 75A return to work plans;
  - ss 76-78 rehabilitation;
  - the rest of s 69;
  - s 65(4) apprentices and juniors;
  - volunteers;
  - firefighters' presumptions (s 50A, reg 5B);
  - the Sch 2 prescribed diseases;
  - ss 78A-78B settlements.
- An independent test pass, and a human gate. Deployment names within 36 characters, if deployed: `au-nt-return-to-work-act-worker` and `au-nt-return-to-work-act-employer`.
