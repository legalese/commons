# First Home Owner Grant and Other Home Owner Grants Act 2000 (Qld): baseline encoding for the first home buyer

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18.
There is no REFUSE in it. A purchase or build that commenced before 20 November 2023, or an amount that only a version of the Act not deposited could give, answers `not covered`, and tests assert it.
It was checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

It is written in two layers, after the pattern of `subjects/us/food-and-nutrition-act-of-2008/encodings/baseline-2026-10/`:

- **`fhog-core.l4`**, the seat-neutral core. It uses the Act's own actors and terms ("the applicant", "the applicant's spouse", "the commissioner", "an interested person"). The definitions, the criteria, the eligible transaction, the amount and the deadlines are functions. Where the text says "must" or sets a period, there is a regulative rule (`DEONTIC`): six in all.
- **`fhog-seat.l4`**, the first home buyer's seat. It asks 22 questions, each with `@export` and a `@desc` on every input, grouped under `§§` headings in the Act's order. It builds the core's records from plain answers and restates no rule. The transaction questions share the same twenty inputs in the same order, and the applicant questions the same twenty-four, so the form can ask each once.

No earlier encoding of this Act existed to keep. Queensland has no requirement ledger, so no ledger line is closed. No scenario life raised the Act: every case is the encoder's, hypothetical.

## Edition

- **The Act.** First Home Owner Grant and Other Home Owner Grants Act 2000 (act-2000-014), the version in force from **1 July 2026**, current on 20 October 2026, as deposited at `../../registers/source-bundle/act-2000-014.txt` (retrieved 2026-10-20; unofficial HTML conversion, not the authorised PDF).
- **The Regulation.** First Home Owner Grant and Other Home Owner Grants Regulation 2021 (sl-2021-0018), the version in force from 19 March 2021, as deposited at `../../../first-home-owner-grant-and-other-home-owner-grants-regulation-2021/registers/source-bundle/sl-2021-0018.txt` (retrieved 2026-10-20). Four of its sections are used:
  - r 2, the declared relevant interests (Act s 8(1)(i));
  - r 3, the persons who are not interested persons (Act s 17(2));
  - r 4, the interest rate on an instalment arrangement (Act s 48(5));
  - r 6, the prescribed completion requirement (a final inspection certificate under the Building Act 1975).

  Regulation r 5 (methods of payment) is not encoded.
- **Licence.** Both texts are the State of Queensland's, under CC BY 4.0: "Based on content from the Queensland Legislation website at 20 October 2026. For the latest information on Queensland Government legislation please go to https://www.legislation.qld.gov.au." The Act's `SOURCE-LICENSE.md` is copied here; the Regulation's is at `../../../first-home-owner-grant-and-other-home-owner-grants-regulation-2021/SOURCE-LICENSE.md`.
- **Inputs the deposit does not supply:** the value of a Queensland penalty unit (Penalties and Sentences Act 1992), and the Reserve Bank's 90-day bank bill yield for May of the previous financial year (Regulation r 4(3)). Both are inputs.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `fhog-core.l4`, `fhog-seat.l4` | `fhog-cases-applicant.l4` | 160 written, 160 satisfied |

In addition, 10 `#TRACE`s carry an `-- expect:` line: five breaches by the applicant and five obligations still pending (or, for the late objection, nothing owed). Each was read and matches its expectation.

`l4 run` on all three files: 0 errors, 0 warnings (2026-10-24). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. As a control, a copy of the case file with one expected value altered (the $24,000 owner build, to $23,000) was run outside the repository. The runner reported the failed assertion.

Every expected value was written by hand from the text, with the working in the comment above the assertion. Day counts were worked on the calendar: 20 March 2028 to 20 March 2029 is 365 days; 1 April to 1 October 2028 is 183.

## Seat

**The first home buyer**: the applicant for a first home owner grant (s 16), who is, or on completion will be, an owner of the home (ss 7, 17). They ask:

- "Is the home I am buying or building an eligible transaction, under the $750,000 cap?"
- "Am I eligible?"
- "How much will I get?"
- "By when must I apply and move in, and for how long must I live there?"
- "What happens if I do not, and must I repay with a penalty?"
- "How do I object?"

Most of Parts 3 to 5 address the Commissioner of State Revenue: authorising payment (ss 19, 22), imposing conditions (s 23), requiring repayment (s 47), registering a charge (s 49), deciding objections (ss 57, 58). Each is encoded as what it means for the buyer: what must be repaid, by when, how large a penalty can be, whether the home is charged, and how long they have to object or seek review. In the core these are regulative rules with the applicant and the commissioner as parties.

**No second seat.** The Act puts its duties on the applicant and its powers on the commissioner, an official. A third party to whom the grant was paid may be required to repay (s 47(4)), but that is too slight to carry a seat.

How each 2026-10-18 default was applied:

- **The Act alone, with the instrument that sets its numbers.** Followed. The Regulation is brought in for rr 2, 3, 4 and 6. The Act's own Part 5 objection rules apply, not the Taxation Administration Act 2001's.
- **The actors the text names.** Followed: the applicant (and joint applicants), the applicant's spouse, the commissioner, interested persons, and the housing chief executive (r 3).
- **Judgments left to someone else are answered conditionally, as inputs.** Followed. Each of these is a fact the commissioner has decided:
  - a scheme (s 5(4) and s 25EA(2)), and satisfaction to the contrary of the presumptions (s 5(5), s 25EA(3));
  - the age exemption (s 11(2));
  - the residence approvals and exemptions (s 15(2), (3), (4));
  - the s 8(1)(g) opinion and the s 8(1)(h) satisfaction;
  - the s 9(3) and (5) satisfactions about couples living apart;
  - allowing an application outside the period (s 16(4));
  - a disqualifying arrangement (s 69A);
  - extending the time to object (s 56(4)).
- **The Act's definitions worked out; borrowed terms asked as facts.** Followed, with one departure.
  - Worked out: home and new home, including a substantially renovated home (s 6); relevant interest (s 8, r 2); home owner (s 7); spouse and de facto partner (s 9); eligible transaction and the cap totals (s 5); criteria 1 to 4; the residence requirements (s 15 and the schedule); completed (schedule, r 6); interested person (s 17, r 3); the application period (s 16); the s 22(3) relevant date.
  - Asked as facts: the GST Act's taxable supply of new residential premises; citizenship and visas (Commonwealth Acts); a relevant interest under another State's corresponding law; the unencumbered value (s 8A is a valuation rule, so the value is stated on its basis).
  - **Departure.** In the criteria questions, an earlier holding is asked in plain words ("owned, or held another listed interest in, land in Australia with a residence on it"). It is not worked out through s 8 for each earlier holding. The s 8 question is there, for one interest at a time.
- **One case is the text's natural unit.** Followed: one application for one eligible transaction (s 10(3)). A joint applicant asks the criteria question from their own seat; the payable question takes their answer as one input.
- **The Act's own terms, each with a plain gloss.** Followed. The comments quote the statutory words.
- **Operative sections in; machinery out.** Followed (see Scope).

## Scope

**In:**

- Part 2 Division 2: s 4; s 5, with the $750,000 caps of s 5(6) to (9) and the s 5(4), (5) scheme presumption as facts; s 6; s 7; s 8 with Regulation r 2; s 8A, as a stated value; s 9.
- Part 3: s 10; ss 11 to 15 (criteria 1 to 5); s 16; s 17 with Regulation r 3; s 20; ss 25EA and 25EB; s 22 (payment in anticipation, and the 14-day duty, as a regulative rule); s 22A (as a regulative rule); s 23 (as a regulative rule). Of s 21, only the payee is noted.
- Part 4 Division 3: s 47 (as a regulative rule, with the penalty caps); s 48(2) to (5) with Regulation r 4; s 49 (the charge, with the release in s 49(4) as a regulative rule). Regulation r 6 (completion).
- Part 5: ss 56 to 59 (objection and review deadlines, as a regulative rule).
- The schedule: commencement date, completed, consideration, comprehensive home building contract, owner builder, permanent resident, residence requirements, residential property.

**Out:**

- Parts 3A and 3B (the regional home building boost and home builder grants): their eligibility is set by administrative directions, which are not deposited.
- Part 3 Divisions 5 and 6 (the 2008 to 2011 and 2016 to 2018 amounts).
- s 18 (guardians), s 19 except as noted, s 24 (death of an applicant), s 25 (notice of decision) except as the start of the objection period.
- Part 4 Divisions 1, 2 and 4 (authorised officers, investigations, offences of false information, legal proceedings), ss 49A to 51A (garnishees, writing off, penalty amounts as an alternative to prosecution, court-ordered repayment).
- s 69A beyond the fact that the commissioner has acted under it; s 69B (valuations).
- Part 6 machinery, and the transitional Parts 7 to 16, except that s 91 (and ss 79 to 81) mark which transactions the deposit can answer.

## Read with the Commonwealth encodings

The stable `l4` cannot IMPORT across encoding folders, so the links are recorded here and not in code.

- **Social security.** The Social Security Act 1991 (`../../../../social-security-act-1991/`) does not count the grant as income. Its s 8(8)(ha), at line 791 of the deposit `C2004A04121.txt`, excludes from income "a payment made by a State or Territory for the purpose of assisting the person to purchase or build his or her own home". Once bought, the home is disregarded in the assets test as the person's principal home (s 1118(1)(a), (b)). The Commonwealth baselines do not yet encode s 8(8)(ha).
- **Income tax.** The deposited Income Tax Assessment Act 1997 (`../../../../income-tax-assessment-act-1997/`) does not mention a State first home owner grant. Whether it is ordinary income (s 6-5) is not answered by its text, and nothing is stated there to link. The Commonwealth's own first home measure in that Act, the first home super saver scheme (Division 313), is separate from this grant and does not affect it.
- **The home.** The Queensland README notes that one fact, "this is my home", also drives the land tax home exemption, the transfer duty home and first home concessions (Duties Act 2001, Chapter 2 Part 9), and the CGT main residence exemption. This Act's s 15 residence requirement is its own test: "principal place of residence" for 6 continuous months starting within 1 year after completion. An encoding of those other laws should not assume they use the same test (the README says the definitions differ).

## What the Act turns out to say

1. **The grant is $30,000 for any new home contracted or started since 20 November 2023.** Section 20(1)(b)(i), as in force from 1 July 2026, gives "$30,000" for a new home eligible transaction. For contracts made and builds started between 20 November 2023 and 30 June 2026, s 25EB gave the same $30,000 "Despite section 20". The grant is the lesser of that and the consideration:
   - Mia's apartment, Sam and Priya's build, Jack's owner build and Lena's townhouse each get $30,000;
   - a $24,000 owner build gets $24,000.

   Asserted.
2. **Section 91 leaves the deposit silent on the past.** For an eligible transaction whose commencement date is before 1 July 2026, the Act applies "as if this Act had not been amended by" Part 3 of the Revenue (Cost of Living Relief Locked-in Law) and Other Legislation Amendment Act 2026. Neither that Act nor the version before it is deposited. That s 20 now reads $30,000, the s 25EB figure, suggests Part 3 raised s 20(1)(b)(i) to it, but that is an inference. The encoding therefore:
   - applies Division 7 as deposited to transactions from 20 November 2023 to 30 June 2026, together with ss 5 to 17 (a reading);
   - answers `not covered` for a transaction in that window that is not a relevant eligible transaction (a s 25EA(2) scheme, found or presumed);
   - answers `not covered` for anything that commenced before 20 November 2023.

   Asserted.
3. **Established homes have been out since 11 October 2012.** Section 5(2) admits a home "other than a new home" only for a contract made, or building begun, "before 11 October 2012". The s 20(1)(b)(ii) amount of $7,000 can reach only those transactions, and older versions govern all of them (ss 79 to 81). Tom's 30-year-old house in Cairns is not an eligible transaction. The $7,000 is encoded in the core and asserted there ($5,000 gives $5,000; $200,000 gives $7,000). A 2010 established-home purchase is eligible under the core's s 5 and `not covered` at the seat. Asserted.
4. **A developer's renovation can make an old house new.** Under s 6(3), a home is "substantially renovated" (and so new, s 6(2)(b)) if three things hold:
   - it is bought under a contract;
   - the sale is "a taxable supply as a sale of new residential premises" under the GST Act s 40-75(1)(b);
   - as renovated, it has not been occupied or sold as a residence.

   Tom's house so renovated attracts $30,000. An owner builder's own renovation cannot qualify, because s 6(3)(a) needs a contract for the purchase. Asserted.
5. **Two caps, and value counts as well as price.** The text sets two tests:
   - s 5(6) bars a transaction whose consideration is "$750,000 or more", so exactly $750,000 is out;
   - s 5(7) to (9) add values: for a purchase, the home's unencumbered value plus the land's; for a build, the price or cost plus the land's value at the commencement date.

   So:
   - a $700,000 purchase of a home worth $450,000 on land worth $310,000 is out ($760,000);
   - Sam and Priya's $480,000 building contract is out on land worth $300,000 ($780,000) and in on land worth $260,000 ($740,000).

   Asserted.
6. **For builds and off-the-plan purchases the cap is tested again on completion.** Section 22A applies where the grant was paid before completion of a building contract, an owner build or a s 5(3)(b) purchase, and the completed home's value (or the final consideration), with the land's value at the commencement date, reaches $750,000. The applicant must, "within 28 days after completion", give written notice and repay (40 penalty units). If Mia's apartment is valued at $560,000 on completion, she must notify and repay by 17 April 2028. A home already standing when the contract was made is not a relevant transaction. Asserted.
7. **A partner's past counts only if the Act calls them a spouse.** Section 9 sets three rules:
   - a de facto partner counts only after "at least 2 years" of living together as a couple;
   - a married or civil partner counts unless the couple live apart and the commissioner is satisfied neither intends to resume;
   - a de facto partner living apart counts if the commissioner is satisfied they intend to resume.

   After 3 years together, Priya's former Sydney unit bars Sam (s 14(4)). After 1 year it does not bar him, but Priya must still join the application (s 17), and she fails criterion 4 herself. So the grant is not payable on their application either way. Asserted.
8. **"Never owned a home" means two things, either side of 1 July 2000.** Before that date, any relevant interest in residential property counts (s 14(1)), lived in or not. From that date, only property "used ... as the residence of the applicant or the applicant's spouse" counts (s 14(4)). An investment flat held in 1998 bars the buyer; one bought in 2015 and never lived in does not. An instalment purchase ended within a year without the title is excused (s 14(2)). So is a home whose earlier grant was repaid for failing criterion 5 (s 14(5), with s 13(2) for the earlier grant). Asserted.
9. **Section 15(4) is narrower than it looks.** It lets the commissioner exempt a joint applicant "from the residence requirement under subsection (3)", which is the requirement to start within 1 year. Read literally, a joint applicant so exempted must still live there for 6 months, at any time. A full exemption is under s 15(2)(b). The encoding follows the words: the seat answers "no deadline to move in, but stay for 6 months". The deposit's schedule entry "residence requirement ..." (line 1099 of the deposit) is truncated in conversion, so whatever the singular term was defined as cannot be checked here. Asserted.
10. **Residence means 6 continuous months as the principal place of residence, starting within 1 year after completion.** Mia moves in on 1 April 2028. She must still live there on 30 September 2028 and may leave on 1 October. A period starting on 31 August ends on 28 February. The commissioner may approve a shorter period, a longer time to start, or an exemption, and may do so even after the period has ended (s 15(5)). Each is a fact. READING: an occupation that began before completion is treated as starting in time. Asserted.
11. **Paid in anticipation but not living there: 14 days from the "relevant date".** Section 22(3) makes the relevant date the earlier of "the end of the period allowed for compliance" and the day "it first becomes apparent" the requirements will not be met. The Act does not say when the period allowed for compliance ends. It is read as the last day to move in plus the required months. Mia moves out on 15 September 2028, so she must notify and repay by 29 September 2028. The regulative trace agrees: she moved out on day 179, and the deadline is day 193. Failing this "without reasonable excuse" carries 40 penalty units (s 22(5)). Asserted.
12. **What can be added to a repayment.** Section 47 allows two penalties:
    - (2): a penalty "of not more than the error amount" where it was paid because of a false or misleading document or statement;
    - (3): another such penalty for failing to make a repayment required.

    Read as separate penalties, together they can reach twice the grant. Further:
    - for a failure to repay under a condition of the grant, the cap is read as the amount to be repaid;
    - the Act sets no period for a s 47(1) repayment, so the notice's period is an input;
    - the liability is joint and several (s 48(2));
    - an instalment arrangement may charge the May bank bill yield, rounded to 2 places, plus 8% (r 4);
    - the debt is "a first charge" on the applicant's interest in the land, with "priority over all other encumbrances" (s 49(2), (2A)), so it ranks ahead of the mortgage.

    Asserted.
13. **The offences are priced in penalty units the deposit does not value.** Breaching ss 22(2), 22A(2) or a grant condition (s 23(4)) carries 40 penalty units. At a hypothetical $170 a unit that is $6,800. Asserted.
14. **Objection within 60 days, review within 60 more.** An objection must be lodged "within 60 days after the objector receives notice of the decision", stating its grounds "fully and in detail" (s 56(2), (3)). The time may be extended for a reasonable excuse (s 56(4)). QCAT review must be sought within 60 days of receiving the objection decision (s 59). READING: the day of receipt is left out, since the Acts Interpretation Act 1954 is not deposited, so notice received on 3 February 2028 gives until 3 April 2028. Two further points:
    - The Act sets no time for the commissioner to decide an objection (s 58), so that trace stays pending.
    - These are the Act's own objection rules (Part 5); the Taxation Administration Act 2001 objection rules do not apply to the grant.

    Asserted.
15. **The scheme rules apply to contracts only.** Section 5(4) says "a contract is not an eligible transaction" if part of a scheme. An owner build is not a contract, so a scheme finding does not exclude it under s 5(4). The commissioner can still act under s 69A. Two other points:
    - The s 5(5) presumption needs an option or right granted before 1 July 2000. For a contract made today it is practically spent, but it is in the text and asserted.
    - The seat asks one "satisfied to the contrary" question for both the s 5(5) and s 25EA(3) presumptions, a simplification.

    Asserted.
16. **Every future owner must apply, with two exceptions in the Regulation.** Section 17 requires "All interested persons" to be applicants. Regulation r 3 excludes two kinds of owner:
    - the holder of another relevant interest where the applicant's interest is one r 2(1) declares, such as parents who own the land under a "granny flat" right they gave;
    - the housing chief executive under the Pathways Shared Equity Loan scheme, holding not more than 40%, with the department financing and the applicant a tenant.

    A father who takes half the title and does not apply makes the grant not payable. Asserted.
17. **A build is completed only when the final inspection certificate issues.** Regulation r 6, read with the schedule's "completed", requires "a final inspection certificate under the Building Act 1975" before a building contract or owner build is complete. Completion starts the 1-year application and move-in clocks. Asserted.
18. **The application period runs from the commencement date to 1 year after completion.** The commissioner may allow an application before or after it (s 16(3), (4)). READING: "1 year after" 29 February is taken as 28 February. Asserted.

## Before relying on it

- **Deposit the version of the Act in force on 30 June 2026, and the Revenue (Cost of Living Relief Locked-in Law) and Other Legislation Amendment Act 2026.** Section 91 makes the pre-amendment Act govern every transaction that commenced before 1 July 2026 (findings 1 and 2). With both deposited, the window from 20 November 2023 could be confirmed and earlier dates covered.
- An independent test pass, and a check against Queensland Revenue Office guidance and decisions (none were consulted).
- Deposit the Acts Interpretation Act 1954 (Qld) to settle the counting of days, months and years (findings 10, 14, 18), and its definition of "State", which decides whether "another State" in s 14(1)(b) includes the Territories.
- The value of a penalty unit and the May bank bill yield, if fixed figures are wanted.
- Settle the reading of s 15(4) (finding 9) and of "the period allowed for compliance" in s 22(3) (finding 11).
- Work earlier holdings out through s 8 for each one, rather than asking them in plain words (the departure noted above).
- Encode ss 18, 24 and 25, ss 49A to 51A, and s 69A's factors, and Parts 3A and 3B if their directions are deposited.
- Encode the Social Security Act s 8(8)(ha) exclusion in the Commonwealth baseline so that the link above is in code there.
