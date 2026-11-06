# Minimum Conditions of Employment Act 1993 (WA) — baseline encoding

**Method: baseline.** Written straight from the deposited text with the `writing-l4-rules`
skill, from the seat of the individual to whom the law is applied, with the design
defaults ruled on 2026-10-18. No REFUSE. No pipeline, no coverage table, no independent
test pass, no human gate. Not for public use as advice.

There was no first-pass (`naive-2026-10`) encoding of this Act to replace.

**Edition:** the consolidated text at legislation.wa.gov.au (law_a516, document
mrdoc_48248, retrieved 7 September 2026; amendments shown up to No. 43 of 2024), as
deposited at `../../registers/source-bundle/mrdoc_48248.txt`. Also read, not encoded:
Industrial Relations Act 1979 (WA) ss 7(1), 7A, 7B, 50A (deposited at
`subjects/au/wa/industrial-relations-act-1979`) and Fair Work Act 2009 (Cth) s 26
(deposited at `subjects/au/fair-work-act-2009`). No regulations are used. The minimum
weekly rates come from the annual State Wage order under the IR Act s 50A, which is not
deposited, so they are inputs; the cases use a hypothetical $987.65 a week.

**Checks:** one module (`mce-employee.l4`), one case file (`mce-cases-employee.l4`),
43 assertions satisfied, 0 errors, 0 warnings, with the stable `l4` of VS Code extension
1.6.98.

## Seat

**The employee**, and in practice a *State system* employee: someone whose employer is
not a national system employer under the Fair Work Act. The Act is written to the
employment relationship and its conditions are the employee's entitlements, so the
employee's seat is the natural one. The first question from that seat is whether the Act
reaches me at all, and for most private-sector workers in WA the answer is no.

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers.** Followed. The numbers come
  from the State Wage order, which is not deposited, so the rates are inputs. The Fair Work
  Act s 26 exclusion is not part of this Act. It is asked as a fact ("my employer is a
  national system employer"), with the reading set out in finding 1.
- **The actors the text names.** Followed: the employee and the employer. The Commission
  appears only as the source of the State Wage rate and the casual loading order.
- **Judgments handed to someone else are asked conditionally.** Followed: whether extra
  hours are reasonable (s 9B), whether a public-holiday request or refusal is reasonable
  (s 30(4)), and whether the relationship is employment in substance (IR Act s 7A).
- **The Act's own definitions worked out, borrowed terms asked.** Followed. "Member of the
  employee's family or household" (s 3) and "redundant" (s 40) are worked out from facts.
  "Employee", "casual employee" and "apprentice" are borrowed from the IR Act and asked.
- **One case is the text's natural unit.** One employment.
- **The Act's own terms, with glosses.** Followed, in the `@desc` of each input.
- **Operative sections in; machinery out.** Followed. Enforcement (s 7), regulations (s 47)
  and the transitional Parts 8 and 9 are out.

## The lives

| Event | What it asks of this Act | Decision |
|---|---|---|
| c040 Chloe joins the Ironbark Logistics graduate program, $70,000 a year | Does this Act give me anything? | `Am I an employee for this Act` (yes); `Does this Act give me its minimum conditions` (no: Ironbark Logistics Pty Ltd is a national system employer) |

The plan names no other event. The rest of the encoding covers what a State system
employee meets: a public servant, a police officer (s 6A), or someone working for an
employer that is not a national system employer.

## Why this scope

The task asked for a small baseline (25 to 45 assertions) on two things: whether the Act
applies, and the minimum conditions it gives. Pay, hours, the four kinds of leave, public
holidays and the redundancy rights are in. Left out: the disability and Supported Wage
rules (ss 15–17), how pay must be paid (Part 3A), the rate of pay for leave (ss 18–18B),
compensated employees, substituted public holidays and leave over a public holiday
(ss 32, 33), proof and confidentiality (ss 22A, 28, 39D, 39E), and flexible working
requests (Part 4A).

## What the Act turns out to say

1. **The Act never says it stops at the national system.** s 5(1) binds "all employees and
   employers". The definitions of employee and employer are borrowed from the IR Act s 7(1),
   and they do not mention national system employers either. The Act's only nods to the
   national system are the s 3 definition of "paid family and domestic violence leave"
   ("a non-national system employee") and the Notes to Part 4 and Division 7. The exclusion
   comes from the Fair Work Act s 26(1), which applies "to the exclusion of all State or
   Territory industrial laws". s 26(3)(c) names the WA IR Act as a general State industrial
   law. This Act is not named. It is caught, on my reading, by s 26(2)(b)(ii) and (c): an
   Act applying to employment generally that provides for terms and conditions of
   employment and deals with leave. That is an inference, and Fair Work Act s 27 (laws not
   excluded) was not read in full. Chloe at Ironbark gets nothing from this Act. Asserted.
2. **The Act has no notice of termination and no redundancy pay.** Part 5 gives a
   non-casual, non-apprentice employee only two things: a right to be told of the
   redundancy and to discuss it (s 41), and up to 8 hours of paid leave for job interviews
   (s 43). Partly asserted (ss 41, 43).
3. **For a full-time 38-hour employee, the leave matches the Fair Work Act baseline.**
   Annual leave is four weeks of ordinary hours, capped at 152 hours (s 23). Personal leave
   is two weeks of ordinary hours, capped at 76 hours (s 20). These match the Fair Work Act
   ss 87 and 96 (4 weeks; 10 days) for a 38-hour week. Unlike the Fair Work Act, the caps
   mean someone working more than 38 ordinary hours earns no extra leave. Asserted.
4. **Junior rates are a statutory table.** Under 21, a non-apprentice gets 90% (age 20)
   down to 40% (under 16) of the adult State Wage rate, rounded to the nearest 10 cents
   (s 13). The hourly minimum is the weekly rate divided by 38 (s 10). A casual adds 25%,
   or a higher loading set by order (s 11). Asserted.
5. **Half of a year's annual leave can be cashed out, never more.** The agreement must come
   after the year of service is complete. It must be in writing and signed, pay at least
   what the leave would have paid, and keep all agreements for that year within 50%. It is
   void if the job offer depended on it (s 8(2C)). Asserted.
6. **The maximum is 38 hours a week unless an instrument sets ordinary hours.** Beyond that,
   only reasonable additional hours may be asked for, and authorised leave counts as hours
   worked (s 9A). Asserted.
7. **Dismissal for misconduct costs leave, but not all of it.** The part-year's untaken
   annual leave is lost if the employee walks out unlawfully or is dismissed for fault
   (s 26(2)). Dismissal for misconduct also loses leave from years completed after the
   misconduct (s 26(3)). I read misconduct as a kind of fault, so the part-year is lost
   too. Asserted.
8. **Bereavement leave reaches the partner's family and the household.** Two days, not
   necessarily consecutive. The family is counted on both the employee's and the
   partner's side, adult children included, plus anyone who lived in the household (s 3,
   s 27). Casuals are not excluded. Asserted.
9. **Family and domestic violence leave here is unpaid: 5 days in each 12-month period**,
   available in full to casuals (ss 39B, 39C). Paid leave of that kind comes to State
   system employees from the Fair Work Act Part 6-3 Division 2A, which the Note to
   Division 7 points to. Asserted (unpaid days).
10. **Public holidays.** An employee may refuse to work if the request is unreasonable or
    the refusal is reasonable (s 30(3)). A non-casual who would ordinarily work that day
    and is not on unpaid leave is paid for it (s 31). Asserted.

## What would need doing before this is worth anything

- Deposit the current State Wage order (IR Act s 50A), so the rates are figures rather
  than inputs.
- Read the Fair Work Act ss 14 and 27, and the IR Act s 80A declarations, to settle who is
  in the State system. The s 26 reading in finding 1 is unchecked.
- Encode Part 4A (flexible working), ss 15–17 (Supported Wage) and ss 18–18B (leave pay
  rates).
- Schedule 1 (public holidays) was not read; whether a day is a public holiday is not
  encoded.
- No Commission decisions or case law were searched.

## Q&A layer (seat and situations as parameters)

Added 6 November 2026 as a layer: `mce-qa.l4` (IMPORTs `prelude` and `mce-employee`) and `mce-qa-cases.l4` (IMPORTs those and
`mce-qa`). The baseline's files are unchanged. The design is the Graffiti Vandalism Act 2016 encoding's (its NOTES.md D2, D4,
D8 and D8.1-D8.15): every exported question takes `my role` IS A Role first (`@desc Which of these describes you`), and answers
`does not arise for you` for a role it is not about without reading any other input; a question that arises only in a
situation takes that situation's fact straight after the role and answers `does not arise for you` when it does not hold,
reading nothing else. No exported question takes a DEONTIC or EVENT input. One deployment serves both roles.

### Roles, and why

| Role | Why | Questions |
|---|---|---|
| `I am an employee` | the baseline's seat | 22 |
| `I am an employer` | new: s 5(1) binds "all employees and employers", and each minimum condition is the employer's duty | 15 |

37 questions in all, none shared: each question is phrased from one side. The Western Australian Industrial Relations
Commission is not a seat; the State Wage order and any casual loading order are figures the person supplies, as in the
baseline.

### Situation inputs

| Name | Type | Gives `does not arise for you` | Questions |
|---|---|---|---|
| `the employer is a national system employer` | BOOLEAN | TRUE | 2nd input of all 34 entitlement questions of both roles (every question but `Am I an employee for the purposes of this Act`, `Does this Act give me its minimum conditions of employment` and `Does this Act bind me in employing this person`; the last two take it as an ordinary input and answer no). The full list is in `encoding.json`. |
| `the employment has ended` | BOOLEAN | FALSE | 3rd input, after the national system input, of `How many hours of untaken annual leave must I be paid out` and `How many hours of untaken annual leave must I pay out to this employee` (s 26: "when the employee's employment ends") |

The national system input is the graffiti lesson applied: the Act gives nothing at all where the Fair Work Act 2009 (Cth)
s 26 excludes it (baseline finding 1), so for Chloe at Ironbark (c040) the form asks one fact and drops every entitlement
question.

### Decisions

- **Input names are neutral between the two roles** ("the employee is casual", "the hours ordinarily worked each week"),
  where the baseline wrote them from the employee ("I am casual"). The facts are the same whoever answers, and one name
  with one `@desc` keeps the questions of both roles consistent. Inputs only the employee can state ("I cannot work because
  of illness, injury or a family emergency") keep the first person.
- **The baseline's MyWork record is built from plain answers**, with `my employer is a national system employer` taken from
  the situation input; the employer's s 5 question passes `I am a police officer` FALSE (s 6A treats a police officer as an
  employee; whether the Commissioner is then an "employer" is not asked).
- **s 24 for the employer** is the negation of the employee's right: the employer "must not refuse" exactly when the employee
  can insist, so `May I refuse to let this employee take annual leave when they want` is `yes if` NOT the baseline's
  `Can I insist on my annual leave`.
- **The redundancy and casual exclusions are not situations.** Part 5 excludes casuals and apprentices (s 40(1)), and the
  leave sections exclude casuals, but the baseline answers no or 0 for them, which tells the person where they stand
  (graffiti D8.1's reasoning). They stay ordinary inputs.
- **The two "does this Act apply" questions take no situation input**: they arise for everyone and answer the threshold.

### Not covered for the employer

The employer's evidence requests (ss 22A, 28, 39D) and confidentiality (s 39E); how pay must be paid (Part 3A); leave pay
rates (ss 18-18B); the s 41 timing ("as soon as reasonably practicable") beyond whether the duty arises; flexible working
requests (Part 4A); enforcement and penalties (s 7 and the IR Act s 83), which the baseline also leaves out.

### Cases

`mce-qa-cases.l4`: 184 assertions, all satisfied. 111 written by hand for the role each question is about (23 of them
assert that the employee's answer equals the baseline export's on the same facts, wrapped in the answer type; the rest give
hand-worked values, the employee's from the baseline's own cases, with the same hypothetical $987.65 State Wage rate); 37
for the other role, every other input ASSUMEd; 36 for the situation values that do not hold, the inputs after them ASSUMEd.
The last two groups were generated by a scratch script from the parameter list and the table above. Checked on stable l4
1.6.98: 0 errors and 0 warnings in all four files, 43 + 184 assertions satisfied, `l4 check mce-qa.l4` succeeds, and a
parameter script confirms `my role` first everywhere, each shared input identical in name, type and @desc, the national
system input second and read first in each role branch, the ended input third, and no DEONTIC or EVENT input. A negative
control on a scratch copy (a wrong expected value; a weekly-rate question that reads the age with the national system check;
a pay-out question that reads the hours with the ended check) failed 3 cases, as it should.
