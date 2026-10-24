# Virginia TANF (Va. Code ss 63.2-600 to 63.2-621, with 22VAC40-295-10 and -50) — baseline encoding

## Method

**Baseline.** Written straight from the deposited text, from the seat of the caretaker applying for or receiving TANF, with the design defaults ruled on 2026-10-18.
No REFUSE. Checked with the stable `l4` of VS Code extension 1.6.98, `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate. **Not for public use as advice.**
There was no earlier encoding to keep.

## Edition

- Code of Virginia Title 63.2 chapter 6, as online after the 2026 Session, retrieved 2026-10-19 (UTC), deposited at `../../registers/source-bundle/title-63-2-chapter-6-temporary-assistance-for-needy-families.txt`.
- **Brought in** (the instrument that sets the Act's numbers, default 2026-10-18): 22VAC40-295-10 (definitions) and 22VAC40-295-50 (income eligibility) as shown online on 10/19/2026, deposited in the sibling subject `../../../virginia-administrative-code-22vac40-295-tanf-income-and-payment/registers/source-bundle/va-22vac40-295-10-50-tanf.txt`. Its `SOURCE-LICENSE.md` is appended to the copy in this folder.

**Amounts not deposited (inputs).** The standard of assistance by family size (set by the State Board; 22VAC40-295-10) and the SNAP standard deduction the earned income disregard uses (22VAC40-295-50 C 1; the USDA tables are deposited under `subjects/us/food-and-nutrition-act-of-2008/` but cannot be imported). The figures in the cases are hypothetical.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `va-tanf.l4` | `va-tanf-cases.l4` | 36 written, 36 satisfied |

Plus five `#TRACE`s of the regulative rules with `-- expect:` comments (three FULFILLED, two breaches by the local department, read in the output). `l4 run` on both files: 0 errors, 0 warnings (2026-10-24). Every expected value was worked by hand from the text.

## Seat

**The caretaker**: the parent or other relative with whom the child lives and to whom the payment is made (22VAC40-295-10 "caretaker"). Questions: "Does my child meet the conditions?", "Have I done what an applicant must?", "Are we income eligible, and how much is the payment?", "What is diversionary assistance worth, and what do I give up?", "Am I exempt from VIEW?", "Can we still get TANF under the 24 months?", "Does TANF continue if I appeal?".
Duties of the local department are encoded as what the caretaker must be given: notice 60 days before termination (s 63.2-612) and continued payment pending a timely appeal (s 63.2-618).

Defaults (2026-10-18):
- **The Act plus the instrument that sets its numbers**: 22VAC40-295-10 and -50.
- **Actors**: the caretaker and the local department.
- **Judgments left to others**: hardship exceptions (s 63.2-613, Board regulations not deposited), medical certification, the department's identification of immunization barriers, good cause for not identifying a parent: asked as facts.
- **Definitions**: the eligible child, net income and the VIEW exemptions are worked out from facts.
- **One case**: one assistance unit in one month.
- **Machinery out**: the TANF Fund and funding pool, the Department's records and reports.

## Federal frame

TANF is run "in compliance with Titles IV-A and IV-F of the Social Security Act" (s 63.2-600). Title IV-A (42 U.S.C. 601-619) is deposited in `subjects/us/social-security-act/`; its 60-month limit (s 608(a)(7)) sits above Virginia's shorter 24-month VIEW limit. Cross-folder IMPORT is not possible.

## Scope

**In:** s 63.2-602 A, B; s 63.2-603; s 63.2-609; s 63.2-612 (with the 60-day notice as a rule); s 63.2-613 (as a fact); s 63.2-617 A; s 63.2-618 (as a rule); 22VAC40-295-50 A, B 10, B 15, B 23, C, D, I.

**Out:** ss 63.2-600, 601, 601.1, 601.2, 608, 610, 611, 615, 616, 621; s 63.2-605; s 63.2-606 (except through the child's attendance); s 63.2-607; s 63.2-614 A (step-parent deeming) and C 1 (the VIEW earned-income cap at a percentage of poverty set by the Commissioner); s 63.2-617 B; 22VAC40-295-50 E-H and the other B disregards (the person leaves them out).

## What the law turns out to say

1. **The payment is the standard of assistance less net income, and eligibility needs net income "less than" the standard** (22VAC40-295-50 A, I). Net income equal to the standard is not eligible. Asserted.
2. **The earned income disregard is borrowed from SNAP.** The SNAP standard deduction, then 20 percent of the remainder (22VAC40-295-50 C), for initial eligibility and for non-VIEW participants. Child or spousal support has a $50 disregard (B 23). For VIEW participants, s 63.2-614 C 1 instead lets TANF continue up to a poverty-level percentage set by the Commissioner; that cap is not encoded. Asserted (the C disregard).
3. **The 24-month limit is for VIEW participants only, and it is followed by 24 months off.** "Unless otherwise exempt, VIEW participants and their families may receive TANF ... for a maximum of 24 months only", and again "after a subsequent period of 24 months" (s 63.2-612). A relative with whom a child is placed after a child protective services report need not wait. Asserted. The federal 60-month lifetime limit also applies but is not in the state text.
4. **Diversionary assistance is "up to 120 days or $1,500, whichever is greater"** and waives eligibility for 1.33 times the days granted (s 63.2-617 A). The 120 days are taken as four monthly payments. Asserted ($300 a month: $1,500; $450 a month: $1,800; 120 days waives 159.6 days).
5. **Immunizations: a reduction, not a denial, and not before barriers are removed.** $50 for the first child and $25 for each other child without verification, and "no sanction may be imposed until the reason ... has been identified and any barriers ... have been removed" (s 63.2-603). Asserted.
6. **An exempt infant carer has at most 12 months, consecutive or not** (s 63.2-609(8)). Asserted.
7. **A hearing request before the effective date keeps payments going** (s 63.2-618). Written with `DO … LEST FULFILLED`, as a permission the caretaker may leave unused. Traced.

## Before relying on it

- Deposit the State Board's standards of assistance and the TANF manual's other rules if a source with acceptable terms exists.
- Encode s 63.2-614 (deeming, the VIEW cap) and s 63.2-613 hardship regulations.
- An independent test pass.
