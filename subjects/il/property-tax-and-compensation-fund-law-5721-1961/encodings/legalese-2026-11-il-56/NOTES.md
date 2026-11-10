# Row il-56: four provisions of the Property Tax and Compensation Fund Law, 5721-1961, recorded as typed values with their tests

Status: draft, version 0.1.0, 2026-11-10, target compiler main.
How each claim was checked: every quotation of an official instrument was typed from a page image that was looked at, and each Hebrew word of the quotations of the three pages that carry a text layer was then found in that text layer by an ad hoc search (the footer lines of those pages have a scrambled text layer and were read from the images only, and the two year tokens on the preamble line of Kovetz HaTakanot 11193 match only with the footnote superscript fused into the year discounted; this search is not a tool in `tools/`).
Every quotation of the consolidation is expanded by `tools/srcquote.py` from the deposited excerpt, not typed.
Quoted lines that rest only on the consolidation are CONSOLIDATION-ONLY unless they are read from an official page, and each says which.
No domain expert has read this against the source.

## Scope

This row is NOT an encoding of the Property Tax and Compensation Fund Law, 5721-1961 (Sefer HaChukim 5721 p. 100).
It records four things, as typed values with tests, and keeps each as an expected-red test.
The files label them I1, I2, I3 and I4.
I1 is a date: one signature line prints a Hebrew date and a Gregorian date that name two days.
I2 is a reference: subsection (ד) of s 38לז deems a claimant to report in a method that no other provision of its chapter uses.
I3 is an indexation clause: s 38נד updates amounts each 1 January, names no organ that publishes the result, and does not say which amounts a claim for earlier damage uses.
I4 is a power and the instrument made under it: s 2א(ב) names a notice and the Finance Committee's approval, and the 2024 instrument is regulations, sets one figure for a tax year over two shares, and was signed after the 2024 tax year began.
Each item has a sound control beside it.
A date for which the sources give no answer is NOTHING; there is no REFUSE, because the target is main.

## Seat

The seat is the claimant of compensation or the taxpayer, the individual to whom the Law is applied.
This row asks no question from the seat, because it records references and dates, not rules.

## Coverage

This row does not encode the Law, so almost all of it is out of scope; the table says why for each part.

| Part | Status | Reason |
| --- | --- | --- |
| The signature line of an amendment of regulations made under s 36(א) of the Law, Kovetz HaTakanot 11420, 18 August 2024, printed page 3287 | encoded | I1. Only the two dates printed on the signature line and the dates of the footer line of the same page are recorded; nothing else about that instrument is recorded. |
| Subsection (ד) of s 38לז, with subsection (ג) and the paragraphs of subsection (ב) as control | encoded | I2. |
| Section 38נד, with the paragraphs of s 38לו and s 38לז(ב) that it cites as control | encoded | I3. |
| Section 2א(א) and (ב), the definition of tax year, and the regulations on Kovetz HaTakanot 11193, printed page 1886 | encoded | I4. |
| Every other provision of the Law, and every other instrument | out-of-scope | This row records the references of four provisions and does not encode the Law. Encoding a provision means encoding what it makes a person liable to pay or entitled to receive, which needs its own brief, its own seat questions and its own tests; none of that is attempted here, and nothing is said about whether any other provision's references resolve. |
| The 1991 regulations that the instrument of I4 amends | out-of-scope | Their own text was not read; the single figure "25%" they carry is known only from the replacement words on the page of the instrument of I4. |

## Fork register

F1 (I1). Which of the two printed dates is the error.
Reading taken: the row records that the Hebrew date and the Gregorian date on the signature line name two days, ten days apart, and does not say which one is wrong.
The day of the month printed is 1 (the letter alef); 1 Av 5784 is 5 August 2024 and 11 Av 5784 is 15 August 2024.
Reading rejected: that the Gregorian date is the signing day, and that the Hebrew date is; nothing on the crop decides it.
The words are the `ext:[KT 11420 p.3287 ...]` lines in `pt56-cross-references.l4`.

F2 (I1). The Hebrew-calendar routine is an aid, not a source.
Reading taken: the row used one routine (Calendrical Calculations, month numbering Nisan = 1), after it gave its control date, 30 Kislev 5785 = 31 December 2024, and records its days as typed values labelled with that source.
Reading rejected: treating a second routine as run; only that one was run by the builder of this row.
The footer line of the same page and the two date pairs of the instrument of I4 are run through it as controls and name one day each: 14 Av 5784 = 18 August 2024, 26 Adar I 5784 = 6 March 2024, 27 Adar I 5784 = 7 March 2024.

F3 (I2). What the target of the deeming is.
Reading taken: the deeming points at a bimonthly reporting method that the chapter recognises elsewhere, and the target is the absence of one: a search of the text layer of the whole issue that enacted the chapter (24 PDF pages) found the bimonthly and one-monthly terms once, in the deeming sentence itself, on printed page 555.
The search covers that issue, not the rest of the Law, and the row says nothing about the rest of the Law.
Reading rejected: that the deeming has another target that the search could not see, for example a category defined by other words; the search was of the two terms only.
In the consolidation the terms occur once in lines 726 to 971 of the page, at line 865 (CONSOLIDATION-ONLY; counted by a search over those lines).

F4 (I2). Whether a deeming with no other use changes anything.
Reading taken: the row does not rule on the legal effect; it records that the target category has no other use in the chapter.
Reading rejected: that the deeming is spent, or that it has effect; neither is shown by the text read.

F5 (I2). Line 865 of the consolidation is deposited in two fragments.
Reading taken: the deposit holds the words up to "וחישוב מחזור העסקאות" and from "כמי שמדווח"; the words between are not deposited and are marked […] in the excerpt and in the quotation, and nothing in the row depends on them.
Reading rejected: depositing the whole line.

F6 (I3). Which amounts a claim for earlier damage uses.
Reading taken: the row records that the clause does not say, and answers neither the amounts as enacted nor the updated amounts.
Reading rejected: either of them.
The row does not record the dates of the damage that the chapter's claims are for; it records only that the first update day (1 January 2027) is after the day the instrument that added the clause was published (4 May 2026, the footer line of printed page 561).

F7 (I3). The first update day.
Reading taken: 1 January 2027, the first 1 January after 4 May 2026; this is an INFERENCE from "on 1 January of each year", ASSUMED, not ruled, that no update fell due on 1 January 2026, before the clause existed.
Reading rejected: 1 January 2026.
The words are the sentence on the `src:967` line and on the `ext:[SH 3525 p.561 ...]` line.

F8 (I3). Whether a later instrument touched the sentence.
Reading taken: the sentence is as printed on page 561 of Sefer HaChukim 3525; the consolidation prints the same words (CONSOLIDATION-ONLY).
Reading rejected: that no later instrument touched it; none was looked for.

F9 (I4). Whether regulations published in Kovetz HaTakanot are the notice that s 2א(ב) names.
Reading taken: they are a different kind of instrument: the power names a notice (a word the consolidation prints on the `src:131` line) published in Reshumot, and the page of the instrument prints a title that says regulations and a preamble that recites making them under ss 2א and 65.
Kovetz HaTakanot is itself a part of Reshumot, so the difference recorded is a notice against regulations, not a gazette against a gazette.
Reading rejected: that publication anywhere in Reshumot satisfies the power.
Not looked for: a saving rule about the form of an instrument; if one exists, the red assertion about the kind of instrument would stop being a defect.

F10 (I4). The tax year.
Reading taken: the tax year is the twelve months beginning on 1 January (the consolidation's definition, CONSOLIDATION-ONLY, `src:114`), so the 2024 tax year began on 1 January 2024.
The instrument was signed on 6 March 2024, the 66th day of that year and 65 days after its first day.
The row records the ordering, not the number of days.
Reading rejected: a tax year that began later.
For the tax year 2025 the instrument was signed before the year began, and that is the control.

F11 (I4). One figure over two shares.
Reading taken: s 2א(א) fixes two shares, 25 percent of the property tax and 15 percent of purchase tax (the excerpt deposits line 130 only as far as those words, CONSOLIDATION-ONLY); the instrument sets one figure for each tax year.
The row records the count (two shares, one figure) and does not say to which share or shares the figure applies, because nothing in the text read says so.
The amendment that added the second share was not read, and neither were the 1991 regulations themselves.
Reading rejected: that the figure applies to both shares, and that it applies to one only.

## Answer table

| | I1: the date | I2: the deeming | I3: the clause | I4: the power and the instrument |
| --- | --- | --- | --- | --- |
| What the citing words say | The Hebrew date printed is the day of the month 1 of Av 5784. | Subsection (ד) of s 38לז treats a claimant who changed method as reporting bimonthly. | Section 38נד updates the listed amounts on 1 January of each year by the rise of an index. | Section 2א(ב) lets the Minister of Finance, with the Finance Committee's approval, change the rate, and says a notice is published in Reshumot. |
| What the target says | The Gregorian date printed beside it is 15 August 2024, which is 11 Av 5784; 1 Av 5784 is 5 August 2024. | No other provision of the chapter uses a bimonthly or one-monthly method (one occurrence in the issue, the deeming itself). | It names no organ that publishes the result, and says nothing about which amounts a claim for damage before 1 January 2027 uses. | The instrument is regulations, recites the Committee's approval, sets one figure for a tax year over two shares, and was signed on 6 March 2024. |
| Exists | The two dates name two days, ten days apart. | No: the target has 0 of the 1 method named. | No organ is named; the question is open. | A different kind of instrument; the approval agrees; the 2024 signing day is after the year began. |
| Limb (a) | The routine's day, after its control date. | A search of the official text layer, the issue not deposited. | The official page, read from its image, the crop deposited. | CONSOLIDATION-ONLY for the power and the year. |
| Limb (b) | The official page, read from its image, the crop deposited. | The official page, read from its image, not deposited. | The official page, read from its image, the crop deposited; no later instrument looked for. | The official page, read from its image, the page extract deposited. |
| Page read | Kovetz HaTakanot 11420, printed page 3287. | Sefer HaChukim 3525, printed page 555 (not deposited). | Sefer HaChukim 3525, printed page 561. | Kovetz HaTakanot 11193, printed page 1886. |
| Control | The footer line of the same page: 14 Av 5784 = 18 August 2024. | Subsection (ג) cites paragraph (7) of subsection (ב), and it is there. | The two citations inside the clause resolve: paragraphs (1) to (3) of the definition in s 38לו, and paragraphs (1) to (7) of subsection (ב). | The approval recited agrees with the approval required, and the tax year 2025 figure was signed for before its year began. |

## The nine expected-red assertions, one by one

`pt56-tests-xrefs-red.l4` holds nine assertions, all failing, and `check.sh` and `encoding.json` declare that count (9).
1. `the two dates on the line name one day` for the signature line is FALSE.
2. The days from the routine's day to the Gregorian date printed on the signature line are 10, not 0.
3. `the citation points at what it says` for the deeming is FALSE.
4. `the target has everything the citing words name` for the deeming is FALSE (the target has 0 of 1).
5. `the clause names an organ that publishes the updated amounts` is FALSE.
6. The clause's record of whether it says which amounts a claim for earlier damage uses is FALSE.
7. `the instrument is the kind of instrument the power names` is FALSE (a notice against regulations).
8. `the instrument was signed before the tax year began` for the tax year 2024 is FALSE.
9. `the instrument sets one figure for each base the statutory rate is set on` is FALSE (one figure, two shares).

## The check

Run from this folder with `L4=$HOME/.cache/l4-main/98/l4 ./check.sh`; the `l4` that wrote the row was 1.6.98 (main, 7689b0d, 2026-10-19) and the main build it was compared with was 1.6.109 (main, 4c887e0, 2026-11-04).

| module | errors | satisfied | failed | refused | expected failed | main: errors | satisfied | failed | refused | main verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pt56-cross-references.l4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | same |
| pt56-nouns.l4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | same |
| pt56-tests-xrefs-red.l4 | 9 | 0 | 9 | 0 | 9 | 9 | 0 | 9 | 0 | same |
| pt56-tests-xrefs.l4 | 0 | 43 | 0 | 0 | 0 | 0 | 43 | 0 | 0 | same |

The nine errors are the nine failed assertions, each reading "assertion failed"; no other error, and no refusal.
`python3 -I tools/hebcheck.py ../../registers/source-bundle/property-tax-and-compensation-fund-law-5721-1961.he.wiki.excerpt.txt *.l4 NOTES.md` exits 0: every run of Hebrew outside a quotation line occurs in the deposited excerpt.

## The deposits

UNOFFICIAL aid: the Hebrew Wikisource consolidation of the Law, revision 3090567 (last edited 2026-10-18T14:30:09Z).
The whole page content has sha256 2952f8c1d814ed72e52ad7ebc3bc6894b1c849084f6de09e3423dad7182ab2d4 and 235547 bytes as retrieved on 2026-11-10; the excerpt deposited has sha256 188cd8719ec8d8678370eb2eefd43418153176a2485f378321b5920982e7dfb1 and 6486 bytes.
The excerpt says in its first lines which lines of the whole page it copies, and each line carries its number in the whole page, so that `src:N` means the line N of the page.
Official pages, in `registers/source-bundle/official/`: a page extract of Kovetz HaTakanot 11193, printed page 1886 (sha256 9bd93b1e5b5a6f08f8d339587ea1b9faaf5436bd003e3a29b296425b89831f31); a cropped image of the signature lines of Kovetz HaTakanot 11420, printed page 3287, in three bands (sha256 6ec9ecde0076df923dbd7b6cb2349a5a2c02e7e3c95d2fea32de62b2cb263e00); a cropped image of section 38נד and the footer line of Sefer HaChukim 3525, printed page 561 (sha256 6bc594aeeb80bcff19a15a4fa8b08dd13c433ac2fe97e5a2b41d4f209704bee0).
Only the pages read are deposited, and no full-page image of any page is deposited.
`registers/source-bundle/SOURCES.json` gives the whole file's sha256 and size for each instrument; the addresses of the two Kovetz HaTakanot files are the host's address pattern and were not re-fetched, and the address of the Sefer HaChukim 3525 file is the one recorded for the identical file (same sha256 and size) in the SOURCES.json of the row for the Women's Employment Law.
Printed page 555 of Sefer HaChukim 3525, where the deeming sentence stands, was read from its image and is not deposited, because the page holds text that is no part of this row.

## What was not done

The text of the 1991 regulations and the amendment that added the second share to s 2א(א) were not read.
No later instrument was looked for that touched s 38נד, s 38לז(ד) or s 2א(ב), and no saving rule about the form of an instrument was looked for.
Only one Hebrew-calendar routine was run, not a second.
The Knesset address of the Sefer HaChukim 3525 file, and the download address of the two Kovetz HaTakanot files as actually used, were not established by this row.
Of the issue of Kovetz HaTakanot 11420 the row records only the dates of the signature line and of the footer line; the preamble that the description of the instrument rests on was viewed on its own page, which is not deposited.
The cover of Kovetz HaTakanot 11193 was read from its text layer only, and is not deposited.
