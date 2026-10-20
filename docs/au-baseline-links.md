# Links between the Australian baseline encodings

Status: register, 21 October 2026. Covers the 118 baseline encodings at
`subjects/au/<slug>/encodings/baseline-2026-10/` (Commonwealth) and
`subjects/au/wa/<slug>/encodings/baseline-2026-10/` (Western Australia).

Many baselines take as an input a fact that another baseline decides. This register lists each such link: the
importing Act and its input, the exporting Act and the decision that answers it, and whether the types line up.
**None of the links is joined in L4 yet.** The stable `l4` cannot import a module from another folder; see the next
section. Each encoding still asks the other Act's answer as a fact, so each stays checkable on its own.

## Why nothing is joined: how `l4` resolves IMPORT

Tested with the stable `l4` from the VS Code extension 1.6.98, with `JL4_LIBRARY_PATH` unset. Read against
`l4-ide` at d84dcb3d8: `jl4-lsp/src/LSP/L4/Rules.hs` (`GetImports`, `resolveLibrary`) and
`jl4-core/src/L4/Import/Resolution.hs`.

1. **IMPORT takes a bare module name only.** `GetImports` turns every import into
   ``takeBaseName (the name as written)``. The source comment says "we curently don't allow any relative or absolute
   file paths, just bare module names". Probes:
   - ``IMPORT `../../b/enc/bmod` `` is read as `bmod`, and fails with "I could not find a module with this name: bmod".
   - `IMPORT "../../b/enc/bmod.l4"` is a parse error. So is the form without `.l4`.
     The skill's `references/builtins.md` shows `IMPORT "my-custom-lib.l4"`, but this binary does not accept it.
2. **The places searched** are fixed, in this order:
   1. `$JL4_LIBRARY_PATH`, which is one directory and, when set, turns the embedded standard library off;
   2. the project root, which `l4 run` sets to the importing file's own directory;
   3. the importing file's directory;
   4. the standard library embedded in the binary;
   5. `%APPDATA%\jl4\libraries`;
   6. the extension's `libraries` folder.

   The working directory does not count. Running `l4 run ../../a/enc/amod.l4` from inside `b/enc` still fails.
   `l4 run` has no root or search-path option.
3. **Within one folder, IMPORT works.** Imported modules' `#ASSERT`s are not re-run in the importer.
4. **A name defined in two modules cannot be used.** This holds whether both definitions are imported, or one is
   local and one imported: a local definition does not shadow an imported one. Every use then fails with "There are
   multiple definitions for the identifier". This holds for functions and for `DECLARE`d types. Across the 118
   baselines, 180 names are defined in more than one encoding. Examples:
   - `the lesser of` in 21 encodings, `the greater of` in 18;
   - `age in completed years` in 8;
   - `My circumstances`, `My offence` and `Offence` in 4 each;
   - `Which income tier am I in` in 3;
   - `My conviction` in 2.

   Proof on a real link: Local Government Act and Rates and Charges were copied side by side into a scratch folder,
   and the first was given ``IMPORT `rcrd-rebates` ``. It then fails twice, on `the lesser of` and `the greater of`,
   which both modules define.
5. **Modules may not import each other.** A cycle is an error ("Your module depends on itself"). Where two baselines
   each ask the other's answer (the Commonwealth Electoral Act and the Constitution, link A22 and B24), at most one
   direction can ever be joined.

Copying an exporting module into the importer's folder would make IMPORT resolve. It is not done: that is a copy of
law between encodings, and the copy would drift from its source.

### What the language would need

- **Path imports, relative to the importing file.**
  - The change: ``IMPORT `../../../../wa/rates-and-charges-rebates-and-deferments-act-1992/encodings/baseline-2026-10/rcrd-rebates` ``
    (or a string form) resolves against the importing file's directory instead of being cut to its base name.
  - In the source, this is `mkImportPath` and `resolveImportUri` in `Rules.hs`, which call `takeBaseName`.
  - The importer-relative tier already builds `takeDirectory importer </> name <.> "l4"`, so passing the path through
    would nearly suffice. `Resolution.hs` has a matching `relativeCandidate` marked `TODO`.
  - Alternatives: a project file at the repository root that lists library folders; or a multi-directory search path
    that does not switch off the embedded standard library (`JL4_LIBRARY_PATH` does).
- **Namespace control.** Any of the following would do:
  - qualified imports (`IMPORT x AS rcrd`, then `rcrd.Am I entitled ...`);
  - selective imports (`IMPORT x (`Am I entitled to a rebate or deferment`)`);
  - letting a local definition shadow an imported one.

  Without one of these, most joins fail on helper and type names even after paths work. Examples:
  - `the lesser of`, as in item 4 above;
  - `My conviction` in Spent Convictions and Young Offenders;
  - `My circumstances` in the Commonwealth Electoral Act and the Constitution.
- **Either order of definition, or a way to break cycles.** For the pairs in item 5 above, one side keeps its input.
  That is a drafting choice, not a language need.

Until then, the link is kept by convention: the importer's `@desc` names the other Act, and the exporter's
comment says "this is its answer".

## How the links were found

The script `find_links.py` (in the session scratchpad) searched every baseline's `NOTES.md` and module comments for
two things:

- another baseline's short title or slug;
- words such as "baseline", "asked as a fact", "input", "answered" and "decides".

That gave 288 pairs that mention another Act, and 168 with one of those words. Each pair below was then read by hand,
and the exporter's decisions listed. False matches were dropped. For example, "Administration Act" matched "Taxation
Administration Act", "Guardianship and Administration Act" and "Land Administration Act". "Criminal Code" in the
Commonwealth Statutory Declarations and Biosecurity baselines is the Commonwealth Code, which is not in Commons.

Line numbers are those of the module in the baseline folder on 21 October 2026.

The "Types" column of tables A and B uses three answers:

- **yes**: the exporter's result has the importer's type;
- **adapter**: a small expression converts one to the other;
- **no**: the exporter does not decide the same thing.

Every exporter decision takes its own facts, usually a record. A joined importer would have to ask those facts in
place of its single input. That is why the plan was to keep the old input-taking decision beside a joined one.

## A. Links ready to join (the exporter's decision answers the input; types line up)

| # | Importing Act: input | Exporting Act: decision | Types |
|---|---|---|---|
| A1 | wa/local-government-act-1995 `lga-rates.l4` 398, 443, 468: `I am entitled to a rebate or deferment` (BOOLEAN; ss 6.51(4) and the instalment and discount sections) | wa/rates-and-charges-rebates-and-deferments-act-1992 `rcrd-rebates.l4` 275: `Am I entitled to a rebate or deferment` (`My cards and circumstances`, `My home`, 2 BOOLEAN → BOOLEAN) | yes. At 398 and 443 the input also covers a concession "the local government resolves", so a joined decision would be `RCRD answer OR that resolution`. Blocked by `the lesser of` and `the greater of`, which both define. |
| A2 | wa/emergency-services-levy-act-2002 `esl-levy.l4` 311: `I am entitled to a rebate or deferment of the levy` | the same; and `Does my rates application also cover the emergency services levy` (`rcrd-rebates.l4` 242) | yes; the same helper clash |
| A3 | wa/dog-act-1976 `doga-owner.l4` 243, 328: `I am an eligible pensioner` (RCRD s 3(1)) | RCRD `Am I an eligible pensioner` (`rcrd-rebates.l4` 133; `My cards and circumstances` → BOOLEAN) | yes |
| A4 | wa/cat-act-2011 `cat-owner.l4` 311: `I am a pensioner` (its `@desc`: eligible pensioner under the RCRD Act) | RCRD `Am I an eligible pensioner` | yes |
| A5 | wa/duties-act-2008 `Purchase`: `each transferee is a concessional first home owner` (s 142A) | wa/first-home-owner-grant-act-2000 `fhog-grant.l4` 774: `Am I a concessional first home owner for duty` (Application → BOOLEAN). Its comment says "The WA Duties Act baseline asks this as a fact; this is its answer." | yes. The FHOG application lists every buyer, which matches "each transferee". |
| A6 | wa/births-deaths-and-marriages-registration-act-1998 `bdm-registration.l4` 453: `the death must be reported to a coroner` (s 44(5), "required under section 17(3) of the Coroners Act") | wa/coroners-act-1996 `cor-deaths.l4` 171: `section 17(3) requires me to report` (Reporter, Death → BOOLEAN; a helper, not exported) | yes |
| A7 | wa/juries-act-1957 `ja-juror.l4` 81: conviction field `it is spent` | wa/spent-convictions-act-1988 `sca-spent.l4` 306: `Is my conviction spent` (`My conviction` → BOOLEAN) | yes |
| A8 | wa/spent-convictions-act-1988 `sca-spent.l4` 131: `it has stopped counting under Young Offenders Act 1994 s 189` | wa/young-offenders-act-1994 `yoa-diversion.l4` 526: `Has my youth conviction stopped counting` (`My conviction`, DATE → BOOLEAN) | yes. Blocked by name: both encodings `DECLARE` a type named `My conviction`. |
| A9 | wa/criminal-code-act-compilation-act-1913 `cc-offences.l4` 400: `the offender is in a family relationship with me` (s 221(1)(a), borrowed from the Restraining Orders Act) | wa/restraining-orders-act-1997 `ro-orders.l4` 98: `Are we in a family relationship` (`The relationship between us` → BOOLEAN) | yes |
| A10 | wa/road-traffic-authorisation-to-drive-act-2008 `rtad-drivers.l4` 622: `the Fines Enforcement Act Part 3 applies` | wa/fines-penalties-and-infringement-notices-enforcement-act-1994 `fpine-infringements.l4` 101: `Does Part 3 apply to my infringement notice` (`My infringement` → BOOLEAN) | yes |
| A11 | wa/duties-act-2008 `da-vehicles.l4` 33: `it must be licensed under the Vehicles Act` | wa/road-traffic-vehicles-act-2012 `rtva-licensing.l4` 173: `Must my vehicle be licensed` (`My vehicle` → BOOLEAN) | yes |
| A12 | wa/motor-vehicle-third-party-insurance-act-1943 `mvtpi-ctp.l4` 90: vehicle field `it is required to be licensed under the Vehicles Act` | the same RTVA decision | yes |
| A13 | wa/road-traffic-vehicles-act-2012 `rtva-licensing.l4` 376: `the duty` (NUMBER, vehicle licence duty on transfer) | wa/duties-act-2008 `da-vehicles.l4` 76: `What vehicle licence duty must I pay` (dutiable value, heavy vehicle, R → NUMBER) | yes. RTVA's input may also include penalty tax, which Duties does not compute. |
| A14 | wa/motor-vehicle-and-workplace-accidents-catastrophic-injuries-act-2016 `mvwaci-ciss.l4` 126: `I am a worker under the Workers Compensation and Injury Management Act 2023` | wa/workers-compensation-and-injury-management-act-2023 `wcima-compensation.l4` 152: `Am I a worker` (`My engagement`, `Prescribed class`, BOOLEAN → BOOLEAN) | yes |
| A15 | wa/civil-liability-act-2002 `cla-damages.l4` 106: `it is a claim against my employer under Part 7 Division 2 of the WCIMA Act` | WCIMA `wcima-compensation.l4` 572: `Does Division 2 apply to my claim` (Defendant, … → BOOLEAN) | yes |
| A16 | wa/health-services-act-2016 `hsa-charges.l4` 155: `I am an eligible person under the Health Insurance Act 1973` | health-insurance-act-1973 `hia-medicare.l4` 133: `Am I an eligible person` (`Me` → BOOLEAN) | yes |
| A17 | higher-education-support-act-2003 `hesa-help.l4` 508: `no Medicare levy payable under s 8` (s 154-1(2)) | medicare-levy-act-1986 `mla-levy.l4` 244: `Is our family income under the family threshold` (Taxpayer → BOOLEAN) | yes |
| A18 | medicare-levy-act-1986 `mla-levy.l4` 110 and others: `taxable income` (NUMBER) | income-tax-assessment-act-1997 `itaa-income.l4` 65: `What is my taxable income` (assessable income, deductions → NUMBER) | yes. Blocked by name: MLA and ITAA both define `the lesser of`. |
| A19 | therapeutic-goods-act-1989 `tga-vaping.l4` 437: `the Customs Act 1901 prohibits the importation` | customs-act-1901 `ca-traveller.l4` 282: `Are my goods prohibited imports` (Prohibition, BOOLEAN → BOOLEAN) | yes |
| A20 | wa/home-building-contracts-act-1991 `hbc-contracts.l4` 97: field `needs a building permit` | wa/building-act-2011 `ba-house.l4` 143: `Do I need a building permit` (Work → BOOLEAN) | yes |
| A21 | paid-parental-leave-act-2010 `ppl-parent.l4` 794: `charge percentage` (NUMBER) | superannuation-guarantee-administration-act-1992 `sgaa-guarantee.l4` 277: `the charge percentage` (12) | yes. PPL asks it per year; SGAA's deposited text sets one figure, 12, with no table of dates. |
| A22 | commonwealth-electoral-act-1918 `cea-elector.l4` 37: `I am incapable of being chosen under section 44 of the Constitution` | commonwealth-of-australia-constitution-act-1900 `const-candidate.l4` 161: `Am I incapable of being chosen under section 44` (`My circumstances` → BOOLEAN) | yes. Blocked by name: both `DECLARE` a type named `My circumstances`, with different fields. It is also one half of a cycle (B24). |

## B. Partial links (an adapter is needed, or the exporter answers only part of the input)

| # | Importing Act: input | Exporting Act: decision | Types / gap |
|---|---|---|---|
| B1 | wa/cremation-act-1929 `cra-cremation.l4` 92: Death field `a certificate of cause of death has been provided` (s 8A(a): a certificate under BDM s 44) | wa/births-deaths-and-marriages-registration-act-1998: `Which doctor must certify the cause of death` (→ `Certifying doctor`, including "no certificate: the death is reported to the coroner") | no. BDM says who must certify; Cremation asks whether a certificate was given. With A6 this makes a chain, Coroners → BDM → Cremation. The Coroners NOTES (finding 3) and the Cremation baseline agree: read literally, a reportable death with no s 44 certificate cannot be cremated. |
| B2 | wa/public-trustee-act-1941 `pta-small-estates.l4` 52: `the deceased left a will` | wa/wills-act-1970 `wills-making.l4`: `Is my will valid` (dates, `My will's signing`, `Another route`, … → BOOLEAN) | adapter. "Left a will" is wider than "left a valid will". |
| B3 | wa/public-trustee-act-1941 `pta-small-estates.l4` 62: `the person first entitled to administration is willing, capable and resident in WA` (borrowed from Administration Act s 25) | wa/administration-act-1903 `aa-estates.l4`: `May I be granted administration` (s 25 → BOOLEAN) | no. s 25 says who may be granted administration, not who is "first entitled". Willingness and capacity stay facts. |
| B4 | wa/administration-act-1903 `aa-estates.l4` 186: `the value the will disposes of` (NUMBER, 0 if there is no will) | Wills Act `Is my will valid` | adapter (`IF valid THEN value ELSE 0`). The value itself stays a fact. |
| B5 | wa/family-provision-act-1972 `fp-claims.l4` 291: `the estate passed wholly or partly on intestacy` | Wills Act `Is my will valid`, with Administration Act s 14 | no. Partial intestacy depends on what a valid will disposes of. That is a fact in both encodings. |
| B6 | wa/security-and-related-activities-control-act-1996 `sarca-licensing.l4` 301: `a law lets me not disclose it` (s 4B(3), "spent") | Spent Convictions `Is my conviction spent`, or Young Offenders `Has my youth conviction stopped counting` | adapter (OR of the two). Importing both hits the `My conviction` clash, as in A8. |
| B7 | wa/juries-act-1957 `ja-juror.l4` 89: `I am enrolled to vote at Legislative Assembly elections` | wa/electoral-act-1907 `ea-elector.l4` 125, 149: `Am I entitled to be enrolled`, `Am I an elector` | no. Being enrolled is a fact; the Electoral Act decides only entitlement. |
| B8 | wa/criminal-code-act-compilation-act-1913 `cc-offences.l4` 257: `I drove it in a way that is an offence under the Road Traffic Act 1974 s 60, 60A or 61` | wa/road-traffic-act-1974 `rta-road.l4` 435: `Am I driving at a reckless speed` (s 60A) | no. Only s 60A is decided; ss 60 and 61 are not. |
| B9 | wa/minimum-conditions-of-employment-act-1993 `mce-employee.l4` 342: `I am experiencing family and domestic violence` (ROA s 5A) | Restraining Orders `Has the respondent committed family violence against me` (`ro-orders.l4` 133) | adapter. Restraining Orders needs a respondent and the relationship. |
| B10 | wa/motor-vehicle-third-party-insurance-act-1943 `mvtpi-ctp.l4` 283: `the injury is catastrophic under the MVWA(CI) Act` | wa/motor-vehicle-and-workplace-accidents-catastrophic-injuries-act-2016 `mvwaci-ciss.l4` 179: `Am I eligible to participate in the CISS` | no. No decision named "catastrophic injury" was found; eligibility is the nearest. |
| B11 | wa/civil-liability-act-2002 `cla-damages.l4` 105: `the Motor Vehicle (Third Party Insurance) Act 1943 applies to the damages` | MVTPI: `Must my vehicle be covered…` and `Is my vehicle covered… right now` (`mvtpi-ctp.l4` 121, 200) | no. MVTPI decides cover, not whether the damages are a CTP claim. |
| B12 | wa/workers-compensation-and-injury-management-act-2023 `wcima-compensation.l4` 570: `the Motor Vehicle (Third Party Insurance) Act 1943 applies` | the same | no |
| B13 | WCIMA `wcima-compensation.l4` 299: `a minimum amount applies to me under the Minimum Conditions of Employment Act 1993` | MCE `mce-employee.l4` 64: `Does this Act give me its minimum conditions` | no. "Gives me its conditions" is not "sets a minimum amount". MCE has no minimum-wage decision. |
| B14 | fair-work-act-2009 `fwa-employee.l4` 422: `if my State's law declares it a public holiday` (s 115) | wa/public-and-bank-holidays-act-1972 `pbha-holidays.l4` 237: `Is this day a public holiday for me in WA` | adapter. The answers line up (BOOLEAN), but the day is a `Holiday` enum in FWA and is described differently in PBHA. PBHA's NOTES asks for this link (Chloe's c042). |
| B15 | fair-work-act-2009 `fwa-employee.l4` 437: `if the super guarantee charge would otherwise apply to me` | SGAA `sgaa-guarantee.l4` 304: `Must super be paid for me on this pay` (`About me` → `Super answer`) | adapter (enum → BOOLEAN) |
| B16 | higher-education-support-act-2003 `hesa-help.l4` 509: `Medicare levy reduced under s 8` | medicare-levy-act-1986 `mla-levy.l4` 264: `By how much is my levy reduced for my family` (NUMBER) | adapter (`> 0`) |
| B17 | HESA `hesa-help.l4` 466: `taxable income less FHSS released amount` | ITAA `What is my taxable income` | adapter. The FHSS released amount is not encoded. |
| B18 | income-tax-assessment-act-1997 `itaa-income.l4` 68-: restates ITRA s 3 and Sch 7 Pt I; `itaa-business.l4` 13: company rate passed in | income-tax-rates-act-1986 `itra-rates.l4` 309, 326, 453: `How much tax is on my taxable income`, `…, simply`, `How much tax must my company pay` (→ `Answer`) | adapter (`Answer`). This is duplicated law today, and the strongest case for a join once imports work. |
| B19 | child-support-registration-and-collection-act-1988 `csrc-collection.l4` 262: `the weekly deduction rate` | child-support-assessment-act-1989 `csa-formula.l4` 383: `How much child support must I pay` (→ `My assessment`) | no. The rate in the Registrar's notice is not the assessed annual rate. CSRC's NOTES asks for the link. |
| B20 | privacy-act-1988 `pa-individual.l4` 483: `the agreement` (`Debt agreement`: day made, how and when ended) | bankruptcy-act-1966 `bda-debt-agreements.l4` 579, 635: `Has my debt agreement ended`, `From when must my agreement come off the Index` | adapter (record). The dates stay facts. |
| B21 | privacy-act-1988 `pa-individual.l4` 262: `the Do Not Call Register Act or Spam Act applies to it` (APP 7.8) | do-not-call-register-act-2006 `dnc-consumer.l4` 158: `Does this Act reach the call` (Call → BOOLEAN), OR spam-act-2003 `sa-messages.l4` 113, 129: `Is this a commercial electronic message` with `Does it have an Australian link` | adapter (OR over two Acts' records). **Stale note:** DNC NOTES.md line 92 says the Spam Act "has no baseline yet"; it now has one. |
| B22 | wa/guardianship-and-administration-act-1990 `gaa-incapacity.l4` 191: `witnesses authorised to take declarations` (NUMBER) | wa/oaths-affidavits-and-statutory-declarations-act-2005 `oasda-witnesses.l4` 197: `May I witness this statutory declaration` (per witness → standing) | adapter (count over a list of witnesses) |
| B23 | a-new-tax-system-australian-business-number-act-1999 `Me and my enterprise` (s 41: "enterprise" as in GST Act s 9-20) | a-new-tax-system-goods-and-services-tax-act-1999 `gst-registration.l4` 89: `Am I carrying on an enterprise` (`My activity` → BOOLEAN) | adapter (record fields) |
| B24 | commonwealth-of-australia-constitution-act-1900 `const-candidate.l4` 194, 222: `the Parliament has otherwise provided`, `I have the qualifications the Parliament has provided` (Electoral Act s 163) | commonwealth-electoral-act-1918 `cea-candidate.l4` 77: `May I stand` | no, and it is a cycle with A22. Only one direction can be joined. A22 is the natural one, since the Electoral Act applies s 44. |
| B25 | wa/tobacco-and-other-products-control-act-2006 `topca-minor.l4` 119: `the prescribed therapeutic conditions are met` ("therapeutic vaping product" is TGA-defined) | therapeutic-goods-act-1989 `tga-vaping.l4` 73: `Are these vaping goods` | no. TGA decides "vaping goods", not "therapeutic good". The NOTES of both record the same reading. |
| B26 | wa/school-education-act-1999 `sea-schooling.l4` 43, 300: "approved VET course" (a comment; the leaving option is asked as an `Option`) | wa/vocational-education-and-training-act-1996 `vet-training.l4` 57: `Is my course an approved VET course` (3 BOOLEAN → BOOLEAN) | adapter. SEA would need a field for the course. |
| B27 | medicare-levy-act-1986 `mla-levy.l4` 311 and a-new-tax-system-medicare-levy-surcharge-fringe-benefits-act-1999 `mlsfb-surcharge.l4` 113: `a complying health insurance policy`; both: tier thresholds | private-health-insurance-act-2007 `phi-cover.l4` 151, 344: `Do I have hospital cover`, `Which income tier am I in` | no. PHI itself asks "insured under a complying policy" as a fact. The indexed tier thresholds are inputs in all three. `Which income tier am I in` is defined in all three, so it would clash. |

## C. No exporter: the other baseline does not decide it either

| # | Importing Act(s): input | Other Act | Why not joinable |
|---|---|---|---|
| C1 | wa/minimum-conditions-of-employment-act-1993 `mce-employee.l4` 55: `my employer is a national system employer` (FW Act s 26) | fair-work-act-2009 | FWA's `Am I a national system employee` takes the same fact as an input. |
| C2 | age-discrimination-act-2004: whether an enterprise agreement term "has effect" (s 39(8)) | fair-work-act-2009 | Not encoded in FWA. ADA NOTES finding 6. |
| C3 | a-new-tax-system-family-assistance-act-1999 `fa-families.l4` 275 (`I am a member of a couple`); FA Administration; paid-parental-leave-act-2010 (`partner`, `Australian resident`); CSRC (`social security pension or benefit`); income-tax-rates-act-1986 (`an eligible pensioner`); wa/land-tax-assessment-act-2002 (ss 26A, 26B qualifications) | social-security-act-1991 | The SSA baseline encodes the age pension and DSP only. It has no "member of a couple", "Australian resident" or "partner" decision. |
| C4 | bankruptcy-act-1966 `bda-bankruptcy.l4` 95 and `bda-debt-agreements.l4` 124 (`the Social Security Act rate`); aged-care-act-2024 `aca-care.l4` 599 (`the basic age pension amount`); FA Administration `faa-administration.l4` 534 (`the small debt amount`, s 1237AAA) | social-security-act-1991 | The indexed figures (point 1064-B1, s 1237AAA) are not in the SSA baseline either. |
| C5 | medicare-levy-act-1986 `mla-levy.l4` 94: `entitled to the s 160AAAA rebate` | ITAA 1936 | Not deposited. The ITAA 1997 baseline does not cover s 160AAAA. |
| C6 | wa/water-services-act-2012 `wsa-charges.l4` 87, 145: `I am the owner of the land` (LGA s 1.4) | wa/local-government-act-1995 | LGA asks "owner" as a fact too. |
| C7 | wa/juries-act-1957 `ja-juror.l4` 105 (`represented person`); wa/restraining-orders-act-1997 `ro-orders.l4` 270 (`I have a guardian`); NDIS | wa/guardianship-and-administration-act-1990 | Whether an order exists is a fact about a Tribunal order. |
| C8 | CSRC `csrc-collection.l4` 572: `the Bankruptcy Act bar is taken to reach child support deductions` | bankruptcy-act-1966 | A question of reading, which the Bankruptcy baseline's finding 4 raises but does not decide. |
| C9 | Visa held: australian-citizenship-act-2007, commonwealth-electoral-act-1918, foreign-acquisitions-and-takeovers-act-1975, health-insurance-act-1973, superannuation-guarantee-administration-act-1992, wa/electoral-act-1907 | migration-act-1958 | The visa a person holds is a fact. The Migration baseline decides grant criteria, not holding. |
| C10 | "Marriage", "divorce order", parental-responsibility orders: wa/wills-act-1970, wa/births-deaths-and-marriages-registration-act-1998, migration-act-1958, australian-passports-act-2005 | marriage-act-1961, family-law-act-1975 | Facts about a marriage or an order. |
| C11 | Kind of offence: wa/children-s-court-of-western-australia-act-1988 (indictable or summary, Criminal Code s 5); wa/security-and-related-activities-control-act-1996 (disqualifying offence); wa/electoral-act-1907 | wa/criminal-code-act-compilation-act-1913 | The Criminal Code baseline does not classify offences by mode of trial or maximum penalty. |
| C12 | wa/duties-act-2008 `da-property.l4` 461: `it must be registered under the Transfer of Land Act` | wa/transfer-of-land-act-1893 | The TLA baseline has no "must be registered" decision. |
| C13 | wa/magistrates-court-civil-proceedings-act-2004 `mccpa-minor-cases.l4` 94, 97: tenant and lessor under the Residential Tenancies Act | wa/residential-tenancies-act | Borrowed terms, asked as facts. No tenancy-status decision was found. |
| C14 | a-new-tax-system-family-assistance-act-1999 `fa-families.l4` 462: "parental leave pay" | paid-parental-leave-act-2010 | Asked as a fact. PPL computes eligibility, not the payment's receipt. |
| C15 | wa/legal-profession-uniform-law-application-act-2022: whether an arbitration agreement binds | wa/commercial-arbitration-act-2012 | Not checked as a decision. LPULAA NOTES leaves it to that Act. |

## D. Pointers and consistency notes (no input is taken)

These need no join. They record that two baselines read a shared point the same way, or divide ground.

- **Coroners and Cremation.** Coroners NOTES finding 3 answers the Cremation baseline's s 8A(a) finding from the
  other side (see B1).
- **Wills, Family Provision and Administration.** Family Provision NOTES line 47 follows k084 through all three
  Acts. Wills NOTES points to Administration for intestacy and to Family Provision for claims. Administration points
  to Family Provision (s 60A) and to the Public Trustee route.
- **Strata Titles and Community Titles.** Community Titles follows the Strata baseline's patterns and readings (for
  example, a 5% change as 5% of the notified proportion). The Transfer of Land, Dividing Fences and Water Services
  baselines mention lot owners under either Act as facts.
- **Fair Work Act consistency:**
  - Long Service Leave (WA): FWA leaves long service leave to State law.
  - Minimum Conditions (WA): leave matches for a 38-hour employee.
  - Public and Bank Holidays (WA): see B14.
  - Juries (WA): shares the hypothetical $400 a day and 15 days.
  - Age Discrimination: general protections are out of both.
- **Electoral (WA) and Commonwealth Electoral.** The two read the age-18 day the same way. Claims under the other Act
  are facts.
- **Divisions of ground:**
  - Magistrates Court Act and Magistrates Court (Civil Proceedings) Act;
  - Legal Profession Uniform Law (WA) and its Application Act;
  - Children's Court and Young Offenders (proceedings for an offence go to Young Offenders s 45);
  - Workers Compensation and Civil Liability.
- **Shared figures under the same names:** Road Traffic Act and Road Traffic (Authorisation to Drive) Act (speeding
  demerit points). The figures are duplicated today, and the names would clash on import.
- **Other agreements:**
  - Road Traffic (Vehicles) Act and Road Traffic Act;
  - School Education and VET (see B26);
  - Foreign Acquisitions and Takeovers and Duties (a permanent resident is not foreign for either);
  - ASIC Act and Competition and Consumer (credit card debt collection falls under ASIC Act s 12DJ);
  - ASIC Act and Corporations;
  - Biosecurity and Customs (two duties on one card);
  - Betting Control, Interactive Gambling and Casino Control;
  - Medicare Levy Surcharge (Fringe Benefits) and Medicare Levy;
  - Private Health Insurance and Medicare Levy (tier names);
  - Income Tax Rates and ITAA 1997 (see B18);
  - NDIS and Social Security (the DSP neither helps nor hinders NDIS access);
  - Oaths, Affidavits and Statutory Declarations (WA) and the Commonwealth Statutory Declarations Act.
- **Pointers only:**
  - Life Insurance to SIS (cover under 25: SIS s 68AAC) and to Bankruptcy;
  - Australian Organ and Tissue Donation (Cth) to the WA Human Tissue and Transplant Act s 22 (opt-in);
  - Business Names to ABN;
  - FA Administration to the FA Act (its NOTES asks for wiring: the FA Act computes rates, the Administration Act
    takes them as given);
  - Family Law to Child Support (Assessment);
  - Patents to Copyright (s 35(6));
  - Housing Act (WA) to Residential Tenancies;
  - Commercial Arbitration to the Legal Profession Uniform Law;
  - Workers Compensation to Civil Liability;
  - Home Building Contracts to Building Services (not in Commons).
- **Rates and Charges itself** (NOTES lines 67 and 96) asks for its `Am I entitled to a rebate or deferment` to be
  linked to the Local Government Act and Emergency Services Levy inputs: links A1 and A2.

## Counts

| Kind | Links |
|---|---|
| A: ready to join | 22 |
| B: partial | 27 |
| C: no exporter | 15 |
| D: pointers and consistency | about 40 pairs |
| **Joined in L4** | **0** |

Of the 22 A links, at least 5 would still fail on a duplicated name after path imports existed:

- A1 and A2 (`the lesser of`, `the greater of`);
- A8 (`My conviction`);
- A18 (`the lesser of`);
- A22 (`My circumstances`).

The other A links were not checked for clashes name by name.

## What to do when the language allows it

1. Join A1-A4 first. The Rates and Charges baseline was written to answer A1 and A2. Then join A5, A6 and A10-A12:
   one-way, one decision each.
2. Join B18 (ITAA and ITRA). It removes duplicated law.
3. For each join, keep the input-taking decision. Add a decision that calls the exporter. Add one to three cases that
   run through both encodings.
4. Before joining, rename or qualify the clashing helpers: `the lesser of`, `the greater of`, `age in completed
   years`, `is on or after`. A shared helper module beside the prelude would also do, but it would be the first file
   in Commons that more than one encoding depends on.
