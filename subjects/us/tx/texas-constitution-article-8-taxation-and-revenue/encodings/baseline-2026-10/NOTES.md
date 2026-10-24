# Texas Constitution art. VIII, the personal taxes the State may not impose — baseline encoding

## Method

**Baseline.** Written straight from the deposited text, from the seat of the individual, with the design defaults ruled on 2026-10-18. No REFUSE. Checked with the stable `l4` of VS Code extension 1.6.98, `JL4_LIBRARY_PATH` unset. No pipeline, no coverage table, no independent test pass, no human gate. **Not for public use as advice.**

This is the "personal income tax" half of the Texas tax and benefits sample. Texas has no individual income tax, and the Constitution forbids one; this short encoding says so from the deposited text, together with the newer bars on capital gains, wealth and death taxes. The benefits half is the TANF encoding (`../../../human-resources-code-chapter-31-financial-assistance-and/encodings/baseline-2026-10/`) and the unemployment benefits encoding (`../../../labor-code-title-4-subtitle-a-texas-unemployment-compensation/encodings/baseline-2026-10/`).

## Edition

Tex. Const. art. VIII as deposited at `../../registers/source-bundle/tex-const-art8.txt` (Texas Legislative Council file dated 2026-07-31, amendments credited to 2025; retrieved 2026-10-19 UTC). Sections 24-a (added Nov. 5, 2019), 24-b (added Nov. 4, 2025), 25 (added Nov. 7, 2023) and 26 (added Nov. 4, 2025).

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `tx-const-personal-taxes.l4` | `tx-const-personal-taxes-cases.l4` | 14 written, 14 satisfied |

`l4 run` on both files: 0 errors, 0 warnings (2026-10-24). Five `#TRACE`s: four show a breach by the legislature when it imposes the barred tax, one shows the s 24-a prohibition still standing after an unrelated act; each matched its `-- expect:` comment.

## Seat

**The individual** (an employee, a sole proprietor, a partner, an investor, an heir). Questions: "Can Texas tax my income?", "Must I file a Texas income tax return?", "Can Texas tax my capital gains or my sale of an asset?", "Can it tax my net worth?", "Can it tax an estate, my inheritance or a gift?".

The sections address the legislature, which gets no seat. Each is written as a prohibition rule (`PARTY the legislature SHANT …`) so the duty is visible, and the individual's questions are derived from the same text.

Defaults followed: the article alone; the actor named (the legislature); one case is one tax; no judgments are left to others.

## Scope

**In:** art. VIII ss 24-a, 24-b, 25, 26.

**Out:** every other section of art. VIII (property tax, homestead exemptions in s 1-b, the s 29 transfer tax on real property except as cited by s 26(b)); federal income tax (`subjects/us/internal-revenue-code-of-1986/`); Texas's franchise, sales and property taxes.

## Regulative rules

Four `SHANT` rules for the legislature, none with a deadline (each stands until the Constitution is amended): ss 24-a, 24-b, 25, 26(a).

## What the article turns out to say

1. **There is no Texas individual income tax, and none can be enacted without amending the Constitution.** Section 24-a: "The legislature may not impose a tax on the net incomes of individuals, including an individual's share of partnership and unincorporated association income." So there is no Texas return to file and no Texas withholding from wages. Asserted. The deposited text shows s 24 as "(Repealed Nov. 5, 2019.)", the same day s 24-a was added.
2. **The bar is on a tax on "net incomes".** A gross-receipts tax on a business (the franchise tax) is a different question, outside this encoding.
3. **The capital gains bar reaches a tax on selling an asset payable by the seller, but not property, sales or use taxes.** Section 24-b(a), (b). Asserted.
4. **Death taxes are barred outright; transfer taxes on inheritances and gifts are frozen at 1 January 2025.** Section 26(a)(1) bars an estate, inheritance or death tax; (a)(2) bars a transfer tax on an estate, inheritance, legacy, succession or gift "if the tax was not in effect on January 1, 2025", and (a)(3) bars increasing one that was. A gift tax on a motor vehicle and property tax are left alone (s 26(b)). The encoding answers the inheritance question conditionally on whether such a tax was in effect on 1 January 2025, a fact the article does not state. Asserted.

## Before relying on it

Nothing further is needed for the income tax answer. An independent check of s 26's reach would help.
