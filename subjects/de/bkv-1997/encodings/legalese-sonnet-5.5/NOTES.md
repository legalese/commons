# NOTES -- Berufskrankheiten-Verordnung § 9(5) and the Freedom of Information Act (access to the Council's papers), L4 encoding by agent `bkv` (Sonnet 5.5, solo)

This encodes the claim to access to a federal authority's documents (IFG § 1(1)), the bar in IFG § 3 no. 4 for information under a statutory confidentiality duty, the confidentiality rule for the papers of the Expert Advisory Council on Occupational Diseases (BKV § 9(5) sentences 2 and 3, as the Seventh Amending Regulation set them from 1 August 2026), the power that rule needs (SGB VII § 9(1a) sentence 4) and the constitutional test that the article by Felix Ringe and Linus Folkerts says the 2026 amendment fails.
It does not decide whether the test is failed: it answers the requester's question under both readings and says which facts each rests on.

The sources are in `../../registers/source-bundle/`: plain-text conversions of per-norm pages of gesetze-im-internet.de read on 2026-11-02, the gazette text of the Seventh Amending Regulation (BGBl. 2026 I Nr. 210, text and PDF), the Bundesrat printed paper 312/26 (text) and an excerpt of BVerfG 2 BvF 3/90, each with its `.meta.json`.
The consolidated texts are the site's reading versions; the gazette is the promulgated text.
The target is `main`: the build compared with is 1.6.108 (main, 2ae7c9b, 2026-11-02).
Modules: `bkv-law.l4` (the law layer), `bkv-seat.l4` (the seat), `bkv-tests.l4` and `bkv-cases-seat.l4`.

## Seat

The seat is **a person who asks a federal authority for a document about the Expert Advisory Council**: the journalist of the article's Case 1, or anyone else with a claim under § 1(1) IFG.
Their questions, in `bkv-seat.l4`, under `§` groups:

- Am I entitled to access to this document under the Freedom of Information Act, reading § 9(5) BKV as it has stood since 1 August 2026? And if the 2026 amendment of § 9(5) is void? (the second group only arises for an external paper submitted to the Council; the heading's comment says so)
- Does § 9(5) BKV make the document confidential, on each reading?
- Does the preamble of the Seventh Amending Regulation cite § 9(1a) sentence 4 SGB VII?

The inputs are facts the requester can state: whether the request is to a federal authority, whether the paper was prepared outside the Council and the Ministry, whether it was submitted to the Council for its deliberations, whether it is one of the documents § 9(5) sentence 1 makes public, and, as two asked-as-facts characterisations, whether another ground for refusal applies and whether another statutory confidentiality duty attaches.
The article's footnote 8 assumes the statement was independently prepared and submitted as non-confidential and holds no internal deliberations, personal data, trade secrets or copyright-protected material: those assumptions are the input `another ground applies` being false.
The people the text also addresses are the Ministry (it decides the request and issues the regulation), the Council's members (they bear the duty of confidentiality) and the association that wrote the statement: none has a seat.

## Method

One agent, working alone, from the deposited sources and the article.
`bkv-law.l4` holds the noun (`Request for a document`), the two wordings of § 9(5), the bar of § 3 no. 4 IFG, the claim of § 1(1) IFG, and the citation test of Art. 80(1) sentence 3 GG with the powers the two preambles cite.
`bkv-seat.l4` holds no rule: it builds the law layer's record from plain inputs and calls the law layer.
Every rule has an `@ref` with locators; `srcrefs.py` checked 24 quote lines and 10 locators, 0 problems.
The tests' expected values were written from the German text, not from this encoding's output.

## Coverage table

| provision | disposition | where, or why |
|---|---|---|
| IFG § 1(1) sentence 1 | encoded | `the requester is entitled to access under the reading` |
| IFG § 1(1) sentences 2 and 3, (2), (3) | out-of-scope | other bodies, the form of access, other statutes' access rules: not the question |
| IFG § 3 no. 4 | encoded | `section 3 no. 4 IFG bars access under the reading` |
| IFG § 3 nos. 1 to 3 and 5 to 8, §§ 2, 4 to 9 | out-of-scope | asked as one fact, `another ground applies` |
| BKV § 9(5) sentence 1 | encoded | the documents excepted from confidentiality |
| BKV § 9(5) sentences 2 and 3 | encoded | `section 9(5) BKV makes the document confidential under the reading`, in both wordings |
| BKV § 8(3), § 9(1) sentence 3, § 9(2) | inert | the members' duty of confidentiality and the non-public meetings; they enter only as the asked-as-fact input `another duty attaches` (fork F3) |
| BKV § 9(1) to (4) and the rest of the Regulation | out-of-scope | meetings, topics, recommendations: not the question |
| SGB VII § 9(1a) sentence 4 | encoded | `the power needed to make the confidentiality rule` |
| SGB VII § 9(1), (6) and § 193(8) | inert | named in the two preambles as powers cited |
| SGB VII § 9(1a) sentences 1 to 3, § 9 (2) to (9) | out-of-scope | other provisions of § 9 |
| BGBl. 2026 I Nr. 210, preamble | encoded | `the powers cited in the preamble of the Seventh Amending Regulation` |
| BGBl. 2026 I Nr. 210, Art. 1 No. 1 | encoded | the new wording of § 9(5) sentences 2 and 3 |
| BGBl. 2026 I Nr. 210, Art. 1 No. 2 (Anlage 1 No. 1322) | out-of-scope | the new occupational disease rests on § 9(1) sentence 1, which the preamble cites; the article does not touch it |
| BGBl. 2026 I Nr. 210, Art. 2 (in force 1 August 2026) | inert | the date from which the new wording stands |
| BKV Eingangsformel (the 1997 preamble) | encoded | `the powers cited in the original preamble of the BKV` |
| Bundesrat Drucksache 312/26 | inert | the source of the earlier wording and of the government's stated reason and competence (findings 2 and 3) |
| Grundgesetz Art. 80(1) sentence 3 | encoded | `the preamble cites the power`, `the 2026 amendment of section 9(5) BKV is void for want of citation` |
| BVerfG 2 BvF 3/90, paras. 151 to 158 | inert | the source of the citation rule |

## Fork register

Each fork gives the readings, the one taken, and the text that licenses each.

**F1. Which reading answers?**
(a) *As in force from 1 August 2026*: the Council's "Beratungsunterlagen" are confidential, whoever made them.
(b) *As before the 2026 amendment*: only the "intern erstellten Beratungsunterlagen".
Taken: **both**, as separate questions, because no court is known to have ruled on (b); the article says it found the point itself.
The answer the Ministry gives today is (a).

**F2. How far does the voidness go?**
(a) Only the new sentences of § 9(5). The article's reading, and the one encoded.
(b) The whole Seventh Amending Regulation. BVerfG 2 BvF 3/90 para. 158 speaks of "die Verordnung" (`bverfg-2bvf3-90-paras-151-158.txt:65-71`); on that reading Anlage 1 No. 1322 (Parkinson syndrome from pesticides) would fall with it, though § 9(1) sentence 1, which the preamble cites, is the power for it. The article does not argue this.

**F3. Exceptions to the citation requirement, and the Council members' duty.**
The article lists three follow-up considerations for Case 1 and rejects each ("highly unlikely"); the encoding has one input, `an exception applies`, for the citation questions and another, `another duty attaches`, for the third:
- *§ 9(1a) SGB VII is not a legal basis but only explains the scope of § 9(1), so it need not be cited.* The article says the Federal Government itself names § 9(1a) as the base for "Durchführung der Beratungen und Veröffentlichung der Ergebnisse" in the explanatory memorandum to the 2020 bill (Bundestag document 19/17586, p. 102, quoted by the article): **not read**. On the 2026 regulation's own memorandum, see finding 3. The input `an exception applies` carries it.
- *If the amendment is void, the previous rule still bars access.* The article says it only protected internally created papers, and the 2026 text was changed to reach external ones. Both are true of the deposit (finding 2); the encoding's reading (b) takes the earlier wording as internal-only.
- *Members' duties of confidentiality and non-public meetings already bar access* (BKV § 8(3), § 9(1) sentence 3). The article says they should not be read as barring access to an independently prepared external statement merely because the Council considered it, and cites BVerwG 7 C 4.11 paras. 30 to 33 (**not read**). The encoding makes it the input `another duty attaches`: `TRUE` bars access under § 3 no. 4 even where § 9(5) does not reach the paper. § 8(3) binds "die Mitglieder" (`bkv-8.txt:7`), and § 3 no. 4 asks whether "die Information" is subject to a duty, which is a different thing; the encoding leaves the call to the person.
**Both inputs are legal judgments left to someone else.**

**F4. Which wording applies to a paper received before 1 August 2026?**
Art. 2 of the Seventh Amending Regulation puts the new wording in force on 1 August 2026 and says nothing of papers already held. The article's scenario does not say when the statement arrived. The encoding does not decide: the reading is chosen by the input and by the void test, not by a date. Open.

**F5. What is a "Beratungsunterlage"?**
The text does not define it. The government's memorandum says the earlier wording left it unclear whether "Eingaben und sonstige Korrespondenz an den ÄSVB" were confidential (`brd-312-26.txt:226-232`). Taken: a paper submitted to the Council for its deliberations is one; the requester states whether theirs was.

## What the law turns out to say

1. **The Seventh Amending Regulation replaced sentence 2 of § 9(5) with two sentences** (Art. 1 No. 1, `bgbl-2026-i-210.txt:22-24`) and inserted Anlage 1 No. 1322 (No. 2, lines 25-26); it is in force from 1 August 2026 (Art. 2) with the Bundesrat's consent (`bgbl-2026-i-210.txt:38`). Its preamble names one power, "§ 9 Absatz 1 Satz 1 und 2" SGB VII (lines 12-14). Asserted in `bkv-tests.l4`.
2. **The government's own memorandum calls the change a clarification and says why.** Drucksache 312/26: "durch eine Präzisierung in § 9 Absatz 5 Satz 2 BKV klargestellt, dass sämtliche Beratungsunterlagen des ÄSVB vertraulich sind. Die Regelung bezog sich bislang ihrem Wortlaut nach auf die intern erstellten Beratungsunterlagen. Hierdurch war nicht eindeutig, ob zum Beispiel Eingaben und sonstige Korrespondenz an den ÄSVB ... ebenfalls vertraulich zu behandeln sind" (`brd-312-26.txt:226-232`). So the earlier wording was internal-only, as the article says, and the government's aim was to reach external submissions. The government also calls it "nicht eindeutig", which is the other side of the article's "highly unlikely" follow-up on the previous rule.
3. **The memorandum names § 9(1) SGB VII as the whole regulation's basis, and names no power for the § 9(5) change.** Section V, "Regelungskompetenz", says the competence "ergibt sich aus § 9 Absatz 1 Satz 1 und Satz 2 SGB VII" (`brd-312-26.txt:283-285`); a search of the extracted text for "1a", "Ermächtigung", "Rechtsgrundlage" and "Zitier" finds only line 627, about the disease list. That matches the premise of the article's argument (the government did not rely on § 9(1a) sentence 4); whether § 9(1a) sentence 4 is a power at all is the article's first follow-up (F3).
4. **The original BKV preamble does not cite § 9(1a) either**, only "§ 9 Abs. 1 und 6 und des § 193 Abs. 8" SGB VII (`bkv-eingangsformel.txt:2`). The preamble printed on the site is the 1997 one; the one that introduced §§ 7 to 11 (the Council) is not in the deposit, and the article does not mention it.
5. **§ 9(1a) sentence 4 reads**: "Das Nähere über die Stellung und die Organisation des Sachverständigenbeirats und der Geschäftsstelle regelt die Bundesregierung in der Rechtsverordnung nach Absatz 1" (`sgb7-9.txt:3`). Whether the confidentiality of the Council's papers is part of its "Stellung und Organisation" is the legal question under the article's first follow-up; the encoding does not answer it.
6. **The earlier wording is deposited only through the memorandum** ("intern erstellten Beratungsunterlagen"). The full earlier sentence is quoted in the article from de.openlegaldata.io, not deposited.

## Answer table

| the paper | access as § 9(5) stands | access if the 2026 amendment is void |
|---|---|---|
| external statement submitted to the Council (the article's case) | no | yes |
| paper made inside the Council or the Ministry | no | no |
| a recommendation, opinion or closing report | yes | yes |
| a paper never submitted to the Council | yes | yes |
| any of these where another ground for refusal applies | no | no |

(Each row assumes a request to a federal authority and no other statutory confidentiality duty.)

## Checks run

`./check.sh` in this folder, target `main`, on 2026-11-02 (the `l4` is a dev build, 25a091f4...; the main build compared with is 1.6.108 (main, 2ae7c9b, 2026-11-02)):

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.108 (main, 2ae7c9b, 2026-11-02)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
bkv-cases-seat.l4                              0        11       0        0         0 |      0        11       0        0  same
bkv-law.l4                                     0         0       0        0         0 |      0         0       0        0  same
bkv-seat.l4                                    0         0       0        0         0 |      0         0       0        0  same
bkv-tests.l4                                   0        22       0        0         0 |      0        22       0        0  same
TOTAL (4 modules)                              0        33       0        0           |      0        33       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

`python3 -I srcrefs.py check --refs ../../registers/source-bundle/ifg-1.txt bkv-law.l4`: 24 src: lines, 7 runs, 10 locators, 0 problems.
No assertion is expected to fail. The check does not see a different trace outcome; the encoding has no regulative rule and no `#TRACE`.

## Before this is worth relying on

- Read Bundestag document 19/17586 p. 102 and BVerwG 7 C 4.11 (the article's footnotes 9 and 11), and decide F3 with someone who knows German administrative and information-access law.
- Get the earlier text of § 9(5) from the gazette and the preamble that introduced §§ 7 to 11 BKV, and decide F4.
- Deposit IFG §§ 3 to 6 and encode the other grounds for refusal, so `another ground applies` can be worked out.
- Have a domain expert read the encoding against the German text (the pipeline's HG1).
