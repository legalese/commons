# Notes: Courts Law [Consolidated Version], the provisions on the Judicial Selection Committee (row IL-38)

Version 0.1.0, draft.
Run `LEGALESE-2026-11-IL-38-20261109`, encoder a Sonnet 5.5 agent, 2026-11-09.
No domain expert has read this encoding against the source, and no independent tester has run.
Every Markdown sentence here is on its own line, so a grep hit is a whole sentence.

**Correction note, 2026-11-10 (two statements in this file were wrong; no rule, test or count in the encoding changes).**
Section 4 said the text of the Basic Law's s 7(4) is unamended; it is not (see the row for s 7(4) in section 4).
Section 6 said the consolidation's header lists no instrument after Sefer HaChukim 3389; it lists three (see the first bullet of the "not read" list in section 6).
Both were found by a hunter who compared this file's statements with the deposited source files and the official page images, and both were checked again against those files before this correction.
Neither changes a rule the encoding uses, as far as the pages read show: the pages read of the three later instruments (the whole of Amendments 106 and 107, and s 5 of the law at SH 3578 p.1055, see section 6) do not touch ss 2, 2A, 6, 6B, 6C, 7, 8, 14 or 25 of the Courts Law, and the amendment to s 7(4) of the Basic Law added a proposer to the provision under which s 14(a) of the Courts Law acts.

## 0. What is encoded, from whose seat, and against which text

**Scope.**
This row encodes **only** the provisions of the Courts Law that Amendment No. 105 (Sefer HaChukim 3389, 1 April 2025) touches, and two that it does not touch: s 2 (which s 6C(a) and s 25(b) cite) and s 14(b), (c) (the procedure for ending a term under s 7(4) of the Basic Law, which row IL-37 encodes).
**Every other section of the Courts Law is out of scope: not touched by the amendment and not needed by a provision it touches.**
The deposited consolidation of the Courts Law has 169 section headings (some repeated, for two vintages of one section); this row does not claim to have encoded the Law.
The indirect amendment of the Knesset Law (Amendment No. 105 s 7) is not encoded.

**The seat** is the individual the Courts Law's rules are applied to: a candidate for the Supreme Court, a person whom the Knesset might choose as a public representative on the committee, and a judge whose term the committee is asked to end.
The committee, the Minister of Justice, the Knesset and the Court have no seat.
Four questions are exported from the seat (`il38-seat.l4`): whether the person is eligible to be chosen a Supreme Court judge or a public representative (s 2, s 6C(a)); whether the person is past the 18-month cooling-off (s 2A(a)); whether the committee's choice of the person is valid at the person's age on the votes it got (s 2A(b)); and whether the committee followed the procedure of s 14(b) when it ended the person's term.

**Target compiler:** `main`, build 1.6.109 (4c887e0, 2026-11-04).

**The texts.**
The rules of ss 2A, 6, 6B, 6C, 7, 8 and 25 and the commencement and application section (s 8 of the amendment) were read from the page images of the Knesset's PDF of Sefer HaChukim 3389, pp. 438-440 (`registers/source-bundle/amending-laws/25_lsr_6165552.pdf`).
The Hebrew Wikisource consolidation (`registers/source-bundle/courts-law-consolidated-version-5744-1984.he.wiki.txt`) is an unofficial aid.
It shows the text before and after the 26th Knesset, each later text marked "(החל מיום תחילת כהונתה של הכנסת העשרים ושש)", and it is the source of the line numbers below, and of the text of s 2 and s 14, which the amendment does not touch.
Where the consolidation and the instrument differ, the instrument is what is encoded; no difference was found in this Law (section 3).

**Vintages** are an explicit input, `A vintage of the Courts Law text`: `the text before the 26th Knesset` and `the text from the 26th Knesset`.
They are never merged.
Amendment No. 105 s 8(a) starts the amendment on the day Basic Law: The Judiciary (Amendment No. 4) starts, the first day of the 26th Knesset's term; row IL-37 holds the vintage rule and the transitional window, and this row takes the vintage as an input.

**Modules** (imports run top to bottom):

| module | what it holds |
| --- | --- |
| `il38-nouns.l4` | `DECLARE` only: vintages, the candidate, who proposes, women on the committee, the typed cross-reference |
| `il38-rules.l4` | the rules of ss 2, 2A, 6, 6B, 6C, 7(b), 7(c), 8, 14, 25 |
| `il38-xrefs.l4` | 11 cross-references as typed values (citing says, target is) |
| `il38-seat.l4` | the four seat questions |
| `il38-tests-rules.l4` | 67 assertions on the rules |
| `il38-tests-xrefs.l4` | 15 assertions: each cross-reference agrees, the whole list, and a positive control |
| `il38-tests-seat.l4` | 10 assertions on the seat questions |

## 1. Coverage table

Dispositions: `encoded`; `inert` (a power, a label or a cited target with nothing to compute); `out-of-scope` (with a reason); `deferred` (not done in this run).
"Line" is the line of the deposited consolidation; "page" is the page of SH 3389.

| provision | line | disposition | where |
| --- | --- | --- | --- |
| s 2, who may be a Supreme Court judge (not touched by the amendment) | 62-69 | encoded | `the person is eligible to be a Supreme Court judge` (fork Z1) |
| s 2A (before): the 18-month cooling-off | 71-72 | encoded | `the cooling-off of 18 months is over` |
| s 2A(a), from the 26th Knesset: the same cooling-off | 75-76 | encoded | the same function (the text is the same in both vintages) |
| s 2A(b), from the 26th Knesset (p. 438): unanimity for a candidate under 55 | 77 | encoded | `the choice of a Supreme Court judge meets section 2A(b)` (forks A1, A2) |
| s 6, opening (the committee of Basic Law s 4) | 94 | inert | target of `xref s 6 to Basic Law s 4` |
| s 6(1), the Knesset elects two Knesset members, before and from the 26th Knesset | 95-96 | encoded | `the number of Knesset members the Knesset elects to the committee`, which is two in both vintages |
| s 6(2), who chooses the Bar's or the public representatives | 97-98 | inert | stated in comments; who chooses is not computed |
| s 6(3), the two justices serve three years | 99 | deferred | the terms of office were not encoded in this run |
| s 6(3A), (3B), the women on the committee, both vintages | 100-102 | encoded | `the gender requirement of section 6 is met` (fork G1) |
| s 6(4), the composition is published in Reshumot | 103 | out-of-scope | not touched by the amendment; nothing to compute |
| s 6, the two definitions "coalition factions", "opposition factions" (p. 438) | 104-106 | encoded | `the faction is one of the coalition factions`, `the faction is one of the opposition factions` |
| s 6A, a member votes on the member's own discretion | 108-109 | out-of-scope | not touched by the amendment |
| s 6B(a), members chosen on a new Government or a crossing of 80 | 113 | encoded | `members must be chosen in place of the ministers, Knesset members and public representatives` (fork B1) |
| s 6B(b), a change of the Knesset member's side | 114 | deferred | not encoded as a rule; cited by no row |
| s 6B(c)(1), two thirds of a side announce | 115 | encoded | `two thirds of that side announce` (fork B2) |
| s 6B(c)(2), a secession from a faction | 116 | inert | target of `xref s 6B(c)(2) to Knesset Law s 61` |
| s 6B(d), election within 30 days | 117 | encoded | `the election was held within 30 days of the ground` (fork B3) |
| s 6C(a), who may be a public representative | 121 | encoded | `the person is eligible to be chosen a public representative` |
| s 6C(b), Knesset Law s 6 applies | 122 | inert | target of `xref s 6C(b) to Knesset Law s 6` |
| s 6C(c), the Knesset's Rules for the order of election | 123 | inert | a power |
| s 6C(d), the Minister's regulations on pay and conflicts of interest | 124-126 | inert | a power; no regulation is deposited |
| s 7(a), the Minister announces and convenes | 129 | out-of-scope | not touched by the amendment |
| s 7(b), who may propose candidates, before and from the 26th Knesset (p. 439) | 130-134 | encoded | `the proposal of a candidate is by someone the text allows` (fork P1) |
| s 7(c), the old majority, before the 26th Knesset only (repealed from it) | 135-137 | encoded | `the old majority of section 7(c) is met`, which is NOTHING from the 26th Knesset (fork O1) |
| s 7(d), the committee sets its other procedures; the Rules published under s 7 | 138-141 | out-of-scope | not touched by the amendment; the Rules were not read |
| s 7A, no proposal of a judge convicted of an offence involving disgrace | 143-144 | out-of-scope | not touched by the amendment |
| s 8(a), the President and Deputy President of the Supreme Court are appointed under Basic Law s 4(a) (and (d) from the 26th Knesset) | 147-148 | encoded | `the provisions of the Basic Law that appoint the President and the Deputy` |
| s 8(b), seven years and no second term | 149 | encoded | `the term of the President or Deputy has run`, `the person may be appointed to that post again` |
| s 14(a), a sub-committee may be appointed | 198 | inert | target of `xref s 14(a) to Basic Law s 7(4)` |
| s 14(b), the judge may read the material and be heard | 199 | encoded | `the committee followed section 14(b)` |
| s 14(c), the pension fixed by the committee has a ceiling | 200 | encoded | `the pension fixed is within section 14(c)` |
| s 25(a), the number of Supreme Court judges is set by the Knesset | 324 | inert | a power; the number is an input to the next row |
| s 25(b), two thirds of the Supreme Court judges served on a district court, from the 26th Knesset (p. 439) | 325 | encoded | `two thirds of the Supreme Court are former district court judges` |
| Amendment No. 105 s 8, commencement and application (p. 440) | not in the consolidation | encoded | s 8(a): see "Vintages" above; s 8(b): the saving in `the choice of a Supreme Court judge meets section 2A(b)` |
| every other section of the Law | | out-of-scope | not touched by Amendment No. 105 and not needed by a provision it touches |

"Out-of-scope" means only that no assertion in this row covers the provision; it is a statement about this run and not about the provision.

## 2. Fork register

A fork is an ambiguity in the source or in the modelling.
Each row gives the reading taken, the reading rejected, and what would settle it.
Every row is assumed, not ruled; no domain expert has chosen between the readings.
Fork rows marked "Interpretation Law" or "the regulations" depend on texts that were not read.

| id | the question | reading taken | reading rejected | what would settle it |
| --- | --- | --- | --- | --- |
| Z1 | s 2(2): "at least ten years, at least five of them in Israel, in one or more of" counsel, a judicial or other legal post in the State's service or another service the regulations set, or teaching law at a university or law school the regulations set | one input, the years in any of the capacities, with a second input for the years in Israel; the capacities are not modelled one by one | each capacity is a separate input | the regulations (not read) |
| A1 | s 2A(a): "eighteen months from the day the term ended" | the caller states the whole months since the term ended; eighteen or more ends the cooling-off | the count is made from the dates by the encoder | the Interpretation Law (not read) |
| A2 | s 2A(b): "who has not yet reached 55" (שטרם מלאו לו 55 שנים) | age in whole years below 55 needs the consent of every member serving; 55 or above does not | age below 55 years and some days | a court's reading |
| B1 | s 6B(a): "if the number of Knesset members of the coalition factions fell to 80 or below, or rose above 80" | a crossing from above 80 to 80 or below, or from 80 or below to above 80, or a new Government | a change of any size | a court's reading |
| B2 | s 6B(c)(1): "two thirds of the Knesset members counted among the coalition factions or the opposition factions" | at least two thirds of that side (three times the announcing members at least twice the side's members) | more than two thirds | a court's reading |
| B3 | s 6B(d): "within 30 days of the day the ground arose" | the election is held on or before the thirtieth day after the ground arose | before the thirtieth day | the Interpretation Law (not read) |
| P1 | s 7(b): "three members of the committee as one" before; "two members" from the 26th Knesset | at least three (before), at least two (from); the Minister of Justice and the President of the Supreme Court may always propose | exactly three, exactly two | a court's reading |
| O1 | s 7(c)(2), before: "seven of the members of the committee; if the participants number fewer than nine, a majority of the participants that is not less than the number of participants less two" | with nine participants, at least seven in favour; with fewer, more than half of the participants and at least the number of participants less two, both required; other judges (s 7(c)(1)): more than half of the participants | the two limbs are alternatives | a court's reading |
| G1 | s 6(3A), (3B): the women on the committee | counts of women by group, the groups the text names; under s 4(f) of the Basic Law (more than 80), s 6(3B) does not apply and at least one public representative whom the Knesset chose is a woman | the group lists are derived from the seats | a court's reading |

## 3. Where the consolidation and the instrument differ

The text of every provision this row encodes from the instrument (ss 2A, 6, 6B, 6C, 7(b), 7(c), 8(a), 25(b)) was compared by eye with the page images of SH 3389 pp. 438-440 and matched the consolidation.
That is a statement about the lines compared, not a guarantee.
Amendment No. 105 s 8 (commencement and application) is not in the consolidation; that is ordinary for an unofficial consolidation, and the section is encoded from the instrument.

## 4. How the tests were written

Every expected value was worked by hand from the Hebrew of the instrument (or, for ss 2 and 14, of the consolidation) before it was asserted, never copied from the code's output.
No assertion is expected to fail.

**Cross-references** are typed values: for each, what the citing text says it points at and what the target says it is, with a test that the two agree.
The 11 are split by where the target was read from:

| target | count | where the target was read |
| --- | --- | --- |
| this Basic Law's s 4, s 4(b)(1)(b) to (d), s 4(d), s 4(f) (twice) | 5 | the instrument SH 3388 p. 434 (row IL-37) |
| this Basic Law's s 4(a), s 7(4) | 2 | the consolidation, CONSOLIDATION-ONLY, with this correction (2026-11-10): s 7(4) was amended by Basic Law: The Judiciary (Amendment No. 2), Sefer HaChukim 1864, 5 August 2002, p. 598, s 1, which replaces "the chairman of the committee" by "the chairman of the committee, the Judges' Ombudsman" (read from the page image), so the text is not unamended and only the words the instruction does not change are the consolidation's; the instructions on SH 3388 p. 434 (Amendment No. 4) open with s 4(b) and do not mention s 4(a) (page image, p. 434 only; the following page was not re-read for this correction) |
| the Knesset Law ss 6, 61 | 2 | the Wikisource consolidation of the Knesset Law, an aid; CONSOLIDATION-ONLY |
| the Courts Law's own s 2, s 2(1) | 2 | the consolidation (the text is unamended); CONSOLIDATION-ONLY |

The citing text of ten of the 11 was read from the instrument; the citing text of `xref s 14(a) to Basic Law s 7(4)` is in a section the amendment did not touch, and was read from the consolidation.
`il38-tests-xrefs.l4` carries a positive control: a pair that does not agree is asserted not to agree, so the check can fail.

## 5. Check numbers

`check.sh` with `L4=l4` and `L4_MAIN=~/.cache/l4-main/109/l4`, `JL4_LIBRARY_PATH` unset, run on 2026-11-09.
The `l4` is `~/.local/bin/l4`, which resolves to the cabal store build jl4-0.1-177906e7 (`--version` prints `dev`), sha256 `2e47661700d89bf98abc2af3fd91fee5f6dee000c20704246c9369a54b53f302`.
The main build is 1.6.109 (4c887e0, 2026-11-04), sha256 `eeb12f1e9d0ec646b6196d53a4b83c41160ada7f3959211aa50b0115652b73cb`.
The numbers below were read from the diagnostics of that run; a repeat run from 14:35:52Z to 14:36:07Z exited 0, and its numbers were not re-read.

| module | errors | satisfied | failed | refused | main errors | main satisfied | main failed | main refused | main |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| il38-nouns.l4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | same |
| il38-rules.l4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | same |
| il38-seat.l4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | same |
| il38-tests-rules.l4 | 0 | 67 | 0 | 0 | 0 | 67 | 0 | 0 | same |
| il38-tests-seat.l4 | 0 | 10 | 0 | 0 | 0 | 10 | 0 | 0 | same |
| il38-tests-xrefs.l4 | 0 | 15 | 0 | 0 | 0 | 15 | 0 | 0 | same |
| il38-xrefs.l4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | same |
| TOTAL (7 modules) | 0 | 92 | 0 | 0 | 0 | 92 | 0 | 0 | |

`expected_red` is empty: no assertion is expected to fail.
The modules without assertions show 0 satisfied because they define rules and values and assert nothing.
The numbers do not see a different `#TRACE` outcome; this row has no `#TRACE`.

**Mutation check**, on scratch copies and never on the repository: in a copy of `il38-rules.l4`, `AT LEAST 18` was changed to `AT LEAST 17`, the two-member proposal threshold to three, the cooling-off's `OR` to `AND`, and `LESS THAN 55` to `LESS THAN 56`.
Failing assertions in the copy: 4 in `il38-tests-rules.l4` and 2 in `il38-tests-seat.l4`.
This shows the tests can fail; it does not show that every rule is tested.

## 6. What was not read

- The regulations s 2(2)(b), (c) refer to (the services and the schools that count), and the Knesset's Rules that s 6B(d) and s 6C(c) refer to: not read.
- The Judicature Rules on the committee's procedure, and the Interpretation Law, 5741-1981: not read.
- The Knesset Law, apart from the headings of ss 6 and 61 as targets of cross-references, read in a Wikisource consolidation (an aid): not read as a source of rules.
- Any amending instrument after Sefer HaChukim 3389: the consolidation's header lists three (corrected 2026-11-10; the first version of this line said none): Amendment No. 106 (Sefer HaChukim 3464, 3 December 2025, p. 32: s 70(b), a new s 70(b1), s 70D(a)(2)), Amendment No. 107 (Sefer HaChukim 3535, 10 June 2026, p. 622: a new s 24A, in force from 1 September 2026) and the law at Sefer HaChukim 3578, 29 July 2026, p. 1055 (s 5 there: ss 68(b)(4) and 70(d)).
  The page images of the first two instruments (each of them the whole of the instrument) and of s 5 of the third (p. 1055, the only section of that law that the hunter found to amend the Courts Law; its other pages were not re-read for this correction) were read for this correction: none touches ss 2, 2A, 6, 6B, 6C, 7, 8, 14 or 25, the sections this row encodes.
  The Knesset's database was not searched for an instrument later than the header's last entry.
- The Knesset's committee protocols and the explanatory notes to the bill that became Amendment No. 105: not read.

## 7. Re-running

`./check.sh` in this directory, with `l4` on `PATH` and `JL4_LIBRARY_PATH` unset.
`check.sh` and `fetch-main-l4.sh` are copied unchanged (`cmp` identical) from `subjects/il/income-support-law-5741-1980/encodings/legalese-sonnet-5.5/`, not from IL-34 as the brief named: IL-34's `check.sh` is an older version with no main-build columns and IL-34 has no `fetch-main-l4.sh`, and the brief asked for the main columns.
`il38-*.l4` import one another and `prelude` and `daydate`; they need no network.
