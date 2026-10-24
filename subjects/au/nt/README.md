# northern-territory/

Northern Territory (Australia) legislation, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md).

The subjects here were laid out on 2026-09-22 for the legislation governing twelve everyday topics. Each was checked against the Northern Territory Legislation (legislation.nt.gov.au); the check is recorded in each subject's `registers/source-bundle/*.meta.json`. No statute text was deposited at that stage. On 2026-10-19 text was deposited for the benefits-and-individual-taxes sample described below; nothing is encoded yet.

**Licence category: conditional.** Reproduction is permitted on the conditions above, but the terms do not expressly grant a right to ADAPT. An L4 encoding that quotes the statute is arguably an adaptation. **Licence ruling, Michael, 24 Oct 2026:** the NT terms permit reproduction but are silent on adaptation; as for Canada, the texts may be quoted in L4 encodings in Commons, keeping the NT attribution and the unofficial-copy notice.

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
- **Territory taxes that fall on an individual**: stamp duty when buying a home, with its first home owner discount, senior, pensioner and carer concession and principal place of residence rebate. Payroll tax (already indexed here) falls on employers, so it is not part of this sample. The NT levies no land tax, so there is no land tax and no principal place of residence exemption to source.

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
- **What this permits**: reproducing the text verbatim is permitted, so each text opens with an unofficial-copy notice and no arms are used. The policy says nothing expressly about *adapting* the text. Licence ruling, Michael, 24 Oct 2026: as for Canada, the texts may be quoted in L4 encodings in Commons, keeping the NT attribution and the unofficial-copy notice.

### Conversion

The register offers each reprint as a PDF and as a Word 97-2003 `.doc`; the `.doc` was used. Word (by COM, macros force-disabled, read-only) saved each file as `.docx`, and python-docx then walked the body paragraphs and tables in order. Headings and the Part, Division, section, subsection and paragraph numbers are kept as typed in the reprint. Indentation follows the reprint's paragraph styles. Each table row is shown as `| a | b |`, with paragraphs inside one cell joined by ` / ` so that amounts stay in the same row as their descriptions. Running headers, footers and page numbers are dropped. Word counts were checked against an independent `antiword` conversion of the same files and agree, apart from one word in the Motor Accidents (Compensation) Act.

### Currency and gaps

- **Reprints lag amendments.** Four texts are more than a year old: the Motor Accidents (Compensation) Act reprint (31 May 2019), the Return to Work Act and Victims of Crime Assistance Regulations reprints (25 March 2024), and the Taxation Administration Act reprint (1 July 2024). An amendment that commenced after a reprint's date is not in it. Check each against the register's history listing before relying on a number.
- **The concession card scheme is not in statute.** Stamp Duty Act s 89A relies on the *NT Pensioner and Carer Concession Card* and the *Northern Territory Concession Scheme Card*. No NT Act on the register's Acts-by-title list (385 titles, fetched 2026-10-19) sets up a concession scheme, so the card scheme is administrative and its eligibility rules are not sourced here.
- **Not sourced**: the Motor Accidents (Compensation) Commission Act 2014 (the insurer's machinery) and the Compensation (Fatal Injuries) Act 1974 (a common-law damages claim, not a benefit). The NT Rates Act 1971 and local government rates were also left out: they fall on owners of land, but their concessions are council or administrative matters.
- **Indexed amounts**: Return to Work weekly payments and several Motor Accidents (Compensation) benefits are indexed to average weekly earnings or CPI by figures published outside these texts (by the Australian Statistician and in Gazette notices). An encoding has to take those figures as inputs.
- Nothing in this sample is encoded yet.

## Encodings (2026-10-24)

The five Acts of the sample now each have a baseline encoding at `<subject>/encodings/baseline-2026-10/`. The other five instruments are brought into these encodings rather than encoded on their own: each set of regulations into its Act's encoding, and the Taxation Administration Act 2007 into the Stamp Duty Act encoding (`taa-procedure.l4`), which encodes objections and appeals for both duty and first home owner grant decisions.

Each encoding is a seat-neutral core in the Act's own actors and terms, with the text's duties and deadlines as regulative rules, and one or more seat layers that ask the individual's questions and restate no rule. Each was checked with the stable `l4` 1.6.98 (`JL4_LIBRARY_PATH` unset): 0 errors, 0 warnings, every assertion satisfied. Each was then reviewed by an independent verifier and corrected the same day; the corrections are recorded in its `NOTES.md`. There was no pipeline, coverage table or human gate. Not for public use as advice.

| Subject | Encoding | Seats | Questions | Regulative rules | Assertions | What a resident would most want to know |
|---|---|---|---|---|---|---|
| Stamp duty on a home or a car (Stamp Duty Act 1978, with the Taxation Administration Act 2007) | [`stamp-duty-act-1978/encodings/baseline-2026-10/`](stamp-duty-act-1978/encodings/baseline-2026-10/) | the buyer and taxpayer: the conveyee of a home, or the person registering a motor vehicle | 39 | 12 | 299 / 299 | None of the Part 5 Division 2 home concessions applies to a home bought now: s 88A, or their own dates, closed them all to conveyances first executed after 30 June 2021 (a reading; finding 2). The live relief is s 90D: a new home bought with its land from a building contractor, under a conveyance first executed from 1 July 2022 to 30 June 2027, is exempt from the whole duty, with no value cap and no first-home condition (finding 4). |
| First home owner grant (First Home Owner Grant Act 2000, with its Regulations) | [`first-home-owner-grant-act-2000/encodings/baseline-2026-10/`](first-home-owner-grant-act-2000/encodings/baseline-2026-10/) | the first home buyer applying, with their spouse or de facto partner | 21 | 4 | 174 / 174 | The grant is $50,000 for a transaction that commences before 1 October 2027 (for a new home from 1 October 2024, for every eligible transaction from 1 October 2025), and $10,000 after that. Since 1 October 2025 an established home does not qualify (s 18(3D)-(3F), s 13(1)(a); findings 1, 2). The buyer must move in within 12 months of completion and, for a transaction that commences from 1 October 2024 to before 1 October 2027, live there at least 12 months, not 6 (s 12(2); finding 4). |
| Workers' compensation (Return to Work Act 1986, with its Regulations) | [`return-to-work-act-1986/encodings/baseline-2026-10/`](return-to-work-act-1986/encodings/baseline-2026-10/) | the injured worker (on a death, the dependants and the person who pays for the funeral); the employer, read with its insurer | 63 (40 worker, 23 employer) | 18 | 380 / 380 | An employer that does not decide a claim within 10 working days is deemed to have accepted liability (ss 85(1), 87). Weekly payments are then owed within 3 working days, a reading (finding 12). Dismissing a worker incapacitated by the injury within 6 months of it is an offence of up to 200 penalty units, unless for serious misconduct (s 65C; finding 17). |
| Motor accident benefits (Motor Accidents (Compensation) Act 1979, with its Regulations) | [`motor-accidents-compensation-act-1979/encodings/baseline-2026-10/`](motor-accidents-compensation-act-1979/encodings/baseline-2026-10/) | the person injured (the eligible person, then the claimant); on a death, the spouse, dependent children and parents, and the person who pays for the funeral | 37 (24 injured, 13 survivors) | 5 | 278 / 278 | Weekly compensation has no step-down. It runs to pension age if the accident was more than 2 years before it, and otherwise for 104 weeks (s 13(5)(a); finding 21). A driver over the alcohol limit loses weekly compensation and the impairment lump sum (that the alcohol contributed is presumed, reg 4A), but a passenger over the limit does not. If the driver dies, the Commission may only reduce the family's benefits, and never the funeral benefit (ss 9, 20A; finding 5). |
| Victims of crime assistance (Victims of Crime Assistance Act 2006, with its Regulations) | [`victims-of-crime-assistance-act-2006/encodings/baseline-2026-10/`](victims-of-crime-assistance-act-2006/encodings/baseline-2026-10/) | the victim (primary, secondary, family or related); the person who paid for a victim's funeral; the person on whom the victims levy is imposed | 35 (24 victim, 8 funeral, 3 levy) | 6 | 286 / 286 | There is no interim payment or award for an injury that motor accident benefits or Return to Work compensation covers, whether or not a claim was made. This reaches secondary and family victims too, but counselling stays open (ss 17, 18; findings 9, 10). A levy of 40 revenue units comes with an infringement notice (reg 26 lists exceptions), for a child as for an adult, and a part payment goes to the levy first (s 61(6), (8); findings 27, 30). |

In all: 195 questions, 45 regulative rules, 1,417 assertions written and satisfied.

**The NT levies no land tax.** A home buyer here meets only stamp duty and the first home owner grant. Unlike Western Australia (`../wa/land-tax-assessment-act-2002/encodings/baseline-2026-10/`), there is no land tax and no principal place of residence exemption to encode. Council rates and their concessions are not in statute here (see Not sourced, above).

### Still inputs, because they are not deposited

- **Figures published outside the texts:**
  - average weekly earnings, the Australian Statistician's NT full-time adult ordinary time earnings (Return to Work s 3(1); Motor Accidents s 4; Victims of Crime reg 23(3), less a notional income tax deduction the Regulations do not describe);
  - the Motor Accidents (Compensation) Commission's maximum weekly amount for each half-year (s 13(2)(a)), and the CPI figures for the indexed caps (reg 3);
  - the market interest rate for each financial year (Taxation Administration Act s 35(2)), for interest on unpaid duty and on a grant to be repaid;
  - the Supreme Court judgment-debt rate, for late weekly payments (Return to Work reg 14);
  - the value of a penalty unit (Penalty Units Act 2009), so fines are given in penalty units, and the value of a revenue unit, for the victims levy (s 61).
- **Formulas lost in conversion.** The deposits were not altered. Each formula needs a `.formulas.md` sidecar transcribed from the authorised PDF reprint.
  - Return to Work s 65(3A) (indexing normal weekly earnings) and s 89(1) (interest on late weekly payments): both results are inputs.
  - Motor Accidents s 13(3) (the weekly amount): an input, bounded by the maximum weekly amount.
  - Stamp Duty Schedule 1 cl 1(2)(a) lost a superscript. It is read as V squared, checked against the meeting point of the scale, and is not an input.
- **Regulations and other Acts not deposited:**
  - the Stamp Duty and Taxation Administration Regulations. The encoding uses the Act's own $650,000 threshold amount and the s 88(1) fallback for the first home owner discount, so a prescribed figure would change the answers;
  - the Interpretation Act 1978 (working days, business days, how periods are counted) and the Territory's public holidays, which are inputs;
  - the NTCAT Act's time for applying for review of a victims of crime decision, an input;
  - the Traffic Regulations 1999 reg 19(2) (Motor Accidents s 31A), an input, and the Age of Majority Act 1974, whose age is fixed at 18;
  - the NT concession card scheme (Stamp Duty s 89A), which is administrative: holding a card is an input.
- **Earlier texts.** Where only an earlier text would answer, the encodings say `not covered` (or `outside this encoding`). This covers conveyances first executed before 1 July 2017 (Stamp Duty Schedule 1), grant transactions that commenced before 1 January 2010, and motor accidents before 31 May 2019 for weekly compensation or before 1 July 2014 for the Part 3 exclusions and reductions.

### Commonwealth encodings linked

Cross-folder IMPORT does not work, so each link is recorded in the encoding's `NOTES.md`, not in code.

| Encoding | Commonwealth encodings it links to |
|---|---|
| Stamp Duty Act | [Social Security Act 1991](../social-security-act-1991/encodings/baseline-2026-10/): Special Disability Trust (Schedule 2 item 6(e)). [Veterans' Entitlements Act 1986](../veterans-entitlements-act-1986/encodings/baseline-2026-10/): the s 22(4) and s 24(4) pension rates, for the vehicle exemption (item 23(k)). [A New Tax System (Goods and Services Tax) Act 1999](../a-new-tax-system-goods-and-services-tax-act-1999/encodings/baseline-2026-10/): new residential premises (s 40-75(1)(b)), asked here as a fact. [Family Law Act 1975](../family-law-act-1975/encodings/baseline-2026-10/): orders and binding financial agreements, for relationship breakdown (s 91). |
| First Home Owner Grant Act | [GST Act](../a-new-tax-system-goods-and-services-tax-act-1999/encodings/baseline-2026-10/): new residential premises (s 4A(1)(b)), asked here as a fact, since that encoding covers GST registration only. [Migration Act 1958](../migration-act-1958/encodings/baseline-2026-10/): a permanent visa (s 30). [Australian Citizenship Act 2007](../australian-citizenship-act-2007/encodings/baseline-2026-10/): citizenship. The grant's income tax and social security treatment is in neither Commonwealth deposit and is not addressed. |
| Return to Work Act | [Social Security Act 1991](../social-security-act-1991/encodings/baseline-2026-10/): pension age (s 23), an input here, and compensation recovery (Part 3.14, s 17). The income tax treatment of the payments ([Income Tax Assessment Act 1997](../income-tax-assessment-act-1997/)) was not checked. |
| Motor Accidents (Compensation) Act | [Social Security Act 1991](../social-security-act-1991/encodings/baseline-2026-10/): pension age (s 23), an input here, and compensation recovery (ss 17, 1166-1173). [Income Tax Assessment Act 1997](../income-tax-assessment-act-1997/): weekly compensation is "paid without any deduction for income tax" (s 13(2)(d)); whether it is assessable income is not answered. |
| Victims of Crime Assistance Act | [Social Security Act 1991](../social-security-act-1991/encodings/baseline-2026-10/): s 17(2B) says a payment under a Territory law for a criminal injury is not compensation, so an award here triggers no compensation recovery or preclusion period. |

The Territory encodings also answer each other's inputs: the Stamp Duty Act's grant entitlement comes from the First Home Owner Grant Act encoding; the Motor Accidents s 10A input (covered by workers compensation) comes from the Return to Work encoding; and the Victims of Crime ss 17-18 inputs come from the Motor Accidents and Return to Work encodings.
