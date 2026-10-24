# South Carolina Family Independence (S.C. Code ch. 43-5) — baseline encoding

## Method

**Baseline.** Written straight from the deposited text, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18. No REFUSE; checked with the stable `l4` of VS Code extension 1.6.98, `JL4_LIBRARY_PATH` unset. No pipeline, no coverage table, no independent test pass, no human gate. **Not for public use as advice.**

There was no earlier encoding of this chapter. No requirement ledger exists for US states.

Every question is a function named as the applicant would ask it, with `@export` and a `@desc` on every input, grouped under `§§` headings.

## Edition

South Carolina Code of Laws Unannotated, Title 43, Chapter 5, "current through the 2025 Session of the General Assembly", as deposited at `../../registers/source-bundle/sc-code-title-43-chapter-5-public-aid-family-independence-act.txt` (retrieved 2026-10-19 UTC; sha256 of the text in the `.meta.json`). No regulation is brought in: the Code of Regulations chapter 114 (DSS) is not deposited (see the state README).

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `sc-fi.l4` | `sc-fi-cases.l4` | 51 written, 51 satisfied |

`l4 run` on both files: 0 errors, 0 warnings (2026-10-24). Three `#TRACE`s check two breaches and an unused permission, each with an `-- expect:` comment; all three gave the expected result. Every expected value was written by hand from the text.

## Seat

**The applicant for or recipient of Family Independence**: the parent or caretaker relative applying for a needy family with a child. Questions: "Does my family meet the conditions?", "Are our assets within the limit?", "How much of our income counts?", "Can we still get it under the time limits?", "Must I take part in employment and training?", "When do benefits start?", "Will the grant go up for a new baby?", "By when must I report a change, or ask for a review?", "How much can be taken from my grant to recover an overpayment?".

Provisions addressed to the Department of Social Services are encoded for what they mean to the applicant: the interview and Social Security number conditions (s 43-5-65), timely notice (s 43-5-45), the department's ten days to act on a change (s 43-5-140(d)), and the 90% floor on recovery (s 43-5-30(c)(2)).

Defaults followed:
- **The chapter alone.** No regulation: the need standard and payment standard are not in the chapter and are not deposited; the one question that needs the payment standard takes it as an input.
- **The actors the text names:** the applicant or recipient, the department, the county department and county director.
- **Judgments left to others answered conditionally:** good cause, the county director's express permission (s 43-5-1170(4), (8)), the department's finding of rape or incest (s 43-5-1175), verification of pregnancy or incapacity are asked as facts.
- **Definitions worked out from facts** where the chapter gives them ("living with", s 43-5-125, in the input's wording; "protective payments", s 43-5-65(b)); "eligible child" is borrowed (Title IV-A) and asked as age, living-with and student facts (finding 6).
- **One case:** one family (benefit group).
- **Machinery out:** the welfare policy statements, agency goals, reports and coordination duties in ss 43-5-1105, 43-5-1115, 43-5-1130 to 43-5-1165, 43-5-1225 to 43-5-1285.

## Scope

**In:** ss 43-5-30(c)(2), 43-5-45, 43-5-65(a), (c), (f), 43-5-70, 43-5-95, 43-5-125 (input wording), 43-5-140(c), (d), 43-5-148 (start date), 43-5-150 (60 days), 43-5-1110(1), 43-5-1120(B) (job search condition), 43-5-1125, 43-5-1170, 43-5-1175, 43-5-1180, 43-5-1190, 43-5-1200, 43-5-1205, 43-5-1210, 43-5-1215, 43-5-1220(A).

**Out:** the amount of the grant (need and payment standards, ADMIN-POLICY, not deposited); the proration formula of s 43-5-148 (finding 4); general assistance (ss 43-5-310 to 43-5-350) and the older AFDC articles (ss 43-5-400 to 43-5-470); child support enforcement and the new hire directory (ss 43-5-220 to 43-5-245, 43-5-580 to 43-5-630); the SNAP fraud article (ss 43-5-910 to 43-5-970); family skills training (s 43-5-1185) beyond its being a condition the department decides on.

## Regulative rules

Five `DEONTIC` rules, counted in days: the recipient's duty to report a change within 10 days (ss 43-5-65(f), 43-5-140(c)); the 30-day conciliation period after a sanction (s 43-5-1125(A)(1)); the permission to appeal a sanction within it; the permission to request a review within 60 days of notice (s 43-5-150); the department's duty to act within 10 days of receiving information (s 43-5-140(d)). The matching date questions are exported.

## What the chapter turns out to say

1. **The chapter sets no payment or need standard.** Section 43-5-65(a) speaks of "the amount of aid", s 43-5-30(c)(2) of "the amount payable to a family of the same composition with no other income", but no section gives a figure. The grant amount is ADMIN-POLICY. The eligibility answer therefore says the family "meets the conditions the chapter states" and that neediness and amount depend on the department's standards. Asserted.
2. **Much of the 1995 Act is written as a duty to seek a federal waiver.** Sections 43-5-1170 (time limits), 43-5-1205 (interest and dividends) and 43-5-1210 (minor's earnings) say the department "shall apply to the federal government for a waiver"; their HISTORY lines say they take effect ninety days after the waiver is approved "or ninety days after federal law permits implementation". The encoding treats them as in effect. A reader should confirm with the department.
3. **The asset limit's vehicle exemption is for families "in work or training".** Section 43-5-1200 exempts "one licensed vehicle per licensed driver ... for Family Independence participants in work or training"; read literally, a family not in work or training counts every vehicle. The encoding exempts the most valuable vehicles first. Exactly $2,500 is within the limit. Asserted.
4. **Section 43-5-148's proration has no workable formula.** "Payments for partial months must be prorated by the ratio of the days in the month to the date of application." A ratio of a number of days to a date has no arithmetic meaning; the likely intent (days from application to month end, over days in the month) is not what it says. Only the start date is encoded.
5. **"Asset" is undefined.** What counts toward $2,500 is the department's; the asset totals are inputs.
6. **"Eligible child" is undefined in the chapter.** Section 43-5-95 adds the 18-year-old full-time secondary or vocational student; the under-18 child living with the caretaker is taken as the core case. Asserted (an 18-year-old non-student gives "no eligible child"; a student is covered).
7. **The time-limit count.** "No more than twenty-four months out of one hundred and twenty months and no more than sixty months in a lifetime": a family with 24 months already in the window cannot have a 25th. The training exception runs to the 30th month and further only with "the express permission of the county director"; the full-compliance exception adds "up to an additional twelve months", then only with the county director's permission; the minor-parent exception runs "up to twenty-four months after the minor parent attains the age of eighteen or completes high school". Asserted.
8. **The family cap counts from when the family "begins to receive AFDC".** A child born "ten or more months after" gets no increase; a child born nine months after does. The encoding counts calendar months from the first day of receipt; a child born exactly ten months on is capped. Asserted.
9. **Child support non-cooperation does not end the child's aid.** Under s 43-5-65(a)(2), where the relative fails to assign support rights or cooperate, "aid for which the child is eligible must be provided in the form of protective payments". The encoding returns that answer rather than ineligibility. Asserted.
10. **Two ten-day reporting rules agree.** Section 43-5-65(f) ("within ten calendar days of the day on which the change becomes known") and s 43-5-140(c) ("within ten days of the date upon which the applicant or recipient became aware") say the same; the failure is "wilful withholding" and lets the department recover an overpayment. Asserted (deadline and trace).

## Before relying on it

- Deposit the DSS regulations (S.C. Code Regs. ch. 114) and, if deposited text allows, the Family Independence payment and need standards; then encode the income test and the grant.
- Confirm with DSS that the waiver-conditioned sections are in force as written.
- An independent test pass, and a check of the eligibility order (which failure is reported first when several apply).
