# Land Tax Act 2010 (Qld): baseline encoding for the individual land owner

## Method

**Baseline.** Written straight from the deposited texts with the `writing-l4-rules` skill, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18.
There is no REFUSE in it. A trustee or company owner (for the rate, the home exemption and the primary production exemption), or a home spread over more than one parcel, answers an explicit `not covered` value, and the tests assert it.
It was checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

It is written in two layers, on the pattern of `subjects/us/food-and-nutrition-act-of-2008/encodings/baseline-2026-10/`:

- **`qlt-core.l4`**, the seat-neutral core. It uses the Acts' own actors and terms ("the owner", "the person", "the taxpayer", "the commissioner", "taxable land", "exempt land", "the 6 month residency period"). Computations (taxable value, aggregation, the rate scales, instalment amounts, interest, penalty tax) are functions. Where the text says "must" or sets a deadline there is a regulative rule (`DEONTIC`): 11 in all, for ss 34, 44, 44A, 71–74, 77 and 77A and TAA ss 28, 30 and 63–69. Beside the rules, core functions turn each rule's clock into a calendar last day (ss 34, 44, 44A, 71(4), 74(2), 74(3), 77, 77A; Regulation s 4(a); TAA ss 28, 30(2), 65, 69), and give the TAA s 69 appeal position on a given day, from the same day counts and conditions the rules use.
- **`qlt-seat.l4`**, the individual land owner's seat. It asks 41 questions, each with `@export` and a `@desc` on every input, grouped under `§§` headings in the Act's order. It builds the core's records from plain answers and restates no rule: every test, deadline and date it gives is a core function.
- **`qlt-cases-owner.l4`**, the worked cases.

No earlier encoding of this Act existed to keep. No requirement ledger covers Queensland, so no ledger line is closed.

## Edition

- **The Act.** Land Tax Act 2010 (act-2010-015), the version in force from 2025-08-01, current on the retrieval date, deposited at `../../registers/source-bundle/act-2010-015.txt` (retrieved 2026-10-20, from the HTML view; not the authorised PDF).
- **The Regulation.** Land Tax Regulation 2021 (sl-2021-0019), in force from 2023-07-01, deposited at `../../../land-tax-regulation-2021/registers/source-bundle/sl-2021-0019.txt` (retrieved 2026-10-20). Brought in: s 2 (primary production activities, for Act s 53) and s 4 (the instalment election period and document, for Act s 72).
- **The administration Act.** Taxation Administration Act 2001 (act-2001-072), in force from 2025-02-28, deposited at `../../../taxation-administration-act-2001/registers/source-bundle/act-2001-072.txt` (retrieved 2026-10-20). Land tax is a revenue law under its s 6(4), and Land Tax Act s 4 says the two Acts are read together. Brought in: ss 28, 30, 54, 58, 63–65, 67–69, as they apply to land tax.
- **Inputs, not deposited:**
  - the s 18(2) averaging factor (its formula was lost in the deposited text: finding 1);
  - the Land Valuation Act values (the Valuer-General's valuations);
  - the "prescribed rate" of interest and the prescribed weekday for late payment interest (TAA s 54; Taxation Administration Regulation 2022, not deposited);
  - the value of a penalty unit, for the TAA s 121 offence named in the breach reasons.

The three texts are CC BY 4.0 (State of Queensland); `SOURCE-LICENSE.md` here is a copy of the Act's. The Regulation and the TAA carry the same terms in their own subjects' `SOURCE-LICENSE.md`. Based on content from the Queensland Legislation website at 20 October 2026.

Conventions: a financial year is named by the calendar year it starts (2026 for 2026-27); a regulative rule's clock counts days from the event its comment names; money is in dollars.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `qlt-core.l4`, `qlt-seat.l4` | `qlt-cases-owner.l4` | 210 written, 210 satisfied |

In addition, 11 `#TRACE`s carry an `-- expect:` line: 9 end in a breach, 2 with something still owed (the Commissioner's decision on an objection; the taxpayer's appeal window). Each was read and matches its expectation, including the party named in each breach (the owner for s 77, the person for ss 44 and 44A, the taxpayer for s 34 and the TAA and instalment rules).

`l4 run qlt-core.l4` and `l4 run qlt-seat.l4`: "Checking succeeded", no diagnostics. `l4 run qlt-cases-owner.l4`: 210 assertions satisfied, 0 errors, 0 warnings (2026-10-24, after the corrections below). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read.

As a control, a copy with two expected values altered ($7,800 to $7,801; $833.33 to $833.34) was run: the runner reported exactly those two failures. After the corrections, a second control altered two of the new expected values (the trustee-absentee farm to "not exempt"; the s 23(3) request to "exempt"): again exactly those two failed.

Every expected value was worked by hand from the texts, with the arithmetic in the comment above the assertion. The stable `l4` cannot compare a breached or pending trace with `EQUALS`, so those are `#TRACE`d with an `-- expect:` line, as the brief says.

## Seat

**The individual land owner**: the home owner, the owner of other land (an investor), or an absentee owner, owning alone or as a co-owner. Three situational groups put the same person in other shoes: the executor or administrator of a deceased owner (s 23), the buyer of land that may carry unpaid land tax (ss 59, 60), and the owner working abroad (s 34). They ask:

- "Do I owe land tax this financial year, and how much?"
- "Is my home exempt, wholly or partly? What if I rent out a room or work from home?"
- "What if I am moving house, renovating or in care?"
- "How much do I owe on my investment land, and do I owe more as an absentee?"
- "When must I tell the Commissioner my home is no longer exempt?"
- "Can I pay by instalments?"
- "How do I object?"

The Commissioner assesses, decides and reassesses. Those powers appear only as what they mean for the owner: whether the owner is liable, what is exempt, what the owner pays, by when the owner must pay, notify, object or appeal. The Commissioner is a party in one regulative rule (TAA ss 67, 68: the objection must be decided and notice given), because that is a duty the owner is owed. No second seat was added: the text puts no duties on another private party that this scope reaches (the mortgagee's s 62 and the home unit company's s 80 are out of scope).

How each 2026-10-18 default was applied:

- **The Act alone, with the instruments that set its numbers or dates.** Followed. The Regulation sets the instalment period and the primary production activities, and is brought in. The TAA sets payment, interest, penalty tax and objections for land tax as a revenue law, and is brought in as far as the scope needs. The averaging factor, valuations and interest rate are inputs.
- **The actors the text names.** Followed: "the owner" (ss 77(2), 77A(2): "The owner of the land must"), "the person" (ss 44(2), 44A(4): "The person must"), "the taxpayer" (s 34(2): "The taxpayer must"; ss 71–74; TAA), and "the commissioner". The four parties are kept apart in the regulative rules as the text names them, each rule naming the actor of its own text, although for this seat the owner, the person and the taxpayer are one individual. (Before the 2026-10-24 corrections the s 34, s 44 and s 44A rules said "the owner"; finding 23.)
- **A judgment handed to someone else is answered conditionally.** Followed. Five answers carry the Commissioner's judgment instead of guessing it:
  - principal place of residence (s 36(1)(c));
  - temporarily living elsewhere because of the works (s 38(a));
  - whether another use is substantial (s 39(2));
  - the employee's absence under s 31(3)(b);
  - whether the person satisfies the Commissioner of ordinary residence (s 31(2)).

  The s 36(2) and s 39(3) factors are facts, and two questions list which of them point the Commissioner's way. The s 40(1)(c) "the commissioner is satisfied the land is used only for" those purposes is read as a fact the owner can state.
- **The Act's own definitions worked out; borrowed terms asked as facts.** Followed.
  - Worked out from facts: owner (ss 10, 11, 13, 14), taxable land, taxable value and averaged value, co-owner shares, aggregation, absentee, used as a home, allowable letting, permitted number, family letting, excluded work, non-exempt purpose, the s 42A and 42B conditions, the s 23 owner and exemption, the s 44A relevant matters, outstanding land tax, the interest start date.
  - Asked as facts: "ordinarily resides", principal place of residence (for the owner's claim), "business of primary production", residential care service (Aged Care Act), "member of the family" (glossed in the `@desc` from Schedule 4), market rent, the Land Valuation Act value.
- **One case is the text's natural unit.** Followed. For the exemptions: one parcel, owned by one individual alone or as a co-owner, at one liability date. For the amount: one taxpayer's total taxable value (s 19). For payment: one assessment notice.
- **The Act's own terms, each with a plain gloss.** Followed. Comments quote the statutory words; the `@desc`s gloss them.
- **Operative sections in; machinery out.** Followed (see Scope).

**Departures:**

- Dates in the seat are calendar dates; the regulative rules count days from a stated event, so the seat converts dates to day counts and back.
- The s 77 and s 77A deadline "within 1 month after the start of the next financial year" is read as 31 July (day 30 counting 1 July as day 0). The Acts Interpretation Act 1954, which governs how periods are counted, is not deposited; it might move the last day to 1 August. The earlier day is the safe one for the owner.
- s 44(3) "within 28 days after the day the liability ... arises" counts from 30 June (the day of the midnight at which the liability arises): 28 July.
- The instalment chain counts each instalment's period from the previous instalment's direct debit. Under direct debit that is its stated date (45, 90, 150 days); an instalment paid early would start the next period early. The s 74 consequence is counted from when the missed instalment is noticed in the trace, which can be a day later than its stated date.
- s 74(2)(b), "the date on which the failure to pay the instalment happens", is read as the missed instalment's own stated date: the direct debit (s 71(3)(b)) is due that day and is not made. So where (b) is the later date the seat says to pay "no later than" that same date (16 October 2026 for a first instalment due then). The other reading, that the failure happens only when that day ends, would make the last day the day after (17 October 2026). The earlier day is the safe one for the taxpayer; the s 74(3) interest start date is the same under both readings, because it runs from the (a) date.

## Scope

**In:**

- **Part 2:** ss 6–8 (land tax on taxable land; liability at midnight on 30 June; the owner is liable).
- **Part 3:**
  - s 9 (taxable land);
  - ss 10, 11, 13, 14 (owner; seller and buyer; mortgagee; life estates);
  - ss 16–18 (taxable value: the lesser of the Land Valuation Act value and the averaged value; the averaging factor an input).
- **Part 4:**
  - s 19 (aggregation);
  - s 22(1)–(3) (co-owners, joint tenants equal, s 22(3) no benefit without the owner requirements);
  - s 23 (deceased estates: who is taken to own; the next-30-June exemption, for land taken to be owned by the deceased person under s 23(4)(a)).
- **Part 5:**
  - s 31 (absentee);
  - s 32(1)(a), (c) with Schedule 1 and Schedule 3 Parts 1 and 2, as tables;
  - s 34 (an employee absent longer than 5 years must notify within 28 days).
- **Part 6 Division 1:**
  - ss 35–38 (used as a home: the 6 month residency test, care, demolition or renovation, the principal place of residence, the s 36(2) factors);
  - ss 39–40 (non-exempt purpose; allowable lettings; work from home; the s 39(3) factors with the $30,000 default);
  - ss 41–42 (whole and partial exemption, one parcel);
  - ss 42A, 42B (old home after moving; new home before moving);
  - ss 44, 44A (the owner's notices after a renovation or moving exemption).
- **Part 6 Division 3:** s 53(1), (2)(a), (3) with Regulation s 2 (primary production by an individual who is not an absentee or trustee; an absentee individual is not exempt; a trustee or company owner is not covered, since s 53(2)(b) and (c) may exempt them).
- **Part 7:** ss 59, 60 (debt; first charge; clearance certificates as facts).
- **Part 9:**
  - ss 70–74 with Regulation s 4 (instalments: who may; electing within 35 days; 45, 90 and 150 days; amounts; a missed instalment);
  - ss 76, 77, 77A (when an application is needed; notices that land is no longer exempt or that the exempt part changed);
  - s 81 (no objection on the ground that the valuation is excessive).
- **TAA:**
  - s 28 (advise an under-assessment within 30 days; read with s 58(3));
  - s 30(1)(e), (2) (pay by the date in the notice, at least 30 days out);
  - s 54 (unpaid tax interest: start date, the noncompliance shift, the daily figure; the prescribed rate an input);
  - s 58 (penalty tax: 75%, up to 20% more);
  - ss 63–65 (who may object, on what, within 60 days);
  - ss 67–69 (the decision; appeal or QCAT review within 60 days after paying).

**Out:**

- Companies and trustees: Schedule 2, s 33, s 20, s 22A, s 24, s 41(1)(b)(ii), s 43, and s 53(2)(b)–(d).
- The foreign surcharge for companies and trusts (ss 18B–18G, Schedule 2 Part 2).
- The commissioner's single assessment of 5 or more co-owners (s 22(4)–(7)).
- Home unit companies (ss 25–28, 80) and time-sharing schemes (ss 15, 21).
- Lots in community titles schemes (s 29), subdivided land (ss 30, 45), and the 2011-12 cap (s 18A).
- Charitable land (Part 6 Division 2) and the other Division 3 exemptions (ss 51–58).
- Build-to-rent (Part 6A), windfall tax (Part 7A) and avoidance (Part 8).
- s 75 (reassessment after electing to pay by instalments), s 78 (notice of change of ownership), s 79 (change of address), and Division 2A (basis of liability notices).
- The transitional provisions (Part 10).
- TAA machinery not named above: self and default assessment procedure, refunds, recovery, s 33, s 34 payment arrangements, s 60 remission (mentioned only), investigations, and the s 121 offence (named in the breach reasons, not computed).

## Commonwealth links

Cross-folder IMPORT does not work, so the links are recorded here.

- **The principal home in the social security assets test.** `subjects/au/social-security-act-1991/` (s 11, homeowner, which says "principal home has the meaning given by section 11A"; s 11A, the principal home and its adjacent land, with the absence rules in s 11A(8) and (9); the assets test). Whether a home is someone's "principal home" for a pension or allowance is a different question from "used as the home" in Land Tax Act s 36. The SSA test turns on where the person lives and on its own absence rules in s 11A(8) and (9): for example, a residence continues to be the principal home during a temporary absence of up to 12 months (or a longer determined period), and for 2 years from going into a care situation (s 11A(9)(a), (b)). Land Tax Act s 36 turns on 6 months' continuous residential use ending at 30 June, or the Commissioner's satisfaction, with the s 37 (care, up to 6 years) and s 38 (renovation) extensions. A person in aged care can have their former home exempt from land tax under s 37 and still have it counted, or not, under the SSA's own rules. The encodings keep the two apart; neither answer can stand in for the other.
- **The CGT main residence exemption.** `subjects/au/income-tax-assessment-act-1997/` (Subdivision 118-B, partly encoded in its baseline and naive encodings). The CGT "main residence" test looks at the whole ownership period and has its own rules for moving and absence, in the deposited text:
  - both homes count for up to 6 months when changing main residences (s 118-140);
  - an absence can be treated as continuing residence, for up to 6 years while the dwelling earns income (s 118-145);
  - building a home counts for up to 4 years (s 118-150).

  Land Tax Act ss 42A and 42B give their own one-year bridges for moving, keyed to 30 June. The 6 years of s 37(6) (care) look like s 118-145's 6 years but are a different rule: s 37 allows no income beyond s 37(5). Whether land tax on investment land is deductible is a Commonwealth income tax question, not encoded here.
- **Land tax is a revenue law of the State.** It is administered with the Duties Act 2001 (Qld) under the same TAA. The Commonwealth Taxation Administration Act 1953 plays no part.

## What the Act turns out to say

1. **The s 18(2) averaging formula is missing from the deposit.** The text reads "using the following formula—" and goes straight to "where— T means … V means …". The averaging factor is therefore an input, and a `act-2010-015.formulas.md` sidecar from the authorised PDF is needed. Asserted only as an input.
2. **Taxable value damps a rise and passes a fall.** It is the lesser of this year's valuation and the 3-year average (s 16). Values of $900,000, $800,000 and $700,000 give $800,000. A fall to $600,000 after $800,000 and $700,000 gives $600,000. Asserted.
3. **The $600,000 threshold is a cliff.** $599,999 pays nil; $600,000 pays $500 at once (Schedule 1: "less than $600,000 | nil", then "$500 plus 1.0c for each $1 more than $600,000"). The marginal rate also falls, from 1.65c to 1.25c above $3,000,000, before rising to 1.75c above $5,000,000. The bands join exactly ($37,500 at $3,000,000). Asserted.
4. **Aggregation can turn two tax-free holdings into a taxed one.** Under s 19, the Act's own example of two $500,000 properties is taxed on $1,000,000: $4,500. Each alone would pay nothing. Asserted.
5. **Absentees pay two scales from $350,000.** The general rate is $1,450 at $350,000. The 3c surcharge counts "for each $1 more than $349,999", so it starts with the first dollar of the threshold: at exactly $350,000 the tax is $1,450.03. On $750,000 an absentee pays $20,250.03 against a resident's $2,000. Asserted.
6. **Only citizens and permanent visa holders are excepted by status.** The exceptions are s 31(3)(c) and (d). Schedule 4's "permanent resident", which includes New Zealand special category visa holders, is not used in s 31. So a New Zealand citizen who lives in New Zealand is an absentee for land they own in Queensland. Asserted.
7. **There is no spouse rule.** Each co-owner is tested on their own use (s 22(3); the notes to ss 41 and 42). A parent who owns half a child's home, or a spouse who owns half the home but lives elsewhere, pays on that half: half of $1,300,000 is $650,000, and the tax is $1,000. Western Australia's s 21(1)(b) exempts spouses if one lives there; Queensland's text has no counterpart. Asserted.
8. **Care keeps a home for up to 6 years, but income ends it.** s 37 keeps the land as the owner's home for up to 6 years after the last 6 months there (s 37(6)). Any income from the land in the year bars it (s 37(4)), unless the letting was for no more than 6 months of the year or the rent only covers rates and upkeep (s 37(5)). A full year's market letting loses the exemption. Asserted.
9. **Renting out rooms is safe only within s 40.** One allowable letting is always safe. Two are safe only if one is a family letting and together they take no more than half the floor area. Three never are (s 40(3)). A letting above market rent, or over half the floor area, is not allowable. An employee working from home is safe unless it is "excluded work". Anything else lets the Commissioner decide a non-exempt purpose if satisfied the use is substantial (s 39); then only the home part is exempt (s 42). Asserted.
10. **The s 39(3)(d) income factor is $30,000, and exactly $30,000 does not count.** The deposited Regulation prescribes no amount, so the $30,000 default applies, and the factor is income "more than" $30,000. Asserted.
11. **An absentee farmer gets no primary production exemption** (s 53(2)(a): "an individual, other than a trustee or absentee"), when owning the land as an individual: none of s 53(2)(b)–(d) describes them. A trustee is a different case (finding 21). Asserted.
12. **The instalment election outlasts the earliest due date.** The election period (35 days, Regulation s 4(a)(i)) is longer than the shortest date for payment in full (30 days, TAA s 30(2)). So a taxpayer can elect after the date for payment in full has passed. Asserted (an election on day 34 against a day-31 date).
13. **The three instalments need not add up to the tax.** Each is the tax divided by 3 and rounded to the cent (s 73(2)), and s 71(5) makes the stated amount the amount payable. $2,500 becomes 3 × $833.33 = $2,499.99; $1,000.01 becomes 3 × $333.34 = $1,000.02. Missing the last instalment leaves the unpaid balance under s 74(4): $833.34, a cent more than the instalment. Asserted.
14. **Missing any instalment backdates interest.** s 74(3) starts TAA s 54 interest from the day after the date the tax would have been payable in full, even when the second instalment is missed in November. Asserted: 3 October 2026 for a 2 October date, whichever instalment is missed.
15. **ss 74(3) and 75(4)(c) cite a subsection that is not there.** They refer to "the Administration Act, section 54(2) and (2A)(a)", but the deposited TAA s 54 has no subsection (2A): late payment interest is now in s 54(3). The newer s 63U already says "section 54(2) and (3)". It looks like a cross-reference left behind by a renumbering. Not asserted; the start-date rule is read as applying to s 54(2) and (3).
16. **The s 54(7) example truncates, and accrues daily.** Its $32.87 is 10,000 × 10% × 12 / 365 = 32.8767…, cut to the cent, not rounded. The example accrues late payment interest daily, while s 54(3)(b) has late payment interest on land tax accrue weekly on a prescribed weekday. The encoding gives the daily figure, since the weekday is not deposited. Asserted (the truncation).
17. **s 58 has a gap.** A reassessment back up to the original figure, after a lower earlier reassessment, is within s 58(1)(c) ("more than … an earlier reassessment"). But s 58(2)(c) needs it to be more than the original, and (d) needs it to be less, so no amount is given; it is nil here. Asserted.
18. **A missed s 77 notice can cost far more than the offence.** It is a lodgement requirement (TAA s 121, up to 100 penalty units). The Commissioner may also make a default assessment (TAA s 13(1)(a)(ii)) carrying 75% penalty tax (s 58(2)(a)): $5,850 on $7,800, or $7,020 with the 20% increase. Interest then runs from a start date moved back by the days of noncompliance (s 54(5)(c)(ii); the 13 April example). Asserted.
19. **Valuation complaints go elsewhere, and appeals need payment first.** s 81 bars objecting to land tax on the ground that the valuation is excessive; that is objected to under the Land Valuation Act 2010. After an objection decision, an appeal or QCAT review needs the whole tax and late payment interest paid first (TAA s 69(1)(b)). It must come within 60 days that QCAT cannot extend (s 69(3)) and the Supreme Court must not extend (s 70(3)). Asserted.
20. **A deceased owner's home stays exempt for one 30 June only.** Under s 23(5), (6) it stays exempt only for the next 30 June after the death (that day itself if the death is on 30 June), and only if it is unused or used only as it was before. It must also still be land the deceased person is taken to own under s 23(4)(a) (finding 22). Asserted.
21. **A trustee farmer is not simply "not exempt".** s 53(2)(a) leaves out "a trustee or absentee" only from the individuals it exempts. s 53(2)(b) then exempts land owned by "a trustee of a trust, if all beneficiaries of the trust are persons mentioned in paragraph (a), (c) or (d)", and (c) exempts "a relevant proprietary company". So the trustee of a family trust whose beneficiaries are all resident individuals can have the farm exempt. Paragraphs (b)–(d) are out of scope, so a trustee or company owner of land used for a prescribed activity now answers `not covered`, whether or not the trustee is an absentee. Only an absentee who owns as an individual answers `not exempt` (finding 11). The baseline first took one input, "an absentee or trustee", and answered `not exempt` for both. Corrected after independent verification (2026-10-24): the seat question now asks the two facts separately. Asserted.
22. **s 23(5) exempts only land the deceased person is taken to own.** Its opening words are "Land that is taken to be owned by the deceased person under subsection (4)(a)". s 23(4) applies only "to the extent subsection (3) does not apply" and "until the administration of the estate is complete". So s 23(5) has nothing to exempt in three cases: the administrator's s 23(2) request is accepted and the beneficiaries are the owners (s 23(3)); the administration is complete; or s 23 does not apply at all (s 23(1)). The baseline's question asked only about the land's state before the death and its use since, so it answered "exempt" in all three. Corrected after independent verification (2026-10-24): the question now asks the s 23(1), (3) and (4) facts and answers from the core's `who is taken to own` rule. Asserted.
23. **Three duties name three different actors.** s 34(2): "The taxpayer must ... give notice". s 44(2): "The person must give notice". s 44A(4): "The person must give notice". ss 77(2) and 77A(2): "The owner of the land must give the commissioner notice". The baseline's regulative rules for ss 34, 44 and 44A named "the owner", against its own NOTES. Corrected after independent verification (2026-10-24): the s 34 rule's party is the taxpayer and the s 44 and s 44A rules' party is the person; the rules were renamed to match. Asserted: the traces' events and breaches name those parties.
24. **A "residential area" is defined by its use.** Schedule 4: "a building, part of a building, or another place of accommodation, that is used or available for use for residential purposes". So the s 40(2)(b) and (3)(b)(ii) floor-area base includes a shed, garage or other outbuilding only if it is used or available for living in. The baseline's `@desc` glossed residential areas as "houses, units, granny flats and associated outbuildings", which would widen the base and make more lettings look allowable. Corrected after independent verification (2026-10-24): both `@desc`s now gloss the Schedule 4 definition. Not asserted (a gloss).

**Other corrections after independent verification (2026-10-24).**

- The seat layer computed some rule logic itself: the TAA s 30(2) 30-day test, the TAA s 69(1)(b) payment condition and 60-day window, the s 74(2) and (3) dates, and the Regulation s 4(a)(ii) and TAA s 65(2) extensions. These are now core functions (`the stated date is at least 30 days after the notice is given (TAA s 30(2))`, `the right to appeal or apply for review (TAA ss 69, 70(3))`, `the date by which the outstanding land tax must be paid (s 74(2))`, `the start date for unpaid tax interest after a missed instalment (s 74(3))`, `the last day to elect to pay by instalments (Regulation s 4(a))`, `the last day to lodge an objection (TAA s 65(1)(d), (2))`). So are the last days of every notice, built from the same clocks as the regulative rules. The seat only calls them. No answer changed, except that the appeal question now returns the core's `Appeal or review answer`, whose wording is seat-neutral.
- The Commonwealth link cited Social Security Act 1991 "s 11" for the principal home. In the deposited text, s 11 defines homeowner and refers the principal home to s 11A, which also holds the absence rules (s 11A(8), (9)). The link and `encoding.json` now cite both.
- The s 74(2)(b) reading (the failure happens on the instalment's stated date) was not recorded. It is now listed under Departures.
- Changed inputs (a breaking change for any deployment): `Is my farm land exempt` asks "trustee or company" and "absentee" separately; `Is the deceased person's land exempt at the first 30 June after the death` asks three more facts and returns `Deceased estate exemption answer` instead of yes or no.

## What would need doing before this is worth relying on

- Deposit the authorised PDF (or a formulas sidecar) for s 18(2), and replace the averaging-factor input with the formula's T and V inputs.
- Deposit the Taxation Administration Regulation 2022 for the prescribed interest rate and weekday, and encode the weekly accrual of late payment interest (s 54(3)(b)).
- Deposit the Acts Interpretation Act 1954 (s 38 and the "month" definition) to settle the s 77 and s 77A last day (31 July or 1 August).
- Check the readings against Queensland Revenue Office practice or a decision:
  - the s 42A(3)(b) and 42B(3)(a) reading of "after it is used as the home";
  - "for each $1" counting whole dollars;
  - finding 15's stale cross-reference;
  - finding 17's penalty tax gap.
- Add the trustee, company and foreign surcharge rates (Schedule 2, s 33), the trust and company primary production exemptions (s 53(2)(b)–(d)), s 75, s 78 and the clearance certificate fee (Regulation s 3) if a scenario needs them.
- Settle the s 74(2)(b) reading (the stated date, or the day after) against Queensland Revenue Office practice or a decision.
- Run the Legalese Studio stages this baseline skipped: Resolve, Refine and Test, an independent test pass, and the human gates.
