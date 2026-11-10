# Row il-42: Real Estate Taxation (Appreciation and Purchase) Law, 5723-1963

Status: draft, version 0.1.0, target compiler main.
No domain expert has read this against the source.
Every claim below was checked against the deposited text or a page image named beside it; where it was not, it says so.
Correction note of 2026-11-10: the two replacement windows (s 9(ג1ג)(2)(ב) and s 49C(1)) were corrected to Amendment 85; see "Correction note, 2026-11-10" below.

## Correction note, 2026-11-10: the replacement windows of s 9(ג1ג)(2)(ב) and s 49C(1)

What was wrong.
The row gave 24 months to every day except 1 June 2023 to 31 May 2025, for both the time to sell the former only dwelling (s 9(ג1ג)(2)(ב)) and the time within which a replacement dwelling must have been bought (s 49C(1)), through one function.
That followed the consolidation, which prints 24 months in both places and carries none of the instrument that moved those windows in 2016 and 2021.

Which instrument.
Amendment 85, Sefer HaChukim 2544 (6 April 2016) p. 694, read from the page image rendered at 250 dpi on 2026-11-10.
The page is not deposited whole, because it also carries the opening of an unrelated Act; the lines read are deposited as four cropped images in `../../registers/source-bundle/amending-laws/`: one each of ss 3, 5 and 6 and one of the footer (`sh2544-5776-p694-crop-s3.png`, `-crop-s5.png`, `-crop-s6.png`, `-crop-footer.png`), all in `SOURCES.json` with the sha256 of the whole file as downloaded.
- Section 3(1) changes "18 months" to "24 months" in s 49C(1), and only there (section 3(2) adds the inherited share of a half to s 49C(3)).
- Section 5 is a temporary provision: for five years from 23 Nisan 5776 (1 May 2016) s 9(ג1ג)(2)(ב) is read with "18 months" in place of "24 months", and that reading applies to a right in land bought in that period.
- Section 6 starts s 49C(1) as changed by s 3(1) at the end of that period, and applies it to a dwelling bought at the end of the period or later as a replacement for the dwelling sold.
Read together, the Amendment brings the two windows level and then lifts both: before 1 May 2016 s 9 read 24 months (SH 2405, 5 August 2013, p. 155, read from the page image, where the paragraph was created) and s 49C(1) read 18; in the period both read 18; from 1 May 2021 both read 24 (and both read 18 for 1 June 2023 to 31 May 2025, fork T2).
So the two windows differ before the period and agree from its first day, which is why each section has a function of its own.

What changed.
- `re42-s9-purchase-tax.l4`: `the months within which the former only dwelling must be sold, for an ordinary purchase` returns 18 for a purchase from 1 May 2016 to 30 April 2021 as well as for 1 June 2023 to 31 May 2025, and 24 for every other day.
- `re42-s49-exemptions.l4`: a new function `the months within which the replacement must have been bought, under section 49C(1)` returns 18 for a replacement bought on or before 30 April 2021 and for 1 June 2023 to 31 May 2025, and 24 for every other day; `the replacement was bought in time` uses it.
  The two sections no longer share a function, so their windows cannot be confused.
- The header comment of s 49C(1) in `re42-s49-exemptions.l4` said "24 months with the 2023-25 exception"; it now says what is above.
- Fork T2 no longer says that one window drives both sections; fork T3 (below) is new.

What it changes in an answer.
A seller whose replacement dwelling was bought on or before 30 April 2021 and who sold more than 18 months later no longer keeps the only-dwelling status through s 49C(1) (for example: bought 1 January 2020, sold 1 September 2021, 20 months later: the old row said the other dwelling did not stand against the seller, the instrument says it does).
A buyer from 1 May 2016 to 30 April 2021 who sold the former only dwelling in month 19 to 24 no longer counts as having sold in time under s 9(ג1ג)(2)(ב).
No amount of purchase tax moves, because no single-dwelling ladder is held for those days (the answer table in section 7).

What the control showed.
The 50 new assertions (22 in `re42-tests-s9.l4`, 28 in `re42-tests-seller.l4`) were run against the old modules, byte-identical to the ones at origin/main f2c31d7b7: 16 failed (7 and 9), 389 satisfied, no other error and no refusal, and the same 50 assertions with the corrected modules all hold (405 satisfied, 0 failed).
The 7 that failed in `re42-tests-s9.l4` are the window for a purchase on 1 May 2016, 1 January 2020 and 30 April 2021 (the old function says 24), and the sale in month 19 after a purchase on 1 May 2016, 1 January 2020 and 30 April 2021, and in month 24 after one on 1 January 2020 (the old rule says in time).
The 9 that failed in `re42-tests-seller.l4` are a sale just beyond 18 months after a replacement bought on 1 January 2016, 30 April 2016, 1 May 2016, 1 January 2020 (two sale days) and 30 April 2021 (the old rule says the replacement was bought in time), and the same facts one step on: the other dwelling stands against you (1 January 2020, sold 1 September 2021) and the sold dwelling is your only dwelling under s 49B(2) (the same purchase, sold 2 July and 1 September 2021).
The 34 new assertions that held on the old modules too are the ones the two rules answer alike: the last day inside an 18-month window (24 months contains it), and every day where both rules say 24 months (before the period for s 9, after it for both sections) or 18 months (Amendment 102).
No assertion that was already here was changed: all 355 hold unchanged, including the one near line 590 of `re42-tests-seller.l4` (a 2020 sale with no replacement dwelling, which does not depend on a window).

What was not settled.
Fork T3 (the last day of the period, and the Interpretation Law's rule for "five years from", which was not read).
Whether the words of s 49C(1) read 18 months on every day before 6 April 2016 was not checked: s 3(1) shows 18 months at that date (official), and the consolidation's amendment tags for s 49C show none between 5773 and 5776 (CONSOLIDATION-ONLY); the row answers 18 for every replacement bought before 1 May 2016.
That Amendment 102 reaches s 49C(1) as it reaches s 9 is the row's existing reading (fork T2) and was not re-verified here.

## 1. Source

The working text is the Hebrew Wikisource consolidation, revision 3085765, last edited 2026-09-30, deposited at `../../registers/source-bundle/real-estate-taxation-law-5723-1963.he.wiki.txt`.
Its sha256 is aa4217b3b917a48356d8069b9e9510694b456506ec77c9b4527a99c6c16dd1ca.
The consolidation is unofficial, so every figure is labelled CONSOLIDATION-ONLY unless this encoder read it on a page image of the Knesset's Sefer HaChukim PDF.
Pages read from the image (listed with their instruments in the header of `re42-published-figures.l4`): SH 5773 pp. 154-156 (the 2013 ladders), SH 5782 p. 460 (the first temporary ladder), SH 5785 pp. 150-152 (the 2025 freeze, with the exemption ceilings).
The 18-month reading (SH 5783 p. 161, s 10, Amendment 102) and the orphan date (SH 5783 p. 542, Amendment 103) were read from the page images by the lead of the session on 2026-11-10; the encoder looked at the Amendment 102 page and not at the Amendment 103 page.
The page of Amendment 85 (SH 2544, 6 April 2016, p. 694: the 24 months of s 49C(1) and the temporary 18 months of s 9(ג1ג)(2)(ב)) was read from the page image at 250 dpi on 2026-11-10, in the correction recorded above; SH 2405 p. 155, already deposited, was read for the 24 months of s 9(ג1ג)(2)(ב) as created.
A second reading of the sources, whose notes are not in this repository, supplied the instrument and page for the later amendments of s 9 (SH 5783 pp. 160-161, SH 5785 pp. 150-152) and for the Finance Committee's approval of the extension order of the temporary ladder, which is the Knesset's record of its meeting no. 511 of 9 December 2024, read as text and not as a page image.
Every instrument named here is deposited in `../../registers/source-bundle/` with its URL and sha256 in `SOURCES.json`: the Sefer HaChukim PDFs in `amending-laws/`, and the Committee's record in `official/`; the law firm's guide on the end date of the temporary ladder (https://www.siboni-law.com/PurchaseTaxGuide2026) is a third party's page and is not deposited.
Only the pages the row cites are deposited as PDFs, except SH 2544 p. 694 (Amendment 85), which is deposited as four cropped images of the lines read; `SOURCES.json` keeps the whole file's URL, sha256 and size as downloaded for provenance.
Every quotation of Hebrew in the modules is expanded mechanically from the deposit by `tools/srcquote.py`, and `tools/hebcheck.py` finds every run of Hebrew in the `.l4` files and in this file in the deposit (it exits 0 when run over `*.l4` and `NOTES.md`).

## 2. Scope

Two seats, money first.
The buyer's seat is an individual who buys a dwelling: purchase tax under s 9 and the advance on the seller's tax under s 15.
The seller's seat is an individual who sells a dwelling: the appreciation, the real appreciation and the inflationary amount (ss 6(b), 17(c), 21(a), 39, 47), the exemptions (ss 49 to 49F), and the tax (ss 48A, 48B).
A third reader, the company that buys, is served only through the ladders of s 9.

Out of scope, each with its reason:

- Sections 49יט to 49לו and 49לז to 49מג, and with them chapters 5-4 (evacuation and rebuilding), 5-5 (building rights under the strengthening plan) and 5-6 (moving a plant to a preferred area), by their headings in the deposit: a different seller and a different chapter from the dwelling sale, and each would need its own figures read from the amending laws.
- Sections 73 to 91 and 94 to 101 (declarations, assessment, appeals, penalties): procedure and sanctions, not the amount of tax; the penalty sections belong to a separate row.
- The regulations: not deposited for this row.
- Sections 22 to 36 (other ways the acquisition value is fixed: lease, gift, inheritance, exchange, expropriation) and s 17(b) and (d): the seller's record takes the value on the acquisition day as a stated fact.
- Section 49G (building rights): its five figures are held in the figures module, official, but no rule uses them, because the exemption turns on the Director's opinion of what influenced the price.
- Section 48A(b3), (b4), (d), (e) and 48A1, 48C: see the header of `re42-s48a-rates.l4`.
- The Income Tax Ordinance: its two rates are inputs (section 4).

## 3. Files

| file | what it holds |
| --- | --- |
| `re42-nouns.l4` | the facts a witness could state: people, dwellings, purchases, sales; no rule |
| `re42-published-figures.l4` | every amount and percentage with where it was read; dated ladders and the exemption ceilings |
| `re42-s9-purchase-tax.l4` | s 9: which ladder, who counts as one buyer, the only-dwelling routes, the tax |
| `re42-s15-advance.l4` | s 15: the buyer's advance and the payment it comes out of |
| `re42-s47-appreciation.l4` | the appreciation, the inflationary amount, the real appreciation and its splits |
| `re42-s49-exemptions.l4` | ss 49 to 49F: what part of the sale value is exempt |
| `re42-s48a-rates.l4` | ss 48A, 48B: the tax on the sale |
| `re42-cross-references.l4` | sixteen citations as typed pairs: what the citing words say, what the target is; all sixteen hold |
| `re42-seat-buyer.l4`, `re42-seat-seller.l4` | one-line `@export` wrappers; no assertions of their own |
| `re42-tests-*.l4` | the tests; no expected-red file is declared |

`re42-tests-seller.l4` was written by a generator script kept in the session scratchpad and not in the repository; the file itself is the artifact, and its inputs and readings of the text are set by hand, while the arithmetic of the expected values (day counts, products, sums) was computed in Python, independent of the L4, and is shown in the comment above each assertion.

## 4. Coverage

| provision | status |
| --- | --- |
| s 9 (purchase tax), every period | encoded; periods before 6 May 2013 are NOTHING for a ladder the sources do not give; the (ג1ה) window is NOTHING on the non-single route |
| s 15 (advance) | encoded except the time limits of (ה) and (ו), the refund in (ד)(3), and the effect on s 16 |
| ss 6(b), 17(c), 21(a), 47 | encoded for a sale by an individual for a consideration, with the expenses and index values the seller states |
| ss 22 to 36, 37 to 39A | the seller states the result; the two-thirds rule for the completion day of a new building (s 47) is not computed |
| ss 49 to 49F | encoded except 49B(5)(b) (a public body inheriting), 49F(c)(2) (spouses of different ages), 49G, 49G1 |
| ss 48A, 48B | encoded for an individual, with the Ordinance rates as inputs; see the header of `re42-s48a-rates.l4` |

## 5. The Ordinance is not encoded

Section 48A taxes real appreciation at the Ordinance's rate, at up to 25%, and s 48B treats the appreciation as the top step of the seller's income.
The seller states two numbers: the rate at which the Ordinance would tax the appreciation as the top step of their income, and the highest rate in its section 121.
The tests stipulate 47% and 50% (and 20% for one case); these are stipulated for the tests, not published figures, and nothing in the encoding holds an Ordinance rate.
The seller's other choice, spreading the appreciation over up to four tax years (s 48A(e)), only lowers the tax and depends on the seller's other income in each year, so the module answers the tax without the election.

## 6. Which figures are official and which are not

Read from the official page: the 2013 as-created ladders (amounts and percentages, SH 5773 pp. 155-156); the temporary ladder as first enacted (SH 5782 p. 460); every amount of the 2025 ladders (SH 5785 p. 151); the five amounts of ss 49A(a1), 49E and 49G (SH 5785 pp. 151-152).
CONSOLIDATION-ONLY: the percentages of the 2025 ladders; the single-dwelling ladders adjusted for 2022, 2023 and 2024 (an editor's table inside the consolidation); the transitional ladders of (ג1ב); the closed-period ladders (ג), (ג1), (ג1א); every rate and day of ss 48A and 47 (25%, 20%, 10%, 0%, the start, change and transition days); the extension of the temporary ladder to 31 December 2026 as to the date of its publication.
A date for which the sources give no figure answers NOTHING; it never gets the nearest vintage.

## 7. Answer table: purchase tax on a given price, by day

The seller's and the buyer's answers are MAYBE NUMBERs.
The rows below are read from the assertions in `re42-tests-s9.l4`, not typed from memory.
"Single dwelling" is an individual resident buyer with no other dwelling (the (ג1ג)(3) ladder); "company" is a buyer who is not an individual (the general ladder).

| buyer | price | day | tax | where read |
| --- | --- | --- | --- | --- |
| single dwelling | 2,000,000 | 6 May to 31 July 2013 | 22,366.35 | the transitional ladder, consolidation only |
| single dwelling | 2,000,000 | 1 August 2013 to 15 January 2014 | 22,366.35 | SH 5773 p. 156, official |
| single dwelling | 2,000,000 | 16 January 2014 to 15 January 2022 | NOTHING | no figure held |
| single dwelling | 2,000,000 | 16 January 2022 to 15 January 2023 | 6,805.925 | editor's table, consolidation only |
| single dwelling | 2,000,000 | 16 January 2023 to 15 January 2024 | 2,829.575 | editor's table, consolidation only |
| single dwelling | 2,000,000 | 16 January 2024 to 31 December 2024 | 743.925 | editor's table, consolidation only |
| single dwelling | 2,000,000 | 1 January 2025 to 15 January 2028 | 743.925 | amounts official, percentages consolidation only |
| single dwelling | 2,000,000 | from 16 January 2028 | NOTHING | the update that begins then is not held |
| company | 5,000,000 | 1 August 2013 to 15 January 2014 | 311,426.1 | SH 5773 p. 155, official |
| company | 5,000,000 | 16 January 2014 on (to 27 November 2021) | NOTHING | no figure held |
| company | 7,000,000 | 11 February 2027 | 440,817.5 | amounts official, percentages consolidation only |

For a single-dwelling purchase from 1 May 2016 to 30 April 2021 the time allowed to sell the former dwelling is 18 months (fork T3), but the table answers NOTHING for those days, so the window changes no amount here.

For 1 January to 10 February 2027 the answer depends on the reading of the end of the temporary ladder (fork T1): 440,817.5 on the general ladder if it ended on 31 December 2024 or 31 December 2026, and 578,898.6 on the temporary ladder if it was carried to 10 February 2027; the declined reading answers NOTHING there.

## 8. Fork register

Each fork gives the reading taken, the reading rejected, and where it is.

- T1, the end of the (ג1ו) period.
  Four readings are named inputs: the end printed in the Law (31 December 2024), the extension to 31 December 2026 (a note in the consolidation, Kovetz HaTakanot 5785 p. 626, and a draft order the Finance Committee approved on 9 December 2024, read as text from the Committee's record), the carrying of the end to 10 February 2027 through section 38 of Basic Law: The Knesset (a law firm's guide quoting a Tax Authority notice that was not read), and a fourth that declines to choose and answers only where all agree.
  No reading is taken; the signed order and the notice were not read.
  The fourth reading was added late, after a second reading of the sources; the tests for 1 January 2027 were revised then (disclosed in section 11).
- T2, the end of the 18-month reading (Amendment 102, s 10).
  Two years from 1 June 2023 is taken to end on 31 May 2025; no instrument extending it was found.
  The row reads the same 18 months into s 9(ג1ג)(2)(ב) and into s 49C(1) (the page of Amendment 102 names both; see `re42-published-figures.l4`); since the correction of 2026-11-10 each has its own function.
  The rejected reading is a window of 24 months throughout; the deposit prints 24 and mentions no reading.
- T3, the end of the temporary period of Amendment 85 and the first day of the 24-month window of s 49C(1).
  Section 5 of Amendment 85 runs for "five years from 23 Nisan 5776 (1 May 2016)"; section 6 starts the 24 months of s 49C(1) "at the end of" that period, for a dwelling bought "at the end of the period or later".
  Taken: the five years are counted as fork T2 counts two years from 1 June 2023, with the first day counted, so the period is 1 May 2016 to 30 April 2021; s 9(ג1ג)(2)(ב) reads 18 months for a purchase on any of those days, and s 49C(1) reads 24 months for a replacement bought from 1 May 2021, the day after the last day.
  Rejected, each moving only the purchase days 30 April 2021 and 1 May 2021: the Interpretation Law's rule for counting a period that runs "from" a day, if it leaves the first day out and ends the period on 1 May 2021 (the rule was not read, as for T2 and I1); "at the end of the period" read as the last day itself, so that a replacement bought on 30 April 2021 already has 24 months.
  The tests pair 30 April 2021 with 1 May 2021 for both sections and say that the pair depends on T3 (`re42-tests-s9.l4`, `re42-tests-seller.l4`); every other day tested is clear of the boundary.
- V1, V2, V3, the windows of the figures.
  V1: the frozen amounts of s 9 and s 49G hold to 15 January 2028, the 49A(a1) and 49E amounts to 31 December 2027, because the sections update on different days.
  V2: the closed-period ladders print one year's figures out of annually updated amounts, so they are encoded as printed for arithmetic and answer NOTHING by date.
  V3: the 2013 amounts hold from 1 August 2013 to 15 January 2014, the day before the first update.
- I1, the day of Amendment 103: its day is taken as the day of its publication, 13 July 2023 (the Interpretation Law's rule was not read); a child orphaned of a parent counts with the buyer only for a purchase before that day.
- A1, s 15(c): "or on the date of the declaration under s 73(c), whichever is later" is not modelled.
- F1, the inflationary amount is the part of the appreciation equal to the excess of the adjusted over the remaining acquisition value, so at most the appreciation; the rejected reading takes the whole excess and can give a negative real appreciation.
- F2, "periods" in s 47 are counted in days, as differences of day serial numbers; the Minister's rounding rules were not found and are not encoded.
- F3, a right acquired on or after 1 January 1994 has no chargeable inflationary amount (there is no 1993 sale of it to imagine), so that tax is 0; for a right acquired earlier the amount needs the index on 31 December 1993 and is NOTHING, except at the 0% rate.
- F4, for a right acquired on or after the start day, the part of the real appreciation up to the start day is 0.
- F5, the boundary of "the 18 months preceding the sale" in s 49B(2): a sale of another dwelling exactly 18 months back is allowed.
- F6, an association dwelling is judged by s 49D's own conditions, and the replacement presumption of s 49C is not applied to it.
- F7, the seller's option to leave months of education or religion out of the four-year period of the definition of a qualifying dwelling is not modelled.
- F8, ASSUMED, NOT READ: the present wording of s 48A governs a sale on or after 1 June 2023; earlier sales answer NOTHING.
  The amendments to s 48A were not read, so the commencement of its present wording is unknown to this encoding.
- F9, "within L months before the sale" is read as month numbers differing by less than L, or by L with the sale's day of the month no later than the purchase's; there is no clamp for a short month.
- Wording kinds kept here only: the citation of s 9(ג1ב)(2)(ב) to "(ג1א)(2)(ב) ו־(3)" is read as (ג1א)(2)(ב) and its paragraph (3) at deposit line 183, which is probably what it means and not a defect; the tax year of the 2025 freeze is not defined where it is used.

## 9. Expected red

None is declared: the number is 0 in `check.sh` and in `encoding.json`.
During this run a seventeenth citation, s 49E(a)(4) to "section 9(c)" for the definition of a dwelling, was kept as an expected-red assertion on the reading that s 9(c) holds only a ladder.
It was retracted the same day: s 9(c) closes with a block that defines "building" and "dwelling" (deposit lines 159 to 164), so the citation is correct and the assertion now passes in `re42-tests-xrefs.l4`.
The same block is the paragraph (2) that s 9(ג1א)(2)(ב)(3) and (ג1ג)(4)(ד) cite for a purchase group (line 163), so those citations are correct too.

## 10. Check numbers

Run as `L4=~/.local/bin/l4 L4_MAIN=~/.cache/l4-main/109/l4 ./check.sh`; main is build 1.6.109 (4c887e0, 2026-11-04).
Both binaries give the same four counts for every one of the 14 files.
The totals are 405 assertions satisfied, 0 failed, 0 refused and 0 errors (355 before the correction of 2026-11-10, which added 50; re-run on that day with `~/.local/bin/l4`, a working-tree build that prints "dev", against main 1.6.109).

| file | satisfied |
| --- | --- |
| `re42-tests-s9.l4` | 181 |
| `re42-tests-s15.l4` | 28 |
| `re42-tests-seller.l4` | 180 |
| `re42-tests-xrefs.l4` | 16 |

The check does not see a different trace outcome, or any difference that no assertion exercises.
Mutation control on the seller tests: four deliberate faults in copies of the modules (the 25% cap made 26%, the 18-month bound made 17, the day before the change day no longer subtracted, the 49A(a1) ceiling made 5,009,000) made 42 assertions fail, so those tests can fail.
An earlier control on the s 9 tests, six wrong expected values, each failed; it was run before the last context window of this session and is not repeated here.
A control on the correction of 2026-11-10 (the correction note above): the 50 new assertions against the old modules, 16 failed.

## 11. Departures and revisions

- `check.sh` and `fetch-main-l4.sh` come from the skill's assets, not from the sibling row il-34, whose `check.sh` has no main columns.
- Tests revised after new official evidence, not to fit code: the expectation for a 24-month sale after a purchase on 1 January 2025 (the Amendment 102 page showed 18); the expectation for a company buying on 1 August 2013 (NOTHING until the 2013 general ladder was read, then a figure); the expectations for 1 January 2027 under the declined reading (when the fourth reading was added).
- Correction of 2026-11-10 (EF-2): no existing assertion was changed; 50 were added, each expected value taken from Amendment 85 (SH 2544 p. 694), Amendment 102 or the 2013 text, none from the code.
- The seller's record `A sale of a dwelling` was changed while the seller modules were written (the gift facts, the one-off facts, the replacement dwelling's purchase day); no earlier test used it.

## 12. Open questions for a domain expert

- Is a seller who sold another dwelling free of tax exactly 18 months earlier barred (fork F5)?
- Does the 18-month reading of Amendment 102 reach s 49C(1) as it reaches s 9, and does a purchase on the last day of the window count (fork T2)?
- Does "five years from 1 May 2016" end on 30 April 2021, and does a dwelling bought on that last day have the 24 months of s 49C(1) or the 18 (fork T3)?
- What is the commencement of the present wording of s 48A (fork F8)?
- What does the signed order extending the temporary ladder say, and does section 38 of Basic Law: The Knesset carry its end to 10 February 2027 (fork T1)?
- Is the chargeable inflationary amount of a right acquired after 1993 zero (fork F3)?

## 13. Observations on the text (public tier)

Each point is about a date or a citation, not about an amount of tax in force.
READ means the lead of the session read the page image of the instrument named, on 2026-11-10; CONSOLIDATION-ONLY means only the Wikisource text was read.
No domain expert has read any of this.

- O1, the end date of s 49לו2 pairs a Hebrew year with a Gregorian date that do not match.
  The consolidation (deposit line 1174) prints "ט׳ בטבת התשצ״ג (31 בדצמבר 2033)", and the official text does the same: s 4(12) and s 6 of the Economic Efficiency Law, SH 3045 (31 May 2023) p. 159, print the same pair of words (READ, rendered at 300 dpi).
  9 Tevet 5793 is 11 December 2032, and 9 Tevet 5794 is 31 December 2033; the routine that computed them reproduced 1 Tishri 5786 = 23 September 2025, 25 Kislev 5785 = 26 December 2024 and 2 Sivan 5786 = 18 May 2026.
  The row does not encode s 49לו2 (out of scope, section 2), so no test depends on it; it is recorded because the two readings are a year apart.
- O2, s 37(1)(א) (deposit line 489, in the definition of "יום הרכישה") refers to the day fixed under s 19 or s 20 as the day of sale, and s 20 was repealed.
  Amendment 70, SH 2281 (15 March 2011) p. 403, s 2, reads "section 20 of the principal Law – repealed" (READ).
  Whether a later instrument touched the citing words of s 37(1)(א) was not read: the deposit's amendment tags for s 37 show none (CONSOLIDATION-ONLY).
  Effect found: none, because s 19 still fixes the day.
- O3, ss 39(4), 118 and 120(א) (deposit lines 519, 1792 and 1801) cite s 7(א), paragraphs (1) to (3) of s 7, and s 7(4) and (5), and s 7 is one sentence.
  Section 2 of the 1965 amendment, SH 442 (10 January 1965) p. 40, replaced s 7 by "the tax is imposed on an act in a land association", the sentence at deposit line 133 (READ).
  Whether a later instrument reprinted the citing words in ss 39(4), 118 and 120(א) was not read (CONSOLIDATION-ONLY).
  Effect found: none; the cited paragraphs are of a 1963 text that no longer exists.
- O4, s 48ב(ב)(4) (deposit line 695) refers to s 48א(ד1), and the consolidation's s 48א has no (ד1); the other subsection it names, s 48א1(א), is a closed temporary provision.
  A second reading searched seven staged instruments for a (ד1) and found none; no official text of s 48א as it stands was read (CONSOLIDATION-ONLY for both limbs).
  The row does not rely on s 48ב(ב)(4).
- O5, four places in the Law still cite s 72ח, which went with the repeal of the sales-tax chapter.
  Amendment 61, SH 2134 (18 February 2008) p. 203, s 5, reads "chapter 6-1 of the principal Law – repealed" (READ); the consolidation prints s 72ח as "(repealed)" (deposit line 1414), and ss 81, 89(ג), 95(א) and 98(א) still name it (deposit lines 1514, 1558, 1620 and 1661).
  The same page shows the Knesset removing sales-tax words from other sections: s 4 (s 49יד(א)), s 6 (s 78(1)), s 7 (s 94(א), including the words that cite s 72ט) and s 8 (s 94א(א)(3)); none of those sections of the Amendment touches ss 81, 89, 95 or 98 (p. 202 was not viewed by the lead).
  SH 2405 (5 August 2013) p. 161, s 43(18)(ב), deleted "לפי סעיף 72ח" from the definition of "גרעון" in s 95(ג) and left it in s 95(א) (READ); the consolidation still prints it in s 95(ג) (deposit line 1628), which is an error of the consolidation and not of the Law.
  Effect found: none, because the sales-tax declaration can no longer be breached and the first limb of the offence in s 98(א) still covers the duties that remain.
  The current text of the four sections is CONSOLIDATION-ONLY.
