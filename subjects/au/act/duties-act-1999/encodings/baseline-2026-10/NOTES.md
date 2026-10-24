# Duties Act 1999 (ACT): baseline encoding for the buyer of a home or vacant land

## Method

**Baseline.** Written straight from the deposited texts with the `writing-l4-rules` skill, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18.
There is no REFUSE in it. A transaction the encoding does not reach (a date outside 1 July 2026 to 30 June 2027, commercial use, a motor vehicle, a landholder, a trust, a commercial lease with premium, business assets, a transfer only partly under a will, the schemes not deposited) answers `not covered` with the reason, and tests assert each one.
It was checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

It is written in two layers:

- **`duties-core.l4`**, the seat-neutral core. It uses the texts' own actors and terms ("the transferee", "an eligible home buyer", "the commissioner", "the taxpayer"). The computations (dutiable value, the three Tables, the scheme tests, interest, penalty tax) are functions. Where the texts say "must" or "may" or set a deadline, there is a regulative rule (`DEONTIC`): six in all.
- **`duties-seat.l4`**, the buyer's seat. It asks 22 questions, each with `@export` and a `@desc` on every input, grouped under `§§` headings. It builds the core's records from plain answers and restates no rule. An input with the same name means the same fact in every question.

No earlier encoding of this Act existed to keep. The ACT has no requirement ledger, so no ledger line is closed. No scenario life raised these provisions; the cases are the encoder's.

## Edition

| Instrument | Register id | Version | Deposited at |
|---|---|---|---|
| Duties Act 1999 | A1999-7 | Republication No 79, effective 16 December 2025 | `../../registers/source-bundle/A1999-7.txt` |
| Taxation Administration (Amounts Payable—Duty) Determination 2026 | DI2026-155 | notified 30 June 2026, commences 1 July 2026 | `../../../taxation-administration-amounts-payable-duty-determination-2026/registers/source-bundle/DI2026-155.txt` |
| Taxation Administration (Amounts Payable—Home Buyer Concession Scheme) Determination 2026 | DI2026-157 | notified 30 June 2026, commences 1 July 2026 | `../../../taxation-administration-amounts-payable-home-buyer-concession-scheme-determination-2026/registers/source-bundle/DI2026-157.txt` |
| Taxation Administration (Amounts Payable—Pensioner Duty Concession Scheme) Determination 2026 | DI2026-159 | notified 30 June 2026, commences 1 July 2026 | `../../../taxation-administration-amounts-payable-pensioner-duty-concession-scheme-determination-2026/registers/source-bundle/DI2026-159.txt` |
| Taxation Administration Act 1999 | A1999-4 | Republication No 52, effective 26 November 2025 | `../../../taxation-administration-act-1999/registers/source-bundle/A1999-4.txt` |

**Every rate and threshold comes from the determinations, not from the Act.** Duties Act s 31 charges "duty at the determined rate", and the dictionary defines that as "a rate determined by the Minister under the Taxation Administration Act, section 139". Tables 1, 2 and 3 of DI2026-155 are encoded as tables. The three determinations commence on 1 July 2026 and revoke the 2025 ones, which are not deposited, so a transaction dated before 1 July 2026 is `not covered`. Determinations under TAA s 139 are made each 1 July, so a transaction dated after 30 June 2027 is also `not covered` until the 2027 ones are deposited.

The Taxation Administration Act is brought in because Duties Act s 3 says it "is incorporated and is to be read as one with this Act": it supplies the consequences of a default (interest, penalty tax, the offence of not lodging or notifying) and the right to object. Two figures it needs are not deposited and are inputs: the interest rate's market rate component (TAA s 26(2): a determined rate, or the RBA 90-day bank bill rate under table 26), and the value of a penalty unit (Legislation Act 2001 s 133; the republication note gives $160 for an individual at 26 November 2025).

**Attribution.** All five texts: © Australian Capital Territory, from the ACT Legislation Register (https://www.legislation.act.gov.au/), licensed under CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/). Changed: converted to plain text by Legalese Commons, and quoted in part in the comments of the `.l4` files. Not endorsed by the ACT Government. Unofficial versions; the authorised versions are the PDFs on the register. The terms record for the Act is the copy of `SOURCE-LICENSE.md` beside this file; each determination's and the TAA's is in its own subject folder.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `duties-core.l4`, `duties-seat.l4` | `duties-cases-transferee.l4` | 186 written, 186 satisfied |

In addition, 5 `#TRACE`s carry an `-- expect:` line: four breaches by the transferee (not lodging under s 15; not paying under s 16 or within the notice of assessment; not giving the DI2026-159 s 5(2) notice; not paying a reassessment after notice) and one obligation still pending (the commissioner's duty to decide an objection, for which s 104 sets no period). Each was read and matches its expectation.

`l4 run` on all three files: 0 errors, 0 warnings (2026-10-24). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. Every expected value was written by hand from the texts, with the arithmetic in the comment above the assertion.

## Seat

**The transferee: an individual buying a home or vacant land in the ACT.** That may be a first-time buyer, an owner-occupier, a pensioner moving to a smaller home, or an investor (Table 2). They ask: "How much duty do I pay, and under which rate?", "Am I eligible for the home buyer concession, the pensioner concession or the owner occupier rate, and if not, which condition fails?", "When must I lodge and pay?", "What interest and penalty tax follow a late payment?", "If I do not move in, or move out within the year, what must I tell the Commissioner, by when, and what do I then owe?", "Can I ask for a shorter residence period or a later start, and by when?", "Is a transfer from a deceased estate, or on separation, dutiable?".

Most of the determinations' machinery speaks of what the Commissioner "may determine". Those powers appear as what they mean for the buyer: an input saying whether the Commissioner has determined a shorter residence period, a later start, a younger required age, an exemption from the same-names rule, or is satisfied of an unforeseen circumstance or a relationship breakdown. In the core, the transferee, the commissioner and an approved person (s 239) are parties to the regulative rules.

**No second seat.** The texts in scope put duties only on the transferee (and, by the s 15(2)(b) alternative, on the approved person who lodges electronically, usually the conveyancer). The transferor has none here.

The 2026-10-18 defaults:

- **The Act, with the instruments that set its numbers.** Those are the three 2026 determinations. The Taxation Administration Act is also brought in, because the Duties Act incorporates it (s 3) and the buyer's questions about defaults need it.
- **The actors the text names:** the transferee, the eligible home buyer, the pensioner, the commissioner, the registrar-general, an approved person.
- **Judgments left to others are answered conditionally:** the exemptions in ss 232D, 232G, 232H and 232I answer "exempt ..., if the commissioner is satisfied ...". The Commissioner's determinations and satisfactions under the schemes are inputs, as is what the Commissioner is satisfied of for penalty tax (TAA ss 31, 34).
- **The texts' own definitions are worked out from facts:** dutiable value, eligible owner occupier transaction, eligible home buyer, eligible transaction (both schemes), allowed interest, required age, residence requirement, residence period, former property. Borrowed terms are asked as facts: the Commonwealth pensions and the Gold Card, a family violence order, "domestic partner", matrimonial and relationship property, "home" (including the Commissioner's opinion that it is suitable).
- **One case:** one dutiable transaction.
- **The texts' own terms,** quoted in the comment above each rule.
- **Machinery out:** the commissioner's powers of assessment and valuation, s 139 itself, commencement and revocation.

One departure, recorded here: the duty question assumes the buyer applies for any concession they are eligible for (DI2026-155 Sch 1 s 5, DI2026-157 s 8, DI2026-159 s 8). Applying is encoded separately, as a permission with its 12-month extension window.

## Scope

**In:**

- Duties Act ss 7 and 10 (as a choice of the kind of transaction and property), s 11 (the transaction date, a fact), s 12, s 13, s 15(1)–(2) (a regulative rule), s 16 and table 16 items 1, 3 and 5 (a regulative rule), s 18, s 20(1), s 21(1), s 22(1), s 31
- Duties Act s 232D(1)(a), and ss 232E–232I
- DI2026-155 pt 2, ss 4–5, Tables 1 and 2; pt 3 Table 3 (computed in the core and asserted; the buyer's questions answer `not covered` for commercial use); Schedule 1 ss 1–6
- DI2026-157 ss 4–8, Schedules 1 and 2
- DI2026-159 ss 3–9
- TAA ss 25–27 (interest), ss 30–35 and table 34 (penalty tax), s 36, s 67 (failure to lodge or notify), ss 100–104 (objection)

**Out, each answering `not covered`:**

- motor vehicle duty (ch 9): its 2026 determined rates are not deposited
- landholder duty and the other ch 3 transactions; declarations of trust and transfers to or from trustees; commercial leases with premium; s 33 business assets; commercial use (DI2026-155 pt 3)
- a transfer only partly in conformity with a will or intestacy (s 232D(2)–(3))
- deferral under pt 2.6A (moot where the home buyer concession makes the duty nil)
- the Disability Duty Concession Scheme and the Pensioner Duty Deferral Scheme (their determinations are not deposited)
- the s 109 disability exemption (see finding 13)
- foreign-purchaser matters (see finding 15)
- a transaction dated before 1 July 2026 or after 30 June 2027

**Out, not asked:** the land rent lease case of s 20(1)(b)(i); aggregation (s 24), apportionment (s 26), partitions (s 29) and price changes (s 30); the other exemptions in pt 2.5 and ch 11; options to purchase (table 16 item 2); cancelled agreements and subsales (s 15(3), s 50); remission of interest and penalty tax (TAA ss 29, 37); extensions and instalments (TAA s 52); internal review and the ACAT.

## Read with the Commonwealth encodings

The stable `l4` cannot IMPORT across encoding folders, so the links are recorded here and not in code.

- **Social Security Act 1991** (`../../../../social-security-act-1991/`). The Pensioner Duty Concession Scheme turns on receiving "a Services Australia age pension" or "a Services Australia disability support pension" at 50 or older (DI2026-159 s 5(1)(a)(i)–(ii)). Whether a buyer receives either is that Act's question; here it is an input.
- **Veterans' Entitlements Act 1986** (`../../../../veterans-entitlements-act-1986/`). The DVA age pension equivalent, the Gold Card and the "service pension" (age, invalidity or partner service pension, DI2026-159 s 3) are that Act's. Inputs here.
- **Family Law Act 1975** (`../../../../family-law-act-1975/`). Its court orders (s 232F), its s 90B–90D and pt 8AB financial agreements (ss 232G, 232H), its s 68B and s 114 injunctions (DI2026-157 Schedule 1(1)(d)(ii)), and its definitions of "de facto relationship" and "spouse party" (s 232E) decide the separation exemptions and the family-violence allowed interest. Inputs here.
- **Income Tax Assessment Act 1997** (`../../../../income-tax-assessment-act-1997/`). The duty paid forms part of the CGT cost base of the property: s 110-35(4), "The third [incidental cost] is stamp duty or other similar duty". A nil duty under either scheme adds nothing to the cost base.

## What the Act turns out to say

1. **Section 75 still refers to a First Home Owner Grant Act 2000, though the ACT has none.** In the pt 2.6A deferral, an "eligible person" includes one who "is eligible for a first home owner grant under the First Home Owner Grant Act 2000" (s 75(b), (c)). The jurisdiction README records that the ACT has no first home owner grant (the Home Buyer Concession Scheme replaced it) and that the A2000-21 number belongs to an unrelated Act. The deferral is not encoded.
2. **DI2026-155 Schedule 1 s 1(1) letters two paragraphs "(b)".** The definition runs "(a) all transferees acquire both a legal and an equitable interest ...; and (b) all transferees are an individual; (i) a transferee is not an individual if the individual acquires the eligible property other than in the individual's personal capacity; and (b) at least 1 transferee will own and occupy ...". The second "(b)" is the residence requirement, and "(i)" hangs under the first. The encoding reads three conditions: the legal and equitable interest, individuals in their personal capacity, and residence. Schedule 1 s 5(1) is also garbled ("on the lodgement of the transfer eligible owner occupier transaction").
3. **Neither scheme has a property-value or income cap.** No dollar limit appears anywhere in DI2026-157 or DI2026-159, so none is encoded. A first home buyer's $2,000,000 house and a pensioner's $1,800,000 unit both pay nil. Asserted.
4. **Table 1 has a cliff at $1,455,000, and Table 2 a dip.** Up to $1,455,000, Table 1 gives $63,078; at $1,455,100 the flat $4.54 per $100 on the whole amount gives $66,061.54, a jump of $2,983.54 for $100 more. At the same point Table 2 falls from $66,070 to $66,061.54. The owner occupier rate saves a flat $2,992 at every value from $300,000 to $1,455,000, and nothing above it. Asserted.
5. **The flat rate is applied unrounded.** The bands charge "for every $100, or part of $100", which rounds up. The flat rate above $1,455,000 (and Table 3's above $2,100,000) is "$4.54 per $100 applied to the total dutiable amount", with no "or part". The encoding applies it to the exact amount ($1,455,050 gives $66,059.27). That is a reading. Asserted.
6. **No text says which determination prevails.** DI2026-155 s 5, DI2026-157 s 7 and DI2026-159 s 9 are each made "for the purposes of section 31". INFERENCE: each scheme's nil rate displaces Tables 1 and 2 for its own eligible transactions. DI2026-155 s 5 note 1 adds that the owner occupier rate "is not a home buyer concession scheme for the purposes of part 2.6A".
7. **The pensioner scheme measures the former home's sale from two different days.** A home the buyer left when it was sold is a "former property" only if sold "within a 1-year period ending on the transaction date" (DI2026-159 s 5(4)(b)). Section 5(1)(c) then requires it to be sold "within 1 year before or after the registration date". A home sold in the gap between the year before the transaction date and the year before registration is a former property, yet fails (c): sold 15 July 2025, contract 10 July 2026, registration 20 July 2026, not eligible. Asserted.
8. **The pensioner scheme has no look-back, and one exception that does nothing.** Section 5(1)(b) asks what the buyers and their partners hold "on the transaction date", not, as DI2026-157 does, in the previous 5 years. Its exception for land "that a person was required to and did relinquish prior to the transaction date" can never apply to land held on that date, so it does no work. The encoding asks only about land held on the transaction date.
9. **The family-violence allowed interest reaches only the buyer's own land.** Under DI2026-157 Schedule 1(1)(d), once the family violence is evidenced, every interest "in land held by the eligible home buyer" is allowed (a READING of its breadth). Nothing held by a domestic partner is allowed under (d); paragraph (c) allows a domestic partner's land only where the partner "is a spouse" and the Commissioner is satisfied the relationship has broken down. So a current de facto partner's land still disqualifies. Asserted for (c) and (d).
10. **The home buyer scheme's family-violence cross-references are loose.** Schedule 2 s 1(1)(b) refers to "Schedule 1, section 1 (d)", and the note in Schedule 1 to "Schedule 2, section 1 (b)", but Schedule 1 has no sections and the provision is Schedule 2 s 1(1)(b). Schedule 1(1) says "interest interest". The extra residence condition binds "the domestic partner referenced in the family violence order or the injunction", so where paragraph (d) rests on a competent person declaration there is no named partner for it to bind. The encoding applies the condition only where paragraph (d) is what makes the buyer eligible. Asserted.
11. **Only the two schemes say "never eligible".** DI2026-157 s 6(3) and DI2026-159 s 5(3) say a buyer who fails the requirements "was never eligible for the concession", and their example puts the tax default at 15 days after registration. DI2026-155 Schedule 1 s 1(3) says only that "duty is calculated with reference to section 5 (1) (b)". INFERENCE: under Duties Act s 16(2) the Table 2 duty was payable on registration, so the same default from day 15 applies to all three. Asserted: interest on Raj and Priya's $2,992 runs from 29 October 2026.
12. **Section 15 sets no penalty, but the TAA does, and most buyers need not lodge.** Section 15(1) says the transferee "must ... lodge" within 90 days, without a penalty. TAA s 67(1) makes failing "to lodge a document ... required to be lodged by a tax law" an offence (maximum 50 penalty units, $8,000 at $160 a unit). INFERENCE: s 67(2), on failing "to notify the commissioner ... of any matter ... of which notice is required to be lodged by a tax law", reaches the 14-day notices in the determinations. Under s 15(2)(a), the duty to lodge does not apply where the registrar-general must report the transaction under the Land Titles Act 1925 s 178B, as for a transfer lodged for registration. Asserted.
13. **The s 109 disability exemption is not a home buyer's exemption.** It is in pt 3.4 and exempts "a person who acquires a land use entitlement by an allotment of shares or an issue of units", for supportive housing, on NDIS and pension conditions. It does not reach an ordinary transfer of a home. The README's account of it, beside the pensioner concessions, could be read more widely. Not encoded.
14. **When the 14 days for notice start is read, not stated.** The notice is due 14 days after the first of "the end of any period allowed for compliance with a requirement of the transaction" and the day the transferee "first becomes aware". The encoding reads the period allowed for the residence requirement as ending on the first anniversary of the residence start date if no one moved in in time, and otherwise at the end of the residence period counted from moving in. Asserted.
15. **There is no foreign-purchaser duty in the deposited Act.** The word "foreign" appears only in s 209A (motor vehicles of foreign countries) and in definitions of places. Nothing in the three determinations turns on citizenship or residency, so a foreign buyer's duty is worked out the same way. Commonwealth foreign investment law is outside. The question answers `not covered`, as the brief asks. Asserted.
16. **Only the schemes have an age condition.** DI2026-157 and DI2026-159 require "the required age" ("18 years of age", or a younger age the Commissioner determines), which is read as 18 or over. DI2026-155 Schedule 1 has no age condition, so a 17-year-old owner-occupier gets Table 1 but needs a Commissioner's determination for the home buyer concession. Asserted.
17. **"Domestic partner" is defined in none of the three determinations.** The Duties Act defines "partner" and "domestic relationship" but not "domestic partner". It is asked as a fact.
18. **"Principal place of residence" is worded slightly differently.** DI2026-155 says "primarily and lawfully occupies"; DI2026-157 and DI2026-159 say "primarily occupies". All three exclude unlawful occupation from "occupy", so the difference changes nothing here.
19. **"A daily basis" is read as the annual rate divided by 365.** TAA s 25(1) charges interest "calculated on a daily basis from the end of the last day for payment", at the market rate component plus "8% per annum" (s 26). The divisor is not stated. Leap years are not treated differently. That is a reading. Asserted.

## Before relying on it

- An independent test pass, and a check of each Table row against the authorised PDF of DI2026-155.
- The 2027 determinations when made (from 1 July 2027), as a second dated row, and the 2025 ones for transactions before 1 July 2026.
- Deposit and encode the Duties (Pensioner Duty Deferral Scheme) Determination 2026 (DI2026-141), the Disability Duty Concession Scheme and the motor vehicle duty determinations 2026, and the interest rate determination under TAA s 139(1)(b).
- Confirm the readings in findings 5, 9, 11, 12 and 14 with ACT Revenue practice or a ruling.
- Encode the transfer only partly under a will (s 232D(2)–(3)), aggregation (s 24) and the other pt 2.5 exemptions.
- The JACS copyright policy, which could not be read on 2026-10-20 (see `SOURCE-LICENSE.md`).
