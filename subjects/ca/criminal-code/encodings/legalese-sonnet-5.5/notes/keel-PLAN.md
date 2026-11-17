# PLAN.md -- the Criminal Code (Canada), R.S.C., 1985, c. C-46: the keel, and what each of the 32 part agents encodes

Status (2026-11-12, written by keel agent `ccc-k`): the core `ccc-core.l4`, the definitions (`ccc-definitions.l4`, `ccc-interpretation.l4`) and their tests exist and compile on the stable binary; the numbers are in `NOTES.md`.
This plan is the hand-over to the part agents. Each seam below is marked **[T]** when it was checked in the text (a cross-reference or the provision's own words) and **[H]** when it was seen only from the headings and the structure of the Code, so the part must check it against the text.
The text is a plain-text rendering, made by a converter script, of the Justice Laws Website consolidation (current to 2026-09-30); it is not the official text, and nothing here claims to be verified against the official text.

## 1. What a part receives, and what it may do

- A part gets ONE read-only module of mine, `ccc-core.l4` (it imports `prelude` and `daydate` only). It does NOT get `ccc-definitions.l4` or `ccc-interpretation.l4`: the brief gives each part the core only, and a part is in a separate sandbox from every other part. (Assumption stated for the lead: if the lead also copies the definitions modules into the sandboxes, a part could call `s 2 ...` instead of taking an input; the names below were chosen so that the input and the function agree, so the swap at the merge is mechanical.)
- So every answer a part needs from section 2, section 2.1, section 2.2, section 2.3, section 3 or section 3.01, and every answer it needs from another part, is an INPUT of its own (a `GIVEN`), named for the section it comes from (section 3 below: the seam rules; section 4: the section 2 terms).
- A part never edits the core and never waits for it. A type or constructor the core lacks is defined in the part's own module under its own prefix and recorded in `NEEDS-CORE.md` in its sandbox; the lead hoists it into the core at the merge.
- Every module of part `X` begins with `X-` (for example `ccc7-privacy.l4`, `ccc7-privacy-tests.l4`).

### The naming rule (every part follows it)

A name defined in two modules that are imported together cannot be used at all, so no two parts may define the same name. Every top-level name (function, constant, type constructor not in the core) a part defines **begins with the section label it implements, in the form `s 4(2)(a) ...`** (the Act's own numbering: `s 515(6)(a) the accused is charged with an offence in the list`, `s 487.04 primary designated offence`, `sch XXII.1 the offence is listed`). Parentheses inside a backtick name parse fine on the stable binary (checked). Types and constructors shared across parts live only in the core; a constructor a part declares itself begins with its section label too (a constructor name must be unique across all the part's enumerations as well as across parts).
- A function's name carries the section it implements and does not claim more than the section says: `s 515(10) the justice may order detention`, not `is the accused detained`. It answers `MAYBE BOOLEAN` (or a `MAYBE` of a core type): `JUST FALSE` only where the text says no in its own words; `NOTHING` everywhere else. Every branch that answers no carries `-- FALSE-kind (the text says no in its own words): "<quoted words>"` and every branch that answers "not covered" carries `-- NOTHING-kind (<why>)`, with <why> one of: silent, list not closed, includes, undefined term, points outside the text, limited by its own wording. (`NOTES.md` of the keel shows the rule applied to every definition; the keel's `work/lint-kinds.py` and `work/verify-quotes.py` check it mechanically, and the lead may run them over the parts.)
- Dates are `Date day month year` (never a `YMD` of your own). Money is a `NUMBER` of dollars. Periods keep the text's units: use the core's `Length of time` (years, months, days, `less a day`), never a day count.

## 2. The core, one line per type (`ccc-core.l4`, 214 lines, `DECLARE` and constants only)

- **Province or territory**: the thirteen provinces and territories as s 2 "superior court of criminal jurisdiction" names them (Ontario, Quebec, Nova Scotia, British Columbia, Prince Edward Island, Newfoundland and Labrador, New Brunswick, Manitoba, Saskatchewan, Alberta, Yukon, Northwest Territories, Nunavut)
- **Party**: one actor type for every regulative rule, 36 constructors: `the accused`, `the offender`, `the victim`, `a witness`, `a juror`, `the jury`, `counsel for the accused`, `the prosecutor`, `the Attorney General`, `the Attorney General or Solicitor General of the province`, `the Attorney General of Canada`, `the Director of Public Prosecutions`, `the informant`, `a peace officer`, `a public officer`, `a justice`, `a provincial court judge`, `a judge`, `the court`, `a court of criminal jurisdiction`, `a superior court of criminal jurisdiction`, `a court of appeal`, `the Supreme Court of Canada`, `a Review Board`, `the clerk of the court`, `a surety`, `a probation officer`, `a supervisor`, `the keeper of a prison`, `the Correctional Service of Canada`, `the Parole Board of Canada`, `the Minister of Justice`, `the Governor in Council`, `an organization`, `a representative of an organization`, `a senior officer`
- **Mode of proceeding**: `by indictment`, `on summary conviction`
- **Class of offence**: `an indictable offence`, `an offence punishable on summary conviction`, `an offence that the section makes both indictable and punishable on summary conviction` ("hybrid" and "dual procedure" occur nowhere in the text)
- **Decision on the charge**: `a finding of guilt`, `an acquittal`, `a verdict of not criminally responsible on account of mental disorder`, `a verdict of unfit to stand trial`, `a stay of proceedings`, `a withdrawal of the charge`, `a discharge at the preliminary inquiry`, `an order to stand trial`
- **Kind of homicide offence**: `first degree murder`, `second degree murder`, `manslaughter`, `infanticide` (a result Part VIII gives and ss 745 to 746.1 turn on)
- **Kind of sentence**: `an absolute discharge`, `a conditional discharge`, `a fine`, `imprisonment`, `a conditional sentence of imprisonment`, `an intermittent sentence`, `probation`, `restitution`, `forfeiture`, `a prohibition order`, `a victim surcharge`
- **Outcome of interim release**: `release on a release order without conditions`, `release on a release order with conditions`, `release on a release order with conditions and a surety`, `detention in custody`
- **Stage of the proceedings**: `investigation and arrest`, `compelling appearance and interim release`, `election, plea and pre-trial procedure`, `preliminary inquiry`, `trial`, `sentencing`, `appeal`, `after sentence`
- **Process document**: `an information`, `an indictment`, `a count`, `a summons`, `a warrant for arrest`, `an appearance notice`, `an undertaking`, `a release order`, `a recognizance`, `a subpoena`, `a search warrant`
- **Length of time**: record `years`, `months`, `days`, `less a day` (BOOLEAN): "two years less a day" is years 2, months 0, days 0, `less a day` TRUE
- **Imprisonment**: `no imprisonment is stated`, `imprisonment for life`, `imprisonment for a term of` (a `Length of time`)
- **Fine**: `no fine is stated`, `a fine in the discretion of the court`, `a fine of` (dollars)
- **Punishment**: record: `mode` (Mode of proceeding), `maximum imprisonment`, `minimum imprisonment`, `maximum fine`, `minimum fine`: ONE limb of a penalty provision, so a section with an indictable limb and a summary limb is answered with two
- **Provision of the Code**: record: `section` (NUMBER, the section number as a decimal: 380; 83.02; 320.1001, which sorts in the Code's order, so "sections 83.18 to 83.23" is a range test) and `subsection` (STRING: "" or e.g. "(2.01)")
- **constants**: `six months`, `ninety days`, `two years less a day`, `two years`, `five years`, `ten years`, `fourteen years` (each a `Length of time`; counts in the text: two years 83, five years 76, ten years 63, fourteen years 47)

Not in the core on purpose: the limb enumerations of the section 2 terms (they are in `ccc-definitions.l4`), a record of facts about the accused (every part asks its own plain inputs), and any rule.

## 3. Seam rules

- **R1.** A provision that NAMES OFFENCES BY SECTION NUMBER (a list: s 7, s 183, s 469, s 487.04, s 553, s 752, the Schedule to Part XXII.1, ...) is tested against the core record `Provision of the Code` (`section` as a decimal, `subsection` as a string). It needs no input from the part that owns the offence.
- **R2.** A provision that depends on what an offence IS (its class, its punishment, whether it is a "serious" or a "designated" offence by a definition elsewhere) takes that answer as an input: `Class of offence`, `Punishment`, or a MAYBE BOOLEAN for a yes/no definition.
- **R3.** Definitions other than section 2 and section 2.1 are scoped by their own lead-in ("In this Part", "In this section", "In this section and in sections ...": checked by grep of every lead-in), so each part encodes its own Part-scoped definitions. The same word defined in two Parts (`court`, `judge`, `offence`, `officer`, `order`, `victim`, `organization`, `serious offence`, `designated offence`, `public officer`, ...) is two different functions; the section label in the name keeps them apart (`s 183 offence`, `s 462.3 enterprise crime offence`).
- **R4.** An answer taken from another part is an INPUT named for the section it comes from, written `s <label> <what is asked>`, typed as the answering section answers: `MAYBE BOOLEAN` for a yes/no that can be "not covered", `BOOLEAN` only where the answering section is a closed "means", otherwise the core type (`Punishment`, `Fine`, `Class of offence`, `Kind of homicide offence`, `Outcome of interim release`, `Decision on the charge`). A caller must never turn NOTHING into FALSE.
- **R5.** A cycle between two parts (each reads the other) is two inputs, one each way; the lead joins them at the merge (the prohibition orders of ss 109 to 117 are split between ccc4 and ccc5, and the production regime of ss 278.1 to 278.98 between ccc9 and ccc10).

## 4. The section 2 and section 2.1 terms a part will need: input names and what the answer can be

Every section 2 term is a function in `ccc-definitions.l4` named `s 2 <term>`; its answer is `MAYBE BOOLEAN` (the one exception: `s 2 Attorney General` answers `MAYBE (LIST OF Party)`). A part that needs one takes the answer as an input named **`s 2 <term>: <the thing asked>`**, typed `MAYBE BOOLEAN`. The column "can be NOTHING" says whether the keel's function can answer "not covered" (an "includes" definition, a limited grant, a term it leaves undefined): if it can, the part must carry NOTHING through and never turn it into FALSE. (The facts each function takes are in its `GIVEN` lines in `ccc-definitions.l4`; each part's sandbox will not have them, so a part that wants the fact-level inputs asks the lead for that module.)

| term | the keel function | can be NOTHING |
| --- | --- | --- |
| 1 the term has the meaning it has in subsection 84(1) | `s 2.1 the term has the meaning it has in subsection 84(1)` | yes |
| Act | `s 2 Act` | yes |
| ammunition | `s 2.1 the term has the meaning it has in subsection 84(1)` | yes |
| antique firearm | `s 2.1 the term has the meaning it has in subsection 84(1)` | yes |
| appearance notice | `s 2 appearance notice` | yes |
| associated personnel | `s 2 associated personnel` | no |
| Attorney General | `s 2 Attorney General` | yes |
| audioconference | `s 2 audioconference` | no |
| automatic firearm | `s 2.1 the term has the meaning it has in subsection 84(1)` | yes |
| bank-note | `s 2 bank-note` | yes |
| bodily harm | `s 2 bodily harm` | no |
| Canadian Forces | `s 2 Canadian Forces` | no |
| cartridge magazine | `s 2.1 the term has the meaning it has in subsection 84(1)` | yes |
| cattle | `s 2 cattle` | no |
| clerk of the court | `s 2 clerk of the court` | yes |
| common-law partner | `s 2 common-law partner` | no |
| complainant | `s 2 complainant` | yes |
| counsel | `s 2 counsel` | no |
| count | `s 2 count` | no |
| court of appeal | `s 2 court of appeal` | no |
| court of criminal jurisdiction | `s 2 court of criminal jurisdiction` | no |
| criminal organization | `s 2 criminal organization` | yes |
| criminal organization offence | `s 2 criminal organization offence` | yes |
| cross-bow | `s 2.1 the term has the meaning it has in subsection 84(1)` | yes |
| day | `s 2 day` | yes |
| document of title to goods | `s 2 document of title to goods` | yes |
| document of title to lands | `s 2 document of title to lands` | yes |
| dwelling-house | `s 2 dwelling-house` | no |
| environment | `s 2 environment` | no |
| every one | `s 2 every one, person and owner` | yes |
| explosive substance | `s 2 explosive substance` | yes |
| firearm | `s 2 firearm` | no |
| firearm part | `s 2.1 the term has the meaning it has in subsection 84(1)` | yes |
| government or public facility | `s 2 government or public facility` | no |
| handgun | `s 2.1 the term has the meaning it has in subsection 84(1)` | yes |
| Her Majesty’s Forces | `s 2 Her Majesty’s Forces` | no |
| highway | `s 2 highway` | no |
| imitation firearm | `s 2.1 the term has the meaning it has in subsection 84(1)` | yes |
| indictment | `s 2 indictment` | yes |
| internationally protected person | `s 2 internationally protected person` | no |
| intimate partner | `s 2 intimate partner` | yes |
| justice | `s 2 justice` | no |
| justice system participant | `s 2 justice system participant` | no |
| mental disorder | `s 2 mental disorder` | no |
| military | `s 2 military` | yes |
| military law | `s 2 military law` | yes |
| motor vehicle | `s 2 motor vehicle` | yes |
| municipality | `s 2 municipality` | yes |
| newly-born child | `s 2 newly-born child` | yes |
| night | `s 2 night` | yes |
| nuclear facility | `s 2 nuclear facility` | no |
| nuclear material | `s 2 nuclear material` | no |
| offence-related property | `s 2 offence-related property` | yes |
| offender | `s 2 offender` | no |
| offensive weapon | `s 2 offensive weapon` | yes |
| organization | `s 2 organization` | no |
| peace officer | `s 2 peace officer` | yes |
| prison | `s 2 prison` | yes |
| prohibited ammunition | `s 2.1 the term has the meaning it has in subsection 84(1)` | yes |
| prohibited device | `s 2.1 the term has the meaning it has in subsection 84(1)` | yes |
| prohibited firearm | `s 2.1 the term has the meaning it has in subsection 84(1)` | yes |
| prohibited weapon | `s 2.1 the term has the meaning it has in subsection 84(1)` | yes |
| property | `s 2 property` | yes |
| prosecutor | `s 2 prosecutor` | no |
| provincial court judge | `s 2 provincial court judge` | no |
| public department | `s 2 public department` | no |
| public officer | `s 2 public officer` | yes |
| public stores | `s 2 public stores` | yes |
| radioactive material | `s 2 radioactive material` | no |
| railway equipment | `s 2 railway equipment` | no |
| recognizance | `s 2 recognizance` | no |
| release order | `s 2 release order` | yes |
| replica firearm | `s 2.1 the term has the meaning it has in subsection 84(1)` | yes |
| representative | `s 2 representative` | no |
| restricted firearm | `s 2.1 the term has the meaning it has in subsection 84(1)` | yes |
| restricted weapon | `s 2.1 the term has the meaning it has in subsection 84(1)` | yes |
| senior officer | `s 2 senior officer` | yes |
| serious offence | `s 2 serious offence` | yes |
| steal | `s 2 steal` | yes |
| summons | `s 2 summons` | yes |
| superior court of criminal jurisdiction | `s 2 superior court of criminal jurisdiction` | no |
| territorial division | `s 2 territorial division` | yes |
| terrorism offence | `s 2 terrorism offence` | yes |
| terrorist activity | `s 2 terrorist activity` | yes |
| terrorist group | `s 2 terrorist group` | yes |
| testamentary instrument | `s 2 testamentary instrument` | yes |
| trustee | `s 2 trustee` | yes |
| undertaking | `s 2 undertaking` | yes |
| unfit to stand trial | `s 2 unfit to stand trial` | no |
| United Nations operation | `s 2 United Nations operation` | no |
| United Nations personnel | `s 2 United Nations personnel` | no |
| valuable mineral | `s 2 valuable mineral` | no |
| valuable security | `s 2 valuable security` | yes |
| victim | `s 2 victim` | yes |
| videoconference | `s 2 videoconference` | no |
| weapon | `s 2 weapon` | yes |
| wreck | `s 2 wreck` | yes |
| writing | `s 2 writing` | yes |

Also in the keel: `s 2.2(1)` and `s 2.2(2)` and their composition `s 2.2 the individual may act on the victim’s behalf, subject to subsection (2)` (who may act for a dead or incapable victim, for ss 606, 672.5, 715.37, 722, 737.1, 745.63); `s 2.3(1)`, `s 2.3(2)` (two functions) and `s 2.3(3)` (the Attorney General of Canada's concurrent jurisdiction); `s 3` (descriptive cross-references: a rule of reading); `s 3.01(1)` and `s 3.01(2)` (what counts as an offence in which violence is used, threatened or attempted, in the provisions section 3.01(2) lists); `s 1` (short title: machinery).

## 5. Definition sections that sit inside the parts' ranges (left to the part that owns them)

Section 2 and section 2.1 are the only Act-wide definitions ("In this Act"): every other definition section is "In this Part", "In this section" or "In this section and in sections ...", which the keel checked by grep of every lead-in. So each of these is encoded by the part whose range holds its first line, and answered to other parts only through the seams in section 7.

| part | line | section | heading |
| --- | --- | --- | --- |
| ccc1 | 646 | s 25.1 | Definitions |
| ccc2 | 1220 | s 82.2 | Definition of device |
| ccc3 | 1253 | s 83.01 | Interpretation / Definitions |
| ccc3 | 1305 | s 83.031 | Definition of Public Safety Minister |
| ccc4 | 1908 | s 84 | Interpretation / Definitions |
| ccc5 | 2714 | s 118 | Interpretation / Definitions |
| ccc6 | 2994 | s 150 | Interpretation / Definitions |
| ccc6 | 3228 | s 163.1 | Definition of child sexual abuse and exploitation material |
| ccc7 | 3523 | s 183 | Definitions / Definitions |
| ccc8 | 4122 | s 197 | Interpretation / Definitions |
| ccc8 | 4398 | s 214 | Interpretation / Definitions |
| ccc8 | 4644 | s 241.1 | Medical Assistance in Dying / Definitions |
| ccc9 | 5304 | s 278.1 | Definitions / Definitions |
| ccc10 | 5913 | s 297 | Defamatory Libel / Definition of newspaper |
| ccc10 | 5915 | s 298 | Definition |
| ccc10 | 6156 | s 320.101 | Conversion Therapy / Definition of conversion therapy |
| ccc11 | 6181 | s 320.11 | Interpretation / Definitions |
| ccc12 | 6515 | s 321 | Interpretation / Definitions |
| ccc12 | 6831 | s 347.1 | Definitions |
| ccc12 | 6951 | s 355.1 | Definition of traffic |
| ccc13 | 7149 | s 379 | Interpretation / Definition of goods |
| ccc13 | 7379 | s 402.1 | Identity Theft and Identity Fraud / Definition of identity information |
| ccc13 | 7620 | s 428 | Interpretation / Definition of property |
| ccc13 | 7697 | s 431.2 | Definitions |
| ccc13 | 7828 | s 445.2 | Definition of cetacean |
| ccc14 | 7879 | s 448 | Interpretation / Definitions |
| ccc14 | 7990 | s 462.3 | Interpretation / Definitions |
| ccc14 | 8260 | s 462.371 | Definition of order |
| ccc14 | 8355 | s 462.48 | Definition of designated substance offence |
| ccc14 | 8477 | s 467.1 | Definitions |
| ccc15 | 8594 | s 477 | Definition of ship |
| ccc16 | 9059 | s 487.011 | Definitions |
| ccc16 | 9292 | s 487.04 | Forensic DNA Analysis / Definitions |
| ccc17 | 9864 | s 488.01 | Definitions |
| ccc17 | 9915 | s 488.1 | Definitions |
| ccc17 | 10060 | s 490.011 | Interpretation / Definitions |
| ccc19 | 10961 | s 492.21 | Definitions / Definitions |
| ccc20 | 11036 | s 493 | Interpretation / Definitions |
| ccc21 | 12215 | s 552 | Interpretation / Definitions |
| ccc23 | 13310 | s 672.1 | Interpretation / Definitions |
| ccc23 | 13414 | s 672.21 | Protected Statements / Definition of protected statement |
| ccc23 | 13494 | s 672.37 | Definition of application for federal employment |
| ccc23 | 13691 | s 672.51 | Definition of disposition information |
| ccc23 | 13821 | s 672.68 | Definition of Minister |
| ccc24 | 14073 | s 673 | Interpretation / Definitions |
| ccc24 | 14401 | s 696.3 | Definition of court of appeal |
| ccc24 | 14429 | s 696.7 | Definitions / Definitions |
| ccc24 | 14830 | s 715.25 | Participants / Definition of participant |
| ccc24 | 14858 | s 715.27 | Prospective Jurors / Definition of prospective juror |
| ccc25 | 14874 | s 715.3 | PART XXII.1 Remediation Agreements / Definitions |
| ccc25 | 15039 | s 715.44 | Definitions / Definitions |
| ccc26 | 15175 | s 716 | Interpretation / Definitions |
| ccc26 | 15518 | s 732.1 | Definitions |
| ccc26 | 15735 | s 734.8 | Definition of penalty |
| ccc27 | 15859 | s 742 | Conditional Sentence of Imprisonment / Definitions |
| ccc28 | 16300 | s 752 | Interpretation / Definitions |
| ccc29 | 16688 | s 785 | Interpretation / Definitions |
| ccc29 | 17120 | s 812 | Appeal / Definition of appeal court |
| ccc29 | 17251 | s 829 | Summary Appeal on Transcript or Agreed Statement of Facts / Definition of appeal court |
| ccc29 | 17317 | s 841 | Electronic Documents / Definitions |
| ccc32 | 19070 | s 22 | Interpretation of 2001, c. 32, ss. 82(1), (2) and (4) |
| ccc32 | 19077 | s 23 | Interpretation of 2001, c. 32, ss. 82(1) and (3) |
| ccc32 | 19419 | s 96 | Definitions |
| ccc32 | 19556 | s 696.1 | Definitions / Definitions |
| ccc32 | 19653 | s 7 | Definitions |

Every range begins at a heading line or a marginal-note line (the keel checked the first line of each); no range begins in the middle of a subsection. A Part, however, is split across ranges in many places (for example Part III across ccc4 and ccc5, Part VIII across ccc8, ccc9 and ccc10, Part XV across ccc16 to ccc18, Part XXIII across ccc26 and ccc27): the seam rule R5 applies.

## 6. Part by part

### ccc1

- **Ranges (copied unchanged from `inputs/PARTS.md`):** 273-849 (12,358 words)
- **What the range holds:** sections 3.1 to 45 (53 section headings); Part I.
- **Definition sections left to this part:** s 25.1 (line 646).
- **Read first:** Part I (general). s 7 lists offences by section (R1). ss 21 to 24 make a person a party to, or an attempter of, an offence whose punishment is in another part (R2). ss 25 to 25.4 use s 2 `peace officer` and `public officer`, and s 25.1(1) defines `public officer` again for its own sections. ss 22.1 and 22.2 turn on s 2 `organization`, `representative` and `senior officer`.
- **Names in the core it should expect to use:** Party, Process document, Outcome of interim release, Decision on the charge, Stage of the proceedings, Provision of the Code, Province or territory, Mode of proceeding; Party, Provision of the Code, Punishment, Imprisonment, Length of time (ss 21 to 24 and the s 7 lists); Class of offence.
- **Section 2 terms it will meet** (occurrences in its range, ordinary uses included; `*` = the keel's function can answer NOTHING): `public officer` (42)*, `peace officer` (32)*, `property` (20)*, `every one` (18)*, `bodily harm` (11), `organization` (9), `valuable security` (9)*, `Attorney General` (7)*, `internationally protected person` (4), `mental disorder` (4), `associated personnel` (3), `government or public facility` (3). Each is an input `s 2 <term>: ...` of type `MAYBE BOOLEAN` where the part's rule turns on it.
- **Seams: this part asks (asking section -> answering section: the input, its type):**
  - [H] ss 21 to 24 -> ccc2 to ccc13 the offence sections (ccc2 to ccc13): input `the punishment of the offence a party aided, abetted or attempted`: Punishment
- **Seams: other parts ask this part (what its sections must answer, as functions that agree with the input name):**
  - [T] s 2 "justice system participant" (b)(viii.1) (keel) asks for s 25.1(1) "public officer": `s 25.1(1) the person is a public officer, or acts at the direction of one`: BOOLEAN
  - [T] s 83.01(1) "terrorist activity" (ccc3) asks for s 7(3.74), (3.75): `s 7 the act or omission is deemed to have been committed in Canada`: MAYBE BOOLEAN

### ccc2

- **Ranges (copied unchanged from `inputs/PARTS.md`):** 850-1248 (6,711 words)
- **What the range holds:** sections 46 to 83 (50 section headings); PART II Offences Against Public Order.
- **Definition sections left to this part:** s 82.2 (line 1220).
- **Read first:** Part II (public order): treason, sabotage, sedition, riots, piracy, hijacking, explosives and nuclear material, prize fights. s 2 `explosive substance`, `nuclear material`, `radioactive material`, `nuclear facility`, `Canadian Forces` and `military` are the terms of art here. Sections 57 and 58 are named in s 2.3(1)(a) (concurrent jurisdiction): that is the keel's rule and asks nothing of this part.
- **Names in the core it should expect to use:** Punishment, Imprisonment, Fine, Length of time, the constants `six months`, `ninety days`, `two years less a day`, `two years`, `five years`, `ten years`, `fourteen years`, Mode of proceeding, Class of offence, Provision of the Code, Party (`the accused`, `the offender`, `the victim`, `a peace officer`, ...).
- **Section 2 terms it will meet** (occurrences in its range, ordinary uses included; `*` = the keel's function can answer NOTHING): `property` (14)*, `explosive substance` (13)*, `bodily harm` (8), `Canadian Forces` (7), `nuclear material` (6), `radioactive material` (6), `peace officer` (4)*, `Attorney General` (3)*, `dwelling-house` (3), `nuclear facility` (3), `territorial division` (3)*. Each is an input `s 2 <term>: ...` of type `MAYBE BOOLEAN` where the part's rule turns on it.
- **Seams: this part asks (asking section -> answering section: the input, its type):**
  - [T] offence sections that say "punishable on summary conviction" and state no penalty -> ccc29 s 787(1) (ccc29): input `s 787(1) the general penalty for an offence punishable on summary conviction`: Punishment
- **Seams: other parts ask this part (what its sections must answer, as functions that agree with the input name):**
  - [H] ss 718.2, 718.3, 743.1 (ccc26) asks for the offence sections: `the punishment the offence charged is liable to (from the offence section itself)`: Punishment
  - [H] ss 463 to 465 (ccc14) asks for the offence sections: `the punishment of the offence attempted, or conspired to be committed`: Punishment
  - [H] ss 21 to 24 (ccc1) asks for the offence sections: `the punishment of the offence a party aided, abetted or attempted`: Punishment
  - [H] ss 515, 522 (ccc20) asks for the offence sections: `whether the offence charged is an indictable offence, and the punishment it is liable to`: Class of offence
  - [H] ss 553 to 555 (ccc21) asks for the offence sections: `the class of the offence charged (the list in s 553 is tested by section number)`: Class of offence

### ccc3

- **Ranges (copied unchanged from `inputs/PARTS.md`):** 1249-1903 (13,430 words)
- **What the range holds:** sections 83.01 to 83.33 (52 section headings); PART II.1 Terrorism.
- **Definition sections left to this part:** s 83.01 (line 1253), s 83.031 (line 1305).
- **Read first:** Part II.1 (terrorism). s 83.01(1) defines `terrorist activity` and `terrorist group`, which s 2 points to (the keel asks them of this part). The authorization, listing and freezing regime (ss 83.03 to 83.1) addresses officials and entities: encode it for what it means for the individual. Section 83.3 is a recognizance with conditions (Form 23).
- **Names in the core it should expect to use:** Punishment, Imprisonment, Fine, Length of time, the constants `six months`, `ninety days`, `two years less a day`, `two years`, `five years`, `ten years`, `fourteen years`, Mode of proceeding, Class of offence, Provision of the Code, Party (`the accused`, `the offender`, `the victim`, `a peace officer`, ...).
- **Section 2 terms it will meet** (occurrences in its range, ordinary uses included; `*` = the keel's function can answer NOTHING): `property` (81)*, `terrorist activity` (57)*, `terrorist group` (46)*, `day` (24)*, `Attorney General` (21)*, `peace officer` (20)*, `recognizance` (20), `terrorism offence` (16)*, `provincial court judge` (13), `organization` (9), `bodily harm` (5), `dwelling-house` (4). Each is an input `s 2 <term>: ...` of type `MAYBE BOOLEAN` where the part's rule turns on it.
- **Seams: this part asks (asking section -> answering section: the input, its type):**
  - [T] ss 83.13, 83.14 -> ccc14 ss 462.32 to 462.4 (ccc14): input `s 462.34 the review of the special warrant or restraint order has been applied for`: MAYBE BOOLEAN
  - [T] ss 83.222, 83.223 -> ccc10 s 320(8) (ccc10): input `s 320(8) the court and the judge the warrant of seizure is made to`: Party
  - [T] s 83.01(1) "terrorist activity" -> ccc1 s 7(3.74), (3.75) (ccc1): input `s 7 the act or omission is deemed to have been committed in Canada`: MAYBE BOOLEAN
  - [T] offence sections that say "punishable on summary conviction" and state no penalty -> ccc29 s 787(1) (ccc29): input `s 787(1) the general penalty for an offence punishable on summary conviction`: Punishment
- **Seams: other parts ask this part (what its sections must answer, as functions that agree with the input name):**
  - [T] s 2 "terrorist activity"; s 2.3(1)(a) (keel) asks for s 83.01(1): `s 83.01(1) the act or omission is a terrorist activity`: MAYBE BOOLEAN
  - [T] s 2 "terrorist group"; s 2 "terrorism offence" (keel) asks for s 83.01(1): `s 83.01(1) the group is a terrorist group`: MAYBE BOOLEAN
  - [H] ss 718.2, 718.3, 743.1 (ccc26) asks for the offence sections: `the punishment the offence charged is liable to (from the offence section itself)`: Punishment
  - [H] ss 463 to 465 (ccc14) asks for the offence sections: `the punishment of the offence attempted, or conspired to be committed`: Punishment
  - [H] ss 21 to 24 (ccc1) asks for the offence sections: `the punishment of the offence a party aided, abetted or attempted`: Punishment
  - [H] ss 515, 522 (ccc20) asks for the offence sections: `whether the offence charged is an indictable offence, and the punishment it is liable to`: Class of offence
  - [H] ss 553 to 555 (ccc21) asks for the offence sections: `the class of the offence charged (the list in s 553 is tested by section number)`: Class of offence

### ccc4

- **Ranges (copied unchanged from `inputs/PARTS.md`):** 1904-2381 (9,479 words)
- **What the range holds:** sections 84 to 110.3 (33 section headings); PART III Firearms and Other Weapons.
- **Definition sections left to this part:** s 84 (line 1908).
- **Read first:** Part III (firearms): s 84(1) defines the terms s 2.1 points to (the keel asks them of this part). Many offences are "knowing" or "unauthorized" possession: the authorization, licence and registration certificate are borrowed facts. Prohibition orders begin here (ss 109 to 110.3) and continue in ccc5 (R5).
- **Names in the core it should expect to use:** Punishment, Imprisonment, Fine, Length of time, the constants `six months`, `ninety days`, `two years less a day`, `two years`, `five years`, `ten years`, `fourteen years`, Mode of proceeding, Class of offence, Provision of the Code, Party (`the accused`, `the offender`, `the victim`, `a peace officer`, ...).
- **Section 2 terms it will meet** (occurrences in its range, ordinary uses included; `*` = the keel's function can answer NOTHING): `firearm` (247), `weapon` (93)*, `ammunition` (69)*, `restricted firearm` (59)*, `prohibited device` (46)*, `prohibited ammunition` (39)*, `prohibited firearm` (38)*, `restricted weapon` (36)*, `prohibited weapon` (35)*, `firearm part` (20)*, `provincial court judge` (17), `motor vehicle` (14)*. Each is an input `s 2 <term>: ...` of type `MAYBE BOOLEAN` where the part's rule turns on it.
- **Seams: this part asks (asking section -> answering section: the input, its type):**
  - [T] ss 109(1), 110(1), (2.1) -> keel s 3.01(1), (2) (keel): input `s 3.01 the offence counts as one in which violence is used, threatened or attempted`: MAYBE BOOLEAN
  - [T] ss 94, 110.1 -> ccc5 ss 110.4, 117.07, 117.1 (ccc5): input `s 117.07 the person is exempt from the prohibition (a public officer, and the other persons s 117.07 names)`: MAYBE BOOLEAN
  - [T] ss 98, 102.1 -> ccc12 ss 321, 342.1(2) (ccc12): input `s 321 the person breaks; s 342.1(2) computer data and computer system`: MAYBE BOOLEAN
  - [T] offence sections that say "punishable on summary conviction" and state no penalty -> ccc29 s 787(1) (ccc29): input `s 787(1) the general penalty for an offence punishable on summary conviction`: Punishment
- **Seams: other parts ask this part (what its sections must answer, as functions that agree with the input name):**
  - [T] s 2.1 (keel) asks for s 84(1): `s 84(1) the thing is within the meaning the term has in subsection 84(1)`: MAYBE BOOLEAN
  - [T] ss 110.4 to 113 (ccc5) asks for ss 109, 110, 110.1: `s 110.1 an emergency prohibition order has been made`: MAYBE BOOLEAN
  - [H] ss 718.2, 718.3, 743.1 (ccc26) asks for the offence sections: `the punishment the offence charged is liable to (from the offence section itself)`: Punishment
  - [H] ss 463 to 465 (ccc14) asks for the offence sections: `the punishment of the offence attempted, or conspired to be committed`: Punishment
  - [H] ss 21 to 24 (ccc1) asks for the offence sections: `the punishment of the offence a party aided, abetted or attempted`: Punishment
  - [H] ss 515, 522 (ccc20) asks for the offence sections: `whether the offence charged is an indictable offence, and the punishment it is liable to`: Class of offence
  - [H] ss 553 to 555 (ccc21) asks for the offence sections: `the class of the offence charged (the list in s 553 is tested by section number)`: Class of offence

### ccc5

- **Ranges (copied unchanged from `inputs/PARTS.md`):** 2382-2989 (15,284 words)
- **What the range holds:** sections 110.4 to 149 (64 section headings); PART IV Offences Against the Administration of Law and Justice.
- **Definition sections left to this part:** s 118 (line 2714).
- **Read first:** Starts inside Part III (prohibition orders and search of ss 110.4 to 117.15, exemptions in ss 117.07 to 117.1) and holds all of Part IV (offences against the administration of law and justice: bribery, perjury, obstruction, escape, contempt). s 118 defines terms for Part IV only. s 145 (failure to comply with a release order or undertaking) needs ccc20.
- **Names in the core it should expect to use:** Punishment, Imprisonment, Fine, Length of time, the constants `six months`, `ninety days`, `two years less a day`, `two years`, `five years`, `ten years`, `fourteen years`, Mode of proceeding, Class of offence, Provision of the Code, Party (`the accused`, `the offender`, `the victim`, `a peace officer`, ...).
- **Section 2 terms it will meet** (occurrences in its range, ordinary uses included; `*` = the keel's function can answer NOTHING): `firearm` (111), `weapon` (60)*, `ammunition` (56)*, `provincial court judge` (53), `peace officer` (50)*, `justice` (39), `prohibited ammunition` (35)*, `prohibited device` (35)*, `Attorney General` (29)*, `prohibited weapon` (27)*, `public officer` (23)*, `restricted weapon` (23)*. Each is an input `s 2 <term>: ...` of type `MAYBE BOOLEAN` where the part's rule turns on it.
- **Seams: this part asks (asking section -> answering section: the input, its type):**
  - [T] ss 110.4 to 113 -> ccc4 ss 109, 110, 110.1 (ccc4): input `s 110.1 an emergency prohibition order has been made`: MAYBE BOOLEAN
  - [T] s 145 -> ccc20 ss 508, 515 (ccc20): input `s 515 the accused is bound by a release order`: BOOLEAN
  - [T] offence sections that say "punishable on summary conviction" and state no penalty -> ccc29 s 787(1) (ccc29): input `s 787(1) the general penalty for an offence punishable on summary conviction`: Punishment
- **Seams: other parts ask this part (what its sections must answer, as functions that agree with the input name):**
  - [T] ss 94, 110.1 (ccc4) asks for ss 110.4, 117.07, 117.1: `s 117.07 the person is exempt from the prohibition (a public officer, and the other persons s 117.07 names)`: MAYBE BOOLEAN
  - [H] ss 718.2, 718.3, 743.1 (ccc26) asks for the offence sections: `the punishment the offence charged is liable to (from the offence section itself)`: Punishment
  - [H] ss 463 to 465 (ccc14) asks for the offence sections: `the punishment of the offence attempted, or conspired to be committed`: Punishment
  - [H] ss 21 to 24 (ccc1) asks for the offence sections: `the punishment of the offence a party aided, abetted or attempted`: Punishment
  - [H] ss 515, 522 (ccc20) asks for the offence sections: `whether the offence charged is an indictable offence, and the punishment it is liable to`: Class of offence
  - [H] ss 553 to 555 (ccc21) asks for the offence sections: `the class of the offence charged (the list in s 553 is tested by section number)`: Class of offence

### ccc6

- **Ranges (copied unchanged from `inputs/PARTS.md`):** 2990-3518 (11,074 words)
- **What the range holds:** sections 150 to 182 (44 section headings); PART V Sexual Offences, Public Morals and Disorderly Conduct.
- **Definition sections left to this part:** s 150 (line 2994), s 163.1 (line 3228).
- **Read first:** Part V (sexual offences, public morals, disorderly conduct). s 150.1 makes consent no defence by age bands: take ages as numbers and the exceptions as facts. s 163.1 defines child sexual abuse and exploitation material for this Part. The warrant-of-seizure and forfeiture sections (164 to 164.3) cite offences in ccc10.
- **Names in the core it should expect to use:** Punishment, Imprisonment, Fine, Length of time, the constants `six months`, `ninety days`, `two years less a day`, `two years`, `five years`, `ten years`, `fourteen years`, Mode of proceeding, Class of offence, Provision of the Code, Party (`the accused`, `the offender`, `the victim`, `a peace officer`, ...).
- **Section 2 terms it will meet** (occurrences in its range, ordinary uses included; `*` = the keel's function can answer NOTHING): `complainant` (49)*, `day` (28)*, `offender` (16), `Attorney General` (15)*, `counsel` (11), `dwelling-house` (7), `peace officer` (7)*, `court of appeal` (4). Each is an input `s 2 <term>: ...` of type `MAYBE BOOLEAN` where the part's rule turns on it.
- **Seams: this part asks (asking section -> answering section: the input, its type):**
  - [T] offence sections that say "punishable on summary conviction" and state no penalty -> ccc29 s 787(1) (ccc29): input `s 787(1) the general penalty for an offence punishable on summary conviction`: Punishment
- **Seams: other parts ask this part (what its sections must answer, as functions that agree with the input name):**
  - [H] ss 718.2, 718.3, 743.1 (ccc26) asks for the offence sections: `the punishment the offence charged is liable to (from the offence section itself)`: Punishment
  - [H] ss 463 to 465 (ccc14) asks for the offence sections: `the punishment of the offence attempted, or conspired to be committed`: Punishment
  - [H] ss 21 to 24 (ccc1) asks for the offence sections: `the punishment of the offence a party aided, abetted or attempted`: Punishment
  - [H] ss 515, 522 (ccc20) asks for the offence sections: `whether the offence charged is an indictable offence, and the punishment it is liable to`: Class of offence
  - [H] ss 553 to 555 (ccc21) asks for the offence sections: `the class of the offence charged (the list in s 553 is tested by section number)`: Class of offence

### ccc7

- **Ranges (copied unchanged from `inputs/PARTS.md`):** 3519-4117 (11,324 words)
- **What the range holds:** sections 183 to 196.1 (26 section headings); PART VI Invasion of Privacy.
- **Definition sections left to this part:** s 183 (line 3523).
- **Read first:** Part VI (invasion of privacy: interception). s 183 defines `offence` for this Part by a long list of sections across the Code (R1): encode it as a table over `Provision of the Code`. s 186.1 turns on s 2 `criminal organization offence` and `terrorism offence`.
- **Names in the core it should expect to use:** Punishment, Imprisonment, Fine, Length of time, the constants `six months`, `ninety days`, `two years less a day`, `two years`, `five years`, `ten years`, `fourteen years`, Mode of proceeding, Class of offence, Provision of the Code, Party (`the accused`, `the offender`, `the victim`, `a peace officer`, ...).
- **Section 2 terms it will meet** (occurrences in its range, ordinary uses included; `*` = the keel's function can answer NOTHING): `writing` (28)*, `Attorney General` (27)*, `criminal organization` (17)*, `day` (17)*, `organization` (17), `peace officer` (17)*, `bodily harm` (11), `property` (10)*, `terrorism offence` (10)*, `justice` (9), `terrorist group` (8)*, `court of criminal jurisdiction` (7). Each is an input `s 2 <term>: ...` of type `MAYBE BOOLEAN` where the part's rule turns on it.
- **Seams: this part asks (asking section -> answering section: the input, its type):**
  - [T] offence sections that say "punishable on summary conviction" and state no penalty -> ccc29 s 787(1) (ccc29): input `s 787(1) the general penalty for an offence punishable on summary conviction`: Punishment
- **Seams: other parts ask this part (what its sections must answer, as functions that agree with the input name):**
  - [H] ss 718.2, 718.3, 743.1 (ccc26) asks for the offence sections: `the punishment the offence charged is liable to (from the offence section itself)`: Punishment
  - [H] ss 463 to 465 (ccc14) asks for the offence sections: `the punishment of the offence attempted, or conspired to be committed`: Punishment
  - [H] ss 21 to 24 (ccc1) asks for the offence sections: `the punishment of the offence a party aided, abetted or attempted`: Punishment
  - [H] ss 515, 522 (ccc20) asks for the offence sections: `whether the offence charged is an indictable offence, and the punishment it is liable to`: Class of offence
  - [H] ss 553 to 555 (ccc21) asks for the offence sections: `the class of the offence charged (the list in s 553 is tested by section number)`: Class of offence

### ccc8

- **Ranges (copied unchanged from `inputs/PARTS.md`):** 4118-5031 (18,240 words)
- **What the range holds:** sections 197 to 269.1 (98 section headings); PART VII Disorderly Houses, Gaming and Betting; PART VIII Offences Against the Person and Reputation.
- **Definition sections left to this part:** s 197 (line 4122), s 214 (line 4398), s 241.1 (line 4644).
- **Read first:** Part VII (disorderly houses, gaming and betting, ss 197 to 213) and the first part of Part VIII (offences against the person: negligence, homicide, murder classification in s 231, assisted dying ss 241.1 to 241.4, assaults to s 269.1). s 231 turns on s 2 `peace officer`, `justice system participant`, `criminal organization offence`, `terrorism offence`. The kind of homicide offence is a result that ccc27 asks of this part (core: `Kind of homicide offence`).
- **Names in the core it should expect to use:** Punishment, Imprisonment, Fine, Length of time, the constants `six months`, `ninety days`, `two years less a day`, `two years`, `five years`, `ten years`, `fourteen years`, Mode of proceeding, Class of offence, Provision of the Code, Party (`the accused`, `the offender`, `the victim`, `a peace officer`, ...); the offence core names above, plus Kind of homicide offence (the result of ss 229 to 236), Mode of proceeding.
- **Section 2 terms it will meet** (occurrences in its range, ordinary uses included; `*` = the keel's function can answer NOTHING): `bodily harm` (26), `day` (19)*, `firearm` (19), `property` (17)*, `victim` (17)*, `complainant` (9)*, `organization` (9), `criminal organization` (6)*, `intimate partner` (6)*, `Attorney General` (4)*, `peace officer` (4)*, `valuable security` (4)*. Each is an input `s 2 <term>: ...` of type `MAYBE BOOLEAN` where the part's rule turns on it.
- **Seams: this part asks (asking section -> answering section: the input, its type):**
  - [T] s 263.1(1) -> keel s 3.01(1), (2) (keel): input `s 3.01 the offence counts as one in which violence is used, threatened or attempted`: MAYBE BOOLEAN
  - [T] s 241.4 -> ccc12 s 321 (ccc12): input `s 321 the thing is a document`: MAYBE BOOLEAN
  - [T] offence sections that say "punishable on summary conviction" and state no penalty -> ccc29 s 787(1) (ccc29): input `s 787(1) the general penalty for an offence punishable on summary conviction`: Punishment
- **Seams: other parts ask this part (what its sections must answer, as functions that agree with the input name):**
  - [T] s 286.1(5) (ccc10) asks for s 197(1): `s 197(1) the place is a place; the place is a public place`: MAYBE BOOLEAN
  - [T] s 745 and 745.01 to 745.6 (ccc27) asks for ss 231, 235: `s 231 the kind of homicide offence`: Kind of homicide offence
  - [H] ss 718.2, 718.3, 743.1 (ccc26) asks for the offence sections: `the punishment the offence charged is liable to (from the offence section itself)`: Punishment
  - [H] ss 463 to 465 (ccc14) asks for the offence sections: `the punishment of the offence attempted, or conspired to be committed`: Punishment
  - [H] ss 21 to 24 (ccc1) asks for the offence sections: `the punishment of the offence a party aided, abetted or attempted`: Punishment
  - [H] ss 515, 522 (ccc20) asks for the offence sections: `whether the offence charged is an indictable offence, and the punishment it is liable to`: Class of offence
  - [H] ss 553 to 555 (ccc21) asks for the offence sections: `the class of the offence charged (the list in s 553 is tested by section number)`: Class of offence

### ccc9

- **Ranges (copied unchanged from `inputs/PARTS.md`):** 5032-5568 (11,594 words)
- **What the range holds:** sections 270 to 278.31 (55 section headings); no Part heading starts here (the range is inside a Part).
- **Definition sections left to this part:** s 278.1 (line 5304).
- **Read first:** Continues Part VIII: assaults on peace officers (ss 270 to 270.03), sexual assault (271 to 273.3), the rules on complainants' sexual-activity evidence (276 to 276.13) and the production of records (278.1 onward). The production regime continues in ccc10 (R5).
- **Names in the core it should expect to use:** Punishment, Imprisonment, Fine, Length of time, the constants `six months`, `ninety days`, `two years less a day`, `two years`, `five years`, `ten years`, `fourteen years`, Mode of proceeding, Class of offence, Provision of the Code, Party (`the accused`, `the offender`, `the victim`, `a peace officer`, ...).
- **Section 2 terms it will meet** (occurrences in its range, ordinary uses included; `*` = the keel's function can answer NOTHING): `complainant` (104)*, `justice` (66), `provincial court judge` (38), `prosecutor` (25), `day` (20)*, `counsel` (11), `writing` (11)*, `firearm` (10), `peace officer` (8)*, `weapon` (8)*, `clerk of the court` (6)*, `bodily harm` (5). Each is an input `s 2 <term>: ...` of type `MAYBE BOOLEAN` where the part's rule turns on it.
- **Seams: this part asks (asking section -> answering section: the input, its type):**
  - [T] ss 278.2 to 278.28 (and ss 272, 273) -> ccc10 ss 278.32 to 278.38 and ss 279, 279.1 (ccc10): input `identity by section number (a list of offences): no input is needed`: -
  - [T] offence sections that say "punishable on summary conviction" and state no penalty -> ccc29 s 787(1) (ccc29): input `s 787(1) the general penalty for an offence punishable on summary conviction`: Punishment
- **Seams: other parts ask this part (what its sections must answer, as functions that agree with the input name):**
  - [T] ss 278.32 to 278.38 (ccc10) asks for ss 278.29, 278.3, 278.31: `s 278.3 an application for a hearing on records in the accused’s possession has been made`: MAYBE BOOLEAN
  - [H] ss 718.2, 718.3, 743.1 (ccc26) asks for the offence sections: `the punishment the offence charged is liable to (from the offence section itself)`: Punishment
  - [H] ss 463 to 465 (ccc14) asks for the offence sections: `the punishment of the offence attempted, or conspired to be committed`: Punishment
  - [H] ss 21 to 24 (ccc1) asks for the offence sections: `the punishment of the offence a party aided, abetted or attempted`: Punishment
  - [H] ss 515, 522 (ccc20) asks for the offence sections: `whether the offence charged is an indictable offence, and the punishment it is liable to`: Class of offence
  - [H] ss 553 to 555 (ccc21) asks for the offence sections: `the class of the offence charged (the list in s 553 is tested by section number)`: Class of offence

### ccc10

- **Ranges (copied unchanged from `inputs/PARTS.md`):** 5569-6176 (11,603 words)
- **What the range holds:** sections 278.32 to 320.104 (82 section headings); no Part heading starts here (the range is inside a Part).
- **Definition sections left to this part:** s 297 (line 5913), s 298 (line 5915), s 320.101 (line 6156).
- **Read first:** Starts inside Part VIII at s 278.32: the end of the production regime, kidnapping, trafficking in persons, abduction, procuring and advertising sexual services, marriage offences, defamatory libel, hate propaganda (ss 318 to 320.1) and conversion therapy (ss 320.101 to 320.104). s 320(8) defines `judge` and `court` for the warrant sections; ccc3 asks it.
- **Names in the core it should expect to use:** Punishment, Imprisonment, Fine, Length of time, the constants `six months`, `ninety days`, `two years less a day`, `two years`, `five years`, `ten years`, `fourteen years`, Mode of proceeding, Class of offence, Provision of the Code, Party (`the accused`, `the offender`, `the victim`, `a peace officer`, ...).
- **Section 2 terms it will meet** (occurrences in its range, ordinary uses included; `*` = the keel's function can answer NOTHING): `complainant` (22)*, `justice` (17), `day` (15)*, `provincial court judge` (11), `firearm` (10), `Attorney General` (6)*. Each is an input `s 2 <term>: ...` of type `MAYBE BOOLEAN` where the part's rule turns on it.
- **Seams: this part asks (asking section -> answering section: the input, its type):**
  - [T] ss 278.32 to 278.38 -> ccc9 ss 278.29, 278.3, 278.31 (ccc9): input `s 278.3 an application for a hearing on records in the accused’s possession has been made`: MAYBE BOOLEAN
  - [T] s 286.1(5) -> ccc8 s 197(1) (ccc8): input `s 197(1) the place is a place; the place is a public place`: MAYBE BOOLEAN
  - [T] offence sections that say "punishable on summary conviction" and state no penalty -> ccc29 s 787(1) (ccc29): input `s 787(1) the general penalty for an offence punishable on summary conviction`: Punishment
- **Seams: other parts ask this part (what its sections must answer, as functions that agree with the input name):**
  - [T] ss 278.2 to 278.28 (and ss 272, 273) (ccc9) asks for ss 278.32 to 278.38 and ss 279, 279.1: `identity by section number (a list of offences): no input is needed`: -
  - [T] ss 83.222, 83.223 (ccc3) asks for s 320(8): `s 320(8) the court and the judge the warrant of seizure is made to`: Party
  - [T] s 478(5) (ccc15) asks for s 297: `s 297 the publication is a newspaper`: MAYBE BOOLEAN
  - [H] ss 718.2, 718.3, 743.1 (ccc26) asks for the offence sections: `the punishment the offence charged is liable to (from the offence section itself)`: Punishment
  - [H] ss 463 to 465 (ccc14) asks for the offence sections: `the punishment of the offence attempted, or conspired to be committed`: Punishment
  - [H] ss 21 to 24 (ccc1) asks for the offence sections: `the punishment of the offence a party aided, abetted or attempted`: Punishment
  - [H] ss 515, 522 (ccc20) asks for the offence sections: `whether the offence charged is an indictable offence, and the punishment it is liable to`: Class of offence
  - [H] ss 553 to 555 (ccc21) asks for the offence sections: `the class of the offence charged (the list in s 553 is tested by section number)`: Class of offence

### ccc11

- **Ranges (copied unchanged from `inputs/PARTS.md`):** 6177-6510 (7,400 words)
- **What the range holds:** sections 320.11 to 320.4 (30 section headings); PART VIII.1 Offences Relating to Conveyances.
- **Definition sections left to this part:** s 320.11 (line 6181).
- **Read first:** Part VIII.1 (offences relating to conveyances): impaired and dangerous operation, refusal, flight, prohibitions, investigative matters, evidence. s 320.11 defines terms (`analyst`, `vessel`, ...) that ccc12 (s 335(2)), ccc26 (s 729.1(2)) and ccc29 (s 811.1(2)) ask of this part. The penalty tables are by number of occasions and by harm caused.
- **Names in the core it should expect to use:** Punishment, Imprisonment, Fine, Length of time, the constants `six months`, `ninety days`, `two years less a day`, `two years`, `five years`, `ten years`, `fourteen years`, Mode of proceeding, Class of offence, Provision of the Code, Party (`the accused`, `the offender`, `the victim`, `a peace officer`, ...).
- **Section 2 terms it will meet** (occurrences in its range, ordinary uses included; `*` = the keel's function can answer NOTHING): `offender` (35), `peace officer` (26)*, `day` (25)*, `motor vehicle` (14)*, `bodily harm` (13), `Attorney General` (11)*, `railway equipment` (3). Each is an input `s 2 <term>: ...` of type `MAYBE BOOLEAN` where the part's rule turns on it.
- **Seams: this part asks (asking section -> answering section: the input, its type):**
  - [T] offence sections that say "punishable on summary conviction" and state no penalty -> ccc29 s 787(1) (ccc29): input `s 787(1) the general penalty for an offence punishable on summary conviction`: Punishment
- **Seams: other parts ask this part (what its sections must answer, as functions that agree with the input name):**
  - [T] s 335(2) (ccc12) asks for s 320.11: `s 320.11 the thing is a vessel`: MAYBE BOOLEAN
  - [T] s 729.1(2) (ccc26) asks for s 320.11: `s 320.11 the person is an analyst`: MAYBE BOOLEAN
  - [T] s 811.1 (ccc29) asks for s 320.11: `s 320.11 the person is an analyst`: MAYBE BOOLEAN
  - [H] ss 718.2, 718.3, 743.1 (ccc26) asks for the offence sections: `the punishment the offence charged is liable to (from the offence section itself)`: Punishment
  - [H] ss 463 to 465 (ccc14) asks for the offence sections: `the punishment of the offence attempted, or conspired to be committed`: Punishment
  - [H] ss 21 to 24 (ccc1) asks for the offence sections: `the punishment of the offence a party aided, abetted or attempted`: Punishment
  - [H] ss 515, 522 (ccc20) asks for the offence sections: `whether the offence charged is an indictable offence, and the punishment it is liable to`: Class of offence
  - [H] ss 553 to 555 (ccc21) asks for the offence sections: `the class of the offence charged (the list in s 553 is tested by section number)`: Class of offence

### ccc12

- **Ranges (copied unchanged from `inputs/PARTS.md`):** 6511-7144 (12,874 words)
- **What the range holds:** sections 321 to 378 (77 section headings); PART IX Offences Against Rights of Property.
- **Definition sections left to this part:** s 321 (line 6515), s 347.1 (line 6831), s 355.1 (line 6951).
- **Read first:** Part IX (theft and offences resembling theft, robbery, extortion, criminal interest rate, break and enter, possession of property obtained by crime, false pretences, forgery). s 321 defines `break`, `document`, ...; s 342.1(2) defines `computer data` and `computer system`, which other parts ask. s 322 (theft) is what s 2 `steal` points to. s 347 (criminal interest rate) is numeric: encode its rates and limits exactly.
- **Names in the core it should expect to use:** Punishment, Imprisonment, Fine, Length of time, the constants `six months`, `ninety days`, `two years less a day`, `two years`, `five years`, `ten years`, `fourteen years`, Mode of proceeding, Class of offence, Provision of the Code, Party (`the accused`, `the offender`, `the victim`, `a peace officer`, ...).
- **Section 2 terms it will meet** (occurrences in its range, ordinary uses included; `*` = the keel's function can answer NOTHING): `property` (50)*, `motor vehicle` (25)*, `indictment` (14)*, `cattle` (12), `dwelling-house` (11), `Attorney General` (10)*, `organization` (10), `steal` (10)*, `firearm` (8), `peace officer` (7)*, `valuable security` (5)*, `criminal organization` (4)*. Each is an input `s 2 <term>: ...` of type `MAYBE BOOLEAN` where the part's rule turns on it.
- **Seams: this part asks (asking section -> answering section: the input, its type):**
  - [T] s 335(2) -> ccc11 s 320.11 (ccc11): input `s 320.11 the thing is a vessel`: MAYBE BOOLEAN
  - [T] offence sections that say "punishable on summary conviction" and state no penalty -> ccc29 s 787(1) (ccc29): input `s 787(1) the general penalty for an offence punishable on summary conviction`: Punishment
- **Seams: other parts ask this part (what its sections must answer, as functions that agree with the input name):**
  - [T] s 2 "steal" (keel) asks for s 322: `s 322 the person commits theft`: MAYBE BOOLEAN
  - [T] ss 98, 102.1 (ccc4) asks for ss 321, 342.1(2): `s 321 the person breaks; s 342.1(2) computer data and computer system`: MAYBE BOOLEAN
  - [T] s 241.4 (ccc8) asks for s 321: `s 321 the thing is a document`: MAYBE BOOLEAN
  - [T] s 487.011 (ccc16) asks for s 342.1(2): `s 342.1(2) computer data and computer system`: MAYBE BOOLEAN
  - [T] s 488.1 (ccc17) asks for s 321: `s 321 the thing is a document`: MAYBE BOOLEAN
  - [T] s 430(8) (ccc13) asks for s 342.1(2): `s 342.1(2) computer data`: MAYBE BOOLEAN
  - [H] ss 718.2, 718.3, 743.1 (ccc26) asks for the offence sections: `the punishment the offence charged is liable to (from the offence section itself)`: Punishment
  - [H] ss 463 to 465 (ccc14) asks for the offence sections: `the punishment of the offence attempted, or conspired to be committed`: Punishment
  - [H] ss 21 to 24 (ccc1) asks for the offence sections: `the punishment of the offence a party aided, abetted or attempted`: Punishment
  - [H] ss 515, 522 (ccc20) asks for the offence sections: `whether the offence charged is an indictable offence, and the punishment it is liable to`: Class of offence
  - [H] ss 553 to 555 (ccc21) asks for the offence sections: `the class of the offence charged (the list in s 553 is tested by section number)`: Class of offence

### ccc13

- **Ranges (copied unchanged from `inputs/PARTS.md`):** 7145-7874 (14,737 words)
- **What the range holds:** sections 379 to 447.1 (90 section headings); PART X Fraudulent Transactions Relating to Contracts and Trade; PART XI Wilful and Forbidden Acts in Respect of Certain Property.
- **Definition sections left to this part:** s 379 (line 7149), s 402.1 (line 7379), s 428 (line 7620), s 431.2 (line 7697), s 445.2 (line 7828).
- **Read first:** Part X (fraud, insider trading, trade secrets, identity theft and fraud, forgery of trademarks, intimidation, secret commissions, ss 379 to 427) and the start of Part XI (mischief, arson, animal cruelty, ss 428 to 447.1). s 402.1 defines `identity information`, which ccc22 asks. ss 423.1, 424, 424.1, 431, 431.1 use s 2 `justice system participant`, `internationally protected person`, `United Nations personnel`, `associated personnel`.
- **Names in the core it should expect to use:** Punishment, Imprisonment, Fine, Length of time, the constants `six months`, `ninety days`, `two years less a day`, `two years`, `five years`, `ten years`, `fourteen years`, Mode of proceeding, Class of offence, Provision of the Code, Party (`the accused`, `the offender`, `the victim`, `a peace officer`, ...).
- **Section 2 terms it will meet** (occurrences in its range, ordinary uses included; `*` = the keel's function can answer NOTHING): `property` (67)*, `wreck` (19)*, `valuable mineral` (18), `justice` (12), `military` (12)*, `offender` (11), `day` (10)*, `Canadian Forces` (8), `organization` (8), `public stores` (6)*, `valuable security` (6)*, `Attorney General` (5)*. Each is an input `s 2 <term>: ...` of type `MAYBE BOOLEAN` where the part's rule turns on it.
- **Seams: this part asks (asking section -> answering section: the input, its type):**
  - [T] s 430(8) -> ccc12 s 342.1(2) (ccc12): input `s 342.1(2) computer data`: MAYBE BOOLEAN
  - [T] offence sections that say "punishable on summary conviction" and state no penalty -> ccc29 s 787(1) (ccc29): input `s 787(1) the general penalty for an offence punishable on summary conviction`: Punishment
- **Seams: other parts ask this part (what its sections must answer, as functions that agree with the input name):**
  - [T] s 657.4 (ccc22) asks for s 402.1: `s 402.1 the information is identity information`: MAYBE BOOLEAN
  - [H] ss 718.2, 718.3, 743.1 (ccc26) asks for the offence sections: `the punishment the offence charged is liable to (from the offence section itself)`: Punishment
  - [H] ss 463 to 465 (ccc14) asks for the offence sections: `the punishment of the offence attempted, or conspired to be committed`: Punishment
  - [H] ss 21 to 24 (ccc1) asks for the offence sections: `the punishment of the offence a party aided, abetted or attempted`: Punishment
  - [H] ss 515, 522 (ccc20) asks for the offence sections: `whether the offence charged is an indictable offence, and the punishment it is liable to`: Class of offence
  - [H] ss 553 to 555 (ccc21) asks for the offence sections: `the class of the offence charged (the list in s 553 is tested by section number)`: Class of offence

### ccc14

- **Ranges (copied unchanged from `inputs/PARTS.md`):** 7875-8523 (14,068 words)
- **What the range holds:** sections 448 to 467.2 (54 section headings); PART XII Offences Relating to Currency; PART XII.1 [Repealed, 2018, c. 16, s. 211]; PART XII.2 Proceeds of Crime; PART XIII Attempts — Conspiracies — Accessories.
- **Definition sections left to this part:** s 448 (line 7879), s 462.3 (line 7990), s 462.371 (line 8260), s 462.48 (line 8355), s 467.1 (line 8477).
- **Read first:** Part XII (currency), Part XII.2 (proceeds of crime: laundering, special warrants, restraint, forfeiture; s 462.3 and s 462.48 define terms for the Part and the section), Part XIII (attempts, conspiracies, accessories, ss 463 to 467, and the criminal organization offences of ss 467.1 to 467.14). s 467.1(1) is what s 2 `criminal organization` and `serious offence` point to (the keel asks them of this part).
- **Names in the core it should expect to use:** Punishment, Imprisonment, Fine, Length of time, the constants `six months`, `ninety days`, `two years less a day`, `two years`, `five years`, `ten years`, `fourteen years`, Mode of proceeding, Class of offence, Provision of the Code, Party (`the accused`, `the offender`, `the victim`, `a peace officer`, ...); the offence core names above (punishments of attempts and conspiracies), Provision of the Code (the s 467.11 to 467.13 sections), Party (`an organization`, `a representative of an organization`).
- **Section 2 terms it will meet** (occurrences in its range, ordinary uses included; `*` = the keel's function can answer NOTHING): `property` (188)*, `Attorney General` (44)*, `organization` (29), `criminal organization` (28)*, `offender` (28), `peace officer` (20)*, `day` (16)*, `writing` (13)*, `bank-note` (10)*, `every one` (10)*, `serious offence` (7)*, `clerk of the court` (6)*. Each is an input `s 2 <term>: ...` of type `MAYBE BOOLEAN` where the part's rule turns on it.
- **Seams: this part asks (asking section -> answering section: the input, its type):**
  - [H] ss 463 to 465 -> ccc2 to ccc13 the offence sections (ccc2 to ccc13): input `the punishment of the offence attempted, or conspired to be committed`: Punishment
- **Seams: other parts ask this part (what its sections must answer, as functions that agree with the input name):**
  - [T] s 2 "criminal organization" (keel) asks for s 467.1(1): `s 467.1(1) the group is a criminal organization`: MAYBE BOOLEAN
  - [T] s 2 "serious offence" (keel) asks for s 467.1(1): `s 467.1(1) the offence is a serious offence`: MAYBE BOOLEAN
  - [T] ss 83.13, 83.14 (ccc3) asks for ss 462.32 to 462.4: `s 462.34 the review of the special warrant or restraint order has been applied for`: MAYBE BOOLEAN

### ccc15

- **Ranges (copied unchanged from `inputs/PARTS.md`):** 8524-8718 (3,933 words)
- **What the range holds:** sections 468 to 482.1 (23 section headings); PART XIV Jurisdiction.
- **Definition sections left to this part:** s 477 (line 8594).
- **Read first:** Part XIV (jurisdiction). s 469 lists the offences only a superior court of criminal jurisdiction may try (R1): ccc20 and ccc21 ask whether an offence is on the list. s 468 and s 469 use s 2 `superior court of criminal jurisdiction`. ss 482 and 482.1 (rules of court, case management) address courts.
- **Names in the core it should expect to use:** Province or territory (ss 468 to 481), Party (`a court of criminal jurisdiction`, `a superior court of criminal jurisdiction`, `a judge`, `a justice`), Provision of the Code (the s 469 list), Mode of proceeding.
- **Section 2 terms it will meet** (occurrences in its range, ordinary uses included; `*` = the keel's function can answer NOTHING): `territorial division` (29)*, `Attorney General` (18)*, `court of criminal jurisdiction` (9), `superior court of criminal jurisdiction` (5), `clerk of the court` (3)*. Each is an input `s 2 <term>: ...` of type `MAYBE BOOLEAN` where the part's rule turns on it.
- **Seams: this part asks (asking section -> answering section: the input, its type):**
  - [T] s 478(5) -> ccc10 s 297 (ccc10): input `s 297 the publication is a newspaper`: MAYBE BOOLEAN
- **Seams: other parts ask this part (what its sections must answer, as functions that agree with the input name):**
  - [T] ss 498, 515, 522, 523 (ccc20) asks for s 469: `s 469 the offence charged is one listed in section 469`: MAYBE BOOLEAN
  - [T] ss 536, 536.1, 554 (ccc21) asks for s 469: `s 469 the offence charged is one listed in section 469`: MAYBE BOOLEAN

### ccc16

- **Ranges (copied unchanged from `inputs/PARTS.md`):** 8719-9543 (15,484 words)
- **What the range holds:** sections 483 to 487.04 (43 section headings); PART XV Special Procedure and Powers.
- **Definition sections left to this part:** s 487.011 (line 9059), s 487.04 (line 9292).
- **Read first:** Part XV opens: ss 483 to 485.2 (officials' powers), 486 to 486.7 (exclusion of the public, publication bans, support persons, testimony outside the court room: these give the accused and witnesses rights and limits), 487 to 487.3 (warrants and production orders), and s 487.04 (DNA definitions, with long lists of designated offences by section: R1).
- **Names in the core it should expect to use:** Party (`a justice`, `a judge`, `a peace officer`, `a public officer`, `a witness`), Process document (`a search warrant`), Provision of the Code (the lists of designated offences).
- **Section 2 terms it will meet** (occurrences in its range, ordinary uses included; `*` = the keel's function can answer NOTHING): `justice` (196), `victim` (46)*, `peace officer` (45)*, `prosecutor` (36), `public officer` (35)*, `day` (32)*, `justice system participant` (18), `writing` (13)*, `indictment` (11)*, `bodily harm` (10), `criminal organization` (8)*, `organization` (8). Each is an input `s 2 <term>: ...` of type `MAYBE BOOLEAN` where the part's rule turns on it.
- **Seams: this part asks (asking section -> answering section: the input, its type):**
  - [T] s 487.011 -> ccc12 s 342.1(2) (ccc12): input `s 342.1(2) computer data and computer system`: MAYBE BOOLEAN
- **Seams: other parts ask this part (what its sections must answer, as functions that agree with the input name):**
  - [T] ss 487.051 to 487.0911 (ccc17) asks for s 487.04: `s 487.04 the offence is a primary designated offence / a secondary designated offence / a designated offence`: MAYBE BOOLEAN

### ccc17

- **Ranges (copied unchanged from `inputs/PARTS.md`):** 9544-10274 (15,292 words)
- **What the range holds:** sections 487.05 to 490.019 (43 section headings); no Part heading starts here (the range is inside a Part).
- **Definition sections left to this part:** s 488.01 (line 9864), s 488.1 (line 9915), s 490.011 (line 10060).
- **Read first:** Continues Part XV: DNA orders and warrants (487.05 to 487.0911), warrants by telecommunication, execution, seizure and detention of things (488 to 490.01), and the beginning of the sex offender information registration orders (490.011 on). The designated-offence lists of s 487.04 are in ccc16.
- **Names in the core it should expect to use:** Party, Process document (`a search warrant`), Provision of the Code (the designated-offence lists in ss 490.011 and 487.04).
- **Section 2 terms it will meet** (occurrences in its range, ordinary uses included; `*` = the keel's function can answer NOTHING): `peace officer` (50)*, `justice` (49), `day` (33)*, `Attorney General` (24)*, `writing` (22)*, `offender` (13), `summons` (13)*, `court of criminal jurisdiction` (12), `prosecutor` (12), `superior court of criminal jurisdiction` (11), `mental disorder` (11), `provincial court judge` (10). Each is an input `s 2 <term>: ...` of type `MAYBE BOOLEAN` where the part's rule turns on it.
- **Seams: this part asks (asking section -> answering section: the input, its type):**
  - [T] ss 487.051 to 487.0911 -> ccc16 s 487.04 (ccc16): input `s 487.04 the offence is a primary designated offence / a secondary designated offence / a designated offence`: MAYBE BOOLEAN
  - [T] s 488.1 -> ccc12 s 321 (ccc12): input `s 321 the thing is a document`: MAYBE BOOLEAN
- **Seams: other parts ask this part (what its sections must answer, as functions that agree with the input name):**
  - [T] ss 490.02 to 490.027, 490.04 (ccc18) asks for ss 490.011, 490.012, 490.019: `s 490.012 an order to comply with the Sex Offender Information Registration Act is in force`: MAYBE BOOLEAN

### ccc18

- **Ranges (copied unchanged from `inputs/PARTS.md`):** 10275-10956 (15,662 words)
- **What the range holds:** sections 490.02 to 492.2 (57 section headings); no Part heading starts here (the range is inside a Part).
- **Read first:** Continues Part XV: the Sex Offender Information Registration Act orders (490.02 on), forfeiture of offence-related property (490.1 to 490.9: s 2 `offence-related property`), forfeiture of weapons (491), restitution of property obtained by crime (491.1), photographic evidence, explosives (492), tracking device and transmission data warrants (492.1, 492.2).
- **Names in the core it should expect to use:** Party, Process document, Provision of the Code.
- **Section 2 terms it will meet** (occurrences in its range, ordinary uses included; `*` = the keel's function can answer NOTHING): `property` (114)*, `day` (56)*, `Attorney General` (54)*, `justice` (45), `offence-related property` (18)*, `mental disorder` (17), `offender` (17), `court of criminal jurisdiction` (15), `peace officer` (15)*, `victim` (13)*, `public officer` (11)*, `dwelling-house` (6). Each is an input `s 2 <term>: ...` of type `MAYBE BOOLEAN` where the part's rule turns on it.
- **Seams: this part asks (asking section -> answering section: the input, its type):**
  - [T] ss 490.02 to 490.027, 490.04 -> ccc17 ss 490.011, 490.012, 490.019 (ccc17): input `s 490.012 an order to comply with the Sex Offender Information Registration Act is in force`: MAYBE BOOLEAN

### ccc19

- **Ranges (copied unchanged from `inputs/PARTS.md`):** 10957-11031 (1,443 words)
- **What the range holds:** sections 492.21 to 492.31 (11 section headings); PART XV.1 Unreasonable Delay.
- **Definition sections left to this part:** s 492.21 (line 10961).
- **Read first:** Part XV.1 (unreasonable delay: ss 492.21 to 492.31). Small and self-contained: the stay of proceedings and the alternatives to it.
- **Names in the core it should expect to use:** Decision on the charge (`a stay of proceedings`), Stage of the proceedings, Party.
- **Section 2 terms it will meet** (occurrences in its range, ordinary uses included; `*` = the keel's function can answer NOTHING): `day` (21)*, `clerk of the court` (4)*. Each is an input `s 2 <term>: ...` of type `MAYBE BOOLEAN` where the part's rule turns on it.

### ccc20

- **Ranges (copied unchanged from `inputs/PARTS.md`):** 11032-11828 (17,835 words)
- **What the range holds:** sections 493 to 529.5 (58 section headings); PART XVI Compelling Appearance of Accused Before a Justice and Interim Release.
- **Definition sections left to this part:** s 493 (line 11036).
- **Read first:** Part XVI (compelling appearance and interim release): arrest with and without warrant (494 to 499), appearance notices, undertakings and release orders (500 to 502, 515), the hearing and its reverse onuses (515(6)), reviews (520 to 522), detention, trial delay (525), powers of entry to arrest (529 to 529.5). s 493 defines terms (including `judge`) for the Part. Heavy use of s 2 `justice`, `peace officer`, `undertaking`, `appearance notice`, `summons`, `release order`, `prosecutor`.
- **Names in the core it should expect to use:** Party (`a justice`, `a judge`, `a peace officer`, `a surety`, `the prosecutor`), Process document (`an appearance notice`, `an undertaking`, `a release order`, `a recognizance`, `a summons`, `a warrant for arrest`), Outcome of interim release, Stage of the proceedings, Provision of the Code.
- **Section 2 terms it will meet** (occurrences in its range, ordinary uses included; `*` = the keel's function can answer NOTHING): `justice` (249), `peace officer` (87)*, `undertaking` (62)*, `appearance notice` (54)*, `summons` (53)*, `release order` (48)*, `prosecutor` (44), `victim` (25)*, `dwelling-house` (23), `day` (21)*, `writing` (15)*, `Attorney General` (12)*. Each is an input `s 2 <term>: ...` of type `MAYBE BOOLEAN` where the part's rule turns on it.
- **Seams: this part asks (asking section -> answering section: the input, its type):**
  - [T] ss 515(3), (4.1), (4.3), (6) -> keel s 3.01(1), (2) (keel): input `s 3.01 the offence counts as one in which violence is used, threatened or attempted`: MAYBE BOOLEAN
  - [T] ss 498, 515, 522, 523 -> ccc15 s 469 (ccc15): input `s 469 the offence charged is one listed in section 469`: MAYBE BOOLEAN
  - [T] ss 515, 522, 523 -> ccc24 ss 673, 679, 680 (ccc24): input `s 679 the person has been released pending determination of an appeal`: MAYBE BOOLEAN
  - [H] ss 515, 522 -> ccc2 to ccc13 the offence sections (ccc2 to ccc13): input `whether the offence charged is an indictable offence, and the punishment it is liable to`: Class of offence
- **Seams: other parts ask this part (what its sections must answer, as functions that agree with the input name):**
  - [T] s 2 "release order" (keel) asks for s 493 "judge": `s 493 the maker of the order is a judge as defined in section 493`: BOOLEAN
  - [T] ss 679, 680 (ccc24) asks for ss 495.1, 512.3, 515, 522: `s 515 the interim release outcome the accused was given`: Outcome of interim release
  - [T] s 145 (ccc5) asks for ss 508, 515: `s 515 the accused is bound by a release order`: BOOLEAN

### ccc21

- **Ranges (copied unchanged from `inputs/PARTS.md`):** 11829-12462 (15,790 words)
- **What the range holds:** sections 530 to 572 (66 section headings); PART XVII Language of Accused; PART XVIII Procedure on Preliminary Inquiry; PART XVIII.1 Case Management Judge; PART XIX Indictable Offences — Trial Without Jury.
- **Definition sections left to this part:** s 552 (line 12215).
- **Read first:** Part XVII (language of the accused), Part XVIII (preliminary inquiry, 535 to 551), Part XVIII.1 (case management judge), Part XIX (indictable offences, trial without jury: absolute jurisdiction s 553, election and re-election ss 554 to 565, indictments ss 566 to 569). s 552 defines terms for Part XIX; the s 553 list is by section (R1).
- **Names in the core it should expect to use:** Mode of proceeding, Decision on the charge (`an order to stand trial`, `a discharge at the preliminary inquiry`), Party, Province or territory (Nunavut ss 535 to 572), Provision of the Code (the s 553 list), Process document.
- **Section 2 terms it will meet** (occurrences in its range, ordinary uses included; `*` = the keel's function can answer NOTHING): `justice` (166), `provincial court judge` (79), `prosecutor` (49), `indictment` (33)*, `writing` (23)*, `counsel` (19), `territorial division` (15)*, `day` (11)*, `organization` (11), `clerk of the court` (10)*, `prison` (9)*, `Attorney General` (7)*. Each is an input `s 2 <term>: ...` of type `MAYBE BOOLEAN` where the part's rule turns on it.
- **Seams: this part asks (asking section -> answering section: the input, its type):**
  - [T] ss 536, 536.1, 554 -> ccc15 s 469 (ccc15): input `s 469 the offence charged is one listed in section 469`: MAYBE BOOLEAN
  - [T] ss 536, 536.1, 561, 561.1 -> ccc22 s 577 (ccc22): input `s 577 a direct indictment has been preferred`: MAYBE BOOLEAN
  - [H] ss 553 to 555 -> ccc2 to ccc13 the offence sections (ccc2 to ccc13): input `the class of the offence charged (the list in s 553 is tested by section number)`: Class of offence
- **Seams: other parts ask this part (what its sections must answer, as functions that agree with the input name):**
  - [T] ss 686, 695 (ccc24) asks for ss 553, 561, 561.1: `s 553 the offence is within the absolute jurisdiction of a provincial court judge; s 561 the accused re-elected`: MAYBE BOOLEAN
  - [T] ss 573.1, 573.2, 574 (ccc22) asks for ss 536, 548, 552: `s 548 the decision the justice made at the preliminary inquiry`: Decision on the charge

### ccc22

- **Ranges (copied unchanged from `inputs/PARTS.md`):** 12463-13305 (18,013 words)
- **What the range holds:** sections 573 to 672 (112 section headings); PART XIX.1 Nunavut Court of Justice; PART XX Procedure in Jury Trials and General Provisions.
- **Read first:** Part XIX.1 (Nunavut Court of Justice) and Part XX (jury trials and general provisions: preferring indictments, counts and particulars, joinder, pleas (606), juries (626 to 653), verdicts (660 to 663), previous convictions (664 to 668), jurisdiction on appointment (669.1 to 669.3), defects in jury process). s 606 is one of the six sections s 2.2 is for the purposes of.
- **Names in the core it should expect to use:** Decision on the charge, Party (`a juror`, `the jury`, `the clerk of the court`, `counsel for the accused`), Process document (`an information`, `an indictment`, `a count`, `a subpoena`), Mode of proceeding.
- **Section 2 terms it will meet** (occurrences in its range, ordinary uses included; `*` = the keel's function can answer NOTHING): `indictment` (106)*, `count` (79), `prosecutor` (53), `justice` (38), `counsel` (35), `Attorney General` (25)*, `property` (22)*, `provincial court judge` (19), `clerk of the court` (15)*, `writing` (14)*, `organization` (13), `victim` (9)*. Each is an input `s 2 <term>: ...` of type `MAYBE BOOLEAN` where the part's rule turns on it.
- **Seams: this part asks (asking section -> answering section: the input, its type):**
  - [T] s 606 -> keel s 2.2(1), (2) (keel): input `s 2.2 the individual may act on the victim’s behalf, subject to subsection (2)`: MAYBE BOOLEAN
  - [T] ss 573.1, 573.2, 574 -> ccc21 ss 536, 548, 552 (ccc21): input `s 548 the decision the justice made at the preliminary inquiry`: Decision on the charge
  - [T] s 657.4 -> ccc13 s 402.1 (ccc13): input `s 402.1 the information is identity information`: MAYBE BOOLEAN
  - [T] s 606(4.1) -> ccc28 s 752 "serious personal injury offence" (ccc28): input `s 752 the offence is a serious personal injury offence`: MAYBE BOOLEAN
- **Seams: other parts ask this part (what its sections must answer, as functions that agree with the input name):**
  - [T] ss 536, 536.1, 561, 561.1 (ccc21) asks for s 577: `s 577 a direct indictment has been preferred`: MAYBE BOOLEAN

### ccc23

- **Ranges (copied unchanged from `inputs/PARTS.md`):** 13306-14068 (17,134 words)
- **What the range holds:** sections 672.1 to 672.95 (94 section headings); PART XX.1 Mental Disorder.
- **Definition sections left to this part:** s 672.1 (line 13310), s 672.21 (line 13414), s 672.37 (line 13494), s 672.51 (line 13691), s 672.68 (line 13821).
- **Read first:** Part XX.1 (mental disorder): assessment orders (672.11 to 672.191), fitness (672.22 to 672.33), the verdict of not criminally responsible (672.34 to 672.37), Review Boards (672.38 to 672.44), disposition hearings and dispositions (672.45 to 672.64), high-risk accused, appeals (672.72 to 672.78), reviews (672.81 to 672.84), transfers and enforcement. s 672.1(1) defines terms for the Part, including `Review Board`, which s 2 points to.
- **Names in the core it should expect to use:** Decision on the charge (`a verdict of not criminally responsible on account of mental disorder`, `a verdict of unfit to stand trial`), Party (`a Review Board`, `the court`, `the accused`), Stage of the proceedings.
- **Section 2 terms it will meet** (occurrences in its range, ordinary uses included; `*` = the keel's function can answer NOTHING): `prosecutor` (40), `justice` (37), `unfit to stand trial` (36), `victim` (33)*, `Attorney General` (29)*, `day` (29)*, `mental disorder` (29), `court of appeal` (26), `counsel` (23), `offender` (23), `peace officer` (8)*, `writing` (8)*. Each is an input `s 2 <term>: ...` of type `MAYBE BOOLEAN` where the part's rule turns on it.
- **Seams: this part asks (asking section -> answering section: the input, its type):**
  - [T] s 672.5 -> keel s 2.2(1), (2) (keel): input `s 2.2 the individual may act on the victim’s behalf, subject to subsection (2)`: MAYBE BOOLEAN
  - [T] s 672.5 -> keel s 2 "victim" (the extension for ss 672.5, 722, 745.63) (keel): input `s 2 victim: the purpose is section 672.5`: MAYBE BOOLEAN
- **Seams: other parts ask this part (what its sections must answer, as functions that agree with the input name):**
  - [T] s 2 "summons"; s 2 "videoconference" (keel) asks for s 672.1(1) "Review Board": `s 672.1(1) the issuer is the chairperson of a Review Board`: BOOLEAN

### ccc24

- **Ranges (copied unchanged from `inputs/PARTS.md`):** 14069-14871 (15,549 words)
- **What the range holds:** sections 673 to 715.27 (107 section headings); PART XXI Appeals — Indictable Offences; PART XXI.1 Applications for Ministerial Review — Miscarriages of Justice; PART XXI.2 Miscarriage of Justice Review Commission; PART XXII Procuring Attendance; PART XXII.01 Remote Attendance by Certain Persons.
- **Definition sections left to this part:** s 673 (line 14073), s 696.3 (line 14401), s 696.7 (line 14429), s 715.25 (line 14830), s 715.27 (line 14858).
- **Read first:** Part XXI (appeals, indictable offences: ss 673 to 696), Part XXI.1 (ministerial review of miscarriages of justice), Part XXI.2 (the Miscarriage of Justice Review Commission: mostly machinery), Part XXII (procuring attendance: subpoenas, warrants, commission evidence), Part XXII.01 (remote attendance). s 673 and s 696.3 define `court of appeal` again for their own sections. A later version of Part XXI.1 is in ccc32 (amendments not in force).
- **Names in the core it should expect to use:** Party (`a court of appeal`, `the Supreme Court of Canada`, `the Minister of Justice`, `the Attorney General`), Decision on the charge, Kind of sentence, Stage of the proceedings (`appeal`), Process document (`a subpoena`).
- **Section 2 terms it will meet** (occurrences in its range, ordinary uses included; `*` = the keel's function can answer NOTHING): `court of appeal` (112), `justice` (62), `provincial court judge` (40), `videoconference` (33), `counsel` (31), `audioconference` (26), `Attorney General` (24)*, `offender` (23), `indictment` (17)*, `undertaking` (16)*, `prosecutor` (13), `court of criminal jurisdiction` (12). Each is an input `s 2 <term>: ...` of type `MAYBE BOOLEAN` where the part's rule turns on it.
- **Seams: this part asks (asking section -> answering section: the input, its type):**
  - [T] ss 679, 680 -> ccc20 ss 495.1, 512.3, 515, 522 (ccc20): input `s 515 the interim release outcome the accused was given`: Outcome of interim release
  - [T] ss 675, 676 -> ccc27 s 743.6 (ccc27): input `s 743.6 the court ordered a delay in eligibility for parole`: MAYBE BOOLEAN
  - [T] ss 686, 695 -> ccc21 ss 553, 561, 561.1 (ccc21): input `s 553 the offence is within the absolute jurisdiction of a provincial court judge; s 561 the accused re-elected`: MAYBE BOOLEAN
- **Seams: other parts ask this part (what its sections must answer, as functions that agree with the input name):**
  - [T] ss 515, 522, 523 (ccc20) asks for ss 673, 679, 680: `s 679 the person has been released pending determination of an appeal`: MAYBE BOOLEAN

### ccc25

- **Ranges (copied unchanged from `inputs/PARTS.md`):** 14872-15170 (6,166 words)
- **What the range holds:** sections 715.3 to 715.6 (31 section headings); PART XXII.1 Remediation Agreements; PART XXII.2 Alternative Measures and Restorative Justice Processes.
- **Definition sections left to this part:** s 715.3 (line 14874), s 715.44 (line 15039).
- **Read first:** Part XXII.1 (remediation agreements: for organizations; s 715.3 takes `organization` and `victim` from s 2 with changes) and Part XXII.2 (alternative measures and restorative justice: warnings, referrals, conferences, records). The offences a remediation agreement may cover are in the Schedule to Part XXII.1, which is in ccc29's range.
- **Names in the core it should expect to use:** Party (`an organization`, `the prosecutor`, `the victim`), Kind of sentence, Provision of the Code (the Schedule offences by section).
- **Section 2 terms it will meet** (occurrences in its range, ordinary uses included; `*` = the keel's function can answer NOTHING): `organization` (62), `prosecutor` (41), `victim` (37)*, `justice` (25), `offender` (10), `Attorney General` (7)*, `peace officer` (4)*. Each is an input `s 2 <term>: ...` of type `MAYBE BOOLEAN` where the part's rule turns on it.
- **Seams: this part asks (asking section -> answering section: the input, its type):**
  - [T] s 715.37 -> keel s 2.2(1), (2) (keel): input `s 2.2 the individual may act on the victim’s behalf, subject to subsection (2)`: MAYBE BOOLEAN
  - [T] s 715.3 "organization", "victim" -> keel s 2 "organization", "victim" (keel): input `s 2 organization / s 2 victim (s 715.3 narrows or widens them: its own words govern)`: MAYBE BOOLEAN
  - [T] ss 715.32(2), 715.43(2), (3) -> ccc29 the Schedule to Part XXII.1 (text lines 17351-17388) (ccc29): input `Schedule to Part XXII.1 the offence is listed`: MAYBE BOOLEAN

### ccc26

- **Ranges (copied unchanged from `inputs/PARTS.md`):** 15171-15768 (12,650 words)
- **What the range holds:** sections 716 to 736 (62 section headings); PART XXIII Sentencing.
- **Definition sections left to this part:** s 716 (line 15175), s 732.1 (line 15518), s 734.8 (line 15735).
- **Read first:** Part XXIII opens: sentencing purposes and principles (718 to 718.4), commencement (719), procedure and evidence (720 to 729.2: victim impact statements 722, reasons 726.2), discharges (730), probation (731 to 733.1), fines (734 to 736). s 716, s 732.1 and s 734.8 define terms for their scope. The punishment of the offence being sentenced is in the offence part (R2).
- **Names in the core it should expect to use:** Kind of sentence, Length of time, Imprisonment, Fine, Punishment, Party (`the offender`, `the victim`, `a probation officer`, `an organization`), Stage of the proceedings (`sentencing`).
- **Section 2 terms it will meet** (occurrences in its range, ordinary uses included; `*` = the keel's function can answer NOTHING): `offender` (178), `victim` (33)*, `organization` (30), `prosecutor` (23), `Attorney General` (22)*, `day` (19)*, `justice` (17), `intimate partner` (5)*, `territorial division` (5)*, `release order` (4)*, `clerk of the court` (3)*, `court of criminal jurisdiction` (3). Each is an input `s 2 <term>: ...` of type `MAYBE BOOLEAN` where the part's rule turns on it.
- **Seams: this part asks (asking section -> answering section: the input, its type):**
  - [T] s 722 -> keel s 2.2(1), (2) (keel): input `s 2.2 the individual may act on the victim’s behalf, subject to subsection (2)`: MAYBE BOOLEAN
  - [T] ss 718.3(8), 726.21 -> keel s 3.01(1), (2) (keel): input `s 3.01 the offence counts as one in which violence is used, threatened or attempted`: MAYBE BOOLEAN
  - [T] s 722 -> keel s 2 "victim" (keel): input `s 2 victim: the purpose is section 722`: MAYBE BOOLEAN
  - [T] s 729.1(2) -> ccc11 s 320.11 (ccc11): input `s 320.11 the person is an analyst`: MAYBE BOOLEAN
  - [H] ss 718.2, 718.3, 743.1 -> ccc2 to ccc13 the offence sections (ccc2 to ccc13): input `the punishment the offence charged is liable to (from the offence section itself)`: Punishment
- **Seams: other parts ask this part (what its sections must answer, as functions that agree with the input name):**
  - [T] ss 737, 738 (ccc27) asks for ss 734, 734.3, 734.8: `s 734.8 the fine and its penalty`: Fine

### ccc27

- **Ranges (copied unchanged from `inputs/PARTS.md`):** 15769-16295 (12,821 words)
- **What the range holds:** sections 737 to 751.1 (55 section headings); no Part heading starts here (the range is inside a Part).
- **Definition sections left to this part:** s 742 (line 15859).
- **Read first:** Continues Part XXIII: victim surcharge (737), restitution (737.1 to 741.2), conditional sentences (742 to 742.7), imprisonment, parole eligibility and life sentences (743 to 746.1), pardons (748 to 749), disabilities (750), costs in libel (751). The life-sentence rules turn on the kind of homicide offence (ccc8).
- **Names in the core it should expect to use:** Kind of sentence, Length of time, Imprisonment (`imprisonment for life`), Fine, Kind of homicide offence, Party (`the offender`, `the Correctional Service of Canada`, `the Parole Board of Canada`, `a supervisor`).
- **Section 2 terms it will meet** (occurrences in its range, ordinary uses included; `*` = the keel's function can answer NOTHING): `offender` (148), `day` (47)*, `victim` (29)*, `Attorney General` (16)*, `justice` (12), `property` (10)*, `court of criminal jurisdiction` (5), `territorial division` (5)*, `superior court of criminal jurisdiction` (4), `peace officer` (4)*. Each is an input `s 2 <term>: ...` of type `MAYBE BOOLEAN` where the part's rule turns on it.
- **Seams: this part asks (asking section -> answering section: the input, its type):**
  - [T] ss 737.1, 745.63 -> keel s 2.2(1), (2) (keel): input `s 2.2 the individual may act on the victim’s behalf, subject to subsection (2)`: MAYBE BOOLEAN
  - [T] s 745.63 -> keel s 2 "victim" (keel): input `s 2 victim: the purpose is section 745.63`: MAYBE BOOLEAN
  - [T] ss 737, 738 -> ccc26 ss 734, 734.3, 734.8 (ccc26): input `s 734.8 the fine and its penalty`: Fine
  - [T] s 745 and 745.01 to 745.6 -> ccc8 ss 231, 235 (ccc8): input `s 231 the kind of homicide offence`: Kind of homicide offence
- **Seams: other parts ask this part (what its sections must answer, as functions that agree with the input name):**
  - [T] ss 675, 676 (ccc24) asks for s 743.6: `s 743.6 the court ordered a delay in eligibility for parole`: MAYBE BOOLEAN

### ccc28

- **Ranges (copied unchanged from `inputs/PARTS.md`):** 16296-16683 (8,757 words)
- **What the range holds:** sections 752 to 784 (43 section headings); PART XXIV Dangerous Offenders and Long-term Offenders; PART XXV Effect and Enforcement of Undertakings, Release Orders and Recognizances; PART XXVI Extraordinary Remedies.
- **Definition sections left to this part:** s 752 (line 16300).
- **Read first:** Part XXIV (dangerous offenders and long-term offenders: s 752 defines `serious personal injury offence`, `primary designated offence`, ... for the Part), Part XXV (forfeiture of recognizances) and Part XXVI (extraordinary remedies: habeas corpus, certiorari, mandamus). ccc22 asks s 752's `serious personal injury offence`.
- **Names in the core it should expect to use:** Kind of sentence, Length of time, Provision of the Code (the lists of offences), Party (`the offender`, `the Parole Board of Canada`, `the Attorney General`, `the keeper of a prison`).
- **Section 2 terms it will meet** (occurrences in its range, ordinary uses included; `*` = the keel's function can answer NOTHING): `offender` (126), `release order` (37)*, `recognizance` (33), `undertaking` (20)*, `Attorney General` (18)*, `justice` (18), `provincial court judge` (15), `prosecutor` (13), `prison` (12)*, `day` (11)*, `court of appeal` (9), `clerk of the court` (8)*. Each is an input `s 2 <term>: ...` of type `MAYBE BOOLEAN` where the part's rule turns on it.
- **Seams: other parts ask this part (what its sections must answer, as functions that agree with the input name):**
  - [T] s 606(4.1) (ccc22) asks for s 752 "serious personal injury offence": `s 752 the offence is a serious personal injury offence`: MAYBE BOOLEAN

### ccc29

- **Ranges (copied unchanged from `inputs/PARTS.md`):** 16684-17450 (15,922 words)
- **What the range holds:** sections 785 to 29 (109 section headings); PART XXVII Summary Convictions; PART XXVIII Miscellaneous; Forms; Forms; SCHEDULE TO PART XX.1; SCHEDULE TO PART XXII.1 (Section 715.3 and subsections 715.32(2) and 715.43(2) and (3)) Offences in respect of which a r.
- **Definition sections left to this part:** s 785 (line 16688), s 812 (line 17120), s 829 (line 17251), s 841 (line 17317).
- **Read first:** Part XXVII (summary convictions: general penalty s 787, procedure, sureties to keep the peace ss 810 to 811.1, appeals 812 to 839, fees 840), Part XXVIII (electronic documents, oaths, copies, the Forms clause s 849), and the Schedules (to Part XX.1: repealed; to Part XXII.1: the offences a remediation agreement may cover; to Part XXV; to Part XXVII: fees), then Forms 1 to the point where ccc30 begins.
- **Names in the core it should expect to use:** Mode of proceeding, Punishment, Fine, Imprisonment, the constant `two years less a day`, Process document, Party (`the informant`, `the prosecutor`, `a justice`), Provision of the Code.
- **Section 2 terms it will meet** (occurrences in its range, ordinary uses included; `*` = the keel's function can answer NOTHING): `recognizance` (130), `justice` (90), `provincial court judge` (66), `Attorney General` (54)*, `day` (21)*, `firearm` (20), `prosecutor` (20), `intimate partner` (14)*, `weapon` (14)*, `ammunition` (14)*, `prison` (12)*, `peace officer` (10)*. Each is an input `s 2 <term>: ...` of type `MAYBE BOOLEAN` where the part's rule turns on it.
- **Seams: this part asks (asking section -> answering section: the input, its type):**
  - [T] s 810.03(4) -> keel s 3.01(1), (2) (keel): input `s 3.01 the offence counts as one in which violence is used, threatened or attempted`: MAYBE BOOLEAN
  - [T] s 811.1 -> ccc11 s 320.11 (ccc11): input `s 320.11 the person is an analyst`: MAYBE BOOLEAN
- **Seams: other parts ask this part (what its sections must answer, as functions that agree with the input name):**
  - [T] ss 715.32(2), 715.43(2), (3) (ccc25) asks for the Schedule to Part XXII.1 (text lines 17351-17388): `Schedule to Part XXII.1 the offence is listed`: MAYBE BOOLEAN
  - [T] offence sections that say "punishable on summary conviction" and state no penalty (ccc2 to ccc13) asks for s 787(1): `s 787(1) the general penalty for an offence punishable on summary conviction`: Punishment

### ccc30

- **Ranges (copied unchanged from `inputs/PARTS.md`):** 17451-18463 (15,934 words)
- **What the range holds:** sections 1 to 9 (61 section headings); FORM 1 (Sections 320.29, 462.32, 462.321 and 487) Information To Obtain a Search Warrant; FORM 2 (Sections 506 and 788) Information; FORM 3; FORM 4 (Sections 566, 566.1, 580 and 591) Heading of Indictment; FORM 5 (Sections 320.29 and 487) Warrant To Search; FORM 5.001 (Subsection 487.012(1)) Preservation Demand.
- **Read first:** Forms 1 to 23 (and their sub-forms 5.001 to 5.3, 6.1 to 6.4, 7.1, 10.1, 11.1, 16.1). A Form that only prescribes the wording of a document is machinery (reason 2 of the three), unless its text states a rule, which is then encoded. Each Form is a coverage row.
- **Names in the core it should expect to use:** Process document (each Form prescribes the wording of one), Provision of the Code (the sections each Form names).
- **Section 2 terms it will meet** (occurrences in its range, ordinary uses included; `*` = the keel's function can answer NOTHING): `territorial division` (87)*, `peace officer` (82)*, `justice` (70), `day` (41)*, `offender` (35), `public officer` (25)*, `undertaking` (25)*, `summons` (23)*, `release order` (22)*, `prison` (21)*, `clerk of the court` (18)*, `appearance notice` (15)*. Each is an input `s 2 <term>: ...` of type `MAYBE BOOLEAN` where the part's rule turns on it.

### ccc31

- **Ranges (copied unchanged from `inputs/PARTS.md`):** 18464-19055 (9,318 words)
- **What the range holds:** sections 1 to 9 (38 section headings); FORM 24 (Section 550) Warrant of Committal of Witness for Failure to Enter into Recognizance; FORM 25 (Section 708) Warrant of Committal for Contempt; FORM 26 (Section 827) Warrant of Committal in Default of Payment of Costs of an Appeal; FORM 27 (Section 773) Warrant of Committal on Forfeiture of Amounts; FORM 28 (Section 528) Endorsement of Warrant; FORM 28.1.
- **Read first:** Forms 24 to 54 (warrants of committal, endorsements, recognizance Form 32, probation order Form 46, assessment orders, SOIRA Forms 52 to 54), then the heading RELATED PROVISIONS at line 19054. Each Form is a coverage row, as for ccc30.
- **Names in the core it should expect to use:** Process document, Provision of the Code.
- **Section 2 terms it will meet** (occurrences in its range, ordinary uses included; `*` = the keel's function can answer NOTHING): `day` (38)*, `territorial division` (37)*, `prison` (33)*, `offender` (31), `justice` (26), `mental disorder` (14), `recognizance` (12), `clerk of the court` (11)*, `peace officer` (10)*, `property` (9)*, `provincial court judge` (9), `Attorney General` (7)*. Each is an input `s 2 <term>: ...` of type `MAYBE BOOLEAN` where the part's rule turns on it.

### ccc32

- **Ranges (copied unchanged from `inputs/PARTS.md`):** 19056-19797 (12,598 words)
- **What the range holds:** sections 10 to 45 (136 section headings); PART XXI.1 Miscarriage of Justice Reviews.
- **Definition sections left to this part:** s 22 (line 19070), s 23 (line 19077), s 96 (line 19419), s 696.1 (line 19556), s 7 (line 19653).
- **Read first:** Related provisions of amending Acts (from line 19056) and, from line 19517 (AMENDMENTS NOT IN FORCE), amendments that are not in force. Each related or transitional provision is a coverage row, encoded if it still affects someone, otherwise machinery (reason 2). A not-in-force block is a second, future text of provisions that ccc9, ccc24 and ccc27 encode in their in-force form: give each name a suffix such as `(not in force)` so that it cannot collide with theirs.
- **Names in the core it should expect to use:** Provision of the Code (the sections amended or saved), Date from `IMPORT daydate` (commencement days).
- **Section 2 terms it will meet** (occurrences in its range, ordinary uses included; `*` = the keel's function can answer NOTHING): `day` (175)*, `intimate partner` (33)*, `justice` (18), `firearm` (12), `court of appeal` (10), `Attorney General` (9)*, `prohibited firearm` (3)*. Each is an input `s 2 <term>: ...` of type `MAYBE BOOLEAN` where the part's rule turns on it.

## 7. All the seams, in one table

| ev | asking part | asking section | answering part | answering section | input name | type |
| --- | --- | --- | --- | --- | --- | --- |
| T | keel | s 2 "criminal organization" | ccc14 | s 467.1(1) | `s 467.1(1) the group is a criminal organization` | MAYBE BOOLEAN |
| T | keel | s 2 "serious offence" | ccc14 | s 467.1(1) | `s 467.1(1) the offence is a serious offence` | MAYBE BOOLEAN |
| T | keel | s 2 "terrorist activity"; s 2.3(1)(a) | ccc3 | s 83.01(1) | `s 83.01(1) the act or omission is a terrorist activity` | MAYBE BOOLEAN |
| T | keel | s 2 "terrorist group"; s 2 "terrorism offence" | ccc3 | s 83.01(1) | `s 83.01(1) the group is a terrorist group` | MAYBE BOOLEAN |
| T | keel | s 2.1 | ccc4 | s 84(1) | `s 84(1) the thing is within the meaning the term has in subsection 84(1)` | MAYBE BOOLEAN |
| T | keel | s 2 "steal" | ccc12 | s 322 | `s 322 the person commits theft` | MAYBE BOOLEAN |
| T | keel | s 2 "release order" | ccc20 | s 493 "judge" | `s 493 the maker of the order is a judge as defined in section 493` | BOOLEAN |
| T | keel | s 2 "summons"; s 2 "videoconference" | ccc23 | s 672.1(1) "Review Board" | `s 672.1(1) the issuer is the chairperson of a Review Board` | BOOLEAN |
| T | keel | s 2 "justice system participant" (b)(viii.1) | ccc1 | s 25.1(1) "public officer" | `s 25.1(1) the person is a public officer, or acts at the direction of one` | BOOLEAN |
| T | ccc22 | s 606 | keel | s 2.2(1), (2) | `s 2.2 the individual may act on the victim’s behalf, subject to subsection (2)` | MAYBE BOOLEAN |
| T | ccc23 | s 672.5 | keel | s 2.2(1), (2) | `s 2.2 the individual may act on the victim’s behalf, subject to subsection (2)` | MAYBE BOOLEAN |
| T | ccc25 | s 715.37 | keel | s 2.2(1), (2) | `s 2.2 the individual may act on the victim’s behalf, subject to subsection (2)` | MAYBE BOOLEAN |
| T | ccc26 | s 722 | keel | s 2.2(1), (2) | `s 2.2 the individual may act on the victim’s behalf, subject to subsection (2)` | MAYBE BOOLEAN |
| T | ccc27 | ss 737.1, 745.63 | keel | s 2.2(1), (2) | `s 2.2 the individual may act on the victim’s behalf, subject to subsection (2)` | MAYBE BOOLEAN |
| T | ccc4 | ss 109(1), 110(1), (2.1) | keel | s 3.01(1), (2) | `s 3.01 the offence counts as one in which violence is used, threatened or attempted` | MAYBE BOOLEAN |
| T | ccc8 | s 263.1(1) | keel | s 3.01(1), (2) | `s 3.01 the offence counts as one in which violence is used, threatened or attempted` | MAYBE BOOLEAN |
| T | ccc20 | ss 515(3), (4.1), (4.3), (6) | keel | s 3.01(1), (2) | `s 3.01 the offence counts as one in which violence is used, threatened or attempted` | MAYBE BOOLEAN |
| T | ccc26 | ss 718.3(8), 726.21 | keel | s 3.01(1), (2) | `s 3.01 the offence counts as one in which violence is used, threatened or attempted` | MAYBE BOOLEAN |
| T | ccc29 | s 810.03(4) | keel | s 3.01(1), (2) | `s 3.01 the offence counts as one in which violence is used, threatened or attempted` | MAYBE BOOLEAN |
| T | ccc23 | s 672.5 | keel | s 2 "victim" (the extension for ss 672.5, 722, 745.63) | `s 2 victim: the purpose is section 672.5` | MAYBE BOOLEAN |
| T | ccc26 | s 722 | keel | s 2 "victim" | `s 2 victim: the purpose is section 722` | MAYBE BOOLEAN |
| T | ccc27 | s 745.63 | keel | s 2 "victim" | `s 2 victim: the purpose is section 745.63` | MAYBE BOOLEAN |
| T | ccc25 | s 715.3 "organization", "victim" | keel | s 2 "organization", "victim" | `s 2 organization / s 2 victim (s 715.3 narrows or widens them: its own words govern)` | MAYBE BOOLEAN |
| T | ccc17 | ss 487.051 to 487.0911 | ccc16 | s 487.04 | `s 487.04 the offence is a primary designated offence / a secondary designated offence / a designated offence` | MAYBE BOOLEAN |
| T | ccc18 | ss 490.02 to 490.027, 490.04 | ccc17 | ss 490.011, 490.012, 490.019 | `s 490.012 an order to comply with the Sex Offender Information Registration Act is in force` | MAYBE BOOLEAN |
| T | ccc20 | ss 498, 515, 522, 523 | ccc15 | s 469 | `s 469 the offence charged is one listed in section 469` | MAYBE BOOLEAN |
| T | ccc21 | ss 536, 536.1, 554 | ccc15 | s 469 | `s 469 the offence charged is one listed in section 469` | MAYBE BOOLEAN |
| T | ccc20 | ss 515, 522, 523 | ccc24 | ss 673, 679, 680 | `s 679 the person has been released pending determination of an appeal` | MAYBE BOOLEAN |
| T | ccc24 | ss 679, 680 | ccc20 | ss 495.1, 512.3, 515, 522 | `s 515 the interim release outcome the accused was given` | Outcome of interim release |
| T | ccc24 | ss 675, 676 | ccc27 | s 743.6 | `s 743.6 the court ordered a delay in eligibility for parole` | MAYBE BOOLEAN |
| T | ccc24 | ss 686, 695 | ccc21 | ss 553, 561, 561.1 | `s 553 the offence is within the absolute jurisdiction of a provincial court judge; s 561 the accused re-elected` | MAYBE BOOLEAN |
| T | ccc22 | ss 573.1, 573.2, 574 | ccc21 | ss 536, 548, 552 | `s 548 the decision the justice made at the preliminary inquiry` | Decision on the charge |
| T | ccc21 | ss 536, 536.1, 561, 561.1 | ccc22 | s 577 | `s 577 a direct indictment has been preferred` | MAYBE BOOLEAN |
| T | ccc27 | ss 737, 738 | ccc26 | ss 734, 734.3, 734.8 | `s 734.8 the fine and its penalty` | Fine |
| T | ccc10 | ss 278.32 to 278.38 | ccc9 | ss 278.29, 278.3, 278.31 | `s 278.3 an application for a hearing on records in the accused’s possession has been made` | MAYBE BOOLEAN |
| T | ccc9 | ss 278.2 to 278.28 (and ss 272, 273) | ccc10 | ss 278.32 to 278.38 and ss 279, 279.1 | `identity by section number (a list of offences): no input is needed` | - |
| T | ccc3 | ss 83.13, 83.14 | ccc14 | ss 462.32 to 462.4 | `s 462.34 the review of the special warrant or restraint order has been applied for` | MAYBE BOOLEAN |
| T | ccc3 | ss 83.222, 83.223 | ccc10 | s 320(8) | `s 320(8) the court and the judge the warrant of seizure is made to` | Party |
| T | ccc3 | s 83.01(1) "terrorist activity" | ccc1 | s 7(3.74), (3.75) | `s 7 the act or omission is deemed to have been committed in Canada` | MAYBE BOOLEAN |
| T | ccc4 | ss 94, 110.1 | ccc5 | ss 110.4, 117.07, 117.1 | `s 117.07 the person is exempt from the prohibition (a public officer, and the other persons s 117.07 names)` | MAYBE BOOLEAN |
| T | ccc5 | ss 110.4 to 113 | ccc4 | ss 109, 110, 110.1 | `s 110.1 an emergency prohibition order has been made` | MAYBE BOOLEAN |
| T | ccc5 | s 145 | ccc20 | ss 508, 515 | `s 515 the accused is bound by a release order` | BOOLEAN |
| T | ccc4 | ss 98, 102.1 | ccc12 | ss 321, 342.1(2) | `s 321 the person breaks; s 342.1(2) computer data and computer system` | MAYBE BOOLEAN |
| T | ccc8 | s 241.4 | ccc12 | s 321 | `s 321 the thing is a document` | MAYBE BOOLEAN |
| T | ccc16 | s 487.011 | ccc12 | s 342.1(2) | `s 342.1(2) computer data and computer system` | MAYBE BOOLEAN |
| T | ccc17 | s 488.1 | ccc12 | s 321 | `s 321 the thing is a document` | MAYBE BOOLEAN |
| T | ccc13 | s 430(8) | ccc12 | s 342.1(2) | `s 342.1(2) computer data` | MAYBE BOOLEAN |
| T | ccc12 | s 335(2) | ccc11 | s 320.11 | `s 320.11 the thing is a vessel` | MAYBE BOOLEAN |
| T | ccc26 | s 729.1(2) | ccc11 | s 320.11 | `s 320.11 the person is an analyst` | MAYBE BOOLEAN |
| T | ccc29 | s 811.1 | ccc11 | s 320.11 | `s 320.11 the person is an analyst` | MAYBE BOOLEAN |
| T | ccc22 | s 657.4 | ccc13 | s 402.1 | `s 402.1 the information is identity information` | MAYBE BOOLEAN |
| T | ccc10 | s 286.1(5) | ccc8 | s 197(1) | `s 197(1) the place is a place; the place is a public place` | MAYBE BOOLEAN |
| T | ccc15 | s 478(5) | ccc10 | s 297 | `s 297 the publication is a newspaper` | MAYBE BOOLEAN |
| T | ccc25 | ss 715.32(2), 715.43(2), (3) | ccc29 | the Schedule to Part XXII.1 (text lines 17351-17388) | `Schedule to Part XXII.1 the offence is listed` | MAYBE BOOLEAN |
| T | ccc22 | s 606(4.1) | ccc28 | s 752 "serious personal injury offence" | `s 752 the offence is a serious personal injury offence` | MAYBE BOOLEAN |
| T | ccc27 | s 745 and 745.01 to 745.6 | ccc8 | ss 231, 235 | `s 231 the kind of homicide offence` | Kind of homicide offence |
| T | ccc2 to ccc13 | offence sections that say "punishable on summary conviction" and state no penalty | ccc29 | s 787(1) | `s 787(1) the general penalty for an offence punishable on summary conviction` | Punishment |
| H | ccc26 | ss 718.2, 718.3, 743.1 | ccc2 to ccc13 | the offence sections | `the punishment the offence charged is liable to (from the offence section itself)` | Punishment |
| H | ccc14 | ss 463 to 465 | ccc2 to ccc13 | the offence sections | `the punishment of the offence attempted, or conspired to be committed` | Punishment |
| H | ccc1 | ss 21 to 24 | ccc2 to ccc13 | the offence sections | `the punishment of the offence a party aided, abetted or attempted` | Punishment |
| H | ccc20 | ss 515, 522 | ccc2 to ccc13 | the offence sections | `whether the offence charged is an indictable offence, and the punishment it is liable to` | Class of offence |
| H | ccc21 | ss 553 to 555 | ccc2 to ccc13 | the offence sections | `the class of the offence charged (the list in s 553 is tested by section number)` | Class of offence |

## 8. What was seen only from headings, and what could not be checked

- Rows marked [H] above: every dependence of a provision on an offence's class or punishment (R2) was assumed from the structure of the Code (each offence section states its own penalty; attempts, conspiracies, parties, sentencing, release and mode of trial look it up). The 124 explicit definition-style cross-references between parts (`as defined in`, `within the meaning of`, `has the same meaning as in`, `has the meaning given by`) were extracted by script (`work/defxref.json`): 36 of them cite section 2 or 3 (the keel), 88 cite another part, and the ones that name a definition in another part are the [T] rows of the table (a few cite a section that only restates a rule, and are not seams).
- Citations that only name an offence by section number are counted in `work/xref.txt` (298 (asking part, cited part) pairs; the heaviest are ccc9 to ccc6 (79), ccc16 to ccc6 (52), ccc18 to ccc17 (48), ccc6 to ccc10 (42), ccc16 to ccc10 (39), ccc7 to ccc2 (36)): they are lists (R1) and need no input.
- The Forms (ccc30, ccc31) were not read: a Form is a coverage row, machinery unless its text states a rule. The related and transitional provisions and the amendments not in force (ccc32) were not read either.
- Which section 2 terms a part really needs was counted by occurrence of the word; common words (`day`, `property`, `justice`, `writing`, `count`) include ordinary uses.

