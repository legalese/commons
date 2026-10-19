# united-states/

United States (federal) legislation, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md).

The subjects here were laid out on 2026-09-22 for the legislation governing twelve everyday topics. Each was checked against the United States Code, 2024 edition (current through 6 January 2025), as published by the US Government Publishing Office on govinfo.gov (USCODE collection). The Office of the Law Revision Counsel site at uscode.house.gov was not reachable.; the check is recorded in each subject's `registers/source-bundle/*.meta.json`. Nothing is encoded yet. Statute text has been deposited for four of these subjects only, on 2026-10-19, as described in the next section.

**Licence category: open.** Statute text may be deposited and quoted in an encoding, subject to the attribution above.

## Benefits and personal income tax: what was sourced on 2026-10-19

Text was deposited for two connected topics, social security and benefits, and personal income tax. The aim is that one person could get answers from the deposited text: which federal benefits they can get and how much, how much federal income tax they owe, and how the two interact. The text is the Office of the Law Revision Counsel's USLM XML at release point **Public Law 119-121 (current through 9 October 2026)**, downloaded from https://uscode.house.gov/download.html. It was converted to plain text that keeps headings, numbers, section text, tables and source credits, and drops the editorial and statutory notes. Each file has a `.meta.json` with its URL, sha256s and a section count checked against the XML. The terms read (17 U.S.C. 105, the OLRC's robots.txt and download page, and the refusal from ssa.gov) are recorded in each subject's `SOURCE-LICENSE.md`. The deposit is 13 statute files (265 sections, about 3.09 million characters) and 4 files of annually set figures (about 0.20 million characters).

| subject | deposited | why it is here |
| --- | --- | --- |
| [`internal-revenue-code-of-1986`](internal-revenue-code-of-1986) | 26 U.S.C. ch. 1 subch. A part I (ss 1-5), part IV subparts A-C (ss 21-37), part VI (ss 55-59); subch. B parts I-III (ss 61-140), part V (ss 151-153), ss 163, 164, 165, 170, part VII (ss 211-224 and on to 226); ch. 2 (ss 1401-1403); ch. 21 subch. A (ss 3101-3102); ss 6012, 6013, 7703 | what a person owes: rates and brackets, filing status, gross income to taxable income, the standard deduction (s 63), dependants (s 152), the Child Tax Credit (s 24), the EITC (s 32) and the other personal credits, the AMT, who must file. Also the payroll and self-employment taxes that pay for, and earn credit towards, Social Security |
| [`social-security-act`](social-security-act) | 42 U.S.C. ch. 7 subch. II (Title II, ss 401-434), subch. XVI (Title XVI, ss 1381-1385), the Medicare eligibility, enrollment and premium sections of subch. XVIII (ss 1395c, 1395i-2, 1395i-2a, 1395j, 1395o-1395r, 1395w-101), ss 1301, 1305 | what a person can get: OASDI retirement, survivors and disability benefits (insured status, the PIA, reductions, the retirement earnings test in s 403, COLAs in s 415(i)), SSI (eligibility, income and resources, the benefit rate), and the basics of Medicare entitlement (s 426) and enrollment |
| [`food-and-nutrition-act-of-2008`](food-and-nutrition-act-of-2008) | 7 U.S.C. ch. 51, all of it (ss 2011-2036d) | SNAP: household, income and resource tests, deductions, the allotment, work requirements |

**How the provisions connect.** Social Security benefits are taxable income under IRC s 86. The test adds half the benefits to modified AGI and compares the total with base amounts fixed in the statute. That links Title II amounts to s 63 taxable income and the s 1 brackets. FICA (s 3101) and SECA (ss 1401-1402) are charged on the same wages and self-employment income that Title II credits towards quarters of coverage and the PIA (42 U.S.C. 409-415). Both stop at the same contribution and benefit base (42 U.S.C. 430). The retirement earnings test (42 U.S.C. 403(b), (f)) cuts benefits for beneficiaries still working, and that changes both the benefit and the s 86 amount. SSI (Title XVI) counts Title II benefits as unearned income. SNAP (7 U.S.C. 2014) counts both Title II and SSI as income, and it gives elderly and disabled members, whom it defines by reference to Titles II and XVI (7 U.S.C. 2012), their own medical deduction and uncapped shelter deduction. Tax credits interact with benefits as well. 26 U.S.C. 6409 keeps refunds, including EITC and the refundable Child Tax Credit, out of income and resources for federal means-tested programs. Section 6409 itself is **not** deposited and is a candidate for a later pass. Medicare Part A entitlement rides on Title II entitlement (42 U.S.C. 426), and the Part B premium (s 1395r) is collected by deduction from Title II benefits under s 1395s, which is not deposited.

**Numbers set each year** are not in the statute. They are recorded as sourced facts in each subject's `registers/annual-figures.json`, with the official publication deposited beside them: Rev. Proc. 2025-32 for tax year 2026 (irs.gov); the SSA's *Cost-of-Living Increase and Other Determinations for 2026* (90 FR 49047) and the CMS Part B notice for 2026 (90 FR 52063), both from federalregister.gov because ssa.gov refused the client; and USDA's SNAP FY 2027 COLA tables (fna.usda.gov). The 2027 tax-year revenue procedure and the SSA's 2027 Federal Register notice were not yet published on 2026-10-19.

`subject.json` in each of these three subjects was left as indexed on 2026-09-22. The deposit is recorded in `SOURCE-LICENSE.md` and the new `.meta.json` files.

## Topics with no legislation here

- **Insurance claims**: This is mainly state law. The McCarran-Ferguson Act (15 U.S.C. 1011 et seq.; its popular name is confirmed in the govinfo note at 15 U.S.C. 1011) leaves insurance regulation to the states, and claims handling is governed by each state's insurance code and unfair claims settlement practices laws. A narrow federal claims regime exists under the National Flood Insurance Act of 1968 (42 U.S.C. 4001 et seq.; short title confirmed on govinfo) for NFIP flood policies. ERISA governs benefit claims under employer plans.
- **Utility billing**: Retail utility billing is regulated by state public utility commissions under state law. The federal Public Utility Regulatory Policies Act of 1978 (16 U.S.C. 2601 et seq.; short title confirmed on govinfo) only requires states to consider certain retail rate and billing standards. It does not directly govern consumer bills.

## Unemployment insurance and TANF: what was added on 2026-10-19 (UTC)

Many of the state samples under `subjects/us/<st>/` are laws that exist to meet a federal frame:

- **State unemployment compensation laws**, for example `ca/unemployment-insurance-code-division-1-part-1-unemployment`, `ny/labor-law-article-18-unemployment-insurance-law` and `tx/labor-code-title-4-subtitle-a-texas-unemployment-compensation`.
- **State public assistance laws that run TANF**, for example `ca/welfare-and-institutions-code-division-9-part-3-chapter-2`, `ny/social-services-law-article-5-assistance-and-care` and `wa/revised-code-of-washington-title-74-public-assistance-chapter`.

Until this deposit, that federal frame was missing from the federal set. It has now been deposited from the same source and release point as the deposit above: OLRC USLM XML, **Public Law 119-121 (current through 9 October 2026)**. The title zips were downloaded again on 2026-10-19 and were byte-identical to the earlier ones. The terms were read again and are recorded in each subject's `SOURCE-LICENSE.md`. Requests used the client name `legalese-commons-source-fetcher/1.0`, and no refusal was met.

| subject | deposited | what it gives a person |
| --- | --- | --- |
| [`social-security-act`](social-security-act) (added to) | `usc42-ch7-schIV-ptA.txt`: Title IV Part A, 42 U.S.C. 601-619 (TANF). 23 sections, 249,601 characters, plus one operative note | The federal limits every state TANF programme must apply: no individual entitlement (s 601(b)), work requirements and hours (s 607), the 60-month limit and other prohibitions (s 608), and the definition of "assistance" (s 619). |
| [`social-security-act`](social-security-act) (added to) | `usc42-ch7-schIII.txt`: Title III, 42 U.S.C. 501-506. 6 sections, 55,236 characters | What a state UI law must give a claimant for the state to receive administrative grants: payment through public employment offices, "Opportunity for a fair hearing, before an impartial tribunal" (s 503(a)(3)), the able, available and actively seeking work condition (s 503(a)(12)), overpayment recovery (s 503(g)), and the limits on drug testing (s 503(l)). |
| [`internal-revenue-code-of-1986`](internal-revenue-code-of-1986) (added to) | `usc26-ch23.txt`: chapter 23, 26 U.S.C. 3301-3311, the Federal Unemployment Tax Act. 11 sections, 121,989 characters | The federal standards a state UI law must meet to be approved (s 3304(a)): no denial for refusing work in a labour dispute or below prevailing conditions (a)(5), no denial while in approved training (a)(8), extended benefits (a)(11), no denial solely for pregnancy (a)(12), and voluntary income tax withholding from benefits (a)(18). Also the definitions of covered employment and wages (s 3306) and the employer tax (s 3301). |
| [`federal-state-extended-unemployment-compensation-act-of-1970`](federal-state-extended-unemployment-compensation-act-of-1970) (**new subject**) | `euca-1970-note-26usc3304.txt`: Pub. L. 91-373 title II (ss 201-208), as set out in the OLRC note under 26 U.S.C. 3304. 39,379 characters | Extended benefits after regular UI is exhausted. The individual's extended account is the least of 50 percent of regular benefits, 13 times the weekly amount, or 39 times the weekly amount less regular benefits paid (s 202(b)); it is larger in a high-unemployment period. The Act also sets stricter suitable-work and work-search rules (s 202(a)(3)), the 20-weeks-of-work condition (s 202(a)(5)), and the state "on" and "off" indicators that open and close an extended benefit period (s 203). |

**Operative notes kept.** Statutory notes are dropped from every federal deposit, with two exceptions. Both are labelled in the text.

- **TANF extension.** The codified s 603(a)(1) still appropriates the family assistance grant "for each of fiscal years 2017 and 2018". The note under s 601 sets out Pub. L. 119-75, div. J, title III, s 6304 (Feb. 3, 2026), which continues Part A "through December 31, 2026, in the manner authorized for fiscal year 2025". It is the only deposited text that shows TANF is funded in 2026.
- **The Extended Unemployment Compensation Act.** The Act is not classified to any Code section, so the OLRC note is its only Code text. The note reflects amendments through Pub. L. 112-240 (Jan. 2, 2013). The Act is deposited as its own subject because it is a separate Act. The text is unofficial in the plain sense: the Statutes at Large are the law.

**Why these went into existing subjects.** TANF and Title III are titles of the Social Security Act, and FUTA is chapter 23 of the Internal Revenue Code. Each belongs to a body of law that already has a subject here, so the text was added to that subject's source bundle rather than opening a second subject for the same Act. No `subject.json` and no existing text was changed. Each of the two `SOURCE-LICENSE.md` files gained a dated section at the end.

**How it connects.**

- **UI federal frame.** FUTA s 3304(a) sets out what a state law must contain. Title III s 503(a) repeats several of these as conditions of administrative grants, and s 3304(a)(11) brings in EUCA. Together they are the federal floor under every state UI sample. A state sample's rules on work search, suitable work, fair hearings, training and extended benefits should be read against them.
- **UI and the federal tax set.** Unemployment compensation is gross income under 26 U.S.C. 85, which is already deposited in `usc26-ch1-schB-ptI-III.txt`. Section 3304(a)(18) lets a claimant elect withholding.
- **TANF and other benefits.** SNAP treats households in which every member receives TANF as categorically eligible (7 U.S.C. 2014(a), deposited). The SSI text refers to TANF payments in its income rules (42 U.S.C. 1382(c)(5), deposited).
- **TANF and the state samples.** TANF gives no individual entitlement (s 601(b)). Benefit levels, income tests and most other rules are set by state law. A person's TANF outcome is therefore a question for the state samples, within the federal limits deposited here.

**2026 figures.** No annual notice was deposited in this pass. The figures that matter are statutory and are in the deposited text:

- **FUTA.** The rate is 6 percent (s 3301), the credit cap is 90 percent of the tax (s 3302(c)(1)) and the wage base is $7,000 (s 3306(b)(1)). These bear on employers, not on what a claimant receives.
- **TANF grant.** The family assistance grant totals $16,566,542,000 a year (s 603(a)(1)(C)) and is continued for 2026 by the Pub. L. 119-75 note. Each state's share is a ratio fixed by s 603(a)(1)(B), not a published 2026 table, and no individual's benefit depends on it.
- **TANF time limit.** The 60-month limit is in s 608(a)(7).

Two things are set by notice, and neither was deposited:

- **Whether extended benefits are "on" in a given state for a given week.** This does decide a claimant's outcome. EUCA s 203(b)(2) requires the Secretary of Labor to publish each determination in the Federal Register. The Department of Labor also issues a weekly trigger notice (unverified (general knowledge)). Two requests were made to oui.doleta.gov: its robots.txt was empty, and its EUC/EB data page linked only to monthly activity data, not to the trigger notices. The search stopped there. This is a gap: an encoding that answers "can I get extended benefits?" needs the current trigger notice for the claimant's state, taken as a fact.
- **The FUTA credit-reduction states for 2026.** The Department of Labor announces these each November (unverified (general knowledge)). They affect employers only.

**Gaps.**

- **Titles IX and XII of the Social Security Act.** Title IX (42 U.S.C. 1101-1111) and Title XII (1321-1324) were considered and left out. They govern trust fund accounts and loans between federal and state accounts, not any individual's claim. Title XII's effect on employers already appears through s 3302(c)(2). The cross-reference from s 3304(a)(4)(B) to s 903 (42 U.S.C. 1103, Reed Act money) points to text that is not deposited.
- **The rest of Title IV.** Part B (child welfare), Part D (child support) and Part E (foster care) are not deposited. Part D matters where TANF requires assignment of support (s 608(a)(3)).
- **Temporary federal UI programmes.** These are not deposited, whether expired or not reflected in the EUCA note (for example the 2020 pandemic programmes, unverified (general knowledge)).
- **26 U.S.C. 6409.** It is still not deposited, as noted above.
