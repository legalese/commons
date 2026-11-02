# NOTES -- Aufenthaltsverordnung § 26 and Anlage C (the airport transit visa), L4 encoding by agent `atv` (Sonnet 5.5, solo)

This encodes the rule that makes nationals of the states in Anlage C hold an airport transit visa to change planes at a German airport, the power it rests on, and the constitutional test that the article by Felix Ringe and Linus Folkerts says the 2015 amendment of Anlage C (Mali) fails.
It does not decide whether the test is failed: it answers the traveller's question under both readings, and says which facts each reading rests on.

The sources are in `../../registers/source-bundle/`: plain-text conversions of per-norm pages of gesetze-im-internet.de read on 2026-11-02, the gazette texts and PDFs of the 2015, 2023 and 2026 amendments of Anlage C, and an excerpt of Art. 3 and Annex IV of the Visa Code checked against the EUR-Lex page the owner saved, each with its `.meta.json`.
The consolidated texts are the site's reading versions, not the gazette.
The target is `main`: the build compared with is 1.6.108 (main, 2ae7c9b, 2026-11-02).
Modules: `atv-law.l4` (the law layer), `atv-seat.l4` (the seat), `atv-tests.l4` and `atv-cases-seat.l4`.

## Seat

The seat is **a person changing planes at a German airport**: the traveller to whom § 26 AufenthV is applied.
Their questions, in `atv-seat.l4`, in the text's order under `§` groups:

- § 26(2) sentence 1: Must I hold an airport transit visa to change planes at a German airport, reading Annex C as it is printed?
- § 26(1) and (2) sentence 2: Am I exempt from needing a residence title while I wait in the transit area, reading Annex C as it is printed?
- the same two questions, **if Article 1 No. 10 of the 2015 amending regulation is void** (a group that only arises if the traveller's state is Mali, South Sudan or Myanmar: the heading's comment says so, so a form can ask first)
- Does the preamble of the 2015 amending regulation cite § 99(3a) AufenthG?

The inputs are facts the traveller can state: nationality, whether they stay in the transit area, whether they hold a visa, whether an Art. 3(5) exemption applies, and, for Jordan and Türkiye, the facts Anlage C asks.
Visa Code Annex IV is worked out from the nationality (the twelve states of the 28.06.2024 consolidation).
Art. 3(5) is asked as one fact because its six categories are documentary: a visa or residence permit, family status, a diplomatic passport, flight crew.
The people the text also addresses are officials (the ministry that issues the regulation, the border police who check the visa): they have no seat.

## Method

One agent, working alone, from the deposited sources and the article.
`atv-law.l4` holds the nouns (`Transit passenger`), Anlage C as data, the two exemptions written into it, Annex IV, the two limbs of § 26(2) sentence 1, § 26(1) with sentence 2, and the citation test of Art. 80(1) sentence 3 GG with the powers the 2015, 2023 and 2026 preambles cite.
`atv-seat.l4` holds no rule: it builds the law layer's record from plain inputs and calls the law layer.
Every rule has an `@ref` with locators, and the quotations were pasted by script from the deposited files and checked with `srcrefs.py` (71 quote lines, 16 locators, 0 problems).
The tests' expected values were written from the German and English texts, not from this encoding's output.
On early runs one assertion failed and some calls had the wrong number of inputs; each was my own transcription of argument positions, and no expectation was edited to match an output.

## Coverage table

| provision | disposition | where, or why |
|---|---|---|
| AufenthV § 26(1) | encoded | `the traveller is exempt from the residence-title requirement under the reading` |
| AufenthV § 26(2) sentence 1, first limb (Visa Code Art. 3(1) with (5)) | encoded | `the traveller must hold an airport transit visa under the reading`, with Annex IV derived and Art. 3(5) asked as a fact |
| AufenthV § 26(2) sentence 1, second limb (Annex C states, unless Art. 3(5)) | encoded | same rule |
| AufenthV § 26(2) sentence 2 | encoded | the exemption of § 26(1) holds only for a holder, where a visa is required |
| AufenthV § 26(2) sentence 3 (the visa is not a residence title) | inert | quoted in the deposit; no question turns on it |
| AufenthV § 26(3) (weggefallen) | inert | repealed |
| AufenthV Anlage C, the eight states | encoded | `the states listed in Annex C as printed` |
| AufenthV Anlage C, Jordanien exemption | encoded | `Annex C exempts the traveller from the airport transit visa requirement` |
| AufenthV Anlage C, Türkei exemption | encoded | same rule |
| AufenthG § 99(3a) | encoded | `the power needed to add a state to Annex C` |
| AufenthG § 99(1) and (2) | inert | named in the 2015 preamble list as powers cited; their content is not encoded: the point is that none of them is (3a) |
| AufenthG § 99(3) and (4) | out-of-scope | other powers (naming the body under §§ 73 and 73a; short-lived regulations); the article does not rely on them |
| Grundgesetz Art. 80(1) sentence 3 | encoded | `the preamble cites the power`, `the 2015 amendment of Annex C is void for want of citation` |
| Grundgesetz Art. 80(1) sentences 1, 2 and 4, (2) to (4) | out-of-scope | the power must be given by statute with its content, purpose and extent fixed: the article does not argue that § 99(3a) fails that |
| BVerfG 2 BvF 3/90, paras. 151 to 158 | inert | the source of the rule that the citation must name the individual provision and that a breach makes the regulation void |
| BGBl. 2015 I Nr. 54, preamble | encoded | `the powers cited in the preamble of the 2015 amending regulation` |
| BGBl. 2015 I Nr. 54, Art. 1 No. 10 (Anlage C: Myanmar out, Mali in, Südsudan in) | encoded | `the states the 2015 amending regulation added`, `the state the 2015 amending regulation took out`, the second reading |
| BGBl. 2015 I Nr. 54, Art. 3(3) and the signature block | inert | in force the day after promulgation (28 Dec 2015, so 29 Dec); the Bundesrat consented |
| BGBl. 2023 I Nr. 201 (Kuba inserted) and 2026 I Nr. 161 (Indien struck) | encoded | their preambles, as `the powers cited in the preamble of the 2023 / 2026 amending regulation`; Anlage C as printed already carries both changes |
| EU Visa Code, Art. 3(1), (5) and Annex IV (consolidated 28.06.2024) | encoded | `the states in Annex IV of the Visa Code`; Art. 3(5) as one asked fact |
| EU Visa Code, Art. 3(2) to (4) (national additions, notification) | inert | quoted in the deposit; a notification does not enter § 26(2) (fork F3) |
| AufenthG § 13(2) (what counts as entering) | out-of-scope | asked as the fact "stays only in the transit area" |
| the rest of AufenthV; AZRG § 40; Verwaltungskostengesetz; the rest of the Visa Code | out-of-scope | not part of the question |

## Fork register

Each fork gives the readings, the one taken, and the text that licenses each.
The article's own "potential follow-up considerations" for Case 2 are listed here with what this encoding does with them.

**F1. Which reading answers?**
(a) *As printed*: the regulation is applied as written, and Mali is listed.
(b) *As if the 2015 amendment of Annex C had not been made*: Article 1 No. 10 is treated as one instruction that fails as a whole, so Myanmar is listed again and Mali and South Sudan are not.
Taken: **both**, as separate questions, because no court is known to have ruled on (b) (the article says it found the point itself and that, to its knowledge, none of its vulnerabilities was previously recorded).
The answer an officer applying the rule today would give is (a).

**F2. How far does the voidness go?**
(a) The whole of Article 1 No. 10, which is one sentence of two operations ("In Anlage C wird das Wort „Myanmar“ durch das Wort „Mali“ ersetzt und wird nach dem Wort „Sudan“ das Wort „Südsudan“ eingefügt", `bgbl-2015-i-54.txt:75-76`). Encoded as reading (b): the previous annex comes back, Myanmar in it.
(b) Only the additions, with the removal of Myanmar surviving as severable. Not encoded: it would leave Myanmar out and Mali and South Sudan out, a state the gazette never had. The article does not discuss the point, and its sentence "the previous Annex C listed neither Mali nor South Sudan" is true of the previous annex only because that annex had Myanmar instead. A defence brief written on 2026-11-02 (a Sonnet agent arguing the Ministry's side, files only) grades the Myanmar deletion as severable and valid on any view, because it widens an exemption, which § 99(1) no. 1 plainly covers, and puts the chance of a court voiding it under 15%; so (b) now has the better argument, and (a) stays encoded only because it is the reading on which the article's "void" is one instruction.
(c) The whole 2015 amending regulation: BVerfG 2 BvF 3/90 para. 158 speaks of "die Verordnung" (`bverfg-2bvf3-90-paras-151-158.txt:65-71`), which would reach its other provisions as well. The article does not argue it.
The encoding follows (a) because it is the reading that treats No. 10 as one provision, which is how the article's "void" is applied; the answer table shows the consequence for Myanmar nationals.

**F3. Exceptions to the citation requirement.**
The article lists five follow-up considerations for Case 2 and rejects each. What the encoding does with them:
- *Other cited powers cover it* ("The visa requirement is covered by other cited legal bases"). The article says no: the cited powers concern residence-title exemptions, procedures, fees, documents and register data. The encoding's test is membership of `AufenthG 99(3a)` in the cited list, so it reads as the article does. A court might read § 99(1) no. 1 (exemptions from the residence title) as covering a visa duty; the encoding cannot say. **This is the point Case 2 turns on, and the record is fuller than the article's one sentence.** Before § 99(3a) existed, the Interior Ministry amended Anlage C by regulation under § 99(1) no. 1: the Dritte Verordnung zur Änderung der Aufenthaltsverordnung of 8 May 2008 added "Myanmar" to Anlage C and its preamble cites, for the Ministry, only "§ 99 Abs. 1 Nr. 1 des Aufenthaltsgesetzes" (`bgbl-2008-i-806-excerpt.txt:4` and `:15-17`, a transcription from umwelt-online.de). § 99(3a) was inserted by Art. 1 No. 56(c) of the Act of 22 November 2011 (BGBl. I S. 2258, in force 26 November 2011; lexetius.com version list, buzer.de text), and the bill's memorandum says the states for which Germany uses the Visa Code's Art. 3(2) option "werden nach § 99 Absatz 3a des Aufenthaltsgesetzes durch das Bundesministerium des Innern im Einvernehmen mit dem Auswärtigen Amt durch Rechtsverordnung ohne Zustimmung des Bundesrates festgelegt" (`btd-17-5470-p30-33.txt`, p. 33, zu Nummer 3 (§ 26)). The same 2011 Act itself recast § 26(2) (adding sentence 3, "Das Flughafentransitvisum ist kein Aufenthaltstitel") and replaced Anlage C in full by statute (Art. 12); buzer.de's text of the Act shows no clause returning those parts to Verordnungsrang. So the question is whether, after 2011, no. 1 survives as an alternative basis for the list, or (3a) displaces it as the specific power with its own procedure (Einvernehmen with the Foreign Office, no Bundesrat); the 2015 regulation has the no. 1 form (Bundesrat consent, no Einvernehmen stated), the 2023 and 2026 ones the (3a) form.
- *The previous rule still requires the visa*: the previous Anlage C listed neither Mali nor South Sudan, as the article says (its footnote 12); it listed Myanmar (F2). Encoded as reading (b).
- *Germany's notification to the Commission under Art. 3(2) of the Visa Code replaces the regulation*: the article says no; § 99(3a) says the Ministry names the states by regulation "nach Maßgabe von Artikel 3 Absatz 2", and Art. 3(2) lets a Member State require the visa for other states in urgent cases of mass influx and notify the Commission (`visacode-excerpt.txt:6`). The notification does not enter § 26(2), whose second limb reaches only Annex C states, so it changes no answer here.
- *Later amendments cured it*: the article says no. Read from the gazettes: the 2023 regulation inserts "Kuba" and the 2026 regulation strikes "Indien"; each cites § 99(3a) in its preamble (`bgbl-2023-i-201.txt:12-16`, `bgbl-2026-i-161.txt:12-17`); neither mentions Mali or South Sudan. Tested.
- *EU law independently requires the visa*: the article says no, because neither state is in Annex IV of the Visa Code. Verified against the 28.06.2024 consolidation: Annex IV lists Afghanistan, Bangladesh, the Democratic Republic of the Congo, Eritrea, Ethiopia, Ghana, Iran, Iraq, Nigeria, Pakistan, Somalia and Sri Lanka (`visacode-excerpt.txt:19-30`). The first limb uses that list, so a Nigerian national needs the visa under both readings (tested).
Separately, a general exception to the citation requirement is the input `an exception applies`: `TRUE` makes the 2015 amendment stand.
The exception the article discusses under Case 3, that a limited amending regulation need not cite the power again if the original regulation's preamble did, rests on OVG NRW 3 A 1217/14 (read: see the SAZV subject's NOTES, finding 6). For this regulation the point is thin: the AufenthV's own preamble is not deposited (the site has no Eingangsformel page for it), so whether the 2004 preamble named § 99(3a) is not known.

**F4. "Der Weiterflug muss innerhalb von zwölf Stunden ..." (Anlage C, Jordanien).**
It is a separate sentence after (a) and (b). Taken: it applies to the exemption as a whole, both (a) and (b), and the tests assert that (a) or (b) alone is not enough.
The other reading, that it qualifies only (b), is open on the text.

**F5. "Stays only in the international transit area"** stands for the text's "ohne im Sinne des § 13 Abs. 2 des Aufenthaltsgesetzes einzureisen" (§ 26(1)). § 13(2) is not deposited, so entry is asked as one fact.

**F6. Annex C's own exemptions (Jordan, Türkiye) are limited to Annex C.**
They are written into the annex and do not reach the first limb (Annex IV states). The tests do not combine them, and Annex IV and Annex C do not overlap on the deposited lists.

**F7. "Sofern diese nicht nach Artikel 3 Absatz 5 ... befreit sind"** (second limb) is read as removing Annex C nationals who fall in an Art. 3(5) category.
The text can also be read as removing them only from the first limb; the words follow the second-limb clause, and are encoded there.

**F8. No date axis.**
Anlage C is encoded as printed on 2026-11-02, with the 2023 addition of Kuba and the 2026 removal of Indien already in it (both read from the gazettes).
A traveller asking about a date between 29 Dec 2015 and the 2026 amendment would get a wrong answer for India and, before the 2023 amendment, for Cuba.
Reading (b) assumes there was no other amendment of Anlage C between 2015 and today beyond those two; amendments between 2015 and 2023 were not checked.

## What the law turns out to say

1. **Sentence 2 of § 26(2) turns the visa into a condition of the transit exemption.** A traveller in the transit area who is within the visa duty but has no visa is not covered by § 26(1) at all (asserted in `atv-tests.l4`). The article speaks of "avoiding the visa procedure and its cost"; the text's own consequence of the duty is that no visa means no exemption from the residence-title requirement. Asserted.
2. **The 2015 preamble cites § 69(2) and (3) nos. 4 and 6 with the Verwaltungskostengesetz, § 99(1) nos. 1 to 3 and 13a, § 99(2) sentence 2 with sentence 1 no. 1, and § 40(1) nos. 1, 4 and 5 AZRG. None is § 99(3a).** Read from the gazette (`bgbl-2015-i-54.txt:12-21`), matching the article's quotation word for word. Asserted in `atv-tests.l4`, with controls: the 2023 and 2026 preambles, which do cite (3a), test as cited.
3. **Where the 2015 gazette and the Visa Code text came from.** The bgbl.de archive answered curl with an HTML shell that needs JavaScript, and EUR-Lex answered curl with HTTP 202 and an empty body. Both were opened in a Chrome session that Meng directed me to drive. Meng saved the 2015 PDF from the viewer (`bgbl-2015-i-54.pdf`, text extracted with pdftotext) and the EUR-Lex page with Cmd+S; the page is not committed because EUR-Lex's reuse terms are undetermined, and `visacode-excerpt.meta.json` records its sha256. A transcription I had made earlier from the browser's text layer was checked line by line against both: all 17 gazette lines and all 27 Visa Code lines matched. The 2023 and 2026 gazettes were fetched directly from recht.bund.de, and their PDFs are deposited. Commons guide §8 treats a bot challenge as a "no" and says never to work around one; the browser read was used with the owner's agreement and the guide is Michael's, so whether that is acceptable is for him to say.
4. **Article 1 No. 10 is a replacement, and that changes the "void" reading.** The article says the regulation "added" Mali. The gazette says "Myanmar" was replaced by "Mali" and "Südsudan" inserted after "Sudan" (`bgbl-2015-i-54.txt:75-76`). If No. 10 fails as a whole, Myanmar nationals need the visa again (tested). The article's "no" to "if the amendment is void, the previous rule still requires the visa" is right about Mali and South Sudan and silent about Myanmar.
5. **BVerfG 2 BvF 3/90 supports the article's engine and differs from it in one word.** Paragraph 151: the citation must name "die ermächtigende Einzelvorschrift" and, where the regulator wants to use several powers, "vollständig". Paragraph 154: the power claimed must arise "gerade aus den von ihr selbst angeführten Vorschriften". Paragraph 158: the defect makes "die Verordnung" void. The article says "provisions ... not covered by the cited legal basis are void" (F2).
6. **Anlage C as printed has eight states** (counted by `atv-tests.l4`), including Kuba and excluding Indien, matching the article's footnote 13, which the two gazettes confirm.
7. **The 2015 preamble does not say "im Einvernehmen mit dem Auswärtigen Amt"**; § 99(3a) authorises the Interior Ministry "im Einvernehmen mit dem Auswärtigen Amt". The 2023 and 2026 preambles say it. The article does not raise this and the encoding does not test it; it may be a second formal point.
8. **Two ministries' names in § 99.** The deposited § 99(1) says "Bundesministerium des Innern und für Heimat" and § 99(2) to (4) say "Bundesministerium des Innern, für Bau und Heimat", the names current at different amendments. No question turns on it.

## Answer table

| nationality (no exempting document, in transit only) | must hold the visa, as printed | if Art. 1 No. 10 of the 2015 regulation is void |
|---|---|---|
| Mali | yes | no |
| South Sudan | yes | no |
| Myanmar | no | yes |
| Cuba, Lebanon, Sudan, Syria | yes | yes |
| Jordan | yes, unless Anlage C's exemption applies (F4) | same |
| Türkiye | yes, unless an official-capacity passport | same |
| the twelve Annex IV states (for example Nigeria) | yes | yes |
| any other state | no | no |

## Checks run

`./check.sh` in this folder, target `main`, on 2026-11-02 (the `l4` is a dev build, 25a091f4...; the main build compared with is 1.6.108 (main, 2ae7c9b, 2026-11-02)):

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.108 (main, 2ae7c9b, 2026-11-02)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
atv-cases-seat.l4                              0        14       0        0         0 |      0        14       0        0  same
atv-law.l4                                     0         0       0        0         0 |      0         0       0        0  same
atv-seat.l4                                    0         0       0        0         0 |      0         0       0        0  same
atv-tests.l4                                   0        56       0        0         0 |      0        56       0        0  same
TOTAL (4 modules)                              0        70       0        0           |      0        70       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

`python3 -I srcrefs.py check --refs ../../registers/source-bundle/aufenthv-26.txt atv-law.l4`: 71 src: lines, 12 runs, 16 locators, 0 problems.
No assertion is expected to fail. The check does not see a different trace outcome; the encoding has no regulative rule and no `#TRACE`.

## Before this is worth relying on

- Anlage C between 2015 and 2023: buzer.de's version list for Anlage C shows no change between 29 Dec 2015 and 29 Jul 2023 (versions: 2005, 2007, 2008 (May), 2009, 2011, 2015, 2023, 2026), so F8's assumption holds on that secondary source; the AufenthV's own 2004 preamble is still not read (the Bundesrat paper 731/04 is a scanned PDF without a text layer).
- Compare the Visa Code excerpt with the Official Journal text, since the consolidated version has no legal effect and may have been amended since 28.06.2024.
- Decide F1 to F3 with someone who knows German administrative law: the article's reading is a new argument, not a settled one, and the Myanmar consequence is new.
- Have a domain expert read the encoding against the German text (the pipeline's HG1).
