# NOTES -- Soldatengesetz § 30c and Soldatenarbeitszeitverordnung § 1 (time off for soldiers' overtime), L4 encoding by agent `saz` (Sonnet 5.5, solo)

This encodes the right of a soldier to time off for ordered overtime (SG § 30c(2)), the exemption that takes soldiers posted to listed international establishments out of it (SAZV § 1(2) and its Anlage), the power that exemption needs (SG § 30c(6) with § 93(2) no. 7), and the constitutional test that the article by Felix Ringe and Linus Folkerts says the 2025 listing of JSEC fails.
It does not decide whether the test is failed: it answers the soldier's question under both readings and says which facts each rests on.

The sources are in `../../registers/source-bundle/`: plain-text conversions of per-norm pages of gesetze-im-internet.de read on 2026-11-02, the gazette text of the 2025 amending regulation (BGBl. 2025 I Nr. 78, text and PDF) and an excerpt of BVerfG 2 BvF 3/90, each with its `.meta.json`.
The consolidated texts are the site's reading versions; the gazette is the promulgated text.
The target is `main`: the build compared with is 1.6.108 (main, 2ae7c9b, 2026-11-02).
Modules: `saz-law.l4` (the law layer), `saz-seat.l4` (the seat), `saz-tests.l4` and `saz-cases-seat.l4`.

## Seat

The seat is **a soldier serving within the remit of the Federal Ministry of Defence**: the person SG § 30c and SAZV § 1 are applied to.
Their questions, in `saz-seat.l4`, under `§` groups:

- Do § 30c(1) to (3) of the Soldiers Act, which give time off for overtime, apply to me, reading the annex as it is printed? And if the 2025 listing of my establishment is void? (the second only arises for a soldier posted to the establishment the article names, JSEC; the group's comment says so)
- How many hours of time off must I be given for this month's overtime, on each reading?
- Within how many months must the time off be given (12, or 6 where the shorter period for soldiers in the armed forces has been set)?
- Does the preamble of the 2025 amending regulation cite § 30c(6) with § 93(2) no. 7?

The inputs are facts the soldier can state: whether they serve within the Ministry's remit, the establishment where they are posted (as the annex prints its name), whether they were assigned there for international tasks, whether the work is an activity listed in § 30c(4), the overtime hours, and the hours that compelling service reasons make impossible.
"An activity listed in § 30c(4)" is a characterisation asked as a fact: the list (operations, disaster aid, multi-day sea voyages, ...) is long and its edges are judgments.
The people the text also addresses are the Ministry (it issues the regulation) and the unit commander (who orders or refuses time off): neither has a seat.

## Method

One agent, working alone, from the deposited sources and the article.
`saz-law.l4` holds the nouns (`Soldier`, `Annex row`), the annex as data (88 rows, generated from lines 4 to 91 of `sazv-anlage.txt` by script and checked by count and by rows 27, 76 and 88), the exclusion of § 1(2), the entitlement of § 30c(2), the period, and the citation test of Art. 80(1) sentence 3 GG with the powers the preambles cite.
`saz-seat.l4` holds no rule: it builds the law layer's record from plain inputs and calls the law layer.
The only field it does not ask is `has a long-term working-time account`, set to a fixed `FALSE` and commented: no seat question reads it (SAZV § 1(3) is encoded in the law layer and tested, but not exported, because § 17 SAZV is not deposited).
Every rule has an `@ref` with locators; `srcrefs.py` checked 16 quote lines and 16 locators, 0 problems.
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
| SG § 93(2) nos. 6, 8 | inert | named in the 2025 preamble list |
| SG § 93(2) no. 7 | encoded | the power to make the regulation that disapplies § 30c(1) to (3) and (5) |
| SG § 93(1), (2) nos. 1 to 5 and 9, (3), (4) | out-of-scope | other powers |
| SAZV § 1(1) | encoded | `the Regulation applies to the soldier under the reading` |
| SAZV § 1(2) | encoded | `section 1(2) SAZV takes the soldier out of the working-time rules under the reading` |
| SAZV § 1(3) | encoded | `the soldier's long-term working-time account is suspended under the reading`; not exported |
| SAZV Anlage (88 rows) | encoded | `the rows of the annex as printed`, with the one entry the article says was added |
| SAZV Eingangsformel (the original 2015 preamble) | encoded | `the powers cited in the original preamble of the SAZV` |
| SAZV §§ 2 to 21 and the rest | out-of-scope | the Regulation's working-time machinery; the question is whether a soldier is out of it |
| BGBl. 2025 I Nr. 78, preamble | encoded | `the powers cited in the preamble of the 2025 amending regulation` |
| BGBl. 2025 I Nr. 78, Art. 5 No. 7 (the Anlage recast) | inert | the annex is encoded as data; see finding 1 |
| BGBl. 2025 I Nr. 78, Arts. 1 to 4, 5 Nos. 1 to 6, 6, 7 | out-of-scope | other amendments |
| Grundgesetz Art. 80(1) sentence 3 | encoded | `the preamble cites the power`, `the 2025 listing is void for want of citation` |
| Grundgesetz Art. 80(1) sentences 1, 2 and 4, (2) to (4) | out-of-scope | not argued |
| BVerfG 2 BvF 3/90, paras. 151 to 158 | inert | the source of the citation rule |

## Fork register

Each fork gives the readings, the one taken, and the text that licenses each.

**F1. Which reading answers?**
(a) *As printed*: the annex as it stands, JSEC at No. 27. What the unit applies today.
(b) *Without the establishment the 2025 regulation added*: JSEC drops out and the rest stays.
Taken: **both**, as separate questions, because no court is known to have ruled on (b); the article says it found the point itself.

**F2. How far does the voidness go?**
(a) Only JSEC. The article's reading, and the one encoded; it rests on the article's statement that the previous annex (BGBl. 2022 I S. 1533) did not list JSEC, which was **not checked**: the 2022 gazette was not obtained.
(b) The whole annex as re-enacted. The 2025 regulation does not "add" JSEC: Art. 5 No. 7 says "Die Anlage zu § 1 Absatz 2 wird wie folgt gefasst" and prints all 88 rows (`bgbl-2025-i-78.txt:176`). If the defect voids what the regulation enacted, the whole recast annex falls, and what remains is whatever the 2022 annex listed, which the deposit does not hold.
(c) The whole amending regulation: BVerfG 2 BvF 3/90 para. 158 speaks of "die Verordnung" (`bverfg-2bvf3-90-paras-151-158.txt:65-71`).
The encoding follows (a) because (b) and (c) need a text it does not have; a soldier posted to any other establishment gets the same answer under both readings only if that establishment was in the 2022 annex.

**F3. Exceptions to the citation requirement.**
The article lists three follow-up considerations for Case 3 and rejects each; the encoding has one input, `an exception applies`, that stands for the judgments they call for:
- *The exemption is covered by other cited legal bases.* The article says no: § 30c(5) sentence 1 no. 2 concerns protective measures for the activities of § 30c(4), and § 30d(1) leaves § 30c(1) to (3) untouched. Both are true of the deposited text (`sg-30c.txt:23-29`, `sg-30d.txt:8`), and the encoding's test is membership of the needed power in the cited list, so it reads as the article does. A court might read some cited power as wide enough; the encoding cannot say.
- *If the new rule is void, JSEC remains exempt under the predecessor rule.* The article says no, because the previous annex did not list it (not checked, F2).
- *Earlier citations suffice for a limited amendment.* The article says "highly unlikely": OVG NRW 3 A 1217/14 accepted an earlier citation under state constitutional law, BVerwG 2 C 31.15 left that undisturbed within its limited scope of review, and the article does not think it applies because JSEC extends the exemption to a new group of soldiers, and because the original SAZV preamble does not cite § 30c(6) either (`sazv-eingangsformel.txt:2`: "§ 30c Absatz 5 in Verbindung mit § 93 Absatz 2 Nummer 5"; tested). The judgments were **not read**; the encoding carries them only as the `TRUE` branch of the input.
**The input is a legal judgment left to someone else: `TRUE` makes the listing stand.**

**F4. "Diese Mehrarbeit" in § 30c(2) sentence 2.**
(a) All the ordered overtime, once more than five hours are reached (the article's reading, and the one encoded: ten hours give ten hours).
(b) Only the hours above five. The words "für diese Mehrarbeit" refer back to the overtime that exceeded five hours, which can be read either way. Tests assert 5 gives 0, 5.5 gives 5.5, 6 gives 6.

**F5. "Soweit" in sentence 5**, "Eine Dienstbefreiung wird nicht gewährt, soweit sie aus zwingenden dienstlichen Gründen nicht möglich ist", is read as a reduction by the number of hours so blocked, not as an all-or-nothing bar.

**F6. The remit.**
§ 30c(1) sentence 1 ties the 41-hour week to soldiers "im Geschäftsbereich des Bundesministeriums der Verteidigung verwendet", and sentence 3 sends others to the receiving body's law. § 30c(2) says only "der Soldat". The encoding asks the remit only for SAZV § 1(1), and treats § 30c(2) as applying to any soldier not excluded and not in a § 30c(4) activity.

**F7. The six-month period** ("kann ... verkürzt werden") is taken as an input: the soldier says whether it has been set for them.

## What the law turns out to say

1. **The 2025 regulation recast the whole annex; it did not add one row.** Art. 5 No. 7 of BGBl. 2025 I Nr. 78 says "Die Anlage zu § 1 Absatz 2 wird wie folgt gefasst" and prints 88 rows, JSEC at No. 27 (`bgbl-2025-i-78.txt:176-283`); the site's annex has the same 88 rows. The article's "amended to add JSEC" is a statement about the difference with the 2022 annex, which was not obtained (F2). Asserted: 88 rows and row 27 in `saz-tests.l4`.
2. **The 2025 preamble names eight powers and not § 30c(6).** It names BBesG § 50b(1), § 56(6) and § 53(7); BBG § 83(4); BUKG § 14(1) sentence 1 and (3) no. 7; SG § 30c(5) sentence 1 no. 2 with (4) and § 93(2) no. 6; SG § 30d(1) sentence 1 with § 93(2) no. 8; and ArbSiG § 38(1) (`bgbl-2025-i-78.txt:14-50`). Asserted in `saz-tests.l4`, with controls.
3. **The original 2015 preamble does not cite § 30c(6) either**, only "§ 30c Absatz 5 in Verbindung mit § 93 Absatz 2 Nummer 5" (`sazv-eingangsformel.txt:2`). The article uses this against the earlier-citation exception. It bears on a second question the article does not raise: whether § 1(2) SAZV itself, and so the annex mechanism, was validly made under that preamble. Whether § 30c(6) existed when § 1(2) was inserted is not in the deposit. Not argued, not encoded.
4. **§ 93(2) no. 7 reaches subsection (5) as well**: "die Nichtanwendung des § 30c Absatz 1 bis 3 und 5 nach § 30c Absatz 6" (`sg-93.txt:20`). The exemption removes the soldier from the Regulation made under (5) as well as from the three subsections.
5. **Not every annex row is obviously a multinational establishment.** § 30c(6) reaches soldiers "bei militärischen Stellen ..., in denen Teile von Streitkräften mehrerer Staaten zusammengeschlossen sind". Rows such as No. 41 and No. 42 ("Ministery of Defense", Lithuania and Netherlands), No. 6 (Canadian Forces College) and No. 81 (United States Air Force Academy) read as national bodies. The article does not raise this, and the encoding does not test it: it is a different possible defect (the scope of the power, not its citation), and for a domain expert.

## Answer table

| soldier | time off for 10 hours of ordered overtime, as printed | if the 2025 listing is void |
|---|---|---|
| at JSEC (No. 27), assigned for international tasks | 0 hours | 10 hours |
| at JSEC, not assigned for international tasks | 10 hours | 10 hours |
| at SHAPE (No. 76), assigned for international tasks | 0 hours | 0 hours |
| at an establishment not in the annex | 10 hours | 10 hours |
| in a § 30c(4) activity | 0 hours | 0 hours |

## Checks run

`./check.sh` in this folder, target `main`, on 2026-11-02 (the `l4` is a dev build, 25a091f4...; the main build compared with is 1.6.108 (main, 2ae7c9b, 2026-11-02)):

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.108 (main, 2ae7c9b, 2026-11-02)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
saz-cases-seat.l4                              0        12       0        0         0 |      0        12       0        0  same
saz-law.l4                                     0         0       0        0         0 |      0         0       0        0  same
saz-seat.l4                                    0         0       0        0         0 |      0         0       0        0  same
saz-tests.l4                                   0        43       0        0         0 |      0        43       0        0  same
TOTAL (4 modules)                              0        55       0        0           |      0        55       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

`python3 -I srcrefs.py check --refs ../../registers/source-bundle/sazv-1.txt saz-law.l4`: 16 src: lines, 8 runs, 16 locators, 0 problems.
No assertion is expected to fail. The check does not see a different trace outcome; the encoding has no regulative rule and no `#TRACE`.

## Before this is worth relying on

- Get BGBl. 2022 I S. 1533 (the previous annex) and compare it row by row with the 2025 annex; replace the article's statement in F2.
- Read OVG NRW 3 A 1217/14 and BVerwG 2 C 31.15 and 3 B 51.18 (the article's footnotes 19 to 21), and decide the input in F3 with someone who knows German administrative law.
- Check finding 5 against § 30c(6) and the annex, row by row.
- Have a domain expert read the encoding against the German text (the pipeline's HG1).
