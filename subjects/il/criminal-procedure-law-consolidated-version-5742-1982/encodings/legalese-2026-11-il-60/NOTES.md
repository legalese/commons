# Row il-60: one reference in the Criminal Procedure Law [Consolidated Version], 5742-1982, and the last day its target prints

Status: draft, version 0.1.0, 2026-11-10, target compiler main.
How each claim was checked: every quotation of the official instrument was typed from a page image that was looked at, and each Hebrew word of 4 of the 5 quotation lines (printed pp. 1016 and 1017 of Sefer HaChukim 2999) was then found in the text layer of the corresponding page of the whole file (PDF pages 2 and 3) by an ad hoc search; the fifth, the footer line of printed p. 1017, was read from the page image only, because the footer's text layer is garbled (this search is not a tool in `tools/`).
Every quotation of the consolidation is expanded by `tools/srcquote.py` from the deposited excerpt, not typed.
The Hebrew dates were converted with the Hebrew-calendar routine in `tools/hebcal.py`, run through `tools/datepairs.py`, which reproduces the routine's own control (30 Kislev 5785 = 31 December 2024) first.
No domain expert has read this against the source.

## Scope

This row is NOT an encoding of the Criminal Procedure Law [Consolidated Version], 5742-1982 (published in Sefer HaChukim 5742).
It records one reference, as typed values with tests, and keeps it as an expected-red test, with one sound control beside it.
The reference is the words "ובסעיף 220ד(א)(4)" in section 220ג(ג), as the instrument printed in Sefer HaChukim 2999 (7 Tammuz 5782, 6 July 2022) has them; printed pp. 1016 and 1017 of it are the pages read here.
The instrument's title is, in the row's English rendering (not an enacted title), "Criminal Procedure Law (Amendment No. 92 - Temporary Provision), 5782-2022".
The words name paragraph (4) of subsection (א) of section 220ד.
The words of that paragraph end "הוראה זו תעמוד בתוקפה עד יום ו׳ באב התשפ״ה (31 ביולי 2025)".
The row records the pair, 6 Av 5785 and 31 July 2025, checked with the Hebrew-calendar routine, and the last day the paragraph prints, as typed values.
The control is the reference to subsection (ב) of the same section, in the same sentence, whose words print no day, and the date pair printed in the footer of the same page, 7 Tammuz 5782 and 6 July 2022.
The row records what each instrument prints and says nothing about any other section of the Law, any other amendment, any other provision that carries a date, or any end date other than the one printed in that paragraph.
A date that the sources held do not give is NOTHING; there is no REFUSE, because the target is main.

## Seat

The seat is the person charged in a criminal case (the נאשם), to whom the Law's procedure is applied.
This row asks no question from the seat, because it records one reference and its control, not rules.

## Coverage

This row does not encode the Law, so almost all of it is out of scope; the table says why for each part.

| Part | Status | Reason |
| --- | --- | --- |
| Section 220ג(ג): the words "ובסעיף 220ד(א)(4)" and the label they name | encoded | The finding. Only the words that name the paragraph and the label are recorded; the rest of the subsection is quoted as the consolidation prints it and is not discussed. |
| Section 220ד(א)(4): the label (4), the paragraph's own printed last day (6 Av 5785 = 31 July 2025) and that pair | encoded | The target of the finding. The row records that the paragraph exists on the printed page, the day it prints and the day after it as the first day certainly past it. |
| Section 220ג(ג): the words "בסעיף קטן (ב)" and subsection (ב) of section 220ג as printed on pp. 1016 to 1017 | encoded | Control for the finding: a sibling reference in the same sentence whose target prints no day. |
| The footer of printed p. 1017: the issue line with its Hebrew date and its Gregorian date (7 Tammuz 5782 = 6 July 2022) | encoded | Control date pair, printed on the same page as the finding's pair. |
| Every other provision of the Law, including the other subsections and paragraphs of the two sections the reference sits in | out-of-scope | This row records one reference and its control and does not encode the Law. Encoding a provision means encoding what it requires, allows or forbids, which needs its own brief, its own seat questions and its own tests; none of that is attempted here, and the row says nothing about those provisions. |
| Instruments published after Sefer HaChukim 2999 that may have touched the two sections | out-of-scope | None was read. The consolidation's amendment tags on the two section headings are the only evidence about them, and every reading that depends on them says CONSOLIDATION-ONLY. |

## Fork register

E1. Whether the day printed as the last day is itself within the paragraph's period.
The Hebrew is "הוראה זו תעמוד בתוקפה עד יום ו׳ באב התשפ״ה (31 ביולי 2025)", and the words do not say whether "עד יום" takes the printed day in or leaves it out.
Reading taken: the words do not settle it, so the row records the printed day (31 July 2025) and the day after it (1 August 2025) as the first day that is certainly past it on either reading; `the target stands on` answers JUST FALSE from 1 August 2025 and NOTHING on the printed day.
The row reads no day on which the paragraph began, so it also answers NOTHING on every earlier day.
Reading rejected: that the printed day is in (the answer would be JUST TRUE through 31 July 2025), and that it is out (JUST FALSE from 31 July 2025); neither is licensed by the words.

E2. Whether a later instrument changed the paragraph's printed day or the words of section 220ג(ג).
Reading taken: none was looked for; the consolidation prints the same words and the same day, and the heading lines of the two sections carry one amendment tag each, "תיקון: תשפ״ב־4", and no other (the `src:1323` and `src:1329` lines in `cp60-cross-references.l4`); that is CONSOLIDATION-ONLY.
The tag's number agrees with the consolidation's own header, which lists this instrument (printed p. 1016) as the fourth entry for 5782; the header is not deposited, and that reading is CONSOLIDATION-ONLY too.
So each limb says "the official instrument, read from its page image; that no later instrument touched the words is CONSOLIDATION-ONLY".
Reading rejected: treating the consolidation's silence as an official finding that no later instrument exists.

E3. Which subsection (ב) the bare words "בסעיף קטן (ב)" name.
Reading taken: subsection (ב) of section 220ג, the section the sentence sits in, because the words name no other section for it, while the next words name section 220ד explicitly.
Reading rejected: a subsection (ב) of another section, which the words do not name.

E4. The day on which the first expected-red assertion asks whether the paragraph stands.
Reading taken: 10 November 2026, the day the row was built; the module has no clock, so the day is typed.
Reading rejected: any day computed from the machine's clock, which would make the count of failing assertions depend on when the row is run.

## Answer table

| | Finding | Control (reference) | Control (date pair) |
| --- | --- | --- | --- |
| What the citing words say | "ובסעיף 220ד(א)(4)" names paragraph (4) of subsection (א) of section 220ד. | "בסעיף קטן (ב)" names subsection (ב) of section 220ג. | Not a citation: the footer prints a Hebrew date and a Gregorian date side by side. |
| What the target says | The paragraph ends "הוראה זו תעמוד בתוקפה עד יום ו׳ באב התשפ״ה (31 ביולי 2025)". | Subsection (ב), printed from the foot of p. 1016 to the head of p. 1017, prints no day. | 7 Tammuz 5782, 6 July 2022. |
| Exists | Yes, on printed p. 1017. | Yes, on printed pp. 1016 to 1017. | Yes, on printed p. 1017. |
| Pair checked with the routine | 6 Av 5785 = 31 July 2025: matches. | none | 7 Tammuz 5782 = 6 July 2022: matches. |
| Limb (a) | The official page read; that no later instrument touched the paragraph is CONSOLIDATION-ONLY. | The same. | The official page read. |
| Limb (b) | The official page read; that no later instrument touched section 220ג(ג) is CONSOLIDATION-ONLY. | The same. | n/a |
| Page read | Sefer HaChukim 2999, printed p. 1017 | Sefer HaChukim 2999, printed pp. 1016 and 1017 | Sefer HaChukim 2999, printed p. 1017 (footer) |

The footer's text layer is garbled, so its Hebrew date and Gregorian date were read from the page image only.
The Hebrew date of the paragraph's last day was read from the page image and the words of the paragraph were also found in the text layer by the ad hoc search; its Gregorian date, 31 July 2025, stands in the page image beside it.

## The expected-red finding, assertion by assertion

`cp60-tests-xrefs-red.l4` holds two assertions, both failing, and `check.sh` and `encoding.json` declare that count (2).
1. `the target stands on` 10 November 2026 is JUST TRUE, which the citing words need: it is JUST FALSE, because 10 November 2026 is after the day after the printed day.
2. `the target stands on` 1 August 2025 is JUST TRUE, which the citing words need: it is JUST FALSE, because 1 August 2025 is the first day certainly after the printed day.
Both fail with JUST FALSE, not with NOTHING.
The row records this and says nothing about what the citing words are for or whether anyone should change them.

## The check

Run from this folder with `L4=$HOME/.cache/l4-main/98/l4 ./check.sh`; the main build was 1.6.109 (main, 4c887e0, 2026-11-04).

| module | errors | satisfied | failed | refused | expected failed | main: errors | satisfied | failed | refused | main verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cp60-cross-references.l4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | same |
| cp60-nouns.l4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | same |
| cp60-tests-xrefs-red.l4 | 2 | 0 | 2 | 0 | 2 | 2 | 0 | 2 | 0 | same |
| cp60-tests-xrefs.l4 | 0 | 31 | 0 | 0 | 0 | 0 | 31 | 0 | 0 | same |

The two errors are the two failed assertions; no other error, and no refusal.
`python3 -I tools/hebcheck.py <the deposited excerpt> *.l4 NOTES.md` exits 0, the ad hoc search of the text layers (not a tool in `tools/`) checked 4 quotation lines with no word missing and skipped 1 (the footer), and `python3 -I tools/datepairs.py` reproduces the routine's control and both pairs.

## The deposits

Hebrew Wikisource consolidation of the Law, revision 3079022 (timestamp 2026-08-25T07:00:46Z), an UNOFFICIAL aid: the whole page has sha256 3ae6b4c35e9f704f317a71ff743cb83455c559b3250772936ff98e9631e88725 and 396525 bytes as retrieved on 2026-11-10 through the MediaWiki API; the excerpt deposited has sha256 4223a40cc8acb27bbc599701af7da06b7d4c53ef3c68f803d6d295c3dc9fc263 and 1988 bytes.
The excerpt says in its first lines which lines of the whole page it copies (the title line and four lines), and each line carries its number in the whole page, so that `src:N` means the line N of the page.
The official pages are two composed images of cropped bands of Sefer HaChukim 2999, each with its bands separated by grey bars: `registers/source-bundle/official/sh2999-5782-p1016-bands.png` (printed p. 1016, PDF page 2 of the 12-page file) and `registers/source-bundle/official/sh2999-5782-p1017-bands.png` (printed p. 1017, PDF page 3).
The first holds the first three lines of subsection (ב) of section 220ג, which begin at the foot of the page, and the footer line.
The second holds the continuation of subsection (ב) and the whole of subsection (ג), the first line of section 220ד(א) (which shows the label), paragraph (4) of 220ד(א) alone, and the footer line.
Nothing else of either page is deposited, and both images were viewed after they were composed.
The rest of the file is not deposited; `registers/source-bundle/SOURCES.json` records its URL, sha256 and size as supplied, and the sha256 and size of the two images and of the excerpt.
No full page of the file is deposited.

## What was not done

No instrument published after Sefer HaChukim 2999 was read, so the statement that none changed the paragraph or section 220ג(ג) rests on the consolidation's amendment tags alone.
The tags of the other sections of the consolidation were not read.
The day the paragraph began was not read, so the row answers NOTHING for every day up to and including the printed day.
The text layer of the footer of printed p. 1017 was not checked, because it is garbled.
