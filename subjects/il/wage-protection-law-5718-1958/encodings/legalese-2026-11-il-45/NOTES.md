# Row il-45: Wage Protection Law, 5718-1958, a targeted record of cross-references

Status: draft, version 0.1.0, target compiler main.
No domain expert has read this against the source.
Every claim below was checked against the deposited text or a page image named beside it; where it was not, it says so.
This row does not encode the Law.

## 1. What this row is

The row records five items in the Law as typed values and tests them: a citation of a law that was repealed (P1), three citations of a category of prisoner's work that the Penal Law no longer has (P3), a citation of the 1968 Consolidated Version of the National Insurance Law (P4), an amending instruction that begins on 31 December 2026 and looks for words another instrument already replaced (P5), and a citation of a definition of the Income Tax Ordinance that was deleted in 2005 (P6).
P3 is three references (three places in the Law), P5 is three references (three places the instruction names), so the five items are nine references.
Beside each item the row keeps one sound reference from the same Law as a control (C1 to C6 below; C5 is a date pair).
The row also keeps a function that answers whether the words section 42 of Postal Law Amendment 11 looks for are still in the Law on a given day.
Each of the nine references says what the citing words say they point at, what the target is in the official text, and two limbs: limb (a), the target is repealed, missing or says something else; limb (b), the citing words still read so in the latest official instrument that touched them.
Section letters are written in Latin letters for the Hebrew letters the Law uses (26C is 26 gimel, 51D is 51 dalet, 19A is 19 alef, 88YA is 88 yod-alef; (a) is alef, (b) bet, (f) vav).

## 2. Seat

The seat is the individual to whom the Law is applied: an employee, or a former employee, whose wage is paid or owed.
The row asks that individual no question, because it records references; there is no input to ask for and no `@export`.

## 3. Source, and how each quotation was made

The working text is the Hebrew Wikisource consolidation of the Law, revision 2966245, last edited 2025-12-04T07:30:26Z, deposited at `../../registers/source-bundle/wage-protection-law-5718-1958.he.wiki.txt`.
Its sha256 is 7ad076309a2b4f0cdf84e8d1e9ae08921ebd082d5c6f3fe1186874ab2813eb09 (79,617 bytes).
It is unofficial, so every statement about the Law's present words is CONSOLIDATION-ONLY unless a page image of the Sefer HaChukim (SH) PDF is named beside it.

Seven other Hebrew Wikisource consolidations are deposited in `../../registers/source-bundle/other-laws/`, all UNOFFICIAL, so everything resting only on them is CONSOLIDATION-ONLY.
Their revision ids were not recorded when they were fetched.

| file | sha256 |
| --- | --- |
| `enforcement-of-labour-laws-law-5772-2011.he.wiki.txt` | 4aaabcdee1f289ce24569257e544d8f53f3ad923e390cdccd96511732a6bd9d4 |
| `interpretation-law-5741-1981.he.wiki.txt` | df3abac9015b4cd919eddece40d46565a97cdf123f78bbe925b687a5f5f0d2ab |
| `penal-law-5737-1977.he.wiki.txt` | 5b78cb985445d414f03ff9a5fb02b67c5fcbd8cb86a84d27cf2746e90210ceef |
| `severance-pay-law-5723-1963.he.wiki.txt` | 979ed62b50ffa43795d96d3a42a1bf8520e401cd2a43f979e5711d9e21b7e863 |
| `cash-reduction-law-5778-2018.he.wiki.txt` | 11e983e340179046c1f61e9c664268f6a7f053ba8a29cca0258fb2e46cb29570 |
| `postal-law-5746-1986.he.wiki.txt` | f22a732e2651cd1872c038364b62ab511c90bb14aef424ff5e7994d9bc9e69e1 |
| `national-insurance-law-consolidated-version-5755-1995.he.wiki.txt` | 78bf47ee29a300d51c5c7646cf85992d7de78aa1380bd8460a4a18265f552a97 |

The National Insurance file was fetched on 2026-10-06 for another subject of this repository and copied here byte for byte.
The Ordinance's consolidation is not deposited, so the Ordinance's present words are not quoted.

The official instruments are eleven Sefer HaChukim PDFs from the Knesset's site, deposited in `../../registers/source-bundle/amending-laws/` with the page images the encoder viewed in `amending-laws/pages/` (100 dpi): SH 1212 (9.4.1987), SH 2024 (10.8.2005), SH 2208 (10.8.2009), SH 2214 (11.11.2009), SH 2326 (19.12.2011), SH 2373 (31.7.2012), SH 2459 (15.7.2014), SH 2708 (15.3.2018), SH 2710 (18.3.2018), SH 2969 (16.3.2022), SH 3046 (6.6.2023).
`SOURCES.json` there gives the URL, retrieval date, sha256 and byte count of every file, recomputed with `shasum -a 256` on 2026-11-10.
The Hebrew in a quotation line is never typed from memory.
A `src:N` line is expanded by `tools/srcquote.py` from the Law's deposit.
An `ext:[tag] N` line is expanded by `tools/extquote.py` from another consolidation.
An `ext:[shNNNN] pP:L` line is expanded by the same tool from line L of the text layer of PDF page P of the instrument (not the printed page); the text layer of these PDFs is partly out of order, so only lines that read in order are quoted, and brackets and numerals in them can look reversed.
Where the text layer is out of order (SH 2208 printed page 315, SH 2326 printed page 75, SH 2708 printed page 409) the page is not quoted from the layer: the encoder viewed the image on 2026-11-10 and compared its words with the consolidation's lines (`src:254` for SH 2208, `ext:[enforcement] 368` for SH 2326, `src:129` for SH 2708), and they are the same words; the one difference is that SH 2208 prints the older word for employer where the consolidation prints the newer one.
`python3 -I tools/hebcheck.py <the Law's deposit> *.l4 NOTES.md` exits 0 (it finds every run of Hebrew outside the quotation lines in the deposit), and `python3 -I tools/extquote.py --check *.l4` exits 0.

## 4. Files

| file | what it holds |
| --- | --- |
| `wp45-nouns.l4` | the kinds of thing a citation can point at, the record of a cross-reference, the questions asked of it |
| `wp45-cross-references.l4` | the nine references of the five items, the six references of the controls, the date pair, and the day function; every one beside its quotation lines |
| `wp45-tests-controls.l4` | 17 assertions that pass: the six control references, the date pair, the day function |
| `wp45-tests-readings.l4` | 27 assertions that pass: for each of the nine references, both limbs hold and how each was read |
| `wp45-tests-red.l4` | 10 assertions that fail on purpose, declared in `check.sh` and `encoding.json` |

## 5. Coverage

| provision | status |
| --- | --- |
| s 26C(a) | encoded as the citing place of P1 |
| s 1, definition of the determining day; s 6(b); s 28(a)(3) | encoded as the three citing places of P3 |
| s 19A(f) | encoded as the citing place of P4 |
| s 6(a), s 8(f), item 8(3) of the Schedule | encoded as the three places named by the instruction of P5 |
| s 1, definition of a provident fund | encoded as the citing place of P6 and of C6 |
| s 2(b); s 19(a); s 25B(a) and (b); s 1, definition of the postal bank | encoded as the citing places of the controls C1, C4, C3 and C2 |
| the rest of s 1 (definitions) | out of scope: this row records citations, not the definitions; an encoding would need the seat's facts (who is the employer, what counts as wages) |
| ss 2 to 8 (payment in cash, in kind, restrictions, all-inclusive wage, method of payment, a deceased employee's wage, attachment) apart from the places above | out of scope: these are the Law's core rules on how wages may be paid, and an encoding of them would have to ask the seat who paid, how and to whom |
| ss 9 to 16C (pay days, increases, place and hours, pension payments) | out of scope: dates for each kind of pay need facts about the pay period and the calendar; no item touches them except through the determining day |
| ss 17 to 20 (compensation for late payment, insolvency, funds, severance) apart from the places above | out of scope: compensation needs rates by period and a second Law's index rules, none of which is deposited |
| ss 21 to 24 (including the wage book and the wage slip) | out of scope: not examined for this row; the Schedule's list of what a slip must show is likewise out, apart from item 8(3) |
| ss 25 to 26B (deductions, penalties, officers, jurisdiction, proof) apart from the places above | out of scope: the penalty levels are stated in the Law but their effect is for a prosecution, not for the seat |
| ss 27 to 29 | out of scope: not examined for this row, apart from s 28(a)(3) above |
| ss 30 to 36 (a new employer's guarantee, execution, consultation, the State as employer, savings, repeals, commencement) | out of scope: not examined for this row |

## 6. Answer tables

"Official" means read from the Sefer HaChukim page image or, for lines marked in section 3, from the quotable text layer; "CO" means CONSOLIDATION-ONLY.
Pages are printed pages, with the PDF page of the image in brackets.

| item | the citing words say | the target is | does the target exist | limb (a) | limb (b) | read |
| --- | --- | --- | --- | --- | --- | --- |
| P1, s 26C(a) | a monetary sanction under the Wage Protection (Monetary Sanction) Law, 2009 | repealed: s 58 of the Law to Increase the Enforcement of Labour Laws, 2011 | no | holds, official (SH 2326 p. 75 [15]) | holds; the enacted words official (SH 2208 p. 315 [6]), the present wording CO; SH 2459 p. 603 [5] does not restate s 26C | the Interpretation Law s 25 is the provision that could cure it (fork F1) |
| P3, s 1 (determining day); s 6(b); s 28(a)(3) | the Penal Law's subchapter B1 of chapter 6, on "עובד שירות בעבודת משק" | no farm-work category: the definitions of s 51A were replaced (SH 2214 p. 240 [1]) and s 51D repealed (SH 2214 p. 242 [3]) | the subchapter's category: no | holds, official; the present Penal Law text CO | holds; inserted by SH 1212 p. 83 [4], the present wording CO | the three places have the same words and the same status |
| P4, s 19A(f) | capitalising future payments in s 185 of the 1968 Consolidated Version | a version that the 1995 Consolidated Version replaced; its s 369 carries the old number 185 | the 1968 version: replaced | holds, CO | holds, CO: the instrument that wrote s 19A(f) was not read | SH 2708 p. 409 [113] moved s 19(a) to the 1995 version and touched no other subsection |
| P5, s 42(1), (2), (3) of Postal Law Amendment 11 | the words naming the postal company, in s 6(a), s 8(f) and item 8(3) | s 73(2), (3), (4) of the Economic Plan Law (SH 3046 p. 370 [192]) already put the postal bank and a list of bodies there | the words: no | holds, official; the present wording CO | holds, official: it begins on 21 Tevet 5787 (31 December 2026), SH 2969 p. 833 [19], s 59(7); that nothing later moved the day is CO | for item 8(3) that the replaced tail held the words is an inference (fork F5) |
| P6, s 1 (provident fund) | s 47 of the Income Tax Ordinance | paragraph (2) of s 47(a) deleted by item (9) of s 61 of the Provident Funds Law (SH 2024 p. 912 [24]); the definition is now in s 1 of that Law | the paragraph: no | holds, official | holds, CO: the present words of the definition are the consolidation's | the same instrument replaced the citation in other laws (its ss 62, 63, 64, 67, 68) and amended this Law only in s 26 (p. 913 [25]) |

| control | the citing words say | the target is | does the target exist | limb (a) | limb (b) |
| --- | --- | --- | --- | --- | --- |
| C1, s 2(b) to ss 2 and 4 of the Cash Law | the limits on paying in cash, and by cheque | the same | yes | does not hold, CO | holds; added by SH 2710 s 34 (pdf-page 12), the present wording CO |
| C2, s 1 (postal bank) to s 88YA of the Postal Law | the definition of the subsidiary company of the postal company | the same | yes | does not hold, CO | holds, CO |
| C3, s 25B(a) and (b) to s 61(a)(2) and (3) of the Penal Law | the fine levels by length of imprisonment | the same | yes | does not hold, CO | holds, CO |
| C4, s 19(a) to s 182 of the 1995 version | the entitlement to a benefit on an insolvency order against the employer | the same | yes | does not hold, CO | holds; SH 2708 p. 409 [113], the present wording CO |
| C6, s 1 (provident fund) to s 14 of the Severance Pay Law | payments to a fund that stand in place of severance pay when the Minister of Labour so provides | the same | yes | does not hold, CO | holds, CO |
| C5, the operative day of Amendment 11 | 21 Tevet 5787 | 31 December 2026 | the pair agrees | not a citation | not a citation |

C5 uses a Hebrew-calendar routine kept outside this repository: it gave 21 Tevet 5787 = 31 December 2026 on 2026-11-10, and its control date, 30 Kislev 5785, gave 31 December 2024.
The same pair is printed in the Postal Law consolidation (`ext:[postal] 14`, CO) and in SH 2969 (`ext:[sh2969] p19:23-24`).

## 7. The day function

`the words naming the postal company are still in the Law on` answers a day with a MAYBE BOOLEAN.
A day before 4 December 2025 answers NOTHING, because the sources do not say when section 73 of the Economic Plan Law began to apply.
A day from 4 December 2025 answers JUST FALSE, because the Law's consolidation of that day (revision 2966245) already prints the replaced words; this is CONSOLIDATION-ONLY.
No day answers JUST TRUE, so the instruction cannot be carried out on 31 December 2026 on this reading.

## 8. Fork register

- F1, whether a court would read through these citations.
  Taken: each citation is recorded as written, and the row does not apply the Interpretation Law s 25 to cure it.
  Rejected: treating P1, P3, P4 and P6 as sound because s 25 reads a reference to a law as including "the provisions that came in its place in another law" (`ext:[interp] 139` in the references module, CO).
  P5 is not a citation, so s 25 does not bear on it.
- F2, what the "target" of P3 is.
  Taken: the category of work that subchapter B1 once defined, which the official instruments no longer have (SH 2214 replaced the definitions and repealed s 51D); the present Penal Law text is CO (`ext:[penal] 677` and `722`).
  Rejected: reading the target as the subchapter as a whole, which still exists.
  The effect on a worker is not typed.
- F3, the correspondence of s 185 of the 1968 version and s 369 of the 1995 version.
  Taken: the 1995 consolidation prints the old number 185 beside s 369 and says it replaces the 1968 version (`ext:[ni1995] 4014` and `16`, CO), and s 369(b) is the provision on capitalisation (`ext:[ni1995] 4018`, CO).
  Rejected: reading s 369 as the only successor; its heading is about non-registration and non-payment of insurance contributions, and only its subsection (b) concerns capitalisation.
- F4, the cut-off of the day function.
  Taken: 4 December 2025, the date of the consolidation that already prints the replaced words.
  Rejected: the day section 73 of the Economic Plan Law began to apply, which was not read.
- F5, the third place of P5.
  Section 42(3) of Amendment 11 replaces the postal-company words in item 8(3) of the Schedule; section 73(4) of the Economic Plan Law replaces a tail of that item beginning at the words about payment through a bank account.
  Taken: the 2012 words were in that tail, which is an inference from the shape of the two instructions, because the text of item 8(3) before 2023 was not deposited.
  Rejected: leaving item 8(3) out; it is kept, with the inference stated on its line.
- F6, counting.
  P3 is counted as three references and P5 as three, because the Law has three places for each; the count of ten red assertions follows (section 9).
- F7, limb (b).
  Taken: "the latest official instrument that touched the words", where the sources show one, and CONSOLIDATION-ONLY where only the consolidation shows the present words.
  Rejected: calling limb (b) official because the enacting instrument is official: for P1, P3 and P5 the enacted words are official and the present wording is not.
- F8, the short name "Economic Plan Law" for SH 3046 is this row's, not the instrument's title, which is on its first page and was not copied.

## 9. Expected red

Ten assertions in `wp45-tests-red.l4` fail on purpose, and `check.sh` and `encoding.json` declare ten.
Nine say that a citation points at what its words say it points at: P1 (1), P3 (3), P4 (1), P5 (3), P6 (1).
The tenth says that the words section 42 of Postal Law Amendment 11 looks for are in the Law on 31 December 2026.
If a defect is cured, its assertion turns green and the declared count must go down with it.

## 10. Check numbers

Run as `L4=~/.local/bin/l4 L4_MAIN=~/.cache/l4-main/109/l4 ./check.sh`; main is build 1.6.109 (4c887e0, 2026-11-04).
Both binaries give the same four counts for every file.

| file | errors | satisfied | failed | refused | declared failed |
| --- | --- | --- | --- | --- | --- |
| `wp45-nouns.l4` | 0 | 0 | 0 | 0 | 0 |
| `wp45-cross-references.l4` | 0 | 0 | 0 | 0 | 0 |
| `wp45-tests-controls.l4` | 0 | 17 | 0 | 0 | 0 |
| `wp45-tests-readings.l4` | 0 | 27 | 0 | 0 | 0 |
| `wp45-tests-red.l4` | 10 | 0 | 10 | 0 | 10 |

The ten errors are the ten declared failed assertions.
The check does not see a different trace outcome, or any difference no assertion exercises.
Mutation control: four deliberate faults in a scratch copy (a control's target changed, P1's limb (a) flipped, P6's limb (b) reading changed, the day function's cut-off moved by one day) turned two assertions red in the controls module and two in the readings module, so those tests can fail (run on the first version of the controls module, before C2 was added).

## 11. What was not done, and open questions

- The instrument that wrote s 19A(f) was not read, so limb (b) of P4 is CONSOLIDATION-ONLY.
- The pre-2023 text of item 8(3), and the day section 73 of the Economic Plan Law began to apply, were not read.
- That no instrument after SH 2969 moved the day of Amendment 11 again rests on the Postal Law consolidation.
- The heading of s 61 of the Provident Funds Law was read from the text layer of PDF page 22 and not viewed as an image.
- The Ordinance's present text is not deposited, and the instrument that wrote the present words of the provident-fund definition in s 1 of the Law was not read; that is why limb (b) of P6 is CONSOLIDATION-ONLY while limb (b) of P1 is official for the enacted words.
- The Postal Law consolidation marks the definition of the subsidiary company in s 88YA(a) as to be deleted on the operative day (`ext:[postal] 813`, CO); C2 records only what the citation reaches today, and what it reaches after that day was not examined.
- The three page images whose text layer is out of order (SH 2208, SH 2326, SH 2708) were compared with the consolidation by eye, not by a tool.
- The deposits' revision ids, other than the Law's, were not recorded.
- Open for a domain expert: would a court read P1, P3, P4 and P6 through s 25 of the Interpretation Law; does any of the three P3 places have a live application; what section 185 of the 1968 version said and which section of the 1995 version now answers it; whether a later instrument removes section 42 of Amendment 11 before 31 December 2026.
