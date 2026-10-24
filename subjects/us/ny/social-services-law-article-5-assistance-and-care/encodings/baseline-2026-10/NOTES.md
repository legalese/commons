# New York Social Services Law, Article 5 (family assistance) — baseline encoding

## Method

**Baseline.** Written straight from the deposited text, from the seat of the individual to whom the law is applied, with the design defaults ruled on 2026-10-18.
There is no REFUSE in it. What is outside the encoding is listed below and is not reachable from the questions, which take only facts the text uses.
Checked with the stable `l4` of VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset.
No pipeline, no coverage table, no independent test pass, no human gate.
**Not for public use as advice.**

The rules are written seat-neutrally in the statute's own terms in `ny-fa.l4`. The applicant's questions are in `ny-fa-seat.l4`, which IMPORTs the core and calls its rules. Each question has `@export` and every input a `@desc`.

Family assistance is New York's cash assistance programme under the federal TANF block grant (Title 10 of Article 5, ss 343-362). There was no earlier encoding of this Article to keep.

## Edition

NYSenate.gov Open Legislation, retrieved 24 October 2026, each section at its "most recent revision": s 131 (2026-05-22), s 131-a (2025-11-07), s 131-n (2025-08-01), s 158 (2023-01-06), s 159 (2014-09-22), ss 343, 344, 349 (2014-09-22), s 350 (2022-07-01). Deposited at `../../registers/source-bundle/ny-ssl-art5-selected.txt`, with its `.meta.json`. Sections 158 and 159 (safety net assistance) and 343, 344 (Title 10's purpose and definitions) are deposited for context but not encoded.

## Checks

| Module | Case file | Assertions |
|---|---|---|
| `ny-fa.l4`, `ny-fa-seat.l4` | `ny-fa-cases.l4` | 51 written, 51 satisfied |

`l4 run` on all three files: 0 errors, 0 warnings (2026-10-24). `l4 run` exits 0 even when an assertion fails, so the diagnostics are what was read. Two `#TRACE`s show breaches (a fair hearing on day 40, assistance given on day 45 of a 90-day disqualification), each with its expected result in an `-- expect:` comment. Every expected value was worked by hand from the text.

## Seat

**The applicant**: a parent, another relative caring for a child, or a pregnant individual. Their questions are: "Can my family get family assistance? How much a month? What counts against it? What if I quit my job? Is there a time limit?"

Provisions addressed to the social services official or district are encoded as what they mean for that person:
- what the official must judge, asked as facts (s 349 A);
- what the district must pay and when it must not (s 131(10), s 131-a(7));
- the hearing it must hold, and by when (s 131(6)).

The 2026-10-18 defaults:

- **The Act alone.** Article 5 only. The shelter and fuel allowances, set "by regulations of the department", are not deposited and are inputs.
- **The actors the text names:** the applicant or recipient, the social services official or district.
- **Judgments handed to others are answered conditionally:** "in the judgment of the social services official" (s 349 A), "independently verified" impairment (s 350(2)), "good cause" (s 131-a(8)(b)), the minor parent exceptions (s 131(6)) and whether an arrangement is "appropriate".
- **The Act's own definitions are worked out from facts:** child (s 349 A), standard of need (s 131-a(2)), exempt resources (s 131-n(1)), disregarded income (s 131-a(8)). Borrowed terms (SSI, TANF-funded assistance, the federal poverty level) are asked as facts.
- **One case:** one household, one month.
- **The Act's own terms**, quoted in the comment above each rule.
- **Machinery out:** the department's powers to make regulations, the payment access card (s 131(9)), job-service staffing (s 131(5-a)).

## Regulative rules

Three, in `ny-fa.l4`:

1. `the minor parent's fair hearing` (s 131(6)): on a timely request, the district MUST hold a fair hearing WITHIN 30 days, LEST BREACH.
2. `the voluntary quit disqualification` (s 131(10)): after a voluntary quit or reduction of earnings to qualify, the district SHANT give public assistance to the applicant WITHIN 90 days.
3. `direct payment of my shelter allowance` (s 131-a(7)): if the official finds the shelter allowance was not applied to rent, and rent is not being withheld under law or a court order, the district MUST pay the landlord directly. No time is set.

## Scope

**In:** s 349 A, B.1, D; s 131(6) (minor parents) and its fair hearing; s 131(10); s 350(2)(a) (the 60-month limit); s 131-n(1) (resources, in the version in force until 22 August 2027); s 131-a(1), (2)(a-4), (b), (d), (e), (3)(a-4), (b), (c), (3-c), (3-d), (7), (8)(a)(i)-(iii), (v), (viii), (xiii), (b), (c).

**Out:** safety net assistance (ss 157-165), to which a family past the 60-month limit is in practice moved; emergency assistance; the work requirements (Title 9-B, and s 131(5), (7) except as inputs); stepparent deeming (s 131-a(9)); the lump sum rule (s 131-a(12)); the HIV rent cap (s 131-a(14), (15)); the special items of s 131-a(5); the disregards in s 131-a(8)(a)(vii) and (ix)-(xii); s 349 B.2 (SSI-pending reclassification, an internal funding matter); s 350(1) beyond adequacy.

Read with the federal Social Security Act encoding (`subjects/us/social-security-act/`, Title IV-A, being encoded on 2026-10-24). The 60-month limit of s 350(2) carries out 42 U.S.C. 608(a)(7). Cross-folder IMPORT is not possible in the stable `l4`.

## What the Article turns out to say

1. **The basic cash allowance has been fixed in the statute since 1 October 2012.** Section 131-a(2)(a-4) and (3)(a-4) give $158 for one person, $252 for two, $336 for three, $433 for four, $534 for five and $617 for six, plus $85 for each additional person, "for the period beginning October first, two thousand twelve and thereafter". To that are added the home energy grant (s 131-a(3-c), unchanged since 1981) and the supplemental home energy grant (s 131-a(3-d), unchanged since 1986). Asserted.
2. **A child's residence is placed among the official's judgments.** Section 349 A lists "such child is a resident of the state on the date of application" as the third thing that holds "in the judgment of the social services official". It is asked as a fact. Asserted.
3. **The grant schedule equals the standard of need.** Because the maximum grant (3)(a-4) is the same table as the need (2)(a-4), a family with no countable income or resources is paid its whole standard of need. Asserted.
4. **Shelter, the largest part of the payment, is not in the statute.** Section 131-a(2)(b) includes "amounts for shelter and fuel for heating", and (2)(c) refers to "the maximum shelter allowance prescribed by regulations of the department". Those maximums are in 18 NYCRR, which is not deposited, so they are inputs. The cases use a hypothetical $400.
5. **The supplemental home energy grant is written as an increase to a superseded schedule.** Section 131-a(3-d) increases "the amounts set forth in paragraph (a) of subdivision three". That is the schedule in force "Through June thirtieth, two thousand nine". The encoding reads it with s 131-a(2)(b), which includes "amounts for supplemental home energy grants" in the standard of need, so it still applies. Interpretive.
6. **The 50 percent earned income disregard is adjusted every June, and the adjusted figure is not in the text.** Section 131-a(8)(a)(ii) sets 50 percent, "provided, however, that such percentage amount shall be adjusted in June of each year". The adjustment makes a household of three in New York City lose eligibility at the poverty line. The percentage is an input; the cases use 50%.
7. **"Income ... in excess of his or her need" in s 131-a(8)(c) is read as gross income.** An applicant with gross income above the standard of need, and no assistance in the four months before, loses the $150 disregard of (iii) but keeps the percentage disregard of (ii). Interpretive. Asserted.
8. **Resources over the exempt amount are taken off the need for the month.** Section 131-a(1) makes provision for need "less any available income or resources which are not required to be disregarded". The encoding subtracts countable resources from the month's need. The department's regulations, which are not deposited, may instead treat excess resources as making the family ineligible (unverified). For an applicant with more than a month's need in countable resources, the two readings agree: nothing is paid. Asserted as encoded.
9. **The resource exemptions in s 131-n(1) stop on 22 August 2027.** The Senate's text has two versions of s 131-n. The one encoded is marked "Effective until August 22, 2027". The version "Effective August 22, 2027" has no $2,500/$3,750/$10,000 exemption, no car, home or burial exemptions; it allows only regulations that follow federal requirements. Unless the legislature extends the first version, a family's resources will be judged under rules that are not in the statute. Not asserted (the encoding is for the current version).
10. **The 60-month limit counts safety net months, and it ends TANF-funded family assistance only.** Section 350(2)(a)(iii) counts "periods in which an adult receives cash assistance in the safety net assistance program". The limit is on assistance "funded in whole or in part under the temporary assistance to needy families block grant". Exempt are a family whose adult member cannot work because of an independently verified impairment (including one from domestic violence) and a family whose adult member receives SSI or additional state payments. Months as a minor child who was not the head of household, or married to one, are not counted. Asserted.
11. **Quitting a job to qualify costs 90 days from the day of quitting**, not from the application (s 131(10)). An application within those 90 days is deemed to be for that purpose (the presumption is in the text; the encoding asks the purpose as a fact). Asserted.
12. **Earned income credit refunds are disregarded twice over:** as income (s 131-a(8)(a)(viii)) and as resources (s 131-n(1), last paragraph). The New York EIC in the Tax Law Article 22 encoding (`../../../tax-law-article-22-personal-income-tax/encodings/baseline-2026-10/`) therefore does not reduce family assistance. Not asserted here (the questions leave EIC refunds out of income).

## What would need doing before this is worth relying on

- **The shelter and fuel allowances** (18 NYCRR Part 352) and the current s 131-a(8)(a)(ii) percentage, deposited from the Office of Temporary and Disability Assistance, so they need not be inputs.
- **Safety net assistance** (ss 157-165), the programme for single adults and for families past the 60-month limit.
- **The work requirements** (Title 9-B) and sanctions, and the application and decision deadlines (s 153 and the regulations), none of which is deposited.
- **Finding 9:** check, before August 2027, whether s 131-n has been extended.
- **An independent test pass.** Findings 5, 7 and 8 should also be checked against OTDA regulations.
