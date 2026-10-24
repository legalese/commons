# Cost of Living Concessions Act 1986 (SA), with the emergency services levy and the car: baseline encoding for the concession holder

## Method

**Baseline.** Written straight from the deposited texts with the `writing-l4-rules` skill, from the seat of the individual to whom the law is applied. It follows the design defaults ruled on 2026-10-18 and the brief for the tax-and-benefits encodings of 24 October 2026. It uses no REFUSE. A year or a kind of land outside the deposited texts answers `not covered`, and tests assert it. It was checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.

There was no pipeline, no coverage table, no independent test pass and no human gate. **Not for public use as advice.** There was no earlier encoding of any of the six instruments to keep.

It brings six South Australian instruments into one encoding, because they are switched on by the same Commonwealth cards and payments (see "Why these six together" below). It is written in two layers:

- **A seat-neutral core**, in the texts' own actors and terms: a person, an eligible person, a ratepayer and the Minister (Cost of Living Concessions Act); the owner of land, co-owners, a married couple or domestic partnership, the Commissioner and the Minister (Emergency Services Funding Act); the owner, the registered owner or operator, the parent or legal guardian, the licence holder, a person who drives, and the Registrar (Motor Vehicles Act). Computations (the concession, the indexed amounts, the water rates remission, the levy remissions, the registration and licence fees) are functions. Where a text says "must" or sets a time, the rule is regulative (`DEONTIC`): eight rules in all.
- **A seat layer**, `colc-seat.l4`: 26 exported questions, each with `@export` and a `@desc` on every input, grouped under `§§` headings. It builds the core's records from plain answers and restates no rule. Where a field of a record is not read by the rule asked, it gets a fixed placeholder, with a comment saying so.

| File | What it holds |
|---|---|
| `colc-common.l4` | Arithmetic, the 10-cent rounding, date helpers (a `YMD` shim, day counts, "one month after", complete months), the financial year, and the list of Commonwealth cards and payments shared by all three cores |
| `colc-concessions.l4` | Core: Cost of Living Concessions Act ss 2(2)-(3), 3, 4(3), 7, 8(2)-(4); Regulations regs 3-8. Four regulative rules |
| `colc-levy.l4` | Core: Emergency Services Funding Act s 3(1), s 15(1)-(2), s 16; Remissions--Land Regulations regs 3, 5A, 6, 7, 8. One regulative rule |
| `colc-vehicles.l4` | Core: Motor Vehicles Act ss 37A, 38, 38A, 38AB, 38B, 40, 40A; Regulations regs 76(4)-(5), 77(3)-(4), Schedule 1 clauses 1 and 22. Three regulative rules |
| `colc-seat.l4` | The concession holder's 26 questions |
| `colc-cases-concessions.l4`, `colc-cases-levy.l4`, `colc-cases-vehicles.l4` | Cases for the three cores |
| `colc-cases-seat.l4` | Cases for the seat layer, asked with plain answers |

Conventions: a financial year is named by the calendar year in which it **begins** (2024 is 2024/25). Money is in Australian dollars. A share of land is a fraction from 0 to 1. Dates are `DATE` values compared through `DATE_SERIAL`, because the stable `l4` has no date comparison without the `daydate` library.

## Edition

**Every text here is the Open Australian Legal Corpus text (version 7.1.0, CC BY 4.0), which the corpus extracted from the register's unauthorised RTF. Each is as at the corpus scrape and may be out of date. Check legislation.sa.gov.au before relying on anything here.** The official register refused this repository's fetcher on 2026-10-19 and 2026-10-24 (see `SOURCE-LICENSE.md` and the jurisdiction README).

| Instrument | Text as at (scraped) | Deposited at |
|---|---|---|
| Cost of Living Concessions Act 1986 | **2015-07-01** (2024-09-13) | `../../registers/source-bundle/cost-of-living-concessions-act-1986.txt` |
| Cost of Living Concessions Regulations 2020 | **2025-01-01** (2025-03-10) | `../../../cost-of-living-concessions-regulations-2020/registers/source-bundle/cost-of-living-concessions-regulations-2020.txt` |
| Emergency Services Funding Act 1998 | **2023-11-25** (2024-09-13). The Current Titles list of 22 September 2026 listed a **later version (4.12.2025)**, so at least one amendment is missing here. | `../../../emergency-services-funding-act-1998/registers/source-bundle/emergency-services-funding-act-1998.txt` |
| Emergency Services Funding (Remissions--Land) Regulations 2014 | **2024-07-01** (2024-09-13) | `../../../emergency-services-funding-remissions-land-regulations-2014/registers/source-bundle/emergency-services-funding-remissions-land-regulations-2014.txt`, with its `.formulas.md` sidecar |
| Motor Vehicles Act 1959 | **2024-11-07** (2025-03-10) | `../../../motor-vehicles-act-1959/registers/source-bundle/motor-vehicles-act-1959.txt` |
| Motor Vehicles Regulations 2010 | **2025-02-20** (2025-03-10) | `../../../motor-vehicles-regulations-2010/registers/source-bundle/motor-vehicles-regulations-2010.txt` |

The Act text is ten years older than its Regulations; the Current Titles list of 22 September 2026 listed the Act at the same date (1.7.2015), so it may simply not have been amended since.

**What is an input, because the deposit does not hold it:**

- the Adelaide CPI figures for reg 3(3) indexation (ABS; for 2024/25 they are not needed: finding 2), and the previous year's amounts for the reg 3(4) floor;
- the Minister's low income amount for each class of person (published on the concessions website; reg 3(1));
- the reg 7(1a) general remission and the reg 7(2) concession holders' remission of the levy: their formulas are missing from the corpus text (finding 1);
- the levy itself (declared each year under s 10 of the Act);
- the prescribed registration fee for a vehicle or trailer (the Regulations' fee scales are not encoded);
- the days allowed where a text sets no time (s 8(2), s 8(3)(a)) or leaves it to the Minister's directions (s 8(3)(b)) or the Registrar's notice (reg 76(4)).

**Coverage by year.** The concession and the water rates remission cover financial years from 2024/25, when reg 8 and the reg 5(5) amounts were substituted (49/2024); an earlier year answers `not covered`. The levy remissions are for 2024/25 only (finding 15); any other year answers `not covered`. The car and licence rules have no year limit, but are the texts as at 2024-11-07 and 2025-02-20.

The licence is the corpus's CC BY 4.0, recorded in this folder's `SOURCE-LICENSE.md` (a copy of the Act subject's) and in each of the other five subjects' `SOURCE-LICENSE.md`. Every module header says the content is based on the South Australian Legislation website, taken from the corpus.

## Checks

`l4 run` on every `.l4` in the folder (2026-10-24, after the corrections in findings 22-25): **0 errors, 0 warnings**, and **270 assertions written, 270 satisfied**.

| Case file | Assertions | `#TRACE`s (each with an `-- expect:` line, read and as expected) |
|---|---|---|
| `colc-cases-concessions.l4` | 109 | 4: the Minister's payment still pending after an application (twice: no payment, and a payment of the wrong amount), a breach of s 8(2), a breach of s 8(3)(b) |
| `colc-cases-levy.l4` | 48 | 2: a breach of the duty to pay the levy by the payment date, and a short payment still pending |
| `colc-cases-vehicles.l4` | 48 | 3: after a death with the balance unpaid, the prohibition on driving the void registration pending, then breached by driving; a breach of the duty to pay the additional licence fee |
| `colc-cases-seat.l4` | 65 | none |

The five modules also run clean on their own. `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. As a control, copies of two case files with expected values altered (the levy remission 246 to 247 in four places, the 2025/26 concession 263.20 to 263.10) were run: the runner reported 4 and 1 failures, as it should. After the corrections, a second control altered two of the new expected values (the last year barred by Switch for Solar 2032 to 2033 in the core cases, Omar's share of the levy 125 to 126 in the seat cases): 1 failure each, as it should.

**A breaking change for deployment.** The corrections removed one input from two exported levy questions (finding 24), so a deployment of `colc-seat.l4` must be updated under the same name.

Every expected value was worked by hand from the texts, with the arithmetic in the comment above each assertion. Levies, remission amounts, fees, incomes and CPI figures in the cases are **illustrative**.

## Seat

**The concession holder**: a holder of a Commonwealth concession card, a recipient of a listed Commonwealth payment, or a low income earner, who owns or rents a home or owns a car. The questions are the ones that person asks:

- Do I occupy my home as an owner or a tenant? Am I an eligible person? Am I entitled to the cost of living concession this year, and if not, why not? How much is it? By what day must I apply? For which years does Switch for Solar bar me?
- If I was paid a concession I was not entitled to, how much can be recovered from me? What is the most I can be fined? Is interest paid if the concession is late?
- Do I meet the criteria for a water (irrigation) rates remission, and how much is remitted?
- For how much of the emergency services levy can the Commissioner look to me? Is my notice's payment date valid? Am I entitled to the concession holders' remission, how much is remitted for me (and a co-owning spouse or partner), and what share of the levy is left for us?
- Is my car registration fee reduced, under which section, and to what? What does my trailer cost? Until when does a reduced registration last after a death or sale? What is the balance, and can I get a refund?
- What is my driver's licence fee and the administration fee? What extra must I pay if I lose my card? Does the Registrar's notice give me enough time?

The Minister, the Commissioner of State Taxation and the Registrar of Motor Vehicles get no seat. Their judgments are answered conditionally: the Minister's opinion under s 4(3) (the water rates question asks whether the criteria are met, "entitled if the Minister is of that opinion"), the Minister's satisfaction about a principal place of residence on 1 July (levy reg 6(6), an input), the Minister's means test for hardship (reg 5(1)(c)), the Minister's split (reg 7(3aa)) and exceptional circumstances (reg 7(3c)), the Registrar's satisfaction "by such evidence as the Registrar requires" (ss 38-38B, stated in each question), and the Registrar's discretion to refund (s 40A, answered as "the Registrar may refund such part ... as the Registrar thinks just").

No second seat: the texts put no real duties on another private party.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers or dates.** Followed, and widened as the task asked: the Cost of Living Concessions Regulations set the concession's numbers; the Emergency Services Funding Act and its Remissions--Land Regulations, and the Motor Vehicles Act and its Regulations, are brought in because the same Commonwealth cards switch them on (below). Only the provisions listed under Scope are read.
- **The actors the text names.** Followed.
- **Judgments left to others are answered conditionally.** Followed (above).
- **Definitions worked out from facts; borrowed terms asked as facts.** Worked out: occupying as an owner or tenant (s 2(2)-(3), reg 4), eligible person (s 3(1), reg 6), prescribed card and prescribed payments (reg 3(1)), low income earner, prescribed capacity (reg 3(2)), the owner of land (ESF Act s 3(1)(a), (e), (f)), residential land as the notice states it, the reg 6(5) classes, the ss 38-38B conditions, the clause 22(7) pensioner entitlement card holder. Asked as facts: holding each Commonwealth card or payment, being a relevant asylum seeker, the result of service under repatriation law, a heavy vehicle.
- **One case is the text's natural unit.** One person, one home and one financial year (the concession, the water rates); one parcel of land and one notice of levy, with the person asking and a co-owning spouse or partner (the levy); one vehicle or trailer and one registration period; one licence.
- **The texts' own terms, each with a plain gloss.** Followed; each rule quotes the words it encodes.
- **Machinery out.** Followed (below).

**Departures and readings**, each also a finding where it matters:

- On the water rates remission, the occupation is taken to be the same on the date billed and the date payable; only the card is asked date by date (reg 5(1)).
- On the levy, a co-owning spouse or partner is taken to hold the same kind of interest as the person asking (seat layer only), and "holds residential land" is read as being the owner (finding 13).
- "One month after" a death or sale is read as the same day of the next month, or its last day where it is shorter (s 38A(3)); the Acts Interpretation Act 1915 is not deposited.
- A remission is never more than what it remits from (findings 11 and 12).

No requirement ledger covers South Australia, so no ledger line is closed. No scenario life cites these texts.

## Scope

**In:**

- Cost of Living Concessions Act 1986: s 2(1) ("residential premises", "rates"), s 2(2)-(3), s 3, s 4(1), (3), s 7, s 8(2)-(4).
- Cost of Living Concessions Regulations 2020: reg 3(1) (prescribed card list, prescribed payments, low income earner, relevant asylum seeker, water rates), reg 3(2), reg 3(3)-(4) (indexation, never below the previous year), reg 4, reg 5 (30% between the indexed minimum of $236.40 and maximum of $377.00, proportionate for joint owners, the relevant date), reg 6, reg 7 (apply before 31 December unless paid last year for the same premises; account details; one payment per premises; the same-room exception; the Minister's split; Switch for Solar for 9 or 10 years; the Minister's exception), reg 8 ($255.60, indexed).
- Emergency Services Funding Act 1998: s 3(1) (owner, paragraphs (a), (e), (f)), s 15(1)-(2), s 16(1)-(3).
- Emergency Services Funding (Remissions--Land) Regulations 2014: reg 3 (residential land; the relevant financial year, 2024/2025 only), reg 5A, reg 6 (the reg 6(5) classes, the window between the notice's issue and payment dates, the principal place of residence on 1 July, joint owners and couples), reg 7(1a) and 7(2) (inputs), reg 7(3) (a further $46), reg 8 (order of deduction).
- Motor Vehicles Act 1959: s 37A, s 38, s 38A, s 38AB, s 38B, the common subsections (2) and (3), s 40, s 40A; s 9(1) only as the consequence of a void registration.
- Motor Vehicles Regulations 2010: reg 76(4)-(5), reg 77(3) (66.667%), reg 77(4) (50%), Schedule 1 clause 1 (level 2 fee) and clause 22(1)-(5), (7) (the licence fee, $26 or $53 a year, by quarters; the administration fee; the additional fee on ceasing to hold the card).

**Out:**

- Cost of Living Concessions Act: s 5 (delegation), s 6 (payments to rating authorities), s 8(1) (false or misleading statements), s 9; the Minister's means test itself.
- The levy on non-residential land, and the rural, regional, residential park and other-use remissions (regs 8A-12); reg 5 (Crown-land occupiers: answered `not covered`); regs 13-20 (Regional area 3, subsequent owners, public land tenants, private roads); ESF Act s 15(3)-(6) (a subsequent owner's liability for a levy left unpaid, and recovery from the owners primarily liable: finding 23); ESF Act s 3(1) paragraphs (b)-(d); s 5(10) (residential land held from the South Australian Housing Trust is exempt); the declaration of the levy and its factors (ss 5-10), the assessment book, refunds, interest and penalty levy, recovery and collection (ss 12-22M), and the levy on vehicles and vessels.
- All other registration and licence fees, including the fee scales; s 34 and s 37 except as "another provision" under subsection (2)(b); s 41 (misuse), s 42 (transfer); clause 22(6); the Motor Vehicles Act's Part 4, which the victims of crime encoding uses separately.

## Why these six together

This answers the concession holder's questions: am I entitled to the cost of living concession this year and how much, by when do I apply, do I get a water rates remission, how much of my emergency services levy is remitted on my home, and what comes off my car registration and licence. They are grouped because the texts switch them on with the same Commonwealth cards and payments, as the jurisdiction README's joins record:

- Cost of Living Concessions Regulations reg 3(1) and Remissions--Land Regulations reg 6(5) list the same Pensioner Concession Card, Low Income Health Care Card, Gold Repatriation cards and Social Security Act payments (with the differences in findings 4 and 10).
- Motor Vehicles Act s 38A and Schedule 1 clause 22 of the Regulations use a Commonwealth pensioner entitlement card.

Each regulation is grouped with the Act whose numbers it sets: the Cost of Living Concessions Regulations with that Act, the Land Remissions Regulations with the Emergency Services Funding Act, Motor Vehicles Regulations reg 77 with ss 38-38B. The Emergency Services Funding and Motor Vehicles Acts come into this one encoding, rather than encodings of their own, to keep the South Australian plan to five encodings. Only the provisions listed are read.

## Commonwealth links

Cross-folder IMPORT does not work, so these are links, not code. Each is an input here:

- **Cards and payments under the Social Security Act 1991**: Austudy, JobSeeker payment, parenting payment, special benefit and youth allowance, the Pensioner Concession Card and the (Low Income) Health Care Card, and the Commonwealth Seniors Health Card. Whether a person holds or receives one is decided there: `../../../../social-security-act-1991/encodings/baseline-2026-10/` (and `naive-2026-10/`).
- **The Gold Repatriation Health Cards (TPI, War Widows, EDA)** and repatriation pensions at the total incapacity rate or for impairment of locomotion (Motor Vehicles Act s 38(1)(b), Schedule 1 clause 22(1)(a)): `../../../../veterans-entitlements-act-1986/encodings/baseline-2026-10/`.
- **The Gold card for 80 or more impairment points** (reg 3(1)(f); levy reg 6(5)(e)): `../../../../military-rehabilitation-and-compensation-act-2004/encodings/baseline-2026-10/`, which works out impairment points under the Guide.
- Abstudy, the Community Development programs, Self-Employment Assistance, farm household allowance (Farm Household Support Act 2014) and the bridging visa E (Migration Act 1958) are Commonwealth matters with no encoding in this repository yet.
- Whether the concession and the remissions count as income for Commonwealth income tests is not stated in these texts (the README marks it unverified).

## What the texts turn out to say

1. **The two levy remission formulas are missing, so their amounts are inputs.** Reg 7(1a) (the general remission) and reg 7(2) (the concession holders' remission) each end "in accordance with the following formula:" with nothing after it in the corpus text; reg 7(2)'s "where" list survives ("A is the amount of the remission; L1 is the amount of the component of the levy that is based on the value of the land; PR is the prescribed rate"). Only the further $46 of reg 7(3) is in the text. The person states both amounts from the notice of levy. Asserted for the $46 and the order of deduction.
2. **For 2024/25 the indexed amounts are the amounts stated.** Reg 3(3) multiplies by the CPI for the December quarter of "the immediately preceding year" divided by the December 2023 quarter. For the year beginning 1 July 2024 both are the December 2023 quarter, so the multiplier is 1: $255.60, $236.40 and $377.00. The first CPI movement is in 2025/26 (illustrative: $263.20). An amount is rounded up to 10 cents and is never below the previous year's (reg 3(4)). Reg 3(3) still says "beginning on 1 July 2021", from before 49/2024 moved the base quarter. Asserted.
3. **The list of prescribed cards ends on "or".** Paragraph (f) of "prescribed card" in reg 3(1) ends "; or" with nothing after it, as if a paragraph were missing, though the legislative history shows no amendment to that definition. Encoded as the six cards listed. Not asserted (an absence).
4. **A Commonwealth Seniors Health Card opens the concession and the levy remission, but not the water rates remission.** Reg 6(b) names it separately for the concession, and levy reg 6(5)(f) lists it, but it is not a "prescribed card", which is all reg 5 accepts. Asserted.
5. **Switch for Solar costs ten years of the concession either way.** A person who enters the program in a year is barred that year and the 10 following years if paid for that year anyway, or the 9 following years if not (reg 7(3a)): ten unpaid years in both cases. The Minister may lift the bar for a year in exceptional circumstances (reg 7(3c)). Asserted.
6. **Reg 7(3b) and s 8(3)-(4) pull different ways.** Reg 7(3b) says a person already paid for the year in which they enter Switch for Solar "is not required to return the payment", although reg 7(3a)(a) makes them not eligible for it; s 8(3)-(4) require a payment one "is not entitled to receive" to be refunded and make it a debt. READING: the regulation's specific relief means the payment is not one to be refunded or recovered. Asserted.
7. **Being a low income earner is measured over the whole year, but s 3(1) asks about 1 July.** Reg 3(1): a person who "during that financial year, earned income that was less than the amount determined by the Minister for that class of person"; s 3(1): "on 1 July of that financial year, the person ... was of a class prescribed". The encoding takes the year's income against the Minister's amount (an input; no notice is deposited). Asserted.
8. **Several classes began halfway through 2024/25.** The relevant asylum seeker and the fleeing-conflict support package (reg 6(e), (f)), rooming house and supported residential facility residents (reg 4(2)(b), (c)), and reg 7(3) and (3aa) came in from 1 January 2025 (102/2024), after the 1 July 2024 test day. Whether they reach 2024/25 is not settled by the text; the encoding applies the text as at 2025-01-01 to every year it covers. Not asserted as a date question.
9. **"Water rates" are irrigation rates only, and the Act's own list of Acts is older.** Reg 3(1): rates under the Irrigation Act 2009 or the Renmark Irrigation Trust Act 2009. So SA Water's water and sewerage charges are not remitted under reg 5. The Act (as at 2015-07-01) still names the Renmark Irrigation Trust Act 1936 and the Irrigation Act 1994 in "rates" and Schedules 1 and 4. Encoded, not asserted.
10. **The two regulations name the Commonwealth programs differently.** The cost of living regulations name "the Community Development Employment Project or Remote Jobs and Economic Development Program"; the levy regulations name "the Community Development Program". Each is its own choice, and each opens only its own remission (asserted). The cost of living regulations name "Self-Employment Assistance allowance payments" and the levy regulations "the Self-Employment Allowance"; READING: one program, one choice. Levy reg 6(5) runs (l), (n) with no (m); both lists skip (iv), (v) and (vii), deleted in 2024.
11. **A water rates remission cannot be more than the rates.** Reg 5(4) gives 30% "subject to the prescribed minimum remission", which is $236.40, but does not say what happens when the rates are less than that. READING: the whole of the rates is remitted. Asserted ($200 of rates, $200 remitted).
12. **The further $46 cannot take the levy below nil.** Reg 8 says the reg 6(1) remission "must be determined and deducted before" the reg 6(2) remission. READING: that order matters because the $46 comes off what is left, so it is held to what is left. Asserted ($220 levy, $200 then $20).
13. **"Holds residential land" and "a couple owns" are read as being owners.** Reg 6(1)(a) says "holds", undefined; reg 6(3)-(4) speak of owning. READING: holding is being the owner liable under s 3(1) and s 15(1), and reg 6(4) needs both members of the couple to be owners. Under reg 6(4) a co-owning spouse without a card is entitled where both live there and either is entitled. Asserted.
14. **Where no owner is entitled under reg 6, the general remission is taken in shares.** Reg 5A(1) remits the levy "for the benefit of all persons who are liable"; reg 5A(3) apportions it by interest only where a co-owner is entitled under reg 6. READING: the answer for one owner's share is that share of the general remission in both cases, matching s 15(2)'s contribution in proportion. So whether some other co-owner is entitled under reg 6 changes nothing for the person asking, and it is not asked (finding 24). Asserted.
15. **The levy remissions are for 2024/25 only.** Reg 3: "relevant financial year means the 2024/2025 financial year"; the history shows the definition varied every year (2022, 2023, 2024). Any other year answers `not covered`. Asserted.
16. **Sections 38, 38A and 38B each exclude the others.** Each subsection (2)(b) excludes a vehicle "in respect of the registration of which a reduced fee is payable pursuant to any provision of this Act other than this section". An incapacitated ex-service owner who also holds a pensioner card meets both s 38 and s 38A, and each points at the other; the text does not say which gives way. Answered `not covered`. Asserted.
17. **The ex-service lists differ between registration and the licence.** Section 38(1)(b): "totally and permanently incapacitated, or is blind, or has lost a leg or foot, or receives" a pension at the total incapacity rate or for locomotion at 70% or more. Schedule 1 clause 22(1)(a): "totally or permanently incapacitated", no blindness, the same pensions. So a person blind from service gets the 66.667% registration reduction but pays the full licence fee, and one incapacitated permanently but not totally pays the $26 licence fee but gets no s 38 reduction. Section 38 says "Her Majesty", clause 22 "His Majesty". Asserted.
18. **Losing the card does not end a reduced registration, but it does cost licence fees.** Section 38A(3) (like ss 38(3), 38AB(3), 38B(3)) acts only when the registered owner dies or stops owning the vehicle: then the registration lasts one month and becomes void unless the balance is paid. Nothing in these sections reaches an owner who keeps the vehicle and loses the card. Clause 22(3), by contrast, charges the licence holder. Asserted.
19. **Clause 22(3) is an additional fee, not a refund.** A person who ceases to be a pensioner entitlement card holder, holding a licence bought at the reduced fee, "must pay an additional fee": for each complete 3 months left, a quarter of the difference between the $53 and $26 annual fees ($6.75). The Registrar may require it by written notice allowing at least 14 days (reg 76(4)) and recover it as a debt (reg 76(5)). READING: a 3-month period is three calendar months, and the unexpired period runs to the end of the expiry day. Asserted ($135 for 20 quarters).
20. **Some duties have no time.** Section 8(2) (tell the Minister on ceasing to meet a remission criterion) and s 8(3)(a) (tell the Minister of a payment not due) set no time, and s 8(3)(b) leaves the time to the Minister's directions; the Minister's duty to pay (s 3(2)) has no time either, and s 7(2) says no interest is payable. The days are inputs; the Minister's duty is left pending in the traces. Asserted.
21. **The payment date on a notice of levy must be at least 28 days after service** (s 16(2)(d)); service on one co-owner is service on all (s 16(3)); co-owners are jointly and severally liable for the whole levy, with contribution between them (s 15(2)). Asserted, except s 16(3).

Findings 22-25 are corrections made on 2026-10-24 after an independent verifier's review; each was checked against the deposited texts before it was made.

22. **Correction: the spouse or domestic partner of a beneficiary under an estate is neither an owner nor in a prescribed capacity.** Section 2(2)(b)(ix) takes its spouses from reg 4(1)(a): "spouses and domestic partners of any of the persons referred to in subparagraphs (i) to (vii) of section 2(2)(b) of the Act". The beneficiary is (viii). Reg 3(2)(h) likewise reaches "the spouse or domestic partner of any of the persons referred to in paragraphs (a) to (g)", and the beneficiary is (i). The first version had one spouse choice, listed below the beneficiary and worded "of a person occupying in one of the capacities above", and counted it in both lists. So the spouse of a beneficiary was wrongly treated as occupying as an owner (for the concession) and in a prescribed capacity (for the water rates remission). Now the spouse of a person in (i)-(vii) is one choice, in both lists, and the spouse of a beneficiary is a separate choice, in neither. No expected value changed, because no earlier case had a beneficiary's spouse. New cases: Ann, living in the house her husband may occupy as a beneficiary, occupies neither as an owner nor as a tenant, is not an eligible person, and does not meet the water rates criteria. Asserted.
23. **Correction: s 15(3) is out of scope.** The scope listed ESF Act s 15(1)-(3), and the levy module's header said "subsequent owners". But s 15(3) ("A subsequent owner of land is liable for a levy, or a part of a levy, in respect of that land that has not been paid by the person or persons primarily liable") was only quoted in a comment. No rule or case reaches it: liability turns only on the interest held at 12.01 a.m. on 1 July (s 15(1)). The scope now reads s 15(1)-(2), and s 15(3)-(6) is listed as out. A buyer asking about a levy the seller left unpaid gets no answer here. Not asserted (an absence).
24. **Correction: an input that changed no answer was removed.** The levy questions "How much of the levy on my home is remitted for us" and "What is my share of the levy after the remissions" asked whether another co-owner is entitled to the concession holders' remission. That answer went into a field of `Owners of the home` that no rule read, so it could not change a result. Under finding 14 it should not: an owner not entitled under reg 6 gets their share of the general remission either way, and an entitled owner's reg 6(3) part depends only on their own share. The field and the input are gone. New cases (Omar, half owner with his brother, no card: 25 remitted, 125 to bear) show the answer without it. Asserted.
25. **Correction: two seat questions restated the core's rules; the rules are now in the core.** "By what day must I apply" worked out the reg 7(2) exemption in its own branch. "For which years does Switch for Solar bar my concession" wrote the reg 7(3a)(a) first barred year and the "entered" test itself. `colc-concessions.l4` now holds both: `regulation 7(2) lifts the application requirement`, which the entitlement rule and the regulative rule also use, with `the application deadline for the financial year beginning in`; and `the first financial year barred by Switch for Solar begins in` with `the financial years barred by Switch for Solar`. The two seat questions only call them. Their answer types moved to the core in the texts' own terms. Two seat-case labels changed with them ("no application needed: paid the concession for the previous financial year for the same premises"; "not barred: the Switch for Solar program was not entered"). No value changed. Asserted, in the core and seat cases.

## What would need doing before this is worth relying on

- Replace all six texts with the current official ones from legislation.sa.gov.au when it can be fetched, and re-run the cases. In particular, take the Emergency Services Funding Act at its later version and the Remissions--Land Regulations for the current financial year, whose "relevant financial year" will have moved.
- Transcribe the reg 7(1a) and 7(2) formulas from the authorised rendering into the `.formulas.md` sidecar, and encode them in place of the two inputs.
- Deposit the ABS Adelaide CPI series and the Minister's published low income amounts, so those inputs can become figures.
- Settle findings 6, 8, 11, 12, 13, 14 and 16 against an authoritative reading.
- Encode the out-of-scope remissions (regs 5, 8A-20), ESF Act s 5(10) and s 15(3)-(6) (a subsequent owner's liability), s 8(1) of the Act, and the registration fee scales, if the seat needs them.
- An independent test pass, a coverage table and a human gate.
