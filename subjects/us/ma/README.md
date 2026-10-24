# massachusetts/

Massachusetts (US state) law, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md). Folder opened on 2026-10-24 for the tax and benefits sample.

## Tax and benefits sample (2026-10-24)

| Subject | Deposited | Encoding |
|---|---|---|
| [`code-of-massachusetts-regulations-106-cmr-704-tafdc-financial-eligibility`](code-of-massachusetts-regulations-106-cmr-704-tafdc-financial-eligibility) | 106 CMR 704.000 (the whole chapter: TAFDC and EAEDC financial eligibility), from the Department of Transitional Assistance's official PDF on Mass.gov; and the TAFDC Table of Need and Payment Standards that 704.410 and 704.420 say the Department posts | [`baseline-2026-10`](code-of-massachusetts-regulations-106-cmr-704-tafdc-financial-eligibility/encodings/baseline-2026-10): the applicant's seat. Need and Payment Standards, the income test, the work-related-expense and dependent care deductions, the 50% and 100% earned income disregards, the monthly grant, and the ten-day duty to report a change in deemed income (regulative). 4 questions, 22 assertions. |

**Terms (Mass.gov).** The Terms of Use (read 2026-10-24) say "all laws and regulations are public record" and that such public record "can be copied and used for any purpose"; other Mass.gov content is Commonwealth copyright, fair use only. Only regulation text was deposited. Details in the subject's `SOURCE-LICENSE.md`.

**Main findings** (in the encoding's `NOTES.md`): Step 7 of 704.500(A) states no grant when the result equals the Payment Standard, which is the case of a family with no countable income; the income test cites 704.400 and 704.405, which do not exist; the address the regulation gives for the posted figures answers 404; a cross-reference in 704.275(B)(1) would, read literally, deny the dependent care deduction to every working client.

## Not reached: the statutes, and personal income tax

**malegislature.gov did not answer.** The General Court's site is the only official publisher of the General Laws. On 2026-10-24 four requests for https://malegislature.gov/robots.txt, spread between about 02:30 and 03:19 UTC (from the commons fetcher and from curl, both with the User-Agent `legalese-commons-source-fetcher/1.0 (+https://github.com/legalese/commons)`) each timed out without a connection after about 21 seconds. A site that hangs is treated as a no: no mirror, other identity or third-party copy was tried. So:

- **Personal income tax (M.G.L. c. 62)** is neither indexed nor sourced. Massachusetts taxes wage income (c. 62, s 4; the 4% surtax on income above $1 million under art. 44 of the Amendments to the Constitution, as amended in 2022: unverified (general knowledge)). The Department of Revenue's guides on Mass.gov are Commonwealth copyright (fair use only under the Terms of Use) and are not law, so nothing was taken from them. The tax regulations (830 CMR 62) are on Mass.gov and could be deposited, but without c. 62 itself they cannot give a person their tax; left for a pass when malegislature.gov answers.
- **M.G.L. c. 118 (TAFDC)** and c. 18 s 10 (the regulation's authority) are not deposited; the TAFDC encoding rests on the regulation.

**To do when the site answers:** deposit c. 62 (with s 6 credits and the c. 62C filing duties) and c. 118, then encode c. 62 for the resident taxpayer; deposit 106 CMR 701, 703 and 705 for the rest of TAFDC.
