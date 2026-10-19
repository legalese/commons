# new-south-wales/

New South Wales Acts, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md).

The subjects here were laid out on 2026-09-22 for the Acts that govern twelve everyday topics -- payroll, leave, termination, pensions, government benefits, personal tax, insurance claims, utility billing, passenger compensation, consumer and tenancy, customs and duties, and work permits. The mapping and the check of each Act against the official register are in `tools/topics/`. Until 2026-10-20 no statute text had been deposited; nothing is encoded yet.

## Social security and benefits, and personal income tax (Priority 3 sample, 2026-10-20)

> **Warning.** Every NSW text deposited for this sample is **taken from the Open Australian Legal Corpus, collected on 2025-03-10; it is not the current official text and may be out of date — check legislation.nsw.gov.au before relying on it.** The official register could not be fetched (see "Terms and access" below).

### How the NSW set connects to the Commonwealth

In Australia personal income tax and the main social security payments are Commonwealth law, and their texts are already sourced beside this folder: [`../income-tax-assessment-act-1997/`](../income-tax-assessment-act-1997/), [`../income-tax-rates-act-1986/`](../income-tax-rates-act-1986/), [`../medicare-levy-act-1986/`](../medicare-levy-act-1986/), [`../social-security-act-1991/`](../social-security-act-1991/), [`../social-security-administration-act-1999/`](../social-security-administration-act-1999/) and [`../a-new-tax-system-family-assistance-act-1999/`](../a-new-tax-system-family-assistance-act-1999/). NSW levies no income tax. What a NSW resident meets on top of the Commonwealth layer is (a) state payments and concessions, some of them switched on by a Commonwealth status, and (b) state taxes that fall on individuals rather than businesses, chiefly on the home.

The joins. Claims confirmed by a deposited text cite the provision; the rest are marked **unverified (from general knowledge, not from the texts)**.

- **Commonwealth pension status opens the council-rates concession.** Local Government Act 1993, Chapter 15, Part 8, Division 1, s 575, reduces the rates and domestic waste charges of an "eligible pensioner" by one-half, capped at $250 a year for ordinary rates and domestic waste charges and $87.50 each for water and sewerage special rates (s 575(3)), as the text stood at 2025-01-01. The Local Government (General) Regulation 2021, cl 134(a), prescribes as eligible pensioners people who receive a pension, benefit or allowance under Chapter 2 of the Social Security Act 1991 (Cth), or a service pension under Part III of the Veterans' Entitlements Act 1986 (Cth), and are entitled to a Commonwealth pensioner concession card; cl 134(b)-(d) add certain DVA and military compensation recipients.
- **Workers compensation weekly payments stop by reference to the Commonwealth age pension age.** Workers Compensation Act 1987, s 52, defines "retiring age" as the age at which the person would be eligible for the age pension under the Social Security Act 1991 (Cth), and ends weekly payments one year after it (or 12 months after the first incapacity, for an injury received after it).
- **State payments and Commonwealth income tests.** That workers compensation weekly payments are assessable income under the Income Tax Assessment Act 1997 and are "compensation" that can reduce or preclude a Centrelink payment (Social Security Act 1991, Part 3.14), and that victims support recognition payments are not counted as income for either, is **unverified (from general knowledge, not from the texts)**.
- **The home ties the state tax side together.** The land tax principal place of residence exemption (Land Tax Management Act 1956, s 10, paragraph (r), and Schedule 1A), the First Home Buyers Assistance Scheme in transfer duty (Duties Act 1997, Part 8, Division 1, including ss 78A and 78AA) and the first home owner grant (First Home Owner Grant and Shared Equity Act 2000, Part 2: s 9, citizenship or permanent residency; s 12, the residence requirement) each turn on owning and occupying a home as a principal place of residence. That the Commonwealth main-residence capital gains exemption (ITAA 1997, Subdivision 118-B) asks a similar but not identical question is **unverified (from general knowledge, not from the texts)**.

### The instruments chosen

Social security and benefits (state layer):

| Subject | Text (corpus version date) | Characters | Why |
| --- | --- | --- | --- |
| [`victims-rights-and-support-act-2013`](victims-rights-and-support-act-2013/) | act-2013-037 (2025-02-01) | 167,610 | The Victims Support Scheme (Part 4): counselling, financial support and recognition payments (categories in s 35). |
| [`victims-rights-and-support-regulation-2019`](victims-rights-and-support-regulation-2019/) | sl-2019-0398 (2025-02-01) | 16,210 | Sets the numbers: for example $5,000 for immediate needs, $30,000 for a primary victim's economic loss, counselling rates. |
| [`workers-compensation-act-1987`](workers-compensation-act-1987/) | act-1987-070 (2023-10-30) | 740,729 | Weekly compensation (Part 3, Division 2), medical expenses, lump sums, death benefits. |
| [`workplace-injury-management-and-workers-compensation-act-1998`](workplace-injury-management-and-workers-compensation-act-1998/) | act-1998-086 (2024-07-01) | 387,961 | Making a claim, provisional liability, notices the worker must be given, disputes. |
| [`workers-compensation-regulation-2016`](workers-compensation-regulation-2016/) | sl-2016-0559 (2024-07-24) | 314,180 | Number-setting instrument under the 1987 Act. |
| [`local-government-act-1993`](local-government-act-1993/) | act-1993-030 (2025-01-01) | 1,197,506 | The statutory pensioner rebate on council rates and charges (ss 575-584). |
| [`local-government-general-regulation-2021`](local-government-general-regulation-2021/) | sl-2021-0460 (2024-09-02) | 658,510 | Defines "eligible pensioner" by Commonwealth pension and card (cl 134). |
| [`first-home-owner-grant-and-shared-equity-act-2000`](first-home-owner-grant-and-shared-equity-act-2000/) | act-2000-021 (2023-09-04) | 98,845 | The first home owner grant ($10,000 for a transaction from 1 January 2016) and its residence requirement. Formerly the First Home Owner Grant (New Homes) Act 2000; the subject is named for the title the corpus records. |

Personal state taxes:

| Subject | Text (corpus version date) | Characters | Why |
| --- | --- | --- | --- |
| [`land-tax-management-act-1956`](land-tax-management-act-1956/) | act-1956-026 (2024-12-02) | 210,764 | Liability, exemptions including the principal place of residence (Schedule 1A), thresholds (Part 7, Division 4). |
| [`land-tax-act-1956`](land-tax-act-1956/) | act-1956-027 (2024-12-02) | 48,801 | Imposes land tax and surcharge land tax and sets the rate scale. |
| [`duties-act-1997`](duties-act-1997/) | act-1997-123 (2025-01-01) | 690,434 | Transfer duty on a home, the First Home Buyers Assistance Scheme, surcharge purchaser duty. |

Eleven texts, 4,531,550 characters in all (including the notice header on each). The [`motor-accident-injuries-act-2017`](motor-accident-injuries-act-2017/) (statutory weekly benefits after a road injury) and [`energy-and-utilities-administration-act-1987`](energy-and-utilities-administration-act-1987/) already sit here and connect to the benefits topic, but were not part of this sample and have no text.

### Terms and access

- **legislation.nsw.gov.au.** The first request, for `https://legislation.nsw.gov.au/robots.txt` at 2026-10-19T17:01:02Z with User-Agent `legalese-commons-source-fetcher/1.0 (+https://github.com/legalese/commons)`, returned **HTTP 403 with a Cloudflare managed challenge** ("Just a moment...", header `cf-mitigated: challenge`). Neither robots.txt nor the copyright page could be read, and no further request was made. The licence recorded for the neighbouring subjects (CC BY 4.0, State of New South Wales, from `https://legislation.nsw.gov.au/copyright` on 2026-09-22) is the last known statement of the site's terms.
- **AustLII** (www.austlii.edu.au). `robots.txt` (read 2026-10-19T17:01:12Z) allows all user-agents (`User-agent: *` / `Allow: /`) but carries the content signal `search=yes,ai-train=no,use=reference` and disallows named AI crawlers. Its copyright page (`/austlii/copyright.html`, 17:01:26Z) returned the same Cloudflare challenge; nothing was taken from AustLII.
- **Open Australian Legal Corpus** (Hugging Face, `isaacus/open-australian-legal-corpus`, version 7.1.0, by Umar Butt / Isaacus) -- **the route used**, on the owner's decision of 2026-10-20.
  - `https://huggingface.co/robots.txt`, read 2026-10-19: `User-agent: *` / `Allow: /`.
  - Dataset card and `LICENCE.md`, read 2026-10-19: the corpus "is licensed under the Creative Commons Attribution 4.0 International Licence"; documents from NSW Legislation are also CC BY 4.0, with the required wording "Sourced from the New South Wales Legislation website at 10 March 2025. For the latest information on New South Wales Government legislation please go to https://www.legislation.nsw.gov.au." NSW Legislation was last collected on 10 March 2025.
  - The corpus has **no per-document licence field** (its fields are version_id, type, jurisdiction, source, mime, date, citation, url, when_scraped, text); each meta.json records the per-document licence as CC BY 4.0 by virtue of `LICENCE.md`.
  - Download: the documented file `corpus.jsonl` (9,401,179,433 bytes) was streamed once in full from `https://huggingface.co/datasets/isaacus/open-australian-legal-corpus/resolve/main/corpus.jsonl`; its sha256 as computed, `5abc64a3ad35a44eca65706babd63d1095c29ebebf3f5c588beb56612097b758`, equals the file's published LFS oid. Only the eleven NSW documents were kept. The First Home Owner Grant text, missed by the first pass because of its changed title, was taken in a second pass that stopped after the first 486,539,264 bytes of the same file.
- Each text opens with the warning, an unofficial-version notice, the NSW and corpus attributions, and the corpus document's version_id, date, url and scrape time. The same are in each meta.json (`corpus`, `warning`, `attribution`, `download_sha256`, `source_text_sha256`, `text_sha256`, `text_chars`) and SOURCE-LICENSE.md.

### Currency and gaps

- **Currency.** The corpus records each document's latest version as of its scrape (2025-03-10): version dates run from 2023-09-04 (First Home Owner Grant Act) to 2025-02-01 (victims support). Everything enacted or indexed since -- land tax thresholds for 2026, any change to the duty concession or grant, the pensioner rebate cap, victims support amounts -- is missing. Check the official register before encoding any number.
- **Tables.** The corpus had already flattened tables into space-aligned lines (for example the counselling rates in the victims support regulation); they were not re-formed into `| a | b |` rows.
- **Numbers set outside these instruments**: the indexed workers compensation weekly maximum and other amounts (SIRA notices in the Government Gazette); the land tax thresholds for each year (worked out under the Management Act, Part 7, Division 4, and published by Revenue NSW). The Land Tax Management Regulation 2024 (sl-2024-0196) is in the corpus but was not taken.
- **Out of scope**: the Taxation Administration Act 1996 (objections, interest and penalties for state taxes -- the next instrument to add for the tax side); concessions run as programmes without their own statute (Seniors Card, transport concessions, most energy rebates).
- **To replace**: when legislation.nsw.gov.au can be fetched (for example after asking the NSW Parliamentary Counsel's Office for a permitted route), re-read its copyright page and replace all eleven texts with current official ones.
