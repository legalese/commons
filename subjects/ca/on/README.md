# ontario/

Ontario (Canada) legislation, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md).

The subjects here were laid out on 2026-09-22 for the legislation governing twelve everyday topics. Each was checked against the e-Laws (Ontario.ca/laws), King's Printer for Ontario; the check is recorded in each subject's `registers/source-bundle/*.meta.json`. Statute and regulation text has since been deposited for four subjects on social security and benefits and on personal income tax (below); nothing is encoded yet.

**Licence category: conditional.** The King's Printer permits anyone to reproduce Ontario statutes and regulations free and without permission, commercial use included, on three conditions: accuracy, the acknowledgement "© King's Printer for Ontario, <year>", and a statement that the copy is not an official version. The terms do not expressly grant a right to ADAPT. An L4 encoding that quotes the statute is arguably an adaptation. **Confirm before quoting the text in an encoding** -- a human decision recorded here.

## Topics with no legislation here

- **Passenger compensation**: Air passenger rights (Canada Transportation Act and the Air Passenger Protection Regulations) and interprovincial rail are federal. No Ontario statute governs passenger compensation.
- **Customs/duties**: Customs and tariffs are exclusively federal (Customs Act, Customs Tariff). Ontario has no customs legislation.
- **Pensions/social security**: Partial gap. The Canada Pension Plan, Old Age Security and Employment Insurance are federal statutes. Only occupational pension plans are provincial (the Pension Benefits Act, listed). Provincial social assistance, disability support and the seniors' top-up are now sourced (below).
- **Work permits/immigration**: Partial gap. Work permits, visas and admission are governed by the federal Immigration and Refugee Protection Act. Ontario legislates only its nominee program and protections for foreign workers (listed).
- **Personal tax/withholding**: Partial gap. Source withholding is administered federally by the Canada Revenue Agency under the Income Tax Act (Canada). Ontario's Taxation Act, 2007 sets provincial rates and credits (now sourced, below).

## Sourced: social security and benefits, and personal income tax (2026-10-20)

Four Ontario Acts, each with the regulation(s) that set the numbers and conditions a person needs, chosen so that a member of the public in Ontario can be told how much Ontario income tax they owe, which provincial benefits and credits they can get (Ontario Works, ODSP income support, GAINS, the Ontario Child Benefit and the Ontario Trillium Benefit), and how these interact with the federal Income Tax Act, EI, CPP, OAS and the Canada Disability Benefit already sourced under [`subjects/ca/`](../README.md). Each regulation is deposited in its Act's subject, beside the Act; `ontario-guaranteed-annual-income-act` is a new subject.

All nine texts are the e-Laws consolidation as it stood at the **e-Laws currency date of 2026-10-14**, English version, converted from e-Laws' own "Download Word" files (one exception, below). Each subject's `SOURCE-LICENSE.md` records the terms read; each `registers/source-bundle/<id>.meta.json` records the URL, consolidation period, retrieval time, sha256 of download and text, characters and conversion method. Every text opens with "© King's Printer for Ontario, <year>." and a not-an-official-version notice.

| Subject | Instrument | Citation | Consolidated from | Last amendment | Characters |
|---|---|---|---|---|---|
| `taxation-act-2007` | Taxation Act, 2007 | S.O. 2007, c. 11, Sched. A | 2026-07-01 | 2026, c. 2, Sched. 15 | 1,170,847 |
| | General (O. Reg. 37/09) | O. Reg. 37/09 | 2023-08-24 | O. Reg. 306/23 | 195,242 |
| `ontario-works-act-1997` | Ontario Works Act, 1997 | S.O. 1997, c. 25, Sched. A | 2025-07-01 | 2024, c. 28, Sched. 25, s. 8 | 90,052 |
| | General (O. Reg. 134/98) | O. Reg. 134/98 | 2026-08-13 | O. Reg. 276/26 | 212,062 |
| `ontario-disability-support-program-act-1997` | Ontario Disability Support Program Act, 1997 | S.O. 1997, c. 25, Sched. B | 2023-10-26 | 2023, c. 15, Sched. 6 | 68,987 |
| | General (O. Reg. 222/98) | O. Reg. 222/98 | 2026-08-13 | O. Reg. 277/26 | 187,391 |
| `ontario-guaranteed-annual-income-act` | Ontario Guaranteed Annual Income Act | R.S.O. 1990, c. O.17 | 2023-05-18 | 2023, c. 8, Sched. 8 | 68,561 |
| | General (R.R.O. 1990, Reg. 874) | R.R.O. 1990, Reg. 874 | 2000-06-26 | O. Reg. 394/00 | 14,247 |
| | Guaranteed Income Limit (O. Reg. 357/96) | O. Reg. 357/96 | 1996-07-23 | no amendments | 1,786 |

Total 2,009,175 characters. The set-up plan marked the GAINS citation "(verify)": e-Laws confirms it as *Ontario Guaranteed Annual Income Act, R.S.O. 1990, c. O.17*, with two current regulations (R.R.O. 1990, Reg. 874, General; O. Reg. 357/96, Guaranteed Income Limit) and one revoked (R.R.O. 1990, Reg. 873, Forms). The other six citations and URLs in the plan were confirmed as given.

### Why these connect

Claims below cite the deposited text where they were read there; anything not read in a deposited text is marked *unverified (general knowledge)*.

- **Taxation Act, 2007** is the Ontario hub. An individual's Ontario personal income tax is worked out in steps (s. 5 (1)) from a basic tax on the "tax base" (s. 6 (1): brackets at $40,120, $80,242, $150,000 and $220,000), and the "tax base" is the individual's *taxable income* for the year (s. 3 (1)), "Federal Act" meaning the Income Tax Act (Canada) (s. 1 definitions). That taxable income is the federal figure computed under ITA Division B, and that the Canada Revenue Agency assesses and collects Ontario tax under a tax collection agreement: *unverified (general knowledge)*. Whether the bracket amounts in s. 6 (1) are indexed each year: *unverified (general knowledge)*.
- **Ontario Child Benefit** (Taxation Act s. 104): the first listed condition for a month is that the individual is an eligible individual in respect of one or more qualified dependants and is entitled to receive a **Canada child benefit** for that month, the CCB being defined by reference to Subdivision A.1 of Division E of Part I of the federal Act (s. 104 (1)). That the OCB phases out on the same adjusted family net income as the CCB: *unverified (general knowledge)*.
- **Ontario Trillium Benefit** (Taxation Act s. 103.3), with the property and sales tax credit rules in **O. Reg. 37/09** s. 2. That the OTB combines the Ontario energy and property tax credit, the Ontario sales tax credit and the Northern Ontario energy credit: *unverified (general knowledge)*.
- **Ontario Works** (Act + O. Reg. 134/98) and **ODSP** (Act + O. Reg. 222/98) read amounts from the federal and Ontario tax set:
  - payments by Canada not included in income: the GST/HST credit (ITA s. 122.5), the Canada child benefit (ITA s. 122.61, payments from July 2008), the Canada workers benefit (ITA s. 122.7 / 122.71) and the **Canada Disability Benefit** (paragraph 20) -- O. Reg. 134/98 s. 53; O. Reg. 222/98 s. 42;
  - payments by Ontario not included in income include the Ontario Trillium Benefit (Taxation Act s. 103.3) -- O. Reg. 134/98 s. 52 (1) para. 18;
  - EI benefits and CPP benefits are not "earnings" for the earnings rules -- O. Reg. 134/98 s. 49 (3); O. Reg. 222/98 s. 38 (3). That they are therefore deducted from assistance as other income, dollar for dollar: *unverified (general knowledge)*;
  - CPP death, orphan's and disabled contributor's child's benefits are in the same lists of payments by Canada not included in income -- O. Reg. 134/98 s. 53 paras. 4 to 4.2; O. Reg. 222/98 s. 42 paras. 4 to 4.2;
  - a CPP or QPP retirement pension available before 65 is not a financial resource the person must pursue -- O. Reg. 134/98 s. 13 (2) (c); O. Reg. 222/98 s. 11 (2) (c);
  - ODSP: persons receiving **CPP disability benefits** are a prescribed class for s. 3 (1) of the ODSP Act -- O. Reg. 222/98 s. 4 (1) para. 6.
- **GAINS** (Ontario Guaranteed Annual Income Act + regulations) tops up low-income seniors and is built on the federal **Old Age Security Act**: "allowance" is the OAS Part III allowance (Act s. 1 (1)), and "basic monthly income" is computed from the OAS pension and Guaranteed Income Supplement a person receives and from 12 or 24 times the maximum OAS pension and supplement (Act s. 1 (1)). **O. Reg. 357/96** s. 2 sets the guaranteed income limit at $996 plus 12 times the maximum monthly pension plus 12 times the maximum monthly supplement for the quarter, "pension" and "supplement" being the OAS Part I pension and Part II Guaranteed Income Supplement (Act s. 1 (1)). **R.R.O. 1990, Reg. 874** s. 1 (1) counts CPP survivor and disability pensions and unemployment insurance benefits as "private pension income", and excludes OAS benefits. That GAINS is paid automatically to OAS/GIS recipients on CRA income data: *unverified (general knowledge)*.

### Currency

e-Laws currency date 2026-10-14 (from the e-Laws API, read 2026-10-20). The Taxation Act consolidation runs from 2026-07-01, so it includes the 2026 budget amendments enacted by 2026, c. 2. O. Reg. 134/98 and O. Reg. 222/98 were last amended on 2026-08-13 (O. Reg. 276/26, 277/26). O. Reg. 37/09 is consolidated from 2023-08-24; the ODSP Act from 2023-10-26; the GAINS Act from 2023-05-18; its regulations from 2000 and 1996. The Ontario Works Act carries not-yet-in-force amendments (2021, c. 25, Sched. 21: "employment and life stabilization assistance"), printed in the text as notes.

### Gaps

- **Rates that are not in the Acts.** Ontario tax rates beyond the brackets, the LIFT credit, the OCB and OTB amounts and their indexation are spread through the Taxation Act; nothing outside it (budget papers, CRA forms ON428/ON-BEN) has been brought in. Annual indexed figures announced administratively are not in these texts.
- **Other Taxation Act regulations.** Only O. Reg. 37/09 (General) is deposited; other regulations under the Act (for example on specific credits) are not.
- **Ontario Works and ODSP: other regulations.** Only the General regulation under each Act is deposited; other regulations made under the two Acts were not reviewed.
- **French versions.** Only English is deposited; the Acts and O. Reg. 134/98 and 222/98 are bilingual and the French is equally authoritative.
- **O. Reg. 357/96** came from the e-Laws API text, not a Word download (none exists; the Word URL answered 403 and was not retried); see the GAINS subject's `SOURCE-LICENSE.md`.
- **Existing subjects not touched**: the other eleven Ontario subjects remain metadata only.
