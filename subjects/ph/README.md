# ph/

Reserved for L4 encodings of the law of the **Philippines**, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md).

Opened on 19 October 2026 with a Priority 3 sample on two connected topics: **social security and benefits** and **personal income tax**. Nine Republic Acts are indexed and their text is deposited (sourced), under six subjects. None is encoded yet.

## What was sourced, and why these connect

The set is chosen so that a member of the public could ask: what must I contribute, and what can I receive? How much income tax do I owe? How do the two meet?

| Subject | Acts deposited | What it answers for the individual |
|---|---|---|
| [`national-internal-revenue-code-1997/`](national-internal-revenue-code-1997/) | RA 8424 (1997), RA 10963 TRAIN (2017), RA 12214 CMEPA (2025) | How much income tax do I owe? The Code as enacted, with the two Acts that rewrote the individual income tax: TRAIN (the graduated rates, the schedule for 2023 onwards, the 8% option, the minimum wage earner exemption, the P90,000 exclusion for 13th month pay and other benefits) and CMEPA (final taxes on interest, dividends and other passive income, from 1 July 2025). |
| [`social-security-act-2018/`](social-security-act-2018/) | RA 11199 (2019) | Must I be covered by the SSS, what do I and my employer pay (15% from 2025, monthly salary credit P5,000 to P35,000), and what benefits can I claim (pension, retirement, death, funeral, disability, sickness, maternity, unemployment)? |
| [`universal-health-care-act-2019/`](universal-health-care-act-2019/) | RA 11223 (2019) | Am I a PhilHealth member (every Filipino is), am I a direct or indirect contributor, and what premium do I pay (5% from 2024, income floor P10,000, ceiling P100,000)? |
| [`home-development-mutual-fund-law-2009/`](home-development-mutual-fund-law-2009/) | RA 9679 (2009) | Must I contribute to the Pag-IBIG Fund, how much do I and my employer pay, and when can I withdraw my savings? |
| [`pantawid-pamilyang-pilipino-program-act-2019/`](pantawid-pamilyang-pilipino-program-act-2019/) | RA 11310 (2019) | Does my household qualify for 4Ps conditional cash transfers, on what conditions, and for how much (education grants of at least P300, P500 or P700 per child per month; health and nutrition grant of at least P750 per month)? |
| [`expanded-senior-citizens-act-2010/`](expanded-senior-citizens-act-2010/) | RA 9994 (2010), RA 11916 (2022) | As a senior citizen, what discounts and exemptions do I get (20% discount, VAT exemption, income tax exemption for minimum wage earners), and as an indigent senior, what social pension (at least P1,000 a month under RA 11916)? |

**How they meet.** The tax side and the benefit side cross at several points an encoding will need:

- contributions to the SSS, PhilHealth and the Pag-IBIG Fund are excluded from the employee's gross income (NIRC s.32(B)(7)(f) of RA 8424, not changed by TRAIN or CMEPA), so they come off before the TRAIN rate schedule is applied;
- SSS benefits are exempt from tax (RA 11199 s.16), and the Code excludes benefits received under the SSS law from gross income (NIRC s.32(B)(6)(e), which still names RA 8282, the law RA 11199 replaced);
- the 13th month pay and other benefits exclusion (NIRC s.32(B)(7)(e), P90,000 since TRAIN) sits beside the contribution exclusion;
- minimum wage earners pay no income tax (NIRC s.24(A)(2), with the definition in s.22(HH)), and senior citizens who are minimum wage earners are exempt again under RA 9994;
- whether 4Ps grants and the senior citizens' social pension are income under the Code is not settled by these texts; an encoding should ask, not assume;
- senior citizens and 4Ps households are covered by PhilHealth with their premiums paid by government (RA 9994, RA 11310 s.8, and RA 11223 on indirect contributors).

## Source and terms (checked 2026-10-19)

All nine texts come from the **Supreme Court of the Philippines E-Library** (https://elibrary.judiciary.gov.ph/), an official source, fetched with the User-Agent `legalese-commons-source-fetcher/1.0 (+https://github.com/legalese/commons)` and at least 3 seconds between requests.

- **Law.** Republic Act No. 8293 (Intellectual Property Code), read from https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/2/4371 : s.175 extends no protection to "any official text of a legislative, administrative or legal nature"; s.176.1, "No copyright shall subsist in any work of the Government of the Philippines", and, while it asks for agency approval to exploit government works for profit, "No prior approval or conditions shall be required for the use for any purpose of statutes, rules and regulations". The Acts may be reproduced for any purpose.
- **E-Library.** https://elibrary.judiciary.gov.ph/robots.txt : HTTP 404 (none). https://elibrary.judiciary.gov.ph/aboutus/scelibrary : no terms of use or licence; footer "(c) Supreme Court E-Library 2019", which can cover no more than the site itself. Document pages are public; the "Republic Acts" list is filled by the page's own POST to `/republic_acts/fetch_ra` (with the page's cookie and CSRF token), which was used to look up document numbers. No login.
- **Official Gazette** (https://www.officialgazette.gov.ph/), the preferred source: robots.txt allows the Act pages (it disallows /wp-content, where the signed PDFs sit, and /tag, /author, /cgi-bin, /wp-admin, /wp-includes, /wget/, /httpd/, /i/, /f/, /t/, /c/, /j/; no crawl-delay). Footer: "All content is in the public domain unless otherwise stated." FAQ (https://www.officialgazette.gov.ph/faq/): the online version "provides only a copy of the issuance and does not serve as an official publication." After three Act pages it served a **Cloudflare bot challenge** (HTTP 403, "Just a moment... Enable JavaScript and cookies to continue"); fetching stopped and nothing from it is deposited.
- **Social Security System** (https://www.sss.gov.ph/): robots.txt disallows only /wp-admin/. Footer: "All content is in the public domain unless otherwise stated." But its Terms of Service (https://www.sss.gov.ph/terms-of-service/) say "You must not conduct any systematic or automated data collection activities in relation to My.SSS without SSS' express written consent" and forbid republishing "any portion of My.SSS". **Not fetched** beyond the home and terms pages; the SSS contribution table and circulars are not deposited.
- **Pag-IBIG Fund** (https://www.pagibigfund.gov.ph/): the request for /robots.txt was answered with a **Google reCAPTCHA challenge page**; stopped there, nothing fetched.
- **PhilHealth** (https://www.philhealth.gov.ph/): /robots.txt HTTP 404; nothing further fetched (the premium schedule needed is in RA 11223 itself).
- **Bureau of Internal Revenue** (https://www.bir.gov.ph/): no robots file (the path returns the app shell); footer "Copyright (c) Bureau of Internal Revenue. All Rights Reserved". Its consolidated Tax Code page renders only in a browser, so it was not used.
- **Lawphil** (https://lawphil.net/): unofficial; robots.txt 404; not used.

Each subject's `SOURCE-LICENSE.md` repeats these terms with the sha256 of every download and text.

## Currency

Every text is **as enacted**, not consolidated: later amendments are not applied. The E-Library's search (by Act number in the title, so not exhaustive) on 2026-10-19 showed:

- NIRC: amended many times; for individuals, TRAIN (RA 10963) and CMEPA (RA 12214, approved 2025-05-29, published 2025-06-09) are deposited. **Not deposited**: RA 11976 Ease of Paying Taxes Act (2024; filing, withholding and invoicing), RA 9504 (2008; the first minimum wage earner exemption, rewritten by TRAIN), and the excise, VAT and corporate amendments (RA 11467, RA 11534 CREATE, RA 12253 and others), which do not change an individual's income tax. To read s.24 or s.32 as in force, an encoder must apply RA 10963 and then RA 12214 to RA 8424 by hand.
- RA 11199: RA 11548 (2021) let the President defer the 2021 contribution increase during the COVID-19 state of calamity; spent. The s.4(a)(9) schedule ends with 2025 (15%, MSC P5,000 to P35,000), which is the current rate unless the Commission has adjusted it under s.4(a)(4).
- RA 11223: no amending Act found. Check whether the 2023 premium increase was implemented (it was reported suspended in 2023; 5% applied from 2024).
- RA 9994: RA 10645 (2014, mandatory PhilHealth coverage of all senior citizens) and RA 11350 (2019, National Commission of Senior Citizens) also amend RA 7432 and are not deposited; RA 11916 (social pension P1,000) is.
- RA 9679 and RA 11310: no amending Act found.

## Gaps

- **The current numbers set outside the Acts** are not deposited: the SSS contribution table (SSS Circular 2024-006, from January 2025; SSS terms forbid automated collection), the Pag-IBIG maximum monthly fund salary and contribution rates (HDMF Circular No. 460, from February 2024; site behind reCAPTCHA), the BIR withholding tables (Revenue Regulations under TRAIN; BIR site not machine-readable), any DSWD adjustment of the 4Ps grant levels, and the appropriation that funds the social pension.
- **No consolidated text**: see Currency.
- **Implementing rules and regulations** of RA 11199, RA 11223, RA 9679, RA 11310 and RA 9994 are not deposited.
- **GSIS** (RA 8291, government employees' social insurance) and the **Employees' Compensation** programme (Labor Code Book IV Title II) are outside this sample.
- **Transcription errors.** The E-Library text is transcribed from print, with typographical and OCR slips. Two that affect numbers are flagged at the top of the texts: TRAIN's 2018-2022 schedule shows "P130,000 + 32%" for the P2,000,000 to P8,000,000 bracket (the arithmetic gives P490,000), and RA 11223's premium schedule shows 3.50% for 2023 (generally given as 4.50%). Check both against the signed copies in the Official Gazette before encoding them.
