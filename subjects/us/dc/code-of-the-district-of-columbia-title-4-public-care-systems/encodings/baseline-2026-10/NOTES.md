# D.C. Code Title 4, chapter 2: Temporary Assistance for Needy Families — baseline encoding

## Method

**Baseline.** Written straight from the deposited text, from the seat of the applicant or recipient, with the design defaults ruled on 2026-10-18.
No REFUSE: a family larger than the table answers `not covered`, asserted.
Checked with the stable `l4` of VS Code extension 1.6.98, `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

There was no earlier encoding of this chapter to keep.

## Edition

The Code of the District of Columbia "through 2026-09-26" (last codified D.C. Law 26-187), from the Council's bulk XML (github.com/DCCouncil/law-xml-codified, branch `publication/2026-05-23`, commit `9c950ac5`), deposited at `../../registers/source-bundle/dc-code-4-ch2-subch-v-xxi-public-assistance-programs-2026-10.txt` (retrieved 2026-10-19). For public reference and encoding, not model training (`ai-train=no`).

**Figures.** In the statute: the 1998 table of standards (s 4-205.52(c)), the child support disregard, the $10 floor, 60 months, and every deadline. **Not in the deposited text, and inputs here:** the work-related expense deduction, the maximum care deduction and the earned income disregard (s 4-205.11(a)(1), (2), (4A): "as the Mayor shall specify through rulemaking"; the DCMR is not deposited), and the current level of assistance after the annual inflation increases of s 4-205.52(d-1) (the 1998 figure is the default). The cases use HYPOTHETICAL deductions.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `dc-tanf.l4` | `dc-cases-tanf.l4` | 32 written, 32 satisfied |

`l4 run` on both files: 0 errors, 0 warnings (2026-10-24). Two `#TRACE`s end in a breach, each with an `-- expect:` line; both were read and match.

## Seat

**The applicant for, or recipient of, TANF:** the parent or caretaker relative. Questions: "What are the standards for my family?", "How much would we get?", "Can we keep getting federally funded TANF?", "By when must the agency act on my application?", "By when must I report my child's long absence?", "Was the notice of a cut timely?", "Will my TANF continue during a hearing?", "Until when may I ask for a hearing?".

The Mayor (the Department of Human Services) appears only as what the Mayor must or may do: decide in 45 days, give timely and adequate notice, reinstate within 96 hours, exempt from the time limit.

The 2026-10-18 defaults:

- **The Act alone**; the Mayor's rules (DCMR) that set the deductions are not deposited, so their amounts are inputs.
- **Actors:** the applicant or recipient, the parent, guardian or caretaker, the assistance unit, the Mayor.
- **Judgments handed to others, answered conditionally:** the s 4-205.11a(e) exemption for hardship or battering; good cause (s 4-205.11(a)(6), s 4-205.18(d)(1)); whether the disregards are withheld in a month (asked as a fact).
- **Definitions** worked out from facts: "gross income" and "earned income" (s 4-205.05); the gross income test; the payment; "timely" notice (s 4-205.55(a)(1)). Residence (s 4-205.03, living in the District voluntarily and not for a temporary purpose) is left to the person; s 4-205.02 forbids any durational residence requirement.
- **One case:** one assistance unit, one month.
- **Machinery out:** the TANF Universal Service Delivery Model, the reviews, the demonstration projects.

## Scope

**In:** s 4-205.05(1), (3), (4); s 4-205.10(a); s 4-205.11(a)(1) to (4A), (6), (8); s 4-205.11a(a) to (e); s 4-205.18(d)(2); s 4-205.26; s 4-205.27; s 4-205.51; s 4-205.52(a), (c), (d-1) (as an input); s 4-205.53(a); s 4-205.54(e); s 4-205.55(a), (b); ss 4-205.56(a), 4-205.57; s 4-205.59(a), (c), (d); s 4-210.09(a), (b).

**Out:** POWER, GAC, GPA, IDA and the other categories; deeming (ss 4-205.11(b), 4-205.22); the assistance unit (s 4-205.15: the size is an input); work requirements and sanctions (ss 4-205.19b to 4-205.19h); lump sums and resources; the hearing procedure beyond the 90 days and 45 days (s 4-210.09(c)); and the provisions marked "[Applicable on October 1, 2026.]" (finding 1).

## Read with

- `subjects/us/social-security-act/` (Title IV-A; s 4-205.11a follows the federal 60-month limit).
- `../../../code-of-the-district-of-columbia-title-47-taxation-licensing/encodings/baseline-2026-10/`: the DC EITC. s 4-205.05(1) leaves earned income credits out of earned income, and s 47-1806.04(f)(3)(C) says the payments are not income for public assistance.

## What the Code turns out to say

1. **Three provisions in force from 1 October 2026 have no text in the deposit.** The bulk XML prints "(a-1) [Applicable on October 1, 2026.]" and "[(g)] [Applicable on October 1, 2026.]" in s 4-205.11a (the 60-month limit), and "(c-4) [Applicable on October 1, 2026.]" in s 4-205.52 (the standards), with no words after them. Today (24 October 2026) they are in force. The encoding cannot say what they change; the time limit and the standards here may be out of date. A re-deposit from a later publication branch is needed.
2. **The table has two columns and the text uses three names.** s 4-205.52(c) heads its columns "Standard Payment Level" and "Level of Assistance" and calls both "the standards of assistance"; s 4-205.52(a) works the payment from "the current payment level"; s 4-205.10 tests income against "the standard of assistance"; (d-1) raises "the assistance levels" for inflation. This encoding reads the Standard Payment Level as the standard the tests use and the Level of Assistance as the payment level (family of 3: $712 and $379). Interpretive. Asserted.
3. **The gross income test counts earned income only, including a student child's.** s 4-205.10(a) bars a family whose "gross income ... exceeds 100% of the standard of assistance", and s 4-205.05(3) defines "gross income" as "total earned income before any deductions". Unearned income is tested only by the initial applicant's net test (s 4-205.11(a)(3)) and by the payment. A student child's earnings are disregarded in the need determination (s 4-205.11(a)(4)), which comes after the gross test, so they count in it. Asserted ($500 + $300 student: not eligible; $500 + $100: $239).
4. **From October 2025 all current child support is disregarded.** Before then the first $150 a month was (s 4-205.11(a)(8)). Asserted ($400 support: $129 in September 2025, $379 from October).
5. **The deductions that decide the amount are in the Mayor's rules.** The work expense, the care maximum (which "may vary depending upon the age of the child") and the earned income disregard (an amount "and/or a percentage") are set by rulemaking (s 4-205.11(a)(1), (2), (4A)). They are inputs. In a month where (a)(6) or s 4-205.54(e) applies, no earned income disregard is given; the encoding then counts the adults' earnings in full.
6. **The 1998 table is the base; the payment level now rises with inflation.** s 4-205.52(d-1): annual CPI-U increases from FY 2015, with set increases for FY 2017 to 2019 and none for FY 2027 to 2030. The current level is an input; the 1998 figure is the default. Asserted.
7. **The 60-month limit is on federally funded TANF.** s 4-205.11a(a) bars "Federally-funded TANF benefits" after 60 months; the Mayor may exempt for hardship or battering, up to 20% of cases (e), (f). Whether locally funded aid can continue is not said in the deposited text (and see finding 1). Asserted.
8. **Notice must be postmarked 15 days ahead; a hearing request before the effective date keeps the benefits.** ss 4-205.55(a)(1), 4-205.59(a). Where the notice was not timely and the hearing is asked for within 10 days of the postmark, assistance must be reinstated within 96 hours (s 4-205.59(c)). A later request within 90 days of the postmark is heard, without continued benefits (s 4-205.59(d), s 4-210.09). Asserted.
9. **The 45 days to decide do not end the application.** s 4-205.26 gives 45 days from receipt to the first payment or a notice of ineligibility, unless an unusual circumstance beyond the Mayor's control intervenes; s 4-205.27 says the Mayor shall not stop considering the application for missing it. The rule is traced to its breach, whose message says so.
10. **A child's long absence must be reported within 5 days.** s 4-205.18(d)(2): a parent who does not notify within the 5-day period beginning on the day it becomes clear the child will be away more than 90 consecutive days is ineligible. Asserted and traced. Sanctions are capped at 6% of the benefit (s 4-205.18(e)).

## Before relying on it

- Re-deposit Title 4 from a publication branch that carries the 1 October 2026 provisions (finding 1).
- Deposit the DCMR TANF rules (the deductions, the disregard, the current payment levels).
- Encode deeming, the assistance unit and the work rules.
- An independent test pass.
