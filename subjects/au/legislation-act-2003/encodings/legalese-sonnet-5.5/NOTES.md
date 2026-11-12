# Legislation Act 2003 (Cth), sections 12 to 54: an L4 encoding

Status: draft.
No domain expert has read this encoding against the text.
Compiler target: `main` (the stable build); written with 1.6.98 and compared with 1.6.110 by `check.sh`.
This file states the current reading of the encoding; it is not a log.

## The text

The only text used is `C2004A01224.txt` in the subject's `registers/source-bundle/` folder: Federal Register compilation C2019C00084 (Compilation No. 39, in force from 24 February 2019) of the Legislation Act 2003 (Cth), Act No. 139 of 2003.
It is a plain-text rendering of the compilation produced by a converter script.
It is not the authorised text, and nothing here is verified against the official text.
Some spaces in it are non-breaking; the scripts read them as ordinary spaces, and every quoted line is copied from the file by `srcrefs.py`, so the quotes keep the file's own characters.
Every layer-1 rule carries an `@ref` with a `src:` locator (lines of that file) and the quoted text above it; `srcrefs.py check` and `check --strict` report 0 problems over every `.l4` file.

## Seat

The seat is an officer of a department or agency who makes or lodges a legislative instrument or a notifiable instrument.
The questions are about commencement, registration and tabling, disallowance, repeal and sunsetting, and what the Federal Register of Legislation must contain.
Seat layer: `lga-seat.l4` (47 questions, each with `@export` and `@desc`, grouped under `§` headings) and `lga-cases-seat.l4` (176 cases).
The seat layer calls the layer-1 rules and restates none; where a question combines two rules (s 14(1) with s 14(2), s 54(1) with s 54(2), s 4 with ss 44(1) and (2), s 46(1) with s 46(2)), the seat only chooses between their answers or feeds one into the other.
Where a question needs a calendar of sitting days, which is not a plain input, it asks for the position of a day in the House's calendar (first sitting day counted as 1) or for a date the officer can read off the calendar.

## Layer 1: the modules

One module per Part, with the definitions and instrument kinds first.
Each rule is a function named for its provision (`s 15G(1): ...`), so that no name is defined twice across modules.
A rule answers `MAYBE BOOLEAN` (a few, where the text leaves nothing open, answer `BOOLEAN`) in the convention of the rulings of 2026-11-04 and 2026-11-05: `JUST TRUE` where the text says yes, `JUST FALSE` only where the text itself says no (a "means" definition, a condition introduced by "if", "where", "when" or "unless", a flat negative, a period it fixes), and `NOTHING` where the text does not say.
Dates, periods and counts are computed in `lga-time.l4`, which imports only the prelude and `daydate`; the other modules call it.
Everything the Act hands to the rules, the regulations or the Attorney-General's or the Counsel's judgment ("as soon as practicable", "considers", the formats the rules prescribe) is a plain input.

| module | sections | what it holds |
|---|---|---|
| `lga-nouns.l4` | various | the two Houses; the kinds of registered law |
| `lga-defs.l4` | 4, 5, 6, 8 to 11 | the definitions the in-scope text uses; legislative instrument and notifiable instrument |
| `lga-instruments.l4` | 12 to 14 | commencement; construction; incorporating other instruments |
| `lga-register.l4` | 15A to 15M | the Register; rectification; lodging and registering; explanatory statements; enforceability; notice of events |
| `lga-compilations.l4` | 15P to 15X | compilations; compilation events; editorial changes |
| `lga-authorised.l4` | 15Z to 15ZB | authorised versions; judicial notice |
| `lga-drafting.l4` | 16, 17, 19 | drafting standards; consultation |
| `lga-scrutiny.l4` | 38 to 48 | tabling; disallowance; reviving; not remaking |
| `lga-repeal.l4` | 48A to 48E | automatic repeal; repeal by regulations |
| `lga-sunset.l4` | 50 to 54 | sunsetting; certificates; lists; continuing by resolution; exemptions |
| `lga-time.l4` | 12 to 54 | every date, period and count the text states |
| `lga-provisions.l4`, `lga-xrefs.l4` | 4 to 54 | the provision index and the cross-references, written by script from the text |

Not encoded as rules, and recorded as `inert` in the coverage table: headings, the simplified outlines (ss 7, 15, 15N, 15Y, 15ZC, 36, 48AA, 48F), the purpose clauses (ss 37, 49), and the rule-making and regulation-making powers (ss 15E, 15M, 15U, 40, 48E(1)).
Out of scope, one row each: the front matter and contents, sections 1 to 3AA, Chapter 4 and the endnotes.


## Jural relations

Each relation is stated once, in layer 1, by a `-- jural:` line above the rule that creates it; this table is generated from those lines.
The pair is the holder and the bearer: claim and duty, privilege and no-right, power and liability, immunity and disability.
Where the text does not name the holder or the bearer, the row says so in those words.

| provision | relation (holder \| bearer) | module |
|---|---|---|
| s 12(1A) | power of the rule-maker \| liability of anyone the instrument governs | instruments |
| s 12(2) | immunity of a person other than the Commonwealth or an authority of the Commonwealth \| disability of the rule-maker to bind that person to the extent of the result | instruments |
| s 12(5) | power of the rule-maker \| liability of the commencement of the instrument | instruments |
| s 13(3) | privilege of the person exercising the power \| no-right of anyone to require each matter to be named separately | instruments |
| s 14(1) | power of the rule-maker \| liability of anyone bound by the instrument | instruments |
| s 14(2) | immunity of anyone bound by the instrument \| disability of the rule-maker | instruments |
| s 15A(1) | claim of nobody the text names \| duty of the First Parliamentary Counsel | register |
| s 15A(2) | claim of nobody the text names \| duty of the First Parliamentary Counsel | register |
| s 15A(3) | privilege of the First Parliamentary Counsel \| no-right of users of the Register | register |
| s 15A(4) | privilege of the First Parliamentary Counsel \| no-right of users of the Register | register |
| s 15A(5) | power of the First Parliamentary Counsel \| liability of anyone affected by what is done | register |
| s 15C | claim of the public \| duty of the First Parliamentary Counsel | register |
| s 15D(1) | claim of nobody the text names \| duty of the First Parliamentary Counsel | register |
| s 15D(2) | claim of nobody the text names \| duty of the First Parliamentary Counsel | register |
| s 15D(3) | immunity of a person who relied on the Register \| disability of the First Parliamentary Counsel | register |
| s 15DA(2) | claim of each House \| duty of the First Parliamentary Counsel | register |
| s 15F | claim of nobody the text names \| duty of the First Parliamentary Counsel | register |
| s 15G(1) | claim of the First Parliamentary Counsel \| duty of the rule-maker | register |
| s 15G(2) | claim of the First Parliamentary Counsel \| duty of the rule-maker | register |
| s 15G(3) | privilege of the rule-maker \| no-right of the First Parliamentary Counsel | register |
| s 15G(4) | claim of the First Parliamentary Counsel \| duty of the rule-maker | register |
| s 15G(5) | privilege of the rule-maker \| no-right of the First Parliamentary Counsel | register |
| s 15H(1) | claim of the rule-maker \| duty of the First Parliamentary Counsel | register |
| s 15H(2) | claim of the person lodging \| duty of the First Parliamentary Counsel | register |
| s 15H(3) | immunity of the person lodging \| disability of the First Parliamentary Counsel | register |
| s 15H(4) | claim of the person lodging \| duty of the First Parliamentary Counsel | register |
| s 15J(4) | privilege of the rule-maker \| no-right of anyone to insist on one statement for each instrument | register |
| s 15K(1) | immunity of any person (including the Commonwealth) \| disability of anyone who would enforce an unregistered instrument | register |
| s 15L(1) and (2) | claim of the First Parliamentary Counsel \| duty of the responsible person | register |
| s 15P(1) and (2) | claim of nobody the text names \| duty of whoever prepares the registered compilation (the text does not say who) | compilations |
| s 15Q(4) | privilege of the rule-maker and the First Parliamentary Counsel \| no-right of anyone to require a compilation for a retrospective commencement | compilations |
| s 15R(1) and (2) | claim of the First Parliamentary Counsel \| duty of the rule-maker | compilations |
| s 15R(3) | claim of the First Parliamentary Counsel \| duty of the rule-maker | compilations |
| s 15S(1) | power of the First Parliamentary Counsel \| liability of the rule-maker | compilations |
| s 15S(2) | claim of the First Parliamentary Counsel \| duty of the rule-maker | compilations |
| s 15S(3) | claim of the First Parliamentary Counsel \| duty of the rule-maker | compilations |
| s 15T(1) | claim of nobody the text names \| duty of the First Parliamentary Counsel | compilations |
| s 15T(2) | claim of nobody the text names \| duty of the First Parliamentary Counsel | compilations |
| s 15T(3) | claim of nobody the text names \| duty of the First Parliamentary Counsel | compilations |
| s 15T(4) | privilege of the First Parliamentary Counsel \| no-right of users of the Register | compilations |
| s 15T(5) | claim of nobody the text names \| duty of the First Parliamentary Counsel | compilations |
| s 15T(6) | privilege of the First Parliamentary Counsel \| no-right of users of the Register | compilations |
| s 15T(7) | claim of nobody the text names \| duty of the First Parliamentary Counsel | compilations |
| s 15V(1) and (2) | power of the First Parliamentary Counsel \| liability of anyone whose rights the changed text governs | compilations |
| s 15V(3) and (4) | power of the First Parliamentary Counsel \| liability of anyone whose rights the changed text governs | compilations |
| s 15V(5) | power of the First Parliamentary Counsel \| liability of anyone whose rights the changed text governs | compilations |
| s 15V(6) and (7) | immunity of anyone bound by the Act or instrument \| disability of the First Parliamentary Counsel | compilations |
| s 15ZB(1) | immunity of a party to the proceedings from having to prove the matter \| disability of the court or tribunal to require proof | authorised |
| s 15ZB(2) | privilege of the court or tribunal \| no-right of a party to insist on a particular source | authorised |
| s 15ZB(3) | claim of the parties \| duty of the court or tribunal | authorised |
| s 16(1) | claim of nobody the text names \| duty of the First Parliamentary Counsel | drafting |
| s 16(3) | claim of nobody the text names \| duty of the First Parliamentary Counsel | drafting |
| s 17(1) | claim of nobody the text names \| duty of the rule-maker | drafting |
| s 38(1) | claim of each House \| duty of the Office of Parliamentary Counsel | scrutiny |
| s 39(1) | claim of each House \| duty of the Office of Parliamentary Counsel | scrutiny |
| s 39(2) | claim of each House \| duty of the Office of Parliamentary Counsel | scrutiny |
| s 39(3) | claim of the House \| duty of the rule-maker | scrutiny |
| s 41 | power of a House \| liability of the rule-maker or the Office of Parliamentary Counsel | scrutiny |
| s 42(1) | power of a House \| liability of the legislative instrument and the person relying on it | scrutiny |
| s 46(1) | immunity of the Parliament's scrutiny of the original instrument \| disability of the rule-maker to remake it | scrutiny |
| s 47(1) | immunity of the Parliament's scrutiny of the original instrument \| disability of the rule-maker to remake it | scrutiny |
| s 47(2) | immunity of the Parliament's scrutiny of the original instrument \| disability of the rule-maker to remake it | scrutiny |
| s 48(1) and (2) | immunity of the Parliament's scrutiny of the disallowed instrument \| disability of the rule-maker to remake it | scrutiny |
| s 48E(2) | claim of nobody the text names \| duty of the Attorney-General | repeal |
| s 51(1) | power of the Attorney-General \| liability of the legislative instrument (its sunsetting day moves) | sunset |
| s 51(5) | claim of the Parliament \| duty of whoever lodges the explanatory statement for the certificate (the text does not say who) | sunset |
| s 51A(1) | power of the Attorney-General \| liability of the instruments to be reviewed (their sunsetting day moves) | sunset |
| s 51A(4) | claim of the Parliament \| duty of whoever lodges the explanatory statement for the sunset-altering instrument (the text does not say who) | sunset |
| s 52(2) | claim of each House \| duty of the Attorney-General | sunset |
| s 52(3) | claim of the rule-maker \| duty of the Office of Parliamentary Counsel | sunset |
| s 52(4) | claim of the rule-maker \| duty of the Office of Parliamentary Counsel (limited to the earlier day) | sunset |
| none | each of these provisions defines a term, states a period or a date, applies an effect to an instrument or document by operation of the Act, or says what a power or the rules may cover; the encoding records no holder or bearer for them (ss 11(3), 17(2), 48(2) and 53(1) read as a permission or an effect on the instrument and are listed here without one) | 128 citations |

The citations in the `none` row: s 4 "commencement instrument", s 4 "compilation", s 4 "disallowable legislative instrument", s 4 "enabling legislation", s 4 "Federal Register of Legislation", s 4 "First Parliamentary Counsel", s 4 "instrument", s 4 "making", s 4 "Office of Parliamentary Counsel", s 4 "power delegated by the Parliament", s 4 "primary law", s 4 "register", s 4 "repeal", s 4 "rules", s 4 "text", s 5(1), s 5(2), s 6(1), s 6(2), s 6(3), s 6(3)(b), s 8(1), s 8(2), s 8(3), s 8(4), s 8(5), s 8(6), s 8(7), s 8(8), s 9(1) and (2), s 9(2), s 9(3), s 10(1), s 10(2), s 11(1), s 11(2), s 11(3), s 11(4), s 12(1), s 12(1)(b), s 12(4), s 13(1), s 13(1)(b), s 13(1)(c), s 13(2), s 13(4), s 13(5), s 14(3), s 14(4), s 15B, s 15D(4), s 15DA(1), s 15DA(3), s 15DA(3)(a), s 15DA(3)(b), s 15DA(3)(c), s 15DA(3)(d), s 15DA(3)(e), s 15DA(3)(f), s 15DA(4), s 15DA(5), s 15J(1), s 15J(2), s 15J(3), s 15K(2), s 15Q(1), s 15Q(2), s 15Q(3), s 15R(4), s 15W, s 15W(b), s 15X(2), s 15X(3), s 15X(4), s 15Z, s 15ZA(1), s 15ZA(1) to (4), s 15ZA(2), s 15ZA(3), s 15ZA(4), s 15ZA(5), s 15ZA(6), s 15ZB(4), s 15ZB(5), s 16(2), s 17(2), s 17(3), s 19, s 38(3), s 39(4), s 42(2), s 42(3), s 44(1), s 44(2), s 44(3), s 45(2) and (3), s 46(3), s 47(3), s 47(4), s 48(3), s 48(4), s 48A(1), s 48A(1A), s 48A(2), s 48A(3), s 48B(1), s 48B(2), s 48B(3), s 48C(1), s 48C(2), s 48C(3), s 48C(5), s 48D(1), s 48D(2), s 48D(3), s 50(1), s 50(2), s 50(3), s 51(3), s 51(4), s 51A(2), s 51A(3), s 53(1), s 53(2), s 53 Note, s 54(1), s 54(2), s 54(3).

## Coverage

The text file has 1646 non-blank lines; every one falls in exactly one row below (checked by a script kept outside the deposit when this file was written: 0 lines missing, 0 in two rows).
A row is a heading, a section, a subsection, a paragraph (with its subparagraphs), a defined term or a table row, or one of four out-of-scope blocks.
The dispositions are `encoded` (a rule cites the lines), `inert`, `fork` (a rule cites the lines and a fork in the register below is taken there), `repealed or blank in this text` and `out of scope`.
`repealed or blank in this text` has no rows: the text prints no repealed or blank unit in the scope.
An `inert` row is one of: not operative (a heading, a simplified outline, a purpose clause, the words that introduce the definitions, a description of what a section covers), or machinery (a rule-making or regulation-making power).
A row whose words only point to another definition ("see section 15J") is `encoded` through the rule that holds the definition, named in the fourth column.

| disposition | rows |
|---|---|
| encoded | 342 |
| fork | 157 |
| inert | 133 |
| repealed or blank in this text | 0 |
| out of scope | 4 |
| total rows | 636 |

Rows by kind: 33 definition, 1 front matter, 94 heading, 3 out of scope, 297 paragraph, 21 section, 176 subsection, 11 table row.

| row | lines | disposition | rules that cite it, or why not | fork |
|---|---|---|---|---|
| Front matter and contents (title, about this compilation, contents,... | 1-23 | out of scope | Front matter and contents (lines 1 to 23) |  |
| Chapter 1 Part 1, sections 1 to 3AA (short title, commencement, obj... | 24-69 | out of scope | Chapter 1 Part 1, sections 1 to 3AA (lines 24 to 69) |  |
| s 4 heading: The Dictionary | 70 | inert | not operative |  |
| In this Act: | 71 | inert | not operative |  |
| definition of amend | 72 | encoded | signpost: the term is defined where it points, s 5(1) in lga-defs |  |
| definition of approved website | 73 | encoded | signpost: the term is defined where it points, s 15C in lga-register |  |
| definition of authorised version | 74 | encoded | signpost: the term is defined where it points, s 15ZA in lga-authorised |  |
| definition of commencement instrument (opening words) | 75 | encoded | defs: s 4 "commencement instrument" |  |
| definition of commencement instrument(a) | 76 | encoded | defs: s 4 "commencement instrument" |  |
| definition of commencement instrument(b) | 77-78 | encoded | defs: s 4 "commencement instrument" |  |
| definition of compilation (opening words) | 79 | encoded | defs: s 4 "compilation" |  |
| definition of compilation(a) | 80 | encoded | defs: s 4 "compilation" |  |
| definition of compilation(b) | 81 | encoded | defs: s 4 "compilation" |  |
| definition of compilation(c) | 82-83 | encoded | defs: s 4 "compilation" |  |
| definition of compilation date | 84 | encoded | signpost: the term is defined where it points, s 4 in lga-defs |  |
| definition of disallowable legislative instrument | 85-86 | encoded | scrutiny: s 4 "disallowable legislative instrument" |  |
| definition of discretionary compilation event | 87 | encoded | signpost: the term is defined where it points, s 15Q(2) in lga-compilations |  |
| definition of editorial change | 88 | encoded | signpost: the term is defined where it points, s 15X(2) in lga-compilations |  |
| definition of enabling legislation | 89 | encoded | defs: s 4 "enabling legislation" |  |
| definition of explanatory statement for a legislative instrument | 90 | encoded | signpost: the term is defined where it points, s 15J(1) in lga-register |  |
| definition of Federal Register of Legislation | 91 | encoded | defs: s 4 "Federal Register of Legislation" |  |
| definition of First Parliamentary Counsel | 92 | encoded | defs: s 4 "First Parliamentary Counsel" |  |
| definition of initial explanatory statement | 93 | encoded | signpost: the term is defined where it points, s 15J(1) in lga-register |  |
| definition of instrument | 94 | encoded | defs: s 4 "instrument" |  |
| definition of legislative instrument | 95-96 | encoded | signpost: the term is defined where it points, s 8 in lga-defs |  |
| definition of making | 97 | encoded | defs: s 4 "making" |  |
| definition of modify | 98 | encoded | signpost: the term is defined where it points, s 5(2) in lga-defs |  |
| definition of notifiable instrument | 99-100 | encoded | signpost: the term is defined where it points, s 11 in lga-defs |  |
| definition of Office of Parliamentary Counsel | 101 | encoded | defs: s 4 "Office of Parliamentary Counsel" |  |
| definition of power delegated by the Parliament (opening words) | 102 | encoded | defs: s 4 "power delegated by the Parliament" |  |
| definition of power delegated by the Parliament(a) | 103 | encoded | defs: s 4 "power delegated by the Parliament" |  |
| definition of power delegated by the Parliament(b) | 104-105 | encoded | defs: s 4 "power delegated by the Parliament" |  |
| definition of primary law | 106 | encoded | defs: s 4 "primary law" |  |
| definition of register | 107 | encoded | defs: s 4 "register" |  |
| definition of registered law or explanatory statement | 108 | encoded | signpost: the term is defined where it points, s 15Z in lga-authorised |  |
| definition of repeal | 109-110 | encoded | defs: s 4 "repeal" |  |
| definition of replacement explanatory statement | 111 | encoded | signpost: the term is defined where it points, s 15J(1) in lga-register |  |
| definition of required compilation event | 112 | encoded | signpost: the term is defined where it points, s 15Q(1) in lga-compilations |  |
| definition of responsible person | 113 | encoded | signpost: the term is defined where it points, s 6(2) in lga-defs |  |
| definition of rule-maker | 114 | encoded | signpost: the term is defined where it points, s 6(1) in lga-defs |  |
| definition of rules | 115-116 | encoded | defs: s 4 "rules" |  |
| definition of supplementary explanatory statement | 117 | encoded | signpost: the term is defined where it points, s 15J(1) in lga-register |  |
| definition of text | 118-119 | encoded | defs: s 4 "text" |  |
| s 5 heading: Definitions of amend and modify | 120 | inert | not operative |  |
| s 5(1) (opening words) | 121 | encoded | defs: s 5(1) |  |
| s 5(1)(a) | 122 | encoded | defs: s 5(1) |  |
| s 5(1)(b) | 123-128 | encoded | defs: s 5(1) |  |
| s 5(1)(c) | 129 | encoded | defs: s 5(1) |  |
| s 5(1)(d) | 130-132 | encoded | defs: s 5(1) |  |
| s 5(2) | 133 | encoded | defs: s 5(2) |  |
| s 6 heading: Definitions of rule-maker and responsible person | 134 | inert | not operative |  |
| s 6(1) (opening words) | 135-136 | encoded | defs: s 6(1) |  |
| s 6(1)(a) | 137 | encoded | defs: s 6(1) |  |
| s 6(1)(b) | 138 | encoded | defs: s 6(1) |  |
| s 6(1)(c) | 139 | encoded | defs: s 6(1) |  |
| s 6(2) (opening words) | 140-141 | encoded | defs: s 6(2) |  |
| s 6(2)(a) | 142 | encoded | defs: s 6(2) |  |
| s 6(2)(b) | 143 | encoded | defs: s 6(2) |  |
| s 6(3) (opening words) | 144 | encoded | defs: s 6(3); defs: s 6(3)(b) |  |
| s 6(3)(a) | 145 | encoded | defs: s 6(3); defs: s 6(3)(b) |  |
| s 6(3)(b) | 146 | encoded | defs: s 6(3); defs: s 6(3)(b) |  |
| Part 2 heading: Key concepts for legislative instruments and notifi... | 147 | inert | not operative |  |
| s 7 heading: Simplified outline of this Part | 148 | inert | not operative |  |
| s 7 | 149-164 | inert | not operative |  |
| s 8 heading: Definition of legislative instrument | 165 | inert | not operative |  |
| s 8(1) | 166-167 | encoded | defs: s 8(1) |  |
| s 8(2) (opening words) | 168-169 | encoded | defs: s 8(2) |  |
| s 8(2)(a) | 170 | encoded | defs: s 8(2) |  |
| s 8(2)(b) | 171-176 | encoded | defs: s 8(2) |  |
| s 8(3) | 177-180 | encoded | defs: s 8(3) |  |
| s 8(4) (opening words) | 181 | encoded | defs: s 8(4) |  |
| s 8(4)(a) | 182 | encoded | defs: s 8(4) |  |
| s 8(4)(b) | 183-185 | encoded | defs: s 8(4) |  |
| s 8(5) | 186-188 | encoded | defs: s 8(5) |  |
| s 8(6) (opening words) | 189-190 | fork | defs: s 8(6) | F17 |
| s 8(6)(a) | 191 | encoded | defs: s 8(6) |  |
| s 8(6)(b) | 192 | encoded | defs: s 8(6) |  |
| s 8(7) | 193 | fork | defs: s 8(7) | F17 |
| s 8(8) (opening words) | 194 | fork | defs: s 8(8) | F17 |
| s 8(8)(a) | 195 | encoded | defs: s 8(8) |  |
| s 8(8)(b) | 196 | encoded | defs: s 8(8) |  |
| s 8(8)(c) | 197 | encoded | defs: s 8(8) |  |
| s 8(8)(d) | 198 | encoded | defs: s 8(8) |  |
| s 8(8)(e) | 199-200 | encoded | defs: s 8(8) |  |
| s 9 heading: Inference of legislative character | 201 | inert | not operative |  |
| s 9(1) | 202-203 | encoded | defs: s 9(1) and (2) |  |
| s 9(2) | 204 | encoded | defs: s 9(2) |  |
| s 9(3) | 205-207 | encoded | defs: s 9(3) |  |
| s 10 heading: Instruments declared to be legislative instruments | 208 | inert | not operative |  |
| s 10(1) (opening words) | 209 | encoded | defs: s 10(1) |  |
| s 10(1)(a) | 210 | fork | defs: s 10(1) | F20 |
| s 10(1)(b) | 211 | encoded | defs: s 10(1) |  |
| s 10(1)(c) | 212 | encoded | defs: s 10(1) |  |
| s 10(1)(d) | 213-214 | encoded | defs: s 10(1) |  |
| s 10(2) (opening words) | 215 | encoded | defs: s 10(2) |  |
| s 10(2)(a) | 216 | encoded | defs: s 10(2) |  |
| s 10(2)(b) | 217 | encoded | defs: s 10(2) |  |
| s 11 heading: Definition of notifiable instrument | 218 | inert | not operative |  |
| s 11(1) (opening words) | 219-220 | encoded | defs: s 11(1) |  |
| s 11(1)(a) | 221 | encoded | defs: s 11(1) |  |
| s 11(1)(b) | 222-227 | encoded | defs: s 11(1) |  |
| s 11(2) (opening words) | 228 | encoded | defs: s 11(2) |  |
| s 11(2)(a) | 229 | encoded | defs: s 11(2) |  |
| s 11(2)(b) | 230 | fork | defs: s 11(2) | F20 |
| s 11(2)(c) | 231 | fork | defs: s 11(2) | F20 |
| s 11(2)(d) | 232-233 | fork | defs: s 11(2) | F20 |
| s 11(3) | 234-236 | encoded | defs: s 11(3) |  |
| s 11(4) | 237-238 | fork | defs: s 11(4) | F19 |
| s 12 heading: Commencement of legislative instruments and notifiabl... | 239 | inert | not operative |  |
| s 12(1) (opening words) | 240-241 | fork | instruments: s 12(1); time: s 12(1) | F07 |
| s 12(1)(a) | 242 | fork | instruments: s 12(1); time: s 12(1) | F07 |
| s 12(1)(b) | 243-244 | fork | instruments: s 12(1)(b) | F07 |
| s 12(1A) | 245-247 | fork | instruments: s 12(1A) | F20 |
| s 12(2) (opening words) | 248-249 | fork | instruments: s 12(2) | F09, F14 |
| s 12(2)(a) | 250 | fork | instruments: s 12(2) | F09 |
| s 12(2)(b) | 251 | fork | instruments: s 12(2) | F09 |
| s 12(4) | 252-253 | encoded | instruments: s 12(4) |  |
| s 12(5) | 254-255 | fork | instruments: s 12(5) | F20 |
| s 13 heading: Construction of legislative instruments and notifiabl... | 256 | inert | not operative |  |
| s 13(1) (opening words) | 257 | fork | instruments: s 13(1) | F19 |
| s 13(1)(a) | 258 | fork | instruments: s 13(1) | F19 |
| s 13(1)(b) | 259 | fork | instruments: s 13(1)(b) | F19 |
| s 13(1)(c) | 260 | fork | instruments: s 13(1)(c) | F19 |
| s 13(2) | 261 | encoded | instruments: s 13(2) |  |
| s 13(3) (opening words) | 262, 265 | encoded | instruments: s 13(3) |  |
| s 13(3)(a) | 263 | encoded | instruments: s 13(3) |  |
| s 13(3)(b) | 264 | encoded | instruments: s 13(3) |  |
| s 13(4) | 266 | encoded | instruments: s 13(4) |  |
| s 13(5) | 267-268 | encoded | instruments: s 13(5) |  |
| s 14 heading: Prescribing matters by reference to other instruments | 269 | inert | not operative |  |
| s 14(1) (opening words) | 270 | fork | instruments: s 14(1) | F19 |
| s 14(1)(a) | 271-274 | fork | instruments: s 14(1) | F19 |
| s 14(1)(b) | 275-277 | fork | instruments: s 14(1) | F19 |
| s 14(2) | 278 | fork | instruments: s 14(2) | F09, F19 |
| s 14(3) (opening words) | 279 | encoded | instruments: s 14(3) |  |
| s 14(3)(a) | 280 | encoded | instruments: s 14(3) |  |
| s 14(3)(b) | 281-282 | encoded | instruments: s 14(3) |  |
| s 14(4) | 283-285 | encoded | instruments: s 14(4) |  |
| Chapter 2 heading: Registration of Acts, legislative instruments an... | 286 | inert | not operative |  |
| Part 1 heading: The Federal Register of Legislation | 287 | inert | not operative |  |
| Division 1 heading: Simplified outline of this Part | 288 | inert | not operative |  |
| s 15 heading: Simplified outline of this Part | 289 | inert | not operative |  |
| s 15 | 290-296 | inert | not operative |  |
| Division 2 heading: Federal Register of Legislation | 297 | inert | not operative |  |
| s 15A heading: Federal Register of Legislation—establishment and ma... | 298 | inert | not operative |  |
| s 15A(1) | 299-304 | encoded | register: s 15A(1) |  |
| s 15A(2) (opening words) | 305 | fork | register: s 15A(2) | F09 |
| s 15A(2)(a) | 306 | fork | register: s 15A(2) | F09 |
| s 15A(2)(b) | 307 | fork | register: s 15A(2) | F09 |
| s 15A(2)(c) | 308 | fork | register: s 15A(2) | F09 |
| s 15A(2)(d) | 309 | fork | register: s 15A(2) | F09 |
| s 15A(2)(e) | 310 | fork | register: s 15A(2) | F09 |
| s 15A(3) (opening words) | 311 | encoded | register: s 15A(3) |  |
| s 15A(3)(a) | 312 | fork | register: s 15A(3) | F20 |
| s 15A(3)(b) | 313 | fork | register: s 15A(3) | F20 |
| s 15A(3)(c) | 314 | encoded | register: s 15A(3) |  |
| s 15A(3)(d) | 315 | fork | register: s 15A(3) | F20 |
| s 15A(3)(e) | 316 | encoded | register: s 15A(3) |  |
| s 15A(4) | 317 | encoded | register: s 15A(4) |  |
| s 15A(5) | 318 | encoded | register: s 15A(5) |  |
| s 15B heading: Federal Register of Legislation—complete record of r... | 319 | inert | not operative |  |
| s 15B | 320-321 | encoded | register: s 15B |  |
| s 15C heading: Federal Register of Legislation—access to registered... | 322 | inert | not operative |  |
| s 15C | 323 | fork | register: s 15C | F09 |
| s 15D heading: Federal Register of Legislation—rectification of Reg... | 324 | inert | not operative |  |
| s 15D(1) (opening words) | 325 | fork | register: s 15D(1) | F09 |
| s 15D(1)(a) | 326 | fork | register: s 15D(1) | F09 |
| s 15D(1)(b) | 327-333 | fork | register: s 15D(1) | F09 |
| s 15D(2) | 334 | fork | register: s 15D(2) | F09 |
| s 15D(3) (opening words) | 335 | fork | register: s 15D(3) | F09 |
| s 15D(3)(a) | 336 | fork | register: s 15D(3) | F09 |
| s 15D(3)(b) | 337 | encoded | register: s 15D(3)(b) |  |
| s 15D(4) | 338-340 | encoded | register: s 15D(4) |  |
| s 15DA heading: Requirement for re-tabling and new disallowance per... | 341 | inert | not operative |  |
| s 15DA(1) (opening words) | 342 | encoded | register: s 15DA(1) |  |
| s 15DA(1)(a) | 343 | encoded | register: s 15DA(1) |  |
| s 15DA(1)(b) | 344 | encoded | register: s 15DA(1) |  |
| s 15DA(1)(c) | 345 | encoded | register: s 15DA(1) |  |
| s 15DA(2) | 346-348 | fork | register: s 15DA(2); time: s 15DA(2) | F03, F09 |
| s 15DA(3) (opening words) | 349-350 | encoded | register: s 15DA(3) |  |
| s 15DA(3)(a) | 351 | fork | register: s 15DA(3)(a) | F19 |
| s 15DA(3)(b) | 352 | encoded | register: s 15DA(3)(b) |  |
| s 15DA(3)(c) | 353 | encoded | register: s 15DA(3)(c) |  |
| s 15DA(3)(d) | 354 | encoded | register: s 15DA(3)(d) |  |
| s 15DA(3)(e) | 355-359 | encoded | register: s 15DA(3)(e); time: s 15DA(3)(e) |  |
| s 15DA(3)(f) | 360 | encoded | register: s 15DA(3)(f) |  |
| s 15DA(4) | 361 | encoded | register: s 15DA(4) |  |
| s 15DA(5) | 362-363 | fork | register: s 15DA(5) | F19 |
| s 15E heading: Federal Register of Legislation—keeping the Register | 364 | inert | not operative |  |
| s 15E (opening words) | 365 | inert | machinery |  |
| s 15E(a) | 366 | inert | machinery |  |
| s 15E(b) | 367 | inert | machinery |  |
| s 15E(c) | 368 | inert | machinery |  |
| s 15E(d) | 369 | inert | machinery |  |
| s 15E(e) | 370 | inert | machinery |  |
| Division 3 heading: Registration on Federal Register of Legislation | 371 | inert | not operative |  |
| s 15F heading: Registration of Acts | 372 | inert | not operative |  |
| s 15F | 373 | fork | register: s 15F | F09 |
| s 15G heading: Lodgement of legislative instruments and notifiable ... | 374 | inert | not operative |  |
| s 15G(1) | 375-376 | fork | register: s 15G(1) | F09 |
| s 15G(2) | 377 | fork | register: s 15G(2) | F09 |
| s 15G(3) | 378-379 | fork | register: s 15G(3) | F20 |
| s 15G(4) (opening words) | 380-381 | fork | register: s 15G(4) | F09 |
| s 15G(4)(a) | 382 | fork | register: s 15G(4) | F09 |
| s 15G(4)(b) | 383-384 | fork | register: s 15G(4) | F09 |
| s 15G(5) | 385-386 | encoded | register: s 15G(5) |  |
| s 15H heading: Registration of legislative instruments and notifiab... | 387 | inert | not operative |  |
| s 15H(1) (opening words) | 388 | fork | register: s 15H(1) | F09 |
| s 15H(1)(a) | 389 | fork | register: s 15H(1) | F09 |
| s 15H(1)(b) | 390 | fork | register: s 15H(1) | F09 |
| s 15H(2) | 391 | fork | register: s 15H(2) | F09 |
| s 15H(3) (opening words) | 392 | fork | register: s 15H(3) | F09 |
| s 15H(3)(a) | 393-395 | fork | register: s 15H(3) | F09 |
| s 15H(3)(b) | 396 | fork | register: s 15H(3) | F09 |
| s 15H(4) | 397 | fork | register: s 15H(4) | F09 |
| s 15J heading: Explanatory statements | 398 | inert | not operative |  |
| s 15J(1) (opening words) | 399-400 | encoded | register: s 15J(1) |  |
| s 15J(1)(a) | 401 | encoded | register: s 15J(1) |  |
| s 15J(1)(b) | 402-404 | encoded | register: s 15J(1) |  |
| s 15J(1)(c) | 405-407 | encoded | register: s 15J(1) |  |
| s 15J(2) (opening words) | 408-409 | encoded | register: s 15J(2) |  |
| s 15J(2)(a) | 410 | encoded | register: s 15J(2) |  |
| s 15J(2)(b) | 411 | encoded | register: s 15J(2) |  |
| s 15J(2)(c) | 412 | encoded | register: s 15J(2) |  |
| s 15J(2)(d) | 413 | encoded | register: s 15J(2) |  |
| s 15J(2)(e) | 414 | encoded | register: s 15J(2) |  |
| s 15J(2)(f) | 415 | encoded | register: s 15J(2) |  |
| s 15J(2)(g) | 416 | encoded | register: s 15J(2) |  |
| s 15J(3) (opening words) | 417-418 | encoded | register: s 15J(3) |  |
| s 15J(3)(a) | 419 | encoded | register: s 15J(3) |  |
| s 15J(3)(b) | 420 | encoded | register: s 15J(3) |  |
| s 15J(4) | 421-422 | encoded | register: s 15J(4) |  |
| s 15K heading: Registration—enforceability of legislative instruments | 423 | inert | not operative |  |
| s 15K(1) | 424 | fork | register: s 15K(1) | F09, F19 |
| s 15K(2) | 425 | encoded | register: s 15K(2) |  |
| s 15L heading: Events affecting the currency or accuracy of the Reg... | 426 | inert | not operative |  |
| s 15L(1) (opening words) | 427 | fork | register: s 15L(1) and (2) | F09 |
| s 15L(1)(a) | 428 | fork | register: s 15L(1) and (2) | F09 |
| s 15L(1)(b) | 429 | fork | register: s 15L(1) and (2) | F09 |
| s 15L(1)(c) | 430 | fork | register: s 15L(1) and (2) | F09 |
| s 15L(1)(d) | 431 | fork | register: s 15L(1) and (2) | F09 |
| s 15L(1)(e) | 432-434 | fork | register: s 15L(1) and (2) | F09 |
| s 15L(1)(f) | 435-436 | fork | register: s 15L(1) and (2) | F09 |
| s 15L(2) (opening words) | 437 | fork | register: s 15L(1) and (2) | F09 |
| s 15L(2)(a) | 438 | fork | register: s 15L(1) and (2) | F09 |
| s 15L(2)(b) | 439 | fork | register: s 15L(1) and (2) | F09 |
| s 15L(2)(c) | 440-442 | fork | register: s 15L(1) and (2) | F09 |
| s 15L(2)(d) | 443-445 | fork | register: s 15L(1) and (2) | F09 |
| s 15L(2)(e) | 446 | fork | register: s 15L(1) and (2) | F09 |
| s 15M heading: Rules for lodgement and registration | 447 | inert | not operative |  |
| s 15M (opening words) | 448 | inert | machinery |  |
| s 15M(a) | 449-454 | inert | machinery |  |
| s 15M(b) | 455-459 | inert | machinery |  |
| s 15M(c) | 460 | inert | machinery |  |
| s 15M(d) | 461 | inert | machinery |  |
| s 15M(e) | 462 | inert | machinery |  |
| s 15M(f) | 463 | inert | machinery |  |
| s 15M(g) | 464 | inert | machinery |  |
| s 15M(h) | 465 | inert | machinery |  |
| Part 2 heading: Compilations | 466 | inert | not operative |  |
| Division 1 heading: Simplified outline of this Part | 467 | inert | not operative |  |
| s 15N heading: Simplified outline of this Part | 468 | inert | not operative |  |
| s 15N | 469-472 | inert | not operative |  |
| Division 2 heading: Registration of compilations | 473 | inert | not operative |  |
| s 15P heading: Registered compilations—information requirements | 474 | inert | not operative |  |
| s 15P(1) (opening words) | 475 | encoded | compilations: s 15P(1) and (2) |  |
| s 15P(1)(a) | 476 | encoded | compilations: s 15P(1) and (2) |  |
| s 15P(1)(b) | 477 | encoded | compilations: s 15P(1) and (2) |  |
| s 15P(1)(c) | 478 | encoded | compilations: s 15P(1) and (2) |  |
| s 15P(1)(d) | 479 | encoded | compilations: s 15P(1) and (2) |  |
| s 15P(1)(e) | 480 | encoded | compilations: s 15P(1) and (2) |  |
| s 15P(2) (opening words) | 481 | encoded | compilations: s 15P(1) and (2) |  |
| s 15P(2)(a) | 482 | encoded | compilations: s 15P(1) and (2) |  |
| s 15P(2)(b) | 483 | encoded | compilations: s 15P(1) and (2) |  |
| s 15Q heading: Definitions of required compilation event and discre... | 484 | inert | not operative |  |
| s 15Q(1) (opening words) | 485-486 | fork | compilations: s 15Q(1) | F12 |
| s 15Q(1)(a) | 487 | encoded | compilations: s 15Q(1) |  |
| s 15Q(1)(b) | 488-490 | encoded | compilations: s 15Q(1) |  |
| s 15Q(1)(c) | 491 | fork | compilations: s 15Q(1) | F20 |
| s 15Q(1)(d) | 492 | encoded | compilations: s 15Q(1) |  |
| s 15Q(2) (opening words) | 493 | fork | compilations: s 15Q(2) | F12 |
| s 15Q(2)(a) | 494 | encoded | compilations: s 15Q(2) |  |
| s 15Q(2)(b) | 495 | encoded | compilations: s 15Q(2) |  |
| s 15Q(2)(c) | 496 | encoded | compilations: s 15Q(2) |  |
| s 15Q(2)(d) | 497 | encoded | compilations: s 15Q(2) |  |
| s 15Q(2)(e) | 498 | encoded | compilations: s 15Q(2) |  |
| s 15Q(2)(f) | 499 | encoded | compilations: s 15Q(2) |  |
| s 15Q(2)(g) | 500 | encoded | compilations: s 15Q(2) |  |
| s 15Q(2)(h) | 501-502 | encoded | compilations: s 15Q(2) |  |
| s 15Q(3) | 503-504 | encoded | compilations: s 15Q(3) |  |
| s 15Q(4) | 505 | encoded | compilations: s 15Q(4) |  |
| s 15R heading: Lodgement of compilations of instruments—required co... | 506 | inert | not operative |  |
| s 15R(1) | 507-508 | fork | compilations: s 15R(1) and (2) | F09 |
| s 15R(2) | 509-510 | encoded | compilations: s 15R(2) |  |
| s 15R(3) | 511-512 | fork | compilations: s 15R(3); time: s 15R(3) | F01, F13 |
| s 15R(4) | 513-515 | encoded | compilations: s 15R(4) |  |
| s 15S heading: Lodgement of compilations of instruments—discretiona... | 516 | inert | not operative |  |
| s 15S(1) | 517-518 | encoded | compilations: s 15S(1) |  |
| s 15S(2) | 519-520 | fork | compilations: s 15S(2) | F09 |
| s 15S(3) | 521-522 | fork | compilations: s 15S(3) | F09 |
| s 15T heading: Registration of compilations | 523 | inert | not operative |  |
| s 15T(1) | 524-525 | fork | compilations: s 15T(1) | F09 |
| s 15T(2) (opening words) | 526-527 | fork | compilations: s 15T(2); compilations: s 15T(2)(a) and (b); time: s 15T(2)(a) | F01, F09 |
| s 15T(2)(a) | 528 | fork | compilations: s 15T(2); compilations: s 15T(2)(a) and (b); time: s 15T(2)(a) | F01, F09 |
| s 15T(2)(b) | 529 | fork | compilations: s 15T(2); compilations: s 15T(2)(a) and (b); time: s 15T(2)(a) | F09 |
| s 15T(3) | 530 | fork | compilations: s 15T(3) | F09 |
| s 15T(4) | 531-532 | fork | compilations: s 15T(4) | F10 |
| s 15T(5) (opening words) | 533 | fork | compilations: s 15T(5) | F09 |
| s 15T(5)(a) | 534 | fork | compilations: s 15T(5) | F09 |
| s 15T(5)(b) | 535 | fork | compilations: s 15T(5) | F09 |
| s 15T(6) | 536-537 | encoded | compilations: s 15T(6) |  |
| s 15T(7) (opening words) | 538-539 | fork | compilations: s 15T(7) | F09 |
| s 15T(7)(a) | 540 | fork | compilations: s 15T(7) | F09 |
| s 15T(7)(b) | 541 | fork | compilations: s 15T(7) | F09 |
| s 15U heading: Compilations—rules | 542 | inert | not operative |  |
| s 15U (opening words) | 543 | inert | machinery |  |
| s 15U(a) | 544 | inert | machinery |  |
| s 15U(b) | 545 | inert | machinery |  |
| s 15U(c) | 546 | inert | machinery |  |
| s 15U(d) | 547-552 | inert | machinery |  |
| s 15U(e) | 553 | inert | machinery |  |
| s 15U(f) | 554 | inert | machinery |  |
| s 15U(g) | 555 | inert | machinery |  |
| s 15U(h) | 556 | inert | machinery |  |
| s 15U(i) | 557 | inert | machinery |  |
| Division 3 heading: Editorial changes and other changes | 558 | inert | not operative |  |
| s 15V heading: Power to make editorial changes and other changes | 559 | inert | not operative |  |
| s 15V(1) | 560-563 | encoded | compilations: s 15V(1) and (2) |  |
| s 15V(2) (opening words) | 564 | encoded | compilations: s 15V(1) and (2) |  |
| s 15V(2)(a) | 565 | encoded | compilations: s 15V(1) and (2) |  |
| s 15V(2)(b) | 566 | encoded | compilations: s 15V(1) and (2) |  |
| s 15V(3) | 567-568 | encoded | compilations: s 15V(3) and (4) |  |
| s 15V(4) | 569 | encoded | compilations: s 15V(3) and (4) |  |
| s 15V(5) (opening words) | 570-571 | encoded | compilations: s 15V(5) |  |
| s 15V(5)(a) | 572 | encoded | compilations: s 15V(5) |  |
| s 15V(5)(b) | 573 | encoded | compilations: s 15V(5) |  |
| s 15V(5)(c) | 574 | encoded | compilations: s 15V(5) |  |
| s 15V(5)(d) | 575-576 | encoded | compilations: s 15V(5) |  |
| s 15V(6) | 577-578 | fork | compilations: s 15V(6) and (7) | F09 |
| s 15V(7) | 579-580 | fork | compilations: s 15V(6) and (7) | F09 |
| s 15W heading: Editorial changes treated in the same way as amendme... | 581 | inert | not operative |  |
| s 15W (opening words) | 582 | encoded | compilations: s 15W |  |
| s 15W(a) | 583 | encoded | compilations: s 15W |  |
| s 15W(b) | 584 | encoded | compilations: s 15W(b) |  |
| s 15X heading: Definition of editorial change | 585 | inert | not operative |  |
| s 15X(1) | 586-587 | inert | not operative |  |
| s 15X(2) (opening words) | 588 | fork | compilations: s 15X(2) | F12 |
| s 15X(2)(a) | 589 | encoded | compilations: s 15X(2) |  |
| s 15X(2)(b) | 590-592 | encoded | compilations: s 15X(2) |  |
| s 15X(2)(c) | 593 | encoded | compilations: s 15X(2) |  |
| s 15X(2)(d) | 594 | encoded | compilations: s 15X(2) |  |
| s 15X(2)(e) | 595 | encoded | compilations: s 15X(2) |  |
| s 15X(2)(f) | 596 | encoded | compilations: s 15X(2) |  |
| s 15X(2)(g) | 597-598 | encoded | compilations: s 15X(2) |  |
| s 15X(2)(h) | 599 | encoded | compilations: s 15X(2) |  |
| s 15X(2)(i) | 600 | encoded | compilations: s 15X(2) |  |
| s 15X(2)(j) | 601 | encoded | compilations: s 15X(2) |  |
| s 15X(2)(k) | 602 | encoded | compilations: s 15X(2) |  |
| s 15X(2)(l) | 603-609 | encoded | compilations: s 15X(2) |  |
| s 15X(2)(m) | 610 | encoded | compilations: s 15X(2) |  |
| s 15X(2)(n) | 611-612 | encoded | compilations: s 15X(2) |  |
| s 15X(2)(o) | 613 | encoded | compilations: s 15X(2) |  |
| s 15X(2)(p) | 614 | encoded | compilations: s 15X(2) |  |
| s 15X(2)(q) | 615 | encoded | compilations: s 15X(2) |  |
| s 15X(3) (opening words) | 616 | encoded | compilations: s 15X(3) |  |
| s 15X(3)(a) | 617 | encoded | compilations: s 15X(3) |  |
| s 15X(3)(b) | 618 | encoded | compilations: s 15X(3) |  |
| s 15X(3)(c) | 619 | encoded | compilations: s 15X(3) |  |
| s 15X(4) (opening words) | 620 | encoded | compilations: s 15X(4) |  |
| s 15X(4)(a) | 621 | encoded | compilations: s 15X(4) |  |
| s 15X(4)(b) | 622 | encoded | compilations: s 15X(4) |  |
| s 15X(4)(c) | 623 | encoded | compilations: s 15X(4) |  |
| s 15X(4)(d) | 624 | encoded | compilations: s 15X(4) |  |
| s 15X(4)(e) | 625 | encoded | compilations: s 15X(4) |  |
| s 15X(4)(f) | 626 | encoded | compilations: s 15X(4) |  |
| Part 3 heading: Authorised versions and judicial notice | 627 | inert | not operative |  |
| Division 1 heading: Introduction | 628 | inert | not operative |  |
| s 15Y heading: Simplified outline of this Part | 629 | inert | not operative |  |
| s 15Y | 630 | inert | not operative |  |
| s 15Z heading: Scope of this Part | 631 | inert | not operative |  |
| s 15Z (opening words) | 632 | encoded | authorised: s 15Z |  |
| s 15Z(a) | 633 | encoded | authorised: s 15Z |  |
| s 15Z(b) | 634 | encoded | authorised: s 15Z |  |
| s 15Z(c) | 635 | encoded | authorised: s 15Z |  |
| s 15Z(d) | 636 | encoded | authorised: s 15Z |  |
| Division 2 heading: Authorised versions and judicial notice | 637 | inert | not operative |  |
| s 15ZA heading: Authorised versions | 638 | inert | not operative |  |
| s 15ZA(1) (opening words) | 639-640 | fork | authorised: s 15ZA(1); authorised: s 15ZA(1) to (4) | F11 |
| s 15ZA(1)(a) | 641 | encoded | authorised: s 15ZA(1); authorised: s 15ZA(1) to (4) |  |
| s 15ZA(1)(b) | 642-645 | encoded | authorised: s 15ZA(1); authorised: s 15ZA(1) to (4) |  |
| s 15ZA(2) (opening words) | 646 | fork | authorised: s 15ZA(2); authorised: s 15ZA(1) to (4) | F11 |
| s 15ZA(2)(a) | 647 | encoded | authorised: s 15ZA(2); authorised: s 15ZA(1) to (4) |  |
| s 15ZA(2)(b) | 648-649 | encoded | authorised: s 15ZA(2); authorised: s 15ZA(1) to (4) |  |
| s 15ZA(3) | 650-651 | fork | authorised: s 15ZA(3) | F11 |
| s 15ZA(4) | 652 | fork | authorised: s 15ZA(4) | F11 |
| s 15ZA(5) (opening words) | 653-654 | fork | authorised: s 15ZA(5) | F19 |
| s 15ZA(5)(a) | 655 | encoded | authorised: s 15ZA(5) |  |
| s 15ZA(5)(b) | 656 | encoded | authorised: s 15ZA(5) |  |
| s 15ZA(5)(c) | 657-659 | encoded | authorised: s 15ZA(5) |  |
| s 15ZA(5)(d) | 660 | encoded | authorised: s 15ZA(5) |  |
| s 15ZA(5)(e) | 661 | encoded | authorised: s 15ZA(5) |  |
| s 15ZA(5)(f) | 662 | encoded | authorised: s 15ZA(5) |  |
| s 15ZA(5)(g) | 663 | encoded | authorised: s 15ZA(5) |  |
| s 15ZA(5)(h) | 664 | encoded | authorised: s 15ZA(5) |  |
| s 15ZA(6) (opening words) | 665-666 | encoded | authorised: s 15ZA(6) |  |
| s 15ZA(6)(a) | 667 | encoded | authorised: s 15ZA(6) |  |
| s 15ZA(6)(b) | 668 | encoded | authorised: s 15ZA(6) |  |
| s 15ZA(6)(c) | 669 | encoded | authorised: s 15ZA(6) |  |
| s 15ZB heading: Judicial notice | 670 | inert | not operative |  |
| s 15ZB(1) (opening words) | 671 | fork | authorised: s 15ZB(1) | F09, F20 |
| s 15ZB(1)(a) | 672 | fork | authorised: s 15ZB(1) | F09 |
| s 15ZB(1)(b) | 673 | fork | authorised: s 15ZB(1) | F09 |
| s 15ZB(1)(c) | 674 | fork | authorised: s 15ZB(1) | F09 |
| s 15ZB(1)(d) | 675 | fork | authorised: s 15ZB(1) | F09 |
| s 15ZB(1)(e) | 676 | fork | authorised: s 15ZB(1) | F09 |
| s 15ZB(1)(f) | 677 | fork | authorised: s 15ZB(1) | F09 |
| s 15ZB(1)(g) | 678 | fork | authorised: s 15ZB(1) | F09 |
| s 15ZB(1)(h) | 679 | fork | authorised: s 15ZB(1) | F09 |
| s 15ZB(2) | 680 | encoded | authorised: s 15ZB(2) |  |
| s 15ZB(3) | 681 | fork | authorised: s 15ZB(3) | F09 |
| s 15ZB(4) | 682 | encoded | authorised: s 15ZB(4) |  |
| s 15ZB(5) | 683 | encoded | authorised: s 15ZB(5) |  |
| Chapter 3 heading: Legislative instruments and notifiable instruments | 684 | inert | not operative |  |
| Part 1 heading: Drafting standards and consultation | 685 | inert | not operative |  |
| s 15ZC heading: Simplified outline of this Part | 686 | inert | not operative |  |
| s 15ZC | 687-688 | inert | not operative |  |
| s 16 heading: Measures to achieve high drafting standards for legis... | 689 | inert | not operative |  |
| s 16(1) | 690 | encoded | drafting: s 16(1) |  |
| s 16(2) (opening words) | 691 | encoded | drafting: s 16(2) |  |
| s 16(2)(a) | 692 | encoded | drafting: s 16(2) |  |
| s 16(2)(b) | 693 | encoded | drafting: s 16(2) |  |
| s 16(2)(c) | 694 | encoded | drafting: s 16(2) |  |
| s 16(2)(d) | 695 | encoded | drafting: s 16(2) |  |
| s 16(2)(e) | 696 | encoded | drafting: s 16(2) |  |
| s 16(2)(f) | 697 | encoded | drafting: s 16(2) |  |
| s 16(3) (opening words) | 698 | encoded | drafting: s 16(3) |  |
| s 16(3)(a) | 699 | encoded | drafting: s 16(3) |  |
| s 16(3)(b) | 700 | encoded | drafting: s 16(3)(b) |  |
| s 16(3)(c) | 701 | encoded | drafting: s 16(3)(c) |  |
| s 17 heading: Rule-makers should consult before making legislative ... | 702 | inert | not operative |  |
| s 17(1) (opening words) | 703 | fork | drafting: s 17(1) | F09 |
| s 17(1)(a) | 704 | fork | drafting: s 17(1) | F09 |
| s 17(1)(b) | 705 | fork | drafting: s 17(1) | F09 |
| s 17(2) (opening words) | 706 | encoded | drafting: s 17(2) |  |
| s 17(2)(a) | 707 | encoded | drafting: s 17(2) |  |
| s 17(2)(b) | 708 | encoded | drafting: s 17(2) |  |
| s 17(3) | 709-710 | encoded | drafting: s 17(3) |  |
| s 19 heading: Consequence of failure to consult | 711 | inert | not operative |  |
| s 19 | 712 | encoded | drafting: s 19 |  |
| Part 2 heading: Parliamentary scrutiny of legislative instruments | 713 | inert | not operative |  |
| s 36 heading: Simplified outline of this Part | 714 | inert | not operative |  |
| s 36 | 715-716 | inert | not operative |  |
| s 37 heading: The purpose of the Part | 717 | inert | not operative |  |
| s 37 | 718-719 | inert | not operative |  |
| s 38 heading: Tabling of legislative instruments | 720 | inert | not operative |  |
| s 38(1) | 721 | fork | scrutiny: s 38(1); time: s 38(1) | F03, F09 |
| s 38(3) | 722 | fork | scrutiny: s 38(3) | F05, F06 |
| s 39 heading: Tabling of explanatory statements | 723 | inert | not operative |  |
| s 39(1) | 724 | fork | scrutiny: s 39(1) | F09 |
| s 39(2) (opening words) | 725 | fork | scrutiny: s 39(2) | F03, F09 |
| s 39(2)(a) | 726-728 | fork | scrutiny: s 39(2); scrutiny: s 39(2)(a)(ii) and (b) | F09 |
| s 39(2)(b) | 729 | fork | scrutiny: s 39(2); scrutiny: s 39(2)(a)(ii) and (b) | F09 |
| s 39(3) | 730 | fork | scrutiny: s 39(3) | F09 |
| s 39(4) (opening words) | 731 | encoded | scrutiny: s 39(4) |  |
| s 39(4)(a) | 732 | encoded | scrutiny: s 39(4) |  |
| s 39(4)(b) | 733-734 | encoded | scrutiny: s 39(4) |  |
| s 40 heading: Regulations may specify manner of delivery of certain... | 735 | inert | not operative |  |
| s 40 | 736 | inert | machinery |  |
| s 41 heading: Incorporated material may be required to be made avai... | 737 | inert | not operative |  |
| s 41 (opening words) | 738 | encoded | scrutiny: s 41 |  |
| s 41(a) | 739 | encoded | scrutiny: s 41 |  |
| s 41(b) | 740 | encoded | scrutiny: s 41 |  |
| s 42 heading: Disallowance of legislative instruments | 741 | inert | not operative |  |
| s 42(1) (opening words) | 742, 745 | fork | scrutiny: s 42(1); time: s 42(1); time: s 42(1)(b) | F04 |
| s 42(1)(a) | 743 | encoded | scrutiny: s 42(1); time: s 42(1); time: s 42(1)(b) |  |
| s 42(1)(b) | 744 | encoded | scrutiny: s 42(1); time: s 42(1); time: s 42(1)(b) |  |
| s 42(2) (opening words) | 746, 751 | fork | scrutiny: s 42(2) | F04 |
| s 42(2)(a) | 747 | encoded | scrutiny: s 42(2) |  |
| s 42(2)(b) | 748-750 | encoded | scrutiny: s 42(2) |  |
| s 42(3) (opening words) | 752, 758 | fork | scrutiny: s 42(3) | F04 |
| s 42(3)(a) | 753 | encoded | scrutiny: s 42(3) |  |
| s 42(3)(b) | 754 | encoded | scrutiny: s 42(3) |  |
| s 42(3)(c) | 755-757 | encoded | scrutiny: s 42(3) |  |
| s 44 heading: Legislative instruments that are not subject to disal... | 759 | inert | not operative |  |
| s 44(1) (opening words) | 760, 763 | fork | scrutiny: s 44(1) | F19 |
| s 44(1)(a) | 761 | encoded | scrutiny: s 44(1) |  |
| s 44(1)(b) | 762 | encoded | scrutiny: s 44(1) |  |
| s 44(2) (opening words) | 764 | encoded | scrutiny: s 44(2) |  |
| s 44(2)(a) | 765 | encoded | scrutiny: s 44(2) |  |
| s 44(2)(b) | 766 | encoded | scrutiny: s 44(2) |  |
| s 44(3) | 767 | encoded | scrutiny: s 44(3) |  |
| s 45 heading: Reviving a legislative instrument, law or provision | 768 | inert | not operative |  |
| s 45(2) (opening words) | 769, 772 | encoded | scrutiny: s 45(2) and (3) |  |
| s 45(2)(a) | 770 | encoded | scrutiny: s 45(2) and (3) |  |
| s 45(2)(b) | 771 | encoded | scrutiny: s 45(2) and (3) |  |
| s 45(3) | 773 | encoded | scrutiny: s 45(2) and (3) |  |
| s 46 heading: Legislative instruments not to be remade while requir... | 774 | inert | not operative |  |
| s 46(1) | 775 | fork | scrutiny: s 46(1) | F09, F19 |
| s 46(2) (opening words) | 776 | fork | time: s 46(2) | F01 |
| s 46(2)(a) | 777 | encoded | time: s 46(2) |  |
| s 46(2)(b) | 778 | encoded | time: s 46(2) |  |
| s 46(2)(c) | 779 | fork | time: s 46(2) | F05 |
| s 46(3) | 780 | encoded | scrutiny: s 46(3) |  |
| s 47 heading: Legislative instruments not to be remade while subjec... | 781 | inert | not operative |  |
| s 47(1) (opening words) | 782 | fork | scrutiny: s 47(1) | F09, F19 |
| s 47(1)(a) | 783 | fork | scrutiny: s 47(1) | F09 |
| s 47(1)(b) | 784 | fork | scrutiny: s 47(1) | F09 |
| s 47(1)(c) | 785 | fork | scrutiny: s 47(1) | F09 |
| s 47(1)(d) | 786 | fork | scrutiny: s 47(1) | F09 |
| s 47(2) (opening words) | 787 | fork | scrutiny: s 47(2) | F09, F19 |
| s 47(2)(a) | 788 | fork | scrutiny: s 47(2) | F09 |
| s 47(2)(b) | 789-790 | fork | scrutiny: s 47(2) | F09 |
| s 47(2)(c) | 791 | fork | scrutiny: s 47(2) | F09 |
| s 47(2)(d) | 792 | fork | scrutiny: s 47(2) | F09 |
| s 47(2)(e) | 793 | fork | scrutiny: s 47(2) | F09 |
| s 47(2)(f) | 794 | fork | scrutiny: s 47(2) | F09 |
| s 47(3) | 795 | encoded | scrutiny: s 47(3) |  |
| s 47(4) | 796 | encoded | scrutiny: s 47(4) |  |
| s 48 heading: Remaking disallowed legislative instruments | 797 | inert | not operative |  |
| s 48(1) | 798 | fork | time: s 48(1) | F02, F19 |
| s 48(2) | 799 | fork | scrutiny: s 48(2) | F19 |
| s 48(3) | 800 | encoded | scrutiny: s 48(3) |  |
| s 48(4) | 801 | encoded | scrutiny: s 48(4) |  |
| Part 3 heading: Repeal of spent legislative instruments, notifiable... | 802 | inert | not operative |  |
| Division 1A heading: Simplified outline of this Part | 803 | inert | not operative |  |
| s 48AA heading: Simplified outline of this Part | 804 | inert | not operative |  |
| s 48AA | 805-806 | inert | not operative |  |
| Division 1 heading: Automatic repeal | 807 | inert | not operative |  |
| Subdivision A heading: Repeal of amending and repealing instruments | 808 | inert | not operative |  |
| s 48A heading: Automatic repeal of amending and repealing instruments | 809 | inert | not operative |  |
| s 48A(1) | 810 | encoded | repeal: s 48A(1) |  |
| s 48A(1A) | 811 | encoded | repeal: s 48A(1A) |  |
| s 48A(2) (opening words) | 812-813 | fork | repeal: s 48A(2); time: s 48A(2) | F08, F19 |
| s 48A(2)(aa) | 814 | encoded | repeal: s 48A(2); time: s 48A(2) |  |
| s 48A(2)(a) | 815-817 | encoded | repeal: s 48A(2); time: s 48A(2) |  |
| s 48A(2)(b) | 818 | encoded | repeal: s 48A(2); time: s 48A(2) |  |
| s 48A(3) | 819-820 | encoded | repeal: s 48A(3) |  |
| Subdivision B heading: Repeal of commencement instruments | 821 | inert | not operative |  |
| s 48B heading: Automatic repeal of commencement instruments | 822 | inert | not operative |  |
| s 48B(1) (opening words) | 823 | encoded | repeal: s 48B(1) |  |
| s 48B(1)(a) | 824 | encoded | repeal: s 48B(1) |  |
| s 48B(1)(b) | 825 | encoded | repeal: s 48B(1) |  |
| s 48B(2) (opening words) | 826-827 | fork | repeal: s 48B(2) | F08 |
| s 48B(2)(a) | 828-832 | encoded | repeal: s 48B(2) |  |
| s 48B(2)(b) | 833 | encoded | repeal: s 48B(2) |  |
| s 48B(3) | 834-835 | encoded | repeal: s 48B(3) |  |
| Subdivision C heading: Repeal of amending or repealing provisions o... | 836 | inert | not operative |  |
| s 48C heading: Automatic repeal of amending and repealing provisions | 837 | inert | not operative |  |
| s 48C(1) (opening words) | 838 | encoded | repeal: s 48C(1) |  |
| s 48C(1)(a) | 839 | encoded | repeal: s 48C(1) |  |
| s 48C(1)(b) | 840-842 | encoded | repeal: s 48C(1) |  |
| s 48C(2) (opening words) | 843-844 | fork | repeal: s 48C(2); time: s 48C(2) | F08, F19 |
| s 48C(2)(aa) | 845 | encoded | repeal: s 48C(2); time: s 48C(2) |  |
| s 48C(2)(a) | 846-848 | encoded | repeal: s 48C(2); time: s 48C(2) |  |
| s 48C(2)(b) | 849 | encoded | repeal: s 48C(2); time: s 48C(2) |  |
| s 48C(3) | 850-851 | encoded | repeal: s 48C(3) |  |
| s 48C(5) (opening words) | 852-853 | encoded | repeal: s 48C(5) |  |
| s 48C(5)(a) | 854 | encoded | repeal: s 48C(5) |  |
| s 48C(5)(b) | 855-856 | encoded | repeal: s 48C(5) |  |
| Subdivision D heading: Repeal of commencement provisions of instrum... | 857 | inert | not operative |  |
| s 48D heading: Automatic repeal of commencement provisions | 858 | inert | not operative |  |
| s 48D(1) (opening words) | 859 | fork | repeal: s 48D(1) | F20 |
| s 48D(1)(a) | 860 | encoded | repeal: s 48D(1) |  |
| s 48D(1)(b) | 861 | encoded | repeal: s 48D(1) |  |
| s 48D(1)(c) | 862 | encoded | repeal: s 48D(1) |  |
| s 48D(2) (opening words) | 863-864 | fork | repeal: s 48D(2) | F08, F19 |
| s 48D(2)(aa) | 865 | encoded | repeal: s 48D(2) |  |
| s 48D(2)(a) | 866-870 | encoded | repeal: s 48D(2) |  |
| s 48D(2)(b) | 871 | encoded | repeal: s 48D(2) |  |
| s 48D(3) | 872-873 | encoded | repeal: s 48D(3) |  |
| Division 2 heading: Repeal by regulations | 874 | inert | not operative |  |
| s 48E heading: Regulations may repeal instruments or provisions no ... | 875 | inert | not operative |  |
| s 48E(1) | 876 | inert | machinery |  |
| s 48E(2) | 877 | fork | repeal: s 48E(2) | F09 |
| Part 4 heading: Sunsetting of legislative instruments | 878 | inert | not operative |  |
| s 48F heading: Simplified outline of this Part | 879 | inert | not operative |  |
| s 48F | 880-884 | inert | not operative |  |
| s 49 heading: The purpose of the Part | 885 | inert | not operative |  |
| s 49 | 886-887 | inert | not operative |  |
| s 50 heading: Sunsetting | 888 | inert | not operative |  |
| s 50(1) | 889 | fork | sunset: s 50(1); time: s 50(1) | F02, F19 |
| s 50(2) | 890-893 | fork | sunset: s 50(2); time: s 50(2) | F16 |
| s 50(2) table, item 1 | 894-896 | encoded | time: s 50(2) |  |
| s 50(2) table, item 2 | 897-899 | encoded | time: s 50(2) |  |
| s 50(2) table, item 3 | 900-902 | encoded | time: s 50(2) |  |
| s 50(2) table, item 4 | 903-905 | encoded | time: s 50(2) |  |
| s 50(2) table, item 5 | 906-908 | encoded | time: s 50(2) |  |
| s 50(2) table, item 6 | 909-911 | encoded | time: s 50(2) |  |
| s 50(2) table, item 7 | 912-914 | encoded | time: s 50(2) |  |
| s 50(2) table, item 8 | 915-917 | encoded | time: s 50(2) |  |
| s 50(2) table, item 9 | 918-920 | encoded | time: s 50(2) |  |
| s 50(2) table, item 10 | 921-923 | encoded | time: s 50(2) |  |
| s 50(2) table, item 11 | 924-926 | encoded | time: s 50(2) |  |
| s 50(3) | 927-929 | encoded | sunset: s 50(3) |  |
| s 51 heading: Attorney-General may defer sunsetting in certain circ... | 930 | inert | not operative |  |
| s 51(1) (opening words) | 931 | encoded | sunset: s 51(1); time: s 51(1)(b) to (d) |  |
| s 51(1)(a) | 932 | encoded | sunset: s 51(1); time: s 51(1)(b) to (d) |  |
| s 51(1)(b) | 933-937 | encoded | sunset: s 51(1); time: s 51(1)(b) to (d) |  |
| s 51(1)(c) | 938 | fork | time: s 51(1)(c) | F15 |
| s 51(1)(d) | 939 | fork | sunset: s 51(1)(d) | F19 |
| s 51(3) | 940 | encoded | sunset: s 51(3) |  |
| s 51(4) | 941 | encoded | sunset: s 51(4); time: s 51(4) |  |
| s 51(5) | 942 | fork | sunset: s 51(5) | F09 |
| s 51A heading: Attorney-General may align sunsetting of instruments... | 943 | inert | not operative |  |
| s 51A(1) (opening words) | 944 | encoded | sunset: s 51A(1) |  |
| s 51A(1)(a) | 945-947 | encoded | sunset: s 51A(1) |  |
| s 51A(1)(b) | 948 | encoded | sunset: s 51A(1) |  |
| s 51A(2) (opening words) | 949 | encoded | sunset: s 51A(2); time: s 51A(2) |  |
| s 51A(2)(a) | 950 | encoded | sunset: s 51A(2); time: s 51A(2) |  |
| s 51A(2)(b) | 951 | fork | sunset: s 51A(2); time: s 51A(2) | F15 |
| s 51A(2)(c) | 952 | fork | sunset: s 51A(2); time: s 51A(2) | F15 |
| s 51A(3) | 953 | encoded | sunset: s 51A(3) |  |
| s 51A(4) | 954 | fork | sunset: s 51A(4) | F09 |
| s 52 heading: Attorney-General must lay lists of instruments due fo... | 955 | inert | not operative |  |
| s 52(1) | 956-958 | fork | time: s 52(1) | F18 |
| s 52(2) | 959 | encoded | sunset: s 52(2) |  |
| s 52(3) | 960 | fork | sunset: s 52(3) | F09 |
| s 52(4) | 961 | fork | sunset: s 52(4) | F09 |
| s 53 heading: Resolution that instrument continue in force | 962 | inert | not operative |  |
| s 53(1) (opening words) | 963 | encoded | sunset: s 53(1) |  |
| s 53(1)(a) | 964-966 | encoded | sunset: s 53(1) |  |
| s 53(1)(b) | 967 | encoded | sunset: s 53(1) |  |
| s 53(2) (opening words) | 968 | encoded | sunset: s 53(2); time: s 53(2)(a) |  |
| s 53(2)(a) | 969 | encoded | sunset: s 53(2); time: s 53(2)(a) |  |
| s 53(2)(b) | 970-971 | encoded | sunset: s 53 Note |  |
| s 54 heading: Instruments to which this Part does not apply | 972 | inert | not operative |  |
| s 54(1) (opening words) | 973 | encoded | sunset: s 54(1) |  |
| s 54(1)(a) | 974 | encoded | sunset: s 54(1) |  |
| s 54(1)(b) | 975 | encoded | sunset: s 54(1) |  |
| s 54(2) (opening words) | 976 | encoded | sunset: s 54(2) |  |
| s 54(2)(a) | 977 | encoded | sunset: s 54(2) |  |
| s 54(2)(b) | 978 | encoded | sunset: s 54(2) |  |
| s 54(2)(c) | 979-984 | encoded | sunset: s 54(2) |  |
| s 54(3) | 985 | encoded | sunset: s 54(3) |  |
| Chapter 4 Miscellaneous, sections 55 to 62 | 986-1053 | out of scope | Chapter 4 Miscellaneous, sections 55 to 62 (lines 986 to 1053) |  |
| Endnotes (about the endnotes, abbreviation key, legislation history... | 1054-1646 | out of scope | Endnotes (line 1054 to the end) |  |

## Fork register

A fork is a place where the text can be read more than one way, or says nothing, and one answer was taken.
Each line gives the provision, the function, the answer taken and the other reading; every one is for the human reviewer to overrule.

| id | question | provisions | the words | answer taken | other reading | function |
|---|---|---|---|---|---|---|
| F01 | Counting "N days after" an event | s 15R(3) (line 512), s 15T(2) (527-529), s 46(2) (776) | "within 28 days after the event occurs"; "ending at the end of 7 days after" the day of laying. | The days after E are E+1 to E+N; the day E is not counted; "within" includes the last day E+N. | Count E as day 1, so that the last day is E+N-1. | lga-time: `the last day of a period of days after an event` |
| F02 | A month or year count whose target day does not exist | s 48(1) (798), s 50(1) (889) | "within 6 months after the day of disallowance"; "the first 1 April or 1 October falling on or after the tenth anniversary of registration". | The same day number in the later month or year; where there is none (6 months after 31 August; the tenth anniversary of 29 February) the answer is NOTHING, except that s 50(1) answers when reading the day back to the 28th and forward to 1 March give the same 1 April or 1 October (they do, for 29 February). | Clamp to the last day of the month (as the date library does), or roll forward to the 1st. | lga-time: `the day with the same day number a number of months after a day`, `s 50(1): the day a legislative instrument is repealed by sunsetting` |
| F03 | Counting "within N sitting days of that House after" an event | s 38(1) (721), s 39(2) (725-729), s 15DA(2) (347) | "within 6 sitting days of that House after the registration of the instrument". | The sitting days strictly after the day of the event; the first of them is day 1; the Nth is the last day; a sitting day on the event day itself is not counted. | Count the event day when it is a sitting day. | lga-time: `the nth sitting day after a day` |
| F04 | The 15 sitting days of section 42 | s 42(1) to (3) (742-758), s 47 (782-794) | "within 15 sitting days of that House beginning on the first sitting day after" the laying (or the notice). | The window begins on the first sitting day after the event and ends on the 15th sitting day counted from it (the same count as F03). | A window that begins on the event day. | lga-time: `s 42(1)(a): notice of a motion to disallow is given in time` |
| F05 | Whose "last day" when a copy is not laid before both Houses | s 38(3) (722), s 46(2)(c) (779) | "the last day for it to be so laid"; "the last day on which subsection 38(1) could have been complied with". | Section 38(1) gives each House its own last day; the later of the two is taken (which matches 46(2)(b), "the later of those days"). | The earlier of the two; or each House separately. | lga-scrutiny: `s 38(3): the first day on which the legislative instrument is no longer in force for not being laid` |
| F06 | When a repeal "immediately after" a last day takes effect | s 38(3) (722) | "repealed immediately after the last day for it to be so laid". | The first day on which the instrument is no longer in force is the day after the last day. | The repeal takes effect at the end of the last day, so the instrument is in force on that day. | lga-scrutiny: `s 38(3): the first day on which the legislative instrument is no longer in force for not being laid` |
| F07 | Section 12(1): paragraph (b) and paragraph (a) | s 12(1) (241-243) | "commences: (a) at the start of the day after the day the instrument is registered; or (b) so far as the instrument provides otherwise-in accordance with such provision". | Where the instrument has its own commencement provision, paragraph (b) governs and (a) does not; otherwise (a). | Both paragraphs are alternatives that apply together. | lga-instruments: `s 12(1)(a): ...`, `s 12(1)(b): ...` |
| F08 | The time of an event for the repeals in ss 48A to 48D | s 48A(2) (813-818), s 48B(2) (827-833), s 48C(2) (844-849), s 48D(2) (864-871) | "on the day after the latest of the following events occurs"; "immediately after the latest of the following events occurs"; "the end of the last day on which the instrument ... may be disallowed". | A commencement or a registration is an event at the start of its day; the end of the last day of disallowance is an event at the end of that day. "Immediately after" an end-of-day event is the next day; immediately after a start-of-day event is that same day. For 48A and 48B the repeal is on the day after the latest event day. | Treat registration as an end-of-day event. | lga-time: `the day after the latest of the days on which events occur`, `the day on which a repeal immediately after the latest event happens` |
| F09 | A duty or prohibition whose "if", "where" or "when" is not met | every rule listed in the last section of this register | The text imposes a duty or prohibition on a stated case and says nothing about other cases. | The function answers NOTHING outside the stated case. (The ruling of 2026-11-05 leaves "a duty whose if or where is unmet" to the encoder; permissions, deemings and effects introduced by "if", "where", "when" or "unless" answer JUST FALSE by the ruling of 2026-11-04 and are not listed.) | JUST FALSE: no duty on those facts. | the rules listed below |
| F10 | Section 15T(4): "if a discretionary compilation event occurs" | s 15T(4) (532), s 15T(6) (537) | "If a discretionary compilation event occurs ..., the First Parliamentary Counsel may prepare and register a compilation"; and (6): "may ... even if neither a required compilation event nor a discretionary compilation event has occurred". | Without an event the answer to (4) is NOTHING, not JUST FALSE, because (6) says the same power exists without an event. | JUST FALSE under the ruling on "if". | lga-compilations: `s 15T(4): ...`, `s 15T(6): ...` |
| F11 | Section 15ZA(1) to (4): a copy that meets none of the routes | s 15ZA(1) to (4) (640-652) | "is an authorised version ... if" (four routes). | A copy that meets none of the four routes answers JUST FALSE (the ruling on "if"). | NOTHING, because each subsection states a sufficient condition only. | lga-authorised: `s 15ZA: the copy ... is an authorised version` |
| F12 | Lists introduced by "is a change ... that" and "occurs when" | s 15X(2) (588-615), s 15Q(1) and (2) (486-501) | "An editorial change ... is a change made by the First Parliamentary Counsel that: (a) ... (q)"; "A required compilation event occurs ... when: (a) ... (d)". | The list is read as the definition: a change or event that matches no paragraph answers JUST FALSE (a definition with "is", and "when" read as "where" by the ruling of 2026-11-05). | NOTHING, because the list is not closed with "only". | lga-compilations: `s 15X(2): ...`, `s 15Q(1): ...`, `s 15Q(2): ...` |
| F13 | Section 15R(3): a compilation lodged before or on the day of the event | s 15R(3) (512) | "within 28 days after the event occurs". | A compilation lodged on any day up to the last day of the 28 days is in time; no lower bound is applied. | Only days after the event count. | lga-compilations: `s 15R(3): the compilation is lodged in time` |
| F14 | Section 12(2): the Commonwealth and its authorities | s 12(2) (249) | "does not apply in relation to a person (other than the Commonwealth or an authority of the Commonwealth)". | For the Commonwealth or an authority the answer is NOTHING (outside the words of the subsection); for any other person it is JUST TRUE where rights are disadvantaged or liabilities imposed, and JUST FALSE where they are not or the instrument does not commence early. | JUST FALSE for the Commonwealth (the instrument applies to it in full). | lga-instruments: `s 12(2): ...` |
| F15 | Sections 51(1)(c) and 51A(2): only an upper limit on the day | s 51(1)(c) (938), s 51A(2)(b) and (c) (951-952) | "on or before the second anniversary of the sunsetting day"; "not more than 5 years after the earliest day". | Only the stated upper limit is applied; a 1 April or 1 October before the sunsetting day (or before the earliest day) passes. | An implied lower limit: the day must be after the sunsetting day (or the earliest day). | lga-time: `s 51(1)(c): ...`, `s 51A(2): ...`; lga-tests-time and lga-cases-seat assert it |
| F16 | Section 50(2): a year made of 2005 or later | s 50(2) (890-926) | The table ends at "2003 or 2004". | An instrument registered on 1 January 2005 and made in 2005 or later is outside every row; the answer is NOTHING. | Apply the last row (1 April 2020), or apply section 50(1). | lga-time: `s 50(2): ...` |
| F17 | Section 8: how the subsections combine | s 8(2) to (8) (168-199) | "(6) Despite subsections (4) and (5), an instrument is not a legislative instrument if ..."; "(7) However, subsection (6) does not apply to an instrument that is a legislative instrument under subsection (3) by registration"; "(8) Despite anything else in this section ...". | Subsection (8) first (not a legislative instrument); then (2) and (3) (a legislative instrument); then (6) displaces (4) and (5) only; so (2) and (3) are not displaced by (6). | Subsection (6) also displaces (2). | lga-defs: `s 8: the instrument is a legislative instrument` |
| F18 | Section 52(1): the "first possible day" | s 52(1) (956-958) | "the first possible day on which any legislative instrument will be repealed by this Part and each 1 April and 1 October occurring after that day". | The first possible day is an input (the text does not give it); it is itself a sunsetting day, and so is each later 1 April and 1 October. | A fixed first day computed from the table in section 50(2). | lga-time: `s 52(1): a day is a sunsetting day` |
| F19 | An "unless" or "except" once it is met | every site in the list after the F09 sites | The text states a rule and then "unless", "except" or "apart from" a condition. | Where the condition is met the function answers JUST FALSE for the rule (the rule does not apply); for s 15K(1) and s 50(1) the text says nothing more and the function answers NOTHING. | NOTHING where the condition is met, because the text does not say what then holds. | the functions listed below |
| F20 | A case "other than" X, and a grant or immunity limited by its own wording | every site in the list after the F19 sites | The text states a rule for a case "other than" X, or for a case it limits in its own words (without "only"). | For the excluded case X, or outside the stated limit, the function answers NOTHING, except where a "means" list or a period fixed in the text decides it (JUST FALSE). | JUST FALSE for the excluded case. | the functions listed below |
| F21 | A bare "must" not done | every duty in the F09 list | The text says a person "must" do something and, in the same provision, states no consequence of not doing it. | The functions say whether the duty applies on the facts; none answers whether it was done, and none states a consequence the text does not state. | Model the duty with a breach and a consequence. | the rules listed in the F09 list |

The sites of F09, generated from the layer-1 modules (a rule with a duty or a bar and an unmet case that answers NOTHING):

| provision | function | answer taken | other reading |
|---|---|---|---|
| s 15ZB(1) | s 15ZB(1): proof is not required about the matter | NOTHING outside the stated case | JUST FALSE: no bar (or the immunity does not apply) on those facts |
| s 15ZB(3) | s 15ZB(3): the court or tribunal must consider whether the source appears to be a reliable source of information | NOTHING outside the stated case | JUST FALSE: no duty on those facts |
| s 15R(1) and (2) | s 15R(1): the rule-maker must prepare and lodge a compilation of the instrument for registration | NOTHING outside the stated case | JUST FALSE: no duty on those facts |
| s 15S(2) | s 15S(2): the compilation date for the compilation | NOTHING outside the stated case | JUST FALSE: no duty on those facts |
| s 15S(3) | s 15S(3): the compilation is lodged within the period | NOTHING outside the stated case | JUST FALSE: no duty on those facts |
| s 15T(1) | s 15T(1): the First Parliamentary Counsel must prepare and register a compilation of the Act as soon as practicable afterwards | NOTHING outside the stated case | JUST FALSE: no duty on those facts |
| s 15T(2) | s 15T(2): the First Parliamentary Counsel must register a compilation of the instrument | NOTHING outside the stated case | JUST FALSE: no duty on those facts |
| s 15T(3) | s 15T(3): the First Parliamentary Counsel must prepare and register a compilation of the instrument as soon as practicable afterwards | NOTHING outside the stated case | JUST FALSE: no duty on those facts |
| s 15T(5) | s 15T(5): the First Parliamentary Counsel must register a compilation of the instrument | NOTHING outside the stated case | JUST FALSE: no duty on those facts |
| s 15T(7) | s 15T(7): the First Parliamentary Counsel must ensure that the registered compilation is no longer shown on the Register as a compilation currently in force | NOTHING outside the stated case | JUST FALSE: no duty on those facts |
| s 15V(6) and (7) | s 15V(6): the First Parliamentary Counsel must not make the change | NOTHING outside the stated case | JUST FALSE: no bar (or the immunity does not apply) on those facts |
| s 17(1) | s 17(1): the rule-maker must be satisfied that the consultation the rule-maker considers appropriate, and that is reasonably practicable, has been undertaken | NOTHING outside the stated case | JUST FALSE: no duty on those facts |
| s 12(2) | s 12(2): the instrument or provision does not apply in relation to the person to the extent of that result | NOTHING outside the stated case | JUST FALSE: no bar (or the immunity does not apply) on those facts |
| s 14(2) | s 14(2): the instrument may not make provision by applying, adopting or incorporating the matter as in force or existing from time to time | NOTHING outside the stated case | JUST FALSE: no bar (or the immunity does not apply) on those facts |
| s 15A(2) | s 15A(2): the Register must contain the document | NOTHING outside the stated case | JUST FALSE: no duty on those facts |
| s 15C | s 15C: the First Parliamentary Counsel must ensure the material is available to the public on the approved website | NOTHING outside the stated case | JUST FALSE: no duty on those facts |
| s 15D(1) | s 15D(1): the First Parliamentary Counsel must arrange for the error to be rectified as soon as possible | NOTHING outside the stated case | JUST FALSE: no duty on those facts |
| s 15D(2) | s 15D(2): the First Parliamentary Counsel must include a statement of the rectification and a brief outline in the Register | NOTHING outside the stated case | JUST FALSE: no duty on those facts |
| s 15D(3) | s 15D(3)(a): the rectification affects the right or privilege | NOTHING outside the stated case | JUST FALSE: no bar (or the immunity does not apply) on those facts |
| s 15DA(2) | s 15DA(2): the First Parliamentary Counsel must arrange for the correct version to be delivered to each House to be laid | NOTHING outside the stated case | JUST FALSE: no duty on those facts |
| s 15F | s 15F: the First Parliamentary Counsel must register the Act as soon as practicable after assent | NOTHING outside the stated case | JUST FALSE: no duty on those facts |
| s 15G(1) | s 15G(1): the rule-maker must lodge the instrument for registration as a legislative instrument as soon as practicable after it is made | NOTHING outside the stated case | JUST FALSE: no duty on those facts |
| s 15G(2) | s 15G(2): the rule-maker must lodge the instrument for registration as a notifiable instrument as soon as practicable after it is made | NOTHING outside the stated case | JUST FALSE: no duty on those facts |
| s 15G(4) | s 15G(4): the rule-maker must lodge the explanatory statement for registration as soon as practicable | NOTHING outside the stated case | JUST FALSE: no duty on those facts |
| s 15H(1) | s 15H(1): the First Parliamentary Counsel must register the instrument as lodged | NOTHING outside the stated case | JUST FALSE: no duty on those facts |
| s 15H(2) | s 15H(2): the First Parliamentary Counsel must register the instrument or document accordingly | NOTHING outside the stated case | JUST FALSE: no duty on those facts |
| s 15H(3) | s 15H(3): the First Parliamentary Counsel must not register the instrument or document | NOTHING outside the stated case | JUST FALSE: no bar (or the immunity does not apply) on those facts |
| s 15H(4) | s 15H(4): the First Parliamentary Counsel must give written notice to the person lodging | NOTHING outside the stated case | JUST FALSE: no duty on those facts |
| s 15K(1) | s 15K(1): the legislative instrument is enforceable by or against any person (including the Commonwealth) | NOTHING outside the stated case | JUST FALSE: no bar (or the immunity does not apply) on those facts |
| s 15L(1) and (2) | s 15L: the responsible person must give notice to the First Parliamentary Counsel of the event | NOTHING outside the stated case | JUST FALSE: no duty on those facts |
| s 48E(2) | s 48E(2): before the Governor-General makes the regulation the Attorney-General must be satisfied that the instrument or provision is spent or is no longer required | NOTHING outside the stated case | JUST FALSE: no duty on those facts |
| s 38(1) | s 38(1): the Office of Parliamentary Counsel must arrange for a copy to be delivered to each House to be laid within 6 sitting days of that House after registration | NOTHING outside the stated case | JUST FALSE: no duty on those facts |
| s 39(1) | s 39(1): the Office of Parliamentary Counsel must arrange for a copy of the explanatory statement to be delivered to each House to be laid | NOTHING outside the stated case | JUST FALSE: no duty on those facts |
| s 39(2) | s 39(2)(a)(i): the delivery must be arranged at the same time as the instrument is delivered under section 38 | NOTHING outside the stated case | JUST FALSE: no duty on those facts |
| s 39(3) | s 39(3): the rule-maker must, as soon as possible, deliver to the House a written statement explaining the lateness of lodgement | NOTHING outside the stated case | JUST FALSE: no duty on those facts |
| s 46(1) | s 46(1): the same legislative instrument is not to be made during the period | NOTHING outside the stated case | JUST FALSE: no bar (or the immunity does not apply) on those facts |
| s 47(1) | s 47(1): the same legislative instrument or provision must not be made | NOTHING outside the stated case | JUST FALSE: no bar (or the immunity does not apply) on those facts |
| s 47(2) | s 47(2): the same legislative instrument or provision must not be made | NOTHING outside the stated case | JUST FALSE: no bar (or the immunity does not apply) on those facts |
| s 48(1) and (2) | s 48(1): the later legislative instrument or provision must not be made on that day | NOTHING outside the stated case | JUST FALSE: no bar (or the immunity does not apply) on those facts |
| s 51(5) | s 51(5): the explanatory statement must include a statement of the reasons for the issue of the certificate | NOTHING outside the stated case | JUST FALSE: no duty on those facts |
| s 51A(4) | s 51A(4): the explanatory statement must include a statement of the reasons for the making of the instrument | NOTHING outside the stated case | JUST FALSE: no duty on those facts |
| s 52(3) | s 52(3): the Office of Parliamentary Counsel must arrange for a copy of the list to be provided to the rule-maker responsible for the legislative instrument | NOTHING outside the stated case | JUST FALSE: no duty on those facts |
| s 52(4) | s 52(4): subsection (3) must be complied with in relation to the day | NOTHING outside the stated case | JUST FALSE: no duty on those facts |

43 sites.

The sites of F19 (an "unless" or "except" once it is met):

| provision | function | answer taken | other reading |
|---|---|---|---|
| s 11(4) | s 11(4): the requirement to publish or notify is taken to be satisfied | contrary intention appears: JUST FALSE | NOTHING |
| s 13(1) | s 13(1)(a), (b), (c) | contrary intention appears: JUST FALSE | NOTHING |
| s 14(1) | s 14(1): the instrument may make provision in relation to the matter by applying, adopting or incorporating it | contrary intention appears: JUST FALSE | NOTHING |
| s 14(2) | s 14(2): the instrument may not make provision by applying, adopting or incorporating the matter as in force or existing from time to time | contrary intention appears: JUST FALSE (the bar does not apply) | NOTHING |
| s 15K(1) | s 15K(1): the legislative instrument is enforceable by or against any person (including the Commonwealth) | registered: NOTHING (the text does not say it is enforceable); not registered: JUST FALSE | JUST TRUE when registered |
| s 15DA(3)(a) | s 15DA(3)(a): the instrument is taken to have been delivered to and laid before the House under subsection 38(1) | the "except" case (the purpose is section 39(2)): JUST FALSE | NOTHING |
| s 15DA(5) | s 15DA(5): the laying before a House affects the time at which the instrument is taken to have been registered | the "except" case (the effect in paragraph (3)(c)): JUST TRUE; any other effect: JUST FALSE | NOTHING for the other effects |
| s 15ZA(5) | s 15ZA(5): the presumption holds | the contrary is proved: JUST FALSE | NOTHING |
| s 44(1) | s 44(1): section 42 does not apply in relation to the instrument | the instrument is a regulation, or an Act makes it disallowable: JUST FALSE | NOTHING |
| s 46(1) | s 46(1): the same legislative instrument is not to be made during the period | both Houses approve by resolution: JUST FALSE | NOTHING |
| s 47(1) and (2) | s 47(1): ..., s 47(2): the same legislative instrument or provision must not be made | notice withdrawn, instrument taken to have been disallowed, motion disposed of, or s 42(3) has applied: JUST FALSE | NOTHING |
| s 48(1) and (2) | s 48(1): the later legislative instrument or provision must not be made on that day; s 48(2): the later instrument or provision may be made within that time | the relevant House approves: JUST FALSE for the bar in (1) and JUST TRUE for the permission in (2) | NOTHING |
| s 48A(2), s 48C(2), s 48D(2) | s 48A(2): the repeal by this section happens; s 48C(2): ...; s 48D(2): ... | repealed earlier by s 38(3) or 42(1) or (2): JUST FALSE | NOTHING |
| s 50(1) | s 50(1): the day a legislative instrument is repealed by sunsetting | registered on 1 January 2005: no day from this subsection (NOTHING); section 50(2) governs | the day s 50(1) would give |
| s 51(1)(d) | s 51(1)(d): the instrument is repealed by section 51 on the specified day instead of the sunsetting day | repealed earlier: JUST FALSE | NOTHING |

15 sites.

The sites of F20 (a case "other than" X, or limited by the text's own words):

| provision | function | answer taken | other reading |
|---|---|---|---|
| s 10(1)(a) | s 10(1): section 10 declares the instrument to be a legislative instrument | a Proclamation that is a commencement instrument: NOTHING unless another paragraph holds | JUST FALSE |
| s 11(2)(b), (c), (d) | s 11(2): the instrument is one that subsection (2) lists as a notifiable instrument | a legislative instrument: those paragraphs do not hold; s 11 answers NOTHING when no paragraph holds | JUST FALSE |
| s 12(1A) and (5) | s 12(1A): ...; s 12(5): ... | an instrument that is neither a legislative instrument nor a notifiable instrument: NOTHING | JUST FALSE |
| s 15A(3)(a), (b), (d) | s 15A(3): the Register may contain the additional document | the excluded kind (registered under this Part): NOTHING | JUST FALSE |
| s 15G(3) | s 15G(3): the rule-maker may lodge the instrument for registration as a legislative instrument or notifiable instrument | a legislative instrument or notifiable instrument: NOTHING | JUST FALSE |
| s 15Q(1)(c) | s 15Q(1): a required compilation event occurs | a repeal under this Act: no paragraph holds, so JUST FALSE (F12) | NOTHING |
| s 15ZB(1) | s 15ZB(1): proof is not required about the matter | not in proceedings in a court or tribunal: NOTHING | JUST FALSE |
| s 48D(1) | s 48D(1): this section repeals the commencement provision | a commencement instrument: NOTHING | JUST FALSE |

8 sites.

### Rulings that bind the answers

Copied word for word from the encoding brief, which copies them from the guide (rulings of 2026-11-04 and 2026-11-05):

> A function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless", a list the text closes with "only", a flat negative.
> Everywhere else it answers `NOTHING`: where the text lists without closing the list, says "includes", leaves a term undefined, is silent, points outside the sources, or limits a grant or prohibition in its own wording and the case falls outside the limit.
> A period the text fixes in its own words: outside it, `JUST FALSE`. A "where ..." condition that fails: `JUST FALSE`. A scope limit with no "only": `NOTHING`.
> Questions the rulings do not settle are decided at each site on the text's own words, with one fork line in the fork register (the provision, the function, the answer taken, the other reading).

"When", "upon" and "whenever" count as "where" under the periods ruling (ruled 2026-11-05).
Applied here: a permission, deeming or effect introduced by "if", "where", "when" or "unless" answers `JUST FALSE` when the condition fails; a duty or a bar whose condition fails answers `NOTHING` (F09), because the six questions the rulings leave open include "a duty whose if or where is unmet".

## What the Act turns out to say

Each statement is the reading the encoding takes, in plain words; "Asserted." means a case in `lga-cases-seat.l4` fixes it, and the case is named in the statement.

1. An instrument that has no commencement provision of its own commences at the start of the day after the day it is registered; one that has its own commencement provision commences as that provision says (s 12(1), F07). Case: "When does my instrument commence". Asserted.
2. A legislative instrument or notifiable instrument may provide that it commences before it is registered (s 12(1A)); the text does not say the same of other instruments. Case: "May my instrument commence before it is registered". Asserted.
3. An instrument or provision that commences before registration does not apply to a person other than the Commonwealth or one of its authorities, to the extent that it would disadvantage the person's rights as at registration or impose liabilities for what was done or omitted before registration; the text does not say how it applies to the Commonwealth (s 12(2), F14). Case: "Does my instrument stop applying to this person". Asserted.
4. Matter from an Act, from a legislative instrument that is or was disallowable, or from rules of court may be applied, adopted or incorporated; matter from any other instrument or writing may be incorporated as in force at, or before, commencement but not as in force from time to time; a contrary intention or the absence of enabling legislation removes the permission (s 14(1) and (2)). Case: "May my instrument incorporate the matter". Asserted.
5. The rule-maker must lodge a legislative instrument, and a notifiable instrument, for registration as soon as practicable after it is made (s 15G(1) and (2)); the text does not say what follows where the instrument has not been made (F09). Cases: "Must I lodge my legislative instrument" and "Must I lodge my notifiable instrument". Asserted.
6. An initial or replacement explanatory statement meets section 15J(2) when all of these hold: it is approved, it explains the purpose and operation of the instrument, it describes any incorporated documents and how to obtain them, it describes the consultation under section 17 or explains why there was none, it contains a statement of compatibility where the instrument is disallowable, and it contains any other information the regulations prescribe. Case: "Does my explanatory statement meet the requirements". Asserted.
7. A supplementary explanatory statement meets section 15J(3) if it is approved and contains the information the regulations prescribe. Case: "Does my supplementary explanatory statement meet the requirements". Asserted.
8. The First Parliamentary Counsel must register what was lodged in accordance with section 15G and the rules (s 15H(1)); a document lodged otherwise than as an instrument, that the Counsel considers not likely to be useful or inappropriate to register, or whose lodgement was withdrawn, is not to be registered (s 15H(3)). Cases: "Will the First Parliamentary Counsel register what I lodged" and "Must the First Parliamentary Counsel refuse to register what I lodged". Asserted.
9. A legislative instrument is not enforceable by or against any person, including the Commonwealth, unless it is registered; the text does not say it is enforceable because it is registered (s 15K(1)). Case: "Can my legislative instrument be enforced". Asserted.
10. A failure to lodge an explanatory statement as section 15G(4) requires does not affect the validity or enforceability of the instrument (s 15K(2)). Case: "Does my failure to lodge an explanatory statement affect the validity or enforceability of my instrument". Asserted.
11. The responsible person must notify the First Parliamentary Counsel of an event that affects the commencement of a registered Act or instrument; the answer is no for a required compilation event (s 15L). Case: "Must I tell the First Parliamentary Counsel about this event". Asserted.
12. Where the Counsel rectifies an error and so replaces a tabled version with the correct version that has been laid, the Counsel must arrange for the correct version to be delivered to each House (s 15DA(2)). Case: "Must the Counsel arrange for the correct version to be laid". Asserted.
13. A rectification of an error does not affect the time at which the instrument is taken to have been registered (s 15D(4)). Case: "Does a correction change the time of registration". Asserted.
14. A required compilation event obliges the rule-maker to prepare and lodge a compilation unless the rules say section 15R does not apply; the compilation must be lodged within 28 days after the event, or a longer period the Counsel allows (s 15R(1) to (3), F01, F13). Cases: "Must I lodge a compilation", "By when must I lodge the compilation" and "Did I lodge the compilation in time". Asserted.
15. On a discretionary compilation event the Counsel may by written notice require the rule-maker to lodge a compilation within a stated period (s 15S(1)). Case: "Can the Counsel require me to lodge a compilation". Asserted.
16. A registered compilation must include the compilation date, a statement and outline of any editorial changes, details of amending laws, the amendment history and any further information the rules prescribe; the last three need not be included where the Counsel is satisfied they are available on an approved website and the compilation says in general terms how to reach them (s 15P). Case: "Does my compilation include everything it must". Asserted.
17. A copy of a registered legislative instrument must be laid before each House within 6 sitting days of that House after registration, the first sitting day after registration being day 1 (s 38(1), F03). Cases: "Must the Office of Parliamentary Counsel arrange for my instrument to be laid before each House" and "Was my instrument laid in time". Asserted.
18. A legislative instrument not laid in accordance with section 38 is repealed immediately after the last day for laying; the first day on which it is no longer in force is the day after the later of the two Houses' last days (s 38(3), F05, F06). Cases: "Is my instrument repealed for not being laid" and "From what day is my instrument no longer in force". Asserted.
19. A disallowable legislative instrument is a legislative instrument to which section 42 applies (s 4); section 42 does not apply where the enabling legislation (not the Corporations Act 2001) facilitates an intergovernmental body or scheme and authorises the instrument, unless the instrument is a regulation or an Act has the effect that it is disallowable (s 44(1)), or where an Act says so or a regulation prescribes it (s 44(2)). Case: "Is my instrument subject to disallowance". Asserted.
20. Notice of a motion to disallow is in time if given within 15 sitting days of the House after laying, and an instrument is disallowed when a resolution passes within 15 sitting days after notice (s 42(1), F04). Cases: "Is a notice of motion to disallow in time" and "Is my instrument disallowed". Asserted.
21. A law repealed by an instrument that is itself repealed under section 38(3) or 42 revives, unless Part 4 would have repealed it before the date of revival (s 45). Case: "Does the repealed law revive". Asserted.
22. Where an original legislative instrument is registered, no instrument the same in substance may be made from the day of registration to the end of 7 days after the day it was laid before both Houses (the later day if different), unless both Houses approve by resolution (s 46(1) and (2), F01, F05). Case: "Am I barred from making the same instrument again under section 46". Asserted.
23. While a notice of a motion to disallow is pending, an instrument the same in substance must not be made unless the notice is withdrawn, the instrument is taken to have been disallowed, the motion is disposed of, or section 42(3) has applied (s 47(1)). Case: "Is the same instrument barred while a notice is pending". Asserted.
24. An instrument the same in substance as one disallowed must not be made within 6 months after the day of disallowance unless the House in which notice was given approves by resolution (s 48(1) and (2), F02). Case: "Is the same instrument barred after disallowance". Asserted.
25. A legislative instrument or notifiable instrument whose only legal effect is to amend or repeal other instruments, and that makes no application, saving or transitional provision, is repealed by section 48A, on the day after the latest of the events the section lists (s 48A(1) and (2), F08). Cases: "Is my amending instrument repealed automatically" and "On what day is my amending instrument repealed". Asserted.
26. A provision of an instrument is repealed by section 48C where its only legal effect is to amend or repeal other instruments, and not where its only effect is to amend its own instrument; a provision that provides solely for commencement is repealed by section 48D unless the instrument is a commencement instrument (s 48C(1), s 48D(1)). Cases: "Is my provision repealed automatically as an amending provision" and "Is my commencement provision repealed automatically". Asserted.
27. A legislative instrument is repealed on the first 1 April or 1 October on or after the tenth anniversary of its registration; one registered on 1 January 2005 is repealed on the day the table in section 50(2) gives for the year it was made (s 50(1) and (2), F02, F16). Case: "On what day does my instrument sunset". Asserted.
28. Part 4 does not apply to an instrument whose enabling legislation facilitates an intergovernmental body or scheme and authorises the instrument, to one an Act says it does not apply to, or to one prescribed by regulation or made as a regulation for a listed purpose (s 54). Case: "Is my instrument exempt from sunsetting". Asserted.
29. The Attorney-General may issue a certificate deferring sunsetting where one of the three grounds in section 51(1)(b) holds, and the certificate may specify a 1 April or 1 October on or before the second anniversary of the sunsetting day (s 51(1), F15). Cases: "May the Attorney-General defer the sunsetting" and "Is the day in my certificate allowed". Asserted.
30. An instrument continues in force despite sections 50, 51 and 51A where a House passes a resolution that it should continue before the repeal day, the instrument being mentioned in a certificate copy or a list laid before that House (s 53(1)). Case: "Will a resolution keep my instrument in force". Asserted.
31. The Office of Parliamentary Counsel must provide the responsible rule-maker with a copy of a list laid under section 52(2) (s 52(3)); the first possible day of repeal, which section 52(1) uses, is not given in the text (F18). Case: "Will I be sent a copy of the list" asserts the first; the second is stated, not asserted.
32. The Register must contain the five kinds of document section 15A(2) lists and may contain additional documents the Counsel considers likely to be useful (s 15A(2) and (3)). Cases: "Must the Register contain the document" and "May the Register contain the additional document". Asserted.
33. An electronic copy of a registered law or explanatory statement is an authorised version where it is accessed at an approved website in the prescribed format and the website or the copy indicates, in the way the rules prescribe, that it is, or where it is in the prescribed format and the copy indicates that it is; a printed copy is an authorised version where it indicates, in the way the rules prescribe, that it is, or where it is produced directly from an authorised version; a copy that meets none of these routes is not (s 15ZA(1) to (4), F11). Case: "Is this copy an authorised version". Asserted.
34. In proceedings in a court or tribunal proof is not required of the matters section 15ZB(1) lists. Case: "Is proof of the matter not required in court". Asserted.

## Cross-references

`lga-provisions.l4` (the provision index) and `lga-xrefs.l4` (the cross-reference rows) are written by scripts kept outside the deposit; no row is typed by hand.
The script reads each in-scope line, finds every citation of a section, subsection, paragraph, Part, Division, Chapter or Subdivision (and "this Part"-style references), and looks the target up in the index it built from the text's own headings.
A reference to another Act is a row of its own kind and is not resolved.
Counts by kind: 163 section, 104 same section, 10 Part, 27 this container, and 17 references to other instruments; 304 rows in all.
4 of the rows point at a provision outside the scope; they are rows like any other with the scope shown as "out of scope".
Every row in the module resolves: its target is in the index and its pinpoint, where it has one, is present in the text; the module's tests assert that for each row and for the count.

## Time module

`lga-time.l4` imports only the prelude and `daydate`; `lga-tests-time.l4` asserts it (204 assertions, each answer worked out by hand from the text, with the boundary cases on both sides of every limit).
It holds every date, period and count the in-scope text states: days after an event (F01), months and years after a day (F02), counts of sitting days against a calendar given as an input (F03, F04), the period of s 46(2), the six months of s 48(1), the events of ss 48A to 48D (F08), the sunsetting day of s 50(1) and (2), and the days of ss 51, 51A, 52 and 53.
Every other module calls it and restates none of it.
A computation that does not close answers `NOTHING` and a test asserts that.

## What the stable binary does not accept

The encoding is written for the stable build (1.6.98) and compared with 1.6.110.
Where a skill page or the brief describes a construct the stable binary rejects, the binary governs.

**Stated in the brief or the dialects page, and not re-tested here:**

- No section-level `GIVEN`: every rule has its own `GIVEN`.
- No `REFUSE`, no `#ASSERT REFUSED` and no `BECAUSE`: a case the text does not cover is `NOTHING` in a `MAYBE`, and a test asserts it.
- No opaque `DECLARE` (a type with no body), no `@lang` line, no sets, and no `TYPICALLY` on a record field.
- No `YMD`: dates are written `Date day month year`.
- Each `#ASSERT` must sit on one line.
- `IMPORT` finds only modules in the importing file's own folder; a name defined in two imported modules cannot be used at all, so every rule and constructor name here is unique across modules.

**Found while writing, each hit once (loud unless it says silent):**

- Silent: `NOT x IMPLIES y` parses as `NOT (x IMPLIES y)`; write `(NOT x) IMPLIES y`. A test caught it in `s 15J(2)`.
- Silent: `Date 29 2 2023` is read as 1 March 2023 (an impossible day rolls forward), while `add months` and `add years` clamp to the last day of the month (`add months (Date 31 8 2025) 6` is 28 February 2026); the time module checks that the day number survives before it answers.
- `NOT a AND b` must be bracketed.
- A `LIST` used as a function argument must be in brackets: `f (LIST a, b)`.
- A list of records written with a comma at the start of each line fails on indentation; write `LIST` and then bracketed items.
- `ELSE IF c THEN a ELSE CONSIDER ...` fails on indentation; put the `ELSE` on its own line and nest the `IF` or `CONSIDER` under it.
- Comparing two `DATE` values in a module that imports only `prelude` fails with "multiple definitions" for `__GEQ__` or `__LT__`; `IMPORT daydate` (directly, or through `lga-time`) makes the comparison resolve.
- `NOTHING EQUALS x` is a parse error; put the `MAYBE` on the left of `EQUALS`.
- Three names were defined in two modules and were renamed after a scan of every module (`any other document for section 15Z`, `any other error for section 15X(4)`, `an initial explanatory statement to be delivered under section 39`).


## What `check.sh` prints

From the encoding folder, with `L4` set to the 1.6.98 build and `L4_MAIN` to the 1.6.110 build:

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.110 (main, e51181d, 2026-11-11)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
lga-authorised.l4                              0         0       0        0         0 |      0         0       0        0  same
lga-cases-seat.l4                              0       176       0        0         0 |      0       176       0        0  same
lga-compilations.l4                            0         0       0        0         0 |      0         0       0        0  same
lga-defs.l4                                    0         0       0        0         0 |      0         0       0        0  same
lga-drafting.l4                                0         0       0        0         0 |      0         0       0        0  same
lga-instruments.l4                             0         0       0        0         0 |      0         0       0        0  same
lga-nouns.l4                                   0         0       0        0         0 |      0         0       0        0  same
lga-provisions.l4                              0       115       0        0         0 |      0       115       0        0  same
lga-register.l4                                0         0       0        0         0 |      0         0       0        0  same
lga-repeal.l4                                  0         0       0        0         0 |      0         0       0        0  same
lga-scrutiny.l4                                0         0       0        0         0 |      0         0       0        0  same
lga-seat.l4                                    0         0       0        0         0 |      0         0       0        0  same
lga-sunset.l4                                  0         0       0        0         0 |      0         0       0        0  same
lga-tests-authorised.l4                        0        98       0        0         0 |      0        98       0        0  same
lga-tests-compilations.l4                      0       173       0        0         0 |      0       173       0        0  same
lga-tests-defs.l4                              0       147       0        0         0 |      0       147       0        0  same
lga-tests-drafting.l4                          0        25       0        0         0 |      0        25       0        0  same
lga-tests-instruments.l4                       0        90       0        0         0 |      0        90       0        0  same
lga-tests-register.l4                          0       194       0        0         0 |      0       194       0        0  same
lga-tests-repeal.l4                            0        50       0        0         0 |      0        50       0        0  same
lga-tests-scrutiny.l4                          0       109       0        0         0 |      0       109       0        0  same
lga-tests-sunset.l4                            0        82       0        0         0 |      0        82       0        0  same
lga-tests-time.l4                              0       204       0        0         0 |      0       204       0        0  same
lga-time.l4                                    0         0       0        0         0 |      0         0       0        0  same
lga-xrefs.l4                                   0       323       0        0         0 |      0       323       0        0  same
TOTAL (25 modules)                             0      1786       0        0           |      0      1786       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

`python3 -I srcrefs.py check ../../registers/source-bundle/C2004A01224.txt lga-*.l4` and the same with `--strict` are run from the encoding folder; the result is in `encoding.json` under `checks`.

## What needs doing before the encoding is worth relying on

- A domain expert has to read every rule against the authorised text: this encoding was written from a converter's plain-text rendering, by one agent working alone.
- The forks above are the places where the text can be read two ways; each needs a ruling, and the 21 numbered forks and the site lists under F09, F19 and F20 are the whole of them.
- The rules, the regulations and other Acts the text hands things to are not among the sources: the formats and indications the rules prescribe, the information the regulations prescribe, the section 61A rules, the Acts Interpretation Act 1901 and the Parliamentary Counsel Act 1970 are plain inputs, never looked up.
- The sitting-day calendars are inputs; nothing here knows when the Houses sit. The seat asks for the position of a day in the calendar, which the officer must count correctly.
- The open-textured words ("as soon as practicable", "considers", "appropriate", "reasonably practicable", "spent or no longer required") are plain inputs and are not decided.
- Section 52(1)'s "first possible day" is an input (F18).
- The seat questions have not been shown to an officer: the `@desc` wording has not been tested on a reader.
- A deploy to a service has not been tried.

