# NOTES (coa10): the Companies Act 2006 (United Kingdom), Part 15 Chapters 10 to 12, sections 441 to 474

Status: written by part agent `coa10` (run `dst-coa10`) on 2026-11-13, for lines 5895-6542 of `ukpga-2006-46.txt`.
How each claim was checked: the counts, tables and quotations below were produced by scripts that read the files as they stand (`work/rows.py`, `work/sites.py`, `work/notes_build.py`) or copied from the `check.sh` and `srcrefs.py` runs at the end of the pass; prose that states a reading says so.
Nothing here is verified against the official text.
The source is a plain-text rendering of the Act made by a converter script from legislation.gov.uk (`inputs/SOURCES.md`); it is not the official text.
The brief governs where it and `inputs/PLAN.md` differ; I noticed no difference that changed a choice in this part.

## What this part is

Layer 1 is ten modules that follow the text's own order and carry `@ref` and `-- src:` quotations for every rule: `coa10-types`, `coa10-period` (ss 442, 443), `coa10-filing` (ss 441, 443A to 447), `coa10-exemptions` (ss 448 to 448C), `coa10-default` (ss 451 to 453), `coa10-revision` (ss 454 to 457), `coa10-disclosure` (ss 458 to 461), `coa10-medium` (ss 465 to 467), `coa10-meaning` (ss 464, 471, 472, 472A, 474) and `coa10-supplementary` (ss 463, 469, 470).
Each module has a test file `coa10-tests-<name>.l4` (the types module is declarations only).
Layer 2 is `coa10-seat.l4` (101 questions, each `@export` with `@desc`, grouped under `§` headings in the text's order, each named "Under section N, ...") and `coa10-cases-seat.l4`.
The seat is an individual who is, or is about to become, a director, a company secretary or a member of a company, or who deals with one (assumed, not ruled, in the brief).
Regulative rules (`DEONTIC`) appear three times in layer 1 (s 441(1) with s 451(1), s 448A(2)(e), s 456(7)); each duty is also a decision function, and the decision functions are what the tests assert (see "What the stable binary does not accept").

## The text in this file

The file prints two texts of s 444, of s 445(7) and of s 446(5), and runs two daily default fines together in s 451(4); `inputs/SOURCES.md` says the text is "revised text; may carry more than one extent version of a provision, and prospective provisions, which CLML marks but this text does not distinguish".
The choice between the two is an input of every rule that depends on it (fork F1).
The text shows a row of dots, or "...", where words were omitted or repealed: these are the rows `repealed or blank in this text` of the coverage table.

## Rulings applied (coa10)

The brief says each ruling is recorded again, word for word, in the `NOTES.md` of each row that carries that rule's `NOTHING-kind` tags.
The text below is copied by `work/notes_build.py` from lines 103 to 115 of `BRIEF.md`; it is not retyped.


These rulings set this corpus's drafting conventions, which each row follows and flags; L4 itself takes no position on them.
The rule of 2026-10-29 for what `JUST FALSE` and `NOTHING` mean is the convention the rows written since then follow (applied in legalese/commons#30 and #37); it was assumed, not ruled as a whole, and the rulings below settle parts of it.
In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").
Everywhere else it answers `NOTHING`: where the text lists without closing the list, says "includes", leaves a term undefined, is silent, points outside the sources, or limits a grant or prohibition in its own wording and the case falls outside the limit.
The wording is copied from section 2 of `docs/design-question-false-or-nothing.md`, which also states the two readings left open for a lawyer.
Each ruling is recorded again, word for word, in the `NOTES.md` of each row that carries that rule's `NOTHING-kind` tags: in its fork register where it has one, and in a section of its own where it has none.

- **E1** (bench `commons-negation-1030`; should a legal effect be one definition gathered from every section that gives it?): option B, as guidance for gathering a legal effect's routes by hand only, with no pilot run; option A (gathering by bare name) is withdrawn as a direction for the language, not deferred; option C (per-section answers) applies everywhere else; the Magna Carta pilot in the printed recommendation (chapters 2, 3, 4, 5, 37, 43, 46 and 53, with a blind second reader) is not to be run. The maintainer's lean, verbatim: "B but generally uncomfortable with this much magic because it takes the language from unopinionated to opinionated in ways that are hard to teach an l4 novice." the maintainer's note, verbatim: "Fundamentally I feel like we are trying to make the language do work that the human l4 drafter should do. Too much magic. Can’t we just decline to be this opinionated and say the programmer needs to do this thinking?" Marked 2026-11-03T23:19:02.812Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
- **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. The maintainer's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." the maintainer's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
- **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. The maintainer's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.
- **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. The maintainer approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.
- **Questions with no convention: decide case by case (the maintainer, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. The maintainer's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with the coordinator where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

Where each ruling bites in this part:
- E1 (no gathering of a legal effect from several sections): every section answers in its own function; the only gathering is `s 441(1) the filing section that applies to the company`, which counts which of ss 443A to 447 apply and answers NOTHING if not exactly one (fork F2).
- N2 (a flat negative is a no): `s 451(3)`, `s 453(4)`, `s 459(6)`, `s 459(7)`, `s 461(7)`, `s 463(4)` and `s 467(4)` answer JUST FALSE where the text says "not", "nothing ... compels" or "no person shall".
- Periods, "where" and scope limits: `where` sites answer JUST FALSE when the condition fails (11 branches tagged "a \"where\" not met", plus s 448C(1), "when"); a period the text fixes in its own words answers JUST FALSE outside it (s 441(1), s 448A(2)(e), s 452(1)(b) and s 455(4): 5 branches); a scope limit without "only" answers NOTHING (for example s 451(1) for a person who was not a director, fork F5).
- Delegated definitions, defences and "until" bars: s 451(2) answers JUST FALSE, worded "this section gives the person a defence on these facts", when the person does not prove reasonable steps.
- Case by case: 25 sites, listed one by one in the fork register below (S1 to S25).

## Coverage (coa10)

The table has one row for each section, subsection, paragraph, sub-paragraph, list item, table row, defined term and heading of lines 5895-6542, and each row has exactly one disposition.
It is generated by `work/rows.py` from the text (`work/units.py` splits the text into units) and the mapping in `rows.py`; the L4 name column lists the names that encode the unit, and the `tests` column counts the `#ASSERT` lines of the `coa10-tests-*` files that name them (a unit whose function is tested only through another function shows a smaller number).
The unit "section title line" and the lead-in lines ("In this section—", "(2) Exemption is conditional upon ...") carry no rule of their own; they sit in the row of their section or subsection.

### Counts and audit

- Units counted by `work/units.py` from the text: 607 (16 heading, 41 section, 206 subsection, 19 list item, 252 paragraph, 49 sub-paragraph, 18 defined term, 6 table row).
- Rows added by hand for units the parser cannot see (the defined expression "period for filing" at line 5910, the closing sentence of s 442(2) at 5914, the defined expression "relevant accounting reference period" at 6082, and the two "..." entries of s 474 at 6511 and 6516): 5.
- Rows in the table: before the 16 headings were given a disposition 596; after 612.
- Non-blank lines in the ranges: 648; lines that fall in no row: 0.
- Dispositions: encoded 338; fork 156; inert (reason 1, not operative) 17; inert (reason 2, machinery) 86; repealed or blank in this text 15; inert (reason 3) 0, the blank and repealed units having their own disposition.
- Rows whose listed names do not all quote every line of the unit through `@ref` src ranges: 37 (the audit in `rows.py` prints them): 32 are a section title line, 3 are a lead-in line (6078, 6378, 6506), and 2 are the "..." entries of s 474 at lines 6511 and 6516, which have their own blank rows.
- Every `encoded` and `fork` row names L4 definitions that exist; `rows.py` stops if one does not.
- Inert rows, reasons: reason 1 is the 16 headings and s 472A(2) (a statement of when the FCA rules were inserted); reason 2 is the regulation-making powers and their procedure (ss 454(3) to (5), 457 except (4), 462, 464(3), 468, 468A, 470(1) and (4), 473, 453(5)).

### The table

| provision | text lines | disposition | L4 name(s) | tests | note |
| --- | --- | --- | --- | --- | --- |
| heading at line 5895 Chapter 10 — Filing of accounts and reports | 5895 | inert (reason 1) | - | - | chapter heading |
| heading at line 5896 Duty to file accounts and reports | 5896-5935 | inert (reason 1) | - | - | cross-heading "Duty to file accounts and reports" |
| s 441 | 5897-5907 | encoded | `s 441(1) the filing section that applies to the company` | 11 | the section title; the operative text is in the rows below |
| s 441(1) | 5898-5904 | fork | `s 441(1) the filing section that applies to the company`; `s 441(1) what the filing section that applies requires of the directors for...`; `s 441(1) the directors' duty to deliver the accounts and reports`; `s 441(1) the requirements were complied with before the end of the period f...` | 24 | the duty is a regulative rule (WITHIN the days of s 442) and, beside it, a decision function; the section that applies is the dispatcher (fork F2) |
| s 441(1) item section 443A | 5899 | encoded | `s 441 filing section` | 1 | the constructor `s 441 section 443A` of that type, answered by `s 443A(1) section 443A applies to the company` |
| s 441(1) item section 444 | 5900 | encoded | `s 441 filing section` | 3 | the constructor `s 441 section 444` of that type, answered by `s 444(1) section 444 applies to the company` |
| s 441(1) item section 444A | 5901 | encoded | `s 441 filing section` | 1 | the constructor `s 441 section 444A` of that type, answered by `s 444A(1) section 444A applies to the company` |
| s 441(1) item section 445 | 5902 | encoded | `s 441 filing section` | 1 | the constructor `s 441 section 445` of that type, answered by `s 445(1) section 445 applies to the company` |
| s 441(1) item section 446 | 5903 | encoded | `s 441 filing section` | 2 | the constructor `s 441 section 446` of that type, answered by `s 446(1) section 446 applies to the company` |
| s 441(1) item section 447 | 5904 | encoded | `s 441 filing section` | 1 | the constructor `s 441 section 447` of that type, answered by `s 447(1) section 447 applies to the company` |
| s 441(2) | 5905-5907 | encoded | `s 441(2) the directors must deliver the accounts and reports for the financ...` | 6 | the exemptions of ss 448 and 448A are inputs |
| s 441(2) item section 448 | 5906 | encoded | `s 441(2) the directors must deliver the accounts and reports for the financ...` | 6 | the exemptions of ss 448 and 448A are inputs |
| s 441(2) item section 448A | 5907 | encoded | `s 441(2) the directors must deliver the accounts and reports for the financ...` | 6 | the exemptions of ss 448 and 448A are inputs |
| s 442 | 5908-5926 | encoded | `s 442(1) the period for filing ends on` | 7 | the section title; the operative text is in the rows below |
| s 442(1) | 5909-5910 | encoded | `s 442(1) the period for filing ends on`; `s 442(1) the number of days from the end of the accounting reference period...` | 9 | the composite over a record of the facts |
| s 442(1) term period for filing | 5910 | encoded | `s 442(1) the period for filing ends on` | 7 | the defined expression "period for filing" is the date this function returns |
| s 442(2) | 5911-5914 | encoded | `s 442(2) the period for filing ends on` | 6 | nine months (private) or six months (public) after the end of the accounting reference period, counted by s 443; the quoted lines include the closing sentence of (2) |
| s 442(2)(a) | 5912 | encoded | `s 442(2) the period for filing ends on` | 6 | nine months (private) or six months (public) after the end of the accounting reference period, counted by s 443; the quoted lines include the closing sentence of (2) |
| s 442(2)(b) | 5913-5914 | encoded | `s 442(2) the period for filing ends on` | 6 | nine months (private) or six months (public) after the end of the accounting reference period, counted by s 443; the quoted lines include the closing sentence of (2) |
| s 442(2) tail "This is subject to the following provisions of this section" | 5914 | encoded | `s 442(2) the period for filing ends on`; `s 442(3) the period for filing ends on for a first accounting reference per...`; `s 442(4) the period for filing ends on where the accounting reference perio...` | 12 | the sentence "This is subject to the following provisions of this section": subsections (3) to (5A) are encoded as exceptions to (2) |
| s 442(3) | 5915-5918 | fork | `s 442(3) the relevant accounting reference period is a period of more than ...`; `s 442(3) the period for filing ends on for a first accounting reference per...` | 8 | fork F3 (how "more than twelve months" and "the first anniversary" are counted) |
| s 442(3)(a) | 5916 | fork | `s 442(3) the relevant accounting reference period is a period of more than ...`; `s 442(3) the period for filing ends on for a first accounting reference per...` | 8 | fork F3 (how "more than twelve months" and "the first anniversary" are counted) |
| s 442(3)(b) | 5917-5918 | fork | `s 442(3) the relevant accounting reference period is a period of more than ...`; `s 442(3) the period for filing ends on for a first accounting reference per...` | 8 | fork F3 (how "more than twelve months" and "the first anniversary" are counted) |
| s 442(4) | 5919-5922 | encoded | `s 442(4) the period for filing ends on where the accounting reference perio...` | 3 | later of the (2)/(3) period and three months from the notice |
| s 442(4)(a) | 5920 | encoded | `s 442(4) the period for filing ends on where the accounting reference perio...` | 3 | later of the (2)/(3) period and three months from the notice |
| s 442(4)(b) | 5921-5922 | encoded | `s 442(4) the period for filing ends on where the accounting reference perio...` | 3 | later of the (2)/(3) period and three months from the notice |
| s 442(5) | 5923 | fork | `s 442(5) the Secretary of State may extend the period for filing`; `s 442(5A) the period for filing ends on after any extension` | 6 | forks F4 ("before the expiry" read as on or before the last day) and F18 (a grant named "may": no special reason is NOTHING, not JUST FALSE) |
| s 442(5A) | 5924 | fork | `s 442(5A) the extension complies with the limit of twelve months after the ...` | 2 | fork F4; an extension past the limit is NOTHING (silent) |
| s 442(6) | 5925 | encoded | `s 442(6) the period for a public company applies` | 2 | status immediately before the end of the accounting reference period |
| s 442(7) | 5926 | encoded | `s 442(7) the accounting reference period is the relevant accounting referen...` | 2 | a definition by "means" |
| s 443 | 5927-5935 | encoded | `s 443(2) the period ends with` | 17 | the section title; the operative text is in the rows below |
| s 443(1) | 5928 | encoded | `s 443(1) section 443 applies to the period for filing` | 2 | scope: NOTHING outside it |
| s 443(2) | 5929 | encoded | `s 443(2) the period ends with` | 17 | the corresponding date; with (3) and (4) in one function |
| s 443(3) | 5930 | encoded | `s 443(3) the specified date is the last day of a month`; `s 443(2) the period ends with` | 24 | differs from the library `add months` (it clamps): tests 30 Apr 2025 + 9 |
| s 443(4) | 5931-5934 | encoded | `s 443(4) the specified date is the 29th or 30th but not the last day of a m...`; `s 443(2) the period ends with` | 23 |  |
| s 443(4)(a) | 5932 | encoded | `s 443(4) the specified date is the 29th or 30th but not the last day of a m...`; `s 443(2) the period ends with` | 23 |  |
| s 443(4)(b) | 5933-5934 | encoded | `s 443(4) the specified date is the 29th or 30th but not the last day of a m...`; `s 443(2) the period ends with` | 23 |  |
| s 443(5) | 5935 | encoded | `s 443(5) the appropriate month`; `s 443(5) the year of the appropriate month` | 9 |  |
| heading at line 5936 Filing obligations of different descriptions of company | 5936-6117 | inert (reason 1) | - | - | cross-heading |
| s 443A | 5937-5947 | encoded | `s 443A(1) section 443A applies to the company` | 4 | the section title; the operative text is in the rows below |
| s 443A(1) | 5938-5940 | encoded | `s 443A(1) the company is described by section 443A`; `s 443A(1) section 443A applies to the company`; `s 443A(1) what section 443A requires of the directors for the document` | 10 | a table from document to must / may / not required |
| s 443A(1)(a) | 5939 | encoded | `s 443A(1) the company is described by section 443A`; `s 443A(1) section 443A applies to the company`; `s 443A(1) what section 443A requires of the directors for the document` | 10 | a table from document to must / may / not required |
| s 443A(1)(b) | 5940 | encoded | `s 443A(1) the company is described by section 443A`; `s 443A(1) section 443A applies to the company`; `s 443A(1) what section 443A requires of the directors for the document` | 10 | a table from document to must / may / not required |
| s 443A(2) | 5941-5942 | encoded | `s 443A(1) what section 443A requires of the directors for the document` | 6 | the auditor's report, and the exemption sentence ("This does not apply if ...") |
| s 443A(3) | 5943 | fork | `s 443A(3) the copy meets the requirement to state who signed it`; `s 443A(3) the copy of a document the section names meets the requirement to...` | 5 | the one function the later sections call; case-by-case site S9 (fork register) |
| s 443A(4) | 5944-5946 | fork | `s 443A(4) the copy of the auditor's report states what the section requires` | 10 | the s 506 answer (coa12) is an input; case-by-case site S10 (fork register) |
| s 443A(4)(a) | 5945 | encoded | `s 443A(4) the copy of the auditor's report states what the section requires` | 10 | the s 506 answer (coa12) is an input |
| s 443A(4)(b) | 5946 | encoded | `s 443A(4) the copy of the auditor's report states what the section requires` | 10 | the s 506 answer (coa12) is an input |
| s 443A(5) | 5947 | encoded | `s 443A(5) the reference to the name of the auditor is a reference to the na...` | 2 |  |
| s 444 | 5948-5993 | fork | `s 444(1) what section 444 requires of the directors for the document` | 3 | fork F1: two texts of s 444 in the file; the caller states which |
| s 444(1) | 5949-5953 | fork | `s 444(1) what the first text of section 444 requires of the directors for t...`; `s 444(1) section 444 applies to the company` | 17 | fork F1 (first text) |
| s 444(1)(a) | 5950 | fork | `s 444(1) what the first text of section 444 requires of the directors for t...`; `s 444(1) section 444 applies to the company` | 17 | fork F1 (first text) |
| s 444(1)(b) | 5951-5953 | fork | `s 444(1) what the first text of section 444 requires of the directors for t...`; `s 444(1) section 444 applies to the company` | 17 | fork F1 (first text) |
| s 444(1)(b)(i) | 5952 | fork | `s 444(1) what the first text of section 444 requires of the directors for t...`; `s 444(1) section 444 applies to the company` | 17 | fork F1 (first text) |
| s 444(1)(b)(ii) | 5953 | fork | `s 444(1) what the first text of section 444 requires of the directors for t...`; `s 444(1) section 444 applies to the company` | 17 | fork F1 (first text) |
| s 444(2) | 5954-5955 | fork | `s 444(1) what the first text of section 444 requires of the directors for t...` | 10 | fork F1: the auditor's report only where the profit and loss account is delivered |
| s 444(2A) | 5956 | fork | `s 444(1) what the first text of section 444 requires of the directors for t...` | 10 | fork F1: the consent statement where the accounts are abridged |
| s 444(3) | 5957 | fork | `s 444(3) the copies delivered are copies of the company's annual accounts a...` | 2 | fork F1 (first text); also case-by-case site S11 |
| s 444(3A) | 5958 | repealed or blank in this text | - | - | the text shows only a row of dots |
| s 444(3B) | 5959 | repealed or blank in this text | - | - | the text shows only a row of dots |
| s 444(4) | 5960 | repealed or blank in this text | - | - | the text shows only a row of dots |
| s 444(5) | 5961-5964 | fork | `s 444(5) the section requires the copy of the balance sheet to contain the ...`; `s 444(5) the copy of the balance sheet contains the statement the section r...` | 7 | fork F1 (first text) |
| s 444(5)(a) | 5962 | fork | `s 444(5) the section requires the copy of the balance sheet to contain the ...`; `s 444(5) the copy of the balance sheet contains the statement the section r...` | 7 | fork F1 (first text) |
| s 444(5)(b) | 5963-5964 | fork | `s 444(5) the section requires the copy of the balance sheet to contain the ...`; `s 444(5) the copy of the balance sheet contains the statement the section r...` | 7 | fork F1 (first text); also case-by-case site S12 |
| s 444(5A) | 5965-5967 | fork | `s 444(5C) subsection (5A) applies to the company`; `s 444(5A)(a) the section requires the copy of the balance sheet to disclose...`; `s 444(5A)(b) the section requires the notes to the balance sheet to satisfy...` | 11 | fork F1 (first text) |
| s 444(5A)(a) | 5966 | fork | `s 444(5C) subsection (5A) applies to the company`; `s 444(5A)(a) the section requires the copy of the balance sheet to disclose...`; `s 444(5A)(b) the section requires the notes to the balance sheet to satisfy...` | 11 | fork F1 (first text) |
| s 444(5A)(b) | 5967 | fork | `s 444(5C) subsection (5A) applies to the company`; `s 444(5A)(a) the section requires the copy of the balance sheet to disclose...`; `s 444(5A)(b) the section requires the notes to the balance sheet to satisfy...` | 11 | fork F1 (first text); also case-by-case site S13 |
| s 444(5B) | 5968-5974 | fork | `s 444(5B) the notes to the balance sheet satisfy the requirements` | 7 | fork F1 (first text); also case-by-case site S14 |
| s 444(5B)(a) | 5969 | fork | `s 444(5B) the notes to the balance sheet satisfy the requirements` | 7 | fork F1 (first text) |
| s 444(5B)(b) | 5970 | fork | `s 444(5B) the notes to the balance sheet satisfy the requirements` | 7 | fork F1 (first text) |
| s 444(5B)(c) | 5971 | fork | `s 444(5B) the notes to the balance sheet satisfy the requirements` | 7 | fork F1 (first text) |
| s 444(5B)(d) | 5972-5974 | fork | `s 444(5B) the notes to the balance sheet satisfy the requirements` | 7 | fork F1 (first text) |
| s 444(5B)(d)(i) | 5973 | fork | `s 444(5B) the notes to the balance sheet satisfy the requirements` | 7 | fork F1 (first text) |
| s 444(5B)(d)(ii) | 5974 | fork | `s 444(5B) the notes to the balance sheet satisfy the requirements` | 7 | fork F1 (first text) |
| s 444(5C) | 5975-5977 | fork | `s 444(5C) subsection (5A) applies to the company` | 5 | fork F1 (first text) |
| s 444(5C)(a) | 5976 | fork | `s 444(5C) subsection (5A) applies to the company` | 5 | fork F1 (first text) |
| s 444(5C)(b) | 5977 | fork | `s 444(5C) subsection (5A) applies to the company` | 5 | fork F1 (first text) |
| s 444(6) | 5978 | fork | `s 444(6) the copy meets the requirement to state who signed it` | 3 | fork F1 (first text) |
| s 444(7) | 5979-5981 | fork | `s 444(7) the copy of the auditor's report states what the section requires` | 2 | fork F1 (first text) |
| s 444(7)(a) | 5980 | fork | `s 444(7) the copy of the auditor's report states what the section requires` | 2 | fork F1 (first text) |
| s 444(7)(b) | 5981 | fork | `s 444(7) the copy of the auditor's report states what the section requires` | 2 | fork F1 (first text) |
| s 444(8) | 5982 | fork | `s 444(8) the references to the name of the auditor are references to the na...` | 2 | fork F1 (first text) |
| s 444(1)[text 2] | 5983-5985 | fork | `s 444(1) what the second text of section 444 requires of the directors for ...`; `s 444(1) the company is described by section 444` | 6 | fork F1 (second text) |
| s 444(1)[text 2](a) | 5984 | fork | `s 444(1) what the second text of section 444 requires of the directors for ...`; `s 444(1) the company is described by section 444` | 6 | fork F1 (second text) |
| s 444(1)[text 2](b) | 5985 | fork | `s 444(1) what the second text of section 444 requires of the directors for ...`; `s 444(1) the company is described by section 444` | 6 | fork F1 (second text) |
| s 444(2)[text 2] | 5986-5987 | fork | `s 444(1) what the second text of section 444 requires of the directors for ...` | 6 | fork F1 (second text) |
| s 444(3)[text 2] | 5988 | fork | `s 444(3) the copy meets the requirement to state who signed it in the secon...` | 2 | fork F1 (second text) |
| s 444(4)[text 2] | 5989-5991 | fork | `s 444(4) the copy of the auditor's report states what the section requires ...` | 2 | fork F1 (second text); (4) and (5) together |
| s 444(4)[text 2](a) | 5990 | fork | `s 444(4) the copy of the auditor's report states what the section requires ...` | 2 | fork F1 (second text); (4) and (5) together |
| s 444(4)[text 2](b) | 5991 | fork | `s 444(4) the copy of the auditor's report states what the section requires ...` | 2 | fork F1 (second text); (4) and (5) together |
| s 444(5)[text 2] | 5992 | fork | `s 444(4) the copy of the auditor's report states what the section requires ...` | 2 | fork F1 (second text) |
| s 444(6)[text 2] | 5993 | fork | `s 444(6) the company is within a section that excludes it from section 444`; `s 444(1) section 444 applies to the company` | 7 | fork F1 (second text): this section does not apply to companies within section 443A |
| s 444A | 5994-6004 | encoded | `s 444A(1) section 444A applies to the company` | 5 | the section title; the operative text is in the rows below |
| s 444A(1) | 5995-5997 | encoded | `s 444A(1) the company is described by section 444A`; `s 444A(1) what section 444A requires of the directors for the document` | 5 |  |
| s 444A(1)(a) | 5996 | encoded | `s 444A(1) the company is described by section 444A`; `s 444A(1) what section 444A requires of the directors for the document` | 5 |  |
| s 444A(1)(b) | 5997 | encoded | `s 444A(1) the company is described by section 444A`; `s 444A(1) what section 444A requires of the directors for the document` | 5 |  |
| s 444A(2) | 5998 | encoded | `s 444A(1) what section 444A requires of the directors for the document` | 5 | the auditor's report, and the exemption sentence ("This does not apply if the company is exempt from audit ...") |
| s 444A(3) | 5999 | encoded | `s 444A(3) the copy meets the requirement to state who signed it` | 3 |  |
| s 444A(4) | 6000-6002 | encoded | `s 444A(4) the copy of the auditor's report states what the section requires` | 2 |  |
| s 444A(4)(a) | 6001 | encoded | `s 444A(4) the copy of the auditor's report states what the section requires` | 2 |  |
| s 444A(4)(b) | 6002 | encoded | `s 444A(4) the copy of the auditor's report states what the section requires` | 2 |  |
| s 444A(4A) | 6003 | encoded | `s 444A(4A) the reference to the name of the auditor is a reference to the n...` | 2 |  |
| s 444A(5) | 6004 | encoded | `s 444A(5) the company is within a section that excludes it from section 444A`; `s 444A(1) section 444A applies to the company` | 5 | a flat negative: JUST FALSE for a company within section 444 |
| s 445 | 6005-6024 | encoded | `s 445(1) section 445 applies to the company` | 5 | the section title; the operative text is in the rows below |
| s 445(1) | 6006-6009 | encoded | `s 445(1) the company is described by section 445`; `s 445(1) what section 445 requires of the directors for the document` | 6 | medium-sized: the answer of ss 465 to 467 is an input |
| s 445(1)(a) | 6007 | encoded | `s 445(1) the company is described by section 445`; `s 445(1) what section 445 requires of the directors for the document` | 6 | medium-sized: the answer of ss 465 to 467 is an input |
| s 445(1)(aa) | 6008 | encoded | `s 445(1) the company is described by section 445`; `s 445(1) what section 445 requires of the directors for the document` | 6 | medium-sized: the answer of ss 465 to 467 is an input |
| s 445(1)(b) | 6009 | encoded | `s 445(1) the company is described by section 445`; `s 445(1) what section 445 requires of the directors for the document` | 6 | medium-sized: the answer of ss 465 to 467 is an input |
| s 445(2) | 6010-6011 | encoded | `s 445(1) what section 445 requires of the directors for the document` | 6 |  |
| s 445(3) | 6012 | repealed or blank in this text | - | - | the text shows only a row of dots |
| s 445(4) | 6013 | repealed or blank in this text | - | - | the text shows only a row of dots |
| s 445(5) | 6014 | encoded | `s 445(5) the copy meets the requirement to state who signed it` | 4 |  |
| s 445(6) | 6015-6017 | encoded | `s 445(6) the copy of the auditor's report states what the section requires` | 2 |  |
| s 445(6)(a) | 6016 | encoded | `s 445(6) the copy of the auditor's report states what the section requires` | 2 |  |
| s 445(6)(b) | 6017 | encoded | `s 445(6) the copy of the auditor's report states what the section requires` | 2 |  |
| s 445(6A) | 6018 | encoded | `s 445(6A) the reference to the name of the auditor is a reference to the na...` | 2 |  |
| s 445(7) | 6019-6021 | fork | `s 445(7) the company is within a section that excludes it from section 445`; `s 445(1) section 445 applies to the company` | 5 | fork F1: the first text excludes companies within 444 and 444A |
| s 445(7)(a) | 6020 | fork | `s 445(7) the company is within a section that excludes it from section 445`; `s 445(1) section 445 applies to the company` | 5 | fork F1: the first text excludes companies within 444 and 444A |
| s 445(7)(b) | 6021 | fork | `s 445(7) the company is within a section that excludes it from section 445`; `s 445(1) section 445 applies to the company` | 5 | fork F1: the first text excludes companies within 444 and 444A |
| s 445(7)[text 2] | 6022-6024 | fork | `s 445(7) the company is within a section that excludes it from section 445`; `s 445(1) section 445 applies to the company` | 5 | fork F1: the second text excludes companies within 443A and 444 |
| s 445(7)[text 2](a) | 6023 | fork | `s 445(7) the company is within a section that excludes it from section 445`; `s 445(1) section 445 applies to the company` | 5 | fork F1: the second text excludes companies within 443A and 444 |
| s 445(7)[text 2](b) | 6024 | fork | `s 445(7) the company is within a section that excludes it from section 445`; `s 445(1) section 445 applies to the company` | 5 | fork F1: the second text excludes companies within 443A and 444 |
| s 446 | 6025-6046 | encoded | `s 446(1) section 446 applies to the company` | 8 | the section title; the operative text is in the rows below |
| s 446(1) | 6026-6031 | encoded | `s 446(1) the company is described by section 446`; `s 446(1) what section 446 requires of the directors for the document` | 8 | "any separate corporate governance statement": NOTHING where there is none |
| s 446(1)(a) | 6027 | encoded | `s 446(1) the company is described by section 446`; `s 446(1) what section 446 requires of the directors for the document` | 8 | "any separate corporate governance statement": NOTHING where there is none |
| s 446(1)(aa) | 6028 | encoded | `s 446(1) the company is described by section 446`; `s 446(1) what section 446 requires of the directors for the document` | 8 | "any separate corporate governance statement": NOTHING where there is none |
| s 446(1)(b) | 6029 | encoded | `s 446(1) the company is described by section 446`; `s 446(1) what section 446 requires of the directors for the document` | 8 | "any separate corporate governance statement": NOTHING where there is none |
| s 446(1)(ba) | 6030 | repealed or blank in this text | - | - | the text shows only a row of dots |
| s 446(1)(c) | 6031 | encoded | `s 446(1) the company is described by section 446`; `s 446(1) what section 446 requires of the directors for the document` | 8 | "any separate corporate governance statement": NOTHING where there is none |
| s 446(2) | 6032-6033 | encoded | `s 446(1) what section 446 requires of the directors for the document` | 8 |  |
| s 446(3) | 6034 | encoded | `s 446(3) the copy meets the requirement to state who signed it` | 3 |  |
| s 446(4) | 6035-6037 | encoded | `s 446(4) the copy of the auditor's report states what the section requires` | 2 |  |
| s 446(4)(a) | 6036 | encoded | `s 446(4) the copy of the auditor's report states what the section requires` | 2 |  |
| s 446(4)(b) | 6037 | encoded | `s 446(4) the copy of the auditor's report states what the section requires` | 2 |  |
| s 446(4A) | 6038 | encoded | `s 446(4A) the reference to the name of the auditor is a reference to the na...` | 2 |  |
| s 446(5) | 6039-6042 | fork | `s 446(5) the company is within a section that excludes it from section 446`; `s 446(1) section 446 applies to the company` | 8 | fork F1: the first text excludes companies within 444, 444A and 445 |
| s 446(5)(a) | 6040 | fork | `s 446(5) the company is within a section that excludes it from section 446`; `s 446(1) section 446 applies to the company` | 8 | fork F1: the first text excludes companies within 444, 444A and 445 |
| s 446(5)(aa) | 6041 | fork | `s 446(5) the company is within a section that excludes it from section 446`; `s 446(1) section 446 applies to the company` | 8 | fork F1: the first text excludes companies within 444, 444A and 445 |
| s 446(5)(b) | 6042 | fork | `s 446(5) the company is within a section that excludes it from section 446`; `s 446(1) section 446 applies to the company` | 8 | fork F1: the first text excludes companies within 444, 444A and 445 |
| s 446(5)[text 2] | 6043-6046 | fork | `s 446(5) the company is within a section that excludes it from section 446`; `s 446(1) section 446 applies to the company` | 8 | fork F1: the second text excludes companies within 443A, 444 and 445 |
| s 446(5)[text 2](a) | 6044 | fork | `s 446(5) the company is within a section that excludes it from section 446`; `s 446(1) section 446 applies to the company` | 8 | fork F1: the second text excludes companies within 443A, 444 and 445 |
| s 446(5)[text 2](b) | 6045 | fork | `s 446(5) the company is within a section that excludes it from section 446`; `s 446(1) section 446 applies to the company` | 8 | fork F1: the second text excludes companies within 443A, 444 and 445 |
| s 446(5)[text 2](c) | 6046 | fork | `s 446(5) the company is within a section that excludes it from section 446`; `s 446(1) section 446 applies to the company` | 8 | fork F1: the second text excludes companies within 443A, 444 and 445 |
| s 447 | 6047-6059 | encoded | `s 447(1) section 447 applies to the company` | 3 | the section title; the operative text is in the rows below |
| s 447(1) | 6048-6053 | encoded | `s 447(1) the company is described by section 447`; `s 447(1) what section 447 requires of the directors for the document` | 9 |  |
| s 447(1)(a) | 6049 | encoded | `s 447(1) the company is described by section 447`; `s 447(1) what section 447 requires of the directors for the document` | 9 |  |
| s 447(1)(b) | 6050 | encoded | `s 447(1) the company is described by section 447`; `s 447(1) what section 447 requires of the directors for the document` | 9 |  |
| s 447(1)(ba) | 6051 | encoded | `s 447(1) the company is described by section 447`; `s 447(1) what section 447 requires of the directors for the document` | 9 |  |
| s 447(1)(c) | 6052 | encoded | `s 447(1) the company is described by section 447`; `s 447(1) what section 447 requires of the directors for the document` | 9 |  |
| s 447(1)(d) | 6053 | encoded | `s 447(1) the company is described by section 447`; `s 447(1) what section 447 requires of the directors for the document` | 9 |  |
| s 447(2) | 6054 | encoded | `s 447(1) what section 447 requires of the directors for the document` | 9 | no exemption sentence for the auditor's report |
| s 447(3) | 6055 | encoded | `s 447(3) the copy meets the requirement to state who signed it` | 4 |  |
| s 447(4) | 6056-6058 | encoded | `s 447(4) the copy of the auditor's report states what the section requires` | 2 |  |
| s 447(4)(a) | 6057 | encoded | `s 447(4) the copy of the auditor's report states what the section requires` | 2 |  |
| s 447(4)(b) | 6058 | encoded | `s 447(4) the copy of the auditor's report states what the section requires` | 2 |  |
| s 447(5) | 6059 | encoded | `s 447(5) the reference to the name of the auditor is a reference to the nam...` | 2 |  |
| s 448 | 6060-6082 | encoded | `s 448(1) the directors of the unlimited company are not required to deliver...` | 8 | the section title; the operative text is in the rows below |
| s 448(1) | 6061 | encoded | `s 448(1) the directors of the unlimited company are not required to deliver...` | 8 |  |
| s 448(2) | 6062-6066 | encoded | `s 448(2) the conditions are met`; `s 448(2)(a) the condition is met`; `s 448(2)(b) the condition is met`; `s 448(2)(c) the condition is met`; `s 448(2) the undertaking was limited at that time` | 14 | the closing sentence defines "limited" at a time |
| s 448(2)(a) | 6063 | encoded | `s 448(2) the conditions are met`; `s 448(2)(a) the condition is met`; `s 448(2)(b) the condition is met`; `s 448(2)(c) the condition is met`; `s 448(2) the undertaking was limited at that time` | 14 | the closing sentence defines "limited" at a time |
| s 448(2)(b) | 6064 | encoded | `s 448(2) the conditions are met`; `s 448(2)(a) the condition is met`; `s 448(2)(b) the condition is met`; `s 448(2)(c) the condition is met`; `s 448(2) the undertaking was limited at that time` | 14 | the closing sentence defines "limited" at a time |
| s 448(2)(c) | 6065-6066 | encoded | `s 448(2) the conditions are met`; `s 448(2)(a) the condition is met`; `s 448(2)(b) the condition is met`; `s 448(2)(c) the condition is met`; `s 448(2) the undertaking was limited at that time` | 14 | the closing sentence defines "limited" at a time |
| s 448(3) | 6067-6074 | encoded | `s 448(3) the section bars the exemption`; `s 448(3)(a) the company is a banking or insurance company or the parent com...`; `s 448(3)(b) each of the members of the company is of a kind that paragraph ...`; `s 448(3) the undertaking counts as a member of a kind that paragraph (b) names` | 19 | the last sentence (comparable undertakings outside the United Kingdom) is the third function |
| s 448(3)(a) | 6068 | encoded | `s 448(3) the section bars the exemption`; `s 448(3)(a) the company is a banking or insurance company or the parent com...`; `s 448(3)(b) each of the members of the company is of a kind that paragraph ...`; `s 448(3) the undertaking counts as a member of a kind that paragraph (b) names` | 19 | the last sentence (comparable undertakings outside the United Kingdom) is the third function |
| s 448(3)(b) | 6069-6074 | encoded | `s 448(3) the section bars the exemption`; `s 448(3)(a) the company is a banking or insurance company or the parent com...`; `s 448(3)(b) each of the members of the company is of a kind that paragraph ...`; `s 448(3) the undertaking counts as a member of a kind that paragraph (b) names` | 19 | the last sentence (comparable undertakings outside the United Kingdom) is the third function |
| s 448(3)(b)(i) | 6070 | encoded | `s 448 a limited company`; `s 448(3)(b) each of the members of the company is of a kind that paragraph ...`; `s 448(3) the undertaking counts as a member of a kind that paragraph (b) names` | 13 | a constructor of `s 448 kind of member`; the unit that closes with (iv) also holds the sentence about comparable undertakings outside the United Kingdom |
| s 448(3)(b)(ii) | 6071 | encoded | `s 448 a limited company`; `s 448(3)(b) each of the members of the company is of a kind that paragraph ...`; `s 448(3) the undertaking counts as a member of a kind that paragraph (b) names` | 13 | a constructor of `s 448 kind of member`; the unit that closes with (iv) also holds the sentence about comparable undertakings outside the United Kingdom |
| s 448(3)(b)(iii) | 6072 | encoded | `s 448 a limited company`; `s 448(3)(b) each of the members of the company is of a kind that paragraph ...`; `s 448(3) the undertaking counts as a member of a kind that paragraph (b) names` | 13 | a constructor of `s 448 kind of member`; the unit that closes with (iv) also holds the sentence about comparable undertakings outside the United Kingdom |
| s 448(3)(b)(iv) | 6073-6074 | encoded | `s 448 a limited company`; `s 448(3)(b) each of the members of the company is of a kind that paragraph ...`; `s 448(3) the undertaking counts as a member of a kind that paragraph (b) names` | 13 | a constructor of `s 448 kind of member`; the unit that closes with (iv) also holds the sentence about comparable undertakings outside the United Kingdom |
| s 448(4) | 6075-6077 | encoded | `s 448(4)(a) the words substituted in section 434(3)`; `s 448(4)(b) the words substituted in section 435(1)(b)` | 6 | the words of the substitution are strings |
| s 448(4)(a) | 6076 | encoded | `s 448(4)(a) the words substituted in section 434(3)`; `s 448(4)(b) the words substituted in section 435(1)(b)` | 6 | the words of the substitution are strings |
| s 448(4)(b) | 6077 | encoded | `s 448(4)(a) the words substituted in section 434(3)`; `s 448(4)(b) the words substituted in section 435(1)(b)` | 6 | the words of the substitution are strings |
| s 448(5) | 6078-6082 | encoded | `s 448(5) the person is a general partner`; `s 448(5) the partnership is a limited partnership`; `s 448(5) the accounting reference period is the relevant accounting referen...` | 7 |  |
| s 448 term general partner | 6079 | encoded | `s 448(5) the person is a general partner`; `s 448(5) the partnership is a limited partnership`; `s 448(5) the accounting reference period is the relevant accounting referen...` | 7 | a defined term of s 448(5) |
| s 448 term general partner(a) | 6080 | encoded | `s 448(5) the person is a general partner`; `s 448(5) the partnership is a limited partnership`; `s 448(5) the accounting reference period is the relevant accounting referen...` | 7 | a defined term of s 448(5) |
| s 448 term general partner(b) | 6081 | encoded | `s 448(5) the person is a general partner`; `s 448(5) the partnership is a limited partnership`; `s 448(5) the accounting reference period is the relevant accounting referen...` | 7 | a defined term of s 448(5) |
| s 448 term limited partnership | 6082 | encoded | `s 448(5) the person is a general partner`; `s 448(5) the partnership is a limited partnership`; `s 448(5) the accounting reference period is the relevant accounting referen...` | 7 | a defined term of s 448(5) |
| s 448 term relevant accounting reference period | 6082 | encoded | `s 448(5) the person is a general partner`; `s 448(5) the partnership is a limited partnership`; `s 448(5) the accounting reference period is the relevant accounting referen...` | 7 | a defined term of s 448(5) |
| s 448A | 6083-6100 | encoded | `s 448A(1) the directors of the dormant subsidiary are not required to deliv...` | 10 | the section title; the operative text is in the rows below |
| s 448A(1) | 6084-6087 | encoded | `s 448A(1) the directors of the dormant subsidiary are not required to deliv...` | 10 | the dormant answer is the keel's s 1169(1) (a BOOLEAN input) |
| s 448A(1)(a) | 6085 | encoded | `s 448A(1) the directors of the dormant subsidiary are not required to deliv...` | 10 | the dormant answer is the keel's s 1169(1) (a BOOLEAN input) |
| s 448A(1)(b) | 6086 | encoded | `s 448A(1) the directors of the dormant subsidiary are not required to deliv...` | 10 | the dormant answer is the keel's s 1169(1) (a BOOLEAN input) |
| s 448A(1)(c) | 6087 | encoded | `s 448A(1) the directors of the dormant subsidiary are not required to deliv...` | 10 | the dormant answer is the keel's s 1169(1) (a BOOLEAN input) |
| s 448A(2) | 6088-6100 | encoded | `s 448A(2) the conditions for the exemption are complied with`; `s 448A(2)(c) the company is included in consolidated accounts drawn up as t...`; `s 448A(2)(e) the directors have delivered the documents within the period f...`; `s 448A(2)(e) the directors' duty to deliver the documents` | 19 | paragraphs (a) and (d) are inputs of the (2) function; (e) is also a regulative rule |
| s 448A(2)(a) | 6089 | encoded | `s 448A(2) the conditions for the exemption are complied with`; `s 448A(2)(c) the company is included in consolidated accounts drawn up as t...`; `s 448A(2)(e) the directors have delivered the documents within the period f...`; `s 448A(2)(e) the directors' duty to deliver the documents` | 19 | paragraphs (a) and (d) are inputs of the (2) function; (e) is also a regulative rule |
| s 448A(2)(b) | 6090 | encoded | `s 448A(2) the conditions for the exemption are complied with`; `s 448A(2)(c) the company is included in consolidated accounts drawn up as t...`; `s 448A(2)(e) the directors have delivered the documents within the period f...`; `s 448A(2)(e) the directors' duty to deliver the documents` | 19 | paragraphs (a) and (d) are inputs of the (2) function; (e) is also a regulative rule |
| s 448A(2)(c) | 6091-6093 | fork | `s 448A(2) the conditions for the exemption are complied with`; `s 448A(2)(c) the company is included in consolidated accounts drawn up as t...`; `s 448A(2)(e) the directors have delivered the documents within the period f...`; `s 448A(2)(e) the directors' duty to deliver the documents` | 19 | paragraphs (a) and (d) are inputs of the (2) function; (e) is also a regulative rule; case-by-case site S7 (fork register) |
| s 448A(2)(c)(i) | 6092 | encoded | `s 448A(2) the conditions for the exemption are complied with`; `s 448A(2)(c) the company is included in consolidated accounts drawn up as t...`; `s 448A(2)(e) the directors have delivered the documents within the period f...`; `s 448A(2)(e) the directors' duty to deliver the documents` | 19 | paragraphs (a) and (d) are inputs of the (2) function; (e) is also a regulative rule |
| s 448A(2)(c)(ii) | 6093 | encoded | `s 448A(2) the conditions for the exemption are complied with`; `s 448A(2)(c) the company is included in consolidated accounts drawn up as t...`; `s 448A(2)(e) the directors have delivered the documents within the period f...`; `s 448A(2)(e) the directors' duty to deliver the documents` | 19 | paragraphs (a) and (d) are inputs of the (2) function; (e) is also a regulative rule |
| s 448A(2)(d) | 6094 | encoded | `s 448A(2) the conditions for the exemption are complied with`; `s 448A(2)(c) the company is included in consolidated accounts drawn up as t...`; `s 448A(2)(e) the directors have delivered the documents within the period f...`; `s 448A(2)(e) the directors' duty to deliver the documents` | 19 | paragraphs (a) and (d) are inputs of the (2) function; (e) is also a regulative rule |
| s 448A(2)(e) | 6095-6100 | fork | `s 448A(2) the conditions for the exemption are complied with`; `s 448A(2)(c) the company is included in consolidated accounts drawn up as t...`; `s 448A(2)(e) the directors have delivered the documents within the period f...`; `s 448A(2)(e) the directors' duty to deliver the documents` | 19 | paragraphs (a) and (d) are inputs of the (2) function; (e) is also a regulative rule; case-by-case site S8 (fork register) |
| s 448A(2)(e)(i) | 6096 | encoded | `s 448A(2) the conditions for the exemption are complied with`; `s 448A(2)(c) the company is included in consolidated accounts drawn up as t...`; `s 448A(2)(e) the directors have delivered the documents within the period f...`; `s 448A(2)(e) the directors' duty to deliver the documents` | 19 | paragraphs (a) and (d) are inputs of the (2) function; (e) is also a regulative rule |
| s 448A(2)(e)(ii) | 6097 | encoded | `s 448A(2) the conditions for the exemption are complied with`; `s 448A(2)(c) the company is included in consolidated accounts drawn up as t...`; `s 448A(2)(e) the directors have delivered the documents within the period f...`; `s 448A(2)(e) the directors' duty to deliver the documents` | 19 | paragraphs (a) and (d) are inputs of the (2) function; (e) is also a regulative rule |
| s 448A(2)(e)(iii) | 6098 | encoded | `s 448A(2) the conditions for the exemption are complied with`; `s 448A(2)(c) the company is included in consolidated accounts drawn up as t...`; `s 448A(2)(e) the directors have delivered the documents within the period f...`; `s 448A(2)(e) the directors' duty to deliver the documents` | 19 | paragraphs (a) and (d) are inputs of the (2) function; (e) is also a regulative rule |
| s 448A(2)(e)(iv) | 6099 | encoded | `s 448A(2) the conditions for the exemption are complied with`; `s 448A(2)(c) the company is included in consolidated accounts drawn up as t...`; `s 448A(2)(e) the directors have delivered the documents within the period f...`; `s 448A(2)(e) the directors' duty to deliver the documents` | 19 | paragraphs (a) and (d) are inputs of the (2) function; (e) is also a regulative rule |
| s 448A(2)(e)(v) | 6100 | encoded | `s 448A(2) the conditions for the exemption are complied with`; `s 448A(2)(c) the company is included in consolidated accounts drawn up as t...`; `s 448A(2)(e) the directors have delivered the documents within the period f...`; `s 448A(2)(e) the directors' duty to deliver the documents` | 19 | paragraphs (a) and (d) are inputs of the (2) function; (e) is also a regulative rule |
| s 448B | 6101-6105 | fork | `s 448B the company is excluded from the dormant subsidiaries exemption` | 11 | fork F9: the text shows paragraphs (b) and (c) only (no lead-in, no (a)); a company within neither is NOTHING |
| s 448B(b) | 6102-6104 | fork | `s 448B the company is excluded from the dormant subsidiaries exemption` | 11 | fork F9: the text shows paragraphs (b) and (c) only (no lead-in, no (a)); a company within neither is NOTHING |
| s 448B(b)(i) | 6103 | fork | `s 448B the company is excluded from the dormant subsidiaries exemption` | 11 | fork F9: the text shows paragraphs (b) and (c) only (no lead-in, no (a)); a company within neither is NOTHING |
| s 448B(b)(ii) | 6104 | fork | `s 448B the company is excluded from the dormant subsidiaries exemption` | 11 | fork F9: the text shows paragraphs (b) and (c) only (no lead-in, no (a)); a company within neither is NOTHING |
| s 448B(c) | 6105 | fork | `s 448B the company is excluded from the dormant subsidiaries exemption` | 11 | fork F9: the text shows paragraphs (b) and (c) only (no lead-in, no (a)); a company within neither is NOTHING |
| s 448C | 6106-6117 | encoded | `s 448C(1) a guarantee is given by the parent undertaking` | 2 | the section title; the operative text is in the rows below |
| s 448C(1) | 6107 | encoded | `s 448C(1) a guarantee is given by the parent undertaking` | 2 | a "when" read as a "where" (ruling of 2026-11-05) |
| s 448C(2) | 6108-6114 | fork | `s 448C(2) the statement meets the requirements of the section` | 7 | paragraph (c) is blank in the text; case-by-case site S6 (fork register) |
| s 448C(2)(a) | 6109 | encoded | `s 448C(2) the statement meets the requirements of the section` | 7 | paragraph (c) is blank in the text |
| s 448C(2)(b) | 6110 | encoded | `s 448C(2) the statement meets the requirements of the section` | 7 | paragraph (c) is blank in the text |
| s 448C(2)(c) | 6111 | repealed or blank in this text | - | - | the text shows only a row of dots |
| s 448C(2)(d) | 6112 | encoded | `s 448C(2) the statement meets the requirements of the section` | 7 | paragraph (c) is blank in the text |
| s 448C(2)(e) | 6113 | encoded | `s 448C(2) the statement meets the requirements of the section` | 7 | paragraph (c) is blank in the text |
| s 448C(2)(f) | 6114 | encoded | `s 448C(2) the statement meets the requirements of the section` | 7 | paragraph (c) is blank in the text |
| s 448C(3) | 6115-6117 | encoded | `s 448C(3)(a) the amount of the outstanding liabilities that the parent unde...`; `s 448C(3)(b) the person may enforce the guarantee against the parent undert...` | 9 |  |
| s 448C(3)(a) | 6116 | encoded | `s 448C(3)(a) the amount of the outstanding liabilities that the parent unde...`; `s 448C(3)(b) the person may enforce the guarantee against the parent undert...` | 9 |  |
| s 448C(3)(b) | 6117 | encoded | `s 448C(3)(a) the amount of the outstanding liabilities that the parent unde...`; `s 448C(3)(b) the person may enforce the guarantee against the parent undert...` | 9 |  |
| heading at line 6118 Requirements where abbreviated accounts delivered | 6118-6122 | inert (reason 1) | - | - | cross-heading "Requirements where abbreviated accounts delivered" |
| s 449 | 6119-6120 | repealed or blank in this text | - | - | the text shows only a row of dots |
| s 450 | 6121-6122 | repealed or blank in this text | - | - | the text shows only a row of dots |
| heading at line 6123 Failure to file accounts and reports | 6123-6144 | inert (reason 1) | - | - | cross-heading "Failure to file accounts and reports" |
| s 451 | 6124-6128 | encoded | `s 451(1) the person commits an offence`; `s 451(4) the person is guilty of an offence under section 451` | 11 | the section title; the operative text is in the rows below |
| s 451(1) | 6125 | fork | `s 451(1) the person commits an offence` | 5 | a person who was not a director immediately before the end of the period is NOTHING (fork F5); case-by-case site S3, S4 (fork register) |
| s 451(2) | 6126 | encoded | `s 451(2) this section gives the person a defence on these facts` | 2 | ruling of 2026-11-05 (b): not proved is JUST FALSE, worded "gives no defence on these facts" |
| s 451(3) | 6127 | encoded | `s 451(3) proving that the documents were not prepared as required is a defe...` | 2 |  |
| s 451(4) | 6128 | fork | `s 451(4) the penalty in the first text`; `s 451(4) the penalty in the second text`; `s 451(4) the greatest fine on summary conviction in pounds`; `s 451(4) the greatest daily default fine in pounds`; `s 451(4) the person is guilty of an offence under section 451` | 19 | fork F1: line 6128 runs two texts of the daily default fine together; NEEDS-CORE.md |
| s 452 | 6129-6134 | encoded | `s 452(1) the court may order the directors to make good the default` | 6 | the section title; the operative text is in the rows below |
| s 452(1) | 6130-6133 | fork | `s 452(1) the court may order the directors to make good the default`; `s 452(1)(b) the directors failed to make good the default within 14 days af...` | 12 | forks F6 (the last day is the service day plus 14) and F19 (a grant named "may": a failed "If" gate is NOTHING, not JUST FALSE) |
| s 452(1)(a) | 6131 | fork | `s 452(1) the court may order the directors to make good the default`; `s 452(1)(b) the directors failed to make good the default within 14 days af...` | 12 | forks F6 (the last day is the service day plus 14) and F19 (a grant named "may": a failed "If" gate is NOTHING, not JUST FALSE) |
| s 452(1)(b) | 6132-6133 | fork | `s 452(1) the court may order the directors to make good the default`; `s 452(1)(b) the directors failed to make good the default within 14 days af...` | 12 | forks F6 (the last day is the service day plus 14) and F19 (a grant named "may": a failed "If" gate is NOTHING, not JUST FALSE) |
| s 452(2) | 6134 | encoded | `s 452(2) the court's order may provide that all the costs are borne by the ...` | 2 |  |
| s 453 | 6135-6144 | encoded | `s 453(1) the company is liable to a civil penalty` | 3 | the section title; the operative text is in the rows below |
| s 453(1) | 6136-6137 | encoded | `s 453(1) the company is liable to a civil penalty`; `s 453(1) the company's liability is in addition to the directors' liability...` | 5 |  |
| s 453(2) | 6138-6140 | encoded | `s 453(2)(a) the number of days between the end of the period for filing and...`; `s 453(2) the amount of the civil penalty` | 5 | the amount is fixed by regulations outside the sources: an input |
| s 453(2)(a) | 6139 | encoded | `s 453(2)(a) the number of days between the end of the period for filing and...`; `s 453(2) the amount of the civil penalty` | 5 | the amount is fixed by regulations outside the sources: an input |
| s 453(2)(b) | 6140 | encoded | `s 453(2)(a) the number of days between the end of the period for filing and...`; `s 453(2) the amount of the civil penalty` | 5 | the amount is fixed by regulations outside the sources: an input |
| s 453(3) | 6141 | encoded | `s 453(3) the registrar may recover the penalty from the company`; `s 453(3) the penalty is to be paid into the Consolidated Fund` | 6 |  |
| s 453(4) | 6142 | encoded | `s 453(4) proving that the documents were not prepared as required is a defe...` | 2 |  |
| s 453(5) | 6143-6144 | inert (reason 2) | - | - | the parliamentary procedure for regulations |
| heading at line 6145 Chapter 11 — Revision of defective accounts and reports | 6145 | inert (reason 1) | - | - | chapter heading |
| heading at line 6146 Voluntary revision | 6146-6169 | inert (reason 1) | - | - | cross-heading "Voluntary revision" |
| s 454 | 6147-6169 | encoded | `s 454(1) the directors may prepare revised accounts or a revised report or ...` | 6 | the section title; the operative text is in the rows below |
| s 454(1) | 6148-6152 | fork | `s 454(1) the directors may prepare revised accounts or a revised report or ...` | 6 | fork F20: a grant named "may": a failed "If" gate is NOTHING, not JUST FALSE |
| s 454(1)(a) | 6149 | fork | `s 454(1) the directors may prepare revised accounts or a revised report or ...` | 6 | fork F20: a grant named "may": a failed "If" gate is NOTHING, not JUST FALSE |
| s 454(1)(b) | 6150 | fork | `s 454(1) the directors may prepare revised accounts or a revised report or ...` | 6 | fork F20: a grant named "may": a failed "If" gate is NOTHING, not JUST FALSE |
| s 454(1)(c) | 6151-6152 | fork | `s 454(1) the directors may prepare revised accounts or a revised report or ...` | 6 | fork F20: a grant named "may": a failed "If" gate is NOTHING, not JUST FALSE |
| s 454(2) | 6153-6155 | fork | `s 454(2) the revisions are confined to correction and consequential alterat...`; `s 454(2) the revision is within the limit the section sets` | 10 | fork F7: "(in the case of a public company)" is read as qualifying only "laid before the company in general meeting"; a "where" not met is JUST FALSE for the confinement (ruling of 2026-11-05); also case-by-case site S19 |
| s 454(2)(a) | 6154 | encoded | `s 454(2) the revisions are confined to correction and consequential alterat...`; `s 454(2) the revision is within the limit the section sets` | 10 | what the revisions are confined to (the correction) |
| s 454(2)(b) | 6155 | encoded | `s 454(2) the revisions are confined to correction and consequential alterat...`; `s 454(2) the revision is within the limit the section sets` | 10 | what the revisions are confined to (necessary consequential alterations) |
| s 454(3) | 6156-6159 | inert (reason 2) | - | - | a regulation-making power of the Secretary of State and its procedure |
| s 454(3)(a) | 6157 | inert (reason 2) | - | - | a regulation-making power of the Secretary of State and its procedure |
| s 454(3)(b) | 6158 | inert (reason 2) | - | - | a regulation-making power of the Secretary of State and its procedure |
| s 454(3)(c) | 6159 | inert (reason 2) | - | - | a regulation-making power of the Secretary of State and its procedure |
| s 454(4) | 6160-6168 | inert (reason 2) | - | - | a regulation-making power of the Secretary of State and its procedure |
| s 454(4)(a) | 6161 | inert (reason 2) | - | - | a regulation-making power of the Secretary of State and its procedure |
| s 454(4)(b) | 6162 | inert (reason 2) | - | - | a regulation-making power of the Secretary of State and its procedure |
| s 454(4)(c) | 6163-6167 | inert (reason 2) | - | - | a regulation-making power of the Secretary of State and its procedure |
| s 454(4)(c)(i) | 6164 | inert (reason 2) | - | - | a regulation-making power of the Secretary of State and its procedure |
| s 454(4)(c)(ii) | 6165 | inert (reason 2) | - | - | a regulation-making power of the Secretary of State and its procedure |
| s 454(4)(c)(iii) | 6166-6167 | inert (reason 2) | - | - | a regulation-making power of the Secretary of State and its procedure |
| s 454(4)(d) | 6168 | inert (reason 2) | - | - | a regulation-making power of the Secretary of State and its procedure |
| s 454(5) | 6169 | inert (reason 2) | - | - | a regulation-making power of the Secretary of State and its procedure |
| heading at line 6170 Secretary of State's notice | 6170-6182 | inert (reason 1) | - | - | cross-heading "Secretary of State's notice" |
| s 455 | 6171-6182 | encoded | `s 455(1) section 455 applies` | 5 | the section title; the operative text is in the rows below |
| s 455(1) | 6172-6175 | encoded | `s 455(1) section 455 applies` | 5 |  |
| s 455(1)(a) | 6173 | encoded | `s 455(1) section 455 applies` | 5 |  |
| s 455(1)(b) | 6174-6175 | fork | `s 455(1) section 455 applies` | 5 | fork F7: "(in the case of a public company)" is read as qualifying only "laid before the company in general meeting" |
| s 455(2) | 6176 | encoded | `s 455(2) the Secretary of State may give notice to the directors indicating...` | 3 |  |
| s 455(3) | 6177 | fork | `s 455(3) the period the notice specifies is not less than one month` | 3 | fork F10: one month counted by the library `add months`; also case-by-case site S20 |
| s 455(4) | 6178-6181 | fork | `s 455(4) the Secretary of State may apply to the court` | 6 | fork F11: "have not (a) ... or (b)" read as "have done neither" |
| s 455(4)(a) | 6179 | fork | `s 455(4) the Secretary of State may apply to the court` | 6 | fork F11: "have not (a) ... or (b)" read as "have done neither" |
| s 455(4)(b) | 6180-6181 | fork | `s 455(4) the Secretary of State may apply to the court` | 6 | fork F11: "have not (a) ... or (b)" read as "have done neither" |
| s 455(5) | 6182 | encoded | `s 455(5) section 455 applies equally to the revised document`; `s 455(5) the references to revised accounts or reports are read as referenc...` | 6 |  |
| heading at line 6183 Application to court | 6183-6244 | inert (reason 1) | - | - | cross-heading "Application to court" |
| s 456 | 6184-6207 | encoded | `s 456(1) the applicant may apply to the court for a declaration and an order` | 4 | the section title; the operative text is in the rows below |
| s 456(1) | 6185-6188 | fork | `s 456(1) the applicant may apply to the court for a declaration and an order` | 4 | fork F15: the list of who may apply is not closed with "only", so another person is NOTHING |
| s 456(1)(a) | 6186 | fork | `s 456(1) the applicant may apply to the court for a declaration and an order` | 4 | fork F15: the list of who may apply is not closed with "only", so another person is NOTHING |
| s 456(1)(b) | 6187-6188 | fork | `s 456(1) the applicant may apply to the court for a declaration and an order` | 4 | fork F15: the list of who may apply is not closed with "only", so another person is NOTHING |
| s 456(2) | 6189 | fork | `s 456(2) the applicant has given the registrar the notice the section requires` | 2 | case-by-case site S21 (fork register) |
| s 456(3) | 6190-6194 | fork | `s 456(3) the court may give the direction` | 7 | fork F21: a grant named "may": a failed "If" gate is NOTHING, not JUST FALSE |
| s 456(3)(a) | 6191 | encoded | `s 456(3) the court may give the direction` | 7 | a kind of direction the court may give |
| s 456(3)(b) | 6192 | encoded | `s 456(3) the court may give the direction` | 7 | a kind of direction the court may give |
| s 456(3)(c) | 6193-6194 | encoded | `s 456(3) the court may give the direction` | 7 | a kind of direction the court may give |
| s 456(4) | 6195-6199 | fork | `s 456(4) the court may give the direction` | 5 | fork F22: a grant named "may": a failed "If" gate is NOTHING, not JUST FALSE |
| s 456(4)(a) | 6196 | encoded | `s 456(4) the court may give the direction` | 5 | a kind of direction the court may give |
| s 456(4)(b) | 6197 | repealed or blank in this text | - | - | the text shows only a row of dots |
| s 456(4)(c) | 6198 | encoded | `s 456(4) the court may give the direction` | 5 | a kind of direction the court may give |
| s 456(4)(d) | 6199 | encoded | `s 456(4) the court may give the direction` | 5 | a kind of direction the court may give |
| s 456(5) | 6200-6204 | encoded | `s 456(5) the director is taken to have been a party to the approval of the ...`; `s 456(5) the court may order that the director bear the costs and expenses` | 7 | fork F23: the court's power is a grant named "may": a failed "If" gate is NOTHING, not JUST FALSE; the presumption function ("unless he shows" met is JUST FALSE) is a case-by-case site |
| s 456(5)(a) | 6201 | encoded | `s 456(5) the court may order that the director bear the costs and expenses` | 4 | the costs and expenses of the application |
| s 456(5)(b) | 6202-6204 | fork | `s 456(5) the director is taken to have been a party to the approval of the ...`; `s 456(5) the court may order that the director bear the costs and expenses` | 7 | fork F23: the court's power is a grant named "may": a failed "If" gate is NOTHING, not JUST FALSE; the presumption function ("unless he shows" met is JUST FALSE) is a case-by-case site; case-by-case site S22 (fork register) |
| s 456(6) | 6205 | encoded | `s 456(6) the court may exclude one or more directors from the order or orde...`; `s 456(6) the director knew or ought to have known that the accounts or repo...` | 5 |  |
| s 456(7) | 6206 | fork | `s 456(7) the applicant's duty to inform the registrar`; `s 456(7) the applicant has complied` | 6 | a regulative rule with no WITHIN (the text states no time) and a decision function; case-by-case site S23, S24 (fork register) |
| s 456(8) | 6207 | encoded | `s 456(8) section 456 applies equally to the revised document` | 2 |  |
| s 457 | 6208-6219 | inert (reason 2) | - | - | the Secretary of State's power to authorise persons by order, and its limits |
| s 457(1) | 6209-6212 | inert (reason 2) | - | - | the Secretary of State's power to authorise persons by order, and its limits |
| s 457(1)(a) | 6210 | inert (reason 2) | - | - | the Secretary of State's power to authorise persons by order, and its limits |
| s 457(1)(b) | 6211 | inert (reason 2) | - | - | the Secretary of State's power to authorise persons by order, and its limits |
| s 457(1)(c) | 6212 | inert (reason 2) | - | - | the Secretary of State's power to authorise persons by order, and its limits |
| s 457(2) | 6213 | inert (reason 2) | - | - | the Secretary of State's power to authorise persons by order, and its limits |
| s 457(3) | 6214 | inert (reason 2) | - | - | the Secretary of State's power to authorise persons by order, and its limits |
| s 457(4) | 6215 | fork | `s 457(4) the proceedings may be brought by or against the association in th...` | 4 | fork F24: a grant named "may": a failed "If" gate is NOTHING, not JUST FALSE; what it means to a person suing or sued |
| s 457(5) | 6216-6217 | inert (reason 2) | - | - | the Secretary of State's power to authorise persons by order, and its limits |
| s 457(6) | 6218 | inert (reason 2) | - | - | the Secretary of State's power to authorise persons by order, and its limits |
| s 457(7) | 6219 | inert (reason 2) | - | - | the Secretary of State's power to authorise persons by order, and its limits |
| s 458 | 6220-6244 | encoded | `s 458(1) the Commissioners may disclose the information to the authorised p...` | 6 | the section title; the operative text is in the rows below |
| s 458(1) | 6221-6223 | encoded | `s 458(1) the Commissioners may disclose the information to the authorised p...` | 6 | the permission to disclose; the data-protection proviso printed after (2) is encoded in the same function |
| s 458(1)(a) | 6222 | encoded | `s 458(1) the Commissioners may disclose the information to the authorised p...` | 6 | the permission to disclose; the data-protection proviso printed after (2) is encoded in the same function |
| s 458(1)(b) | 6223 | encoded | `s 458(1) the Commissioners may disclose the information to the authorised p...` | 6 | the permission to disclose; the data-protection proviso printed after (2) is encoded in the same function |
| s 458(2) | 6224-6225 | encoded | `s 458(2) a statutory or other restriction bars the disclosure under this se...`; `s 458(1) the Commissioners may disclose the information to the authorised p...` | 8 | the text prints the data-protection proviso (line 6225) as part of (2); the encoding applies it inside the s 458(1) function, whose quoted lines run to 6225 (finding) |
| s 458(3) | 6226-6233 | encoded | `s 458(3)(a) the section bars the use of the information`; `s 458(3)(b) the section bars the further disclosure of the information` | 7 | an "except" met is JUST FALSE (case-by-case ruling) |
| s 458(3)(a) | 6227-6230 | fork | `s 458(3)(a) the section bars the use of the information`; `s 458(3)(b) the section bars the further disclosure of the information` | 7 | an "except" met is JUST FALSE (case-by-case ruling); case-by-case site S1 (fork register) |
| s 458(3)(a)(i) | 6228 | encoded | `s 458(3)(a) the section bars the use of the information`; `s 458(3)(b) the section bars the further disclosure of the information` | 7 | an "except" met is JUST FALSE (case-by-case ruling) |
| s 458(3)(a)(ii) | 6229-6230 | encoded | `s 458(3)(a) the section bars the use of the information`; `s 458(3)(b) the section bars the further disclosure of the information` | 7 | an "except" met is JUST FALSE (case-by-case ruling) |
| s 458(3)(b) | 6231-6233 | fork | `s 458(3)(a) the section bars the use of the information`; `s 458(3)(b) the section bars the further disclosure of the information` | 7 | an "except" met is JUST FALSE (case-by-case ruling); case-by-case site S2 (fork register) |
| s 458(3)(b)(i) | 6232 | encoded | `s 458(3)(a) the section bars the use of the information`; `s 458(3)(b) the section bars the further disclosure of the information` | 7 | an "except" met is JUST FALSE (case-by-case ruling) |
| s 458(3)(b)(ii) | 6233 | encoded | `s 458(3)(a) the section bars the use of the information`; `s 458(3)(b) the section bars the further disclosure of the information` | 7 | an "except" met is JUST FALSE (case-by-case ruling) |
| s 458(4) | 6234-6236 | encoded | `s 458(4) the person commits an offence` | 6 | an "unless" met is JUST FALSE (case-by-case ruling) |
| s 458(4)(a) | 6235 | encoded | `s 458(4) the person commits an offence` | 6 | an "unless" met is JUST FALSE (case-by-case ruling) |
| s 458(4)(b) | 6236 | encoded | `s 458(4) the person commits an offence` | 6 | an "unless" met is JUST FALSE (case-by-case ruling) |
| s 458(5) | 6237-6241 | encoded | `s 458(5) the penalty for the offence` | 5 | the core `Penalty` record, by place of conviction |
| s 458(5)(a) | 6238 | encoded | `s 458(5) the penalty for the offence` | 5 | the core `Penalty` record, by place of conviction |
| s 458(5)(b) | 6239-6241 | encoded | `s 458(5) the penalty for the offence` | 5 | the core `Penalty` record, by place of conviction |
| s 458(5)(b)(i) | 6240 | encoded | `s 458(5) the penalty for the offence` | 5 | the core `Penalty` record, by place of conviction |
| s 458(5)(b)(ii) | 6241 | encoded | `s 458(5) the penalty for the offence` | 5 | the core `Penalty` record, by place of conviction |
| s 458(6) | 6242-6244 | encoded | `s 458(6) the person is treated as an officer of the body`; `s 458(6) the officer of the body corporate also commits the offence` | 9 | the s 1121 answer is an input |
| s 458(6)(a) | 6243 | encoded | `s 458(6) the person is treated as an officer of the body`; `s 458(6) the officer of the body corporate also commits the offence` | 9 | the s 1121 answer is an input |
| s 458(6)(b) | 6244 | encoded | `s 458(6) the person is treated as an officer of the body`; `s 458(6) the officer of the body corporate also commits the offence` | 9 | the s 1121 answer is an input |
| heading at line 6245 Power of authorised person to require documents etc | 6245-6322 | inert (reason 1) | - | - | cross-heading "Power of authorised person to require documents etc" |
| s 459 | 6246-6259 | encoded | `s 459(2) the authorised person may require the person to produce the docume...` | 5 | the section title; the operative text is in the rows below |
| s 459(1) | 6247 | encoded | `s 459(1) section 459 applies` | 2 |  |
| s 459(2) | 6248-6250 | encoded | `s 459(2) the authorised person may require the person to produce the docume...` | 5 |  |
| s 459(2)(a) | 6249 | encoded | `s 459(2) the authorised person may require the person to produce the docume...` | 5 |  |
| s 459(2)(b) | 6250 | encoded | `s 459(2) the authorised person may require the person to produce the docume...` | 5 |  |
| s 459(3) | 6251-6254 | fork | `s 459(3) the person is one whom the authorised person may require` | 4 | fork F14: the list is not closed with "only", so another person is NOTHING |
| s 459(3)(a) | 6252 | fork | `s 459(3) the person is one whom the authorised person may require` | 4 | fork F14: the list is not closed with "only", so another person is NOTHING |
| s 459(3)(b) | 6253 | fork | `s 459(3) the person is one whom the authorised person may require` | 4 | fork F14: the list is not closed with "only", so another person is NOTHING |
| s 459(3)(c) | 6254 | fork | `s 459(3) the person is one whom the authorised person may require` | 4 | fork F14: the list is not closed with "only", so another person is NOTHING |
| s 459(4) | 6255 | fork | `s 459(4) the authorised person may apply to the court` | 2 | fork F25: a grant named "may": a failed "If" gate is NOTHING, not JUST FALSE |
| s 459(5) | 6256 | fork | `s 459(5) the court may order the person to take such steps as it directs` | 2 | fork F26: a grant named "may": a failed "If" gate is NOTHING, not JUST FALSE |
| s 459(6) | 6257 | encoded | `s 459(6) the statement may be used in evidence against the person who made it` | 3 |  |
| s 459(7) | 6258 | encoded | `s 459(7) the section compels the person to disclose the document or informa...` | 2 |  |
| s 459(8) | 6259 | encoded | `s 459(8) the thing is a document for the purposes of section 459` | 2 | "includes" |
| s 460 | 6260-6276 | encoded | `s 460(2) the section bars the disclosure of the information` | 7 | the section title; the operative text is in the rows below |
| s 460(1) | 6261 | encoded | `s 460(1) the information is within section 460` | 3 |  |
| s 460(2) | 6262 | encoded | `s 460(2) the section bars the disclosure of the information` | 7 | consent: limited by its own wording, NOTHING |
| s 460(3) | 6263-6265 | encoded | `s 460(2) the section bars the disclosure of the information` | 7 | a flat negative: JUST FALSE where s 461 permits or the information is public |
| s 460(3)(a) | 6264 | encoded | `s 460(2) the section bars the disclosure of the information` | 7 | a flat negative: JUST FALSE where s 461 permits or the information is public |
| s 460(3)(b) | 6265 | encoded | `s 460(2) the section bars the disclosure of the information` | 7 | a flat negative: JUST FALSE where s 461 permits or the information is public |
| s 460(4) | 6266-6268 | encoded | `s 460(4) the person commits an offence` | 4 |  |
| s 460(4)(a) | 6267 | encoded | `s 460(4) the person commits an offence` | 4 |  |
| s 460(4)(b) | 6268 | encoded | `s 460(4) the person commits an offence` | 4 |  |
| s 460(5) | 6269-6273 | encoded | `s 460(5) the penalty for the offence` | 3 | the same penalties as s 458(5) |
| s 460(5)(a) | 6270 | encoded | `s 460(5) the penalty for the offence` | 3 | the same penalties as s 458(5) |
| s 460(5)(b) | 6271-6273 | encoded | `s 460(5) the penalty for the offence` | 3 | the same penalties as s 458(5) |
| s 460(5)(b)(i) | 6272 | encoded | `s 460(5) the penalty for the offence` | 3 | the same penalties as s 458(5) |
| s 460(5)(b)(ii) | 6273 | encoded | `s 460(5) the penalty for the offence` | 3 | the same penalties as s 458(5) |
| s 460(6) | 6274-6276 | encoded | `s 460(6) the person is treated as an officer of the body`; `s 460(6) the officer of the body corporate also commits the offence` | 4 | the same sentence as s 458(6) |
| s 460(6)(a) | 6275 | encoded | `s 460(6) the person is treated as an officer of the body`; `s 460(6) the officer of the body corporate also commits the offence` | 4 | the same sentence as s 458(6) |
| s 460(6)(b) | 6276 | encoded | `s 460(6) the person is treated as an officer of the body`; `s 460(6) the officer of the body corporate also commits the offence` | 4 | the same sentence as s 458(6) |
| s 461 | 6277-6315 | encoded | `s 461(1) the disclosure is permitted by section 461` | 6 | the section title; the operative text is in the rows below |
| s 461(1) | 6278 | encoded | `s 461(1) the disclosure is permitted by section 461` | 6 |  |
| s 461(2) | 6279 | encoded | `s 461(2) the prohibition in section 460 does not apply to the disclosure` | 2 |  |
| s 461(3) | 6280-6287 | fork | `s 461(3) the prohibition in section 460 does not apply to disclosure to the...`; `s 461 the Secretary of State` | 10 | fork F16: the list of recipients is not closed with "only"; a constructor of `s 461 recipient` for each paragraph |
| s 461(3)(a) | 6281 | fork | `s 461(3) the prohibition in section 460 does not apply to disclosure to the...`; `s 461 the Secretary of State` | 10 | fork F16: the list of recipients is not closed with "only"; a constructor of `s 461 recipient` for each paragraph |
| s 461(3)(b) | 6282 | fork | `s 461(3) the prohibition in section 460 does not apply to disclosure to the...`; `s 461 the Secretary of State` | 10 | fork F16: the list of recipients is not closed with "only"; a constructor of `s 461 recipient` for each paragraph |
| s 461(3)(c) | 6283 | fork | `s 461(3) the prohibition in section 460 does not apply to disclosure to the...`; `s 461 the Secretary of State` | 10 | fork F16: the list of recipients is not closed with "only"; a constructor of `s 461 recipient` for each paragraph |
| s 461(3)(d) | 6284 | fork | `s 461(3) the prohibition in section 460 does not apply to disclosure to the...`; `s 461 the Secretary of State` | 10 | fork F16: the list of recipients is not closed with "only"; a constructor of `s 461 recipient` for each paragraph |
| s 461(3)(e) | 6285 | fork | `s 461(3) the prohibition in section 460 does not apply to disclosure to the...`; `s 461 the Secretary of State` | 10 | fork F16: the list of recipients is not closed with "only"; a constructor of `s 461 recipient` for each paragraph |
| s 461(3)(ea) | 6286 | fork | `s 461(3) the prohibition in section 460 does not apply to disclosure to the...`; `s 461 the Secretary of State` | 10 | fork F16: the list of recipients is not closed with "only"; a constructor of `s 461 recipient` for each paragraph |
| s 461(3)(f) | 6287 | fork | `s 461(3) the prohibition in section 460 does not apply to disclosure to the...`; `s 461 the Secretary of State` | 10 | fork F16: the list of recipients is not closed with "only"; a constructor of `s 461 recipient` for each paragraph |
| s 461(4) | 6288-6308 | fork | `s 461(4) the prohibition in section 460 does not apply to disclosure for th...` | 4 | fork F16: the list of purposes is not closed with "only"; a constructor of `s 461 purpose` for each paragraph |
| s 461(4)(a) | 6289 | fork | `s 461(4) the prohibition in section 460 does not apply to disclosure for th...` | 4 | fork F16: the list of purposes is not closed with "only"; a constructor of `s 461 purpose` for each paragraph |
| s 461(4)(aa) | 6290 | fork | `s 461(4) the prohibition in section 460 does not apply to disclosure for th...` | 4 | fork F16: the list of purposes is not closed with "only"; a constructor of `s 461 purpose` for each paragraph |
| s 461(4)(b) | 6291 | fork | `s 461(4) the prohibition in section 460 does not apply to disclosure for th...` | 4 | fork F16: the list of purposes is not closed with "only"; a constructor of `s 461 purpose` for each paragraph |
| s 461(4)(c) | 6292-6297 | fork | `s 461(4) the prohibition in section 460 does not apply to disclosure for th...` | 4 | fork F16: the list of purposes is not closed with "only"; a constructor of `s 461 purpose` for each paragraph |
| s 461(4)(c)(i) | 6293 | fork | `s 461(4) the prohibition in section 460 does not apply to disclosure for th...` | 4 | fork F16: the list of purposes is not closed with "only"; a constructor of `s 461 purpose` for each paragraph |
| s 461(4)(c)(ii) | 6294 | fork | `s 461(4) the prohibition in section 460 does not apply to disclosure for th...` | 4 | fork F16: the list of purposes is not closed with "only"; a constructor of `s 461 purpose` for each paragraph |
| s 461(4)(c)(iii) | 6295 | fork | `s 461(4) the prohibition in section 460 does not apply to disclosure for th...` | 4 | fork F16: the list of purposes is not closed with "only"; a constructor of `s 461 purpose` for each paragraph |
| s 461(4)(c)(iv) | 6296 | fork | `s 461(4) the prohibition in section 460 does not apply to disclosure for th...` | 4 | fork F16: the list of purposes is not closed with "only"; a constructor of `s 461 purpose` for each paragraph |
| s 461(4)(c)(v) | 6297 | fork | `s 461(4) the prohibition in section 460 does not apply to disclosure for th...` | 4 | fork F16: the list of purposes is not closed with "only"; a constructor of `s 461 purpose` for each paragraph |
| s 461(4)(d) | 6298 | fork | `s 461(4) the prohibition in section 460 does not apply to disclosure for th...` | 4 | fork F16: the list of purposes is not closed with "only"; a constructor of `s 461 purpose` for each paragraph |
| s 461(4)(e) | 6299 | fork | `s 461(4) the prohibition in section 460 does not apply to disclosure for th...` | 4 | fork F16: the list of purposes is not closed with "only"; a constructor of `s 461 purpose` for each paragraph |
| s 461(4)(f) | 6300 | fork | `s 461(4) the prohibition in section 460 does not apply to disclosure for th...` | 4 | fork F16: the list of purposes is not closed with "only"; a constructor of `s 461 purpose` for each paragraph |
| s 461(4)(g) | 6301-6307 | fork | `s 461(4) the prohibition in section 460 does not apply to disclosure for th...` | 4 | fork F16: the list of purposes is not closed with "only"; a constructor of `s 461 purpose` for each paragraph |
| s 461(4)(g)(i) | 6302 | fork | `s 461(4) the prohibition in section 460 does not apply to disclosure for th...` | 4 | fork F16: the list of purposes is not closed with "only"; a constructor of `s 461 purpose` for each paragraph |
| s 461(4)(g)(ia) | 6303 | fork | `s 461(4) the prohibition in section 460 does not apply to disclosure for th...` | 4 | fork F16: the list of purposes is not closed with "only"; a constructor of `s 461 purpose` for each paragraph |
| s 461(4)(g)(ii) | 6304 | fork | `s 461(4) the prohibition in section 460 does not apply to disclosure for th...` | 4 | fork F16: the list of purposes is not closed with "only"; a constructor of `s 461 purpose` for each paragraph |
| s 461(4)(g)(iii) | 6305 | fork | `s 461(4) the prohibition in section 460 does not apply to disclosure for th...` | 4 | fork F16: the list of purposes is not closed with "only"; a constructor of `s 461 purpose` for each paragraph |
| s 461(4)(g)(iv) | 6306 | fork | `s 461(4) the prohibition in section 460 does not apply to disclosure for th...` | 4 | fork F16: the list of purposes is not closed with "only"; a constructor of `s 461 purpose` for each paragraph |
| s 461(4)(g)(v) | 6307 | fork | `s 461(4) the prohibition in section 460 does not apply to disclosure for th...` | 4 | fork F16: the list of purposes is not closed with "only"; a constructor of `s 461 purpose` for each paragraph |
| s 461(4)(h) | 6308 | fork | `s 461(4) the prohibition in section 460 does not apply to disclosure for th...` | 4 | fork F16: the list of purposes is not closed with "only"; a constructor of `s 461 purpose` for each paragraph |
| s 461(5) | 6309 | encoded | `s 461(5) the prohibition in section 460 does not apply to disclosure to the...` | 4 |  |
| s 461(6) | 6310-6314 | fork | `s 461(6) the authorised person has had regard to the considerations the sec...` | 3 | a bare "must" not done: JUST FALSE (case-by-case ruling); case-by-case site S5 (fork register) |
| s 461(6)(a) | 6311 | encoded | `s 461(6) the authorised person has had regard to the considerations the sec...` | 3 | a bare "must" not done: JUST FALSE (case-by-case ruling) |
| s 461(6)(b) | 6312-6314 | encoded | `s 461(6) the authorised person has had regard to the considerations the sec...` | 3 | a bare "must" not done: JUST FALSE (case-by-case ruling) |
| s 461(6)(b)(i) | 6313 | encoded | `s 461(6) the authorised person has had regard to the considerations the sec...` | 3 | a bare "must" not done: JUST FALSE (case-by-case ruling) |
| s 461(6)(b)(ii) | 6314 | encoded | `s 461(6) the authorised person has had regard to the considerations the sec...` | 3 | a bare "must" not done: JUST FALSE (case-by-case ruling) |
| s 461(7) | 6315 | encoded | `s 461(7) the section authorises the disclosure` | 2 | a flat negative |
| s 462 | 6316-6322 | inert (reason 2) | - | - | the Secretary of State's order-making power to amend s 461 and its limits |
| s 462(1) | 6317 | inert (reason 2) | - | - | the Secretary of State's order-making power to amend s 461 and its limits |
| s 462(2) | 6318-6321 | inert (reason 2) | - | - | the Secretary of State's order-making power to amend s 461 and its limits |
| s 462(2)(a) | 6319 | inert (reason 2) | - | - | the Secretary of State's order-making power to amend s 461 and its limits |
| s 462(2)(b) | 6320 | inert (reason 2) | - | - | the Secretary of State's order-making power to amend s 461 and its limits |
| s 462(2)(c) | 6321 | inert (reason 2) | - | - | the Secretary of State's order-making power to amend s 461 and its limits |
| s 462(3) | 6322 | inert (reason 2) | - | - | the Secretary of State's order-making power to amend s 461 and its limits |
| heading at line 6323 Chapter 12 — Supplementary provisions | 6323 | inert (reason 1) | - | - | chapter heading |
| heading at line 6324 Liability for false or misleading statements in reports and  | 6324-6342 | inert (reason 1) | - | - | cross-heading "Liability for false or misleading statements in reports and statements" |
| s 463 | 6325-6342 | encoded | `s 463(2) the director is liable to compensate the company for the loss` | 7 | the section title; the operative text is in the rows below |
| s 463(1) | 6326-6331 | fork | `s 463(1) the section applies to the report or statement` | 5 | fork F13: the list of reports and statements is not closed with "only" |
| s 463(1)(za) | 6327 | fork | `s 463(1) the section applies to the report or statement` | 5 | fork F13: the list of reports and statements is not closed with "only" |
| s 463(1)(a) | 6328 | fork | `s 463(1) the section applies to the report or statement` | 5 | fork F13: the list of reports and statements is not closed with "only" |
| s 463(1)(b) | 6329 | fork | `s 463(1) the section applies to the report or statement` | 5 | fork F13: the list of reports and statements is not closed with "only" |
| s 463(1)(c) | 6330 | repealed or blank in this text | - | - | the text shows only a row of dots |
| s 463(1)(d) | 6331 | fork | `s 463(1) the section applies to the report or statement` | 5 | fork F13: the list of reports and statements is not closed with "only" |
| s 463(2) | 6332-6334 | encoded | `s 463(2) the director is liable to compensate the company for the loss` | 7 |  |
| s 463(2)(a) | 6333 | encoded | `s 463(2) the director is liable to compensate the company for the loss` | 7 |  |
| s 463(2)(b) | 6334 | encoded | `s 463(2) the director is liable to compensate the company for the loss` | 7 |  |
| s 463(3) | 6335-6337 | fork | `s 463(2) the director is liable to compensate the company for the loss` | 7 | fork F17: limb (a) or limb (b) of the "only if" either suffices, whichever of (2)(a) or (2)(b) caused the loss |
| s 463(3)(a) | 6336 | fork | `s 463(2) the director is liable to compensate the company for the loss` | 7 | fork F17: limb (a) or limb (b) of the "only if" either suffices, whichever of (2)(a) or (2)(b) caused the loss |
| s 463(3)(b) | 6337 | fork | `s 463(2) the director is liable to compensate the company for the loss` | 7 | fork F17: limb (a) or limb (b) of the "only if" either suffices, whichever of (2)(a) or (2)(b) caused the loss |
| s 463(4) | 6338 | encoded | `s 463(4) a person is subject to liability to the claimant` | 4 |  |
| s 463(5) | 6339 | encoded | `s 463(5) the claim is within the liability that subsection (4) removes` | 2 | "includes" |
| s 463(6) | 6340-6342 | encoded | `s 463(6) the section affects the liability` | 3 |  |
| s 463(6)(a) | 6341 | encoded | `s 463(6) the section affects the liability` | 3 |  |
| s 463(6)(b) | 6342 | encoded | `s 463(6) the section affects the liability` | 3 |  |
| heading at line 6343 Accounting and reporting standards | 6343-6347 | inert (reason 1) | - | - | cross-heading "Accounting and reporting standards" |
| s 464 | 6344-6347 | encoded | `s 464(1) the statement is an accounting standard` | 4 | the section title; the operative text is in the rows below |
| s 464(1) | 6345 | encoded | `s 464(1) the statement is an accounting standard` | 4 | the prescribing body is s 1167's (a MAYBE BOOLEAN input) |
| s 464(2) | 6346 | encoded | `s 464(2) the accounting standard is applicable to the company's annual acco...` | 5 |  |
| s 464(3) | 6347 | inert (reason 2) | - | - | a regulation-making power of the Secretary of State |
| heading at line 6348 Companies qualifying as medium-sized | 6348-6406 | inert (reason 1) | - | - | cross-heading "Companies qualifying as medium-sized" |
| s 465 | 6349-6365 | encoded | `s 465(7) the company qualifies as medium-sized, subject to section 466` | 7 | the section title; the operative text is in the rows below |
| s 465(1) | 6350 | encoded | `s 465(1) the company qualifies as medium-sized in relation to its first fin...` | 2 |  |
| s 465(2) | 6351-6354 | encoded | `s 465(2) the company qualifies as medium-sized in relation to a subsequent ...` | 8 |  |
| s 465(2)(a) | 6352 | encoded | `s 465(2) the company qualifies as medium-sized in relation to a subsequent ...` | 8 |  |
| s 465(2)(b) | 6353 | encoded | `s 465(2) the company qualifies as medium-sized in relation to a subsequent ...` | 8 |  |
| s 465(2)(c) | 6354 | encoded | `s 465(2) the company qualifies as medium-sized in relation to a subsequent ...` | 8 |  |
| s 465(3) | 6355-6358 | encoded | `s 465(3) the qualifying conditions are met` | 9 | two or more of the three requirements |
| s 465(3) table row 1 | 6356 | encoded | `s 465(3) the requirement for turnover is satisfied` | 4 | 54,000,000 pounds, adjusted by (4) |
| s 465(3) table row 2 | 6357 | encoded | `s 465(3) the requirement for the balance sheet total is satisfied` | 2 | 27,000,000 pounds |
| s 465(3) table row 3 | 6358 | encoded | `s 465(3) the requirement for the number of employees is satisfied` | 2 | 250 |
| s 465(4) | 6359 | fork | `s 465(4) the maximum figure for turnover for the financial year` | 3 | fork F8: "proportionately" read in months |
| s 465(5) | 6360 | encoded | `s 465(5) the balance sheet total` | 2 |  |
| s 465(6) | 6361-6364 | encoded | `s 465(6) the number of employees` | 3 |  |
| s 465(6)(a) | 6362 | encoded | `s 465(6) the number of employees` | 3 |  |
| s 465(6)(b) | 6363 | encoded | `s 465(6) the number of employees` | 3 |  |
| s 465(6)(c) | 6364 | encoded | `s 465(6) the number of employees` | 3 |  |
| s 465(7) | 6365 | encoded | `s 465(7) the company qualifies as medium-sized, subject to section 466` | 7 |  |
| s 466 | 6366-6387 | encoded | `s 466(1) the parent company qualifies as a medium-sized company` | 3 | the section title; the operative text is in the rows below |
| s 466(1) | 6367 | encoded | `s 466(1) the parent company qualifies as a medium-sized company` | 3 | "only if": JUST FALSE or NOTHING, never JUST TRUE |
| s 466(2) | 6368 | encoded | `s 466(2) the group qualifies as medium-sized in relation to the parent comp...` | 2 |  |
| s 466(3) | 6369-6372 | encoded | `s 466(3) the group qualifies as medium-sized in relation to a subsequent fi...` | 5 |  |
| s 466(3)(a) | 6370 | encoded | `s 466(3) the group qualifies as medium-sized in relation to a subsequent fi...` | 5 |  |
| s 466(3)(b) | 6371 | encoded | `s 466(3) the group qualifies as medium-sized in relation to a subsequent fi...` | 5 |  |
| s 466(3)(c) | 6372 | encoded | `s 466(3) the group qualifies as medium-sized in relation to a subsequent fi...` | 5 |  |
| s 466(4) | 6373-6376 | encoded | `s 466(4) the qualifying conditions are met by the group` | 4 |  |
| s 466(4) table row 1 | 6374 | encoded | `s 466(4) the requirement for aggregate turnover is satisfied` | 3 | 54,000,000 pounds net or 64,000,000 gross |
| s 466(4) table row 2 | 6375 | encoded | `s 466(4) the requirement for the aggregate balance sheet total is satisfied` | 3 | 27,000,000 pounds net or 32,000,000 gross |
| s 466(4) table row 3 | 6376 | encoded | `s 466(4) the requirement for the aggregate number of employees is satisfied` | 2 | 250 |
| s 466(5) | 6377 | encoded | `s 466(5) the aggregate figure` | 1 |  |
| s 466(6) | 6378-6383 | encoded | `s 466(6) the figure is a net figure`; `s 466(6) the figure is a gross figure`; `s 466(4) the qualifying conditions are met by the group` | 9 | the closing sentence (a company may satisfy a requirement on either the net or the gross figure) is applied inside s 466(4)'s function |
| s 466 term net | 6379 | encoded | `s 466(6) the figure is a net figure` | 3 |  |
| s 466 term net(a) | 6380 | encoded | `s 466(6) the figure is a net figure` | 3 |  |
| s 466 term net(b) | 6381 | encoded | `s 466(6) the figure is a net figure` | 3 |  |
| s 466 term gross | 6382-6383 | encoded | `s 466(6) the figure is a gross figure`; `s 466(4) the qualifying conditions are met by the group` | 6 | the closing sentence (either figure) is applied inside s 466(4)'s function |
| s 466(7) | 6384-6387 | encoded | `s 466(7) the end of the subsidiary undertaking's financial year whose figur...`; `s 466(7) the figures to take for the subsidiary undertaking` | 7 |  |
| s 466(7)(a) | 6385 | encoded | `s 466(7) the end of the subsidiary undertaking's financial year whose figur...`; `s 466(7) the figures to take for the subsidiary undertaking` | 7 |  |
| s 466(7)(b) | 6386-6387 | encoded | `s 466(7) the end of the subsidiary undertaking's financial year whose figur...`; `s 466(7) the figures to take for the subsidiary undertaking` | 7 |  |
| s 467 | 6388-6406 | encoded | `s 467(1) the section bars the company from taking advantage of the medium-s...` | 9 | the section title; the operative text is in the rows below |
| s 467(1) | 6389-6396 | encoded | `s 467(1) the section bars the company from taking advantage of the medium-s...` | 9 | titled as the bar |
| s 467(1)(a) | 6390 | encoded | `s 467(1) the section bars the company from taking advantage of the medium-s...` | 9 | titled as the bar |
| s 467(1)(b) | 6391-6394 | encoded | `s 467(1) the section bars the company from taking advantage of the medium-s...` | 9 | titled as the bar |
| s 467(1)(b)(i) | 6392 | encoded | `s 467(1) the section bars the company from taking advantage of the medium-s...` | 9 | titled as the bar |
| s 467(1)(b)(ii) | 6393 | encoded | `s 467(1) the section bars the company from taking advantage of the medium-s...` | 9 | titled as the bar |
| s 467(1)(b)(iii) | 6394 | encoded | `s 467(1) the section bars the company from taking advantage of the medium-s...` | 9 | titled as the bar |
| s 467(1)(ba) | 6395 | encoded | `s 467(1) the section bars the company from taking advantage of the medium-s...` | 9 | titled as the bar |
| s 467(1)(c) | 6396 | encoded | `s 467(1) the section bars the company from taking advantage of the medium-s...` | 9 | titled as the bar |
| s 467(2) | 6397-6404 | encoded | `s 467(2) the member is within one of the paragraphs`; `s 467(2) the group is ineligible` | 15 | "(other than a small company)" in (c) and "a small company" in (d): decided at this site |
| s 467(2)(a) | 6398 | encoded | `s 467(2) the member is within one of the paragraphs`; `s 467(2) the group is ineligible` | 15 | "(other than a small company)" in (c) and "a small company" in (d): decided at this site |
| s 467(2)(b) | 6399 | encoded | `s 467(2) the member is within one of the paragraphs`; `s 467(2) the group is ineligible` | 15 | "(other than a small company)" in (c) and "a small company" in (d): decided at this site |
| s 467(2)(c) | 6400 | fork | `s 467(2) the member is within one of the paragraphs`; `s 467(2) the group is ineligible` | 15 | "(other than a small company)" in (c) and "a small company" in (d): decided at this site; case-by-case site S18 (fork register) |
| s 467(2)(ca) | 6401 | encoded | `s 467(2) the member is within one of the paragraphs`; `s 467(2) the group is ineligible` | 15 | "(other than a small company)" in (c) and "a small company" in (d): decided at this site |
| s 467(2)(d) | 6402 | encoded | `s 467(2) the member is within one of the paragraphs`; `s 467(2) the group is ineligible` | 15 | "(other than a small company)" in (c) and "a small company" in (d): decided at this site |
| s 467(2)(e) | 6403 | encoded | `s 467(2) the member is within one of the paragraphs`; `s 467(2) the group is ineligible` | 15 | "(other than a small company)" in (c) and "a small company" in (d): decided at this site |
| s 467(2)(f) | 6404 | encoded | `s 467(2) the member is within one of the paragraphs`; `s 467(2) the group is ineligible` | 15 | "(other than a small company)" in (c) and "a small company" in (d): decided at this site |
| s 467(3) | 6405 | encoded | `s 467(3) the company is a small company for the purposes of subsection (2)` | 3 | the s 382 answer (coa8) is an input |
| s 467(4) | 6406 | encoded | `s 467(4) the section prevents the company from taking advantage of section ...` | 2 | a flat negative |
| heading at line 6407 General power to make further provision about accounts and r | 6407-6444 | inert (reason 1) | - | - | cross-heading "General power to make further provision about accounts and reports" |
| s 468 | 6408-6426 | inert (reason 2) | - | - | the Secretary of State's regulation-making power (further provision about accounts and reports) |
| s 468(1) | 6409-6418 | inert (reason 2) | - | - | the Secretary of State's regulation-making power (further provision about accounts and reports) |
| s 468(1)(a) | 6410 | inert (reason 2) | - | - | the Secretary of State's regulation-making power (further provision about accounts and reports) |
| s 468(1)(b) | 6411 | inert (reason 2) | - | - | the Secretary of State's regulation-making power (further provision about accounts and reports) |
| s 468(1)(c) | 6412 | inert (reason 2) | - | - | the Secretary of State's regulation-making power (further provision about accounts and reports) |
| s 468(1)(d) | 6413-6418 | inert (reason 2) | - | - | the Secretary of State's regulation-making power (further provision about accounts and reports) |
| s 468(1)(d)(i) | 6414 | inert (reason 2) | - | - | the Secretary of State's regulation-making power (further provision about accounts and reports) |
| s 468(1)(d)(ii) | 6415 | inert (reason 2) | - | - | the Secretary of State's regulation-making power (further provision about accounts and reports) |
| s 468(1)(d)(iii) | 6416 | inert (reason 2) | - | - | the Secretary of State's regulation-making power (further provision about accounts and reports) |
| s 468(1)(d)(iv) | 6417 | inert (reason 2) | - | - | the Secretary of State's regulation-making power (further provision about accounts and reports) |
| s 468(1)(d)(v) | 6418 | inert (reason 2) | - | - | the Secretary of State's regulation-making power (further provision about accounts and reports) |
| s 468(2) | 6419 | inert (reason 2) | - | - | the Secretary of State's regulation-making power (further provision about accounts and reports) |
| s 468(3) | 6420-6422 | inert (reason 2) | - | - | the Secretary of State's regulation-making power (further provision about accounts and reports) |
| s 468(3)(a) | 6421 | inert (reason 2) | - | - | the Secretary of State's regulation-making power (further provision about accounts and reports) |
| s 468(3)(b) | 6422 | inert (reason 2) | - | - | the Secretary of State's regulation-making power (further provision about accounts and reports) |
| s 468(4) | 6423-6424 | inert (reason 2) | - | - | the Secretary of State's regulation-making power (further provision about accounts and reports) |
| s 468(5) | 6425-6426 | inert (reason 2) | - | - | the Secretary of State's regulation-making power (further provision about accounts and reports) |
| s 468A | 6427-6444 | inert (reason 2) | - | - | the Secretary of State's regulation-making power (use or disclosure of profit and loss accounts) |
| s 468A(1) | 6428-6432 | inert (reason 2) | - | - | the Secretary of State's regulation-making power (use or disclosure of profit and loss accounts) |
| s 468A(1)(a) | 6429 | inert (reason 2) | - | - | the Secretary of State's regulation-making power (use or disclosure of profit and loss accounts) |
| s 468A(1) item section 443A | 6430 | inert (reason 2) | - | - | the Secretary of State's regulation-making power (use or disclosure of profit and loss accounts) |
| s 468A(1) item section 444 | 6431 | inert (reason 2) | - | - | the Secretary of State's regulation-making power (use or disclosure of profit and loss accounts) |
| s 468A(1)(b) | 6432 | inert (reason 2) | - | - | the Secretary of State's regulation-making power (use or disclosure of profit and loss accounts) |
| s 468A(2) | 6433-6439 | inert (reason 2) | - | - | the Secretary of State's regulation-making power (use or disclosure of profit and loss accounts) |
| s 468A(2)(a) | 6434 | inert (reason 2) | - | - | the Secretary of State's regulation-making power (use or disclosure of profit and loss accounts) |
| s 468A(2)(b) | 6435 | inert (reason 2) | - | - | the Secretary of State's regulation-making power (use or disclosure of profit and loss accounts) |
| s 468A(2)(c) | 6436 | inert (reason 2) | - | - | the Secretary of State's regulation-making power (use or disclosure of profit and loss accounts) |
| s 468A(2)(d) | 6437 | inert (reason 2) | - | - | the Secretary of State's regulation-making power (use or disclosure of profit and loss accounts) |
| s 468A(2)(e) | 6438 | inert (reason 2) | - | - | the Secretary of State's regulation-making power (use or disclosure of profit and loss accounts) |
| s 468A(2)(f) | 6439 | inert (reason 2) | - | - | the Secretary of State's regulation-making power (use or disclosure of profit and loss accounts) |
| s 468A(3) | 6440 | inert (reason 2) | - | - | the Secretary of State's regulation-making power (use or disclosure of profit and loss accounts) |
| s 468A(4) | 6441 | inert (reason 2) | - | - | the Secretary of State's regulation-making power (use or disclosure of profit and loss accounts) |
| s 468A(5) | 6442 | inert (reason 2) | - | - | the Secretary of State's regulation-making power (use or disclosure of profit and loss accounts) |
| s 468A(6) | 6443 | inert (reason 2) | - | - | the Secretary of State's regulation-making power (use or disclosure of profit and loss accounts) |
| s 468A(7) | 6444 | inert (reason 2) | - | - | the Secretary of State's regulation-making power (use or disclosure of profit and loss accounts) |
| heading at line 6445 Other supplementary provisions | 6445-6542 | inert (reason 1) | - | - | cross-heading "Other supplementary provisions" |
| s 469 | 6446-6454 | encoded | `s 469(3) the translation meets the requirements of the section` | 5 | the section title; the operative text is in the rows below |
| s 469(1) | 6447 | encoded | `s 469(1) the amounts may also be shown in the same accounts translated into...` | 2 |  |
| s 469(2) | 6448 | encoded | `s 469(2) the directors may deliver to the registrar an additional copy of t...` | 2 |  |
| s 469(3) | 6449-6451 | fork | `s 469(3) the translation meets the requirements of the section` | 5 | a bare "must" not done: JUST FALSE (case-by-case ruling); case-by-case site S25 (fork register) |
| s 469(3)(a) | 6450 | encoded | `s 469(3) the translation meets the requirements of the section` | 5 | a bare "must" not done: JUST FALSE (case-by-case ruling) |
| s 469(3)(b) | 6451 | encoded | `s 469(3) the translation meets the requirements of the section` | 5 | a bare "must" not done: JUST FALSE (case-by-case ruling) |
| s 469(3A) | 6452 | encoded | `s 469(3A) subsection (3)(b) requires the rate to be disclosed in the notes` | 2 |  |
| s 469(4) | 6453-6454 | encoded | `s 469(4) the additional copy is treated as statutory accounts of the company`; `s 469(4) the references in sections 434 and 435 to the auditor's report are...` | 4 |  |
| s 470 | 6455-6461 | encoded | `s 470(2) the partnership is a banking partnership` | 3 | the section title; the operative text is in the rows below |
| s 470(1) | 6456 | inert (reason 2) | - | - | a regulation-making power of the Secretary of State |
| s 470(2) | 6457-6458 | encoded | `s 470(2) the partnership is a banking partnership` | 3 |  |
| s 470(3) | 6459-6460 | encoded | `s 470(3) the expression has the same meaning as in those provisions` | 2 |  |
| s 470(4) | 6461 | inert (reason 2) | - | - | the parliamentary procedure for regulations |
| s 471 | 6462-6478 | encoded | `s 471(1) the accounts are part of the company's annual accounts` | 4 | the section title; the operative text is in the rows below |
| s 471(1) | 6463-6466 | encoded | `s 471(1) the accounts are part of the company's annual accounts`; `s 471(1) the individual profit and loss account is part of the annual accounts` | 7 | the second sentence ("subject to section 408") is the second function |
| s 471(1)(a) | 6464 | encoded | `s 471(1) the accounts are part of the company's annual accounts`; `s 471(1) the individual profit and loss account is part of the annual accounts` | 7 | the second sentence ("subject to section 408") is the second function |
| s 471(1)(b) | 6465-6466 | encoded | `s 471(1) the accounts are part of the company's annual accounts`; `s 471(1) the individual profit and loss account is part of the annual accounts` | 7 | the second sentence ("subject to section 408") is the second function |
| s 471(2) | 6467-6472 | fork | `s 471(2) the annual accounts and reports of an unquoted company`; `s 471(2) the item is among the annual accounts and reports of the unquoted ...` | 7 | fork F12: a quoted definition read as closed |
| s 471(2)(a) | 6468 | fork | `s 471(2) the annual accounts and reports of an unquoted company`; `s 471(2) the item is among the annual accounts and reports of the unquoted ...` | 7 | fork F12: a quoted definition read as closed |
| s 471(2)(aa) | 6469 | fork | `s 471(2) the annual accounts and reports of an unquoted company`; `s 471(2) the item is among the annual accounts and reports of the unquoted ...` | 7 | fork F12: a quoted definition read as closed |
| s 471(2)(ab) | 6470 | repealed or blank in this text | - | - | the text shows only a row of dots |
| s 471(2)(b) | 6471 | fork | `s 471(2) the annual accounts and reports of an unquoted company`; `s 471(2) the item is among the annual accounts and reports of the unquoted ...` | 7 | fork F12: a quoted definition read as closed |
| s 471(2)(c) | 6472 | fork | `s 471(2) the annual accounts and reports of an unquoted company`; `s 471(2) the item is among the annual accounts and reports of the unquoted ...` | 7 | fork F12: a quoted definition read as closed |
| s 471(3) | 6473-6478 | fork | `s 471(3) the annual accounts and reports of a quoted company`; `s 471(3) the item is among the annual accounts and reports of the quoted co...` | 5 | fork F12: a quoted definition read as closed |
| s 471(3)(a) | 6474 | fork | `s 471(3) the annual accounts and reports of a quoted company`; `s 471(3) the item is among the annual accounts and reports of the quoted co...` | 5 | fork F12: a quoted definition read as closed |
| s 471(3)(b) | 6475 | fork | `s 471(3) the annual accounts and reports of a quoted company`; `s 471(3) the item is among the annual accounts and reports of the quoted co...` | 5 | fork F12: a quoted definition read as closed |
| s 471(3)(ba) | 6476 | fork | `s 471(3) the annual accounts and reports of a quoted company`; `s 471(3) the item is among the annual accounts and reports of the quoted co...` | 5 | fork F12: a quoted definition read as closed |
| s 471(3)(c) | 6477 | fork | `s 471(3) the annual accounts and reports of a quoted company`; `s 471(3) the item is among the annual accounts and reports of the quoted co...` | 5 | fork F12: a quoted definition read as closed |
| s 471(3)(d) | 6478 | fork | `s 471(3) the annual accounts and reports of a quoted company`; `s 471(3) the item is among the annual accounts and reports of the quoted co...` | 5 | fork F12: a quoted definition read as closed |
| s 472 | 6479-6482 | encoded | `s 472(2) the notes are included in a reference to the annual accounts, bala...` | 3 | the section title; the operative text is in the rows below |
| s 472(1) | 6480 | repealed or blank in this text | - | - | the text shows only a row of dots |
| s 472(1A) | 6481 | encoded | `s 472(1A) the notes must be included at the foot of the balance sheet` | 4 |  |
| s 472(2) | 6482 | encoded | `s 472(2) the notes are included in a reference to the annual accounts, bala...` | 3 | "include" |
| s 472A | 6483-6486 | encoded | `s 472A(1) the statement is a corporate governance statement` | 2 | the section title; the operative text is in the rows below |
| s 472A(1) | 6484 | encoded | `s 472A(1) the statement is a corporate governance statement` | 2 | the rules of the FCA sourcebook are not among the sources: an input |
| s 472A(2) | 6485 | inert (reason 1) | - | - | a statement of the history of the rules (when they were inserted and by what instrument): no rule |
| s 472A(3) | 6486 | encoded | `s 472A(3) the statement is a separate corporate governance statement` | 4 |  |
| s 473 | 6487-6504 | inert (reason 2) | - | - | the parliamentary procedure for regulations under this Part |
| s 473(1) | 6488-6497 | inert (reason 2) | - | - | the parliamentary procedure for regulations under this Part |
| s 473(1) item section 396 | 6489 | inert (reason 2) | - | - | the parliamentary procedure for regulations under this Part |
| s 473(1) item section 404 | 6490 | inert (reason 2) | - | - | the parliamentary procedure for regulations under this Part |
| s 473(1) item section 409 | 6491 | inert (reason 2) | - | - | the parliamentary procedure for regulations under this Part |
| s 473(1) item section 412 | 6492 | inert (reason 2) | - | - | the parliamentary procedure for regulations under this Part |
| s 473(1) item section 416 | 6493 | inert (reason 2) | - | - | the parliamentary procedure for regulations under this Part |
| s 473(1) item section 421 | 6494 | inert (reason 2) | - | - | the parliamentary procedure for regulations under this Part |
| s 473(1) item section 444 | 6495 | inert (reason 2) | - | - | the parliamentary procedure for regulations under this Part |
| s 473(1) item section 445 | 6496 | inert (reason 2) | - | - | the parliamentary procedure for regulations under this Part |
| s 473(1) item section 468 | 6497 | inert (reason 2) | - | - | the parliamentary procedure for regulations under this Part |
| s 473(2) | 6498 | inert (reason 2) | - | - | the parliamentary procedure for regulations under this Part |
| s 473(3) | 6499-6503 | inert (reason 2) | - | - | the parliamentary procedure for regulations under this Part |
| s 473(3)(a) | 6500 | inert (reason 2) | - | - | the parliamentary procedure for regulations under this Part |
| s 473(3)(b) | 6501 | inert (reason 2) | - | - | the parliamentary procedure for regulations under this Part |
| s 473(3)(c) | 6502-6503 | inert (reason 2) | - | - | the parliamentary procedure for regulations under this Part |
| s 473(4) | 6504 | inert (reason 2) | - | - | the parliamentary procedure for regulations under this Part |
| s 474 | 6505-6542 | encoded | `s 474(1) the turnover of the company` | 2 | see the terms |
| s 474(1) | 6506-6540 | encoded | `s 474(1) the turnover of the company` | 2 | the lead-in "In this Part" |
| s 474 term e-money issuer | 6507 | encoded | `s 474(1) the person is an e-money issuer` | 3 | borrowed facts, BOOLEAN inputs |
| s 474 term e-money issuer(a) | 6508 | encoded | `s 474(1) the person is an e-money issuer` | 3 | borrowed facts, BOOLEAN inputs |
| s 474 term e-money issuer(b) | 6509 | encoded | `s 474(1) the person is an e-money issuer` | 3 | borrowed facts, BOOLEAN inputs |
| s 474 term group | 6510-6511 | encoded | `s 474(1) the undertaking is a member of the group` | 3 |  |
| s 474 term blank entry after "group" | 6511 | repealed or blank in this text | - | - | the text shows only a row of dots |
| s 474 term included in the consolidation | 6512 | encoded | `s 474(1) the undertaking is included in the consolidation`; `s 474(1) the undertaking is excluded from consolidation` | 4 | the "excluded from consolidation" sentence is the second function |
| s 474 term international accounting standards | 6513 | encoded | `s 474(1) the standards are international accounting standards` | 2 | borrowed fact: Regulation (EC) No 1606/2002 |
| s 474 term micro-entity minimum accounting item | 6514 | encoded | `s 474(1) the item is a micro-entity minimum accounting item` | 4 | the micro-entity answer (ss 384A, 384B, coa8) is an input |
| s 474 term micro-entity provisions | 6515-6516 | encoded | `s 474(1) the provision is one of the micro-entity provisions` | 3 |  |
| s 474 term blank entry after "micro-entity provisions" | 6516 | repealed or blank in this text | - | - | the text shows only a row of dots |
| s 474 term MiFID investment firm | 6517 | fork | `s 474(1) the person is a MiFID investment firm` | 4 | an "(other than X)" site, decided here: within X, JUST FALSE; case-by-case site S15 (fork register) |
| s 474 term MiFID investment firm(a) | 6518 | encoded | `s 474(1) the person is a MiFID investment firm` | 4 | an "(other than X)" site, decided here: within X, JUST FALSE |
| s 474 term MiFID investment firm(b) | 6519 | encoded | `s 474(1) the person is a MiFID investment firm` | 4 | an "(other than X)" site, decided here: within X, JUST FALSE |
| s 474 term profit and loss account | 6520 | encoded | `s 474(1) the statement is included in a reference to a profit and loss account` | 3 | "includes" |
| s 474 term qualified | 6521 | encoded | `s 474(1) the auditor's report is qualified` | 2 |  |
| s 474 term regulated activity | 6522 | fork | `s 474(1) the activity is a regulated activity for the purposes of this Part` | 15 | a table of the excluded kinds, the s 22 answer being an input; case-by-case site S16, S17 (fork register) |
| s 474 term regulated activity(a) | 6523 | encoded | `s 474(1) the activity is a regulated activity for the purposes of this Part` | 15 | a table of the excluded kinds, the s 22 answer being an input |
| s 474 term regulated activity(b) | 6524 | encoded | `s 474(1) the activity is a regulated activity for the purposes of this Part` | 15 | a table of the excluded kinds, the s 22 answer being an input |
| s 474 term regulated activity(c) | 6525 | encoded | `s 474(1) the activity is a regulated activity for the purposes of this Part` | 15 | a table of the excluded kinds, the s 22 answer being an input |
| s 474 term regulated activity(ca) | 6526 | encoded | `s 474(1) the activity is a regulated activity for the purposes of this Part` | 15 | a table of the excluded kinds, the s 22 answer being an input |
| s 474 term regulated activity(d) | 6527 | encoded | `s 474(1) the activity is a regulated activity for the purposes of this Part` | 15 | a table of the excluded kinds, the s 22 answer being an input |
| s 474 term regulated activity(e) | 6528 | encoded | `s 474(1) the activity is a regulated activity for the purposes of this Part` | 15 | a table of the excluded kinds, the s 22 answer being an input |
| s 474 term regulated activity(f) | 6529 | encoded | `s 474(1) the activity is a regulated activity for the purposes of this Part` | 15 | a table of the excluded kinds, the s 22 answer being an input |
| s 474 term regulated activity(g) | 6530 | encoded | `s 474(1) the activity is a regulated activity for the purposes of this Part` | 15 | a table of the excluded kinds, the s 22 answer being an input |
| s 474 term regulated activity(ga) | 6531 | encoded | `s 474(1) the activity is a regulated activity for the purposes of this Part` | 15 | a table of the excluded kinds, the s 22 answer being an input |
| s 474 term regulated activity(h) | 6532 | encoded | `s 474(1) the activity is a regulated activity for the purposes of this Part` | 15 | a table of the excluded kinds, the s 22 answer being an input |
| s 474 term regulated activity(i) | 6533 | encoded | `s 474(1) the activity is a regulated activity for the purposes of this Part` | 15 | a table of the excluded kinds, the s 22 answer being an input |
| s 474 term traded company | 6534 | encoded | `s 474(1) the company is a traded company` | 3 |  |
| s 474 term turnover | 6535 | encoded | `s 474(1) the turnover of the company` | 2 |  |
| s 474 term turnover(a) | 6536 | encoded | `s 474(1) the turnover of the company` | 2 |  |
| s 474 term turnover(b) | 6537 | encoded | `s 474(1) the turnover of the company` | 2 |  |
| s 474 term turnover(c) | 6538 | encoded | `s 474(1) the turnover of the company` | 2 |  |
| s 474 term UCITS management company | 6539 | encoded | `s 474(1) the company is a UCITS management company` | 3 | the Glossary's answer, passed through |
| s 474 term UK-adopted international accounting standards | 6540 | encoded | `s 474(1) the standards are UK-adopted international accounting standards` | 2 |  |
| s 474(2) | 6541-6542 | encoded | `s 474(2) the reference to a profit and loss account is to an income and exp...`; `s 474(2) the reference to a consolidated profit and loss account is to a co...` | 4 |  |

## Fork register (coa10)

A fork is a place where the text can be read two or more ways with different outcomes.
F1 to F17 are the readings of the text, F18 to F26 are the grants the name-test sweep of 2026-11-12 moved to NOTHING; S1 to S25 are the sites where the maintainer ruled (typed 2026-11-05T10:25:24Z) that the encoder decides case by case and gives each site one fork line.
The coverage table points each `fork` row at its F or S number.

### F1 to F26

| id | provision | the text and what it licenses | the reading taken, and the other readings | the rule that encodes the reading taken |
| --- | --- | --- | --- | --- |
| F1 | s 444, s 445(7), s 446(5), s 451(4) | The file prints two texts of s 444 (lines 5949-5982 and 5983-5993), of s 445(7) (6019-6021 and 6022-6024), of s 446(5) (6039-6042 and 6043-6046), and runs two daily default fines together in s 451(4) (line 6128: "one-tenth of level 5 on the standard scale" then "one-tenth of the greater of £5,000 or level 4 on the standard scale"). SOURCES.md says of the file: "revised text; may carry more than one extent version of a provision, and prospective provisions, which CLML marks but this text does not distinguish". | TAKEN: neither text is preferred; the caller says which one is in force, as the input `s 441 text of the sections the file prints twice` (`s 441 first text in the file` or `s 441 second text in the file`), and every rule that differs between them has one function per text. OTHER: the later text is the one in force; the earlier text is; the two are merged. The text does not say which. | `s 444(1) what section 444 requires of the directors for the document`; `s 445(1) section 445 applies to the company`; `s 446(1) section 446 applies to the company`; `s 451(4) the greatest daily default fine in pounds` |
| F2 | s 441(1), s 443A, s 444 (first text) | In the first text, s 444(1) describes a company "subject to the small companies regime" and has no sentence excluding companies within s 443A, so a company that is a micro-entity and is also subject to the small companies regime (the answers of ss 384A and 381, coa8's) is described by both s 443A(1) and the first-text s 444(1). The second text adds s 444(6), "This section does not apply to companies within section 443A". | TAKEN: when more than one section applies, or none, the dispatcher answers NOTHING ("the text does not say which governs"). OTHER: s 443A governs because it is the more specific; s 444 governs because it is the earlier. | `s 441(1) the filing section that applies to the company` |
| F3 | s 442(3) | "If the relevant accounting reference period is the company's first and is a period of more than twelve months, the period is— (a) nine months or six months, as the case may be, from the first anniversary of the incorporation of the company, or (b) three months after the end of the accounting reference period, whichever last expires." The text does not say how "more than twelve months" or "first anniversary" is counted. | TAKEN: "more than twelve months" means the period ends on or after the day twelve calendar months after it began (15 January 2025 to 14 January 2026 is twelve months and no more); "first anniversary" is the same day and month one year on (library `add years`, which for a 29 February incorporation date is the library's own rule); the nine or six months are then counted by s 443. OTHER: count in days (365 or 366); count the period from the day after it began. | `s 442(3) the relevant accounting reference period is a period of more than twelve months`; `s 442(3) the period for filing ends on for a first accounting reference period of more than twelve months` |
| F4 | s 442(5), s 442(5A) | "on an application made before the expiry of the period otherwise allowed" and "Any such extension must not have the effect of extending the period for filing to more than twelve months after the end of the relevant accounting reference period." The text does not say whether an application made on the last day is "before the expiry", nor what a notice that exceeds the limit achieves. | TAKEN: the period expires at the end of its last day (s 443(2): "the period ends with the date"), so an application made on or before that date is in time; an application after it is NOTHING (limited by its own wording); an extension past the s 442(5A) limit is answered "does not comply" and the period for filing it would give is NOTHING (the text says what the extension must not do, not what it does). OTHER: "before the expiry" excludes the last day; an over-limit notice extends to the limit. | `s 442(5) the Secretary of State may extend the period for filing`; `s 442(5A) the extension complies with the limit of twelve months after the end of the accounting reference period`; `s 442(1) the period for filing ends on` |
| F5 | s 451(1) | "every person who immediately before the end of that period was a director of the company commits an offence." The text names who commits the offence and is silent about anyone else. | TAKEN: a person who was not a director immediately before the end of the period is NOTHING (limited by its own wording). OTHER: JUST FALSE, because the text names the offenders. | `s 451(1) the person commits an offence` |
| F6 | s 452(1)(b) | "fail to make good the default within 14 days after the service of a notice on them requiring compliance". The text does not say whether the day of service is day 1. | TAKEN: the last day is the day of service plus 14 (the day of service is not counted). OTHER: the day of service is day 1, so the last day is one earlier. | `s 452(1)(b) the directors failed to make good the default within 14 days after the service of the notice` |
| F7 | s 454(2), s 455(1)(b) | "sent out to members, delivered to the registrar or (in the case of a public company) laid before the company in general meeting" (s 454(2); s 455(1)(b) has the same parenthesis). The parenthesis could qualify the last item only or all three. | TAKEN: it qualifies only "laid before the company in general meeting", the item it follows (a private company does not lay accounts before a general meeting). OTHER: it qualifies all three items. | `s 454(2) the revisions are confined to correction and consequential alterations`; `s 455(1) section 455 applies` |
| F8 | s 465(4) | "For a period that is a company's financial year but not in fact a year the maximum figures for turnover must be proportionately adjusted." The text does not say by what measure. | TAKEN: in months (12 months is a year), and only the turnover figure is adjusted, as the text says. OTHER: in days. | `s 465(4) the maximum figure for turnover for the financial year` |
| F9 | s 448B (and so s 448A(1)) | The text shows s 448B as paragraphs (b) and (c) only (lines 6101-6105): the lead-in and paragraph (a) are missing. The parallel s 394B (lines 5077-5085, another part's range) has a full list that includes "a traded company"; it was not borrowed. | TAKEN: s 448B answers JUST TRUE for a company within (b) or (c) and otherwise NOTHING (the list cannot be taken as closed); so s 448A(1) is NOTHING for a company whose other conditions are met and that is within neither. OTHER: JUST FALSE for a company within neither; or add a paragraph (a) from s 394B. | `s 448B the company is excluded from the dormant subsidiaries exemption`; `s 448A(1) the directors of the dormant subsidiary are not required to deliver a copy of the individual accounts` |
| F10 | s 455(3) | "a period of not less than one month". The text gives no rule for counting this month (s 443 counts the months of s 442 only). | TAKEN: calendar months by the library `add months` (the clamping rule). OTHER: s 443's rule for a last-day date; thirty days. | `s 455(3) the period the notice specifies is not less than one month` |
| F11 | s 455(4) | "it appears to the Secretary of State that the directors have not— (a) given a satisfactory explanation of the accounts or report, or (b) revised the accounts or report so as to comply". | TAKEN: "have not (a) ... or (b)" means that they have done neither (the Secretary of State may apply to the court only if neither was done). OTHER: they have done at least one of them not (the Secretary of State may apply if either was not done). | `s 455(4) the Secretary of State may apply to the court` |
| F12 | s 471(2), s 471(3) | "In the case of an unquoted company, its “annual accounts and reports” for a financial year are— (a) ... (c) ...": a definition by a list of items, not closed with "only". | TAKEN: read as closed: an item not in the list is not among the annual accounts and reports (JUST FALSE), because the sentence is a definition ("are"). OTHER: NOTHING for an item not in the list. | `s 471(2) the item is among the annual accounts and reports of the unquoted company`; `s 471(3) the item is among the annual accounts and reports of the quoted company` |
| F13 | s 463(1) | "The reports and statements to which this section applies are— (za) the strategic report, (a) the directors' report, (b) the directors' remuneration report, and (c) ... (d) any separate corporate governance statement." The list is not closed with "only". | TAKEN: a report or statement not in the list is NOTHING (list not closed). OTHER: JUST FALSE. | `s 463(1) the section applies to the report or statement` |
| F14 | s 459(3) | "Those persons are— (a) the company; (b) any officer, employee, or auditor of the company; (c) any persons who fell within paragraph (b) at a time to which the document or information required by the authorised person relates." Not closed with "only". | TAKEN: another person is NOTHING. OTHER: JUST FALSE. | `s 459(3) the person is one whom the authorised person may require` |
| F15 | s 456(1) | "An application may be made to the court— (a) by the Secretary of State, after having complied with section 455, or (b) by a person authorised by the Secretary of State". Not closed with "only". | TAKEN: another person, and the Secretary of State who has not complied with s 455, are NOTHING. OTHER: JUST FALSE. | `s 456(1) the applicant may apply to the court for a declaration and an order` |
| F16 | s 461(3), s 461(4) | Lists of recipients (s 461(3)(a) to (f)) and of purposes (s 461(4)(a) to (h)) to which "It does not apply to disclosure to/for". Not closed with "only". | TAKEN: a recipient or purpose not listed is NOTHING. OTHER: JUST FALSE (the prohibition in s 460 then applies). | `s 461(3) the prohibition in section 460 does not apply to disclosure to the recipient`; `s 461(4) the prohibition in section 460 does not apply to disclosure for the purpose` |
| F17 | s 463(3) | "(2) A director of a company is liable to compensate the company for any loss suffered by it as a result of— (a) any untrue or misleading statement ..., or (b) the omission ... (3) He is so liable only if— (a) he knew the statement to be untrue or misleading or was reckless ..., or (b) he knew the omission to be dishonest concealment of a material fact." The text does not say whether (3)(a) goes with (2)(a) and (3)(b) with (2)(b). | TAKEN: either limb of (3) suffices for either kind of loss. OTHER: (3)(a) for a loss caused by a statement and (3)(b) for a loss caused by an omission. | `s 463(2) the director is liable to compensate the company for the loss` |
| F18 | s 442(5) | "Subject to subsection (5A), if for any special reason the Secretary of State thinks fit he may, on an application made before the expiry of the period otherwise allowed, by notice in writing to a company extend that period" (line 5923). | Name-test sweep of 2026-11-12. TAKEN: a failed "If" gate on a grant named "may" is NOTHING (the text limits a grant in its own wording, and the case falls outside the limit; the text does not close the gate with "only if"). OTHER: JUST FALSE, a failed "if" read as the text's own no (marginal reading (a)). Case: no special reason. | `s 442(5) the Secretary of State may extend the period for filing` |
| F19 | s 452(1) | "If— (a) the requirements of section 441 ... are not complied with ... before the end of the period for filing ..., and (b) the directors of the company fail to make good the default within 14 days after the service of a notice on them requiring compliance, the court may, on the application of any member or creditor of the company or of the registrar, make an order" (lines 6130-6133). | Name-test sweep of 2026-11-12. TAKEN: a failed "If" gate on a grant named "may" is NOTHING (the text limits a grant in its own wording, and the case falls outside the limit; the text does not close the gate with "only if"). OTHER: JUST FALSE, a failed "if" read as the text's own no (marginal reading (a)). Cases: the requirements were complied with in time; the default was made good within the 14 days. | `s 452(1) the court may order the directors to make good the default` |
| F20 | s 454(1) | "If it appears to the directors of a company that— (a) the company's annual accounts, (b) the directors' remuneration report or the directors' report, or (c) a strategic report of the company, did not comply with the requirements of this Act ..., they may prepare revised accounts or a revised report or statement." (lines 6148-6152). | Name-test sweep of 2026-11-12. TAKEN: a failed "If" gate on a grant named "may" is NOTHING (the text limits a grant in its own wording, and the case falls outside the limit; the text does not close the gate with "only if"). OTHER: JUST FALSE, a failed "if" read as the text's own no (marginal reading (a)). Case: it does not appear to the directors that the document did not comply. | `s 454(1) the directors may prepare revised accounts or a revised report or statement` |
| F21 | s 456(3) | "If the court orders the preparation of revised accounts, it may give directions as to—" (line 6190). | Name-test sweep of 2026-11-12. TAKEN: a failed "If" gate on a grant named "may" is NOTHING (the text limits a grant in its own wording, and the case falls outside the limit; the text does not close the gate with "only if"). OTHER: JUST FALSE, a failed "if" read as the text's own no (marginal reading (a)). Case: the court has not ordered revised accounts. | `s 456(3) the court may give the direction` |
| F22 | s 456(4) | "If the court orders the preparation of a revised strategic report or directors' report it may give directions as to—" (line 6195). | Name-test sweep of 2026-11-12. TAKEN: a failed "If" gate on a grant named "may" is NOTHING (the text limits a grant in its own wording, and the case falls outside the limit; the text does not close the gate with "only if"). OTHER: JUST FALSE, a failed "if" read as the text's own no (marginal reading (a)). Case: the court has not ordered a revised strategic report or directors' report. | `s 456(4) the court may give the direction` |
| F23 | s 456(5) | "If the court finds that the accounts or report did not comply with the requirements of this Act ... it may order that all or part of— (a) the costs ... of and incidental to the application, and (b) any reasonable expenses incurred by the company ..., are to be borne by such of the directors as were party to the approval of the defective accounts or report." (lines 6200-6203). | Name-test sweep of 2026-11-12. TAKEN: a failed "If" gate on a grant named "may" is NOTHING (the text limits a grant in its own wording, and the case falls outside the limit; the text does not close the gate with "only if"). OTHER: JUST FALSE, a failed "if" read as the text's own no (marginal reading (a)). Case: the court has not found that the accounts or report did not comply. | `s 456(5) the court may order that the director bear the costs and expenses` |
| F24 | s 457(4) | "If the authorised person is an unincorporated association, proceedings brought in, or in connection with, the exercise of any function by the association as an authorised person may be brought by or against the association in the name of a body corporate whose constitution provides for the establishment of the association." (line 6215). | Name-test sweep of 2026-11-12. TAKEN: a failed "If" gate on a grant named "may" is NOTHING (the text limits a grant in its own wording, and the case falls outside the limit; the text does not close the gate with "only if"). OTHER: JUST FALSE, a failed "if" read as the text's own no (marginal reading (a)). Case: the authorised person is not an unincorporated association. | `s 457(4) the proceedings may be brought by or against the association in the name of the body corporate` |
| F25 | s 459(4) | "If a person fails to comply with such a requirement, the authorised person may apply to the court." (line 6255). | Name-test sweep of 2026-11-12. TAKEN: a failed "If" gate on a grant named "may" is NOTHING (the text limits a grant in its own wording, and the case falls outside the limit; the text does not close the gate with "only if"). OTHER: JUST FALSE, a failed "if" read as the text's own no (marginal reading (a)). Case: the person has not failed to comply. | `s 459(4) the authorised person may apply to the court` |
| F26 | s 459(5) | "If it appears to the court that the person has failed to comply with a requirement under subsection (2), it may order the person to take such steps as it directs" (line 6256). | Name-test sweep of 2026-11-12. TAKEN: a failed "If" gate on a grant named "may" is NOTHING (the text limits a grant in its own wording, and the case falls outside the limit; the text does not close the gate with "only if"). OTHER: JUST FALSE, a failed "if" read as the text's own no (marginal reading (a)). Case: it does not appear to the court that the person has failed to comply. | `s 459(5) the court may order the person to take such steps as it directs` |

### S1 to S25: the case-by-case sites

Each row gives the function, the words of the text, the answer taken and the other reading.
For "unless" and "except" sites the answer taken is JUST FALSE for the grant, bar or offence once the exception is met, because the text states the exception in its own words.
For "bare must" and "shall" sites the answer taken is JUST FALSE when the thing the provision requires is not done, so that "the copy states who signed it" is JUST FALSE when it does not; the other reading is NOTHING (the text does not say what follows).
For "(other than X)" sites the answer taken is JUST FALSE for a person within X; the other reading is NOTHING.

| id | module and line | function | the site | answer taken | the other reading |
| --- | --- | --- | --- | --- | --- |
| S1 | coa10-disclosure.l4:77 | `s 458(3)(a) the section bars the use of the information` | an "except" met: "may not be used except in or in connection with— (i) taking steps to discover whether there are grounds ..., or (ii) deciding whether or not to mak..." | JUST FALSE | NOTHING |
| S2 | coa10-disclosure.l4:89 | `s 458(3)(b) the section bars the further disclosure of the information` | an "except" met: "must not be further disclosed except— (i) to the person to whom the information relates, or (ii) in, or in connection with, proceedings on any such..." | JUST FALSE | NOTHING |
| S3 | coa10-disclosure.l4:104 | `s 458(4) the person commits an offence` | an "unless" met: "commits an offence unless— (a) he did not know, and had no reason to suspect, that the information had been disclosed under this section, or (b) he..." | JUST FALSE | NOTHING |
| S4 | coa10-disclosure.l4:317 | `s 460(4) the person commits an offence` | an "unless" met: "commits an offence, unless— (a) he did not know, and had no reason to suspect, that the information had been disclosed under section 459, or (b) he..." | JUST FALSE | NOTHING |
| S5 | coa10-disclosure.l4:466 | `s 461(6) the authorised person has had regard to the considerations the section names` | a bare "must" not done: "the authorised person must have regard to the following considerations" | JUST FALSE | NOTHING |
| S6 | coa10-exemptions.l4:301 | `s 448C(2) the statement meets the requirements of the section` | a bare "must" not done: "The statement under subsection (1) must be authenticated by the parent undertaking and must specify" | JUST FALSE | NOTHING |
| S7 | coa10-exemptions.l4:348 | `s 448A(2)(c) the company is included in consolidated accounts drawn up as the paragraph requires` | a bare "must" not done: "the company must be included in the consolidated accounts drawn up for that year or to an earlier date in that year by the parent undertaking in ac..." | JUST FALSE | NOTHING |
| S8 | coa10-exemptions.l4:375 | `s 448A(2)(e) the directors have delivered the documents within the period for filing` | a bare "must" not done: "the directors of the company must deliver to the registrar within the period for filing the company's accounts and reports for that year" | JUST FALSE | NOTHING |
| S9 | coa10-filing.l4:622 | `s 443A(3) the copy of a document the section names meets the requirement to state who signed it` | a bare "must" not done: "must state the name of the person who signed it on behalf of the board" | JUST FALSE | NOTHING |
| S10 | coa10-filing.l4:723 | `s 443A(4) the copy of the auditor's report states what the section requires` | a bare "must" not done: "The copy of the auditor's report delivered to the registrar under this section must— (a) state the name of the auditor ... or (b) if the conditions..." | JUST FALSE | NOTHING |
| S11 | coa10-filing.l4:835 | `s 444(3) the copies delivered are copies of the company's annual accounts and reports` | a bare "must" not done: "the copies of accounts and reports delivered to the registrar must be copies of the company's annual accounts and reports" | JUST FALSE | NOTHING |
| S12 | coa10-filing.l4:867 | `s 444(5) the copy of the balance sheet contains the statement the section requires` | a bare "must" not done: "the copy of the balance sheet delivered to the registrar must contain in a prominent position a statement" | JUST FALSE | NOTHING |
| S13 | coa10-filing.l4:904 | `s 444(5A)(b) the section requires the notes to the balance sheet to satisfy the requirements in subsection (5B)` | an "unless" met: "unless the company is exempt from audit and the directors have taken advantage of that exemption" | JUST FALSE | NOTHING |
| S14 | coa10-filing.l4:928 | `s 444(5B) the notes to the balance sheet satisfy the requirements` | a bare "must" not done: "Those requirements are that the notes to the balance sheet must— (a) state whether the auditor's report was qualified or unqualified, (b) where tha..." | JUST FALSE | NOTHING |
| S15 | coa10-meaning.l4:291 | `s 474(1) the person is a MiFID investment firm` | "(other than X)": "“MiFID investment firm” means an investment firm within the meaning of Article 2.1A of Regulation (EU) No. 600/2014 ..., other than— (a) a company ..." | JUST FALSE | NOTHING |
| S16 | coa10-meaning.l4:363 | `s 474(1) the activity is a regulated activity for the purposes of this Part` | an "except" met: "except that it does not include activities of the kind specified in ... (h) article 21 (dealing as agent), article 25 (arranging deals in investmen..." | JUST FALSE | NOTHING |
| S17 | coa10-meaning.l4:365 | `s 474(1) the activity is a regulated activity for the purposes of this Part` | an "except" met: "except that it does not include activities of the kind specified in any of the following provisions of the Financial Services and Markets Act 2000 ..." | JUST FALSE | NOTHING |
| S18 | coa10-medium.l4:344 | `s 467(2) the member is within one of the paragraphs` | "(other than X)": "(c) a person (other than a small company) who has permission under Part 4A of the Financial Services and Markets Act 2000 to carry on a regulated a..." | JUST FALSE | NOTHING |
| S19 | coa10-revision.l4:76 | `s 454(2) the revision is within the limit the section sets` | a bare "must" not done: "the revisions must be confined to— (a) the correction of those respects in which the previous accounts or report did not comply with the requiremen..." | JUST FALSE | NOTHING |
| S20 | coa10-revision.l4:120 | `s 455(3) the period the notice specifies is not less than one month` | a bare "must" not done: "The notice must specify a period of not less than one month" | JUST FALSE | NOTHING |
| S21 | coa10-revision.l4:203 | `s 456(2) the applicant has given the registrar the notice the section requires` | a bare "shall" not done: "Notice of the application, together with a general statement of the matters at issue in the proceedings, shall be given by the applicant to the reg..." | JUST FALSE | NOTHING |
| S22 | coa10-revision.l4:277 | `s 456(5) the director is taken to have been a party to the approval of the defective accounts or report` | an "unless" met: "unless he shows that he took all reasonable steps to prevent that approval" | JUST FALSE | NOTHING |
| S23 | coa10-revision.l4:356 | `s 456(7) the applicant has complied` | a bare "must" not done: "the applicant must send to the registrar for registration a copy of the court order" | JUST FALSE | NOTHING |
| S24 | coa10-revision.l4:360 | `s 456(7) the applicant has complied` | a bare "must" not done: "give notice to the registrar that the application has failed or been withdrawn" | JUST FALSE | NOTHING |
| S25 | coa10-supplementary.l4:149 | `s 469(3) the translation meets the requirements of the section` | a bare "must" not done: "In both cases— (a) the amounts must have been translated at the exchange rate prevailing on the date to which the balance sheet is made up, and (b)..." | JUST FALSE | NOTHING |

### Name-test sweep of 2026-11-12

The sweep covers every layer-1 function of this part whose name contains "may", "permitted", "power", "entitled" or "authorised": 25 functions.
A function named for a grant that answered JUST FALSE because an "If" gate failed now answers NOTHING, with one fork line each (F18 to F26 above, and in the marginal readings below); the other reading is JUST FALSE.
The text closing the gate itself ("only if", a flat negative) keeps JUST FALSE; "where", "when" and "upon" gates and "entitled"-named functions are listed, not flipped (assumed, not ruled).

| flipped to NOTHING | kept JUST FALSE (gate closed by the text) | listed: "may" with where/when/upon | listed: "entitled" |
| --- | --- | --- | --- |
| 9 | 4 | 4 | 0 |

Flipped to NOTHING (JUST FALSE before; the assertions this changed are restated in place with `-- RECONCILED 2026-11-12` in the `coa10-tests-*` files and in `coa10-cases-seat.l4`):
- `s 442(5) the Secretary of State may extend the period for filing` (F18)
- `s 452(1) the court may order the directors to make good the default` (F19)
- `s 454(1) the directors may prepare revised accounts or a revised report or statement` (F20)
- `s 456(3) the court may give the direction` (F21)
- `s 456(4) the court may give the direction` (F22)
- `s 456(5) the court may order that the director bear the costs and expenses` (F23)
- `s 457(4) the proceedings may be brought by or against the association in the name of the body corporate` (F24)
- `s 459(4) the authorised person may apply to the court` (F25)
- `s 459(5) the court may order the person to take such steps as it directs` (F26)

Kept JUST FALSE, the text closing the gate itself (the fork register does not list these; they are not the error):
- `s 458(1) the Commissioners may disclose the information to the authorised person`: the JUST FALSE branch is the data-protection proviso, "information is not to be disclosed in contravention of the data protection legislation" (line 6225): a flat negative.
- `s 459(6) the statement may be used in evidence against the person who made it`: the text says "may not be used in evidence against him in any criminal proceedings" (line 6257): a flat negative.
- `s 461(1) the disclosure is permitted by section 461`: its JUST FALSE branch is s 461(7), "Nothing in this section authorises the making of a disclosure in contravention of the data protection legislation" (line 6315): a flat negative.
- `s 461(7) the section authorises the disclosure`: "Nothing in this section authorises" (line 6315): a flat negative.

Listed, not flipped: "may" functions whose gate is "where", "when" or "upon" or an equivalent (assumed, not ruled, that these equivalents go with the listed group).
Ruling (b) of the periods ruling says JUST FALSE for a failed "where" and the Guide's line on grants points the other way; that is a question for the maintainer or a lawyer, so the answers are left as they were.

| function | gate, and the other reading |
| --- | --- |
| `s 459(2) the authorised person may require the person to produce the document or provide the information or explanation` | "This section applies where it appears to a person who is authorised under section 457 ..." (s 459(1), line 6247): a "where" gate; answers JUST FALSE when s 459(1) does not apply. The other reading: NOTHING (the Guide's line on grants). |
| `s 455(4) the Secretary of State may apply to the court` | "If at the end of the specified period, or such longer period as the Secretary of State may allow, it appears ..." (lines 6178-6181): the gate is anchored to the end of a period ("at the end of"), so it is listed with the "when/upon" group; answers JUST FALSE before the period ends and when an explanation was given or the accounts revised. The other reading: NOTHING. |
| `s 456(6) the court may exclude one or more directors from the order or order the payment of different amounts` | "Where the court makes an order under subsection (5) it shall have regard ... and may exclude ..." (line 6205): a "where" gate; answers JUST FALSE when no order was made. The other reading: NOTHING. |
| `s 469(2) the directors may deliver to the registrar an additional copy of the annual accounts translated into euros` | "When complying with section 441 ..., the directors of a company may deliver" (line 6448): a "when" gate; it already answers NOTHING when the directors are not complying (not JUST FALSE), so no answer was changed. The other reading: JUST FALSE (ruling (b) of the periods ruling). |

Listed, not flipped: "entitled"-named functions (an entitlement is a claim, not a power, and the Guide does not settle it): 0.

Not named for a grant or a power although the name contains a keyword (a duty, a bar or the provision's own question), JUST FALSE kept:
- `s 461(6) the authorised person has had regard to the considerations the section names`: a duty ("must have regard"), not a grant: JUST FALSE kept (case-by-case site S5).

Named for a grant and already answering NOTHING where the gate fails (no answer changed):
- `s 452(2) the court's order may provide that all the costs are borne by the directors`
- `s 453(3) the registrar may recover the penalty from the company`
- `s 455(2) the Secretary of State may give notice to the directors indicating the respects in which a question arises`
- `s 456(1) the applicant may apply to the court for a declaration and an order`
- `s 459(3) the person is one whom the authorised person may require`
- `s 448C(3)(b) the person may enforce the guarantee against the parent undertaking`
- `s 469(1) the amounts may also be shown in the same accounts translated into euros`

Outside the sweep: named "it is lawful": 0.

Callers checked: none of the nine flipped functions is called by another layer-1 function; each is called only by its seat question (s 442(5), s 452(1), s 454(1), s 456(5), s 457(4), s 459(4)) or by its tests (s 456(3), s 456(4), s 459(5)), and the seat cases and tests that read the changed answer are restated.

## Jural relations (coa10)

One row per provision (or group of provisions that create the same relation) of lines 5895-6542, in the text's order.
Hohfeld's correlatives: a claim and a duty, a privilege and a no-right, a power and a liability, an immunity and a disability.
A provision that creates no relation (a definition, a counting rule, a condition of another provision, a blank) is listed as `none`.
Layer 1 states each relation once, as a rule between two parties, and never again from the other side.
The parties are named as the text names them; "the State" stands for prosecution under an offence section, where the text names no prosecutor.

| provision | holder (claim, privilege, power or immunity) | bearer (duty, no-right, liability or disability) | kind | the L4 rule |
| --- | --- | --- | --- | --- |
| s 441(1) | the registrar | the directors of the company | claim / duty | `s 441(1) the directors' duty to deliver the accounts and reports`; `s 441(1) the filing section that applies to the company` |
| s 441(2) | the registrar (the privilege of the exempt directors of ss 448 and 448A is the correlative of their no-right) | the directors of the company | claim / duty | `s 441(2) the directors must deliver the accounts and reports for the financial year` |
| s 442(1) to (4), (6), (7) | none: counting rules, which fix when the duty of s 441 falls due | - | none | `s 442(1) the period for filing ends on` |
| s 442(5) | the Secretary of State (power to extend the period) | the company and its directors (liability to a longer period) | power / liability | `s 442(5) the Secretary of State may extend the period for filing` |
| s 442(5A) | the company and its directors (immunity from an extension beyond twelve months) | the Secretary of State (disability) | immunity / disability | `s 442(5A) the extension complies with the limit of twelve months after the end of the accounting reference period` |
| s 443 | none: a counting rule | - | none | `s 443(2) the period ends with` |
| s 443A(1), (2) | the registrar (claim to the annual accounts and the auditor's report); the directors (privilege to deliver the directors' report, "may", and, where exempt from audit, no duty as to the auditor's report) | the directors of a micro-entity (duty); the registrar (no-right as to the directors' report) | claim / duty; privilege / no-right | `s 443A(1) what section 443A requires of the directors for the document` |
| s 443A(3) | the registrar | the directors of a micro-entity | claim / duty (the copy states who signed it) | `s 443A(3) the copy meets the requirement to state who signed it` |
| s 443A(4), (5) | the registrar | the directors of a micro-entity | claim / duty (the copy of the auditor's report states the name or the s 506 resolution) | `s 443A(4) the copy of the auditor's report states what the section requires` |
| s 444(1), (2), (2A) (first and second text) | the registrar; the directors (privilege, "may", for the profit and loss account and directors' report in the first text) | the directors of a company subject to the small companies regime; the registrar (no-right) | claim / duty; privilege / no-right | `s 444(1) what section 444 requires of the directors for the document` |
| s 444(3) (first text) | the registrar | the directors | claim / duty (the copies are copies of the annual accounts and reports) | `s 444(3) the copies delivered are copies of the company's annual accounts and reports` |
| s 444(3A), (3B), (4) (first text) | none: blank in this text | - | none | none |
| s 444(5), (5A), (5B), (5C) (first text) | the registrar | the directors | claim / duty (the balance sheet carries the statement; the notes disclose the auditor's report) | `s 444(5) the section requires the copy of the balance sheet to contain the statement`; `s 444(5B) the notes to the balance sheet satisfy the requirements`; `s 444(5C) subsection (5A) applies to the company` |
| s 444(6), (7), (8) (first text); s 444(3), (4), (5) (second text) | the registrar | the directors | claim / duty (who signed; the auditor's report) | `s 444(6) the copy meets the requirement to state who signed it`; `s 444(7) the copy of the auditor's report states what the section requires` |
| s 444(6) (second text) | none: the section does not apply to companies within s 443A (the duty of s 443A stands) | - | none | `s 444(6) the company is within a section that excludes it from section 444` |
| s 444A(1), (2) | the registrar; the directors (privilege, "may", for the directors' report) | the directors; the registrar (no-right) | claim / duty; privilege / no-right | `s 444A(1) what section 444A requires of the directors for the document` |
| s 444A(3), (4), (4A) | the registrar | the directors | claim / duty (who signed; the auditor's report) | `s 444A(3) the copy meets the requirement to state who signed it`; `s 444A(4) the copy of the auditor's report states what the section requires` |
| s 444A(5) | none: the section does not apply to companies within s 444 | - | none | `s 444A(5) the company is within a section that excludes it from section 444A` |
| s 445(1), (2) | the registrar | the directors of a medium-sized company | claim / duty | `s 445(1) what section 445 requires of the directors for the document` |
| s 445(3), (4) | none: blank in this text | - | none | none |
| s 445(5), (6), (6A) | the registrar | the directors | claim / duty (who signed; the auditor's report) | `s 445(5) the copy meets the requirement to state who signed it`; `s 445(6) the copy of the auditor's report states what the section requires` |
| s 445(7) (both texts) | none: the section does not apply to companies within the sections it names | - | none | `s 445(7) the company is within a section that excludes it from section 445` |
| s 446(1), (2) | the registrar | the directors of an unquoted company | claim / duty | `s 446(1) what section 446 requires of the directors for the document` |
| s 446(3), (4), (4A) | the registrar | the directors | claim / duty (who signed; the auditor's report) | `s 446(3) the copy meets the requirement to state who signed it`; `s 446(4) the copy of the auditor's report states what the section requires` |
| s 446(5) (both texts) | none: the section does not apply to companies within the sections it names | - | none | `s 446(5) the company is within a section that excludes it from section 446` |
| s 447(1), (2) | the registrar | the directors of a quoted company | claim / duty | `s 447(1) what section 447 requires of the directors for the document` |
| s 447(3), (4), (5) | the registrar | the directors | claim / duty (who signed; the auditor's report) | `s 447(3) the copy meets the requirement to state who signed it`; `s 447(4) the copy of the auditor's report states what the section requires` |
| s 448(1) | the directors of an unlimited company (privilege: no duty to deliver) | the registrar (no-right) | privilege / no-right | `s 448(1) the directors of the unlimited company are not required to deliver accounts and reports` |
| s 448(2), (3) | none: the conditions of the privilege of s 448(1) and the limits that bar it | - | none | `s 448(2) the conditions are met`; `s 448(3) the section bars the exemption` |
| s 448(4), (5) | none: a substitution of words in ss 434 and 435, and definitions | - | none | `s 448(4)(a) the words substituted in section 434(3)`; `s 448(5) the person is a general partner` |
| s 448A(1) | the directors of a dormant subsidiary (privilege: no duty to deliver the individual accounts) | the registrar (no-right) | privilege / no-right | `s 448A(1) the directors of the dormant subsidiary are not required to deliver a copy of the individual accounts` |
| s 448A(2)(a) to (d) | none: conditions of the privilege of s 448A(1) | - | none | `s 448A(2) the conditions for the exemption are complied with` |
| s 448A(2)(e) | the registrar | the directors of the dormant subsidiary | claim / duty (five documents within the period for filing) | `s 448A(2)(e) the directors' duty to deliver the documents`; `s 448A(2)(e) the directors have delivered the documents within the period for filing` |
| s 448B | none: the companies excluded from the privilege of s 448A | - | none | `s 448B the company is excluded from the dormant subsidiaries exemption` |
| s 448C(1), (2) | none: when a guarantee is given and what its statement must say | - | none | `s 448C(1) a guarantee is given by the parent undertaking`; `s 448C(2) the statement meets the requirements of the section` |
| s 448C(3)(a) | the persons to whom the subsidiary is liable (claim) | the parent undertaking (duty to guarantee the outstanding liabilities) | claim / duty | `s 448C(3)(a) the amount of the outstanding liabilities that the parent undertaking still guarantees` |
| s 448C(3)(b) | any person to whom the subsidiary company is liable (power to enforce) | the parent undertaking (liability) | power / liability | `s 448C(3)(b) the person may enforce the guarantee against the parent undertaking` |
| s 449, s 450 | none: blank in this text | - | none | none |
| s 451(1) | the State (power to prosecute; the duty broken is that of s 441) | a director immediately before the end of the period (liability to conviction) | power / liability | `s 451(1) the person commits an offence` |
| s 451(2) | the charged director (immunity: a defence) | the prosecution (disability) | immunity / disability | `s 451(2) this section gives the person a defence on these facts` |
| s 451(3) | none: the text withholds a defence, so it creates no immunity | - | none | `s 451(3) proving that the documents were not prepared as required is a defence to the offence` |
| s 451(4) | the State (power to fine, and to fine daily for continued contravention) | the person guilty of the offence (liability) | power / liability | `s 451(4) the person is guilty of an offence under section 451`; `s 451(4) the greatest fine on summary conviction in pounds`; `s 451(4) the greatest daily default fine in pounds` |
| s 452(1) | any member or creditor of the company, or the registrar (power to apply); the court (power to order) | the directors (liability to the order) | power / liability | `s 452(1) the court may order the directors to make good the default` |
| s 452(2) | the court (power over the costs) | the directors (liability for the costs) | power / liability | `s 452(2) the court's order may provide that all the costs are borne by the directors` |
| s 453(1) | the registrar (claim to the civil penalty) | the company (duty / liability to a civil penalty) | claim / duty | `s 453(1) the company is liable to a civil penalty` |
| s 453(2) | none: the amount is fixed by regulations outside the sources | - | none | `s 453(2) the amount of the civil penalty`; `s 453(2)(a) the number of days between the end of the period for filing and the day on which the requirements are complied with` |
| s 453(3) | the registrar (power to recover the penalty) | the company (liability) | power / liability | `s 453(3) the registrar may recover the penalty from the company` |
| s 453(4) | none: the text withholds a defence | - | none | `s 453(4) proving that the documents were not prepared as required is a defence to the civil penalty` |
| s 453(5) | none: procedure for the regulations (machinery) | - | none | none |
| s 454(1) | the directors (privilege to prepare revised accounts or a revised report) | everyone else (no-right to unrevised accounts) | privilege / no-right | `s 454(1) the directors may prepare revised accounts or a revised report or statement` |
| s 454(2) | the members and the registrar who hold copies | the directors (duty to confine the revisions) | claim / duty | `s 454(2) the revision is within the limit the section sets` |
| s 454(3), (4), (5) | the Secretary of State (power to make regulations) | companies (liability) | power / liability (machinery, inert) | none |
| s 455(1) | none: when the section applies | - | none | `s 455(1) section 455 applies` |
| s 455(2) | the Secretary of State (power to give notice) | the directors (liability to a notice) | power / liability | `s 455(2) the Secretary of State may give notice to the directors indicating the respects in which a question arises` |
| s 455(3) | the directors (claim to a period of at least one month) | the Secretary of State (duty) | claim / duty | `s 455(3) the period the notice specifies is not less than one month` |
| s 455(4) | the Secretary of State (power to apply to the court) | the directors (liability) | power / liability | `s 455(4) the Secretary of State may apply to the court` |
| s 455(5) | none: the section applies equally to revised documents | - | none | `s 455(5) section 455 applies equally to the revised document` |
| s 456(1) | the Secretary of State, or a person authorised by the Secretary of State (power to apply to the court) | the company and its directors (liability) | power / liability | `s 456(1) the applicant may apply to the court for a declaration and an order` |
| s 456(2) | the registrar (claim to notice of the application) | the applicant (duty) | claim / duty | `s 456(2) the applicant has given the registrar the notice the section requires` |
| s 456(3), (4) | the court (power to give directions) | the directors (liability) | power / liability | `s 456(3) the court may give the direction` |
| s 456(5) | the court (power to order costs); the director who shows reasonable steps (immunity from the presumption) | the directors party to the approval (liability); the applicant (disability as to a director who shows them) | power / liability; immunity / disability | `s 456(5) the court may order that the director bear the costs and expenses`; `s 456(5) the director is taken to have been a party to the approval of the defective accounts or report` |
| s 456(6) | the court (power to exclude or vary) | the directors (liability) | power / liability | `s 456(6) the court may exclude one or more directors from the order or order the payment of different amounts` |
| s 456(7) | the registrar (claim to the order or the notice) | the applicant (duty) | claim / duty | `s 456(7) the applicant's duty to inform the registrar`; `s 456(7) the applicant has complied` |
| s 456(8) | none: the section applies equally to revised documents | - | none | `s 456(8) section 456 applies equally to the revised document` |
| s 457(1) to (3), (5) to (7) | the Secretary of State (power to authorise persons by order) | the persons authorised and companies (liability) | power / liability (machinery, inert) | none |
| s 457(4) | an unincorporated association authorised under s 457 (power to sue and be sued in the name of a body corporate) | the other party to the proceedings (liability to be sued so) | power / liability | `s 457(4) the proceedings may be brought by or against the association in the name of the body corporate` |
| s 458(1) | Her Majesty's Revenue and Customs (privilege to disclose to an authorised person) | the person the information concerns (no-right) | privilege / no-right | `s 458(1) the Commissioners may disclose the information to the authorised person` |
| s 458(2) | Her Majesty's Revenue and Customs (immunity from other restrictions on disclosure) | anyone who would rely on such a restriction (disability) | immunity / disability | `s 458(2) a statutory or other restriction bars the disclosure under this section` |
| s 458(3) | the person to whom the information relates (claim to its limited use and disclosure) | the authorised person (duty) | claim / duty | `s 458(3)(a) the section bars the use of the information`; `s 458(3)(b) the section bars the further disclosure of the information` |
| s 458(4), (5) | the State (power to prosecute and punish) | the person who contravenes subsection (3) (liability) | power / liability | `s 458(4) the person commits an offence`; `s 458(5) the penalty for the offence` |
| s 458(6) | the State (power to prosecute the officer in default) | the officer of the body corporate, including a person who purports to act as one and a shadow director (liability) | power / liability | `s 458(6) the person is treated as an officer of the body` |
| s 459(1), (3), (8) | none: when the section applies, who may be required, and what a document is | - | none | `s 459(1) section 459 applies`; `s 459(3) the person is one whom the authorised person may require`; `s 459(8) the thing is a document for the purposes of section 459` |
| s 459(2) | the authorised person (power to require documents, information and explanations) | the company, its officers, employees and auditors and former ones (liability) | power / liability | `s 459(2) the authorised person may require the person to produce the document or provide the information or explanation` |
| s 459(4) | the authorised person (power to apply to the court) | the person who fails to comply (liability) | power / liability | `s 459(4) the authorised person may apply to the court` |
| s 459(5) | the court (power to order steps) | the person who has failed to comply (liability) | power / liability | `s 459(5) the court may order the person to take such steps as it directs` |
| s 459(6) | the person who made the statement (immunity from its use in criminal proceedings) | the prosecution (disability) | immunity / disability | `s 459(6) the statement may be used in evidence against the person who made it` |
| s 459(7) | a person with a claim to legal professional privilege (immunity) | the authorised person (disability) | immunity / disability | `s 459(7) the section compels the person to disclose the document or information` |
| s 460(1) to (3) | the individual or business the information concerns (claim to confidentiality) | whoever holds the information (duty not to disclose without consent) | claim / duty | `s 460(1) the information is within section 460`; `s 460(2) the section bars the disclosure of the information` |
| s 460(4), (5) | the State (power to prosecute and punish) | the person who discloses in contravention (liability) | power / liability | `s 460(4) the person commits an offence`; `s 460(5) the penalty for the offence` |
| s 460(6) | the State (power to prosecute the officer in default) | the officer of the body corporate (liability) | power / liability | `s 460(6) the person is treated as an officer of the body` |
| s 461(1) to (5) | the authorised person (privilege to disclose to the listed recipients and for the listed purposes) | the individual or business concerned (no-right) | privilege / no-right | `s 461(1) the disclosure is permitted by section 461`; `s 461(2) the prohibition in section 460 does not apply to the disclosure`; `s 461(3) the prohibition in section 460 does not apply to disclosure to the recipient`; `s 461(4) the prohibition in section 460 does not apply to disclosure for the purpose`; `s 461(5) the prohibition in section 460 does not apply to disclosure to the overseas body` |
| s 461(6) | the individual or business concerned (claim to the authorised person's regard to the considerations) | the authorised person (duty) | claim / duty | `s 461(6) the authorised person has had regard to the considerations the section names` |
| s 461(7) | none: a saving of the data protection legislation | - | none | `s 461(7) the section authorises the disclosure` |
| s 462 | the Secretary of State (power to amend s 461(3) to (5)) | those affected (liability) | power / liability (machinery, inert) | none |
| s 463(1) | none: which reports and statements the section applies to | - | none | `s 463(1) the section applies to the report or statement` |
| s 463(2), (3) | the company (claim to compensation for loss) | the director (duty to compensate, only if he knew or was reckless) | claim / duty | `s 463(2) the director is liable to compensate the company for the loss` |
| s 463(4) | any person (immunity from liability to someone other than the company for reliance on the report or statement) | persons other than the company (disability) | immunity / disability | `s 463(4) a person is subject to liability to the claimant` |
| s 463(5), (6) | none: what "liability" includes, and a saving of civil penalties and criminal offences | - | none | `s 463(5) the claim is within the liability that subsection (4) removes`; `s 463(6) the section affects the liability` |
| s 464(1), (2) | none: definitions | - | none | `s 464(1) the statement is an accounting standard`; `s 464(2) the accounting standard is applicable to the company's annual accounts` |
| s 464(3) | the Secretary of State (power to make regulations) | companies (liability) | power / liability (machinery, inert) | none |
| s 465(1) to (7) | none: when a company qualifies as medium-sized (counting and defining rules) | - | none | `s 465(7) the company qualifies as medium-sized, subject to section 466`; `s 465(3) the qualifying conditions are met`; `s 465(4) the maximum figure for turnover for the financial year`; `s 465(5) the balance sheet total`; `s 465(6) the number of employees` |
| s 466(1) to (7) | none: when a parent company and its group qualify as medium-sized | - | none | `s 466(1) the parent company qualifies as a medium-sized company`; `s 466(4) the qualifying conditions are met by the group`; `s 466(7) the end of the subsidiary undertaking's financial year whose figures are used` |
| s 467(1) | the registrar and the public (privilege to require the full filing) | a public company, a regulated or insurance-market company, a Master Trust scheme funder, an e-money issuer, or a member of an ineligible group (no-right to the medium-sized provisions) | privilege / no-right | `s 467(1) the section bars the company from taking advantage of the medium-sized provisions` |
| s 467(2), (3) | none: what an ineligible group is and what a small company is | - | none | `s 467(2) the group is ineligible`; `s 467(3) the company is a small company for the purposes of subsection (2)` |
| s 467(4) | the company (immunity: membership of an ineligible group alone does not bar s 417(7)) | those who would bar it (disability) | immunity / disability | `s 467(4) the section prevents the company from taking advantage of section 417(7)` |
| s 468, s 468A | the Secretary of State (power to make regulations) | companies and the registrar (liability) | power / liability (machinery, inert) | none |
| s 469(1) | the company (privilege to show the amounts in euros as well) | readers of the accounts (no-right) | privilege / no-right | `s 469(1) the amounts may also be shown in the same accounts translated into euros` |
| s 469(2) | the directors (privilege to deliver a euro copy) | the registrar (no-right) | privilege / no-right | `s 469(2) the directors may deliver to the registrar an additional copy of the annual accounts translated into euros` |
| s 469(3), (3A) | the registrar and readers (claim to translation at the balance sheet date rate, disclosed in the notes) | the directors (duty) | claim / duty | `s 469(3) the translation meets the requirements of the section`; `s 469(3A) subsection (3)(b) requires the rate to be disclosed in the notes` |
| s 469(4) | none: the copy is treated as statutory accounts for ss 434 and 435 | - | none | `s 469(4) the additional copy is treated as statutory accounts of the company` |
| s 470(1), (4) | the Secretary of State (power to apply the Part to banking partnerships) | banking partnerships (liability) | power / liability (machinery, inert) | none |
| s 470(2), (3) | none: definitions | - | none | `s 470(2) the partnership is a banking partnership`; `s 470(3) the expression has the same meaning as in those provisions` |
| s 471 | none: definitions | - | none | `s 471(1) the accounts are part of the company's annual accounts`; `s 471(2) the item is among the annual accounts and reports of the unquoted company`; `s 471(3) the item is among the annual accounts and reports of the quoted company` |
| s 472(1A) | the registrar and readers (claim that the notes of a micro-entity are at the foot of the balance sheet) | the directors (duty) | claim / duty | `s 472(1A) the notes must be included at the foot of the balance sheet` |
| s 472(1), (2) | none: blank (1); (2) a definition by "include" | - | none | `s 472(2) the notes are included in a reference to the annual accounts, balance sheet or profit and loss account` |
| s 472A | none: definitions | - | none | `s 472A(1) the statement is a corporate governance statement`; `s 472A(3) the statement is a separate corporate governance statement` |
| s 473 | the Secretary of State (the procedure for regulations) | Parliament (machinery, inert) | none | none |
| s 474 | none: definitions | - | none | `s 474(1) the turnover of the company`; `s 474(1) the company is a traded company`; `s 474(1) the person is a MiFID investment firm`; `s 474(1) the activity is a regulated activity for the purposes of this Part`; `s 474(2) the reference to a profit and loss account is to an income and expenditure account` |

## Marginal readings for a lawyer (coa10)

The brief asks every branch that rests on one of two readings to be listed, with the other reading stated.
- Reading (a): a failed "if" counts as the text's no, clause by clause within the provision that holds the "if", and a flat negative counts as the text saying no. The other reading: NOTHING (an "if A then B" does not itself say "if not A then not B").
- Reading (b): a prohibition or grant limited by its own wording does not give a no outside its limit. The other reading: JUST FALSE.
Every branch tagged `FALSE-kind` in layer 1 rests on reading (a) unless its tag says it rests on a ruling (a "where", a period, a defence) or on a definition ("means"); every branch tagged `NOTHING-kind (limited by its own wording)` rests on reading (b).
The two tables below are generated by `work/sites.py` from the tags in the modules, so they list every such branch (127 and 78).

The name-test sweep of 2026-11-12 moved nine grants named "may" from JUST FALSE to NOTHING when an "If" gate fails; each is one fork line (F18 to F26 above) and the other reading is JUST FALSE, a failed "if" read as the text's own no (reading (a)):
- F18 `s 442(5) the Secretary of State may extend the period for filing` (no special reason).
- F19 `s 452(1) the court may order the directors to make good the default` (requirements complied with in time; default made good within 14 days).
- F20 `s 454(1) the directors may prepare revised accounts or a revised report or statement` (it does not appear to the directors that the document did not comply).
- F21 `s 456(3) the court may give the direction` (the court has not ordered revised accounts).
- F22 `s 456(4) the court may give the direction` (the court has not ordered a revised strategic report or directors' report).
- F23 `s 456(5) the court may order that the director bear the costs and expenses` (the court has not found non-compliance).
- F24 `s 457(4) the proceedings may be brought by or against the association in the name of the body corporate` (the authorised person is not an unincorporated association).
- F25 `s 459(4) the authorised person may apply to the court` (the person has not failed to comply).
- F26 `s 459(5) the court may order the person to take such steps as it directs` (it does not appear to the court that the person has failed to comply).

One further reading the tags do not show:
- `s 454(2) the revision is within the limit the section sets` answers NOTHING when the confinement does not apply (no copy has gone out), while `s 454(2) the revisions are confined to correction and consequential alterations` answers JUST FALSE there (ruling on "where"). Another reading of the derived question: JUST TRUE (there is no limit to exceed).

### Branches resting on reading (a): FALSE-kind

| module and line | function | tag | quoted words |
| --- | --- | --- | --- |
| coa10-default.l4:14 | `` | FALSE-kind (the text says no in its own words) | "<the words>"`); NOTHING = the text does not decide |
| coa10-default.l4:32 | `s 451(1) the person commits an offence` | FALSE-kind (the text says no in its own words, an "If" not met) | "If the requirements of section 441 (duty to file accounts and reports) are not complied with ... before th... |
| coa10-default.l4:48 | `s 451(2) this section gives the person a defence on these facts` | FALSE-kind (ruling of 2026-11-05, a defence not proved) | "It is a defence for a person charged with such an offence to prove that he took all reasonable steps for s... |
| coa10-default.l4:56 | `s 451(3) proving that the documents were not prepared as required is a defenc...` | FALSE-kind (the text says no in its own words) | "It is not a defence to prove that the documents in question were not in fact prepared as required by this ... |
| coa10-default.l4:69 | `s 451(4) the person is guilty of an offence under section 451` | FALSE-kind (the text says no in its own words) | no offence under s 451(1) is committed, so no person is guilty of one |
| coa10-default.l4:72 | `s 451(4) the person is guilty of an offence under section 451` | FALSE-kind (the text says no in its own words) | "It is a defence for a person charged with such an offence to prove that he took all reasonable steps" |
| coa10-default.l4:136 | `s 452(1)(b) the directors failed to make good the default within 14 days afte...` | FALSE-kind (a period fixed in the text's own words, ruling of 2026-11-05) | "fail to make good the default within 14 days after the service of a notice on them requiring compliance" |
| coa10-default.l4:184 | `s 453(1) the company is liable to a civil penalty` | FALSE-kind (a "where" not met, ruling of 2026-11-05) | "Where the requirements of section 441 are not complied with in relation to a company's accounts and report... |
| coa10-default.l4:247 | `s 453(4) proving that the documents were not prepared as required is a defenc...` | FALSE-kind (the text says no in its own words) | "It is not a defence in proceedings under this section to prove that the documents in question were not in ... |
| coa10-disclosure.l4:15 | `` | FALSE-kind (the text says no in its own words) | "<the words>"`); NOTHING = the text does not decide |
| coa10-disclosure.l4:37 | `s 458(1) the Commissioners may disclose the information to the authorised person` | FALSE-kind (the text says no in its own words) | "in the case of personal data within the meaning of Parts 5 to 7 of the Data Protection Act 2018 ..., infor... |
| coa10-disclosure.l4:49 | `s 458(2) a statutory or other restriction bars the disclosure under this section` | FALSE-kind (the text says no in its own words) | "This section applies despite any statutory or other restriction on the disclosure of information." |
| coa10-disclosure.l4:77 | `s 458(3)(a) the section bars the use of the information` | FALSE-kind (the text says no in its own words, an "except" met, ruling of 2026-11-05) | "may not be used except in or in connection with— (i) taking steps to discover whether there are grounds ..... |
| coa10-disclosure.l4:89 | `s 458(3)(b) the section bars the further disclosure of the information` | FALSE-kind (the text says no in its own words, an "except" met, ruling of 2026-11-05) | "must not be further disclosed except— (i) to the person to whom the information relates, or (ii) in, or in... |
| coa10-disclosure.l4:104 | `s 458(4) the person commits an offence` | FALSE-kind (the text says no in its own words, an "unless" met, ruling of 2026-11-05) | "commits an offence unless— (a) he did not know, and had no reason to suspect, that the information had bee... |
| coa10-disclosure.l4:153 | `s 458(6) the officer of the body corporate also commits the offence` | FALSE-kind (a "where" not met, ruling of 2026-11-05) | "Where an offence under this section is committed by a body corporate, every officer of the body who is in ... |
| coa10-disclosure.l4:174 | `s 459(1) section 459 applies` | FALSE-kind (a "where" not met, ruling of 2026-11-05) | "This section applies where it appears to a person who is authorised under section 457 that there is, or ma... |
| coa10-disclosure.l4:209 | `s 459(2) the authorised person may require the person to produce the document...` | FALSE-kind (a "where" not met, ruling of 2026-11-05) | "This section applies where it appears to a person who is authorised under section 457" |
| coa10-disclosure.l4:241 | `s 459(6) the statement may be used in evidence against the person who made it` | FALSE-kind (the text says no in its own words) | "A statement made by a person in response to a requirement under subsection (2) or an order under subsectio... |
| coa10-disclosure.l4:250 | `s 459(7) the section compels the person to disclose the document or information` | FALSE-kind (the text says no in its own words) | "Nothing in this section compels any person to disclose documents or information in respect of which a clai... |
| coa10-disclosure.l4:296 | `s 460(2) the section bars the disclosure of the information` | FALSE-kind (the text says no in its own words) | "This does not apply— ... (b) to the disclosure of information that is or has been available to the public ... |
| coa10-disclosure.l4:298 | `s 460(2) the section bars the disclosure of the information` | FALSE-kind (the text says no in its own words) | "This does not apply— (a) to disclosure permitted by section 461" |
| coa10-disclosure.l4:317 | `s 460(4) the person commits an offence` | FALSE-kind (the text says no in its own words, an "unless" met, ruling of 2026-11-05) | "commits an offence, unless— (a) he did not know, and had no reason to suspect, that the information had be... |
| coa10-disclosure.l4:466 | `s 461(6) the authorised person has had regard to the considerations the secti...` | FALSE-kind (a bare "must" not done, decided at this site, ruling of 2026-11-05) | "the authorised person must have regard to the following considerations" |
| coa10-disclosure.l4:475 | `s 461(7) the section authorises the disclosure` | FALSE-kind (the text says no in its own words) | "Nothing in this section authorises the making of a disclosure in contravention of the data protection legi... |
| coa10-disclosure.l4:488 | `s 461(1) the disclosure is permitted by section 461` | FALSE-kind (the text says no in its own words) | "Nothing in this section authorises the making of a disclosure in contravention of the data protection legi... |
| coa10-exemptions.l4:17 | `` | FALSE-kind (the text says no in its own words) | "<the words>"`); NOTHING = the text does not decide |
| coa10-exemptions.l4:32 | `s 448(2) the undertaking was limited at that time` | FALSE-kind (the text says no in its own words) | "are to an undertaking (under whatever law established) the liability of whose members is at that time limi... |
| coa10-exemptions.l4:41 | `s 448(2)(a) the condition is met` | FALSE-kind (the text says no in its own words) | "The conditions are that at no time during the relevant accounting reference period— (a) has the company be... |
| coa10-exemptions.l4:51 | `s 448(2)(b) the condition is met` | FALSE-kind (the text says no in its own words) | "(b) have there been, to its knowledge, exercisable by or on behalf of two or more undertakings which were ... |
| coa10-exemptions.l4:61 | `s 448(2)(c) the condition is met` | FALSE-kind (the text says no in its own words) | "(c) has the company been a parent company of an undertaking which was then limited" |
| coa10-exemptions.l4:117 | `s 448(3)(b) each of the members of the company is of a kind that paragraph (b...` | FALSE-kind (the text says no in its own words, an "if" not met) | "does not apply if— ... (b) each of the members of the company is— (i) a limited company ..." |
| coa10-exemptions.l4:160 | `s 448(1) the directors of the unlimited company are not required to deliver a...` | FALSE-kind (the text says no in its own words) | "The exemption conferred by this section does not apply if" |
| coa10-exemptions.l4:164 | `s 448(1) the directors of the unlimited company are not required to deliver a...` | FALSE-kind (the text says no in its own words, an "if" not met) | "are not required to deliver accounts and reports in respect of a financial year if the following condition... |
| coa10-exemptions.l4:168 | `s 448(1) the directors of the unlimited company are not required to deliver a...` | FALSE-kind (the text says no in its own words, an "if" not met) | "are not required to deliver accounts and reports in respect of a financial year if the following condition... |
| coa10-exemptions.l4:206 | `s 448(5) the person is a general partner` | FALSE-kind (the text says no in its own words) | "“general partner” means— (a) in relation to a Scottish partnership which is a limited partnership, a perso... |
| coa10-exemptions.l4:215 | `s 448(5) the partnership is a limited partnership` | FALSE-kind (the text says no in its own words) | "“limited partnership” means a partnership registered under the Limited Partnerships Act 1907" |
| coa10-exemptions.l4:224 | `s 448(5) the accounting reference period is the relevant accounting reference...` | FALSE-kind (the text says no in its own words) | "the “relevant accounting reference period”, in relation to a financial year, means the accounting referenc... |
| coa10-exemptions.l4:276 | `s 448C(1) a guarantee is given by the parent undertaking` | FALSE-kind (a "when" read as a "where", ruling of 2026-11-05) | "A guarantee is given by a parent undertaking under this section when the directors of the subsidiary compa... |
| coa10-exemptions.l4:301 | `s 448C(2) the statement meets the requirements of the section` | FALSE-kind (a bare "must" not done, decided at this site, ruling of 2026-11-05) | "The statement under subsection (1) must be authenticated by the parent undertaking and must specify" |
| coa10-exemptions.l4:348 | `s 448A(2)(c) the company is included in consolidated accounts drawn up as the...` | FALSE-kind (a bare "must" not done, decided at this site, ruling of 2026-11-05) | "the company must be included in the consolidated accounts drawn up for that year or to an earlier date in ... |
| coa10-exemptions.l4:375 | `s 448A(2)(e) the directors have delivered the documents within the period for...` | FALSE-kind (a bare "must" not done, and a period fixed in the text's own words, rulings of 2026-11-05) | "the directors of the company must deliver to the registrar within the period for filing the company's acco... |
| coa10-exemptions.l4:426 | `s 448A(1) the directors of the dormant subsidiary are not required to deliver...` | FALSE-kind (the text says no in its own words, an "if" not met) | "are not required to deliver a copy of the company's individual accounts to the registrar in respect of a f... |
| coa10-exemptions.l4:428 | `s 448A(1) the directors of the dormant subsidiary are not required to deliver...` | FALSE-kind (the text says no in its own words, the heading of s 448B) | "Companies excluded from the dormant subsidiaries exemption" |
| coa10-exemptions.l4:432 | `s 448A(1) the directors of the dormant subsidiary are not required to deliver...` | FALSE-kind (the text says no in its own words) | "Exemption is conditional upon compliance with all of the following conditions" |
| coa10-filing.l4:17 | `` | FALSE-kind (the text says no in its own words) | "<the words>"`. |
| coa10-filing.l4:156 | `s 441(1) a filing section applies given its description and its exclusions` | FALSE-kind (the text says no in its own words) | "This section does not apply to companies within ..." (s 444(6) in the second text, s 444A(5), s 445(7), s ... |
| coa10-filing.l4:389 | `s 441(2) the directors must deliver the accounts and reports for the financia...` | FALSE-kind (the text says no in its own words) | "The directors of an unlimited company are not required to deliver accounts and reports" (s 448(1)); "The d... |
| coa10-filing.l4:415 | `s 443A(1) what section 443A requires of the directors for the document` | FALSE-kind (the text says no in its own words) | "This does not apply if the company is exempt from audit and the directors have taken advantage of that exe... |
| coa10-filing.l4:439 | `s 444(1) what the first text of section 444 requires of the directors for the...` | FALSE-kind (a "where" not met, ruling of 2026-11-05) | "Where the directors deliver to the registrar a copy of the company's profit and loss account under subsect... |
| coa10-filing.l4:441 | `s 444(1) what the first text of section 444 requires of the directors for the...` | FALSE-kind (the text says no in its own words) | "This does not apply if the company is exempt from audit and the directors have taken advantage of that exe... |
| coa10-filing.l4:446 | `s 444(1) what the first text of section 444 requires of the directors for the...` | FALSE-kind (a "where" not met, ruling of 2026-11-05) | "Where the balance sheet or profit and loss account is abridged pursuant to paragraph 1A of Schedule 1" |
| coa10-filing.l4:464 | `s 444(1) what the second text of section 444 requires of the directors for th...` | FALSE-kind (the text says no in its own words) | "This does not apply if the company is exempt from audit and the directors have taken advantage of that exe... |
| coa10-filing.l4:506 | `s 444A(1) what section 444A requires of the directors for the document` | FALSE-kind (the text says no in its own words) | "This does not apply if the company is exempt from audit and the directors have taken advantage of that exc... |
| coa10-filing.l4:527 | `s 445(1) what section 445 requires of the directors for the document` | FALSE-kind (the text says no in its own words) | "This does not apply if the company is exempt from audit and the directors have taken advantage of that exe... |
| coa10-filing.l4:554 | `s 446(1) what section 446 requires of the directors for the document` | FALSE-kind (the text says no in its own words) | "This does not apply if the company is exempt from audit and the directors have taken advantage of that exe... |
| coa10-filing.l4:622 | `s 443A(3) the copy of a document the section names meets the requirement to s...` | FALSE-kind (the text says no in its own words) | "must state the name of the person who signed it on behalf of the board" |
| coa10-filing.l4:698 | `s 443A(5) the reference to the name of the auditor is a reference to the name...` | FALSE-kind (the text says no in its own words, an "If" not met) | "If more than one person is appointed as auditor, the reference ... is to be read as a reference to the nam... |
| coa10-filing.l4:723 | `s 443A(4) the copy of the auditor's report states what the section requires` | FALSE-kind (the text says no in its own words) | "The copy of the auditor's report delivered to the registrar under this section must— (a) state the name of... |
| coa10-filing.l4:835 | `s 444(3) the copies delivered are copies of the company's annual accounts and...` | FALSE-kind (a bare "must" not done, decided at this site, ruling of 2026-11-05) | "the copies of accounts and reports delivered to the registrar must be copies of the company's annual accou... |
| coa10-filing.l4:852 | `s 444(5) the section requires the copy of the balance sheet to contain the st...` | FALSE-kind (a "where" not met, ruling of 2026-11-05) | "Where the directors of a company subject to the small companies regime ... (a) do not deliver ... a copy o... |
| coa10-filing.l4:867 | `s 444(5) the copy of the balance sheet contains the statement the section req...` | FALSE-kind (the text says no in its own words) | "the copy of the balance sheet delivered to the registrar must contain in a prominent position a statement" |
| coa10-filing.l4:882 | `s 444(5C) subsection (5A) applies to the company` | FALSE-kind (a "where" not met, ruling of 2026-11-05) | "where the directors of a company subject to the small companies regime do not deliver to the registrar a c... |
| coa10-filing.l4:884 | `s 444(5C) subsection (5A) applies to the company` | FALSE-kind (the text says no in its own words) | "Subsection (5A) does not apply in relation to a company if— (a) the company qualifies as a micro-entity ..... |
| coa10-filing.l4:904 | `s 444(5A)(b) the section requires the notes to the balance sheet to satisfy t...` | FALSE-kind (the text says no in its own words, an "unless" met, ruling of 2026-11-05) | "unless the company is exempt from audit and the directors have taken advantage of that exemption" |
| coa10-filing.l4:928 | `s 444(5B) the notes to the balance sheet satisfy the requirements` | FALSE-kind (the text says no in its own words) | "Those requirements are that the notes to the balance sheet must— (a) state whether the auditor's report wa... |
| coa10-filing.l4:964 | `s 441(1) the requirements were complied with before the end of the period for...` | FALSE-kind (a period fixed in the text's own words, ruling of 2026-11-05) | "before the end of the period for filing" |
| coa10-filing.l4:967 | `s 441(1) the requirements were complied with before the end of the period for...` | FALSE-kind (a period fixed in the text's own words, ruling of 2026-11-05) | "are not complied with ... before the end of the period for filing" |
| coa10-meaning.l4:15 | `` | FALSE-kind (the text says no in its own words) | "<the words>"`); NOTHING = the text does not decide |
| coa10-meaning.l4:32 | `s 464(1) the statement is an accounting standard` | FALSE-kind (the text says no in its own words) | "“accounting standards” means statements of standard accounting practice issued by such body or bodies as m... |
| coa10-meaning.l4:43 | `s 464(2) the accounting standard is applicable to the company's annual accounts` | FALSE-kind (the text says no in its own words) | "References in this Part to accounting standards applicable to a company's annual accounts are to such stan... |
| coa10-meaning.l4:60 | `s 471(1) the accounts are part of the company's annual accounts` | FALSE-kind (the text says no in its own words) | "In this Part a company's “annual accounts”, in relation to a financial year, means— (a) any individual acc... |
| coa10-meaning.l4:71 | `s 471(1) the individual profit and loss account is part of the annual accounts` | FALSE-kind (the text says no in its own words) | "This is subject to section 408 (option to omit individual profit and loss account from annual accounts whe... |
| coa10-meaning.l4:113 | `s 471(2) the item is among the annual accounts and reports of the unquoted co...` | FALSE-kind (the text says no in its own words, a quoted definition read as closed, fork F12) | "its “annual accounts and reports” for a financial year are— (a) its annual accounts, (aa) the strategic re... |
| coa10-meaning.l4:144 | `s 471(3) the item is among the annual accounts and reports of the quoted company` | FALSE-kind (the text says no in its own words, a quoted definition read as closed, fork F12) | "its “annual accounts and reports” for a financial year are— (a) its annual accounts, (b) the directors' re... |
| coa10-meaning.l4:185 | `s 472A(1) the statement is a corporate governance statement` | FALSE-kind (the text says no in its own words) | "“corporate governance statement” means the statement required by rules 7.2.1 to 7.2.11 in the Disclosure R... |
| coa10-meaning.l4:196 | `s 472A(3) the statement is a separate corporate governance statement` | FALSE-kind (the text says no in its own words) | "A “separate” corporate governance statement means one that is not included in the directors' report." |
| coa10-meaning.l4:215 | `s 474(1) the person is an e-money issuer` | FALSE-kind (the text says no in its own words) | "“e-money issuer” means— (a) an electronic money institution, within the meaning of the Electronic Money Re... |
| coa10-meaning.l4:225 | `s 474(1) the undertaking is a member of the group` | FALSE-kind (the text says no in its own words) | "“group” means a parent undertaking and its subsidiary undertakings" |
| coa10-meaning.l4:234 | `s 474(1) the undertaking is included in the consolidation` | FALSE-kind (the text says no in its own words) | "“included in the consolidation”, in relation to group accounts, ... means that the undertaking is included... |
| coa10-meaning.l4:243 | `s 474(1) the undertaking is excluded from consolidation` | FALSE-kind (the text says no in its own words) | "references to an undertaking excluded from consolidation shall be construed accordingly" |
| coa10-meaning.l4:253 | `s 474(1) the standards are international accounting standards` | FALSE-kind (the text says no in its own words) | "“international accounting standards” means the international accounting standards, within the meaning of A... |
| coa10-meaning.l4:262 | `s 474(1) the item is a micro-entity minimum accounting item` | FALSE-kind (the text says no in its own words) | "“micro-entity minimum accounting item” means an item of information required by this Part or by regulation... |
| coa10-meaning.l4:273 | `s 474(1) the provision is one of the micro-entity provisions` | FALSE-kind (the text says no in its own words) | "“micro-entity provisions” means any provisions of this Part, Part 16 or regulations under this Part relati... |
| coa10-meaning.l4:291 | `s 474(1) the person is a MiFID investment firm` | FALSE-kind (the text says no in its own words, an "other than" site decided here) | "“MiFID investment firm” means an investment firm within the meaning of Article 2.1A of Regulation (EU) No.... |
| coa10-meaning.l4:309 | `s 474(1) the auditor's report is qualified` | FALSE-kind (the text says no in its own words) | "“qualified”, in relation to an auditor's report, means that the report does not state the auditor's unqual... |
| coa10-meaning.l4:363 | `s 474(1) the activity is a regulated activity for the purposes of this Part` | FALSE-kind (the text says no in its own words) | "except that it does not include activities of the kind specified in ... (h) article 21 (dealing as agent),... |
| coa10-meaning.l4:365 | `s 474(1) the activity is a regulated activity for the purposes of this Part` | FALSE-kind (the text says no in its own words) | "except that it does not include activities of the kind specified in any of the following provisions of the... |
| coa10-meaning.l4:377 | `s 474(1) the company is a traded company` | FALSE-kind (the text says no in its own words) | "“traded company” ... means a company any of whose transferable securities are admitted to trading on a UK ... |
| coa10-meaning.l4:408 | `s 474(1) the standards are UK-adopted international accounting standards` | FALSE-kind (the text says no in its own words) | "“UK-adopted international accounting standards” means the international accounting standards which are ado... |
| coa10-medium.l4:15 | `` | FALSE-kind (the text says no in its own words) | "<the words>"`); NOTHING = the text does not decide |
| coa10-medium.l4:69 | `s 465(3) the qualifying conditions are met` | FALSE-kind (the text says no in its own words, "satisfies two or more" not met) | "The qualifying conditions are met by a company in a year in which it satisfies two or more of the followin... |
| coa10-medium.l4:100 | `s 465(1) the company qualifies as medium-sized in relation to its first finan...` | FALSE-kind (the text says no in its own words, an "if" not met) | "A company qualifies as medium-sized in relation to its first financial year if the qualifying conditions a... |
| coa10-medium.l4:141 | `s 466(6) the figure is a net figure` | FALSE-kind (the text says no in its own words) | "“net” means after any set-offs and other adjustments made to eliminate group transactions— (a) in the case... |
| coa10-medium.l4:150 | `s 466(6) the figure is a gross figure` | FALSE-kind (the text says no in its own words) | "“gross” means without those set-offs and other adjustments" |
| coa10-medium.l4:190 | `s 466(4) the qualifying conditions are met by the group` | FALSE-kind (the text says no in its own words, "satisfies two or more" not met) | "The qualifying conditions are met by a group in a year in which it satisfies two or more of the following ... |
| coa10-medium.l4:228 | `s 466(1) the parent company qualifies as a medium-sized company` | FALSE-kind (the text says no in its own words, an "only if") | "A parent company qualifies as a medium-sized company in relation to a financial year only if the group hea... |
| coa10-medium.l4:240 | `s 466(2) the group qualifies as medium-sized in relation to the parent compan...` | FALSE-kind (the text says no in its own words, an "if" not met) | "A group qualifies as medium-sized in relation to the parent company's first financial year if the qualifyi... |
| coa10-medium.l4:268 | `s 465(7) the company qualifies as medium-sized, subject to section 466` | FALSE-kind (the text says no in its own words) | section 465(1) and (2) answer no |
| coa10-medium.l4:276 | `s 465(7) the company qualifies as medium-sized, subject to section 466` | FALSE-kind (the text says no in its own words, an "only if") | "A parent company qualifies as a medium-sized company in relation to a financial year only if the group hea... |
| coa10-medium.l4:339 | `s 467(2) the member is within one of the paragraphs` | FALSE-kind (the text says no in its own words, "if any of its members is" not met by this member) | "A group is ineligible if any of its members is— ... (d) a small company that is an authorised insurance co... |
| coa10-medium.l4:344 | `s 467(2) the member is within one of the paragraphs` | FALSE-kind (the text says no in its own words, "if any of its members is" not met by this member) | "(c) a person (other than a small company) who has permission under Part 4A of the Financial Services and M... |
| coa10-medium.l4:362 | `s 467(2) the group is ineligible` | FALSE-kind (the text says no in its own words, an "if" not met) | "A group is ineligible if any of its members is" |
| coa10-medium.l4:403 | `s 467(4) the section prevents the company from taking advantage of section 41...` | FALSE-kind (the text says no in its own words) | "This section does not prevent a company from taking advantage of section 417(7) (business review: non-fina... |
| coa10-period.l4:14 | `` | FALSE-kind (the text says no in its own words) | "<the words>"`), NOTHING where it does not decide |
| coa10-period.l4:116 | `s 442(7) the accounting reference period is the relevant accounting reference...` | FALSE-kind (the text says no in its own words) | "“the relevant accounting reference period” means the accounting reference period by reference to which the... |
| coa10-period.l4:200 | `s 442(5A) the extension complies with the limit of twelve months after the en...` | FALSE-kind (the text says no in its own words) | "Any such extension must not have the effect of extending the period for filing to more than twelve months ... |
| coa10-revision.l4:15 | `` | FALSE-kind (the text says no in its own words) | "<the words>"`); NOTHING = the text does not decide |
| coa10-revision.l4:62 | `s 454(2) the revisions are confined to correction and consequential alterations` | FALSE-kind (a "where" not met, ruling of 2026-11-05) | "Where copies of the previous accounts or report have been sent out to members, delivered to the registrar ... |
| coa10-revision.l4:76 | `s 454(2) the revision is within the limit the section sets` | FALSE-kind (the text says no in its own words) | "the revisions must be confined to— (a) the correction of those respects in which the previous accounts or ... |
| coa10-revision.l4:98 | `s 455(1) section 455 applies` | FALSE-kind (a "where" not met, ruling of 2026-11-05) | "This section applies where— (a) copies ... have been sent out under section 423, or (b) a copy ... has bee... |
| coa10-revision.l4:120 | `s 455(3) the period the notice specifies is not less than one month` | FALSE-kind (the text says no in its own words) | "The notice must specify a period of not less than one month" |
| coa10-revision.l4:136 | `s 455(4) the Secretary of State may apply to the court` | FALSE-kind (a period fixed in the text's own words, ruling of 2026-11-05) | "If at the end of the specified period, or such longer period as the Secretary of State may allow" |
| coa10-revision.l4:139 | `s 455(4) the Secretary of State may apply to the court` | FALSE-kind (the text says no in its own words, an "If" not met) | "If at the end of the specified period ... it appears to the Secretary of State that the directors have not... |
| coa10-revision.l4:203 | `s 456(2) the applicant has given the registrar the notice the section requires` | FALSE-kind (a bare "shall" not done, decided at this site, ruling of 2026-11-05) | "Notice of the application, together with a general statement of the matters at issue in the proceedings, s... |
| coa10-revision.l4:277 | `s 456(5) the director is taken to have been a party to the approval of the de...` | FALSE-kind (the text says no in its own words, an "unless" met) | "unless he shows that he took all reasonable steps to prevent that approval" |
| coa10-revision.l4:303 | `s 456(6) the court may exclude one or more directors from the order or order ...` | FALSE-kind (a "where" not met, ruling of 2026-11-05) | "Where the court makes an order under subsection (5) it shall have regard to ... and it may exclude one or ... |
| coa10-revision.l4:356 | `s 456(7) the applicant has complied` | FALSE-kind (a bare "must" not done, decided at this site, ruling of 2026-11-05) | "the applicant must send to the registrar for registration a copy of the court order" |
| coa10-revision.l4:360 | `s 456(7) the applicant has complied` | FALSE-kind (a bare "must" not done, decided at this site, ruling of 2026-11-05) | "give notice to the registrar that the application has failed or been withdrawn" |
| coa10-supplementary.l4:15 | `` | FALSE-kind (the text says no in its own words) | "<the words>"`); NOTHING = the text does not decide |
| coa10-supplementary.l4:73 | `s 463(2) the director is liable to compensate the company for the loss` | FALSE-kind (the text says no in its own words, an "only if") | "He is so liable only if— (a) he knew the statement to be untrue or misleading or was reckless as to whethe... |
| coa10-supplementary.l4:94 | `s 463(4) a person is subject to liability to the claimant` | FALSE-kind (the text says no in its own words) | "No person shall be subject to any liability to a person other than the company resulting from reliance, by... |
| coa10-supplementary.l4:111 | `s 463(6) the section affects the liability` | FALSE-kind (the text says no in its own words) | "This section does not affect— (a) liability for a civil penalty" |
| coa10-supplementary.l4:112 | `s 463(6) the section affects the liability` | FALSE-kind (the text says no in its own words) | "This section does not affect— ... (b) liability for a criminal offence" |
| coa10-supplementary.l4:149 | `s 469(3) the translation meets the requirements of the section` | FALSE-kind (a bare "must" not done, decided at this site, ruling of 2026-11-05) | "In both cases— (a) the amounts must have been translated at the exchange rate prevailing on the date to wh... |
| coa10-supplementary.l4:157 | `s 469(3A) subsection (3)(b) requires the rate to be disclosed in the notes` | FALSE-kind (the text says no in its own words) | "Subsection (3)(b) does not apply to the Companies Act individual accounts of a company for a financial yea... |
| coa10-supplementary.l4:192 | `s 470(2) the partnership is a banking partnership` | FALSE-kind (the text says no in its own words) | "A “banking partnership” means a partnership which has permission under Part 4A of the Financial Services a... |

### Branches resting on reading (b): NOTHING-kind (limited by its own wording)

| module and line | function | tag | quoted words |
| --- | --- | --- | --- |
| coa10-default.l4:36 | `s 451(1) the person commits an offence` | NOTHING-kind (limited by its own wording) | "every person who immediately before the end of that period was a director of the company" |
| coa10-default.l4:57 | `s 451(3) proving that the documents were not prepared as required is a defenc...` | NOTHING-kind (limited by its own wording) | the sentence speaks only of proving that the documents were not prepared |
| coa10-default.l4:154 | `s 452(1) the court may order the directors to make good the default` | NOTHING-kind (limited by its own wording) | "the requirements of section 441 (duty to file accounts and reports) are not complied with in relation to a... |
| coa10-default.l4:157 | `s 452(1) the court may order the directors to make good the default` | NOTHING-kind (limited by its own wording) | "the directors of the company fail to make good the default within 14 days after the service of a notice on... |
| coa10-default.l4:161 | `s 452(1) the court may order the directors to make good the default` | NOTHING-kind (limited by its own wording) | "on the application of any member or creditor of the company or of the registrar" |
| coa10-default.l4:172 | `s 452(2) the court's order may provide that all the costs are borne by the di...` | NOTHING-kind (limited by its own wording) | "The court's order may provide" |
| coa10-default.l4:195 | `s 453(1) the company's liability is in addition to the directors' liability u...` | NOTHING-kind (limited by its own wording) | "This is in addition to any liability of the directors under section 451" |
| coa10-default.l4:218 | `s 453(2) the amount of the civil penalty` | NOTHING-kind (limited by its own wording) | the company is liable to a penalty only where s 453(1) is met |
| coa10-default.l4:228 | `s 453(3) the registrar may recover the penalty from the company` | NOTHING-kind (limited by its own wording) | "The penalty may be recovered by the registrar" |
| coa10-default.l4:238 | `s 453(3) the penalty is to be paid into the Consolidated Fund` | NOTHING-kind (limited by its own wording) | "the penalty ... is to be paid into the Consolidated Fund" |
| coa10-default.l4:248 | `s 453(4) proving that the documents were not prepared as required is a defenc...` | NOTHING-kind (limited by its own wording) | the sentence speaks only of proving that the documents were not prepared |
| coa10-disclosure.l4:40 | `s 458(1) the Commissioners may disclose the information to the authorised person` | NOTHING-kind (limited by its own wording) | "may disclose information to a person authorised under section 457 for the purpose of facilitating" |
| coa10-disclosure.l4:107 | `s 458(4) the person commits an offence` | NOTHING-kind (limited by its own wording) | "A person who contravenes subsection (3)" |
| coa10-disclosure.l4:158 | `s 458(6) the officer of the body corporate also commits the offence` | NOTHING-kind (limited by its own wording) | "every officer of the body who is in default" |
| coa10-disclosure.l4:160 | `s 458(6) the officer of the body corporate also commits the offence` | NOTHING-kind (limited by its own wording) | "every officer of the body" |
| coa10-disclosure.l4:212 | `s 459(2) the authorised person may require the person to produce the document...` | NOTHING-kind (limited by its own wording) | "that he may reasonably require for the purpose of— (a) discovering whether there are grounds for an applic... |
| coa10-disclosure.l4:223 | `s 459(4) the authorised person may apply to the court` | NOTHING-kind (limited by its own wording) | "If a person fails to comply with such a requirement, the authorised person may apply to the court." |
| coa10-disclosure.l4:232 | `s 459(5) the court may order the person to take such steps as it directs` | NOTHING-kind (limited by its own wording) | "If it appears to the court that the person has failed to comply with a requirement under subsection (2), i... |
| coa10-disclosure.l4:242 | `s 459(6) the statement may be used in evidence against the person who made it` | NOTHING-kind (limited by its own wording) | the bar is of use "against him in any criminal proceedings" |
| coa10-disclosure.l4:274 | `s 460(1) the information is within section 460` | NOTHING-kind (limited by its own wording) | "This section applies to information (in whatever form) obtained in pursuance of a requirement or order und... |
| coa10-disclosure.l4:292 | `s 460(2) the section bars the disclosure of the information` | NOTHING-kind (limited by its own wording) | the section applies only to the information subsection (1) describes |
| coa10-disclosure.l4:293 | `s 460(2) the section bars the disclosure of the information` | NOTHING-kind (limited by its own wording) | the section applies only to the information subsection (1) describes |
| coa10-disclosure.l4:300 | `s 460(2) the section bars the disclosure of the information` | NOTHING-kind (limited by its own wording) | "during the lifetime of that individual or so long as that business continues to be carried on" |
| coa10-disclosure.l4:302 | `s 460(2) the section bars the disclosure of the information` | NOTHING-kind (limited by its own wording) | "without the consent of that individual or the person for the time being carrying on that business" |
| coa10-disclosure.l4:320 | `s 460(4) the person commits an offence` | NOTHING-kind (limited by its own wording) | "A person who discloses information in contravention of this section" |
| coa10-disclosure.l4:394 | `s 461(3) the prohibition in section 460 does not apply to disclosure to the r...` | NOTHING-kind (limited by its own wording) | such a body is subsection (5)'s case, not subsection (3)'s |
| coa10-disclosure.l4:451 | `s 461(5) the prohibition in section 460 does not apply to disclosure to the o...` | NOTHING-kind (limited by its own wording) | "to a body exercising functions of a public nature under legislation in any country or territory outside th... |
| coa10-exemptions.l4:158 | `s 448(1) the directors of the unlimited company are not required to deliver a...` | NOTHING-kind (limited by its own wording) | "The directors of an unlimited company" |
| coa10-exemptions.l4:181 | `s 448(4)(a) the words substituted in section 434(3)` | NOTHING-kind (limited by its own wording) | "Where a company is exempt by virtue of this section from the obligation to deliver accounts" |
| coa10-exemptions.l4:192 | `s 448(4)(b) the words substituted in section 435(1)(b)` | NOTHING-kind (limited by its own wording) | "Where a company is exempt by virtue of this section from the obligation to deliver accounts" |
| coa10-exemptions.l4:313 | `s 448C(3)(a) the amount of the outstanding liabilities that the parent undert...` | NOTHING-kind (limited by its own wording) | "A guarantee given under this section has the effect that" |
| coa10-exemptions.l4:327 | `s 448C(3)(b) the person may enforce the guarantee against the parent undertaking` | NOTHING-kind (limited by its own wording) | "by any person to whom the subsidiary company is liable in respect of those liabilities" |
| coa10-exemptions.l4:328 | `s 448C(3)(b) the person may enforce the guarantee against the parent undertaking` | NOTHING-kind (limited by its own wording) | "A guarantee given under this section has the effect that" |
| coa10-filing.l4:160 | `s 441(1) a filing section applies given its description and its exclusions` | NOTHING-kind (limited by its own wording) | the company is not one the section describes |
| coa10-filing.l4:164 | `s 441(1) a filing section applies given its description and its exclusions` | NOTHING-kind (limited by its own wording) | the company is not one the section describes |
| coa10-filing.l4:551 | `s 446(1) what section 446 requires of the directors for the document` | NOTHING-kind (limited by its own wording) | "any separate corporate governance statement" |
| coa10-filing.l4:578 | `s 447(1) what section 447 requires of the directors for the document` | NOTHING-kind (limited by its own wording) | "any separate corporate governance statement" |
| coa10-filing.l4:623 | `s 443A(3) the copy of a document the section names meets the requirement to s...` | NOTHING-kind (limited by its own wording) | the section names only certain documents |
| coa10-filing.l4:868 | `s 444(5) the copy of the balance sheet contains the statement the section req...` | NOTHING-kind (limited by its own wording) | the statement is required only where the profit and loss account or the directors' report is not delivered |
| coa10-meaning.l4:69 | `s 471(1) the individual profit and loss account is part of the annual accounts` | NOTHING-kind (limited by its own wording) | there are no individual accounts for the section to apply to |
| coa10-meaning.l4:160 | `s 472(1A) the notes must be included at the foot of the balance sheet` | NOTHING-kind (limited by its own wording) | "the notes to the accounts for that year required by section 413 of this Act and regulation 5A of, and para... |
| coa10-meaning.l4:161 | `s 472(1A) the notes must be included at the foot of the balance sheet` | NOTHING-kind (limited by its own wording) | "In the case of a company which qualifies as a micro-entity" |
| coa10-meaning.l4:198 | `s 472A(3) the statement is a separate corporate governance statement` | NOTHING-kind (limited by its own wording) | the sentence defines "separate" for a corporate governance statement |
| coa10-meaning.l4:374 | `s 474(1) the company is a traded company` | NOTHING-kind (limited by its own wording) | "unless the context otherwise requires" |
| coa10-meaning.l4:418 | `s 474(2) the reference to a profit and loss account is to an income and expen...` | NOTHING-kind (limited by its own wording) | "In the case of an undertaking not trading for profit" |
| coa10-meaning.l4:427 | `s 474(2) the reference to a consolidated profit and loss account is to a cons...` | NOTHING-kind (limited by its own wording) | the sentence follows "In the case of an undertaking not trading for profit" |
| coa10-medium.l4:229 | `s 466(1) the parent company qualifies as a medium-sized company` | NOTHING-kind (limited by its own wording) | "only if" states a necessary condition and does not say the parent company qualifies when the group does |
| coa10-medium.l4:404 | `s 467(4) the section prevents the company from taking advantage of section 41...` | NOTHING-kind (limited by its own wording) | the sentence speaks only of "by reason only of its having been a member of an ineligible group" |
| coa10-period.l4:34 | `s 443(1) section 443 applies to the period for filing` | NOTHING-kind (limited by its own wording) | "which is expressed as a specified number of months from a specified date or after the end of a specified p... |
| coa10-period.l4:189 | `s 442(5) the Secretary of State may extend the period for filing` | NOTHING-kind (limited by its own wording) | "if for any special reason the Secretary of State thinks fit he may" |
| coa10-period.l4:190 | `s 442(5) the Secretary of State may extend the period for filing` | NOTHING-kind (limited by its own wording) | "on an application made before the expiry of the period otherwise allowed" |
| coa10-revision.l4:45 | `s 454(1) the directors may prepare revised accounts or a revised report or st...` | NOTHING-kind (limited by its own wording) | the section lists the annual accounts, the directors' remuneration report or directors' report, and a strat... |
| coa10-revision.l4:48 | `s 454(1) the directors may prepare revised accounts or a revised report or st...` | NOTHING-kind (limited by its own wording) | "If it appears to the directors that ... did not comply with the requirements of this Act ..., they may pre... |
| coa10-revision.l4:77 | `s 454(2) the revision is within the limit the section sets` | NOTHING-kind (limited by its own wording) | the confinement applies only "Where copies of the previous accounts or report have been sent out ..." |
| coa10-revision.l4:107 | `s 455(2) the Secretary of State may give notice to the directors indicating t...` | NOTHING-kind (limited by its own wording) | the power is given only where the section applies |
| coa10-revision.l4:155 | `s 455(5) section 455 applies equally to the revised document` | NOTHING-kind (limited by its own wording) | "revised annual accounts, revised strategic reports and revised directors' reports" |
| coa10-revision.l4:166 | `s 455(5) the references to revised accounts or reports are read as references...` | NOTHING-kind (limited by its own wording) | "in which case they have effect as if" applies only to revised annual accounts, strategic reports and direc... |
| coa10-revision.l4:193 | `s 456(1) the applicant may apply to the court for a declaration and an order` | NOTHING-kind (limited by its own wording) | "by the Secretary of State, after having complied with section 455" |
| coa10-revision.l4:231 | `s 456(3) the court may give the direction` | NOTHING-kind (limited by its own wording) | "If the court orders the preparation of revised accounts, it may give directions as to" |
| coa10-revision.l4:254 | `s 456(4) the court may give the direction` | NOTHING-kind (limited by its own wording) | "If the court orders the preparation of a revised strategic report or directors' report it may give directi... |
| coa10-revision.l4:275 | `s 456(5) the director is taken to have been a party to the approval of the de...` | NOTHING-kind (limited by its own wording) | "every director of the company at the time of the approval" |
| coa10-revision.l4:290 | `s 456(5) the court may order that the director bear the costs and expenses` | NOTHING-kind (limited by its own wording) | "If the court finds that the accounts or report did not comply with the requirements of this Act ... it may... |
| coa10-revision.l4:293 | `s 456(5) the court may order that the director bear the costs and expenses` | NOTHING-kind (limited by its own wording) | "are to be borne by such of the directors as were party to the approval of the defective accounts or report" |
| coa10-revision.l4:294 | `s 456(5) the court may order that the director bear the costs and expenses` | NOTHING-kind (limited by its own wording) | the order reaches only directors who were party to the approval |
| coa10-revision.l4:368 | `s 456(8) section 456 applies equally to the revised document` | NOTHING-kind (limited by its own wording) | "revised annual accounts, revised strategic reports and revised directors' reports" |
| coa10-revision.l4:385 | `s 457(4) the proceedings may be brought by or against the association in the ...` | NOTHING-kind (limited by its own wording) | "If the authorised person is an unincorporated association, proceedings brought in, or in connection with, ... |
| coa10-revision.l4:387 | `s 457(4) the proceedings may be brought by or against the association in the ...` | NOTHING-kind (limited by its own wording) | "proceedings brought in, or in connection with, the exercise of any function by the association as an autho... |
| coa10-revision.l4:390 | `s 457(4) the proceedings may be brought by or against the association in the ...` | NOTHING-kind (limited by its own wording) | "in the name of a body corporate whose constitution provides for the establishment of the association" |
| coa10-supplementary.l4:67 | `s 463(2) the director is liable to compensate the company for the loss` | NOTHING-kind (limited by its own wording) | the section applies only to the reports and statements subsection (1) lists |
| coa10-supplementary.l4:70 | `s 463(2) the director is liable to compensate the company for the loss` | NOTHING-kind (limited by its own wording) | "liable to compensate the company for any loss suffered by it as a result of" |
| coa10-supplementary.l4:95 | `s 463(4) a person is subject to liability to the claimant` | NOTHING-kind (limited by its own wording) | the sentence is limited to liability to a person other than the company resulting from reliance on informat... |
| coa10-supplementary.l4:113 | `s 463(6) the section affects the liability` | NOTHING-kind (limited by its own wording) | the sentence names only liability for a civil penalty and for a criminal offence |
| coa10-supplementary.l4:126 | `s 469(1) the amounts may also be shown in the same accounts translated into e...` | NOTHING-kind (limited by its own wording) | "The amounts set out in the annual accounts of a company" |
| coa10-supplementary.l4:135 | `s 469(2) the directors may deliver to the registrar an additional copy of the...` | NOTHING-kind (limited by its own wording) | "When complying with section 441 (duty to file accounts and reports)" |
| coa10-supplementary.l4:158 | `s 469(3A) subsection (3)(b) requires the rate to be disclosed in the notes` | NOTHING-kind (limited by its own wording) | the sentence speaks only of a micro-entity's Companies Act individual accounts |
| coa10-supplementary.l4:167 | `s 469(4) the additional copy is treated as statutory accounts of the company` | NOTHING-kind (limited by its own wording) | "any additional copy of the company's annual accounts delivered to the registrar under subsection (2) above" |
| coa10-supplementary.l4:176 | `s 469(4) the references in sections 434 and 435 to the auditor's report are r...` | NOTHING-kind (limited by its own wording) | "In the case of such a copy" |
| coa10-supplementary.l4:202 | `s 470(3) the expression has the same meaning as in those provisions` | NOTHING-kind (limited by its own wording) | "Expressions used in this section that are also used in the provisions regulating activities under the Fina... |

### Reading a result: FALSE and NOTHING (coa10)

In this part a JUST FALSE ("no") means the text says no to the case in its own words.
For the filing sections it means, for example: the section's own exclusion applies ("This section does not apply to companies within section 444"); the directors are told to do something and did not (a copy that does not state who signed it); a period the text fixes has run out (delivered after the period for filing); or the Act says "It is not a defence ..." (s 451(3), s 453(4)).
For the exemptions it means a condition of the exemption is not met (s 448(2), s 448A(2)), or a bar applies (s 448(3), s 448B).
For the offences and civil penalty it means the documents were delivered in time, or the person proved the defence of s 451(2) (worded "this section gives the person a defence on these facts").
For the supplementary provisions it means the thing is not within a definition the text states as "means" or "are", or a flat negative applies ("No person shall be subject to any liability ...").
A NOTHING ("not covered") means the text does not say: a person who was not a director immediately before the end of the period (s 451(1)); a document that ss 443A to 447 do not name for that kind of company; a person, report, recipient or purpose that a list does not name and does not close with "only" (ss 456(1), 459(3), 461(3) and (4), 463(1)); a company within neither paragraph of s 448B, so that s 448A(1) cannot be answered; an extension of the period for filing beyond the limit of s 442(5A); a first-text micro-entity that two sections both describe (fork F2); or an input the part takes from another part that is itself NOTHING.
A grant named "may" (for example s 442(5), s 454(1) or s 459(4)) answers NOTHING, not JUST FALSE, when its "If" gate is not met: the text limits the grant in its own wording and the case falls outside the limit (fork F18 to F26).
A caller must never turn NOTHING into FALSE: in particular, `s 441(2)` answering NOTHING does not mean the directors need not deliver, and `s 448A(1)` answering NOTHING does not mean the exemption fails.

## Seams (coa10)

A seam input is declared once, in the function that asks, named for the section that answers it, and by default `MAYBE BOOLEAN` so that a NOTHING in the answering section stays NOTHING here (PLAN.md, section 4).

### Seam inputs taken (25)

| input | module | answered by (PLAN.md part) | type |
| --- | --- | --- | --- |
| `s 384A the company qualifies as a micro-entity` | coa10-filing | ss 384A, 384B [coa8] | MAYBE BOOLEAN |
| `s 384B the company would qualify as a micro-entity but for being or having been a member of an ineligible group` | coa10-filing | ss 384A, 384B [coa8] | MAYBE BOOLEAN |
| `s 384A the company qualifies as a micro-entity in relation to the financial year` | coa10-filing | ss 384A, 384B [coa8] | MAYBE BOOLEAN |
| `s 381 the company is subject to the small companies regime` | coa10-filing | s 381 [coa8] | MAYBE BOOLEAN |
| `s 384 the company would be subject to the small companies regime but for being or having been a member of an ineligible group` | coa10-filing | s 384 [coa8] | MAYBE BOOLEAN |
| `s 415A the company is entitled to small companies exemption in relation to the directors' report` | coa10-filing | s 415A [coa9] | MAYBE BOOLEAN |
| `s 385(3) the company is an unquoted company` | coa10-filing | s 385 [coa8] | MAYBE BOOLEAN |
| `s 385(2) the company is a quoted company` | coa10-filing | s 385 [coa8] | MAYBE BOOLEAN |
| `s 475(1) the company is exempt from audit and the directors have taken advantage of that exemption` | coa10-filing | ss 475 to 479A [coa11] | MAYBE BOOLEAN |
| `s 506 the conditions in section 506 for omitting the names are met` | coa10-filing | s 506 [coa12] | MAYBE BOOLEAN |
| `s 1164(2) the company is a banking company` | coa10-exemptions | s 1164 [keel] | MAYBE BOOLEAN |
| `s 1165(3) the company is an insurance company` | coa10-exemptions | s 1165 [keel] | MAYBE BOOLEAN |
| `s 1164(4) the company is the parent company of a banking group` | coa10-exemptions | s 1164 [keel] | MAYBE BOOLEAN |
| `s 1165(5) the company is the parent company of an insurance group` | coa10-exemptions | s 1165 [keel] | MAYBE BOOLEAN |
| `s 1165(2) the company is an authorised insurance company` | coa10-exemptions | s 1165 [keel] | MAYBE BOOLEAN |
| `s 1165 the company carries on insurance market activity` | coa10-exemptions | s 1165 [keel] | MAYBE BOOLEAN |
| `s 1169(1) the company has been dormant throughout the whole of the financial year` | coa10-exemptions | s 1169 [keel] | BOOLEAN |
| `s 1121 the officer is in default` | coa10-disclosure | s 1121 [coa24] | MAYBE BOOLEAN |
| `s 1167 the body that issued it is prescribed by regulations` | coa10-meaning | s 1167 "Meaning of prescribed" [keel] | MAYBE BOOLEAN |
| `s 394 the company prepares individual accounts for the year` | coa10-meaning | s 394 [coa8] | MAYBE BOOLEAN |
| `s 399 the company prepares group accounts for the year` | coa10-meaning | s 399 [coa8] | MAYBE BOOLEAN |
| `s 408 the company has taken the option to omit the individual profit and loss account from the annual accounts` | coa10-meaning | s 408 [coa8] | MAYBE BOOLEAN |
| `s 22 the activity is a regulated activity within section 22 of the Financial Services and Markets Act 2000` | coa10-meaning | section 22 of the Financial Services and Markets Act 2000 (an Act outside the sources; not in the plan) | BOOLEAN |
| `s 1173(1) the company is a parent company` | coa10-medium | s 1173 [keel] | MAYBE BOOLEAN |
| `s 382 the company qualified as small in relation to its last financial year ending on or before the end of the financial year in question` | coa10-medium | ss 382, 383 [coa8] | MAYBE BOOLEAN |

The table was built from the `GIVEN` lines and record fields of the layer-1 modules whose names begin with the number of a section outside 441 to 474.

### Cross-references of the plan that are plain facts here, not seam inputs

PLAN.md lists these for this part; each is a fact a person can state, or a name only, so the function asks it as a plain `BOOLEAN` (or text) in its own words and the lead may wire it to the answering part at the merge:
- s 392 (coa8): `the period was shortened by a notice under section 392` and `the date of that notice`, fields of `s 442 facts about the accounting reference period`.
- s 423 and s 426 (coa9): `copies ... have been sent out under section 423` in s 455(1); s 454(4)(c) is regulation-making (inert).
- s 434 and s 435 (coa9): the words substituted by s 448(4) are `MAYBE STRING` values in `s 448(4)(a)` and `s 448(4)(b)`.
- s 498 (coa12) and schedule 1 (coa28): reproduced statements and the abridgement of paragraph 1A, asked as plain facts in `s 444(5B)` and `s 444(1)`.
- s 117 (coa3): "special register body", asked as a plain fact in `s 448B`.
- s 404, s 417, s 393, s 1110F, s 396, s 409, s 412, s 416, s 421 (coa8, coa9, coa24): cited only inside rules that are inert machinery (ss 468, 468A, 473) or as a name (s 466(6), s 467(4)).

### Seams this part found that the plan lacks

- `s 1167 the body that issued it is prescribed by regulations`: s 464(1) turns on who is prescribed; s 1167 is "Meaning of “prescribed”" in the headings.
- `s 22 the activity is a regulated activity within section 22 of the Financial Services and Markets Act 2000`: s 474(1) "regulated activity" borrows that Act's section 22, which is not among the sources.
- The borrowed facts of s 474(1) (e-money issuer, MiFID investment firm, UCITS management company, international accounting standards) are asked as plain facts in their own words.

### What this part answers for others

The functions below are the answers other parts ask for (PLAN.md, section 6): the period for filing (s 442), accounting standards (s 464), medium-sized companies (ss 465 to 467), annual accounts and annual accounts and reports (s 471), corporate governance statement (s 472A) and the minor definitions of s 474.
- s 442: `s 442(1) the period for filing ends on`
- s 464: `s 464(1) the statement is an accounting standard`
- ss 465 to 467: `s 465(7) the company qualifies as medium-sized, subject to section 466`; `s 467(1) the section bars the company from taking advantage of the medium-sized provisions`
- s 471: `s 471(1) the accounts are part of the company's annual accounts`; `s 471(2) the item is among the annual accounts and reports of the unquoted company`; `s 471(3) the item is among the annual accounts and reports of the quoted company`
- s 472A: `s 472A(1) the statement is a corporate governance statement`; `s 472A(3) the statement is a separate corporate governance statement`
- s 474: `s 474(1) the turnover of the company`; `s 474(1) the company is a traded company`; `s 474(1) the person is an e-money issuer`; `s 474(1) the person is a MiFID investment firm`; `s 474(1) the auditor's report is qualified`; `s 474(1) the activity is a regulated activity for the purposes of this Part`

## The seat layer (coa10)

The questions, in the text's order; the last column names the layer-1 rule each calls (the first two it calls).

| # | question | returns | calls |
| --- | --- | --- | --- |
| 1 | Under section 441(2), must the directors deliver the accounts and reports for the financial year to the registrar | MAYBE BOOLEAN | `s 441(2) the directors must deliver the accounts and reports for the financial year` |
| 2 | Under section 441(1), which of sections 443A to 447 sets out the accounts and reports required of the directors of my company | MAYBE `s 441 filing section` | `s 441(1) the filing section that applies to the company`; `s 441 facts about the company` |
| 3 | Under section 441(1), does the filing section that applies to my company make it a duty, a permission or not required for the directors to deliver this document to the registrar | MAYBE `s 441 requirement` | `s 441(1) what the filing section that applies requires of the directors for the document`; `s 441 facts about the company` |
| 4 | Under section 441(1), were the accounts and reports delivered before the end of the period for filing | MAYBE BOOLEAN | `s 442(1) the number of days from the end of the accounting reference period to the end of the period for filing`; `s 441(1) the requirements were complied with before the end of the period for filing` |
| 5 | Under section 442(1), on what date does the period for filing the accounts and reports end | MAYBE DATE | `s 442(1) the period for filing ends on`; `s 442 facts about the accounting reference period` |
| 6 | Under section 442(2), on what date does the period for filing end for an ordinary accounting reference period | DATE | `s 442(2) the period for filing ends on` |
| 7 | Under section 442(3), on what date does the period for filing end for a first accounting reference period of more than twelve months | DATE | `s 442(3) the period for filing ends on for a first accounting reference period of more than twelve months` |
| 8 | Under section 442(3), is the accounting reference period a period of more than twelve months | BOOLEAN | `s 442(3) the relevant accounting reference period is a period of more than twelve months` |
| 9 | Under section 442(4), on what date does the period for filing end, allowing for any notice under section 392 that shortened the accounting reference period | DATE | `s 442(4) the period for filing ends on where the accounting reference period is treated as shortened` |
| 10 | Under section 442(5), leaving aside the limit in subsection (5A), may the Secretary of State extend the period for filing on my application | MAYBE BOOLEAN | `s 442(5) the Secretary of State may extend the period for filing` |
| 11 | Under section 442(5A), does the extension comply with the limit of twelve months after the end of the accounting reference period | MAYBE BOOLEAN | `s 442(5A) the extension complies with the limit of twelve months after the end of the accounting reference period` |
| 12 | Under section 442(6), does the period for a public company apply | BOOLEAN | `s 442(6) the period for a public company applies` |
| 13 | Under section 443, on what date does a period of a stated number of months from a given date end | DATE | `s 443(2) the period ends with` |
| 14 | Under section 443A(1), is delivering this document to the registrar a duty, a permission or not required of the directors of a micro-entity | MAYBE `s 441 requirement` | `s 443A(1) what section 443A requires of the directors for the document`; `s 441 facts about what is delivered` |
| 15 | Under section 444(1), is delivering this document to the registrar a duty, a permission or not required of the directors of a company subject to the small companies regime | MAYBE `s 441 requirement` | `s 444(1) what section 444 requires of the directors for the document`; `s 441 facts about what is delivered` |
| 16 | Under section 444A(1), is delivering this document to the registrar a duty, a permission or not required of the directors of a company entitled to the small companies exemption in relation to the directors' report | MAYBE `s 441 requirement` | `s 444A(1) what section 444A requires of the directors for the document`; `s 441 facts about what is delivered` |
| 17 | Under section 445(1), must the directors of a medium-sized company deliver this document to the registrar | MAYBE `s 441 requirement` | `s 445(1) what section 445 requires of the directors for the document`; `s 441 facts about what is delivered` |
| 18 | Under section 446(1), must the directors of an unquoted company deliver this document to the registrar | MAYBE `s 441 requirement` | `s 446(1) what section 446 requires of the directors for the document`; `s 441 facts about what is delivered` |
| 19 | Under section 447(1), must the directors of a quoted company deliver this document to the registrar | MAYBE `s 441 requirement` | `s 447(1) what section 447 requires of the directors for the document`; `s 441 facts about what is delivered` |
| 20 | Under section 443A(3), does the copy of this document meet the requirement to state who signed it on behalf of the board | MAYBE BOOLEAN | `s 443A(3) the copy meets the requirement to state who signed it` |
| 21 | Under section 444(6), in the first text of section 444, does the copy of this document meet the requirement to state who signed it on behalf of the board | MAYBE BOOLEAN | `s 444(6) the copy meets the requirement to state who signed it` |
| 22 | Under section 445(5), does the copy of this document meet the requirement to state who signed it on behalf of the board | MAYBE BOOLEAN | `s 445(5) the copy meets the requirement to state who signed it` |
| 23 | Under section 446(3), does the copy of this document meet the requirement to state who signed it on behalf of the board | MAYBE BOOLEAN | `s 446(3) the copy meets the requirement to state who signed it` |
| 24 | Under section 447(3), does the copy of this document meet the requirement to state who signed it on behalf of the board | MAYBE BOOLEAN | `s 447(3) the copy meets the requirement to state who signed it` |
| 25 | Under section 443A(4), does the copy of the auditor's report state what the section requires | MAYBE BOOLEAN | `s 443A(4) the copy of the auditor's report states what the section requires`; `s 443A facts about the copy of the auditor's report` |
| 26 | Under section 445(6), does the copy of the auditor's report state what the section requires | MAYBE BOOLEAN | `s 445(6) the copy of the auditor's report states what the section requires`; `s 443A facts about the copy of the auditor's report` |
| 27 | Under section 447(4), does the copy of the auditor's report state what the section requires | MAYBE BOOLEAN | `s 447(4) the copy of the auditor's report states what the section requires`; `s 443A facts about the copy of the auditor's report` |
| 28 | Under section 444(5), in the first text of section 444, must the copy of the balance sheet contain a statement that the accounts and reports have been delivered under the small companies regime provisions | MAYBE BOOLEAN | `s 444(5) the section requires the copy of the balance sheet to contain the statement` |
| 29 | Under section 444(5C), in the first text of section 444, does subsection (5A) apply to my company | MAYBE BOOLEAN | `s 444(5C) subsection (5A) applies to the company` |
| 30 | Under section 444(5B), in the first text of section 444, do the notes to the balance sheet satisfy the requirements of that subsection | MAYBE BOOLEAN | `s 444(5B) the notes to the balance sheet satisfy the requirements`; `s 443A facts about the copy of the auditor's report` |
| 31 | Under section 448(1), does the unlimited company exemption mean the directors of my company are not required to deliver accounts and reports | MAYBE BOOLEAN | `s 448(1) the directors of the unlimited company are not required to deliver accounts and reports`; `s 448(2) the conditions are met` |
| 32 | Under section 448A(1), does the dormant subsidiaries exemption mean the directors of my company are not required to deliver a copy of the individual accounts | MAYBE BOOLEAN | `s 448A(1) the directors of the dormant subsidiary are not required to deliver a copy of the individual accounts`; `s 448A(2) the conditions for the exemption are complied with` |
| 33 | Under section 448B, is my company excluded from the dormant subsidiaries exemption | MAYBE BOOLEAN | `s 448B the company is excluded from the dormant subsidiaries exemption` |
| 34 | Under section 448C(2), does the parent undertaking's statement meet the requirements of the section | MAYBE BOOLEAN | `s 448C(2) the statement meets the requirements of the section` |
| 35 | Under section 448C(3), if a parent undertaking has given a guarantee under section 448C, how much of the subsidiary company's outstanding liabilities does it still guarantee, in pounds | MAYBE NUMBER | `s 448C(3)(a) the amount of the outstanding liabilities that the parent undertaking still guarantees`; `s 448C(1) a guarantee is given by the parent undertaking` |
| 36 | Under section 448C(3), may I enforce against a parent undertaking a guarantee under section 448C | MAYBE BOOLEAN | `s 448C(3)(b) the person may enforce the guarantee against the parent undertaking`; `s 448C(1) a guarantee is given by the parent undertaking` |
| 37 | Under section 451(1), have I committed an offence in relation to the delivery of the company's accounts and reports before the end of the period for filing | MAYBE BOOLEAN | `s 451(1) the person commits an offence` |
| 38 | Under section 451(2), does section 451 give me a defence on these facts | MAYBE BOOLEAN | `s 451(2) this section gives the person a defence on these facts` |
| 39 | Under section 451(3), is it a defence to the offence to prove that the documents were not in fact prepared as the Act requires | MAYBE BOOLEAN | `s 451(3) proving that the documents were not prepared as required is a defence to the offence` |
| 40 | Under section 451(4), am I guilty of an offence under section 451 | MAYBE BOOLEAN | `s 451(4) the person is guilty of an offence under section 451`; `s 451(1) the person commits an offence` |
| 41 | Under section 451(4), what is the greatest fine on summary conviction for the offence, in pounds | NUMBER | `s 451(4) the greatest fine on summary conviction in pounds` |
| 42 | Under section 451(4), what is the greatest daily default fine for continued contravention, in pounds | NUMBER | `s 451(4) the greatest daily default fine in pounds` |
| 43 | Under section 452(1), may the court order the directors to make good a default in filing the accounts and reports | MAYBE BOOLEAN | `s 452(1) the court may order the directors to make good the default`; `s 452(1)(b) the directors failed to make good the default within 14 days after the service of the notice` |
| 44 | Under section 452(2), if the court makes an order under section 452(1), may the order provide that the costs are borne by the directors | MAYBE BOOLEAN | `s 452(2) the court's order may provide that all the costs are borne by the directors` |
| 45 | Under section 453(1), is the company liable to a civil penalty for filing late | MAYBE BOOLEAN | `s 453(1) the company is liable to a civil penalty` |
| 46 | Under section 453(2), how many days after the end of the period for filing were the accounts and reports delivered, for the civil penalty | NUMBER | `s 453(2)(a) the number of days between the end of the period for filing and the day on which the requirements are complied with` |
| 47 | Under section 453(2), if the company is liable to a civil penalty, what is its amount, in pounds | MAYBE NUMBER | `s 453(2) the amount of the civil penalty`; `s 453(1) the company is liable to a civil penalty` |
| 48 | Under section 453(3), may the registrar recover a civil penalty under section 453 from the company | MAYBE BOOLEAN | `s 453(3) the registrar may recover the penalty from the company`; `s 453(1) the company is liable to a civil penalty` |
| 49 | Under section 453(4), is it a defence to the civil penalty to prove that the documents were not in fact prepared as the Act requires | MAYBE BOOLEAN | `s 453(4) proving that the documents were not prepared as required is a defence to the civil penalty` |
| 50 | Under section 454(1), may the directors prepare revised accounts or a revised report or statement | MAYBE BOOLEAN | `s 454(1) the directors may prepare revised accounts or a revised report or statement` |
| 51 | Under section 454(2), are the revisions I am making confined to the correction of the respects in which the previous accounts or report did not comply and necessary consequential alterations | MAYBE BOOLEAN | `s 454(2) the revision is within the limit the section sets`; `s 454(2) the revisions are confined to correction and consequential alterations` |
| 52 | Under section 455(1), does section 455 apply to the company's accounts or report | MAYBE BOOLEAN | `s 455(1) section 455 applies` |
| 53 | Under section 455(3), does the notice specify a period of not less than one month for the directors | MAYBE BOOLEAN | `s 455(3) the period the notice specifies is not less than one month` |
| 54 | Under section 455(4), may the Secretary of State apply to the court | MAYBE BOOLEAN | `s 455(4) the Secretary of State may apply to the court` |
| 55 | Under section 456(1), may this person apply to the court for a declaration that the accounts or report do not comply | MAYBE BOOLEAN | `s 456(1) the applicant may apply to the court for a declaration and an order` |
| 56 | Under section 456(5), am I taken to have been a party to the approval of the defective accounts or report | MAYBE BOOLEAN | `s 456(5) the director is taken to have been a party to the approval of the defective accounts or report` |
| 57 | Under section 456(5), may the court order me to bear the costs and expenses of the application | MAYBE BOOLEAN | `s 456(5) the court may order that the director bear the costs and expenses`; `s 456(5) the director is taken to have been a party to the approval of the defective accounts or report` |
| 58 | Under section 456(6), where the court has made an order under section 456(5), may it exclude me from the order or order me to pay a different amount | MAYBE BOOLEAN | `s 456(6) the court may exclude one or more directors from the order or order the payment of different amounts` |
| 59 | Under section 456(7), has the applicant done what the section requires when the proceedings end | MAYBE BOOLEAN | `s 456(7) the applicant has complied` |
| 60 | Under section 457(4), may proceedings brought in connection with the functions of an authorised person be brought by or against the authorised person in the name of a body corporate | MAYBE BOOLEAN | `s 457(4) the proceedings may be brought by or against the association in the name of the body corporate` |
| 61 | Under section 458(1), may the Commissioners for Her Majesty's Revenue and Customs disclose this information | MAYBE BOOLEAN | `s 458(1) the Commissioners may disclose the information to the authorised person` |
| 62 | Under section 458(3), does the section bar this use of the information that the Commissioners disclosed to the authorised person | MAYBE BOOLEAN | `s 458(3)(a) the section bars the use of the information` |
| 63 | Under section 458(3), does the section bar this further disclosure of the information that the Commissioners disclosed to the authorised person | MAYBE BOOLEAN | `s 458(3)(b) the section bars the further disclosure of the information` |
| 64 | Under section 458(4), do I commit an offence by my use or further disclosure of information disclosed under section 458 | MAYBE BOOLEAN | `s 458(4) the person commits an offence` |
| 65 | Under section 458(5), what is the greatest penalty for the offence on this kind of conviction | MAYBE Penalty | `s 458(5) the penalty for the offence` |
| 66 | Under section 458(6), is the person treated as an officer of the body corporate that committed the offence | MAYBE BOOLEAN | `s 458(6) the person is treated as an officer of the body` |
| 67 | Under section 459(2), may the authorised person require me to produce this document or give this information | MAYBE BOOLEAN | `s 459(2) the authorised person may require the person to produce the document or provide the information or explanation`; `s 459(1) section 459 applies` |
| 68 | Under section 459(4), if a person fails to comply with a requirement under section 459(2), may the authorised person apply to the court | MAYBE BOOLEAN | `s 459(4) the authorised person may apply to the court` |
| 69 | Under section 459(6), may my statement be used in evidence against me in criminal proceedings | MAYBE BOOLEAN | `s 459(6) the statement may be used in evidence against the person who made it` |
| 70 | Under section 459(7), does section 459 compel me to disclose this document or information | MAYBE BOOLEAN | `s 459(7) the section compels the person to disclose the document or information` |
| 71 | Under section 460(2), does section 460 bar the disclosure of this information | MAYBE BOOLEAN | `s 460(2) the section bars the disclosure of the information`; `s 460(1) the information is within section 460` |
| 72 | Under section 460(4), do I commit an offence by disclosing information obtained under section 459 | MAYBE BOOLEAN | `s 460(4) the person commits an offence` |
| 73 | Under section 461(3), does the prohibition in section 460 not apply to a disclosure to this recipient | MAYBE BOOLEAN | `s 461(3) the prohibition in section 460 does not apply to disclosure to the recipient` |
| 74 | Under section 461(4), does the prohibition in section 460 not apply to a disclosure for this purpose | MAYBE BOOLEAN | `s 461(4) the prohibition in section 460 does not apply to disclosure for the purpose` |
| 75 | Under section 463(2), is the director liable to compensate the company for its loss from an untrue or misleading statement in, or an omission from, a report or statement | MAYBE BOOLEAN | `s 463(2) the director is liable to compensate the company for the loss`; `s 463(1) the section applies to the report or statement` |
| 76 | Under section 463(4), is a person subject to liability to someone other than the company for relying on the information in a report or statement | MAYBE BOOLEAN | `s 463(4) a person is subject to liability to the claimant`; `s 463(1) the section applies to the report or statement` |
| 77 | Under section 463(6), does section 463 affect this other liability | MAYBE BOOLEAN | `s 463(6) the section affects the liability` |
| 78 | Under section 465(3), are the qualifying conditions for a medium-sized company met in the year | MAYBE BOOLEAN | `s 465(3) the qualifying conditions are met` |
| 79 | Under section 465(5), what is the company's balance sheet total, in pounds | NUMBER | `s 465(5) the balance sheet total` |
| 80 | Under section 465(6), what is the company's number of employees | MAYBE NUMBER | `s 465(6) the number of employees` |
| 81 | Under section 465(1), does the company qualify as medium-sized in its first financial year | MAYBE BOOLEAN | `s 465(1) the company qualifies as medium-sized in relation to its first financial year` |
| 82 | Under section 465(2), does the company qualify as medium-sized in a later financial year | MAYBE BOOLEAN | `s 465(2) the company qualifies as medium-sized in relation to a subsequent financial year` |
| 83 | Under section 465(7), does the company qualify as medium-sized, taking account of section 466 if it is a parent company | MAYBE BOOLEAN | `s 465(7) the company qualifies as medium-sized, subject to section 466` |
| 84 | Under section 466(4), are the qualifying conditions for a medium-sized group met in the year | MAYBE BOOLEAN | `s 466(4) the qualifying conditions are met by the group` |
| 85 | Under section 466(7), on what date does the financial year of the subsidiary undertaking whose figures are used end | MAYBE DATE | `s 466(7) the end of the subsidiary undertaking's financial year whose figures are used` |
| 86 | Under section 466(3), does the group qualify as medium-sized in a later financial year of the parent company | MAYBE BOOLEAN | `s 466(3) the group qualifies as medium-sized in relation to a subsequent financial year` |
| 87 | Under section 467(1), is the company barred from taking advantage of the medium-sized provisions | MAYBE BOOLEAN | `s 467(1) the section bars the company from taking advantage of the medium-sized provisions` |
| 88 | Under section 467(2), is the group ineligible because of one of its members | MAYBE BOOLEAN | `s 467(2) the group is ineligible`; `s 467 member of a group` |
| 89 | Under section 467(4), does section 467 prevent the company taking advantage of section 417(7) by reason only of membership of an ineligible group | MAYBE BOOLEAN | `s 467(4) the section prevents the company from taking advantage of section 417(7)` |
| 90 | Under section 469(3), does the translation of the accounts into euros meet the requirements of the section | MAYBE BOOLEAN | `s 469(3) the translation meets the requirements of the section` |
| 91 | Under section 469(2), may the directors deliver an additional copy of the annual accounts in euros to the registrar | MAYBE BOOLEAN | `s 469(2) the directors may deliver to the registrar an additional copy of the annual accounts translated into euros` |
| 92 | Under section 471(2), is this document among the annual accounts and reports of an unquoted company | MAYBE BOOLEAN | `s 471(2) the item is among the annual accounts and reports of the unquoted company` |
| 93 | Under section 471(3), is this document among the annual accounts and reports of a quoted company | MAYBE BOOLEAN | `s 471(3) the item is among the annual accounts and reports of the quoted company` |
| 94 | Under section 474(1), what is the turnover of the company, in pounds | NUMBER | `s 474(1) the turnover of the company` |
| 95 | Under section 474(1), is the company a traded company | MAYBE BOOLEAN | `s 474(1) the company is a traded company` |
| 96 | Under section 474(1), is the auditor's report qualified | MAYBE BOOLEAN | `s 474(1) the auditor's report is qualified` |
| 97 | Under section 474(1), is the person an e-money issuer | MAYBE BOOLEAN | `s 474(1) the person is an e-money issuer` |
| 98 | Under section 474(1), is the person a MiFID investment firm | MAYBE BOOLEAN | `s 474(1) the person is a MiFID investment firm` |
| 99 | Under section 464(1), is this statement an accounting standard | MAYBE BOOLEAN | `s 464(1) the statement is an accounting standard` |
| 100 | Under section 472A(3), is this a separate corporate governance statement | MAYBE BOOLEAN | `s 472A(3) the statement is a separate corporate governance statement`; `s 472A(1) the statement is a corporate governance statement` |
| 101 | Under section 474(1), is this activity a regulated activity for the purposes of Part 15 | MAYBE BOOLEAN | `s 474(1) the activity is a regulated activity for the purposes of this Part` |

### Direction of each question against its body

I read every question name against the layer-1 function it calls and against the polarity of the text.
The questions that ask for a bar, a no-duty or a defence are named as that thing, so that JUST TRUE means the thing holds: "does the section bar this use ..." (s 458(3)), "is my company excluded from the dormant subsidiaries exemption" (s 448B), "does the unlimited company exemption mean the directors ... are not required to deliver" (ss 448(1), 448A(1)), "does section 460 bar the disclosure" (s 460(2)), "does the prohibition in section 460 not apply ..." (s 461(3), (4)), "is the company barred from taking advantage of the medium-sized provisions" (s 467(1)), "is the group ineligible" (s 467(2)).
The questions whose text says "no" are named as the sentence asks it, so a JUST FALSE is the text's answer: "is it a defence to the offence to prove that the documents were not in fact prepared as the Act requires" (s 451(3), the Act says it is not), the same for s 453(4), "may my statement be used in evidence against me" (s 459(6)), "does section 459 compel me" (s 459(7)), "is a person subject to liability to someone other than the company" (s 463(4)), "does section 463 affect this other liability" (s 463(6)), "does section 467 prevent the company taking advantage of section 417(7)" (s 467(4)).
No question was found whose name asks one direction and whose body answers the other.
One seat body had wrong inputs, not a wrong direction: the question for s 467(2) first fed one "small company that is a bank" input to two fields of the member record; it now asks the member's small-company status and its category separately.

### Second audit of the seat questions (2026-11-12)

Every question name and `@export` text was read again against the body of the layer-1 function it calls, not against that function's title.
Questions read: 101. Retitled: 31 (direction: 0; subject, that is a premise or status stated in the name that the function tests, or a limb the name asked more or less of than the body answers: 31).
Each retitled question keeps the "Under section N," form, and its `@export` text and `DECIDE` name are the same words (the `@export` text with a question mark).
No expected value changed for a retitled question; `coa10-cases-seat.l4` is generated by question key and carries the new names, with a `-- RECONCILED 2026-11-12` line at the head of each retitled question.
Seven expected values changed because of the name-test sweep, each restated in place: the questions for s 442(5), s 452(1) (two cases), s 454(1), s 456(5), s 457(4) and s 459(4).

| # | old question | new question | why |
| --- | --- | --- | --- |
| 1 | Under section 441(1), which section of Chapter 10 sets out the accounts and reports the directors must deliver | Under section 441(1), which of sections 443A to 447 sets out the accounts and reports required of the directors of my company | subject: Chapter 10 also holds ss 448 to 453, and the function names only one of ss 443A to 447; "must deliver" was a consequence the function does not compute |
| 2 | Under section 441(1), must or may the directors deliver this document under the filing section that applies to my company | Under section 441(1), does the filing section that applies to my company make it a duty, a permission or not required for the directors to deliver this document to the registrar | subject: the function answers one of must, may or not required; "must or may" left out the third answer |
| 3 | Under section 442(4), on what date does the period for filing end where the accounting reference period was shortened by a notice under section 392 | Under section 442(4), on what date does the period for filing end, allowing for any notice under section 392 that shortened the accounting reference period | subject: the name stated the shortening as a given, but the function tests it and returns the ordinary period when there is none |
| 4 | Under section 442(5), may the Secretary of State extend the period for filing | Under section 442(5), leaving aside the limit in subsection (5A), may the Secretary of State extend the period for filing on my application | subject: the function does not apply the twelve-month limit of s 442(5A), which the name left unsaid |
| 5 | Under section 443A(1), must or may the directors of a micro-entity deliver this document to the registrar | Under section 443A(1), is delivering this document to the registrar a duty, a permission or not required of the directors of a micro-entity | subject: the function answers must, may or not required; "must or may" left out the third answer |
| 6 | Under section 444(1), must or may the directors of a company subject to the small companies regime deliver this document to the registrar | Under section 444(1), is delivering this document to the registrar a duty, a permission or not required of the directors of a company subject to the small companies regime | subject: the function answers must, may or not required; "must or may" left out the third answer |
| 7 | Under section 444A(1), must or may the directors of a company entitled to the small companies exemption in relation to the directors' report deliver this document to the registrar | Under section 444A(1), is delivering this document to the registrar a duty, a permission or not required of the directors of a company entitled to the small companies exemption in relation to the directors' report | subject: the function answers must, may or not required; "must or may" left out the third answer |
| 8 | Under section 444(6), does the copy of this document meet the requirement to state who signed it on behalf of the board | Under section 444(6), in the first text of section 444, does the copy of this document meet the requirement to state who signed it on behalf of the board | subject: the body is the first text's s 444(6); in the second text s 444(6) says something else, and the name did not say which text |
| 9 | Under section 444(5), must the copy of the balance sheet contain a statement that the accounts and reports have been delivered under the small companies regime provisions | Under section 444(5), in the first text of section 444, must the copy of the balance sheet contain a statement that the accounts and reports have been delivered under the small companies regime provisions | subject: the body is the first text's s 444(5); the second text has no such subsection, and the name did not say which text |
| 10 | Under section 444(5C), does subsection (5A) apply to my company | Under section 444(5C), in the first text of section 444, does subsection (5A) apply to my company | subject: the body is the first text's s 444(5C); the name did not say which text |
| 11 | Under section 444(5B), do the notes to the balance sheet satisfy the requirements | Under section 444(5B), in the first text of section 444, do the notes to the balance sheet satisfy the requirements of that subsection | subject: the body is the first text's s 444(5B), and "the requirements" named no subsection |
| 12 | Under section 448(1), are the directors of my unlimited company not required to deliver accounts and reports | Under section 448(1), does the unlimited company exemption mean the directors of my company are not required to deliver accounts and reports | subject: the name stated "my unlimited company" as a given, but the function tests whether the company is unlimited |
| 13 | Under section 448A(1), are the directors of my dormant subsidiary not required to deliver a copy of the individual accounts | Under section 448A(1), does the dormant subsidiaries exemption mean the directors of my company are not required to deliver a copy of the individual accounts | subject: the name stated "my dormant subsidiary" as a given, but the function tests subsidiary, dormant and parent |
| 14 | Under section 448C(3), how much of the subsidiary's outstanding liabilities does the parent undertaking still guarantee, in pounds | Under section 448C(3), if a parent undertaking has given a guarantee under section 448C, how much of the subsidiary company's outstanding liabilities does it still guarantee, in pounds | subject: the name presupposed a guarantee, but the function tests whether one was given and answers NOTHING if not |
| 15 | Under section 448C(3), may I enforce the parent undertaking's guarantee against it | Under section 448C(3), may I enforce against a parent undertaking a guarantee under section 448C | subject: the name presupposed the parent undertaking's guarantee, but the function tests whether one was given |
| 16 | Under section 451(1), do I commit an offence as a director because the accounts and reports were not delivered in time | Under section 451(1), have I committed an offence in relation to the delivery of the company's accounts and reports before the end of the period for filing | subject: the name stated "as a director" and non-delivery as givens, but the function tests both |
| 17 | Under section 452(1), may the court order the directors to make good the default in filing | Under section 452(1), may the court order the directors to make good a default in filing the accounts and reports | subject: the name presupposed "the default", but the function tests whether there is one |
| 18 | Under section 452(2), may the court's order provide that the costs are borne by the directors | Under section 452(2), if the court makes an order under section 452(1), may the order provide that the costs are borne by the directors | subject: the name presupposed an order, but the function tests whether one was made |
| 19 | Under section 453(2), how many days late was the filing, for the late-filing penalty | Under section 453(2), how many days after the end of the period for filing were the accounts and reports delivered, for the civil penalty | subject: the function is the difference in days and does not test lateness (a negative number means early) |
| 20 | Under section 453(2), what is the amount of the company's civil penalty, in pounds | Under section 453(2), if the company is liable to a civil penalty, what is its amount, in pounds | subject: the name presupposed a penalty, but the function tests liability and answers NOTHING if there is none |
| 21 | Under section 453(3), may the registrar recover the civil penalty from the company | Under section 453(3), may the registrar recover a civil penalty under section 453 from the company | subject: the name presupposed the penalty, but the function tests liability |
| 22 | Under section 454(2), is the revision within the limit the section sets, now that copies of the previous accounts or report have gone out | Under section 454(2), are the revisions I am making confined to the correction of the respects in which the previous accounts or report did not comply and necessary consequential alterations | subject: the name stated "now that copies have gone out" as a given, but the function tests whether the confinement applies |
| 23 | Under section 455(3), is the period the Secretary of State's notice gives the directors long enough | Under section 455(3), does the notice specify a period of not less than one month for the directors | subject: "long enough" is looser than the one-month test the function applies |
| 24 | Under section 456(6), may the court exclude me from the order or order me to pay a different amount | Under section 456(6), where the court has made an order under section 456(5), may it exclude me from the order or order me to pay a different amount | subject: the name presupposed the order, but the function tests whether one was made |
| 25 | Under section 457(4), may proceedings be brought by or against the authorised association in the name of a body corporate | Under section 457(4), may proceedings brought in connection with the functions of an authorised person be brought by or against the authorised person in the name of a body corporate | subject: the name stated "the authorised association" as a given, but the function tests whether the authorised person is an unincorporated association |
| 26 | Under section 458(1), may the Commissioners for Her Majesty's Revenue and Customs disclose this information to a person authorised under section 457 | Under section 458(1), may the Commissioners for Her Majesty's Revenue and Customs disclose this information | subject: the name stated "to a person authorised under section 457" as a given, but the function tests it and the purpose |
| 27 | Under section 458(4), do I commit an offence by using or disclosing the information in a way section 458(3) bars | Under section 458(4), do I commit an offence by my use or further disclosure of information disclosed under section 458 | subject: the name stated "in a way section 458(3) bars" as a given, but the function tests whether the use or disclosure contravenes s 458(3) |
| 28 | Under section 459(4), may the authorised person apply to the court because I have not complied with a requirement | Under section 459(4), if a person fails to comply with a requirement under section 459(2), may the authorised person apply to the court | subject: the name stated the failure as a given ("because I have not complied"), but the function tests it |
| 29 | Under section 460(4), do I commit an offence by disclosing information in contravention of section 460 | Under section 460(4), do I commit an offence by disclosing information obtained under section 459 | subject: the name stated "in contravention of section 460" as a given, but the function tests whether the disclosure contravenes s 460 |
| 30 | Under section 463(2), is the director liable to compensate the company for its loss from a false or misleading report or statement | Under section 463(2), is the director liable to compensate the company for its loss from an untrue or misleading statement in, or an omission from, a report or statement | subject: the name asked only about a false or misleading report, but the function also answers the omission limb of s 463(2)(b) and (3)(b) |
| 31 | Under section 466(7), whose financial year are the subsidiary undertaking's figures taken from | Under section 466(7), on what date does the financial year of the subsidiary undertaking whose figures are used end | subject: the function returns the date the financial year ends, not whose year it is |

### Cases

`coa10-cases-seat.l4` has a case for every question: a yes and a no where the section has both, and a not-covered (NOTHING) case where some input can make the answer NOTHING.
A question has no NOTHING case when no input can make it NOTHING: its inputs are plain true or false and the section has no gap (found by running every combination of true and false inputs for the questions that take only true or false inputs, up to nine inputs, and by reading the others).
A question has no no case when the text only grants and is silent otherwise (s 442(5), s 448B, s 448C(3) enforcement, s 452(1), s 452(2), s 453(3), s 454(1), s 456(1), s 456(5) costs, s 457(4), s 458(6), s 459(4), s 461(3) and (4), s 469(2)).
A question has no yes case when the text only ever says no (s 451(3), s 453(4), s 459(6), s 459(7), s 463(4), s 463(6), s 467(4)) or when the part's fork makes a yes impossible (`Under section 448A(1)`, because of fork F9).
Every expected value was written down from the provision the question names before the file was run.

## Findings: what the text turns out to say (coa10)

1. The file prints two texts of s 444 (lines 5949-5982 and 5983-5993), of s 445(7), of s 446(5), and two daily default fines in s 451(4) (line 6128). Their exclusion lists differ: the first text of s 445(7) excludes companies within 444 and 444A, the second 443A and 444; the first text of s 446(5) excludes 444, 444A and 445, the second 443A, 444 and 445. Fork F1.
2. s 448B has no lead-in and no paragraph (a): it begins "(b) a company that—" (line 6102). Fork F9.
3. s 443 is not the library's month arithmetic: 30 April 2025 plus nine months is 31 January 2026 by s 443(3) (the last day of a month goes to the last day of the appropriate month) and 30 January 2026 by `add months`; both values were run on 1.6.110 and the first is asserted in `coa10-tests-period.l4`.
4. s 442(3) deals with a first accounting reference period of more than twelve months: the later of nine or six months from the first anniversary of incorporation and three months after the end of the period applies. Fork F3.
5. s 451(3) and s 453(4) say "It is not a defence ... to prove that the documents in question were not in fact prepared as required"; s 451(2) says "It is a defence ... to prove that he took all reasonable steps". The first two are flat negatives, the third a defence.
6. s 453(2) leaves the amount of the civil penalty to regulations: the encoding takes the amount as an input and encodes the number of days between the end of the period for filing and compliance (paragraph (a)).
7. s 458: the data-protection proviso is printed after "(2) This section applies despite any statutory or other restriction" (line 6225); the encoding applies it inside the s 458(1) function and quotes line 6225 there.
8. s 455(1) and (4) and s 456(1) carry elisions ("...") where words were omitted from the rendering; the encoding reads only the words shown.
9. s 465(4) adjusts only "the maximum figures for turnover" for a financial year that is not a year (line 6359), not the balance sheet total or the number of employees. Fork F8.
10. s 466(7): a subsidiary undertaking's figures are those of its financial year that ends with the parent company's, or else its financial year ending last before it; the encoding takes the latest year ending on or before the parent's year end, and NOTHING if there is none; "the latest available figures" (line 6387) is a type, with the judgment about expense or delay an input.
11. s 467(2)(c) says "(other than a small company)" and (d) "a small company that is an authorised insurance company, a banking company, ... a MiFID investment firm or a UCITS management company"; s 467(3) defines "small" by the last financial year ending on or before the end of the year in question.
12. s 474(1) "regulated activity" is the meaning in section 22 of the Financial Services and Markets Act 2000 "except that it does not include" the kinds specified in the articles listed in paragraphs (a) to (i) (lines 6522-6533); the encoding takes the kind of activity as an input and answers JUST FALSE for the kinds listed in paragraphs (a) to (i).
13. The text shows these units as blank or repealed ("..." or a row of dots): s 444(3A), (3B), (4); s 445(3), (4); s 446(1)(ba); s 448C(2)(c); ss 449 and 450; s 456(4)(b); s 463(1)(c); s 471(2)(ab); s 472(1); and two "..." entries of s 474(1) (lines 6511 and 6516).
14. s 454(2) and s 455(1)(b) put "(in the case of a public company)" after the last of three items. Fork F7.
15. The expected value for s 445(1) for a small company was first written NOTHING and corrected to JUST FALSE on rereading s 445(7) ("This section does not apply to companies within section 444"); the test file records the correction beside the assertion.
16. `s 459(4)` ("If a person fails to comply with such a requirement, the authorised person may apply to the court") is its own rule and has its own seat question, separate from the court's power in s 459(5).

## What the stable binary does not accept (coa10)

Observed on 1.6.110 (and the same counts on 1.6.109) while writing these files:
- A regulative rule's trace result (`FULFILLED` or `BREACH`) is printed by `#TRACE` but is not asserted: no assertion form for a trace result was available to me. Each of the three duties is therefore also a decision function (`s 441(1) the requirements were complied with before the end of the period for filing`, `s 448A(2)(e) the directors have delivered the documents within the period for filing`, `s 456(7) the applicant has complied`), and the decision functions are asserted. The traces of the three test files that hold regulative rules read the same on 1.6.110 and 1.6.109 (a crude comparison of the printed outcomes, `work/trace-*.txt`).
- A record built with `OF` needs commas between arguments when they are on separate lines; a missing comma is a type error that names the wrong argument.
- `WHERE name MEANS` with a long expression needs the expression indented on the next line.
- `NOT` is parenthesised everywhere (`NOT a AND b` is `NOT (a AND b)`), and every `#ASSERT` is on one line.
- `REFUSE`, `#ASSERT REFUSED`, `YMD` and `BECAUSE` (outside `LEST BREACH ... BECAUSE`) are not used; dates are `Date day month year`.
- The library `add months` clamps to the last day of a shorter month, so it is not s 443; s 443 is encoded explicitly (finding 3).
- `l4 check` printed no "is at the end of the file" or "follows code on its line" message for any file of this part (checked file by file).

## What check.sh printed (coa10)

Run in this folder as `L4=<L4_BIN> L4_MAIN=<L4_MAIN> ./check.sh` with `L4_BIN` the stable 1.6.110 build and `L4_MAIN` the 1.6.109 build, at the end of the pass:

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.109 (main, 4c887e0, 2026-11-04)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
coa-core.l4                                    0         0       0        0         0 |      0         0       0        0  same
coa-definitions.l4                             0         0       0        0         0 |      0         0       0        0  same
coa10-cases-seat.l4                            0       307       0        0         0 |      0       307       0        0  same
coa10-default.l4                               0         0       0        0         0 |      0         0       0        0  same
coa10-disclosure.l4                            0         0       0        0         0 |      0         0       0        0  same
coa10-exemptions.l4                            0         0       0        0         0 |      0         0       0        0  same
coa10-filing.l4                                0         0       0        0         0 |      0         0       0        0  same
coa10-meaning.l4                               0         0       0        0         0 |      0         0       0        0  same
coa10-medium.l4                                0         0       0        0         0 |      0         0       0        0  same
coa10-period.l4                                0         0       0        0         0 |      0         0       0        0  same
coa10-revision.l4                              0         0       0        0         0 |      0         0       0        0  same
coa10-seat.l4                                  0         0       0        0         0 |      0         0       0        0  same
coa10-supplementary.l4                         0         0       0        0         0 |      0         0       0        0  same
coa10-tests-default.l4                         0        60       0        0         0 |      0        60       0        0  same
coa10-tests-disclosure.l4                      0       108       0        0         0 |      0       108       0        0  same
coa10-tests-exemptions.l4                      0       112       0        0         0 |      0       112       0        0  same
coa10-tests-filing.l4                          0       217       0        0         0 |      0       217       0        0  same
coa10-tests-meaning.l4                         0        98       0        0         0 |      0        98       0        0  same
coa10-tests-medium.l4                          0       106       0        0         0 |      0       106       0        0  same
coa10-tests-period.l4                          0        79       0        0         0 |      0        79       0        0  same
coa10-tests-revision.l4                        0        81       0        0         0 |      0        81       0        0  same
coa10-tests-supplementary.l4                   0        41       0        0         0 |      0        41       0        0  same
coa10-types.l4                                 0         0       0        0         0 |      0         0       0        0  same
TOTAL (23 modules)                             0      1209       0        0           |      0      1209       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

`python3 -I srcrefs.py check --refs ../../../inputs/ukpga-2006-46.txt coa10-*.l4` and the same with `--strict` each printed `684 src: lines, 250 runs, 270 locators, 0 problems`.
The top-level names of the part (567 declarations, constructors, fields and functions) all begin with a section label, checked by script.
