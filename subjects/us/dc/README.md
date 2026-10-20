# district-of-columbia/

District of Columbia (US) legislation, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md).

The subjects here were laid out on 2026-09-23 for the legislation governing twelve everyday topics. Each was checked against the D.C. Law Library - Code of the District of Columbia (Council of the District of Columbia, published with the non-profit Open Law Library); the check is recorded in each subject's `registers/source-bundle/*.meta.json`. No statute text has been deposited and nothing is encoded yet.

**Licence category: unclear.** **Metadata only until resolved.** No human has recorded a licence decision for this jurisdiction in `tools/topics/round3/licence-decisions.json`. The register's own terms, quoted above, are the evidence to decide on.

## Register access

Reachable and fast. About 20 GET requests on 23 September 2026 from curl with an honest, self-identifying user-agent ('canon-legislation-indexer/1.0 (metadata indexing; contact ...)'), spaced roughly 2 seconds apart; no user-agent spoofing, no browser impersonation. Every request returned HTTP 200 on the first try; no 403, no 429, no bot challenge, no CAPTCHA at any point. Stable URL shape: /us/dc/council/code, /us/dc/council/code/titles/<n>, /us/dc/council/code/titles/<n>/chapters/<n>, and .../subchapters/<roman>. Title and chapter pages print the exact caption, the child subchapters or the section catchlines, and the section range; the Code table of contents page also prints the Publication Information block with the 'Current through' date. I fetched table-of-contents pages only - no section text pages - so no statute text was copied. TWO THINGS A HUMAN SHOULD WEIGH BEFORE ANY BULK USE: (1) every page footer says 'The codes and laws on this website are in the public domain. Please do not scrape. Instead, bulk download the HTML or XML.' (the bulk repositories are github.com/DCCouncil/law-html and github.com/DCCouncil/law-xml; neither carries a LICENSE file - the GitHub API reports license: null, default branch 'publication/2021-10-18'); (2) https://code.dccouncil.gov/robots.txt allows general crawling for '*' ('Allow: /') but sets 'Content-signal: search=yes,ai-train=no' and separately disallows named AI crawlers, including 'ClaudeBot', 'GPTBot', 'CCBot', 'Google-Extended', 'Applebot-Extended', 'Bytespider', 'Amazonbot' and 'meta-externalagent'. My fetches were made under the generic '*' group (Allow: /), were metadata-only, were not a crawl and were not for model training, but the site's stated preference is bulk download over page fetching and the ai-train signal is 'no'. Curiosity worth recording: the D.C. Law Library also carries 941 'Federal Laws Codified in the D.C. Code' and 15 'Laws of the United Kingdom Codified in the D.C. Code'.

## Topics with no legislation here

- **Passenger compensation**: Federal, and largely preempted. Compensation for denied boarding, cancellation and delay comes from US DOT rules under 49 U.S.C. s 41712 (14 C.F.R. pt. 250 oversales, pt. 259 customer service), and the Airline Deregulation Act (49 U.S.C. s 41713) preempts state and District laws on air-carrier prices, routes and services; intercity rail runs on Amtrak's own contract of carriage under 49 U.S.C. subtit. V. The District's own passenger rules are for taxis and vehicles for hire and are regulatory (31 DCMR) rather than statutory - no D.C. statute grants a passenger a compensation right, so nothing is listed.
- **Customs/duties**: Federal, and constitutionally exclusive. U.S. Const. art. I, s 8, cl. 1 and s 10, cl. 2; the Tariff Act of 1930 and the Harmonized Tariff Schedule, 19 U.S.C. The District has no customs statute.
- **Work permits/immigration**: Federal. Immigration status and work authorisation are governed by the Immigration and Nationality Act, 8 U.S.C. ch. 12 (employment authorisation and employer verification at 8 U.S.C. s 1324a). The District legislates around the edges (e.g. Title 32, ch. 13C, Prohibition on Discrimination against the Unemployed) but has no work-permit statute.

## Priority 3 sample: personal income tax, and social security and benefits (deposited 2026-10-20)

Statute text for the District's personal income tax and its cash benefits was deposited on 2026-10-20 from the **bulk XML the Council itself offers**, with the owner's approval of that route on 20 October 2026.

**Why the bulk route.** code.dccouncil.gov says on every page: "The codes and laws on this website are in the public domain. Please do not scrape. Instead, bulk download the HTML or XML." Its robots.txt names AI crawlers (ClaudeBot, GPTBot, CCBot, Google-Extended, Amazonbot, Applebot-Extended, Bytespider, meta-externalagent) and disallows `/` to them, and carries `Content-signal: search=yes,ai-train=no`. No page of code.dccouncil.gov was fetched for this deposit. The text comes from the Council's repository github.com/DCCouncil/law-xml-codified ("the code fully supplemented"), publication branch `publication/2026-05-23`, commit `9c950ac5f53283bdf32c1150a45a9245f930dedd`, taken once as a repository archive (zip, 70,317,370 bytes, sha256 `fb9dbdaa...e34287cc`) through the GitHub REST API on 2026-10-19T23:38:30Z. No git command or clone was used, and the zip was deleted after extraction.

**ai-train=no.** Commons deposits this text for public reference and for encoding the law as rules, not for model training. It should not be used as training data.

**Terms.** The repository has no LICENSE file. The Council's DC-Law project README says "All repositories are licensed under CC0". The site says the codes and laws are in the public domain, and statutory text carries no copyright anyway (*Georgia v. Public.Resource.Org*, 2020). Only the unannotated statutory text is deposited: each section's annotations (history, editor's notes) are dropped. Verdict: **conditions, met** (bulk route, no scraping, no training use). The licence line at the top of this README dates from the 2026-09-23 index check. It is superseded for these subjects by the owner's approval of 2026-10-20.

**Currency.** The Code's recency block reads "through 2026-09-26": last codified D.C. Law 26-187; emergency D.C. Act 26-416; federal Pub. L. 115-334. Build and codified date 2026-10-07. Every text is marked as an unofficial version.

| Subject | File | What | Sections | Characters |
| --- | --- | --- | --- | --- |
| `code-of-the-district-of-columbia-title-47-taxation-licensing` (existing) | `dc-code-47-ch18-subch-i-vi-individual-income-tax-2026-10` | Ch. 18 subch. I-VI: definitions, gross income, returns, the tax on residents: rates 47-1806.03, DC EITC 47-1806.04(f), Schedule H property tax credit 47-1806.06 | 58 | 185,893 |
| same | `dc-code-47-ch18-subch-xii-xvi-assessment-collection-2026-10` | Ch. 18 subch. XII-XVI: assessment, collection, withholding (47-1812.08), refunds, penalties, appeal | 42 | 44,976 |
| `code-of-the-district-of-columbia-title-47-chapter-8-residential-property-tax-relief` (new) | `dc-code-47-ch8-residential-property-tax-relief-sel-2026-10` | Homestead deduction 47-849 to 47-850.04; senior and disability relief 47-863; senior tax deferral 47-845.03; owner-occupant credit 47-864 | 9 | 51,910 |
| `code-of-the-district-of-columbia-title-51-chapter-1-unemployment-compensation` (new) | `dc-code-51-ch1-unemployment-compensation-2026-10` | Whole chapter: benefit amount and duration 51-107, eligibility 51-109, disqualification 51-110, shared work | 47 | 259,858 |
| `code-of-the-district-of-columbia-title-4-public-care-systems` (existing) | `dc-code-4-ch2-subch-i-iv-a-definitions-programs-medicaid-2026-10` | Ch. 2 subch. I-IV-A: definitions, programs, Medicaid administration, Interim Disability Assistance for SSI applicants (4-204.07) | 46 | 39,026 |
| same | `dc-code-4-ch2-subch-v-xxi-public-assistance-programs-2026-10` | Ch. 2 subch. V-XXI: TANF, GC, POWER, payment standards 4-205.52, DC supplement for SSI recipients in community residences 4-205.49(c), hearings | 188 | 204,194 |

Total: 6 texts, 390 sections, 785,857 characters.

**How the pieces connect.** These connections were read in the deposited text:
- DC "gross income" has "the same meaning as defined in § 61 of the Internal Revenue Code of 1986" (47-1803.02(a)), so the federal subject `subjects/us/internal-revenue-code-of-1986` is the starting point.
- Social security and tier 1 railroad retirement benefits taxable under IRC § 86 are excluded from DC gross income (47-1803.02(a)(2)(L)).
- Unemployment benefits paid under Title 51 ch. 1 are excluded for taxable years beginning after 31 December 2020 (47-1803.02(a)(2)(LL)), so the UI subject feeds the income tax.
- The DC EITC is a percentage of the federal credit under IRC § 32: 40%; 70% from 2022 and 85% from 2025 for filers with a qualifying child; 100% from 2029. Childless filers and ITIN filers have their own rules (47-1806.04(f)). DC EITC payments are not income for public assistance (47-1806.04(f)(3)(C)).
- The child and dependent care credit is 32% of the federal § 21 credit (47-1806.04(c)).
- Schedule H (47-1806.06) gives a credit for property tax, or for rent deemed to be property tax, in excess of a share of household income. It sits beside the homestead deduction and senior relief in Title 47 ch. 8.
- 4-205.49(c) pays $631.20 a month to SSI or GPA recipients in small community residence facilities or assisted living residences. This is the District's supplement to federal SSI (`subjects/us/social-security-act`, Title XVI).
- Recipients of TANF, SSI or unemployment compensation are excluded from POWER (4-205.72(d)).

These links were not read in deposited text and are unverified (general knowledge):
- TANF (4-205.xx) runs under the District's state plan for SSA Title IV-A.
- UI is the federal-state programme under SSA Titles III and IX and FUTA.
- UI benefits are federally taxable under IRC § 85.
- SNAP is federal (`subjects/us/food-and-nutrition-act-of-2008`).

**Gaps.**
- Ch. 18 subch. VII-XI and XVII-XIX (corporate, unincorporated business, estates and trusts, apportionment, high-tech and e-commerce credits) are out of scope for an individual.
- The rest of Title 47 ch. 8 (real property tax rates, special districts) is not deposited.
- DC Municipal Regulations (TANF payment levels set by rule, the UI maximum weekly benefit set each year by the Director under 51-107(b)(3)) were not sourced.
- The standard deduction and personal exemption follow the IRC by cross-reference in 47-1801.04 and 47-1806.02. Check them when encoding.
