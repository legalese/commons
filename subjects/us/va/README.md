# virginia/

Virginia (US state) legislation, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md).

The subjects here were laid out on 2026-09-23 for the legislation governing twelve everyday topics. Each was checked against the Virginia Law Portal - Code of Virginia (Virginia General Assembly, Division of Legislative Automated Systems, for the Virginia Code Commission); the check is recorded in each subject's `registers/source-bundle/*.meta.json`. No statute text has been deposited and nothing is encoded yet.

**Licence category: unclear.** **Metadata only until resolved.** No human has recorded a licence decision for this jurisdiction in `tools/topics/round3/licence-decisions.json`. The register's own terms, quoted above, are the evidence to decide on.

## Register access

Fetched over plain HTTPS with curl and an honest self-identifying user agent ('canon-legislation-indexer/1.0 (legalese/canon corpus; metadata only)'). About 22 requests, spaced ~2 seconds apart: the /vacode/ root, title index pages for Titles 38.2, 51.1, 56, 60.2 and 63.2, chapter pages for tit. 2.2 ch. 39, tit. 38.2 ch. 5, tit. 40.1 ch. 3, tit. 51.1 ch. 1, tit. 55.1 ch. 12, tit. 56 ch. 10, tit. 58.1 ch. 3, tit. 60.2 ch. 6 and ch. 8, tit. 63.2 ch. 6, two individual section pages (ss 40.1-33.3 and 60.2-801), the 2026 Updates page and the /developers page. All returned HTTP 200 as server-rendered HTML - no bot challenge, no 403, no rate limiting and no JavaScript shell (by contrast the separate lis.virginia.gov/privacy page IS a JS app and returned only 'You need to enable JavaScript to run this app'). Article-level URLs return 200 but with an empty content pane, so chapter pages were used as the citable register pages. The register also offers bulk PDF and CSV downloads through its Virginia Law Library and JSON/XML web services via https://law.lis.virginia.gov/developers.

## Topics with no legislation here

- **Passenger compensation**: Federal matter, and largely regulation rather than statute. Air passenger rights are pre-empted by the Airline Deregulation Act, 49 U.S.C. s 41713, and administered by the US Department of Transportation under 14 C.F.R. parts 250 and 259; rail passenger rights arise under 49 U.S.C. subtit. V. There is no state-level passenger compensation statute.
- **Customs/duties**: Federal matter. Customs duties and import procedure are exclusively federal (U.S. Const. art. I, s 8, cl. 1; Tariff Act of 1930, 19 U.S.C. ch. 4; Harmonized Tariff Schedule). No US state legislates on customs.
- **Work permits/immigration**: Federal matter. Immigration status and work authorisation are governed by the Immigration and Nationality Act, 8 U.S.C. ch. 12, and 8 C.F.R. part 274a. States may not issue work permits.

## Benefits and personal income tax sample (deposited 2026-10-20)

Statute text was deposited on 2026-10-20 for a Priority 3 sample: personal income tax and benefits, from the seat of the Virginia resident who asks "What income tax do I owe, and what credits and benefits can I get?". Source: the Virginia Law Portal's 'Read all' pages (law.lis.virginia.gov/vacodefull/...), retrieved 2026-10-19 UTC: **the Code as online after the 2026 Session (changes effective 1 July 2026)**. Every text is an unofficial conversion and says so at its top. 180 sections (counting those shown as Repealed or Expired), 412,065 characters in 8 files.

| Subject | File | What it holds |
|---|---|---|
| `code-of-virginia-title-58-1-taxation-chapter-3-articles-1-3-individual-income-tax` (new) | `title-58-1-chapter-3-article-1-general-provisions` | ss 58.1-300 to 58.1-319: fixed-date conformity to the Internal Revenue Code (s 58.1-301), definitions (s 58.1-302), residency, returns, assessment and refunds |
| same | `title-58-1-chapter-3-article-2-individual-income-tax` | ss 58.1-320 to 58.1-326: rates (2%-5.75%, s 58.1-320), filing thresholds (s 58.1-321), Virginia taxable income, additions, subtractions (incl. Social Security), deductions (incl. the age deduction, s 58.1-322.03) |
| same | `title-58-1-chapter-3-article-3-tax-credits-for-individuals` | ss 58.1-330 to 58.1-339.14: credits incl. taxes paid to other states (s 58.1-332) and the low-income credit / earned income credit (s 58.1-339.8) |
| `code-of-virginia-title-60-2-unemployment-compensation-chapters-2-and-6-benefits` (new) | `title-60-2-chapter-2-definitions` | ss 60.2-200 to 60.2-231: base period, benefit year, employment, wages |
| same | `title-60-2-chapter-6-benefits` | ss 60.2-600 to 60.2-637: weekly benefit amount, duration, extended benefits, eligibility, disqualification, claims and appeals |
| `code-of-virginia-title-63-2-welfare-social-services-chapter-6` (existing) | `title-63-2-chapter-6-temporary-assistance-for-needy-families` | ss 63.2-600 to 63.2-621: TANF and VIEW (work programme) |
| `code-of-virginia-title-58-1-taxation-chapter-32-article-2-real-estate-tax-relief-elderly-disabled` (new) | `title-58-1-chapter-32-article-2-elderly-and-disabled` | ss 58.1-3210 to 58.1-3218: local real estate tax exemption or deferral for owners 65+ or permanently and totally disabled |
| same | `title-58-1-chapter-32-article-2-3-disabled-veterans` | ss 58.1-3219.5 to 58.1-3219.8: exemption for veterans with a 100% service-connected, permanent and total disability |

**How the pieces connect** (read in the deposited texts unless marked):

- Virginia taxable income of a resident is "his federal adjusted gross income for the taxable year" with the Virginia modifications (s 58.1-322), and terms take their federal meaning, with references to the Internal Revenue Code fixed "as they existed on December 31, 2025" (s 58.1-301) -- `subjects/us/internal-revenue-code-of-1986`.
- Social Security benefits are subtracted: s 58.1-322.02 subtracts "Benefits received under Title II of the Social Security Act and other benefits subject to federal income taxation solely pursuant to s 86 of the Internal Revenue Code" (`subjects/us/social-security-act`, Title II; IRC s 86). The age deduction (s 58.1-322.03) uses an "adjusted federal adjusted gross income" that leaves those benefits out.
- The earned income credit is a share of the federal credit "pursuant to s 32 of the Internal Revenue Code": for taxable years 2025 and 2026 a refundable credit of 20 percent of the federal credit (s 58.1-339.8).
- Unemployment compensation is defined against the Federal Unemployment Tax Act (26 U.S.C. 3301 ff.) and the Social Security Act (ch. 2), and "state law" means one approved by the US Secretary of Labor under 26 U.S.C. 3304 (ch. 6). That benefits are taxable federally (26 U.S.C. 85) and that Virginia taxes them: unverified (general knowledge).
- TANF is administered "in compliance with Titles IV-A and IV-F of the Social Security Act and related federal regulations" as in effect when PRWORA (P.L. 104-193) was enacted (s 63.2-600). SNAP is federal (`subjects/us/food-and-nutrition-act-of-2008`).
- Real estate tax relief is local: the article enables each locality to grant it by ordinance within the article's limits.

**Terms**: clean. law.lis.virginia.gov has no robots.txt (404). The register says its online database "excludes material copyrighted by the publisher, Michie" (annotations and revisors' notes); the footer reads "(c) Copyright Commonwealth of Virginia ... All rights reserved.", read as covering the website, not the law. No terms of use restrict reuse. Details in each subject's `SOURCE-LICENSE.md`.

**Gaps**: the Benefit Tables in s 60.2-602 are printed online only as "SEE PRINTED BILL FOR TABLES", so the weekly benefit amount table is missing (4 places). Local ordinances under ch. 32 art. 2 are not here. Virginia's auxiliary grant (state supplement for SSI recipients in assisted living, Title 51.5 / 63.2) was not sourced. The individual income tax articles went into a new subject because the existing `code-of-virginia-title-58-1-taxation-chapter-3-income-tax` is scoped to art. 16 (withholding) in its `subject.json`.

## Administrative rules deposited 2026-10-20: benefit formulas (amounts set elsewhere)

| Subject | Text | What it sets | Characters |
| --- | --- | --- | --- |
| `virginia-administrative-code-22vac40-295-tanf-income-and-payment` (new; made under Title 63.2 ch. 6) | 22VAC40-295-10 (definitions), 22VAC40-295-50 (income eligibility), whole sections | TANF: payment = standard of assistance minus net income (50 I). Disregards include the first $50 of child or spousal support, and for earnings the SNAP standard deduction plus 20% of the remainder (50 C). The "standard of assistance" is the dollar amount by family size "established by the State Board of Social Services" (10) | 17,349 |
| `virginia-administrative-code-22vac30-80-auxiliary-grants-program` (new) | 22VAC30-80-10 (definitions), -40 (personal needs allowance), -50 (establishment of rate), whole sections | Auxiliary Grant, Virginia's state supplement for SSI recipients in assisted living, adult foster care or supportive housing: payment = rate "as set forth in the appropriation act" + personal needs allowance (amount "established by the Virginia General Assembly") - countable income | 14,381 |

**Amounts that now come from deposited text.** Only the formulas and the small fixed amounts named above. The dollar figures sit outside the Administrative Code and are **not sourced**: the TANF standards of assistance (State Board) and the AG rate and personal needs allowance (Appropriation Act).

**Terms.** Same register as the statutes (law.lis.virginia.gov). robots.txt is 404. Pages say the Administrative Code "is provided online by the Virginia General Assembly". The footer copyright notice is read as covering the website. Verdict: **clean**.

**Remaining gaps.**
- TANF standards of assistance by family size and locality group: not in the VAC and not sourced.
- The Auxiliary Grant rate and personal needs allowance: in the Appropriation Act (budget.lis.virginia.gov), not sourced.
- The UI weekly benefit table in s 60.2-602: still missing ("SEE PRINTED BILL FOR TABLES"). No Virginia Employment Commission notice was sourced.
- Code of Virginia Title 51.5 (the AG enabling statute) is not in commons.

## Encodings added 2026-10-24: tax and benefits baselines

Two baseline encodings, written from the individual's seat with the 2026-10-18 defaults and checked with the stable `l4` (1.6.98). Each folder's `NOTES.md` has the method, scope and findings.

| Encoding | Seat | Questions | Regulative rules | Assertions |
| --- | --- | --- | --- | --- |
| [`code-of-virginia-title-58-1-taxation-chapter-3-articles-1-3-individual-income-tax/encodings/baseline-2026-10`](code-of-virginia-title-58-1-taxation-chapter-3-articles-1-3-individual-income-tax/encodings/baseline-2026-10) | the individual taxpayer | am I a resident (s 58.1-302); am I below the filing threshold (s 58.1-321 A); the age deduction (s 58.1-322.03(5)); Virginia taxable income and tax (ss 58.1-320 to 58.1-325, with the Social Security subtraction); the low-income or earned income credit (s 58.1-339.8) | 2 (pay a deficiency within 30 days, s 58.1-308; amend within a year of a federal change, s 58.1-311) | 40 / 40 |
| [`code-of-virginia-title-63-2-welfare-social-services-chapter-6/encodings/baseline-2026-10`](code-of-virginia-title-63-2-welfare-social-services-chapter-6/encodings/baseline-2026-10) | the caretaker applying for TANF | the eligible child and the applicant's duties (s 63.2-602); income eligibility and the payment (22VAC40-295-50, brought in, with the immunization reduction of s 63.2-603); diversionary assistance (s 63.2-617 A); VIEW exemptions (s 63.2-609); the 24-month limit (s 63.2-612); continued payment on appeal (s 63.2-618) | 3 (the 60-day notice before termination, s 63.2-612; the hearing request and continued payment, s 63.2-618) | 36 / 36 |

Inputs, not deposited: the HHS poverty guideline, the TANF standard of assistance (State Board) and the SNAP standard deduction. Federal AGI and the federal EIC are inputs linked to `subjects/us/internal-revenue-code-of-1986/`.
