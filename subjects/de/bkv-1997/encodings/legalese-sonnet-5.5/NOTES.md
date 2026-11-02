# NOTES -- Berufskrankheiten-Verordnung § 9(5) and the Freedom of Information Act (access to the Council's papers), L4 encoding by agent `bkv` (Sonnet 5.5, solo)

This encodes the claim to access to a federal authority's documents (IFG § 1(1)), the bar in IFG § 3 no. 4 for information under a statutory confidentiality duty, the confidentiality rule for the papers of the Expert Advisory Council on Occupational Diseases (BKV § 9(5) sentences 2 and 3, as the Seventh Amending Regulation set them from 1 August 2026), the power that rule needs (SGB VII § 9(1a) sentence 4) and the constitutional test that the article by Felix Ringe and Linus Folkerts says the 2026 amendment fails.
It does not decide whether the test is failed: it answers the requester's question under both readings and says which facts each rests on.

Two additions, written on 2026-11-02 beside the first four modules and leaving them unchanged, extend it.
The first spells out the grounds for refusing access in IFG § 3 nos. 1 to 8, § 4(1), § 5(1) and § 6 as rules, so that the requester's question no longer rests on one input, `another ground applies`.
The second is a second seat, a worker who asks whether their disease is a listed occupational disease: BKV § 1(1) with Anlage 1 No. 1322, the Parkinson entry inserted by the same Seventh Amending Regulation, under two readings of that Regulation (it stands, or it is void as a whole).

The sources are in `../../registers/source-bundle/`: plain-text conversions of per-norm pages of gesetze-im-internet.de read on 2026-11-02, the gazette text of the Seventh Amending Regulation (BGBl. 2026 I Nr. 210, text and PDF), the Bundesrat printed paper 312/26 (text), excerpts of Bundestag document 19/17586 (pp. 101 to 102), BVerwG 7 C 4.11 and BVerfG 2 BvF 3/90, each with its `.meta.json`.
The consolidated texts are the site's reading versions; the gazette is the promulgated text.
The target is `main`: the build compared with is 1.6.108 (main, 2ae7c9b, 2026-11-02).
Since the first pass the bundle also holds IFG §§ 4, 5 and 6, BKV § 1, and the heading and the rows for Nos. 1321 and 1322 of BKV Anlage 1 (an excerpt, with the group headings 1 and 13), all from gesetze-im-internet.de, read on 2026-11-02 with the User-Agent `Mozilla/5.0 (Macintosh) legalese-commons-fetcher`; each has a `.meta.json` and a row in `SOURCE-LICENSE.md`.
Modules of the first pass: `bkv-law.l4` (the law layer), `bkv-seat.l4` (the seat), `bkv-tests.l4` and `bkv-cases-seat.l4`.
Modules of the IFG grounds: `bkv-ifg-law.l4` (the grounds), `bkv-ifg-seat.l4` (a second layer of the requester's seat) and `bkv-ifg-tests.l4`.
Modules of the worker: `bkv-worker-law.l4`, `bkv-worker-seat.l4` and `bkv-worker-tests.l4`.
`check.sh` runs every `.l4` in the folder, so it has no module list to edit.

## Seats

There are two seats: the requester of a document, in two layers, and a worker with a disease.
The accident insurer (the Unfallversicherungsträger, who finds the individual causal link) has no seat, and nor do the parties named under the requester's first layer.

### The requester, first layer (`bkv-seat.l4`)

The seat is **a person who asks a federal authority for a document about the Expert Advisory Council**: the journalist of the article's Case 1, or anyone else with a claim under § 1(1) IFG.
Their questions, in `bkv-seat.l4`, under `§` groups:

- Am I entitled to access to this document under the Freedom of Information Act, reading § 9(5) BKV as it has stood since 1 August 2026? And if the 2026 amendment of § 9(5) is void? (the second group only arises for an external paper submitted to the Council; the heading's comment says so)
- Does § 9(5) BKV make the document confidential, on each reading?
- Does the preamble of the Seventh Amending Regulation cite § 9(1a) sentence 4 SGB VII?

The inputs are facts the requester can state: whether the request is to a federal authority, whether the paper was prepared outside the Council and the Ministry, whether it was submitted to the Council for its deliberations, whether it is one of the documents § 9(5) sentence 1 makes public, and, as two asked-as-facts characterisations, whether another ground for refusal applies and whether another statutory confidentiality duty attaches.
The article's footnote 8 assumes the statement was independently prepared and submitted as non-confidential and holds no internal deliberations, personal data, trade secrets or copyright-protected material: those assumptions are the input `another ground applies` being false.
The people the text also addresses are the Ministry (it decides the request and issues the regulation), the Council's members (they bear the duty of confidentiality) and the association that wrote the statement: none has a seat.

### The requester, second layer (`bkv-ifg-seat.l4`)

The same person, with the grounds for refusing access spelled out instead of asked as one input.
Two questions, each asked on both readings of § 9(5) (four exports), under `§` groups in the order of the first layer:

- Am I entitled to access, with every ground for refusal in §§ 3 to 6 IFG spelled out, reading § 9(5) BKV as it has stood since 1 August 2026?
  And if the 2026 amendment is void?
  (the second group only arises for an external paper submitted to the Council; the heading's comment says so)
- Which grounds for refusing access apply, on each reading?
  The answer is a list of the grounds, and an empty list means none does.

The inputs are the first layer's five facts about the document and the request (not `another ground applies`, which this layer replaces) and 44 inputs for the grounds, one per fact or characterisation, in the order of the text, each with a `@desc` from the requester's seat (the exception input is added in the second question of each pair).
The facts describe the information the person asks for: a person who asks only for a part answers about that part (fork F12).
The layer builds the law layers' records inside each question, with a `WHERE` block, and calls `the requester is entitled to access under the reading` of `bkv-law.l4` with its field `another ground for refusing access applies` set from `bkv-ifg-law.l4`'s `a ground for refusal other than a statutory duty applies`.
It restates no rule, and no name is defined in two modules.
The inputs are many and a form should ask only the ones the answer still depends on: any ground that holds settles the answer, and every ground must be false for access to stand.

### The worker (`bkv-worker-seat.l4`)

The seat is **a worker who has a disease and asks whether it is a listed occupational disease**: BKV § 1(1) with Anlage 1 No. 1322, "Parkinson-Syndrom durch langjährig, häufig und selbst angewendete Pestizide", inserted by Art. 1 No. 2 of the Seventh Amending Regulation and in force from 1 August 2026 (Art. 2).
Their questions, under `§` groups:

- Is my disease a listed occupational disease, reading the Seventh Amending Regulation as in force since 1 August 2026?
  The answer is yes, no, or nothing for a disease the encoding does not cover (a `MAYBE BOOLEAN`).
- The same, if the whole Seventh Amending Regulation is void (the second group only arises if the person asks what follows from the article's argument; the heading's comment says so).
  The export text says that a no does not decide whether the disease can still be recognised like an occupational disease (finding 9).
- Does the preamble of the Seventh Amending Regulation cite the power for the new entry, § 9(1) sentences 1 and 2 SGB VII?
  (yes; the premise of fork F14)

The inputs are facts the worker can state: which disease they have (Parkinson syndrome, or another disease), and, asked as characterisations, whether it was caused by pesticides, whether the pesticides were applied over many years, whether often, whether by the worker themself, whether the use was part of work covered by the statutory accident insurance, and the date for which they ask.
The date is the day the question is about, such as the day of the request to the insurer: it is not the day the illness arose or began, which BKV and SGB VII treat elsewhere (fork F15).

## Method

One agent, working alone, from the deposited sources and the article.
`bkv-law.l4` holds the noun (`Request for a document`), the two wordings of § 9(5), the bar of § 3 no. 4 IFG, the claim of § 1(1) IFG, and the citation test of Art. 80(1) sentence 3 GG with the powers the two preambles cite.
`bkv-seat.l4` holds no rule: it builds the law layer's record from plain inputs and calls the law layer.
Every rule has an `@ref` with locators; `srcrefs.py` checked 24 quote lines and 10 locators, 0 problems.
The tests' expected values were written from the German text, not from this encoding's output.

The two additions were written the same way, by the same encoder, in new modules.
`bkv-ifg-law.l4` has one record of facts for each ground (`Facts about section 3 no. 1`, and so on, eleven in all), one rule for each ground, and the compositions the seat needs: `a ground for refusal other than section 3 no. 4 applies` (one `OR` line for each of the ten other grounds), `a ground for refusal other than a statutory duty applies` (that, with the limbs of no. 4 that `bkv-law.l4` does not have) and `the grounds for refusing access that apply` (a list).
Each field of each record carries a trailing comment, F for a fact and J for a judgment kept as an input, and the reason (fork F6).
`bkv-worker-law.l4` has the worker's case, the two readings of the Seventh Amending Regulation, three rules (what the entry describes, whether it is in force on a day under a reading, and whether the disease is a listed occupational disease), and the test that the preamble cites the power for the new entry.
`bkv-ifg-law.l4`: 24 quote lines, 12 runs and 15 locators, 0 problems; `bkv-worker-law.l4`: 29 quote lines, 9 runs and 9 locators, 0 problems (`python3 -I srcrefs.py check --refs ../../registers/source-bundle/ifg-1.txt <module>`).

The tests were written from the German text before the first run of the new modules, and no expected value was changed afterwards: the new tests passed at their first run, 186 assertions in `bkv-ifg-tests.l4` and 29 in `bkv-worker-tests.l4`, and 14 more assertions were then added to `bkv-ifg-tests.l4` (the in-force column of the requester's second answer table, which the first version left to follow from the law layer's conjunction).
Because a first run with no failure shows nothing about whether the tests can fail, rule mutations were tried on scratch copies (never kept): dropping the sentence-2 branch of § 4(1), dropping the express-consent branch of § 5(1), reading § 3 no. 7 as `OR`, dropping § 5(2), reading the list's statutory limb as false, reading the date as strictly after, reading the void reading as standing, dropping the self-applied condition, dropping the insured-work condition, and answering `JUST FALSE` for another disease; each was caught by between 1 and 8 failing assertions.
Swapping seat inputs of different grounds was also caught (three swaps tried), but swapping two inputs that sit in the same `OR`, or the same `AND`, of one ground is not (tried on the two inputs of § 3 no. 7): the answer cannot differ, and only the `@desc` would then be on the wrong input.
The six new `.l4` modules were emitted by scripts from one table of names, descriptions and expected sets, with the quote lines taken from `srcrefs.py quoteid`; the scripts are not deposited, so from here the `.l4` is edited by hand, and a reader who meets the 44 parallel `WITH` lines of the seat should know they were mechanical.
The guide asks for mirror cases where an Act has two seats; the requester and the worker share no facts, so there are none, and the agreement tests between the two requester layers are the nearest equivalent.
The seat tests reach the seat's exports by naming every input (`WITH`), true if the input's name is in a list the test writes, so each test reads as the boxes the person ticks; a misspelt name ticks nothing and a test that expects a ground then fails.

## Coverage table

| provision | disposition | where, or why |
|---|---|---|
| IFG § 1(1) sentence 1 | encoded | `the requester is entitled to access under the reading` |
| IFG § 1(1) sentences 2 and 3, (2), (3) | out-of-scope | other bodies, the form of access, other statutes' access rules: not the question |
| IFG § 2 | out-of-scope | not deposited; what is "amtliche Information" and who is a "Dritter" are asked as facts or characterisations (the section titles in this table are from the site's table of contents, read on 2026-11-02, not deposited) |
| IFG § 3 no. 1, limbs a to g | encoded | `section 3 no. 1 IFG bars access` (`bkv-ifg-law.l4`; forks F6 and F8) |
| IFG § 3 no. 2 | encoded | `section 3 no. 2 IFG bars access` |
| IFG § 3 no. 3, limbs a and b | encoded | `section 3 no. 3 IFG bars access` (fork F8) |
| IFG § 3 no. 4 | encoded | the limb "durch Rechtsvorschrift": `section 3 no. 4 IFG bars access under the reading` (`bkv-law.l4`); the other limbs: `section 3 no. 4 IFG bars access for a reason other than a statutory duty` (`bkv-ifg-law.l4`; fork F7) |
| IFG § 3 no. 5 | encoded | `section 3 no. 5 IFG bars access` |
| IFG § 3 no. 6 | encoded | `section 3 no. 6 IFG bars access` |
| IFG § 3 no. 7 | encoded | `section 3 no. 7 IFG bars access` (fork F11) |
| IFG § 3 no. 8 | encoded | `section 3 no. 8 IFG bars access` (fork F11) |
| IFG § 4(1) | encoded | `section 4(1) IFG says the application should be refused` (fork F9) |
| IFG § 4(2) | out-of-scope | the requester is to be told when the procedure ends: not a ground |
| IFG § 5(1) | encoded | `section 5(1) IFG bars access to personal data` (fork F10) |
| IFG § 5(2) and (3) | encoded | `the interest in access outweighs the interest of the third party under section 5 IFG` (fork F10) |
| IFG § 5(4) | out-of-scope | the names and office details of case handlers; it enters only through the weighing input (fork F10) |
| IFG § 6 | encoded | `section 6 IFG bars access` (fork F11) |
| IFG §§ 7 to 9 | out-of-scope | not deposited: the application and procedure, the part of third parties, and the refusal itself and legal remedy; the facts describe what is asked for (fork F12) |
| IFG §§ 10 to 15 | out-of-scope | fees, publication duties, the Commissioner, evaluation and commencement: not the question |
| BKV § 1(1) | encoded | `the disease is a listed occupational disease under the reading` (`bkv-worker-law.l4`) |
| BKV § 1(2) | inert | the Council's published results are to be taken into account first when deciding under SGB VII § 9(1) sentence 2 and § 9(2), including on the extent of the causal exposures; the Council's recommendation on No. 1322 is not deposited (fork F16) |
| BKV § 9(5) sentence 1 | encoded | the documents excepted from confidentiality |
| BKV § 9(5) sentences 2 and 3 | encoded | `section 9(5) BKV makes the document confidential under the reading`, in both wordings |
| BKV § 8(3), § 9(1) sentence 3, § 9(2) | inert | the members' duty of confidentiality and the non-public meetings; they enter only as the asked-as-fact input `another duty attaches` (fork F3) |
| BKV § 9(1) to (4) and the rest of the Regulation | out-of-scope | meetings, topics, recommendations: not the question |
| BKV Anlage 1 No. 1322 | encoded | `entry No. 1322 of Anlage 1 BKV describes the disease` (`bkv-worker-law.l4`; forks F14 to F16) |
| BKV Anlage 1 No. 1321 | inert | deposited for position: the gazette inserts No. 1322 after it |
| BKV Anlage 1, the rest of the list | out-of-scope | not deposited: the worker seat answers nothing for any other listed disease (the answer is `NOTHING`, "not covered") |
| SGB VII § 9(1a) sentence 4 | encoded | `the power needed to make the confidentiality rule` |
| SGB VII § 9(1) sentences 1 and 2 | encoded | `the power needed to list a disease`, the power for No. 1322 (fork F14) |
| SGB VII § 9(1) as a whole, § 9(6) and § 193(8) | inert | named in the 1997 preamble as powers cited |
| SGB VII § 9(1a) sentences 1 to 3, § 9(3) to (9) | out-of-scope | other provisions of § 9 |
| SGB VII § 9(2) and (2a) | out-of-scope | recognition like an occupational disease and the retroactive effect of listing; quoted at the end of `bkv-worker-law.l4` and in finding 9 (fork F17) |
| SGB VII §§ 2, 3 and 6 | out-of-scope | not deposited: who is insured; BKV § 1(1) refers to them, and the seat asks whether the pesticide use was part of insured work as one characterisation (fork F16) |
| BGBl. 2026 I Nr. 210, preamble | encoded | `the powers cited in the preamble of the Seventh Amending Regulation` |
| BGBl. 2026 I Nr. 210, Art. 1 No. 1 | encoded | the new wording of § 9(5) sentences 2 and 3 |
| BGBl. 2026 I Nr. 210, Art. 1 No. 2 (Anlage 1 No. 1322) | encoded | `entry No. 1322 of Anlage 1 BKV describes the disease`; the first pass had it out-of-scope, since the article does not touch it, and forks F2(b) and F14 ask what follows if it falls with the rest |
| BGBl. 2026 I Nr. 210, Art. 2 (in force 1 August 2026) | encoded | `entry No. 1322 of Anlage 1 BKV is in force on the day under the reading`; for the new wording of § 9(5) it stays inert, the reading being chosen by an input (fork F4) |
| BKV Eingangsformel (the 1997 preamble) | encoded | `the powers cited in the original preamble of the BKV` |
| Bundesrat Drucksache 312/26 | inert | the source of the earlier wording and of the government's stated reason and competence (findings 2 and 3), and of what listing settles and of the earlier recognition of the disease (findings 9 and 12) |
| Bundestag Drucksache 19/17586, pp. 47-48, 101-102 and 130-132 | inert | the bill that wrote §§ 7 to 11 BKV and its memorandum (finding 4, fork F3) |
| Grundgesetz Art. 80(1) sentence 3 | encoded | `the preamble cites the power`, `the 2026 amendment of section 9(5) BKV is void for want of citation` |
| BVerfG 2 BvF 3/90, paras. 151 to 158 | inert | the source of the citation rule, and of "Nichtigkeit der Verordnung" behind the reading `the Seventh Amending Regulation is void as a whole` (fork F14) |
| BVerwG 7 C 4.11, Rn. 29 to 34 | inert | read for fork F3 and for § 3 no. 3 b (fork F8); the encoding quotes para. 31 |

## Fork register

Each fork gives the readings, the one taken, and the text that licenses each.

**F1. Which reading answers?**
(a) *As in force from 1 August 2026*: the Council's "Beratungsunterlagen" are confidential, whoever made them.
(b) *As before the 2026 amendment*: only the "intern erstellten Beratungsunterlagen".
Taken: **both**, as separate questions, because no court is known to have ruled on (b); the article says it found the point itself.
The answer the Ministry gives today is (a).

**F2. How far does the voidness go?**
(a) Only the new sentences of § 9(5).
The article's reading, and the one encoded in the requester's questions.
(b) The whole Seventh Amending Regulation.
BVerfG 2 BvF 3/90 para. 158 speaks of "die Verordnung" (`bverfg-2bvf3-90-paras-151-158.txt:65-71`); on that reading Anlage 1 No. 1322 (Parkinson syndrome from pesticides) would fall with it, though § 9(1) sentence 1, which the preamble cites, is the power for it.
The article does not argue this.
Encoded for the worker's seat as the second reading of the Seventh Amending Regulation, beside the first (fork F14).

**F3. Exceptions to the citation requirement, and the Council members' duty.**
The article lists three follow-up considerations for Case 1 and rejects each ("highly unlikely"); the encoding has one input, `an exception applies`, for the citation questions and another, `another duty attaches`, for the third. Both sources the article relies on here were read on 2026-11-02:
- *§ 9(1a) SGB VII is not a legal basis but only explains the scope of § 9(1), so it need not be cited.* The article says the Federal Government itself names § 9(1a) as the base for "Durchführung der Beratungen und Veröffentlichung der Ergebnisse" in the explanatory memorandum to the 2020 bill. Read (Bundestag document 19/17586, p. 102, `btd-19-17586-p101-102.txt:97-99`, in the commentary on the new § 9 Absatz 1a that begins at line 39): "Das Nähere über die Stellung und die Organisation des Sachverständigenbeirats, wie etwa zur Stellung seiner Mitglieder, der Durchführung der Beratungen und der Veröffentlichung der Ergebnisse, sowie zu der Geschäftsstelle wird auf Basis der gesetzlichen Ermächtigung in der BKV geregelt". The article's quotation is accurate. The sentence says "gesetzliche Ermächtigung" and does not print "(1a) sentence 4", but it sits in the commentary on (1a). On the 2026 regulation's own memorandum, see finding 3. The input `an exception applies` carries the point.
- *If the amendment is void, the previous rule still bars access.* The article says it only protected internally created papers, and the 2026 text was changed to reach external ones. Both are true of the deposit (finding 2); the encoding's reading (b) takes the earlier wording as internal-only.
- *Members' duties of confidentiality and non-public meetings already bar access* (BKV § 8(3), § 9(1) sentence 3). The article says they should not be read as barring access to an independently prepared external statement merely because the Council considered it, and cites BVerwG 7 C 4.11 paras. 30 to 33. Read: the court held § 3 no. 4 IFG did not bar access to statements the Ministry had given the Petitions Committee, because "die von der Beklagten angeführten, auf die Arbeit des Petitionsausschusses bezogenen Vertraulichkeitsbestimmungen betreffen nur dessen Tätigkeit und dessen Informationen; im Verhältnis zum verfügungsberechtigten Bundesministerium sind sie ohne Bedeutung" (para. 30, `bverwg-7c4-11-excerpt.txt:4-5`), and it saw no impairment of the committee's deliberations from disclosing "eine nicht vom Petitionsausschuss stammende und insoweit externe Beratungsgrundlage" (para. 32, `:8-9`). That supports the article, with two limits: it concerned a parliamentary committee and not a ministry's expert council, and it left open whether § 3 no. 3 IFG could protect the statement as a pure consultation basis (para. 32 "kann dahinstehen"). The encoding makes the point the input `another duty attaches`: `TRUE` bars access under § 3 no. 4 even where § 9(5) does not reach the paper. § 8(3) binds "die Mitglieder" (`bkv-8.txt:7`), and § 3 no. 4 asks whether "die Information" is subject to a duty, which is a different thing; the encoding leaves the call to the person.
**Both inputs are legal judgments left to someone else.**

**F4. Which wording applies to a paper received before 1 August 2026?**
Art. 2 of the Seventh Amending Regulation puts the new wording in force on 1 August 2026 and says nothing of papers already held. The article's scenario does not say when the statement arrived. The encoding does not decide: the reading is chosen by the input and by the void test, not by a date. Open.

**F5. What is a "Beratungsunterlage"?**
The text does not define it. The government's memorandum says the earlier wording left it unclear whether "Eingaben und sonstige Korrespondenz an den ÄSVB" were confidential (`brd-312-26.txt:226-232`). Taken: a paper submitted to the Council for its deliberations is one; the requester states whether theirs was.

**F6. Which inputs of the grounds are facts, and which are judgments?**
Each ground of IFG §§ 3 to 6 is a rule over a small record of booleans (`Facts about section 3 no. 1`, and so on, in `bkv-ifg-law.l4`), and every field there carries a trailing comment: F for a fact a person can state, J for a judgment or characterisation that stays an input.
Taken: a fact is what a witness of ordinary competence could testify to; a judgment is left to the person as an input and never guessed (ENCODING-GUIDE section 4).
Judgments kept as inputs: every forecast in § 3 nos. 1, 2, 3 and 6 ("nachteilige Auswirkungen haben kann", "gefährden kann", "beeinträchtigt werden", "geeignet wäre") and in § 4(1) ("vereitelt würde"); the intention in § 3 no. 5 ("nicht Bestandteil der eigenen Vorgänge werden soll"); the interest of the third party in § 3 no. 7; the borrowed terms professional secret, special official secret, § 10 no. 3 of the Security Clearance Act, the special categories of Article 9(1) of the General Data Protection Regulation, intellectual property and trade or business secret; "unmittelbare Vorbereitung" in § 4(1); "entgegensteht" in § 6; the weighing of § 5(1); and every "atypical case" (forks F9 and F10).
Facts: the five facts about the request and the paper that `bkv-law.l4` already took; that the document is classified as a Verschlusssache (whether a classification must also be justified is not in the deposit); where the information came from and how it was handled (no. 5); how it was received (no. 7); which authority was asked (no. 8); that it is a draft or a third party's statement (§ 4(1)); that it holds personal data of a third party and whether and how that person consented; that the data come from certain files or are limited to certain details, and that the third party gave an expert opinion (§ 5); that the holder of a secret consented (§ 6).
Alternative: ask each ground as one yes/no. Not taken: it would ask the person a question about the law and hide which facts the answer turns on.
A requester often cannot know the authority's forecasts; each `@desc` says "answer as you expect it to decide" and the answer table shows what each ground does to the result.

**F7. § 3 no. 4: which limbs are new?**
(a) All of no. 4 in the new module.
(b) Only the limbs `bkv-law.l4` does not have.
Taken (b).
`bkv-law.l4` has the limb "durch Rechtsvorschrift", BKV § 9(5) and the input `another statutory confidentiality duty attaches`, and the brief keeps that module untouched.
The new module adds the limbs "Allgemeine Verwaltungsvorschrift zum materiellen und organisatorischen Schutz von Verschlusssachen geregelten Geheimhaltungs- oder Vertraulichkeitspflicht", "Berufsgeheimnis" and "besonderes Amtsgeheimnis" (`ifg-3.txt:15`), as three fields.
So `a ground for refusal other than section 3 no. 4 applies` leaves out no. 4 in every limb, as its name says, and `a ground for refusal other than a statutory duty applies` adds the new limbs; the seat passes the second to `bkv-law.l4`'s rule as `another ground for refusing access applies`, so that no statutory duty is counted twice.
The text of no. 4 could also be read as four limbs (statute, the administrative rule, professional secret, official secret) with "durch Rechtsvorschrift" as a kind of "Geheimhaltungs- oder Vertraulichkeitspflicht"; the split above is the same on any such reading.

**F8. § 3 nos. 1 to 3: forecasts, and "wenn und solange".**
Nos. 1 and 2 are forecasts and are inputs (F6).
No. 3 says "wenn und solange ... beeinträchtigt werden"; BVerwG 7 C 4.11 para. 31 reads it as an "Aufschub" ("grundsätzlich nur aufgeschoben"), reads the "notwendige Vertraulichkeit" of limb a into limb b, and says the end of the procedure is not an insurmountable limit (`bverwg-7c4-11-excerpt.txt:7`).
Para. 32 leaves open whether an outside statement that is a "reine Beratungsgrundlage" and allows no inference to the course of the committee's opinion-forming is protectable at all ("kann dahinstehen"), and finds it "nicht ersichtlich" that knowing of a later disclosure of such an external basis could impair the committee's will-forming (`bverwg-7c4-11-excerpt.txt:9`).
Taken: limb b is one input, answered as of the day of the decision; a later day is a different question and is not modelled.
Readings: (a) an outside statement the authority consulted is outside limb b; (b) every paper in the deliberation file is inside; (c) the person states whether disclosure would impair the deliberations.
Taken (c): the court left (a) open and decided its own case on its facts, so the finding is not turned into a rule.

**F9. § 4(1): "soll abgelehnt werden" and "regelmäßig".**
Sentence 1 says the application "soll abgelehnt werden" for drafts and the immediate preparation of a decision "soweit und solange" early disclosure would frustrate it, where § 3 says the claim "besteht nicht".
Sentence 2 says results of evidence-taking, expert opinions and statements of third parties "regelmäßig" do not serve the immediate preparation.
Taken: the ground applies when the paper serves the immediate preparation, early disclosure would frustrate the decision, and the case is not atypical; and a paper of the sentence-2 kinds serves it only if the person says the case is atypical in that way (two inputs, `a paper of that kind nevertheless serves ...` and `the case is atypical, so that the application should not be refused`).
Alternatives: (a) read sentence 2 as a flat exclusion, with no input; not taken, because of "regelmäßig".
(b) read "soll" as a discretion in every case; not taken: the text says "should", not "may".
The usual German reading of "soll" (a binding rule in the typical case, with room in an atypical one) is not in the deposited text; the encoding says only that the atypical case, stated as an input, displaces the ground.
A third party's statement that is also a draft: taken, sentence 2 prevails unless the atypical input is set; no test asserts it.
The answer is yes or no where the text gives a rule with exceptions (fork F12).

**F10. § 5(1) to (3): the weighing, the consent and the special categories.**
The weighing of § 5(1) sentence 1 is a judgment and an input.
§ 5(2) says the interest of the requester "überwiegt nicht" for information from documents about the third party's service or office relationship or a mandate, "und" for information under a professional or official secret (`ifg-5.txt:3`); § 5(3) says it outweighs "in der Regel" when the data are limited to name, title, academic degree, professional or functional designation, office address and office telephone number and the third party gave an opinion in a proceeding as an expert or in a comparable way (`ifg-5.txt:4`).
Taken: the "und" of § 5(2) joins two cases, each enough; § 5(2) prevails over § 5(3) when both apply, because it is categorical where § 5(3) is a rule with exceptions; § 5(3) needs both of its conditions and gives way to an atypical case, an input.
Not taken: (a) "und" as cumulative, which would make § 5(2) reach only information that is both; (b) § 5(3) prevailing, which would let an expert's office details be released from documents about their service relationship. The text decides neither; the register records the reading and one row of the tests asserts it.
Sentence 2 of § 5(1): data of the special categories of Article 9(1) of the General Data Protection Regulation (not deposited) may be transmitted only if the third party "ausdrücklich eingewilligt hat"; taken: for them only express consent opens access, whatever the weighing; for other personal data consent, express or not, or a favourable weighing is enough.
§ 5(4), the names and office details of case handlers, "soweit sie Ausdruck und Folge der amtlichen Tätigkeit sind und kein Ausnahmetatbestand erfüllt ist", is not encoded: which exemption it refers to is not settled by the deposit, and it enters only through the weighing input.

**F11. § 3 nos. 5 to 8 and § 6: the structure of the limbs.**
No. 5 needs all three of: information of another public body, drawn in only temporarily, not to become part of the authority's own records.
No. 6 is either of the two interests.
No. 7 needs both: the information was received in confidence, and the third party's interest in confidential treatment "im Zeitpunkt des Antrags noch fortbesteht"; the article's footnote 8, "submitted as non-confidential", is the first being false.
No. 8 is either: an intelligence service is asked, or a federal body performing tasks within § 10 no. 3 of the Security Clearance Act and the request concerns them; that Act is read but not deposited (§ 10 no. 3 there speaks of persons working for an intelligence service or for a federal body that the Federal Government has found, under its § 34, to perform tasks of comparable security sensitivity), so the second limb stays a characterisation.
§ 6 sentence 1 needs intellectual property and that its protection stands in the way; sentence 2 bars trade or business secrets unless the person concerned consented.
Whether the consent of a right-holder is already inside "entgegensteht" is not settled by the text; it is an input.

**F12. The grounds are asked of the information as asked for, and their three modalities are flattened.**
"soweit" occurs in § 3 nos. 7 and 8, § 4(1), § 5(1) and § 6: access may be allowed to the part that is not protected.
Partial access is the subject of IFG § 7(2), read on 2026-11-02 but not deposited: "Besteht ein Anspruch auf Informationszugang zum Teil, ist dem Antrag in dem Umfang stattzugeben, in dem der Informationszugang ohne Preisgabe der geheimhaltungsbedürftigen Informationen oder ohne unverhältnismäßigen Verwaltungsaufwand möglich ist."
The same page says in § 7(1) sentence 3 that a request that concerns data of third parties within § 5(1) and (2) or § 6 "muss begründet werden"; that is not encoded either.
Taken: the facts describe the information the person asks for, and a person who asks only for the unprotected part answers about that part.
The grounds say "besteht nicht" (§ 3, § 6 sentence 1), "soll abgelehnt werden" (§ 4(1)) and "darf nur gewährt werden, soweit" (§ 5(1), § 6 sentence 2); each is returned as one yes or no, `a ground applies`, with the exceptions carried by the atypical-case inputs.

**F13. How the grounds reach the first layer's rule.**
`bkv-law.l4`'s `the requester is entitled to access under the reading` reads one field, `another ground for refusing access applies`.
Taken: the second seat layer builds that record with the field set from `a ground for refusal other than a statutory duty applies` and calls the rule unchanged.
Not taken: a new entitlement rule in the IFG law module, which would restate the first and let the two drift; editing `bkv-law.l4`, which the brief keeps untouched.
The two layers agree where they should: `bkv-ifg-tests.l4` asserts the same answers for the journalist's case and for the case with the one input true (one spelled-out ground against the single input).

**F14. The worker: does the whole Seventh Amending Regulation fall?**
(a) Only the new sentences of § 9(5) fall, so the new Anlage 1 entry stands.
(b) The whole Regulation falls: "Nichtigkeit der Verordnung" in BVerfG 2 BvF 3/90 para. 158, applied to the Regulation entire.
Both are encoded, as `Reading of the Seventh Amending Regulation`: `the Seventh Amending Regulation stands` and `the Seventh Amending Regulation is void as a whole`, because the answer differs.
The brief's assessment is that (a), severability, is the stronger view, and that (b) is encoded only because the article's engine speaks of "die Verordnung"; this encoder records that as the brief's assessment and gives the evidence found, which does not settle it.
For (a): the power for No. 1322, § 9(1) sentences 1 and 2 SGB VII, is cited in the preamble (`bgbl-2026-i-210.txt:12-14`; asserted in `bkv-worker-tests.l4`), and the government's memorandum names the same provisions as its competence (`brd-312-26.txt:283-284`); the court says the executive must find its power "gerade aus den von ihr selbst angeführten Vorschriften" and must see its norm-setting programme through the citation (para. 154, `bverfg-2bvf3-90-paras-151-158.txt:30-37`), which is satisfied for the entry.
For (b): para. 158 speaks of "die Verordnung" (`bverfg-2bvf3-90-paras-151-158.txt:66-71`), and para. 156 says a regulation need not state for each provision which power it rests on (`bverfg-2bvf3-90-paras-151-158.txt:54-56`), so the unit of the test is the regulation.
The deposit has no passage on partial nullity ("Teilnichtigkeit"), so no deposited authority settles the choice.
Not encoded: a middle reading, such as void only for the provisions no cited power covers; that is (a) here.

**F15. The worker: the date.**
Art. 2 puts the Regulation in force on 1 August 2026 (`bgbl-2026-i-210.txt:33`).
Taken: on reading (a) the entry is in force on and after that day; on reading (b) never, since "Nichtigkeit" is not repeal; whether voidness acts from the start or only from a ruling is not in the deposit.
The date input is the day for which the person asks, such as the day of the request to the insurer.
It is not the day the illness arose or began: SGB VII § 9(5) fixes the time of the insured event, for benefit rules, at the beginning of the incapacity for work or the need for treatment (or, if better for the insured person, of the pension-qualifying reduction in earning capacity), and § 9(2a) no. 1 lets an earlier illness be recognised retroactively at the earliest from the day the designation came into force (`sgb7-9.txt:11` and `:5-6`); neither is encoded.

**F16. The worker: the words of the entry.**
"langjährig", "häufig", "selbst angewendete", "durch" and "Pestizide" are not defined in the deposit, and the entry gives no figures.
The Council's published recommendation (Gemeinsames Ministerialblatt Nr. 10-11 of 20 March 2024, p. 194 ff., and the updated one, Nr. 44-45 of 28 November 2025, p. 971 ff., both named in `brd-312-26.txt:246-249`) is not deposited and may fix what they mean.
Taken: each of the three adjectives and "durch" is an input, as a characterisation; "selbst angewendete" is a fact; "infolge einer den Versicherungsschutz nach § 2, 3 oder 6 ... begründenden Tätigkeit" (BKV § 1(1), `bkv-1.txt:2`) is one characterisation, since SGB VII §§ 2, 3 and 6 are not deposited.
Listing is not recognition in the individual case (finding 12): the seat answers whether the disease is the listed one, with the individual cause as an input.

**F17. The worker: a disease that is not listed.**
SGB VII § 9(2) has the insurers recognise a disease that is not in the Regulation like an occupational disease when current medical findings meet the conditions for designating it, and § 9(2a) no. 2 dates that from the day the findings existed or, once the Council has recommended a new disease, from the day of its resolution (`sgb7-9.txt:4` and `:7`).
Not encoded: whether the conditions are met is a medical and legal judgment, and the day of the Council's resolution is not in the deposited sources, only the dates of the Council's published recommendations (`brd-312-26.txt:246-249`).
The Federal Government says Parkinson's disease caused by work is already recognised this way and that the two routes give the same benefits (finding 9).
So a no from the worker seat on reading (b) does not end the claim, and the export text says so.

## What the law turns out to say

1. **The Seventh Amending Regulation replaced sentence 2 of § 9(5) with two sentences** (Art. 1 No. 1, `bgbl-2026-i-210.txt:22-24`) and inserted Anlage 1 No. 1322 (No. 2, lines 25-26); it is in force from 1 August 2026 (Art. 2) with the Bundesrat's consent (`bgbl-2026-i-210.txt:38`). Its preamble names one power, "§ 9 Absatz 1 Satz 1 und 2" SGB VII (lines 12-14). Asserted in `bkv-tests.l4`.
2. **The government's own memorandum calls the change a clarification and says why.** Drucksache 312/26: "durch eine Präzisierung in § 9 Absatz 5 Satz 2 BKV klargestellt, dass sämtliche Beratungsunterlagen des ÄSVB vertraulich sind. Die Regelung bezog sich bislang ihrem Wortlaut nach auf die intern erstellten Beratungsunterlagen. Hierdurch war nicht eindeutig, ob zum Beispiel Eingaben und sonstige Korrespondenz an den ÄSVB ... ebenfalls vertraulich zu behandeln sind" (`brd-312-26.txt:226-232`). So the earlier wording was internal-only, as the article says, and the government's aim was to reach external submissions. The government also calls it "nicht eindeutig", which is the other side of the article's "highly unlikely" follow-up on the previous rule.
3. **The memorandum names § 9(1) SGB VII as the whole regulation's basis, and names no power for the § 9(5) change.** Section V, "Regelungskompetenz", says the competence "ergibt sich aus § 9 Absatz 1 Satz 1 und Satz 2 SGB VII" (`brd-312-26.txt:283-285`); a search of the extracted text for "1a", "Ermächtigung", "Rechtsgrundlage" and "Zitier" finds only line 627, about the disease list. That matches the premise of the article's argument (the government did not rely on § 9(1a) sentence 4); whether § 9(1a) sentence 4 is a power at all is the article's first follow-up (F3).
4. **The original BKV preamble does not cite § 9(1a) either**, only "§ 9 Abs. 1 und 6 und des § 193 Abs. 8" SGB VII (`bkv-eingangsformel.txt:2`). The preamble printed on the site is the 1997 one. **§§ 7 to 11 (the Council) were not introduced by a regulation at all: Parliament wrote them**, as Article 24 of the Siebtes Gesetz zur Änderung des SGB IV of 12 June 2020 (BGBl. I S. 1248, in force 1 January 2021; the bill's text is deposited as `btd-19-17586-p47-48.txt`, where the original § 9(5) reads "Die vorbereitenden, intern erstellten Beratungsunterlagen des Sachverständigenbeirats sind vertraulich", lines 73 to 74). The bill's memorandum on Article 24 (`btd-19-17586-p130-132.txt`, lines 69 to 72) says the Federal Government "ist nach Satz 2 der Vorschrift [§ 9 Abs. 1a] ermächtigt, das Nähere über die Stellung und die Organisation des Sachverständigenbeirats und der Geschäftsstelle in der Rechtsverordnung über die Bezeichnung der Berufskrankheiten, das heißt in der BKV, zu regeln" (sentence 4 in the enacted text). So the document that enacted §§ 7 to 11 named § 9(1a) as the power for them, which is the premise of the article's Case 1. The Fünfte Verordnung zur Änderung der BKV of 29 June 2021 cited "§ 9 Absatz 1 Satz 1 und 2" and amended only Anlage 1 (read on umwelt-online.de, not deposited). No clause returning the statute-amended parts of the BKV to Verordnungsrang was found in the bill text of 19/17586 (grep for "Verordnungsrang", "beruhenden Teile", "durch Rechtsverordnung geändert werden"); the enacted text was not checked. Whether a provision Parliament wrote into a regulation can be amended by regulation at all is a separate question from the citation one and is not pursued here.
5. **§ 9(1a) sentence 4 reads**: "Das Nähere über die Stellung und die Organisation des Sachverständigenbeirats und der Geschäftsstelle regelt die Bundesregierung in der Rechtsverordnung nach Absatz 1" (`sgb7-9.txt:3`). Whether the confidentiality of the Council's papers is part of its "Stellung und Organisation" is the legal question under the article's first follow-up; the encoding does not answer it.
6. **The earlier wording is deposited only through the memorandum** ("intern erstellten Beratungsunterlagen"). The full earlier sentence is quoted in the article from de.openlegaldata.io, not deposited.

7. **IFG § 4(1) sentence 2 speaks to the article's statement.** "Nicht der unmittelbaren Entscheidungsvorbereitung nach Satz 1 dienen regelmäßig Ergebnisse der Beweiserhebung und Gutachten oder Stellungnahmen Dritter" (`ifg-4.txt:2`).
   An association's written statement is a statement of a third party, so § 4(1), the ground about the preparation of a decision, regularly does not reach it; the "regelmäßig" leaves an atypical case, which the encoding takes as an input (fork F9).
   Asserted in `bkv-ifg-tests.l4` (the `§ 4(1)` rows and the seat's case).
8. **§ 3 no. 3 b is a deferral and the court left the external basis open.** The Federal Administrative Court reads "wenn und solange" as "grundsätzlich nur aufgeschoben" and leaves open whether an outside statement that shows nothing of the committee's opinion-forming is protectable at all (`bverwg-7c4-11-excerpt.txt:7` and `:9`).
   So a refusal on § 3 no. 3 b lasts at most while the deliberations are impaired, and whether it is available for an outside statement was left open in that case.
   Not asserted: it is the court's finding on its own facts, not a rule the encoding can test (fork F8).
9. **Before 1 August 2026 the disease was already recognised, and by the same benefits.** Drucksache 312/26: "Ab dem Zeitpunkt, zu dem der ÄSVB eine Empfehlung für eine neue Berufskrankheit beschließt, ist diese Erkrankung durch die Unfallversicherungsträger als sogenannte 'Wie-Berufskrankheit' anzuerkennen und zu entschädigen (§ 9 Absatz 2 in Verbindung mit Absatz 2a Nummer 2 SGB VII)" (`brd-312-26.txt:56-59`), and "Beruflich bedingte Parkinson-Erkrankungen sind nach geltender Rechtslage bereits als sogenannte 'Wie-Berufskrankheit' ... anzuerkennen.
   Wie-Berufskrankheiten und Berufskrankheiten, die in die Anlage 1 der BKV aufgenommen sind, lösen dieselben Leistungsansprüche nach dem SGB VII aus" (`brd-312-26.txt:329-333`).
   So on reading (b) of fork F14 a worker who is told "not listed" may still be recognised under § 9(2), and the government says the benefits are the same; the worker seat's second question says so in its export text.
   Not encoded (fork F17).
10. **The power for No. 1322 is cited.** The preamble names "§ 9 Absatz 1 Satz 1 und 2" SGB VII (`bgbl-2026-i-210.txt:12-14`), which are the power to designate diseases by regulation (`sgb7-9.txt:2`), and the memorandum names the same provisions as the competence of the whole Regulation (`brd-312-26.txt:283-284`).
    The preamble does not cite § 9(1a) sentence 4.
    Both facts are asserted in `bkv-worker-tests.l4` (the second also in `bkv-tests.l4`): the defect the article finds for the § 9(5) change is not a defect of the citation for the new entry.
11. **The official consolidated list already carries No. 1322, and it prints a note between Nos. 1321 and 1322.** The page read on 2026-11-02 has No. 1322 after a note, "Zu den Nummern 1101 bis 1110, 1201 und 1202, 1303 bis 1309 und 1315: Ausgenommen sind Hauterkrankungen ...", that is about other numbers; the gazette says No. 1322 is inserted "nach Nummer 1321" (`bgbl-2026-i-210.txt:25-26`).
    The deposited excerpt leaves the note out, as the metadata of `bkv-anlage-1-nrn-1321-1322` says.
12. **Listing is not recognition in the individual case.** Drucksache 312/26: "Mit Aufnahme in die Anlage 1 der BKV wird festgestellt, dass die betreffenden Pestizid-Einwirkungen generell geeignet sind, das Parkinson-Syndrom zu verursachen.
    Für die Anerkennung als Berufskrankheit im Einzelfall bedarf es zusätzlich der Feststellung über die individuellen Ursachenzusammenhänge durch die Unfallversicherungsträger" (`brd-312-26.txt:252-257`).
    That is why "caused by pesticides" is an input of the worker seat and why the seat says "listed", not "recognised" (fork F16).
    The date and all the entry's conditions are asserted in `bkv-worker-tests.l4`.

## Answer tables

The first table is the first layer's, with the grounds asked as one input.

| the paper | access as § 9(5) stands | access if the 2026 amendment is void |
|---|---|---|
| external statement submitted to the Council (the article's case) | no | yes |
| paper made inside the Council or the Ministry | no | no |
| a recommendation, opinion or closing report | yes | yes |
| a paper never submitted to the Council | yes | yes |
| any of these where another ground for refusal applies | no | no |

(Each row assumes a request to a federal authority and no other statutory confidentiality duty.)

The second table is the second layer's, for the article's case: a request to a federal authority for an association's external statement submitted to the Council, with every other input false unless the row says otherwise (`bkv-ifg-tests.l4`, "Cases: the entitlement question").
In the first column § 9(5) as in force already makes the statement confidential, so access is barred whatever else is true; the second column is the reading in which the 2026 amendment is void and no exception to the citation requirement is accepted, so that the ground in the row alone decides.

| the ground raised, and the facts that raise it | access, § 9(5) as in force | access, if the amendment is void |
|---|---|---|
| none: the article's footnote 8 | no | yes |
| § 3 no. 7: received in confidence, and the third party still wants confidence | no | no |
| § 3 no. 7: received in confidence, but that interest has ended | no | yes |
| § 3 no. 1: harm to international relations | no | no |
| § 3 no. 2: danger to public safety | no | no |
| § 3 no. 3 b: disclosure now would impair an authority's deliberations | no | no |
| § 3 no. 4, other limbs: classified as a Verschlusssache, or a professional secret | no | no |
| § 4(1): the statement is a third party's statement and early disclosure would frustrate the decision | no | yes |
| § 4(1): a draft of a decision that early disclosure would frustrate | no | no |
| § 5(1): personal data of a third party, no consent, no favourable weighing | no | no |
| § 5(1): the same, with the third party's consent | no | yes |
| § 6 sentence 1: copyright standing in the way | no | no |
| § 6 sentence 2: a trade secret, without the holder's consent | no | no |
| § 6 sentence 2: the same, with the holder's consent | no | yes |

The grounds that are asserted alone in the law layer's tests but not in a row above (§ 3 no. 1 limbs b to g, no. 3 a, nos. 5, 6 and 8, § 5(1) with the special categories or § 5(2), § 5(3)) are in the tests' ground-by-ground rows, with the facts that raise each.
The list of grounds that apply, for the same case, is `section 3 no. 4 by a statute` when § 9(5) stands and nothing when the amendment is void, and each ground raised alone is listed under its own name (asserted for every ground, with the document inputs false).

The third table is the worker's: a Parkinson syndrome with the entry's conditions met unless the row says otherwise (`bkv-worker-tests.l4`).

| the worker | the Seventh Amending Regulation stands | the Seventh Amending Regulation is void as a whole |
|---|---|---|
| all conditions met, asked for 1 August 2026 or a later day | listed | not listed |
| all conditions met, asked for 31 July 2026, the day before | not listed | not listed |
| not caused by pesticides | not listed | not listed |
| not applied over many years | not listed | not listed |
| not applied often | not listed | not listed |
| not applied by the worker | not listed | not listed |
| the use was not part of insured work | not listed | not listed |
| another disease | nothing (not covered) | nothing (not covered) |

(A "not listed" on the second reading does not decide whether the disease can still be recognised like an occupational disease: findings 9 and 12, fork F17.
Whether each condition is met is the worker's input.)

## Checks run

`./check.sh` in this folder, target `main`, on 2026-11-02 (the `l4` is a dev build, 25a091f4...; the main build compared with is 1.6.108 (main, 2ae7c9b, 2026-11-02)); it exited 0.
A count of `DiagnosticSeverity_Warning` over `l4 run` of each of the ten modules, with the dev build and with the main build, is 0 for every module (`check.sh` counts errors only):

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.108 (main, 2ae7c9b, 2026-11-02)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
bkv-cases-seat.l4                              0        11       0        0         0 |      0        11       0        0  same
bkv-ifg-law.l4                                 0         0       0        0         0 |      0         0       0        0  same
bkv-ifg-seat.l4                                0         0       0        0         0 |      0         0       0        0  same
bkv-ifg-tests.l4                               0       200       0        0         0 |      0       200       0        0  same
bkv-law.l4                                     0         0       0        0         0 |      0         0       0        0  same
bkv-seat.l4                                    0         0       0        0         0 |      0         0       0        0  same
bkv-tests.l4                                   0        22       0        0         0 |      0        22       0        0  same
bkv-worker-law.l4                              0         0       0        0         0 |      0         0       0        0  same
bkv-worker-seat.l4                             0         0       0        0         0 |      0         0       0        0  same
bkv-worker-tests.l4                            0        29       0        0         0 |      0        29       0        0  same
TOTAL (10 modules)                             0       262       0        0           |      0       262       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

The four modules of the first pass keep their counts: 11 assertions in `bkv-cases-seat.l4` and 22 in `bkv-tests.l4`, and none in `bkv-law.l4` and `bkv-seat.l4`.
The six new modules add 229 satisfied assertions: 200 in `bkv-ifg-tests.l4` and 29 in `bkv-worker-tests.l4`.
`python3 -I srcrefs.py check --refs ../../registers/source-bundle/ifg-1.txt <module>`:
- `bkv-law.l4`: 24 src: lines, 7 runs, 10 locators, 0 problems.
- `bkv-ifg-law.l4`: 24 src: lines, 12 runs, 15 locators, 0 problems.
- `bkv-worker-law.l4`: 29 src: lines, 9 runs, 9 locators, 0 problems.

No assertion is expected to fail. The check does not see a different trace outcome; the encoding has no regulative rule and no `#TRACE`.
What the tests cannot see: a swap between two seat inputs that sit in the same `OR`, or the same `AND`, of one ground (Method); the wording of an `@desc` against its input; and any reading of a text that the encoder and the test author, who is the same encoder, share.
The positive controls (rule mutations that fail the tests) are described under Method; they were run on scratch copies and are not part of the folder.

## Before this is worth relying on

- Get the earlier text of § 9(5) from the gazette and the preamble that introduced §§ 7 to 11 BKV, and decide F4.
- Decide F3 with someone who knows German administrative and information-access law.
- Have someone who knows German information-access law read forks F6 to F13: the split of facts from judgments, the reading of "soll" and "regelmäßig" in § 4(1), the priority of § 5(2) over § 5(3), and the flattening of three modalities into one yes or no.
- Deposit what the grounds borrow, so that the borrowed characterisations can be worked out and not asked: IFG § 2 (what is "amtliche Information" and "Dritter") and § 7 (partial access, and that a request touching third-party data must give reasons), Security Clearance Act § 10 no. 3, Article 9(1) of the General Data Protection Regulation, and the sources for "professional secret" and "special official secret".
- Decide, with that reader, whether a form of 49 inputs for the requester is the right shape or whether the grounds should be asked in two steps (the coarse yes or no for each ground first); the question planner may already ask only what the answer needs.
- Deposit the Council's published recommendation on Parkinson syndrome from pesticides (Gemeinsames Ministerialblatt Nr. 10-11 of 20 March 2024 and Nr. 44-45 of 28 November 2025), which may say what "langjährig" and "häufig" mean, and SGB VII §§ 2, 3 and 6, which BKV § 1(1) refers to.
- Decide fork F14 with someone who knows the law on partial nullity of regulations: the register attributes severability as the stronger view to the brief and gives evidence for it, which does not prove it.
- Encode, or decide not to, the route of SGB VII § 9(2) and (2a) for a disease that is not listed, which the government says gives the same benefits (finding 9).
- Have a domain expert read the encoding against the German text (the pipeline's HG1).
- Ask an independent test author, who has not seen this encoding, to write expectations for the grounds and for the worker's entry from the German text; the tests here were written by the encoder.
