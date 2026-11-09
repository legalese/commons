# Notes: Basic Law: The Judiciary, the Judicial Selection Committee (row IL-37)

Version 0.1.0, draft.
Run `LEGALESE-2026-11-IL-37-20261109`, encoder a Sonnet 5.5 agent, 2026-11-09.
No domain expert has read this encoding against the source, and no independent tester has run.
Every Markdown sentence here is on its own line, so a grep hit is a whole sentence.

## 0. What is encoded, from whose seat, and against which text

**The seat** is the individual the committee's rules are applied to: a candidate whom the committee chooses or declines to choose as a judge, and a judge whom the committee is asked to remove (s 7(4)).
The committee, the Minister of Justice, the Knesset and the Court have no seat; they appear only as what they do to that person.
Two questions are exported from the seat (`il37-seat.l4`): whether the committee's choice of the person was valid on the votes it got, and whether the committee can end the person's term on the votes it got.
Neither question asks whether s 4B or the transitional window of Amendment No. 4 s 3 barred an election on that day; those are separate rules (`section 4B bars the election of judges on`, `the committee may elect judges in this vintage`) that the seat questions do not call.
The first question assumes all nine seats are filled and voting; it takes one yes-or-no per seat.

**Target compiler:** `main`, build 1.6.109 (4c887e0, 2026-11-04).

**The texts.**
The rules of s 4(b) to (f), s 4A, s 4B and the commencement and application section (s 3) of Amendment No. 4 were read from the page images of the Knesset's PDF of Sefer HaChukim 3388, 1 April 2025, pp. 434-436 (`registers/source-bundle/amending-laws/25_lsr_6165425.pdf`).
The PDF's text layer on p. 434 is scrambled, so no mechanical comparison with the consolidation was possible; every line was compared by eye with the page image.
The Hebrew Wikisource consolidation (`registers/source-bundle/basic-law-the-judiciary-5744-1984.he.wiki.txt`) is an unofficial aid.
It shows the text before and after the 26th Knesset side by side, each later text marked "(החל מיום תחילת כהונתה של הכנסת העשרים ושש)", and it is the source of the line numbers below.
Where the consolidation and the instrument differ, the instrument is what is encoded (section 3).

**Vintages are explicit inputs and are never merged:** `the text before the 26th Knesset`, `the transitional window of Amendment No. 4 section 3`, `the text from the 26th Knesset`.
The day the 26th Knesset's term begins and the day a committee is set up under the new text are inputs the caller states (`the vintage that applies on`).

**Modules** (imports run top to bottom):

| module | what it holds |
| --- | --- |
| `il37-nouns.l4` | `DECLARE` only: seats, vintages, kinds of decision, days, the typed cross-reference |
| `il37-committee.l4` | the rules of s 4(b) to (f), 4A, 4B, 7(4), 5 and Amendment No. 4 s 3 |
| `il37-xrefs.l4` | 22 cross-references as typed values (citing says, target is) |
| `il37-seat.l4` | the two seat questions |
| `il37-tests-composition-and-majority.l4` | 47 assertions: seats, paragraphs, counting, the majorities of s 4(d), (e), (f) |
| `il37-tests-time-rules.l4` | 47 assertions: quorum, vintages, s 4B, s 4A, s 7(4), s 5 |
| `il37-tests-xrefs.l4` | 26 assertions: each cross-reference agrees, the whole list, and a positive control |
| `il37-tests-seat.l4` | 12 assertions: the seat questions |

## 1. Coverage table

Dispositions: `encoded`; `inert` (a power, a label or a cited target with nothing to compute); `out-of-scope` (with a reason); `deferred` (not done in this run).
"Line" is the line of the deposited consolidation; "page" is the page of SH 3388.

| provision | line | disposition | where |
| --- | --- | --- | --- |
| ss 1 to 3 (jurisdiction, independence, open court) | 20-37 | out-of-scope | not touched by Amendment No. 4 and not about the committee |
| s 4(a), the President appoints on the committee's election | 42 | inert | the target of two cross-references (`xref 4A(c) to 4(a)`, `xref 4A(d)(2) to 4(a)`) |
| s 4(b), who sits, before the 26th Knesset | 43 | encoded | `the seats before the 26th Knesset` |
| s 4(b)(1), who sits, from the 26th Knesset (p. 434) | 45-49 | encoded | `the seats of the committee` (with the more-than-80 case) |
| s 4(b)(2), the Minister of Justice chairs | 50 | encoded | `the seat chairs the committee` |
| s 4(c), the committee may act with seven (both vintages) | 51 | encoded | `the committee may act with this many members` |
| s 4(c), the quorum of five (instrument only, p. 434) | not in the consolidation | encoded | `a meeting of the committee has a quorum` (section 3) |
| s 4(d), the ordinary majority | 52-55 | encoded | `the ordinary majority of section 4(d)`, `the paragraph of section 4(d) that a seat is in` |
| s 4(d), last words (a law may set a greater majority) | 56 | inert | stated, not encoded (fork D1) |
| s 4(e), the Supreme Court majority | 57 | encoded | `the majority of section 4 is met`, kind `the election of a judge of the Supreme Court` |
| s 4(f)(1), three from different factions, two of them consent | 59 | encoded | `the composition meets section 4(f)(1)`, `the number in favour from the three of section 4(f)(1)` (fork F1) |
| s 4(f)(2), the Knesset chooses both public representatives | 60 | encoded | `the seats of the committee`; fork D2 |
| s 4(f)(3), the opposition Knesset member's consent not needed | 61 | encoded | inside `the majority of section 4 is met` (fork F1) |
| s 4A(a)(1), (2), the Minister may decide once per Knesset | 65-66 | encoded | `the Minister of Justice may decide that section 4A applies` (forks Y1, Y2) |
| s 4A(b), the two proposals of three and the choice by the others | 67-69 | deferred | not encoded as a rule in this run; the two cross-references into s 4(d) are typed |
| s 4A(c), the chosen candidates are appointed together | 70 | inert | target of `xref 4A(c) to 4(a)` |
| s 4A(d)(1), the proposers may choose after a month | 71 | encoded | `the proposers may choose from their own candidates` (fork M1) |
| s 4A(d)(2), one side proposes and the other does not | 72 | deferred | target of `xref 4A(d)(2) to 4(a)` only; no rule computed |
| s 4B, opening and (1) to (4), the periods with no election of judges | 76-80 | encoded | `section 4B bars the election of judges on` (forks E1, E2); 11 cross-references typed (into Basic Law: The Knesset and Basic Law: The Government) |
| s 4B, after the colon, other decisions with all members serving | 76 | encoded | `all the members serving consent` (fork T1) |
| Amendment No. 4 s 3, commencement and the transitional window (p. 436) | not in the consolidation | encoded | `the vintage that applies on`, `the committee may elect judges in this vintage` (fork V1) |
| s 5, citizenship | 83 | encoded | `the person may be appointed a judge, as to citizenship` |
| s 6, the oath | 85-87 | out-of-scope | not touched by Amendment No. 4 and not about the committee |
| s 7(1) to (3), (5), ways a term ends | 90-95 | out-of-scope | not about the committee |
| s 7(4), the committee ends a term by seven members | 94 | encoded | `the committee's decision ends the judge's term` |
| ss 8 to 14 | 97-124 | out-of-scope | not touched by Amendment No. 4 and not about the committee |
| s 15 (the Supreme Court), as amended by Amendment No. 3 of 2023 | 128-139 | out-of-scope | a different amendment (Amendment No. 3 of 2023); not read and not encoded in this run |
| ss 16 to 24 | 140-193 | out-of-scope | not touched by Amendment No. 4 and not about the committee |

"Out-of-scope" means only that no assertion in this row covers the provision; it is a statement about this run and not about the provision.

## 2. Fork register

A fork is an ambiguity in the source or in the modelling.
Each row gives the reading taken, the reading rejected, and what would settle it.
Every row is assumed, not ruled; no domain expert has chosen between the readings.
The two rows marked "Interpretation Law" depend on a statute that was not read.

| id | the question | reading taken | reading rejected | what would settle it |
| --- | --- | --- | --- | --- |
| E1 | s 4B: "until members are chosen in place of ..." (ועד שייבחרו): does the bar apply on the day they are chosen? | the bar runs through the day before; on the day members are chosen it no longer applies | the bar includes the day members are chosen | a court's reading, or the Knesset's practice; tested at `il37-tests-time-rules.l4` (19 and 20 November 2026) |
| E2 | s 4B(1): "from the 90th day before the election day"; s 4B(2) to (4): "from the day" | the day named is the first day of the bar (election day minus 90, counting back; the grounds' own day) | the bar starts the day after | the Interpretation Law (not read) |
| Y1 | s 4A(a)(1): "a year has passed" (וחלפה שנה) from the later of two days | a year has passed on the same calendar day a year later | a year passes only at the end of that day | the Interpretation Law (not read) |
| Y2 | s 4A(a)(1): the vote after the year | the vote must be on or after that day | a vote before it also qualifies | the text reads "after that year the committee convened for the purpose and in a vote held in it no judge was elected" |
| M1 | s 4A(d)(1): "a month has passed" (חלף חודש) | the same day of the next month; a proposal on the 29th to 31st is not covered (the arithmetic overflows: 31 January 2028 gives 2 March 2028, and 29 February 2028 plus a year gives 1 March 2029, measured with `l4 run` on the module's own functions, 2026-11-09) | the last day of the shorter month | the Interpretation Law (not read); an untested edge, flagged and not blessed |
| T1 | s 4B, s 7(4), Amendment No. 4 s 3: "the consent of all the members serving" | a tally lists every member serving; one who is absent or does not vote in favour is in the list as not in favour, so one such member defeats "all" | a tally lists only the members present | a court's reading |
| D1 | s 4(d), last words: "or if a greater majority is set by law" | not encoded: only the Basic Law's own majorities are computed | a law that sets a greater majority is joined here | the list of such laws; none is encoded in this row |
| D2 | s 4(f)(2) with s 4(d): a public representative whom the Knesset as a whole chose is named in none of paragraphs (1) to (3) | such a member counts toward the five votes and toward no paragraph | such a member is placed in paragraph (2) or (3) | a court's reading |
| F1 | s 4(f): with more than 80 coalition Knesset members, what replaces the paragraph requirements of s 4(d), (e)? | an ordinary decision needs five votes, one judge, and two of the three of s 4(f)(1); a Supreme Court choice needs five votes and two of the three; the opposition Knesset member's consent is not needed (s 4(f)(3)) | the paragraph (2) and (3) requirements of s 4(d), (e) survive alongside | the words "with these changes" (בשינויים אלה); a court's reading |
| C1 | s 4(f)(1): "each from a different faction" | an input fact the caller states (`the three are each from a different faction`), as the text states it | the encoding derives it from faction membership | the faction lists, which this row does not model |
| Q1 | s 4(c): "may act as long as not fewer than seven" and the quorum of five | two separate functions, each as the text states it, not combined | one rule for both | a court's reading |
| V1 | Amendment No. 4 s 3: the window | from the first day of the 26th Knesset's term until a committee is set up under the new text; both days are inputs the caller states; with no set-up day stated, the transitional text applies | the encoder supplies a day | the caller's own facts |

## 3. Where the consolidation and the instrument differ

**s 4(c), the quorum.**
The instrument (SH 3388 p. 434, s 1(2)) adds at the end of s 4(c): "והמניין החוקי בישיבותיה הוא חמישה חברים" (the legal quorum at its meetings is five members).
The deposited consolidation's s 4(c) (line 51) reads only: "הועדה רשאית לפעול אף אם פחת מספר חבריה, כל עוד לא פחת משבעה", and omits that sentence.
This is a defect of the consolidation, not of the Law, and the encoding follows the instrument (`a meeting of the committee has a quorum`).
Verification: read from the page image of p. 434; compared by eye; no mechanical comparison was possible (scrambled text layer).

**s 3 of Amendment No. 4** (commencement and application, p. 436) is not in the consolidation at all.
That is ordinary for an unofficial consolidation; it is recorded so that a reader does not look for it there.
It is encoded from the instrument (fork V1).

The rest of s 4, s 4A and s 4B were compared with the page images by eye and matched.
No other difference was found; that is a statement about the lines compared, not a guarantee.

## 4. How the tests were written

Every expected value was worked by hand from the Hebrew of the instrument before it was asserted, never copied from the code's output.
Every date in a test is a hypothetical fixture chosen so that the answer can be counted by hand; none is a date the Law or the Knesset has fixed.

**A fixture error, found and corrected during the run, and disclosed here and not hidden.**
Several tallies in `il37-tests-composition-and-majority.l4` that the comments called "five votes" or "four votes" were built with fewer `TRUE` values than the comment said, so some assertions failed.
The expected values had been worked from the text first, so I corrected the tallies and left the expected values unchanged.
That was a transcription error in the fixture, not a finding about the Law.

**Cross-references** are typed values: for each, what the citing text says it points at and what the target says it is, with a test that the two agree.
The 11 references from s 4B into Basic Law: The Knesset and Basic Law: The Government have as target the Wikisource consolidations of those laws, which are aids and unofficial; those 11 are CONSOLIDATION-ONLY on the target side.
The other 11 point into this Basic Law's own text: 9 of them (into s 4(b)(1)(b) to (d), s 4(d), s 4(d)(2), s 4(d)(3), s 4(e) and s 4(b)(1)(d)) were read from the instrument, and 2 (`xref 4A(c) to 4(a)` and `xref 4A(d)(2) to 4(a)`) point at s 4(a), which the amendment did not touch, so their target side is CONSOLIDATION-ONLY too.
`il37-tests-xrefs.l4` carries a positive control: a pair that does not agree is asserted not to agree, so the check can fail.

## 5. Check numbers

`check.sh` with `L4=l4` and `L4_MAIN=~/.cache/l4-main/109/l4`, `JL4_LIBRARY_PATH` unset, run on 2026-11-09.
The `l4` is `~/.local/bin/l4`, which resolves to the cabal store build jl4-0.1-177906e7 (`--version` prints `dev`), sha256 `2e47661700d89bf98abc2af3fd91fee5f6dee000c20704246c9369a54b53f302`.
The main build is 1.6.109 (4c887e0, 2026-11-04), sha256 `eeb12f1e9d0ec646b6196d53a4b83c41160ada7f3959211aa50b0115652b73cb`.
The numbers below were read from the diagnostics of that run; a repeat run from 14:35:52Z to 14:36:07Z exited 0, and its numbers were not re-read.

| module | errors | satisfied | failed | refused | main errors | main satisfied | main failed | main refused | main |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| il37-committee.l4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | same |
| il37-nouns.l4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | same |
| il37-seat.l4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | same |
| il37-tests-composition-and-majority.l4 | 0 | 47 | 0 | 0 | 0 | 47 | 0 | 0 | same |
| il37-tests-seat.l4 | 0 | 12 | 0 | 0 | 0 | 12 | 0 | 0 | same |
| il37-tests-time-rules.l4 | 0 | 47 | 0 | 0 | 0 | 47 | 0 | 0 | same |
| il37-tests-xrefs.l4 | 0 | 26 | 0 | 0 | 0 | 26 | 0 | 0 | same |
| il37-xrefs.l4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | same |
| TOTAL (8 modules) | 0 | 132 | 0 | 0 | 0 | 132 | 0 | 0 | |

`expected_red` is empty: no assertion is expected to fail.
The modules without assertions show 0 satisfied because they define rules and values and assert nothing.
The numbers do not see a different `#TRACE` outcome; this row has no `#TRACE`.

**Mutation check**, on scratch copies and never on the repository: in a copy of `il37-committee.l4`, every `AT LEAST 5` was changed to `AT LEAST 4`, every `AT LEAST 7` to `AT LEAST 6`, and every `AT LEAST 1` to `AT LEAST 0`.
Failing assertions in the copy: 22 in `il37-tests-composition-and-majority.l4`, 6 in `il37-tests-time-rules.l4`, 4 in `il37-tests-seat.l4`.
This shows the tests can fail; it does not show that every rule is tested.

## 6. What was not read

- The Knesset Rules, which s 4(b)(1)(c), (d) refer to for how the Knesset members and public representatives are chosen: not read, and not modelled.
- The Judicature Rules on the committee's procedure (כללי השפיטה), and the Interpretation Law, 5741-1981: not read.
- Any amending instrument after Sefer HaChukim 3389: the consolidation's header lists none, but the Knesset's database was not searched for a later one.
- The Knesset's committee protocols and the explanatory notes to Knesset bill 947: not read.
- Amendment No. 3 of 2023 (s 15) and the Court's judgment in HCJ 5658/23: not read.
- The two sister Basic Laws that s 4B cites are deposited as aids only (`registers/source-bundle/aids/`), as Wikisource consolidations.

## 7. Re-running

`./check.sh` in this directory, with `l4` on `PATH` and `JL4_LIBRARY_PATH` unset.
`check.sh` and `fetch-main-l4.sh` are copied unchanged (`cmp` identical) from `subjects/il/income-support-law-5741-1980/encodings/legalese-sonnet-5.5/`, not from IL-34 as the brief named: IL-34's `check.sh` is an older version with no main-build columns and IL-34 has no `fetch-main-l4.sh`, and the brief asked for the main columns.
`il37-*.l4` import one another and `prelude` and `daydate`; they need no network.
