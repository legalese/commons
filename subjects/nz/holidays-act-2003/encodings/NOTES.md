# Holidays Act 2003 (New Zealand) — encoding notes

Read this first. `BRIEF.md` is the specification. The source is `../registers/source-bundle/act_public_2003_129.txt`, the PCO's version as at 20 December 2023, converted from its XML on 2026-10-13 (sha256 `45dffd4b…`; `act_public_2003_129.meta.json` beside it).

## 1. What is encoded

**The whole Act**: ss 1-91, Schedule 1AA, and Schedules 1-3 (which carry no operative text in this version).

**What the converted text lacks.** Paragraph labels are gone, so a label in a comment or a constructor name is read from the provision's place in its list. Labels the encoding could not be sure of (s 44(1) after (d), s 75(2), s 81(2)) are left off. The formulas in s 8(2) and s 9A(2) have lost their symbols; the encoding reads them as `(a − b) ÷ c` and `a ÷ b`, the variables in the order the text defines them. That reading should be checked against the PDF (open question 1).

**Inputs.** These are taken as given rather than worked out:
- who is an employee (ERA s 6) and who is "involved" (ERA s 142W);
- whether a day would otherwise be a working day (s 12), except that the public-holiday calendar reads it from the weekdays the employee usually works;
- what the employee would have received on a day, and gross earnings over a period (s 14 is encoded, as a sum over typed payments, for a reader who wants to build the figure);
- Matariki Observance Day (Schedule 1 of the Te Kāhui o Matariki Public Holiday Act 2022) and the local anniversary day;
- agreements between employer and employee, Labour Inspector determinations, whether an employer accepts a bereavement under s 69(2)(b), and whether an employer's choice of day under s 57(2) is reasonable;
- the days left in the current sick or family violence leave entitlement.

**Dates from outside the text.** Three commencement dates come from the amending Acts, not from this text: the Holidays Amendment Act 2016 (1 April 2016), Part 2 of the Domestic Violence—Victims' Protection Act 2018 (1 April 2019, when subpart 5 began), and the Holidays (Increasing Sick Leave) Amendment Act 2021 (24 July 2021). The encoding refuses what falls under the text as it stood before each of them: penalties and s 77A recovery for conduct before 1 April 2016, family violence leave before 1 April 2019, and sick leave in a 12-month period that began before 24 July 2021. It also refuses a public-holiday calendar before 2022, when Matariki was added to s 44(1).

### The top-level goal

`the holiday pay position for` a `Holiday event` (`ha-goal.l4`, `@export default`) answers: *for this holiday or leave event, is the employee entitled, how much must the employer pay at least, when is it due, does the employee earn an alternative holiday, and how much entitlement is used?* The event is one of: an annual holiday, the end of the employment, a public holiday, an alternative holiday taken, a spell of sick, bereavement or family violence leave, a closedown, a cash-up of annual holidays, or an exchange of an alternative holiday.

| goal | question | main functions | provisions | module |
| --- | --- | --- | --- | --- |
| 1 | What are the pay measures? | `the ordinary weekly pay` (`@export`), `the daily pay` (`@export`), `the gross earnings in` (`@export`), `the average weekly earnings over 12 months…` | ss 5, 8-10A, 14, 16(3) | `ha-pay.l4` |
| 2 | Annual holidays: entitlement, pay, timing, cash-up, closedowns, ending the employment | `the annual holiday pay for` (`@export`), `the annual holiday pay owed at the end of` (`@export`), `the payout for` (`@export`), `the closedown position for` (`@export`), `the day the employee becomes entitled to annual holidays…` | ss 16-40 | `ha-annual.l4` |
| 3 | Public holidays: which days, what pay, alternative holidays | `the public holidays for the employee in` (`@export`), `the pay for the public holiday` (`@export`), `the employee earns an alternative holiday for` (`@export`), `the alternative holiday meets s 57`, `the public holidays in the notional holiday after…` | ss 40(3), 44-61A | `ha-public.l4` |
| 4-5 | Sick, bereavement and family violence leave | `the leave position for` (`@export`), `the sick leave available for the period beginning…` (`@export`), `the bereavement leave for`, `the employer may require proof of sickness or injury` | ss 63-72J; Schedule 1AA cls 4, 5 | `ha-leave.l4` |
| 6 | Enforcement and records | `the maximum penalty under s 75 for a breach of…` (`@export`), `the arrears recoverable under s 77A by…` (`@export`), `the last day to commence a penalty action…`, `the holiday and leave record meets s 81`, `the employment is treated as continuous…` | ss 73-91; Schedule 1AA cls 1-2 | `ha-enforcement.l4` |

## 2. Coverage table

| provision | disposition |
| --- | --- |
| ss 1-7 | carried as text (s 6(3): a term that reduces an entitlement has no effect, which is why a lower special rate under ss 8(3), 9(1A) is ignored) |
| s 8 | Goal 1 |
| ss 9, 9A, 10, 10A | Goal 1 |
| s 11 | carried as text (a Labour Inspector's determination is an input; `the average daily pay` refuses where s 9A(2) gives nothing) |
| ss 12, 13 | input; s 12 read from the usual weekdays for the calendar |
| s 14 | Goal 1 |
| s 15 | carried as text |
| s 16 | Goals 1, 2 |
| s 17 | carried as text (the 4 weeks are counted in weeks) |
| s 18(1) | Goal 2 |
| s 18(2)-(4), s 20 | carried as text |
| s 19 | Goal 2 |
| ss 21-27 | Goal 2 |
| s 28 | Goal 2 |
| ss 28A, 28B, 28E | Goal 2 |
| ss 28C, 28D, 28F | carried as text |
| ss 29, 31 | carried as text |
| ss 30, 32-35 | Goal 2 |
| ss 36-40 | Goals 2, 3 |
| ss 41, 42, 58 | no text in this version |
| s 43 | carried as text |
| ss 44-45A | Goal 3 |
| s 46 | Goal 3 (through s 48) |
| ss 47-50 | Goal 3 |
| s 51 | carried as text (it ran out in 2007, or when the existing collective agreement was replaced) |
| ss 52, 53 | Goal 3 |
| s 54 | carried as text |
| ss 55-57, 59-61A | Goal 3 |
| s 62 | carried as text |
| s 63 | Goals 4, 5 |
| s 64 | carried as text |
| ss 65-72 | Goal 4 |
| ss 72A, 72E, 72G | carried as text (s 72G: proof may always be required; its effect on payment is in `the leave position for`) |
| ss 72B-72D, 72F, 72H-72J | Goal 5 |
| s 73 | carried as text |
| ss 74-76 | Goal 6 (s 76(2)-(4), (6) carried as text) |
| ss 76A, 76B, 77, 78-80 | carried as text |
| s 77A | Goal 6 |
| ss 81-83 | Goal 6 (s 81(3A)-(3C), (5) carried as text) |
| s 84 | carried as text |
| s 85 | Goal 6 |
| ss 86-91 | carried as text |
| Schedule 1AA cls 1-2 | Goal 6 (the 2016 gate) |
| Schedule 1AA cls 3-4 | Goal 5 (the 2019 gate) |
| Schedule 1AA cl 5 | Goal 4 (the 2021 gate) |
| Schedules 1-3 | no operative text |

`provisions carried as text` in `ha-enforcement.l4` lists the text-only provisions.

## 3. Fork register

| id | provision | question | reading taken | why |
| --- | --- | --- | --- | --- |
| F1 | s 8(2) | Is c still 4 where a pay period longer than 4 weeks is used? | Yes | "c is 4", with no exception |
| F2 | ss 9A, 49, 60, 71, 72I | When is average daily pay used instead of relevant daily pay? | Where relevant daily pay cannot be determined, always; where it can, only if daily pay varies in the pay period and the employer chooses average daily pay | s 9A(1) "An employer may use" |
| F3 | s 16(2)(a)(vi), (b) | Other unpaid leave longer than 1 week | Left out of the 12 months whole, not only the days beyond the first week | "(vi) ... for a period of no more than 1 week" describes the period |
| F4 | ss 19(2), 32(3), 57(3) | "not less than 14 days' notice" | 14 clear days between the notice and the day: notice on 1 December allows a start on 16 December, not 15 | The Legislation Act 2019's rule that a number of days between 2 events, expressed as "not less than", excludes the days on which the events happen. That Act is outside the bundle; the independent author, reading this Act alone, counted 14 days by date difference (§4) |
| F5 | s 16(1)-(2) | Effect of unpaid leave not counted | The 12 months end later by the length of that leave | The 12 months "does not include" it |
| F6 | ss 18(1), 61(2), 76(5) | "within 12 months after" a date | The first anniversary of the date is the last day (and, for s 61(2), the first day on which 12 months "have passed") | The period runs from the day after the date |
| F7 | s 22(2)(b)(ii) | Has the employee "worked for the employer for not less than 12 months"? | Counted to the end of the last pay period before the holiday | That is the end of the period the average is taken over |
| F8 | ss 23(2), 25(2), 34(2) | Holiday pay paid in advance or under s 28 exceeds the 8% | Nothing is owed; the excess is not recoverable under this Act | "less any amount"; the Act gives no clawback |
| F9 | s 33(3) | The part of a closedown beyond an entitled employee's entitlement, with no agreement | Unpaid under this Act | s 33 gives pay only for annual holidays, and for the rest only by agreement |
| F10 | s 44(2) | Does s 44(2) apply after ss 45, 45A move a holiday? | Yes: holidays treated as falling on the same day count once (ANZAC Day 2038, a Sunday, moved to Easter Monday) | ss 45, 45A apply "for the purposes of this subpart", and so does s 44(2) |
| F11 | s 66(2) | Carry-over | The new period's 10 days plus up to 10 unused days, never more than 20 | "up to 10 days' sick leave to a maximum of 20 days' current entitlement" |
| F12 | s 40(2)-(3) | The rate for public holidays in the notional holiday on termination | Relevant or average daily pay for the last day of employment | s 40(3) gives no rate; s 60(2)(b) uses this one for untaken alternative holidays at the same moment. Only for an employee entitled to annual holidays (s 40(2)(b)) |

Also read, without a fork: Easter by the Gregorian computus (the Act names Good Friday and Easter Monday without saying how they are found); bereavement leave is not deducted from any balance (s 70 grants it per bereavement); days paid ACC weekly compensation are neither paid nor deducted (s 71(2)-(3)); an agreement entered into on 1 April 2004 is refused, being neither "before" (s 5) nor "after" (s 52(1)) that day.

## 4. Tests

`L4=~/.local/bin/l4 ./check.sh` on 2026-10-15:

| module | errors | satisfied | failed |
| --- | --- | --- | --- |
| `ha-tests.l4` (encoder) | 0 | 292 | 0 |
| `tests-independent.l4` | 3 | 295 | 3 |
| the 7 rule modules | 0 | 0 | 0 |
| **total** | 3 | 587 | 3 |

**3 failures are expected**, and they are why `check.sh` exits non-zero. They are the independent author's three notice cases (ss 19(2), 32(3), 57(3)): notice on 1 December for 15 December, which the author counted as 14 days and the encoding, by fork F4, as 13 clear days. Neither side's expected value has been changed; a New Zealand lawyer should settle it (open question 2). The 3 errors are those 3 failed assertions; there are no others.

The independent pass (`INDEPENDENT-TEST-REPORT.md`) found one error, now fixed: public holidays in the notional holiday (s 40(3)) were paid to an employee not yet entitled to annual holidays. It also found two gaps, now closed: the cash-up and closedown rates ignored the s 16(3) divisor, and a cash-up was not limited to the entitlement not yet taken. Before the fixes, 294 of its 298 assertions passed.

**Known limits** (the encoding answers them only through inputs): the s 63(1)(b) hours test (the date it was first met is an input); whether the employee is entitled at the end of the employment; the series-of-fixed-terms rule in s 28; which provision a breach falls under for s 75. The s 28 subsection labels are inferred from unlabelled text and may be off by one.

## 5. Open questions for a New Zealand employment lawyer

1. ss 8(2), 9A(2): confirm the formulas against the official print (the converted text has lost their symbols).
2. F4: is 14 days' notice counted in clear days (notice on 1 December allows 16 December), or by date difference (15 December)?
3. F1: should the s 8(2) divisor follow a pay period longer than 4 weeks?
4. F9: is the uncovered part of a closedown unpaid for an entitled employee who does not agree to take holidays in advance?
5. F10: does ANZAC Day, moved by s 45A onto Easter Monday, give one public holiday or two?
6. F12: at what rate is a public holiday paid under s 40(3)?
