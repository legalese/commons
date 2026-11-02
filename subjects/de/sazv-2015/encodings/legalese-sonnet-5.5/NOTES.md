# NOTES -- Soldatengesetz § 30c and Soldatenarbeitszeitverordnung § 1 (time off for soldiers' overtime), L4 encoding by agent `saz` (Sonnet 5.5, solo)

This encodes the right of a soldier to time off for ordered overtime (SG § 30c(2)), the exemption that takes soldiers posted to listed international establishments out of it (SAZV § 1(2) and its Anlage), the power that exemption needs (SG § 30c(6) with § 93(2) no. 7), and the constitutional test that the article by Felix Ringe and Linus Folkerts says the 2025 recast of the annex fails.
It does not decide whether the test is failed: it answers the soldier's question under both readings and says which facts each rests on.
On the reading where the 2025 recast is void, the annex that stands is the 2022 one (41 rows), not "the 2025 annex without JSEC" (finding 1).

The sources are in `../../registers/source-bundle/`: plain-text conversions of per-norm pages of gesetze-im-internet.de read on 2026-11-02, the gazette texts and PDFs of the 2025 and 2022 amending regulations, excerpts of the court decisions the article cites, and an excerpt of BVerfG 2 BvF 3/90, each with its `.meta.json`.
The consolidated texts are the site's reading versions; the gazette is the promulgated text.
The target is `main`: the build compared with is 1.6.108 (main, 2ae7c9b, 2026-11-02).
Modules: `saz-law.l4` (the law layer), `saz-seat.l4` (the seat), `saz-tests.l4` and `saz-cases-seat.l4`.

## Seat

The seat is **a soldier serving within the remit of the Federal Ministry of Defence**: the person SG § 30c and SAZV § 1 are applied to.
Their questions, in `saz-seat.l4`, under `§` groups:

- Do § 30c(1) to (3) of the Soldiers Act, which give time off for overtime, apply to me, reading the annex as it is printed? And if the 2025 recast of the annex is void? (the second group only arises for a soldier posted to one of the roughly fifty establishments the 2025 annex lists and the 2022 annex did not; the group's comment says so)
- How many hours of time off must I be given for this month's overtime, on each reading?
- Within how many months must the time off be given (12, or 6 where the shorter period for soldiers in the armed forces has been set)?
- Does the preamble of the 2025 amending regulation cite § 30c(6) with § 93(2) no. 7?

The inputs are facts the soldier can state: whether they serve within the Ministry's remit, the establishment where they are posted (as the annex prints its name), whether they were assigned there for international tasks, whether the work is an activity listed in § 30c(4), the overtime hours, and the hours that compelling service reasons make impossible.
"An activity listed in § 30c(4)" is a characterisation asked as a fact: the list (operations, disaster aid, multi-day sea voyages, ...) is long and its edges are judgments.
The people the text also addresses are the Ministry (it issues the regulation) and the unit commander (who orders or refuses time off): neither has a seat.

## Method

One agent, working alone, from the deposited sources and the article.
`saz-law.l4` holds the nouns (`Soldier`, `Annex row`), both annexes as data (88 rows from the site's annex, generated from lines 4 to 91 of `sazv-anlage.txt`; 41 rows from the 2022 gazette, generated from the table in lines 322 to 371 of `bgbl-2022-i-34.txt`; both checked by count and by rows), the exclusion of § 1(2), the entitlement of § 30c(2), the period, and the citation test of Art. 80(1) sentence 3 GG with the powers the 2015, 2022 and 2025 preambles cite.
`saz-seat.l4` holds no rule: it builds the law layer's record from plain inputs and calls the law layer.
The only field it does not ask is `has a long-term working-time account`, set to a fixed `FALSE` and commented: no seat question reads it (SAZV § 1(3) is encoded in the law layer and tested, but not exported, because § 17 SAZV is not deposited).
Every rule has an `@ref` with locators; `srcrefs.py` checked 25 quote lines and 18 locators, 0 problems.
The tests' expected values were written from the German text, not from this encoding's output.

## Coverage table

| provision | disposition | where, or why |
|---|---|---|
| SG § 30c(1) | out-of-scope | the 41-hour week and the exceptions for senior officers: the overtime is taken as a number the soldier states |
| SG § 30c(2) sentences 1 to 3 and 5 | encoded | `the soldier is entitled to time off for overtime under the reading`, `the hours of time off to be given under the reading`, `the months within which time off must be given` |
| SG § 30c(2) sentence 4 (the Dienstherr may order the time off) | inert | a power over the soldier; no question turns on it |
| SG § 30c(3) | out-of-scope | on-call duty (Bereitschaftsdienst) and the 54-hour week in medical facilities: not part of the question |
| SG § 30c(4) | encoded | the soldier states whether the work is one of the listed activities; if so, (1) to (3) do not apply |
| SG § 30c(5) | inert | the power to regulate working time; named in the 2025 preamble list |
| SG § 30c(6) | encoded | `the power needed to exempt a group of soldiers` |
| SG § 30d(1), (2) | inert | named in the 2025 preamble list; sentence 3 of (1) says § 30c(1) to (3) "bleibt unberührt", so § 30d is not an exemption power (`sg-30d.txt:8`) |
| SG § 93(2) nos. 6, 8 | inert | named in the 2025 preamble list (no. 6 also in the 2022 one) |
| SG § 93(2) no. 7 | encoded | the power to make the regulation that disapplies § 30c(1) to (3) and (5) |
| SG § 93(1), (2) nos. 1 to 5 and 9, (3), (4) | out-of-scope | other powers |
| SAZV § 1(1) | encoded | `the Regulation applies to the soldier under the reading` |
| SAZV § 1(2) | encoded | `section 1(2) SAZV takes the soldier out of the working-time rules under the reading` |
| SAZV § 1(3) | encoded | `the soldier's long-term working-time account is suspended under the reading`; not exported |
| SAZV Anlage as recast in 2025 (88 rows) | encoded | `the rows of the annex as printed` |
| SAZV Anlage as recast in 2022 (41 rows) | encoded | `the establishments in the 2022 annex`, the second reading |
| SAZV Eingangsformel (the original 2015 preamble) | encoded | `the powers cited in the original preamble of the SAZV` |
| SAZV §§ 2 to 21 and the rest | out-of-scope | the Regulation's working-time machinery; the question is whether a soldier is out of it |
| BGBl. 2025 I Nr. 78, preamble | encoded | `the powers cited in the preamble of the 2025 amending regulation` |
| BGBl. 2025 I Nr. 78, Art. 5 No. 7 (the Anlage recast) | inert | the annex is encoded as data; see finding 1 |
| BGBl. 2025 I Nr. 78, Arts. 1 to 4, 5 Nos. 1 to 6, 6, 7 | out-of-scope | other amendments |
| BGBl. 2022 I Nr. 34, preamble | encoded | `the powers cited in the preamble of the 2022 amending regulation` |
| BGBl. 2022 I Nr. 34, Art. 4 (§ 1(2) and the 41-row Anlage) | encoded | `the establishments in the 2022 annex` |
| BGBl. 2022 I Nr. 34, other articles | out-of-scope | other amendments (long-term accounts, flexitime, § 5a) |
| Grundgesetz Art. 80(1) sentence 3 | encoded | `the preamble cites the power`, `the 2025 recast of the annex is void for want of citation` |
| Grundgesetz Art. 80(1) sentences 1, 2 and 4, (2) to (4) | out-of-scope | not argued |
| BVerfG 2 BvF 3/90, paras. 151 to 158 | inert | the source of the citation rule |
| BVerwG 3 B 51.18 paras. 33 to 35; BVerwG 2 C 31.15 paras. 26 to 33; OVG NRW 3 A 1217/14 paras. 105 to 123 | inert | the cases the article cites on the earlier-citation exception (finding 6) |

## Fork register

Each fork gives the readings, the one taken, and the text that licenses each.

**F1. Which reading answers?**
(a) *As printed*: the 2025 annex, 88 rows, JSEC at No. 27. What the unit applies today.
(b) *As in the 2022 annex*: the 2025 recast is void and the annex stands as the 2022 regulation printed it, 41 rows, with no JSEC.
Taken: **both**, as separate questions, because no court is known to have ruled on (b); the article says it found the point itself.

**F2. How far does the voidness go?**
(a) The whole recast annex. The 2025 regulation does not "add" JSEC: Art. 5 No. 7 says "Die Anlage zu § 1 Absatz 2 wird wie folgt gefasst" and prints all 88 rows (`bgbl-2025-i-78.txt:176-283`). If the defect voids what the regulation enacted, the whole recast falls and the 2022 annex returns. Encoded as reading (b). The article's own argument therefore reaches every establishment new in 2025, about fifty, not only JSEC (finding 1).
(b) JSEC alone: "the 2025 annex without JSEC". Not encoded: it would be an annex that no regulation ever printed. Earlier drafts of this encoding did this; it was wrong once the 2022 gazette was read.
(c) The whole amending regulation: BVerfG 2 BvF 3/90 para. 158 speaks of "die Verordnung" (`bverfg-2bvf3-90-paras-151-158.txt:65-71`).
Taken: (a).

**F3. Exceptions to the citation requirement.**
The article lists three follow-up considerations for Case 3 and rejects each; the encoding has one input, `an exception applies`, that stands for the judgments they call for:
- *The exemption is covered by other cited legal bases.* The article says no: § 30c(5) sentence 1 no. 2 concerns protective measures for the activities of § 30c(4), and § 30d(1) leaves § 30c(1) to (3) untouched. Both are true of the deposited text (`sg-30c.txt:23-29`, `sg-30d.txt:8`), and the encoding's test is membership of the needed power in the cited list, so it reads as the article does.
- *If the new rule is void, JSEC remains exempt under the predecessor rule.* The article says no, because the previous annex did not list it. Verified from the 2022 gazette PDF: JSEC is not among its 41 rows (`bgbl-2022-i-34.txt:322-371`).
- *Earlier citations suffice for a limited amendment.* The article says "highly unlikely" and gives as its reason that the original 2015 preamble cites only § 30c(5) with § 93(2) no. 5. **The article does not mention that the 2022 regulation, which gave § 1(2) its present wording and recast the annex to 41 rows, was itself made "Auf Grund des § 93 Absatz 2 Nummer 6 und 7 des Soldatengesetzes"** (`bgbl-2022-i-34-flow.txt:9-13`, Art. 4 from line 318 of `bgbl-2022-i-34.txt`, in force 1 October 2022): no. 7 is the exemption power. So the regulation as amended in 2022 did carry a citation of the exemption power, which is the shape of the exception the article discusses. Against it: the 2022 preamble names § 93(2) no. 7 but not § 30c(6) (the article's test is "§ 30c(6) with § 93(2) no. 7"; no. 7 itself points to § 30c(6), `sg-93.txt:20`); and the 2025 recast re-enacts an 88-row annex with about fifty new rows, which may not be a limited amendment. The court decisions are read in finding 6. Open: not decided here.
**The input is a legal judgment left to someone else: `TRUE` makes the 2025 annex stand.**

**F4. "Diese Mehrarbeit" in § 30c(2) sentence 2.**
(a) All the ordered overtime, once more than five hours are reached (the article's reading, and the one encoded: ten hours give ten hours).
(b) Only the hours above five. The words "für diese Mehrarbeit" refer back to the overtime that exceeded five hours, which can be read either way. Tests assert 5 gives 0, 5.5 gives 5.5, 6 gives 6.

**F5. Renamed rows.**
Under the 2022 reading a soldier's establishment is matched by name. Five 2022 names are not in the 2025 annex: "European Union Military Committee", "NATO Alliance Ground Surveillance Force", "NATO Military Committee", "Joint Chemical Biological Radiological Nuclear Defence Centre of Excellence" and "NATO Communications and Information Agency (Anteil Norfolk)". The last two look like the 2025 rows "Chemical, Biological, Radiological and Nuclear Centre of Excellence" (No. 9) and "NATO Communications and Information Agency Norfolk" (No. 52). The encoding **assumes, not rules,** that they are the same establishments (`the 2025 spellings taken to be 2022 rows under another name`); neither regulation says so. The first three have no 2025 counterpart by name.

**F6. "Soweit" in sentence 5**, "Eine Dienstbefreiung wird nicht gewährt, soweit sie aus zwingenden dienstlichen Gründen nicht möglich ist", is read as a reduction by the number of hours so blocked, not as an all-or-nothing bar.

**F7. The remit.**
§ 30c(1) sentence 1 ties the 41-hour week to soldiers "im Geschäftsbereich des Bundesministeriums der Verteidigung verwendet", and sentence 3 sends others to the receiving body's law. § 30c(2) says only "der Soldat". The encoding asks the remit only for SAZV § 1(1), and treats § 30c(2) as applying to any soldier not excluded and not in a § 30c(4) activity.

**F8. The six-month period** ("kann ... verkürzt werden") is taken as an input: the soldier says whether it has been set for them.

## What the law turns out to say

1. **Both the 2022 and the 2025 regulations recast the whole annex, and 2025 added about fifty rows.** The 2022 annex has 41 rows (`bgbl-2022-i-34.txt:322-371`); the 2025 annex has 88 (`bgbl-2025-i-78.txt:176-283`, the site's annex has the same 88). 36 names appear in both; five 2022 names are not in 2025 (F5); 52 rows of the 2025 annex are not in the 2022 annex by exact name, about fifty after the two assumed renames. NATO Force Integration Unit (six rows), the NATO Communications and Information Agency rows, and JSEC are among them. The article's "amended to add JSEC" describes one of about fifty. Asserted in `saz-tests.l4`.
2. **The 2025 preamble names eight powers and not § 30c(6) or § 93(2) no. 7.** It names BBesG § 50b(1), § 56(6) and § 53(7); BBG § 83(4); BUKG § 14(1) sentence 1 and (3) no. 7; SG § 30c(5) sentence 1 no. 2 with (4) and § 93(2) no. 6; SG § 30d(1) sentence 1 with § 93(2) no. 8; and ArbSiG § 38(1) (`bgbl-2025-i-78.txt:14-50`). Asserted.
3. **The 2022 preamble names § 93(2) nos. 6 and 7; the original 2015 preamble does not.** The 2015 one names "§ 30c Absatz 5 in Verbindung mit § 93 Absatz 2 Nummer 5" (`sazv-eingangsformel.txt:2`). The article cites the 2015 one; the 2022 one is what F3 turns on. Asserted.
4. **§ 93(2) no. 7 reaches subsection (5) as well**: "die Nichtanwendung des § 30c Absatz 1 bis 3 und 5 nach § 30c Absatz 6" (`sg-93.txt:20`). The exemption removes the soldier from the Regulation made under (5) as well as from the three subsections.
5. **Not every annex row is obviously a multinational establishment.** § 30c(6) reaches soldiers "bei militärischen Stellen ..., in denen Teile von Streitkräften mehrerer Staaten zusammengeschlossen sind". Rows such as No. 41 and No. 42 ("Ministery of Defense", Lithuania and Netherlands), No. 6 (Canadian Forces College) and No. 81 (United States Air Force Academy) read as national bodies. The article does not raise this, and the encoding does not test it: it is a different possible defect (the scope of the power, not its citation), and for a domain expert.
6. **What the court decisions the article cites say, read on 2026-11-02.**
   - *BVerwG 3 B 51.18, para. 35* (`bverwg-3b51-18-excerpt.txt:7`) restates the rule the article uses: the power claimed must arise "gerade aus den von ihr selbst angeführten Vorschriften", and a regulation resting on several powers must cite them all. It also holds that where the whole of a multi-paragraph power is used, the preamble need not list its sentences: "Es ist nicht erforderlich, alle Untergliederungen einer Ermächtigungsgrundlage aufzuzählen, wenn sie alle in Anspruch genommen werden". That relief is about sentences within a cited paragraph; § 30c(6) is a different paragraph from the cited § 30c(5), so it does not help the 2025 preamble.
   - *BVerwG 2 C 31.15, paras. 27 to 33* (`bverwg-2c31-15-excerpt.txt:5-17`) concerns the Zitiergebot of the North Rhine-Westphalia constitution (Art. 70 sentence 3), which the court says is not reviewable on appeal on points of law and is not a principle the Basic Law requires of the Länder (paras. 28 to 30). It leaves the OVG's view undisturbed because it is not arbitrary (para. 33, `:17`). It therefore decides nothing about Art. 80(1) sentence 3 GG itself, as the article says.
   - *OVG NRW 3 A 1217/14, paras. 105 to 123*: no breach where the second amending regulation did not cite the power again, because it made only "punktuelle" changes whose content can only be understood through the original regulation, whose preamble cites the power (`ovg-nrw-3a1217-14-excerpt.txt:4-6`); no new subject matter was introduced (para. 113, `:10`); it only changed existing percentages (para. 120, `:17`); and citation requirements are not to harden into mere formalities (para. 121, `:18`). The article's reason for distinguishing it ("adding JSEC extends the exemption to a new group") is a reading of para. 113; see F3 for the 2022 preamble the article did not consider.
7. **Where the 2022 text came from.** The bgbl.de archive answered curl with an HTML shell that needs JavaScript. The document was opened in a Chrome session that Meng directed me to drive, and Meng saved the PDF from the viewer (`bgbl-2022-i-34.pdf`; text extracted with pdftotext both as laid out, `bgbl-2022-i-34.txt`, and in reading order, `bgbl-2022-i-34-flow.txt`). A transcription I had made earlier from the browser's text layer was checked against it: every line matched, and the 41 annex names generated from the PDF text are the same 41 I had transcribed. Commons guide §8 treats a bot challenge as a "no" and says never to work around one; the browser read was used with the owner's agreement and the guide is Michael's, so whether that is acceptable is for him to say.

## Answer table

| soldier | time off for 10 hours of ordered overtime, as printed | if the 2025 recast is void (2022 annex) |
|---|---|---|
| at JSEC or any of the ~50 other rows new in 2025, assigned for international tasks | 0 hours | 10 hours |
| at SHAPE (2022 No. 39, 2025 No. 76) or another row in both annexes, assigned for international tasks | 0 hours | 0 hours |
| at a row listed under another name in 2022 (F5), assigned for international tasks | 0 hours | 0 hours (assumed) |
| at JSEC, not assigned for international tasks | 10 hours | 10 hours |
| at an establishment not in either annex | 10 hours | 10 hours |
| in a § 30c(4) activity | 0 hours | 0 hours |

## Checks run

`./check.sh` in this folder, target `main`, on 2026-11-02 (the `l4` is a dev build, 25a091f4...; the main build compared with is 1.6.108 (main, 2ae7c9b, 2026-11-02)):

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.108 (main, 2ae7c9b, 2026-11-02)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
saz-cases-seat.l4                              0        14       0        0         0 |      0        14       0        0  same
saz-law.l4                                     0         0       0        0         0 |      0         0       0        0  same
saz-seat.l4                                    0         0       0        0         0 |      0         0       0        0  same
saz-tests.l4                                   0        58       0        0         0 |      0        58       0        0  same
TOTAL (4 modules)                              0        72       0        0           |      0        72       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

`python3 -I srcrefs.py check --refs ../../registers/source-bundle/sazv-1.txt saz-law.l4`: 25 src: lines, 10 runs, 18 locators, 0 problems.
No assertion is expected to fail. The check does not see a different trace outcome; the encoding has no regulative rule and no `#TRACE`.

## Before this is worth relying on

- Decide F3 and the 2022-preamble point with someone who knows German administrative law, and check finding 5 against § 30c(6) and the annex, row by row.
- Have a domain expert read the encoding against the German text (the pipeline's HG1).
