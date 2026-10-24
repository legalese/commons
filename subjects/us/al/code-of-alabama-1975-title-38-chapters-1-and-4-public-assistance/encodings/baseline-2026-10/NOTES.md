# Alabama Family Assistance (TANF cash assistance) — baseline encoding

## Method

**Baseline.** Written straight from the deposited text, from the seat of the applicant (the parent or caretaker relative applying for a needy child), with the design defaults ruled on 2026-10-18.
The core rules use the texts' own actors and terms; the applicant's questions (`@export`, `@desc`, under `§ Questions for the applicant`) are derived from them.
Duties and rights (reporting new income, the county director's written notice, the fair hearing) are regulative rules with the party as a parameter.
Checked with the stable `l4` of VS Code extension 1.6.98, `JL4_LIBRARY_PATH` unset. No pipeline, no coverage table, no independent test pass, no human gate.
**Not advice.**

Part of the Alabama "tax and benefits" sample, with the income tax (`../../../code-of-alabama-1975-title-40-chapter-18-income-taxes/encodings/baseline-2026-10/`) and unemployment benefits (`../../../code-of-alabama-1975-title-25-chapter-4-unemployment/encodings/baseline-2026-10/`).

## Edition

- Code of Alabama 1975, Title 38, Chapters 1, 4 and 11A, as ALISON served them on 2026-10-20 (no "current through" date): `../../registers/source-bundle/ala-code-38-1.txt`, `ala-code-38-4.txt`, `ala-code-38-11a.txt`.
- Alabama Administrative Code, Department of Human Resources rules 660-2-2-.10, -.27, -.31 and -.32, as shown on 2026-10-19, deposited in a sibling subject: `../../../alabama-administrative-code-660-2-2-and-660-2-4-family-assistance-payment-and-state-supplementation/registers/source-bundle/ala-admin-code-660-2-2-and-660-2-4.txt`. That subject's licence record is copied here as `SOURCE-LICENSE-admin-code-660.md`.

**The payment standard is an input (ADMIN-POLICY).** Rule 660-2-2-.31 says the Department "has developed a payment standard which varies by family size"; the attachment that held the table was repealed in 2018, and no current table is deposited anywhere. The family's rounded total net countable income is also an input: the income disregards are DHR policy, not deposited. The cases use made-up standards and say so.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `al-family-assistance.l4` | `al-family-assistance-cases.l4` | 27 written, 27 satisfied |

`l4 run` on both files: 0 errors, 0 warnings (2026-10-24). One `#TRACE` (an unreported change: breach) with an `-- expect:` comment that matched. Every expected value was worked out by hand.

## Seat

**The applicant**: the parent or caretaker relative applying for a needy child, and later the recipient. Questions: "Is my family eligible?", "How much a month?", "How much for the month I applied?", "Can I appeal?".

The 2026-10-18 defaults:

- **The Act alone, with the instruments that set its numbers:** Title 38 with DHR's grant rules. The rule that would set the number (the payment standard table) is no longer rule text, so the number is an input.
- **The actors the texts name:** the applicant, the recipient, the county director, the county and state departments.
- **Judgments left to others** are asked as facts: dependent child (a federal term, s 38-4-1(d)), good cause for quitting, satisfactory probation, the hardship exemption.
- **One case:** one assistance group, one month.
- **Machinery out:** subpoenas (s 38-4-6), county boards (s 38-4-10), trust funds, the Confederate pension provisions.

**Departure:** the federal 60-month limit (42 U.S.C. 608(a)(7), deposited in `subjects/us/social-security-act/registers/source-bundle/usc42-ch7-schIV-ptA.txt`) is applied here as a fact-driven condition, because s 38-4-4(b) makes Alabama's TANF eligibility "conform with federal eligibility requirement standards as provided for in Title IV, Part A". The stable `l4` cannot IMPORT across folders; the condition is one line, written from the federal text.

## Scope

**In:** s 38-4-1(a) (the institution bar), (d); s 38-4-2(a) (notice); s 38-4-4(a), (b) (as the 60-month condition); s 38-4-5; s 38-11A-2(b), (c); s 38-1-8; rr 660-2-2-.10, -.27, -.31, -.32.

**Out:** the other categories of s 38-4-1 (blind, old age, disabled); State Supplementation (660-2-4); SNAP; ss 38-4-14 and 38-4-15 (what benefits may be spent on); sanctions (rr 660-2-2-.18, -.23, not deposited); recoupment of overpayments; the TANF drug screening programme (s 38-1-7, terminated 30 September 2017).

## What the texts turn out to say

1. **No statute or rule in force gives the Family Assistance amount.** The grant is the payment standard less the family's rounded net income (rr 660-2-2-.10, -.32), and the standard is set by DHR "based on the amount of funds available" (r -.31; s 38-4-2(b): "subject to the funds available"). A person cannot get a dollar figure from the deposited law without DHR's current table.
2. **Applicants must first apply for three jobs.** "As a condition of eligibility ... an applicant shall have applied for at least three positions of unsubsidized employment prior to completing the application process" (s 38-11A-2(b)). Asserted.
3. **The need test and the $10 minimum work together.** Rule 660-2-2-.27 bars a family whose net income equals or exceeds the standard "subject to the minimum payment regulations of Rule No. 660-2-2-.10", and r -.10 says "The minimum grant is $10". Read together: a deficit under $10 means no grant and, by -.27, no eligibility. Asserted ($5: not eligible; $10: eligible, $10 paid).
4. **The first month's prorated payment is not held to the $10 minimum.** Rule 660-2-2-.10 applies the minimum "except when the initial payment is authorized for the month of the application and is prorated". Proration is by days from the application date to the month's end over 30, so applying on the 1st of a 31-day month pays more than a full month's grant. Asserted (1 December: 31/30 of the grant; 28 February: $5).
5. **A drug-felony conviction bars TANF only until the sentence is completed, or while probation is not being served satisfactorily** (s 38-1-8, using 21 U.S.C. 862a(d)). Asserted.
6. **The duty to report a change is "immediately"**, with no number of days (s 38-4-4(a)). The encoding allows one day. The consequence the statute gives is that the county department "shall, after investigation, continue, reduce or cancel" the grant; it states no penalty. Traced.
7. **The right to a fair hearing has no time limit in the statute** (s 38-4-5); any limit is in DHR's rules, which are not deposited. The rule is a permission with no `WITHIN`. Asserted.
8. **Assistance is exempt from state and local tax and from garnishment, and cannot be assigned** (s 38-4-8). Not a question here; it settles that Family Assistance is not Alabama taxable income.

## Before relying on it

- Deposit DHR's current Family Assistance payment standard table, and the income disregard and sanction rules.
- An independent test pass.
