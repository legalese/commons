# Victims of Crime Act 2001 (SA), with the CTP claim: baseline encoding for the injured person and the CTP insurer

> **The texts are not official and may be out of date.** Every text this encoding is written from is the **Open Australian Legal Corpus** text (South Australian legislation last collected 2025-03-10), not the official text on legislation.sa.gov.au, which refused this repository's fetcher. Each is as at the corpus scrape:
>
> - **Victims of Crime Act 2001**: as at **2021-01-01**. The Current Titles list of 22 September 2026 lists it at **1.4.2025**, so at least one later version exists and is not reflected here.
> - **Victims of Crime (Statutory Compensation) Regulations 2019**: as at **2023-05-11**.
> - **Motor Vehicles Act 1959**: as at **2024-11-07**.
> - **Motor Vehicles (Third Party Insurance) Regulations 2013**: as at **2021-11-01**.
> - **Civil Liability Act 1936**: as at **2023-06-22**.
> - **Civil Liability Regulations 2013**: as at **2015-10-02**.
>
> Check legislation.sa.gov.au before relying on any answer. Based on content from the South Australian Legislation website (CC BY 4.0); see `SOURCE-LICENSE.md`.

## Method

**Baseline.** Written straight from the deposited texts with the `writing-l4-rules` skill, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18.
There is no REFUSE in it. A case outside the encoding answers an explicit `not covered` value, and tests assert it: an offence before 1 July 2015, an accident before 1 July 2013, a scale value or injury scale value that is not a whole number in range, a limited claim's legal costs that Schedule 2 does not prescribe, another State's CTP scheme.
It was checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

One encoding covers two schemes, because the same injured person asks both sets of questions and one provision decides between them. Victims of Crime Act s 17(5)(c) says a person is not entitled to statutory compensation if the injury "falls within the ambit of a compulsory third-party insurance scheme covering the motor vehicle (whether the vehicle is in fact insured under the scheme or an action for damages lies against a nominal defendant)". So a person hit by a dangerous driver, though the victim of an offence, claims under the CTP part. Section 17(5)(b) likewise sends a harm covered by a Return to Work payment for death or non-economic loss to that Act (the Return to Work encoding). The home is the Victims of Crime Act, because its s 17(5) decides the route. Each regulation is grouped with the Act whose numbers it sets: the Victims of Crime Regulations with s 18 and s 25, the Third Party Insurance Regulations with Motor Vehicles Act s 126A, Civil Liability Regulations regs 18-19 with Civil Liability Act s 58.

It is written in layers:

- **`voc-common.l4`**: calendar and rounding arithmetic shared by both cores (built-in date functions only; no daydate library).
- **`voc-core.l4`**: the Victims of Crime Act core, in the Act's own actors and terms ("a person", "an immediate victim", "the claimant", "the offender", "the Crown Solicitor", "the Crown", "the court"). Computations are functions: who is an immediate victim, the four eligibilities and the s 17(5) exclusions, the application periods, the period for negotiation and the court's last day, what an application must contain, the s 20 amounts with s 4(2) indexation, the aggregate limit, the legal costs. Where the text states a duty, there is a regulative rule (`DEONTIC`): four in all (s 18(1)-(4); s 18(5)-(6) with s 19(2); s 19(2)-(3); s 21(1)).
- **`ctp-core.l4`**: the CTP core: Motor Vehicles Act s 99(3), (3a), ss 115, 116 and 126A with the Third Party Insurance Regulations regs 4-6, and Civil Liability Act Part 8 for an MVA motor accident with Civil Liability Regulations reg 7 and regs 18-19. Three regulative rules: the claimant's notice (s 126A(1)-(2), reg 4), and the insurer's and nominal defendant's duties (s 126A(4), (5)).
- **`voc-seat.l4`**: the injured person's seat, 29 questions.
- **`voc-seat-insurer.l4`**: the CTP insurer's seat (which also answers for the nominal defendant), 9 questions.

Each question has `@export` and a `@desc` on every input, grouped under `§§` headings in the texts' order. Where a group arises only in a situation the person may not be in, the heading's comment says so ("situation: you were hurt by a crime ...", "situation: you were injured in a motor accident", "situation: your CTP claim is being assessed"). The seats build the cores' records from plain answers and restate no rule. Where one answer depends on another question (whether the injury falls within the CTP scheme), the `@desc` names that question.

No earlier encoding of any of these six texts existed. South Australia has no requirement ledger, so no ledger line is closed, and no scenario life covers South Australia, so every case is hypothetical.

## Edition

| Text | As at (corpus) | Deposit |
|---|---|---|
| Victims of Crime Act 2001 | 2021-01-01 (listed at 1.4.2025: a later version exists) | `../../registers/source-bundle/victims-of-crime-act-2001.txt` |
| Victims of Crime (Statutory Compensation) Regulations 2019 | 2023-05-11 | `subjects/au/sa/victims-of-crime-statutory-compensation-regulations-2019/registers/source-bundle/` |
| Motor Vehicles Act 1959 | 2024-11-07 | `subjects/au/sa/motor-vehicles-act-1959/registers/source-bundle/` |
| Motor Vehicles (Third Party Insurance) Regulations 2013 | 2021-11-01 | `subjects/au/sa/motor-vehicles-third-party-insurance-regulations-2013/registers/source-bundle/` |
| Civil Liability Act 1936 | 2023-06-22 | `subjects/au/sa/civil-liability-act-1936/registers/source-bundle/` |
| Civil Liability Regulations 2013 | 2015-10-02 | `subjects/au/sa/civil-liability-regulations-2013/registers/source-bundle/` |

No formula was found missing in any of the six deposits.

**Coverage dates.** Victims of Crime Act ss 17, 20 and Schedule a1 took their present form from 1 July 2015 (the Victims of Crime (Compensation) Amendment Act 2016, in operation from 1.7.2015), and s 34 assesses compensation under the Act "as in force at the time of the commission of the offence"; an offence before 1 July 2015 answers `not covered`. Motor Vehicles Act s 126A and Civil Liability Act s 52(3)-(8), 56A and 58B came in on 1 July 2013 (Motor Vehicle Accidents (Lifetime Support Scheme) Act 2013), not affecting earlier causes of action; an accident before 1 July 2013 answers `not covered`. Later offences and accidents are answered under the deposited texts, which may since have been amended.

**Figures that are inputs.** The texts fix their stated amounts, which are constants here: the $2 000 threshold and three-quarters (s 20(3)(a)(i)), Schedule a1, $100 000, $20 000 and $14 000 (s 20), the Schedule 2 legal costs, 3 years, 12 months, 3 months and 6 months (s 18), 6 months and 21 days (reg 4, s 126A(4)), $2 750 and $2.2 million (CLA s 3), 7 days (s 52(1)), the s 52(3) bands, 7 and 10 (ss 56A, 52, 58), 20% (ss 56A(5), 58B(3)), 4 weeks, 6 hours and 6 months (s 58), $25 an hour (reg 19). What no deposit holds is an **input**:

- the CPI (All groups, Adelaide) figures that index every "(indexed)" amount: the September quarters for Victims of Crime Act s 4(2) (base September 2014) and for the CLA prescribed minimum and maximum (base September 2001), and the March quarters for CLA s 52(7) and reg 19(2) (base March 2013);
- State average weekly earnings (reg 18: an ABS figure);
- the minimum superannuation guarantee percentage (Commonwealth law, not deposited);
- every amount and value the court assesses before the texts' limits apply: the financial loss, the s 20(3)(a)(ii) scale value, the grief amount the court thinks fit, the injury scale value (assessed under the Civil Liability Regulations' Part 2 and Schedule 1, not encoded), the losses of earning capacity and financial support;
- the court's and others' judgments: the s 17(3)(c) suitability, the s 18(7) extension, the s 19(3)(b) exemption, the s 20(5), (5a) and (7) findings, the reg 4(2) prejudice, the s 52(5), s 56A(3) and s 58(3) satisfactions, the ss 115(4), 116(5) prejudice and justice, and whether a mental harm is a recognised psychiatric illness.

The case files use **HYPOTHETICAL** CPI figures and earnings, chosen to test the arithmetic. They are not the ABS's published figures.

## Checks

| Modules | Case file | Assertions |
|---|---|---|
| `voc-common.l4`, `voc-core.l4`, `ctp-core.l4`, `voc-seat.l4` | `voc-cases-injured.l4` | 196 written, 196 satisfied |
| `voc-common.l4`, `ctp-core.l4`, `voc-seat-insurer.l4`, `voc-seat.l4` (mirror cases) | `voc-cases-insurer.l4` | 42 written, 42 satisfied |

That is 238 assertions, all satisfied, including 14 mirror assertions (the same facts asked from both seats, with answers that must agree) and 3 more that check the agreed answer by hand. In addition, 8 `#TRACE`s carry an `-- expect:` line, and each was read and matches its expectation:

- 6 breaches: by the claimant under s 18(1)-(4) twice (an unverified application; one on day 1 097), s 18(6) (a court application a day late) and s 126A(1)-(2) twice (notice to the wrong respondent; no notice and no excuse), and by the insurer under s 126A(4) (a copy on day 22);
- 2 obligations still pending: the claimant's s 19(2) service (no time is stated), and the nominal defendant's s 126A(5) standing duty. The stable `l4` prints the latter's breach clause as `BREACH BY` `the respondent` (the rule's parameter name) rather than its value.

`l4 run` on all seven files: 0 errors, 0 warnings (2026-10-24). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. Every expected value was written by hand from the texts, with the arithmetic in the comment above the assertion; the count (60) and total ($2 413 667) of Schedule a1 were taken from the deposit's table, not from the encoding.

A negative control was run on copies outside the repository: Schedule a1 row 14 raised by $1 was caught (the Schedule a1 total). The s 52(3)(c)(ii) $3 000 raised by $1 was not caught, because s 52(7) rounds every amount to the nearest $10 and $3 001 rounds back to $3 000 at the proportions tested: the rounding the text requires absorbs it.

The case files take about a minute each to run (they import both seats or both cores).

## Seats

**1. The injured person** (`voc-seat.l4`): the victim of an offence; a family member claiming for grief, the dependants' financial loss or funeral expenses; or a person injured in a motor accident. They ask:

- "Which scheme covers me: victims of crime compensation, a CTP claim, or neither?"
- "Am I eligible, and for what?"
- "By when must I apply to the Crown Solicitor, and then to the court? Must I serve the offender? What must my application contain?"
- "How much can I get, what are the limits, and what may my lawyer charge?"
- "Whom must I give my CTP notice of claim to, by when, and with what? What happens if I am late or something is missing?"
- "What damages can I get after a motor accident, and what limits apply?"

**2. The CTP insurer** (`voc-seat-insurer.l4`). Motor Vehicles Act s 126A(4)-(5) put real duties on "an insurer or the nominal defendant": to send the claimant a copy of every record obtained under the access authority within 21 days, and to keep practices and procedures to help claimants comply. In South Australia the CTP insurers are licensed private insurers (approved insurers, s 101); the nominal defendant is appointed by the Minister (s 116A) and its liabilities are met by the insurers (ss 115(2), 116(6)), and the same questions answer for it. The insurer asks: "Is this claim mine or the nominal defendant's? By when should the claimant have notified me? May I decline to deal with it? Can the claimant sue? What must I do, and by when? What can be awarded against my insured?"

**No seat** for the Crown Solicitor, the Attorney-General, the Crown, the court or the CTP Regulator, which are officials, and none for the offender. Their powers appear only as what they mean for the person: the court's judgments are inputs; the Crown's right to require a medical examination is the claimant's s 21(1) duty.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers or dates.** Departed from in one way, by the plan: two Acts with their instruments in one encoding, because s 17(5)(c) joins them (above). Each instrument is used only for the numbers its Act needs.
- **The actors the texts name**: the claimant, the victim, the offender, the Crown Solicitor, the Crown, the court; the claimant, the insurer, the nominal defendant, the injured person.
- **Judgments left to others are answered conditionally, as inputs** (listed under Edition).
- **The Acts' own definitions are worked out from facts**: immediate family, victim, immediate victim (s 4(1)); "caused by or arising out of the use of a motor vehicle" (s 99(3), (3a)); uninsured motor vehicle (s 116(1)); the prescribed minimum and maximum (CLA s 3). Borrowed terms are asked as facts: spouse and domestic partner (Family Relationships Act 1975), homicide, sexual offence, motor vehicle (MV Act s 5), recognised psychiatric illness, the ISV.
- **One case**: one offence and one claimant; one motor accident and one claim.
- **The texts' own terms**, quoted in the comment above each rule.
- **Machinery out**: the Commissioner for Victims' Rights and the advisory committee, the Victims of Crime Fund and levy, approved insurers and premiums, the CTP Regulator, the Lifetime Support Scheme.

## Scope

**In:**

- Victims of Crime Act: s 4(1) (child, dependants, harm, homicide, immediate family, immediate victim, injury, victim), s 4(2); s 17(1)-(5) (s 17(5)(d) by leaving recoverable expenses out of the financial loss; s 17(6) as a note); s 18 (s 18(4a) out); s 19(2), (3); s 20(1), (3), (5), (5a), (7), (9) (with (4) and (8) inside the court's assessment); s 21(1), (2); s 25(1); s 34; Schedule a1.
- Victims of Crime (Statutory Compensation) Regulations 2019: reg 4 and Schedule 1 (the application's contents); reg 5 and Schedule 2 clauses 2, 3 and 3A (legal costs).
- Motor Vehicles Act 1959, Part 4: s 99(3), (3a); s 104(1)(a); s 115(1), (3), (4); s 116(1), (2), (4), (5); s 126A(1)-(7).
- Motor Vehicles (Third Party Insurance) Regulations 2013: regs 4, 5, 6.
- Civil Liability Act 1936, Part 8 for an MVA motor accident: s 3(1) (MVA motor accident, prescribed minimum and maximum, State average weekly earnings, mental harm terms); s 51; s 52(1), (3)-(8); s 53; s 54; s 56; s 56A(2), (3), (5)-(9); s 58(1)(a), (2)-(4); s 58B(3).
- Civil Liability Regulations 2013: reg 7, regs 18 and 19.

**Out:**

- Victims of Crime Act Parts 2, 3, 5 (payment by the Attorney-General, recovery), 6 (the Fund and levy) and 7 other than s 34; ss 18(4a), 19(1), 20(2), (6), (10), (11), 21(3)-(5), 22 (proof and corroboration), 23 (joint offences), 24 (appeals), 25(2), 26; Schedule 1; Schedule 2 clause 4 of the Regulations (disbursements); the Regulations' reg 6.
- Motor Vehicles Act Part 4 apart from the sections above (premiums, approved insurers, the insurer's rights of recovery, s 127 medical examinations, ss 127A-127C, 128); s 99(4) (conditionally registered machines); another State's or Territory's CTP law.
- Civil Liability Act Parts 1-7 and 9 (liability, contributory negligence, Part 5 death claims beyond s 54(3) and s 58B), s 52(2) (the 0-60 scale for non-motor negligence), s 55 (the discount rate), s 56A(4) and s 58B(2) (how the court weighs chances), s 57, s 58(1)(b), s 58(5), (6) and s 58A (the Lifetime Support Scheme), s 76.
- Civil Liability Regulations Part 2 (beyond reg 7) and Schedule 1 (the ISV is the court's), Parts 4 and 5 (including the insurer's reg 20(4) and reg 23(3) duties to send reports within 21 days, which would be the next addition to the insurer's seat).

## Commonwealth links

Cross-folder IMPORT is not possible, so these are recorded here, not in code.

- **Social Security Act 1991, Part 3.14** (`subjects/au/social-security-act-1991/`): whether CTP damages under the Civil Liability Act and victims of crime statutory compensation count as "compensation" that can reduce or preclude a Centrelink payment is **unverified (general knowledge, not from the texts)**, as the jurisdiction README says. This encoding answers what the state law gives; the Commonwealth effect is not encoded.
- **Superannuation guarantee** (Commonwealth law, not deposited): the minimum percentage in CLA s 56A(7), (9) is an input.
- **GST** (A New Tax System (Goods and Services Tax) Act 1999, named in s 25(3)): the Schedule 2 amounts are "plus GST"; this encoding gives them before GST.
- **Return to Work Act 2014 (SA)** (`subjects/au/sa/return-to-work-act-2014/`): s 17(5)(b) and (6) are the join; whether a payment "in respect of death or non-economic loss" is due under that Act is an input here.

## What the texts turn out to say

1. **The switch is s 17(5)(c), and it follows the CTP scheme wherever it reaches.** A victim of an offence whose injury falls within the CTP scheme gets no statutory compensation "whether the vehicle is in fact insured under the scheme or an action for damages lies against a nominal defendant". A person hit by a dangerous driver, by a hit-and-run driver (s 115) or by an uninsured car on a road (s 116) claims under the CTP part, not as a victim of crime; so does the widow of a man killed by a driver convicted of manslaughter, for grief. Asserted.
2. **Where the CTP scheme does not reach, statutory compensation does.** "Use of a motor vehicle" means only a direct consequence of driving, running out of control, or a collision on a road with a stationary vehicle (s 99(3)), never a terrorist act (s 99(3a)), and an uninsured vehicle is covered only "on a road" (s 116(2)). An assault inside a parked car, a vehicle used in a terrorist act, or an uninsured car driven at someone on private land falls outside CTP, and the victim of crime scheme applies. Asserted.
3. **s 17(5)(b) is narrower than "a workers compensation payment".** It bars statutory compensation only where the person has received or is entitled to "a payment or damages in respect of death or non-economic loss for the same harm" under the Return to Work Act. Weekly payments alone do not bar it, and s 17(6) then says statutory compensation for the same harm gives no right of recovery under that Act. The encoding asks the narrower fact.
4. **Schedule a1 lists amounts for scale values 1 and 2 ($1 000 and $2 000, indexed), but s 20(3)(a)(ii) says that at 2 or less "no award will be made".** Those two rows can never apply. Asserted.
5. **The $2 000 financial-loss threshold is not indexed.** The $100 000 limit, the $20 000 grief limit, the $14 000 funeral limit and every Schedule a1 amount are "(indexed)"; the $2 000 in s 20(3)(a)(i) is not, so a larger share of every financial loss is cut by a quarter each year. Asserted.
6. **The amounts are frozen at the offence (s 34), and indexed by a two-decimal quotient.** The amount in force is the one adjusted on the last 1 January on or before the offence, by the September quarter CPI of the year before over September 2014 (s 4(2)). The quotient "will be calculated to 2 decimal places": the text does not say whether that rounds or truncates; read as rounding, a half up (1.11568 gives 1.12). An offence in 2015 takes the stated amounts. Asserted.
7. **s 18(2) does not say which period applies to a family member's own injury after a homicide.** Such an application is both "an application by a victim" (3 years after the offence) and "an application arising from the death of a victim" (12 months after the death). The encoding treats an application for the claimant's own injury as one by a victim, and grief, dependants' and funeral claims as arising from the death. A reading.
8. **The Regulations' "(indexed)" legal costs have no indexation rule of their own.** Regulation 3 does not define it, and s 4(2) speaks of amounts "in this Act". The encoding applies s 4(2) (the Acts Interpretation Act 1915, which may say so, is not deposited), at "the time of commencement of the proceedings" (s 25(1)). So the costs limit is indexed to a different date from the compensation (the offence, s 34). A reading.
9. **Schedule 2 clause 2(1) prescribes nothing for some limited claims.** Paragraph (a) covers a limited claim (grief or funeral expenses only) only "where the identity of the offender is known and compensation is agreed"; paragraph (b) covers only claims that are "not a limited claim or a related claim". A limited claim against an unknown offender, or one that goes to court, has no prescribed solicitor's amount. Asserted (`not covered`).
10. **Applying early costs nothing.** The last day to apply to the court is "the later of" the end of the initial application period and 6 months after the period for negotiation (s 18(6)), so a victim who applies to the Crown Solicitor in the first year keeps the full 3 years for the court. A "longer period" for negotiation can only lengthen it: an agreed shorter period leaves the 3 months. Asserted.
11. **A late CTP notice lets the insurer decline to deal with the claim, but not stop the claimant suing.** Regulation 4(2) excuses lateness only if it was caused by one of the listed reasons and "the proper assessment of the claim has not been substantially prejudiced"; otherwise s 126A(6)(a) lets the insurer "decline to consider or deal with the claim while the failure continues", and a lateness cannot be cured, so the encoding reads that as lasting. But reg 4(3) says nothing in s 126A affects the claimant's ability to commence or continue proceedings once the s 126A(2)(c) and (d) material is provided, "including after the period ... has expired". A notice not in the approved form likewise lets the insurer decline but does not bar proceedings. Asserted.
12. **A victim of a road crime with a minor injury may get nothing for pain and suffering from either scheme.** Section 17(5)(c) takes the injury out of the victim of crime scheme, which would pay for a scale value of 3 or more (Schedule a1), and Civil Liability Act s 52(4) pays non-economic loss for an MVA motor accident only if the injury scale value "exceeds 10". Dana (hypothetical), hit by a dangerous driver with an ISV of 10, gets no non-economic loss damages, though the same injury from an assault would. Asserted in its two parts.
13. **The s 52(5) exception can still give nothing.** For an ISV of 10 or less the court may award damages if the case is exceptional and the threshold harsh and unjust, on an ISV that "should rarely be more than 25% higher" (s 52(6)). But the s 52(3)(c) bands start above 10, so an ISV of 8 or less, raised by 25%, still has no amount. Asserted (an ISV of 9 assessed at 10 gives nothing; at 11, $3 900 at the hypothetical CPI).
14. **The 20% discounts come after the caps.** Damages for loss of earning capacity (s 56A(5)) and for loss of financial support after a death (s 58B(3)) are discounted by a further 20% "after applying ... any other principle arising under this Act". The encoding reads the s 54(2) and (3) caps as such principles, so the award is at most 80% of the prescribed maximum. A reading, asserted ($3 308 800 on a $4 136 000 maximum).
15. **The indexed $25 hourly rate for family care has no rounding rule.** Regulation 19(2) adjusts it each 1 July by the March quarter CPI but, unlike s 52(7) (to the nearest $10), says nothing about rounding; none is applied. Asserted ($32.50 at 1.30).
16. **s 126A(6) sanctions only the claimant.** The insurer's and nominal defendant's duties in s 126A(4) and (5) carry no stated consequence. The encoding records a failure as a breach by the respondent, but nothing in the texts says what follows.
17. **The nominal defendant's notice is required three times, with different sanctions.** Sections 115(3) and 116(4) and reg 4(1)(a) all require notice "as soon as reasonably practicable after it becomes apparent" that the vehicle cannot be identified or was uninsured. A breach of reg 4(1) engages s 126A(6). A breach of ss 115(3) or 116(4) lets the court dismiss the action, if the defence was prejudiced and justice requires it (ss 115(4), 116(5)). No number of days is fixed; the encoding names the day the time runs from. Asserted.
18. **Interest is barred differently.** No interest may be awarded on any statutory compensation (s 20(9)); under the Civil Liability Act only damages for non-economic or future loss carry none (s 56). Asserted.
19. **Every figure that moves is an input, and the texts are old.** No deposit holds a CPI figure, so every indexed amount here depends on figures the person supplies. The Victims of Crime Act text is the version of 1 January 2021, and a later version (1.4.2025) is listed; the Civil Liability Regulations are as at 2015.

## Before relying on it

- Replace all six texts with the current official ones from legislation.sa.gov.au, and re-check s 17, s 18, s 20 and Schedule a1 against the version listed at 1.4.2025 (and any later), and s 126A, reg 4, s 52 and s 58 against theirs.
- Deposit the CPI (All groups, Adelaide) series, or the gazetted or published indexed amounts, so the amounts need not be inputs; settle the rounding readings (findings 6, 15) and the Regulations' indexation (finding 8) against them.
- Settle the readings in findings 3, 7, 11 and 14, and whether an interstate vehicle's injury is within "a compulsory third-party insurance scheme" for s 17(5)(c) on that scheme's own test.
- Add the Civil Liability Regulations' reg 20(4) and reg 23(3) duties to the insurer's seat, and Part 2 of those Regulations if an ISV is ever to be estimated rather than asked.
- Verify the Commonwealth links (Social Security Act Part 3.14) from the Commonwealth texts.
- An independent test pass and the human gates.
