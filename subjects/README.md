# subjects/

One directory per body of law. **Nineteen subjects are listed as at 2026-09-26**; the first sixteen are described in this paragraph, and the last three, which arrived with the bulk ingestion, below it. Ten are enacted
law, or announced as law: four Singapore subjects, three pieces of Israeli legislation, one
US federal regulation, one Act of the UK Parliament and one Law of Jersey. Of the other six, one is a synthetic insurance
policy, two are commercial standard forms, one is eight private issuers' card T&Cs bundled as
one comparison subject, one is a judge-made doctrine encoded across four jurisdictions, and one
is a body of Israeli **collective agreements** rather than enacted law at all. Each of those six
is flagged below. One subject, `contracts/investment/yc-safe-premoney`, holds source text and no
encoding at all, which the `what it encodes` column says plainly.

| subject | what it encodes | status |
| --- | --- | --- |
| [`uk/child-benefit-rates-regulations-2006`](uk/child-benefit-rates-regulations-2006) | Child Benefit (Rates) Regulations 2006 (S.I. 2006/965) — the whole text as deposited, as a law layer and a seat for a person who claims Child Benefit — encoding `legalese-sonnet-5.5` | `draft` |
| [`uk/social-security-benefits-up-rating-order-2026`](uk/social-security-benefits-up-rating-order-2026) | Social Security Benefits Up-rating Order 2026 (S.I. 2026/148) — the whole text as deposited (the amounts it sets), as a law layer and a seat for a person who receives a UK social security benefit — encoding `legalese-sonnet-5.5` | `draft` |
| [`uk/personal-independence-payment-regulations-2013`](uk/personal-independence-payment-regulations-2013) | Social Security (Personal Independence Payment) Regulations 2013 (S.I. 2013/377) — the whole text as deposited, as a law layer and a seat for a person who claims Personal Independence Payment — encoding `legalese-sonnet-5.5` | `draft` |
| [`us/federal-state-extended-unemployment-compensation-act-of-1970`](us/federal-state-extended-unemployment-compensation-act-of-1970) | Federal-State Extended Unemployment Compensation Act of 1970 (Pub. L. 91-373, title II), as set out in the note under 26 U.S.C. 3304 — the whole text as deposited, as a law layer and a seat for an unemployed worker — encoding `legalese-sonnet-5.5` | `draft` |
| [`sg/succession`](sg/succession) | Wills Act 1838, Intestate Succession Act 1967, Probate and Administration Act 1934 — three Acts against one ontology | `draft` |
| [`sg/child-support`](sg/child-support) | the SG Child Support Package announced at the National Day Rally on 23 August 2026, and childcare leave under the Child Development Co-Savings Act 2001 | `draft` |
| [`sg/pdpa-2012`](sg/pdpa-2012) | Personal Data Protection Act 2012, Part VIA (data breach notification) | `draft` |
| [`sg/penal-code-1871`](sg/penal-code-1871) | Penal Code 1871 — cheating, theft, extortion, robbery, criminal breach of trust, criminal intimidation, hurt (ss 22–25, 321, 323A, 378–384, 390–394, 405–406, 415–420, 503–506) with the form of a charge under CPC 2010 ss 123–126, and s 301 (transferred malice) | `draft` |
| [`us/chubb-hospital-cash`](us/chubb-hospital-cash) | a **synthetic** supplemental hospitalization cash policy — never law, never in force — encoded twice, independently, as evidence in a replication study | `experimental` |
| [`us/regcf`](us/regcf) | SEC Regulation Crowdfunding, 17 CFR Part 227, encoded twice and independently: the eight requirement groups one wiki page presents, with a rule-version axis back to commencement in 2016, and all 22 sections de novo from the eCFR | `draft` |
| [`uk/bna-1981`](uk/bna-1981) | British Nationality Act 1981, section 1 — British citizenship by birth or adoption in the United Kingdom, as in force on 4 July 2026; the demo pipeline's smoke-test subject, "as is traditional" (Sergot et al., 1986) | `draft` |
| [`je/charities-2014`](je/charities-2014) | Charities (Jersey) Law 2014 — the charity test (Articles 5-7, with the definitions it needs), encoded de novo as a cleanroom smoke test, with its DMN/BPMN projections and a three-way comparison against an earlier encoding of the whole Law | `draft` |
| [`br/lei-8213-1991`](br/lei-8213-1991) | Lei nº 8.213/1991 (Planos de Benefícios da Previdência Social) — the whole text as deposited, in Portuguese, in four pieces after a shared core, as a law layer and seat layers for an insured person or a dependant — row `legalese-sonnet-5.5` | `draft` |
| [`br/lei-8742-1993`](br/lei-8742-1993) | Lei nº 8.742/1993 (Lei Orgânica da Assistência Social) — the whole text as deposited, in Portuguese, as a law layer and a seat for a person or family who needs social assistance — row `legalese-sonnet-5.5` | `draft` |
| [`contracts/investment/yc-safe-postmoney`](contracts/investment/yc-safe-postmoney) | the Y Combinator post-money SAFE — six instruments plus four Pro Rata Side Letters, with their User Guide — deposited verbatim, with one encoding row | `draft` |
| [`contracts/investment/yc-safe-premoney`](contracts/investment/yc-safe-premoney) | nothing, and none planned in this repository — **sources only**: the 2013–2018 "original safe", four US variants, recovered from the Internet Archive | `draft` |
| [`contracts/payments/sg-miles-card`](contracts/payments/sg-miles-card) | eight Singapore card issuers' reward-programme T&Cs — DBS yuu, DBS Woman's World, Citi Rewards, HSBC Revolution, UOB Lady's Solitaire, POSB PAssion, plus two flat-rate cards with no held T&C — against one shared ontology, so "which card earns the most on this purchase" can be asked across all eight at once. A second encoding row, `legalese-2026-10`, covers twelve programmes over 28 documents held by link | `draft` |
| [`il/ofek-hadash-2008`](il/ofek-hadash-2008) | the Ofek Hadash reform — the collective agreements, and one budget-law chapter, that determine an Israeli teacher's pay | `draft` |
| [`il/hvac-work-licensing-2025`](il/hvac-work-licensing-2025) | the Refrigeration or Air-Conditioning Systems Work Licensing Law 5785-2025 (licence grades, eligibility with the Second Schedule, validity, foreign experts, commencement) and its Fees Regulations in THREE vintages — the SimpLEX draft shown in Schwartz, Bar-Siman-Tov & Gelbard (2025), as made, as amended — with the paper's own test table run against all three | `draft` |
| [`il/interpretation-law-1981`](il/interpretation-law-1981) | the Interpretation Law 5741-1981 and the surviving provisions of the Interpretation Ordinance [New Version] — how a period "from" a day or "after" an event ends (s. 10, with a caller-supplied rest-day input), "until" (s. 8), the moment a statute binds (s. 21) and when regulations come into force (Ordinance s. 17) — as a reusable time module that other encodings vendor | `draft` |
| [`uk/interpretation-act-1978`](uk/interpretation-act-1978) | Interpretation Act 1978 — counting time, commencement, repeal, service and application, and the rules of construction that compute — row `legalese-sonnet-5.5` | `draft` |
| [`ca/interpretation-act`](ca/interpretation-act) | Interpretation Act (R.S.C., 1985, c. I-21) — the calendar and holidays, counting time, repeal, and the general rules — row `legalese-sonnet-5.5` | `draft` |
| [`ca/bc/interpretation-act`](ca/bc/interpretation-act) | Interpretation Act (British Columbia, RSBC 1996, c. 238) — counting periods of days, weeks, months and years, commencement, repeal and the defined terms — row `legalese-sonnet-5.5` | `draft` |
| [`ie/interpretation-act-2005`](ie/interpretation-act-2005) | Interpretation Act 2005, as enacted — counting periods, commencement, repeal, powers and service, and the time words, with a named refusal wherever the Act has no rule — row `legalese-sonnet-5.5` | `draft` |
| [`us/title-1-united-states-code-general-provisions`](us/title-1-united-states-code-general-provisions) | 1 U.S.C. (Title 1, General Provisions) — chapter 1 rules of construction, chapter 2 forms of acts, international agreements and repeals, chapter 3 codes, evidence of law, and the time rules — row `legalese-sonnet-5.5` | `draft` |
| [`us/ca/interpretation-provisions`](us/ca/interpretation-provisions) | California has no single interpretation act, so this is a **cluster** of 159 sections of the Government, Civil and Civil Procedure Codes — computing time, holidays, the operation of statutes — whose choice of sections is an assumption, not a ruling — row `legalese-sonnet-5.5` | `draft` |
| [`br/lindb-1942`](br/lindb-1942) | Lei de Introdução às Normas do Direito Brasileiro (Decreto-Lei 4.657/1942) — the life of a law, conflict of laws, public law, and the time rules — row `legalese-sonnet-5.5` | `draft` |
| [`il/income-tax-ordinance-new-version`](il/income-tax-ordinance-new-version) | Income Tax Ordinance [New Version] — three rows, one per slice, each against its own nouns: `legalese-2026-10-il-01` (credit points, ss 33A, 34, 36, 36A), `legalese-2026-10-il-02` (s 66, separate calculation for spouses) and `legalese-2026-10-il-03` (ss 120B indexation, 121 individual rates, 121B additional tax); the rest of the Ordinance is not encoded, and the three slices' nouns are not yet reconciled | `draft` |
| [`il/national-insurance-law-consolidated-version-5755-1995`](il/national-insurance-law-consolidated-version-5755-1995) | National Insurance Law [Consolidated Version], 5755-1995 — three rows, one per slice: `legalese-2026-10-il-04` (s 1 definitions, s 334, Schedule J contribution rates, s 337; v0.2.0, repaired against the enacted amending Laws), `legalese-2026-10-il-05` (Schedule K income bounds, s 342 who pays and the employer's deduction, s 348 maximum and minimum) and `legalese-2026-10-il-06` (ss 65 to 68, the child allowance); the rest of the Law is not encoded, the enacted amending Laws are deposited beside the Hebrew text, and each row declares findings about the source's own inconsistencies as expected failures | `draft` |
| [`il/employed-parent-monthly-net`](il/employed-parent-monthly-net) | a **composed** subject, not a statute: one row, `legalese-2026-10-il-07`, that composes the six income-tax and national-insurance rows above into the monthly net income of an employed resident parent with children in a month of 2026, through adapters because this `l4` cannot import across directories; every provision no row encodes is a named input or a named refusal, listed in its GAPS.md | `draft` |
| [`il/penal-law-1977`](il/penal-law-1977) | Penal Law 5737-1977 — theft and robbery (ss 383, 384, 402, 403, 404), encoded in Hebrew with English renderings beside every rule | `draft` |
| [`il/traffic-ordinance-bac`](il/traffic-ordinance-bac) | Traffic Ordinance [New Version] 5721-1961, s 64B(a) "intoxicated" — the drink-driving alcohol thresholds, with reg. 169A of the Traffic Regulations — on the rule-effective axis either side of the 2010 amendment that lowered the threshold for new, young and professional drivers | `draft` |
| [`ca/employment-insurance-act`](ca/employment-insurance-act) | Employment Insurance Act (S.C. 1996, c. 23) and Employment Insurance Regulations (SOR/96-332) — the whole text of both as deposited, in thirteen pieces after a shared core, as a law layer and seat layers for a person who has lost work or cannot work — row `legalese-sonnet-5.5` | `draft` |
| [`ca/canada-pension-plan`](ca/canada-pension-plan) | Canada Pension Plan (R.S.C., 1985, c. C-8) and Canada Pension Plan Regulations (C.R.C., c. 385) — the whole text of both as deposited, in eight pieces after a shared core, as a law layer and seat layers for a worker, self-employed person, survivor, child or person with a disability — row `legalese-sonnet-5.5` | `draft` |
| [`doctrine/contract/unilateral-mistake`](doctrine/contract/unilateral-mistake) | the Singapore doctrine of unilateral mistake in contract — *Chwee Kin Keong v Digilandmall.com* [2005] SGCA 2 — encoded beside three comparators (English common law, *Taylor v Johnson*, Restatement (Second) § 153) against one ontology | `draft` |
| [`comparative/ai-content-labelling`](comparative/ai-content-labelling) | AI-content labelling across three authorities — EU AI Act Art. 50(2) and (4) with the Code of Practice's Measure 1.1, Washington E2SHB 1170 (2026), California Bus. & Prof. Code 22757 as amended by SB 1000 (2026) — encoded against one domain module, run over real and test-signed C2PA files, with a census of where the three disagree; first row under a **proposed** `comparative/` grammar (see its README) | `draft` |
| [`eu/FinMont-demo`](eu/FinMont-demo) | PSD2 strong customer authentication (Commission Delegated Regulation (EU) 2018/389) and refunds and liability under Directive (EU) 2015/2366, orchestrated for one firm — row `legalese-aswathy` | `draft` |
| [`eu/gpai-code-of-practice-2025`](eu/gpai-code-of-practice-2025) | the EU Code of Practice for General-Purpose AI Models, Safety and Security Chapter — Commitment 9, serious incident reporting (Measures 9.1 to 9.4: the four initial-report clocks of 2, 5, 10 and 15 days, intermediate reports every four weeks, the final report 60 days after resolution, five-year retention) and the Code's status as binding only its Signatories, from the provider's seat — row `solo-2026-10`; a **voluntary** code, not legislation | `draft` |
| [`eu/ai-act-2024`](eu/ai-act-2024) | EU AI Act (Regulation (EU) 2024/1689), serious-incident reporting from the provider's seat — Arts 3, 20(2), 51, 52(1), 55(1)(c), 73, 99, 101, 111, 113 — as enacted and as amended by Regulation (EU) 2026/1744 (Art 75(1a): reports to the AI Office) — row `solo-2026-10`; Official Journal licence UNDETERMINED | `draft` |
| [`us/ca/business-and-professions-code-division-8-chapter-25-1-transparency-in-frontier-ai`](us/ca/business-and-professions-code-division-8-chapter-25-1-transparency-in-frontier-ai) | California's Transparency in Frontier Artificial Intelligence Act (SB 53, Bus. & Prof. Code §§ 22757.10–22757.16), critical safety incident reporting from the frontier developer's seat — who is a frontier developer and a large one, the four kinds of critical safety incident, the 15-day report to the Office of Emergency Services (counted under Code Civ. Proc. §§ 12, 12a), the 24-hour disclosure, the federal deemed-compliance route, and the civil penalty, which reaches only large frontier developers — row `solo-2026-10`; public domain | `draft` |
| [`nz/online-safety-minimum-age-bill-2026`](nz/online-safety-minimum-age-bill-2026) | the Online Safety (Minimum Age and Child Safety Risk Assessment) Bill — row `legalese-michael` | `draft` |
| [`au/wa/residential-tenancies-act`](au/wa/residential-tenancies-act) | Residential Tenancies Act 1987 (Western Australia) — row `legalese-michael` | `draft` |
| [`au/wa/cat-act-2011`](au/wa/cat-act-2011) | Cat Act 2011 (Western Australia) and Cat Regulations 2012 — row `legalese-michael`: Part 1, Part 2 Divs 1–3, regs 9, 10, 12 and s 79 in two versions; row `legalese-aswathy`: the whole Act (ss 1–88) and the whole Regulations (regs 1–30, Schedules 1–3), as in force from 25 September 2025, an independent reading with a 16-entry fork register | `draft` |
| [`sg/consumer-protection-fair-trading-act-2003`](sg/consumer-protection-fair-trading-act-2003) | Consumer Protection (Fair Trading) Act 2003 — the whole Act (ss 1–44, First, Second, Fourth and Fifth Schedules), every delegation to regulations a named refusal — row `legalese-aswathy` | `draft` |
| [`sg/business-names-registration-act-2014`](sg/business-names-registration-act-2014) | Business Names Registration Act 2014 — the whole Act (ss 1–45), notice duties as regulative rules, every delegation to regulations an input fact or a named refusal — row `legalese-aswathy` | `draft` |
| [`sg/carriage-by-air-act-1988`](sg/carriage-by-air-act-1988) | Carriage by Air Act 1988 (ss 1–13) and the three texts of the Warsaw Convention in its Schedules — the original, as amended by the Hague Protocol, and as further amended by Montreal Protocol No. 4 — each its own answer, the limits in francs and SDRs, the conversion a named refusal — row `legalese-aswathy` | `draft` |
| [`sg/criminal-procedure-code-2010`](sg/criminal-procedure-code-2010) | Criminal Procedure Code 2010 — the First Schedule (tabular statement of offences under the Penal Code 1871: 478 rows plus the four other-law bands, each with arrest, warrant or summons, bail, court) with ss 2(1) and 7 to 9, and the Second Schedule (laws to which criminal case disclosure procedures apply) with ss 159 and 211A; and the treatment of an offence under the Prevention of Corruption Act 1960 and the Misuse of Drugs Act 1973, read with what each Act says about its own offences (a statement carried in an interface module shared by the three subjects); the rest of the Code and Schedules 3 to 7 are not encoded — row `legalese-aswathy` | `draft` |
| [`sg/evidence-act-1893`](sg/evidence-act-1893) | Evidence Act 1893 — Parts 1 to 4 and both Schedules organised by evidentiary question (relevancy, hearsay, documents, presumptions and burden, witnesses and privilege, examination), ss 117 to 119 not encoded, with an interface module shared with the Criminal Procedure Code subject — row `legalese-aswathy` | `draft` |
| [`sg/prevention-of-corruption-act-1960`](sg/prevention-of-corruption-act-1960) | Prevention of Corruption Act 1960 — Parts 1, 3, 4, 5, 6 and ss 3 and 4: the offences, the s 8 presumption and s 9 deeming, the penalty rules, the powers of arrest, investigation and search, the evidence rules, and a statement to the Criminal Procedure Code subject (ss 32(1), 34); ss 4A to 4F (CPIB superannuation) not encoded — row `legalese-aswathy` | `draft` |
| [`sg/misuse-of-drugs-act-1973`](sg/misuse-of-drugs-act-1973) | Misuse of Drugs Act 1973 — the offences (controlled drugs and psychoactive substances), the presumptions and certificates, the powers of search, arrest and specimen, forfeiture, jurisdiction, and every punishment (the Second Schedule's table in full, 86 rows, with ss 33, 33A, 33B); the substance lists of the First, Third and Fifth Schedules and ss 34 to 52 are not encoded — row `legalese-aswathy` | `draft` |
| [`sg/apportionment-act-1928`](sg/apportionment-act-1928) | Apportionment Act 1928 — the whole Act (ss 1–7): what is apportionable, the day-by-day accrued part, when it is payable and how it is recovered | `draft` |
| [`sg/metrication-act-1970`](sg/metrication-act-1970) | Metrication Act 1970 — the whole Act (ss 1–7) and all four Schedules: SI membership, every unit row, every Third Schedule conversion, the s 7 saving | `draft` |
| [`sg/notaries-public-act-1959`](sg/notaries-public-act-1959) | Notaries Public Act 1959 — the whole Act (ss 1–8): appointment and temporary appointment, when an appointment has effect, oath powers under s 4, revocation, the s 7 offence, rules; refuses before 1 June 2007 | `draft` |
| [`sg/work-injury-compensation-act-2019`](sg/work-injury-compensation-act-2019) | Work Injury Compensation Act 2019 — the whole Act (ss 1–83 with Part 3A, ss 34A–34P, platform workers) and the First to Sixth Schedules, as eight goal-level conclusions: coverage, liability (accidents, platform operators' shares, principals, disease), amount, payment, the claim process, damages, insurance, offences; refuses accidents before 1 January 2025; beside the `naive-2026-10` row (s 7 and First Schedule paras 1–3) | `draft` |
| [`sg/carbon-pricing-act-2018`](sg/carbon-pricing-act-2018) | Carbon Pricing Act 2018 — the whole Act (ss 1–79, First to Fifth Schedules) under one top-level goal (what a facility's operator must do and owe for an emissions year) and seven goals: registration, reporting, the carbon tax, payment and credits, assessments and appeals, records, offences; refuses years before 2024 | `draft` |
| [`sg/income-tax-act-1947`](sg/income-tax-act-1947) | Income Tax Act 1947 — every section given a disposition, under one top-level goal (how much income tax a person owes for a year of assessment, and by when) and ten goals: residence, the charge, exemptions, deductions and allowances, statutory to chargeable income and reliefs, rates, rebates and credits, withholding, filing and disputes, payment, offences; approval-based incentives take the approval as input; YA 2024 onwards | `draft` |
| [`sg/computer-misuse-act-1993`](sg/computer-misuse-act-1993) | Computer Misuse Act 1993 — the whole Act (ss 1–20, both Schedules) under one top-level goal (is the conduct reached, is the offence made out, the most it can cost) and four goals: definitions, offences, punishment, reach and procedure; refuses conduct before 30 December 2025 | `draft` |
| [`sg/child-development-co-savings-act-2001`](sg/child-development-co-savings-act-2001) | Child Development Co-Savings Act 2001 — the whole Act (Parts 1–4, First and Second Schedules) under one top-level goal (what paid leave or Government payment a parent gets for a child, capped how, and what the employer claims back) and eight goals: common measures, the Co-Savings Scheme, maternity, adoption, fathers, shared parental leave, childcare leave, recovery and offences | `draft` |
| [`sg/insurance-act-1966`](sg/insurance-act-1966) | Insurance Act 1966 — the whole Act under two top-level goals: a regulated person (does the Act reach and permit the activity; the offence and its maximum penalty, every penalty in the Act tabled) and a policy (Singapore or offshore, class, validity and recoverable amount, the owner's rights, nominations and who is paid without probate); supervision, appeals, transfers and the s 123 winding-up priority as a fifth goal | `draft` |
| [`vn/decree-67-2023`](vn/decree-67-2023) | Decree 67/2023/NĐ-CP on compulsory motor vehicle owners' civil liability insurance, compulsory fire and explosion insurance, and compulsory insurance in construction investment — encoded in L4 with the Vietnamese quoted line by line from the source (VN-10: the compulsory motor insurance, Articles 5-13, with Annexes I and VI; VN-27: the Motor Vehicle Insurance Fund, Articles 14-22, and the insurer's duties, Article 75); a draft that no Vietnamese-qualified reader has checked, with a fork register and findings in its `NOTES.md` | `draft` |
| [`vn/road-traffic-order-safety-law-36-2024`](vn/road-traffic-order-safety-law-36-2024) | Law 36/2024/QH15 on Road Traffic Order and Safety, from 1 January 2025 — the parts that bear on motor insurance (driving licence classes and validity, alcohol and drugs, vehicle registration and service life), encoded in L4 with the Vietnamese quoted line by line from the source (VN-28); a draft that no Vietnamese-qualified reader has checked, with a fork register and findings in its `NOTES.md` | `draft` |
| [`vn/insurance-business-law-08-2022`](vn/insurance-business-law-08-2022) | Law 08/2022/QH15 on Insurance Business, the whole Act (157 articles) as made, in force from 1 January 2023, and as amended by Law 139/2025/QH15 from 1 January 2026 and 1 July 2026 — three vintages, every article given a disposition (136 encoded, 21 inert), encoded in L4 with the Vietnamese quoted line by line from the gazette (VN-29); a draft that no Vietnamese-qualified reader has checked, with a fork register and findings in its `NOTES.md` | `draft` |
| [`br/codigo-penal-1940`](br/codigo-penal-1940) | the Código Penal, Decreto-Lei 2.848/1940, arts. 1-361 (Parte Geral and Parte Especial) as compiled by Planalto and current through Lei 15.517/2026, in Portuguese with English glosses -- row `legalese-2026-09`: a composer and 169 component modules, a roadmap of 434 units, a register of 126 later norms and court decisions, 423 forks, and 2,148 independent test cases held as `cp-ind-*` files that are red on purpose where they disagree (55). **Not read by a lawyer, and the vintage pass was not done: no prescription is computable for a fact before 4 July 2025** | `draft` |
| [`ca/canada-business-corporations-act`](ca/canada-business-corporations-act) | Canada Business Corporations Act (R.S.C., 1985, c. C-44) — the whole text as deposited, in five pieces after a shared core, as a law layer and seat layers for an incorporator, a director or a shareholder — row `legalese-sonnet-5.5` | `draft` |
| [`uk/universal-credit-regulations-2013`](uk/universal-credit-regulations-2013) | Universal Credit Regulations 2013 (S.I. 2013/376) — the whole text as deposited, in four pieces after a shared core, as a law layer and seat layers for a claimant — row `legalese-sonnet-5.5` | `draft` |
| [`ca/old-age-security-act`](ca/old-age-security-act) | Old Age Security Act (R.S.C., 1985, c. O-9) and Old Age Security Regulations (C.R.C., c. 1246) — the whole text of both as deposited, in three pieces after a shared core, as a law layer and seat layers for a person aged 65 or approaching it — row `legalese-sonnet-5.5` | `draft` |
| [`br/lei-6404-1976`](br/lei-6404-1976) | Lei das Sociedades por Ações (Lei nº 6.404, de 15 de dezembro de 1976) — the whole text as deposited, in seven pieces after a shared core, with Portuguese identifiers, as a law layer and seat layers for a shareholder (acionista) — row `legalese-sonnet-5.5` | `draft` |
| [`jp/ai-promotion-act-2025`](jp/ai-promotion-act-2025) | Japan's Act on Promotion of Research and Development, and Utilization of Artificial Intelligence-related Technology (Act No. 53 of 2025), from the seat of a business operator that develops, provides or uses AI — every Article (1–28) and Supplementary Provision as a row of a provisions table quoted in Japanese and English, with Articles 2, 6, 7, 16, 25 and the commencement provision as rules; finds no reporting duty, penalty, naming or order power, and a duty to cooperate (Art. 7) with no sanction — row `solo-2026-10`; a draft no Japan-qualified reader has checked | `draft` |
| [`kr/ai-framework-act-2025`](kr/ai-framework-act-2025) | Korea's Framework Act on the Development of Artificial Intelligence and Establishment of Trust (Act No. 20676 of 2025, as amended by Act No. 21311 of 2026) with its Enforcement Decree, from the seat of an AI business operator — the Article 32 safety obligation (Decree Art 24: 10^26 FLOPs and two further criteria), the domestic representative (Art 36, Decree Art 29), prior notice to users (Art 31(1)), investigations (Art 40) and fines (Art 43, Decree Annex 2), encoded from the Korean; finds no incident-reporting duty and no period for submitting the Article 32 results — row `solo-2026-10`; a draft no Korea-qualified reader has checked | `draft` |
| [`us/ny/general-business-law-article-44-b-responsible-ai-safety-and-education`](us/ny/general-business-law-article-44-b-responsible-ai-safety-and-education) | New York's Responsible AI Safety and Education (RAISE) Act (Gen. Bus. Law Art. 44-B, §§ 1420–1429, as repealed and re-added by L. 2026, ch. 96, effective 1 January 2027), critical safety incident reporting from the frontier developer's seat — who is a frontier developer or a large one, the four kinds of critical safety incident, the 72-hour report to the office in the Department of Financial Services (counted in minutes from the earlier of determination and reasonable belief, across midnight and daylight saving), the 24-hour imminent-risk disclosure, the federal deemed-compliance route, the Attorney General's $1,000,000 / $3,000,000 penalty (large frontier developers only) — with the 2025 text (L. 2025, ch. 699) deposited for comparison — row `solo-2026-10`; from the Assembly's bill prints, not checked against the official Laws of New York; source terms UNDETERMINED | `draft` |
| [`uk/criminal-damage-act-1971`](uk/criminal-damage-act-1971) | Criminal Damage Act 1971 — the offences, lawful excuse, the ceilings on conviction on indictment and the Act's extent (ss 1 to 7, 9 to 12 in part), for the person suspected or charged — row `legalese-sonnet-5.5` | `draft` |
| [`uk/offences-against-the-person-act-1861`](uk/offences-against-the-person-act-1861) | Offences against the Person Act 1861 — 40 sections (ss 4, 5 as to penalty, 9, 10, 16 to 18, 20 to 40, 42, 44, 45, 47, 57 to 60, 64, 65, 68 and 78), for the person suspected or charged, with the date of enactment kept as data — row `legalese-sonnet-5.5` | `draft` |
| [`uk/fraud-act-2006`](uk/fraud-act-2006) | Fraud Act 2006 — ss 1 to 9, 11 to 13 and 15(1) to (3), with the parts of Schedules 1 and 2 that bear on liability and the date of enactment, for the person suspected or charged — row `legalese-sonnet-5.5` | `draft` |
| [`au/acts-interpretation-act-1901`](au/acts-interpretation-act-1901) | Acts Interpretation Act 1901 (Australia) — the sections that compute a deadline, a day, a moment, a permission or a validity, for a person with a time limit to meet — row `legalese-sonnet-5.5` | `draft` |
| [`uk/theft-act-1968`](uk/theft-act-1968) | Theft Act 1968 — the whole Act as shown in the deposited text, for the person suspected or charged, as a law layer and a seat layer — row `legalese-sonnet-5.5` | `draft` |
| [`uk/state-pension-credit-act-2002`](uk/state-pension-credit-act-2002) | State Pension Credit Act 2002 — ss 1 to 10, 12(1), 15 to 17, 18A and 22 in part, and the schedule paragraphs its encoding lists, for a person of an age to claim — row `legalese-sonnet-5.5` | `draft` |
| [`ca/canada-disability-benefit-act`](ca/canada-disability-benefit-act) | Canada Disability Benefit Act (S.C. 2023, c. 17) and the Canada Disability Benefit Regulations (SOR/2025-35) — Act ss 4 to 9, 10.1 and 14 and most of the Regulations, for a person with a disability who may apply — row `legalese-sonnet-5.5` | `draft` |
| [`uk/state-pension-regulations-2015`](uk/state-pension-regulations-2015) | State Pension Regulations 2015 (S.I. 2015/173) — regulations 1(3), 1(5), 1A, 2 to 13 and 15 to 39 and the Schedule's inserted regulation 6, for a person who is or will become entitled to the State Pension, with the dates made and in force kept as data — row `legalese-sonnet-5.5` | `draft` |

Two subjects above carry a second, independent row from the bulk ingestion: `sg/penal-code-1871/encodings/legalese-aswathy/` (the whole Code, Chapters 1–23) beside the `legalese` row, and `il/hvac-work-licensing-2025/encodings/legalese-michael/` (the whole Law, in Hebrew-commented English L4; an external contribution made with ChatGPT, without Legalese's pipeline skill; that subject's `encodings/README.md` says which row is which) beside `legalese` and `legalese-he`. Rows are equal; neither is primary.
`sg/penal-code-1871` also has a third row, `encodings/legalese-whole-code/` (2026-09-26): the whole Code again, made in one run of nine agents to the charge generator's contract, with 443 sections encoded and 42 deferred for time.

`sg/child-support` is the odd one and worth knowing about before you read it: its primary
source is an **announcement, not an enactment**. No Bill has been introduced, so its
rule-version axis carries *administered today* against *announced*, and the statute the
announcement would amend is recorded as the source bundle's `instrument`.

`sg/penal-code-1871` grew on 2026-09-17 from one section to ten modules, encoded in inert style
for the charge-generator demo, with a seven-case bench of reported judgments asserted inside the
modules rather than a `cases/` directory; it gained section 393 and a `projections/` directory on
2026-09-21, and still has no `registers/`, `report/` or `gates/`. The projections are the
repository's **first generated ladder figures** — six robbery decisions read out of the module
through `jl4-lsp` in four carriers each, one of them prose, so the section's elements can be laid
beside a textbook's list without anyone transcribing them. It is filed as a
subject rather than an l4-ide example because it is a body of law, and this is where bodies
of law live; its `NOTES.md` states what the sidecar does not carry. It is also the row whose
**source terms bite hardest**: inert style works by quoting the statute inline, so unlike
`sg/pdpa-2012` it reproduces its section verbatim rather than paraphrasing it. See that
row's `SOURCE-LICENSE.md`.

`us/chubb-hospital-cash` is the row that most needs its label read. It is the first `experimental`
row, and the status is not a weaker `draft` — it marks a different kind of thing. **The instrument is
synthetic: fictional parties, never issued, never in force, never construed.** It was invented by
researchers as a benchmarking target, and it is filed here because it is a body of contractual rules
that has been encoded, not because anyone is subject to it. It is also the first row whose source
terms are **determined** rather than undetermined — the policy originates in a CC BY 4.0 article, so
attribution is required and is recorded in `NOTICE`. Two independent encodings sit side by side under
`encodings/`, written blind to each other and to the benchmark's answer key, because the comparison
between them is the evidence. Read its `NOTES.md` before drawing any conclusion from it: the source
text was modified before publication in a way that removed the operative insuring clause.

`doctrine/contract/unilateral-mistake` is the first row under a **third grammar**, and the first
whose subject is **judge-made law**. Everything else here is a text somebody enacted or drafted;
this is a rule that exists only as a line of holdings, and the encoding's point is comparative —
Singapore's equitable limb requires constructive knowledge **plus** an additional element of
impropriety, and that formula is visible as distinctive only when England's, Australia's and the
American rule are computed on the same facts beside it. Filing it under `sg/` would have made
three of its four modules trespassers; filing four sibling subjects would have left the comparison
homeless. So it seeds `doctrine/<area>/<leaf>/`, with a controlled area vocabulary in
[`doctrine/AREAS.md`](doctrine/AREAS.md) on the model of `contracts/GENRES.md`. **That grammar is a
proposal, not a ruling** — `docs/directory-conventions.md` §12 owns the rewrite and this row has
not amended it; the argument is set out in the row's `NOTES.md` §1 so a reviewer can disagree with
it rather than reconstruct it.

Two things about that row need reading before it is relied on. Its **comparators are read at second
hand**: the English and Australian authorities were never fetched from their own reports, only from
*Chwee Kin Keong*'s account of them, and the American column states the Restatement rule rather than
the law of any State. And it is the first row whose registers had to be **bent to fit** — a judgment
has no in-force banner and no amendment markers, so the source bundle declares no annotations and
the sweep register has nothing to dispose of; both say so in their own notes, and both record the
schema vocabulary gaps as upstream candidates rather than papering over them.

`contracts/payments/sg-miles-card` is the first subject under a **new genre**, `payments/`,
seeded in the same change (`contracts/GENRES.md` records why). It is also the first `contracts/`
row that is a **bundle**: eight instruments by five different issuers, filed as one leaf against
one shared domain module and composer, because the point of the encoding is a comparison across
all eight (Meng ruled this shape on 2026-09-21, the day it was deposited) — the same reason
`sg/succession` bundles four Acts and `il/ofek-hadash-2008` bundles several collective agreements.
Its `subject.json.encodings_note` and its row's `NOTES.md` §0 both state the argument in full.
**HG1 was waived, not signed** — `status: draft` is not a weaker claim about the encoding's
correctness than usual; it specifically reflects that nobody has checked its isomorphism to the
eight source texts yet, notwithstanding that every machine gate (848 scenario assertions, a
Catala projection with zero refusals) passed. See `encodings/legalese/gates/HG1.waiver.md`.

The two `contracts/` rows are the first entries under a **second grammar**. Everything above them
is enacted law, filed by the authority that enacted it — `sg/`, `us/`, an ISO 3166-1 code. A
commercial instrument has no promulgating authority and often no jurisdiction at all until a
governing-law clause supplies one, so it is filed by **genre** instead:
`contracts/<genre>/<leaf>/`, with `governing_law` as a `subject.json` field rather than a
directory. The genre vocabulary is controlled — insurance, investment, leasing, lending — and
lives in [`contracts/GENRES.md`](contracts/GENRES.md), which these rows seed. See
`docs/directory-conventions.md` §3, and §8.4 of that document, which names
`yc-safe-postmoney` as its worked example of a standard form. **That document is not on this
branch**: it lives on `docs/directory-conventions` and is unlinked here for that reason, so
read it with `git show docs/directory-conventions:docs/directory-conventions.md`.

Both SAFE rows carry the publisher's text byte-exact, a Markdown rendering of it, the header and
footer strings pandoc throws away (which is where the licence and the version stamp live), digests
for everything, and a validated source bundle. **`yc-safe-premoney` stops there** — no `encodings/`
directory, and none planned in this repository; its `NOTES.md` says why. `yc-safe-postmoney` adds
one encoding row and a fork register, and neither row has `projections/`, `report/` or `gates/`, so
no human review has been sought for either. They also differ from each other in the way that matters
most for a corpus: `yc-safe-postmoney` is the second row
here whose source terms are **determined** — CC BY-ND 4.0, printed in the form's own footer, so
attribution is a condition and is recorded in `NOTICE` — while `yc-safe-premoney` carries **no
terms at all**, because the licence footer was added in 2018 and those captures are from 2014.
Read each row's `SOURCE-LICENSE.md` before deriving anything from it. `yc-safe-postmoney`'s also
records an unresolved question: whether an L4 formalisation of a form is an "adaptation" under a
NoDerivatives licence.

`il/penal-law-1977` is the second Israeli row and the first that is enacted law. Its source --
the consolidated text of the Penal Law, 651 sections, deposited 2026-09-16 -- had sat in the tree
with no encoding beside it until 2026-09-21, when five of those sections were encoded: theft, and
the robbery sub-chapter that builds on it. The row exists to be read **beside**
`sg/penal-code-1871`, whose robbery module encodes the same crime from the other colonial code,
and its `NOTES.md` carries an element-by-element comparison of the two. Two things about it are
unlike every other row here. It is written in **Hebrew** -- identifiers, section titles and the
default natural-language rendering of every rule -- with an English rendering tagged beside each
one, so the same source produces a whole document in either language. And it carries the same two
open source-terms questions as `il/ofek-hadash-2008`, for the same reason: the consolidated text
was read from a Wikisource volunteer project rather than from *Reshumot*, which is geo-blocked and
publishes no consolidation. Its `SOURCE-LICENSE.md` sits beside `source/` at the subject level
rather than inside the encoding row.

`il/ofek-hadash-2008` is the first row whose subject is **not enacted law**, and the label
should be read before the row is. Ofek Hadash is a **collective agreement** between the State
of Israel and the Teachers' Union, layered with later agreements, binding decisions of a joint
bipartite follow-up committee, and ministry circulars. The one Act in the picture — Chapter 9
of the 2025 budget law — works by referring back to an *approved collective agreement* rather
than setting a rate itself, so even the statutory layer routes through the agreements. It is
filed under `il/` because the State is one of the two parties and the Knesset is the authority
for the fiscal chapter; `contracts/` would have been wrong, because this is not a commercial
instrument and it governs a whole profession.

It is also the first row read **entirely from a third-party corpus** rather than from an
official publisher, and the first whose `SOURCE-LICENSE.md` therefore carries **two** open
questions instead of one: what may be done with the instruments, and what may be done with the
compilation that transcribed them. Nothing was fetched from the Ministry of Education or from
*Reshumot*; the digests are over the corpus's published HTML. Its `/akn/il/…` identifiers,
which appear throughout that row's document register, are a convention of that corpus and are
**not citable outside it** — the corpus says so itself, and the row repeats it rather than
letting the identifiers pass as citations. Two further things distinguish it: all 282 documents
of the source corpus were read and are deposited as a per-document register, which is what
surfaced a January 2025 committee decision as the authoritative source for salary tables
otherwise attributed to an October 2022 agreement; and it is the first row to carry an
**executed** foreign-notation projection — six worked cases run through `catala interpret`
against the emitted Catala module, reproducing the figures the L4 asserts.

`us/regcf` was encoded in `legalese/l4-ide` and deposited here on 2026-09-23, byte-identical, with
its history left in l4-ide, which vendors it back into its regression corpus once its
`etc/canon-pin.json` names a commit that contains it. Its `README.md`, `PROJECTIONS.md`
and ladder figures stayed in l4-ide, because they describe l4-ide's own projections of the
corpus, and each row's `NOTES.md` says where they are. `uk/bna-1981` and `je/charities-2014` were
deposited from l4-ide the same day, in the same way, and nothing of either stayed behind.
`je/charities-2014` is the first row under a Crown Dependency. Its code, `je`, is Jersey's own
ISO 3166-1 alpha-2 code: Jersey legislates for itself, so the Law is filed under Jersey and not
under `uk/`.

*(This paragraph read "Empty at this writing" until 2026-08-25, by which point three
subjects had landed; a fourth landed on 2026-08-27, a fifth on 2026-08-31, the two
`contracts/` rows on 2026-09-04, and the first `doctrine/` row and the first `il/` row on
2026-09-07. A README that
describes a directory it no longer matches is worse than none, because it is believed.)*

## The bulk ingestion, by jurisdiction

Every jurisdiction directory uses its ISO 3166 code (`docs/directory-conventions.md` §2): countries and the EU at the top (`sg`, `il`, `nz`, `eu`), subdivisions nested beneath them (`au/wa`, `us/ca`, `ca/on`).
Most subjects below hold source text and metadata only; where one had already been encoded, the encoding is a row under its `encodings/`, as above.

One directory per jurisdiction, then one directory per body of law inside it.

| jurisdiction | contents |
| ------------ | -------- |
| [`au/wa/`](au/wa/) | Western Australian Acts |
| [`eu/`](eu/) | European Union Regulations and Directives |
| [`sg/`](sg/) | Singapore Acts |
| [`sg/sale-of-food-act-1973`](sg/sale-of-food-act-1973) | Sale of Food Act 1973 — the whole Act under one top-level goal (does the Act reach the article, is an offence committed, does a defence answer it, the most it can cost) and four goals: what the Act reaches (food, unsafe, unsuitable, adulterated, non-retail business), offences and penalties, defences and liability, enforcement and procedure | `draft` |
| [`sg/housing-and-development-act-1959`](sg/housing-and-development-act-1959) | Housing and Development Act 1959 — the whole Act under one top-level goal (may the person buy the flat, is the dealing lawful, is it safe from creditors, may the Board re-enter, acquire or penalise instead) and six goals: buying, dealings, the Board's remedies and periods, upgrading, the Board, offences and service | `draft` |
| [`sg/building-strata-management-act-2004`](sg/building-strata-management-act-2004) | Building (Strata Management) Act 2004 — the whole Act under one top-level goal (is the matter validly decided, may this person sit on the council, what does a proprietor in arrears face) and six goals: resolutions and meetings, the owner developer, the management corporation, the council, Strata Titles Boards, offences and service | `draft` |
| [`sg/goods-and-services-tax-act-1993`](sg/goods-and-services-tax-act-1993) | Goods and Services Tax Act 1993 — the whole Act under one top-level goal (is GST charged on this supply, when, at what rate, how much, who accounts) and six goals: the charge, registration, input tax, assessment and appeal, collection and rulings, penalties | `draft` |
| [`au/`](au/) | Commonwealth of Australia Acts |
| [`au/nsw/`](au/nsw/) | New South Wales Acts |
| [`au/vic/`](au/vic/) | Victorian Acts -- **not openly licensed; metadata only** until permission is obtained |
| [`au/qld/`](au/qld/) | Queensland Acts |
| [`au/sa/`](au/sa/) | South Australian Acts |
| [`au/tas/`](au/tas/) | Tasmanian Acts |
| [`nz/`](nz/) | New Zealand Acts and Bills |
| [`nz/accident-compensation-act-2001`](nz/accident-compensation-act-2001) | Accident Compensation Act 2001 (NZ) — the whole Act under one top-level goal (is there cover, what class of injury, which Account pays, what weekly compensation follows) and six goals: cover, claims, entitlements, reviews and appeals, levies, offences — row `legalese-aswathy` | `draft` |
| [`nz/civil-aviation-act-2023`](nz/civil-aviation-act-2023) | Civil Aviation Act 2023 (NZ) — passenger compensation for delay in domestic carriage under one top-level goal (applies, carrier answerable, most payable, time limit) and three goals — row `legalese-aswathy` | `draft` |
| [`nz/consumer-guarantees-act-1993`](nz/consumer-guarantees-act-1993) | Consumer Guarantees Act 1993 (NZ) — the whole Act under one top-level goal (for a supply and a failure, does the Act give redress, and which remedies does the consumer have against the supplier and the manufacturer) and four goals: scope, goods and the supplier, goods and the manufacturer, services — row `legalese-aswathy` | `draft` |
| [`nz/credit-contracts-and-consumer-finance-act-2003`](nz/credit-contracts-and-consumer-finance-act-2003) | Credit Contracts and Consumer Finance Act 2003 (NZ) — cancellation, interest, high-cost credit, hardship and statutory damages under one top-level goal and four goals — row `legalese-aswathy` | `draft` |
| [`nz/customs-and-excise-act-2018`](nz/customs-and-excise-act-2018) | Customs and Excise Act 2018 (NZ) — Customs value, duty, payment, late payment penalties and refunds under one top-level goal (Customs value, duty, payment date, penalties) and four goals: Customs value, duty and its payment, late payment penalties, refunds — row `legalese-aswathy` | `draft` |
| [`nz/electricity-industry-act-2010`](nz/electricity-industry-act-2010) | Electricity Industry Act 2010 (NZ) — the supply obligation, the dispute resolution scheme and enforcement limits under one top-level goal and three goals (billing is in the Participation Code, not the Act) — row `legalese-aswathy` | `draft` |
| [`nz/employment-relations-act-2000`](nz/employment-relations-act-2000) | Employment Relations Act 2000 (NZ) — dismissal and personal grievances under one top-level goal (barred, raised in time, deadlines, remedies, reimbursement) and three goals: trial periods and high earners, raising and time limits, remedies — row `legalese-aswathy` | `draft` |
| [`nz/fair-trading-act-1986`](nz/fair-trading-act-1986) | Fair Trading Act 1986 (NZ) — under one top-level goal (for a piece of conduct, does it contravene the Act, is it an offence and up to what fine, may a party seek an order under s 43 and by when) and four goals: conduct, consumer transactions and auctions, information and safety, enforcement — row `legalese-aswathy` | `draft` |
| [`nz/holidays-act-2003`](nz/holidays-act-2003) | Holidays Act 2003 (NZ) — the whole Act under one top-level goal (for a holiday or leave event, is the employee entitled, how much must the employer pay, when, and is an alternative holiday earned) and six goals: pay measures, annual holidays, public holidays, sick and bereavement leave, family violence leave, enforcement and records — row `legalese-aswathy` | `draft` |
| [`nz/immigration-act-2009`](nz/immigration-act-2009) | Immigration Act 2009 (NZ) — eligibility, unlawful status and work, deportation liability and employers under one top-level goal (barred from a visa, unlawful and barred from working, appeal deadline, s 161 liability) and four goals — row `legalese-aswathy` | `draft` |
| [`nz/income-tax-act-2007`](nz/income-tax-act-2007) | Income Tax Act 2007 (NZ) — personal income tax of a natural person under one top-level goal (residence, taxable income, liability, independent earner tax credit, terminal tax or refund) and four goals: residence, taxable income and liability, credits, secondary tax codes — row `legalese-aswathy` | `draft` |
| [`nz/kiwisaver-act-2006`](nz/kiwisaver-act-2006) | KiwiSaver Act 2006 (NZ) — Parts 1-3 and the scheme rules under one top-level goal (for a person, an employment and a pay: automatic enrolment and the opt-out window, the deduction and compulsory employer contribution, and the most that may be withdrawn) and three goals: membership, contributions, withdrawals — row `legalese-aswathy` | `draft` |
| [`nz/minimum-wage-act-1983`](nz/minimum-wage-act-1983) | Minimum Wage Act 1983 (NZ) — the whole Act under one top-level goal (does the Act apply, which minimum rate governs, what must be paid after the deductions the Act allows, how much is owed) and five goals: the rate, the payment, enforcement, hours, administration — row `legalese-aswathy` | `draft` |
| [`nz/new-zealand-superannuation-and-retirement-income-act-2001`](nz/new-zealand-superannuation-and-retirement-income-act-2001) | New Zealand Superannuation and Retirement Income Act 2001 (NZ) — entitlement, rates, absence and the Fund's computable rules under one top-level goal (for a person on a date: entitled, from when, which rate) and three goals: entitlement, absence and payment overseas, the rates and the Fund — row `legalese-aswathy` | `draft` |
| [`nz/parental-leave-and-employment-protection-act-1987`](nz/parental-leave-and-employment-protection-act-1987) | Parental Leave and Employment Protection Act 1987 (NZ) — the whole Act under one top-level goal (for a person and a child, which leave may they take and for how long, are they entitled to parental leave payments, at what rate and for how many weeks) and four goals: eligibility, leave, notices and protection, payments — row `legalese-aswathy` | `draft` |
| [`nz/residential-tenancies-act-1986`](nz/residential-tenancies-act-1986) | Residential Tenancies Act 1986 (NZ) — the computable rules for tenancy steps under one top-level goal (does the Act apply, is the step lawful, its key date) and five goals: application and working days, bonds and rent, termination, entry and boarding houses, the Tribunal — row `legalese-aswathy` | `draft` |
| [`nz/social-security-act-2018`](nz/social-security-act-2018) | Social Security Act 2018 (NZ) — the three main benefits for adults under one top-level goal (entitled, weekly rate after the income test, commencement) and three goals: general requirements, entitlement, rate and commencement — row `legalese-aswathy` | `draft` |
| [`nz/tax-administration-act-1994`](nz/tax-administration-act-1994) | Tax Administration Act 1994 (NZ) — PAYE reporting, returns and penalties under one top-level goal (must they file, when, late filing and late payment penalties, shortfall penalty, time bar) and four goals: employment income information and tax codes, returns and the time bar, late filing and payment, shortfall penalties — row `legalese-aswathy` | `draft` |
| [`nz/telecommunications-act-2001`](nz/telecommunications-act-2001) | Telecommunications Act 2001 (NZ) — copper withdrawal, dispute appeals and code periods, and late levy interest under one top-level goal and three goals (consumer terms are in codes, not the Act) — row `legalese-aswathy` | `draft` |
| [`nz/wages-protection-act-1983`](nz/wages-protection-act-1983) | Wages Protection Act 1983 (NZ) — the whole Act under one top-level goal (were the deductions lawful, were the wages paid in a lawful manner, did the employer contravene the Act, what may be recovered under s 11) and four goals: deductions and overpayments, the manner of payment, recovery, premiums and penalties — row `legalese-aswathy` | `draft` |
| [`uk/communications-act-2003`](uk/communications-act-2003) | Communications Act 2003 — ending a phone or broadband contract early, TV licensing, and misuse of a network, from the individual end-user's seat — row `legalese-aswathy` | `draft` |
| [`uk/consumer-insurance-disclosure-and-representations-act-2012`](uk/consumer-insurance-disclosure-and-representations-act-2012) | Consumer Insurance (Disclosure and Representations) Act 2012 — does the Act apply, qualifying misrepresentations and their class, and the insurer's remedies under Schedule 1 — row `legalese-aswathy` | `draft` |
| [`uk/consumer-rights-act-2015`](uk/consumer-rights-act-2015) | Consumer Rights Act 2015 — the short-term right to reject, the six-month presumption, the final right to reject and refund, and remedies for services — row `legalese-aswathy` | `draft` |
| [`uk/customs-and-excise-management-act-1979`](uk/customs-and-excise-management-act-1979) | Customs and Excise Management Act 1979 — seizure, claims and condemnation (Schedule 3), fraudulent evasion and its maximum penalties (s 170, Schedule 1), and time limits for proceedings (s 146A) — row `legalese-aswathy` | `draft` |
| [`uk/electricity-act-1989`](uk/electricity-act-1989) | Electricity Act 1989 — connection, disconnection for non-payment and entry, consumer redress orders and resale prices, from the electricity customer's seat — row `legalese-aswathy` | `draft` |
| [`uk/employment-rights-act-1996`](uk/employment-rights-act-1996) | Employment Rights Act 1996 — minimum notice, unfair dismissal (qualifying period, time limit with early conciliation, basic award) and the statutory redundancy payment — row `legalese-aswathy` | `draft` |
| [`uk/employment-rights-act-2025`](uk/employment-rights-act-2025) | Employment Rights Act 2025 — statutory sick pay as amended, the six-month unfair dismissal qualifying period, and guaranteed-hours complaint time limits — row `legalese-aswathy` | `draft` |
| [`uk/gas-act-1986`](uk/gas-act-1986) | Gas Act 1986 — connection, cutting off for debt and entry, consumer redress orders and resale prices, from the gas consumer's seat — row `legalese-aswathy` | `draft` |
| [`uk/housing-act-1988`](uk/housing-act-1988) | Housing Act 1988 — s 8 notice periods and Ground 7A timing, s 21 notices in England, and statutory damages for unlawful eviction — row `legalese-aswathy` | `draft` |
| [`uk/immigration-act-1971`](uk/immigration-act-1971) | Immigration Act 1971 — right of abode and the need for leave, continuation of leave (s 3C), and the maximum sentences and time limits for ss 24 and 24B offences — row `legalese-aswathy` | `draft` |
| [`uk/immigration-asylum-and-nationality-act-2006`](uk/immigration-asylum-and-nationality-act-2006) | Immigration, Asylum and Nationality Act 2006 — illegal working: employment contrary to s 15, the civil penalty with its notice and appeal dates, and the s 21 offence — row `legalese-aswathy` | `draft` |
| [`uk/income-tax-act-2007`](uk/income-tax-act-2007) | Income Tax Act 2007 — personal allowance, income tax on wages, savings and dividends, and the marriage allowance, from the individual taxpayer's seat — row `legalese-aswathy` | `draft` |
| [`uk/income-tax-earnings-and-pensions-act-2003`](uk/income-tax-earnings-and-pensions-act-2003) | Income Tax (Earnings and Pensions) Act 2003 — company car and cheap loan benefits, and termination payments (post-employment notice pay and the £30,000 threshold), from the employee's seat — row `legalese-aswathy` | `draft` |
| [`uk/insurance-act-2015`](uk/insurance-act-2015) | Insurance Act 2015 — application, the duty of fair presentation and the insurer's remedies, warranties, risk-reducing terms and fraudulent claims, and the amount payable on a claim — row `legalese-aswathy` | `draft` |
| [`uk/landlord-and-tenant-act-1985`](uk/landlord-and-tenant-act-1985) | Landlord and Tenant Act 1985 — the s 11 repairing and s 9A fitness covenants, service charges after ss 19, 20 and 20B, and landlord information deadlines — row `legalese-aswathy` | `draft` |
| [`uk/national-minimum-wage-act-1998`](uk/national-minimum-wage-act-1998) | National Minimum Wage Act 1998 (UK) — who qualifies, s 17 arrears and access to records under one top-level goal (qualifies, additional remuneration owed, records production and complaint deadlines, the s 11 award) — row `legalese-aswathy` | `draft` |
| [`uk/nationality-and-borders-act-2022`](uk/nationality-and-borders-act-2022) | Nationality and Borders Act 2022 — the refugee determination (ss 30-35), Article 31(1) immunity conditions (s 37), and priority removal notices and late evidence — row `legalese-aswathy` | `draft` |
| [`uk/network-and-information-systems-regulations-2018`](uk/network-and-information-systems-regulations-2018) | The Network and Information Systems Regulations 2018 (S.I. 2018/506) — incident notification from the seat of a company providing an AI model service: whether it is an RDSP or an OES (reg 1, with 'cloud computing service' as an explicit yes/no/cannot-say input), whether and whom it must notify (regs 3, 11, 12), the 72-hour clocks to the minute, and the penalty ceilings of £1m, £8.5m and £17m (regs 17-18); **not an AI law**; finds no UK AI-specific incident duty, and the Cyber Security and Resilience Bill not yet law — row `solo-2026-10`; source an **aid** (Lex API), not checked against the official text | `draft` |
| [`uk/pension-schemes-act-1993`](uk/pension-schemes-act-1993) | Pension Schemes Act 1993 — early leavers (short service benefit, cash transfer sum or contribution refund) and cash equivalent transfer deadlines — row `legalese-aswathy` | `draft` |
| [`uk/pensions-act-2008`](uk/pensions-act-2008) | Pensions Act 2008 — automatic enrolment status, qualifying earnings and minimum contributions, and penalty notices — row `legalese-aswathy` | `draft` |
| [`uk/pensions-act-2014`](uk/pensions-act-2014) | Pensions Act 2014 — the new state pension (entitlement, full, reduced and transitional rates), deferral increments, and bereavement support payment — row `legalese-aswathy` | `draft` |
| [`uk/protection-from-eviction-act-1977`](uk/protection-from-eviction-act-1977) | Protection from Eviction Act 1977 — court proceedings to recover possession, notices to quit (both versions of s 5), the s 1 offence and the s 1A financial penalty with its Schedule A1 dates — row `legalese-aswathy` | `draft` |
| [`uk/renters-rights-act-2025`](uk/renters-rights-act-2025) | Renters' Rights Act 2025 — periodic tenancies and rent periods, rent in advance, and rental bidding penalties — row `legalese-aswathy` | `draft` |
| [`uk/social-security-administration-act-1992`](uk/social-security-administration-act-1992) | Social Security Administration Act 1992 — recoverable overpayments, benefit offences, and the administrative penalty — row `legalese-aswathy` | `draft` |
| [`uk/social-security-contributions-and-benefits-act-1992`](uk/social-security-contributions-and-benefits-act-1992) | Social Security Contributions and Benefits Act 1992 — Class 1 contributions, statutory sick pay amounts and linking, and statutory maternity pay — row `legalese-aswathy` | `draft` |
| [`uk/taxation-cross-border-trade-act-2018`](uk/taxation-cross-border-trade-act-2018) | Taxation (Cross-border Trade) Act 2018 — import duty liability, persons liable, amount and notification time limit — row `legalese-aswathy` | `draft` |
| [`uk/taxes-management-act-1970`](uk/taxes-management-act-1970) | Taxes Management Act 1970 — self-assessment deadlines (notification, filing, amendment, enquiry), payments on account and balancing payment, and assessment time limits — row `legalese-aswathy` | `draft` |
| [`uk/third-parties-rights-against-insurers-act-2010`](uk/third-parties-rights-against-insurers-act-2010) | Third Parties (Rights against Insurers) Act 2010 — transfer of an insolvent insured's rights, recovery from the insurer and against the insured, binding conditions, and Schedule 1 information deadlines — row `legalese-aswathy` | `draft` |
| [`uk/trade-union-and-labour-relations-consolidation-act-1992`](uk/trade-union-and-labour-relations-consolidation-act-1992) | Trade Union and Labour Relations (Consolidation) Act 1992 — union-related detriment and dismissal, collective redundancy consultation and protective awards, and protected industrial action, from the worker's seat — row `legalese-aswathy` | `draft` |
| [`uk/water-industry-act-1991`](uk/water-industry-act-1991) | Water Industry Act 1991 — connections, disconnection for non-payment, and charges and meters, from the water customer's seat — row `legalese-aswathy` | `draft` |
| [`uk/welfare-reform-act-2012`](uk/welfare-reform-act-2012) | Welfare Reform Act 2012 — universal credit entitlement and award, personal independence payment components, and the benefit cap — row `legalese-aswathy` | `draft` |
| [`uk/`](uk/) | United Kingdom Acts (Westminster) |
| [`au/act/`](au/act/) | Australian Capital Territory Acts |
| [`au/nt/`](au/nt/) | Northern Territory Acts -- conditional permission; confirm before quoting text |
| [`au/death-penalty-abolition-act-1973`](au/death-penalty-abolition-act-1973) | Death Penalty Abolition Act 1973 (Cth) — whether death may be imposed and the penalty in its place, from the seat of the person charged — row `legalese-aswathy` | `draft` |
| [`au/commonwealth-volunteers-protection-act-2003`](au/commonwealth-volunteers-protection-act-2003) | Commonwealth Volunteers Protection Act 2003 (Cth) — the volunteer's protection from civil liability, who bears it, and the duty to assist, from the volunteer's seat — row `legalese-aswathy` | `draft` |
| [`au/carer-recognition-act-2010`](au/carer-recognition-act-2010) | Carer Recognition Act 2010 (Cth) — who is a carer, what agencies must do, and that it is not enforceable, from the carer's seat — row `legalese-aswathy` | `draft` |
| [`au/damage-by-aircraft-act-1999`](au/damage-by-aircraft-act-1999) | Damage by Aircraft Act 1999 (Cth) — strict liability for harm caused by aircraft, who is liable, and contributory negligence, from the seat of the person on the ground — row `legalese-aswathy` | `draft` |
| [`au/privy-council-limitation-of-appeals-act-1968`](au/privy-council-limitation-of-appeals-act-1968) | Privy Council (Limitation of Appeals) Act 1968 (Cth) — when leave to appeal to the Privy Council may be asked, from the litigant's seat — row `legalese-aswathy` | `draft` |
| [`au/privy-council-appeals-from-the-high-court-act-1975`](au/privy-council-appeals-from-the-high-court-act-1975) | Privy Council (Appeals from the High Court) Act 1975 (Cth) — the end of special leave to appeal from the High Court, from the litigant's seat — row `legalese-aswathy` | `draft` |
| [`au/human-rights-sexual-conduct-act-1994`](au/human-rights-sexual-conduct-act-1994) | Human Rights (Sexual Conduct) Act 1994 (Cth) — protection of private sexual conduct between consenting adults from arbitrary interference — row `legalese-aswathy` | `draft` |
| [`au/common-informers-parliamentary-disqualifications-act-1975`](au/common-informers-parliamentary-disqualifications-act-1975) | Common Informers (Parliamentary Disqualifications) Act 1975 (Cth) — the sum payable for sitting in Parliament while disqualified, from the seat of the member sued — row `legalese-aswathy` | `draft` |
| [`au/first-home-super-saver-tax-act-2017`](au/first-home-super-saver-tax-act-2017) | First Home Super Saver Tax Act 2017 (Cth) — the 20% tax on assessable FHSS released amounts — row `legalese-aswathy` | `draft` |
| [`au/territories-stolen-generations-redress-scheme-facilitation-act-2021`](au/territories-stolen-generations-redress-scheme-facilitation-act-2021) | Territories Stolen Generations Redress Scheme (Facilitation) Act 2021 (Cth) — how redress payments are treated for benefits, compensation and assets, and their inalienability — row `legalese-aswathy` | `draft` |
| [`au/not-for-profit-sector-freedom-to-advocate-act-2013`](au/not-for-profit-sector-freedom-to-advocate-act-2013) | Not-for-profit Sector Freedom to Advocate Act 2013 (Cth) — gag clauses in Commonwealth agreements with not-for-profits — row `legalese-aswathy` | `draft` |
| [`au/parliamentary-retiring-allowances-increases-act-1967`](au/parliamentary-retiring-allowances-increases-act-1967) | Parliamentary Retiring Allowances (Increases) Act 1967 (Cth) — the 1967 increases in parliamentary pensions and widows' rates — row `legalese-aswathy` | `draft` |
| [`au/commonwealth-entities-payment-surcharges-act-2024`](au/commonwealth-entities-payment-surcharges-act-2024) | Commonwealth Entities (Payment Surcharges) Act 2024 (Cth) — when a Commonwealth entity may surcharge a payment, from the payer's seat — row `legalese-aswathy` | `draft` |
| [`au/superannuation-distribution-of-surplus-act-1974`](au/superannuation-distribution-of-surplus-act-1974) | Superannuation (Distribution of Surplus) Act 1974 (Cth) — who shares in the 1972 surplus of the Superannuation Fund — row `legalese-aswathy` | `draft` |
| [`au/superannuation-pension-increases-act-1961`](au/superannuation-pension-increases-act-1961) | Superannuation (Pension Increases) Act 1961 (Cth) — the 1961 increases in Commonwealth superannuation pensions — row `legalese-aswathy` | `draft` |
| [`au/defence-forces-retirement-benefits-pension-increases-act-1973`](au/defence-forces-retirement-benefits-pension-increases-act-1973) | Defence Forces Retirement Benefits (Pension Increases) Act 1973 (Cth) — the 1973 indexed increase in DFRB pensions — row `legalese-aswathy` | `draft` |
| [`au/superannuation-pension-increases-act-1967`](au/superannuation-pension-increases-act-1967) | Superannuation (Pension Increases) Act 1967 (Cth) — the 1967 increases in Commonwealth superannuation pensions — row `legalese-aswathy` | `draft` |
| [`au/transferred-officers-allowances-act-1948`](au/transferred-officers-allowances-act-1948) | Transferred Officers' Allowances Act 1948 (Cth) — allowances on the pensions of officers transferred from State to Commonwealth service — row `legalese-aswathy` | `draft` |
| [`au/parliamentary-retiring-allowances-increases-act-1971`](au/parliamentary-retiring-allowances-increases-act-1971) | Parliamentary Retiring Allowances (Increases) Act 1971 (Cth) — the 1971 increases in parliamentary and office-holders' pensions and widows' rates — row `legalese-aswathy` | `draft` |
| [`au/defence-force-retirement-and-death-benefits-pension-increases-act-1974`](au/defence-force-retirement-and-death-benefits-pension-increases-act-1974) | Defence Force Retirement and Death Benefits (Pension Increases) Act 1974 (Cth) — the 1974 indexed increases in DFRB pensions and DFRDB pension benefits — row `legalese-aswathy` | `draft` |
| [`au/defence-forces-retirement-benefits-pension-increases-act-1971`](au/defence-forces-retirement-benefits-pension-increases-act-1971) | Defence Forces Retirement Benefits (Pension Increases) Act 1971 (Cth) — the 1971 increases in DFRB pensions — row `legalese-aswathy` | `draft` |
| [`au/papua-new-guinea-members-of-the-forces-benefits-act-1957`](au/papua-new-guinea-members-of-the-forces-benefits-act-1957) | Papua New Guinea (Members of the Forces Benefits) Act 1957 (Cth) — who is a member of the Forces and when the Commonwealth is liable for war-service incapacity or death — row `legalese-aswathy` | `draft` |
| [`au/maintenance-orders-commonwealth-officers-act-1966`](au/maintenance-orders-commonwealth-officers-act-1966) | Maintenance Orders (Commonwealth Officers) Act 1966 (Cth) — attachment of Commonwealth pay for maintenance orders and their priority — row `legalese-aswathy` | `draft` |
| [`au/customs-securities-penalties-act-1981`](au/customs-securities-penalties-act-1981) | Customs Securities (Penalties) Act 1981 (Cth) — the penalty for failing to give security after a tender is accepted — row `legalese-aswathy` | `draft` |
| [`au/customs-undertakings-penalties-act-1981`](au/customs-undertakings-penalties-act-1981) | Customs Undertakings (Penalties) Act 1981 (Cth) — the penalty for breaching a Customs undertaking, with the reduction for partial compliance — row `legalese-aswathy` | `draft` |
| [`au/removal-of-prisoners-territories-act-1923`](au/removal-of-prisoners-territories-act-1923) | Removal of Prisoners (Territories) Act 1923 (Cth) — removal of Territory prisoners, review of conviction, free return, and escape — row `legalese-aswathy` | `draft` |
| [`au/united-states-naval-communication-station-civilian-employees-act-1968`](au/united-states-naval-communication-station-civilian-employees-act-1968) | United States Naval Communication Station (Civilian Employees) Act 1968 (Cth) — compensation and damages for civilian employees at the Station — row `legalese-aswathy` | `draft` |
| [`au/commonwealth-motor-vehicles-liability-act-1959`](au/commonwealth-motor-vehicles-liability-act-1959) | Commonwealth Motor Vehicles (Liability) Act 1959 (Cth) — the driver presumed the Commonwealth's agent, and the jury rule — row `legalese-aswathy` | `draft` |
| [`au/australian-veterans-recognition-putting-veterans-and-their-families-first-act-2019`](au/australian-veterans-recognition-putting-veterans-and-their-families-first-act-2019) | Australian Veterans' Recognition (Putting Veterans and their Families First) Act 2019 (Cth) — who is a veteran, and the 90-day decision commitment — row `legalese-aswathy` | `draft` |
| [`au/scout-association-act-1924`](au/scout-association-act-1924) | Scout Association Act 1924 (Cth) — the offences of misusing the Scout name and badges — row `legalese-aswathy` | `draft` |
| [`au/charities-act-2013`](au/charities-act-2013) | Charities Act 2013 (Cth) — whether an entity is a charity — row `legalese-aswathy` | `draft` |
| [`au/domicile-act-1982`](au/domicile-act-1982) | Domicile Act 1982 (Cth) — independent domicile, children's domicile and domicile of choice — row `legalese-aswathy` | `draft` |
| [`au/judges-long-leave-payments-act-1979`](au/judges-long-leave-payments-act-1979) | Judges (Long Leave Payments) Act 1979 (Cth) — the long leave payment on a federal Judge's retirement or death — row `legalese-aswathy` | `draft` |
| [`au/defence-forces-retirement-benefits-pension-increases-act-1967`](au/defence-forces-retirement-benefits-pension-increases-act-1967) | Defence Forces Retirement Benefits (Pension Increases) Act 1967 (Cth) — the 1967 increase in DFRB pensions — row `legalese-aswathy` | `draft` |
| [`au/epidemiological-studies-confidentiality-act-1981`](au/epidemiological-studies-confidentiality-act-1981) | Epidemiological Studies (Confidentiality) Act 1981 (Cth) — secrecy of prescribed studies such as the Vietnam Veterans Study — row `legalese-aswathy` | `draft` |
| [`au/diplomatic-and-consular-missions-act-1978`](au/diplomatic-and-consular-missions-act-1978) | Diplomatic and Consular Missions Act 1978 (Cth) — false claims of diplomatic or consular status — row `legalese-aswathy` | `draft` |
| [`au/submarine-cables-and-pipelines-protection-act-1963`](au/submarine-cables-and-pipelines-protection-act-1963) | Submarine Cables and Pipelines Protection Act 1963 (Cth) — damage to submarine cables and pipelines — row `legalese-aswathy` | `draft` |
| [`au/protection-of-word-anzac-act-1920`](au/protection-of-word-anzac-act-1920) | Protection of Word "Anzac" Act 1920 (Cth) — penalties for misusing the word Anzac — row `legalese-aswathy` | `draft` |
| [`au/circuit-layouts-act-1989`](au/circuit-layouts-act-1989) | Circuit Layouts Act 1989 (Cth) — EL rights in integrated circuit layouts — row `legalese-aswathy` | `draft` |
| [`au/parliamentary-privileges-act-1987`](au/parliamentary-privileges-act-1987) | Parliamentary Privileges Act 1987 (Cth) — contempt, witness protection and immunity from court — row `legalese-aswathy` | `draft` |
| [`au/advance-australia-logo-protection-act-1984`](au/advance-australia-logo-protection-act-1984) | Advance Australia Logo Protection Act 1984 (Cth) — the monopoly in the Advance Australia logo — row `legalese-aswathy` | `draft` |
| [`au/civil-dispute-resolution-act-2011`](au/civil-dispute-resolution-act-2011) | Civil Dispute Resolution Act 2011 (Cth) — genuine steps statements in federal civil proceedings — row `legalese-aswathy` | `draft` |
| [`au/trusts-hague-convention-act-1991`](au/trusts-hague-convention-act-1991) | Trusts (Hague Convention) Act 1991 (Cth) — the law governing trusts and their recognition — row `legalese-aswathy` | `draft` |
| [`au/control-of-naval-waters-act-1918`](au/control-of-naval-waters-act-1918) | Control of Naval Waters Act 1918 (Cth) — directions, removal and sale of craft in naval waters — row `legalese-aswathy` | `draft` |
| [`au/explosives-act-1961`](au/explosives-act-1961) | Explosives Act 1961 (Cth) — the reach of the Commonwealth's explosives regulations and the penalty for breach — row `legalese-aswathy` | `draft` |
| [`au/superannuation-pension-increases-act-1971`](au/superannuation-pension-increases-act-1971) | Superannuation (Pension Increases) Act 1971 (Cth) — the 1971 increase in Superannuation Act 1922 pensions — row `legalese-aswathy` | `draft` |
| [`au/crimes-biological-weapons-act-1976`](au/crimes-biological-weapons-act-1976) | Crimes (Biological Weapons) Act 1976 (Cth) — biological and toxin weapons offences — row `legalese-aswathy` | `draft` |
| [`au/defence-forces-special-retirement-benefits-act-1960`](au/defence-forces-special-retirement-benefits-act-1960) | Defence Forces Special Retirement Benefits Act 1960 (Cth) — benefits for soldiers discharged in the 1961 reduction — row `legalese-aswathy` | `draft` |
| [`au/defence-force-retirement-and-death-benefits-pension-increases-act-1976`](au/defence-force-retirement-and-death-benefits-pension-increases-act-1976) | Defence Force Retirement and Death Benefits (Pension Increases) Act 1976 (Cth) — the 1973-76 DFRB and DFRDB pension increases — row `legalese-aswathy` | `draft` |
| [`au/asbestos-related-claims-management-of-commonwealth-liabilities-act-2005`](au/asbestos-related-claims-management-of-commonwealth-liabilities-act-2005) | Asbestos-related Claims (Management of Commonwealth Liabilities) Act 2005 (Cth) — Commonwealth asbestos liabilities transferred to Comcare — row `legalese-aswathy` | `draft` |
| [`au/services-trust-funds-act-1947`](au/services-trust-funds-act-1947) | Services Trust Funds Act 1947 (Cth) — the Navy, Army and Air Force relief trust funds — row `legalese-aswathy` | `draft` |
| [`au/national-rental-affordability-scheme-act-2008`](au/national-rental-affordability-scheme-act-2008) | National Rental Affordability Scheme Act 2008 (Cth) — the Act's conditions of an NRAS allocation — row `legalese-aswathy` | `draft` |
| [`au/defence-parliamentary-candidates-act-1969`](au/defence-parliamentary-candidates-act-1969) | Defence (Parliamentary Candidates) Act 1969 (Cth) — leaving and returning to the Defence Force to stand for Parliament — row `legalese-aswathy` | `draft` |
| [`au/statutory-declarations-act-1959`](au/statutory-declarations-act-1959) | Statutory Declarations Act 1959 (Cth) — making and using a Commonwealth statutory declaration — row `legalese-aswathy` | `draft` |
| [`au/air-accidents-commonwealth-government-liability-act-1963`](au/air-accidents-commonwealth-government-liability-act-1963) | Air Accidents (Commonwealth Government Liability) Act 1963 (Cth) — Commonwealth liability to air passengers — row `legalese-aswathy` | `draft` |
| [`au/crimes-overseas-act-1964`](au/crimes-overseas-act-1964) | Crimes (Overseas) Act 1964 (Cth) — Australian criminal law for Australians abroad — row `legalese-aswathy` | `draft` |
| [`au/public-and-educational-lending-rights-better-income-for-authors-act-2026`](au/public-and-educational-lending-rights-better-income-for-authors-act-2026) | Public and Educational Lending Rights (Better Income for Authors) Act 2026 (Cth) — who the lending rights scheme pays, and review — row `legalese-aswathy` | `draft` |
| [`au/crimes-hostages-act-1989`](au/crimes-hostages-act-1989) | Crimes (Hostages) Act 1989 (Cth) — hostage-taking offences — row `legalese-aswathy` | `draft` |
| [`au/weapons-of-mass-destruction-prevention-of-proliferation-act-1995`](au/weapons-of-mass-destruction-prevention-of-proliferation-act-1995) | Weapons of Mass Destruction (Prevention of Proliferation) Act 1995 (Cth) — supplying goods and services to WMD programs — row `legalese-aswathy` | `draft` |
| [`au/immigration-guardianship-of-children-act-1946`](au/immigration-guardianship-of-children-act-1946) | Immigration (Guardianship of Children) Act 1946 (Cth) — the Minister's guardianship of unaccompanied non-citizen children — row `legalese-aswathy` | `draft` |
| [`au/protection-of-cultural-objects-on-loan-act-2013`](au/protection-of-cultural-objects-on-loan-act-2013) | Protection of Cultural Objects on Loan Act 2013 (Cth) — immunity from seizure for objects on loan for exhibition — row `legalese-aswathy` | `draft` |
| [`au/war-crimes-act-1945`](au/war-crimes-act-1945) | War Crimes Act 1945 (Cth) — Second World War crimes in Europe — row `legalese-aswathy` | `draft` |
| [`au/war-gratuity-act-1945`](au/war-gratuity-act-1945) | War Gratuity Act 1945 (Cth) — the Second World War service gratuity — row `legalese-aswathy` | `draft` |
| [`au/adelaide-airport-curfew-act-2000`](au/adelaide-airport-curfew-act-2000) | Adelaide Airport Curfew Act 2000 (Cth) — the night curfew at Adelaide Airport — row `legalese-aswathy` | `draft` |
| [`au/immigration-education-act-1971`](au/immigration-education-act-1971) | Immigration (Education) Act 1971 (Cth) — migrant English tuition (AMEP) eligibility and time limits — row `legalese-aswathy` | `draft` |
| [`au/federal-proceedings-costs-act-1981`](au/federal-proceedings-costs-act-1981) | Federal Proceedings (Costs) Act 1981 (Cth) — costs certificates for litigants in federal appeals — row `legalese-aswathy` | `draft` |
| [`au/maternity-leave-commonwealth-employees-act-1973`](au/maternity-leave-commonwealth-employees-act-1973) | Maternity Leave (Commonwealth Employees) Act 1973 (Cth) — maternity leave and pay for Commonwealth employees — row `legalese-aswathy` | `draft` |
| [`us/`](us/) | United States federal Acts (public domain) |
| [`us/ca/`](us/ca/) | California code divisions (public domain) |
| [`us/ny/`](us/ny/) | New York Consolidated Laws articles |
| [`us/tx/`](us/tx/) | Texas code chapters |
| [`ca/`](ca/) | Canadian federal Acts -- English and French equally authoritative; conditional permission |
| [`ca/on/`](ca/on/) | Ontario statutes -- English and French equally authoritative; conditional permission |
| [`ca/bc/`](ca/bc/) | British Columbia statutes (King's Printer Licence) |
| [`in/`](in/) | Indian central Acts -- no reuse licence; not independently spot-checked |
| [`ie/`](ie/) | Irish Acts (Oireachtas PSI Licence, CC BY 4.0) |
| [`za/`](za/) | South African Acts -- **licence unclear; metadata only** until resolved |
| [`hk/`](hk/) | Hong Kong ordinances -- **not openly licensed; metadata only**; English and Chinese equally authentic |
| [`il/`](il/) | Israeli Laws (no copyright in statutes, Copyright Act 2007 s 6) -- Hebrew authoritative |
| [`br/`](br/) | Brazilian federal laws (no copyright in laws, Lei 9.610/1998 art. 8º IV) -- Portuguese authoritative; where the text is, and what LexML does and does not give, in its README |
| [`jp/`](jp/) | Japanese Acts (Public Data License 1.0 for the e-Gov text and the Ministry of Justice translations) -- Japanese authoritative; the Ministry of Justice's English translations are aids, not official texts |
| [`kr/`](kr/) | Korean Acts and Presidential Decrees (not protected by copyright, Copyright Act Art 7) -- Korean authoritative, from law.go.kr; English translations are aids, not official texts |
| [`us/al/`](us/al/) | Alabama (US state) -- **metadata only**; licence decision pending |
| [`us/ak/`](us/ak/) | Alaska (US state) -- **metadata only**; licence decision pending |
| [`us/az/`](us/az/) | Arizona (US state) -- **metadata only**; licence decision pending |
| [`us/ar/`](us/ar/) | Arkansas (US state) -- **metadata only**; licence decision pending |
| [`us/co/`](us/co/) | Colorado (US state) -- **metadata only**; licence decision pending |
| [`us/ct/`](us/ct/) | Connecticut (US state) -- **metadata only**; licence decision pending |
| [`us/de/`](us/de/) | Delaware (US state) -- **metadata only**; licence decision pending |
| [`us/dc/`](us/dc/) | District of Columbia (US federal district) -- **metadata only**; licence decision pending |
| [`us/fl/`](us/fl/) | Florida (US state) -- **metadata only**; licence decision pending |
| [`us/ga/`](us/ga/) | Georgia (US state) -- **metadata only**; licence decision pending |
| [`us/hi/`](us/hi/) | Hawaii (US state) -- **metadata only**; licence decision pending |
| [`us/in/`](us/in/) | Indiana (US state) -- **metadata only**; licence decision pending |
| [`us/ia/`](us/ia/) | Iowa (US state) -- **metadata only**; licence decision pending |
| [`us/ks/`](us/ks/) | Kansas (US state) -- **metadata only**; licence decision pending |
| [`us/ky/`](us/ky/) | Kentucky (US state) -- **metadata only**; licence decision pending |
| [`us/me/`](us/me/) | Maine (US state) -- **metadata only**; licence decision pending |
| [`us/md/`](us/md/) | Maryland (US state) -- **metadata only**; licence decision pending |
| [`us/mn/`](us/mn/) | Minnesota (US state) -- **metadata only**; licence decision pending |
| [`us/ms/`](us/ms/) | Mississippi (US state) -- **metadata only**; licence decision pending |
| [`us/mt/`](us/mt/) | Montana (US state) -- **metadata only**; licence decision pending |
| [`us/nm/`](us/nm/) | New Mexico (US state) -- **metadata only**; licence decision pending |
| [`us/nd/`](us/nd/) | North Dakota (US state) -- **metadata only**; licence decision pending |
| [`us/ok/`](us/ok/) | Oklahoma (US state) -- **metadata only**; licence decision pending |
| [`us/sc/`](us/sc/) | South Carolina (US state) -- **metadata only**; licence decision pending |
| [`us/sd/`](us/sd/) | South Dakota (US state) -- **metadata only**; licence decision pending |
| [`us/tn/`](us/tn/) | Tennessee (US state) -- **metadata only**; licence decision pending |
| [`us/vt/`](us/vt/) | Vermont (US state) -- **metadata only**; licence decision pending |
| [`us/va/`](us/va/) | Virginia (US state) -- **metadata only**; licence decision pending |
| [`us/wa/`](us/wa/) | Washington (US state) -- **metadata only**; licence decision pending |
| [`us/wy/`](us/wy/) | Wyoming (US state) -- **metadata only**; licence decision pending |
| [`ca/ab/`](ca/ab/) | Alberta (Canadian province or territory) -- **metadata only**; licence decision pending |
| [`ca/mb/`](ca/mb/) | Manitoba (Canadian province or territory) -- **metadata only**; licence decision pending |
| [`ca/nl/`](ca/nl/) | Newfoundland and Labrador (Canadian province or territory) -- **metadata only**; licence decision pending |
| [`ca/nt/`](ca/nt/) | Northwest Territories (Canadian province or territory) -- **metadata only**; licence decision pending |
| [`ca/ns/`](ca/ns/) | Nova Scotia (Canadian province or territory) -- **metadata only**; licence decision pending |
| [`ca/nu/`](ca/nu/) | Nunavut (Canadian province or territory) -- **metadata only**; licence decision pending |
| [`ca/qc/`](ca/qc/) | Quebec (Canadian province or territory) -- **metadata only**; licence decision pending |
| [`ca/sk/`](ca/sk/) | Saskatchewan (Canadian province or territory) -- **metadata only**; licence decision pending |

The directory contract (the "class" — see the repository README for the class/instance
design) is the subject-sidecar shape defined by the l4-ide orchestrator:

| file                | role                                                                                                                                                 |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `subject.json`      | machine-readable descriptor: id, display name, citation, source URL, corpus modules, per-leg projection declarations, encoding version, status       |
| `NOTES.md`          | this subject's idiosyncrasies, in prose, for humans — no script reads it                                                                             |
| `SOURCE-LICENSE.md` | the terms the quoted legal text carries, and the attribution NOTICE requires                                                                         |
| `*.l4`              | the encoding, in inert style, with `@ref` citations on dated arms                                                                                    |
| `cases/`            | dated scenario cases; expected values machine-evaluated, never hand-typed                                                                            |
| `projections/`      | emitted DMN/BPMN/other artifacts + fidelity reports declaring every loss                                                                             |
| `registers/`        | fork register, external-modification register, source bundle — validated against the schemas in l4-ide `specs/todo/single-instruction-demo/schemas/` |
| `report/`           | the conversion report                                                                                                                                |
| `gates/`            | HG1/HG2 grant artifacts: payloads, signatures, waivers, `allowed_signers`                                                                            |

An instance is expected to veer from the class; its divergences are recorded in its own
`NOTES.md`, never by forking the template.

Two amendments to that table are already in force and are not yet written into it, because
`docs/directory-conventions.md` supersedes it and its own §12
owns the rewrite. First, the sidecar shape above now describes a **vendored encoding row** under
`encodings/<encoder>/`, one level below the subject, and the descriptor splits in two:
`subject.json` at the subject level carries facts about the law, `encoding.json` in each row
carries facts about the encoding (§4.2). All seven subjects already do this. Second, `source/` and
`registers/` sit at the **subject** level, because the source text is a fact about the law and is
shared by every row (§6). That one is not yet uniform, and the tree is the honest record: both
`contracts/` rows put `source/` and `registers/` at the subject level, `us/chubb-hospital-cash`
puts `registers/` there, and the `sg/` rows keep both inside the encoding row. Do not read the
table above as contradicting the conventions document.

The stages an encoding passes through, and what the HG1 and HG2 gates certify, are in
[`PIPELINE.md`](../PIPELINE.md).
