# north-dakota/

North Dakota (US state) legislation, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md).

The subjects here were laid out on 2026-09-23 for the legislation governing twelve everyday topics. Each was checked against the North Dakota Legislative Branch - North Dakota Century Code (North Dakota Legislative Council); the check is recorded in each subject's `registers/source-bundle/*.meta.json`. No statute text had been deposited when they were laid out; see the 2026-10-20 sample below. Two baselines were encoded on 2026-10-24 (see the last section).

**Licence category: unclear.** **Metadata only until resolved.** No human has recorded a licence decision for this jurisdiction in `tools/topics/round3/licence-decisions.json`. The register's own terms, quoted above, are the evidence to decide on.

## Register access

Fully accessible. Plain HTTPS GET with the honest user agent 'canon-index-builder/1.0 (+https://github.com/legalese/canon)' worked with no challenge, no rate limiting and no block. Structure discovered by probing: /cencode/tNN.html is a per-title chapter index (chapter number, chapter name, and a '[Repealed]' marker where applicable) and /cencode/tNNcCC.html is a per-chapter section index; the actual statute text is served only as /cencode/tNNcCC.pdf, which was deliberately never downloaded. Titles with a decimal use a hyphen in the path (Title 26.1 is /cencode/t26-1.html; /cencode/t261.html is a 404), and decimal chapters likewise (Chapter 54-52.4 is /cencode/t54c52-4.html). Note that /cencode/ itself returns a ~46 MB response; it was not retrieved beyond a HEAD-style size check. About 30 requests in total, spaced 2 s apart. Verification used only the register's own chapter and section index pages plus the Century Code landing page and the site's disclaimer page.

## Topics with no legislation here

- **Passenger compensation**: No state statute. Compensation for denied boarding, delay and cancellation is federal: 14 C.F.R. part 250 and 49 U.S.C. ch. 417 for air, 49 U.S.C. for rail. Title 49 of the Century Code regulates rail and pipeline carriers for safety and rates, and its motor carrier chapter 49-18 is marked [Repealed] on the register's own index; no chapter creates a passenger compensation entitlement.
- **Customs/duties**: Federal matter. Customs duties and tariffs are exclusively federal (Tariff Act of 1930, 19 U.S.C.); U.S. Const. art. I, sec. 10, cl. 2 bars states from laying imposts or duties on imports or exports.
- **Work permits/immigration**: Federal matter. Immigration status and work authorisation are governed by the Immigration and Nationality Act, 8 U.S.C., and I-9 verification by 8 U.S.C. sec. 1324a. The Century Code has no immigration or work-permit chapter; the nearest state provision is ch. 34-15 (Directory of New Hires), which is a child-support reporting register, not a work-authorisation scheme.

## Benefits and personal income tax sample (sourced 2026-10-20)

Statute text was deposited for five chapters of the North Dakota Century Code, so that a member of the public can get state determinations on two topics, personal income tax and social security and benefits, and see where each one plugs into the federal set already in `subjects/us/` (`internal-revenue-code-of-1986`, `social-security-act`, `food-and-nutrition-act-of-2008`; those are indexed only, with no text).

| Subject | Chapter | Why it is in the set |
|---|---|---|
| `north-dakota-century-code-chapter-57-38-income-tax` | N.D.C.C. ch. 57-38 | The personal income tax. Section 57-38-30.3 sets the individual rate schedules (0% / 1.95% / 2.50% by filing status, kept as tables) and the adjustments to federal taxable income. |
| `north-dakota-century-code-chapter-52-06-benefits` | N.D.C.C. ch. 52-06 | Unemployment compensation: eligibility, weekly benefit amount, disqualifications. |
| `north-dakota-century-code-chapter-50-09-aid-to-dependent-children` | N.D.C.C. ch. 50-09 | Cash assistance. Sections 50-09-28 and 50-09-29 make the chapter the state's TANF programme under title IV-A of the Social Security Act. |
| `north-dakota-century-code-chapter-50-24-5-aid-to-aged-blind-and-disabled` | N.D.C.C. ch. 50-24.5 | Aid to aged, blind and disabled persons: basic-care supplementation for people on SSI/Medicaid. |
| `north-dakota-century-code-chapter-57-02-general-property-assessment` | N.D.C.C. ch. 57-02 | Section 57-02-08.1, the homestead credit for people 65+ or disabled and the renters' refund; 57-02-08.9 and 08.10, the primary residence credit. |

**How the pieces connect, as read in the deposited texts.**

- Income tax starts from federal taxable income: 57-38-01(13) defines "taxable income" as federal taxable income plus or minus the chapter's adjustments, and 57-38-01(5) and (15) read references to the Internal Revenue Code as the IRC of 1986 (IRC subject).
- 57-38-30.3(2)(s) reduces North Dakota taxable income by the social security benefits included in federal AGI under IRC section 86, so Social Security benefits taxable federally are not taxed by North Dakota.
- 50-09-28 substitutes "temporary assistance for needy families" for the old aid-to-dependent-children terms, referring to section 402 of the Social Security Act as added by Pub. L. 104-193; 50-09-29 sets the requirements for administering TANF (social-security-act subject, Title IV-A).
- 50-24.5-01 defines "aged", "blind" and "disabled" by the SSI programme under titles II and XVI of the Social Security Act and requires eligible beneficiaries to apply for those benefits and Medicaid (title XIX).
- 52-06 lets the waiting week be suspended when federal reimbursement is available (52-06-01), and 52-06-02(15) reduces benefits for a week in which an employer-funded pension is received, federal social security retirement benefits excepted.
- Unverified (general knowledge): North Dakota has no state earned income tax credit; UI benefits are federally taxable under IRC section 85 and the programme runs under SSA Titles III and IX and FUTA; SNAP is federal (food-and-nutrition-act-of-2008).

**Terms.** https://ndlegis.gov/disclaimer and the Century Code landing page, read 2026-10-20: the Century Code text on the site "is the official version"; the disclaimer covers accuracy and privacy only, with no reuse restriction. robots.txt (Drupal defaults) allows `/cencode/`. Verdict: clean. Each subject's `SOURCE-LICENSE.md` records the detail.

**Currency.** The register's 07/01/25 update: all changes approved by the 69th Legislative Assembly (2025 session).

**Format.** The register serves statute text only as chapter PDFs. Texts were converted with poppler `pdftotext -layout` and a scratch script that drops page footers, rejoins paragraphs at section headings and list markers, and renders the rate schedules as `| a | b |` rows. Each text carries an unofficial-version notice; each `.meta.json` has the source URL, retrieval time, hashes and character count. Spot-check the paragraph joins against the PDF before encoding (a wrapped line that begins with a number and a full stop could be read as a new list item).

**Gaps.** No North Dakota Administrative Code (the TANF, AABD and UI rules) was sourced. Chapter 57-38 also contains the corporate income tax and many business credits; only the individual parts matter for this sample.

## Administrative rules deposited 2026-10-20: TANF income rules and fixed amounts

| Subject | Text | What it sets | Characters |
| --- | --- | --- | --- |
| `north-dakota-administrative-code-chapter-75-02-01-2-tanf-income-and-standards` (new; made under ch. 50-09) | N.D. Admin. Code 75-02-01.2-01 (definitions), -22 (asset limits), -42 (whole dollars), -43 (under $10 not paid), -47 (budgeting), -48 (net income test), -50 (earned income considerations), -51 (disregarded income), whole sections; chapter amended effective as late as April 1, 2026 | TANF: asset limits of $9,000 for one person, $15,000 for two, plus $500 for each additional person. Standard employment expense allowance: the greater of $180 or 27% of gross earnings. Time-limited employment incentive: at least 50% of net earnings disregarded in months 1-6, 35% in months 7-9, 25% in months 10-12. Income is matched against the standard of need. No benefit under $10 is paid | 27,150 |

**Amounts that now come from deposited text.** The asset limits, the earned-income allowance and disregards, the grant rounding and the $10 minimum. The **standard of need** by household size, which is the amount actually paid, is set by the department and appears nowhere in chapter 75-02-01.2. It is not sourced.

**Terms.** Same register and disclaimer as the Century Code: https://ndlegis.gov/disclaimer covers accuracy and privacy only. robots.txt (Drupal defaults) allows /information/acdata/. Verdict: **clean**.

**Remaining gaps.**
- The TANF standard of need table, set by the department (e.g. its policy manual), is not sourced.
- The AABD rules (state supplement and basic care, under ch. 50-24.5) are not sourced.
- The UI weekly benefit maximum, computed each year by Job Service North Dakota under ch. 52-06, has no notice sourced.
- Sections 75-02-01.2-56 and -57 (payment computation) were repealed effective April 1, 2026. How the payment is now computed beyond the net income test (section 48) is not stated in the deposited sections.

## Encodings of 2026-10-24: income tax and TANF

Two baselines were encoded from the texts deposited on 2026-10-20. No new text was fetched.

| Encoding | Seat | What it answers | Checks |
|---|---|---|---|
| `north-dakota-century-code-chapter-57-38-income-tax/encodings/baseline-2026-10/` | the individual taxpayer | Residence (s 57-38-01(11)); who must file, by 15 April, paying with the return (ss 57-38-31, -34, -35); reporting a federal change within 90 days (s 57-38-34.4); North Dakota taxable income from federal taxable income (s 57-38-30.3(2)); the tax on the printed schedules and on the commissioner's indexed schedules ((1)(g)); the marriage penalty credit (s 57-38-01.28) | 8 questions, 2 regulative rules, 31 assertions |
| `north-dakota-century-code-chapter-50-09-aid-to-dependent-children/encodings/baseline-2026-10/` (with N.D.A.C. ch. 75-02-01.2) | the TANF applicant | The 60-month limit and hardship exemption (s 50-09-29(1)); absent children; assignment of support rights; the asset limit with one vehicle excluded; the employment expense allowance and the time-limited earned income incentive; the net income test; the grant in whole dollars and the $10 minimum; the fair hearing on appeal | 8 questions, 2 regulative rules, 37 assertions |

**Main findings.**
- The income tax rate schedules printed in s 57-38-30.3(1) are replaced each year by the commissioner's indexed schedules ((1)(g)). Those are not deposited, so the thresholds are an input.
- Chapter 57-38 has no earned income or child credit.
- Chapter 50-09 sets no TANF amounts at all. The rules give the asset limits and the disregards. The standard of need, which decides the grant, is in neither text and is an input.
- Section 50-09-06.1(5) refers to a "benefit cap imposed under section 50-09-29" that the deposited s 50-09-29 does not contain.
