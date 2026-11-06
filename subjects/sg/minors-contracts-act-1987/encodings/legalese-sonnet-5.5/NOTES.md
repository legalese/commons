# Minors' Contracts Act 1987 (Singapore): encoding notes (legalese-sonnet-5.5, target main)

**Status: draft.** No domain expert has read this encoding against the text (`not_reviewed`).
How the claims below were checked: the L4 by `check.sh` on two main builds (1.6.109 and 1.6.108), the quotations by `srcrefs.py` (`check --refs` and `check --strict`, 0 problems), the coverage table by `coverage.py` (every non-blank line of the text is in exactly one primary row), and each `file:line` reference in this file by `coverage.py --verify-notes`.
Nothing here was checked by a lawyer.

**The source is a plain-text rendering.**
`inputs/MCA1987.txt` was made by a converter script from Singapore Statutes Online (2020 Revised Edition, informal consolidation, version in force from 1 April 2022); it is not the official text, and nothing in this row is "verified against the official text".
The licence note for the text is the subject-level one, `inputs/STUB-SOURCE-LICENSE.md`, pointed at from `SOURCE-LICENSE.md`.
Quotations in the `.l4` files are `-- src:N | text` lines copied from that file by line number.

## Seat

**A minor, or a person who contracted with a minor, asking on facts they can state whether the contract binds the minor, can be ratified, or can be enforced, and what restitution is available.**

Why this seat: Commons turns every Act into a question form for the individual to whom the law is applied, and this Act is applied to exactly two people, the minor and the person who dealt with them.
The Act answers only part of what that person would ask.
It does not say whether a minor's contract binds the minor, can be ratified or can be enforced; it takes the common law for granted and changes four things: it switches off the Infants Relief Act 1874 for contracts made by minors (s 1), it keeps a guarantee of a minor's obligation enforceable against the guarantor (s 2), it lets the court order the minor to give back property (s 3), and it shuts itself out of contracts made in a window of years (s 4).
So the seat's ten questions are the questions the Act answers, and the headline questions are listed under "What the text does not answer".
No question is exported that would always answer `NOTHING`.

The seat is the two files `mca-seat.l4` and `mca-cases-seat.l4`; no layer-1 module changes to suit it.
The six questions on ss 2 and 3 pass "a party was a minor when the contract was made" as true to the layer-1 rule, because a person who asks about a guarantee of a minor's obligation or about restitution from a minor is asking about a minor's contract; the first input's `@desc` of each of the six says so ("This question assumes that a party was a minor when the contract was made; if none was, it does not apply to you"), so a person to whom it does not apply knows to stop.
There is no seat for the court: s 3(1) addresses the court, and the person meets it as "can the court make the minor transfer ...?".

## What is encoded and what is not

| file | layer | what it holds |
| --- | --- | --- |
| `mca-nouns.l4` | 1 | the nouns: the contract, the guarantee case, the restitution case, property, remedy, the Act's two defined terms |
| `mca-act.l4` | 1 | sections 1 to 4 in the Act's order; section 4 is written last, as the Act orders it, and read by sections 1 to 3 as a gate |
| `mca-reading.l4` | 1 | the Interpretation Act 1965 as it reads two words of this Act ("he", "a person"); imports the copied `sgia-p1-definitions.l4` |
| `mca-cases.l4` | 1 | 251 assertions and 4 `#TRACE`s on layer 1 |
| `mca-seat.l4` | 2 | ten exported questions, each with `@desc` on every input, in four `§§` groups in the text's order |
| `mca-cases-seat.l4` | 2 | 103 assertions on the seat's questions |
| `sgia-p1-definitions.l4` | dependency | copied unchanged from Commons; see "Dependencies" |

Encoded: sections 1, 2, 3 and 4 and the two defined terms of s 3(1)(a).
Not encoded: the title, headings, the arrangement of sections, the page furniture, the Legislative History (which the text says "is not part of the Act") and the abbreviations (reason 1: not operative); the revised edition's own commencement, the bracketed commencement date `[12 November 1993]`, and s 5, the short title ("This Act may be cited as the Minors' Contracts Act 1987") (reason 2: machinery).
Nothing is repealed or blank in this text.

## Jural relations

The Act creates few relations, and names the parties to none of them except the court and the two labels of s 3(1)(a).
`none` means the provision creates no relation between parties.

| provision | right-holder (claim, privilege, power, immunity) | correlative bearer (duty, no-right, liability, disability) | L4 rule |
| --- | --- | --- | --- |
| s 1 | none: it disapplies a statute; it gives the contracting minor no claim and the other party no duty | none | `s 1 the Infants Relief Act 1874 applies to the contract` (mca-act.l4:79) |
| s 2 | claim: the person to whom the guarantee was given (the Act does not name them; it speaks only of "the guarantor") | duty: the guarantor; the Act removes one defence, so the guarantor has no privilege to resist on that ground alone | `s 2 the guarantee is saved from unenforceability on that ground alone` (mca-act.l4:168) |
| s 3(1) | power: the court, to require a transfer | liability: the defendant (the minor), who is subject to that power; the claimant has no claim to the transfer, only the chance that the court uses it | `s 3(1) the court may require the defendant to transfer property to the claimant` (mca-act.l4:308), `s 3(1) the court's permission to require the transfer` (mca-act.l4:332) |
| s 3(2) | immunity: the claimant, whose other remedies s 3 does not touch | disability: the court and the defendant have no power under s 3 to cut down those other remedies | `s 3(2) this section prejudices another remedy available to the claimant` (mca-act.l4:347) |
| s 4 | none: a scope rule for the whole Act; it creates no relation between parties | none | `s 4 this Act is barred from applying to the contract` (mca-act.l4:452) |
| s 5 | none: short title | none | not encoded (reason 2) |

N2 (ruled 2026-11-04) says a flat negative's prohibition (`SHANT`) is derived where the text names who bears it.
None of this Act's flat negatives names a bearer: "shall not apply" has the 1874 Act as its subject, "shall not ... be unenforceable" has the guarantee, "Nothing in this Act applies" has the Act, and "shall not be taken to prejudice" has the section.
So no `SHANT` is derived and no `PARTY` is invented.

## Coverage table

One row per provision, subsection, paragraph, defined term, arrangement entry, history entry and abbreviation.
`coverage.py` holds the table, checks that the 37 primary rows partition the 99 non-blank lines of the text (every non-blank line in exactly one), checks that every L4 name a row points at exists in an `mca-*.l4` file, and writes this table.
Sub rows (S and A) refine lines a primary row (P) already covers.

<!-- COVERAGE:BEGIN -->
| row | lines | provision (the Act's words, shortened) | disposition | pointer or reason |
| --- | --- | --- | --- | --- |
| P01 | 1-4 | Title block: The Statutes of the Republic of Singapore; Minors' Contracts Act 1987; 2020 Revised Edition | inert | reason 1 (not operative: title) |
| P02 | 6-7 | Revised-edition statement: incorporates amendments to 1 December 2021, comes into operation on 31 December 2021 | inert | reason 2 (machinery: the revised edition's own commencement) |
| P03 | 9-13 | Publisher legend: Law Revision Commission; Revised Edition of the Laws Act 1983 | inert | reason 1 (not operative) |
| P04 | 15-16 | Banner: Informal Consolidation, version in force from 1/4/2022; 2020 Ed. | inert | reason 1 (not operative; it names the version encoded) |
| P05 | 18 | Running title | inert | reason 1 (not operative: title) |
| P06 | 20-26 | Arrangement of sections | inert | reason 1 (not operative: headings) |
| P07 | 28 | Long title: An Act to amend the law relating to minors' contracts | inert | reason 1 (not operative: long title) |
| P08 | 29 | [12 November 1993] | inert | reason 2 (machinery: the date the Act took effect in Singapore; s 4 states its own 12 November 1993, which is encoded in P27) |
| P09 | 31 | Heading of s 1: Disapplication of Infants Relief Act 1874 | inert | reason 1 (not operative: heading) |
| P10 | 32-36 | s 1: the Infants Relief Act 1874 shall not apply to any contract made by a minor after 9 April 1987 | fork | F2, F7; `s 1 the disapplication reaches the contract`, `s 1 the Infants Relief Act 1874 applies to the contract`, `s 1 the Infants Relief Act 1874 invalidates the contract`, `s 1 the Infants Relief Act 1874 bars an action on the contract ratified after majority` |
| P11 | 38 | Heading of s 2: Guarantees | inert | reason 1 (not operative: heading) |
| P12 | 39 | s 2 chapeau: Where -- | encoded | `s 2 the guarantee is saved from unenforceability on that ground alone` (a failed "where" is JUST FALSE: ruling of 2026-11-05 (b)) |
| P13 | 40-41 | s 2(a): a guarantee is given in respect of an obligation of a party to a contract made after 9 April 1987 | encoded | `s 2(a) a guarantee is given in respect of an obligation of a party to a contract made after 9 April 1987` (date: F2) |
| P14 | 42-44 | s 2(b): the obligation is unenforceable against him (or he repudiates the contract) because he was a minor when the contract was made | fork | F1; `s 2(b) the obligation is unenforceable against him, or he repudiates the contract, because he was a minor when the contract was made` |
| P15 | 46-47 | s 2 tail: the guarantee shall not for that reason alone be unenforceable against the guarantor | encoded | `s 2 the guarantee is unenforceable against the guarantor for that reason alone` |
| P16 | 49 | Heading of s 3: Restitution | inert | reason 1 (not operative: heading) |
| P17 | 50 | s 3(1) chapeau: 3.-(1) Where -- | encoded | `s 3(1) the conditions for the court's power are met` |
| P18 | 51-52 | s 3(1)(a): a person (the claimant) has after 9 April 1987 entered into a contract with another (the defendant) | encoded | `s 3(1)(a) the claimant has after 9 April 1987 entered into a contract with the defendant` (date: F2) |
| P19 | 54 | Page number 1 | inert | reason 1 (not operative: page furniture) |
| P20 | 56-57 | Page header: Informal Consolidation banner; 2020 Ed. Minors' Contracts Act 1987, page 2 | inert | reason 1 (not operative: page furniture) |
| P21 | 59-61 | s 3(1)(b): the contract is unenforceable against the defendant (or he repudiates it) because he was a minor when the contract was made | fork | F1; `s 3(1)(b) the contract is unenforceable against the defendant, or he repudiates it, because he was a minor when the contract was made` |
| P22 | 63-65 | s 3(1) tail: the court may, if it is just and equitable to do so, require the defendant to transfer to the claimant any property acquired by the defendant under the contract, or any property representing it | fork | F4; `s 3(1) the court may require the defendant to transfer property to the claimant`, `s 3(1) the property is within what the court may require to be transferred`, `s 3(1) the court's permission to require the transfer` |
| P23 | 67 | Amendment note: [Act 25 of 2021 wef 01/04/2022] | inert | reason 1 (not operative: an editorial note; the amendment's effect is in the in-force wording encoded; the pre-amendment wording is not among the sources) |
| P24 | 69-70 | s 3(2): Nothing in this section shall be taken to prejudice any other remedy available to the claimant | fork | F5; `s 3(2) this section prejudices another remedy available to the claimant` |
| P25 | 72 | Amendment note: [Act 25 of 2021 wef 01/04/2022] | inert | reason 1 (not operative: an editorial note) |
| P26 | 74 | Heading of s 4: Contracts before 12 November 1993 | inert | reason 1 (not operative: heading) |
| P27 | 76-79 | s 4: Nothing in this Act applies in relation to a contract made after 9 April 1987 and before 12 November 1993 except in so far as it was applicable by virtue of section 5 of the Civil Law Act 1909 in force before 12 November 1993 | fork | QA, F2, F3, F6; `s 4 this Act is barred from applying to the contract`, `s 4 the provision of this Act is open to apply to the contract`, `s 4 what this section does to a provision of this Act`, `s 4 the band a contract made on a day falls in` |
| P28 | 81 | Heading of s 5: Short title | inert | reason 1 (not operative: heading) |
| P29 | 82 | s 5: This Act may be cited as the Minors' Contracts Act 1987 | inert | reason 2 (machinery: short title) |
| P30 | 84 | Banner: Informal Consolidation, version in force from 1/4/2022 | inert | reason 1 (not operative: page furniture) |
| P31 | 85-86 | Legislative History: title lines | inert | reason 1 (not operative: the history is not part of the Act, line 89) |
| P32 | 88-89 | Statement that the Legislative History is a service, not part of the Act | inert | reason 1 (not operative) |
| P33 | 91-120 | Legislative History entries 1 to 4 | inert | reason 1 (not operative: not part of the Act, line 89; see finding 8 on 'sections 1(b) and 4(1)' and fork F11 on '9 June 1987') |
| P34 | 122-123 | Banner and page number ii | inert | reason 1 (not operative: page furniture) |
| P35 | 125 | Heading: Abbreviations | inert | reason 1 (not operative: heading) |
| P36 | 127-152 | Abbreviations table | inert | reason 1 (not operative: a glossary of the abbreviations used in the legislative history) |
| P37 | 154 | Banner: Informal Consolidation, version in force from 1/4/2022 | inert | reason 1 (not operative: page furniture) |
| S01 | 22 | Arrangement entry 1: Disapplication of Infants Relief Act 1874 | inert | reason 1 (heading) |
| S02 | 23 | Arrangement entry 2: Guarantees | inert | reason 1 (heading) |
| S03 | 24 | Arrangement entry 3: Restitution | inert | reason 1 (heading) |
| S04 | 25 | Arrangement entry 4: Contracts before 12 November 1993 | inert | reason 1 (heading) |
| S05 | 26 | Arrangement entry 5: Short title | inert | reason 1 (heading) |
| S06 | 32 | s 1 names the Infants Relief Act 1874 (a statute not among the sources) | encoded | named in `s 1 the Infants Relief Act 1874 applies to the contract`; what it says is not asked: s 1 only turns it off |
| S07 | 32-35 | s 1 parenthesis: (which invalidates certain contracts made by minors and prohibits actions to enforce contracts ratified after majority) | encoded | `s 1 the effects the Act describes the Infants Relief Act 1874 as having`, `s 1 the Infants Relief Act 1874 invalidates the contract`, `s 1 the Infants Relief Act 1874 bars an action on the contract ratified after majority`; F7 |
| S08 | 35-36 | s 1 scope: any contract made by a minor after 9 April 1987 | fork | F2; `s 1 the contract was made by a minor after 9 April 1987` |
| S09 | 42-43 | s 2(b) parenthesis: (or he repudiates the contract) | fork | F1; read inside `s 2(b) the obligation is unenforceable against him, or he repudiates the contract, because he was a minor when the contract was made` |
| S10 | 51 | Defined term: the claimant | encoded | `s 3(1)(a) the terms the Act defines`, `s 3(1)(a) the Act's definition of` |
| S11 | 51-52 | Defined term: the defendant | encoded | `s 3(1)(a) the terms the Act defines`, `s 3(1)(a) the Act's definition of` |
| S12 | 51 | s 3(1)(a) 'a person' (read through the Interpretation Act 1965 s 2(1)) | encoded | `s 3(1)(a) the Act's word a person reaches the claimant` (mca-reading.l4) |
| S13 | 42-43 | s 2(b) 'him', 'he' (read through the Interpretation Act 1965 s 2(1)) | encoded | `ss 2(b) and 3(1)(b) the masculine word he reaches the party` (mca-reading.l4) |
| S14 | 59-60 | s 3(1)(b) parenthesis: (or he repudiates it) | fork | F1; read inside `s 3(1)(b) the contract is unenforceable against the defendant, or he repudiates it, because he was a minor when the contract was made` |
| S15 | 63 | s 3(1): if it is just and equitable to do so | encoded | judgment taken as a plain input, `s 3(1) the court may require the defendant to transfer property to the claimant` |
| S16 | 64-65 | s 3(1): any property acquired by the defendant under the contract, or any property representing it | encoded | `s 3(1) the property is within what the court may require to be transferred`; F4 |
| S17 | 63-64 | s 3(1): require the defendant to transfer to the claimant | encoded | `s 3(1) the property is within what the court may require to be transferred` (the transferee), `s 3(1) the court's permission to require the transfer` |
| S18 | 69-70 | s 3(2): any other remedy available to the claimant | encoded | `s 3(2) this section prejudices another remedy available to the claimant`; F5 |
| S19 | 76-77 | s 4: a contract made after 9 April 1987 and before 12 November 1993 (the band) | encoded | `s 4 the band a contract made on a day falls in` (F2) |
| S20 | 77-79 | s 4: except in so far as it was applicable by virtue of section 5 of the Civil Law Act 1909 in force before 12 November 1993 | fork | QA, F6; `s 4 what this section does to a provision of this Act`, `s 4 this Act is barred from applying to the contract` |
| S21 | 78 | s 4 names section 5 of the Civil Law Act 1909 (an Act not among the sources) | encoded | taken as the input `section 5 of the Civil Law Act 1909 made the provision applicable` (mca-nouns.l4), listed under Dependencies |
| S22 | 91-101 | History entry 1: U.K. 1987, c. 13; commencement 9 June 1987; application 12 November 1993 (except sections 1(b) and 4(1)); note on the Application of English Law Act 1993 | inert | reason 1 (not part of the Act) |
| S23 | 103-105 | History entry 2: 1994 Revised Edition; operation 20 May 1994 | inert | reason 1 (not part of the Act) |
| S24 | 107-109 | History entry 3: 2020 Revised Edition; operation 31 December 2021 | inert | reason 1 (not part of the Act) |
| S25 | 111-120 | History entry 4: Act 25 of 2021 (Courts (Civil and Criminal Justice) Reform Act 2021) s 163; commencement 1 April 2022 | inert | reason 1 (not part of the Act) |
| A01 | 127 | Abbreviation: C.P. Council Paper | inert | reason 1 (not operative: glossary entry) |
| A02 | 129 | Abbreviation: G.N. No. S (N.S.) Government Notification Number Singapore (New Series) | inert | reason 1 (not operative: glossary entry) |
| A03 | 131 | Abbreviation: G.N. No. Government Notification Number | inert | reason 1 (not operative: glossary entry) |
| A04 | 133 | Abbreviation: G.N. No. S Government Notification Number Singapore | inert | reason 1 (not operative: glossary entry) |
| A05 | 135 | Abbreviation: G.N. Sp. No. S Government Notification Special Number Singapore | inert | reason 1 (not operative: glossary entry) |
| A06 | 137 | Abbreviation: L.A. Legislative Assembly | inert | reason 1 (not operative: glossary entry) |
| A07 | 139-141 | Abbreviation: L.N. Legal Notification (Federal/Malaysian Subsidiary Legislation) | inert | reason 1 (not operative: glossary entry) |
| A08 | 143 | Abbreviation: M. Act Malayan Act/Malaysia Act | inert | reason 1 (not operative: glossary entry) |
| A09 | 145 | Abbreviation: M. Ordinance Malayan Ordinance | inert | reason 1 (not operative: glossary entry) |
| A10 | 147 | Abbreviation: Parl. Parliament | inert | reason 1 (not operative: glossary entry) |
| A11 | 149-150 | Abbreviation: S.S.G.G. (E) No. Straits Settlements Government Gazette (Extraordinary) Number | inert | reason 1 (not operative: glossary entry) |
| A12 | 152 | Abbreviation: S.S.G.G. No. Straits Settlements Government Gazette Number | inert | reason 1 (not operative: glossary entry) |
<!-- COVERAGE:END -->

Audit counts (printed by `python3 -I coverage.py <text>`): the text is 154 lines with 99 non-blank lines and 663 words (the 663 matches `inputs/SOURCES.md`); the table has 37 primary rows and 37 sub rows, 74 rows in all; no line is uncovered and none is in two primary rows.
The first table had 75 rows; regrouping the wrapped `L.N.` abbreviation entry (lines 139-141) as one entry took it to 74, which is the table above.
No row is `inert` for a reason outside 1, 2 and 3, and no row is `out-of-scope` or `deferred`.

## Fork register

### Rulings of 2026-11-04 and 2026-11-05 (copied word for word from the brief by `coverage.py --brief`)

<!-- RULINGS:BEGIN -->
- **E1** (bench `commons-negation-1030`; should a legal effect be one definition gathered from every section that gives it?): option B, as guidance for gathering a legal effect's routes by hand only, with no pilot run; option A (gathering by bare name) is withdrawn as a direction for the language, not deferred; option C (per-section answers) applies everywhere else; the Magna Carta pilot in the printed recommendation (chapters 2, 3, 4, 5, 37, 43, 46 and 53, with a blind second reader) is not to be run. Meng's lean, verbatim: "B but generally uncomfortable with this much magic because it takes the language from unopinionated to opinionated in ways that are hard to teach an l4 novice." Meng's note, verbatim: "Fundamentally I feel like we are trying to make the language do work that the human l4 drafter should do. Too much magic. Can’t we just decline to be this opinionated and say the programmer needs to do this thinking?" Marked 2026-11-03T23:19:02.812Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
- **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. Meng's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." Meng's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
- **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.
- **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.
<!-- RULINGS:END -->

How this row applied them:

- **E1.** Nothing gathers a legal effect "by name".
  Each section gives its own answer (option C): s 1, s 2, s 3(1), s 3(2) and s 4 each have their own functions, and the seat calls them one by one.
  I did not write a hand-gathering function (option B), so there is no gathering to report.
- **N2.** Flat negatives answer `JUST FALSE`: "shall not apply" (s 1), "shall not ... be unenforceable" (s 2), "Nothing in this section shall be taken to prejudice" (s 3(2)) and "Nothing in this Act applies" (s 4).
  No `SHANT` is derived (see "Jural relations").
- **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.
  (a) The Act counts no period of days, months or years, but it fixes two dates in its own words, 9 April 1987 and 12 November 1993; outside them the answer is `JUST FALSE` at every site that reads them: the s 1 disapplication, s 2(a), s 3(1)(a) and the s 4 bar (F2).
  (b) A failed "Where" answers `JUST FALSE`: s 2's chapeau and limbs (a) and (b), s 3(1)'s chapeau and limbs (a) and (b); and "because he was a minor" when the record says no party was a minor.
  (c) A scope limit with no "only" answers `NOTHING`: s 1's "made by a minor" (once its date is met), s 3(2)'s "the claimant" and "any other remedy", and s 3(1)'s "to the claimant any property acquired ... or any property representing it".
- **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.
  None arises: the Act has no schedule, no defence and no "until" bar.
  s 3(1)(a) defines two words by a label, not by handing a list over, so an undefined word answers `NOTHING` (finding 9).

### Forks taken

| id | provision | the reading taken | the other reading |
| --- | --- | --- | --- |
| F1 | s 2(b), s 3(1)(b) | "because he was a minor ..." governs both limbs, "the obligation is unenforceable against him" and "(or he repudiates the contract)"; the tail of s 2, "for that reason alone", points back to minority; a party who repudiates for another reason does not satisfy (b); the record's own minority fact is read first, so when no party was a minor the limb is `JUST FALSE` whatever else is known, and when a party was a minor and the reason is not known the limb stays `NOTHING` (`s 2(b) the obligation is unenforceable against him, or he repudiates the contract, because he was a minor when the contract was made` (mca-act.l4:141)) | (unenforceable AND because) OR repudiates, so any repudiation satisfies (b); and, for the minority fact, `NOTHING` when the record says no party was a minor but the reason is unknown (the first draft) |
| F2 | s 1 "made by a minor after 9 April 1987"; s 2(a) "a contract made after 9 April 1987"; s 3(1)(a) "has after 9 April 1987 entered into a contract"; s 4 "a contract made after 9 April 1987 and before 12 November 1993" | the dates are fixed in the text's own words, and all four sites are read the same way: outside the date the answer is `JUST FALSE` (rulings of 2026-11-05: (a) a date or period fixed in the text's own words, (b) a "Where" that fails, (d) a bar that does not bite outside the date it names). Site by site: **s 1**, the date is a condition of the class of contracts the disapplication reaches, so a contract made on or before 9 April 1987 gets `JUST FALSE` from `s 1 the disapplication reaches the contract` (mca-act.l4:60, branch at mca-act.l4:65-67), tested before the minor limb; **s 2(a)** and **s 3(1)(a)**, the date sits inside a "Where", so `JUST FALSE` (`s 2(a) a guarantee is given in respect of an obligation of a party to a contract made after 9 April 1987` (mca-act.l4:123), `s 3(1)(a) the claimant has after 9 April 1987 entered into a contract with the defendant` (mca-act.l4:236)); **s 4**, a bar over a window, so outside it (on or before 9 April 1987, or on or after 12 November 1993) the bar question `s 4 this Act is barred from applying to the contract` (mca-act.l4:452, branch at mca-act.l4:459) answers `JUST FALSE` and the gate answers `JUST TRUE` (the provision is simply open). The exported question "does the 1874 Act apply" does not change: it stays `NOTHING` outside the date, because s 1 says nothing of the 1874 Act's application there. s 1's minor limb stays a scope limit (`NOTHING`, ruling (c)). Both sides of each date are asserted at all four sites (the day before, the day itself and the day after 9 April 1987, and the same around 12 November 1993) | the first draft read s 1's date and s 4's window as scope limits (ruling (c)), so `NOTHING` outside them while ss 2(a) and 3(1)(a) answered `JUST FALSE`; the other uniform reading is all four as scope limits, `NOTHING` at ss 2(a) and 3(1)(a) too |
| F3 | s 4 "Nothing in this Act" | s 4 gates sections 1, 2, 3(1) and 3(2) alike, including s 1, because "this Act" includes s 1 (`s 4 the provision of this Act is open to apply to the contract` (mca-act.l4:436)) | s 1 turns off an earlier Act and is not "applied in relation to" a contract in s 4's sense, so s 4 would gate ss 2 and 3 only |
| F4 | s 3(1) "any property representing it" | "it" is the property acquired by the defendant under the contract; property representing it is property that stands in its place (`s 3(1) the property is within what the court may require to be transferred` (mca-act.l4:287)) | "it" is the contract, so property representing the contract |
| F5 | s 3(2) "any other remedy available to the claimant" | "the claimant" is the label s 3(1)(a) gives, so s 3(2) needs limb (a) only and does not read limb (b), whether the contract is unenforceable because of minority; when limb (a) fails (the claimant did not contract with the defendant, or the contract was made on or before 9 April 1987) it answers `NOTHING` without reading limb (b), because the label "the claimant" then names nobody (`s 3(2) this section prejudices another remedy available to the claimant` (mca-act.l4:347)); this differs on purpose from ss 2(a) and 3(1)(a), which sit inside a "Where" and answer `JUST FALSE`, because s 3(2) is not introduced by "Where" and speaks of a label; asserted with (a) failing and (b) met, and with (a) met and (b) failing | s 3(2) speaks only where s 3(1) as a whole applies, so limb (b) is needed too |
| F6 | s 4 "except in so far as it was applicable by virtue of section 5 of the Civil Law Act 1909" | "in so far as" is read provision by provision: whether that section made THIS provision applicable is a fact asked per question (`s 4 what this section does to a provision of this Act` (mca-act.l4:418)); the seat asks it once per question | one yes/no for the whole Act: either that section made the Act applicable to the contract or it did not |
| F7 | s 1 parenthesis "(which invalidates certain contracts made by minors and prohibits actions to enforce contracts ratified after majority)" | the parenthesis describes the 1874 Act and creates no rule of this Act; the two effects are listed (`s 1 the effects the Act describes the Infants Relief Act 1874 as having` (mca-act.l4:44)); "does the 1874 Act invalidate this contract" answers `JUST FALSE` when s 1 reaches the contract and `NOTHING` otherwise, and never `JUST TRUE`, because the text never says the 1874 Act applies and does not say which contracts are "certain contracts" (`s 1 the Infants Relief Act 1874 invalidates the contract` (mca-act.l4:91), `s 1 the Infants Relief Act 1874 bars an action on the contract ratified after majority` (mca-act.l4:103)) | the parenthesis states law that this Act asserts, so a question about the 1874 Act's effect on a contract it does reach would answer yes |
| F8 | ss 2 and 3(1): which of two blockers comes first | a "Where" that fails on its own is tested before an exception that is not known: contract in the s 4 window, section 5's effect not known, no guarantee given, answers `JUST FALSE` rather than `NOTHING`, at mca-act.l4:173 and mca-act.l4:264 (asserted in mca-cases-seat.l4, the F8 case) | the unknown exception first, so `NOTHING` |
| F9 | s 3(1): which of two blockers comes first | the person's "not just and equitable" is tested before the property scope: wrong property and not equitable answers `JUST FALSE`, at mca-act.l4:314-317 (asserted in mca-cases-seat.l4, the F9 case) | the property scope first, so `NOTHING` |
| F10 | s 3(1) "to the claimant" in the seat | the seat fixes the transferee as the claimant, because the person asking never asks about a transfer to anyone else; the layer-1 function still answers `NOTHING` for another transferee (mca-seat.l4:166-172 and 185-191, mca-act.l4:289-291) | ask the transferee as an input |
| F11 | the date "9 April 1987" | the operative text says "9 April 1987" four times (lines 36, 41, 51 and 77 of `inputs/MCA1987.txt`: s 1, s 2(a), s 3(1)(a) and s 4); the Legislative History (line 93, which the text says "is not part of the Act") gives the commencement of the U.K. Act as "9 June 1987"; the encoding uses 9 April 1987 from the operative text everywhere (`9 April 1987` (mca-act.l4:374)) | 9 June 1987 as the date compared (a one-line change of that constant); which date is right is not something the text settles |

### Judgment calls

One line per site, as the brief asks: question id, provision, function, file:line, the answer taken, the other reading.

| id | provision | function and file:line | taken | other reading |
| --- | --- | --- | --- | --- |
| QA | s 4 "except in so far as it was applicable by virtue of section 5 of the Civil Law Act 1909" | `s 4 the provision of this Act is open to apply to the contract` (mca-act.l4:436), branch at mca-act.l4:440; and, for the bar as its own question, `s 4 this Act is barred from applying to the contract` (mca-act.l4:452), branch at mca-act.l4:455 | the exception is met: the gate answers `JUST TRUE` (the exception names the provisions that go on applying, so the provision's own words operate) and the bar question answers `JUST FALSE` (the bar does not operate); the two are opposite questions and agree. They also agree outside the window the text names: the gate answers `JUST TRUE` (the provision is simply open to apply) and the bar question `JUST FALSE` (the bar does not reach the contract; F2) | the default: the permission question answers `NOTHING` (a lifted bar grants nothing), with the bar question as its twin. Its consequence would be that every seat question answers `NOTHING` for every contract made from 10 April 1987 to 11 November 1993, whatever the person says, so the seat would never give a positive answer in that window |
| QB | none | does not arise: the Act has no bare "must" (a search of the text for "must" finds none) | n/a | n/a |
| QC | none | does not arise: the Act has no schedule or list to be "listed in" | n/a | n/a |
| QD | none | does not arise: s 3(1) is a power (MAY), not a duty, and s 2 and s 3(2) are savings, so there is no compliance function; the court's permission is `s 3(1) the court's permission to require the transfer` (mca-act.l4:332) | n/a | n/a |
| QE | s 3(2) "any other remedy" | `s 3(2) this section prejudices another remedy available to the claimant` (mca-act.l4:347), branch at mca-act.l4:355 | `NOTHING` for the s 3(1) transfer itself and for a remedy that is not available (the phrase limits a flat negative's reach: "limited by its own wording") | `JUST FALSE`, reading "other than" as "except" |
| QF | none | not applicable: this encoding writes no events to the state ledger | n/a | n/a |

No site is answered two ways in this range: the four date sites agree (F2), and QA's gate and bar question agree (opposite questions).

## Marginal readings for a lawyer

Reading (a): a failed "if" or "where" is the text's no (an inference: "if A then B" does not itself say "if not A then not B"), and flat negatives are the text's no.
Reading (b): a prohibition or grant limited by its own wording does not say no outside the limit.
Every branch that rests on one is listed, with the other reading.

| # | branch (file:line) | rests on | the other reading |
| --- | --- | --- | --- |
| M1 | `s 2 the guarantee is saved from unenforceability on that ground alone` (mca-act.l4:168): limb (a) not met, `JUST FALSE` at mca-act.l4:173-175 | (a), and the 2026-11-05 ruling (b) on "Where" | `NOTHING` |
| M2 | the same function: limb (b) is `JUST FALSE`, so `JUST FALSE` at mca-act.l4:176-178 | (a), ruling (b) | `NOTHING` |
| M3 | `s 2(b) the obligation is unenforceable against him, or he repudiates the contract, because he was a minor when the contract was made` (mca-act.l4:141): "because" is `JUST FALSE`, so the limb is `JUST FALSE` at mca-act.l4:146-147 (F1) | (a) | `NOTHING`, or F1's other reading |
| M4 | `s 3(1) the conditions for the court's power are met` (mca-act.l4:259): limb (a) not met, `JUST FALSE` at mca-act.l4:264-266 | (a), ruling (b) | `NOTHING` |
| M5 | the same function: limb (b) is `JUST FALSE` at mca-act.l4:267-269 | (a), ruling (b) | `NOTHING` |
| M6 | `s 3(1) the court may require the defendant to transfer property to the claimant` (mca-act.l4:308): "if it is just and equitable" is `JUST FALSE`, so `JUST FALSE` at mca-act.l4:316-317 | (a): an "if" that fails | `NOTHING` |
| M7 | `s 1 the Infants Relief Act 1874 applies to the contract` (mca-act.l4:79): s 1 reaches the contract, so `JUST FALSE` at mca-act.l4:81-82 | a flat negative, "shall not apply" (N2) | `NOTHING` |
| M8 | `s 2 the guarantee is unenforceable against the guarantor for that reason alone` (mca-act.l4:190): the guarantee is saved, so `JUST FALSE` at mca-act.l4:192-193 | a flat negative, "shall not ... be unenforceable" (N2) | `NOTHING` |
| M9 | `s 3(2) this section prejudices another remedy available to the claimant` (mca-act.l4:347): `JUST FALSE` at mca-act.l4:361-362 | a flat negative, "shall not be taken to prejudice" (N2) | `NOTHING` |
| M10 | the gate `s 4 the provision of this Act is open to apply to the contract` (mca-act.l4:436): s 4 shuts the provision out, `JUST FALSE` at mca-act.l4:438-439; and the bar question (mca-act.l4:452): `JUST TRUE` when s 4 shuts out, `JUST FALSE` when the exception is met (mca-act.l4:455-456) | a flat negative, "Nothing in this Act applies" (N2), and the exception ("except in so far as"), QA | `NOTHING` for the exception met |
| M11 | `s 1 the disapplication reaches the contract` (mca-act.l4:60): not a minor, the date met, `NOTHING` at mca-act.l4:68-70 | (b), ruling (c) | `JUST FALSE` |
| M12 | `s 3(1) the property is within what the court may require to be transferred` (mca-act.l4:287): property not acquired under the contract and not representing it, or a transferee other than the claimant, `NOTHING` at mca-act.l4:289-297 | (b), ruling (c) | `JUST FALSE` |
| M13 | `s 3(2) this section prejudices another remedy available to the claimant` (mca-act.l4:347): not "the claimant" (including a contract made on or before 9 April 1987), or a remedy that is the s 3(1) transfer itself or is not available, `NOTHING` at mca-act.l4:352-357 | (b), ruling (c); QE | `JUST FALSE` |
| M14 | `s 4 this Act is barred from applying to the contract` (mca-act.l4:452): a contract made outside the window, `JUST FALSE` at mca-act.l4:459-460 | the window is fixed in the text's own words: rulings (a) and (d) of 2026-11-05 (F2) | `NOTHING` (a scope limit, ruling (c)) |
| M15 | the "no" branches F8 and F9 above | the order in which two blockers are tested | the other order |
| M16 | `s 1 the disapplication reaches the contract` (mca-act.l4:60): a contract made on or before 9 April 1987, `JUST FALSE` at mca-act.l4:65-67 | the date is fixed in the text's own words: rulings (a) and (b) of 2026-11-05 (F2) | `NOTHING` (a scope limit, ruling (c)) |
| M17 | `s 2(b) the obligation is unenforceable against him, or he repudiates the contract, because he was a minor when the contract was made` (mca-act.l4:141), and through it `s 3(1)(b) the contract is unenforceable against the defendant, or he repudiates it, because he was a minor when the contract was made` (mca-act.l4:247): the record says no party was a minor, `JUST FALSE` at mca-act.l4:142-144 | (a): "because he was a minor" is a condition that cannot be met, ruling (b) | `NOTHING` while the reason is not known |

### Reading a result: FALSE and NOTHING

`JUST TRUE` is the Act's own yes; `JUST FALSE` is the Act saying no in its own words; `NOTHING` is "the Act does not answer on these facts".
A caller must never turn `NOTHING` into `FALSE` or into "no".

What a "no" (`JUST FALSE`) is in this row:

- For s 1: "the 1874 Act applies to this contract" is `JUST FALSE` when s 1 reaches it, because s 1 says the 1874 Act "shall not apply".
  It does not say the contract is valid, binding or ratifiable.
  "The disapplication reaches the contract" is `JUST FALSE` when the contract was made on or before 9 April 1987, the date the text fixes in its own words.
- For s 2: "the guarantee is saved" is `JUST FALSE` when no guarantee was given, when the contract was made on or before 9 April 1987, when no party was a minor, or when the obligation is not unenforceable (and there is no repudiation) because of minority, because s 2 begins "Where" those things hold.
  It does not say the guarantee is unenforceable: that question stays `NOTHING`.
- For s 3: "the court may require the transfer" is `JUST FALSE` when the claimant did not contract with the defendant, when the contract is not unenforceable against the defendant because of minority, or when the person says it is not just and equitable.
  "This section prejudices another remedy" is `JUST FALSE` when the conditions hold, which is the Act saying it does not.
- For s 4: "this provision is open to apply" is `JUST FALSE` when s 4 shuts it out, which is the Act saying "Nothing in this Act applies"; "this Act is barred from applying" is `JUST FALSE` when the exception is met or when the contract was made outside the window the text names (on or before 9 April 1987, or on or after 12 November 1993).

What "not covered" (`NOTHING`) is in this row, by why:

- silent: the Act says nothing about the law of minors' contracts at large; the 1874 Act's application to a contract s 1 does not reach.
- points outside the text: whether an obligation is unenforceable against a minor and because of minority (law outside the sources), and whether section 5 of the Civil Law Act 1909 made a provision applicable (that Act is not among the sources).
- undefined term: any word s 3(1)(a) does not define, and "just and equitable", which the Act hands to the court.
- limited by its own wording: a contract not made by a minor under s 1 (its date met), a claimant or remedy outside s 3(2)'s words, other property or another transferee under s 3(1).
- includes: the Interpretation Act's "include" entries for "person" and the masculine gender (a person who is neither male nor female; another kind of claimant) answer `NOTHING`.

## Findings (what the text turns out to say)

Each ends "Asserted." where a case asserts it, and otherwise says why not.
Section names in brackets are the headings of the test files.

1. **The Act does not answer whether a minor's contract binds the minor, can be ratified, or can be enforced.**
   It assumes the common law.
   What it says is that the 1874 Act does not apply (s 1), that a guarantee survives (s 2), that the court may order the minor to give back property (s 3), and that none of it applies to contracts made between 9 April 1987 and 12 November 1993 unless section 5 of the Civil Law Act 1909 made it applicable (s 4).
   Not asserted: there is no rule in the Act to assert it against.
2. **Section 1 is a disapplication, not a validation.**
   The only thing the Act says on these facts is that the 1874 Act does not apply, so "does the 1874 Act apply?" answers `JUST FALSE` and the two questions about its effects answer `JUST FALSE`; "is the contract valid?" is not asked.
   Asserted (mca-cases.l4, § Tests -- section 1; mca-cases-seat.l4, § Cases ... (s 1)).
3. **The Act reaches a contract made on or after 12 November 1993 without more; a contract made from 10 April 1987 to 11 November 1993 only if section 5 of the Civil Law Act 1909 made the provision applicable.**
   Section 4's window runs "after 9 April 1987 and before 12 November 1993", strictly at both ends: the contract made on 10 April 1987 and the one made on 11 November 1993 are in it; those made on 9 April 1987 and 12 November 1993 are not.
   Asserted at the day before, the day itself and the day after each date, at all four sites (mca-cases.l4, § Tests -- section 4 and § Tests -- the dates at the four sites; mca-cases-seat.l4, § Cases ... (s 4)).
4. **Section 1's own date is strict.**
   A contract made on 9 April 1987 itself is not "after 9 April 1987", so the s 1 disapplication does not reach it (`JUST FALSE`), s 2(a) and s 3(1)(a) fail (`JUST FALSE`), and the s 4 bar does not reach it (`JUST FALSE`): the four sites agree (F2).
   The exported question "does the 1874 Act apply" stays `NOTHING` for such a contract.
   Asserted.
5. **Section 2 saves a guarantee "for that reason alone" and says nothing of any other reason.**
   When s 2 saves the guarantee, "unenforceable for that reason alone" is `JUST FALSE`; when s 2 does not save it, that question is `NOTHING`, not `JUST TRUE`.
   Asserted (mca-cases-seat.l4, § Cases ... (s 2)).
6. **A minor who repudiates for a reason other than minority does not satisfy (b) on the reading taken (F1).**
   Asserted (mca-cases.l4, § Tests -- section 2, the limb (b) cases).
7. **The facts the person is asked about but the Act cannot decide stay `NOTHING` when the person is not sure.**
   "The obligation is unenforceable against the minor", "that is because they were a minor" and "section 5 of the Civil Law Act 1909 made it applicable" are asked as Yes, No or "I am not sure", and "I am not sure" is never turned into No.
   Asserted (every section's tests, and the seat cases).
8. **The legislative history says the Act applied in Singapore on 12 November 1993 "except sections 1(b) and 4(1)", and this text has no s 1(b) or s 4(1).**
   The history says it "is not part of the Act", so nothing is encoded from it; the numbering must belong to the Act the note is about (U.K. 1987, c. 13), not to this consolidation.
   A lawyer should confirm that nothing turns on it.
   Not asserted: nothing is encoded.
9. **The Act defines two words, "the claimant" and "the defendant", by a label in a bracket, and no others.**
   "Minor", "guarantee", "obligation", "property" and "the court" are undefined here, so a look-up of any other word answers `NOTHING`.
   Asserted (mca-cases.l4, § Tests -- section 3, the definition look-up).
10. **"He" and "a person" are read through the Interpretation Act 1965 s 2(1).**
    "Words importing the masculine gender include females", so a female party is within "he"; a party who is neither male nor female is `NOTHING`, because "include" does not close the list.
    "Person" includes a company, an association and a body of persons; another kind of claimant is `NOTHING`.
    Asserted (mca-cases.l4, § Tests -- the Interpretation Act as it reads this Act).
11. **Section 3(1) gives the court a power ("may"), not an order.**
    `JUST TRUE` from `s 3(1) the court may require the defendant to transfer property to the claimant` (mca-act.l4:308) means the court has the power on these facts; it does not say the court will use it.
    The court's permission, run with `#TRACE`: the court acting is `FULFILLED`; the court idle leaves a standing `MAY` and no breach; unmet conditions and "not just and equitable" are `FULFILLED` with nothing to do (four traces, compared by eye on 1.6.109 and 1.6.108, identical).
    Not asserted by `#ASSERT`: a deontic cannot be compared in `#ASSERT` on this binary, so the decision function over the same facts is asserted.
12. **"Just and equitable" is the court's judgment and the Act states no test.**
    The person states their own view or "I am not sure", which is `NOTHING`.
    Asserted.
13. **Section 3(2) protects "any other remedy available to the claimant".**
    The protected remedies are those other than the s 3(1) transfer and available to the claimant (QE); for the transfer itself or an unavailable remedy the Act says nothing.
    Asserted.
14. **The Act counts no period and runs no deadline.**
    Its two dates are compared with the day a contract was made, not counted from an event, so the Interpretation Act's time rules are not used.
    Not asserted: nothing to assert.
15. **Section 3 carries two amendment notes ("Act 25 of 2021 wef 01/04/2022"); the wording before 1 April 2022 is not among the sources.**
    One vintage is encoded: the version in force from 1 April 2022.
    Not asserted.
16. **A `NOT` bug found by the tests while writing.**
    `IF NOT (a) AND b EQUALS c` parses as `NOT ((a) AND ...)`; a first draft of `s 2(b)` answered `JUST FALSE` where it should have answered `NOTHING`, and the case that exercises "repudiation false, unenforceable unknown" caught it.
    Fixed by bracketing (mca-act.l4:149).
    See "What your main binary does not accept".
17. **"Because he was a minor" cannot hold if no party was a minor.**
    `s 2(b)` and `s 3(1)(b)` read the record's own minority fact first: when no party was a minor the limb is `JUST FALSE` whatever the reason says (a reason of "minority" with no minor is a contradiction, not a yes); when a party was a minor and the reason is not known the limb stays `NOTHING`.
    Asserted (mca-cases.l4, § Tests -- section 2 and § Tests -- section 3, limb (b), and through the whole sections).
18. **The court's power is held in two forms.**
    The fact that the court holds the s 3(1) power is a `MAYBE BOOLEAN` (`s 3(1) the court may require the defendant to transfer property to the claimant` (mca-act.l4:308)), which is asserted, and a `DEONTIC` (`s 3(1) the court's permission to require the transfer` (mca-act.l4:332)), which is run with `#TRACE` only, because a deontic cannot be compared in `#ASSERT` on this binary.
    Not asserted for the deontic.
19. **The effect of s 2 on the guarantor is carried by function names.**
    "The guarantee shall not for that reason alone be unenforceable against the guarantor" is the pair `s 2 the guarantee is saved from unenforceability on that ground alone` (mca-act.l4:168) and `s 2 the guarantee is unenforceable against the guarantor for that reason alone` (mca-act.l4:190); there is no typed record of the guarantor's position to assert against.
    Asserted as the pair's answers, not as a value.
20. **Whether the court is required to order has no function.**
    s 3(1) says "may", so the Act gives no duty to order; QD does not arise and no compliance function exists.
    Not asserted: nothing to assert.
21. **An indemnity is not asked about.**
    "A guarantee is given in respect of an obligation" is a plain yes/no fact the person states, so the encoding never decides whether an arrangement such as an indemnity is a guarantee; the "undefined term" `NOTHING` for the word "guarantee" is reached only through the look-up `s 3(1)(a) the Act's definition of` (mca-act.l4:223), not through the seat.
    Asserted for the look-up.

## What the text does not answer

- Whether a minor's contract binds the minor, can be ratified, or can be enforced against the minor or by the minor: the Act assumes the common law and says nothing (finding 1).
  These are the seat's headline questions and the encoding cannot answer them.
- At what age a person stops being a minor: the Act does not say.
  "Was a party a minor when the contract was made?" is a fact the person states, and no age is typed anywhere in this row.
- What the Infants Relief Act 1874 provides, and which contracts are "certain contracts" it invalidates: the 1874 Act is not among the sources.
- Whether section 5 of the Civil Law Act 1909 (as in force before 12 November 1993) made a provision of this Act applicable to a contract made from 10 April 1987 to 11 November 1993: that Act is not among the sources; the person is asked, and "I am not sure" is `NOTHING`.
- Whether an obligation is unenforceable against a minor, and whether that is because of minority: law outside the sources; asked.
- When the court should exercise its s 3(1) power, and what "just and equitable" requires: handed to the court.
- Whether property "representing" acquired property includes proceeds, substitutes or traceable assets: the Act does not say, so it is a fact the person states.
- Whether a contract ratified after majority is enforceable: s 1 names the 1874 Act's bar on actions on ratified contracts and disapplies that Act, but does not say the contract can be enforced.
- Whether the minor can ratify a contract, and when.
- Whether the guarantee is enforceable overall: s 2 says only that it is not unenforceable "for that reason alone".
- Any compensation in money for property the minor no longer holds or has consumed: s 3(1) speaks of transferring property, or property representing it, and says nothing of money.
- Restitution to the minor, that is, what the minor can recover from the other party: s 3 gives the court a power against the minor only.
- Any remedy other than s 3's: s 3(2) preserves them without naming which they are.
- Necessaries: the Act does not mention them.
- A time limit for a claim under s 3: the Act states none.
- A parent's or guardian's liability: the Act does not mention it.

## What your main binary does not accept

The binary governs; the skills describe constructs that main rejects.
Sorted by how the failure shows:

**Silent (a wrong answer, exit code 0):**

- **`NOT (a) AND b EQUALS c` is read as `NOT ((a) AND b EQUALS c)`.**
  `NOT` without brackets takes everything to its right.
  The wrong answer was `JUST FALSE` for a case that should have been `NOTHING`; only an assertion on that case caught it.
  Written as `(NOT (a)) AND (b EQUALS c)` at mca-act.l4:149.
- **A `#TRACE` outcome is not seen by `check.sh`'s counts.**
  The four traces in `mca-cases.l4` were run on both main builds and compared by eye (same four outcomes).

**Loud (the binary stops):**

- **A date constant with no declared type is ambiguous to `GREATER THAN`** (`Day` is overloaded).
  Compare `DATE`s directly, and give each date constant `GIVETH A DATE` at mca-act.l4:373, mca-act.l4:377 and mca-act.l4:387.
- **`length` is unknown; the list length is `count`.**
- **A `LIST` of backticked constructors on separate lines is read as a function application.**
  Put commas between items (mca-act.l4:45-47).
- **A deontic cannot be compared in `#ASSERT`.**
  `s 3(1) the court's permission to require the transfer` (mca-act.l4:332) is run with `#TRACE`, and the decision function it calls is asserted.
- **`REFUSE`, `#ASSERT REFUSED` and `BECAUSE` are not used.**
  "Not covered" is `NOTHING`, asserted.

## Dependencies

| module | Commons path | blob | sections used |
| --- | --- | --- | --- |
| `sgia-p1-definitions.l4` | `subjects/sg/interpretation-act/encodings/legalese-sonnet-5.5/sgia-p1-definitions.l4` at Commons main d468311a6ea4bab765b1ee7ccc8f0d7ccb29a357 | `ca5e2607c635962769a753d71154ad4ae6055f59` (the copy carries a 3-line header; with it removed, the blob is this one, checked) | Interpretation Act 1965 s 2(1), entries 86 ("words importing the masculine gender") and 59 ("person") |

- The copy is byte-identical to the staged one (`cmp`), unedited, and keeps its own file name under brief line 109, which overrides the `mca-` rule for file names.
  `srcrefs.py` is run on `mca-*.l4` only.
- The time module `sgia-interpretation-time.l4` is staged for this row and not copied: this Act counts no period (finding 14).
- Taken as inputs, to be filled when those Acts are encoded: section 5 of the Civil Law Act 1909 as in force before 12 November 1993 (`section 5 of the Civil Law Act 1909 made the provision applicable`, mca-nouns.l4:24); the common law of minors' contracts (the two "unenforceable ... because he was a minor" facts, mca-nouns.l4:21 and 23); the Infants Relief Act 1874, named by s 1 and not encoded.
- No time-keeping, no age of majority and no rate comes from memory.

## Unstable dialect

I looked at time, versions and workarounds and found no shape that earns a second encoding: s 4's two dates are compared with a day (plain `DATE` comparisons, no counting), s 3 has one amendment vintage in the sources (the version from 1 April 2022), and s 3(1)'s power has no deadline to count.
A second, unstable encoding of these provisions does not exist.

## What check.sh prints

**Target: main.**
Written with `l4 --version` 1.6.109 (main, 4c887e0, 2026-11-04), sha256 `eeb12f1e9d0ec646b6196d53a4b83c41160ada7f3959211aa50b0115652b73cb`, and compared with the main build 1.6.108 (main, 2ae7c9b, 2026-11-02).
Final run, after the last change to any `.l4` file (exit 0):

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.108 (main, 2ae7c9b, 2026-11-02)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
mca-act.l4                                     0         0       0        0         0 |      0         0       0        0  same
mca-cases-seat.l4                              0       103       0        0         0 |      0       103       0        0  same
mca-cases.l4                                   0       251       0        0         0 |      0       251       0        0  same
mca-nouns.l4                                   0         0       0        0         0 |      0         0       0        0  same
mca-reading.l4                                 0         0       0        0         0 |      0         0       0        0  same
mca-seat.l4                                    0         0       0        0         0 |      0         0       0        0  same
sgia-p1-definitions.l4                         0         0       0        0         0 |      0         0       0        0  same
TOTAL (7 modules)                              0       354       0        0           |      0       354       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

The first full run, before the QA change and before any fix round, printed 7 modules, 284 satisfied (193 + 91), 0 failed, 0 errors, 0 refused.
The two F8 and F9 seat cases then made it 286 (193 + 93), and the second round (the dates at the four sites, the minority fact in limb (b), the s 3(2) cases) made it 354 (251 + 103).
There is no earlier committed baseline for this row to compare with.
Every file runs with no `DiagnosticSeverity_Error` or `_Warning`; the assertions written equal the assertions satisfied (251 and 103).

## What would need doing before this encoding is worth relying on

- A lawyer reads it against the official text (this one is a converter's rendering) and rules on M1 to M17 and F1 to F11, in particular F1, F2, F3 and QA.
- The Infants Relief Act 1874 and section 5 of the Civil Law Act 1909, as in force before 12 November 1993, are encoded, so that the two facts the person is asked about can be filled by rule rather than by question.
- The common law on minors' contracts is encoded, so that the seat's headline questions (does the contract bind, can it be ratified, can it be enforced) have an answer; this Act cannot supply it.
- The wording of s 3 before 1 April 2022 is added if contracts made before that date matter.
- The "just and equitable" judgment, and what "property representing" acquired property covers, are looked at in the case law, which this row does not have.
