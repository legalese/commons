# NOTES -- Child Benefit (Rates) Regulations 2006 (S.I. 2006/965), L4 encoding by agent `cbr` (Sonnet 5.5)

The source is `uksi-2006-965.txt`, a plain-text rendering made by a converter script from the CLML of legislation.gov.uk (version dated 2026-04-06, see ../../registers/source-bundle/uksi-2006-965.meta.json).
It is the converter's rendering, not the official text.
It is not marked up, it fuses footnote numbers to years in the Table of regulation 4, and nothing here is verified against the official text.
The parent Act (the Social Security Contributions and Benefits Act 1992 and its Northern Ireland twin) and the Child Benefit (General) Regulations 2006 are not encoded.
Entitlement to child benefit, the meaning of "child", and the other terms this text borrows are therefore asked as facts, and many of the seat's questions are rate lookups.
The target is the stable `l4` (main, version 1.6.98, commit 7689b0d).

Layer 1 is `cbr-nouns.l4`, `cbr-reg1.l4`, `cbr-reg2-benefits.l4`, `cbr-reg2-couples.l4`, `cbr-reg2-rate.l4`, `cbr-reg3.l4` and `cbr-reg4.l4`, with tests in `cbr-tests-reg*.l4`.
Layer 2 is `cbr-seat.l4` and its cases `cbr-cases-seat.l4`.

## Seat

The seat is a person who is responsible for a child or qualifying young person and claims or receives Child Benefit.
That person asks what weekly rate is payable for each child, and when the enhanced rate is not paid for a second child (couples and polygamous marriages).
It was chosen because it is the only party the text speaks to: every operative paragraph (reg 2(1) to (6), reg 3) fixes what is payable to "a person" in respect of a child.
The other persons the text mentions (the spouse, the partner, the other members of a polygamous marriage, the voluntary organisation, the Commissioners, the body that pays an allowance) are plain inputs, not seats.
The paying authority is not named in this text (the Act names it), and the seat never speaks for an official.
The text puts no duty on the person: it requires no claim, notice or return and sets no penalty, so there is no "What do I owe?" question.
What the person is exposed to is a judgment: the Commissioners' acceptance of an analogous allowance (reg 2(6)(c)(viii)), which the seat takes as a fact.
The seat has thirteen questions, in the text's order, under `§` groups in `cbr-seat.l4`:

- reg 1(1): Are these Regulations in force for the week I am asking about?
- reg 1(2): Is the young person I look after a qualifying young person for these Regulations?
- reg 1(3): On what day are the facts about me and my child tested for my week?
- reg 2(1): Does the enhanced rate or the rate in any other case apply to this child?
- reg 2 and reg 3: What weekly amount of child benefit is payable for this child, in pounds?
- reg 2(2)(a): Am I in a household where the couples rule in regulation 2(2) can apply to me?
- reg 2(3): Am I a member of a polygamous marriage?
- reg 2(2): Is the enhanced rate paid for my child, or only for an older child in my household?
- reg 2(4): Is the enhanced rate withheld from this child because I am a voluntary organisation or live with the child's parent?
- reg 2(6): Is the payment I receive a specified benefit?
- reg 2(5): Does the payment I receive give me the enhanced rate for this child?
- reg 3(2): Which transitional provisions and savings decide whether the earlier rates give me more?
- reg 3(1): How much am I paid, in pounds a week, if the earlier rates would have given me more?

Regulation 4 has no seat question: it revokes other instruments and gives the person nothing to ask.
The seat layer builds the records the long modules expect in each question's `WHERE`, from plain inputs, and calls the same layer-1 rule.
It restates no rule.
Where a rule never reads a record field, the seat gives the field a fixed placeholder and says so in a comment (31 such comment lines in `cbr-seat.l4`).

## Jural relations

The paying authority (the person liable to pay child benefit under the parent Act) is not named in this text.
The table calls it "the payer".
The claimant is "the person to whom child benefit is payable".
Rows for pure definitions and counting rules say `none`.

| holder of right / privilege / power / immunity | bearer of correlative duty / no-right / liability / disability | section | L4 rule |
|---|---|---|---|
| none | none | reg 1(1), commencement (src:9) | `these Regulations are in force in the week beginning` |
| none | none | reg 1(2), "qualifying young person" (src:13-15) | `a person is a qualifying young person for the purposes of these Regulations` |
| none | none | reg 1(3) (src:16) | `the day on which conditions and facts are tested in the week beginning` |
| the claimant: right to the enhanced rate (£27.05) for the only, elder or eldest child | the payer: duty to pay it | reg 2(1)(a) (src:19) | `the case under regulation 2(1) for the child in the week beginning`, `the enhanced rate` |
| the claimant: right to £17.90 for any other child | the payer: duty to pay it | reg 2(1)(b) (src:20) | `the rate in any other case` |
| the payer: privilege of not paying the enhanced rate for the younger of the couple's or household's children | the claimant: no-right to the enhanced rate for that child | reg 2(2) (src:21-28) | `paragraph (2) allows the enhanced rate for the claimant's child` |
| none | none | reg 2(2)(a), (3) (src:21-25, src:29-31) | `paragraph (2)(a) applies to the claimant`, `a claimant is a member of a polygamous marriage` |
| the payer: privilege of not paying the enhanced rate | a voluntary organisation, or a person residing with a parent of the child otherwise than as a couple: no-right | reg 2(4) (src:32-34) | `paragraph (4) bars the enhanced rate` |
| the claimant paid a specified benefit for the only, elder or eldest child: right to the enhanced rate | the payer: duty to pay it | reg 2(5) (src:35-38) | `paragraph (5) gives the enhanced rate for the child` |
| none | none | reg 2(6)(a), (b), (c)(i) to (vii) (src:39-49) | `a payment is a specified benefit` |
| the Commissioners for Her Majesty's Revenue and Customs: power to accept an allowance as analogous | the claimant paid such an allowance: liability to have the enhanced rate turn on their acceptance | reg 2(6)(c)(viii) (src:50) | `a payment is a specified benefit under paragraph (6)(c)(viii)`, with the acceptance as an input |
| the claimant: right to the greater amount | the payer: duty to pay it | reg 3(1) (src:52-55) | `the greater amount payable under regulation 3(1)` |
| none | none | reg 3(2) (src:56-58) | `the relevant transitional provisions and savings for` |
| none: an act done to other instruments, which gives the person nothing | none | reg 4 (src:59-87) | `the Table in regulation 4` |

## Coverage table

The text has 4 regulations and 87 lines (title block lines 1-7).
Every line of the 87 is in a row.
Counts: 42 rows; 18 `encoded`, 13 `fork`, 11 `inert`, 0 `repealed or blank in this text`.
A row is `fork` when a Fork register entry is about a reading of that row's own words (a term of art the row uses whose reading is settled in another row, such as "week" in reg 2(2), stays `encoded`, and the note names the fork).

| provision | source lines | disposition | where | note |
|---|---|---|---|---|
| title block | src:1-3 | inert | -- | pure citation or title: the instrument number, the subject heading and the title name the instrument and fix no rate. |
| date of making ("Made 29th March 2006") | src:4 | encoded | cbr-reg1.l4: `the date these Regulations were made` | carried as a defined value. |
| coming-into-force line | src:5 | encoded | cbr-reg1.l4: `the date these Regulations come into force` | points to reg 1(1); the date is carried once, there. |
| recital: draft approved by both Houses | src:6 | inert | -- | machinery: the parliamentary procedure by which the Regulations were made. |
| enacting words and powers | src:7 | inert | -- | machinery: the Treasury's regulation-making powers under both Acts. |
| reg 1 heading | src:8 | inert | -- | pure title. |
| reg 1(1), citation half | src:9 | inert | -- | pure citation: how the Regulations may be cited. |
| reg 1(1), commencement half | src:9 | fork | cbr-reg1.l4: `these Regulations are in force in the week beginning` | F9: "immediately after the Child Benefit (General) Regulations 2006" cannot be ordered within the day; the date, 10 April 2006, is encoded. |
| reg 1(2), lead-in and "SSCBA" | src:10-11 | inert | -- | pure citation: an abbreviation for the title of an Act. |
| reg 1(2), "SSCB(NI)A" | src:12 | inert | -- | pure citation: an abbreviation for the title of an Act. |
| reg 1(2), "qualifying young person" | src:13-15 | encoded | cbr-reg1.l4: `a person is a qualifying young person for the purposes of these Regulations` | the two limbs are alternatives by place; Part 9 of each Act is asked as a fact. |
| reg 1(3) | src:16 | fork | cbr-reg1.l4: `the day on which conditions and facts are tested in the week beginning` | F7: "that week" has no antecedent in reg 1(3) and "week" is undefined; tested on the first day of the week. |
| reg 2 heading | src:17 | inert | -- | pure title. |
| reg 2(1), lead-in | src:18 | fork | cbr-reg2-rate.l4: `the person is a child or a qualifying young person`, `the weekly rate of child benefit under regulation 2 for the child in the week beginning` | "child" is not defined in the text and is asked (F13). |
| reg 2(1)(a) | src:19 | fork | cbr-reg2-rate.l4: `the enhanced rate`, `the enhanced rate would, but for paragraph (2), be payable for the child`, `the case under regulation 2(1) for the child in the week beginning` | F1, F2, F5, F8: "subject to paragraphs (2) to (5)" gives no order; the text dates the figure in no way. |
| reg 2(1)(b) | src:20 | fork | cbr-reg2-rate.l4: `the rate in any other case` | £17.90, the figure of the version encoded (F8). |
| reg 2(2), lead-in | src:21 | encoded | cbr-reg2-couples.l4: `paragraph (2) allows the enhanced rate for the claimant's child` | "in any week": the week is the first day (F7). |
| reg 2(2)(a)(i) | src:22-23 | encoded | cbr-reg2-couples.l4: `paragraph (2)(a) applies to the claimant` | living with a spouse or civil partner: asked as a fact. |
| reg 2(2)(a)(ii) | src:24 | encoded | cbr-reg2-couples.l4: `paragraph (2)(a) applies to the claimant` | living with another as spouse or civil partner: asked as a fact. |
| reg 2(2)(a)(iii) | src:25 | encoded | cbr-reg2-couples.l4: `paragraph (2)(a) applies to the claimant`, `a claimant is a member of a polygamous marriage` | both limbs needed ("and"). |
| reg 2(2)(b) | src:26 | fork | cbr-reg2-rate.l4: `the enhanced rate would, but for paragraph (2), be payable for the child` | feeds the `paragraph (2)(b) holds` input of the couples rule; F2 says what "but for this paragraph" includes. |
| reg 2(2)(c) | src:27 | fork | cbr-reg2-couples.l4: the `Other persons listed in paragraph (2)(a) at the start of the week` record | F4, F10: several other persons; "another child or qualifying person" (no "young"). |
| reg 2(2), closing words | src:28 | fork | cbr-reg2-couples.l4: `the claimant's child is the elder of the children referred to in paragraph (2)(b) and (c)` | F3, F11: same-day births; the younger child's rate. |
| reg 2(3) | src:29-31 | encoded | cbr-reg2-couples.l4: `a claimant is a member of a polygamous marriage` | both (a) and (b) ("and"). |
| reg 2(4)(a) | src:32-33 | fork | cbr-reg2-rate.l4: `paragraph (4)(a) applies to the claimant` | F1: (5) can give the enhanced rate back after this bar. Voluntary organisation: asked as a fact. |
| reg 2(4)(b) | src:34 | fork | cbr-reg2-rate.l4: `paragraph (4)(b) applies to the claimant` | the carve-out "otherwise than as mentioned in paragraph (2)(a)" is read (F15); (4) against (5) is F1. |
| reg 2(5) | src:35-38 | fork | cbr-reg2-benefits.l4: `paragraph (5) gives the enhanced rate for the child` | F1, F2, F5, F6. |
| reg 2(6), lead-in | src:39 | encoded | cbr-reg2-benefits.l4: `a payment is a specified benefit` | the union of (a), (b), (c). |
| reg 2(6)(a) | src:40 | encoded | cbr-reg2-benefits.l4: `a payment is a specified benefit under paragraph (6)(a)` | the entitlement to the Schedule 4 increase is asked. |
| reg 2(6)(b) | src:41 | encoded | cbr-reg2-benefits.l4: `a payment is a specified benefit under paragraph (6)(b)` | same, Northern Ireland. |
| reg 2(6)(c), lead-in | src:42 | encoded | cbr-reg2-benefits.l4: `an instrument is one of those listed in paragraph (6)(c)(i) to (vii)`, `a payment is a specified benefit under paragraph (6)(c)(i) to (vii)` | an allowance for a child on a death due to service or war injury. |
| reg 2(6)(c)(i) to (vii) | src:43-49 | encoded | cbr-reg2-benefits.l4: the seven constructors of `Instrument granting an allowance for a child on a death due to service or war injury` (in cbr-nouns.l4) | seven named instruments; their content is out of text. |
| reg 2(6)(c)(viii) | src:50 | encoded | cbr-reg2-benefits.l4: `a payment is a specified benefit under paragraph (6)(c)(viii)` | the Commissioners' acceptance is asked as a fact. |
| reg 3 heading | src:51 | inert | -- | pure title. |
| reg 3(1) | src:52-55 | fork | cbr-reg3.l4: `the greater amount payable under regulation 3(1)`, `the weekly amount payable after the saving in regulation 3`, `the earlier Regulations named in regulation 3(1)` | F12: compared per child per week; the earlier amount is out of text. |
| reg 3(2)(a) | src:56-57 | encoded | cbr-reg3.l4: `the relevant transitional provisions and savings for` | child benefit payable under SSCBA. |
| reg 3(2)(b) | src:58 | encoded | cbr-reg3.l4: `the relevant transitional provisions and savings for` | child benefit payable under SSCB(NI)A. |
| reg 4 heading | src:59 | inert | -- | pure title. |
| reg 4, operative sentence | src:60 | encoded | cbr-reg4.l4: `the Table in regulation 4`, `regulation 4 revokes the whole of the instrument cited as`, `regulation 4 revokes part only of the instrument cited as` | encoded as data because reg 3 says "despite the revocation". |
| reg 4, footnote citations of the Table | src:61-73 | fork | cbr-reg4.l4: the `citation` field of each row | F14: the converter's fused footnote numbers. |
| reg 4, Table column headings | src:74 | inert | -- | pure title: the two column headings of the Table. |
| reg 4, Table rows 1 to 13 | src:75-87 | encoded | cbr-reg4.l4: `the Table in regulation 4` | 13 rows, 6 revoked in whole and 7 in part. |

## Fork register

Where I looked: the date at which each condition is tested (reg 1(3), F7); whether conditions are cumulative or alternative on the words (reg 2(2)(a), (b), (c) "and"; (2)(a)(i) to (iii) "or"; (3)(a) "and" (b); (4)(a) "or" (b)); what the text does when two rules overlap (reg 2(2), (4), (5), F1 and F2); and every place the text defers to something I do not have (the Dependencies table).

| fork | readings seen | reading taken | the text that licenses it |
|---|---|---|---|
| F1: does (5) give the enhanced rate back after (4) takes it away? | A: (5) wins over (4). B: (4) is an absolute bar. | A. | (1)(a) is "subject to paragraphs (2) to (5)" and states no order. (5)(b) describes the same child as (1)(a), so on B paragraph (5) would have no work to do. |
| F2: how do (2), (4) and (5) compose? | A: (2) takes the result of (1)(a), (4) and (5) as its "but for this paragraph" input. B: (5) overrides (2), so a specified-benefit recipient keeps the enhanced rate for a younger child in a couple. | A. The order is (1)(a), (4), (5), (2), stated in the head comment of cbr-reg2-rate.l4. | (2)(b) says "would, but for this paragraph, be payable ... at the enhanced rate": that is what remains after the other paragraphs. Nothing says (5) overrides (2). |
| F3: two children born on the same day | The elder is the one born first; the text does not say what the tie is. | NOTHING (not covered), never the enhanced rate, never 17.90. "Elder" is read as born earlier by date of birth. | (2) closing words: "only the elder or eldest of the children". |
| F4: reg 2(2) with three or more persons | (c) names "one of the other persons"; with several, any one of them could be it. | Only the eldest of the other persons' candidate children matters, so the seat takes one date. | (2) closing words: "the elder or eldest of the children and qualifying young persons referred to in sub-paragraphs (b) and (c)". |
| F5: "payable" in (1)(a) against "entitled" in (5)(b) | Two different sets of children. | The same set: one flag, "the only person, or the elder or eldest person, in respect of whom child benefit is payable to the claimant". | (5)(b) "the only, elder or eldest child ... in respect of whom that person is entitled to child benefit" repeats (1)(a)'s condition in other words. |
| F6: "which is a specified benefit" in (5) | It qualifies the allowance or the increase, or the benefit, pension or allowance being increased. | The payment: the allowance, or the increase, is what must be a specified benefit. | The relative clause follows "an allowance, or an increase of a benefit, pension or allowance". Reading it the other way changes only which of two facts is asked. |
| F7: "week", and "that week" in reg 1(3) | "Week" is undefined; reg 1(3) says "that week" with no week before it. | The week of the rate; every fact is tested on its first day; the one date input is that first day. A Monday-to-Sunday convention is out of text and not encoded. | reg 1(3): "at the beginning of that week"; reg 2(1)(a) and (2): "in any week". |
| F8: the date of the two figures | £27.05 and £17.90 are 2006 figures; or the figures of some later uprating. | The text dates neither. They are those of the version encoded (6 April 2026, from ../../registers/source-bundle/uksi-2006-965.meta.json, which is not part of the text), so a week beginning before 6 April 2026 is NOTHING. | reg 2(1)(a), (b) state the figures with no date or amount of increase. |
| F9: "shall come into force on 10th April 2006 immediately after the Child Benefit (General) Regulations 2006" | These Regulations come into force a moment after the General Regulations on the same day, or the date alone. | The date alone, and tested in weeks: a week beginning on or after 10 April 2006 is in force. Order within the day is not modelled. | reg 1(1). |
| F10: (2)(c) says "another child or qualifying person" | "Qualifying person" is a different thing from "qualifying young person". | The same: a qualifying young person. | (2)(b) and the closing words say "qualifying young person", and there is no definition of "qualifying person". |
| F11: the rate for the younger child under (2) | The text says the enhanced rate is payable "in respect of only the elder or eldest" and does not say what the younger child gets. | The younger child falls to "any other case", 17.90. | (1)(b): "in any other case". |
| F12: what reg 3(1) compares | One amount per person, per child, or per week. | The weekly amount payable for one child. | (1) is a rate per child per week; reg 3(1) says "the amount of child benefit which would have been payable", "greater than the amount prescribed by these Regulations". |
| F13: entitlement and "child" | The Regulations could fix a rate whether or not child benefit is payable; "child" could be defined here. | Entitlement is the parent Act's: asked as a fact, and where child benefit is not payable the answer is NOTHING, never 0. "Child" is asked as a fact. | (1): "the weekly rate of child benefit payable in respect of a child or qualifying young person". The text defines "qualifying young person" and not "child". |
| F14: the converter's fused footnote numbers in the Table | "19761" is the year 1976 and footnote 1, or a year 19761. | The year with the footnote number removed; each row's citation comes from the footnote text. Each citation's S.I. or S.R. year agrees with the title year on all 13 rows. | src:61-73 against src:75-87. |
| F15: (4)(b) "residing (otherwise than as mentioned in paragraph (2)(a)) with a parent" | The bracket takes out any claimant who is within (2)(a), or only the residence with the parent that is as mentioned in (2)(a). | The second: the question is whether the claimant lives WITH THAT PARENT as spouse, partner or fellow member of a polygamous marriage. A grandmother who lives with her husband and, separately, with the child's mother is caught by (4)(b). | the bracket qualifies "residing ... with a parent". |

F1 and F2 change real amounts for real households, and F8 means no figure here applies to a week before 6 April 2026.
F15 is exercised in the seat cases only; no layer-1 test asserts it.

## Dependencies on instruments outside the text

There are 17 dependencies.
The ones that matter most are 1, 2, 7, 8, 12 and 13: entitlement, the meaning of "child", the Schedule 4 increases, the Commissioners' acceptance, the earlier amount under reg 3, and the version of the figures.

| your provision | the provision it depends on | the input you made |
|---|---|---|
| 1. reg 2(1) "payable ... to a person" (src:18-19) | entitlement to child benefit under Part 9 of SSCBA (and the Northern Ireland Act) and the Child Benefit (General) Regulations 2006: not in the text, not encoded | `child benefit is payable to the claimant in respect of the child or qualifying young person` (BOOLEAN); NOTHING if false |
| 2. reg 2(1) "child" (src:18) | the Act's meaning of "child", not defined in the text | `a child for the purposes of child benefit` (BOOLEAN) |
| 3. reg 2(1)(a), (5)(b) "only person, or the elder or eldest" | the Act's rules on which person the benefit is payable to for each child | `the only person, or the elder or eldest person, in respect of whom child benefit is payable to the claimant` (BOOLEAN) |
| 4. reg 1(2) "qualifying young person" (src:13-15) | Part 9 of SSCBA, and of SSCB(NI)A | `where the young person is` (three-way choice) and two BOOLEANs, one for each Act |
| 5. reg 2(2)(a)(i), (ii) "spouse or civil partner", "living with" (src:22-24) | marriage and civil partnership law; no definition in the text | `living with the claimant's spouse or civil partner`, `living with another person as the claimant's spouse or civil partner` (BOOLEANs) |
| 6. reg 2(3)(b) "the law of a country which permits polygamy" (src:31) | foreign law | `the ceremony of the marriage took place under the law of a country which permits polygamy` (BOOLEAN) |
| 7. reg 2(6)(a) (src:40) | the Table in Part 4 of Schedule 4 to SSCBA, column 2 | `receipt of the benefit entitles the recipient to an increase for dependants specified in the Table in Schedule 4 to that Act` (BOOLEAN) |
| 8. reg 2(6)(b) (src:41) | the Table in Part IV of Schedule 4 to SSCB(NI)A | the same BOOLEAN, with the kind `a benefit under SSCB(NI)A` |
| 9. reg 2(6)(c)(i) to (vii) (src:43-49) | seven instruments: the Armed Forces and Reserve Forces (Compensation Scheme) Order 2005, the Naval, Military and Air Forces Etc. (Disablement and Death) Service Pensions Order 1983, the Pensions (Polish Forces) Scheme 1964, the War Pensions (Mercantile Marine) Scheme 1964, the Warrant of 21st December 1964, the Order of 22nd December 1964, and the Order by Her Majesty of 4th January 1971 | a choice of seven constructors plus `an instrument not listed in paragraph (6)(c)(i) to (vii)` |
| 10. reg 2(4)(a) "voluntary organisation" (src:33) | no definition in the text | `a voluntary organisation` (BOOLEAN) |
| 11. reg 2(4)(b) "a parent of the child" (src:34) | no definition in the text | `the claimant resides with a parent of the child or qualifying young person` (BOOLEAN) |
| 12. reg 2(6)(c)(viii) (src:50) | the judgment of the Commissioners for Her Majesty's Revenue and Customs | `the Commissioners accept the allowance as analogous to one granted under those instruments` (BOOLEAN) |
| 13. reg 3(1) (src:52-55) | the earlier Regulations of 1976 (GB and NI) and regulations 3 and 4 of the 1998 Amendment Regulations, whose content is not in the text and which reg 4 revokes | the earlier amount as a `MAYBE NUMBER` (NOTHING when no saving applies) |
| 14. reg 1(1) (src:9) | the Child Benefit (General) Regulations 2006 coming into force immediately before these | none: the order within the day is not modelled (F9) |
| 15. reg 2(1)(a), (b) (src:19-20) | the later uprating instruments that set the figures | `the date of the version of the text encoded` (6 April 2026, from ../../registers/source-bundle/uksi-2006-965.meta.json, not from the text) |
| 16. reg 1(3), 2(1)(a), 2(2) "week" | no definition of "week" in the text | the first day of the week, as a DATE (F7) |
| 17. reg 2(5) "paid in respect of a week" (src:35) | the instruments that pay the allowance or increase | `paid to the claimant in respect of the week`, `paid in respect of the child or qualifying young person` (BOOLEANs) |

## What the text turns out to say

1. The text states two figures, £27.05 and £17.90, and dates neither. They are the figures of the version dated 6 April 2026; the encoding answers for weeks beginning on or after that date and returns NOTHING for earlier weeks. Asserted.
2. The text fixes no order among paragraphs (2), (4) and (5), though (1)(a) is "subject to" all three. The order taken is (1)(a), (4), (5), (2). Asserted.
3. Paragraph (5) matters only where paragraph (4) has taken the enhanced rate away: where (4) does not apply, a specified benefit changes nothing. Asserted.
4. A voluntary organisation, and a person living with a parent of the child otherwise than as a couple (a grandmother, say), are not paid the enhanced rate (unless paragraph (5) gives it back); a stepfather who lives with the mother as her spouse is. Asserted.
5. The couples rule needs all of (a), (b) and (c). If the other person would not be paid the enhanced rate, or the claimant does not live with a spouse, partner or the other members of the marriage, the claimant keeps it. Asserted.
6. Paragraph (2)(a)(iii) needs a member of a polygamous marriage who is also residing with the other members, and paragraph (3) needs both a party married to more than one person and a ceremony under a law that permits polygamy. Asserted.
7. Under paragraph (2) the enhanced rate is payable for only the elder or eldest of the children; the text does not say what the younger child gets, and (1)(b) supplies 17.90. Asserted.
8. Two children born on the same day are not covered: the text does not say which is the elder. Asserted.
9. Paragraph (2)(c) writes "another child or qualifying person", where (2)(b) and the closing words write "qualifying young person". The encoding reads them as the same.
10. A specified benefit that is paid to someone else, or for a different child, or for a child who is not the only, elder or eldest, gives nothing under (5). Asserted.
11. Whether an allowance is "analogous" in (6)(c)(viii) is the Commissioners' judgment, not a rule; and (viii) reaches only allowances for a child on a death due to service or war injury. Asserted.
12. Paragraph (6)(a) writes "Part 4" and (6)(b) writes "Part IV", and (6)(b) spells the Act "SSCB (NI) A" where paragraph (2) of regulation 1 defines "SSCB(NI)A". The encoding treats them as the same Act.
13. A person who is in neither Great Britain nor Northern Ireland is not a qualifying young person, nor is a person in Great Britain who is one only under the Northern Ireland Act. Asserted.
14. "Child" is not defined in the text; "qualifying young person" is. The encoding asks both as facts. Asserted.
15. Where child benefit is not payable for a child at all, the text fixes no rate: the answer is NOTHING, never 0. Asserted.
16. Regulation 1(3) says "that week" with no week before it, and "week" is undefined. The encoding tests every fact on the first day of the week. Asserted.
17. The Regulations are in force from 10 April 2006 itself; the day before is not. Asserted.
18. Regulation 3's saving compares "the amount of child benefit which would have been payable under those Regulations" with the amount prescribed here; the text gives no earlier amount, so it is an input. Equal amounts give the same answer either way, and a penny more is the greater. Asserted.
19. Regulation 3(2) names regulations 3 and 4 of the two 1998 Amendment Regulations as "the relevant transitional provisions and savings", reg 3(1) applies them "had they remained in force", and reg 4 revokes those same two instruments in whole (rows 9 and 10). Asserted, the two halves separately: reg 3(2)'s names in `cbr-tests-reg3.l4`, the revocation in `cbr-tests-reg4.l4`.
20. The Table in regulation 4 has 13 rows: rows 1 to 4, 9 and 10 are revoked in whole, and rows 5 to 8 and 11 to 13 in part. Asserted.
21. Nothing in the text puts a duty or a penalty on the person: every operative paragraph fixes what is payable.

## What the stable binary does not accept

Observed on the stable binary (1.6.98), with a one-line probe each:

- `REFUSE` is not defined: "I could not find a definition for the identifier REFUSE". Not covered is therefore `NOTHING` in a `MAYBE` result; no `#ASSERT REFUSED` is used.
- `YMD` is not defined: "I could not find a definition for the identifier YMD". Dates are `Date d m y` (day first), with `IMPORT daydate`.
- Comparing two dates without `IMPORT daydate` fails with "There are multiple definitions for the identifier `__LT__`"; with the import it checks.
- `BECAUSE` after an `#ASSERT` is a parse error.

Named by the brief and the dialect notes as not available on main, and avoided without a probe: section-level `GIVEN`, `TYPICALLY`, and sets.
Not an error here but followed anyway, because the brief says so: every `NOT` is parenthesised (a bare `NOT a` on a variable checked), every `#ASSERT` is on one line, and arithmetic is bracketed across line breaks.
Followed because the stable binary needs them: names with parentheses, commas, apostrophes and periods are backticked; record constructors are backticked (`` `Type` OF ... `` and `` `Type` WITH ``); a function argument that is a genitive is parenthesised; `IMPORT` finds only modules in the importing file's folder, so layer 2 lives beside layer 1.

## What check.sh prints

Run from the encoding folder as `L4=<stable l4> L4_TARGET=unstable ./check.sh`.
Exit code 0.
Stderr:

```
check.sh: the target is unstable, so the main check was skipped.
```

Stdout:

```
module                                    errors satisfied  failed  refused  expected
cbr-cases-seat.l4                              0        83       0        0         0
cbr-nouns.l4                                   0         0       0        0         0
cbr-reg1.l4                                    0         0       0        0         0
cbr-reg2-benefits.l4                           0         0       0        0         0
cbr-reg2-couples.l4                            0         0       0        0         0
cbr-reg2-rate.l4                               0         0       0        0         0
cbr-reg3.l4                                    0         0       0        0         0
cbr-reg4.l4                                    0         0       0        0         0
cbr-seat.l4                                    0         0       0        0         0
cbr-tests-reg1.l4                              0        20       0        0         0
cbr-tests-reg2-benefits.l4                     0        32       0        0         0
cbr-tests-reg2-couples.l4                      0        26       0        0         0
cbr-tests-reg2-rate.l4                         0        61       0        0         0
cbr-tests-reg3.l4                              0        16       0        0         0
cbr-tests-reg4.l4                              0        23       0        0         0
TOTAL (15 modules)                             0       261       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
```

Each case file ends with assertions written equal to assertions satisfied (83 of 83 in the seat cases; 178 of 178 in the layer-1 tests).
`python3 -I srcrefs.py check --refs ../../registers/source-bundle/uksi-2006-965.txt cbr-*.l4` printed: `srcrefs check: 143 src: lines, 38 runs, 48 locators, 0 problems`.
`l4 check` over each of the 15 files printed no warning.
All expected values are written by hand from the text, with the reason beside each.
As a check on the tests themselves, fourteen one-line mutations of the layer-1 modules were each caught by at least one assertion: a reversed date comparison, a dropped carve-out in (4)(b), (5) no longer giving the rate back, a wrong figure (both), the version gate dropped, reg 3 always taking the earlier amount, (6)(b) reading the wrong Act, the reg 1(2)(b) limb reading the SSCBA flag, (2)(a)(iii) "or" for "and", a tie returning the elder, (4)(a) ignored, and entitlement ignored in either of two places.

## Before this is worth relying on

- No lawyer has read this, and nothing was checked against the official text, only against the converter's rendering of it.
- The figures are those of the version of 6 April 2026. They are stale after the next uprating, and every earlier week returns NOTHING. A later version needs a new `the date of the version of the text encoded` and new figures.
- Entitlement to child benefit, "child", the Part 9 meaning of "qualifying young person", the Schedule 4 increases and the earlier 1976 amount all live in instruments that are not encoded. A user must answer them correctly, and the encoding cannot catch a wrong answer.
- F1, F2 and F15 change amounts for households with a couple, a parent in the house, or a specified benefit, and the text does not settle them. A reviewer who reads (5) or (2) the other way changes the assertions marked FORK in `cbr-tests-reg2-rate.l4` and `cbr-cases-seat.l4`.
- The couples rule takes the eldest candidate child of the other persons as one date (F4). A household of three or more adults with children of several ages is only as good as that reading.
- Reg 3 compares amounts the text does not give. It is correct only if the earlier amount is entered correctly, and only for the transitional provisions and savings of the 1998 Amendment Regulations.

## Checked after the run

This section was added by the session that ran the agent, after the run; the sections above are the agent's.

- `L4=<L4_BIN> L4_MAIN=<L4_BIN> ./check.sh` in this folder, with `JL4_LIBRARY_PATH` unset, on the stable `l4` 1.6.98 (main, 7689b0d, 2026-10-19): `TOTAL (15 modules) 0 261 0 0 | 0 261 0 0`; exit status 0; every main column reads `same`.
  The build written with and the main build compared with are the same build, so the main columns are a second run of one compiler, not a comparison between two.
  The agent ran `check.sh` with `L4_TARGET=unstable`, as its brief said, so the output printed above under "What check.sh prints" is from that run.
- `srcrefs.py check --refs` against `../../registers/source-bundle/uksi-2006-965.txt`: `srcrefs check: 143 src: lines, 38 runs, 48 locators, 0 problems`.
- `srcrefs.py check --strict`: `srcrefs check: 143 src: lines, 38 runs, 48 locators, 0 problems`. These findings are counted here and have not been reviewed one by one.
- 13 `@export` seat questions; 42 coverage rows (18 encoded, 13 fork, 11 inert, 0 repealed or blank).
- Paths in the agent's files that named its run folder (`inputs/...`) were rewritten on copying to name the deposited text in `../../registers/source-bundle/`; the agent's brief is kept verbatim as `BRIEF.md`, and the paths in it are the run's own.
