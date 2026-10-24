# A.R.S. Title 46, Chapter 2, Article 5 (TANF cash assistance) — baseline encoding

## Method

**Baseline.** Written straight from the deposited text, from the seat of the applicant (the parent or nonparent relative applying for a dependent child), with the design defaults ruled on 2026-10-18.
The core rules use the statute's own actors and terms; the applicant's questions (`@export`, `@desc`, under `§ Questions for the applicant`) are derived from them.
Where the text states duties (cooperate on child support, support a good cause claim within 20 days, school attendance, immunization, the department's three working days for diversion), they are regulative rules with the party as a parameter.
Checked with the stable `l4` of VS Code extension 1.6.98, `JL4_LIBRARY_PATH` unset. No pipeline, no coverage table, no independent test pass, no human gate.
**Not advice.**

Part of the Arizona "tax and benefits" sample, with the income tax at `../../../arizona-revised-statutes-title-43-taxation-of-income/encodings/baseline-2026-10/`.

## Edition

The Legislature's online Arizona Revised Statutes, "updated to include the revised sections from the 57th Legislature, 2nd Regular Session", unofficial, sections fetched 2026-10-19, deposited at `../../registers/source-bundle/az-ars-46-ch2-art5-tanf-sel-2026.txt`: ss 46-101, 46-207, 46-207.01, 46-292, 46-294, 46-296, 46-298, 46-300 only.

**Inputs, not deposited:** the department's monthly cash assistance amount (set by DES rule: ADMIN-POLICY); the HHS federal poverty guidelines (s 46-101(12)) and the 1992 federal poverty level; whether DES has found hardship; whether an employable adult refused work (the employability determination is the department's). The cases use made-up poverty levels and grants and say so.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `az-cash-assistance.l4` | `az-cash-assistance-cases.l4` | 38 written, 38 satisfied |

`l4 run` on both files: 0 errors, 0 warnings (2026-10-24). Three `#TRACE`s with `-- expect:` comments matched (the department halving the grant after non-cooperation; a good cause claim unsupported after 20 days; diversion benefits late).

## Seat

**The applicant**: the parent or nonparent relative who applies for cash assistance for a dependent child, and then the recipient. Questions: "Do we meet the conditions?", "How much of my pay is counted?", "How much childcare is disregarded?", "As a grandparent asking only for the child, is our income low enough?", "What is the least we must get?", "How much is a diversion payment?", "What do we get in a month we are sanctioned?".

The 2026-10-18 defaults:

- **The Act alone:** Article 5 and the sections of Article 1 it relies on. DES rules are not deposited; their numbers are inputs.
- **The actors the text names:** the applicant or recipient, the head of household, the department.
- **Judgments left to the department** are asked as facts: employability and refusal of work, intent to evade by a transfer, hardship, good cause, the minor-parent exceptions.
- **Definitions:** "dependent child", "needy family", "child only case" are glossed in the `@desc`s and asked as facts; "qualified alien" (PRWORA s 431) is a borrowed term, asked as a status.
- **One case:** one assistance unit.
- **Machinery out:** reports to the Joint Legislative Budget Committee (ss 46-207(B), 46-298(J)), rule-making powers.

## Scope

**In:** s 46-292(A), (B)(1)-(3), (C), (D), (E), (G), (P)(1)-(2), (S), (T); s 46-294(A), (C), (E), (G); s 46-296(A), (B); s 46-298(C), (D); s 46-300(D); s 46-207.01 with s 46-207(D).

**Out:** s 46-292(H)-(L) (no extra cash for a child born while on assistance, and its exceptions); s 46-292(Q), (R) (whose income counts in a child only case: noted, not computed); s 46-292(O) (no denial because the principal earner works 100 hours a month: true of every case here, since hours are not asked); s 46-294(D) (months not counted: the person states months already net of them), (F) (the 2016 cut-off); s 46-299 (work activities, not deposited); s 46-300(A), (B) (what counts as noncompliance: asked as the instance number).

## What the statute turns out to say

1. **The statute does not set the monthly amount.** Section 46-207(A) excludes TANF from the general need test, and the only amount in the text is a floor: cash plus nonexempt income "shall not be less than thirty-six per cent of the 1992 federal poverty level" (s 46-207.01), with the poverty level cut by 37% for a family with no shelter costs (s 46-207(D)). The floor is pegged to 1992 and never updated. Asserted.
2. **Arizona's time limit is twelve months**, counted from 1 October 2002, consecutive or not (s 46-294(A), (B)), with one further twelve months for a family whose work-program adult is in full compliance and whose school-age children attend at least 90% (G), and the federal-style sixty-month lifetime limit across states (E). Asserted.
3. **Section 46-292(B)(1) lists no category for a qualified alien who entered after 21 August 1996 and is in no exception group, even after five years.** Subsection (C) bars such aliens "for a period of five years beginning on their date of entry", which implies eligibility afterwards, but (B)(1) admits only pre-1996 entrants, PRWORA s 412 exception groups and the Attorney General's s 501 category. The encoding follows (B)(1): not eligible. Asserted. DES practice may differ.
4. **Each employed person keeps $90 and 30% of the rest of their earnings** (s 46-292(P)(1)); dependent care up to $200 a month for a child under two and $175 for each other dependent is also disregarded, but only where it is needed for work or job-preparatory training. Asserted.
5. **A relative asking only for the child must have family income at most 130% of the poverty guidelines** (s 46-292(P)(2)); then only the child's income counts towards the amount ((Q)). Asserted for the test.
6. **Sanctions are graduated: half the grant for one month for the first instance, then no grant for at least a month or until compliance**, counting months that are not consecutive (s 46-300(C), (D)). Asserted.
7. **Diversion pays three months' cash at once, within three working days of a completed application** (s 46-298(C), (D)); reapplying within three months prorates it against later cash assistance ((H), not computed). Asserted and traced.
8. **A good cause claim against child support cooperation must be supported within 20 days** (s 46-292(G)). The duty to cooperate itself has no time in the statute; the case uses an assumed 30 days. Traced.
9. **An unmarried parent under 18 cannot head an assistance unit** unless one of four exceptions applies (s 46-296). Asserted.

## Before relying on it

- Deposit DES's rules on the cash assistance amount (the payment standard by family size), resources and the assistance unit, and s 46-299 (work activities).
- Settle finding 3 against DES practice.
- An independent test pass.
