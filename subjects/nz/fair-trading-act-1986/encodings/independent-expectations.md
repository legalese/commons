# Independent expectations: Fair Trading Act 1986 (NZ)

Written from BRIEF.md and the source text (`act_public_1986_121.txt`, as at 1 July 2026) **before** any `.l4` file was opened.
Each scenario gives the facts, the expected answer, and the provision and words relied on.
Where a scenario could not be expressed against the encoding, that is noted in the final section (added in phase 2; no expected value was changed).

## Assumptions

- **Working day.** The Act does not define it. I take the Legislation Act 2019 s 13 definition: every day except Saturday, Sunday, Waitangi Day, Good Friday, Easter Monday, Anzac Day, the Sovereign's birthday, Matariki, Labour Day (and Mondayised Waitangi/Anzac Days), and any day from 25 December to 2 January inclusive. The brief says the encoding takes non-working weekdays as an input list, so tests pass the list explicitly.
  - Holidays used in tests: Good Friday 3 Apr 2026, Easter Monday 6 Apr 2026, Labour Day Mon 26 Oct 2026, and 25 Dec 2026 to 1 Jan 2027 (the weekdays Fri 25, Mon 28, Tue 29, Wed 30, Thu 31 Dec 2026 and Fri 1 Jan 2027).
- **"Within N working days after day X"**: day X is excluded; the deadline is the Nth working day after X, inclusive.
- **"N working days beginning with the date"** (s 36Q(1)(b)) includes the date itself if it is a working day.
- **"Within 3 years after the date"** (s 43A): the date is excluded; the last day is the anniversary date. For 29 February I take 28 February of the target year (no corresponding day, so the last day of the month) and flag the ambiguity.
- **Dollar thresholds** referring to other Acts: Disputes Tribunal Act 1988 s 10(1A)(b) is currently $30,000 and District Court Act 2016 s 74 is currently $350,000, so the Act's own floors ($60,000 and $350,000) govern.
- "Exceeds the annual value threshold" is defined in s 26D(3)(b) as consideration of **at least** the specified amount; so exactly $250,000 exceeds it.

Weekdays checked: 15 Oct 2026 Thu; 16 Oct Fri; 22 Oct Thu; 23 Oct Fri; 26 Oct Mon (Labour Day); 24 Dec 2026 Thu; 4 Jan 2027 Mon.

---

## A. Part 1: which provisions need conduct "in trade"

| # | Facts | Expected | Provision / words |
|---|---|---|---|
| A1 | s 7 unconscionable conduct, not in trade | no contravention | s 7(1) "must not, in trade, engage in conduct that is unconscionable" |
| A2 | s 7, in trade, conduct unconscionable | contravention | s 7(1) |
| A3 | s 7, in trade, no contract entered, no identified victim | still contravention | s 7(2) "whether or not ... a contract is entered into" |
| A4 | s 9 misleading conduct, not in trade (private sale) | no contravention | s 9 "No person shall, in trade" |
| A5 | s 9, in trade, misleading | contravention | s 9 |
| A6 | s 10 / s 11, not in trade | no contravention | ss 10, 11 "in trade" |
| A7 | s 12 employment misrepresentation, not in trade | **contravention** (no "in trade" limb) | s 12 "No person shall, in relation to employment ..." |
| A8 | s 12A unsubstantiated, not in trade | no contravention | s 12A(1) "must not, in trade" |
| A9 | s 13 false representation, not in trade | no contravention | s 13 "in trade" |
| A10 | s 14(1) land, not in trade | no contravention | s 14(1) "in trade" |
| A11 | s 14(2) physical force re land sale, not in trade | **contravention** | s 14(2) "No person shall use physical force, harassment, or coercion" (no "in trade") |
| A12 | s 16 trade mark forgery, not in trade | no contravention | s 16(1) "in trade" |
| A13 | s 17 gifts offered with no intention to provide, not in trade | **contravention** | s 17 no "in trade" limb |
| A14 | s 19(1) bait advertising, not in trade | no contravention | s 19(1) "in trade" |
| A15 | s 20 referral selling, not in trade | **contravention** | s 20(1) no "in trade" |
| A16 | s 20, acquisition of goods for resupply | no contravention | s 20(2) |
| A17 | s 21 accepting payment without intending to supply, not in trade | **contravention** | s 21 no "in trade" |
| A18 | s 21C asserting right to payment for unsolicited goods, not in trade | no contravention | s 21C(1) "in trade" |
| A19 | s 22 misleading home-business representation, not in trade | **contravention** | s 22 no "in trade" |
| A20 | s 23 harassment re supply, not in trade | **contravention** | s 23 no "in trade" |
| A21 | s 24 pyramid scheme, not in trade | **contravention** | s 24 no "in trade" |
| A22 | s 26A applying a declared unfair term, not in trade | contravention (no "in trade" limb) | s 26A(1) "a person must not" |
| A23 | s 32 supplying goods after a compulsory recall notice, not in trade | no contravention: s 32 notices go only to a person who "has in trade supplied goods", and s 32(5) forbids supply "in trade" | s 32(1), (5) |
| A24 | s 19(2) failure to offer advertised goods at the advertised price, advertiser not in trade | **ambiguous**; s 19(2) has no "in trade" limb ("Any person who has advertised"), unlike s 19(1). Best literal reading: contravention. | s 19(2) |
| A25 | s 36RA entering against a direction, s 31(4) supplying unsafe goods, not in trade | contravention (no "in trade" limb) | ss 31(4), 36RA |

## B. Application: Crown (s 4), Crown corporations (s 5), outside NZ (s 3), Takeovers Code (s 5B)

| # | Facts | Expected | Provision |
|---|---|---|---|
| B1 | Crown engages in misleading conduct in trade | Act binds Crown; contravention | s 4(1) "bind the Crown in so far as the Crown engages in trade" |
| B2 | Crown, conduct not in trade | Act does not bind Crown | s 4(1) |
| B3 | Crown contravenes s 13 (offence provision) | no prosecution; Commission or person directly affected may seek a High Court declaration (beyond reasonable doubt) | s 4(2) |
| B4 | Crown, who may seek s 4(2) declaration | Commission and person directly affected (not "any person") | s 4(2) |
| B5 | Crown entity body corporate in trade | Act applies; Part 5 proceedings may be brought (including prosecution) | s 5(1), (2) |
| B6 | Conduct outside NZ by NZ resident relating to supply within NZ | Act applies | s 3 |
| B7 | Conduct outside NZ by non-resident not carrying on business in NZ | Act does not extend (s 3) | s 3 |
| B8 | Conduct outside NZ by NZ resident relating to supply outside NZ | Act does not extend | s 3 "relates to the supply ... within New Zealand" |
| B9 | Conduct in a transaction regulated by the Takeovers Code | nothing in the Act applies | s 5B |

## C. News media (s 15)

| # | Facts | Expected | Provision |
|---|---|---|---|
| C1 | Newspaper publisher publishes misleading editorial matter | ss 9-14 do not apply: no contravention | s 15(1) |
| C2 | Newspaper publishes an advertisement that is misleading | s 15 exemption does not apply | s 15(1)(a) |
| C3 | Publisher publishes matter promoting its own goods | not exempt | s 15(1)(b)(i) |
| C4 | Publisher publishes matter for a person who has an arrangement with it about content | not exempt | s 15(1)(b)(ii) |
| C5 | Broadcaster broadcasts misleading news | exempt | s 15(2) |
| C6 | Broadcaster broadcasts advertisement | not exempt | s 15(2)(a) |
| C7 | Publisher's editorial engages s 12A (unsubstantiated) | exempt (12A lies within "sections 9 to 14") | s 15(1) |
| C8 | Publisher's editorial: s 16 / s 17 conduct | s 15 does not exempt (outside 9-14) | s 15 |
| C9 | Ambiguity: s 14A (vendor bids) is numbered after 14. Best reading: "sections 9 to 14" does not reach 14A, though in practice s 14A only deems a representation and s 13/14 does the work. Not asserted. | — | s 15, s 14A |

## D. Unsubstantiated representations (ss 12A, 12C, 12D)

| # | Facts | Expected | Provision |
|---|---|---|---|
| D1 | In trade, no reasonable grounds when made, representation true | contravention | s 12A(2) "irrespective of whether the representation is false" |
| D2 | In trade, reasonable grounds existed | no contravention | s 12A(2) |
| D3 | Reasonable person would not expect substantiation (puffery) | no contravention | s 12A(3) |
| D4 | Another enactment sets grounds requirements and the person complies | 12A does not apply | s 12D(a),(b) |
| D5 | Another enactment sets requirements but person does not comply | 12A applies: contravention | s 12D(b) |
| D6 | A consumer wants to bring proceedings / s 43 order for 12A | not permitted: only the Commission | s 12C |
| D7 | Commission brings 12A proceedings | permitted | s 12C |
| D8 | Competitor seeks injunction for 12A | not permitted | s 12C "apply for an injunction" |
| D9 | 12A contravention is an offence | yes, 40(1): $200,000 individual / $600,000 body corporate | s 40(1) (12A not excluded) |

## E. Contracting out (ss 5C, 5D) and who may seek s 43 orders

| # | Facts | Expected | Provision |
|---|---|---|---|
| E1 | Consumer contract with clause excluding s 9 | clause unenforceable | s 5C(2) |
| E2 | Clause imposes stricter duty on supplier | 5C(1),(2) do not apply: enforceable | s 5C(4)(a) |
| E3 | All 5D(3) requirements met, clause excludes s 9 | enforceable; no party may seek s 43 order for s 9 | s 5D(1)(a),(b) |
| E4 | Same, but agreement oral | 5D not met: unenforceable | s 5D(3)(a) |
| E5 | Same, but one party not in trade | 5D not met | s 5D(3)(c)(i) |
| E6 | Same, but not fair and reasonable | 5D not met | s 5D(3)(d) |
| E7 | Same, goods not acquired in trade | 5D not met | s 5D(3)(b) |
| E8 | 5D requirements met, clause purports to exclude s 7 (unconscionable) | 5D does not cover s 7: unenforceable | s 5D(1) lists only 9, 12A, 13, 14(1) |
| E9 | 5D met, clause purports to exclude s 10 | unenforceable | s 5D(1) |
| E10 | 5D met for s 13; Commission prosecutes s 13 offence | permitted | s 5D(5)(a) |
| E11 | 5D met for s 13; a party to the agreement seeks s 43 order | barred | s 5D(1)(b) |
| E12 | 5D met for s 13; a non-party third person seeks s 43 order | not barred by 5D (bar is on "any party to the agreement") | s 5D(1)(b), s 43(1) "on the application of any person" |
| E13 | s 9 contravention, consumer seeks s 43 order (no contracting out) | permitted | s 43(1) |
| E14 | Who may seek s 42 order | Commission only | s 42(1) "on the application of the Commission" |
| E15 | Who may seek s 41 injunction (non-12A) | Commission or any other person | s 41(1) |
| E16 | s 43 order for a Part 4A contravention (e.g. 36F) | available | s 43(1)(a) "Parts 1 to 4A" |
| E17 | s 41 injunction for Part 4A provision other than 36WB/36WC (e.g. 36ZD) | not available | s 41(1)(a) |
| E18 | s 41 injunction for 36WB | available | s 41(1)(a) |
| E19 | s 42 order for 36WC | available (Commission) | s 42(1) |

## F. Vendor bids (ss 14A, 36ZD)

| # | Facts | Expected | Provision |
|---|---|---|---|
| F1 | Auction, vendor bid, no reserve | s 14A: false/misleading price representation | s 14A(2) |
| F2 | Reserve; bid before reserve reached; clearly identified | not a misrepresentation | s 14A(3) |
| F3 | Reserve; bid after reserve reached; identified | misrepresentation | s 14A(3)(b) |
| F4 | Reserve; bid before reserve; not identified | misrepresentation | s 14A(3)(b) |
| F5 | Non-auction bidding process with all bids disclosed, vendor bid, no reserve | 14A applies: misrepresentation | s 14A(1)(b) |
| F6 | Passed-in reference to a vendor bid as the passed-in amount | misrepresentation | s 14A(4) |
| F7 | s 36ZD: terms permit, identified, reserve, bid below reserve | auctioneer may accept | s 36ZD(1) |
| F8 | s 36ZD: terms do not permit vendor bids (otherwise as F7) | must not accept | s 36ZD(1)(a) |
| F9 | s 36ZD: bid equal to reserve | must not accept ("less than") | s 36ZD(1)(c) |
| F10 | s 36ZD: no reserve | must not accept | s 36ZD(1)(c) |
| F11 | s 36ZD: not identified as given | must not accept | s 36ZD(1)(b) |
| F12 | 36ZD contravention: offence, fine | Part 4A: $10,000 individual / $30,000 body corporate | s 40(1B) |
| F13 | 36ZD contravention: is it an infringement offence | no | s 40B |

## G. Unsolicited goods (s 21A) and services (ss 21B, 21C)

| # | Facts | Expected | Provision |
|---|---|---|---|
| G1 | Unsolicited goods received Fri 16 Oct 2026; Labour Day 26 Oct non-working | collection window ends Mon 2 Nov 2026 | s 21A(1)(b) "10 working days after the day on which the recipient receives" |
| G2 | Same, with no holidays listed | ends Fri 30 Oct 2026 | s 21A(1)(b) |
| G3 | Received Thu 24 Dec 2026; holidays 25 Dec-1 Jan | ends Fri 15 Jan 2027 | s 21A(1)(b) |
| G4 | Received Thu 15 Oct 2026 | ends Fri 30 Oct 2026 | s 21A(1)(b) |
| G5 | Period expired, recipient complied, no knowledge | recipient takes goods as unconditional gift | s 21A(3)(a), (4) |
| G6 | Sender in trade failed to inform recipient; period not expired; recipient blameless | gift immediately | s 21A(3)(b) |
| G7 | Period expired but recipient knew goods were not intended for them | no gift | s 21A(5)(b) |
| G8 | Period expired; recipient refused collection without reasonable excuse | no gift | s 21A(5)(a) |
| G9 | Sender not in trade, did not inform | no 21A(2) duty, so 21A(3)(b) not triggered; no gift before expiry | s 21A(2) "If the sender is in trade" |
| G10 | Recipient fails to make goods available | not an offence | s 21A(6)(a) |
| G11 | Reticulated electricity supplied unasked | not "unsolicited goods" | s 21A(7)(b) |
| G12 | Recipient liable to pay for unsolicited goods? | no | s 21A(1)(a)(i) |
| G13 | Recipient liable for accidental damage? | no; deliberate damage yes | s 21A(1)(a)(ii) |
| G14 | Invoice for unsolicited services stating no obligation to pay (no regs) | not a contravention | s 21C(1)(b), (2)(b) |

## H. Specified trade contracts (ss 26C, 26D)

| # | Facts | Expected | Provision |
|---|---|---|---|
| H1 | Both in trade, not consumer, transparent term $249,999.99 per year | small trade contract (specified) | s 26C(2), s 26D(3)(b), (5) $250,000 |
| H2 | Same, exactly $250,000 | not a small trade contract ("at least") | s 26D(3)(b)(i) |
| H3 | Same, $253,000 incl GST (Example 1) | not small | s 26D Example 1 |
| H4 | No transparent term; expected $100,000 per year at start; later $300,000 (Example 3) | small trade contract (value at first arising) | s 26D Example 3 |
| H5 | Expected $120,000 + $180,000 under similar contracts (Example 2) | not small: $300,000 aggregated | s 26D Example 2 |
| H6 | One party not in trade | not specified trade contract | s 26C(2)(a) |
| H7 | It is a consumer contract | not specified | s 26C(2)(b) |
| H8 | Grocery: regulated grocery retailer + supplier, end-user consumer, $999,999 | grocery supply contract | s 26C(3), s 26D(5)(b) $1 million |
| H9 | Grocery, $1,000,000 | not grocery supply contract | s 26D(3)(b) |
| H10 | Grocery-type contract at $500,000 | grocery supply contract (and not small trade, since ≥ $250,000) | ss 26C(2),(3) |
| H11 | Grocery, end-user not a consumer, $300,000 | neither (not grocery; not small) | s 26C(3)(d) |
| H12 | Contract entered pre-commencement, not varied | 26B-26E do not apply | Sch 1AA cl 1(1)(a) |

## I. Unfair contract terms (ss 46H-46L, 26A, 26B)

| # | Facts | Expected | Provision |
|---|---|---|---|
| I1 | Commission applies re standard form consumer contract term | may apply | s 46H(1), 46I(1)(a) |
| I2 | Consumer applies directly re standard form consumer contract | cannot (may only ask the Commission) | s 46H(2), 46I(1)(a) |
| I3 | Supplier (any person) applies re grocery supply standard form trade contract | may apply | s 46H(3), 46I(1)(b) |
| I4 | Any person applies re small trade contract | cannot | s 46I(1) |
| I5 | Term defines main subject matter | cannot be declared unfair | s 46K(1)(a) |
| I6 | Term sets upfront price, transparent | cannot be declared | s 46K(1)(b), (2) |
| I7 | Price term not transparent | not "upfront price": may be declared | s 46K(2) |
| I8 | Term required by enactment | cannot be declared | s 46K(1)(c) |
| I9 | Significant imbalance, not reasonably necessary, detriment | unfair | s 46L(1) |
| I10 | Imbalance and detriment, advantaged party proves reasonably necessary | not unfair | s 46L(1)(b), (3) |
| I11 | Imbalance and detriment; no evidence on necessity | presumed not reasonably necessary: unfair | s 46L(3) |
| I12 | No detriment | not unfair | s 46L(1)(c) |
| I13 | Insurance: term specifying sum insured, with imbalance and detriment | deemed reasonably necessary: not unfair | s 46L(4)(b) |
| I14 | All 46I(2) limbs met, contract is not standard form | no declaration | s 46I(2)(b) |
| I15 | Party alleges standard form, no rebuttal | presumed standard form | s 46J(3) |
| I16 | Declared term later applied in a standard form contract | contravenes s 26A; Part 1 offence $200k/$600k | s 26A(1)(b), s 40(1) |
| I17 | Declared term included in a way that complies with court's decision | no contravention | s 26A(1)(a) |
| I18 | Jurisdiction for 46I declaration | High Court or District Court | ss 37, 38, 46H |

## J. Layby (ss 36B, 36F, 36G, 36H, 36I)

| # | Facts | Expected | Provision |
|---|---|---|---|
| J1 | Price $60,000, 3 instalments, possession after full payment | layby sale agreement | s 36B(1),(2) "more than $60,000" excluded |
| J2 | Price $60,000.01 | not layby | s 36B(2) |
| J3 | 2 instalments, agreement says it is layby | layby | s 36B(1)(b)(ii) |
| J4 | 2 instalments, not described as layby | not layby | s 36B(1)(b)(i) |
| J5 | Deposit + 2 instalments, not described | layby (deposit counts → 3) | s 36B(3) |
| J6 | Consumer takes possession immediately | not layby | s 36B(1)(a) |
| J7 | Consumer cancels before possession | may cancel | s 36F(1)(a) |
| J8 | Consumer cancels after possession | may not | s 36F(1)(a) |
| J9 | Consumer cancels; agreement provides charge; supplier not in breach | charge permitted, capped at reasonable costs | s 36F(3), (4) |
| J10 | Consumer cancels; agreement does not provide a charge | no charge | s 36F(3)(b) |
| J11 | Consumer cancels; supplier has breached | no charge | s 36F(3)(c) |
| J12 | Paid $500, charge $80 (≤ reasonable costs) | refund $420 immediately | s 36H(a) |
| J13 | Paid $50, charge $80 | refund $0; supplier recovers $30 as debt | s 36H(a),(b) |
| J14 | Agreement charge $200, reasonable costs $120, paid $500 | charge limited to $120: refund $380 | s 36F(4) |
| J15 | Supplier cancels because goods unavailable (36G(b)), paid $500, agreement charge $80 | full refund $500 (no deduction) | s 36H(a) "in the case of cancellation under section 36F or 36G(a)" |
| J16 | Supplier cancels for consumer's material breach; charge $80; paid $500 | refund $420 | s 36F(3)(a)(ii), 36H(a) |
| J17 | Supplier cancels for a non-material breach | supplier may not cancel | s 36G(a) |
| J18 | Supplier liquidated; goods part of assets; consumer paid within 3 months before | consumer may complete on paying balance | s 36I(2) |
| J19 | Supplier liquidated; consumer, in breach, paid nothing in prior 3 months | no completion right | s 36I(4) |
| J20 | Supplier in voluntary administration; consumer pays after event; agreement not completed | refund in full | s 36I(5),(6) |
| J21 | Supplier's further-disclosure statement requested Fri 23 Oct 2026 (Labour Day) | due Mon 2 Nov 2026, free | s 36D(2) |
| J22 | Layby disclosure (36C) breach: infringement offence | yes | s 40B(d)(i) |
| J23 | 36F cancellation-charge breach: infringement offence | no (offence under 40(1B) only) | s 40B |

## K. Uninvited direct sales (ss 36K, 36M, 36N, 36Q, 36R, 36RA)

| # | Facts | Expected | Provision |
|---|---|---|---|
| K1 | Door-to-door at home, uninvited, price $100.01 | UDS agreement | s 36K(1)(b)(i), (2) |
| K2 | Same, price exactly $100 | not UDS | s 36K(1)(b)(i) "more than $100" |
| K3 | Same, price not ascertainable at supply | UDS | s 36K(1)(b)(ii) |
| K4 | Consumer invited supplier to home for that supply | not UDS | s 36K(2) |
| K5 | Consumer invited supplier for a different supply | UDS | s 36K(2) parenthesis |
| K6 | Uninvited telephone call, $500 | UDS | s 36K(3) |
| K7 | Consumer merely gave contact details for another purpose | not an invitation: UDS | s 36K(5)(a)(i) |
| K8 | Renewal agreement (same parties, similar goods/terms, existing in force) | not UDS | s 36K(4), (6) |
| K9 | Supply not in trade | not UDS | s 36K(1) "in trade" |
| K10 | Copy received Fri 16 Oct 2026; cancel Fri 23 Oct | in time (5th working day) | s 36M(1)(a) |
| K11 | Copy received Fri 16 Oct; cancel Mon 26 Oct | late (unless 36L breach) | s 36M(1)(a) |
| K12 | Copy received Thu 22 Oct 2026, Labour Day 26 Oct | last day Fri 30 Oct 2026 | s 36M(1)(a) |
| K13 | Same, cancel Mon 2 Nov | late | s 36M(1)(a) |
| K14 | Supplier failed 36L (material); cancel months later | may cancel at any time | s 36M(1)(b) |
| K15 | Supplier failed 36L only in a minor, non-prejudicial way; cancel after 5 WD | out of time (36N(2) carve-out) | s 36M(1)(b) "except to the extent provided for in section 36N(2)" |
| K16 | Telephone agreement on Wed 21 Oct 2026; copy deadline | Thu 29 Oct 2026 | s 36L(1)(b)(ii) |
| K17 | Notice of cancellation given Thu 15 Oct 2026: end of 36Q care period ("10 working days beginning with the date") | Thu 29 Oct 2026 | s 36Q(1)(b) |
| K18 | Notice Thu 15 Oct 2026: end of 36R custody period ("10 working days after the date") | Fri 30 Oct 2026 | s 36R(2)(a) |
| K19 | On cancellation supplier must refund | all money paid, immediately | s 36P |
| K20 | Services supplied pre-cancellation | no compensation for services | s 36R(3)(a) |
| K21 | Specific direction to leave, given 1 Mar 2025; re-entry 1 Mar 2027 | prohibited ("within 2 years after") | s 36RA(5) |
| K22 | Same, re-entry 2 Mar 2027 | permitted under 36RA(5) | s 36RA(5) |
| K23 | Same, re-entry 28 Feb 2027 | prohibited | s 36RA(5) |
| K24 | General standing direction (gate sign); entering | must not enter | s 36RA(2), (4)(c) |
| K25 | Defence: direction-giver no longer resides there | defence available | s 44(7)(a) |
| K26 | 36RA breach fine | Part 4A: $10,000 / $30,000 | s 40(1B) |
| K27 | 36RA breach: infringement offence | no | s 40B |
| K28 | 36L breach: infringement offence | yes | s 40B(d)(iii) |

## L. Extended warranties (s 36V), gift cards (s 36WB)

| # | Facts | Expected | Provision |
|---|---|---|---|
| L1 | Copy received Fri 18 Dec 2026; Christmas period non-working | cancel by Mon 4 Jan 2027 | s 36V(1)(a) |
| L2 | Same, cancel Tue 5 Jan 2027 | late | s 36V(1)(a) |
| L3 | Warranty entered as condition of a consumer credit contract | no 36V(1) cancellation right | s 36V(2)(a) |
| L4 | Warrantor failed 36U materially; cancel at any time | may cancel | s 36V(1)(b) |
| L5 | Minor non-prejudicial 36U failure; after 5 WD | may not cancel | s 36V(2)(b) |
| L6 | Refund on cancellation: paid $300 for warranty | $300 in full, no deductions | s 36V(5) |
| L7 | Gift card sold 15 Oct 2026, expiry 15 Oct 2029 | complies (not less than 3 years) | s 36WB(1) |
| L8 | Expiry 14 Oct 2029 | contravenes; expiry taken to be 15 Oct 2029 | s 36WB(1), (3) |
| L9 | Expiry 15 Oct 2028 | contravenes | s 36WB(1) |
| L10 | Gift card sold not in trade | no contravention | s 36WB(1) "in trade" |
| L11 | Sold to a business (not consumer) | no contravention | s 36WB(1) "to a consumer" |
| L12 | Prepaid public transport card | not a gift card | s 36WA (b) |
| L13 | Card sold principally for charity | not a gift card | s 36WA (f) |
| L14 | 36WB breach: fine / infringement | $10,000 / $30,000; infringement offence | s 40(1B), 40B(d)(v) |
| L15 | Card with no expiry date stated prominently | contravenes s 36WC | s 36WC |
| L16 | Sold 29 Feb 2028, expiry 28 Feb 2031 | ambiguous (no 29 Feb 2031). Best reading: 3 years after ends 28 Feb 2031, so complies. Not asserted. | s 36WB |

## M. Auctions (ss 36ZA, 36ZF)

| # | Facts | Expected | Provision |
|---|---|---|---|
| M1 | Auction Fri 16 Oct 2026, passed in; post-auction offer from attendee accepted Mon 19 Oct | treated as sold at auction | s 36ZA(3)(b) "before the end of the first working day following" |
| M2 | Same, accepted Tue 20 Oct | not sold at auction | s 36ZA(3)(b) |
| M3 | Auction Fri 23 Oct 2026; Labour Day Mon 26; accepted Tue 27 Oct | sold at auction | s 36ZA(3) |
| M4 | Auction Thu 24 Dec 2026; accepted Mon 4 Jan 2027 | sold at auction | s 36ZA(3) |
| M5 | Offer from a person who did not attend | not treated as sold at auction | s 36ZA(3)(a) |
| M6 | Sale Thu 15 Oct 2026: proceeds/account deadline (Labour Day) | Fri 30 Oct 2026 | s 36ZF(1) |
| M7 | Vendor requests sooner on Mon 19 Oct 2026 | auctioneer must comply by Tue 27 Oct 2026 | s 36ZF(2) |
| M8 | Vendor in trade and agrees 36ZF(1) need not apply | auctioneer need not comply | s 36ZF(3) |
| M9 | Vendor in trade but does not agree | must comply | s 36ZF(3)(b) |
| M10 | Private vendor selling household goods, agrees | must comply (3(a) not met) | s 36ZF(3)(a) |
| M11 | Land sold by licensed real estate agent | 36ZF does not apply | s 36ZF(4) |
| M12 | Online "auction" where contract is directly between winner and seller | not an auction under subpart | s 36X(2) |

## N. Consumer information and product safety (ss 28, 30, 31, 31A, 33D)

| # | Facts | Expected | Provision |
|---|---|---|---|
| N1 | CIS applies; supplier does not comply | contravention of s 28; Part 2 fine $10,000/$30,000; infringement offence | s 28(1), 40(1B), 40B(b) |
| N2 | Two CISs; complies with one | no contravention | s 28(2) |
| N3 | Non-compliant goods labelled "for export only" | no contravention | s 28(3)(a) |
| N4 | PSS applies; goods non-compliant; supplied | contravention of s 30; Part 3 fine $200,000/$600,000; not infringement | s 30(1), 40(1) |
| N5 | PSS non-compliant goods marked export only | no contravention | s 30(3) |
| N6 | Unsafe goods notice under 31(1) published 1 Jan 2025: in force 1 Jul 2026? | yes (18 months after publication runs to 1 Jul 2026) | s 31(2) |
| N7 | Same, 2 Jul 2026 | expired | s 31(2) |
| N8 | Notice under 31(1A), published 1 Jan 2025, on 1 Jan 2027 | **ambiguous**: s 31(2) fixes the 18-month life only for "a notice made pursuant to subsection (1)". Best reading: a (1A) notice has no statutory expiry and stays in force until revoked; an encoding should refuse or treat it as in force, not expire it. | s 31(2) |
| N9 | Supplying goods while an unsafe goods notice is in force | contravention; $200,000/$600,000 | s 31(4), 40(1) |
| N10 | Voluntary recall Fri 16 Oct 2026 | notify chief executive by Tue 20 Oct 2026 | s 31A(2) |
| N11 | Recall Thu 22 Oct 2026 (Labour Day 26th) | by Tue 27 Oct 2026 | s 31A(2) |
| N12 | Recall Thu 24 Dec 2026 | by Tue 5 Jan 2027 | s 31A(2) |
| N13 | Recall Thu 2 Apr 2026 (Easter) | by Wed 8 Apr 2026 | s 31A(2) |
| N14 | Recall where another enactment requires reporting | s 31A does not apply | s 31A(1)(b) |
| N15 | Recall for commercial reasons (no injury risk, compliant) | s 31A does not apply | s 31A(1)(a) |
| N16 | Suspension notice issued Thu 22 Oct 2026 | must expire no later than 5 pm Wed 28 Oct 2026 | s 33D(3)(b) |
| N17 | Issued Thu 24 Dec 2026 | no later than 5 pm Wed 6 Jan 2027 | s 33D(3)(b) |
| N18 | Renewal: third renewal | not permitted | s 33D(5)(a) |
| N19 | Total prohibition 9 consecutive working days | permitted | s 33D(5)(b) |
| N20 | Total 10 working days | not permitted | s 33D(5)(b) |
| N21 | Breach of a suspension of supply notice | offence 40(1) $200,000/$600,000; infringement offence | s 33D(4), 40(1), 40B(a) |
| N22 | 28B trader status not disclosed online | Part 2 offence $10,000/$30,000; infringement offence | s 28B, 40(1B), 40B(c) |
| N23 | Services safety standard not complied with (s 36) | Part 4 offence $200,000/$600,000 | s 36, 40(1) |

## O. Offences and fines (s 40) and infringement offences (s 40B)

| # | Facts | Expected | Provision |
|---|---|---|---|
| O1 | s 9 contravention: offence? | no | s 40(1) except 9 |
| O2 | s 14(2): offence? | no | s 40(1) except 14(2) |
| O3 | s 14(1): offence, individual | yes, $200,000 | s 40(1)(a) |
| O4 | s 23: offence? | no | s 40(1) except 23 |
| O5 | s 24 individual | $600,000 | s 40(1A) |
| O6 | s 24 body corporate | $600,000 | s 40(1A) |
| O7 | s 13 body corporate | $600,000 | s 40(1)(b) |
| O8 | s 7 individual | $200,000 (s 7 is not excluded) | s 40(1) |
| O9 | s 10 body corporate | $600,000 | s 40(1) |
| O10 | s 36C individual | $10,000 | s 40(1B)(a) |
| O11 | s 36L body corporate | $30,000 | s 40(1B)(b) |
| O12 | s 28 body corporate | $30,000 | s 40(1B)(b) |
| O13 | s 21A(1)(b) failure by recipient | not an offence | s 21A(6)(a) |
| O14 | Two similar contemporaneous s 13 convictions, body corporate | aggregate cap $600,000 | s 40(2) |
| O15 | Two s 13 convictions not at about the same time | no aggregate cap (each up to $600,000) | s 40(2) |
| O16 | s 47F obstruction: individual / body corporate | $10,000 / $30,000 | s 47F(2) |
| O17 | s 47J failure to comply with 47G notice | $10,000 / $30,000 | s 47J(2) |
| O18 | s 46E breach of banning order | $60,000 | s 46E |
| O19 | Infringement offence: s 36D | yes | s 40B(d)(ii) |
| O20 | Infringement offence: s 36U | yes | s 40B(d)(iv) |
| O21 | Infringement offence: s 36WC | yes | s 40B(d)(vi) |
| O22 | Infringement offence: s 13 | no | s 40B |
| O23 | Infringement offence: s 30 (PSS) | no | s 40B |
| O24 | Infringement fee prescribed above $2,000 (e.g. $2,500) | not valid ("not exceeding $2,000") | s 40B |
| O25 | 28A fund-raiser disclosure breach | Part 2 offence $10,000/$30,000; not infringement | s 40(1B) |
| O26 | Crown contravention of s 13 | not prosecutable | s 4(2) |

## P. Time limit (s 43A) and jurisdiction (ss 37-39, 43B)

| # | Facts | Expected | Provision |
|---|---|---|---|
| P1 | Loss discovered 15 Oct 2023; application 15 Oct 2026 | in time | s 43A "within 3 years after the date" |
| P2 | Application 16 Oct 2026 | out of time | s 43A |
| P3 | Deadline for discovery 15 Oct 2023 | 15 Oct 2026 | s 43A |
| P4 | Discovered 29 Feb 2024 | ambiguous: best reading 28 Feb 2027 (alt. 1 Mar 2027) | s 43A |
| P5 | Disputes Tribunal, s 43(3)(f) payment $60,000 | within jurisdiction | s 43B(2)(a) |
| P6 | DT, $60,000.01 | outside | s 43B(2) |
| P7 | District Court, $350,000 | within | s 43B(1) |
| P8 | District Court, $350,000.01 | outside | s 43B(1) |
| P9 | High Court, $5,000,000 | within (no limit) | s 37(d) |
| P10 | Undertaking enforcement 46B: $350,000 | District Court | s 38(c) |
| P11 | 46B: $350,001 | High Court | s 37(e) |
| P12 | Prosecution for s 40 offence: first instance | District Court | s 38(a) |
| P13 | DT may grant s 41 injunction? | no; DT jurisdiction is s 43 orders only | s 39 |

## Q. Management banning orders (ss 46C-46F)

| # | Facts | Expected | Provision |
|---|---|---|---|
| Q1 | Individual convicted under 40(1) on 2 occasions 5 years apart; order necessary to protect public | eligible | s 46C(1)(a), (2) |
| Q2 | Only 1 occasion | not eligible | s 46C(1)(a) |
| Q3 | 2 occasions 11 years apart, no other | not eligible (not within a 10-year period) | s 46C(1)(a) |
| Q4 | 2 occasions exactly 10 years apart (1 Jan 2015 and 1 Jan 2025) | **ambiguous**; best reading eligible: both fall within one 10-year period | s 46C(1)(a) |
| Q5 | 2 offences under 40(1B) (Part 4A) only | not eligible | s 46C(1)(a) "40(1) or (1A)" |
| Q6 | Director of company when it committed 40(1) offence twice | eligible | s 46C(1)(a)(ii) |
| Q7 | Prohibited overseas under fair trading law | eligible | s 46C(1)(b) |
| Q8 | Grounds met but order not necessary to protect public | no order | s 46C(2) |
| Q9 | Order for 10 years | permitted | s 46D "no more than 10 years" |
| Q10 | Order for 11 years | not permitted | s 46D |
| Q11 | Body corporate as subject | not possible (individual only) | s 46C(1) |
| Q12 | Who may apply | Commission only | s 46F(1) |
| Q13 | Court | District Court | s 46C(1), 38(d) |

## R. ss 47F, 47J, 47I

| # | Facts | Expected | Provision |
|---|---|---|---|
| R1 | Obstructing a product safety officer under 33C | offence; $10,000 individual / $30,000 body corporate | s 47F |
| R2 | Supplying false documents knowingly in response to 47G | offence; $10,000/$30,000 | s 47J(1)(b), (2) |
| R3 | Failure to comply with 47G with reasonable excuse | no offence | s 47J(1)(a) |
| R4 | 47G notice emailed Thu 24 Dec 2026 | treated as received Tue 5 Jan 2027 | s 47I(3) |
| R5 | 47J proceedings: court | District Court | s 38(a) |

---

## Scenarios that could not be expressed against the encoding

(Filled in phase 2, after reading the module signatures; expected values above are unchanged.)

Expected values were not changed after the encoding was read. The scenarios below have no function or input in the encoding, so `tests-independent.l4` does not assert them:

- **B3-B4** s 4(2): there is no route for a Crown declaration (who may apply, High Court, beyond reasonable doubt). The encoding gives a fine of 0 for the Crown, and I assert that.
- **B5-B9** ss 3, 5, 5B: conduct outside NZ, Crown corporations and the Takeovers Code are carried as text only.
- **C9** s 14A and s 15: there is no s 14A constructor in `Prohibition`.
- **E1-E2** s 5C(2), (4): there is no function for whether a contracting-out clause is enforceable outside s 5D, or for the stricter-duty exception.
- **E12** s 5D(1)(b): the bar applies to "any party to the agreement". The encoding's `a party may apply for a s 43 order` cannot tell a non-party third person apart from a party.
- **E14-E19** ss 41, 42: who may seek injunctions and s 42 orders, and for which provisions (Parts 1-4 plus 36WB/36WC, not the rest of Part 4A), is carried as text.
- **F5-F6** s 14A(1)(b), (4): non-auction bidding processes and passed-in references have no inputs. The s 14A function assumes the process is covered.
- **G10-G14** ss 21A(1)(a), (6), (7), 21C(2): not encoded.
- **H12** Sch 1AA cl 1: there is no pre-commencement input for specified trade contracts.
- **I1-I4, I15-I18** ss 46H, 46I(1), 46J(3), 26A(1)(a): who may apply for a declaration, the standard-form presumption and jurisdiction are not encoded. **I13**: the insurance deeming in s 46L(4) can only be fed in as "shown to be reasonably necessary".
- **J7-J9, J17, J20** ss 36F(1), 36G, 36I(5): cancellation timing, supplier grounds and the post-event refund are not encoded.
- **K5, K7** s 36K(2), (5): handled only as a pre-digested `negotiations` input.
- **K17** s 36Q(1)(b) "10 working days **beginning with** the date". There is no function for this. The encoding's only working-day helper counts days *after* a date, so it would give Fri 30 Oct 2026 for a notice on Thu 15 Oct 2026, where I expect Thu 29 Oct.
- **K19-K20, K24-K25** ss 36P, 36R(3), 36RA(2)-(4), 44(7): not encoded. 36RA(5) is encoded only for a specific direction.
- **L3** s 36V(2)(a): a warranty entered as a condition of a consumer credit contract has **no** cooling-off right. The shared cooling-off function has no input for this, so it would wrongly allow cancellation. This is an omission.
- **L5, K15**: the s 36N(2) / 36V(2)(b) "minor failure" carve-out can only be expressed by setting "disclosure failed materially" to FALSE.
- **L6** s 36V(5): the full refund is not encoded.
- **L10-L13, L15-L16** ss 36WA, 36WB, 36WC: the gift card definition and exclusions are not encoded. The expiry function has no in-trade or to-a-consumer input; its in-trade limb is tested only through `the conduct contravenes the provision`.
- **M8-M12** s 36ZF(3)-(4), s 36X(2): not encoded. The 36ZF(2) words "unless the vendor and auctioneer have agreed otherwise" are not an input either.
- **N5, N14-N15** s 31A(1): the conditions for 31A applying are not encoded. The export rule is shared between ss 28 and 30.
- **N8** s 31(2): the 18-month life applies only to a notice "made pursuant to subsection (1)". The encoding's function applies 18 months to every unsafe goods notice and cannot tell a s 31(1A) notice apart. I think a (1A) notice has no statutory expiry. This is an omission.
- **O13-O15, O25** ss 21A(6), 40(2), 28A: the aggregate-fine cap in s 40(2) is not encoded, and there is no s 28A or s 21A(2) constructor.
- **P10-P13** ss 37(e), 38(c), 39: jurisdiction over undertakings and prosecutions is not encoded.
- **Q2, Q5-Q7, Q11-Q13** s 46C(1)(a)(ii), (b), 46F: the banning-order function takes exactly two dates. It cannot express a single occasion, the kind of offence (40(1)/(1A) against 40(1B)), director liability, an overseas prohibition, or who may apply.
- **R3, R5** s 47J(1)(a) reasonable excuse, and jurisdiction: not encoded.

## Results (phase 2)

`tests-independent.l4`: 239 assertions, 237 satisfied, 2 failed, 0 other errors.

1. **A23, s 32 not in trade.** I expect no contravention. The encoding finds one, because s 32 is missing from `the provision applies only in trade`.
2. **A24, s 19(2) not in trade (ambiguous).** I expect a contravention on the literal words. The encoding finds none, because it treats all of s 19 as "in trade".
