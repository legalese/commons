# european-union/

L4 encodings of European Union law — one subject-id per body of law (Regulation,
Directive, or delegated act), following the subject-sidecar shape described in
[`subjects/README.md`](../README.md).

| subject | instrument | status |
| ------- | ---------- | ------ |
| [`FinMont-demo`](FinMont-demo/) | Commission Delegated Regulation (EU) 2018/389 — PSD2 regulatory technical standards for strong customer authentication | `draft` |
| [`social-security-coordination-regulation-2004`](social-security-coordination-regulation-2004/) | Regulation (EC) No 883/2004 — coordination of social security systems | sourced |
| [`social-security-coordination-implementing-regulation-2009`](social-security-coordination-implementing-regulation-2009/) | Regulation (EC) No 987/2009 — implementing Regulation 883/2004 | sourced |
| [`third-country-nationals-social-security-regulation-2010`](third-country-nationals-social-security-regulation-2010/) | Regulation (EU) No 1231/2010 — 883/2004 and 987/2009 extended to third-country nationals | sourced |
| [`free-movement-of-workers-regulation-2011`](free-movement-of-workers-regulation-2011/) | Regulation (EU) No 492/2011 — freedom of movement for workers | sourced |
| [`citizens-rights-directive-2004`](citizens-rights-directive-2004/) | Directive 2004/38/EC — right of Union citizens and family members to move and reside | sourced |
| [`cross-border-healthcare-directive-2011`](cross-border-healthcare-directive-2011/) | Directive 2011/24/EU — patients' rights in cross-border healthcare | sourced |
| [`supplementary-pension-rights-directive-2014`](supplementary-pension-rights-directive-2014/) | Directive 2014/50/EU — acquisition and preservation of supplementary pension rights | sourced |
| [`tfeu-2007`](tfeu-2007/) | Treaty on the Functioning of the European Union, consolidated, with Protocols and Annexes | sourced |
| [`charter-of-fundamental-rights-2000`](charter-of-fundamental-rights-2000/) | Charter of Fundamental Rights of the European Union (2016/C 202/02) | sourced |
| [`eu-staff-tax-regulation-1968`](eu-staff-tax-regulation-1968/) | Regulation (EEC, Euratom, ECSC) No 260/68 — the Union tax on its officials' salaries | sourced |

"Sourced" means the text is deposited in `registers/source-bundle/` and nothing is encoded yet.

## Cross-border social security, benefits and personal income tax (sourced 2026-10-19)

A Priority 3 sample. The Union runs no general benefit scheme and levies no income tax on the
public, so the useful EU law for a member of the public is the law they meet when they **move,
work or are treated across a border**. The set is chosen so that it can answer questions such as:

- *I work in one country and live in another: which country's social security covers me, and where
  do I pay contributions?* (883/2004 Title II; 987/2009 Arts 14-16)
- *Do my years of work in another Member State count towards my pension or my unemployment
  benefit?* (883/2004 Art 6 and the benefit chapters; 987/2009 Arts 12-13)
- *Can I take my unemployment benefit with me while I look for work abroad, and for how long?*
  (883/2004 Art 64: at least four weeks registered first, then three months, extendable to six;
  987/2009 Art 55)
- *Which country pays child benefit when my children live in another Member State?*
  (883/2004 Arts 67-68; 987/2009 Arts 58-61)
- *Am I entitled to social assistance after moving, and when do I get permanent residence?*
  (2004/38 Arts 7, 16 and 24(2))
- *Must the host State give me the same tax and social advantages as its own workers?*
  (492/2011 Art 7(2); TFEU Art 45)
- *Can I be treated in another Member State and be reimbursed?* (883/2004 Arts 19-20;
  2011/24 Arts 7-9)
- *I am not an EU national: do the coordination rules cover me?* (1231/2010 Art 1)
- *Will my occupational pension vest if I leave for a job in another Member State?* (2014/50 Art 4)

| Subject | Text deposited | Version | Characters | Why it is in the set |
|---|---|---|---|---|
| `social-security-coordination-regulation-2004` | `reg-2004-883.txt` | consolidated, **31.07.2019** (CELEX 02004R0883-20190731) | 224,052 | The coordination rules themselves: persons and benefits covered, equal treatment, aggregation, export, the single applicable legislation, and the benefit-by-benefit chapters. |
| `social-security-coordination-implementing-regulation-2009` | `reg-2009-987.txt` | consolidated, **01.01.2018** (02009R0987-20180101) | 168,726 | The procedures: residence, provisional benefits, posting, healthcare abroad, pension claims, unemployment export, family-benefit priority, recovery of overpayments. |
| `third-country-nationals-social-security-regulation-2010` | `reg-2010-1231.txt` | as published, OJ L 344, 29.12.2010 (32010R1231; no consolidation exists) | 11,399 | Brings legally resident non-EU nationals in cross-border situations within 883/2004 and 987/2009. |
| `free-movement-of-workers-regulation-2011` | `reg-2011-492.txt` | consolidated, **01.08.2021** (02011R0492-20210801) | 19,789 | Equal treatment of EU workers, including Art 7(2), "the same social and tax advantages as national workers". |
| `citizens-rights-directive-2004` | `dir-2004-38.txt` | consolidated, **16.06.2011** (02004L0038-20110616) | 45,966 | Residence rights that gate benefits; the Art 24(2) derogation for social assistance and student maintenance aid. |
| `cross-border-healthcare-directive-2011` | `dir-2011-24.txt` | consolidated, **12.01.2025** (02011L0024-20250112) | 51,854 | The second route to treatment abroad, and its Art 8(3) link back to 883/2004. |
| `supplementary-pension-rights-directive-2014` | `dir-2014-50.txt` | as published, OJ L 128, 30.4.2014 (32014L0050; no consolidation exists) | 27,835 | Occupational pensions, which 883/2004 does not coordinate. |
| `tfeu-2007` | `tfeu-2016.txt` | consolidated, **15.03.2025** (02016E/TXT-20250315) | 675,620 | Arts 18, 21, 45, 48, 49 and 63, and Protocol (No 7) Art 12; the Treaty base of the tax non-discrimination case law. |
| `charter-of-fundamental-rights-2000` | `charter-2016.txt` | as published, OJ C 202, 7.6.2016, p. 389 (12016P/TXT) | 25,628 | Art 34 (social security and social assistance), Art 35 (health care), Art 45 (movement and residence), Art 51 (scope). |
| `eu-staff-tax-regulation-1968` | `reg-1968-260.txt` | consolidated, **03.10.2002** (01968R0260-20021003) — **stale, see Gaps** | 15,746 | The only income tax the Union levies on individuals: on the salaries of its own officials and servants. |

Total: 10 instruments, 1,266,615 characters. Each text carries its source, CELEX number,
consolidation date and the authenticity notice at the top; each `.meta.json` records the request
and final URLs, the retrieval time (UTC), the sha256 of the download and of the text, the
character count, the conversion method, and any amending acts CELLAR lists with effect after the
consolidation date.

### Why the pieces connect

- **TFEU Art 48** directs the Parliament and Council to adopt social security measures for migrant
  workers, naming aggregation of periods and payment of benefits to persons resident in other
  Member States; **883/2004** is that measure, **987/2009** its procedure, and **1231/2010**
  (legal base TFEU Art 79(2)(b), per its citation) extends both to third-country nationals.
- **TFEU Art 45** secures free movement of workers and abolishes nationality discrimination as
  regards remuneration and other conditions of work; **492/2011** spells it out, and its Art 7(2)
  gives the migrant worker the same social **and tax** advantages as nationals.
- **TFEU Art 21** gives every citizen the right to move and reside "subject to the limitations and
  conditions laid down in the Treaties and by the measures adopted to give them effect";
  **2004/38** is the main such measure. Its residence categories decide whether a person can claim
  social assistance (Art 24), while 883/2004 decides which State's social security applies.
  The two are separate tests and both must be run.
- **Healthcare** has two routes. 883/2004 Arts 19-20 (necessary care during a stay, and authorised
  planned treatment) and 2011/24 (reimbursement up to the home-State tariff). 2011/24 Art 8(3)
  sends a request for prior authorisation that meets the 883/2004 conditions down the Regulation
  route unless the patient asks otherwise.
- **Pensions** are in three layers: statutory pensions under 883/2004 (aggregation and pro rata),
  occupational pensions under 2014/50 (vesting and preservation only, no aggregation), and private
  pensions, which no instrument here covers.
- **The Charter** (Art 34(2)) restates the entitlement of everyone residing and moving legally to
  social security benefits and social advantages "in accordance with Union law and national laws
  and practices". By Art 51 it binds Member States only when they implement Union law, which
  includes applying 883/2004 and 2004/38.

### Personal income tax: what binding EU law there is

- **No directive or regulation harmonises the personal income tax of the public.** The binding EU
  law on an individual's income tax is the Treaty freedoms themselves (TFEU Arts 18, 21, 45, 49
  and 63, deposited) and, in secondary law, 492/2011 Art 7(2) (deposited).
- **The non-discrimination principle in direct tax is case law, not text.** The Court of Justice
  has held that a State of employment must in some cases give a non-resident who earns almost all
  of their income there the same personal allowances as a resident (*Schumacker*, C-279/93, 1995),
  and has developed this in later cases. Unverified (general knowledge). The judgments are not
  deposited. An encoding of a "may I be taxed like a resident?" decision would need them, and so
  would sit beside this set rather than within it.
- **Commission Recommendation 94/79/EC** on the taxation of certain items of income received by
  non-residents is not binding and is not deposited. Unverified (general knowledge).
- **Council Directive 2011/16/EU** (administrative cooperation in taxation, "DAC") governs exchanges
  between tax authorities, not the individual's liability, and is left out. Its content is
  unverified (general knowledge).
- **The Union does levy one personal income tax**, on its own officials and other servants.
  Protocol (No 7) Art 12 (in the TFEU deposit) makes them liable to a tax for the benefit of the
  Union and exempts them from national taxes on their Union salaries. **260/68** sets the conditions
  and procedure: Art 2 lists who is liable, Art 3 the taxable amount and deductions, Art 4 the
  rates, and collection is by deduction at source. It is in the set because it is the only binding
  EU law that taxes an individual's income directly. It reaches only Union staff.

### How this meets the national sets already in commons

- **Ireland** (`subjects/ie/`, social welfare and income tax set of 2026-10-19). The deposited
  revised Social Welfare Consolidation Act 2005 cites Directive 2004/38/EC: in the habitual
  residence provisions it refers to a worker or self-employed person "residing in the State
  pursuant to article 7" of that Directive. It also cites Regulation (EC) No 883/2004 for
  bereaved partner's (contributory) pension and Regulation (EEC) No 1408/71 for invalidity
  pension. An Irish encoding of habitual residence or of a pension paid under the coordination
  rules can therefore call into `citizens-rights-directive-2004` and
  `social-security-coordination-regulation-2004` here. Ireland opted into 1231/2010 (its recital 17).
- **United Kingdom** (`subjects/uk/`). The deposited UK texts still carry the EU hooks.
  The Social Security Contributions and Benefits Act 1992 bars attendance allowance and similar
  benefits to "a person to whom either Regulation (EC) No 1408/71 or Regulation (EC) No 883/2004
  applies" unless conditions are met. The Personal Independence Payment Regulations 2013 turn on
  whether "a relevant EU Regulation" applies. The Universal Credit Regulations 2013 apply a habitual
  residence test. The United Kingdom did not take part in 1231/2010 (its recital 18). Since the
  United Kingdom left the Union, coordination with it has run under Part Two of the Withdrawal
  Agreement (for people in a cross-border situation before the end of 2020) and the Protocol on
  Social Security Coordination of the EU-UK Trade and Cooperation Agreement. The UK also keeps
  883/2004 as assimilated law in its own revised form on legislation.gov.uk. All of this
  paragraph's post-exit history is unverified (general knowledge); none of those texts is deposited.
- The Union texts here are the **EU version**. Where a national set relies on the UK's retained or
  assimilated copy of an EU instrument, that copy is a different text and belongs under `uk/`.

### Terms, as read on 2026-10-19 (UTC)

- **eur-lex.europa.eu/robots.txt**: requested once, at 2026-10-19T17:41:09Z, with the User-Agent
  `legalese-commons-source-fetcher/1.0 (+https://github.com/legalese/commons)`. EUR-Lex answered
  HTTP 202 with an empty body and the header `x-amzn-waf-action: challenge` (an AWS WAF bot
  challenge). Per the access rules, that was not worked around and nothing further was requested
  from eur-lex.europa.eu. **EUR-Lex's own legal notice was therefore not read.**
- **publications.europa.eu/robots.txt** redirected (301) to **op.europa.eu/robots.txt**:
  `User-agent: *` / `Allow: /`, with disallows only for portal paths (`/c/portal/`, basket, auth,
  `requestAction=rdf`, `/webdav/*`, short URLs, dynamic-state parameters). It gives no Crawl-delay
  and does not disallow `/resource/` or `/webapi/`. Requests were spaced at least 3 s apart.
- **Commission Decision 2011/833/EU** (fetched from CELLAR, CELEX 32011D0833, and read). It covers
  documents of the Commission or published by the Publications Office on its behalf (Art 2).
  All documents are available for re-use, commercial or not, free of charge, without individual
  application (Art 4). Conditions may require acknowledging the source, not distorting the original
  meaning, and accepting the Commission's non-liability (Art 6(2)). Re-use "calculated to deceive
  or to defraud" is excluded (Art 2(4)).
- **Publications Office copyright notice**
  (op.europa.eu/en/web/about-us/legal-notices/publications-office-of-the-european-union-copyright,
  read): the website's editorial content is CC BY 4.0. For content on EUR-Lex it refers the reader
  to EUR-Lex's own copyright notice. For the conditions on re-use of **CELLAR** content it says to
  contact op-copyright@publications.europa.eu. This was **not** done; see "Check before
  committing".
- **Council Regulation (EU) No 216/2013** (consolidated 14.03.2024, fetched from CELLAR, read):
  only the electronic edition of the Official Journal is authentic and produces legal effects
  (Art 1(2)). Electronic editions corresponding to printed editions published after 1 July 2013 are
  the only authentic editions (Art 3(3)). Each consolidated text carries its own notice that it "is
  meant purely as a documentation tool and has no legal effect".
- The commonly quoted EUR-Lex wording is that re-use is authorised provided the source is
  acknowledged, with the attribution "© European Union, https://eur-lex.europa.eu". The
  Commission's adoption of CC BY 4.0 for its documents in 2019 is also often cited. Both are
  unverified (general knowledge). One request fetched CELEX 32019D1372 on the mistaken belief that
  it was that 2019 decision. It is an unrelated INSPIRE monitoring decision and was discarded.
- **Access route.** All law texts came from the Publications Office's official machine routes: the
  SPARQL endpoint (https://publications.europa.eu/webapi/rdf/sparql) to find each act's latest
  consolidated version and its amending acts, then CELLAR content negotiation (`Accept:
  application/xhtml+xml`, `Accept-Language: eng`) on the work URI, which redirects (303) to the
  English XHTML manifestation. 38 requests to publications.europa.eu and op.europa.eu, plus
  the robots.txt requests above. No 403 or 429 responses and no further challenges.

### Currency

Consolidation dates are those EUR-Lex/CELLAR gave at retrieval on 2026-10-19. Each meta file lists
the amending acts CELLAR records with effect after the consolidation date:

- **883/2004 (31.07.2019), 492/2011 (01.08.2021), 2004/38 (16.06.2011), TFEU (15.03.2025)**: no
  later amending act recorded. The long-running proposal to revise 883/2004 and 987/2009 had not
  produced an amending act in CELLAR at retrieval. The proposal's status is unverified (general
  knowledge).
- **987/2009 (01.01.2018)**: Administrative Commission Decision No H9 of 17 June 2020
  (32020D0807(01)), which postponed the deadlines in Arts 67 and 70 because of COVID-19, is
  recorded as amending it and is not in the consolidation. It was temporary.
- **2011/24 (12.01.2025)**: Regulation (EU) 2025/327 on the European Health Data Space amends the
  Directive in stages (CELLAR dates: 2025-03-25, 2027-03-26, 2029-03-26, 2031-03-26, 2035-03-26).
  None of those changes is in the deposited text. They concern the eHealth provisions, not the
  reimbursement rules (unverified (general knowledge); check before encoding Art 14).
- **260/68 (03.10.2002)**: **stale.** CELLAR records four later amending Regulations: 1558/2007,
  420/2008, 1296/2009 and 1239/2010, the last titled as adjusting staff remuneration with effect
  from 1 July 2010. None is consolidated. The Art 4 rate bands in the deposited text are the 2002
  figures. Bands after 2010 are not in any deposited text: how they are now updated is unverified
  (general knowledge).
- **1231/2010, 2014/50, the Charter**: no consolidated version exists. CELLAR records no amending act.

### Gaps

- **Withdrawal Agreement and EU-UK Trade and Cooperation Agreement** (Protocol on Social Security
  Coordination): not deposited. Both are long, and they decide every EU-UK case.
- **EEA and Switzerland**: 883/2004 applies to them through the EEA Agreement and the EU-Swiss
  agreement on free movement of persons (unverified (general knowledge)); not deposited.
- **Regulations 1408/71 and 574/72**: still referred to in national texts and in 883/2004 Art 90 for
  residual cases; not deposited.
- **Administrative Commission decisions** (the A, E, F, H, P, S and U series, and the portable
  documents such as A1 and S1): they decide much of the practice, and none is deposited.
- **Other third-country-national equal-treatment rules**: the Long-term Residents Directive
  2003/109/EC, the Single Permit Directive and the Blue Card Directive each carry
  social-security equal-treatment clauses (unverified (general knowledge)); not deposited.
- **Directive 2014/54/EU** (measures facilitating the exercise of workers' free movement rights):
  enforcement machinery; left out.
- **Case law**: the Court's judgments on direct-tax non-discrimination, on "social advantages"
  under 492/2011 Art 7(2), and on access to benefits under 2004/38 Art 24 (unverified (general
  knowledge)); not deposited.
- **Conversion**: complex tables with row and column spans are flattened, with spanned cells left
  empty. The concordance tables in 883/2004 Annex VII misalign, and TFEU Annex I (the Art 38
  product list) came out as lines rather than rows. Check any table against the OJ before
  encoding from it.

## Licensing note for this jurisdiction

Where Western Australian material is CC BY 4.0, EU material is not. Reuse of Official
Journal text is authorised under
[Commission Decision 2011/833/EU](https://eur-lex.europa.eu/eli/dec/2011/833/oj) — free of
charge, including commercially, provided the source is acknowledged and the original
meaning is not distorted. Each subject records its own terms in `SOURCE-LICENSE.md`, and
the attribution required is collected in the repository [`NOTICE`](../../NOTICE).

Only the electronic Official Journal on EUR-Lex is authentic
([Council Regulation (EU) No 216/2013](https://eur-lex.europa.eu/eli/reg/2013/216/oj)).
Nothing encoded here is authentic legal text.
