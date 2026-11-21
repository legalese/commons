# Independent readings, slice B (Regulation W, 12 CFR Part 223: covered transactions to exemptions)

Written independently from the regulation text and the interface, before the encoding was read.
Companion to `regwb-independent-tests.l4` (966 assertions, 68 end-to-end scenarios).

Counts against the answer-FALSE interface (main 1.6.112): 516 assertions fail (these can fail the real encoding), 450 pass (every one of them expects FALSE, 0 or a first constructor; the list is the appendix).

Percent arguments are written as the regulation prints them (10 means 10 percent).
That is an interface assumption, IA1 below, not a reading of the regulation.

## R-entries: where the words fork

Each entry gives the words that fork, the reading the assertions take, and what the other reading would give.
The assertions that depend on an entry are in the last section of the test file, `Contested readings`, at the lines listed.

### R1. Which company does 223.3(h) test for affiliation?

- **Words.** 223.3(h)(4): "the acceptance of a security issued by the affiliate as collateral for an extension of credit to any person or company"; (h)(5): "a guarantee, acceptance, or letter of credit ... on behalf of the affiliate"; 223.3(j): a cross-affiliate netting arrangement is "among a member bank, one or more affiliates ... and one or more nonaffiliates".
  In these three the counterparty can be a nonaffiliate while the affiliate is the issuer, or the company on whose behalf the bank acts.
  The interface's `Transaction` has two names, `with` and `affiliate concerned`, and the text does not say which one `is a covered transaction` tests.
- **Reading taken (A).** The affiliate is the `affiliate concerned`: the issuer in (h)(4), the company on whose behalf in (h)(5), the affiliate party in a netting arrangement. `with` is the counterparty and may be a nonaffiliate.
  So (h)(4), (h)(5) and netting with `with` = Stranger Corp and `affiliate concerned` = Acme Holdings are covered; (h)(4) with a nonaffiliate's security and an affiliate borrower is not.
- **Other reading (B).** The test is on `with`: the first three are not covered, and the last is covered.
- Every other covered-transaction assertion in the file sets `with` and `affiliate concerned` to the same company, so it holds under both readings.
- Assertions: lines 1469, 1470, 1471, 1472, 1475, 1476, 1477, 1478, 1479.

### R2. "5 percent" in 223.15(b)(3)

- **Words.** "does not exceed its proportional share of the original transaction by more than 5 percent".
- **Reading A (constructor `Five percentage points above the proportional share`).** share at most proportional plus 5 (25 against 20 is within; 5 against 0 is within).
- **Reading B (constructor `Five percent more than the proportional share`).** share at most 1.05 times proportional (25 against 20 is not within; 21.01 against 20 is not; 5 against 0 is not).
- The interface carries a switch, so each constructor has its own assertions (also at the `renewal exception applies` and `prohibited` level).
  The cases where both readings agree (20/20, 21/20, 15/20, 0/0, 25.01/20, 50/20, 5.01/0) are in the section for 223.15, asserted under both constructors.
- Needs IA2 (shares are percentages).
- Assertions: lines 1482, 1483, 1484, 1485, 1486, 1487, 1488, 1489, 1490, 1491, 1492.

### R3. A senior claim larger than the collateral (223.14(d)(2))

- **Words.** The bank "must deduct from the value of collateral ... the lesser of" the senior security interest and the senior credit. Nothing says the result stops at zero.
- **Reading taken (A).** The effective value is not below zero, so over-encumbered collateral contributes nothing to the amount secured.
- **Other reading (B).** The deduction is taken as written and the effective value is negative (100 less 500 is -400), so over-encumbered collateral reduces the amount that clean collateral secures.
- Tested through `amount of the transaction secured by collateral`, where B would give -300 and A gives 100.
- Assertions: lines 1494.

### R4. Where an unperfected security interest bites (223.14(d)(1))

- **Words.** The bank "must maintain a security interest in collateral required by this section that is perfected and enforceable".
  223.14(c) (ineligible collateral) lists no perfection condition.
- **Reading taken (A).** Perfection is not part of eligibility: `is eligible collateral` is TRUE for an unperfected Treasury, and its `effective value` is 0.
- **Other readings.** (B) perfection is part of eligibility, so `is eligible collateral` is FALSE and `effective value` ignores perfection (it is the market value); (C) both are affected: `is eligible collateral` FALSE and effective value 0.
- Every assertion at the level of `amount of the transaction secured by collateral`, `collateral requirement is met` and the assessment treats an unperfected interest as securing nothing, which all three readings agree on.
- The assertion on `effective value of collateral` = 0 also passes against the answer-0 interface (listed in the appendix).
- Assertions: lines 1496, 1497.

### R5. What counts as "secured" in the 223.42(c) exemption

- **Words.** "to the extent that the transaction is and remains secured by" Treasuries, guaranteed obligations or a segregated deposit.
  223.42(c)(2)'s example uses market values with no senior lien.
  223.14(d)(2)'s priority deduction is stated for "collateral required by this section" (223.14), not for 223.42.
- **Reading taken (A).** The exempt part is the collateral's value net of a senior lien (Treasuries of 100 behind a senior 40 lien exempt 60 of the loan).
- **Other reading (B).** The exempt part is the market value as it stands (the same facts exempt 100).
- Assertions: lines 1499.

### R6. Does 223.15 still apply to a 223.16(c) transaction?

- **Words.** 223.16(c): the transactions "are not subject to the quantitative limits of 223.11 and 223.12 or the collateral requirements of 223.14. The transactions are, however, subject to the safety and soundness requirement of 223.13 and the market terms requirement and other provisions of subpart F."
  223.41 expressly keeps 223.13 and 223.15; 223.42 keeps 223.13 only; 223.16(c) names 223.13 and subpart F and says nothing of 223.15.
- **Reading taken (A).** Only the three named requirements are lifted, so 223.15 still applies (`requirement still applies` is TRUE).
- **Other reading (B).** Only 223.13 and subpart F remain, so 223.15 does not apply.
- Assertions: lines 1501.

### R7. An exemption that covers only part of a transaction (223.42(c)) and the limits

- **Words.** 223.42(c): the transaction is exempt "to the extent" it is secured by Treasuries; its example says "the value of the covered transaction is $50" for a loan of 100 with Treasuries of 50.
  223.42 also says "The following transactions are not subject to the quantitative limits".
- **Reading taken (A).** The limits apply to the part that is not exempt: the 50 that is left is tested against 10 percent of capital stock and surplus (500: not over; 499: over).
- **Other reading (B).** Claiming a 223.42 exemption switches the limits off for the whole transaction, so neither scenario breaches.
- Assertions: lines 1505, 1506, 1507, 1508, 1509, 1513, 1514, 1515, 1516.

### R8. What "amount that counts toward the limits" reports

- **Words.** 223.3(a): the aggregate amount is the amount about to be engaged in added to the outstanding amount.
  The interface's field name does not say whether it reports the transaction's own amount or the aggregate.
- **Reading taken (A).** The transaction's own amount, its value less the value exempt (60 for a loan of 60 with 40 outstanding).
- **Other reading (B).** The aggregate (100 in the same case).
- The scenarios with nothing outstanding give the same answer on both readings, and those are the ones that assert this field outside the contested section.
- Assertions: lines 1521, 1522, 1523, 1524.

### R9. 223.24(b) when the nonaffiliate collateral exceeds the credit

- **Words.** "the total value of the extension of credit less the fair market value of the nonaffiliate collateral" can be negative; nothing says it stops at zero.
- **Reading taken (A).** The value is not below zero (100 less 150 gives 0).
- **Other reading (B).** The lesser of -50 and 50 is -50.
- The assertion also passes against the answer-0 interface (listed in the appendix).
- Assertions: lines 1527.

### R10. The percentage for a Board-approved intangible asset

- **Words.** 223.14(c)(4): intangible assets (including servicing assets) are not eligible collateral "unless specifically approved by the Board".
  223.14(b)(1) lists percentages for four groups and ends with "stock, leases, or other real or personal property" at 130 percent; it does not name intangibles.
- **Reading taken (A).** An approved intangible asset is "other ... personal property", so 130 percent.
- **Other reading (B).** The words give it no percentage (the Board's approval might set one), so `percent the collateral must stand at` has no answer for that kind.
- Assertions: lines 1529, 1530, 1531, 1532.

### R11. The member bank as its own affiliate (slice A's switch, passed through)

- **Words.** 223.2(a)(2) with 223.3(f), slice A: the member bank is a company controlled by a company that controls it, so on the literal words it is its own affiliate. Slice A carries the switch.
- **Not a fork in slice B's words.** The assertions check only that the `Readings` given to slice B reach `is an affiliate`: a loan to "Acme Bank" itself is not covered under the default constructor and is covered under the literal one (and so for `would breach the single-affiliate limit` and `purchase of a low-quality asset is prohibited`).
  Every other call in the file passes the same `Readings`, so without these an encoding that ignored the argument would pass.
- Assertions: lines 1534, 1535, 1536, 1537, 1538.

## How the file was checked

- It type-checks and every `#ASSERT` evaluates on main 1.6.112, against the interface and against a scratch reference model.
- The reference model is my own, written from the regulation text and the interface signatures and kept outside the deliverables; it agreed with all 966 assertions once the one gap below was closed, and no expectation was changed to make it agree.
  Its one finding was that the words give no percentage for a Board-approved intangible asset (the model divided by zero): that assertion was moved into the contested section as R10 with its expected value unchanged.
- 43 single-token mutations of the model (an edge comparison turned strict, a limb dropped, a threshold changed, a constructor mishandled) are each caught by at least one assertion. On the first run one survived: 223.42(g)(3)(ii) compared the price with the electronic quotation instead of the average of the broker-dealer quotes and nothing noticed. Two cases were added for it, from the words, and it is now caught.
  This shows the file is consistent and sensitive on the edges. It does not show the readings are right: the model and the file have one author.

## Interface assumptions (not readings of the regulation)

These are choices about what an input or output of the interface means.
They are not R-entries because the regulation's words do not fork on them; the interface leaves them open.
A failure that traces to one of these is about the convention, not about the law.

- **IA1. Percent scale.** Every percent argument is the number the regulation prints: 10 for 10 percent, 130 for 130 percent, 25 for 25 percent (`percent`, `percentPermitted`, `percentAllowed`, `percentBoughtFromAffiliates`, `percentOfClass`, `percentOfEquity`, `bankHolds`, `institutionHolds`, `companyHoldsOf...`).
  Evidence: slice A's `percent of class` is tested `AT LEAST 25`; and the regulation's own 223.14(d)(3) arithmetic fixes `collateral value required 2000 130` = 2600.
  If the encoding uses fractions (0.10) every test of an edge on a percent will fail for reasons of scale.
- **IA2. Shares in 223.15(b)(3).** `the bank's share of the renewal` and `its proportional share` are percentages of the transaction (20 means 20 percent); the percentage-points reading cannot be computed from dollar amounts.
- **IA3. `value` and `outstanding`.** `Transaction.value` is the amount already valued under 223.21 to 223.23 (a revolving facility is valued at its full 300, 223.21(a)(4)(ii)), and the `outstanding` figures exclude the proposed transaction.
- **IA4. `value exempt`.** The part of the value an exemption removes: 0 with no exemption, the full value for a transaction exempt altogether, a part only in the 223.42(c) scenarios of R7.
  Every non-contested scenario gives a consistent pair of `exemption claimed` and `value exempt`.
- **IA5. Aggregates.** `aggregateValue` in 223.41(d)(6) already includes the present transaction; `originatedInThePrecedingYear` in 223.42(k)(5) includes the present extension of credit; `otherPurchasesInThePrecedingYear` does not include `thisAmount`.
- **IA6. Purpose.** The affiliate lookup for covered transactions uses `Section 23A` (223.3(h) belongs to the section 23A subparts), so a sister depository institution is an affiliate.
  Under `Subpart F, section 23B` it would not be (223.2(c)).
- **IA7. Kinds.** `A purchase of, or an investment in, a security` is read as an equity-type or other non-debt security; a purchase of a debt security of an affiliate is an extension of credit (223.3(o)(4)), modelled as `An extension of credit`, which is why 223.14(f)(3) is tested on that kind.
  A renewal of a loan participation (223.15(b)) is modelled as `A purchase of an asset`, because the interface puts the renewal facts only under `Asset purchase facts`.
- **IA8. Vacuous answers.** At the level of the ASSESSMENT, `meets the collateral requirements` and `meets the safety and soundness requirement` are not asserted for transactions the requirement does not reach (non-covered, non-credit, exempt): whether the field says TRUE (not applicable, so met) or something else is a reporting convention; `may be entered into` is asserted for those.
  At the level of the function `collateral requirement is met` the file does assert TRUE where nothing must be secured (a purchase of an asset, a security or an acceptance as collateral; a credit of value 0; the (f)(1) and (f)(3) cases), reading it as 'the amount secured is at least the amount that must be secured'.
- **IA9. Exception flags are tested with the kinds the words name.** 223.14(f)(1) with the guarantee/acceptance kind; (f)(2) with an extension of credit (and a guarantee with an unused figure is asserted to have no unused portion excepted); (f)(3) with an extension of credit.
  What an `an acceptance already fully secured` flag does on an extension-of-credit kind is not asserted.
- **IA10. Inputs outside the regulation's range are not tested.** `percentPermitted` below 10 or above 25 (223.41(d)(6)); `percentAllowed` above 50 (223.42(k)(5)); shares above 100; negative amounts; an amortization or reduction larger than the initial figure.
- **IA11. `names a financial subsidiary`** is tested only on a party that is both flagged and controlled by the bank; whether control by the bank is required is not tested.
- **IA12. Not tested because the words give no answer or the interface has no function.** `percent the collateral must stand at` for the four kinds that are ineligible without exception (the intangible asset is R10); a Board-exempted purchase of property that is also a low-quality asset; a purchase of a low-quality security (223.3(v)(1) says "including a security"; the interface has the asset-purchase and security-purchase kinds separately).
- **IA13. Rules with no function in the interface.** 223.14(e) (replacement of retired collateral); the timing rules 223.21(b), 223.22(b), 223.23(b) (only the `held` flag of `value of an asset purchase later` is reached); 223.21(b)(2)(i) (collateral within one year of becoming an affiliate); the 12-month arithmetic of 223.16(c)(4)(iii); the fiduciary parenthetical of 223.24(c)(2)(ii).
  The first half of the 223.21(b)(2)(iii) example (no violation at the time of the stock acquisition) has no function either; its second half (no further covered transaction until the loan falls below 10 percent) is in scenarios 47 to 49 of the assessment section.
- **IA14. Conditions the interface collapses into one flag** (`wellCapitalizedAndWellManaged`, `compensationMeetsMarketTerms`, `notInformedByTheBoardItMayNotUseIt`, the 223.42(n) period flag) cannot be separated into their sub-limbs.

## Appendix: assertions that pass against the answer-FALSE/0 interface

All 450 of them expect FALSE, 0 or the first constructor of the result type, which is exactly what the interface answers, so they pass for that reason and not because any rule was applied.
They are kept because each is the "one condition violated alone" or "the other side of the edge" case the task asks for: a real encoding that ignores the condition fails them.
Every assertion that expects TRUE or a non-zero value fails against the interface (516).
By section:

- 223.3(h) and (i): covered transactions and credit transactions, expects FALSE (14): lines 140, 141, 142, 143, 150, 165, 166, 167, 168, 169, 170, 171, 172, 175
- 223.3(a): the aggregate amount of covered transactions, expects 0 (1): lines 185
- 223.3(a): the aggregate amount of covered transactions, expects FALSE (8): lines 192, 194, 195, 197, 198, 200, 203, 205
- 223.11: the single-affiliate limit, expects FALSE (18): lines 211, 212, 213, 214, 215, 216, 221, 223, 224, 226, 231, 241, 242, 243, 245, 246, 247, 248
- 223.12: the all-affiliates limit, expects FALSE (12): lines 255, 257, 258, 260, 262, 263, 266, 268, 270, 277, 278, 279
- 223.16(a) and (b): transactions with any person treated as transactions with an affiliate, expects 0 (2): lines 294, 298
- 223.16(c): exemptions from the limits and the collateral requirements, expects FALSE (24): lines 313, 314, 317, 318, 319, 320, 323, 324, 325, 326, 335, 336, 338, 339, 341, 342, 343, 344, 353, 354, 355, 356, 357, 358
- 223.3(v): a low-quality asset, expects FALSE (5): lines 370, 371, 372, 375, 378
- 223.14: collateral requirements, expects FALSE (36): lines 401, 402, 403, 404, 405, 407, 408, 409, 410, 476, 478, 480, 482, 484, 486, 488, 490, 492, 494, 496, 497, 498, 500, 501, 502, 503, 504, 505, 510, 511, 512, 517, 519, 521, 524, 526
- 223.14: collateral requirements, expects 0 (8): lines 447, 448, 462, 463, 464, 465, 470, 472
- 223.15: low-quality assets, expects FALSE (31): lines 538, 539, 540, 545, 546, 547, 559, 560, 561, 562, 566, 567, 574, 575, 577, 578, 579, 580, 581, 584, 585, 590, 597, 598, 599, 600, 601, 606, 612, 613, 614
- 223.22: valuation of asset purchases, expects the first constructor (1): lines 641
- 223.22: valuation of asset purchases, expects 0 (3): lines 655, 656, 657
- 223.24: extensions of credit secured by affiliate securities, expects FALSE (8): lines 699, 701, 711, 712, 713, 714, 715, 718
- 223.41: exemptions from the quantitative limits and the collateral requirements, expects FALSE (31): lines 731, 732, 733, 734, 735, 736, 737, 738, 742, 743, 744, 745, 746, 749, 750, 751, 759, 760, 761, 762, 763, 764, 765, 766, 768, 769, 773, 774, 777, 778, 780
- 223.42: exemptions from the quantitative limits, collateral requirements and the low-quality asset prohibition, expects FALSE (81): lines 787, 788, 791, 792, 798, 799, 800, 801, 802, 803, 804, 805, 806, 828, 829, 835, 836, 837, 838, 846, 847, 848, 849, 850, 851, 852, 854, 855, 859, 869, 870, 874, 876, 879, 880, 881, 885, 887, 888, 889, 892, 893, 894, 895, 899, 900, 901, 904, 905, 908, 909, 915, 916, 917, 918, 919, 921, 923, 926, 927, 928, 930, 935, 936, 937, 938, 939, 942, 943, 944, 947, 948, 949, 950, 951, 952, 953, 956, 957, 958, 959
- 223.42: exemptions from the quantitative limits, collateral requirements and the low-quality asset prohibition, expects 0 (5): lines 815, 816, 817, 820, 821
- The effects of an exemption: which requirements remain, expects FALSE (10): lines 973, 974, 976, 978, 979, 981, 982, 983, 984, 986
- The assessment of a proposed transaction, expects FALSE (130): lines 1000, 1001, 1004, 1012, 1015, 1016, 1021, 1022, 1029, 1030, 1035, 1036, 1042, 1044, 1049, 1050, 1056, 1058, 1063, 1064, 1072, 1078, 1083, 1084, 1085, 1090, 1091, 1092, 1097, 1098, 1099, 1104, 1105, 1106, 1114, 1115, 1121, 1122, 1129, 1130, 1136, 1137, 1143, 1144, 1145, 1156, 1157, 1169, 1175, 1176, 1177, 1179, 1185, 1192, 1193, 1194, 1199, 1206, 1207, 1208, 1213, 1220, 1221, 1222, 1228, 1229, 1236, 1237, 1238, 1239, 1244, 1258, 1259, 1266, 1267, 1268, 1273, 1274, 1275, 1280, 1281, 1286, 1287, 1292, 1293, 1304, 1305, 1310, 1311, 1317, 1318, 1324, 1325, 1326, 1333, 1338, 1339, 1346, 1352, 1354, 1359, 1360, 1367, 1368, 1369, 1377, 1382, 1389, 1394, 1402, 1403, 1410, 1411, 1412, 1413, 1419, 1420, 1427, 1428, 1429, 1430, 1436, 1437, 1444, 1445, 1446, 1447, 1452, 1453, 1461
- The assessment of a proposed transaction, expects 0 (5): lines 1366, 1375, 1401, 1418, 1435
- Contested readings, expects FALSE (15): lines 1472, 1477, 1478, 1485, 1486, 1487, 1489, 1491, 1507, 1508, 1516, 1523, 1532, 1534, 1537
- Contested readings, expects 0 (2): lines 1497, 1527
