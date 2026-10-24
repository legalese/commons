# south-australia/

South Australian Acts, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md).

**579 Acts are indexed here, and ten regulations were added on 2026-10-24. Twenty instruments (ten Acts and ten regulations) are sourced, all for the tax-and-benefits sample below and all from the Open Australian Legal Corpus. Nothing was encoded when they were deposited.**

## Indexed

Every principal Act on the South Australian *Current Titles* list of 22 September 2026 has a subject folder with `subject.json`, `SOURCE-LICENSE.md` and `registers/source-bundle/<id>.meta.json`.
Fourteen were laid out on 2026-09-22 for twelve everyday topics (payroll, leave, termination, pensions, government benefits, personal tax, insurance claims, utility billing, passenger compensation, consumer and tenancy, customs and duties, and work permits); the other 565 were added on 2026-10-19 from the same list.
Each new `meta.json` carries the version the list gave (`listed_version`, as `d.m.yyyy`).

Eight entries appear on the list with only an uncommenced version stamp: Animal Welfare Act 2025, Biodiversity Act 2025, Biosecurity Act 2025, Children and Young People (Safety and Support) Act 2025, Explosives Act 2024, Scrap Metal Dealers Act 2025, Social Workers Registration Act 2021, and Environment Protection (Sea Dumping) Act 1984.
Their `meta.json` has a `note` saying the Act may not yet be in force.
Some of them (the 1984 Act certainly) are in force with an amendment pending, and the stamp sits where the list wrapped a line; the register must settle each one.

The list could not be re-read on 2026-10-19 or since (see "Terms and access" below), so an Act passed, commenced or repealed after 22 September 2026 is not yet reflected here.

## Tax and benefits sample (sourced 2026-10-24)

> **Warning.** Every South Australian text deposited here is **taken from the Open Australian Legal Corpus, which last collected South Australian legislation on 2025-03-10; it is not the current official text and may be out of date — check legislation.sa.gov.au before relying on it.** The official register could not be fetched (see "Terms and access" below).

### How the South Australian set connects to the Commonwealth

In Australia personal income tax and the main social security payments are Commonwealth law, and their texts are already sourced beside this folder: [`../income-tax-assessment-act-1997/`](../income-tax-assessment-act-1997/), [`../income-tax-rates-act-1986/`](../income-tax-rates-act-1986/), [`../medicare-levy-act-1986/`](../medicare-levy-act-1986/), [`../social-security-act-1991/`](../social-security-act-1991/), [`../social-security-administration-act-1999/`](../social-security-administration-act-1999/) and [`../a-new-tax-system-family-assistance-act-1999/`](../a-new-tax-system-family-assistance-act-1999/). South Australia levies no income tax. What a resident meets on top of the Commonwealth layer is (a) state taxes that fall on individuals, chiefly on the home and the car, and (b) state payments and concessions, several of them switched on by a Commonwealth card or payment.

The joins. Claims confirmed by a deposited text cite the provision; the rest are marked **unverified (from general knowledge, not from the texts)**.

- **Commonwealth cards and payments open the cost of living concession.** The Cost of Living Concessions Regulations 2020, reg 3(1), define a "prescribed card" as a Pensioner Concession Card, a Low Income Health Care Card or one of the Gold Repatriation Health Cards issued by the Commonwealth, and "prescribed payments" as, among others, Austudy, JobSeeker, parenting payment, special benefit and youth allowance under the Social Security Act 1991 (Cth); reg 8 sets the concession at $255.60 (indexed by the Adelaide CPI under reg 3(3)), as the text stood at 2025-01-01. Entitlement turns on occupying residential premises as owner or tenant on 1 July (Act, s 3).
- **The same cards and payments open the emergency services levy remission on the home.** Emergency Services Funding (Remissions—Land) Regulations 2014, reg 6: the levy on residential land that is the holder's principal place of residence is remitted for a holder of a Commonwealth Pensioner Concession Card, Commonwealth Seniors Health Card, Low Income Health Care Card or Gold Repatriation Health Card, or a recipient of the Social Security Act 1991 payments listed in reg 6(5)(h); reg 7(3) adds a further $46. The main amount (reg 7(2)) is a formula the corpus text has lost (below).
- **A Commonwealth pensioner card halves the car's registration fee.** Motor Vehicles Act 1959, s 38A: the registration fee of one vehicle wholly or mainly used to transport an owner who holds a pensioner entitlement card under a Commonwealth law, and is entitled to reduced public transport fares in the State, is reduced by the prescribed amount; Motor Vehicles Regulations 2010, reg 77(4), prescribes 50% of the registration fee (also for trailers, s 38AB). Schedule 1 to the Regulations (clause 22) sets a reduced driver's licence fee for the same card holders.
- **Workers compensation weekly payments stop at the Commonwealth age pension age.** Return to Work Act 2014, s 44: "retiring age" is the lesser of the normal retiring age for the employment and the age at which the worker would be eligible for the age pension under the Social Security Act 1991 (Cth); weekly payments are not payable for incapacity after it (s 44(2)), with a separate rule for a worker who becomes incapacitated within two years of that age or after it (s 44(3)).
- **State payments and Commonwealth income tests.** That Return to Work weekly payments are assessable income under the Income Tax Assessment Act 1997 and are "compensation" that can reduce or preclude a Centrelink payment (Social Security Act 1991, Part 3.14), that motor accident damages under the Civil Liability Act 1936 are compensation in the same sense, and that victims of crime statutory compensation and the cost of living concession are not counted as income for either, is **unverified (from general knowledge, not from the texts)**.
- **The home ties the state tax side together.** Land tax's residential land exemption (Land Tax Act 1936, ss 5, 5AA, 5A), the stamp duty relief on new homes and land (Stamp Duties Act 1923, s 71DD), the first home owner grant's residence requirement (First Home and Housing Construction Grants Act 2000, s 12) and the levy remission above each turn on owning and occupying a home. That the Commonwealth main-residence capital gains exemption (ITAA 1997, Subdivision 118-B) asks a similar but not identical question is **unverified (from general knowledge, not from the texts)**.

### The instruments chosen

Each subject's `registers/source-bundle/<slug>.txt` is the text; its `.meta.json` records the corpus version_id, scrape time and hashes, and `SOURCE-LICENSE.md` the terms and the ruling. The source id is the subject's slug; `register_file` in the meta names the register's own document file.

Personal state taxes:

| Subject | Text as at (scraped) | Characters | Why |
| --- | --- | --- | --- |
| [`stamp-duties-act-1923`](stamp-duties-act-1923/) | 2025-02-13 (2025-03-10) | 363,479 | Conveyance duty on a home (Schedule 2 clause 3), the off-the-plan apartment concession (s 71DB), relief on new homes and land (s 71DD) and its clawback (s 71DE), motor vehicle duty (Part 3 Division 4, Schedule 2 clause 2). 9 formulas missing. |
| [`stamp-duties-regulations-2013`](stamp-duties-regulations-2013/) | 2022-09-29 (2024-09-13) | 10,764 | The concession card class for a motor vehicle duty exemption (reg 14), heavy and electric vehicle exemptions. |
| [`land-tax-act-1936`](land-tax-act-1936/) | 2023-07-01 (2024-09-13) | 147,916 | Exemptions including the residential land exemption (ss 5-5A), calculation (s 8A), the scales (Schedule 1). 8 formulas missing, among them the threshold indexation in s 8A. |
| [`taxation-administration-act-1996`](taxation-administration-act-1996/) | 2019-10-03 (2024-09-13) | 107,786 | Assessments, refunds, interest and penalty tax, objections and appeals for stamp duty and land tax. |
| [`emergency-services-funding-act-1998`](emergency-services-funding-act-1998/) | 2023-11-25 (2024-09-13) | 90,301 | The emergency services levy on land and on vehicles and vessels; objections, refunds, interest and penalty levy. |
| [`emergency-services-funding-remissions-land-regulations-2014`](emergency-services-funding-remissions-land-regulations-2014/) | 2024-07-01 (2024-09-13) | 30,265 | Remissions of the levy on the home, including for Commonwealth concession card holders (regs 5A-7). 9 formulas missing. |
| [`emergency-services-funding-remissions-motor-vehicles-and-vessels-regulations-2014`](emergency-services-funding-remissions-motor-vehicles-and-vessels-regulations-2014/) | 2020-07-01 (2024-09-13) | 5,637 | Remission of the levy on trailers and vessels (whole) and primary producers' vehicles ($20). |
| [`motor-vehicles-regulations-2010`](motor-vehicles-regulations-2010/) | 2025-02-20 (2025-03-10) | 276,806 | Registration and licence fees and the pensioner reductions (reg 77(4), Schedule 1). |

State payments and concessions:

| Subject | Text as at (scraped) | Characters | Why |
| --- | --- | --- | --- |
| [`first-home-and-housing-construction-grants-act-2000`](first-home-and-housing-construction-grants-act-2000/) | 2025-02-13 (2025-03-10) | 103,257 | The first home owner grant: eligibility (Part 2 Division 2, residence requirement s 12), amount (s 18), objections, repayment and recovery (ss 39, 40). 4 formulas missing, in the bonus grants (ss 18B, 18BA), the housing construction grant (s 18BAB) and the seniors housing grant (s 18BAC). |
| [`first-home-and-housing-construction-grants-regulations-2015`](first-home-and-housing-construction-grants-regulations-2015/) | 2021-03-11 (2024-09-13) | 10,584 | Interest on a grant repaid by instalments (reg 6), relevant interests, exclusions. |
| [`cost-of-living-concessions-act-1986`](cost-of-living-concessions-act-1986/) | 2015-07-01 (2024-09-13) | 13,821 | The cost of living concession and remission of rates. Formerly the Rates and Land Tax Remission Act 1986. |
| [`cost-of-living-concessions-regulations-2020`](cost-of-living-concessions-regulations-2020/) | 2025-01-01 (2025-03-10) | 18,327 | Who qualifies (Commonwealth cards and payments) and the amount (reg 8). |
| [`return-to-work-act-2014`](return-to-work-act-2014/) | 2024-12-01 (2025-03-10) | 478,930 | Claims, medical expenses, weekly payments (Part 4 Division 4), redemptions, lump sums for permanent impairment, death benefits, common law limits. 3 formulas missing: the overtime component of average weekly earnings (s 5), the economic loss lump sum (s 56(4)), the base premium (s 142). |
| [`return-to-work-regulations-2015`](return-to-work-regulations-2015/) | 2024-12-01 (2025-03-10) | 108,507 | Indexation, average weekly earnings, notice of injury, interest on arrears, lump sums (reg 34), death (reg 35). |
| [`motor-vehicles-act-1959`](motor-vehicles-act-1959/) | 2024-11-07 (2025-03-10) | 652,739 | Pensioner registration concessions (ss 38A-40A) and Part 4, compulsory third party insurance: the claim notice (s 126A), the nominal defendant (ss 115, 116). |
| [`motor-vehicles-third-party-insurance-regulations-2013`](motor-vehicles-third-party-insurance-regulations-2013/) | 2021-11-01 (2024-09-13) | 6,214 | When and how the injured person must give notice of a CTP claim (within 6 months, reg 4). |
| [`civil-liability-act-1936`](civil-liability-act-1936/) | 2023-06-22 (2024-09-13) | 162,219 | Part 8, damages for personal injury, which applies to motor accidents: where the injured person's entitlements under the CTP scheme are assessed. |
| [`civil-liability-regulations-2013`](civil-liability-regulations-2013/) | 2015-10-02 (2024-09-13) | 132,929 | Injury scale values (Schedule 1), State average weekly earnings and gratuitous services, motor vehicle injury assessment. |
| [`victims-of-crime-act-2001`](victims-of-crime-act-2001/) | 2021-01-01 (2024-09-13) | 72,275 | Statutory compensation (Part 4), with the indexed caps in s 20 and the non-financial loss scale (Schedule a1). |
| [`victims-of-crime-statutory-compensation-regulations-2019`](victims-of-crime-statutory-compensation-regulations-2019/) | 2023-05-11 (2024-09-13) | 22,043 | What an application must contain (Schedule 1) and the prescribed legal costs (Schedule 2). |

Twenty texts, 2,814,799 characters in all (including the notice header on each). The Motor Vehicles Act was taken for both its Part 4 and its registration concessions; the person's damages after a road injury are assessed under the Civil Liability Act 1936, Part 8, so both are here. The Compulsory Third Party Insurance Regulation Act 2016 (the CTP Regulator) and the Return to Work Corporation of South Australia Act 1994 are machinery and were not taken.

### Currency and gaps

- **Currency.** The corpus records each document's latest version as of its scrape: 13 of the 20 were scraped on 2024-09-13 and 7 on 2025-03-10, and the version dates run from 2015-07-01 (Cost of Living Concessions Act) to 2025-02-20 (Motor Vehicles Regulations). Compared with the Current Titles list of 22 September 2026: the Land Tax Act, the Taxation Administration Act, the Emergency Services Funding Act and the First Home and Housing Construction Grants Act were listed at 4.12.2025 and the Victims of Crime Act at 1.4.2025, so each has at least one later version than the text here; the Civil Liability Act (22.6.2023) and the Cost of Living Concessions Act (1.7.2015) were listed at the same date as their texts. The Stamp Duties Act, the Return to Work Act, the Motor Vehicles Act and the ten regulations have no listed version to compare. Everything amended or indexed since -- land tax thresholds for 2025-26 and 2026-27, the cost of living concession amount, the indexed victims of crime caps, Return to Work amounts -- is missing. Each `meta.json` has a `currency` note where a comparison was possible.
- **Formulas.** 33 formulas are missing from the corpus text: 9 in the Stamp Duties Act (including the s 71DD relief on new homes and the s 71DB off-the-plan concession), 8 in the Land Tax Act (including the s 8A threshold indexation and the double-taxation deductions), 9 in the levy's land remissions, 4 in the First Home and Housing Construction Grants Act, and 3 in the Return to Work Act. Each subject that has them carries a `<slug>.formulas.md` sidecar listing where each was lost, its lead-in and the terms its "where" list defines. **None is restored**: the authorised rendering could not be fetched, and none may be guessed. The places were found by their lead-in pattern; a formula lost in some other way would not be listed.
- **Tables.** The corpus kept tables as `cell|cell|` rows (striprtf's rendering of the RTF tables), for example the duty and land tax scales; they were not re-formed.
- **Numbers set outside these instruments**: the emergency services levy rates and area and land use factors, declared each year by notice (Emergency Services Funding Act, s 10); the "low income earner" amounts, published by the Minister on the concessions website (Cost of Living Concessions Regulations, reg 3); the amounts marked "(indexed)", which the Victims of Crime Act (s 4(2), each 1 January by the CPI), the Cost of Living Concessions Regulations (reg 3(3)) and the Return to Work Act and Regulations adjust each year; the land tax thresholds, adjusted by the s 8A formulas that are missing here.
- **In the corpus but not taken**: Land Tax Regulations 2010 (owners' notices), Taxation Administration Regulations 2017 (disclosure), Victims of Crime (Fund and Levy) Regulations 2018, the Return to Work transitional regulations, Motor Vehicles (National Heavy Vehicles Registration Fees) Regulations 2008, Valuation of Land Act 1971, Local Government (General) Regulations 2013.
- **To replace**: when legislation.sa.gov.au can be fetched (for example after asking the Attorney-General's Department, which runs it, for a permitted route), re-read its copyright page, replace all twenty texts with the current official ones, and restore the formulas from the authorised versions.

## Terms and access

**Owner's ruling, 2026-10-24.** Michael ruled in chat, in these words: "On NT, Vic and SA, yes please go ahead". For South Australia this means the texts may be sourced the same way the New South Wales texts were on 2026-10-20, from the Open Australian Legal Corpus (CC BY 4.0), if the official register still refuses. It still refused on 2026-10-24 (below), so the corpus was used. The ruling is recorded in each deposited subject's `SOURCE-LICENSE.md` and `meta.json` (`ruling`).

Read on 2026-10-19:

- `https://www.legislation.sa.gov.au/robots.txt` allows `/lz` and `/_legislation-documents`, disallows `/search` and the CMS's own paths, and sets `Crawl-delay: 10`.
- The footer of every page: "Except where otherwise noted content on this site is licensed under a Creative Commons Attribution 4.0 International Licence (CC BY 4.0). See Copyright for more information."
- `https://www.legislation.sa.gov.au/copyright` (read on 2026-09-22: CC BY 4.0) was behind the bot challenge.
- `https://www.legislation.sa.gov.au/disclaimer`: the State accepts no liability for accuracy except as set out there; legislation published under the *Legislation Revision and Publication Act 2002* is the authorised version, identified by a tick logo at the point of download and a statement at the foot of each page.

On 2026-10-19 the register's documents, for example the current RTF of the Electricity Act 1996 at
`https://www.legislation.sa.gov.au/_legislation-documents/lz/c/a/electricity-act-1996/current/1996.96.un.rtf`,
answered a scripted client with HTTP 403 and a Cloudflare managed challenge (`Cf-Mitigated: challenge`, "Enable JavaScript and cookies to continue").
The Copyright page and the Current Titles page answered the same way.
The Act landing pages (`/lz?path=/C/A/<TITLE>`) and the Disclaimer page did load, and show where each text lives: every Act has `current/<year>.<number>.un.rtf` (unauthorised, the one to convert) and `current/<year>.<number>.auth.pdf` (the authorised version) under `_legislation-documents/lz/c/a/<slug>/`.

On 2026-10-24, one check, with User-Agent `legalese-commons-source-fetcher/1.0 (+https://github.com/legalese/commons)`:

- `https://www.legislation.sa.gov.au/robots.txt` (04:20:41Z): HTTP 200, unchanged in substance (`Crawl-delay: 10`; `/_designs/`, `/search` and the CMS's own paths disallowed).
- The Stamp Duties Act 1923 landing page, `https://www.legislation.sa.gov.au/lz?path=%2FC%2FA%2FSTAMP%20DUTIES%20ACT%201923` (04:21:31Z, more than ten seconds later): **HTTP 403 with `cf-mitigated: challenge`** ("Just a moment...", "Enable JavaScript and cookies to continue"). The landing pages now refuse too, so the RTF link could not be read and the RTF was not requested. No further request was made to the register; this repository does not route around bot protection.

The route used, the **Open Australian Legal Corpus** (Hugging Face, `isaacus/open-australian-legal-corpus`, version 7.1.0, by Umar Butler / Isaacus):

- `https://huggingface.co/robots.txt`, read 2026-10-24: `User-agent: *` / `Allow: /`.
- Dataset card and `LICENCE.md`, read 2026-10-24: the corpus "is licensed under the Creative Commons Attribution 4.0 International Licence"; documents from the South Australian Legislation database are also CC BY 4.0, with the required wording "Sourced from the South Australian Legislation website at 10 March 2025. For the latest information on South Australian Government legislation, please go to www.legislation.sa.gov.au/." The card says South Australian Legislation was last collected on 10 March 2025, taking the most recent versions of all in force Acts and of all in force proclamations, policies and regulations; the corpus holds 1,350 South Australian documents (572 Acts, 495 secondary instruments, 283 bills).
- The corpus has **no per-document licence field** (its fields are version_id, type, jurisdiction, source, mime, date, citation, url, when_scraped, text); each meta.json records the per-document licence as CC BY 4.0 by virtue of `LICENCE.md`. Every South Australian document the corpus holds was extracted from the register's unauthorised RTF (`mime` `application/rtf`), with striprtf.
- Download: the documented file `corpus.jsonl` (9,401,179,433 bytes, 232,560 documents) was streamed once in full from `https://huggingface.co/datasets/isaacus/open-australian-legal-corpus/resolve/main/corpus.jsonl` on 2026-10-24 (04:24:59Z to 04:37:24Z) without being written to disk; its sha256 as computed, `5abc64a3ad35a44eca65706babd63d1095c29ebebf3f5c588beb56612097b758`, equals the file's published LFS oid (the same file the NSW texts came from). Only South Australian records were kept, and twenty were deposited.
- Each text opens with the warning, an unofficial-version notice, the South Australian and corpus attributions, the corpus document's version_id, date, url and scrape time, and a note of the changes made (line endings and blank lines normalised; no wording changed). The same are in each meta.json (`corpus`, `warning`, `attribution`, `download_sha256`, `corpus_line_sha256`, `source_text_sha256`, `text_sha256`, `text_chars`) and SOURCE-LICENSE.md.
