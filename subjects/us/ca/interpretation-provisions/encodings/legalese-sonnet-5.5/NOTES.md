# NOTES: California interpretation provisions, row `legalese-sonnet-5.5`

**Status: draft, version 0.2.1.**
No domain expert has read this encoding against the statute.
Pass 1 (version 0.1.0, 2026-10-22) was written by one Sonnet 5.5 agent working alone from a brief; pass 2 (version 0.2.0, 2026-10-29) was written by another Sonnet 5.5 agent working alone from a second brief, to take the row to "whole" (every section, subdivision, list item and defined term has exactly one disposition).
Step 8 of the skill, the independent test pass, was then run on 2026-10-29 by a test author who worked from the text alone and was told not to open NOTES or PROGRESS: 665 scenarios written first, 76 of which the encoding had no function for (gaps), and `tests-independent.l4` for the rest.
That file is in the row's review folder, not in this deposit.
This version (0.2.1, the same day) is the encoder's repair after that pass: one defect fixed, the gaps that were rules of the text answered by new functions, and the register and this file corrected (see "Changes to existing modules" and "Findings" 21-24).
Run in a scratch copy against this deposit, the reconciled `tests-independent.l4` (625 assertions) gives 625 satisfied, 0 failed and 0 refused; S487, the one disagreement the encoder kept (F-9605b), is asserted `REFUSED` in it, with the test author's expectation quoted above (see "Independent test pass" at the end of the file).

**The source text.**
The six `.txt` files this encoding was written from are a converter-made plain-text rendering of California Legislative Information (the Legislature's bulk file), not the official text.
Nothing here was checked against the official text.
Every quotation in the modules (`-- src:ID:N | text` lines) was copied by script from those files and checked against them by `srcrefs.py check --refs` (`srcrefs.py` is in this folder; it is the tool of the encoding skill, documented in its `references/source-locators.md`), which reports 0 problems for each of the twelve modules (measured 2026-10-29, command and numbers under "What `check.sh` prints").
That proves the quotation is the deposited text; it does not prove the deposited text is the law.
The terms of the source are in `SOURCE-LICENSE.md`.

**How this file is organised.**
"What is encoded" says what each module answers.
"Re-disposition audit" says what pass 2 changed and why.
"Coverage table" has one row per unit of the text.
"Fork register" has one entry per place the text allows more than one reading or says nothing.
"Jural relations" and "Changes to existing modules" are the two sections the second brief added; the latter records the repair after the independent test pass.
"Findings" are numbered.
"What `check.sh` prints" and "What to do before relying on this encoding" close the file.

## What is encoded

**Scope.**
California has no single interpretation act; Gov. Code § 9603 says the general rules of construction are in the preliminary provisions of the different codes.
The deposit therefore holds six files, 159 sections: Gov. Code §§ 1-26, Civ. Code §§ 1-23.6, Code Civ. Proc. §§ 1-34, Gov. Code §§ 6700-6736 (holidays), §§ 6800-6808 (computation of time) and §§ 9600-9612 (operation of statutes and resolutions).
The coverage table has a row for every unit of those sections and for the seven numbers the ranges skip.
No unit is left out: `scope.not_encoded` in `encoding.json` is absent because nothing is excluded.
What the text does not answer is not "not encoded"; it is a named `REFUSE` in the module, an entry of the fork register, or a question under "Open questions for a domain expert".

**The modules.**
The section lists are generated from the coverage table: a section is listed against a module when its row names that module (a section whose functions are in two modules is listed against both).

| Module | Pass | Sections whose coverage-table row names it | What it answers |
|---|---|---|---|
| `usca-interpretation-time.l4` | pass 1 | Gov. Code §§ 6700, 6706, 6707, 6800, 6801, 6802, 6803, 6804, 6805, 6806, 6807, 6808, 9600, 9602; Civ. Code §§ 2, 7, 10, 11, 14; Code Civ. Proc. §§ 2, 10, 12, 12a, 12c, 13, 13a, 13b, 17 | commencement, counting a period, the last day on a holiday, the time words, daylight saving time |
| `usca-holidays.l4` | pass 1 | Gov. Code §§ 6700, 6701, 6702, 6703, 6704, 6705; Civ. Code §§ 7, 7.1, 9; Code Civ. Proc. §§ 10, 12b | which days are holidays, under each code's meaning |
| `usca-operation-of-statutes.l4` | pass 1 | Gov. Code §§ 2, 3, 4, 5, 9, 9604, 9605, 9606, 9607, 9608, 9609, 9610, 9611; Civ. Code §§ 3, 5, 6, 20, 22.2, 23, 23.1, 23.2, 23.3, 23.4, 23.5, 23.6; Code Civ. Proc. §§ 3, 5, 6, 7, 8, 9, 18 | amendment, repeal, revival, retroactivity, continuation, conflicts among provisions |
| `usca-general-provisions.l4` | pass 1 | Gov. Code §§ 7, 8, 14, 16, 16.5, 18, 9612; Civ. Code §§ 12, 14, 17, 18, 19; Code Civ. Proc. §§ 11, 12c, 15, 17, 34 | "shall" and "may", joint authority, signature by mark, digital and electronic signature, notice, "writing", "State" |
| `usca-canons-of-reading.l4` | pass 2 | Gov. Code §§ 6, 10, 11, 12, 12.5, 13, 23, 24, 9603; Civ. Code §§ 4, 13, 22, 22.1; Code Civ. Proc. §§ 4, 16 | how the codes tell a reader to read: strict or liberal construction, headings, tense, gender and number, severability, the will of the supreme power |
| `usca-definitions.l4` | pass 2 | Gov. Code §§ 12.2, 15, 17, 19, 20, 21, 22, 26; Code Civ. Proc. §§ 14 | the defined terms, as a table of what each is said to include or mean, and the special cases |
| `usca-remedies-and-actions.l4` | pass 2 | Code Civ. Proc. §§ 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 32.5, 33 | a classification tree: judicial remedy, action or special proceeding, civil or criminal, obligation or injury |
| `usca-proclaimed-days.l4` | pass 2 | Gov. Code §§ 6708, 6709, 6710, 6711, 6712, 6713, 6714, 6715, 6716, 6717, 6718, 6719, 6720, 6721, 6722, 6723, 6724, 6725, 6726, 6727, 6728, 6729, 6731, 6733, 6735, 6736 | the day or period each section directs the Governor to proclaim, in a given year, and whether the duty recurs |
| `usca-deputies.l4` | pass 2 | Gov. Code §§ 7.5, 7.6, 7.7, 7.8, 7.9, 7.9a | who may be designated to sit in an officer's place, where, with what powers, and who answers for the deputy |
| `usca-assessed-value.l4` | pass 2 | Gov. Code §§ 25 | assessed value by fiscal year, restating an amount or a tax rate for comparison, the two conversion factors |
| `usca-further-limbs.l4` | pass 2 | Gov. Code §§ 16.5, 6700, 6801, 6808, 9606 | the limbs of pass-1 sections that pass 1 left out: Gov. Code § 6700(b), § 6801 (first day of the year), § 6808(a) and (c), § 9606 (second sentence), § 16.5(d)-(f) |
| `usca-further-asks.l4` | after the test pass | Gov. Code §§ 4, 12.5, 14, 16.5, 24, 6701, 6703, 6704, 6705, 6706, 6707, 6801, 6802, 6804, 9602, 9604, 9605, 9607, 9608, 9610, 9611; Civ. Code §§ 3, 17, 20, 22.2, 23.6; Code Civ. Proc. §§ 3, 9, 10, 12, 12a, 12b, 13a, 13b, 33 | the questions the first two passes gave no function for: who may act or must close under Gov. Code §§ 6701(c) and (d), 6703-6707, 9602-9611, which source or office a rule reaches (Code Civ. Proc. §§ 12a(b), 12b), the yes-or-no limbs of Civ. Code §§ 14(b), 17, 20, 22.2, 23.6 and Code Civ. Proc. § 9, and the Section 135 variants that refuse when the list is not given |

**The questions the brief asked, and where they are answered.**

| Question | Where | In one line |
|---|---|---|
| Commencement of a statute, a resolution, the codes | `usca-interpretation-time.l4`, section `When an enactment goes into effect` | Gov. Code § 9600(a) and (b), § 9602, Civ. Code § 2, Code Civ. Proc. § 2, with the moment within the day; an Act that names its own day, subordinate legislation and the Government Code's own day are refused |
| Counting days, weeks, months, years | same, sections `Counting a period` and `Year, half year and quarter of a year` | § 6800, § 6803, § 6804, § 6805; a month with no day of the start day's number is refused |
| Rest days and holidays | same, section `The last day of a period when it falls on a holiday`, and `usca-holidays.l4` | The calendar is an input; the holidays module offers the Government Code, Civil Code and Code of Civil Procedure calendars |
| Deemed service or notice | `usca-general-provisions.l4` | The deposit has no general rule; both functions refuse and say so; nothing was invented |
| Repeal | `usca-operation-of-statutes.l4`, and `usca-further-limbs.l4` for § 9606's second sentence | Gov. Code §§ 9605-9611 (and 9604), Civ. Code § 20, Code Civ. Proc. § 18 |
| Time words | `usca-interpretation-time.l4`, `usca-further-limbs.l4` | Gov. Code §§ 6803-6806 (year, half year, quarter, month, week, day), § 6807 (daytime), § 6808 (daylight saving time; the standard time and the Legislature's power to amend, in the further-limbs module) |
| The meaning of a word | `usca-canons-of-reading.l4`, `usca-definitions.l4`, `usca-remedies-and-actions.l4` | Each code's defined terms, and its rules of reading, as functions of the code and the facts the caller states |
| What the Governor is told to proclaim | `usca-proclaimed-days.l4` | Which day, in which year |

**What the text does not answer.**
Each of these is a named `REFUSE` in a module, with a test that asserts it (`#ASSERT REFUSED`), and each has an entry in the fork register or a question below.
Examples: whether a day proclaimed under Gov. Code §§ 6708-6736 is a holiday (F-hol-6); whether the duty of §§ 6708-6711 recurs each year (F-proclaim-once); whether 21:00 or 22:00 is inside "between 9 p.m. and 10 p.m." (F-between); the Sunday meant by § 6720 in a year when April 24 is a Sunday (F-6720); the offset of Pacific standard time from UTC (15 U.S.C. §§ 261 and 263 are not deposited); what follows when fewer than two employees qualify under Gov. Code § 7.9(b); a remedy that is not a judicial remedy (F-23); depriving an owner of the benefit of property by a way other than the four § 28 names (F-28).
Inputs the text does not give and the caller supplies: the days of Lunar New Year, Diwali, Good Friday and Thanksgiving Day, the days appointed by the President or Governor, the judicial holidays of Code Civ. Proc. § 135 (not deposited), the day of the astronomical Northward equinox (§ 6727), the meaning of "recycled water" (Water Code § 13050(n), not deposited), whether a person holds a position specified in Art. VII § 4 or Art. IX § 2.1 of the Constitution (not deposited), whether a vote is a two-thirds vote (§ 6808(c)), and the full value of a property (§ 25).

**Reading a result.**
A function here returns `TRUE`, `FALSE` or a value, or it refuses.
What a result means depends on what the function's name asks, and some failures give no sign that they happened.
They are sorted below by whether the encoding says so.

*Failures that say so (loud).*
- A `REFUSE "..."`: `l4 run` prints "The model refuses to answer" and the message, which says what the text does not say.
  An `#ASSERT` over an expression that refuses is "refused" (Warning severity), and `check.sh` counts it as refused, which makes the run red.
- A type error, a name not in scope or a parse error: an error diagnostic, counted by `check.sh`.
- A calendar in which more than 366 days in a row are holidays: the loop guard refuses (F-run).

*Failures that return an answer with exit status 0 (SILENT).* Read these first.
- **A list of days the caller leaves out is read as empty, so a holiday is not a holiday.**
  `Days supplied by the caller` has ten fields, nine of them lists of dates (Lunar New Year; Diwali; days appointed by the President or Governor; Thursdays appointed as Thanksgiving Day; Good Friday; days on which March 31 is observed instead; the judicial holidays of Code Civ. Proc. § 135; days a public office is closed for the whole day; bank closings).
  `no day is supplied` fills all nine with the empty list, and a record built by hand with one list forgotten is indistinguishable from one built with that list empty.
  The result is `FALSE` for the day, with no diagnostic.
  The case that matters most is Code Civ. Proc. § 135, which is not deposited: with no § 135 day, `a holiday under Code Civ. Proc. § 10`, `a holiday for computing time under Code Civ. Proc. § 12` and both `a holiday for the extension of Code Civ. Proc. § 12a(a)` functions answer `FALSE` for 25 December 2026 and for 1 January 2027 (`test-usca-further-asks.l4` asserts this for 25 December on the two older functions, on purpose).
  A caller who forgets § 135 is told that Christmas is not a holiday for the Code of Civil Procedure.
  **A loud variant exists for § 135 only**: the four functions of `usca-further-asks.l4` named `... the Section 135 days being` take the list as a `MAYBE`; `NOTHING` (the caller has not said) refuses, `JUST EMPTY` (the caller says there are none) answers from the rest of the record.
  The other eight lists have no loud variant, and a caller who does not know one of them should not use `no day is supplied` for it.
  The older functions keep their signatures and their silence.
- **A date before an amendment is answered with today's text** (F-vintage): the deposit holds one version of each section.
- **`FALSE` is not the opposite.** Read next.
- **A refusal asserted without its message** (102 of the 111 `#ASSERT REFUSED` lines of the pass-2 tests): a `REFUSE` that fires for a reason other than the intended one would pass.
  The tests added after the independent test pass assert every message.

*What `FALSE` and `REFUSE` mean, by the name of the function.*
- A function whose name asks what **this section** gives, requires or permits (`Gov. Code § 6704 gives the body the power ...`, `Code Civ. Proc. § 13a or § 13b requires an act to be performed on`) answers `FALSE` for a case outside the section's condition.
  `FALSE` says "this section does not give that result"; it does not say the opposite is true, and another provision may give the result.
  Every function of `usca-further-asks.l4` is of this kind unless it is listed below.
- A function that asks what a thing **is**, or what the law at large permits, or whether a section reaches a thing that **arguably falls inside a category the section names**, **refuses**: no section says no.
  The model is Gov. Code § 7: `a power of a public officer may be exercised, or a duty performed, by` refuses for "another person", since the section lets a deputy or a person authorised pursuant to law act and does not say that no one else may.
  In `usca-further-asks.l4` the refusals of this kind are: `Gov. Code § 6703 requires the body to be closed on the day` for the Legislature on Admission Day (the Legislature is among the "public offices of the state" in (b)); `Gov. Code § 6706 applies to an act appointed to be performed on a particular day by` a court order (arguably "law"); `Code Civ. Proc. § 12a applies to a period fixed by` a contract; `Code Civ. Proc. § 12b applies to the computation of time under` Gov. Code § 6800 (which says the same as the section named); `Gov. Code § 9604 applies to a reference made by` a contract or a regulation (a regulation is akin to an ordinance); and the others marked "refuses" in the table under "Findings".
  The line between the two kinds is the encoder's judgment, not the text's: `FALSE` where the thing plainly is not in the section's class (a county is not "a city or district", a county agency is not "a state agency", a branch office or a private office is not "a public office", other than a branch office), `REFUSE` where it arguably is.
- Older functions follow this in most places and not in all (the next paragraphs list the ones that matter).
  Where they differ, the message of the refusal says what the text does not say, and the fork register says why the answer is what it is.

*Three rules of the text and what the encoding does with them.*
1. **The asymmetry between the codes on the common law (deliberate).**
   Civ. Code § 5 construes a provision "substantially the same as existing statutes or the common law" as a continuation; Gov. Code § 2 speaks only of "existing statutory provisions relating to the same subject matter", and Code Civ. Proc. § 5 only of "existing statutes" (`GOV-ss-1-26.txt:10`, `CIV-ss-1-23.6.txt:20`, `CCP-ss-1-34.txt:20`).
   `the section construes a provision of` code `as a restatement and continuation ...` therefore answers `TRUE` for a provision substantially the same only as the common law under the Civil Code and `FALSE` under the other two.
   That is the second kind of `FALSE` above: it says the Government Code and the Code of Civil Procedure sections do not do this for the common law, which is what their words say; it does not say the provision is a new enactment.
   It was not changed.
   The test author expected "not covered" for the Government Code (S3) and the Code of Civil Procedure (S522) and the reconciled assertions say `FALSE`.
2. **"Includes" is not exhaustive, so a thing outside the list refuses.**
   A definition by inclusion names some members and does not say there are none other; the encoding refuses for an unlisted thing, and answers `FALSE` only for a definition by "means" or "is coextensive with" or a thing the definition expressly excludes.
   Two examples: Civ. Code § 14(a) ("oath includes affirmation or declaration"; "person includes a corporation") and Code Civ. Proc. § 17(b)(5)(B) ("Testify includes any mode of oral statement made under oath or affirmation").
3. **"Unless otherwise expressed / provided / apparent": it is not true that every such function refuses.**
   The sections say only that they yield; none says what governs when the contrary provision applies.
   The encoding does one of two things, by what the function asks: a function that asks *whether the section's own rule applies* answers `FALSE` once the exception holds (it is the first kind above); a function that asks for *the outcome the contrary provision decides* refuses.
   The sorting is in F-otherwise.

## Re-disposition audit

**Status.** Written on 2026-10-29 before any new L4 was written, and kept current: the counts and the verdicts below were re-run from `coverage.py` and `units.py` after the last change to `dispositions.tsv`.
Pass 1 worked to a narrower standard of what to skip; this section re-derives every disposition from the text.

**How the units were counted.**
`units.py` (in this folder; `python3 -I units.py`, add `--ids` for the list) reads the six deposited `.txt` files and counts, by script:
every section (a line that starts with a section number above the previous one), every labelled subdivision at any depth (`(a)`, `(1)`, `(A)`, and two labels on one line as in `(20) (A)`), every unlabelled list item (the divisions of the Civil Code, the parts of the Code of Civil Procedure, the numbered limbs of Civ. Code § 18 and Code Civ. Proc. §§ 21, 24, 25, 27), and every defined-term entry.
The text has no table: the converter turns a table row into a line, and none of the six files contains one, so the count of table rows is 0.
A defined-term entry is a term in curly quotes followed by `means`, `includes`, `signifies`, `refers to`, `coextensive` or the like, found by pattern, plus the entries whose term is not in quotes (the tense, gender and number limbs of Gov. Code §§ 11-13, Civ. Code § 14(a) and Code Civ. Proc. § 17(a), `testify` and `depose` in Civ. Code § 14(a), `shall` and `may`, `law`, `actual notice` and `constructive notice`, `week`, `day`, `daytime`, `nighttime`, `half year`, `quarter of a year`, `holidays within the meaning of the code`, and the terms of Code Civ. Proc. §§ 20-29 that define by a sentence).
Those unquoted entries were read by hand and are listed in `EXTRA_TERMS` in `units.py`: 43 of the defined-term entries are hand-added, the rest are found by the pattern.
The seven section numbers that the ranges skip are counted as units of their own (kind N).

```
sections: 159
labelled subdivisions: 132
list items: 18
defined-term entries: 90
table rows: 0
units in all: 399
  sections in GOV 1-26: 35
  sections in GOV 6700-6736: 34
  sections in GOV 6800-6808: 9
  sections in GOV 9600-9612: 12
  sections in CIV 1-23.6: 29
  sections in CCP 1-34: 40
units that are numbers absent from the text: 7
units in all (the rows of the coverage table): 406
```

| | pass 1 | now |
|---|---|---|
| sections | 159 rows | 159 rows |
| numbers absent from the text | 7 rows | 7 rows |
| labelled subdivisions, list items, defined-term entries | 0 rows (the table was one row per section) | 240 rows |
| rows in all | 166 | 406 |
| `not applicable` | 48 rows | 0: the brief has no such disposition |
| section rows by disposition | 82 encoded, 29 inert, 48 not applicable | 133 encoded, 21 fork, 5 inert |

**Units that pass 1's table did not have** (every one is now a row of the coverage table; section: its units):

- Gov. Code § 7.6: (a); (b); (c); (d); (e); (f)
- Gov. Code § 7.9: (a); (b); (c)
- Gov. Code § 10: term Section; term Subdivision
- Gov. Code § 12.2: term Spouse
- Gov. Code § 15: term Oath
- Gov. Code § 16: term Signature
- Gov. Code § 16.5: (a); (a)(1); (a)(2); (a)(3); (a)(4); (a)(5); (b); (c); (d); (d) term Digital signature; (e); (f)
- Gov. Code § 17: term Person
- Gov. Code § 18: term State
- Gov. Code § 19: term County
- Gov. Code § 20: term City
- Gov. Code § 21: term Town
- Gov. Code § 22: term Process
- Gov. Code § 25: (a); (a) term assessed value; (b); (c)
- Gov. Code § 26: term recycled water
- Gov. Code § 14: term shall; term may
- Gov. Code § 11: term present tense; term future tense
- Gov. Code § 12: term masculine gender
- Gov. Code § 13: term singular number; term plural number
- Gov. Code § 6700: (a); (a)(1); (a)(2); (a)(3); (a)(4); (a)(5); (a)(6); (a)(7); (a)(8); (a)(9); (a)(10); (a)(11); (a)(12); (a)(13); (a)(14); (a)(15); (a)(16); (a)(17); (a)(18); (a)(19); (a)(20); (a)(20)(A); (a)(20)(B); (b)
- Gov. Code § 6701: (a); (b); (c); (c)(1); (c)(2); (c)(3); (d)
- Gov. Code § 6703: (a); (b)
- Gov. Code § 6726: (a); (b); (c); (d)
- Gov. Code § 6731: (a); (b)
- Gov. Code § 6705: term special or limited holiday
- Gov. Code § 6803: term Year; term half year; term quarter of a year
- Gov. Code § 6804: term Month
- Gov. Code § 6808: (a); (b); (c)
- Gov. Code § 6805: term week
- Gov. Code § 6806: term day
- Gov. Code § 6807: term Daytime; term Nighttime
- Gov. Code § 9600: (a); (b)
- Gov. Code § 9605: (a); (a)(1); (a)(2); (b); (b)(1); (b)(2)
- Gov. Code § 9607: (a); (b)
- Civ. Code § 1: item I; item II; item III; item IV
- Civ. Code § 7.1: (a); (b); (c); (d); (e); (f); (g); (h); (i); (j); (k); (l); (m); (n); (o); (p); (q); (r)
- Civ. Code § 14: (a); (b); (b)(1); (b)(1) term property; (b)(2); (b)(2) term real property; (b)(3); (b)(3) term personal property; (b)(4); (b)(4) term month; (b)(5); (b)(5) term will; (b)(6); (b)(6) term section; (b)(7); (b)(7) term spouse; term (a) present tense; term (a) masculine gender; term (a) singular number; term (a) plural number; term (a) person; term (a) county; term (a) writing; term (a) oath; term (a) testify; term (a) depose; term (a) signature or subscription
- Civ. Code § 18: item 1; item 2; term actual notice; term constructive notice
- Civ. Code § 22.1: (a); (b)
- Civ. Code § 7: term holidays within the meaning of the code
- Civ. Code § 22: term law
- Code Civ. Proc. § 1: item I; item II; item III; item IV
- Code Civ. Proc. § 12a: (a); (a) term holiday; (b)
- Code Civ. Proc. § 12c: (a); (b)
- Code Civ. Proc. § 14: term seal
- Code Civ. Proc. § 17: (a); (b); (b)(1); (b)(1) term Affinity; (b)(2); (b)(2) term County; (b)(3); (b)(3) term Electronic signature; (b)(4); (b)(4) term Month; (b)(5); (b)(5) term Oath; (b)(5)(A); (b)(5)(A) term Depose; (b)(5)(B); (b)(5)(B) term Testify; (b)(6); (b)(6) term Person; (b)(7); (b)(7) term Process; (b)(8); (b)(8) term Property; (b)(8)(A); (b)(8)(A) term Personal property; (b)(8)(B); (b)(8)(B) term Real property; (b)(9); (b)(9) term Section; (b)(10); (b)(10) term Sheriff; (b)(11); (b)(11) term Signature; (b)(12); (b)(12) term Spouse; (b)(13); (b)(13) term State; (b)(13) term United States; (b)(14); (b)(14) term Will; (b)(15); (b)(15) term Writ; (b)(16); (b)(16) term Writing; term (a) present tense; term (a) masculine gender; term (a) singular number; term (a) plural number
- Code Civ. Proc. § 21: item 1; item 2
- Code Civ. Proc. § 24: item 1; item 2
- Code Civ. Proc. § 25: item 1; item 2; term civil action
- Code Civ. Proc. § 26: (a); (b); term obligation; term obligation arising from contract; term obligation arising from operation of law
- Code Civ. Proc. § 27: item 1; item 2
- Code Civ. Proc. § 32.5: term jurisdictional classification
- Code Civ. Proc. § 20: term judicial remedies
- Code Civ. Proc. § 22: term action
- Code Civ. Proc. § 23: term special proceeding
- Code Civ. Proc. § 28: term injury to property
- Code Civ. Proc. § 29: term injury to the person
- Code Civ. Proc. § 10: term holidays within the meaning of the code

**Verdict on every section row that was not `encoded` in pass 1** (29 `inert` and 48 `not applicable`, 77 in all).
Pass 1's reasons (`a canon of construction`, `a one-line definition`, `addresses an official`, `board machinery`, `no input fact changes the answer`, `a pointer to a section that is not deposited`, `a classification of a procedural category`) are on the brief's list of reasons that no longer stand.
Of the 77: 5 keep `inert` (all pass-1 `inert`: Gov. Code § 1, Civ. Code §§ 1 and 21, Code Civ. Proc. §§ 1 and 19), 60 move to `encoded` (21 of the 29 pass-1 `inert`, 39 of the 48 `not applicable`) and 12 move to `fork` (3 and 9).
The reasons the 5 keep are the brief's: reason 1 (not operative: title, enacting words) and reason 2 (machinery: short title).
`not applicable` is not one of the four dispositions and no row keeps it.

- Gov. Code § 1 (pass 1: inert): keeps `inert`, reason 2 (short title: the Act is known as the Government Code)
- Gov. Code § 6 (pass 1: inert): moves to `encoded`: `usca-canons-of-reading.l4`, section `Gov. Code § 6: headings`. was inert in pass 1; after the independent test pass the function also takes the heading of a subdivision and of a paragraph, which the section does not name, and refuses them
- Gov. Code § 7.5 (pass 1: not applicable): moves to `encoded`: `usca-deputies.l4`, section `Gov. Code § 7.5: a director of a state department`: `Gov. Code § 7.5 lets the director designate`; `this many directors may be represented by deputies at a meeting under`; `a designated deputy may do the act in the officer's place` and `the officer is responsible for the act of the deputy` (one function for each of §§ 7.5, 7.6(a), 7.8 and 7.9(a)). was `not applicable` in pass 1
- Gov. Code § 7.6 (pass 1: not applicable): moves to `encoded`: `usca-deputies.l4`, section `Gov. Code § 7.6: officers whose offices the Constitution creates`: the functions listed against its subdivisions (a) to (e); subdivision (f) is a fork. was `not applicable` in pass 1
- Gov. Code § 7.7 (pass 1: not applicable): moves to `encoded`: `usca-deputies.l4`, section `Gov. Code § 7.7: saving of Section 7`: `the section affects or modifies Section 7`. was `not applicable` in pass 1
- Gov. Code § 7.8 (pass 1: not applicable): moves to `fork`: `usca-deputies.l4`, section `Gov. Code § 7.8: the State Allocation Board`: `Gov. Code § 7.8 lets the director designate`; `this many directors may be represented by deputies at a meeting under`; `more persons may represent the same director at a meeting under Section 7.8`; `a designated deputy may do the act in the officer's place` and `the officer is responsible for the act of the deputy` (one function for each of §§ 7.5, 7.6(a), 7.8 and 7.9(a)). fork F-7.8: `irrespective of whether there shall be more than one such person representing a director` is read as lifting § 7.5's limit of one director represented per meeting, at the State Allocation Board; whether several persons may represent the same director is refused; was `not applicable` in pass 1
- Gov. Code § 7.9 (pass 1: not applicable): moves to `encoded`: `usca-deputies.l4`, section `Gov. Code § 7.9 and § 7.9a: the Controller, the Treasurer, the Director of Finance and the Superintendent of Public Instruction`: the functions listed against its subdivisions (a) to (c). was `not applicable` in pass 1
- Gov. Code § 7.9a (pass 1: not applicable): moves to `encoded`: `usca-deputies.l4`, section `Gov. Code § 7.9 and § 7.9a: the Controller, the Treasurer, the Director of Finance and the Superintendent of Public Instruction`: `Gov. Code § 7.9a requires two more employees of the officer to be classified as career executives`; `the career executive may be classified at`. was `not applicable` in pass 1
- Gov. Code § 10 (pass 1: inert): moves to `encoded`: `usca-canons-of-reading.l4`, section `Gov. Code § 10, Civ. Code § 14(b)(6), Code Civ. Proc. § 17(b)(9): section and subdivision`. was inert in pass 1
- Gov. Code § 11 (pass 1: inert): moves to `fork`: `usca-canons-of-reading.l4`, section `Tense, gender and number: Gov. Code §§ 11-13, Civ. Code § 14(a), Code Civ. Proc. § 17(a)`: `a word used in the tense includes the tense, in`. fork F-tense: Gov. Code § 11 says the present tense includes the past and future and the future the present; Civ. Code § 14(a) and Code Civ. Proc. § 17(a) say the present includes the future and say nothing of the past; the function takes the code and refuses a pair of tenses the code does not mention; was inert in pass 1
- Gov. Code § 12 (pass 1: inert): moves to `encoded`: `usca-canons-of-reading.l4`, section `Tense, gender and number: Gov. Code §§ 11-13, Civ. Code § 14(a), Code Civ. Proc. § 17(a)`. was inert in pass 1
- Gov. Code § 12.2 (pass 1: inert): moves to `encoded`: `usca-definitions.l4`, section `The table of defined terms`. was inert in pass 1
- Gov. Code § 12.5 (pass 1: inert): moves to `encoded`: `usca-canons-of-reading.l4`, section `Gov. Code § 12.5 and § 24: the words man and workmen's compensation`; added after the independent test pass, `usca-further-asks.l4`: `the declaration of Gov. Code § 12.5 or § 24 is amendatory of existing law`. was inert in pass 1; the last sentence (declaratory, not amendatory) states a fact about the Act and creates no rule (inert reason 1), and since the independent test pass it can be asked: `the declaration of Gov. Code § 12.5 or § 24 is amendatory of existing law` is FALSE
- Gov. Code § 13 (pass 1: inert): moves to `encoded`: `usca-canons-of-reading.l4`, section `Tense, gender and number: Gov. Code §§ 11-13, Civ. Code § 14(a), Code Civ. Proc. § 17(a)`. was inert in pass 1
- Gov. Code § 15 (pass 1: inert): moves to `encoded`: `usca-definitions.l4`, section `The table of defined terms`. was inert in pass 1
- Gov. Code § 17 (pass 1: inert): moves to `encoded`: `usca-definitions.l4`, section `The table of defined terms`. was inert in pass 1
- Gov. Code § 19 (pass 1: inert): moves to `encoded`: `usca-definitions.l4`, section `The table of defined terms`. was inert in pass 1
- Gov. Code § 20 (pass 1: inert): moves to `encoded`: `usca-definitions.l4`, section `The table of defined terms`. was inert in pass 1
- Gov. Code § 21 (pass 1: inert): moves to `encoded`: `usca-definitions.l4`, section `The table of defined terms`. was inert in pass 1
- Gov. Code § 22 (pass 1: inert): moves to `fork`: `usca-definitions.l4`, section `Process: Gov. Code § 22, Code Civ. Proc. § 17(b)(7)`: `a document is process under Gov. Code § 22`. fork F-process: Gov. Code § 22 says process `includes` a writ or summons issued in a civil or criminal judicial proceeding (an open list, so anything else is refused); Code Civ. Proc. § 17(b)(7) says it `signifies` a writ or summons issued in a judicial proceeding and is read as closed; was inert in pass 1
- Gov. Code § 23 (pass 1: inert): moves to `encoded`: `usca-canons-of-reading.l4`, section `Gov. Code § 23: severability`. was inert in pass 1
- Gov. Code § 24 (pass 1: inert): moves to `encoded`: `usca-canons-of-reading.l4`, section `Gov. Code § 12.5 and § 24: the words man and workmen's compensation`; added after the independent test pass, `usca-further-asks.l4`: `the declaration of Gov. Code § 12.5 or § 24 is amendatory of existing law`. was inert in pass 1; the last sentence is declaratory (inert reason 1), and since the independent test pass it can be asked: see Gov. Code § 12.5
- Gov. Code § 25 (pass 1: not applicable): moves to `encoded`: `usca-assessed-value.l4`: the functions listed against its subdivisions (a) to (c). section row; was `not applicable` in pass 1
- Gov. Code § 26 (pass 1: inert): moves to `encoded`: `usca-definitions.l4`, section `Recycled water: Gov. Code § 26`. was inert in pass 1; the meaning is in Water Code § 13050(n), not deposited, so it is asked as an input
- Gov. Code § 6708 (pass 1: not applicable): moves to `fork`: `usca-proclaimed-days.l4`, section `The days the Governor is directed to proclaim: Gov. Code §§ 6708-6736`. fork F-proclaim-once: these four sections say `shall proclaim` without `annually`, so the text does not say whether the duty recurs each year; the function refuses for a year after the first; was `not applicable` in pass 1
- Gov. Code § 6709 (pass 1: not applicable): moves to `fork`: `usca-proclaimed-days.l4`, section `The days the Governor is directed to proclaim: Gov. Code §§ 6708-6736`. fork F-proclaim-once: these four sections say `shall proclaim` without `annually`, so the text does not say whether the duty recurs each year; the function refuses for a year after the first; was `not applicable` in pass 1
- Gov. Code § 6710 (pass 1: not applicable): moves to `fork`: `usca-proclaimed-days.l4`, section `The days the Governor is directed to proclaim: Gov. Code §§ 6708-6736`. fork F-proclaim-once: these four sections say `shall proclaim` without `annually`, so the text does not say whether the duty recurs each year; the function refuses for a year after the first; was `not applicable` in pass 1
- Gov. Code § 6711 (pass 1: not applicable): moves to `fork`: `usca-proclaimed-days.l4`, section `The days the Governor is directed to proclaim: Gov. Code §§ 6708-6736`. fork F-proclaim-once: these four sections say `shall proclaim` without `annually`, so the text does not say whether the duty recurs each year; the function refuses for a year after the first; was `not applicable` in pass 1
- Gov. Code § 6712 (pass 1: not applicable): moves to `encoded`: `usca-proclaimed-days.l4`, section `The days the Governor is directed to proclaim: Gov. Code §§ 6708-6736`. was `not applicable` in pass 1; whether a proclaimed day is a holiday is fork F-hol-6, answered by a refusal in `a proclamation under the section makes the day a holiday`
- Gov. Code § 6713 (pass 1: not applicable): moves to `encoded`: `usca-proclaimed-days.l4`, section `The days the Governor is directed to proclaim: Gov. Code §§ 6708-6736`. was `not applicable` in pass 1; whether a proclaimed day is a holiday is fork F-hol-6, answered by a refusal in `a proclamation under the section makes the day a holiday`
- Gov. Code § 6714 (pass 1: not applicable): moves to `encoded`: `usca-proclaimed-days.l4`, section `The days the Governor is directed to proclaim: Gov. Code §§ 6708-6736`. was `not applicable` in pass 1; whether a proclaimed day is a holiday is fork F-hol-6, answered by a refusal in `a proclamation under the section makes the day a holiday`
- Gov. Code § 6715 (pass 1: not applicable): moves to `encoded`: `usca-proclaimed-days.l4`, section `The days the Governor is directed to proclaim: Gov. Code §§ 6708-6736`. was `not applicable` in pass 1; whether a proclaimed day is a holiday is fork F-hol-6, answered by a refusal in `a proclamation under the section makes the day a holiday`
- Gov. Code § 6716 (pass 1: not applicable): moves to `encoded`: `usca-proclaimed-days.l4`, section `The days the Governor is directed to proclaim: Gov. Code §§ 6708-6736`. was `not applicable` in pass 1; whether a proclaimed day is a holiday is fork F-hol-6, answered by a refusal in `a proclamation under the section makes the day a holiday`
- Gov. Code § 6717 (pass 1: not applicable): moves to `encoded`: `usca-proclaimed-days.l4`, section `The days the Governor is directed to proclaim: Gov. Code §§ 6708-6736`. was `not applicable` in pass 1; whether a proclaimed day is a holiday is fork F-hol-6, answered by a refusal in `a proclamation under the section makes the day a holiday`
- Gov. Code § 6718 (pass 1: not applicable): moves to `encoded`: `usca-proclaimed-days.l4`, section `The days the Governor is directed to proclaim: Gov. Code §§ 6708-6736`. was `not applicable` in pass 1; whether a proclaimed day is a holiday is fork F-hol-6, answered by a refusal in `a proclamation under the section makes the day a holiday`
- Gov. Code § 6719 (pass 1: not applicable): moves to `encoded`: `usca-proclaimed-days.l4`, section `The days the Governor is directed to proclaim: Gov. Code §§ 6708-6736`. was `not applicable` in pass 1; whether a proclaimed day is a holiday is fork F-hol-6, answered by a refusal in `a proclamation under the section makes the day a holiday`
- Gov. Code § 6720 (pass 1: not applicable): moves to `fork`: `usca-proclaimed-days.l4`, section `The days the Governor is directed to proclaim: Gov. Code §§ 6708-6736`: `the days the Governor is directed to proclaim under`. fork F-6720: when April 24 is itself a Sunday the text does not say whether that day is `the Sunday before` it, so the period is refused for such a year; whether the day is a holiday is fork F-hol-6; was `not applicable` in pass 1
- Gov. Code § 6721 (pass 1: not applicable): moves to `encoded`: `usca-proclaimed-days.l4`, section `The days the Governor is directed to proclaim: Gov. Code §§ 6708-6736`. was `not applicable` in pass 1; whether a proclaimed day is a holiday is fork F-hol-6, answered by a refusal in `a proclamation under the section makes the day a holiday`
- Gov. Code § 6722 (pass 1: not applicable): moves to `encoded`: `usca-proclaimed-days.l4`, section `The days the Governor is directed to proclaim: Gov. Code §§ 6708-6736`. was `not applicable` in pass 1; whether a proclaimed day is a holiday is fork F-hol-6, answered by a refusal in `a proclamation under the section makes the day a holiday`
- Gov. Code § 6723 (pass 1: not applicable): moves to `encoded`: `usca-proclaimed-days.l4`, section `The days the Governor is directed to proclaim: Gov. Code §§ 6708-6736`. was `not applicable` in pass 1; whether a proclaimed day is a holiday is fork F-hol-6, answered by a refusal in `a proclamation under the section makes the day a holiday`
- Gov. Code § 6724 (pass 1: not applicable): moves to `encoded`: `usca-proclaimed-days.l4`, section `The days the Governor is directed to proclaim: Gov. Code §§ 6708-6736`. was `not applicable` in pass 1; whether a proclaimed day is a holiday is fork F-hol-6, answered by a refusal in `a proclamation under the section makes the day a holiday`
- Gov. Code § 6725 (pass 1: not applicable): moves to `encoded`: `usca-proclaimed-days.l4`, section `The days the Governor is directed to proclaim: Gov. Code §§ 6708-6736`. was `not applicable` in pass 1; whether a proclaimed day is a holiday is fork F-hol-6, answered by a refusal in `a proclamation under the section makes the day a holiday`
- Gov. Code § 6726 (pass 1: not applicable): moves to `encoded`: `usca-proclaimed-days.l4`, section `Gov. Code § 6726: Space Day`: `a school, educational institution, resident, business or public entity is required to take part in Space Day`. was `not applicable` in pass 1; the day itself (the first Friday in May) is in the table of proclamations
- Gov. Code § 6727 (pass 1: not applicable): moves to `encoded`: `usca-proclaimed-days.l4`, section `The days the Governor is directed to proclaim: Gov. Code §§ 6708-6736`. was `not applicable` in pass 1; whether a proclaimed day is a holiday is fork F-hol-6, answered by a refusal in `a proclamation under the section makes the day a holiday`
- Gov. Code § 6728 (pass 1: not applicable): moves to `encoded`: `usca-proclaimed-days.l4`, section `The days the Governor is directed to proclaim: Gov. Code §§ 6708-6736`. was `not applicable` in pass 1; whether a proclaimed day is a holiday is fork F-hol-6, answered by a refusal in `a proclamation under the section makes the day a holiday`
- Gov. Code § 6729 (pass 1: not applicable): moves to `encoded`: `usca-proclaimed-days.l4`, section `The days the Governor is directed to proclaim: Gov. Code §§ 6708-6736`. was `not applicable` in pass 1; whether a proclaimed day is a holiday is fork F-hol-6, answered by a refusal in `a proclamation under the section makes the day a holiday`
- Gov. Code § 6731 (pass 1: not applicable): moves to `encoded`: `usca-proclaimed-days.l4`, section `The days the Governor is directed to proclaim: Gov. Code §§ 6708-6736`: `Gov. Code § 6731: California Farmworker Day` (the day, August 26, and the annual duty of subdivision (b)). was `not applicable` in pass 1
- Gov. Code § 6733 (pass 1: not applicable): moves to `encoded`: `usca-proclaimed-days.l4`, section `The days the Governor is directed to proclaim: Gov. Code §§ 6708-6736`. was `not applicable` in pass 1; whether a proclaimed day is a holiday is fork F-hol-6, answered by a refusal in `a proclamation under the section makes the day a holiday`
- Gov. Code § 6735 (pass 1: not applicable): moves to `encoded`: `usca-proclaimed-days.l4`, section `The days the Governor is directed to proclaim: Gov. Code §§ 6708-6736`. was `not applicable` in pass 1; whether a proclaimed day is a holiday is fork F-hol-6, answered by a refusal in `a proclamation under the section makes the day a holiday`
- Gov. Code § 6736 (pass 1: not applicable): moves to `encoded`: `usca-proclaimed-days.l4`, section `The days the Governor is directed to proclaim: Gov. Code §§ 6708-6736`. was `not applicable` in pass 1; whether a proclaimed day is a holiday is fork F-hol-6, answered by a refusal in `a proclamation under the section makes the day a holiday`
- Gov. Code § 9603 (pass 1: inert): moves to `encoded`: `usca-canons-of-reading.l4`, section `Gov. Code § 9603: where the general rules are`. was inert in pass 1
- Civ. Code § 1 (pass 1: inert): keeps `inert`, reason 1 (title and enacting words: names the Act and lists its four divisions)
- Civ. Code § 4 (pass 1: inert): moves to `encoded`: `usca-canons-of-reading.l4`, section `Strict and liberal construction: Civ. Code § 4, Code Civ. Proc. § 4`. was inert in pass 1
- Civ. Code § 13 (pass 1: inert): moves to `encoded`: `usca-canons-of-reading.l4`, section `Words and phrases: Civ. Code § 13, Code Civ. Proc. § 16`. was inert in pass 1
- Civ. Code § 21 (pass 1: inert): keeps `inert`, reason 2 (short title: how the Act may be cited)
- Civ. Code § 22 (pass 1: inert): moves to `fork`: `usca-canons-of-reading.l4`, section `Civ. Code § 22 and § 22.1: law and the will of the supreme power`. fork F-22: `Law is a solemn expression of the will of the supreme power of the State` is read as a definition, so an expression is a law only if it is both; was inert in pass 1
- Civ. Code § 22.1 (pass 1: inert): moves to `encoded`: `usca-canons-of-reading.l4`, section `Civ. Code § 22 and § 22.1: law and the will of the supreme power`. was inert in pass 1
- Code Civ. Proc. § 1 (pass 1: inert): keeps `inert`, reason 1 (title and enacting words: names the Act and lists its four parts)
- Code Civ. Proc. § 4 (pass 1: inert): moves to `encoded`: `usca-canons-of-reading.l4`, section `Strict and liberal construction: Civ. Code § 4, Code Civ. Proc. § 4`. was inert in pass 1
- Code Civ. Proc. § 14 (pass 1: inert): moves to `encoded`: `usca-definitions.l4`, section `The table of defined terms`. was inert in pass 1
- Code Civ. Proc. § 16 (pass 1: inert): moves to `encoded`: `usca-canons-of-reading.l4`, section `Words and phrases: Civ. Code § 13, Code Civ. Proc. § 16`. was inert in pass 1
- Code Civ. Proc. § 19 (pass 1: inert): keeps `inert`, reason 2 (short title: how the Act may be cited)
- Code Civ. Proc. § 20 (pass 1: not applicable): moves to `encoded`: `usca-remedies-and-actions.l4`, section `Code Civ. Proc. § 20: judicial remedies`. was `not applicable` in pass 1
- Code Civ. Proc. § 21 (pass 1: not applicable): moves to `encoded`: `usca-remedies-and-actions.l4`, section `Code Civ. Proc. § 21, § 22, § 23: actions and special proceedings`. was `not applicable` in pass 1
- Code Civ. Proc. § 22 (pass 1: not applicable): moves to `encoded`: `usca-remedies-and-actions.l4`, section `Code Civ. Proc. § 21, § 22, § 23: actions and special proceedings`. was `not applicable` in pass 1
- Code Civ. Proc. § 23 (pass 1: not applicable): moves to `fork`: `usca-remedies-and-actions.l4`, section `Code Civ. Proc. § 21, § 22, § 23: actions and special proceedings`: `the class of the judicial remedy`. fork F-23: `every other remedy is a special proceeding` is read as every other judicial remedy, the remedies § 21 divides; a remedy that is not a judicial remedy is refused; was `not applicable` in pass 1
- Code Civ. Proc. § 24 (pass 1: not applicable): moves to `encoded`: `usca-remedies-and-actions.l4`, section `Code Civ. Proc. § 24, § 25, § 30: civil and criminal actions`. was `not applicable` in pass 1
- Code Civ. Proc. § 25 (pass 1: not applicable): moves to `encoded`: `usca-remedies-and-actions.l4`, section `Code Civ. Proc. § 24, § 25, § 30: civil and criminal actions`. was `not applicable` in pass 1
- Code Civ. Proc. § 26 (pass 1: not applicable): moves to `encoded`: `usca-remedies-and-actions.l4`, section `Code Civ. Proc. § 26: obligation`. was `not applicable` in pass 1
- Code Civ. Proc. § 27 (pass 1: not applicable): moves to `encoded`: `usca-remedies-and-actions.l4`, section `Code Civ. Proc. § 27, § 28, § 29: injury`. was `not applicable` in pass 1
- Code Civ. Proc. § 28 (pass 1: not applicable): moves to `fork`: `usca-remedies-and-actions.l4`, section `Code Civ. Proc. § 27, § 28, § 29: injury`: `the kind of an injury`. fork F-28: § 28 says depriving an owner of the benefit of property `is done by` four ways and § 29 calls every other injury an injury to the person; depriving by some other way is refused, since reading § 29 literally would ignore § 28; was `not applicable` in pass 1
- Code Civ. Proc. § 29 (pass 1: not applicable): moves to `fork`: `usca-remedies-and-actions.l4`, section `Code Civ. Proc. § 27, § 28, § 29: injury`: `the kind of an injury`. fork F-28: § 28 says depriving an owner of the benefit of property `is done by` four ways and § 29 calls every other injury an injury to the person; depriving by some other way is refused, since reading § 29 literally would ignore § 28; was `not applicable` in pass 1
- Code Civ. Proc. § 30 (pass 1: not applicable): moves to `encoded`: `usca-remedies-and-actions.l4`, section `Code Civ. Proc. § 24, § 25, § 30: civil and criminal actions`. was `not applicable` in pass 1
- Code Civ. Proc. § 31 (pass 1: not applicable): moves to `encoded`: `usca-remedies-and-actions.l4`, section `Code Civ. Proc. § 31, § 32, § 32.5, § 33: criminal action, non-merger, classification, prosecuting attorney`. was `not applicable` in pass 1
- Code Civ. Proc. § 32 (pass 1: not applicable): moves to `encoded`: `usca-remedies-and-actions.l4`, section `Code Civ. Proc. § 31, § 32, § 32.5, § 33: criminal action, non-merger, classification, prosecuting attorney`. was `not applicable` in pass 1
- Code Civ. Proc. § 32.5 (pass 1: not applicable): moves to `encoded`: `usca-remedies-and-actions.l4`, section `Code Civ. Proc. § 31, § 32, § 32.5, § 33: criminal action, non-merger, classification, prosecuting attorney`. was `not applicable` in pass 1
- Code Civ. Proc. § 33 (pass 1: not applicable): moves to `encoded`: `usca-remedies-and-actions.l4`, section `Code Civ. Proc. § 31, § 32, § 32.5, § 33: criminal action, non-merger, classification, prosecuting attorney`; added after the independent test pass, `usca-further-asks.l4`: `Code Civ. Proc. § 33 requires a prosecuting attorney to assist in the civil resolution of a violation`. was `not applicable` in pass 1

**Rows that were `encoded` in pass 1 but left a limb out** (each limb now has its own row, and the ones below are new rules):
- Gov. Code § 6700(b) (a memorandum of understanding controls in a conflict): new rule, `usca-further-limbs.l4`.
- Gov. Code § 6808(a) (standard time is Pacific standard time) and (c) (the Legislature's power to amend by a two-thirds vote): new rules, `usca-further-limbs.l4`.
- Gov. Code § 16.5(d), (e), (f): new rules, `usca-further-limbs.l4`.
- Gov. Code § 6801, second limb (January 1 after 1752 is reckoned the first day of the year): new rule, `usca-further-limbs.l4`.
- Gov. Code § 9606, second sentence (persons acting under a statute act in contemplation of the power of repeal): new rule, `usca-further-limbs.l4`.
- The limbs of Civ. Code § 14(a), § 14(b) and Code Civ. Proc. § 17(a), (b) that pass 1 called `canons and one-line definitions` and left inert: now rows of `usca-canons-of-reading.l4` and `usca-definitions.l4`.
- Gov. Code § 26 and Code Civ. Proc. § 17(b)(1), (7), (13) (second half), (15) were `not applicable` or `inert` and are now definitions (`usca-definitions.l4`); Code Civ. Proc. § 32.5 is in `usca-remedies-and-actions.l4`.

**Rows that are `inert` now, and why.**
There are 14 rows, in 6 sections, and they are the only ones.
- Reason 1 (not operative): Civ. Code § 1 and its four division items (it names the Act and lists the divisions; no fact an individual states changes anything); Code Civ. Proc. § 1 and its four part items (the same); Gov. Code § 6726(c) (`Space Day shall promote space observation and appreciation ...`, a purpose clause that creates no rule).
- Reason 2 (machinery: short title): Gov. Code § 1 (the Act is known as the Government Code), Civ. Code § 21 and Code Civ. Proc. § 19 (how the Act may be cited).
- Reason 3 (shown repealed or blank): none is `inert`; the seven absent numbers have their own disposition, `repealed or blank in this text`.
- Sentences inside an `encoded` row that are themselves not operative are named in that row's note: Gov. Code § 12.5 and § 24 (`This act is declaratory and not amendatory of existing law`, reason 1; asked as a constant after the independent test pass), Gov. Code § 16.5(a)(5) (whom the secretary shall consult, reason 2; the date and the fewest hearings are asked since the test pass), Gov. Code § 6703(b) (the intent that the University of California also be closed, reason 1; asked as `FALSE` since the test pass).

**Counts by disposition after this pass** (`python3 -I coverage.py check`):

```
units with a row: 406  kinds: {'D': 132, 'L': 18, 'N': 7, 'S': 159, 'T': 90}
per disposition: {'encoded': 330, 'inert': 14, 'fork': 55, 'repealed or blank in this text': 7}
inert by reason: {'1': 11, '2': 3}
```

**What a `fork` row means.**
A row is `fork` when the reading of that very unit is an entry of the fork register: the code takes one reading or refuses, and the register says which and why.
A row is `encoded` when the unit is encoded as written; a fork is named in its note only when it concerns what the unit does to another section (F-hol-6 on §§ 6708-6736, whose days are computed as written), or when only one sentence of a larger row is a fork (F-6702city).
A section row whose limbs are rows of their own stays `encoded` if at least one limb is encoded and the fork limbs carry their own row (Gov. Code § 7.6 with § 7.6(f); Gov. Code § 25 with § 25(c); Gov. Code § 6726 with § 6726(b) and (d)).

## Target, build and layout

- **Target: `unstable`.** The brief requires `REFUSE` and `@lang en`, which `main` does not read.
  `check.sh` defaults to target `unstable`; with that target it prints that the main check was skipped, and there is no `fetch-main-l4.sh` in this row.
  Do not file this row for `main`.
- **Build.** `l4 --version` prints `unstable-20261028-5e95b5a (unstable, 5e95b5a, 2026-10-28)`.
  The binary is `/Volumes/transcend/claude-tmp/claude-502/-Users-mengwong-src-legalese-l4-ide/ca81f332-162b-4c52-8cc3-57ed15b3f6fa/scratchpad/bin/l4-unstable-0528`, sha256 `0f0f1b86d37164af242ca2b6c03aa31ddeedef752bd10474f1459b78cf539e9d`, also recorded in `encoding.json` (`l4_bin`).
  `JL4_LIBRARY_PATH` was left unset throughout.
  Pass 1 used another build (sha256 `2d912dd2a61ba36b3fb8c1e02dcbd445ba1143c3b8ecb931462c01050cd607d7`, version `dev`); pass 2 re-ran every pass-1 file with the build above and got the same numbers (1,696 satisfied, 8 expected failures); after the repair `test-usca-operation.l4` has 11 more satisfied assertions (1,707 in all for the pass-1 files), see "What `check.sh` prints" and "Changes to existing modules".
- **Modules, in reading order** (an `IMPORT` goes only upward in this list or to `prelude` and `daydate`):
  1. `usca-interpretation-time.l4` imports only `prelude` and `daydate`, as the pass-1 brief required.
     It has no holiday and no rest day in it: every function that needs a calendar takes it as an input of type `FUNCTION FROM DATE TO BOOLEAN`.
     The nouns it needs (`Moment`, `Kind of enactment`, `Enactment of a statute`) are declared in it; there is no separate nouns module.
  2. `usca-holidays.l4` imports `prelude`, `daydate` and the time module.
     It builds the calendars the time module takes, from the days the text fixes by the calendar and from lists the caller supplies for what the text does not compute.
  3. `usca-operation-of-statutes.l4` imports `prelude` and `daydate`.
  4. `usca-general-provisions.l4` imports `prelude`.
  5. `usca-canons-of-reading.l4` and `usca-definitions.l4` import `prelude` and the operation module (for `Kind of code`: `the Government Code`, `the Civil Code`, `the Code of Civil Procedure`); `usca-remedies-and-actions.l4` imports `prelude` only.
  6. `usca-proclaimed-days.l4` imports `prelude`, `daydate`, the time module (for `Moment`) and the holidays module (for the n-th weekday of a month): no rule is copied.
  7. `usca-deputies.l4` and `usca-assessed-value.l4` import `prelude` only; `usca-further-limbs.l4` imports `prelude` and `daydate`.
  8. `usca-further-asks.l4` (added after the independent test pass) imports `prelude`, `daydate`, the time module, the holidays module, the general-provisions module (for `Force of a word` and `Method of mailing`) and the operation module (for `Kind of code` and two functions it extends).
     It changes no earlier module: each of its functions sits beside the one it extends.
- **Tests** are at the top level (`check.sh` globs `*.l4` non-recursively): pass 1's `test-usca-time.l4`, `test-usca-rules.l4`, `test-usca-holidays.l4`, `test-usca-operation.l4`, `test-usca-general.l4`, `test-usca-worked.l4`, and `tests-red.l4`, which is meant to fail (see "What `check.sh` prints"); pass 2's `test-usca-canons.l4`, `test-usca-definitions.l4`, `test-usca-remedies.l4`, `test-usca-proclaimed-days.l4`, `test-usca-deputies.l4`, `test-usca-assessed.l4` and `test-usca-further-limbs.l4`; and, added after the independent test pass, `test-usca-further-asks.l4`.
  Each of the eight pass-2 and repair test files ends with `-- assertions written: N`, and N equals the number of `#ASSERT` lines and the number satisfied.
  The pass-1 test files have no such line; counting their `#ASSERT` lines gives 425, 334, 627, 134, 98 and 89, which are the satisfied counts of `check.sh`, and 8 for `tests-red.l4`, which are its 8 expected failures.
  Of them only `test-usca-operation.l4` was edited (it had 123; see "Changes to existing modules"); the others are byte-for-byte what pass 1 left.
- **Tools in this folder.**
  `units.py` counts the units of the text (`python3 -I units.py`, `--ids` for the list); `coverage.py` and `dispositions.tsv` generate the coverage table (`python3 -I coverage.py check`, `table`, `verdicts`, `missing`).
  `NOTES-pass1.md` is pass 1's file, kept because `coverage.py` reads the pass-1 function lists from it.
  `dispositions.tsv` is the hand-kept record from which the coverage table is generated: edit it, not the table.
- **How the calendars are meant to be used.**
  The caller builds a `Days supplied by the caller` record (or uses `no day is supplied`) and passes the time module a function from a date to a Boolean.
  A mixfix function is not partially applicable in L4, so the calendar is a named function of one date (`calendar G` in `test-usca-worked.l4`) or a lambda (`GIVEN x YIELD ...`, used in `test-usca-holidays.l4`).

**Conventions.**
- `FALSE` means "this section does not give this result"; `REFUSE` means an antecedent is undetermined or the section has no consequence for the case.
  No module has a home-made three-valued type.
  A function named "Gov. Code § X lets ..." returns `FALSE` when the facts do not bring the person within what that section gives; that does not say that no other law gives it.
- A definition by inclusion ("includes", and "signifies" where noted) names some members and does not say there are no others: a thing outside the list is `REFUSE`d.
  A definition by meaning ("means", "is coextensive with") is closed: a thing outside the list is `FALSE`.
- A moment is a day and a count of seconds after the midnight that begins it (fork F-midnight).
- A fiscal year is given by the first calendar year in its name (1980 for 1980-81).
- Every refusal is a named `REFUSE "..."` whose message says what the text does not say.
  The pass-1 tests assert the message exactly (`BECAUSE`); of the 111 `#ASSERT REFUSED` lines of the pass-2 tests, 9 do and 102 assert only that the expression refuses; all 22 of `test-usca-further-asks.l4` assert the message.
- Each rule is stated once, as a relation between two parties, and named neutrally (the brief's Hohfeld rule): "lets" for a power or privilege, "requires" or "is responsible for" for a duty, "may not be appointed" for a disability.

## Coverage table

One row per unit of the text (section, labelled subdivision, list item, defined-term entry) and one per absent number: 406 rows.
Generated by `python3 -I coverage.py table` from the text (`units.py`) and `dispositions.tsv`; do not edit the table by hand, edit `dispositions.tsv` and regenerate.
A pass-1 pointer (`P1`) was taken from pass 1's row for the section, which is kept in `NOTES-pass1.md`; each pass-1 function is listed under the module whose text contains it; a row for a limb of a section says so and points at the functions listed in the section row.
Dispositions: `encoded`, `inert` (reason 1, 2 or 3 as the brief defines them), `fork` (the entry of the fork register is named in the row), `repealed or blank in this text`.

<!-- coverage-table:begin -->
| Unit | Text file : line | Disposition | Where it is encoded, or why it is not |
|---|---|---|---|
| Gov. Code § 1 | GOV-ss-1-26.txt:8 | inert | 2 (short title: the Act is known as the Government Code). moved nowhere; pass 1 also had it inert |
| Gov. Code § 2 | GOV-ss-1-26.txt:10 | encoded | `usca-operation-of-statutes.l4`: `the section construes a provision of` |
| Gov. Code § 3 | GOV-ss-1-26.txt:12 | encoded | `usca-operation-of-statutes.l4`: `a holder of an office under a repealed act continues to hold it under Gov. Code § 3` |
| Gov. Code § 4 | GOV-ss-1-26.txt:14 | encoded | `usca-operation-of-statutes.l4`: `the section protects an action, proceeding or accrued right from the code`; `procedure taken after the code took effect in a proceeding begun before must conform to the code`; added after the independent test pass, `usca-further-asks.l4`: `the code says that no part of it is retroactive unless expressly so declared` |
| Gov. Code § 5 | GOV-ss-1-26.txt:16 | encoded | `usca-operation-of-statutes.l4`: `the general provisions of the Government Code govern the construction of the code` |
| Gov. Code § 6 | GOV-ss-1-26.txt:18 | encoded | `usca-canons-of-reading.l4`, section `Gov. Code § 6: headings`. was inert in pass 1; after the independent test pass the function also takes the heading of a subdivision and of a paragraph, which the section does not name, and refuses them |
| Gov. Code § 7 | GOV-ss-1-26.txt:20 | encoded | `usca-general-provisions.l4`: `a power of a public officer may be exercised, or a duty performed, by` |
| Gov. Code § 7.5 | GOV-ss-1-26.txt:22 | encoded | `usca-deputies.l4`, section `Gov. Code § 7.5: a director of a state department`: `Gov. Code § 7.5 lets the director designate`; `this many directors may be represented by deputies at a meeting under`; `a designated deputy may do the act in the officer's place` and `the officer is responsible for the act of the deputy` (one function for each of §§ 7.5, 7.6(a), 7.8 and 7.9(a)). was `not applicable` in pass 1 |
| Gov. Code § 7.6 | GOV-ss-1-26.txt:24 | encoded | `usca-deputies.l4`, section `Gov. Code § 7.6: officers whose offices the Constitution creates`: the functions listed against its subdivisions (a) to (e); subdivision (f) is a fork. was `not applicable` in pass 1 |
| Gov. Code § 7.6(a) | GOV-ss-1-26.txt:24 | encoded | `usca-deputies.l4`, section `Gov. Code § 7.6: officers whose offices the Constitution creates`: `Gov. Code § 7.6(a) lets the officer designate`; `a designated deputy may do the act in the officer's place` and `the officer is responsible for the act of the deputy` (one function for each of §§ 7.5, 7.6(a), 7.8 and 7.9(a)). was `not applicable` in pass 1 |
| Gov. Code § 7.6(b) | GOV-ss-1-26.txt:25 | encoded | `usca-deputies.l4`, section `Gov. Code § 7.6: officers whose offices the Constitution creates`: `Gov. Code § 7.6(b) lets the Lieutenant Governor designate`; `a deputy may not be appointed to act for the officer at meetings of` (the Senate, the Regents, the Trustees). was `not applicable` in pass 1 |
| Gov. Code § 7.6(c) | GOV-ss-1-26.txt:26 | encoded | `usca-deputies.l4`, section `Gov. Code § 7.6: officers whose offices the Constitution creates`: `Gov. Code § 7.6(c) lets the Chief Justice designate`. was `not applicable` in pass 1 |
| Gov. Code § 7.6(d) | GOV-ss-1-26.txt:27 | encoded | `usca-deputies.l4`, section `Gov. Code § 7.6: officers whose offices the Constitution creates`: `Gov. Code § 7.6(d) lets the Attorney General designate`; `a person designated by the Attorney General may act as presiding officer in the Attorney General's place`. was `not applicable` in pass 1 |
| Gov. Code § 7.6(e) | GOV-ss-1-26.txt:28 | encoded | `usca-deputies.l4`, section `Gov. Code § 7.6: officers whose offices the Constitution creates`: `Gov. Code § 7.6(e) lets the Superintendent of Public Instruction designate`; `a deputy may not be appointed to act for the officer at meetings of` (the State Board of Education, the Regents, the Trustees). was `not applicable` in pass 1 |
| Gov. Code § 7.6(f) | GOV-ss-1-26.txt:29 | fork | `usca-deputies.l4`, section `Gov. Code § 7.6: officers whose offices the Constitution creates`: `this many officers may be represented at a meeting of the State Lands Commission under Section 7.6`. fork F-7.6f: `officer subject to this section` and `deputy subject to this section` are read as an officer designating under § 7.6, so a director represented under § 7.5 or § 7.9 is not counted; was `not applicable` in pass 1 |
| Gov. Code § 7.7 | GOV-ss-1-26.txt:31 | encoded | `usca-deputies.l4`, section `Gov. Code § 7.7: saving of Section 7`: `the section affects or modifies Section 7`. was `not applicable` in pass 1 |
| Gov. Code § 7.8 | GOV-ss-1-26.txt:33 | fork | `usca-deputies.l4`, section `Gov. Code § 7.8: the State Allocation Board`: `Gov. Code § 7.8 lets the director designate`; `this many directors may be represented by deputies at a meeting under`; `more persons may represent the same director at a meeting under Section 7.8`; `a designated deputy may do the act in the officer's place` and `the officer is responsible for the act of the deputy` (one function for each of §§ 7.5, 7.6(a), 7.8 and 7.9(a)). fork F-7.8: `irrespective of whether there shall be more than one such person representing a director` is read as lifting § 7.5's limit of one director represented per meeting, at the State Allocation Board; whether several persons may represent the same director is refused; was `not applicable` in pass 1 |
| Gov. Code § 7.9 | GOV-ss-1-26.txt:35 | encoded | `usca-deputies.l4`, section `Gov. Code § 7.9 and § 7.9a: the Controller, the Treasurer, the Director of Finance and the Superintendent of Public Instruction`: the functions listed against its subdivisions (a) to (c). was `not applicable` in pass 1 |
| Gov. Code § 7.9(a) | GOV-ss-1-26.txt:35 | encoded | `usca-deputies.l4`, section `Gov. Code § 7.9 and § 7.9a: the Controller, the Treasurer, the Director of Finance and the Superintendent of Public Instruction`: `Gov. Code § 7.9(a) lets the officer designate`; `a designated deputy may do the act in the officer's place` and `the officer is responsible for the act of the deputy` (one function for each of §§ 7.5, 7.6(a), 7.8 and 7.9(a)). was `not applicable` in pass 1 |
| Gov. Code § 7.9(b) | GOV-ss-1-26.txt:36 | encoded | `usca-deputies.l4`, section `Gov. Code § 7.9 and § 7.9a: the Controller, the Treasurer, the Director of Finance and the Superintendent of Public Instruction`: `Gov. Code § 7.9(b) requires two employees of the officer to be classified as career executives`; `the career executive may be classified at`. was `not applicable` in pass 1 |
| Gov. Code § 7.9(c) | GOV-ss-1-26.txt:37 | encoded | `usca-deputies.l4`, section `Gov. Code § 7.9 and § 7.9a: the Controller, the Treasurer, the Director of Finance and the Superintendent of Public Instruction`: `a deputy may not be appointed to act for the officer at meetings of`, for the Superintendent of Public Instruction (the State Board of Education, the Regents, the Trustees). was `not applicable` in pass 1 |
| Gov. Code § 7.9a | GOV-ss-1-26.txt:39 | encoded | `usca-deputies.l4`, section `Gov. Code § 7.9 and § 7.9a: the Controller, the Treasurer, the Director of Finance and the Superintendent of Public Instruction`: `Gov. Code § 7.9a requires two more employees of the officer to be classified as career executives`; `the career executive may be classified at`. was `not applicable` in pass 1 |
| Gov. Code § 8 | GOV-ss-1-26.txt:41 | encoded | `usca-general-provisions.l4`: `a message is a writing`; `a notice, report, statement or record required or authorized by the Government Code is made as the code requires`; `the version of a document in two languages that has authority` |
| Gov. Code § 9 | GOV-ss-1-26.txt:43 | encoded | `usca-operation-of-statutes.l4`: `a reference to a portion of the Government Code or of another law of this State applies to its amendments and additions, whenever made` |
| Gov. Code § 10 | GOV-ss-1-26.txt:45 | encoded | `usca-canons-of-reading.l4`, section `Gov. Code § 10, Civ. Code § 14(b)(6), Code Civ. Proc. § 17(b)(9): section and subdivision`. was inert in pass 1 |
| Gov. Code § 10 term Section | GOV-ss-1-26.txt:45 | encoded | `usca-canons-of-reading.l4`, section `Gov. Code § 10, Civ. Code § 14(b)(6), Code Civ. Proc. § 17(b)(9): section and subdivision`. was inert in pass 1 |
| Gov. Code § 10 term Subdivision | GOV-ss-1-26.txt:45 | encoded | `usca-canons-of-reading.l4`, section `Gov. Code § 10, Civ. Code § 14(b)(6), Code Civ. Proc. § 17(b)(9): section and subdivision`. was inert in pass 1 |
| Gov. Code § 11 | GOV-ss-1-26.txt:47 | fork | `usca-canons-of-reading.l4`, section `Tense, gender and number: Gov. Code §§ 11-13, Civ. Code § 14(a), Code Civ. Proc. § 17(a)`: `a word used in the tense includes the tense, in`. fork F-tense: Gov. Code § 11 says the present tense includes the past and future and the future the present; Civ. Code § 14(a) and Code Civ. Proc. § 17(a) say the present includes the future and say nothing of the past; the function takes the code and refuses a pair of tenses the code does not mention; was inert in pass 1 |
| Gov. Code § 12 | GOV-ss-1-26.txt:49 | encoded | `usca-canons-of-reading.l4`, section `Tense, gender and number: Gov. Code §§ 11-13, Civ. Code § 14(a), Code Civ. Proc. § 17(a)`. was inert in pass 1 |
| Gov. Code § 12.2 | GOV-ss-1-26.txt:51 | encoded | `usca-definitions.l4`, section `The table of defined terms`. was inert in pass 1 |
| Gov. Code § 12.2 term Spouse | GOV-ss-1-26.txt:51 | encoded | `usca-definitions.l4`, section `The table of defined terms`. was inert in pass 1 |
| Gov. Code § 12.5 | GOV-ss-1-26.txt:53 | encoded | `usca-canons-of-reading.l4`, section `Gov. Code § 12.5 and § 24: the words man and workmen's compensation`; added after the independent test pass, `usca-further-asks.l4`: `the declaration of Gov. Code § 12.5 or § 24 is amendatory of existing law`. was inert in pass 1; the last sentence (declaratory, not amendatory) states a fact about the Act and creates no rule (inert reason 1), and since the independent test pass it can be asked: `the declaration of Gov. Code § 12.5 or § 24 is amendatory of existing law` is FALSE |
| Gov. Code § 13 | GOV-ss-1-26.txt:55 | encoded | `usca-canons-of-reading.l4`, section `Tense, gender and number: Gov. Code §§ 11-13, Civ. Code § 14(a), Code Civ. Proc. § 17(a)`. was inert in pass 1 |
| Gov. Code § 14 | GOV-ss-1-26.txt:57 | encoded | `usca-general-provisions.l4`: `the force of the word in the Government Code word`; added after the independent test pass, `usca-further-asks.l4`: `the force of the word as written in Gov. Code § 14` |
| Gov. Code § 15 | GOV-ss-1-26.txt:59 | encoded | `usca-definitions.l4`, section `The table of defined terms`. was inert in pass 1 |
| Gov. Code § 15 term Oath | GOV-ss-1-26.txt:59 | encoded | `usca-definitions.l4`, section `The table of defined terms`. was inert in pass 1 |
| Gov. Code § 16 | GOV-ss-1-26.txt:61 | encoded | `usca-general-provisions.l4`: `a mark is a signature or subscription`; `a signature by mark can be acknowledged or serve as the signature to a sworn statement` |
| Gov. Code § 16 term Signature | GOV-ss-1-26.txt:61 | encoded | `usca-general-provisions.l4`: a limb of Gov. Code § 16, whose functions are listed in its section row |
| Gov. Code § 16.5 | GOV-ss-1-26.txt:63 | encoded | `usca-general-provisions.l4`: `a digital signature has the same force and effect as a manual signature`; `a public entity is required to use or permit the use of a digital signature`; `Gov. Code § 16.5 applies to the digital signature`; added after the independent test pass, `usca-further-asks.l4`: `the latest date for the Secretary of State's initial regulations under Gov. Code § 16.5(a)(5)`; `the fewest public hearings the Secretary of State must hold before adopting the regulations under Gov. Code § 16.5(a)(5)`. subdivisions (d), (e) and (f) are in `usca-further-limbs.l4`, section `Gov. Code § 16.5(d), (e), (f): digital and electronic signatures` |
| Gov. Code § 16.5(a) | GOV-ss-1-26.txt:63 | encoded | `usca-general-provisions.l4`: a limb of Gov. Code § 16.5, whose functions are listed in its section row; added after the independent test pass, `usca-further-asks.l4`: `the latest date for the Secretary of State's initial regulations under Gov. Code § 16.5(a)(5)`; `the fewest public hearings the Secretary of State must hold before adopting the regulations under Gov. Code § 16.5(a)(5)`. the second to fourth sentences of (a)(5) (regulation timing, advice, hearing) are rule-making machinery (inert reason 2) and create no fact an individual supplies; the attribute itself is encoded, and since the independent test pass the latest date for the initial regulations (1 January 1997) and the fewest public hearings (one) can be asked |
| Gov. Code § 16.5(a)(1) | GOV-ss-1-26.txt:64 | encoded | `usca-general-provisions.l4`: a limb of Gov. Code § 16.5, whose functions are listed in its section row. the second to fourth sentences of (a)(5) (regulation timing, advice, hearing) are rule-making machinery (inert reason 2) and create no fact an individual supplies; the attribute itself is encoded, and since the independent test pass the latest date for the initial regulations (1 January 1997) and the fewest public hearings (one) can be asked |
| Gov. Code § 16.5(a)(2) | GOV-ss-1-26.txt:65 | encoded | `usca-general-provisions.l4`: a limb of Gov. Code § 16.5, whose functions are listed in its section row. the second to fourth sentences of (a)(5) (regulation timing, advice, hearing) are rule-making machinery (inert reason 2) and create no fact an individual supplies; the attribute itself is encoded, and since the independent test pass the latest date for the initial regulations (1 January 1997) and the fewest public hearings (one) can be asked |
| Gov. Code § 16.5(a)(3) | GOV-ss-1-26.txt:66 | encoded | `usca-general-provisions.l4`: a limb of Gov. Code § 16.5, whose functions are listed in its section row. the second to fourth sentences of (a)(5) (regulation timing, advice, hearing) are rule-making machinery (inert reason 2) and create no fact an individual supplies; the attribute itself is encoded, and since the independent test pass the latest date for the initial regulations (1 January 1997) and the fewest public hearings (one) can be asked |
| Gov. Code § 16.5(a)(4) | GOV-ss-1-26.txt:67 | encoded | `usca-general-provisions.l4`: a limb of Gov. Code § 16.5, whose functions are listed in its section row. the second to fourth sentences of (a)(5) (regulation timing, advice, hearing) are rule-making machinery (inert reason 2) and create no fact an individual supplies; the attribute itself is encoded, and since the independent test pass the latest date for the initial regulations (1 January 1997) and the fewest public hearings (one) can be asked |
| Gov. Code § 16.5(a)(5) | GOV-ss-1-26.txt:68 | encoded | `usca-general-provisions.l4`: a limb of Gov. Code § 16.5, whose functions are listed in its section row; added after the independent test pass, `usca-further-asks.l4`: `the latest date for the Secretary of State's initial regulations under Gov. Code § 16.5(a)(5)`; `the fewest public hearings the Secretary of State must hold before adopting the regulations under Gov. Code § 16.5(a)(5)`. the second to fourth sentences of (a)(5) (regulation timing, advice, hearing) are rule-making machinery (inert reason 2) and create no fact an individual supplies; the attribute itself is encoded, and since the independent test pass the latest date for the initial regulations (1 January 1997) and the fewest public hearings (one) can be asked |
| Gov. Code § 16.5(b) | GOV-ss-1-26.txt:69 | encoded | `usca-general-provisions.l4`: a limb of Gov. Code § 16.5, whose functions are listed in its section row. the second to fourth sentences of (a)(5) (regulation timing, advice, hearing) are rule-making machinery (inert reason 2) and create no fact an individual supplies; the attribute itself is encoded, and since the independent test pass the latest date for the initial regulations (1 January 1997) and the fewest public hearings (one) can be asked |
| Gov. Code § 16.5(c) | GOV-ss-1-26.txt:71 | encoded | `usca-general-provisions.l4`: a limb of Gov. Code § 16.5, whose functions are listed in its section row. the second to fourth sentences of (a)(5) (regulation timing, advice, hearing) are rule-making machinery (inert reason 2) and create no fact an individual supplies; the attribute itself is encoded, and since the independent test pass the latest date for the initial regulations (1 January 1997) and the fewest public hearings (one) can be asked |
| Gov. Code § 16.5(d) | GOV-ss-1-26.txt:72 | encoded | `usca-further-limbs.l4`, section `Gov. Code § 16.5(d), (e), (f): digital and electronic signatures`: `a digital signature in the sense of Gov. Code § 16.5(d)`; `it is an electronic signature for purposes of Gov. Code § 16.5`. pass 1 left (d)-(f) inert; the meaning of `electronic signature` is in Civil Code § 1633.2(h), not deposited |
| Gov. Code § 16.5(d) term Digital signature | GOV-ss-1-26.txt:72 | encoded | `usca-further-limbs.l4`, section `Gov. Code § 16.5(d), (e), (f): digital and electronic signatures`: `a digital signature in the sense of Gov. Code § 16.5(d)`; `it is an electronic signature for purposes of Gov. Code § 16.5`. pass 1 left (d)-(f) inert; the meaning of `electronic signature` is in Civil Code § 1633.2(h), not deposited |
| Gov. Code § 16.5(e) | GOV-ss-1-26.txt:73 | encoded | `usca-further-limbs.l4`, section `Gov. Code § 16.5(d), (e), (f): digital and electronic signatures`: `Gov. Code § 16.5 limits the right of a public entity or government agency to use and accept it`. pass 1 left (d)-(f) inert |
| Gov. Code § 16.5(f) | GOV-ss-1-26.txt:74 | encoded | `usca-further-limbs.l4`, section `Gov. Code § 16.5(d), (e), (f): digital and electronic signatures`: `the Secretary of State's regulations to implement Gov. Code § 16.5 apply to the use of`. pass 1 left (d)-(f) inert |
| Gov. Code § 17 | GOV-ss-1-26.txt:76 | encoded | `usca-definitions.l4`, section `The table of defined terms`. was inert in pass 1 |
| Gov. Code § 17 term Person | GOV-ss-1-26.txt:76 | encoded | `usca-definitions.l4`, section `The table of defined terms`. was inert in pass 1 |
| Gov. Code § 18 | GOV-ss-1-26.txt:78 | encoded | `usca-general-provisions.l4`: `the meaning of State in the Government Code` |
| Gov. Code § 18 term State | GOV-ss-1-26.txt:78 | encoded | `usca-general-provisions.l4`: a limb of Gov. Code § 18, whose functions are listed in its section row |
| Gov. Code § 19 | GOV-ss-1-26.txt:80 | encoded | `usca-definitions.l4`, section `The table of defined terms`. was inert in pass 1 |
| Gov. Code § 19 term County | GOV-ss-1-26.txt:80 | encoded | `usca-definitions.l4`, section `The table of defined terms`. was inert in pass 1 |
| Gov. Code § 20 | GOV-ss-1-26.txt:82 | encoded | `usca-definitions.l4`, section `The table of defined terms`. was inert in pass 1 |
| Gov. Code § 20 term City | GOV-ss-1-26.txt:82 | encoded | `usca-definitions.l4`, section `The table of defined terms`. was inert in pass 1 |
| Gov. Code § 21 | GOV-ss-1-26.txt:84 | encoded | `usca-definitions.l4`, section `The table of defined terms`. was inert in pass 1 |
| Gov. Code § 21 term Town | GOV-ss-1-26.txt:84 | encoded | `usca-definitions.l4`, section `The table of defined terms`. was inert in pass 1 |
| Gov. Code § 22 | GOV-ss-1-26.txt:86 | fork | `usca-definitions.l4`, section `Process: Gov. Code § 22, Code Civ. Proc. § 17(b)(7)`: `a document is process under Gov. Code § 22`. fork F-process: Gov. Code § 22 says process `includes` a writ or summons issued in a civil or criminal judicial proceeding (an open list, so anything else is refused); Code Civ. Proc. § 17(b)(7) says it `signifies` a writ or summons issued in a judicial proceeding and is read as closed; was inert in pass 1 |
| Gov. Code § 22 term Process | GOV-ss-1-26.txt:86 | fork | `usca-definitions.l4`, section `Process: Gov. Code § 22, Code Civ. Proc. § 17(b)(7)`: `a document is process under Gov. Code § 22`. fork F-process: Gov. Code § 22 says process `includes` a writ or summons issued in a civil or criminal judicial proceeding (an open list, so anything else is refused); Code Civ. Proc. § 17(b)(7) says it `signifies` a writ or summons issued in a judicial proceeding and is read as closed; was inert in pass 1 |
| Gov. Code § 23 | GOV-ss-1-26.txt:88 | encoded | `usca-canons-of-reading.l4`, section `Gov. Code § 23: severability`. was inert in pass 1 |
| Gov. Code § 24 | GOV-ss-1-26.txt:90 | encoded | `usca-canons-of-reading.l4`, section `Gov. Code § 12.5 and § 24: the words man and workmen's compensation`; added after the independent test pass, `usca-further-asks.l4`: `the declaration of Gov. Code § 12.5 or § 24 is amendatory of existing law`. was inert in pass 1; the last sentence is declaratory (inert reason 1), and since the independent test pass it can be asked: see Gov. Code § 12.5 |
| Gov. Code § 25 | GOV-ss-1-26.txt:92 | encoded | `usca-assessed-value.l4`: the functions listed against its subdivisions (a) to (c). section row; was `not applicable` in pass 1 |
| Gov. Code § 25(a) | GOV-ss-1-26.txt:92 | encoded | `usca-assessed-value.l4`, section `Gov. Code § 25(a): assessed value and the way tax rates are expressed`: `the percent of full value that assessed value is in the fiscal year`; `the assessed value of property whose full value is`; `the way tax rates are expressed in the fiscal year`. was `not applicable` in pass 1 |
| Gov. Code § 25(a) term assessed value | GOV-ss-1-26.txt:92 | encoded | `usca-assessed-value.l4`, section `Gov. Code § 25(a): assessed value and the way tax rates are expressed`: `the percent of full value that assessed value is in the fiscal year`; `the assessed value of property whose full value is`; `the way tax rates are expressed in the fiscal year`. was `not applicable` in pass 1 |
| Gov. Code § 25(b) | GOV-ss-1-26.txt:93 | encoded | `usca-assessed-value.l4`, section `Gov. Code § 25(b): comparisons for different years are made on the same basis`: `an amount of assessed value restated for comparison`; `a tax rate restated for comparison`. was `not applicable` in pass 1 |
| Gov. Code § 25(c) | GOV-ss-1-26.txt:94 | fork | `usca-assessed-value.l4`, section `Gov. Code § 25(c): the two conversion factors`: `a rate in dollars on each $100 of assessed value at a 25 percent assessment ratio, restated as comparable to a percentage of full value`; `a rate expressed as a percentage of full value, restated as comparable to dollars on each $100 of assessed value at a 25 percent assessment ratio`. fork F-25c: the two conversion factors are consistent only if a rate expressed as a percentage is read as a fraction (1 percent is 0.01), so 0.0025 times 400 is 1; was `not applicable` in pass 1 |
| Gov. Code § 26 | GOV-ss-1-26.txt:96 | encoded | `usca-definitions.l4`, section `Recycled water: Gov. Code § 26`. was inert in pass 1; the meaning is in Water Code § 13050(n), not deposited, so it is asked as an input |
| Gov. Code § 26 term recycled water | GOV-ss-1-26.txt:96 | encoded | `usca-definitions.l4`, section `Recycled water: Gov. Code § 26`. was inert in pass 1; the meaning is in Water Code § 13050(n), not deposited, so it is asked as an input |
| Gov. Code § 14 term shall | GOV-ss-1-26.txt (term in prose) | encoded | `usca-general-provisions.l4`: a limb of Gov. Code § 14, whose functions are listed in its section row |
| Gov. Code § 14 term may | GOV-ss-1-26.txt (term in prose) | encoded | `usca-general-provisions.l4`: a limb of Gov. Code § 14, whose functions are listed in its section row |
| Gov. Code § 11 term present tense | GOV-ss-1-26.txt (term in prose) | fork | `usca-canons-of-reading.l4`, section `Tense, gender and number: Gov. Code §§ 11-13, Civ. Code § 14(a), Code Civ. Proc. § 17(a)`: `a word used in the tense includes the tense, in`. fork F-tense: Gov. Code § 11 says the present tense includes the past and future and the future the present; Civ. Code § 14(a) and Code Civ. Proc. § 17(a) say the present includes the future and say nothing of the past; the function takes the code and refuses a pair of tenses the code does not mention; was inert in pass 1 |
| Gov. Code § 11 term future tense | GOV-ss-1-26.txt (term in prose) | fork | `usca-canons-of-reading.l4`, section `Tense, gender and number: Gov. Code §§ 11-13, Civ. Code § 14(a), Code Civ. Proc. § 17(a)`: `a word used in the tense includes the tense, in`. fork F-tense: Gov. Code § 11 says the present tense includes the past and future and the future the present; Civ. Code § 14(a) and Code Civ. Proc. § 17(a) say the present includes the future and say nothing of the past; the function takes the code and refuses a pair of tenses the code does not mention; was inert in pass 1 |
| Gov. Code § 12 term masculine gender | GOV-ss-1-26.txt (term in prose) | encoded | `usca-canons-of-reading.l4`, section `Tense, gender and number: Gov. Code §§ 11-13, Civ. Code § 14(a), Code Civ. Proc. § 17(a)`. was inert in pass 1 |
| Gov. Code § 13 term singular number | GOV-ss-1-26.txt (term in prose) | encoded | `usca-canons-of-reading.l4`, section `Tense, gender and number: Gov. Code §§ 11-13, Civ. Code § 14(a), Code Civ. Proc. § 17(a)`. was inert in pass 1 |
| Gov. Code § 13 term plural number | GOV-ss-1-26.txt (term in prose) | encoded | `usca-canons-of-reading.l4`, section `Tense, gender and number: Gov. Code §§ 11-13, Civ. Code § 14(a), Code Civ. Proc. § 17(a)`. was inert in pass 1 |
| Gov. Code § 6700 | GOV-ss-6700-6736.txt:8 | encoded | `usca-interpretation-time.l4`: `the section that says which days are holidays for kind`; `usca-holidays.l4`: `Gov. Code § 6700(a) fixes the day by the calendar d`; `Gov. Code § 6700(a)(3) makes the day a holiday d`; `Gov. Code § 6700(a)(7), as § 6701(c) qualifies it, makes the day a holiday supplied d` (and 5 more). subdivision (b), the memorandum of understanding, is in `usca-further-limbs.l4`, section `Gov. Code § 6700(b): a memorandum of understanding that conflicts with the holiday section` |
| Gov. Code § 6700(a) | GOV-ss-6700-6736.txt:8 | encoded | `usca-holidays.l4`: a limb of Gov. Code § 6700, whose functions are listed in its section row |
| Gov. Code § 6700(a)(1) | GOV-ss-6700-6736.txt:9 | encoded | `usca-holidays.l4`: a limb of Gov. Code § 6700, whose functions are listed in its section row |
| Gov. Code § 6700(a)(2) | GOV-ss-6700-6736.txt:10 | encoded | `usca-holidays.l4`: a limb of Gov. Code § 6700, whose functions are listed in its section row |
| Gov. Code § 6700(a)(3) | GOV-ss-6700-6736.txt:11 | encoded | `usca-holidays.l4`: a limb of Gov. Code § 6700, whose functions are listed in its section row |
| Gov. Code § 6700(a)(4) | GOV-ss-6700-6736.txt:12 | encoded | `usca-holidays.l4`: a limb of Gov. Code § 6700, whose functions are listed in its section row |
| Gov. Code § 6700(a)(5) | GOV-ss-6700-6736.txt:13 | encoded | `usca-holidays.l4`: a limb of Gov. Code § 6700, whose functions are listed in its section row |
| Gov. Code § 6700(a)(6) | GOV-ss-6700-6736.txt:14 | encoded | `usca-holidays.l4`: a limb of Gov. Code § 6700, whose functions are listed in its section row |
| Gov. Code § 6700(a)(7) | GOV-ss-6700-6736.txt:15 | encoded | `usca-holidays.l4`: a limb of Gov. Code § 6700, whose functions are listed in its section row |
| Gov. Code § 6700(a)(8) | GOV-ss-6700-6736.txt:16 | encoded | `usca-holidays.l4`: a limb of Gov. Code § 6700, whose functions are listed in its section row |
| Gov. Code § 6700(a)(9) | GOV-ss-6700-6736.txt:17 | encoded | `usca-holidays.l4`: a limb of Gov. Code § 6700, whose functions are listed in its section row |
| Gov. Code § 6700(a)(10) | GOV-ss-6700-6736.txt:18 | encoded | `usca-holidays.l4`: a limb of Gov. Code § 6700, whose functions are listed in its section row |
| Gov. Code § 6700(a)(11) | GOV-ss-6700-6736.txt:19 | encoded | `usca-holidays.l4`: a limb of Gov. Code § 6700, whose functions are listed in its section row |
| Gov. Code § 6700(a)(12) | GOV-ss-6700-6736.txt:20 | encoded | `usca-holidays.l4`: a limb of Gov. Code § 6700, whose functions are listed in its section row |
| Gov. Code § 6700(a)(13) | GOV-ss-6700-6736.txt:21 | encoded | `usca-holidays.l4`: a limb of Gov. Code § 6700, whose functions are listed in its section row |
| Gov. Code § 6700(a)(14) | GOV-ss-6700-6736.txt:22 | encoded | `usca-holidays.l4`: a limb of Gov. Code § 6700, whose functions are listed in its section row |
| Gov. Code § 6700(a)(15) | GOV-ss-6700-6736.txt:23 | encoded | `usca-holidays.l4`: a limb of Gov. Code § 6700, whose functions are listed in its section row |
| Gov. Code § 6700(a)(16) | GOV-ss-6700-6736.txt:24 | encoded | `usca-holidays.l4`: a limb of Gov. Code § 6700, whose functions are listed in its section row |
| Gov. Code § 6700(a)(17) | GOV-ss-6700-6736.txt:25 | encoded | `usca-holidays.l4`: a limb of Gov. Code § 6700, whose functions are listed in its section row |
| Gov. Code § 6700(a)(18) | GOV-ss-6700-6736.txt:26 | encoded | `usca-holidays.l4`: a limb of Gov. Code § 6700, whose functions are listed in its section row |
| Gov. Code § 6700(a)(19) | GOV-ss-6700-6736.txt:27 | encoded | `usca-holidays.l4`: a limb of Gov. Code § 6700, whose functions are listed in its section row |
| Gov. Code § 6700(a)(20) | GOV-ss-6700-6736.txt:28 | encoded | `usca-holidays.l4`: a limb of Gov. Code § 6700, whose functions are listed in its section row |
| Gov. Code § 6700(a)(20)(A) | GOV-ss-6700-6736.txt:28 | encoded | `usca-holidays.l4`: a limb of Gov. Code § 6700, whose functions are listed in its section row |
| Gov. Code § 6700(a)(20)(B) | GOV-ss-6700-6736.txt:29 | encoded | `usca-holidays.l4`: a limb of Gov. Code § 6700, whose functions are listed in its section row |
| Gov. Code § 6700(b) | GOV-ss-6700-6736.txt:31 | encoded | `usca-further-limbs.l4`, section `Gov. Code § 6700(b): a memorandum of understanding that conflicts with the holiday section`: `the memorandum of understanding controls over Gov. Code § 6700`; `further legislative action is needed before the memorandum of understanding controls`. pass 1 left (b) out |
| Gov. Code § 6701 | GOV-ss-6700-6736.txt:33 | encoded | `usca-holidays.l4`: `one of the days Gov. Code § 6701(a) names d`; `Gov. Code § 6701(a) or (b) makes the day a holiday d`; `Gov. Code § 6700(a)(7), as § 6701(c) qualifies it, makes the day a holiday supplied d`; `a holiday under Gov. Code § 6700 and § 6701 for the state supplied d` (and 2 more); added after the independent test pass, `usca-further-asks.l4`: `the days on which the Legislature may observe March 31 of the year`; `Gov. Code § 6701(c) lets the Legislature observe March 31 on the day`; `Gov. Code § 6701(d) lets the body provide an alternate day for a holiday falling on` |
| Gov. Code § 6701(a) | GOV-ss-6700-6736.txt:33 | encoded | `usca-holidays.l4`: a limb of Gov. Code § 6701, whose functions are listed in its section row |
| Gov. Code § 6701(b) | GOV-ss-6700-6736.txt:34 | encoded | `usca-holidays.l4`: a limb of Gov. Code § 6701, whose functions are listed in its section row |
| Gov. Code § 6701(c) | GOV-ss-6700-6736.txt:36 | fork | `usca-holidays.l4`: a limb of Gov. Code § 6701, whose functions are listed in its section row; added after the independent test pass, `usca-further-asks.l4`: `the days on which the Legislature may observe March 31 of the year`; `Gov. Code § 6701(c) lets the Legislature observe March 31 on the day`. fork F-6701c (the Legislature may observe March 31 on another day; does March 31 stay a holiday?) |
| Gov. Code § 6701(c)(1) | GOV-ss-6700-6736.txt:37 | encoded | `usca-holidays.l4`: a limb of Gov. Code § 6701, whose functions are listed in its section row; added after the independent test pass, `usca-further-asks.l4`: `the days on which the Legislature may observe March 31 of the year`; `Gov. Code § 6701(c) lets the Legislature observe March 31 on the day`. moved from `fork` after the independent test pass: the three days are computed as the text states them (`the days on which the Legislature may observe March 31 of the year`); the fork F-6701c belongs to paragraph (c) itself |
| Gov. Code § 6701(c)(2) | GOV-ss-6700-6736.txt:38 | encoded | `usca-holidays.l4`: a limb of Gov. Code § 6701, whose functions are listed in its section row; added after the independent test pass, `usca-further-asks.l4`: `the days on which the Legislature may observe March 31 of the year`; `Gov. Code § 6701(c) lets the Legislature observe March 31 on the day`. moved from `fork` after the independent test pass: the three days are computed as the text states them (`the days on which the Legislature may observe March 31 of the year`); the fork F-6701c belongs to paragraph (c) itself |
| Gov. Code § 6701(c)(3) | GOV-ss-6700-6736.txt:39 | encoded | `usca-holidays.l4`: a limb of Gov. Code § 6701, whose functions are listed in its section row; added after the independent test pass, `usca-further-asks.l4`: `the days on which the Legislature may observe March 31 of the year`; `Gov. Code § 6701(c) lets the Legislature observe March 31 on the day`. moved from `fork` after the independent test pass: the three days are computed as the text states them (`the days on which the Legislature may observe March 31 of the year`); the fork F-6701c belongs to paragraph (c) itself |
| Gov. Code § 6701(d) | GOV-ss-6700-6736.txt:40 | fork | `usca-holidays.l4`: a limb of Gov. Code § 6701, whose functions are listed in its section row; added after the independent test pass, `usca-further-asks.l4`: `Gov. Code § 6701(d) lets the body provide an alternate day for a holiday falling on`. fork F-6701d (a county's alternate day; does the Saturday stop being a holiday?) |
| Gov. Code § 6702 | GOV-ss-6700-6736.txt:43 | encoded | `usca-holidays.l4`: `the moment falls in the Saturday holiday of Gov. Code § 6702`; `legal process may be issued, filed, served, executed or recorded in the Saturday holiday of Gov. Code § 6702`; `public offices of a city are closed on the day under Gov. Code § 6702`. the third sentence is fork F-6702city, answered in the same section row |
| Gov. Code § 6703 | GOV-ss-6700-6736.txt:45 | encoded | `usca-holidays.l4`: `Gov. Code § 6703 requires public offices of the state to be closed on the day d`; `the day is a closure day under Code Civ. Proc. § 12b supplied d`; added after the independent test pass, `usca-further-asks.l4`: `Gov. Code § 6703 requires the body to be closed on the day` |
| Gov. Code § 6703(a) | GOV-ss-6700-6736.txt:45 | encoded | `usca-holidays.l4`: a limb of Gov. Code § 6703, whose functions are listed in its section row; added after the independent test pass, `usca-further-asks.l4`: `Gov. Code § 6703 requires the body to be closed on the day` |
| Gov. Code § 6703(b) | GOV-ss-6700-6736.txt:46 | encoded | `usca-holidays.l4`: a limb of Gov. Code § 6703, whose functions are listed in its section row; added after the independent test pass, `usca-further-asks.l4`: `Gov. Code § 6703 requires the body to be closed on the day`. the last sentence (the intent that the University of California also be closed on Veterans Day) is an intent clause with no rule (inert reason 1); since the independent test pass it can be asked: `Gov. Code § 6703 requires the body to be closed on the day` is FALSE for the University of California on Veterans Day |
| Gov. Code § 6704 | GOV-ss-6700-6736.txt:49 | encoded | `usca-holidays.l4`: `a Saturday is a holiday for the public offices of a city or district under Gov. Code § 6704`; added after the independent test pass, `usca-further-asks.l4`: `Gov. Code § 6704 gives the body the power to make every Saturday a holiday for its public offices`; `Gov. Code § 6704 requires provision for the continuance of essential public services such as police and fire protection` |
| Gov. Code § 6705 | GOV-ss-6700-6736.txt:51 | encoded | `usca-holidays.l4`: `courts and public offices are open on a special or limited holiday appointed by the President or Governor`; added after the independent test pass, `usca-further-asks.l4`: `a holiday is a special or limited holiday under Gov. Code § 6705`; `Gov. Code § 6705 has a contract performed and business transacted as usual by the party on a special or limited holiday` |
| Gov. Code § 6706 | GOV-ss-6700-6736.txt:55 | encoded | `usca-interpretation-time.l4`: `the latest day on which an act appointed for`; added after the independent test pass, `usca-further-asks.l4`: `Gov. Code § 6706 applies to an act appointed to be performed on a particular day by`; `Gov. Code § 6706 requires the act to be performed on the next business day` |
| Gov. Code § 6707 | GOV-ss-6700-6736.txt:57 | encoded | `usca-interpretation-time.l4`: `the latest day for filing with a state agency, when the last day is`; added after the independent test pass, `usca-further-asks.l4`: `Gov. Code § 6707 gives the next business day for a filing with` |
| Gov. Code § 6708 | GOV-ss-6700-6736.txt:59 | fork | `usca-proclaimed-days.l4`, section `The days the Governor is directed to proclaim: Gov. Code §§ 6708-6736`. fork F-proclaim-once: these four sections say `shall proclaim` without `annually`, so the text does not say whether the duty recurs each year; the function refuses for a year after the first; was `not applicable` in pass 1 |
| Gov. Code § 6709 | GOV-ss-6700-6736.txt:61 | fork | `usca-proclaimed-days.l4`, section `The days the Governor is directed to proclaim: Gov. Code §§ 6708-6736`. fork F-proclaim-once: these four sections say `shall proclaim` without `annually`, so the text does not say whether the duty recurs each year; the function refuses for a year after the first; was `not applicable` in pass 1 |
| Gov. Code § 6710 | GOV-ss-6700-6736.txt:63 | fork | `usca-proclaimed-days.l4`, section `The days the Governor is directed to proclaim: Gov. Code §§ 6708-6736`. fork F-proclaim-once: these four sections say `shall proclaim` without `annually`, so the text does not say whether the duty recurs each year; the function refuses for a year after the first; was `not applicable` in pass 1 |
| Gov. Code § 6711 | GOV-ss-6700-6736.txt:65 | fork | `usca-proclaimed-days.l4`, section `The days the Governor is directed to proclaim: Gov. Code §§ 6708-6736`. fork F-proclaim-once: these four sections say `shall proclaim` without `annually`, so the text does not say whether the duty recurs each year; the function refuses for a year after the first; was `not applicable` in pass 1 |
| Gov. Code § 6712 | GOV-ss-6700-6736.txt:67 | encoded | `usca-proclaimed-days.l4`, section `The days the Governor is directed to proclaim: Gov. Code §§ 6708-6736`. was `not applicable` in pass 1; whether a proclaimed day is a holiday is fork F-hol-6, answered by a refusal in `a proclamation under the section makes the day a holiday` |
| Gov. Code § 6713 | GOV-ss-6700-6736.txt:69 | encoded | `usca-proclaimed-days.l4`, section `The days the Governor is directed to proclaim: Gov. Code §§ 6708-6736`. was `not applicable` in pass 1; whether a proclaimed day is a holiday is fork F-hol-6, answered by a refusal in `a proclamation under the section makes the day a holiday` |
| Gov. Code § 6714 | GOV-ss-6700-6736.txt:71 | encoded | `usca-proclaimed-days.l4`, section `The days the Governor is directed to proclaim: Gov. Code §§ 6708-6736`. was `not applicable` in pass 1; whether a proclaimed day is a holiday is fork F-hol-6, answered by a refusal in `a proclamation under the section makes the day a holiday` |
| Gov. Code § 6715 | GOV-ss-6700-6736.txt:73 | encoded | `usca-proclaimed-days.l4`, section `The days the Governor is directed to proclaim: Gov. Code §§ 6708-6736`. was `not applicable` in pass 1; whether a proclaimed day is a holiday is fork F-hol-6, answered by a refusal in `a proclamation under the section makes the day a holiday` |
| Gov. Code § 6716 | GOV-ss-6700-6736.txt:75 | encoded | `usca-proclaimed-days.l4`, section `The days the Governor is directed to proclaim: Gov. Code §§ 6708-6736`. was `not applicable` in pass 1; whether a proclaimed day is a holiday is fork F-hol-6, answered by a refusal in `a proclamation under the section makes the day a holiday` |
| Gov. Code § 6717 | GOV-ss-6700-6736.txt:77 | encoded | `usca-proclaimed-days.l4`, section `The days the Governor is directed to proclaim: Gov. Code §§ 6708-6736`. was `not applicable` in pass 1; whether a proclaimed day is a holiday is fork F-hol-6, answered by a refusal in `a proclamation under the section makes the day a holiday` |
| Gov. Code § 6718 | GOV-ss-6700-6736.txt:79 | encoded | `usca-proclaimed-days.l4`, section `The days the Governor is directed to proclaim: Gov. Code §§ 6708-6736`. was `not applicable` in pass 1; whether a proclaimed day is a holiday is fork F-hol-6, answered by a refusal in `a proclamation under the section makes the day a holiday` |
| Gov. Code § 6719 | GOV-ss-6700-6736.txt:81 | encoded | `usca-proclaimed-days.l4`, section `The days the Governor is directed to proclaim: Gov. Code §§ 6708-6736`. was `not applicable` in pass 1; whether a proclaimed day is a holiday is fork F-hol-6, answered by a refusal in `a proclamation under the section makes the day a holiday` |
| Gov. Code § 6720 | GOV-ss-6700-6736.txt:83 | fork | `usca-proclaimed-days.l4`, section `The days the Governor is directed to proclaim: Gov. Code §§ 6708-6736`: `the days the Governor is directed to proclaim under`. fork F-6720: when April 24 is itself a Sunday the text does not say whether that day is `the Sunday before` it, so the period is refused for such a year; whether the day is a holiday is fork F-hol-6; was `not applicable` in pass 1 |
| Gov. Code § 6721 | GOV-ss-6700-6736.txt:86 | encoded | `usca-proclaimed-days.l4`, section `The days the Governor is directed to proclaim: Gov. Code §§ 6708-6736`. was `not applicable` in pass 1; whether a proclaimed day is a holiday is fork F-hol-6, answered by a refusal in `a proclamation under the section makes the day a holiday` |
| Gov. Code § 6722 | GOV-ss-6700-6736.txt:88 | encoded | `usca-proclaimed-days.l4`, section `The days the Governor is directed to proclaim: Gov. Code §§ 6708-6736`. was `not applicable` in pass 1; whether a proclaimed day is a holiday is fork F-hol-6, answered by a refusal in `a proclamation under the section makes the day a holiday` |
| Gov. Code § 6723 | GOV-ss-6700-6736.txt:90 | encoded | `usca-proclaimed-days.l4`, section `The days the Governor is directed to proclaim: Gov. Code §§ 6708-6736`. was `not applicable` in pass 1; whether a proclaimed day is a holiday is fork F-hol-6, answered by a refusal in `a proclamation under the section makes the day a holiday` |
| Gov. Code § 6724 | GOV-ss-6700-6736.txt:92 | encoded | `usca-proclaimed-days.l4`, section `The days the Governor is directed to proclaim: Gov. Code §§ 6708-6736`. was `not applicable` in pass 1; whether a proclaimed day is a holiday is fork F-hol-6, answered by a refusal in `a proclamation under the section makes the day a holiday` |
| Gov. Code § 6725 | GOV-ss-6700-6736.txt:94 | encoded | `usca-proclaimed-days.l4`, section `The days the Governor is directed to proclaim: Gov. Code §§ 6708-6736`. was `not applicable` in pass 1; whether a proclaimed day is a holiday is fork F-hol-6, answered by a refusal in `a proclamation under the section makes the day a holiday` |
| Gov. Code § 6726 | GOV-ss-6700-6736.txt:96 | encoded | `usca-proclaimed-days.l4`, section `Gov. Code § 6726: Space Day`: `a school, educational institution, resident, business or public entity is required to take part in Space Day`. was `not applicable` in pass 1; the day itself (the first Friday in May) is in the table of proclamations |
| Gov. Code § 6726(a) | GOV-ss-6700-6736.txt:96 | encoded | `usca-proclaimed-days.l4`, section `Gov. Code § 6726: Space Day`: `a school, educational institution, resident, business or public entity is required to take part in Space Day`. was `not applicable` in pass 1; the day itself (the first Friday in May) is in the table of proclamations |
| Gov. Code § 6726(b) | GOV-ss-6700-6736.txt:97 | fork | `usca-proclaimed-days.l4`, section `Gov. Code § 6726: Space Day`: `the moment falls in the lights-out hour of Space Day` (and, for (d), `the Governor is to direct the Department of General Services to turn off the light on Space Day`). fork F-between: `between 9 p.m. and 10 p.m.` does not say whether the instants of 9 p.m. and 10 p.m. are inside, so the function refuses at those two instants; for (d) an essential light is also refused; was `not applicable` in pass 1 |
| Gov. Code § 6726(c) | GOV-ss-6700-6736.txt:99 | inert | 1 (a purpose clause: Space Day shall promote space observation and appreciation, the aerospace industry and careers in science; it creates no rule) |
| Gov. Code § 6726(d) | GOV-ss-6700-6736.txt:100 | fork | `usca-proclaimed-days.l4`, section `Gov. Code § 6726: Space Day`: `the moment falls in the lights-out hour of Space Day` (and, for (d), `the Governor is to direct the Department of General Services to turn off the light on Space Day`). fork F-between: `between 9 p.m. and 10 p.m.` does not say whether the instants of 9 p.m. and 10 p.m. are inside, so the function refuses at those two instants; for (d) an essential light is also refused; was `not applicable` in pass 1 |
| Gov. Code § 6727 | GOV-ss-6700-6736.txt:102 | encoded | `usca-proclaimed-days.l4`, section `The days the Governor is directed to proclaim: Gov. Code §§ 6708-6736`. was `not applicable` in pass 1; whether a proclaimed day is a holiday is fork F-hol-6, answered by a refusal in `a proclamation under the section makes the day a holiday` |
| Gov. Code § 6728 | GOV-ss-6700-6736.txt:104 | encoded | `usca-proclaimed-days.l4`, section `The days the Governor is directed to proclaim: Gov. Code §§ 6708-6736`. was `not applicable` in pass 1; whether a proclaimed day is a holiday is fork F-hol-6, answered by a refusal in `a proclamation under the section makes the day a holiday` |
| Gov. Code § 6729 | GOV-ss-6700-6736.txt:106 | encoded | `usca-proclaimed-days.l4`, section `The days the Governor is directed to proclaim: Gov. Code §§ 6708-6736`. was `not applicable` in pass 1; whether a proclaimed day is a holiday is fork F-hol-6, answered by a refusal in `a proclamation under the section makes the day a holiday` |
| Gov. Code § 6731 | GOV-ss-6700-6736.txt:108 | encoded | `usca-proclaimed-days.l4`, section `The days the Governor is directed to proclaim: Gov. Code §§ 6708-6736`: `Gov. Code § 6731: California Farmworker Day` (the day, August 26, and the annual duty of subdivision (b)). was `not applicable` in pass 1 |
| Gov. Code § 6731(a) | GOV-ss-6700-6736.txt:108 | encoded | `usca-proclaimed-days.l4`, section `The days the Governor is directed to proclaim: Gov. Code §§ 6708-6736`: `Gov. Code § 6731: California Farmworker Day` (the day, August 26, and the annual duty of subdivision (b)). was `not applicable` in pass 1 |
| Gov. Code § 6731(b) | GOV-ss-6700-6736.txt:109 | encoded | `usca-proclaimed-days.l4`, section `The days the Governor is directed to proclaim: Gov. Code §§ 6708-6736`: `Gov. Code § 6731: California Farmworker Day` (the day, August 26, and the annual duty of subdivision (b)). was `not applicable` in pass 1 |
| Gov. Code § 6733 | GOV-ss-6700-6736.txt:111 | encoded | `usca-proclaimed-days.l4`, section `The days the Governor is directed to proclaim: Gov. Code §§ 6708-6736`. was `not applicable` in pass 1; whether a proclaimed day is a holiday is fork F-hol-6, answered by a refusal in `a proclamation under the section makes the day a holiday` |
| Gov. Code § 6735 | GOV-ss-6700-6736.txt:113 | encoded | `usca-proclaimed-days.l4`, section `The days the Governor is directed to proclaim: Gov. Code §§ 6708-6736`. was `not applicable` in pass 1; whether a proclaimed day is a holiday is fork F-hol-6, answered by a refusal in `a proclamation under the section makes the day a holiday` |
| Gov. Code § 6736 | GOV-ss-6700-6736.txt:115 | encoded | `usca-proclaimed-days.l4`, section `The days the Governor is directed to proclaim: Gov. Code §§ 6708-6736`. was `not applicable` in pass 1; whether a proclaimed day is a holiday is fork F-hol-6, answered by a refusal in `a proclamation under the section makes the day a holiday` |
| Gov. Code § 6705 term special or limited holiday | GOV-ss-6700-6736.txt (term in prose) | encoded | `usca-holidays.l4`: a limb of Gov. Code § 6705, whose functions are listed in its section row; added after the independent test pass, `usca-further-asks.l4`: `a holiday is a special or limited holiday under Gov. Code § 6705`; `Gov. Code § 6705 has a contract performed and business transacted as usual by the party on a special or limited holiday` |
| Gov. Code § 6800 | GOV-ss-6800-6808.txt:8 | fork | `usca-interpretation-time.l4`: `before the rest-day rule, the last day of n days counted from firstDay`; `before the rest-day rule, the last day of n months counted from firstDay`; `last day of a count of units in which the leap-day pair counts once`; `with a holiday last day also excluded, once holiday d` (and 5 more). forks F-from, F-contract, F-run, F-direction, F-unit: the text does not say what the first day is, whether the rule reaches a contract, whether a holiday last day moves on once or runs on, which way it moves, or whether it applies to months and years; the headline function takes the run reading, `with a holiday last day also excluded, once` is the other |
| Gov. Code § 6801 | GOV-ss-6800-6808.txt:10 | encoded | `usca-interpretation-time.l4`: `is a leap year under section 6802 year`; added after the independent test pass, `usca-further-asks.l4`: `Gov. Code § 6801 computes time according to the Gregorian calendar`. plus the new-year limb in `usca-further-limbs.l4`, section `Gov. Code § 6801: January 1 is the first day of the year`: `the day reckoned as the first day of the year` |
| Gov. Code § 6802 | GOV-ss-6800-6808.txt:12 | encoded | `usca-interpretation-time.l4`: `is a leap year under section 6802 year`; added after the independent test pass, `usca-further-asks.l4`: `days in the year under Gov. Code § 6802` |
| Gov. Code § 6803 | GOV-ss-6800-6808.txt:14 | fork | `usca-interpretation-time.l4`: `leap-day pair of the year lies in the period`; `count of leap-day pairs in the period`; `day number on which a count of units ends`; `last day of a count of units in which the leap-day pair counts once` (and 7 more). forks F-year and F-pair: a year is 365 days exactly, and the leap-day pair is read literally (the headline) or purposively (a separate function) |
| Gov. Code § 6803 term Year | GOV-ss-6800-6808.txt:14 | fork | `usca-interpretation-time.l4`: a limb of Gov. Code § 6803, whose functions are listed in its section row. forks F-year and F-pair: a year is 365 days exactly, and the leap-day pair is read literally (the headline) or purposively (a separate function) |
| Gov. Code § 6804 | GOV-ss-6800-6808.txt:16 | fork | `usca-interpretation-time.l4`: `before the rest-day rule, the last day of n months counted from firstDay`; `the section that defines month for kind`; added after the independent test pass, `usca-further-asks.l4`: `Gov. Code § 6804 gives the word month the meaning of a calendar month`. fork F-month: the text says only `a calendar month`, so a start on the 29th, 30th or 31st that reaches a shorter month is refused |
| Gov. Code § 6804 term Month | GOV-ss-6800-6808.txt:16 | fork | `usca-interpretation-time.l4`: a limb of Gov. Code § 6804, whose functions are listed in its section row; added after the independent test pass, `usca-further-asks.l4`: `Gov. Code § 6804 gives the word month the meaning of a calendar month`. fork F-month: the text says only `a calendar month`, so a start on the 29th, 30th or 31st that reaches a shorter month is refused |
| Gov. Code § 6805 | GOV-ss-6800-6808.txt:18 | encoded | `usca-interpretation-time.l4`: `before the rest-day rule, the last day of n weeks counted from firstDay`; `days in a week under section 6805` |
| Gov. Code § 6806 | GOV-ss-6800-6808.txt:20 | encoded | `usca-interpretation-time.l4`: `the midnight that begins the day d`; `the midnight that ends the day d`; `the moment m falls within the day d`; `the moment a statute goes into effect enactment` (and 3 more) |
| Gov. Code § 6807 | GOV-ss-6800-6808.txt:22 | encoded | `usca-interpretation-time.l4`: `the part of the day at t given sunrise at sunrise and sunset at sunset` |
| Gov. Code § 6808 | GOV-ss-6800-6808.txt:24 | encoded | `usca-interpretation-time.l4`: `the second Sunday of March of y`; `the first Sunday of November of y`; `daylight saving time at a clock reading on the day it commences secs`; `daylight saving time at a clock reading on the day it ends secs` (and 2 more). subdivisions (a) and (c) are in `usca-further-limbs.l4`, section `Gov. Code § 6808(a) and (c): the standard time and the power to amend` |
| Gov. Code § 6808(a) | GOV-ss-6800-6808.txt:24 | encoded | `usca-further-limbs.l4`, section `Gov. Code § 6808(a) and (c): the standard time and the power to amend`: `the standard time within the state is that of`; the offset from Coordinated Universal Time is refused because 15 U.S.C. §§ 261 and 263 are not deposited. pass 1 left (a) out |
| Gov. Code § 6808(b) | GOV-ss-6800-6808.txt:25 | encoded | `usca-interpretation-time.l4`: a limb of Gov. Code § 6808, whose functions are listed in its section row; added after the independent test pass, `usca-further-asks.l4`: `the clock reading, in seconds after midnight, at which daylight saving time begins and ends under Gov. Code § 6808(b)` |
| Gov. Code § 6808(c) | GOV-ss-6800-6808.txt:26 | encoded | `usca-further-limbs.l4`, section `Gov. Code § 6808(a) and (c): the standard time and the power to amend`: `Gov. Code § 6808(c) lets the Legislature make the amendment`. pass 1 left (c) out |
| Gov. Code § 6803 term half year | GOV-ss-6800-6808.txt (term in prose) | fork | `usca-interpretation-time.l4`: a limb of Gov. Code § 6803, whose functions are listed in its section row. forks F-year and F-pair: a year is 365 days exactly, and the leap-day pair is read literally (the headline) or purposively (a separate function) |
| Gov. Code § 6803 term quarter of a year | GOV-ss-6800-6808.txt (term in prose) | fork | `usca-interpretation-time.l4`: a limb of Gov. Code § 6803, whose functions are listed in its section row. forks F-year and F-pair: a year is 365 days exactly, and the leap-day pair is read literally (the headline) or purposively (a separate function) |
| Gov. Code § 6805 term week | GOV-ss-6800-6808.txt (term in prose) | encoded | `usca-interpretation-time.l4`: a limb of Gov. Code § 6805, whose functions are listed in its section row |
| Gov. Code § 6806 term day | GOV-ss-6800-6808.txt (term in prose) | encoded | `usca-interpretation-time.l4`: a limb of Gov. Code § 6806, whose functions are listed in its section row |
| Gov. Code § 6807 term Daytime | GOV-ss-6800-6808.txt (term in prose) | encoded | `usca-interpretation-time.l4`: a limb of Gov. Code § 6807, whose functions are listed in its section row |
| Gov. Code § 6807 term Nighttime | GOV-ss-6800-6808.txt (term in prose) | encoded | `usca-interpretation-time.l4`: a limb of Gov. Code § 6807, whose functions are listed in its section row |
| Gov. Code § 9600 | GOV-ss-9600-9612.txt:8 | encoded | `usca-interpretation-time.l4`: `a statute is of a kind that goes into effect immediately upon its enactment enactment`; `the day a regular-session statute goes into effect when enacted on dayOfEnactment`; `the day a special-session statute goes into effect, the special session having adjourned on`; `the day a statute goes into effect enactment` (and 6 more) |
| Gov. Code § 9600(a) | GOV-ss-9600-9612.txt:8 | fork | `usca-interpretation-time.l4`: a limb of Gov. Code § 9600, whose functions are listed in its section row. forks F-commence, F-enactment, F-own-day, F-moment: counting the 90-day period, what the date of enactment is, whether a statute may name its own day, and the moment within the day |
| Gov. Code § 9600(b) | GOV-ss-9600-9612.txt:9 | encoded | `usca-interpretation-time.l4`: a limb of Gov. Code § 9600, whose functions are listed in its section row |
| Gov. Code § 9602 | GOV-ss-9600-9612.txt:11 | encoded | `usca-interpretation-time.l4`: `the moment a concurrent or joint resolution takes effect, having been filed with the Secretary of State at`; `the day silent subordinate legislation comes into force, when made on madeOn`; added after the independent test pass, `usca-further-asks.l4`: `a concurrent or joint resolution is in effect at the moment` |
| Gov. Code § 9603 | GOV-ss-9600-9612.txt:13 | encoded | `usca-canons-of-reading.l4`, section `Gov. Code § 9603: where the general rules are`. was inert in pass 1 |
| Gov. Code § 9604 | GOV-ss-9600-9612.txt:15 | encoded | `usca-operation-of-statutes.l4`: `Gov. Code § 9604 deems a reference to be a reference to the restatements and continuations`; added after the independent test pass, `usca-further-asks.l4`: `Gov. Code § 9604 applies to a reference made by` |
| Gov. Code § 9605 | GOV-ss-9600-9612.txt:17 | encoded | `usca-operation-of-statutes.l4`: `the day a provision of an amended section is considered to have been enacted`; `the day a provision of an amended section is considered to have been repealed`; `a portion stands after successive acts of one session amend the same section`; `the statute that prevails when two statutes of one session amend the same section first second`; added after the independent test pass, `usca-further-asks.l4`: `Gov. Code § 9605(b) makes the presumption conclusive` |
| Gov. Code § 9605(a) | GOV-ss-9600-9612.txt:17 | encoded | `usca-operation-of-statutes.l4`: a limb of Gov. Code § 9605, whose functions are listed in its section row |
| Gov. Code § 9605(a)(1) | GOV-ss-9600-9612.txt:17 | encoded | `usca-operation-of-statutes.l4`: a limb of Gov. Code § 9605, whose functions are listed in its section row |
| Gov. Code § 9605(a)(2) | GOV-ss-9600-9612.txt:18 | encoded | `usca-operation-of-statutes.l4`: a limb of Gov. Code § 9605, whose functions are listed in its section row |
| Gov. Code § 9605(b) | GOV-ss-9600-9612.txt:20 | fork | `usca-operation-of-statutes.l4`: a limb of Gov. Code § 9605, whose functions are listed in its section row; added after the independent test pass, `usca-further-asks.l4`: `Gov. Code § 9605(b) makes the presumption conclusive`. fork F-9605b: the text does not rank the presumption of (b)(1) (`conclusively presumed`) against that of (b)(2) (`presumed`) when they point at different statutes, so the function refuses; for two statutes of the same order of enactment (b)(1) has no statute enacted last and (b)(2) decides |
| Gov. Code § 9605(b)(1) | GOV-ss-9600-9612.txt:21 | fork | `usca-operation-of-statutes.l4`: a limb of Gov. Code § 9605, whose functions are listed in its section row; added after the independent test pass, `usca-further-asks.l4`: `Gov. Code § 9605(b) makes the presumption conclusive`. fork F-9605b: the text does not rank the presumption of (b)(1) (`conclusively presumed`) against that of (b)(2) (`presumed`) when they point at different statutes, so the function refuses; for two statutes of the same order of enactment (b)(1) has no statute enacted last and (b)(2) decides |
| Gov. Code § 9605(b)(2) | GOV-ss-9600-9612.txt:22 | fork | `usca-operation-of-statutes.l4`: a limb of Gov. Code § 9605, whose functions are listed in its section row; added after the independent test pass, `usca-further-asks.l4`: `Gov. Code § 9605(b) makes the presumption conclusive`. fork F-9605b: the text does not rank the presumption of (b)(1) (`conclusively presumed`) against that of (b)(2) (`presumed`) when they point at different statutes, so the function refuses; for two statutes of the same order of enactment (b)(1) has no statute enacted last and (b)(2) decides |
| Gov. Code § 9606 | GOV-ss-9600-9612.txt:25 | encoded | `usca-operation-of-statutes.l4`: `a statute may be repealed vested rights would be impaired`. the second sentence is in `usca-further-limbs.l4`, section `Gov. Code § 9606: acting in contemplation of repeal`: `the person acts in contemplation of the power of repeal` |
| Gov. Code § 9607 | GOV-ss-9600-9612.txt:27 | encoded | `usca-operation-of-statutes.l4`: `a repealed statute is revived by the repeal of the statute that repealed it`; `the day a terminated or repealed law is revived by a later statute chaptered on`; added after the independent test pass, `usca-further-asks.l4`: `Gov. Code § 9607(b) revives the terminated or repealed law` |
| Gov. Code § 9607(a) | GOV-ss-9600-9612.txt:27 | encoded | `usca-operation-of-statutes.l4`: a limb of Gov. Code § 9607, whose functions are listed in its section row |
| Gov. Code § 9607(b) | GOV-ss-9600-9612.txt:28 | fork | `usca-operation-of-statutes.l4`: a limb of Gov. Code § 9607, whose functions are listed in its section row; added after the independent test pass, `usca-further-asks.l4`: `Gov. Code § 9607(b) revives the terminated or repealed law`. fork F-9607b: whether the date of termination is the last day the law operates or the first day it does not |
| Gov. Code § 9608 | GOV-ss-9600-9612.txt:30 | encoded | `usca-operation-of-statutes.l4`: `the termination or suspension of a criminal law bars indictment, information and punishment`; added after the independent test pass, `usca-further-asks.l4`: `Gov. Code § 9608 leaves an act already committed open to proceedings and punishment after the law ends` |
| Gov. Code § 9609 | GOV-ss-9600-9612.txt:32 | encoded | `usca-operation-of-statutes.l4`: `Gov. Code § 9609 makes a statute amending a section of a repealed statute void` |
| Gov. Code § 9610 | GOV-ss-9600-9612.txt:34 | encoded | `usca-operation-of-statutes.l4`: `a statute fixing the salary of a State officer or employee is an appropriation of money for it`; `the salary fixed by statute shall be paid`; added after the independent test pass, `usca-further-asks.l4`: `Gov. Code § 9610 makes the salary fixed by statute payable only if moneys are made available by another provision of law` |
| Gov. Code § 9611 | GOV-ss-9600-9612.txt:36 | fork | `usca-operation-of-statutes.l4`: `a law temporarily suspended or modified is deemed repealed`; `the original provision has its full force again on the day`; added after the independent test pass, `usca-further-asks.l4`: `Gov. Code § 9611 keeps the original provision from being deemed repealed`. fork F-9611: on which day the original provision resumes |
| Gov. Code § 9612 | GOV-ss-9600-9612.txt:38 | encoded | `usca-general-provisions.l4`: `a term in a statute is deemed to include the United States Air Force` |
| Civ. Code § 1 | CIV-ss-1-23.6.txt:8 | inert | 1 (title and enacting words: names the Act and lists its four divisions) |
| Civ. Code § 1 item I | CIV-ss-1-23.6.txt:9 | inert | 1 (title and enacting words: names the Act and lists its four divisions) |
| Civ. Code § 1 item II | CIV-ss-1-23.6.txt:10 | inert | 1 (title and enacting words: names the Act and lists its four divisions) |
| Civ. Code § 1 item III | CIV-ss-1-23.6.txt:11 | inert | 1 (title and enacting words: names the Act and lists its four divisions) |
| Civ. Code § 1 item IV | CIV-ss-1-23.6.txt:12 | inert | 1 (title and enacting words: names the Act and lists its four divisions) |
| Civ. Code § 2 | CIV-ss-1-23.6.txt:14 | encoded | `usca-interpretation-time.l4`: `the moment the Civil Code takes effect` |
| Civ. Code § 3 | CIV-ss-1-23.6.txt:16 | encoded | `usca-operation-of-statutes.l4`: `a part of the Civil Code or the Code of Civil Procedure is retroactive`; added after the independent test pass, `usca-further-asks.l4`: `the code says that no part of it is retroactive unless expressly so declared` |
| Civ. Code § 4 | CIV-ss-1-23.6.txt:18 | encoded | `usca-canons-of-reading.l4`, section `Strict and liberal construction: Civ. Code § 4, Code Civ. Proc. § 4`. was inert in pass 1 |
| Civ. Code § 5 | CIV-ss-1-23.6.txt:20 | encoded | `usca-operation-of-statutes.l4`: `the section construes a provision of` |
| Civ. Code § 6 | CIV-ss-1-23.6.txt:22 | encoded | `usca-operation-of-statutes.l4`: `the section protects an action, proceeding or accrued right from the code` |
| Civ. Code § 7 | CIV-ss-1-23.6.txt:24 | encoded | `usca-interpretation-time.l4`: `the section that says which days are holidays for kind`; `usca-holidays.l4`: `a holiday under Civ. Code § 7 supplied d`; `the day is a holiday within the meaning of a provision of kind kind supplied d` |
| Civ. Code § 7.1 | CIV-ss-1-23.6.txt:26 | encoded | `usca-holidays.l4`: `an optional bank holiday under Civ. Code § 7.1 supplied d`; `the moment falls in the Good Friday optional bank holiday of Civ. Code § 7.1(o)` |
| Civ. Code § 7.1(a) | CIV-ss-1-23.6.txt:27 | encoded | `usca-holidays.l4`: a limb of Civ. Code § 7.1, whose functions are listed in its section row |
| Civ. Code § 7.1(b) | CIV-ss-1-23.6.txt:28 | encoded | `usca-holidays.l4`: a limb of Civ. Code § 7.1, whose functions are listed in its section row |
| Civ. Code § 7.1(c) | CIV-ss-1-23.6.txt:29 | encoded | `usca-holidays.l4`: a limb of Civ. Code § 7.1, whose functions are listed in its section row |
| Civ. Code § 7.1(d) | CIV-ss-1-23.6.txt:30 | encoded | `usca-holidays.l4`: a limb of Civ. Code § 7.1, whose functions are listed in its section row |
| Civ. Code § 7.1(e) | CIV-ss-1-23.6.txt:31 | encoded | `usca-holidays.l4`: a limb of Civ. Code § 7.1, whose functions are listed in its section row |
| Civ. Code § 7.1(f) | CIV-ss-1-23.6.txt:32 | encoded | `usca-holidays.l4`: a limb of Civ. Code § 7.1, whose functions are listed in its section row |
| Civ. Code § 7.1(g) | CIV-ss-1-23.6.txt:33 | encoded | `usca-holidays.l4`: a limb of Civ. Code § 7.1, whose functions are listed in its section row |
| Civ. Code § 7.1(h) | CIV-ss-1-23.6.txt:34 | encoded | `usca-holidays.l4`: a limb of Civ. Code § 7.1, whose functions are listed in its section row |
| Civ. Code § 7.1(i) | CIV-ss-1-23.6.txt:35 | encoded | `usca-holidays.l4`: a limb of Civ. Code § 7.1, whose functions are listed in its section row |
| Civ. Code § 7.1(j) | CIV-ss-1-23.6.txt:36 | encoded | `usca-holidays.l4`: a limb of Civ. Code § 7.1, whose functions are listed in its section row |
| Civ. Code § 7.1(k) | CIV-ss-1-23.6.txt:37 | encoded | `usca-holidays.l4`: a limb of Civ. Code § 7.1, whose functions are listed in its section row |
| Civ. Code § 7.1(l) | CIV-ss-1-23.6.txt:38 | encoded | `usca-holidays.l4`: a limb of Civ. Code § 7.1, whose functions are listed in its section row |
| Civ. Code § 7.1(m) | CIV-ss-1-23.6.txt:39 | encoded | `usca-holidays.l4`: a limb of Civ. Code § 7.1, whose functions are listed in its section row |
| Civ. Code § 7.1(n) | CIV-ss-1-23.6.txt:40 | encoded | `usca-holidays.l4`: a limb of Civ. Code § 7.1, whose functions are listed in its section row |
| Civ. Code § 7.1(o) | CIV-ss-1-23.6.txt:41 | encoded | `usca-holidays.l4`: a limb of Civ. Code § 7.1, whose functions are listed in its section row |
| Civ. Code § 7.1(p) | CIV-ss-1-23.6.txt:42 | encoded | `usca-holidays.l4`: a limb of Civ. Code § 7.1, whose functions are listed in its section row |
| Civ. Code § 7.1(q) | CIV-ss-1-23.6.txt:43 | encoded | `usca-holidays.l4`: a limb of Civ. Code § 7.1, whose functions are listed in its section row |
| Civ. Code § 7.1(r) | CIV-ss-1-23.6.txt:44 | encoded | `usca-holidays.l4`: a limb of Civ. Code § 7.1, whose functions are listed in its section row |
| Civ. Code § 9 | CIV-ss-1-23.6.txt:46 | encoded | `usca-holidays.l4`: `a business day under Civ. Code § 9 supplied d`; `a business day under Civ. Code § 9 for an act to be performed through a bank supplied d`; `an act appointed for an optional bank holiday may be performed on that day itself`; `the next business day after an optional bank holiday on which an act was appointed for a bank` |
| Civ. Code § 10 | CIV-ss-1-23.6.txt:49 | fork | `usca-interpretation-time.l4`: `before the rest-day rule, the last day of n days counted from firstDay`; `with a holiday last day also excluded, once holiday d`; `the last day of a period of`; `the date d falls inside the period after firstDay through lastDay`. forks F-from, F-contract, F-run, F-direction, F-unit: the text does not say what the first day is, whether the rule reaches a contract, whether a holiday last day moves on once or runs on, which way it moves, or whether it applies to months and years; the headline function takes the run reading, `with a holiday last day also excluded, once` is the other |
| Civ. Code § 11 | CIV-ss-1-23.6.txt:51 | encoded | `usca-interpretation-time.l4`: `the latest day on which an act appointed for` |
| Civ. Code § 12 | CIV-ss-1-23.6.txt:53 | encoded | `usca-general-provisions.l4`: `a joint authority may be exercised by those acting` |
| Civ. Code § 13 | CIV-ss-1-23.6.txt:55 | encoded | `usca-canons-of-reading.l4`, section `Words and phrases: Civ. Code § 13, Code Civ. Proc. § 16`. was inert in pass 1 |
| Civ. Code § 14 | CIV-ss-1-23.6.txt:57 | encoded | `usca-interpretation-time.l4`: `the section that defines month for kind`; `usca-general-provisions.l4`: `a mark is a signature or subscription`; `a signature by mark can be acknowledged or serve as the signature to a sworn statement`. section row; the limbs are in the rows below |
| Civ. Code § 14(a) | CIV-ss-1-23.6.txt:57 | encoded | `usca-canons-of-reading.l4`, section `Tense, gender and number: Gov. Code §§ 11-13, Civ. Code § 14(a), Code Civ. Proc. § 17(a)`. the person, county, writing, oath, testify, depose and signature limbs are in the definitions module and the general-provisions module; pass 1 left them inert |
| Civ. Code § 14(b) | CIV-ss-1-23.6.txt:59 | encoded | `usca-definitions.l4`, section `The table of defined terms`; added after the independent test pass, `usca-further-asks.l4`: `Civ. Code § 14(b) and Code Civ. Proc. § 17(b) give the word the signification they state`; `a signification stated in Civ. Code § 14(b) or Code Civ. Proc. § 17(b) is displaced`. pass 1 left these limbs inert |
| Civ. Code § 14(b)(1) | CIV-ss-1-23.6.txt:60 | encoded | `usca-definitions.l4`, section `The table of defined terms`. pass 1 left these limbs inert |
| Civ. Code § 14(b)(1) term property | CIV-ss-1-23.6.txt:60 | encoded | `usca-definitions.l4`, section `The table of defined terms`. pass 1 left these limbs inert |
| Civ. Code § 14(b)(2) | CIV-ss-1-23.6.txt:61 | encoded | `usca-definitions.l4`, section `The table of defined terms`. pass 1 left these limbs inert |
| Civ. Code § 14(b)(2) term real property | CIV-ss-1-23.6.txt:61 | encoded | `usca-definitions.l4`, section `The table of defined terms`. pass 1 left these limbs inert |
| Civ. Code § 14(b)(3) | CIV-ss-1-23.6.txt:63 | encoded | `usca-definitions.l4`, section `The table of defined terms`. pass 1 left these limbs inert |
| Civ. Code § 14(b)(3) term personal property | CIV-ss-1-23.6.txt:63 | encoded | `usca-definitions.l4`, section `The table of defined terms`. pass 1 left these limbs inert |
| Civ. Code § 14(b)(4) | CIV-ss-1-23.6.txt:64 | fork | `usca-interpretation-time.l4`: a limb of Civ. Code § 14, whose functions are listed in its section row; added after the independent test pass, `usca-further-asks.l4`: `Gov. Code § 6804 gives the word month the meaning of a calendar month`. fork F-month: the text says only `a calendar month`, so a start on the 29th, 30th or 31st that reaches a shorter month is refused |
| Civ. Code § 14(b)(4) term month | CIV-ss-1-23.6.txt:64 | fork | `usca-interpretation-time.l4`: a limb of Civ. Code § 14, whose functions are listed in its section row; added after the independent test pass, `usca-further-asks.l4`: `Gov. Code § 6804 gives the word month the meaning of a calendar month`. fork F-month: the text says only `a calendar month`, so a start on the 29th, 30th or 31st that reaches a shorter month is refused |
| Civ. Code § 14(b)(5) | CIV-ss-1-23.6.txt:65 | encoded | `usca-definitions.l4`, section `The table of defined terms`. pass 1 left these limbs inert |
| Civ. Code § 14(b)(5) term will | CIV-ss-1-23.6.txt:65 | encoded | `usca-definitions.l4`, section `The table of defined terms`. pass 1 left these limbs inert |
| Civ. Code § 14(b)(6) | CIV-ss-1-23.6.txt:66 | encoded | `usca-canons-of-reading.l4`, section `Gov. Code § 10, Civ. Code § 14(b)(6), Code Civ. Proc. § 17(b)(9): section and subdivision`. pass 1 left this limb inert |
| Civ. Code § 14(b)(6) term section | CIV-ss-1-23.6.txt:66 | encoded | `usca-canons-of-reading.l4`, section `Gov. Code § 10, Civ. Code § 14(b)(6), Code Civ. Proc. § 17(b)(9): section and subdivision`. pass 1 left this limb inert |
| Civ. Code § 14(b)(7) | CIV-ss-1-23.6.txt:67 | encoded | `usca-definitions.l4`, section `The table of defined terms`. pass 1 left these limbs inert |
| Civ. Code § 14(b)(7) term spouse | CIV-ss-1-23.6.txt:67 | encoded | `usca-definitions.l4`, section `The table of defined terms`. pass 1 left these limbs inert |
| Civ. Code § 17 | CIV-ss-1-23.6.txt:69 | encoded | `usca-general-provisions.l4`: `a requirement of the Civil Code or the Code of Civil Procedure that a notice be mailed by registered mail is met by`; `the day service by mail is deemed made, the document having been mailed on`; `the day a notice is deemed given, the notice having been sent on the day the notice is sent`; added after the independent test pass, `usca-further-asks.l4`: `a requirement of the Civil Code that a notice be mailed by certified mail is met by` |
| Civ. Code § 18 | CIV-ss-1-23.6.txt:71 | encoded | `usca-general-provisions.l4`: `a person has actual notice of a fact the person has express information of the fact`; `a person has constructive notice of a fact the law imputes the fact to the person` |
| Civ. Code § 18 item 1 | CIV-ss-1-23.6.txt:72 | encoded | `usca-general-provisions.l4`: a limb of Civ. Code § 18, whose functions are listed in its section row |
| Civ. Code § 18 item 2 | CIV-ss-1-23.6.txt:73 | encoded | `usca-general-provisions.l4`: a limb of Civ. Code § 18, whose functions are listed in its section row |
| Civ. Code § 19 | CIV-ss-1-23.6.txt:75 | encoded | `usca-general-provisions.l4`: `a person has constructive notice of the fact itself under Civ. Code § 19` |
| Civ. Code § 20 | CIV-ss-1-23.6.txt:77 | encoded | `usca-operation-of-statutes.l4`: `an earlier statute, law or rule remains in force`; `the repeal by the code revives a former law that was repealed before`; added after the independent test pass, `usca-further-asks.l4`: `the repeal by the Civil Code affects a private statute` |
| Civ. Code § 21 | CIV-ss-1-23.6.txt:80 | inert | 2 (short title: how the Act may be cited) |
| Civ. Code § 22 | CIV-ss-1-23.6.txt:82 | fork | `usca-canons-of-reading.l4`, section `Civ. Code § 22 and § 22.1: law and the will of the supreme power`. fork F-22: `Law is a solemn expression of the will of the supreme power of the State` is read as a definition, so an expression is a law only if it is both; was inert in pass 1 |
| Civ. Code § 22.1 | CIV-ss-1-23.6.txt:84 | encoded | `usca-canons-of-reading.l4`, section `Civ. Code § 22 and § 22.1: law and the will of the supreme power`. was inert in pass 1 |
| Civ. Code § 22.1(a) | CIV-ss-1-23.6.txt:85 | encoded | `usca-canons-of-reading.l4`, section `Civ. Code § 22 and § 22.1: law and the will of the supreme power`. was inert in pass 1 |
| Civ. Code § 22.1(b) | CIV-ss-1-23.6.txt:86 | encoded | `usca-canons-of-reading.l4`, section `Civ. Code § 22 and § 22.1: law and the will of the supreme power`. was inert in pass 1 |
| Civ. Code § 22.2 | CIV-ss-1-23.6.txt:88 | encoded | `usca-operation-of-statutes.l4`: `the common law of England is the rule of decision`; added after the independent test pass, `usca-further-asks.l4`: `Civ. Code § 22.2 makes the law of England the rule of decision in the courts of this State` |
| Civ. Code § 23 | CIV-ss-1-23.6.txt:90 | encoded | `usca-operation-of-statutes.l4`: `the day each of the four 1872 codes is construed as having been passed` |
| Civ. Code § 23.1 | CIV-ss-1-23.6.txt:92 | encoded | `usca-operation-of-statutes.l4`: `Civ. Code § 23.1 makes the provision of a law passed at the 1872 session prevail over the code provision` |
| Civ. Code § 23.2 | CIV-ss-1-23.6.txt:94 | encoded | `usca-operation-of-statutes.l4`: `one of the four 1872 codes prevails over another by having been passed later` |
| Civ. Code § 23.3 | CIV-ss-1-23.6.txt:96 | encoded | `usca-operation-of-statutes.l4`: `the provision that prevails when units conflict unit matter` |
| Civ. Code § 23.4 | CIV-ss-1-23.6.txt:98 | encoded | `usca-operation-of-statutes.l4`: `the provision that prevails when units conflict unit matter` |
| Civ. Code § 23.5 | CIV-ss-1-23.6.txt:100 | encoded | `usca-operation-of-statutes.l4`: `the provision that prevails when units conflict unit matter` |
| Civ. Code § 23.6 | CIV-ss-1-23.6.txt:102 | fork | `usca-operation-of-statutes.l4`: `the section that prevails, the first being`; added after the independent test pass, `usca-further-asks.l4`: `Civ. Code § 23.6 makes the section last in numerical order prevail`. fork F-23.6: sections numbered with a letter have no numerical place, and an inconsistent construction is not resolved by the text |
| Civ. Code § 7 term holidays within the meaning of the code | CIV-ss-1-23.6.txt (term in prose) | encoded | `usca-holidays.l4`: a limb of Civ. Code § 7, whose functions are listed in its section row |
| Civ. Code § 18 term actual notice | CIV-ss-1-23.6.txt (term in prose) | encoded | `usca-general-provisions.l4`: a limb of Civ. Code § 18, whose functions are listed in its section row |
| Civ. Code § 18 term constructive notice | CIV-ss-1-23.6.txt (term in prose) | encoded | `usca-general-provisions.l4`: a limb of Civ. Code § 18, whose functions are listed in its section row |
| Civ. Code § 22 term law | CIV-ss-1-23.6.txt (term in prose) | fork | `usca-canons-of-reading.l4`, section `Civ. Code § 22 and § 22.1: law and the will of the supreme power`. fork F-22: `Law is a solemn expression of the will of the supreme power of the State` is read as a definition, so an expression is a law only if it is both; was inert in pass 1 |
| Civ. Code § 14 term (a) present tense | CIV-ss-1-23.6.txt (term in prose) | fork | `usca-canons-of-reading.l4`, section `Tense, gender and number: Gov. Code §§ 11-13, Civ. Code § 14(a), Code Civ. Proc. § 17(a)`: `a word used in the tense includes the tense, in`. fork F-tense: this code says the present tense includes the future and nothing of the past; was inert in pass 1 |
| Civ. Code § 14 term (a) masculine gender | CIV-ss-1-23.6.txt (term in prose) | encoded | `usca-canons-of-reading.l4`, section `Tense, gender and number: Gov. Code §§ 11-13, Civ. Code § 14(a), Code Civ. Proc. § 17(a)` |
| Civ. Code § 14 term (a) singular number | CIV-ss-1-23.6.txt (term in prose) | encoded | `usca-canons-of-reading.l4`, section `Tense, gender and number: Gov. Code §§ 11-13, Civ. Code § 14(a), Code Civ. Proc. § 17(a)` |
| Civ. Code § 14 term (a) plural number | CIV-ss-1-23.6.txt (term in prose) | encoded | `usca-canons-of-reading.l4`, section `Tense, gender and number: Gov. Code §§ 11-13, Civ. Code § 14(a), Code Civ. Proc. § 17(a)` |
| Civ. Code § 14 term (a) person | CIV-ss-1-23.6.txt (term in prose) | encoded | `usca-definitions.l4`, section `The table of defined terms` |
| Civ. Code § 14 term (a) county | CIV-ss-1-23.6.txt (term in prose) | encoded | `usca-definitions.l4`, section `The table of defined terms` |
| Civ. Code § 14 term (a) writing | CIV-ss-1-23.6.txt (term in prose) | encoded | `usca-definitions.l4`, section `The table of defined terms` |
| Civ. Code § 14 term (a) oath | CIV-ss-1-23.6.txt (term in prose) | encoded | `usca-definitions.l4`, section `The table of defined terms` |
| Civ. Code § 14 term (a) testify | CIV-ss-1-23.6.txt (term in prose) | encoded | `usca-definitions.l4`, section `Testify and depose: Civ. Code § 14(a), Code Civ. Proc. § 17(b)(5)` |
| Civ. Code § 14 term (a) depose | CIV-ss-1-23.6.txt (term in prose) | encoded | `usca-definitions.l4`, section `Testify and depose: Civ. Code § 14(a), Code Civ. Proc. § 17(b)(5)` |
| Civ. Code § 14 term (a) signature or subscription | CIV-ss-1-23.6.txt (term in prose) | encoded | `usca-interpretation-time.l4`: a limb of Civ. Code § 14, whose functions are listed in its section row. `a mark is a signature or subscription` in `usca-general-provisions.l4` |
| Code Civ. Proc. § 1 | CCP-ss-1-34.txt:8 | inert | 1 (title and enacting words: names the Act and lists its four parts) |
| Code Civ. Proc. § 1 item I | CCP-ss-1-34.txt:9 | inert | 1 (title and enacting words: names the Act and lists its four parts) |
| Code Civ. Proc. § 1 item II | CCP-ss-1-34.txt:10 | inert | 1 (title and enacting words: names the Act and lists its four parts) |
| Code Civ. Proc. § 1 item III | CCP-ss-1-34.txt:11 | inert | 1 (title and enacting words: names the Act and lists its four parts) |
| Code Civ. Proc. § 1 item IV | CCP-ss-1-34.txt:12 | inert | 1 (title and enacting words: names the Act and lists its four parts) |
| Code Civ. Proc. § 2 | CCP-ss-1-34.txt:14 | encoded | `usca-interpretation-time.l4`: `the moment the Code of Civil Procedure takes effect` |
| Code Civ. Proc. § 3 | CCP-ss-1-34.txt:16 | encoded | `usca-operation-of-statutes.l4`: `a part of the Civil Code or the Code of Civil Procedure is retroactive`; added after the independent test pass, `usca-further-asks.l4`: `the code says that no part of it is retroactive unless expressly so declared` |
| Code Civ. Proc. § 4 | CCP-ss-1-34.txt:18 | encoded | `usca-canons-of-reading.l4`, section `Strict and liberal construction: Civ. Code § 4, Code Civ. Proc. § 4`. was inert in pass 1 |
| Code Civ. Proc. § 5 | CCP-ss-1-34.txt:20 | encoded | `usca-operation-of-statutes.l4`: `the section construes a provision of` |
| Code Civ. Proc. § 6 | CCP-ss-1-34.txt:22 | encoded | `usca-operation-of-statutes.l4`: `a holder of an office under a repealed Act continues to hold it under Code Civ. Proc. § 6 and § 7` |
| Code Civ. Proc. § 7 | CCP-ss-1-34.txt:24 | encoded | `usca-operation-of-statutes.l4`: `a holder of an office under a repealed Act continues to hold it under Code Civ. Proc. § 6 and § 7` |
| Code Civ. Proc. § 8 | CCP-ss-1-34.txt:26 | encoded | `usca-operation-of-statutes.l4`: `the section protects an action, proceeding or accrued right from the code`; `procedure taken after the code took effect in a proceeding begun before must conform to the code` |
| Code Civ. Proc. § 9 | CCP-ss-1-34.txt:28 | fork | `usca-operation-of-statutes.l4`: `days left of a limitation that began to run before the code took effect`; added after the independent test pass, `usca-further-asks.l4`: `Code Civ. Proc. § 9 deems the time already run part of the time the code prescribes`. fork F-ccp9: whether the days already run are counted with or without the day the code took effect |
| Code Civ. Proc. § 10 | CCP-ss-1-34.txt:30 | encoded | `usca-interpretation-time.l4`: `the section that says which days are holidays for kind`; `usca-holidays.l4`: `a holiday under Code Civ. Proc. § 10 supplied d`; `a holiday for computing time under Code Civ. Proc. § 12 supplied d`; `a holiday for the extension of Code Civ. Proc. § 12a(a), taking in the Sundays of § 10 supplied d` (and 1 more); added after the independent test pass, `usca-further-asks.l4`: `a holiday under Code Civ. Proc. § 10, the Section 135 days being`; `the days supplied, with the Section 135 days stated as` |
| Code Civ. Proc. § 11 | CCP-ss-1-34.txt:32 | encoded | `usca-general-provisions.l4`: `a requirement of the Civil Code or the Code of Civil Procedure that a notice be mailed by registered mail is met by`; `the day service by mail is deemed made, the document having been mailed on`; `the day a notice is deemed given, the notice having been sent on the day the notice is sent` |
| Code Civ. Proc. § 12 | CCP-ss-1-34.txt:34 | fork | `usca-interpretation-time.l4`: `before the rest-day rule, the last day of n days counted from firstDay`; `with a holiday last day also excluded, once holiday d`; `the last day of a period of`; `the date d falls inside the period after firstDay through lastDay` (and 1 more); added after the independent test pass, `usca-further-asks.l4`: `a holiday for computing time under Code Civ. Proc. § 12, the Section 135 days being`. forks F-from, F-contract, F-run, F-direction, F-unit: the text does not say what the first day is, whether the rule reaches a contract, whether a holiday last day moves on once or runs on, which way it moves, or whether it applies to months and years; the headline function takes the run reading, `with a holiday last day also excluded, once` is the other |
| Code Civ. Proc. § 12a | CCP-ss-1-34.txt:36 | encoded | `usca-interpretation-time.l4`: `next day from the date that is not a holiday, counting days so far holiday d daysSoFar`; `extended to the next day that is not a holiday holiday d`; `the last day of a period of n u counted from firstDay under the calendar holiday`; `the date d falls inside a period of n u counted from firstDay under the calendar holiday` (and 5 more); added after the independent test pass, `usca-further-asks.l4`: `Code Civ. Proc. § 12a applies to a period fixed by`; added after the independent test pass, `usca-further-asks.l4`: `a holiday for the extension of Code Civ. Proc. § 12a(a), read literally, the Section 135 days being`; `a holiday for the extension of Code Civ. Proc. § 12a(a), taking in the Sundays of § 10, the Section 135 days being` |
| Code Civ. Proc. § 12a(a) | CCP-ss-1-34.txt:36 | fork | `usca-interpretation-time.l4`: a limb of Code Civ. Proc. § 12a, whose functions are listed in its section row. forks F-holiday and F-run: whether Sundays are holidays for the extension (the text names Saturdays and the § 135 days only), and whether the extension runs past several holidays |
| Code Civ. Proc. § 12a(a) term holiday | CCP-ss-1-34.txt:36 | encoded | `usca-interpretation-time.l4`: a limb of Code Civ. Proc. § 12a, whose functions are listed in its section row |
| Code Civ. Proc. § 12a(b) | CCP-ss-1-34.txt:37 | encoded | `usca-interpretation-time.l4`: a limb of Code Civ. Proc. § 12a, whose functions are listed in its section row; added after the independent test pass, `usca-further-asks.l4`: `Code Civ. Proc. § 12a applies to a period fixed by` |
| Code Civ. Proc. § 12b | CCP-ss-1-34.txt:40 | encoded | `usca-holidays.l4`: `the day is a closure day under Code Civ. Proc. § 12b supplied d`; `a holiday for computing time under Code Civ. Proc. § 12 supplied d`; added after the independent test pass, `usca-further-asks.l4`: `Code Civ. Proc. § 12b makes the day a holiday for computing time when the office is closed for the whole of it`; `Code Civ. Proc. § 12b applies to the computation of time under` |
| Code Civ. Proc. § 12c | CCP-ss-1-34.txt:42 | fork | `usca-interpretation-time.l4`: `the last day to act, when the act is due`; `usca-general-provisions.l4`: `the day service by mail is deemed made, the document having been mailed on`; `the day a notice is deemed given, the notice having been sent on the day the notice is sent`. fork F-backward: the text does not say which way a backward-counted last day on a holiday moves, so the function refuses |
| Code Civ. Proc. § 12c(a) | CCP-ss-1-34.txt:42 | fork | `usca-interpretation-time.l4`: a limb of Code Civ. Proc. § 12c, whose functions are listed in its section row. fork F-backward: the text does not say which way a backward-counted last day on a holiday moves, so the function refuses |
| Code Civ. Proc. § 12c(b) | CCP-ss-1-34.txt:43 | fork | `usca-interpretation-time.l4`: a limb of Code Civ. Proc. § 12c, whose functions are listed in its section row. fork F-backward: the text does not say which way a backward-counted last day on a holiday moves, so the function refuses |
| Code Civ. Proc. § 13 | CCP-ss-1-34.txt:46 | encoded | `usca-interpretation-time.l4`: `the latest day on which an act appointed for` |
| Code Civ. Proc. § 13a | CCP-ss-1-34.txt:48 | encoded | `usca-interpretation-time.l4`: `an act required by law on a day or within a period may be performed on kind`; added after the independent test pass, `usca-further-asks.l4`: `Code Civ. Proc. § 13a or § 13b requires an act to be performed on` |
| Code Civ. Proc. § 13b | CCP-ss-1-34.txt:50 | encoded | `usca-interpretation-time.l4`: `an act required by law on a day or within a period may be performed on kind`; added after the independent test pass, `usca-further-asks.l4`: `Code Civ. Proc. § 13a or § 13b requires an act to be performed on` |
| Code Civ. Proc. § 14 | CCP-ss-1-34.txt:52 | encoded | `usca-definitions.l4`, section `The table of defined terms`. was inert in pass 1 |
| Code Civ. Proc. § 14 term seal | CCP-ss-1-34.txt:52 | encoded | `usca-definitions.l4`, section `The table of defined terms`. was inert in pass 1 |
| Code Civ. Proc. § 15 | CCP-ss-1-34.txt:54 | encoded | `usca-general-provisions.l4`: `a joint authority may be exercised by those acting` |
| Code Civ. Proc. § 16 | CCP-ss-1-34.txt:56 | encoded | `usca-canons-of-reading.l4`, section `Words and phrases: Civ. Code § 13, Code Civ. Proc. § 16`. was inert in pass 1 |
| Code Civ. Proc. § 17 | CCP-ss-1-34.txt:58 | encoded | `usca-interpretation-time.l4`: `the section that defines month for kind`; `usca-general-provisions.l4`: `a mark is a signature or subscription`; `a signature by mark can be acknowledged or serve as the signature to a sworn statement`; `a thing is an electronic signature`. section row; the limbs are in the rows below |
| Code Civ. Proc. § 17(a) | CCP-ss-1-34.txt:58 | encoded | `usca-canons-of-reading.l4`, section `Tense, gender and number: Gov. Code §§ 11-13, Civ. Code § 14(a), Code Civ. Proc. § 17(a)` |
| Code Civ. Proc. § 17(b) | CCP-ss-1-34.txt:59 | encoded | `usca-interpretation-time.l4`: a limb of Code Civ. Proc. § 17, whose functions are listed in its section row; added after the independent test pass, `usca-further-asks.l4`: `Civ. Code § 14(b) and Code Civ. Proc. § 17(b) give the word the signification they state`; `a signification stated in Civ. Code § 14(b) or Code Civ. Proc. § 17(b) is displaced`. section row; the limbs are in the rows below |
| Code Civ. Proc. § 17(b)(1) | CCP-ss-1-34.txt:61 | encoded | `usca-definitions.l4`, section `Affinity: Code Civ. Proc. § 17(b)(1)`. pass 1 left these limbs inert |
| Code Civ. Proc. § 17(b)(1) term Affinity | CCP-ss-1-34.txt:61 | encoded | `usca-definitions.l4`, section `Affinity: Code Civ. Proc. § 17(b)(1)`. pass 1 left these limbs inert |
| Code Civ. Proc. § 17(b)(2) | CCP-ss-1-34.txt:62 | encoded | `usca-definitions.l4`, section `The table of defined terms`. pass 1 left these limbs inert |
| Code Civ. Proc. § 17(b)(2) term County | CCP-ss-1-34.txt:62 | encoded | `usca-definitions.l4`, section `The table of defined terms`. pass 1 left these limbs inert |
| Code Civ. Proc. § 17(b)(3) | CCP-ss-1-34.txt:63 | encoded | `usca-general-provisions.l4`: `a thing is an electronic signature` |
| Code Civ. Proc. § 17(b)(3) term Electronic signature | CCP-ss-1-34.txt:63 | encoded | `usca-general-provisions.l4`: `a thing is an electronic signature` |
| Code Civ. Proc. § 17(b)(4) | CCP-ss-1-34.txt:64 | fork | `usca-interpretation-time.l4`: a limb of Code Civ. Proc. § 17, whose functions are listed in its section row; added after the independent test pass, `usca-further-asks.l4`: `Gov. Code § 6804 gives the word month the meaning of a calendar month`. fork F-month: the text says only `a calendar month`, so a start on the 29th, 30th or 31st that reaches a shorter month is refused |
| Code Civ. Proc. § 17(b)(4) term Month | CCP-ss-1-34.txt:64 | fork | `usca-interpretation-time.l4`: a limb of Code Civ. Proc. § 17, whose functions are listed in its section row; added after the independent test pass, `usca-further-asks.l4`: `Gov. Code § 6804 gives the word month the meaning of a calendar month`. fork F-month: the text says only `a calendar month`, so a start on the 29th, 30th or 31st that reaches a shorter month is refused |
| Code Civ. Proc. § 17(b)(5) | CCP-ss-1-34.txt:65 | encoded | `usca-definitions.l4`, section `The table of defined terms`. pass 1 left these limbs inert |
| Code Civ. Proc. § 17(b)(5) term Oath | CCP-ss-1-34.txt:65 | encoded | `usca-definitions.l4`, section `The table of defined terms`. pass 1 left these limbs inert |
| Code Civ. Proc. § 17(b)(5)(A) | CCP-ss-1-34.txt:66 | encoded | `usca-definitions.l4`, section `The table of defined terms`. pass 1 left these limbs inert |
| Code Civ. Proc. § 17(b)(5)(A) term Depose | CCP-ss-1-34.txt:66 | encoded | `usca-definitions.l4`, section `Testify and depose: Civ. Code § 14(a), Code Civ. Proc. § 17(b)(5)` |
| Code Civ. Proc. § 17(b)(5)(B) | CCP-ss-1-34.txt:68 | encoded | `usca-definitions.l4`, section `The table of defined terms`. pass 1 left these limbs inert |
| Code Civ. Proc. § 17(b)(5)(B) term Testify | CCP-ss-1-34.txt:68 | encoded | `usca-definitions.l4`, section `Testify and depose: Civ. Code § 14(a), Code Civ. Proc. § 17(b)(5)` |
| Code Civ. Proc. § 17(b)(6) | CCP-ss-1-34.txt:69 | encoded | `usca-definitions.l4`, section `The table of defined terms`. pass 1 left these limbs inert |
| Code Civ. Proc. § 17(b)(6) term Person | CCP-ss-1-34.txt:69 | encoded | `usca-definitions.l4`, section `The table of defined terms`. pass 1 left these limbs inert |
| Code Civ. Proc. § 17(b)(7) | CCP-ss-1-34.txt:70 | fork | `usca-definitions.l4`, section `Process: Gov. Code § 22, Code Civ. Proc. § 17(b)(7)`. fork F-process: see Gov. Code § 22; this code's `signifies` is read as a closed definition, so a thing outside it is FALSE; was `not applicable` in pass 1 |
| Code Civ. Proc. § 17(b)(7) term Process | CCP-ss-1-34.txt:70 | fork | `usca-definitions.l4`, section `Process: Gov. Code § 22, Code Civ. Proc. § 17(b)(7)`. fork F-process: see Gov. Code § 22; this code's `signifies` is read as a closed definition, so a thing outside it is FALSE; was `not applicable` in pass 1 |
| Code Civ. Proc. § 17(b)(8) | CCP-ss-1-34.txt:71 | encoded | `usca-definitions.l4`, section `The table of defined terms`. pass 1 left these limbs inert |
| Code Civ. Proc. § 17(b)(8) term Property | CCP-ss-1-34.txt:71 | encoded | `usca-definitions.l4`, section `The table of defined terms`. pass 1 left these limbs inert |
| Code Civ. Proc. § 17(b)(8)(A) | CCP-ss-1-34.txt:72 | encoded | `usca-definitions.l4`, section `The table of defined terms`. pass 1 left these limbs inert |
| Code Civ. Proc. § 17(b)(8)(A) term Personal property | CCP-ss-1-34.txt:72 | encoded | `usca-definitions.l4`, section `The table of defined terms`. pass 1 left these limbs inert |
| Code Civ. Proc. § 17(b)(8)(B) | CCP-ss-1-34.txt:73 | encoded | `usca-definitions.l4`, section `The table of defined terms`. pass 1 left these limbs inert |
| Code Civ. Proc. § 17(b)(8)(B) term Real property | CCP-ss-1-34.txt:73 | encoded | `usca-definitions.l4`, section `The table of defined terms`. pass 1 left these limbs inert |
| Code Civ. Proc. § 17(b)(9) | CCP-ss-1-34.txt:74 | encoded | `usca-canons-of-reading.l4`, section `Gov. Code § 10, Civ. Code § 14(b)(6), Code Civ. Proc. § 17(b)(9): section and subdivision` |
| Code Civ. Proc. § 17(b)(9) term Section | CCP-ss-1-34.txt:74 | encoded | `usca-canons-of-reading.l4`, section `Gov. Code § 10, Civ. Code § 14(b)(6), Code Civ. Proc. § 17(b)(9): section and subdivision` |
| Code Civ. Proc. § 17(b)(10) | CCP-ss-1-34.txt:76 | encoded | `usca-definitions.l4`, section `The table of defined terms`. pass 1 left these limbs inert |
| Code Civ. Proc. § 17(b)(10) term Sheriff | CCP-ss-1-34.txt:76 | encoded | `usca-definitions.l4`, section `The table of defined terms`. pass 1 left these limbs inert |
| Code Civ. Proc. § 17(b)(11) | CCP-ss-1-34.txt:77 | encoded | `usca-general-provisions.l4`: `a mark is a signature or subscription`; `a signature by mark can be acknowledged or serve as the signature to a sworn statement` |
| Code Civ. Proc. § 17(b)(11) term Signature | CCP-ss-1-34.txt:77 | encoded | `usca-general-provisions.l4`: `a mark is a signature or subscription`; `a signature by mark can be acknowledged or serve as the signature to a sworn statement` |
| Code Civ. Proc. § 17(b)(12) | CCP-ss-1-34.txt:78 | encoded | `usca-definitions.l4`, section `The table of defined terms`. pass 1 left these limbs inert |
| Code Civ. Proc. § 17(b)(12) term Spouse | CCP-ss-1-34.txt:78 | encoded | `usca-definitions.l4`, section `The table of defined terms`. pass 1 left these limbs inert |
| Code Civ. Proc. § 17(b)(13) | CCP-ss-1-34.txt:79 | encoded | `usca-definitions.l4`, section `United States: Code Civ. Proc. § 17(b)(13)`. the State limb is `the meaning of State in the Government Code` in `usca-general-provisions.l4` |
| Code Civ. Proc. § 17(b)(13) term State | CCP-ss-1-34.txt:79 | encoded | `usca-definitions.l4`, section `United States: Code Civ. Proc. § 17(b)(13)`. the State limb is `the meaning of State in the Government Code` in `usca-general-provisions.l4` |
| Code Civ. Proc. § 17(b)(13) term United States | CCP-ss-1-34.txt:79 | encoded | `usca-definitions.l4`, section `United States: Code Civ. Proc. § 17(b)(13)`. the State limb is `the meaning of State in the Government Code` in `usca-general-provisions.l4` |
| Code Civ. Proc. § 17(b)(14) | CCP-ss-1-34.txt:80 | encoded | `usca-definitions.l4`, section `The table of defined terms`. pass 1 left these limbs inert |
| Code Civ. Proc. § 17(b)(14) term Will | CCP-ss-1-34.txt:80 | encoded | `usca-definitions.l4`, section `The table of defined terms`. pass 1 left these limbs inert |
| Code Civ. Proc. § 17(b)(15) | CCP-ss-1-34.txt:81 | encoded | `usca-definitions.l4`, section `Writ: Code Civ. Proc. § 17(b)(15)` |
| Code Civ. Proc. § 17(b)(15) term Writ | CCP-ss-1-34.txt:81 | encoded | `usca-definitions.l4`, section `Writ: Code Civ. Proc. § 17(b)(15)` |
| Code Civ. Proc. § 17(b)(16) | CCP-ss-1-34.txt:82 | encoded | `usca-definitions.l4`, section `The table of defined terms`. pass 1 left these limbs inert |
| Code Civ. Proc. § 17(b)(16) term Writing | CCP-ss-1-34.txt:82 | encoded | `usca-definitions.l4`, section `The table of defined terms`. pass 1 left these limbs inert |
| Code Civ. Proc. § 18 | CCP-ss-1-34.txt:84 | encoded | `usca-operation-of-statutes.l4`: `an earlier statute, law or rule remains in force`; `the repeal by the code revives a former law that was repealed before`; `the repeal by the Code of Civil Procedure affects a private statute` |
| Code Civ. Proc. § 19 | CCP-ss-1-34.txt:86 | inert | 2 (short title: how the Act may be cited) |
| Code Civ. Proc. § 20 | CCP-ss-1-34.txt:88 | encoded | `usca-remedies-and-actions.l4`, section `Code Civ. Proc. § 20: judicial remedies`. was `not applicable` in pass 1 |
| Code Civ. Proc. § 21 | CCP-ss-1-34.txt:90 | encoded | `usca-remedies-and-actions.l4`, section `Code Civ. Proc. § 21, § 22, § 23: actions and special proceedings`. was `not applicable` in pass 1 |
| Code Civ. Proc. § 21 item 1 | CCP-ss-1-34.txt:91 | encoded | `usca-remedies-and-actions.l4`, section `Code Civ. Proc. § 21, § 22, § 23: actions and special proceedings`. was `not applicable` in pass 1 |
| Code Civ. Proc. § 21 item 2 | CCP-ss-1-34.txt:92 | encoded | `usca-remedies-and-actions.l4`, section `Code Civ. Proc. § 21, § 22, § 23: actions and special proceedings`. was `not applicable` in pass 1 |
| Code Civ. Proc. § 22 | CCP-ss-1-34.txt:94 | encoded | `usca-remedies-and-actions.l4`, section `Code Civ. Proc. § 21, § 22, § 23: actions and special proceedings`. was `not applicable` in pass 1 |
| Code Civ. Proc. § 23 | CCP-ss-1-34.txt:96 | fork | `usca-remedies-and-actions.l4`, section `Code Civ. Proc. § 21, § 22, § 23: actions and special proceedings`: `the class of the judicial remedy`. fork F-23: `every other remedy is a special proceeding` is read as every other judicial remedy, the remedies § 21 divides; a remedy that is not a judicial remedy is refused; was `not applicable` in pass 1 |
| Code Civ. Proc. § 24 | CCP-ss-1-34.txt:98 | encoded | `usca-remedies-and-actions.l4`, section `Code Civ. Proc. § 24, § 25, § 30: civil and criminal actions`. was `not applicable` in pass 1 |
| Code Civ. Proc. § 24 item 1 | CCP-ss-1-34.txt:99 | encoded | `usca-remedies-and-actions.l4`, section `Code Civ. Proc. § 24, § 25, § 30: civil and criminal actions`. was `not applicable` in pass 1 |
| Code Civ. Proc. § 24 item 2 | CCP-ss-1-34.txt:100 | fork | `usca-remedies-and-actions.l4`, section `Code Civ. Proc. § 24, § 25, § 30: civil and criminal actions`: `the kind of an action brought for`. fork F-criminal: the deposit never defines a criminal action (§ 31 sends that to the Penal Code), so an action brought for the punishment of a public offense is read as criminal and an action for some other purpose is refused; was `not applicable` in pass 1 |
| Code Civ. Proc. § 25 | CCP-ss-1-34.txt:102 | encoded | `usca-remedies-and-actions.l4`, section `Code Civ. Proc. § 24, § 25, § 30: civil and criminal actions`. was `not applicable` in pass 1 |
| Code Civ. Proc. § 25 item 1 | CCP-ss-1-34.txt:103 | encoded | `usca-remedies-and-actions.l4`, section `Code Civ. Proc. § 24, § 25, § 30: civil and criminal actions`. was `not applicable` in pass 1 |
| Code Civ. Proc. § 25 item 2 | CCP-ss-1-34.txt:104 | encoded | `usca-remedies-and-actions.l4`, section `Code Civ. Proc. § 24, § 25, § 30: civil and criminal actions`. was `not applicable` in pass 1 |
| Code Civ. Proc. § 26 | CCP-ss-1-34.txt:106 | encoded | `usca-remedies-and-actions.l4`, section `Code Civ. Proc. § 26: obligation`. was `not applicable` in pass 1 |
| Code Civ. Proc. § 26(a) | CCP-ss-1-34.txt:107 | encoded | `usca-remedies-and-actions.l4`, section `Code Civ. Proc. § 26: obligation`. was `not applicable` in pass 1 |
| Code Civ. Proc. § 26(b) | CCP-ss-1-34.txt:108 | encoded | `usca-remedies-and-actions.l4`, section `Code Civ. Proc. § 26: obligation`. was `not applicable` in pass 1 |
| Code Civ. Proc. § 27 | CCP-ss-1-34.txt:110 | encoded | `usca-remedies-and-actions.l4`, section `Code Civ. Proc. § 27, § 28, § 29: injury`. was `not applicable` in pass 1 |
| Code Civ. Proc. § 27 item 1 | CCP-ss-1-34.txt:111 | encoded | `usca-remedies-and-actions.l4`, section `Code Civ. Proc. § 27, § 28, § 29: injury`. was `not applicable` in pass 1 |
| Code Civ. Proc. § 27 item 2 | CCP-ss-1-34.txt:112 | encoded | `usca-remedies-and-actions.l4`, section `Code Civ. Proc. § 27, § 28, § 29: injury`. was `not applicable` in pass 1 |
| Code Civ. Proc. § 28 | CCP-ss-1-34.txt:114 | fork | `usca-remedies-and-actions.l4`, section `Code Civ. Proc. § 27, § 28, § 29: injury`: `the kind of an injury`. fork F-28: § 28 says depriving an owner of the benefit of property `is done by` four ways and § 29 calls every other injury an injury to the person; depriving by some other way is refused, since reading § 29 literally would ignore § 28; was `not applicable` in pass 1 |
| Code Civ. Proc. § 29 | CCP-ss-1-34.txt:116 | fork | `usca-remedies-and-actions.l4`, section `Code Civ. Proc. § 27, § 28, § 29: injury`: `the kind of an injury`. fork F-28: § 28 says depriving an owner of the benefit of property `is done by` four ways and § 29 calls every other injury an injury to the person; depriving by some other way is refused, since reading § 29 literally would ignore § 28; was `not applicable` in pass 1 |
| Code Civ. Proc. § 30 | CCP-ss-1-34.txt:118 | encoded | `usca-remedies-and-actions.l4`, section `Code Civ. Proc. § 24, § 25, § 30: civil and criminal actions`. was `not applicable` in pass 1 |
| Code Civ. Proc. § 31 | CCP-ss-1-34.txt:120 | encoded | `usca-remedies-and-actions.l4`, section `Code Civ. Proc. § 31, § 32, § 32.5, § 33: criminal action, non-merger, classification, prosecuting attorney`. was `not applicable` in pass 1 |
| Code Civ. Proc. § 32 | CCP-ss-1-34.txt:122 | encoded | `usca-remedies-and-actions.l4`, section `Code Civ. Proc. § 31, § 32, § 32.5, § 33: criminal action, non-merger, classification, prosecuting attorney`. was `not applicable` in pass 1 |
| Code Civ. Proc. § 32.5 | CCP-ss-1-34.txt:124 | encoded | `usca-remedies-and-actions.l4`, section `Code Civ. Proc. § 31, § 32, § 32.5, § 33: criminal action, non-merger, classification, prosecuting attorney`. was `not applicable` in pass 1 |
| Code Civ. Proc. § 32.5 term jurisdictional classification | CCP-ss-1-34.txt:124 | encoded | `usca-remedies-and-actions.l4`, section `Code Civ. Proc. § 31, § 32, § 32.5, § 33: criminal action, non-merger, classification, prosecuting attorney`. was `not applicable` in pass 1 |
| Code Civ. Proc. § 33 | CCP-ss-1-34.txt:126 | encoded | `usca-remedies-and-actions.l4`, section `Code Civ. Proc. § 31, § 32, § 32.5, § 33: criminal action, non-merger, classification, prosecuting attorney`; added after the independent test pass, `usca-further-asks.l4`: `Code Civ. Proc. § 33 requires a prosecuting attorney to assist in the civil resolution of a violation`. was `not applicable` in pass 1 |
| Code Civ. Proc. § 34 | CCP-ss-1-34.txt:128 | encoded | `usca-general-provisions.l4`: `an electronic signature is as effective as an original signature under Code Civ. Proc. § 34` |
| Code Civ. Proc. § 17 term (a) present tense | CCP-ss-1-34.txt (term in prose) | fork | `usca-canons-of-reading.l4`, section `Tense, gender and number: Gov. Code §§ 11-13, Civ. Code § 14(a), Code Civ. Proc. § 17(a)`: `a word used in the tense includes the tense, in`. fork F-tense: this code says the present tense includes the future and nothing of the past; was inert in pass 1 |
| Code Civ. Proc. § 17 term (a) masculine gender | CCP-ss-1-34.txt (term in prose) | encoded | `usca-canons-of-reading.l4`, section `Tense, gender and number: Gov. Code §§ 11-13, Civ. Code § 14(a), Code Civ. Proc. § 17(a)` |
| Code Civ. Proc. § 17 term (a) singular number | CCP-ss-1-34.txt (term in prose) | encoded | `usca-canons-of-reading.l4`, section `Tense, gender and number: Gov. Code §§ 11-13, Civ. Code § 14(a), Code Civ. Proc. § 17(a)` |
| Code Civ. Proc. § 17 term (a) plural number | CCP-ss-1-34.txt (term in prose) | encoded | `usca-canons-of-reading.l4`, section `Tense, gender and number: Gov. Code §§ 11-13, Civ. Code § 14(a), Code Civ. Proc. § 17(a)` |
| Code Civ. Proc. § 26 term obligation | CCP-ss-1-34.txt (term in prose) | encoded | `usca-remedies-and-actions.l4`, section `Code Civ. Proc. § 26: obligation`. was `not applicable` in pass 1 |
| Code Civ. Proc. § 26 term obligation arising from contract | CCP-ss-1-34.txt (term in prose) | encoded | `usca-remedies-and-actions.l4`, section `Code Civ. Proc. § 26: obligation`. was `not applicable` in pass 1 |
| Code Civ. Proc. § 26 term obligation arising from operation of law | CCP-ss-1-34.txt (term in prose) | encoded | `usca-remedies-and-actions.l4`, section `Code Civ. Proc. § 26: obligation`. was `not applicable` in pass 1 |
| Code Civ. Proc. § 20 term judicial remedies | CCP-ss-1-34.txt (term in prose) | encoded | `usca-remedies-and-actions.l4`, section `Code Civ. Proc. § 20: judicial remedies`. was `not applicable` in pass 1 |
| Code Civ. Proc. § 22 term action | CCP-ss-1-34.txt (term in prose) | encoded | `usca-remedies-and-actions.l4`, section `Code Civ. Proc. § 21, § 22, § 23: actions and special proceedings`. was `not applicable` in pass 1 |
| Code Civ. Proc. § 23 term special proceeding | CCP-ss-1-34.txt (term in prose) | fork | `usca-remedies-and-actions.l4`, section `Code Civ. Proc. § 21, § 22, § 23: actions and special proceedings`: `the class of the judicial remedy`. fork F-23: `every other remedy is a special proceeding` is read as every other judicial remedy, the remedies § 21 divides; a remedy that is not a judicial remedy is refused; was `not applicable` in pass 1 |
| Code Civ. Proc. § 25 term civil action | CCP-ss-1-34.txt (term in prose) | encoded | `usca-remedies-and-actions.l4`, section `Code Civ. Proc. § 24, § 25, § 30: civil and criminal actions`. was `not applicable` in pass 1 |
| Code Civ. Proc. § 28 term injury to property | CCP-ss-1-34.txt (term in prose) | fork | `usca-remedies-and-actions.l4`, section `Code Civ. Proc. § 27, § 28, § 29: injury`: `the kind of an injury`. fork F-28: § 28 says depriving an owner of the benefit of property `is done by` four ways and § 29 calls every other injury an injury to the person; depriving by some other way is refused, since reading § 29 literally would ignore § 28; was `not applicable` in pass 1 |
| Code Civ. Proc. § 29 term injury to the person | CCP-ss-1-34.txt (term in prose) | fork | `usca-remedies-and-actions.l4`, section `Code Civ. Proc. § 27, § 28, § 29: injury`: `the kind of an injury`. fork F-28: § 28 says depriving an owner of the benefit of property `is done by` four ways and § 29 calls every other injury an injury to the person; depriving by some other way is refused, since reading § 29 literally would ignore § 28; was `not applicable` in pass 1 |
| Code Civ. Proc. § 10 term holidays within the meaning of the code | CCP-ss-1-34.txt (term in prose) | encoded | `usca-holidays.l4`: a limb of Code Civ. Proc. § 10, whose functions are listed in its section row |
| Civ. Code § 8 | - | repealed or blank in this text | 3 (the number does not appear in the deposited text; the deposit holds only sections marked current, so the text shows nothing more than the gap) |
| Civ. Code § 15 | - | repealed or blank in this text | 3 (the number does not appear in the deposited text; the deposit holds only sections marked current, so the text shows nothing more than the gap) |
| Civ. Code § 16 | - | repealed or blank in this text | 3 (the number does not appear in the deposited text; the deposit holds only sections marked current, so the text shows nothing more than the gap) |
| Gov. Code § 6730 | - | repealed or blank in this text | 3 (the number does not appear in the deposited text; the deposit holds only sections marked current, so the text shows nothing more than the gap) |
| Gov. Code § 6732 | - | repealed or blank in this text | 3 (the number does not appear in the deposited text; the deposit holds only sections marked current, so the text shows nothing more than the gap) |
| Gov. Code § 6734 | - | repealed or blank in this text | 3 (the number does not appear in the deposited text; the deposit holds only sections marked current, so the text shows nothing more than the gap) |
| Gov. Code § 9601 | - | repealed or blank in this text | 3 (the number does not appear in the deposited text; the deposit holds only sections marked current, so the text shows nothing more than the gap) |
<!-- coverage-table:end -->

## Fork register

A fork is a place where the deposited text allows more than one reading, or says nothing.
Each entry gives the readings seen, the one the code takes, the text that licenses each reading, and where in the code the choice sits.
"The text" always means the deposited `.txt` files, which are a converter-made rendering and not the official text.
Where a reading is not licensed by the deposited text the code refuses (`REFUSE`) and the entry says so.
Where the code offers both readings as separate functions the entry says which one the headline function uses.
Nothing here was settled by a court or by a regulator: the deposit contains no decision and no commentary.
No fork was resolved by looking at another encoding (pass 2 read no other encoding).

**A convention that is not a fork.**
In these modules a Boolean result `FALSE` means "this section does not give this result", and `REFUSE` is used where an antecedent is undetermined or where the section has no consequence for the case.
So a function such as `a statute fixing the salary of a State officer or employee is an appropriation of money for it` is constant `FALSE` (Gov. Code § 9610 says it is not), and `an earlier statute, law or rule remains in force` refuses on a matter the code does not provide for.
There is no home-made third value anywhere.

### Counting a period

**F-from: which day is the excluded "first day", and is the last day inside the period?**
- Text: Gov. Code § 6800, Civ. Code § 10 and Code Civ. Proc. § 12 all say a period is computed "by excluding the first day, and including the last".
  The text says the last day is included; that part is not a fork.
- Readings of "first day": (1) the day of the event the period runs from; (2) the day after it.
  Under (1) a period of 30 days from 1 January ends on 31 January; under (2) it ends on 1 February.
- Taken: (1).
  Every counting function takes the day the period is counted from and treats that day as the excluded first day.
  The caller who means "from the day after the event" passes the day after.
- The text does not distinguish "from" from "after": nothing deposited says that "within 30 days after" and "within 30 days from" differ.
  The code has one function for both, so the difference is the caller's choice of start day.
- `the date d falls inside the period after firstDay through lastDay` reads the period as the first day excluded and the last included, and is tested at both ends.
- Where: `usca-interpretation-time.l4`, the section `Counting a period`.

**F-contract: does the period rule reach a period fixed by contract?**
- Text: Gov. Code § 6800 and Civ. Code § 10 speak of "any act provided by law"; Code Civ. Proc. § 12a(a) of "any act provided or required by law"; Gov. Code § 6706, Civ. Code § 11 and Code Civ. Proc. § 13 speak of an act "appointed by law or contract" but only for an act on a particular day.
- Readings: (1) a period set by contract is counted the same way; (2) it is not within these sections.
- Taken: neither.
  The counting functions take a period and a start and make no claim about the kind of act, so nothing refuses and nothing asserts coverage.
  Which readings apply to a contract is an open question (Q-contract).

**F-run: when the last day is a holiday, does the extension stop at the next day, or run past several in a row?**
- Text: Gov. Code § 6800, Civ. Code § 10 and Code Civ. Proc. § 12: "unless the last day is a holiday, and then it is also excluded".
  Code Civ. Proc. § 12a(a): the period "is hereby extended to and including the next day that is not a holiday".
- Readings: (1) run: carry on to the first day that is not a holiday (the words of § 12a(a)); (2) one step: exclude the holiday last day once, and the day after it is the last day, whatever that day is.
- Taken: (1) for the headline function `the last day of a period of n u counted from d under the calendar holiday`; (2) is offered as `with a holiday last day excluded once under the calendar`.
  The two differ when the day after a holiday last day is itself a holiday.
  Example from the worked cases: five years from 2025-09-01 ends on Sunday 2030-09-01; the Government Code calendar gives 2030-09-03 on (1) and 2030-09-02 on (2), and 2030-09-02 is itself a holiday (first Monday in September, Gov. Code § 6700(a)(13)).
- "Two holidays in a row" is therefore tested on both: Saturday and Sunday under the Code of Civil Procedure calendar, and Sunday and Monday holiday together under the Government Code calendar.
- A calendar in which more than 366 days in a row are holidays is refused rather than looped over (the loop guard is a limit on the caller's calendar, not a rule of the text; 366 in a row resolve, 367 are refused).
- Where: `extended to the next day that is not a holiday`, `with a holiday last day also excluded, once`.

**F-direction: which way does a last day on a holiday move?**
- Text: Code Civ. Proc. § 12a(a) says "extended to and including the next day"; § 6800's "also excluded" does not say which way.
- Taken: forward, for every forward-counted period.
  Excluding a counted day lengthens the span, so "also excluded" is read as the same direction as § 12a(a).
- For a period counted backward from a hearing (Code Civ. Proc. § 12c) the text gives no direction: see F-backward.

**F-unit: does the holiday extension apply to a period of months or years, not only of days?**
- Text: the sections say "any act provided by law" and "a specified period of time" and draw no line by unit.
- Taken: the same rule for every unit (days, weeks, months, years, half years, quarters of a year).
  A reader who thinks a period counted in months ends on its date whatever the day can read `before the rest-day rule, the last day of ...`, which does not apply the extension.
- Where: the dispatcher `the last day of a period of n u counted from d under the calendar holiday`.

**F-holiday: which days are "holidays"?**
- The text has three definitions and they differ.
  Gov. Code § 6700(a): "the holidays in this state", a list of twenty paragraphs, Sundays among them, Saturdays not.
  Civ. Code § 7: "every Sunday and such other days as are specified or provided for as holidays in the Government Code".
  Code Civ. Proc. § 10: every Sunday and the judicial holidays in § 135; Code Civ. Proc. § 12a(a): "all day on Saturdays, all holidays specified in Section 135 and, to the extent provided in Section 12b, all days that by terms of Section 12b are required to be considered as holidays".
- Readings of § 12a(a): (1) literal: Sunday is not named, so it is a holiday for the extension only if § 135 specifies it, and § 135 is not in the deposit; (2) § 10 is read into § 12a, so Sundays count.
- Taken: both are functions (`...read literally`, `...taking in the Sundays of § 10`); the worked cases use (2).
- Code Civ. Proc. § 135 is not in the deposited text.
  Its days are a list the caller supplies.
  A caller who supplies none gets Saturdays and Sundays (and § 12b closures) under the Code of Civil Procedure calendars, and, for example, 1 January is then not a holiday under them.
  The module cannot tell an empty list from an omitted one (Q-135).
- The days that need a calendar the text does not give are inputs, never computed: Lunar New Year (§ 6700(a)(4)), Diwali (§ 6700(a)(9)), Good Friday, days appointed by the President or Governor, Thanksgiving Day (the Thursday "appointed"), days a public office is closed (§ 12b), bank closings (Civ. Code § 7.1(a)).
- Where: `usca-holidays.l4`, with the record `Days supplied by the caller`.

**F-vintage: which version of a section applies to a date.**
- Text: the deposit holds one version of each section, the current one (the `current_to` field of the `.meta.json` files in `../../registers/source-bundle/` says 2026-10-19), with its amendment line (for example § 6700: "Amended by Stats. 2026, Ch. 7, Sec. 1. (AB 2156) Effective March 26, 2026").
  It holds no earlier version of any section.
- Taken: the deposited text is applied to every date, including dates before the amendment, because the text carries nothing to apply instead.
  A period counted in 2024 against the holiday list therefore uses today's list.
  The functions take no vintage; adding one would need the earlier texts (Q-vintage).
  The worked cases and many tests use dates before 26 March 2026, so the modules do not refuse on a date before an amendment.

**F-governs: which definition of "holiday" and of "month" governs which kind of enactment?**
- Text: each code says "within the meaning of this code" for holidays (Civ. Code § 7, Code Civ. Proc. § 10).
  "Month" is defined three times, in the same words: Gov. Code § 6804, Civ. Code § 14(b)(4) and Code Civ. Proc. § 17(b)(4) ("a calendar month, unless otherwise expressed").
  The two codes give their definitions "in this code" and "unless otherwise apparent from the context" as well; § 6804 has no limit of its own beyond "unless otherwise expressed".
  Gov. Code § 9603 says the general rules of construction are in the preliminary provisions of the different codes.
  Gov. Code § 5 says the general provisions govern the construction of that code.
  Code Civ. Proc. § 12a(b) makes § 12a apply to "all other provisions of law ... whether expressed in this or any other code or statute, ordinance, rule, or regulation".
- Taken, with `Kind of enactment`:
  a provision of the Civil Code: Civ. Code § 7 and § 14(b)(4); a provision of the Code of Civil Procedure: Code Civ. Proc. § 10 (with § 12b) and § 17(b)(4); a provision of the Government Code: Gov. Code § 6700(a) and § 6804; another State statute: Gov. Code § 6700(a) and § 6804; an ordinance, rule or regulation: REFUSE.
- "Another State statute" taking the Government Code's definitions is an assumption: § 6700(a) says "the holidays in this state" and § 6804 has no limit of its own, and nothing deposited says more.
- For the extension of a last day, Code Civ. Proc. § 12a(a) names its own holiday list "for purposes of this section", and § 12a(b) reaches every kind of provision, so the extension question is answered the same for every kind (`the section that extends a last day falling on a holiday for kind`).
- Where: the section `Which section governs` of `usca-interpretation-time.l4` and `the day is a holiday within the meaning of a provision of kind` in `usca-holidays.l4`.

**F-overlap: Gov. Code § 6800, Civ. Code §§ 10-11 and Code Civ. Proc. §§ 12-13b overlap.**
- Gov. Code § 6800, Civ. Code § 10 and Code Civ. Proc. § 12 say the same thing in the same words (§ 10 omits one comma).
  One set of functions serves all three.
- Gov. Code § 6706, Civ. Code § 11 and Code Civ. Proc. § 13 also say one thing (an act of a secular nature, not a work of necessity or mercy, appointed for a particular day that is a holiday may be done on the next business day).
  One function serves all three.
- The real overlap: Code Civ. Proc. § 12a(b) extends "an act to be performed on a particular day" to the next day that is not a holiday, and § 13 gives the next business day.
  They reach different days where one makes Saturday a holiday (§ 12a(a)) and the other makes Saturday a business day (Civ. Code § 9 counts every day other than those in § 7 as a business day).
  The function for § 13, Civ. Code § 11 and Gov. Code § 6706 takes both a holiday calendar and a business-day calendar and returns the day by that rule alone; it does not pick between that rule and § 12a.
- Gov. Code § 6707 (a filing with a state agency whose last day is a Saturday or a holiday) names Saturday expressly, so a Saturday is not a business day for this one rule even though it is for Civ. Code § 9.
- Code Civ. Proc. § 13a and § 13b allow an act to be performed on a special holiday or on a Saturday "with like effect"; the text has no sentence about performing an act on a Sunday or another holiday, and the function refuses for that case.

**F-week: a week.**
- Gov. Code § 6805: "seven consecutive days".
  Taken: a period of n weeks is a period of 7n days, counted by § 6800.
  Nothing in the text counts weeks by the calendar week.

**F-month: a month, and a start on the 29th, 30th or 31st.**
- Text: Gov. Code § 6804 says a month is "a calendar month, unless otherwise expressed" and nothing more.
  § 6800 excludes the first day.
- Readings: (1) corresponding day: n months from the 15th is the 15th, n calendar months on; (2) when the month reached is shorter, the last day of it (this is what daydate's `add months` does); (3) when it is shorter, spill into the next month by days.
- Taken: (1), and where the month reached has no day with the start day's number (a start on 31 January for one month; on 29, 30 or 31 January in a common year; on 31 March for one month), REFUSE: the text licenses neither (2) nor (3).
  The worked case "one month from 2025-01-31" is therefore refused.
  Start on the 31st reaching a month that has a 31st is answered (31 January plus two months is 31 March).
- Where: `before the rest-day rule, the last day of` n `months counted from` d.

**F-year: a year is 365 days.**
- Text: Gov. Code § 6803: "Year" means a period of 365 days; "half year," 182 days; "quarter of a year," 91 days.
  Three years from 2025-07-16 is 1,095 counted days.
  29 February 2028 lies in that period and the pair counts as one day (see F-pair), so the last day is 2028-07-16, which is 1,096 calendar days on.
- Taken: the lengths are 365, 182 and 91 days exactly, counted from the first day by § 6800.
  The text defines "year" nowhere as a calendar year, so a "year" in these modules is never "the same date next year".
- Where: `last day of n periods of fixed length`.

**F-pair: the leap-day pair.**
- Text: Gov. Code § 6803: "The added day of a leap year, and the day immediately preceding, if they occur in any such period, shall be reckoned together as one day."
  The added day is 29 February; the day immediately preceding it is 28 February.
- Question: does the pair "occur in" the period when 28 February is the excluded first day of the period (§ 6800)?
- Readings: (S) literal: both days must be counted days of the period, so a period whose first day is 28 February does not contain the pair; (P) purposive: the added day is in the period, so the pair counts as one day.
- Taken: (S) for the functions without a reading in their names; (P) is offered as `on the purposive reading of the leap-day pair, ...`.
  The two readings differ only for a period starting on 28 February of a leap year; the worked case "two years from 2024-02-28" ends on 2026-02-27 (S) or 2026-02-28 (P).
- A start on 29 February: 28 February is before the period on both readings, so no pair is counted for that year.

**F-29Feb: a start on 29 February.**
- Years: one year from 2024-02-29 ends on 2025-02-28 (365 days from 29 February; no pair, since 28 February is before the period).
- Months: a start on 29 February reaching a month with a 29th is answered (one month: 29 March; 48 months: 29 February 2028); reaching 2025-02 or 2026-02 (12 or 24 months) is refused under F-month.
- Half years and quarters are counted in days (182, 91), so they never refuse.

### Commencement and the moment of binding

**F-commence: counting the 90-day period of § 9600(a).**
- Text: "a statute enacted at a regular session shall go into effect on January 1 next following a 90-day period from the date of enactment of the statute".
- Questions: is the day of enactment inside the period (§ 6800 speaks of acts "to be done" and a commencement is not one); and what is "next following" when the 90th day is itself a January 1?
- Taken: the period is counted under § 6800, so the day of enactment is excluded and the 90th day is 90 days on.
  The January 1 next following the 90th day is the January 1 after it.
  When the 90th day is itself a January 1 (enactment on 3 October, in any year) the text does not say whether that January 1 is part of the period, and the function refuses.
  Enacted 2026-10-02: 2027-01-01.
  Enacted 2026-10-03: refused.
  Enacted 2026-10-04: 2028-01-01.
- If the day of enactment were counted as day 1, every boundary would move one day later: enactment on 3 October would give 1 January 2027, enactment on 4 October would be the refused case, and 5 October would give the following 1 January.
  The text does not say that § 6800 applies to a commencement, so that reading cannot be ruled out, and the code does not offer it (open question Q-commence).
- Special session: "the 91st day after adjournment", counted from the day of adjournment with that day excluded, so adjournment plus 91 days.

**F-enactment: what is "the date of enactment"?**
- Text: § 9600(a) says "the date of enactment of the statute" without saying whether it is the day a bill is passed, signed or published.
- Taken: the caller supplies the moment of enactment it means (`the moment of enactment`); the code does not choose.

**F-own-day: an Act that names its own day of effect.**
- Text: § 9600(a) says a statute "shall go into effect on January 1 next following a 90-day period"; the exceptions in (b) are statutes calling elections, tax levies, appropriations for the usual current expenses of the state, and urgency statutes.
  The text neither lets a statute's own day displace (a) nor forbids it.
- Taken: REFUSE.
  The worked case "an Act whose day is to be fixed later, fixed as 2026-06-01" is therefore refused for the day and for the moment.
  A caller who takes the day the Act names to govern can call `the day a statute goes into effect, taking the day it names itself to govern`, which is that assumption and nothing more.

**F-subordinate: subordinate legislation.**
- Text: § 9600 speaks of statutes and § 9602 of concurrent and joint resolutions; no deposited section says when a regulation, rule or order takes effect.
- Taken: REFUSE.
  The worked case "subordinate legislation made 2026-03-10 and silent" is refused.

**F-moment: the moment within the day a statute binds.**
- Text: § 9600(a) names a day.
  § 6806 says a day is the period between any midnight and the midnight following.
  Civ. Code § 2 and Code Civ. Proc. § 2 name noon on 1 January 1873 for those codes alone.
- Readings: (1) from the midnight that begins the day; (2) from some other moment, for example the moment of enactment on the day; (3) at the end of the day.
- Taken: for a statute under (a): REFUSE.
  For a statute under (b) ("immediately upon their enactment"): the moment of enactment, which is the caller's input.
  `the moment a statute goes into effect, taking it to bind from the midnight that begins its day` is offered as the explicit assumption (1).
- The two codes: noon on 1 January 1873, from their own text.
  The Government Code's own day is not in the deposit (§§ 1-26 say "this code takes effect" in § 4 without a day): REFUSE.

**F-midnight: who owns the midnight instant?**
- Text: § 6806 says a day runs between "any midnight and the midnight following" and does not say which day the instant of midnight belongs to.
- Taken: a representation chosen here and not a rule of the text: the instant that ends one day and begins the next is the beginning (0 seconds) of the later day.
  A moment is a day and a count of seconds after the midnight that begins it, and a moment lies within the day it names.

**F-language: which language version is authoritative?**
- Text: Gov. Code § 8 says a notice, report, statement or record required or authorized by the code "shall be made in writing in the English language unless it is expressly provided otherwise".
  The Legislature publishes the codes in English only, and the deposit has no sentence about a version in another language.
- Taken: the form of such a record is computed (writing, English, unless otherwise provided); which of two language versions has authority is REFUSED, with a message that names the gap.

**F-deemed-service: deemed service or notice.**
- The deposit has no general rule deeming service or notice made on any day.
  Civ. Code § 17 and Code Civ. Proc. § 11 say only that certified mail is a sufficient compliance where registered mail is required; Civ. Code §§ 18 and 19 define actual and constructive notice without a day; Code Civ. Proc. § 12c(b) counts days added for a method of service backward from a hearing, which is not a deeming rule.
- Taken: `the day service by mail is deemed made, the document having been mailed on` and `the day a notice is deemed given, the notice having been sent on` both REFUSE, with messages that say so.
  Nothing was invented to fill the gap.

**F-backward: counting backward from a hearing (Code Civ. Proc. § 12c).**
- Text: § 12c(a): an act due a number of days before a hearing counts back from the hearing date, the hearing day excluded; (b): days added for a method of service count back from the resulting day.
- Questions: (1) which way a backward-counted last day on a holiday moves, given that § 12a(a) moves it forward (toward the hearing) and § 12 excludes it (which backward is earlier); (2) whether the day § 12c(a) gives is itself checked against the calendar before the (b) days are counted.
- Taken: (1) REFUSE when it arises; (2) not checked.

### Rules about particular days and the like

**F-13ab: acts on a special holiday or on a Saturday.**
- Text: § 13a (a special holiday as § 6705 of the Government Code uses the term) and § 13b (a Saturday): the act "may be performed (but is not hereby required to be performed) ... with like effect as if performed on a day which is not a holiday".
- Taken: TRUE for each; REFUSE for a Sunday or another holiday, to which these two sections say nothing.

**F-6700a19: Good Friday "from 12 noon until 3 p.m.".**
- Taken: a function of the moment; at noon it has begun; at exactly 3 p.m. the text does not say whether "until" includes the instant, and the function refuses.
- Civ. Code § 7.1(o) (Good Friday "from 12 noon until closing"): the bank's closing second is an input.

**F-6701c: March 31 observed on another day.**
- Text: § 6701(c): when March 31 falls on a Tuesday, Wednesday or Thursday, "the Legislature may observe the holiday on" the preceding Friday, the preceding Monday or the following Friday.
- Question: does March 31 itself then stop being a holiday?
- Taken: the caller says (`March 31 itself stays a holiday in a year in which it is observed on another day`), and the observed day is a list the caller supplies.

**F-6701d: a county's alternate day.**
- Text: § 6701(d): if a § 6700 holiday falls on a Saturday, a county board may by ordinance or resolution provide that an alternate day is a holiday for county employees, except court attaches.
- Question: does the Saturday stop being a holiday for them?
- Taken: the alternate days are a list the caller supplies; nothing is taken away from the Saturday.
  The function does not check that the alternate day was provided for a Saturday holiday, which is the board's fact.

**F-6702city: "those holidays enumerated in Section 6700" for a city's offices.**
- Text: § 6702, third sentence: "Public offices of a city shall be closed on those holidays enumerated in Section 6700 unless otherwise provided by charter, ordinance or resolution."
- Question: are the Monday after a Sunday holiday and the Friday before a Saturday November 11 (§ 6701(a), (b)) "enumerated in Section 6700"?
- Taken: no.
  The days of § 6700 that apply to a city under (a)(20)(B), nothing from § 6701.
  When a charter, ordinance or resolution provides otherwise, REFUSE: what it provides is not in the text.
  A reader who wants the § 6701 days as well can use `a holiday under Gov. Code § 6700 and § 6701 for a city, county or district`.

**F-hol-6: the commemorative proclamations, §§ 6708-6736.**
- Each directs the Governor to proclaim a day or month (for example § 6709 for 15 January, while § 6700(a)(3) makes the third Monday in January the holiday).
  None says the day is a holiday, and § 6700(a)(20)(A) makes holidays of "every day appointed by the President or Governor for a public fast, thanksgiving, or holiday".
- Question: is a day proclaimed under one of these sections "appointed ... for a ... holiday"?
- Taken: not decided in code.
  Since pass 2 the sections are encoded (`usca-proclaimed-days.l4`: which day, in which year, whether the duty recurs), and `a proclamation under the section makes the day a holiday` is a `REFUSE`.
  A caller who treats a proclamation as such an appointment supplies the day in `days appointed by the President or Governor for a public fast, thanksgiving or holiday`.
  § 6705 (a special or limited holiday applies only to a special class and courts and offices stay open) is encoded as the constant `TRUE` of its second paragraph.

**F-6802: a hundredth year before 1900.**
- Text: § 6802 names 1900, 2100, 2200, 2300 "or any other future hundredth year" as common years, and 2000, 2400, 2800 and every fourth hundredth year after 2000 as leap years; "every fourth year ... which, by usage in this State is considered a leap year" is a leap year.
- Taken: for a hundredth year before 1900 (1800, 1700, ...) the text names no rule, so REFUSE; every other year follows § 6802.
- Gov. Code § 6801 (the Gregorian calendar) is what daydate's day numbers are; no date is checked against 1752.

**F-dst: daylight saving time.**
- Text: § 6808(a), (b): standard time is Pacific standard time; daylight saving time advances the clock one hour from 2 a.m. on the second Sunday in March to 2 a.m. on the first Sunday in November.
- Taken: the clock readings from 2 a.m. up to 3 a.m. on the March day do not occur and are refused; the readings from 1 a.m. up to 2 a.m. on the November day occur twice and are refused (a reading alone cannot say which).
  The November change is read as 2 a.m. on the daylight clock; the text does not say which clock.

**F-daytime: sunrise and sunset themselves.**
- Text: § 6807: daytime is "between sunrise and sunset" and nighttime "between sunset and sunrise".
- Taken: sunrise and sunset are inputs (seconds after midnight); the instant of sunrise or of sunset is refused, as is a day on which sunset does not follow sunrise.

### The operation of statutes

**F-9605b: two amending statutes of one session (Gov. Code § 9605(b)).**
- Text (`GOV-ss-9600-9612.txt:20-23`): (1) "it shall be conclusively presumed that the statute that is enacted last is intended to prevail over statutes that are enacted earlier at the same session", absent an express provision to the contrary in it; (2) "it shall be presumed that the statute with a higher chapter number is intended by the Legislature to prevail", absent an express provision to the contrary in it; "every statute enacted in the even-numbered year of a two-year regular session ... is deemed to bear a higher chapter number than any statute enacted in the odd-numbered year of that session".
- Question 1: when (1) and (2) point at different statutes, which governs?
  Readings: (R1) (1) governs, because it is "conclusively" presumed and (2) only "presumed"; (R2) the text does not rank them.
  The test author took R1 (its Z11).
- Taken: R2, `REFUSE`.
  "Conclusively" and "presumed" say how strong each presumption is against contrary evidence; the text does not say that a conclusive presumption of (1) outranks the presumption of (2).
  R1 is not offered as a function.
  `Gov. Code § 9605(b) makes the presumption conclusive` answers what the words say: `TRUE` for (1), `FALSE` for (2).
- Question 2 (repaired after the independent test pass): two statutes with the same order of enactment have no statute "enacted last", so (1) is not open.
  Taken: (2) alone decides: the statute whose chapter rank is higher prevails, an even-year statute ranking above every odd-year one, unless that statute expressly provides that it is not to prevail.
  Equal ranks: `REFUSE`.
  The first version of the function refused for every pair of the same order before it reached (2), which was a defect of the encoding and not a reading of the text.
- Question 3: a statute whose own text says it is not to prevail.
  Taken: that closes only the presumption that would favour it.
  § 9605(b) does not say the other statute then prevails, so when no other presumption is open the function `REFUSE`s; the other statute prevails by the disclaiming statute's own words, which this function does not read.
  The test author expected "the other statute" for two statutes of the same order where the higher-numbered one disclaims (S487); the encoding refuses, and the reconciled `tests-independent.l4` asserts the refusal, with the test author's expectation quoted above it.
  Returning the other statute would be a change of the last branch of `the statute that prevails when two statutes of one session amend the same section` and of one test.
- Where: `usca-operation-of-statutes.l4`, function `the statute that prevails when two statutes of one session amend the same section first second`; `usca-further-asks.l4`, `Gov. Code § 9605(b) makes the presumption conclusive`.

**F-9607b: the date of termination.**
- Text: § 9607(b): a later statute that deletes or extends the date of termination or repeal, if "chaptered before such date of termination or repeal", revives the law "when the later enacted statute becomes operative".
- Question: is the date of termination the last day the law operates or the first day it does not?
- Taken: the dates are compared as stated: chaptered strictly earlier than the stated date revives the law on the day the later statute becomes operative; otherwise the answer is `NOTHING` (§ 9607(b) says nothing about a statute chaptered on or after that date).

**F-9611: when a temporary provision expires.**
- Text: § 9611: "upon the expiration of the time of the temporary suspension or the effectiveness of the inconsistent provision, the original provision shall have the same force and effect".
- Taken: the input is the last day the temporary provision is effective; the original has full force from the day after.
  The text says "upon the expiration" and not on which day.

**F-ccp9: Code Civ. Proc. § 9.**
- Text: where a limitation "has begun to run before this code goes into effect", the time already run "shall be deemed part of the time prescribed".
- Question: are the days already run counted with or without the day the code took effect?
- Taken: the days already run are the difference of the two dates (the day the code took effect minus the day the limitation began), which is the count whichever of the two end days is left out; the text does not say which.
  That difference is taken off the days the code prescribes.
  A limitation that did not begin before the code is refused.

**F-23.6: Civ. Code § 23.6.**
- Text: "the sections last in numerical order shall prevail, unless such construction is inconsistent with the meaning of the chapter or article."
- Question: sections numbered with a letter (for example 12a) have no numerical place in the text.
- Taken: the section numbers are numbers (17.5 for section 17.5); a letter-numbered section cannot be given to the function, and two sections with one number are refused; an inconsistent construction is refused because the text does not say which section then prevails.

### Definitions, canons, remedies, proclamations, deputies and assessed value (pass 2)

**F-tense: the past tense, and the three codes.**
- Text: Gov. Code § 11, "The present tense includes the past and future tenses; and the future, the present."
  Civ. Code § 14(a) and Code Civ. Proc. § 17(a): words in the present tense "include the future as well as the present".
- Question: in the Civil Code and the Code of Civil Procedure, does the present tense include the past, and the future the present?
  In the Government Code, does the future include the past?
- Taken: `a word used in the tense includes the tense, in` takes the code.
  Government Code: the present includes every tense; the future includes the present; the future including the past, and anything the past includes, are `REFUSE`.
  The other two codes: the present includes the future; every other pair of different tenses is `REFUSE`.
  A tense includes itself in all three.
- Where: `usca-canons-of-reading.l4`, section `Tense, gender and number: Gov. Code §§ 11-13, Civ. Code § 14(a), Code Civ. Proc. § 17(a)`.

**F-process: "process" in two codes.**
- Text: Gov. Code § 22, "Process" includes a writ or summons issued in the course of judicial proceedings of either a civil or criminal nature.
  Code Civ. Proc. § 17(b)(7), "Process" signifies a writ or summons issued in the course of a judicial proceeding.
- Question: is each an open list or a closed one?
- Taken: § 22 is open ("includes"): a document outside it is `REFUSE`d.
  § 17(b)(7) is read as closed ("signifies"): a document outside it is `FALSE`.
  The two are separate functions; the table of defined terms keeps the rule by inclusion or by meaning with each entry.
- Where: `usca-definitions.l4`, section `Process: Gov. Code § 22, Code Civ. Proc. § 17(b)(7)`.

**F-22: "Law is a solemn expression of the will of the supreme power of the State."**
- Text: Civ. Code § 22.
- Question: is the sentence a definition (an expression is a law only if it is both a solemn expression and an expression of that will) or a description of what law is?
- Taken: a definition, so both limbs are needed (`an expression is a law`).
  § 22.1 then lists how the will of the supreme power is expressed (the Constitution, the statutes), and that list is a separate function.
- Where: `usca-canons-of-reading.l4`, section `Civ. Code § 22 and § 22.1: law and the will of the supreme power`.

**F-23: "Every other remedy is a special proceeding."**
- Text: Code Civ. Proc. § 21 divides "these remedies", the judicial remedies of § 20, into actions and special proceedings; § 22 says what an action is; § 23, "Every other remedy is a special proceeding".
- Question: does "every other remedy" reach a remedy that is not a judicial remedy under § 20?
- Taken: no.
  "Every other remedy" is every other judicial remedy, the remedies § 21 divides; a remedy that is not a judicial remedy is `REFUSE`d.
- Where: `usca-remedies-and-actions.l4`, function `the class of the judicial remedy`.

**F-criminal: a criminal action is never defined in the deposit.**
- Text: Code Civ. Proc. § 24 says actions are civil or criminal; § 22 lists the purposes of an action (the declaration, enforcement or protection of a right, the redress or prevention of a wrong, the punishment of a public offense); § 30 says a civil action is prosecuted for the first two; § 31 says "The Penal Code defines and provides for the prosecution of a criminal action".
- Question: is an action brought for the punishment of a public offense a criminal action?
- Taken: yes; § 24 gives two kinds and § 30's civil purposes do not include it.
  An action for any other purpose is `REFUSE`d, since § 22 does not list that purpose.
- Where: `usca-remedies-and-actions.l4`, function `the kind of an action brought for`.

**F-28: depriving an owner of the benefit of property in a way § 28 does not name.**
- Text: Code Civ. Proc. § 28, an injury to property "consists in depriving its owner of the benefit of it, which is done by taking, withholding, deteriorating, or destroying it"; § 29, "Every other injury is an injury to the person".
- Question: an act that deprives the owner of the benefit by some other way: an injury to property, or (by § 29) an injury to the person?
- Taken: `REFUSE`.
  Reading § 29 literally would call it an injury to the person only by ignoring what § 28 says depriving "is done by".
  An act that does not deprive the owner of the benefit is an injury to the person (§ 29).
- Where: `usca-remedies-and-actions.l4`, function `the kind of an injury`.

**F-25c: the conversion factors of Gov. Code § 25(c).**
- Text: a rate in dollars on each $100 of assessed value at a 25 percent ratio "may be multiplied by a conversion factor of twenty-five hundredths of 1 percent to determine a rate comparable to a rate expressed as a percentage of full value", and a rate "expressed as a percentage of full value may be multiplied by a factor of 400" for the reverse.
- Question: is a rate expressed as a percentage the figure (1 for 1 percent) or the fraction it stands for (0.01)?
- Taken: the fraction.
  Only that reading makes the factors agree: 0.0025 times 400 is 1.
  Read as the figure, the second factor would turn a rate of $4 on each $100 into 400 instead of back into 4.
  The same factors come out of subdivision (b), which asks for the same tax revenue (the tests check this with independent arithmetic).
- Where: `usca-assessed-value.l4`, section `Gov. Code § 25(c): the two conversion factors`.

**F-7.8: "irrespective of whether there shall be more than one such person representing a director".**
- Text: Gov. Code § 7.8; § 7.5 says "Not more than one director shall be represented by such a deputy at any meeting or session".
- Question: does § 7.8 lift § 7.5's limit on the number of directors represented, or allow several persons to represent the same director?
- Taken: it lifts the limit for the State Allocation Board (the three Directors it names); whether several persons may represent the same director is `REFUSE`d for more than one.
- Where: `usca-deputies.l4`, functions `this many directors may be represented by deputies at a meeting under` and `more persons may represent the same director at a meeting under Section 7.8`.

**F-7.6f: "not more than one officer subject to this section shall be represented by a deputy subject to this section".**
- Text: Gov. Code § 7.6(f), at any meeting or session of the State Lands Commission.
- Question: does a director represented under § 7.5 or § 7.9 count?
- Taken: no; "this section" is § 7.6, so only officers designating under § 7.6 are counted.
- Where: `usca-deputies.l4`, function `this many officers may be represented at a meeting of the State Lands Commission under Section 7.6`.

**F-proclaim-once: "shall proclaim" without "annually".**
- Text: Gov. Code §§ 6708-6711 ("The Governor shall proclaim September 28th to be known hereafter as ...") against the others ("annually", "each year", "of each year").
- Question: does the duty of §§ 6708-6711 recur each year?
- Taken: `REFUSE` for a year after the first; the fixed date is computed for any year.
- Where: `usca-proclaimed-days.l4`, function `the section directs a proclamation every year`.

**F-6720: April 24 on a Sunday.**
- Text: Gov. Code § 6720, the days of remembrance run from "the Sunday before that day through the following Sunday".
- Question: when April 24 is itself a Sunday, is that day "the Sunday before"?
- Taken: `REFUSE` for such a year (2022 is one); otherwise the Sunday strictly before and strictly after.
- Where: `usca-proclaimed-days.l4`, function `the days the Governor is directed to proclaim under`.

**F-between: "between 9 p.m. and 10 p.m."**
- Text: Gov. Code § 6726(b) and (d).
- Question: are the instants 21:00 and 22:00 inside?
- Taken: `REFUSE` at those two instants; strictly between is inside, strictly outside is not, and a different day is not.
  (The same question for sunrise and sunset is F-daytime.)
- Where: `usca-proclaimed-days.l4`, function `the moment falls in the lights-out hour of Space Day`.

**Not a fork: three codes, three lists of persons.**
Gov. Code § 17 names eight kinds of person; Civ. Code § 14(a) and Code Civ. Proc. § 17(b)(6) name others (the corporation among them).
Each list is encoded as its code states it and every lookup in `usca-definitions.l4` takes the code, so there is no choice to make here; which code reaches another statute is F-governs.

### After the independent test pass (version 0.2.1)

Eight entries were added, and F-9605b (in the pass-1 part of this register) was rewritten.
The table at the end says where each of the test author's nineteen ambiguities (Z1-Z19: Z1-Z15 are in its `ANSWERS.md`, Z16-Z19 were added in its report) is registered.

**F-business-day: "business day" is defined once.**
- Text: Civ. Code § 9 defines "business day" (every day other than a holiday of § 7, with a proviso for an act by a bank); Gov. Code § 6706 and § 6707, Civ. Code § 11 and Code Civ. Proc. § 13 say "the next business day" and define nothing.
- Question: does Civ. Code § 9 govern the others?
  Is a Saturday a business day for Gov. Code § 6706 and Code Civ. Proc. § 13?
  (§ 6707 names "a Saturday or holiday" and so treats Saturday as no business day for that filing.)
- Taken: no function decides it.
  The functions for "the next business day" take the business-day calendar as an input; `a business day under Civ. Code § 9` is offered as one such calendar, and under it a Saturday is a business day for an act not made through a bank.
  `the latest day for filing with a state agency` moves a last day on a Saturday itself, as § 6707 says.
- Where: `usca-interpretation-time.l4`, `the next business day after`, and `usca-holidays.l4`, `a business day under Civ. Code § 9`.

**F-sat-civ7: is a Saturday a holiday of Civ. Code § 7 through Gov. Code § 6702?**
- Text: Civ. Code § 7, holidays are "every Sunday and such other days as are specified or provided for as holidays in the Government Code"; Gov. Code § 6702, "Every Saturday from noon to midnight is a holiday as regards the transaction of business in the public offices of the state and political divisions where laws, ordinances, or charters provide that public offices shall be closed on holidays".
- Question: does § 6702 make a Saturday "provided for as a holiday" for Civ. Code § 7, so that it is not a "business day" under § 9?
- Readings: (1) no: § 6702 makes part of a Saturday a holiday for the business of certain offices only, and § 7 is read as the days of §§ 6700 and 6701; (2) yes.
- Taken: (1).
  `a holiday under Civ. Code § 7` is Sundays and the days of §§ 6700 and 6701; § 6702 is a function of the moment (`the moment falls in the Saturday holiday of Gov. Code § 6702`), not of the day.
  So under Gov. Code § 6800 and Civ. Code § 10 alone a last day on a Saturday is not excluded; Code Civ. Proc. § 12a(a) names Saturday and does exclude it (F-holiday).
  For an act by a bank, Civ. Code § 7.1(b) makes every Saturday an optional bank holiday.
- Where: `usca-holidays.l4`, `a holiday under Civ. Code § 7` and `a business day under Civ. Code § 9`.

**F-year-governs: does the 365-day year of Gov. Code § 6803 reach the other codes?**
- Text: Gov. Code § 6803 ("Year" means a period of 365 days; "half year," 182 days; "quarter of a year," 91 days) sits in the Government Code's chapter on computation of time; Civ. Code § 14(b)(4) and Code Civ. Proc. § 17(b)(4) define "month" and nothing else of time.
- Question: is "year" in the Civil Code, the Code of Civil Procedure or another statute 365 days?
- Taken: yes, for every kind of enactment.
  `the last day of a period of n u counted from d` takes no kind of enactment, so 365 days is the only year the encoding offers (F-governs dispatches holidays and months by kind, not years).
  A reader who thinks "year" in the Civil Code is a calendar year has no function for it; F-year says the text defines no calendar year.
- Where: `usca-interpretation-time.l4`, `last day of n periods of fixed length`.

**F-6703b: Veterans Day on a Saturday or a Sunday.**
- Text (`GOV-ss-6700-6736.txt:46-47`): offices of the state "shall be closed on November 11, Veterans Day.
  If, in a given year, November 11 falls on a Saturday, then ... closed on Friday, November 10.
  If ... on a Sunday, then ... closed on Monday, November 12."
- Question: when November 11 falls on a Saturday or a Sunday, is the office closed on November 11 itself as well, or only on the day named?
- Readings: (1) both, since the first sentence is unconditional and the others add a day; (2) the day named replaces November 11.
- Taken: (1).
  `Gov. Code § 6703 requires public offices of the state to be closed on the day` is `TRUE` for 11 November whatever its weekday and for the Friday or the Monday.
  A Saturday is in any case a holiday from noon where laws close offices (§ 6702).
- Where: `usca-holidays.l4` (pass 1), `Gov. Code § 6703 requires public offices of the state to be closed on the day`; `usca-further-asks.l4` extends it by body.

**F-6703leg: the Legislature on Admission Day.**
- Text: § 6703(a), "Public offices of the state, state institutions, and the University of California shall be closed on Admission Day"; (b) names "all state agencies and the Legislature" among "Public offices of the state and state institutions" for Veterans Day.
- Question: is the Legislature among the "public offices of the state" of (a)?
- Taken: `REFUSE`: (a) does not name it, and (b) names it for Veterans Day only.
  The Legislature on Veterans Day is `TRUE`.
- Where: `usca-further-asks.l4`, `Gov. Code § 6703 requires the body to be closed on the day`.

**F-6704county: a county and Saturday holidays.**
- Text: § 6704, "The legislative body of any city or district may, by ordinance or resolution, provide that every Saturday is a holiday" for its public offices; § 6701(d) lets a county board of supervisors give county employees an alternate day for a § 6700 holiday that falls on a Saturday, which is another thing.
- Question: may a county make every Saturday a holiday under § 6704?
- Taken: `Gov. Code § 6704 gives the body the power to make every Saturday a holiday for its public offices` is `FALSE` for a county board of supervisors: this section does not give it; whether another provision does is not in the deposit.
- Where: `usca-further-asks.l4`.

**F-22.1: is the list in Civ. Code § 22.1 exhaustive?**
- Text: "The will of the supreme power is expressed: (a) By the Constitution. (b) By statutes."
- Question: does anything else express it?
- Taken: `REFUSE` for "something else": the list names two and does not say there are no more.
- Where: `usca-canons-of-reading.l4`, `the will of the supreme power is expressed by`.

**F-otherwise: "unless otherwise expressed", "unless the context otherwise requires".**
- Text: the sections that yield to a contrary provision are Gov. Code § 5 ("the provision or the context otherwise requires"), § 6702 ("unless otherwise provided by charter, ordinance or resolution"), § 7 ("unless this code expressly provides otherwise"), § 8 ("unless expressly provided otherwise"), § 9604 ("unless a contrary intent appears"), § 9612 ("unless the context otherwise requires"), § 6804 and Civ. Code § 14(b)(4) and Code Civ. Proc. § 17(b)(4) ("unless otherwise expressed"), Civ. Code § 14(b) and Code Civ. Proc. § 17(b) ("unless otherwise apparent from the context"), and Civ. Code § 12 and Code Civ. Proc. § 15 ("unless it is otherwise expressed in the Act giving the authority").
- Question: when the contrary provision applies, what does the section say governs?
  Nothing: each says only that it yields.
- Taken: the answer depends on what the function asks (see "Reading a result").
  `FALSE` (the section's own rule does not apply): `the general provisions of the Government Code govern the construction of the code` (§ 5); `a power of a public officer may be exercised, or a duty performed, by` a deputy or a person authorised pursuant to law (§ 7); `Gov. Code § 9604 deems a reference to be a reference to the restatements and continuations`; `a term in a statute is deemed to include the United States Air Force` for the four named terms (§ 9612); `Gov. Code § 6804 gives the word month the meaning of a calendar month`; `Civ. Code § 14(b) and Code Civ. Proc. § 17(b) give the word the signification they state`.
  `REFUSE` (the outcome is decided by the contrary provision): `a notice, report, statement or record required or authorized by the Government Code is made as the code requires` (§ 8); `a joint authority may be exercised by those acting` (Civ. Code § 12, Code Civ. Proc. § 15); `public offices of a city are closed on the day under Gov. Code § 6702`.
  The two kinds were not made uniform; doing so is a change to pass-1 functions.
- Where: the functions named, in `usca-operation-of-statutes.l4`, `usca-general-provisions.l4`, `usca-holidays.l4` and `usca-further-asks.l4`.

**Where the test author's nineteen ambiguities are.**

| Item | Subject | Registered as |
|---|---|---|
| Z1 | Gov. Code § 9600(a): the January 1 next following, and whether the first day is excluded | F-commence (the 90th day that is itself a January 1 refuses; the day of enactment is excluded; the other counting is named in the entry and not offered) |
| Z2 | Gov. Code § 6800: a holiday after a holiday last day | F-run |
| Z3 | "business day" defined only in Civ. Code § 9 | F-business-day (new) |
| Z4 | Saturday as a holiday of Civ. Code § 7 through Gov. Code § 6702 | F-sat-civ7 (new) |
| Z5 | Sunday as a holiday for Code Civ. Proc. § 12a | F-holiday |
| Z6 | Gov. Code § 6803: the leap-day pair when 28 February is the excluded first day | F-pair |
| Z7 | whether the year of Gov. Code § 6803 reaches the other codes | F-year-governs (new) |
| Z8 | March 31 when observed elsewhere | F-6701c |
| Z9 | Veterans Day itself when it is a Saturday | F-6703b (new) |
| Z10 | Gov. Code § 6720 when April 24 is a Sunday | F-6720 |
| Z11 | Gov. Code § 9605(b): conclusive against presumed | F-9605b (rewritten) |
| Z12 | a county's power over Saturday holidays | F-6704county (new) |
| Z13 | whether Civ. Code § 22.1 is exhaustive | F-22.1 (new) |
| Z14 | the equinox, the new moon, Diwali, Good Friday | not a fork: inputs (F-holiday, last bullet; the equinox is an input of `usca-proclaimed-days.l4`) |
| Z15 | Code Civ. Proc. § 12c: a backward count landing on a holiday | F-backward |
| Z16 | Gov. Code § 7.8: "more than one such person representing a director" | F-7.8 (kept refusing) |
| Z17 | Gov. Code § 6808(b): which clock the 2 a.m. change is read on, and the repeated hour in November | F-dst (the readings from 1 a.m. to 2 a.m. refuse and the message names both questions) |
| Z18 | Gov. Code § 9600(a): the moment within the day | F-moment |
| Z19 | "unless otherwise expressed" patterns | F-otherwise (new) |

### Scope

**F-scope-1: the cluster itself.**
- California has no single interpretation act; § 9603 says "The general rules for the construction of statutes are contained in the preliminary provisions of the different codes".
  The scope (Gov. Code §§ 1-26, Civ. Code §§ 1-23.6, Code Civ. Proc. §§ 1-34, Gov. Code §§ 6700-6736, §§ 6800-6808, §§ 9600-9612) was fixed when the subject was stubbed; the stub calls it "an assumption ... not a ruling".
- Taken: the whole cluster, section by section, each rule tagged with its section; the Penal Code and the Evidence Code preliminary provisions and the many sections on construction found outside the six deposited files are not in scope.
- Consequence: the rules for "another State statute" (F-governs) are the least secure part, since a statute in a code whose preliminary provisions are not deposited may carry its own definitions.

## Jural relations

Hohfeld's correlatives: a claim (right) is matched by a duty; a privilege (liberty) by a no-right; a power by a liability; an immunity by a disability.
Each relation is stated once in the L4 rule, from the side of the party who holds the right, privilege, power or immunity, and named neutrally; the table gives both sides so that nothing is written twice in the code.
A provision may appear on more than one row, once for each relation it creates.
Where the text names no claimant for a duty (for example the duty of the Governor to proclaim a day), the row says "none named in the text"; the encoding does not supply one.

| Provision | Holder of the right, privilege, power or immunity | Other party (duty, no-right, liability or disability) | Kind | The L4 rule |
|---|---|---|---|---|
| Gov. Code § 3; Code Civ. Proc. § 6 | a person who holds an office under an act the code repeals and continues (claim to hold it according to its former tenure) | the State (duty not to end the tenure) | right / duty | `a holder of an office under a repealed act continues to hold it under Gov. Code § 3`; `a holder of an office under a repealed Act continues to hold it under Code Civ. Proc. § 6 and § 7` |
| Code Civ. Proc. § 7 | the Legislature, by repealing an act no code continues (power to end the office) | the person who held the office (liability: the office ceases when the codes take effect) | power / liability | `a holder of an office under a repealed Act continues to hold it under Code Civ. Proc. § 6 and § 7` |
| Gov. Code § 4; Civ. Code § 6; Code Civ. Proc. § 8 (first limb) | a party to an action or proceeding commenced before the code takes effect, and the holder of a right accrued before (immunity) | the code (disability: it does not affect them) | immunity / disability | `the section protects an action, proceeding or accrued right from the code` |
| Gov. Code § 4; Code Civ. Proc. § 8 (second limb) | none named in the text | the parties and courts of a proceeding begun before the code (duty: procedure thereafter taken must conform to the code) | duty (no claimant named) | `procedure taken after the code took effect in a proceeding begun before must conform to the code` |
| Civ. Code § 3; Code Civ. Proc. § 3 | a person whose act or right predates the code (immunity from its retroactive operation) | the code (disability: no part is retroactive unless expressly so declared) | immunity / disability | `a part of the Civil Code or the Code of Civil Procedure is retroactive` |
| Gov. Code § 7 | a public officer on whom a power or duty is imposed (power to have it exercised or performed by a deputy or by a person the officer authorises pursuant to law) | the deputy or the person authorised (liability), unless the code expressly provides otherwise | power / liability | `a power of a public officer may be exercised, or a duty performed, by` |
| Gov. Code § 7.5 | the director of a state department who is by law a member of a state board (power to designate a deputy director in a position the Constitution specifies) | the deputy director designated (liability: acts in the director's place, is counted for a quorum, votes) and the body (liability: counts the deputy) | power / liability | `Gov. Code § 7.5 lets the director designate`; `a designated deputy may do the act in the officer's place` |
| Gov. Code § 7.5 (second sentence) | the body and its other members (immunity from being represented by deputies of more than one director at a meeting) | a second director (disability) | immunity / disability | `this many directors may be represented by deputies at a meeting under` |
| Gov. Code § 7.5, § 7.6(a), § 7.8, § 7.9(a) (last sentence of each) | none named in the text (those affected by the deputy's acts) | the officer who designated (duty: answers for the deputy's acts as for the deputy's official duties) | duty (no claimant named) | `the officer is responsible for the act of the deputy` |
| Gov. Code § 7.6(a) | an officer whose office the Constitution creates and who is by law a member of a state board (power to designate a deputy of the office in a position the Constitution specifies) | the deputy designated and the body (liability) | power / liability | `Gov. Code § 7.6(a) lets the officer designate`; `a designated deputy may do the act in the officer's place` |
| Gov. Code § 7.6(b) | the Lieutenant Governor (power to designate any person in the office in a position the Constitution specifies) | the person designated (liability) | power / liability | `Gov. Code § 7.6(b) lets the Lieutenant Governor designate` |
| Gov. Code § 7.6(b), § 7.6(e), § 7.9(c) | the Senate, the Regents, the Trustees (and, for the Superintendent of Public Instruction, the State Board of Education): immunity from a deputy of the Lieutenant Governor or of the Superintendent | the Lieutenant Governor, the Superintendent of Public Instruction (disability: may not appoint a deputy at their meetings) | immunity / disability | `a deputy may not be appointed to act for the officer at meetings of` |
| Gov. Code § 7.6(c) | the Chief Justice (power to designate a judge or employee of a state court, or an employee of the Administrative Office of the Courts) | the person designated (liability) | power / liability | `Gov. Code § 7.6(c) lets the Chief Justice designate` |
| Gov. Code § 7.6(d) | the Attorney General (power to designate any employee of the office) | the employee designated (liability) | power / liability | `Gov. Code § 7.6(d) lets the Attorney General designate` |
| Gov. Code § 7.6(d) (second sentence) | the body of which the Attorney General is presiding officer (immunity from a designee presiding in the Attorney General's place) | the Attorney General's designee (disability) | immunity / disability | `a person designated by the Attorney General may act as presiding officer in the Attorney General's place` |
| Gov. Code § 7.6(e) | the Superintendent of Public Instruction (power to designate a person in the office in a position specified in Art. IX § 2.1) | the person designated (liability) | power / liability | `Gov. Code § 7.6(e) lets the Superintendent of Public Instruction designate` |
| Gov. Code § 7.6(f) | the State Lands Commission and its other members (immunity from deputies of more than one officer subject to § 7.6) | a second officer subject to § 7.6 (disability) | immunity / disability (fork F-7.6f) | `this many officers may be represented at a meeting of the State Lands Commission under Section 7.6` |
| Gov. Code § 7.7 | a public officer's power under § 7 (immunity from modification by §§ 7.5 and 7.6) | §§ 7.5 and 7.6 (disability: they do not affect or modify § 7) | immunity / disability | `the section affects or modifies Section 7` |
| Gov. Code § 7.8 | the Directors of Finance, General Services and Education (power to appoint any deputy or assistant director in the department to act on the State Allocation Board) | the deputy or assistant director and the board (liability); the one-director limit of § 7.5 does not bind them (fork F-7.8) | power / liability | `Gov. Code § 7.8 lets the director designate`; `more persons may represent the same director at a meeting under Section 7.8` |
| Gov. Code § 7.9(a) | the Controller, the Treasurer, the Director of Finance and the Superintendent of Public Instruction (power to designate any deputy of the office to sit on any state board) | the deputy and the body (liability) | power / liability | `Gov. Code § 7.9(a) lets the officer designate`; `a designated deputy may do the act in the officer's place` |
| Gov. Code § 7.9(b), § 7.9a | the Controller and the Treasurer (power to request, § 7.9(b)); the Controller (power to request, § 7.9a) | the authority that classifies and compensates (liability to the request, then duty to classify two employees at category level IV or V); the two employees have the correlative claim | power / liability, then claim / duty | `Gov. Code § 7.9(b) requires two employees of the officer to be classified as career executives`; `Gov. Code § 7.9a requires two more employees of the officer to be classified as career executives`; `the career executive may be classified at` |
| Gov. Code § 8 | none named in the text | a person who makes a notice, report, statement or record the code requires or authorises (duty: make it in writing in the English language unless expressly provided otherwise) | duty (no claimant named) | `a notice, report, statement or record required or authorized by the Government Code is made as the code requires` |
| Gov. Code § 16.5(a) | a party to a written communication with a public entity (power to affix a digital signature), and the public entity (power to elect to use it) | the public entity (liability: the signature has the force and effect of a manual signature if the public entity elects and the five attributes are embodied) | power / liability | `a digital signature has the same force and effect as a manual signature` |
| Gov. Code § 16.5(b) | a public entity (immunity from being required to use or permit a digital signature) | any party (disability) | immunity / disability | `a public entity is required to use or permit the use of a digital signature` |
| Gov. Code § 16.5(c) | a person who employs a digital signature under Public Resources Code § 71066 (immunity from § 16.5) | § 16.5 (disability: it does not apply to such a signature) | immunity / disability | `Gov. Code § 16.5 applies to the digital signature` |
| Gov. Code § 16.5(e) | a public entity or government agency (privilege to use and accept an electronic signature as defined in Civ. Code § 1633.2(h)) | anyone relying on § 16.5 to limit it (no-right) | privilege / no-right | `Gov. Code § 16.5 limits the right of a public entity or government agency to use and accept it` |
| Gov. Code § 6700(b) | the parties to a memorandum of understanding under Chapter 12 of Division 4 of Title 1 (power to displace § 6700 for those it covers), unless its provisions require the expenditure of funds | the State employer and employees covered (liability); the Legislature holds an immunity from provisions that need money until it approves them in the annual Budget Act | power / liability; immunity / disability | `the memorandum of understanding controls over Gov. Code § 6700`; `further legislative action is needed before the memorandum of understanding controls` |
| Gov. Code § 6701(c) | the Legislature (power to observe March 31 on a Friday or Monday near it) | those for whom the holiday is observed (liability) | power / liability (fork F-6701c: the caller supplies the observed day) | `the days on which the Legislature may observe March 31 of the year` and `Gov. Code § 6701(c) lets the Legislature observe March 31 on the day` in `usca-further-asks.l4` (which days); whether March 31 itself stays a holiday is an input in `usca-holidays.l4` (`March 31 itself stays a holiday in a year in which it is observed on another day`) |
| Gov. Code § 6701(d) | the board of supervisors of a county (power to provide an alternate holiday for county employees other than court attaches) | the county employees (liability) | power / liability | `a holiday for an employee of a county, taking in the alternate days of Gov. Code § 6701(d)`; who holds the power: `Gov. Code § 6701(d) lets the body provide an alternate day for a holiday falling on` in `usca-further-asks.l4` |
| Gov. Code § 6702 (second sentence) | a person issuing, filing, serving, executing or recording legal process or a written instrument in the Saturday holiday (privilege) | anyone who would invalidate it (no-right) | privilege / no-right | `legal process may be issued, filed, served, executed or recorded in the Saturday holiday of Gov. Code § 6702` |
| Gov. Code § 6702 (third sentence) | none named in the text | the public offices of a city (duty to be closed on the holidays enumerated in § 6700, unless a charter, ordinance or resolution provides otherwise) | duty (no claimant named; fork F-6702city) | `public offices of a city are closed on the day under Gov. Code § 6702` |
| Gov. Code § 6703 | none named in the text | the public offices of the state, state institutions, the University of California (Admission Day) and the Legislature (Veterans Day) (duty to be closed) | duty (no claimant named) | `Gov. Code § 6703 requires public offices of the state to be closed on the day`; by body (the University of California, the Legislature): `Gov. Code § 6703 requires the body to be closed on the day` in `usca-further-asks.l4` |
| Gov. Code § 6704 | the legislative body of a city or district (power to provide that every Saturday is a holiday for its offices) | the public offices of the city or district (liability) | power / liability | `a Saturday is a holiday for the public offices of a city or district under Gov. Code § 6704`; who holds the power, and the duty to provide for essential services: `Gov. Code § 6704 gives the body the power to make every Saturday a holiday for its public offices` and `Gov. Code § 6704 requires provision for the continuance of essential public services such as police and fire protection` in `usca-further-asks.l4` |
| Gov. Code § 6705 (second paragraph) | none named in the text | courts and public offices (duty to be open and function normally on a special or limited holiday appointed by the President or Governor); the contracting parties (duty to perform as usual) | duty (no claimant named) | `courts and public offices are open on a special or limited holiday appointed by the President or Governor`; the contracting parties: `Gov. Code § 6705 has a contract performed and business transacted as usual by the party on a special or limited holiday` in `usca-further-asks.l4` |
| Gov. Code § 6706, § 6707; Civ. Code § 11; Code Civ. Proc. § 13 | the person who must perform an act on a day that falls on a holiday (privilege to perform it on the next business day with the same effect) | the other party and the agency (no-right to treat it as late) | privilege / no-right | `the latest day on which an act appointed for`; `the latest day for filing with a state agency, when the last day is` |
| Code Civ. Proc. § 13a, § 13b | the person required to act on a day or within a period (privilege, not duty, to act on a special holiday or a Saturday) | the other party (no-right to object) | privilege / no-right | `an act required by law on a day or within a period may be performed on` |
| Code Civ. Proc. § 12a(a) | the person who must act within a period whose last day is a holiday (privilege: the period is extended to the next day that is not a holiday) | whoever would treat the act as late (no-right) | privilege / no-right (forks F-holiday, F-run) | `extended to the next day that is not a holiday` |
| Civ. Code § 9 | the person obligated to perform an act appointed for an optional bank holiday (privilege to perform it on the next succeeding business day, or on that day if the bank is open) | the other party (no-right to insist on the optional bank holiday) | privilege / no-right | `an act appointed for an optional bank holiday may be performed on that day itself`; `the next business day after an optional bank holiday on which an act was appointed for a bank` |
| Civ. Code § 12; Code Civ. Proc. § 15 | a majority of three or more public officers or persons given a joint authority (power to exercise it) | the minority and those subject to the authority (liability) | power / liability | `a joint authority may be exercised by those acting` |
| Civ. Code § 17; Code Civ. Proc. § 11 | a person who must mail a notice by registered mail (privilege to use certified mail) | the recipient (no-right to insist on registered mail) | privilege / no-right | `a requirement of the Civil Code or the Code of Civil Procedure that a notice be mailed by registered mail is met by` |
| Civ. Code § 18, § 19 | a person who relies on a fact (power to treat another as having constructive notice of it) | a person with actual notice of circumstances that put a prudent person on inquiry (liability to be charged with constructive notice) | power / liability | `a person has constructive notice of the fact itself under Civ. Code § 19` |
| Civ. Code § 22.2 | none named in the text (the parties to a case) | the courts of the State (duty to decide by the common law of England so far as not repugnant to the Constitutions or the laws) | duty (no claimant named) | `the common law of England is the rule of decision` |
| Gov. Code § 9606 (first sentence) | the Legislature (power to repeal any statute at any time) | persons acting under the statute (liability) | power / liability | `a statute may be repealed` |
| Gov. Code § 9606 (first sentence, exception; second sentence) | the holder of a vested right (immunity from repeal that would impair it) | the Legislature (disability); persons acting under a statute act in contemplation of the power | immunity / disability | `a statute may be repealed`; `the person acts in contemplation of the power of repeal` |
| Gov. Code § 9608 | the State, through the prosecuting authority (power to indict and punish an act already committed) | the person who committed the act (liability), unless the intention to bar is expressly declared | power / liability | `the termination or suspension of a criminal law bars indictment, information and punishment` |
| Gov. Code § 9610 | the State (immunity from a claim for salary founded on the salary statute alone) | a State officer or employee (no-right to payment until moneys are made available by another provision of law) | immunity / no-right | `a statute fixing the salary of a State officer or employee is an appropriation of money for it`; `the salary fixed by statute shall be paid` |
| Code Civ. Proc. § 32 | the person with the right to prosecute either a civil or a criminal remedy for one violation (immunity: the right to prosecute one is not merged in the other) | the court and the other proceeding (disability: no merger) | immunity / disability | `the right to prosecute one remedy is merged in the other` |
| Code Civ. Proc. § 33 | a prosecuting attorney (privilege, in discretion, to assist in the civil resolution of a Title 13 offense in lieu of a criminal complaint) | the person alleged to have violated it (no-right to either course) | privilege / no-right | `a prosecuting attorney may assist in the civil resolution of a violation in lieu of filing a criminal complaint` |
| Code Civ. Proc. § 34 | a court or judicial officer (power to give a paper the effect of an original signature by an electronic signature) | a person affected by the paper (liability) | power / liability | `an electronic signature is as effective as an original signature under Code Civ. Proc. § 34` |
| Gov. Code §§ 6708-6729, 6731(b), 6733, 6735, 6736 | none named in the text | the Governor (duty to proclaim the day or month, annually in all but §§ 6708-6711, where F-proclaim-once) | duty (no claimant named) | `the proclamations of Gov. Code §§ 6708-6736`; `the days the Governor is directed to proclaim under`; `the section directs a proclamation every year` |
| Gov. Code § 6726(a), (b), (d) | none named in the text | the Governor (duty to proclaim, to encourage schools, residents, businesses and public entities, and to direct the Department of General Services to turn off the nonessential lights); the Department of General Services (duty, once directed, to turn them off) | duty (no claimant named) | `the Governor is to direct the Department of General Services to turn off the light on Space Day`; `the moment falls in the lights-out hour of Space Day` |
| Gov. Code § 6726(a), (b) (what is not asked) | a school, educational institution, resident, business or public entity (privilege: nothing is required of it) | the Governor (no-right to its participation) | privilege / no-right | `a school, educational institution, resident, business or public entity is required to take part in Space Day` |
| Gov. Code § 6808(c) | the Legislature (power to amend § 6808 by a two-thirds vote to change the dates and times of daylight saving time, consistent with federal law, or to provide for year-round daylight saving time if federal law authorises it) | those subject to the standard time of the State (liability) | power / liability | `Gov. Code § 6808(c) lets the Legislature make the amendment` |
| none: the sections below create no relation between two parties (a definition, a counting rule, a rule of construction, a statement of intent, a short title, a classification) | none | none | none | the functions named against each in the coverage table |

**The sections with no relation** (the last row of the table; 88 of the 159 sections, with the 7 numbers the ranges skip, which are not provisions and create nothing): Gov. Code §§ 1, 2, 5, 6, 9, 10, 11, 12, 12.2, 12.5, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 6800, 6801, 6802, 6803, 6804, 6805, 6806, 6807, 9600, 9602, 9603, 9604, 9605, 9607, 9609, 9611, 9612; Civ. Code §§ 1, 2, 4, 5, 7, 7.1, 10, 13, 14, 20, 21, 22, 22.1, 23, 23.1, 23.2, 23.3, 23.4, 23.5, 23.6; Code Civ. Proc. §§ 1, 2, 4, 5, 9, 10, 12, 12b, 12c, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32.5.
Each of these appears in the coverage table with its disposition.
The reading used is the one a lay reader would give; where a section could be read as creating a relation and the text is unclear, the fork register says so (F-6702city, F-7.8, F-7.6f, F-proclaim-once).
`Gov. Code § 14` ("shall" is mandatory and "may" is permissive) is in the last row: it does not create a relation itself, but it is what tells a reader whether the other sections create a duty or a privilege.

## Changes to existing modules

Two pass-1 files were edited after the independent test pass, both for one defect, and two pass-2 files were edited for one small addition.
Every other pass-1 file is what pass 1 left: the modification time of `usca-interpretation-time.l4`, `usca-holidays.l4`, `usca-general-provisions.l4`, the five other pass-1 test files, `tests-red.l4`, `check.sh`, `srcrefs.py`, `BRIEF-pass1.md` and `SOURCE-LICENSE.md` is still the one of the copy this run started with (29 October 2026, 15:06:24 local), and the two files below are the only ones of them that differ.

1. **`usca-operation-of-statutes.l4` (pass 1): the function `the statute that prevails when two statutes of one session amend the same section first second` (Gov. Code § 9605(b); `GOV-ss-9600-9612.txt:22-23` is paragraph (b)(2)).**
   Before: when the two statutes had the same `order of enactment` the function refused with "Gov. Code § 9605(b)(1) turns on which statute is enacted last; two statutes with the same order of enactment have none", before it looked at the chapter numbers.
   After: for the same order of enactment (b)(1) has no statute "enacted last" and (b)(2) alone decides: the higher chapter rank prevails (an even-year statute ranking above every odd-year one), unless that statute says it is not to prevail, or the ranks are equal; those two cases refuse with the new message "Gov. Code § 9605(b)(2) gives no presumption between two statutes of the same order of enactment when their chapter ranks are equal or the statute with the higher chapter number expressly provides that it is not to prevail, and (b)(1) has no statute enacted last".
   For different orders of enactment nothing changed (the other two messages and every other branch are as pass 1 left them).
   The old message no longer exists anywhere in the deposit.
   Why: (b)(2) is a presumption of its own and does not wait for (b)(1); the refusal was a defect of the encoding, not a reading of the text.
   The change is four lines of the function body and three lines of comment above it.
2. **`test-usca-operation.l4` (pass 1): one assertion's expected value flipped, and 11 assertions were added.**
   The assertion over `(a statute 2 7 FALSE FALSE) (a statute 2 9 FALSE FALSE)` was `#ASSERT REFUSED ... BECAUSE "Gov. Code § 9605(b)(1) turns on which statute is enacted last; ..."`.
   It now says `EQUALS the second statute` (chapter 9 over chapter 7), with its mirror, and is followed by the cases the test author's fix list asked for: Chapter 700 against Chapter 650 of one order, in both argument positions; a 2026 statute of Chapter 5 against a 2025 statute of Chapter 900 of one order (the even-year rule), in both positions; the higher-numbered statute saying it is not to prevail (refused, in both positions, with the new message); the lower-numbered one saying so (the higher still prevails); equal chapter ranks (refused); and, to show that different orders are unchanged, Chapter 700 of order 1 against Chapter 650 of order 2 (refused as before) and Chapter 650 of order 1 against Chapter 700 of order 2 (the second).
   That is 12 assertions in place of 1; the file went from 123 to 134 satisfied, and it still has no `-- assertions written` line, as pass 1 left it.
3. **`usca-canons-of-reading.l4` and `test-usca-canons.l4` (pass 2, the encoder's own).**
   `Element of the text` gained `a subdivision heading` and `a paragraph heading`, which `the element may affect the scope, meaning or intent of the provisions of the Government Code` refuses (Gov. Code § 6 names title, division, part, chapter, article and section headings); two assertions with their messages were added (90 to 92).
4. **Bookkeeping**: `NOTES.md` (rewritten), `encoding.json`, `PROGRESS.md`, `dispositions.tsv` (three rows moved, notes corrected), `coverage.py` and the new `extras.tsv` (a list of functions appended to the "where" cell of the rows they answer).

Added, not changed: `usca-further-asks.l4` and `test-usca-further-asks.l4`.

No pass-1 or pass-2 assertion other than the one of item 2 had its expected value changed.
The reconciled `tests-independent.l4` of the test author, run in a scratch copy of this deposit, gives 625 satisfied, 0 failed and 0 refused (S487 is asserted `REFUSED`: F-9605b); run in the folder that held the modules before the repair it gave 622 satisfied, 0 failed and 3 refused (S485, S486 and S487).

## Findings

Numbered; 1-7 are from pass 1 (2026-10-22), 8-20 from pass 2 (2026-10-29).
Each says how it was found.

1. **L4's `MODULO` fails on a non-integer operand** (pass 1).
   The first version of the whole-number test used `n MODULO 1 EQUALS 0`, which crashed on 1.5 ("Expected an Integer").
   The modules now use `FLOOR n EQUALS n`.
   For whoever maintains the runtime; not a finding about the statute.
2. **Pass 1's own expectations that were wrong against the text** (pass 1): 1 November 2025 is on daylight saving time; 8 November 2026 is a Sunday; 4 July 2026 is a Saturday and so a Code Civ. Proc. § 12a(a) holiday; 1 January 2026 is not a Code of Civil Procedure holiday unless § 135 is supplied.
   Corrected from the text, not from the module.
3. **The deposit has no general rule that deems a notice or service made on some day after it is sent** (pass 1): both functions refuse (F-deemed-service).
4. **The leap-day pair of Gov. Code § 6803 is ambiguous** (pass 1): two readings are offered (F-pair).
5. **A month with no day of the start day's number** (pass 1): the text says only "calendar month"; refused (F-month).
6. **Gov. Code § 9600(a): a January 1 that ends the 90-day period** (pass 1): "next following" is not answered (F-commence).
7. **`tests-red.l4` fails 8 times on purpose** (pass 1): each assertion states what a naive reading gives.
8. **The three codes differ on the tenses** (pass 2): Gov. Code § 11 says the present includes the past; Civ. Code § 14(a) and Code Civ. Proc. § 17(a) say nothing of the past (F-tense).
   Found by reading the three sentences side by side while writing `usca-canons-of-reading.l4`.
9. **A bug in my own new function, caught by its own test** (pass 2): in `a word used in the tense includes the tense, in`, the Government Code branch first returned `FALSE` for "the future tense includes the past".
   The text does not say that the future includes the past (§ 11 says the present includes the past and future, and the future the present), so the answer is `REFUSE`; the function was changed, not the expectation.
   No pass-1 module is affected.
   This is the one assertion that failed against new code on a first run in this pass.
10. **Gov. Code § 25(c)'s two conversion factors agree only on one reading** (pass 2): 0.0025 times 400 is 1 only if a rate "expressed as a percentage" is the fraction it stands for (F-25c).
    The independent arithmetic in `test-usca-assessed.l4` (the tax a rate produces on a property of a given full value, before and after restating the rate) confirms the same factors from subdivision (b).
11. **Code Civ. Proc. §§ 28 and 29 cannot both be applied literally** (pass 2): an injury to the owner's benefit by some other way than the four named is, by § 29, an injury to the person, yet § 28 says depriving "is done by" those four (F-28).
12. **The deposit never defines a criminal action** (pass 2): Code Civ. Proc. § 31 hands that to the Penal Code, which is not deposited (F-criminal).
13. **Gov. Code § 7.8 and § 7.6(f) each have a phrase that can be read two ways** (pass 2) (F-7.8, F-7.6f).
14. **Gov. Code § 6720 breaks in 2022, and Space Day has a boundary** (pass 2): a calendar fact (April 24, 2022 was a Sunday) turns the days of remembrance into a case the text does not answer (F-6720); "between 9 p.m. and 10 p.m." does not say whether the end instants are inside (F-between).
15. **Gov. Code §§ 6708-6711 do not say "annually"** (pass 2): the duty may be a single proclamation (F-proclaim-once).
16. **No section of Gov. Code §§ 6708-6736 calls its day a holiday** (pass 2), and Gov. Code § 6709 proclaims January 15 while § 6700(a)(3) makes the third Monday in January the holiday: the proclaimed day and the holiday differ (F-hol-6).
17. **Gov. Code § 6726(a), (b) and (d) put every duty on the Governor** (pass 2): the text asks nothing of a school, resident, business or public entity, and `a school, educational institution, resident, business or public entity is required to take part in Space Day` is `FALSE`.
18. **Pass 1's table had 166 rows; the units of the text are 406** (pass 2): the sections were 159 and each subdivision, list item and defined term was inside a section's row.
    Counted by `units.py` from the text, not by hand; 48 sections that pass 1 called `not applicable` and 29 it called `inert` were re-judged (see the audit).
19. **Every module draws one lint hint from the compiler** (pass 2): `A module that declares nothing is English; this line can go.` at `@lang en` (severity Hint).
    The brief requires `@lang en`, so the line stays; `check.sh` counts errors, failed and refused assertions only, and does not count hints.
    Measured on 2026-10-29 with the binary above on all eleven modules (a module that imports others draws the hint once for each, so the count per module is 1 to 3).
20. **`check.sh` does not see quotations or locators** (pass 2): it counts error diagnostics and assertion lines only.
    `srcrefs.py check --refs` is the second check, and a positive control shows it is not hollow: one word altered in a quotation of `usca-deputies.l4`, in a scratch copy, gave 1 problem.
21. **Gov. Code § 9605(b)(2) was never reached for two statutes enacted at the same time** (repair, found by the independent test pass).
    The pass-1 function refused for every pair with the same order of enactment, saying that (b)(1) turns on which statute is enacted last.
    But (b)(2) does not depend on (b)(1): it decides by chapter number, and a Chapter 700 and a Chapter 650 of one day got no answer.
    The pass-1 test had asserted the refusal, which is why the suite was green.
    Repaired in place and logged under "Changes to existing modules"; the reading choices that remain are in F-9605b.
22. **A list the caller leaves out is a silent failure, and Code Civ. Proc. § 135 is the sharp case** (found by the test author, scenarios S375 and S605).
    With no § 135 day supplied, the Code of Civil Procedure functions answer `FALSE` for 25 December, with no diagnostic.
    Sorted and stated under "Reading a result"; a loud variant was added for § 135 and not for the other eight lists.
23. **The "unless otherwise" sections do not all answer the same way** (found by reading the functions while writing "Reading a result").
    Some answer `FALSE` once the exception holds and some refuse; the sorting is in F-otherwise.
    A one-sentence rule ("the encoding refuses once the contrary provision applies") would have been wrong for five of the eleven functions.
24. **76 of the 665 scenarios of the independent test pass had no function to ask** (the rest of the file, 625 assertions, ran).
    The 76 are the numbers of `ANSWERS.md` that do not appear as `S<n>` in `tests-independent.l4`, computed by script, then each sorted by hand: 53 are rules the text states that no function let a caller ask (they now have one), 23 are not rules a function could compute.
    The table is below.

### The 76 scenarios the encoding had no function for

How they were found: the test author wrote 665 numbered scenarios (`ANSWERS.md`, written from the text before any module was opened); `tests-independent.l4` carries an assertion for every number that appears as `S<n>` in it; the 76 that do not appear are the gaps.
That subtraction was done by script when this file was built, and the build stops if the sorted list below does not equal it.
Each gap was then sorted by hand:
- **(b) a rule the text states that no function let a caller ask**: 53 scenarios, now answered by a function (the test author's expected answer is in the second column; the expected values of `test-usca-further-asks.l4` were decided from the text and a calendar before its first run).
- **(a) not a rule a function could compute**: 23 scenarios, left as stated limits: dates the text does not compute (Lunar New Year, Diwali), dates in history notes, counts of divisions, parts and classes, short-title and citation rows (inert), and sections not deposited.
  Each has its reason in the last column.

| Scenario | The test author's scenario and expected answer | Kind | Answered by, or why it is left |
|---|---|---|---|
| S14 | [GOV 6] The heading of a subdivision or paragraph does not affect meaning => NOT COVERED (GOV 6 names title, division, part, chapter, article and section headings only) | (b) | canons: `the element may affect the scope, meaning or intent of the provisions of the Government Code` now takes `a subdivision heading` and `a paragraph heading`, which it refuses (the section names six kinds of heading) |
| S76 | [GOV 12.5] The declaration about "man"/"men" is amendatory of existing law => FALSE (declaratory) | (b) | `the declaration of Gov. Code § 12.5 or § 24 is amendatory of existing law`, FALSE |
| S83 | [GOV 14] "Must" is mandatory => NOT COVERED | (b) | `the force of the word as written in Gov. Code § 14`, which refuses "must" |
| S95 | [GOV 16.5(a)(5)] Latest date for the Secretary of State's initial regulations => 1997-01-01 | (b) | `the latest date for the Secretary of State's initial regulations under Gov. Code § 16.5(a)(5)`, 1 January 1997 |
| S96 | [GOV 16.5(a)(5)] Public hearings the Secretary must hold before adopting the regulations, at least => 1 | (b) | `the fewest public hearings the Secretary of State must hold before adopting the regulations under Gov. Code § 16.5(a)(5)`, 1 |
| S122 | [GOV 24] The declaration on "workers' compensation" is amendatory of existing law => FALSE (declaratory) | (b) | `the declaration of Gov. Code § 12.5 or § 24 is amendatory of existing law`, FALSE |
| S191 | [GOV 6701(c)] 2026-03-31 is a Tuesday: the Legislature may observe on the preceding Friday 2026-03-27 => TRUE | (b) | `the days on which the Legislature may observe March 31 of the year`; `Gov. Code § 6701(c) lets the Legislature observe March 31 on the day` |
| S192 | [GOV 6701(c)] ... on the preceding Monday 2026-03-30 => TRUE | (b) | `the days on which the Legislature may observe March 31 of the year`; `Gov. Code § 6701(c) lets the Legislature observe March 31 on the day` |
| S193 | [GOV 6701(c)] ... on the following Friday 2026-04-03 => TRUE | (b) | `the days on which the Legislature may observe March 31 of the year`; `Gov. Code § 6701(c) lets the Legislature observe March 31 on the day` |
| S194 | [GOV 6701(c)] ... on the following Monday 2026-04-06 => FALSE | (b) | `the days on which the Legislature may observe March 31 of the year`; `Gov. Code § 6701(c) lets the Legislature observe March 31 on the day` |
| S195 | [GOV 6701(c)] 2025-03-31 is a Monday: the Legislature may observe on another day under (c) => FALSE | (b) | `the days on which the Legislature may observe March 31 of the year`; `Gov. Code § 6701(c) lets the Legislature observe March 31 on the day` |
| S198 | [GOV 6701(d)] 2025-07-04 is a Friday (not a Saturday): the board may provide an alternate day under (d) => FALSE | (b) | `Gov. Code § 6701(d) lets the body provide an alternate day for a holiday falling on`, a county board of supervisors only, a Saturday holiday only |
| S199 | [GOV 6701(d)] A city council may provide an alternate day under (d) => FALSE | (b) | `Gov. Code § 6701(d) lets the body provide an alternate day for a holiday falling on`, a county board of supervisors only, a Saturday holiday only |
| S207 | [GOV 6703(a)] University of California closed on Admission Day => TRUE | (b) | `Gov. Code § 6703 requires the body to be closed on the day`, by body (the University of California on Admission Day only; Veterans Day is an intent, FALSE) |
| S211 | [GOV 6703(b)] The University of California is required to close on Veterans Day (intent only) => FALSE | (b) | `Gov. Code § 6703 requires the body to be closed on the day`, by body (the University of California on Admission Day only; Veterans Day is an intent, FALSE) |
| S213 | [GOV 6704] ... must provide for continuance of essential public services (police and fire) => TRUE | (b) | `Gov. Code § 6704 requires provision for the continuance of essential public services such as police and fire protection`; `Gov. Code § 6704 gives the body the power to make every Saturday a holiday for its public offices` (a county: FALSE, F-6704county) |
| S214 | [GOV 6704] A county may do so under s.6704 => FALSE | (b) | `Gov. Code § 6704 requires provision for the continuance of essential public services such as police and fire protection`; `Gov. Code § 6704 gives the body the power to make every Saturday a holiday for its public offices` (a county: FALSE, F-6704county) |
| S215 | [GOV 6705] A holiday applying only to a special class of business or persons is a special or limited holiday => TRUE | (b) | `a holiday is a special or limited holiday under Gov. Code § 6705`; `Gov. Code § 6705 has a contract performed and business transacted as usual by the party on a special or limited holiday` |
| S216 | [GOV 6705] A holiday appointed for all classes of business and persons, generally observed => special or limited holiday => FALSE | (b) | `a holiday is a special or limited holiday under Gov. Code § 6705`; `Gov. Code § 6705 has a contract performed and business transacted as usual by the party on a special or limited holiday` |
| S220 | [GOV 6705] ... a contract with performance due on that day, by a party outside the limited class, is performed as usual => TRUE | (b) | `a holiday is a special or limited holiday under Gov. Code § 6705`; `Gov. Code § 6705 has a contract performed and business transacted as usual by the party on a special or limited holiday` |
| S221 | [GOV 6705] ... performance by the class expressly limited by the proclamation is required as usual => FALSE | (b) | `a holiday is a special or limited holiday under Gov. Code § 6705`; `Gov. Code § 6705 has a contract performed and business transacted as usual by the party on a special or limited holiday` |
| S226 | [GOV 6706] ... performance on the next business day is obligatory (not just permitted) => FALSE | (b) | `Gov. Code § 6706 requires the act to be performed on the next business day`, FALSE; `Gov. Code § 6706 applies to an act appointed to be performed on a particular day by` (a court order refuses) |
| S227 | [GOV 6706] ... the date is fixed by court order => NOT COVERED (law or contract only) | (b) | `Gov. Code § 6706 requires the act to be performed on the next business day`, FALSE; `Gov. Code § 6706 applies to an act appointed to be performed on a particular day by` (a court order refuses) |
| S231 | [GOV 6707] Last day for filing with a COUNTY agency falls on a Saturday: 6707 permits the next business day => FALSE | (b) | `Gov. Code § 6707 gives the next business day for a filing with`, a state office or agency only |
| S292 | [GOV 6804] "Month" means a calendar month, unless otherwise expressed: a "lunar month" or "30-day month" is a calendar month => FALSE | (b) | `Gov. Code § 6804 gives the word month the meaning of a calendar month` (F-otherwise) |
| S314 | [GOV 6808(b)] Hour of day at which it begins and ends => 2 a.m. (02:00) | (b) | `the clock reading, in seconds after midnight, at which daylight saving time begins and ends under Gov. Code § 6808(b)`, 7200 |
| S329 | [GOV 6801] The Gregorian calendar is used => TRUE | (b) | `Gov. Code § 6801 computes time according to the Gregorian calendar` |
| S345 | [GOV 6802] Days in 2100 => 365 | (b) | `days in the year under Gov. Code § 6802` |
| S346 | [GOV 6802] Days in 2400 => 366 | (b) | `days in the year under Gov. Code § 6802` |
| S373 | [CCP 12a(b)] 12a applies to Sections 659, 659a and 921 => TRUE | (b) | `Code Civ. Proc. § 12a applies to a period fixed by` (a contract refuses) |
| S374 | [CCP 12a(b)] 12a applies to a period fixed by a regulation (any other provision of law, "rule or regulation") => TRUE | (b) | `Code Civ. Proc. § 12a applies to a period fixed by` (a contract refuses) |
| S378 | [CCP 12b] ... a BRANCH office closed the whole day => FALSE | (b) | `Code Civ. Proc. § 12b makes the day a holiday for computing time when the office is closed for the whole of it`; `Code Civ. Proc. § 12b applies to the computation of time under` (Gov. Code § 6800 refuses) |
| S379 | [CCP 12b] ... a PRIVATE office closed the whole day => FALSE | (b) | `Code Civ. Proc. § 12b makes the day a holiday for computing time when the office is closed for the whole of it`; `Code Civ. Proc. § 12b applies to the computation of time under` (Gov. Code § 6800 refuses) |
| S381 | [CCP 12b] 12b applies for computing time under GOV 6800 => NOT COVERED | (b) | `Code Civ. Proc. § 12b makes the day a holiday for computing time when the office is closed for the whole of it`; `Code Civ. Proc. § 12b applies to the computation of time under` (Gov. Code § 6800 refuses) |
| S389 | [CCP 13a] ... is required to be performed on the special holiday => FALSE | (b) | `Code Civ. Proc. § 13a or § 13b requires an act to be performed on`, FALSE |
| S391 | [CCP 13b] ... is required to be performed on a Saturday => FALSE | (b) | `Code Civ. Proc. § 13a or § 13b requires an act to be performed on`, FALSE |
| S454 | [GOV 9602] A joint resolution not yet filed is in effect => FALSE | (b) | `a concurrent or joint resolution is in effect at the moment`, with the filing moment a `MAYBE` |
| S464 | [GOV 4] The Government Code has a general rule that no part of it is retroactive => NOT COVERED | (b) | `the code says that no part of it is retroactive unless expressly so declared` (the Government Code refuses) |
| S474 | [GOV 9604] ... a contract's reference => NOT COVERED | (b) | `Gov. Code § 9604 applies to a reference made by` (a contract or a regulation refuses) |
| S475 | [GOV 9604] ... a regulation's reference => NOT COVERED | (b) | `Gov. Code § 9604 applies to a reference made by` (a contract or a regulation refuses) |
| S484 | [GOV 9605(b)(1)] ... that presumption is conclusive (cannot be rebutted) => TRUE | (b) | `Gov. Code § 9605(b) makes the presumption conclusive` (F-9605b) |
| S496 | [GOV 9607(b)] ... the later statute does not delete or extend the date (amends other matters) => FALSE | (b) | `Gov. Code § 9607(b) revives the terminated or repealed law` |
| S499 | [GOV 9608] A law creating civil liability is terminated: pending claims for acts already done are barred => NOT COVERED | (b) | `Gov. Code § 9608 leaves an act already committed open to proceedings and punishment after the law ends` (a law creating civil liability refuses) |
| S503 | [GOV 9610] ... a county officer's salary => NOT COVERED | (b) | `Gov. Code § 9610 makes the salary fixed by statute payable only if moneys are made available by another provision of law` (a county or city officer refuses) |
| S507 | [GOV 9611] ... the modifying provision has NO stated limited period (permanent): 9611 preserves the original => FALSE | (b) | `Gov. Code § 9611 keeps the original provision from being deemed repealed` |
| S558 | [CIV 14(b)] "Spouse" includes a registered domestic partner where the context makes it otherwise apparent => FALSE | (b) | `Civ. Code § 14(b) and Code Civ. Proc. § 17(b) give the word the signification they state`; `a signification stated in Civ. Code § 14(b) or Code Civ. Proc. § 17(b) is displaced` (F-otherwise) |
| S561 | [CIV 17] Mailing by registered mail where CERTIFIED mail is required => NOT COVERED | (b) | `a requirement of the Civil Code that a notice be mailed by certified mail is met by`: certified mail yes, registered mail and any other method refuse |
| S573 | [CIV 20] The repeal affects a private statute not expressly repealed => NOT COVERED | (b) | `the repeal by the Civil Code affects a private statute`, which refuses (Civ. Code § 20 has no sentence about a private statute; Code Civ. Proc. § 18 has) |
| S584 | [CIV 22.2] An English STATUTE is the rule of decision => NOT COVERED | (b) | `Civ. Code § 22.2 makes the law of England the rule of decision in the courts of this State` (an English statute refuses) |
| S595 | [CIV 23.6] Conflicting sections in DIFFERENT chapters: 23.6 decides by numerical order => FALSE | (b) | `Civ. Code § 23.6 makes the section last in numerical order prevail`, with a yes-or-no for "same chapter or article" |
| S603 | [CCP 9] ... the Code prescribes NO limitation: the time already run counts toward the Code's period => FALSE | (b) | `Code Civ. Proc. § 9 deems the time already run part of the time the code prescribes`, with a yes-or-no for "the code prescribes the same or any limitation" |
| S641 | [CCP 17(b)] A definition in (b) is displaced where otherwise apparent from the context => TRUE | (b) | `Civ. Code § 14(b) and Code Civ. Proc. § 17(b) give the word the signification they state`; `a signification stated in Civ. Code § 14(b) or Code Civ. Proc. § 17(b) is displaced` (F-otherwise) |
| S663 | [CCP 33] ... the attorney is required to do so => FALSE | (b) | `Code Civ. Proc. § 33 requires a prosecuting attorney to assist in the civil resolution of a violation`, FALSE |
| S1 | [GOV 1] Short title of the code => "Government Code" | (a) | inert, reason 2: the short title of the Government Code (Gov. Code § 1); no fact an individual states changes anything |
| S135 | [GOV 26] The content of that meaning (Water Code s.13050(n) is not deposited) => NOT COVERED | (a) | the content of the meaning is in Water Code § 13050(n), which is not deposited; a fact the caller supplies (Gov. Code § 26) |
| S173 | [GOV 6700(a)(4)] The date of Lunar New Year in 2026 computed from the text alone (second new moon after winter solstice) => NOT COVERED (needs astronomical data) | (a) | the date of Lunar New Year needs astronomical data the text does not give; an input of `Days supplied by the caller` (F-holiday) |
| S174 | [GOV 6700(a)(9)] The date of Diwali in 2026 computed from the text alone => NOT COVERED (needs the Hindu lunar calendar) | (a) | the date of Diwali needs the Hindu lunar calendar; an input of `Days supplied by the caller` (F-holiday) |
| S276 | [GOV 6736] Section in force on 2026-09-19 => FALSE | (a) | the date a section is in force is in its history note ("Effective September 20, 2026"); the deposit holds one version of each section and no function reads a history note (F-vintage) |
| S277 | [GOV 6736] Section in force on 2026-09-20 => TRUE | (a) | as S276 |
| S278 | [GOV 6736] Governor required to proclaim Dolly Parton Day in 2025 => FALSE | (a) | as S276: the year in which the duty begins follows from the history note |
| S385 | [CCP 12c] The number of additional days for service by mail => NOT COVERED | (a) | the added days for service by mail are in a section not deposited (Code Civ. Proc. § 1013); `the last day to act, when the act is due` takes them as an input |
| S465 | [GOV 6736] Current text effective date => 2026-09-20 | (a) | as S276: the effective date of Gov. Code § 6736 is a history note |
| S466 | [GOV 6808] Current text effective date (approved in Proposition 7, election 2018-11-06) => 2018-12-19 | (a) | as S276 (Gov. Code § 6808) |
| S467 | [GOV 6700] Current text effective date => 2026-03-26 | (a) | as S276 (Gov. Code § 6700) |
| S468 | [GOV 6701] Current text effective date => 2020-06-29 | (a) | as S276 (Gov. Code § 6701) |
| S469 | [GOV 6703] Current text effective date => 2011-01-01 | (a) | as S276 (Gov. Code § 6703) |
| S470 | [GOV 6700] Whether 2025-03-31 was a holiday under the text in force on that date (the deposit holds only the 2026 text) => NOT COVERED | (a) | needs the version of Gov. Code § 6700 in force on 2025-03-31, which is not deposited (F-vintage, Q-vintage) |
| S514 | [CIV 1] Number of divisions of the Civil Code => 4 | (a) | inert, reason 1: the divisions of the Civil Code are listed in Civ. Code § 1; a count of them is not a rule |
| S515 | [CIV 1] Division II relates to => Property | (a) | inert, reason 1: as S514 |
| S575 | [CIV 21] The Code may be cited simply as => "The Civil Code" (adding the section number) | (a) | inert, reason 2: how the Civil Code may be cited (Civ. Code § 21) |
| S576 | [CCP 19] The Code may be cited simply as => "The Code of Civil Procedure" | (a) | inert, reason 2: how the Code of Civil Procedure may be cited (Code Civ. Proc. § 19) |
| S596 | [CCP 1] Number of parts of the Code of Civil Procedure => 4 | (a) | inert, reason 1: the parts of the Code of Civil Procedure are listed in Code Civ. Proc. § 1 |
| S597 | [CCP 1] Part IV is => Miscellaneous Provisions | (a) | inert, reason 1: as S596 |
| S645 | [CCP 21] Number of classes into which judicial remedies are divided => 2 (actions; special proceedings) | (a) | the text states the count of the classes only by listing them (Code Civ. Proc. § 21); the module holds the members as an enumeration and no function counts them |
| S648 | [CCP 24] Kinds of action => 2 (civil; criminal) | (a) | as S645 (Code Civ. Proc. § 24) |
| S652 | [CCP 27] Kinds of injury => 2 (to the person; to property) | (a) | as S645 (Code Civ. Proc. § 27) |

## Answer table (worked cases)

Every cell below is the value as run; it equals the value written down before the run.

How these were made.
The expected values were written down on 2026-10-21 from the statute text and an independent forward-simulating script (not part of the deposit), before the first run of `usca-interpretation-time.l4`.
They were then evaluated with `l4 run` (one `#EVAL` per cell, 63 in all, the first six sections of `test-usca-worked.l4` and the month-end neighbours of the one-month case) and compared with the values written down.
Result: 63 evaluations, 0 differences.
The same cells are `#ASSERT`s in `test-usca-worked.l4`, all satisfied, so a later change that moves a cell turns the file red.
No cell of this table was edited after a run.
Expectations elsewhere that were corrected after a failing run are listed under "What `check.sh` prints".

Calendars used for the rest-day input (the caller supplies one; the module hard-codes none):

- **G**: Gov. Code § 6800 / Civ. Code §§ 7, 10: Sundays and the days Gov. Code §§ 6700(a) and 6701(a)-(b) fix by the calendar; no Saturdays; no appointed or lunar days.
- **C**: Code Civ. Proc. §§ 10, 12a(a): every Saturday and every Sunday; no § 135 days (§ 135 is not deposited) and no § 12b closures.
- **C+**: C, with the days of G supplied as the § 135 days. That supply is an assumption of the test, not a reading of the text, which does not say what § 135 contains.

"run" is the run-extending reading of the last-day rule (CCP § 12a(a): "to and including the next day that is not a holiday"); "step" is the one-step reading of "it is also excluded" (Gov. Code § 6800, Civ. Code § 10, CCP § 12) applied once.

| period, counted from | last day before the rest-day rule | G (run / step) | C (run / step) | C+ (run / step) | licensed by |
|---|---|---|---|---|---|
| three years from 2025-07-16 | 2028-07-16 (Sunday) | 2028-07-17 / 2028-07-17 | 2028-07-17 / 2028-07-17 | 2028-07-17 / 2028-07-17 | Gov. § 6803 (365 days; the leap day 2028-02-29 and 2028-02-28 are in the period and count as one, so 1096 calendar days), § 6800 |
| five years from 2025-01-15 | 2030-01-15 (Tuesday) | same | same | same | § 6803, § 6800 (leap day of 2028 in the period; 2032 is not) |
| five years from 2025-09-01 | 2030-09-01 (Sunday) | 2030-09-03 / 2030-09-02 | 2030-09-02 / 2030-09-02 | 2030-09-03 / 2030-09-02 | § 6803, § 6800; Monday 2030-09-02 is the first Monday in September (Gov. § 6700(a)(13)) |
| thirty days from 2026-01-01 | 2026-01-31 (Saturday) | 2026-01-31 / 2026-01-31 | 2026-02-02 / 2026-02-01 | 2026-02-02 / 2026-02-01 | § 6800; CCP § 12a(a) makes Saturday a holiday, Gov. § 6700 does not |
| two years from 2024-02-28 | reading S: 2026-02-27 (Friday); reading P: 2026-02-28 (Saturday) | S: 2026-02-27 both; P: 2026-02-28 both | S: 2026-02-27 both; P: 2026-03-02 / 2026-03-01 | S: 2026-02-27; P: 2026-03-02 / 2026-03-01 | § 6803: the day before the added day is 2024-02-28, the excluded first day (§ 6800), so under S the pair does not "occur in" the period |
| one year from 2024-02-29 | 2025-02-28 (Friday) | same | same | same | § 6803 (2024-02-28 is before the period; no pair), § 6800 |
| one month from 2025-01-31 | the text does not say (no 31 February; § 6804 says only "calendar month") | REFUSED | REFUSED | REFUSED | § 6804, § 6800 |

Commencement (Gov. Code § 9600, § 9602):

| case | expected from the text |
|---|---|
| an Act enacted 2026-03-10 at a regular session, none of the § 9600(b) kinds, saying nothing about its own commencement | day: 2027-01-01 (the 90-day period from 2026-03-10 ends 2026-06-08; the next January 1 following it); moment within the day: the text does not say, REFUSED |
| the same Act is an urgency statute, calls an election, levies a tax or appropriates for the usual current expenses | day: 2026-03-10, "immediately upon their enactment", at the moment of enactment (a supplied input) |
| an Act that fixes its own day, later fixed as 2026-06-01 | the text does not say (§ 9600 names no exception for an Act that fixes its own day): day REFUSED, moment REFUSED. A caller who takes the Act's own day to govern gets 2026-06-01, by that assumption alone |
| subordinate legislation made 2026-03-10 and silent | the deposited text has no provision (§ 9600 speaks of statutes, § 9602 of resolutions): REFUSED |
| Civil Code and Code of Civil Procedure themselves | noon, 1873-01-01 (Civ. § 2, CCP § 2); the Government Code's own day is not in the deposit: REFUSED |
| boundary of § 9600(a) | enacted 2026-10-02: 2027-01-01; enacted 2026-10-03: REFUSED (the 90th day is 2027-01-01 itself, and the text does not say whether a January 1 that ends the period is "followed" by that January 1); enacted 2026-10-04: 2028-01-01 |

**Worked cases of the pass-2 modules.**
Each cell is an `#ASSERT` in the test file named, written from the text before the file's first run, and satisfied in the final run.

| case | value | test file |
|---|---|---|
| the day Gov. Code § 6709 directs the Governor to proclaim, in 2026 | 15 January 2026 (the holiday of § 6700(a)(3) is the third Monday, 19 January; 15 January is not a holiday) | `test-usca-proclaimed-days.l4` |
| § 6712 (fourth Friday in September) in 2026 and 2027 | 25 September 2026; 24 September 2027 | same |
| § 6720 in 2026 and in 2022 | 19 to 26 April 2026; 2022 REFUSED (24 April 2022 was a Sunday) | same |
| § 6718 in 2028 | 1 to 29 February 2028 | same |
| § 6726, Space Day in 2026 and 2027; 21:30 on the day; exactly 21:00 | 1 May 2026; 7 May 2027; inside; REFUSED | same |
| Gov. Code § 7.5: the director is by law a member, the person is a deputy director of the department, in a position the Constitution specifies | the director may designate (TRUE); with no such position, FALSE; two directors represented at one meeting, FALSE | `test-usca-deputies.l4` |
| Gov. Code § 7.9(b): the Controller requests; three employees hold permanent civil service status and are designated deputies; only one does | TRUE; REFUSED | same |
| Gov. Code § 25: full value 1,000,000 in the 1980-81 and the 1981-82 fiscal year; a rate of $4 on each $100 restated for 1981-82 | assessed value 250,000 and 1,000,000; 0.01 | `test-usca-assessed.l4` |
| Code Civ. Proc. §§ 22, 23: an ordinary proceeding in a court by which one party prosecutes another for the redress of a wrong; the same for some other purpose | action; special proceeding | `test-usca-remedies.l4` |
| Gov. Code § 6801: the day reckoned as the first day of the year 1753 and 1752 | 1 January 1753; 1752 REFUSED | `test-usca-further-limbs.l4` |
| Gov. Code § 11 and Civ. Code § 14(a): does the present tense include the past | Government Code: TRUE; Civil Code: REFUSED (F-tense) | `test-usca-canons.l4` |
| the statute that prevails: Chapter 700 against Chapter 650, enacted on the same day | the first (Chapter 700) | `test-usca-operation.l4` |
| the same, a 2026 statute of Chapter 5 against a 2025 statute of Chapter 900 | the 2026 statute (an even-year statute is deemed higher) | same |
| the days on which the Legislature may observe March 31, in 2026 and in 2025 | 27 March, 30 March and 3 April 2026 (31 March 2026 is a Tuesday); none in 2025 (a Monday) | `test-usca-further-asks.l4` |
| days in the year 2100 and 2400 under Gov. Code § 6802 | 365; 366 | same |
| is the Legislature required to close on Admission Day (9 September 2026), and the University of California on Veterans Day | REFUSED (F-6703leg); FALSE (an intent only) | same |
| is 25 December 2026 a holiday under Code Civ. Proc. § 10 with no Section 135 day supplied | the older function: FALSE, silently; the `... the Section 135 days being` function: REFUSED when the list is not given, FALSE when it is given as empty, TRUE when it is given as 25 December | same |

## What `check.sh` prints

**Target: `unstable`.**
Run as `L4_TARGET=unstable L4=<L4_BIN> ./check.sh` from this folder, with `L4_BIN` the binary under "Target, build and layout".
`l4 --version` prints `unstable-20261028-5e95b5a (unstable, 5e95b5a, 2026-10-28)`; the binary's sha256 is `0f0f1b86d37164af242ca2b6c03aa31ddeedef752bd10474f1459b78cf539e9d`.
With the target `unstable`, `check.sh` skips the `main` comparison, so there are no main columns and no main build to name.

The output of the final run on 2026-10-29, taken after the last change to any `.l4` file, verbatim (standard output, then the line on standard error and the exit status):

```
module                                    errors satisfied  failed  refused  expected
test-usca-assessed.l4                          0        30       0        0         0
test-usca-canons.l4                            0        92       0        0         0
test-usca-definitions.l4                       0       129       0        0         0
test-usca-deputies.l4                          0       130       0        0         0
test-usca-further-asks.l4                      0       181       0        0         0
test-usca-further-limbs.l4                     0        46       0        0         0
test-usca-general.l4                           0        98       0        0         0
test-usca-holidays.l4                          0       627       0        0         0
test-usca-operation.l4                         0       134       0        0         0
test-usca-proclaimed-days.l4                   0        94       0        0         0
test-usca-remedies.l4                          0        46       0        0         0
test-usca-rules.l4                             0       334       0        0         0
test-usca-time.l4                              0       425       0        0         0
test-usca-worked.l4                            0        89       0        0         0
tests-red.l4                                   8         0       8        0         8
usca-assessed-value.l4                         0         0       0        0         0
usca-canons-of-reading.l4                      0         0       0        0         0
usca-definitions.l4                            0         0       0        0         0
usca-deputies.l4                               0         0       0        0         0
usca-further-asks.l4                           0         0       0        0         0
usca-further-limbs.l4                          0         0       0        0         0
usca-general-provisions.l4                     0         0       0        0         0
usca-holidays.l4                               0         0       0        0         0
usca-interpretation-time.l4                    0         0       0        0         0
usca-operation-of-statutes.l4                  0         0       0        0         0
usca-proclaimed-days.l4                        0         0       0        0         0
usca-remedies-and-actions.l4                   0         0       0        0         0
TOTAL (27 modules)                             8      2455       8        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
[stderr] check.sh: the target is unstable, so the main check was skipped.
[exit status 0]
```

**The baseline it replaces** (pass 1's last run, taken again on 2026-10-29 before any change with the binary above; its 1,696 satisfied are the pass-1 files' numbers, and after the repair they are 1,707, since `test-usca-operation.l4` has 11 more):

```
TOTAL (11 modules)                             8      1696       8        0
```

**How to read it.**
The `errors` column counts error diagnostics, and a failed assertion is also one, so in `tests-red.l4` the 8 errors are the 8 failed assertions; `expected` is the count `check.sh` was told to expect for that file.
Every other file has 0 errors, 0 failed and 0 refused.
A refused assertion would make the run red, and there is none.
The run is green exactly when every `failed` equals its `expected`.
Pass 2 added 14 files (7 modules, 7 test files) and 565 satisfied assertions (30 + 90 + 129 + 130 + 46 + 94 + 46); 2,261 = 1,696 + 565.
The repair after the independent test pass added 2 files (`usca-further-asks.l4`, `test-usca-further-asks.l4`) and 194 satisfied assertions (181 in the new test file, 11 in `test-usca-operation.l4`, 2 in `test-usca-canons.l4`); 2,455 = 2,261 + 194, over 27 modules.
`#ASSERT REFUSED ...` counts as satisfied when the expression refuses.
The pass-1 tests give the refusal message (`BECAUSE`); 102 of the 109 `#ASSERT REFUSED` lines of the pass-2 tests do not, so they show that something refuses, not which `REFUSE` fired.

**Expected failures: `tests-red.l4`, 8 assertions.**
Each states the answer a naive reading gives and the text does not support, so a failure is the module disagreeing with the naive reading.
`check.sh` carries the count in its `expected_failed` table and `encoding.json` in `expected_red`.

| # | The naive answer asserted | The answer the text supports |
|---|---|---|
| 1 | three years from 2025-07-16 end 2028-07-15 (1,095 days) | 2028-07-16: the leap pair of 2028 counts once (Gov. Code § 6803) |
| 2 | five years from 2025-01-15 end 2030-01-14 | 2030-01-15, same reason |
| 3 | five years from 2025-09-01 end 2030-08-31 | 2030-09-01, same reason |
| 4 | ten days from 2026-03-10 end 2026-03-19 (the first day counts) | 2026-03-20 (Gov. Code § 6800 excludes the first day) |
| 5 | thirty days from 2026-01-01 end 2026-02-02 on a calendar of Sundays only | 2026-01-31: a Saturday is not a holiday on that calendar, and § 6700 names no Saturday |
| 6 | the one-step function gives the run answer, 2026-03-17 (last day Saturday 2026-03-14, with Sunday 15 and Monday 16 March also holidays) | the run reading of Code Civ. Proc. § 12a(a) gives 2026-03-17, from the run function; the one-step function returns 2026-03-15, so the assertion fails |
| 7 | a statute enacted 2026-03-10 takes effect 2026-06-08 | 2027-01-01 (Gov. Code § 9600(a)) |
| 8 | daylight saving time is not in effect at 3 a.m. on 8 March 2026 | it is (Gov. Code § 6808(b): commences at 2 a.m.) |

**What else was checked, and with what result** (measured on 2026-10-29 against the files as they stand):
- `python3 -I srcrefs.py check --refs ../../registers/source-bundle/CCP-ss-1-34.txt <module>` (every quotation is the deposited line, and every `@ref` locator names lines that exist; the other five raw files are found beside the one named, by their `ID.txt`), one run per module:

  ```
  usca-interpretation-time: srcrefs check: 67 src: lines, 18 runs, 76 locators, 0 problems
  usca-holidays: srcrefs check: 69 src: lines, 13 runs, 39 locators, 0 problems
  usca-operation-of-statutes: srcrefs check: 40 src: lines, 23 runs, 43 locators, 0 problems
  usca-general-provisions: srcrefs check: 82 src: lines, 14 runs, 31 locators, 0 problems
  usca-canons-of-reading: srcrefs check: 26 src: lines, 13 runs, 32 locators, 0 problems
  usca-definitions: srcrefs check: 36 src: lines, 30 runs, 34 locators, 0 problems
  usca-remedies-and-actions: srcrefs check: 28 src: lines, 12 runs, 16 locators, 0 problems
  usca-proclaimed-days: srcrefs check: 37 src: lines, 27 runs, 29 locators, 0 problems
  usca-deputies: srcrefs check: 28 src: lines, 19 runs, 28 locators, 0 problems
  usca-assessed-value: srcrefs check: 7 src: lines, 7 runs, 7 locators, 0 problems
  usca-further-limbs: srcrefs check: 12 src: lines, 11 runs, 11 locators, 0 problems
  usca-further-asks: srcrefs check: 57 src: lines, 35 runs, 50 locators, 0 problems
  ```

  A positive control: in a scratch copy of `usca-deputies.l4`, one word of a quotation was altered and the same command reported 1 problem; the real module reports 0.
- `--strict`, which also wants the lines each locator cites to be the lines quoted in the run directly above it:

  ```
  usca-interpretation-time: srcrefs check: 67 src: lines, 18 runs, 76 locators, 23 problems
  usca-holidays: srcrefs check: 69 src: lines, 13 runs, 39 locators, 13 problems
  usca-operation-of-statutes: srcrefs check: 40 src: lines, 23 runs, 43 locators, 0 problems
  usca-general-provisions: srcrefs check: 82 src: lines, 14 runs, 31 locators, 5 problems
  usca-canons-of-reading: srcrefs check: 26 src: lines, 13 runs, 32 locators, 0 problems
  usca-definitions: srcrefs check: 36 src: lines, 30 runs, 34 locators, 0 problems
  usca-remedies-and-actions: srcrefs check: 28 src: lines, 12 runs, 16 locators, 0 problems
  usca-proclaimed-days: srcrefs check: 37 src: lines, 27 runs, 29 locators, 0 problems
  usca-deputies: srcrefs check: 28 src: lines, 19 runs, 28 locators, 0 problems
  usca-assessed-value: srcrefs check: 7 src: lines, 7 runs, 7 locators, 0 problems
  usca-further-limbs: srcrefs check: 12 src: lines, 11 runs, 11 locators, 0 problems
  usca-further-asks: srcrefs check: 57 src: lines, 35 runs, 50 locators, 0 problems
  ```

  The pass-1 problems are the same as pass 1 reported (23, 13 and 5): the locator cites lines that the same module quotes somewhere other than directly above the locator, or cites a whole section where the run above it quotes part; no quoted line differs from the file.
  The brief does not ask for the strict mode; the pass-2 modules are clean under it (two problems found in `usca-remedies-and-actions.l4` and `usca-proclaimed-days.l4` were fixed).
  The pass-1 modules were left as they are (no pass-1 file is edited).
- Coverage: `python3 -I coverage.py check` says every one of the 406 units has exactly one disposition and every rule of `dispositions.tsv` is used; the coverage table was generated from it.
  Every module and section heading named in the table was checked to exist in the module it names, by script.
- **Mutation check of the tests (pass 1 only: it covers the four pass-1 modules as they were before the repair, and was not repeated for the eight modules added since)** (a scratch script, written for this run, removed at the end, so it is not in the row; run on 2026-10-22 on the files as shipped; afterwards only the header comments of `test-usca-time.l4` and `test-usca-holidays.l4` were reworded, and no assertion changed).
  It applies one change at a time to a module (swap `PLUS` and `MINUS`, `AND` and `OR`, `GREATER THAN` and `AT LEAST`, `LESS THAN` and `AT MOST`, `EQUALS` and `GREATER THAN`, `THEN TRUE` and `THEN FALSE`; add 1 to a constant such as 365, 91, 43200, 54000, 7, 28, 29), runs the tests that import the module, and counts the mutant killed if any assertion fails or is refused, or the run errors.
  It leaves out comments, names in backticks and the text of refusal messages.
  Result: 366 mutants, 357 killed (356 by a failed or refused assertion, 1 by another error), 9 survived.

  | module | mutants | killed | survived |
  |---|---|---|---|
  | `usca-interpretation-time.l4` | 131 | 128 | 3 |
  | `usca-holidays.l4` | 191 | 188 | 3 |
  | `usca-operation-of-statutes.l4` | 21 | 18 | 3 |
  | `usca-general-provisions.l4` | 23 | 23 | 0 |

  The 9 survivors, each read and none a hole in a test:
  - `usca-holidays.l4`, the two `PLUS 7` to `MINUS 7` mutants in the helpers for "the n-th" and "the last" weekday of a month (lines 55 and 62): the number sits inside `( ... ) MODULO 7`, and `MODULO` takes the floor, so adding or subtracting 7 leaves the remainder as it was (measured with a probe of `(0 MINUS 3) MODULO 7`, which is 4).
  - `usca-holidays.l4` line 244, `LESS THAN 54000` to `AT MOST 54000`: the two readings differ only at the instant 3 p.m., which the line above refuses ("does not say whether the instant of 3 p.m. is inside"). The neighbouring mutant, 54000 to 54001, did not survive: half-second readings test it.
  - `usca-interpretation-time.l4` line 175, the starting guess `Day firstDay PLUS units` of the search that finds the day on which a count of units ends: the search repeats until its guess reproduces itself, so a different start reached the same day on every input the tests use. Not proved for every input.
  - `usca-interpretation-time.l4` line 409, `GREATER THAN sunrise` and `LESS THAN sunset` each to the inclusive form: they differ only at the instants of sunrise and sunset themselves, which an earlier line refuses (fork F-daytime).
  - `usca-operation-of-statutes.l4` line 431 (426 when the check was run), `GREATER THAN` to `AT LEAST` on the section number of Civ. Code § 23.6: it differs only when the two numbers are equal, which the line above refuses.
  - `usca-operation-of-statutes.l4` line 194 (189 when the check was run), the same mutation on the order of enactment: it differs only when the two orders are equal, and since the repair the first branch of the function takes that case on its own and decides it from the chapter ranks, so the value is read only when the orders differ (the repair added five lines above it, and the check was not rerun on the repaired file).
  - `usca-operation-of-statutes.l4` line 196 (191 when the check was run), the same mutation on the chapter rank: the value is read only when the two ranks differ.
  Earlier runs on earlier states of the files left more survivors, and they changed the tests.
  A first run of the holiday module (189 mutants) had 29 survivors, 24 of them in Civ. Code § 7.1, 23 of those in its rules (q) and (r) (a Monday after a Sunday holiday, a Friday before a Saturday holiday), which only a few hand-picked dates tested; whole-year tests of § 7.1 against a Python rendering of the section were added.
  A second run, on the lines then changed, still had survivors in the same rule, because no year from 2024 to 2030 has January 1 on a Sunday (2023 and 2034 do), so the range of the whole-year tests was widened to 2022-2035.
  It also had a survivor at the Good Friday boundary (54000 to 54001) that only a reading between whole seconds can tell apart; half-second tests were added.
- Not run: the independent test pass of the skill (step 8), a mutation check of the eight modules added since pass 1 (for `test-usca-further-asks.l4` a control of two mutants was run, and both were caught), and any run against `main`.

## What to do before relying on this encoding

1. **Have a lawyer qualified in California read it against the official text.**
   The deposit is a converter-made rendering; nothing here was checked against the official text, and no domain expert has read this encoding.
2. **Rule on the forks that change an answer in practice**, in this order of likely effect: F-from, F-run and F-holiday (the last day of a period); F-commence and F-own-day (when a statute takes effect); F-hol-6 (whether a proclaimed day is a holiday); F-tense and F-process (which code's wording governs a word); F-7.8 and F-7.6f (deputies).
   Each entry of the fork register states the readings seen and the one the code takes.
3. **Supply the inputs the text does not give**: the judicial holidays of Code Civ. Proc. § 135, the days of Lunar New Year, Diwali, Good Friday and Thanksgiving Day, the days appointed by the President or Governor, the equinox, the Constitution's positions, the meaning of "recycled water" (Water Code § 13050(n)).
4. **Run the independent test pass again on this version.**
   Step 8 was run once, before the repair; the repair (the 9605(b) fix and `usca-further-asks.l4`) has been tested only by the encoder's tests and by the same test author's file, which was written before it.
5. **Run a mutation check on the eight modules added after pass 1.**
   Pass 1's mutation check (366 mutants, 357 killed, 9 survived, each survivor read) covers only the four pass-1 modules; it was not repeated.
   For `test-usca-further-asks.l4` only a two-mutant control was run, to show that its assertions can fail.
6. **Read the `REFUSE` messages as the list of what the text does not answer**; a caller who needs an answer there must decide it outside the encoding.
   Add `BECAUSE` messages to the 102 pass-2 `#ASSERT REFUSED` lines that have none: as they stand, a `REFUSE` that fires for a reason other than the one intended would not be noticed.
7. **Check the version of every section.**
   Only the current version is deposited (Q-vintage); the holiday list of Gov. Code § 6700 was last amended with effect from 26 March 2026.
8. **Rule on the forks added after the test pass** (F-business-day, F-sat-civ7, F-year-governs, F-6703b, F-6703leg, F-6704county, F-22.1, F-otherwise) and on the one deliberate disagreement with the test author (F-9605b, S487).
9. **Decide whether the `--strict` layout of `@ref`s matters**: `srcrefs.py check --strict` reports problems in three pass-1 modules (see "What `check.sh` prints"); no quotation differs from the file.

## Open questions for a domain expert

Each question is one the deposited text does not answer, with the way the code leaves it.
The numbers are the fork or question identifiers used elsewhere in this file.

1. **Q-135.** What are the judicial holidays "specified in Section 135" of the Code of Civil Procedure?
   § 135 is not deposited.
   They are an input, and a caller who supplies none gets Saturdays and Sundays only under the Code of Civil Procedure calendars.
   Should the holiday function refuse unless the caller says the list is complete?
2. **Q-contract.** Do Gov. Code § 6800, Civ. Code § 10 and Code Civ. Proc. §§ 12 and 12a reach a period fixed by contract ("within 30 days of signing")?
   The sections speak of an act "provided by law"; only §§ 6706, 11 and 13 mention contract, and only for an act on a particular day.
3. **Q-commence.** Does § 6800 apply to the 90-day period of Gov. Code § 9600(a), so that the day of enactment is excluded?
   The code excludes it; counting the day of enactment as day 1 moves every boundary one day later, and the refused case from 3 October to 4 October.
   What is "next following" when the 90th day is itself a January 1?
4. **Q-own-day.** May a statute name its own day of effect, and if so does that displace § 9600(a)?
   The text of § 9600 neither allows nor forbids it, and the code refuses.
   (The Constitution is not deposited.)
5. **Q-enactment.** Is "the date of enactment" the day a bill is passed, signed or chaptered?
   It is an input.
6. **Q-moment.** From which moment of its day does a statute under § 9600(a) bind: the midnight that begins it, or another moment?
   Refused; the helper for the midnight reading is an explicit assumption.
7. **Q-governs.** Which definitions of "holiday" and "month" reach a statute of another code, and an ordinance, rule or regulation?
   The code gives another State statute the Government Code's, as an assumption, and refuses for an ordinance, rule or regulation.
8. **Q-pair.** Does the leap-day pair of Gov. Code § 6803 "occur in" a period whose excluded first day is 28 February?
   Two readings are offered; the literal one is the headline.
9. **Q-month.** What is the last day of one month from 31 January, or from the 29th to 31st of another month, when the month reached is shorter?
   The text says only "a calendar month"; the code refuses.
10. **Q-run.** After a last day that is a holiday, does the one-step exclusion of § 6800 stop at the next day, or carry on as § 12a(a) does?
    Both are offered; the run reading is the headline.
11. **Q-vintage.** Which version of each section governs a date before the deposited version took effect?
    Only the current version is deposited; the holiday list in § 6700 was last amended with effect from 26 March 2026.
12. **Q-1752.** What does § 6801 require of a date before 1752, and which hundredth years before 1900 are leap years?
    The leap-year function refuses a hundredth year before 1900; no other date is checked against 1752.
13. **Q-service.** Where is the rule that deems service or notice made on a day?
    None is in the deposit.
    If one exists it is in a part of the codes outside the six files, so both functions refuse.
14. **Q-hol-6.** Is a day proclaimed under one of Gov. Code §§ 6708-6736 a day "appointed ... for a public fast, thanksgiving, or holiday" within § 6700(a)(20)(A)?
15. **Q-6701.** Does March 31 stop being a holiday when the Legislature observes it on another day (§ 6701(c))?
    Does the Saturday stop being one for county employees when a board names an alternate day (§ 6701(d))?
    Are the days § 6701(a) and (b) add "enumerated in Section 6700" for a city's offices (§ 6702)?
16. **Q-9605b.** Which presumption of § 9605(b) governs when the statute enacted last and the statute with the higher chapter number are different statutes?
17. **Q-9607b, Q-9611.** Is the "date of termination" in § 9607(b) the last day the law operates or the first it does not?
    On which day does the original provision resume under § 9611?
18. **Q-ccp9.** In Code Civ. Proc. § 9, are the days already run counted with or without the day the code took effect?
19. **Q-12c.** Which way does a last day move that falls on a holiday when counted backward from a hearing?
    Refused.
20. **Q-scope.** Is the cluster the right one?
    The Penal Code and Evidence Code preliminary provisions, and every other code's general provisions, are outside it, and § 9603 says the rules are spread across "the different codes".
21. **Q-source.** The six `.txt` files are converter-made; is any section different in the official text?
22. **Q-FALSE.** Is the convention that `FALSE` means "this section does not give this result" the one a reviewer wants, or should those functions refuse?
    It is used, as a constant `FALSE`, for Gov. Code § 9605(a)(1) (an amended section is not repealed and re-enacted), § 9610 (a statute fixing a salary is not an appropriation), § 9611 (a temporarily suspended law is not repealed), Civ. Code § 20 and Code Civ. Proc. § 18 (the repeal by the code revives no former law) and Civ. Code § 23.2 (one of the four codes does not prevail over another by being later).
23. **Q-tense.** Do the Civil Code and the Code of Civil Procedure mean the present tense to include the past?
    Does the future include the past in the Government Code?
    The code refuses both (F-tense).
24. **Q-process.** Is "process" an open list in Gov. Code § 22 and a closed one in Code Civ. Proc. § 17(b)(7)?
    The code reads the first as open and the second as closed (F-process).
25. **Q-22.** Is Civ. Code § 22 a definition of law (both limbs needed) or a description?
    Read as a definition (F-22).
26. **Q-23.** Does "every other remedy" in Code Civ. Proc. § 23 reach a remedy that is not a judicial remedy?
    Read as no (F-23).
27. **Q-criminal.** Is an action for the punishment of a public offense a criminal action?
    Read as yes (F-criminal).
28. **Q-28.** What is an injury that deprives the owner of the benefit of property in a way other than taking, withholding, deteriorating or destroying?
    Refused (F-28).
29. **Q-25c.** Is a rate "expressed as a percentage of full value" a figure or a fraction?
    Read as the fraction (F-25c).
30. **Q-7.8.** Does Gov. Code § 7.8 lift § 7.5's one-director limit, or let several persons represent one director?
    The first is taken; the second is refused (F-7.8).
31. **Q-7.6f.** Does a director represented under § 7.5 or § 7.9 count toward the limit of § 7.6(f)?
    Read as no (F-7.6f).
32. **Q-7.9b.** What follows under Gov. Code § 7.9(b) when fewer than two employees hold permanent civil service status and have been designated deputies, and which two when more than two do?
    Refused for fewer than two; the choice of two is not modelled.
33. **Q-proclaim-once.** Does the duty of Gov. Code §§ 6708-6711 recur each year?
    Refused for a year after the first (F-proclaim-once).
34. **Q-6720.** Which Sunday does Gov. Code § 6720 mean when April 24 is a Sunday?
    Refused (F-6720).
35. **Q-between.** Are the instants 9 p.m. and 10 p.m. inside "between 9 p.m. and 10 p.m." in Gov. Code § 6726?
    Refused (F-between).
36. **Q-offset.** What is the offset of Pacific standard time from Coordinated Universal Time?
    15 U.S.C. §§ 261 and 263, which Gov. Code § 6808(a) cites, are not deposited; refused.
37. **Q-two-thirds.** What counts as "a two-thirds vote" in Gov. Code § 6808(c) (of which body, of the members or of those voting)?
    The caller says whether the vote was one.
38. **Q-business-day.** Does the definition of "business day" in Civ. Code § 9 govern Gov. Code §§ 6706 and 6707 and Code Civ. Proc. § 13?
    No function decides it (F-business-day).
39. **Q-sat-civ7.** Is a Saturday a holiday of Civ. Code § 7 through Gov. Code § 6702?
    Read as no (F-sat-civ7).
40. **Q-year-governs.** Does the 365-day year of Gov. Code § 6803 reach the Civil Code and the Code of Civil Procedure?
    Read as yes (F-year-governs).
41. **Q-6703b.** When November 11 falls on a Saturday or a Sunday, are the offices of the state closed on November 11 itself as well as on the day § 6703(b) names?
    Read as yes (F-6703b).
42. **Q-6703leg.** Is the Legislature among the "public offices of the state" that Gov. Code § 6703(a) closes on Admission Day?
    Refused (F-6703leg).
43. **Q-6704county.** May a county make every Saturday a holiday under Gov. Code § 6704?
    `FALSE` under that section; another provision is not deposited (F-6704county).
44. **Q-22.1.** Is the list in Civ. Code § 22.1 exhaustive?
    Refused for "something else" (F-22.1).
45. **Q-9605b-express.** For two statutes of one session with the same order of enactment, when the higher-numbered one says it is not to prevail, does the other prevail under § 9605(b)?
    Refused; the disclaiming statute's own words may decide it (F-9605b, S487).
46. **Q-otherwise.** When a contrary provision displaces a section that says "unless otherwise expressed" or the like, what governs?
    Nothing in the text says; the functions answer `FALSE` or refuse by what they ask (F-otherwise).

## Generators and checkers used and not shipped

Some files this document names were used while the encoding was written and are not in this folder: `coverage.py`, `dispositions.tsv`, `extras.tsv`, `units.py`.
They were scripts and tables written for one run and are not part of the encoding.
The counts and tables they produced are copied into this file, and the `.l4` modules, not the scripts, are the source of truth.
Where a script generated a module, the module in this folder is the file to edit, and its template is not shipped.
The lead keeps them outside this repository.

## Independent test pass

A separate agent that had not seen this encoding, its NOTES.md or its brief wrote `ANSWERS.md` from the text alone before it opened any `.l4` file: 665 numbered scenarios over the six deposited files.
It then wrote `tests-independent.l4`, one `#ASSERT` per scenario that the encoding has a function for (625 assertions), and ran it against the pass-2 encoding.
`ANSWERS.md` is not kept in this folder; the scenario numbers `S<n>` in `tests-independent.l4` refer to it, and each assertion carries its provision.
Its own narrative of what was repaired afterwards is in the sections "After the independent test pass (version 0.2.1)", "Findings" 21-24 and "The 76 scenarios the encoding had no function for"; this section says what the test file shows now.

| step | assertions | satisfied | failed | refused |
| --- | --- | --- | --- | --- |
| first run against the pass-2 encoding | 625 | 601 | 6 | 18 |
| after the repair (version 0.2.1) and the reconciliation below | 625 | 625 | 0 | 0 |

The 76 scenarios the encoding had no function for are not marked in the test file; they are the table in "The 76 scenarios the encoding had no function for", checked against the file by script.
53 of them are rules the text states, now answered by `usca-further-asks.l4` (181 assertions in `test-usca-further-asks.l4`); 23 are left as stated limits, each with its reason.

**What the 24 disagreements turned out to be** (6 failed and 18 refused in the first run).

- **Two led to a repair (S485, S486).**
  Gov. Code § 9605(b)(2) was never reached for two statutes enacted at the same time: the function refused on equal order of enactment before it looked at the chapter number.
  It now applies (b)(2) for equal order, and `test-usca-operation.l4` gained 11 assertions for it.
- **Thirteen were the test author's expectation, not the encoding (S6, S17, S52, S63, S205, S316, S532, S544, S560, S570, S594, S623, S662).**
  Each asked what follows outside a provision's stated condition, and the section does not say, so the encoding refuses.
  For S316 the 02:00 reading on the day the clocks change is ill-posed, which is the test author's own ambiguity Z17.
- **Four are rewritten to the encoding's value:** S3 and S522 (a provision substantially the same only as the common law gets `FALSE` under Gov. Code § 2 and Code Civ. Proc. § 5; Civ. Code § 5 gives `TRUE`, a difference recorded in NOTES), S660 (Code Civ. Proc. § 32.5 says "means ... limited ... or unlimited", an exhaustive definition) and S657 (the module returns `the Penal Code`, the author wrote `Penal Code`; no legal difference).
- **Three are genuine forks, kept as `REFUSED` and registered:** S47 (Gov. Code § 7.8 "irrespective of whether there shall be more than one such person"; F-7.8, the author's Z16), S483 (§ 9605(b)(1) "conclusively presumed" and (b)(2) "presumed" point at different statutes; the author's Z11) and S487 (F-9605b: when the higher-numbered statute disclaims, the presumption of (b)(2) does not run and the section says nothing further; the author expected the other statute).
- **Two are a silent limit, stated in NOTES (S375, S605).**
  With no § 135 day supplied, Code Civ. Proc. §§ 12a(a) and 10 answer `FALSE` for 25 December with no diagnostic; the author expected a refusal and recommends one.
  The convention is kept, a test asserts it, NOTES sorts it as silent, and loud variants that refuse were added beside the old functions.

Each of the 22 rewritten assertions has a `-- RECONCILED S<n>` comment above it that quotes the author's original and gives the reason; none is deleted.

The author's report also says a Python reference model it wrote matched the encoding on about 44,000 cases with no mismatch; that checks that two programs agree on one reading, not that the reading is right.

**Independence caveat.** At 09:31Z, after the test author's `ANSWERS.md` was last changed (09:20Z) and after it first wrote `tests-independent.l4` (09:03Z), the harness delivered into its session the contents of a backlog file and the paths of four other rows' triage files (AU, CA, SG, UK); this encoder's session received the same set.
A search of every tool call of both sessions finds no read of any of them.

**Check.** `check.sh` with `tests-independent.l4` in the folder, run with `L4_TARGET=unstable` (so not compared with a main build): 28 modules, 3080 satisfied, 8 failed (the expected eight in `tests-red.l4`), 0 refused, run on 2026-10-29.
The mutation check was not rerun on the repaired `usca-operation-of-statutes.l4`.
