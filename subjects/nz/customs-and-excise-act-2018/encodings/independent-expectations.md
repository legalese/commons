# Independent expectations: Customs and Excise Act 2018 (NZ), value, duty, penalties, refunds

Written from the Act (as at 4 September 2026) and the Legislation Act 2019 s 13, 54, 55 only,
before any `.l4` file was opened. Expected values are fixed; they are not to be changed after the
encoding is read.

## Working-day calendar I rely on (Legislation Act 2019 s 13 "working day")

"a day of a week other than— a Saturday, a Sunday, Waitangi Day, Good Friday, Easter Monday, Anzac
Day, the Sovereign's birthday, ... Matariki Observance Day, and Labour Day; and a day in the period
commencing with 25 December in a year and ending with 2 January in the following year; and if
1 January falls on a Friday, the following Monday; and if 1 January falls on a Saturday or a Sunday,
the following Monday and Tuesday; and if Waitangi Day or Anzac Day falls on a Saturday or a Sunday,
the following Monday".

Non-working weekdays used: 2026: Fri 6 Feb (Waitangi), Fri 3 Apr, Mon 6 Apr (Easter), Mon 27 Apr
(Anzac Sat 25 Apr, Mondayised), Mon 1 Jun (King's Birthday), Fri 10 Jul (Matariki), Mon 26 Oct
(Labour), 25 Dec 2026 - 2 Jan 2027, Mon 4 Jan 2027 (1 Jan 2027 is Friday). 2027: Mon 8 Feb (Waitangi
Sat), Fri 26 Mar, Mon 29 Mar (Easter), Mon 26 Apr (Anzac Sun), Mon 7 Jun, Fri 25 Jun (Matariki),
Mon 25 Oct, 25 Dec 2027 - 2 Jan 2028, Mon 3 and Tue 4 Jan 2028 (1 Jan 2028 Saturday).

"Within 20 working days after the date on which X": the day X is not counted (Legislation Act
s 54, item "after"); the period ends at the close of the 20th working day after X. "Within 4 years
after the duty has been paid": starts the day after payment and ends at the close of the
anniversary date four years on (s 54; by analogy with s 56's month rule); s 55 extends a thing
"done within a limited period" to the next working day if the last day is not a working day.

## Goal 1: Customs value (Schedule 4)

### Related persons, cl 2(2)(a) — "persons are related if—"

| id | inputs | expected | words relied on |
|---|---|---|---|
| R1 | officers or directors of one another's business; nothing else | related | "they are officers or directors of one another's business" |
| R2 | legally recognised partners in business | related | "they are legally recognised partners in business" |
| R3 | employer and employee | related | "they are employer and employee" |
| R4 | a person holds exactly 5% of the voting shares of each | related | "holds 5% or more of the outstanding voting stock or shares of both of them" |
| R5 | a person holds 4.99% of one and 60% of the other; no other limb | not related | "5% or more ... of both of them" — 4.99% of one fails |
| R6 | a person holds 5% of one and 5% of the other but via indirect holdings | related | "directly or indirectly owns, controls, or holds" |
| R7 | one controls the other | related | "one of them directly or indirectly controls the other" |
| R8 | both controlled by a third person | related | "both of them are directly or indirectly controlled by a third person" |
| R9 | together they control a third person | related | "together they directly or indirectly control a third person" |
| R10 | members of the same family (blood relationship within 4th degree, e.g. cousins) | related | cl 2(2)(a) "they are members of the same family"; (b) "connected by a blood relationship within the fourth degree" |
| R11 | blood relationship of the 5th degree only | not related | "within the fourth degree" |
| R12 | married / civil union / de facto | related | (b) "married to, or in a civil union or a de facto relationship with, one another" |
| R13 | one married to a person within 4th degree of the other (in-law) | related | (b) "one of them is married to ... a person who is within the fourth degree of relationship to the other" |
| R14 | one adopted as child of the other | related | (b) "one has been adopted as the child of— the other" |
| R15 | one adopted as child of a person within 3rd degree of the other | related | (b) "a person who is within the third degree of relationship to the other" |
| R16 | none of the limbs | not related | — |

Note: the family limb degree counting (civil-law vs canon-law) is not stated; I treat degree as an
input fact.

### Clause 5 — when the transaction value can be used

Base case B5: no restrictions, no unvaluable condition, no proceeds accrue to seller, not related.

| id | inputs | expected | words |
|---|---|---|---|
| C1 | B5 | transaction value usable | cl 5 all limbs met |
| C2 | restriction on disposition/use that is imposed by law | usable | "(a) ... other than restrictions that— are imposed by law" |
| C3 | restriction limiting geographic resale area | usable | "limit the geographical area in which the goods may be resold" |
| C4 | restriction that does not substantially affect value | usable | "do not substantially affect the value of the goods" |
| C5 | other restriction (substantially affects value, not law, not geographic) | not usable | "there are no restrictions respecting the disposition or use" |
| C6 | sale subject to a condition whose value cannot be determined | not usable | "(b) neither the sale ... nor the price ... is subject to some condition or consideration in respect of which a value cannot be determined" |
| C7 | condition exists but its value can be determined | usable | same, negative |
| C8 | proceeds accrue to seller, price includes them or can be adjusted under cl 7 | usable | "(c) ... includes the value of that part of the proceeds or can be adjusted in accordance with clause 7" |
| C9 | proceeds accrue to seller, neither included nor adjustable | not usable | (c) |
| C10 | related, chief executive does not require cl 6 | usable | "(d) ... or, if they are related at that time, the importer complies with clause 6 if required" |
| C11 | related, CE requires cl 6, importer complies | usable | (d) |
| C12 | related, CE requires cl 6, importer does not comply | not usable | (d) |

### Clause 7 — transaction value

| id | inputs | expected | words |
|---|---|---|---|
| T1 | price 10,000, nothing else | 10,000 | 7(a) "taking the price paid or payable" |
| T2 | price 10,000 + commission (not buying) 500 not in price, sufficient info | 10,500 | 7(b)(i) "commissions and brokerage ... incurred by the buyer" |
| T3 | price 10,000; buying commission (buyer's agent overseas) 300 | 10,000 | 7(b)(i) "other than fees paid ... to the buyer's agent for the service of representing the buyer overseas" |
| T4 | price 10,000 + packing 200 not in price | 10,200 | 7(b)(ii) packing costs |
| T5 | price 10,000 + assist (moulds) 1,000 | 11,000 | 7(b)(iii) "tools, dies, moulds" |
| T6 | price 10,000 + royalty 400 that is a condition of sale | 10,400 | 7(b)(iv) "royalties and licence fees ... as a condition of the sale" |
| T7 | price 10,000 + royalty 400 not a condition of sale | 10,000 | 7(b)(iv) |
| T8 | price 10,000 + proceeds to seller 250 | 10,250 | 7(b)(v) |
| T9 | price 10,000 + repair materials/service 150 | 10,150 | 7(b)(vi) |
| T10 | price 10,000 + transport to leaving export country 600, paid to seller as condition | 10,600 | 7(b)(vii) "until the goods have left the country of export if ... paid or payable by the buyer ... to or for the benefit of the seller as a condition of the transaction" |
| T11 | price 10,000; amount already included in price (packing 200 included) | 10,000 | 7(b) "to the extent that each amount is not included in the price" |
| T12 | price 12,000 includes international freight & insurance after leaving export country 1,500 | 10,500 | 7(c)(i) |
| T13 | price 12,000 includes post-import assembly 800, separately identified | 11,200 | 7(c)(ii)(A) "if ... identified separately" |
| T14 | as T13 but not separately identified | 12,000 | 7(c)(ii) "if the cost ... is identified separately" |
| T15 | price 12,000 includes NZ inland transport 300 separately identified | 11,700 | 7(c)(ii)(B) |
| T16 | price 12,000 includes NZ duties/taxes 900 separately identified | 11,100 | 7(c)(ii)(C) |
| T17 | carrier media price 5,000 of which data value 4,000, distinguished, not in data-processing equipment | 1,000 | 7(d) |
| T18 | as T17 but data not distinguished | 5,000 | 7(d)(i) |
| T19 | as T17 but incorporated in data processing equipment | 5,000 | 7(d)(ii) |
| T20 | combined: price 10,000 + commission 500 + packing 200 + royalty 400 (condition) − international freight 1,000 (included) | 10,100 | cl 7(a)-(c) |
| T21 | interest 700 included in price, distinguished, actually sold at declared price, buyer demonstrates writing and rate not exceeding prevailing | value excludes interest (price 10,700 → 10,000) | cl 3 "is not to be regarded as part of the Customs value if—" |
| T22 | as T21 but interest not distinguished | interest stays in (10,700) | cl 3(a) |
| T23 | as T21 but rate exceeds prevailing level | interest stays in (10,700) | cl 3(c)(ii) |
| T24 | as T21 but not in writing | stays in (10,700) | cl 3(c)(i) |
| T25 | an addition required (e.g. royalty) lacks sufficient information | transaction value cannot be used; fall to method 2 | cl 4(2)(b) "an adjustment that is required to be made under clause 7(b), (c), or (d) cannot be made because of a lack of sufficient information" with cl 4(3). Ambiguity: cl 4(3) is "may" and "opinion of the chief executive"; I take the lack of information as leading to methods 2-6. |

Ambiguity on T21: cl 3 says interest "is not to be regarded as part of the Customs value"; it does
not say interest is deducted from the price. I read it as: if interest is in the declared price and
the conditions are met it is excluded; otherwise it stays.

### Methods 2 and 3 (cls 9-12) and the overall Customs value

| id | inputs | expected | words |
|---|---|---|---|
| M1 | cl 5 met, price 10,000 | Customs value 10,000 (method 1) | cl 4(1) "primary basis ... is the transaction value" |
| M2 | cl 5 not met; identical TVs (same level & qty) 9,800, 9,500, 10,200 | 9,500 | cl 9(2) "lowest such transaction value" |
| M3 | cl 5 not met; one identical TV 9,800 adjusted +200 for transport distance | 10,000 | cl 9(1)(b) adjustments, lowest "determined after ... adjusted" |
| M4 | cl 5 not met; identical TVs 9,800 (adj +500 → 10,300) and 10,000 (adj −100 → 9,900) | 9,900 | cl 9(2) lowest after adjustment |
| M5 | cl 5 not met; no identical; similar TVs 9,000 and 8,700 | 8,700 | cl 11(2) |
| M6 | cl 5 not met; identical 11,000 and similar 8,000 | 11,000 (identical first) | cl 11 "cannot be determined under Parts 1 and 2" |
| M7 | cl 5 not met; no identical, no similar | not determinable here (methods 4-6 not encoded) → refuse | cl 4(3) sequential to methods 4-6 |
| M8 | cl 5 not met; no identical at same level/qty, identical at different level 9,600 (adjusted −100) | 9,500 | cl 10 |
| M9 | cl 5 not met; identical same-level 9,900 and different-level 9,000 | 9,900 (cl 9 before cl 10) | cl 10 applies only "if ... cannot be determined under clause 9" |
| M10 | identical goods by a different producer only, none by same producer | they count as identical | cl 2(3) |
| M11 | identical goods by same producer 10,000 and by different producer 9,000 | 10,000 | cl 2(3) "where there are no goods that were produced by ... the person who produced" |
| M12 | cl 5 met but chief executive doubts truth/accuracy and has sought explanation | may proceed to methods 2-6 | cl 4(2)(c), (4) |

## Goal 2: Duty and when it must be paid

### s 120 proportionate duty

| id | inputs | expected | words |
|---|---|---|---|
| D1 | rate 5% ad valorem; value 20,000 | 1,000 | s 120 "charged proportionately on a greater or smaller ... value" |
| D2 | rate $2.50 per litre; 1,000.5 litres | 2,501.25 | "proportionately on a greater or smaller quantity" (no rounding to whole units) |
| D3 | rate $3 per kg; 0.4 kg | 1.20 | same, smaller quantity |
| D4 | rate 0%, value 50,000 | 0 | — |

### Payment occasions and dates (ss 122-124)

| id | event / date | expected payment time | words |
|---|---|---|---|
| P1 | entered under s 75 and passed for home consumption on 2 Nov 2026 | 2 Nov 2026 (when) | s 122(a) "must be paid ... when ... the entry has been passed for home consumption" |
| P2 | entered for removal to a manufacturing area 5 Oct 2026 | 5 Oct 2026 | s 122(b) |
| P3 | wrongfully landed 20 Jan 2027 | 20 Jan 2027 | s 122(c) |
| P4 | offence committed 15 Apr 2027 | 15 Apr 2027 | s 122(d) |
| P5 | deferred payment authorised (s 123), deferred time expires 20 Jan 2027 | 20 Jan 2027 | s 123(1)(a), s 160(4) |
| P6 | s 112 amendment made 2 Nov 2026 | 30 Nov 2026 | s 124(2) "within 20 working days after the date on which the assessment is amended" |
| P7 | s 113 assessment notice given 27 Nov 2026 | 5 Jan 2027 (across Christmas/New Year and Mon 4 Jan 2027) | s 124(3) |
| P8 | s 114 notice 1 Dec 2026 | 7 Jan 2027 | s 124(4) |
| P9 | s 117 amendment notice 10 Dec 2026 | 18 Jan 2027 | s 124(5) |
| P10 | s 138(3) demand given 24 Dec 2026 | 1 Feb 2027 | s 124(6) |
| P11 | s 113 notice given 25 Dec 2026 (non-working) | 1 Feb 2027 | s 124(3); counting starts after 25 Dec |
| P12 | s 112 amendment 20 Mar 2026 (Easter 3-6 Apr) | 21 Apr 2026 | s 124(2) |
| P13 | s 117 notice 27 Mar 2026 (Easter and Anzac Mondayised 27 Apr) | 29 Apr 2026 | s 124(5) |
| P14 | s 113 notice 15 Jun 2026 (Matariki 10 Jul) | 14 Jul 2026 | s 124(3) |
| P15 | s 113 notice 29 May 2026 (King's Birthday 1 Jun) | 29 Jun 2026 | s 124(3) |
| P16 | s 113 notice 2 Feb 2026 (Waitangi Fri 6 Feb) | 3 Mar 2026 | s 124(3) |
| P17 | s 113 notice 1 Feb 2027 (Waitangi Sat → Mon 8 Feb) | 2 Mar 2027 | s 124(3) |
| P18 | s 113 notice 12 Oct 2026 (Labour Day 26 Oct) | 10 Nov 2026 | s 124(3) |
| P19 | s 112 amendment 30 Nov 2027 (1 Jan 2028 Sat → 3, 4 Jan off) | 6 Jan 2028 | s 124(2) |
| P20 | s 139(4) demand 23 Dec 2027 | 31 Jan 2028 | s 124(6) |
| P21 | s 113 notice 12 Jan 2027 (crosses Mon 8 Feb) | 10 Feb 2027 | s 124(3) |
| P22 | s 124(7) notice: earlier time specified 10 Nov 2026 for a s 113 duty otherwise due later | 10 Nov 2026 | s 124(7) "pay the duty within that earlier time" |
| P23 | 2 Nov 2026 → 20 WD | 30 Nov 2026 | plain 4 weeks, no holidays |

## Goal 3: Late payment penalties (ss 159-160)

Payment date (PD) per s 160. "Not fully paid ... before the close of the payment date" → 1% of
unpaid "as at the close of the payment date"; "not fully paid ... before the close of the seventh
day after the payment date" → further 4% of unpaid "as at the close of that seventh day". I read
"seventh day after" as calendar days (PD + 7) — the Act says "day", not "working day". I read the
4% base as duty only (the penalty is "of the amount of the duty still to be paid"), not
duty-plus-1%.

Base: s 113 duty 10,000, notice 2 Nov 2026 → PD 30 Nov 2026; 7th day 7 Dec 2026.

| id | inputs | expected penalty | words |
|---|---|---|---|
| L1 | paid in full on 30 Nov 2026 | 0 | "not fully paid ... before the close of the payment date" — paid on PD is before the close |
| L2 | nothing paid by 7 Dec 2026 | 100 + 400 = 500 | s 159(2), (4) |
| L3 | paid in full 1 Dec 2026 | 100 | s 159(2); 4% not triggered |
| L4 | paid in full 7 Dec 2026 | 100 | "before the close of the seventh day" |
| L5 | paid in full 8 Dec 2026 | 500 | s 159(3),(4) |
| L6 | 6,000 paid by 30 Nov, balance 4,000 paid 3 Dec | 40 | 1% of 4,000; nothing outstanding at close of 7th day |
| L7 | 6,000 paid by 30 Nov, nothing more by 7 Dec | 40 + 160 = 200 | 1% of 4,000 + 4% of 4,000 |
| L8 | nothing by 30 Nov, 7,000 by 7 Dec | 100 + 120 = 220 | 1% of 10,000 + 4% of 3,000 |
| L9 | 2,000 by 30 Nov, a further 5,000 by 7 Dec | 80 + 120 = 200 | 1% of 8,000 + 4% of 3,000 |
| L10 | s 122(a) duty (entry passed for home consumption), unpaid | no s 159 penalty (0 / not applicable) | s 160 provides only for cl 5(a) Sch 3, s 123(1), s 124(2)-(7) |
| L11 | s 123 deferred, PD 20 Jan 2027, duty 10,000 unpaid until 1 Mar 2027 | 500 | s 160(3), (4) |
| L12 | s 123 deferred, PD 20 Jan 2027, paid 27 Jan 2027 | 100 | 27 Jan is the 7th day |
| L13 | excise duty, Sch 3 cl 5(a) applies, prescribed time expires 15 Jun 2026, 10,000 unpaid | 500 | s 160(1), (2) |
| L14 | s 124(6) demand 24 Dec 2026 → PD 1 Feb 2027, duty 8,000 unpaid until 9 Feb 2027 | 80 + 320 = 400 | 7th day = 8 Feb 2027 (calendar, even though a non-working day) |
| L15 | as L14, paid in full 8 Feb 2027 | 80 | paid before close of the 7th day; reading: calendar 7th day; Mondayised Waitangi day does not shift it |
| L16 | s 124(7) earlier time 10 Nov 2026, duty 5,000 unpaid until 18 Nov 2026 | 50 + 200 = 250 | s 160(5),(6) "s 124(2) to (7)" |
| L17 | s 112 amendment (s 124(2)), duty 10,000 fully paid 1 Dec 2026 when PD is 30 Nov | 100 | s 160(5) |

Ambiguity: s 55 Legislation Act might let a payment due on a non-working payment date be made on
the next working day. Payment dates computed under s 124 always fall on working days, so only
deferred/excise dates can raise it; not tested.

## Goal 4: Refunds and appeals

### s 142 — "must, unless there is good reason not to, refund the duty— (a) at any time within 4 years after the duty has been paid; or (b) at any later time if an application is made within 4 years"

| id | inputs | expected | words |
|---|---|---|---|
| F1 | paid in error 15 May 2026, 1,200; refund considered 15 May 2030; no good reason | refund 1,200 | (a), last day of the 4 years |
| F2 | same, considered 16 May 2030, no application | no refund obligation (0) | (a) out of time, (b) no application |
| F3 | considered 2 Jun 2031, application made 15 May 2030 | refund 1,200 | (b) |
| F4 | considered 2 Jun 2031, application made 16 May 2030 | 0 | (b) application out of time |
| F5 | within time but good reason not to refund (obvious error in instrument) | 0 | "unless there is good reason not to"; s 142(2) |
| F6 | not paid in error | 0 | "If the chief executive is satisfied that duty has been paid in error" |
| F7 | error of law (not fact), within 4 years | refund | "either of law or of fact" |
| F8 | paid 16 Mar 2026, application Mon 18 Mar 2030 (16 Mar 2030 is Saturday) | refund (s 55 extension) | Legislation Act s 55 — ambiguous whether applied; my reading: yes |
| F9 | paid 29 Feb 2028, considered 29 Feb 2032 | refund | 2032 is a leap year; period ends close of 29 Feb 2032 |
| F10 | paid 15 May 2026, considered 1 Aug 2027 | refund | (a) |

### s 143 — provisional Customs value

| id | inputs | expected | words |
|---|---|---|---|
| V1 | provisional value under s 102(1), paid 5,000 on provisional, amended under s 112, final duty 4,200 | refund 800 | s 143(2) "refund the difference" |
| V2 | as V1, final duty 5,600 | no s 143 refund (0); 600 extra payable under s 124(2) | s 143(1)(d) "lower amount of duty" |
| V3 | as V1, final duty 5,000 | 0 | (d) not lower |
| V4 | not amended under s 112 yet | 0 / not applicable | (1)(c) |
| V5 | no provisional value | 0 / not applicable | (1)(a) |
| V6 | final value set by the chief executive under s 117 (not importer under s 112) | s 143 does not apply | (1)(c) "the importer subsequently amends ... under section 112" |

### Appeal / review periods (20 working days after notice of the decision)

| id | inputs | expected | words |
|---|---|---|---|
| A1 | s 142 decision notice 27 Nov 2026; last day | 5 Jan 2027 | s 142(3) "within 20 working days after the date on which notice of the decision is given" |
| A2 | s 142 notice 27 Nov 2026; appeal lodged 5 Jan 2027 | in time | s 142(3) |
| A3 | s 142 notice 27 Nov 2026; appeal lodged 6 Jan 2027 | out of time | s 142(3) |
| A4 | s 113 notice 2 Nov 2026; review or appeal by 30 Nov 2026 | in time; one but not both | s 113(3) "do 1 (but not both)" |
| A5 | s 123 decision notice 12 Jan 2027 | last day 10 Feb 2027; appeal only | s 123(4) |
| A6 | s 124(7) decision notice 23 Dec 2027 | last day 31 Jan 2028 | s 124(8) |
| A7 | s 113: applies for both review and appeal | not allowed | s 113(3) "1 (but not both)" — likely not expressible |

## Top-level

| id | inputs | expected |
|---|---|---|
| G1 | cl 5 met, price 10,000, 5% rate, s 113 notice 2 Nov 2026, unpaid until 8 Dec 2026, no refund | value 10,000, duty 500, due 30 Nov 2026, penalty 25 (1% of 500 = 5, + 4% of 500 = 20), refund 0 |

## Not expressible as input/output tests (stated before reading the encoding)

- Whether "seventh day" might be read as working day; the Act says "day" — I test calendar.
- "Opinion of the chief executive" judgments (cl 4(2), cl 9 "cannot be determined") are inputs.
- cl 6 evidence, cl 8 apportionment, methods 4-6: out of scope.

## Added after reading the encoding (no expected value above changed)

Not expressible against the encoding's functions and inputs:

- R6, R11, and the family sub-limbs R10/R12-R15: one boolean `members of the same family`, and one
  number for the cl 2(2)(a)(iv) share; tested only as the collapsed inputs.
- C2-C4, C7, C8: cl 5(a)-(c) exceptions are folded into the caller's booleans.
- C10 vs C11: one boolean `clause 6 complied with or not required`.
- T3, T7, T11, T14 (which amounts qualify as additions/deductions: buying commission, royalty not a
  condition of sale, amounts already in the price, not separately identified): the caller supplies
  the lists of qualifying amounts. T19 and T18 share one boolean; T22-T24 share `interest meets
  clause 3`.
- M8, M9 (cl 9 before cl 10), M10, M11 (cl 2(3) producer rule): only one list of adjusted identical
  values; the ordering between cl 9 and cl 10 and the same-producer preference are not modelled.
- M7: the encoding REFUSEs (methods 4 to 6 not encoded) — matches; not asserted.
- P22, L16 (s 124(7) earlier time): no payment occasion for s 124(7), although s 160(5) and the
  encoding's own comment refer to "124(2) to (7)".
- L13 (excise duty under Sch 3 cl 5(a), s 160(1)-(2)): not encoded (out of the brief's scope).
- V4-V6: the s 143(1) conditions are not inputs; the function takes only duty paid and final duty.
- A4 "1 (but not both)", A7: not expressible.
- F9 tested; F8 (Legislation Act s 55) is the one failing assertion.
