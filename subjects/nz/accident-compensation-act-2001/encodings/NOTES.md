# Accident Compensation Act 2001 (New Zealand) — encoding notes

Read this first. `BRIEF.md` is the specification; `../source/PROVENANCE.md` says where the text came from.

## 1. What is encoded

**The whole Act** (Parts 1–11 and Schedules 1AA, 1–8), as in the PCO's version 249 as at 10 July 2026. It is encoded from the PDF the user supplied; the text is deposited and the PDF is not.

**Inputs.** These are taken as given rather than worked out:
- the Corporation's, the Minister's and the courts' discretions, opinions and findings;
- regulations, including lump sum amounts between the floor and ceiling, levy rates and interest rates;
- **indexed amounts**: the figures in Schedule 1 cls 46, 56, 64, 65 and 76 are encoded as the Act prints them, but ss 115–116 index them, so current figures should be supplied by the caller;
- minimum weekly earnings (cl 42(3));
- whether a fact falls within Schedules 2, 3 and 3A.

### The top-level goal

`the ACC position for` an `Injury case` (`acc-goal.l4`) answers: *for this injury, does the person have cover; what kind of injury is it and which Account pays; and what weekly compensation is payable after the first five weeks?*

Weekly compensation is worked out only for an employee in permanent employment (cl 34). The goal does not ask whether the employment is permanent: it applies cl 34 to every `an employee`, so a caller with a non-permanent employee (cls 35-36) must not rely on that figure. A non-earner gets 0 (no cl 32 entitlement). For the self-employed, shareholder-employees and potential earners it is NOTHING, because those formulas are carried as text or need facts the case does not carry.

| goal | question | main functions | provisions | module |
| --- | --- | --- | --- | --- |
| 1 | Is there an accident and a personal injury; is there cover; what class of injury; which Account? | `the occurrence is an accident`, `an accident under s 25…`, `a personal injury`, `a treatment injury`, `has cover, injury…`, `ordinarily resident…`, `a work-related gradual process injury…`, `a motor vehicle injury`, `the class of injury…`, `the Account that pays for…`, `a gradual process injury is suffered on…` | ss 17, 20-38; 166-228 | `acc-cover.l4` |
| 2 | Is the claim in time; by when must it be decided; is cover deemed? | `a claim is due by…`, `a complicated claim…`, `the claim must be decided by…`, `cover is deemed…`, s 66, s 75 | Part 3 | `acc-claims-disputes.l4` |
| 3 | What first week, weekly and lump sum compensation; what for survivors; what is barred? | `first week compensation…`, `weekly compensation starts on…`, `the weekly earnings of a permanent employee…`, `the weekly earnings after the low-earner rule…`, `the weekly compensation on weekly earnings of…`, `potential earner compensation…`, cl 52, s 112, s 87, s 114, `entitled to a lump sum…`, `the lump sum for impairment of…`, the funeral, survivor and child care rules, `the entitlement is barred by…` | Part 4; Schedule 1 | `acc-entitlements.l4` |
| 4 | Is the review in time; when is it decided or deemed; when is an appeal due? | `the review application is in time…`, `a review decision is deemed for the applicant…`, s 148, `the appeal must be filed by…`, `an appeal lies to the District Court…`, s 162 | Part 5 | `acc-claims-disputes.l4` |
| 5 | When is a levy due; refunds, adjustments, penalties; purchased weekly compensation | ss 168, 172, 173, 174, 231, 232, 243, 249, 250, 254, 181, 209, 223, 226, 214(4)(b) | Part 6 | `acc-levies-offences.l4` |
| 6 | Offences, penalties, limitation, proceedings | `the maximum penalty for`, ss 309, 316(2), 313, 317-319 | Part 9 | `acc-levies-offences.l4` |

## 2. Coverage table

| provision | disposition |
| --- | --- |
| ss 1-16, 18, 18A | read into the facts |
| s 17 | Goal 1 |
| ss 20-23, 25-30, 32, 35, 37 | Goal 1 |
| ss 21A, 24, 25A, 31, 33, 34, 36, 38 | carried as text |
| ss 39-52, 54, 55, 59-64, 65(1), (3)-(5) | carried as text |
| ss 53, 56-58, 65(2), 66, 75 | Goal 2 |
| ss 67-96 | carried as text (rehabilitation), except s 75 (Goal 2) and s 87(2) (Goal 3) |
| ss 97, 112, 114, 119-123, 126, 127, 129 | Goal 3 |
| ss 98-111, 113, 115-118, 124, 125, 128, 130-132 | carried as text |
| Schedule 1 Part 1 | carried as text |
| Schedule 1 Part 2 cls 32, 34, 42, 46, 47, 51, 52 | Goal 3; the other earnings formulas carried as text |
| Schedule 1 Part 3 cls 54, 56, 57, 59(6) | Goal 3; cls 55-55D, 58, 60-62 carried as text |
| Schedule 1 Part 4 cls 63-66, 70, 71, 74, 76, 77 | Goal 3; cls 67, 72, 75, 78 carried as text |
| ss 133-164 | Goal 4 (ss 135, 141, 144, 146, 148, 149, 151, 152, 162); the rest carried as text |
| ss 165-258 | Goal 5 (the sections in §1); the rest carried as text |
| Parts 7, 8 | carried as text |
| ss 294-336C | Goal 6 (ss 98(3), 160(4), 242, 308-310, 313, 315-319, 335); the rest carried as text |
| Parts 10, 11; Schedules 1AA, 2-8 | carried as text (Schedules 2, 3 and 3A as inputs) |

## 3. Fork register

| id | provision | question | reading taken | why |
| --- | --- | --- | --- | --- |
| F1 | s 25(1)(d), (e) "1 month" | How long is a month? | 30 days; "exceeding 1 month" means more than 30 days | The inputs are day counts; a calendar-month reading would need dates |
| F2 | ss 28(5), 228(3) | Is a treatment injury from treatment of a work injury a treatment injury? | It is classed as work-related and paid from the Work Account | s 228(3) excludes it from the Treatment Injury Account; s 28(5) makes it work-related |
| F3 | s 17(1)(a), (3) | A person now in New Zealand: what shows a permanent place of residence? | An input. The 183-day test applies only to an absent person | s 17(3) speaks of a person "although absent" |
| F4 | Schedule 1 cl 34(1) "each of the 4 weeks after the first week" | Which weeks use the 4-week figure? | Weeks 2 to 5 of incapacity | The text |
| F5 | Schedule 1 cl 56 | The lump sum between 10% and 80% | The regulation amount, kept within $2,500–$100,000 | cl 56(1)-(4) |
| F6 | s 313(1) "the year in which the offence was committed" | Which year? | The calendar year | The text gives no other year |
| F7 | s 121(2) | Lump sums while in prison | Treated as barred while in prison | Assessments and payments are not required while a prisoner |
| F8 | s 22(3)-(4) | A treatment injury abroad: whose residence, and when? | For a treatment injury, `ordinarily resident in New Zealand` is read as residence when the treatment was given; (4)(a)-(b), the provider's equivalent qualifications, are folded into `caused by treatment` | (4)(c) fixes residence at the time of treatment and makes residence at the injury date irrelevant |
| F9 | ss 21(2)(b), 21B(2)(c) | For mental injury, what do "in New Zealand" and "ordinarily resident" refer to? | Where the act or event took place, and residence at that time | ss 21(3), 21B(3) make residence when the mental injury is suffered irrelevant; the place and residence that matter are those of the act or event |

## 4. Tests

`L4=~/.local/bin/l4 ./check.sh` on 2026-10-12: **8 modules, 0 errors, 551 assertions satisfied, 0 failed, 0 warnings**.

- `acc-tests.l4`, the encoder's tests: 236 assertions, with expected values worked from the text.
- `tests-independent.l4`, the independent pass: 315 assertions. A separate agent wrote `independent-expectations.md` from the brief and the text before it read the encoding. Its first run was 308/315. All seven disagreements were encoding errors, and they are fixed:
  1. s 22(3)-(4): a treatment injury abroad was covered before 1 July 2005 (E53).
  2. s 21(2)(b)(ii): a Schedule 3 act abroad on a person not then ordinarily resident was covered (E55).
  3. s 21B(2)(c): the same for a work event abroad (E66).
  4. s 17(3) was treated as the only route for an absent person; it is sufficient, not necessary (E69).
  5. s 250(4): the first penalty fell on day 210, which is still "within 210 days" (E237).
  6. s 35(1)(b): a work-related mental injury from a vehicle crash was classed as a motor vehicle injury (E90).
  7. A non-earner's weekly compensation was NOTHING rather than 0 (E137).

  Its report also said the goal ignored s 228(3), because it passed `for a work injury: FALSE`. `Treatment facts` now carries `the treatment was for a work-related injury`, and the goal uses it.
- **Plumbing-only edits** to `tests-independent.l4`: the fixture `tf` sets the new field to FALSE. No expected value was changed.
- **Two of the encoder's own expected values were wrong** and were corrected against the text, each with a comment in `acc-tests.l4`. They were s 21 abroad without residence (same misreading as item 2) and s 250(4) day 210 (item 5).
- The harness was shown to fail. A copy of the tests with a deliberately wrong assertion, run inside this directory, reports `assertion failed`.

The independent report's other observations are listed in `INDEPENDENT-TEST-REPORT.md`, under "Triage by the encoder".

## 5. Open questions

- F1: whether "1 month" in s 25 is a calendar month.
- Indexed figures: the encoding uses the figures printed in the Act, so callers must supply current indexed amounts.
- F8, F9: the reading of the residence input for treatment injury abroad and for ss 21/21B.
- Whether the goal should take the cl 34-36 employment pattern as an input, so that non-permanent employees can be computed.

## 6. Checks

See `encoding.json` → `checks`.

## Legislation Act 2019 s 55 (added 2026-10-17)

At the user's direction, the next-working-day rule in s 55 of the Legislation Act 2019 ("A thing that, under legislation, must or may be done on a particular day or within a limited period of time may, if that day or the last day of that period is not a working day, be done on the next working day") now applies to the deadlines for lodging a claim (s 53), deciding claims (ss 54-57), deciding the need for a rehabilitation plan (s 75), applying for review (s 135), the review decision (s 144), paying review costs (s 148), appealing (s 151) and seeking leave (s 162), the Corporation's list for the Registrar (s 152), recovering levies (s 226), a ceasing employer's notice (s 232), laying a charge (s 336) and an estate's application (s 120); not the s 146 deemed decision, whose date is tied to the 3 months. The working day is the Legislation Act s 13 meaning, because s 55 is in that Act; the Matariki Observance Days are the statutory dates in Schedule 1 of the Te Kāhui o Matariki Public Holiday Act 2022 (to 2052; later years are refused). The rule lives in `acc-s55.l4`. Dates of entitlement, earliest days and periods of liability are not deadlines for doing something, and are not moved (fork S55).

`check.sh` on 2026-10-17: 549 satisfied (238 encoder, 311 independent), 4 failed (4 independent assertions written before the s 55 change). The encoder's tests whose deadlines moved were changed and marked; tests of the rule were added.
