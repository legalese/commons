# Independent expectations: Immigration Act 2009 (NZ), ss 9, 15-17, 21, 154, 157, 161, 167, 185, 350

Written from BRIEF.md and the Act text (as at 10 July 2026) only, before any `.l4` file was opened.
Expected values below are fixed; they are not to be changed after the encoding is read.

## Conventions and readings taken

- **"not later than N days after D"** (ss 154(2), 154(4), 157(4), 161(2), 185(2)(a)): Legislation Act 2019 s 54 — a period "after" a day does not include that day. The last permitted day is D + N calendar days, inclusive. 42 days after 1 Mar 2026 = 12 Apr 2026.
- **"N days from the date of service"** (s 157(2)): "from" a day also excludes the day; last day = service + N.
- **"at any time in the preceding 10 years"** (s 15(1)(b)) and **"preceding 12 months"** (s 350(4)): ambiguous at the boundary. Reading taken: the window is the 10 years (12 months) ending on the day before the assessment date, so it opens on the same calendar day 10 years (12 months) earlier; a conviction (notice) on that exact anniversary day is *inside*. Exact-day scenarios are flagged AMBIGUOUS; the clear-side scenarios are not.
- **"not later than N years after the person first held a residence class visa"** (s 161(1)): the offence date must be on or before first-held date + N years (same calendar day, inclusive).
- **Excluded time (s 161(3), s 167(2))**: the period is extended by the number of days excluded, i.e. end = start + N years + excluded days. Ambiguity: whether imprisonment outside the window (e.g. after it would otherwise have closed) also counts, and whether adding days before or after the year arithmetic matters around 29 Feb. I add days after the year arithmetic, and use only imprisonment/suspension falling inside the period. Scenarios avoid 29 Feb.
- **s 167(1) "for a period of 10 years following the arising"**: the period starts the day after liability arises and ends on the 10th anniversary of the arising date; liable on that anniversary, not liable the day after.
- **Sentence lengths** in months (5 years = 60 months). s 15(2) / s 161(4) aggregation (cumulative or single sentences, suspended or deferred) is done by the caller, per the brief: the input is the already-aggregated term.
- **s 161 "power to impose imprisonment for a term of 3 months or more"** is the offence's maximum penalty (an input).
- Assessment date for s 15/16/17 scenarios is **10 Jul 2026** unless stated.

## Goal 1: Eligibility (ss 15-17)

| id | inputs | expected | provision / words relied on |
|---|---|---|---|
| E15-01 | conviction 1 Jan 1990, sentence 60 months | NOT eligible | s 15(1)(a) "at any time ... sentenced to imprisonment for a term of 5 years or more" |
| E15-02 | conviction 1 Jan 1990, sentence 59 months | eligible (too old for (b), under 5 yrs for (a)) | s 15(1)(a),(b) |
| E15-03 | conviction 1 Jan 1990, indeterminate sentence capable of running 5 yrs or more | NOT eligible | s 15(1)(a) "or for an indeterminate period capable of running for 5 years or more" |
| E15-04 | conviction 1 Jan 2020, sentence 12 months | NOT eligible | s 15(1)(b) "in the preceding 10 years ... 12 months or more" |
| E15-05 | conviction 1 Jan 2020, sentence 11 months | eligible | s 15(1)(b) threshold not met |
| E15-06 | conviction 1 Jul 2016, sentence 24 months | eligible (outside preceding 10 yrs) | s 15(1)(b) |
| E15-07 | conviction 15 Jul 2016, sentence 24 months | NOT eligible | s 15(1)(b) |
| E15-08 | conviction 10 Jul 2016, sentence 24 months (AMBIGUOUS boundary) | NOT eligible (anniversary day inside) | s 15(1)(b) "preceding 10 years" |
| E15-09 | conviction 1 Jan 2020, sentence 12 months, suspended | NOT eligible | s 15(2)(a) "whether ... suspended in whole or in part" |
| E15-10 | two 7-month cumulative sentences same proceedings 1 Jan 2020, caller passes 14 months | NOT eligible | s 15(2)(b) (aggregation by caller) |
| E15-11 | conviction 1 Jan 2020, indeterminate sentence capable of running 12 months+ (but < 5 yrs) | NOT eligible | s 15(1)(b) |
| E15-12 | subject to period of prohibition under s 179 | NOT eligible | s 15(1)(c) |
| E15-13 | deported from NZ under this Act, still subject to s 179 prohibition | NOT eligible | s 15(1)(c),(d) |
| E15-14 | deported from NZ under this Act, no longer subject to prohibition | eligible | s 15(3)(c) "is not, or is no longer, subject to a period of prohibition" |
| E15-15 | removal order under s 54 former Act, expired/cancelled | eligible | s 15(3)(b) |
| E15-16 | deported under s 158 Shipping and Seamen Act 1952 | eligible | s 15(3)(a) |
| E15-17 | deported under s 20 Immigration Act 1964 for s 14(5)/15(5) offence | eligible | s 15(3)(d) |
| E15-18 | deported from NZ under another enactment, no exception | NOT eligible | s 15(1)(d) "removed or deported from New Zealand under any enactment" |
| E15-19 | excluded from NZ under any enactment | NOT eligible | s 15(1)(e) |
| E15-20 | removed / deported / excluded from another country | NOT eligible | s 15(1)(f) |
| E15-21 | no convictions, no history | eligible | s 15 nothing applies |
| E16-01 | Minister believes likely to commit offence punishable by imprisonment | NOT eligible | s 16(a)(i) |
| E16-02 | Minister believes threat to security | NOT eligible | s 16(a)(ii) |
| E16-03 | Minister believes threat to public order | NOT eligible | s 16(a)(iii) |
| E16-04 | Minister believes threat to public interest | NOT eligible | s 16(a)(iv) |
| E16-05 | member of designated terrorist entity | NOT eligible | s 16(b) |
| E16-06 | no beliefs | eligible | s 16 |
| E17-01 | E15-01 facts + special direction | visa may be granted (not barred) | s 17(1)(a) "Despite sections 15 and 16 ... may be granted ... in accordance with a special direction" |
| E17-02 | E16-02 facts + grant under s 83 | may be granted | s 17(1)(b) |
| E17-03 | E15-04 facts, holder of permanent resident visa | entry permission MUST be granted | s 17(2)(a)(i) |
| E17-04 | E15-04 facts, resident visa granted in NZ | entry permission MUST be granted | s 17(2)(a)(ii) |
| E17-05 | E15-04 facts, resident visa granted offshore, first arrival | no s 17(2) entitlement; still barred | s 17(2)(a)(iii) "second or subsequent time" |
| E17-06 | E15-04 facts, resident visa, second arrival as holder | entry permission MUST be granted | s 17(2)(a)(iii) |
| E17-07 | E16-03 facts, diplomatic immunity | visa and entry permission MUST be granted | s 17(2)(b) |
| E17-08 | s 17(3) absolute discretion; s 17(4) s 75A | not expressible as a test (discretion) | s 17(3),(4) |

## Goal 2: Unlawful status and work (ss 9, 21, 154, 185)

| id | inputs | expected | provision |
|---|---|---|---|
| U9-01 | in NZ, holds visa, granted entry permission | lawful | s 9(1) |
| U9-02 | in NZ, no visa | UNLAWFUL | s 9(1)(a) "is not the holder of a visa" |
| U9-03 | in NZ, visa, no entry permission | UNLAWFUL | s 9(1)(b) |
| U9-04 | not in NZ, no visa | not unlawfully in NZ | s 9(1) "if the person is in New Zealand" |
| U9-05 | arrived 5 Mar 2026, never lawful | unlawful from 5 Mar 2026 | s 9(2)(a) "starting on the date the person arrived" |
| U9-06 | visa expired 31 Jan 2026, no other granted | unlawful from 1 Feb 2026 | s 9(2)(b) "the day after the date on which the person's visa expired" |
| U9-07 | visa cancelled 10 May 2026, no other granted | unlawful from 11 May 2026 | s 9(2)(b) "or was cancelled" |
| U9-08 | visa expired 31 Jan 2026, query 31 Jan 2026 | lawful on that date | s 9(2)(b) |
| U9-09 | visa expired 31 Jan 2026, query 1 Feb 2026 | unlawful | s 9(2)(b) |
| U9-10 | visa expired 31 Jan 2026, new visa granted 31 Jan 2026 | lawful | s 9(2)(b) "without another visa being granted" |
| U9-11 | former-Act permit expired 30 Jun 2010, no new permit | unlawful from 1 Jul 2010 | s 9(2)(c) |
| U9-12 | born in NZ on/after 1 Jan 2006, not citizen | start date per ss 373-374: out of scope, REFUSE (not expressible as a date) | s 9(2)(d) |
| U21-01 | unlawfully in NZ | may NOT work | s 21(a) |
| U21-02 | lawfully in NZ | s 21 no bar | s 21 |
| U154-01 | unlawful | liable for deportation | s 154(1) |
| U154-02 | lawful | not liable under s 154 | s 154(1) |
| U154-03 | became unlawful 1 Feb 2026, no reconsideration | appeal deadline 15 Mar 2026 | s 154(2) "not later than 42 days after first becoming unlawfully" |
| U154-04 | became unlawful 1 Mar 2026 | deadline 12 Apr 2026 | s 154(2) |
| U154-05 | unlawful 1 Feb 2026 after s 185 reconsideration; confirmation received 20 Feb 2026 | deadline 3 Apr 2026 | s 154(4)(b) "later of" |
| U154-06 | unlawful 1 Feb 2026 after s 185 reconsideration; confirmation 10 Jan 2026 | deadline 15 Mar 2026 | s 154(4)(a) |
| U154-07 | unlawful after cancellation under s 64(1)(ab) | no appeal right | s 154(5)(a) |
| U154-08 | already had opportunity to appeal (unexercised) | no appeal right | s 154(5)(b) "whether exercised or not" |
| U154-09 | s 167(3): unlawful person's s 154 liability persists while unlawful (no 10-year end) | liable on any date while unlawful | s 167(3) |
| R185-01 | temp visa holder onshore, applied during currency, declined by officer, notice received 3 Mar 2026, applies 17 Mar 2026, still lawful | MAY apply | s 185(2)(a),(b) |
| R185-02 | same, applies 18 Mar 2026 | may NOT apply | s 185(2)(a) "not later than 14 days" |
| R185-03 | same, applies 10 Mar 2026, but no longer lawfully in NZ | may NOT apply | s 185(2)(b) |
| R185-04 | decline made by the Minister | section does not apply; no right | s 185(1)(c) |
| R185-05 | applied for further visa after current visa expired (not during currency) | no right | s 185(1)(a) |
| R185-06 | offshore applicant | no right | s 185(1)(a) "is onshore" |

## Goal 3: Deportation liability (ss 157, 161, 167)

s 157 (Minister's determination is an input):

| id | inputs | expected | provision |
|---|---|---|---|
| D157-01 | temp visa holder, Minister determines sufficient reason | liable | s 157(1) |
| D157-02 | no determination | not liable under s 157 | s 157(1) |
| D157-03 | notice served 2 Mar 2026 | reasons due by 16 Mar 2026 | s 157(2) "14 days from the date of service" |
| D157-04 | same, limited visa holder | no 14-day right | s 157(3)(a) |
| D157-05 | same, Minister determines excluded person | no 14-day right | s 157(3)(b) |
| D157-06 | notice served 2 Mar 2026, temporary visa holder | appeal by 30 Mar 2026 | s 157(4) "not later than 28 days after" |
| D157-07 | limited visa holder | no s 157(4) appeal (only temporary or interim visa holders) | s 157(4) |

s 161 (residence class visa holder; first held 1 Jul 2020 = granted in NZ unless stated; no imprisonment unless stated):

| id | offence date / facts | expected | provision |
|---|---|---|---|
| D161-01 | committed 1 Jul 2022, max penalty 3 months | LIABLE | s 161(1)(a)(iii) "not later than 2 years after" (inclusive) |
| D161-02 | committed 2 Jul 2022, max penalty 1 year | not liable | (a)(iii) out of time, (b) penalty < 2 yrs |
| D161-03 | committed 1 Jan 2021, max penalty 2 months | not liable | (a) "3 months or more" not met |
| D161-04 | committed 2 Jul 2022, max penalty 2 years | LIABLE | s 161(1)(b) |
| D161-05 | committed 1 Jul 2025, max penalty 2 years | LIABLE | s 161(1)(b) inclusive |
| D161-06 | committed 2 Jul 2025, max penalty 2 years, sentence 1 yr | not liable | s 161(1)(b) out of time |
| D161-07 | committed 1 Jan 2024, max penalty 23 months | not liable | (b) "2 years or more" not met, (a)(iii) out of time |
| D161-08 | committed 1 Jul 2030, sentenced 60 months | LIABLE | s 161(1)(c) |
| D161-09 | committed 2 Jul 2030, sentenced 60 months | not liable | s 161(1)(c) out of time |
| D161-10 | committed 1 Jan 2027, sentenced 59 months, max 14 yrs | not liable | (c) "5 years or more" not met; (b) out of time |
| D161-11 | committed 1 Jan 2027, sentenced 60 months | LIABLE | s 161(1)(c) |
| D161-12 | committed 1 Jan 2027, indeterminate sentence capable of 5 yrs+ | LIABLE | s 161(1)(c) |
| D161-13 | s 350(1) offence committed 1 Jul 2030 | LIABLE | s 161(1)(d) |
| D161-14 | s 350(1) offence committed 2 Jul 2030 | not liable | s 161(1)(d) |
| D161-15 | s 351 offence committed 1 Jan 2029 | LIABLE | s 161(1)(d) |
| D161-16 | committed 1 Mar 2015 while unlawfully in NZ, max 3 months (first held 2020) | LIABLE | s 161(1)(a)(i) "at any time ... when the person was unlawfully in New Zealand" |
| D161-17 | committed 1 Mar 2018 while holding temp visa, max 6 months | LIABLE | s 161(1)(a)(ii) |
| D161-18 | committed while unlawful, max 2 months | not liable | s 161(1)(a) threshold |
| D161-19 | committed 9 Oct 2022, max 1 yr, 100 days imprisonment inside the 2-yr window | LIABLE (window ends 9 Oct 2022) | s 161(3) "exclusive of any time spent ... in imprisonment" |
| D161-20 | committed 10 Oct 2022, same 100 days | not liable | s 161(3) |
| D161-21 | committed 2 Jul 2022, max 1 yr, 0 days imprisonment | not liable (control for D161-19) | s 161(3) |
| D161-22 | visa granted offshore 1 Mar 2020, first arrived with entry permission 1 Sep 2020; offence 15 Aug 2022, max 6 months | LIABLE (first held 1 Sep 2020) | s 161(5)(b) |
| D161-23 | same as D161-22 but offence 2 Sep 2022 | not liable | s 161(5)(b) |
| D161-24 | first held 1 Jul 2015; absent 1 Jul 2018-1 Jan 2024 (5y6m); re-entered with entry permission 1 Jan 2024; offence 1 Jun 2025, max 6 months | LIABLE (first held reset to 1 Jan 2024) | s 161(5)(c) "continuous period of absence ... at least 5 years" |
| D161-25 | same but absence only 4 years (1 Jul 2018-1 Jul 2022), offence 1 Jun 2025 max 6 months | not liable (first held stays 1 Jul 2015) | s 161(5)(c) |
| D161-26 | not a residence class visa holder | not liable under s 161 | s 161(1) |
| D161-27 | liability notice served 10 Jun 2026 | appeal by 8 Jul 2026 | s 161(2) "not later than 28 days after being served" |
| D161-28 | refugee/protected person appeal against RPO decision | not expressible beyond the date (no input/output beyond deadline) | s 161(2)(b) |

s 167:

| id | inputs | expected | provision |
|---|---|---|---|
| D167-01 | residence visa holder; liability arose 1 Mar 2020; no exclusions | liability ends 1 Mar 2030 | s 167(1) |
| D167-02 | same; query 1 Mar 2030 | still liable | s 167(1) |
| D167-03 | same; query 2 Mar 2030 | no longer liable | s 167(1) |
| D167-04 | arose 1 Mar 2020; 200 days imprisonment | ends 17 Sep 2030 | s 167(2)(a) |
| D167-05 | arose 1 Mar 2020; 365 days suspension (s 172) | ends 1 Mar 2031 | s 167(2)(b) |
| D167-06 | arose 1 Mar 2020; 200 days imprisonment + 365 days suspension | ends 17 Sep 2031 | s 167(2) |
| D167-07 | query 1 Jul 2030 with 200 days imprisonment | still liable | s 167(2)(a) |
| D167-08 | s 154 (unlawful) liability | no end date while unlawful | s 167(3) (see U154-09) |

## Goal 4: Employers (s 350)

Work day examined: 1 Jul 2026; employee is not entitled to do the work unless stated.

| id | inputs | expected | provision |
|---|---|---|---|
| S350-01 | employer actually knows | OFFENCE | s 350(1) "knowing that the person is not entitled" |
| S350-02 | no knowledge, no notice | no offence | s 350(1) |
| S350-03 | written notice from immigration officer 1 Sep 2025 | OFFENCE (deemed knowledge) | s 350(4) "at any time in the preceding 12 months ... informed ... in writing" |
| S350-04 | written notice 1 Jun 2025 (13 months before) | no offence | s 350(4) |
| S350-05 | written notice 1 Jul 2025 (AMBIGUOUS boundary) | OFFENCE (anniversary day inside) | s 350(4) |
| S350-06 | written notice 10 Jul 2026 (after the work day) | no offence on 1 Jul 2026 | s 350(4) "preceding" |
| S350-07 | oral notice only 1 Sep 2025, no actual knowledge | no offence | s 350(4) "in writing" |
| S350-08 | actual knowledge, but work on that day is within the minimum notice period under the employment agreement | NOT liable | s 350(5) |
| S350-09 | notice 1 Sep 2025, work within the notice period | NOT liable | s 350(5) |
| S350-10 | actual knowledge, work day outside the notice period | OFFENCE | s 350(5) limited to "any period during which" |
| S350-11 | employee entitled to do the work, employer "knows" nothing | no offence | s 350(1) |
| S350-12 | work began before Act commenced | irrelevant; OFFENCE if knowing | s 350(2) |
| S350-13 | s 350(3) charge particulars | not expressible (procedural) | s 350(3) |

## Top-level goal

| id | inputs | expected |
|---|---|---|
| T-01 | person: visa expired 31 Jan 2026, in NZ, no convictions, assessed 10 Jul 2026 | unlawful; may not work; liable under s 154; humanitarian appeal deadline 15 Mar 2026 |
| T-02 | resident visa holder, first held 1 Jul 2020, offence 1 Jul 2022 max 3 months, notice served 10 Jun 2026 | lawful; liable under s 161; appeal by 8 Jul 2026 |
| T-03 | person with 60-month conviction 1990 | not eligible for visa |

## Added after reading the encoding: scenarios not expressible

(Expected values above are unchanged. These scenarios have no function or input in the encoding, so no assertion was written.)

- E15-14 to E15-17: the s 15(3) exceptions are not modelled; the caller folds them into one flag (`removed or deported ..., outside the s 15(3) exceptions`). Only the "flag FALSE gives not barred" consequence is tested.
- E16-01 to E16-05: one s 16 flag; the limbs are not separate inputs (tested once).
- E17-03 to E17-08: s 17(2) (mandatory entry permission for permanent/resident visa holders, diplomats), s 17(3), s 17(4): no input or output.
- U9-04: no "in New Zealand" input; s 9(1) is evaluated as if the person is in NZ.
- U9-08, U9-09: `is unlawfully in New Zealand` takes no date; status on a given day is not queryable.
- U9-11: s 9(2)(c) former-Act permits: no input.
- U9-12: s 9(2)(d) (born in NZ on/after 1 Jan 2006): no input, no REFUSE.
- U154-01, U154-02: no separate s 154(1) liability function (same as unlawful status).
- U154-07, U154-08: s 154(5) exclusions: no input.
- U154-09, D167-08: s 167(3): no function.
- R185-04 to R185-06: s 185(1) preconditions: no input.
- D157-01, D157-02, D157-04, D157-05, D157-07: s 157(1) liability and the s 157(3) / s 157(4) exclusions: no input (only the 14/28-day date arithmetic exists).
- D161-26: no "residence class visa holder" flag in the s 161 function (top-level uses NOTHING for non-residents).
- D161-28: s 161(2)(b): not an input/output test.
- D161-22 to D161-25: s 161(5) "first held" is supplied by the caller, so only the downstream consequence is tested, not the s 161(5) computation.
- S350-13: s 350(3) procedural.
