# NOTES.md -- the keel for the Criminal Code (Canada), R.S.C., 1985, c. C-46 (lines 1-272 of the text)

Status (2026-11-12, keel agent `ccc-k`): written after the modules; every number below was produced by a command run in this session and is repeated in `PROGRESS.md`. The target is the stable `l4` (1.6.110, `main`, e51181d, 2026-11-11) checked against a second stable build (1.6.109): `check.sh` compares the two.
The text is a plain-text rendering, made by a converter script, of the Justice Laws Website consolidation (current to 2026-09-30; last amended 2026-07-18). It is not the official text, and nothing here is claimed verified against the official text. The French version is equally authoritative and is not among the sources; the quotation lines are whole lines of the text, so the French equivalents in parentheses at the end of a defined term appear inside them: they are quoted, not encoded.

## What is encoded and what is not

Lines 1-272 of the text: the banner and title, section 1 (short title), section 2 (85 defined-term rows, three of them shown repealed, plus paragraphs (g) and (h) of "superior court of criminal jurisdiction", shown repealed), section 2.1 (firearms terms), section 2.2 (acting on victim's behalf), section 2.3 (concurrent jurisdiction), section 3 (descriptive cross-references) and section 3.01 (violence in commission of an offence).
Everything in that range has a row in the coverage table below and one disposition. Nothing is `out-of-scope` or `deferred`.
Not in this range, and left to the parts: every other definition section (they are all scoped "In this Part" or "In this section": PLAN.md section 5 lists them with the part that owns each), and every offence, power, duty, procedure and penalty from line 273 on.
The deliverables are `ccc-core.l4` (the shared vocabulary: DECLARE and constants only), `ccc-definitions.l4` and `ccc-definitions-tests.l4` (section 2 and 2.1), `ccc-interpretation.l4` and `ccc-interpretation-tests.l4` (sections 1, 2.2, 2.3, 3, 3.01: split from the definitions because they are rules, not definitions, and for size), `PLAN.md`, `NOTES.md`, `PROGRESS.md`, and `check.sh`, `fetch-main-l4.sh`, `srcrefs.py` (copied from the skill).

## Seat

The seat is a person who is, or may be, accused of an offence under the Criminal Code, asking on facts they can state whether what they did is an offence, what its gravity and penalty are, what defences, rights and procedures apply from arrest through trial, sentence and appeal, and what follows from a conviction (assumed, not ruled: Singapore's Penal Code is the model, per the maintainer's instruction of 2026-11-09, but this is a plain seat layer; no charge-generator contract).
This range holds no question the accused asks directly: it holds the vocabulary every other part reads. So there is no `@export` and no `@desc` here, and no seat layer; the lead's seat layer is built after the merge. Provisions that address only an official (section 2.3, the Attorney General) are encoded for what they mean for the accused: who may prosecute them.

## How to read the answers

### Reading a result: FALSE and NOTHING

Every definition and rule here answers a `MAYBE BOOLEAN` (the one exception: `s 2 Attorney General` answers a `MAYBE (LIST OF Party)`, the list of persons who are the Attorney General in the proceedings).
- `JUST TRUE`: on the facts given, the case is within the term or the rule, on the text's own words.
- `JUST FALSE`, a "no": the text says no in its own words. In this range that means: a definition that says "means" and the case is outside it; a condition the text introduces with "if", "where", "when" or "while" that fails; a flat negative ("does not include railway equipment"; "is not entitled to act"; "does not include an operation authorized by the Security Council as an enforcement action"). Every such branch carries `-- FALSE-kind (the text says no in its own words): "<the quoted words>"`, and a script (`work/verify-quotes.py`) checks that each quoted fragment occurs in the text.
- `NOTHING`, "not covered": the text lists without closing the list ("includes", "without restricting the generality of the foregoing"), leaves a term undefined, is silent, points to something outside the sources (`terrorist activity` is in s 83.01, another part), or limits a grant or prohibition in its own wording (the purposes it is for, "unless a contrary intention appears", "when" or "while" in a limb of an "includes" list) and the case falls outside the limit. Every such branch carries `-- NOTHING-kind (<why>)`, with <why> one of: silent, list not closed, includes, undefined term, points outside the text, limited by its own wording.
- A caller must never turn `NOTHING` into `FALSE`. In particular, "peace officer includes" means a person in a capacity the definition does not list is NOT COVERED, not "not a peace officer"; the same for "public officer", "property", "writing", "weapon", "trustee" and every other "includes" definition.
- Where a definition is written as a list of the kinds of thing it covers, the list is a DECLAREd table: one constructor per member the text names, and one for "a case the list does not name", so that "none of those" is something a caller says and the encoding does not have to guess.
- `REFUSE` is not used (the brief's rule for the stable line, see Finding 6): "not covered" is `NOTHING`, asserted with `EQUALS NOTHING`.

## Coverage table

One row per provision of lines 1-272. Disposition: `encoded` (a rule, definition or table in layer 1, with a test, cited with `@ref` and a `src:` locator); `inert` (only for the three reasons); `fork` (a row whose reading is in the fork register: the register entry, and the rule that encodes the chosen reading, are named); `repealed or blank in this text` (what the text shows). The last column is the number of `#ASSERT`s that name the function in the tests files.

| row | text lines | provision | disposition | encoded by | asserts |
| --- | --- | --- | --- | --- | --- |
| banner | 1-3 | the converter's notice: unofficial text, source, omitted notes | inert (reason 1: not operative) | - | - |
| title | 5-7 | Criminal Code; R.S.C., 1985, c. C-46; An Act respecting the Criminal Law (title and long title) | inert (reason 1: title and long title) | - | - |
| s 1 | 9-11 | Short Title; short title; 1 This Act may be cited as the Criminal Code. | inert (reason 2: machinery, the Act's short title); carried as a quotation | `s 1 the short title` | 1 |
| s 2 lead-in | 13-15 | headings Interpretation, Definitions; the enacting words "2 In this Act," | inert (reason 1: headings and enacting words; "In this Act" is the scope of every definition below) | - | - |
| s 2 "Act" | 16-20 | definition | encoded | `s 2 Act` | 5 |
| s 2 "appearance notice" | 21 | definition | encoded | `s 2 appearance notice` | 4 |
| s 2 "associated personnel" | 22-26 | definition | encoded | `s 2 associated personnel` | 5 |
| s 2 "Attorney General" | 27-32 | definition | fork (F15) | `s 2 Attorney General` | 7 |
| s 2 "audioconference" | 33 | definition | encoded | `s 2 audioconference` | 3 |
| s 2 "bank-note" | 34-37 | definition | encoded | `s 2 bank-note` | 6 |
| s 2 "bodily harm" | 38 | definition | encoded | `s 2 bodily harm` | 4 |
| s 2 "Canadian Forces" | 39 | definition | encoded | `s 2 Canadian Forces` | 2 |
| s 2 "cattle" | 40 | definition | fork (F2) | `s 2 cattle` | 9 |
| s 2 "clerk of the court" | 41 | definition | encoded | `s 2 clerk of the court` | 3 |
| s 2 "common-law partner" | 42 | definition | encoded | `s 2 common-law partner` | 4 |
| s 2 "complainant" | 43 | definition | encoded | `s 2 complainant` | 3 |
| s 2 "counsel" | 44 | definition | encoded | `s 2 counsel` | 3 |
| s 2 "count" | 45 | definition | encoded | `s 2 count` | 4 |
| s 2 "court of appeal" | 46 | definition | encoded | `s 2 court of appeal` | 2 |
| s 2 "court of criminal jurisdiction" | 47-51 | definition | fork (F5, F7) | `s 2 court of criminal jurisdiction` | 11 |
| s 2 "criminal organization" | 52 | definition | encoded (the definition is in s 467.1(1): answer taken as a named input) | `s 2 criminal organization` | 3 |
| s 2 "criminal organization offence" | 53-55 | definition | encoded | `s 2 criminal organization offence` | 13 |
| s 2 "day" | 56 | definition | fork (F1) | `s 2 day` | 13 |
| s 2 "document of title to goods" | 57 | definition | encoded | `s 2 document of title to goods` | 7 |
| s 2 "document of title to lands" | 58 | definition | encoded | `s 2 document of title to lands` | 4 |
| s 2 "dwelling-house" | 59-61 | definition | fork (F2) | `s 2 dwelling-house` | 5 |
| s 2 "environment" | 62-66 | definition | fork (F2) | `s 2 environment` | 6 |
| s 2 "every one, person and owner, and similar expressions" | 67 | definition | fork (F4) | `s 2 every one, person and owner` | 7 |
| s 2 "explosive substance" | 68-71 | definition | encoded | `s 2 explosive substance` | 5 |
| s 2 "feeble-minded person" | 72 | definition | repealed or blank in this text: the text shows "feeble-minded person [Repealed, 1991, c. 43, s. 9]" | `s 2 feeble-minded person as the text shows it` | 1 |
| s 2 "firearm" | 73 | definition | fork (F2) | `s 2 firearm` | 6 |
| s 2 "government or public facility" | 74 | definition | encoded | `s 2 government or public facility` | 9 |
| s 2 "Her Majesty’s Forces" | 75 | definition | fork (F2) | `s 2 Her Majesty’s Forces` | 3 |
| s 2 "highway" | 76 | definition | fork (F2) | `s 2 highway` | 5 |
| s 2 "indictment" | 77-80 | definition | encoded | `s 2 indictment` | 4 |
| s 2 "internationally protected person" | 81-85 | definition | fork (F5) | `s 2 internationally protected person` | 9 |
| s 2 "intimate partner" | 86 | definition | encoded | `s 2 intimate partner` | 7 |
| s 2 "justice" | 87 | definition | fork (F2) | `s 2 justice` | 5 |
| s 2 "justice system participant" | 88-109 | definition | encoded | `s 2 justice system participant` | 21 |
| s 2 "magistrate" | 110 | definition | repealed or blank in this text: the text shows "magistrate [Repealed, R.S., 1985, c. 27 (1st Supp.), s. 2]" | `s 2 magistrate as the text shows it` | 1 |
| s 2 "mental disorder" | 111 | definition | encoded | `s 2 mental disorder` | 2 |
| s 2 "military" | 112 | definition | fork (F3) | `s 2 military` | 3 |
| s 2 "military law" | 113 | definition | encoded | `s 2 military law` | 4 |
| s 2 "motor vehicle" | 114 | definition | encoded | `s 2 motor vehicle` | 4 |
| s 2 "municipality" | 115 | definition | fork (F18) | `s 2 municipality` | 9 |
| s 2 "newly-born child" | 116 | definition | encoded | `s 2 newly-born child` | 5 |
| s 2 "night" | 117 | definition | fork (F1) | `s 2 night` | 12 |
| s 2 "nuclear facility" | 118-120 | definition | encoded | `s 2 nuclear facility` | 3 |
| s 2 "nuclear material" | 121-126 | definition | fork (F16) | `s 2 nuclear material` | 10 |
| s 2 "offence-related property" | 127-130 | definition | encoded | `s 2 offence-related property` | 7 |
| s 2 "offender" | 131 | definition | encoded | `s 2 offender` | 3 |
| s 2 "offensive weapon" | 132 | definition | encoded | `s 2 offensive weapon` | 3 |
| s 2 "organization" | 133-138 | definition | encoded | `s 2 organization` | 13 |
| s 2 "peace officer" | 139-155 | definition | fork (F5) | `s 2 peace officer` | 22 |
| s 2 "prison" | 156 | definition | encoded | `s 2 prison` | 8 |
| s 2 "property" | 157-160 | definition | encoded | `s 2 property` | 9 |
| s 2 "prosecutor" | 161 | definition | fork (F2) | `s 2 prosecutor` | 6 |
| s 2 "provincial court judge" | 162 | definition | fork (F2) | `s 2 provincial court judge` | 5 |
| s 2 "public department" | 163 | definition | encoded | `s 2 public department` | 4 |
| s 2 "public officer" | 164-168 | definition | fork (F5) | `s 2 public officer` | 6 |
| s 2 "public stores" | 169 | definition | encoded | `s 2 public stores` | 3 |
| s 2 "radioactive material" | 170 | definition | encoded | `s 2 radioactive material` | 3 |
| s 2 "railway equipment" | 171-173 | definition | fork (F5) | `s 2 railway equipment` | 4 |
| s 2 "recognizance" | 174 | definition | encoded | `s 2 recognizance` | 3 |
| s 2 "release order" | 175 | definition | encoded | `s 2 release order` | 5 |
| s 2 "representative" | 176 | definition | encoded | `s 2 representative` | 7 |
| s 2 "senior officer" | 177 | definition | fork (F2, F17) | `s 2 senior officer` | 8 |
| s 2 "serious offence" | 178 | definition | encoded (the definition is in another part: answer taken as a named input) | `s 2 serious offence` | 3 |
| s 2 "steal" | 179 | definition | encoded | `s 2 steal` | 3 |
| s 2 "street racing" | 180 | definition | repealed or blank in this text: the text shows "street racing [Repealed, 2018, c. 21, s. 12]" | `s 2 street racing as the text shows it` | 1 |
| s 2 "summons" | 181 | definition | fork (F6) | `s 2 summons` | 7 |
| s 2 "superior court of criminal jurisdiction" | 182-188 | definition | fork (F7, F8) | `s 2 superior court of criminal jurisdiction` | 24 |
| s 2 "paragraphs (g) and (h) of superior court of criminal jurisdiction" | 189 | definition | repealed or blank in this text: the text shows "(g) and (h) [Repealed, 2015, c. 3, s. 44]" | `s 2 superior court of criminal jurisdiction paragraphs (g) and (h) as the text shows them` | 1 |
| s 2 "territorial division" | 190 | definition | encoded | `s 2 territorial division` | 10 |
| s 2 "terrorism offence" | 191-195 | definition | encoded | `s 2 terrorism offence` | 28 |
| s 2 "terrorist activity" | 196 | definition | encoded (the definition is in another part: answer taken as a named input) | `s 2 terrorist activity` | 3 |
| s 2 "terrorist group" | 197 | definition | encoded (the definition is in another part: answer taken as a named input) | `s 2 terrorist group` | 3 |
| s 2 "testamentary instrument" | 198 | definition | encoded | `s 2 testamentary instrument` | 5 |
| s 2 "trustee" | 199 | definition | encoded | `s 2 trustee` | 7 |
| s 2 "undertaking" | 200 | definition | fork (F6) | `s 2 undertaking` | 5 |
| s 2 "unfit to stand trial" | 201-204 | definition | fork (F10) | `s 2 unfit to stand trial` | 6 |
| s 2 "United Nations operation" | 205 | definition | encoded | `s 2 United Nations operation` | 7 |
| s 2 "United Nations personnel" | 206-208 | definition | fork (F5) | `s 2 United Nations personnel` | 4 |
| s 2 "valuable mineral" | 209 | definition | fork (F2) | `s 2 valuable mineral` | 7 |
| s 2 "valuable security" | 210-217 | definition | encoded | `s 2 valuable security` | 7 |
| s 2 "victim" | 218 | definition | fork (F2, F9) | `s 2 victim` | 7 |
| s 2 "videoconference" | 219 | definition | encoded | `s 2 videoconference` | 3 |
| s 2 "weapon" | 220-223 | definition | encoded | `s 2 weapon` | 7 |
| s 2 "wreck" | 224 | definition | encoded | `s 2 wreck` | 6 |
| s 2 "writing" | 225 | definition | encoded | `s 2 writing` | 4 |
| s 2.1 | 226-227 | Further definitions -- firearms: fifteen terms, and authorization, licence and registration certificate used in relation to them, have the meaning given in subsection 84(1) | encoded (the meaning is in s 84(1): answer taken as a named input) | `s 2.1 the term has the meaning it has in subsection 84(1)` | 21 |
| s 2.2(1) | 228-234 | Acting on victim's behalf: individuals (a) to (e) may act for a dead or incapable victim, for ss 606, 672.5, 715.37, 722, 737.1, 745.63 | fork (F11) | `s 2.2(1) the individual may act on the victim’s behalf` | 17 |
| s 2.2(2) | 235-236 | Exception: an accused, a person found guilty, or found NCR or unfit, is not entitled to act | fork (F11) | `s 2.2(2) the individual is not entitled to act on the victim’s behalf` | 6 |
| s 2.2 (1)+(2) | 229-236 | (a composition of the two functions, not a separate provision) | encoded | `s 2.2 the individual may act on the victim’s behalf, subject to subsection (2)` | 7 |
| s 2.3(1)(a)-(f) | 237-244 | Concurrent jurisdiction: the proceedings for the purposes of paragraph (a) of the definition Attorney General are (a) to (f) | fork (F12) | `s 2.3(1) the proceedings are referred to in subsection 2.3(1)` | 56 |
| s 2.3(2) lead-in | 245-246 | For greater certainty: the Attorney General of Canada may exercise the Attorney General's powers for the offences in (1) and under other Acts of Parliament | encoded | `s 2.3(2) the Attorney General of Canada may exercise the powers and perform the duties and functions of the Attorney General` | 5 |
| s 2.3(2)(a)-(f) | 247-252 | those powers include commencing and conducting (a) conspiracy etc., (b) criminal organization offence, (c) ss 354, 355.2, 355.4, 462.31, (d) breach of court order, (e) failure to comply with release conditions, (f) ancillary proceedings | encoded | `s 2.3(2) those powers include the power to commence and to conduct the proceeding` | 7 |
| s 2.3(3) | 253-254 | For greater certainty: the Director of Public Prosecutions for the Canada Elections Act | encoded | `s 2.3(3) the Director of Public Prosecutions exercises the powers and performs the duties and functions of the Attorney General of Canada` | 2 |
| s 3 | 255-256 | Descriptive cross-references: words in parenthesis after a cross-reference form no part of the provision | fork (F13) | `s 3 the words in parenthesis form no part of the provision and are deemed inserted for convenience of reference only` | 5 |
| s 3.01(1)(a)-(d) | 257-262 | Violence in commission of offence: a reference to an offence of violence includes (a) sexual offences, (b) s 264, (c) s 279.01, (d) s 279.011 | fork (F14) | `s 3.01(1) the offence counts as an offence in the commission of which violence is used, threatened or attempted against any person or class of persons` | 9 |
| s 3.01(2)(a)-(f) | 263-271 | the provisions (a) 109(1), (b) 110(1) and (2.1), (b.1) 263.1(1), (c) 515(3), (4.1), (4.3), (6), (d) 718.3(8), (e) 726.21, (f) 810.03(4) | fork (F14) | `s 3.01(2) subsection (1) applies with respect to the provision` | 23 |
| blank | 272 | blank line before Part I (line 273) | inert (reason 1: not text) | - | - |

Blank lines (lines 4, 8, 12, 272 and the like) are not provisions and have no row. Where a term has two functions (a table type and the function over it), the type is a DECLARE and is not listed; the function is.
Where the definition of a term is in another part (criminal organization, serious offence, terrorist activity, terrorist group, and the meanings s 2.1 takes from s 84(1)), the keel's function is a pass-through of a named input, so that the question "what does the definition say" is answered by the part that owns it (PLAN.md section 7, rows marked keel).

## Fork register

A fork is a place where the text can be read two or more ways with different outcomes. Each entry: the provision and function, the readings and the text that licenses each, the reading taken. The taken reading is the status quo for a lawyer to overrule.

- **F1. `day` and `night` share their end-points** (`s 2 day`, `s 2 night`; lines 56, 117). "day means the period between six o’clock in the forenoon and nine o’clock in the afternoon of the same day"; "night means the period between nine o’clock in the afternoon and six o’clock in the forenoon of the following day". At exactly 06:00 and 21:00 the readings are: in day; in night; in both; in neither. The text does not choose. Taken: NOTHING at those two instants (NOTHING-kind (silent)); JUST TRUE inside, JUST FALSE outside. Time is taken as minutes after midnight (the core may not import `time`); fractions of a minute are allowed. Tested on both sides of both end-points.
- **F2. "means ... and includes ..."** (`s 2 cattle`, `dwelling-house`, `environment`, `firearm`, `Her Majesty’s Forces`, `highway`, `justice`, `prosecutor`, `provincial court judge`, `senior officer`, `valuable mineral`, `victim`). Reading A: "means" closes the definition, and the "includes" part is an extension that is itself closed, so anything not within the means part or the listed extension is outside (JUST FALSE). Reading B: "includes" keeps the list open (NOTHING). Licence: "means" (A); "includes" (B). Taken: A. Where the text adds "without restricting the generality of the foregoing" (`weapon`, `trustee`) the list is open and the answer is NOTHING: that is the text's own word, not a fork.
- **F3. "military shall be construed as relating to all or any of the Canadian Forces"** (`s 2 military`; line 112). Not a "means". Reading A: a rule of construction that says what the word relates to and not that it relates to nothing else (NOTHING for anything else). Reading B: a closed definition (JUST FALSE). Taken: A.
- **F4. "every one, person and owner, and similar expressions, include Her Majesty and an organization"** (`s 2 every one, person and owner`; line 67). For an individual, reading A: the provision is silent on whether they are within the expressions (NOTHING); reading B: an individual is obviously within "every one" (JUST TRUE). For an expression not similar to the three: NOTHING (undefined term). Taken: A.
- **F5. "when", "while" and "whenever" limbs.** In an "includes" list (`s 2 peace officer` (c.1), (d), (e), (f); `s 2 public officer` (d)) a person in the named office but outside the stated situation (a customs officer not performing a customs duty; a pilot not in flight) is NOT COVERED, because the list is open. In a "means" list (`s 2 court of criminal jurisdiction` (a) "when presided over by a superior court judge"; `railway equipment` (b); `United Nations personnel` (b); `internationally protected person` (a) and (b)) the same person is JUST FALSE, because "means" is closed. Reading B for the "includes" lists: the "when"/"while" condition failing is the text's no (the periods and "where" ruling of 2026-11-05, (b) and (c): "when" counts as "where"), so JUST FALSE for the limb, and since the list is open the overall answer would still be NOTHING; the only difference is the limb's own sub-answer. Taken: as stated.
- **F6. "unless a contrary intention appears"** (`s 2 summons`, `s 2 undertaking`; lines 181, 200). When a contrary intention appears the definition does not apply and the text does not say what the word then means. Reading A: NOTHING. Reading B: JUST FALSE ("an 'unless' once it is met" is one of the six questions the maintainer ruled are decided case by case, 2026-11-05). Taken: A.
- **F7. A court named in one province but offered for another** (`s 2 court of criminal jurisdiction` (a.1) and (c), `s 2 superior court of criminal jurisdiction` (a) to (f)). The Court of Quebec is a court of criminal jurisdiction "in the Province of Quebec"; asked about Ontario it is outside. Reading A: "means" closes the list by province, so JUST FALSE. Reading B: the province is a scope limit with no "only", so NOTHING (ruling (c) of 2026-11-05). Taken: A.
- **F8. Paragraph (b) of "superior court of criminal jurisdiction" does not name the Court of Appeal of Quebec** (line 184: "(b) in the Province of Quebec, the Superior Court"), though (a), (c) and (d) name the Court of Appeal for their provinces. Reading A (taken): the text as it stands: in Quebec only the Superior Court is a superior court of criminal jurisdiction, so the Quebec Court of Appeal is JUST FALSE. Reading B: an omission to be read in. This is also Finding 2.
- **F9. The extension of "victim" for sections 672.5, 722 and 745.63** (`s 2 victim`; line 218). A person harmed by an offence against another person is a victim "for the purposes of sections 672.5, 722 and 745.63". For any other purpose, reading A: the grant is limited by its own wording, so NOTHING; reading B: "means" closes the term, so JUST FALSE. Taken: A. (Section 2.2(1) names six sections, including 606, 715.37 and 737.1, which `s 2 victim` does not extend to: that is the text.)
- **F10. "unfit to stand trial ... and, in particular, unable on account of mental disorder to (a), (b) or (c)"** (`s 2 unfit to stand trial`; lines 201-204). Reading A (taken): (a), (b) and (c) are cases that suffice. Reading B: they merely illustrate the general inability (so each also implies it). The two give the same answer on consistent facts and differ only if a caller says "unable to communicate with counsel" but not "unable to conduct a defence".
- **F11. Section 2.2** (`s 2.2(1)`, `s 2.2(2)`). (i) If the victim is neither dead nor incapable, "if the victim is dead or incapable of acting on their own behalf" fails: A (taken) JUST FALSE, B NOTHING. (ii) An individual with none of the five relations: A (taken) NOTHING (the list does not say "only"), B JUST FALSE. (iii) A section outside the six: NOTHING (a limited grant: ruling (c) of 2026-11-05). (iv) Subsection (2), "is not entitled to act on a victim’s behalf if the individual is an accused ...": the three conditions failing, A (taken) JUST FALSE for "barred", B NOTHING. (v) (1) and (2) are separate functions; the composition `s 2.2 ... subject to subsection (2)` says JUST FALSE whenever (2) says JUST TRUE.
- **F12. Section 2.3(1) says the proceedings "are" (a) to (f)**, without "only" (`s 2.3(1)`; line 238). Reading A (taken): "are" is definitional and closes the list: none of the six is JUST FALSE. Reading B: NOTHING. Where limb (a) turns on whether an offence is a terrorism offence, the answer of `s 2 terrorism offence` is an input and a NOTHING from it gives NOTHING here (NOTHING-kind (points outside the text)).
- **F13. Section 3, "Where, in any provision of this Act, a reference ... is followed by words in parenthesis ..."** (`s 3`; line 256). When any of the four limbs fails, A (taken) JUST FALSE (the periods and "where" ruling of 2026-11-05, (b): a "where" condition failing gives the text's no); B NOTHING.
- **F14. Section 3.01** (`s 3.01(1)`, `s 3.01(2)`). (i) A provision not in the list of (2): A (taken) NOTHING (a scope limit with no "only": ruling (c) of 2026-11-05); B JUST FALSE. (ii) In a listed provision, an offence that is none of (a) to (d): NOTHING ("includes a reference to any of the following offences"): not a fork.
- **F15. `s 2 Attorney General`** (lines 27-32). The answer is the list of persons who are the Attorney General; in a proceeding referred to in 2.3(1) both the Attorney General of Canada and the province's are named (paragraph (a): "the Attorney General of Canada or the Attorney General or Solicitor General of the province"), so the list holds both (concurrent). Reading B: only the Attorney General of Canada. The input "referred to in subsection 2.3(1)" is a BOOLEAN, so the caller must have decided; a NOTHING from `s 2.3(1)` must not be passed as FALSE. If none of paragraphs (a), (b), (c) speaks to the proceedings: NOTHING (silent).
- **F16. `nuclear material` (c) and (d) overlap at 0.72%** (`s 2 nuclear material`; lines 123-125). (c) is "greater than 0.72%": a ratio of exactly 0.72% is outside (c) (JUST FALSE for that constructor). Uranium "with an isotopic concentration equal to that occurring in nature" is (d), which the caller must choose as the constructor: the encoding does not guess which the substance is.
- **F17. `senior officer`** (line 177): "means a representative who ... and, in the case of a body corporate, includes a director, its chief executive officer and its chief financial officer". Reading A (taken): the director, CEO and CFO of a body corporate are senior officers whether or not they play the stated role. Reading B: they must still be representatives who play the role. Also the answer of `s 2 representative` is a `MAYBE BOOLEAN` input.
- **F18. `municipality`** (line 115): "includes the corporation of a city, town, ... the inhabitants of which are incorporated or are entitled to hold property collectively for a public purpose". A listed kind of division whose inhabitants are neither: A (taken) NOTHING (outside this limb of an open list); B JUST FALSE.

## Marginal readings for a lawyer

The two readings left open for a lawyer, applied as the status quo (the rule of 2026-10-29; assumed, not ruled): (a) a failed "if" counts as the text's no, clause by clause, within the provision that holds the "if", and flat negatives count as the text saying no; (b) a prohibition or grant limited by its own wording does not.

Branches that rest on reading (a) (the other reading: NOTHING, because "if A then B" does not itself say "if not A then not B"):
- `s 2.2(1)`: the victim is neither dead nor incapable: JUST FALSE.
- `s 2.2(2)`: none of the three conditions: JUST FALSE for "barred".
- `s 2.3(1)`: none of (a) to (f): JUST FALSE.
- `s 3`: any of the four limbs failing: JUST FALSE.
- `s 2 court of criminal jurisdiction` (a): sessions not presided over by a superior court judge ("when presided over"): JUST FALSE.
- `s 2 prosecutor`: the person who institutes proceedings where the Attorney General intervenes ("where the Attorney General does not intervene"): JUST FALSE.
- `s 2 railway equipment` (b): adaptations not in use ("while ... are in use"): JUST FALSE.
- `s 2 United Nations personnel` (b): not present in an official capacity in the area: JUST FALSE.
- `s 2 internationally protected person` (a) and (b): in the state where the office is held; not accompanying: JUST FALSE.
- `s 2 dwelling-house` (b): a mobile unit not being used as a residence: JUST FALSE.
- `s 2 United Nations operation`: neither the peace-and-security purpose nor a declared exceptional risk ("if the operation is for the purpose ... or if the Security Council ... has declared"): JUST FALSE.
- `s 2 common-law partner`: cohabiting for less than a year ("having so cohabited for a period of at least one year"): JUST FALSE (a period the text fixes in its own words: ruling (a) of 2026-11-05).
- `s 2 valuable mineral`: a mineral under $100 per kilogram: JUST FALSE; `s 2 newly-born child`: age one or more: JUST FALSE.
- `s 2 appearance notice`, `s 2 recognizance`, `s 2 release order`: not in the stated Form: JUST FALSE ("means a notice in Form 9").

Branches that rest on reading (b) (a grant or prohibition limited by its own wording and the case outside the limit: NOTHING; the other reading: JUST FALSE):
- `s 2.2(1)`: a purpose that is not one of the six sections; an individual with none of the five relations.
- `s 2.3(2)`, `s 2.3(3)`: an offence outside those the power is stated for.
- `s 3.01(1)`, `s 3.01(2)`: a provision not in the list.
- `s 2 victim`: harm from an offence against another person, for a purpose outside the three sections.
- `s 2 summons`, `s 2 undertaking`: a contrary intention appears.
- `s 2 peace officer`, `s 2 public officer`: a "when" or "while" limb not met.
- `s 2 military`; `s 2 every one, person and owner` (an individual); `s 2 municipality`.
- `s 2.1`: authorization, licence or registration certificate used in relation to something other than the fifteen terms.

## Rulings carried, word for word

Each ruling is recorded again, word for word, in the NOTES.md of each row that carries that rule's `NOTHING-kind` tags: in its fork register where it has one, and in a section of its own where it has none. This row has a fork register, so they are recorded here, copied by script from the brief.

- **E1** (bench `commons-negation-1030`; should a legal effect be one definition gathered from every section that gives it?): option B, as guidance for gathering a legal effect's routes by hand only, with no pilot run; option A (gathering by bare name) is withdrawn as a direction for the language, not deferred; option C (per-section answers) applies everywhere else; the Magna Carta pilot in the printed recommendation (chapters 2, 3, 4, 5, 37, 43, 46 and 53, with a blind second reader) is not to be run. The maintainer's lean, verbatim: "B but generally uncomfortable with this much magic because it takes the language from unopinionated to opinionated in ways that are hard to teach an l4 novice." the maintainer's note, verbatim: "Fundamentally I feel like we are trying to make the language do work that the human l4 drafter should do. Too much magic. Can’t we just decline to be this opinionated and say the programmer needs to do this thinking?" Marked 2026-11-03T23:19:02.812Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
- **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. The maintainer's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." the maintainer's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
- **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. The maintainer's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.
- **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. The maintainer approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.
- **Questions with no convention: decide case by case (the maintainer, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. The maintainer's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with the coordinator where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

Where each ruling bites in this range: N2 (a flat negative counts as the text's no): `s 2 motor vehicle` ("does not include railway equipment"), `s 2.2(2)`, `s 2 United Nations operation` ("It does not include"). Periods, "where" and scope limits: (a) `s 2 common-law partner`, `s 2 newly-born child`, `s 2 valuable mineral`; (b) `s 2.2(1)`, `s 3`, the "when" and "while" limbs; (c) `s 3.01(2)`, `s 2.2(1)` (purposes). Delegated definitions: (a) none in this range hands a definition to a list in the way the ruling describes; the pointers to s 467.1(1), s 83.01(1) and s 84(1) are not lists. Case by case: "an 'unless' or 'except' once it is met" (F6); "(other than X)" is not met in this range except "other than this Act or the Canada Elections Act" in `s 2.3(2)` and `s 2 Attorney General` (b)(ii), which are conditions of fact asked as BOOLEAN inputs.

## Jural relations

One row per provision that creates a relation. Hohfeld's correlatives: right and duty; privilege and no-right; power and liability; immunity and disability. A provision that creates none (a definition, a counting rule, a rule of reading) is listed once as `none`.

| provision | holder (right, privilege, power or immunity) | bearer (duty, no-right, liability or disability) | section | L4 rule |
| --- | --- | --- | --- | --- |
| the banner, title, headings | none | none | -- | -- |
| the short title | none | none | s 1 | `s 1 the short title` |
| every definition of section 2 (85 rows, listed in the coverage table), including the repealed ones | none | none | s 2 | the `s 2 <term>` functions |
| the firearms terms | none | none | s 2.1 | `s 2.1 the term has the meaning it has in subsection 84(1)` |
| who may act for a dead or incapable victim | power: the victim's spouse or common-law partner (or the one at the time of death), a relative or dependant, a person with custody of or responsible for the victim, a person with custody of or responsible for a dependant of the victim: to act on the victim's behalf for ss 606, 672.5, 715.37, 722, 737.1 and 745.63 | liability: the victim (their entitlement is exercised by another), and the court or justice that must receive that exercise | s 2.2(1) | `s 2.2(1) the individual may act on the victim’s behalf` |
| who may not | immunity: the victim (no one who is the accused, or is found guilty, not criminally responsible or unfit, in respect of the offence can act for them) | disability: the accused, the person found guilty, the person found not criminally responsible or unfit | s 2.2(2) | `s 2.2(2) the individual is not entitled to act on the victim’s behalf` |
| the two together | (composition of the two rows above) | (composition) | s 2.2 | `s 2.2 the individual may act on the victim’s behalf, subject to subsection (2)` |
| which proceedings the Attorney General of Canada may also take | none (it defines "the proceedings for the purposes of paragraph (a) of the definition Attorney General"; the relation arises in s 2 "Attorney General" and s 2.3(2)) | none | s 2.3(1) | `s 2.3(1) the proceedings are referred to in subsection 2.3(1)` |
| the Attorney General of Canada's power to prosecute | power: the Attorney General of Canada and their lawful deputy: to exercise all the Attorney General's powers and perform the duties and functions for the offences in (1) and the offences under other Acts of Parliament | liability: the person prosecuted (they may be prosecuted by the Attorney General of Canada as well as the province's) | s 2.3(2) | `s 2.3(2) the Attorney General of Canada may exercise the powers and perform the duties and functions of the Attorney General` |
| the kinds of proceeding that power includes | power: the Attorney General of Canada: to commence and to conduct (a) to (f) | liability: the person who conspires, attempts, is an accessory or counsels; is charged with a criminal organization offence, a laundering or possession offence; breaches a court order or release condition; is the subject of ancillary proceedings | s 2.3(2)(a)-(f) | `s 2.3(2) those powers include the power to commence and to conduct the proceeding` |
| the Director of Public Prosecutions for the Canada Elections Act | power: the Director of Public Prosecutions: to exercise the powers and perform the duties and functions of the Attorney General of Canada, for an offence under the Canada Elections Act | liability: the person prosecuted under the Canada Elections Act | s 2.3(3) | `s 2.3(3) the Director of Public Prosecutions exercises the powers and performs the duties and functions of the Attorney General of Canada` |
| descriptive cross-references | none (a rule of reading: the words in parenthesis are no part of the provision) | none | s 3 | `s 3 the words in parenthesis form no part of the provision and are deemed inserted for convenience of reference only` |
| violence in the commission of an offence | none (it extends a phrase in the listed provisions; the relations are those provisions' own: for example the reverse onus of s 515(6) and the prohibition orders of s 109, which the parts that own them encode) | none | s 3.01(1), (2) | `s 3.01(1) ...`, `s 3.01(2) ...` |

## Findings

### What the Act turns out to say (numbered)

1. "Hybrid" and "dual procedure" occur nowhere in the text (0 hits), so the core's `Class of offence` words its third value from the Act's own phrase ("is guilty of (a) an indictable offence ... or (b) an offence punishable on summary conviction"). "Two years less a day" occurs 30 times, which is why the core's `Length of time` keeps years, months, days and a "less a day" flag instead of a day count. The maxima named in the text are two years (83 times), five years (76), ten years (63) and fourteen years (47; four more are written "fourteen years").
2. Paragraph (b) of "superior court of criminal jurisdiction" names only the Superior Court of Quebec, not the Court of Appeal of Quebec, though (a), (c) and (d) name the Court of Appeal for their provinces (fork F8). Encoded as the text has it.
3. "day" and "night" are both defined by "between" the same two instants (fork F1): at 06:00 and 21:00 the text does not say which applies.
4. "justice system participant" (b)(vi) takes in a peace officer "within the meaning of any of paragraphs (b), (c), (d), (e) and (g)" of the definition of peace officer, so a mayor, sheriff or justice of the peace (paragraph (a)), a designated officer under the cross-border Act ((c.1)), an immigration officer ((d.1)) and a pilot in command ((f)) are not named in (vi) (they would be within (b) generally only if they play a role in the administration of criminal justice). Encoded as constructors; the caller picks the one that fits.
5. The section 2 text still says "Court of Queen’s Bench" for four provinces ("(d) in the Provinces of New Brunswick, Manitoba, Saskatchewan and Alberta, the Court of Appeal or the Court of Queen’s Bench"); the table uses the text's spelling.
6. Section 2.2(1) is "for the purposes of sections 606, 672.5, 715.37, 722, 737.1 and 745.63" (six sections) while "victim" in section 2 is extended "for the purposes of sections 672.5, 722 and 745.63" (three): fork F9.
7. Section 2.3(2)(c) cites "section 354, 355.2, 355.4 or 462.31"; section 2.3(1)(a) lists 15 sections and five subsections of section 7, then "any terrorism offence"; (b) names "266 to 269" and "271 to 273" as ranges. Section numbers are decimals and sort in the Code's order (83.18 to 83.23 takes in 83.181 ... 83.231's predecessors up to 83.23 and nothing after; 266 to 269 takes in 268.1 and 269 but not 269.01 or 269.1; tested at both ends of each range), which is why the core's `Provision of the Code` carries `section` as a NUMBER.
8. "feeble-minded person", "magistrate" and "street racing" are shown repealed ("[Repealed, 1991, c. 43, s. 9]", "[Repealed, R.S., 1985, c. 27 (1st Supp.), s. 2]", "[Repealed, 2018, c. 21, s. 12]"), and "(g) and (h)" of "superior court of criminal jurisdiction" are shown repealed ("[Repealed, 2015, c. 3, s. 44]"). Each is carried as a string constant that quotes what the text shows.
9. Only section 2 and section 2.1 are Act-wide ("In this Act"); every other definition section in the text is "In this Part", "In this section" or "In this section and in sections ...", which is why the parts encode their own (PLAN.md section 5).

### What the stable binary does not accept

Measured on 2026-11-12 on 1.6.110 (main, e51181d) and 1.6.109 (main, 4c887e0), each probe a small file run with `l4 run`:
- `DECLARE Applicant` with no body (an opaque type): rejected, `parse/unexpected-GIVEN` at the next declaration.
- `TYPICALLY 18` on a record field: rejected, `parse/unexpected-number` (`unexpected 18`).
- A section `GIVEN` followed by two rules that read it: rejected, `check/unknown-identifier` for the second (`I could not find a definition for the identifier r`): the `GIVEN` is the signature of the next rule only. This module uses none.
- The same name defined in two modules that are imported together, and used: rejected, `check/ambiguous-identifier` (`There are multiple definitions for the identifier foo`). The same error for a constructor name that two enumerations of one module share, when it is used. Every constructor in this range is unique module-wide, and none repeats a core constructor.
- `IF a THEN x` followed on the next lines by `ELSE IF b THEN y` at the same indentation: rejected, `parse/indentation` (`incorrect indentation (got 10, should be greater than 10)`). Written with `BRANCH` or with the nested `ELSE IF` indented under the `ELSE`.
- A type named `A` (as in `DECLARE A IS ONE OF`): rejected, `unexpected A` (the article is a keyword).
- Accepted, contrary to the brief and to the skill's dialect page (which measured 1.6.98): `REFUSE "reason"` (`Checking succeeded.`), `#ASSERT REFUSED` (the assertion machinery exists: an expression that answers a value gives `assertion failed: expected a refusal, but the expression produced a value`) and `YMD 2025 1 15` (evaluates to `DATE OF 15, 1, 2025`), on both 1.6.109 and 1.6.110. None is used here, because the brief and the Commons guide set the rule for the stable line (no `REFUSE`, `Date day month year`), and the guide's target is the build the VS Code extension ships. The lead may want to re-measure `dialects.md`.
- What was not probed and is therefore not claimed: `NOT a AND b` without brackets (every `NOT` in this range is bracketed), `WAIT UNTIL`, `@export` placement.

### Limits of this work

- Expected values in the tests are written by hand from the text before each run, but by the same agent that wrote the functions. The independent test pass the skill recommends (a fresh session that decides the answers before reading the encoding) was not run: no subagent was available.
- The tests exercise each branch and each threshold of each function. They do not test that a caller composes the functions correctly across parts: that is the merge's job.
- The `@ref` locators and quotations are checked by `srcrefs.py check --refs` (and `--strict`); the FALSE-kind and NOTHING-kind quotations by `work/verify-quotes.py`. Neither checks that an encoding means what the text says: that is for a reviewer.

## What `check.sh` printed

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.109 (main, 4c887e0, 2026-11-04)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
ccc-core.l4                                    0         0       0        0         0 |      0         0       0        0  same
ccc-definitions-tests.l4                       0       557       0        0         0 |      0       557       0        0  same
ccc-definitions.l4                             0         0       0        0         0 |      0         0       0        0  same
ccc-interpretation-tests.l4                    0       134       0        0         0 |      0       134       0        0  same
ccc-interpretation.l4                          0         0       0        0         0 |      0         0       0        0  same
TOTAL (5 modules)                              0       691       0        0           |      0       691       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
check.sh exit status: 0
```

Read with it: the exit status of `check.sh` was 0 (captured without a pipe); the assertions written (`grep -c '^#ASSERT'`: 557 in `ccc-definitions-tests.l4` and 134 in `ccc-interpretation-tests.l4`, 691 in all) equal the assertions satisfied (691); no module is expected to fail; `DiagnosticSeverity_Warning` was counted over every module on both builds and is 0 (`check.sh` counts errors only, so this was a separate count); `srcrefs.py check --refs` over all five modules, and `--strict` over the three non-test modules, report 0 problems (255 `src:` lines, 97 runs, 151 locators); every FALSE-kind and NOTHING-kind quotation was found in the text by `work/verify-quotes.py`, and every JUST FALSE and NOTHING branch carries its kind comment (`work/lint-kinds.py`: 80 and 55, 0 problems).
The harness can fail: a control file with one deliberately wrong `#ASSERT` beside a right one was run through the same counting and gave `errors=1 satisfied=1 failed=1` (the file was deleted afterwards; it is not in the deposit).

## Open questions for a domain expert

1. Does the Quebec Court of Appeal belong in paragraph (b) of "superior court of criminal jurisdiction" (F8)?
2. Are the end-points of "day" and "night" in the one, the other, both or neither (F1)?
3. Is "means ... and includes ..." closed (F2)? This decides about a dozen definitions.
4. Do the readings in "Marginal readings for a lawyer" hold, in particular that a failed "if", "where" or "when" is the text's no?
5. Is an individual within "every one, person and owner" for the purposes of that definition, or is it silent about them (F4)? The encoding answers NOTHING for an individual, the reading a lawyer is most likely to overrule.
6. For `s 2 Attorney General`, is the Attorney General of Canada the Attorney General alongside the province's in every proceeding referred to in section 2.3(1) (F15)?

## Copied modules

None. This row copies no module from another encoding, and no existing encoding of any Act was read. The files `check.sh`, `fetch-main-l4.sh` and `srcrefs.py` were provided in the deposit by the lead (from the `encoding-a-subject` skill) and are unchanged.

## Files

`ccc-core.l4`, `ccc-definitions.l4`, `ccc-definitions-tests.l4`, `ccc-interpretation.l4`, `ccc-interpretation-tests.l4`, `PLAN.md`, `NOTES.md`, `PROGRESS.md`; scripts in `../../work/` (outside the deposit: `build.py` and `mk.sh` expand the `@@Q n-m label@@` placeholders of the templates in `work/src/` into verbatim `-- src:` quotation lines and `@ref` lines, so no quotation was retyped).
