# Row il-57: three references in the Women's Employment Law, 5714-1954, that Amendment 67 and a 2026 amendment left uneven

Status: draft, version 0.1.0, 2026-11-10, target compiler main.
How each claim was checked: every quotation of an official instrument was typed from a cropped page image that was looked at (the images are deposited), and `tools/pdfcheck.py` then confirmed that each Hebrew word of it occurs in the text layer of that page in the file as downloaded (18 quotation lines, no word missing; the four footer lines are tagged `footer` and are NOT checked, because the text layer prints a footer in visual order).
Every quotation of a consolidation is expanded by `tools/srcquote.py` or `tools/extquote.py` from the deposited excerpt, not typed.
A reading that rests only on a Hebrew Wikisource consolidation is labelled CONSOLIDATION-ONLY on its line and in this file.
No domain expert has read this against the source.

## Scope

This row is NOT an encoding of the Women's Employment Law, 5714-1954 ("the Law"), and it does not encode the National Insurance Law.
It records three references that the printed texts show, as typed values with tests, and keeps each defect as an expected-red test.
The first is a list of extensions: section 6(ב)(2) of the Law defines the term "הארכות" by listing sections 6(ב1), (ג) and (ד), while Amendment 67 (Sefer HaChukim 3482, printed p. 214) added a further extension in a new section 6(ד3) and put it into the cumulation rule in section 6(ד2) but not into that definition.
The second is a list of subsections: section 51(ד) of the National Insurance Law fixes the payment date of the additional maternity allowance of subsections (א) and (א1), and Amendment 67 section 2 added a subsection (א3) that gives the same kind of allowance without touching (ד); the National Insurance Law appears only as the TARGET of that reference.
The third is a pronoun: the words that Sefer HaChukim 3525 (printed p. 563, section 5(2)) puts into a paragraph whose head names "עובד או עובדת" use a feminine form for the five-day limb, while the same instrument's replacement in the National Insurance Law's definition uses a masculine form under a masculine noun.
Each item has one sound control beside it.
A date that the sources held do not give is NOTHING; there is no REFUSE, because the target is main.

## Seat

The seat is an employee on or returning from maternity or adoption leave: the individual to whom sections 6, 7 and 9 of the Law, and section 51 of the National Insurance Law, are applied.
This row asks no question from the seat, because it records references and wording, not rules.

## Coverage

This row does not encode the Law, so almost all of it is out of scope; the table says why for each part.

| Part | Status | Reason |
| --- | --- | --- |
| Section 6(ב)(2): the definition of "הארכות" by a list of three subsections | encoded | Item 1, the defect. |
| Section 6(ד2) and (ד3) as Amendment 67 section 1 changes and adds them | encoded | Control 1 for item 1: the cumulation rule names (ד3); the record of (ד3) is quoted. |
| Section 6(ח)(1א) and section 7(ד)(1), which use the defined term | encoded | Recorded as the definition's dependants, with the definition's description and no claim of their own. |
| Section 6(ז1)(2) and section 9ג(ב), two lists that print no (ד3) | encoded | Recorded as printed. Whether they should name (ד3) is a policy question the row does not answer (fork R3). |
| Section 51(ד) of the National Insurance Law, and (א3) as Amendment 67 section 2 adds it | encoded | Item 2, the defect, and control 2. The National Insurance Law is cited only as a target. |
| The five-day limb of the paragraph quoted as section 9(ג)(2ג)(א) of the Law, and the same replacement in the National Insurance Law's definition | encoded | Item 3, the defect, and control 3. Only the pronoun and its verb are recorded. |
| Every other provision of the Law (the rest of section 6, sections 1 to 5, 7, 8, 9 and following, the schedules) | out-of-scope | This row records three references and does not encode the Law. Encoding a section means encoding what it grants or forbids, which needs its own brief, its own seat questions and its own tests; none of that is attempted, and nothing is said about whether any other citation in the Law stands. |
| The National Insurance Law beyond the lines of section 51 quoted above | out-of-scope | It is a target here, not a subject. Its rates, conditions and procedure are not read. |
| The instruments other than the pages named in the answer table | out-of-scope | Only those pages were read; whether any later or earlier instrument touched the words was not looked for, and each limb says so. |

## Fork register

D1. The day Amendment 67 took effect.
Reading taken: 1 April 2026, the builder's computation from the printed sentence of section 3 ("on the 1st of the month after the end of 60 days from its publication") and the issue date printed in the footer of p. 214, 7 January 2026; 60 days from that day end on 7 or 8 March 2026 by either usual count, so the first of the next month is 1 April 2026 either way.
Reading rejected: a day taken from a table of commencement dates or from the consolidation; none was looked at.
The Hebrew that licenses the computation is on the `ext:[SH 3482 ...]` lines for section 3 and the footer in `we57-cross-references.l4`; the issue date was taken as the day of publication, which is itself an assumption.

D2. Whether anything later than Amendment 67 and the 2026 instruments touched the quoted words.
Reading taken: that is CONSOLIDATION-ONLY. Limb (b) of each defect says `the official instrument, read from its page image; that no later instrument touched the words is CONSOLIDATION-ONLY`, because the consolidation (revision 3084933, last edited 2026-09-27T06:30:08Z) prints the words unchanged and its tags were not matched to instruments.
Reading rejected: treating the consolidation's silence as a finding that no later instrument exists.

R1. Whether section 6(ב)(2)'s list is the definition's only input.
Reading taken: the term is defined by the list in 6(ב)(2) ("(להלן – הארכות)") and no other definition was looked for in the Law's consolidation.
Reading rejected: that section 6(ד2)'s cumulation rule is itself a definition of the term; it counts the extensions, it does not name them "הארכות".

R2. What the dependants are.
Reading taken: section 6(ח)(1א) and section 7(ד)(1) print the term and so take the definition's description; each is recorded with the description the definition gives and with no claim about what it does to a person who uses (ד3).
Reading rejected: asserting an effect on unpaid leave or on the floor in section 6(ב)(2); the definitional gap stands without any effect claim, and none is read from the sources here.

R3. Whether sections 6(ז1)(2) and 9ג(ב) should also name (ד3).
Reading taken: that is a policy question; the row records what each list prints, asserts that neither names (ד3), and asserts nothing about whether it should.
Reading rejected: calling them defects, or leaving them out.

P1. Whether the feminine pronoun is a defect or a reading a court would correct.
Reading taken: the printed pronoun and its verb are feminine and the head names a masculine and a feminine noun; the pronoun fits one of them (green test) and does not fit both (red test); the row says no more.
Reading rejected: a ruling that the words are read as referring to the employee, or that they are not; the question is not asked.

P2. Which words are "the five-day limb".
Reading taken: the words inserted by section 5(2) of Sefer HaChukim 3525 after the replaced words "for a continuous period of at least 14 days" (the Hebrew is on the ext: line for Sefer HaChukim 3513 p. 461 in `we57-cross-references.l4`; read on that page), as printed on p. 563.
Reading rejected: the whole paragraph; only the limb that carries the pronoun is recorded.

N1. The revision of the National Insurance Law's consolidation.
Reading taken: the excerpt copies lines from the whole-page deposit already in this repository; its Wikisource revision id is recorded in `SOURCES.json` if a one-call history lookup matched it, and otherwise the sha256 of the whole page is the identification (see the deposits below).
Reading rejected: re-fetching the whole 1.1 MB page, which the brief did not ask for.

C1. Crops instead of page extracts.
Reading taken: each page read carries text outside the three items (the footnotes of p. 214 cite other instruments; pp. 461, 562 and 563 carry other provisions), so cropped images of the lines read are deposited and no PDF is.
Reading rejected: depositing the pages whole.

## Answer table

| | Item 1: the definition of "הארכות" | Item 2: section 51(ד) | Item 3: the pronoun | Control 1 | Control 2 | Control 3 |
| --- | --- | --- | --- | --- | --- | --- |
| What the citing words say | The extensions under 6(ב1), (ג) and (ד). | The payment date for the additional allowance of 51(א) and (א1). | The five-day limb, "שהיא הוצאה", feminine, under a head naming "עובד או עובדת". | Section 6(ד2) counts the extensions of (ב1) to (ד) and (ד3) together. | Section 51(א3) cites section 6(ד3). | The same replacement in the National Insurance Law's definition, masculine, under "של עובד". |
| What the target says | Four extensions: (ב1), (ג), (ד) and (ד3), as 6(ד2) counts them. | Three subsections give the allowance: (א), (א1) and (א3). | A head naming a masculine and a feminine noun. | The same four. | Section 6(ד3) exists as Amendment 67 section 1(2) inserts it. | A head naming one masculine noun. |
| Exists | The term exists; its list is short of (ד3). | The date rule exists; its list is short of (א3). | The words exist as printed. | Yes. | Yes. | Yes. |
| Limb (a) | CONSOLIDATION-ONLY (older instruments that last changed the line were not read). | CONSOLIDATION-ONLY (section 51(ד) as the consolidation prints it). | CONSOLIDATION-ONLY for the paragraph as it stands; the words replaced are read on Sefer HaChukim 3513 p. 461. | CONSOLIDATION-ONLY. | CONSOLIDATION-ONLY for the line; the new (ד3) is on p. 214. | Read from the page image of p. 562. |
| Limb (b) | Read from p. 214, section 1: two instructions only, in (ד2) and the new (ד3); nothing touches 6(ב)(2), 6(ח)(1א), 7(ד)(1), 6(ז1)(2) or 9ג(ב). | Read from p. 214, section 2: only (א3) is added, before subsection (ב); nothing touches (ד). | Read from p. 563, section 5(2). | As item 1. | Read from p. 214, section 2. | Read from p. 562, section 5(1). |
| Page read | Sefer HaChukim 3482 p. 214 | Sefer HaChukim 3482 p. 214 | Sefer HaChukim 3525 p. 563; 3513 p. 461 | Sefer HaChukim 3482 p. 214 | Sefer HaChukim 3482 p. 214 | Sefer HaChukim 3525 p. 562 |
| The one-line amendment that would repair it (proposed, not enacted) | In section 6(ב)(2) replace "(ב1), (ג) ו־(ד)" by "(ב1), (ג), (ד) ו־(ד3)". | In section 51(ד) replace "(א) ו־(א1)" by "(א), (א1) ו־(א3)". | Replace the feminine form by a wording that fits both nouns, in section 3(1) of the 2026 law as quoted. | n/a | n/a | n/a |

Amendment 67 takes effect on the first of the month after 60 days from publication (section 3); the day used is 1 April 2026 (fork D1).

## The expected-red assertions, one by one

`we57-tests-xrefs-red.l4` holds five assertions, all failing, and `check.sh` and `encoding.json` declare that count (5).
1. `the citation points at what it says` for the definition of the extensions is FALSE: the citing words describe three subsections, the target four.
2. `the citing words are complete on` 10 November 2026 for the same definition is JUST FALSE, not JUST TRUE.
3. `the citation points at what it says` for section 51(ד) is FALSE: two subsections against three.
4. `the citing words are complete on` 10 November 2026 for section 51(ד) is JUST FALSE, not JUST TRUE.
5. `the pronoun fits every noun the head names` for the Law's five-day limb is FALSE: the pronoun and its verb are feminine, the head names a masculine and a feminine noun.
The failures were read in the diagnostics: the five failing ranges are lines 16, 18, 23, 25 and 30 of the file, each "assertion failed".
The green file asserts the same functions on the three controls and gets TRUE or JUST TRUE.

## The check

Run from this folder with `L4=$HOME/.cache/l4-main/98/l4 ./check.sh` (the cached stable build); check.sh's own main build was 1.6.109 (main, 4c887e0, 2026-11-04).

| module | errors | satisfied | failed | refused | expected failed | main: errors | satisfied | failed | refused | main verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| we57-cross-references.l4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | same |
| we57-nouns.l4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | same |
| we57-tests-xrefs-red.l4 | 5 | 0 | 5 | 0 | 5 | 5 | 0 | 5 | 0 | same |
| we57-tests-xrefs.l4 | 0 | 38 | 0 | 0 | 0 | 0 | 38 | 0 | 0 | same |

The five errors are the five failed assertions; no other error, and no refusal.
`tools/hebcheck-all.sh *.l4 NOTES.md` exits 0.
`tools/pdfcheck.py *.l4` with `SH3482_PDF`, `SH3513_PDF` and `SH3525_PDF` naming the files as downloaded checked 18 quotation lines and found no problem; without those variables it skips them and says so.
No PDF is deposited, so there is nothing for a text-layer scan of the deposits to read.

## The deposits (UNOFFICIAL aids first)

Hebrew Wikisource consolidation of the Law, revision 3084933 (last edited 2026-09-27T06:30:08Z): the whole page has sha256 68e91f1e3691df168468bdeac5d3764969d7c7e1d18e43278c253b0a5380ecad and 129522 bytes as retrieved on 2026-11-10; the excerpt deposited has sha256 fa1afc685b6d1d01195b0f58e81de7540d305f256026d574cabfd37c66567b13 and 5333 bytes.
Hebrew Wikisource consolidation of the National Insurance Law: its Wikisource revision id is NOT established: the deposit on main does not record it, and two one-call history lookups on 2026-11-10 each gave up (exit status 75) after 300 s without obtaining the relay lock. the whole page has sha256 78bf47ee29a300d51c5c7646cf85992d7de78aa1380bd8460a4a18265f552a97 and 1097449 bytes; the excerpt deposited has sha256 c7313097f67554affc5d6ccb08483cbc92dc0bad794125ec98342c5c85534be1 and 2301 bytes.
Each excerpt says in its first lines which lines of the whole page it copies and which only in part, and each line carries its number in the whole page, so that `src:N` and `ext:[ni] N` mean the line N of the page.
The official pages are four cropped images in `registers/source-bundle/amending-laws/`: Sefer HaChukim 3482 printed p. 214 (sections 1 to 3 and the footer), 3513 printed p. 461 (section 3(1), the first lines of the inserted paragraph and the footer), 3525 printed p. 562 (section 5(1), without its middle line) and printed p. 563 (section 5(2)); the sha256 and size of each, and of each whole file as downloaded (not deposited), are in `registers/source-bundle/SOURCES.json`.
The crop of p. 461 cuts off the first word of the paragraph's second line, and the crop of p. 562 leaves out the line between its first two bands; the text layer of p. 461 holds each line twice, so its words were checked by presence only.

## What was not done

No instrument other than the four pages above was read, and whether any later instrument touched the quoted words was not looked for.
The 2026 law that Sefer HaChukim 3513 prints and Sefer HaChukim 3525 amends was read only at section 3(1) and section 5.
The National Insurance Law's consolidation was not re-fetched; what is known of its revision is in `SOURCES.json`.
Amendment 67's date of effect is a computation (fork D1), not a printed date.
Whether any of the three defects has any effect on anyone was not examined.
