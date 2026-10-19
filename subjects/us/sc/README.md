# south-carolina/

South Carolina (US state) legislation, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md).

The subjects here were laid out on 2026-09-23 for the legislation governing twelve everyday topics. Each was checked against the South Carolina General Assembly - South Carolina Code of Laws (South Carolina Legislative Council / Legislative Services Agency); the check is recorded in each subject's `registers/source-bundle/*.meta.json`. No statute text has been deposited and nothing is encoded yet.

**Licence category: unclear.** **Metadata only until resolved.** No human has recorded a licence decision for this jurisdiction in `tools/topics/round3/licence-decisions.json`. The register's own terms, quoted above, are the evidence to decide on.

## Register access

Fully accessible. Plain HTTPS GET with the honest user agent 'canon-legislation-indexer/1.0 (legalese/canon corpus metadata survey)' worked with no challenge, no CAPTCHA and no block. Structure: /code/statmast.php is the master index of the 63 Titles with the Legislative Council's disclaimer and currency statement; /code/titleNN.php is a per-title chapter index; /code/tNNcCCC.php is a per-chapter page (note the zero padding - Title 8 Chapter 11 is /code/t08c011.php, Title 41 Chapter 10 is /code/t41c010.php). Chapter pages carry the full statutory text, so only the chapter heading, article headings, section numbers, section catchlines and HISTORY effective-date lines were read and recorded; the downloaded copies of the larger chapter pages were deleted immediately after the headings were extracted, and no statute text was copied into this record. The site sits behind Cloudflare: 2 of about 22 requests returned a transient HTTP 522 (origin timeout) and succeeded on a single retry after a pause; this is a flaky origin, not a block. About 22 requests in total, spaced 2 s apart. Verification used only the register's own index, title, chapter and disclaimer pages.

## Topics with no legislation here

- **Termination/severance**: No South Carolina statute governs termination of employment or severance pay. South Carolina is an at-will state and the exceptions are common-law (public policy; handbook-based contract). The only statutory rule on separation is sec. 41-10-50 in the Payment of Wages chapter, requiring final wages to be paid within 48 hours of discharge or by the next regular payday: that is a wage-payment duty, not a termination statute, and it is already captured under Payroll/wages. Collective redundancy notice is federal (WARN Act, 29 U.S.C. ch. 23); there is no South Carolina mini-WARN Act. Verified by reading the Title 41 chapter index at https://www.scstatehouse.gov/code/title41.php, on which no chapter deals with termination or severance.
- **Passenger compensation**: No state statute. Compensation for denied boarding, delay and cancellation is federal: 14 C.F.R. part 250 and 49 U.S.C. ch. 417 for air, 49 U.S.C. for rail. Title 58's carrier chapters (ch. 58-13 Carriers Generally, ch. 58-23 Motor Vehicle Carriers, ch. 58-25 Regional Transportation Authority Law), verified on https://www.scstatehouse.gov/code/title58.php, regulate carriers for safety, franchising and rates and create no passenger compensation entitlement.
- **Customs/duties**: Federal matter. Customs duties and tariffs are exclusively federal (Tariff Act of 1930, 19 U.S.C.); U.S. Const. art. I, sec. 10, cl. 2 bars states from laying imposts or duties on imports or exports.
- **Work permits/immigration**: Federal matter. Immigration status and work authorisation are governed by the Immigration and Nationality Act, 8 U.S.C., and I-9 verification by 8 U.S.C. sec. 1324a. South Carolina's adjacent provisions are employer-verification mandates riding on the federal scheme, not work-permit schemes: Title 41, Chapter 8 (Illegal Aliens and Private Employment), Title 8, Chapter 14 (Unauthorized Aliens and Public Employment) and Title 8, Chapter 29 (Verification of Lawful Presence in the United States), all verified in force on the register's own title indexes, with Title 8, Chapter 30 marked [REPEALED].

## Benefits and personal income tax sample (text deposited 2026-10-20)

Code text was deposited on 2026-10-20 for a connected set on personal income tax and state benefits. It was taken from the Legislative Council's "South Carolina Code of Laws Unannotated" on www.scstatehouse.gov: 6 chapter pages, all HTTP 200. robots.txt was honoured, and every request used the User-Agent `legalese-commons-source-fetcher/1.0 (+https://github.com/legalese/commons)`. The register publishes one page per chapter, so a chapter is the unit, except for the homestead extract.

| Subject | File in `registers/source-bundle/` | Unit | What it gives a person |
| --- | --- | --- | --- |
| `south-carolina-code-of-laws-title-12-chapter-6-south-carolina` (existing) | `sc-code-title-12-chapter-6-income-tax-act.txt` | whole ch. 6 | South Carolina income tax owed: IRC adoption (12-6-40), rates and bracket indexing (12-6-510, 12-6-520), gross income and modifications (12-6-1110 ff.), deductions including retirement income (12-6-1140, 12-6-1170), credits including the EITC (12-6-3632), returns and withholding. It also covers corporate tax, which is not needed for individuals. |
| `south-carolina-code-of-laws-title-41-chapter-35-employment-and` (existing) | `sc-code-title-41-chapter-35-benefits-and-claims.txt` | whole ch. 35 | Unemployment benefits: amount, duration, eligibility, disqualification, claims, appeals, extended benefits |
| same | `sc-code-title-41-chapter-27-general-provisions-definitions.txt` | whole ch. 27 | The definitions that ch. 35 uses (employment, wages, base period, and so on) |
| same | `sc-code-title-41-chapter-39-protection-of-rights-and-benefits.txt` | whole ch. 39 | Benefits not assignable or waivable |
| `south-carolina-code-of-laws-title-43-chapter-5-public-aid-assistance-and-relief` (new) | `sc-code-title-43-chapter-5-public-aid-family-independence-act.txt` | whole ch. 5 | Public assistance, appeals, general relief, and the Family Independence Act of 1995 (43-5-1105 ff.): time limits (43-5-1170), work requirements, asset limits (43-5-1200) |
| `south-carolina-code-of-laws-title-12-chapter-37-homestead-exemption` (new) | `sc-code-title-12-chapter-37-sections-245-to-295-homestead-exemption.txt` | 14 sections of ch. 37, art. 3 | Homestead exemption for owners aged 65 or over, totally and permanently disabled, or legally blind (12-37-250) |

**How the pieces connect.**

- *Read in the deposited text:*
  - "Internal Revenue Code" means the IRC of 1986 "as amended through December 31, 2024" (12-6-40(A)(1)(a)), which ties it to `subjects/us/internal-revenue-code-of-1986`.
  - South Carolina gross income is determined without IRC section 86 (Social Security and Tier 1 Railroad Retirement Benefits) (12-6-1120(4)), so Social Security benefits taxed federally under 26 U.S.C. 86 are not taxed by the State.
  - The EITC is a nonrefundable credit of 125% of the federal earned income credit under IRC section 32, for full-year residents, phased in under 2017 Act No. 40 (12-6-3632 and its Editor's Note).
  - From tax year 2022 the rates are 0% / 3% / 6%. The top rate is phased down from 6.5% subject to revenue triggers, and the brackets are indexed (12-6-510(B)).
  - "Family Independence" is defined as "Aid to Families with Dependent Children" cash payments (43-5-1110(1)).
  - Ch. 43-5 refers to Title IV-D and Title IV-E of the federal Social Security Act.
  - The homestead exemption covers the first $50,000 of the fair market value of the dwelling (12-37-250(A)(1)). Disability may be classified by "a state or federal agency".
- *Unverified (general knowledge):*
  - Family Independence is South Carolina's TANF programme under SSA Title IV-A (42 U.S.C. 601 ff.).
  - SNAP is federal under the Food and Nutrition Act of 2008.
  - UI benefits are federally taxable under 26 U.S.C. 85, and South Carolina follows that by conformity.

**Terms.** Verdict: *conditions*, met.
- The Code index expressly permits copying "Code text, numbering, history, and Effect of Amendment, Editor's, and Code Commissioner's notes ... without need for permission".
- The site disclaimer says "This information is intended for personal, not commercial, uses". That line is met by the owner's ruling of 20 October 2026 that Legalese Commons is non-commercial use, which is recorded in each SOURCE-LICENSE.md.

**Currency.** "The South Carolina Code on the General Assembly's website is now current through the 2025 Session of the General Assembly" (read 2026-10-20). 2026-session changes may be missing. The official version is the print Code.

**Gaps.**
- Chapters 41-37 (employer coverage) and 41-41 (offences) were fetched but not deposited.
- The South Carolina Code of Regulations (DSS regulations, ch. 114) was not sourced. It sets Family Independence payment amounts.
- Ch. 12-6 is deposited whole (about 510,000 characters), including corporate provisions.

## Administrative regulations checked 2026-10-20 (nothing deposited)

The question was where South Carolina sets the **amounts** a person gets: the Family Independence grant, the state SSI supplement (Optional State Supplementation), and the UI maximum weekly benefit.

**Terms read.** The South Carolina Code of Regulations index (https://www.scstatehouse.gov/coderegs/statmast.php, read 2026-10-19 UTC) says the unannotated Code of Regulations, "consisting only of Regulation text, numbering, and history, may be copied from this website at the reader's expense and effort without need for permission". It says the files are "current through State Register Volume 50, Issue 3, effective March 27, 2026", and that the online version "is not official". The site disclaimer says the information "is intended for personal, not commercial, uses", which the owner's ruling of 20 Oct 2026 meets (Legalese Commons is non-commercial use). robots.txt allows /coderegs/. Verdict: **clean**. Chapter 114 (Department of Social Services) is offered only as PDF and Word; its HTML link is commented out.

**Why nothing was deposited:**
- The Chapter 114 PDF (https://www.scstatehouse.gov/coderegs/Chapter%20114.pdf) returned **HTTP 522** (origin timeout) at 2026-10-19T18:54:57Z. Under the access rules a timeout stops the host, so www.scstatehouse.gov was not used again in this pass, and the Word version was not tried.
- The Department of Social Services (dss.sc.gov) timed out on robots.txt, and the Department of Health and Human Services (www.scdhhs.gov, which runs OSS) answered HTTP 403 to robots.txt. Both hosts were dropped.

**Remaining gaps (unchanged):** the Family Independence payment amounts; the OSS amount; the UI weekly maximum. It is unverified (general knowledge) whether Chapter 114 sets Family Independence dollar amounts at all; they may sit in the DSS policy manual instead. A later pass should retry the Chapter 114 PDF on a fresh day.
