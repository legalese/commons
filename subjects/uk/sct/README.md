# uk/sct/ — law made in Scotland under devolved powers

This folder holds law made by the **Scottish Parliament** and the **Scottish Ministers**.
That follows [`docs/directory-conventions.md`](../../../docs/directory-conventions.md) §2.1.
The path names the authority that made the law, not the place where it applies.
ISO 3166-2:GB `GB-SCT` becomes `uk/sct`. Westminster legislation that applies in Scotland, such as ITA 2007, ITEPA 2003 and the Welfare Reform Act 2012, stays directly under [`uk/`](../README.md).

## Social security and personal income tax in Scotland: a connected sample (sourced 2026-10-20)

This is a Priority 3 sample. It sits beside the UK-wide benefits and income tax set under `uk/` (see [`uk/README.md`](../README.md)) and repeats none of it.
It covers what a person living in Scotland meets on top of, or instead of, the UK-wide rules:

- the Scottish benefits paid by Social Security Scotland, and how much they pay in 2026-27;
- the Scottish income tax rates and bands for 2026-27.

| Subject | What it gives a person | Text |
|---|---|---|
| `social-security-scotland-act-2018` (asp 2018/9) | The framework. Part 1: principles and the charter. Part 2, ss 24-36: the duty to give assistance and the types of assistance, including carer's (s 28), disability (s 31) and early years (s 32). Chapter 3: determination, re-determination and appeal. Part 3, s 79: top-up of reserved benefits. Ss 86A-86B: uprating. | revised to 2026-03-15 |
| `scottish-child-payment-regulations-2020` (SSI 2020/351) | Scottish Child Payment, made under s 79 as a top-up for families receiving a qualifying reserved benefit (reg 14 lists the qualifying kinds of assistance, among them universal credit and state pension credit; reg 12 links the child to the award). Reg 20(1): **£28.20 a week** per child. | revised to 2026-04-01 |
| `disability-assistance-for-children-and-young-people-regulations-2021` (SSI 2021/174) | Child Disability Payment: eligibility, care and mobility components. Reg 23: amounts, e.g. highest care rate £114.60. | revised to 2026-04-06 |
| `disability-assistance-for-working-age-people-regulations-2022` (SSI 2022/54) | Adult Disability Payment, Scotland's replacement for PIP: daily living and mobility components, activities and points. Reg 34: amount and form. | revised to 2026-04-06 |
| `disability-assistance-for-older-people-regulations-2024` (SSI 2024/166) | Pension Age Disability Payment, Scotland's replacement for Attendance Allowance. Reg 6: rates; reg 26: amount. | revised to 2026-04-06 |
| `carers-assistance-carer-support-payment-regulations-2023` (SSI 2023/302) | Carer Support Payment, Scotland's replacement for Carer's Allowance: the cared-for person's qualifying benefit, hours, earnings and education conditions. Reg 16: amount. | revised to 2026-04-05 |
| `social-security-up-rating-miscellaneous-amendments-regulations-2026` (SSI 2026/170) | The 2026-27 amounts. Regs 2-17 substitute the new figures in each set of Scottish benefit regulations, e.g. reg 8 (SCP £27.15 to £28.20) and reg 9 (CDP). The schedule holds the savings. | as made (no revised version) |
| `scottish-rate-resolution-2026-27` (Parliament motion S6M-20844) | The Scottish income tax rates and limits for 2026-27 (see below). | the motion as agreed 2026-02-19 |

### How the instruments connect

**Within this folder.**
- Every set of benefit regulations is made under the 2018 Act: ss 28, 31 and 79, with ss 41-52 (determinations) and s 95 (procedure). Each preamble says so.
- SSI 2026/170 amends the amount provisions of all five sets of benefit regulations deposited here. Because the revised texts here are dated April 2026, those texts already show the 2026-27 figures. The checks made for this deposit: SCP reg 20(1) reads £28.20 and CDP reg 23 reads £114.60.

**With the UK set** (each point read in the deposited texts):
- *Universal Credit Regulations 2013* (`uk/universal-credit-regulations-2013`), reg 2, defines "adult disability payment", "child disability payment" and "carer support payment" by reference to the Scottish regulations deposited here. Those benefits are the passports to UC elements and exemptions.
- The same regulations disregard early years, funeral expense and winter heating assistance under ss 32, 34 and 30 of the 2018 Act as capital (Sch 10, paras 21-24).
- *ITEPA 2003* (`uk/income-tax-earnings-and-pensions-act-2003`) lists carer support payment among the taxable social security benefits in Table A (s 660, with s 661 for the amount).
- Scottish Child Payment is a top-up of reserved benefits such as UC and Pension Credit (`uk/welfare-reform-act-2012`, `uk/state-pension-credit-act-2002`).
- *ITA 2007* (`uk/income-tax-act-2007`), s 11A(1A): "Income tax is charged at Scottish rates on the non-savings income of a Scottish taxpayer". The motion here sets those rates "for the purposes of section 11A".
  - Savings and dividend income, the personal allowance and its taper (s 35) stay UK-wide. They are in the UK set, as is Finance Act 2026 for the UK rates.

### The Scottish rate resolution 2026-27

The Scottish Parliament agreed motion S6M-20844 on 19 February 2026, by 93 votes to 29. It sets the rates and limits on income above the personal allowance:

| Rate | % | Income above the personal allowance |
|---|---|---|
| starter | 19 | up to £3,967 |
| Scottish basic | 20 | £3,967 – £16,956 |
| intermediate | 21 | £16,956 – £31,092 |
| higher | 42 | £31,092 – £62,430 |
| advanced | 45 | £62,430 – £125,140 |
| top | 48 | above £125,140 |

The resolution is **not on legislation.gov.uk**. Its list of document types has no category for Scottish Parliament resolutions. It was taken from the motion page on parliament.scot, the official record of the motion and its result. The deposit keeps the motion text, the status and the vote totals, and omits the per-member vote lists.

The Scottish Parliament's power to set the rates is in Part 4A of the Scotland Act 1998 (s 80C, *unverified (general knowledge)*). That Act is **not deposited** here or in `uk/`.

## Terms read on 2026-10-20, before fetching

- **legislation.gov.uk**
  - `robots.txt`: `User-agent: *`, `Crawl-delay: 5`. It disallows `*/data.pdf`, `*/data.docx` and `/defralex`; `data.xml` and `data.feed` are allowed.
  - `/fair-use-policy`: identify yourself with a legitimate user agent; follow robots.txt and its crawl-delay; stay under 1,500 requests in any 5 minutes. The National Archives "encourage the downloading of data for re-use".
  - `/developer` and `/developer/formats`: the Legislation API is free to reuse; `data.xml` is the CLML of an item.
  - `/help`: legislation.gov.uk holds all secondary legislation from 1987, including SSIs.
  - The site footer, and the OGL v3.0 page at nationalarchives.gov.uk: content under the Open Government Licence v3.0. Attribution: "Contains public sector information licensed under the Open Government Licence v3.0".
- **parliament.scot**
  - `robots.txt`: no Crawl-delay. It disallows `/sitecore`, `/temp/`, `/upload/`, `/xsl/` and similar, not the motion pages.
  - `/about/copyright`: the Scottish Parliament Copyright Licence, "aligned with OGLv3.0". Use is free on condition of attribution: "Contains information licensed under the Scottish Parliament Copyright Licence". It excludes personal data and the SPCB corporate identity, and any use suggesting endorsement, or for party political or advertising-endorsement purposes.

All requests carried the User-Agent `legalese-commons-source-fetcher/1.0 (+https://github.com/legalese/commons)` and were sent one at a time, at least 6 seconds apart per host. None was refused, and no 403, 429 or challenge was met.

## Currency and outstanding changes (status on legislation.gov.uk, 2026-10-20)

Each `.meta.json` records the version date, the retrieval time (UTC), the sha256 of the download and of the text, the character count and the conversion method. It also lists the effects in force but not yet applied (`outstanding_effects_list`). Each `.txt` opens with a header giving the source, the version, the OGL attribution and this status.

| Text | Version | Outstanding effects | Prospective effects |
|---|---|---|---|
| Social Security (Scotland) Act 2018 | 2026-03-15 | **1** (s 81(11)(b)(i)(E), inserted by SSI 2025 cross-border regs, from 2025-11-06) | 96 |
| Scottish Child Payment Regs 2020 | 2026-04-01 | 0 | 0 |
| CDP Regs 2021 | 2026-04-06 | 0 | 0 |
| ADP Regs 2022 | 2026-04-06 | 0 | 0 |
| PADP Regs 2024 | 2026-04-06 | 0 | 0 |
| Carer Support Payment Regs 2023 | 2026-04-05 | 0 | 0 |
| Up-rating (Misc. Amendments) Regs 2026 | as made, 2026-03-26 | n/a (no revised version) | 0 |
| Scottish Rate Resolution 2026-27 | agreed 2026-02-19 | n/a (not legislation; one tax year) | — |

The deposit totals **891,234 characters** in 8 texts.

## Gaps and choices

- **Not taken: the Early Years Assistance (Best Start Grants) (Scotland) Regulations 2018** (SSI 2018/370). These are one-off grants and the sample was capped at eight. The 2026 amounts are in SSI 2026/170, reg 3. They are the next candidate.
- **Not taken: the Social Security Up-rating (Scotland) Order 2026** (SSI 2026/171). It was fetched, inspected and withdrawn. It up-rates the GB benefits still paid in Scotland under the 1992 Act (attendance allowance, severe disablement allowance, carer's allowance, industrial injuries benefit), not the Scottish benefits. SSI 2026/170 is the instrument that sets the Scottish amounts.
- **Not taken:** Scottish Adult DLA, the winter heating, funeral support and young carer regulations, and the 2018 Act's commencement and transitional instruments.
- **Not on legislation.gov.uk:** the Scottish rate resolution (see above).
- Revised texts may hold more than one extent version of a provision, and prospective provisions. CLML marks these but the plain text does not distinguish them; see `text_caveat` in each meta file.
