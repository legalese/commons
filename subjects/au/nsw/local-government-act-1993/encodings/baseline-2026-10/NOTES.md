# Local Government Act 1993 (NSW): pensioner rates concession, baseline encoding for the eligible pensioner

> **The texts encoded are not the current official text and may be out of date.** Both come from the Open Australian Legal Corpus as collected on 10 March 2025 (the owner's decision of 2026-10-20), because legislation.nsw.gov.au refused this repository's fetcher. Check legislation.nsw.gov.au before relying on anything here.

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18.
There is no REFUSE in it. A case outside the encoding answers `not covered` with its reason, and tests assert each one.
It was checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

It is written in two layers:

- **`lga-concession.l4`**, the seat-neutral core. It uses the Act's own actors and terms: "an eligible pensioner", "a jointly eligible occupier", "the person making the application", "the council". The computations (the cl 134 class, the s 575(2) paragraph, the reduction and its caps, full quarters, the s 584 end day and credit) are functions. Where the text says "is to", "may" or "may not", there is a regulative rule (`DEONTIC`): five in all, with the council as the actor in each.
- **`lga-seat.l4`**, the pensioner's seat. It asks 10 questions, each with `@export` and a `@desc` on every input, grouped under `§§` headings. It builds the core's records from plain answers and restates no rule.

No earlier encoding of this Act existed, so nothing is kept beside it. There is no NSW requirement ledger, so no ledger line is closed. The Act was deposited for the pensioner rates concession only (Chapter 15, Part 8, Division 1); nothing else in it is encoded.

## Edition

- **The Act:** Local Government Act 1993 No 30, corpus document `nsw_legislation:2025-01-01/act-1993-030` (version 2025-01-01, scraped 10 March 2025), deposited at `../../registers/source-bundle/act-1993-030.txt` (1,197,506 characters, text sha256 `bf04ffc6…f95f0`). Used: Chapter 15, Part 8, Division 1 (ss 575–584), the Dictionary definitions of "dwelling", "eligible pensioner", "jointly eligible occupier", "quarter" and "year", and, for reading them, ss 546 (levying by notice), 560(3) (joint and several liability) and 562 (instalments).
- **The Regulation:** Local Government (General) Regulation 2021, corpus document `nsw_legislation:2024-09-02/sl-2021-0460` (version 2024-09-02), deposited at `../../../local-government-general-regulation-2021/registers/source-bundle/sl-2021-0460.txt` (658,510 characters, text sha256 `1d369b31…e1fc7`). Used: Part 5, Division 4, cll 134 (prescribed classes), 135 (the approved form) and 136 (persons prescribed for s 582); cl 127(1)(j) for reading "quarterly instalment period". The same CC BY 4.0 terms apply; its own `SOURCE-LICENSE.md` is beside its deposit.
- **Figures.** The caps are the Act's own: $250 for ordinary rates and domestic waste management charges together, $87.50 each for water supply and sewerage special rates or charges (s 575(3)). They are not indexed. Section 580 lets a regulation vary the reduction; the deposited regulation does not, so the caps stand as stated, and a person who says a later regulation has varied them is answered `not covered`.

Based on content from the New South Wales Legislation website at 10 March 2025 (State of New South Wales, CC BY 4.0), through the Open Australian Legal Corpus (CC BY 4.0). See `SOURCE-LICENSE.md`.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `lga-concession.l4`, `lga-seat.l4` | `lga-cases-pensioner.l4` | 82 written, 82 satisfied |

`l4 run` on each of the three files: 0 errors, 0 warnings (2026-10-24). In addition, 3 `#TRACE`s carry an `-- expect:` line: one breach by the council (proceedings to recover an ordinary write-off), and two duties still pending (a reduction not written off; a credit of the wrong amount). Each was read and matches its expectation.

`l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. As a control, a copy with one expected value altered (Ron's total, $402.50 to $400) was run: the runner reported the two assertions that use it as failed.

Every expected value was worked by hand from the text, with the arithmetic in the comment above the assertion. All the amounts are exact in binary fractions, so equality is exact.

## Seat

**The eligible pensioner liable, solely or jointly, for council rates and charges on the dwelling they live in.** They ask: "Am I an eligible pensioner for this dwelling?", "How much are my rates and charges reduced this year, alone or with a co-owner?", "What if I became a pensioner part-way through the year?", "When does my concession stop, and is anything credited?", "Can the council later recover what it wrote off?", and "Can the council give me more under s 582?".

Most of Division 1 is addressed to the council: reduce on application, write off, credit, do not recover. Each is encoded as what the pensioner is owed. In the core they are regulative rules with the council as the actor. **The council is a public body and has no seat**; no other party bears duties under this Division, so there is no second seat.

The 2026-10-18 defaults:

- **The Act alone, with the instrument that sets its numbers.** Followed. The Regulation is brought in because it defines who qualifies (cl 134) and prescribes the form (cl 135) and the s 582 class (cl 136). It sets no numbers.
- **The actors the text names:** the eligible pensioner, the jointly eligible occupier, the other persons jointly liable, the council.
- **Judgments left to others are answered conditionally, as inputs:** the time for applying fixed by council resolution (s 579(2)); whether eligibility was verified "as prescribed" (s 579(3)); whether a council hardship order (s 577) or a s 582 waiver applies, each of which makes the answer `not covered`.
- **The Act's own definitions are worked out from facts:** eligible pensioner (with the cl 134 classes), jointly eligible occupier (its three limbs and the shared home), dwelling, quarter, year. Borrowed terms are asked as facts: every Commonwealth status in cl 134 and cl 136, "spouse or de facto partner", "sole or principal place of living".
- **One case:** one pensioner, one parcel of land, one rating year.
- **The Act's own terms**, quoted in the comment above each rule.
- **Machinery out:** reimbursement of councils (s 581).

Departures, each small:

- **Co-owners are asked as counts.** The core takes a list of the other persons liable, one record each. The seat asks how many fall in each limb of "jointly eligible occupier" and how many in none, and builds the list. This keeps the form to plain numbers and the definition in the core.
- **Dates are `DATE` inputs**, and the rating year is named by the calendar year in which it starts.

## Scope

**In:**

- the Dictionary definitions above;
- cl 134(a)–(d): the five prescribed classes;
- s 575(1): reduction on application and evidence, for land on which a dwelling is situated;
- s 575(2)(a) and (b): one-half, or the proportional share of one-half;
- s 575(3): the caps, reduced in the same proportion under (2)(b);
- s 575(4): becoming an eligible pensioner after the levy, by full quarters remaining;
- s 575(5): discharge as between persons jointly liable (a core function, asserted; not a separate question);
- s 576: postponed rates, as an instruction for the amounts entered;
- s 579 with cl 135: the application, its form and time, and continuation without re-application (regulative rules);
- s 583: writing off, and when proceedings to recover are allowed;
- s 584: the end of the entitlement and the credit for a full prepayment;
- s 582 with cl 136: who the council may choose to relieve (a permission and a yes/no question).

**Not covered, with an explicit answer and a test:**

- a regulation varying the amounts under s 580 (none in the deposited regulation);
- a council hardship order under ss 577–578 (council discretion; its effective date and refund directions are the council's);
- the amount of a s 582 waiver (council discretion);
- a rates notice served outside the rating year it is for (s 546(2), (3));
- a part of the liability, under s 575(2)(b), that is not more than 0 and at most 1.

**Out:**

- Division 2, postponement of rates (ss 585–599), and the rest of Part 8;
- every other part of the Act and the Regulation, including cl 130(b) (writing off stormwater charges for eligible pensioners, under s 607);
- water and sewerage concessions of Sydney Water and Hunter Water, which fall under other statutes;
- rounding: the Act states none, and none is applied.

## What the Act turns out to say

1. **Once eligible for the MRCA Special Rate Disability Pension is enough, for life.** Regulation cl 134(d) prescribes persons "who receive, or who at some point in their life have been eligible for" it. No current payment, no card and no income or assets test is needed. Classes (b) and (b1) carry the card's means test; (a) needs entitlement to the card; (c) and (d) need neither. Asserted.
2. **A co-owner who lives in the home is not always a jointly eligible occupier.** Only a spouse or de facto partner, another eligible pensioner, or the partner of another eligible pensioner qualifies, and each must share the pensioner's home. An adult child who lives there but is not a pensioner is none of these, so one such co-owner moves the pensioner from s 575(2)(a) to (2)(b). Kevin and Lyn, owning three-quarters with their daughter Amy, get $187.50 instead of $250, because the cap is also cut to three-quarters. Dorothy, half-owner with a son who lives elsewhere, gets $183.75 on rates and charges of $2,260, whose half would be $1,130. Asserted.
3. **On its words, s 575 halves every rate or charge on the land, and caps only three groups.** Section 575(1) and (2) reach "a rate or charge levied on land on which a dwelling is situated". Section 575(3) caps only (a) ordinary rates with domestic waste management charges, (b) water supply special rates or charges and (c) sewerage special rates or charges. Any other special rate, or a stormwater management services charge, is therefore halved with no cap. The encoding follows the words and reports this part separately: a $25 stormwater charge adds $12.50 to Margaret's $250, for $262.50. Asserted. Regulation cl 130(b), which separately lets a council write off a stormwater charge for an eligible pensioner, suggests the drafters did not expect s 575 to reach it. Whether councils apply s 575 to these charges is **unverified (from general knowledge, not from the texts)**. Check it before relying on this part.
4. **Becoming a pensioner the day after the notice costs a quarter, and the cap is scaled too.** Under s 575(2) the test is eligibility "on the date on which the rate or charge is levied", that is, the day the notice is served (s 546(1)). Under s 575(4), a person who becomes eligible later gets a reduction "proportionate to the number of full quarters remaining after the day". Eligible on the levy day itself, Helen gets the whole year. The next day, three quarters: $187.50 and $65.625 for $253.125. From 10 November 2025, two quarters: $168.75. From 1 April 2026, nothing for 2025-26. Asserted. The encoding reads the proportion as applying to the capped reduction. Read the other way (half the rates times the quarters, then capped), Helen's 10 November case would give $325 rather than $168.75. That alternative is not asserted.
5. **"Quarterly instalment period" is not defined.** Section 584(1) ends the entitlement "on the last day of the quarterly instalment period during which those circumstances occur". The encoding reads that as the Dictionary "quarter" (ending 30 September, 31 December, 31 March or 30 June). Regulation cl 127(1)(j) supports this reading: rates notices must say that "concessions are available to eligible pensioners for any quarter in which they are eligible pensioners". On that reading, a change on 15 November 2025 ends the concession on 31 December 2025, and $800 of a $1,600 full prepayment is credited. A change in the April–June quarter leaves nothing to credit. Asserted. If the periods ran instead to the instalment due dates (31 August, 30 November, 28 February, 31 May, s 562(3)), some end dates would move.
6. **Section 584 gives no recovery power in terms, though s 583(2) points to it.** A council "may not take proceedings to recover an amount so written off unless" for a wilfully false statement "or except as provided by section 584". Section 584 only ends the entitlement and gives a credit. The exception is read as reaching an amount written off for a quarter after the entitlement ended. Asserted. Section 584(2) also gives a credit only where the year's reduced rates "have been paid in full", and says nothing for a pensioner paying by instalments. Asserted.
7. **The regulation prescribes the form but not the time, and no way of verifying.** Section 579(1) requires an application "within the time and in the manner prescribed by the regulations". Clause 135 prescribes only the approved form. The time is read as the one fixed by council resolution under s 579(2), even though the regulation is "in force" for the manner. That time is an input, or none. Section 579(3) lets a council continue a reduction without a fresh application if eligibility "is verified by the council as prescribed by the regulations", but the deposited regulation prescribes no verification. So whether it was verified "as prescribed" is an input. Applying is the pensioner's choice: not applying is no breach, but brings no reduction, and the Act sets the council no time to act. Asserted in the regulative cases.
8. **The s 582 discretion reaches fewer people than the s 575 reduction.** Clause 136 prescribes only a person who receives a Social Security Act Chapter 2 payment and "is the holder of" a pensioner concession card. Clause 134(a) asks only for entitlement to the card, and also admits VEA service pensioners, while cl 134(b)–(d) need no card at all. A VEA service pensioner holding a card, a war widow or a TPI veteran is an eligible pensioner for s 575, but the council has no s 582 power to waive their rates. Asserted.
9. **"Entitled to a pensioner concession card" is not the Social Security Act's word, and other cards do not count.** The Act says a person "is qualified for a pensioner concession card on a day if a social security pension is payable" (s 1061ZA(1)). Clause 134(a) is read as meaning the same. A Commonwealth seniors health card or a health care card is a different card. A self-funded retiree with a seniors health card is in no class. So is a JobSeeker recipient with only a health care card, even though JobSeeker payment is a Chapter 2 payment. Asserted.
10. **The caps are fixed dollar figures.** $250 and $87.50 are written into s 575(3), with no indexation; only a regulation under s 580 can change them. As at the corpus version (1 January 2025) no such regulation is in the deposited Regulation. A later one would change every capped answer, and the encoding answers `not covered` when one is said to apply. Asserted.
11. **The reduction is also a discharge against co-owners.** Under s 575(5), the pensioner and any jointly eligible occupier are "discharged from liability as between that person and any other person jointly liable" to the extent of the reduction. So the co-owners cannot ask the pensioner to contribute the amount reduced: $183.75 for Dorothy as against her son. Asserted.

## The Commonwealth layer: what would feed the cl 134 facts

Cross-folder IMPORT does not work on the stable `l4`, so these links are recorded here, not in code.

- **Social Security Act 1991, Chapter 2, and the pensioner concession card.** `subjects/au/social-security-act-1991/encodings/baseline-2026-10/`. Its outputs answer this encoding's first input, "I receive a pension, benefit or allowance under Chapter 2" (cl 134(a), cl 136):
  - `Is the age pension payable to me on a given day` (Part 2.2);
  - `Am I qualified for the disability support pension` (Part 2.3);
  - `Am I qualified for carer payment for the disabled adult I care for` (Part 2.5);
  - `Am I qualified for jobseeker payment on a given day` (Part 2.12);
  - the youth allowance questions (Part 2.11).

  The pensioner concession card (Part 2A.1, s 1061ZA) is not encoded there. Section 1061ZA(1) makes a person qualified for the card when "a social security pension is payable", so a "payable" answer for the age pension, the disability support pension or carer payment is the route to the card input. Its seniors health card questions answer a different card, and do not feed cl 134.
- **Veterans' Entitlements Act 1986, Part III, s 22(4) and s 24.** `subjects/au/veterans-entitlements-act-1986/encodings/baseline-2026-10/`.
  - `Am I eligible for the age service pension (s 36)?` and `Am I eligible for the invalidity service pension (s 37)?` feed the Part III service pension input (cl 134(a)). That encoding answers eligibility, not payment, and does not encode the DVA's pensioner concession card.
  - `What rate of disability pension am I paid for my war-caused incapacity, and how much a fortnight (ss 22, 23, 24)?` feeds cl 134(c). Its answers `the extreme disablement adjustment rate (s 22(4))` or `the special rate (s 24)` put the person in that class.
  - `My partner, a veteran, has died. Do I get a war widow's or widower's pension without claiming (s 13A)?` and `What is my war widow's or widower's pension a fortnight (s 30(1))?` feed cl 134(b)(i). The card's income and assets limits are not encoded there.
- **Military Rehabilitation and Compensation Act 2004, s 234(1)(b) and the Special Rate Disability Pension.** `subjects/au/military-rehabilitation-and-compensation-act-2004/encodings/baseline-2026-10/`. Chapter 5 (s 234, wholly dependent partners) and Part 6 (the SRDP) are outside that encoding's scope; see its NOTES, the Out list and its finding 20. So no Commonwealth encoding yet answers cl 134(b1) or (d). Its question `As a former ADF member unable to work, which rate of incapacity compensation applies to me this week` says when Part 6 applies instead, which is a pointer to (d), not an answer to it.

## What would be needed before relying on it

- Replace both corpus texts with the current official ones from legislation.nsw.gov.au. Then check that s 575, the caps and cll 134–136 are unchanged, and that no regulation under s 580 has varied the amounts.
- Settle the readings in findings 3 to 7 against Office of Local Government guidance and council practice, especially the uncapped half of other rates and charges (finding 3) and the mid-year proportion (finding 4).
- Encode the Commonwealth pensioner concession card (SSA Part 2A.1 and its VEA counterpart), MRCA s 234 and the SRDP, so that the cl 134 facts can be worked out rather than asked.
- An independent test pass, and the human gates.
