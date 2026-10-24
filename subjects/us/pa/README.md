# pennsylvania/

Pennsylvania (US state) legislation, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../../README.md).

This folder was opened on 2026-10-24 for "tax and benefits" (docs/ENCODING-GUIDE.md section 6): personal income tax, and social security and benefits.

## Source

The Pennsylvania General Assembly's own site, **palegis.us** (Legislative Data Processing Center), publishes the Unconsolidated Statutes (the Acts not yet in Pennsylvania Consolidated Statutes) as whole-Act HTML. Both Acts below are unconsolidated.

- **Terms** (read 2026-10-24): https://www.palegis.us/legal is a disclaimer ("made available as an information service only ... not intended to replace official versions") and a DMCA notice. Nothing restricts reuse. Statute text is not copyrightable (*Georgia v. Public.Resource.Org*, 590 U.S. 255 (2020)). **Licence category: open.**
- **robots.txt**: has rules only for one accessibility scanner. Nothing applies to `/statutes/`.
- **Access**: plain HTTPS GET with the User-Agent `legalese-commons-source-fetcher/1.0 (+https://github.com/legalese/commons)`, at least 3 seconds apart. One request timed out on the first try and succeeded on the second. No challenge was met. The older host `www.legis.state.pa.us` did not respond (connection timeout), and it was not needed.

## Subjects

| subject | deposited | encoded |
| --- | --- | --- |
| [`tax-reform-code-of-1971`](tax-reform-code-of-1971) | the whole Act (Act of Mar. 4, 1971, P.L. 6, No. 2), as served 2026-10-24 | [`baseline-2026-10`](tax-reform-code-of-1971/encodings/baseline-2026-10): Article III personal income tax from the taxpayer's seat. Covers residence, the duty to file and pay, the 3.07% tax on the eight classes, the other-state credit, Tax Forgiveness (s 304) and the balance due |
| [`human-services-code`](human-services-code) | the whole Act (Act of Jun. 13, 1967, P.L. 31, No. 21, formerly the Public Welfare Code), as served 2026-10-24 | [`baseline-2026-10`](human-services-code/encodings/baseline-2026-10): Article IV cash assistance from the applicant's and recipient's seat. Covers TANF class, State supplement to SSI, the end of general assistance cash, the bars, resources, whose income counts, RESET work requirements and disqualification, notice and appeal. The grant amount is not computed, because the payment standards are in regulations |

## Not sourced

- **The Pennsylvania Code (regulations)**, at pacodeandbulletin.gov, which holds 55 Pa. Code ch. 175 and the TANF payment standards. Its robots.txt (read 2026-10-24) ends with `User-agent: *` / `Disallow: /`, so nothing was fetched. Its terms say "No part of the information on this website may be reproduced for profit or sold for profit", which would otherwise be acceptable as non-commercial.

## Findings worth knowing

- Pennsylvania's tax does not start from federal AGI. It taxes eight classes of income at one rate, with no personal exemption, no standard deduction and no filing threshold. The only low-income relief in the text is Tax Forgiveness (s 304).
- No state earned income tax credit or child credit appears in the Tax Reform Code as served on 2026-10-24 (see the encoding's NOTES.md, finding 11).
- General assistance cash ended on 1 August 2019 (Human Services Code s 403.2(a)). TANF cash assistance and the State supplement to SSI remain.
