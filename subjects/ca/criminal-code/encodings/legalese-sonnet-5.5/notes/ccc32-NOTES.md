# NOTES.md -- part ccc32: the related and transitional provisions of amending Acts, and the amendments not in force (Criminal Code (Canada), lines 19056-19797)

Status (2026-11-13, agent ccc32, run dst-ccc32): complete as filed.
How each claim here was checked: the counts in the coverage table, the audit and the branch lists were produced by scripts from the files on disk (the generator is in `../../../work/` and is not shipped); the layer-1 modules, the tests, the seat and the cases were run with the stable `l4` (1.6.110) and `check.sh`; the quotations were checked by `srcrefs.py check --refs` and `--strict`; nothing was checked against the official text.

**The source is not the official text.**
It is a plain-text rendering, made by a converter script, of the Justice Laws Website consolidation of the Criminal Code (current to 2026-09-30).
Nothing in this encoding is claimed to be verified against the official text; the French version is equally authoritative and was not among the sources.
The quotations in the `-- src:` lines are copied by script from the converter's text and are the converter's wording, never the official wording; the glosses beside them are plain-language comments.

## What this range is

The range is lines 19056-19797 of the text, 12,598 words, 612 non-blank lines, in two bands.
1. Lines 19056-19516: "Related provisions of amending Acts", from 1991, c. 43, s. 10 to 2026, c. 19, s. 119: application rules, deeming rules, continuing-application rules, clarifications, and reviews by Parliament.
2. Lines 19517-19797: "AMENDMENTS NOT IN FORCE": replacement texts that are not law today (the victim surcharge, the sentence-forwarding rule, release pending a review, the whole of Part XXI.1 as replaced, the exemptions from sex offender registration, and the new offence of coercion or control of an intimate partner), and coordinating clauses.

A not-in-force block is a SECOND, FUTURE text of provisions that other parts encode in their in-force form (for example ccc9 for section 241.2, ccc24 for section 679, ccc27 for sections 737 and 743.2, ccc18 for sections 490.02 to 490.06).
Every name of such text carries `(not in force)` after its section label, so it cannot collide with theirs, and nothing in these modules says the text is law today.

Nothing in this range carries a date of commencement.
Every "the day on which section N comes into force" is therefore a DATE input that a caller states; the one day the text computes is the commencement day of 2026, c. 19 (the 30th day after royal assent, section 96), and the assent date is an input.

## Departures from PLAN.md and from the brief (stated, as the brief asks)

1. **Names of amending-Act provisions.** PLAN.md section 1 says every top-level name begins with `s 4(2)(a) ...`, the Act's own numbering. An amending Act's section `s 5` would collide with the Code's `s 5` and with every other amending Act's section 5, so a provision of an amending Act is named `2015 c 13 s 44 ...` (year, chapter, section, as the text's header writes them). Replacement text of the Code itself follows PLAN.md section 6: `s 696.4(3) (not in force) ...`.
2. **Seat questions** begin `Under section 5 of 2009 c 29, ...` for an amending-Act provision and `Under section 696.4(3) (not in force), ...` for replacement text, because the brief's form `Under section N,` alone would be ambiguous between the two.
3. **PLAN.md section numbers.** The brief points at PLAN.md sections 2, 3, 4, 5 and 6 for the naming rule, the core, the seams, the traps and the part rows. In the PLAN.md in my inputs the naming rule is in section 1, the core in section 2, the seam rules in section 3, the definition sections in section 5, the part rows in section 6 and the seam table in section 7; there is no section of traps. I used the sections by their titles. Where PLAN.md and the brief differ, the brief governs.
4. **Periods.** PLAN.md says periods keep the text's units and use the core's `Length of time`, never a day count. Every period in this range runs from a date a caller states to a date compared with a date ("within 180 days after", "on that day or within 14 days after", "not later than 14 days before the day first appointed", "more than six months after"), so the rules use `Date`, `PLUS n` days and daydate's `add months` and `add years`. The core's `Length of time` is used only for `ten years` in section 264.01(4).
5. **Own party and act types.** The Miscarriage of Justice Review Commission and a medical practitioner or nurse practitioner are not in the core's `Party`, so the modules declare small types of their own under their prefix (`s 696.1 (not in force) party`, `2021 c 2 s 4 party`); NEEDS-CORE.md lists them.
6. **Regulative rules and the stable binary.** A DEONTIC value cannot be asserted on the stable binary (finding in the section on what the binary does not accept), so every regulative rule is run with `#TRACE` and each duty is also written as a decision function ("... owes the duty to ...") that is asserted.

## Coverage (ccc32)

One row per unit of the range, built from the text by `parse_rows.py` and mapped to the L4 names by `coverage.py`, which reads the `@ref (src:lo-hi)` locators of the layer-1 modules, so an L4 name in the table is a name that exists in a module (each is also checked by `names.py`).
A row begins at the line after the previous row's last line and ends at its unit line (a numbered section, a subsection `(n)`, a paragraph `(a)`, a subparagraph `(i)` or a defined term); the header lines (`-- 2015, c. 13, s. 37`) and the marginal notes and headings that precede a unit line belong to its row (inert, reason 1: not operative, carried by the row they precede).

### Audit counts

- Lines in the range: 742; blank: 130; non-blank: 612.
- Every one of the 612 non-blank lines lies in exactly one row (asserted by the script that wrote this file, which stops if one does not).
- Text units counted independently of the row parser (lines that begin with a section number, `(n)`, `(a)`, `(i)`, or that are a defined term with its French equivalent): 307. Header lines `-- year, c. n, s. m`: 124. Headings and marginal notes: 181.
- Rows in the table before the audit: 307; after: 307. The audit added and removed no row: the independent count of units (307) equals the rows.

### Counts per disposition

| disposition | rows |
| --- | --- |
| encoded | 158 |
| fork | 87 |
| inert | 60 |
| repealed or blank in this text | 2 |
| total | 307 |

Layer 1 holds 198 named decision functions and rules in eight modules, with 683 assertions and 15 traces in eight test files (`check.sh` below).
The seat layer holds 147 questions under 7 `§` headings and 231 cases.

### Rows left inert, with the reason number

Reason 1 (not operative): the headings and marginal notes, which ride with the row of the unit they precede; no row is inert for reason 1 alone.
Reason 3 (text shown repealed or blank): rows r006 and r007 are dispositioned `repealed or blank in this text` (the text shows `(c) and (d) [Repealed, 2005, c. 22, s. 43]` and `(4) to (7) [Repealed, 2005, c. 22, s. 43]`); each is also kept as a constant that shows the text.
Reason 2 (machinery): the rows below.

| rows | what they are | why inert (reason 2) |
| --- | --- | --- |
| r015-r017, r026-r029, r040-r043, r047-r048, r070-r072, r074-r080, r089-r095, r101, r104-r109, r147-r148, r213 | reviews and reports by Parliament, a committee or a Minister: 2005 c 32 s 27.1; 2009 c 28 s 12; 2014 c 6 s 20.1; 2014 c 25 s 45.1; 2016 c 3 ss 9.1, 10; 2018 c 21 s 31.1; 2021 c 2 ss 3.1, 5; 2022 c 15 s 21; 2022 c 17 ss 78.1, 78.2; 2023 c 30 s 2; 2023 c 32 s 14.2; 2024 c 1 s 2; 2026 c 19 ss 118.1, 119; s 696.62 (not in force) | committee/ministerial review or report (a duty on Parliament, a committee or a Minister to review and report): no person under the Code holds a right or bears a duty from it (fork F19) |
| r151-r156 | coordinating clauses among Bills: 2018 c 21 s 51; 2018 c 29 ss 79, 80 | coordinating clause among Bills (which of two amending Acts prevails, or a renumbering): amends other enactments' commencement and numbering and affects no one under the Code |
| r274 | 2026 c 16 s 53 | a change of the title of an office in the wording of Form 52 ("Canadian Forces Provost Marshal" to "Provost Marshal General"): a Form that only prescribes the wording of a document is machinery |
| r236, r238, r240, r244, r246, r250, r255, r257, r260, r264, r268, r270, r272 | the amending instructions of 2026 c 16 ss 48 to 52 ("X is replaced by the following", "is amended by adding") | the instruction itself creates no rule: it names the text it replaces or adds to; the text it enacts is encoded in the row that follows it (the replacement row of each instruction: r236 in r237; r238 in r239; r240 in r241-r243; r244 in r245; r246 in r247-r249; r250 in r251-r254; r255 in r256; r257 in r258-r259; r260 in r261-r263; r264 in r265-r267; r268 in r269; r270 in r271; r272 in r273) |

Inert rows in all: 60 (committee, parliamentary and ministerial reviews: 40, see fork F19; amending instructions that only name the text replaced; coordinating clauses; the wording of Form 52).

### The table

Columns: row, lines, provision, disposition, the L4 name(s) that encode it (a function, or a type that the function reads), and the number of test assertions that call the first name (`tests`), and of seat questions (`seat`).

| row | lines | provision | disposition | L4 name | tests | seat |
| --- | --- | --- | --- | --- | --- | --- |
| r001 | 19056-19058 | 1991 c 43 s 10(1) | encoded | `1991 c 43 s 10(1) the order for detention continues in force` | 8 | 1 |
| r002 | 19059-19060 | 1991 c 43 s 10(2) | fork (F2) | `1991 c 43 s 10(2) the Review Board must review the case`; `1991 c 43 s 10(2) the review was within twelve months after the coming into force` | 9 | 1 |
| r003 | 19061-19062 | 1991 c 43 s 10(3) | encoded | `1991 c 43 s 10(3) the section applies, with such modifications as the circumstances require, to the review` | 6 | 1 |
| r004 | 19063-19063 | 1991 c 43 s 10(3)(a) | encoded | `1991 c 43 s 10(3) the section applies, with such modifications as the circumstances require, to the review`; `1991 c 43 s 10(3)(a) the review is treated as a review of a disposition conducted under section 672.81` | 8 | 1 |
| r005 | 19064-19064 | 1991 c 43 s 10(3)(b) | encoded | `1991 c 43 s 10(3) the section applies, with such modifications as the circumstances require, to the review`; `1991 c 43 s 10(3)(b) the warrant is treated as a disposition made under section 672.54` | 9 | 1 |
| r006 | 19065-19065 | 1991 c 43 s 10(3)(c) and (d) | repealed or blank in this text | `1991 c 43 s 10(3)(c) and (d) as the text shows them` | 1 | 0 |
| r007 | 19066-19066 | 1991 c 43 s 10(4) to (7) | repealed or blank in this text | `1991 c 43 s 10(3)(c) and (d) as the text shows them`; `1991 c 43 s 10(4) to (7) as the text shows them` | 2 | 0 |
| r008 | 19068-19070 | 2004 c 12 s 22 | fork (F20) | `2004 c 12 s 22 the reference is read as referring to` | 4 | 0 |
| r009 | 19071-19071 | 2004 c 12 s 22(a) | fork (F20) | `2004 c 12 s 22 the reference is read as referring to` | 4 | 0 |
| r010 | 19072-19072 | 2004 c 12 s 22(b) | fork (F20) | `2004 c 12 s 22 the reference is read as referring to` | 4 | 0 |
| r011 | 19073-19073 | 2004 c 12 s 22(c) | fork (F20) | `2004 c 12 s 22 the reference is read as referring to` | 4 | 0 |
| r012 | 19075-19077 | 2004 c 12 s 23 | fork (F20) | `2004 c 12 s 23 the reference is read as referring to` | 3 | 0 |
| r013 | 19078-19078 | 2004 c 12 s 23(a) | fork (F20) | `2004 c 12 s 23 the reference is read as referring to` | 3 | 0 |
| r014 | 19079-19079 | 2004 c 12 s 23(b) | fork (F20) | `2004 c 12 s 23 the reference is read as referring to` | 3 | 0 |
| r015 | 19081-19083 | 2005 c 32 s 27.1(1) | inert (reason 2: machinery) | none | 0 | 0 |
| r016 | 19084-19085 | 2005 c 32 s 27.1(2) | inert (reason 2: machinery) | none | 0 | 0 |
| r017 | 19087-19089 | 2009 c 28 s 12 | inert (reason 2: machinery) | none | 0 | 0 |
| r018 | 19091-19093 | 2009 c 29 s 5 | fork (F12) | `2009 c 29 s 5 the person is within the limit on subsections 719(3) to (3.4)` | 3 | 1 |
| r019 | 19095-19097 | 2011 c 2 s 7(1) | encoded | `2011 c 2 s 7(1) the application is dealt with and disposed of under the Code as it read immediately before that day` | 3 | 1 |
| r020 | 19098-19099 | 2011 c 2 s 7(2) | fork (F1, F2) | `2011 c 2 s 7(2) the person may make an application under subsection 745.6(1) as amended` | 6 | 1 |
| r021 | 19100-19101 | 2011 c 2 s 7(3) | fork (F1) | `2011 c 2 s 7(3) the person may make an application under subsection 745.6(1) as amended` | 6 | 1 |
| r022 | 19103-19105 | 2012 c 1 s 163 | encoded | `2012 c 1 s 163(a) the reference to an application for a record suspension is also a reference to an application for a pardon` | 5 | 1 |
| r023 | 19106-19106 | 2012 c 1 s 163(a) | encoded | `2012 c 1 s 163(a) the reference to an application for a record suspension is also a reference to an application for a pardon` | 5 | 1 |
| r024 | 19108-19110 | 2012 c 1 s 165 | encoded | `2012 c 1 s 165(b) the reference to a record suspension is also a reference to a pardon` | 4 | 1 |
| r025 | 19111-19111 | 2012 c 1 s 165(b) | encoded | `2012 c 1 s 165(b) the reference to a record suspension is also a reference to a pardon` | 4 | 1 |
| r026 | 19113-19115 | 2014 c 6 s 20.1(1) | inert (reason 2: machinery) | none | 0 | 0 |
| r027 | 19116-19117 | 2014 c 6 s 20.1(2) | inert (reason 2: machinery) | none | 0 | 0 |
| r028 | 19119-19121 | 2014 c 25 s 45.1(1) | inert (reason 2: machinery) | none | 0 | 0 |
| r029 | 19122-19123 | 2014 c 25 s 45.1(2) | inert (reason 2: machinery) | none | 0 | 0 |
| r030 | 19125-19127 | 2015 c 13 s 37 | fork (F17) | `2015 c 13 s 37 subsection 278.3(5) as it read immediately before that day continues to apply to the hearing` | 5 | 1 |
| r031 | 19129-19131 | 2015 c 13 s 38 | fork (F14) | `2015 c 13 s 38 section 380.3 as it read immediately before that day continues to apply to the request for restitution` | 3 | 1 |
| r032 | 19133-19135 | 2015 c 13 s 39 | fork (F14) | `2015 c 13 s 39 section 380.4 as it read immediately before that day continues to apply to the statement` | 3 | 1 |
| r033 | 19137-19139 | 2015 c 13 s 40 | fork (F12) | `2015 c 13 s 40 the conduct is within the limit on section 423.1` | 3 | 1 |
| r034 | 19141-19143 | 2015 c 13 s 41 | fork (F14) | `2015 c 13 s 41 section 672.5 as it read immediately before that day continues to apply to the statement` | 3 | 1 |
| r035 | 19145-19147 | 2015 c 13 s 42 | fork (F12) | `2015 c 13 s 42 the conduct is within the limit on the amendments to section 718` | 3 | 1 |
| r036 | 19149-19151 | 2015 c 13 s 42.1 | fork (F12) | `2015 c 13 s 42.1 the conduct is within the limit on the amendment to paragraph 718.2(e)` | 3 | 1 |
| r037 | 19153-19155 | 2015 c 13 s 43 | fork (F14) | `2015 c 13 s 43 section 722 as it read immediately before that day continues to apply to the statement` | 3 | 1 |
| r038 | 19157-19159 | 2015 c 13 s 44 | fork (F12) | `2015 c 13 s 44 the conduct is within the limit on section 737.1 and sections 739.1 to 739.4` | 3 | 1 |
| r039 | 19161-19163 | 2015 c 20 s 28 | encoded | `2015 c 20 s 28 the information is deemed to have been laid under subsection 810.011(1)` | 4 | 1 |
| r040 | 19165-19167 | 2016 c 3 s 9.1(1) | inert (reason 2: machinery) | none | 0 | 0 |
| r041 | 19168-19168 | 2016 c 3 s 9.1(2) | inert (reason 2: machinery) | none | 0 | 0 |
| r042 | 19170-19172 | 2016 c 3 s 10(1) | inert (reason 2: machinery) | none | 0 | 0 |
| r043 | 19173-19174 | 2016 c 3 s 10(2) | inert (reason 2: machinery) | none | 0 | 0 |
| r044 | 19176-19178 | 2018 c 12 s 406(1) | fork (F14) | `2018 c 12 s 406(1) a remediation agreement may be entered into in respect of the offence` | 3 | 1 |
| r045 | 19179-19180 | 2018 c 12 s 406(2) | encoded | `2018 c 12 s 406(2) the term has the meaning it has in section 715.3` | 4 | 0 |
| r046 | 19182-19184 | 2018 c 21 s 10 | encoded | `2018 c 21 s 10 the thing is deemed to be approved, as the same kind of thing, under section 254.01 as enacted by section 4` | 5 | 1 |
| r047 | 19186-19188 | 2018 c 21 s 31.1(1) | inert (reason 2: machinery) | none | 0 | 0 |
| r048 | 19189-19190 | 2018 c 21 s 31.1(2) | inert (reason 2: machinery) | none | 0 | 0 |
| r049 | 19192-19194 | 2018 c 21 s 32(1) | encoded | `2018 c 21 s 32(1) section 320.34 as enacted by section 15 applies to the application` | 3 | 1 |
| r050 | 19195-19196 | 2018 c 21 s 32(2) | encoded | `2018 c 21 s 32(2) subsection 320.31(1) as enacted by section 15 applies to the trial` | 3 | 1 |
| r051 | 19198-19200 | 2018 c 21 s 33 | encoded | `2018 c 21 s 33 section 320.36 as enacted by section 15 applies to the thing` | 4 | 1 |
| r052 | 19202-19204 | 2018 c 21 s 34(1) | encoded | `2018 c 21 s 34(1) an appeal may be taken against the order`; `2018 c 21 s 34(1) the appeal is taken under section 675 and disposed of under the provisions of the Act, each as it read immediately before that day` | 5 | 2 |
| r053 | 19205-19206 | 2018 c 21 s 34(2) | encoded | `2018 c 21 s 34(2) sections 261 and 680 as they read immediately before that day apply to the appeal` | 2 | 1 |
| r054 | 19208-19210 | 2018 c 21 s 35 | encoded | `2018 c 21 s 35 the thing is deemed to be approved, as the same kind of thing, under section 320.39 as enacted by section 15` | 6 | 1 |
| r055 | 19212-19214 | 2018 c 21 s 36 | encoded | `2018 c 21 s 36 the person is deemed to be designated as a qualified technician under paragraph 320.4(a)` | 2 | 1 |
| r056 | 19216-19218 | 2018 c 21 s 37 | encoded | `2018 c 21 s 37 the person is deemed to be designated as a qualified technician under subparagraph 320.4(b)(i)` | 2 | 1 |
| r057 | 19220-19222 | 2018 c 21 s 38 | encoded | `2018 c 21 s 38 the person is deemed to be designated as an analyst under subparagraph 320.4(b)(ii) and paragraph 320.4(c)` | 2 | 1 |
| r058 | 19224-19226 | 2018 c 29 s 74 | fork (F17) | `2018 c 29 s 74 subsection 278.3(5) as it read immediately before that day continues to apply to the hearing` | 5 | 1 |
| r059 | 19228-19230 | 2019 c 13 s 155 | fork (F14) | `2019 c 13 s 155 paragraph 83.05(1)(b) and subsection 83.05(3) as they read immediately before that day continue to apply to the application` | 4 | 0 |
| r060 | 19232-19234 | 2019 c 13 s 156 | encoded | `2019 c 13 s 156 the proceedings are to be completed under sections 83.28 and 83.29 as they read before that day` | 3 | 0 |
| r061 | 19236-19238 | 2019 c 13 s 157 | fork (F16) | `2019 c 13 s 157 a report is to be prepared under subsection 810.011(15)` | 2 | 0 |
| r062 | 19240-19242 | 2019 c 13 s 157.1 | encoded | `2019 c 13 s 157.1 section 83.3 becomes effective again as of the day on which this section comes into force`; `2019 c 13 s 157.1 sections 146 and 148 of 2019, c. 13 apply in respect of section 83.3` | 4 | 1 |
| r063 | 19244-19246 | 2019 c 25 s 354 | fork (F3) | `2019 c 25 s 354 the person is deemed to be bound by an appearance notice as defined in section 2` | 4 | 1 |
| r064 | 19248-19250 | 2019 c 25 s 355 | fork (F3) | `2019 c 25 s 355 the person is deemed to be bound by an undertaking as defined in section 2` | 5 | 1 |
| r065 | 19252-19254 | 2019 c 25 s 356 | fork (F3) | `2019 c 25 s 356 the person is deemed to be bound by an undertaking as defined in section 2` | 5 | 1 |
| r066 | 19256-19258 | 2019 c 25 s 357 | fork (F3) | `2019 c 25 s 357 the person is deemed to be bound by a release order as defined in section 2` | 7 | 1 |
| r067 | 19260-19262 | 2019 c 25 s 358 | fork (F3) | `2019 c 25 s 358 the person is deemed to be bound by a release order as defined in section 2` | 4 | 1 |
| r068 | 19264-19266 | 2019 c 25 s 359 | fork (F4, F25) | `2019 c 25 s 359 the person may elect another mode of trial` | 9 | 1 |
| r069 | 19268-19270 | 2019 c 25 s 360 | fork (F2) | `2019 c 25 s 360 the proceedings are within the time limit` | 7 | 1 |
| r070 | 19272-19274 | 2021 c 2 s 3.1(1) | inert (reason 2: machinery) | none | 0 | 0 |
| r071 | 19275-19276 | 2021 c 2 s 3.1(2) | inert (reason 2: machinery) | none | 0 | 0 |
| r072 | 19277-19278 | 2021 c 2 s 3.1(3) | inert (reason 2: machinery) | none | 0 | 0 |
| r073 | 19280-19282 | 2021 c 2 s 4 | encoded | `2021 c 2 s 4 the provider must provide medical assistance in dying in accordance with the old section 241.2`; `2021 c 2 s 4 the provider must provide it in accordance with the old section 241.2 and subsections 241.2(3.2) to (3.5)` | 4 | 1 |
| r074 | 19284-19286 | 2021 c 2 s 5(1) | inert (reason 2: machinery) | none | 0 | 0 |
| r075 | 19287-19288 | 2021 c 2 s 5(2) | inert (reason 2: machinery) | none | 0 | 0 |
| r076 | 19289-19290 | 2021 c 2 s 5(3) | inert (reason 2: machinery) | none | 0 | 0 |
| r077 | 19291-19292 | 2021 c 2 s 5(4) | inert (reason 2: machinery) | none | 0 | 0 |
| r078 | 19293-19294 | 2021 c 2 s 5(5) | inert (reason 2: machinery) | none | 0 | 0 |
| r079 | 19295-19296 | 2021 c 2 s 5(6) | inert (reason 2: machinery) | none | 0 | 0 |
| r080 | 19298-19300 | 2022 c 15 s 21 | inert (reason 2: machinery) | none | 0 | 0 |
| r081 | 19302-19304 | 2022 c 17 s 76 | fork (F5) | `2022 c 17 s 76 the amendments made by 2022, c. 17 apply to the proceedings, subject to sections 77 and 78` | 6 | 1 |
| r082 | 19306-19308 | 2022 c 17 s 77(1) | encoded | `2022 c 17 s 77(1) the Criminal Code as it read immediately before that day continues to apply` | 8 | 1 |
| r083 | 19309-19309 | 2022 c 17 s 77(1)(a) | encoded | `2022 c 17 s 77(1) the Criminal Code as it read immediately before that day continues to apply` | 8 | 1 |
| r084 | 19310-19310 | 2022 c 17 s 77(1)(b) | encoded | `2022 c 17 s 77(1) the Criminal Code as it read immediately before that day continues to apply` | 8 | 1 |
| r085 | 19311-19311 | 2022 c 17 s 77(1)(c) | encoded | `2022 c 17 s 77(1) the Criminal Code as it read immediately before that day continues to apply` | 8 | 1 |
| r086 | 19312-19312 | 2022 c 17 s 77(1)(d) | encoded | `2022 c 17 s 77(1) the Criminal Code as it read immediately before that day continues to apply` | 8 | 1 |
| r087 | 19313-19313 | 2022 c 17 s 77(1)(e) | encoded | `2022 c 17 s 77(1) the Criminal Code as it read immediately before that day continues to apply` | 8 | 1 |
| r088 | 19315-19317 | 2022 c 17 s 78 | encoded | `2022 c 17 s 78 section 489.1 as it read immediately before that day continues to apply to the thing seized` | 3 | 1 |
| r089 | 19319-19321 | 2022 c 17 s 78.1(1) | inert (reason 2: machinery) | none | 0 | 0 |
| r090 | 19322-19322 | 2022 c 17 s 78.1(1)(a) | inert (reason 2: machinery) | none | 0 | 0 |
| r091 | 19323-19323 | 2022 c 17 s 78.1(1)(b) | inert (reason 2: machinery) | none | 0 | 0 |
| r092 | 19324-19324 | 2022 c 17 s 78.1(1)(c) | inert (reason 2: machinery) | none | 0 | 0 |
| r093 | 19325-19326 | 2022 c 17 s 78.1(2) | inert (reason 2: machinery) | none | 0 | 0 |
| r094 | 19328-19330 | 2022 c 17 s 78.2(1) | inert (reason 2: machinery) | none | 0 | 0 |
| r095 | 19331-19332 | 2022 c 17 s 78.2(2) | inert (reason 2: machinery) | none | 0 | 0 |
| r096 | 19334-19336 | 2023 c 26 s 613 | encoded | `2023 c 26 s 613 the word or expression has the meaning it has in sections 347 and 347.1` | 4 | 0 |
| r097 | 19338-19340 | 2023 c 26 s 614 | fork (F16) | `2023 c 26 s 614 the definition criminal rate in subsection 347(2), as it reads on that day, applies to the receipt` | 4 | 1 |
| r098 | 19342-19344 | 2023 c 26 s 615 | fork (F16) | `2023 c 26 s 615 paragraph 347.1(2)(a.1), as it reads on that day, applies to the person` | 4 | 1 |
| r099 | 19345-19345 | 2023 c 26 s 615(a) | fork (F16) | `2023 c 26 s 615 paragraph 347.1(2)(a.1), as it reads on that day, applies to the person` | 4 | 1 |
| r100 | 19346-19346 | 2023 c 26 s 615(b) | fork (F16) | `2023 c 26 s 615 paragraph 347.1(2)(a.1), as it reads on that day, applies to the person` | 4 | 1 |
| r101 | 19348-19350 | 2023 c 30 s 2 | inert (reason 2: machinery) | none | 0 | 0 |
| r102 | 19352-19354 | 2023 c 30 s 3 | fork (F13) | `2023 c 30 s 3 the amendments made by 2023, c. 30 apply to the matter or proceeding` | 2 | 1 |
| r103 | 19356-19358 | 2023 c 32 s 14.1 | fork (F16) | `2023 c 32 s 14.1 paragraph (e) of the definition prohibited firearm applies to the firearm in relation to those proceedings` | 3 | 1 |
| r104 | 19360-19362 | 2023 c 32 s 14.2(1) | inert (reason 2: machinery) | none | 0 | 0 |
| r105 | 19363-19364 | 2023 c 32 s 14.2(2) | inert (reason 2: machinery) | none | 0 | 0 |
| r106 | 19366-19368 | 2024 c 1 s 2(1) | inert (reason 2: machinery) | none | 0 | 0 |
| r107 | 19369-19370 | 2024 c 1 s 2(2) | inert (reason 2: machinery) | none | 0 | 0 |
| r108 | 19371-19372 | 2024 c 1 s 2(3) | inert (reason 2: machinery) | none | 0 | 0 |
| r109 | 19373-19374 | 2024 c 1 s 2(4) | inert (reason 2: machinery) | none | 0 | 0 |
| r110 | 19376-19377 | 2024 c 22 s 8 | encoded | `2024 c 22 s 8 the information is deemed to have been laid under subsection 810.03(1)` | 10 | 1 |
| r111 | 19379-19381 | 2024 c 23 s 13 | encoded | `2024 c 23 s 13 the amendments made by 2024, c. 23 affect the validity of the proceedings`; `2024 c 23 s 13 the amendments made by 2024, c. 23 affect the validity of the document`; `2024 c 23 s 13 the reference to child pornography in the document is read as a reference to` | 9 | 3 |
| r112 | 19383-19385 | 2026 c 11 s 56 | encoded | `2026 c 11 s 56 the word or expression has the same meaning as in the Criminal Code` | 5 | 0 |
| r113 | 19387-19389 | 2026 c 11 s 57 | encoded | `2026 c 11 s 57 the provisions of the Criminal Code enacted by sections 41 and 42 apply to the proceeds of the fine` | 2 | 1 |
| r114 | 19391-19393 | 2026 c 11 s 58(1) | fork (F12) | `2026 c 11 s 58(1) the offence is within the limit on the provisions enacted by sections 8, 9, 11, 37, 40 and 43` | 3 | 1 |
| r115 | 19394-19395 | 2026 c 11 s 58(2) | fork (F13) | `2026 c 11 s 58(2) the amendments to Parts XVI and XXVIII made by 2026, c. 11 apply to the matter or proceeding` | 2 | 1 |
| r116 | 19396-19397 | 2026 c 11 s 58(3) | fork (F13) | `2026 c 11 s 58(3) the provisions enacted by sections 10, 34 to 36, 38 and 39 of 2026, c. 11 apply to the matter or proceeding` | 2 | 1 |
| r117 | 19399-19401 | 2026 c 12 s 15 | fork (F16) | `2026 c 12 s 15 subsection 236(2) applies to the offence` | 3 | 1 |
| r118 | 19403-19405 | 2026 c 12 s 16 | fork (F13) | `2026 c 12 s 16 subsection 490(2) as amended by section 3 of 2026, c. 12 applies to the matter or proceeding` | 2 | 1 |
| r119 | 19407-19409 | 2026 c 15 s 11.1(1) | fork (F18) | `2026 c 15 s 11.1(1) the clarification applies to the person's communication of the statement` | 4 | 1 |
| r120 | 19410-19411 | 2026 c 15 s 11.1(2) | fork (F18) | `2026 c 15 s 11.1(2) the clarification applies to the person's communication of the statement` | 3 | 1 |
| r121 | 19413-19415 | 2026 c 19 s 87 | encoded | `2026 c 19 s 87 the operation of the minimum punishment is affirmed following the enactment of section 718.4` | 2 | 1 |
| r122 | 19417-19419 | 2026 c 19 s 96 | encoded | `2026 c 19 s 96 the definitions apply in the section` | 5 | 0 |
| r123 | 19420-19420 | 2026 c 19 s 96 "Act" | encoded | `2026 c 19 s 96 Act` | 2 | 0 |
| r124 | 19421-19421 | 2026 c 19 s 96 "commencement day" | encoded | `2026 c 19 s 96 commencement day` | 4 | 1 |
| r125 | 19423-19425 | 2026 c 19 s 97 | fork (F12) | `2026 c 19 s 97 the act or omission is within the time limit on subsection 7(4.1)` | 3 | 1 |
| r126 | 19427-19429 | 2026 c 19 s 98 | fork (F16) | `2026 c 19 s 98 paragraphs 236(2)(b) to (d) apply to the offence` | 3 | 1 |
| r127 | 19431-19433 | 2026 c 19 s 99 | fork (F13) | `2026 c 19 s 99 paragraph 264(4)(a) applies to the matter or proceeding` | 2 | 1 |
| r128 | 19435-19437 | 2026 c 19 s 100 | fork (F12) | `2026 c 19 s 100 the offence is within the time limit on the provisions of sections 276, 276.01 to 276.13 and 278.1 to 278.38 named by this section` | 3 | 1 |
| r129 | 19439-19441 | 2026 c 19 s 101 | fork (F13) | `2026 c 19 s 101 subsection 346(1.4) applies to the matter or proceeding` | 2 | 1 |
| r130 | 19443-19445 | 2026 c 19 s 102 | fork (F13) | `2026 c 19 s 102 sections 486.1, 486.2 and 486.3 as amended by sections 38, 39 and 40 of 2026, c. 19 apply to the matter or proceeding` | 2 | 1 |
| r131 | 19447-19449 | 2026 c 19 s 103 | fork (F13) | `2026 c 19 s 103 subsection 489.1(4) applies to the matter or proceeding` | 2 | 1 |
| r132 | 19451-19453 | 2026 c 19 s 105 | fork (F12) | `2026 c 19 s 105 the offence is within the time limit on Part XV.1` | 3 | 1 |
| r133 | 19455-19457 | 2026 c 19 s 106 | fork (F13) | `2026 c 19 s 106 subsection 507.1(9) as enacted by section 47 of 2026, c. 19 applies to the matter or proceeding` | 2 | 1 |
| r134 | 19459-19461 | 2026 c 19 s 107 | fork (F13) | `2026 c 19 s 107 paragraphs 515(3)(a) and (b), (4.1)(a), (4.3)(c) and (6)(b.1) and (b.2), as construed in application of section 3.01, apply to the matter or proceeding` | 2 | 1 |
| r135 | 19463-19465 | 2026 c 19 s 108 | fork (F13) | `2026 c 19 s 108 subsections 537(1.001), 571(2), 645(3.1), 803(1.1) and 824(2) apply to the matter or proceeding` | 2 | 1 |
| r136 | 19467-19469 | 2026 c 19 s 109 | fork (F13) | `2026 c 19 s 109 section 657.4 applies to the matter or proceeding` | 2 | 1 |
| r137 | 19471-19473 | 2026 c 19 s 110 | fork (F14) | `2026 c 19 s 110 section 672.5011 applies to the order` | 3 | 1 |
| r138 | 19475-19477 | 2026 c 19 s 111(1) | fork (F3) | `2026 c 19 s 111(1) the measure is deemed to be an alternative measure, as defined in section 715.44` | 4 | 1 |
| r139 | 19478-19479 | 2026 c 19 s 111(2) | fork (F13) | `2026 c 19 s 111(2) the provisions enacted by sections 59, 64 and 65 of 2026, c. 19 apply to the matter or proceeding` | 2 | 1 |
| r140 | 19481-19483 | 2026 c 19 s 112 | fork (F13) | `2026 c 19 s 112 sections 722 and 722.2 as amended by sections 66 and 67 of 2026, c. 19 apply to the matter or proceeding` | 2 | 1 |
| r141 | 19485-19487 | 2026 c 19 s 113 | fork (F13) | `2026 c 19 s 113 section 726.21 applies to the matter or proceeding` | 2 | 1 |
| r142 | 19489-19491 | 2026 c 19 s 114 | fork (F12) | `2026 c 19 s 114 the offence is within the time limit on section 729.2` | 3 | 1 |
| r143 | 19493-19495 | 2026 c 19 s 115 | fork (F12) | `2026 c 19 s 115 the order is within the limits on section 740.1` | 3 | 1 |
| r144 | 19497-19499 | 2026 c 19 s 116 | fork (F12) | `2026 c 19 s 116 the offence is within the time limit on section 752.01` | 3 | 1 |
| r145 | 19501-19503 | 2026 c 19 s 117 | fork (F13) | `2026 c 19 s 117 section 810.03 as amended by section 81 of 2026, c. 19 applies to the matter or proceeding` | 2 | 1 |
| r146 | 19505-19507 | 2026 c 19 s 118 | fork (F13) | `2026 c 19 s 118 section 810.1 as amended by section 82 of 2026, c. 19 applies to the matter or proceeding` | 2 | 1 |
| r147 | 19509-19511 | 2026 c 19 s 118.1 | inert (reason 2: machinery) | none | 0 | 0 |
| r148 | 19513-19515 | 2026 c 19 s 119 | inert (reason 2: machinery) | none | 0 | 0 |
| r149 | 19517-19520 | 2018 c 16 s 190 | encoded | `2018 c 16 s 190 subsection 737(1) is replaced by the following` | 3 | 0 |
| r150 | 19521-19522 | s 737(1) (not in force) | encoded | `s 737(1) (not in force) the offender shall pay a victim surcharge for each offence` | 5 | 1 |
| r151 | 19524-19525 | 2018 c 21 s 51(1) | inert (reason 2: machinery) | none | 0 | 0 |
| r152 | 19526-19526 | 2018 c 21 s 51(2) | inert (reason 2: machinery) | none | 0 | 0 |
| r153 | 19528-19529 | 2018 c 29 s 79(1) | inert (reason 2: machinery) | none | 0 | 0 |
| r154 | 19530-19530 | 2018 c 29 s 79(2) | inert (reason 2: machinery) | none | 0 | 0 |
| r155 | 19532-19533 | 2018 c 29 s 80(1) | inert (reason 2: machinery) | none | 0 | 0 |
| r156 | 19534-19534 | 2018 c 29 s 80(2) | inert (reason 2: machinery) | none | 0 | 0 |
| r157 | 19536-19537 | 2021 c 2 s 1(2.1) | encoded | `2021 c 2 s 1(2.1) subsection 241.2(2.1) is repealed` | 2 | 0 |
| r158 | 19539-19540 | 2023 c 28 s 35 | encoded | `s 743.2 (not in force) the court shall forward the item to the Correctional Service of Canada`; `s 743.2 (not in force) the court must forward the reasons, reports, information and victim contact details to the Correctional Service of Canada` | 7 | 0 |
| r159 | 19541-19542 | s 743.2 (not in force) | encoded | `s 743.2 (not in force) the court shall forward the item to the Correctional Service of Canada`; `s 743.2 (not in force) the court must forward the reasons, reports, information and victim contact details to the Correctional Service of Canada` | 7 | 0 |
| r160 | 19544-19545 | 2024 c 33 s 2 | encoded | `s 679(7) (not in force) section 679 applies to the release or detention of the person as though the person were an appellant in an appeal described in paragraph (1)(a)` | 5 | 1 |
| r161 | 19546-19547 | s 679(7) as replaced by 2024 c 33 s 2 (not in force) | encoded | `s 679(7) (not in force) section 679 applies to the release or detention of the person as though the person were an appellant in an appeal described in paragraph (1)(a)` | 5 | 1 |
| r162 | 19549-19550 | 2024 c 33 s 3 | encoded | `2024 c 33 s 3 Part XXI.1 is replaced by the following` | 2 | 0 |
| r163 | 19552-19556 | s 696.1 (not in force) | encoded | `s 696.1 (not in force) the definitions apply in the provision` | 2 | 0 |
| r164 | 19557-19557 | s 696.1 "applicant, in relation to a miscarriage of justice review application," (not in force) | encoded | `s 696.1 "applicant" (not in force)` | 2 | 0 |
| r165 | 19558-19558 | s 696.1 "Commission" (not in force) | encoded | `s 696.1 "Commission" (not in force)` | 2 | 0 |
| r166 | 19559-19559 | s 696.1 "court of appeal" (not in force) | encoded | `s 696.1 "court of appeal" (not in force)` | 4 | 0 |
| r167 | 19561-19563 | s 696.2(1) (not in force) | fork (F7) | `s 696.2(1) (not in force) an application for a review on the grounds of miscarriage of justice may be made to the Commission by or on behalf of the person` | 8 | 1 |
| r168 | 19564-19564 | s 696.2(1)(a) (not in force) | fork (F7) | `s 696.2(1) (not in force) an application for a review on the grounds of miscarriage of justice may be made to the Commission by or on behalf of the person` | 8 | 1 |
| r169 | 19565-19565 | s 696.2(1)(b) (not in force) | fork (F7) | `s 696.2(1) (not in force) an application for a review on the grounds of miscarriage of justice may be made to the Commission by or on behalf of the person` | 8 | 1 |
| r170 | 19566-19566 | s 696.2(1)(c) (not in force) | fork (F7) | `s 696.2(1) (not in force) an application for a review on the grounds of miscarriage of justice may be made to the Commission by or on behalf of the person` | 8 | 1 |
| r171 | 19567-19568 | s 696.2(2) (not in force) | fork (F8) | `s 696.2(2) (not in force) the application includes what it must include` | 4 | 1 |
| r172 | 19570-19572 | s 696.3(1) (not in force) | encoded | `s 696.3(1) (not in force) the Commission must deal with the application as expeditiously as possible`; `s 696.3(1) (not in force) the Commission must provide the applicant with an update on a regular basis`; `s 696.3(1) (not in force) the Commission owes the applicant the duty to deal with the application as expeditiously as possible and to provide regular updates` | 4 | 1 |
| r173 | 19573-19574 | s 696.3(2) (not in force) | encoded | `s 696.3(2) (not in force) the notice or information may be provided to a representative of the applicant in addition to or instead of the applicant` | 3 | 1 |
| r174 | 19575-19576 | s 696.4(1) (not in force) | encoded | `s 696.4(1) (not in force) the Commission must decide whether the application is admissible`; `s 696.4(1) (not in force) the Commission owes the duty to decide whether the application is admissible` | 3 | 0 |
| r175 | 19577-19578 | s 696.4(2) (not in force) | encoded | `s 696.4(2) (not in force) the Commission must dismiss the application as inadmissible on the ground that the person is not described in subsection 696.2(1)` | 7 | 1 |
| r176 | 19579-19580 | s 696.4(3) (not in force) | encoded | `s 696.4(3) (not in force) the Commission must dismiss the application as inadmissible on a ground in subsection (3)` | 4 | 1 |
| r177 | 19581-19581 | s 696.4(3)(a) (not in force) | encoded | `s 696.4(3) (not in force) the Commission must dismiss the application as inadmissible on a ground in subsection (3)` | 4 | 1 |
| r178 | 19582-19582 | s 696.4(3)(b) (not in force) | encoded | `s 696.4(3) (not in force) the Commission must dismiss the application as inadmissible on a ground in subsection (3)` | 4 | 1 |
| r179 | 19583-19584 | s 696.4(4) (not in force) | encoded | `s 696.4(4) (not in force) the Commission may decide that the application is admissible despite subsection (3)` | 2 | 1 |
| r180 | 19585-19585 | s 696.4(4)(a) (not in force) | encoded | `s 696.4(4) (not in force) the Commission must take the factor into account` | 6 | 1 |
| r181 | 19586-19586 | s 696.4(4)(b) (not in force) | encoded | `s 696.4(4) (not in force) the Commission must take the factor into account` | 6 | 1 |
| r182 | 19587-19587 | s 696.4(4)(c) (not in force) | encoded | `s 696.4(4) (not in force) the Commission must take the factor into account` | 6 | 1 |
| r183 | 19588-19588 | s 696.4(4)(d) (not in force) | fork (F15) | `s 696.4(4) (not in force) the Commission must take the factor into account`; `s 696.4(4)(d) (not in force) the application is supported by a new matter of significance that meets subparagraphs (i) to (iii)` | 11 | 2 |
| r184 | 19589-19589 | s 696.4(4)(d)(i) (not in force) | fork (F15) | `s 696.4(4) (not in force) the Commission must take the factor into account`; `s 696.4(4)(d) (not in force) the application is supported by a new matter of significance that meets subparagraphs (i) to (iii)` | 11 | 2 |
| r185 | 19590-19590 | s 696.4(4)(d)(ii) (not in force) | fork (F15) | `s 696.4(4) (not in force) the Commission must take the factor into account`; `s 696.4(4)(d) (not in force) the application is supported by a new matter of significance that meets subparagraphs (i) to (iii)` | 11 | 2 |
| r186 | 19591-19591 | s 696.4(4)(d)(iii) (not in force) | fork (F15) | `s 696.4(4) (not in force) the Commission must take the factor into account`; `s 696.4(4)(d) (not in force) the application is supported by a new matter of significance that meets subparagraphs (i) to (iii)` | 11 | 2 |
| r187 | 19592-19592 | s 696.4(4)(e) (not in force) | encoded | `s 696.4(4) (not in force) the Commission must take the factor into account` | 6 | 1 |
| r188 | 19593-19594 | s 696.4(5) (not in force) | encoded | `s 696.4(5) (not in force) the Commission must notify the applicant and the relevant Attorney General of its decision on admissibility`; `s 696.4(5) (not in force) the Commission owes the duty to notify the applicant and the relevant Attorney General of its decision on admissibility` | 3 | 1 |
| r189 | 19595-19596 | s 696.5(1) (not in force) | fork (F24) | `s 696.5(1) (not in force) the Commission may conduct an investigation in relation to the application` | 4 | 1 |
| r190 | 19597-19598 | s 696.5(2) (not in force) | encoded | `s 696.5(2) (not in force) the Commission must send a notice indicating whether an investigation will be conducted`; `s 696.5(2) (not in force) the Commission owes the duty to send a notice indicating whether an investigation will be conducted`; `s 696.5(2) (not in force) the notice must also specify a reasonable period within which further information may be provided` | 5 | 2 |
| r191 | 19599-19600 | s 696.5(3) (not in force) | encoded | `s 696.5(3) (not in force) the condition for deciding under section 696.6 without an investigation is met` | 2 | 1 |
| r192 | 19601-19602 | s 696.5(4) (not in force) | encoded | `s 696.5(4) (not in force) the Commission has the powers of a commissioner under Part I of the Inquiries Act` | 2 | 1 |
| r193 | 19603-19604 | s 696.5(5) (not in force) | encoded | `s 696.5(5) (not in force) the Commission may authorize the person to exercise the powers referred to in subsection (4)` | 3 | 0 |
| r194 | 19605-19606 | s 696.5(6) (not in force) | encoded | `s 696.5(6) (not in force) the Commission must prepare a report and provide a copy of it`; `s 696.5(6) (not in force) the Commission owes the duty to prepare a report and provide a copy of it` | 3 | 1 |
| r195 | 19607-19608 | s 696.5(7) (not in force) | encoded | `s 696.5(7) (not in force) the report must specify a reasonable period within which a written response may be provided` | 2 | 1 |
| r196 | 19609-19610 | s 696.5(8) (not in force) | encoded | `s 696.5(8) (not in force) the condition for deciding under section 696.6 after an investigation is met` | 4 | 1 |
| r197 | 19611-19612 | s 696.6(1) (not in force) | encoded | `s 696.6(1) (not in force) the Commission must make a decision on the application`; `s 696.6(1) (not in force) the Commission owes the duty to make a decision on the application` | 3 | 0 |
| r198 | 19613-19614 | s 696.6(2) (not in force) | encoded | `s 696.6(2) (not in force) the Commission must grant a remedy under paragraph (a) or (b)` | 4 | 1 |
| r199 | 19615-19615 | s 696.6(2)(a) (not in force) | fork (F9) | `s 696.6(2) (not in force) the Commission must grant a remedy under paragraph (a) or (b)`; `s 696.6(2)(a) (not in force) the form of the new proceeding the Commission directs` | 6 | 2 |
| r200 | 19616-19616 | s 696.6(2)(b) (not in force) | encoded | `s 696.6(2) (not in force) the Commission must grant a remedy under paragraph (a) or (b)` | 4 | 1 |
| r201 | 19617-19618 | s 696.6(3) (not in force) | encoded | `s 696.6(3) (not in force) the Commission must dismiss the application` | 2 | 1 |
| r202 | 19619-19620 | s 696.6(4) (not in force) | encoded | `s 696.6(4) (not in force) the Commission may take the step` | 4 | 1 |
| r203 | 19621-19622 | s 696.6(5) (not in force) | encoded | `s 696.6(5) (not in force) the Commission must take the factor into account` | 7 | 1 |
| r204 | 19623-19623 | s 696.6(5)(a) (not in force) | encoded | `s 696.6(5) (not in force) the Commission must take the factor into account` | 7 | 1 |
| r205 | 19624-19624 | s 696.6(5)(b) (not in force) | encoded | `s 696.6(5) (not in force) the Commission must take the factor into account` | 7 | 1 |
| r206 | 19625-19625 | s 696.6(5)(c) (not in force) | encoded | `s 696.6(5) (not in force) the Commission must take the factor into account` | 7 | 1 |
| r207 | 19626-19626 | s 696.6(5)(d) (not in force) | encoded | `s 696.6(5) (not in force) the Commission must take the factor into account` | 7 | 1 |
| r208 | 19627-19627 | s 696.6(5)(e) (not in force) | encoded | `s 696.6(5) (not in force) the Commission must take the factor into account` | 7 | 1 |
| r209 | 19628-19628 | s 696.6(5)(f) (not in force) | encoded | `s 696.6(5) (not in force) the Commission must take the factor into account` | 7 | 1 |
| r210 | 19629-19630 | s 696.6(6) (not in force) | encoded | `s 696.6(6) (not in force) the Commission may grant a remedy under subsection (2) even if the evidence does not establish the innocence of the applicant` | 2 | 1 |
| r211 | 19631-19632 | s 696.6(7) (not in force) | encoded | `s 696.6(7) (not in force) the Commission must notify the applicant and the relevant Attorney General of its decision`; `s 696.6(7) (not in force) the Commission owes the duty to notify the applicant and the relevant Attorney General of its decision` | 3 | 1 |
| r212 | 19634-19636 | s 696.61 (not in force) | encoded | `s 696.61 (not in force) the Commission may refer the question to the court of appeal for its opinion`; `s 696.61 (not in force) the court of appeal must provide its opinion`; `s 696.61 (not in force) the court of appeal must provide its opinion on the question` | 6 | 1 |
| r213 | 19638-19640 | s 696.62 (not in force) | inert (reason 2: machinery) | none | 0 | 0 |
| r214 | 19642-19643 | 2024 c 33 s 5 | encoded | `s 696.7 "applicant" (not in force)` | 2 | 0 |
| r215 | 19644-19644 | s 696.7 "applicant" as replaced by 2024 c 33 s 5 (not in force) | encoded | `s 696.7 "applicant" (not in force)` | 2 | 0 |
| r216 | 19646-19647 | 2024 c 33 s 6 | encoded | `s 696.72 (not in force) the application is within the Commission’s mandate` | 3 | 1 |
| r217 | 19648-19649 | s 696.72 (not in force) | encoded | `s 696.72 (not in force) the application is within the Commission’s mandate` | 3 | 1 |
| r218 | 19651-19653 | 2024 c 33 s 7 | encoded | `2024 c 33 s 7 the definitions apply in the section` | 5 | 0 |
| r219 | 19654-19654 | 2024 c 33 s 7 "applicant" | encoded | `2024 c 33 s 7 "applicant"` | 2 | 0 |
| r220 | 19655-19655 | 2024 c 33 s 7 "commencement day" | encoded | `2024 c 33 s 7 "commencement day"` | 1 | 0 |
| r221 | 19656-19656 | 2024 c 33 s 7 "Commission" | encoded | `2024 c 33 s 7 "Commission"` | 2 | 0 |
| r222 | 19657-19657 | 2024 c 33 s 7 "Minister" | encoded | `2024 c 33 s 7 "Minister"` | 2 | 0 |
| r223 | 19658-19658 | 2024 c 33 s 7 "new scheme" | encoded | `2024 c 33 s 7 "new scheme"` | 4 | 0 |
| r224 | 19659-19659 | 2024 c 33 s 7 "old scheme" | fork (F10) | `2024 c 33 s 7 "old scheme"` | 5 | 0 |
| r225 | 19661-19663 | 2024 c 33 s 8 | encoded | `2024 c 33 s 8 the Minister must ask the applicant whether they consent to the transfer`; `2024 c 33 s 8 the Minister owes the duty to ask the applicant whether they consent to the transfer` | 4 | 1 |
| r226 | 19665-19667 | 2024 c 33 s 9 | fork (F21) | `2024 c 33 s 9 the application is deemed to have been made to the Commission under the new scheme`; `2024 c 33 s 9 the Minister is authorized to disclose to the Commission all information pertaining to the application that is under the Minister’s control` | 8 | 2 |
| r227 | 19669-19671 | 2024 c 33 s 10(1) | encoded | `2024 c 33 s 10(1) subsection (2) or (3) applies` | 4 | 1 |
| r228 | 19672-19673 | 2024 c 33 s 10(2) | encoded | `2024 c 33 s 10(2) the old scheme continues to apply in respect of the application` | 4 | 1 |
| r229 | 19674-19675 | 2024 c 33 s 10(3) | fork (F23) | `2024 c 33 s 10(3) the application is deemed not to have been made`; `2024 c 33 s 10(3) the applicant may apply to the Commission under the new scheme` | 6 | 2 |
| r230 | 19677-19679 | 2024 c 33 s 11 | fork (F22) | `2024 c 33 s 11 the application is deemed to have been made to the Commission under the new scheme`; `2024 c 33 s 11 the Minister is authorized to disclose to the Commission all information pertaining to the application that is under the Minister’s control` | 10 | 2 |
| r231 | 19680-19680 | 2024 c 33 s 11(a) | fork (F22) | `2024 c 33 s 11 the application is deemed to have been made to the Commission under the new scheme`; `2024 c 33 s 11 the Minister is authorized to disclose to the Commission all information pertaining to the application that is under the Minister’s control` | 10 | 2 |
| r232 | 19681-19681 | 2024 c 33 s 11(b) | fork (F22) | `2024 c 33 s 11 the application is deemed to have been made to the Commission under the new scheme`; `2024 c 33 s 11 the Minister is authorized to disclose to the Commission all information pertaining to the application that is under the Minister’s control` | 10 | 2 |
| r233 | 19682-19682 | 2024 c 33 s 11(c) | fork (F22) | `2024 c 33 s 11 the application is deemed to have been made to the Commission under the new scheme`; `2024 c 33 s 11 the Minister is authorized to disclose to the Commission all information pertaining to the application that is under the Minister’s control` | 10 | 2 |
| r234 | 19684-19686 | 2024 c 33 s 12 | encoded | `2024 c 33 s 12 the consent may be revoked` | 2 | 1 |
| r235 | 19688-19690 | 2024 c 33 s 13 | encoded | `2024 c 33 s 13 the fact that the Minister dismissed the application under the old scheme prevents the applicant from applying under the new scheme` | 2 | 1 |
| r236 | 19692-19693 | 2026 c 16 s 48 | inert (reason 2: machinery) | none | 0 | 0 |
| r237 | 19694-19695 | s 490.02(3) as replaced by 2026 c 16 s 48 (not in force) | encoded | `s 490.02(3) (not in force) the day before which the provision referred to is read` | 4 | 0 |
| r238 | 19697-19698 | 2026 c 16 s 49 | inert (reason 2: machinery) | none | 0 | 0 |
| r239 | 19699-19700 | s 490.022(4) as replaced by 2026 c 16 s 49 (not in force) | encoded | `s 490.022(4) (not in force) the day before which the definition referred to is read` | 3 | 0 |
| r240 | 19702-19703 | 2026 c 16 s 50(1) (amending: paragraphs 490.04(1)(a) and (b) replaced) | inert (reason 2: machinery) | none | 0 | 0 |
| r241 | 19704-19704 | s 490.04(1)(a) (not in force) | encoded | `s 490.04(1) (not in force) the order or obligation is one listed in paragraph (a), (a.1) or (b)` | 13 | 1 |
| r242 | 19705-19705 | s 490.04(1)(a.1) (not in force) | encoded | `s 490.04(1) (not in force) the order or obligation is one listed in paragraph (a), (a.1) or (b)` | 13 | 1 |
| r243 | 19706-19706 | s 490.04(1)(b) (not in force) | encoded | `s 490.04(1) (not in force) the order or obligation is one listed in paragraph (a), (a.1) or (b)` | 13 | 1 |
| r244 | 19707-19707 | 2026 c 16 s 50(2) (amending: subsection 490.04(2) replaced) | inert (reason 2: machinery) | none | 0 | 0 |
| r245 | 19708-19709 | s 490.04(2) (not in force) | encoded | `s 490.04(2) (not in force) the person is permitted to apply under paragraph (1)(b)` | 3 | 1 |
| r246 | 19710-19710 | 2026 c 16 s 50(3) (amending: paragraph 490.04(3)(a) replaced) | inert (reason 2: machinery) | none | 0 | 0 |
| r247 | 19711-19711 | s 490.04(3)(a) (not in force) | encoded | `s 490.04(3)(a) (not in force) a superior court of criminal jurisdiction is a court that may receive the application` | 4 | 1 |
| r248 | 19712-19712 | s 490.04(3)(a)(i) (not in force) | encoded | `s 490.04(3)(a) (not in force) a superior court of criminal jurisdiction is a court that may receive the application` | 4 | 1 |
| r249 | 19713-19713 | s 490.04(3)(a)(ii) (not in force) | encoded | `s 490.04(3)(a) (not in force) a superior court of criminal jurisdiction is a court that may receive the application` | 4 | 1 |
| r250 | 19714-19714 | 2026 c 16 s 50(4) (amending: the opening of subsection 490.04(4) replaced) | inert (reason 2: machinery) | none | 0 | 0 |
| r251 | 19715-19716 | s 490.04(4) lead-in (not in force) | encoded | `s 490.04(4) (not in force) the court may make an exemption order` | 12 | 1 |
| r252 | 19717-19717 | s 490.04(4)(a) (not in force) | encoded | `s 490.04(4) (not in force) the court may make an exemption order` | 12 | 1 |
| r253 | 19718-19718 | s 490.04(4)(a.1) (not in force) | encoded | `s 490.04(4) (not in force) the court may make an exemption order` | 12 | 1 |
| r254 | 19719-19719 | s 490.04(4)(b) (not in force) | encoded | `s 490.04(4) (not in force) the court may make an exemption order` | 12 | 1 |
| r255 | 19720-19720 | 2026 c 16 s 50(5) (amending: subsection 490.04(8) replaced) | inert (reason 2: machinery) | none | 0 | 0 |
| r256 | 19721-19722 | s 490.04(8) (not in force) | encoded | `s 490.04(8) (not in force) the court shall also make an order requiring the Royal Canadian Mounted Police to permanently remove the information from the database` | 6 | 1 |
| r257 | 19724-19725 | 2026 c 16 s 51(1) (amending: paragraph 490.05(1)(a) replaced) | inert (reason 2: machinery) | none | 0 | 0 |
| r258 | 19726-19726 | s 490.05(1)(a) (not in force) | encoded | `s 490.05(1) (not in force) the order or obligation is one listed in the replaced paragraphs` | 16 | 1 |
| r259 | 19727-19727 | s 490.05(1)(a.1) (not in force) | encoded | `s 490.05(1) (not in force) the order or obligation is one listed in the replaced paragraphs` | 16 | 1 |
| r260 | 19728-19728 | 2026 c 16 s 51(2) (amending: paragraphs 490.05(1)(c) and (d) replaced) | inert (reason 2: machinery) | none | 0 | 0 |
| r261 | 19729-19729 | s 490.05(1)(b.1) (not in force) | encoded | `s 490.05(1) (not in force) the order or obligation is one listed in the replaced paragraphs` | 16 | 1 |
| r262 | 19730-19730 | s 490.05(1)(c) (not in force) | encoded | `s 490.05(1) (not in force) the order or obligation is one listed in the replaced paragraphs` | 16 | 1 |
| r263 | 19731-19731 | s 490.05(1)(d) (not in force) | encoded | `s 490.05(1) (not in force) the order or obligation is one listed in the replaced paragraphs` | 16 | 1 |
| r264 | 19732-19732 | 2026 c 16 s 51(3) (amending: paragraph 490.05(3)(a) replaced) | inert (reason 2: machinery) | none | 0 | 0 |
| r265 | 19733-19733 | s 490.05(3)(a) (not in force) | encoded | `s 490.05(3)(a) (not in force) a superior court of criminal jurisdiction is a court that may receive the application` | 4 | 1 |
| r266 | 19734-19734 | s 490.05(3)(a)(i) (not in force) | encoded | `s 490.05(3)(a) (not in force) a superior court of criminal jurisdiction is a court that may receive the application` | 4 | 1 |
| r267 | 19735-19735 | s 490.05(3)(a)(ii) (not in force) | encoded | `s 490.05(3)(a) (not in force) a superior court of criminal jurisdiction is a court that may receive the application` | 4 | 1 |
| r268 | 19736-19736 | 2026 c 16 s 51(4) (amending: paragraph 490.05(5)(a.1) added) | inert (reason 2: machinery) | none | 0 | 0 |
| r269 | 19737-19737 | s 490.05(5)(a.1) (not in force) | encoded | `s 490.05(5) (not in force) the provision applied to the offence in question with the longest maximum term of imprisonment` | 3 | 0 |
| r270 | 19738-19738 | 2026 c 16 s 51(5) (amending: paragraph 490.05(5)(b.1) added) | inert (reason 2: machinery) | none | 0 | 0 |
| r271 | 19739-19739 | s 490.05(5)(b.1) (not in force) | encoded | `s 490.05(5) (not in force) the provision applied to the offence in question with the longest maximum term of imprisonment` | 3 | 0 |
| r272 | 19741-19742 | 2026 c 16 s 52 | inert (reason 2: machinery) | none | 0 | 0 |
| r273 | 19743-19744 | s 490.06(2) as replaced by 2026 c 16 s 52 (not in force) | encoded | `s 490.06(2) (not in force) the appeal court shall also make an order requiring the Royal Canadian Mounted Police to permanently remove the information from the database` | 6 | 1 |
| r274 | 19746-19747 | 2026 c 16 s 53 | inert (reason 2: machinery) | none | 0 | 0 |
| r275 | 19749-19750 | 2026 c 19 s 2(2) | encoded | `s 3.01(1)(b.1) (not in force) the offence counts as one in which violence is used, threatened or attempted` | 2 | 1 |
| r276 | 19751-19751 | s 3.01(1)(b.1) as added by 2026 c 19 s 2(2) (not in force) | encoded | `s 3.01(1)(b.1) (not in force) the offence counts as one in which violence is used, threatened or attempted` | 2 | 1 |
| r277 | 19753-19754 | 2026 c 19 s 4 | encoded | `s 109(1)(b) (not in force) the offence is one listed in paragraph (b)` | 16 | 1 |
| r278 | 19755-19755 | s 109(1)(b) as replaced by 2026 c 19 s 4 (not in force) | encoded | `s 109(1)(b) (not in force) the offence is one listed in paragraph (b)` | 16 | 1 |
| r279 | 19757-19758 | 2026 c 19 s 24(5) | encoded | `s 183 "offence" (a)(xxxix.4) (not in force) the offence is within paragraph (a) of the definition` | 2 | 1 |
| r280 | 19759-19759 | s 183 "offence" (a)(xxxix.4) as added by 2026 c 19 s 24(5) (not in force) | encoded | `s 183 "offence" (a)(xxxix.4) (not in force) the offence is within paragraph (a) of the definition` | 2 | 1 |
| r281 | 19761-19762 | 2026 c 19 s 28 | encoded | `s 264.01(1) (not in force) the accused commits an offence` | 8 | 1 |
| r282 | 19763-19764 | s 264.01(1) (not in force) | fork (F11) | `s 264.01(1) (not in force) the accused commits an offence` | 8 | 1 |
| r283 | 19765-19766 | s 264.01(2) (not in force) | fork (F6) | `s 264.01(2) (not in force) the acts make up a pattern of coercive or controlling conduct` | 7 | 1 |
| r284 | 19767-19767 | s 264.01(2)(a) (not in force) | encoded | `s 264.01(2)(a) (not in force) the act is within paragraph (a)` | 6 | 1 |
| r285 | 19768-19768 | s 264.01(2)(a)(i) (not in force) | encoded | `s 264.01(2)(a) (not in force) the act is within paragraph (a)` | 6 | 1 |
| r286 | 19769-19769 | s 264.01(2)(a)(ii) (not in force) | encoded | `s 264.01(2)(a) (not in force) the act is within paragraph (a)` | 6 | 1 |
| r287 | 19770-19770 | s 264.01(2)(a)(iii) (not in force) | encoded | `s 264.01(2)(a) (not in force) the act is within paragraph (a)` | 6 | 1 |
| r288 | 19771-19771 | s 264.01(2)(a)(iv) (not in force) | encoded | `s 264.01(2)(a) (not in force) the act is within paragraph (a)` | 6 | 1 |
| r289 | 19772-19772 | s 264.01(2)(b) (not in force) | encoded | `s 264.01(2)(b) (not in force) the act is within paragraph (b)` | 2 | 1 |
| r290 | 19773-19773 | s 264.01(2)(c) (not in force) | encoded | `s 264.01(2)(c) (not in force) the conduct is within paragraph (c)` | 2 | 1 |
| r291 | 19774-19774 | s 264.01(2)(c)(i) (not in force) | encoded | `s 264.01(2)(c) (not in force) the conduct is within paragraph (c)`; `s 264.01(2)(c) (not in force) the conduct is listed in one of the subparagraphs` | 11 | 2 |
| r292 | 19775-19775 | s 264.01(2)(c)(ii) (not in force) | encoded | `s 264.01(2)(c) (not in force) the conduct is within paragraph (c)`; `s 264.01(2)(c) (not in force) the conduct is listed in one of the subparagraphs` | 11 | 2 |
| r293 | 19776-19776 | s 264.01(2)(c)(iii) (not in force) | encoded | `s 264.01(2)(c) (not in force) the conduct is within paragraph (c)`; `s 264.01(2)(c) (not in force) the conduct is listed in one of the subparagraphs` | 11 | 2 |
| r294 | 19777-19777 | s 264.01(2)(c)(iv) (not in force) | encoded | `s 264.01(2)(c) (not in force) the conduct is within paragraph (c)`; `s 264.01(2)(c) (not in force) the conduct is listed in one of the subparagraphs` | 11 | 2 |
| r295 | 19778-19778 | s 264.01(2)(c)(v) (not in force) | encoded | `s 264.01(2)(c) (not in force) the conduct is within paragraph (c)`; `s 264.01(2)(c) (not in force) the conduct is listed in one of the subparagraphs` | 11 | 2 |
| r296 | 19779-19779 | s 264.01(2)(c)(vi) (not in force) | encoded | `s 264.01(2)(c) (not in force) the conduct is within paragraph (c)`; `s 264.01(2)(c) (not in force) the conduct is listed in one of the subparagraphs` | 11 | 2 |
| r297 | 19780-19780 | s 264.01(2)(c)(vii) (not in force) | encoded | `s 264.01(2)(c) (not in force) the conduct is within paragraph (c)`; `s 264.01(2)(c) (not in force) the conduct is listed in one of the subparagraphs` | 11 | 2 |
| r298 | 19781-19781 | s 264.01(2)(c)(viii) (not in force) | encoded | `s 264.01(2)(c) (not in force) the conduct is within paragraph (c)`; `s 264.01(2)(c) (not in force) the conduct is listed in one of the subparagraphs` | 11 | 2 |
| r299 | 19782-19783 | s 264.01(3) (not in force) | encoded | `s 264.01(3) (not in force) the circumstances referred to in paragraph (2)(c) include the circumstance` | 4 | 1 |
| r300 | 19784-19785 | s 264.01(4) (not in force) | encoded | `s 264.01(4) (not in force) the class of the offence`; `s 264.01(4) (not in force) the punishment for the offence` | 6 | 2 |
| r301 | 19786-19786 | s 264.01(4)(a) (not in force) | encoded | `s 264.01(4) (not in force) the class of the offence`; `s 264.01(4) (not in force) the punishment for the offence` | 6 | 2 |
| r302 | 19787-19787 | s 264.01(4)(b) (not in force) | encoded | `s 264.01(4) (not in force) the class of the offence`; `s 264.01(4) (not in force) the punishment for the offence` | 6 | 2 |
| r303 | 19788-19789 | s 264.01(5) (not in force) | encoded | `s 264.01(5) (not in force) a person’s safety includes the kind of safety` | 2 | 1 |
| r304 | 19791-19792 | 2026 c 19 s 42 | encoded | `s 487.04 "secondary designated offence" (c)(v.1) (not in force) the offence is within paragraph (c) of the definition` | 2 | 1 |
| r305 | 19793-19793 | s 487.04 "secondary designated offence" (c)(v.1) as added by 2026 c 19 s 42 (not in force) | encoded | `s 487.04 "secondary designated offence" (c)(v.1) (not in force) the offence is within paragraph (c) of the definition` | 2 | 1 |
| r306 | 19795-19796 | 2026 c 19 s 45(2) | encoded | `s 490.011(1) "secondary offence" (a)(ix.1) (not in force) the offence is within paragraph (a) of the definition` | 2 | 1 |
| r307 | 19797-19797 | s 490.011(1) "secondary offence" (a)(ix.1) as added by 2026 c 19 s 45(2) (not in force) | encoded | `s 490.011(1) "secondary offence" (a)(ix.1) (not in force) the offence is within paragraph (a) of the definition` | 2 | 1 |

## Fork register (ccc32)

Each entry gives the provision, the reading taken, the other reading, and the text that licenses each.
The ruling of 2026-11-05, "questions with no convention: decide case by case", governs the choices below that are not covered by another ruling: each is one line for the human reviewer to overrule.
The rows that rest on an entry carry its id in the `disposition` column of the coverage table.
The rulings of 2026-11-04 and 2026-11-05 that the `NOTHING-kind` and `FALSE-kind` tags of these entries rest on (E1, N2, periods, delegated definitions, case by case) are carried word for word in the section "Rulings carried word for word (ccc32)" below, which says how each applies in this range.

### F1. the end of two years after the day, then within 180 days

- **Provision:** 2011 c 2 s 7(2), (3).
- **Rows:** r020-r021.
- **Reading taken:** The window opens the day after the anniversary (two years after the determination, or the day the set time ends) and closes on the 180th day after it: on the anniversary itself the answer is JUST FALSE, on the 180th day after it JUST TRUE, on the 181st JUST FALSE (ruling 2026-11-05 (a): a period fixed in the text's own words).
- **Other reading:** The two years end at the close of the day before the anniversary, so the window opens on the anniversary and closes 180 days after the day before it: the same window shifted by one day.
- **Licence:** "within 180 days after the end of two years after the day on which the person is the subject of the determination or conclusion" (line 19099); "within 180 days after the end of that time" (line 19101).

### F2. month and year arithmetic at the end of a month

- **Provision:** 1991 c 43 s 10(2) (twelve months), 2011 c 2 s 7(2) (two years), 2019 c 25 s 360 (six months).
- **Rows:** r002, r020, r069.
- **Reading taken:** daydate's `add months` and `add years` are used as they are: they clamp to the last day of a shorter month (31 August 2019 plus six months is 29 February 2020; 29 February 2020 plus two years is 28 February 2022). The tests assert this.
- **Other reading:** A period that ends in a month with no such day rolls forward to the first of the next month; or the period ends on the last day of the month, whichever the lawyer prefers.
- **Licence:** The text says "within twelve months after" (line 19060), "two years" (line 19099) and "six months after" (line 19085) and does not say how a month end is counted. This is a finding about the arithmetic of the library, not about the Code.

### F3. "is deemed, on and after that day, to be bound"

- **Provision:** 2019 c 25 ss 354 to 358; 2026 c 19 s 111(1).
- **Rows:** r063-r067, r138.
- **Reading taken:** Asked as of a day before the stated day, the answer is JUST FALSE (a period fixed in the text's own words: ruling 2026-11-05 (a)); asked on or after it, JUST TRUE when the person was bound or the measure was used under the old provision; where the old provision is not one the section lists, NOTHING.
- **Other reading:** Asked as of a day before the stated day, the answer is NOTHING: "on and after that day" is a scope limit with no "only" (ruling 2026-11-05 (c)).
- **Licence:** "is deemed, on and after that day, to be bound by an appearance notice" (line 19246); "is deemed, on or after the commencement day, to be an alternative measure" (line 19477).

### F4. the right to re-elect and its time limit

- **Provision:** 2019 c 25 s 359.
- **Rows:** r068.
- **Reading taken:** A person within the section who has not already elected may elect another mode of trial: JUST TRUE up to 14 days before the first day appointed for trial, and after that only with the prosecutor's written consent; after the 14 days and without consent JUST FALSE (a period fixed in the text's own words: ruling 2026-11-05 (a); listed in the name-test sweep, below); a person not accused before the day, or not in one of the cases of section 561, NOTHING (the cases of section 561 are a seam input). A person who has already elected is NOTHING, not JUST FALSE: see F25.
- **Other reading:** After the 14 days and without consent the answer is NOTHING, because the grant is limited by its own wording and the 14 days are a limit on the grant, not a bar.
- **Licence:** "not later than 14 days before the day first appointed for the trial and they may do so after that time with the written consent of the prosecutor" (line 19266).

### F5. "subject to sections 77 and 78"

- **Provision:** 2022 c 17 s 76.
- **Rows:** r081.
- **Reading taken:** The amendments apply to ongoing proceedings (JUST TRUE) unless section 77 or 78 answers JUST TRUE for the matter, in which case JUST FALSE (the text says "subject to"); where either of them answers NOTHING, NOTHING.
- **Other reading:** Where section 77 or 78 answers JUST TRUE, the answer is NOTHING: the clause "subject to" points at those sections without itself saying no.
- **Licence:** "For greater certainty, but subject to sections 77 and 78, the amendments made by this Act also apply with respect to proceedings that are ongoing on the day on which this Act comes into force." (line 19304).

### F6. the pattern needs at least two acts

- **Provision:** s 264.01(2) (not in force).
- **Rows:** r283.
- **Reading taken:** A pattern of coercive or controlling conduct consists of "any combination, or repeated instances, of any of the following acts": two or more acts in all (a combination of different acts, or repeated instances of one) make a pattern, and fewer than two is JUST FALSE, because "consists of" is read as a definition.
- **Other reading:** A single act is a pattern when it is serious enough; or fewer than two acts is NOTHING (the text does not say a single act is not a pattern).
- **Licence:** "A pattern of coercive or controlling conduct consists of any combination, or repeated instances, of any of the following acts:" (line 19766).

### F7. who may apply, and the list that is not closed

- **Provision:** s 696.2(1) (not in force) and s 696.4(2) (not in force).
- **Rows:** r167-r170.
- **Reading taken:** Section 696.2(1) lists the persons who may apply and is not closed by "only": a person of another kind is NOTHING at section 696.2(1). Section 696.4(2) separately says the Commission must dismiss an application by or for a person not described in 696.2(1): its failed "if" is JUST FALSE for that ground.
- **Other reading:** Section 696.2(1) is read as a closed list, so a person of another kind is JUST FALSE at 696.2(1) itself.
- **Licence:** "An application for a review on the grounds of miscarriage of justice may be made to the Commission by or on behalf of" (line 19563); "must dismiss the application as inadmissible if it is made by or on behalf of a person who is not described in subsection 696.2(1)" (line 19578).

### F8. a bare "must" not done: the content of an application

- **Provision:** s 696.2(2) (not in force).
- **Rows:** r171.
- **Reading taken:** The application must include information on whether the rights to appeal are exhausted and, if they are not, on the factors in section 696.4(4): when it does not, JUST FALSE for this content requirement (decided case by case, the maintainer 2026-11-05).
- **Other reading:** NOTHING: the text states a content requirement but not what follows when it is not met.
- **Licence:** "For the purposes of subsection 696.4(3), the application must include" (line 19568).

### F9. a new trial, or a new hearing, for a dangerous or long-term offender

- **Provision:** s 696.6(2)(a) (not in force).
- **Rows:** r199.
- **Reading taken:** For an applicant who was found a dangerous offender or long-term offender under Part XXIV, the form of the new proceeding is a new hearing under that Part; for any other applicant, a new trial before any court the Commission thinks proper.
- **Other reading:** The Commission may direct either a new trial or a new hearing for such an applicant (the text names the new hearing "in the case of" them but does not say a new trial is excluded).
- **Licence:** "direct a new trial before any court that the Commission thinks proper or, in the case of an applicant who was found to be a dangerous offender or long-term offender under Part XXIV, a new hearing under that Part" (line 19615).

### F10. "immediately before the commencement day"

- **Provision:** 2024 c 33 s 7 "old scheme" and the sections that use it.
- **Rows:** r224.
- **Reading taken:** The old scheme is Part XXI.1 and the Regulations as they read on the day before the commencement day: `2024 c 33 s 7 "old scheme"` answers JUST TRUE for that text read as of that day and JUST FALSE for the same text read as of any other day, and for any other text (a "means" definition).
- **Other reading:** The text as it reads at the start of the commencement day, before the amendments take effect: the same text, unless an amendment is itself made on that day.
- **Licence:** "old scheme means Part XXI.1 of the Criminal Code and the Regulations Respecting Applications for Ministerial Review -- Miscarriages of Justice as they read immediately before the commencement day" (line 19659).

### F11. "Everyone commits an offence who ..." when an element fails

- **Provision:** s 264.01(1) (not in force).
- **Rows:** r282.
- **Reading taken:** When an element is not established (no pattern, no intent, knowledge or recklessness, no intimate partner), the section neither says yes nor no: NOTHING (a grant or prohibition limited by its own wording).
- **Other reading:** The elements are necessary and sufficient, so when one fails the answer is JUST FALSE.
- **Licence:** "Everyone commits an offence who engages in a pattern of coercive or controlling conduct referred to in subsection (2), with intent ... or knowing that, or being reckless as to whether ..." (line 19764).

### F12. "applies only" to later conduct or charges

- **Provision:** 2009 c 29 s 5; 2015 c 13 ss 40, 42, 42.1, 44; 2026 c 11 s 58(1); 2026 c 19 ss 97, 100, 105, 114, 115, 116.
- **Rows:** r018, r033, r035-r036, r038, r114, r125, r128, r132, r142-r144.
- **Reading taken:** A provision that "applies only" to conduct, a charge or an offence on or after a day: on or after that day JUST TRUE; before it JUST FALSE (the text closes the list with "only").
- **Other reading:** Before the day, NOTHING: "only" describes the amendment's scope, and the text does not say the person is not covered.
- **Licence:** "apply only to persons charged after the day" (line 19093); "applies only in respect of conduct engaged in on or after the day" (line 19139); "apply only with respect to an offence that is committed on or after" (line 19393).

### F13. "applies with respect to any matter or proceeding that is ongoing"

- **Provision:** 2022 c 17 s 76; 2023 c 30 s 3; 2026 c 11 s 58(2), (3); 2026 c 12 s 16; 2026 c 19 ss 99, 101 to 103, 106 to 109, 111(2), 112, 113, 117, 118.
- **Rows:** r102, r115-r116, r118, r127, r129-r131, r133-r136, r139-r141, r145-r146.
- **Reading taken:** A matter ongoing on the day is JUST TRUE; any other matter is NOTHING (a grant limited by its own wording and "for greater certainty": the text is silent on matters that are not ongoing).
- **Other reading:** A matter that is not ongoing is JUST FALSE: the provision applies to ongoing matters, so it does not apply to others.
- **Licence:** "applies with respect to any matter or proceeding that is ongoing on the commencement day" (line 19433) and its variants.

### F14. "continues to apply" to a case begun or made before the day

- **Provision:** 2015 c 13 ss 38, 39, 41, 43; 2018 c 12 s 406(1); 2019 c 13 s 155; 2026 c 19 s 110.
- **Rows:** r031-r032, r034, r037, r044, r059, r137.
- **Reading taken:** A request, statement, application or order made (or an offence alleged) before the day is JUST TRUE; any other case is NOTHING (a grant limited by its own wording).
- **Other reading:** A case made on or after the day is JUST FALSE: the old text continues only for the earlier cases.
- **Licence:** "continues to apply in respect of requests for restitution made to the court under that section 380.3 before that day" (line 19131) and its variants.

### F15. the three limbs of a new matter of significance

- **Provision:** s 696.4(4)(d) (not in force).
- **Rows:** r183-r186.
- **Reading taken:** The three limbs (not considered before, requires investigation, does not raise only a question of law) are conjunctive; when one fails the text neither says yes nor no: NOTHING.
- **Other reading:** When one limb fails the matter is not a new matter of significance within the paragraph: JUST FALSE.
- **Licence:** "(i) was not considered by the courts or previously considered by the Commission ... (ii) requires investigation, and (iii) does not raise only a question of law" (line 19589).

### F16. a flat negative with a date or condition

- **Provision:** 2019 c 13 s 157; 2023 c 26 ss 614, 615; 2023 c 32 s 14.1; 2026 c 12 s 15; 2026 c 19 s 98.
- **Rows:** r061, r097-r100, r103, r117, r126.
- **Reading taken:** When the case is the one the negative describes the answer is JUST FALSE (a flat negative: ruling N2, option A); for any other case NOTHING (the negative is limited by its own wording).
- **Other reading:** For a case the negative does not describe the answer is JUST TRUE, because the provision it limits then applies.
- **Licence:** "does not apply in respect of any receipt of a payment" (line 19340); "Subsection 236(2) ... does not apply with respect to an offence that is committed before ..." (line 19401).

### F17. a period fixed in the text's own words: "on that day or within n days after"

- **Provision:** 2015 c 13 s 37; 2018 c 29 s 74.
- **Rows:** r030, r058.
- **Reading taken:** A hearing within the period is JUST TRUE; outside it JUST FALSE (ruling 2026-11-05 (a)); a hearing that is not of the kind the subsection refers to, NOTHING.
- **Other reading:** Outside the period the answer is NOTHING: the period limits a continued application and the text does not say what governs after it.
- **Licence:** "continues to apply in respect of any hearing referred to in that subsection that takes place on that day or within 14 days after that day" (line 19127).

### F18. a clarification named for the protection it gives

- **Provision:** 2026 c 15 s 11.1(1), (2).
- **Rows:** r119-r120.
- **Reading taken:** The clarification protects a statement on a matter of public interest when the person does not wilfully promote hatred (or antisemitism): JUST TRUE; when the person does, JUST FALSE for this clarification only; the answer says nothing about whether section 319 itself prohibits the statement, which is for section 319.
- **Other reading:** The same facts answer NOTHING (the clarification says what is not prohibited and is silent on the rest).
- **Licence:** "nothing in subsection 319(2) or (2.2) of the Criminal Code shall be construed as prohibiting a person from communicating a statement on a matter of public interest ... if they do not wilfully promote hatred against an identifiable group by communicating the statement" (line 19409).

### F19. reviews and reports by Parliament, committees and Ministers are inert

- **Provision:** 2005 c 32 s 27.1; 2009 c 28 s 12; 2014 c 6 s 20.1; 2014 c 25 s 45.1; 2016 c 3 ss 9.1, 10; 2018 c 21 s 31.1; 2021 c 2 ss 3.1, 5; 2022 c 15 s 21; 2022 c 17 ss 78.1, 78.2; 2023 c 30 s 2; 2023 c 32 s 14.2; 2024 c 1 s 2; 2026 c 19 ss 118.1, 119; s 696.62 (not in force).
- **Rows:** r015-r017, r026-r029, r040-r043, r047-r048, r070-r072, r074-r080, r089-r095, r101, r104-r109, r147-r148, r213.
- **Reading taken:** Inert, reason 2 (machinery): each is a duty on a committee or Minister to review a Part and report to Parliament, and it affects no person under the Code. 40 rows (listed in the coverage table).
- **Other reading:** Each is a rule with a party (the committee or Minister) and a deadline (five years, three years) and is encoded as a regulative rule with its time limit; the seat has no question for it either way. A reviewer who disagrees changes one disposition: every row of this fork moves together, and none of them has a seat question.
- **Licence:** The brief's reason 2 (not a quotation of the Code): boards and offices and their staffing, and savings and transitional provisions that affect no one now.

### F20. 2004 c 12 ss 22 and 23 are encoded, not inert

- **Provision:** 2004 c 12 ss 22, 23.
- **Rows:** r008-r014.
- **Reading taken:** Each "for greater certainty" reading rule (what a reference to a Bill in an old amending Act refers to) is encoded as a reading table that returns the thing referred to as a MAYBE STRING.
- **Other reading:** Inert, reason 2: the references are inside amending Acts that have long since come into force, and affect no one now.
- **Licence:** "For greater certainty, section 82 of An Act to amend the Criminal Code ... is to be read in accordance with the following" (line 19070). The sections are in the Code text a reader finds, so they are encoded.

### F21. 2024 c 33 s 9: the Minister is authorized to disclose (name-test sweep of 2026-11-12)

- **Provision:** `2024 c 33 s 9 the Minister is authorized to disclose to the Commission all information pertaining to the application that is under the Minister's control`.
- **Rows:** r226.
- **Reading taken:** Named for a power: when the "If" gate (written consent within the time limit fixed by the Minister) is not met the answer is NOTHING, because the grant is limited by its own wording (Guide section 5, "In short"). The sibling `... the application is deemed to have been made ...` is not a power and keeps JUST FALSE.
- **Other reading:** JUST FALSE: a failed "if" read as the text's own no.
- **Licence:** "If the applicant gives, within the time limit fixed by the Minister, written consent to transfer the application" (line 19667).

### F22. 2024 c 33 s 11: the Minister is authorized to disclose (name-test sweep of 2026-11-12)

- **Provision:** `2024 c 33 s 11 the Minister is authorized to disclose to the Commission all information pertaining to the application that is under the Minister's control`.
- **Rows:** r230-r233.
- **Reading taken:** Named for a power: when any of the three conditions (a) to (c) fails the answer is NOTHING. The sibling `... deemed to have been made ...` keeps JUST FALSE.
- **Other reading:** JUST FALSE: a failed "if" read as the text's own no.
- **Licence:** "An application is deemed to have been made to the Commission under the new scheme and the Minister is authorized to disclose to the Commission all information pertaining to the application that is under the Minister's control if" (line 19679).

### F23. 2024 c 33 s 10(3): the applicant may apply to the Commission (name-test sweep of 2026-11-12)

- **Provision:** `2024 c 33 s 10(3) the applicant may apply to the Commission under the new scheme`.
- **Rows:** r229.
- **Reading taken:** Named for a power: when the Minister did complete the preliminary assessment before the commencement day the answer is NOTHING, not JUST FALSE.
- **Other reading:** JUST FALSE: a failed "if" read as the text's own no.
- **Licence:** "If the Minister did not complete the preliminary assessment before the commencement day" (line 19675).

### F24. s 696.5(1): the Commission may conduct an investigation (name-test sweep of 2026-11-12)

- **Provision:** `s 696.5(1) (not in force) the Commission may conduct an investigation in relation to the application`.
- **Rows:** r189.
- **Reading taken:** Named for a power: when neither ground is present (no reasonable grounds to believe that a miscarriage of justice may have occurred, and no view that an investigation is in the interests of justice) the answer is NOTHING, not JUST FALSE.
- **Other reading:** JUST FALSE: a failed "if" read as the text's own no.
- **Licence:** "If the Commission has reasonable grounds to believe that a miscarriage of justice may have occurred or considers that it is in the interests of justice to do so" (line 19596).

### F25. 2019 c 25 s 359: a person who has already elected (name-test sweep of 2026-11-12)

- **Provision:** `2019 c 25 s 359 the person may elect another mode of trial`.
- **Rows:** r068.
- **Reading taken:** Named for a power: a person who has already elected another mode of trial is NOTHING, not JUST FALSE; this is the "if they have not already done so" branch only. The 14-day deadline branch keeps JUST FALSE (F4).
- **Other reading:** JUST FALSE: a failed "if" read as the text's own no.
- **Licence:** "may, if they have not already done so and despite those provisions, elect another mode of trial" (line 19266).

### Name-test sweep of 2026-11-12

The lead asked for every layer-1 function whose name contains "may", "permitted", "power", "entitled", "authorised" or "authorized" to be tested: a function named for a grant or a power that answers JUST FALSE because an "if" gate failed reads as "may not", which turns a grant into a bar.
24 functions matched (none contains "entitled").
Outside the sweep: named "it is lawful": 0 functions (functions so named are outside the sweep and are listed here for a lawyer to decide; this part has none).

| flipped to NOTHING | kept JUST FALSE (gate closed by the text, a bar or a duty) | listed: "may" with where/when/upon | listed: "entitled" |
| --- | --- | --- | --- |
| 5 | 6 | 3 | 0 |

Most of this range is transitional and coming-into-force rules, not grants; 11 of the 24 matched functions have no JUST FALSE branch at all.
(11 functions have a grant-like name and no JUST FALSE branch, so nothing was to be decided: `s 490.04(3)(a) (not in force) a superior court of criminal jurisdiction is a court that may receive the application`; `s 490.05(3)(a) (not in force) a superior court of criminal jurisdiction is a court that may receive the application`; `s 696.2(1) (not in force) an application for a review on the grounds of miscarriage of justice may be made to the Commission by or on behalf of the person`; `s 696.3(2) (not in force) the notice or information may be provided to a representative of the applicant in addition to or instead of the applicant`; `s 696.4(4) (not in force) the Commission may decide that the application is admissible despite subsection (3)`; `s 696.5(4) (not in force) the Commission has the powers of a commissioner under Part I of the Inquiries Act`; `s 696.5(5) (not in force) the Commission may authorize the person to exercise the powers referred to in subsection (4)`; `s 696.6(6) (not in force) the Commission may grant a remedy under subsection (2) even if the evidence does not establish the innocence of the applicant`; `s 696.61 (not in force) the Commission may refer the question to the court of appeal for its opinion`; `2018 c 12 s 406(1) a remediation agreement may be entered into in respect of the offence`; `2018 c 21 s 34(1) an appeal may be taken against the order`.)
(`2019 c 25 s 359` is counted in the first and the third column: its "already elected" branch is flipped and its deadline branch is listed.)

**Flipped to NOTHING** (one fork line each, F21 to F25 above, and in the marginal readings below; the other reading is JUST FALSE, a failed "if" read as the text's own no):
- `2024 c 33 s 9 the Minister is authorized to disclose to the Commission all information pertaining to the application that is under the Minister’s control`
- `2024 c 33 s 10(3) the applicant may apply to the Commission under the new scheme`
- `2024 c 33 s 11 the Minister is authorized to disclose to the Commission all information pertaining to the application that is under the Minister’s control`
- `s 696.5(1) (not in force) the Commission may conduct an investigation in relation to the application`
- `2019 c 25 s 359 the person may elect another mode of trial`

**Kept JUST FALSE:**
- `s 490.04(2) (not in force) the person is permitted to apply under paragraph (1)(b)`: a bar ("A person is not permitted"); left as decided in the seat audit
- `s 490.04(4) (not in force) the court may make an exemption order`: a bar ("The court shall not make"); left as decided in the seat audit
- `2024 c 33 s 12 the consent may be revoked`: a bar ("is irrevocable"): JUST FALSE when the gate is met, not when it fails
- `s 696.6(4) (not in force) the Commission may take the step`: gate closed by the text ("may only refer the matter ... or dismiss")
- `s 696.5(2) (not in force) the notice must also specify a reasonable period within which further information may be provided`: a duty ("must"), not a grant
- `s 696.5(7) (not in force) the report must specify a reasonable period within which a written response may be provided`: a duty ("must"), not a grant

**Listed, not flipped: "may" with a where, when, upon or period gate.** Assumed, not ruled, that these go with the listed group; ruling (b) of the periods ruling says JUST FALSE and the Guide's line on grants points the other way, so the question is for the maintainer or a lawyer:
- `2011 c 2 s 7(2) the person may make an application under subsection 745.6(1) as amended`: "within 180 days after": a window, JUST FALSE outside it (ruling 2026-11-05 (a)); other reading NOTHING (a stated period limiting a grant)
- `2011 c 2 s 7(3) the person may make an application under subsection 745.6(1) as amended`: "within 180 days after": as above
- `2019 c 25 s 359 the person may elect another mode of trial`: the deadline branch only ("not later than 14 days before ... and ... after that time with the written consent"): JUST FALSE after the deadline without consent (ruling (a)); other reading NOTHING. The "if they have not already done so" branch of the same function is flipped (F25).

**Listed, not flipped: "entitled":** none.

### Decisions that are not forks (assumed, not ruled)

- **D1. The future text is a second text.** Every replacement text under "AMENDMENTS NOT IN FORCE" is carried under names with `(not in force)`; the seat questions about it sit under their own `§` headings whose comment says to show them only to a person who asks about the future text. Licence: the band's own heading, and PLAN.md section 6 (ccc32).
- **D2. A date the text does not give is an input.** No commencement day, royal assent day or time limit fixed by a Minister is in the sources, so each is a DATE input. Licence: the brief ("Amounts, rates and thresholds the text leaves to regulations, orders or a Minister are INPUTS").
- **D3. The "for greater certainty" clauses are encoded as rules**, not as inert: they say which text governs, and a person can be asked. Licence: the brief ("Each related or transitional provision is a coverage row, encoded if it still affects someone").
- **D4. A provision that addresses only an official is encoded in layer 1 for what it decides**, and has a seat question only for what it means to the person (the Review Board's twelve months, the Commission's duties, the Minister's duty to ask). Licence: the brief ("Provisions that address only an official ...").
- **D5. Borrowed terms are asked as facts.** `intimate partner` (section 2), the meaning of a word "as in section 347", "715.3" or the Code, the cases of section 561, subsection 737(1.1) and paragraph 490.04(4)(b) are MAYBE BOOLEAN inputs (see Seams): the seat passes the accused's yes or no as a firm answer, so this layer cannot say "not covered" on the accused's behalf. Licence: Guide section 4 as quoted in the brief.

## Rulings carried word for word (ccc32)

The brief asks that each ruling of 2026-11-04 and 2026-11-05 be recorded again, word for word, in the NOTES.md of each row that carries a `NOTHING-kind` tag of its kind.
This range carries 162 `NOTHING-kind` tags (of which 135 are `limited by its own wording`) and 94 `FALSE-kind` tags, so every ruling below is applied here; the copies below are made by a script from the brief, not retyped.
How each applies in this range: **E1** (option C, per-section answers): every provision here answers for itself and no legal effect is gathered across sections; **N2** (option A): a flat negative ("does not apply", "shall not", "no report is to be prepared") answers JUST FALSE; **periods** (a)-(c): a window fixed in the text's own words answers JUST FALSE outside it, a failed "where" answers JUST FALSE, a scope limit with no "only" answers NOTHING outside it; **delegated definitions, defences and "until" bars** (d): the "until" of 1991 c 43 s 10(1) is encoded as the bar (JUST TRUE before a section 672.54 order, JUST FALSE after); **case by case**: the sites are the fork entries F4, F5, F8 and F11.

- **E1** (bench `commons-negation-1030`; should a legal effect be one definition gathered from every section that gives it?): option B, as guidance for gathering a legal effect's routes by hand only, with no pilot run; option A (gathering by bare name) is withdrawn as a direction for the language, not deferred; option C (per-section answers) applies everywhere else; the Magna Carta pilot in the printed recommendation (chapters 2, 3, 4, 5, 37, 43, 46 and 53, with a blind second reader) is not to be run. The maintainer's lean, verbatim: "B but generally uncomfortable with this much magic because it takes the language from unopinionated to opinionated in ways that are hard to teach an l4 novice." the maintainer's note, verbatim: "Fundamentally I feel like we are trying to make the language do work that the human l4 drafter should do. Too much magic. Can’t we just decline to be this opinionated and say the programmer needs to do this thinking?" Marked 2026-11-03T23:19:02.812Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23

- **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. The maintainer's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." the maintainer's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23

- **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. The maintainer's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

- **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. The maintainer approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

- **Questions with no convention: decide case by case (the maintainer, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. The maintainer's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with the coordinator where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

## Jural relations (ccc32)

One row per provision that creates a relation, in the text's order; a provision that creates none is listed once with `none` in the kind column.
The kinds are Hohfeld's: claim / duty, privilege / no-right, power / liability, immunity / disability.
Most of this range is application, deeming and reading rules, which fix which text governs and create no relation of their own: they are `none`, and the relation lies in the provision they apply.
A provision that withholds a new provision from earlier conduct or an earlier charge is read as an immunity of that person and a disability of the court (assumed, not ruled).
Provisions that only bind an official (a committee, a Minister) are listed with that relation and are inert (reason 2).

| provision | holds (right, privilege, power, immunity) | bears (duty, no-right, liability, disability) | kind | L4 rule |
| --- | --- | --- | --- | --- |
| 1991 c 43 s 10(1) (the order keeps its force until a section 672.54 order is made) | the authority detaining the person under the old order | the detained person | power / liability | `1991 c 43 s 10(1) the order for detention continues in force` |
| 1991 c 43 s 10(2) (a review within twelve months; also written as a regulative rule) | the detained person | the Review Board of the province | claim / duty | `1991 c 43 s 10(2) the Review Board must review the case`; `1991 c 43 s 10(2) the review was within twelve months after the coming into force` |
| 1991 c 43 s 10(3), (3)(a), (3)(b) (an application rule: sections 672.5 to 672.85 apply with changes, the review is read as a review under 672.81 and the warrant as a disposition) | none | none | none | `1991 c 43 s 10(3) the section applies, with such modifications as the circumstances require, to the review`; `1991 c 43 s 10(3)(a) the review is treated as a review of a disposition conducted under section 672.81`; `1991 c 43 s 10(3)(b) the warrant is treated as a disposition made under section 672.54` |
| 1991 c 43 s 10(3)(c), (d), (4) to (7) (repealed in the text) | none | none | none | `1991 c 43 s 10(3)(c) and (d) as the text shows them`; `1991 c 43 s 10(4) to (7) as the text shows them` |
| 2004 c 12 ss 22, 23 (reading rules: what a cross-reference in a Bill refers to) | none | none | none | `2004 c 12 s 22 the reference is read as referring to`; `2004 c 12 s 23 the reference is read as referring to` |
| 2005 c 32 s 27.1 (a review of the provisions and a report to Parliament (inert, reason 2)) | Parliament (a House, a committee, or the public through Parliament) | the parliamentary committee | claim / duty | none (inert) |
| 2009 c 28 s 12 (a review and a report (inert, reason 2)) | Parliament (a House, a committee, or the public through Parliament) | the committee of a House | claim / duty | none (inert) |
| 2009 c 29 s 5 | a person charged on or before the day | the court (it may not apply subsections 719(3) to (3.4) to that person) | immunity / disability | `2009 c 29 s 5 the person is within the limit on subsections 719(3) to (3.4)` |
| 2011 c 2 s 7(1) (an application rule: it fixes which text governs; the relations are those of the provision it applies) | none | none | none | `2011 c 2 s 7(1) the application is dealt with and disposed of under the Code as it read immediately before that day` |
| 2011 c 2 s 7(2), (3) | the person whose application under section 745.6 was pending | the court (it must hear a new application made in the window) | power / liability | `2011 c 2 s 7(2) the person may make an application under subsection 745.6(1) as amended`; `2011 c 2 s 7(3) the person may make an application under subsection 745.6(1) as amended` |
| 2012 c 1 ss 163, 165 (reading rules: a reference to a record suspension also covers a pardon) | none | none | none | `2012 c 1 s 163(a) the reference to an application for a record suspension is also a reference to an application for a pardon`; `2012 c 1 s 165(b) the reference to a record suspension is also a reference to a pardon` |
| 2014 c 6 s 20.1; 2014 c 25 s 45.1 (a review and a report (inert, reason 2)) | Parliament (a House, a committee, or the public through Parliament) | the committee or Minister named | claim / duty | none (inert) |
| 2015 c 13 s 37 (an application rule: it fixes which text governs; the relations are those of the provision it applies) | none | none | none | `2015 c 13 s 37 subsection 278.3(5) as it read immediately before that day continues to apply to the hearing` |
| 2015 c 13 ss 38, 39, 41, 43 (an application rule: it fixes which text governs; the relations are those of the provision it applies) | none | none | none | `2015 c 13 s 38 section 380.3 as it read immediately before that day continues to apply to the request for restitution`; `2015 c 13 s 39 section 380.4 as it read immediately before that day continues to apply to the statement`; `2015 c 13 s 41 section 672.5 as it read immediately before that day continues to apply to the statement` (+1 more) |
| 2015 c 13 ss 40, 42, 42.1, 44 (section 40 (423.1), 42 (718), 42.1 (718.2(e)), 44 (737.1, 739.1 to 739.4)) | a person whose conduct was before the day | the court (it may not apply the amended text to that conduct) | immunity / disability | `2015 c 13 s 40 the conduct is within the limit on section 423.1`; `2015 c 13 s 42 the conduct is within the limit on the amendments to section 718`; `2015 c 13 s 42.1 the conduct is within the limit on the amendment to paragraph 718.2(e)` (+1 more) |
| 2015 c 20 s 28 (a deeming rule: an information laid under 810.01(1) is treated as laid under 810.011(1)) | none | none | none | `2015 c 20 s 28 the information is deemed to have been laid under subsection 810.011(1)` |
| 2016 c 3 ss 9.1, 10 (reports and a review (inert, reason 2)) | Parliament (a House, a committee, or the public through Parliament) | the Ministers and the committee named | claim / duty | none (inert) |
| 2018 c 12 s 406 (an application rule (406(1)) and a reading rule (406(2))) | none | none | none | `2018 c 12 s 406(1) a remediation agreement may be entered into in respect of the offence`; `2018 c 12 s 406(2) the term has the meaning it has in section 715.3` |
| 2018 c 21 s 10 (a deeming rule: devices approved under the old subsection 254(1) are treated as approved) | none | none | none | `2018 c 21 s 10 the thing is deemed to be approved, as the same kind of thing, under section 254.01 as enacted by section 4` |
| 2018 c 21 s 31.1 (a review and a report (inert, reason 2)) | Parliament (a House, a committee, or the public through Parliament) | the Minister of Justice | claim / duty | none (inert) |
| 2018 c 21 ss 32, 33 (an application rule: it fixes which text governs; the relations are those of the provision it applies) | none | none | none | `2018 c 21 s 32(1) section 320.34 as enacted by section 15 applies to the application`; `2018 c 21 s 32(2) subsection 320.31(1) as enacted by section 15 applies to the trial`; `2018 c 21 s 33 section 320.36 as enacted by section 15 applies to the thing` |
| 2018 c 21 s 34(1) (may appeal on or after the day, under the old law) | a person against whom an order was made under the old section 259 | the court of appeal | power / liability | `2018 c 21 s 34(1) an appeal may be taken against the order`; `2018 c 21 s 34(1) the appeal is taken under section 675 and disposed of under the provisions of the Act, each as it read immediately before that day` |
| 2018 c 21 s 34(2) (an application rule: it fixes which text governs; the relations are those of the provision it applies) | none | none | none | `2018 c 21 s 34(2) sections 261 and 680 as they read immediately before that day apply to the appeal` |
| 2018 c 21 ss 35 to 38 (deeming rules: old approvals and designations are treated as new ones) | none | none | none | `2018 c 21 s 35 the thing is deemed to be approved, as the same kind of thing, under section 320.39 as enacted by section 15`; `2018 c 21 s 36 the person is deemed to be designated as a qualified technician under paragraph 320.4(a)`; `2018 c 21 s 37 the person is deemed to be designated as a qualified technician under subparagraph 320.4(b)(i)` (+1 more) |
| 2018 c 29 s 74 (an application rule: it fixes which text governs; the relations are those of the provision it applies) | none | none | none | `2018 c 29 s 74 subsection 278.3(5) as it read immediately before that day continues to apply to the hearing` |
| 2019 c 13 ss 155, 156 (an application rule: it fixes which text governs; the relations are those of the provision it applies) | none | none | none | `2019 c 13 s 155 paragraph 83.05(1)(b) and subsection 83.05(3) as they read immediately before that day continue to apply to the application`; `2019 c 13 s 156 the proceedings are to be completed under sections 83.28 and 83.29 as they read before that day` |
| 2019 c 13 s 157 (no report for the year before the subsection came into force; it addresses only an official) | the Minister who would have had to report | Parliament | immunity / disability | `2019 c 13 s 157 a report is to be prepared under subsection 810.011(15)` |
| 2019 c 13 s 157.1 (a revival rule: section 83.3 is effective again) | none | none | none | `2019 c 13 s 157.1 section 83.3 becomes effective again as of the day on which this section comes into force`; `2019 c 13 s 157.1 sections 146 and 148 of 2019, c. 13 apply in respect of section 83.3` |
| 2019 c 25 ss 354 to 358 (deeming rules: an old promise, undertaking or recognizance is treated as an appearance notice, undertaking or release order) | none | none | none | `2019 c 25 s 354 the person is deemed to be bound by an appearance notice as defined in section 2`; `2019 c 25 s 355 the person is deemed to be bound by an undertaking as defined in section 2`; `2019 c 25 s 356 the person is deemed to be bound by an undertaking as defined in section 2` (+2 more) |
| 2019 c 25 s 359 | an accused person caught by the new limits on mode of trial | the court (it must try the case in the mode elected) | power / liability | `2019 c 25 s 359 the person may elect another mode of trial` |
| 2019 c 25 s 360 | a person charged with an old summary conviction offence | the prosecutor (no proceedings after six months) | immunity / disability | `2019 c 25 s 360 the proceedings are within the time limit` |
| 2021 c 2 s 3.1 (a review and a report (inert, reason 2)) | Parliament (a House, a committee, or the public through Parliament) | the Ministers of Justice and of Health | claim / duty | none (inert) |
| 2021 c 2 s 4 (the old section 241.2 governs a request signed before royal assent; also written as a regulative rule) | the public, as represented by the Crown | a medical practitioner or nurse practitioner who provides medical assistance in dying | claim / duty | `2021 c 2 s 4 the provider must provide medical assistance in dying in accordance with the old section 241.2`; `2021 c 2 s 4 the provider must provide it in accordance with the old section 241.2 and subsections 241.2(3.2) to (3.5)` |
| 2021 c 2 s 5 (a comprehensive review and a report (inert, reason 2)) | Parliament (a House, a committee, or the public through Parliament) | the Joint Committee | claim / duty | none (inert) |
| 2022 c 15 s 21 (a review (inert, reason 2)) | Parliament (a House, a committee, or the public through Parliament) | the committee named | claim / duty | none (inert) |
| 2022 c 17 s 76 (an application rule: it fixes which text governs; the relations are those of the provision it applies) | none | none | none | `2022 c 17 s 76 the amendments made by 2022, c. 17 apply to the proceedings, subject to sections 77 and 78` |
| 2022 c 17 ss 77, 78 (an application rule: it fixes which text governs; the relations are those of the provision it applies) | none | none | none | `2022 c 17 s 77(1) the Criminal Code as it read immediately before that day continues to apply`; `2022 c 17 s 78 section 489.1 as it read immediately before that day continues to apply to the thing seized` |
| 2022 c 17 ss 78.1, 78.2 (reviews and reports (inert, reason 2)) | Parliament (a House, a committee, or the public through Parliament) | the Minister of Justice and the committees named | claim / duty | none (inert) |
| 2023 c 26 s 613 (a reading rule) | none | none | none | `2023 c 26 s 613 the word or expression has the meaning it has in sections 347 and 347.1` |
| 2023 c 26 ss 614, 615 | a person who receives interest under an agreement made before the day | the Crown (the new criminal-rate provisions do not apply to that person) | immunity / disability | `2023 c 26 s 614 the definition criminal rate in subsection 347(2), as it reads on that day, applies to the receipt`; `2023 c 26 s 615 paragraph 347.1(2)(a.1), as it reads on that day, applies to the person` |
| 2023 c 30 s 2 (a review (inert, reason 2)) | Parliament (a House, a committee, or the public through Parliament) | the committee named | claim / duty | none (inert) |
| 2023 c 30 s 3 (an application rule: it fixes which text governs; the relations are those of the provision it applies) | none | none | none | `2023 c 30 s 3 the amendments made by 2023, c. 30 apply to the matter or proceeding` |
| 2023 c 32 s 14.1 (paragraph (e) does not apply to the firearm in those proceedings) | the person in proceedings begun before paragraph (e) came into force | the Crown | immunity / disability | `2023 c 32 s 14.1 paragraph (e) of the definition prohibited firearm applies to the firearm in relation to those proceedings` |
| 2023 c 32 s 14.2; 2024 c 1 s 2 (reviews and reports (inert, reason 2)) | Parliament (a House, a committee, or the public through Parliament) | the committee named | claim / duty | none (inert) |
| 2024 c 22 s 8 (a deeming rule: an information under 810(1) is treated as laid under 810.03(1)) | none | none | none | `2024 c 22 s 8 the information is deemed to have been laid under subsection 810.03(1)` |
| 2024 c 23 s 13 (a saving rule (the amendments do not affect validity) and a reading rule (a reference to child pornography)) | none | none | none | `2024 c 23 s 13 the amendments made by 2024, c. 23 affect the validity of the proceedings`; `2024 c 23 s 13 the amendments made by 2024, c. 23 affect the validity of the document`; `2024 c 23 s 13 the reference to child pornography in the document is read as a reference to` |
| 2026 c 11 s 56 (a reading rule) | none | none | none | `2026 c 11 s 56 the word or expression has the same meaning as in the Criminal Code` |
| 2026 c 11 s 57 (an application rule: it fixes which text governs; the relations are those of the provision it applies) | none | none | none | `2026 c 11 s 57 the provisions of the Criminal Code enacted by sections 41 and 42 apply to the proceeds of the fine` |
| 2026 c 11 s 58(1) | a person who committed an offence before the day | the court | immunity / disability | `2026 c 11 s 58(1) the offence is within the limit on the provisions enacted by sections 8, 9, 11, 37, 40 and 43` |
| 2026 c 11 s 58(2), (3) (an application rule: it fixes which text governs; the relations are those of the provision it applies) | none | none | none | `2026 c 11 s 58(2) the amendments to Parts XVI and XXVIII made by 2026, c. 11 apply to the matter or proceeding`; `2026 c 11 s 58(3) the provisions enacted by sections 10, 34 to 36, 38 and 39 of 2026, c. 11 apply to the matter or proceeding` |
| 2026 c 12 s 15 | a person who committed manslaughter before the 30th day after royal assent | the court (subsection 236(2) does not apply) | immunity / disability | `2026 c 12 s 15 subsection 236(2) applies to the offence` |
| 2026 c 12 s 16 (an application rule: it fixes which text governs; the relations are those of the provision it applies) | none | none | none | `2026 c 12 s 16 subsection 490(2) as amended by section 3 of 2026, c. 12 applies to the matter or proceeding` |
| 2026 c 15 s 11.1(1), (2) (a clarification of what section 319 does not prohibit) | the person who communicates a statement on a matter of public interest | anyone who would prosecute under 319(2), (2.1) or (2.2) | privilege / no-right | `2026 c 15 s 11.1(1) the clarification applies to the person's communication of the statement`; `2026 c 15 s 11.1(2) the clarification applies to the person's communication of the statement` |
| 2026 c 19 s 87 (an affirmation that a minimum punishment still operates) | none | none | none | `2026 c 19 s 87 the operation of the minimum punishment is affirmed following the enactment of section 718.4` |
| 2026 c 19 s 96 (definitions) (definitions of `Act` and `commencement day`) | none | none | none | `2026 c 19 s 96 the definitions apply in the section`; `2026 c 19 s 96 Act`; `2026 c 19 s 96 commencement day` |
| 2026 c 19 ss 97, 98, 100, 105 (section 97: subsection 7(4.1); 98: paragraphs 236(2)(b) to (d); 100: the rules on records and admissibility; 105: Part XV.1) | a person who committed the offence, or was charged, before the commencement day | the court | immunity / disability | `2026 c 19 s 97 the act or omission is within the time limit on subsection 7(4.1)`; `2026 c 19 s 98 paragraphs 236(2)(b) to (d) apply to the offence`; `2026 c 19 s 100 the offence is within the time limit on the provisions of sections 276, 276.01 to 276.13 and 278.1 to 278.38 named by this section` (+1 more) |
| 2026 c 19 ss 99, 101 to 103, 106 to 109, 111(2), 112, 113, 117, 118 (an application rule: it fixes which text governs; the relations are those of the provision it applies) | none | none | none | `2026 c 19 s 99 paragraph 264(4)(a) applies to the matter or proceeding`; `2026 c 19 s 101 subsection 346(1.4) applies to the matter or proceeding`; `2026 c 19 s 102 sections 486.1, 486.2 and 486.3 as amended by sections 38, 39 and 40 of 2026, c. 19 apply to the matter or proceeding` (+10 more) |
| 2026 c 19 s 110 (an application rule: it fixes which text governs; the relations are those of the provision it applies) | none | none | none | `2026 c 19 s 110 section 672.5011 applies to the order` |
| 2026 c 19 s 111(1) (a deeming rule: an old alternative measure is an alternative measure under 715.44) | none | none | none | `2026 c 19 s 111(1) the measure is deemed to be an alternative measure, as defined in section 715.44` |
| 2026 c 19 ss 114 to 116 (sections 729.2, 740.1 and 752.01) | a person who committed the offence before the commencement day (and, for section 116, the prosecutor) | the court | immunity / disability | `2026 c 19 s 114 the offence is within the time limit on section 729.2`; `2026 c 19 s 115 the order is within the limits on section 740.1`; `2026 c 19 s 116 the offence is within the time limit on section 752.01` |
| 2026 c 19 ss 118.1, 119 (reviews (inert, reason 2)) | Parliament (a House, a committee, or the public through Parliament) | the committee or Minister named | claim / duty | none (inert) |
| 2018 c 16 s 190 (replacing 737(1)) (a conditional replacement: it takes effect only if Bill C-28 receives royal assent and both provisions are in force) | none | none | none | `2018 c 16 s 190 subsection 737(1) is replaced by the following` |
| s 737(1) as replaced (not in force) (the victim surcharge, subject to subsection (1.1)) | the Crown (the victim surcharge fund) | the offender | claim / duty | `s 737(1) (not in force) the offender shall pay a victim surcharge for each offence` |
| 2018 c 21 s 51; 2018 c 29 ss 79, 80 (coordinating clauses among Bills: they settle the order in which amendments take effect (inert, reason 2)) | none | none | none | none (inert) |
| 2021 c 2 s 1(2.1) (not in force) (a repeal) | none | none | none | `2021 c 2 s 1(2.1) subsection 241.2(2.1) is repealed` |
| s 743.2 as replaced (not in force) (also written as a regulative rule) | the Correctional Service of Canada (and a victim who wishes to receive information) | the court that sentences or commits a person to penitentiary | claim / duty | `s 743.2 (not in force) the court shall forward the item to the Correctional Service of Canada`; `s 743.2 (not in force) the court must forward the reasons, reports, information and victim contact details to the Correctional Service of Canada` |
| s 679(7) as replaced (not in force) (section 679 applies as though the person were an appellant) | a person whom the Commission has told that the application is admissible | the court | power / liability | `s 679(7) (not in force) section 679 applies to the release or detention of the person as though the person were an appellant in an appeal described in paragraph (1)(a)` |
| 2024 c 33 s 3 and s 696.1 (not in force) (the replacement instruction and the definitions of Part XXI.1) | none | none | none | `2024 c 33 s 3 Part XXI.1 is replaced by the following`; `s 696.1 (not in force) the definitions apply in the provision`; `s 696.1 "applicant" (not in force)` (+2 more) |
| s 696.2(1) (not in force) (the power to apply for a review on the grounds of miscarriage of justice) | a person described in the subsection | the Commission | power / liability | `s 696.2(1) (not in force) an application for a review on the grounds of miscarriage of justice may be made to the Commission by or on behalf of the person` |
| s 696.2(2) (not in force) (the content an application must have) | the Commission | the applicant | claim / duty | `s 696.2(2) (not in force) the application includes what it must include` |
| s 696.3(1) (not in force) (deal with the application as expeditiously as possible and give regular updates; also written as regulative rules) | the applicant | the Commission | claim / duty | `s 696.3(1) (not in force) the Commission must deal with the application as expeditiously as possible`; `s 696.3(1) (not in force) the Commission must provide the applicant with an update on a regular basis`; `s 696.3(1) (not in force) the Commission owes the applicant the duty to deal with the application as expeditiously as possible and to provide regular updates` |
| s 696.3(2) (not in force) (a communication rule: a notice may go to the applicant's representative) | none | none | none | `s 696.3(2) (not in force) the notice or information may be provided to a representative of the applicant in addition to or instead of the applicant` |
| s 696.4(1) (not in force) (decide whether the application is admissible) | the applicant | the Commission | claim / duty | `s 696.4(1) (not in force) the Commission must decide whether the application is admissible`; `s 696.4(1) (not in force) the Commission owes the duty to decide whether the application is admissible` |
| s 696.4(2), (3) (not in force) (must dismiss an inadmissible application) | the Crown and the public (the correlative claim holder is not named) | the Commission | claim / duty | `s 696.4(2) (not in force) the Commission must dismiss the application as inadmissible on the ground that the person is not described in subsection 696.2(1)`; `s 696.4(3) (not in force) the Commission must dismiss the application as inadmissible on a ground in subsection (3)` |
| s 696.4(4) (not in force) (may decide an application is admissible although there was no appeal) | the Commission | the applicant | power / liability | `s 696.4(4) (not in force) the Commission may decide that the application is admissible despite subsection (3)` |
| s 696.4(4)(a) to (e) (not in force) (the factors the Commission must take into account) | the applicant | the Commission | claim / duty | `s 696.4(4) (not in force) the Commission must take the factor into account`; `s 696.4(4)(d) (not in force) the application is supported by a new matter of significance that meets subparagraphs (i) to (iii)` |
| s 696.4(5) (not in force) (notice of the admissibility decision) | the applicant and the relevant Attorney General | the Commission | claim / duty | `s 696.4(5) (not in force) the Commission must notify the applicant and the relevant Attorney General of its decision on admissibility`; `s 696.4(5) (not in force) the Commission owes the duty to notify the applicant and the relevant Attorney General of its decision on admissibility` |
| s 696.5(1) (not in force) (the power to investigate) | the Commission | the applicant | power / liability | `s 696.5(1) (not in force) the Commission may conduct an investigation in relation to the application` |
| s 696.5(2) (not in force) (notice whether there will be an investigation, and a period to send further information) | the applicant and the relevant Attorney General | the Commission | claim / duty | `s 696.5(2) (not in force) the Commission must send a notice indicating whether an investigation will be conducted`; `s 696.5(2) (not in force) the Commission owes the duty to send a notice indicating whether an investigation will be conducted`; `s 696.5(2) (not in force) the notice must also specify a reasonable period within which further information may be provided` |
| s 696.5(3) (not in force) (may decide without an investigation after the period) | the Commission | the applicant | power / liability | `s 696.5(3) (not in force) the condition for deciding under section 696.6 without an investigation is met` |
| s 696.5(4), (5) (not in force) (the powers of a commissioner under Part I of the Inquiries Act, and their delegation) | the Commission | persons from whom evidence is sought | power / liability | `s 696.5(4) (not in force) the Commission has the powers of a commissioner under Part I of the Inquiries Act`; `s 696.5(5) (not in force) the Commission may authorize the person to exercise the powers referred to in subsection (4)` |
| s 696.5(6), (7) (not in force) (a report after an investigation, with a period for a written response) | the applicant and the relevant Attorney General | the Commission | claim / duty | `s 696.5(6) (not in force) the Commission must prepare a report and provide a copy of it`; `s 696.5(6) (not in force) the Commission owes the duty to prepare a report and provide a copy of it`; `s 696.5(7) (not in force) the report must specify a reasonable period within which a written response may be provided` |
| s 696.5(8) (not in force) (may decide after the investigation) | the Commission | the applicant | power / liability | `s 696.5(8) (not in force) the condition for deciding under section 696.6 after an investigation is met` |
| s 696.6(1) (not in force) (make a decision on completion of a review) | the applicant | the Commission | claim / duty | `s 696.6(1) (not in force) the Commission must make a decision on the application`; `s 696.6(1) (not in force) the Commission owes the duty to make a decision on the application` |
| s 696.6(2) (not in force) (the power to grant a remedy) | the Commission | the court (a new trial or hearing) and the applicant (the conviction) | power / liability | `s 696.6(2) (not in force) the Commission must grant a remedy under paragraph (a) or (b)`; `s 696.6(2)(a) (not in force) the form of the new proceeding the Commission directs` |
| s 696.6(3) (not in force) (must dismiss the application where it grants no remedy) | the applicant and the public | the Commission | claim / duty | `s 696.6(3) (not in force) the Commission must dismiss the application` |
| s 696.6(4) (not in force) | the applicant's estate or representative | the Commission (it may only refer or dismiss) | immunity / disability | `s 696.6(4) (not in force) the Commission may take the step` |
| s 696.6(5) (not in force) (the factors the Commission must take into account) | the applicant | the Commission | claim / duty | `s 696.6(5) (not in force) the Commission must take the factor into account` |
| s 696.6(6) (not in force) (a remedy may be granted even if the evidence does not establish innocence) | the Commission | no one (a clarification) | privilege / no-right | `s 696.6(6) (not in force) the Commission may grant a remedy under subsection (2) even if the evidence does not establish the innocence of the applicant` |
| s 696.6(7) (not in force) (notice of the decision) | the applicant and the relevant Attorney General | the Commission | claim / duty | `s 696.6(7) (not in force) the Commission must notify the applicant and the relevant Attorney General of its decision`; `s 696.6(7) (not in force) the Commission owes the duty to notify the applicant and the relevant Attorney General of its decision` |
| s 696.61 (not in force) (the Commission may refer a question; the court of appeal must give its opinion) | the Commission | the court of appeal | claim / duty | `s 696.61 (not in force) the Commission may refer the question to the court of appeal for its opinion`; `s 696.61 (not in force) the court of appeal must provide its opinion`; `s 696.61 (not in force) the court of appeal must provide its opinion on the question` |
| s 696.62 (not in force) (a review of the Part (inert, reason 2)) | Parliament (a House, a committee, or the public through Parliament) | the Minister of Justice | claim / duty | none (inert) |
| 2024 c 33 ss 5, 6; s 696.7 "applicant"; s 696.72 (not in force) (a definition and a statement of the Commission's mandate) | none | none | none | `s 696.7 "applicant" (not in force)`; `s 696.72 (not in force) the application is within the Commission’s mandate` |
| 2024 c 33 s 7 (definitions) (definitions used in sections 7 to 13) | none | none | none | `2024 c 33 s 7 the definitions apply in the section`; `2024 c 33 s 7 "applicant"`; `2024 c 33 s 7 "commencement day"` (+4 more) |
| 2024 c 33 s 8 (the Minister must ask whether the applicant consents to the transfer; also written as a regulative rule) | the applicant | the Minister of Justice | claim / duty | `2024 c 33 s 8 the Minister must ask the applicant whether they consent to the transfer`; `2024 c 33 s 8 the Minister owes the duty to ask the applicant whether they consent to the transfer` |
| 2024 c 33 s 9 (consent within the time limit transfers the application and authorizes disclosure) | the applicant (power to consent); the Minister (power to disclose) | the Minister; the Commission | power / liability | `2024 c 33 s 9 the application is deemed to have been made to the Commission under the new scheme`; `2024 c 33 s 9 the Minister is authorized to disclose to the Commission all information pertaining to the application that is under the Minister’s control` |
| 2024 c 33 s 10 (what follows when the applicant does not reply or refuses) | the applicant (the power to apply under the new scheme, in (3)) | the Minister | power / liability | `2024 c 33 s 10(1) subsection (2) or (3) applies`; `2024 c 33 s 10(2) the old scheme continues to apply in respect of the application`; `2024 c 33 s 10(3) the application is deemed not to have been made` (+1 more) |
| 2024 c 33 s 11 | the applicant (power to consent late); the Minister (power to disclose) | the Minister; the Commission | power / liability | `2024 c 33 s 11 the application is deemed to have been made to the Commission under the new scheme`; `2024 c 33 s 11 the Minister is authorized to disclose to the Commission all information pertaining to the application that is under the Minister’s control` |
| 2024 c 33 s 12 (consent given under section 9 or 11 is irrevocable) | the Minister and the Commission | the applicant (no power to revoke) | immunity / disability | `2024 c 33 s 12 the consent may be revoked` |
| 2024 c 33 s 13 | the applicant | the Minister (the dismissal does not bar a new application) | immunity / disability | `2024 c 33 s 13 the fact that the Minister dismissed the application under the old scheme prevents the applicant from applying under the new scheme` |
| 2026 c 16 ss 48, 49; s 490.02(3), 490.022(4) (not in force) (reading rules about a reference to the definition designated offence) | none | none | none | `s 490.02(3) (not in force) the day before which the provision referred to is read`; `s 490.022(4) (not in force) the day before which the definition referred to is read` |
| s 490.04(1) (not in force) (the power to apply for an exemption order) | the person subject to the order or obligation | the court | power / liability | `s 490.04(1) (not in force) the order or obligation is one listed in paragraph (a), (a.1) or (b)` |
| s 490.04(2) (not in force) | the court and the Crown | the person (not permitted to apply again) | immunity / disability | `s 490.04(2) (not in force) the person is permitted to apply under paragraph (1)(b)` |
| s 490.04(3) (not in force) (a jurisdiction rule: which court may receive the application) | none | none | none | `s 490.04(3)(a) (not in force) a superior court of criminal jurisdiction is a court that may receive the application` |
| s 490.04(4) (not in force) | the Crown and the community | the court (it shall not make an exemption order in the listed cases) | immunity / disability | `s 490.04(4) (not in force) the court may make an exemption order` |
| s 490.04(8) (not in force) | the person who obtained an exemption order | the court (it shall order the RCMP to remove the information) | claim / duty | `s 490.04(8) (not in force) the court shall also make an order requiring the Royal Canadian Mounted Police to permanently remove the information from the database` |
| s 490.05(1) (not in force) (the power to apply for an order terminating it) | the person subject to a lifelong order or obligation | the court | power / liability | `s 490.05(1) (not in force) the order or obligation is one listed in the replaced paragraphs` |
| s 490.05(3) (not in force) (a jurisdiction rule) | none | none | none | `s 490.05(3)(a) (not in force) a superior court of criminal jurisdiction is a court that may receive the application` |
| s 490.05(5) (not in force) (a reading rule: which provision applies to the offence with the longest maximum) | none | none | none | `s 490.05(5) (not in force) the provision applied to the offence in question with the longest maximum term of imprisonment` |
| s 490.06(2) (not in force) | the person who obtained an exemption order on appeal | the appeal court (it shall order the RCMP to remove the information) | claim / duty | `s 490.06(2) (not in force) the appeal court shall also make an order requiring the Royal Canadian Mounted Police to permanently remove the information from the database` |
| 2026 c 16 s 53 (Form 52) (a change of the wording of a Form) | none | none | none | none (inert) |
| 2026 c 19 ss 2(2), 4, 24(5), 42, 45(2) (not in force) (additions of section 264.01 to lists that other sections use (3.01(1), 109(1), 183, 487.04, 490.011); the relations are those sections' own) | none | none | none | `s 3.01(1)(b.1) (not in force) the offence counts as one in which violence is used, threatened or attempted`; `s 109(1)(b) (not in force) the offence is one listed in paragraph (b)`; `s 183 "offence" (a)(xxxix.4) (not in force) the offence is within paragraph (a) of the definition` (+2 more) |
| s 264.01(1) (not in force) (the offence; the prohibition on the person follows from the flat negative of the text's wording (ruling N2)) | the Crown, for the community | everyone (not to engage in the pattern with the stated state of mind) | claim / duty | `s 264.01(1) (not in force) the accused commits an offence` |
| s 264.01(2), (3) (not in force) (definitions: the pattern, its acts and the circumstances) | none | none | none | `s 264.01(2) (not in force) the acts make up a pattern of coercive or controlling conduct`; `s 264.01(2)(a) (not in force) the act is within paragraph (a)`; `s 264.01(2)(b) (not in force) the act is within paragraph (b)` (+3 more) |
| s 264.01(4) (not in force) (on indictment up to ten years; the summary penalty is taken from section 787(1)) | the court (power to sentence) | the person convicted | power / liability | `s 264.01(4) (not in force) the class of the offence`; `s 264.01(4) (not in force) the punishment for the offence` |
| s 264.01(5) (not in force) (a definition: what safety includes) | none | none | none | `s 264.01(5) (not in force) a person’s safety includes the kind of safety` |

(The table covers all 307 rows of the coverage table, each exactly once; asserted by the script that wrote this file.)

## Marginal readings for a lawyer (ccc32)

### Reading a result: FALSE and NOTHING (ccc32)

Most of this range says which text governs a person around a change of the law, or what a not-yet-in-force provision would say.
- **A "no" (JUST FALSE)** in this range means the provision says no in its own words: it "applies only" to later conduct and the conduct was earlier; it "does not apply" or "is irrevocable" or "shall not" and the case is the one it describes; a period the text fixes ("on that day or within 14 days after", "within 180 days after", "not later than 14 days before", "more than six months after") has run; an "until" has been reached (an order was made under section 672.54); a condition the provision itself introduces with "if" is not met (marginal reading (a) below).
- **"Not covered" (NOTHING)** means the facts are outside what the provision grants or prohibits and the text says nothing about them: a matter that is not ongoing on the day, an order made after the day, a person of another kind, a case a list does not name, an element the section leaves to another provision or to another Act (an intimate partner, a section 561 case), or a time the section is silent about (the time before a repeal takes effect).
- A "no" about one provision is never an answer about another: for example a failed section 11.1 clarification does not say that section 319 prohibits the statement, and a JUST FALSE from a transitional rule does not say that the person is convicted, acquitted or sentenced.
- A caller must never turn NOTHING into FALSE.

The brief names two readings as for a lawyer, not for the encoder, and asks that every branch resting on one be listed with the other reading stated.
The branch lists below were produced by scanning the `FALSE-kind` and `NOTHING-kind` comments of the eight layer-1 modules; a function appears once with the number of branches in it.

### (a) A failed "if" counts as the text's no, clause by clause, within the provision that holds the "if"; a flat negative counts as the text saying no

#### (a1) A failed "if" inside the provision (and "subject to", "unless")

- **Reading taken:** JUST FALSE for the person when the provision's own "if" (or "subject to") is not met, with `-- FALSE-kind` quoting the words.
- **Other reading:** NOTHING: "if A then B" does not itself say "if not A then not B", so the person is not covered when the condition fails.
- **Status:** for a lawyer (brief, reading (a)).
- **Sites:** 39 branches in 31 functions.

| function | branches |
| --- | --- |
| `2018 c 16 s 190 subsection 737(1) is replaced by the following` | 1 |
| `s 737(1) (not in force) the offender shall pay a victim surcharge for each offence` | 1 |
| `s 679(7) (not in force) section 679 applies to the release or detention of the person as though the person were an appellant in an appeal described in paragraph (1)(a)` | 1 |
| `s 264.01(2)(c) (not in force) the conduct is within paragraph (c)` | 1 |
| `s 490.04(4) (not in force) the court may make an exemption order` | 3 |
| `s 490.04(8) (not in force) the court shall also make an order requiring the Royal Canadian Mounted Police to permanently remove the information from the database` | 1 |
| `s 490.05(1) (not in force) the order or obligation is one listed in the replaced paragraphs` | 5 |
| `s 490.06(2) (not in force) the appeal court shall also make an order requiring the Royal Canadian Mounted Police to permanently remove the information from the database` | 1 |
| `2024 c 33 s 8 the Minister owes the duty to ask the applicant whether they consent to the transfer` | 1 |
| `2024 c 33 s 9 the application is deemed to have been made to the Commission under the new scheme` | 1 |
| `2024 c 33 s 10(1) subsection (2) or (3) applies` | 1 |
| `2024 c 33 s 10(2) the old scheme continues to apply in respect of the application` | 1 |
| `2024 c 33 s 10(3) the application is deemed not to have been made` | 1 |
| `2024 c 33 s 11 the application is deemed to have been made to the Commission under the new scheme` | 1 |
| `s 696.4(2) (not in force) the Commission must dismiss the application as inadmissible on the ground that the person is not described in subsection 696.2(1)` | 1 |
| `s 696.4(3) (not in force) the Commission must dismiss the application as inadmissible on a ground in subsection (3)` | 1 |
| `s 696.5(2) (not in force) the notice must also specify a reasonable period within which further information may be provided` | 1 |
| `s 696.6(2) (not in force) the Commission must grant a remedy under paragraph (a) or (b)` | 1 |
| `s 696.6(3) (not in force) the Commission must dismiss the application` | 1 |
| `2015 c 20 s 28 the information is deemed to have been laid under subsection 810.011(1)` | 1 |
| `2018 c 21 s 32(1) section 320.34 as enacted by section 15 applies to the application` | 1 |
| `2018 c 21 s 32(2) subsection 320.31(1) as enacted by section 15 applies to the trial` | 1 |
| `2019 c 13 s 156 the proceedings are to be completed under sections 83.28 and 83.29 as they read before that day` | 1 |
| `2019 c 13 s 157.1 section 83.3 becomes effective again as of the day on which this section comes into force` | 1 |
| `2019 c 13 s 157.1 sections 146 and 148 of 2019, c. 13 apply in respect of section 83.3` | 1 |
| `2022 c 17 s 78 section 489.1 as it read immediately before that day continues to apply to the thing seized` | 1 |
| `2022 c 17 s 76 the amendments made by 2022, c. 17 apply to the proceedings, subject to sections 77 and 78` | 1 |
| `2024 c 22 s 8 the information is deemed to have been laid under subsection 810.03(1)` | 3 |
| `2026 c 11 s 56 the word or expression has the same meaning as in the Criminal Code` | 1 |
| `2026 c 15 s 11.1(1) the clarification applies to the person's communication of the statement` | 1 |
| `2026 c 15 s 11.1(2) the clarification applies to the person's communication of the statement` | 1 |

#### (a2) A flat negative

- **Reading taken:** JUST FALSE where the case is the one the negative describes ("does not", "shall not", "is not permitted", "is irrevocable", "no report is to be prepared").
- **Other reading:** NOTHING: a negative is a prohibition on the official or on the provision, not a statement about the person.
- **Status:** ruled for flat negatives (N2, option A, 2026-11-04) and flagged here because the typing of the kind is still a lawyer's.
- **Sites:** 9 branches in 9 functions.

| function | branches |
| --- | --- |
| `s 490.04(2) (not in force) the person is permitted to apply under paragraph (1)(b)` | 1 |
| `2024 c 33 s 12 the consent may be revoked` | 1 |
| `2024 c 33 s 13 the fact that the Minister dismissed the application under the old scheme prevents the applicant from applying under the new scheme` | 1 |
| `2019 c 13 s 157 a report is to be prepared under subsection 810.011(15)` | 1 |
| `2023 c 26 s 614 the definition criminal rate in subsection 347(2), as it reads on that day, applies to the receipt` | 1 |
| `2023 c 26 s 615 paragraph 347.1(2)(a.1), as it reads on that day, applies to the person` | 1 |
| `2023 c 32 s 14.1 paragraph (e) of the definition prohibited firearm applies to the firearm in relation to those proceedings` | 1 |
| `2024 c 23 s 13 the amendments made by 2024, c. 23 affect the validity of the proceedings` | 1 |
| `2024 c 23 s 13 the amendments made by 2024, c. 23 affect the validity of the document` | 1 |

#### (a3) A bare "must" not met, and a definition's "consists of"

- **Reading taken:** JUST FALSE (the content requirement is not met; fewer than two acts is not a pattern).
- **Other reading:** NOTHING: the text states the requirement or the definition and is silent on what follows.
- **Status:** decided case by case (2026-11-05); see F6 and F8.
- **Sites:** 2 branches in 2 functions.

| function | branches |
| --- | --- |
| `s 264.01(2) (not in force) the acts make up a pattern of coercive or controlling conduct` | 1 |
| `s 696.2(2) (not in force) the application includes what it must include` | 1 |

### Sites ruled, or governed by the brief's own rule (listed for completeness)

#### (a4) A period fixed in the text's own words, or an "until"

- **Reading taken:** JUST FALSE outside the period, JUST TRUE inside; the "until" bar is JUST TRUE before the stated event and JUST FALSE after.
- **Other reading:** NOTHING outside the period (it would be a scope limit with no "only").
- **Status:** ruled: the periods ruling (a) and the delegated-definitions ruling (d), 2026-11-05.
- **Sites:** 21 branches in 20 functions.

| function | branches |
| --- | --- |
| `s 490.04(1) (not in force) the order or obligation is one listed in paragraph (a), (a.1) or (b)` | 2 |
| `2024 c 33 s 7 "new scheme"` | 1 |
| `2024 c 33 s 7 "old scheme"` | 1 |
| `1991 c 43 s 10(1) the order for detention continues in force` | 1 |
| `1991 c 43 s 10(2) the review was within twelve months after the coming into force` | 1 |
| `2011 c 2 s 7(2) the person may make an application under subsection 745.6(1) as amended` | 1 |
| `2011 c 2 s 7(3) the person may make an application under subsection 745.6(1) as amended` | 1 |
| `2015 c 13 s 37 subsection 278.3(5) as it read immediately before that day continues to apply to the hearing` | 1 |
| `2018 c 29 s 74 subsection 278.3(5) as it read immediately before that day continues to apply to the hearing` | 1 |
| `2019 c 25 s 354 the person is deemed to be bound by an appearance notice as defined in section 2` | 1 |
| `2019 c 25 s 355 the person is deemed to be bound by an undertaking as defined in section 2` | 1 |
| `2019 c 25 s 356 the person is deemed to be bound by an undertaking as defined in section 2` | 1 |
| `2019 c 25 s 357 the person is deemed to be bound by a release order as defined in section 2` | 1 |
| `2019 c 25 s 358 the person is deemed to be bound by a release order as defined in section 2` | 1 |
| `2019 c 25 s 359 the person may elect another mode of trial` | 1 |
| `2019 c 25 s 360 the proceedings are within the time limit` | 1 |
| `2026 c 12 s 15 subsection 236(2) applies to the offence` | 1 |
| `2026 c 19 s 98 paragraphs 236(2)(b) to (d) apply to the offence` | 1 |
| `2026 c 19 s 111(1) the measure is deemed to be an alternative measure, as defined in section 715.44` | 1 |
| `2026 c 19 s 115 the order is within the limits on section 740.1` | 1 |

#### (a5) A list closed by "only"

- **Reading taken:** JUST FALSE outside the closed limit ("applies only to ... on or after the day").
- **Other reading:** NOTHING: see F12.
- **Status:** the brief's rule (a list closed with "only").
- **Sites:** 15 branches in 15 functions.

| function | branches |
| --- | --- |
| `s 696.5(3) (not in force) the condition for deciding under section 696.6 without an investigation is met` | 1 |
| `s 696.5(8) (not in force) the condition for deciding under section 696.6 after an investigation is met` | 1 |
| `s 696.6(4) (not in force) the Commission may take the step` | 1 |
| `2009 c 29 s 5 the person is within the limit on subsections 719(3) to (3.4)` | 1 |
| `2015 c 13 s 40 the conduct is within the limit on section 423.1` | 1 |
| `2015 c 13 s 42 the conduct is within the limit on the amendments to section 718` | 1 |
| `2015 c 13 s 42.1 the conduct is within the limit on the amendment to paragraph 718.2(e)` | 1 |
| `2015 c 13 s 44 the conduct is within the limit on section 737.1 and sections 739.1 to 739.4` | 1 |
| `2026 c 11 s 58(1) the offence is within the limit on the provisions enacted by sections 8, 9, 11, 37, 40 and 43` | 1 |
| `2026 c 19 s 97 the act or omission is within the time limit on subsection 7(4.1)` | 1 |
| `2026 c 19 s 100 the offence is within the time limit on the provisions of sections 276, 276.01 to 276.13 and 278.1 to 278.38 named by this section` | 1 |
| `2026 c 19 s 105 the offence is within the time limit on Part XV.1` | 1 |
| `2026 c 19 s 114 the offence is within the time limit on section 729.2` | 1 |
| `2026 c 19 s 115 the order is within the limits on section 740.1` | 1 |
| `2026 c 19 s 116 the offence is within the time limit on section 752.01` | 1 |

#### (a6) A "means" definition

- **Reading taken:** JUST FALSE for a thing outside the definition ("means" closes it).
- **Other reading:** NOTHING for a term the definition does not mention.
- **Status:** the brief's rule (a "means" definition).
- **Sites:** 8 branches in 8 functions.

| function | branches |
| --- | --- |
| `2024 c 33 s 7 "applicant"` | 1 |
| `2024 c 33 s 7 "Commission"` | 1 |
| `2024 c 33 s 7 "Minister"` | 1 |
| `2024 c 33 s 7 "old scheme"` | 1 |
| `s 696.1 "applicant" (not in force)` | 1 |
| `s 696.1 "Commission" (not in force)` | 1 |
| `s 696.1 "court of appeal" (not in force)` | 1 |
| `2026 c 19 s 96 Act` | 1 |

### (b) A prohibition or grant limited by its own wording does not give a "no"

#### (b) NOTHING where the grant, application or prohibition is limited by its own wording and the case falls outside the limit

- **Reading taken:** NOTHING (`-- NOTHING-kind (limited by its own wording)`), for example a matter that is not ongoing, an order made after the day, a person who is not in the class named.
- **Other reading:** JUST FALSE: the provision applies only to the case it describes, so it does not apply to any other.
- **Status:** for a lawyer (brief, reading (b)); the periods ruling (c) governs a scope limit with no "only".
- **Sites:** 135 branches in 122 functions.

| function | branches |
| --- | --- |
| `2018 c 16 s 190 subsection 737(1) is replaced by the following` | 1 |
| `s 737(1) (not in force) the offender shall pay a victim surcharge for each offence` | 1 |
| `s 743.2 (not in force) the court shall forward the item to the Correctional Service of Canada` | 1 |
| `s 679(7) (not in force) section 679 applies to the release or detention of the person as though the person were an appellant in an appeal described in paragraph (1)(a)` | 1 |
| `s 264.01(1) (not in force) the accused commits an offence` | 2 |
| `s 264.01(2)(a) (not in force) the act is within paragraph (a)` | 2 |
| `s 264.01(2)(b) (not in force) the act is within paragraph (b)` | 1 |
| `s 490.02(3) (not in force) the day before which the provision referred to is read` | 1 |
| `s 490.022(4) (not in force) the day before which the definition referred to is read` | 1 |
| `s 490.04(1) (not in force) the order or obligation is one listed in paragraph (a), (a.1) or (b)` | 2 |
| `s 490.04(2) (not in force) the person is permitted to apply under paragraph (1)(b)` | 1 |
| `s 490.04(4) (not in force) the court may make an exemption order` | 2 |
| `s 490.04(8) (not in force) the court shall also make an order requiring the Royal Canadian Mounted Police to permanently remove the information from the database` | 1 |
| `s 490.06(2) (not in force) the appeal court shall also make an order requiring the Royal Canadian Mounted Police to permanently remove the information from the database` | 1 |
| `2024 c 33 s 7 the definitions apply in the section` | 1 |
| `2024 c 33 s 9 the Minister is authorized to disclose to the Commission all information pertaining to the application that is under the Minister’s control` | 1 |
| `2024 c 33 s 10(2) the old scheme continues to apply in respect of the application` | 1 |
| `2024 c 33 s 10(3) the application is deemed not to have been made` | 1 |
| `2024 c 33 s 10(3) the applicant may apply to the Commission under the new scheme` | 2 |
| `2024 c 33 s 11 the Minister is authorized to disclose to the Commission all information pertaining to the application that is under the Minister’s control` | 1 |
| `2024 c 33 s 12 the consent may be revoked` | 1 |
| `2024 c 33 s 13 the fact that the Minister dismissed the application under the old scheme prevents the applicant from applying under the new scheme` | 1 |
| `s 696.1 (not in force) the definitions apply in the provision` | 1 |
| `s 696.2(1) (not in force) an application for a review on the grounds of miscarriage of justice may be made to the Commission by or on behalf of the person` | 1 |
| `s 696.3(1) (not in force) the Commission owes the applicant the duty to deal with the application as expeditiously as possible and to provide regular updates` | 1 |
| `s 696.3(2) (not in force) the notice or information may be provided to a representative of the applicant in addition to or instead of the applicant` | 1 |
| `s 696.4(1) (not in force) the Commission owes the duty to decide whether the application is admissible` | 1 |
| `s 696.4(4) (not in force) the Commission may decide that the application is admissible despite subsection (3)` | 1 |
| `s 696.4(4) (not in force) the Commission must take the factor into account` | 1 |
| `s 696.4(5) (not in force) the Commission owes the duty to notify the applicant and the relevant Attorney General of its decision on admissibility` | 1 |
| `s 696.5(1) (not in force) the Commission may conduct an investigation in relation to the application` | 1 |
| `s 696.5(4) (not in force) the Commission has the powers of a commissioner under Part I of the Inquiries Act` | 1 |
| `s 696.5(5) (not in force) the Commission may authorize the person to exercise the powers referred to in subsection (4)` | 1 |
| `s 696.5(6) (not in force) the Commission owes the duty to prepare a report and provide a copy of it` | 1 |
| `s 696.5(7) (not in force) the report must specify a reasonable period within which a written response may be provided` | 1 |
| `s 696.5(8) (not in force) the condition for deciding under section 696.6 after an investigation is met` | 1 |
| `s 696.6(1) (not in force) the Commission owes the duty to make a decision on the application` | 1 |
| `s 696.6(4) (not in force) the Commission may take the step` | 1 |
| `s 696.6(5) (not in force) the Commission must take the factor into account` | 1 |
| `s 696.6(6) (not in force) the Commission may grant a remedy under subsection (2) even if the evidence does not establish the innocence of the applicant` | 1 |
| `s 696.6(7) (not in force) the Commission owes the duty to notify the applicant and the relevant Attorney General of its decision` | 1 |
| `s 696.61 (not in force) the Commission may refer the question to the court of appeal for its opinion` | 1 |
| `s 696.61 (not in force) the court of appeal must provide its opinion on the question` | 1 |
| `s 696.72 (not in force) the application is within the Commission’s mandate` | 1 |
| `1991 c 43 s 10(1) the order for detention continues in force` | 2 |
| `1991 c 43 s 10(3) the section applies, with such modifications as the circumstances require, to the review` | 1 |
| `1991 c 43 s 10(3)(a) the review is treated as a review of a disposition conducted under section 672.81` | 1 |
| `1991 c 43 s 10(3)(b) the warrant is treated as a disposition made under section 672.54` | 1 |
| `2004 c 12 s 22 the reference is read as referring to` | 1 |
| `2004 c 12 s 23 the reference is read as referring to` | 1 |
| `2011 c 2 s 7(1) the application is dealt with and disposed of under the Code as it read immediately before that day` | 1 |
| `2011 c 2 s 7(2) the person may make an application under subsection 745.6(1) as amended` | 1 |
| `2011 c 2 s 7(3) the person may make an application under subsection 745.6(1) as amended` | 1 |
| `2012 c 1 s 163(a) the reference to an application for a record suspension is also a reference to an application for a pardon` | 2 |
| `2012 c 1 s 165(b) the reference to a record suspension is also a reference to a pardon` | 2 |
| `2015 c 13 s 37 subsection 278.3(5) as it read immediately before that day continues to apply to the hearing` | 1 |
| `2015 c 13 s 38 section 380.3 as it read immediately before that day continues to apply to the request for restitution` | 1 |
| `2015 c 13 s 39 section 380.4 as it read immediately before that day continues to apply to the statement` | 1 |
| `2015 c 13 s 41 section 672.5 as it read immediately before that day continues to apply to the statement` | 1 |
| `2015 c 13 s 43 section 722 as it read immediately before that day continues to apply to the statement` | 1 |
| `2018 c 12 s 406(1) a remediation agreement may be entered into in respect of the offence` | 1 |
| `2018 c 12 s 406(2) the term has the meaning it has in section 715.3` | 1 |
| `2018 c 21 s 10 the thing is deemed to be approved, as the same kind of thing, under section 254.01 as enacted by section 4` | 2 |
| `2018 c 21 s 32(1) section 320.34 as enacted by section 15 applies to the application` | 1 |
| `2018 c 21 s 32(2) subsection 320.31(1) as enacted by section 15 applies to the trial` | 1 |
| `2018 c 21 s 33 section 320.36 as enacted by section 15 applies to the thing` | 2 |
| `2018 c 21 s 34(1) an appeal may be taken against the order` | 1 |
| `2018 c 21 s 34(1) the appeal is taken under section 675 and disposed of under the provisions of the Act, each as it read immediately before that day` | 1 |
| `2018 c 21 s 34(2) sections 261 and 680 as they read immediately before that day apply to the appeal` | 1 |
| `2018 c 21 s 35 the thing is deemed to be approved, as the same kind of thing, under section 320.39 as enacted by section 15` | 2 |
| `2018 c 21 s 36 the person is deemed to be designated as a qualified technician under paragraph 320.4(a)` | 1 |
| `2018 c 21 s 37 the person is deemed to be designated as a qualified technician under subparagraph 320.4(b)(i)` | 1 |
| `2018 c 21 s 38 the person is deemed to be designated as an analyst under subparagraph 320.4(b)(ii) and paragraph 320.4(c)` | 1 |
| `2018 c 29 s 74 subsection 278.3(5) as it read immediately before that day continues to apply to the hearing` | 1 |
| `2019 c 13 s 155 paragraph 83.05(1)(b) and subsection 83.05(3) as they read immediately before that day continue to apply to the application` | 1 |
| `2019 c 13 s 156 the proceedings are to be completed under sections 83.28 and 83.29 as they read before that day` | 1 |
| `2019 c 13 s 157 a report is to be prepared under subsection 810.011(15)` | 1 |
| `2019 c 25 s 354 the person is deemed to be bound by an appearance notice as defined in section 2` | 1 |
| `2019 c 25 s 355 the person is deemed to be bound by an undertaking as defined in section 2` | 1 |
| `2019 c 25 s 356 the person is deemed to be bound by an undertaking as defined in section 2` | 1 |
| `2019 c 25 s 357 the person is deemed to be bound by a release order as defined in section 2` | 1 |
| `2019 c 25 s 358 the person is deemed to be bound by a release order as defined in section 2` | 1 |
| `2019 c 25 s 359 the person may elect another mode of trial` | 2 |
| `2019 c 25 s 360 the proceedings are within the time limit` | 1 |
| `2021 c 2 s 4 the provider must provide it in accordance with the old section 241.2 and subsections 241.2(3.2) to (3.5)` | 1 |
| `2022 c 17 s 77(1) the Criminal Code as it read immediately before that day continues to apply` | 2 |
| `2022 c 17 s 78 section 489.1 as it read immediately before that day continues to apply to the thing seized` | 1 |
| `2022 c 17 s 76 the amendments made by 2022, c. 17 apply to the proceedings, subject to sections 77 and 78` | 1 |
| `2023 c 26 s 613 the word or expression has the meaning it has in sections 347 and 347.1` | 1 |
| `2023 c 26 s 614 the definition criminal rate in subsection 347(2), as it reads on that day, applies to the receipt` | 1 |
| `2023 c 26 s 615 paragraph 347.1(2)(a.1), as it reads on that day, applies to the person` | 1 |
| `2023 c 30 s 3 the amendments made by 2023, c. 30 apply to the matter or proceeding` | 1 |
| `2023 c 32 s 14.1 paragraph (e) of the definition prohibited firearm applies to the firearm in relation to those proceedings` | 1 |
| `2024 c 23 s 13 the amendments made by 2024, c. 23 affect the validity of the proceedings` | 1 |
| `2024 c 23 s 13 the amendments made by 2024, c. 23 affect the validity of the document` | 1 |
| `2024 c 23 s 13 the reference to child pornography in the document is read as a reference to` | 1 |
| `2026 c 11 s 56 the word or expression has the same meaning as in the Criminal Code` | 1 |
| `2026 c 11 s 57 the provisions of the Criminal Code enacted by sections 41 and 42 apply to the proceeds of the fine` | 1 |
| `2026 c 11 s 58(2) the amendments to Parts XVI and XXVIII made by 2026, c. 11 apply to the matter or proceeding` | 1 |
| `2026 c 11 s 58(3) the provisions enacted by sections 10, 34 to 36, 38 and 39 of 2026, c. 11 apply to the matter or proceeding` | 1 |
| `2026 c 12 s 15 subsection 236(2) applies to the offence` | 1 |
| `2026 c 12 s 16 subsection 490(2) as amended by section 3 of 2026, c. 12 applies to the matter or proceeding` | 1 |
| `2026 c 15 s 11.1(1) the clarification applies to the person's communication of the statement` | 1 |
| `2026 c 15 s 11.1(2) the clarification applies to the person's communication of the statement` | 1 |
| `2026 c 19 s 87 the operation of the minimum punishment is affirmed following the enactment of section 718.4` | 1 |
| `2026 c 19 s 96 the definitions apply in the section` | 1 |
| `2026 c 19 s 98 paragraphs 236(2)(b) to (d) apply to the offence` | 1 |
| `2026 c 19 s 99 paragraph 264(4)(a) applies to the matter or proceeding` | 1 |
| `2026 c 19 s 101 subsection 346(1.4) applies to the matter or proceeding` | 1 |
| `2026 c 19 s 102 sections 486.1, 486.2 and 486.3 as amended by sections 38, 39 and 40 of 2026, c. 19 apply to the matter or proceeding` | 1 |
| `2026 c 19 s 103 subsection 489.1(4) applies to the matter or proceeding` | 1 |
| `2026 c 19 s 106 subsection 507.1(9) as enacted by section 47 of 2026, c. 19 applies to the matter or proceeding` | 1 |
| `2026 c 19 s 107 paragraphs 515(3)(a) and (b), (4.1)(a), (4.3)(c) and (6)(b.1) and (b.2), as construed in application of section 3.01, apply to the matter or proceeding` | 1 |
| `2026 c 19 s 108 subsections 537(1.001), 571(2), 645(3.1), 803(1.1) and 824(2) apply to the matter or proceeding` | 1 |
| `2026 c 19 s 109 section 657.4 applies to the matter or proceeding` | 1 |
| `2026 c 19 s 110 section 672.5011 applies to the order` | 1 |
| `2026 c 19 s 111(1) the measure is deemed to be an alternative measure, as defined in section 715.44` | 1 |
| `2026 c 19 s 111(2) the provisions enacted by sections 59, 64 and 65 of 2026, c. 19 apply to the matter or proceeding` | 1 |
| `2026 c 19 s 112 sections 722 and 722.2 as amended by sections 66 and 67 of 2026, c. 19 apply to the matter or proceeding` | 1 |
| `2026 c 19 s 113 section 726.21 applies to the matter or proceeding` | 1 |
| `2026 c 19 s 117 section 810.03 as amended by section 81 of 2026, c. 19 applies to the matter or proceeding` | 1 |
| `2026 c 19 s 118 section 810.1 as amended by section 82 of 2026, c. 19 applies to the matter or proceeding` | 1 |

#### (b2) Name-test flips of 2026-11-12: a function named for a grant or power that now answers NOTHING where its "if" gate fails

- **Reading taken:** NOTHING (a grant limited by its own wording: Guide section 5, "In short").
- **Other reading:** JUST FALSE (a failed "if" read as the text's own no), as it was before the sweep.
- **Sites:** F21 `2024 c 33 s 9` (authorized to disclose); F22 `2024 c 33 s 11` (authorized to disclose); F23 `2024 c 33 s 10(3)` (the applicant may apply); F24 `s 696.5(1) (not in force)` (the Commission may conduct an investigation); F25 `2019 c 25 s 359` (a person who has already elected).

### Other NOTHING branches (not marginal: the text gives no "no")

- `points outside the text`: 16 branches in 14 functions.
- `list not closed`: 4 branches in 4 functions.
- `silent`: 3 branches in 3 functions.
- `includes`: 3 branches in 3 functions.
- `undefined term`: 1 branches in 1 functions.

## Seams (ccc32)

Each seam input taken, as PLAN.md names it, and the seams found that the plan lacks.
A seam input is a `MAYBE BOOLEAN` that another part or another Act answers; the rule treats `JUST TRUE` as yes, `JUST FALSE` as no and `NOTHING` as not covered; the seat asks it as a yes or no and passes it on as `JUST`.

| input (as named in the module) | taken from | plan or found | where used |
| --- | --- | --- | --- |
| `s 2 intimate partner: the person at risk is the other person's intimate partner` and `... is a child of the other person's intimate partner` | s 2 "intimate partner" (PLAN.md section 6, ccc32 row: `intimate partner` (33)) | plan | `2024 c 22 s 8 the information is deemed to have been laid under subsection 810.03(1)` |
| `s 2 intimate partner: the person subjected to the pattern is the accused's intimate partner` | s 2 "intimate partner" | plan | `s 264.01(1) (not in force) the accused commits an offence` |
| `s 2 the word or expression is within the meaning it has in the Criminal Code` | s 2 (the Code's definitions) | found (plan lists `day`, `justice`, `firearm`, `court of appeal`, `Attorney General`, `prohibited firearm`, none of which a rule here turns on) | `2026 c 11 s 56 the word or expression has the same meaning as in the Criminal Code` |
| `s 715.3 the thing is within the meaning that remediation agreement or offence has` | s 715.3, as enacted by section 404 of 2018, c. 12 (outside this range; not among the plan's seams) | found | `2018 c 12 s 406(2)` |
| `s 347 the word or expression is within the meaning it has in sections 347 and 347.1` | ss 347, 347.1 (outside this range) | found | `2023 c 26 s 613` |
| `s 561 the person is in one of the cases described in subparagraph 561(1)(b)(i) or subsection 561(2) or 561.1(2) as enacted by 2019, c. 25` | s 561 (mode of trial; ccc21) | found | `2019 c 25 s 359` |
| `s 737(1.1) subsection 737(1.1) relieves the offender of the surcharge` | s 737(1.1), in-force text of ccc27 outside this range (the replaced subsection (1) is "subject to subsection (1.1)") | found | `s 737(1) (not in force) the offender shall pay a victim surcharge for each offence` |
| `s 490.04(4)(b) before or after the order was made, the person did what subparagraphs (b)(i) and following describe` | the in-force text of paragraph 490.04(4)(b), which the replacement leaves unchanged (ccc18) | found | `s 490.04(4) (not in force) the court may make an exemption order` |
| `s 787(1) the general penalty for an offence punishable on summary conviction` (a `Punishment`) | s 787(1) (ccc29): section 264.01(4)(b) states no penalty for the summary limb | found | `s 264.01(4) (not in force) the punishment for the offence` |

Not seams but worth saying: the lists that section 264.01 is added to (3.01(1), 109(1), 183 "offence", 487.04 "secondary designated offence", 490.011(1) "secondary offence") are other parts' in-force lists; this part answers only whether the added item matches (`s 3.01(1)(b.1) (not in force) ...`, `s 109(1)(b) (not in force) ...` and so on), and `s 109(1)(b)` answers JUST TRUE for the offences it names in this replacement text (subsection 85(1) and the rest of the paragraph's list), which another part's in-force paragraph 109(1)(b) does not replace.
The cross-references into the Code that the transitional rules name by section (672.35, 750, 490.011, 499, 503, 515 ...) are `Provision of the Code` values: the seat asks them as a section number and a subsection string.

## The seat layer (ccc32)

`ccc32-seat.l4` has 147 questions under 7 `§` headings, in the text's order, each with `@export` and an `@desc` on every input; `ccc32-cases-seat.l4` has 231 cases, every question at least once, with the expected value written by hand from the provision.
The seat is a person who is, or may be, accused of an offence under the Criminal Code; this range holds the transitional rules for that person (which text governs when they were detained, charged, tried or sentenced around a change) and future text (a new offence, a new review of convictions, a new surcharge).
Questions about not-in-force text sit under headings that say so.
Provisions that address only an official have no question unless they mean something to the accused; reviews, coordinating clauses and Form 52 are inert and have none.
Assumed, not ruled: Singapore's Penal Code is the model the brief names; this seat layer has no charge-generator contract.
Each question is generated by a script from a table of one-line facts; the layer-1 rule is called by name and never restated.

51 of the 198 layer-1 functions have no seat question:

| function | why no question |
| --- | --- |
| `2018 c 16 s 190 subsection 737(1) is replaced by the following` | an amending instruction (no fact about the person decides it) |
| `2021 c 2 s 1(2.1) subsection 241.2(2.1) is repealed` | an amending instruction (no fact about the person decides it) |
| `s 743.2 (not in force) the court shall forward the item to the Correctional Service of Canada` | a step inside section 743.2: the court's duty to the Correctional Service of Canada (official-only) |
| `s 743.2 (not in force) the court must forward the reasons, reports, information and victim contact details to the Correctional Service of Canada` | a regulative rule: not exported (a DEONTIC value is not a seat answer); where a question exists for the duty, it calls the rule's decision twin |
| `s 490.02(3) (not in force) the day before which the provision referred to is read` | a reading rule (which text or meaning a reference takes): no fact about the person decides it; the borrowed fact is a seam input of the questions that use it |
| `s 490.022(4) (not in force) the day before which the definition referred to is read` | a reading rule (which text or meaning a reference takes): no fact about the person decides it; the borrowed fact is a seam input of the questions that use it |
| `s 490.05(5) (not in force) the provision applied to the offence in question with the longest maximum term of imprisonment` | a reading rule (which text or meaning a reference takes): no fact about the person decides it; the borrowed fact is a seam input of the questions that use it |
| `2024 c 33 s 7 the definitions apply in the section` | a definition (it answers what a term means, not a fact about the person) |
| `2024 c 33 s 7 "applicant"` | a definition (it answers what a term means, not a fact about the person) |
| `2024 c 33 s 7 "commencement day"` | a definition (it answers what a term means, not a fact about the person) |
| `2024 c 33 s 7 "Commission"` | a definition (it answers what a term means, not a fact about the person) |
| `2024 c 33 s 7 "Minister"` | a definition (it answers what a term means, not a fact about the person) |
| `2024 c 33 s 7 "new scheme"` | a definition (it answers what a term means, not a fact about the person) |
| `2024 c 33 s 7 "old scheme"` | a definition (it answers what a term means, not a fact about the person) |
| `2024 c 33 s 8 the Minister must ask the applicant whether they consent to the transfer` | a regulative rule: not exported (a DEONTIC value is not a seat answer); where a question exists for the duty, it calls the rule's decision twin |
| `2024 c 33 s 3 Part XXI.1 is replaced by the following` | an amending instruction (no fact about the person decides it) |
| `s 696.1 (not in force) the definitions apply in the provision` | a definition (it answers what a term means, not a fact about the person) |
| `s 696.1 "applicant" (not in force)` | a definition (it answers what a term means, not a fact about the person) |
| `s 696.1 "Commission" (not in force)` | a definition (it answers what a term means, not a fact about the person) |
| `s 696.1 "court of appeal" (not in force)` | a definition (it answers what a term means, not a fact about the person) |
| `s 696.3(1) (not in force) the Commission must deal with the application as expeditiously as possible` | a regulative rule: not exported (a DEONTIC value is not a seat answer); where a question exists for the duty, it calls the rule's decision twin |
| `s 696.3(1) (not in force) the Commission must provide the applicant with an update on a regular basis` | a regulative rule: not exported (a DEONTIC value is not a seat answer); where a question exists for the duty, it calls the rule's decision twin |
| `s 696.4(1) (not in force) the Commission must decide whether the application is admissible` | a regulative rule: not exported (a DEONTIC value is not a seat answer); where a question exists for the duty, it calls the rule's decision twin |
| `s 696.4(1) (not in force) the Commission owes the duty to decide whether the application is admissible` | the decision twin of a regulative rule; no question written for this duty (assumed, not ruled) |
| `s 696.4(5) (not in force) the Commission must notify the applicant and the relevant Attorney General of its decision on admissibility` | a regulative rule: not exported (a DEONTIC value is not a seat answer); where a question exists for the duty, it calls the rule's decision twin |
| `s 696.5(2) (not in force) the Commission must send a notice indicating whether an investigation will be conducted` | a regulative rule: not exported (a DEONTIC value is not a seat answer); where a question exists for the duty, it calls the rule's decision twin |
| `s 696.5(5) (not in force) the Commission may authorize the person to exercise the powers referred to in subsection (4)` | a power of the Commission to authorize another: official-only |
| `s 696.5(6) (not in force) the Commission must prepare a report and provide a copy of it` | a regulative rule: not exported (a DEONTIC value is not a seat answer); where a question exists for the duty, it calls the rule's decision twin |
| `s 696.6(1) (not in force) the Commission must make a decision on the application` | a regulative rule: not exported (a DEONTIC value is not a seat answer); where a question exists for the duty, it calls the rule's decision twin |
| `s 696.6(1) (not in force) the Commission owes the duty to make a decision on the application` | the decision twin of a regulative rule; no question written for this duty (assumed, not ruled) |
| `s 696.6(7) (not in force) the Commission must notify the applicant and the relevant Attorney General of its decision` | a regulative rule: not exported (a DEONTIC value is not a seat answer); where a question exists for the duty, it calls the rule's decision twin |
| `s 696.61 (not in force) the court of appeal must provide its opinion` | a regulative rule: not exported (a DEONTIC value is not a seat answer); where a question exists for the duty, it calls the rule's decision twin |
| `s 696.61 (not in force) the court of appeal must provide its opinion on the question` | no seat question written (assumed, not ruled) |
| `s 696.7 "applicant" (not in force)` | a definition (it answers what a term means, not a fact about the person) |
| `1991 c 43 s 10(2) the Review Board must review the case` | a regulative rule: not exported (a DEONTIC value is not a seat answer); where a question exists for the duty, it calls the rule's decision twin |
| `1991 c 43 s 10(3)(a) the review is treated as a review of a disposition conducted under section 672.81` | a deeming step inside section 10(3), whose own question is asked |
| `1991 c 43 s 10(3)(b) the warrant is treated as a disposition made under section 672.54` | a deeming step inside section 10(3), whose own question is asked |
| `1991 c 43 s 10(3)(c) and (d) as the text shows them` | repealed or blank in the text (kept as a constant) |
| `1991 c 43 s 10(4) to (7) as the text shows them` | repealed or blank in the text (kept as a constant) |
| `2004 c 12 s 22 the reference is read as referring to` | a reading table for a cross-reference in a Bill (no fact about the person decides it) |
| `2004 c 12 s 23 the reference is read as referring to` | a reading table for a cross-reference in a Bill (no fact about the person decides it) |
| `2018 c 12 s 406(2) the term has the meaning it has in section 715.3` | a reading rule (which text or meaning a reference takes): no fact about the person decides it; the borrowed fact is a seam input of the questions that use it |
| `2019 c 13 s 155 paragraph 83.05(1)(b) and subsection 83.05(3) as they read immediately before that day continue to apply to the application` | a continued-application rule for a listing application (155) or an investigative hearing (156): not about a person accused of an offence (assumed, not ruled) |
| `2019 c 13 s 156 the proceedings are to be completed under sections 83.28 and 83.29 as they read before that day` | a continued-application rule for a listing application (155) or an investigative hearing (156): not about a person accused of an offence (assumed, not ruled) |
| `2019 c 13 s 157 a report is to be prepared under subsection 810.011(15)` | a report to be prepared by an official: official-only |
| `2019 c 13 s 157.1 sections 146 and 148 of 2019, c. 13 apply in respect of section 83.3` | a step inside the revival rule, whose own question is asked |
| `2021 c 2 s 4 the provider must provide medical assistance in dying in accordance with the old section 241.2` | a regulative rule: not exported (a DEONTIC value is not a seat answer); where a question exists for the duty, it calls the rule's decision twin |
| `2023 c 26 s 613 the word or expression has the meaning it has in sections 347 and 347.1` | a reading rule (which text or meaning a reference takes): no fact about the person decides it; the borrowed fact is a seam input of the questions that use it |
| `2026 c 11 s 56 the word or expression has the same meaning as in the Criminal Code` | a reading rule (which text or meaning a reference takes): no fact about the person decides it; the borrowed fact is a seam input of the questions that use it |
| `2026 c 19 s 96 the definitions apply in the section` | a definition (it answers what a term means, not a fact about the person) |
| `2026 c 19 s 96 Act` | a definition (it answers what a term means, not a fact about the person) |

### Seat audit of 2026-11-12

The lead asked for every seat question's name and `@export` text to be read against the layer-1 function its body calls, for a mismatch of direction (a permission named over a bar, or the reverse) or of subject ("must I" over "have I", "does it apply" over "is it within the limit").
I read all 147 questions.
Direction mismatches found: 0.
Subject mismatches found: 23; 18 names and 17 `@export` texts were retitled, and no `@desc` needed to change (each describes a fact, not the question).
The functions and their answers were not changed, and no answer was negated: a bar's NOTHING and JUST FALSE are not a grant.
32 assertions in `ccc32-cases-seat.l4` named a retitled question and are restated in place with a `-- RECONCILED 2026-11-12: was ...; reason` comment above the new assertion (the facts and the expected values did not change); the assertion count stays 231.

What was wrong, by kind:
- **"applies" over "is within the limit"** (11 questions: 2009 c 29 s 5; 2015 c 13 ss 40, 42, 42.1, 44; 2026 c 11 s 58(1); 2026 c 19 ss 100, 105, 114, 115, 116). The text says a provision "applies only" to later conduct or charges, and the function answers whether the case is within that limit, which is a necessary condition and not a statement that the provision applies. Six names and all eleven `@export` texts now say "within the limit"; five of the eleven already had a correct name and an `@export` text that asked "apply".
- **"protect" over "the clarification applies"** (2026 c 15 s 11.1(1) and (2)): a failed clarification was readable as "not protected", i.e. as a prohibition under section 319, which the function does not say.
- **"must give" over "must give in accordance with"** (section 4 of 2021 c 2): the duty is about the manner in which the provider gives medical assistance in dying, not a duty to give it.
- **"can the Commission decide" over "is the condition met"** (ss 696.5(3) and (8)): the text says "only if", a necessary condition.
- **"what may the Commission do" over "may the Commission take this step"** (s 696.6(4)).
- **A consequence or a whole definition named over a listing or a paragraph** (s 490.04(1) "may apply" over "is listed"; s 109(1)(b) "leads to a firearms prohibition" over "is listed"; the 264.01 additions to ss 183, 487.04 and 490.011(1), where the definition has further limbs, for example a secondary designated offence is an offence "other than a primary designated offence"; s 87 of 2026 c 19 "still in operation" over "affirmed").

Examined and left unchanged, for the lead and the lawyer:
- Questions over a function that is named in the positive and answers JUST FALSE for a flat negative in the text (2026 c 12 s 15, 2026 c 19 s 98, 2023 c 26 ss 614 and 615, 2023 c 32 s 14.1, 2024 c 23 s 13 twice, 2024 c 33 ss 12 and 13): the question and the function ask the same thing, so JUST FALSE reads "no" and there is no JUST TRUE to misread.
- Two questions are titled as a permission over a function that encodes a bar and can answer only JUST FALSE (the text says no) or NOTHING (the text is silent): s 490.04(2) "am I permitted to apply" and s 490.04(4) "may the court make an exemption order". The direction is consistent (JUST FALSE means "no"), and retitling either to the bar would invert JUST FALSE, so they stand. The layer-1 names `... is permitted ...` and `... may make ...` for a "shall not" are misleading, and renaming a layer-1 function was outside the audit.

### The seat questions, in order

| # | question | layer-1 function |
| --- | --- | --- |
| 1 | Under section 10(1) of 1991 c 43, does my detention order made by a lieutenant governor's warrant stay in force | `1991 c 43 s 10(1) the order for detention continues in force` |
| 2 | Under section 10(2) of 1991 c 43, was the Review Board's review of my case within twelve months | `1991 c 43 s 10(2) the review was within twelve months after the coming into force` |
| 3 | Under section 10(3) of 1991 c 43, does a given section of the Criminal Code apply to the Review Board's review of my case | `1991 c 43 s 10(3) the section applies, with such modifications as the circumstances require, to the review` |
| 4 | Under section 5 of 2009 c 29, am I within the limit on subsections 719(3) to (3.4) because of when I was charged | `2009 c 29 s 5 the person is within the limit on subsections 719(3) to (3.4)` |
| 5 | Under section 7(1) of 2011 c 2, is my application under section 745.6 dealt with under the old law | `2011 c 2 s 7(1) the application is dealt with and disposed of under the Code as it read immediately before that day` |
| 6 | Under section 7(2) of 2011 c 2, may I make a new application under section 745.6(1) now | `2011 c 2 s 7(2) the person may make an application under subsection 745.6(1) as amended` |
| 7 | Under section 7(3) of 2011 c 2, may I make a new application under section 745.6(1) after a time set for me has ended | `2011 c 2 s 7(3) the person may make an application under subsection 745.6(1) as amended` |
| 8 | Under section 163(a) of 2012 c 1, is a reference to an application for a record suspension also a reference to my pardon application | `2012 c 1 s 163(a) the reference to an application for a record suspension is also a reference to an application for a pardon` |
| 9 | Under section 165(b) of 2012 c 1, is a reference to a record suspension in the Code also a reference to my pardon | `2012 c 1 s 165(b) the reference to a record suspension is also a reference to a pardon` |
| 10 | Under section 37 of 2015 c 13, does the old subsection 278.3(5) still apply to my hearing | `2015 c 13 s 37 subsection 278.3(5) as it read immediately before that day continues to apply to the hearing` |
| 11 | Under section 38 of 2015 c 13, does the old section 380.3 still apply to a request for restitution made against me | `2015 c 13 s 38 section 380.3 as it read immediately before that day continues to apply to the request for restitution` |
| 12 | Under section 39 of 2015 c 13, does the old section 380.4 still apply to a community impact statement filed in my case | `2015 c 13 s 39 section 380.4 as it read immediately before that day continues to apply to the statement` |
| 13 | Under section 40 of 2015 c 13, is what I did within the limit on section 423.1 as amended | `2015 c 13 s 40 the conduct is within the limit on section 423.1` |
| 14 | Under section 41 of 2015 c 13, does the old section 672.5 still apply to a victim impact statement filed before the change | `2015 c 13 s 41 section 672.5 as it read immediately before that day continues to apply to the statement` |
| 15 | Under section 42 of 2015 c 13, is the conduct I may be sentenced for within the limit on the amendments to section 718 | `2015 c 13 s 42 the conduct is within the limit on the amendments to section 718` |
| 16 | Under section 42.1 of 2015 c 13, is the conduct I may be sentenced for within the limit on the amendment to paragraph 718.2(e) | `2015 c 13 s 42.1 the conduct is within the limit on the amendment to paragraph 718.2(e)` |
| 17 | Under section 43 of 2015 c 13, does the old section 722 still apply to a victim impact statement filed before the change | `2015 c 13 s 43 section 722 as it read immediately before that day continues to apply to the statement` |
| 18 | Under section 44 of 2015 c 13, is what I did within the limit on section 737.1 and sections 739.1 to 739.4 | `2015 c 13 s 44 the conduct is within the limit on section 737.1 and sections 739.1 to 739.4` |
| 19 | Under section 28 of 2015 c 20, is an information against me under section 810.01(1) treated as laid under section 810.011(1) | `2015 c 20 s 28 the information is deemed to have been laid under subsection 810.011(1)` |
| 20 | Under section 406(1) of 2018 c 12, may a remediation agreement be entered into for an offence alleged to have been committed before section 404 came into force | `2018 c 12 s 406(1) a remediation agreement may be entered into in respect of the offence` |
| 21 | Under section 10 of 2018 c 21, is the screening device, instrument or container used on me treated as approved under section 254.01 | `2018 c 21 s 10 the thing is deemed to be approved, as the same kind of thing, under section 254.01 as enacted by section 4` |
| 22 | Under section 32(1) of 2018 c 21, does section 320.34 apply to my application for disclosure of further information | `2018 c 21 s 32(1) section 320.34 as enacted by section 15 applies to the application` |
| 23 | Under section 32(2) of 2018 c 21, does subsection 320.31(1) apply to my trial | `2018 c 21 s 32(2) subsection 320.31(1) as enacted by section 15 applies to the trial` |
| 24 | Under section 33 of 2018 c 21, does section 320.36 apply to the bodily substances and test results taken from me | `2018 c 21 s 33 section 320.36 as enacted by section 15 applies to the thing` |
| 25 | Under section 34(1) of 2018 c 21, may I appeal an order made against me under the old section 259 | `2018 c 21 s 34(1) an appeal may be taken against the order` |
| 26 | Under section 34(1) of 2018 c 21, is my appeal taken and decided under the old law | `2018 c 21 s 34(1) the appeal is taken under section 675 and disposed of under the provisions of the Act, each as it read immediately before that day` |
| 27 | Under section 34(2) of 2018 c 21, do the old sections 261 and 680 apply to my appeal and any stay | `2018 c 21 s 34(2) sections 261 and 680 as they read immediately before that day apply to the appeal` |
| 28 | Under section 35 of 2018 c 21, is the equipment used on me treated as approved under section 320.39 | `2018 c 21 s 35 the thing is deemed to be approved, as the same kind of thing, under section 320.39 as enacted by section 15` |
| 29 | Under section 36 of 2018 c 21, is the person who took my breath sample treated as a qualified technician under section 320.4(a) | `2018 c 21 s 36 the person is deemed to be designated as a qualified technician under paragraph 320.4(a)` |
| 30 | Under section 37 of 2018 c 21, is the person who took my blood sample treated as a qualified technician under section 320.4(b)(i) | `2018 c 21 s 37 the person is deemed to be designated as a qualified technician under subparagraph 320.4(b)(i)` |
| 31 | Under section 38 of 2018 c 21, is the person who analysed my sample treated as an analyst under section 320.4 | `2018 c 21 s 38 the person is deemed to be designated as an analyst under subparagraph 320.4(b)(ii) and paragraph 320.4(c)` |
| 32 | Under section 74 of 2018 c 29, does the old subsection 278.3(5) still apply to my hearing | `2018 c 29 s 74 subsection 278.3(5) as it read immediately before that day continues to apply to the hearing` |
| 33 | Under section 157.1 of 2019 c 13, does section 83.3 (the terrorism recognizance with arrest) become effective again | `2019 c 13 s 157.1 section 83.3 becomes effective again as of the day on which this section comes into force` |
| 34 | Under section 354 of 2019 c 25, am I treated as bound by an appearance notice because I gave a promise to appear | `2019 c 25 s 354 the person is deemed to be bound by an appearance notice as defined in section 2` |
| 35 | Under section 355 of 2019 c 25, am I treated as bound by an undertaking as defined in section 2 because I gave an undertaking to a peace officer | `2019 c 25 s 355 the person is deemed to be bound by an undertaking as defined in section 2` |
| 36 | Under section 356 of 2019 c 25, am I treated as bound by an undertaking as defined in section 2 because I entered into a recognizance before a peace officer | `2019 c 25 s 356 the person is deemed to be bound by an undertaking as defined in section 2` |
| 37 | Under section 357 of 2019 c 25, am I treated as bound by a release order because I gave an undertaking to a judge or justice | `2019 c 25 s 357 the person is deemed to be bound by a release order as defined in section 2` |
| 38 | Under section 358 of 2019 c 25, am I treated as bound by a release order because I entered into a recognizance before a judge or justice | `2019 c 25 s 358 the person is deemed to be bound by a release order as defined in section 2` |
| 39 | Under section 359 of 2019 c 25, may I elect another mode of trial | `2019 c 25 s 359 the person may elect another mode of trial` |
| 40 | Under section 360 of 2019 c 25, are proceedings against me for a summary conviction offence within the six-month limit | `2019 c 25 s 360 the proceedings are within the time limit` |
| 41 | Under section 4 of 2021 c 2, must a provider who gives me medical assistance in dying give it in accordance with the old section 241.2 | `2021 c 2 s 4 the provider must provide it in accordance with the old section 241.2 and subsections 241.2(3.2) to (3.5)` |
| 42 | Under section 77(1) of 2022 c 17, does the old Criminal Code continue to apply to my authorization, warrant or application | `2022 c 17 s 77(1) the Criminal Code as it read immediately before that day continues to apply` |
| 43 | Under section 78 of 2022 c 17, does the old section 489.1 continue to apply to what was seized from me | `2022 c 17 s 78 section 489.1 as it read immediately before that day continues to apply to the thing seized` |
| 44 | Under section 76 of 2022 c 17, do the amendments made by 2022 c 17 apply to my ongoing proceedings | `2022 c 17 s 76 the amendments made by 2022, c. 17 apply to the proceedings, subject to sections 77 and 78` |
| 45 | Under section 614 of 2023 c 26, does the new definition of criminal rate apply to interest I received under an older agreement | `2023 c 26 s 614 the definition criminal rate in subsection 347(2), as it reads on that day, applies to the receipt` |
| 46 | Under section 615 of 2023 c 26, does paragraph 347.1(2)(a.1) apply to me because of a payday loan agreement | `2023 c 26 s 615 paragraph 347.1(2)(a.1), as it reads on that day, applies to the person` |
| 47 | Under section 3 of 2023 c 30, do the amendments made by 2023 c 30 apply to my ongoing proceedings | `2023 c 30 s 3 the amendments made by 2023, c. 30 apply to the matter or proceeding` |
| 48 | Under section 14.1 of 2023 c 32, does paragraph (e) of the definition prohibited firearm apply to a firearm in my proceedings | `2023 c 32 s 14.1 paragraph (e) of the definition prohibited firearm applies to the firearm in relation to those proceedings` |
| 49 | Under section 8 of 2024 c 22, is an information laid against me under section 810(1) treated as laid under section 810.03(1) | `2024 c 22 s 8 the information is deemed to have been laid under subsection 810.03(1)` |
| 50 | Under section 13 of 2024 c 23, do the amendments affect the validity of my proceedings related to section 163.1 | `2024 c 23 s 13 the amendments made by 2024, c. 23 affect the validity of the proceedings` |
| 51 | Under section 13 of 2024 c 23, do the amendments affect the validity of a document in my proceedings | `2024 c 23 s 13 the amendments made by 2024, c. 23 affect the validity of the document` |
| 52 | Under section 13 of 2024 c 23, how is a reference to child pornography in a document in my proceedings read | `2024 c 23 s 13 the reference to child pornography in the document is read as a reference to` |
| 53 | Under section 57 of 2026 c 11, do the new provisions on the proceeds of a fine apply to my unpaid fine | `2026 c 11 s 57 the provisions of the Criminal Code enacted by sections 41 and 42 apply to the proceeds of the fine` |
| 54 | Under section 58(1) of 2026 c 11, is my offence within the limit on the provisions enacted by sections 8, 9, 11, 37, 40 and 43 | `2026 c 11 s 58(1) the offence is within the limit on the provisions enacted by sections 8, 9, 11, 37, 40 and 43` |
| 55 | Under section 58(2) of 2026 c 11, do the amendments to Parts XVI and XXVIII apply to my ongoing bail matter | `2026 c 11 s 58(2) the amendments to Parts XVI and XXVIII made by 2026, c. 11 apply to the matter or proceeding` |
| 56 | Under section 58(3) of 2026 c 11, do the provisions enacted by sections 10, 34 to 36, 38 and 39 apply to my ongoing matter | `2026 c 11 s 58(3) the provisions enacted by sections 10, 34 to 36, 38 and 39 of 2026, c. 11 apply to the matter or proceeding` |
| 57 | Under section 15 of 2026 c 12, does subsection 236(2) (manslaughter sentencing) apply to my offence | `2026 c 12 s 15 subsection 236(2) applies to the offence` |
| 58 | Under section 16 of 2026 c 12, does subsection 490(2) as amended apply to my ongoing matter | `2026 c 12 s 16 subsection 490(2) as amended by section 3 of 2026, c. 12 applies to the matter or proceeding` |
| 59 | Under section 11.1(1) of 2026 c 15, does the clarification on subsection 319(2) or (2.2) apply to my statement on a matter of public interest | `2026 c 15 s 11.1(1) the clarification applies to the person's communication of the statement` |
| 60 | Under section 11.1(2) of 2026 c 15, does the clarification on subsection 319(2.1) apply to my statement on a matter of public interest | `2026 c 15 s 11.1(2) the clarification applies to the person's communication of the statement` |
| 61 | Under section 87 of 2026 c 19, is the operation of the minimum punishment that applies to me affirmed following the enactment of section 718.4 | `2026 c 19 s 87 the operation of the minimum punishment is affirmed following the enactment of section 718.4` |
| 62 | Under section 96 of 2026 c 19, what is the commencement day | `2026 c 19 s 96 commencement day` |
| 63 | Under section 97 of 2026 c 19, is my act or omission within the time limit on subsection 7(4.1) | `2026 c 19 s 97 the act or omission is within the time limit on subsection 7(4.1)` |
| 64 | Under section 98 of 2026 c 19, do paragraphs 236(2)(b) to (d) apply to my offence | `2026 c 19 s 98 paragraphs 236(2)(b) to (d) apply to the offence` |
| 65 | Under section 99 of 2026 c 19, does paragraph 264(4)(a) apply to my ongoing matter | `2026 c 19 s 99 paragraph 264(4)(a) applies to the matter or proceeding` |
| 66 | Under section 100 of 2026 c 19, are the production and admissibility rules for records of complainants and witnesses within the time limit for my charge | `2026 c 19 s 100 the offence is within the time limit on the provisions of sections 276, 276.01 to 276.13 and 278.1 to 278.38 named by this section` |
| 67 | Under section 101 of 2026 c 19, does subsection 346(1.4) (aggravating factor in extortion) apply to my ongoing matter | `2026 c 19 s 101 subsection 346(1.4) applies to the matter or proceeding` |
| 68 | Under section 102 of 2026 c 19, do the amended testimonial aid rules apply to my ongoing matter | `2026 c 19 s 102 sections 486.1, 486.2 and 486.3 as amended by sections 38, 39 and 40 of 2026, c. 19 apply to the matter or proceeding` |
| 69 | Under section 103 of 2026 c 19, does subsection 489.1(4) apply to my ongoing matter | `2026 c 19 s 103 subsection 489.1(4) applies to the matter or proceeding` |
| 70 | Under section 105 of 2026 c 19, is my offence within the time limit on Part XV.1 | `2026 c 19 s 105 the offence is within the time limit on Part XV.1` |
| 71 | Under section 106 of 2026 c 19, does subsection 507.1(9) apply to my ongoing matter | `2026 c 19 s 106 subsection 507.1(9) as enacted by section 47 of 2026, c. 19 applies to the matter or proceeding` |
| 72 | Under section 107 of 2026 c 19, do the listed bail provisions, read with section 3.01, apply to my ongoing matter | `2026 c 19 s 107 paragraphs 515(3)(a) and (b), (4.1)(a), (4.3)(c) and (6)(b.1) and (b.2), as construed in application of section 3.01, apply to the matter or proceeding` |
| 73 | Under section 108 of 2026 c 19, do the listed adjournment provisions apply to my ongoing matter | `2026 c 19 s 108 subsections 537(1.001), 571(2), 645(3.1), 803(1.1) and 824(2) apply to the matter or proceeding` |
| 74 | Under section 109 of 2026 c 19, does section 657.4 apply to my ongoing matter | `2026 c 19 s 109 section 657.4 applies to the matter or proceeding` |
| 75 | Under section 110 of 2026 c 19, does section 672.5011 apply to an order made about me before the commencement day | `2026 c 19 s 110 section 672.5011 applies to the order` |
| 76 | Under section 111(1) of 2026 c 19, is an alternative measure used for me treated as an alternative measure under section 715.44 | `2026 c 19 s 111(1) the measure is deemed to be an alternative measure, as defined in section 715.44` |
| 77 | Under section 111(2) of 2026 c 19, do the provisions enacted by sections 59, 64 and 65 apply to my ongoing matter | `2026 c 19 s 111(2) the provisions enacted by sections 59, 64 and 65 of 2026, c. 19 apply to the matter or proceeding` |
| 78 | Under section 112 of 2026 c 19, do the amended victim and community impact statement rules apply to my ongoing matter | `2026 c 19 s 112 sections 722 and 722.2 as amended by sections 66 and 67 of 2026, c. 19 apply to the matter or proceeding` |
| 79 | Under section 113 of 2026 c 19, does section 726.21 apply to my ongoing matter | `2026 c 19 s 113 section 726.21 applies to the matter or proceeding` |
| 80 | Under section 114 of 2026 c 19, is my offence within the time limit on section 729.2 | `2026 c 19 s 114 the offence is within the time limit on section 729.2` |
| 81 | Under section 115 of 2026 c 19, is my order within the limits on section 740.1 | `2026 c 19 s 115 the order is within the limits on section 740.1` |
| 82 | Under section 116 of 2026 c 19, is my offence within the time limit on section 752.01 | `2026 c 19 s 116 the offence is within the time limit on section 752.01` |
| 83 | Under section 117 of 2026 c 19, does section 810.03 as amended apply to my ongoing matter | `2026 c 19 s 117 section 810.03 as amended by section 81 of 2026, c. 19 applies to the matter or proceeding` |
| 84 | Under section 118 of 2026 c 19, does section 810.1 as amended apply to my ongoing matter | `2026 c 19 s 118 section 810.1 as amended by section 82 of 2026, c. 19 applies to the matter or proceeding` |
| 85 | Under section 737(1) (not in force), must I pay a victim surcharge | `s 737(1) (not in force) the offender shall pay a victim surcharge for each offence` |
| 86 | Under section 696.2(1) (not in force), may an application for a review on the grounds of miscarriage of justice be made to the Commission by or on behalf of me | `s 696.2(1) (not in force) an application for a review on the grounds of miscarriage of justice may be made to the Commission by or on behalf of the person` |
| 87 | Under section 696.2(2) (not in force), does my application include what it must include | `s 696.2(2) (not in force) the application includes what it must include` |
| 88 | Under section 696.3(2) (not in force), may the Commission's notices and information go to my representative | `s 696.3(2) (not in force) the notice or information may be provided to a representative of the applicant in addition to or instead of the applicant` |
| 89 | Under section 696.4(2) (not in force), must the Commission dismiss my application because I am not a person described in section 696.2(1) | `s 696.4(2) (not in force) the Commission must dismiss the application as inadmissible on the ground that the person is not described in subsection 696.2(1)` |
| 90 | Under section 696.4(3) (not in force), must the Commission dismiss my application because my appeals are not finished | `s 696.4(3) (not in force) the Commission must dismiss the application as inadmissible on a ground in subsection (3)` |
| 91 | Under section 696.4(4) (not in force), may the Commission decide my application is admissible although I did not appeal | `s 696.4(4) (not in force) the Commission may decide that the application is admissible despite subsection (3)` |
| 92 | Under section 696.4(4) (not in force), must the Commission take a given factor into account on admissibility | `s 696.4(4) (not in force) the Commission must take the factor into account` |
| 93 | Under section 696.4(4)(d) (not in force), is my application supported by a new matter of significance within subparagraphs (i) to (iii) | `s 696.4(4)(d) (not in force) the application is supported by a new matter of significance that meets subparagraphs (i) to (iii)` |
| 94 | Under section 696.5(1) (not in force), may the Commission investigate my application | `s 696.5(1) (not in force) the Commission may conduct an investigation in relation to the application` |
| 95 | Under section 696.5(2) (not in force), must the notice I receive give a period to send further information | `s 696.5(2) (not in force) the notice must also specify a reasonable period within which further information may be provided` |
| 96 | Under section 696.5(3) (not in force), is the condition for the Commission to decide my application without an investigation met | `s 696.5(3) (not in force) the condition for deciding under section 696.6 without an investigation is met` |
| 97 | Under section 696.5(8) (not in force), is the condition for the Commission to decide my application after its investigation met | `s 696.5(8) (not in force) the condition for deciding under section 696.6 after an investigation is met` |
| 98 | Under section 696.6(2) (not in force), must the Commission order a new trial or refer my case to the court of appeal | `s 696.6(2) (not in force) the Commission must grant a remedy under paragraph (a) or (b)` |
| 99 | Under section 696.6(2)(a) (not in force), what form does the new proceeding take for me | `s 696.6(2)(a) (not in force) the form of the new proceeding the Commission directs` |
| 100 | Under section 696.6(3) (not in force), must the Commission dismiss my application | `s 696.6(3) (not in force) the Commission must dismiss the application` |
| 101 | Under section 696.6(4) (not in force), may the Commission take a given step on my application if I am deceased | `s 696.6(4) (not in force) the Commission may take the step` |
| 102 | Under section 696.6(5) (not in force), must the Commission take a given factor into account in its decision | `s 696.6(5) (not in force) the Commission must take the factor into account` |
| 103 | Under section 696.6(6) (not in force), may the Commission grant me a remedy even if the evidence does not establish my innocence | `s 696.6(6) (not in force) the Commission may grant a remedy under subsection (2) even if the evidence does not establish the innocence of the applicant` |
| 104 | Under section 696.61 (not in force), may the Commission refer a question about my application to the court of appeal for its opinion | `s 696.61 (not in force) the Commission may refer the question to the court of appeal for its opinion` |
| 105 | Under section 696.72 (not in force), is my application within the Commission's mandate | `s 696.72 (not in force) the application is within the Commission’s mandate` |
| 106 | Under section 679(7) (not in force), am I treated as an appellant for release or detention while the Commission reviews my case | `s 679(7) (not in force) section 679 applies to the release or detention of the person as though the person were an appellant in an appeal described in paragraph (1)(a)` |
| 107 | Under section 8 of 2024 c 33, must the Minister ask me whether I consent to my application being moved to the Commission | `2024 c 33 s 8 the Minister owes the duty to ask the applicant whether they consent to the transfer` |
| 108 | Under section 9 of 2024 c 33, is my application deemed made to the Commission because I consented in time | `2024 c 33 s 9 the application is deemed to have been made to the Commission under the new scheme` |
| 109 | Under section 9 of 2024 c 33, may the Minister give the Commission what the Minister holds on my application because I consented in time | `2024 c 33 s 9 the Minister is authorized to disclose to the Commission all information pertaining to the application that is under the Minister’s control` |
| 110 | Under section 10(1) of 2024 c 33, do subsections (2) and (3) apply because I did not reply or I refused | `2024 c 33 s 10(1) subsection (2) or (3) applies` |
| 111 | Under section 10(2) of 2024 c 33, does the old scheme continue to apply to my application | `2024 c 33 s 10(2) the old scheme continues to apply in respect of the application` |
| 112 | Under section 10(3) of 2024 c 33, is my application deemed not to have been made | `2024 c 33 s 10(3) the application is deemed not to have been made` |
| 113 | Under section 10(3) of 2024 c 33, may I apply to the Commission under the new scheme | `2024 c 33 s 10(3) the applicant may apply to the Commission under the new scheme` |
| 114 | Under section 11 of 2024 c 33, is my application deemed made to the Commission because I consented late | `2024 c 33 s 11 the application is deemed to have been made to the Commission under the new scheme` |
| 115 | Under section 11 of 2024 c 33, may the Minister give the Commission what the Minister holds on my application because I consented late | `2024 c 33 s 11 the Minister is authorized to disclose to the Commission all information pertaining to the application that is under the Minister’s control` |
| 116 | Under section 12 of 2024 c 33, may I take back my consent to the transfer | `2024 c 33 s 12 the consent may be revoked` |
| 117 | Under section 13 of 2024 c 33, does the Minister's dismissal of my application under the old scheme stop me applying under the new scheme | `2024 c 33 s 13 the fact that the Minister dismissed the application under the old scheme prevents the applicant from applying under the new scheme` |
| 118 | Under section 696.3(1) (not in force), must the Commission deal with my application as expeditiously as possible and give me updates | `s 696.3(1) (not in force) the Commission owes the applicant the duty to deal with the application as expeditiously as possible and to provide regular updates` |
| 119 | Under section 696.4(5) (not in force), must the Commission notify me of its decision on whether my application is admissible | `s 696.4(5) (not in force) the Commission owes the duty to notify the applicant and the relevant Attorney General of its decision on admissibility` |
| 120 | Under section 696.5(2) (not in force), must the Commission send me a notice saying whether it will investigate | `s 696.5(2) (not in force) the Commission owes the duty to send a notice indicating whether an investigation will be conducted` |
| 121 | Under section 696.5(4) (not in force), does the Commission have a commissioner's powers when it investigates my application | `s 696.5(4) (not in force) the Commission has the powers of a commissioner under Part I of the Inquiries Act` |
| 122 | Under section 696.5(6) (not in force), must the Commission give me a copy of its investigation report | `s 696.5(6) (not in force) the Commission owes the duty to prepare a report and provide a copy of it` |
| 123 | Under section 696.5(7) (not in force), must the report give me a period to respond in writing | `s 696.5(7) (not in force) the report must specify a reasonable period within which a written response may be provided` |
| 124 | Under section 696.6(7) (not in force), must the Commission notify me of its decision on my application | `s 696.6(7) (not in force) the Commission owes the duty to notify the applicant and the relevant Attorney General of its decision` |
| 125 | Under section 490.04(1) (not in force), is my order or obligation one listed in paragraphs (a), (a.1) and (b) | `s 490.04(1) (not in force) the order or obligation is one listed in paragraph (a), (a.1) or (b)` |
| 126 | Under section 490.04(2) (not in force), am I permitted to apply under paragraph (1)(b) after an earlier application | `s 490.04(2) (not in force) the person is permitted to apply under paragraph (1)(b)` |
| 127 | Under section 490.04(3)(a) (not in force), is a superior court of criminal jurisdiction a court that may receive my application | `s 490.04(3)(a) (not in force) a superior court of criminal jurisdiction is a court that may receive the application` |
| 128 | Under section 490.04(4) (not in force), may the court make an exemption order for me | `s 490.04(4) (not in force) the court may make an exemption order` |
| 129 | Under section 490.04(8) (not in force), if the court makes an exemption order, must it also order my information removed from the database | `s 490.04(8) (not in force) the court shall also make an order requiring the Royal Canadian Mounted Police to permanently remove the information from the database` |
| 130 | Under section 490.05(1) (not in force), is my order or obligation one listed in the replaced paragraphs | `s 490.05(1) (not in force) the order or obligation is one listed in the replaced paragraphs` |
| 131 | Under section 490.05(3)(a) (not in force), is a superior court of criminal jurisdiction a court that may receive my application | `s 490.05(3)(a) (not in force) a superior court of criminal jurisdiction is a court that may receive the application` |
| 132 | Under section 490.06(2) (not in force), if an appeal court makes an exemption order, must it also order my information removed from the database | `s 490.06(2) (not in force) the appeal court shall also make an order requiring the Royal Canadian Mounted Police to permanently remove the information from the database` |
| 133 | Under section 264.01(2) (not in force), do my acts make up a pattern of coercive or controlling conduct | `s 264.01(2) (not in force) the acts make up a pattern of coercive or controlling conduct` |
| 134 | Under section 264.01(1) (not in force), would my conduct be the offence of coercion or control of an intimate partner | `s 264.01(1) (not in force) the accused commits an offence` |
| 135 | Under section 264.01(2)(c) (not in force), is my other conduct within paragraph (c) | `s 264.01(2)(c) (not in force) the conduct is within paragraph (c)` |
| 136 | Under section 264.01(3) (not in force), is a given circumstance one that paragraph (2)(c) includes | `s 264.01(3) (not in force) the circumstances referred to in paragraph (2)(c) include the circumstance` |
| 137 | Under section 264.01(5) (not in force), does a person's safety include a given kind of safety | `s 264.01(5) (not in force) a person’s safety includes the kind of safety` |
| 138 | Under section 264.01(4) (not in force), is the offence indictable, summary or both | `s 264.01(4) (not in force) the class of the offence` |
| 139 | Under section 264.01(4) (not in force), what is the most I can be imprisoned for, in years, if convicted on indictment | `s 264.01(4) (not in force) the punishment for the offence` |
| 140 | Under section 109(1)(b) (not in force), is my offence one listed in the future paragraph | `s 109(1)(b) (not in force) the offence is one listed in paragraph (b)` |
| 141 | Under section 3.01(1)(b.1) (not in force), does my offence count as one in which violence is used, threatened or attempted | `s 3.01(1)(b.1) (not in force) the offence counts as one in which violence is used, threatened or attempted` |
| 142 | Under section 264.01(2)(a) (not in force), is an act of violence of mine within paragraph (a) | `s 264.01(2)(a) (not in force) the act is within paragraph (a)` |
| 143 | Under section 264.01(2)(b) (not in force), is my conduct within paragraph (b), coercing sexual activity | `s 264.01(2)(b) (not in force) the act is within paragraph (b)` |
| 144 | Under section 264.01(2)(c) (not in force), is my conduct one of the kinds listed in subparagraphs (i) to (viii) | `s 264.01(2)(c) (not in force) the conduct is listed in one of the subparagraphs` |
| 145 | Under section 183 (not in force), is the offence of coercion or control of an intimate partner within paragraph (a) of the definition offence in Part VI | `s 183 "offence" (a)(xxxix.4) (not in force) the offence is within paragraph (a) of the definition` |
| 146 | Under section 487.04 (not in force), is the offence of coercion or control of an intimate partner within paragraph (c) of the definition secondary designated offence | `s 487.04 "secondary designated offence" (c)(v.1) (not in force) the offence is within paragraph (c) of the definition` |
| 147 | Under section 490.011(1) (not in force), is the offence of coercion or control of an intimate partner within paragraph (a) of the definition secondary offence | `s 490.011(1) "secondary offence" (a)(ix.1) (not in force) the offence is within paragraph (a) of the definition` |

## What the text turns out to say (ccc32)

1. **No commencement day is in the text.** Every transitional provision that turns on "the day on which section N comes into force" leaves that day to a date a caller states. The single day the text computes is the `commencement day` of 2026, c. 19: the 30th day after royal assent (line 19421); the assent date is also an input.
2. **Section 104 of 2026, c. 19 is not in the text.** The related provisions run from section 103 (line 19449) to section 105 (line 19453); no line of the range begins `104 `. Nothing here depends on it, but a reader looking for it will not find it.
3. **Two Acts restrict subsection 236(2) by date, in different words.** 2026, c. 12, s. 15 says subsection 236(2) does not apply to an offence committed before the 30th day after that Act's royal assent (line 19401); 2026, c. 19, s. 98 says paragraphs 236(2)(b) to (d) do not apply to an offence committed before the commencement day of c. 19 (line 19429). They are encoded as two rules, and the encoding does not say which governs an offence committed between the two days.
4. **Sections 357 and 358 of 2019, c. 25 list different sections.** Section 357 (an undertaking given to a judge or justice, line 19258) lists subsection 503(3.1) and sections 515, 522, 524, 525, 597, 679, 683, 816 and 832; section 358 (a recognizance before a judge or justice, line 19262) lists the same except section 597. A recognizance entered into under section 597 is therefore not covered by section 358 as the text reads.
5. **"applicant" is defined twice, differently.** Section 696.1 (not in force) says an applicant is the person who is the subject of the finding or verdict in question (line 19557); section 7 of 2024, c. 33 says the applicant is that person "or their representative" (line 19654). The encoding keeps both under their own names.
6. **Section 264.01(4)(b) states no penalty for the summary limb.** The paragraph says only "guilty of an offence punishable on summary conviction" (line 19787), so the penalty on summary conviction is that of section 787(1), which is outside the range; the encoding takes it as an input (a `Punishment`). On indictment the maximum is ten years (line 19786).
7. **Subsection 696.2(2) (not in force) is worded as a requirement on every application, but is stated "for the purposes of subsection 696.4(3)"** (line 19568), the dismissal for appeals not finished. The encoding asks it of every application (fork F8).
8. **Conditional replacement.** Section 190 of 2018, c. 16 replaces subsection 737(1) only if Bill C-28 receives royal assent and then only on the first day on which both subsection 2(1) of that Act and section 222 of 2018, c. 16 are in force (line 19520); nothing in the text says whether either has happened, so the encoding asks both as facts.
9. **The commencement day of 2024, c. 33 is the day section 3 comes into force** (line 19655); the text gives no date, so sections 8 to 13 turn on a DATE input.
10. **The arithmetic of the months.** `add months` and `add years` clamp to the last day of a shorter month: 31 August 2019 plus six months is 29 February 2020, and 29 February 2020 plus two years is 28 February 2022 (asserted in the tests; fork F2).

## What the stable binary does not accept (ccc32)

The stable build is `l4` 1.6.110 (main), with 1.6.109 (main) as the second build that `check.sh` compares; where a skill describes a construct the binary rejects, the binary governs.
These are findings of this run, each seen on the stable binary, sorted by whether the binary says so (loud) or returns a wrong-looking answer with exit code 0 (silent):
1. **Loud: a DEONTIC value cannot be asserted.** An `#ASSERT` that a regulative rule (for example the Review Board's duty in 1991 c 43 s 10(2)) EQUALS FULFILLED fails with `Trying to check equality on types that do not support it`. Each regulative rule is therefore run with `#TRACE ... AT 0 WITH PARTY ... DOES ... AT n` and its FULFILLED or BREACH result is read from the evaluation output, and the same duty is also written as a decision function that is asserted (named `... owes the duty to ...` where the rule and its twin would otherwise share a name).
2. **Loud: `AFTER` is not an operator.** `a AFTER b` parses as an application of `a` to arguments and fails with `You are trying to apply a (predefined) of type DATE (which is not a function) to 2 arguments`. A comparison "after the day" is written `GREATER THAN`.
3. **Loud: a constructor pattern that binds a field is written `WHEN ctor name THEN`, not `WHEN ctor WITH name THEN`.** The `WITH` form is rejected with `unexpected WITH`.
4. **Silent: `add months` and `add years` clamp at a month end** instead of rolling forward (finding 10). It returns a date with exit code 0, so the tests assert the clamped dates.
5. **Not used, and not tested here:** `REFUSE`, `#ASSERT ... REFUSED`, `BECAUSE` outside `LEST BREACH ... BECAUSE`, a `YMD` of my own, `TYPICALLY`, a section-level `GIVEN`.
Every module is run with `l4 run` and the diagnostics are read, not the exit code: `check.sh` counts `DiagnosticSeverity_Error` and the satisfied, failed and refused assertions.

## Limits, and what I peeked at (ccc32)

- I read the brief, PLAN.md, COMMONS-CLAUDE.md, ENCODING-GUIDE.md, KEEL-NOTES.md (in part), the two skills' SKILL.md files, `dialects.md`, `source-locators.md`, `regulative.md` and `source-patterns` entries 4.1 and 4.2 and the headings of 5, 9, 10 and 11; I did not read all of `source-patterns/` or `drafting-patterns.md` that the brief asks for (I read the entries this range needs).
- `peeked`: nothing outside `INPUTS_DIR`, `DEPOSIT`, `work/` and the two skills' files; no other directory of the runs tree, nothing under `<local tool>`, and no existing encoding.
- The text read was the converter's plain text; a table or a form in the original may be laid out differently. No provision of this range is a table; the only mention of a Form is the amendment of Form 52 (inert, reason 2).
- The seat questions were written from the text and the plan, not from asking a person; their wording is for a human reviewer to improve.
- `check.sh` compares assertion counts on the two builds and, as it says, does not see a different TRACE outcome: the 15 traces were read on `l4` 1.6.110 only.

## What check.sh printed (ccc32)

The output of `L4=<L4_BIN> L4_MAIN=<l4-main-109> ./check.sh`, run last and unedited:

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.109 (main, 4c887e0, 2026-11-04)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
ccc-core.l4                                    0         0       0        0         0 |      0         0       0        0  same
ccc-definitions.l4                             0         0       0        0         0 |      0         0       0        0  same
ccc-interpretation.l4                          0         0       0        0         0 |      0         0       0        0  same
ccc32-cases-seat.l4                            0       231       0        0         0 |      0       231       0        0  same
ccc32-nif-1.l4                                 0         0       0        0         0 |      0         0       0        0  same
ccc32-nif-c19.l4                               0         0       0        0         0 |      0         0       0        0  same
ccc32-nif-soirsa.l4                            0         0       0        0         0 |      0         0       0        0  same
ccc32-nif-xxi1-transition.l4                   0         0       0        0         0 |      0         0       0        0  same
ccc32-nif-xxi1.l4                              0         0       0        0         0 |      0         0       0        0  same
ccc32-related-1.l4                             0         0       0        0         0 |      0         0       0        0  same
ccc32-related-2.l4                             0         0       0        0         0 |      0         0       0        0  same
ccc32-related-3.l4                             0         0       0        0         0 |      0         0       0        0  same
ccc32-seat.l4                                  0         0       0        0         0 |      0         0       0        0  same
ccc32-tests-nif-1.l4                           0        21       0        0         0 |      0        21       0        0  same
ccc32-tests-nif-c19.l4                         0        70       0        0         0 |      0        70       0        0  same
ccc32-tests-nif-soirsa.l4                      0        74       0        0         0 |      0        74       0        0  same
ccc32-tests-nif-xxi1-transition.l4             0        60       0        0         0 |      0        60       0        0  same
ccc32-tests-nif-xxi1.l4                        0       115       0        0         0 |      0       115       0        0  same
ccc32-tests-related-1.l4                       0        94       0        0         0 |      0        94       0        0  same
ccc32-tests-related-2.l4                       0       137       0        0         0 |      0       137       0        0  same
ccc32-tests-related-3.l4                       0       112       0        0         0 |      0       112       0        0  same
TOTAL (21 modules)                             0       914       0        0           |      0       914       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

Baseline numbers it replaced: the first full `check.sh` run of this part printed 913 assertions satisfied in all (682 in the eight test files and 231 in `ccc32-cases-seat.l4`, 0 failed, 0 refused, 0 errors); the final run is above (the difference is the one assertion added for the section 561 seam of 2019 c 25 s 359).

