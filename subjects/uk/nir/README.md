# uk/nir/ — law made for Northern Ireland

This folder holds law made by the **Northern Ireland Assembly** and **Northern Ireland departments**. It also holds Northern Ireland Orders in Council, the legislation.gov.uk type `nisi`.
That follows [`docs/directory-conventions.md`](../../../docs/directory-conventions.md) §2.1: the path names the authority that made the law. ISO 3166-2:GB `GB-NIR` becomes `uk/nir`.

**A Westminster Act for Northern Ireland is filed under `uk/`, not here.** The convention says Westminster legislation sits directly under `uk/`. So the Social Security Contributions and Benefits (Northern Ireland) Act 1992, an Act of the UK Parliament (1992 c. 7), is at [`uk/social-security-contributions-and-benefits-northern-ireland-act-1992`](../social-security-contributions-and-benefits-northern-ireland-act-1992/). It belongs to the set described below.

**Orders in Council are filed here.** The Welfare Reform (Northern Ireland) Order 2015 is an Order in Council, so its maker is formally His (then Her) Majesty in Council. legislation.gov.uk files Orders in Council as Northern Ireland legislation (`nisi`), and they take the place of Assembly legislation on transferred matters. On that basis the Order is filed here. This is a judgment call; see "Check before committing" in the report.

## Social security in Northern Ireland: a connected sample (sourced 2026-10-20)

This is a Priority 3 sample. Social security is a transferred matter in Northern Ireland. The Department for Communities runs it, under a separate statute book that keeps parity with Great Britain. A person in Northern Ireland is governed by these texts, not by the GB texts under `uk/`, which mostly extend to England, Wales and Scotland only.

**Income tax in Northern Ireland is UK-wide.** No devolved income tax rate exists. ITA 2007 provides Scottish rates (s 11A) and Welsh rates (s 11B) and nothing for Northern Ireland (read in the deposited `uk/income-tax-act-2007`). A Northern Ireland taxpayer is therefore covered by the UK set: `uk/income-tax-act-2007`, `uk/income-tax-earnings-and-pensions-act-2003`, `uk/income-tax-trading-and-other-income-act-2005` and `uk/finance-act-2026`. Nothing for income tax is deposited here.

| Subject | What it gives a person | Text |
|---|---|---|
| `uk/social-security-contributions-and-benefits-northern-ireland-act-1992` (1992 c. 7) | The NI counterpart of the SSCBA 1992. Part I: contributions. Part II: contributory benefits. Part III: non-contributory benefits (attendance allowance, carer's allowance s 70). Part V: industrial injuries. Part VII: income-related benefits. Part IX: child benefit (rate, s 141). It extends to Northern Ireland only, except s 116(2) and s 173 (s 173(5)-(6)). | revised to 2026-07-09 |
| `welfare-reform-northern-ireland-order-2015` (S.I. 2015/2006 (N.I. 1)) | The NI counterpart of the Welfare Reform Act 2012. Part 2: universal credit. Part 3: working-age benefits. Part 5: personal independence payment. Part 6: general. | revised to 2026-10-01 |
| `universal-credit-regulations-northern-ireland-2016` (S.R. 2016/216) | Universal credit: entitlement, the award, elements. Reg 38 table: amounts, e.g. standard allowance for a single claimant aged 25 or over, £424.90 per assessment period. Reg 23 table: work allowance, £710 / £427. Earnings, capital and housing costs. | revised to 2026-07-16 |
| `personal-independence-payment-regulations-northern-ireland-2016` (S.R. 2016/217) | PIP: activities, descriptors and points (Sch 1). Reg 24: weekly rates, daily living £76.70 / £114.60 and mobility £30.30 / £80.00. | revised to 2026-04-06 |
| `state-pension-credit-act-northern-ireland-2002` (2002 c. 14 (N.I.)) | Pension Credit for people over State Pension age: entitlement (s 1), guarantee credit (s 2), savings credit (s 3), exclusions (s 4). | revised to 2026-03-15 |
| `social-security-benefits-up-rating-order-northern-ireland-2026` (S.R. 2026/59) | The 2026-27 rates. Art 3, art 4 and Sch 1: benefits under the 1992 (NI) Act. Art 15: PIP. Art 29: state pension credit. Art 32 and Sch 13: UC work allowance and elements. Also income support, housing benefit, JSA and ESA. | revised to 2026-05-05 |

### How the instruments connect

**Within the set.**
- The Order of 2015 creates UC and PIP for Northern Ireland. Its Parts 2 and 5 empower the UC and PIP Regulations (NI) 2016.
- The 1992 (NI) Act and the Pension Credit Act (NI) 2002 carry the older benefits.
- The 2026 up-rating order changes the amounts in all of them, under the Social Security Administration (NI) Act 1992, which is not deposited.
- The revised UC and PIP texts already show the 2026-27 figures. Two checks were made: the reg 23 work allowance reads £710 / £427, as substituted by art 32(1), and PIP reg 24 reads £114.60.
- Schedule 13 of the order does not list the standard allowance. The instrument that set the £424.90 shown in the revised reg 38 table was not identified in this deposit.

**With the UK set.** Each NI text is the parity counterpart of a GB text already deposited under `uk/`:

| Northern Ireland | Great Britain (`uk/`) |
|---|---|
| SSCB (NI) Act 1992 | `social-security-contributions-and-benefits-act-1992` |
| Welfare Reform (NI) Order 2015 | `welfare-reform-act-2012` |
| UC Regulations (NI) 2016 | `universal-credit-regulations-2013` |
| PIP Regulations (NI) 2016 | `personal-independence-payment-regulations-2013` |
| State Pension Credit Act (NI) 2002 | `state-pension-credit-act-2002` |
| Up-rating Order (NI) 2026 | `social-security-benefits-up-rating-order-2026` |

Encoders can diff the pairs. That the provisions run largely in parallel with NI-specific variations is *unverified (general knowledge)*; it was not checked section by section.

Some parts stay UK-wide and are not duplicated here:
- the State Pension under the Pensions Act 2014, whose NI counterpart is the Pensions Act (NI) 2015 (*unverified (general knowledge)*, not deposited);
- the taxability of benefits, under ITEPA 2003 Part 10, which is UK-wide.

## Terms read on 2026-10-20, before fetching

**legislation.gov.uk:**
- `robots.txt`: `User-agent: *`, `Crawl-delay: 5`. It disallows `*/data.pdf`, `*/data.docx` and `/defralex`; `data.xml` and `data.feed` are allowed.
- `/fair-use-policy`: identify yourself with a legitimate user agent; follow robots.txt and its crawl-delay; no more than 1,500 requests in any 5 minutes. Re-use is encouraged.
- `/developer` and `/developer/formats`: the Legislation API is free to reuse, and `data.xml` is the CLML.
- `/help`: legislation.gov.uk holds all secondary legislation from 1987, including NI Statutory Rules.
- The site footer and the OGL v3.0 page: everything here is Crown copyright under the Open Government Licence v3.0. Attribution: "Contains public sector information licensed under the Open Government Licence v3.0".

Every request carried the User-Agent `legalese-commons-source-fetcher/1.0 (+https://github.com/legalese/commons)`. Requests went one at a time, at least 6 seconds apart. None was refused. Two search requests failed at the local network level (DNS / unreachable host), not at the server, and succeeded on retry.

## Currency and outstanding changes (status on legislation.gov.uk, 2026-10-20)

Each `.meta.json` file records:
- the version date and the retrieval time (UTC);
- the sha256 of the download and of the text, and the character count;
- the conversion method;
- the outstanding effects (`outstanding_effects_list`).

Each `.txt` file opens with a header giving the source, the version, the OGL attribution and this status.

| Text | Version | Outstanding (in force, not applied) | Prospective unapplied |
|---|---|---|---|
| SSCB (NI) Act 1992 | 2026-07-09 | **43** | 205 |
| Welfare Reform (NI) Order 2015 | 2026-10-01 | **3** (EEA/Swiss citizens' rights orders, 2020-12-31, against Parts 2 and 5) | 30 |
| UC Regulations (NI) 2016 | 2026-07-16 | **4** (all from the revoked Up-rating (No. 2) Order (NI) 2023, against reg 23, reg 38 and Sch 4 para 13(1); the 2026 figures are already shown) | 0 |
| PIP Regulations (NI) 2016 | 2026-04-06 | **4** (same revoked 2023 order, against reg 24; the 2026 figures are already shown) | 0 |
| State Pension Credit Act (NI) 2002 | 2026-03-15 | **5** (2010-2020, incl. s 3A(5)(a) from 2018) | 13 |
| Up-rating Order (NI) 2026 | 2026-05-05 | 0 | 0 |

Total: **1,630,936 characters** in 6 texts. One of them, the 1992 (NI) Act, is filed under `uk/`.

## Gaps and choices

**Fetched and withdrawn: the State Pension Credit Regulations (Northern Ireland) 2003** (S.R. 2003/28). On legislation.gov.uk its latest revised version is dated **2016-04-06**, and **660** effects in force are listed as not yet applied. That text would mislead anyone using it to calculate Pension Credit now, so it was not deposited. The 2026 guarantee credit amounts are in art 29 of the up-rating order. If the regulations are wanted, take the as-made text plus amendments, or wait for the register to catch up.

**Not taken:**
- the Social Security Administration (NI) Act 1992 (claims, up-rating power, overpayments);
- the Pensions Act (NI) 2015;
- the UC/PIP/JSA/ESA Claims and Payments and Decisions and Appeals Regulations (NI) 2016;
- the NI welfare supplementary payment ("mitigation") schemes;
- the Social Security Benefits Up-rating Regulations (NI) 2026 (S.R. 2026/61).

**Extent versions.** Revised texts may hold more than one extent version of a provision, and prospective provisions; CLML marks these but the text does not. The 1992 (NI) Act's CLML root says `E+W+S+N.I.` because two provisions extend to Great Britain.
