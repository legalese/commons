# Wyoming POWER, state SSI supplement and burial assistance (W.S. 42-2, with DFS rule 049.0030 ch. 1) — baseline encoding

## Method

**Baseline.** Written straight from the deposited text, from the seat of the caretaker relative applying for or receiving POWER (and of the SSI recipient for the state supplement), with the design defaults ruled on 2026-10-18. No REFUSE. Checked with the stable `l4` of VS Code extension 1.6.98, `JL4_LIBRARY_PATH` unset. No pipeline, no coverage table, no independent test pass, no human gate. **Not for public use as advice.**

## Edition

- Wyoming Statutes Title 42 chapter 2 (the Public Assistance and Social Services Act), the Legislative Service Office's title 42 PDF (created 2026-05-08), downloaded 2026-10-19, deposited at `../../registers/source-bundle/wy-stat-42-ch02.txt` (unofficial).
- **Brought in** (the instrument that sets the Act's numbers): the Department of Family Services' POWER rule, Chapter 1 (Reference 049.0030.1.01122018, in effect from 01/12/2018, current on 2026-10-19), deposited in the sibling subject `../../../wyoming-administrative-rules-049-0030-chapter-1-power-program/registers/source-bundle/wy-rules-049-0030-ch1-power.txt`. Its licence note is appended to this folder's `SOURCE-LICENSE.md`.

**Amounts not deposited (inputs).** The current maximum POWER payment: the statute prints the 2008 table and adjusts it each July by the Wyoming cost-of-living index (42-2-103(e)(iii)); the adjusted figures are not published as a rule. The shelter qualified and disqualified maxima (rule s 9(a)(iv)) are folded into that input. The state SSI supplement amount is set in the budget. The figures in the cases are hypothetical.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `wy-power.l4` | `wy-power-cases.l4` | 35 written, 35 satisfied |

Plus four `#TRACE`s of the two reporting rules with `-- expect:` comments (two FULFILLED, two breaches by the recipient, read in the output). `l4 run` on both files: 0 errors, 0 warnings (2026-10-24). Every expected value was worked by hand from the text.

## Seat

**The caretaker relative** applying for or receiving POWER for a dependent child; for W.S. 42-2-103(d), **the SSI recipient**; for 42-2-103(c), the family of a recipient who has died. Questions: "Is my child a dependent child?", "Are we under the asset limit?", "What was the 2008 maximum?", "What is our payment?", "How much is the earned income incentive?", "Do the five years apply?", "Am I entitled to the state SSI supplement?", "How much burial assistance?", and, as rules with deadlines, reporting a change and providing verifications within ten days.

Defaults (2026-10-18): the Act plus the rule that sets its numbers; the actors it names (the recipient, the department); the department's determinations (school attendance, total disability, extensions, domestic violence waivers) asked as facts; one case is one assistance unit in one month.

## Federal frame

POWER is Wyoming's TANF programme; the Act refers to sections 402, 407 and 408 of the Social Security Act as amended by P.L. 104-193 (W.S. 42-2-103(b)(ix), (xii), (xiii)). Title IV-A and Title XVI (SSI) are deposited in `subjects/us/social-security-act/`.

## Scope

**In:** W.S. 42-2-103(c), (d), (e)(i), (iii), (iv) (the fixed disregard), (viii) (as a fact); 42-2-104(b); 42-2-106(c); 42-2-109(b) (a rule); rule s 6(a)(x)(A); s 9(a)(v), (vii)(B)(I)-(VII), (X); s 9(a)(vii)(G) (a rule); s 9(b)(xii)(C).

**Out:** Medicaid (art. 4); child care copayments (42-2-103(f)); the individual earned income disregard (42-2-103(e)(iv)(A)-(G)); deeming (rule s 9(a)(vi)); Pay-After-Performance work and child support requirements (rule ss 7, 8); minor parents; the approved educational programme (42-2-109(a)); appeals (42-2-110, which sets no deadline).

## What the law turns out to say

1. **The dependent child definition runs three conditions together.** W.S. 42-2-104(b): a child "under eighteen (18) years of age and living with a relative ..., regularly attending school or its equivalent as determined by the department, or is expected to graduate from high school before the age of nineteen (19) years". The rule reads it as "up to age 18 or up to age 19 when expected to graduate" (s 9(a)(ii)(B)). This encoding requires living with a relative in every case, school attendance under 18, and expected graduation for an 18-year-old. Asserted.
2. **The statute prints a 2008 payment table and an indexing rule, but no current figure.** The table (1: $290 ... 7 and above: $566) is kept as a question; the current maximum is an input. Asserted (the table).
3. **One disregard: $600, or $1,200 for a married couple** (42-2-103(e)(iv)); the rule limits the $1,200 to a married couple with a child in common. The payment is the maximum less (earnings over the disregard plus unearned income), payable only while that balance is "less than" the maximum (rule s 9(a)(vii)(B)). Asserted.
4. **Veterans' service-connected disability compensation is not counted if its annual amount is at or below the poverty level** (42-2-106(c)). Asserted.
5. **The five-year limit has a full exemption for the totally disabled and their full-time carers** (42-2-103(e)(i)), and the domestic violence provision says time limits "shall be waived under paragraph (i)" ((e)(viii)), though paragraph (i) itself does not mention domestic violence. The encoding asks whether the limit has been waived. Asserted.
6. **An unreported change is noncompliance.** A recipient must report new property, income or assets within ten calendar days (42-2-109(b)); the rule extends this to every change in circumstances, requires verifications within ten days of a request, and treats a late report as noncompliance (rule s 9(a)(vii)(G), s 9(b)(xii)(C)). Traced.
7. **The state SSI supplement is for SSI recipients with no other income that month** (42-2-103(d)); its amount is a budget figure. Asserted.
8. **Burial assistance is capped at $1,500 after other funds, plus up to $500 transport for a veteran** (42-2-103(c)). Asserted.

## Before relying on it

- Find and deposit the current indexed maximum POWER payments (the Department of Family Services publishes examples only, under a copyright notice with no reuse grant: read, not deposited, 2026-10-19).
- Encode the Pay-After-Performance requirements and sanctions (rule ss 7, 8).
- An independent test pass.
