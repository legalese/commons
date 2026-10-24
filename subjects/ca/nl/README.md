# newfoundland-and-labrador/

Newfoundland and Labrador (Canada) legislation, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md).

The subjects here were laid out on 2026-09-23 for the legislation governing twelve everyday topics. Each was checked against the House of Assembly of Newfoundland and Labrador - Statutes and Subordinate Legislation (consolidations prepared by the Office of the Legislative Counsel, Department of Justice); the check is recorded in each subject's `registers/source-bundle/*.meta.json`. Text has since been deposited, and encoded, for two of them: see *Tax and benefits* below.

**Licence category: unclear.** The House of Assembly's Copyright & Privacy Statement permits excerpting and citing for non-commercial purposes such as research, with acknowledgement, and adds that no permission to reproduce, adapt or distribute beyond that is to be implied. On 2026-10-24 those terms were read under Michael's ruling of 24 Oct 2026 (Canadian texts whose terms permit reproduction but are silent on adaptation may be quoted in L4 encodings in Commons, with the publisher's attribution and a not-an-official-version notice), and excerpts were deposited for the two tax-and-benefits subjects. **Michael to confirm** that the closing reservation does not take these terms outside that ruling; the other subjects remain metadata only.

## Register access

Fully accessible. Fetched over plain HTTPS with an honestly identified client (User-Agent 'canon-legislation-indexer/1.0 (contact address removed)'), requests spaced about 1.8s apart; roughly 20 requests in total (the directory index of /Legislation/sr/statutes/, ten statute pages, the statutes Important Information page, the update-notice page and the House of Assembly Copyright and Privacy Statement). No 403s, no rate limiting, no bot challenge. Directory listing is enabled at /Legislation/sr/statutes/, which yielded the exact file/citation codes (for example l02.htm = RSNL1990 cL-2), so nothing had to be guessed. Statute pages are Word-generated HTML in which the title, chapter citation, the 'This is an official version.' banner and the 'Amended:' chain all appear in the header. CanLII was not used: it refuses this network.

## Topics with no legislation here

- **Passenger compensation**: No provincial passenger-compensation statute. Air, rail and marine passenger rights are federal: Canada Transportation Act, SC 1996 c 10, with the Air Passenger Protection Regulations, SOR/2019-150, made under it. The province's Motor Carrier Act, RSNL1990 cM-19 - verified as an official version at https://www.assembly.nl.ca/legislation/sr/statutes/m19.htm, amended to 2001 c19, long title 'An Act to Provide for the Regulation of Motor Vehicles Used in the Transportation of Persons for Compensation' - licenses intra-provincial passenger carriers but creates no compensation entitlement for passengers.
- **Customs/duties**: Federal matter: Customs Act, RSC 1985 c 1 (2nd Supp), and Customs Tariff, SC 1997 c 36. Provinces have no customs power (Constitution Act, 1867, s 91(2) and (3)).
- **Work permits/immigration**: Federal matter: Immigration and Refugee Protection Act, SC 2001 c 27, and its regulations. Work permits are issued federally; the provincial nominee and priority-skills streams operate administratively under a federal-provincial agreement, not under a provincial statute.

## Tax and benefits (2026-10-24)

Sourced and encoded on 2026-10-24 from the House of Assembly consolidations (and, for the indexed tax figures, the Department of Finance's published tables, which gov.nl.ca permits the public to use), as excerpts with a not-an-official-version notice:

| Subject | Deposited | Encoding |
|---|---|---|
| `income-tax-act-2000` | Income Tax Act, 2000, ss 2, 5, 6, 6.1, 7, 9, 17, 21.1, 23, 34; NLR 32/16 (income supplement and seniors' benefit); NLR 60/24 (low income tax reduction 2024); Department of Finance tables for 2025 and 2026 | `encodings/baseline-2026-10/`: the individual taxpayer's tax, credits, low income reduction, income supplement and seniors' benefit, and the duty to notify changes (2025 and 2026) |
| `income-and-employment-support-act` | Income and Employment Support Act, ss 2, 13-17, 41, 43; Income and Employment Support Regulations, NLR 144/04, Part I and s 45 | `encodings/baseline-2026-10/`: the applicant's eligibility, liquid assets, income test, most monthly income support, reporting, and the review and appeal time limits |

Each subject's `SOURCE-LICENSE.md` records the terms read and the point left for Michael.
