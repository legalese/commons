# NOTES (sgn): Companies Act 1967 (Singapore), Part 11A, ss 386AA to 386AP

Part agent `sgn`, one context, no subagents.
Source lines 25372-27069 of `inputs/CoA1967.txt`.
The stable build 1.6.110 (`l4-main-110`) wrote and checked every file; the second stable build, 1.6.109 (`l4-main-109`), is the main-build comparison that `check.sh` runs.
Where PLAN.md and the brief differ, the brief governs (the next-but-one section says where that mattered).

## Edition encoded

The Companies Act 1967, 2020 Revised Edition, Singapore Statutes Online informal consolidation "version in force from 6/5/2026 to 20/10/2026", retrieved 2026-10-09, carrying the amendments up to Act 24 of 2025.
A later consolidation may exist and was not read.
The encoding is of that text only.
The text is a rendering of the Act (a PDF turned into plain text), not the official text, and nothing here is verified against the official text.
Amendment marks (`[15/2017]`, `[Act 23 of 2024 wef 16/06/2025]`) and the page furniture lines are not text and are never quoted as rules.
The quotations in the modules are copied mechanically from the text file by script; no sentence of the Act is typed by hand.
This work states no endorsement by, and no association with, the Singapore Government or the Attorney-General's Chambers.

## Where this brief and PLAN.md differ

One difference touched the work.
PLAN.md section 6 (the `sgn` row) says to expect the keel's `s 4(1) "company"`, `"foreign company"` and `"corporation"` terms, and the keel's `s 5` and `s 7` functions "where the text calls them".
Part 11A's own text cites only `s 4` (lines 25925 and 25928, the definitions of "chief executive officer" and "director with executive control"), `s 6` (line 25637, the employer of a legal counsel) and `s 396A` (line 26846).
So no `s 5` or `s 7` function is called anywhere, and the keel's `s 4(1) "company"` is not called either: the layer-1 functions take a company or a foreign company as plain facts, because the text itself speaks of a company and a foreign company as two things the Part applies to (s 386AA(1)).
`s 4(1) "chief executive officer"` is called, once, in `s 386AFA(8) "chief executive officer"` (`sgn-register.l4`).
`s 6` is taken as a plain fact under a name of its own, `the corporation is related under section 6 to the corporation that employs the legal counsel`, and not through the keel's one-fact function `s 4(1) "related corporation" the other corporation is a related corporation of the corporation` (`sg-groups.l4`), because that function's input, `the other corporation is deemed to be related to the corporation by virtue of section 6`, does not say which of the two corporations in `s 386AE(2) "employer"` is meant.
That is a difference from the PLAN row for `sgn` ("takes the keel's group ... functions"), made on my own judgment and not ruled: swapping in the keel's function is a change to the one function `s 386AE(2) "employer"` and its input name, and the seat question for it.
The grant ruling of 2026-11-12 (a function named for a grant answers `NOTHING` when an "if" gate fails) is in the brief and in the Guide (lines 96-99); I applied it, and the fork register has one line for each function it governs (F-GR1 to F-GR9).

## What is here

| file | what it is |
| --- | --- |
| `sgn-application.l4` | ss 386AA, 386AB, 386AC: application, definitions, "registrable" |
| `sgn-evidence.l4` | ss 386AD, 386AE: the state of mind of a corporation, legal privilege |
| `sgn-register.l4` | ss 386AF, 386AFA: the register of controllers, the additional particulars; the one timing helper that every module calls |
| `sgn-notices.l4` | ss 386AG, 386AH, 386AI, 386AIA, 386AJ, 386AK: notices to controllers, and the controllers' own duties |
| `sgn-nominees.l4` | ss 386AKA, 386AL, 386ALA, 386ALB: the registers of nominee directors and nominee shareholders, and the nominee's duty to disclose |
| `sgn-registrar.l4` | ss 386AM, 386AN, 386ANA, 386AO, 386AP: the power to enforce, the central registers, codes of practice, exemption |
| `sgn-tests-application.l4`, `sgn-tests-evidence.l4`, `sgn-tests-register.l4`, `sgn-tests-notices.l4`, `sgn-tests-nominees.l4`, `sgn-tests-nominees-rules.l4`, `sgn-tests-registrar.l4` | layer-1 tests: assertions and traces |
| `sgn-seat.l4`, `sgn-cases-seat.l4` | layer 2: 58 questions "Under section N, ...", and the cases that exercise them |
| `PROGRESS.md` | the encoder's own working note |

Layer 1 has 273 definitions (functions and constants) and 71 regulative rules: 53 `MUST` with a time limit (a limit of 0 days where the text says "on that date"), 13 `MUST` with no time limit, 5 `SHANT`.
It has 666 assertions and 138 traces in the test files, and the case file adds 150 more assertions, so `check.sh` counts 816 satisfied.
Every trace carries a `-- EXPECT` word and was compared with what it prints on both builds by `work/traces.py` (0 mismatches).
The scripts that wrote the generated files (`work/pre.py`, `work/gen.py`, `work/gen_rule_tests.py`, `work/seat/*.py`, `work/cov.py`, `work/mknotes.py`) are in the scratch folder, not in this one.

## Coverage (sgn)

One row per unit of the text.
The rows are a partition of lines 25372-27069 made by script from the `@ref` locators of the modules: a row starts at each distinct locator start, and at each heading and each deleted paragraph.
A row lists the provision label(s) of the declarations whose locator covers it, its disposition, and the L4 name(s).
A row's first name is the declaration that starts it; later labels are declarations of the same provision (a rule and a function over the same text, or a paragraph inside a subsection) whose locators overlap it.
Rows listed: 210.
The script's partition has 235 cells; 25 of them hold only blank lines or an amendment mark (a blank line after a heading or a deleted line, and the mark under the Part title) and are not listed, because they are not text.
The audit before and after: the first run of `work/cov.py`, before the encoding was finished, had 206 cells and 33 gap rows; nine of those gap rows were operative text with no function yet (the lead-in of s 386AB, the lead-in of s 386AE(2) at 25628, the last line of s 386AF(1) at 25673, the lead-in of s 386AFA(8) at 25920, and the five exemption subsections s 386AG(4), s 386AH(4), s 386AI(4), s 386AJ(3) and s 386AK(3)); each was then encoded, and the final run has 235 cells and 28 gap rows (23 headings and 5 deleted lines).
Non-blank lines in the range: 1178, of which 972 are text (neither page furniture nor a bare amendment mark).
Text lines in no row: 0 (checked by `work/cov.py`, which prints the number, and again by `work/mknotes.py`).
Dispositions: encoded 33; fork 149 (the row's provision has at least one branch that the fork register below records); inert 23 (all reason 1: the Part title and the marginal headings, which create no rule; none for reasons 2 or 3); repealed or blank in this text 5.
The five "repealed or blank" rows are the five `[Deleted ...]` lines of the range: a deleted definition in s 386AB (line 25480), paragraph (a) of s 386AL(2) (26435), s 386AL(7) (26512), paragraph (a) of s 386ALB(2) (26628) and paragraph (a) of s 386ALB(4) (26678).
Where the row of a deleted paragraph shows a span, the span is the subsection that surrounds it, which is encoded around the gap (finding 6).

| lines | provision | disposition | L4 name |
| --- | --- | --- | --- |
| 25372-25377 | heading: PART 11A REGISTER OF CONTROLLERS, NOMINEE DIRECTORS AND NOMINEE SHAREHOLDERS OF COMPANIES | inert (reason 1: heading or Part title, no rule) | none |
| 25381 | heading: Application of this Part | inert (reason 1: heading or Part title, no rule) | none |
| 25383-25393 | s 386AA(1)(a), s 386AA(1)(b), s 386AA(1) | fork (F-AA1) | `s 386AA(1)(a) this Part applies to the company`; `s 386AA(1)(b) this Part applies to the foreign company`; `s 386AA(1) this Part applies to the company or foreign company` |
| 25394-25407 | s 386AA(1A) | encoded | `s 386AA(1A) the provision applies to the person` |
| 25408-25417 | s 386AA(2) | encoded | `s 386AA(2) the obligation to comply with this Part extends to the person` |
| 25418-25422 | s 386AA(3) | encoded | `s 386AA(3) this Part extends to the act or omission` |
| 25423 | heading: Interpretation of this Part | inert (reason 1: heading or Part title, no rule) | none |
| 25425-25426 | s 386AB | fork (F-AB1) | `s 386AB the definitions of this Part apply here` |
| 25427-25429 | s 386AB "approved exchange" | encoded | `s 386AB "approved exchange" the exchange is an approved exchange` |
| 25430-25432 | s 386AB "controller" | encoded | `s 386AB "controller" the person is a controller of the company or foreign company` |
| 25433-25437 | s 386AB "corporate controller" | encoded | `s 386AB "corporate controller" the person is a corporate controller` |
| 25438-25442 | s 386AB "individual controller" | encoded | `s 386AB "individual controller" the person is an individual controller` |
| 25443-25446 | s 386AB "legal entity" | fork (F-AB2) | `s 386AB "legal entity" the body is a legal entity` |
| 25447-25449 | s 386AB "limited liability partnership" | encoded | `s 386AB "limited liability partnership" the partnership is a limited liability partnership` |
| 25450-25459 | s 386AB "member of the public" | fork (F-AB3) | `s 386AB "member of the public" the person is a member of the public` |
| 25460-25479 | s 386AB "register of controllers" | encoded | `s 386AB "register of controllers" the register is the register of controllers` |
| 25480 | the text shows `[Deleted by Act 22 of 2024 wef 09/06/2025]` | repealed or blank in this text | none |
| 25482-25484 | s 386AB "significant control" | encoded | `s 386AB "significant control" the person has significant control` |
| 25485-25489 | s 386AB "significant interest" | encoded | `s 386AB "significant interest" the person has a significant interest` |
| 25490 | heading: Meaning of “registrable” | inert (reason 1: heading or Part title, no rule) | none |
| 25492-25499 | s 386AC | encoded | `s 386AC the controller is registrable` |
| 25500-25532 | s 386AC(c), s 386AC | encoded | `s 386AC(c) the controller is of a kind that paragraph (c) lists`; `s 386AC the controller is registrable` |
| 25533 | heading: State of mind of corporation, unincorporated association, etc. | inert (reason 1: heading or Part title, no rule) | none |
| 25535-25548 | s 386AD(1) | fork (F-AD1, F-AD2) | `s 386AD(1) the evidence is evidence that the corporation had that state of mind` |
| 25549-25563 | s 386AD(2) | fork (F-AD1, F-AD2) | `s 386AD(2) the evidence is evidence that the unincorporated association or partnership had that state of mind` |
| 25564 | heading: Meaning of “legal privilege” | inert (reason 1: heading or Part title, no rule) | none |
| 25566-25627 | s 386AE(1) | fork (F-AE1) | `s 386AE(1) the information or document is subject to legal privilege` |
| 25628-25633 | s 386AE(2) "client" | encoded | `s 386AE(2) "client" the person is within the word client` |
| 25634-25653 | s 386AE(2) "employer" | encoded | `s 386AE(2) "employer" the person is within the word employer` |
| 25654-25657 | s 386AE(2) "lawyer" | fork (F-AB2) | `s 386AE(2) "lawyer" the person is a lawyer` |
| 25658-25663 | s 386AE(2) "legal counsel" | fork (F-AB2) | `s 386AE(2) "legal counsel" the person is a legal counsel` |
| 25664 | heading: Register of controllers | inert (reason 1: heading or Part title, no rule) | none |
| 25666-25678 | s 386AF(1) | fork (F-AF1) | `s 386AF(1) the last day by which the company must have kept its register`; `s 386AF(1) a company incorporated on or after 31 March 2017 but before the appointed day must keep a register not later than 30 days after incorporation` |
| 25679-25684 | s 386AF(1A) | fork (F-AF1) | `s 386AF(1A) the day on which the company must start to keep its register`; `s 386AF(1A) a company incorporated on or after the appointed day must keep a register starting on the date of incorporation` |
| 25685-25690 | s 386AF(2) | fork (F-AF1) | `s 386AF(2) the last day by which the company must have kept its register`; `s 386AF(2) a company incorporated before 31 March 2017 must keep a register not later than 60 days after that date` |
| 25691-25698 | s 386AF(3) | fork (F-AF1) | `s 386AF(3) the last day by which the company must have kept its register`; `s 386AF(3) a company that becomes subject to this Part must keep a register not later than 60 days after the Part applies or re-applies` |
| 25699-25707 | s 386AF(4) | fork (F-AF1) | `s 386AF(4) the last day by which the foreign company must have kept its register`; `s 386AF(4) a foreign company registered on or after 31 March 2017 but before the appointed day must keep a register not later than 30 days after registration` |
| 25708-25713 | s 386AF(4A) | fork (F-AF1) | `s 386AF(4A) the day on which the foreign company must start to keep its register`; `s 386AF(4A) a foreign company registered on or after the appointed day must keep a register starting on the date of registration` |
| 25714-25719 | s 386AF(5) | fork (F-AF1) | `s 386AF(5) the last day by which the foreign company must have kept its register`; `s 386AF(5) a foreign company registered before 31 March 2017 must keep a register not later than 60 days after that date` |
| 25720-25730 | s 386AF(6) | fork (F-AF1) | `s 386AF(6) the last day by which the foreign company must have kept its register`; `s 386AF(6) a foreign company that becomes subject to this Part must keep a register not later than 60 days after the Part applies or re-applies` |
| 25731-25750 | s 386AF(7), s 386AF(7)(a), s 386AF(7)(aa), s 386AF(7)(b) ... | fork (F-AF2) | `s 386AF(7) the register is as the subsection requires`; `s 386AF(7)(a) a company or foreign company must ensure that its register contains the prescribed particulars`; `s 386AF(7)(aa) a company or foreign company must ensure that its register contains the note and particulars required under section 386AFA(3)` (and 2 more of the same provision) |
| 25751-25756 | s 386AF(8) | fork (F-AF5) | `s 386AF(8) the company or foreign company has entered the particulars and updated the register in time and in the prescribed manner`; `s 386AF(8) a company or foreign company must enter the particulars and update its register within the prescribed time` |
| 25757-25763 | s 386AF(9), s 386AF(9)(a) | fork (F-AF5) | `s 386AF(9) the company or foreign company has done what the subsection requires`; `s 386AF(9)(a) a company or foreign company must enter or update the particulars of a controller after the controller confirms them` |
| 25764-25770 | s 386AF(9), s 386AF(9)(b) | fork (F-AF5) | `s 386AF(9) the company or foreign company has done what the subsection requires`; `s 386AF(9)(b) a company or foreign company that does not receive the confirmation must enter or update the particulars with a note` |
| 25771-25776 | s 386AF(10) | encoded | `s 386AF(10) the controller's confirmation is a confirmation for the purposes of subsection (9)(a)` |
| 25777-25785 | s 386AF(11) | fork (F-AF3) | `s 386AF(11) the company or foreign company is barred from disclosing the register to the person`; `s 386AF(11) a company or foreign company must not disclose the register to a member of the public` |
| 25786-25801 | s 386AF(12) | fork (F-AF6) | `s 386AF(12) the company is guilty of the offence`; `s 386AF(12) the officer of the company is guilty of the offence`; `s 386AF(12) the most the company or an officer in default may be sentenced to on conviction` |
| 25802-25817 | s 386AF(13) | fork (F-AF6) | `s 386AF(13) the foreign company is guilty of the offence`; `s 386AF(13) the officer of the foreign company is guilty of the offence`; `s 386AF(13) the most the foreign company or an officer in default may be sentenced to on conviction` |
| 25818-25823 | s 386AF(14) | fork (F-AL1) | `s 386AF(14) "appointed day" the appointed day` |
| 25824 | heading: Additional particulars | inert (reason 1: heading or Part title, no rule) | none |
| 25826-25835 | s 386AFA(1) | fork (F-AFA1) | `s 386AFA(1) this section applies to the company or foreign company` |
| 25836-25843 | s 386AFA(2) | fork (F-AFA1) | `s 386AFA(2) the person is taken to be a registrable controller of the company or foreign company for the purposes of this Part` |
| 25844-25867 | s 386AFA(3) | fork (F-AFA1) | `s 386AFA(3) the company or foreign company has entered in its register what the subsection requires`; `s 386AFA(3) a company or foreign company to which the section applies must enter the note and the prescribed particulars` |
| 25868-25889 | s 386AFA(4) | fork (F-AF5) | `s 386AFA(4) the company or foreign company has entered the matters within the prescribed period`; `s 386AFA(4) a company or foreign company must enter the matters mentioned in subsection (3) within the prescribed period` |
| 25890-25896 | s 386AFA(5) | fork (F-AF5) | `s 386AFA(5) the company or foreign company has updated its register within the prescribed period`; `s 386AFA(5) a company or foreign company must update its register of controllers within the prescribed period after it knows of a change` |
| 25897-25911 | s 386AFA(6) | fork (F-AFA2) | `s 386AFA(6) the company or foreign company has entered the note at the same time`; `s 386AFA(6) a company or foreign company must at the same time enter the note` |
| 25912-25919 | s 386AFA(7) | fork (F-AF6) | `s 386AFA(7) the company or foreign company is guilty of the offence`; `s 386AFA(7) the officer of the company or foreign company is guilty of the offence`; `s 386AFA(7) the most the company or foreign company or an officer in default may be sentenced to on conviction` |
| 25920-25931 | s 386AFA(8) "chief executive officer" | encoded | `s 386AFA(8) "chief executive officer" the person is a chief executive officer of the company or foreign company` |
| 25932-25941 | s 386AFA(8) "director with executive control" | encoded | `s 386AFA(8) "director with executive control" the person is a director with executive control` |
| 25942-25951 | s 386AFA(9) | encoded | `s 386AFA(9) the reference to a controller or a registrable controller includes the person` |
| 25952-25953 | heading: Duty of company and foreign company to investigate and obtain information | inert (reason 1: heading or Part title, no rule) | none |
| 25955-25960 | s 386AG(1) | fork (F-AG1) | `s 386AG(1) the company or foreign company has complied with the duty to take reasonable steps`; `s 386AG(1) a company or foreign company must take reasonable steps to find out and identify its registrable controllers` |
| 25961-25998 | s 386AG(2) | fork (F-AG2, F-AH1) | `s 386AG(2) the company or foreign company must give a notice to the person`; `s 386AG(2) the notice requires what the paragraph requires` |
| 25999-26006 | s 386AG(3)(a) and (b) | encoded | `s 386AG(3)(a) and (b) the notice is as the subsection requires` |
| 26007-26014 | s 386AG(3)(c) | fork (F-AF5) | `s 386AG(3)(c) the company or foreign company has given the notice in time`; `s 386AG(2) and (3)(c) a company or foreign company must give the notice within the prescribed period after it first knows` |
| 26015-26024 | s 386AG(4) | fork (F-AG2) | `s 386AG(4) subsection (2) requires the company or foreign company to give notice in respect of the information` |
| 26025-26034 | s 386AG(5) | fork (F-AF6) | `s 386AG(5) the company or foreign company is guilty of the offence`; `s 386AG(5) the officer of the company or foreign company is guilty of the offence`; `s 386AG(5) the most the company or foreign company or an officer in default may be sentenced to on conviction` |
| 26035-26044 | s 386AG(6) | fork (F-AG3) | `s 386AG(6) the addressee is required to provide the information`; `s 386AG(6) the addressee has complied with the notice within the time specified`; `s 386AG(6) an addressee must comply with the notice within the time specified in it` |
| 26045-26052 | s 386AG(7) | fork (F-AF6) | `s 386AG(7) the addressee is guilty of the offence`; `s 386AG(7) the most the addressee may be sentenced to on conviction` |
| 26053-26054 | heading: Duty of company and foreign company to keep information up‑to‑date | inert (reason 1: heading or Part title, no rule) | none |
| 26056-26071 | s 386AH(1) | fork (F-AH1) | `s 386AH(1) the company or foreign company must give notice to the registrable controller`; `s 386AH(1) the notice requires what the subsection requires` |
| 26072-26078 | s 386AH(2) | fork (F-AF5) | `s 386AH(2) the company or foreign company has given the notice in time`; `s 386AH(1) and (2) a company or foreign company must give the notice within the prescribed period after it first knows of the change` |
| 26079-26085 | s 386AH(3) | encoded | `s 386AH(3) the notice is as section 386AG(3)(a) and (b) require` |
| 26086-26094 | s 386AH(4) | fork (F-AG2) | `s 386AH(4) subsection (1) requires the company or foreign company to give notice in respect of the information` |
| 26095-26109 | s 386AH(5) | fork (F-AF6) | `s 386AH(5) the company or foreign company is guilty of the offence`; `s 386AH(5) the officer of the company or foreign company is guilty of the offence`; `s 386AH(5) the most the company or foreign company or an officer in default may be sentenced to on conviction` |
| 26110-26118 | s 386AH(6) | fork (F-AF6, F-AG3) | `s 386AH(6) the addressee has complied with the notice within the time specified`; `s 386AH(6) the addressee is guilty of the offence`; `s 386AH(6) the most the addressee may be sentenced to on conviction` |
| 26119-26130 | s 386AH(7) | fork (F-AH2) | `s 386AH(7) a relevant change occurs` |
| 26131 | heading: Duty of company and foreign company to correct information | inert (reason 1: heading or Part title, no rule) | none |
| 26133-26141 | s 386AI(1) | fork (F-AH1) | `s 386AI(1) the company or foreign company must give notice to the registrable controller`; `s 386AI(1) the notice requires what the subsection requires` |
| 26142-26148 | s 386AI(2) | fork (F-AF5) | `s 386AI(2) the company or foreign company has given the notice in time`; `s 386AI(1) and (2) a company or foreign company must give the notice within the prescribed period after it first knows the information is incorrect` |
| 26149-26158 | s 386AI(3) | encoded | `s 386AI(3) the notice is as section 386AG(3)(a) and (b) require` |
| 26159-26167 | s 386AI(4) | fork (F-AG2) | `s 386AI(4) subsection (1) requires the company or foreign company to give notice in respect of the information` |
| 26168-26178 | s 386AI(5) | fork (F-AF6) | `s 386AI(5) the company or foreign company is guilty of the offence`; `s 386AI(5) the officer of the company or foreign company is guilty of the offence`; `s 386AI(5) the most the company or foreign company or an officer in default may be sentenced to on conviction` |
| 26179-26187 | s 386AI(6) | fork (F-AF6, F-AG3) | `s 386AI(6) the addressee has complied with the notice within the time specified`; `s 386AI(6) the addressee is guilty of the offence`; `s 386AI(6) the most the addressee may be sentenced to on conviction` |
| 26188-26189 | heading: Duty of company and foreign company to ensure information in register is up‑to‑date and correct | inert (reason 1: heading or Part title, no rule) | none |
| 26191-26210 | s 386AIA(1) | fork (F-AIA1, F-AIA2) | `s 386AIA(1) the notice serves the purposes the subsection lists`; `s 386AIA(1) the company or foreign company has given the next notice at the prescribed frequency`; `s 386AIA(1) a company or foreign company must give a notice to each registrable controller at the prescribed frequency` |
| 26211-26219 | s 386AIA(2) | encoded | `s 386AIA(2) the notice is as the subsection requires` |
| 26220-26223 | s 386AIA(3) | fork (F-AG3) | `s 386AIA(3) the addressee has complied with the notice no later than the time specified`; `s 386AIA(3) an addressee must comply with the notice no later than the time specified in it` |
| 26224-26229 | s 386AIA(4) | fork (F-AF6) | `s 386AIA(4) the company or foreign company is guilty of the offence`; `s 386AIA(4) the officer of the company or foreign company is guilty of the offence`; `s 386AIA(4) the most the company or foreign company or an officer in default may be sentenced to on conviction` |
| 26230-26233 | s 386AIA(5) | fork (F-AF6) | `s 386AIA(5) the addressee is guilty of the offence`; `s 386AIA(5) the most the addressee may be sentenced to on conviction` |
| 26234-26245 | s 386AIA(6) | fork (F-AH2) | `s 386AIA(6) a relevant change occurs` |
| 26246 | heading: Controller’s duty to provide information | inert (reason 1: heading or Part title, no rule) | none |
| 26248-26266 | s 386AJ(1) | fork (F-AJ1) | `s 386AJ(1) the person must notify the company or foreign company` |
| 26267-26274 | s 386AJ(2) | fork (F-AF5) | `s 386AJ(1) and (2) the person has complied with the requirements in time`; `s 386AJ(1) and (2) a person who is a registrable controller must notify the company or foreign company within the prescribed period` |
| 26275-26282 | s 386AJ(3) | fork (F-AG2) | `s 386AJ(3) subsection (1) requires the person to comply` |
| 26283-26290 | s 386AJ(4) | fork (F-AF6) | `s 386AJ(4) the person is guilty of the offence`; `s 386AJ(4) the most the person may be sentenced to on conviction` |
| 26291 | heading: Controller’s duty to provide change of information | inert (reason 1: heading or Part title, no rule) | none |
| 26293-26304 | s 386AK(1) | fork (F-AJ1) | `s 386AK(1) the person must notify the company or foreign company of the relevant change` |
| 26305-26314 | s 386AK(2) | fork (F-AF5) | `s 386AK(1) and (2) the person has notified the company or foreign company of the relevant change in time`; `s 386AK(1) and (2) a registrable controller must notify the company or foreign company of a relevant change within the prescribed period` |
| 26315-26322 | s 386AK(3) | fork (F-AG2) | `s 386AK(3) subsection (1) requires the person to comply` |
| 26323-26330 | s 386AK(4) | fork (F-AF6) | `s 386AK(4) the person is guilty of the offence`; `s 386AK(4) the most the person may be sentenced to on conviction` |
| 26331-26340 | s 386AK(5) | fork (F-AH2) | `s 386AK(5) a relevant change occurs` |
| 26341 | heading: Register of nominee directors | inert (reason 1: heading or Part title, no rule) | none |
| 26343-26347 | s 386AKA(1) | fork (F-AF2, F-AKA1) | `s 386AKA(1) the company or foreign company has kept the register of nominee directors as required`; `s 386AKA(1) a company or foreign company must keep a register of nominee directors` |
| 26348-26352 | s 386AKA(2) | fork (F-AF3) | `s 386AKA(2) a company or foreign company must not disclose the register of nominee directors to a member of the public`; `s 386AKA(2) the company or foreign company is barred from disclosing the register of nominee directors to the person` |
| 26353-26358 | s 386AKA(3) | encoded | `s 386AKA(3) the company or foreign company has entered the fact and the particulars in time`; `s 386AKA(3) a company or foreign company must enter the fact and the particulars in its register of nominee directors within 7 days after it is informed` |
| 26359-26372 | s 386AKA(4) | encoded | `s 386AKA(4) the company or foreign company has entered the cessation in time`; `s 386AKA(4) a company or foreign company must enter the cessation of a director as a nominee within 7 days after it is informed` |
| 26373-26383 | s 386AKA(5) | encoded | `s 386AKA(5) the company or foreign company has entered the change in time`; `s 386AKA(5) a company or foreign company must enter the new particulars within 7 days after it is informed of a change` |
| 26384-26391 | s 386AKA(6) | fork (F-AF6) | `s 386AKA(6) the company or foreign company is guilty of the offence`; `s 386AKA(6) the officer of the company or foreign company is guilty of the offence`; `s 386AKA(6) the most the company or foreign company or an officer in default may be sentenced to on conviction` |
| 26392 | heading: Nominee directors | inert (reason 1: heading or Part title, no rule) | none |
| 26394-26396 | s 386AL(1) | fork (F-AL2) | `s 386AL(1) the last day by which the director must have informed the company` |
| 26397-26403 | s 386AL(1), s 386AL(1)(a) | fork (F-AL2) | `s 386AL(1) the last day by which the director must have informed the company`; `s 386AL(1)(a) a director of a company incorporated on or after 31 March 2017 but before the appointed day who is a nominee on the date of incorporation must inform the company within 30 days after the date of incorporation` |
| 26404-26416 | s 386AL(1), s 386AL(1)(b) | fork (F-AL2) | `s 386AL(1) the last day by which the director must have informed the company`; `s 386AL(1)(b) a director of a company incorporated on or after 31 March 2017 but before the appointed day who becomes a nominee after the date of incorporation must inform the company within 30 days after becoming a nominee` |
| 26417-26419 | s 386AL(1A) | fork (F-AL2) | `s 386AL(1A) the last day by which the director must have informed the company` |
| 26420-26424 | s 386AL(1A), s 386AL(1A)(a) | fork (F-AL2) | `s 386AL(1A) the last day by which the director must have informed the company`; `s 386AL(1A)(a) a director of a company incorporated on or after the appointed day who is a nominee on the date of incorporation must inform the company on that date` |
| 26425-26432 | s 386AL(1A), s 386AL(1A)(b) | fork (F-AL2) | `s 386AL(1A) the last day by which the director must have informed the company`; `s 386AL(1A)(b) a director of a company incorporated on or after the appointed day who becomes a nominee after the date of incorporation must inform the company within 30 days after becoming a nominee` |
| 26433-26434 | s 386AL(2) | fork (F-AL2) | `s 386AL(2) the last day by which the director must have informed the company` |
| 26435 | the text shows `(a) [Deleted by Act 23 of 2024 wef 16/06/2025]` (in the span of s 386AL(2)) | repealed or blank in this text | none |
| 26436 | s 386AL(2) | fork (F-AL2) | `s 386AL(2) the last day by which the director must have informed the company` |
| 26437-26446 | s 386AL(2), s 386AL(2)(b) | fork (F-AL2) | `s 386AL(2) the last day by which the director must have informed the company`; `s 386AL(2)(b) a director of a company incorporated before 31 March 2017 who becomes a nominee after 31 March 2017 must inform the company within 30 days after becoming a nominee` |
| 26447-26449 | s 386AL(3) | fork (F-AL2) | `s 386AL(3) the last day by which the director must have informed the company` |
| 26450-26452 | s 386AL(3), s 386AL(3)(a) | fork (F-AL2) | `s 386AL(3) the last day by which the director must have informed the company`; `s 386AL(3)(a) a director must inform the company within 30 days after the director ceases to be a nominee` |
| 26453-26458 | s 386AL(3), s 386AL(3)(b) | fork (F-AL2) | `s 386AL(3) the last day by which the director must have informed the company`; `s 386AL(3)(b) a director must inform the company within 30 days after a change to the particulars provided to the company` |
| 26459-26461 | s 386AL(4) | fork (F-AL2) | `s 386AL(4) the last day by which the director must have informed the foreign company` |
| 26462-26469 | s 386AL(4), s 386AL(4)(a) | fork (F-AL2) | `s 386AL(4) the last day by which the director must have informed the foreign company`; `s 386AL(4)(a) a director of a foreign company registered on or after the appointed day who is a nominee on the date of registration must inform the foreign company on that date` |
| 26470-26477 | s 386AL(4), s 386AL(4)(b) | fork (F-AL2) | `s 386AL(4) the last day by which the director must have informed the foreign company`; `s 386AL(4)(b) a director of a foreign company registered on or after the appointed day who becomes a nominee after the date of registration must inform the foreign company within 30 days after becoming a nominee` |
| 26478-26480 | s 386AL(5) | fork (F-AL2) | `s 386AL(5) the last day by which the director must have informed the foreign company` |
| 26481-26485 | s 386AL(5), s 386AL(5)(a) | fork (F-AL2) | `s 386AL(5) the last day by which the director must have informed the foreign company`; `s 386AL(5)(a) a director of a foreign company registered before the appointed day who is a nominee on the appointed day must inform the foreign company within 60 days after that day` |
| 26486-26493 | s 386AL(5), s 386AL(5)(b) | fork (F-AL2) | `s 386AL(5) the last day by which the director must have informed the foreign company`; `s 386AL(5)(b) a director of a foreign company registered before the appointed day who becomes a nominee after the appointed day must inform the foreign company within 30 days after becoming a nominee` |
| 26494-26496 | s 386AL(5A) | fork (F-AL2) | `s 386AL(5A) the last day by which the director must have informed the foreign company` |
| 26497-26499 | s 386AL(5A), s 386AL(5A)(a) | fork (F-AL2) | `s 386AL(5A) the last day by which the director must have informed the foreign company`; `s 386AL(5A)(a) a director of a foreign company mentioned in subsection (4) or (5) must inform the foreign company within 30 days after ceasing to be a nominee` |
| 26500-26505 | s 386AL(5A), s 386AL(5A)(b) | fork (F-AL2) | `s 386AL(5A) the last day by which the director must have informed the foreign company`; `s 386AL(5A)(b) a director of a foreign company mentioned in subsection (4) or (5) must inform the foreign company of a change to the particulars within 30 days after the change` |
| 26506-26511 | s 386AL(6) | fork (F-AF6) | `s 386AL(6) the director is guilty of the offence`; `s 386AL(6) the most the director may be sentenced to on conviction` |
| 26512 | the text shows `(7) [Deleted by Act 2 of 2022 wef 30/05/2022]` | repealed or blank in this text | none |
| 26514-26526 | s 386AL(8) | fork (F-AL3) | `s 386AL(8) the director is a nominee` |
| 26527-26532 | s 386AL(9) | fork (F-AL1) | `s 386AL(9) "appointed day" the appointed day` |
| 26533 | heading: Register of nominee shareholders | inert (reason 1: heading or Part title, no rule) | none |
| 26535-26539 | s 386ALA(1) | fork (F-AF2) | `s 386ALA(1) the company or foreign company has kept the register of nominee shareholders as required`; `s 386ALA(1) a company or foreign company must keep a register of nominee shareholders` |
| 26540-26547 | s 386ALA(2) | encoded | `s 386ALA(2) the company or foreign company has entered the fact and the particulars in time`; `s 386ALA(2) a company or foreign company must enter the fact and the particulars in its register of nominee shareholders within 7 days after it is informed` |
| 26548-26557 | s 386ALA(3) | encoded | `s 386ALA(3) the company or foreign company has entered the cessation in time`; `s 386ALA(3) a company or foreign company must enter the cessation of a shareholder as a nominee within 7 days after it is informed` |
| 26558-26570 | s 386ALA(4) | encoded | `s 386ALA(4) the company or foreign company has entered the change in time`; `s 386ALA(4) a company or foreign company must enter the new particulars within 7 days after it is informed of a change` |
| 26571-26575 | s 386ALA(5) | fork (F-AF3) | `s 386ALA(5) the company or foreign company is barred from disclosing the register of nominee shareholders to the person`; `s 386ALA(5) a company or foreign company must not disclose the register of nominee shareholders to a member of the public` |
| 26576-26585 | s 386ALA(6) | fork (F-AF6) | `s 386ALA(6) the company or foreign company is guilty of the offence`; `s 386ALA(6) the officer of the company or foreign company is guilty of the offence`; `s 386ALA(6) the most the company or foreign company or an officer in default may be sentenced to on conviction` |
| 26586 | heading: Nominee shareholders | inert (reason 1: heading or Part title, no rule) | none |
| 26588-26590 | s 386ALB(1) | fork (F-AL2) | `s 386ALB(1) the last day by which the shareholder must have informed the company` |
| 26591-26596 | s 386ALB(1), s 386ALB(1)(a) | fork (F-AL2) | `s 386ALB(1) the last day by which the shareholder must have informed the company`; `s 386ALB(1)(a) a shareholder of a company incorporated on or after 4 October 2022 but before the appointed day who is a nominee on the date of incorporation must inform the company within 30 days after the date of incorporation` |
| 26597-26604 | s 386ALB(1), s 386ALB(1)(b) | fork (F-AL2) | `s 386ALB(1) the last day by which the shareholder must have informed the company`; `s 386ALB(1)(b) a shareholder of a company incorporated on or after 4 October 2022 but before the appointed day who becomes a nominee after the date of incorporation must inform the company within 30 days after becoming a nominee` |
| 26605-26607 | s 386ALB(1A) | fork (F-AL2) | `s 386ALB(1A) the last day by which the shareholder must have informed the company` |
| 26608-26612 | s 386ALB(1A), s 386ALB(1A)(a) | fork (F-AL2) | `s 386ALB(1A) the last day by which the shareholder must have informed the company`; `s 386ALB(1A)(a) a shareholder of a company incorporated on or after the appointed day who is a nominee on the date of incorporation must inform the company on that date` |
| 26613-26624 | s 386ALB(1A), s 386ALB(1A)(b) | fork (F-AL2) | `s 386ALB(1A) the last day by which the shareholder must have informed the company`; `s 386ALB(1A)(b) a shareholder of a company incorporated on or after the appointed day who becomes a nominee after the date of incorporation must inform the company within 30 days after becoming a nominee` |
| 26625-26627 | s 386ALB(2) | fork (F-AL2) | `s 386ALB(2) the last day by which the shareholder must have informed the company` |
| 26628 | the text shows `(a) [Deleted by Act 23 of 2024 wef 16/06/2025]` (in the span of s 386ALB(2)) | repealed or blank in this text | none |
| 26629 | s 386ALB(2) | fork (F-AL2) | `s 386ALB(2) the last day by which the shareholder must have informed the company` |
| 26630-26637 | s 386ALB(2), s 386ALB(2)(b) | fork (F-AL2) | `s 386ALB(2) the last day by which the shareholder must have informed the company`; `s 386ALB(2)(b) a shareholder of a company incorporated before 4 October 2022 who becomes a nominee after 4 October 2022 must inform the company within 30 days after becoming a nominee` |
| 26638-26640 | s 386ALB(3) | fork (F-AL2) | `s 386ALB(3) the last day by which the shareholder must have informed the foreign company` |
| 26641-26646 | s 386ALB(3), s 386ALB(3)(a) | fork (F-AL2) | `s 386ALB(3) the last day by which the shareholder must have informed the foreign company`; `s 386ALB(3)(a) a shareholder of a foreign company registered on or after 4 October 2022 but before the appointed day who is a nominee on the date of registration must inform the foreign company within 30 days after the date of registration` |
| 26647-26654 | s 386ALB(3), s 386ALB(3)(b) | fork (F-AL2) | `s 386ALB(3) the last day by which the shareholder must have informed the foreign company`; `s 386ALB(3)(b) a shareholder of a foreign company registered on or after 4 October 2022 but before the appointed day who becomes a nominee after the date of registration must inform the foreign company within 30 days after becoming a nominee` |
| 26655-26657 | s 386ALB(3A) | fork (F-AL2) | `s 386ALB(3A) the last day by which the shareholder must have informed the foreign company` |
| 26658-26662 | s 386ALB(3A), s 386ALB(3A)(a) | fork (F-AL2) | `s 386ALB(3A) the last day by which the shareholder must have informed the foreign company`; `s 386ALB(3A)(a) a shareholder of a foreign company registered on or after the appointed day who is a nominee on the date of registration must inform the foreign company on that date` |
| 26663-26674 | s 386ALB(3A), s 386ALB(3A)(b) | fork (F-AL2) | `s 386ALB(3A) the last day by which the shareholder must have informed the foreign company`; `s 386ALB(3A)(b) a shareholder of a foreign company registered on or after the appointed day who becomes a nominee after the date of registration must inform the foreign company within 30 days after becoming a nominee` |
| 26675-26677 | s 386ALB(4) | fork (F-AL2) | `s 386ALB(4) the last day by which the shareholder must have informed the foreign company` |
| 26678 | the text shows `(a) [Deleted by Act 23 of 2024 wef 16/06/2025]` (in the span of s 386ALB(4)) | repealed or blank in this text | none |
| 26679 | s 386ALB(4) | fork (F-AL2) | `s 386ALB(4) the last day by which the shareholder must have informed the foreign company` |
| 26680-26687 | s 386ALB(4), s 386ALB(4)(b) | fork (F-AL2) | `s 386ALB(4) the last day by which the shareholder must have informed the foreign company`; `s 386ALB(4)(b) a shareholder of a foreign company registered before 4 October 2022 who becomes a nominee after 4 October 2022 must inform the foreign company within 30 days after becoming a nominee` |
| 26688-26691 | s 386ALB(5) | fork (F-AL2) | `s 386ALB(5) the last day by which the shareholder must have informed the company or foreign company` |
| 26692-26695 | s 386ALB(5), s 386ALB(5)(a) | fork (F-AL2) | `s 386ALB(5) the last day by which the shareholder must have informed the company or foreign company`; `s 386ALB(5)(a) a shareholder must inform the company or foreign company within 30 days after ceasing to be a nominee` |
| 26696-26702 | s 386ALB(5), s 386ALB(5)(b) | fork (F-AL2) | `s 386ALB(5) the last day by which the shareholder must have informed the company or foreign company`; `s 386ALB(5)(b) a shareholder must inform the company or foreign company of a change to the particulars within 30 days after the change` |
| 26703-26709 | s 386ALB(6) | fork (F-AF6) | `s 386ALB(6) the shareholder is guilty of the offence`; `s 386ALB(6) the most the shareholder may be sentenced to on conviction` |
| 26710-26728 | s 386ALB(7) | fork (F-AL3) | `s 386ALB(7) the shareholder is a nominee` |
| 26729-26743 | s 386ALB(7A) | fork (F-AL3) | `s 386ALB(7A) the day on which the shareholder is treated as becoming a nominee` |
| 26744-26751 | s 386ALB(8) | fork (F-AL1) | `s 386ALB(8) "appointed day" the appointed day` |
| 26752-26756 | s 386ALB(8) | fork (F-AL1) | `s 386ALB(8) "company" and "foreign company" the body is one within this section and section 386ALA` |
| 26757-26763 | s 386ALB(8) | fork (F-AL1) | `s 386ALB(8) "shareholder" the person is a shareholder` |
| 26764 | heading: Power to enforce | inert (reason 1: heading or Part title, no rule) | none |
| 26766-26787 | s 386AM(1) | fork (F-GR1) | `s 386AM(1) the Registrar or an officer of the Authority may exercise the power` |
| 26788-26809 | s 386AM(2) | fork (F-AM1) | `s 386AM(2) the power of the Registrar or an officer of the Authority extends to the requirement` |
| 26810-26816 | s 386AM(3) | fork (F-GR2) | `s 386AM(3) the public agency may exercise the powers conferred by subsections (1) and (2)` |
| 26817-26827 | s 386AM(4) | fork (F-AF6) | `s 386AM(4) the person is guilty of the offence`; `s 386AM(4) the most the person may be sentenced to on conviction` |
| 26828-26836 | s 386AM(4A) | fork (F-AF6) | `s 386AM(4A) the person is guilty of the offence`; `s 386AM(4A) the most the person may be sentenced to on conviction` |
| 26837-26844 | s 386AM(4B) | fork (F-AM2) | `s 386AM(4B) this section gives a defence on these facts` |
| 26845-26849 | s 386AM(5) | encoded | `s 386AM(5) this section applies in addition to any right of inspection conferred by section 396A` |
| 26850-26856 | s 386AM(6) | encoded | `s 386AM(6) "public agency" the person is a public agency` |
| 26857 | heading: Central register of controllers | inert (reason 1: heading or Part title, no rule) | none |
| 26859-26864 | s 386AN(1) | fork (F-AN1) | `s 386AN(1) this section applies` |
| 26865-26868 | s 386AN(2) | fork (F-AN1) | `s 386AN(2) the duties of paragraphs (a) and (b) apply to the Registrar` |
| 26869-26873 | s 386AN(2), s 386AN(2)(a) | fork (F-AN1) | `s 386AN(2) the duties of paragraphs (a) and (b) apply to the Registrar`; `s 386AN(2)(a) the Registrar must keep a central register of controllers` |
| 26874-26893 | s 386AN(2)(b) | fork (F-AN1) | `s 386AN(2)(b) the Registrar must require each company or foreign company to lodge the particulars and updates` |
| 26894-26901 | s 386AN(3) | fork (F-AF5) | `s 386AN(3) the company or foreign company has lodged what the Registrar required in time and in the prescribed form and manner`; `s 386AN(3) a company or foreign company must lodge the particulars, matters and updates within the prescribed time after the Registrar requires it` |
| 26902-26913 | s 386AN(4) | fork (F-AF6) | `s 386AN(4) the company or foreign company is guilty of the offence`; `s 386AN(4) the officer of the company or foreign company is guilty of the offence`; `s 386AN(4) the most the company or foreign company or an officer in default may be sentenced to on conviction` |
| 26914-26920 | s 386AN(5) | fork (F-AF3) | `s 386AN(5) the Registrar is barred from disclosing the central register to the person`; `s 386AN(5) the Registrar must not disclose the central register of controllers to a member of the public` |
| 26921-26926 | s 386AN(6) | fork (F-GR3) | `s 386AN(6) the Registrar may disclose the information to the person` |
| 26927-26935 | s 386AN(7) | encoded | `s 386AN(7) different information and persons may be prescribed for the different circumstances` |
| 26936-26937 | heading: Central registers of nominee directors and nominee shareholders | inert (reason 1: heading or Part title, no rule) | none |
| 26939-26943 | s 386ANA(1) | fork (F-AN1) | `s 386ANA(1) the Registrar must keep a central register of nominee directors and a central register of nominee shareholders` |
| 26944-26960 | s 386ANA(2) | fork (F-AN1) | `s 386ANA(2) the company or foreign company has lodged what the subsection requires` |
| 26961-26964 | s 386ANA(3) | fork (F-ANA1, F-AF5) | `s 386ANA(3) the company or foreign company has lodged in time and in the prescribed form and manner`; `s 386ANA(3) a company or foreign company must lodge the particulars, matters and updates within the prescribed time` |
| 26965-26970 | s 386ANA(4) | fork (F-AF6) | `s 386ANA(4) the company or foreign company is guilty of the offence`; `s 386ANA(4) the officer of the company or foreign company is guilty of the offence`; `s 386ANA(4) the most the company or foreign company or an officer in default may be sentenced to on conviction` |
| 26971-26975 | s 386ANA(5) | fork (F-AF3) | `s 386ANA(5) the Registrar is barred from disclosing the central registers of nominee directors and nominee shareholders to the person`; `s 386ANA(5) the Registrar must not disclose the central registers of nominee directors and nominee shareholders to a member of the public` |
| 26976-26982 | s 386ANA(6) | fork (F-GR4) | `s 386ANA(6) the Registrar may disclose the information to the person` |
| 26983-26988 | s 386ANA(7) | encoded | `s 386ANA(7) different information and persons may be prescribed for the different circumstances` |
| 26989 | heading: Codes of practice, etc. | inert (reason 1: heading or Part title, no rule) | none |
| 26991-27002 | s 386AO(1) | fork (F-GR5) | `s 386AO(1) the Registrar may issue the instrument for the purpose` |
| 27003-27008 | s 386AO(2) | fork (F-GR6) | `s 386AO(2) the Registrar may publish the instrument in such manner as the Registrar thinks fit` |
| 27009-27015 | s 386AO(3) | fork (F-GR7) | `s 386AO(3) the Registrar may revoke, vary, revise or amend the instrument` |
| 27016-27034 | s 386AO(4) | fork (F-AO1) | `s 386AO(4)(b) a reference to the instrument is a reference to the instrument as amended` |
| 27035-27044 | s 386AO(5) | fork (F-AO1, F-GR8) | `s 386AO(5) the failure of itself renders the person liable to criminal proceedings`; `s 386AO(5) a party to proceedings may rely on the failure as tending to establish or to negate a liability in question` |
| 27045-27055 | s 386AO(6) | fork (F-AO1) | `s 386AO(6) the instrument is of a kind that the subsection allows` |
| 27056-27061 | s 386AO(7) | fork (F-AO1) | `s 386AO(7) the instrument must be published in the Gazette` |
| 27062 | heading: Exemption | inert (reason 1: heading or Part title, no rule) | none |
| 27064-27069 | s 386AP | fork (F-GR9) | `s 386AP the person is exempt from the provision of this Part` |

## Fork register (sgn)

One line per site where the text can be read two ways with different outcomes: the provision, the function, the answer taken, the other reading, and the text that licenses the answer.
Each ID appears in a comment beside the branch it governs in the modules (an ID with no comment in the code is a group of sites the coverage table names).
"Guide line N" is a line of `inputs/ENCODING-GUIDE.md`; the words in quotation marks after it are the Guide's own.
The rulings the answers rest on are quoted in full in "The rulings this encoding relies on, word for word" below.
A fork line marked (i) or (ii) is a split site: see "Split sites (sgn)".

| ID | provision and function | answer taken | other reading | licensing text |
| --- | --- | --- | --- | --- |
| F-AA1 | s 386AA(1)(a), (1)(b), (1): `this Part applies to the company`, `... to the foreign company`, `... to the company or foreign company` | JUST TRUE for a company not in the Fourteenth Schedule or a foreign company registered under Division 2 of Part 11 not in the Fifteenth; JUST FALSE for one that is in its Schedule ("other than"); NOTHING for a body that is neither (for paragraph (a) a foreign company, and the reverse) | JUST FALSE ("this Part does not apply") for a body that is neither | Guide line 87: "Everywhere else it answers `NOTHING`: where the text lists without closing the list"; the subsection lists two kinds of body and does not say "only" |
| F-AB1 | s 386AB (lead-in): `the definitions of this Part apply here` | the input `the context otherwise requires` decides: JUST FALSE when it does, JUST TRUE when it does not | NOTHING when the context is not stated | Guide line 86: "a condition the text introduces with ... 'unless'"; whether the context requires otherwise is a judgment the text leaves open, so it is a plain input |
| F-AB2 | s 386AB "legal entity", s 386AE(2) "lawyer", s 386AE(2) "legal counsel" | JUST FALSE for what the "means" definition leaves out; the "includes" in each widens the definition by one named kind of person and does not open it | NOTHING for what is left out, because each definition also says "includes" | Guide line 86: "a "means" definition"; against Guide line 87: "says "includes""; the word "means" governs the whole definition and "includes" adds to it |
| F-AB3 | s 386AB "member of the public": `the person is a member of the public` | JUST TRUE for the two listed kinds, NOTHING for anyone else | JUST FALSE for anyone not listed | Guide line 87: "says "includes"" (the definition is "includes (a) ...; and (b) ..."), a list not closed |
| F-AD1 | s 386AD(1), (2): `the evidence is evidence that the corporation had that state of mind`, `... the unincorporated association or partnership had ...` | JUST FALSE when the proceeding is not one where it is necessary to prove a state of mind (a failed "Where") | NOTHING (neither function is named for a grant, so the grant ruling does not move it) | Guide line 93 (periods ruling, item (b)): "a "where ..." condition: when it fails the answer is `JUST FALSE`" |
| F-AD2 | s 386AD(1), (2), the same functions | NOTHING for evidence that is not within the paragraphs; the subsection says what is evidence, not that other evidence is none; for (2), an officer who is neither employee nor agent is outside it | JUST FALSE for other evidence | Guide line 87: "or limits a grant or prohibition in its own wording and the case falls outside the limit" (the provision is a rule of proof that names what counts) and "is silent" |
| F-AE1 | s 386AE(1): `the information or document is subject to legal privilege` | JUST FALSE when none of paragraphs (a) to (e) holds, clause by clause (the subsection says "is subject to legal privilege if"); the five kinds are a list of one choice type; the second printed "(c)" (line 25598) is the closing words of paragraph (c) (finding 5) | NOTHING ("if A then B" does not itself say "if not A then not B") | Guide line 86: "a condition the text introduces with "if", "only if", "as long as" or "unless""; marginal reading (a) |
| F-AF1 | s 386AF(1), (1A), (2), (3) and (4), (4A), (5), (6): the date functions, and `s 386AF(1), (1A), (2) and (3) the company has kept its register in time` (and the foreign-company twin) | the date of incorporation (or registration) picks the subsection; where the company is one "that is not a company to which this Part applies" and "subsequently becomes" one, subsection (3) governs; a date none of them fits is NOTHING, and a function asked about a company outside its subsection is NOTHING | JUST FALSE ("no duty on these dates"); or (1) or (2) and (3) apply together and the earlier last day governs | Guide line 93 (periods ruling, item (c)): "a scope limit with no "only" ... outside the scope the answer is `NOTHING`" |
| F-AF2 | s 386AF(7): `the register is as the subsection requires`; s 386AKA(1) and s 386ALA(1): `the company or foreign company has kept the register ... as required` | JUST FALSE where the register is not as the subsection requires (a duty not met is the provision's own question); the four limbs of (7) and the two register-keeping duties have no time of their own, so a register not kept on the date asked is the failure | NOTHING (the duty has no time, so "not yet" is not "not done") | Guide line 98: "keep `JUST FALSE` ... for a bar, a duty or the provision's own question" |
| F-AF3 | s 386AF(11), s 386AKA(2), s 386ALA(5), s 386AN(5), s 386ANA(5): `... is barred from disclosing ... to the person` | read as a bar: JUST TRUE where the person is a member of the public; JUST FALSE where a requirement under s 386AM (or, for the Registrar, a disclosure under subsection (6)) lifts it ("Subject to ..."); NOTHING where the person is not a member of the public | JUST FALSE for a person who is not a member of the public ("no bar") | Guide line 87: a prohibition "limited ... in its own wording" (the limit is "to any member of the public") "and the case falls outside the limit"; Guide line 92 (N2): "flat negatives count as a no"; marginal reading (b) |
| F-AF4 | every "prescribed" thing: s 386AF(7), (8), (10), s 386AFA(4), (5), s 386AG(2), (3), s 386AIA, s 386AJ, s 386AK, s 386AN(3), s 386ANA(3) | the particulars, form, place, manner, period, time and frequency the regulations prescribe are inputs named for the fact; a prescribed period is a number of DAYS; tests use 14 and 90 days, an assumed value and not the text | a period in weeks, months or working days (the text says only "prescribed") | the brief: "Amounts, rates and thresholds the text leaves to regulations, orders or a Minister are INPUTS"; the regulations are not a source |
| F-AF5 | s 386AF(8) `timing: the act was done in time`, called by every time limit of the Part | the last day is the day the time began plus the number of days, and the day counts ("not later than 30 days after"); an act on any earlier day is in time too; not done and the last day has passed is JUST FALSE; not done and the last day has not passed is NOTHING | the Nth day is out of time ("after N days"); or "not yet" is JUST FALSE | Guide line 93 (periods ruling, item (a)): "a period the text fixes in its own words ... outside the period the answer is `JUST FALSE`"; the helper is `period: the date is not later than the end of a period after` of `sg-periods` |
| F-AF6 | the 21 offence subsections (see "Split sites (sgn)"): `... is guilty of the offence` (32 functions, one for each party named) | JUST TRUE when the failure is made out (and, for an officer, when the person is an officer "who is in default" as s 408(3) gives that meaning); JUST FALSE when it is not (type (i)); the penalty function answers a fine of $25,000 and no imprisonment, else NOTHING | NOTHING for an unmet element | Guide line 98: "keep `JUST FALSE` ... for a bar, a duty or the provision's own question"; Guide line 86: a condition introduced with "if" ("If a company fails to comply with ..."); for the seven sites worded "who fails to comply" with no "if" (listed under "Split sites (sgn)"), line 98 only |
| F-AFA1 | s 386AFA(1), (2), (3): `this section applies to the company or foreign company`, `the person is taken to be a registrable controller ...`, `the company ... has entered in its register what the subsection requires` | JUST FALSE where the section does not apply (a failed "where") | NOTHING | Guide line 93 (periods ruling, item (b)): "a "where ..." condition: when it fails the answer is `JUST FALSE`"; Guide line 94, item (c): ""when", "upon" and "whenever" count as "where"" |
| F-AFA2 | s 386AFA(6): `the company or foreign company has entered the note at the same time` | NOTHING where the company has not entered the particulars of a registrable controller under s 386AF(9) (an "if" on a duty that is unmet) | JUST FALSE, as for s 386AH(1) and s 386AI(1) (F-AH1) | Guide line 95: "a duty whose "if" or "where" is unmet" is decided case by case; here the duty has nothing to attach to, so the text does not speak |
| F-AG1 | s 386AG(1): `the company or foreign company has complied with the duty to take reasonable steps` | NOTHING while the steps are not taken: "reasonable" is not defined and the subsection fixes no time | JUST FALSE (steps not taken is a failure) | Guide line 87: "leaves a term undefined"; Guide line 95: "a bare "must" not done" is decided case by case |
| F-AG2 | s 386AG(2), (4), s 386AH(4), s 386AI(4), s 386AJ(3), s 386AK(3): the exemptions | JUST FALSE where the exemption is met (the text says "does not require" or "need not comply"); NOTHING in any other case (the subsection says only when the duty does not arise) | JUST TRUE (the duty applies unless excused) for the other case | Guide line 86: "a flat negative ("does not", "shall not", "may not")"; Guide line 92 (N2); the other case: Guide line 87, "is silent" |
| F-AG3 | s 386AG(6), s 386AH(6), s 386AI(6), s 386AIA(3): `the addressee has complied with the notice within the time specified` | the time is the number of days the notice itself specifies for compliance (an input), counted by the timing helper; a notice that specifies a date is the helper called with 0 days after that date | none read | the text: "within the time specified in the notice for compliance" (lines 26036, 26111, 26180) and "not later than the time specified for compliance (which must be the prescribed time)" (26214) |
| F-AH1 | s 386AH(1), s 386AI(1): `the company or foreign company must give notice to the registrable controller`; contrast s 386AG(2) (a scope limit, NOTHING) | JUST FALSE where the condition ("If a company or foreign company knows or has reasonable grounds to believe that a relevant change has occurred") is not met | NOTHING (as s 386AFA(6), F-AFA2) | Guide line 86: "a condition the text introduces with "if""; marginal reading (a); Guide line 98 keeps `JUST FALSE` "for ... a duty" |
| F-AH2 | s 386AH(7), s 386AIA(6), s 386AK(5): `a relevant change occurs` | JUST FALSE where none of the listed events holds (the definitions say "occurs if") | NOTHING (an "if" definition does not say "only if") | Guide line 86: "a condition the text introduces with "if""; marginal reading (a) |
| F-AIA1 | s 386AIA(1): `the notice serves the purposes the subsection lists` | both purposes, (a) and (b), are read as required; JUST FALSE if either is missing | either purpose alone is enough | the text: "give a notice ... for the following purposes: (a) ...; (b) ..."; the provision's own question (Guide line 98) |
| F-AIA2 | s 386AIA(1): `the company or foreign company has given the next notice at the prescribed frequency` | the frequency is the most days that may pass between one notice and the next; the first notice has no time stated | a fixed calendar schedule from a base date | the text: "at such frequency as may be prescribed" (a prescribed thing: F-AF4) |
| F-AJ1 | s 386AJ(1), s 386AK(1): `the person must notify ...` | NOTHING for a person who is not within the class ("A person who knows or ought reasonably to know that the person is a registrable controller"); the exemption in subsection (3) is JUST FALSE (F-AG2) | JUST FALSE for the person outside the class | Guide line 93 (periods ruling, item (c)); Guide line 87 |
| F-AKA1 | s 386AKA(1): `... has kept the register of nominee directors as required` | the words "registered under Division 2 of Part 11" qualify "foreign company" only, so a domestic company is within it; contrast s 386ALA(1), which has no such words | the words qualify both, so no domestic company keeps the register | s 386AA(1)(b) uses the phrase for foreign companies only; Guide line 87, "limits a grant or prohibition in its own wording" |
| F-AL1 | s 386AF(14), s 386AL(9), s 386ALB(8): "appointed day" | three different commencement dates (finding 1), each an input date; the tests give each the same assumed date, 16 June 2025 (finding 4) | none | the text: sections 4, 8 and 10 of the 2024 Act; the Act is not a source |
| F-AL2 | s 386AL(1), (1A), (2), (3), (4), (5), (5A) and s 386ALB(1), (1A), (2), (3), (3A), (4), (5): the date functions, with the combined functions `s 386AL(1), (1A), (2), (4) and (5) the last day ...` and `s 386ALB(1), (1A), (2), (3), (3A) and (4) the last day ...` | the date and the kind of body pick the subsection; "on that date" is 0 days; a director or shareholder outside the subsection is NOTHING; for s 386AL(2), s 386ALB(2) and s 386ALB(4) paragraph (a) is deleted, so the duty for a person who already was a nominee is not in the text | JUST FALSE for a person outside the subsection | Guide line 93 (periods ruling, item (c)); the deleted paragraphs are shown as such in the text (finding 6) |
| F-AL3 | s 386AL(8), s 386ALB(7), s 386ALB(7A): `the director is a nominee`, `the shareholder is a nominee`, `the day on which the shareholder is treated as becoming a nominee` | JUST FALSE where no limb of the "is a nominee if" definition holds; s 386ALB(7A) is NOTHING outside its wording | NOTHING (an "if" definition does not say "only if") | Guide line 86; marginal reading (a) |
| F-AM1 (ii) | s 386AM(2): `the power of the Registrar or an officer of the Authority extends to the requirement` | JUST FALSE where the register or documents are not kept in electronic form (a failed "Where") | NOTHING (the function is named for a power) | Guide line 93 (periods ruling, item (b)): "a "where ..." condition: when it fails the answer is `JUST FALSE`"; Guide line 99, limit 3: a "may" function whose gate is "where" is not changed, but listed here |
| F-AM2 | s 386AM(4B): `this section gives a defence on these facts` | JUST FALSE, worded "this section gives no defence on these facts", where the accused has not proved the steps and diligence; NOTHING where the proceedings are not for an offence under (4A) | NOTHING where not proved | Guide line 94, item (b): "when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"" |
| F-AN1 | s 386AN(1), (2), (2)(a), (2)(b): `this section applies`, `the duties ... apply to the Registrar` | JUST FALSE where the Minister has not directed the Registrar by notification in the Gazette (a failed "where"); s 386ANA(1), (2) has no such condition | NOTHING | Guide line 93 (periods ruling, item (b)) |
| F-ANA1 | s 386ANA(3): `the company or foreign company has lodged in time and in the prescribed form and manner` | the day the prescribed time begins to run is an input, because the subsection names none (s 386AN(3) is triggered by "Where the Registrar requires", and I read its time as running from that requirement; s 386ANA(3) has no trigger at all) | none read | the text: "within the prescribed time" (line 26963) |
| F-AO1 | s 386AO(4)(b), (6), (7): `a reference to the instrument is a reference to the instrument as amended`, `the instrument is of a kind that the subsection allows`, `the instrument must be published in the Gazette` | (4)(b) JUST FALSE where "the context otherwise requires"; (6) NOTHING for a kind outside the permissions; (7) JUST FALSE for an instrument issued under the section ("It is not necessary to publish ... in the Gazette") | (7): NOTHING | Guide line 86: "a flat negative"; Guide line 87: "lists without closing the list" |
| F-GR1 | s 386AM(1): `the Registrar or an officer of the Authority may exercise the power` | NOTHING where the person is not the Registrar or an officer, the body is not one the Part applies to, or the inquiry is not necessary (grant function, gate failed) | JUST FALSE ("may not") | Guide line 97 (limit 1): "answer `NOTHING`, with one fork line each, only for a function named for a grant or a power ("may", "is permitted to", "has power to") whose `if` gate failed" |
| F-GR2 | s 386AM(3): `the public agency may exercise the powers conferred by subsections (1) and (2)` | NOTHING unless the person is a public agency and the exercise is to administer or enforce a written law | JUST FALSE | Guide line 97 (limit 1) |
| F-GR3 | s 386AN(6): `the Registrar may disclose the information to the person` | NOTHING: the information, persons and circumstances are prescribed (the regulations are not a source), and the gate fails otherwise | JUST FALSE | Guide line 97 (limit 1); Guide line 87: "points outside the sources" |
| F-GR4 | s 386ANA(6): `the Registrar may disclose the information to the person` | NOTHING, for the same reasons as F-GR3 | JUST FALSE | Guide line 97 (limit 1); Guide line 87 |
| F-GR5 | s 386AO(1): `the Registrar may issue the instrument for the purpose` | NOTHING for another kind of instrument or purpose than the subsection lists | JUST FALSE | Guide line 97 (limit 1) |
| F-GR6 | s 386AO(2): `the Registrar may publish the instrument in such manner as the Registrar thinks fit` | NOTHING unless the instrument was issued under the section | JUST FALSE | Guide line 97 (limit 1) |
| F-GR7 | s 386AO(3): `the Registrar may revoke, vary, revise or amend the instrument` | NOTHING unless the instrument was issued under the section | JUST FALSE | Guide line 97 (limit 1) |
| F-GR8 | s 386AO(5): `a party to proceedings may rely on the failure as tending to establish or to negate a liability in question`; the companion `the failure of itself renders the person liable to criminal proceedings` is a flat negative (JUST FALSE, F-AO1 and N2) | NOTHING where there is no such failure | JUST FALSE | Guide line 97 (limit 1) |
| F-GR9 | s 386AP: `the person is exempt from the provision of this Part` | NOTHING where the Minister has made no order (the section is a grant, "The Minister may, by order in the Gazette, exempt") | JUST FALSE | Guide line 97 (limit 1); the function is named "is exempt" and not "may", so it is also listed under limit 3 |

### The grant ruling's three limits, applied

1. Limit 1 (one fork line each, NOTHING): F-GR1 to F-GR9, nine functions.
2. Limit 2 (keep JUST FALSE where the text closes the gate itself, and for a bar, a duty or the provision's own question): the bars of F-AF3 (JUST FALSE where a requirement under s 386AM lifts the bar), the duties of F-AF2, F-AH1, the offences of F-AF6.
3. Limit 3 (listed, not changed): one "may" function whose gate is "where": F-AM1 (s 386AM(2)); no "when" or "upon" gate on a "may" function; no "entitled"-named function (0).

### The rulings this encoding relies on, word for word

The brief says each ruling is recorded again, word for word, in the NOTES of each row that carries its `NOTHING-kind` tags.
This row carries the tags "list not closed", "includes", "limited by its own wording", "silent" and "points outside the text", so these are the Guide's lines, copied by script from `inputs/ENCODING-GUIDE.md`; the label above each block gives its line numbers.

Lines 86 and 87 (the rule of 2026-10-29, "In short"):

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").
> Everywhere else it answers `NOTHING`: where the text lists without closing the list, says "includes", leaves a term undefined, is silent, points outside the sources, or limits a grant or prohibition in its own wording and the case falls outside the limit.

Line 92 (N2, ruled 2026-11-04):

> - **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. The maintainer's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." the maintainer's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23

Line 93 (the periods ruling, ruled 2026-11-05):

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. The maintainer's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

Line 94 (delegated definitions, defences and "until" bars, ruled 2026-11-05):

> - **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. The maintainer approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

Line 95 (case by case, typed 2026-11-05):

> - **Questions with no convention: decide case by case (the maintainer, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. The maintainer's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with the coordinator where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

Lines 96 to 99 (functions named for a grant or a power, 2026-11-12, "not confirmed by the maintainer"):

> - **Functions named for a grant or a power (ruled by the coordinating session of the UK and Canada encodings on 2026-11-12; not confirmed by the maintainer).** A function named for a grant or a power ("the court may ...", "the registrar may ...") that answers `JUST FALSE` because an `if` gate failed reads as "may not": a grant turned into a bar. The ruling sets three limits:
>   1. answer `NOTHING`, with one fork line each, only for a function named for a grant or a power ("may", "is permitted to", "has power to") whose `if` gate failed;
>   2. keep `JUST FALSE` where the text closes the gate itself ("only if", "only where", "may not ... unless", a list closed with "only"), and for a bar, a duty or the provision's own question;
>   3. do not change, but list in the row's fork register for the maintainer or a lawyer, a "may" function whose gate is "where", "when" or "upon" (ruling (b) of the periods ruling above says `JUST FALSE`, and the "In short" line on grants points the other way), and an "entitled"-named function (an entitlement is a claim, not a power, and this guide does not settle it).

## Jural relations (sgn)

Hohfeld's pairs: a claim and a duty; a privilege and a no-right; a power and a liability; an immunity and a disability.
Where the text names nobody who holds the claim against a duty-bearer, the table says "no holder named": it does not supply the State or the Registrar.
Where the correlative of a duty is a person's claim, the table gives the pair once, as one relation, not twice from each side.

| provision | holder (claim, privilege, power, immunity) | bearer (duty, no-right, liability, disability) | relation | L4 rule or function |
| --- | --- | --- | --- | --- |
| s 386AA(1), (1A), (2), (3) | none | none | scope of the Part | none |
| s 386AB | none | none | definitions | none |
| s 386AC | none | none | a counting rule (who is registrable) | none |
| s 386AD(1), (2) | none | none | a rule of proof of state of mind | none |
| s 386AE | none | none | a definition of legal privilege | none |
| s 386AF(1), (1A), (2), (3) | no holder named | the company: duty to keep a register by a date | claim and duty | rules `s 386AF(1)`, `(1A)`, `(2)`, `(3)` |
| s 386AF(4), (4A), (5), (6) | no holder named | the foreign company: the same duty | claim and duty | rules `s 386AF(4)`, `(4A)`, `(5)`, `(6)` |
| s 386AF(7)(a), (aa), (b), (c) | no holder named | the company or foreign company: duty to keep the register complete, current and in form | claim and duty | four rules `s 386AF(7)(a)` ... `(c)` |
| s 386AF(8) | no holder named | the company or foreign company: duty to enter and update within the prescribed time | claim and duty | rule `s 386AF(8)` |
| s 386AF(9)(a), (b) | no holder named | the company or foreign company: duty to enter or update after confirmation, or with a note without it | claim and duty | rules `s 386AF(9)(a)`, `(b)` |
| s 386AF(10) | none | none | what a confirmation is | none |
| s 386AF(11) | no holder named | the company or foreign company: duty not to disclose; a member of the public has no claim to disclosure | duty (SHANT) and no-right | rule `s 386AF(11)` |
| s 386AF(12), (13) | no holder named | the company, the foreign company and the officer in default: liability to conviction and a fine up to $25,000 | liability | offence and penalty functions of `s 386AF(12)`, `(13)` |
| s 386AF(14) | none | none | a definition (appointed day) | none |
| s 386AFA(1), (2) | none | none | application and a deeming rule | none |
| s 386AFA(3), (4), (5), (6) | no holder named | the company or foreign company: duty to enter the note and particulars, within the prescribed period, to update, and to enter the note at the same time | claim and duty | rules `s 386AFA(3)` to `(6)` |
| s 386AFA(7) | no holder named | the company and the officer in default: liability | liability | offence and penalty functions |
| s 386AFA(8), (9) | none | none | definitions | none |
| s 386AG(1) | no holder named | the company or foreign company: duty to take reasonable steps to find its registrable controllers | claim and duty | rule `s 386AG(1)` |
| s 386AG(2), (3) | no holder named | the company or foreign company: duty to give the notice, in the form the subsection requires, within the prescribed period | claim and duty | rule `s 386AG(2) and (3)(c)` |
| s 386AG(4) | the company or foreign company: privilege not to give notice for information already provided | no holder named: no-right | privilege | function `s 386AG(4)` |
| s 386AG(5) | no holder named | the company and the officer in default: liability | liability | offence and penalty functions |
| s 386AG(6) | the company or foreign company: claim to the information | the addressee: duty to comply within the time the notice specifies | claim and duty | rule `s 386AG(6)` |
| s 386AG(7) | no holder named | the addressee: liability | liability | offence and penalty functions |
| s 386AH(1), (2) | no holder named | the company or foreign company: duty to give notice of a change within the prescribed period | claim and duty | rule `s 386AH(1) and (2)` |
| s 386AH(3) | none | none | what the notice must contain | none |
| s 386AH(4) | the company or foreign company: privilege not to give notice for information already provided | no holder named: no-right | privilege | function `s 386AH(4)` |
| s 386AH(5), (6) | no holder named | the company and the officer in default (5), the addressee (6): liability | liability | offence and penalty functions |
| s 386AH(7) | none | none | when a relevant change occurs | none |
| s 386AI(1), (2) | no holder named | the company or foreign company: duty to give notice that information is incorrect | claim and duty | rule `s 386AI(1) and (2)` |
| s 386AI(3), (4), (5), (6) | as s 386AH(3) to (6) | as s 386AH(3) to (6) | as s 386AH(3) to (6) | as s 386AH |
| s 386AIA(1), (2) | no holder named | the company or foreign company: duty to give a notice to each registrable controller at the prescribed frequency | claim and duty | rule `s 386AIA(1)` |
| s 386AIA(3) | the company or foreign company: claim to the response | the addressee: duty to comply no later than the time specified | claim and duty | rule `s 386AIA(3)` |
| s 386AIA(4), (5) | no holder named | the company, the officer and the addressee: liability | liability | offence and penalty functions |
| s 386AIA(6) | none | none | when a relevant change occurs | none |
| s 386AJ(1), (2) | the company or foreign company: claim to be notified | the person who is a registrable controller: duty to notify within the prescribed period | claim and duty | rule `s 386AJ(1) and (2)` |
| s 386AJ(3) | the person: privilege not to comply if the person has already complied with a notice under s 386AG(2) | the company: no-right | privilege | function `s 386AJ(3)` |
| s 386AJ(4) | no holder named | the person: liability | liability | offence and penalty functions |
| s 386AK(1), (2), (3), (4) | as s 386AJ(1) to (4), for a relevant change | as s 386AJ(1) to (4) | as s 386AJ | rule `s 386AK(1) and (2)`; functions |
| s 386AK(5) | none | none | when a relevant change occurs | none |
| s 386AKA(1) | no holder named | the company or foreign company: duty to keep a register of nominee directors | claim and duty | rule `s 386AKA(1)` |
| s 386AKA(2) | no holder named | the company or foreign company: duty not to disclose to a member of the public; the member has no claim | duty (SHANT) and no-right | rule `s 386AKA(2)` |
| s 386AKA(3), (4), (5) | no holder named | the company or foreign company: duty to enter the fact, the cessation, the change within 7 days after it is informed | claim and duty | rules `s 386AKA(3)`, `(4)`, `(5)` |
| s 386AKA(6) | no holder named | the company and the officer in default: liability | liability | offence and penalty functions |
| s 386AL(1), (1A), (2), (3), (4), (5), (5A) | the company or foreign company: claim to be informed | the director: duty to inform it within 30 days (60 for s 386AL(5)(a), or on the date for (1A)(a) and (4)(a)) | claim and duty | the 13 rules `s 386AL(1)(a)` ... `(5A)(b)` |
| s 386AL(6) | no holder named | the director: liability | liability | offence and penalty functions |
| s 386AL(7), (8), (9) | none | none | (7) deleted; (8) a definition; (9) a definition | none |
| s 386ALA(1) to (6) | as s 386AKA(1) to (6), for nominee shareholders | as s 386AKA(1) to (6) | as s 386AKA | rules `s 386ALA(1)` to `(5)`; functions |
| s 386ALB(1) to (5) | the company or foreign company: claim to be informed | the shareholder: duty to inform within 30 days (or on the date, or within 60 days where the subsection says) | claim and duty | the 12 rules `s 386ALB(1)(a)` ... `(5)(b)` |
| s 386ALB(6) | no holder named | the shareholder: liability | liability | offence and penalty functions |
| s 386ALB(7), (7A), (8) | none | none | definitions and a treating rule | none |
| s 386AM(1) | the Registrar or an officer of the Authority: power to require production, to inspect and copy, to inquire | the company or foreign company: liability to those powers | power and liability | function `s 386AM(1)` |
| s 386AM(2) | the same: power to require a legible copy and assistance | the person on the premises: liability | power and liability | function `s 386AM(2)` |
| s 386AM(3) | a public agency: power to exercise the powers of (1) and (2) | the same persons: liability | power and liability | function `s 386AM(3)` |
| s 386AM(4), (4A) | no holder named | the person who fails to comply, or gives false or misleading information: liability to conviction and a fine up to $25,000 | liability | offence and penalty functions |
| s 386AM(4B) | the accused: immunity from conviction under (4A) on proof of all reasonable steps and due diligence | no holder named: disability | immunity | function `s 386AM(4B)` |
| s 386AM(5), (6) | none | none | an addition to s 396A; a definition | none |
| s 386AN(1) | none | none | when the section applies | none |
| s 386AN(2)(a), (b) | no holder named | the Registrar: duty to keep the central register and to require lodgment | claim and duty | rules `s 386AN(2)(a)`, `(b)` |
| s 386AN(3) | the Registrar: claim to the lodgment | the company or foreign company: duty to lodge in the prescribed form and manner within the prescribed time | claim and duty | rule `s 386AN(3)` |
| s 386AN(4) | no holder named | the company and the officer in default: liability | liability | offence and penalty functions |
| s 386AN(5) | no holder named | the Registrar: duty not to disclose to a member of the public; the member has no claim | duty (SHANT) and no-right | rule `s 386AN(5)` |
| s 386AN(6) | the Registrar: power to disclose prescribed information to prescribed persons | those whose information it is: liability | power and liability | function `s 386AN(6)` |
| s 386AN(7) | none | none | to avoid doubt: different information and persons may be prescribed | none |
| s 386ANA(1) to (7) | as s 386AN(2) to (7), for the central registers of nominee directors and nominee shareholders | as s 386AN | as s 386AN | rules `s 386ANA(1)`, `(3)`, `(5)`; functions |
| s 386AO(1), (2), (3) | the Registrar: power to issue, publish, revoke, vary, revise or amend a code | those to whom the code applies: liability | power and liability | functions `s 386AO(1)`, `(2)`, `(3)` |
| s 386AO(4) | none | none | amendments and references | none |
| s 386AO(5) | the person: immunity from criminal liability by the failure alone; any party to proceedings: power to rely on the failure | the prosecution: disability; the other party: liability | immunity and power | functions `s 386AO(5)` (two) |
| s 386AO(6), (7) | the Registrar: privilege of general or specific application, and not to publish in the Gazette | no holder named: no-right | privilege | functions `s 386AO(6)`, `(7)` |
| s 386AP | the Minister: power to exempt; the exempted person: immunity from the provision | the person or class: liability; the enforcers: disability | power and immunity | function `s 386AP` |

## Marginal readings for a lawyer (sgn)

The brief marks two readings as "for a lawyer, not for you to decide".
Both are taken as the status quo, and every branch that rests on one is listed here with the other reading.

**(a) A failed "if" counts as the text's no, clause by clause, and a flat negative counts as the text saying no.**
The other reading is that an "if" states a sufficient condition and says nothing of its failure, so the answer is NOTHING.

| branch | what it answers when the "if" fails | other reading |
| --- | --- | --- |
| s 386AE(1) `the information or document is subject to legal privilege` | JUST FALSE when none of (a) to (e) holds | NOTHING |
| s 386AH(1) and s 386AI(1) `... must give notice to the registrable controller` | JUST FALSE when the company does not know or have reasonable grounds to believe | NOTHING |
| s 386AH(7), s 386AIA(6), s 386AK(5) `a relevant change occurs` | JUST FALSE when no listed event holds | NOTHING |
| s 386AL(8) and s 386ALB(7) `... is a nominee` | JUST FALSE when no limb holds | NOTHING |

The flat negatives taken as a no (the second half of reading (a), and the Guide's N2, line 92): s 386AG(4), s 386AH(4), s 386AI(4) ("does not require"), s 386AJ(3), s 386AK(3) ("need not comply"), s 386AO(5) ("does not of itself render ... liable"), s 386AO(7) ("It is not necessary to publish").
The other reading for each is NOTHING.

**(b) A prohibition or a grant limited by its own wording does not count as the text's no.**
The branches that answer NOTHING because the case falls outside the limit of the wording are:

| branch | the limit in the wording | other reading |
| --- | --- | --- |
| s 386AF(11), s 386AKA(2), s 386ALA(5), s 386AN(5), s 386ANA(5) the bars | "to any member of the public" (F-AF3) | JUST FALSE for a person who is not a member of the public |
| s 386AM(1), s 386AM(3), s 386AN(6), s 386ANA(6), s 386AO(1), (2), (3), (5), s 386AP the grants | the person, the body, the purpose or the order named (F-GR1 to F-GR9) | JUST FALSE |
| s 386AJ(1), s 386AK(1) the duties to notify | "knows or ought reasonably to know" (F-AJ1) | JUST FALSE |
| s 386AD(1), (2) the evidence rules, outside the paragraphs | the paragraphs name what is evidence (F-AD2) | JUST FALSE |

**A site that fits neither reading nor any Guide line.**
None: every site above names a Guide line.
The two sites where two Guide lines point opposite ways are F-AM1 (periods ruling (b) and the grant ruling's limit 3) and F-AFA2 against F-AH1 (line 95, decided by case): both are listed in the fork register and left for a lawyer.

### Reading a result: FALSE and NOTHING (sgn)

A result in this row has three shapes.
`JUST TRUE` is yes: the text says so on these facts.
`JUST FALSE` is the text's no, and it appears only where the text says no in its own words: a "means" definition that leaves the case out (a body that is not a "legal entity"); a condition the text introduces with "if" or "where" that is not met (the Part does not apply to a company that is in the Fourteenth Schedule; the section does not apply because the Minister has not directed the Registrar); a flat negative ("does not require", "need not comply", "does not of itself render ... liable"); a time the text fixes in its own words that has passed ("not later than 30 days after"); an offence whose failure is not made out (the company did not fail to comply, so this subsection makes it guilty of nothing); a defence not proved ("this section gives no defence on these facts", and never "no defence at all").
`NOTHING` is "the text does not answer on these facts", and a caller must never turn it into a no.
In this Part it means: the person or body is outside the limit of the provision's own wording (a person who is not a controller, a foreign company where the paragraph speaks of companies, a person who is not a member of the public); the time has not yet run out; a list that "includes" or is not closed; the matter is left to regulations, an order or a direction that is not in the text (what is prescribed, what the Registrar may disclose, whether the Minister has exempted the person); the text is silent (a penalty for a person the subsection does not make guilty).
The two readings in "Marginal readings for a lawyer (sgn)" mark the places where a lawyer might move a result from one shape to another.

## Seams (sgn)

A part cannot import another part, so a fact that another part's provision settles is an input named for the fact.
PLAN.md section 4 has no seam row that names a provision of this Part, and the `sgn` row of section 6 says "Asks later parts nothing".
The XREFS table shows five citations of this Part from other ranges (the keel, at 1078 and 1079, cites s 386AA; sgg 24542, 24545 and 24548 cite ss 386AF, 386AKA and 386ALA), so the keel and sgg may ask this part for the answer of those sections; this part offers the functions of those sections for that and takes no input from the citing text.
The seams I took, each checked against the text before it was written:

| asking provision | answering provision | input (name and type) | seen |
| --- | --- | --- | --- |
| s 386AFA(8) "chief executive officer" | s 4(1) (keel, `sg-definitions`) | imported: `s 4(1) "chief executive officer" the person is a chief executive officer of the company` | text 25920-25930 |
| s 386AE(2) "employer" (a) | s 6 (the keel, `sg-groups`) | `the corporation is related under section 6 to the corporation that employs the legal counsel` BOOLEAN | text 25637; the keel's one-fact function `s 4(1) "related corporation" ...` (sg-groups.l4) was not called: see "Where this brief and PLAN.md differ" |
| s 386AM(5) | s 396A (another part) | none: the subsection says only that the section applies in addition to the right of inspection; one function with the answer TRUE | text 26846 |
| s 386AA(1)(a), (1)(b), (1A) | the Fourteenth and Fifteenth Schedules (another part) | `the company is set out in the Fourteenth Schedule` BOOLEAN; `the foreign company is set out in the Fifteenth Schedule` BOOLEAN | text 25386, 25390, 25398-25404 |
| s 386AB "significant control", "significant interest", s 386AC | the Sixteenth Schedule (another part) | `the person has significant control over the company or foreign company, as the Sixteenth Schedule gives that meaning` BOOLEAN; `the person has a significant interest in the company or foreign company, as the Sixteenth Schedule gives that meaning` BOOLEAN | text 25483, 25486 |
| s 386AF(14), s 386AL(9), s 386ALB(8) | the Companies and Limited Liability Partnerships (Miscellaneous Amendments) Act 2024, sections 4, 8, 10 | three date inputs (F-AL1) | text 25818, 26527, 26746 |
| every offence provision, for "officer who is in default" | s 408(3) (another part) | `the person is an officer of the company or foreign company who is in default, as section 408(3) gives that meaning` BOOLEAN (and the company and foreign-company forms) | text 28136-28142 (the same file, outside this range) |
| s 386AB "approved exchange", "limited liability partnership"; s 386AE(2) "legal counsel", "employer" (b) | the Securities and Futures Act 2001 s 2(1); the Limited Liability Partnerships Act 2005 s 4(1); the Evidence Act 1893 s 3(7) and s 128A(6) | one BOOLEAN each, named for the fact and the section | text, the same definitions |
| every "prescribed" thing | the regulations (not a source) | inputs (F-AF4) | text |

A seam the plan lacks: s 386AB "legal entity" and s 386AE(2) "lawyer" and "legal counsel" take a plain fact each (the person is a "solicitor or a professional legal adviser" and so on), because who may practise is left to other law.

## Split sites (sgn)

**Type (i): an unmet element of an offence or a contravention.**
Count: 21 sites (provisions), carried by 32 functions (a company function and an officer function for each of eleven of them; one function each for the other ten).
The answer taken at every site is JUST FALSE ("the text does not make the person guilty on these facts"), and the fork line for all of them is F-AF6.
The 21 sites: s 386AF(12), s 386AF(13), s 386AFA(7), s 386AG(5), s 386AG(7), s 386AH(5), s 386AH(6), s 386AI(5), s 386AI(6), s 386AIA(4), s 386AIA(5), s 386AJ(4), s 386AK(4), s 386AKA(6), s 386AL(6), s 386ALA(6), s 386ALB(6), s 386AM(4), s 386AM(4A), s 386AN(4), s 386ANA(4).
The Guide line the answer relies on is line 98 (grant ruling, limit 2): "keep `JUST FALSE` ... for a bar, a duty or the provision's own question".
For the fourteen sites that open "If a ... fails to comply with ..." (s 386AF(12), s 386AF(13), s 386AFA(7), s 386AG(5), s 386AH(5), s 386AI(5), s 386AIA(4), s 386AJ(4), s 386AKA(6), s 386AL(6), s 386ALA(6), s 386ALB(6), s 386AN(4), s 386ANA(4)), line 86 adds: "a condition the text introduces with "if"".
The other seven are worded "who fails to comply" with no "if" (s 386AG(7), s 386AH(6), s 386AI(6), s 386AIA(5), s 386AK(4), s 386AM(4), s 386AM(4A)), so for them line 98 alone is the licence.
The other reading, NOTHING, is the Guide's line 87 ("is silent") if one reads the offence as a separate question from the duty.

**Type (ii): a "may" gated by "where", "when", "upon", "on application", "with the consent of".**
Count: 1 site, s 386AM(2) (F-AM1), answer JUST FALSE (a failed "Where ... kept in electronic form").
The licence is the periods ruling, Guide line 93, item (b): "a "where ..." condition: when it fails the answer is `JUST FALSE`".
The other reading, NOTHING, is the grant ruling (Guide line 97, limit 1: "answer `NOTHING` ... only for a function named for a grant or a power ("may", "is permitted to", "has power to") whose `if` gate failed"), and limit 3 (line 99) says to list it, not change it: it is listed.
No other "may" function in the range has a "where", "when" or "upon" gate; the "may" functions with other gates answer NOTHING (F-GR1 to F-GR9).
"Entitled"-named functions: none.

**Grant-ruling NOTHING functions (limit 1): 9**, one fork line each (F-GR1 to F-GR9).

**The failed "where" sites: 8 in all**, every one JUST FALSE under line 93 item (b): s 386AD(1), s 386AD(2), s 386AFA(1), s 386AFA(2), s 386AFA(3), s 386AN(1), s 386AN(2) (none of these seven is a "may"), and s 386AM(2) (a "may" function, so type (ii) above).

## Rules with no breach path (sgn)

> Added 2026-11-27 (decided by Claude, assumed, not ruled): this section was written before the pass recorded in `lest-without-deadline.md`, and it is no longer true of the rules listed below.
> Each of them now takes an input-length `WITHIN` and can reach `BREACH`, so read "no time limit", "no deadline" and "no breach path" of them as the position before that pass, here and wherever else these notes say so of them:
>
> - `s 386AN(2)(b) the Registrar must require each company or foreign company to lodge the particulars and updates`
>
> The other rules named in this section are unchanged.

Each `MUST` below has no time limit and no consequence the text states beyond the offence in a separate subsection (not a trace of this rule), so a late act cannot show it breached: a trace of it can only be FULFILLED or RESIDUAL.
No deadline or consequence is invented.

| provision | rule |
| --- | --- |
| s 386AF(7)(a) | `s 386AF(7)(a) a company or foreign company must ensure that its register contains the prescribed particulars` |
| s 386AF(7)(aa) | `s 386AF(7)(aa) ... contains the note and particulars required under section 386AFA(3)` |
| s 386AF(7)(b) | `s 386AF(7)(b) ... its register is updated if any change occurs` |
| s 386AF(7)(c) | `s 386AF(7)(c) ... kept in the prescribed form and at the prescribed place` |
| s 386AF(9)(a) | `s 386AF(9)(a) ... must enter or update the particulars of a controller after the controller confirms them` |
| s 386AF(9)(b) | `s 386AF(9)(b) ... that does not receive the confirmation must enter or update the particulars with a note` |
| s 386AFA(3) | `s 386AFA(3) a company or foreign company to which the section applies must enter the note and the prescribed particulars` |
| s 386AG(1) | `s 386AG(1) ... must take reasonable steps to find out and identify its registrable controllers` |
| s 386AKA(1) | `s 386AKA(1) a company or foreign company must keep a register of nominee directors` |
| s 386ALA(1) | `s 386ALA(1) a company or foreign company must keep a register of nominee shareholders` |
| s 386AN(2)(a) | `s 386AN(2)(a) the Registrar must keep a central register of controllers` |
| s 386AN(2)(b) | `s 386AN(2)(b) the Registrar must require each company or foreign company to lodge the particulars and updates` |
| s 386ANA(1) | `s 386ANA(1) the Registrar must keep a central register of nominee directors and a central register of nominee shareholders` |

That is 13 rules.
The `MUST` rules with a time limit (53, counting a limit of 0 days where the text says "on that date") each have a trace that reaches BREACH.
The five `SHANT` rules (s 386AF(11), s 386AKA(2), s 386ALA(5), s 386AN(5), s 386ANA(5)) each have a trace in which the forbidden act occurs and BREACH results.
Over all test files there are 138 traces: 59 are marked `-- EXPECT BREACH`, 66 `FULFILLED`, 13 `RESIDUAL`, and `work/traces.py` found 0 mismatches against the output on either build.

## What the text turns out to say

Numbered findings, each checked against the text of lines 25372-27069 before it was written.

1. **Three different "appointed days".**
   s 386AF(14) means the commencement of section 4 of the Companies and Limited Liability Partnerships (Miscellaneous Amendments) Act 2024 (line 25818); s 386AL(9) means section 8 (26527); s 386ALB(8), which governs "this section and section 386ALA", means section 10 (26746).
   They are three dates, not one, and each is an input.
2. **The Part fixes only three numbers of days.**
   Every period in the range is 7 days, 30 days or 60 days, or is "prescribed", or is "the time specified in the notice for compliance"; no other number of days, weeks, months or years appears in the range.
3. **The obligation to comply extends to all natural persons and all entities.**
   s 386AA(2) says so whether the person is resident in Singapore or not and a citizen or not, and whether the entity is formed, constituted or carrying on business in Singapore or not (25408-25411), so residence, citizenship and place of formation are not inputs of the `s 386AA(2)` function.
4. **The tests use 16 June 2025 for every appointed day, and that date is assumed, not text.**
   It is the "wef" date that the consolidation's amendment marks show for the 2024 Act's amendments; the Act that fixes the appointed days is not a source.
5. **s 386AE(1) has two lines that begin "(c)".**
   The second, at line 25598, is the closing words of paragraph (c) ("in connection with, and for the purposes of, any legal proceedings ..."), not a second paragraph; the subsection's paragraphs are (a), (b), (c), (d) and (e).
6. **Three paragraphs are deleted, and one subsection and one definition as well.**
   Paragraph (a) of s 386AL(2) (26435), paragraph (a) of s 386ALB(2) (26628) and paragraph (a) of s 386ALB(4) (26678) are each shown as "[Deleted by Act 23 of 2024 wef 16/06/2025]", so the duty in each of those subsections is now stated only for a director or shareholder who "becomes a nominee after" the date in (b).
   s 386AL(7) (26512) is "[Deleted by Act 2 of 2022 wef 30/05/2022]", and a definition in s 386AB (25480) is "[Deleted by Act 22 of 2024 wef 09/06/2025]".
7. **Every offence in the range is a fine of $25,000 at most, and none carries imprisonment or a default penalty.**
   There are 21 lines with "$25,000" in the range, one for each of the 21 offence subsections listed under "Split sites (sgn)", and no line in the range contains "imprison" or "default penalty".
   The function that returns the penalty answers a fine of $25,000, no imprisonment, and the flags false.
8. **s 386AM(4B) puts the burden of proof on the accused.**
   "In proceedings for an offence under subsection (4A), it is a defence to the charge for the accused to prove, on a balance of probabilities, that the accused took all reasonable steps and exercised all due diligence to ensure that the information provided was not false or misleading."
   s 386AM(4A), the offence it answers, is the one about false or misleading information; s 386AM(4), the failure to comply with a requirement, has no defence provision of its own in the range.
9. **A failure to comply with a code of practice is not itself a crime, but may be relied on.**
   s 386AO(5): the failure "does not of itself render that person liable to criminal proceedings but any such failure may, in any proceedings whether civil or criminal, be relied upon by any party".
10. **s 386AN applies only where the Minister directs; s 386ANA does not.**
    s 386AN(1) says "This section applies where the Minister, by notification in the Gazette, directs the Registrar to maintain a central register of controllers"; s 386ANA(1) says "The Registrar must keep a central register of nominee directors and a central register of nominee shareholders" with no condition.
11. **The notice sets its own time for a response.**
    The addressee must comply "within the time specified in the notice for compliance" (s 386AG(6), s 386AH(6), s 386AI(6), s 386AIA(3)), and under s 386AIA(2)(a) that time "must be the prescribed time", so the Act itself never fixes the number of days a person has to answer a notice.
12. **The exemptions for information already provided cover only the notice "in respect of" that information.**
    s 386AG(4) says "Subsection (2) does not require a company or foreign company to give notice to any person in respect of any information" that the person, or a registered corporate service provider on the person's behalf, previously provided; s 386AH(4) and s 386AI(4) say the same of subsection (1).
    The text does not excuse the notice itself, only the notice "in respect of" that information.
13. **s 386AKA(1) says "registered under Division 2 of Part 11" and s 386ALA(1) does not.**
    s 386AKA(1) opens "A company or foreign company registered under Division 2 of Part 11 must keep a register of its directors who are nominees"; s 386ALA(1) opens "A company or foreign company must keep a register of its shareholders who are nominees".
    The two registers are otherwise parallel, so a reader who takes the phrase to qualify both words of s 386AKA(1) would give the directors' register a narrower reach than the shareholders' (fork F-AKA1).
14. **s 386AA(1A) lifts the Schedule exemption for six provisions.**
    "Despite subsection (1)", ss 386AG(6), 386AH(6), 386AI(6), 386AIA(3), 386AJ and 386AK apply to a person who is, or of whom there are reasonable grounds to believe is, a registrable controller of a company or foreign company that is not itself in the Schedule, "whether or not the person is" a company in the Fourteenth Schedule or a foreign company in the Fifteenth Schedule (25394-25404).
    So a Schedule company that holds a significant interest in a company outside the Schedules still has the notice and notification duties of those six provisions.

## What the stable binary does not accept

The stable build 1.6.110 is the binary; where the skills describe a construct it rejects, the binary governs.
Found while writing this row:

- **`NOT a AND b` parses as `NOT (a AND b)`.**
  Three assertions of `s 386AO(1)` failed until each `NOT` was parenthesised; every `NOT` in a conjunction in these modules is parenthesised.
  This is a wrong answer with exit code 0 if it is missed, so it is the failure that does not announce itself.
- **A residual trace prints the rule's own text, and that text contains "LEST BREACH".**
  A harness that searches the message for "BREACH" counts every residual obligation as a breach; a real breach message starts `DEONTIC BREACHED`.
  `work/traces.py` tests for that prefix (it did not at first, and reported residual traces as breaches; fixed, 0 mismatches since).
- **`check.sh` counts assertions only.**
  Its own last line says it does not see a different TRACE outcome, so the 138 traces are compared by `work/traces.py` on both builds, with the `-- EXPECT` word above each.
- **Not used because the brief names them as unavailable on the stable binary, and not tested by me:** `REFUSE`, `YMD`, `TYPICALLY` on fields.
  Every `#ASSERT` is on one line, and `WAITUNTIL` is used in 13 traces.
- **Each duty with a time limit is both a rule and a decision function.**
  The rule is exercised by `#TRACE`; the function (the timing helper, `s 386AF(8) timing: ...`) is asserted.

No type or constructor was missing from the core, so there is no `NEEDS-CORE.md`.

## The seat layer

`sgn-seat.l4` asks 58 questions "Under section N, ...", in five groups, one for each of: ss 386AA to 386AC; ss 386AF and 386AFA; ss 386AG to 386AK; ss 386AKA to 386ALB; ss 386AM to 386AP.
The seat is an individual who is a director, the company secretary or a member of a company (or of a foreign company), or deals with one (assumed, not ruled; the Act is addressed to companies).
There is no seat for the Registrar, the Minister or the Authority; their powers appear only as what they mean to the individual.
Every question has an `@export` and an `@desc`, takes plain inputs (a fact each, with a description worded as the person would be asked it, and the same name and `@desc` for the same fact in every question), and calls the layer-1 function of the same provision.
`sgn-cases-seat.l4` has 150 assertions that exercise them.
The one place a record would have been needed is s 386AC, which takes a list of the kinds of controller through which the person holds the interest; the seat asks one kind and wraps it.
The amounts, periods and forms the regulations prescribe, the appointed days and the Schedules' lists are inputs the person supplies.

## What check.sh prints

Run from the output folder as `L4=<l4-main-110> L4_MAIN=<l4-main-109> ./check.sh`.
It exits 0.
The baseline it replaced is the keel's own run, copied in `inputs/KEEL-NOTES.md` ("What `check.sh` prints"): 17 modules, 0 errors, 974 assertions satisfied, 0 failed, 0 refused, the same four counts on both builds, exit 0.
This folder holds the eight keel modules without their test files, so the run below has 23 modules and the keel modules show 0 assertions each; all 816 satisfied assertions are this part's, and the keel's 974 are not in this run's total.

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
sgn-application.l4                             0         0       0        0         0 |      0         0       0        0  same
sgn-cases-seat.l4                              0       150       0        0         0 |      0       150       0        0  same
sgn-evidence.l4                                0         0       0        0         0 |      0         0       0        0  same
sgn-nominees.l4                                0         0       0        0         0 |      0         0       0        0  same
sgn-notices.l4                                 0         0       0        0         0 |      0         0       0        0  same
sgn-register.l4                                0         0       0        0         0 |      0         0       0        0  same
sgn-registrar.l4                               0         0       0        0         0 |      0         0       0        0  same
sgn-seat.l4                                    0         0       0        0         0 |      0         0       0        0  same
sgn-tests-application.l4                       0        83       0        0         0 |      0        83       0        0  same
sgn-tests-evidence.l4                          0        42       0        0         0 |      0        42       0        0  same
sgn-tests-nominees-rules.l4                    0         0       0        0         0 |      0         0       0        0  same
sgn-tests-nominees.l4                          0       130       0        0         0 |      0       130       0        0  same
sgn-tests-notices.l4                           0       166       0        0         0 |      0       166       0        0  same
sgn-tests-register.l4                          0       138       0        0         0 |      0       138       0        0  same
sgn-tests-registrar.l4                         0       107       0        0         0 |      0       107       0        0  same
TOTAL (23 modules)                             0       816       0        0           |      0       816       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

## The text is a rendering

The source is a plain-text rendering of the Singapore Statutes Online informal consolidation, not the official text of the Act; a quotation in a module is a line of that rendering, and its `@ref` locator names the lines.

## The S1b ruling on failed gates (2026S1bC)

The Guide records this ruling at section 5, in the bullet that begins “Failed gates of the pure “may” functions”; it is copied here word for word, as the Guide asks of every ruling.

> - **Failed gates of the pure "may" functions of the two Singapore encodings: the split follows the background, not the holder's name (card S1b of the bench "Singapore Split Sites", option C as modified on the card; accepted by Meng).** Conditions as printed on the card: (1) It governs only the functions that stay Boolean after the protocol split, the pure gates (58 on the card's line); the type (i) sites, an unmet element of an offence, are unchanged. (2) A failed gate answers `JUST FALSE` where the function is a public body's power, a relief from an express bar or duty, or a gate the text closes (“so long as”, “only if”); it answers `NOTHING` where it states a company's or person's liberty, standard or privilege with no bar to relieve. (3) At the card's reading that changes 16 answers: 6 `NOTHING` to `JUST FALSE` at public bodies, and 10 `JUST FALSE` to `NOTHING` at liberties (C024, C046, C084, C115, C135, C138, C154, C155, C157, C159), each a fork line with the other reading and each borderline, because a relief and a liberty are a judgment. The 10 liberties that already answered `NOTHING` stay. (4) Applied one commit per part, each “assumed, not ruled” until the card was marked, flipping the branch each site's tag marks. (5) The difference between an express bar and silence stays in the code's `FALSE-kind` and `NOTHING-kind` comments and in NOTES, which is the provenance channel, and not in the truth value. (6) Recorded in this guide, with limit 3 of the grant ruling above replaced for the Singapore rows, and in the `NOTES.md` of the parts that carry limit 3 (the card's own wording; this paragraph is that record). (7) The ruling reaches the two Singapore encodings only. The UK (164 listed sites) and Israel stay on the Guide as it stands until Meng rules; until then the differential compares Singapore under C with the UK under limit 3. The sites the 16 answers belong to: the public-body powers that went from `NOTHING` to `JUST FALSE` are s 173F (C045), s 32(4) (C106), s 139(6) (F018), s 139(10) (F019), s 282AA(1) (F057), s 281(1) (F062); the liberties that went from `JUST FALSE` to `NOTHING` are s 145(1), s 202A(2), s 21(7), s 130(2), s 173J(3), s 179(2), s 387A(1), s 387B(1), s 387D, s 390(1). Meng's note, verbatim: “Suggest that the changed encodings, and future rules encoded under this ruling, be marked with a greppable string like 2026S1bC to show where this rule took effect. Then in future we can revisit and review the consequences of this rule on encodings that haven’t been done today.” Marked 2026-11-21T12:17:37.989Z (accept, option C, not blind), ruled 2026-11-21, so the commits that applied it are ruled and no longer “assumed, not ruled”. Reading of the note (assumed, not ruled): each function this ruling changed, and each function encoded later under it in these two encodings, carries the string `2026S1bC` in its `FALSE-kind` or `NOTHING-kind` comment, and on its `FORK` line where it has one, so that `grep -rn 2026S1bC` lists where the rule took effect and a later review can find its consequences. Bench: https://claude.ai/artifact/SYSny5zjFYHHcMFeNYi5RX

No site of this part changed under it (2026S1bC): the functions of this part that stay Boolean after the protocol split already answered as the ruling reads, and its protocol-shaped functions keep limit 3 of the grant ruling until they are re-encoded.
