# NOTES -- Aufenthaltsverordnung § 26 and Anlage C (the airport transit visa), L4 encoding by agent `atv` (Sonnet 5.5, solo)

This encodes the rule that makes nationals of the states in Anlage C hold an airport transit visa to change planes at a German airport, the power it rests on, and the constitutional test that the article by Felix Ringe and Linus Folkerts says the 2015 addition of Mali fails.
It does not decide whether the test is failed: it answers the traveller's question under both readings, and says which facts each reading rests on.

The sources are in `../../registers/source-bundle/`, as plain-text conversions of the per-norm pages of gesetze-im-internet.de read on 2026-11-02, with their `.meta.json`.
They are the site's reading versions, not the gazette.
The preamble of the 2015 amending regulation is deposited **only** as the German quotation the article prints (`aufenthv-2015-preamble-aid.txt`), because the gazette text could not be obtained (finding 3).
The target is `main`: the build compared with is 1.6.108 (main, 2ae7c9b, 2026-11-02).
Modules: `atv-law.l4` (the law layer), `atv-seat.l4` (the seat), `atv-tests.l4` and `atv-cases-seat.l4`.

## Seat

The seat is **a person changing planes at a German airport**: the traveller to whom § 26 AufenthV is applied.
Their questions, in `atv-seat.l4`, in the text's order under `§` groups:

- § 26(2) sentence 1: Must I hold an airport transit visa to change planes at a German airport, reading Annex C as it is printed?
- § 26(1) and (2) sentence 2: Am I exempt from needing a residence title while I wait in the transit area, reading Annex C as it is printed?
- the same two questions, **if the entries the 2015 amending regulation added to Annex C are void** (a group that only arises if the traveller's state is Mali or South Sudan: the heading's comment says so, so a form can ask first)
- Does the preamble of the 2015 amending regulation cite § 99(3a) AufenthG?

The inputs are facts the traveller can state: nationality, whether they stay in the transit area, whether they hold a visa, and, for Jordan and Türkiye, the facts Anlage C asks.
Two borrowed terms are asked as facts, as the ruled default says: Art. 3(5) of the Visa Code (an exemption) and Annex IV of the Visa Code (the common list), because the Visa Code is not deposited.
The people the text also addresses are officials (the ministry that issues the regulation, the border police who check the visa): they have no seat.

## Method

One agent, working alone, from the deposited sources and the article.
The encoding is three layers in two modules.
`atv-law.l4` holds the nouns (`Transit passenger`), Anlage C as data, the two exemptions written into it, the two limbs of § 26(2) sentence 1, § 26(1) with sentence 2, and the citation test of Art. 80(1) sentence 3 GG with the powers the 2015 preamble cites.
`atv-seat.l4` holds no rule: it builds the law layer's record from plain inputs and calls the law layer.
Every rule has an `@ref` with locators, and the quotations were pasted by script from the deposited files and checked with `srcrefs.py` (28 quote lines, 10 locators, 0 problems).
The tests' expected values were written from the German text, not from this encoding's output.
One assertion failed on the first run: my own transcription put a `TRUE` in the wrong argument position (the expected value was right and the call was wrong); the argument was moved and the expectation was not touched.

## Coverage table

| provision | disposition | where, or why |
|---|---|---|
| AufenthV § 26(1) | encoded | `the traveller is exempt from the residence-title requirement under the reading` |
| AufenthV § 26(2) sentence 1, first limb (Visa Code Art. 3(1) with (5)) | encoded | `the traveller must hold an airport transit visa under the reading`, with Annex IV and Art. 3(5) asked as facts |
| AufenthV § 26(2) sentence 1, second limb (Annex C states, unless Art. 3(5)) | encoded | same rule |
| AufenthV § 26(2) sentence 2 | encoded | the exemption of § 26(1) holds only for a holder, where a visa is required |
| AufenthV § 26(2) sentence 3 (the visa is not a residence title) | inert | quoted in the deposit; no question turns on it |
| AufenthV § 26(3) (weggefallen) | inert | repealed |
| AufenthV Anlage C, the eight states | encoded | `the states listed in Annex C as printed` |
| AufenthV Anlage C, Jordanien exemption | encoded | `Annex C exempts the traveller from the airport transit visa requirement` |
| AufenthV Anlage C, Türkei exemption | encoded | same rule |
| AufenthG § 99(3a) | encoded | `the power needed to add a state to Annex C`: the power the article says was needed |
| AufenthG § 99(1) and (2) | inert | named in the 2015 preamble list as powers cited; their content is not encoded: the point is that none of them is (3a) |
| AufenthG § 99(3) and (4) | out-of-scope | other powers (naming the body under §§ 73 and 73a; short-lived regulations); the article does not rely on them |
| Grundgesetz Art. 80(1) sentence 3 | encoded | `the preamble cites the power`, `the 2015 addition to Annex C is void for want of citation` |
| Grundgesetz Art. 80(1) sentences 1, 2 and 4, (2) to (4) | out-of-scope | the power must be given by statute with its content, purpose and extent fixed: the article does not argue that § 99(3a) fails that |
| BVerfG 2 BvF 3/90, paras. 151 to 158 | inert | the source of the rule that the citation must name the individual provision and that a breach makes the regulation void |
| 2015 amending regulation, preamble | encoded | `the powers cited in the preamble of the 2015 amending regulation`, from the aid (finding 3) |
| 2015 amending regulation, Art. 1 No. 10 (the Annex C change) | out-of-scope | not obtained from the gazette; the statement that it added Mali and South Sudan is the article's (finding 3) |
| the 2023 amendment (adds Cuba) and the 2026 amendment (removes India) | out-of-scope | no date axis: only Anlage C as printed on 2026-11-02 is encoded (fork F8) |
| EU Visa Code (Regulation (EC) No 810/2009), Art. 3(1), (2), (5), Annex IV | out-of-scope | not deposited (EUR-Lex answered the fetch with HTTP 202 and an empty body; not retried or worked around); asked as facts |
| AufenthG § 13(2) (what counts as entering) | out-of-scope | asked as the fact "stays only in the transit area" |
| the rest of AufenthV; AZRG § 40; Verwaltungskostengesetz | out-of-scope | not part of the question |

## Fork register

Each fork gives the readings, the one taken, and the text that licenses each.
The article's own "potential follow-up considerations" for Case 2 are listed here with what this encoding does with them.

**F1. Which reading answers?**
(a) *As printed*: the regulation is applied as written, and Mali is listed.
(b) *Without the 2015 additions*: the entries the 2015 regulation added are void for want of citation.
Taken: **both**, as separate questions, because no court is known to have ruled on (b) (the article says it found the point itself and that, to its knowledge, none of its vulnerabilities was previously recorded).
The answer an officer applying the rule today would give is (a).

**F2. How far does the voidness go?**
(a) Only the entries the amending regulation added (Mali, South Sudan). The article's reading, and the one encoded.
(b) The whole amending regulation. BVerfG 2 BvF 3/90 para. 158 says a breach of the citation requirement "führt ... zur Nichtigkeit der Verordnung" (`bverfg-2bvf3-90-paras-151-158.txt:65-71`, the paragraph is not provision-scoped), though the case there concerned a regulation with no valid basis in the first place.
(c) The whole of Anlage C, if the 2015 regulation re-enacted the annex rather than adding two entries. The article describes an addition; the gazette was not read.
The encoding follows (a) because (b) and (c) would reach things the article does not argue and the deposit cannot check.

**F3. Exceptions to the citation requirement.**
The article lists five follow-up considerations for Case 2 and rejects each. What the encoding does with them:
- *Other cited powers cover it* ("The visa requirement is covered by other cited legal bases"). The article says no: the cited powers concern residence-title exemptions, procedures, fees, documents and register data. The encoding's test is membership of `AufenthG 99(3a)` in the cited list, so it reads as the article does. A court might read § 99(1) no. 1 (exemptions from the residence title) as covering a visa duty; the encoding cannot say.
- *The previous rule still requires the visa*: the article says the previous Anlage C listed neither Mali nor South Sudan (its footnote 12). Encoded as reading (b), without those two entries; unverified (finding 3).
- *Germany's notification to the Commission under Art. 3(2) of the Visa Code replaces the regulation*: the article says no; § 99(3a) says the Ministry names the states by regulation "nach Maßgabe von Artikel 3 Absatz 2". The notification does not enter § 26(2), whose second limb reaches only Annex C states, so it changes no answer here.
- *Later amendments cured it*: the article says no, because the 2023 and 2026 amendments cite their own powers and do not re-enact Mali or South Sudan. Not encoded: it needs the two gazettes.
- *EU law independently requires the visa*: the article says no, because neither state is in Annex IV of the Visa Code. Encoded through the first limb: the traveller states whether they are in an Annex IV state, and the tests assert that a Malian national who is also in an Annex IV state needs the visa under both readings.
Separately, a general exception to the citation requirement (OVG NRW 3 A 1217/14, which the article discusses under Case 3, accepted an earlier regulation's citation for a limited amendment) is the input `an exception applies`: `TRUE` makes the additions stand.

**F4. "Der Weiterflug muss innerhalb von zwölf Stunden ..." (Anlage C, Jordanien).**
It is a separate sentence after (a) and (b). Taken: it applies to the exemption as a whole, both (a) and (b), and the tests assert that (a) or (b) alone is not enough.
The other reading, that it qualifies only (b), is open on the text.

**F5. "Stays only in the international transit area"** stands for the text's "ohne im Sinne des § 13 Abs. 2 des Aufenthaltsgesetzes einzureisen" (§ 26(1)). § 13(2) is not deposited, so entry is asked as one fact.

**F6. Annex C's own exemptions (Jordan, Türkiye) are limited to Annex C.**
They are written into the annex and do not reach the first limb (Visa Code Annex IV states). A Jordanian national who is also in an Annex IV state is a combination the encoding allows and the text does not discuss.

**F7. "Sofern diese nicht nach Artikel 3 Absatz 5 ... befreit sind"** (second limb) is read as removing Annex C nationals who fall in an Art. 3(5) category.
The text can also be read as removing them only from the first limb; the words follow the second-limb clause, and are encoded there.

**F8. No date axis.**
Anlage C is encoded as printed on 2026-11-02, with the 2023 addition of Kuba and the 2026 removal of Indien (the article's footnote 13) already in it.
A traveller asking about a date between 29 Dec 2015 and the 2026 amendment would get a wrong answer for India and, before the 2023 amendment, for Cuba.

## What the law turns out to say

1. **Sentence 2 of § 26(2) turns the visa into a condition of the transit exemption.** A traveller in the transit area who is within the visa duty but has no visa is not covered by § 26(1) at all (asserted in `atv-tests.l4`). The article speaks of "avoiding the visa procedure and its cost"; the text's own consequence of the duty is that no visa means no exemption from the residence-title requirement. Asserted.
2. **The 2015 preamble, as the article quotes it, cites § 69(2) and (3) nos. 4 and 6 with the Verwaltungskostengesetz, § 99(1) nos. 1 to 3 and 13a, § 99(2) sentence 2 with sentence 1 no. 1, and § 40(1) nos. 1, 4 and 5 AZRG. None is § 99(3a).** Asserted in `atv-tests.l4` against the aid file, with a control (a list that does contain (3a) tests as cited).
3. **Two things rest on the article and not on the gazette**: the preamble text just quoted, and the statement that Article 1 No. 10 of BGBl. 2015 I S. 2467 added Mali and South Sudan. The bgbl.de archive viewer needs JavaScript and returned no PDF; no 2015 text was read.
4. **BVerfG 2 BvF 3/90 supports the article's engine and differs from it in one word.** Paragraph 151: the citation must name "die ermächtigende Einzelvorschrift" and, where the regulator wants to use several powers, "vollständig" ("nach seinem erkennbar geäußerten Willen"). Paragraph 154: the power claimed must arise "gerade aus den von ihr selbst angeführten Vorschriften". Paragraph 158: the defect makes "die Verordnung" void. The article says "provisions ... not covered by the cited legal basis are void" (F2).
5. **Anlage C as printed has eight states** (counted by `atv-tests.l4`), including Kuba and excluding Indien, matching the article's footnote 13.
6. **Two ministries' names in § 99.** The deposited § 99(1) says "Bundesministerium des Innern und für Heimat" and § 99(2) to (4) say "Bundesministerium des Innern, für Bau und Heimat", the names current at different amendments; the article's 2015 translation says "Federal Ministry of the Interior". No question turns on it.

## Answer table

| nationality (no exempting document, in transit only) | must hold the visa, as printed | if the 2015 additions are void |
|---|---|---|
| Mali | yes | no |
| South Sudan | yes | no |
| Cuba, Lebanon, Sudan, Syria | yes | yes |
| Jordan | yes, unless Anlage C's exemption applies (F4) | same |
| Türkiye | yes, unless an official-capacity passport | same |
| any other state | no, unless the state is in Visa Code Annex IV | same |

## Checks run

`./check.sh` in this folder, target `main`, on 2026-11-02 (the `l4` is a dev build, 25a091f4...; the main build compared with is 1.6.108 (main, 2ae7c9b, 2026-11-02)):

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.108 (main, 2ae7c9b, 2026-11-02)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
atv-cases-seat.l4                              0        12       0        0         0 |      0        12       0        0  same
atv-law.l4                                     0         0       0        0         0 |      0         0       0        0  same
atv-seat.l4                                    0         0       0        0         0 |      0         0       0        0  same
atv-tests.l4                                   0        43       0        0         0 |      0        43       0        0  same
TOTAL (4 modules)                              0        55       0        0           |      0        55       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

`python3 -I srcrefs.py check --refs ../../registers/source-bundle/aufenthv-26.txt atv-law.l4`: 28 src: lines, 7 runs, 10 locators, 0 problems.
No assertion is expected to fail. The check does not see a different trace outcome; the encoding has no regulative rule and no `#TRACE`.

## Before this is worth relying on

- Get BGBl. 2015 I S. 2467 and read its preamble and Article 1 No. 10; replace the aid.
- Get the Visa Code consolidation (EUR-Lex refused the fetch) and encode Art. 3(1), (2), (5) and Annex IV, so the two facts asked of the traveller can be worked out.
- Decide F1 to F3 with someone who knows German administrative law: the article's reading is a new argument, not a settled one.
- Have a domain expert read the encoding against the German text (the pipeline's HG1).
