# india/

India (central / Union legislation) legislation, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md).

The subjects here were laid out on 2026-09-22 for the legislation governing twelve everyday topics. Each was checked against the India Code (Legislative Department, Ministry of Law and Justice); the check is recorded in each subject's `registers/source-bundle/*.meta.json`. No statute text has been deposited and nothing is encoded yet.

**Not independently spot-checked.** On 2026-09-22 India Code refused both scripted and browser access, and Legal Data Hunter was rate-limiting, so these subjects rest on the index agent's evidence alone. Four are marked unverified in their metadata (Insurance Act 1938, Railways Act 1989, Carriage by Air Act 1972, and the 2025 rural employment guarantee Act). The commencement of the Code on Wages 2019 and the Code on Social Security 2020 on 21 November 2025 is supported by a Press Information Bureau release, not yet by the Gazette notification.

**Licence category: conditional.** Reproduction is permitted on the conditions above, but the terms do not expressly grant a right to ADAPT. An L4 encoding that quotes the statute is arguably an adaptation. **Confirm before depositing text or quoting it in an encoding** -- a human decision recorded here.

## Topics with no legislation here

- **Consumer/tenancy**: Residential tenancy is State law (rent control Acts of each State or UT). The Model Tenancy Act 2021 is a model for States, not a central Act. Only the consumer half is covered centrally (Consumer Protection Act 2019).
- **Utility billing**: Only electricity has a central Act. Water and sewerage billing is State or municipal law. Retail electricity tariffs and billing codes are set by State Electricity Regulatory Commissions under the Electricity Act. Telecom billing sits under TRAI regulations; the Telecommunications Act 2023 was not verified or listed.
- **Passenger compensation**: Air passenger compensation for denied boarding, cancellation and delay is in DGCA Civil Aviation Requirements Section 3 Series M Part IV (subsidiary rules), not an Act. The Act-level statutes (Carriage by Air Act, Railways Act) could not be verified this run.

## Social security, benefits and personal income tax (sourced 2026-10-19)

These instruments were chosen so that a member of the public can get three answers: what social security covers me and what I or my employer must pay; how much income tax I owe; and how the two interact.

### The instruments

| Subject | Instrument | Why it is here | Text |
|---|---|---|---|
| `the-income-tax-act-2025` | Income-tax Act, 2025 (Act 30 of 2025), Gazette CG-DL-E-22082025-265620 | It replaced the Income-tax Act, 1961 from 1 April 2026 (s.1(3)) and governs the tax year 2026-27. It contains the charge, the heads of income, deductions, the new-regime slab table (s.202) and salary TDS. | Staged, not deposited (it is an Act) |
| `the-finance-act-2026` (new) | Finance Act, 2026 (Act 4 of 2026), Gazette CG-DL-E-31032026-271439 | It sets the rates for **both** regimes now in use: assessment year 2026-27 under the 1961 Act (s.2, First Schedule Part I-A) and tax year 2026-27 under the 2025 Act (s.3, Part I-B). It also sets TDS and advance-tax rates and amends the 2025 Act. | Staged, not deposited (it is an Act) |
| `the-code-on-social-security-2020` | Code on Social Security, 2020 (Act 36 of 2020), Gazette CG-DL-E-29092020-222111 | It commenced on 21 November 2025 (S.O. 5319(E)) and repealed the EPF Act 1952, ESI Act 1948, Payment of Gratuity Act 1972, Maternity Benefit Act 1961 and five others (s.164). It covers provident fund and pension contributions (s.16), ESI, gratuity (s.53), maternity benefit (s.60) and gig and unorganised workers. | Staged, not deposited (it is an Act) |
| `the-social-security-central-rules-2026` (new) | Social Security (Central) Rules, 2026, G.S.R. 344(E), Gazette CG-DL-E-08052026-272366 | The Code's central rules, in force 8 May 2026. They supersede the ESI (Central) Rules 1950, the Payment of Gratuity (Central) Rules 1972 and others, and set benefit rates and procedures. | **Deposited** (English pages) |
| `the-national-food-security-act-2013` | National Food Security Act, 2013 (Act 20 of 2013), Gazette of 10 September 2013 | The legal entitlement to subsidised foodgrains, maternity benefit of not less than Rs 6,000 (s.4) and child meals. | Staged, not deposited (it is an Act) |
| same | S.O. 6148(E) of 30 December 2022 (CG-DL-E-30122022-241510) and S.O. 5241(E) of 4 December 2023 (CG-DL-E-11122023-250548) | Under Schedule I, foodgrains are free of cost for eligible households from 1 January 2023 to 31 December 2028. These notifications set the current price, which is nil. | **Deposited** |

**How they connect.** The Income-tax Act decides how social security money is taxed. For example, Code s.18 deems the Code's Provident Fund to be a recognised provident fund for the Income-tax Act 1961, and the 2025 Act taxes the annual accretion and transferred balances of recognised provident funds (s.7, Schedule XI). The Finance Act sets the slabs that apply to income that is not exempt. The Code and its Rules settle contributions, which are deducted from wages, and benefits.

### Terms and currency

- **The source is e-Gazette (egazette.gov.in).** It has no robots.txt and publishes no terms. India Code, the Legislative Department, the Income Tax Department, EPFO and the Ministry of Labour all returned 403 to the declared fetcher on 2026-10-19. None of them was retried by another route. ESIC timed out. Full records are in each subject's SOURCE-LICENSE.md.
- **What could be deposited.** Gazette matter other than Acts is freely reproducible (Copyright Act s.52(1)(q)(i)), so only the Rules and the notifications are deposited. Acts may be reproduced only together with commentary or other original matter (s.52(1)(q)(ii)). The four Act texts are therefore converted, checksummed in their meta files and held outside the repository until someone decides on that condition.
- **The texts are as published, not consolidated.** None includes later amendments. In particular, the Income-tax Act 2025 text does not include the Finance Act, 2026's amendments.
- Currency as checked: Income-tax Act 2025 in force 1 April 2026; Finance Act 2026 assented 30 March 2026; Code commenced 21 November 2025; Rules in force 8 May 2026; free foodgrains until 31 December 2028.

### Gaps

- **Income-tax Act, 1961.** It still governs assessment year 2026-27, the returns being filed in 2026. No consolidated text could be reached, because India Code and the Income Tax Department refused access.
- **Income-tax Rules, 2026** (CBDT, Gazette CG-DL-E-20032026-271092, about 29 MB, bilingual). Found but not fetched for this sample. They hold perquisite valuation and other figures.
- **Commencement notification S.O. 5319(E) of 21 November 2025.** It is known only from its citation in ESIC notification CG-DL-E-29072026-274902, which is in Hindi, and from that item's archive.org summary. It is not in the archive.org mirror and was not retrieved. Whether the Code commenced fully or in part is therefore not confirmed from the notification itself.
- **Not sourced:** schemes continued under the Code (EPF Scheme 1952, Employees' Pension Scheme 1995, EDLI 1976), which hold the EPF wage ceiling and the pension formula; ESIC contribution rates and the wage ceiling for coverage; the gratuity ceiling notification; the NFSA price notification for ss.4-6 (S.O. 3546(E), 2019), the principal Schedule I notification (S.O. 3577(E), 2016) and the 2023 Schedule II amendment.
- **Conversion.** Marginal section headings were missed for about 15 sections of the Income-tax Act 2025, 3 of the Code, 4 of the NFSA and 4 of the Finance Act. Unruled schedule tables are split on column gaps, and multi-line cells become several rows.
