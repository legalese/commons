# Maryland Family Investment Program (Human Services Title 5, Subtitle 3) — baseline encoding

## Method

**Baseline.** Written straight from the deposited text with the `writing-l4-rules` skill, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18. No REFUSE. No pipeline, no coverage table, no independent test pass, no human gate. Not for public use as advice.

One module, `fip.l4`: the rules in the statute's own terms (family, applicant, recipient, work activity, exemption, good cause, the local department and the Department), and the exported questions for the applicant or recipient under `§§ Questions for the applicant` and the later headings, each calling the rules. Two duties are written as regulative rules (`DEONTIC`): the bar on reducing or terminating TCA within 30 days of the first written notice of noncompliance (s 5-312(e)(4), a `SHANT` on the Department) and the 30-day conciliation period in which the recipient may comply before a reduction becomes permitted (s 5-312(e)(3)). One case file, `fip-cases.l4`; expected values were worked out by hand from the text.

There was no earlier encoding of this subject.

## Edition

Human Services Article ss 5-301 to 5-323 as in effect on 1 October 2026 (mgaleg.maryland.gov, "include enactments of the last session: Yes"), deposited 2026-10-20 at `../../registers/source-bundle/human-services-title-5-subtitle-3-family-investment-program.txt`. s 5-304 has a future version (effective 30 September 2029) and s 5-310 two contingency versions; none of them is encoded.

**The amount of temporary cash assistance is not in the statute.** s 5-315(c) says only that it is "determined with due regard to the available resources, necessary expenditures, and specific conditions of a family" and "sufficient ... to provide a child with a reasonable subsistence"; s 5-316(a) is a budgeting duty on the Governor (61.25% of the State minimum living level, TCA and food stamps combined), not a figure for any family. The payment levels and the income and resource tests are in COMAR Title 07, which is **not deposited**: the official host (dsd.maryland.gov) answered 403 to robots.txt on 2026-10-19 (see `subjects/us/md/README.md`). So the grant amount and the adults' portion are inputs, and "meets all other FIP requirements that the Secretary establishes by regulation" (s 5-308(a)(3)(iv)) is asked as one fact.

## Checks

- `fip-cases.l4`: 41 assertions written, 41 satisfied, 0 errors, 0 warnings. One `#TRACE` (the Department cuts the grant on day 12) prints `BREACH` by the Department, as its `-- expect:` comment says.
- `fip.l4`: 0 errors, 0 warnings.
- Stable `l4` of VS Code extension legalese.l4-vscode 1.6.98, `JL4_LIBRARY_PATH` unset; diagnostics read.

## Seat

**The applicant or recipient**: the parent, caretaker relative or pregnant individual who asks "Can my family get TCA? Am I exempt from work activity? How many hours can they make me do? Can my grant be cut, by how much, and when?"

Defaults:

- **The Act alone, with the instruments that set its numbers.** Followed as far as the deposit allows; the regulations that set the numbers (COMAR) are not deposited, so the numbers are inputs.
- **The actors the text names.** The applicant, the recipient, the family, the local department, the Department, the Secretary, the Child Support Administration.
- **Judgments left to someone else, answered conditionally.** Good cause and adequate reason for child support (s 5-308(d), (e); the FIP and the Child Support Administration decide), the hardship exemption (s 5-313(b)), the caseworker's view that transitional assistance is appropriate (s 5-312(f)(2)), the social worker's confirmation for a minor parent (s 5-312(b)(3)(iii)), and suspension of s 5-308(a)(4) for new applicants (s 5-308(a)(5)): all asked as facts.
- **Definitions from facts; borrowed terms as facts.** Work activity (s 5-301(i)) is asked as one fact; "severely disabled" and "work-eligible" are not defined in the subtitle and are asked.
- **One case is one family's application or case.**
- **Machinery out**: ss 5-302 to 5-307 and 5-316 to 5-323 (the Department's plans, contracts, budgets, demonstration sites, mentoring, reports).

## Scope

In: ss 5-308(a)(2), (3), (4), (6), (7), (b), (c) (as "good cause" asked), (d), (e) (as facts), (h); 5-312(b), (c), (e), (f)(1), (2); 5-313(a), (b)(1) (as a fact); 5-315(b).

Out: the amount of TCA and the income and resource tests (COMAR); sponsor deeming (s 5-312(d)); ss 5-308.1 and 5-308.2 (conditions on work experience and community service placements); s 5-309 (assessment, the agreement, welfare avoidance grants); s 5-310; s 5-311 (recertification); s 5-314 (substance abuse screening); medical assistance and food stamps continuing (ss 5-312(e)(6), 5-315(d)), which belong to other programmes.

## Links

TCA is "the cash assistance component of the FIP that is funded wholly or partly through Title IV, Part A, of the Social Security Act" (s 5-301(f)): `subjects/us/social-security-act/` holds 42 U.S.C. 601-619 (TANF). The 60-month limit in s 5-313(a)(1) mirrors 42 U.S.C. 608(a)(7). SSI (s 5-315(b)) is Title XVI of the same Act.

## What the Act turns out to say

1. **The 24-month rule has no exemption for an adult who is exempt from work.** s 5-313(a)(2) bars TCA to a family with an adult who "has received more than 24 cumulative months" of federally funded TCA and "is not participating in a work activity". Nothing in s 5-313 carves out an adult exempt under s 5-308(b) (for example one caring for a baby under 1), and the hardship exemption of s 5-313(b)(1) is from "the limitation under subsection (a)(1)" only. Read literally, a mother past 24 months who stops work activity to care for a newborn loses TCA, although s 5-308(b)(3) says her exemption "may not be restricted to a maximum number of months". The only way out in the text is "regulations that the Secretary adopts" (s 5-313(a), not deposited). Asserted.
2. **The two sanctions are not said to compound.** s 5-312(e)(1) reduces "the portion of a recipient's grant amount designated for the adult" members by 30%; (e)(2) reduces "the entire grant amount" by 25%. Where both apply, the text does not say whether the 25% is taken before or after the 30%. The encoding takes each of the unreduced amount (700 - 75 - 175 = 450 in the cases). Taking the 25% after the 30% would give 468.75.
3. **The 55-hour proviso says "or".** s 5-308(a)(6)(iv) allows 55 combined hours for two parents with federally funded child care "provided that an adult in the family does not have a disability or is not caring for a child with a disability". Read literally that holds unless one adult both has a disability and cares for a disabled child. The encoding reads it as "no adult has a disability or cares for a child with a disability", and where the proviso fails the text sets no other figure: the answer says so rather than guessing 35.
4. **A six-month gap exempts from work activity.** s 5-308(b)(2)(iii) requires the Secretary's exemption criteria to include "adults who have not received assistance for at least 6 months". As written this exempts every applicant who has been off assistance for six months, which covers most first applications. Encoded as written; asserted.
5. **"Entitled".** s 5-312(c) says "A recipient who meets the requirements of the FIP is entitled to temporary cash assistance benefits", while the federal TANF statute says Part A creates no individual entitlement (42 U.S.C. 601(b)). The State text governs the Maryland answer; the encoding says "entitled".
6. **The bar on early cuts runs from the first notice, not the finding.** s 5-312(e)(4) counts 30 days "after the day on which the first written notice of noncompliance was sent", so the day of sending is day 0 in the regulative rule, and a cut on day 30 is still within the bar.

## Before relying on it

- Deposit the COMAR Title 07 TCA regulations once the Division of State Documents allows the fetcher, and encode the payment standard and the income and resource tests.
- Encode s 5-309 (the agreement and assessment) and s 5-311.
- An independent test pass, and a person's check of findings 1 to 4.
