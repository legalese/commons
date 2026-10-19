# connecticut/

Connecticut (US state) legislation, one subject-id per body of law, following the subject-sidecar shape described in [`subjects/README.md`](../README.md).

The subjects here were laid out on 2026-09-23 for the legislation governing twelve everyday topics. Each was checked against the Connecticut General Assembly — General Statutes of Connecticut (prepared under the direction of the Legislative Commissioners' Office); the check is recorded in each subject's `registers/source-bundle/*.meta.json`. No statute text had been deposited when they were laid out; see the 2026-10-20 sample below. Nothing is encoded yet.

**Licence category: unclear.** **Metadata only until resolved.** No human has recorded a licence decision for this jurisdiction in `tools/topics/round3/licence-decisions.json`. The register's own terms, quoted above, are the evidence to decide on.

## Register access

Plain HTTPS GETs with an honest UA ('canon-legislation-indexer/1.0 (legalese/canon L4 corpus; metadata only)'), about 18 requests spaced ~1.8 s apart. No block, challenge or rate limit. One caveat: the WebFetch tool failed on this host with 'unable to verify the first certificate' (the server serves an incomplete TLS chain); curl with default verification succeeded, so the chain resolves for normal clients. Titles index states 'Revised to January 1, 2025', and every chapter page carries the note that the 2026 Supplement, revised to January 1, 2026, holds updates from the 2025 sessions — so the free site is the 2025 revision plus a separately published 2026 supplement, and an as-at-2026 reading requires checking the supplement as well.

## Topics with no legislation here

- **Termination/severance**: No state statute. Connecticut is an at-will state with no severance entitlement and no mini-WARN Act; the Title 31 index carries no plant-closing notice chapter. The statutory consequences of dismissal are limited to payment of final wages (§ 31-71c, Chapter 558), continuation of group health coverage on a plant closing (§ 31-51o) and unemployment compensation (Chapter 567). Mass-layoff notice is federal: WARN Act, 29 U.S.C. § 2101 et seq.
- **Passenger compensation**: No state statute. Airline delay, cancellation and denied-boarding compensation is federal and preempts state regulation (Airline Deregulation Act, 49 U.S.C. § 41713; 14 C.F.R. part 250). Connecticut's Title 16 chapters on motor buses (286) and taxicabs (287) are licensing and rate regulation, not passenger compensation.
- **Customs/duties**: Federal matter. Import duties and customs are exclusively federal (U.S. Const. art. I, § 10, cl. 2; Tariff Act of 1930, 19 U.S.C. ch. 4).
- **Work permits/immigration**: Federal matter. Admission and work authorisation are governed by the Immigration and Nationality Act, 8 U.S.C. ch. 12, and employment verification by 8 U.S.C. § 1324a. Connecticut regulates only minors' employment certificates (Chapter 557, §§ 31-23 et seq.), which is a different subject.

## Benefits and personal income tax sample (sourced 2026-10-20)

Statute text was deposited for four chapters of the General Statutes, so that a member of the public can get state determinations on two topics, personal income tax and social security and benefits, and see where each one plugs into the federal set already in `subjects/us/` (`internal-revenue-code-of-1986`, `social-security-act`, `food-and-nutrition-act-of-2008`; those are indexed only, with no text). Each chapter is deposited twice: the 2025 revision, and the 2026 Supplement, which holds only the sections changed in the 2025 sessions. Where a section appears in both, the Supplement version governs from its effective date.

| Subject | Chapter | Why it is in the set |
|---|---|---|
| `general-statutes-of-connecticut-title-12-taxation-chapter-229` | ch. 229, 12-700 ff. | The personal income tax. 12-700 sets the rates (from 2024: tables up to 6.99%, kept as tables); 12-701 defines Connecticut AGI; 12-704e is the state earned income tax credit (the Supplement version adds an additional amount). |
| `general-statutes-of-connecticut-title-17b-social-services` | ch. 319s, 17b-75 ff. | Cash assistance: temporary family assistance (TANF), 17b-112; the state supplement to SSI, 17b-104 and 17b-106. |
| `general-statutes-of-connecticut-title-31-labor-chapter-567-unemployment` | ch. 567, 31-222 ff. | Unemployment compensation: benefit rate 31-231a, eligibility 31-235, disqualification 31-236. |
| `general-statutes-of-connecticut-title-12-taxation-chapter-204a-elderly-tax-relief` | ch. 204a | Property tax relief for elderly or totally disabled homeowners (12-170aa) and the renters' refund (12-170d). |

The plan named "17b-600 ff." for the state supplement; the register shows the state supplement to SSI at 17b-104 and 17b-106 in chapter 319s, so that chapter covers it.

**How the pieces connect, as read in the deposited texts.**

- Income tax starts from federal AGI: 12-701(a)(20) defines "Connecticut adjusted gross income" as adjusted gross income with the listed modifications (IRC subject).
- 12-701(a)(20) subtracts Social Security benefits included in federal AGI: in full below income thresholds, and above them the excess over 25% of benefits or of the IRC section 86(b)(1) excess (2026 Supplement text).
- 12-704e: the credit is a percentage of the earned income credit claimed and allowed under IRC section 32, refundable as an overpayment; it is not counted as income for state or federal means-tested programmes.
- 17b-104(a): the Commissioner of Social Services administers state supplementation to the SSI programme "provided for by the Social Security Act and state law" (SSA Title XVI); 17b-112 requires families on temporary family assistance to cooperate with child support enforcement under title IV-D.
- 17b-105a to 17b-105i (in chapter 319s) cover SNAP administration, which is federal (food-and-nutrition-act-of-2008).
- Chapter 567 defines "employment" by reference to the Federal Unemployment Tax Act (IRC ch. 23).
- Unverified (general knowledge): the TFA programme is Connecticut's TANF plan under SSA Title IV-A; UI benefits are federally taxable under IRC section 85.

**Terms.** The terms page (https://www.cga.ct.gov/asp/menu/disclaimer.asp) is under `/asp/menu/`, which robots.txt disallows, so it was not re-read on 2026-10-20. The 2026-09-23 reading said the online documents "are not official copies"; nothing restricts reuse. The `/current/pub/` and `/2026/sup/` pages carry no terms notice. robots.txt allows both paths. Verdict: clean. Each subject's `SOURCE-LICENSE.md` records the detail.

**What was left out.** Only the unannotated text was deposited. The Legislative Commissioners' Office's source notes ("(P.A. ...)"), history notes, case annotations, cross-reference notes, chapter front notes and "(Formerly Sec. ...)" catchline notes were removed. One catchline in the chapter 319s Supplement (17b-99a) keeps the LCO's pointer to an amended subsection, because it marks a deferred amendment.

**Currency.** The General Statutes revised to January 1, 2025, with the 2026 Supplement revised to January 1, 2026. Changes from 2026 sessions are not included.

**Access note.** The host's TLS chain does not verify against Python's certifi bundle, so pages were fetched with curl using the Windows trust store, with the same User-Agent.

**Gaps.** The Regulations of Connecticut State Agencies were not sourced: no UI or TFA regulations, and no DRS income tax regulations. Chapter 229 also covers withholding, pass-through entities and tax preparers, which matter less here.
