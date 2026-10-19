# north-dakota/

North Dakota (US state) legislation, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md).

The subjects here were laid out on 2026-09-23 for the legislation governing twelve everyday topics. Each was checked against the North Dakota Legislative Branch - North Dakota Century Code (North Dakota Legislative Council); the check is recorded in each subject's `registers/source-bundle/*.meta.json`. No statute text had been deposited when they were laid out; see the 2026-10-20 sample below. Nothing is encoded yet.

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
