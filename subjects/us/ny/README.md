# new-york/

New York (US state) legislation, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md).

The subjects here were laid out on 2026-09-22 for the legislation governing twelve everyday topics. Each was checked against the New York State Senate - Open Legislation / Consolidated Laws of New York; the check is recorded in each subject's `registers/source-bundle/*.meta.json`. Statute text was deposited and two baselines encoded on 2026-10-24; see the section below.

**Licence category: open.** Statute text may be deposited and quoted in an encoding, subject to the attribution above.

## Topics with no legislation here

- **Passenger compensation**: Airline passenger rights are federal: the Airline Deregulation Act preempts them and DOT rules (14 CFR Parts 250, 259, 260) govern. New York's 2008 Passenger Bill of Rights (GBL Art. 14-C) was struck down as preempted (Air Transport Ass'n v. Cuomo, 2d Cir. 2008). No operative state Act exists.
- **Customs/duties**: This is a federal matter (U.S. Const. art. I §10; 19 U.S.C.). States levy no customs duties.
- **Work permits/immigration**: This is a federal matter (Immigration and Nationality Act, 8 U.S.C.). New York does not legislate work authorisation.

## Tax and benefits sample (sourced and encoded 2026-10-24)

Text was deposited from NYSenate.gov Open Legislation (CC BY-NC-ND 3.0 US with the CC+ waiver, which allows derivative works not related to political fundraising; terms at https://www.nysenate.gov/policies-and-waivers, read 2026-10-24), one section page each, with the honest client name. The Open Legislation API host (legislation.nysenate.gov) timed out and was not used; a Python client was refused with HTTP 403 by the site's Cloudflare front end, while `curl` with the same User-Agent was served (recorded in each `SOURCE-LICENSE.md`).

| Subject | Deposited | Encoding |
|---|---|---|
| `tax-law-article-22-personal-income-tax` | Tax Law ss 601, 601-a, 605, 606, 611, 612, 613, 614, 616, 651, 652 (690,790 characters) | `encodings/baseline-2026-10/`: the resident individual taxpayer's seat for tax years 2026 and 2027. It covers residence, the duty to file and pay, New York AGI, the deduction and exemptions, the s 601 tables, the household credit, the Empire State child credit and the New York EIC. 14 questions, 3 regulative rules, 75 assertions |
| `social-services-law-article-5-assistance-and-care` | Social Services Law ss 131, 131-a, 131-n, 158, 159, 343, 344, 349, 350 (83,356 characters) | `encodings/baseline-2026-10/`: the family assistance (TANF) applicant's seat. It covers who it is given to, the minor parent rule, the 60-month limit, the voluntary quit rule, exempt resources, the standard of need, the grant schedules, the earned income disregards and the monthly grant. 11 questions, 3 regulative rules, 51 assertions |

**How they connect.** The tax starts from federal AGI and borrows the federal EIC (Tax Law ss 612(a), 606(d)). Both are inputs that the federal IRC encoding could supply. The New York EIC refund is disregarded for family assistance (Social Services Law s 131-a(8)(a)(viii), s 131-n(1)). Federally taxable social security is subtracted in full (s 612(c)(3-c)).

**Gaps.** The amounts set by regulation or by the Tax Department are not in the deposited text and are inputs: the s 614(f) adjusted standard deductions, the 18 NYCRR shelter and fuel allowances, and the June-adjusted earned income disregard percentage. Not covered: nonresidents, the recapture tax above $100,000 of New York AGI, and safety net assistance. The resource exemptions of s 131-n(1) are marked to expire on 22 August 2027.
