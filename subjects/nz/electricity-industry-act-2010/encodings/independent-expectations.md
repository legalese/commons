# Independent expectations: Electricity Industry Act 2010 (supply, disputes, enforcement)

Written from BRIEF.md and the source text (as at 30 March 2025) before any `.l4` file was opened.
Working days follow the Legislation Act 2019, s 13 ("working day means a day of a week other than a Saturday, a Sunday, Waitangi Day, Good Friday, Easter Monday, Anzac Day, the Sovereign's birthday, Te Ra Aro ki a Matariki/Matariki Observance Day, and Labour Day; ... a day in the period commencing with 25 December in a year and ending with 2 January in the following year; ... if 1 January falls on a Friday, the following Monday; ... if Waitangi Day or Anzac Day falls on a Saturday or a Sunday, the following Monday").
Dates used: Labour Day 2026 = Mon 26 Oct 2026; Matariki 2026 = Fri 10 Jul 2026; King's Birthday 2026 = Mon 1 Jun 2026; Good Friday / Easter Monday 2027 = 26 / 29 Mar 2027; 1 Jan 2027 is a Friday so Mon 4 Jan 2027 is not a working day; Waitangi Day 2027 is Sat 6 Feb so Mon 8 Feb 2027 is not a working day; Anzac Day 2027 is Sun 25 Apr so Mon 26 Apr 2027 is not a working day.

Once the encoding was opened, no expected value below was changed. Only the "Status" column/notes about expressibility were added afterwards.

## Goal 1: supply obligation (ss 105-107)

s 105(1): "This section applies to a distributor who, in relation to any place, (a) is, immediately before the repeal ... of section 62 of the Electricity Act 1992, prohibited from ceasing to supply ... ; or (b) is the successor in business to a distributor referred to in paragraph (a)."
s 105(2): "must ... either (a) supply line function services ... or (b) supply the place with electricity from an alternative source."
s 105(3): "subject to anything to the contrary in the Electricity Act 1992, any regulations made under section 169 of that Act, or any written agreement, entered into before this section comes into force, between the distributor and a landowner".
s 106(1): "comes to an end ... if (a) the landowner and (if the landowner is not the consumer) the consumer, or the Minister, agree in writing ...; or (b) the obligation is assigned to, or assumed by, a successor in business".
s 106(2): "suspended ... (a) ... ceased as a result of circumstances beyond the control of the distributor ...: (b) ... needs to cease for reasons of safety or in order to carry out maintenance or upgrading work: (c) the distributor, or a retailer, is entitled to cease supply ... because of a failure to pay money due".
s 106(3): "the cessation may continue only for as long as the reason for cessation continues."

| id | inputs | expected | provision |
|---|---|---|---|
| S01 | distributor was prohibited under old s 62 for the place; nothing else | obligation applies and is in force (must supply) | s 105(1)(a), (2) |
| S02 | distributor is successor in business to such a distributor | obligation applies | s 105(1)(b) |
| S03 | neither (a) nor (b) | s 105 does not apply; no obligation | s 105(1) |
| S04 | applies; landowner is also consumer; landowner agrees in writing to end | obligation ended | s 106(1)(a) |
| S05 | applies; landowner is not the consumer; landowner agrees in writing, consumer does not | obligation NOT ended (still must supply) | s 106(1)(a) "the landowner and (if the landowner is not the consumer) the consumer" |
| S06 | applies; landowner not consumer; both agree in writing | ended | s 106(1)(a) |
| S07 | applies; Minister agrees in writing (no landowner/consumer agreement) | ended | s 106(1)(a) "or the Minister" |
| S08 | applies; landowner and consumer agree orally only | not ended | s 106(1)(a) "agree in writing" |
| S09 | applies; obligation assigned to a successor in business | ended (for this distributor) | s 106(1)(b) |
| S10 | applies; supply ceased due to earthquake, reason continuing | suspended | s 106(2)(a) |
| S11 | applies; supply needs to cease for maintenance, maintenance continuing | suspended | s 106(2)(b) |
| S12 | applies; retailer entitled to cease for non-payment, still unpaid | suspended | s 106(2)(c) |
| S13 | applies; maintenance reason has ended | not suspended (must supply) | s 106(3) "only for as long as the reason for cessation continues" |
| S14 | applies; pre-commencement written agreement with landowner to the contrary | obligation does not bind (displaced by the agreement) | s 105(3) |
| S15 | applies; written agreement to the contrary entered into AFTER s 105 came into force (not a s 106(1)(a) agreement) | obligation still applies | s 105(3) "entered into before this section comes into force" |
| S16 | applies; supply via line function services (network) | obligation met | s 105(2)(a) |
| S17 | applies; supply via alternative source | obligation met | s 105(2)(b) |

s 105(4) offence: "commits an offence, and is liable on conviction to a fine not exceeding $10,000 and to a further fine not exceeding $1,000 for every day or part of a day during which the offence continues, if the distributor, (a) having been made aware that supply to the place has ceased in the circumstances described in section 106(2)(a), fails to resume supply as soon as is reasonable in the circumstances; or (b) knowingly ceases to supply ... other than in the circumstances described in section 106(2)(b) or (c)."

Reading taken: the "further fine" is $1,000 multiplied by the number of days (or parts of days) during which the offence continues, given as an input N. Ambiguity: whether the first day of the offence is itself a day "during which the offence continues"; I take N as given and do not add or subtract a day.

| id | inputs | expected | provision |
|---|---|---|---|
| S18 | obliged; ceased by storm (106(2)(a)); distributor made aware; failed to resume as soon as reasonable | offence (limb a) | s 105(4)(a) |
| S19 | obliged; ceased by storm; made aware; resumed as soon as reasonable | no offence | s 105(4)(a) |
| S20 | obliged; ceased by storm; NOT made aware; not resumed | no offence under (a) | s 105(4)(a) "having been made aware" |
| S21 | obliged; distributor knowingly ceases supply for no permitted reason | offence (limb b) | s 105(4)(b) |
| S22 | obliged; knowingly ceases for safety/maintenance (106(2)(b)) | no offence | s 105(4)(b) "other than ... 106(2)(b)" |
| S23 | obliged; knowingly ceases for non-payment (106(2)(c)) | no offence | s 105(4)(b) "or (c)" |
| S24 | obliged; ceases but not knowingly (and not 106(2)(a)) | no offence | s 105(4)(b) "knowingly" |
| S25 | obligation has ended under s 106(1) (Minister agreed in writing); distributor knowingly ceases | no offence (not "obliged under subsection (2)") | s 105(4) opening words, s 106(1) |
| S26 | offence, continues 0 further days | max fine $10,000 | s 105(4) |
| S27 | offence continues 10 days | max $20,000 | s 105(4) |
| S28 | offence continues 365 days | max $375,000 | s 105(4) |
| S29 | no offence | no fine (0 or not applicable) — the Act imposes none | s 105(4) |

s 107(1): "must give at least 6 months' notice of the proposal to (a) every consumer affected ...; and (b) if the landowner is not the consumer, the landowner; and (c) every retailer who supplies electricity to the place; and (d) the public in the district". s 107(3): "If the distributor is unable to locate a landowner ... after taking reasonable steps ... not required to give notice to the landowner".

Reading taken on "6 months' notice": the notice period is a period of months under Legislation Act s 56, starting the day after notice is given (s 54 / the s 56 example "3 months after the date on which notice is sent ... starts on 3 August ... ends at the close of 2 November"); the alternative supply may start on the day after the period ends. So notice on 1 Jan 2026 runs 2 Jan to close of 1 Jul 2026; earliest start 2 Jul 2026. AMBIGUOUS: a reading counting from the notice day itself would allow 1 Jul 2026. The Act also does not say what event the 6 months must precede; I take it to be the start of supply from the alternative source.

| id | inputs | expected | provision |
|---|---|---|---|
| S30 | notice given 1 Jan 2026; alt supply to start 1 Jan 2027 | notice sufficient | s 107(1) |
| S31 | notice 1 Jan 2026; start 1 Jun 2026 | insufficient | s 107(1) |
| S32 | notice 1 Jan 2026; start 2 Jul 2026 | sufficient | s 107(1), LA s 56 |
| S33 | notice 1 Jan 2026; start 1 Jul 2026 | insufficient (my reading; ambiguous boundary) | s 107(1), LA ss 54, 56 |
| S34 | notice 31 Aug 2026; start 1 Mar 2027 | sufficient (period 1 Sep 2026 to close of 28 Feb 2027) | LA s 56(c) |
| S35 | notice 31 Aug 2026; start 28 Feb 2027 | insufficient | LA s 56 |
| S36 | 6+ months; notice given to consumers, retailers and public, but landowner (not the consumer, locatable) not notified | non-compliant | s 107(1)(b) |
| S37 | as S36 but landowner could not be located after reasonable steps | compliant | s 107(3) |
| S38 | 6+ months; landowner is the consumer; consumer, retailers, public notified | compliant | s 107(1)(b) "if the landowner is not the consumer" |
| S39 | 6+ months; public not notified | non-compliant | s 107(1)(d) |
| S40 | 6+ months; a retailer supplying the place not notified | non-compliant | s 107(1)(c) |

## Goal 2: disputes (ss 95-96)

s 95(1): "may make a complaint ... concerning Transpower (except in its capacity as system operator) or any distributor or retailer." s 95(2): "any persons (including consumers, potential consumers, and owners and occupiers of land) except members of the dispute resolution scheme."
s 96(1): "Transpower (other than in its capacity as system operator), and every distributor and retailer, must be a member ... unless exempt under subsection (3)." s 96(2): "knowingly refuses or fails to become a member ... fine not exceeding $100,000". s 96(3): "(a) ... a class of industry participants identified in regulations made under section 111 ...; or (b) the Minister of Consumer Affairs exempts the person by issuing an individual exemption notice in the Gazette that (i) identifies the person ...; and (ii) gives reasons".

| id | inputs | expected | provision |
|---|---|---|---|
| D01 | consumer complains about a retailer | may complain | s 95(1),(2) |
| D02 | potential consumer complains about a distributor | may complain | s 95(2) |
| D03 | landowner (non-member) complains about Transpower (not as system operator) | may complain | s 95 |
| D04 | consumer complains about Transpower in its capacity as system operator | may not | s 95(1) "except in its capacity as system operator" |
| D05 | consumer complains about a generator (not distributor/retailer/Transpower) | may not (scheme is "concerning" only those) | s 95(1) |
| D06 | a retailer that is a scheme member complains about a distributor | may not | s 95(2) "except members" |
| D07 | a retailer exempt and not a member complains about a distributor | may complain | s 95(2) |
| D08 | occupier of land complains about a distributor | may complain | s 95(2) |
| D09 | distributor, not exempt | must be member | s 96(1) |
| D10 | retailer, not exempt | must be member | s 96(1) |
| D11 | Transpower (other than as system operator) | must be member | s 96(1) |
| D12 | generator only (not distributor/retailer/Transpower) | not required | s 96(1) |
| D13 | retailer in a class exempted by s 111 regulations | not required | s 96(3)(a) |
| D14 | distributor with Gazette notice identifying it and giving reasons | not required | s 96(3)(b) |
| D15 | distributor with Gazette notice that gives no reasons | required (no valid exemption) | s 96(3)(b)(ii) |
| D16 | distributor exempted by an instrument not published in the Gazette | required | s 96(3)(b) "notice in the Gazette" |
| D17 | required; knowingly fails to become member | offence, max fine $100,000 | s 96(2) |
| D18 | required; fails but not knowingly | no offence | s 96(2) "knowingly" |
| D19 | required; is a member | no offence | s 96(2) |
| D20 | exempt; knowingly does not join | no offence (my reading: s 96(2) is read with (1); an exempt person "need not be a member") | s 96(2),(3). Ambiguous on its face: s 96(2) says "A person"; read with (1). |

## Goal 3: enforcement (ss 52, 54, 66, 80)

s 52(1): "may not exercise its powers ... if the breach (a) was discovered, or ought reasonably to have been discovered, more than 3 years before the exercise of the power; or (b) occurred more than 10 years before". s 52(2): "once the Authority has exercised a power in relation to the breach ..., the limitations in subsection (1) do not apply."
Reading taken: "more than 3 years before" means the exercise date is later than the third anniversary of discovery; exercise on the anniversary itself is allowed. For an anniversary that does not exist (29 Feb), I take the last day of the month (28 Feb), by analogy with LA s 56(c). The relevant discovery date is the earlier of actual and constructive discovery.

| id | inputs | expected | provision |
|---|---|---|---|
| E01 | breach 1 Mar 2024, discovered 1 Mar 2024, exercise 16 Oct 2026 | may act | s 52(1) |
| E02 | breach and discovery 1 Mar 2023, exercise 1 Mar 2026 | may act (exactly 3 years is not "more than") | s 52(1)(a) |
| E03 | breach and discovery 1 Mar 2023, exercise 2 Mar 2026 | barred | s 52(1)(a) |
| E04 | breach 1 Jun 2016, discovered 1 Jan 2025, exercise 1 Jun 2026 | may act (exactly 10 years) | s 52(1)(b) |
| E05 | breach 1 Jun 2016, discovered 1 Jan 2025, exercise 2 Jun 2026 | barred (10 years) | s 52(1)(b) |
| E06 | breach 1 Jan 2015, discovered 1 Jan 2025, exercise 16 Oct 2026 | barred by (b) though (a) is met | s 52(1)(b) |
| E07 | breach 1 Jan 2023, actually discovered 1 Jan 2025, ought reasonably to have been discovered 1 Feb 2023; exercise 16 Oct 2026 | barred | s 52(1)(a) "or ought reasonably to have been discovered" |
| E08 | breach and discovery 29 Feb 2024, exercise 28 Feb 2027 | may act | s 52(1)(a) (reading as above) |
| E09 | breach and discovery 29 Feb 2024, exercise 1 Mar 2027 | barred (ambiguous anniversary; reading as above) | s 52(1)(a) |
| E10 | as E06 but Authority has already exercised a power in relation to the breach | may act | s 52(2) |
| E11 | as E03 but already exercised a power | may act | s 52(2) |

s 54(1)(d): "a pecuniary penalty ... not exceeding $2 million and a further amount not exceeding $10,000 for every day or part of a day during which the breach continues". s 54(3): "Two or more breaches relating to one event or series of closely related events arising from the same cause or circumstance must be treated as a single breach."

| id | inputs | expected | provision |
|---|---|---|---|
| E12 | one breach, continues 0 days | max $2,000,000 | s 54(1)(d) |
| E13 | continues 1 day | max $2,010,000 | s 54(1)(d) |
| E14 | continues 30 days | max $2,300,000 | s 54(1)(d) |
| E15 | continues 365 days | max $5,650,000 | s 54(1)(d) |
| E16 | 3 breaches arising from one event (same cause), continuing 0 days | treated as one breach; max $2,000,000 | s 54(3) |
| E17 | 3 unrelated breaches | 3 breaches (each subject to its own s 54(1)(d) maximum) | s 54(3) a contrario |

s 80(2): individual "must not ... exceed $500,000 in respect of each act or omission". s 80(3): body corporate "the greater of (a) $10 million; or (b) either, (i) if it can be readily ascertained and if the court is satisfied that the contravention occurred in the course of producing a commercial gain, 3 times the value of any commercial gain ...; or (ii) if the commercial gain cannot be readily ascertained, 10% of the turnover of the body corporate and all of its interconnected bodies corporate".
Reading taken: where the gain is readily ascertainable but the court is not satisfied it occurred in the course of producing a commercial gain, neither (b)(i) nor (b)(ii) applies, so the cap is $10 million.

| id | inputs | expected | provision |
|---|---|---|---|
| E18 | individual | max $500,000 | s 80(2) |
| E19 | individual with $5m gain | still $500,000 | s 80(2) |
| E20 | body corporate, gain readily ascertained $5,000,000, in course of commercial gain | $15,000,000 | s 80(3)(b)(i) |
| E21 | body corporate, gain ascertained $2,000,000, in course of commercial gain | $10,000,000 (greater of $10m and $6m) | s 80(3)(a) |
| E22 | body corporate, gain ascertained exactly $3,333,333 | $10,000,000 ($9,999,999 < $10m) | s 80(3) |
| E23 | body corporate, gain not ascertainable, turnover (incl. interconnected) $200,000,000 | $20,000,000 | s 80(3)(b)(ii) |
| E24 | body corporate, gain not ascertainable, turnover $50,000,000 | $10,000,000 | s 80(3)(a) |
| E25 | body corporate, gain ascertainable $8m but court not satisfied it was in course of commercial gain, turnover $500m | $10,000,000 | s 80(3)(b)(i) condition unmet, (ii) inapplicable |
| E26 | body corporate, gain not ascertainable, turnover $100,000,000 | $10,000,000 (equal) | s 80(3) |

s 66: "notice of appeal within 20 working days after the date of the decision or order appealed against or within any further time that the High Court allows." Day of decision excluded (LA s 54, "after"); deadline is the 20th working day.

| id | inputs | expected deadline | provision |
|---|---|---|---|
| E27 | decision Thu 1 Oct 2026 (Labour Day 26 Oct in range) | Fri 30 Oct 2026 | s 66; LA s 13 |
| E28 | decision Fri 16 Oct 2026 | Mon 16 Nov 2026 | s 66 |
| E29 | decision Sat 17 Oct 2026 | Mon 16 Nov 2026 | s 66 |
| E30 | decision Fri 26 Jun 2026 (Matariki 10 Jul in range) | Mon 27 Jul 2026 | s 66; LA s 13 |
| E31 | decision Wed 1 Jul 2026 | Thu 30 Jul 2026 | s 66 |
| E32 | decision Mon 1 Jun 2026 (King's Birthday, itself) | Mon 29 Jun 2026 | s 66 |
| E33 | decision Tue 1 Dec 2026 (Christmas break and Mon 4 Jan 2027) | Thu 7 Jan 2027 | LA s 13 (b),(c) |
| E34 | decision Thu 10 Dec 2026 | Mon 18 Jan 2027 | LA s 13 |
| E35 | decision Fri 18 Dec 2026 | Tue 26 Jan 2027 | LA s 13 |
| E36 | decision Fri 15 Jan 2027 (Waitangi Sat 6 Feb, so Mon 8 Feb out) | Mon 15 Feb 2027 | LA s 13 (e) |
| E37 | decision Wed 10 Mar 2027 (Good Friday 26 Mar, Easter Monday 29 Mar) | Fri 9 Apr 2027 | LA s 13 |
| E38 | decision Mon 12 Apr 2027 (Anzac Sun 25 Apr, so Mon 26 Apr out) | Tue 11 May 2027 | LA s 13 (e) |
| E39 | decision Wed 24 Dec 2025 (1 Jan 2026 is a Thursday, no extra day) | Fri 30 Jan 2026 | LA s 13 |
| E40 | decision 1 Oct 2026, notice filed 30 Oct 2026 | in time | s 66 |
| E41 | decision 1 Oct 2026, notice filed 2 Nov 2026, no extension | out of time | s 66 |
| E42 | as E41 but High Court allowed further time | in time (not expressible as a date unless the extension is an input) | s 66 "within any further time that the High Court allows" |

## Not (yet) expressible / judgement items

- Whether a cessation was "beyond the control of the distributor", whether resumption was "as soon as is reasonable", whether the gain "can be readily ascertained", and whether the breach "ought reasonably to have been discovered" earlier are evaluative questions: they can only be inputs.
- The content requirements of the s 107(2) and (4) notices (outline, reasonable comment period, newspaper) are evaluative; tested only as a single "given" if at all.
- The s 56 matters the Rulings Panel must consider when setting the amount are discretion; only the maximum is testable.
- The extent of any High Court extension under s 66 is not computable.

## Status after opening the encoding (expected values above unchanged)

Not expressible with the encoding's inputs (no test written):
- S05, S08: s 106(1)(a) is a single boolean "ending agreed in writing by the landowner, consumer or Minister", so a landowner-only or oral agreement cannot be put.
- S16, S17: no input for the mode of supply (network or alternative source).
- S20: no input for whether the distributor was "made aware"; the field is "resumed as soon as reasonable after learning of it".
- S29: the s 105(4) fine function takes only the days and not whether an offence was committed.
- S36-S40: no input for who was notified under s 107(1)(a)-(d) or s 107(3); only the notice date.
- D15, D16: the Gazette exemption is one boolean; the identify/give-reasons requirements of s 96(3)(b) cannot be put.
- E16, E17: s 54(3) has no input (no number of breaches or relatedness).
- E25: no input for whether the court is satisfied the contravention occurred "in the course of producing a commercial gain"; giving JUST 8m would yield $24m, against the expected $10m.
- E42: no input for a High Court extension under s 66.
