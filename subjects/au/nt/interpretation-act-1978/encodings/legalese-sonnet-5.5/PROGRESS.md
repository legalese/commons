# Progress

Encoding of the Interpretation Act 1978 (Northern Territory), reprint as in force at 21 April 2023, text file `11865.txt`.
The in-scope text is the Act and its Schedule: lines 149 to 962 of the text file.
Lines 1 to 148 are the deposit notice, the cover, the table of provisions, the title and the long title.
Lines 963 to 1531 are the endnotes, which section 55(6) says are not part of the Act.

## State

Every module is written, type-checks and passes its tests: 33 modules, 1600 assertions satisfied, none failed, none refused, on both builds.
`srcrefs.py check` and `check --strict` report 0 problems.
`NOTES.md` is generated from the files by a script that stops on any citation it cannot find, so its line numbers, function names and counts are read from the files.
The coverage table has 661 rows over 814 non-blank lines: 515 encoded, 41 fork, 105 inert.

## Modules and their tests

- `nt-interpretation-time.l4` with `nt-tests-time.l4`: sections 5, 6, 6A, 6B, 11 to 16, 17 ("calendar month", "month", "year", "business day", "calendar year", "financial year", "sitting day"), 25(2) to (4), 28, 29, 30, 63B.
- `nt-provisions.l4` with `nt-tests-xrefs.l4`: the provision index (one entry per Part, Division, section, subsection, paragraph, subparagraph, the Schedule and each Part of it).
- `nt-xrefs.l4` with `nt-tests-xrefs.l4`: the cross-reference rows.
- `nt-part1-application.l4` with `nt-tests-part1.l4`: sections 2(3), 2(4), 3, 4.
- `nt-part2-commencement.l4` with `nt-tests-part2.l4`: sections 7, 8, 9.
- `nt-part4-reading.l4` with `nt-tests-part4-reading.l4`: sections 18 to 38A (except those in the time module).
- `nt-part4-definitions.l4` with `nt-tests-part4-definitions.l4`: section 17, definitions (a generated table of 133 and hand-written functions).
- `nt-part4a-penalties.l4` with `nt-tests-part4a.l4`: sections 38B to 38G.
- `nt-part5-powers.l4` with `nt-tests-part5.l4`: sections 39 to 48B.
- `nt-part6-mechanics.l4` with `nt-tests-part6.l4`: sections 49 to 57B.
- `nt-part7-construction.l4` with `nt-tests-part7-construction.l4`: sections 58 to 62E.
- `nt-part7-instruments.l4` with `nt-tests-part7-instruments.l4`: sections 63 to 66.
- `nt-part7-general.l4` with `nt-tests-part7-general.l4`: sections 66A to 72.
- `nt-part7a-reprints.l4` with `nt-tests-part7a.l4`: sections 72A to 72D.
- `nt-part8-transitional.l4` with `nt-tests-part8.l4`: sections 73 to 78.
- `nt-schedule.l4` with `nt-tests-schedule.l4`: the Schedule and section 2(1), (2).
- `nt-seat.l4` with `nt-cases-seat.l4`: layer 2: the seat's questions.

## Decisions taken

Each is a fork-register entry in `NOTES.md`, with the text that licenses it:

- F1: Which day starts the count of a period.
- F2: Months and years are counted one calendar month at a time.
- F3: Section 28(2) applies to periods of days, months and years.
- F4: Periods in subordinate legislation.
- F5: Weeks, and lengths that are not whole positive numbers.
- F6: Day of service of a document given to a person.
- F7: Service by fax: the current number and evidence to the contrary.
- F8: Subordinate legislation that commences on a day fixed by Gazette notice.
- F9: "Subject to section 2" in section 3(1).
- F10: Section 8(2)(b): taking effect before the commencement.
- F11: Section 9: the period in which a proposed law may be cited and amended.
- F12: A reference to a paragraph inside a subsection (section 53(3) and (4)).
- F13: Section 40(1)(b): "1 year after the office-holder ceased to hold office".
- F14: Individuals under "person" and "party".
- F15: "Sufficient" in sections 66A(1) and 68.
- F16: "Alphabetical order" in section 57B.
- F17: Items numbered "in the order" when two have the same day.
- F18: Periods counted in sitting days and months after a day (sections 63, 63A, 63C, 64).
- F19: Part-day public holidays in section 28(2).
- F20: Section 19A(1)(b): both persons Aboriginal or Torres Strait Islander.

Rulings applied everywhere: a function answers JUST FALSE where the text itself says no, and NOTHING where it is silent, lists without closing, says "includes", leaves a term undefined, or limits a permission without the word "only".

## Still to do

- A domain expert reads each rule against the official text.
- The seat layer is run through the website's question form.
- The public holidays and the sitting days of the Legislative Assembly are supplied by the user; tables of them are not among the sources.
