# NOTES: Art. 336, 336a and 336b of the Swiss Code of Obligations (OR, SR 220), abusive termination of an employment contract, whole, in L4 (stable)

**Status: draft, not reviewed by any domain expert.**
No Swiss employment lawyer has read this encoding against the text.
The encoder is one Sonnet 5.5 agent working alone from the brief (`BRIEF.md`, a copy of which sits beside this file), with the two skills and the Commons guide copies as its only references.
Every claim in this file was checked the way its sentence says: a command and its output, a case that asserts it, or "reading of the text, not asserted".

**The text is a script rendering, not the official text.**
`inputs/ch-or-sr220-art-336-336b-20261001.txt` is Fedlex's consolidated German version applicable from 2026-10-01 rendered by a converter script (`akn_to_text.py`); it is not the official text.
Whether the consolidated version on Fedlex or only the publication in the Official Compilation of Federal Legislation is authoritative was not established (`SOURCE-LICENSE.md` and `inputs/STUB-SOURCE-LICENSE.md`).
Nothing in this encoding is "verified against the official text".
The English in identifiers, `@desc` strings, comments and this file is the encoder's gloss, not the law; the German is quoted exactly, in `-- src:` lines, and `srcrefs.py` checks each quotation against the file.

**Target compiler: `main`.**
Written with `l4` 1.6.110 (main, e51181d, 2026-11-11), sha256 `9c7656f74151383da2c7344ad53269a8754bd874af8eb513180d61dc145016c7`, at `<scratchpad>/bin/l4-main-110`.
Compared by `check.sh` with the second stable build 1.6.109 (main, 4c887e0, 2026-11-04).
`JL4_LIBRARY_PATH` was left unset throughout.

## Seat

**The seat is an employee**: one person in one employment with one employer, asking on facts they can state whether a notice of termination (their employer's, or their own) is abusive, what they can claim and how much at most, and by when they must object and sue.
**The second seat is the employer**: a person or business that employs one employee, asking on facts it can state whether a notice it gave (or received) is abusive, what it can be made to pay and how much at most, and what the other side must do, and by when, to keep a claim.

Why these two.
The Articles apply to a notice given by "eine Partei" and put the consequences on "die Partei, die ... kündigt" and "die andere Partei": the individual to whom the law is applied is whichever party gave or received the notice, and in an employment relation that is one of exactly two people.
Employment law gives both seats (Guide section 2), and Art. 336(2) is addressed to the employer alone, so the employee's seat asks about it as "my employer's notice".
There is no seat for the judge: what the judge does ("vom Richter ... festgesetzt") is encoded for what it means to the person, namely the ceiling on what the compensation can be.

How the two seats are built.
Each seat module (`or336-seat.l4`, `or336-seat-employer.l4`) IMPORTs the layer-1 modules and calls their rules; it never restates a rule, and no layer-1 module changed to suit it.
Every question takes plain inputs (yes/no, a date, a number, one choice from a list), each with an `@desc` worded as that person would be asked, and the questions sit under `§` headings in the order of the Articles.
The employer's question names all start "As the employer," so that two seat modules never define the same name; both seats are generated from one table by a script, `work/gen_seats.py`, which is scratch and not deposited, so the `.l4` files are the source of record.
The facts about the grounds are asked from the position of "the person who received the notice" (the text's "die andere Partei"), and each `@desc` says who that is for the person asking.
A flag input (`my employer gave the notice` in the employee's seat, `I gave the notice` in the employer's) chooses the party for the questions about Art. 336(2) and for the aggregate; the compensation questions fix the giver in their wording ("the notice my employer gave me", "the notice I gave").
The employer's seat has six questions more than the employee's.
One is "is this amount within the cap" (question 12), which has no twin.
The other five exist because Art. 336(1) covers a notice given by either party, so the employer can be the party that received the notice (F31): it asks whether its own objection is valid (22), the last day to object (23), whether it can assert its claim (21), the last day to bring its action (24) and whether its claim is forfeited (25), each with the employer's own facts, under a heading of their own.
They are the twins of the employee's questions 15, 16, 17, 18 and 19, they call the same layer-1 rules, and the mirror module asserts that each pair agrees on the same facts.
The employer's questions 17 to 20 (and 16) keep their wording for an employer that gave the notice ("the other side").
Where a question does not read some facts, the seat gives them a fixed placeholder, and a comment on the binding says why.

Where the seats depart from the defaults ruled for Commons (recorded, not hidden): the questions are asked of a notice that either party may have given, because Art. 336(1) says "eine Partei"; judgments the text leaves to the person (connection with the employment, impairment of cooperation, justified reason, good faith, mass dismissal, consultation) are plain facts; the notice period and the day the employment ends are dates the person states, because they are outside the three Articles.

## Jural relations

Hohfeld's correlatives: a claim is matched by a duty; a privilege by a no-right; a power by a liability (being subject to the power, not an obligation); an immunity by a disability.
Each relation is stated once, in layer 1, between two parties.
"Giver" is the party that gave the notice; "recipient" is the party that received it; either can be the employer or the employee.

| provision | holder | right, privilege, power or immunity | bearer | correlative | L4 rule |
| --- | --- | --- | --- | --- | --- |
| Art. 336(1) chapeau, (a) to (e) | none | none: these provisions define when a notice is "missbräuchlich"; what follows from the status is in Art. 336a | none | none | `Art 336(1)(a) the notice is abusive` to `Art 336(1)(e) the notice is abusive`, `Art 336(1) a ground in paragraph 1 makes the notice abusive` |
| Art. 336(2) chapeau, (a) to (c) | none | none: the same, for the employer's notice only | none | none | `Art 336(2)(a) the notice is abusive`, `Art 336(2)(b) the notice is abusive`, `Art 336(2)(c) the notice is abusive`, `Art 336(2) a ground in paragraph 2 makes the notice abusive` |
| Art. 336(3) | none | none: a counting rule that extends "while the employee is a representative" to the time the mandate would have lasted | none | none | `Art 336(3) the protection of the employee representative continues` |
| Art. 336a(1) | recipient | claim to a compensation | giver | duty to pay it (no time named) | `Art 336a(1) the party giving notice owes the other party compensation`, `Art 336a(1) the duty to pay compensation` |
| Art. 336a(2) first clause | the judge | power to fix the amount on all the circumstances | giver (and recipient, as to what they can claim) | liability to the judge's fixing | `Art 336a(2) the amount of the compensation` (NOTHING: the amount is the judge's) |
| Art. 336a(2) second clause | giver | immunity against an award above six months' wages | the judge and the recipient | disability to award or claim more | `Art 336a(2) the cap of six months' wages`, `Art 336a(2) the compensation stays within the cap` |
| Art. 336a(2) third clause | recipient | claim to damages on another legal basis, preserved | giver | duty on that other basis, preserved; the cap does not limit it | `Art 336a(2) the cap limits this claim` |
| Art. 336a(3) | giver of a notice abusive under Art. 336(2)(c) | immunity against an award above two months' wages | the judge and the recipient | disability to award or claim more | `Art 336a(3) the cap of two months' wages`, `Art 336a(2) and (3) the most the compensation can be` |
| Art. 336b(1) | recipient | power to object in writing and so keep the claim alive; "muss" makes it a burden, which has no correlative right in the giver | giver | liability to the objection | `Art 336b(1) the objection meets the requirements`, `Art 336b(1) the last day to object`, `Art 336b(1) the duty to object` (F28) |
| Art. 336b(2) first sentence | recipient | power to assert the compensation claim after a valid objection and no agreement to continue | giver | liability to the claim | `Art 336b(2) the party that received the notice can assert the compensation claim` |
| Art. 336b(2) second sentence | giver | immunity: once 180 days after the end of the employment pass with no action made pending, the claim is forfeited | recipient | disability to enforce it | `Art 336b(2) the claim is forfeited`, `Art 336b(2) the last day to bring the action`, `Art 336b(2) the window to bring the action` (F28) |
| Art. 336b(2) second sentence, the action | recipient | power to make an action pending within the 180 days | giver | liability to the action | `Art 336b(2) the window to bring the action` |

No provision of the three Articles creates a privilege or a no-right in so many words.
Nothing here gives a seat to the judge; the judge's powers appear only as what they mean for the two parties.

## What is encoded and what is not

Encoded, whole: Art. 336 (the grounds in paragraphs 1 and 2, and the extension of paragraph 3), Art. 336a (the compensation, its two ceilings, the reservation of damages on another legal basis) and Art. 336b (the written objection, the period for it, the assertion of the claim, the 180 days and the forfeiture).
Layer 1 is `or336-nouns.l4` (the types), `or336-art336.l4`, `or336-art336a.l4`, `or336-art336b.l4`, with tests in `or336-tests-art336.l4`, `or336-tests-art336a.l4`, `or336-tests-art336b.l4` and `or336-traces.l4`; layer 2 is the two seats and their case modules, plus `or336-cases-mirror.l4`.

Not encoded, and why:
- The amount of the compensation: the text hands it to the judge, so the encoding computes only the ceiling and answers NOTHING for the amount (F17).
- Art. 333 and Art. 335f: context for two cross-references (Art. 336(2)(c) and (3)); they are not among the scope, and get no rows.
- Art. 335d (what a mass dismissal is), Art. 335 to 335c (notice periods) and the day the employment ends: outside the sources; asked as plain facts (F12, F27).
- Art. 336c and 336d, the Gender Equality Act, the Civil Code, and any case law: not in the sources.
- The procedure after an action is made pending (the court's handling): the text says nothing about it.

## Coverage table

Built by a script (`work/coverage.py`, scratch) from the text itself, one row per heading, article, paragraph, limb and sentence clause of the file, plus one row for each term the text uses and does not define.
The script checks that every non-blank line of the text falls in some row (footnote lines fall in the row of the provision that carries their marker, and are described there, since footnotes get no rows of their own), that every function a row names is defined in a layer-1 module, and that every fork a row names has an entry below.
Dispositions are `encoded`, `inert` (with its reason: 1 not operative, 2 machinery, 3 shown repealed or blank), `fork` (the text reads two ways; the row points at the fork entry and at the rule that encodes the chosen reading, or at the explicit NOTHING) or `repealed`.
There is no out-of-scope row and no deferred row.

| row | lines | provision | disposition | functions | forks | tested in | note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R01 | 1 | Title line of the deposited file | inert (reason 1) |  |  |  | The converter's title line; not the Act. |
| R02 | 3-5 | The deposit's own header: source, conversion note, status of the rendering | inert (reason 1) |  |  |  | Provenance of the deposit, written by the converter; not part of the Act. NOTES.md says the text is a script rendering, not the official text. |
| R03 | 7 | Zweite Abteilung: Die einzelnen Vertragsverhältnisse | inert (reason 1) |  |  |  | Heading. |
| R04 | 8 | Zehnter Titel: Der Arbeitsvertrag | inert (reason 1) |  |  |  | Heading. fn 1: Fassung gemäss (amended text), in Kraft seit 1. Jan. 1972 |
| R05 | 9 | Erster Abschnitt: Der Einzelarbeitsvertrag | inert (reason 1) |  |  |  | Heading. |
| R06 | 10 | G. Beendigung des Arbeitsverhältnisses | inert (reason 1) |  |  |  | Heading. |
| R07 | 11 | III. Kündigungsschutz | inert (reason 1) |  |  |  | Heading. |
| R08 | 12 | 1. Missbräuchliche Kündigung | inert (reason 1) |  |  |  | Heading. |
| R09 | 13 | a. Grundsatz | inert (reason 1) |  |  |  | Heading. |
| R10 | 15 | Art. 336 (article heading) | inert (reason 1) |  |  |  | Heading; the amendment history is footnote 2. fn 2: Fassung gemäss (amended text), in Kraft seit 1. Jan. 1989 |
| R11 | 16 | Art. 336(1) chapeau: a notice is abusive if a party gives it on a ground below | fork | `Art 336(1) a ground in paragraph 1 makes the notice abusive`<br>`Art 336 a ground the Article lists makes the notice abusive` | F1, F9 | or336-tests-art336.l4, or336-cases-seat.l4, or336-cases-seat-employer.l4, or336-cases-mirror.l4 | The chapeau and the aggregate. Term row R44 (missbräuchlich) is this and Art. 336(2). |
| R12 | 17 | Art. 336(1)(a): because of a characteristic that the other party holds by virtue of personality, unless connected with the employment or substantially impairing cooperation | fork | `Art 336(1)(a) the notice is abusive` | F2, F4 | or336-tests-art336.l4, or336-cases-seat.l4, or336-cases-seat-employer.l4, or336-cases-mirror.l4 |  |
| R13 | 18 | Art. 336(1)(b): because the other party exercises a constitutional right, unless the exercise breaches a duty from the employment or substantially impairs cooperation | fork | `Art 336(1)(b) the notice is abusive` | F3, F4 | or336-tests-art336.l4, or336-cases-seat.l4, or336-cases-seat-employer.l4, or336-cases-mirror.l4 |  |
| R14 | 19 | Art. 336(1)(c): exclusively to thwart the arising of the other party's claims from the employment | fork | `Art 336(1)(c) the notice is abusive` | F5 | or336-tests-art336.l4, or336-cases-seat.l4, or336-cases-seat-employer.l4, or336-cases-mirror.l4 |  |
| R15 | 20 | Art. 336(1)(d): because the other party asserts claims from the employment in good faith | encoded | `Art 336(1)(d) the notice is abusive` | F6 | or336-tests-art336.l4, or336-cases-seat.l4, or336-cases-seat-employer.l4, or336-cases-mirror.l4 | Open-textured: good faith is a plain input (F6 records it; no second reading changes an outcome). |
| R16 | 21 | Art. 336(1)(e): because the other party performs Swiss compulsory military or civil protection service or Swiss civilian service, or fulfils a legal duty not voluntarily assumed | fork | `Art 336(1)(e) the notice is abusive` | F7 | or336-tests-art336.l4, or336-cases-seat.l4, or336-cases-seat-employer.l4, or336-cases-mirror.l4 | Footnote 3: amended by the Civil Service Act of 6 October 1995, in force from 1 October 1996. fn 3: Fassung gemäss (amended text), in Kraft seit 1. Okt. 1996 |
| R17 | 22 | Art. 336(2) chapeau: the employer's notice is in addition abusive if given on a ground below | fork | `Art 336(2) a ground in paragraph 2 makes the notice abusive` | F8 | or336-tests-art336.l4, or336-cases-seat.l4, or336-cases-seat-employer.l4, or336-cases-mirror.l4 | For a notice given by the employee the paragraph says nothing (NOTHING). |
| R18 | 23 | Art. 336(2)(a): because the employee belongs or does not belong to an employees' association, or lawfully takes part in union activity | encoded | `Art 336(2)(a) the notice is abusive` | F8 | or336-tests-art336.l4, or336-cases-seat.l4, or336-cases-seat-employer.l4, or336-cases-mirror.l4 | The employee-notice branch is F8; there is no further reading of this limb. |
| R19 | 24 | Art. 336(2)(b): while the employee is an elected employee representative in a body of the business or an institution connected with the undertaking, and the employer cannot prove a justified reason | fork | `Art 336(2)(b) the notice is abusive` | F10, F11, F30 | or336-tests-art336.l4, or336-cases-seat.l4, or336-cases-seat-employer.l4, or336-cases-mirror.l4 |  |
| R20 | 25 | Art. 336(2)(c): in the course of a mass dismissal without consulting the employee representation (or, if there is none, the employees) | fork | `Art 336(2)(c) the notice is abusive` | F12 | or336-tests-art336.l4, or336-cases-seat.l4, or336-cases-seat-employer.l4, or336-cases-mirror.l4 | Footnote 4: inserted by the Federal Act of 17 December 1993, in force from 1 May 1994. fn 4: Eingefügt (inserted), in Kraft seit 1. Mai 1994 |
| R21 | 26 | Art. 336(3): protection of an employee representative whose mandate ends on a transfer (Art. 333) | fork | `Art 336(3) the protection of the employee representative continues` | F13 | or336-tests-art336.l4, or336-cases-seat.l4, or336-cases-seat-employer.l4, or336-cases-mirror.l4 | Footnote 5: inserted by the Federal Act of 17 December 1993, in force from 1 May 1994. Art. 333 is context only. fn 5: Eingefügt (inserted), in Kraft seit 1. Mai 1994 |
| R22 | 28 | Zehnter Titel: Der Arbeitsvertrag (second heading) | inert (reason 1) |  |  |  | Heading; footnote 6 repeats the amendment history of the title. fn 6: Fassung gemäss (amended text), in Kraft seit 1. Jan. 1972 |
| R23 | 29 | b. Sanktionen | inert (reason 1) |  |  |  | Heading. |
| R24 | 31 | Art. 336a (article heading) | inert (reason 1) |  |  |  | Heading; the amendment history is footnote 7. fn 7: Fassung gemäss (amended text), in Kraft seit 1. Jan. 1989 |
| R25 | 32 | Art. 336a(1): the party that terminates abusively owes the other party a compensation | fork | `Art 336a(1) the party giving notice owes the other party compensation`<br>`Art 336a(1) the duty to pay compensation` | F14, F28 | or336-tests-art336a.l4, or336-traces.l4, or336-cases-seat.l4, or336-cases-seat-employer.l4, or336-cases-mirror.l4 | Stated once, neutrally: either party can owe it. |
| R26 | 33 (i) | Art. 336a(2) first clause: the judge fixes the compensation on all the circumstances | fork | `Art 336a(2) the amount of the compensation` | F17 | or336-tests-art336a.l4 | The amount is the judge's: the encoding answers NOTHING. |
| R27 | 33 (ii) | Art. 336a(2) second clause: the compensation may not exceed the employee's wages for six months | fork | `Art 336a(2) the cap of six months' wages`<br>`Art 336a(2) the compensation stays within the cap`<br>`Art 336a(2) and (3) the most the compensation can be` | F15, F16 | or336-tests-art336a.l4, or336-cases-seat.l4, or336-cases-seat-employer.l4, or336-cases-mirror.l4 | The ceiling is computed from a monthly wage the person states. |
| R28 | 33 (iii) | Art. 336a(2) third clause: damages claims on another legal basis are reserved | fork | `Art 336a(2) the cap limits this claim` | F18 | or336-tests-art336a.l4, or336-cases-seat.l4, or336-cases-seat-employer.l4, or336-cases-mirror.l4 |  |
| R29 | 34 | Art. 336a(3): if the notice is abusive under Art. 336(2)(c), the compensation may not exceed two months' wages | fork | `Art 336a(3) the cap of two months' wages`<br>`Art 336a(2) and (3) the most the compensation can be` | F16 | or336-tests-art336a.l4, or336-cases-seat.l4, or336-cases-seat-employer.l4, or336-cases-mirror.l4 | Footnote 8: inserted by the Federal Act of 17 December 1993, in force from 1 May 1994. fn 8: Eingefügt (inserted), in Kraft seit 1. Mai 1994 |
| R30 | 36 | Zehnter Titel: Der Arbeitsvertrag (third heading) | inert (reason 1) |  |  |  | Heading; footnote 9 repeats the amendment history of the title. fn 9: Fassung gemäss (amended text), in Kraft seit 1. Jan. 1972 |
| R31 | 37 | c. Verfahren | inert (reason 1) |  |  |  | Heading. |
| R32 | 39 | Art. 336b (article heading) | inert (reason 1) |  |  |  | Heading; the amendment history is footnote 10. fn 10: Fassung gemäss (amended text), in Kraft seit 1. Jan. 1989 |
| R33 | 40 | Art. 336b(1): whoever wants to assert compensation under Art. 336 and 336a must object to the notice in writing, with the party that gave it, at the latest by the end of the notice period | fork | `Art 336b(1) the objection meets the requirements`<br>`Art 336b(1) the last day to object`<br>`Art 336b(1) the duty to object` | F19, F20, F26, F27, F28, F29, F31 | or336-tests-art336b.l4, or336-traces.l4, or336-cases-seat.l4, or336-cases-seat-employer.l4, or336-cases-mirror.l4 |  |
| R34 | 41 (i) | Art. 336b(2) first sentence: if the objection was valid and the parties do not agree on continuing the employment, the party that received the notice can assert the claim | fork | `Art 336b(2) the party that received the notice can assert the compensation claim` | F21, F31 | or336-tests-art336b.l4, or336-cases-seat.l4, or336-cases-seat-employer.l4, or336-cases-mirror.l4 |  |
| R35 | 41 (ii) | Art. 336b(2) second sentence: if no action is made pending within 180 days after the end of the employment, the claim is forfeited | fork | `Art 336b(2) the last day to bring the action`<br>`Art 336b(2) the claim is forfeited`<br>`Art 336b(2) the window to bring the action` | F22, F23, F24, F25, F26, F28 | or336-tests-art336b.l4, or336-traces.l4, or336-cases-seat.l4, or336-cases-seat-employer.l4, or336-cases-mirror.l4 |  |
| R36 | term | missbräuchlich (abusive), the only term the three Articles give a content to, by the grounds of Art. 336(1) and (2) (lines 16 and 22) | encoded | `Art 336(1) a ground in paragraph 1 makes the notice abusive`<br>`Art 336(2) a ground in paragraph 2 makes the notice abusive`<br>`Art 336 a ground the Article lists makes the notice abusive` | F1 | or336-tests-art336.l4, or336-cases-seat.l4, or336-cases-seat-employer.l4, or336-cases-mirror.l4 | Defined by 'ist missbräuchlich, wenn': one decision per ground, and the two aggregates. The aggregate answers 'a ground the Article lists', never 'abusive' without the list (F1). |
| R37 | term | Lohn (wages), used in Art. 336a(2) and (3) and not defined in the encoded text | fork | `Art 336a(2) the cap of six months' wages`<br>`Art 336a(3) the cap of two months' wages` | F15 | or336-tests-art336a.l4 | Undefined term: the person states the monthly wage as a number. |
| R38 | term | Massenentlassung (mass dismissal), used in Art. 336(2)(c); Art. 335d is outside the sources | fork | `Art 336(2)(c) the notice is abusive` | F12 | or336-tests-art336.l4, or336-cases-seat.l4, or336-cases-seat-employer.l4, or336-cases-mirror.l4 | Borrowed term: asked as a plain fact. |
| R39 | term | Kündigungsfrist (notice period) and Beendigung des Arbeitsverhältnisses (end of the employment), used in Art. 336b; Art. 335 to 335c are outside the sources | fork | `Art 336b(1) the last day to object`<br>`Art 336b(2) the last day to bring the action` | F27 | or336-tests-art336b.l4, or336-cases-seat.l4, or336-cases-seat-employer.l4, or336-cases-mirror.l4 | Borrowed terms: the person states the two dates. |

Audit: the text file has 52 lines, of which 44 are non-blank (34 lines of the file's own header, headings and Articles, and 10 footnote lines described in the rows that carry their markers); the table has 39 rows (35 rows tied to lines of the text, 4 term rows); rows before this encoding: 0 (a new encoding, there was no earlier table); rows after: 39; the coverage script reported 0 problems (every non-blank line covered, every named function defined, every named fork registered).

Counts per disposition: encoded 3; fork 20; inert 16 (reason 1: 16; reason 2: 0; reason 3: 0); repealed or blank 0; total 39 rows.

No row was moved out of `inert`, because this is a new encoding and nothing was inert before; every inert row is a heading or the deposit's own header (reason 1).
Defined terms: the three Articles define one term only, "missbräuchlich" (R36), by the grounds of Art. 336(1) and (2); the other terms the text leans on and leaves undefined ("Lohn", "Massenentlassung", the notice period, the end of the employment) have their own rows (R37 to R39).

## Fork register

Each entry gives the provision, the readings seen, the one taken, the text that licenses each, the rule that carries the choice and the case that asserts it.
A fork is a site where the text can be read two or more ways with different outcomes.
The conventions ruled for this corpus (2026-10-29, 2026-11-04, 2026-11-05, 2026-11-12) are applied as the brief states them; where one of them decides an entry, the entry says which.
Per the case-by-case ruling of 2026-11-05, each "unless" once met, each unmet "if" or "where", and each period gets a fork line here for the human reviewer to overrule.

### F1 Art. 336(1) and Art. 336 as a whole: is the list of grounds closed?
Readings: (A) the grounds of paragraphs 1 and 2 are the only grounds, so a notice that meets none is not abusive; (B) the text lists grounds and does not say it lists all of them, so a notice that meets none is simply not covered by the list.
Text: (Text: "Die Kündigung eines Arbeitsverhältnisses ist missbräuchlich, wenn eine Partei sie ausspricht:") has no "nur" or "ausschliesslich" on the list as a whole.
Taken: the aggregate is named `Art 336 a ground the Article lists makes the notice abusive`, and its JUST FALSE says only that no listed ground is met on these facts; it never says that no other ground exists.
This follows reading (a) of the rule of 2026-10-29 (a failed "wenn" is the text's no, clause by clause); under reading (B) the otherwise-branch would be NOTHING.
Asserted by cases 44 and 46 (and, at layer 1, `or336-tests-art336.l4`).

### F2 Art. 336(1)(a): the exception "es sei denn" once met
Readings: (A) once the characteristic is connected with the employment or substantially impairs cooperation, the limb says no: JUST FALSE; (B) the exception removes the case from the limb and the text is silent about it: NOTHING.
Text: (Text: "es sei denn, diese Eigenschaft stehe in einem Zusammenhang mit dem Arbeitsverhältnis oder beeinträchtige wesentlich die Zusammenarbeit im Betrieb").
Taken: (A), because "es sei denn" is on the list of words by which the text says no in its own words (the brief, "unless" and "except").
Rule: `Art 336(1)(a) the notice is abusive`.
Asserted by cases 2 and 3.

### F3 Art. 336(1)(b): the exception "es sei denn" once met
Same as F2.
Text: (Text: "es sei denn, die Rechtsausübung verletze eine Pflicht aus dem Arbeitsverhältnis oder beeinträchtige wesentlich die Zusammenarbeit im Betrieb").
Taken: JUST FALSE.
Rule: `Art 336(1)(b) the notice is abusive`.
Asserted by cases 6 and 7.

### F4 Art. 336(1)(a) and (b), and all limbs with "wegen" or "weil": causation
Readings: (A) the ground must be the reason or the main reason for the notice; (B) it is enough that the ground is one reason among others; (C) the text sets no test.
Text: (Text: "wegen einer Eigenschaft, die der anderen Partei kraft ihrer Persönlichkeit zusteht") and "weil" in (b), (d), (e) and in paragraph 2(a).
Taken: (C) with the judgment left to the person: "the notice was given because of ..." is a plain yes/no input, so the encoding takes no side between (A) and (B); the person states the fact.
Rule: the first test of each limb function.
Asserted by cases 1, 4, 5, 8 and 12.

### F5 Art. 336(1)(c): "ausschliesslich" and a mixed purpose
Readings: (A) a notice with another purpose beside the thwarting of claims is outside the limb: JUST FALSE; (B) the text is silent on it: NOTHING.
Text: (Text: "ausschliesslich um die Entstehung von Ansprüchen der anderen Partei aus dem Arbeitsverhältnis zu vereiteln").
Taken: (A): "ausschliesslich" is the text's own word for "only", and the brief lists "only" among the words by which the text says no.
Rule: `Art 336(1)(c) the notice is abusive`.
Asserted by case 10.

### F6 Art. 336(1)(d): "nach Treu und Glauben"
Readings: (A) good faith qualifies the assertion of the claim (the person asserts it honestly); (B) it also requires that the claim exist or be well founded.
Text: (Text: "weil die andere Partei nach Treu und Glauben Ansprüche aus dem Arbeitsverhältnis geltend macht").
Taken: (A), as a plain input ("the person who received the notice asserted those claims in good faith"), because the text puts the phrase next to the assertion; (B) would need a judgment about the claim that the person cannot state as a fact.
If (A) is wrong the outcome differs only where claims are asserted in good faith and are unfounded.
Rule: `Art 336(1)(d) the notice is abusive`.
Asserted by cases 12, 13, 14.

### F7 Art. 336(1)(e): how far "obligatorischen" reaches, and what the legal duty is
Readings: (A) "obligatorischen" qualifies military service and civil protection service (Schutzdienst) and "schweizerischen Zivildienst" stands alone; (B) it qualifies all three.
Text: (Text: "schweizerischen obligatorischen Militär- oder Schutzdienst oder schweizerischen Zivildienst leistet oder eine nicht freiwillig übernommene gesetzliche Pflicht erfüllt").
Taken: military, civil protection and civilian service are three separate yes/no inputs, so the question asked of the person already says "compulsory" for the first two and nothing for the third; the encoding tests no further qualifier.
The legal duty is a fourth input, qualified by a fifth: the duty was voluntarily assumed.
Rule: `Art 336(1)(e) the notice is abusive`.
Asserted by cases 15 to 20 (case 17 is the civilian-service case).

### F8 Art. 336(2): a notice given by the employee
Readings: (A) the paragraph speaks of the employer's notice only, so for an employee's notice it says nothing: NOTHING; (B) it says that an employee's notice is not abusive on these grounds: JUST FALSE.
Text: (Text: "Die Kündigung des Arbeitsverhältnisses durch den Arbeitgeber ist im Weiteren missbräuchlich") limits the paragraph by its own wording.
Taken: (A), under reading (b) of the rule of 2026-10-29 (a prohibition or grant limited by its own wording does not say no outside the limit).
Rule: `Art 336(2)(a) the notice is abusive`, `(b)`, `(c)` and `Art 336(2) a ground in paragraph 2 makes the notice abusive`.
Asserted by cases 25, 34 and 41.
For the aggregate `Art 336 a ground the Article lists ...`, an employee's notice with only paragraph-2 reasons answers JUST FALSE (no listed ground is met: paragraph 1 is not met and paragraph 2 does not apply), asserted by case 46.

### F9 Art. 336(1): whose notice
Readings: (A) paragraph 1 applies to a notice given by either party; (B) it applies to the employer's notice only, as paragraph 2 does.
Text: (Text: "wenn eine Partei sie ausspricht") and, in paragraph 2, (Text: "im Weiteren") that adds the employer's grounds to those of paragraph 1.
Taken: (A): "eine Partei", "die andere Partei" in all five limbs, and the word "im Weiteren" in paragraph 2 which only makes sense if paragraph 1 was not already limited to the employer.
Rule: the limb functions take no party; the seats ask them without the flag.
Asserted by cases 45, 50 and 59 (an employee's notice that meets Art. 336(1)(d)).

### F10 Art. 336(2)(b): "begründeter Anlass" and who can prove it
Readings: (A) the employer's proof is a fact the person states; (B) the text sets a standard of proof the encoding must apply.
Text: (Text: "und der Arbeitgeber nicht beweisen kann, dass er einen begründeten Anlass zur Kündigung hatte").
Taken: (A): a plain input "the employer can prove a justified reason", asked from the position of the person asking ("Can your employer prove ...?", "Can you prove ...?").
The text names no standard and gives no definition of "begründeter Anlass".
Rule: `Art 336(2)(b) the notice is abusive`.
Asserted by cases 26 and 28.

### F11 Art. 336(2)(b): when "während ... ist" is tested
Readings: (A) at the day the notice is given; (B) at the day the notice takes effect.
Text: (Text: "während der Arbeitnehmer gewählter Arbeitnehmervertreter in einer betrieblichen oder in einer dem Unternehmen angeschlossenen Einrichtung ist"), present tense.
Taken: (A): "ausgesprochen wird" ties the verb to the day the notice is pronounced; the input asks whether the notice was given while the person was a representative.
Rule: `Art 336(2)(b) the notice is abusive`.
Asserted by cases 26 and 27 (the status stated at the notice).

### F12 Art. 336(2)(c): "Massenentlassung", consultation, and "falls es keine solche gibt"
Readings on the consultation: (A) when there is an employee representation, only its consultation counts, and the employees' consultation counts only when there is none; (B) either consultation suffices.
Text: (Text: "im Rahmen einer Massenentlassung, ohne dass die Arbeitnehmervertretung oder, falls es keine solche gibt, die Arbeitnehmer, konsultiert worden sind (Art. 335f)").
Taken: (A), by the words "falls es keine solche gibt".
"Massenentlassung" is defined in Art. 335d, which is outside the sources, so it is a plain yes/no input; whether a representation exists, whether it was consulted and whether the employees were consulted are three further plain inputs.
Rule: `Art 336(2)(c) the notice is abusive`.
Asserted by cases 35 to 41 (case 39 is the representation that was not consulted although the employees were).

### F13 Art. 336(3): the last day, and a mandate that did not end by transfer
Readings: (A) the protection lasts through the last day the mandate would have lasted, so a notice given on that day is protected; (B) it ends at the start of that day.
Text: (Text: "besteht so lange weiter, als das Mandat gedauert hätte, falls das Arbeitsverhältnis nicht übertragen worden wäre").
Taken: (A), inclusive: "so lange ... als" covers the day the mandate would still have been running.
Where the mandate did not end because of a transfer, paragraph 3 says nothing (the paragraph is limited to a mandate that ends "infolge Übergangs des Arbeitsverhältnisses"): NOTHING, and the status is then decided by paragraph 2(b) alone.
Rule: `Art 336(3) the protection of the employee representative continues`.
Asserted by cases 30, 31, 32 (the day, the day before, the day after) and by the layer-1 tests.

### F14 Art. 336a(1): a notice that is not abusive
Readings: (A) the duty is put on the party that gives an abusive notice and the text is silent about any other notice: NOTHING; (B) a notice that is not abusive gives no compensation: JUST FALSE.
Text: (Text: "Die Partei, die das Arbeitsverhältnis missbräuchlich kündigt, hat der anderen Partei eine Entschädigung auszurichten").
Taken: (A), under reading (b) of the rule of 2026-10-29: the provision names the class of notices that it burdens and says nothing outside it.
The function is named for a duty ("owes"), not for a grant or power, so the ruling of 2026-11-12 on functions named for a grant or a power does not apply.
Rule: `Art 336a(1) the party giving notice owes the other party compensation`.
Asserted by cases 49 and 51.

### F15 Art. 336a(2) and (3): "Lohn", and a cap computed from a monthly wage
Readings: (A) the cap is the monthly wage the person states times the number of months the text names (six, two); (B) "Lohn" includes elements (bonuses, allowances) the person must add up.
Text: (Text: "der dem Lohn des Arbeitnehmers für sechs Monate entspricht") and "für zwei Monate".
Taken: the person states one number, the wage for one month, and the encoding multiplies; "Lohn" is undefined in the sources, so what the figure includes is for the person (or a lawyer) to decide before asking.
A negative number is no wage, so the cap is NOTHING; a wage of 0 gives a cap of 0, which is a cap and not "no cap".
Rule: `Art 336a(2) the cap of six months' wages`, `Art 336a(3) the cap of two months' wages`.
Asserted by cases 52, 53, 57, 58 and the layer-1 tests (including a wage of 0).

### F16 Art. 336a(2) and (3): which ceiling governs when both apply
Readings: (A) where the notice is abusive under Art. 336(2)(c) both ceilings bind (both say "darf ... nicht"), so the lower, two months, governs even if the notice is also abusive on another ground; (B) paragraph 3 governs only if Art. 336(2)(c) is the sole ground.
Text: (Text: "Ist die Kündigung nach Artikel 336 Absatz 2 Buchstabe c missbräuchlich, so darf die Entschädigung nicht mehr als den Lohn des Arbeitnehmers für zwei Monate betragen").
Taken: (A): the paragraph is conditioned on the notice being abusive under (2)(c) and not on its being abusive only under it.
Rule: `Art 336a(2) and (3) the most the compensation can be`.
Asserted by cases 54 and 55 (case 55 has another ground too).

### F17 Art. 336a(2) first clause: the amount
Readings: (A) the text gives no rule for the amount: NOTHING; (B) any figure up to the ceiling can be asserted as the amount.
Text: (Text: "Die Entschädigung wird vom Richter unter Würdigung aller Umstände festgesetzt").
Taken: (A), whatever the facts.
Rule: `Art 336a(2) the amount of the compensation`.
Asserted by the layer-1 test for it.

### F18 Art. 336a(2) third clause: "vorbehalten"
Readings: (A) damages claims on another legal basis are reserved, so the cap does not limit them: JUST FALSE for "the cap limits this claim"; (B) the clause only says that such claims survive and is silent on whether the cap applies to them: NOTHING.
Text: (Text: "Schadenersatzansprüche aus einem anderen Rechtstitel sind vorbehalten").
Taken: (A): "vorbehalten" is read as the plain variant of "save" in the brief's list of words by which the text says no.
Rule: `Art 336a(2) the cap limits this claim`.
Asserted by case 62; a claim of any third kind is NOTHING (case 63).

### F19 Art. 336b(1): "bis zum Ende der Kündigungsfrist"
Readings: (A) the last day to object is the last day of the notice period; (B) the objection must be made before that day.
Text: (Text: "längstens bis zum Ende der Kündigungsfrist").
Taken: (A), inclusive, as the text fixes a period by its own words: outside it, JUST FALSE (the ruling of 2026-11-05 on periods, (a)).
Rule: `Art 336b(1) the last day to object`, `Art 336b(1) the objection meets the requirements`.
Asserted by cases 69, 70, 71 and the layer-1 tests (the day before, the day of, the day after).

### F20 Art. 336b(1): an objection that fails a requirement
Readings: (A) "muss ... schriftlich Einsprache erheben" is a flat requirement, so an objection that is not in writing, not against the notice, not made to the giver or late does not meet it: JUST FALSE; (B) the text is silent on the effect of failing the requirement: NOTHING.
Text: (Text: "Wer gestützt auf Artikel 336 und 336a eine Entschädigung geltend machen will, muss gegen die Kündigung längstens bis zum Ende der Kündigungsfrist beim Kündigenden schriftlich Einsprache erheben").
Taken: (A), as "muss" with a period and a form is the text's own requirement.
Rule: `Art 336b(1) the objection meets the requirements`.
Asserted by cases 72, 73, 74.

### F21 Art. 336b(2) first sentence: a power with a "wenn" gate
Readings: (A) an agreement to continue the employment fails the gate of the power and the text does not say no: NOTHING (the ruling of 2026-11-12, made by the coordinating session of the UK and Canada encodings and not confirmed by the maintainer: a function named for a power whose "if" gate failed answers NOTHING); an invalid objection is JUST FALSE, because Art. 336b(1) makes a valid objection a flat requirement for asserting the claim; (B) both NOTHING; (C) both JUST FALSE.
Text: (Text: "Ist die Einsprache gültig erfolgt und einigen sich die Parteien nicht über die Fortsetzung des Arbeitsverhältnisses, so kann die Partei, der gekündigt worden ist, ihren Anspruch auf Entschädigung geltend machen").
Taken: (A).
The invalid-objection branch is listed for the maintainer under limb 3 of the ruling, since "muss" is not one of "only if, only where, may not ... unless".
Rule: `Art 336b(2) the party that received the notice can assert the compensation claim`.
Asserted by cases 76 to 79.

### F22 Art. 336b(2): the 180 days
Readings: (A) the last day is the end of the employment plus 180 calendar days, so the end is day 0; (B) the day the employment ends is day 1, so the last day is the end plus 179.
Text: (Text: "Wird nicht innert 180 Tagen nach Beendigung des Arbeitsverhältnisses eine Klage anhängig gemacht, ist der Anspruch verwirkt").
Taken: (A), calendar days, inclusive of the 180th day; "nach Beendigung" counts from the day after the end.
Examples: 31 December 2026 + 180 = 29 June 2027; 31 December 2027 + 180 = 28 June 2028 (across 29 February 2028).
Rule: `Art 336b(2) the last day to bring the action`.
Asserted by cases 80 and 81 and the layer-1 tests, with dates computed on a calendar program independent of the encoding.

### F23 Art. 336b(2): an action made pending before the employment ended
Readings: (A) an action made pending before the end counts as in time; (B) the text names the closing edge only, and an earlier action is outside it.
Text: (Text: "innert 180 Tagen nach Beendigung des Arbeitsverhältnisses").
Taken: (A): the text sets a last day and no first day.
Rule: `Art 336b(2) the claim is forfeited`.
Asserted by the layer-1 test for an action brought before the employment ended.

### F24 Art. 336b(2): "anhängig gemacht"
Readings: filing, service on the other party, or another act in the court's procedure makes an action "pending".
Text: (Text: "eine Klage anhängig gemacht"): the three Articles do not say.
Taken: the person states the day the action was made pending; the encoding takes no side.
Rule: the input `the day the action was brought` of `Action on the claim`.
Asserted by cases 82 to 84.

### F25 Art. 336b(2): is forfeiture tied to a valid objection?
Readings: (A) the second sentence is independent: with no action in 180 days the claim is forfeited whatever happened to the objection; (B) it applies only where the first sentence's conditions are met.
Text: the second sentence is a separate sentence, (Text: "Wird nicht innert 180 Tagen nach Beendigung des Arbeitsverhältnisses eine Klage anhängig gemacht, ist der Anspruch verwirkt").
Taken: (A): the forfeiture function reads only the action, not the objection.
Rule: `Art 336b(2) the claim is forfeited`.
Asserted by cases 82 to 86 (they state no objection).

### F26 Regulative rules: where the clock starts
The text names no start for the periods of Art. 336b.
Taken, as an assumption: for the objection the clock starts on the day the notice was given and the period is the number of days to the end of the notice period (an input); for the action the clock starts on the day the employment ended.
The unit is days.
Rule: `Art 336b(1) the duty to object`, `Art 336b(2) the window to bring the action`.
Checked by `or336-traces.l4` and `check-traces.py`.

### F27 Art. 336b: the notice period and the end of the employment
Both are outside the three Articles (Art. 335 to 335c are not among the sources).
Taken: the person states the last day of the notice period and the day the employment ends, as dates.
Rule: `Art 336b(1) the last day to object`, `Art 336b(2) the last day to bring the action`.
Asserted by cases 75 and 80.

### F28 Regulative modality: MUST, MAY and DO
Readings for Art. 336b(1): (A) "muss ... Einsprache erheben" is a duty (MUST) whose breach is a BREACH; (B) it is a burden, a condition for asserting the claim, owed to nobody.
Taken: the closest form to the words, MUST, with `LEST BREACH BECAUSE "..."` saying in the reason that the BREACH stands for "the condition for asserting the claim is not met"; the Hohfeld table lists it as a burden.
Readings for Art. 336b(2): the text says what happens when the 180 days pass (the claim is forfeited) and imposes no duty to sue.
Taken: DO, because MAY with a LEST lapses to FULFILLED on the stable binary (probed on both builds, see "What the stable binary does not accept"), and DO carries both a HENCE and a LEST branch without a duty.
Art. 336a(1) names no time and no consequence, so its MUST has no WITHIN and no LEST (the trace at 1000 days stays RESIDUAL).
Rule: the three regulative rules.
Checked by `or336-traces.l4` and `check-traces.py`; each decision function carries the same content over the facts.

### F29 Art. 336b(1): "gestützt auf Artikel 336 und 336a"
Readings: (A) the objection requirement is limited to claims resting on Art. 336 and 336a, so for a claim on another legal basis (damages reserved by Art. 336a(2)) the provision says nothing: NOTHING; (B) it also covers those claims: JUST FALSE.
Text: (Text: "Wer gestützt auf Artikel 336 und 336a eine Entschädigung geltend machen will").
Taken: (A), under reading (b): the provision limits itself by its own wording.
The seats set the input to TRUE because every seat question is about the compensation of Art. 336 and 336a, and a comment on the binding says so.
Rule: `Art 336b(1) the objection meets the requirements`.
Asserted by the layer-1 test for a claim not under Art. 336 and 336a.

### F30 Art. 336(2)(b): the two bodies, and "gewählter"
Readings: the representative may sit in a body of the business ("betriebliche Einrichtung") or in an institution connected with the undertaking ("dem Unternehmen angeschlossene Einrichtung"); the text treats them alike.
Taken: two separate yes/no inputs, either of which makes the employee a protected representative; "gewählter" (elected) is part of the question wording and the person states the fact.
Rule: `Art 336(2)(b) the notice is abusive`.
Asserted by cases 26 and 27.

### F31 Art. 336b(1) and (2): the party that received the notice can be the employer
Readings: (A) "Wer ... eine Entschädigung geltend machen will" and "die Partei, der gekündigt worden ist" are whichever party received the notice, so an employer that receives an abusive notice from its employee has the same objection and the same claim as the employee has; (B) the procedure of Art. 336b is the employee's alone.
Text: (Text: "Wer gestützt auf Artikel 336 und 336a eine Entschädigung geltend machen will") and (Text: "so kann die Partei, der gekündigt worden ist, ihren Anspruch auf Entschädigung geltend machen"), read with "der anderen Partei" in Art. 336a(1) and "eine Partei" in Art. 336(1) (F9).
Taken: (A).
The layer-1 rule has no party in it.
The employer's seat asks it as questions 21 to 25 (the assertion, the validity of its objection, the last day to object, the last day to bring its action, forfeiture), with the employer's own facts worded for an employer that objects to its employee's notice, and each question answers the procedure only, as its twin in the employee's seat does: whether the notice was abusive is asked by the questions on Art. 336, with the flag "I gave the notice" answered no.
No question of the five has a rule of its own: each builds the same `Objection` or `Action on the claim` record from the employer's inputs and calls the layer-1 rule the employee's twin calls.
Under the ruling of 2026-11-12 the "parties agreed on continuing" branch stays NOTHING, and an invalid objection stays JUST FALSE (F21).
Rule: `Art 336b(2) the party that received the notice can assert the compensation claim`.
Asserted by cases 87 to 94 (the assertion: the employee's question 17 and the employer's question 21 on the same facts), by cases 69 to 75 and 80 to 86 (each now has an employer recipient-side twin on the same facts, for questions 22 to 25) and by cases 95 to 97 (new facts put to both seats), and by the mirror module, which asserts that each pair agrees.
Those cases include the day before, the day of and the day after the end of the notice period and the 180th day, and both sides of each requirement of the objection.

## Marginal readings for a lawyer

The two readings the brief says are for a lawyer to decide, not for the encoder, are: (a) a failed "if" counts as the text's no, clause by clause, within the provision that holds the "if"; (b) a prohibition or grant limited by its own wording does not say no outside the limit.
Every branch that rests on one is listed here with the other reading.

| function and branch | reading taken | the other reading |
| --- | --- | --- |
| `Art 336(1)(a)` to `(d)`, first branch: the ground's "weil" or "wegen" not met | (a): JUST FALSE | NOTHING |
| `Art 336(1)(c)`, `(d)`: the second clause ("ausschliesslich", "nach Treu und Glauben") not met | (a): JUST FALSE | NOTHING |
| `Art 336(1)(e)`: none of the four grounds met | (a): JUST FALSE | NOTHING |
| `Art 336(1) a ground in paragraph 1 ...`: no limb met | (a): JUST FALSE | NOTHING (F1) |
| `Art 336(2)(a)`: no reason met | (a): JUST FALSE | NOTHING |
| `Art 336(2)(b)`: not a representative; the employer proves a justified reason | (a): JUST FALSE | NOTHING |
| `Art 336(2)(c)`: not a mass dismissal; consultation happened | (a): JUST FALSE | NOTHING |
| `Art 336(2) a ground in paragraph 2 ...`: no limb met | (a): JUST FALSE | NOTHING |
| `Art 336 a ground the Article lists ...`: no listed ground met | (a): JUST FALSE | NOTHING (F1) |
| `Art 336(2)(a)`, `(b)`, `(c)`, `Art 336(2)`: notice given by the employee | (b): NOTHING | JUST FALSE (F8) |
| `Art 336(3)`: the mandate did not end by transfer | (b): NOTHING | JUST FALSE |
| `Art 336a(1)`: the notice is not abusive | (b): NOTHING | JUST FALSE (F14) |
| `Art 336a(2) the cap of six months' wages`: the notice is not abusive | (b): NOTHING | JUST FALSE |
| `Art 336a(3)`: the notice is not abusive under Art. 336(2)(c) | (b): NOTHING | JUST FALSE |
| `Art 336b(1) the objection meets the requirements`: the claim does not rest on Art. 336 and 336a | (b): NOTHING | JUST FALSE (F29) |
| `Art 336b(2) ... can assert ...`: the parties agreed on continuing | (b): NOTHING | JUST FALSE (F21) |
| `Art 336b(2) ... can assert ...`: no valid objection | JUST FALSE, through the flat "muss" of Art. 336b(1) | NOTHING (F21) |

The two readings left at the status quo are not mine to settle; each row above names the function and the branch so that a lawyer can overrule it by changing one `OTHERWISE` or `THEN`.

## Findings: what the text turns out to say

1. **Either party's notice can be abusive on the grounds of paragraph 1.** "Eine Partei" ... "die andere Partei" is symmetric, and the compensation of Art. 336a(1) runs from the giver to the other party, whoever is the employer (cases 45, 50, 59, and the mirror cases). Asserted.
2. **Paragraph 2 speaks only of the employer's notice.** For an employee's notice it says nothing; the encoding answers NOTHING and not FALSE (F8) (cases 25, 34, 41). Asserted.
3. **The grounds of paragraph 2 are added to those of paragraph 1** ("im Weiteren"); the encoding's aggregate for the employer's notice reads both (cases 42 and 43). Asserted.
4. **The text never says that its list of grounds is closed**; the aggregate's JUST FALSE therefore means "no listed ground is met", not "the notice is lawful" (F1) (cases 44, 46). Asserted.
5. **A mixed purpose takes a notice out of Art. 336(1)(c)** because of "ausschliesslich" (F5) (case 10). Asserted.
6. **The consultation of the employees counts for Art. 336(2)(c) only where there is no employee representation** (F12): a representation that was not consulted makes the notice abusive even though the employees were consulted (case 39). Asserted.
7. **The protection of Art. 336(3) is a period, not a status**: it runs through the last day the mandate would have lasted (cases 30, 31, 32). Asserted.
8. **The compensation is a ceiling, not a figure.** The judge fixes the amount; the text gives the ceiling as a count of months of wages, six, or two for the mass-dismissal ground. The encoding answers NOTHING for the amount and a number for the ceiling (the layer-1 test for the amount; cases 52 to 60). Asserted.
9. **Both ceilings bind where Art. 336(2)(c) applies**, so the lower, two months' wages, governs (F16) (cases 54, 55). Asserted.
10. **The reservation of damages on another legal basis is a statement about the cap**: the cap does not limit them (F18) (cases 61 to 63). Asserted.
11. **The objection is a condition of the claim, not a duty owed to anyone**, and the text names no consequence of failing it other than that the claim cannot be asserted (F28). Checked by the traces and by the objection cases (69 to 74).
12. **The two periods of Art. 336b run from different events and are independent**: the objection by the end of the notice period; the action within 180 days after the end of the employment, with no link to the validity of the objection (F25) (cases 69 to 71 and 82 to 86). Asserted.
13. **The 180 days are calendar days counted from the day the employment ended**; 31 December 2026 + 180 days is 29 June 2027, and 31 December 2027 + 180 days is 28 June 2028 (F22) (cases 80, 81). Asserted.
14. **An agreement to continue the employment leaves the claim neither asserted nor refused**: the text says what the party can do when there is no agreement and is silent when there is one (F21) (case 77). Asserted.
15. **Art. 336a(1) names no time for the payment and no consequence of not paying**, so the regulative duty has no WITHIN and never reaches BREACH (F28). Checked by the trace at 1000 days.
16. **The three Articles are identical in the consolidation applicable from 2027-07-01**, by the deposit's own record (`inputs/SOURCES.md`); the encoder did not check this, and the encoding is of the version applicable from 2026-10-01 only.
17. **The two seats answer the same facts identically**; a mirror module asserts it for every scenario that both seats ask (`or336-cases-mirror.l4`). Asserted.
18. **The party that received the notice can be the employer**: "die Partei, der gekündigt worden ist" and "die andere Partei" are not tied to the employee, so the employer seat asks Art. 336b(2) from the recipient's side too (F31), and the same objection and action facts give the same answer from both seats (cases 69 to 75, 80 to 97). Asserted.

### Reading a result: FALSE and NOTHING

In this row a `JUST TRUE` means that the text's own condition is met on the stated facts, and a `JUST FALSE` means that the text itself says no to the case in its own words, and nothing wider.
For the grounds of abusiveness `JUST FALSE` means: the ground's own conditions are not met, including an exception ("es sei denn") that is met.
For the aggregate it means only that no ground the Articles list is met on these facts; it does not say that the notice is lawful or that no other ground exists.
For the objection and the forfeiture it means that the requirement or the period the text fixes in its own words is not met.
`NOTHING` is "not covered": the text does not decide.
In this row that is: a paragraph that speaks of the employer's notice asked of the employee's; the protection after a transfer asked where the mandate did not end by transfer; the compensation asked where the notice is not abusive on a listed ground; the amount, which is the judge's; a claim of another kind, or one not resting on Art. 336 and 336a; an agreement to continue the employment; a negative wage.
A caller must never turn `NOTHING` into `FALSE`: "the text does not say" is not "no".
On the form that the seats feed, a question that answers NOTHING reads "the text does not decide this on your facts", and a question that answers JUST FALSE reads "on your facts the text says no".

## What the stable binary does not accept

Each entry below was met or probed while building this encoding, on 1.6.110 (and, where stated, on 1.6.109), and is sorted by how it shows.

Loud (the binary errors, so the author learns):
- **`ELSE IF ... ELSE NOTHING` chains.** `IF a THEN x` / `ELSE IF b THEN y` / `ELSE NOTHING` gave `incorrect indentation (got 10, should be greater than 10)` on the last line (probed 2026-11-17 on 1.6.110). Every decision here uses `BRANCH` instead.
- **A DEONTIC value in an `#ASSERT`.** `#ASSERT <regulative rule> EQUALS FULFILLED` gives `assertion could not be evaluated: Trying to check equality on types that do not support it` (probed on 1.6.110). So the three regulative rules cannot be asserted: they are run by `#TRACE`, and `check-traces.py` compares each printed outcome with an `-- EXPECT:` comment on both builds. The same duties are encoded as decision functions over the facts (the notice period and the 180 days).
- **A constructor named `A` or `B`.** `DECLARE Party IS ONE OF` with constructors `A` and `B` fails with `unexpected A` (probed on 1.6.110).

Silent (exit code 0, a wrong or surprising answer):
- **`MAY` with a `LEST` lapses to FULFILLED.** A `MAY sue WITHIN 10 ... LEST BREACH`, waited to day 11, prints `FULFILLED` on both 1.6.110 and 1.6.109, while the same rule with `DO` prints `DEONTIC BREACHED` (probed on both builds). `check.sh` does not see this, because a trace prints no assertion line: it is why Art. 336b(2) is written with `DO` (F28), and why `check-traces.py` exists.
- **`check.sh` cannot count a trace.** It counts error diagnostics and assertion lines only; a regulative rule that is wrong passes it. The 15 traces are checked by `check-traces.py`, and the mutation check (below) shows that changing a regulative period fails it.

Not used, so not tested here: `REFUSE`, `#ASSERT REFUSED`, `BECAUSE` outside `LEST BREACH BECAUSE`, section `GIVEN`, `TYPICALLY`, sets, `EVERY`, `YMD`; the brief says the stable binary rejects them and this encoding avoids them.
`Date day month year` and `WAITUNTIL` are used; umlauts in backtick identifiers are not used (identifiers are English), and umlauts in `-- src:` lines and strings are accepted.

## Tests and checks

What the tests cover: every branch of every layer-1 rule; the day before, the day of and the day after each period (the end of the notice period, 180 days after the end of the employment, the last day of the mandate of Art. 336(3)); the cap one below, on and one above; every seat question with the facts a person in the seat would state; mirror cases; and cases outside the encoding, each an asserted NOTHING.
Expected values were written by hand from the German text, beside each assertion, before the files were run; dates were counted on the calendar and checked with an independent calendar program, never taken from the encoding.

How the checks were run, and what each cannot see:
- `check.sh` (below): counts error diagnostics and assertion lines on both stable builds; every module has the same four counts on both.
- `check-traces.py`: runs `or336-traces.l4` with both builds and compares each trace's printed outcome with its `-- EXPECT:` comment. It cannot see a trace without an expectation (it reports one) or a difference no trace exercises.
- `python3 -I srcrefs.py check --refs <the raw text> <every .l4>`: every `-- src:N` quotation is an exact line of the text, and every `@ref` locator resolves.
- `mutation-check.py`: breaks one thing at a time in a copy of the encoding (41 mutants: 30 in layer 1, namely a flipped test, an off-by-one on every period, a wrong party, a wrong multiplier, a reversed exception; and 11 in the employer's recipient-side questions 21 to 25, namely a swapped or wrongly wired input, a constant in place of an input, the wrong layer-1 rule) and runs every module and the traces after each. A layer-1 mutant must be caught by the layer-1 tests and traces; a seat mutant by the seat cases. A mutant that leaves every check green is a gap. Its result is below.
- A grep for any `NOT` not followed by an opening parenthesis in every `.l4` file (the brief: parenthesise every `NOT`, because `NOT a AND b` parses as `NOT (a AND b)`): one hit, in `Art 336(2)(b)`, where `NOT` stood before a single identifier and could not capture an `AND`; it is parenthesised now, and the answer did not change.
- A negative test of the instrument itself: one expected value was changed in a copy of the folder, and `check.sh` on the copy exited 1 and printed one error and one failed assertion for that module on both builds.

### The check.sh output

Run as `L4=<l4-main-110> L4_MAIN=<l4-main-109> ./check.sh`, target `main`, with `l4` 1.6.110 (main, e51181d, 2026-11-11) and the main build 1.6.109 (main, 4c887e0, 2026-11-04); exit status 0.

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.109 (main, 4c887e0, 2026-11-04)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
or336-art336.l4                                0         0       0        0         0 |      0         0       0        0  same
or336-art336a.l4                               0         0       0        0         0 |      0         0       0        0  same
or336-art336b.l4                               0         0       0        0         0 |      0         0       0        0  same
or336-cases-mirror.l4                          0       106       0        0         0 |      0       106       0        0  same
or336-cases-seat-employer.l4                   0       111       0        0         0 |      0       111       0        0  same
or336-cases-seat.l4                            0        92       0        0         0 |      0        92       0        0  same
or336-nouns.l4                                 0         0       0        0         0 |      0         0       0        0  same
or336-seat-employer.l4                         0         0       0        0         0 |      0         0       0        0  same
or336-seat.l4                                  0         0       0        0         0 |      0         0       0        0  same
or336-tests-art336.l4                          0        76       0        0         0 |      0        76       0        0  same
or336-tests-art336a.l4                         0        38       0        0         0 |      0        38       0        0  same
or336-tests-art336b.l4                         0        28       0        0         0 |      0        28       0        0  same
or336-traces.l4                                0         0       0        0         0 |      0         0       0        0  same
TOTAL (13 modules)                             0       451       0        0           |      0       451       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

The baseline numbers it replaced: the first full run of `check.sh`, before the last layer-1 test was added, printed 389 satisfied, 0 errors, 0 failed, 0 refused on the same 13 modules on both builds.
The one assertion added afterwards (a wage of 0 under Art. 336a(3), which the mutation check showed was untested) made 390.
The first follow-up added the employer-as-recipient question (Art. 336b(2), question 21 of the employer's seat, with cases 87 to 94 in both seats and eight more mirror assertions) and made 414.
The second follow-up added the other four recipient-side questions (22 to 25: the objection, the last day to object, the last day to bring the action, forfeiture), employer twins on the same facts for cases 69 to 75 and 80 to 86, three new scenarios (95 to 97) put to both seats, and 17 more mirror assertions, and made 451; the table above is that final run, and no existing answer changed.
Every case and test file ends with assertions written equal to assertions satisfied: the `#ASSERT` lines are 76 + 38 + 28 in the three test files, and 92 + 111 + 106 in the three case files, which is the 451 above.
Every file also runs without a `DiagnosticSeverity_Warning` and without the layout diagnostics ("is at the end of the file", "follows code on its line") on both builds.

### The trace check

`check-traces: 30 trace checks (15 traces x 2 builds), 0 problems`

`or336-traces.l4` holds 15 traces: Art. 336a(1) paid early, paid late, not yet paid (the duty has no time limit, so no breach however long it waits); Art. 336b(1) on the day before, the day of and the day after the end of the notice period, for both parties; Art. 336b(2) on day 179, 180 and 181 after the end of the employment, for both parties.

### The source locators

`python3 -I srcrefs.py check --strict --refs inputs/ch-or-sr220-art-336-336b-20261001.txt or336-*.l4`: `srcrefs check: 71 src: lines, 42 runs, 57 locators, 0 problems`

### The mutation check

`L4=<l4-main-110> python3 -I mutation-check.py`: `41 mutants (30 in layer 1, 11 in the employer's seat), 0 survived every check, 0 were not caught by the checks meant to catch them (layer-1 mutants: the layer-1 tests and traces; seat mutants: the seat cases)`
No mutant survived and none was skipped.
The first run of this check had one survivor: a wage of 0 under Art. 336a(3) (the mutant turned `LESS THAN 0` into `AT MOST 0`), which no test exercised; the test was added and the mutant is now killed.
All 30 layer-1 mutants are killed by the layer-1 tests and traces alone, so the seat cases are a second, independent line of defence and not the only one.
All 11 mutants of the employer's recipient-side questions (21 to 25) are killed by the seat cases.


## What would need doing before the encoding is worth relying on

- A Swiss employment lawyer should read it against the official text, and settle the marginal readings above and the 31 fork entries, starting with F1 (is the list closed), F2 and F3 (the exceptions), F8 (the employee's notice and paragraph 2), F16 (which ceiling governs), F18 ("vorbehalten") and F21 (the power with a "wenn" gate).
- Whether the consolidated Fedlex text or only the Official Compilation is authoritative should be established (`SOURCE-LICENSE.md`), and the 2027-07-01 consolidation checked against it.
- The judgments the text leaves to the person (causation, good faith, justified reason, mass dismissal, what a "Lohn" includes) are plain inputs; a lawyer may want guidance text in the `@desc` strings, which the encoder had no source for.
- Art. 335 to 335c (notice periods) and Art. 335d (mass dismissal) are outside the sources: an encoding that includes them would turn the notice period and the mass-dismissal question from inputs into rules.
- The traces rest on an assumed clock (F26); a lawyer should say when each period starts.
- Nothing here was run through a deployed Legalese service; the `@export` and `@desc` annotations are untested beyond `l4 run`.

## Files

`or336-nouns.l4`, `or336-art336.l4`, `or336-art336a.l4`, `or336-art336b.l4` (layer 1); `or336-tests-art336.l4`, `or336-tests-art336a.l4`, `or336-tests-art336b.l4`, `or336-traces.l4` (layer-1 tests and traces); `or336-seat.l4`, `or336-cases-seat.l4` (employee's seat); `or336-seat-employer.l4`, `or336-cases-seat-employer.l4` (employer's seat); `or336-cases-mirror.l4` (the two seats agree); `check.sh`, `fetch-main-l4.sh`, `srcrefs.py`, `check-traces.py`, `mutation-check.py`; `NOTES.md`, `PROGRESS.md`, `encoding.json`, `SOURCE-LICENSE.md`, `BRIEF.md`.
