# ng/

Federal legislation of Nigeria, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md).

The subjects here were laid out on 2026-10-19 as a connected sample on two topics, **personal income tax** and **social security and benefits**, chosen so that a member of the public could get useful answers to three questions: how much income tax do I owe; what pension, housing-fund, health-insurance and injury-compensation contributions or benefits apply to me, and how much; and how the two interact.
Nothing is encoded yet.

## What was sourced

| Subject | Instrument | Text | Why it is here |
|---|---|---|---|
| [`nigeria-tax-act-2025`](nigeria-tax-act-2025/) | Nigeria Tax Act, 2025 (Act No. 7 of 2025) | deposited (440,928 chars) | Personal income tax from 1 January 2026: chargeable income, eligible deductions (s. 30), individual rates (Fourth Schedule), exemptions (s. 162). Repeals the Personal Income Tax Act, Cap. P8 (s. 195(g)). |
| [`nigeria-tax-administration-act-2025`](nigeria-tax-administration-act-2025/) | Nigeria Tax Administration Act, 2025 (Act No. 5 of 2025) | deposited (191,197 chars) | How the tax is collected from the individual: Tax ID, returns, PAYE and deduction at source, assessments, penalties, refunds, objections and appeals. |
| [`pension-reform-act-2014`](pension-reform-act-2014/) | Pension Reform Act, 2014 (Act No. 4 of 2014) | deposited, **OCR quality** (138,696 chars) | Who is in the contributory pension scheme (s. 2), the rates (s. 4: at least 10% employer, 8% employee), retirement benefits and withdrawals, tax exemption (s. 10). |
| [`national-housing-fund-act`](national-housing-fund-act/) | National Housing Fund Act, Cap. N45, LFN 2004 | deposited (22,839 chars) | The 2.5% of basic monthly salary contribution (s. 4), employer deduction (s. 9), refund on retirement (s. 17), tax exemption (s. 23). |
| [`national-health-insurance-authority-act-2022`](national-health-insurance-authority-act-2022/) | National Health Insurance Authority Act, 2022 (Act No. 17 of 2022) | **indexed only** (scan without text layer) | Mandatory health insurance (s. 14) and the Vulnerable Group Fund (ss. 25-27). |
| [`employees-compensation-act-2010`](employees-compensation-act-2010/) | Employees' Compensation Act, 2010 (Act No. 13 of 2010) | **indexed only** (no official copy reachable) | Compensation for workplace injury, disease and death. |

Counts: 4 texts deposited; 2 indexed without text (1 downloaded but scanned, 1 not obtainable from an official host). 793,660 characters deposited in all, including the notice at the top of each text.

## How they connect

- **Income tax is computed after the social-security contributions.** Section 30(2)(a) of the Nigeria Tax Act lists as *eligible deductions* the individual's contributions under the National Housing Fund, the National Health Insurance Scheme and the Pension Reform Act, alongside mortgage interest on an owner-occupied home and life-assurance premiums. The chargeable income those deductions produce is taxed at the Fourth Schedule rates.
- **The benefit side is tax-exempt.** Pension funds and assets under the Pension Reform Act are exempt (Nigeria Tax Act s. 162; Pension Reform Act s. 10), as are NHF contributions and refunds (NHF Act s. 23), and employment income of national minimum wage or less (Nigeria Tax Act s. 162(1)(t)).
- **The employer is the collecting point for all of them.** PAYE deduction at source (Nigeria Tax Administration Act), pension remittance (Pension Reform Act s. 11), NHF deduction (NHF Act s. 9) and, for injury compensation, the employer's contribution to the Employees' Compensation Fund.

## The numbers a person needs, and where they are set

| Number | Value in the deposited text | Where |
|---|---|---|
| Individual income tax bands (2026) | first N800,000 at 0%; next N2,200,000 at 15%; next N9,000,000 at 18%; next N13,000,000 at 21%; next N25,000,000 at 23%; above N50,000,000 at 25% | Nigeria Tax Act, Fourth Schedule |
| Pension contribution | at least 10% (employer) and 8% (employee) of monthly emoluments; 20% where the employer bears it all; group life cover of at least 3 times annual total emolument | Pension Reform Act s. 4 |
| Pension scheme coverage (private sector) | organisations with 15 or more employees; others may join | Pension Reform Act s. 2 |
| NHF contribution | 2.5% of basic monthly salary, for a worker earning N3,000 a year or more; 4% interest on contributions | NHF Act s. 4 |
| National minimum wage (threshold for the s. 162 exemption) | **not sourced**; the Nigeria Tax Act defines it by reference to the National Minimum Wage Act, Cap. N61, as amended | gap, see below |

## Terms read before fetching

All requests used the User-Agent `legalese-commons-source-fetcher/1.0 (+https://github.com/legalese/commons)`, honoured robots.txt, and were spaced at least 3 seconds apart (30 seconds on pencom.gov.ng, per its Crawl-delay). Read on 2026-10-19:

- **Copyright Act, 2022, s. 3(b)** (gazette copy at https://www.copyright.gov.ng/CopyrightAct/CopyrightAct2023FinalPublication1.pdf; robots.txt at https://www.copyright.gov.ng/robots.txt does not disallow it): "official texts of a legislative or administrative nature as well as any official translations, except their compilations" are not eligible for copyright. **This is the basis for every deposit here.** Only the words of each instrument are deposited; no host's pages, arrangement or commentary.
- **tat.gov.ng** (Tax Appeal Tribunal): robots.txt 404 (none); no terms or re-use page; footer "(c) Tax Appeal Tribunal 2026". Source of both 2025 tax Acts.
- **pencom.gov.ng** (National Pension Commission): robots.txt `Crawl-delay: 30`, nothing disallowed; no terms page, only privacy notices that say nothing about re-use. Source of the Pension Reform Act.
- **fmbn.gov.ng** (Federal Mortgage Bank of Nigeria): robots.txt 404; Terms of Use clause 6: "Copyright in the pages and in the screens displaying the pages, and in the information and material therein and arrangement is owned by the bank." **Flagged** (see below). Source of the NHF Act.
- **nhia.gov.ng** (National Health Insurance Authority): robots.txt disallows only WooCommerce and admin paths; no terms page; footer "Copyright NATIONAL HEALTH INSURANCE AUTHORITY. All rights reserved".
- **nsitf.gov.ng** (Nigeria Social Insurance Trust Fund): robots.txt 404; the footer's "Terms" link points to the home page, so no terms are published.
- **nrs.gov.ng** (Nigeria Revenue Service, formerly FIRS): robots.txt read (disallows `/api/`, `/admin/`, `/_next/`, `/static/` and similar). After one page loaded, the next requests were redirected to a **Radware bot challenge**; the site was abandoned there and nothing was taken from it. www.firs.gov.ng did not answer.
- Checked for robots.txt but not used: www.nass.gov.ng (returns its home page for /robots.txt, i.e. no file), placng.org and lawsofnigeria.placng.org (404). PLAC's copies are unofficial and were not used. No Federal Ministry of Justice laws portal was used.

## Currency

- Nigeria Tax Act, 2025: gazetted 26 June 2025, in force 1 January 2026; the text is as enacted. It governs personal income tax for the 2026 year of assessment (1 January to 31 December).
- Nigeria Tax Administration Act, 2025: gazetted 26 June 2025; commencement printed as 26 June 2025; as enacted.
- Pension Reform Act, 2014: as enacted (authenticated copy assented in 2014; assent date illegible in the scan); later amendments not checked.
- National Housing Fund Act: LFN 2004 revision; later amendments not checked.
- National Health Insurance Authority Act, 2022: gazetted 24 May 2022 (not converted).

## Gaps and flags

1. **Disputed versions of the 2025 tax Acts.** In December 2025 members of the House of Representatives alleged that the gazetted Acts differ from the Bills passed; the House released Certified True Copies in January 2026 and an ad hoc committee is examining the matter. The NRS applies the gazetted text, which is what is deposited. The Certified True Copies were found only on news and law-firm sites and were not used.
2. **Pension Reform Act text is OCR.** PenCom's PDF is a scan with a hidden OCR layer; the text was recovered from that layer and carries its errors (240 unreadable characters marked `[?]`, broken words, marginal notes interleaved). Proof-read before encoding.
3. **NHIA Act not converted**: scan without a text layer; needs OCR.
4. **Employees' Compensation Act not sourced**: NSITF's new site publishes no Acts (`/api/public/acts` returns an empty list) and its old PDF link is 404.
5. **National Minimum Wage Act** (Cap. N61, as amended in 2024) not sourced: no official host found. Needed for the minimum-wage exemption in Nigeria Tax Act s. 162(1)(t).
6. **FMBN copyright claim** over its site material: the NHF Act's words are deposited in reliance on Copyright Act s. 3(b); FMBN's page material is not reproduced.
7. Not sought in this pass: regulations and guidelines that set operational numbers (NRS PAYE guidance, PenCom regulations and circulars, NHIA operational guidelines and contribution rates, NSITF rates); State-level administration of personal income tax (the NTAA allocates jurisdiction between the federal and State tax authorities, s. 3; State laws and State IRS guidance were not sought); the Personal Income Tax Act, Cap. P8, which applies to years of assessment before 2026.
