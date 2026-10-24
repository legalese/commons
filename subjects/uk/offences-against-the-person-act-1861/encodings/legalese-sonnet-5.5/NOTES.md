# Offences against the Person Act 1861 -- encoding `legalese-sonnet-5.5`

Status: **draft**, 2026-10-22.
Written by a single Claude Sonnet 5.5 agent working alone from the brief in `BRIEF.md` (run `porridge-uk-oapa-b`).
No domain expert has read this encoding against the text.
Nothing here is legal advice.

**The source is a converter rendering, not the official text.**
`ukpga-Vict-24-25-100.txt` is a plain-text rendering, made by a converter script, of the revised text of the Act at the point in time 2026-04-29, taken from legislation.gov.uk.
It is not the official text and it is not marked up.
This encoding has not been verified against the official text, and nothing in this folder claims it has.
Its sha256 is `63920ce06519ca15ea7160bc31f8446a7076b6465440028cfb16b05de019f5ee`.
Where the rendering shows ". . ." the words have been omitted; the deposit does not say why, so this file says "omitted" and never "repealed" about those gaps.

All the numbers in this file are a point-in-time record of one build.
They were produced by `l4` 1.6.98 (the "main" dialect), `l4`, sha256 `82ea44addf093ea4dd84c4e4416184920857ca9c762c5b31feed20541c20263e`, with `JL4_LIBRARY_PATH` unset.

## Seat

**The seat is a person who may be accused of an offence under the Act (the person suspected or charged), asking what the Act makes of what they did or are alleged to have done, and the most that can follow.**
Why this seat: the Act's operative provisions are almost all prohibitions followed by a penalty, and the rest are powers exercised over that person (where they may be tried, what two justices may order, a search warrant) or protections they hold (the certificate of dismissal, the bar to further proceedings, the provisos against a second punishment, the exceptions to bigamy).
The individual to whom the law is applied is therefore the accused.
There is never a seat for an official: the court, the jury, the justices, the prosecutor and the person executing a warrant appear only as what they may do to the accused or must give the accused.
No further seat is built.
A seat for the party aggrieved (who may complain under section 42 and is barred by section 45) would be a natural second one; it is not written, and sections 42 to 45 are stated from the accused’s side only.

The seat layer is `oapa-seat.l4` (55 `@export` questions, listed below) and its worked cases are `oapa-cases-seat.l4`.
It IMPORTs the layer-1 modules and calls their rules; it restates none.
Each question takes plain inputs, one per fact the person can state, each with an `@desc` worded as the person would be asked.
The records the layer-1 rules expect are built inside each question, in its `WHERE`, from those answers.
Where a rule never reads a record field, that field gets a fixed placeholder with a comment; they are listed under "Placeholders" below.
An offence question returns a record `What the Act makes of it`: whether the facts make out the offence, what the Act calls it, how the Act says it is tried, and the most the Act states can follow.
Wherever a term is hidden by ". . ." in the deposited text, the answer says "for a term the text does not state"; it never fills a gap.

## What is encoded and what is not

**Encoded (layer 1).**
Every operative provision of the deposited text that creates an offence, a penalty, a power over the accused or a protection of the accused: sections 4, 5, 9, 10, 16-18, 20-40, 42, 44, 45, 47, 57-60, 64, 65, 68 and 78, 40 sections in all.
Each offence is a fact record named in the Act’s own words and a rule over it, with three further statements per offence: what the text calls it (felony, misdemeanor, "an offence", or nothing), how the text says it is tried (only where it says), and the sentences it states.
`oapa-table.l4` gathers the three statements for the 32 listed offences so that section 64 (which asks which offences are felonies) and section 68 (which asks which are indictable) do not list them again.

**Not encoded, and said so in the module that would hold it.**
- Murder and manslaughter themselves: sections 1 and 2 are rows of dots and section 5 gives only a penalty.
  The two questions "does this text tell me whether what I did is a murder / a manslaughter" return `the deposited text does not say`.
- Assault, battery, wounding, grievous bodily harm, actual bodily harm, "maliciously", "wilfully" and "unlawfully" are not defined in the text; each is a fact the person states.
- The Abortion Act 1967 and any other statute that makes an act lawful or unlawful.
  "Unlawfully" is a stated fact, as everywhere in the Act.
- The "powers and protections" that section 65 borrows from 23 & 24 Vict. c. 139, and the manner of a trial abroad "before the passing of this Act" that the proviso to section 9 preserves.
  Neither is in the inputs.
- Section 76 (procedure for summary offences, by reference to two other Acts): inert.
- Every penalty term hidden by ". . .": recorded as `for a term the text does not state`, never filled from memory or from a later Act.
- Pleading, venue other than ss 9, 10, 68, prosecution consent, evidence and defences outside the Act’s own words.

## Files, in reading order

Layer 1 (the law): `oapa-nouns.l4`, `oapa-homicide.l4`, `oapa-threats.l4`, `oapa-danger-bodily-harm.l4`, `oapa-danger-neglect-explosives.l4`, `oapa-danger-railways-vehicles.l4`, `oapa-assaults.l4`, `oapa-bigamy.l4`, `oapa-abortion-birth.l4`, `oapa-gunpowder.l4`, `oapa-other.l4`, `oapa-table.l4`.
Tests: one `oapa-tests-<module>.l4` for each layer-1 module except `oapa-nouns.l4` (11 files).
Layer 2 (the seat): `oapa-seat.l4`, `oapa-cases-seat.l4`.
Tools and records: `check.sh`, `srcrefs.py`, `PROGRESS.md`, `NOTES.md`, `encoding.json`, `SOURCE-LICENSE.md`, `BRIEF.md` (a copy of the brief).
All `.l4` files sit flat in this folder.
Every layer-1 rule that rests on a line of the text carries an `@ref` with `src:` locators, and the quote lines above it were copied from the raw text by `srcrefs.py quote` through a small wrapper that is not deposited.

## Coverage

The table below has one row for each section number from 1 to 79.
It was built at the end of the run, by a script, from the rows of the deposited text.
During the run the census it rests on (which sections have text, which are rows of dots, which numbers are absent) was kept in `PROGRESS.md`, and this table was not kept on disk section by section; that is how it was done, not how the brief asked.
Where a number has no row in the text (3, 8, 12-15, 51, 55, 62, 63, 67, 75), the disposition is `not applicable`, and the reason is that the text has no row for it.
There are no Schedules or tables in the text.
The title, chapter number, long title and date of enactment (lines 1-4 of the raw text) and the group headings (Homicide, Letters threatening to murder, Child-stealing, and so on) are not provisions; the group headings are carried as `§` headings.

Counts: **40 encoded, 1 inert, 26 repealed or blank in this text, 12 not applicable; 79 in all.**

| No. | Heading as the text writes it | Disposition | What the text shows / where it is encoded |
| --- | --- | --- | --- |
| 1 | (a row of dots) | repealed or blank in this text | The text shows the number and a row of dots (src:6). Carried as a stub string in `oapa-homicide.l4`. |
| 2 | (a row of dots) | repealed or blank in this text | The text shows the number and a row of dots (src:7). Carried as a stub string in `oapa-homicide.l4`. |
| 3 | (no row in this text) | not applicable | The deposited text has no row with this number; there is nothing to encode. |
| 4 | Conspiring or soliciting to commit murder. | encoded | Layer 1: `oapa-homicide.l4`, `s 4: soliciting or proposing a murder`. Source lines src:8-9. |
| 5 | Manslaughter. | encoded | Layer 1: `oapa-homicide.l4`, `s 5: the sentences the text states for a conviction of manslaughter` (the penalty only). Source lines src:10-11. |
| 6 | (a row of dots) | repealed or blank in this text | The text shows the number and a row of dots (src:12). Carried as a stub string in `oapa-homicide.l4`. |
| 7 | (a row of dots) | repealed or blank in this text | The text shows the number and a row of dots (src:13). Carried as a stub string in `oapa-homicide.l4`. |
| 8 | (no row in this text) | not applicable | The deposited text has no row with this number; there is nothing to encode. |
| 9 | Murder or manslaughter abroad. | encoded | Layer 1: `oapa-homicide.l4`, `s 9: the person may be dealt with, tried and punished in England or Ireland`, `s 9: a trial out of England or Ireland is not prevented by this Act`. Source lines src:14-15. |
| 10 | Provision for the trial of murder and manslaughter where the death or cause of death only happens in England or Ireland. | encoded | Layer 1: `oapa-homicide.l4`, `s 10: the person may be dealt with, tried and punished in England or Ireland`. Source lines src:16-17. |
| 11 | (a row of dots) | repealed or blank in this text | The text shows the number and a row of dots (src:18). Carried as a stub string in `oapa-homicide.l4`. |
| 12 | (no row in this text) | not applicable | The deposited text has no row with this number; there is nothing to encode. |
| 13 | (no row in this text) | not applicable | The deposited text has no row with this number; there is nothing to encode. |
| 14 | (no row in this text) | not applicable | The deposited text has no row with this number; there is nothing to encode. |
| 15 | (no row in this text) | not applicable | The deposited text has no row with this number; there is nothing to encode. |
| 16 | Threats to kill. | encoded | Layer 1: `oapa-threats.l4`, `s 16: threats to kill`. Source lines src:20-21. |
| 17 | Impeding a person endeavouring to save himself from shipwreck. | encoded | Layer 1: `oapa-danger-bodily-harm.l4`, `s 17: impeding a person endeavouring to save their life from shipwreck`. Source lines src:23-24. |
| 18 | Shooting or attempting to shoot, or wounding with intent to do grievous bodily harm. | encoded | Layer 1: `oapa-danger-bodily-harm.l4`, `s 18: wounding or causing grievous bodily harm, with intent`. Source lines src:25-26. |
| 19 | (a row of dots) | repealed or blank in this text | The text shows the number and a row of dots (src:27). Carried as a stub string in `oapa-danger-bodily-harm.l4`. |
| 20 | Inflicting bodily injury, with or without weapon. | encoded | Layer 1: `oapa-danger-bodily-harm.l4`, `s 20: wounding or inflicting grievous bodily harm`. Source lines src:28-29. |
| 21 | Attempting to choke, &c. in order to commit any indictable offence. | encoded | Layer 1: `oapa-danger-bodily-harm.l4`, `s 21: attempting to choke or render insensible, to commit an indictable offence`. Source lines src:30-31. |
| 22 | Using chloroform, &c. to commit any indictable offence. | encoded | Layer 1: `oapa-danger-bodily-harm.l4`, `s 22: administering a stupefying drug, to commit an indictable offence`. Source lines src:32-33. |
| 23 | Maliciously administering poison, &c. so as to endanger life or inflict grievous bodily harm. | encoded | Layer 1: `oapa-danger-bodily-harm.l4`, `s 23: administering poison so as to endanger life or inflict grievous bodily harm`. Source lines src:34-35. |
| 24 | Maliciously administering poison, &c. with intent to injure, aggrieve, or annoy any other person. | encoded | Layer 1: `oapa-danger-bodily-harm.l4`, `s 24: administering poison with intent to injure, aggrieve or annoy`. Source lines src:36-37. |
| 25 | If the jury be not satisfied that any person charged is guilty of felony, but guilty of misdemeanor they may find him guilty accordingly. | encoded | Layer 1: `oapa-danger-bodily-harm.l4`, `s 25: the jury may acquit of the section 23 felony and find the person guilty of the section 24 misdemeanor`, `s 25: the sentences open after an alternative verdict`. Source lines src:38-39. |
| 26 | Not providing apprentices or servants with food, &c. whereby life is endangered. | encoded | Layer 1: `oapa-danger-neglect-explosives.l4`, `s 26: neglecting or harming an apprentice or servant`. Source lines src:40-41. |
| 27 | Exposing children whereby life is endangered. | encoded | Layer 1: `oapa-danger-neglect-explosives.l4`, `s 27: abandoning or exposing a child under two years`. Source lines src:42-43. |
| 28 | Causing bodily injury by gunpowder. | encoded | Layer 1: `oapa-danger-neglect-explosives.l4`, `s 28: causing bodily injury by an explosion`. Source lines src:44-45. |
| 29 | Causing gunpowder to explode, or sending to any person an explosive substance, or throwing corrosive fluid on a person, with intent to do grievous bodily harm. | encoded | Layer 1: `oapa-danger-neglect-explosives.l4`, `s 29: causing an explosion, or sending or applying a dangerous thing, with intent`. Source lines src:46-47. |
| 30 | Placing gunpowder near a building, with intent to do bodily injury to any person. | encoded | Layer 1: `oapa-danger-neglect-explosives.l4`, `s 30: placing an explosive near a building, ship or vessel, with intent`. Source lines src:48-49. |
| 31 | Setting spring guns, &c., with intent to inflict grievous bodily harm. | encoded | Layer 1: `oapa-danger-neglect-explosives.l4`, `s 31: setting a spring gun or man trap`. Source lines src:50-51. |
| 32 | Placing wood, &c., on a railway, with intent to endanger passengers. | encoded | Layer 1: `oapa-danger-railways-vehicles.l4`, `s 32: placing an obstruction on a railway, with intent to endanger`. Source lines src:52-53. |
| 33 | Casting stone, &c. upon a railway carriage, with intent to endanger the safety of any person therein. | encoded | Layer 1: `oapa-danger-railways-vehicles.l4`, `s 33: casting a thing at a railway carriage, with intent`. Source lines src:54-55. |
| 34 | Doing or omitting anything to endanger passengers by railway. | encoded | Layer 1: `oapa-danger-railways-vehicles.l4`, `s 34: endangering railway passengers`. Source lines src:56-57. |
| 35 | Drivers of carriages injuring persons by furious driving. | encoded | Layer 1: `oapa-danger-railways-vehicles.l4`, `s 35: bodily harm by furious driving or wilful misconduct`. Source lines src:58-59. |
| 36 | Obstructing or assaulting a clergyman or other minister in the discharge of his duties. | encoded | Layer 1: `oapa-assaults.l4`, `s 36: obstructing or assaulting a clergyman or other minister`. Source lines src:61-62. |
| 37 | Assaulting a magistrate, &c. on account of his preserving wreck. | encoded | Layer 1: `oapa-assaults.l4`, `s 37: assaulting a person preserving a vessel or wreck`. Source lines src:63-64. |
| 38 | Assault with intent to commit felony, or on peace officers, &c. | encoded | Layer 1: `oapa-assaults.l4`, `s 38: assault with intent to resist or prevent lawful apprehension`. Source lines src:65-66. |
| 39 | Assaults with intent to obstruct the sale of grain, or its free passage. | encoded | Layer 1: `oapa-assaults.l4`, `s 39: violence to obstruct the sale or conveyance of grain` and its proviso. Source lines src:67-68. |
| 40 | Assaults on seamen, &c. | encoded | Layer 1: `oapa-assaults.l4`, `s 40: violence to hinder a seaman, keelman or caster` and its proviso. Source lines src:69-70. |
| 41 | (a row of dots) | repealed or blank in this text | The text shows the number and a row of dots (src:71). Carried as a stub string in `oapa-assaults.l4`. |
| 42 | Persons committing any common assault or battery may be imprisoned or compelled by two magistrates to pay fine and costs not exceeding 5 l. | encoded | Layer 1: `oapa-assaults.l4`, `s 42: two justices may hear and determine a common assault or battery`, `s 42: the fine together with the costs is within the maximum`, `s 42: the imprisonment is within the maximum`. Source lines src:72-73. |
| 43 | Persons convicted of aggravated assaults on females and boys under fourteen years of age may be imprisoned or fined. | repealed or blank in this text | The title survives (src:74) and the text is a row of dots (src:75). Carried as a stub string in `oapa-assaults.l4`; nothing is encoded. |
| 44 | If the magistrates dismiss the complaint, they shall make out a certificate to that effect. | encoded | Layer 1: `oapa-assaults.l4`, `s 44: a certificate of dismissal is owed to the person complained against`, `s 44: when the certificate is due`. Source lines src:76-77. |
| 45 | Certificate or conviction shall be a bar to any other proceedings. | encoded | Layer 1: `oapa-assaults.l4`, `s 45: the person is released from all further proceedings, civil or criminal, for the same cause`. Source lines src:78-79. |
| 46 | (a row of dots) | repealed or blank in this text | The text shows the number and a row of dots (src:80). Carried as a stub string in `oapa-assaults.l4`. |
| 47 | Assault occasioning bodily harm. | encoded | Layer 1: `oapa-assaults.l4`, `s 47: assault occasioning actual bodily harm`. Source lines src:81-82. |
| 48 | (a row of dots) | repealed or blank in this text | The text shows the number and a row of dots (src:83). Carried as a stub string in `oapa-assaults.l4`. |
| 49 | (a row of dots) | repealed or blank in this text | The text shows the number and a row of dots (src:84). Carried as a stub string in `oapa-assaults.l4`. |
| 50 | (a row of dots) | repealed or blank in this text | The text shows the number and a row of dots (src:85). Carried as a stub string in `oapa-assaults.l4`. |
| 51 | (no row in this text) | not applicable | The deposited text has no row with this number; there is nothing to encode. |
| 52 | (a row of dots) | repealed or blank in this text | The text shows the number and a row of dots (src:86). Carried as a stub string in `oapa-assaults.l4`. |
| 53 | (a row of dots) | repealed or blank in this text | The text shows the number and a row of dots (src:87). Carried as a stub string in `oapa-assaults.l4`. |
| 54 | (a row of dots) | repealed or blank in this text | The text shows the number and a row of dots (src:88). Carried as a stub string in `oapa-assaults.l4`. |
| 55 | (no row in this text) | not applicable | The deposited text has no row with this number; there is nothing to encode. |
| 56 | Child-stealing. | repealed or blank in this text | The title survives (src:90) and the text is a row of dots (src:91). Carried as a stub string in `oapa-bigamy.l4`; nothing is encoded. |
| 57 | Bigamy. Offence may be dealt with where offender shall be apprehended. Not to extend to second marriages, &c. herein stated. | encoded | Layer 1: `oapa-bigamy.l4`, `s 57: bigamy` and the four exception rules. Source lines src:93-94. |
| 58 | Administering drugs or using instruments to procure abortion. | encoded | Layer 1: `oapa-abortion-birth.l4`, `s 58: administering drugs or using instruments to procure abortion` (two limb rules). Source lines src:97-98. |
| 59 | Procuring drugs, &c. to cause abortion. | encoded | Layer 1: `oapa-abortion-birth.l4`, `s 59: supplying drugs or instruments to procure abortion`. Source lines src:99-100. |
| 60 | Concealing the birth of a child. | encoded | Layer 1: `oapa-abortion-birth.l4`, `s 60: concealing the birth of a child`. Source lines src:102-103. |
| 61 | (a row of dots) | repealed or blank in this text | The text shows the number and a row of dots (src:104). Carried as a stub string in `oapa-abortion-birth.l4`. |
| 62 | (no row in this text) | not applicable | The deposited text has no row with this number; there is nothing to encode. |
| 63 | (no row in this text) | not applicable | The deposited text has no row with this number; there is nothing to encode. |
| 64 | Making or having gunpowder, &c., with intent to commit any felony against this Act. | encoded | Layer 1: `oapa-gunpowder.l4`, `s 64: making or having gunpowder or a dangerous thing to commit a felony of this Act`. Source lines src:106-107. |
| 65 | Justices may issue warrants for searching houses, &c. in which explosive substances are suspected to be made for the purpose of committing felonies against this Act. | encoded | Layer 1: `oapa-gunpowder.l4`, `s 65: a justice of the peace may issue a warrant to search the place`, `s 65: the thing and its receptacles may be seized, removed and detained`. Source lines src:108-109. |
| 66 | (a row of dots) | repealed or blank in this text | The text shows the number and a row of dots (src:111). Carried as a stub string in `oapa-other.l4`. |
| 67 | (no row in this text) | not applicable | The deposited text has no row with this number; there is nothing to encode. |
| 68 | Offences committed within the jurisdiction of the Admiralty. | encoded | Layer 1: `oapa-other.l4`, `s 68: the offence is indictable`, `s 68: the person is liable to the same punishments as if the offence had been committed upon the land`. Source lines src:112-113. |
| 69 | (a row of dots) | repealed or blank in this text | The text shows the number and a row of dots (src:114). Carried as a stub string in `oapa-other.l4`. |
| 70 | (a row of dots) | repealed or blank in this text | The text shows the number and a row of dots (src:115). Carried as a stub string in `oapa-other.l4`. |
| 71 | (a row of dots) | repealed or blank in this text | The text shows the number and a row of dots (src:116). Carried as a stub string in `oapa-other.l4`. |
| 72 | (a row of dots) | repealed or blank in this text | The text shows the number and a row of dots (src:117). Carried as a stub string in `oapa-other.l4`. |
| 73 | (a row of dots) | repealed or blank in this text | The text shows the number and a row of dots (src:118). Carried as a stub string in `oapa-other.l4`. |
| 74 | (a row of dots) | repealed or blank in this text | The text shows the number and a row of dots (src:119). Carried as a stub string in `oapa-other.l4`. |
| 75 | (no row in this text) | not applicable | The deposited text has no row with this number; there is nothing to encode. |
| 76 | Summary proceedings in England may be under the 11 & 12 Vict. c. 43., and in Ireland under the 14 & 15 Vict. c. 93. Except in London and the Metropolitan Police District. | inert | Section 76 says how a summary offence is prosecuted, by reference to two other Acts (the Magistrates’ Courts Act 1952 and the Petty Sessions (Ireland) Act 1851) that are not among the inputs, and saves the law for the City of London and the Metropolitan Police District. It addresses the court and the prosecutor and tells the person nothing about whether they have offended or the most that can follow, so it is carried as a stub string and nothing is decided. Stub in `oapa-other.l4`. |
| 77 | (a row of dots) | repealed or blank in this text | The text shows the number and a row of dots (src:122). Carried as a stub string in `oapa-other.l4`. |
| 78 | Act not to extend to Scotland. | encoded | Layer 1: `oapa-other.l4`, `s 78: the Act extends to Scotland for this matter`. Source lines src:123-124. |
| 79 | (a row of dots) | repealed or blank in this text | The text shows the number and a row of dots (src:125). Carried as a stub string in `oapa-other.l4`. |

## Jural relations

One row per provision that creates a relation, each stated once and neutrally.
The text names no holder of the claim that the offence sections correlate with: it says "whosoever shall ... shall be guilty", so each offence section is recorded as the court’s power to convict and sentence and the accused’s liability to it.
The same rule is the duty on the person not to do the act, read from the other side; it is not written twice.
Definitions and counting rules are listed once as `none`.

| Section | Relation | Holder | Bearer | L4 rule(s) |
| --- | --- | --- | --- | --- |
| 4 | power to convict and sentence (soliciting or proposing a murder) / liability | the court (acting on a prosecution the text does not name) | the person accused | `s 4: soliciting or proposing a murder`; `s 4: the sentences the text states` |
| 16 | power to convict and sentence (threats to kill) / liability | the court (acting on a prosecution the text does not name) | the person accused | `s 16: threats to kill`; `s 16: the sentences the text states` |
| 17 | power to convict and sentence (impeding a rescue from shipwreck) / liability | the court (acting on a prosecution the text does not name) | the person accused | `s 17: impeding a person endeavouring to save their life from shipwreck`; `s 17: the sentences the text states` |
| 18 | power to convict and sentence (wounding or causing grievous bodily harm, with intent) / liability | the court (acting on a prosecution the text does not name) | the person accused | `s 18: wounding or causing grievous bodily harm, with intent`; `s 18: the sentences the text states` |
| 20 | power to convict and sentence (wounding or inflicting grievous bodily harm) / liability | the court (acting on a prosecution the text does not name) | the person accused | `s 20: wounding or inflicting grievous bodily harm`; `s 20: the sentences the text states` |
| 21 | power to convict and sentence (attempting to choke, to commit an indictable offence) / liability | the court (acting on a prosecution the text does not name) | the person accused | `s 21: attempting to choke or render insensible, to commit an indictable offence`; `s 21: the sentences the text states` |
| 22 | power to convict and sentence (a stupefying drug, to commit an indictable offence) / liability | the court (acting on a prosecution the text does not name) | the person accused | `s 22: administering a stupefying drug, to commit an indictable offence`; `s 22: the sentences the text states` |
| 23 | power to convict and sentence (poison endangering life or inflicting grievous bodily harm) / liability | the court (acting on a prosecution the text does not name) | the person accused | `s 23: administering poison so as to endanger life or inflict grievous bodily harm`; `s 23: the sentences the text states` |
| 24 | power to convict and sentence (poison with intent to injure, aggrieve or annoy) / liability | the court (acting on a prosecution the text does not name) | the person accused | `s 24: administering poison with intent to injure, aggrieve or annoy`; `s 24: the sentences the text states` |
| 26 | power to convict and sentence (neglecting or harming an apprentice or servant) / liability | the court (acting on a prosecution the text does not name) | the person accused | `s 26: neglecting or harming an apprentice or servant`; `s 26: the sentences the text states` |
| 27 | power to convict and sentence (abandoning or exposing a child under two years) / liability | the court (acting on a prosecution the text does not name) | the person accused | `s 27: abandoning or exposing a child under two years`; `s 27: the sentences the text states` |
| 28 | power to convict and sentence (bodily injury by an explosion) / liability | the court (acting on a prosecution the text does not name) | the person accused | `s 28: causing bodily injury by an explosion`; `s 28: the sentences the text states` |
| 29 | power to convict and sentence (an explosion, or sending or applying a dangerous thing, with intent) / liability | the court (acting on a prosecution the text does not name) | the person accused | `s 29: causing an explosion, or sending or applying a dangerous thing, with intent`; `s 29: the sentences the text states` |
| 30 | power to convict and sentence (an explosive near a building, ship or vessel, with intent) / liability | the court (acting on a prosecution the text does not name) | the person accused | `s 30: placing an explosive near a building, ship or vessel, with intent`; `s 30: the sentences the text states` |
| 31 | power to convict and sentence (setting a spring gun or man trap) / liability | the court (acting on a prosecution the text does not name) | the person accused | `s 31: setting a spring gun or man trap`; `s 31: the sentences the text states` |
| 32 | power to convict and sentence (an obstruction on a railway, with intent to endanger) / liability | the court (acting on a prosecution the text does not name) | the person accused | `s 32: placing an obstruction on a railway, with intent to endanger`; `s 32: the sentences the text states` |
| 33 | power to convict and sentence (casting a thing at a railway carriage, with intent) / liability | the court (acting on a prosecution the text does not name) | the person accused | `s 33: casting a thing at a railway carriage, with intent`; `s 33: the sentences the text states` |
| 34 | power to convict and sentence (endangering railway passengers) / liability | the court (acting on a prosecution the text does not name) | the person accused | `s 34: endangering railway passengers`; `s 34: the sentences the text states` |
| 35 | power to convict and sentence (bodily harm by furious driving or wilful misconduct) / liability | the court (acting on a prosecution the text does not name) | the person accused | `s 35: bodily harm by furious driving or wilful misconduct`; `s 35: the sentences the text states` |
| 36 | power to convict and sentence (obstructing or assaulting a clergyman or other minister) / liability | the court (acting on a prosecution the text does not name) | the person accused | `s 36: obstructing or assaulting a clergyman or other minister`; `s 36: the sentences the text states` |
| 37 | power to convict and sentence (assaulting a person preserving a vessel or wreck) / liability | the court (acting on a prosecution the text does not name) | the person accused | `s 37: assaulting a person preserving a vessel or wreck`; `s 37: the sentences the text states` |
| 38 | power to convict and sentence (assault to resist or prevent lawful apprehension) / liability | the court (acting on a prosecution the text does not name) | the person accused | `s 38: assault with intent to resist or prevent lawful apprehension`; `s 38: the sentences the text states` |
| 39 | power to convict and sentence (violence to obstruct the sale or conveyance of grain) / liability | the court (acting on a prosecution the text does not name) | the person accused | `s 39: violence to obstruct the sale or conveyance of grain`; `s 39: the sentences the text states` |
| 40 | power to convict and sentence (violence to hinder a seaman, keelman or caster) / liability | the court (acting on a prosecution the text does not name) | the person accused | `s 40: violence to hinder a seaman, keelman or caster`; `s 40: the sentences the text states` |
| 47 | power to convict and sentence (assault occasioning actual bodily harm) / liability | the court (acting on a prosecution the text does not name) | the person accused | `s 47: assault occasioning actual bodily harm`; `s 47: the sentences the text states` |
| 57 | power to convict and sentence (bigamy) / liability | the court (acting on a prosecution the text does not name) | the person accused | `s 57: bigamy`; `s 57: the sentences the text states` |
| 58 | power to convict and sentence (procuring abortion by drugs or instruments) / liability | the court (acting on a prosecution the text does not name) | the person accused | `s 58: administering drugs or using instruments to procure abortion`; `s 58: the sentences the text states` |
| 59 | power to convict and sentence (supplying drugs or instruments to procure abortion) / liability | the court (acting on a prosecution the text does not name) | the person accused | `s 59: supplying drugs or instruments to procure abortion`; `s 59: the sentences the text states` |
| 60 | power to convict and sentence (concealing the birth of a child) / liability | the court (acting on a prosecution the text does not name) | the person accused | `s 60: concealing the birth of a child`; `s 60: the sentences the text states` |
| 64 | power to convict and sentence (gunpowder or a dangerous thing to commit a felony of the Act) / liability | the court (acting on a prosecution the text does not name) | the person accused | `s 64: making or having gunpowder or a dangerous thing to commit a felony of this Act`; `s 64: the sentences the text states` |
| 5 | power to sentence on a conviction of manslaughter / liability | the court | the person convicted of manslaughter | `s 5: the sentences the text states for a conviction of manslaughter` |
| 9 | power to deal with, try and punish in England or Ireland a killing on land out of the United Kingdom / liability | the courts of England or Ireland | the subject of Her Majesty charged | `s 9: the person may be dealt with, tried and punished in England or Ireland` |
| 9 (proviso) | the courts outside England and Ireland keep their power to try / liability | the courts of any place outside England or Ireland | the person who killed there | `s 9: a trial out of England or Ireland is not prevented by this Act` |
| 10 | power to deal with, try and punish where the hurt or the death was in England or Ireland / liability | the courts of England or Ireland | the person who hurt, where the death or its cause was in England or Ireland | `s 10: the person may be dealt with, tried and punished in England or Ireland` |
| 25 | power to find the section 24 misdemeanor on a section 23 trial / liability | the jury | the person tried for the section 23 felony | `s 25: the jury may acquit of the section 23 felony and find the person guilty of the section 24 misdemeanor`; `s 25: the sentences open after an alternative verdict` |
| 39 (proviso) | immunity from a second punishment under any other law | the person already punished under the section | any other authority that might punish (a disability) | `s 39: the person cannot be punished for the same offence under any other law` |
| 40 (proviso) | immunity from a second punishment under any other law | the person already punished under the section | any other authority that might punish (a disability) | `s 40: the person cannot be punished for the same offence under any other law` |
| 42 | power to hear and determine a common assault or battery / liability | two justices of the peace | the person complained against | `s 42: two justices may hear and determine a common assault or battery` |
| 42 (limits) | immunity from an order above the maxima / disability of the justices | the person convicted by the justices | the justices | `s 42: the fine together with the costs is within the maximum`; `s 42: the imprisonment is within the maximum` |
| 44 | claim to a certificate of dismissal / duty to make it out and deliver it forthwith | the person complained against | the justices | `s 44: a certificate of dismissal is owed to the person complained against`; `s 44: when the certificate is due` |
| 45 | immunity from all further proceedings, civil or criminal, for the same cause / disability | the person who obtained the certificate, or paid, or served | the party aggrieved and anyone else who might bring proceedings for that cause | `s 45: the person is released from all further proceedings, civil or criminal, for the same cause` |
| 57 (four exceptions) | privilege to marry again in the four cases / no-right | the married person in one of the four cases | the court and the prosecutor | `s 57: exception for a second marriage contracted abroad by a person who is not a subject`; `s 57: exception for a spouse continually absent seven years and not known to be living`; `s 57: exception for a person divorced from the first marriage`; `s 57: exception for a former marriage declared void` |
| 65 (warrant) | power to issue a search warrant on reasonable cause assigned upon oath / liability | a justice of the peace | the person in occupation of the house, mill, magazine, storehouse, warehouse, shop, cellar, yard, wharf or other place, or of the carriage, ship, boat or vessel | `s 65: a justice of the peace may issue a warrant to search the place` |
| 65 (seizure) | power to seize, remove and detain what is found / liability | the person acting in the execution of the warrant | the person whose things are found | `s 65: the thing and its receptacles may be seized, removed and detained` |
| 68 | power to punish as if the offence had been committed on land / liability | the courts of England or Ireland | the person who committed an indictable offence of the Act within the Admiralty’s jurisdiction | `s 68: the person is liable to the same punishments as if the offence had been committed upon the land`; `s 68: the offence is indictable` |
| 78 | none: a rule of reach (the Act does not extend to Scotland unless expressly provided) | none | none | `s 78: the Act extends to Scotland for this matter` |
| 76 | none: procedure by reference to other Acts (inert) | none | none | `s 76: procedure for summary offences, not encoded` |
| 1, 2, 6, 7, 11, 19, 41, 43, 46, 48-50, 52-54, 56, 61, 66, 69-74, 77, 79 | none: blank in this text | none | none | the stub string rules |
| (nouns) | none: the kinds of punishment, the words of classification, the list of offences | none | none | `oapa-nouns.l4` |
| (table) | none: a lookup from each offence to the three statements its own section makes, and an arithmetic comparison | none | none | `oapa-table.l4` |

## Fork register

Each entry gives the ambiguity, the readings seen, the reading taken, and the text that licenses it (by raw-text line).
Where the reading matters to an answer, the case that shows it is named.
Identifiers are the section number and a letter; the seat and the modules cite them.

| Id | Section | Ambiguity | Readings seen | Reading taken | Licensing text |
| --- | --- | --- | --- | --- | --- |
| 4a | 4 | Does "to murder any other person" attach to all five verbs? | all five; only "propose" | all five verbs are alternatives, and what is put to the other person must be a murder. The plain glosses of the verbs in the module are the encoder’s, not the text’s | src:9: "solicit, encourage, persuade, or endeavour to persuade, or shall propose to any person, to murder any other person" |
| 5a | 1, 2, 5 | The text defines neither murder nor manslaughter | treat as inputs; answer "not covered" | the two questions return `the deposited text does not say`; section 5 gives only the penalty, taken when the person states a conviction | src:6, src:7 (rows of dots), src:11 |
| 9a | 9 | Which facts does the main rule read, and which the proviso? | one rule reading all six fields; two rules | the main rule reads: a murder or manslaughter, on land out of the United Kingdom, the person charged is a subject. The proviso reads: a murder or manslaughter, and the killing out of England or Ireland. "within the Queen’s dominions" and "the person killed was a subject" are read by neither | src:15: "whether within the Queen’s dominions or without, and whether the person killed were a subject of Her Majesty or not" |
| 16a | 16 | "intending that that other would fear it would be carried out" -- whose intention? | the threatener must mean to carry the threat out; must only intend the other’s fear | the intention is about the other person’s fear; meaning to carry it out is not an element (asserted: `s16 meant to carry it out but did not intend fear`) | src:21 |
| 18a | 18 | The text has lost its first verbs and starts mid-sentence | four combinations of verb and intent; fewer | (wound OR cause grievous bodily harm) AND (intent to do grievous bodily harm OR intent to resist lawful apprehension) | src:26 |
| 20a | 20 | "wound or inflict" against section 18’s "wound or cause" | one verb pair; two | two fields, kept apart; the encoding does not decide whether the verbs differ | src:26, src:29 |
| 25a | 25 | The jury "may" convict of the lesser offence | a court power only; a fact the person can state | the person states the trial facts (tried for the section 23 felony, jury not satisfied of it, jury satisfied of section 24); the sentence is section 24’s | src:39 |
| 26a | 26 | Does "so that the life ... shall be endangered, or the health ... permanently injured" govern both ways in? | the result clause governs both; governs only the second | governs both: (liable, and refused without excuse) OR (unlawfully, maliciously, bodily harm), AND (life endangered OR health injured). Asserted: `s26 bodily harm, but no life or health result` | src:41 |
| 27a | 27 | "under the age of two years" | complete months below 24; days | complete months, below 24 (asserted at 23 and 24) | src:43 |
| 31a | 31 | "with the intent that the same or whereby the same may destroy" | one intent; two alternative intents | two alternative intents; the first proviso (vermin) and the second (dwelling house) cover both ways in because the permitting limb deems the person to have set the engine with the intent | src:51 |
| 34a | 34 | Does "wilful" govern both "omission" and "neglect"? | yes; only "omission" | both | src:57 |
| 36a | 36 | Does "to the knowledge of the offender" attach to the minister “engaged in” the rites? | all three limbs; only the “about to engage” and “going to perform or returning” limbs | only the last two; a minister actually engaged needs no knowledge | src:62 |
| 38a | 38 | The text begins ". . ." and the heading names felony and peace officers | encode the heading; encode only the words that remain | only the words that remain: an assault with intent to resist or prevent the lawful apprehension or detainer of oneself or another for any offence | src:65-66 |
| 39a | 39 | Two limbs | one; two | (violence with intent to deter, hinder or compel) OR (violence to a carrier, with intent to stop the conveyance) | src:68 |
| 40a | 40 | "unlawfully" appears in the first limb only | both; first only | first limb only | src:70 |
| 42a | 42 | Heading says "5 l."; the body says £200 | the heading; the body | the body governs (asserted at 200 and 201) | src:72-73 |
| 44a | 44 | The justices’ findings, and the blank section 43 | refuse; take the findings as inputs | the findings (deemed not proved, justified, trifling; dismissed) are inputs the person can state; "under either of the last two preceding sections" is met by a section 42 complaint, section 43 being blank | src:77 |
| 45a | 45 | Are the three ways in alternatives? | alternatives; cumulative | alternatives: a certificate, or paying the whole amount, or serving the imprisonment | src:79 |
| 47a | 47 | The section states a penalty but no elements | refuse; read the elements from the heading | an assault that occasioned actual bodily harm; both terms undefined | src:81-82 |
| 57a | 57 | The four exceptions | each alone; combined | each alone takes the person out. Exception 1 needs both outside England and Ireland and not a subject | src:95 |
| 57b | 57 | "continually absent ... for the space of seven years then last past" | complete years at least 7; more than 7 | at least 7 complete years (asserted at 6, 7, 10) | src:95 |
| 57c | 57 | "whose former marriage shall have been declared void" -- when? | before the second marriage; at any time | had been declared void at the time of the second marriage; the text does not say, and a later declaration is not modelled | src:95 |
| 58a | 58 | Limb two says "any woman", not "any other woman" | limb two excludes the woman herself; includes her | includes her, so limb one is contained in limb two for the same acts; both carry the same penalty so no answer changes (asserted: `s58 a woman not with child acting on herself, as limb two reads`) | src:98 |
| 58b | 58, 59 | "unlawfully" | import the Abortion Act 1967; a stated fact | a stated fact; the Act alone | src:98, src:100 |
| 60a | 60 | "every person" | the woman only; anyone | anyone, the woman included (asserted) | src:103 |
| 64a | 64 | "any of the felonies in this Act mentioned" | the felonies of the Act as the text names them; any felony | the offences the text itself calls "felony" (12 of the 32 listed: ss 17, 18, 21, 22, 23, 28, 29, 30, 32, 33, 57, 58), worked out in `oapa-table.l4`, never asked. See finding 6 | src:107 and the penalty line of each section |
| 65a | 65 | Whether the cause assigned is "reasonable"; what powers are borrowed | the justice’s judgment as an input; refuse | the justice’s acceptance of the cause is an input; the borrowed powers of 23 & 24 Vict. c. 139 are not encoded | src:108-109 |
| 68a | 68 | "indictable offences" -- which are? | the text names them; ask | the text says "on indictment" only in ss 16 and 47 and "before two justices" in ss 39, 40, 42; for the rest the person states whether it is indictable (asserted) | src:21, src:82, src:68, src:70, src:73, src:113 |
| 76a | 76 | Procedure by reference to other Acts | encode; inert | inert | src:120-121 |
| 78a | 78 | "except as herein-before otherwise expressly provided" | ask the person; fix the input | fixed at "no earlier provision names Scotland": the deposited text mentions Scotland only in section 78 (2 lines), so the seat passes FALSE. If a ". . ." gap hid an express extension the answer would change | src:123-124 |
| U1 | all penalties | Units and the text’s own words | convert to modern terms; keep | every fixed term in months (2 years = 24, 7 = 84, 10 = 120, 14 = 168); "penal servitude" and "misdemeanor" kept as the text spells them | each penalty line |
| U2 | seat | "unlawfully", "maliciously", "wilfully" | decide for the person; ask | asked, with an `@desc` that says the Act does not define "maliciously" | the offence sections |

## What the text turns out to say (findings)

1. The deposited text does not define murder or manslaughter.
   Sections 1 and 2 are rows of dots (src:6, src:7) and section 5 states only the penalty (src:11).
   The seat’s "does this text tell me whether what I did is a murder / a manslaughter" questions return `the deposited text does not say`.
   Asserted.
2. Eleven offences have a penalty whose term is hidden by ". . .": sections 20, 24, 26, 27, 31, 47 and 59 (penal servitude, no term at all) and sections 28, 29, 30 and 32 (an imprisonment alternative with no term, beside a stated penal servitude).
   For the seven the most that can follow is not computable from the text; for the four the imprisonment alternative has no stated term while a penal servitude figure is stated.
   In both cases the comparison returns `the text states no maximum for that kind of sentence` for the kind whose term is hidden.
   Asserted.
3. The text calls twelve of the 32 listed offences "felony": sections 17, 18, 21, 22, 23, 28, 29, 30, 32, 33, 57 and 58.
   Section 4 (soliciting a murder), 20, 24, 26, 27, 31, 34-38, 59, 60 and 64 are "misdemeanor"; section 16 is only "an offence"; sections 39, 40, 42 and 47 carry no classification, and neither does the manslaughter penalty in section 5.
   Asserted (`oapa-tests-table.l4`).
4. Only sections 16 and 47 say "on indictment"; sections 39, 40 and 42 say "before two justices of the peace"; the other offences say nothing about how they are tried.
   Asserted.
5. Section 42’s heading says "5 l." and its body says "£200".
   The body governs; the ceiling is the fine together with costs, 200 pounds, and imprisonment up to 6 months, and imprisonment up to 6 months again in default of payment.
   Asserted at 200/201 pounds and 6/7 months.
6. Section 64 reaches only "the felonies in this Act mentioned".
   The deposited text never applies the word "felony" to murder or manslaughter (no line between the Homicide heading and the Letters-threatening-to-murder heading contains it), so an intent to commit murder is not caught by section 64 as this text reads.
   A person asking the seat who intended murder can only say the intended offence is not one of the Act’s listed offences, and gets "not made out".
   That may not match the law as it stands, because the text before the omissions may have said otherwise; it is the limit of the deposit.
   Asserted for the listed offences; the murder gap is stated here and not asserted.
7. Section 43’s text is a row of dots but its title survives, and sections 44 and 45 still refer to complaints "under either of the last two preceding sections".
   Only section 42 complaints are modelled.
8. Section 38 begins ". . ." and its heading speaks of felony and peace officers, which the remaining words do not mention.
   Only the remaining words are encoded.
9. Section 58’s second limb says "any woman", so on its words it reaches a woman acting on herself; the first limb adds only the requirement that she be with child.
   Both carry penal servitude for life, so no answer changes.
   Asserted.
10. In section 57 the four exceptions are separate ways out.
    Seven complete years of absence is enough and six is not (asserted at 6, 7 and 10), and the person must also not have known the spouse to be living within that time.
    Asserted.
11. Section 27’s "under the age of two years" is read as under 24 complete months.
    Asserted at 23 and 24.
12. Section 16 does not make an intention to carry the threat out an element.
    Asserted (layer 1).
13. Section 44 gives the person complained against a claim to a certificate "forthwith" and states no number of days.
    Asserted.
14. Section 45 releases the person on any one of three events (a certificate, payment of the whole amount adjudged, serving the imprisonment awarded).
    Asserted.
15. Section 78: the word Scotland occurs on two lines of the text, both in section 78, so the seat answers that the Act does not reach what was done in Scotland.
    Asserted.
16. Section 25: a person tried for the section 23 felony may be found guilty of the section 24 misdemeanor and is punished as for it, with the section 24 term hidden (finding 2).
    Asserted.
17. The text is the revised text at 2026-04-29 as rendered; the penalties it shows (penal servitude, terms in years, "imprisonment for life") are the text’s words and are not today’s sentencing law.
    Nothing here says what a court would impose today.

## Placeholders in the seat

A record field no rule reads gets a fixed value, with a comment at the line; "derived" means the value comes from other inputs.

| Question | Kind | Record field | Why |
| --- | --- | --- | --- |
| Could what I said to someone amount to soliciting or proposing a murder (s 4)? | placeholder | the other person is a subject of Her Majesty | the rule does not read this field; section 4 says it does not matter whether the other person is a subject of Her Majesty. |
| Could what I said to someone amount to soliciting or proposing a murder (s 4)? | placeholder | the other person is within the Queen's dominions | the rule does not read this field; section 4 says it does not matter whether the other person is within the Queen's dominions. |
| Can I be dealt with, tried and punished in England or Ireland for a killing abroad (s 9)? | placeholder | the place is within the Queen's dominions | the rule does not read this field; section 9 applies whether the place is within the Queen's dominions or not. |
| Can I be dealt with, tried and punished in England or Ireland for a killing abroad (s 9)? | placeholder | the person killed was a subject of Her Majesty | the rule does not read this field; section 9 applies whether the person killed was a subject of Her Majesty or not. |
| Can I be dealt with, tried and punished in England or Ireland for a killing abroad (s 9)? | placeholder | the killing was out of England or Ireland | the rule does not read this field; it is read only by the proviso below. |
| Does the Act leave it open to try me outside England and Ireland for a killing abroad (s 9)? | placeholder | on land out of the United Kingdom | the proviso rule does not read this field. |
| Does the Act leave it open to try me outside England and Ireland for a killing abroad (s 9)? | placeholder | the person charged is a subject of Her Majesty | the proviso rule does not read this field. |
| Does the Act leave it open to try me outside England and Ireland for a killing abroad (s 9)? | placeholder | the place is within the Queen's dominions | the proviso rule does not read this field. |
| Does the Act leave it open to try me outside England and Ireland for a killing abroad (s 9)? | placeholder | the person killed was a subject of Her Majesty | the proviso rule does not read this field. |
| Could a threat I made amount to the offence of threatening to kill (s 16)? | placeholder | meant to carry the threat out | the rule does not read this field; section 16 does not make an intention to carry the threat out an element. |
| Could I have broken section 20 by wounding or inflicting grievous bodily harm? | placeholder | used a weapon or instrument | the rule does not read this field; section 20 applies "with or without any weapon or instrument". |
| Could I have broken section 29 by causing an explosion, or sending or applying a dangerous thing, with intent? | placeholder | bodily injury was effected | the rule does not read this field; section 29 applies "whether any bodily injury be effected or not". |
| Could I have broken section 30 by placing an explosive near a building, ship or vessel with intent? | placeholder | an explosion took place | the rule does not read this field; section 30 applies "whether or not any explosion take place". |
| Could I have broken section 30 by placing an explosive near a building, ship or vessel with intent? | placeholder | bodily injury was effected | the rule does not read this field; section 30 applies "whether or not any bodily injury be effected". |
| Am I excused from a bigamy charge because I married abroad and am not a subject of Her Majesty (s 57)? | placeholder | the person was married | this exception does not read this field. |
| Am I excused from a bigamy charge because I married abroad and am not a subject of Her Majesty (s 57)? | placeholder | the person married another person | this exception does not read this field. |
| Am I excused from a bigamy charge because I married abroad and am not a subject of Her Majesty (s 57)? | placeholder | the former husband or wife was then living | this exception does not read this field. |
| Am I excused from a bigamy charge because I married abroad and am not a subject of Her Majesty (s 57)? | placeholder | the number of complete years the husband or wife had been continually absent | this exception does not read this field. |
| Am I excused from a bigamy charge because I married abroad and am not a subject of Her Majesty (s 57)? | placeholder | the person had known the husband or wife to be living within that time | this exception does not read this field. |
| Am I excused from a bigamy charge because I married abroad and am not a subject of Her Majesty (s 57)? | placeholder | the person had been divorced from the bond of the first marriage | this exception does not read this field. |
| Am I excused from a bigamy charge because I married abroad and am not a subject of Her Majesty (s 57)? | placeholder | the former marriage had been declared void by the sentence of a court of competent jurisdiction | this exception does not read this field. |
| Am I excused from a bigamy charge because my husband or wife had been absent for seven years and I did not know they were living (s 57)? | placeholder | the person was married | this exception does not read this field. |
| Am I excused from a bigamy charge because my husband or wife had been absent for seven years and I did not know they were living (s 57)? | placeholder | the person married another person | this exception does not read this field. |
| Am I excused from a bigamy charge because my husband or wife had been absent for seven years and I did not know they were living (s 57)? | placeholder | the former husband or wife was then living | this exception does not read this field. |
| Am I excused from a bigamy charge because my husband or wife had been absent for seven years and I did not know they were living (s 57)? | placeholder | the second marriage took place in England or Ireland | this exception does not read this field. |
| Am I excused from a bigamy charge because my husband or wife had been absent for seven years and I did not know they were living (s 57)? | placeholder | the person is a subject of Her Majesty | this exception does not read this field. |
| Am I excused from a bigamy charge because my husband or wife had been absent for seven years and I did not know they were living (s 57)? | placeholder | the person had been divorced from the bond of the first marriage | this exception does not read this field. |
| Am I excused from a bigamy charge because my husband or wife had been absent for seven years and I did not know they were living (s 57)? | placeholder | the former marriage had been declared void by the sentence of a court of competent jurisdiction | this exception does not read this field. |
| Am I excused from a bigamy charge because I was divorced from the first marriage (s 57)? | placeholder | the person was married | this exception does not read this field. |
| Am I excused from a bigamy charge because I was divorced from the first marriage (s 57)? | placeholder | the person married another person | this exception does not read this field. |
| Am I excused from a bigamy charge because I was divorced from the first marriage (s 57)? | placeholder | the former husband or wife was then living | this exception does not read this field. |
| Am I excused from a bigamy charge because I was divorced from the first marriage (s 57)? | placeholder | the second marriage took place in England or Ireland | this exception does not read this field. |
| Am I excused from a bigamy charge because I was divorced from the first marriage (s 57)? | placeholder | the person is a subject of Her Majesty | this exception does not read this field. |
| Am I excused from a bigamy charge because I was divorced from the first marriage (s 57)? | placeholder | the number of complete years the husband or wife had been continually absent | this exception does not read this field. |
| Am I excused from a bigamy charge because I was divorced from the first marriage (s 57)? | placeholder | the person had known the husband or wife to be living within that time | this exception does not read this field. |
| Am I excused from a bigamy charge because I was divorced from the first marriage (s 57)? | placeholder | the former marriage had been declared void by the sentence of a court of competent jurisdiction | this exception does not read this field. |
| Am I excused from a bigamy charge because my former marriage had been declared void (s 57)? | placeholder | the person was married | this exception does not read this field. |
| Am I excused from a bigamy charge because my former marriage had been declared void (s 57)? | placeholder | the person married another person | this exception does not read this field. |
| Am I excused from a bigamy charge because my former marriage had been declared void (s 57)? | placeholder | the former husband or wife was then living | this exception does not read this field. |
| Am I excused from a bigamy charge because my former marriage had been declared void (s 57)? | placeholder | the second marriage took place in England or Ireland | this exception does not read this field. |
| Am I excused from a bigamy charge because my former marriage had been declared void (s 57)? | placeholder | the person is a subject of Her Majesty | this exception does not read this field. |
| Am I excused from a bigamy charge because my former marriage had been declared void (s 57)? | placeholder | the number of complete years the husband or wife had been continually absent | this exception does not read this field. |
| Am I excused from a bigamy charge because my former marriage had been declared void (s 57)? | placeholder | the person had known the husband or wife to be living within that time | this exception does not read this field. |
| Am I excused from a bigamy charge because my former marriage had been declared void (s 57)? | placeholder | the person had been divorced from the bond of the first marriage | this exception does not read this field. |
| Could I have broken section 60 by secretly disposing of a child's body to conceal its birth? | placeholder | the person is the woman who was delivered | the rule does not read this field; section 60 reaches "every person", the woman or anyone else. |
| Could having or making gunpowder or a dangerous thing amount to an offence under section 64? | derived | how the text classifies the offence intended | the Act's own word for the offence intended; an offence outside this Act has no word in it. |
| Can a justice of the peace issue a warrant to search my premises, carriage or vessel (s 65)? | placeholder | the thing was found upon the search | the warrant rule does not read this field. |
| Can a justice of the peace issue a warrant to search my premises, carriage or vessel (s 65)? | placeholder | the person executing the warrant has good cause to suspect it to be intended to be used in committing such a felony | the warrant rule does not read this field. |
| Am I liable to the same punishment for an offence on the water within the Admiralty's jurisdiction as for one on land (s 68)? | derived | the offence is one mentioned in this Act | the person chose it from the Act's own list of offences. |

## The seat’s questions


| Group | Question |
| --- | --- |
| Murder, manslaughter and killing abroad | Could what I said to someone amount to soliciting or proposing a murder (s 4)? |
| Murder, manslaughter and killing abroad | Does this text tell me whether what I did is a murder (ss 1, 2)? |
| Murder, manslaughter and killing abroad | Does this text tell me whether what I did is a manslaughter (s 5)? |
| Murder, manslaughter and killing abroad | What is the most that can follow if I am convicted of manslaughter (s 5)? |
| Murder, manslaughter and killing abroad | Can I be dealt with, tried and punished in England or Ireland for a killing abroad (s 9)? |
| Murder, manslaughter and killing abroad | Does the Act leave it open to try me outside England and Ireland for a killing abroad (s 9)? |
| Murder, manslaughter and killing abroad | Can I be tried in England or Ireland where the hurt and the death happened in different places (s 10)? |
| Threats to kill | Could a threat I made amount to the offence of threatening to kill (s 16)? |
| Endangering life and causing bodily harm | Could I have broken section 17 by stopping someone saving their life from a shipwreck? |
| Endangering life and causing bodily harm | Could I have broken section 18 by wounding or harming someone with intent? |
| Endangering life and causing bodily harm | Could I have broken section 20 by wounding or inflicting grievous bodily harm? |
| Endangering life and causing bodily harm | Could I have broken section 21 by attempting to choke someone to commit an indictable offence? |
| Endangering life and causing bodily harm | Could I have broken section 22 by giving someone a stupefying drug to commit an indictable offence? |
| Endangering life and causing bodily harm | Could I have broken section 23 by giving someone poison that endangered their life or caused grievous bodily harm? |
| Endangering life and causing bodily harm | Could I have broken section 24 by giving someone poison with intent to injure, aggrieve or annoy? |
| Endangering life and causing bodily harm | If I am tried under section 23 and the jury is not satisfied of that, can I be found guilty under section 24 instead (s 25)? |
| Neglect, abandonment, explosives and traps | Could I have broken section 26 by neglecting or harming my apprentice or servant? |
| Neglect, abandonment, explosives and traps | Could I have broken section 27 by abandoning or exposing a child under two years old? |
| Neglect, abandonment, explosives and traps | Could I have broken section 28 by causing bodily injury with an explosion? |
| Neglect, abandonment, explosives and traps | Could I have broken section 29 by causing an explosion, or sending or applying a dangerous thing, with intent? |
| Neglect, abandonment, explosives and traps | Could I have broken section 30 by placing an explosive near a building, ship or vessel with intent? |
| Neglect, abandonment, explosives and traps | Could I have broken section 31 by setting a spring gun, man trap or similar engine? |
| Railways and carriages | Could I have broken section 32 by placing an obstruction on a railway or interfering with its signals? |
| Railways and carriages | Could I have broken section 33 by throwing something at a railway carriage? |
| Railways and carriages | Could I have broken section 34 by endangering railway passengers through an unlawful act or neglect? |
| Railways and carriages | Could I have broken section 35 by causing bodily harm through furious driving or wilful misconduct? |
| Assaults | Could I have broken section 36 by obstructing, striking or arresting a clergyman or other minister? |
| Assaults | Could I have broken section 37 by assaulting a person preserving a vessel or wreck? |
| Assaults | Could I have broken section 38 by assaulting someone to resist or prevent a lawful arrest? |
| Assaults | Could I have broken section 39 by using violence to obstruct the sale or carriage of grain? |
| Assaults | Once punished under section 39, can I be punished again for the same offence under another law (s 39)? |
| Assaults | Could I have broken section 40 by using violence to hinder a seaman, keelman or caster? |
| Assaults | Once punished under section 40, can I be punished again for the same offence under another law (s 40)? |
| Assaults | Could two justices hear a complaint against me of assault or battery, and what is the most they can order (s 42)? |
| Assaults | Is a fine of this size, with costs, within what two justices can order for assault or battery (s 42)? |
| Assaults | Is a term of imprisonment of this length within what two justices can order for assault or battery (s 42)? |
| Assaults | Am I entitled to a certificate of dismissal (s 44)? |
| Assaults | By when must the justices give me the certificate of dismissal (s 44)? |
| Assaults | Am I protected from any further civil or criminal proceedings for the same cause (s 45)? |
| Assaults | Could I have broken section 47 by an assault that caused actual bodily harm? |
| Bigamy | Could my second marriage amount to bigamy (s 57)? |
| Bigamy | Am I excused from a bigamy charge because I married abroad and am not a subject of Her Majesty (s 57)? |
| Bigamy | Am I excused from a bigamy charge because my husband or wife had been absent for seven years and I did not know they were living (s 57)? |
| Bigamy | Am I excused from a bigamy charge because I was divorced from the first marriage (s 57)? |
| Bigamy | Am I excused from a bigamy charge because my former marriage had been declared void (s 57)? |
| Attempts to procure abortion, and concealing the birth of a child | Could I have broken section 58 by taking, giving or using something to procure a miscarriage? |
| Attempts to procure abortion, and concealing the birth of a child | Could I have broken section 59 by supplying something to be used to procure a miscarriage? |
| Attempts to procure abortion, and concealing the birth of a child | Could I have broken section 60 by secretly disposing of a child's body to conceal its birth? |
| Gunpowder, and searches for it | Could having or making gunpowder or a dangerous thing amount to an offence under section 64? |
| Gunpowder, and searches for it | Can a justice of the peace issue a warrant to search my premises, carriage or vessel (s 65)? |
| Gunpowder, and searches for it | Can what is found on a search be seized, removed and detained (s 65)? |
| Offences on the water, and where the Act reaches | Am I liable to the same punishment for an offence on the water within the Admiralty's jurisdiction as for one on land (s 68)? |
| Offences on the water, and where the Act reaches | Does the Act reach what I did if I did it in Scotland (s 78)? |
| The most that can follow, for any offence of the Act | What is the most I could face if I am convicted of this offence? |
| The most that can follow, for any offence of the Act | Is this custodial sentence within the most the Act states for the offence? |

## What the stable binary does not accept

Observed with `l4` 1.6.98, and nothing else claimed:
- A constructor pattern with field names in `CONSIDER` (`WHEN ctor WITH field THEN`) is a parse error ("unexpected WITH"); the patterns are positional (`WHEN ctor x THEN`).

Forbidden by the brief for this binary, and respected (not probed here): `REFUSE`, `#ASSERT REFUSED`, `BECAUSE`, `YMD`, `TYPICALLY` on a field, section `GIVEN`, sets, `EVERY`, the ledger.
Also followed from the brief: every `NOT` is parenthesised, one `#ASSERT` per line, arithmetic bracketed across line breaks, `IMPORT` only of modules in this folder, no name defined in two imported modules is used, `JL4_LIBRARY_PATH` unset, and the diagnostics (not exit codes) are read.

My own slips while writing, which are ordinary L4 syntax and not stable-binary limits: parenthesised arguments in `CONCAT` (it is variadic with commas: `CONCAT "a", TOSTRING m, "b"`), and commas between the arguments of a function application (commas belong to `OF`).

## Rules without an @ref

The three arithmetic helpers in `oapa-table.l4` (`how a proposed term fits a stated term`, `how a proposed sentence fits one stated option`, `a proposed custodial sentence measured against the text`) cite no line: they compare a proposed term with figures the lookup above them already took from the text.
The layer-2 helpers in `oapa-seat.l4` (`the term in words` and its siblings) cite none either; layer 2 carries no `@ref` at all.
Every other layer-1 rule has one; the stub for section 76 has its `@ref` above a comment block.

## What check.sh prints

Run as `L4=l4 ./check.sh` from this folder (the `L4_TARGET` variable is accepted by `check.sh` and does nothing).
`check.sh` was extended from the pre-deposited copy with a `warnings` column and a `written` column, and goes red when warnings differ from refused assertions or when `written` is not the sum of satisfied, failed and refused.

```
module                             errors warnings written satisfied  failed  refused  expected
oapa-abortion-birth.l4                  0        0       0         0       0        0         0
oapa-assaults.l4                        0        0       0         0       0        0         0
oapa-bigamy.l4                          0        0       0         0       0        0         0
oapa-cases-seat.l4                      0        0     403       403       0        0         0
oapa-danger-bodily-harm.l4              0        0       0         0       0        0         0
oapa-danger-neglect-explosives.l4       0        0       0         0       0        0         0
oapa-danger-railways-vehicles.l4        0        0       0         0       0        0         0
oapa-gunpowder.l4                       0        0       0         0       0        0         0
oapa-homicide.l4                        0        0       0         0       0        0         0
oapa-nouns.l4                           0        0       0         0       0        0         0
oapa-other.l4                           0        0       0         0       0        0         0
oapa-seat.l4                            0        0       0         0       0        0         0
oapa-table.l4                           0        0       0         0       0        0         0
oapa-tests-abortion-birth.l4            0        0      29        29       0        0         0
oapa-tests-assaults.l4                  0        0      81        81       0        0         0
oapa-tests-bigamy.l4                    0        0      21        21       0        0         0
oapa-tests-danger-bodily-harm.l4        0        0      65        65       0        0         0
oapa-tests-danger-neglect-explosives.l4      0        0      65        65       0        0         0
oapa-tests-danger-railways-vehicles.l4      0        0      35        35       0        0         0
oapa-tests-gunpowder.l4                 0        0      19        19       0        0         0
oapa-tests-homicide.l4                  0        0      31        31       0        0         0
oapa-tests-other.l4                     0        0      17        17       0        0         0
oapa-tests-table.l4                     0        0     155       155       0        0         0
oapa-tests-threats.l4                   0        0      12        12       0        0         0
oapa-threats.l4                         0        0       0         0       0        0         0
TOTAL (25 modules)                      0        0     933       933       0        0
(a failed assertion is also an error, a refused one is also a warning; any other error or warning, any refused assertion, or written != satisfied+failed+refused, makes the run red)
```

Also run, and clean: `python3 -I srcrefs.py check --refs --strict ../../../../../registers/source-bundle/ukpga-Vict-24-25-100.txt oapa-*.l4` printed `0 problems`; no `zz-*` probe files remain; no marker lines remain in any `.l4` file.

Two instruments were given a positive control: a deliberately wrong assertion fails (four wrong assertions all printed "assertion failed"), and the field-read check in the seat generator was run against the earlier wrong section 9 question (which asked an input the called rule never reads) and reported it.

## How the seat and its cases were made

`oapa-seat.l4` and `oapa-cases-seat.l4` were first written by two small throwaway scripts that live outside this folder (in the run's scratch folder, not deposited; the brief says to write only under the deposit, and these scripts were written in the shared scratchpad before being moved to that folder at the end of the run).
The seat generator read the field list of each record from the layer-1 file, refused to run when a question gave the wrong number of entries, and checked transitively that every input a question asks is read by the rule it calls and that every placeholder is not.
The files in this folder are the output; they are the source of truth and may be edited by hand.
The expected values in the cases were decided from the text before the run and written beside the assertion.

## Before relying on this encoding

- A domain expert should read it against the official text, not this rendering.
- The penalty terms hidden by ". . ." (finding 2) need the official text or a consolidated source; today the encoding says "the text does not state" and the "most that can follow" is unknown for the seven offences whose penal servitude term is hidden (ss 20, 24, 26, 27, 31, 47, 59), and the imprisonment alternative is unknown for four more (ss 28, 29, 30, 32).
- Sections 1, 2, 5 (the elements), 6, 7, 11, 19, 41, 43, 46, 48-50, 52-54, 56, 61, 66, 69-74, 77 and 79 are blank in the deposit; a fuller source is needed for murder and manslaughter in particular (finding 6).
- The forks marked in the register need a ruling where they change an answer: 26a, 31a, 36a, 57c, 58a, 64a, 68a and 78a.
- Sections 9 (the pre-Act manner of trial abroad) and 65 (the borrowed powers) point at other texts that should be added as inputs.
- The seat for the party aggrieved (sections 42 to 45) is not built.
- The wording of every `@desc` has not been tested on a real person.


## Added after the run: the date as data

`oapa-enactment.l4` was added by the lead after the agent finished, at the maintainer's request that the date of enactment be kept as data for rule-effective-date logic.
It is one definition with a quoted source line and an `@ref`; no rule reads it yet.
