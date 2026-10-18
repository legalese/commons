# Independent expectations: CEMA 1979 (Sch 3, s 170, Sch 1, s 149, s 146A)

Written from BRIEF.md and the Act's text only (source bundle, point in time 29 April 2026), before any `.l4` file was opened. Each scenario gives inputs, the expected answer, and the words relied on.

Conventions:
- "fixed sum" is the summary sum printed as "the prescribed sum £20,000"; the brief makes it an input. Unless stated, fixed sum = £20,000.
- Dates follow the brief: Sch 3 para 3 one month = on or before the corresponding date one month later, clamped to the last day of the month if none; s 146A(2)/(3) "period of N years beginning with" = ends the day before the corresponding date; s 146A(3) six months "from" = on or before the corresponding date six months later (clamped).

## Goal 1. Seizure and condemnation (Sch 3 paras 1, 3, 4, 5, 6)

Para 1(1): "The Commissioners shall, except as provided in sub-paragraph (2) below, give notice of the seizure ... to any person who to their knowledge was at the time of the seizure the owner or one of the owners thereof."
Para 1(2): "Notice need not be given ... if the seizure was made in the presence of— (a) the person whose offence or suspected offence occasioned the seizure; or (b) the owner or any of the owners of the thing seized or any servant or agent of his; or (ba) a person who has (or appears to have) possession or control of the thing being seized; or (c) in the case of any thing seized on or from any ship or aircraft, the master or commander, or (d) in the case of any thing seized on or from a vehicle, the driver of the vehicle."

| # | Inputs | Expected | Words |
|---|--------|----------|-------|
| F1 | nobody listed present; seized at a warehouse | notice required | para 1(1) |
| F2 | offender present | notice not required | para 1(2)(a) |
| F3 | owner present | not required | para 1(2)(b) "the owner" |
| F4 | owner's servant or agent present | not required | para 1(2)(b) "servant or agent of his" |
| F5 | person in (apparent) possession or control present | not required | para 1(2)(ba) |
| F6 | seized from a ship, master present | not required | para 1(2)(c) |
| F7 | seized from an aircraft, commander present | not required | para 1(2)(c) |
| F8 | master/commander present but goods seized from a vehicle (not ship/aircraft) | notice required | (c) applies only "in the case of any thing seized on or from any ship or aircraft" |
| F9 | seized from a vehicle, driver present | not required | para 1(2)(d) |
| F10 | driver present but goods seized from a ship | notice required | (d) only "on or from a vehicle" |
| F11 | several present (offender + driver) | not required | any one limb suffices |

Para 3: "within one month of the date of the notice of seizure or, where no such notice has been served on him, within one month of the date of the seizure".

| # | Inputs | Expected last day for claim | Words |
|---|--------|-----------------|-------|
| C1 | seizure 10 Mar 2025, notice served 15 Mar 2025 | 15 Apr 2025 | runs from date of the notice |
| C2 | seizure 10 Mar 2025, no notice served | 10 Apr 2025 | "where no such notice has been served ... date of the seizure" |
| C3 | notice 31 Jan 2025 | 28 Feb 2025 | no 31 Feb; last day of month (brief) |
| C4 | notice 31 Jan 2024 (leap) | 29 Feb 2024 | as above |
| C5 | seizure 31 Jan 2023, no notice | 28 Feb 2023 | |
| C6 | seizure 30 Jan 2024, no notice | 29 Feb 2024 | |
| C7 | notice 31 Mar 2025 | 30 Apr 2025 | |
| C8 | notice 15 Dec 2025 | 15 Jan 2026 | year rollover |
| C9 | notice 31 Aug 2025 | 30 Sep 2025 | |
| C10 | seizure 29 Feb 2024, no notice | 29 Mar 2024 | |

Para 5: "If on the expiration of the relevant period ... no such notice has been given ..., or if, in the case of any such notice given, any requirement of paragraph 4 above is not complied with, the thing in question shall be deemed to have been duly condemned as forfeited."
Para 6: "Where notice of claim ... is duly given in accordance with paragraphs 3 and 4 above, the Commissioners shall take proceedings for the condemnation of that thing by the court".

| # | Inputs | Expected | Words |
|---|--------|----------|-------|
| D1 | notice 15 Mar 2025; claim 15 Apr 2025 (last day), para 4 met | proceedings (not deemed condemned) | "within one month"; para 6 |
| D2 | notice 15 Mar 2025; claim 16 Apr 2025, para 4 met | deemed condemned | late = no notice given within the period; para 5 |
| D3 | no claim at all | deemed condemned | para 5 first limb |
| D4 | claim in time (1 Apr 2025), para 4 not met | deemed condemned | para 5 second limb |
| D5 | no notice served, seizure 31 Jan 2025; claim 28 Feb 2025, para 4 met | proceedings | |
| D6 | no notice served, seizure 31 Jan 2025; claim 1 Mar 2025 | deemed condemned | |
| D7 | notice 31 Jan 2024; claim 29 Feb 2024, para 4 met | proceedings | |
| D8 | claim on seizure day itself (before notice), para 4 met, notice 15 Mar, seizure 10 Mar, claim 10 Mar | proceedings | "within one month of" read as not later than the end; a claim before the notice is not out of time |
| D9 | late claim and para 4 not met | deemed condemned | |

## Goal 2. Penalties (s 170, Sch 1, s 149)

Offence, s 170(1): "(a) knowingly acquires possession of any of the following goods ... (i) unlawfully removed from a warehouse ...; (ii) chargeable with a duty which has not been paid; (iii) ... prohibition or restriction ...; or (b) is in any way knowingly concerned in carrying, ... or in any manner dealing with any such goods, and does so with intent to defraud Her Majesty of any duty payable on the goods or to evade any such prohibition or restriction".
s 170(2): "in any way knowingly concerned in any fraudulent evasion or attempt at evasion (a) of any duty ...; (b) of any prohibition or restriction ...; (c) of any provision of the Customs and Excise Acts 1979 ...".
s 170(5): no s 170 offence where it is "in connection with a prohibition or restriction" and there is "a corresponding offence under the enactment ... imposing the prohibition or restriction, being an offence for which a fine or other penalty is expressly provided".

| # | Inputs | Expected | Words |
|---|--------|----------|-------|
| O1 | knowingly acquires duty-unpaid goods, intent to defraud duty | guilty | (1)(a)(ii) + intent |
| O2 | knowingly acquires duty-unpaid goods, no intent | not guilty under (1) | "and does so with intent" |
| O3 | not knowing, intent | not guilty | "knowingly" |
| O4 | knowingly concerned in carrying prohibited goods, intent to evade prohibition | guilty | (1)(b) + (iii) |
| O5 | knowingly acquires goods unlawfully removed from warehouse, intent | guilty | (1)(a)(i) |
| O6 | knowingly concerned in fraudulent evasion of duty | guilty | (2)(a) |
| O7 | knowingly concerned in an attempt at evasion of a prohibition | guilty | (2)(b) "or attempt at evasion" |
| O8 | (2)(b) case + corresponding offence with express penalty | not guilty | (5) |
| O9 | (2)(a) duty-only case + corresponding offence flag set (no prohibition) | guilty | (5) only "in connection with a prohibition or restriction" (reading) |
| O10 | goods of none of kinds (i)-(iii), knowing, intent, no (2) involvement | not guilty | |
| O11 | (2)(c) provision of the Acts evaded, knowingly concerned | guilty | (2)(c) |

Maximum penalties (fixed sum F; value V). s 170(3): summary "the prescribed sum £20,000 or ... three times the value of the goods, whichever is the greater, or ... imprisonment ... not exceeding 6 months"; indictment "penalty of any amount, or ... not exceeding 14 years".

| # | Kind; V; F | Summary penalty | Summary prison | Indictment |
|---|-----------|----------|-------|-----|
| P1 | ordinary; 5,000; 20,000 | 20,000 | 6 months | any amount, 14 years |
| P2 | ordinary; 10,000; 20,000 | 30,000 | 6 months | 14 years |
| P3 | ordinary; 8,000; 20,000 | 24,000 | 6 m | 14 y |
| P4 | ordinary; 1,000; 1,000 (E&W prescribed sum) | 3,000 | 6 m | 14 y |
| P5 | ordinary; 0; 20,000 | 20,000 | | |
| P6 | Class A; 100,000; 20,000 | 300,000 | 6 months | life (Sch 1 (b)(i)) |
| P7 | Class A; 2,000; 20,000 | 20,000 | 6 m | life |
| P8 | Class B; 50,000 | 150,000 | 6 m | 14 years (Sch 1 (b)(ii)) |
| P9 | temporary class drug; 1,000 | 20,000 | 6 m | 14 years |
| P10 | Class C; 100 | 500 (floor) | 3 months | 14 years |
| P11 | Class C; 200 | 600 | 3 months | 14 y |
| P12 | Class C; 10,000; F=20,000 | 30,000 (F irrelevant) | 3 m | 14 y |
| P13 | Class C; 1,000; F=20,000 | 3,000, NOT 20,000 — Sch 1 Class C text has no prescribed sum | 3 m | 14 y |
| P14 | Class C; 0 | 500 | | |
| P15 | s 170(4A) weapons; 1,000 | 20,000 | 6 months | life ("imprisonment for life") |
| P16 | weapons; 50,000 | 150,000 | 6 m | life |
| P17 | seal skins; 100,000 | 20,000 (no three-times-value; "a fine not exceeding the statutory maximum £20,000") | 3 months | any amount, 2 years |
| P18 | seal skins; 1,000 | 20,000 | 3 m | 2 years |
| P19 | s 149(1): aggregate of summary term + default term | 15 months | | |

All indictment money penalties: "a penalty of any amount" (unlimited).

## Goal 3. Time limits (s 146A)

s 146A(2): "shall not be commenced after the end of the period of 20 years beginning with the day on which the offence was committed."
s 146A(3): "shall not be commenced after the end of the period of 3 years beginning with that day but, subject to that, may be commenced at any time within 6 months from the date on which sufficient evidence ... came to the knowledge of the prosecuting authority."

| # | Inputs | Expected last day | Note |
|---|--------|------|------|
| T1 | indictable, offence 1 Mar 2010 | 28 Feb 2030 | 20y ends day before 1 Mar 2030 |
| T2 | indictable, offence 15 Jun 2005 | 14 Jun 2025 | |
| T3 | indictable, offence 1 Jan 2000 | 31 Dec 2019 | |
| T4 | indictable, offence 29 Feb 2004 | 28 Feb 2024 | corresponding date 29 Feb 2024 exists |
| T5 | indictable, offence 29 Feb 2000 | 28 Feb 2020 | |
| T6 | indictable, offence 1 Mar 2004 | 29 Feb 2024 | day before 1 Mar 2024 (leap) |
| S1 | summary, offence 1 Jan 2020, evidence 1 Mar 2020 | 1 Sep 2020 | 6-month end earlier than 3y end (31 Dec 2022) |
| S2 | summary, offence 1 Jan 2020, evidence 1 Oct 2022 | 31 Dec 2022 | 3y end (31 Dec 2022) earlier than 6m end (1 Apr 2023) |
| S3 | summary, offence 1 Jan 2020, evidence 30 Jun 2022 | 30 Dec 2022 | 6m = 30 Dec 2022 < 31 Dec 2022 |
| S4 | summary, offence 1 Jan 2020, evidence 1 Jul 2022 | 31 Dec 2022 | 6m = 1 Jan 2023 > 3y end; 3y wins |
| S5 | summary, offence 10 May 2021, evidence 31 Aug 2023 | 29 Feb 2024 | 6m: no 31 Feb, clamp to 29 Feb 2024; 3y end 9 May 2024 |
| S6 | summary, offence 10 May 2021, evidence 31 Aug 2022 | 28 Feb 2023 | clamp non-leap |
| S7 | summary, offence 1 Mar 2021, evidence 1 Sep 2023 | 29 Feb 2024 | 6m = 1 Mar 2024; 3y ends day before 1 Mar 2024 = 29 Feb 2024; 3y wins |
| S8 | summary, offence 29 Feb 2020, evidence 15 Dec 2022 | 28 Feb 2023 | AMBIGUOUS: 3y from 29 Feb 2020 has no corresponding date; my reading: the 3-year period ends 28 Feb 2023 (the last day before 1 Mar 2023); 6m = 15 Jun 2023 |
| S9 | summary, offence 1 Jan 2020, evidence 1 Jan 2020 (same day) | 1 Jul 2020 | |
| S10 | summary, offence 1 Jan 2020, evidence 1 Feb 2023 (after 3y end) | 31 Dec 2022 | earlier of the two; proceedings already barred |
| S11 | summary, offence 31 Mar 2019, evidence 31 Aug 2019 | 29 Feb 2020 | leap clamp |

## Ambiguities and readings

1. Para 3 period start when notice served after seizure: runs from the notice date; a claim before the notice date is not late (D8).
2. Late claim treated as "no such notice has been given" within the relevant period (para 5).
3. s 146A(3) for an offence on 29 Feb (S8): corresponding date three years on does not exist. Read the period as ending 28 Feb 2023 (the anniversary falls at the start of 1 Mar). An alternative clamp-then-subtract reading gives 27 Feb 2023; I regard that as wrong because it shortens the period by a day.
4. s 170(5) applies only where the offence is in connection with a prohibition or restriction (O9).
5. Class C summary penalty ignores the fixed sum: Sch 1 substitutes "three times the value of the goods or £500, whichever is the greater".
6. Seal skins summary penalty is the fixed sum only, with no three-times-value alternative; whether "statutory maximum £20,000" equals the input fixed sum is assumed yes.
7. s 146A(3) when evidence arrives after the 3-year period: the "last day" is the 3-year end, even though it is before the evidence date.
