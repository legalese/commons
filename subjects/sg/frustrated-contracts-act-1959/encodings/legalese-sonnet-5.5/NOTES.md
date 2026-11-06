# NOTES: the Frustrated Contracts Act 1959 (Singapore), whole, on main

Status: draft.
Written 2026-11-05 by a single Sonnet 5.5 agent working alone from `BRIEF.md`; no domain expert has read it against the text (`encoding.json`, `not_reviewed`).
Target: `main`.
How verified: every module and every test file was run with `l4 run` on the main build 1.6.109 (main, 4c887e0, 2026-11-04) and on 1.6.108 (main, 2ae7c9b, 2026-11-02) through `check.sh`; the numbers are in "What check.sh prints" below.
The expected value of every assertion was written by hand from the text before the run.
A positive control was run twice on scratch copies, later discarded: first three runs, each with a deliberate break (the s 3(1) cut-off date; the s 2(6) exception; the s 2(3) ceiling and the s 2(2) net sum together), which turned assertions red in both the section tests and the seat cases (2 and 2, 1 and 1, 5 and 4 failed); then, for the sums taken together, two runs (the ceiling's `min` made `max`; the total made the first sum only), which turned 8 and 5, and 9 and 4, assertions red in the section tests and the seat cases.
The source is a plain-text rendering made by a converter script from Singapore Statutes Online; it is not the official text, and nothing here is "verified against the official text".

## Seat

The seat is **a party to a contract that has become impossible to perform, asking on facts they can state what happens to money paid or payable and to benefits already received, and whether the Act applies to the contract at all**.
Why this seat: section 2 is written about the parties' money and benefits ("sums paid or payable to any party", "a valuable benefit"), and section 3 is the answer to "does the Act reach my contract".
The two questions a person in that position asks first are the ones the brief names, and the Act answers both without leaving the contract and its parties.
There is never a seat for the court.
The Act names one actor who does anything, the court, and every provision that addresses only the court (ss 2(3), 2(5), 2(6), 2(7), 3(3), 3(4)) is encoded in layer 1 for what it decides (`fca-court.l4`, and the decision functions it calls) and in layer 2 only for what it means to the person: what the court may or must do with their money, their benefit or their contract.
Layer 2 is `fca-seat.l4` (32 exported questions in nine `§§` groups under one `§` heading, in the text's order, each input with an `@desc` worded as the person would be asked) and `fca-cases-seat.l4` (107 assertions, at least one per question and one "not covered" case among them).
It imports layer 1 and never restates a rule: every question is a call to a layer-1 function, and the only code in `fca-seat.l4` that is not such a call is the wiring that turns plain answers (yes/no, a number, a date, "Yes / No / I am not sure") into the records layer 1 expects.
Nothing in layer 1 was changed to suit it.

## What is encoded and what is not

Everything in the deposited text that creates a rule or defines a term is encoded: section 2 (subsections 1 to 7 and paragraphs 4(a) and 4(b)), section 3 (subsections 1 to 5 and paragraphs 5(a) to 5(c)), and the two things the Act defines for itself ("the time of discharge", "the benefited party").
Not encoded, and each with its inert reason in the coverage table: the cover page, the arrangement of sections, the long title, the date of enactment, headings, section 1 (short title), the legislative history and the abbreviations key, and the page furniture.
There is no `out-of-scope` row and no `deferred` row.

| file | what it holds |
| --- | --- |
| `sgia-p1-definitions.l4` | copied unchanged from Commons (see "Dependencies"); the Interpretation Act 1965 s 2(1) definitions |
| `fca-nouns.l4` | the facts a case is made of: contract, sums, expenses, benefit, obligor, insurance, severable part, with the two enumerations for ss 2(4) and 3(4) |
| `fca-definitions.l4` | the Act's own defined term and label (s 2(2), s 2(4)(a)); the four Interpretation Act words it uses, looked up |
| `fca-s3-application.l4` | section 3, imported by section 2 because section 2 is "subject to section 3" |
| `fca-s2-adjustment.l4` | section 2 |
| `fca-court.l4` | the court's permissions, prohibition and duties as `PARTY the court MAY / SHANT / MUST` rules, each guarded by the decision function that carries the same condition |
| `fca-tests-definitions.l4`, `fca-tests-s3.l4`, `fca-tests-s2.l4`, `fca-tests-court.l4` | tests of layer 1 (20, 64, 132 and 13 assertions; 15 traces) |
| `fca-seat.l4`, `fca-cases-seat.l4` | layer 2 (32 questions; 107 assertions) |

Reading order of the modules: nouns, definitions, section 3, section 2, court, seat.
The court's judgments are inputs, never computed: whether the court "considers it just" (ss 2(3), 2(7)), how much it allows (s 2(3)), what is consistent with the contract's own provision (s 3(3)), whether a part "can properly be severed" (s 3(4)), and the sum it "considers just" for a benefit (s 2(4)).
The Act sets no money amount, rate or period, so every number in the encoding is one the person or the court supplies.

## Coverage table

Built from the text by `coverage.py` (kept in this folder); `python3 -I coverage.py ../../../inputs/FCA1959.txt` audits it and exits non-zero on a problem.
Text units counted: 233 raw lines, 163 of them non-blank; every one of the 163 falls in exactly one primary row (46 primary rows).
Two overlay rows (T01, T02) record the Act's defined term and label, which sit inside rows R09 and R12.
Rows in the table when it was first built from the text: 48 (46 primary and 2 overlay); rows at the end: 48; no row was added or removed, and the dispositions of eight rows were changed from `encoded` to `fork` when the forks were written up.
Dispositions over all 48 rows: encoded 11, fork 8, inert (reason 1) 28, inert (reason 2) 1, repealed or blank 0.
No row was moved out of inert: every inert row is one of the reasons the brief allows (reason 1: R01 to R05, R07, R17, R26 to R46; reason 2: R06, the short title).
The `file:line` citations in this table are resolved by `coverage.py` from the function names, and the audit fails if a name is missing; every other `file:line` in this file (fork register, judgment calls, jural relations, marginal readings, findings) was written by hand on 2026-11-05 against the files as deposited, and is valid only for them: an edit to a layer-1 file shifts them.
A row is `fork` when the text can be read two ways with different outcomes and I chose one; the rule that encodes the chosen reading is named in the last column and the entry is in the fork register.

| row | provision | raw lines | kind | disposition | where / why |
| --- | --- | --- | --- | --- | --- |
| R01 | Cover page: title, edition banner, publisher | 1-14 | front matter | inert (reason 1) | Not operative: title, edition banner (2020 Revised Edition, in operation 31 December 2021), publisher. |
| R02 | Arrangement of Sections (as the converter printed it, garbled) | 16-23 | contents list | inert (reason 1) | Not operative: a table of contents.  The converter has split each entry across lines (finding 1). |
| R03 | Long title: 'An Act relating to the frustration of contracts.' | 25 | long title | inert (reason 1) | Not operative: long title. |
| R04 | Date of enactment: [13 February 1959] | 27 | enactment date | inert (reason 1) | Not operative: the date of enactment.  The same date is used by s 3(1) as a date the Act's application does not depend on (R18). |
| R05 | Heading: 'Short title' | 29 | heading | inert (reason 1) | Not operative: heading. |
| R06 | s 1: This Act is the Frustrated Contracts Act 1959. | 31 | section | inert (reason 2) | Machinery: the short title. |
| R07 | Heading of s 2: 'Adjustment of rights and liabilities of parties to frustrated contracts' | 33-34 | heading | inert (reason 1) | Not operative: heading. |
| R08 | s 2(1): when section 2 has effect | 36-40 | subsection | fork | fca-s2-adjustment.l4:33 `s 2(1) section 2 has effect in relation to the contract` (fork F1 (subject to section 3)) |
| R09 | s 2(2): sums paid are recoverable; sums payable cease to be payable | 42-47 | subsection | fork | fca-s2-adjustment.l4:57 `s 2(2) a sum paid is recoverable from the party who received it`; fca-s2-adjustment.l4:79 `s 2(2) a sum payable ceases to be payable`; fca-s2-adjustment.l4:228 `s 2(2) subject to s 2(3) the amount of the sum paid that is recoverable`; fca-s2-adjustment.l4:259 `s 2(2) subject to s 2(3) the amount of the sum payable that remains payable` (fork F2 (the time bound on the sums)) |
| R10 | s 2(3): the court may allow expenses to be retained or recovered | 49-53, 60-61 | subsection | fork | fca-s2-adjustment.l4:163 `s 2(3) the court may allow the party to retain or recover the whole or part of the sums`; fca-s2-adjustment.l4:187 `s 2(3) the most the court may allow to be retained or recovered`; fca-s2-adjustment.l4:206 `s 2(3) the amount the court allows is within the limit`; fca-court.l4:47 `s 2(3) the court's permission to allow the party to retain or recover`; fca-s2-adjustment.l4:515 `s 2(3) the most the court may allow to be retained or recovered from the sums taken together`; fca-s2-adjustment.l4:542 `s 2(3) the amount the court allows from the sums taken together is within the limit` (fork F2 (the time bound) and fork F6 (the sums taken together)) |
| R11 | s 2(4) (chapeau): a sum is recoverable for a valuable benefit | 63-70 | subsection | fork | fca-s2-adjustment.l4:296 `s 2(4) a sum is recoverable from the party who obtained a valuable benefit`; fca-s2-adjustment.l4:316 `s 2(4) the most that is recoverable for the valuable benefit`; fca-s2-adjustment.l4:329 `s 2(4) the sum the court considers just is within the limit` (fork F3 (the time bound in a Where) and judgment call QE (the money-payment parenthesis)) |
| R12 | s 2(4)(a): the benefited party's expenses | 72-77 | paragraph | encoded | fca-s2-adjustment.l4:351 `s 2(4)(a) the amount of the benefited party's expenses that the court has regard to` |
| R13 | s 2(4)(b): the effect of the circumstances giving rise to the frustration | 79-80 | paragraph | encoded | fca-s2-adjustment.l4:367 `s 2(4) the court is to have regard to this matter` |
| R14 | s 2(5): overhead expenses and personal work in estimating expenses | 82-86 | subsection | encoded | fca-s2-adjustment.l4:107 `s 2(5) the court may include a reasonable sum for overhead expenses and for work performed personally`; fca-s2-adjustment.l4:127 `s 2(5) the expenses as estimated`; fca-s2-adjustment.l4:140 `s 2(5) the amount of the expenses as estimated, counting none incurred as 0`; fca-court.l4:59 `s 2(5) the court's permission to include overhead expenses and personal work` |
| R15 | s 2(6): insurance sums are not taken into account | 88-94 | subsection | fork | fca-s2-adjustment.l4:398 `s 2(6) the court shall not take the insurance sums into account`; fca-s2-adjustment.l4:413 `s 2(6) the court may take the insurance sums into account`; fca-court.l4:89 `s 2(6) the court's prohibition on taking the insurance sums into account` (fork F4 ('In considering' as a 'where') and judgment call QA (the 'unless')) |
| R16 | s 2(7): a benefit conferred on another person treated as obtained by the obligor | 96-100, 103-104 | subsection | encoded | fca-s2-adjustment.l4:442 `s 2(7) the court may treat the benefit conferred on another person as a benefit obtained by the person who assumed the obligations`; fca-court.l4:73 `s 2(7) the court's permission to treat the benefit as obtained by the person who assumed the obligations` |
| R17 | Heading of s 3: 'Provision as to application of Act' | 106 | heading | inert (reason 1) | Not operative: heading. |
| R18 | s 3(1): which contracts the Act applies to, by the time of discharge | 108-111 | subsection | encoded | fca-s3-application.l4:26 `s 3(1) this Act applies to a contract whether made before or after 13 February 1959`; fca-s3-application.l4:36 `s 3(1) this Act applies to the contract by its time of discharge` |
| R19 | s 3(2): contracts to which the Government is a party | 113-114 | subsection | encoded | fca-s3-application.l4:55 `s 3(2) this Act applies in like manner to a contract to which the Government is a party` |
| R20 | s 3(3): the contract's own provision for frustration | 116-123 | subsection | encoded | fca-s3-application.l4:176 `s 3(3) the court is to give effect to the provision of the contract`; fca-s3-application.l4:200 `s 3(3) the amount of section 2 that is given effect`; fca-court.l4:106 `s 3(3) the court's duty to give effect to the provision of the contract` (judgment call QD (no compliance function)) |
| R21 | s 3(4): severance of a part wholly performed | 125-132 | subsection | encoded | fca-s3-application.l4:228 `s 3(4) the court is to treat the part of the contract as a separate contract that has not been frustrated`; fca-s3-application.l4:255 `s 3(4) section 2 applies to this portion of the contract`; fca-court.l4:122 `s 3(4) the court's duty to treat the part of the contract as a separate contract` (judgment call QD (no compliance function)) |
| R22 | s 3(5) (chapeau): the Act shall not apply to (a), (b) or (c) | 134 | subsection | encoded | fca-s3-application.l4:147 `s 3 this Act applies to the contract` (the composite of s 3(1) and s 3(5)(a) to (c)) |
| R23 | s 3(5)(a): charterparties and carriage of goods by sea | 136-139 | paragraph | fork | fca-s3-application.l4:73 `s 3(5)(a) this Act shall not apply to the contract` (judgment call QE (twice: the exception and the parenthesis)) |
| R24 | s 3(5)(b): contracts of insurance, except as provided by s 2(6) | 140-141 | paragraph | fork | fca-s3-application.l4:91 `s 3(5)(b) this Act shall not apply to the contract`; fca-s3-application.l4:105 `s 3(5)(b) section 2(6) still applies although the contract is a contract of insurance` (judgment call QA (the exception)) |
| R25 | s 3(5)(c): s 7 Sale of Goods Act 1979 and other contracts for the sale of specific goods that have perished | 143-146, 149-153 | paragraph | fork | fca-s3-application.l4:125 `s 3(5)(c) this Act shall not apply to the contract` (fork F5 (the 'where' of the second limb); s 7 of the Sale of Goods Act 1979 is an input) |
| R26 | Legislative History: heading and statement that it is not part of the Act | 154-158 | legislative history | inert (reason 1) | Not operative: line 157-158 says 'It is not part of the Act'. |
| R27 | Legislative History entry 1: Ordinance 6 of 1959 (commencement 13 February 1959) | 160-169 | legislative history row | inert (reason 1) | Not operative: history of the text, not part of the Act. |
| R28 | Legislative History entry 2: L.N. 40/1965 (commencement 18 February 1965) | 171-175 | legislative history row | inert (reason 1) | Not operative: history of the text. |
| R29 | Legislative History entry 3: 1970 Revised Edition (operation 1 March 1971) | 177-179 | legislative history row | inert (reason 1) | Not operative: history of the text. |
| R30 | Legislative History entry 4: 1985 Revised Edition (operation 30 March 1987) | 181-183 | legislative history row | inert (reason 1) | Not operative: history of the text. |
| R31 | Legislative History entry 5: Act 7 of 1997, Statutes (Miscellaneous Amendments) Act 1997 (1 October 1997) | 185-196 | legislative history row | inert (reason 1) | Not operative: history of the text (an amendment already made into the text above). |
| R32 | Legislative History entry 6: 2014 Revised Edition (operation 31 July 2014) | 198-200 | legislative history row | inert (reason 1) | Not operative: history of the text. |
| R33 | Abbreviations: heading | 205 | heading | inert (reason 1) | Not operative: heading. |
| R34 | Abbreviation C.P. (Council Paper) | 207 | abbreviation row | inert (reason 1) | Not operative: key to the legislative history. |
| R35 | Abbreviation G.N. No. S (N.S.) | 209 | abbreviation row | inert (reason 1) | Not operative: key to the legislative history. |
| R36 | Abbreviation G.N. No. | 211 | abbreviation row | inert (reason 1) | Not operative: key to the legislative history. |
| R37 | Abbreviation G.N. No. S | 213 | abbreviation row | inert (reason 1) | Not operative: key to the legislative history. |
| R38 | Abbreviation G.N. Sp. No. S | 215 | abbreviation row | inert (reason 1) | Not operative: key to the legislative history. |
| R39 | Abbreviation L.A. (Legislative Assembly) | 217 | abbreviation row | inert (reason 1) | Not operative: key to the legislative history. |
| R40 | Abbreviation L.N. (Legal Notification) | 219-221 | abbreviation row | inert (reason 1) | Not operative: key to the legislative history. |
| R41 | Abbreviation M. Act | 223 | abbreviation row | inert (reason 1) | Not operative: key to the legislative history. |
| R42 | Abbreviation M. Ordinance | 225 | abbreviation row | inert (reason 1) | Not operative: key to the legislative history. |
| R43 | Abbreviation Parl. | 227 | abbreviation row | inert (reason 1) | Not operative: key to the legislative history. |
| R44 | Abbreviation S.S.G.G. (E) No. | 229-230 | abbreviation row | inert (reason 1) | Not operative: key to the legislative history. |
| R45 | Abbreviation S.S.G.G. No. | 232 | abbreviation row | inert (reason 1) | Not operative: key to the legislative history. |
| R46 | Page furniture: page numbers, running heads, the date stamp 31.12.2021 | 55, 57-58, 101, 147-148, 202-203 | page furniture | inert (reason 1) | Not operative: printed page numbers and running heads (lines 55, 57, 58, 101, 147, 148, 202, 203; line 233 is a form feed and blank). |
| T01 | Defined term: 'the time of discharge' (s 2(2)) | 43-45 | defined term | encoded | fca-definitions.l4:26 `s 2(2) definition of the time of discharge`; fca-definitions.l4:76 `s 2(2) the time of discharge`; fca-definitions.l4:90 `s 2(2) there is a time of discharge` |
| T02 | Label: 'the benefited party' (s 2(4)(a)) | 72-73 | defined term | encoded | fca-definitions.l4:39 `s 2(4)(a) label for the benefited party` |

## Fork register

### The four rulings (copied word for word from the brief)

- **E1** (bench `commons-negation-1030`; should a legal effect be one definition gathered from every section that gives it?): option B, as guidance for gathering a legal effect's routes by hand only, with no pilot run; option A (gathering by bare name) is withdrawn as a direction for the language, not deferred; option C (per-section answers) applies everywhere else; the Magna Carta pilot in the printed recommendation (chapters 2, 3, 4, 5, 37, 43, 46 and 53, with a blind second reader) is not to be run. Meng's lean, verbatim: "B but generally uncomfortable with this much magic because it takes the language from unopinionated to opinionated in ways that are hard to teach an l4 novice." Meng's note, verbatim: "Fundamentally I feel like we are trying to make the language do work that the human l4 drafter should do. Too much magic. Can’t we just decline to be this opinionated and say the programmer needs to do this thinking?" Marked 2026-11-03T23:19:02.812Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
- **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. Meng's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." Meng's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
- **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.
- **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

How each applies in this Act:

- **E1.** Each section's answer stands on its own (option C).
  The one place I gathered routes to a legal effect by hand, in plain L4, is `s 3 this Act applies to the contract` (`fca-s3-application.l4:147`), which gathers s 3(1) and the three exclusions of s 3(5) into the one answer a reader asks for; `s 2(1) section 2 has effect in relation to the contract` (`fca-s2-adjustment.l4:33`) then gathers that with the two "where"s of s 2(1).
  No construct that gathers "by name" was looked for.
- **N2.** The flat negatives of this Act count as the text's no: "but not to contracts" (s 3(1), `fca-s3-application.l4:44-45`), "This Act shall not apply" (s 3(5), the composite's arms at `:151-156`), "shall not take into account" (s 2(6), `fca-s2-adjustment.l4:423`), "not being an amount in excess" (s 2(3), `:210`), "not exceeding the value" (s 2(4), `:333`), "only applicable to the remainder" (s 3(4), `fca-s3-application.l4:259`).
  The one bearer-naming prohibition, s 2(6), has its `SHANT` derived from that answer (`fca-court.l4:89`).
  The Hohfeld kinds are in "Jural relations" and not in any person-facing answer.
- **Periods.** The Act fixes no period of days, weeks, months or years; its dates (13 February 1959, 1 January 1959) are fixed calendar dates, and 13 February 1959 changes no answer (finding 3).
  Rule (a) reaches "on or after 1 January 1959 ... but not ... before" in s 3(1), which is also a flat negative, and the time bound "before the time of discharge" in s 2(2), s 2(3) and s 2(4) (fork F2): outside it the answer is `JUST FALSE`.
- **"Where".**
  Rule (b), a "where" that is not met answers `JUST FALSE`: s 2(1) (both "where"s), s 2(4) (the benefit obtained, obtained before the discharge, and not a payment of money to which s 2(2) applies: judgment call QE), s 2(7) (an obligation assumed, in consideration of a benefit), s 3(3) (a provision of the kind), s 3(4) (a severable part wholly performed), s 3(5)(c) second limb.
  Rule (c) of the delegated ruling, "when" counts as "where": s 2(6) "In considering" (fork F4).
  Rule (c) of the periods ruling, a scope limit with no "only" answers `NOTHING`: "in pursuance of the contract" in s 2(2) and s 2(3), s 3(2) for a contract the Government is not a party to, the three paragraphs of s 3(5) for a contract they do not describe, the "other sums" outside s 2(6).
- **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.
  None of (a), (b) or (d) arises: the Act hands no definition to a list or Schedule, gives no defence and has no "until" bar.
  (c) is the s 2(6) line above.

### Forks

Each fork is a site where the text can be read two ways with different outcomes.
Every other site in this Act is answered by the rulings above and is not a fork.

| id | provision | function | file:line | reading taken | other reading | text that licenses each |
| --- | --- | --- | --- | --- | --- | --- |
| F1 | s 2(1) "this section shall, subject to section 3, have effect" | `s 2(1) section 2 has effect in relation to the contract` | `fca-s2-adjustment.l4:33` (the carrying arm is `:40`) | s 3's answer is carried: where s 3 says "This Act shall not apply" (a flat negative) section 2 has no effect, `JUST FALSE`; where s 3 cannot be applied, `NOTHING` | "subject to" is a limit by the section's own wording, so section 2 would answer `NOTHING` when s 3 bites | "subject to section 3" (line 39) against "This Act shall not apply" (line 134) |
| F2 | s 2(2), s 2(3) and, in the same words, s 2(4): "before the time when the parties were so discharged" | `s 2(2) a sum paid is recoverable from the party who received it`, `s 2(2) a sum payable ceases to be payable`, `s 2(3) the court may allow the party to retain or recover the whole or part of the sums` | `fca-s2-adjustment.l4:57`, `:79`, `:163` (the arms are `:67-68`, `:89-90`, `:171-172`; the note is `:44-46`) | a time the text fixes in its own words (periods ruling (a)): a sum paid, or falling payable, at or after the discharge answers `JUST FALSE`, which agrees with s 2(4) (F3) and with the "if" of s 2(3) ("incurred expenses before the time of discharge"); "in pursuance of the contract" stays a scope limit (ruling (c)) and answers `NOTHING`; the number-valued functions cannot say `JUST FALSE` and answer `NOTHING` for such a sum, and their yes/no twins say `JUST FALSE` | a scope limit with no "only" (ruling (c)): a sum outside the time answers `NOTHING`, because the sentence says that sums paid before are recoverable and does not say what follows for sums paid after | lines 42-44 "all sums paid or payable to any party in pursuance of the contract before the time when the parties were so discharged"; the facts are stated and not derived from two dates, because a sum paid on the very day of the discharge cannot be placed "before the time" by dates alone, so the person (or the court) states which came first |
| F3 | s 2(4) "obtained a valuable benefit ... before the time of discharge" | `s 2(4) a sum is recoverable from the party who obtained a valuable benefit` | `fca-s2-adjustment.l4:296` (the arm is `:306-307`) | `JUST FALSE` when not met, on two grounds: it is a time the text fixes in its own words (ruling (a), as in F2) and a limb of a "Where" sentence (ruling (b)) | `NOTHING` (a scope limit, as F2's other reading) | line 63 "Where any party to the contract has ... obtained a valuable benefit ... before the time of discharge"; F2 and F3 now agree |
| F4 | s 2(6) "In considering whether any sum ought to be recovered or retained under this section" | `s 2(6) the court shall not take the insurance sums into account` | `fca-s2-adjustment.l4:398` (the arm is `:400-401`) | "In considering" is read as "when considering", which counts as "where": when the court is not so considering, `JUST FALSE` | a scope limit, `NOTHING` | lines 88-89; the delegated ruling (c) names "when", "upon" and "whenever", and does not name "in considering" |
| F5 | s 3(5)(c) second limb, "any other contract for the sale ... of specific goods, where the contract is frustrated by reason of the fact that the goods have perished" | `s 3(5)(c) this Act shall not apply to the contract` | `fca-s3-application.l4:125` (the arm is `:131-132`) | the "where" is the text's own word, so a sale of specific goods not frustrated by their perishing answers `JUST FALSE` | a scope limit, `NOTHING` (the paragraph reaches only the contracts it describes) | lines 150-153 "where the contract is frustrated by reason of the fact that the goods have perished" |
| F6 | s 2(3) "the whole or any part of the sums so paid or payable ... not being an amount in excess of the expenses so incurred" | `s 2(3) the most the court may allow to be retained or recovered from the sums taken together` and `s 2(3) the amount the court allows from the sums taken together is within the limit` | `fca-s2-adjustment.l4:515`, `:542` (helpers `:480`, `:494`) | one ceiling over all the sums s 2(2) reaches, the sums paid and the sums payable together: the sums are added up, so the order of the list changes nothing; the function returns only the aggregate amount the court may allow, and does not apportion it between a part "retained" and a part "recovered" or say which sums come first | a ceiling for each sum (the single-sum functions, kept as they were, would allow each sum its own ceiling: 2,000 paid and 3,000 payable against expenses of 4,000 would allow 5,000 in all where the Act allows 4,000); an order, or an apportionment, among the sums | lines 49-61: the cap is stated once, for "the sums so paid or payable", and nothing in the Act orders the sums or divides the allowance |

### Judgment calls

The six questions with no convention, decided site by site on the text (the corpus owner's instruction of 2026-11-05).
One line per site, in the brief's form: question id, provision, function name, file and line, the answer taken, the other reading.

- QA | s 2(6) | `s 2(6) the court may take the insurance sums into account` | `fca-s2-adjustment.l4:413` | `NOTHING` when the "unless" is met (a lifted bar grants nothing); `JUST FALSE` stays for the bar side, `fca-s2-adjustment.l4:398` ("the court shall not ... unless" met: the bar does not apply) | `JUST TRUE` (the exception permits it)
- QA | s 3(5)(b) | `s 3(5)(b) section 2(6) still applies although the contract is a contract of insurance` | `fca-s3-application.l4:105` | `JUST TRUE` for a contract of insurance, because here the "except" names the provision it preserves ("except as is provided by section 2(6)"), whereas the "unless" of s 2(6) names no grant; the bar side `s 3(5)(b) this Act shall not apply to the contract` (`:91`) is `JUST TRUE` for a contract of insurance and `NOTHING` for any other | `NOTHING` (a lifted bar grants nothing), the default; the two QA lines differ for the reason given and not because the sites were thought alike
- QB | none | none | none | not arising: no function in this encoding asks whether a requirement stated with a bare "must" was met; the "shall" of s 3(3) and s 3(4) is the court's duty and lives in the deontic rules (`fca-court.l4:106`, `:122`) | not applicable
- QC | none | none | none | not arising: the Act has no Schedule and nothing is "listed in" any list | not applicable
- QD | s 3(3) | `s 3(3) the court is to give effect to the provision of the contract` | `fca-s3-application.l4:176` | the "duty arises" companion answers `JUST FALSE` when the "where" is unmet (the Act does not apply, or the contract has no such provision); no compliance function was written, the deontic rule `fca-court.l4:106` carries the duty (`FULFILLED` when it does not arise); the seat exports the companion (`fca-seat.l4`, "Must the court give effect to my contract's own provision") and not a compliance question | a compliance function answering `NOTHING` when the duty does not arise, with this function as the companion
- QD | s 3(4) | `s 3(4) the court is to treat the part of the contract as a separate contract that has not been frustrated` | `fca-s3-application.l4:228` | as the line above; the deontic rule is `fca-court.l4:122` | as the line above
- QE | s 3(5)(a), the exception "except a time charterparty or a charterparty by way of demise" | `s 3(5)(a) this Act shall not apply to the contract` | `fca-s3-application.l4:73` (the arm is `:79-80`) | `NOTHING` for a time charterparty or a charterparty by way of demise: the phrase limits what a prohibition covers | `JUST FALSE` (as "except"), or `NOTHING` always
- QE | s 3(5)(a), the parenthesis "(other than a charterparty)" in the second limb | `s 3(5)(a) this Act shall not apply to the contract` | `fca-s3-application.l4:73` (the arm is `:80-81`: a charterparty is decided by the first limb and never reaches the second) | `NOTHING` for a time or demise charterparty even if it is also a contract for the carriage of goods by sea: the second limb does not reach a charterparty | `JUST FALSE` for a charterparty at the second limb
- QE | s 2(4), the parenthesis "(other than a payment of money to which subsection (2) applies)" | `s 2(4) a sum is recoverable from the party who obtained a valuable benefit` | `fca-s2-adjustment.l4:296` (the arm is `:302-303`) | `JUST FALSE` for such a payment: the bracket is part of what the "Where" describes ("a valuable benefit (other than ...)"), so a payment to which s 2(2) applies is a "where" not met (ruling (b)), and it agrees with the other arms of the same function | `NOTHING`: the bracket takes the payment out of what the grant covers (the default for a grant)
- QF | none | none | none | not applicable: this encoding writes no events to the state ledger | not applicable

## Jural relations

Hohfeld kinds, one row per provision.
The correlatives are the brief's: right/duty, privilege/no-right, power/liability, immunity/disability.
A provision that creates no relation is `none`.
The Act addresses the court far more than the parties, so most rows are a party against the court.

| provision | holder (right, privilege, power, immunity) | bearer (duty, no-right, liability, disability) | kind | L4 rule |
| --- | --- | --- | --- | --- |
| s 1 | none | none | none (short title) | none |
| s 2(1) | none | none | none (the condition on which section 2 has effect) | `fca-s2-adjustment.l4:33` |
| s 2(2), sums paid | the party who paid | the party who received | claim / duty (the sum is "recoverable ... as money received by him for the use of the party by whom the sums were paid") | `fca-s2-adjustment.l4:57`, `:228` |
| s 2(2), sums payable | the party who was to pay | the party who was to be paid | privilege / no-right (the sum "cease[s] to be ... payable") | `fca-s2-adjustment.l4:79`, `:259` |
| s 2(3) | the court | the party who received or was to receive the sums, and the party who paid | power / liability (the court "may ... allow him to retain or ... recover") | `fca-court.l4:47`; `fca-s2-adjustment.l4:163`, `:187`, `:206`, `:515`, `:542` |
| s 2(4) | the party by whom the benefit was conferred | the party who obtained the valuable benefit | claim / duty (a sum "recoverable from him ... as the court considers just") | `fca-s2-adjustment.l4:296`, `:316`, `:329` |
| s 2(4)(a), (b) | the parties | the court | claim / duty (the court is to have regard to these matters; no time or consequence is stated, so a decision function and not a deontic rule) | `fca-s2-adjustment.l4:351`, `:367` |
| s 2(5) | the court | the party whose expenses are estimated | power / liability | `fca-court.l4:59`; `fca-s2-adjustment.l4:107`, `:127`, `:140` |
| s 2(6) | the party to whom insurance money became payable | the court | claim / duty (the court "shall not take into account") | `fca-court.l4:89`; `fca-s2-adjustment.l4:398`, `:413` |
| s 2(7) | the court | the person who assumed the obligations | power / liability (the court "may ... treat ... any benefit so conferred as a benefit obtained by the person who has assumed those obligations") | `fca-court.l4:73`; `fca-s2-adjustment.l4:442` |
| s 3(1) | none | none | none (a rule of application) | `fca-s3-application.l4:26`, `:36` |
| s 3(2) | none | none | none (a rule of application; the Government is subject to the Act on the footing of a private party) | `fca-s3-application.l4:55` |
| s 3(3) | the parties to the contract | the court | claim / duty (the court "shall give effect to that provision" and to section 2 only so far as consistent) | `fca-court.l4:106`; `fca-s3-application.l4:176`, `:200` |
| s 3(4) | the parties to the contract | the court | claim / duty (the court "shall treat that part ... as if it were a separate contract") | `fca-court.l4:122`; `fca-s3-application.l4:228`, `:255` |
| s 3(5), (a) to (c) | none | none | none (they mark where the Act does not reach; their effect is the absence of the s 2 relations) | `fca-s3-application.l4:73`, `:91`, `:105`, `:125`, `:147` |
| s 2(2), "the time of discharge"; s 2(4)(a), "the benefited party" | none | none | none (definition and label) | `fca-definitions.l4:26`, `:39` |
| the cover page, arrangement of sections, long title, date of enactment, headings, legislative history, abbreviations, page furniture | none | none | none (not operative) | none |

## Findings: what the text turns out to say

1. The deposited text is a converter's plain-text rendering and shows it.
   The Arrangement of Sections is garbled (lines 16-23): "1." stands alone, "2." carries the title of section 1 ("Short title"), and the title of section 2 is split across the line after it and the line of "3." ("Adjustment of rights and liabilities of parties to frustrated" / "contracts").
   Page numbers and running heads sit inside provisions (lines 55, 57, 58, 101, 147, 148, 202, 203).
   `FCA1959.meta.json` gives a `text_sha256` of `bc6629bf58bd484e03339117394cac1561e914fbb6a2b1acd7cdcdab7d980606`; the sha256 of `FCA1959.txt` is `2e1b536e8c7d40f6eaf3328a776dce181fdb995e0e6415b2bb29d39ae3d0ee61`, which is the value `SOURCES.md` records.
   I could not tell what `text_sha256` hashes: it is not the file, and it is not the file without its last byte.
   The text was read as given; nothing was corrected.
2. The Act defines one term of its own, "the time of discharge" (s 2(2)), and attaches one label, "the benefited party" (s 2(4)(a)).
   Four other words it uses ("court", "Government", "party", "person") are defined by the Interpretation Act 1965 s 2(1); the copied module has an entry for each, and `fca-definitions.l4:109` looks them up.
   Asserted.
3. s 3(1) says two things.
   The date a contract was made changes nothing ("whether made before or after 13 February 1959"): `JUST TRUE` on both sides of the date.
   The date of discharge decides: on or after 1 January 1959 the Act applies and before it does not, so 31 December 1958 is `JUST FALSE` and 1 January 1959 is `JUST TRUE`.
   13 February 1959 is also the date of enactment (line 27) and the first commencement (line 169), so the first limb only says that a contract made before the Act existed is not excluded on that ground.
   Asserted.
4. The Act gives no answer to "does the Act apply" when the parties were not discharged.
   `s 2(1)` answers `JUST FALSE` (its "where" about discharge is unmet); `s 3` answers `NOTHING` (s 3(1) compares the time of discharge with a date and there is none to compare).
   The two modules differ on the same facts because s 2(1) has the "where" and s 3(1) does not.
   Asserted (both).
5. The ceiling in s 2(3) is the smaller of the sums and the expenses: "any part of the sums ... not being an amount in excess of the expenses so incurred".
   Expenses of 300 against a sum of 1000 give a ceiling of 300; expenses of 2000 against a sum of 1000 give 1000.
   Asserted.
6. s 2(5) lets the court add a reasonable sum for overheads and for work done personally when "estimating ... the amount of any expenses incurred", and the estimate is what the s 2(3) ceiling and the s 2(4)(a) matter use.
   Expenses of 300 plus 50 and 25 give 375 and a ceiling of 375.
   I took that reading without finding the text to say it in terms (see "Marginal readings").
   Asserted.
7. s 2(3) cuts both ways: for sums paid the court may allow the recipient to "retain" part, for sums payable it may allow the payee to "recover" part.
   With a sum of 1000 and an allowance of 200, 800 of the money paid is recoverable and 200 of the sum payable remains payable; if the court does not consider it just to allow anything, the whole 1000 is recoverable and 0 remains payable.
   An allowance above the expenses is not one the Act provides for: the net-sum functions answer `NOTHING` for it and the limit function answers `JUST FALSE`.
   Asserted.
8. The Act gives no formula for the amount: the court's allowance (s 2(3)) and the sum it "considers just" (s 2(4)) are inputs, and the Act fixes only the ceilings.
   Asserted at the ceilings (a sum of 5000 is within the limit of 5000; 5001 is not).
9. s 2(4) and s 2(3) meet in paragraph (a): the benefited party's expenses count "including any sums paid or payable by him to any other party ... and retained or recoverable by that party under subsection (3)".
   Expenses of 300 plus 100 retained or recoverable give 400.
   Asserted.
10. s 2(4) opens with a "Where" and takes "a payment of money to which subsection (2) applies" out; for such a payment the answer is `JUST FALSE`: the bracket is part of what the "Where" describes, and the payment is dealt with by s 2(2) and s 2(3) (judgment call QE).
    The matters "in particular" (paragraphs (a) and (b)) do not close the list: "all the circumstances of the case" is the instruction, so any circumstance is a matter to have regard to, and something that is not a circumstance of the case is `NOTHING`.
    Asserted.
11. s 2(6): the bar on taking insurance money into account is lifted by "an obligation to insure imposed by an express term of the frustrated contract or by or under any enactment".
    When the "unless" is met the bar is `JUST FALSE`; the text then says nothing about whether the court may, or must, count the money, so the permission question is `NOTHING`.
    Asserted.
12. s 3(5)(b) excludes contracts of insurance "except as is provided by section 2(6)".
    I could not see what that exception adds.
    s 2(6) bites only when the court is considering a recovery or retention "under this section" by a party, and section 2 does not apply to a contract of insurance, so for a frustrated contract of insurance the court is never so considering; for any other frustrated contract section 2 applies without the exception.
    The encoding says the text preserves s 2(6) (`JUST TRUE`) and claims nothing more: `s 2(2)` is `JUST FALSE` for a contract of insurance.
    This is a point for a lawyer.
    Asserted (the two answers; the puzzle itself is not asserted).
13. A time charterparty or a charterparty by way of demise is outside the exclusion of s 3(5)(a), and the Act then applies to it if s 3(1) is met.
    A voyage charterparty is excluded; so is a contract, other than a charterparty, for the carriage of goods by sea.
    Asserted.
14. s 3(5)(c) borrows section 7 of the Sale of Goods Act 1979, which is not among the sources; whether it applies to the contract is a fact the person states.
    The second limb is a "where": a sale of specific goods not frustrated by their perishing is `JUST FALSE`; a contract that is not a sale of specific goods is `NOTHING`.
    Asserted.
15. The Act names one actor who does anything, the court, and states no time limit, deadline or consequence for any of its permissions, its prohibition or its duties.
    None was invented: the six deontic rules have no `WITHIN`, no `HENCE` beyond completion and no `LEST`.
    The traces (the next finding) show what that means.
    Not asserted: see finding 16.
16. The outcome of a deontic value cannot be compared in an `#ASSERT` on main (`Trying to check equality on types that do not support it`, code `eval/unsupported-equality`), so what is asserted is each rule's guard (the decision function that switches the rule on, 13 assertions in `fca-tests-court.l4`) and the rule itself is run with `#TRACE`.
    The 15 traces were run on 1.6.109 and 1.6.108 and print the same text on both; their outcomes, each as the text predicts, are:
    s 2(3) permission: the court allows (`FULFILLED`); the court does something else (the permission stays open: `PARTY the court MAY allow ... HENCE FULFILLED`, an unused MAY is not a breach); no expenses (`FULFILLED`, the permission is not switched on).
    s 2(5) permission: the court includes the sum (`FULFILLED`); no expenses (`FULFILLED`).
    s 2(7) permission: the court treats the benefit (`FULFILLED`); the court does not consider it just (`FULFILLED`).
    s 2(6) prohibition: the court takes the insurance sums into account (`DEONTIC BREACHED`, the one breach in the file; the printed text speaks of a deadline "at 1" although the Act states none, which is how the engine words a `MUST NOT` done); the court does something else (the prohibition stands: `PARTY the court MUST NOT take the insurance sums into account HENCE FULFILLED`); an express term to insure (`FULFILLED`, nothing is prohibited).
    s 3(3) duty: the court gives effect (`FULFILLED`); the court does something else (the duty stays open: `PARTY the court MUST give effect ... HENCE FULFILLED`, and since the Act states no deadline it never reaches breach); no such provision (`FULFILLED`).
    s 3(4) duty: the court treats the part as separate (`FULFILLED`); the part was not performed (`FULFILLED`).
    Not asserted; read.
17. s 3(4) has two halves: the court treats the severed part as a separate contract not frustrated, and "shall treat section 2 as only applicable to the remainder".
    Where the severance rule applies, section 2 applies to the remainder (`JUST TRUE`) and not to the severed part (`JUST FALSE`); where it does not apply, s 3(4) says nothing about either portion (`NOTHING`).
    Asserted.
18. s 3(3) gives the court's duty ("shall give effect to that provision") and limits section 2 ("only ... to such extent, if any, as appears to the court to be consistent").
    The extent is the court's view, an input; it is capped by what section 2 would otherwise give, so a court that finds 150 consistent where section 2 gives 100 yields 100; "to such extent, if any" allows 0.
    Asserted.

19. The cap of s 2(3) is one cap for the sums together.
    "The whole or any part of the sums so paid or payable ... not being an amount in excess of the expenses so incurred" is stated once, for the sums paid and the sums payable taken together.
    The single-sum functions would allow each sum its own ceiling, so 2,000 paid and 3,000 payable against expenses of 4,000 would give ceilings of 2,000 and 3,000 (5,000 in all) where the Act allows 4,000.
    `s 2(3) the most the court may allow to be retained or recovered from the sums taken together` adds up the sums that s 2(2) reaches and returns the smaller of that total and the expenses as estimated under s 2(5): 4,000 for 2,000 + 3,000 against 4,000; 1,500 for 1,000 + 500 against 4,000; 1,000 for 5,000 in all against 1,000; 5,000 for 5,000 in all against 5,000.
    A sum paid after the discharge, or not in pursuance of the contract, is not counted; with no sum that s 2(2) reaches there is no total and the answer is `NOTHING`.
    The twin says whether the amount in fact allowed is within the cap (4,000 yes, 4,001 no, and 5,000 no).
    The Act does not say in what order the sums count or how the allowance is divided between a part retained and a part recovered; see fork F6.
    The single-sum functions are unchanged and are for one sum.
    Asserted.
20. "Before the time of discharge" is a time bound in three places (s 2(2), s 2(3), s 2(4)) and each now answers `JUST FALSE` when it is not met; "in pursuance of the contract" is the scope limit and answers `NOTHING`.
    The facts are stated: the Act speaks of "the time" and a payment on the very day of the discharge cannot be placed before or after it by dates alone, so the person or the court says which came first (fork F2).
    Asserted (a sum paid after the discharge; a sum not in pursuance of the contract).

### Reading a result: FALSE and NOTHING

(The rule of 2026-10-29, assumed and not ruled by a lawyer; the brief's wording applied to this Act.)

A **no** in this row (`JUST FALSE`) means the Act itself says no to this person's case, in its own words, or that a "where" or "if" the Act itself sets as the condition of a rule is not met on the facts.
Examples: the parties were discharged before 1 January 1959 ("but not to contracts"); a sum was paid after the discharge (the time bound of s 2(2)); the contract is one of insurance ("This Act shall not apply"); the court does not consider it just; the contract has no provision of the kind s 3(3) speaks of.
It does not mean the person has no claim in general.

**Not covered** (`NOTHING`) means the Act does not answer on these facts: the sentence is silent, or limited by its own wording and the case lies outside the limit, or it hands the answer to the court and the court has not said ("I am not sure" in the seat), or it hangs on a term the Act does not define.
Examples: a sum not paid in pursuance of the contract is outside s 2(2), and the subsection says nothing about it; a contract that is not a charterparty or a sea-carriage contract is outside the description of s 3(5)(a), and the paragraph says nothing about it; a time charterparty is taken out of the exclusion and the paragraph does not say the Act applies to it.
**Never read `NOTHING` as no.**
A caller must never turn `NOTHING` into `FALSE`.

A function whose result is a number, a date or a party cannot carry `JUST FALSE`, so it has a yes/no twin: the twin says whether the rule applies, and the number is `NOTHING` where the twin is not `JUST TRUE`.
The twin is named in the comment above or inside each such function.

## What the text does not answer

Each of these is answered `NOTHING`, or left to an input; none is answered `FALSE`.

- **Short title and commencement.** The deposited text has s 1 (the short title) and no commencement provision; the commencement dates appear only in the legislative history, which says it "is not part of the Act" (lines 157-158).
  Rows R06 and R26 to R32 are inert for that reason.
- **Who recovers from whom.** It is built into the function names (`s 2(2) a sum paid is recoverable from the party who received it`, `s 2(4) a sum is recoverable from the party who obtained a valuable benefit`) and is not returned as a value: the functions answer yes/no or a number, and do not return the payer and the payee.
- **Who holds the power.** The court is the deontic party in `fca-court.l4`; a deontic value cannot be compared in an `#ASSERT` on this binary, so the traces show the holder and the outcome and nothing asserts it (finding 16).
- **What else the court may include in the expenses (s 2(5)).** The Act says the court may, "without prejudice to the generality of this section", include a reasonable sum for overhead expenses and for work or services performed personally.
  It does not say whether anything else (lost profit, for example) may be included; the encoding covers the two heads the text names and no others.
- **Interest, limitation, costs.** Nothing in the operative text (lines 30 to 153) mentions interest on a sum recovered or retained, a period for bringing an action, or the costs of the proceedings.
- **The test for frustration.** The Act uses "impossible of performance or ... otherwise frustrated" and defines no test, so whether a contract is frustrated is a fact the person states.
- **Self-induced frustration, fault, and lost profit.** The Act does not say whether a party who brought about the frustration may rely on section 2, or whether anything for lost profit is recoverable; section 2 speaks of sums paid or payable, expenses and a valuable benefit.
- **A foreign governing law.** The Act does not say whether it applies to a contract governed by another law; s 3 speaks only of the time of discharge, the Government, the contract's own provision, a severable part and the three exclusions.
- **The court's judgments.** Whether the court "considers it just" (ss 2(3), 2(7)), how much it allows (s 2(3)), the sum it "considers just" for a benefit (s 2(4)), what is consistent with the contract's own provision (s 3(3)) and whether a part "can properly be severed" (s 3(4)) are the court's; the Act gives no formula.
  They are inputs, and `NOTHING` until the court has said.
- **A time or consequence for any court act.** The Act states no deadline, period or consequence for the court's permissions, prohibition or duties (finding 15).
- **After the "unless" of s 2(6).** Once the bar is lifted the Act does not say whether the court may, or must, count the insurance money (finding 11).
- **The order of the sums, and how the allowance is divided (s 2(3)).** The Act does not say in what order the sums paid and the sums payable count against the cap, or whether the allowance is shared between a part retained and a part recovered (fork F6).
- **A payment on the day of the discharge.** "Before the time of discharge" cannot be decided from two dates when they are the same day; the person or the court states which came first (fork F2).
- **Parties not discharged.** s 2(1) says `JUST FALSE`; s 3 says `NOTHING`, because s 3(1) compares the time of discharge with a date and there is none (finding 4).
- **Contracts the exclusions of s 3(5) do not describe, and contracts that are not the Government's.** s 3(5)(a) to (c) and s 3(2) say nothing about them (`NOTHING`).
- **Terms the Act does not define.** "Frustrated", "charterparty", "contract of insurance", "specific goods", "perished", "valuable benefit", "expenses" and "enactment" are asked as facts.
- **Section 7 of the Sale of Goods Act 1979.** It is outside the sources and is an input (see "Dependencies").

## Marginal readings for a lawyer

The two readings the brief flags "for a lawyer, not for you to decide" are taken as the status quo and every branch that rests on one is listed here with the other reading.
(a) A failed "if", "where" or "unless" counts as the text's no, clause by clause, within the provision that holds it (an inference: "if A then B" does not itself say "if not A then not B"), and flat negatives count as the text saying no.
Other reading for every branch in the first list: `NOTHING` (the Act is silent when its condition fails).
(b) A grant or prohibition limited by its own wording does not count as the text's no: outside the limit the answer is `NOTHING`.
Other reading for every branch in the second list: `JUST FALSE`.

**Branches resting on (a) (`JUST FALSE`):**

- `fca-definitions.l4:90`: `s 2(2) there is a time of discharge` is `JUST FALSE` when the parties were not discharged (a definition: "the time when the parties were so discharged").
- `fca-s2-adjustment.l4:33` (s 2(1)): both "where"s, `:36` and `:38`; and every function that carries s 2(1)'s `JUST FALSE`: `:57`, `:79`, `:107`, `:163`, `:296` (via `:299`), `:367` (via `:370`), `:442`.
- `fca-s2-adjustment.l4:163` (s 2(3)): "If the party ... incurred expenses" unmet, `:174`; "if it considers it just" answered No, `:176`.
- `fca-s2-adjustment.l4:206` and `:329`: the amount allowed above the expenses, `:211`; the sum above the value of the benefit, `:334` (flat negatives).
- `fca-s2-adjustment.l4:296` (s 2(4)): no benefit obtained by reason of what the other party did, `:305`; not obtained before the discharge, `:307` (fork F3); a payment of money to which s 2(2) applies, `:303` (judgment call QE).
- `fca-s2-adjustment.l4:57`, `:79`, `:163` (s 2(2), s 2(3)): the time bound, a sum paid or falling payable at or after the discharge, `:68`, `:90`, `:172` (fork F2).
- `fca-s2-adjustment.l4:398` (s 2(6) bar): "In considering" unmet, `:401` (fork F4); the two "unless"s met, `:405` and `:407`.
- `fca-s2-adjustment.l4:413` (s 2(6) permission): `JUST FALSE` from the flat "shall not", `:424`.
- `fca-s2-adjustment.l4:442` (s 2(7)): no person has assumed obligations, `:449`; not in consideration of a benefit conferred, `:451`; the court does not consider it just, `:453`.
- `fca-s3-application.l4:36` (s 3(1)): the discharge is before 1 January 1959, `:45` (a flat negative).
- `fca-s3-application.l4:125` (s 3(5)(c)): specific goods that did not perish, `:132` (fork F5).
- `fca-s3-application.l4:147` (the composite): each `JUST FALSE` arm, `:150`, `:152`, `:154`, `:156`.
- `fca-s3-application.l4:176` (s 3(3)): the Act does not apply, `:179`; no provision of the kind, `:186`.
- `fca-s3-application.l4:228` (s 3(4)): the Act does not apply, `:231`; the court does not find a part can properly be severed, `:235`; the part was not performed in either way, `:242`.
- `fca-s3-application.l4:255` (s 3(4)): the severed part is `JUST FALSE` (the flat "only applicable to the remainder"), `:260`.
- The seat's yes/no answers inherit all of the above; "No" to a court judgment is `JUST FALSE`, "I am not sure" is `NOTHING`.

**Branches resting on (b) (`NOTHING`):**

- `fca-s3-application.l4:55` (s 3(2)): a contract the Government is not a party to, `:60`.
- `fca-s3-application.l4:73`, `:91`, `:105`, `:125` (s 3(5)): a contract the paragraph does not describe, `:83`, `:96`, `:110`, `:134`; the excepted charterparties, `:80` (QE).
- `fca-s2-adjustment.l4:57`, `:79`, `:163` (s 2(2), s 2(3)): a sum not in pursuance of the contract, `:63`, `:85`, `:169-170`; the wrong limb (a sum paid asked as payable, and the reverse), `:65`, `:87`.
- `fca-s2-adjustment.l4:107`, `:127` (s 2(5)): no expenses incurred, `:115`, `:133`.
- `fca-s2-adjustment.l4:187`, `:228`, `:259` and `:316`, `:351` (the ceilings and the net sums): outside the rule they depend on, `:189-193`, `:230`, `:261`, `:320`, `:356`.
- `fca-s2-adjustment.l4:494`, `:515`, `:542` (the sums taken together): none of the sums given is one s 2(2) reaches, `:497`; no ceiling, `:517`, `:544`; an amount above the total of the sums, `:553`.
- `fca-s2-adjustment.l4:367` (s 2(4)): something that is not a circumstance of the case, `:379`.
- `fca-s2-adjustment.l4:398`, `:413` (s 2(6)): other sums, `:403`, `:415-418`; a lifted bar, `:420-422` (QA).
- `fca-s3-application.l4:200` (s 3(3)): the extent not stated by the court, `:205`; no provision, `:209`.
- `fca-s3-application.l4:255` (s 3(4)): the severance rule does not apply, `:263`.
- The court's judgments not yet made (`I am not sure`), wherever they are an input: `:178` (s 2(3)), `:235`-`:240` and `:266`-`:271` (net sums), `:455` (s 2(7)), `fca-s3-application.l4:205`, `:237`.

**Other readings that are not about (a) and (b), and that a lawyer may want:**

- Whether the s 2(5) sums raise the s 2(3) ceiling.
  Taken: yes, because the ceiling is "the expenses so incurred" and s 2(5) says how "the amount of any expenses incurred" is estimated "for the purposes of this section".
  Other reading: the ceiling is the expenses actually incurred and s 2(5) is only for what the court has regard to.
  Sites: `fca-s2-adjustment.l4:187`, `:127`.
- Whether the Act's application when the contract is one the Government is party to is `JUST TRUE` only for that case (s 3(2)).
  Taken: `NOTHING` for any other contract, since s 3(2) speaks only of the Government's contracts and adds nothing to the composite answer (`fca-s3-application.l4:139`).
- The order of the arms of the composite (`fca-s3-application.l4:147`) is the encoding's, not the Act's: the Act states no priority between s 3(1) and s 3(5).
  By reading the code, and not by a test of every combination: the four `JUST FALSE` arms are independent of one another and come before the `NOTHING` arm, so a `JUST FALSE` from any of them wins over a `NOTHING` from s 3(1), and any order of the four gives the same answer.
- `fca-s2-adjustment.l4:40`: section 2(1) "subject to section 3" (fork F1).
- Whether the cap of s 2(3) is one cap for all the sums or one for each sum (fork F6); taken: one cap, `fca-s2-adjustment.l4:515`.

## Dependencies

| module | Commons path | blob | sha256 of the copy | sections used | note |
| --- | --- | --- | --- | --- | --- |
| `sgia-p1-definitions.l4` | `subjects/sg/interpretation-act/encodings/legalese-sonnet-5.5/sgia-p1-definitions.l4` at Commons main `d468311a6ea4bab765b1ee7ccc8f0d7ccb29a357` | `ca5e2607c635962769a753d71154ad4ae6055f59` | `80441fd1745f75d4f142246c62213a229337a620ff5a35aeeac9732aae22af27` | Interpretation Act 1965 s 2(1): the definitions of "court", "Government", "party", "person" | copied unchanged with its 3-line header (`git hash-object` of the file with the header removed gives the blob); `IMPORT`ed by name in `fca-definitions.l4`; `srcrefs.py` is run on my own files only |

Not copied: `sgia-interpretation-time.l4` (blob `fe60ab2c1f2326a5b061e163761bd63e4f47e12a`).
The Act counts no period, sets no commencement or deemed-service rule of its own, and its two dates are fixed calendar dates compared once; there is nothing for a time module to do here.
Taken as an input and recorded as one to fill later: section 7 of the Sale of Goods Act 1979 (s 3(5)(c)); the field `section 7 of the Sale of Goods Act 1979 applies to the contract` of `Contract facts` (`fca-nouns.l4`) is what a staged encoding of that section would replace.
"Enactment" (s 2(6)) is not itself a word the copied module defines; the nearest, "written law", includes "Ordinances and enactments by whatever name called" (`sgia-p1-definitions.l4:1181`), so whether an obligation to insure was imposed "by or under any enactment" is asked as a fact.
No finding against the copied module.

## Unstable dialect

I looked at time (the Act counts no period and has only two fixed dates), versions (one current text; the legislative history lists a 1997 amendment but the deposited text does not say which provision it changed, and no rule of the Act is stated to run from different dates) and workarounds (helper functions where main does not take an inline `CONSIDER`, and traces read by eye where main cannot compare a deontic value) in `fca-s3-application.l4`, `fca-s2-adjustment.l4` and `fca-court.l4`, and found no shape the unstable dialect would express better; no second encoding was written, and I did not test whether the unstable build compares deontic values.

## What your main binary does not accept

The binary governs; where the skills describe a construct that it rejects, this is what I met (build 1.6.109, tested here).

- A deontic value cannot be compared in `#ASSERT`: `eval/unsupported-equality`, "Trying to check equality on types that do not support it", with the two values printed (`PARTY the court / MUST NOT take the insurance sums into account`).
  Consequence: each rule's guard is asserted and the rule is run with `#TRACE`; the same duties and permissions exist as decision functions over the facts, as the brief asks (finding 16).
  The outcome of a trace is not counted by `check.sh`, which sees only assertion lines (the 108 comparison was done by hand: the trace text is identical on 1.6.109 and 1.6.108).
- `length` is not defined (`check/unknown-identifier`); I used `sum (map (GIVEN t YIELD 1) xs)` in a test.
- `JUST (min x's amount 10)` is a parse error (`parse/unexpected-open-paren`): a genitive in a function argument is bracketed, `(min (x's amount) 10)`.
- An inline `CONSIDER` inside an argument (`GREATER THAN (CONSIDER ...)`) is a parse error: I used a helper function (`fca-s2-adjustment.l4:140`).
- From the brief and not re-tested by me: no `REFUSE`, `#ASSERT REFUSED` or `BECAUSE`; `NOT` must be parenthesised; each `#ASSERT` on one line; no section `GIVEN`; no `YMD` of my own.
  "Not covered" is `NOTHING` throughout and is asserted.

## What check.sh prints

Command: `L4=<L4_BIN> L4_MAIN=<l4-main-108> ./check.sh` (target `main`), run from this folder, 2026-11-05.
There is no baseline: this is the first run of a new row.

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.108 (main, 2ae7c9b, 2026-11-02)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
fca-cases-seat.l4                              0       107       0        0         0 |      0       107       0        0  same
fca-court.l4                                   0         0       0        0         0 |      0         0       0        0  same
fca-definitions.l4                             0         0       0        0         0 |      0         0       0        0  same
fca-nouns.l4                                   0         0       0        0         0 |      0         0       0        0  same
fca-s2-adjustment.l4                           0         0       0        0         0 |      0         0       0        0  same
fca-s3-application.l4                          0         0       0        0         0 |      0         0       0        0  same
fca-seat.l4                                    0         0       0        0         0 |      0         0       0        0  same
fca-tests-court.l4                             0        13       0        0         0 |      0        13       0        0  same
fca-tests-definitions.l4                       0        20       0        0         0 |      0        20       0        0  same
fca-tests-s2.l4                                0       132       0        0         0 |      0       132       0        0  same
fca-tests-s3.l4                                0        64       0        0         0 |      0        64       0        0  same
sgia-p1-definitions.l4                         0         0       0        0         0 |      0         0       0        0  same
TOTAL (12 modules)                             0       336       0        0           |      0       336       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

Trace outcomes of `fca-tests-court.l4` are not in these numbers (finding 16).
`srcrefs.py`, run as `python3 -I srcrefs.py check --refs ../../../inputs/FCA1959.txt` on my own files (not `sgia-p1-definitions.l4`), reports: `srcrefs check: 190 src: lines, 41 runs, 50 locators, 0 problems`.

## What would need doing before this encoding is worth relying on

- A lawyer reads it against the official text (it is a converter rendering), starting with the forks F1 to F5, the QA and QE lines and the "Marginal readings".
- Finding 12 (what s 3(5)(b)'s exception adds) needs a lawyer.
- A staged encoding of section 7 of the Sale of Goods Act 1979 would replace the s 3(5)(c) input.
- The seat's 32 questions have been type-checked and exercised with 107 worked cases, but not put to a real person, not deployed to Legalese Cloud, and not run through the website's Interact form.
- Every expected value was written by the one agent who wrote the rules; there was no independent test author and no blind second reader.
- The trace outcomes are read by eye; a build that can compare deontic values would let them be asserted.
- Process limit: I did not read all of the skills' `source-patterns` areas 1 to 11, nor all of `drafting-patterns`; I read the index, area 8 and entries 5.4, 2.2, 4.1, 4.2, 1.6 and 7.1, and the sections of `drafting-patterns` on decision results and deontic rules.
