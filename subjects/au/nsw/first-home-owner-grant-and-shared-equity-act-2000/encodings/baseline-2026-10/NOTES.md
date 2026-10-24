# First Home Owner Grant and Shared Equity Act 2000 (NSW): baseline encoding for the applicant

> **Warning.** The text encoded here is **taken from the Open Australian Legal Corpus, collected on 10 March 2025. It is not the current official text and may be out of date.** Its corpus version is dated 2023-09-04, the oldest in the NSW sample. Check legislation.nsw.gov.au before relying on anything here.

Based on content from the New South Wales Legislation website (State of New South Wales, CC BY 4.0), via the Open Australian Legal Corpus (CC BY 4.0); see `SOURCE-LICENSE.md`.

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18.
There is no REFUSE in it. A case outside the encoding answers `not covered`, with the reason, and tests assert it.
It was checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

It is written in two layers:

- **`fhog-core.l4`**, the seat-neutral core. It uses the Act's own actors and terms ("the applicant", joint applicants, "the applicant's spouse", "the Chief Commissioner"). The cap, the total value, the amount and the dates are functions. Where the text states a duty with a deadline or a power over the applicant, there is a regulative rule (`DEONTIC`): seven in all (ss 14(5)-(6), 20(2), 20(2A), 20(3), 21(2)-(3), 45(1), 45(2)). The applicants are numbered parties, so the seat is a parameter. Answers that can reach a gap have the type `Answer`: `answered` with the value, or `not covered` with the reason. Three-valued `and also` / `or else` let a definite "no" or "yes" settle a question even where another part is not covered.
- **`fhog-seat.l4`**, the applicant's seat. It asks 28 questions, each with `@export` and a `@desc` on every input, grouped under `§§` headings in the Act's order. It builds the core's records from plain answers and restates no rule. Every question takes its inputs in the same order: the transaction, you, the other person, the other owners. A record field that a question does not read gets a fixed placeholder, with a comment saying so.

The long argument lists in the case file were laid out by the scratchpad generator `gen_cases.py` (in the `au-nsw-2` scratchpad folder), from the seat's canonical input list, so that no argument is misplaced. The expected values were written into it by hand.

No earlier encoding of this Act existed. No requirement ledger covers New South Wales, so no ledger line is closed.

## Edition

- **The Act:** First Home Owner Grant and Shared Equity Act 2000 No 21 (formerly the First Home Owner Grant (New Homes) Act 2000), source id act-2000-021, corpus version_id `nsw_legislation:2023-09-04/act-2000-021`, as deposited at `../../registers/source-bundle/act-2000-021.txt`. It was taken from the Open Australian Legal Corpus version 7.1.0, whose NSW documents were collected on 10 March 2025. It is **not the current official text and may be out of date**: anything enacted after 2023-09-04, or not yet in the corpus on 10 March 2025, is missing. The owner decided on 2026-10-20 to use this route, because legislation.nsw.gov.au returned a bot challenge.
- **No regulation is deposited.** The Act lets the regulations set a different eligibility cap (s 13A(4)). The cap is therefore an input that defaults to the s 13A(2) figures. A regulation would change the answers.
- **Figures in the Act itself** are statutory constants: the caps of $750,000 and $600,000 (s 13A(2)); the amounts of $15,000, $10,000 and $7,000 (s 18); 12 months to move in and 12 months of residence (s 12); 6 months of earlier residence (s 11(3)); 5% for a small interest holder (s 15(2)(e)); 12 months to apply after completion (s 14(5)); 12 months to complete and 14 days to give notice and repay (s 20); 50 penalty units (ss 20(4), 21(4)). The value of a penalty unit is set by another Act, which is not deposited.

Dates are `DATE`s from the prelude (`DATE_FROM_DMY`, `DATE_SERIAL`), with no `daydate` import. "12 months after" a day is the same day a year later (Interpretation Act reckoning, the day itself excluded), and 29 February moves to 28 February (a READING).

## Checks

| Modules | Case file | Assertions |
|---|---|---|
| `fhog-core.l4`, `fhog-seat.l4` | `fhog-cases-applicant.l4` | 186 written, 186 satisfied |

In addition, 5 `#TRACE`s carry an `-- expect:` line: four breaches (a late application under s 14(5), no repayment under s 20(2), a late repayment under s 20(2A), a late notice under s 21(2)) and one permission still open (a penalty above the s 45(2) limit). Each was read and matches its expectation.

`l4 run` on all three files: 0 errors, 0 warnings (2026-10-24). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read.

A copy of the case file with one expected value altered (the s 18(2) transitional amount, $7,000 changed to $15,000) was run as a control. The runner reported the one failure.

## Seat

**The applicant for the first home owner grant**: a person buying or building a first home in New South Wales, alone or with one other person. They ask:

- Am I eligible?
- Is this home an eligible transaction, and is it under the cap?
- How much is the grant?
- By when must I apply?
- What must I do, and by when, if a condition fails, and what can be recovered?

Most of the Act after Division 2 of Part 2 addresses the Chief Commissioner of State Revenue: deciding (s 17), paying early (s 20(1)), imposing conditions (s 21), and requiring repayment and penalties (s 45). Each is encoded for what it means to the applicant: what they must do and by when, what may be done to them, and how much. In the core, the Chief Commissioner appears as a party to the s 45 permissions. There is **no second seat**: the Act puts duties only on applicants. The Chief Commissioner is an official, and gets no seat.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed. No regulation is deposited, so the s 13A(4) cap is an input (see Edition).
- **The actors the text names.** Followed: the applicant, joint applicants, the applicant's spouse, the owners of the home, the Chief Commissioner.
- **A judgment left to someone else is answered conditionally, as a fact.** Followed. The answer holds if the Chief Commissioner has decided it:
  - an approved life estate, reasonable security of tenure, or shares or units for exclusive occupation (s 5(2)(b), (f), (g));
  - being satisfied of the s 6(2) separation;
  - the age exemption (s 8A(2));
  - the residence approvals and exemption (s 12(3), (4));
  - being satisfied a contract replaces an earlier one (s 13(3A), Schedule 1 cll 19, 20(3), 22(2));
  - another commencement date for an owner build (s 13(4)(b)(ii)), folded into the commencement date;
  - allowing an application outside the period (s 14(6));
  - authorising payment before completion (s 20(1)(a));
  - a longer period for completion (s 20(2)).

  The Chief Commissioner's opinion that a building is a suitable home (s 4) and on value-reducing schemes (s 13B(3)(c), (4)) are folded into the facts "home" and "unencumbered value".
- **The Act's own definitions worked out; borrowed terms asked as facts.** Followed, with two departures.
  - Worked out: new home (s 4A), relevant interest (s 5), spouse (s 6), permanent resident (s 3), eligible transaction (s 13), type of grant (s 13AA), cap (s 13A), total value (s 13B), the application period (s 14(5)) and interested persons (s 15).
  - Asked as facts: Australian citizen and the visas (Commonwealth Acts); de facto partner (Interpretation Act 1987 s 21C, not deposited); whether something counts under the "corresponding law" of another State or a Territory (not deposited).
  - **Departure 1.** In the earlier history (ss 10, 11), whether a person held "a relevant interest in residential property" is asked as one fact. The s 5 test is a question of its own (`Is my interest a relevant interest`), but it is not applied to each past property.
  - **Departure 2.** The s 15 owners who do not apply are described by two numbers: the largest share among them, and the total share of all small interest holders. They are not listed one by one (see finding 7).
- **One case is the text's natural unit.** Followed: one eligible transaction (s 7(4)), with every applicant on the application.
  - **Departure 3.** The core takes any number of applicants and partners, but the seat asks about you and one other person (a spouse or de facto partner, applying or not, or a co-applicant). Where there is someone further, the questions that involve other people answer `not covered`.
- **The Act's own terms, each with a plain gloss.** Followed: comments quote the statutory words.
- **Operative sections in; machinery out.** Followed.

## Scope

**In:**

- s 4A (new home), s 5 (owner, relevant interest), s 6 (spouse);
- s 7 (entitlement, including s 7(3) payment before completion and s 7(4) one grant per transaction);
- ss 8, 8A, 9, 10, 11, 12 (the eligibility criteria, with the joint-applicant exemptions in ss 9(2) and 12(6));
- s 13 (eligible transactions, commencement date, completion, consideration), s 13AA (builder's and purchaser's grants), s 13A (caps), s 13B (total value);
- s 14(5), (6) (the application period), as a function and as a regulative rule;
- s 15 (all interested persons to apply, with the s 15(2)(e) small interest holder worked out);
- s 18 (amount);
- s 20(2), (2A), (3), (4) (the conditions of an advance payment), as dates and as regulative rules;
- s 21(2)-(4) (conditions imposed by the Chief Commissioner; joint liability);
- s 45(1)-(3) (repayment and penalty), as functions and as permissions of the Chief Commissioner.

**Not covered** (answered `not covered`, and asserted):

- a commencement date before 1 October 2012: Schedule 1 cl 18 keeps the earlier Part 2, which is not in the deposit;
- a contract the Chief Commissioner is satisfied replaces one made before 1 July 2017 (s 13(3A); Schedule 1 cll 19, 20(3), 22(2));
- the eligibility cap, and so payability, for a commencement date before 1 July 2017: Schedule 1 cl 22(1) keeps the earlier caps. The amount under s 18(1)(a) is still answered;
- a regulation under s 13A(4) whose cap was not given;
- anything that turns on the "corresponding law" of another State or a Territory (ss 10, 11), when the applicant cannot say whether it counts there;
- a seat question about more people than you and one other.

**Out:**

- Part 2A (shared equity schemes): a fund administered by the Chief Commissioner, not an entitlement;
- s 43A (the ADF home buyer's grant; see finding 16);
- Parts 2B and 3 (objections and review, administration, investigations);
- ss 6A-6D and 13(6) (multiple occupancy, homes on another's land, manufactured and moveable homes);
- s 14(1)-(4), (7) (form and information);
- s 16 (guardians), s 19 (how the grant is paid), s 22 (death of an applicant), ss 23, 24 (correcting decisions, notice);
- s 44 (false information; see finding 18);
- ss 46, 46A (recovery as a debt, the charge on the home, third parties);
- Schedule 1's transitional caps and earlier Parts, regulations, and review.

## What the Act turns out to say

1. **The grant is $10,000 for a commencement date from 1 January 2016, and $15,000 from 1 October 2012 to 31 December 2015** (s 18(1)). It is capped at the consideration (s 18(4)): an owner builder whose costs are $8,000 gets $8,000. A purchase or building contract made under an option granted in the 2012 transitional period gets $7,000 (s 18(2)). Section 18(2) has no end date, so an option granted in 2012 and exercised in 2016 still gives $7,000, less than a fresh contract would get. It does not reach an owner build. Asserted.
2. **There are two caps, by type of grant.** A purchase of a new home gets the purchaser's grant, with a $600,000 cap. A building contract or an owner build gets the builder's grant, with a $750,000 cap (ss 13AA, 13A(2)). They apply to commencement dates from 1 July 2017 (s 13A(5)); earlier dates are under Schedule 1, which is not covered. "Does not exceed" means a total value exactly at the cap is in. Asserted.
3. **A knock-down rebuild by an owner who lived in the old house.** Section 4A(3)(c) says a home built to replace demolished premises counts only if "the owner of the home did not occupy the demolished premises". But on its literal words s 4A(1) already makes any home "not previously occupied or sold" a new home, and that covers a new replacement house, so (3)(c) would change nothing. The encoding gives (3)(c) its work: such a home is not new. Asserted. That owner will often fail s 11(3) anyway; (3)(c) bites where they lived there less than 6 months.
4. **Total value, not price, is tested against the cap** (s 13B):
   - for a purchase, the greater of the price and the unencumbered value: a $590,000 price with a $605,000 value is over the purchaser's cap;
   - for a building contract, the build price plus the land at the greater of what was paid and its value: $330,000 plus land worth $420,000 is $750,000, exactly at the builder's cap, and land worth $421,000 puts it over;
   - for an owner build, the home's value at completion plus the land: the owner builder's own costs, which are its "consideration" (s 13(7)(c)), affect only the s 18(4) limit on the amount, not the cap.

   Asserted. Section 13A(3)(b) tests a building contract's total value "as at" completion, but s 13B(1)(b)(ii) values the land "at the commencement date". Read together, the build price is the one at completion. This is a comment, not an assertion.
5. **For joint applicants, one is enough for all, without asking the Chief Commissioner.** One citizen or permanent resident among joint applicants exempts the rest (s 9(2)). One applicant who meets the residence requirement exempts the rest (s 12(6)). Both work automatically, unlike WA's discretionary s 13(6). They need joint applicants: a citizen spouse who is not applying does not help, and neither does a partner who lives there without applying. With three applicants, one citizen is enough. Asserted.
6. **A permanent resident is a permanent visa holder, or a New Zealand citizen with a special category visa** (s 3). There is no intention-to-reside test, unlike WA's s 7B. Asserted.
7. **The s 15(2)(e) proviso changes nothing.** A small interest holder (5% or less) need not apply, "but only if, in a case where there is more than one small interest holder", their total is 5% or less. With one small interest holder, the total is that holder's own share, which is 5% or less anyway. So the test is always: the total of all small interest holders is 5% or less. Two parents with 3% each must join the application; two with 2% each need not. Asserted.
8. **A spouse's past counts against the applicant, even when the spouse is not applying** (ss 10, 11: "the applicant or the applicant's spouse").
   - A husband's unrepaid 2010 grant bars his wife, unless the Chief Commissioner is satisfied they had separated for good (s 6(2)).
   - A de facto partner counts too. This Act sets no minimum period of living together (unlike WA's 2 years). The definition is borrowed from the Interpretation Act 1987 s 21C, which is not deposited.

   Asserted.
9. **"Never owned a home" is narrower than it sounds** (s 11). Any relevant interest in residential property held before 1 July 2000 bars the applicant, whether or not they lived there. After that, an interest bars only if the person also lived there for 6 continuous months before the commencement date (s 11(3)). An investment property never lived in does not bar. Asserted.
10. **An earlier grant paid back with any s 45 penalty no longer bars** (s 10(2)). That holds even where it is uncertain whether the other State's law is a "corresponding law": once the grant is repaid, the answer is the same either way. An unrepaid grant of uncertain standing is not covered. Asserted.
11. **When does "the period allowed for compliance" with the residence requirement end?** Section 20(3) runs the 14 days from it, but the Act does not say. READING:
    - if the applicant did not move in within the time allowed, it ends with that time (12 months after completion, or a later start approved);
    - if they moved in but left too soon, it ends 12 months after they moved in, when the required stay would have ended.

    So a buyer who completed on 15 August 2025 and moved in on 1 September 2025 must give notice and repay by 15 September 2026. One who never moved in must do so by 29 August 2026. Asserted. Revenue NSW practice should settle this reading.
12. **Joint liability under s 21(3) is stated only for conditions the Chief Commissioner imposes.** By its words, s 21(3) covers "a requirement under subsection (2)", a condition imposed by the Chief Commissioner. The encoding applies it to the statutory s 20 conditions as well. Otherwise each joint applicant would owe the whole grant back. Each joint applicant is bound, and a notice or repayment by any one of them counts for all. In the trace, each side of the `ROR` breaches. Asserted with traces. Section 46(2A) separately makes the amount joint and several.
13. **Each 14-day clock starts on a different day:**
    - s 20(2): the end of 12 months from the commencement date, or the longer period allowed. A contract of 1 March 2024 still not completed must be notified and repaid by 15 March 2025; with a period allowed to 30 June 2025, by 14 July 2025;
    - s 20(2A): the day the applicant becomes aware the total value is over the cap;
    - s 20(3): the end of the period allowed for compliance (finding 11).

    Failing is an offence, with a maximum of 50 penalty units (s 20(4)). It also lets the Chief Commissioner impose a penalty up to the amount to be repaid (s 45(2)(c)(ii)), so up to twice the grant can be recovered. Without a ground to require repayment there can be no penalty: it cannot exceed the amount to be repaid, which is then nothing. Asserted.
14. **An off-the-plan buyer can apply on the day the contract is made, but is paid on completion.** The application period runs from the commencement date to 12 months after completion (s 14(5)). The grant is payable only once the transaction is completed, unless the Chief Commissioner authorises payment before completion (ss 7(3), 20(1)(a)). An application the day before the contract, or the day after the 12 months, needs the Chief Commissioner's leave (s 14(6)). Asserted.
15. **Section 8A does not say on what day the applicant must be 18.** READING: the day of application. A 17-year-old with the Chief Commissioner's exemption qualifies. There is no upper age. Asserted.
16. **Section 43A, the ADF home buyer's grant, is in force on the face of the deposit.** Nothing repeals it or gives it a closing date. It is a separate grant for permanent ADF members enrolled to vote in NSW, with no residence requirement. It is payable only if a first home owner grant is not (s 43A(4)), so leaving it out changes no answer here. Not asserted.
17. **The start of the 2012 transitional period is not in the deposit.** Section 18(5) fixes it by the day the Bill for the 2012 Budget Measures Act "was introduced in the Legislative Assembly", so it is asked as a fact. Not asserted.
18. **The deposited s 44(2) has no maximum penalty.** Section 44(1) (false statements to an authorised officer) carries 100 penalty units. Subsection (2) (false statements in an application) has no penalty line in the deposited text. This may be a gap in the corpus copy; check the official text. Section 44 is out of scope. Not asserted.
19. **READING: all interested persons joining (s 15(1)) is treated as a condition of payability.** Section 7 does not list it, but an application without every interested person is not one the Act allows. Asserted (finding 7's cases go through `Is the grant payable on my application`).

## Links to other encodings

Cross-folder IMPORT does not work, so these are links only.

- **Duties Act 1997 (NSW)**, `../../../duties-act-1997/`: the First Home Buyers Assistance Scheme (Part 8, Division 1) asks about the same buyer, the same Chief Commissioner, and a parallel 12-month residence and repayment duty. The deposited Duties Act borrows this Act's s 4A "new home" in s 74(5), s 78AA(7) and s 104ZJA. Its s 85(1)(b) excludes from the New Home Grant Scheme anyone eligible for a grant under this Act. Its encoding was not yet in Commons when this was written.
- **Income Tax Assessment Act 1997 (Cth)**, `../../../../income-tax-assessment-act-1997/`: whether the grant is assessable income. **Unverified** (from general knowledge, not from the texts).
- **Social Security Act 1991 (Cth)**, `../../../../social-security-act-1991/`: whether the grant, or money set aside for a home, counts in the assets test. **Unverified** (from general knowledge, not from the texts).
- **First Home Owner Grant Act 2000 (WA)**, `../../../../wa/first-home-owner-grant-act-2000/encodings/baseline-2026-10/`: the WA grant, for comparison (findings 5, 6 and 8).

## What would need doing before this is worth relying on

- Replace the corpus text with the current official text from legislation.nsw.gov.au, and recheck every amount, cap and date. The text dates from 2023-09-04.
- Find out whether any regulation under s 13A(4) sets a cap, and deposit it.
- Deposit the Interpretation Act 1987 (s 21C, de facto partner; the rules for reckoning time) and the value of a penalty unit.
- Settle the readings against Revenue NSW guidance and decisions, none of which were consulted:
  - s 4A(3)(c) (finding 3);
  - the end of the residence compliance period (finding 11);
  - s 21(3) and the s 20 conditions (finding 12);
  - the age day (finding 15);
  - s 15 as a condition of payment (finding 19).
- Encode, if historical claims matter: Schedule 1's transitional caps and the pre-October 2012 Part 2, s 43A, ss 6A-6D and 13(6), the objection and review deadlines (Part 2B), and the s 46 charge on the home.
- Run an independent test pass.
