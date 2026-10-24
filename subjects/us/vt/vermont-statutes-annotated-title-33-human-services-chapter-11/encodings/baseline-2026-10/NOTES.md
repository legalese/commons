# Reach Up (33 V.S.A. ch. 11) — baseline encoding

## Method

**Baseline.** Written straight from the deposited text, from the seat of the person applying for or receiving Reach Up for a family, with the design defaults ruled on 2026-10-18.
No REFUSE. Checked with the stable `l4` of VS Code extension 1.6.98, `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate. **Not for public use as advice.**
There was no earlier encoding of this chapter to keep.

## Edition

Vermont Statutes Online (Office of Legislative Counsel), **unofficial**, "now include the actions of the 2026 session", fetched 2026-10-19 (UTC), deposited at `../../registers/source-bundle/vt-33-vsa-ch11-2026.txt`. The text includes 2025, No. 136 (Adj. Sess.), effective 1 July 2026, in s 1103.

**Amounts set by rule (ADMIN-POLICY).** The Reach Up payment standard, the maximum housing allowance and the financial eligibility test ("in accordance with rules adopted by the Commissioner", s 1101(11); s 1103(a), (c)) are in the Department's rules, which are not deposited: the official Vermont rules are hosted by LexisNexis, whose terms bar automated access (README). They are **inputs**. The figures in the cases are hypothetical.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `vt-reach-up.l4` | `vt-reach-up-cases.l4` | 38 written, 38 satisfied |

Plus five `#TRACE`s of the two regulative rules, each with an `-- expect:` comment (three FULFILLED, two breaches; the breach parties were read in the output). `l4 run` on both files: 0 errors, 0 warnings (2026-10-24). Every expected value was worked by hand from the text.

## Seat

**The parent, relative or caretaker** applying for or receiving Reach Up financial assistance for a family (s 1103(a): assistance "shall be given for the benefit of a dependent child to the relative or caretaker with whom the child is living"). Questions: "Is my child a dependent child?", "Are we a family?", "Is there an asset limit?", "At least how much will we get?", "Am I within the 60 months?", "Are my requirements deferred?", "How much is a sanction?", "Do payments continue if I appeal?".
Provisions addressed to the Commissioner or the Department are encoded as what they mean for that person: the disregards the rules must give, the housing protection, the review and the continued payments.

Defaults (2026-10-18):
- **The Act alone**: chapter 11; the rules that set amounts are not deposited (inputs).
- **Actors**: the participating adult, the Department for Children and Families (its duty to continue payments is written as a rule so the person can see what they are owed).
- **Judgments left to others**: the program director's monthly determination (s 1108(e)), good cause, deferment by rule (s 1114(4)) and the availability of services (s 1115(a)) are asked as facts, and answers are phrased conditionally.
- **Definitions** from facts: dependent child, family, the countable months.
- **One case**: one family in one month.
- **Machinery out**: purposes, evaluation, Reach First / Reach Ahead, matched savings, separate State programs.

## Scope

**In:** s 1101(3), (6), (10), (12); s 1103(a), (c)(1), (c)(4), (c)(5), (f); s 1108(a)-(e); s 1114; s 1115(a); s 1116(a), (c), (f)(1), (g), (h); s 1132(b), (c).

**Out:** ss 1106, 1107, 1112 (case management and plans) except as the participation that a sanction turns on; s 1113 activity list (asked as "engaged in a work activity"); s 1103(c)(3) incentive amounts, (c)(6) transitional medical assistance, (c)(7) vehicle equity (not needed: there is no asset limit), (c)(8), (d)(2), (e) (minor parents), (g), (h); s 1116(b), (d) (forgiveness is reflected only in the month count asked); ss 1121-1123, 1131, 1133, 1134.

## Federal frame

TANF is defined by reference to Title IV-A of the Social Security Act (s 1101(26)); work activities count only "to the extent and degree that they are allowed and countable" under it (s 1101(28)). Title IV-A (42 U.S.C. 601-619) is deposited in `subjects/us/social-security-act/` (`usc42-ch7-schIV-ptA.txt`), including the federal 60-month limit (s 608(a)(7)) and its hardship exception. Cross-folder IMPORT is not possible; the link is recorded here.

## What the chapter turns out to say

1. **The statute sets only floors for the disregards, so a statutory grant is a minimum.** Section 1103(c)(1) disregards "not less than the first $350.00 per month of earnings ... and 25 percent of the remaining earnings"; s 1103(f) "not less than $100.00 per month of child support". The rules may disregard more, which can only raise the grant. The exported question is therefore "At least how much …". Asserted (payment standard $900, earnings $1,150: at least $300).
2. **Section 1108(d) cross-refers to the wrong subdivision.** The hardship exemption applies where the adult "is engaged in any of the work activities listed in subdivision 1101(2) ... with the exception of subdivision 1101(2)(L)". Section 1101(2) defines "able to work part time" and has no subdivision (L); the work activities, with an (L) for child care for a community service participant, are in s 1101(28). This encoding reads the reference as s 1101(28). Asserted (the hardship case).
3. **The hardship exemption needs none of the s 1108(b) criteria to apply.** A family past 60 months for whom a (b) criterion now applies cannot use (d) even while working; its months under (b) would not have counted, but once past 60 it falls to the director's determination under (e). Asserted. This is the text's order; whether a family meeting a (b) criterion is ever past 60 counted months depends on how the months were counted.
4. **There is no asset limit.** Section 1103(c)(5): "The Department shall not impose an asset limit for the purpose of initial and continuing eligibility". Asserted. The vehicle exclusion in (c)(7) therefore matters only for SNAP compatibility.
5. **Sanctions are flat for three months, then per adult.** $75 for each of the first three months (not per adult), then $150 "for each adult sanctioned" (s 1116(c)). Section 1116(c)(2) still says "not subject to the reduction required by subsection (e)", but (e) is repealed: the words have nothing to refer to. Asserted.
6. **The housing protection lasts six cumulative months.** For the first six months of fiscal sanctions the grant cannot fall below the family's actual housing costs (capped at the maximum housing allowance) less its other countable income (s 1116(f)(1)); after more than six cumulative months it goes (s 1116(g)). The floor never raises a grant above what it was before the sanction. Asserted.
7. **An appeal received before the effective date keeps the payments going** (s 1132(c)). The appeal is the participant's choice, written with `DO … LEST FULFILLED`: an unused `MAY` in the stable `l4` takes its `HENCE` when the time runs out, which would have put the Department under a duty to continue payments with no appeal made. Traced.
8. **To be paid during a sanction, the adult must meet the case manager at least once a month** (s 1116(h)). Traced (met: FULFILLED; not met by day 31: breach by the participating adult).

## Before relying on it

- Compare the text with the official Vermont Statutes Annotated.
- Deposit the Reach Up rules (payment standards, housing allowances, financial eligibility, the actual disregards) if a source with acceptable terms can be found, and replace the inputs.
- An independent test pass.
