# Independent expectations: Electricity Act 1989 (customer's seat)

Written from BRIEF.md and the source text only, before any `.l4` file was opened.

Bank holidays used (input list, England and Wales): 2026 — 1 Jan, 6 Apr, 4 May, 25 May,
31 Aug, 28 Dec; plus 1 Jan 2027 and 29 Mar 2027 where a scenario runs into 2027. Christmas
Day and Good Friday (3 Apr 2026, 26 Mar 2027) are excluded by s 64(1) itself and are never
put in the list. "BH" below means that list; "no BH" means an empty list.

## Date conventions, and where I read the Act differently from the brief

* "not less than seven working days' notice" (s 17(3), Sch 6 para 2(2)(b)) and "at least two
  working days' notice" (paras 7(5), 8(4)): the brief says the act may be done on or after the
  7th (2nd) working day after the day of the notice. I follow that for the main assertions.
  **Dissent:** the settled rule for "not less than N days' notice" is clear days (both the day
  of giving and the day of the act are excluded: *Re Railway Sleepers Supply Co* (1885);
  *R v Turner* [1910]). On that reading the earliest day is the next working day after the
  7th (2nd) working day. Scenarios C9 and N12 record that reading, and are expected to fail
  against an encoding that follows the brief; they are findings about the brief, not the code.
* Sch 6 para 2(3), "the period of 28 days after the making ... of a demand": the period is
  demand+1 .. demand+28; payment on demand+28 is in time; the power exists from demand+29.
  Agree with the brief.
* s 23(1C), "12 months beginning with the time when the connection is made": ends the day
  before the anniversary; a 29 Feb start ends 28 Feb. Agree with the brief.
* s 20(3): whole 50p sums times whole three-month periods (a period is complete on the
  corresponding date three months on, last day of month where there is none). Agree.
* s 27G(5), 27K, 27M(2): "from" excludes the day; ends on the corresponding date / day +7 /
  day +42. Agree with the brief.
* s 17(3) applies only to disconnection under s 17(1)(c). A disconnection under s 20(1A)(b)
  (security not given) needs no s 17(3) notice. (The Act gives no notice period there.)

## Goal 1 — Connection (ss 16, 16A, 17, 20, 22, 23)

| # | Facts | Expected | Words of the Act |
|---|---|---|---|
| C1 | Occupier requires connection; s 16A notice specifies premises, date and max power; no s 17 circumstance; no special agreement; security given | duty applies: TRUE | s 16(1)(a)(i) "when required to do so by the owner or occupier" |
| C2 | As C1 but required by an authorised supplier acting with the owner's consent | TRUE | s 16(1)(a)(ii) |
| C3 | As C1 but the s 16A notice does not specify the maximum power | no duty yet (FALSE) | s 16A(1)-(2)(c) "That notice must specify ... the maximum power" |
| C4 | As C1 but distributor prevented by circumstances not within his control | FALSE | s 17(1)(a) |
| C5 | Circumstances would involve breach of s 29 regulations, and distributor has taken all reasonable steps | FALSE (exception) | s 17(1)(b) |
| C5b | Same circumstances, but distributor has NOT taken all reasonable steps | TRUE (exception fails) | s 17(1)(b) "and he has taken all such steps as it was reasonable to take" |
| C6 | Connection not in accordance with designated strategic plans | FALSE | s 17(1)(ba) |
| C7 | Not reasonable in all the circumstances (input) | FALSE | s 17(1)(c) |
| C8 | Needs Sch 3/4 power without consent; licence does not provide for it; consent not given at request — all three | FALSE | s 17(2)(a)-(c) |
| C8b | As C8 but consent had been given at the time of request | TRUE | s 17(2)(c) |
| C8c | Special connection agreement effective | s 16 duty does not govern (FALSE) | s 22(2) "rights and liabilities ... those arising under the agreement and not those provided for by sections 16 to 21" |
| C8d | Security required and not given, connection not yet made | distributor may refuse (duty does not compel): FALSE | s 20(1A)(a) |
| C8e | Security not given, connection being maintained | distributor may disconnect: TRUE (may disconnect) | s 20(1A)(b) |
| C9 | Maintained connection, s 17(1)(c); notice to occupier Mon 30 Mar 2026; BH | earliest disconnection Fri 10 Apr 2026 (Good Friday 3 Apr and Easter Monday 6 Apr skipped) | s 17(3) "not less than seven working days' notice"; s 64(1) |
| C9a | same, disconnection on Thu 9 Apr / Fri 10 Apr / Mon 13 Apr 2026 | not permitted / permitted / permitted | s 17(3) |
| C9b | same notice, no BH (Good Friday still excluded by s 64, Easter Monday then a working day) | Thu 9 Apr 2026 | s 64(1) "Good Friday" |
| C9c | notice Mon 21 Dec 2026; BH incl. 28 Dec 2026, 1 Jan 2027 | Mon 4 Jan 2027 | s 64(1) "Christmas Day", bank holidays |
| C9d | notice Mon 21 Dec 2026; no BH | Thu 31 Dec 2026 (Christmas Day still out) | s 64(1) |
| C9e | notice Fri 9 Oct 2026 / Sat 10 Oct 2026; BH | Tue 20 Oct 2026 in both cases | s 64(1) Saturdays, Sundays |
| C9f | notice Fri 1 May 2026; BH (4 May) | Wed 13 May 2026 | s 64(1) |
| C9g | **Dissent (clear days)**: notice Mon 30 Mar 2026; BH | Mon 13 Apr 2026 | "not less than seven working days' notice" |
| C9h | Disconnection under s 17(1)(c) with no notice given | not permitted | s 17(3) "unless the distributor gives ... notice" |
| C10 | Deposit £100.25, rate £0.01 per 50p per 3 months, 15 Jan 2026 to 15 Jul 2026 | 200 sums x 2 periods x £0.01 = £4.00 | s 20(3) "on every sum of 50p ... for every three months" |
| C10a | same deposit, returned 14 Jul 2026 | 1 period: £2.00 | s 20(3) |
| C10b | same deposit, returned 14 Apr 2026 | £0.00 | s 20(3) |
| C10c | deposit £0.49, a year | £0.00 (no whole 50p) | s 20(3) |
| C10d | deposit £10.00, rate £0.02, 31 Aug 2026 to 30 Nov 2026 | 20 x 1 x 0.02 = £0.40 (three months from 31 Aug end 30 Nov) | s 20(3) |
| C11 | connection made 15 Mar 2026 | last day to refer: 14 Mar 2027 | s 23(1C) "12 months beginning with the time when the connection is made" |
| C11a | reference on 14 Mar 2027 / 15 Mar 2027 | in time / too late | s 23(1C) |
| C11b | connection made 29 Feb 2028 | 28 Feb 2029 | s 23(1C) |
| C11c | connection made 1 Mar 2027 | 29 Feb 2028 (leap year) | s 23(1C) |
| C11d | connection made 1 Jan 2026 | 31 Dec 2026 | s 23(1C) |

## Goal 2 — Non-payment and entry (Sch 6 paras 2, 5, 7, 8, 10)

| # | Facts | Expected | Words |
|---|---|---|---|
| N1 | demand Mon 2 Mar 2026, unpaid | requisite period ends 30 Mar 2026; power from 31 Mar 2026 | para 2(3) "period of 28 days after the making ... of a demand" |
| N2 | demand 2 Mar 2026, notice Fri 20 Mar 2026; BH | earliest day 31 Mar 2026 (7th working day after notice is also 31 Mar) | para 2(1), 2(2)(b), 2(3) |
| N3 | demand 2 Mar 2026, notice Wed 25 Mar 2026; BH | earliest 7 Apr 2026 (notice limb governs; Easter skipped) | para 2(2)(b) |
| N3a | N3 facts; act on 2 Apr / 7 Apr 2026 | may not / may | para 2(2)(b) |
| N4 | demand 1 Feb 2026; paid 1 Mar 2026 | paid within the period: no power | para 2(1) "has not, within the requisite period, made all the relevant payments" |
| N4a | demand 1 Feb 2026; paid 2 Mar 2026 | power exists (earliest 2 Mar 2026, subject to notice) | para 2(3) |
| N5 | demand 1 Feb 2028 (leap) | earliest 1 Mar 2028 (period ends 29 Feb) | para 2(3) |
| N5a | demand 31 Jan 2026 | earliest 1 Mar 2026 (period ends 28 Feb) | para 2(3) |
| N6 | whole amount genuinely in dispute | power may not be exercised | para 2(2)(a) |
| N6a | dispute is only under s 39 (standards of performance) | disregarded: power may be exercised | para 2(2)(a) "disregarding for this purpose a dispute under section 39" |
| N7 | no notice of intention given | may not exercise | para 2(2)(b) |
| N8 | Officer enters to install pre-payment meter; supplier authorised by para 2(1); reasonable time; 2 working days' notice given Thu 2 Apr 2026, entry Wed 8 Apr 2026; produces document | may enter | para 7(4), 7(5), 10(4) |
| N8a | same, entry Tue 7 Apr 2026 | may not (only one working day after notice) | para 7(5) |
| N8b | same, no authenticated document | may not | para 10(4) "only ... on production of some duly authenticated document" |
| N8c | same, not at a reasonable time | may not | para 7(4) "at all reasonable times" |
| N9 | Entry to disconnect for non-payment (para 8(3)(a)); notice Thu 24 Dec 2026, entry Wed 30 Dec 2026; BH | may enter (Christmas Day, 28 Dec skipped; 2nd WD = 30 Dec) | para 8(3)(a), 8(4) |
| N9a | same, entry 29 Dec 2026 | may not | para 8(4) |
| N10 | 2 WD notice Thu 25 Mar 2027 with 29 Mar 2027 in list | earliest entry Wed 31 Mar 2027 (Good Friday 26 Mar 2027 computed) | s 64(1) |
| N11 | Customer restores connection after supplier disconnection, without supplier's consent | offence, level 3 fine: TRUE | para 5(1)-(2) |
| N11a | restored with supplier's consent | no offence | para 5(1) "without the consent of the supplier" |
| N11b | disconnection was under regulations under s 29, restored without consent | para 5 does not apply: no offence | para 5(1) "otherwise than in the exercise of a power conferred by regulations under section 29" |
| N12 | **Dissent (clear days)**: 2 WD notice Thu 2 Apr 2026, entry Wed 8 Apr 2026 | may not (clear days: earliest Thu 9 Apr) | para 7(5) |

## Goal 3 — Redress and resale (ss 27G-27O, 44)

| # | Facts | Expected | Words |
|---|---|---|---|
| R1 | contravention 10 Mar 2020, loss to consumers, no final/provisional order, order given 10 Mar 2025 | can be made | s 27K(1) "not later than the end of the period of 5 years from the time of the contravention" |
| R1a | same, order 11 Mar 2025, no saving notice | cannot | s 27K(1) |
| R1b | same, order 11 Mar 2025, s 27I(1) notice served 1 Mar 2025 | can | s 27K(2)(a) |
| R1c | contravention 29 Feb 2020; order 28 Feb 2025 / 1 Mar 2025 | can / cannot | s 27K(1) |
| R2 | final order made 30 Nov 2024; 27I notice 28 Feb 2025 / 1 Mar 2025 | can / cannot | s 27K(3)(a) "within 3 months from ... the making of the final order" |
| R2a | provisional order confirmed 15 Jan 2025; notice 15 Apr / 16 Apr 2025 | can / cannot | s 27K(3)(a) |
| R2b | provisional order made 31 Aug 2024, not confirmed; notice 28 Feb 2025 / 1 Mar 2025 | can / cannot | s 27K(3)(b) "within 6 months" |
| R3 | Authority satisfied Competition Act 1998 the most appropriate way | cannot | s 27N(2) |
| R4 | contravention in 2010 (before Energy Act 2013 Sch 14 in force) | cannot | s 27N(4) |
| R5 | no loss, damage or inconvenience to consumers | cannot | s 27G(1)(b) |
| R6 | service 24 Dec 2025 | earliest compliance date 31 Dec 2025; 30 Dec invalid | s 27G(5) "not ... earlier than the end of the period of 7 days from the date of the service" |
| R6a | service 25 Feb 2028 | earliest 3 Mar 2028 (leap day counted); 2 Mar invalid | s 27G(5) |
| R7 | service 1 Mar 2026 | last day for appeal 12 Apr 2026; 13 Apr late | s 27M(2) "within 42 days from the date of service" |
| R7a | appeal made and not determined | compliance suspended | s 27M(5) |
| R8 | compliance date 31 Jan 2026, unpaid | interest runs from 1 Feb 2026 at the Judgments Act rate | s 27N(1) |
| R8a | paid by 31 Jan 2026 | no interest | s 27N(1)(b) |
| R9 | turnover £1,000,000, compensation £150,000, no penalty | maximum compensation £100,000 | s 27O(2) "may not exceed 10 per cent of the person's turnover" |
| R9a | turnover £1,000,000, penalty £60,000, compensation ordered £50,000 | combined cap £100,000; compensation at most £40,000 | s 27O(3)-(4) |
| R9b | turnover £1,000,000, penalty £120,000 | compensation at most £0 (the combined cap is already used up) | s 27O(4) |
| R10 | max resale price 30p/kWh, charged 35p, 1,000 kWh | excess £50.00 recoverable | s 44(4)(a) |
| R10a | charged 28p | £0.00 | s 44(4) "at a price exceeding the maximum price" |
| R10c | as R10, direction provides interest of £5 | £55.00 | s 44(4)(b) |
| R10b | reseller failed to give information; direction reduces maximum by 10% (30p to 27p); charged 30p, 1,000 kWh | excess £30.00 | s 44(2)(b), 44(4) |


Note added at step 3: R9b was recast (the encoding gives the cap, not the capped award), and R10c was added. No expected value was changed after the code was read.
