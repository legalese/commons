# NOTES -- the keel for the Money Laundering, Terrorist Financing and Transfer of Funds (Information on the Payer) Regulations 2017 (S.I. 2017/692), United Kingdom

STATUS (2026-11-05): written after `mlr-core.l4`, `mlr-definitions.l4` and `mlr-definitions-tests.l4` compiled and ran clean on the main build 1.6.109 (and read the same on 1.6.108); the exact `check.sh` numbers are in the final report.
**This is not the official text.** The source is `uksi-2017-692.txt`, a plain-text rendering made by a converter script (`inputs/SOURCES.md`); nothing here is verified against the official text.
A `-- src:N | ...` line in the modules is a verbatim slice of that rendering, and `python3 -I srcrefs.py check --refs` reports 0 problems over both modules.
In the rendering a definition that was taken out shows as `...` on a line of its own; this note calls such a line "blank".

What the keel is: the shared vocabulary for five part agents (`mlr1` to `mlr5`), who each encode their own line ranges afterwards, and who see only `mlr-core.l4`.
It is lines 1-232 of the text: the title block, the enacting words and Part 1 (regulations 1 to 7).
`PLAN.md` says what each part should expect from the core, and lists the seams.

## What the files hold

- `mlr-core.l4`: nouns and two constants only; no rule.
- `mlr-definitions.l4`: every definition and rule of reading in lines 1-232 (regulations 2 to 7), as defined-term functions; the parts do NOT import it (a part cannot import another module of the family), so what a part needs from it arrives as an input named for the regulation it comes from (`PLAN.md`, seams S-K1 to S-K4).
- `mlr-definitions-tests.l4`: expected values written by hand from the text, both sides of every threshold, and a NOTHING case wherever a function can answer NOTHING.
- `PLAN.md`, `PROGRESS.md`.

## Coverage table (lines 1-232 of `uksi-2017-692.txt`; the keel's whole range)

Every line from 1 to 232 is in exactly one row.
The dispositions were assigned by reading each row, and the `encoded` rows were then tied to functions by the `@ref` locator that covers their lines (a row with no covering locator could not be called `encoded`).
A reg 3(1) term that only says "has the meaning given by ..." is encoded as a pointer: a function returning, as a STRING, the provision it points at, word for word from the line.
The definition itself is the row of the part that owns the provision pointed at (`PLAN.md`, "Definitions left to the parts").

| lines | provision | disposition | where |
|---|---|---|---|
| 1-3 | Made / Laid before Parliament / Coming into force (dates blank in the rendering) | inert (reason 1: not operative) | the date of making, laying and coming into force; the rendering gives no dates |
| 4-5 | Enacting words | inert (reasons 1 and 2: enacting words; a designation and regulation-making power) | the Treasury's designation under section 2(2) of the European Communities Act 1972 and the powers the Regulations are made under |
| 6 | PART 1 heading | inert (reason 1: heading) |  |
| 7-8 | reg 1 heading; reg 1(1) citation | inert (reason 2: short title) | reg 1(1) says what the Regulations may be cited as; it binds no one |
| 9 | reg 1(2) commencement | encoded | `reg 1(2) the date these Regulations came into force` (mlr-core.l4) |
| 10-11 | reg 2 Prescribed regulations | encoded | `reg 2 these Regulations are prescribed for the purposes of` |
| 12-13 | reg 3 heading; reg 3(1) chapeau | inert (reason 1: heading and introductory words) | the limbs below are encoded, each in its own row |
| 14 | reg 3(1) Annex 1 financial institution | encoded | `reg 3(1) Annex 1 financial institution is given by` |
| 15 | reg 3(1) appropriate body | encoded | `reg 3(1) the body is an appropriate body` |
| 16 | reg 3(1) art market participant | encoded | `reg 3(1) art market participant is given by` |
| 17 | reg 3(1) auction platform | encoded | `reg 3(1) auction platform is given by` |
| 18 | reg 3(1) auditor | encoded | `reg 3(1) auditor is given by` |
| 19 | reg 3(1) authorised cryptoasset firm | encoded | `reg 3(1) the person is an authorised cryptoasset firm` |
| 20 | reg 3(1) authorised person | encoded | `reg 3(1) the person is an authorised person` |
| 21 | reg 3(1) the FCA | encoded | `reg 3(1) the FCA` |
| 22-25 | reg 3(1) beneficial owner | encoded | `reg 3(1) beneficial owner is given by` |
| 26-32 | reg 3(1) body corporate | encoded | `reg 3(1) the entity is a body corporate` |
| 33 | reg 3(1) bill payment service provider | encoded | `reg 3(1) the person is a bill payment service provider` |
| 34 | reg 3(1) branch | encoded | `reg 3(1) the place is a branch` |
| 35 | reg 3(1) business relationship | encoded | `reg 3(1) business relationship is given by` |
| 36 | reg 3(1) (blank) | repealed or blank in this text | the rendering shows `...` where a definition was taken out; nothing to encode |
| 37 | reg 3(1) the capital requirements regulation | encoded | `reg 3(1) the capital requirements regulation` |
| 38 | reg 3(1) cash | encoded | `reg 3(1) the payment is in cash` |
| 39 | reg 3(1) casino | encoded | `reg 3(1) casino is given by` |
| 40 | reg 3(1) the Commissioners | encoded | `reg 3(1) the Commissioners` |
| 41 | reg 3(1) contract of long-term insurance | encoded | `reg 3(1) the contract is a contract of long-term insurance` |
| 42 | reg 3(1) correspondent relationship | encoded | `reg 3(1) correspondent relationship is given by` |
| 43 | reg 3(1) credit institution | encoded | `reg 3(1) credit institution is given by` |
| 44 | reg 3(1) cryptoasset business | encoded | `reg 3(1) cryptoasset business is given by` |
| 45 | reg 3(1) cryptoasset exchange provider | encoded | `reg 3(1) cryptoasset exchange provider is given by` |
| 46 | reg 3(1) custodian wallet provider | encoded | `reg 3(1) custodian wallet provider is given by` |
| 47 | reg 3(1) customer due diligence measures | encoded | `reg 3(1) the measures required by a regulation are customer due diligence measures` |
| 48 | reg 3(1) the data protection legislation | encoded | `reg 3(1) the data protection legislation is given by` |
| 49 | reg 3(1) Department for the Economy | encoded | `reg 3(1) Department for the Economy` |
| 50 | reg 3(1) designated supervisory authority | encoded | `reg 3(1) designated supervisory authority is given by` |
| 51 | reg 3(1) document | encoded | `reg 3(1) the thing is a document` |
| 52 | reg 3(1) electronic money | encoded | `reg 3(1) electronic money is given by` |
| 53 | reg 3(1) electronic money institution | encoded | `reg 3(1) electronic money institution is given by` |
| 54 | reg 3(1) electronic money issuer | encoded | `reg 3(1) electronic money issuer is given by` |
| 55 | reg 3(1) eligible Scottish partnership | encoded | `reg 3(1) eligible Scottish partnership is given by` |
| 56 | reg 3(1) the emission allowance auctioning regulation | encoded | `reg 3(1) the emission allowance auctioning regulation` |
| 57-61 | reg 3(1) enactment | encoded | `reg 3(1) an enactment contained in the source is an enactment` |
| 62 | reg 3(1) enhanced customer due diligence measures | encoded | `reg 3(1) the measures required by a regulation are enhanced customer due diligence measures` |
| 63 | reg 3(1) estate agent | encoded | `reg 3(1) estate agent is given by` |
| 64 | reg 3(1) (blank) | repealed or blank in this text | the rendering shows `...` where a definition was taken out; nothing to encode |
| 65 | reg 3(1) external accountant | encoded | `reg 3(1) external accountant is given by` |
| 66 | reg 3(1) financial institution | encoded | `reg 3(1) financial institution is given by` |
| 67 | reg 3(1) firm | encoded | `reg 3(1) the entity is a firm` |
| 68 | reg 3(1) fourth money laundering directive | encoded | `reg 3(1) the fourth money laundering directive` |
| 69 | reg 3(1) FSMA | encoded | `reg 3(1) FSMA` |
| 70 | reg 3(1) funds transfer regulation | encoded | `reg 3(1) the funds transfer regulation` |
| 71 | reg 3(1) (blank) | repealed or blank in this text | the rendering shows `...` where a definition was taken out; nothing to encode |
| 72 | reg 3(1) group | encoded | `reg 3(1) group is given by` |
| 73 | reg 3(1) high value dealer | encoded | `reg 3(1) high value dealer is given by` |
| 74 | reg 3(1) independent legal professional | encoded | `reg 3(1) independent legal professional is given by` |
| 75 | reg 3(1) insolvency practitioner | encoded | `reg 3(1) insolvency practitioner is given by` |
| 76 | reg 3(1) law enforcement authority | encoded | `reg 3(1) law enforcement authority is given by` |
| 77 | reg 3(1) letting agent | encoded | `reg 3(1) letting agent is given by` |
| 78 | reg 3(1) local weights and measures authority | encoded | `reg 3(1) local weights and measures authority is given by` |
| 79 | reg 3(1) manager | fork F5 | `reg 3(1) the person is a manager of the firm` |
| 80 | reg 3(1) markets in financial instruments directive | encoded | `reg 3(1) the markets in financial instruments directive` |
| 81 | reg 3(1) markets in financial instruments regulation | encoded | `reg 3(1) the markets in financial instruments regulation` |
| 82 | reg 3(1) money laundering | encoded | `reg 3(1) money laundering is given by` |
| 83 | reg 3(1) money service business | encoded | `reg 3(1) the undertaking is a money service business` |
| 84 | reg 3(1) the NCA | encoded | `reg 3(1) the NCA` |
| 85 | reg 3(1) nominated officer | encoded | `reg 3(1) the person is a nominated officer` |
| 86 | reg 3(1) notice | encoded | `reg 3(1) the communication is a notice` |
| 87 | reg 3(1) occasional transaction | encoded | `reg 3(1) the transaction is an occasional transaction` |
| 88-93 | reg 3(1) officer | encoded | `reg 3(1) officer of a body corporate`; `reg 3(1) officer of an unincorporated association`; `reg 3(1) officer of a partnership`; `reg 3(1) the person is an officer of the entity` |
| 94 | reg 3(1) ongoing monitoring | encoded | `reg 3(1) the measures are ongoing monitoring` |
| 95 | reg 3(1) payment services | encoded | `reg 3(1) payment services is given by` |
| 96 | reg 3(1) payment service provider | encoded | `reg 3(1) payment service provider is given by` |
| 97 | reg 3(1) politically exposed person | encoded | `reg 3(1) politically exposed person is given by` |
| 98 | reg 3(1) the PRA | encoded | `reg 3(1) the PRA` |
| 99 | reg 3(1) PRA-authorised person | encoded | `reg 3(1) PRA-authorised person is given by` |
| 100 | reg 3(1) proliferation financing | encoded | `reg 3(1) proliferation financing is given by` |
| 101 | reg 3(1) regulated activity | encoded | `reg 3(1) regulated activity is given by` |
| 102-106 | reg 3(1) regulated market | encoded | `reg 3(1) the market is a regulated market` |
| 107 | reg 3(1) relevant parent undertaking | encoded | `reg 3(1) the person is a relevant parent undertaking` |
| 108 | reg 3(1) relevant person | encoded | `reg 3(1) relevant person is given by` |
| 109 | reg 3(1) relevant requirement | encoded | `reg 3(1) relevant requirement is given by` |
| 110 | reg 3(1) self-regulatory organisation | encoded | `reg 3(1) the body is a self-regulatory organisation` |
| 111 | reg 3(1) senior management | encoded | `reg 3(1) the person is senior management` |
| 112 | reg 3(1) (blank) | repealed or blank in this text | the rendering shows `...` where a definition was taken out; nothing to encode |
| 113-116 | reg 3(1) specified disclosure obligations | encoded | `reg 3(1) the obligation is a specified disclosure obligation` |
| 117 | reg 3(1) (blank) | repealed or blank in this text | the rendering shows `...` where a definition was taken out; nothing to encode |
| 118 | reg 3(1) specified investment cryptoasset | encoded | `reg 3(1) specified investment cryptoasset is given by` |
| 119-121 | reg 3(1) specified investment cryptoasset firm | encoded | `reg 3(1) the person is a specified investment cryptoasset firm` |
| 122-124 | reg 3(1) supervisory authority | encoded | `reg 3(1) the provisions that name the supervisory authority` |
| 125 | reg 3(1) supervisory functions | encoded | `reg 3(1) the function is a supervisory function` |
| 126 | reg 3(1) tax adviser | encoded | `reg 3(1) tax adviser is given by` |
| 127 | reg 3(1) telecommunication, digital and IT payment service provider | encoded | `reg 3(1) telecommunication, digital and IT payment service provider is given by` |
| 128-132 | reg 3(1) terrorist financing | encoded | `reg 3(1) the act is terrorist financing` |
| 133 | reg 3(1) (blank) | repealed or blank in this text | the rendering shows `...` where a definition was taken out; nothing to encode |
| 134 | reg 3(1) third country | encoded | `reg 3(1) the place is a third country` |
| 135 | reg 3(1) transfer of funds supervisory authority | encoded | `reg 3(1) transfer of funds supervisory authority is given by` |
| 136 | reg 3(1) trust or company service provider | encoded | `reg 3(1) trust or company service provider is given by` |
| 137 | reg 3(1) UK auctioning regulations | encoded | `reg 3(1) the UK auctioning regulations` |
| 138 | reg 3(1) the UK GDPR | encoded | `reg 3(1) the UK GDPR is given by` |
| 139 | reg 3(1) UK regulated market | encoded | `reg 3(1) the market is a UK regulated market` |
| 140 | reg 3(2) chapeau | inert (reason 1: introductory words) | the limbs (a) to (f) below are encoded, each in its own row |
| 141 | reg 3(2)(a) | encoded | `reg 3(2)(a) the amount is at least the sterling threshold`; `reg 3(2)(a) the amount exceeds the sterling threshold` |
| 142 | reg 3(2)(b) | fork F3 | `reg 3(2)(b) the equivalent in another currency of a sum in sterling` |
| 143 | reg 3(2)(c) | encoded | `reg 3(2)(c) the property is real property` |
| 144 | reg 3(2)(d) | encoded | `reg 3(2)(d) references to carrying on business in the United Kingdom are read in accordance with` |
| 145 | reg 3(2)(e) | encoded | `reg 3(2)(e) a qualifying relationship is read in accordance with` |
| 146 | reg 3(2)(f) | encoded | `reg 3(2)(f) parent undertaking and subsidiary undertaking have the same meaning as in` |
| 147 | reg 4 heading | inert (reason 1: heading) |  |
| 148-150 | reg 4(1) | encoded | `reg 4(1) the relationship is a business relationship`; `reg 4(1) to (3) there is a business relationship` [gathered by hand, ruling E1 option B] |
| 151 | reg 4(2) | encoded | `reg 4(2) the relationship is treated as a business relationship`; `reg 4(1) to (3) there is a business relationship` [gathered by hand, ruling E1 option B] |
| 152 | reg 4(3) | encoded | `reg 4(3) the estate agent is treated as entering into a business relationship with the purchaser`; `reg 4(3) the date on which the estate agent is treated as entering into a business relationship with the purchaser`; `reg 4(1) to (3) there is a business relationship` [gathered by hand, ruling E1 option B] |
| 153 | reg 5 heading | inert (reason 1: heading) |  |
| 154-157 | reg 5(1) | fork F1 | `reg 5(1) the individual is a beneficial owner of the body corporate` |
| 158-160 | reg 5(2) | encoded | `reg 5(2) the individual controls the body corporate` |
| 161-164 | reg 5(3) | encoded | `reg 5(3) the individual is a beneficial owner of the partnership` |
| 165 | reg 5(4) | encoded | `reg 5(4) limited liability partnership is given by` |
| 166 | reg 6 heading | inert (reason 1: heading) |  |
| 167-172 | reg 6(1) | encoded | `reg 6(1) the person is a beneficial owner of the trust` |
| 173-178 | reg 6(2) | encoded | `reg 6(2) the power is control over the trust`; `reg 6(2) and (4)(b) the individual has control over the trust` [gathered by hand, ruling E1 option B] |
| 179 | reg 6(3) | encoded | `reg 6(3) the individual is a beneficial owner of the foundation or other legal arrangement` |
| 180-186 | reg 6(4) | encoded | `reg 6(4)(b) the individual has control over the trust, given the four exclusions`; `reg 6(2) and (4)(b) the individual has control over the trust` [gathered by hand, ruling E1 option B]; `reg 6(4)(a) the individual is regarded as entitled to the interest or having control over the trust` |
| 187-189 | reg 6(5) | encoded | `reg 6(5) the interest is a specified interest` |
| 190-192 | reg 6(6) | encoded | `reg 6(6) the person is a beneficial owner of the estate` |
| 193-196 | reg 6(7) | fork F2 | `reg 6(7) the person is a beneficial owner of the legal entity or arrangement`; `reg 6(7) and (9) the individual is a beneficial owner of an entity outside regulation 5 and regulation 6(1), (3) and (6)` [gathered by hand, ruling E1 option B] |
| 197 | reg 6(8) | encoded | `reg 6(8) the individual is regarded as benefiting from or exercising control over the property` |
| 198 | reg 6(9) | fork F2 | `reg 6(9) the individual is a beneficial owner in any other case`; `reg 6(7) and (9) the individual is a beneficial owner of an entity outside regulation 5 and regulation 6(1), (3) and (6)` [gathered by hand, ruling E1 option B] |
| 199 | reg 7 heading | inert (reason 1: heading) |  |
| 200-221 | reg 7(1) | encoded | `reg 7(1)(a) the relevant person is within a class the FCA supervises`; `reg 7(1)(b) the professional bodies that are supervisory authorities for the relevant person`; `reg 7(1)(c) the relevant person is within a class the Commissioners supervise`; `reg 7(1)(d) the relevant person is within a class the Gambling Commission supervises`; `reg 7(1) the supervisory authorities of the relevant person`; DECLARE Authority (mlr-core.l4) |
| 222 | reg 7(2) | encoded | `reg 7(2) the supervisory authorities may agree that one of them acts as the supervisory authority` |
| 223 | reg 7(3) | encoded | `reg 7(3) the authority which agreed to act has notified the relevant person or published the agreement` |
| 224 | reg 7(4) | encoded | `reg 7(4) the supervisory authorities for the relevant person must co-operate in the performance of their functions` |
| 225 | reg 7(5) | encoded | `reg 7(5) the money service business is an excluded money service business` |
| 226-229 | reg 7(6) | encoded | `reg 7(6) paragraph (5) must be read with` |
| 230-232 | reg 7(7) | encoded | `reg 7(7) the credit union is a credit union in Northern Ireland` |

## Fork register

Each fork names every reading, the text that licenses it, and the rule that encodes the chosen reading (or the explicit "not covered" value).

### F1 -- reg 5(1): a company whose securities are listed on a regulated market

The text (reg 5(1), lines 154-157):

```
L154 | (1) In these Regulations, “beneficial owner”, in relation to a body corporate which is not a company whose securities are listed on a regulated market, means—
L155 | (a) any individual who exercises ultimate control over the management of the body corporate;
L156 | (b) any individual who ultimately owns or controls (in each case whether directly or indirectly), including through bearer share holdings or by other means, more than 25% of the shares or voting rights in the body corporate; or
L157 | (c) an individual who controls the body corporate.
```

- **Reading 1 (encoded):** reg 5(1) gives a definition for "a body corporate which is not a company whose securities are listed on a regulated market".
  A listed company is outside the definition, and the text says nothing in these lines about who its beneficial owners are, so the answer is NOTHING (NOTHING-kind: limited by its own wording).
  Licensed by: the limit sits in the words that introduce the definition ("which is not a company whose securities are listed ...").
- **Reading 2:** a listed company has no beneficial owner at all, so the answer is JUST FALSE.
  Licensed by: "means", which closes the definition for what it covers; but a listed company is not what it covers.
- **Reading 3:** the three limbs apply to a listed company as well.
  Not licensed by the words; listed for completeness.
- **Encoded as:** `reg 5(1) the individual is a beneficial owner of the body corporate` answers NOTHING for a `Customer` that is a `a company` with `securities listed on a regulated market` set, whatever the individual's holdings (asserted in the tests, both shareholding levels).
  What follows for a listed company is for the rules that speak of one: regs 28(5), 30ZA(b), 37(3)(a)(iv) and 43(1) (lines 824, 933, 1186 and 1366).

### F2 -- reg 6(7) and reg 6(9): an entity that both paragraphs reach

The text (lines 193-198):

```
L193 | (7) In these Regulations, “beneficial owner”, in relation to a legal entity or legal arrangement which does not fall within regulation 5 or paragraphs (1), (3) or (6) of this regulation, means—
L194 | (a) any individual who benefits from the property of the entity or arrangement;
L195 | (b) where the individuals who benefit from the entity or arrangement have yet to be determined, the class of persons in whose main interest the entity or arrangement is set up or operates;
L196 | (c) any individual who exercises control over the property of the entity or arrangement.
L197 | (8) For the purposes of paragraph (7), where an individual is the beneficial owner of a body corporate which benefits from or exercises control over the property of the entity or arrangement, the individual is to be regarded as benefiting from or exercising control over the property of the entity or arrangement.
L198 | (9) In these Regulations, “beneficial owner”, in any other case, means the individual who ultimately owns or controls the entity or arrangement or on whose behalf a transaction is being conducted.
```

- Reg 6(7) covers a legal entity or arrangement "which does not fall within regulation 5 or paragraphs (1), (3) or (6)"; reg 6(9) covers "any other case".
  An entity outside regulation 5 and paragraphs (1), (3) and (6) is therefore inside both.
  The text does not say which governs.
- **Encoded as:** two functions, one per paragraph (ruling E1, option C), and one hand-gathered function (E1, option B as guidance): `reg 6(7) and (9) the individual is a beneficial owner of an entity outside regulation 5 and regulation 6(1), (3) and (6)`.
  Where reg 6(9) says yes, the answer is JUST TRUE (every reading agrees); where reg 6(7) says yes and reg 6(9) says no, NOTHING (the text does not choose); where both say no, JUST FALSE; where either is unanswered and the other does not settle it, NOTHING.
  The matrix is asserted in `mlr-definitions-tests.l4`.
- **Other reading (not encoded):** reg 6(7) governs and reg 6(9) is the residue for what reg 6(7) leaves; the answer would then be reg 6(7)'s alone.
  A lawyer may prefer it; it would turn the `reg 6(7) yes, reg 6(9) no` row from NOTHING to JUST TRUE.

### F3 -- reg 3(2)(b): "the previous working day" has no definition in Part 1

The text (reg 3(2)(b), line 142), and the only definition of "working day" in the Regulations (reg 64B, line 2119):

```
L142 | (b) the equivalent in another currency on a particular day of a sum expressed in sterling is determined by converting the sum in sterling into its equivalent in ... that other currency using the London closing exchange rate for sterling and the relevant currency for the previous working day;
L2119 | “working day” means any day other than a Saturday, a Sunday, Christmas Day, Good Friday or a day which is a bank holiday under the Banking and Financial Dealings Act 1971 in any part of the United Kingdom.
```

- **Reading 1 (encoded):** reg 64B's definition opens "In this Part" (Part 7A), so reg 3(2)(b) uses an undefined term and, for the exchange rate itself, points outside the text (the London closing rate).
  NOTHING-kind (undefined term; points outside the text).
- **Reading 2:** reg 64B's definition is the Regulations' meaning of "working day" everywhere, so a Saturday, Sunday, Christmas Day, Good Friday or bank holiday is not a working day.
- **Encoded as:** `reg 3(2)(b) the equivalent in another currency of a sum in sterling` takes the rate as an input and answers NOTHING when the rate is not a positive number.
  The function does not choose a day, so both readings give the same encoded outcome; the choice would bite only in a rule that computes the day (none in this range).

### F4 -- Schedule 2: the rendering shows 13 unnumbered items, and reg 10 speaks of points by number

This fork is raised by the core (`Listed activity`); the owning rows are reg 10(2)(a), (3)(c) and (4)(a) (part `mlr1`) and Schedule 2 itself (part `mlr4`).

```
L293 | (c) an undertaking whose only listed activity is trading for its own account in one or more of the products listed in point 7 of ... Schedule 2 where the undertaking does not have a customer (and, for this purpose, “customer” means a person other than the undertaking which is not a member of the same group as the undertaking).
L295 | (a) a “listed activity” means an activity listed in points 2 to 12, 14 and 15 of ... Schedule 2;
```

- **Reading 1:** the items are numbered 1 to 13 in the order the rendering prints them; "points 2 to 12, 14 and 15" then names points that do not exist.
- **Reading 2:** the items carry the numbering of the Schedule's source list, with gaps: 2 to 12, then 14 and 15 (13 items); then "point 7" is the sixth printed item, "Trading for own account or for account of customers in any of the following".
  Licensed by: reg 10(3)(c) speaks of "trading for its own account ... in point 7", which only the sixth item matches, and reg 10(4)(a)'s "points 2 to 12, 14 and 15" is 13 points, the number of items shown.
  Schedule 3A (line 3165, part `mlr5`) also cites "points 2, 3, 6, 7 or 8 of ... Schedule 2", which this keel cannot place by the rendering alone either.
- **Encoded as:** the core names the 13 items and numbers none (`Listed activity`).
  The part that encodes reg 10 chooses; this keel records that reading 2 matches both citations and that the rendering alone cannot confirm it.

### F5 -- reg 3(1) "manager": "means ... and includes"

The text (line 79):

```
L79 | “manager”, in relation to a firm, means a person who has control, authority or responsibility for managing the business of that firm, and includes a nominated officer;
```

- **Reading 1 (encoded):** "means" closes the definition: a person with control, authority or responsibility for managing the business, plus a nominated officer; anyone else is not a manager (JUST FALSE).
- **Reading 2:** "includes" opens the list, so a person who is neither is not covered either way (NOTHING).
- **Encoded as:** `reg 3(1) the person is a manager of the firm`; listed again under "Marginal readings for a lawyer", (d).

### Hand-gathered functions (ruling E1, option B as guidance)

I gathered the routes to one legal effect by hand in plain L4, and only where it helps a reader; every route also has its own function (option C).
- reg 4(1) to (3): `reg 4(1) to (3) there is a business relationship` (routes: the relationship of reg 4(1), reg 4(2)'s services, reg 4(3)'s estate-agent case).
- reg 6(2) with reg 6(4)(b): `reg 6(2) and (4)(b) the individual has control over the trust`.
- reg 6(7) with reg 6(9): see F2.
No construct that gathers a legal effect by name was looked for or proposed.

### Rulings of 2026-11-04 (bench `commons-negation-1030`), word for word from the brief

- **E1** (bench `commons-negation-1030`; should a legal effect be one definition gathered from every section that gives it?): option B, as guidance for gathering a legal effect's routes by hand only, with no pilot run; option A (gathering by bare name) is withdrawn as a direction for the language, not deferred; option C (per-section answers) applies everywhere else; the Magna Carta pilot in the printed recommendation (chapters 2, 3, 4, 5, 37, 43, 46 and 53, with a blind second reader) is not to be run. Meng's lean, verbatim: "B but generally uncomfortable with this much magic because it takes the language from unopinionated to opinionated in ways that are hard to teach an l4 novice." Meng's note, verbatim: "Fundamentally I feel like we are trying to make the language do work that the human l4 drafter should do. Too much magic. Can’t we just decline to be this opinionated and say the programmer needs to do this thinking?" Marked 2026-11-03T23:19:02.812Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
- **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. Meng's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." Meng's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23

## Jural relations

Most of the keel's range creates no relation: it defines terms and gives rules of reading.
Those provisions are listed once, as `none`.
The relations that Part 1 does create are all in reg 7 (who supervises whom).
The Hohfeld kinds are recorded here and are not typed into any answer (ruling N2).

| provision | holder (right, privilege, power, immunity) | bearer (duty, no-right, liability, disability) | kind | L4 rule |
|---|---|---|---|---|
| reg 7(1)(a) | the FCA | a relevant person in a class listed in (a)(i) to (ix) | power / liability to be supervised | `reg 7(1)(a) the relevant person is within a class the FCA supervises`; `reg 7(1) the supervisory authorities of the relevant person` |
| reg 7(1)(b) | each professional body listed in Schedule 1 | a relevant person who is a member of it, or regulated or supervised by it | power / liability to be supervised | `reg 7(1)(b) the professional bodies that are supervisory authorities for the relevant person` |
| reg 7(1)(c) | the Commissioners | a relevant person in a class listed in (c)(i) to (viii) | power / liability to be supervised | `reg 7(1)(c) the relevant person is within a class the Commissioners supervise` |
| reg 7(1)(d) | the Gambling Commission | a casino | power / liability to be supervised | `reg 7(1)(d) the relevant person is within a class the Gambling Commission supervises` |
| reg 7(2) | the supervisory authorities, together | the relevant person | power (to agree that one acts) / liability | `reg 7(2) the supervisory authorities may agree that one of them acts as the supervisory authority` |
| reg 7(3) | the relevant person | the authority which agreed to act | claim / duty (to notify or publish) | `reg 7(3) the authority which agreed to act has notified the relevant person or published the agreement` |
| reg 7(4) | each supervisory authority | each other supervisory authority for the same person | claim / duty (to co-operate) | `reg 7(4) the supervisory authorities for the relevant person must co-operate in the performance of their functions` |
| regs 1(1), 1(2), 2 | none | none | none: citation, commencement; reg 2 gives the Regulations a status under FSMA, and the relations that follow are FSMA's | `reg 1(2) the date these Regulations came into force`; `reg 2 these Regulations are prescribed for the purposes of` |
| reg 3(1) | none | none | none: definitions, each a function whose name begins `reg 3(1)` | see the coverage table |
| reg 3(2) | none | none | none: rules of reading, `reg 3(2)(a)` to `(f)` | see the coverage table |
| reg 4 | none | none | none: a definition | `reg 4(1) the relationship is a business relationship` and the others |
| regs 5, 6 | none | none | none: definitions of "beneficial owner" | `reg 5(1)` to `reg 6(9)` |
| regs 7(5), 7(6), 7(7) | none | none | none: definitions | `reg 7(5)`, `reg 7(6)`, `reg 7(7)` |

## Marginal readings for a lawyer

The brief names two readings that I took as the status quo and was not to decide: (a) a failed "if" counts as the text's no, clause by clause, and flat negatives count as the text's no; (b) a prohibition or grant limited by its own wording does not.
Two more are mine and are flagged the same way: (c) and (d).
The code comment on each branch carries `Marginal readings, (x)` for (a), (c) and (d); every branch tagged `NOTHING-kind (limited by its own wording)` rests on (b), and the table under (b) is generated from those comments.

**(a) A failed "if" or a flat negative answers JUST FALSE.** The other reading: the text does not say "only if", so a failed "if" is NOT covered (NOTHING).
- `reg 5(2) the individual controls the body corporate`: "an individual controls a body corporate if (a) ... or (b) ...".
- `reg 7(5) the money service business is an excluded money service business`: "is an excluded money service business if it is an authorised person who has permission ...".
- `reg 7(7) the credit union is a credit union in Northern Ireland`: "is a credit union which is (a) ... or (b) ..." (a definition by "is", not by "means").
- `reg 6(4)(b) the individual has control over the trust, given the four exclusions` (four branches) and `reg 6(2) and (4)(b) the individual has control over the trust`: "does not have control solely as a result of" is a flat negative, so ruling N2 applies; the other reading is NOTHING.

**(b) A grant or limit by its own wording answers NOTHING outside the limit.** The other reading: the case outside the limit is the text's no (JUST FALSE).
Every branch below answers NOTHING because the text limits what it says to a case, a context or a period, and the case before it falls outside:

| line in `mlr-definitions.l4` | function | the limiting words |
|---|---|---|
| 138 | `reg 3(1) auditor is given by` | "(except in regulation 31(4))" |
| 187 | `reg 3(1) external accountant is given by` | "(except in regulation 31(4))" |
| 241 | `reg 3(1) tax adviser is given by` | "(except in regulation 31(4))" |
| 457 | `reg 3(1) the place is a branch` | "except where the context otherwise requires" |
| 515 | `reg 3(1) the measures required by a regulation are customer due diligence measures` | "where relevant, those required by regulations 29 and 33 to 37" |
| 516 | `reg 3(1) the measures required by a regulation are customer due diligence measures` | "where relevant, those required by regulations 29 and 33 to 37" |
| 536 | `reg 3(1) the measures are ongoing monitoring` | "(except where the context otherwise requires)" |
| 539 | `reg 3(1) the measures are ongoing monitoring` | "means at least the measures described in regulation 28(11)"; a lower bound, and the text does not say fewer is not ongoing monitoring |
| 721 | `reg 3(1) the person is an officer of the entity` | "except in Part 8 and Schedule 5" |
| 906 | `reg 3(1) the act is terrorist financing` | "(except where the context otherwise requires)" |
| 1050 | `reg 4(2) the relationship is treated as a business relationship` | the paragraph treats a relationship of that kind as a business relationship and says nothing of any other |
| 1064 | `reg 4(3) the estate agent is treated as entering into a business relationship with the purchaser` | "at the point when the purchaser's offer is accepted by the seller"; the paragraph says nothing before that point or of any other party |
| 1076 | `reg 4(3) the date on which the estate agent is treated as entering into a business relationship with the purchaser` | the paragraph speaks of an estate agent and a purchaser |
| 1301 | `reg 6(1) the person is a beneficial owner of the trust` | "where the individuals (or some of the individuals) benefiting from the trust have not been determined" (Marginal readings, (b)) |
| 1329 | `reg 6(4)(a) the individual is regarded as entitled to the interest or having control over the trust` | "where an individual is the beneficial owner of a body corporate which is entitled to a specified interest ... or which has control over the trust" |
| 1396 | `reg 6(7) the person is a beneficial owner of the legal entity or arrangement` | "where the individuals who benefit from the entity or arrangement have yet to be determined" (Marginal readings, (b)) |
| 1409 | `reg 6(8) the individual is regarded as benefiting from or exercising control over the property` | "where an individual is the beneficial owner of a body corporate which benefits from or exercises control over the property" |
| 1584 | `reg 7(2) the supervisory authorities may agree that one of them acts as the supervisory authority` | "Where ... there is more than one supervisory authority" |
| 1585 | `reg 7(2) the supervisory authorities may agree that one of them acts as the supervisory authority` | "Where ... there is more than one supervisory authority" |
| 1599 | `reg 7(3) the authority which agreed to act has notified the relevant person or published the agreement` | "Where there has been an agreement under paragraph (2)" |
| 1615 | `reg 7(4) the supervisory authorities for the relevant person must co-operate in the performance of their functions` | "Where there has not been an agreement under paragraph (2)" |

**(c) A "must" that has not been done answers JUST FALSE.** `reg 7(3) the authority which agreed to act has notified the relevant person or published the agreement` answers FALSE when there has been an agreement under reg 7(2) and the authority has done neither.
The text states a duty, not its failure; I read the undischarged duty as the text's no (a compliance answer).
The other reading: NOTHING, because the text does not say what follows.

**(d) "means ... and includes".** `reg 3(1) the person is a manager of the firm`: see fork F5.

### Reading a result: FALSE and NOTHING

In this row an answer is `JUST TRUE`, `JUST FALSE` or `NOTHING`.
- **A "no" (`JUST FALSE`)** is the Regulations saying no in their own words: a thing defined by "means" that does not meet the definition (not a branch, not a document, not a business relationship, not an excluded money service business); a closed list that does not contain the case; a flat negative (a person who "does not have control solely as a result of" a listed matter does not have control).
- **"Not covered" (`NOTHING`)** is the Regulations not answering: a term they leave undefined or define "except where the context otherwise requires"; a list they open with "includes"; a rule limited to a case the facts fall outside of ("where there has been an agreement under paragraph (2)", "except in regulation 31(4)", "where the individuals ... have not been determined"); a company whose securities are listed on a regulated market, in the definition of beneficial owner of a body corporate; a person whom no paragraph of reg 7(1) lists; a sterling conversion with no exchange rate supplied; a fact the Regulations take from another Act or instrument and the caller has not supplied.
- A caller must never turn `NOTHING` into `FALSE`.
  A part that takes a function of this keel as an input takes it as `MAYBE BOOLEAN` and passes `NOTHING` through (`PLAN.md`, "How a seam input is typed and used").

## Unstable dialect

I looked at time, versions and workarounds in lines 1-232 and found nothing that earned a second encoding on the unstable build.
Time: the only date that operates in the range is the commencement date in reg 1(2) (26 June 2017, a constant in the core); every other date is the date of an instrument the text cites.
Versions: the rendering shows one version of each provision here; removed definitions appear as `...`.
Workarounds: the hand-gathering of reg 4's routes and reg 6's controls (ruling E1, option B) and the `MAYBE BOOLEAN` pass-through need no construct the main build lacks.
No second, unstable encoding of these provisions was written.

## What the main binary does not accept

The binary governs; where a skill describes something main rejects, this is what main said.
Measured on 1.6.109 and read the same on 1.6.108 unless stated.
Sorted by how the failure shows:

**Silent (wrong answer, exit code 0):**
- `NOT a AND b` parses as `NOT (a AND b)`: with `a` true and `b` false it answers TRUE where `(NOT a) AND b` answers FALSE (probe over both builds, both assertions satisfied).
  Every `NOT` in the modules is parenthesised.
- A name defined in two imported modules cannot be used, and the failure comes at the use, not at the import (from the brief, not re-measured).
  The modules avoid it by construction: every constructor lives once, in the core, and the enumerations private to `mlr-definitions.l4` use constructors that appear nowhere else.

**Loud (an error says so):**
- `x elem xs` (infix): "You are trying to apply x (predefined) of type NUMBER (which is not a function) to 2 arguments here" (1.6.109).
  `elem x xs`, prefix, is what main accepts.
- An `#ASSERT` whose expression continues on a second line: "unexpected EQUALS ... expecting %, ;, end of input, or space token" (1.6.109).
  Every `#ASSERT` here is on one line.
- `REFUSE` as a branch: "unexpected end of input, expecting String Literal" (1.6.109).
  "Not covered" is `NOTHING` throughout.
- No section-level `GIVEN`, no sets, no `YMD` of my own: from the brief; the modules use none of them.

## Findings the parts will want

- The rendering of Schedule 2 is unnumbered (fork F4).
- The rendering marks removed definitions as `...` (rows 36, 64, 71, 112, 117, 133); one of them sits inside the list of "specified disclosure obligations" and leaves that list with three limbs.
- "Working day" is defined only for Part 7A (fork F3).
- Many reg 3(1) terms point at a provision the parts own; `PLAN.md` lists them under "Definitions left to the parts".

