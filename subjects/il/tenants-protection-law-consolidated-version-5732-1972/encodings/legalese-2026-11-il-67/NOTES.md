# Row il-67: Tenants' Protection Law [Consolidated Version], 5732-1972, a targeted record of four cross-references

Status on 2026-11-10: draft, version 0.1.0, target compiler main.
No domain expert has read this against the source.
Every claim below was checked against a deposited page image or the deposited excerpt named beside it; where it was not, it says so.
This row does not encode the Law.

## 1. What this row is

The row records four items of the Law as typed values and tests them.
Items I1, I2 and I3 are citations whose numbers include section 46, which an instruction of a 1980 amending law (SH 978 item 2) ends with the word for repealed.
Item I1 is section 50(a), which cites sections 46 and 49 for the maximum and the minimum.
Item I2 is section 51(b)(1), which cites sections 45 and 46.
Item I3 is section 48, which cites a range of sections, 42 to 46, whose last number is section 46.
Item I4 is section 57(1), which cites subsection (c) of section 52, and a 1982 amending law deletes subsections (c), (d) and (e) of section 52.
Beside each item the row keeps what the same citation also reaches that is still in force: section 49 for I1, section 45 for I2 and I3, and for I4 the citation in section 53, which the same 1982 amending law updates.
Each item has two limbs: limb (a), the target is repealed, missing or says something else, read from an official instrument; limb (b), the citing words still read so in the latest official instrument read.
Section letters are written in Latin letters for the Hebrew letters the Law uses (52A is 52 alef; subsection (a) is alef, (b) bet, (c) gimel, (d) dalet, (e) he).

## 2. Seat

The seat is the individual to whom the Law applies, a tenant or a landlord.
The row asks that individual no question, because it records references: there is no input to ask for and no `@export`.

## 3. Source, and how each quotation was made

The working text is the Hebrew Wikisource consolidation of the Law, revision 2970726, last edited 2025-12-28T09:30:14Z.
Only an excerpt of it is deposited, `../../registers/source-bundle/tenants-protection-law-5732-1972.he.wiki.excerpt.txt`: 23 whole lines of the page, with a header that gives the revision id, its timestamp, the whole page's size and sha256, and the line numbers copied.
The whole page is 138880 bytes and its sha256 is 0378f03e4aa2ea8530e068fb2dc1aaff62599bb1593ce5ca88151e64f2d20abf; the sha256 of the excerpt is in `SOURCES.json` there.
The consolidation is unofficial, so every statement about the Law's present words that rests only on it is labelled CONSOLIDATION-ONLY.

The official instruments are three issues of Sefer HaChukim (SH) from the Knesset's site.
Only the lines the row reads are deposited, as four cropped images in `../../registers/source-bundle/pages/`; no full page is deposited, and the whole files are not in the bundle.
`SOURCES.json` there gives the URL, retrieval time, sha256 and size of each whole file (recomputed with `shasum -a 256` and `stat -f %z` on 2026-11-10) and of each deposit.

| deposit | instrument | printed page (PDF page of the whole file) | what is on it |
| --- | --- | --- | --- |
| `sh668-p184-ss48-52.png` | SH 668, 13.8.1972, the Law as made | 184 (9) | one band from the first line of section 48 to the last line of section 51(b)(4); one band with the first lines of section 52 on the page (subsection (a) and the first two lines of subsection (b)); the footer line |
| `sh668-p185-ss52-53-57.png` | SH 668, 13.8.1972 | 185 (10) | subsections (c), (d) and (e) of section 52; section 53 whole; section 57 to the end of paragraph (1); the footer line |
| `sh978-p165-items1-2.png` | SH 978, 31.7.1980, the 1980 amending law | 165 (1) | the title; item 1 (section 45); item 2 (section 46); the footer line |
| `sh1070-p21-items1-3.png` | SH 1070, 31.12.1982, the 1982 amending law (Amendment No. 2) | 21 (1) | the title; item 1 whole; item 2 as far as its instruction, the number and margin heading of the new section 52A and its first two lines; item 3; the footer line |

For SH 668 the printed page is the PDF page plus 175, and for SH 1070 it is the PDF page plus 20; both were checked by rendering the pages before cropping (printed page 184 is PDF page 9, printed page 185 is PDF page 10, and the footer of each crop prints the printed number).
Every crop was viewed with the Read tool after it was composed, and what each band holds is in the table above.

Quotation lines in the modules are of three kinds.
A `src:N` line is expanded by `tools/srcquote.py` from the excerpt, and N is the line number in the whole page, which the excerpt's header lists; `python3 -I tools/srcquote.py --check <excerpt> *.l4` exits 0.
An `ext:[shNNN-pPPP]` line quotes the Hebrew read from the deposited image of issue NNN, printed page PPP.
No consolidation other than the Law's is quoted, so `tools/extquote.py` of row il-45 is not used here.
`python3 -I tools/hebcheck.py <excerpt> *.l4 NOTES.md` exits 0: every run of Hebrew outside a quotation line is in the excerpt, and the little Hebrew this file carries (in forks F2 and F9) is limited to words that occur there.

The text layers of these old printed pages are partly wrong (letters misread, digits and brackets out of order), so the Hebrew of every `ext:` line was read from the image.
Compared with the text layer, with the same digits and letters: the numbers of section 50(a) (46 and 49), of section 51(b)(1) (45 and 46) and of section 57(1) (52 and the letter of subsection (c)); the words of section 53 as made, which were copied from a line of the text layer and checked against the crop; the number in the instruction of SH 978 item 2 (46); the letters of SH 1070 item 1(2); and the words of SH 1070 item 3 (the layer carries them in reversed word order).
**Not the same:** in section 48 the text layer of printed page 184 prints the second number of the range as 48, while the image reads 46 and so does the consolidation (`src:256`); the image decides (fork F1).
The lines of section 52 on printed page 184 were read from the image and agree, word for word as far as the crop goes, with the consolidation's `src:282` and `src:283`; the text layer misreads one word of subsection (a), and subsection (b) was not compared with it.
Not compared with any text layer (read from the image only): the titles and the item 1 lines of SH 978 and SH 1070 and the heading words of their instructions, and every footer, because a footer is in no text layer.

## 4. Files

| file | what it holds |
| --- | --- |
| `tn67-nouns.l4` | the status of a section as the instruments read give it, the record of a citation (of sections, of a range, of a subsection), and the questions asked of them |
| `tn67-cross-references.l4` | the nine sections the citing words name with their statuses, the four items, and the control beside I4, each beside its quotation lines |
| `tn67-tests-controls.l4` | 10 assertions that pass: the sections kept as controls, and the day-of-effect answer (NOTHING) |
| `tn67-tests-readings.l4` | 40 assertions that pass: the numbers each citation names, the status of each section, both limbs and how each was read, the subsections of section 52, the flags |
| `tn67-tests-red.l4` | 4 assertions that fail on purpose, one per item, declared in `check.sh` and `encoding.json` |

## 5. Coverage

| provision | status |
| --- | --- |
| section 50(a), the sentence citing sections 46 and 49 | encoded as item I1 |
| section 51(b)(1), the paragraph citing sections 45 and 46 | encoded as item I2 |
| section 48, the words citing sections 42 to 46 | encoded as item I3 |
| section 57(1), the paragraph citing section 52(c) | encoded as item I4 |
| sections 45, 46, 49, 52 and 52A, as targets and controls | read for their status only, as the instruments read give it: 46 repealed; 45, 49, 52 and 52A present; for 52, the subsections as made and after the 1982 amending law |
| section 53, the control beside I4 | read for the numbers it cites as made and as updated by the 1982 amending law |
| sections 42, 43, 44 and 61, named by a citing sentence | not read: typed `NotChecked`, because the row reads sections 45 and 46 only for I3 and nothing deposited reads section 61 |
| the other sentences and subsections of sections 48, 50, 51 and 57 | out of scope: the row records one citing sentence in each; the others state rules whose application would need facts the seat would have to give (which premises, which tenancy, what was agreed or ordered), and this row asks no question |
| the rest of the Law, and anything made under it | out of scope: this row records four references and does not encode the Law; no other section was read as a rule for this row beyond what locating the four items required, and an encoding of the Law would need its own coverage table, a seat layer with questions, and tests written from the whole text |

## 6. Answer tables

"Official" means read from a deposited page image of Sefer HaChukim; "CO" means CONSOLIDATION-ONLY.
Pages are printed pages.

| item | the citing words say | the target says | does the target exist | limb (a) | limb (b) | page read |
| --- | --- | --- | --- | --- | --- | --- |
| I1, section 50(a) | sections 46 and 49 for the maximum and minimum | 46: SH 978 item 2 repeals section 46 of the principal Law; the consolidation prints the section's body as the word for repealed (CO). 49: printed on SH 668 page 184, no instrument read touches it | 46: no; 49: yes | holds, official (SH 978 p. 165) | holds: the citing words are on SH 668 p. 184 as made; later instruments, section 7 | SH 668 p. 184; SH 978 p. 165 |
| I2, section 51(b)(1) | sections 45 and 46 | 46 as in I1; 45: SH 978 item 1 replaces its subsections (a) and (c), and no instrument read repeals it | 46: no; 45: yes | holds, official | holds, as I1 | SH 668 p. 184; SH 978 p. 165 |
| I3, section 48 | the range 42 to 46 (the numbers 42, 43, 44, 45, 46) | 46 as in I1; 45 as in I2; 42, 43 and 44 not checked | 46: no; 45: yes; 42 to 44: not checked | holds, official | holds, as I1 | SH 668 p. 184; SH 978 p. 165 |
| I4, section 57(1) | section 52, subsection (c) | SH 1070 item 1(2) deletes subsections (c), (d) and (e) of section 52; after it the subsections are (a) and (b); the consolidation prints (a) and (b) only (CO) | subsection (c): no | holds, official (SH 1070 p. 21) | holds: the citing words are on SH 668 p. 185 as made; no instrument read touches them | SH 668 p. 185; SH 1070 p. 21 |

| control | what it cites or reaches | status | read |
| --- | --- | --- | --- |
| I1: section 49 | printed on SH 668 p. 184, subsections (a) and (b) | present, untouched | SH 668 p. 184 |
| I2 and I3: section 45 | SH 978 item 1 replaces subsections (a) and (c) | present | SH 978 p. 165 |
| I4: section 53 | as made it cites sections 52 and 61 (SH 668 p. 185); item 3 of SH 1070 puts 52A after 52 (p. 21); the consolidation prints 52, 52A and 61 (CO) | 52 present (item 1 of SH 1070 amends it; (a) and (b) remain); 52A present (added by item 2); 61 not checked | SH 668 p. 185; SH 1070 p. 21 |

The row records the publication date of the instrument that repeals section 46 as its issue's footer prints it, 31.7.1980, and nothing about the day the repeal took effect: `the day the repeal of the section took effect` answers NOTHING.
The flag "a later instrument read touches the citing words" is true for the citing words of section 53 (item 3 of SH 1070) and false for sections 48, 50(a), 51(b)(1) and 57(1).

## 7. Limb (b): the later instruments

The citing words of each item are on SH 668 as made, and the two later instruments deposited here were read as to the items on the deposited pages: the three items of SH 978 name sections 45, 46 and 47, and the items of SH 1070 on printed page 21 name sections 52, 52A, 53, 55, 61 and 148.
Examined from the page image for this row and not deposited, as the examination that preceded this row states (the encoder of this row did not view these pages, and no claim about them is made here beyond that statement): SH 1070 (1982) items 1 to 8, which touch sections 52, 53, 55, 61 and 148, add section 52A, and give a transitional rule and a commencement day; SH 1704 (15.2.1999) page 98 item 15, which touches section 52A(b); SH 3016 (9.2.2023) page 21 item 49, which touches section 68(a); and a correction notice, SH 673 (22.12.1972) page 19, which touches section 140(a).
That examination states that none of them names section 50, section 51, section 48 or section 57.
An amendment made inside another law between 9 February 2023 and 28 December 2025 is NOT ESTABLISHED either way: the open data lists none, and the check was by name, not by every law.
So limb (b) of each item is "holds, on the instruments read", and `how limb (b) was read` says so (`official page image, with later instruments examined by name`).

## 8. Fork register

- F1, the last number of the range in section 48.
  Taken: 46, as the image of SH 668 printed page 184 reads and as the consolidation prints (`src:256`).
  Rejected: 48, which is what the text layer of that page prints; the layer misreads other words of the same line.
- F2, whether the range names its end numbers.
  Taken: the range names its first and its last number and the whole numbers between them, so 42, 43, 44, 45 and 46; the consolidation's link text for the same words is `סעיפים 42 עד 46`.
  Rejected: reading it as stopping before 46, which would not name the repealed section; the row types the range both as two integers and as the set and tests that they agree.
- F3, what the letter in "section 52(c)" is.
  Taken: subsection (c) of section 52, a subsection of the section; SH 1070 item 1(2) speaks of subsections, and the subsections of section 52 as made are (a) and (b) on printed page 184 and (c), (d) and (e) on printed page 185.
  Rejected: reading the letter as a paragraph or an item.
  Subsections (a) and (b) of section 52 as made are on printed page 184, where the deposited band holds subsection (a) and the first two lines of subsection (b), which goes on over the page; the deposited band of printed page 185 holds (c), (d) and (e).
- F4, what "in force in the current official text" means.
  Taken: as the instruments read give it, with sections repealed or deleted by a deposited instrument marked so, and the row says nothing of the day the repeal took effect.
  Rejected: reading the printed date of the issue (31.7.1980) as the day of effect.
- F5, a section named by the citing words that the row did not read (42, 43, 44, 61).
  Taken: a status value `NotChecked`, which a test can see and which is not "present" and not "repealed".
  Rejected: typing them `Present`, which would claim a reading the row did not make; and answering NOTHING, which would hide the difference between not read and not known.
- F6, the shape of the controls.
  Taken: for I1 to I3 the control is the other section named by the same citation, tested as a section; for I4 it is the sibling citation in section 53.
  Rejected: separate control citations as in row il-45, because the same citation already names the sound target.
- F7, the form of the four failing assertions.
  Taken: one per item, about the whole citation (I1, I2: every section named is in force; I3: no section named by the range is repealed; I4: the cited subsection is among those in force after item 1(2)).
  Rejected: one failing assertion per cited section, which would add passing ones and move the declared count.
- F8, I3's range under the "no section repealed" assertion.
  The sections 42 to 44 are `NotChecked`, not repealed, so that assertion fails only because of section 46.
- F9, the dash and a space.
  The page prints a long dash in the instruction of SH 978 item 2 and in SH 1070 item 1(2), and a space between 52 and the bracket in section 57(1); the `ext:` lines write the dash as the en dash the consolidation uses and write 52(ג) without the space, which are typographic differences only.
- F10, the issue number of the 1980 amending law.
  The footer of printed page 165 prints 978, read at 800 dpi; the file had been described to the encoder as SH 976, which is not what the page prints.
  Taken: 978.

## 9. Expected red

Four assertions in `tn67-tests-red.l4` fail on purpose, and `check.sh` and `encoding.json` declare four.
I1: every section section 50(a) cites is in force; false, because section 46 is repealed.
I2: every section section 51(b)(1) cites is in force; false, for the same reason.
I3: no section named by the range in section 48 is repealed; false, because the range ends at section 46.
I4: the subsection section 57(1) cites is among the subsections of section 52 in force after item 1(2) of SH 1070; false, because subsection (c) is not among them.
If a later instrument changes one of these, its assertion turns green and the declared count must go down with it.

## 10. Check numbers

Run as `L4=~/.local/bin/l4 L4_MAIN=~/.cache/l4-main/109/l4 ./check.sh`; main is build 1.6.109 (4c887e0, 2026-11-04).
Both binaries give the same four counts for every file.

| file | errors | satisfied | failed | refused | declared failed |
| --- | --- | --- | --- | --- | --- |
| `tn67-nouns.l4` | 0 | 0 | 0 | 0 | 0 |
| `tn67-cross-references.l4` | 0 | 0 | 0 | 0 | 0 |
| `tn67-tests-controls.l4` | 0 | 10 | 0 | 0 | 0 |
| `tn67-tests-readings.l4` | 0 | 40 | 0 | 0 | 0 |
| `tn67-tests-red.l4` | 4 | 0 | 4 | 0 | 4 |

The four errors are the four declared failed assertions.
The check does not see a different trace outcome, or any difference no assertion exercises; there are no traces here.
Mutation control: three deliberate faults in a scratch copy (section 46 given the status Present, section 49 given the status Repealed, subsection (c) added to the subsections of section 52 after the amending law) turned one assertion red in the controls module, three in the readings module, and made three of the four red assertions pass; so these tests can fail and the red ones can turn.

## 11. What was not done, and open questions

- The pages SH 1070 page 22, SH 1704 page 98, SH 3016 page 21 and SH 673 page 19 were not viewed by the encoder of this row and are not deposited; section 7 rests on the statement of the examination that preceded the row.
- Sections 42, 43, 44 and 61 were not read, and the status of each is `NotChecked`.
- The words of section 52(c) after its first line were not typed: the crop holds them.
- The day the repeal of section 46 took effect is not read; neither is the day the deletions of 1982 took effect.
- An amendment inside another law between 9 February 2023 and 28 December 2025 is NOT ESTABLISHED either way.
- Open for a domain expert: whether any of the four citations is applied in practice as written, and how; this row does not say.
