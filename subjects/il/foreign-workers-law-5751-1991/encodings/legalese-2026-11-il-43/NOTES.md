# Row il-43: four citations in s 1יג(ד)(2) and s 2(א1)(1) of the Foreign Workers Law, 5751-1991 (one defect, three controls)

Status: draft, version 0.1.0, target compiler main.
No domain expert has read this against the source.
Every claim below was checked against a text in the source bundle or a page image named beside it; where it was not, it says so.

## 1. Scope

This row is not an encoding of the Foreign Workers Law, 5751-1991.
It records four citations as typed values that tests check, and keeps the one that does not hold as expected-red tests.
For each citation the row types two descriptions, what the citing words say they point at and what the target is, and records where each of the two readings comes from.
The seat is the employer to whom s 1יג applies; for s 1יג(ד) that is an individual who has reached the retirement age and applies for a permit to employ a foreign worker in the nursing sector other than in the course of their business (s 1יג(ד)(1)).
This row asks no question from that seat, because it records references and not duties, so no `@export` module is written.
No domain expert has read this against the source.

## 2. Sources

The Foreign Workers Law is read from the Hebrew Wikisource consolidation, revision 2990506, last edited 2026-02-17T10:00:15Z (sha256 0c6230271ec70026c2ad40f1b9b99acd7a3b3036163a554a9316270801e76124), at `../../registers/source-bundle/foreign-workers-law-5751-1991.he.wiki.txt`.
The National Insurance Law is read from the Hebrew Wikisource consolidation, revision 3085079, last edited 2026-09-27T13:00:41Z (sha256 78bf47ee29a300d51c5c7646cf85992d7de78aa1380bd8460a4a18265f552a97), at `../../registers/source-bundle/national-insurance-law-consolidated-version-5755-1995.he.wiki.txt`.
Both are unofficial aids; the revision of each was identified on 2026-11-10 by matching the file's content hash to the page history.
Every statement that rests only on one of them says CONSOLIDATION-ONLY.

The official instruments are in `../../registers/source-bundle/amending-laws/`, each with a page image of the page read from it; `../../registers/source-bundle/SOURCES.json` gives the URL, retrieval date, sha256 and size of every file, and the sha256 values were recomputed with `shasum -a 256` on 2026-11-10.

| instrument | pages read from the page image | what the page shows |
| --- | --- | --- |
| Sefer HaChukim 2407, 30 Av 5773 (6 August 2013), National Insurance Law Amendment 147 | p. 227 | s 3 adds s 1יג(ד) to the Foreign Workers Law; paragraph (2) is the sentence that cites ss 1, 223 and 223א |
| Sefer HaChukim 2459, 17 Tammuz 5774 (15 July 2014), the Law Replacing the Term "employer" | p. 604 (p. 600 from the text layer) | item 24 lists the Foreign Workers Law; s 1 replaces word forms, none of which occurs in the paragraph |
| Sefer HaChukim 2504, 2 Cheshvan 5776 (15 October 2015), National Insurance Law Amendment 162 | p. 2 | s 6 amends s 1יג(ד): paragraph (1) (one word) and paragraph (3) (deleted); paragraph (2) is not touched |
| Sefer HaChukim 2713, 6 Nisan 5778 (22 March 2018), the Economic Efficiency Law for the 2019 budget year | pp. 524 and 527 (the cover, p. 510, for the issue number) | s 23(2) deletes the three definitions in s 223א of the National Insurance Law; s 25(b) commences the Subsection on 23 Cheshvan 5779 (1 November 2018) |

The Hebrew of an official page is typed by the encoder from the page image on a line `-- ext:[SH <issue> p.<page>, ...] | ...` in `il43-cross-references.l4`.
`tools/pdfcheck.py` checks every Hebrew word of such a line against the text layer of that page (6 lines, 0 problems); it cannot see the order of the words, because these text layers reverse and interleave runs, so the page image is what the typing was read from.
The Hebrew of the two consolidations is expanded mechanically by `tools/srcquote.py` (`src:` lines, the Foreign Workers Law) and `tools/extquote.py` (`ext:[nii]` lines).
`tools/hebcheck-all.sh *.l4 NOTES.md` finds every other run of Hebrew in the `.l4` files and in this file in the two consolidations, and exits 0.

One thing is unresolved.
The issue number of the 2018 instrument is 2713 on its cover page image and in its cover text layer.
The small footer line of pp. 524 and 527 prints an issue number that I read as 2013, which cannot be right for 22 March 2018; I take the cover and the printed date, and I did not resolve the footer.

## 3. Files

| file | what it holds |
| --- | --- |
| `il43-nouns.l4` | the kinds of provision, the two sources of a reading, and the record of a citation; no rule |
| `il43-cross-references.l4` | the three functions, and one typed value per citation with the Law's words and the target's words quoted beside it |
| `il43-tests-xrefs.l4` | 18 assertions: the controls point at what they say, what was read from where, the day the defect's target was deleted |
| `il43-tests-xrefs-red.l4` | 2 assertions that fail, on purpose (section 7) |
| `check.sh`, `fetch-main-l4.sh` | the check; `check.sh` declares 2 expected failures for the file above |
| `tools/` | `srcquote.py`, `extquote.py`, `hebcheck.py`, `hebcheck-all.sh`, `pdfcheck.py` |

## 4. Coverage

| provision | status |
| --- | --- |
| s 1יג(ד)(2) to s 223א of the National Insurance Law, the term "היתר שהותלה" | encoded; a defect; both limbs read from official instruments |
| s 1יג(ד)(2) to s 1 of the National Insurance Law, the term "גיל הפרישה" | encoded; a sound control; limb (b) official, limb (a) CONSOLIDATION-ONLY |
| s 1יג(ד)(2) to s 223 of the National Insurance Law, the term "גמלת סיעוד" | encoded; a sound control; limb (b) official, limb (a) CONSOLIDATION-ONLY |
| s 2(א1)(1) to s 398(א2)(5) of the National Insurance Law | encoded; a sound control; both limbs CONSOLIDATION-ONLY |
| s 1יג(ד)(1), the choice an individual makes when applying | out-of-scope: it states what the individual chooses on a form, not a reference, and this row records references; the seat is named for that paragraph but no question is asked |
| every other provision of the Law, and every other citation in it | out-of-scope: this row does not encode the Law; it records the four citations that were examined and the three amending instructions that bear on the one that fails, and says nothing of the rest of the text |
| the rest of National Insurance Law Amendments 147, 162 and 203 | out-of-scope: only the instructions that bear on the four citations were read |

## 5. The four citations: answer table

"Stands" means that the target is in the official text of its law today.
Limb (a) asks whether the target is what the citing words say; limb (b) asks whether the citing words still read so in the latest official text of the citing provision.

| citation | the citing words say it points at | the target is | stands today | limb (a) | limb (b) |
| --- | --- | --- | --- | --- | --- |
| s 1יג(ד)(2) to s 223א, "היתר שהותלה" | the definition of a suspended permit | a definition that was deleted; the section prints "(נמחקה)" in its place | no, from 1 November 2018 | official: SH 2713 p. 524, s 23(2), and p. 527, s 25(b) | official: SH 2407 p. 227 wrote the words, SH 2504 p. 2 was the last instrument to touch s 1יג(ד) and left paragraph (2) alone |
| s 1יג(ד)(2) to s 1, "גיל הפרישה" | the definition of the retirement age | the definition of the retirement age (consolidation lines 130 to 132) | yes, by the consolidation | CONSOLIDATION-ONLY | official, same page as above |
| s 1יג(ד)(2) to s 223, "גמלת סיעוד" | the definition of the nursing benefit | the definition of the nursing benefit (consolidation line 2168) | yes, by the consolidation | CONSOLIDATION-ONLY | official, same page as above |
| s 2(א1)(1) to s 398(א2)(5) | a person with a medical disability fixed under items 33, 34 or 91, or found to need constant supervision | the same (consolidation line 4295) | yes, by the consolidation | CONSOLIDATION-ONLY | CONSOLIDATION-ONLY |

What limb (b) of the defect rests on, sorted by how strong it is.
Read from the page images: that SH 2407 p. 227 wrote the sentence, and that SH 2504 p. 2 changed paragraphs (1) and (3) of s 1יג(ד) and not paragraph (2).
Read from the page image together with the text layer of p. 600: that SH 2459 replaced word forms for "employer" in the Law, and that none of those word forms occurs in paragraph (2).
CONSOLIDATION-ONLY: that no instrument after SH 2504 touched s 1יג(ד)(2); the consolidation's list of amending instruments for s 1יג ends with the Act of 5776.
Six pages of the latest amending instruments of the Law since March 2018 were looked at in their text layers and none touches s 1יג; they are not in the source bundle, and the other instruments since March 2018 were not read.
Instruments between October 2015 and March 2018 were not read either; the consolidation lists none for s 1יג.

## 6. Fork register

Each fork gives the reading taken, the reading rejected, and the Hebrew that licenses it.

- K1, the kinds.
  The kinds in `What a provision is about` are my plain descriptions, so that two descriptions of the same thing are the same kind; they are not the Law's terms.
  Taken: one kind per target as its heading or first words describe it.
  Rejected: comparing the Law's words as strings, which would make every citation fail on punctuation.
- P1, the pairing in s 1יג(ד)(2).
  The sentence names three terms and three sections, "בהתאמה" (consolidation line 302).
  Taken: the terms and sections pair in order, so "גיל הפרישה" goes with s 1, "גמלת סיעוד" with s 223 and "היתר שהותלה" with s 223א.
  Rejected: each term defined in each section, which "בהתאמה" excludes.
- D1, a day before the deletion.
  No source in the bundle says when the definition was added to s 223א.
  Taken: for 31 October 2018 and any earlier day the answer is NOTHING; for 1 November 2018 and every later day it is JUST FALSE.
  Rejected: JUST TRUE for 31 October 2018, which the instruction's own words "shall be deleted" presuppose but which this row does not type, because the page that added the definition was not read.
  A control has no recorded deletion, so its answer is NOTHING on every day; that is not a statement that its target stands.
- D2, the commencement of s 23(2).
  SH 2713 p. 527, s 25(b), commences "this Subsection" on 23 Cheshvan 5779 (1 November 2018); the heading of Subsection C stands on p. 524 above s 23 and s 25 carries the marginal note of Subsection C.
  The exceptions in the same paragraph name s 225ג and the repeal of s 7(b) of Amendment 162, which are other provisions, so s 223א is not excepted.
  Taken: 1 November 2018.
  Rejected: 1 January 2019, which is the date of the exceptions.
- D3, the Hebrew dates.
  The calendar routine reproduced 30 Kislev 5785 = 31 December 2024 before it was used.
  Then: 23 Cheshvan 5779 = 1 November 2018 and 24 Tevet 5779 = 1 January 2019 (SH 2713 p. 527); 6 Nisan 5778 = 22 March 2018 (SH 2713); 30 Av 5773 = 6 August 2013 (SH 2407); 17 Tammuz 5774 = 15 July 2014 (SH 2459); 2 Cheshvan 5776 = 15 October 2015 (SH 2504).
  Every pair matches the Gregorian date printed beside it.
- E1, what follows from the defect.
  The term "היתר שהותלה" is also used in s 1יג(ד)(1) (consolidation line 301), and s 7(ג) of Amendment 162 used it in 2015.
  This row does not say what follows from paragraph (2) pointing at a deleted definition, and no test depends on an answer.
- A1, "אדם כאמור" in s 2(א1)(1).
  Taken: a person of the kind that s 398(א2)(5) of the National Insurance Law describes, which is the person to whom the subsection does not apply.
  Rejected: a reference to the subsection as a whole.

## 7. Expected red

Two assertions in `il43-tests-xrefs-red.l4` fail on purpose, and the count (2) is declared in `check.sh` and in `encoding.json`.
Both state what the citing words need and both are about the one defect.

- `the citation points at what it says` for s 1יג(ד)(2) to s 223א: the citing words say it points at the definition of a suspended permit; the target is a definition that was deleted.
- `the target stands in the official text on` 10 November 2026, expected JUST TRUE: the answer is JUST FALSE, because the deletion commenced on 1 November 2018.

Nothing in either file was edited to make it pass.

## 8. Check numbers

Run as `L4=~/.local/bin/l4 L4_MAIN=~/.cache/l4-main/109/l4 ./check.sh`; main is build 1.6.109 (4c887e0, 2026-11-04).
Both binaries give the same four counts for every file.

| file | errors | satisfied | failed | refused | expected failed |
| --- | --- | --- | --- | --- | --- |
| `il43-nouns.l4` | 0 | 0 | 0 | 0 | 0 |
| `il43-cross-references.l4` | 0 | 0 | 0 | 0 | 0 |
| `il43-tests-xrefs.l4` | 0 | 18 | 0 | 0 | 0 |
| `il43-tests-xrefs-red.l4` | 2 | 0 | 2 | 0 | 2 |
| total | 2 | 18 | 2 | 0 | 2 |

The two errors are the two expected failures.
Mutation control, on copies of the modules that were deleted afterwards: two deliberate faults (the deletion day moved to 1 November 2019, and one control's target given the wrong kind) made 3 assertions fail, so the tests can fail.
The check does not see a difference that no assertion exercises.

## 9. Open questions for a domain expert

- What is to be read into s 1יג(ד)(1) and (2) now that the definition of "היתר שהותלה" has been deleted (fork E1)?
- Did an instrument between October 2015 and March 2018, or the instruments after March 2018, touch the words of s 1יג(ד)(2)? Only the consolidation's list and a text-layer reading of the later instruments say not.
- When was the definition of "היתר שהותלה" added to s 223א (fork D1)?
- What does the footer of SH 2713 print as its issue number (section 2)?
- Is the person in s 2(א1)(1) intended to be every person described in s 398(א2)(5) (fork A1)?

No domain expert has read this against the source.
