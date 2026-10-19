# montana/

Montana (US state) legislation, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md).

The subjects here were laid out on 2026-09-23 for the legislation governing twelve everyday topics. Each was checked against the Montana Code Annotated, published by the Legislative Services Division of the Montana Legislature; the check is recorded in each subject's `registers/source-bundle/*.meta.json`. No statute text had been deposited when they were laid out; see the 2026-10-20 sample below. Nothing is encoded yet.

**Licence category: unclear.** **Metadata only until resolved.** No human has recorded a licence decision for this jurisdiction in `tools/topics/round3/licence-decisions.json`. The register's own terms, quoted above, are the evidence to decide on.

## Register access

Fetched cleanly over HTTPS with an honest identifying user agent ('canon-legislation-indexer/1.0 (legalese/canon metadata research)'), requests spaced ~2 seconds apart; about 16 requests. Legacy hosts leg.mt.gov and archive.legmt.gov both 301 to mca.legmt.gov, which serves static HTML. No 403, 429 or challenge was encountered, although the pages do carry an obfuscated client-side bot-detection script; every request returned HTTP 200 with full content. URL patterns used: /bills/mca/index.html (table of contents), /bills/mca/title_0XXX/chapter_0YYY/parts_index.html, /bills/mca/title_0XXX/chapter_0YYY/part_0ZZZ/sections_index.html, /bills/mca/title_.../section_.../<file>.html. No copyright or terms-of-use page exists on the MCA site (mca.legmt.gov/bills/mca/help.html has none; www.legmt.gov/terms-of-use/, www.mt.gov/copyright and mt.gov/terms-of-use all 404); only the disclaimer quoted below.

## Topics with no legislation here

- **Passenger compensation**: No state statute. Air passenger rights are federal (49 U.S.C. 41712; DOT denied-boarding rules, 14 C.F.R. pt. 250); intercity rail is Amtrak under federal law. Title 69 regulates carriers but confers no passenger compensation entitlement.
- **Customs/duties**: Federal matter, not state: Tariff Act of 1930 and the Harmonized Tariff Schedule, 19 U.S.C.
- **Work permits/immigration**: Federal matter, not state: Immigration and Nationality Act, 8 U.S.C. ch. 12; employment authorisation and verification at 8 U.S.C. 1324a.

## Benefits and personal income tax sample (sourced 2026-10-20)

Statute text was deposited for eight parts of the Montana Code Annotated, filed under three subjects, so that a member of the public can get state determinations on two topics, personal income tax and social security and benefits, and see where each one plugs into the federal set already in `subjects/us/` (`internal-revenue-code-of-1986`, `social-security-act`, `food-and-nutrition-act-of-2008`; those are indexed only, with no text). The register publishes each section as its own web page. Each deposited text is one part, built from the part's section index and its live section pages, with every page listed in the `.meta.json`.

| Subject | Parts deposited | Why it is in the set |
|---|---|---|
| `montana-code-annotated-title-15-taxation-chapter-30-individual` | 15-30 part 21 (rate and general provisions), part 23 (credits) | 15-30-2103 sets the rates: 4.7% / 5.65% for now, with a second version "(Effective January 1, 2027)" also deposited. 15-30-2120 holds the adjustments to federal taxable income. 15-30-2318 is the earned income tax credit. 15-30-2337 to 15-30-2341 are the elderly homeowner/renter credit, with its reduction table kept. |
| `montana-code-annotated-title-39-labor-chapter-51-unemployment` | 39-51 part 2 (definitions), 21 (eligibility), 22 (amount and duration), 23 (disqualification) | Unemployment insurance benefits: weekly benefit amount 39-51-2201, maximum 39-51-2204. |
| `montana-code-annotated-title-53-chapter-4-tanf` | 53-4 part 2 (TANF general provisions), part 6 (TANF cash assistance) | Cash assistance under the TANF block grant. |

The plan gave the top rate as 5.9%. The deposited 15-30-2103 (temporary version) shows 5.65%. The plan also listed a separate senior property tax relief instrument. In Montana that relief is the income tax credit at 15-30-2337 ff., so it sits inside part 23.

**How the pieces connect, as read in the deposited texts.**

- 15-30-2120(1): Montana taxable income is federal taxable income plus the additions in subsection (2) and minus the subtractions in subsection (3) (IRC subject). 15-30-2120(3)(g) gives an additional subtraction of $5,500 for each taxpayer aged 65 or over. No subtraction for Social Security benefits appears in 15-30-2120, so benefits taxable federally under IRC section 86 appear to stay in Montana taxable income. That is an inference from the deposited text; confirm it before encoding.
- 15-30-2318: the credit is 20% of the federal earned income credit under IRC section 32 (26 U.S.C. 32), refundable.
- 53-4-201(13): "temporary assistance for needy families" means the federal block grant under 42 U.S.C. 601 et seq. (social-security-act subject, Title IV-A); 53-4-201(12), the state plan certified by the federal agency.
- 39-51 part 2 defines employer and employment by reference to the Federal Unemployment Tax Act (IRC ch. 23).
- 39-51-2207 requires claimants to be told that unemployment compensation is subject to federal income tax (IRC section 85), and lets them elect federal withholding; 39-51-2203 reduces benefits for certain other payments, with payments under the Social Security Act treated differently.
- Unverified (general knowledge): the UI programme runs under SSA Titles III and IX; SNAP is federal (food-and-nutrition-act-of-2008). No Montana state supplement to SSI was looked for in this sample.

**Terms.** The disclaimer on the MCA index page and in every page footer, read 2026-10-20, says the Internet version "is provided as a research tool" and that "the printed version will prevail". The help page says the online MCA carries no annotations other than histories. Those histories were removed from the deposited text. https://mca.legmt.gov/robots.txt returns 404, so all paths are allowed. Verdict: clean.

**Currency.** Montana Code Annotated 2025 (the 2025 session), with the site marked "Updated August 2026". Sections marked "(Temporary)" are deposited as published; where the register shows a later "(Effective ...)" version on the same page, both are kept.

**Gaps.** Not sourced: the other parts of the three chapters (withholding, administration, employer contributions, claims procedure, extended benefits, TANF training part 7) and the Administrative Rules of Montana.

## Administrative rules: sourcing attempt 2026-10-20 (nothing deposited; index only, flagged)

Montana's TANF benefit standards and other assistance amounts are set by the Department of Public Health and Human Services in the Administrative Rules of Montana (ARM), Title 37. Chapter 37.78 covers TANF (unverified (general knowledge)). Nothing was deposited.

- **Host.** The ARM is published by the Secretary of State at https://rules.mt.gov. The page is a JavaScript application on a vendor platform: its HTML describes itself as "Esper ... cloud-based platform to help governments proactively manage public policy". Rule text is served only through the vendor's API (`/api/policy-library`, addressed by collection, section and policy UUIDs), and the application also posts viewing metrics (`/api/consumption-metrics`).
- **robots.txt.** https://rules.mt.gov/robots.txt, read 2026-10-19 (UTC): `User-agent: *` with an empty `Disallow:`, so everything is allowed.
- **Terms.** The site footer's "Disclaimer" link points to a vendor-hosted PDF, https://app.public.staging.esper.com/assets/DisclaimerForARM.pdf, which answered **HTTP 403** (an XML error body). It could not be read, and that host was not tried again. The State's general disclaimer, https://mt.gov/discover/disclaimer (read 2026-10-19), covers accuracy and endorsement only.
- **Verdict: index only, flagged.** The rules carry no copyright, since they are edicts of government. But the text sits behind a vendor's API, and the vendor's own terms for that site are unreadable. Under the brief's rule for vendor hosts, no rule text was taken. To unblock, read or obtain the Esper/SOS terms for rules.mt.gov, or written confirmation from the Secretary of State that automated reading of the public ARM is permitted.

**Remaining gaps.**
- TANF benefit standards (ARM 37.78), the state SSI supplement, if any, and the UI weekly maximum (set each year by the Department of Labor and Industry under Title 39 ch. 51) are all not sourced.
