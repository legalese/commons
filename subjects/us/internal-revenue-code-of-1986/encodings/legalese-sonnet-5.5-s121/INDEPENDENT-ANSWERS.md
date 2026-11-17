# ANSWERS: 26 U.S.C. section 121, written from the text alone before any .l4 file was opened

Notation.
`Y` = yes / true (the text says so).
`N` = no / false: the text itself says no, so a function would answer `JUST FALSE` (the reason is in the Guide note).
`NOTHING` = not covered (the text is silent): a function would answer `NOTHING`.
A number is the dollar amount of gain EXCLUDED from gross income unless stated.
Dates are ISO.
Day counts are inclusive of both end dates: a home used from 2021-07-01 through 2023-06-30 has been used for exactly 2 years.
Where the answer depends on the encoder's day-count convention I say so in the scenario, and treat a disagreement there as AMBIGUOUS at triage.

BASE (applies unless a scenario says otherwise): one individual taxpayer, unmarried, spouse not deceased, sale on 2023-06-30, the property owned and used as the taxpayer's principal residence continuously from 2019-01-01 to the sale, no earlier sale or exchange, no election, no depreciation adjustments, no period of rental or other non-residence use, an ordinary sale, the gain as stated.

## (a) The exclusion and its two-year-in-five test

1. (a) BASE, gain 100,000 => Y; excluded 100,000.
2. (a) Owned and used from 2021-06-30 through the sale on 2023-06-30 (2 years and 1 day), gain 100,000 => Y; 100,000.
3. (a) Owned and used from 2021-07-01 through the sale on 2023-06-30 (exactly 2 years), gain 100,000 => Y; 100,000. Day-count sensitive: 729 days by plain date subtraction.
4. (a) Owned and used from 2021-07-02 through the sale on 2023-06-30 (2 years less 1 day), gain 100,000 => N; excluded 0. Guide: "if" condition unmet.
5. (a) Owned 10 years; used as principal residence only 2012-01-01 to 2018-01-01; sale 2023-06-30, gain 100,000 => N; 0. The use falls before the 5-year window (2018-06-30 to 2023-06-30). Guide: "if".
6. (a) Owned throughout; used as principal residence 2018-12-01 to 2019-12-01 and again 2022-06-30 to 2023-06-30 (two separate years, both inside the window), gain 100,000 => Y; 100,000. "Periods aggregating".
7. (a) Owned 2017-01-01 to sale; used 2017-01-01 to 2019-01-01 only (2 years, of which only 2018-06-30 to 2019-01-01 is inside the window), gain 100,000 => N; 0. Guide: "if".
8. (a) Owned 6 years, never lived in it (a pure rental), gain 100,000 => N; 0. Guide: "if".
9. (a) Owned 5 years, used as principal residence only 1 year 6 months, gain 100,000 => N; 0. Guide: "if".
10. (a) Owned and used for 1 year 6 months only (bought 2021-12-30), gain 100,000 => N; 0. Guide: "if".
11. (a) The taxpayer is 72 years old, owned and used 3 years, gain 100,000 => Y; 100,000. The text sets no age condition.

## (b)(1) the $250,000 ceiling

12. (b)(1) BASE, gain 250,000 => 250,000.
13. (b)(1) BASE, gain 250,001 => 250,000.
14. (b)(1) BASE, gain 600,000 => 250,000.

## (b)(2) joint returns; (d)(1)

15. (b)(2)(A) Husband and wife, joint return for 2023; husband owned and lived there 5 years, wife lived there 2.5 years; gain 600,000 => 500,000.
16. (b)(2)(A) Same, gain 500,001 => 500,000.
17. (b)(2)(A) Same, gain 400,000 => 400,000.
18. (b)(2)(B) Joint return; husband owned and used 5 years, wife only 1 year (moved in at marriage); gain 400,000 => 250,000 (wife's limit is nil, the husband's is 250,000).
19. (b)(2)(B) Joint return; both owned and used 3 years; husband sold another home 12 months ago and excluded the gain under (a); wife has no such sale; gain 400,000 => 250,000 ((A)(iii) fails; wife is treated as owning for the husband's ownership period, so she is entitled to 250,000 and he to nil).
20. (b)(2)(B) Joint return; both owned and used 3 years; each spouse sold another home 12 months ago and excluded the gain under (a); gain 400,000 => 0.
21. (b)(2) Married but each files separately; husband owned and used 5 years; gain 300,000 => 250,000 (the joint-return rule is silent for separate returns; (b)(1) governs).
22. (d)(1) Joint return; husband owned and used 5 years; wife never lived there; gain 100,000 => Y; 100,000.
23. (d)(1) Joint return; each spouse used it only 1 year, owned 1 year, no change of employment or health; gain 80,000 => N; 0. Guide: "if".

## (b)(3) one sale every two years

24. (b)(3) Prior sale on 2022-06-30 to which (a) applied; this sale 2023-06-30; otherwise qualifying; gain 100,000 => (a) does not apply: N; excluded 0. Guide: flat negative "shall not apply".
25. (b)(3) Prior sale on 2021-04-30 to which (a) applied (2 years 2 months before); gain 100,000 => no bar; Y; 100,000.
26. (b)(3) Prior (a)-sale on 2021-07-01 (the first day of the 2-year period ending 2023-06-30) => barred; N; 0. Guide: flat negative. Day-count sensitive at the edge.
27. (b)(3) Prior (a)-sale on 2021-06-30 (the day before the 2-year period begins) => no bar; Y; 100,000. Day-count sensitive at the edge.
28. (b)(3) Prior sale 12 months ago, but that taxpayer elected under (f) not to have section 121 apply to it => no bar ((a) did not apply to it); Y; 100,000.
29. (b)(3) Prior sale 12 months ago at which the taxpayer failed the 2-year test and excluded nothing => no bar; Y; 100,000.

## (b)(4) surviving spouse; (d)(2)

30. (b)(4) Unmarried; spouse died 2022-03-10; sale 2023-06-30; both spouses had owned and used 10 years and neither was barred by (3) immediately before the death; gain 450,000 => 450,000.
31. (b)(4) Same, spouse died 2021-06-30 (sale exactly 2 years after the death), gain 450,000 => 450,000. "Not later than 2 years after".
32. (b)(4) Same, spouse died 2021-06-29 (sale 2 years and 1 day after), gain 450,000 => 250,000. Guide: period fixed in the text's own words; outside it the $500,000 substitution is N.
33. (b)(4) Survivor remarried before the sale and files separately; otherwise as 30; gain 450,000 => 250,000.
34. (b)(4) Survivor had moved in only 1 year before the spouse died (so did not meet the use requirement immediately before the death); spouse died 6 months before the sale; gain 400,000 => 250,000.
35. (d)(2) Unmarried; spouse died 8 months before the sale; survivor's own ownership and use 11 months; the deceased spouse had owned and used it 4 years before death; gain 100,000 => Y; 100,000 (the deceased's period is included).
36. (d)(2) Same but the survivor remarried before the sale => N; 0. The tacking rule is for an unmarried individual; the survivor's own 11 months fail (a). Guide: "if".

## (b)(5) nonqualified use

37. (b)(5)(C)(i) Bought 2000-01-01; rented out 2000-01-01 to 2004-01-01; lived there 2004-01-01 to the sale on 2008-06-30; gain 200,000 => 200,000 (no period of nonqualified use: the rental precedes 2009-01-01).
38. (b)(5) Bought 2009-01-01; rented 2009-01-01 to 2011-01-01; lived there 2011-01-01 to the sale on 2019-01-01; gain 200,000 => 160,000 (2 of 10 years nonqualified; 40,000 allocated; the rental begins ON 2009-01-01 and counts).
39. (b)(5)(C)(i) Bought 2007-01-01; rented 2007-01-01 to 2010-01-01; lived there 2010-01-01 to the sale on 2014-01-01; gain 140,000 => 120,000 (only 2009-01-01 to 2010-01-01 counts: 1 of 7 years; 20,000 allocated).
40. (b)(5)(C)(ii)(I) Bought 2015-01-01; lived there until 2020-01-01; vacant and for sale until the sale on 2021-12-31; gain 100,000 => 100,000 (the vacancy is after the last use inside the 5-year window, so not nonqualified).
41. (b)(5)(C)(ii)(II) Bought 2010-01-01; lived there 2010-01-01 to 2013-01-01; taxpayer on qualified official extended duty (uniformed services, station 200 miles away, indefinite order) 2013-01-01 to 2019-01-01 while it was rented; lived there again 2019-01-01 to the sale on 2023-01-01; gain 200,000 => 200,000 (6 years excepted, under the 10-year cap).
42. (b)(5)(C)(ii)(III) Bought 2010-01-01; lived there until 2012-01-01; away 18 months (to 2013-07-01) because of a change of employment, not on qualified duty; lived there 2013-07-01 to the sale on 2018-01-01; gain 160,000 => 160,000 (within the 2-year exception).
43. (b)(5)(C)(ii)(III) Same, but away 30 months (2012-01-01 to 2014-07-01); lived there again 2014-07-01 to the sale on 2018-01-01 (ownership 8 years); gain 160,000 => 150,000 (2 years excepted, the remaining 6 months nonqualified: 1/16 of 160,000 = 10,000). AMBIGUOUS-prone: the other reading excepts nothing when the absence exceeds 2 years (30/96 x 160,000 = 50,000; excluded 110,000).
44. (b)(5)(C)(i) Bought 2010-01-01; taxpayer lived there 2010-01-01 to 2014-01-01 and 2016-01-01 to the sale on 2020-01-01; the taxpayer's adult child lived there 2014-01-01 to 2016-01-01; gain 150,000 => 120,000 (2 of 10 years nonqualified; 30,000 allocated).
45. (b)(5)(C)(i) Same dates, but 2014-01-01 to 2016-01-01 the taxpayer's spouse lived there as the spouse's principal residence => 150,000 (no nonqualified use).
46. (b)(5)(C)(i) Same dates, but 2014-01-01 to 2016-01-01 the taxpayer's former spouse lived there as the former spouse's principal residence => 150,000 (no nonqualified use).
47. (b)(5)+(b)(1) Facts of 38 with gain 600,000 => 250,000 (120,000 allocated to nonqualified use; the remaining 480,000 is capped at 250,000).
48. (b)(5)(D) Facts of 38 with gain 200,000 of which 50,000 is attributable to post-1997 depreciation adjustments => 120,000 ((d)(6) first removes 50,000; the allocation of 20 percent applies to the other 150,000, removing 30,000).

## (c) failing the tests: a reduced exclusion

49. (c) Bought and used 2022-06-30 to the sale on 2023-06-30 (1 year); the sale is by reason of a change in place of employment; no earlier sale; gain 200,000 => 125,000 (250,000 x 1/2).
50. (c) Same, gain 100,000 => 100,000.
51. (c) Same, but the sale is because the taxpayer wanted a bigger house => N; 0. Guide: "if" in (c)(2)(B) unmet, so (c) does not apply and (a) fails.
52. (c) Same as 49, the sale is by reason of health (doctor-advised move), gain 200,000 => 125,000.
53. (c)(2)(B) Same as 49, the sale is by reason of a divorce (offered as an unforeseen circumstance) => NOTHING. Guide: points outside the sources ("to the extent provided in regulations").
54. (c)(1)(B)(II) Owned and used 2020-06-30 to the sale on 2023-06-30 (3 years); sold another home on 2022-06-30 and excluded the gain under (a); this sale is by reason of a change of employment; gain 200,000 => 125,000 (the shorter period is 1 year: 250,000 x 1/2).
55. (c)(2)(A) BASE (owned and used 4.5 years), sale by reason of a change of employment, gain 200,000 => the (c) rule does not apply: N for (c); excluded 200,000 under (a). Guide: "if".

## (d)(3) property of a spouse or former spouse

56. (d)(3)(A) Husband owned and used 6 years and wife lived there 3 years as his spouse; he transfers it to her in a transaction described in section 1041(a); she sells 3 months later; gain 100,000 => Y; 100,000 (her ownership includes his period).
57. (d)(3)(A) A taxpayer bought the house from a stranger 8 months before the sale and lived there since => N; 0 (no transferor's period to add).
58. (d)(3)(B) Husband owned from 2018-01-01 and lived there until 2018-07-01; a decree of divorce grants the wife use from 2018-07-01 until the sale on 2021-01-01; gain 100,000 => Y; 100,000 (he is treated as using it during the wife's granted use: 3 years).
59. (d)(3)(B) Same but the wife stays on with no decree or written agreement => N; 0.
60. (d)(3)(C)(ii) A written separation agreement is a "divorce or separation instrument" => Y.
61. (d)(3)(C) An oral agreement to separate is a "divorce or separation instrument" => N. Guide: "means" definition, closed.
62. (d)(3)(C)(iii) A decree, not a decree of divorce or separate maintenance, requiring a spouse to pay support to the other spouse is a "divorce or separation instrument" => Y.

## (d)(4) cooperative housing

63. (d)(4) The taxpayer held stock as a tenant-stockholder for 3 years and occupied the apartment as a principal residence for 3 years; gain 100,000 => Y; 100,000.
64. (d)(4) Held the stock 3 years but occupied the apartment only 1 year => N; 0.

## (d)(5) involuntary conversions

65. (d)(5)(A) A principal residence owned and used 5 years is destroyed by fire on 2023-03-01; gain on the insurance proceeds 100,000 => treated as a sale; Y; 100,000.
66. (d)(5)(B) Amount realized 700,000, excluded under section 121 250,000 => the amount realized for section 1033 is 450,000.
67. (d)(5)(C) Old home owned and used 3 years, then condemned; replacement bought at once, basis fixed under section 1033(b), lived in 6 months before sale; gain 100,000 => Y; 100,000 (the old home's holding and use count).
68. (d)(5)(A) The taxpayer gives the house to a charity (neither a sale nor one of the listed events): does section 121 exclude anything? => NOTHING. Guide: the list is not closed with "only", and a gift is silent.

## (d)(6) depreciation

69. (d)(6) Gain 100,000, of which depreciation adjustments attributable to periods after 1997-05-06 total 30,000 => 70,000.
70. (d)(6) Gain 20,000; post-1997-05-06 depreciation adjustments 30,000 => 0.
71. (d)(6) Gain 100,000; depreciation of 40,000 attributable only to periods ending on or before 1997-05-06 => 100,000.
72. (d)(6) Gain 100,000; 30,000 of depreciation attributable to a period beginning 1997-05-07 => 70,000.

## (d)(7) out-of-residence care

73. (d)(7) The taxpayer became incapable of self-care; owned and used the home exactly 1 year (2019-01-01 to 2020-01-01), then lived 3 years in a State-licensed nursing home while still owning it; sale 2023-01-01; gain 100,000 => Y; 100,000.
74. (d)(7)(B) Same but only 11 months of use before the nursing home => N; 0.
75. (d)(7) Same as 73 but the facility is the taxpayer's daughter's house, not licensed => N; 0.
76. (d)(7)(A) Same as 73 but the taxpayer is capable of self-care and chose a licensed retirement home => N; 0.
77. (d)(7) Same as 73 but the facility is a State-licensed assisted-living facility licensed to care for a person in the taxpayer's condition => Y; 100,000. "Including a nursing home" is not a limit.

## (d)(8) remainder interests

78. (d)(8)(A) The taxpayer elects, and sells a remainder interest in the principal residence to an unrelated buyer; owned and used 3 years; gain 100,000 => Y; 100,000.
79. (d)(8)(B) The remainder interest is sold to the taxpayer's sister (a relationship described in section 267(b)) => the election in (A) is unavailable: N. Guide: flat negative "shall not apply".
80. (d)(8)(A) The taxpayer sells a life estate (not a remainder interest) separately => section 121 does not apply: N. Guide: flat negative.

## (d)(9) uniformed services, Foreign Service, intelligence community

81. (d)(9)(A) Bought 2012-01-01; lived there 2012-01-01 to 2014-01-01; on qualified official extended duty (uniformed services, station 200 miles away, order for an indefinite period) 2014-01-01 to 2022-01-01 while it was rented; sale 2022-06-30; the taxpayer ELECTED; gain 100,000 => Y; 100,000.
82. (d)(9)(A) Same facts, NO election => N; 0. Guide: "if" the use falls outside the unextended window.
83. (d)(9)(B) Lived 2007-06-30 to 2009-06-30; on qualified official extended duty 2009-06-30 to 2023-06-30 (14 years); elected; sale 2023-06-30; gain 100,000 => N; 0 (the window can grow by 10 years only, to 2008-06-30: 1 year of use inside).
84. (d)(9)(C)(i) Same as 81 but the duty station is 30 miles from the home and the taxpayer is not in Government quarters => N (not qualified official extended duty; no suspension; (a) fails); 0.
85. (d)(9)(C)(i) Same as 81 but the duty station is exactly 50 miles away => Y; 100,000.
86. (d)(9)(C)(i) Same as 81 but the duty station is 10 miles away and the taxpayer resides in Government quarters under Government orders => Y; 100,000.
87. (d)(9)(C)(v) A call to active duty for exactly 90 days is "extended duty" => N. A call for 91 days => Y. Guide: "means" definition.
88. (d)(9)(C)(v) An order to active duty for an indefinite period is "extended duty" => Y.
89. (d)(9)(D)(i) Same as 81 but an election is already in effect for another property => the election may not be made; N; 0. Guide: flat negative "may not be made".
90. (d)(9)(D)(ii) After revoking the election for property A, the taxpayer may elect for property B => Y.
91. (d)(9)(C)(iv) An employee of the Department of Agriculture is an "employee of the intelligence community" => N. Guide: "means" list. An employee of the Central Intelligence Agency => Y.
92. (d)(9)(A) Same as 81 but the taxpayer's SPOUSE served the duty, taxpayer elected => Y; 100,000.

## (d)(10) like-kind exchange

93. (d)(10) Acquired 2020-01-01 in an exchange with gain not recognized in whole or part under section 1031(a); sold 2024-06-30 (4 years 6 months); lived there 2 years; gain 100,000 => (a) does not apply: N; 0. Guide: flat negative "shall not apply".
94. (d)(10) Same, sale on 2024-12-31 (the last day of the 5-year period beginning 2020-01-01) => N; 0. Day-count sensitive at the edge.
95. (d)(10) Same, sale on 2025-01-01 (the day after) => Y; 100,000. Day-count sensitive at the edge.
96. (d)(10) Same, sale on 2025-06-30 (5 years 6 months) => Y; 100,000.
97. (d)(10) Acquired by an ordinary taxable purchase on 2020-01-01; sold 2024-06-30; lived there 2 years => Y; 100,000. The rule applies only to a section 1031 acquisition.
98. (d)(10) The taxpayer's daughter receives the property by gift with a carryover basis and sells within 5 years of the original 1031 acquisition => (a) does not apply to her: N.

## (d)(12) Peace Corps

99. (d)(12)(A) Lived there 2015-01-01 to 2017-01-01; Peace Corps volunteer outside the United States 2017-01-01 to 2020-01-01; sale 2020-07-01; ELECTED; gain 100,000 => Y; 100,000.
100. (d)(12)(A) Same but the volunteer service was inside the United States => N (no suspension; (a) fails); 0.
101. (d)(12)(B) Same as 99 but an election is already in effect for another property => N; 0. Guide: "rules similar to" (9)(D): flat negative.

## (e), (f), (g)

102. (e) An individual to whom the treatment in section 877(a)(1) applies sells a qualifying home; gain 100,000 => N; 0. Guide: "shall not apply".
103. (e) The individual is not subject to section 877(a)(1); BASE; gain 100,000 => Y; 100,000. The denial does not operate.
104. (f) The taxpayer elects not to have the section apply; BASE; gain 100,000 => N; 0.
105. (g) Property acquired 1996-06-01 in a rollover under section 1034 (nonrecognition of gain on the old residence); the old residence was owned and used 1986-01-01 to 1996-06-01; the new one used 1996-06-01 to the sale on 1997-08-01 (14 months); gain 100,000 => Y; 100,000 (the old residence's periods are included).
106. (g) Same but the home was bought outright, not in a rollover => N; 0.

## The text is silent: "not covered"

107. (a) What tax rate applies to the gain above the ceiling => NOTHING.
108. (a) Whether a LOSS on the sale of a principal residence is deductible => NOTHING.
109. (a) Whether a seasonal vacation cabin the taxpayer visits 8 weeks a year is the taxpayer's "principal residence" => NOTHING (term undefined).
110. (a) Whether the exclusion applies to State income tax => NOTHING.
111. (a) How the gain is computed (amount realized less adjusted basis) => NOTHING (section 1001 is outside the text).
112. (a) Whether the excluded gain escapes the net investment income tax => NOTHING.
113. (f) The deadline for making the election not to have the section apply => NOTHING.
114. (a) Whether the taxpayer must report the sale on a return => NOTHING.
115. (a) Whether land sold separately from the house, within the same lot, may use the exclusion => NOTHING.

## Seat scenarios: an individual taxpayer who has sold, in the person's own facts

116. "I'm single. I bought my house on 2019-01-01, lived in it until I sold it on 2023-06-30, and made 120,000. I haven't sold any other home." => can exclude: Y; excluded 120,000; taxable 0.
117. Same, but my gain was 320,000 => excluded 250,000; taxable 70,000.
118. "We are married and file jointly. I own the house; we both lived in it 4 years; sold 2023-06-30; our gain is 480,000; neither of us sold another home." => excluded 480,000; taxable 0.
119. Same, gain 560,000 => excluded 500,000; taxable 60,000.
120. "I lived in my home only 14 months (bought 2021-04-30, sold 2022-06-30) because I took a job in another city. Gain 80,000. I'm single." => excluded 80,000; taxable 0 (the reduced ceiling, 250,000 x 14/24, is about 145,800).
121. Same, but I moved because I wanted a bigger yard => excluded 0; taxable 80,000.
122. "I excluded the gain on another home I sold 10 months ago. I've lived in this one 4 years. I'm selling because my doctor said I must move. Gain 90,000." => excluded 90,000 (the reduced ceiling is about 104,000).
123. Same, but I'm selling for no particular reason => excluded 0; taxable 90,000.
124. "I owned my home 2010-01-01 to 2020-01-01 and rented it out for 3 years in the middle (2012-01-01 to 2015-01-01); I lived there before and after. Gain 200,000. Single." => excluded 140,000; taxable 60,000.
125. "I lived in my home from 2015-01-01 until 2020-01-01, moved out, and sold it on 2021-12-31. Gain 150,000. Single." => excluded 150,000; taxable 0.
126. "I lived in my home 10 years and claimed 15,000 of depreciation for a home office, all after 1997. Gain 100,000. Single." => excluded 85,000; taxable 15,000.
127. "My spouse died on 2022-03-10; we both lived in our home 10 years; I haven't remarried; I sold it 2023-06-30 for a gain of 400,000." => excluded 400,000; taxable 0.
128. Same, but I sold it 2025-06-30 => excluded 250,000; taxable 150,000.
129. "I own and live in my home for 4 years, but I choose not to have section 121 apply to this sale. Gain 100,000." => excluded 0; taxable 100,000.
130. "I became unable to care for myself. I lived in my home exactly 1 year (2019-01-01 to 2020-01-01), then 3 years in a State-licensed nursing home, still owning it; I sold 2023-01-01; gain 100,000." => excluded 100,000; taxable 0.

## Addendum, written after the first run, repairing facts I got wrong (the originals above stay as they are and stay failing)

Reading the first run's numbers I found five scenarios where MY facts were incomplete: I let ownership begin before use (a period of nonqualified use after 2008 under (b)(5)(C)(i)) or left out a fact the encoding asks for.
The originals are not edited.
The repairs below are new scenarios whose expected values come from the text, decided here before they are run.

R6. (a) Owned from 2018-01-01; used as the principal residence 2018-12-01 to 2019-12-01 and 2022-06-30 to 2023-06-30; sale 2023-06-30 => the two-year-in-five test is met: Y. (Asked of the (a) test alone, since the gap in the middle is nonqualified use under (b)(5).)
R56. (d)(3)(A) As 56, with the husband's (former spouse's) use of the home 2017-06-30 to 2023-03-29 stated as use by a former spouse => 100,000 (his use is not nonqualified use).
R92b. (d)(9)(A) As 92 but the spouse's service is stated in the taxpayer's own list of periods of service (the taxpayer elects) => 100,000.
R95. (d)(10) Acquired 2020-01-01 in a 1031 exchange and lived in it from then on; sold 2025-01-01 (the day after the 5-year period) => 100,000.
R96. (d)(10) Same, sold 2025-06-30 => 100,000.
R97. (d)(10) Bought outright 2020-01-01 and lived in it from then on (no 1031 exchange); sold 2024-06-30 => 100,000.

## Addendum 2, written before running, for the seat's new inputs (surviving spouse, election under (f), care facility)

Expected values below are from the text alone, decided before the assertions were written or run.
Each answer is the amount left out of gross income, then the amount still taxed.

N1. (b)(4), (d)(2) Seat, filing alone: "My spouse died on 2022-03-10. We both lived in our home since 2013-06-30 and I owned it from then. I have not remarried. I sold on 2023-06-30. My gain is 400,000." => left out 400,000; taxed 0. (The limit is 500,000: sale within 2 years of the death and the (2)(A) requirements were met before it.)
N2. (b)(4) Seat, filing alone: same facts, sold on 2025-06-30 (more than 2 years after the death) => left out 250,000; taxed 150,000. Guide: period fixed in the text's own words; outside it the 500,000 substitution is N.
N3. (f) Seat, filing alone: "I am single. I bought my home on 2019-01-01 and lived in it until I sold it on 2023-06-30. My gain is 100,000. I elect not to have section 121 apply." => left out 0; taxed 100,000. Guide: flat negative "shall not apply".
N4. (d)(7) Seat, filing alone: "I became unable to care for myself. I owned my home from 2019-01-01 and lived in it exactly one year (2019-01-01 to 2019-12-31). From 2020-01-01 until I sold it on 2023-01-01 I lived in a State-licensed nursing home that is licensed for my condition. My gain is 100,000. I am single." => left out 100,000; taxed 0. (The nursing-home years count as use; no nonqualified use.)
