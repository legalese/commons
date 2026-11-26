# Companies Act 1967 (Singapore), Part 6 Division 1 (ss 199 to 204) and the Twelfth Schedule: NOTES for `sgc1`

This is the NOTES.md of the part agent `sgc1` of a parallel encoding of the Act in L4 on the stable binary.
It covers lines 17849-19068 and 28897-29012 of `CoA1967.txt` and nothing else.
Status on 2026-11-18: layer 1, its tests, the seat layer and its cases are written and pass on both stable builds; the numbers `check.sh` printed are in the last section.
The section headings are the ones the brief names.

## Edition encoded

This encoding is of the Companies Act 1967 (Singapore), 2020 Revised Edition, in the Singapore Statutes Online informal consolidation "version in force from 6/5/2026 to 20/10/2026", retrieved 2026-10-09, which carries the amendments up to Act 24 of 2025.
A later consolidation may exist and was not read.
The encoding is of that text only: nothing in it comes from memory of the Act, from an earlier edition, or from any other Act, instrument or case.
The ranges are lines 17849-19068 and 28897-29012 of `CoA1967.txt`: Part 6 Division 1 (ss 199 to 204, with ss 200 and 200A shown repealed) and the Twelfth Schedule (the contents of the directors' statement).
Amendment marks such as `[36/2014]` are not text and are not quoted.
The words quoted in `-- src:` lines are copied from the file by script (`work/qgen.py`, outside the deposit), so that each line number is the file's own.

## Seat

The seat is an individual who is, or is about to become, a director, a company secretary or a member of a company incorporated under the Act, or who deals with one.
It is the seat of the brief (assumed, not ruled).
The Registrar, the Minister, the Authority and the Court have no seat: their powers appear only as what they mean to that individual (may the Registrar give me a notice, may the Court order costs against me, may the Registrar require this document).
The seat layer is `sgc1-seat.l4` (144 questions, each with `@export` and `@desc`, each named "Under section N," or "Under schedule 12 paragraph N,", grouped under `§` headings in the text's order) with its cases in `sgc1-cases-seat.l4`.
Every question calls exactly one layer-1 rule and passes its answer through unchanged; the seat never turns NOTHING into a no and never restates a rule.
Two kinds of input are reshaped and nothing else is: an optional number (the longer period the Registrar may allow, s 202B(2)) is asked as a number where 0 means none, and the result of s 201(12), (13) and (15A) is asked as the four facts those subsections turn on.
The amount in s 201A(5)(a)(ii) and (iii) is asked as a number, `the amount that applies, in Singapore dollars`, with a description that says it is $500,000 unless the Minister has prescribed another amount in substitution.
That follows the Guide's default (section 4): a number set by an instrument that is not among the sources is an input.
**Without that input the seat would answer the s 201A(5)(a) question on $500,000 even after a Ministerial substitution, and would say nothing about it.**
The regulative (DEONTIC) rules are not seat questions: the person asks "by when" through the last-day and in-time rules, and "what follows" through the offence and penalty rules.

### Direction of the seat questions' names

Each seat question was named from the layer-1 rule it calls, with the same direction: a question that asks "may", "must" or "has" calls a rule whose JUST TRUE is yes.
The questions whose rule is a bar or a "need not" are worded as the bar or the "need not" so that JUST TRUE reads the same way as the name.
Ten questions are worded that way, and each calls the layer-1 rule of the same wording (checked by reading the ten question bodies on 2026-11-18):

| question | JUST TRUE means |
| --- | --- |
| Under section 201(12), is it the case that the financial statements need not comply with the requirements of the Accounting Standards because the Registrar has approved? | TRUE: they need not comply |
| Under section 201(13), is it the case that the financial statements need not comply with a requirement of the Accounting Standards in order to give a true and fair view? | TRUE: they need not comply |
| Under section 201(17), is the representation that my company has a reserve barred? | TRUE: barred |
| Under section 201C(1), is it the case that the directors of a private company need not lay financial statements before the company at its annual general meeting? | TRUE: they need not lay |
| Under section 202(3), is the Registrar not barred from making an order under section 202(1)? | TRUE: not barred |
| Under section 202(4), has the order made under section 202(1) not ended? | TRUE: has not ended (still stands) |
| Under section 202A(4), are the directors barred from causing the financial statements to be revised? | TRUE: barred |
| Under section 202B(3), is it the case that the directors need take no further action on the notice? | TRUE: need take no further action |
| Under section 203A(3), is it the case that the company need not send the summary financial statement to the member? | TRUE: need not send |
| Under section 204(4), am I barred from being sentenced to imprisonment for the offence? | TRUE: barred (not wilful); JUST FALSE when the Court is of the opinion that the offence was committed wilfully |

## What is in the deposit

Everything is under `encodings/legalese-sonnet-5.5/`.
The keel's `sg-*.l4`, `check.sh`, `srcrefs.py` and `fetch-main-l4.sh` are the keel's and were not edited.

| file | lines | what it holds | assertions or traces |
| --- | --- | --- | --- |
| `sgc1-s199.l4` | 256 | layer 1: s 199: accounting records and systems of control, the offence of default; 16 functions | - |
| `sgc1-tests-s199.l4` | 129 | tests for `sgc1-s199` | 46 assertions, 8 traces |
| `sgc1-s201.l4` | 343 | layer 1: s 201(1) to (11): laying, compliance, audit, the directors' steps, the ultimate parent corporation; 20 functions | - |
| `sgc1-tests-s201.l4` | 155 | tests for `sgc1-s201` | 48 assertions, 12 traces |
| `sgc1-s201-departures.l4` | 153 | layer 1: s 201(12) to (15A): departures from the Accounting Standards and the Minister's orders; 7 functions | - |
| `sgc1-tests-s201-departures.l4` | 57 | tests for `sgc1-s201-departures` | 22 assertions, 0 traces |
| `sgc1-s201-statement.l4` | 213 | layer 1: s 201(16) to (23): the directors' statement, the reserve bar, banking corporations, charities, the 2015 savings; 12 functions | - |
| `sgc1-tests-s201-statement.l4` | 92 | tests for `sgc1-s201-statement` | 33 assertions, 6 traces |
| `sgc1-s201a.l4` | 379 | layer 1: s 201A (dormant companies exempt from s 201) and s 201AA (keeping the documents, inspection, offences); 21 functions | - |
| `sgc1-tests-s201a.l4` | 161 | tests for `sgc1-s201a` | 75 assertions, 4 traces |
| `sgc1-s201b.l4` | 336 | layer 1: s 201B (audit committees) and s 201C (directors who need not lay); 20 functions | - |
| `sgc1-tests-s201b.l4` | 171 | tests for `sgc1-s201b` | 55 assertions, 10 traces |
| `sgc1-s202.l4` | 490 | layer 1: s 202 (relief), s 202A (voluntary revision), s 202B (the Registrar's notice and application to Court); 24 functions | - |
| `sgc1-tests-s202.l4` | 201 | tests for `sgc1-s202` | 95 assertions, 3 traces |
| `sgc1-s203.l4` | 330 | layer 1: s 203 (members' entitlement to the statements, copies, offence, meeting on notice); 22 functions | - |
| `sgc1-tests-s203.l4` | 159 | tests for `sgc1-s203` | 65 assertions, 7 traces |
| `sgc1-s203a.l4` | 178 | layer 1: s 203A (summary financial statement); 11 functions | - |
| `sgc1-tests-s203a.l4` | 90 | tests for `sgc1-s203a` | 35 assertions, 4 traces |
| `sgc1-s204.l4` | 156 | layer 1: s 204 (penalty); 6 functions | - |
| `sgc1-tests-s204.l4` | 72 | tests for `sgc1-s204` | 30 assertions, 0 traces |
| `sgc1-sch12.l4` | 255 | layer 1: the Twelfth Schedule (contents of the directors' statement); 12 functions | - |
| `sgc1-tests-sch12.l4` | 115 | tests for `sgc1-sch12` | 54 assertions, 0 traces |
| `sgc1-seat.l4` | 1279 | layer 2: the seat, 144 questions with `@export` and `@desc` | - |
| `sgc1-cases-seat.l4` | 826 | cases for every seat question | 328 assertions |
| `NOTES.md`, `PROGRESS.md` | - | this file; the progress record | - |

Totals: 171 layer-1 functions (every one is named in at least one assertion or trace of its tests file, by script), 558 assertions and 54 traces in the layer-1 tests, 144 seat questions, 328 seat assertions.
The `.l4` files of layer 1 were generated from quote files by `work/qgen.py` (outside the deposit), which copies the quoted lines from the text by script so that every `-- src:` line number is the file's own; the files themselves are plain `.l4`.

## Where PLAN.md and the brief differ, and how this part read them

The brief governs where the two differ.
The differences found, each checked against the text or the plan file:

- PLAN.md's row for `sgc1` lists the keel's group functions `s 5(1) ...` and `s 5(4) ...` as names this part takes "for consolidated statements".
  The words "parent company", "subsidiary company", "subsidiary corporation", "group" and "ultimate parent corporation" are defined for Part 6 by s 209A ("In this Part, unless the contrary intention appears", line 20125), by reference to the Accounting Standards and not to s 5.
  This part therefore takes each of them as a plain fact input named for the fact (for example `the company is a parent company at the end of its financial year`), and calls one keel group function only (besides the keel's period functions): `s 4(1) "related corporation"` in `sg-groups.l4`, for s 201B(11), where the text speaks of a "related corporation" (s 6's term).
- PLAN.md cites a "section 7" (the seat layer) in four places (lines 17, 46, 612 and 619), and the file ends at section 6.
  This part followed the brief's seat rules, and could not follow a section it could not read.
- PLAN.md's seam table A says the giving part's seat "asks the same fact under the same name".
  This part's seat questions are named for the duty they ask about (`Under section 201(2), ...`), and each of the keel's seam facts is the answer of a layer-1 function here, not an input (see Seams).
- `inputs/XREFS.md` lists s 12 ("Registers") as cited at line 18172.
  That line cites "section 12(1)(f) of that Act", the Charities Act 1994, so the entry is a false hit of the script, which reads section numbers only; nothing from s 12 of this Act is used.

## Coverage (sgc1)

One row per unit of the two ranges: section, subsection, paragraph, sub-paragraph, schedule paragraph and sub-paragraph, plus one row for each heading or title.
Each row has exactly one disposition, and the table is generated by script from the text and from the layer-1 files, so a row's L4 names are the ones in the code.
A row whose provision has no function of its own says which row's rules encode it.

Counts: 223 rows.
`encoded`: 126.
`fork`: 68 (each row names its fork-register entries).
`inert`: 22 (16 with reason 1, not operative, headings and titles; 6 with reason 2, machinery, the regulation-making powers of s 202A(5) and s 203A(9); none with reason 3).
`repealed or blank in this text`: 7.

### Audit of the coverage table

Units counted in the text by two methods.
The first is the parser that builds the table (`work/covparse.py`): 207 unit rows (sections, subsections, paragraphs, sub-paragraphs, schedule paragraphs and sub-paragraphs) before any heading row was added, and 223 rows after the 16 heading and title rows were added.
The second is a separate count of line patterns in the raw text, which does not use the parser: 14 section starts (12 with a subsection (1), 2 shown repealed), 87 later subsections, 69 lettered paragraphs, 18 roman sub-paragraphs, 19 schedule paragraphs and sub-paragraphs.
The table's rows by depth: 99 subsections (the 12 first subsections plus the 87 later ones are 99), 69 paragraphs, 18 sub-paragraphs, 9 schedule paragraphs, 10 schedule sub-paragraphs, 2 repealed sections; the two methods agree on each.
Non-blank lines in the two ranges that fall in no row: 0.
The brief's word count for the ranges is 8475 (`inputs/PARTS.md`), and a count of the words on the same lines of the file gives 8475; the count includes the page furniture ("Informal Consolidation ..." and "2020 Ed. Companies Act 1967 N" lines), which lies inside rows and is quoted by none.

### Inert rows, with their reason numbers

Reason 1 (not operative): Part 6 and Division 1 headings (17849-17855); s 199 marginal heading (17857); s 201 marginal heading (17928); s 201A marginal heading (18214-18215); s 201AA marginal heading (18328-18329); s 201B marginal heading (18402); s 201C marginal heading (18502-18503); s 202 marginal heading (18527-18528); s 202A marginal heading (18577-18578); s 202B marginal heading (18672-18674); s 203 marginal heading (18824); s 203A marginal heading (18922); s 204 marginal heading (18993); Twelfth Schedule title, cross-reference line and heading (28897-28901); Twelfth Schedule running heading (continued, page 1) (28911-28915); Twelfth Schedule running heading (continued, page 2) (28965).
Reason 2 (machinery: a regulation-making power, Guide section 4): s 202A(5) (18637-18640); s 202A(5)(a) (18642-18644); s 202A(5)(b) (18646-18650); s 202A(5)(c) (18652-18662); s 202A(5)(d) (18664-18670); s 203A(9) (18987-18991).
Reason 3 (text shown repealed or blank) is not used: the seven such units have their own disposition below.

Repealed or blank in this text: s 200 (17924) shows `[Repealed by Act 36 of 2014]`; s 200A (17926) shows `[Repealed by Act 39 of 2007]`; s 201(3) (17945) shows `[Deleted by Act 15 of 2017]`; s 201(4) (17947-17950) shows `[Deleted by Act 15 of 2017]`; s 201(6) (17974) shows `[Deleted by Act 15 of 2017]`; s 201B(10) (18492) shows `[Deleted by Act 36 of 2014]`; s 203A(8) (18985) shows `[Deleted by Act 36 of 2014]`.

### The table

| unit | lines | disposition | where in the L4, or why not |
| --- | --- | --- | --- |
| Part 6 and Division 1 headings | 17849-17855 | inert | reason 1: not operative (a heading or title, no rule) |
| s 199 marginal heading | 17857 | inert | reason 1: not operative (a heading or title, no rule) |
| s 199(1) | 17859-17867 | encoded | sgc1-s199: `s 199(1) the company has caused the records to be kept as the subsection requires`, `s 199(1) a company must cause accounting and other records to be kept` |
| s 199(2) | 17869-17874 | encoded | sgc1-s199: `s 199(2) the last day of the period for which the company must retain the records`, `s 199(2) the subsection requires the company to retain the records on the day`, `s 199(2) a company must not dispose of the records within 5 years from the end of the financial year` |
| s 199(2A) | 17876-17879 | encoded | sgc1-s199: `s 199(2A) the company must devise and maintain a system of internal accounting controls`, `s 199(2A) the company has devised and maintained the system the subsection requires`, `s 199(2A) a public company or a subsidiary company of a public company must devise and maintain a system of internal accounting controls` |
| s 199(2A)(a) | 17881-17882 | encoded | encoded in the rules of the row for s 199(2A) |
| s 199(2A)(b) | 17884-17889 | encoded | encoded in the rules of the row for s 199(2A) |
| s 199(3) | 17891-17896 | encoded | sgc1-s199: `s 199(3) the records are kept as the subsection requires`, `s 199(3) the records must be open to inspection by the person`, `s 199(3) a company must keep its accounting records open to inspection by the directors` |
| s 199(4) | 17898-17905 | fork (F-duty-if) | sgc1-s199: `s 199(4) the company must send to and keep at a place in Singapore statements and returns`, `s 199(4) the company has complied with the subsection` |
| s 199(5) | 17907-17912 | encoded | sgc1-s199: `s 199(5) the Court may order the records to be open to inspection by the public accountant` |
| s 199(6) | 17914-17922 | fork (F-S1) | sgc1-s199: `s 199(6) the person is guilty of the offence this subsection creates`, `s 199(6) the most the person may be sentenced to on conviction`, `s 199(6) penalty` |
| s 200 | 17924 | repealed or blank in this text | the text shows `[Repealed by Act 36 of 2014]` |
| s 200A | 17926 | repealed or blank in this text | the text shows `[Repealed by Act 39 of 2007]` |
| s 201 marginal heading | 17928 | inert | reason 1: not operative (a heading or title, no rule) |
| s 201(1) | 17930-17934 | encoded | sgc1-s201: `s 201(1) the financial statements are the ones the directors must lay before the company at its annual general meeting`, `s 201(1) the directors of a company must lay the financial statements before the company at its annual general meeting` |
| s 201(2) | 17936-17943 | fork (F-201-2) | sgc1-s201: `s 201(2) the document complies with the Accounting Standards and gives a true and fair view` |
| s 201(3) | 17945 | repealed or blank in this text | the text shows `[Deleted by Act 15 of 2017]` |
| s 201(4) | 17947-17950 | repealed or blank in this text | the text shows `[Deleted by Act 15 of 2017]` |
| s 201(5) | 17952-17955 | fork (F-201-2) | sgc1-s201: `s 201(5) the directors need not comply with subsection (1) but must lay the consolidated financial statements and the balance sheet`, `s 201(5) the consolidated financial statements and the balance sheet are as the subsection requires`, `s 201(5) the directors of a parent company must cause to be made out and lay the consolidated financial statements and the balance sheet` |
| s 201(5)(a) | 17957-17960 | encoded | encoded in the rules of the row for s 201(5) |
| s 201(5)(b) | 17962-17972 | encoded | encoded in the rules of the row for s 201(5) |
| s 201(6) | 17974 | repealed or blank in this text | the text shows `[Deleted by Act 15 of 2017]` |
| s 201(7) | 17976-17978 | encoded | sgc1-s201: `s 201(7) the directors must take reasonable steps before the financial statements are made out` |
| s 201(7)(a) | 17980-17984 | encoded | sgc1-s201: `s 201(7)(a) the directors have taken the reasonable steps as to bad debts and doubtful debts` |
| s 201(7)(b) | 17986-17990 | encoded | sgc1-s201: `s 201(7)(b) the directors have taken the reasonable steps as to current assets` |
| s 201(7)(b)(i) | 17992-17993 | encoded | encoded in the rules of the row for s 201(7)(b) |
| s 201(7)(b)(ii) | 17995-18000 | encoded | encoded in the rules of the row for s 201(7)(b) |
| s 201(7)(c) | 18002-18013 | encoded | sgc1-s201: `s 201(7)(c) the directors have taken the reasonable steps as to non-current assets` |
| s 201(8) | 18015-18020 | encoded | sgc1-s201: `s 201(8) the financial statements have been audited and reported on as the subsection requires` |
| s 201(9) | 18022 | encoded | sgc1-s201: `s 201(9)(a) the latest day by which the financial statements are to be audited`, `s 201(9)(a) the financial statements have been audited in time`, `s 201(9)(a) the directors must take reasonable steps to ensure that the financial statements are audited not less than 14 days before the annual general meeting`, `s 201(9)(b) the directors have caused the auditor's report to be attached`, `s 201(9)(b) the directors must cause the auditor's report to be attached to the financial statements` |
| s 201(9)(a) | 18024-18031 | encoded | sgc1-s201: `s 201(9)(a) the latest day by which the financial statements are to be audited`, `s 201(9)(a) the financial statements have been audited in time`, `s 201(9)(a) the directors must take reasonable steps to ensure that the financial statements are audited not less than 14 days before the annual general meeting` |
| s 201(9)(b) | 18033-18037 | encoded | sgc1-s201: `s 201(9)(b) the directors have caused the auditor's report to be attached`, `s 201(9)(b) the directors must cause the auditor's report to be attached to the financial statements` |
| s 201(10) | 18039-18040 | encoded | sgc1-s201: `s 201(10) the documents that "financial statements" means in subsections (8) and (9)`, `s 201(10) the documents meant by financial statements` |
| s 201(10)(a) | 18042-18048 | encoded | encoded in the rules of the row for s 201(10) |
| s 201(10)(b) | 18050-18056 | encoded | encoded in the rules of the row for s 201(10) |
| s 201(11) | 18058-18065 | fork (F-duty-if) | sgc1-s201: `s 201(11) the directors must state the name of the ultimate parent corporation`, `s 201(11) the directors have stated the name of the ultimate parent corporation`, `s 201(11) the directors of a subsidiary company must state the name of its ultimate parent corporation` |
| s 201(12) | 18067-18075 | fork (F-exempt) | sgc1-s201-departures: `s 201(12) the financial statements need not comply with the requirements of the Accounting Standards` |
| s 201(13) | 18077-18086 | fork (F-exempt) | sgc1-s201-departures: `s 201(13) the financial statements need not comply with the requirement of the Accounting Standards` |
| s 201(14) | 18088-18091 | fork (F-duty-if) | sgc1-s201-departures: `s 201(14) the financial statements must include the statement, particulars and information the subsection lists`, `s 201(14) the financial statements include what the subsection requires` |
| s 201(14)(a) | 18093-18101 | encoded | encoded in the rules of the row for s 201(14) |
| s 201(14)(b) | 18103-18104 | encoded | encoded in the rules of the row for s 201(14) |
| s 201(14)(c) | 18106-18109 | encoded | encoded in the rules of the row for s 201(14) |
| s 201(15) | 18111-18118 | fork (F-exempt) | sgc1-s201-departures: `s 201(15) the substituted standards apply to the company in place of the Accounting Standards` |
| s 201(15A) | 18120-18127 | fork (F-exempt) | sgc1-s201-departures: `s 201(15A) the directors are exempt from having to ensure that the financial statements comply with the requirement` |
| s 201(16) | 18129-18136 | fork (F-16) | sgc1-s201-statement: `s 201(16) the financial statements are accompanied by the directors' statement the subsection requires`, `s 201(16) the directors must accompany the financial statements with a statement signed on their behalf by 2 directors`, `s 201(16) to (23) act` |
| s 201(17) | 18138-18143 | fork (F-other-than; F-unless) | sgc1-s201-statement: `s 201(17) the representation that the company has a reserve is barred`, `s 201(17) a company must not publish a document that represents that it has a reserve unless the representation is accompanied` |
| s 201(17)(a) | 18145-18150 | encoded | encoded in the rules of the row for s 201(17) |
| s 201(17)(b) | 18152-18156 | encoded | encoded in the rules of the row for s 201(17) |
| s 201(18) | 18158-18165 | encoded | sgc1-s201-statement: `s 201(18) the form and content provisions apply to the banking corporation as they stand` |
| s 201(19) | 18167-18175 | encoded | sgc1-s201-statement: `s 201(19) the Accounting Standards requirements apply to the charity as they stand` |
| s 201(20) | 18177-18183 | fork (F-transitional) | sgc1-s201-statement: `s 201(20) the documents are within a reference to the preceding financial statements` |
| s 201(21) | 18185-18193 | fork (F-transitional) | sgc1-s201-statement: `s 201(21) the laying of the documents is within a reference to the requirement to lay financial statements` |
| s 201(22) | 18195-18205 | fork (F-transitional) | sgc1-s201-statement: `s 201(22) subsection (16) applies to the company for the financial year`, `s 201(22) the earlier provisions of section 201 continue to apply to the company for the financial year` |
| s 201(23) | 18207-18212 | fork (F-transitional) | sgc1-s201-statement: `s 201(23) the company must attach a copy of the report prepared under section 201(5) as it then stood to the return`, `s 201(23) a company with an old financial year must attach a copy of the report to its return` |
| s 201A marginal heading | 18214-18215 | inert | reason 1: not operative (a heading or title, no rule) |
| s 201A(1) | 18217-18222 | fork (F-exempt) | sgc1-s201a: `s 201A(1) the directors are exempt from the requirements of section 201 for the financial year` |
| s 201A(2) | 18224 | encoded | sgc1-s201a: `s 201A(2) the requirements for the exemption are satisfied` |
| s 201A(2)(a) | 18226 | encoded | encoded in the rules of the row for s 201A(2) |
| s 201A(2)(a)(i) | 18228 | encoded | encoded in the rules of the row for s 201A(2) |
| s 201A(2)(a)(ii) | 18230 | encoded | encoded in the rules of the row for s 201A(2) |
| s 201A(2)(b) | 18232-18233 | encoded | encoded in the rules of the row for s 201A(2) |
| s 201A(2)(b)(i) | 18235-18236 | encoded | encoded in the rules of the row for s 201A(2) |
| s 201A(2)(b)(ii) | 18238-18239 | encoded | encoded in the rules of the row for s 201A(2) |
| s 201A(2)(b)(iii) | 18241-18243 | encoded | encoded in the rules of the row for s 201A(2) |
| s 201A(2)(c) | 18245-18249 | encoded | encoded in the rules of the row for s 201A(2) |
| s 201A(3) | 18251-18261 | encoded | sgc1-s201a: `s 201A(3) the relevant person may by written notice require the directors of the dormant relevant company to comply with section 201` |
| s 201A(4) | 18263 | encoded | sgc1-s201a: `s 201A(4) the person is a relevant person` |
| s 201A(4)(a) | 18265 | encoded | encoded in the rules of the row for s 201A(4) |
| s 201A(4)(b) | 18267-18269 | encoded | encoded in the rules of the row for s 201A(4) |
| s 201A(4)(c) | 18271-18275 | encoded | encoded in the rules of the row for s 201A(4) |
| s 201A(5) | 18277 | encoded | sgc1-s201a: `s 201A(5)(a) the company is a relevant company`, `s 201A(5)(a)(ii)(A) the amount the section states, in Singapore dollars`, `s 201A(5)(b) the relevant company is dormant` |
| s 201A(5)(a) | 18279 | encoded | sgc1-s201a: `s 201A(5)(a) the company is a relevant company` |
| s 201A(5)(a)(i) | 18281-18282 | encoded | encoded in the rules of the row for s 201A(5)(a) |
| s 201A(5)(a)(ii) | 18284-18290 | encoded | sgc1-s201a: `s 201A(5)(a)(ii)(A) the amount the section states, in Singapore dollars` |
| s 201A(5)(a)(iii) | 18292-18301 | encoded | encoded in the rules of the row for s 201A(5)(a) |
| s 201A(5)(b) | 18303-18309 | encoded | sgc1-s201a: `s 201A(5)(b) the relevant company is dormant` |
| s 201A(6) | 18311-18319 | fork (F-transitional) | sgc1-s201a: `s 201A(6) this section applies to the directors for the financial year`, `s 201A(6) the directors must prepare and lay the accounts under Part VI as it stood` |
| s 201A(7) | 18321-18326 | fork (F-transitional) | sgc1-s201a: `s 201A(7) the company must attach a copy of the accounts to the return`, `s 201A(7) a company with an old financial year must attach a copy of the accounts to its return` |
| s 201AA marginal heading | 18328-18329 | inert | reason 1: not operative (a heading or title, no rule) |
| s 201AA(1) | 18331-18333 | encoded | sgc1-s201a: `s 201AA(1) the last day of the period for which the company must keep the documents`, `s 201AA(1) the subsection requires the company to keep the documents on the day`, `s 201AA(1) the documents are kept at a place the subsection allows`, `s 201AA(1) a company must not dispose of the documents within 5 years` |
| s 201AA(1)(a) | 18335-18339 | encoded | encoded in the rules of the row for s 201AA(1) |
| s 201AA(1)(b) | 18341-18343 | encoded | encoded in the rules of the row for s 201AA(1) |
| s 201AA(1)(b)(i) | 18345 | encoded | encoded in the rules of the row for s 201AA(1) |
| s 201AA(1)(b)(ii) | 18347-18350 | encoded | encoded in the rules of the row for s 201AA(1) |
| s 201AA(1)(b) [second paragraph printed with the same label] | 18352-18364 | encoded | encoded in the rules of the row for s 201AA(1) |
| s 201AA(2) | 18366-18372 | fork (F-S1) | sgc1-s201a: `s 201AA(2) the person is guilty of the offence this subsection creates`, `s 201AA(2) the most the person may be sentenced to on conviction`, `s 201AA(2) penalty` |
| s 201AA(3) | 18374-18379 | encoded | sgc1-s201a: `s 201AA(3) the company may be required to furnish the document and the document may be inspected` |
| s 201AA(4) | 18381 | fork (F-S1) | sgc1-s201a: `s 201AA(4) the person is guilty of the offence this subsection creates`, `s 201AA(4) the most the person may be sentenced to on conviction` |
| s 201AA(4)(a) | 18383-18385 | encoded | encoded in the rules of the row for s 201AA(4) |
| s 201AA(4)(b) | 18387-18395 | encoded | encoded in the rules of the row for s 201AA(4) |
| s 201AA(5) | 18397-18400 | encoded | sgc1-s201a: `s 201AA(5) the person is an authorised officer` |
| s 201B marginal heading | 18402 | inert | reason 1: not operative (a heading or title, no rule) |
| s 201B(1) | 18404 | encoded | sgc1-s201b: `s 201B(1) the company must have an audit committee`, `s 201B(1) a listed company must have an audit committee` |
| s 201B(2) | 18406-18412 | fork (F-201B) | sgc1-s201b: `s 201B(2) the audit committee is appointed and composed as the subsection requires` |
| s 201B(2)(a) | 18414-18415 | encoded | encoded in the rules of the row for s 201B(2) |
| s 201B(2)(b) | 18417-18419 | encoded | encoded in the rules of the row for s 201B(2) |
| s 201B(2)(c) | 18421-18424 | encoded | encoded in the rules of the row for s 201B(2) |
| s 201B(3) | 18426-18428 | encoded | sgc1-s201b: `s 201B(3) the person is eligible to be elected chairperson of the audit committee` |
| s 201B(4) | 18430-18434 | fork (F-201B) | sgc1-s201b: `s 201B(4) the last day for the board of directors to appoint new members`, `s 201B(4) the board of directors has appointed new members in time`, `s 201B(4) the board of directors must within 3 months appoint new members to make up the minimum number` |
| s 201B(5) | 18436 | encoded | sgc1-s201b: `s 201B(5) the function is one of the functions of an audit committee`, `s 201B(5) function` |
| s 201B(5)(a) | 18438 | encoded | encoded in the rules of the row for s 201B(5) |
| s 201B(5)(a)(i) | 18440 | encoded | encoded in the rules of the row for s 201B(5) |
| s 201B(5)(a)(ii) | 18442-18443 | encoded | encoded in the rules of the row for s 201B(5) |
| s 201B(5)(a)(iii) | 18445 | encoded | encoded in the rules of the row for s 201B(5) |
| s 201B(5)(a)(iv) | 18447-18448 | encoded | encoded in the rules of the row for s 201B(5) |
| s 201B(5)(a)(v) | 18450-18451 | encoded | encoded in the rules of the row for s 201B(5) |
| s 201B(5)(a)(vi) | 18453-18460 | encoded | encoded in the rules of the row for s 201B(5) |
| s 201B(5)(b) | 18462-18468 | encoded | encoded in the rules of the row for s 201B(5) |
| s 201B(6) | 18470-18472 | encoded | sgc1-s201b: `s 201B(6) the auditor has the right to appear and be heard at any meeting of the audit committee`, `s 201B(6) the auditor must appear before the committee`, `s 201B(6) the auditor must appear before the committee when required to do so` |
| s 201B(7) | 18474-18477 | fork (F-duty-if) | sgc1-s201b: `s 201B(7) the chairperson must convene a meeting of the audit committee`, `s 201B(7) the chairperson must convene a meeting of the committee on the auditor's request` |
| s 201B(8) | 18479-18482 | encoded | sgc1-s201b: `s 201B(8) the audit committee may regulate the matter` |
| s 201B(9) | 18484-18490 | fork (F-duty-if) | sgc1-s201b: `s 201B(9) the directors must describe the audit committee's functions in the statement`, `s 201B(9) the directors' statement describes the audit committee's functions as the subsection requires`, `s 201B(9) the directors of a listed company must describe the audit committee's functions in the statement` |
| s 201B(10) | 18492 | repealed or blank in this text | the text shows `[Deleted by Act 36 of 2014]` |
| s 201B(11) | 18494-18500 | fork (F-201B) | sgc1-s201b: `s 201B(11) the director is an executive director` |
| s 201C marginal heading | 18502-18503 | inert | reason 1: not operative (a heading or title, no rule) |
| s 201C(1) | 18505-18515 | fork (F-exempt) | sgc1-s201b: `s 201C(1) the directors need not lay financial statements before the company at its annual general meeting` |
| s 201C(2) | 18517-18525 | encoded | sgc1-s201b: `s 201C(2) the reference in section 207(1) is read as a reference to the documents sent under section 203(1)` |
| s 202 marginal heading | 18527-18528 | inert | reason 1: not operative (a heading or title, no rule) |
| s 202(1) | 18530-18541 | fork (F-grant; F-other-than) | sgc1-s202: `s 202(1) the directors may apply to the Registrar in writing for an order relieving them from the requirement`, `s 202(1) the Registrar may make the order on condition that the directors comply with the other requirement`, `s 202(1) the directors are relieved by the Registrar's order from the requirement` |
| s 202(2) | 18543-18559 | fork (F-202-4) | sgc1-s202: `s 202(2) the directors are relieved by the Registrar's order for a class of companies from the requirement` |
| s 202(3) | 18561-18569 | encoded | sgc1-s202: `s 202(3) the Registrar is not barred from making an order under section 202(1)` |
| s 202(4) | 18571-18575 | fork (F-202-4) | sgc1-s202: `s 202(4) the order made under section 202(1) has not ended` |
| s 202A marginal heading | 18577-18578 | inert | reason 1: not operative (a heading or title, no rule) |
| s 202A(1) | 18580-18581 | encoded | sgc1-s202: `s 202A(1) the section applies` |
| s 202A(1)(a) | 18583-18590 | encoded | encoded in the rules of the row for s 202A(1) |
| s 202A(1)(b) | 18592-18597 | encoded | encoded in the rules of the row for s 202A(1) |
| s 202A(2) | 18599-18612 | fork (F-202A-2; F-grant) | sgc1-s202: `s 202A(2) the directors may cause the financial statements to be revised` |
| s 202A(3) | 18614-18616 | encoded | sgc1-s202: `s 202A(3) the revision is confined as the subsection requires` |
| s 202A(3)(a) | 18618-18621 | encoded | encoded in the rules of the row for s 202A(3) |
| s 202A(3)(b) | 18623-18625 | encoded | encoded in the rules of the row for s 202A(3) |
| s 202A(4) | 18627-18635 | fork (F-unless) | sgc1-s202: `s 202A(4) the directors are barred from causing the financial statements to be revised` |
| s 202A(5) | 18637-18640 | inert | reason 2: machinery (a regulation-making power, Guide section 4) |
| s 202A(5)(a) | 18642-18644 | inert | reason 2: machinery (a regulation-making power, Guide section 4) |
| s 202A(5)(b) | 18646-18650 | inert | reason 2: machinery (a regulation-making power, Guide section 4) |
| s 202A(5)(c) | 18652-18662 | inert | reason 2: machinery (a regulation-making power, Guide section 4) |
| s 202A(5)(d) | 18664-18670 | inert | reason 2: machinery (a regulation-making power, Guide section 4) |
| s 202B marginal heading | 18672-18674 | inert | reason 1: not operative (a heading or title, no rule) |
| s 202B(1) | 18676-18685 | fork (F-grant; F-202B-days) | sgc1-s202: `s 202B(1) the Registrar may give the directors a notice` |
| s 202B(2) | 18687-18689 | fork (F-202B-longer) | sgc1-s202: `s 202B(2) the number of days allowed for the response`, `s 202B(2) the last day for the directors to respond`, `s 202B(2) the directors responded by the end of the period`, `s 202B(2) the directors must respond to the Registrar's notice by the end of the period` |
| s 202B(2)(a) | 18691-18696 | fork (F-duty-if) | sgc1-s202: `s 202B(2)(a) the directors must give the Registrar an explanation of the financial statements` |
| s 202B(2)(b) | 18698-18707 | fork (F-202B-b) | sgc1-s202: `s 202B(2)(b) the directors must inform the Registrar how they propose to revise the financial statements` |
| s 202B(3) | 18709-18715 | fork (F-exempt) | sgc1-s202: `s 202B(3) the directors need take no further action on the notice` |
| s 202B(4) | 18717-18724 | fork (F-grant) | sgc1-s202: `s 202B(4) the directors may cause the financial statements to be revised in the manner agreed` |
| s 202B(5) | 18726 | fork (F-grant) | sgc1-s202: `s 202B(5) the Registrar may apply to Court under subsection (6)` |
| s 202B(5)(a) | 18728-18729 | encoded | encoded in the rules of the row for s 202B(5) |
| s 202B(5)(b) | 18731-18734 | encoded | encoded in the rules of the row for s 202B(5) |
| s 202B(5)(c) | 18736-18741 | encoded | encoded in the rules of the row for s 202B(5) |
| s 202B(6) | 18743-18744 | encoded | sgc1-s202: `s 202B(6) the application to Court may be for the relief` |
| s 202B(6)(a) | 18746-18749 | encoded | encoded in the rules of the row for s 202B(6) |
| s 202B(6)(b) | 18751-18758 | encoded | encoded in the rules of the row for s 202B(6) |
| s 202B(7) | 18760-18762 | fork (F-202B-7) | sgc1-s202: `s 202B(7) the Court may give directions on the matter`, `s 202B(7) matter of directions` |
| s 202B(7)(a) | 18764-18765 | encoded | encoded in the rules of the row for s 202B(7) |
| s 202B(7)(b) | 18767-18771 | encoded | encoded in the rules of the row for s 202B(7) |
| s 202B(7)(c) | 18773-18776 | encoded | encoded in the rules of the row for s 202B(7) |
| s 202B(7)(d) | 18778-18779 | encoded | encoded in the rules of the row for s 202B(7) |
| s 202B(7)(e) | 18781-18785 | encoded | encoded in the rules of the row for s 202B(7) |
| s 202B(7)(f) | 18787-18789 | encoded | encoded in the rules of the row for s 202B(7) |
| s 202B(8) | 18791-18794 | fork (F-grant) | sgc1-s202: `s 202B(8) the Court may order that the director bears all or part of the costs and expenses` |
| s 202B(8)(a) | 18796 | encoded | encoded in the rules of the row for s 202B(8) |
| s 202B(8)(b) | 18798-18812 | encoded | encoded in the rules of the row for s 202B(8) |
| s 202B(9) | 18814-18822 | encoded | sgc1-s202: `s 202B(9) the section applies to the statements as it applies to the first statements` |
| s 203 marginal heading | 18824 | inert | reason 1: not operative (a heading or title, no rule) |
| s 203(1) | 18826-18833 | encoded | sgc1-s203: `s 203(1) the company must send the documents to all persons entitled to receive notice of general meetings`, `s 203(1) the documents were sent in time`, `s 203(1) the company must send the documents by the last day` |
| s 203(1)(a) | 18835-18836 | fork (F-203-unless) | sgc1-s203: `s 203(1)(a) the last day for sending the documents` |
| s 203(1)(b) | 18838-18844 | encoded | sgc1-s203: `s 203(1)(b) the last day for sending the documents` |
| s 203(2) | 18846-18852 | fork (F-grant) | sgc1-s203: `s 203(2) the documents may be sent less than 14 days before the date of the meeting` |
| s 203(3) | 18854-18868 | fork (F-duty-if) | sgc1-s203: `s 203(3) the company must furnish the person without charge with a copy of the last financial statements and the auditor's report`, `s 203(3) the company must furnish a copy of the last financial statements on request` |
| s 203(3A) | 18870-18879 | fork (F-S1; F-unless; F-defence) | sgc1-s203: `s 203(3A) the subsection gives the person a defence on these facts`, `s 203(3A) the person is guilty of the offence this subsection creates`, `s 203(3A) the most the person may be sentenced to on conviction`, `s 203(3A) penalty` |
| s 203(4) | 18881-18887 | fork (F-203-4) | sgc1-s203: `s 203(4) the last day for the notice requiring a general meeting`, `s 203(4) the person may by notice require that a general meeting be held to lay the documents before the company` |
| s 203(4A) | 18889-18896 | fork (F-203-4A) | sgc1-s203: `s 203(4A) the person may by notice require that a general meeting be held to lay the documents before the company` |
| s 203(5) | 18898-18901 | encoded | sgc1-s203: `s 203(5) section 175A(5) applies, with the necessary modifications, to the giving of the notice` |
| s 203(6) | 18903-18910 | encoded | sgc1-s203: `s 203(6) the directors must convene a meeting for the purpose referred to in the notice`, `s 203(6) the last day for the directors to convene the meeting`, `s 203(6) the directors convened the meeting in time`, `s 203(6) the directors must within 14 days convene the meeting` |
| s 203(7) | 18912-18913 | fork (F-S1) | sgc1-s203: `s 203(7)(a) the person is guilty of the offence this paragraph creates`, `s 203(7)(a) the most the person may be sentenced to on conviction`, `s 203(7)(b) the Court may order a general meeting to be called`, `s 203(7)(a) penalty` |
| s 203(7)(a) | 18915-18917 | fork (F-S1) | sgc1-s203: `s 203(7)(a) the person is guilty of the offence this paragraph creates`, `s 203(7)(a) the most the person may be sentenced to on conviction`, `s 203(7)(a) penalty` |
| s 203(7)(b) | 18919-18920 | fork (F-203-7b; F-grant) | sgc1-s203: `s 203(7)(b) the Court may order a general meeting to be called` |
| s 203A marginal heading | 18922 | inert | reason 1: not operative (a heading or title, no rule) |
| s 203A(1) | 18924-18930 | encoded | sgc1-s203a: `s 203A(1) the company may send a summary financial statement instead of copies of the documents referred to in section 203(1)` |
| s 203A(2) | 18932-18938 | fork (F-203A-2) | sgc1-s203a: `s 203A(2) the person may instead request a summary financial statement` |
| s 203A(3) | 18940-18941 | fork (F-exempt) | sgc1-s203a: `s 203A(3) the company need not send the summary financial statement to the member` |
| s 203A(4) | 18943-18944 | encoded | sgc1-s203a: `s 203A(4) the company must send copies of the documents referred to in section 203(1) to the member`, `s 203A(4) the company must send copies of the documents to the member who wishes to receive them` |
| s 203A(5) | 18946-18951 | encoded | sgc1-s203a: `s 203A(5) the summary financial statement is derived and in the form the subsection requires` |
| s 203A(6) | 18953 | encoded | sgc1-s203a: `s 203A(6) the summary financial statement contains the statements the subsection requires` |
| s 203A(6)(a) | 18955-18960 | encoded | encoded in the rules of the row for s 203A(6) |
| s 203A(6)(b) | 18962-18969 | encoded | encoded in the rules of the row for s 203A(6) |
| s 203A(6A) | 18971-18975 | encoded | sgc1-s203a: `s 203A(6A) the directors have ensured that the summary financial statements comply with subsections (5) and (6)`, `s 203A(6A) the directors must ensure that the summary financial statements comply` |
| s 203A(7) | 18977-18983 | fork (F-S1; F-other-than) | sgc1-s203a: `s 203A(7) the person is guilty of the offence this subsection creates`, `s 203A(7) the most the person may be sentenced to on conviction`, `s 203A(7) penalty` |
| s 203A(8) | 18985 | repealed or blank in this text | the text shows `[Deleted by Act 36 of 2014]` |
| s 203A(9) | 18987-18991 | inert | reason 2: machinery (a regulation-making power, Guide section 4) |
| s 204 marginal heading | 18993 | inert | reason 1: not operative (a heading or title, no rule) |
| s 204(1) | 18995-19001 | fork (F-S1) | sgc1-s204: `s 204(1) the person is guilty of the offence this subsection creates` |
| s 204(1AA) | 19003-19007 | fork (F-S1) | sgc1-s204: `s 204(1AA) the person is guilty of the offence this subsection creates` |
| s 204(1A) | 19009 | fork (F-S1; F-other-than) | sgc1-s204: `s 204(1A) the person is guilty of the offence this subsection creates` |
| s 204(1A)(a) | 19011-19015 | fork (F-other-than) | sgc1-s204: `s 204(1A) the person is guilty of the offence this subsection creates` (within s 204(1A)) |
| s 204(1A)(b) | 19017-19018 | encoded | encoded in the rules of the row for s 204(1A) |
| s 204(1A)(c) | 19020-19027 | encoded | encoded in the rules of the row for s 204(1A) |
| s 204(2) | 19029-19040 | fork (F-defence) | sgc1-s204: `s 204(2) the subsection gives the person a defence on these facts` |
| s 204(3) | 19042-19044 | encoded | sgc1-s204: `s 204 the most the offender may be sentenced to on conviction`, `s 204 offence`, `s 204 penalty` (s 204 penalty rule) |
| s 204(3)(a) | 19046-19050 | encoded | sgc1-s204: `s 204 the most the offender may be sentenced to on conviction`, `s 204 offence`, `s 204 penalty` (s 204 penalty rule) |
| s 204(3)(aa) | 19052-19056 | encoded | sgc1-s204: `s 204 the most the offender may be sentenced to on conviction`, `s 204 offence`, `s 204 penalty` (s 204 penalty rule) |
| s 204(3)(b) | 19058-19060 | encoded | sgc1-s204: `s 204 the most the offender may be sentenced to on conviction`, `s 204 offence`, `s 204 penalty` (s 204 penalty rule) |
| s 204(4) | 19062-19067 | fork (F-unless) | sgc1-s204: `s 204(4) the person is barred from being sentenced to imprisonment for the offence` |
| Twelfth Schedule title, cross-reference line and heading | 28897-28901 | inert | reason 1: not operative (a heading or title, no rule) |
| sch 12 para 1 | 28902 | fork (F-sch12-verb) | sgc1-sch12: `sch 12 para 1 the statement contains the matters the paragraph requires` |
| sch 12 para 1(a) | 28904-28909 | encoded | encoded in the rules of the row for sch 12 para 1 |
| Twelfth Schedule running heading (continued, page 1) | 28911-28915 | inert | reason 1: not operative (a heading or title, no rule) |
| sch 12 para 1(b) | 28917-28918 | encoded | encoded in the rules of the row for sch 12 para 1 |
| sch 12 para 2 | 28920-28923 | fork (F-duty-if; F-other-than; F-sch12-verb) | sgc1-sch12: `sch 12 para 2 the statement must state the particulars of the option`, `sch 12 para 2 the statement states the particulars of the option` |
| sch 12 para 2(a) | 28925-28926 | encoded | encoded in the rules of the row for sch 12 para 2 |
| sch 12 para 2(b) | 28928 | encoded | encoded in the rules of the row for sch 12 para 2 |
| sch 12 para 2(c) | 28930 | encoded | encoded in the rules of the row for sch 12 para 2 |
| sch 12 para 2(d) | 28932-28934 | encoded | encoded in the rules of the row for sch 12 para 2 |
| sch 12 para 3 | 28936-28941 | fork (F-sch12-3) | sgc1-sch12: `sch 12 para 3 the particulars may be stated by reference to the earlier statement or report` |
| sch 12 para 4 | 28943-28947 | fork (F-duty-if) | sgc1-sch12: `sch 12 para 4 the directors' statement of the parent company must state the corporation and the other particulars`, `sch 12 para 4 the statement states the corporation and the other particulars` |
| sch 12 para 5 | 28949-28951 | fork (F-sch12-verb) | sgc1-sch12: `sch 12 para 5 the statement states the particulars of shares issued on the exercise of options` |
| sch 12 para 6 | 28953-28957 | fork (F-sch12-verb) | sgc1-sch12: `sch 12 para 6 the statement states the unissued shares under option` |
| sch 12 para 7 | 28959-28963 | fork (F-sch12-verb) | sgc1-sch12: `sch 12 para 7 the statement states the names of the directors in office` |
| Twelfth Schedule running heading (continued, page 2) | 28965 | inert | reason 1: not operative (a heading or title, no rule) |
| sch 12 para 8 | 28967-28969 | fork (F-duty-if; F-sch12-verb) | sgc1-sch12: `sch 12 para 8 the statement must also explain the effect of the arrangements and name the directors`, `sch 12 para 8 the statement states whether the arrangements subsisted and, if so, their effect` |
| sch 12 para 8(a) | 28971-28975 | encoded | encoded in the rules of the row for sch 12 para 8 |
| sch 12 para 8(b) | 28977-28983 | encoded | encoded in the rules of the row for sch 12 para 8 |
| sch 12 para 9 | 28985-28986 | fork (F-duty-if; F-sch12-verb) | sgc1-sch12: `sch 12 para 9 the statement states the director's interests in shares and debentures` |
| sch 12 para 9(a) | 28988-28995 | encoded | encoded in the rules of the row for sch 12 para 9 |
| sch 12 para 9(b) | 28997-29011 | encoded | encoded in the rules of the row for sch 12 para 9 |

## Fork register (sgc1)

Every ambiguity this part found, the readings seen, the one taken, and the text that licenses each.
A fork row in the coverage table names its entries here by id.
A fork is answered in the code with a comment that names its id, and the other reading is one edit away.

| id | where | readings | taken | licence: the text, and the Guide's own words where a ruling is relied on |
| --- | --- | --- | --- | --- |
| F-S1 | An unmet element of an offence (the facts do not satisfy one element): s 199(6), s 201AA(2), s 201AA(4), s 203(3A), s 203(7)(a), s 203A(7), s 204(1), s 204(1AA), s 204(1A); also the prohibition s 201(17). | (a) JUST FALSE: not guilty on these facts. (b) NOTHING: the text does not say. | JUST FALSE at all ten sites, answering the provision's own question. | "If default is made in complying with this section, the company and every officer of the company who is in default shall be guilty of an offence" (s 199(6)); "If any director of a company fails to comply with section 201(2) or (5), he or she shall be guilty of an offence" (s 204(1)). Guide 2026-11-04, "In short": a condition the text introduces with "if" answers JUST FALSE; grant ruling limit 2: JUST FALSE "for a bar, a duty or the provision's own question". |
| F-exempt | A relief that applies "if" or "where" a condition holds, when the condition fails: s 201(12), s 201(13), s 201(15), s 201(15A), s 201A(1), s 201C(1), s 202B(3), s 203A(3). | (a) JUST FALSE: the person is not relieved. (b) NOTHING: the relief is grant-like and the text does not say what follows. | JUST FALSE (reading (a) of the rule of 2026-10-29). | "need not comply with all or any of the requirements of the Accounting Standards ... if the company has obtained the approval of the Registrar" (s 201(12)); "need not comply with the requirement in section 201 ... if the company need not hold an annual general meeting because of section 175A(1)" (s 201C(1)). |
| F-202A-2 | s 202A(2) `the directors may cause the financial statements to be revised`: a "may" gated by "where" (and by "if it appears to the directors"). | (a) JUST FALSE when section 202A does not apply (periods ruling (b)). (b) NOTHING (grant ruling). | NOTHING for the "where" gate (S1b ruling, 2026S1bC, Guide line 101: the directors' own liberty to revise, no bar to relieve); NOTHING for the "if it appears" gate (see F-grant). | "Where this section applies, if it appears to the directors of the company that the financial statements ... do not comply with the requirements of this Act ..., the directors may cause the financial statements ... to be revised". Split site (ii); the Guide's words relied on: Guide section 5, periods ruling of 2026-11-05, item (b): "a "where ..." condition: when it fails the answer is `JUST FALSE`"; delegated-definitions ruling of 2026-11-05, item (c): ""when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above"; grant ruling of 2026-11-12, limit 3: "do not change, but list in the row's fork register ... a "may" function whose gate is "where", "when" or "upon"". |
| F-202B-7 | s 202B(7) `the Court may give directions on the matter`: a "may" gated by "where". | (a) JUST FALSE when the Court has not ordered revised statements (periods ruling (b)). (b) NOTHING. | JUST FALSE; every listed matter is open once the Court has ordered, because paragraph (f) ("such other matters as the Court thinks fit") makes the list of (a) to (e) illustrative, so the matter input never changes the answer. | "Where the Court orders the preparation of revised financial statements, or consolidated financial statements or balance sheet, under subsection (6), it may give directions as to —". Split site (ii); the Guide's words relied on: Guide section 5, periods ruling of 2026-11-05, item (b): "a "where ..." condition: when it fails the answer is `JUST FALSE`"; delegated-definitions ruling of 2026-11-05, item (c): ""when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above"; grant ruling of 2026-11-12, limit 3: "do not change, but list in the row's fork register ... a "may" function whose gate is "where", "when" or "upon"". |
| F-203-4A | s 203(4A) `the person may by notice require that a general meeting be held ...`: a "may" gated by "where". | (a) JUST FALSE when the company is not within s 175A(1)(b). (b) NOTHING. | JUST FALSE. | "Where a company is not required to hold an annual general meeting because of section 175A(1)(b), any member or auditor of the company may, by notice to the company not later than 14 days after the day on which the documents referred to in subsection (1) were sent out, require that a general meeting be held". Split site (ii); the Guide's words relied on: Guide section 5, periods ruling of 2026-11-05, item (b): "a "where ..." condition: when it fails the answer is `JUST FALSE`"; delegated-definitions ruling of 2026-11-05, item (c): ""when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above"; grant ruling of 2026-11-12, limit 3: "do not change, but list in the row's fork register ... a "may" function whose gate is "where", "when" or "upon"". |
| F-203-4 | s 203(4) the same power "In a case referred to in subsection (1)(b)": a "may" gated by a case reference, not by the word "where". | (a) NOTHING: a grant limited in its own wording. (b) JUST FALSE, as for "where". | NOTHING outside the case or the persons; JUST FALSE after the 14 days. | "In a case referred to in subsection (1)(b), any member or auditor of the company may, by notice to the company not later than 14 days after the day on which the documents referred to in subsection (1) were sent out, require that a general meeting be held". Guide 2026-11-04, "In short": NOTHING where the text "limits a grant or prohibition in its own wording and the case falls outside the limit". |
| F-203-7b | s 203(7)(b) `the Court may order a general meeting to be called`: a "may" gated by "If default is made" and by "on application of the member or auditor". | (a) JUST FALSE when no application is made ("on application" counted as "upon", delegated-definitions ruling (c), then periods ruling (b)). (b) NOTHING (grant ruling). | NOTHING where no default is made (an `if` gate on a grant, F-grant); JUST FALSE where default is made and no application is. | "the Court may, on application of the member or auditor, order a general meeting to be called". Split site (ii); the Guide's words relied on: Guide section 5, periods ruling of 2026-11-05, item (b): "a "where ..." condition: when it fails the answer is `JUST FALSE`"; delegated-definitions ruling of 2026-11-05, item (c): ""when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above"; grant ruling of 2026-11-12, limit 3: "do not change, but list in the row's fork register ... a "may" function whose gate is "where", "when" or "upon"". |
| F-203A-2 | s 203A(2) `the person may instead request a summary financial statement`: a "may" gated by "where". | (a) JUST FALSE when the company has sent no summary under subsection (1) (periods ruling (b)). (b) NOTHING. | JUST FALSE; NOTHING for anyone who is not a member or debenture holder entitled to a copy under s 203(3). | "Where a company sends to its members a summary financial statement under subsection (1), any member of the company, and any holder of a debenture, entitled to be furnished by the company with a copy of the documents referred to in section 203(3) may instead request for a summary financial statement". Split site (ii); the Guide's words relied on: Guide section 5, periods ruling of 2026-11-05, item (b): "a "where ..." condition: when it fails the answer is `JUST FALSE`"; delegated-definitions ruling of 2026-11-05, item (c): ""when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above"; grant ruling of 2026-11-12, limit 3: "do not change, but list in the row's fork register ... a "may" function whose gate is "where", "when" or "upon"". |
| F-sch12-3 | sch 12 para 3 `the particulars may be stated by reference to the earlier statement or report`: a "may" gated by "where". | (a) JUST FALSE when the particulars have not been stated before (periods ruling (b)). (b) NOTHING. | JUST FALSE. | "Where any of the particulars required by paragraph 2 have been stated in a previous directors' statement, or a previous directors' report ..., they may be stated by reference to that statement or report". Split site (ii); the Guide's words relied on: Guide section 5, periods ruling of 2026-11-05, item (b): "a "where ..." condition: when it fails the answer is `JUST FALSE`"; delegated-definitions ruling of 2026-11-05, item (c): ""when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above"; grant ruling of 2026-11-12, limit 3: "do not change, but list in the row's fork register ... a "may" function whose gate is "where", "when" or "upon"". |
| F-203-unless | s 203(1)(a) `the documents were sent in time`: "unless subsection (2) applies", once (2) applies. | (a) TRUE on or before the meeting and NOTHING after it (the text sets no other day). (b) JUST FALSE for less than 14 days. (c) no deadline at all. | TRUE on or before the date of the meeting, NOTHING after it. | "(a) unless subsection (2) applies — not less than 14 days before the date of the meeting"; "may be sent less than 14 days before the date of the meeting as required under subsection (1)(a) if all the persons entitled to receive notice of general meetings of the company so agree". Guide 2026-11-05: an "unless" or "except" once it is met is one of the six decided case by case. |
| F-unless | An "unless" once it is met: s 202A(4) (unless the Registrar agrees), s 203(3A) (unless it is proved ...), s 204(4) (unless wilful), s 201(17) (unless the representation is accompanied). | (a) JUST FALSE for the bar or the guilt (the bar no longer applies). (b) NOTHING. | JUST FALSE. | "the directors may not cause the financial statements ... to be revised unless the Registrar agrees"; "shall, unless it is proved that ..., each be guilty of an offence"; "shall not be sentenced to imprisonment ... unless in the opinion of the Court ... the offence was committed wilfully". |
| F-defence | A defence "to prove": s 203(3A) and s 204(2). | Per the ruling: JUST FALSE for that provision's defence when it is not proved. | JUST FALSE, worded "the subsection gives the person a defence on these facts". | Guide 2026-11-05, delegated definitions, defences and "until" bars (b): "when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"". |
| F-duty-if | A duty whose "if", "where", "upon" or "and if so" is unmet (a "must" function, not a grant): s 199(4), s 201(11), s 201(14), s 201B(7), s 201B(9), s 202B(2)(a), s 203(3) ("on a request"), sch 12 paras 2, 4, 8 and 9. | (a) JUST FALSE: the duty does not arise. (b) NOTHING: the text does not say. | JUST FALSE for the "must" function; NOTHING for the companion "has complied" function when the duty does not arise. | "Where at the end of a financial year a company is the subsidiary company of another corporation, the directors of the company must state ..." (s 201(11)); "Upon the request of the auditor, the chairperson of the audit committee must convene a meeting" (s 201B(7)). Guide 2026-11-05: periods ruling (b), and delegated-definitions ruling (c) for "upon" and "when"; 2026-11-05 list of six: "a duty whose `if` or `where` is unmet". |
| F-other-than | "(other than X)": s 201(17), s 202(1), s 204(1A)(a), s 203A(7), sch 12 para 2. | (a) JUST FALSE where X is the case (a bar or offence the parenthesis takes out: s 201(17), s 204(1A), s 203A(7), sch 12 para 2). (b) NOTHING. | JUST FALSE at those four sites; NOTHING at s 202(1), where the parenthesis limits a grant ("(other than a requirement of the Accounting Standards)") and the case falls outside it. | Guide 2026-11-05 list of six: "'(other than X)'". |
| F-grant | A function named for a grant or a power whose `if` gate failed (grant ruling of 2026-11-12, limit 1): one line per site, below. | (a) NOTHING (limit 1). (b) JUST FALSE. | NOTHING at every site below. | Guide, grant ruling, limit 1: "answer `NOTHING`, with one fork line each, only for a function named for a grant or a power ("may", "is permitted to", "has power to") whose `if` gate failed". |
| F-202B-days | s 202B(1) and (2): the Registrar "specif[ies] the period within which the directors must respond"; the text gives no unit. | days, weeks, months. | a number of days, an input. | "specify the period within which the directors must respond" (s 202B(1)). |
| F-202B-longer | s 202B(2): "such longer period as the Registrar may allow". | (a) a total counted from the notice. (b) an extension added to the first period. | (a): the allowed number of days is the larger of the first and the longer period. | "at the end of the period mentioned in subsection (1), or such longer period as the Registrar may allow". |
| F-202B-b | s 202B(2)(b) `the directors must inform the Registrar how they propose to revise ...` for directors who do not propose to revise. | (a) NOTHING: paragraph (b) states no condition of its own and paragraph (a) covers them. (b) JUST FALSE. | NOTHING. | "(a) give the Registrar an explanation ..., if the directors do not propose to revise ...; or (b) inform the Registrar how the directors propose to revise". |
| F-201B | s 201B(2), (4), (11): "a majority must not be" (more than half), "the board of directors must" (a collective), "in conjunction with". | see Marginal readings M5 to M7. | M5 to M7. | "must be composed of 3 or more members of whom a majority must not be"; "the board of directors must, within 3 months of that event, appoint such number of new members". |
| F-202-4 | s 202(4) applies to "an order under subsection (1)" only: how long a class order under subsection (2) lasts is not said. | (a) NOTHING: the text does not say. (b) the same limits as (1) orders. | (a): the class-order function has no period input. | "The Registrar may make an order under subsection (1) which may be limited to a specific period and may from time to time ... revoke or suspend the operation of any such order". |
| F-201-2 | s 201(2) and (5): the duty to comply with the Accounting Standards is "Subject to subsections (12) to (15A)". | (a) JUST FALSE for a document that does not comply when no departure is allowed. (b) NOTHING. | (a), through the composite `s 201(12), (13) and (15A) a departure from the Accounting Standards is allowed`. | "Subject to subsections (12) to (15A), the financial statements ... must comply with the requirements of the Accounting Standards". |
| F-16 | s 201(16) "signed on behalf of the directors by 2 directors". | at least 2; exactly 2. | at least 2. | "by a statement signed on behalf of the directors by 2 directors of the company". |
| F-sch12-verb | sch 12 paras 1, 2, 5, 6, 7, 8, 9 have no verb ("A statement as to whether ...", "The particulars of shares issued ..."). | (a) each lists what the statement must contain, so an omission is JUST FALSE. (b) the paragraph states no duty and an omission is NOTHING. | (a), reading the Schedule with s 201(16): "containing the information set out in the Twelfth Schedule". | s 201(16): "by a statement signed on behalf of the directors by 2 directors of the company containing the information set out in the Twelfth Schedule". |
| F-transitional | s 201(20) to (23) and s 201A(6) and (7) (financial years that ended before 1 July 2015 or before 3 January 2016) are encoded, not left inert. | (a) inert, reason 2 (savings that affect no one now). (b) encoded. | (b): a late return for an old financial year can still be filed, so someone can still be affected. | "Without limiting section 197(2), a company referred to in subsection (22) ... must attach a copy of the report" (s 201(23), s 201A(7) likewise). |

### Grant sites: a function named for a grant or a power whose `if` gate failed (F-grant)

The grant ruling of 2026-11-12, limit 1, asks for one fork line each.
9 sites answer `NOTHING`; the other reading is `JUST FALSE`.

| provision | function | when the gate fails | the text's own limit |
| --- | --- | --- | --- |
| s 202(1) | `the Registrar may make the order on condition that the directors comply with the other requirement` | the requirement is not about the form and content of the statements, or the Registrar does not think it fit | grant limited to "such other requirements ... as the Registrar thinks fit to impose" |
| s 202(1) | `the directors may apply to the Registrar in writing for an order relieving them from the requirement` | a requirement of the Accounting Standards, or not about form and content | grant limited by "(other than a requirement of the Accounting Standards)" (F-other-than) |
| s 202A(2) | `the directors may cause the financial statements to be revised` (second gate) | it does not appear to the directors that the statements fail to comply | "if it appears to the directors" |
| s 202B(1) | `the Registrar may give the directors a notice` | it does not appear to the Registrar that there is, or may be, a question | "If it appears to the Registrar that there is, or may be, a question" |
| s 202B(4) | `the directors may cause the financial statements to be revised in the manner agreed` | the Registrar does not agree on the manner (s 202A(4) is what bars the revision) | "If the Registrar agrees with the directors on the manner" |
| s 202B(5) | `the Registrar may apply to Court under subsection (6)` | none of the three cases holds | "The Registrar may apply to Court under subsection (6) if —" |
| s 202B(8) | `the Court may order that the director bears all or part of the costs and expenses` | no finding of non-compliance, or the person was not a director as at the date of the directors' statement | "If the Court finds that the financial statements ... did not comply" |
| s 203(2) | `the documents may be sent less than 14 days before the date of the meeting` | not all the persons entitled to receive notice agree | "if all the persons entitled to receive notice of general meetings of the company so agree" |
| s 203(7)(b) | `the Court may order a general meeting to be called` (first gate) | no default is made in convening the meeting | "If default is made in convening the meeting under subsection (6)" |

The brief's second group for the fork register is the "entitled"-named functions (a claim, not a power), which limit 3 says to list and leave.
No function in layer 1 is named "entitled".
One function is named for a right: `s 201B(6) the auditor has the right to appear and be heard at any meeting of the audit committee`.
It answers `NOTHING` for a person who is not "the auditor" (limited by its own wording) and never answers `JUST FALSE`, so its branch is the one the ruling leaves open and the other reading is `JUST FALSE` outside the limit.
`s 203(3) the company must furnish the person without charge with a copy ...` and `s 203A(4) the company must send copies ... to the member who wishes to receive them` are duties of the company that give a member or debenture holder a claim, and are answered under the duty rows of the fork register (F-duty-if).

### Modelling choices that are not forks (assumed, not ruled)

A regulative rule takes its time limit as a number of days from the start of the trace, and the last-day functions say which day the number must be.
A duty to keep or retain for a period (s 199(2), s 201AA(1)) is a `SHANT` on disposal for that period, with a `MAYBE BOOLEAN` function that says whether the duty holds on a given day.
A penalty provision is a record function: the highest fine, the longest imprisonment in months (0 where the text gives none), whether the court may impose both, and whether a default penalty also applies.
A judgment the text hands to the Registrar, the Minister, the Court, the Monetary Authority or the board of directors is a plain yes/no input, never guessed (the Guide's default, section 4).

### The Guide's rulings, word for word

The brief asks that each ruling be recorded again, word for word, in the NOTES.md of each row that carries that rule's `NOTHING-kind` tags.
The rulings below are copied by script from `inputs/ENCODING-GUIDE.md`, section 5, "Rulings on negatives and legal effects (ruled 2026-11-04)", with line breaks only between sentences.
Ruling E1 (gathering a legal effect's routes) is not copied: no row of this Division uses it.

**In short (2026-11-04)**, `inputs/ENCODING-GUIDE.md` lines 86-87:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").
> Everywhere else it answers `NOTHING`: where the text lists without closing the list, says "includes", leaves a term undefined, is silent, points outside the sources, or limits a grant or prohibition in its own wording and the case falls outside the limit.

**N2 (flat negatives)**, `inputs/ENCODING-GUIDE.md` lines 92-92:

> **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said.
> the maintainer's lean, verbatim: "Why are we even trying to do this work?
> Some of these rules are metatextual and require more homoiconicity than we currently have in L4."
> the maintainer's note: none written.
> Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04.
> Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23

**Periods, "where" and scope limits (2026-11-05)**, `inputs/ENCODING-GUIDE.md` lines 93-93:

> **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`.
> the maintainer's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c."
> Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

**Delegated definitions, defences and "until" bars (2026-11-05)**, `inputs/ENCODING-GUIDE.md` lines 94-94:

> **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed.
> the maintainer approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace."
> The note is a request about how (d) is modelled, not part of the ruling.
> Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

**Questions with no convention: decide case by case (2026-11-05)**, `inputs/ENCODING-GUIDE.md` lines 95-95:

> **Questions with no convention: decide case by case (the maintainer, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger.
> Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover.
> the maintainer's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with the coordinator where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still?
> In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in."
> The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

**Functions named for a grant or a power (2026-11-12)**, `inputs/ENCODING-GUIDE.md` lines 96-100:

> **Functions named for a grant or a power (ruled by the coordinating session of the UK and Canada encodings on 2026-11-12; not confirmed by the maintainer).** A function named for a grant or a power ("the court may ...", "the registrar may ...") that answers `JUST FALSE` because an `if` gate failed reads as "may not": a grant turned into a bar.
> The ruling sets three limits:
> 1. answer `NOTHING`, with one fork line each, only for a function named for a grant or a power ("may", "is permitted to", "has power to") whose `if` gate failed;
> 2. keep `JUST FALSE` where the text closes the gate itself ("only if", "only where", "may not ... unless", a list closed with "only"), and for a bar, a duty or the provision's own question;
> 3. do not change, but list in the row's fork register for the maintainer or a lawyer, a "may" function whose gate is "where", "when" or "upon" (ruling (b) of the periods ruling above says `JUST FALSE`, and the "In short" line on grants points the other way), and an "entitled"-named function (an entitlement is a claim, not a power, and this guide does not settle it).
> The ruling and the counts it produced are recorded in `subjects/uk/companies-act-2006/encodings/legalese-sonnet-5.5/NOTES.md`, section "The grant and power name test".

## Split sites (sgc1)

The brief asks for a count of two kinds of site and the answer taken at each, with the fork line and the Guide's own words that the answer relies on.
(i) is an unmet element of an offence: the facts do not satisfy one element, and the function answers either `JUST FALSE` (not guilty on these facts) or `NOTHING` (the text does not say).
(ii) is a "may" gated by "where", "when" or "upon": the grant ruling of 2026-11-12, limit 3, says do not change the answer the periods ruling gives, and list the site.
A "may" whose gate the text closes itself ("only upon", "may not ... unless", a proviso) is not a split site; it is answered `JUST FALSE` under limit 2 and listed below so the difference is visible.

### (i) An unmet element of an offence

Ten sites: nine offence functions and the bar of s 201(17), whose unmet element (the representation, or the missing accompaniment) is the same kind.
Answer taken at all ten: `JUST FALSE`, worded as "not guilty on these facts" or "not barred".
Other reading: `NOTHING`.
Fork line: F-S1, in the register above.
The Guide's words relied on: Guide section 5, rulings of 2026-11-04, "In short": a function answers `JUST FALSE` where the text says no "in its own words: ... a condition the text introduces with "if", "only if", "as long as" or "unless""; and the grant ruling of 2026-11-12, limit 2: "keep `JUST FALSE` ... for a bar, a duty or the provision's own question".

| provision | function | answer taken | other reading | fork |
| --- | --- | --- | --- | --- |
| s 199(6) | `s 199(6) the person is guilty of the offence this subsection creates` | JUST FALSE | NOTHING | F-S1 |
| s 201AA(2) | `s 201AA(2) the person is guilty of the offence this subsection creates` | JUST FALSE | NOTHING | F-S1 |
| s 201AA(4) | `s 201AA(4) the person is guilty of the offence this subsection creates` | JUST FALSE | NOTHING | F-S1 |
| s 203(3A) | `s 203(3A) the person is guilty of the offence this subsection creates` | JUST FALSE | NOTHING | F-S1 |
| s 203(7)(a) | `s 203(7)(a) the person is guilty of the offence this paragraph creates` | JUST FALSE | NOTHING | F-S1 |
| s 203A(7) | `s 203A(7) the person is guilty of the offence this subsection creates` | JUST FALSE | NOTHING | F-S1 |
| s 204(1) | `s 204(1) the person is guilty of the offence this subsection creates` | JUST FALSE | NOTHING | F-S1 |
| s 204(1AA) | `s 204(1AA) the person is guilty of the offence this subsection creates` | JUST FALSE | NOTHING | F-S1 |
| s 204(1A) | `s 204(1A) the person is guilty of the offence this subsection creates` | JUST FALSE | NOTHING | F-S1 |
| s 201(17) | `s 201(17) the representation that the company has a reserve is barred` | JUST FALSE | NOTHING | F-S1 |

### (ii) A "may" gated by "where", "when" or "upon"

Seven sites: 5 answer `JUST FALSE` (the periods ruling) and 2 answer `NOTHING` (s 203(4), whose gate is a case reference and not one of the three words; and s 202A(2), by the S1b ruling, 2026S1bC, Guide line 101).
Under limit 3 the five `JUST FALSE` answers are not changed and are listed here and in the fork register for the maintainer or a lawyer.
The other reading at each of the five is `NOTHING`, since the "In short" line on grants points that way.

| provision | function | the gate | answer taken | other reading | fork | Guide's words relied on |
| --- | --- | --- | --- | --- | --- | --- |
| s 202A(2) | `s 202A(2) the directors may cause the financial statements to be revised` | "Where this section applies" | NOTHING when the section does not apply (S1b ruling, 2026S1bC: the directors' own liberty to revise, no bar to relieve; Guide line 101, which replaces limit 3 for this site) | JUST FALSE | F-202A-2 | The other reading rests on Guide section 5, periods ruling of 2026-11-05, item (b): "a "where ..." condition: when it fails the answer is `JUST FALSE`"; delegated-definitions ruling of 2026-11-05, item (c): ""when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above"; grant ruling of 2026-11-12, limit 3: "do not change, but list in the row's fork register ... a "may" function whose gate is "where", "when" or "upon"". |
| s 202B(7) | `s 202B(7) the Court may give directions on the matter` | "Where the Court orders the preparation of revised financial statements ... under subsection (6)" | JUST FALSE when the Court has not so ordered | NOTHING | F-202B-7 | Guide section 5, periods ruling of 2026-11-05, item (b): "a "where ..." condition: when it fails the answer is `JUST FALSE`"; delegated-definitions ruling of 2026-11-05, item (c): ""when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above"; grant ruling of 2026-11-12, limit 3: "do not change, but list in the row's fork register ... a "may" function whose gate is "where", "when" or "upon"". |
| s 203(4A) | `s 203(4A) the person may by notice require that a general meeting be held to lay the documents before the company` | "Where a company is not required to hold an annual general meeting because of section 175A(1)(b)" | JUST FALSE for a company outside s 175A(1)(b) | NOTHING | F-203-4A | Guide section 5, periods ruling of 2026-11-05, item (b): "a "where ..." condition: when it fails the answer is `JUST FALSE`"; delegated-definitions ruling of 2026-11-05, item (c): ""when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above"; grant ruling of 2026-11-12, limit 3: "do not change, but list in the row's fork register ... a "may" function whose gate is "where", "when" or "upon"". |
| s 203(7)(b) | `s 203(7)(b) the Court may order a general meeting to be called` | "on application of the member or auditor" ("upon"); the other gate, "If default is made in convening the meeting", is an `if` and is answered NOTHING (F-grant) | JUST FALSE when default is made and no application is | NOTHING | F-203-7b | Guide section 5, periods ruling of 2026-11-05, item (b): "a "where ..." condition: when it fails the answer is `JUST FALSE`"; delegated-definitions ruling of 2026-11-05, item (c): ""when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above"; grant ruling of 2026-11-12, limit 3: "do not change, but list in the row's fork register ... a "may" function whose gate is "where", "when" or "upon"". |
| s 203A(2) | `s 203A(2) the person may instead request a summary financial statement` | "Where a company sends to its members a summary financial statement under subsection (1)" | JUST FALSE when no summary was sent | NOTHING | F-203A-2 | Guide section 5, periods ruling of 2026-11-05, item (b): "a "where ..." condition: when it fails the answer is `JUST FALSE`"; delegated-definitions ruling of 2026-11-05, item (c): ""when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above"; grant ruling of 2026-11-12, limit 3: "do not change, but list in the row's fork register ... a "may" function whose gate is "where", "when" or "upon"". |
| sch 12 para 3 | `sch 12 para 3 the particulars may be stated by reference to the earlier statement or report` | "Where any of the particulars required by paragraph 2 have been stated in a previous directors' statement" | JUST FALSE when they have not | NOTHING | F-sch12-3 | Guide section 5, periods ruling of 2026-11-05, item (b): "a "where ..." condition: when it fails the answer is `JUST FALSE`"; delegated-definitions ruling of 2026-11-05, item (c): ""when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above"; grant ruling of 2026-11-12, limit 3: "do not change, but list in the row's fork register ... a "may" function whose gate is "where", "when" or "upon"". |
| s 203(4) | `s 203(4) the person may by notice require that a general meeting be held to lay the documents before the company` | "In a case referred to in subsection (1)(b)" | NOTHING outside the case or the persons; JUST FALSE after the 14 days | JUST FALSE, as for "where" | F-203-4 | Guide section 5, "In short": `NOTHING` where the text "limits a grant or prohibition in its own wording and the case falls outside the limit"; the gate here is "In a case referred to in subsection (1)(b)", which is not the word "where", "when" or "upon", so limit 3 does not apply to it. |

### Not split sites: the text closes the gate itself (grant ruling, limit 2)

| provision | the text's own closing words | why it is not a split site | answer taken |
| --- | --- | --- | --- |
| s 199(5) | "but only upon an undertaking in writing" | the gate is closed with "only" (limit 2) | JUST FALSE when no undertaking is given |
| s 201A(3) | "but the written notice must be issued to the directors not less than 3 months before the end of the financial year" | a proviso that closes the gate (limit 2) | JUST FALSE when the notice is late |
| s 202A(4) | "the directors may not cause the financial statements ... to be revised unless the Registrar agrees" | "may not ... unless" (limit 2) | JUST FALSE for the bar when no notice was given; see F-unless |
| s 203A(1) | "in such cases as may be specified by regulations and provided all the conditions so specified are complied with" | "provided" closes the gate (limit 2) | JUST FALSE when a condition is not met; NOTHING for whether the case is one the regulations specify, which points outside the text |

## Jural relations (sgc1)

One row per provision, or per group of provisions that create the same relation, over the whole of the two ranges.
The pairs are Hohfeld's: right (claim) and duty; privilege and no-right; power and liability; immunity and disability.
"The text names no holder" means the provision states a duty or liability and no person who can demand it.
A provision that creates no relation is a row marked `none`.
The last column is built by script from the layer-1 files.

| provision | relation | holder of the right, privilege, power or immunity | bearer of the duty, no-right, liability or disability | L4 rules |
| --- | --- | --- | --- | --- |
| s 199(1) | duty / right (claim) | the text names no holder | the company | `s 199(1) the company has caused the records to be kept as the subsection requires`; `s 199(1) a company must cause accounting and other records to be kept` |
| s 199(2) | duty / right (claim) | the text names no holder | the company | `s 199(2) the last day of the period for which the company must retain the records`; `s 199(2) the subsection requires the company to retain the records on the day`; `s 199(2) a company must not dispose of the records within 5 years from the end of the financial year` |
| s 199(2A) | duty / right (claim) | the text names no holder | every public company and every subsidiary company of a public company | `s 199(2A) the company must devise and maintain a system of internal accounting controls`; `s 199(2A) the company has devised and maintained the system the subsection requires`; `s 199(2A) a public company or a subsidiary company of a public company must devise and maintain a system of internal accounting controls` |
| s 199(3) | right (claim) / duty; and the directors' discretion over the place | the directors (inspection at all times; they also choose the place, "as the directors think fit") | the company | `s 199(3) the records are kept as the subsection requires`; `s 199(3) the records must be open to inspection by the person`; `s 199(3) a company must keep its accounting records open to inspection by the directors` |
| s 199(4) | right (claim) / duty | the directors (statements and returns open to their inspection at all times) | the company, where records are kept outside Singapore | `s 199(4) the company must send to and keep at a place in Singapore statements and returns`; `s 199(4) the company has complied with the subsection` |
| s 199(5) | power / liability | the Court (may order inspection by a public accountant acting for a director, but only upon a written undertaking) | the company (its records become open to inspection) | `s 199(5) the Court may order the records to be open to inspection by the public accountant` |
| s 199(6) | liability (to conviction and a penalty) | the text names no prosecutor | the company and every officer of the company in default | `s 199(6) the person is guilty of the offence this subsection creates`; `s 199(6) the most the person may be sentenced to on conviction`; `s 199(6) penalty` |
| s 200, s 200A | none | - | - | none: a coverage row only |
| s 201(1) | duty / right (claim) | the text names no claimant (the statements are laid before the company at its annual general meeting) | the directors of every company | `s 201(1) the financial statements are the ones the directors must lay before the company at its annual general meeting`; `s 201(1) the directors of a company must lay the financial statements before the company at its annual general meeting` |
| s 201(2) | duty / right (claim) | the text names no holder | the text names no bearer (s 204(1) makes a director's failure to comply an offence) | `s 201(2) the document complies with the Accounting Standards and gives a true and fair view` |
| s 201(5) | privilege (need not comply with subsection (1)) and duty | the directors of a parent company (privilege) | the directors of a parent company (duty to make out and lay the consolidated statements and the balance sheet) | `s 201(5) the directors need not comply with subsection (1) but must lay the consolidated financial statements and the balance sheet`; `s 201(5) the consolidated financial statements and the balance sheet are as the subsection requires`; `s 201(5) the directors of a parent company must cause to be made out and lay the consolidated financial statements and the balance sheet` |
| s 201(7) | duty / right (claim) | the text names no holder | the directors | `s 201(7) the directors must take reasonable steps before the financial statements are made out` |
| s 201(8) | duty / right (claim) | the text names no holder | the text names no bearer (subsection (9) puts the steps on the directors) | `s 201(8) the financial statements have been audited and reported on as the subsection requires` |
| s 201(9) | duty / right (claim); power (the agreement of the persons entitled to notice lifts the 14 days) | the persons entitled to receive notice of general meetings (their agreement) | the directors | `s 201(9)(a) the latest day by which the financial statements are to be audited`; `s 201(9)(a) the financial statements have been audited in time`; `s 201(9)(a) the directors must take reasonable steps to ensure that the financial statements are audited not less than 14 days before the annual general meeting`; `s 201(9)(b) the directors have caused the auditor's report to be attached`; `s 201(9)(b) the directors must cause the auditor's report to be attached to the financial statements` |
| s 201(10) | none (a definition of "financial statements" for subsections (8) and (9)) | - | - | `s 201(10) the documents that "financial statements" means in subsections (8) and (9)`; `s 201(10) the documents meant by financial statements` |
| s 201(11) | duty / right (claim) | the text names no holder | the directors of a subsidiary company | `s 201(11) the directors must state the name of the ultimate parent corporation`; `s 201(11) the directors have stated the name of the ultimate parent corporation`; `s 201(11) the directors of a subsidiary company must state the name of its ultimate parent corporation` |
| s 201(12) | privilege (need not comply) on a condition | the company's directors | the text names no bearer; the condition is the Registrar's approval, whose power the text does not set out | `s 201(12) the financial statements need not comply with the requirements of the Accounting Standards` |
| s 201(13) | privilege (need not comply, to the extent necessary) | the company's directors | the text names no bearer | `s 201(13) the financial statements need not comply with the requirement of the Accounting Standards` |
| s 201(14) | duty / right (claim) | the text names no holder | the text names no bearer ("there must be included") | `s 201(14) the financial statements must include the statement, particulars and information the subsection lists`; `s 201(14) the financial statements include what the subsection requires` |
| s 201(15) | power / liability | the Minister (to substitute other accounting standards by order in the Gazette) | companies of the specified class | `s 201(15) the substituted standards apply to the company in place of the Accounting Standards` |
| s 201(15A) | power / liability; immunity / disability | the Minister (power); the directors of the specified class (immunity) | the directors of the specified class (liable to have the duty lifted); the text names no one who loses a claim | `s 201(15A) the directors are exempt from having to ensure that the financial statements comply with the requirement` |
| s 201(16) | duty / right (claim) | the text names no holder | the directors (the statement is signed on their behalf by 2 of them) | `s 201(16) the financial statements are accompanied by the directors' statement the subsection requires`; `s 201(16) the directors must accompany the financial statements with a statement signed on their behalf by 2 directors`; `s 201(16) to (23) act` |
| s 201(17) | duty (a prohibition) / right (claim); immunity | the text names no holder; a banking corporation and financial statements are outside the bar | a company (other than a banking corporation) | `s 201(17) the representation that the company has a reserve is barred`; `s 201(17) a company must not publish a document that represents that it has a reserve unless the representation is accompanied` |
| s 201(18) | power / liability | the Monetary Authority of Singapore (determines modifications and exceptions) | a banking corporation | `s 201(18) the form and content provisions apply to the banking corporation as they stand` |
| s 201(19) | none in this Act (the modification is prescribed under s 12(1)(f) of the Charities Act 1994, outside the sources) | - | a company registered as a charity or approved as an institution of a public character | `s 201(19) the Accounting Standards requirements apply to the charity as they stand` |
| s 201(20), (21) | none (rules of reading for the earlier text) | - | - | `s 201(20) the documents are within a reference to the preceding financial statements`; `s 201(21) the laying of the documents is within a reference to the requirement to lay financial statements` |
| s 201(22) | immunity / disability; continuing duty | a company, for a financial year that ended before 1 July 2015 (subsection (16) does not apply) | the text names no one | `s 201(22) subsection (16) applies to the company for the financial year`; `s 201(22) the earlier provisions of section 201 continue to apply to the company for the financial year` |
| s 201(23) | duty / right (claim) | the text names no holder (the return is lodged with the Registrar under s 197) | a company referred to in subsection (22) | `s 201(23) the company must attach a copy of the report prepared under section 201(5) as it then stood to the return`; `s 201(23) a company with an old financial year must attach a copy of the report to its return` |
| s 201(3), (4), (6) | none (shown deleted) | - | - | none: a coverage row only |
| s 201A(1) | immunity / disability | the directors of a dormant relevant company (exempt from s 201) | the Registrar and the members, who cannot require compliance except under subsection (3) | `s 201A(1) the directors are exempt from the requirements of section 201 for the financial year`; `s 201A(2) the requirements for the exemption are satisfied` |
| s 201A(3), (4) | power / liability | a relevant person: the Registrar, members holding at least 5% of the issued shares, or at least 5% of the members | the directors of the dormant relevant company | `s 201A(3) the relevant person may by written notice require the directors of the dormant relevant company to comply with section 201`; `s 201A(4) the person is a relevant person` |
| s 201A(5) | none (definitions of "relevant company" and of dormancy) | - | - | `s 201A(5)(a) the company is a relevant company`; `s 201A(5)(a)(ii)(A) the amount the section states, in Singapore dollars`; `s 201A(5)(b) the relevant company is dormant` |
| s 201A(6), (7) | immunity; duty / right (claim) | the text names no holder (the return is lodged with the Registrar under s 197) | the directors (prepare and lay accounts under the earlier Part VI); the company (attach a copy to the return) | `s 201A(6) this section applies to the directors for the financial year`; `s 201A(6) the directors must prepare and lay the accounts under Part VI as it stood`; `s 201A(7) the company must attach a copy of the accounts to the return`; `s 201A(7) a company with an old financial year must attach a copy of the accounts to its return` |
| s 201AA(1) | duty / right (claim) | the text names no holder | the company | `s 201AA(1) the last day of the period for which the company must keep the documents`; `s 201AA(1) the subsection requires the company to keep the documents on the day`; `s 201AA(1) the documents are kept at a place the subsection allows`; `s 201AA(1) a company must not dispose of the documents within 5 years` |
| s 201AA(2) | liability (to conviction and a penalty) | the text names no prosecutor | the company and every officer in default | `s 201AA(2) the person is guilty of the offence this subsection creates`; `s 201AA(2) the most the person may be sentenced to on conviction`; `s 201AA(2) penalty` |
| s 201AA(3) | power / liability; privilege / no-right | the Registrar or an authorised officer (may require a document; may inspect and copy without fee) | the company (liable to produce) | `s 201AA(3) the company may be required to furnish the document and the document may be inspected` |
| s 201AA(4) | duty / right (claim); liability | the Registrar and the authorised officer (the claim to the document and to be free of obstruction) | any person who refuses without lawful excuse, or assaults, obstructs, hinders or delays | `s 201AA(4) the person is guilty of the offence this subsection creates`; `s 201AA(4) the most the person may be sentenced to on conviction` |
| s 201AA(5) | none (a definition of "authorised officer") | - | - | `s 201AA(5) the person is an authorised officer` |
| s 201B(1) | duty / right (claim) | the text names no holder | every listed company | `s 201B(1) the company must have an audit committee`; `s 201B(1) a listed company must have an audit committee` |
| s 201B(2) | duty / right (claim) | the text names no holder | the directors (appoint from among their number, by a board resolution) | `s 201B(2) the audit committee is appointed and composed as the subsection requires` |
| s 201B(3) | duty / right (claim) | the text names no holder | the members of the audit committee (elect a chairperson who is not an executive director or an employee) | `s 201B(3) the person is eligible to be elected chairperson of the audit committee` |
| s 201B(4) | duty / right (claim) | the text names no holder | the board of directors (3 months) | `s 201B(4) the last day for the board of directors to appoint new members`; `s 201B(4) the board of directors has appointed new members in time`; `s 201B(4) the board of directors must within 3 months appoint new members to make up the minimum number` |
| s 201B(5) | none (a list of the committee's functions, with no party bound to anyone) | - | - | `s 201B(5) the function is one of the functions of an audit committee`; `s 201B(5) function` |
| s 201B(6) | right (claim) / duty; power / liability | the auditor (right to appear and be heard); the audit committee (may require the auditor to appear) | the audit committee (must hear); the auditor (must appear when required) | `s 201B(6) the auditor has the right to appear and be heard at any meeting of the audit committee`; `s 201B(6) the auditor must appear before the committee`; `s 201B(6) the auditor must appear before the committee when required to do so` |
| s 201B(7) | power / liability; duty / right (claim) | the auditor (a request); the auditor (claim to the meeting) | the chairperson of the audit committee (must convene) | `s 201B(7) the chairperson must convene a meeting of the audit committee`; `s 201B(7) the chairperson must convene a meeting of the committee on the auditor's request` |
| s 201B(8) | privilege / no-right | each audit committee (regulates its own procedure) | the text names no one | `s 201B(8) the audit committee may regulate the matter` |
| s 201B(9) | duty / right (claim) | the text names no holder | the directors of a listed company, or of a parent company that is listed | `s 201B(9) the directors must describe the audit committee's functions in the statement`; `s 201B(9) the directors' statement describes the audit committee's functions as the subsection requires`; `s 201B(9) the directors of a listed company must describe the audit committee's functions in the statement` |
| s 201B(10) | none (shown deleted) | - | - | none: a coverage row only |
| s 201B(11) | none (a definition of "executive director") | - | - | `s 201B(11) the director is an executive director` |
| s 201C(1) | privilege (need not comply) | the directors of a private company that need not hold an annual general meeting because of s 175A(1) | the text names no bearer | `s 201C(1) the directors need not lay financial statements before the company at its annual general meeting` |
| s 201C(2) | none (a rule of reading for s 207(1)) | - | - | `s 201C(2) the reference in section 207(1) is read as a reference to the documents sent under section 203(1)` |
| s 202(1) | power / liability; privilege | the Registrar (may make the order, with or without conditions); the directors (may apply) | the directors (liable to the order's conditions, immune from the requirement once relieved) | `s 202(1) the directors may apply to the Registrar in writing for an order relieving them from the requirement`; `s 202(1) the Registrar may make the order on condition that the directors comply with the other requirement`; `s 202(1) the directors are relieved by the Registrar's order from the requirement` |
| s 202(2) | power / liability; immunity | the Registrar (class order); the directors of the class (immune from the specified requirements) | the directors of the class | `s 202(2) the directors are relieved by the Registrar's order for a class of companies from the requirement` |
| s 202(3) | disability | the text names no one who benefits | the Registrar (must not make an order under s 202(1) unless of the stated opinion) | `s 202(3) the Registrar is not barred from making an order under section 202(1)` |
| s 202(4) | power / liability | the Registrar (limit to a period; revoke or suspend, on application or without one); the directors (a claim to be heard where there is no application) | the directors (the relief ends); the Registrar (must give the directors an opportunity of being heard where there is no application) | `s 202(4) the order made under section 202(1) has not ended` |
| s 202A(1), (2) | privilege / no-right | the directors (may cause the statements to be revised) | the text names no one | `s 202A(1) the section applies`; `s 202A(2) the directors may cause the financial statements to be revised` |
| s 202A(3) | duty / right (claim) | the text names no holder | the directors (confine the revision) | `s 202A(3) the revision is confined as the subsection requires` |
| s 202A(4) | duty (a prohibition) / right (claim) | the Registrar (whose agreement lifts the bar) | the directors | `s 202A(4) the directors are barred from causing the financial statements to be revised` |
| s 202A(5) | power (inert: machinery) | the Minister (regulations under s 411) | - | none: a coverage row only |
| s 202B(1) | power / liability | the Registrar (give a notice and specify the period) | the directors | `s 202B(1) the Registrar may give the directors a notice` |
| s 202B(2) | duty / right (claim) | the Registrar | the directors to whom the notice is given | `s 202B(2) the number of days allowed for the response`; `s 202B(2) the last day for the directors to respond`; `s 202B(2) the directors responded by the end of the period`; `s 202B(2) the directors must respond to the Registrar's notice by the end of the period` |
| s 202B(3) | immunity | the directors (no further action once the Registrar is satisfied) | the Registrar (no right to further action on the notice) | `s 202B(3) the directors need take no further action on the notice` |
| s 202B(4) | privilege / no-right | the directors (may revise in the manner agreed) | the text names no one | `s 202B(4) the directors may cause the financial statements to be revised in the manner agreed` |
| s 202B(5), (6) | power / liability | the Registrar (may apply to Court on the three grounds, for a declaration and an order) | the directors | `s 202B(5) the Registrar may apply to Court under subsection (6)`; `s 202B(6) the application to Court may be for the relief` |
| s 202B(7) | power / liability | the Court (directions) | the directors and the company | `s 202B(7) the Court may give directions on the matter`; `s 202B(7) matter of directions` |
| s 202B(8) | power / liability | the Court (costs and expenses) | any or all of the directors as at the date of the directors' statement | `s 202B(8) the Court may order that the director bears all or part of the costs and expenses` |
| s 202B(9) | none (a rule of reading for further revisions) | - | - | `s 202B(9) the section applies to the statements as it applies to the first statements` |
| s 203(1) | duty / right (claim) | all persons entitled to receive notice of general meetings | the company | `s 203(1) the company must send the documents to all persons entitled to receive notice of general meetings`; `s 203(1) the documents were sent in time`; `s 203(1) the company must send the documents by the last day` |
| s 203(2) | privilege; power | the company (may send late); all persons entitled to receive notice (their agreement is what lifts the 14 days) | all persons entitled to receive notice (liable to have the period shortened) | `s 203(2) the documents may be sent less than 14 days before the date of the meeting` |
| s 203(3) | right (claim) / duty | any member to whom copies were not sent, and any debenture holder | the company | `s 203(3) the company must furnish the person without charge with a copy of the last financial statements and the auditor's report`; `s 203(3) the company must furnish a copy of the last financial statements on request` |
| s 203(3A) | liability; immunity | the text names no prosecutor; the company and officers hold the defence (proof of an earlier request and copy) | the company and every officer in default | `s 203(3A) the subsection gives the person a defence on these facts`; `s 203(3A) the person is guilty of the offence this subsection creates`; `s 203(3A) the most the person may be sentenced to on conviction`; `s 203(3A) penalty` |
| s 203(4), (4A) | power / liability | any member or auditor of the company (notice within 14 days of the sending out) | the company | `s 203(4) the last day for the notice requiring a general meeting`; `s 203(4) the person may by notice require that a general meeting be held to lay the documents before the company`; `s 203(4A) the person may by notice require that a general meeting be held to lay the documents before the company` |
| s 203(5) | none (applies s 175A(5), a later wave's) | - | - | `s 203(5) section 175A(5) applies, with the necessary modifications, to the giving of the notice` |
| s 203(6) | duty / right (claim) | the member or auditor who gave notice | the directors (convene within 14 days) | `s 203(6) the directors must convene a meeting for the purpose referred to in the notice`; `s 203(6) the last day for the directors to convene the meeting`; `s 203(6) the directors convened the meeting in time`; `s 203(6) the directors must within 14 days convene the meeting` |
| s 203(7) | liability; power / liability | the text names no prosecutor; the Court (on application of the member or auditor) | each director in default; the directors | `s 203(7)(a) the person is guilty of the offence this paragraph creates`; `s 203(7)(a) the most the person may be sentenced to on conviction`; `s 203(7)(b) the Court may order a general meeting to be called`; `s 203(7)(a) penalty` |
| s 203A(1) | privilege / no-right | the company (may send a summary instead, in the cases regulations specify) | members (no right to the full documents in those cases) | `s 203A(1) the company may send a summary financial statement instead of copies of the documents referred to in section 203(1)` |
| s 203A(2) | privilege | any member, and any debenture holder entitled to a copy under s 203(3) (may request a summary instead) | the text names no one | `s 203A(2) the person may instead request a summary financial statement` |
| s 203A(3) | privilege (need not send) | the company | a member who does not wish to receive the statement | `s 203A(3) the company need not send the summary financial statement to the member` |
| s 203A(4) | right (claim) / duty | any member who wishes to receive copies | the company | `s 203A(4) the company must send copies of the documents referred to in section 203(1) to the member`; `s 203A(4) the company must send copies of the documents to the member who wishes to receive them` |
| s 203A(5), (6) | duty / right (claim) | the text names no holder | the company (the summary's derivation and form); the text does not say whether the company or the auditors give the auditors' statement | `s 203A(5) the summary financial statement is derived and in the form the subsection requires`; `s 203A(6) the summary financial statement contains the statements the subsection requires` |
| s 203A(6A) | duty / right (claim) | the text names no holder | the directors | `s 203A(6A) the directors have ensured that the summary financial statements comply with subsections (5) and (6)`; `s 203A(6A) the directors must ensure that the summary financial statements comply` |
| s 203A(7) | liability | the text names no prosecutor | the company and every officer in default | `s 203A(7) the person is guilty of the offence this subsection creates`; `s 203A(7) the most the person may be sentenced to on conviction`; `s 203A(7) penalty` |
| s 203A(8) | none (shown deleted) | - | - | none: a coverage row only |
| s 203A(9) | power (inert: machinery) | the Minister (regulations) | - | none: a coverage row only |
| s 204(1), (1AA), (1A) | liability | the text names no prosecutor | a director who fails to comply with s 201(2) or (5); with s 201(16); or with any other provision of the Division, fails to take all reasonable steps, or wilfully causes a default | `s 204(1) the person is guilty of the offence this subsection creates`; `s 204(1AA) the person is guilty of the offence this subsection creates`; `s 204(1A) the person is guilty of the offence this subsection creates` |
| s 204(2) | immunity (a defence to prove) | the person charged with failing to take reasonable steps because of an omission from the statements | the prosecution (the text names none) | `s 204(2) the subsection gives the person a defence on these facts` |
| s 204(3) | liability (a heavier penalty) | the text names no prosecutor | the offender who acts with intent to defraud creditors or for a fraudulent purpose | `s 204 the most the offender may be sentenced to on conviction`; `s 204 offence`; `s 204 penalty` |
| s 204(4) | disability / immunity | the person (immune from imprisonment unless the offence was wilful) | the Court (may not sentence to imprisonment unless of that opinion) | `s 204(4) the person is barred from being sentenced to imprisonment for the offence` |
| Twelfth Schedule, paras 1, 2, 4 to 9 | duty / right (claim) | the text names no holder | the directors (what the directors' statement of s 201(16) must contain) | `sch 12 para 1 the statement contains the matters the paragraph requires`; `sch 12 para 2 the statement must state the particulars of the option`; `sch 12 para 2 the statement states the particulars of the option`; `sch 12 para 4 the directors' statement of the parent company must state the corporation and the other particulars`; `sch 12 para 4 the statement states the corporation and the other particulars`; `sch 12 para 5 the statement states the particulars of shares issued on the exercise of options`; `sch 12 para 6 the statement states the unissued shares under option`; `sch 12 para 7 the statement states the names of the directors in office`; `sch 12 para 8 the statement must also explain the effect of the arrangements and name the directors`; `sch 12 para 8 the statement states whether the arrangements subsisted and, if so, their effect`; `sch 12 para 9 the statement states the director's interests in shares and debentures` |
| Twelfth Schedule, para 3 | privilege | the directors (may state the particulars by reference to an earlier statement or report) | the text names no one | `sch 12 para 3 the particulars may be stated by reference to the earlier statement or report` |
| Part 6 and Division 1 headings, marginal headings, the Schedule's title and running headings | none (not rules) | - | - | none: a coverage row only |

## Marginal readings for a lawyer (sgc1)

Two readings are left to a lawyer by the rule of 2026-10-29: (a) a failed "if" counts as the text's no, clause by clause within the provision that holds the "if", and flat negatives count as the text saying no; (b) a prohibition or grant limited by its own wording does not.
This part took both as the status quo.
Each branch that rests on one is listed here with the other reading.
M1 to M3, M19 and M20 are built by script from the comments in the code; the sites are the code's own.

| id | the reading taken | sites | answer taken | the other reading |
| --- | --- | --- | --- | --- |
| M1 | A failed "if", "where" or "in the event of" in a relief, an exemption or a duty counts as the text's no (reading (a) of the rule of 2026-10-29). | s 199(4), s 201(12), s 201(14), s 201A(1), s 201C(1), s 202B(3), s 203A(3) | JUST FALSE when the condition fails. | NOTHING: "if A then B" does not itself say "if not A then not B", and each relief is grant-like. |
| M2 | A Ministerial order that the person says does not apply counts as the text's no. | s 201(15), s 201(15A) | JUST FALSE ("The Minister may, by order in the Gazette ...": the only route the subsection gives is an order, and the person states whether one applies). | NOTHING, since whether an order exists points outside the text. |
| M3 | A fact the text hands to another section (dormancy under s 205B(2) and (3)) that the person says is not met counts as the text's no. | s 201A(5)(b) | JUST FALSE. | NOTHING, since the answer is another part's and points outside the text. |
| M4 | s 201(2) and (5): a departure from the Accounting Standards is allowed only by s 201(12), (13) or (15A), and when none allows it the duty stands. | s 201(2), s 201(5), `s 201(12), (13) and (15A) a departure ... is allowed`. | JUST FALSE for a document that does not comply and has no allowed departure. | NOTHING (the layer-1 functions answer NOTHING only when the allowance itself is not supplied). |
| M5 | "A majority must not be" (s 201B(2)) means more than half: exactly half is allowed. | s 201B(2). | members within (a), (b) or (c) times 2 at most the number of members (exactly half is allowed). | Exactly half is also barred: fewer than half may be within (a), (b) or (c). |
| M6 | "In conjunction with his or her office of director and his or her membership of any audit committee" (s 201B(11)) is not asked as a separate fact. | s 201B(11). | A director who is an employee, or holds another office of profit, in the company or in a related corporation is an executive director. | The qualifying words could limit the employment or office of profit to one held in conjunction with the office of director. |
| M7 | The obligor in s 201B(4) is "the board of directors", a collective, and is encoded as a Director party with a name. | s 201B(4). | Any named director may be the party of the rule. | The board as one party, which the keel's Party type has no constructor for. |
| M8 | "Subject to subsection (3)" in s 202A(1) is read as a limit on the revision (subsection (3) says what the revision may touch), not on when the section applies. | s 202A(1), s 202A(3). | s 202A(1) depends on the two timing paragraphs only. | Subsection (3) could narrow the cases to which the section applies. |
| M9 | "At the end of the period" (s 202B(2)) is read as "by the end of the period". | s 202B(2). | A response on any day up to and including the last day is in time. | A response is due on the last day and not before. |
| M10 | A "longer period as the Registrar may allow" (s 202B(2)) is a total number of days counted from the same day as the first period. | s 202B(2). | total days from the notice. | an extension added to the first period. |
| M11 | s 203(1)(b) applies to "a company ... not required to hold an annual general meeting because of section 175A(1)(a)", and s 175A(1)(b) (a later wave's) borrows "the period specified in section 203(1)(b)" for companies that need not hold one because of s 175A(1)(b): the cross-references point past each other, and a company within s 175A(1)(b) is counted under paragraph (a) when the person says it is not within s 175A(1)(a). | s 203(1), s 203(4A). | Paragraph (a), which counts back from "the date of the meeting" that the person supplies. | The five months of paragraph (b), which s 175A(1)(b) itself points at; or no deadline, since neither paragraph names s 175A(1)(b). |
| M12 | s 203(3A)'s defence ("has already made a request for and been furnished with a copy") is a defence for any default of subsection (1) or (3), and it will rarely fit a default of subsection (1). | s 203(3A). | JUST TRUE where proved, JUST FALSE otherwise ("this section gives no defence on these facts"). | The defence belongs to default of subsection (3) only. |
| M13 | The imprisonment term of a penalty is 0 months where the text gives none, and a "default penalty" is recorded as a flag, its amount being s 408's. | s 203(3A), s 203(7)(a), s 203A(7), s 204(1), s 204(1AA). | 0 months and a flag. | NOTHING for the term. |
| M14 | s 204(3) replaces the ordinary penalty with the fraud penalty where the offence is committed with intent to defraud; it does not add to it. | s 204(3), `s 204 the most the offender may be sentenced to on conviction`. | the (3) penalty replaces. | the (3) penalty is added to the subsection (1), (1AA) or (1A) penalty. |
| M15 | Twelfth Schedule paragraphs 1, 2, 5, 6, 7, 8 and 9 have no verb; each is read as "the directors' statement must contain what the paragraph lists", through s 201(16) ("containing the information set out in the Twelfth Schedule"). | sch 12 paras 1, 2, 5, 6, 7, 8, 9. | A statement that omits a listed item answers JUST FALSE for that paragraph. | NOTHING, since the paragraph states no duty in words. |
| M16 | "(if any)" in paragraph 6 asks for the rights where there are some, and a statement that gives none where none exist meets it. | sch 12 para 6. | the rights input is a plain yes/no "the statement gives the rights, if any". | A separate fact whether any rights exist. |
| M17 | The counting of periods (the day of the event is not counted, months and years clamp to the last day of a short month, "not less than 14 days before" is the meeting date minus 14) is the keel's convention P1 to P9 in `sg-periods.l4`, assumed because the Interpretation Act 1965 is not among the sources. | s 199(2), s 201(9)(a), s 201A(3), s 201AA(1), s 201B(4), s 202B(2), s 203(1), s 203(4), s 203(6). | keel P1 to P9. | other counting (clear days, P7). |
| M18 | s 201(16): "signed on behalf of the directors by 2 directors" is read as at least 2. | s 201(16). | at least 2 signatures. | exactly 2. |
| M19 | A grant or a prohibition limited by its own wording does not count as the text's no (reading (b)). | 66 functions and 67 branches: s 199(2), s 199(2A), s 199(3), s 199(4), s 199(5), s 199(6), s 201(1), s 201(5), s 201(9)(a), s 201(11), s 201(14), s 201(18), s 201(19), s 201(22), s 201(23), s 201A(3), s 201A(6), s 201A(7), s 201AA(1), s 201AA(2), s 201AA(3), s 201AA(4), s 201B(1), s 201B(4), s 201B(6), s 201B(8), s 201B(9), s 201C(1), s 202(1), s 202A(2), s 202B(1), s 202B(2)(a), s 202B(2)(b), s 202B(4), s 202B(5), s 202B(8), s 202B(9), s 203(1), s 203(2), s 203(3), s 203(3A), s 203(4), s 203(4A), s 203(5), s 203(6), s 203(7)(a), s 203(7)(b), s 203A(2), s 203A(4), s 203A(7), s 204(2), s 204, s 204(4), sch 12 para 2, sch 12 para 4, sch 12 para 5, sch 12 para 6, sch 12 para 9 | NOTHING outside the limit. | JUST FALSE outside the limit. |
| M20 | A flat negative ("shall not", "must not", "may not", "does not apply") counts as the text's no (reading (a), second limb). | s 201(17), s 202(3), s 202A(4), s 204(4), s 201(22) and s 201A(6) (the last two marked `a flat negative` in the code). | JUST FALSE where the bar or the negative applies. | NOTHING. |

### Sites where the Guide itself leaves the answer to the encoder

Six questions the Guide leaves open (an "unless" once met, a bare "must" not done, "listed in Schedule N", a duty whose "if" or "where" is unmet, "(other than X)", a missing event in a state ledger) are decided site by site.
Each of those sites has a fork line in the register above (F-unless, F-duty-if, F-other-than and F-203-unless).
No "listed in Schedule N" site and no state ledger occurs in these ranges.

### Reading a result: FALSE and NOTHING (sgc1)

Almost every rule here answers `MAYBE BOOLEAN`, and the result has three values that must never be mixed up.
`JUST TRUE` is yes.
`JUST FALSE` is the text saying no in its own words: a "means" definition, a condition the text introduces with "if", "only if", "unless" or "provided", a period the text fixes ("not less than 5 years", "within 14 days", "not later than 5 months"), a flat negative ("shall not", "may not"), or the provision's own question (a duty not met, an offence element not met).
`NOTHING` is "the text does not answer this case": the text is silent, lists without closing the list, says "includes", leaves a term to regulations, a Minister or another Act (the cases of s 203A(1) are those "specified by regulations"), or limits a grant or a prohibition in its own wording and the case falls outside the limit (s 201B(8) gives the committee "its own procedure", and a matter that is not procedure is outside the grant).
In this Division a yes is, for example, "your directors must lay the financial statements" (s 201(1)); a no in the text's own words is "you are not guilty of this offence on these facts" (s 204(1) answers JUST FALSE for a person who is not a director) or "this section gives no defence on these facts" (s 203(3A), s 204(2)); and not-covered is "the text does not say" (the Registrar's order is a fact the text does not state, so s 202(1) "are the directors relieved by the Registrar's order" answers NOTHING when no order is supplied).
A caller must never turn NOTHING into FALSE: "not covered" is not "not required".
The rule of 2026-10-29 is assumed, not ruled by a lawyer, and the two readings it leaves open for a lawyer are listed under "Marginal readings for a lawyer (sgc1)" with the sites of each.
Every JUST FALSE branch in the layer-1 files carries a `-- FALSE-kind (the text says no in its own words): "<quoted words>"` comment, and every NOTHING branch a `-- NOTHING-kind (<why>)` comment with one of the six reasons the brief names.
The quoted words of every such comment were checked against the text by script (`work/check_quotes.py`): 361 fragments, 353 found in the text, and the 8 not found are quotations of the Guide's own words ("In short", "(other than X)", "this section gives no defence on these facts", "limits a grant or prohibition in its own wording and the case falls outside the limit"), not of the Act.

The tags by count: 107 `FALSE-kind` and 79 `NOTHING-kind`.
The reasons given on the `NOTHING-kind` tags: limited by its own wording 67, points outside the text 7, silent 2, includes 2, list not closed 1.
The tags were counted from the layer-1 files by script (`work/scan.py`); every branch that answers `JUST FALSE` or `NOTHING` in them carries a tag on its line or the line after.

## Seams (sgc1)

A seam is a fact that another part's section answers.
This part cannot import another part, so a fact it needs from one is an input named for the fact and the section.
The seams below are each seam this part took or gave, and each seam found that PLAN.md's table lacks is marked.

### Seams where the keel asks and this part answers (PLAN.md section 4, table A)

| the keel asks | the input as PLAN.md names it | what this part has | L4 rules |
| --- | --- | --- | --- |
| s 7A(4)(a)(i) in `sg-solvency` (line 2357-2359) | `the directors had regard to the most recent financial statements of the company that comply with section 201(2) and (5), as the case may be` (BOOLEAN) | This part answers whether financial statements comply with s 201(2) and (5) through two functions, and the merged seat or the keel's caller can pass their answer as that input. | `s 201(2) the document complies with the Accounting Standards and gives a true and fair view`; `s 201(5) the directors need not comply with subsection (1) but must lay the consolidated financial statements and the balance sheet`; `s 201(5) the consolidated financial statements and the balance sheet are as the subsection requires`; `s 201(5) the directors of a parent company must cause to be made out and lay the consolidated financial statements and the balance sheet` |
| s 4(1) "audit requirements" | `the requirement is a requirement of section 201(8) or (9)` (BOOLEAN) | This part encodes whether the duties of s 201(8) and (9) are met, not which requirements belong to them, so the classifying fact is not defined here; the three duty functions are the rules the classification would point at. | `s 201(8) the financial statements have been audited and reported on as the subsection requires`; `s 201(9)(a) the latest day by which the financial statements are to be audited`; `s 201(9)(a) the financial statements have been audited in time`; `s 201(9)(a) the directors must take reasonable steps to ensure that the financial statements are audited not less than 14 days before the annual general meeting`; `s 201(9)(b) the directors have caused the auditor's report to be attached`; `s 201(9)(b) the directors must cause the auditor's report to be attached to the financial statements` |
| s 4(1) "summary financial statement" | `the statement is a summary financial statement referred to in section 203A` (BOOLEAN) | Likewise a classification, not a duty: this part encodes what the summary must be (derivation, form, content), not whether a given statement is one. | `s 203A(5) the summary financial statement is derived and in the form the subsection requires`; `s 203A(6) the summary financial statement contains the statements the subsection requires` |

### Seams where this part takes another section's answer as an input

| input, as named in layer 1 | section it comes from | owner | used in | note |
| --- | --- | --- | --- | --- |
| `the company is not required to hold an annual general meeting because of section 175A(1)(a)`; `... (1)(b)`; `the company need not hold an annual general meeting because of section 175A(1)`; `... for the financial year because of section 175A(1)`; `... under section 175A` | s 175A(1) | later wave | s 203(1), s 203(4A), s 201C(1), s 201AA(1), s 202A(1) | BOOLEAN each; the lines of the text that cite s 175A are 18343, 18513, 18584, 18839 and 18890 (`inputs/XREFS.md`) |
| `s 175A(5) applies, with the necessary modifications, to the giving of the notice` (as the rule `s 203(5)`) | s 175A(5) | later wave | s 203(5) | found: s 203(5) only applies another section, so the encoding says that it applies and answers NOTHING for what s 175A(5) says |
| `the statement has been lodged with the Registrar at the same time that the annual return is required to be lodged under section 197(1)` | s 197(1) | later wave | s 201A(2)(c) | BOOLEAN |
| `the company is dormant as section 205B(2) and (3) determine` | s 205B(2), (3) | sgc2 | s 201A(5)(b) | BOOLEAN; marginal reading M3 |
| `the auditor's report required by section 207 is attached to or endorsed upon the financial statements`; `the auditor's report that is furnished to the directors under section 207(1A) is attached to the financial statements` | s 207 | sgc2 | s 201(8), s 201(9)(b) | BOOLEAN each |
| `s 201C(2) the reference in section 207(1) is read as a reference to the documents sent under section 203(1)` | s 207(1) | sgc2 | s 201C(2) | found: the reading rule is encoded as a rule about the reference, since s 207 is another part's |
| `the statement says whether or not, according to the register kept for the purposes of section 164, the director was at the end of that year interested ...` | s 164 | sgb2 | sch 12 para 9 | BOOLEAN |
| The default penalty (a flag in each penalty record, its amount not given) | s 408 | later wave | s 199(6), s 201AA(2), s 203(3A), s 203(7)(a), s 203A(7) | the penalty record says that a default penalty also applies; its amount is s 408's |
| `the case is one specified by regulations`; `all the conditions specified by regulations are complied with`; `the summary financial statement is in the form, and contains the information, that regulations specify` | regulations under s 203A(1), (5), (9) and s 411 | not a source | s 203A(1), s 203A(5) | BOOLEAN each; the regulations are not among the sources |
| `the company is a listed company`; `the company is a private company`; `the company is a public company`; `the company is a subsidiary company of a public company`; `the company is a parent company ...` | s 4(1) and s 209A | keel and sgc2 | s 199(2A), s 201(5), s 201A(5)(a), s 201B(1), s 201C(1), sch 12 para 2 and 4 | plain BOOLEAN inputs: s 209A defines the terms for this Part by the Accounting Standards (see the differences above) |
| `the other corporation is deemed to be related to the company by virtue of section 6` | s 6 | keel | s 201B(11) | passed to the keel's `s 4(1) "related corporation"` function |
| `the Monetary Authority of Singapore has determined modifications or exceptions, generally or in the particular case` | Monetary Authority of Singapore Act 1970 (named in s 201(18)) | not a source | s 201(18) | BOOLEAN; found: not in PLAN.md's table |
| `a modification has been prescribed under section 12(1)(f) of the Charities Act 1994 in respect of such a company` | Charities Act 1994 s 12(1)(f) | not a source | s 201(19) | BOOLEAN; found: not in PLAN.md's table |
| `an order in the Gazette substitutes other accounting standards ...`; `an order in the Gazette exempts the directors ...` | the Minister's orders under s 201(15) and (15A) | not a source | s 201(15), s 201(15A) | BOOLEAN each; marginal reading M2 |
| `the Registrar has made an order ...`; `the Registrar is satisfied ...`; `the Registrar agrees ...`; `the Registrar thinks it fit ...` | the Registrar's acts | not a source | s 202, s 202A(4), s 202B | BOOLEAN each: a judgment the text hands to the Registrar is an input, never guessed |
| `the amount that applies, in Singapore dollars` | the Minister's substitution under s 201A(5)(a)(ii)(B) and (iii)(B) | not a source | s 201A(5)(a) | NUMBER, asked in the seat (see Seat) |

One internal cycle exists in the text and is cut by an input.
s 202B(2)(b) says the directors "inform the Registrar how the directors propose to revise", and s 202A(4) bars revision after a notice unless the Registrar agrees "on the manner in which to revise ... referred to in section 202B(2)(b)".
`s 202A(4)` takes the Registrar's agreement as a fact and `s 202B(2)` does not call `s 202A(4)`, so the two rules do not call each other.

### Seams where this part asks and the keel answers (table B)

One group call: `s 4(1) "related corporation" the other corporation is a related corporation of the corporation` (`sg-groups.l4`), from s 201B(11).
The keel's period functions are called as follows: `period: the date is at least a period before` in s 201(9)(a), s 201A(3); `period: the date is not later than the end of a period after` in s 201B(4); `period: the last day of a period after` in s 199(2), s 201AA(1), s 201B(4), s 202B(2), s 203(1)(b), s 203(4), s 203(6); `period: the latest day for an act a period before` in s 201(9)(a), s 203(1)(a).
The keel's `Party` type and its constructors are used by every regulative rule.
No keel module was changed, and no `NEEDS-CORE.md` is written: no type or constructor the core lacks was needed.

## Rules with no breach path (sgc1)

> Added 2026-11-27 (decided by Claude, assumed, not ruled): this section was written before the pass recorded in `lest-without-deadline.md`, and it is no longer true of the rules listed below.
> Each of them now takes an input-length `WITHIN` and can reach `BREACH`, so read "no time limit", "no deadline" and "no breach path" of them as the position before that pass, here and wherever else these notes say so of them:
>
> - `s 201B(7) the chairperson must convene a meeting of the committee on the auditor's request`
> - `s 203A(4) the company must send copies of the documents to the member who wishes to receive them`
> - `s 203(3) the company must furnish a copy of the last financial statements on request`
>
> The other rules named in this section are unchanged.

The brief asks for a trace that reaches `BREACH` for every regulative rule, and for a list of every rule where none can.
This part encodes 26 regulative rules.
Twelve have a trace to `BREACH`: a prohibition (`SHANT`) with the forbidden act in the trace, or a duty with a time limit (`WITHIN`) that the trace misses.
The 14 below are `MUST` rules with no time limit in the text, and no event can make a `MUST` with no limit breached: a late act still reads `FULFILLED`.
None has a deadline invented for it.
Where the text states a consequence of default it is an offence, and the offence is encoded as a penalty function over the facts (the last column), not as a breach in a trace.
Each rule has a `FULFILLED` trace in its tests file, and the third column says which also has a `RESIDUAL` trace that shows the duty still open.

| the rule | where | traces in its tests (kinds) | what the text states as the consequence of default | where that consequence is encoded |
| --- | --- | --- | --- | --- |
| `s 199(1) a company must cause accounting and other records to be kept` | sgc1-s199.l4 | FULFILLED, RESIDUAL | s 199(6): the company and every officer in default are guilty of an offence (a fine up to $10,000 or imprisonment up to 12 months, and a default penalty) | `s 199(6) the person is guilty of the offence this subsection creates`; `s 199(6) the most the person may be sentenced to on conviction` |
| `s 199(2A) a public company or a subsidiary company of a public company must devise and maintain a system of internal accounting controls` | sgc1-s199.l4 | FULFILLED | s 199(6), as above | `s 199(6) the person is guilty of the offence this subsection creates`; `s 199(6) the most the person may be sentenced to on conviction` |
| `s 199(3) a company must keep its accounting records open to inspection by the directors` | sgc1-s199.l4 | FULFILLED | s 199(6), as above | `s 199(6) the person is guilty of the offence this subsection creates`; `s 199(6) the most the person may be sentenced to on conviction` |
| `s 201(9)(b) the directors must cause the auditor's report to be attached to the financial statements` | sgc1-s201.l4 | FULFILLED, RESIDUAL | s 204(1A): a director who fails to comply with a provision of the Division other than s 201(2), (5) or (16) (a fine up to $10,000 or imprisonment up to 2 years) | `s 204(1A) the person is guilty of the offence this subsection creates` |
| `s 201(11) the directors of a subsidiary company must state the name of its ultimate parent corporation` | sgc1-s201.l4 | FULFILLED | s 204(1A), as above | `s 204(1A) the person is guilty of the offence this subsection creates` |
| `s 201(23) a company with an old financial year must attach a copy of the report to its return` | sgc1-s201-statement.l4 | FULFILLED, RESIDUAL | s 204(1A), as above | `s 204(1A) the person is guilty of the offence this subsection creates` |
| `s 201A(7) a company with an old financial year must attach a copy of the accounts to its return` | sgc1-s201a.l4 | FULFILLED, RESIDUAL | s 204(1A), as above | `s 204(1A) the person is guilty of the offence this subsection creates` |
| `s 201B(1) a listed company must have an audit committee` | sgc1-s201b.l4 | FULFILLED, RESIDUAL | s 204(1A), as above | `s 204(1A) the person is guilty of the offence this subsection creates` |
| `s 201B(6) the auditor must appear before the committee when required to do so` | sgc1-s201b.l4 | FULFILLED, RESIDUAL | none stated for the auditor: s 204(1A) speaks of a director | none |
| `s 201B(7) the chairperson must convene a meeting of the committee on the auditor's request` | sgc1-s201b.l4 | FULFILLED, RESIDUAL | s 204(1A), as above (the chairperson is a member of the committee, which s 201B(2) has the directors appoint "from among their number") | `s 204(1A) the person is guilty of the offence this subsection creates` |
| `s 201B(9) the directors of a listed company must describe the audit committee's functions in the statement` | sgc1-s201b.l4 | FULFILLED, RESIDUAL | s 204(1A), as above | `s 204(1A) the person is guilty of the offence this subsection creates` |
| `s 203(3) the company must furnish a copy of the last financial statements on request` | sgc1-s203.l4 | FULFILLED, RESIDUAL | s 203(3A): the company and every officer in default (a fine up to $5,000 and a default penalty), unless it is proved that the member or debenture holder has already made a request and been furnished with a copy | `s 203(3A) the person is guilty of the offence this subsection creates`; `s 203(3A) the most the person may be sentenced to on conviction` |
| `s 203A(4) the company must send copies of the documents to the member who wishes to receive them` | sgc1-s203a.l4 | FULFILLED, RESIDUAL | s 203A(7): the company and every officer in default (a fine up to $5,000 and a default penalty) | `s 203A(7) the person is guilty of the offence this subsection creates`; `s 203A(7) the most the person may be sentenced to on conviction` |
| `s 203A(6A) the directors must ensure that the summary financial statements comply` | sgc1-s203a.l4 | FULFILLED, RESIDUAL | s 204(1A), as above; s 203A(7) excludes a default of subsection (6A) | `s 204(1A) the person is guilty of the offence this subsection creates` |

Counts: 26 regulative rules; 12 with a trace to `BREACH`; 14 with none, all of them listed above.
Of the 14, 11 have a `RESIDUAL` trace (the duty still open) and all have a `FULFILLED` trace.
`s 201(17)` (a `SHANT`, with no time limit) is not in the list: its forbidden act is in a trace that reaches `BREACH`.

## What the text does not answer (sgc1)

79 branches of layer 1 answer `NOTHING`, each with a `NOTHING-kind` comment that gives one of the brief's reasons.
67 of them are a case outside the limit of a grant or a duty that the text states in its own words (marginal reading M19 lists the sites).
The other 12 are the cases where the text is silent, lists without closing the list, says "includes", or points outside the sources:

| provision | function | reason | what the comment says |
| --- | --- | --- | --- |
| s 201(2) | `s 201(2) the document complies with the Accounting Standards and gives a true and fair view` | points outside the text | whether a departure is allowed is not decided by the facts given |
| s 201(5) | `s 201(5) the consolidated financial statements and the balance sheet are as the subsection requires` | points outside the text | whether a departure is allowed is not decided by the facts given |
| s 201(17) | `s 201(17) the representation that the company has a reserve is barred` | silent | paragraphs (a) and (b) name a reserve invested outside the business and a reserve used in the business, and the subsection is silent on a reserve that is neither |
| s 201(18) | `s 201(18) the form and content provisions apply to the banking corporation as they stand` | points outside the text | "with such modifications and exceptions as are determined either generally or in any particular case by the Monetary Authority of Singapore": the determination is not among the sources |
| s 201(19) | `s 201(19) the Accounting Standards requirements apply to the charity as they stand` | points outside the text | "subject to any modification prescribed under section 12(1)(f) of that Act": the modification is not among the sources |
| s 201(20) | `s 201(20) the documents are within a reference to the preceding financial statements` | includes | "a reference to the preceding financial statements includes ..." leaves the list open |
| s 201(21) | `s 201(21) the laying of the documents is within a reference to the requirement to lay financial statements` | includes | "a reference to the requirement to lay financial statements before a company includes ..." leaves the list open |
| s 202(1) | `s 202(1) the directors are relieved by the Registrar's order from the requirement` | points outside the text | whether an order exists, and what it covers, is a fact about the Registrar's own order that the text does not state |
| s 202(2) | `s 202(2) the directors are relieved by the Registrar's order for a class of companies from the requirement` | points outside the text | whether an order exists, which class it names and which requirements it specifies are facts about the Registrar's own order that the text does not state |
| s 202B(2)(b) | `s 202B(2)(b) the directors must inform the Registrar how they propose to revise the financial statements` | silent | paragraph (b) states no condition of its own and paragraph (a) covers directors who do not propose to revise; whether (b) binds directors who do not propose to revise is not said (fork F-202B-b, NOTES.md) |
| s 202B(6) | `s 202B(6) the application to Court may be for the relief` | list not closed | the application "may be for" the two reliefs listed and the subsection does not close the list with "only" |
| s 203A(1) | `s 203A(1) the company may send a summary financial statement instead of copies of the documents referred to in section 203(1)` | points outside the text | the cases are those "as may be specified by regulations", which are not among the sources |

Questions the text leaves open, found while encoding, each with its finding or fork line:

- How the Registrar's approval under s 201(12) is given, since the text names the approval only as a condition and sets out no power or procedure for it.
- How long an order under s 202(2) lasts, since s 202(4) speaks only of an order "under subsection (1)" (F-202-4).
- The unit of the period the Registrar specifies in s 202B(1) (F-202B-days) and whether a longer period is a total or an addition (F-202B-longer).
- When a company exempt only under s 175A(1)(b) must send the documents, since s 203(1) names no period for it (finding 7, marginal reading M11).
- Who must give the auditors' statement of s 203A(6)(b), since the paragraph says the summary must "contain a statement by the company's auditors" and names no one who must supply it.
- Whether one default may be charged under both its own section and s 204(1A) (finding 3).
- What the old s 201(5) to (8), (11), (12) and (15) said, since s 201(22) keeps them for old financial years and they are not among the sources (finding 12).
- Whether the Minister has amended the Twelfth Schedule under s 8(7)(a) (finding 11).
- The amount of a default penalty (s 408, not among the sources).

## What the text turns out to say

Each finding was read off the text of this edition and carries its line numbers in `CoA1967.txt`.
A finding is a place where the text is odd, silent or easy to misread; none is advice, and each says what the encoding does.

1. **Seven units of the ranges are shown repealed or deleted.**
    They are s 200 (line 17924), s 200A (17926), s 201(3) and (4) (17945, 17947), s 201(6) (17974), s 201B(10) (18492) and s 203A(8) (18985).
    Each is a coverage row with the disposition `repealed or blank in this text` and no L4 name.

2. **s 204 gives imprisonment only to subsection (1A) and to the fraud penalties of subsection (3), and subsection (4) bars it unless the offence was wilful.**
    Subsection (1) is a fine of not more than $250,000 (18995-18997), subsection (1AA) a fine of not more than $50,000 (19003-19005), and subsection (1A) a fine of not more than $10,000 or imprisonment of not more than 2 years (19009-19025).
    Where an offence is committed with intent to defraud, subsection (3) gives, for (1), $250,000 or 3 years or both; for (1AA), $100,000 or 3 years or both; for (1A), $15,000 or 3 years or both (19042-19060).
    So a (1A) offence done with intent to defraud has a higher fine ceiling ($15,000) than the plain offence ($10,000), and subsection (3) replaces the plain penalty, not adds to it (marginal reading M14).
    Subsection (4) says that "a person shall not be sentenced to imprisonment for any offence under this section unless ... the offence was committed wilfully" (19062-19064), and "any offence under this section" includes the offences of subsection (3), so the 3-year terms need wilfulness too.
    `s 204(4) the person is barred from being sentenced to imprisonment for the offence` is a function of its own, and the penalty function gives the most the section allows without applying that bar.

3. **The same default can fall under two offence provisions with different ceilings, and the text does not say which governs.**
    A director's failure to comply with s 199 can be charged under s 199(6) against "every officer of the company who is in default" (a fine up to $10,000 or imprisonment up to 12 months and a default penalty: 17914-17918), because s 4(1) says "officer" includes "any director or secretary" (1574-1577), and under s 204(1A) (a fine up to $10,000 or imprisonment up to 2 years: 19009-19025).
    The same is true of the other provisions of the Division that carry their own offence (s 201AA(2), s 203(3A), s 203(7)(a) and s 203A(7)).
    No function here combines the two penalties or chooses between them: each provision has its own penalty function.

4. **A default of s 203A(6A) is not an offence of the company under s 203A(7), but it is within the words of s 204(1A)(a).**
    Section 203A(7) applies to "default ... in complying with this section other than subsection (6A) or any regulations made under subsection (9)" (18977-18978).
    Section 204(1A)(a) applies to a director who "fails to comply with any provision of this Division (other than section 201(2), (5) or (16))" (19009-19012), and s 203A(6A) is a provision of this Division.
    The encoding answers each provision's own question and does not join them.

5. **s 201AA(1) prints the paragraph label (b) twice.**
    The first (b) is at line 18341 ("in respect of any financial year for which the company need not hold an annual general meeting because of section 175A(1)") and the second at line 18352 ("and a copy of the auditors' report where such financial statements ... are duly audited").
    The rendering is a PDF turned to text, so the doubled label may belong to the rendering and not to the Act.
    The encoding reads the second (b) as the words that follow sub-paragraphs (i) and (ii) of the first, so the 5 years in paragraph (b) run from "the date on which the documents were sent" (18360-18362).

6. **s 202(1) and (2) cannot relieve a requirement of the Accounting Standards, and the route for those is s 201(12).**
    Both subsections exclude "a requirement of the Accounting Standards" from the Registrar's order (18533-18534, 18547-18548).
    The Registrar's approval of non-compliance with the Accounting Standards is s 201(12) (18067-18071), and a departure needed for a true and fair view is s 201(13) with the inclusions of s 201(14) (18077-18107).
    An order under s 202 therefore never answers a question about the Accounting Standards, and `s 202(1)` answers NOTHING for such a requirement (F-other-than).

7. **s 203(1)(b) and s 175A(1)(b) point past each other.**
    Section 203(1)(b) (18838-18842) sets the five months for a company that is "not required to hold an annual general meeting because of section 175A(1)(a)", which is the route by resolution.
    Section 175A(1)(b) (15812-15816, another part's range) exempts a private company that "has sent ... the documents mentioned in section 203(1) within the period specified in section 203(1)(b)".
    A company that is exempt only under s 175A(1)(b) therefore takes its five-month period from s 175A(1)(b) borrowing s 203(1)(b), and s 203(1) as printed gives it no period of its own: paragraph (a) counts from "the date of the meeting", and there is none.
    Section 203(4) (18881) applies "In a case referred to in subsection (1)(b)" and s 203(4A) (18889-18890) to a company exempt under s 175A(1)(b), in otherwise identical words.
    Marginal reading M11 records what this encoding does.

8. **s 201(5) lets the directors of a parent company leave out subsection (1), and the duty that replaces it names two documents.**
    The directors "need not comply with subsection (1) but must cause to be made out and laid" the consolidated financial statements and "a balance sheet dealing with the state of affairs of the parent company" (17952-17963).
    Section 201(2)'s compliance duty is for "the financial statements mentioned in subsection (1)" (17936-17938), and the consolidated documents carry their own compliance words at the end of subsection (5) (17965-17968).
    Section 204(1) treats "section 201(2) or (5)" as one offence (18995-18996).

9. **The words "parent company" and "subsidiary company" in this Division are s 209A's.**
    Section 209A (line 20125 onward, another part's range) defines "parent company" as "a company that is required under the Accounting Standards to prepare financial statements in relation to a group" and "subsidiary company" as "a subsidiary as defined in the Accounting Standards".
    So the keel's s 5 group functions are not what this Division asks, and this part takes each as a plain fact.

10. **s 201B(11) defines the negative and says to read the positive "accordingly".**
    It says a reference to a director who is not an executive director is a reference to a director who is "not an employee of, and does not hold any other office of profit in, the company or in any related corporation of that company in conjunction with his or her office of director and his or her membership of any audit committee" (18494-18499).
    The encoding builds the positive: an employee, or the holder of another office of profit, in the company or in a related corporation (marginal reading M6).

11. **The Twelfth Schedule can be changed by the Minister, and the encoding takes it as printed.**
    Section 8(7)(a) (line 2448) lets the Minister "add to, vary or amend" the Twelfth Schedule by notification in the Gazette, and the Schedule's own heading says "Sections 8(7) and 201(16)" (28899).
    The encoding has no input for a notification, so an amendment of the Schedule after 20 October 2026 is not asked about.

12. **s 201(22) keeps the old s 201 alive for old financial years, and the old text is not among the sources.**
    For a financial year that ended before 1 July 2015, "section 201(5) to (8), (11), (12) and (15) in force immediately before that date continues to apply" (18195-18203).
    The encoding states that those provisions continue to apply (`s 201(22) the earlier provisions of section 201 continue to apply to the company for the financial year`) and answers NOTHING for what they say.

13. **s 199(2) and s 201AA(1) set a period of years and the encoding reads each as a prohibition on disposal inside the period.**
    The text says the company "must retain" the records "for a period of not less than 5 years from the end of the financial year" (17869-17872), and "must cause to be kept" the documents "for a period of not less than 5 years" (18331-18337).
    Each has a `SHANT` rule (a prohibition on disposal, with the days as input) for a trace, and a `MAYBE BOOLEAN` function that says whether the duty to keep holds on a given day (JUST FALSE after the period: the periods ruling of 2026-11-05, item (a)).
    This is a modelling choice, assumed and not ruled.

14. **The text gives no unit and no time to some periods the Registrar sets.**
    Section 202B(1) has the Registrar "specify the period within which the directors must respond", and s 202B(2) has the directors respond "at the end of the period mentioned in subsection (1), or such longer period as the Registrar may allow" (18682-18689).
    The encoding takes a number of days (F-202B-days), reads "at the end of" as "by the end of" (M9), and takes the longer period as a total counted from the same day (F-202B-longer, M10).

15. **The 14 days of s 203(1)(a) and s 201(9)(a) count back from the meeting, and the day of the meeting is the keel's counting convention.**
    Both say "not less than 14 days before" the meeting (18835-18836, 18024-18026).
    This part uses the keel's `period: the latest day for an act a period before` (convention P1 to P9 in `sg-periods.l4`), assumed because the Interpretation Act 1965 is not among the sources (M17).

## What the stable binary does not accept

The binary governs where a skill describes something it rejects.
The Guide's list in section 5 (no `REFUSE`, `#ASSERT REFUSED` or `BECAUSE` except `LEST BREACH ... BECAUSE`; parenthesise every `NOT`; keep each `#ASSERT` on one line; bracket arithmetic across a line break; no `YMD` of one's own) was followed, and this part tested none of those again.
The two failures this part hit itself were both probed again on 2026-11-18 on `l4-main-110` and `l4-main-109`, with the same result on both:

- The possessive form after a constructor, `` JUST p's `the highest fine, in Singapore dollars` ``, is rejected: "You are trying to apply p (defined at ...) of type `s 199(6) penalty` (which is not a function) to 1 argument here."
- The form `` (`the highest fine, in Singapore dollars` OF p) `` in parentheses is accepted, and this part writes field access that way, with the OF form and a bracket, in every module and in the seat.
- When two imported records have a field of the same name and the possessive form is used, the file also gets "There are multiple definitions for the identifier ... and I do not have sufficient information to make a choice between them"; the OF form did not give that error in a small probe.
- This part nonetheless prefixes every penalty field with its provision label (`s 199(6) the highest fine, in Singapore dollars`), as the brief's naming rule asks for every top-level name, so that no two records in the merged seat can share a field.

Nothing else in the stable binary stopped this part: no construct a skill describes was found rejected, and none of the constructs of the Guide's list was needed that it forbids.
Two things about the build came up that are not the binary's: the text file carries U+2011 (non-breaking hyphen) in words such as "non‑compliance" (line 18088), so quotes copied from it keep the character, and `work/check_quotes.py` normalises it before comparing.
The second is that `srcrefs.py --strict` rejects a quote run followed by a second `@ref` that is not inside the nearest run above, so a function that needs its own `@ref` re-quotes its lines.

## What check.sh prints, and the other checks

The baseline `check.sh` replaced is the keel alone: 8 modules (`sg-*.l4`), 0 assertions satisfied.
`check.sh` was run as `L4=<l4-main-110> L4_MAIN=<l4-main-109> ./check.sh` from the deposit folder, after the last edit to any `.l4` file.
Its output, unedited:

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.109 (main, 4c887e0, 2026-11-04)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
sg-auditors.l4                                 0         0       0        0         0 |      0         0       0        0  same
sg-core.l4                                     0         0       0        0         0 |      0         0       0        0  same
sg-definitions.l4                              0         0       0        0         0 |      0         0       0        0  same
sg-groups.l4                                   0         0       0        0         0 |      0         0       0        0  same
sg-interests.l4                                0         0       0        0         0 |      0         0       0        0  same
sg-interpretation.l4                           0         0       0        0         0 |      0         0       0        0  same
sg-periods.l4                                  0         0       0        0         0 |      0         0       0        0  same
sg-solvency.l4                                 0         0       0        0         0 |      0         0       0        0  same
sgc1-cases-seat.l4                             0       328       0        0         0 |      0       328       0        0  same
sgc1-s199.l4                                   0         0       0        0         0 |      0         0       0        0  same
sgc1-s201-departures.l4                        0         0       0        0         0 |      0         0       0        0  same
sgc1-s201-statement.l4                         0         0       0        0         0 |      0         0       0        0  same
sgc1-s201.l4                                   0         0       0        0         0 |      0         0       0        0  same
sgc1-s201a.l4                                  0         0       0        0         0 |      0         0       0        0  same
sgc1-s201b.l4                                  0         0       0        0         0 |      0         0       0        0  same
sgc1-s202.l4                                   0         0       0        0         0 |      0         0       0        0  same
sgc1-s203.l4                                   0         0       0        0         0 |      0         0       0        0  same
sgc1-s203a.l4                                  0         0       0        0         0 |      0         0       0        0  same
sgc1-s204.l4                                   0         0       0        0         0 |      0         0       0        0  same
sgc1-sch12.l4                                  0         0       0        0         0 |      0         0       0        0  same
sgc1-seat.l4                                   0         0       0        0         0 |      0         0       0        0  same
sgc1-tests-s199.l4                             0        46       0        0         0 |      0        46       0        0  same
sgc1-tests-s201-departures.l4                  0        22       0        0         0 |      0        22       0        0  same
sgc1-tests-s201-statement.l4                   0        33       0        0         0 |      0        33       0        0  same
sgc1-tests-s201.l4                             0        48       0        0         0 |      0        48       0        0  same
sgc1-tests-s201a.l4                            0        75       0        0         0 |      0        75       0        0  same
sgc1-tests-s201b.l4                            0        55       0        0         0 |      0        55       0        0  same
sgc1-tests-s202.l4                             0        95       0        0         0 |      0        95       0        0  same
sgc1-tests-s203.l4                             0        65       0        0         0 |      0        65       0        0  same
sgc1-tests-s203a.l4                            0        35       0        0         0 |      0        35       0        0  same
sgc1-tests-s204.l4                             0        30       0        0         0 |      0        30       0        0  same
sgc1-tests-sch12.l4                            0        54       0        0         0 |      0        54       0        0  same
TOTAL (32 modules)                             0       886       0        0           |      0       886       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
exit 0
```

### Other checks, run after the last edit to any `.l4` file

- `srcrefs.py check` plain, `--refs` and `--strict` over every `sgc1-*.l4` (layer 1, tests, seat, cases), `RAW` being `inputs/CoA1967.txt`:
  - `plain`: srcrefs check: 821 src: lines, 106 runs, 171 locators, 0 problems
  - `--refs`: srcrefs check: 821 src: lines, 106 runs, 171 locators, 0 problems
  - `--strict`: srcrefs check: 821 src: lines, 106 runs, 171 locators, 0 problems
- Every trace's outcome against its `-- EXPECT` comment, on each build (`work/check_traces.py`):
  - l4-main-110: traces 54, mismatches 0; expected kinds {'FULFILLED': 27, 'BREACH': 15, 'RESIDUAL': 12}
  - l4-main-109: traces 54, mismatches 0; expected kinds {'FULFILLED': 27, 'BREACH': 15, 'RESIDUAL': 12}
- Quoted words of the `FALSE-kind` and `NOTHING-kind` comments against the text (`work/check_quotes.py`): 361 fragments, 8 not found, all 8 being the Guide's own words ("In short", "(other than X)", "this section gives no defence on these facts" and the grant ruling's phrase), not the Act's.
- Boundary mutations (`work/mutate.py`): one constant changed in a copy, the module's tests re-run, and the change must be detected:
  - s 203(1)(b): five months becomes six: 1 occurrence(s) changed in sgc1-s203.l4; sgc1-tests-s203.l4 satisfied/failed/errors before (65, 0, 0), after (61, 4, 0)
  - s 204(1): $250,000 becomes $250,001: 2 occurrence(s) changed in sgc1-s204.l4; sgc1-tests-s204.l4 satisfied/failed/errors before (30, 0, 0), after (28, 2, 0)
  - s 199(2): five years becomes four: 1 occurrence(s) changed in sgc1-s199.l4; sgc1-tests-s199.l4 satisfied/failed/errors before (46, 0, 0), after (43, 3, 0)
- Every function is named by an assertion or a trace of its tests file; every `#ASSERT` of a case file passes: assertions written equal assertions satisfied in every file (the table above).
- No expectation is meant to fail, and no test is kept apart for that: `check.sh`'s `expected_failed` is empty.


## The S1b ruling on failed gates (2026S1bC)

The Guide records this ruling at section 5, in the bullet that begins “Failed gates of the pure “may” functions”; it is copied here word for word, as the Guide asks of every ruling.

> - **Failed gates of the pure "may" functions of the two Singapore encodings: the split follows the background, not the holder's name (card S1b of the bench "Singapore Split Sites", option C as modified on the card; accepted by Meng).** Conditions as printed on the card: (1) It governs only the functions that stay Boolean after the protocol split, the pure gates (58 on the card's line); the type (i) sites, an unmet element of an offence, are unchanged. (2) A failed gate answers `JUST FALSE` where the function is a public body's power, a relief from an express bar or duty, or a gate the text closes (“so long as”, “only if”); it answers `NOTHING` where it states a company's or person's liberty, standard or privilege with no bar to relieve. (3) At the card's reading that changes 16 answers: 6 `NOTHING` to `JUST FALSE` at public bodies, and 10 `JUST FALSE` to `NOTHING` at liberties (C024, C046, C084, C115, C135, C138, C154, C155, C157, C159), each a fork line with the other reading and each borderline, because a relief and a liberty are a judgment. The 10 liberties that already answered `NOTHING` stay. (4) Applied one commit per part, each “assumed, not ruled” until the card was marked, flipping the branch each site's tag marks. (5) The difference between an express bar and silence stays in the code's `FALSE-kind` and `NOTHING-kind` comments and in NOTES, which is the provenance channel, and not in the truth value. (6) Recorded in this guide, with limit 3 of the grant ruling above replaced for the Singapore rows, and in the `NOTES.md` of the parts that carry limit 3 (the card's own wording; this paragraph is that record). (7) The ruling reaches the two Singapore encodings only. The UK (164 listed sites) and Israel stay on the Guide as it stands until Meng rules; until then the differential compares Singapore under C with the UK under limit 3. The sites the 16 answers belong to: the public-body powers that went from `NOTHING` to `JUST FALSE` are s 173F (C045), s 32(4) (C106), s 139(6) (F018), s 139(10) (F019), s 282AA(1) (F057), s 281(1) (F062); the liberties that went from `JUST FALSE` to `NOTHING` are s 145(1), s 202A(2), s 21(7), s 130(2), s 173J(3), s 179(2), s 387A(1), s 387B(1), s 387D, s 390(1). Meng's note, verbatim: “Suggest that the changed encodings, and future rules encoded under this ruling, be marked with a greppable string like 2026S1bC to show where this rule took effect. Then in future we can revisit and review the consequences of this rule on encodings that haven’t been done today.” Marked 2026-11-21T12:17:37.989Z (accept, option C, not blind), ruled 2026-11-21, so the commits that applied it are ruled and no longer “assumed, not ruled”. Reading of the note (assumed, not ruled): each function this ruling changed, and each function encoded later under it in these two encodings, carries the string `2026S1bC` in its `FALSE-kind` or `NOTHING-kind` comment, and on its `FORK` line where it has one, so that `grep -rn 2026S1bC` lists where the rule took effect and a later review can find its consequences. Bench: https://claude.ai/artifact/SYSny5zjFYHHcMFeNYi5RX

Sites of this part changed under it (2026S1bC): s 202A(2), `s 202A(2) the directors may cause the financial statements to be revised` (fork F-202A-2, `sgc1-s202.l4:194`), from `JUST FALSE` to `NOTHING` for the "Where this section applies" gate: the directors' own liberty with no bar to relieve. The "if it appears to the directors" gate of the same function answered `NOTHING` before and still does.
