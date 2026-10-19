# northern-territory/

Northern Territory (Australia) legislation, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md).

The subjects here were laid out on 2026-09-22 for the legislation governing twelve everyday topics. Each was checked against the Northern Territory Legislation (legislation.nt.gov.au); the check is recorded in each subject's `registers/source-bundle/*.meta.json`. No statute text was deposited at that stage. On 2026-10-19 text was deposited for the benefits-and-individual-taxes sample described below; nothing is encoded yet.

**Licence category: conditional.** Reproduction is permitted on the conditions above, but the terms do not expressly grant a right to ADAPT. An L4 encoding that quotes the statute is arguably an adaptation. **Verbatim deposit is within the permission; confirm before quoting it in an encoding** -- a human decision recorded here.

## Topics with no legislation here

- **Pensions/social security**: Commonwealth matter (Social Security Act 1991 (Cth); Superannuation Guarantee (Administration) Act 1992 (Cth)).
- **Personal tax/withholding**: Commonwealth matter: income tax and PAYG withholding are under the Income Tax Assessment Acts and Taxation Administration Act 1953 (Cth). The NT levies no personal income tax; its employer payroll tax is listed under Payroll/wages.
- **Passenger compensation**: Commonwealth matter (Civil Aviation (Carriers' Liability) Act 1959 (Cth); airline consumer protections under the Australian Consumer Law).
- **Work permits/immigration**: Commonwealth matter (Migration Act 1958 (Cth)).
- **Termination/severance**: Partial gap: private-sector unfair dismissal, notice and redundancy pay are Commonwealth (Fair Work Act 2009). The NT is not a referring state because, as a territory, it is covered by the Fair Work Act directly. Only the public-sector Act is listed.
- **Government benefits**: Partial gap: income-support benefits are Commonwealth (Social Security Act 1991). The NT's own benefits (victims of crime assistance, return-to-work and motor accident compensation, the first home owner grant) are sourced in the sample below.

## Sample: territory benefits and individual taxes (sourced 2026-10-19)

A Priority 3 sample for two topics, **social security and benefits** and **personal income tax**, chosen so a member of the public can get determinations from it. Ten instruments now carry deposited text; five were already indexed here and five subjects are new.

### Why this set, and how it connects to the Commonwealth

Personal income tax and the main income-support payments are Commonwealth law, already sourced under `subjects/au/`: `income-tax-assessment-act-1997`, `income-tax-assessment-act-1936`, `income-tax-rates-act-1986`, `medicare-levy-act-1986`, `taxation-administration-act-1953`, `social-security-act-1991`, `social-security-administration-act-1999`, `a-new-tax-system-family-assistance-act-1999` and `veterans-entitlements-act-1986`. The NT levies no income tax and pays no pension. This sample is the territory law a resident meets on top of those Acts:

- **Benefits the Territory pays to an individual**: financial assistance to victims of violent acts; weekly payments and other compensation to injured workers; no-fault benefits after a motor accident; the first home owner grant.
- **Territory taxes that fall on an individual**: stamp duty when buying a home, with its first home owner discount, senior, pensioner and carer concession and principal place of residence rebate. Payroll tax (already indexed here) falls on employers, so it is not part of this sample.

The texts tie to the Commonwealth Acts at specific points:

- The Return to Work Act stops or reduces weekly payments at *pension age*, defined by the age pension age under the Social Security Act 1991 (Cth). The Motor Accidents (Compensation) Act uses the same definition (s 23(1) of the Social Security Act).
- Stamp duty Schedule 2 exempts transfers to a Special Disability Trust as defined in the Social Security Act 1991 (Cth) or the Veterans' Entitlements Act 1986 (Cth), and to some veterans on the rates in that Act. Its trust provisions borrow Income Tax Assessment Act 1997 (Cth) terms.
- The first home owner grant borrows *new residential premises* and GST terms from the A New Tax System (Goods and Services Tax) Act 1999 (Cth), and *permanent resident* from the Migration Act 1958 (Cth).

The texts also tie to each other:

- The Taxation Administration Act 2007 is the procedure for both the grant and stamp duty: applications, assessments, objections, interest and penalties. It is how an individual challenges a decision under either.
- Stamp Duty Act ss 89-90B set the order between the grant and the duty concessions. For example, s 89A(1)(ga) denies the senior, pensioner and carer concession to a buyer who gets the grant, and s 90B stops a buyer taking more than one concession.
- The Victims of Crime Assistance Act deals with injuries that a Return to Work or Motor Accidents (Compensation) claim also covers. Return to Work and Motor Accidents (Compensation) cross-refer in the same way, so someone injured at work on the road, or by a crime at work, needs all three.

### Instruments sourced

| Subject | Reprint | As in force at | Characters | Why it is in the set |
|---|---|---|---|---|
| `victims-of-crime-assistance-act-2006` (new) | REPV014 | 1 July 2025 | 90,616 | Who can claim financial assistance or counselling after a violent act, interim payments, awards and caps |
| `victims-of-crime-assistance-regulations-2007` (new) | REPV014R1 | 25 March 2024 | 50,632 | The standard amounts: compensable violent acts (Sch 1), compensable injuries (Sch 3), loss of earnings |
| `return-to-work-act-1986` | REPR050 | 25 March 2024 | 339,640 | Workers compensation: who is a worker, weekly payments and their step-downs, medical costs, lump sums, death benefits |
| `return-to-work-regulations-1986` (new) | REPR050R2 | 1 July 2024 | 53,755 | Prescribed amounts and lists: funeral benefit, prescribed diseases, catastrophic injury, late weekly payments |
| `motor-accidents-compensation-act-1979` | REPM022 | 31 May 2019 | 100,851 | No-fault motor accident benefits for Territory residents: loss of earning capacity, impairment, death, medical and care |
| `motor-accidents-compensation-regulations-1984` (new) | REPM022R1 | 28 August 2026 | 40,089 | Alcohol exclusion and reduction, impairment guides, attendant care and building alteration benefits, commutation |
| `first-home-owner-grant-act-2000` | REPF039 | 1 July 2026 | 67,603 | Eligibility for the grant and its amount by commencement date (s 18) |
| `first-home-owner-grant-regulations-2000` (new) | REPF039R1 | 1 July 2009 | 7,217 | The non-conforming interests in land that count for the grant |
| `stamp-duty-act-1978` | REPS013 | 1 July 2025 | 291,096 | Duty on a home purchase (Sch 1), first home owner discount, senior, pensioner and carer concession, principal place of residence rebate, exemptions (Sch 2) |
| `taxation-administration-act-2007` | REPT039 | 1 July 2024 | 144,646 | Procedure for the grant and the duty: assessments, objections, appeals, interest, penalties |

Total 1,186,145 characters. Each text is at `<subject>/registers/source-bundle/<stem>.txt`. Its `.meta.json` records the landing page, the Word download URL and filename, the reprint, the as-in-force date, the retrieval time, the sha256 of the download and of the text, the character count and the converter. "As in force at" is the date on the reprint's cover, which is the latest reprint the register published on 2026-10-19.

### Terms read before fetching

- **Copyright policy**: https://legislation.nt.gov.au/en/Footer/Terms-of-Use, read 2026-10-19 17:03 UTC. Key lines: "Copyright in Northern Territory legislation is owned by the Northern Territory". Also: "The Northern Territory grants permission to any person to publish or deal with any legislation of the Northern Territory in accordance with the following conditions". The conditions are that the publication must not indicate that it is an official version, the NT arms must not be used, and the material must be "accurately reproduced in a context that does not mislead". The NT may revoke, vary or withdraw the permission on reasonable notice. The policy has been in effect since 8 October 1996, and "Legislation" includes regulations.
- **robots.txt**: https://legislation.nt.gov.au/robots.txt, read 2026-10-19 17:03 UTC (Last-Modified 7 December 2016). It disallows `/` only for `SiteCheck-sitecrawl by Siteimprove.com` and `LinkCheck by Siteimprove.com`. It has no rule for other agents and no Crawl-delay.
- **Access**: User-Agent `legalese-commons-source-fetcher/1.0 (+https://github.com/legalese/commons)` on every request, at least 3 s between requests. There were 23 requests in all (robots.txt, the terms page, 10 landing pages, the Acts-by-title list, 10 Word reprints), and every one returned 200. No block, challenge or rate limit was met.
- **What this permits**: reproducing the text verbatim is permitted, so each text opens with an unofficial-copy notice and no arms are used. The policy says nothing expressly about *adapting* the text, and the question recorded above stands for encodings that quote it.

### Conversion

The register offers each reprint as a PDF and as a Word 97-2003 `.doc`; the `.doc` was used. Word (by COM, macros force-disabled, read-only) saved each file as `.docx`, and python-docx then walked the body paragraphs and tables in order. Headings and the Part, Division, section, subsection and paragraph numbers are kept as typed in the reprint. Indentation follows the reprint's paragraph styles. Each table row is shown as `| a | b |`, with paragraphs inside one cell joined by ` / ` so that amounts stay in the same row as their descriptions. Running headers, footers and page numbers are dropped. Word counts were checked against an independent `antiword` conversion of the same files and agree, apart from one word in the Motor Accidents (Compensation) Act.

### Currency and gaps

- **Reprints lag amendments.** Four texts are more than a year old: the Motor Accidents (Compensation) Act reprint (31 May 2019), the Return to Work Act and Victims of Crime Assistance Regulations reprints (25 March 2024), and the Taxation Administration Act reprint (1 July 2024). An amendment that commenced after a reprint's date is not in it. Check each against the register's history listing before relying on a number.
- **The concession card scheme is not in statute.** Stamp Duty Act s 89A relies on the *NT Pensioner and Carer Concession Card* and the *Northern Territory Concession Scheme Card*. No NT Act on the register's Acts-by-title list (385 titles, fetched 2026-10-19) sets up a concession scheme, so the card scheme is administrative and its eligibility rules are not sourced here.
- **Not sourced**: the Motor Accidents (Compensation) Commission Act 2014 (the insurer's machinery) and the Compensation (Fatal Injuries) Act 1974 (a common-law damages claim, not a benefit). The NT Rates Act 1971 and local government rates were also left out: they fall on owners of land, but their concessions are council or administrative matters.
- **Indexed amounts**: Return to Work weekly payments and several Motor Accidents (Compensation) benefits are indexed to average weekly earnings or CPI by figures published outside these texts (by the Australian Statistician and in Gazette notices). An encoding has to take those figures as inputs.
- Nothing in this sample is encoded yet.
