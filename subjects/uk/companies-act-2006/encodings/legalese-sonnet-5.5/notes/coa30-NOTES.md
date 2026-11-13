# NOTES: Companies Act 2006 (United Kingdom), part coa30 (Schedules 10 to 16, lines 20017-20928 of `ukpga-2006-46.txt`)

Written by part agent coa30 (Sonnet 5.5), 2026-11-12. Status: every module of this folder compiles on the stable binary 1.6.110 (main, e51181d, 2026-11-11) and on 1.6.109 (main, 4c887e0, 2026-11-04) with no `DiagnosticSeverity_Error` and no `_Warning`; every assertion is satisfied (1012 assertions in 8 test and case modules (and `coa30-tests-regulative.l4`, which holds the traces)); `srcrefs.py check --refs` and `--strict` report 0 problems on every coa30 file. No row of the coverage table is left `deferred`. Not reviewed by a lawyer.

Where PLAN.md and the brief differ, the brief governs. They differ in one place that mattered: PLAN.md section 5 says the two supplied builds accept `REFUSE`, `#ASSERT REFUSED` and `YMD`; the brief forbids them; none is used here ("not covered" is `NOTHING` or a constructor, and dates are `Date day month year`). The brief says layer 1 imports the keel's `coa-core.l4` and `coa-definitions.l4`, and PLAN.md section 1 step 2 says a part imports `coa-core` but never the definitions: no module here imports either, because no core type is used by layer 1 (the paragraphs need no `Company profile`, `Kind of person`, `Period`, `Penalty` or `Fine limit`: Schedules 10 to 16 create no offence and count periods as dates), and the regulative module declares its own party and act types for the reason NEEDS-CORE.md gives. PLAN.md section 6 lists `sch 1 [coa28]` among this range's seams: it is a false positive of the script (the words are "Schedule 1 to the Recognition of Professional Qualifications ... Regulations 2023" in paragraph 20A(1), not Schedule 1 of this Act).

## Source and what "verified" means here

The only source is `ukpga-2006-46.txt`, a plain-text rendering of the Act and its Schedules from legislation.gov.uk (Open Government Licence v3.0) made by a converter script (`inputs/SOURCES.md`): it is not the official text and nothing here is "verified against the official text". It is the revised text of the version dated 2026-07-16, which "may carry more than one extent version of a provision, and prospective provisions". Every `-- src:` quote line in the layer-1 modules was copied from the text by `work/build.py` (a script that reads the file; no quotation was typed), and `python3 -I srcrefs.py check --refs <text> coa30-*.l4` and `--strict` both print `0 problems` (659 quote lines, 224 runs, 232 locators). `srcrefs.py` checks that the quoted words are in the text and that each `@ref` locator reaches the quoted lines; it does not check that the `@ref` names the right provision or that the L4 means what the text says.

## Seat

The seat is the one the brief fixes: an individual who is, or is about to become, a director, a company secretary or a member (shareholder) of a company registered under the Act, or who deals with one, asking on facts they can state what the Act requires or lets them do, what rights they have against the company or its directors, what they must disclose, file, approve or vote on and by when, and what follows (liability, offences, penalties) if it is not done. (Assumed, not ruled: the Act is addressed to companies, so the individual is whoever stands in a company's management or ownership.)

How the seat maps onto Schedules 10 to 16 (assumed, not ruled; the seat fork). These Schedules address the supervisory bodies that recognise and discipline auditors, the bodies that award audit qualifications, the registered third country auditors, the body to which the Secretary of State delegates its functions, and the persons who may hold information obtained under Part 42. The individual who "deals with" a company and is affected by them is: (1) the company's statutory auditor or a would-be auditor (including an individual, a firm of auditors, a key audit partner, a third country auditor), whose eligibility, independence, inspection, sanction and transfers of audit papers the supervisory bodies' rules govern (Schedule 10 Part 2); (2) a person who holds, or wants to sit, a recognised professional qualification (Schedule 11); (3) a person who holds information obtained under Part 42 and wants to know whom it may be given to (Schedule 11A); (4) a registered third country auditor (Schedule 12); (5) a member, officer or employee of the delegated body, or a person affected by its instruments (Schedule 13); and (6) a director who asks whether the company is a public interest entity or whether its former auditor may join the board (paragraphs 9(1A), 10C(3), 20A(1)). Provisions that address only an official or a body (the Secretary of State's procedure for recognising a body, what a body must have in its rules) are encoded in layer 1 for what they decide and appear in the seat only through what they mean to the person (for example the right of a member or a person affected to make representations on a proposed revocation, paragraph 3(5)). There is never a seat for an official. Schedules 14, 15 and 16 amend and repeal other Acts and have no question.

The 43 questions of `coa30-seat.l4`:

**§ Schedule 10 -- Recognised supervisory bodies: the people they audit and the auditors they supervise**

- Under schedule 10 paragraph 3(5), may I still make representations to the Secretary of State on the proposed revocation of the recognition of a supervisory body (sch 10 para 3(5), sch 10 para 3(6))
- Under schedule 10 paragraph 3(2), does the order revoking the recognition of a supervisory body state a valid date for the revocation to take effect (sch 10 para 3(2))
- Under schedule 10 paragraph 6(1), do the rules that a recognised supervisory body must have bar me from appointment as a statutory auditor when I am an individual (sch 10 para 6(1))
- Under schedule 10 paragraph 6(1), do the rules that a recognised supervisory body must have bar my firm from appointment as a statutory auditor (sch 10 para 6(1), sch 10 para 7(3))
- Under schedule 10 paragraph 7(4), do the qualified members of my firm hold a majority of the members of the firm (sch 10 para 7(4))
- Under schedule 10 paragraph 6(1A), do I meet the requirements for a third country auditor to be eligible for appointment as a statutory auditor (sch 10 para 6(1A))
- Under schedule 10 paragraph 6(2), may the aptitude test that I am required to take test my knowledge of this matter (sch 10 para 6(2))
- Under schedule 10 paragraph 6(2B), is the period that I have been asked to complete an adaptation period (sch 10 para 6(2B))
- Under schedule 10 paragraph 6(3), may my firm, which has ceased to comply with the conditions for eligibility, be permitted to remain eligible for appointment as a statutory auditor (sch 10 para 6(3))
- Under schedule 10 paragraph 8(4), am I a controller of a body corporate for the purposes of the fit and proper test for its auditors (sch 10 para 8(4))
- Under schedule 10 paragraph 9(1A), must the rules of a recognised supervisory body bar my company's former auditor from being appointed to its board or management on this date (sch 10 para 9(1A))
- Under schedule 10 paragraph 10C(3), must the rules of a recognised supervisory body bar the former auditor of my public interest entity from being appointed to its board or management on this date (sch 10 para 10C(3))
- Under schedule 10 paragraph 9(5), is the auditor of my company regarded as an officer of the company for the purposes of the bar on a former auditor joining its board or management (sch 10 para 9(5))
- Under schedule 10 paragraph 9(4), is a fine imposed on me by my former supervisory body for breach of its independence or confidentiality rules recoverable by it as a debt (sch 10 para 9(4))
- Under schedule 10 paragraph 12(6), must my identity be kept from the public when the body publishes the sanction it imposed on me (sch 10 para 12(6))
- Under schedule 10 paragraph 12(7), must the body still be publishing the sanction imposed on me on this day (sch 10 para 12(7), sch 10 para 12(8))
- Under schedule 10 paragraph 12(4), does the temporary prohibition imposed by my former supervisory body still apply to me although I am no longer a member (sch 10 para 12(4))
- Under schedule 10 paragraph 13(3)(b)(ii), is another inspection of me due by this day (sch 10 para 13(3)(b)(ii))
- Under schedule 10 paragraph 13(5), may this person conduct the inspection of me (sch 10 para 13(5))
- Under schedule 10 paragraph 13(10), may the inspection of my firm be treated as an inspection of me as an individual responsible for its audit work (sch 10 para 13(10))
- Under schedule 10 paragraph 16A, may I transfer audit working papers and investigation reports to a third country competent authority (sch 10 para 16A(1), sch 10 para 16AA, sch 10 para 16AB)
- Under schedule 10 paragraph 16A(2), must I refuse to transfer audit working papers and investigation reports to a third country competent authority (sch 10 para 16A(2))
- Under schedule 10 paragraph 17, am I able to meet claims against me arising out of my statutory audit work (sch 10 para 17(2))
- Under schedule 10 paragraph 20A(1), is my company a public interest entity (sch 10 para 20A(1))
- Under schedule 10 paragraph 20A(1), am I a key audit partner (sch 10 para 20A(1))

**§ Schedule 11 -- Recognised professional qualifications (for the person who holds, or wants, one)**

- Under schedule 11 paragraph 3(5), as a holder of or student for a recognised professional qualification, may I still make representations on the proposed revocation of its recognition (sch 11 para 3(5), sch 11 para 3(6))
- Under schedule 11 paragraph 6, may the qualification be open to me (sch 11 para 6(1), sch 11 para 6(2), sch 11 para 6(4))
- Under schedule 11 paragraph 7, may the qualification be restricted to me because of my course of theoretical instruction or my professional experience (sch 11 para 7)
- Under schedule 11 paragraph 8, is the examination that I have passed of the kind that the qualification must require, allowing for sub-paragraphs (2) and (3) (sch 11 para 8(1), sch 11 para 8(2), sch 11 para 8(3))
- Under schedule 11 paragraph 9, does my practical training meet the requirements of sub-paragraphs (1) and (4) (three years, audit work, and two-thirds given by eligible persons) (sch 11 para 9(1), sch 11 para 9(4))
- Under schedule 11 paragraph 10(1), how many years of professional experience are required of me once my theoretical instruction is deducted (sch 11 para 10(1))

**§ Schedule 11A -- Disclosure of information obtained under Part 42 (for a person who holds such information and wonders whom it may be given to)**

- Under schedule 11A paragraphs 1 to 17D, is the person I want to disclose the information to a specified person (sch 11A part 1)
- Under schedule 11A paragraphs 18 to 78, is my disclosure of the information one of the specified descriptions of disclosure (sch 11A part 2)
- Under schedule 11A paragraph 79, is my disclosure to an approved third country competent authority made in accordance with Part 3 of the Schedule (sch 11A para 79)
- Under schedule 11A paragraph 80, is my disclosure to a third country competent authority made in accordance with Part 3 of the Schedule (sch 11A para 80)

**§ Schedule 12 -- Registered third country auditors (for a registered third country auditor)**

- Under schedule 12 paragraph 4, have I paid the costs of the monitoring and disciplinary arrangements that the arrangements provide I am to pay (sch 12 para 4)
- Under schedule 12 paragraph 2(1A), may a decision on disciplinary action against me be made without a hearing because I agree in writing (sch 12 para 2(1A))
- Under schedule 12 paragraph 6(1), am I obliged to participate in this set of arrangements when there are two or more (sch 12 para 6(1))

**§ Schedule 13 -- The body to which the Secretary of State's functions are delegated (for a member, an employee, or a person affected by its instruments)**

- Under schedule 13 paragraph 2, am I, as a member, officer or employee of the body designated by a delegation order, to be regarded as a Crown servant (sch 13 para 2)
- Under schedule 13 paragraph 4(3), has the body paid me the compensation that it must pay for ceasing to be a member before the end of my term (sch 13 para 4(3))
- Under schedule 13 paragraph 8(2), does the fact that an instrument of the body had not been made available give me a defence to an alleged contravention of it (sch 13 para 8(2))
- Under schedule 13 paragraph 9(3), may I require the body to cause a copy of its instrument to be endorsed with a certificate for use in legal proceedings (sch 13 para 9(3))
- Under schedule 13 paragraph 10(6), may I be appointed as auditor of the body (sch 13 para 10(6))

Each question begins "Under schedule N paragraph M," (or "paragraphs M to N,"), has `@export` and, on every input, `@desc` worded as that person would be asked, and calls the layer-1 rules; no rule is restated in the seat layer. Each has at least one case in `coa30-cases-seat.l4` (135 cases). The questions about Schedule 11A take a choice from the list's own type (a constructor per paragraph), which is thinner than one export per paragraph (about 110 would be needed); this is deliberate and the type is in `coa30-sch11a.l4`.

### Seat audit of 2026-11-12

Every one of the 43 seat questions was read, name and `@export` text against the layer-1 function its body calls. Five mismatched, all of the subject kind (the name asked one thing and the function answered another); none was a direction mismatch (a permission titled over a bar, or the reverse). The five were retitled together with their `@export` text, and each of their 15 case assertions is restated in place under a `-- RECONCILED 2026-11-12: was ...` comment (the facts and the expected values did not change):

1. was: `Under schedule 10 paragraph 3(2), is the date stated for the revocation of the recognition of a supervisory body to take effect late enough`; now: `Under schedule 10 paragraph 3(2), does the order revoking the recognition of a supervisory body state a valid date for the revocation to take effect`
2. was: `Under schedule 11 paragraph 8, may the qualification be awarded to me on the examination that I have passed`; now: `Under schedule 11 paragraph 8, is the examination that I have passed of the kind that the qualification must require, allowing for sub-paragraphs (2) and (3)`
3. was: `Under schedule 11 paragraph 9, does my practical training meet the requirements for the qualification`; now: `Under schedule 11 paragraph 9, does my practical training meet the requirements of sub-paragraphs (1) and (4) (three years, audit work, and two-thirds given by eligible persons)`
4. was: `Under schedule 12 paragraph 4, must I pay the costs of the monitoring and disciplinary arrangements that I am obliged to take part in`; now: `Under schedule 12 paragraph 4, have I paid the costs of the monitoring and disciplinary arrangements that the arrangements provide I am to pay`
5. was: `Under schedule 13 paragraph 2, am I, as a member, officer or employee of the body designated by a delegation order, a Crown servant`; now: `Under schedule 13 paragraph 2, am I, as a member, officer or employee of the body designated by a delegation order, to be regarded as a Crown servant`

Questions read and kept: the bar questions ("do the rules ... bar me", "must the rules ... bar", "must my identity be kept from the public", "must I refuse to transfer") are named as the function states them, so JUST TRUE is the bar and JUST FALSE is "the text says no to the bar". Four "may" questions rest on an "only if" paragraph (Schedule 10 paragraph 16A(1), Schedule 11 paragraphs 6(1) and 7, Schedule 13 paragraph 10(6)): their name and function say the same thing, and JUST TRUE there means the paragraph's condition is met and this paragraph does not bar, not that no other provision could; they were kept because the layer-1 function says exactly that. The permission questions (`may I ...`) answer JUST TRUE as the paragraph's own yes.

## What is encoded and what is not

Encoded: Schedules 10 to 13 in full, as layer-1 modules that follow the Schedules' own paragraph numbering: `coa30-sch10-part1.l4` (paras 1 to 5), `coa30-sch10-part2-a.l4` (5A to 8), `coa30-sch10-part2-b.l4` (9 to 20A), `coa30-sch11.l4`, `coa30-sch11a.l4` (the lists of Parts 1 and 2 as enumerated types with one lookup function each, and Part 3), `coa30-sch12.l4`, `coa30-sch13.l4`, and `coa30-regulative.l4` (the duties of these Schedules as regulative rules, each with a decision-function twin in the module it cites). The tests are `coa30-tests-*.l4`; the seat layer is `coa30-seat.l4` with cases in `coa30-cases-seat.l4`.

Not encoded, and why (inert, with the reason number of the brief): the headings and the reference lines ("Section 1217") (reason 1); Schedules 14, 15 and 16, which amend and repeal other Acts and Orders (reason 2: amendments of other Acts); in Schedule 13, the body's name, members, chairman and proceedings (paras 3 and 5), the power to make an order on consultation (7(3)), the orders on the transfer or resumption of a function (11(2) to (4)) and on revocation (12) (reason 2: boards, offices, staffing and order-making powers); Schedule 12 paragraph 6(2) and Schedule 11 paragraph 8(4) (a statement that an order or regulations are subject to negative resolution procedure: reason 2); Schedule 10 paragraph 7(1) (a signpost, reason 1, fork). The 35 units the text shows as dots (Schedule 10 Part 3 paragraphs 21 to 27 and their headings, and the omitted limbs inside Part 2) are `repealed or blank in this text` (reason 3). Amounts, periods and thresholds the Act leaves to regulations, standards or the Secretary of State (the length of the bar above the minimum in 9(1A) and 10C(3), the amounts the Secretary of State determines under Schedule 13 paragraph 4) are inputs.

## Rulings applied (recorded word for word)

The brief's rulings that the `NOTHING-kind` and `FALSE-kind` tags in these modules rest on, copied from the brief:

- **E1** (bench `commons-negation-1030`; should a legal effect be one definition gathered from every section that gives it?): option B, as guidance for gathering a legal effect's routes by hand only, with no pilot run; option A (gathering by bare name) is withdrawn as a direction for the language, not deferred; option C (per-section answers) applies everywhere else; the Magna Carta pilot in the printed recommendation (chapters 2, 3, 4, 5, 37, 43, 46 and 53, with a blind second reader) is not to be run. The maintainer's lean, verbatim: "B but generally uncomfortable with this much magic because it takes the language from unopinionated to opinionated in ways that are hard to teach an l4 novice." the maintainer's note, verbatim: "Fundamentally I feel like we are trying to make the language do work that the human l4 drafter should do. Too much magic. Can’t we just decline to be this opinionated and say the programmer needs to do this thinking?" Marked 2026-11-03T23:19:02.812Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
- **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. The maintainer's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." the maintainer's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
- **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. The maintainer's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.
- **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. The maintainer approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.
- **Questions with no convention: decide case by case (the maintainer, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. The maintainer's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with the coordinator where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

## Tests (coa30): what each kind of assertion proves

The expected values were decided from the text, one paragraph at a time, before each module was run, and a failing assertion would have been a finding (none failed). They are not all independent of the code, and the brief's independent test pass (a second reader who writes expectations before opening the encoding) was not possible here (one agent, no subagents). Of the 1012 assertions, 145 were emitted by the same generator call (`req()` in `work/genlib.py`) that emitted the function they test: for a "The body must have ..." paragraph the function is the conjunction of the paragraph's limbs and the tests are "all limbs true is JUST TRUE; each single limb false is JUST FALSE (or a gated limb vacuously met)". Those prove the wiring (every limb is read, none is dropped, the gate works); they cannot prove that the limbs were read correctly from the text, because a misread conjunction would pass. Each of those sites lists things the body must have, joined by "and" or listed cumulatively with no "or" (read by eye, not by script); the one disjunctive limb pair of Part 1 (paragraph 2(4)) is hand-written, not generated. Another 112 (the Schedule 11A table tests) are one per constructor and prove that each paragraph's constructor is wired to JUST TRUE, not that the paragraph's description was transcribed correctly (the labels were written by hand from the text and each carries its paragraph number). The remaining 755 assertions were written by hand with the expectation decided from the paragraph, including both sides of every period, threshold and boundary (three months at 31 March and 1 April, 15% at 0.15 and 0.1499, seven years at 7 and 6.9, 36 months, two-thirds of training, six years, three years, five years) and every case that falls outside the encoding (`NOTHING`); the 135 seat cases are among them. A lawyer's or a second reader's pass remains owed.

## Coverage (coa30)

Every unit of lines 20017-20928 has one row: 823 rows built from the text by `work/segment.py` (a Schedule or Part heading, a reference line, a cross-heading, a numbered paragraph, a sub-paragraph, a lettered or roman limb, a defined term, a repealed or omitted line, a table row), and the script that builds this table refuses to run unless every non-blank line of the range falls in a row and every row has a disposition (the audit: 912 lines, all non-blank, all claimed; rows before the table was filled: 823; rows in the table: 823). Counts per disposition:

- encoded: 182
- fork: 412
- inert (reason 1): 98
- inert (reason 2): 96
- repealed or blank in this text (reason 3): 35

"fork" is a row whose function carries a fork-register entry (the other reading changes an answer); "encoded" is a row whose function has none; both rows have a test. A limb row ("limb of the row above") is encoded by the function of its sub-paragraph. "tests" counts the `#ASSERT` lines of the test and case modules that call a function of the row (a line that calls two functions counts once for each). Kinds of row: {'heading': 97, 'sub-paragraph': 208, 'limb': 317, 'paragraph': 128, 'defined term': 16, 'blank marker': 2, 'table row': 55}.

| provision | text lines | disposition | L4 name | tests | forks | note |
| --- | --- | --- | --- | --- | --- | --- |
| sch 10 heading | 20017 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 10 section reference | 20018 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 10 part 1 heading | 20019 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 10 cross-heading (line 20020) "Application for recognition of supervisory body" | 20020 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 10 para 1(1) | 20021 | fork | `sch 10 para 1(1) the body may apply to the Secretary of State for a recognition order` | 3 | F1 |  |
| sch 10 para 1(2) | 20022 | fork | `sch 10 para 1(2) the application is made and accompanied as required` | 3 | F2 |  |
| sch 10 para 1(2)(a) | 20023 | fork | limb of the row above: `sch 10 para 1(2) the application is made and accompanied as required` |  | F2 |  |
| sch 10 para 1(2)(b) | 20024 | fork | limb of the row above: `sch 10 para 1(2) the application is made and accompanied as required` |  | F2 |  |
| sch 10 para 1(3) | 20025 | fork | `sch 10 para 1(3) the Secretary of State may require the applicant to furnish additional information` | 3 | F3 |  |
| sch 10 para 1(4) | 20026 | fork | `sch 10 para 1(4) the directions and requirements may differ as between different applications` | 3 | F1 |  |
| sch 10 para 1(5) | 20027 | fork | `sch 10 para 1(5) the Secretary of State may specify the form or manner of verification` | 2 | F1 |  |
| sch 10 para 1(6) | 20028 | fork | `sch 10 para 1(6) the application is accompanied as required` | 4 | F2 |  |
| sch 10 para 1(6)(a) | 20029 | fork | limb of the row above: `sch 10 para 1(6) the application is accompanied as required` |  | F2 |  |
| sch 10 para 1(6)(b) | 20030 | fork | limb of the row above: `sch 10 para 1(6) the application is accompanied as required` |  | F2 |  |
| sch 10 para 1(7) | 20031 | encoded | `sch 10 para 1(7) the guidance is guidance issued by the applicant` | 4 |  |  |
| sch 10 para 1(7)(a) | 20032 | encoded | limb of the row above: `sch 10 para 1(7) the guidance is guidance issued by the applicant` |  |  |  |
| sch 10 para 1(7)(b) | 20033 | encoded | limb of the row above: `sch 10 para 1(7) the guidance is guidance issued by the applicant` |  |  |  |
| sch 10 para 1(7)(c) | 20034-20035 | encoded | limb of the row above: `sch 10 para 1(7) the guidance is guidance issued by the applicant` |  |  |  |
| sch 10 cross-heading (line 20036) "Grant and refusal of recognition" | 20036 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 10 para 2(1) | 20037 | fork | `sch 10 para 2(1) the Secretary of State may make or refuse to make a recognition order` | 3 | F4 |  |
| sch 10 para 2(2) | 20038 | encoded | `sch 10 para 2(2) the Secretary of State may make a recognition order` | 4 |  |  |
| sch 10 para 2(2)(a) | 20039 | encoded | limb of the row above: `sch 10 para 2(2) the Secretary of State may make a recognition order` |  |  |  |
| sch 10 para 2(2)(b) | 20040 | encoded | limb of the row above: `sch 10 para 2(2) the Secretary of State may make a recognition order` |  |  |  |
| sch 10 para 2(2)(c) | 20041 | encoded | limb of the row above: `sch 10 para 2(2) the Secretary of State may make a recognition order` |  |  |  |
| sch 10 para 2(3) | 20042 | fork | `sch 10 para 2(3) the Secretary of State may refuse to make a recognition order` | 4 | F5 |  |
| sch 10 para 2(3)(a) | 20043 | fork | limb of the row above: `sch 10 para 2(3) the Secretary of State may refuse to make a recognition order` |  | F5 |  |
| sch 10 para 2(3)(b) | 20044 | fork | limb of the row above: `sch 10 para 2(3) the Secretary of State may refuse to make a recognition order` |  | F5 |  |
| sch 10 para 2(4) | 20045 | fork | `sch 10 para 2(4) the Secretary of State`; `sch 10 para 2(4) the recognised supervisory body`; `sch 10 para 2(4) a person within paragraph 3(6)` (+6 more) | 4 | F2 |  |
| sch 10 para 2(4)(a) | 20046 | fork | limb of the row above: `sch 10 para 2(4) the Secretary of State` (+8) |  | F2 |  |
| sch 10 para 2(4)(b) | 20047 | fork | limb of the row above: `sch 10 para 2(4) the Secretary of State` (+8) |  | F2 |  |
| sch 10 para 2(5) | 20048 | fork | `sch 10 para 2(5) the recognition order is made as required` | 2 | F2 |  |
| sch 10 cross-heading (line 20049) "Revocation of recognition" | 20049 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 10 para 3(1) | 20050 | fork | `sch 10 para 3(1) the Secretary of State may revoke the recognition order` | 7 | F6 |  |
| sch 10 para 3(1)(a) | 20051 | fork | limb of the row above: `sch 10 para 3(1) the Secretary of State may revoke the recognition order` |  | F6 |  |
| sch 10 para 3(1)(b) | 20052 | fork | limb of the row above: `sch 10 para 3(1) the Secretary of State may revoke the recognition order` |  | F6 |  |
| sch 10 para 3(1)(c) | 20053 | fork | limb of the row above: `sch 10 para 3(1) the Secretary of State may revoke the recognition order` |  | F6 |  |
| sch 10 para 3(1A) | 20054 | fork | `sch 10 para 3(1A) the Secretary of State may revoke the recognition order` | 3 | F7 |  |
| sch 10 para 3(1A)(a) | 20055 | fork | limb of the row above: `sch 10 para 3(1A) the Secretary of State may revoke the recognition order` |  | F7 |  |
| sch 10 para 3(1A)(b) | 20056 | fork | limb of the row above: `sch 10 para 3(1A) the Secretary of State may revoke the recognition order` |  | F7 |  |
| sch 10 para 3(2) | 20057 | fork | `sch 10 para 3(2) the first day after a period of months beginning with a date`; `sch 10 para 3(2) the revocation order states a valid date of effect` | 10 | F8, F9 |  |
| sch 10 para 3(3) | 20058 | fork | `sch 10 para 3(3) the duties before revoking`; `sch 10 para 3(3) the Secretary of State has done what he must do before revoking` | 4 | F2 |  |
| sch 10 para 3(3)(a) | 20059 | fork | limb of the row above: `sch 10 para 3(3)(a) give written notice of the intention to revoke to the recognised body` |  | F2 |  |
| sch 10 para 3(3)(b) | 20060 | fork | limb of the row above: `sch 10 para 3(3)(b) take reasonably practicable steps to bring the notice to the attention of the members` |  | F2 |  |
| sch 10 para 3(3)(c) | 20061 | fork | limb of the row above: `sch 10 para 3(3)(c) publish the notice` |  | F2 |  |
| sch 10 para 3(4) | 20062 | fork | `sch 10 para 3(4) the notice has the contents required` | 3 | F2 |  |
| sch 10 para 3(4)(a) | 20063 | fork | limb of the row above: `sch 10 para 3(4) the notice has the contents required` |  | F2 |  |
| sch 10 para 3(4)(b) | 20064 | fork | limb of the row above: `sch 10 para 3(4) the notice has the contents required` |  | F2 |  |
| sch 10 para 3(5) | 20065 | fork | `sch 10 para 3(5) make written or oral representations`; `sch 10 para 3(5) the permission to make representations`; `sch 10 para 3(5) the person may make written and oral representations` | 7 | F8, F10 |  |
| sch 10 para 3(6) | 20066 | fork | `sch 10 para 3(6) the person is within this sub-paragraph` | 4 | F11 |  |
| sch 10 para 3(6)(a) | 20067 | fork | limb of the row above: `sch 10 para 3(6) the person is within this sub-paragraph` |  | F11 |  |
| sch 10 para 3(6)(b) | 20068 | fork | limb of the row above: `sch 10 para 3(6) the person is within this sub-paragraph` |  | F11 |  |
| sch 10 para 3(6)(c) | 20069 | fork | limb of the row above: `sch 10 para 3(6) the person is within this sub-paragraph` |  | F11 |  |
| sch 10 para 3(7) | 20070 | fork | `sch 10 para 3(7) the Secretary of State has had regard to the representations` | 3 | F12 |  |
| sch 10 para 3(8) | 20071 | fork | `sch 10 para 3(8) the Secretary of State may revoke without regard to the restriction in sub-paragraph (2)` | 2 | F13 |  |
| sch 10 para 3(8)(a) | 20072 | fork | limb of the row above: `sch 10 para 3(8) the Secretary of State may revoke without regard to the restriction in sub-paragraph (2)` |  | F13 |  |
| sch 10 para 3(8)(b) | 20073 | fork | limb of the row above: `sch 10 para 3(8) the Secretary of State may revoke without regard to the restriction in sub-paragraph (2)` |  | F13 |  |
| sch 10 para 3(9) | 20074 | fork | `sch 10 para 3(9) the revocation order may contain the transitional provision` | 2 | F1 |  |
| sch 10 para 3(10) | 20075 | fork | `sch 10 para 3(10) the revocation is not subject to the restrictions and requirements listed` | 2 | F1 |  |
| sch 10 para 3(10)(a) | 20076 | fork | limb of the row above: `sch 10 para 3(10) the revocation is not subject to the restrictions and requirements listed` |  | F1 |  |
| sch 10 para 3(10)(b) | 20077 | fork | limb of the row above: `sch 10 para 3(10) the revocation is not subject to the restrictions and requirements listed` |  | F1 |  |
| sch 10 para 3(11) | 20078 | fork | `sch 10 para 3(11) the duties on making the order`; `sch 10 para 3(11) the Secretary of State has done what he must do on making the revocation order` | 4 | F2 |  |
| sch 10 para 3(11)(a) | 20079 | fork | limb of the row above: `sch 10 para 3(11)(a) give written notice of the making of the order to the body` |  | F2 |  |
| sch 10 para 3(11)(b) | 20080 | fork | limb of the row above: `sch 10 para 3(11)(b) take reasonably practicable steps to bring the making of the order to the attention of the members` |  | F2 |  |
| sch 10 para 3(11)(c) | 20081 | fork | limb of the row above: `sch 10 para 3(11)(c) publish a notice of the making of the order` |  | F2 |  |
| sch 10 cross-heading (line 20082) "Transitional provision" | 20082 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 10 para 4 | 20083 | fork | `sch 10 para 4 the order has effect after commencement as an order made under paragraph 2(1) of this Schedule` | 3 | F14 |  |
| sch 10 para 4(a) | 20084 | fork | limb of the row above: `sch 10 para 4 the order has effect after commencement as an order made under paragraph 2(1) of this Schedule` |  | F14 |  |
| sch 10 para 4(b) | 20085-20086 | fork | limb of the row above: `sch 10 para 4 the order has effect after commencement as an order made under paragraph 2(1) of this Schedule` |  | F14 |  |
| sch 10 cross-heading (line 20087) "Orders not statutory instruments" | 20087 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 10 para 5 | 20088 | fork | `sch 10 para 5 the order is to be made by statutory instrument` | 2 | F1 |  |
| sch 10 part 2 heading | 20089 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 10 cross-heading (line 20090) "Delegation etc. of tasks by competent authority" | 20090 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 10 para 5A | 20091 | fork | `sch 10 para 5A the body meets the requirement` | 4 | F15 |  |
| sch 10 para 5A(a) | 20092 | fork | limb of the row above: `sch 10 para 5A the body meets the requirement` |  | F15 |  |
| sch 10 para 5A(b) | 20093 | fork | limb of the row above: `sch 10 para 5A the body meets the requirement` |  | F15 |  |
| sch 10 para 5A(c) | 20094 | fork | limb of the row above: `sch 10 para 5A the body meets the requirement` |  | F15 |  |
| sch 10 cross-heading (line 20095) "Consultation" | 20095 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 10 para 5B | 20096 | fork | `sch 10 para 5B the body meets the requirement` | 2 | F16 |  |
| sch 10 cross-heading (line 20097) "Holding of appropriate qualification" | 20097 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 10 para 6(1) | 20098 | fork | `sch 10 para 6(1) the person is not eligible for appointment as a statutory auditor under the rule the body must have` | 11 | F17 |  |
| sch 10 para 6(1)(a) | 20099 | fork | limb of the row above: `sch 10 para 6(1) the person is not eligible for appointment as a statutory auditor under the rule the body must have` |  | F17 |  |
| sch 10 para 6(1)(aa) | 20100 | fork | limb of the row above: `sch 10 para 6(1) the person is not eligible for appointment as a statutory auditor under the rule the body must have` |  | F17 |  |
| sch 10 para 6(1)(aa)(i) | 20101 | fork | limb of the row above: `sch 10 para 6(1) the person is not eligible for appointment as a statutory auditor under the rule the body must have` |  | F17 |  |
| sch 10 para 6(1)(aa)(ii) | 20102 | fork | limb of the row above: `sch 10 para 6(1) the person is not eligible for appointment as a statutory auditor under the rule the body must have` |  | F17 |  |
| sch 10 para 6(1)(aa)(iii) | 20103 | fork | limb of the row above: `sch 10 para 6(1) the person is not eligible for appointment as a statutory auditor under the rule the body must have` |  | F17 |  |
| sch 10 para 6(1)(b) | 20104 | fork | limb of the row above: `sch 10 para 6(1) the person is not eligible for appointment as a statutory auditor under the rule the body must have` |  | F17 |  |
| sch 10 para 6(1)(b)(i) | 20105 | fork | limb of the row above: `sch 10 para 6(1) the person is not eligible for appointment as a statutory auditor under the rule the body must have` |  | F17 |  |
| sch 10 para 6(1)(b)(ii) | 20106 | fork | limb of the row above: `sch 10 para 6(1) the person is not eligible for appointment as a statutory auditor under the rule the body must have` |  | F17 |  |
| sch 10 para 6(1)(c) | 20107 | repealed or blank in this text (reason 3) | - | - | F17 | the text shows only dots: nothing to encode |
| sch 10 para 6(1A) | 20108 | fork | `sch 10 para 6(1A) the requirements of this sub-paragraph are met` | 11 | F18 |  |
| sch 10 para 6(1A)(a) | 20109 | fork | limb of the row above: `sch 10 para 6(1A) the requirements of this sub-paragraph are met` |  | F18 |  |
| sch 10 para 6(1A)(b) | 20110 | fork | limb of the row above: `sch 10 para 6(1A) the requirements of this sub-paragraph are met` |  | F18 |  |
| sch 10 para 6(1A)(b)(i) | 20111 | fork | limb of the row above: `sch 10 para 6(1A) the requirements of this sub-paragraph are met` |  | F18 |  |
| sch 10 para 6(1A)(b)(ii) | 20112 | fork | limb of the row above: `sch 10 para 6(1A) the requirements of this sub-paragraph are met` |  | F18 |  |
| sch 10 para 6(1A)(b)(iii) | 20113 | fork | limb of the row above: `sch 10 para 6(1A) the requirements of this sub-paragraph are met` |  | F18 |  |
| sch 10 para 6(1A)(c) | 20114 | fork | limb of the row above: `sch 10 para 6(1A) the requirements of this sub-paragraph are met` |  | F18 |  |
| sch 10 para 6(1A)(c)(i) | 20115 | fork | limb of the row above: `sch 10 para 6(1A) the requirements of this sub-paragraph are met` |  | F18 |  |
| sch 10 para 6(1A)(c)(ii) | 20116 | fork | limb of the row above: `sch 10 para 6(1A) the requirements of this sub-paragraph are met` |  | F18 |  |
| sch 10 para 6(1B) | 20117 | encoded | `sch 10 para 6(1B) another requirement`; `sch 10 para 6(1B) the rules of the body specify one of the requirements listed` | 5 |  |  |
| sch 10 para 6(1B)(a) | 20118 | encoded | limb of the row above: `sch 10 para 6(1B)(a) a requirement to pass an aptitude test` |  |  |  |
| sch 10 para 6(1B)(b) | 20119 | encoded | limb of the row above: `sch 10 para 6(1B)(b) a requirement to complete an adaptation period` |  |  |  |
| sch 10 para 6(1B)(c) | 20120 | encoded | limb of the row above: `sch 10 para 6(1B)(c) a requirement either to pass an aptitude test or to complete an adaptation period at the choice of the individual` |  |  |  |
| sch 10 para 6(2) | 20121 | encoded | `sch 10 para 6(2) the aptitude test may test the person's knowledge of the matter` | 5 |  |  |
| sch 10 para 6(2)(a) | 20122 | encoded | limb of the row above: `sch 10 para 6(2)(a) the aptitude test must test the person's knowledge of the subject` |  |  |  |
| sch 10 para 6(2)(a)(i) | 20123 | encoded | limb of the row above: `sch 10 para 6(2)(a) the aptitude test must test the person's knowledge of the subject` |  |  |  |
| sch 10 para 6(2)(a)(ii) | 20124 | encoded | limb of the row above: `sch 10 para 6(2)(a) the aptitude test must test the person's knowledge of the subject` |  |  |  |
| sch 10 para 6(2)(a)(iii) | 20125 | encoded | limb of the row above: `sch 10 para 6(2)(a) the aptitude test must test the person's knowledge of the subject` |  |  |  |
| sch 10 para 6(2)(b) | 20126 | encoded | limb of the row above: `sch 10 para 6(2) the aptitude test may test the person's knowledge of the matter` |  |  |  |
| sch 10 para 6(2)(c) | 20127 | encoded | limb of the row above: `sch 10 para 6(2) the aptitude test may test the person's knowledge of the matter` |  |  |  |
| sch 10 para 6(2A) | 20128 | repealed or blank in this text (reason 3) | - | - |  | the text shows only dots: nothing to encode |
| sch 10 para 6(2B) | 20129 | encoded | `sch 10 para 6(2B) the period is an adaptation period` | 4 |  |  |
| sch 10 para 6(2C) | 20130 | fork | `sch 10 para 6(2C) the body meets the requirements for the adaptation period` | 5 | F19 |  |
| sch 10 para 6(2C)(a) | 20131 | fork | limb of the row above: `sch 10 para 6(2C) the body meets the requirements for the adaptation period` |  | F19 |  |
| sch 10 para 6(2C)(b) | 20132 | fork | limb of the row above: `sch 10 para 6(2C)(b) the applicant may be required to undergo further training during the adaptation period` |  | F19 |  |
| sch 10 para 6(2C)(c) | 20133 | fork | limb of the row above: `sch 10 para 6(2C) the body meets the requirements for the adaptation period` |  | F19 |  |
| sch 10 para 6(2C)(d) | 20134 | fork | limb of the row above: `sch 10 para 6(2C) the body meets the requirements for the adaptation period` |  | F19 |  |
| sch 10 para 6(3) | 20135 | fork | `sch 10 para 6(3) the firm may be permitted to remain eligible for appointment as a statutory auditor` | 4 | F8, F20 |  |
| sch 10 para 7(1) | 20136 | inert (reason 1) | - | - | F21 | a signpost: it says what paragraph 7 explains and creates no rule (fork) |
| sch 10 para 7(2) | 20137 | fork | `sch 10 para 7(2) the person is qualified` | 5 | F22 |  |
| sch 10 para 7(2)(a) | 20138 | fork | limb of the row above: `sch 10 para 7(2) the person is qualified` |  | F22 |  |
| sch 10 para 7(2)(a)(i) | 20139 | fork | limb of the row above: `sch 10 para 7(2) the person is qualified` |  | F22 |  |
| sch 10 para 7(2)(a)(ii) | 20140 | fork | limb of the row above: `sch 10 para 7(2) the person is qualified` |  | F22 |  |
| sch 10 para 7(2)(b) | 20141 | fork | limb of the row above: `sch 10 para 7(2) the person is qualified` |  | F22 |  |
| sch 10 para 7(2)(b)(i) | 20142 | fork | limb of the row above: `sch 10 para 7(2) the person is qualified` |  | F22 |  |
| sch 10 para 7(2)(b)(ii) | 20143 | repealed or blank in this text (reason 3) | - | - | F22 | the text shows only dots: nothing to encode |
| sch 10 para 7(3) | 20144 | encoded | `sch 10 para 7(3) the firm is controlled by qualified persons` | 7 |  |  |
| sch 10 para 7(3)(a) | 20145 | encoded | limb of the row above: `sch 10 para 7(3) the firm is controlled by qualified persons` |  |  |  |
| sch 10 para 7(3)(b) | 20146 | encoded | limb of the row above: `sch 10 para 7(3) the firm is controlled by qualified persons` |  |  |  |
| sch 10 para 7(4) | 20147 | fork | `sch 10 para 7(4) the qualified members are a majority of the members of the firm` | 5 | F22 |  |
| sch 10 para 7(4)(a) | 20148 | fork | limb of the row above: `sch 10 para 7(4) the qualified members are a majority of the members of the firm` |  | F22 |  |
| sch 10 para 7(4)(b) | 20149 | fork | limb of the row above: `sch 10 para 7(4) the qualified members are a majority of the members of the firm` |  | F22 |  |
| sch 10 para 7(5) | 20150 | fork | `sch 10 para 7(5) the qualified members are a majority of the members of the management body of the firm` | 4 | F22 |  |
| sch 10 para 7(5)(a) | 20151 | fork | limb of the row above: `sch 10 para 7(5) the qualified members are a majority of the members of the management body of the firm` |  | F22 |  |
| sch 10 para 7(5)(b) | 20152 | fork | limb of the row above: `sch 10 para 7(5) the qualified members are a majority of the members of the management body of the firm` |  | F22 |  |
| sch 10 para 7(6) | 20153 | encoded | `sch 10 para 7(6) paragraphs 5 to 11 of Schedule 7 apply to the counting of rights` | 2 |  |  |
| sch 10 para 7A(1) | 20154 | fork | `sch 10 para 7A(1) the body meets the requirement` | 2 | F23 |  |
| sch 10 para 7A(2) | 20155 | fork | `sch 10 para 7A(2) the body meets the requirement` | 2 | F24 |  |
| sch 10 para 7A(3) | 20156 | encoded | `sch 10 para 7A(3) the applicant may be required to undergo further training during the adaptation period` | 3 |  |  |
| sch 10 para 7A(4) | 20157 | fork | `sch 10 para 7A(4) the body meets the requirement` | 2 | F25 |  |
| sch 10 para 7A(5) | 20158 | fork | `sch 10 para 7A(5) the body meets the requirement` | 2 | F26 |  |
| sch 10 cross-heading (line 20159) "Auditors to be fit and proper persons" | 20159 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 10 para 8(1) | 20160 | fork | `sch 10 para 8(1) the body meets the requirement` | 2 | F27 |  |
| sch 10 para 8(2) | 20161 | fork | `sch 10 para 8(2) any other person`; `sch 10 para 8(2) the matters the body may take into account must include a matter relating to this person` | 12 | F28 |  |
| sch 10 para 8(2)(a) | 20162 | fork | limb of the row above: `sch 10 para 8(2)(a) a person employed by or associated with the person for statutory audit work` |  | F28 |  |
| sch 10 para 8(2)(b) | 20163 | fork | limb of the row above: `sch 10 para 8(2) any other person` (+1) |  | F28 |  |
| sch 10 para 8(2)(b)(i) | 20164 | fork | limb of the row above: `sch 10 para 8(2)(b)(i) a director or controller of the body corporate` |  | F28 |  |
| sch 10 para 8(2)(b)(ii) | 20165 | fork | limb of the row above: `sch 10 para 8(2)(b)(ii) another body corporate in the same group` |  | F28 |  |
| sch 10 para 8(2)(b)(iii) | 20166 | fork | limb of the row above: `sch 10 para 8(2)(b)(iii) a director or controller of such another body corporate` |  | F28 |  |
| sch 10 para 8(2)(c) | 20167 | fork | limb of the row above: `sch 10 para 8(2) any other person` (+1) |  | F28 |  |
| sch 10 para 8(2)(c)(i) | 20168 | fork | limb of the row above: `sch 10 para 8(2)(c)(i) a partner` |  | F28 |  |
| sch 10 para 8(2)(c)(ii) | 20169 | fork | limb of the row above: `sch 10 para 8(2)(c)(ii) a director or controller of a partner` |  | F28 |  |
| sch 10 para 8(2)(c)(iii) | 20170 | fork | limb of the row above: `sch 10 para 8(2)(c)(iii) a body corporate in the same group as a partner` |  | F28 |  |
| sch 10 para 8(2)(c)(iv) | 20171 | fork | limb of the row above: `sch 10 para 8(2)(c)(iv) a director or controller of such another body corporate in the group of a partner` |  | F28 |  |
| sch 10 para 8(3) | 20172 | encoded | `sch 10 para 8(3) director is to be read as member in sub-paragraph (2)(b)` | 2 |  |  |
| sch 10 para 8(4) | 20173 | encoded | `sch 10 para 8(4) the person is a controller of the body corporate` | 4 |  |  |
| sch 10 cross-heading (line 20174) "Professional integrity and independence" | 20174 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 10 para 9(1) | 20175 | fork | `sch 10 para 9(1) the body meets the requirement` | 5 | F29 |  |
| sch 10 para 9(1)(a) | 20176 | fork | limb of the row above: `sch 10 para 9(1) the body meets the requirement` |  | F29 |  |
| sch 10 para 9(1)(b) | 20177 | fork | limb of the row above: `sch 10 para 9(1) the body meets the requirement` |  | F29 |  |
| sch 10 para 9(1)(c) | 20178 | fork | limb of the row above: `sch 10 para 9(1) the body meets the requirement` |  | F29 |  |
| sch 10 para 9(1)(d) | 20179 | fork | limb of the row above: `sch 10 para 9(1) the body meets the requirement` |  | F29 |  |
| sch 10 para 9(1)(e) | 20180 | repealed or blank in this text (reason 3) | - | - | F29 | the text shows only dots: nothing to encode |
| sch 10 para 9(1A) | 20181 | fork | `sch 10 para 9(1A) the rules of the body must bar the appointment`; `sch 10 para 9(1A) the bar on appointment is in force on the day` | 9 | F8, F30 |  |
| sch 10 para 9(1A)(a) | 20182 | fork | limb of the row above: `sch 10 para 9(1A) the rules of the body must bar the appointment` (+1) |  | F8, F30 |  |
| sch 10 para 9(1A)(b) | 20183 | fork | limb of the row above: `sch 10 para 9(1A) the rules of the body must bar the appointment` (+1) |  | F8, F30 |  |
| sch 10 para 9(2) | 20184 | repealed or blank in this text (reason 3) | - | - |  | the text shows only dots: nothing to encode |
| sch 10 para 9(3) | 20185 | encoded | `sch 10 para 9(3)(b) the body meets the requirement` | 2 |  |  |
| sch 10 para 9(3)(a) | 20186 | repealed or blank in this text (reason 3) | - | - |  | the text shows only dots: nothing to encode |
| sch 10 para 9(3)(b) | 20187 | fork | limb of the row above: `sch 10 para 9(3)(b) the body meets the requirement` |  | F31 |  |
| sch 10 para 9(3)(c) | 20188 | repealed or blank in this text (reason 3) | - | - |  | the text shows only dots: nothing to encode |
| sch 10 para 9(3A) | 20189 | fork | `sch 10 para 9(3A) the body meets the requirement` | 2 | F32 |  |
| sch 10 para 9(4) | 20190 | fork | `sch 10 para 9(4) the body meets the requirement that the rules apply to former members`; `sch 10 para 9(4) the fine is recoverable by the body as a debt due to it from the person obliged to pay it` | 4 | F33 |  |
| sch 10 para 9(5) | 20191 | encoded | `sch 10 para 9(5) the auditor is regarded as an officer of the audited person for the purposes of sub-paragraph (1A)(a) and (b)` | 2 |  |  |
| sch 10 cross-heading (line 20192) "Technical standards" | 20192 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 10 para 10(1) | 20193 | fork | `sch 10 para 10(1) the body meets the requirement` | 3 | F34 |  |
| sch 10 para 10(1)(a) | 20194 | fork | limb of the row above: `sch 10 para 10(1) the body meets the requirement` |  | F34 |  |
| sch 10 para 10(1)(b) | 20195 | fork | limb of the row above: `sch 10 para 10(1) the body meets the requirement` |  | F34 |  |
| sch 10 para 10(2) | 20196 | fork | `sch 10 para 10(2) the body meets the requirement` | 2 | F35 |  |
| sch 10 cross-heading (line 20197) "Technical standards for group audits" | 20197 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 10 para 10A(1) | 20198 | fork | `sch 10 para 10A(1) the body meets the requirement` | 3 | F36 |  |
| sch 10 para 10A(1)(a) | 20199 | fork | limb of the row above: `sch 10 para 10A(1) the body meets the requirement` |  | F36 |  |
| sch 10 para 10A(1)(b) | 20200 | fork | limb of the row above: `sch 10 para 10A(1) the body meets the requirement` |  | F36 |  |
| sch 10 para 10A(2) | 20201 | fork | `sch 10 para 10A(2) the body meets the requirement` | 2 | F37 |  |
| sch 10 para 10A(3) | 20202 | fork | `sch 10 para 10A(3) the body meets the requirement` | 2 | F38 |  |
| sch 10 para 10A(4) | 20203 | repealed or blank in this text (reason 3) | - | - |  | the text shows only dots: nothing to encode |
| sch 10 para 10A(5) | 20204 | repealed or blank in this text (reason 3) | - | - |  | the text shows only dots: nothing to encode |
| sch 10 para 10A(6) | 20205 | repealed or blank in this text (reason 3) | - | - |  | the text shows only dots: nothing to encode |
| sch 10 para 10A(7) | 20206 | encoded | `sch 10 para 10A(7) the person is a group auditor`; `sch 10 para 10A(7) the companies form a group` | 5 |  |  |
| sch 10 para 10A(7) term “group auditor” | 20207 | encoded | `sch 10 para 10A(7) the person is a group auditor` | 2 |  |  |
| sch 10 para 10A(7) term “group” | 20208 | encoded | `sch 10 para 10A(7) the companies form a group` | 3 |  |  |
| sch 10 cross-heading (line 20209) "Public interest entity reporting requirements" | 20209 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 10 para 10B | 20210 | repealed or blank in this text (reason 3) | - | - |  | the text shows only dots: nothing to encode |
| sch 10 cross-heading (line 20211) "Public interest entity independence requirements" | 20211 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 10 para 10C(1) | 20212 | repealed or blank in this text (reason 3) | - | - |  | the text shows only dots: nothing to encode |
| sch 10 para 10C(2) | 20213 | repealed or blank in this text (reason 3) | - | - |  | the text shows only dots: nothing to encode |
| sch 10 para 10C(3) | 20214 | fork | `sch 10 para 10C(3) the rules of the body must bar the appointment` | 7 | F8 |  |
| sch 10 para 10C(3)(a) | 20215 | fork | limb of the row above: `sch 10 para 10C(3) the rules of the body must bar the appointment` |  | F8 |  |
| sch 10 para 10C(3)(b) | 20216 | fork | limb of the row above: `sch 10 para 10C(3) the rules of the body must bar the appointment` |  | F8 |  |
| sch 10 para 10C(4) | 20217 | fork | `sch 10 para 10C(4) the body meets the requirement that the rules apply to former members`; `sch 10 para 10C(4) the fine is recoverable by the body as a debt due to it from the person obliged to pay it` | 4 | F39 |  |
| sch 10 para 10C(5) | 20218 | encoded | `sch 10 para 10C(5) the auditor is regarded as an officer of the entity for the purposes of sub-paragraph (3)(a) and (b)` | 2 |  |  |
| sch 10 para 10C(6) | 20219 | repealed or blank in this text (reason 3) | - | - |  | the text shows only dots: nothing to encode |
| sch 10 cross-heading (line 20220) "Procedures for maintaining competence" | 20220 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 10 para 11 | 20221 | fork | `sch 10 para 11 the body meets the requirement` | 2 | F40 |  |
| sch 10 cross-heading (line 20222) "Monitoring and enforcement" | 20222 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 10 para 12(1) | 20223 | fork | `sch 10 para 12(1) the body meets the requirement` | 3 | F41 |  |
| sch 10 para 12(1)(a) | 20224 | fork | limb of the row above: `sch 10 para 12(1) the body meets the requirement` |  | F41 |  |
| sch 10 para 12(1)(b) | 20225 | fork | limb of the row above: `sch 10 para 12(1) the body meets the requirement` |  | F41 |  |
| sch 10 para 12(1A) | 20226 | fork | `sch 10 para 12(1A) the body meets the requirement` | 3 | F42 |  |
| sch 10 para 12(1A)(a) | 20227 | fork | limb of the row above: `sch 10 para 12(1A) the body meets the requirement` |  | F42 |  |
| sch 10 para 12(1A)(b) | 20228 | fork | limb of the row above: `sch 10 para 12(1A) the body meets the requirement` |  | F42 |  |
| sch 10 para 12(2) | 20229 | fork | `sch 10 para 12(2) the body meets the requirement` | 2 | F43 |  |
| sch 10 para 12(3) | 20230 | encoded | `sch 10 para 12(3)(a) the body meets the requirement`; `sch 10 para 12(3)(b) the body meets the requirement`; `sch 10 para 12(3)(c) the body meets the requirement` | 14 |  |  |
| sch 10 para 12(3)(a) | 20231 | fork | limb of the row above: `sch 10 para 12(3)(a) the body meets the requirement` |  | F44 |  |
| sch 10 para 12(3)(b) | 20232 | fork | limb of the row above: `sch 10 para 12(3)(b) the body meets the requirement` |  | F45 |  |
| sch 10 para 12(3)(b)(i) | 20233 | fork | limb of the row above: `sch 10 para 12(3)(b) the body meets the requirement` |  | F45 |  |
| sch 10 para 12(3)(b)(ii) | 20234 | fork | limb of the row above: `sch 10 para 12(3)(b) the body meets the requirement` |  | F45 |  |
| sch 10 para 12(3)(b)(iii) | 20235 | fork | limb of the row above: `sch 10 para 12(3)(b) the body meets the requirement` |  | F45 |  |
| sch 10 para 12(3)(b)(iv) | 20236 | fork | limb of the row above: `sch 10 para 12(3)(b) the body meets the requirement` |  | F45 |  |
| sch 10 para 12(3)(b)(v) | 20237 | fork | limb of the row above: `sch 10 para 12(3)(b) the body meets the requirement` |  | F45 |  |
| sch 10 para 12(3)(b)(vi) | 20238 | fork | limb of the row above: `sch 10 para 12(3)(b) the body meets the requirement` |  | F45 |  |
| sch 10 para 12(3)(b)(vii) | 20239 | fork | limb of the row above: `sch 10 para 12(3)(b) the body meets the requirement` |  | F45 |  |
| sch 10 para 12(3)(b)(viii) | 20240 | fork | limb of the row above: `sch 10 para 12(3)(b) the body meets the requirement` |  | F45 |  |
| sch 10 para 12(3)(b)(ix) | 20241 | fork | limb of the row above: `sch 10 para 12(3)(b) the body meets the requirement` |  | F45 |  |
| sch 10 para 12(3)(c) | 20242 | fork | limb of the row above: `sch 10 para 12(3)(c) the body meets the requirement` |  | F46 |  |
| sch 10 para 12(4) | 20243 | fork | `sch 10 para 12(4) the body meets the requirement that the sanctions apply to former members`; `sch 10 para 12(4) the sanction applies to the person as it applies to members` | 5 | F47 |  |
| sch 10 para 12(5) | 20244 | encoded | `sch 10 para 12(5) the information made available to the public includes what it must include` | 6 |  |  |
| sch 10 para 12(5)(a) | 20245 | encoded | limb of the row above: `sch 10 para 12(5) the information made available to the public includes what it must include` |  |  |  |
| sch 10 para 12(5)(b) | 20246 | encoded | limb of the row above: `sch 10 para 12(5) the information made available to the public includes what it must include` |  |  |  |
| sch 10 para 12(5)(c) | 20247 | encoded | limb of the row above: `sch 10 para 12(5) the information made available to the public includes what it must include` |  |  |  |
| sch 10 para 12(6) | 20248 | fork | `sch 10 para 12(6) the identity of the person sanctioned must not be made available to the public` | 5 | F48 |  |
| sch 10 para 12(6)(a) | 20249 | fork | limb of the row above: `sch 10 para 12(6) the identity of the person sanctioned must not be made available to the public` |  | F48 |  |
| sch 10 para 12(6)(b) | 20250 | fork | limb of the row above: `sch 10 para 12(6) the identity of the person sanctioned must not be made available to the public` |  | F48 |  |
| sch 10 para 12(6)(c) | 20251 | fork | limb of the row above: `sch 10 para 12(6) the identity of the person sanctioned must not be made available to the public` |  | F48 |  |
| sch 10 para 12(6)(d) | 20252 | fork | limb of the row above: `sch 10 para 12(6) the identity of the person sanctioned must not be made available to the public` |  | F48 |  |
| sch 10 para 12(7) | 20253 | fork | `sch 10 para 12(7) the information must be published on the website of the body on the day` | 4 | F49 |  |
| sch 10 para 12(8) | 20254 | encoded | `sch 10 para 12(8) the relevant date` | 3 |  |  |
| sch 10 para 12(8)(a) | 20255 | encoded | limb of the row above: `sch 10 para 12(8) the relevant date` |  |  |  |
| sch 10 para 12(8)(b) | 20256 | encoded | limb of the row above: `sch 10 para 12(8) the relevant date` |  |  |  |
| sch 10 cross-heading (line 20257) "Monitoring of audits" | 20257 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 10 para 13(1) | 20258 | fork | `sch 10 para 13(1) the body meets the requirement` | 12 | F50 |  |
| sch 10 para 13(1)(a) | 20259 | fork | limb of the row above: `sch 10 para 13(1) the body meets the requirement` |  | F50 |  |
| sch 10 para 13(1)(b) | 20260 | fork | limb of the row above: `sch 10 para 13(1) the body meets the requirement` |  | F50 |  |
| sch 10 para 13(1)(b)(i) | 20261 | fork | limb of the row above: `sch 10 para 13(1) the body meets the requirement` |  | F50 |  |
| sch 10 para 13(1)(b)(ii) | 20262 | fork | limb of the row above: `sch 10 para 13(1) the body meets the requirement` |  | F50 |  |
| sch 10 para 13(1)(c) | 20263 | fork | limb of the row above: `sch 10 para 13(1) the body meets the requirement` |  | F50 |  |
| sch 10 para 13(1)(c)(i) | 20264 | fork | limb of the row above: `sch 10 para 13(1) the body meets the requirement` |  | F50 |  |
| sch 10 para 13(1)(c)(ii) | 20265 | fork | limb of the row above: `sch 10 para 13(1) the body meets the requirement` |  | F50 |  |
| sch 10 para 13(1)(d) | 20266 | fork | limb of the row above: `sch 10 para 13(1) the body meets the requirement` |  | F50 |  |
| sch 10 para 13(2) | 20267 | encoded | `sch 10 para 13(2) the monitoring is regarded as monitoring of compliance with the rules of the body for the purposes of paragraph 12(1) and (1A)` | 3 |  |  |
| sch 10 para 13(3) | 20268 | encoded | `sch 10 para 13(3)(a) the body meets the requirement`; `sch 10 para 13(3)(b)(i) the arrangements meet the requirement`; `sch 10 para 13(3)(b)(ii) another inspection of the person is due by the day asked about` | 9 |  |  |
| sch 10 para 13(3)(a) | 20269 | fork | limb of the row above: `sch 10 para 13(3)(a) the body meets the requirement` |  | F51 |  |
| sch 10 para 13(3)(b) | 20270 | encoded | limb of the row above: `sch 10 para 13(3)(b)(i) the arrangements meet the requirement` (+1) |  |  |  |
| sch 10 para 13(3)(b)(i) | 20271 | fork | limb of the row above: `sch 10 para 13(3)(b)(i) the arrangements meet the requirement` |  | F52 |  |
| sch 10 para 13(3)(b)(ii) | 20272 | fork | limb of the row above: `sch 10 para 13(3)(b)(ii) another inspection of the person is due by the day asked about` |  | F8, F53 |  |
| sch 10 para 13(4) | 20273 | encoded | `sch 10 para 13(4) the arrangements meet the requirement` | 2 |  |  |
| sch 10 para 13(5) | 20274 | fork | `sch 10 para 13(5) the inspector is a person by whom the inspection may be conducted` | 9 | F8 |  |
| sch 10 para 13(5)(a) | 20275 | fork | limb of the row above: `sch 10 para 13(5) the inspector is a person by whom the inspection may be conducted` |  | F8 |  |
| sch 10 para 13(5)(b) | 20276 | fork | limb of the row above: `sch 10 para 13(5) the inspector is a person by whom the inspection may be conducted` |  | F8 |  |
| sch 10 para 13(5)(b)(i) | 20277 | fork | limb of the row above: `sch 10 para 13(5) the inspector is a person by whom the inspection may be conducted` |  | F8 |  |
| sch 10 para 13(5)(b)(ii) | 20278 | fork | limb of the row above: `sch 10 para 13(5) the inspector is a person by whom the inspection may be conducted` |  | F8 |  |
| sch 10 para 13(5)(b)(iii) | 20279-20281 | fork | limb of the row above: `sch 10 para 13(5) the inspector is a person by whom the inspection may be conducted` |  | F8 |  |
| sch 10 para 13(5)(c) | 20282 | fork | limb of the row above: `sch 10 para 13(5) the inspector is a person by whom the inspection may be conducted` |  | F8 |  |
| sch 10 para 13(5)(d) | 20283 | fork | limb of the row above: `sch 10 para 13(5) the inspector is a person by whom the inspection may be conducted` |  | F8 |  |
| sch 10 para 13(5)(e) | 20284 | fork | limb of the row above: `sch 10 para 13(5) the inspector is a person by whom the inspection may be conducted` |  | F8, F54 |  |
| sch 10 para 13(6) | 20285 | encoded | `sch 10 para 13(6) the inspection meets the requirement` | 2 |  |  |
| sch 10 para 13(7) | 20286 | fork | `sch 10 para 13(7) the body meets the requirement` | 9 | F55 |  |
| sch 10 para 13(7)(a) | 20287 | fork | limb of the row above: `sch 10 para 13(7) the body meets the requirement` |  | F55 |  |
| sch 10 para 13(7)(b) | 20288 | fork | limb of the row above: `sch 10 para 13(7) the body meets the requirement` |  | F55 |  |
| sch 10 para 13(7)(c) | 20289 | fork | limb of the row above: `sch 10 para 13(7) the body meets the requirement` |  | F55 |  |
| sch 10 para 13(7)(d) | 20290 | fork | limb of the row above: `sch 10 para 13(7) the body meets the requirement` |  | F55 |  |
| sch 10 para 13(8) | 20291 | fork | `sch 10 para 13(8) the body meets the requirement` | 2 | F56 |  |
| sch 10 para 13(9) | 20292 | fork | `sch 10 para 13(9) the body has taken account of the proportionality of the standards` | 7 | F57 |  |
| sch 10 para 13(10) | 20293 | fork | `sch 10 para 13(10) the inspection of the firm may be treated as an inspection of all individuals responsible` | 3 | F58 |  |
| sch 10 para 13(11) | 20294 | fork | `sch 10 para 13(11) the body meets the requirement` | 4 | F59 |  |
| sch 10 para 13(11)(a) | 20295 | fork | limb of the row above: `sch 10 para 13(11) the body meets the requirement` |  | F59 |  |
| sch 10 para 13(11)(b) | 20296 | fork | limb of the row above: `sch 10 para 13(11) the body meets the requirement` |  | F59 |  |
| sch 10 para 13(12) | 20297 | fork | `sch 10 para 13(12) deliver to the Secretary of State a summary of the results of inspections`; `sch 10 para 13(12) the annual summary`; `sch 10 para 13(12) the body has complied for the calendar year` | 2 | F60 |  |
| sch 10 cross-heading (line 20298) "Membership, eligibility and enforcement" | 20298 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 10 para 14 | 20299 | fork | `sch 10 para 14 the body meets the requirement` | 6 | F61 |  |
| sch 10 para 14(a) | 20300 | fork | limb of the row above: `sch 10 para 14 the body meets the requirement` |  | F61 |  |
| sch 10 para 14(b) | 20301 | fork | limb of the row above: `sch 10 para 14 the body meets the requirement` |  | F61 |  |
| sch 10 para 14(c) | 20302-20303 | fork | limb of the row above: `sch 10 para 14 the body meets the requirement` |  | F61 |  |
| sch 10 cross-heading (line 20304) "Investigation of complaints" | 20304 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 10 para 15(1) | 20305 | fork | `sch 10 para 15(1) the body meets the requirement` | 3 | F62 |  |
| sch 10 para 15(1)(a) | 20306 | fork | limb of the row above: `sch 10 para 15(1) the body meets the requirement` |  | F62 |  |
| sch 10 para 15(1)(b) | 20307 | fork | limb of the row above: `sch 10 para 15(1) the body meets the requirement` |  | F62 |  |
| sch 10 para 15(2) | 20308 | fork | `sch 10 para 15(2) the body meets the requirement` | 2 | F63 |  |
| sch 10 cross-heading (line 20309) "Independent investigation for enforcement purposes" | 20309 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 10 para 16(1) | 20310 | fork | `sch 10 para 16(1) the body meets the requirement` | 3 | F64 |  |
| sch 10 para 16(2) | 20311 | fork | `sch 10 para 16(2) the body meets the requirement` | 4 | F65 |  |
| sch 10 para 16(2)(a) | 20312 | fork | limb of the row above: `sch 10 para 16(2) the body meets the requirement` |  | F65 |  |
| sch 10 para 16(2)(b) | 20313 | fork | limb of the row above: `sch 10 para 16(2) the body meets the requirement` |  | F65 |  |
| sch 10 para 16(2)(c) | 20314 | fork | limb of the row above: `sch 10 para 16(2) the body meets the requirement` |  | F65 |  |
| sch 10 para 16(3) | 20315 | encoded | `sch 10 para 16(3) the matter is a non-delegated case` | 2 |  |  |
| sch 10 cross-heading (line 20316) "Transfer of papers to third countries" | 20316 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 10 para 16A(1) | 20317 | fork | `sch 10 para 16A(1) the body meets the requirement`; `sch 10 para 16A(1) the person may transfer audit working papers and investigation reports to the third country competent authority` | 6 | F66, F67 |  |
| sch 10 para 16A(1)(a) | 20318 | fork | limb of the row above: `sch 10 para 16A(1) the body meets the requirement` (+1) |  | F66, F67 |  |
| sch 10 para 16A(1)(b) | 20319 | fork | limb of the row above: `sch 10 para 16A(1) the body meets the requirement` (+1) |  | F66, F67 |  |
| sch 10 para 16A(2) | 20320 | fork | `sch 10 para 16A(2) the person must refuse to transfer audit working papers and investigation reports to the third country competent authority`; `sch 10 para 16A(2) the body meets the requirement that the person must refuse` | 5 | F68 |  |
| sch 10 cross-heading (line 20321) "Transfer to approved third country competent authority" | 20321 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 10 para 16AA | 20322 | encoded | `sch 10 para 16AA the requirements of this paragraph are met` | 3 |  |  |
| sch 10 para 16AA(a) | 20323 | encoded | limb of the row above: `sch 10 para 16AA the requirements of this paragraph are met` |  |  |  |
| sch 10 para 16AA(b) | 20324 | encoded | limb of the row above: `sch 10 para 16AA the requirements of this paragraph are met` |  |  |  |
| sch 10 cross-heading (line 20325) "Transfer for purposes of investigation of auditor" | 20325 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 10 para 16AB(1) | 20326 | encoded | `sch 10 para 16AB the requirements of this paragraph are met` | 9 |  |  |
| sch 10 para 16AB(1)(a) | 20327 | encoded | limb of the row above: `sch 10 para 16AB the requirements of this paragraph are met` |  |  |  |
| sch 10 para 16AB(1)(b) | 20328 | encoded | limb of the row above: `sch 10 para 16AB the requirements of this paragraph are met` |  |  |  |
| sch 10 para 16AB(2) | 20329 | encoded | `sch 10 para 16AB the requirements of this paragraph are met` | 9 |  |  |
| sch 10 para 16AB(3) | 20330 | encoded | `sch 10 para 16AB the requirements of this paragraph are met` | 9 |  |  |
| sch 10 para 16AB(3)(a) | 20331 | encoded | limb of the row above: `sch 10 para 16AB the requirements of this paragraph are met` |  |  |  |
| sch 10 para 16AB(3)(b) | 20332 | encoded | limb of the row above: `sch 10 para 16AB the requirements of this paragraph are met` |  |  |  |
| sch 10 para 16AB(4) | 20333 | encoded | `sch 10 para 16AB the requirements of this paragraph are met` | 9 |  |  |
| sch 10 para 16AB(5) | 20334 | encoded | `sch 10 para 16AB the requirements of this paragraph are met` | 9 |  |  |
| sch 10 cross-heading (line 20335) "Meeting of claims arising out of audit work" | 20335 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 10 para 17(1) | 20336 | fork | `sch 10 para 17(1) the body meets the requirement` | 2 | F69 |  |
| sch 10 para 17(2) | 20337 | encoded | `sch 10 para 17(2) the person is able to meet claims arising out of statutory audit work` | 3 |  |  |
| sch 10 cross-heading (line 20338) "Register of auditors and other information to be made avail…" | 20338 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 10 para 18 | 20339 | fork | `sch 10 para 18 the body meets the requirement` | 4 | F70 |  |
| sch 10 para 18(a) | 20340 | fork | limb of the row above: `sch 10 para 18 the body meets the requirement` |  | F70 |  |
| sch 10 para 18(b) | 20341 | fork | limb of the row above: `sch 10 para 18 the body meets the requirement` |  | F70 |  |
| sch 10 para 18(c) | 20342 | fork | limb of the row above: `sch 10 para 18 the body meets the requirement` |  | F70 |  |
| sch 10 cross-heading (line 20343) "Taking account of costs of compliance" | 20343 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 10 para 19 | 20344 | fork | `sch 10 para 19 the body meets the requirement` | 2 | F71 |  |
| sch 10 cross-heading (line 20345) "Promotion and maintenance of standards" | 20345 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 10 para 20 | 20346 | fork | `sch 10 para 20 the body meets the requirement` | 3 | F72 |  |
| sch 10 para 20(a) | 20347 | fork | limb of the row above: `sch 10 para 20 the body meets the requirement` |  | F72 |  |
| sch 10 para 20(b) | 20348 | fork | limb of the row above: `sch 10 para 20 the body meets the requirement` |  | F72 |  |
| sch 10 cross-heading (line 20349) "Supplementary: funding of arrangements" | 20349 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 10 para 20ZA(1) | 20350 | fork | `sch 10 para 20ZA pay the costs incurred by the competent authority or another recognised supervisory body`; `sch 10 para 20ZA the duty to pay the costs`; `sch 10 para 20ZA the body has paid the costs it must pay` | 5 | F73 |  |
| sch 10 para 20ZA(2) | 20351 | fork | `sch 10 para 20ZA pay the costs incurred by the competent authority or another recognised supervisory body`; `sch 10 para 20ZA the duty to pay the costs`; `sch 10 para 20ZA the body has paid the costs it must pay` | 5 | F73 |  |
| sch 10 para 20ZA(2)(a) | 20352 | fork | limb of the row above: `sch 10 para 20ZA pay the costs incurred by the competent authority or another recognised supervisory body` (+2) |  | F73 |  |
| sch 10 para 20ZA(2)(b) | 20353-20354 | fork | limb of the row above: `sch 10 para 20ZA pay the costs incurred by the competent authority or another recognised supervisory body` (+2) |  | F73 |  |
| sch 10 cross-heading (line 20355) "Interpretation" | 20355 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 10 para 20A(1) | 20356 | encoded | `sch 10 para 20A(1) the instrument is the Audit Directive`; `sch 10 para 20A(1) the requirement is one of the audit reporting requirements`; `sch 10 para 20A(1) the person is an EEA auditor` (+8 more) | 34 |  |  |
| sch 10 para 20A(1) term “the Audit Directive” | 20357 | fork | `sch 10 para 20A(1) the instrument is the Audit Directive` | 2 | F74 |  |
| sch 10 para 20A(1) term “audit reporting requirements” | 20358 | fork | `sch 10 para 20A(1) the requirement is one of the audit reporting requirements` | 2 | F74 |  |
| sch 10 para 20A(1) term “EEA auditor” | 20359 | fork | `sch 10 para 20A(1) the person is an EEA auditor` | 4 | F74 |  |
| sch 10 para 20A(1) term “EEA competent authority” | 20360 | fork | `sch 10 para 20A(1) the body is an EEA competent authority` | 3 | F74 |  |
| sch 10 para 20A(1) term “issuer” | 20361 | fork | `sch 10 para 20A(1) the person is an issuer` | 2 | F74 |  |
| sch 10 para 20A(1) term “key audit partner” | 20362-20367 | fork | `sch 10 para 20A(1) the individual is a key audit partner` | 7 | F74 |  |
| sch 10 para 20A(1) term “public interest entity” | 20368-20371 | fork | `sch 10 para 20A(1) the person is a public interest entity` | 4 | F74 |  |
| sch 10 para 20A(1) term “specified state” | 20372 | fork | `sch 10 para 20A(1) the state is a specified state` | 2 | F74 |  |
| sch 10 para 20A(1) term “specified state auditor” | 20373 | fork | `sch 10 para 20A(1) the person is a specified state auditor` | 3 | F74 |  |
| sch 10 para 20A(1) omitted text, line 20374 | 20374 | repealed or blank in this text (reason 3) | - | - |  | the text shows only dots: nothing to encode |
| sch 10 para 20A(1) term “statutory audit function” | 20375 | fork | `sch 10 para 20A(1) the function is a statutory audit function` | 2 | F74 |  |
| sch 10 para 20A(1) term “third country audit function” | 20376 | fork | `sch 10 para 20A(1) the function is a third country audit function` | 3 | F74 |  |
| sch 10 para 20A(1) omitted text, line 20377 | 20377 | repealed or blank in this text (reason 3) | - | - |  | the text shows only dots: nothing to encode |
| sch 10 para 20A(2) | 20378 | encoded | `sch 10 para 20A(2) the territory is treated as an EEA State and subject to the Audit Directive for the purposes of this Schedule` | 2 |  |  |
| sch 10 part 3 heading | 20379 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 10 cross-heading (line 20380) "Arrangements for setting standards relating to professional…" | 20380 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 10 para 21 | 20381 | repealed or blank in this text (reason 3) | - | - |  | the text shows only dots: nothing to encode |
| sch 10 cross-heading (line 20382) "Arrangements for setting technical standards" | 20382 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 10 para 22 | 20383 | repealed or blank in this text (reason 3) | - | - |  | the text shows only dots: nothing to encode |
| sch 10 cross-heading (line 20384) "Arrangements for setting standards relating to public inter…" | 20384 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 10 para 22A | 20385 | repealed or blank in this text (reason 3) | - | - |  | the text shows only dots: nothing to encode |
| sch 10 cross-heading (line 20386) "Arrangements for setting standards relating to public inter…" | 20386 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 10 para 22B | 20387 | repealed or blank in this text (reason 3) | - | - |  | the text shows only dots: nothing to encode |
| sch 10 cross-heading (line 20388) "Arrangements for independent monitoring of audits of listed…" | 20388 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 10 para 23 | 20389 | repealed or blank in this text (reason 3) | - | - |  | the text shows only dots: nothing to encode |
| sch 10 cross-heading (line 20390) "Arrangements for independent monitoring of third country au…" | 20390 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 10 para 23A | 20391 | repealed or blank in this text (reason 3) | - | - |  | the text shows only dots: nothing to encode |
| sch 10 cross-heading (line 20392) "Arrangements for independent investigation for disciplinary…" | 20392 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 10 para 24 | 20393 | repealed or blank in this text (reason 3) | - | - |  | the text shows only dots: nothing to encode |
| sch 10 cross-heading (line 20394) "Supplementary: arrangements to operate independently of body" | 20394 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 10 para 25 | 20395 | repealed or blank in this text (reason 3) | - | - |  | the text shows only dots: nothing to encode |
| sch 10 cross-heading (line 20396) "Supplementary: funding of arrangements" | 20396 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 10 para 26 | 20397 | repealed or blank in this text (reason 3) | - | - |  | the text shows only dots: nothing to encode |
| sch 10 cross-heading (line 20398) "Supplementary: scope of arrangement" | 20398 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 10 para 27 | 20399 | repealed or blank in this text (reason 3) | - | - |  | the text shows only dots: nothing to encode |
| sch 11 heading | 20400 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 11 section reference | 20401 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 11 part 1 heading | 20402 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 11 cross-heading (line 20403) "Application for recognition of professional qualification" | 20403 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 11 para 1(1) | 20404 | encoded | `sch 11 para 1(1) the body may apply to the Secretary of State for a recognition order` | 3 |  |  |
| sch 11 para 1(2) | 20405 | encoded | `sch 11 para 1(2) the body is a recognised qualifying body` | 3 |  |  |
| sch 11 para 1(3) | 20406 | encoded | `sch 11 para 1(3) the application is made and accompanied as required` | 3 |  |  |
| sch 11 para 1(3)(a) | 20407 | encoded | limb of the row above: `sch 11 para 1(3) the application is made and accompanied as required` |  |  |  |
| sch 11 para 1(3)(b) | 20408 | encoded | limb of the row above: `sch 11 para 1(3) the application is made and accompanied as required` |  |  |  |
| sch 11 para 1(4) | 20409 | encoded | `sch 11 para 1(4) the Secretary of State may require the applicant to furnish additional information` | 3 |  |  |
| sch 11 para 1(5) | 20410 | encoded | `sch 11 para 1(5) the directions and requirements may differ as between different applications` | 3 |  |  |
| sch 11 para 1(6) | 20411 | encoded | `sch 11 para 1(6) the Secretary of State may specify the form or manner of verification` | 2 |  |  |
| sch 11 para 1(7) | 20412 | encoded | `sch 11 para 1(7) the verification required may include independent moderation of the examinations` | 2 |  |  |
| sch 11 para 1(8) | 20413 | encoded | `sch 11 para 1(8) the application is accompanied as required` | 4 |  |  |
| sch 11 para 1(8)(a) | 20414 | encoded | limb of the row above: `sch 11 para 1(8) the application is accompanied as required` |  |  |  |
| sch 11 para 1(8)(b) | 20415 | encoded | limb of the row above: `sch 11 para 1(8) the application is accompanied as required` |  |  |  |
| sch 11 para 1(9) | 20416 | encoded | `sch 11 para 1(9) the guidance is guidance issued by the applicant` | 4 |  |  |
| sch 11 para 1(9)(a) | 20417 | encoded | limb of the row above: `sch 11 para 1(9) the guidance is guidance issued by the applicant` |  |  |  |
| sch 11 para 1(9)(b) | 20418 | encoded | limb of the row above: `sch 11 para 1(9) the guidance is guidance issued by the applicant` |  |  |  |
| sch 11 para 1(9)(c) | 20419-20420 | encoded | limb of the row above: `sch 11 para 1(9) the guidance is guidance issued by the applicant` |  |  |  |
| sch 11 para 1(10) | 20421 | encoded | `sch 11 para 1(10) the matter is within this sub-paragraph` | 5 |  |  |
| sch 11 para 1(10)(a) | 20422 | encoded | limb of the row above: `sch 11 para 1(10) the matter is within this sub-paragraph` |  |  |  |
| sch 11 para 1(10)(b) | 20423 | encoded | limb of the row above: `sch 11 para 1(10) the matter is within this sub-paragraph` |  |  |  |
| sch 11 para 1(10)(c) | 20424-20425 | encoded | limb of the row above: `sch 11 para 1(10) the matter is within this sub-paragraph` |  |  |  |
| sch 11 cross-heading (line 20426) "Grant and refusal of recognition" | 20426 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 11 para 2(1) | 20427 | encoded | `sch 11 para 2(1) the Secretary of State may make or refuse to make a recognition order` | 3 |  |  |
| sch 11 para 2(2) | 20428 | encoded | `sch 11 para 2(2) the Secretary of State may make a recognition order` | 2 |  |  |
| sch 11 para 2(3) | 20429 | encoded | `sch 11 para 2(3) the notice of refusal is given as required` | 3 |  |  |
| sch 11 para 2(4) | 20430 | encoded | `sch 11 para 2(4) the recognition order is made as required` | 2 |  |  |
| sch 11 cross-heading (line 20431) "Revocation of recognition" | 20431 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 11 para 3(1) | 20432 | fork | `sch 11 para 3(1) the Secretary of State may revoke the recognition order` | 3 | F75 |  |
| sch 11 para 3(1)(a) | 20433 | fork | limb of the row above: `sch 11 para 3(1) the Secretary of State may revoke the recognition order` |  | F75 |  |
| sch 11 para 3(1)(b) | 20434 | fork | limb of the row above: `sch 11 para 3(1) the Secretary of State may revoke the recognition order` |  | F75 |  |
| sch 11 para 3(2) | 20435 | fork | `sch 11 para 3(2) the revocation order states a valid date of effect` | 3 | F8 |  |
| sch 11 para 3(3) | 20436 | encoded | `sch 11 para 3(3) the Secretary of State has done what he must do before revoking` | 4 |  |  |
| sch 11 para 3(3)(a) | 20437 | encoded | limb of the row above: `sch 11 para 3(3) the Secretary of State has done what he must do before revoking` |  |  |  |
| sch 11 para 3(3)(b) | 20438 | encoded | limb of the row above: `sch 11 para 3(3) the Secretary of State has done what he must do before revoking` |  |  |  |
| sch 11 para 3(3)(c) | 20439 | encoded | limb of the row above: `sch 11 para 3(3) the Secretary of State has done what he must do before revoking` |  |  |  |
| sch 11 para 3(4) | 20440 | encoded | `sch 11 para 3(4) the notice has the contents required` | 3 |  |  |
| sch 11 para 3(4)(a) | 20441 | encoded | limb of the row above: `sch 11 para 3(4) the notice has the contents required` |  |  |  |
| sch 11 para 3(4)(b) | 20442 | encoded | limb of the row above: `sch 11 para 3(4) the notice has the contents required` |  |  |  |
| sch 11 para 3(5) | 20443 | fork | `sch 11 para 3(5) the person may make written and oral representations` | 6 | F8, F10, F76 |  |
| sch 11 para 3(6) | 20444 | fork | `sch 11 para 3(6) the person is within this sub-paragraph` | 4 | F76 |  |
| sch 11 para 3(6)(a) | 20445 | fork | limb of the row above: `sch 11 para 3(6) the person is within this sub-paragraph` |  | F76 |  |
| sch 11 para 3(6)(b) | 20446 | fork | limb of the row above: `sch 11 para 3(6) the person is within this sub-paragraph` |  | F76 |  |
| sch 11 para 3(6)(c) | 20447 | fork | limb of the row above: `sch 11 para 3(6) the person is within this sub-paragraph` |  | F76 |  |
| sch 11 para 3(7) | 20448 | encoded | `sch 11 para 3(7) the Secretary of State has had regard to the representations` | 3 |  |  |
| sch 11 para 3(8) | 20449 | fork | `sch 11 para 3(8) the Secretary of State may revoke without regard to the restriction in sub-paragraph (2)` | 2 | F77 |  |
| sch 11 para 3(8)(a) | 20450 | fork | limb of the row above: `sch 11 para 3(8) the Secretary of State may revoke without regard to the restriction in sub-paragraph (2)` |  | F77 |  |
| sch 11 para 3(8)(b) | 20451 | fork | limb of the row above: `sch 11 para 3(8) the Secretary of State may revoke without regard to the restriction in sub-paragraph (2)` |  | F77 |  |
| sch 11 para 3(9) | 20452 | encoded | `sch 11 para 3(9) the revocation order may contain the transitional provision` | 2 |  |  |
| sch 11 para 3(10) | 20453 | encoded | `sch 11 para 3(10) the revocation is not subject to the restrictions and requirements listed` | 2 |  |  |
| sch 11 para 3(10)(a) | 20454 | encoded | limb of the row above: `sch 11 para 3(10) the revocation is not subject to the restrictions and requirements listed` |  |  |  |
| sch 11 para 3(10)(b) | 20455 | encoded | limb of the row above: `sch 11 para 3(10) the revocation is not subject to the restrictions and requirements listed` |  |  |  |
| sch 11 para 3(11) | 20456 | encoded | `sch 11 para 3(11) the Secretary of State has done what he must do on making the revocation order` | 4 |  |  |
| sch 11 para 3(11)(a) | 20457 | encoded | limb of the row above: `sch 11 para 3(11) the Secretary of State has done what he must do on making the revocation order` |  |  |  |
| sch 11 para 3(11)(b) | 20458 | encoded | limb of the row above: `sch 11 para 3(11) the Secretary of State has done what he must do on making the revocation order` |  |  |  |
| sch 11 para 3(11)(c) | 20459 | encoded | limb of the row above: `sch 11 para 3(11) the Secretary of State has done what he must do on making the revocation order` |  |  |  |
| sch 11 cross-heading (line 20460) "Transitional provision" | 20460 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 11 para 4 | 20461 | fork | `sch 11 para 4 the order has effect after commencement as an order made under paragraph 2(1) of this Schedule` | 3 | F14 |  |
| sch 11 para 4(a) | 20462 | fork | limb of the row above: `sch 11 para 4 the order has effect after commencement as an order made under paragraph 2(1) of this Schedule` |  | F14 |  |
| sch 11 para 4(b) | 20463-20464 | fork | limb of the row above: `sch 11 para 4 the order has effect after commencement as an order made under paragraph 2(1) of this Schedule` |  | F14 |  |
| sch 11 cross-heading (line 20465) "Orders not statutory instruments" | 20465 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 11 para 5 | 20466 | encoded | `sch 11 para 5 the order is to be made by statutory instrument` | 2 |  |  |
| sch 11 part 2 heading | 20467 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 11 cross-heading (line 20468) "Entry requirements" | 20468 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 11 para 6(1) | 20469 | encoded | `sch 11 para 6(1) the qualification may be open to the person` | 5 |  |  |
| sch 11 para 6(1)(a) | 20470 | encoded | limb of the row above: `sch 11 para 6(1) the qualification may be open to the person` |  |  |  |
| sch 11 para 6(1)(b) | 20471 | encoded | limb of the row above: `sch 11 para 6(1) the qualification may be open to the person` |  |  |  |
| sch 11 para 6(2) | 20472 | encoded | `sch 11 para 6(2) the person has attained university entrance level` | 5 |  |  |
| sch 11 para 6(2)(a) | 20473 | encoded | limb of the row above: `sch 11 para 6(2) the person has attained university entrance level` |  |  |  |
| sch 11 para 6(2)(a)(i) | 20474 | encoded | limb of the row above: `sch 11 para 6(2) the person has attained university entrance level` |  |  |  |
| sch 11 para 6(2)(a)(ii) | 20475 | encoded | limb of the row above: `sch 11 para 6(2) the person has attained university entrance level` |  |  |  |
| sch 11 para 6(2)(b) | 20476 | encoded | limb of the row above: `sch 11 para 6(2) the person has attained university entrance level` |  |  |  |
| sch 11 para 6(3) | 20477 | encoded | `sch 11 para 6(3) the assessment may be conducted by the body` | 3 |  |  |
| sch 11 para 6(3)(a) | 20478 | encoded | limb of the row above: `sch 11 para 6(3) the assessment may be conducted by the body` |  |  |  |
| sch 11 para 6(3)(b) | 20479 | encoded | limb of the row above: `sch 11 para 6(3) the assessment may be conducted by the body` |  |  |  |
| sch 11 para 6(4) | 20480 | fork | `sch 11 para 6(4) the person has a sufficient period of professional experience` | 3 | F78 |  |
| sch 11 cross-heading (line 20481) "Requirement for theoretical instruction or professional exp…" | 20481 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 11 para 7(1) | 20482 | encoded | `sch 11 para 7 the qualification may be restricted to the person` | 3 |  |  |
| sch 11 para 7(1)(a) | 20483 | encoded | limb of the row above: `sch 11 para 7 the qualification may be restricted to the person` |  |  |  |
| sch 11 para 7(1)(b) | 20484 | encoded | limb of the row above: `sch 11 para 7 the qualification may be restricted to the person` |  |  |  |
| sch 11 para 7(2) | 20485 | fork | `sch 11 para 7 the qualification may be restricted to the person` | 3 | F78 |  |
| sch 11 cross-heading (line 20486) "Examination" | 20486 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 11 para 8(1) | 20487 | encoded | `sch 11 para 8(1) the examination is of the kind the qualification must require` | 5 |  |  |
| sch 11 para 8(1)(a) | 20488 | encoded | limb of the row above: `sch 11 para 8(1) the examination is of the kind the qualification must require` |  |  |  |
| sch 11 para 8(1)(b) | 20489-20490 | encoded | limb of the row above: `sch 11 para 8(1) the examination is of the kind the qualification must require` |  |  |  |
| sch 11 para 8(2) | 20491 | encoded | `sch 11 para 8(2) the qualification may be awarded without the theoretical knowledge of the subject being tested by examination` | 3 |  |  |
| sch 11 para 8(3) | 20492 | encoded | `sch 11 para 8(3) the qualification may be awarded without the ability to apply the theoretical knowledge of the subject in practice being tested by examination` | 2 |  |  |
| sch 11 para 8(4) | 20493 | inert (reason 2) | - | - |  | regulation-making: regulations under paragraph 8 are subject to negative resolution procedure |
| sch 11 cross-heading (line 20494) "Practical training" | 20494 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 11 para 9(1) | 20495 | encoded | `sch 11 para 9(1) the practical training meets the requirement` | 4 |  |  |
| sch 11 para 9(1)(a) | 20496 | encoded | limb of the row above: `sch 11 para 9(1) the practical training meets the requirement` |  |  |  |
| sch 11 para 9(1)(b) | 20497 | encoded | limb of the row above: `sch 11 para 9(1) the practical training meets the requirement` |  |  |  |
| sch 11 para 9(2) | 20498 | fork | `sch 11 para 9(2) the work is statutory audit work` | 4 | F79 |  |
| sch 11 para 9(3) | 20499 | encoded | `sch 11 para 9(3) the training is given as required` | 2 |  |  |
| sch 11 para 9(4) | 20500 | fork | `sch 11 para 9(4) at least two-thirds of the training is given by a person of the kind required` | 4 | F80 |  |
| sch 11 para 9(4)(a) | 20501 | fork | limb of the row above: `sch 11 para 9(4) at least two-thirds of the training is given by a person of the kind required` |  | F80 |  |
| sch 11 para 9(4)(b) | 20502 | fork | limb of the row above: `sch 11 para 9(4) at least two-thirds of the training is given by a person of the kind required` |  | F80 |  |
| sch 11 para 9(4A) | 20503 | encoded | `sch 11 para 9(4A) the conditions are met in relation to the person` | 4 |  |  |
| sch 11 para 9(4A)(a) | 20504 | encoded | limb of the row above: `sch 11 para 9(4A) the conditions are met in relation to the person` |  |  |  |
| sch 11 para 9(4A)(b) | 20505 | encoded | limb of the row above: `sch 11 para 9(4A) the conditions are met in relation to the person` |  |  |  |
| sch 11 para 9(4A)(c) | 20506 | encoded | limb of the row above: `sch 11 para 9(4A) the conditions are met in relation to the person` |  |  |  |
| sch 11 para 9(5) | 20507 | repealed or blank in this text (reason 3) | - | - |  | the text shows only dots: nothing to encode |
| sch 11 cross-heading (line 20508) "Supplementary provision with respect to a sufficient period…" | 20508 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 11 para 10(1) | 20509 | fork | `sch 11 para 10(1) the years of professional experience required after the deduction` | 7 | F81 |  |
| sch 11 para 10(1)(a) | 20510 | fork | limb of the row above: `sch 11 para 10(1) the years of professional experience required after the deduction` |  | F81 |  |
| sch 11 para 10(1)(b) | 20511-20512 | fork | limb of the row above: `sch 11 para 10(1) the years of professional experience required after the deduction` |  | F81 |  |
| sch 11 para 10(2) | 20513 | encoded | `sch 11 para 10(2) the experience route is not shorter than the course route` | 3 |  |  |
| sch 11 cross-heading (line 20514) "The body offering the qualification" | 20514 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 11 para 11(1) | 20515 | fork | `sch 11 para 11(1) the body meets the requirement` | 3 | F82 |  |
| sch 11 para 11(1)(a) | 20516 | fork | limb of the row above: `sch 11 para 11(1) the body meets the requirement` |  | F82 |  |
| sch 11 para 11(1)(b) | 20517 | fork | limb of the row above: `sch 11 para 11(1) the body meets the requirement` |  | F82 |  |
| sch 11 para 11(2) | 20518 | fork | `sch 11 para 11(2) the arrangements meet the requirement` | 3 | F83 |  |
| sch 11 para 11(2)(a) | 20519 | fork | limb of the row above: `sch 11 para 11(2) the arrangements meet the requirement` |  | F83 |  |
| sch 11 para 11(2)(b) | 20520 | fork | limb of the row above: `sch 11 para 11(2) the arrangements meet the requirement` |  | F83 |  |
| sch 11A heading | 20521 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 11A part 1 heading | 20522 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 11A para 1 | 20523 | fork | `sch 11A para 1 the Secretary of State`; `sch 11A part 1 the person is a specified person` | 1 | F84 |  |
| sch 11A para 2 | 20524 | fork | `sch 11A para 2 the Department of Enterprise, Trade and Investment for Northern Ireland`; `sch 11A part 1 the person is a specified person` | 1 | F84 |  |
| sch 11A para 3 | 20525 | fork | `sch 11A para 3 the Treasury`; `sch 11A part 1 the person is a specified person` | 1 | F84 |  |
| sch 11A para 4 | 20526 | fork | `sch 11A para 4 the Bank of England`; `sch 11A part 1 the person is a specified person` | 1 | F84 |  |
| sch 11A para 5 | 20527 | fork | `sch 11A para 5 the Financial Conduct Authority`; `sch 11A part 1 the person is a specified person` | 2 | F84 |  |
| sch 11A para 5A | 20528 | fork | `sch 11A para 5A the Prudential Regulation Authority`; `sch 11A part 1 the person is a specified person` | 1 | F84 |  |
| sch 11A para 6 | 20529 | fork | `sch 11A para 6 the Commissioners for Revenue and Customs`; `sch 11A part 1 the person is a specified person` | 1 | F84 |  |
| sch 11A para 7 | 20530 | fork | `sch 11A para 7 the Lord Advocate`; `sch 11A part 1 the person is a specified person` | 1 | F84 |  |
| sch 11A para 8 | 20531 | fork | `sch 11A para 8 the Director of Public Prosecutions`; `sch 11A part 1 the person is a specified person` | 1 | F84 |  |
| sch 11A para 9 | 20532 | fork | `sch 11A para 9 the Director of Public Prosecutions for Northern Ireland`; `sch 11A part 1 the person is a specified person` | 1 | F84 |  |
| sch 11A para 10 | 20533 | fork | `sch 11A para 10 a constable`; `sch 11A part 1 the person is a specified person` | 1 | F84 |  |
| sch 11A para 11 | 20534 | fork | `sch 11A para 11 a procurator fiscal`; `sch 11A part 1 the person is a specified person` | 1 | F84 |  |
| sch 11A para 12 | 20535 | fork | `sch 11A para 12 the Scottish Ministers`; `sch 11A part 1 the person is a specified person` | 1 | F84 |  |
| sch 11A para 13 | 20536 | fork | `sch 11A para 13 a body designated by the Secretary of State under section 1252`; `sch 11A part 1 the person is a specified person` | 1 | F84 |  |
| sch 11A para 14 | 20537 | fork | `sch 11A para 14 a recognised supervisory body`; `sch 11A part 1 the person is a specified person` | 2 | F84 |  |
| sch 11A para 15 | 20538 | fork | `sch 11A para 15 a recognised qualifying body`; `sch 11A part 1 the person is a specified person` | 1 | F84 |  |
| sch 11A para 16 | 20539 | fork | `sch 11A para 16 the competent authority`; `sch 11A part 1 the person is a specified person` | 1 | F84 |  |
| sch 11A para 17 | 20540 | fork | `sch 11A para 17 the Independent Supervisor`; `sch 11A part 1 the person is a specified person` | 1 | F84 |  |
| sch 11A para 17A | 20541 | fork | `sch 11A para 17A a recognised supervisory body as defined in section 1217(4) and Schedule 10 as they have effect by virtue of Schedule 5 to the Local Audit and Accountability Act 2014`; `sch 11A part 1 the person is a specified person` | 1 | F84 |  |
| sch 11A para 17B | 20542 | fork | `sch 11A para 17B a recognised qualifying body as defined in section 1219(13) as it has effect by virtue of that Schedule`; `sch 11A part 1 the person is a specified person` | 1 | F84 |  |
| sch 11A para 17C | 20543 | fork | `sch 11A para 17C a body designated by the Secretary of State under section 1252 as it has effect by virtue of that Schedule`; `sch 11A part 1 the person is a specified person` | 1 | F84 |  |
| sch 11A para 17D | 20544 | fork | `sch 11A para 17D a body participating with a recognised supervisory body within the meaning of that Act in arrangements for the purposes of paragraph 23 or 24 of Schedule 10 as it has effect by virtue of that Schedule`; `sch 11A part 1 the person is a specified person` | 1 | F84 |  |
| sch 11A part 2 heading | 20545 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 11A para 18 | 20546 | fork | `sch 11A para 18 enabling or assisting a person authorised under section 457 of this Act to exercise his functions`; `sch 11A part 2 the disclosure is of a specified description` | 1 | F84 |  |
| sch 11A para 19 | 20547 | fork | `sch 11A para 19 enabling or assisting an inspector appointed under Part 14 of the Companies Act 1985 to exercise his functions`; `sch 11A part 2 the disclosure is of a specified description` | 1 | F84 |  |
| sch 11A para 20 | 20548 | fork | `sch 11A para 20 enabling or assisting a person authorised under section 447 of the Companies Act 1985 or section 84 of the Companies Act 1989 to exercise his functions`; `sch 11A part 2 the disclosure is of a specified description` | 1 | F84 |  |
| sch 11A para 21 | 20549 | fork | `sch 11A para 21 enabling or assisting a person appointed under section 167 of the Financial Services and Markets Act 2000 (general investigations)`; `sch 11A part 2 the disclosure is of a specified description` | 1 | F84 |  |
| sch 11A para 22 | 20550 | fork | `sch 11A para 22 enabling or assisting a person appointed under section 168 of the Financial Services and Markets Act 2000 (investigations in particular cases)`; `sch 11A part 2 the disclosure is of a specified description` | 1 | F84 |  |
| sch 11A para 23 | 20551 | fork | `sch 11A para 23 enabling or assisting a person appointed under section 169(1)(b) of the Financial Services and Markets Act 2000 (investigation in support of overseas regulator)`; `sch 11A part 2 the disclosure is of a specified description` | 1 | F84 |  |
| sch 11A para 24 | 20552 | fork | `sch 11A para 24 enabling or assisting the body corporate administering the ombudsman scheme under section 225 of the Financial Services and Markets Act 2000`; `sch 11A part 2 the disclosure is of a specified description` | 1 | F84 |  |
| sch 11A para 25 | 20553 | fork | `sch 11A para 25 enabling or assisting a person appointed under paragraph 4 or 5 of Schedule 17 to the Financial Services and Markets Act 2000`; `sch 11A part 2 the disclosure is of a specified description` | 1 | F84 |  |
| sch 11A para 26 | 20554 | fork | `sch 11A para 26 enabling or assisting a person appointed under regulations made under section 262(1) and (2)(k) of the Financial Services and Markets Act 2000`; `sch 11A part 2 the disclosure is of a specified description` | 1 | F84 |  |
| sch 11A para 27 | 20555 | fork | `sch 11A para 27 enabling or assisting a person appointed under section 284 of the Financial Services and Markets Act 2000`; `sch 11A part 2 the disclosure is of a specified description` | 1 | F84 |  |
| sch 11A para 28 | 20556 | fork | `sch 11A para 28 enabling or assisting the investigator appointed under section 84 of the Financial Services Act 2012`; `sch 11A part 2 the disclosure is of a specified description` | 1 | F84 |  |
| sch 11A para 29 | 20557 | fork | `sch 11A para 29 enabling or assisting a person appointed by the Treasury to hold an inquiry into matters relating to financial services`; `sch 11A part 2 the disclosure is of a specified description` | 1 | F84 |  |
| sch 11A para 30 | 20558 | fork | `sch 11A part 2 the disclosure is of a specified description` | 89 | F84 |  |
| sch 11A para 30(a) | 20559 | fork | limb of the row above: `sch 11A para 30(a) enabling or assisting the Secretary of State or the Treasury to exercise functions under the Companies Acts` (+1) |  | F84 |  |
| sch 11A para 30(b) | 20560 | fork | limb of the row above: `sch 11A para 30(b) enabling or assisting the Secretary of State or the Treasury to exercise functions under Part 5 of the Criminal Justice Act 1993 (insider dealing)` (+1) |  | F84 |  |
| sch 11A para 30(c) | 20561 | fork | limb of the row above: `sch 11A para 30(c) enabling or assisting the Secretary of State or the Treasury to exercise functions under the Insolvency Act 1986` (+1) |  | F84 |  |
| sch 11A para 30(d) | 20562 | fork | limb of the row above: `sch 11A para 30(d) enabling or assisting the Secretary of State or the Treasury to exercise functions under the Company Directors Disqualification Act 1986` (+1) |  | F84 |  |
| sch 11A para 30(e) | 20563 | fork | limb of the row above: `sch 11A para 30(e) enabling or assisting the Secretary of State or the Treasury to exercise functions under Part 42 of this Act (statutory auditors)` (+1) |  | F84 |  |
| sch 11A para 30(f) | 20564 | fork | limb of the row above: `sch 11A para 30(f) enabling or assisting the Secretary of State or the Treasury to exercise functions under Part 3 or 7 of the Companies Act 1989` (+1) |  | F84 |  |
| sch 11A para 30(g) | 20565 | fork | limb of the row above: `sch 11A para 30(g) enabling or assisting the Secretary of State or the Treasury to exercise functions under the Financial Services and Markets Act 2000` (+1) |  | F84 |  |
| sch 11A para 31 | 20566 | fork | `sch 11A para 31 enabling or assisting the Scottish Ministers to exercise their functions under the enactments relating to insolvency`; `sch 11A part 2 the disclosure is of a specified description` | 1 | F84 |  |
| sch 11A para 32 | 20567 | fork | `sch 11A para 32 enabling or assisting the Department of Enterprise, Trade and Investment for Northern Ireland to exercise powers under the enactments relating to companies or insolvency`; `sch 11A part 2 the disclosure is of a specified description` | 1 | F84 |  |
| sch 11A para 33 | 20568 | fork | `sch 11A para 33 enabling or assisting a person appointed or authorised by the Department of Enterprise, Trade and Investment for Northern Ireland to exercise his functions`; `sch 11A part 2 the disclosure is of a specified description` | 1 | F84 |  |
| sch 11A para 34 | 20569 | fork | `sch 11A part 2 the disclosure is of a specified description` | 89 | F84 |  |
| sch 11A para 34(a) | 20570 | fork | limb of the row above: `sch 11A para 34(a) enabling or assisting the Pensions Regulator to exercise functions under the Pension Schemes Act 1993` (+1) |  | F84 |  |
| sch 11A para 34(b) | 20571 | fork | limb of the row above: `sch 11A para 34(b) enabling or assisting the Pensions Regulator to exercise functions under the Pensions Act 1995` (+1) |  | F84 |  |
| sch 11A para 34(c) | 20572 | fork | limb of the row above: `sch 11A para 34(c) enabling or assisting the Pensions Regulator to exercise functions under the Welfare Reform and Pensions Act 1999` (+1) |  | F84 |  |
| sch 11A para 34(d) | 20573 | fork | limb of the row above: `sch 11A para 34(d) enabling or assisting the Pensions Regulator to exercise functions under the Pensions Act 2004` (+1) |  | F84 |  |
| sch 11A para 34(e) | 20574 | fork | limb of the row above: `sch 11A para 34(e) enabling or assisting the Pensions Regulator to exercise functions under a corresponding enactment in force in Northern Ireland` (+1) |  | F84 |  |
| sch 11A para 35 | 20575 | fork | `sch 11A para 35 enabling or assisting the Board of the Pension Protection Fund to exercise its functions`; `sch 11A part 2 the disclosure is of a specified description` | 1 | F84 |  |
| sch 11A para 36 | 20576 | fork | `sch 11A part 2 the disclosure is of a specified description` | 89 | F84 |  |
| sch 11A para 36(a) | 20577 | fork | limb of the row above: `sch 11A para 36(a) enabling or assisting the Bank of England to exercise its functions` (+1) |  | F84 |  |
| sch 11A para 36(b) | 20578 | fork | limb of the row above: `sch 11A para 36(b) enabling or assisting the European Central Bank to exercise its functions` (+1) |  | F84 |  |
| sch 11A para 36(c) | 20579 | fork | limb of the row above: `sch 11A para 36(c) enabling or assisting the central bank of a country or territory outside the United Kingdom to exercise its functions` (+1) |  | F84 |  |
| sch 11A para 37 | 20580 | fork | `sch 11A para 37 enabling or assisting the Commissioners for Revenue and Customs to exercise their functions`; `sch 11A part 2 the disclosure is of a specified description` | 1 | F84 |  |
| sch 11A para 38 | 20581 | fork | `sch 11A para 38 enabling or assisting organs of the Society of Lloyds to exercise their functions`; `sch 11A part 2 the disclosure is of a specified description` | 1 | F84 |  |
| sch 11A para 39 | 20582 | fork | `sch 11A part 2 the disclosure is of a specified description` | 89 | F84 |  |
| sch 11A para 39(a) | 20583 | fork | limb of the row above: `sch 11A para 39(a) enabling or assisting the Competition and Markets Authority to exercise functions under the Fair Trading Act 1973` (+1) |  | F84 |  |
| sch 11A para 39(b) | 20584 | repealed or blank in this text (reason 3) | - | - | F84 | the text shows only dots: nothing to encode |
| sch 11A para 39(c) | 20585 | repealed or blank in this text (reason 3) | - | - | F84 | the text shows only dots: nothing to encode |
| sch 11A para 39(d) | 20586 | fork | limb of the row above: `sch 11A para 39(d) enabling or assisting the Competition and Markets Authority to exercise functions under the Competition Act 1980` (+1) |  | F84 |  |
| sch 11A para 39(e) | 20587 | fork | limb of the row above: `sch 11A para 39(e) enabling or assisting the Competition and Markets Authority to exercise functions under the Competition Act 1998` (+1) |  | F84 |  |
| sch 11A para 39(f) | 20588 | fork | limb of the row above: `sch 11A para 39(f) enabling or assisting the Competition and Markets Authority to exercise functions under the Financial Services and Markets Act 2000` (+1) |  | F84 |  |
| sch 11A para 39(g) | 20589 | fork | limb of the row above: `sch 11A para 39(g) enabling or assisting the Competition and Markets Authority to exercise functions under the Enterprise Act 2002` (+1) |  | F84 |  |
| sch 11A para 39(h) | 20590 | fork | limb of the row above: `sch 11A para 39(h) enabling or assisting the Competition and Markets Authority to exercise functions under the Control of Misleading Advertisements Regulations 1988` (+1) |  | F84 |  |
| sch 11A para 39(i) | 20591 | fork | limb of the row above: `sch 11A para 39(i) enabling or assisting the Competition and Markets Authority to exercise functions under Schedule 3 to the Consumer Rights Act 2015` (+1) |  | F84 |  |
| sch 11A para 39(j) | 20592 | fork | limb of the row above: `sch 11A para 39(j) enabling or assisting the Competition and Markets Authority to exercise functions under Parts 3 and 4 of the Enterprise and Regulatory Reform Act 2013` (+1) |  | F84 |  |
| sch 11A para 40 | 20593 | repealed or blank in this text (reason 3) | - | - | F84 | the text shows only dots: nothing to encode |
| sch 11A para 41 | 20594 | fork | `sch 11A para 41 with a view to the institution of, or for the purposes of, proceedings before the Competition Appeal Tribunal`; `sch 11A part 2 the disclosure is of a specified description` | 1 | F84 |  |
| sch 11A para 42 | 20595 | fork | `sch 11A para 42 enabling or assisting an enforcer under Chapter 3 or 4 of Part 3 of the Digital Markets, Competition and Consumers Act 2024`; `sch 11A part 2 the disclosure is of a specified description` | 1 | F84 |  |
| sch 11A para 43 | 20596 | fork | `sch 11A para 43 enabling or assisting the Takeover Panel to perform its functions under Part 28 of this Act`; `sch 11A part 2 the disclosure is of a specified description` | 1 | F84 |  |
| sch 11A para 44 | 20597 | fork | `sch 11A para 44 enabling or assisting the Charity Commission to exercise its functions`; `sch 11A part 2 the disclosure is of a specified description` | 1 | F84 |  |
| sch 11A para 45 | 20598 | fork | `sch 11A para 45 enabling or assisting the Attorney General to exercise his functions in connection with charities`; `sch 11A part 2 the disclosure is of a specified description` | 1 | F84 |  |
| sch 11A para 46 | 20599 | fork | `sch 11A para 46 enabling or assisting the Gambling Commission to exercise its functions under sections 5 to 10 and 15 of the National Lottery etc. Act 1993`; `sch 11A part 2 the disclosure is of a specified description` | 1 | F84 |  |
| sch 11A para 47 | 20600 | fork | `sch 11A para 47 by the Gambling Commission to the Comptroller and Auditor General for an examination under Part 2 of the National Audit Act 1983`; `sch 11A part 2 the disclosure is of a specified description` | 1 | F84 |  |
| sch 11A para 48 | 20601 | fork | `sch 11A para 48 enabling or assisting a regulator under Schedule 3 to the Consumer Rights Act 2015 other than the Competition and Markets Authority`; `sch 11A part 2 the disclosure is of a specified description` | 1 | F84 |  |
| sch 11A para 49 | 20602 | fork | `sch 11A para 49 enabling or assisting an enforcement authority under the Consumer Contracts (Information, Cancellation and Additional Charges) Regulations 2013`; `sch 11A part 2 the disclosure is of a specified description` | 1 | F84 |  |
| sch 11A para 50 | 20603 | fork | `sch 11A para 50 enabling or assisting an enforcement authority under the Financial Services (Distance Marketing) Regulations 2004`; `sch 11A part 2 the disclosure is of a specified description` | 1 | F84 |  |
| sch 11A para 51 | 20604 | fork | `sch 11A para 51 enabling or assisting a local weights and measures authority in England and Wales under section 171(2) of the Digital Markets, Competition and Consumers Act 2024`; `sch 11A part 2 the disclosure is of a specified description` | 1 | F84 |  |
| sch 11A para 51A | 20605 | fork | `sch 11A para 51A enabling or assisting the lead enforcement authority under the Estate Agents Act 1979`; `sch 11A part 2 the disclosure is of a specified description` | 1 | F84 |  |
| sch 11A para 52 | 20606 | fork | `sch 11A part 2 the disclosure is of a specified description` | 89 | F84 |  |
| sch 11A para 52(a) | 20607 | fork | limb of the row above: `sch 11A para 52(a) enabling or assisting the Financial Conduct Authority or the Prudential Regulation Authority to exercise functions under the legislation relating to friendly societies` (+1) |  | F84 |  |
| sch 11A para 52(aa) | 20608 | fork | limb of the row above: `sch 11A para 52(aa) enabling or assisting the Financial Conduct Authority or the Prudential Regulation Authority to exercise functions under the Consumer Credit Act 1974` (+1) |  | F84 |  |
| sch 11A para 52(ab) | 20609 | fork | limb of the row above: `sch 11A para 52(ab) enabling or assisting the Financial Conduct Authority or the Prudential Regulation Authority to exercise functions under the Credit Unions Act 1979` (+1) |  | F84 |  |
| sch 11A para 52(b) | 20610 | fork | limb of the row above: `sch 11A para 52(b) enabling or assisting the Financial Conduct Authority or the Prudential Regulation Authority to exercise functions under the Building Societies Act 1986` (+1) |  | F84 |  |
| sch 11A para 52(c) | 20611 | fork | limb of the row above: `sch 11A para 52(c) enabling or assisting the Financial Conduct Authority or the Prudential Regulation Authority to exercise functions under Part 7 of the Companies Act 1989` (+1) |  | F84 |  |
| sch 11A para 52(d) | 20612 | fork | limb of the row above: `sch 11A para 52(d) enabling or assisting the Financial Conduct Authority or the Prudential Regulation Authority to exercise functions under the Financial Services and Markets Act 2000` (+1) |  | F84 |  |
| sch 11A para 52(e) | 20613 | fork | limb of the row above: `sch 11A para 52(e) enabling or assisting the Financial Conduct Authority or the Prudential Regulation Authority to exercise functions under the Co-operative and Community Benefit Societies Act 2014` (+1) |  | F84 |  |
| sch 11A para 53 | 20614 | repealed or blank in this text (reason 3) | - | - | F84 | the text shows only dots: nothing to encode |
| sch 11A para 54 | 20615 | fork | `sch 11A para 54 enabling or assisting the compensation scheme manager established under section 212(1) of the Financial Services and Markets Act 2000`; `sch 11A part 2 the disclosure is of a specified description` | 1 | F84 |  |
| sch 11A para 55 | 20616 | fork | `sch 11A para 55 enabling or assisting a recognised investment exchange, a recognised clearing house or a recognised CSD to exercise its functions as such`; `sch 11A para 55 the body is a recognised investment exchange, a recognised clearing house or a recognised CSD`; `sch 11A part 2 the disclosure is of a specified description` | 3 | F84 |  |
| sch 11A para 56 | 20617 | fork | `sch 11A para 56 enabling or assisting an operator of a relevant system for the purposes of the Uncertificated Securities Regulations 2001`; `sch 11A part 2 the disclosure is of a specified description` | 1 | F84 |  |
| sch 11A para 57 | 20618 | fork | `sch 11A para 57 enabling or assisting a body designated under section 326(1) of the Financial Services and Markets Act 2000`; `sch 11A part 2 the disclosure is of a specified description` | 1 | F84 |  |
| sch 11A para 58 | 20619 | fork | `sch 11A para 58 with a view to the institution of, or for the purposes of, civil proceedings arising under or by virtue of the Financial Services and Markets Act 2000`; `sch 11A part 2 the disclosure is of a specified description` | 1 | F84 |  |
| sch 11A para 59 | 20620 | fork | `sch 11A para 59 enabling or assisting a body designated under section 1252 of this Act to exercise its functions under Part 42 of this Act`; `sch 11A part 2 the disclosure is of a specified description` | 1 | F84 |  |
| sch 11A para 60 | 20621 | fork | `sch 11A para 60 enabling or assisting a recognised supervisory or qualifying body to exercise its functions as such`; `sch 11A part 2 the disclosure is of a specified description` | 1 | F84 |  |
| sch 11A para 61 | 20622 | fork | `sch 11A para 61 making available to an audited person information relating to a statutory audit of that persons accounts`; `sch 11A part 2 the disclosure is of a specified description` | 1 | F84 |  |
| sch 11A para 62 | 20623 | fork | `sch 11A para 62 making available to the public information relating to inspections under regulation 9 of the Statutory Auditors and Third Country Auditors Regulations 2016`; `sch 11A part 2 the disclosure is of a specified description` | 4 | F84, F85 |  |
| sch 11A para 63 | 20624 | fork | `sch 11A para 63 enabling or assisting an official receiver to exercise his functions under the enactments relating to insolvency`; `sch 11A part 2 the disclosure is of a specified description` | 1 | F84 |  |
| sch 11A para 64 | 20625 | repealed or blank in this text (reason 3) | - | - | F84 | the text shows only dots: nothing to encode |
| sch 11A para 65 | 20626 | fork | `sch 11A para 65 enabling or assisting a recognised professional body for the purposes of section 391 of the Insolvency Act 1986`; `sch 11A part 2 the disclosure is of a specified description` | 1 | F84 |  |
| sch 11A para 66 | 20627 | fork | `sch 11A para 66 enabling or assisting an overseas regulatory authority to exercise its regulatory functions`; `sch 11A para 66 the body is an overseas regulatory authority`; `sch 11A part 2 the disclosure is of a specified description` | 3 | F84 |  |
| sch 11A para 67 | 20628 | fork | `sch 11A para 67 enabling or assisting the Regulator of Community Interest Companies`; `sch 11A part 2 the disclosure is of a specified description` | 1 | F84 |  |
| sch 11A para 68 | 20629 | fork | `sch 11A para 68 with a view to the institution of, or for the purposes of, criminal proceedings`; `sch 11A part 2 the disclosure is of a specified description` | 2 | F84 |  |
| sch 11A para 69 | 20630 | fork | `sch 11A para 69 enabling or assisting a person authorised by the Secretary of State under Part 2, 3 or 4 of the Proceeds of Crime Act 2002`; `sch 11A part 2 the disclosure is of a specified description` | 1 | F84 |  |
| sch 11A para 70 | 20631 | fork | `sch 11A para 70 with a view to the institution of, or for the purposes of, proceedings on an application under section 6, 7 or 8 of the Company Directors Disqualification Act 1986`; `sch 11A part 2 the disclosure is of a specified description` | 1 | F84 |  |
| sch 11A para 71 | 20632 | fork | `sch 11A part 2 the disclosure is of a specified description` | 89 | F84 |  |
| sch 11A para 71(a) | 20633 | fork | limb of the row above: `sch 11A para 71(a) with a view to proceedings before the Upper Tribunal in respect of a decision of the Financial Conduct Authority` (+1) |  | F84 |  |
| sch 11A para 71(aa) | 20634 | fork | limb of the row above: `sch 11A para 71(aa) with a view to proceedings before the Upper Tribunal in respect of a decision of the Prudential Regulation Authority` (+1) |  | F84 |  |
| sch 11A para 71(b) | 20635 | fork | limb of the row above: `sch 11A para 71(b) with a view to proceedings before the Upper Tribunal in respect of a decision of the Bank of England` (+1) |  | F84 |  |
| sch 11A para 71(c) | 20636 | fork | limb of the row above: `sch 11A para 71(c) with a view to proceedings before the Upper Tribunal in respect of a decision relating to the assessment of compensation under the Banking legislation` (+1) |  | F84 |  |
| sch 11A para 72 | 20637 | fork | `sch 11A para 72 for the purposes of proceedings before the Financial Services Tribunal by virtue of the 2001 Partly Completed Procedures Order`; `sch 11A part 2 the disclosure is of a specified description` | 1 | F84 |  |
| sch 11A para 73 | 20638 | fork | `sch 11A para 73 for the purposes of proceedings before a tribunal in relation to a decision of the Pensions Regulator`; `sch 11A part 2 the disclosure is of a specified description` | 1 | F84 |  |
| sch 11A para 74 | 20639 | fork | `sch 11A para 74 enabling or assisting a body appointed under section 14 of the Companies (Audit, Investigations and Community Enterprise) Act 2004`; `sch 11A part 2 the disclosure is of a specified description` | 1 | F84 |  |
| sch 11A para 75 | 20640 | fork | `sch 11A para 75 with a view to disciplinary proceedings relating to the performance by a relevant lawyer, foreign lawyer, auditor, accountant, valuer or actuary of his professional duties`; `sch 11A para 75 the person is a relevant lawyer`; `sch 11A part 2 the disclosure is of a specified description` | 5 | F84 |  |
| sch 11A para 75(None) term “foreign lawyer” | 20641 | fork | `sch 11A para 75 with a view to disciplinary proceedings relating to the performance by a relevant lawyer, foreign lawyer, auditor, accountant, valuer or actuary of his professional duties`; `sch 11A para 75 the person is a relevant lawyer`; `sch 11A part 2 the disclosure is of a specified description` | 5 | F84 |  |
| sch 11A para 75(None) term “relevant lawyer” | 20642-20645 | fork | `sch 11A para 75 with a view to disciplinary proceedings relating to the performance by a relevant lawyer, foreign lawyer, auditor, accountant, valuer or actuary of his professional duties`; `sch 11A para 75 the person is a relevant lawyer`; `sch 11A part 2 the disclosure is of a specified description` | 5 | F84 |  |
| sch 11A para 76 | 20646 | fork | `sch 11A para 76 with a view to disciplinary proceedings relating to the performance by a public servant of his duties`; `sch 11A para 76 the person is a public servant`; `sch 11A part 2 the disclosure is of a specified description` | 3 | F84 |  |
| sch 11A para 77 | 20647 | fork | `sch 11A para 77 the provision of a summary or collection of information framed so as not to enable the identity of any person to whom it relates to be ascertained`; `sch 11A part 2 the disclosure is of a specified description` | 1 | F84 |  |
| sch 11A para 78 | 20648 | fork | `sch 11A para 78 in pursuance of any assimilated obligation`; `sch 11A part 2 the disclosure is of a specified description` | 1 | F84 |  |
| sch 11A part 3 heading | 20649 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 11A para 79 | 20650 | fork | `sch 11A para 79 the disclosure is made in accordance with this Part of this Schedule` | 4 | F86 |  |
| sch 11A para 80 | 20651 | fork | `sch 11A para 80 the disclosure is made in accordance with this Part of this Schedule` | 5 | F87 |  |
| sch 11A para 80(a) | 20652 | fork | limb of the row above: `sch 11A para 80 the disclosure is made in accordance with this Part of this Schedule` |  | F87 |  |
| sch 11A para 80(b) | 20653 | fork | limb of the row above: `sch 11A para 80 the disclosure is made in accordance with this Part of this Schedule` |  | F87 |  |
| sch 12 heading | 20654 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 12 section reference | 20655 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 12 cross-heading (line 20656) "Arrangements for independent monitoring of audits of UK-tra…" | 20656 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 12 para 1(1) | 20657 | fork | `sch 12 para 1(1) the arrangements are appropriate arrangements` | 3 | F88 |  |
| sch 12 para 1(1)(a) | 20658 | fork | limb of the row above: `sch 12 para 1(1) the arrangements are appropriate arrangements` |  | F88 |  |
| sch 12 para 1(1)(b) | 20659 | fork | limb of the row above: `sch 12 para 1(1) the arrangements are appropriate arrangements` |  | F88 |  |
| sch 12 para 1(2) | 20660 | repealed or blank in this text (reason 3) | - | - |  | the text shows only dots: nothing to encode |
| sch 12 cross-heading (line 20661) "Arrangements for independent investigations for disciplinar…" | 20661 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 12 para 2(1) | 20662 | fork | `sch 12 para 2(1) the arrangements are appropriate arrangements` | 7 | F88 |  |
| sch 12 para 2(1)(a) | 20663 | fork | limb of the row above: `sch 12 para 2(1) the arrangements are appropriate arrangements` |  | F88 |  |
| sch 12 para 2(1)(b) | 20664 | fork | limb of the row above: `sch 12 para 2(1) the arrangements are appropriate arrangements` |  | F88 |  |
| sch 12 para 2(1)(b)(i) | 20665 | fork | limb of the row above: `sch 12 para 2(1) the arrangements are appropriate arrangements` |  | F88 |  |
| sch 12 para 2(1)(b)(ii) | 20666 | fork | limb of the row above: `sch 12 para 2(1) the arrangements are appropriate arrangements` |  | F88 |  |
| sch 12 para 2(1)(b)(iii) | 20667 | fork | limb of the row above: `sch 12 para 2(1) the arrangements are appropriate arrangements` |  | F88 |  |
| sch 12 para 2(1)(c) | 20668 | fork | limb of the row above: `sch 12 para 2(1) the arrangements are appropriate arrangements` |  | F88 |  |
| sch 12 para 2(1A) | 20669 | encoded | `sch 12 para 2(1A) decisions to take disciplinary action may be made without a disciplinary hearing` | 2 |  |  |
| sch 12 para 2(2) | 20670 | encoded | `sch 12 para 2(2) the action is disciplinary action` | 2 |  |  |
| sch 12 para 2(2) term “disciplinary action” | 20671-20672 | encoded | `sch 12 para 2(2) the action is disciplinary action` | 2 |  |  |
| sch 12 cross-heading (line 20673) "Supplementary: arrangements to operate independently of thi…" | 20673 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 12 para 3(1) | 20674 | encoded | `sch 12 para 3(1) this paragraph applies` | 3 |  |  |
| sch 12 para 3(1)(a) | 20675 | encoded | limb of the row above: `sch 12 para 3(1) this paragraph applies` |  |  |  |
| sch 12 para 3(1)(b) | 20676 | encoded | limb of the row above: `sch 12 para 3(1) this paragraph applies` |  |  |  |
| sch 12 para 3(2) | 20677 | fork | `sch 12 para 3(2) the arrangements are not to be regarded as appropriate for ensuring independence` | 4 | F89 |  |
| sch 12 para 3(2)(a) | 20678 | fork | limb of the row above: `sch 12 para 3(2) the arrangements are not to be regarded as appropriate for ensuring independence` |  | F89 |  |
| sch 12 para 3(2)(b) | 20679 | fork | limb of the row above: `sch 12 para 3(2) the arrangements are not to be regarded as appropriate for ensuring independence` |  | F89 |  |
| sch 12 para 3(3) | 20680 | encoded | `sch 12 para 3(3) additional criteria may need to be satisfied for the arrangements to be regarded as appropriate` | 2 |  |  |
| sch 12 cross-heading (line 20681) "Supplementary: funding of arrangements" | 20681 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 12 para 4(1) | 20682 | encoded | `sch 12 para 4 pay the costs of maintaining the relevant arrangements`; `sch 12 para 4 the duty to pay the costs`; `sch 12 para 4 the registered third country auditor has paid the costs it must pay` | 5 |  |  |
| sch 12 para 4(2) | 20683 | encoded | `sch 12 para 4 pay the costs of maintaining the relevant arrangements`; `sch 12 para 4 the duty to pay the costs`; `sch 12 para 4 the registered third country auditor has paid the costs it must pay` | 5 |  |  |
| sch 12 cross-heading (line 20684) "Supplementary: scope of arrangements" | 20684 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 12 para 5 | 20685 | encoded | `sch 12 para 5 the arrangements may qualify as arrangements within paragraph 1 or 2` | 2 |  |  |
| sch 12 cross-heading (line 20686) "Specification of particular arrangements by the Secretary o…" | 20686 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 12 para 6(1) | 20687 | encoded | `sch 12 para 6(1) the registered third country auditor is obliged to participate in the set of arrangements` | 4 |  |  |
| sch 12 para 6(2) | 20688 | inert (reason 2) | - | - | F90 | says how an order is made (negative resolution procedure) |
| sch 13 heading | 20689 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 13 section reference | 20690 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 13 cross-heading (line 20691) "Operation of this Schedule" | 20691 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 13 para 1(1) | 20692 | fork | `sch 13 para 1(1) the paragraph has effect in relation to the body` | 12 | F91 |  |
| sch 13 para 1(1)(a) | 20693 | fork | limb of the row above: `sch 13 para 1(1) the paragraph has effect in relation to the body` |  | F91 |  |
| sch 13 para 1(1)(b) | 20694 | fork | limb of the row above: `sch 13 para 1(1) the paragraph has effect in relation to the body` |  | F91 |  |
| sch 13 para 1(1)(c) | 20695 | fork | limb of the row above: `sch 13 para 1(1) the paragraph has effect in relation to the body` |  | F91 |  |
| sch 13 para 1(2) | 20696 | encoded | `sch 13 para 1(2) paragraph 2 or 6 applies to the existing body in relation to the thing or function` | 3 |  |  |
| sch 13 para 1(2)(a) | 20697 | encoded | limb of the row above: `sch 13 para 1(2) paragraph 2 or 6 applies to the existing body in relation to the thing or function` |  |  |  |
| sch 13 para 1(2)(b) | 20698 | encoded | limb of the row above: `sch 13 para 1(2) paragraph 2 or 6 applies to the existing body in relation to the thing or function` |  |  |  |
| sch 13 para 1(3) | 20699 | encoded | `sch 13 para 1(3) the power is a power to make provision by an order under section 1252` | 2 |  |  |
| sch 13 cross-heading (line 20700) "Status" | 20700 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 13 para 2 | 20701 | encoded | `sch 13 para 2 the person is regarded as acting on behalf of the Crown or as a Crown servant` | 3 |  |  |
| sch 13 cross-heading (line 20702) "Name, members and chairman" | 20702 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 13 para 3(1) | 20703 | inert (reason 2) | - | - |  | boards, offices and their staffing: the name, membership and chairman of the delegated body (para 3), its proceedings (para 5), the order that provides for its winding up on revocation (para 12) |
| sch 13 para 3(2) | 20704 | inert (reason 2) | - | - |  | boards, offices and their staffing: the name, membership and chairman of the delegated body (para 3), its proceedings (para 5), the order that provides for its winding up on revocation (para 12) |
| sch 13 para 3(3) | 20705 | inert (reason 2) | - | - |  | boards, offices and their staffing: the name, membership and chairman of the delegated body (para 3), its proceedings (para 5), the order that provides for its winding up on revocation (para 12) |
| sch 13 para 3(4) | 20706 | inert (reason 2) | - | - |  | boards, offices and their staffing: the name, membership and chairman of the delegated body (para 3), its proceedings (para 5), the order that provides for its winding up on revocation (para 12) |
| sch 13 para 3(4)(a) | 20707 | inert (reason 2) | - | - |  | boards, offices and their staffing: the name, membership and chairman of the delegated body (para 3), its proceedings (para 5), the order that provides for its winding up on revocation (para 12) |
| sch 13 para 3(4)(b) | 20708 | inert (reason 2) | - | - |  | boards, offices and their staffing: the name, membership and chairman of the delegated body (para 3), its proceedings (para 5), the order that provides for its winding up on revocation (para 12) |
| sch 13 cross-heading (line 20709) "Financial provisions" | 20709 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 13 para 4(1) | 20710 | fork | `sch 13 para 4(1) the body has paid what it must pay by way of remuneration and allowances` | 4 | F92 |  |
| sch 13 para 4(2) | 20711 | encoded | `sch 13 para 4(2) the body has paid or made provision for the pension, allowance or gratuity` | 3 |  |  |
| sch 13 para 4(2)(a) | 20712 | encoded | limb of the row above: `sch 13 para 4(2) the body has paid or made provision for the pension, allowance or gratuity` |  |  |  |
| sch 13 para 4(2)(b) | 20713-20714 | encoded | limb of the row above: `sch 13 para 4(2) the body has paid or made provision for the pension, allowance or gratuity` |  |  |  |
| sch 13 para 4(3) | 20715 | fork | `sch 13 para 4(3) the body has paid the compensation it must pay` | 5 | F92 |  |
| sch 13 para 4(3)(a) | 20716 | fork | limb of the row above: `sch 13 para 4(3) the body has paid the compensation it must pay` |  | F92 |  |
| sch 13 para 4(3)(b) | 20717-20718 | fork | limb of the row above: `sch 13 para 4(3) the body has paid the compensation it must pay` |  | F92 |  |
| sch 13 cross-heading (line 20719) "Proceedings" | 20719 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 13 para 5(1) | 20720 | inert (reason 2) | - | - |  | boards, offices and their staffing: the name, membership and chairman of the delegated body (para 3), its proceedings (para 5), the order that provides for its winding up on revocation (para 12) |
| sch 13 para 5(2) | 20721 | inert (reason 2) | - | - |  | boards, offices and their staffing: the name, membership and chairman of the delegated body (para 3), its proceedings (para 5), the order that provides for its winding up on revocation (para 12) |
| sch 13 para 5(2)(a) | 20722 | inert (reason 2) | - | - |  | boards, offices and their staffing: the name, membership and chairman of the delegated body (para 3), its proceedings (para 5), the order that provides for its winding up on revocation (para 12) |
| sch 13 para 5(2)(b) | 20723 | inert (reason 2) | - | - |  | boards, offices and their staffing: the name, membership and chairman of the delegated body (para 3), its proceedings (para 5), the order that provides for its winding up on revocation (para 12) |
| sch 13 cross-heading (line 20724) "Fees" | 20724 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 13 para 6(1) | 20725 | encoded | `sch 13 para 6(1) the body may retain the fees` | 2 |  |  |
| sch 13 para 6(2) | 20726 | encoded | `sch 13 para 6(2) the fees are applied as required` | 3 |  |  |
| sch 13 para 6(2)(a) | 20727 | encoded | limb of the row above: `sch 13 para 6(2) the fees are applied as required` |  |  |  |
| sch 13 para 6(2)(b) | 20728 | encoded | limb of the row above: `sch 13 para 6(2) the fees are applied as required` |  |  |  |
| sch 13 para 6(3) | 20729 | encoded | `sch 13 para 6(3) the expense is one of the expenses of the body` | 2 |  |  |
| sch 13 para 6(4) | 20730 | encoded | `sch 13 para 6(4) the fees prescribed are as required` | 2 |  |  |
| sch 13 para 6(5) | 20731 | encoded | `sch 13 para 6(5) the exercise of the power to prescribe fees has the approval required` | 2 |  |  |
| sch 13 para 6(6) | 20732 | encoded | `sch 13 para 6(6) the Secretary of State may by order vary or revoke regulations prescribing fees` | 2 |  |  |
| sch 13 cross-heading (line 20733) "Legislative functions" | 20733 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 13 para 7(1) | 20734 | encoded | `sch 13 para 7(1)-(2) the regulations or order of the body are made as required` | 4 |  |  |
| sch 13 para 7(2) | 20735 | encoded | `sch 13 para 7(1)-(2) the regulations or order of the body are made as required` | 4 |  |  |
| sch 13 para 7(3) | 20736 | inert (reason 2) | - | - |  | a power to make an order about consultation |
| sch 13 para 7(4) | 20737 | encoded | `sch 13 para 7(4) the regulations or order are subject to negative resolution procedure or affirmative resolution procedure` | 2 |  |  |
| sch 13 para 8(1) | 20738 | encoded | `sch 13 para 8(1) print the instrument and make it available to the public`; `sch 13 para 8(1) the duty to make the instrument available`; `sch 13 para 8(1) the instrument has been printed and made available as required` | 3 |  |  |
| sch 13 para 8(2) | 20739 | fork | `sch 13 para 8(2) this paragraph gives a defence to the alleged contravention` | 2 | F93 |  |
| sch 13 para 9(1) | 20740 | encoded | `sch 13 para 9(1) the printed copy is evidence of the facts stated in the certificate` | 4 |  |  |
| sch 13 para 9(1)(a) | 20741 | encoded | limb of the row above: `sch 13 para 9(1) the printed copy is evidence of the facts stated in the certificate` |  |  |  |
| sch 13 para 9(1)(b) | 20742 | encoded | limb of the row above: `sch 13 para 9(1) the printed copy is evidence of the facts stated in the certificate` |  |  |  |
| sch 13 para 9(1)(c) | 20743-20744 | encoded | limb of the row above: `sch 13 para 9(1) the printed copy is evidence of the facts stated in the certificate` |  |  |  |
| sch 13 para 9(2) | 20745 | encoded | `sch 13 para 9(2) the certificate is deemed to have been duly signed` | 3 |  |  |
| sch 13 para 9(3) | 20746 | encoded | `sch 13 para 9(3) cause a copy of the instrument to be endorsed with a certificate`; `sch 13 para 9(3) the duty to endorse a copy`; `sch 13 para 9(3) the person may require the body to cause a copy of the instrument to be endorsed with a certificate` | 2 |  |  |
| sch 13 cross-heading (line 20747) "Report and accounts" | 20747 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 13 para 10(1) | 20748 | fork | `sch 13 para 10(1) make a report to the Secretary of State`; `sch 13 para 10(1) the annual report`; `sch 13 para 10(1) the body has complied for the calendar year` | 3 | F94 |  |
| sch 13 para 10(1)(a) | 20749 | fork | limb of the row above: `sch 13 para 10(1) make a report to the Secretary of State` (+2) |  | F94 |  |
| sch 13 para 10(1)(b) | 20750 | fork | limb of the row above: `sch 13 para 10(1) make a report to the Secretary of State` (+2) |  | F94 |  |
| sch 13 para 10(2) | 20751 | encoded | `sch 13 para 10(2) the delegation order may modify sub-paragraph (1) for the calendar year` | 2 |  |  |
| sch 13 para 10(3) | 20752 | encoded | `sch 13 para 10(3) lay copies of the report before Parliament`; `sch 13 para 10(3) the duty to lay the report`; `sch 13 para 10(3) the Secretary of State has laid the report before Parliament as required` | 3 |  |  |
| sch 13 para 10(4) | 20753 | encoded | `sch 13 para 10(4) the sub-paragraph applies to the body` | 6 |  |  |
| sch 13 para 10(4)(a) | 20754 | encoded | limb of the row above: `sch 13 para 10(4) the sub-paragraph applies to the body` |  |  |  |
| sch 13 para 10(4)(b) | 20755 | encoded | limb of the row above: `sch 13 para 10(4) the sub-paragraph applies to the body` |  |  |  |
| sch 13 para 10(5) | 20756 | encoded | `sch 13 para 10(5) the Secretary of State may give directions about the accounts and the audit of the accounts` | 3 |  |  |
| sch 13 para 10(6) | 20757 | encoded | `sch 13 para 10(6) the person may be appointed as auditor of the body` | 4 |  |  |
| sch 13 para 10(7) | 20758 | encoded | `sch 13 para 10(7) the Secretary of State may give directions about the accounts and the audit of the accounts` | 5 |  |  |
| sch 13 para 10(8) | 20759 | encoded | `sch 13 para 10(8) the Secretary of State may direct that provisions of this Act specified in the directions apply to the body` | 2 |  |  |
| sch 13 cross-heading (line 20760) "Other supplementary provisions" | 20760 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 13 para 11(1) | 20761 | encoded | `sch 13 para 11(1) the transfer or resumption of the function affects the thing previously done` | 2 |  |  |
| sch 13 para 11(2) | 20762 | inert (reason 2) | - | - |  | orders providing for the transfer or resumption of a function: order-making machinery |
| sch 13 para 11(3) | 20763 | inert (reason 2) | - | - |  | orders providing for the transfer or resumption of a function: order-making machinery |
| sch 13 para 11(3)(a) | 20764 | inert (reason 2) | - | - |  | orders providing for the transfer or resumption of a function: order-making machinery |
| sch 13 para 11(3)(b) | 20765 | inert (reason 2) | - | - |  | orders providing for the transfer or resumption of a function: order-making machinery |
| sch 13 para 11(3)(c) | 20766 | inert (reason 2) | - | - |  | orders providing for the transfer or resumption of a function: order-making machinery |
| sch 13 para 11(3)(d) | 20767 | inert (reason 2) | - | - |  | orders providing for the transfer or resumption of a function: order-making machinery |
| sch 13 para 11(3)(e) | 20768 | inert (reason 2) | - | - |  | orders providing for the transfer or resumption of a function: order-making machinery |
| sch 13 para 11(4) | 20769 | inert (reason 2) | - | - |  | orders providing for the transfer or resumption of a function: order-making machinery |
| sch 13 para 11(4)(a) | 20770 | inert (reason 2) | - | - |  | orders providing for the transfer or resumption of a function: order-making machinery |
| sch 13 para 11(4)(b) | 20771 | inert (reason 2) | - | - |  | orders providing for the transfer or resumption of a function: order-making machinery |
| sch 13 para 11(4)(c) | 20772 | inert (reason 2) | - | - |  | orders providing for the transfer or resumption of a function: order-making machinery |
| sch 13 para 12 | 20773 | inert (reason 2) | - | - |  | boards, offices and their staffing: the name, membership and chairman of the delegated body (para 3), its proceedings (para 5), the order that provides for its winding up on revocation (para 12) |
| sch 13 para 12(a) | 20774 | inert (reason 2) | - | - |  | boards, offices and their staffing: the name, membership and chairman of the delegated body (para 3), its proceedings (para 5), the order that provides for its winding up on revocation (para 12) |
| sch 13 para 12(b) | 20775 | inert (reason 2) | - | - |  | boards, offices and their staffing: the name, membership and chairman of the delegated body (para 3), its proceedings (para 5), the order that provides for its winding up on revocation (para 12) |
| sch 13 para 13(1) | 20776 | encoded | `sch 13 para 13(2) the proceedings may be brought by or against the body in the name of the body corporate` | 4 |  |  |
| sch 13 para 13(2) | 20777 | encoded | `sch 13 para 13(2) the proceedings may be brought by or against the body in the name of the body corporate` | 4 |  |  |
| sch 13 para 13(3) | 20778 | encoded | `sch 13 para 13(2) the proceedings may be brought by or against the body in the name of the body corporate` | 4 |  |  |
| sch 13 para 13(4) | 20779 | encoded | `sch 13 para 13(4) the reference in paragraph 11(3)(e) or (4)(c) is read with the appropriate modifications` | 2 |  |  |
| sch 14 heading | 20780 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 14 section reference | 20781 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 14 cross-heading (line 20782) "Companies (Audit, Investigations and Community Enterprise) …" | 20782 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 14 para 1 | 20783-20789 | inert (reason 2) | - | - |  | amendment or repeal of other Acts: amends section 16 of the Companies (Audit, Investigations and Community Enterprise) Act 2004 |
| sch 15 heading | 20790 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 15 section reference | 20791 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 15 part 1 heading | 20792 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 15 para 1 | 20793 | inert (reason 2) | - | - |  | amendment or repeal of other Acts: amends the Financial Services and Markets Act 2000 or the Companies (Audit, Investigations and Community Enterprise) Act 2004 |
| sch 15 para 2 | 20794 | repealed or blank in this text (reason 3) | - | - |  | the text shows only dots: nothing to encode |
| sch 15 para 3 | 20795-20796 | inert (reason 2) | - | - |  | amendment or repeal of other Acts: amends the Financial Services and Markets Act 2000 or the Companies (Audit, Investigations and Community Enterprise) Act 2004 |
| sch 15 para 4 | 20797 | inert (reason 2) | - | - |  | amendment or repeal of other Acts: amends the Financial Services and Markets Act 2000 or the Companies (Audit, Investigations and Community Enterprise) Act 2004 |
| sch 15 para 5 | 20798 | inert (reason 2) | - | - |  | amendment or repeal of other Acts: amends the Financial Services and Markets Act 2000 or the Companies (Audit, Investigations and Community Enterprise) Act 2004 |
| sch 15 para 6 | 20799-20817 | inert (reason 2) | - | - |  | amendment or repeal of other Acts: amends the Financial Services and Markets Act 2000 or the Companies (Audit, Investigations and Community Enterprise) Act 2004 |
| sch 15 para 7 | 20818-20820 | inert (reason 2) | - | - |  | amendment or repeal of other Acts: amends the Financial Services and Markets Act 2000 or the Companies (Audit, Investigations and Community Enterprise) Act 2004 |
| sch 15 para 8 | 20821-20827 | inert (reason 2) | - | - |  | amendment or repeal of other Acts: amends the Financial Services and Markets Act 2000 or the Companies (Audit, Investigations and Community Enterprise) Act 2004 |
| sch 15 para 9 | 20828 | repealed or blank in this text (reason 3) | - | - |  | the text shows only dots: nothing to encode |
| sch 15 para 10 | 20829-20834 | inert (reason 2) | - | - |  | amendment or repeal of other Acts: amends the Financial Services and Markets Act 2000 or the Companies (Audit, Investigations and Community Enterprise) Act 2004 |
| sch 15 para 11 | 20835-20839 | inert (reason 2) | - | - |  | amendment or repeal of other Acts: amends the Financial Services and Markets Act 2000 or the Companies (Audit, Investigations and Community Enterprise) Act 2004 |
| sch 15 para 12 | 20840 | inert (reason 2) | - | - |  | amendment or repeal of other Acts: amends the Financial Services and Markets Act 2000 or the Companies (Audit, Investigations and Community Enterprise) Act 2004 |
| sch 15 part 2 heading | 20841 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 15 para 13 | 20842 | inert (reason 2) | - | - |  | amendment or repeal of other Acts: amends the Financial Services and Markets Act 2000 or the Companies (Audit, Investigations and Community Enterprise) Act 2004 |
| sch 15 para 14 | 20843-20857 | inert (reason 2) | - | - |  | amendment or repeal of other Acts: amends the Financial Services and Markets Act 2000 or the Companies (Audit, Investigations and Community Enterprise) Act 2004 |
| sch 15 para 15 | 20858-20865 | inert (reason 2) | - | - |  | amendment or repeal of other Acts: amends the Financial Services and Markets Act 2000 or the Companies (Audit, Investigations and Community Enterprise) Act 2004 |
| sch 16 heading | 20866 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 16 section reference | 20867 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 16 table 1 heading | 20868 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 16 table 1 column headings | 20869 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 16 table 1 row 1: Companies Act 1985 (c. 6) | 20870 | inert (reason 2) | - | - |  | amendment or repeal of other Acts: repeals enactments of other Acts and Orders (a table row) |
| sch 16 table 1 row 2: Insolvency Act 1985 (c. 65) | 20871 | inert (reason 2) | - | - |  | amendment or repeal of other Acts: repeals enactments of other Acts and Orders (a table row) |
| sch 16 table 1 row 3: Insolvency Act 1986 (c. 45) | 20872 | inert (reason 2) | - | - |  | amendment or repeal of other Acts: repeals enactments of other Acts and Orders (a table row) |
| sch 16 table 1 row 4: Building Societies Act 1986 (c. 53) | 20873 | inert (reason 2) | - | - |  | amendment or repeal of other Acts: repeals enactments of other Acts and Orders (a table row) |
| sch 16 table 1 row 5: Finance Act 1988 (c. 39) | 20874 | inert (reason 2) | - | - |  | amendment or repeal of other Acts: repeals enactments of other Acts and Orders (a table row) |
| sch 16 table 1 row 6: Water Act 1989 (c. 15) | 20875 | inert (reason 2) | - | - |  | amendment or repeal of other Acts: repeals enactments of other Acts and Orders (a table row) |
| sch 16 table 1 row 7: Companies Act 1989 (c. 40) | 20876 | inert (reason 2) | - | - |  | amendment or repeal of other Acts: repeals enactments of other Acts and Orders (a table row) |
| sch 16 table 1 row 8: Age of Legal Capacity (Scotland) Act 1991 (c. 50) | 20877 | inert (reason 2) | - | - |  | amendment or repeal of other Acts: repeals enactments of other Acts and Orders (a table row) |
| sch 16 table 1 row 9: Water Consolidation (Consequential Provisions) Act 1991 (c. 60) | 20878 | inert (reason 2) | - | - |  | amendment or repeal of other Acts: repeals enactments of other Acts and Orders (a table row) |
| sch 16 table 1 row 10: Charities Act 1992 (c. 41) | 20879 | inert (reason 2) | - | - |  | amendment or repeal of other Acts: repeals enactments of other Acts and Orders (a table row) |
| sch 16 table 1 row 11: Charities Act 1993 (c. 10) | 20880 | inert (reason 2) | - | - |  | amendment or repeal of other Acts: repeals enactments of other Acts and Orders (a table row) |
| sch 16 table 1 row 12: Criminal Justice Act 1993 (c. 36) | 20881 | inert (reason 2) | - | - |  | amendment or repeal of other Acts: repeals enactments of other Acts and Orders (a table row) |
| sch 16 table 1 row 13: Welsh Language Act 1993 (c. 38) | 20882 | inert (reason 2) | - | - |  | amendment or repeal of other Acts: repeals enactments of other Acts and Orders (a table row) |
| sch 16 table 1 row 14: Pension Schemes Act 1993 (c. 48) | 20883 | inert (reason 2) | - | - |  | amendment or repeal of other Acts: repeals enactments of other Acts and Orders (a table row) |
| sch 16 table 1 row 15: Trade Marks Act 1994 (c. 26) | 20884 | inert (reason 2) | - | - |  | amendment or repeal of other Acts: repeals enactments of other Acts and Orders (a table row) |
| sch 16 table 1 row 16: Deregulation and Contracting Out Act 1994 (c. 40) | 20885 | inert (reason 2) | - | - |  | amendment or repeal of other Acts: repeals enactments of other Acts and Orders (a table row) |
| sch 16 table 1 row 17: Requirements of Writing (Scotland) Act 1995 (c. 7) | 20886 | inert (reason 2) | - | - |  | amendment or repeal of other Acts: repeals enactments of other Acts and Orders (a table row) |
| sch 16 table 1 row 18: Criminal Procedure (Consequential Provisions) (Scotland) Act 1995 (c.… | 20887 | inert (reason 2) | - | - |  | amendment or repeal of other Acts: repeals enactments of other Acts and Orders (a table row) |
| sch 16 table 1 row 19: Disability Discrimination Act 1995 (c. 50) | 20888 | inert (reason 2) | - | - |  | amendment or repeal of other Acts: repeals enactments of other Acts and Orders (a table row) |
| sch 16 table 1 row 20: Financial Services and Markets Act 2000 (c. 8) | 20889 | inert (reason 2) | - | - |  | amendment or repeal of other Acts: repeals enactments of other Acts and Orders (a table row) |
| sch 16 table 1 row 21: Limited Liability Partnerships Act 2000 (c. 12) | 20890 | inert (reason 2) | - | - |  | amendment or repeal of other Acts: repeals enactments of other Acts and Orders (a table row) |
| sch 16 table 1 row 22: Political Parties, Elections and Referendums Act 2000 (c. 41) | 20891 | inert (reason 2) | - | - |  | amendment or repeal of other Acts: repeals enactments of other Acts and Orders (a table row) |
| sch 16 table 1 row 23: Criminal Justice and Police Act 2001 (c. 16) | 20892 | inert (reason 2) | - | - |  | amendment or repeal of other Acts: repeals enactments of other Acts and Orders (a table row) |
| sch 16 table 1 row 24: Enterprise Act 2002 (c. 40) | 20893 | inert (reason 2) | - | - |  | amendment or repeal of other Acts: repeals enactments of other Acts and Orders (a table row) |
| sch 16 table 1 row 25: Companies (Audit, Investigations and Community Enterprise) Act 2004 (… | 20894 | inert (reason 2) | - | - |  | amendment or repeal of other Acts: repeals enactments of other Acts and Orders (a table row) |
| sch 16 table 1 row 26: Civil Partnership Act 2004 (c. 33) | 20895 | inert (reason 2) | - | - |  | amendment or repeal of other Acts: repeals enactments of other Acts and Orders (a table row) |
| sch 16 table 1 row 27: Constitutional Reform Act 2005 (c. 4) | 20896 | inert (reason 2) | - | - |  | amendment or repeal of other Acts: repeals enactments of other Acts and Orders (a table row) |
| sch 16 table 2 heading | 20897 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 16 table 2 column headings | 20898 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 16 table 2 row 1: Companies (Northern Ireland) Order 1986 (S.I. 1986/1032 (N.I. 6)) | 20899 | inert (reason 2) | - | - |  | amendment or repeal of other Acts: repeals enactments of other Acts and Orders (a table row) |
| sch 16 table 2 row 2: Companies Consolidation (Consequential Provisions) (Northern Ireland)… | 20900 | inert (reason 2) | - | - |  | amendment or repeal of other Acts: repeals enactments of other Acts and Orders (a table row) |
| sch 16 table 2 row 3: Business Names (Northern Ireland) Order 1986 (S.I. 1986/1033 (N.I. 7)) | 20901 | inert (reason 2) | - | - |  | amendment or repeal of other Acts: repeals enactments of other Acts and Orders (a table row) |
| sch 16 table 2 row 4: Industrial Relations (Northern Ireland) Order 1987 (S.I. 1987/936 N.I… | 20902 | inert (reason 2) | - | - |  | amendment or repeal of other Acts: repeals enactments of other Acts and Orders (a table row) |
| sch 16 table 2 row 5: Finance Act 1988 (c. 39) | 20903 | inert (reason 2) | - | - |  | amendment or repeal of other Acts: repeals enactments of other Acts and Orders (a table row) |
| sch 16 table 2 row 6: Companies (Northern Ireland) Order 1989 (S.I. 1989/2404 (N.I. 18)) | 20904 | inert (reason 2) | - | - |  | amendment or repeal of other Acts: repeals enactments of other Acts and Orders (a table row) |
| sch 16 table 2 row 7: Insolvency (Northern Ireland) Order 1989 (S.I. 1989/2405 (N.I. 19)) | 20905 | inert (reason 2) | - | - |  | amendment or repeal of other Acts: repeals enactments of other Acts and Orders (a table row) |
| sch 16 table 2 row 8: European Economic Interest Groupings Regulations (Northern Ireland) 1… | 20906 | inert (reason 2) | - | - |  | amendment or repeal of other Acts: repeals enactments of other Acts and Orders (a table row) |
| sch 16 table 2 row 9: Companies (Northern Ireland) Order 1990 (S.I. 1990/593 (N.I. 5)) | 20907 | inert (reason 2) | - | - |  | amendment or repeal of other Acts: repeals enactments of other Acts and Orders (a table row) |
| sch 16 table 2 row 10: Companies (No. 2) (Northern Ireland) Order 1990 (S.I. 1990/1504 (N.I.… | 20908 | inert (reason 2) | - | - |  | amendment or repeal of other Acts: repeals enactments of other Acts and Orders (a table row) |
| sch 16 table 2 row 11: Criminal Justice Act 1993 (c. 36) | 20909 | inert (reason 2) | - | - |  | amendment or repeal of other Acts: repeals enactments of other Acts and Orders (a table row) |
| sch 16 table 2 row 12: Financial Provisions (Northern Ireland) Order 1993 (S.I. 1993/1252 (N… | 20910 | inert (reason 2) | - | - |  | amendment or repeal of other Acts: repeals enactments of other Acts and Orders (a table row) |
| sch 16 table 2 row 13: Deregulation and Contracting Out Act 1994 (c. 40) | 20911 | inert (reason 2) | - | - |  | amendment or repeal of other Acts: repeals enactments of other Acts and Orders (a table row) |
| sch 16 table 2 row 14: Pensions (Northern Ireland) Order 1995 (S.I. 1995/3213 (N.I. 22)) | 20912 | inert (reason 2) | - | - |  | amendment or repeal of other Acts: repeals enactments of other Acts and Orders (a table row) |
| sch 16 table 2 row 15: Deregulation and Contracting Out (Northern Ireland) Order 1996 (S.I. … | 20913 | inert (reason 2) | - | - |  | amendment or repeal of other Acts: repeals enactments of other Acts and Orders (a table row) |
| sch 16 table 2 row 16: Youth Justice and Criminal Evidence Act 1999 (c. 23) | 20914 | inert (reason 2) | - | - |  | amendment or repeal of other Acts: repeals enactments of other Acts and Orders (a table row) |
| sch 16 table 2 row 17: Limited Liability Partnerships Act (Northern Ireland) 2002 (c. 12 (N.… | 20915 | inert (reason 2) | - | - |  | amendment or repeal of other Acts: repeals enactments of other Acts and Orders (a table row) |
| sch 16 table 2 row 18: Open-Ended Investment Companies Act (Northern Ireland) 2002 (c. 13) | 20916 | inert (reason 2) | - | - |  | amendment or repeal of other Acts: repeals enactments of other Acts and Orders (a table row) |
| sch 16 table 2 row 19: Company Directors Disqualification (Northern Ireland) Order 2002 (S.I… | 20917 | inert (reason 2) | - | - |  | amendment or repeal of other Acts: repeals enactments of other Acts and Orders (a table row) |
| sch 16 table 2 row 20: Companies (Audit, Investigations and Community Enterprise) Act 2004 (… | 20918 | inert (reason 2) | - | - |  | amendment or repeal of other Acts: repeals enactments of other Acts and Orders (a table row) |
| sch 16 table 2 row 21: Law Reform (Miscellaneous Provisions) (Northern Ireland) Order 2005 (… | 20919 | inert (reason 2) | - | - |  | amendment or repeal of other Acts: repeals enactments of other Acts and Orders (a table row) |
| sch 16 table 2 row 22: Companies (Audit, Investigations and Community Enterprise) (Northern … | 20920 | inert (reason 2) | - | - |  | amendment or repeal of other Acts: repeals enactments of other Acts and Orders (a table row) |
| sch 16 table 3 heading | 20921 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 16 table 3 column headings | 20922 | inert (reason 1) | - | - |  | a heading or a reference line: not operative |
| sch 16 table 3 row 1: Limited Partnerships Act 1907 (c. 24) | 20923 | inert (reason 2) | - | - |  | amendment or repeal of other Acts: repeals enactments of other Acts and Orders (a table row) |
| sch 16 table 3 row 2: Business Names Act 1985 (c. 7) | 20924 | inert (reason 2) | - | - |  | amendment or repeal of other Acts: repeals enactments of other Acts and Orders (a table row) |
| sch 16 table 3 row 3: Companies Act 1989 (c. 40) | 20925 | inert (reason 2) | - | - |  | amendment or repeal of other Acts: repeals enactments of other Acts and Orders (a table row) |
| sch 16 table 3 row 4: Criminal Procedure (Consequential Provisions) (Scotland) Act 1995 (c.… | 20926 | inert (reason 2) | - | - |  | amendment or repeal of other Acts: repeals enactments of other Acts and Orders (a table row) |
| sch 16 table 3 row 5: Companies (Audit, Investigations and Community Enterprise) Act 2004 (… | 20927 | inert (reason 2) | - | - |  | amendment or repeal of other Acts: repeals enactments of other Acts and Orders (a table row) |
| sch 16 table 3 row 6: Civil Partnership Act 2004 (c. 33) | 20928 | inert (reason 2) | - | - |  | amendment or repeal of other Acts: repeals enactments of other Acts and Orders (a table row) |

## Fork register (coa30)

Each entry gives the provision, the function, the reading taken, the other reading, and the text that licenses it. The sites the 2026-11-05 ruling leaves to the encoder's judgment carry one line each: an "unless" or "except" met (9(1A) for a public interest entity, 3(10)), a bare "must" not done (every "The body must have ..." paragraph and every "must" of Part 1: one line each), "listed in Schedule N" (Schedule 11A), a duty whose "if" or "where" is unmet (6(2C), 3(7), 13(9), 20ZA, Schedule 12 paragraph 2(1)(b)), "(other than X)" (none in these ranges), and a missing event in the state ledger (none: the stable binary has no ledger).

- **F1** (sch 10 para 1(1), 1(4), 1(5), 3(9), 3(10), 5; the functions of these sub-paragraphs): Taken: NOTHING outside the limit each states in its own wording ("A supervisory body may apply", "The directions ... given or imposed under sub-paragraphs (2) and (3)", "any information to be furnished under this paragraph", "such transitional provision as ...", "at the request or with the consent of the recognised body", "Orders under this Part of this Schedule"): marginal reading (b), a grant limited by its own wording does not say no outside the limit. Other reading: JUST FALSE outside the limit. Text: "A supervisory body may apply to the Secretary of State"
- **F2** (sch 10 para 1(2), 1(6), 2(4), 2(5), 3(3), 3(4), 3(11); the functions of these sub-paragraphs (each a bare "must" in Part 1)): Taken: JUST FALSE when the duty is not done or the thing is not in the order or notice (a bare "must" not done: case-by-case ruling of 2026-11-05). In 1(6) the guidance limb bites only if the applicant has issued guidance ("a copy of any guidance issued"). Other reading: NOTHING (a bare "must" not done does not itself say "no"). Text: "Any such application must be—; Every application must be accompanied by—; he must give the applicant a written notice; A recognition order must state the date; the Secretary of State must—"
- **F3** (sch 10 para 1(3); `sch 10 para 1(3) the Secretary of State may require the applicant to furnish additional information` (and `sch 11 para 1(4)`)): Taken: JUST FALSE outside the period "after receiving an application and before determining it" (a period the text fixes in its own words: ruling of 2026-11-05 (a)). Other reading: NOTHING. Text: "At any time after receiving an application and before determining it"
- **F4** (sch 10 para 2(1); `sch 10 para 2(1) the Secretary of State may make or refuse to make a recognition order`): Taken: JUST FALSE when the application is not "duly made in accordance with paragraph 1" or the information has not been furnished: "on an application ... and after being furnished" is read as a "where"/"upon" condition (2026-11-05 ruling (b) and (c)). Other reading: NOTHING (a power limited in its own wording). Text: "on an application duly made in accordance with paragraph 1 and after being furnished with all such information as he may require"
- **F5** (sch 10 para 2(3); `sch 10 para 2(3) the Secretary of State may refuse to make a recognition order`): Taken: NOTHING when the three facts are not all present: "may refuse ... if he considers" names a power limited by an "if" that the text does not close with "only", and nothing in paragraph 2 says a refusal may be made on no other ground (the Guide, section 5, "In short": a grant limited in its own wording gives NOTHING outside the limit). Other reading: JUST FALSE, a failed "if" read as the text's own no (marginal reading (a)). Text: "The Secretary of State may refuse to make a recognition order in respect of a body if he considers that its recognition is unnecessary"
- **F6** (sch 10 para 3(1); `sch 10 para 3(1) the Secretary of State may revoke the recognition order`): Taken: NOTHING when no limb holds, or the requirement or obligation relates to a delegated task: "may be revoked ... if at any time it appears to him" names a power limited by an "if" that the text does not close with "only"; the other routes (3(1A), 3(8), 3(10)) are separate functions, so none of them says another is closed. Other reading: JUST FALSE, a failed "if" read as the text's own no (marginal reading (a)). Text: "may be revoked by a further order made by the Secretary of State if at any time it appears to him"
- **F7** (sch 10 para 3(1A); `sch 10 para 3(1A) the Secretary of State may revoke the recognition order`): Taken: NOTHING when no task delegated to the body has been reclaimed, or continued recognition does not appear to the Secretary of State to be undesirable: "may be revoked ... if at any time" names a power limited by an "if" that the text does not close with "only". Other reading: JUST FALSE, a failed "if" read as the text's own no (marginal reading (a)). Text: "may be revoked by a further order made by the Secretary of State if at any time"
- **F8** (sch 10 para 3(2), 3(5), 6(3), 9(1A), 10C(3), 13(3)(b)(ii), 13(5), sch 11 para 3(2), 3(5); `sch 10 para 3(2) the first day after a period of months beginning with a date` (the helper, used by every month-counted period)): Taken: "the period of N months beginning with [a date]" includes the date itself and ends the day before the corresponding date N months later (1 January: three months end 31 March); where the corresponding date does not exist (30 November plus three months: no 30 February) the period ends on the last day of that month, so the first day after it is 1 March. The Act says nothing about month-ends and the Interpretation Act 1978 is outside the sources, so the corresponding-date rule is assumed. Other reading: a period that ends a fixed number of days later (90 days), or a month-end that rolls over into the next month (30 November plus three months as 2 March). Text: "the period of three months beginning with the date of service or publication of the notice"
- **F9** (sch 10 para 3(2); `sch 10 para 3(2) the revocation order states a valid date of effect`): Taken: JUST FALSE when no date is stated or the date is not after the three months: "must state ... which must be after" is a flat "must"; the exceptions in 3(8) (public interest) and 3(10) (consent) are separate functions and are not folded in. Other reading: a function that also takes the 3(8) and 3(10) exceptions as inputs and answers JUST TRUE where either applies. Text: "which must be after the period of three months beginning with the date on which the revocation order is made"
- **F10** (sch 10 para 3(5), sch 11 para 3(5) (seat); the seat questions `Under schedule 10 paragraph 3(5), ...`, `Under schedule 11 paragraph 3(5), ...`): Taken: a longer period allowed by the Secretary of State is a date input (the last day of the longer period); the seat asks "Has the Secretary of State allowed a longer period?" and passes JUST of the date or NOTHING. Other reading: asking for a number of months. Text: "or such longer period as the Secretary of State may allow"
- **F11** (sch 10 para 3(6); `sch 10 para 3(6) the person is within this sub-paragraph` (and `sch 11 para 3(6)`)): Taken: JUST FALSE when the person is neither the body, a member, nor a person who appears to the Secretary of State to be affected: the list is closed by the catch-all (c) "any other person who appears to the Secretary of State to be affected". Other reading: NOTHING (a list introduced by "are" without "only"). Text: "The persons within this sub-paragraph are—"
- **F12** (sch 10 para 3(7); `sch 10 para 3(7) the Secretary of State has had regard to the representations` (and `sch 11 para 3(7)`)): Taken: NOTHING when no representations were made in accordance with (5): the duty exists only for "any representations made" (a duty whose condition is unmet: case-by-case ruling of 2026-11-05). Other reading: JUST TRUE (nothing to have regard to) or JUST FALSE. Text: "must have regard to any representations made in accordance with sub-paragraph (5)"
- **F13** (sch 10 para 3(8); `sch 10 para 3(8) the Secretary of State may revoke without regard to the restriction in sub-paragraph (2)`): Taken: NOTHING when the Secretary of State does not consider revocation essential in the public interest: "If in any case ... he may revoke ... without regard to the restriction" names a power limited by an "if" that the text does not close with "only"; whether the restriction in sub-paragraph (2) then applies is the answer of another function. Other reading: JUST FALSE, a failed "if" read as the text's own no (marginal reading (a)). Text: "If in any case the Secretary of State considers it essential to do so in the public interest he may revoke a recognition order without regard to the restriction"
- **F14** (sch 10 para 4, sch 11 para 4; `sch 10 para 4 the order has effect ...`; `sch 11 para 4 ...`): Taken: NOTHING when the order was not made under the old provision or was revoked: "A recognition order made and not revoked under" limits the transitional rule in its own wording. Other reading: JUST FALSE. Text: "A recognition order made and not revoked under—"
- **F15** (sch 10 para 5A; sch 10 para 5A the body meets the requirement): Taken: JUST FALSE when a limb that applies is not met: "must" is read as the condition the paragraph states, and the paragraph is a requirement for recognition (para 2(2)(a), 3(1)(a)). Other reading: NOTHING: a bare "must" not done does not itself say "no" (2026-11-05 case-by-case ruling). Text: "The body (“B”) must have rules providing that"
- **F16** (sch 10 para 5B; sch 10 para 5B the body meets the requirement): Taken: JUST FALSE when a limb that applies is not met: "must" is read as the condition the paragraph states, and the paragraph is a requirement for recognition (para 2(2)(a), 3(1)(a)). Other reading: NOTHING: a bare "must" not done does not itself say "no" (2026-11-05 case-by-case ruling). Text: "The body must consult with the competent authority and with other recognised supervisory bodies"
- **F17** (sch 10 para 6(1); sch 10 para 6(1) the person is not eligible ... under the rule the body must have): Taken: the function states what the rule the body must have says about the person: JUST TRUE (not eligible) when no "unless" limb holds, JUST FALSE when one holds ("unless": the text says no to the bar), NOTHING when (1A) or para 7 is unknown. Meeting a limb does not make the person eligible (the rule is only a necessary condition), so there is no "is eligible" answer. Other reading: an "is eligible" function answering JUST TRUE when a limb holds (reads "unless" as sufficient) or NOTHING (reads it as necessary only, which is the same information the other way round). Text: "a person is not eligible for appointment as a statutory auditor unless"
- **F18** (sch 10 para 6(1A); sch 10 para 6(1A) the requirements of this sub-paragraph are met): Taken: JUST FALSE when no limb holds: "The requirements of this sub-paragraph are that" is a definition by "are that" read as closed (marginal reading (a)). Other reading: NOTHING (another route to eligibility may exist outside the sub-paragraph). Text: "The requirements of this sub-paragraph are that"
- **F19** (sch 10 para 6(2C); sch 10 para 6(2C) the body meets the requirements for the adaptation period; 6(2C)(b)): Taken: NOTHING when the rules do not specify a requirement that may or must be met by an adaptation period (a duty whose "where" is unmet: no requirement arises, the text says nothing more). Other reading: JUST FALSE under the 2026-11-05 periods ruling (b) ("where" fails: JUST FALSE for that provision). Text: "Where the body’s rules specify a requirement that may or must be met by completing an adaptation period"
- **F20** (sch 10 para 6(3); sch 10 para 6(3) the firm may be permitted to remain eligible ...): Taken: the three months run from the date the firm ceased to comply (the text names no starting day: "for a period of not more than three months"); JUST FALSE after the period (periods ruling (a)). Other reading: the period starts when the firm is permitted to remain (the permission date); a firm not within the opening words answers NOTHING. Text: "A firm which has ceased to comply with the conditions mentioned in sub-paragraph (1)(b) may be permitted to remain eligible for appointment as a statutory auditor for a period of not more than three months"
- **F21** (sch 10 para 7(1); (inert)): Taken: inert under reason 1: it says what the paragraph explains ("This paragraph explains what is meant in paragraph 6(1)(b) by a firm being controlled by qualified persons") and creates no rule of its own; the rule is 7(3). Other reading: an operative signpost returning JUST TRUE. Text: "This paragraph explains what is meant in paragraph 6(1)(b) by a firm being “controlled by qualified persons”."
- **F22** (sch 10 para 7(2), 7(4), 7(5); sch 10 para 7(2) the person is qualified; 7(4); 7(5)): Taken: JUST FALSE when no limb holds: "references ... are" and "means" are read as closed definitions; "a majority of the rights to vote" is more than half (0.5 is not a majority). Other reading: NOTHING for 7(2) (a list introduced by "are" without "only"); "majority" as at least half. Text: "In this paragraph references to a person being qualified are—"
- **F23** (sch 10 para 7A(1); sch 10 para 7A(1) the body meets the requirement): Taken: JUST FALSE when a limb that applies is not met: "must" is read as the condition the paragraph states, and the paragraph is a requirement for recognition (para 2(2)(a), 3(1)(a)). Other reading: NOTHING: a bare "must" not done does not itself say "no" (2026-11-05 case-by-case ruling). Text: "The body must have rules and practices governing the adaptation period and the ability assessment"
- **F24** (sch 10 para 7A(2); sch 10 para 7A(2) the body meets the requirement): Taken: JUST FALSE when a limb that applies is not met: "must" is read as the condition the paragraph states, and the paragraph is a requirement for recognition (para 2(2)(a), 3(1)(a)). Other reading: NOTHING: a bare "must" not done does not itself say "no" (2026-11-05 case-by-case ruling). Text: "The body must have regard to the circumstances of each applicant"
- **F25** (sch 10 para 7A(4); sch 10 para 7A(4) the body meets the requirement): Taken: JUST FALSE when a limb that applies is not met: "must" is read as the condition the paragraph states, and the paragraph is a requirement for recognition (para 2(2)(a), 3(1)(a)). Other reading: NOTHING: a bare "must" not done does not itself say "no" (2026-11-05 case-by-case ruling). Text: "The applicant’s performance during the adaptation period must be assessed by the body"
- **F26** (sch 10 para 7A(5); sch 10 para 7A(5) the body meets the requirement): Taken: JUST FALSE when a limb that applies is not met: "must" is read as the condition the paragraph states, and the paragraph is a requirement for recognition (para 2(2)(a), 3(1)(a)). Other reading: NOTHING: a bare "must" not done does not itself say "no" (2026-11-05 case-by-case ruling). Text: "The body must determine the applicant’s professional status during the adaptation period"
- **F27** (sch 10 para 8(1); sch 10 para 8(1) the body meets the requirement): Taken: JUST FALSE when a limb that applies is not met: "must" is read as the condition the paragraph states, and the paragraph is a requirement for recognition (para 2(2)(a), 3(1)(a)). Other reading: NOTHING: a bare "must" not done does not itself say "no" (2026-11-05 case-by-case ruling). Text: "The body must have adequate rules and practices designed to ensure that the persons eligible under its rules for appointment as a statutory auditor are fit and proper persons"
- **F28** (sch 10 para 8(2); sch 10 para 8(2) the matters the body may take into account must include ...): Taken: NOTHING for a person outside the listed relations ("must include" is not closed), and NOTHING for a relation that belongs to the other kind of person ("in the case of a body corporate", "in the case of a partnership"). Other reading: JUST FALSE for a person outside the list. Text: "The matters which the body may take into account for this purpose in relation to a person must include—"
- **F29** (sch 10 para 9(1); sch 10 para 9(1) the body meets the requirement): Taken: JUST FALSE when a limb that applies is not met: "must" is read as the condition the paragraph states, and the paragraph is a requirement for recognition (para 2(2)(a), 3(1)(a)). Other reading: NOTHING: a bare "must" not done does not itself say "no" (2026-11-05 case-by-case ruling). Text: "The body must have adequate rules and practices designed to ensure that"
- **F30** (sch 10 para 9(1A); sch 10 para 9(1A) the rules of the body must bar the appointment (and the helper `sch 10 para 9(1A) the bar on appointment is in force on the day`)): Taken: within the one-year minimum JUST TRUE; after it NOTHING (the standards of the competent authority, outside the sources, decide), unless the standards period is supplied and has not run out; a public interest entity answers JUST FALSE ("except where": the sub-paragraph does not apply and 10C(3) does). Other reading: JUST FALSE after the first year (a period the text fixes in its own words, periods ruling (a)); the "except where" met answers NOTHING. Text: "during a period of not less than one year determined in standards set by the competent authority and commencing on the date on which the individual’s appointment as a statutory auditor ended"
- **F31** (sch 10 para 9(3)(b); sch 10 para 9(3)(b) the body meets the requirement): Taken: JUST FALSE when the body lacks the rules ("must also have"). Other reading: NOTHING (a bare "must" not done). Text: "The body must also have adequate rules and practices designed to ensure that"
- **F32** (sch 10 para 9(3A); sch 10 para 9(3A) the body meets the requirement): Taken: JUST FALSE when a limb that applies is not met: "must" is read as the condition the paragraph states, and the paragraph is a requirement for recognition (para 2(2)(a), 3(1)(a)). Other reading: NOTHING: a bare "must" not done does not itself say "no" (2026-11-05 case-by-case ruling). Text: "The rules and practices mentioned in sub-paragraphs (1) and (3) must include provision requiring compliance with standards"
- **F33** (sch 10 para 9(4); sch 10 para 9(4) the body meets the requirement that the rules apply to former members): Taken: JUST FALSE when a limb that applies is not met: "must" is read as the condition the paragraph states, and the paragraph is a requirement for recognition (para 2(2)(a), 3(1)(a)). Other reading: NOTHING: a bare "must" not done does not itself say "no" (2026-11-05 case-by-case ruling). Text: "The rules referred to in sub-paragraphs (1A) and (3)(b) must apply to persons who are no longer members of the body as they apply to members"
- **F34** (sch 10 para 10(1); sch 10 para 10(1) the body meets the requirement): Taken: JUST FALSE when a limb that applies is not met: "must" is read as the condition the paragraph states, and the paragraph is a requirement for recognition (para 2(2)(a), 3(1)(a)). Other reading: NOTHING: a bare "must" not done does not itself say "no" (2026-11-05 case-by-case ruling). Text: "The body must have rules and practices as to"
- **F35** (sch 10 para 10(2); sch 10 para 10(2) the body meets the requirement): Taken: JUST FALSE when a limb that applies is not met: "must" is read as the condition the paragraph states, and the paragraph is a requirement for recognition (para 2(2)(a), 3(1)(a)). Other reading: NOTHING: a bare "must" not done does not itself say "no" (2026-11-05 case-by-case ruling). Text: "The rules and practices mentioned in sub-paragraph (1) must include provision requiring compliance"
- **F36** (sch 10 para 10A(1); sch 10 para 10A(1) the body meets the requirement): Taken: JUST FALSE when a limb that applies is not met: "must" is read as the condition the paragraph states, and the paragraph is a requirement for recognition (para 2(2)(a), 3(1)(a)). Other reading: NOTHING: a bare "must" not done does not itself say "no" (2026-11-05 case-by-case ruling). Text: "The body must have rules and practices as to technical standards ensuring that group auditors"
- **F37** (sch 10 para 10A(2); sch 10 para 10A(2) the body meets the requirement): Taken: JUST FALSE when a limb that applies is not met: "must" is read as the condition the paragraph states, and the paragraph is a requirement for recognition (para 2(2)(a), 3(1)(a)). Other reading: NOTHING: a bare "must" not done does not itself say "no" (2026-11-05 case-by-case ruling). Text: "The rules and practices mentioned in sub-paragraph (1) must include provision requiring compliance"
- **F38** (sch 10 para 10A(3); sch 10 para 10A(3) the body meets the requirement): Taken: JUST FALSE when a limb that applies is not met: "must" is read as the condition the paragraph states, and the paragraph is a requirement for recognition (para 2(2)(a), 3(1)(a)). Other reading: NOTHING: a bare "must" not done does not itself say "no" (2026-11-05 case-by-case ruling). Text: "The body must have rules and practices ensuring that group auditors retain copies"
- **F39** (sch 10 para 10C(4); sch 10 para 10C(4) the body meets the requirement that the rules apply to former members): Taken: JUST FALSE when a limb that applies is not met: "must" is read as the condition the paragraph states, and the paragraph is a requirement for recognition (para 2(2)(a), 3(1)(a)). Other reading: NOTHING: a bare "must" not done does not itself say "no" (2026-11-05 case-by-case ruling). Text: "The rules referred to in sub-paragraph (3) must apply to persons who are no longer members of the body as they apply to members"
- **F40** (sch 10 para 11; sch 10 para 11 the body meets the requirement): Taken: JUST FALSE when a limb that applies is not met: "must" is read as the condition the paragraph states, and the paragraph is a requirement for recognition (para 2(2)(a), 3(1)(a)). Other reading: NOTHING: a bare "must" not done does not itself say "no" (2026-11-05 case-by-case ruling). Text: "The body must have rules and practices designed to ensure that persons eligible for appointment as statutory auditors take part in appropriate programmes of continuing education"
- **F41** (sch 10 para 12(1); sch 10 para 12(1) the body meets the requirement): Taken: JUST FALSE when a limb that applies is not met: "must" is read as the condition the paragraph states, and the paragraph is a requirement for recognition (para 2(2)(a), 3(1)(a)). Other reading: NOTHING: a bare "must" not done does not itself say "no" (2026-11-05 case-by-case ruling). Text: "The body must"
- **F42** (sch 10 para 12(1A); sch 10 para 12(1A) the body meets the requirement): Taken: JUST FALSE when a limb that applies is not met: "must" is read as the condition the paragraph states, and the paragraph is a requirement for recognition (para 2(2)(a), 3(1)(a)). Other reading: NOTHING: a bare "must" not done does not itself say "no" (2026-11-05 case-by-case ruling). Text: "The body must"
- **F43** (sch 10 para 12(2); sch 10 para 12(2) the body meets the requirement): Taken: JUST FALSE when a limb that applies is not met: "must" is read as the condition the paragraph states, and the paragraph is a requirement for recognition (para 2(2)(a), 3(1)(a)). Other reading: NOTHING: a bare "must" not done does not itself say "no" (2026-11-05 case-by-case ruling). Text: "The arrangements for monitoring must make provision for that function to be performed by the competent authority"
- **F44** (sch 10 para 12(3)(a); sch 10 para 12(3)(a) the body meets the requirement): Taken: JUST FALSE when a limb that applies is not met: "must" is read as the condition the paragraph states, and the paragraph is a requirement for recognition (para 2(2)(a), 3(1)(a)). Other reading: NOTHING: a bare "must" not done does not itself say "no" (2026-11-05 case-by-case ruling). Text: "The arrangements for enforcement must make provision for that function to be performed by the competent authority"
- **F45** (sch 10 para 12(3)(b); sch 10 para 12(3)(b) the body meets the requirement): Taken: JUST FALSE when a limb that applies is not met: "must" is read as the condition the paragraph states, and the paragraph is a requirement for recognition (para 2(2)(a), 3(1)(a)). Other reading: NOTHING: a bare "must" not done does not itself say "no" (2026-11-05 case-by-case ruling). Text: "The arrangements for enforcement must include provision for sanctions which include"
- **F46** (sch 10 para 12(3)(c); sch 10 para 12(3)(c) the body meets the requirement): Taken: JUST FALSE when a limb that applies is not met: "must" is read as the condition the paragraph states, and the paragraph is a requirement for recognition (para 2(2)(a), 3(1)(a)). Other reading: NOTHING: a bare "must" not done does not itself say "no" (2026-11-05 case-by-case ruling). Text: "The arrangements for enforcement must include provision for the body to make available to the public information"
- **F47** (sch 10 para 12(4); sch 10 para 12(4) the body meets the requirement that the sanctions apply to former members): Taken: JUST FALSE when a limb that applies is not met: "must" is read as the condition the paragraph states, and the paragraph is a requirement for recognition (para 2(2)(a), 3(1)(a)). Other reading: NOTHING: a bare "must" not done does not itself say "no" (2026-11-05 case-by-case ruling). Text: "The sanctions referred to in sub-paragraph (3)(b)(v) must apply to persons who are no longer members of the body as they apply to members"
- **F48** (sch 10 para 12(6); sch 10 para 12(6) the identity of the person sanctioned must not be made available to the public): Taken: JUST FALSE when none of (a) to (d) holds: 12(5)(b) requires the identity "unless any of the circumstances mentioned in sub-paragraph (6) applies", so outside them the text does not bar publication (marginal reading (a): an "unless"). Other reading: NOTHING: "are" followed by a list with no "only". Text: "The circumstances in which the identity of the person sanctioned must not be made available to the public are—"
- **F49** (sch 10 para 12(7); sch 10 para 12(7) the information must be published on the website of the body on the day): Taken: JUST TRUE on every day after the relevant date up to and including its fifth anniversary; NOTHING otherwise (before the relevant date the text is silent; after five years "a proportionate period" is undefined). Other reading: JUST FALSE after the fifth anniversary (period fixed in its own words, periods ruling (a)); but the sub-paragraph also says "for a proportionate period", which the text does not fix. Text: "must be published on the body’s website for at least five years after the relevant date"
- **F50** (sch 10 para 13(1); sch 10 para 13(1) the body meets the requirement): Taken: JUST FALSE when a limb that applies is not met: "must" is read as the condition the paragraph states, and the paragraph is a requirement for recognition (para 2(2)(a), 3(1)(a)); a limb whose "where"/"in the case of" gate is unmet does not bite (counts as met), the other limbs still decide. Other reading: NOTHING: a bare "must" not done does not itself say "no" (2026-11-05 case-by-case ruling); for a gate unmet, NOTHING or JUST FALSE for that limb. Text: "The body must—"
- **F51** (sch 10 para 13(3)(a); sch 10 para 13(3)(a) the body meets the requirement): Taken: JUST FALSE when a limb that applies is not met: "must" is read as the condition the paragraph states, and the paragraph is a requirement for recognition (para 2(2)(a), 3(1)(a)). Other reading: NOTHING: a bare "must" not done does not itself say "no" (2026-11-05 case-by-case ruling). Text: "The arrangements referred to in sub-paragraph (1)(a) must make provision for inspections to be conducted by the competent authority"
- **F52** (sch 10 para 13(3)(b)(i); sch 10 para 13(3)(b)(i) the arrangements meet the requirement): Taken: JUST FALSE when a limb that applies is not met: "must" is read as the condition the paragraph states, and the paragraph is a requirement for recognition (para 2(2)(a), 3(1)(a)). Other reading: NOTHING: a bare "must" not done does not itself say "no" (2026-11-05 case-by-case ruling). Text: "The arrangements referred to in sub-paragraph (1)(a) must include an inspection which is conducted in relation to each person eligible for appointment as a statutory auditor"
- **F53** (sch 10 para 13(3)(b)(ii); sch 10 para 13(3)(b)(ii) another inspection of the person is due by the day asked about): Taken: a person who has audited an entity not subject to the small companies regime in the previous five years: JUST TRUE once six years (72 months) have run from the previous inspection (the day six years on is included); JUST FALSE before that; NOTHING for any other person ("in the case of a person who"). Other reading: NOTHING after the six years (the text sets a minimum frequency, it does not say what happens on the day). Text: "at least once every six years in the case of a person who, during any of the previous five years, has carried out a statutory audit of an entity not subject to the small companies regime"
- **F54** (sch 10 para 13(5)(e); sch 10 para 13(5) the inspector is a person by whom the inspection may be conducted): Taken: "for at least three years before the inspection": the inspection date must be on or after the day three years on from the day the association last existed (1 June 2023 allows 1 June 2026). Other reading: the day after the association ended counts as the first day of the three years (a one-day difference). Text: "have not been an employee or partner or member of the management body of the person subject to inspection and have not been otherwise associated with that person for at least three years before the inspection"
- **F55** (sch 10 para 13(7); sch 10 para 13(7) the body meets the requirement): Taken: JUST FALSE when a limb that applies is not met: "must" is read as the condition the paragraph states, and the paragraph is a requirement for recognition (para 2(2)(a), 3(1)(a)); a limb whose "where"/"in the case of" gate is unmet does not bite (counts as met), the other limbs still decide. Other reading: NOTHING: a bare "must" not done does not itself say "no" (2026-11-05 case-by-case ruling); for a gate unmet, NOTHING or JUST FALSE for that limb. Text: "The inspection must include an assessment of"
- **F56** (sch 10 para 13(8); sch 10 para 13(8) the body meets the requirement): Taken: JUST FALSE when a limb that applies is not met: "must" is read as the condition the paragraph states, and the paragraph is a requirement for recognition (para 2(2)(a), 3(1)(a)). Other reading: NOTHING: a bare "must" not done does not itself say "no" (2026-11-05 case-by-case ruling). Text: "The inspection must be appropriate and proportionate"
- **F57** (sch 10 para 13(9); sch 10 para 13(9) the body has taken account of the proportionality of the standards): Taken: JUST TRUE or JUST FALSE for an undertaking that qualifies as small or medium sized (any of the four seam answers JUST TRUE); NOTHING for an undertaking that does not (the duty is limited to those undertakings) and when no seam says it does and the others are unknown. Other reading: JUST FALSE for an undertaking that is neither small nor medium sized (a duty whose "where" is unmet). Text: "Where undertaking inspections of statutory audits of undertakings that qualify as small (see sections 382 and 383) or medium sized (see sections 465 and 466) the body must take account"
- **F58** (sch 10 para 13(10); sch 10 para 13(10) the inspection of the firm may be treated as an inspection of all individuals responsible): Taken: NOTHING when the inspection is not conducted in relation to a firm or the firm has no common quality assurance policy that each responsible individual is required to comply with: "may be treated as an inspection of all individuals ..., if the firm has a common quality assurance policy" names a permission limited by an "if" that the text does not close with "only" (the Guide, section 5, "In short": a grant limited in its own wording gives NOTHING outside the limit). Other reading: JUST FALSE, a failed "if" read as the text's own no (marginal reading (a)). Text: "An inspection conducted in relation to a firm may be treated as an inspection of all individuals responsible for statutory audit work on behalf of that firm, if the firm has a common quality assurance policy"
- **F59** (sch 10 para 13(11); sch 10 para 13(11) the body meets the requirement): Taken: JUST FALSE when a limb that applies is not met: "must" is read as the condition the paragraph states, and the paragraph is a requirement for recognition (para 2(2)(a), 3(1)(a)). Other reading: NOTHING: a bare "must" not done does not itself say "no" (2026-11-05 case-by-case ruling). Text: "The main conclusions of the inspection must be recorded in a report which is made available to"
- **F60** (sch 10 para 13(12); sch 10 para 13(12) the body has complied for the calendar year): Taken: JUST FALSE when a limb that applies is not met: "must" is read as the condition the paragraph states, and the paragraph is a requirement for recognition (para 2(2)(a), 3(1)(a)). Other reading: NOTHING: a bare "must" not done does not itself say "no" (2026-11-05 case-by-case ruling). Text: "The body must, at least once in every calendar year, deliver to the Secretary of State a summary of the results of inspections"
- **F61** (sch 10 para 14; sch 10 para 14 the body meets the requirement): Taken: JUST FALSE when a limb that applies is not met: "must" is read as the condition the paragraph states, and the paragraph is a requirement for recognition (para 2(2)(a), 3(1)(a)); a limb whose "where"/"in the case of" gate is unmet does not bite (counts as met), the other limbs still decide. Other reading: NOTHING: a bare "must" not done does not itself say "no" (2026-11-05 case-by-case ruling); for a gate unmet, NOTHING or JUST FALSE for that limb. Text: "must be fair and reasonable and include adequate provision for appeals"
- **F62** (sch 10 para 15(1); sch 10 para 15(1) the body meets the requirement): Taken: JUST FALSE when a limb that applies is not met: "must" is read as the condition the paragraph states, and the paragraph is a requirement for recognition (para 2(2)(a), 3(1)(a)). Other reading: NOTHING: a bare "must" not done does not itself say "no" (2026-11-05 case-by-case ruling). Text: "The body must have effective arrangements for the investigation of complaints against"
- **F63** (sch 10 para 15(2); sch 10 para 15(2) the body meets the requirement): Taken: JUST FALSE when a limb that applies is not met: "must" is read as the condition the paragraph states, and the paragraph is a requirement for recognition (para 2(2)(a), 3(1)(a)). Other reading: NOTHING: a bare "must" not done does not itself say "no" (2026-11-05 case-by-case ruling). Text: "The arrangements mentioned in sub-paragraph (1) must make provision for the whole or part of the function of investigating those complaints to be performed by the competent authority"
- **F64** (sch 10 para 16(1); sch 10 para 16(1) the body meets the requirement): Taken: JUST FALSE when a limb that applies is not met: "must" is read as the condition the paragraph states, and the paragraph is a requirement for recognition (para 2(2)(a), 3(1)(a)); a limb whose "where"/"in the case of" gate is unmet does not bite (counts as met), the other limbs still decide. Other reading: NOTHING: a bare "must" not done does not itself say "no" (2026-11-05 case-by-case ruling); for a gate unmet, NOTHING or JUST FALSE for that limb. Text: "The body must have rules and practices designed to ensure that, where the competent authority has decided that any particular enforcement action should be taken against a member of the body"
- **F65** (sch 10 para 16(2); sch 10 para 16(2) the body meets the requirement): Taken: JUST FALSE when a limb that applies is not met: "must" is read as the condition the paragraph states, and the paragraph is a requirement for recognition (para 2(2)(a), 3(1)(a)). Other reading: NOTHING: a bare "must" not done does not itself say "no" (2026-11-05 case-by-case ruling). Text: "The body must have adequate arrangements as part of its rules and practices"
- **F66** (sch 10 para 16A(1); sch 10 para 16A(1) the body meets the requirement): Taken: JUST FALSE when a limb that applies is not met: "must" is read as the condition the paragraph states, and the paragraph is a requirement for recognition (para 2(2)(a), 3(1)(a)). Other reading: NOTHING: a bare "must" not done does not itself say "no" (2026-11-05 case-by-case ruling). Text: "The body must have adequate rules and practices designed to ensure that a person eligible under its rules for appointment as a statutory auditor transfers audit working papers and investigation reports to a third country competent authority only in accordance with"
- **F67** (sch 10 para 16A(1); sch 10 para 16A(1) the person may transfer ... (requirement function: `sch 10 para 16A(1) the body meets the requirement`)): Taken: the person may transfer only in accordance with 16AA or 16AB: JUST TRUE if either is met, JUST FALSE if both are known unmet, NOTHING otherwise (seams unknown). Other reading: NOTHING when neither is met ("only in accordance with" read as a flat negative only for the body, not the person). Text: "only in accordance with the requirements of"
- **F68** (sch 10 para 16A(2); sch 10 para 16A(2) the body meets the requirement that the person must refuse): Taken: JUST FALSE when a limb that applies is not met: "must" is read as the condition the paragraph states, and the paragraph is a requirement for recognition (para 2(2)(a), 3(1)(a)). Other reading: NOTHING: a bare "must" not done does not itself say "no" (2026-11-05 case-by-case ruling). Text: "The body must also have adequate rules and practices designed to ensure that"
- **F69** (sch 10 para 17(1); sch 10 para 17(1) the body meets the requirement): Taken: JUST FALSE when a limb that applies is not met: "must" is read as the condition the paragraph states, and the paragraph is a requirement for recognition (para 2(2)(a), 3(1)(a)). Other reading: NOTHING: a bare "must" not done does not itself say "no" (2026-11-05 case-by-case ruling). Text: "The body must have adequate rules or arrangements designed to ensure that persons eligible under its rules for appointment as a statutory auditor take such steps"
- **F70** (sch 10 para 18; sch 10 para 18 the body meets the requirement): Taken: JUST FALSE when a limb that applies is not met: "must" is read as the condition the paragraph states, and the paragraph is a requirement for recognition (para 2(2)(a), 3(1)(a)). Other reading: NOTHING: a bare "must" not done does not itself say "no" (2026-11-05 case-by-case ruling). Text: "The body must have rules requiring persons eligible under its rules for appointment as a statutory auditor to comply with any obligations imposed on them by"
- **F71** (sch 10 para 19; sch 10 para 19 the body meets the requirement): Taken: JUST FALSE when a limb that applies is not met: "must" is read as the condition the paragraph states, and the paragraph is a requirement for recognition (para 2(2)(a), 3(1)(a)). Other reading: NOTHING: a bare "must" not done does not itself say "no" (2026-11-05 case-by-case ruling). Text: "The body must have satisfactory arrangements for taking account, in framing its rules, of the cost"
- **F72** (sch 10 para 20; sch 10 para 20 the body meets the requirement): Taken: JUST FALSE when a limb that applies is not met: "must" is read as the condition the paragraph states, and the paragraph is a requirement for recognition (para 2(2)(a), 3(1)(a)). Other reading: NOTHING: a bare "must" not done does not itself say "no" (2026-11-05 case-by-case ruling). Text: "The body must be able and willing"
- **F73** (sch 10 para 20ZA; sch 10 para 20ZA the body has paid the costs it must pay): Taken: NOTHING when the paragraph does not apply (no delegation, other costs, an auditor not bound by the rules of B): "This paragraph applies where" limits the duty; JUST FALSE when it applies and the costs are unpaid ("must pay"). Other reading: JUST FALSE where the delegation condition fails (2026-11-05 periods ruling (b): a "where" condition fails). Text: "B must pay the costs incurred by"
- **F74** (sch 10 para 20A(1) terms; "key audit partner", "public interest entity", "EEA auditor", "EEA competent authority", "specified state auditor", "statutory audit function", "third country audit function", "the Audit Directive"): Taken: each "means" definition answers JUST FALSE when no limb holds (a closed definition); the borrowed terms ("audit reporting requirements", "issuer", "specified state") are inputs of type MAYBE BOOLEAN passed through. Other reading: NOTHING for a "means" definition whose own limbs refer to instruments outside the sources. Text: "“ key audit partner ” means—"
- **F75** (sch 11 para 3(1); sch 11 para 3(1) the Secretary of State may revoke the recognition order): Taken: NOTHING when neither ground appears to the Secretary of State to be made out: "may be revoked ... if at any time it appears to him" names a power limited by an "if" that the text does not close with "only" (the Guide, section 5, "In short": a grant limited in its own wording gives NOTHING outside the limit). Other reading: JUST FALSE, a failed "if" read as the text's own no (marginal reading (a)). Text: "may be revoked by a further order made by the Secretary of State if at any time it appears to him"
- **F76** (sch 11 para 3(5), 3(6); sch 11 para 3(5) the person may make written and oral representations; para 3(6)): Taken: as Schedule 10 para 3(5): the three months begin with the date of service or publication and are inclusive of it; JUST FALSE outside the period or the longer period (periods ruling (a)); a person not within (6) answers NOTHING. Other reading: JUST FALSE for a person not within (6). Text: "A person within sub-paragraph (6) may, within the period of three months beginning with the date of service or publication or such longer period as the Secretary of State may allow, make written representations"
- **F77** (sch 11 para 3(8); sch 11 para 3(8) the Secretary of State may revoke without regard to the restriction in sub-paragraph (2)): Taken: NOTHING when the Secretary of State does not consider revocation essential in the public interest: "If in any case ... he may revoke ... without regard to the restriction" names a power limited by an "if" that the text does not close with "only"; whether the restriction in sub-paragraph (2) then applies is the answer of another function. Other reading: JUST FALSE, a failed "if" read as the text's own no (marginal reading (a)). Text: "If in any case the Secretary of State considers it essential to do so in the public interest he may revoke a recognition order without regard to the restriction"
- **F78** (sch 11 para 6(4), 7(2); sch 11 para 6(4) the person has a sufficient period of professional experience; sch 11 para 7): Taken: "not less than seven years' experience in a professional capacity in the fields of finance, law and accountancy" is read as seven years of professional experience across those fields together (one NUMBER input), not seven years in each field. Other reading: seven years in each of the three fields. Text: "not less than seven years' experience in a professional capacity in the fields of finance, law and accountancy"
- **F79** (sch 11 para 9(2); sch 11 para 9(2) the work is statutory audit work): Taken: NOTHING for work that is neither statutory audit work nor foreign audit work meeting the similar-law test ("includes" does not close the list). Other reading: JUST FALSE. Text: "“statutory audit work” includes the work of a person appointed as the auditor of a person under the law of a country or territory outside the United Kingdom"
- **F80** (sch 11 para 9(4); sch 11 para 9(4) at least two-thirds of the training ...): Taken: two-thirds is tested as 3 x (months by eligible persons) at least 2 x (total months); the (4A)(b) alternative is the months given by a person eligible outside the United Kingdom with the (4A) conditions met. Other reading: the (4A) conditions asked of each trainer rather than of the months. Text: "At least two-thirds of the training must be given by a person"
- **F81** (sch 11 para 10(1); sch 11 para 10(1) the years of professional experience required after the deduction): Taken: a NUMBER of years: seven less the years of qualifying instruction, at most four; no deduction when the instruction did not last a year or is not attested ("provided"); the instruction years are the total qualifying years. Other reading: the proviso applying period by period (each period of instruction of at least one year counts separately). Text: "Periods of theoretical instruction in the fields of finance, law and accountancy may be deducted from the required period of professional experience, provided the instruction"
- **F82** (sch 11 para 11(1); sch 11 para 11(1) the body meets the requirement): Taken: JUST FALSE when a limb that applies is not met: "must" is read as the condition the paragraph states, and the paragraph is a requirement for recognition (para 2(2)(a), 3(1)(a)). Other reading: NOTHING: a bare "must" not done does not itself say "no" (2026-11-05 case-by-case ruling). Text: "The body offering the qualification must have"
- **F83** (sch 11 para 11(2); sch 11 para 11(2) the arrangements meet the requirement): Taken: JUST FALSE when a limb that applies is not met: "must" is read as the condition the paragraph states, and the paragraph is a requirement for recognition (para 2(2)(a), 3(1)(a)). Other reading: NOTHING: a bare "must" not done does not itself say "no" (2026-11-05 case-by-case ruling). Text: "The arrangements must include arrangements for monitoring"
- **F84** (sch 11A part 1, part 2; `sch 11A part 1 the person is a specified person`; `sch 11A part 2 the disclosure is of a specified description`): Taken: JUST TRUE for each listed person or description; NOTHING for any person or purpose that no paragraph names, because the Schedule lists without closing the list in its own words (section 1224A, coa26, is where "only to specified persons" would be stated; it is outside this range). Other reading: JUST FALSE for an unlisted person or purpose (a definition handed to a list: 2026-11-05 ruling (a)), which is right if section 1224A says disclosure is allowed only to the listed. Text: "Specified persons / Specified descriptions of disclosures"
- **F85** (sch 11A para 62; `sch 11A part 2 the disclosure is of a specified description` (para 62 arm)): Taken: JUST FALSE when the information made available identifies an audited person ("provided such information does not identify any audited person": a proviso met by its negative). Other reading: NOTHING (a proviso not met leaves the paragraph silent). Text: "provided such information does not identify any audited person"
- **F86** (sch 11A para 79; `sch 11A para 79 the disclosure is made in accordance with this Part of this Schedule`): Taken: JUST FALSE when the disclosure is not made to an approved third country competent authority or section 1253B is known unmet ("A disclosure is made in accordance with this Part of this Schedule if it is made ..."): marginal reading (a), a failed "if" counts as no, within the provision. Other reading: NOTHING (para 80 or another provision may bring the disclosure within the Part). Text: "A disclosure is made in accordance with this Part of this Schedule if it is made to an approved third country competent authority"
- **F87** (sch 11A para 80; `sch 11A para 80 the disclosure is made in accordance with this Part of this Schedule`): Taken: JUST FALSE when neither limb holds (marginal reading (a)); the limbs are (a) a transfer of papers in accordance with the 16A rules, (b) a disclosure other than such a transfer made to a third country competent authority to enable or assist its functions. Other reading: NOTHING. Text: "A disclosure is made in accordance with this Part of this Schedule if it is—"
- **F88** (sch 12 para 1(1), 2(1); `sch 12 para 1(1) the arrangements are appropriate arrangements`; `sch 12 para 2(1) ...`): Taken: JUST FALSE when a limb fails: "are appropriate arrangements—" is a definition by "are", read as closed; the hearing limbs of 2(1)(b) bite only "where it appears to be desirable following the conclusion of such investigations" (gate unmet: the limbs do not bite). Other reading: NOTHING (a list introduced by "are" without "only"). Text: "The arrangements referred to in section 1242(1)(a) are appropriate arrangements—"
- **F89** (sch 12 para 3(2); `sch 12 para 3(2) the arrangements are not to be regarded as appropriate for ensuring independence`): Taken: states what the paragraph says about the arrangements: JUST TRUE when either limb is not designed in; JUST FALSE when both are ("not ... unless"); para 3(3) says the minimum may need more, so JUST FALSE here does not make the arrangements appropriate. Other reading: an "are appropriate" function (NOTHING when both limbs hold). Text: "Arrangements are not to be regarded as appropriate for the purpose of ensuring that a thing is done independently of the registered third country auditor unless they are designed to ensure that"
- **F90** (sch 12 para 6(2); (inert)): Taken: inert under reason 2: an order specifying the arrangements is subject to negative resolution procedure (a statement about how an order is made). Other reading: operative. Text: "An order under sub-paragraph (1) is subject to negative resolution procedure."
- **F91** (sch 13 para 1(1); `sch 13 para 1(1) the paragraph has effect in relation to the body`): Taken: JUST TRUE when the paragraph number is within the range the text gives for the kind of body, JUST FALSE otherwise ("has effect ... as follows" is read as closed). Other reading: NOTHING for a paragraph outside the ranges. Text: "This Schedule has effect in relation to a body designated by a delegation order as follows"
- **F92** (sch 13 para 4(1), 4(3); `sch 13 para 4(1) the body has paid what it must pay ...`; `... 4(3)`): Taken: the amount is the Secretary of State's determination (an input, MAYBE NUMBER; NOTHING when not made); paying at least the amount is JUST TRUE, less is JUST FALSE ("must pay"). Other reading: a function that returns the amount owed. Text: "such remuneration ... as the Secretary of State may determine"
- **F93** (sch 13 para 8(2); `sch 13 para 8(2) this paragraph gives a defence to the alleged contravention`): Taken: JUST FALSE when the person does not show that the instrument had not been made available: "this paragraph gives no defence on these facts" (2026-11-05 ruling (b), never "no defence at all"). Other reading: NOTHING. Text: "A person is not to be taken to have contravened any regulation or order if he shows that"
- **F94** (sch 13 para 10(1); sch 13 para 10(1) the body has complied for the calendar year): Taken: JUST FALSE when a limb that applies is not met: "must" is read as the condition the paragraph states, and the paragraph is a requirement for recognition (para 2(2)(a), 3(1)(a)). Other reading: NOTHING: a bare "must" not done does not itself say "no" (2026-11-05 case-by-case ruling). Text: "The body must, at least once in each calendar year for which the delegation order is in force, make a report to the Secretary of State on"
- **F95** (seat layer, all questions; the 43 questions of `coa30-seat.l4`): Taken: the individuals in the seat are, for these Schedules, the people who deal with a company as its statutory auditor or a would-be auditor (including a firm, a key audit partner and a third country auditor), the holder or student of a recognised professional qualification, a member or employee of the delegated body, a person who holds information obtained under Part 42, and a director who asks about the company's auditor (assumed, not ruled). Other reading: a seat only for the director, secretary and member of the company, which would leave almost every paragraph of these Schedules without a question. Text: "a company ... or who deals with one"
- **F96** (sch 11A heading and "Section 1224A" line, Parts 1-3 headings; (inert)): Taken: inert under reason 1: the title and the Part headings are not operative. Other reading: none. Text: "SCHEDULE 11A — Specified persons, descriptions, disclosures etc for the purposes of section 1224A"
- **F97** (sch 13 paras 3, 5, 7(3), 11(2)-(4), 12; (inert)): Taken: inert under reason 2: the body's name, members, chairman (para 3), its proceedings (para 5), the powers to make orders on consultation (7(3)), transitional provision on the transfer or resumption of a function (11(2) to (4)) and on revocation (12) are boards, offices, staffing and order-making powers. Other reading: operative (a person who sits on the body has a claim under paragraph 4, which is encoded). Text: "The body is to be known by such name as may be specified in the delegation order."

### Listed, not flipped: grants whose gate is "after ...", "on ..." or "with the consent of ..." (name-test sweep of 2026-11-12)

Assumed, not ruled: these equivalents of "where", "when" and "upon" go with the listed group. Ruling (b) of the Guide's "Periods, "where" and scope limits" paragraph (and ruling (c) of the 2026-11-05 delegated ruling) says `JUST FALSE`, and the Guide's line on grants (section 5, "In short": "limits a grant or prohibition in its own wording and the case falls outside the limit") says `NOTHING`, so the choice is a question for the maintainer or a lawyer, not one the sweep settles. Each function below answers `JUST FALSE` when its gate is unmet; the other reading is `NOTHING` (a grant limited in its own wording, so the case outside the gate is not covered). One row per function; the rows are not in the marginal readings.

| function | the gate in the text | text line | note |
| --- | --- | --- | --- |
| `sch 10 para 1(3) the Secretary of State may require the applicant to furnish additional information` | "At any time after receiving an application and before determining it" | 20025 |  |
| `sch 10 para 2(1) the Secretary of State may make or refuse to make a recognition order` | "on an application duly made in accordance with paragraph 1 and after being furnished with all such information as he may require under that paragraph" | 20037 |  |
| `sch 11 para 1(4) the Secretary of State may require the applicant to furnish additional information` | "At any time after receiving an application and before determining it" | 20409 |  |
| `sch 11 para 2(1) the Secretary of State may make or refuse to make a recognition order` | "on an application duly made in accordance with paragraph 1 and after being furnished with all such information as he may require under that paragraph" | 20427 |  |
| `sch 13 para 6(6) the Secretary of State may by order vary or revoke regulations prescribing fees` | "after consultation with the body" | 20732 |  |
| `sch 13 para 10(5) the Secretary of State may give directions about the accounts and the audit of the accounts` | "with the consent of the Treasury" (assumed, not ruled, to go with "after ..." and "on ...") | 20756 | The function also answers JUST FALSE when the body is not established by the order; that limb is closed by "apply only where the body is established by the order" and is not part of what is listed. |
| `sch 13 para 10(7) the Secretary of State may give directions about the accounts and the audit of the accounts` | "with the consent of the Treasury" (assumed, not ruled, to go with "after ..." and "on ...") | 20758 | The "Unless the body is a company to which section 394 applies" and "existing body" limbs already answer NOTHING; only the Treasury-consent branch answers JUST FALSE. |

### Name-test sweep of 2026-11-12

The sweep sorted every layer-1 function whose name contains "may", "permitted", "power", "entitled" or "authorised" (50 functions; a seat question answers what the function it calls answers, so the seat layer was not swept). The test is what the text puts between the grant and the act. A function named for a grant (a power, a permission) whose gate is a bare "if" that the text does not close with "only" answers `NOTHING` outside the gate, with one fork line and one marginal-reading row each, and the other reading, `JUST FALSE` (a failed "if" read as the text's own no), is named in both. "Only if", "must only", "must not ... any other", a flat "must", a period the text fixes in its own words and a requirement that is not itself a grant keep `JUST FALSE`. A gate of "after ...", "on ..." or "with the consent of ..." is listed above and not flipped. No function of this part has "entitled" in its name.

| flipped to NOTHING | kept JUST FALSE (gate closed by the text) | listed: "may" with where/when/upon | listed: "entitled" |
| --- | --- | --- | --- |
| 7 | 12 | 7 | 0 |

Flipped to NOTHING (7): `sch 10 para 2(3) the Secretary of State may refuse to make a recognition order`; `sch 10 para 3(1) the Secretary of State may revoke the recognition order`; `sch 10 para 3(1A) the Secretary of State may revoke the recognition order`; `sch 10 para 3(8) the Secretary of State may revoke without regard to the restriction in sub-paragraph (2)`; `sch 10 para 13(10) the inspection of the firm may be treated as an inspection of all individuals responsible`; `sch 11 para 3(1) the Secretary of State may revoke the recognition order`; `sch 11 para 3(8) the Secretary of State may revoke without regard to the restriction in sub-paragraph (2)`.

Kept `JUST FALSE`, gate closed by the text (12): `sch 10 para 2(2) the Secretary of State may make a recognition order` ("may make a recognition order only if"); `sch 10 para 3(5) the person may make written and oral representations` (a period the text fixes in its own words ("within the period of three months beginning with ..."), periods ruling (a), already forked); `sch 10 para 6(2) the aptitude test may test the person's knowledge of the matter` ("(c) must not test the person's knowledge of any other matters"); `sch 10 para 6(3) the firm may be permitted to remain eligible for appointment as a statutory auditor` ("for a period of not more than three months", periods ruling (a), already forked); `sch 10 para 13(5) the inspector is a person by whom the inspection may be conducted` ("The inspection must be conducted by persons who" (a flat "must")); `sch 10 para 16A(1) the person may transfer audit working papers and investigation reports to the third country competent authority` ("may be made only in accordance with"); `sch 11 para 2(2) the Secretary of State may make a recognition order` ("may make a recognition order only if"); `sch 11 para 3(5) the person may make written and oral representations` (a period the text fixes in its own words, periods ruling (a), already forked); `sch 11 para 6(1) the qualification may be open to the person` ("must only be open to persons who"); `sch 11 para 7 the qualification may be restricted to the person` ("must be restricted to persons who"); `sch 13 para 6(5) the exercise of the power to prescribe fees has the approval required` ("requires the approval of the Secretary of State": a requirement, not a function named for a grant (its "power" is the thing that needs approval)); `sch 13 para 10(6) the person may be appointed as auditor of the body` ("may only be appointed ... if").

Listed, "may" with where/when/upon (7): `sch 10 para 1(3) the Secretary of State may require the applicant to furnish additional information`; `sch 10 para 2(1) the Secretary of State may make or refuse to make a recognition order`; `sch 11 para 1(4) the Secretary of State may require the applicant to furnish additional information`; `sch 11 para 2(1) the Secretary of State may make or refuse to make a recognition order`; `sch 13 para 6(6) the Secretary of State may by order vary or revoke regulations prescribing fees`; `sch 13 para 10(5) the Secretary of State may give directions about the accounts and the audit of the accounts`; `sch 13 para 10(7) the Secretary of State may give directions about the accounts and the audit of the accounts`.

Listed, "entitled" (0): none.

The other 24 functions with such a name answer only `JUST TRUE` or `NOTHING` (the build script checks that none has a `JUST FALSE` answer), so there is nothing to sort: `sch 10 para 1(1)`; `sch 10 para 1(4)`; `sch 10 para 1(5)`; `sch 10 para 3(9)`; `sch 10 para 6(2C)(b)`; `sch 10 para 7A(3)`; `sch 10 para 8(2)`; `sch 11 para 1(1)`; `sch 11 para 1(5)`; `sch 11 para 1(6)`; `sch 11 para 1(7)`; `sch 11 para 3(9)`; `sch 11 para 6(3)`; `sch 11 para 8(2)`; `sch 11 para 8(3)`; `sch 12 para 2(1A)`; `sch 12 para 3(3)`; `sch 12 para 5`; `sch 13 para 1(3)`; `sch 13 para 6(1)`; `sch 13 para 9(3)`; `sch 13 para 10(2)`; `sch 13 para 10(8)`; `sch 13 para 13(2)`.

The one seat question that calls a flipped function is `Under schedule 10 paragraph 13(10), may the inspection of my firm be treated as an inspection of me as an individual responsible for its audit work`; it answers `NOTHING` where its function does. The 14 layer-1 assertions and the 1 seat case that the flips changed are restated in place in their test and case modules, each under a `-- RECONCILED 2026-11-12: was ...` comment.

## Jural relations (coa30)

Hohfeld's correlatives, stated once per provision as a relation between two parties and named neutrally. Most paragraphs of Part 2 of Schedule 10 are conditions of recognition: the Secretary of State holds the power to refuse or revoke recognition if the condition is not met (paragraphs 2(2)(a) and 3(1)(a)) and the body bears the liability; the correlative duty (to have the rule, arrangement or practice) is the body's. Where the text requires the body's rules to give a person something (a fair hearing and appeal, a debt owed to the body, an inspector who has not been associated with the person for three years) the person and the body are named in the row. Where the text does not name who benefits (the bar on a former auditor joining the board, the information the body must publish) the row says "not named". A limb (a), (b) or a roman sub-limb has the relation of the paragraph or sub-paragraph row that holds it and is not repeated (the coverage table above has a row for each limb and names the same function). A definition or counting rule creates no relation and is `none`. The rule column gives the function; Schedules 14, 15 and 16 are amendments of other Acts and create no relation in this text.

| provision | holder of the right, privilege, power or immunity | bearer of the duty, no-right, liability or disability | L4 rule |
| --- | --- | --- | --- |
| sch 10 heading | none | none | (inert) |
| sch 10 section reference | none | none | (inert) |
| sch 10 part 1 heading | none | none | (inert) |
| sch 10 cross-heading (line 20020) "Application for recognition of supervisory body" | none | none | (inert) |
| sch 10 para 1(1) | the supervisory body (power to apply) | the Secretary of State (liability: an application may be made to him) | `sch 10 para 1(1) the body may apply to the Secretary of State for a recognition order` |
| sch 10 para 1(2) | the Secretary of State (claim) | the applicant (duty: make and accompany the application as required) | `sch 10 para 1(2) the application is made and accompanied as required` |
| sch 10 para 1(3) | the Secretary of State (power) | the applicant (liability) | `sch 10 para 1(3) the Secretary of State may require the applicant to furnish additional information` |
| sch 10 para 1(4) | the Secretary of State (privilege to differ) | the applicant (no-right) | `sch 10 para 1(4) the directions and requirements may differ as between different applications` |
| sch 10 para 1(5) | the Secretary of State (power) | the applicant (liability) | `sch 10 para 1(5) the Secretary of State may specify the form or manner of verification` |
| sch 10 para 1(6) | the Secretary of State (claim) | the applicant (duty: make and accompany the application as required) | `sch 10 para 1(6) the application is accompanied as required` |
| sch 10 para 1(7) | none | none | `sch 10 para 1(7) the guidance is guidance issued by the applicant` |
| sch 10 cross-heading (line 20036) "Grant and refusal of recognition" | none | none | (inert) |
| sch 10 para 2(1) | the Secretary of State (power to make or refuse a recognition order) | the applicant body (liability) | `sch 10 para 2(1) the Secretary of State may make or refuse to make a recognition order` |
| sch 10 para 2(2) | the Secretary of State (power to make or refuse a recognition order) | the applicant body (liability) | `sch 10 para 2(2) the Secretary of State may make a recognition order` |
| sch 10 para 2(3) | the Secretary of State (power to make or refuse a recognition order) | the applicant body (liability) | `sch 10 para 2(3) the Secretary of State may refuse to make a recognition order` |
| sch 10 para 2(4) | the applicant body (claim to a written notice of refusal) | the Secretary of State (duty) | `sch 10 para 2(4) the Secretary of State`; `sch 10 para 2(4) the recognised supervisory body` |
| sch 10 para 2(5) | none | none | `sch 10 para 2(5) the recognition order is made as required` |
| sch 10 cross-heading (line 20049) "Revocation of recognition" | none | none | (inert) |
| sch 10 para 3(1) | the Secretary of State (power to revoke) | the recognised body (liability) | `sch 10 para 3(1) the Secretary of State may revoke the recognition order` |
| sch 10 para 3(1A) | the Secretary of State (power to revoke) | the recognised body (liability) | `sch 10 para 3(1A) the Secretary of State may revoke the recognition order` |
| sch 10 para 3(2) | the recognised body and its members (immunity from an earlier date of effect) | the Secretary of State (disability) | `sch 10 para 3(2) the first day after a period of months beginning with a date`; `sch 10 para 3(2) the revocation order states a valid date of effect` |
| sch 10 para 3(3) | the recognised body, its members and persons affected (claim to notice) | the Secretary of State (duty) | `sch 10 para 3(3) the duties before revoking`; `sch 10 para 3(3) the Secretary of State has done what he must do before revoking` |
| sch 10 para 3(4) | the recognised body, its members and persons affected (claim to notice) | the Secretary of State (duty) | `sch 10 para 3(4) the notice has the contents required` |
| sch 10 para 3(5) | a person within sub-paragraph (6) (privilege to make representations) | the Secretary of State (no-right) | `sch 10 para 3(5) make written or oral representations`; `sch 10 para 3(5) the permission to make representations` |
| sch 10 para 3(6) | none | none | `sch 10 para 3(6) the person is within this sub-paragraph` |
| sch 10 para 3(7) | a person who made representations (claim that regard is had to them) | the Secretary of State (duty) | `sch 10 para 3(7) the Secretary of State has had regard to the representations` |
| sch 10 para 3(8) | the Secretary of State (power to revoke) | the recognised body (liability) | `sch 10 para 3(8) the Secretary of State may revoke without regard to the restriction in sub-paragraph (2)` |
| sch 10 para 3(9) | the Secretary of State (power to revoke) | the recognised body (liability) | `sch 10 para 3(9) the revocation order may contain the transitional provision` |
| sch 10 para 3(10) | the Secretary of State (immunity from the restrictions where the body requests or consents) | the recognised body (no-right) | `sch 10 para 3(10) the revocation is not subject to the restrictions and requirements listed` |
| sch 10 para 3(11) | the recognised body, its members and persons affected (claim to notice) | the Secretary of State (duty) | `sch 10 para 3(11) the duties on making the order`; `sch 10 para 3(11) the Secretary of State has done what he must do on making the revocation order` |
| sch 10 cross-heading (line 20082) "Transitional provision" | none | none | (inert) |
| sch 10 para 4 | none | none | `sch 10 para 4 the order has effect after commencement as an order made under paragraph 2(1) of this Schedule` |
| sch 10 cross-heading (line 20087) "Orders not statutory instruments" | none | none | (inert) |
| sch 10 para 5 | none | none | `sch 10 para 5 the order is to be made by statutory instrument` |
| sch 10 part 2 heading | none | none | (inert) |
| sch 10 cross-heading (line 20090) "Delegation etc. of tasks by competent authority" | none | none | (inert) |
| sch 10 para 5A | the Secretary of State (power to refuse or revoke recognition if the requirement is not met: paras 2(2)(a), 3(1)(a)) | the body (liability; the requirement is the body's duty) | `sch 10 para 5A the body meets the requirement` |
| sch 10 cross-heading (line 20095) "Consultation" | none | none | (inert) |
| sch 10 para 5B | the Secretary of State (power to refuse or revoke recognition if the requirement is not met: paras 2(2)(a), 3(1)(a)) | the body (liability; the requirement is the body's duty) | `sch 10 para 5B the body meets the requirement` |
| sch 10 cross-heading (line 20097) "Holding of appropriate qualification" | none | none | (inert) |
| sch 10 para 6(1) | the recognised supervisory body (power, under its rules, to treat a person as not eligible) | the person (liability) | `sch 10 para 6(1) the person is not eligible for appointment as a statutory auditor under the rule the body must have` |
| sch 10 para 6(1A) | the recognised supervisory body (power, under its rules, to treat a person as not eligible) | the person (liability) | `sch 10 para 6(1A) the requirements of this sub-paragraph are met` |
| sch 10 para 6(1B) | the recognised supervisory body (power, under its rules, to treat a person as not eligible) | the person (liability) | `sch 10 para 6(1B) another requirement`; `sch 10 para 6(1B) the rules of the body specify one of the requirements listed` |
| sch 10 para 6(2) | the person taking the aptitude test (claim that only the permitted matters are tested) | the body (duty) | `sch 10 para 6(2) the aptitude test may test the person's knowledge of the matter` |
| sch 10 para 6(2A) | none | none | (blank) |
| sch 10 para 6(2B) | none | none | `sch 10 para 6(2B) the period is an adaptation period` |
| sch 10 para 6(2C) | none | none | `sch 10 para 6(2C) the body meets the requirements for the adaptation period` |
| sch 10 para 6(3) | the body (power to permit a firm to remain eligible for up to three months) | the firm (liability: no longer eligible after the period) | `sch 10 para 6(3) the firm may be permitted to remain eligible for appointment as a statutory auditor` |
| sch 10 para 7(1) | none | none | (inert) |
| sch 10 para 7(2) | none | none | `sch 10 para 7(2) the person is qualified` |
| sch 10 para 7(3) | none | none | `sch 10 para 7(3) the firm is controlled by qualified persons` |
| sch 10 para 7(4) | none | none | `sch 10 para 7(4) the qualified members are a majority of the members of the firm` |
| sch 10 para 7(5) | none | none | `sch 10 para 7(5) the qualified members are a majority of the members of the management body of the firm` |
| sch 10 para 7(6) | none | none | `sch 10 para 7(6) paragraphs 5 to 11 of Schedule 7 apply to the counting of rights` |
| sch 10 para 7A(1) | the Secretary of State (power to refuse or revoke recognition if the requirement is not met: paras 2(2)(a), 3(1)(a)) | the body (liability; the requirement is the body's duty) | `sch 10 para 7A(1) the body meets the requirement` |
| sch 10 para 7A(2) | the Secretary of State (power to refuse or revoke recognition if the requirement is not met: paras 2(2)(a), 3(1)(a)) | the body (liability; the requirement is the body's duty) | `sch 10 para 7A(2) the body meets the requirement` |
| sch 10 para 7A(3) | the body (power to require further training) | the applicant (liability) | `sch 10 para 7A(3) the applicant may be required to undergo further training during the adaptation period` |
| sch 10 para 7A(4) | the Secretary of State (power to refuse or revoke recognition if the requirement is not met: paras 2(2)(a), 3(1)(a)) | the body (liability; the requirement is the body's duty) | `sch 10 para 7A(4) the body meets the requirement` |
| sch 10 para 7A(5) | none | none | `sch 10 para 7A(5) the body meets the requirement` |
| sch 10 cross-heading (line 20159) "Auditors to be fit and proper persons" | none | none | (inert) |
| sch 10 para 8(1) | the Secretary of State (power to refuse or revoke recognition if the requirement is not met: paras 2(2)(a), 3(1)(a)) | the body (liability; the requirement is the body's duty) | `sch 10 para 8(1) the body meets the requirement` |
| sch 10 para 8(2) | the body (privilege to take the matters into account) | the person assessed (no-right) | `sch 10 para 8(2) any other person`; `sch 10 para 8(2) the matters the body may take into account must include a matter relating to this person` |
| sch 10 para 8(3) | none | none | `sch 10 para 8(3) director is to be read as member in sub-paragraph (2)(b)` |
| sch 10 para 8(4) | none | none | `sch 10 para 8(4) the person is a controller of the body corporate` |
| sch 10 cross-heading (line 20174) "Professional integrity and independence" | none | none | (inert) |
| sch 10 para 9(1) | the Secretary of State (power to refuse or revoke recognition if the requirement is not met: paras 2(2)(a), 3(1)(a)) | the body (liability; the requirement is the body's duty) | `sch 10 para 9(1) the body meets the requirement` |
| sch 10 para 9(1A) | not named in the text (the bar protects the audited person) | the former auditor or key audit partner (disability: may not be appointed within the period) | `sch 10 para 9(1A) the rules of the body must bar the appointment`; `sch 10 para 9(1A) the bar on appointment is in force on the day` |
| sch 10 para 9(2) | none | none | (blank) |
| sch 10 para 9(3) | the Secretary of State (power to refuse or revoke recognition if the requirement is not met: paras 2(2)(a), 3(1)(a)) | the body (liability; the requirement is the body's duty) | `sch 10 para 9(3)(b) the body meets the requirement` |
| sch 10 para 9(3A) | the Secretary of State (power to refuse or revoke recognition if the requirement is not met: paras 2(2)(a), 3(1)(a)) | the body (liability; the requirement is the body's duty) | `sch 10 para 9(3A) the body meets the requirement` |
| sch 10 para 9(4) | the supervisory body (claim: a fine is a debt due to it) | the person obliged to pay it (duty) | `sch 10 para 9(4) the body meets the requirement that the rules apply to former members`; `sch 10 para 9(4) the fine is recoverable by the body as a debt due to it from the person obliged to pay it` |
| sch 10 para 9(5) | the auditor (immunity from being treated as an officer for the bar) | the body and the audited person (disability) | `sch 10 para 9(5) the auditor is regarded as an officer of the audited person for the purposes of sub-paragraph (1A)(a) and (b)` |
| sch 10 cross-heading (line 20192) "Technical standards" | none | none | (inert) |
| sch 10 para 10(1) | the Secretary of State (power to refuse or revoke recognition if the requirement is not met: paras 2(2)(a), 3(1)(a)) | the body (liability; the requirement is the body's duty) | `sch 10 para 10(1) the body meets the requirement` |
| sch 10 para 10(2) | the Secretary of State (power to refuse or revoke recognition if the requirement is not met: paras 2(2)(a), 3(1)(a)) | the body (liability; the requirement is the body's duty) | `sch 10 para 10(2) the body meets the requirement` |
| sch 10 cross-heading (line 20197) "Technical standards for group audits" | none | none | (inert) |
| sch 10 para 10A(1) | the Secretary of State (power to refuse or revoke recognition if the requirement is not met: paras 2(2)(a), 3(1)(a)) | the body (liability; the requirement is the body's duty) | `sch 10 para 10A(1) the body meets the requirement` |
| sch 10 para 10A(2) | the Secretary of State (power to refuse or revoke recognition if the requirement is not met: paras 2(2)(a), 3(1)(a)) | the body (liability; the requirement is the body's duty) | `sch 10 para 10A(2) the body meets the requirement` |
| sch 10 para 10A(3) | the Secretary of State (power to refuse or revoke recognition if the requirement is not met: paras 2(2)(a), 3(1)(a)) | the body (liability; the requirement is the body's duty) | `sch 10 para 10A(3) the body meets the requirement` |
| sch 10 para 10A(4) | none | none | (blank) |
| sch 10 para 10A(5) | none | none | (blank) |
| sch 10 para 10A(6) | none | none | (blank) |
| sch 10 para 10A(7) | none | none | `sch 10 para 10A(7) the person is a group auditor` (+1) |
| sch 10 para 10A(7) term "group auditor" | none | none | `sch 10 para 10A(7) the person is a group auditor` |
| sch 10 para 10A(7) term "group" | none | none | `sch 10 para 10A(7) the companies form a group` |
| sch 10 cross-heading (line 20209) "Public interest entity reporting requirements" | none | none | (inert) |
| sch 10 para 10B | none | none | (blank) |
| sch 10 cross-heading (line 20211) "Public interest entity independence requirements" | none | none | (inert) |
| sch 10 para 10C(1) | none | none | (blank) |
| sch 10 para 10C(2) | none | none | (blank) |
| sch 10 para 10C(3) | not named in the text (the bar protects the audited person) | the former auditor or key audit partner (disability: may not be appointed within the period) | `sch 10 para 10C(3) the rules of the body must bar the appointment` |
| sch 10 para 10C(4) | the supervisory body (claim: a fine is a debt due to it) | the person obliged to pay it (duty) | `sch 10 para 10C(4) the body meets the requirement that the rules apply to former members`; `sch 10 para 10C(4) the fine is recoverable by the body as a debt due to it from the person obliged to pay it` |
| sch 10 para 10C(5) | the auditor (immunity from being treated as an officer for the bar) | the body and the audited person (disability) | `sch 10 para 10C(5) the auditor is regarded as an officer of the entity for the purposes of sub-paragraph (3)(a) and (b)` |
| sch 10 para 10C(6) | none | none | (blank) |
| sch 10 cross-heading (line 20220) "Procedures for maintaining competence" | none | none | (inert) |
| sch 10 para 11 | the Secretary of State (power to refuse or revoke recognition if the requirement is not met: paras 2(2)(a), 3(1)(a)) | the body (liability; the requirement is the body's duty) | `sch 10 para 11 the body meets the requirement` |
| sch 10 cross-heading (line 20222) "Monitoring and enforcement" | none | none | (inert) |
| sch 10 para 12(1) | the Secretary of State (power to refuse or revoke recognition if the requirement is not met: paras 2(2)(a), 3(1)(a)) | the body (liability; the requirement is the body's duty) | `sch 10 para 12(1) the body meets the requirement` |
| sch 10 para 12(1A) | the Secretary of State (power to refuse or revoke recognition if the requirement is not met: paras 2(2)(a), 3(1)(a)) | the body (liability; the requirement is the body's duty) | `sch 10 para 12(1A) the body meets the requirement` |
| sch 10 para 12(2) | the Secretary of State (power to refuse or revoke recognition if the requirement is not met: paras 2(2)(a), 3(1)(a)) | the body (liability; the requirement is the body's duty) | `sch 10 para 12(2) the body meets the requirement` |
| sch 10 para 12(3) | none | none | `sch 10 para 12(3)(a) the body meets the requirement` (+2) |
| sch 10 para 12(4) | the body (power to impose the sanctions) | its members and former members (liability) | `sch 10 para 12(4) the body meets the requirement that the sanctions apply to former members`; `sch 10 para 12(4) the sanction applies to the person as it applies to members` |
| sch 10 para 12(5) | the public (not named in the text) | the body (duty to make the information available) | `sch 10 para 12(5) the information made available to the public includes what it must include` |
| sch 10 para 12(6) | the person sanctioned (claim that identity is not made public in the four cases) | the body (duty) | `sch 10 para 12(6) the identity of the person sanctioned must not be made available to the public` |
| sch 10 para 12(7) | the public (not named in the text) | the body (duty to make the information available) | `sch 10 para 12(7) the information must be published on the website of the body on the day` |
| sch 10 para 12(8) | the public (not named in the text) | the body (duty to make the information available) | `sch 10 para 12(8) the relevant date` |
| sch 10 cross-heading (line 20257) "Monitoring of audits" | none | none | (inert) |
| sch 10 para 13(1) | the body (power to inspect its members) | its members (liability to inspection) | `sch 10 para 13(1) the body meets the requirement` |
| sch 10 para 13(2) | none | none | `sch 10 para 13(2) the monitoring is regarded as monitoring of compliance with the rules of the body for the purposes of paragraph 12(1) and (1A)` |
| sch 10 para 13(3) | the body (power to inspect its members) | its members (liability to inspection) | `sch 10 para 13(3)(a) the body meets the requirement`; `sch 10 para 13(3)(b)(i) the arrangements meet the requirement` |
| sch 10 para 13(4) | the body (power to inspect its members) | its members (liability to inspection) | `sch 10 para 13(4) the arrangements meet the requirement` |
| sch 10 para 13(5) | the body (power to inspect its members) | its members (liability to inspection) | `sch 10 para 13(5) the inspector is a person by whom the inspection may be conducted` |
| sch 10 para 13(6) | the body (power to inspect its members) | its members (liability to inspection) | `sch 10 para 13(6) the inspection meets the requirement` |
| sch 10 para 13(7) | the body (power to inspect its members) | its members (liability to inspection) | `sch 10 para 13(7) the body meets the requirement` |
| sch 10 para 13(8) | the body (power to inspect its members) | its members (liability to inspection) | `sch 10 para 13(8) the body meets the requirement` |
| sch 10 para 13(9) | the body (power to inspect its members) | its members (liability to inspection) | `sch 10 para 13(9) the body has taken account of the proportionality of the standards` |
| sch 10 para 13(10) | the body (power to inspect its members) | its members (liability to inspection) | `sch 10 para 13(10) the inspection of the firm may be treated as an inspection of all individuals responsible` |
| sch 10 para 13(11) | the person to whom the inspection relates (claim to the report) | the body (duty) | `sch 10 para 13(11) the body meets the requirement` |
| sch 10 para 13(12) | the Secretary of State (claim to an annual summary) | the body (duty) | `sch 10 para 13(12) deliver to the Secretary of State a summary of the results of inspections`; `sch 10 para 13(12) the annual summary` |
| sch 10 cross-heading (line 20298) "Membership, eligibility and enforcement" | none | none | (inert) |
| sch 10 para 14 | members of the body and persons affected (not named: claim to fair and reasonable rules and appeals) | the body (duty) | `sch 10 para 14 the body meets the requirement` |
| sch 10 cross-heading (line 20304) "Investigation of complaints" | none | none | (inert) |
| sch 10 para 15(1) | complainants (not named: claim to effective arrangements) | the body (duty) | `sch 10 para 15(1) the body meets the requirement` |
| sch 10 para 15(2) | complainants (not named: claim to effective arrangements) | the body (duty) | `sch 10 para 15(2) the body meets the requirement` |
| sch 10 cross-heading (line 20309) "Independent investigation for enforcement purposes" | none | none | (inert) |
| sch 10 para 16(1) | the Secretary of State (power to refuse or revoke recognition if the requirement is not met: paras 2(2)(a), 3(1)(a)) | the body (liability; the requirement is the body's duty) | `sch 10 para 16(1) the body meets the requirement` |
| sch 10 para 16(2) | the Secretary of State (power to refuse or revoke recognition if the requirement is not met: paras 2(2)(a), 3(1)(a)) | the body (liability; the requirement is the body's duty) | `sch 10 para 16(2) the body meets the requirement` |
| sch 10 para 16(3) | the Secretary of State (power to refuse or revoke recognition if the requirement is not met: paras 2(2)(a), 3(1)(a)) | the body (liability; the requirement is the body's duty) | `sch 10 para 16(3) the matter is a non-delegated case` |
| sch 10 cross-heading (line 20316) "Transfer of papers to third countries" | none | none | (inert) |
| sch 10 para 16A(1) | the Secretary of State (claim that papers go only as 16AA or 16AB allows) | the person eligible for appointment as a statutory auditor (duty) | `sch 10 para 16A(1) the body meets the requirement`; `sch 10 para 16A(1) the person may transfer audit working papers and investigation reports to the third country competent authority` |
| sch 10 para 16A(2) | the Secretary of State (claim that the person refuses when directed) | the person eligible for appointment (duty) | `sch 10 para 16A(2) the person must refuse to transfer audit working papers and investigation reports to the third country competent authority`; `sch 10 para 16A(2) the body meets the requirement that the person must refuse` |
| sch 10 cross-heading (line 20321) "Transfer to approved third country competent authority" | none | none | (inert) |
| sch 10 para 16AA | none | none | `sch 10 para 16AA the requirements of this paragraph are met` |
| sch 10 cross-heading (line 20325) "Transfer for purposes of investigation of auditor" | none | none | (inert) |
| sch 10 para 16AB(1) | none | none | `sch 10 para 16AB the requirements of this paragraph are met` |
| sch 10 para 16AB(2) | none | none | `sch 10 para 16AB the requirements of this paragraph are met` |
| sch 10 para 16AB(3) | none | none | `sch 10 para 16AB the requirements of this paragraph are met` |
| sch 10 para 16AB(4) | none | none | `sch 10 para 16AB the requirements of this paragraph are met` |
| sch 10 para 16AB(5) | none | none | `sch 10 para 16AB the requirements of this paragraph are met` |
| sch 10 cross-heading (line 20335) "Meeting of claims arising out of audit work" | none | none | (inert) |
| sch 10 para 17(1) | persons with claims arising out of audit work (not named) | the person eligible for appointment (duty to take steps to meet them) | `sch 10 para 17(1) the body meets the requirement` |
| sch 10 para 17(2) | the Secretary of State (power to refuse or revoke recognition if the requirement is not met: paras 2(2)(a), 3(1)(a)) | the body (liability; the requirement is the body's duty) | `sch 10 para 17(2) the person is able to meet claims arising out of statutory audit work` |
| sch 10 cross-heading (line 20338) "Register of auditors and other information to be made avail…" | none | none | (inert) |
| sch 10 para 18 | the Secretary of State (claim) | the person eligible for appointment (duty to comply with the obligations) | `sch 10 para 18 the body meets the requirement` |
| sch 10 cross-heading (line 20343) "Taking account of costs of compliance" | none | none | (inert) |
| sch 10 para 19 | the Secretary of State (power to refuse or revoke recognition if the requirement is not met: paras 2(2)(a), 3(1)(a)) | the body (liability; the requirement is the body's duty) | `sch 10 para 19 the body meets the requirement` |
| sch 10 cross-heading (line 20345) "Promotion and maintenance of standards" | none | none | (inert) |
| sch 10 para 20 | the Secretary of State (power to refuse or revoke recognition if the requirement is not met: paras 2(2)(a), 3(1)(a)) | the body (liability; the requirement is the body's duty) | `sch 10 para 20 the body meets the requirement` |
| sch 10 cross-heading (line 20349) "Supplementary: funding of arrangements" | none | none | (inert) |
| sch 10 para 20ZA(1) | the competent authority and another recognised supervisory body (claim to costs) | the body B (duty to pay) | `sch 10 para 20ZA pay the costs incurred by the competent authority or another recognised supervisory body`; `sch 10 para 20ZA the duty to pay the costs` |
| sch 10 para 20ZA(2) | the competent authority and another recognised supervisory body (claim to costs) | the body B (duty to pay) | `sch 10 para 20ZA pay the costs incurred by the competent authority or another recognised supervisory body`; `sch 10 para 20ZA the duty to pay the costs` |
| sch 10 cross-heading (line 20355) "Interpretation" | none | none | (inert) |
| sch 10 para 20A(1) | none | none | `sch 10 para 20A(1) the instrument is the Audit Directive` (+10) |
| sch 10 para 20A(1) term "the Audit Directive" | none | none | `sch 10 para 20A(1) the instrument is the Audit Directive` |
| sch 10 para 20A(1) term "audit reporting requirements" | none | none | `sch 10 para 20A(1) the requirement is one of the audit reporting requirements` |
| sch 10 para 20A(1) term "EEA auditor" | none | none | `sch 10 para 20A(1) the person is an EEA auditor` |
| sch 10 para 20A(1) term "EEA competent authority" | none | none | `sch 10 para 20A(1) the body is an EEA competent authority` |
| sch 10 para 20A(1) term "issuer" | none | none | `sch 10 para 20A(1) the person is an issuer` |
| sch 10 para 20A(1) term "key audit partner" | none | none | `sch 10 para 20A(1) the individual is a key audit partner` |
| sch 10 para 20A(1) term "public interest entity" | none | none | `sch 10 para 20A(1) the person is a public interest entity` |
| sch 10 para 20A(1) term "specified state" | none | none | `sch 10 para 20A(1) the state is a specified state` |
| sch 10 para 20A(1) term "specified state auditor" | none | none | `sch 10 para 20A(1) the person is a specified state auditor` |
| sch 10 para 20A(1) omitted text, line 20374 | none | none | (blank) |
| sch 10 para 20A(1) term "statutory audit function" | none | none | `sch 10 para 20A(1) the function is a statutory audit function` |
| sch 10 para 20A(1) term "third country audit function" | none | none | `sch 10 para 20A(1) the function is a third country audit function` |
| sch 10 para 20A(1) omitted text, line 20377 | none | none | (blank) |
| sch 10 para 20A(2) | none | none | `sch 10 para 20A(2) the territory is treated as an EEA State and subject to the Audit Directive for the purposes of this Schedule` |
| sch 10 part 3 heading | none | none | (inert) |
| sch 10 cross-heading (line 20380) "Arrangements for setting standards relating to professional…" | none | none | (inert) |
| sch 10 para 21 | none | none | (blank) |
| sch 10 cross-heading (line 20382) "Arrangements for setting technical standards" | none | none | (inert) |
| sch 10 para 22 | none | none | (blank) |
| sch 10 cross-heading (line 20384) "Arrangements for setting standards relating to public inter…" | none | none | (inert) |
| sch 10 para 22A | none | none | (blank) |
| sch 10 cross-heading (line 20386) "Arrangements for setting standards relating to public inter…" | none | none | (inert) |
| sch 10 para 22B | none | none | (blank) |
| sch 10 cross-heading (line 20388) "Arrangements for independent monitoring of audits of listed…" | none | none | (inert) |
| sch 10 para 23 | none | none | (blank) |
| sch 10 cross-heading (line 20390) "Arrangements for independent monitoring of third country au…" | none | none | (inert) |
| sch 10 para 23A | none | none | (blank) |
| sch 10 cross-heading (line 20392) "Arrangements for independent investigation for disciplinary…" | none | none | (inert) |
| sch 10 para 24 | none | none | (blank) |
| sch 10 cross-heading (line 20394) "Supplementary: arrangements to operate independently of body" | none | none | (inert) |
| sch 10 para 25 | none | none | (blank) |
| sch 10 cross-heading (line 20396) "Supplementary: funding of arrangements" | none | none | (inert) |
| sch 10 para 26 | none | none | (blank) |
| sch 10 cross-heading (line 20398) "Supplementary: scope of arrangement" | none | none | (inert) |
| sch 10 para 27 | none | none | (blank) |
| sch 11 heading | none | none | (inert) |
| sch 11 section reference | none | none | (inert) |
| sch 11 part 1 heading | none | none | (inert) |
| sch 11 cross-heading (line 20403) "Application for recognition of professional qualification" | none | none | (inert) |
| sch 11 para 1(1) | the qualifying body (power to apply) | the Secretary of State (liability) | `sch 11 para 1(1) the body may apply to the Secretary of State for a recognition order` |
| sch 11 para 1(2) | none | none | `sch 11 para 1(2) the body is a recognised qualifying body` |
| sch 11 para 1(3) | the Secretary of State (claim) | the applicant (duty) | `sch 11 para 1(3) the application is made and accompanied as required` |
| sch 11 para 1(4) | the Secretary of State (power) | the applicant (liability) | `sch 11 para 1(4) the Secretary of State may require the applicant to furnish additional information` |
| sch 11 para 1(5) | none | none | `sch 11 para 1(5) the directions and requirements may differ as between different applications` |
| sch 11 para 1(6) | the Secretary of State (power) | the applicant (liability) | `sch 11 para 1(6) the Secretary of State may specify the form or manner of verification` |
| sch 11 para 1(7) | the Secretary of State (power) | the applicant (liability) | `sch 11 para 1(7) the verification required may include independent moderation of the examinations` |
| sch 11 para 1(8) | the Secretary of State (claim) | the applicant (duty) | `sch 11 para 1(8) the application is accompanied as required` |
| sch 11 para 1(9) | none | none | `sch 11 para 1(9) the guidance is guidance issued by the applicant` |
| sch 11 para 1(10) | none | none | `sch 11 para 1(10) the matter is within this sub-paragraph` |
| sch 11 cross-heading (line 20426) "Grant and refusal of recognition" | none | none | (inert) |
| sch 11 para 2(1) | the Secretary of State (power to make or refuse) | the applicant (liability) | `sch 11 para 2(1) the Secretary of State may make or refuse to make a recognition order` |
| sch 11 para 2(2) | the Secretary of State (power to make or refuse) | the applicant (liability) | `sch 11 para 2(2) the Secretary of State may make a recognition order` |
| sch 11 para 2(3) | the applicant (claim to a written notice of refusal) | the Secretary of State (duty) | `sch 11 para 2(3) the notice of refusal is given as required` |
| sch 11 para 2(4) | none | none | `sch 11 para 2(4) the recognition order is made as required` |
| sch 11 cross-heading (line 20431) "Revocation of recognition" | none | none | (inert) |
| sch 11 para 3(1) | the Secretary of State (power to revoke) | the qualifying body (liability) | `sch 11 para 3(1) the Secretary of State may revoke the recognition order` |
| sch 11 para 3(2) | the qualifying body, holders and students (immunity from an earlier date of effect) | the Secretary of State (disability) | `sch 11 para 3(2) the revocation order states a valid date of effect` |
| sch 11 para 3(3) | the qualifying body, holders and students (claim to notice) | the Secretary of State (duty) | `sch 11 para 3(3) the Secretary of State has done what he must do before revoking` |
| sch 11 para 3(4) | the qualifying body, holders and students (claim to notice) | the Secretary of State (duty) | `sch 11 para 3(4) the notice has the contents required` |
| sch 11 para 3(5) | a person within sub-paragraph (6), including a holder of or student for the qualification (privilege to make representations) | the Secretary of State (no-right) | `sch 11 para 3(5) the person may make written and oral representations` |
| sch 11 para 3(6) | none | none | `sch 11 para 3(6) the person is within this sub-paragraph` |
| sch 11 para 3(7) | a person who made representations (claim) | the Secretary of State (duty) | `sch 11 para 3(7) the Secretary of State has had regard to the representations` |
| sch 11 para 3(8) | the Secretary of State (power to revoke) | the qualifying body (liability) | `sch 11 para 3(8) the Secretary of State may revoke without regard to the restriction in sub-paragraph (2)` |
| sch 11 para 3(9) | the Secretary of State (power to revoke) | the qualifying body (liability) | `sch 11 para 3(9) the revocation order may contain the transitional provision` |
| sch 11 para 3(10) | the Secretary of State (immunity where the body requests or consents) | the qualifying body (no-right) | `sch 11 para 3(10) the revocation is not subject to the restrictions and requirements listed` |
| sch 11 para 3(11) | the qualifying body, holders and students (claim to notice) | the Secretary of State (duty) | `sch 11 para 3(11) the Secretary of State has done what he must do on making the revocation order` |
| sch 11 cross-heading (line 20460) "Transitional provision" | none | none | (inert) |
| sch 11 para 4 | none | none | `sch 11 para 4 the order has effect after commencement as an order made under paragraph 2(1) of this Schedule` |
| sch 11 cross-heading (line 20465) "Orders not statutory instruments" | none | none | (inert) |
| sch 11 para 5 | none | none | `sch 11 para 5 the order is to be made by statutory instrument` |
| sch 11 part 2 heading | none | none | (inert) |
| sch 11 cross-heading (line 20468) "Entry requirements" | none | none | (inert) |
| sch 11 para 6(1) | the Secretary of State (power to refuse or revoke recognition if the requirement is not met) | the qualifying body (liability; the requirement is its duty) | `sch 11 para 6(1) the qualification may be open to the person` |
| sch 11 para 6(2) | the Secretary of State (power to refuse or revoke recognition if the requirement is not met) | the qualifying body (liability; the requirement is its duty) | `sch 11 para 6(2) the person has attained university entrance level` |
| sch 11 para 6(3) | the Secretary of State (power to refuse or revoke recognition if the requirement is not met) | the qualifying body (liability; the requirement is its duty) | `sch 11 para 6(3) the assessment may be conducted by the body` |
| sch 11 para 6(4) | the Secretary of State (power to refuse or revoke recognition if the requirement is not met) | the qualifying body (liability; the requirement is its duty) | `sch 11 para 6(4) the person has a sufficient period of professional experience` |
| sch 11 cross-heading (line 20481) "Requirement for theoretical instruction or professional exp…" | none | none | (inert) |
| sch 11 para 7(1) | the Secretary of State (power to refuse or revoke recognition if the requirement is not met) | the qualifying body (liability; the requirement is its duty) | `sch 11 para 7 the qualification may be restricted to the person` |
| sch 11 para 7(2) | the Secretary of State (power to refuse or revoke recognition if the requirement is not met) | the qualifying body (liability; the requirement is its duty) | `sch 11 para 7 the qualification may be restricted to the person` |
| sch 11 cross-heading (line 20486) "Examination" | none | none | (inert) |
| sch 11 para 8(1) | the Secretary of State (power to refuse or revoke recognition if the requirement is not met) | the qualifying body (liability; the requirement is its duty) | `sch 11 para 8(1) the examination is of the kind the qualification must require` |
| sch 11 para 8(2) | the Secretary of State (power to refuse or revoke recognition if the requirement is not met) | the qualifying body (liability; the requirement is its duty) | `sch 11 para 8(2) the qualification may be awarded without the theoretical knowledge of the subject being tested by examination` |
| sch 11 para 8(3) | the Secretary of State (power to refuse or revoke recognition if the requirement is not met) | the qualifying body (liability; the requirement is its duty) | `sch 11 para 8(3) the qualification may be awarded without the ability to apply the theoretical knowledge of the subject in practice being tested by examination` |
| sch 11 para 8(4) | the Secretary of State (power to refuse or revoke recognition if the requirement is not met) | the qualifying body (liability; the requirement is its duty) | (inert) |
| sch 11 cross-heading (line 20494) "Practical training" | none | none | (inert) |
| sch 11 para 9(1) | the Secretary of State (power to refuse or revoke recognition if the requirement is not met) | the qualifying body (liability; the requirement is its duty) | `sch 11 para 9(1) the practical training meets the requirement` |
| sch 11 para 9(2) | the Secretary of State (power to refuse or revoke recognition if the requirement is not met) | the qualifying body (liability; the requirement is its duty) | `sch 11 para 9(2) the work is statutory audit work` |
| sch 11 para 9(3) | the Secretary of State (power to refuse or revoke recognition if the requirement is not met) | the qualifying body (liability; the requirement is its duty) | `sch 11 para 9(3) the training is given as required` |
| sch 11 para 9(4) | the Secretary of State (power to refuse or revoke recognition if the requirement is not met) | the qualifying body (liability; the requirement is its duty) | `sch 11 para 9(4) at least two-thirds of the training is given by a person of the kind required` |
| sch 11 para 9(4A) | the Secretary of State (power to refuse or revoke recognition if the requirement is not met) | the qualifying body (liability; the requirement is its duty) | `sch 11 para 9(4A) the conditions are met in relation to the person` |
| sch 11 para 9(5) | the Secretary of State (power to refuse or revoke recognition if the requirement is not met) | the qualifying body (liability; the requirement is its duty) | (blank) |
| sch 11 cross-heading (line 20508) "Supplementary provision with respect to a sufficient period…" | none | none | (inert) |
| sch 11 para 10(1) | the Secretary of State (power to refuse or revoke recognition if the requirement is not met) | the qualifying body (liability; the requirement is its duty) | `sch 11 para 10(1) the years of professional experience required after the deduction` |
| sch 11 para 10(2) | the Secretary of State (power to refuse or revoke recognition if the requirement is not met) | the qualifying body (liability; the requirement is its duty) | `sch 11 para 10(2) the experience route is not shorter than the course route` |
| sch 11 cross-heading (line 20514) "The body offering the qualification" | none | none | (inert) |
| sch 11 para 11(1) | the Secretary of State (power to refuse or revoke recognition if the requirement is not met) | the qualifying body (liability; the requirement is its duty) | `sch 11 para 11(1) the body meets the requirement` |
| sch 11 para 11(2) | the Secretary of State (power to refuse or revoke recognition if the requirement is not met) | the qualifying body (liability; the requirement is its duty) | `sch 11 para 11(2) the arrangements meet the requirement` |
| sch 11A heading | none | none | (inert) |
| sch 11A part 1 heading | none | none | (inert) |
| sch 11A para 1 | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A para 1 the Secretary of State`; `sch 11A part 1 the person is a specified person` |
| sch 11A para 2 | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A para 2 the Department of Enterprise, Trade and Investment for Northern Ireland`; `sch 11A part 1 the person is a specified person` |
| sch 11A para 3 | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A para 3 the Treasury`; `sch 11A part 1 the person is a specified person` |
| sch 11A para 4 | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A para 4 the Bank of England`; `sch 11A part 1 the person is a specified person` |
| sch 11A para 5 | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A para 5 the Financial Conduct Authority`; `sch 11A part 1 the person is a specified person` |
| sch 11A para 5A | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A para 5A the Prudential Regulation Authority`; `sch 11A part 1 the person is a specified person` |
| sch 11A para 6 | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A para 6 the Commissioners for Revenue and Customs`; `sch 11A part 1 the person is a specified person` |
| sch 11A para 7 | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A para 7 the Lord Advocate`; `sch 11A part 1 the person is a specified person` |
| sch 11A para 8 | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A para 8 the Director of Public Prosecutions`; `sch 11A part 1 the person is a specified person` |
| sch 11A para 9 | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A para 9 the Director of Public Prosecutions for Northern Ireland`; `sch 11A part 1 the person is a specified person` |
| sch 11A para 10 | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A para 10 a constable`; `sch 11A part 1 the person is a specified person` |
| sch 11A para 11 | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A para 11 a procurator fiscal`; `sch 11A part 1 the person is a specified person` |
| sch 11A para 12 | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A para 12 the Scottish Ministers`; `sch 11A part 1 the person is a specified person` |
| sch 11A para 13 | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A para 13 a body designated by the Secretary of State under section 1252`; `sch 11A part 1 the person is a specified person` |
| sch 11A para 14 | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A para 14 a recognised supervisory body`; `sch 11A part 1 the person is a specified person` |
| sch 11A para 15 | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A para 15 a recognised qualifying body`; `sch 11A part 1 the person is a specified person` |
| sch 11A para 16 | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A para 16 the competent authority`; `sch 11A part 1 the person is a specified person` |
| sch 11A para 17 | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A para 17 the Independent Supervisor`; `sch 11A part 1 the person is a specified person` |
| sch 11A para 17A | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A para 17A a recognised supervisory body as defined in section 1217(4) and Schedule 10 as they have effect by virtue of Schedule 5 to the Local Audit and Accountability Act 2014`; `sch 11A part 1 the person is a specified person` |
| sch 11A para 17B | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A para 17B a recognised qualifying body as defined in section 1219(13) as it has effect by virtue of that Schedule`; `sch 11A part 1 the person is a specified person` |
| sch 11A para 17C | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A para 17C a body designated by the Secretary of State under section 1252 as it has effect by virtue of that Schedule`; `sch 11A part 1 the person is a specified person` |
| sch 11A para 17D | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A para 17D a body participating with a recognised supervisory body within the meaning of that Act in arrangements for the purposes of paragraph 23 or 24 of Schedule 10 as it has effect by virtue of that Schedule`; `sch 11A part 1 the person is a specified person` |
| sch 11A part 2 heading | none | none | (inert) |
| sch 11A para 18 | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A para 18 enabling or assisting a person authorised under section 457 of this Act to exercise his functions`; `sch 11A part 2 the disclosure is of a specified description` |
| sch 11A para 19 | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A para 19 enabling or assisting an inspector appointed under Part 14 of the Companies Act 1985 to exercise his functions`; `sch 11A part 2 the disclosure is of a specified description` |
| sch 11A para 20 | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A para 20 enabling or assisting a person authorised under section 447 of the Companies Act 1985 or section 84 of the Companies Act 1989 to exercise his functions`; `sch 11A part 2 the disclosure is of a specified description` |
| sch 11A para 21 | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A para 21 enabling or assisting a person appointed under section 167 of the Financial Services and Markets Act 2000 (general investigations)`; `sch 11A part 2 the disclosure is of a specified description` |
| sch 11A para 22 | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A para 22 enabling or assisting a person appointed under section 168 of the Financial Services and Markets Act 2000 (investigations in particular cases)`; `sch 11A part 2 the disclosure is of a specified description` |
| sch 11A para 23 | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A para 23 enabling or assisting a person appointed under section 169(1)(b) of the Financial Services and Markets Act 2000 (investigation in support of overseas regulator)`; `sch 11A part 2 the disclosure is of a specified description` |
| sch 11A para 24 | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A para 24 enabling or assisting the body corporate administering the ombudsman scheme under section 225 of the Financial Services and Markets Act 2000`; `sch 11A part 2 the disclosure is of a specified description` |
| sch 11A para 25 | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A para 25 enabling or assisting a person appointed under paragraph 4 or 5 of Schedule 17 to the Financial Services and Markets Act 2000`; `sch 11A part 2 the disclosure is of a specified description` |
| sch 11A para 26 | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A para 26 enabling or assisting a person appointed under regulations made under section 262(1) and (2)(k) of the Financial Services and Markets Act 2000`; `sch 11A part 2 the disclosure is of a specified description` |
| sch 11A para 27 | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A para 27 enabling or assisting a person appointed under section 284 of the Financial Services and Markets Act 2000`; `sch 11A part 2 the disclosure is of a specified description` |
| sch 11A para 28 | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A para 28 enabling or assisting the investigator appointed under section 84 of the Financial Services Act 2012`; `sch 11A part 2 the disclosure is of a specified description` |
| sch 11A para 29 | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A para 29 enabling or assisting a person appointed by the Treasury to hold an inquiry into matters relating to financial services`; `sch 11A part 2 the disclosure is of a specified description` |
| sch 11A para 30 | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A part 2 the disclosure is of a specified description` |
| sch 11A para 31 | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A para 31 enabling or assisting the Scottish Ministers to exercise their functions under the enactments relating to insolvency`; `sch 11A part 2 the disclosure is of a specified description` |
| sch 11A para 32 | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A para 32 enabling or assisting the Department of Enterprise, Trade and Investment for Northern Ireland to exercise powers under the enactments relating to companies or insolvency`; `sch 11A part 2 the disclosure is of a specified description` |
| sch 11A para 33 | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A para 33 enabling or assisting a person appointed or authorised by the Department of Enterprise, Trade and Investment for Northern Ireland to exercise his functions`; `sch 11A part 2 the disclosure is of a specified description` |
| sch 11A para 34 | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A part 2 the disclosure is of a specified description` |
| sch 11A para 35 | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A para 35 enabling or assisting the Board of the Pension Protection Fund to exercise its functions`; `sch 11A part 2 the disclosure is of a specified description` |
| sch 11A para 36 | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A part 2 the disclosure is of a specified description` |
| sch 11A para 37 | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A para 37 enabling or assisting the Commissioners for Revenue and Customs to exercise their functions`; `sch 11A part 2 the disclosure is of a specified description` |
| sch 11A para 38 | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A para 38 enabling or assisting organs of the Society of Lloyds to exercise their functions`; `sch 11A part 2 the disclosure is of a specified description` |
| sch 11A para 39 | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A part 2 the disclosure is of a specified description` |
| sch 11A para 40 | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | (blank) |
| sch 11A para 41 | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A para 41 with a view to the institution of, or for the purposes of, proceedings before the Competition Appeal Tribunal`; `sch 11A part 2 the disclosure is of a specified description` |
| sch 11A para 42 | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A para 42 enabling or assisting an enforcer under Chapter 3 or 4 of Part 3 of the Digital Markets, Competition and Consumers Act 2024`; `sch 11A part 2 the disclosure is of a specified description` |
| sch 11A para 43 | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A para 43 enabling or assisting the Takeover Panel to perform its functions under Part 28 of this Act`; `sch 11A part 2 the disclosure is of a specified description` |
| sch 11A para 44 | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A para 44 enabling or assisting the Charity Commission to exercise its functions`; `sch 11A part 2 the disclosure is of a specified description` |
| sch 11A para 45 | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A para 45 enabling or assisting the Attorney General to exercise his functions in connection with charities`; `sch 11A part 2 the disclosure is of a specified description` |
| sch 11A para 46 | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A para 46 enabling or assisting the Gambling Commission to exercise its functions under sections 5 to 10 and 15 of the National Lottery etc. Act 1993`; `sch 11A part 2 the disclosure is of a specified description` |
| sch 11A para 47 | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A para 47 by the Gambling Commission to the Comptroller and Auditor General for an examination under Part 2 of the National Audit Act 1983`; `sch 11A part 2 the disclosure is of a specified description` |
| sch 11A para 48 | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A para 48 enabling or assisting a regulator under Schedule 3 to the Consumer Rights Act 2015 other than the Competition and Markets Authority`; `sch 11A part 2 the disclosure is of a specified description` |
| sch 11A para 49 | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A para 49 enabling or assisting an enforcement authority under the Consumer Contracts (Information, Cancellation and Additional Charges) Regulations 2013`; `sch 11A part 2 the disclosure is of a specified description` |
| sch 11A para 50 | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A para 50 enabling or assisting an enforcement authority under the Financial Services (Distance Marketing) Regulations 2004`; `sch 11A part 2 the disclosure is of a specified description` |
| sch 11A para 51 | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A para 51 enabling or assisting a local weights and measures authority in England and Wales under section 171(2) of the Digital Markets, Competition and Consumers Act 2024`; `sch 11A part 2 the disclosure is of a specified description` |
| sch 11A para 51A | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A para 51A enabling or assisting the lead enforcement authority under the Estate Agents Act 1979`; `sch 11A part 2 the disclosure is of a specified description` |
| sch 11A para 52 | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A part 2 the disclosure is of a specified description` |
| sch 11A para 53 | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | (blank) |
| sch 11A para 54 | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A para 54 enabling or assisting the compensation scheme manager established under section 212(1) of the Financial Services and Markets Act 2000`; `sch 11A part 2 the disclosure is of a specified description` |
| sch 11A para 55 | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A para 55 enabling or assisting a recognised investment exchange, a recognised clearing house or a recognised CSD to exercise its functions as such`; `sch 11A para 55 the body is a recognised investment exchange, a recognised clearing house or a recognised CSD` |
| sch 11A para 56 | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A para 56 enabling or assisting an operator of a relevant system for the purposes of the Uncertificated Securities Regulations 2001`; `sch 11A part 2 the disclosure is of a specified description` |
| sch 11A para 57 | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A para 57 enabling or assisting a body designated under section 326(1) of the Financial Services and Markets Act 2000`; `sch 11A part 2 the disclosure is of a specified description` |
| sch 11A para 58 | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A para 58 with a view to the institution of, or for the purposes of, civil proceedings arising under or by virtue of the Financial Services and Markets Act 2000`; `sch 11A part 2 the disclosure is of a specified description` |
| sch 11A para 59 | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A para 59 enabling or assisting a body designated under section 1252 of this Act to exercise its functions under Part 42 of this Act`; `sch 11A part 2 the disclosure is of a specified description` |
| sch 11A para 60 | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A para 60 enabling or assisting a recognised supervisory or qualifying body to exercise its functions as such`; `sch 11A part 2 the disclosure is of a specified description` |
| sch 11A para 61 | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A para 61 making available to an audited person information relating to a statutory audit of that persons accounts`; `sch 11A part 2 the disclosure is of a specified description` |
| sch 11A para 62 | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A para 62 making available to the public information relating to inspections under regulation 9 of the Statutory Auditors and Third Country Auditors Regulations 2016`; `sch 11A part 2 the disclosure is of a specified description` |
| sch 11A para 63 | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A para 63 enabling or assisting an official receiver to exercise his functions under the enactments relating to insolvency`; `sch 11A part 2 the disclosure is of a specified description` |
| sch 11A para 64 | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | (blank) |
| sch 11A para 65 | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A para 65 enabling or assisting a recognised professional body for the purposes of section 391 of the Insolvency Act 1986`; `sch 11A part 2 the disclosure is of a specified description` |
| sch 11A para 66 | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A para 66 enabling or assisting an overseas regulatory authority to exercise its regulatory functions`; `sch 11A para 66 the body is an overseas regulatory authority` |
| sch 11A para 67 | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A para 67 enabling or assisting the Regulator of Community Interest Companies`; `sch 11A part 2 the disclosure is of a specified description` |
| sch 11A para 68 | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A para 68 with a view to the institution of, or for the purposes of, criminal proceedings`; `sch 11A part 2 the disclosure is of a specified description` |
| sch 11A para 69 | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A para 69 enabling or assisting a person authorised by the Secretary of State under Part 2, 3 or 4 of the Proceeds of Crime Act 2002`; `sch 11A part 2 the disclosure is of a specified description` |
| sch 11A para 70 | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A para 70 with a view to the institution of, or for the purposes of, proceedings on an application under section 6, 7 or 8 of the Company Directors Disqualification Act 1986`; `sch 11A part 2 the disclosure is of a specified description` |
| sch 11A para 71 | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A part 2 the disclosure is of a specified description` |
| sch 11A para 72 | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A para 72 for the purposes of proceedings before the Financial Services Tribunal by virtue of the 2001 Partly Completed Procedures Order`; `sch 11A part 2 the disclosure is of a specified description` |
| sch 11A para 73 | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A para 73 for the purposes of proceedings before a tribunal in relation to a decision of the Pensions Regulator`; `sch 11A part 2 the disclosure is of a specified description` |
| sch 11A para 74 | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A para 74 enabling or assisting a body appointed under section 14 of the Companies (Audit, Investigations and Community Enterprise) Act 2004`; `sch 11A part 2 the disclosure is of a specified description` |
| sch 11A para 75 | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A para 75 with a view to disciplinary proceedings relating to the performance by a relevant lawyer, foreign lawyer, auditor, accountant, valuer or actuary of his professional duties`; `sch 11A para 75 the person is a relevant lawyer` |
| sch 11A para 75(None) term "foreign lawyer" | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A para 75 with a view to disciplinary proceedings relating to the performance by a relevant lawyer, foreign lawyer, auditor, accountant, valuer or actuary of his professional duties`; `sch 11A para 75 the person is a relevant lawyer` |
| sch 11A para 75(None) term "relevant lawyer" | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A para 75 with a view to disciplinary proceedings relating to the performance by a relevant lawyer, foreign lawyer, auditor, accountant, valuer or actuary of his professional duties`; `sch 11A para 75 the person is a relevant lawyer` |
| sch 11A para 76 | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A para 76 with a view to disciplinary proceedings relating to the performance by a public servant of his duties`; `sch 11A para 76 the person is a public servant` |
| sch 11A para 77 | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A para 77 the provision of a summary or collection of information framed so as not to enable the identity of any person to whom it relates to be ascertained`; `sch 11A part 2 the disclosure is of a specified description` |
| sch 11A para 78 | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A para 78 in pursuance of any assimilated obligation`; `sch 11A part 2 the disclosure is of a specified description` |
| sch 11A part 3 heading | none | none | (inert) |
| sch 11A para 79 | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A para 79 the disclosure is made in accordance with this Part of this Schedule` |
| sch 11A para 80 | the person who holds the information (privilege to disclose in the listed cases) | the person the information concerns (no-right) | `sch 11A para 80 the disclosure is made in accordance with this Part of this Schedule` |
| sch 12 heading | none | none | (inert) |
| sch 12 section reference | none | none | (inert) |
| sch 12 cross-heading (line 20656) "Arrangements for independent monitoring of audits of UK-tra…" | none | none | (inert) |
| sch 12 para 1(1) | the body maintaining the arrangements (power to monitor and discipline) | the registered third country auditor (liability) | `sch 12 para 1(1) the arrangements are appropriate arrangements` |
| sch 12 para 1(2) | none | none | (blank) |
| sch 12 cross-heading (line 20661) "Arrangements for independent investigations for disciplinar…" | none | none | (inert) |
| sch 12 para 2(1) | the body maintaining the arrangements (power to monitor and discipline) | the registered third country auditor (liability) | `sch 12 para 2(1) the arrangements are appropriate arrangements` |
| sch 12 para 2(1A) | the registered third country auditor (power to agree that no hearing is held) | the body (liability) | `sch 12 para 2(1A) decisions to take disciplinary action may be made without a disciplinary hearing` |
| sch 12 para 2(2) | none | none | `sch 12 para 2(2) the action is disciplinary action` |
| sch 12 para 2(2) term "disciplinary action" | none | none | `sch 12 para 2(2) the action is disciplinary action` |
| sch 12 cross-heading (line 20673) "Supplementary: arrangements to operate independently of thi…" | none | none | (inert) |
| sch 12 para 3(1) | none | none | `sch 12 para 3(1) this paragraph applies` |
| sch 12 para 3(2) | the monitoring or investigating body (claim to independence) | the registered third country auditor (duty not to be involved) | `sch 12 para 3(2) the arrangements are not to be regarded as appropriate for ensuring independence` |
| sch 12 para 3(3) | none | none | `sch 12 para 3(3) additional criteria may need to be satisfied for the arrangements to be regarded as appropriate` |
| sch 12 cross-heading (line 20681) "Supplementary: funding of arrangements" | none | none | (inert) |
| sch 12 para 4(1) | the body maintaining the arrangements (claim to the costs) | the registered third country auditor (duty to pay) | `sch 12 para 4 pay the costs of maintaining the relevant arrangements`; `sch 12 para 4 the duty to pay the costs` |
| sch 12 para 4(2) | the body maintaining the arrangements (claim to the costs) | the registered third country auditor (duty to pay) | `sch 12 para 4 pay the costs of maintaining the relevant arrangements`; `sch 12 para 4 the duty to pay the costs` |
| sch 12 cross-heading (line 20684) "Supplementary: scope of arrangements" | none | none | (inert) |
| sch 12 para 5 | none | none | `sch 12 para 5 the arrangements may qualify as arrangements within paragraph 1 or 2` |
| sch 12 cross-heading (line 20686) "Specification of particular arrangements by the Secretary o…" | none | none | (inert) |
| sch 12 para 6(1) | the Secretary of State (power to specify the set) | the registered third country auditor (liability) | `sch 12 para 6(1) the registered third country auditor is obliged to participate in the set of arrangements` |
| sch 12 para 6(2) | none | none | (inert) |
| sch 13 heading | none | none | (inert) |
| sch 13 section reference | none | none | (inert) |
| sch 13 cross-heading (line 20691) "Operation of this Schedule" | none | none | (inert) |
| sch 13 para 1(1) | none | none | `sch 13 para 1(1) the paragraph has effect in relation to the body` |
| sch 13 para 1(2) | none | none | `sch 13 para 1(2) paragraph 2 or 6 applies to the existing body in relation to the thing or function` |
| sch 13 para 1(3) | none | none | `sch 13 para 1(3) the power is a power to make provision by an order under section 1252` |
| sch 13 cross-heading (line 20700) "Status" | none | none | (inert) |
| sch 13 para 2 | the body and its members, officers and employees (immunity from Crown status) | the Crown (disability) | `sch 13 para 2 the person is regarded as acting on behalf of the Crown or as a Crown servant` |
| sch 13 cross-heading (line 20702) "Name, members and chairman" | none | none | (inert) |
| sch 13 para 3(1) | none | none | (inert) |
| sch 13 para 3(2) | none | none | (inert) |
| sch 13 para 3(3) | none | none | (inert) |
| sch 13 para 3(4) | none | none | (inert) |
| sch 13 cross-heading (line 20709) "Financial provisions" | none | none | (inert) |
| sch 13 para 4(1) | the chairman or member of the body (claim) | the body (duty) | `sch 13 para 4(1) the body has paid what it must pay by way of remuneration and allowances` |
| sch 13 para 4(2) | the chairman or member of the body (claim) | the body (duty) | `sch 13 para 4(2) the body has paid or made provision for the pension, allowance or gratuity` |
| sch 13 para 4(3) | the chairman or member of the body (claim) | the body (duty) | `sch 13 para 4(3) the body has paid the compensation it must pay` |
| sch 13 cross-heading (line 20719) "Proceedings" | none | none | (inert) |
| sch 13 para 5(1) | none | none | (inert) |
| sch 13 para 5(2) | none | none | (inert) |
| sch 13 cross-heading (line 20724) "Fees" | none | none | (inert) |
| sch 13 para 6(1) | the body (privilege to retain fees) | persons who pay fees (no-right) | `sch 13 para 6(1) the body may retain the fees` |
| sch 13 para 6(2) | the Secretary of State (claim) | the body (duty) | `sch 13 para 6(2) the fees are applied as required` |
| sch 13 para 6(3) | none | none | `sch 13 para 6(3) the expense is one of the expenses of the body` |
| sch 13 para 6(4) | the Secretary of State (claim) | the body (duty) | `sch 13 para 6(4) the fees prescribed are as required` |
| sch 13 para 6(5) | the Secretary of State (power: approve, vary or revoke the fees) | the body (liability) | `sch 13 para 6(5) the exercise of the power to prescribe fees has the approval required` |
| sch 13 para 6(6) | the Secretary of State (power: approve, vary or revoke the fees) | the body (liability) | `sch 13 para 6(6) the Secretary of State may by order vary or revoke regulations prescribing fees` |
| sch 13 cross-heading (line 20733) "Legislative functions" | none | none | (inert) |
| sch 13 para 7(1) | the public (not named in the text) | the body (duty) | `sch 13 para 7(1)-(2) the regulations or order of the body are made as required` |
| sch 13 para 7(2) | the public (not named in the text) | the body (duty) | `sch 13 para 7(1)-(2) the regulations or order of the body are made as required` |
| sch 13 para 7(3) | none | none | (inert) |
| sch 13 para 7(4) | none | none | `sch 13 para 7(4) the regulations or order are subject to negative resolution procedure or affirmative resolution procedure` |
| sch 13 para 8(1) | the public (not named in the text) | the body (duty) | `sch 13 para 8(1) print the instrument and make it available to the public`; `sch 13 para 8(1) the duty to make the instrument available` |
| sch 13 para 8(2) | the person alleged to have contravened (immunity: no contravention if the instrument was not available) | whoever alleges the contravention (disability) | `sch 13 para 8(2) this paragraph gives a defence to the alleged contravention` |
| sch 13 para 9(1) | none | none | `sch 13 para 9(1) the printed copy is evidence of the facts stated in the certificate` |
| sch 13 para 9(2) | none | none | `sch 13 para 9(2) the certificate is deemed to have been duly signed` |
| sch 13 para 9(3) | a person citing an instrument in legal proceedings (power to require a certified copy) | the body (liability) | `sch 13 para 9(3) cause a copy of the instrument to be endorsed with a certificate`; `sch 13 para 9(3) the duty to endorse a copy` |
| sch 13 cross-heading (line 20747) "Report and accounts" | none | none | (inert) |
| sch 13 para 10(1) | the Secretary of State (claim to an annual report) | the body (duty) | `sch 13 para 10(1) make a report to the Secretary of State`; `sch 13 para 10(1) the annual report` |
| sch 13 para 10(2) | none | none | `sch 13 para 10(2) the delegation order may modify sub-paragraph (1) for the calendar year` |
| sch 13 para 10(3) | Parliament (not named as holder) | the Secretary of State (duty to lay the reports) | `sch 13 para 10(3) lay copies of the report before Parliament`; `sch 13 para 10(3) the duty to lay the report` |
| sch 13 para 10(4) | none | none | `sch 13 para 10(4) the sub-paragraph applies to the body` |
| sch 13 para 10(5) | the Secretary of State (power) | the body (liability) | `sch 13 para 10(5) the Secretary of State may give directions about the accounts and the audit of the accounts` |
| sch 13 para 10(6) | none | none | `sch 13 para 10(6) the person may be appointed as auditor of the body` |
| sch 13 para 10(7) | the Secretary of State (power) | the body (liability) | `sch 13 para 10(7) the Secretary of State may give directions about the accounts and the audit of the accounts` |
| sch 13 para 10(8) | the Secretary of State (power) | the body (liability) | `sch 13 para 10(8) the Secretary of State may direct that provisions of this Act specified in the directions apply to the body` |
| sch 13 cross-heading (line 20760) "Other supplementary provisions" | none | none | (inert) |
| sch 13 para 11(1) | persons who acted under the function (immunity: what was done stands) | the Secretary of State and the body (disability) | `sch 13 para 11(1) the transfer or resumption of the function affects the thing previously done` |
| sch 13 para 11(2) | none | none | (inert) |
| sch 13 para 11(3) | none | none | (inert) |
| sch 13 para 11(4) | none | none | (inert) |
| sch 13 para 12 | none | none | (inert) |
| sch 13 para 13(1) | none | none | `sch 13 para 13(2) the proceedings may be brought by or against the body in the name of the body corporate` |
| sch 13 para 13(2) | none | none | `sch 13 para 13(2) the proceedings may be brought by or against the body in the name of the body corporate` |
| sch 13 para 13(3) | none | none | `sch 13 para 13(2) the proceedings may be brought by or against the body in the name of the body corporate` |
| sch 13 para 13(4) | none | none | `sch 13 para 13(4) the reference in paragraph 11(3)(e) or (4)(c) is read with the appropriate modifications` |
| sch 14 heading | none | none | (inert) |
| sch 14 section reference | none | none | (inert) |
| sch 14 cross-heading (line 20782) "Companies (Audit, Investigations and Community Enterprise) …" | none | none | (inert) |
| sch 14 para 1 | none | none | (inert) |
| sch 15 heading | none | none | (inert) |
| sch 15 section reference | none | none | (inert) |
| sch 15 part 1 heading | none | none | (inert) |
| sch 15 para 1 | none | none | (inert) |
| sch 15 para 2 | none | none | (blank) |
| sch 15 para 3 | none | none | (inert) |
| sch 15 para 4 | none | none | (inert) |
| sch 15 para 5 | none | none | (inert) |
| sch 15 para 6 | none | none | (inert) |
| sch 15 para 7 | none | none | (inert) |
| sch 15 para 8 | none | none | (inert) |
| sch 15 para 9 | none | none | (blank) |
| sch 15 para 10 | none | none | (inert) |
| sch 15 para 11 | none | none | (inert) |
| sch 15 para 12 | none | none | (inert) |
| sch 15 part 2 heading | none | none | (inert) |
| sch 15 para 13 | none | none | (inert) |
| sch 15 para 14 | none | none | (inert) |
| sch 15 para 15 | none | none | (inert) |
| sch 16 heading | none | none | (inert) |
| sch 16 section reference | none | none | (inert) |
| sch 16 table 1 heading | none | none | (inert) |
| sch 16 table 1 column headings | none | none | (inert) |
| sch 16 table 1 row 1: Companies Act 1985 (c. 6) | none | none | (inert) |
| sch 16 table 1 row 2: Insolvency Act 1985 (c. 65) | none | none | (inert) |
| sch 16 table 1 row 3: Insolvency Act 1986 (c. 45) | none | none | (inert) |
| sch 16 table 1 row 4: Building Societies Act 1986 (c. 53) | none | none | (inert) |
| sch 16 table 1 row 5: Finance Act 1988 (c. 39) | none | none | (inert) |
| sch 16 table 1 row 6: Water Act 1989 (c. 15) | none | none | (inert) |
| sch 16 table 1 row 7: Companies Act 1989 (c. 40) | none | none | (inert) |
| sch 16 table 1 row 8: Age of Legal Capacity (Scotland) Act 1991 (c. 50) | none | none | (inert) |
| sch 16 table 1 row 9: Water Consolidation (Consequential Provisions) Act 1991 (c. 60) | none | none | (inert) |
| sch 16 table 1 row 10: Charities Act 1992 (c. 41) | none | none | (inert) |
| sch 16 table 1 row 11: Charities Act 1993 (c. 10) | none | none | (inert) |
| sch 16 table 1 row 12: Criminal Justice Act 1993 (c. 36) | none | none | (inert) |
| sch 16 table 1 row 13: Welsh Language Act 1993 (c. 38) | none | none | (inert) |
| sch 16 table 1 row 14: Pension Schemes Act 1993 (c. 48) | none | none | (inert) |
| sch 16 table 1 row 15: Trade Marks Act 1994 (c. 26) | none | none | (inert) |
| sch 16 table 1 row 16: Deregulation and Contracting Out Act 1994 (c. 40) | none | none | (inert) |
| sch 16 table 1 row 17: Requirements of Writing (Scotland) Act 1995 (c. 7) | none | none | (inert) |
| sch 16 table 1 row 18: Criminal Procedure (Consequential Provisions) (Scotland) Act 1995 (c.… | none | none | (inert) |
| sch 16 table 1 row 19: Disability Discrimination Act 1995 (c. 50) | none | none | (inert) |
| sch 16 table 1 row 20: Financial Services and Markets Act 2000 (c. 8) | none | none | (inert) |
| sch 16 table 1 row 21: Limited Liability Partnerships Act 2000 (c. 12) | none | none | (inert) |
| sch 16 table 1 row 22: Political Parties, Elections and Referendums Act 2000 (c. 41) | none | none | (inert) |
| sch 16 table 1 row 23: Criminal Justice and Police Act 2001 (c. 16) | none | none | (inert) |
| sch 16 table 1 row 24: Enterprise Act 2002 (c. 40) | none | none | (inert) |
| sch 16 table 1 row 25: Companies (Audit, Investigations and Community Enterprise) Act 2004 (… | none | none | (inert) |
| sch 16 table 1 row 26: Civil Partnership Act 2004 (c. 33) | none | none | (inert) |
| sch 16 table 1 row 27: Constitutional Reform Act 2005 (c. 4) | none | none | (inert) |
| sch 16 table 2 heading | none | none | (inert) |
| sch 16 table 2 column headings | none | none | (inert) |
| sch 16 table 2 row 1: Companies (Northern Ireland) Order 1986 (S.I. 1986/1032 (N.I. 6)) | none | none | (inert) |
| sch 16 table 2 row 2: Companies Consolidation (Consequential Provisions) (Northern Ireland)… | none | none | (inert) |
| sch 16 table 2 row 3: Business Names (Northern Ireland) Order 1986 (S.I. 1986/1033 (N.I. 7)) | none | none | (inert) |
| sch 16 table 2 row 4: Industrial Relations (Northern Ireland) Order 1987 (S.I. 1987/936 N.I… | none | none | (inert) |
| sch 16 table 2 row 5: Finance Act 1988 (c. 39) | none | none | (inert) |
| sch 16 table 2 row 6: Companies (Northern Ireland) Order 1989 (S.I. 1989/2404 (N.I. 18)) | none | none | (inert) |
| sch 16 table 2 row 7: Insolvency (Northern Ireland) Order 1989 (S.I. 1989/2405 (N.I. 19)) | none | none | (inert) |
| sch 16 table 2 row 8: European Economic Interest Groupings Regulations (Northern Ireland) 1… | none | none | (inert) |
| sch 16 table 2 row 9: Companies (Northern Ireland) Order 1990 (S.I. 1990/593 (N.I. 5)) | none | none | (inert) |
| sch 16 table 2 row 10: Companies (No. 2) (Northern Ireland) Order 1990 (S.I. 1990/1504 (N.I.… | none | none | (inert) |
| sch 16 table 2 row 11: Criminal Justice Act 1993 (c. 36) | none | none | (inert) |
| sch 16 table 2 row 12: Financial Provisions (Northern Ireland) Order 1993 (S.I. 1993/1252 (N… | none | none | (inert) |
| sch 16 table 2 row 13: Deregulation and Contracting Out Act 1994 (c. 40) | none | none | (inert) |
| sch 16 table 2 row 14: Pensions (Northern Ireland) Order 1995 (S.I. 1995/3213 (N.I. 22)) | none | none | (inert) |
| sch 16 table 2 row 15: Deregulation and Contracting Out (Northern Ireland) Order 1996 (S.I. … | none | none | (inert) |
| sch 16 table 2 row 16: Youth Justice and Criminal Evidence Act 1999 (c. 23) | none | none | (inert) |
| sch 16 table 2 row 17: Limited Liability Partnerships Act (Northern Ireland) 2002 (c. 12 (N.… | none | none | (inert) |
| sch 16 table 2 row 18: Open-Ended Investment Companies Act (Northern Ireland) 2002 (c. 13) | none | none | (inert) |
| sch 16 table 2 row 19: Company Directors Disqualification (Northern Ireland) Order 2002 (S.I… | none | none | (inert) |
| sch 16 table 2 row 20: Companies (Audit, Investigations and Community Enterprise) Act 2004 (… | none | none | (inert) |
| sch 16 table 2 row 21: Law Reform (Miscellaneous Provisions) (Northern Ireland) Order 2005 (… | none | none | (inert) |
| sch 16 table 2 row 22: Companies (Audit, Investigations and Community Enterprise) (Northern … | none | none | (inert) |
| sch 16 table 3 heading | none | none | (inert) |
| sch 16 table 3 column headings | none | none | (inert) |
| sch 16 table 3 row 1: Limited Partnerships Act 1907 (c. 24) | none | none | (inert) |
| sch 16 table 3 row 2: Business Names Act 1985 (c. 7) | none | none | (inert) |
| sch 16 table 3 row 3: Companies Act 1989 (c. 40) | none | none | (inert) |
| sch 16 table 3 row 4: Criminal Procedure (Consequential Provisions) (Scotland) Act 1995 (c.… | none | none | (inert) |
| sch 16 table 3 row 5: Companies (Audit, Investigations and Community Enterprise) Act 2004 (… | none | none | (inert) |
| sch 16 table 3 row 6: Civil Partnership Act 2004 (c. 33) | none | none | (inert) |

## Marginal readings for a lawyer (coa30)

Every branch below rests on one of the two readings the brief marks "for a lawyer": (a) a failed "if" counts as the text's no, clause by clause, within the provision that holds the "if" (an inference: "if A then B" does not itself say "if not A then not B"), and flat negatives count as the text saying no; (b) a prohibition or grant limited by its own wording does not (the case outside the limit answers NOTHING). The list was built by a script that reads the `FALSE-kind` and `NOTHING-kind` comments of the layer-1 modules: a `NOTHING-kind (limited by its own wording)` branch rests on (b); a `FALSE-kind` branch whose quoted words contain "if", "where", "unless", "provided", "while", "until" or "except" (and are not a "means" definition or a flat "shall not") rests on (a). The other reading is stated for each. Branches that rest on a flat "must" or "may only if", on a definition by "means", or on a period the text fixes in its own words are not listed here: they follow the rulings of 2026-11-04 (N2 option A) and 2026-11-05 (periods ruling (a)).

| function | branch | rests on | the other reading |
| --- | --- | --- | --- |
| `sch 10 para 1(1) the body may apply to the Secretary of State for a recognition order` | NOTHING outside the limit the text states in its own words | (b) a grant or prohibition limited by its own wording does not say no outside the limit | JUST FALSE outside the limit |
| `sch 10 para 1(4) the directions and requirements may differ as between different applications` | NOTHING outside the limit the text states in its own words | (b) a grant or prohibition limited by its own wording does not say no outside the limit | JUST FALSE outside the limit |
| `sch 10 para 1(5) the Secretary of State may specify the form or manner of verification` | NOTHING outside the limit the text states in its own words | (b) a grant or prohibition limited by its own wording does not say no outside the limit | JUST FALSE outside the limit |
| `sch 10 para 2(2) the Secretary of State may make a recognition order` | JUST FALSE when the "if"/"where"/"unless" condition fails | (a) a failed condition counts as the text's no, within the provision that holds it | NOTHING (the condition is not said to be the only route) |
| `sch 10 para 2(3) the Secretary of State may refuse to make a recognition order` | NOTHING when the "if" gate fails (a power named for a grant, not closed with "only") | (b) a grant limited by its own wording does not say no outside the limit | JUST FALSE, a failed "if" read as the text's own no (reading (a)) |
| `sch 10 para 3(1) the Secretary of State may revoke the recognition order` | NOTHING when the "if" gate fails (a power named for a grant, not closed with "only") | (b) a grant limited by its own wording does not say no outside the limit | JUST FALSE, a failed "if" read as the text's own no (reading (a)) |
| `sch 10 para 3(1A) the Secretary of State may revoke the recognition order` | NOTHING when the "if" gate fails (a power named for a grant, not closed with "only") | (b) a grant limited by its own wording does not say no outside the limit | JUST FALSE, a failed "if" read as the text's own no (reading (a)) |
| `sch 10 para 3(5) the person may make written and oral representations` | NOTHING outside the limit the text states in its own words | (b) a grant or prohibition limited by its own wording does not say no outside the limit | JUST FALSE outside the limit |
| `sch 10 para 3(7) the Secretary of State has had regard to the representations` | NOTHING outside the limit the text states in its own words | (b) a grant or prohibition limited by its own wording does not say no outside the limit | JUST FALSE outside the limit |
| `sch 10 para 3(8) the Secretary of State may revoke without regard to the restriction in sub-paragraph (2)` | NOTHING when the "if" gate fails (a power named for a grant, not closed with "only") | (b) a grant limited by its own wording does not say no outside the limit | JUST FALSE, a failed "if" read as the text's own no (reading (a)) |
| `sch 10 para 3(9) the revocation order may contain the transitional provision` | NOTHING outside the limit the text states in its own words | (b) a grant or prohibition limited by its own wording does not say no outside the limit | JUST FALSE outside the limit |
| `sch 10 para 3(10) the revocation is not subject to the restrictions and requirements listed` | NOTHING outside the limit the text states in its own words | (b) a grant or prohibition limited by its own wording does not say no outside the limit | JUST FALSE outside the limit |
| `sch 10 para 4 the order has effect after commencement as an order made under paragraph 2(1) of this Schedule` | NOTHING outside the limit the text states in its own words | (b) a grant or prohibition limited by its own wording does not say no outside the limit | JUST FALSE outside the limit |
| `sch 10 para 5 the order is to be made by statutory instrument` | NOTHING outside the limit the text states in its own words | (b) a grant or prohibition limited by its own wording does not say no outside the limit | JUST FALSE outside the limit |
| `sch 10 para 6(1) the person is not eligible for appointment as a statutory auditor under the rule the body must have` | JUST FALSE when the "if"/"where"/"unless" condition fails | (a) a failed condition counts as the text's no, within the provision that holds it | NOTHING (the condition is not said to be the only route) |
| `sch 10 para 6(2)(a) the aptitude test must test the person's knowledge of the subject` | NOTHING outside the limit the text states in its own words | (b) a grant or prohibition limited by its own wording does not say no outside the limit | JUST FALSE outside the limit |
| `sch 10 para 6(2C) the body meets the requirements for the adaptation period` | NOTHING outside the limit the text states in its own words | (b) a grant or prohibition limited by its own wording does not say no outside the limit | JUST FALSE outside the limit |
| `sch 10 para 6(2C)(b) the applicant may be required to undergo further training during the adaptation period` | NOTHING outside the limit the text states in its own words | (b) a grant or prohibition limited by its own wording does not say no outside the limit | JUST FALSE outside the limit |
| `sch 10 para 6(3) the firm may be permitted to remain eligible for appointment as a statutory auditor` | NOTHING outside the limit the text states in its own words | (b) a grant or prohibition limited by its own wording does not say no outside the limit | JUST FALSE outside the limit |
| `sch 10 para 7(3) the firm is controlled by qualified persons` | JUST FALSE when the "if"/"where"/"unless" condition fails | (a) a failed condition counts as the text's no, within the provision that holds it | NOTHING (the condition is not said to be the only route) |
| `sch 10 para 7(6) paragraphs 5 to 11 of Schedule 7 apply to the counting of rights` | NOTHING outside the limit the text states in its own words | (b) a grant or prohibition limited by its own wording does not say no outside the limit | JUST FALSE outside the limit |
| `sch 10 para 7A(3) the applicant may be required to undergo further training during the adaptation period` | NOTHING outside the limit the text states in its own words | (b) a grant or prohibition limited by its own wording does not say no outside the limit | JUST FALSE outside the limit |
| `sch 10 para 8(2) the matters the body may take into account must include a matter relating to this person` | NOTHING outside the limit the text states in its own words | (b) a grant or prohibition limited by its own wording does not say no outside the limit | JUST FALSE outside the limit |
| `sch 10 para 8(3) director is to be read as member in sub-paragraph (2)(b)` | NOTHING outside the limit the text states in its own words | (b) a grant or prohibition limited by its own wording does not say no outside the limit | JUST FALSE outside the limit |
| `sch 10 para 8(4) the person is a controller of the body corporate` | NOTHING outside the limit the text states in its own words | (b) a grant or prohibition limited by its own wording does not say no outside the limit | JUST FALSE outside the limit |
| `sch 10 para 9(1A) the rules of the body must bar the appointment` | JUST FALSE when the "if"/"where"/"unless" condition fails | (a) a failed condition counts as the text's no, within the provision that holds it | NOTHING (the condition is not said to be the only route) |
| `sch 10 para 9(1A) the rules of the body must bar the appointment` | NOTHING outside the limit the text states in its own words | (b) a grant or prohibition limited by its own wording does not say no outside the limit | JUST FALSE outside the limit |
| `sch 10 para 9(1A) the bar on appointment is in force on the day` | NOTHING outside the limit the text states in its own words | (b) a grant or prohibition limited by its own wording does not say no outside the limit | JUST FALSE outside the limit |
| `sch 10 para 9(4) the fine is recoverable by the body as a debt due to it from the person obliged to pay it` | NOTHING outside the limit the text states in its own words | (b) a grant or prohibition limited by its own wording does not say no outside the limit | JUST FALSE outside the limit |
| `sch 10 para 9(5) the auditor is regarded as an officer of the audited person for the purposes of sub-paragraph (1A)(a) and (b)` | NOTHING outside the limit the text states in its own words | (b) a grant or prohibition limited by its own wording does not say no outside the limit | JUST FALSE outside the limit |
| `sch 10 para 10C(3) the rules of the body must bar the appointment` | NOTHING outside the limit the text states in its own words | (b) a grant or prohibition limited by its own wording does not say no outside the limit | JUST FALSE outside the limit |
| `sch 10 para 10C(4) the fine is recoverable by the body as a debt due to it from the person obliged to pay it` | NOTHING outside the limit the text states in its own words | (b) a grant or prohibition limited by its own wording does not say no outside the limit | JUST FALSE outside the limit |
| `sch 10 para 10C(5) the auditor is regarded as an officer of the entity for the purposes of sub-paragraph (3)(a) and (b)` | NOTHING outside the limit the text states in its own words | (b) a grant or prohibition limited by its own wording does not say no outside the limit | JUST FALSE outside the limit |
| `sch 10 para 12(4) the sanction applies to the person as it applies to members` | NOTHING outside the limit the text states in its own words | (b) a grant or prohibition limited by its own wording does not say no outside the limit | JUST FALSE outside the limit |
| `sch 10 para 12(6) the identity of the person sanctioned must not be made available to the public` | JUST FALSE when the "if"/"where"/"unless" condition fails | (a) a failed condition counts as the text's no, within the provision that holds it | NOTHING (the condition is not said to be the only route) |
| `sch 10 para 12(7) the information must be published on the website of the body on the day` | NOTHING outside the limit the text states in its own words | (b) a grant or prohibition limited by its own wording does not say no outside the limit | JUST FALSE outside the limit |
| `sch 10 para 13(2) the monitoring is regarded as monitoring of compliance with the rules of the body for the purposes of paragraph 12(1) and (1A)` | NOTHING outside the limit the text states in its own words | (b) a grant or prohibition limited by its own wording does not say no outside the limit | JUST FALSE outside the limit |
| `sch 10 para 13(3)(b)(ii) another inspection of the person is due by the day asked about` | NOTHING outside the limit the text states in its own words | (b) a grant or prohibition limited by its own wording does not say no outside the limit | JUST FALSE outside the limit |
| `sch 10 para 13(9) the body has taken account of the proportionality of the standards` | NOTHING outside the limit the text states in its own words | (b) a grant or prohibition limited by its own wording does not say no outside the limit | JUST FALSE outside the limit |
| `sch 10 para 13(10) the inspection of the firm may be treated as an inspection of all individuals responsible` | NOTHING when the "if" gate fails (a power named for a grant, not closed with "only") | (b) a grant limited by its own wording does not say no outside the limit | JUST FALSE, a failed "if" read as the text's own no (reading (a)) |
| `sch 10 para 16(1) the body meets the requirement` | JUST FALSE when the "if"/"where"/"unless" condition fails | (a) a failed condition counts as the text's no, within the provision that holds it | NOTHING (the condition is not said to be the only route) |
| `sch 10 para 16A(2) the person must refuse to transfer audit working papers and investigation reports to the third country competent authority` | NOTHING outside the limit the text states in its own words | (b) a grant or prohibition limited by its own wording does not say no outside the limit | JUST FALSE outside the limit |
| `sch 10 para 20ZA the body has paid the costs it must pay` | NOTHING outside the limit the text states in its own words | (b) a grant or prohibition limited by its own wording does not say no outside the limit | JUST FALSE outside the limit |
| `sch 10 para 20A(2) the territory is treated as an EEA State and subject to the Audit Directive for the purposes of this Schedule` | NOTHING outside the limit the text states in its own words | (b) a grant or prohibition limited by its own wording does not say no outside the limit | JUST FALSE outside the limit |
| `sch 11 para 1(1) the body may apply to the Secretary of State for a recognition order` | NOTHING outside the limit the text states in its own words | (b) a grant or prohibition limited by its own wording does not say no outside the limit | JUST FALSE outside the limit |
| `sch 11 para 1(5) the directions and requirements may differ as between different applications` | NOTHING outside the limit the text states in its own words | (b) a grant or prohibition limited by its own wording does not say no outside the limit | JUST FALSE outside the limit |
| `sch 11 para 1(6) the Secretary of State may specify the form or manner of verification` | NOTHING outside the limit the text states in its own words | (b) a grant or prohibition limited by its own wording does not say no outside the limit | JUST FALSE outside the limit |
| `sch 11 para 1(7) the verification required may include independent moderation of the examinations` | NOTHING outside the limit the text states in its own words | (b) a grant or prohibition limited by its own wording does not say no outside the limit | JUST FALSE outside the limit |
| `sch 11 para 2(2) the Secretary of State may make a recognition order` | JUST FALSE when the "if"/"where"/"unless" condition fails | (a) a failed condition counts as the text's no, within the provision that holds it | NOTHING (the condition is not said to be the only route) |
| `sch 11 para 3(1) the Secretary of State may revoke the recognition order` | NOTHING when the "if" gate fails (a power named for a grant, not closed with "only") | (b) a grant limited by its own wording does not say no outside the limit | JUST FALSE, a failed "if" read as the text's own no (reading (a)) |
| `sch 11 para 3(5) the person may make written and oral representations` | NOTHING outside the limit the text states in its own words | (b) a grant or prohibition limited by its own wording does not say no outside the limit | JUST FALSE outside the limit |
| `sch 11 para 3(7) the Secretary of State has had regard to the representations` | NOTHING outside the limit the text states in its own words | (b) a grant or prohibition limited by its own wording does not say no outside the limit | JUST FALSE outside the limit |
| `sch 11 para 3(8) the Secretary of State may revoke without regard to the restriction in sub-paragraph (2)` | NOTHING when the "if" gate fails (a power named for a grant, not closed with "only") | (b) a grant limited by its own wording does not say no outside the limit | JUST FALSE, a failed "if" read as the text's own no (reading (a)) |
| `sch 11 para 3(9) the revocation order may contain the transitional provision` | NOTHING outside the limit the text states in its own words | (b) a grant or prohibition limited by its own wording does not say no outside the limit | JUST FALSE outside the limit |
| `sch 11 para 3(10) the revocation is not subject to the restrictions and requirements listed` | NOTHING outside the limit the text states in its own words | (b) a grant or prohibition limited by its own wording does not say no outside the limit | JUST FALSE outside the limit |
| `sch 11 para 4 the order has effect after commencement as an order made under paragraph 2(1) of this Schedule` | NOTHING outside the limit the text states in its own words | (b) a grant or prohibition limited by its own wording does not say no outside the limit | JUST FALSE outside the limit |
| `sch 11 para 5 the order is to be made by statutory instrument` | NOTHING outside the limit the text states in its own words | (b) a grant or prohibition limited by its own wording does not say no outside the limit | JUST FALSE outside the limit |
| `sch 11 para 6(2) the person has attained university entrance level` | NOTHING outside the limit the text states in its own words | (b) a grant or prohibition limited by its own wording does not say no outside the limit | JUST FALSE outside the limit |
| `sch 11 para 8(2) the qualification may be awarded without the theoretical knowledge of the subject being tested by examination` | NOTHING outside the limit the text states in its own words | (b) a grant or prohibition limited by its own wording does not say no outside the limit | JUST FALSE outside the limit |
| `sch 11 para 8(3) the qualification may be awarded without the ability to apply the theoretical knowledge of the subject in practice being tested by examination` | NOTHING outside the limit the text states in its own words | (b) a grant or prohibition limited by its own wording does not say no outside the limit | JUST FALSE outside the limit |
| `sch 11A part 2 the disclosure is of a specified description` | JUST FALSE when the "if"/"where"/"unless" condition fails | (a) a failed condition counts as the text's no, within the provision that holds it | NOTHING (the condition is not said to be the only route) |
| `sch 11A para 79 the disclosure is made in accordance with this Part of this Schedule` | JUST FALSE when the "if"/"where"/"unless" condition fails | (a) a failed condition counts as the text's no, within the provision that holds it | NOTHING (the condition is not said to be the only route) |
| `sch 11A para 80 the disclosure is made in accordance with this Part of this Schedule` | JUST FALSE when the "if"/"where"/"unless" condition fails | (a) a failed condition counts as the text's no, within the provision that holds it | NOTHING (the condition is not said to be the only route) |
| `sch 12 para 2(1A) decisions to take disciplinary action may be made without a disciplinary hearing` | NOTHING outside the limit the text states in its own words | (b) a grant or prohibition limited by its own wording does not say no outside the limit | JUST FALSE outside the limit |
| `sch 12 para 3(1) this paragraph applies` | NOTHING outside the limit the text states in its own words | (b) a grant or prohibition limited by its own wording does not say no outside the limit | JUST FALSE outside the limit |
| `sch 12 para 3(2) the arrangements are not to be regarded as appropriate for ensuring independence` | JUST FALSE when the "if"/"where"/"unless" condition fails | (a) a failed condition counts as the text's no, within the provision that holds it | NOTHING (the condition is not said to be the only route) |
| `sch 12 para 3(3) additional criteria may need to be satisfied for the arrangements to be regarded as appropriate` | NOTHING outside the limit the text states in its own words | (b) a grant or prohibition limited by its own wording does not say no outside the limit | JUST FALSE outside the limit |
| `sch 12 para 4 the registered third country auditor has paid the costs it must pay` | NOTHING outside the limit the text states in its own words | (b) a grant or prohibition limited by its own wording does not say no outside the limit | JUST FALSE outside the limit |
| `sch 12 para 5 the arrangements may qualify as arrangements within paragraph 1 or 2` | NOTHING outside the limit the text states in its own words | (b) a grant or prohibition limited by its own wording does not say no outside the limit | JUST FALSE outside the limit |
| `sch 12 para 6(1) the registered third country auditor is obliged to participate in the set of arrangements` | NOTHING outside the limit the text states in its own words | (b) a grant or prohibition limited by its own wording does not say no outside the limit | JUST FALSE outside the limit |
| `sch 13 para 1(3) the power is a power to make provision by an order under section 1252` | NOTHING outside the limit the text states in its own words | (b) a grant or prohibition limited by its own wording does not say no outside the limit | JUST FALSE outside the limit |
| `sch 13 para 2 the person is regarded as acting on behalf of the Crown or as a Crown servant` | NOTHING outside the limit the text states in its own words | (b) a grant or prohibition limited by its own wording does not say no outside the limit | JUST FALSE outside the limit |
| `sch 13 para 4(1) the body has paid what it must pay by way of remuneration and allowances` | NOTHING outside the limit the text states in its own words | (b) a grant or prohibition limited by its own wording does not say no outside the limit | JUST FALSE outside the limit |
| `sch 13 para 4(2) the body has paid or made provision for the pension, allowance or gratuity` | NOTHING outside the limit the text states in its own words | (b) a grant or prohibition limited by its own wording does not say no outside the limit | JUST FALSE outside the limit |
| `sch 13 para 4(3) the body has paid the compensation it must pay` | NOTHING outside the limit the text states in its own words | (b) a grant or prohibition limited by its own wording does not say no outside the limit | JUST FALSE outside the limit |
| `sch 13 para 6(1) the body may retain the fees` | NOTHING outside the limit the text states in its own words | (b) a grant or prohibition limited by its own wording does not say no outside the limit | JUST FALSE outside the limit |
| `sch 13 para 7(4) the regulations or order are subject to negative resolution procedure or affirmative resolution procedure` | NOTHING outside the limit the text states in its own words | (b) a grant or prohibition limited by its own wording does not say no outside the limit | JUST FALSE outside the limit |
| `sch 13 para 8(2) this paragraph gives a defence to the alleged contravention` | JUST FALSE when the "if"/"where"/"unless" condition fails | (a) a failed condition counts as the text's no, within the provision that holds it | NOTHING (the condition is not said to be the only route) |
| `sch 13 para 9(1) the printed copy is evidence of the facts stated in the certificate` | NOTHING outside the limit the text states in its own words | (b) a grant or prohibition limited by its own wording does not say no outside the limit | JUST FALSE outside the limit |
| `sch 13 para 9(2) the certificate is deemed to have been duly signed` | NOTHING outside the limit the text states in its own words | (b) a grant or prohibition limited by its own wording does not say no outside the limit | JUST FALSE outside the limit |
| `sch 13 para 9(2) the certificate is deemed to have been duly signed` | JUST FALSE when the "if"/"where"/"unless" condition fails | (a) a failed condition counts as the text's no, within the provision that holds it | NOTHING (the condition is not said to be the only route) |
| `sch 13 para 9(3) the person may require the body to cause a copy of the instrument to be endorsed with a certificate` | NOTHING outside the limit the text states in its own words | (b) a grant or prohibition limited by its own wording does not say no outside the limit | JUST FALSE outside the limit |
| `sch 13 para 10(2) the delegation order may modify sub-paragraph (1) for the calendar year` | NOTHING outside the limit the text states in its own words | (b) a grant or prohibition limited by its own wording does not say no outside the limit | JUST FALSE outside the limit |
| `sch 13 para 10(3) the Secretary of State has laid the report before Parliament as required` | NOTHING outside the limit the text states in its own words | (b) a grant or prohibition limited by its own wording does not say no outside the limit | JUST FALSE outside the limit |
| `sch 13 para 10(4) the sub-paragraph applies to the body` | JUST FALSE when the "if"/"where"/"unless" condition fails | (a) a failed condition counts as the text's no, within the provision that holds it | NOTHING (the condition is not said to be the only route) |
| `sch 13 para 10(6) the person may be appointed as auditor of the body` | NOTHING outside the limit the text states in its own words | (b) a grant or prohibition limited by its own wording does not say no outside the limit | JUST FALSE outside the limit |
| `sch 13 para 10(6) the person may be appointed as auditor of the body` | JUST FALSE when the "if"/"where"/"unless" condition fails | (a) a failed condition counts as the text's no, within the provision that holds it | NOTHING (the condition is not said to be the only route) |
| `sch 13 para 10(7) the Secretary of State may give directions about the accounts and the audit of the accounts` | NOTHING outside the limit the text states in its own words | (b) a grant or prohibition limited by its own wording does not say no outside the limit | JUST FALSE outside the limit |
| `sch 13 para 10(8) the Secretary of State may direct that provisions of this Act specified in the directions apply to the body` | NOTHING outside the limit the text states in its own words | (b) a grant or prohibition limited by its own wording does not say no outside the limit | JUST FALSE outside the limit |
| `sch 13 para 11(1) the transfer or resumption of the function affects the thing previously done` | NOTHING outside the limit the text states in its own words | (b) a grant or prohibition limited by its own wording does not say no outside the limit | JUST FALSE outside the limit |
| `sch 13 para 13(2) the proceedings may be brought by or against the body in the name of the body corporate` | NOTHING outside the limit the text states in its own words | (b) a grant or prohibition limited by its own wording does not say no outside the limit | JUST FALSE outside the limit |
| `sch 13 para 13(4) the reference in paragraph 11(3)(e) or (4)(c) is read with the appropriate modifications` | NOTHING outside the limit the text states in its own words | (b) a grant or prohibition limited by its own wording does not say no outside the limit | JUST FALSE outside the limit |

### Reading a result: FALSE and NOTHING (coa30)

The rule of 2026-10-29 (assumed, not ruled by a lawyer), as it reads in these Schedules. Every decision function answers `MAYBE BOOLEAN` (or a `MAYBE` of a date, or a plain `NUMBER` where the text fixes a number).

- `JUST TRUE`: the Schedule says yes: the Secretary of State may make the order, the person is a key audit partner, the disclosure is of a specified description, the qualification may be restricted to the person.
- `JUST FALSE` ("a no"): the Schedule says no in its own words: a "means" or "are" definition whose limbs fail ("public interest entity" means ...), a "must have" requirement not met, a power that may be exercised "only if" a condition and the condition fails, a period the text fixes in its own words and the day falls outside it ("within the period of three months beginning with ..."), a flat negative ("shall not be made by statutory instrument", "not to be regarded as an officer"), a proviso not met ("provided such information does not identify any audited person"), and the defence of Schedule 13 paragraph 8(2) not shown ("this paragraph gives no defence on these facts", never "no defence at all"). Each such branch carries `-- FALSE-kind (the text says no in its own words): "<the quoted words>"`.
- `NOTHING` ("not covered"): the Schedule does not decide the case: a list that is not closed (Schedule 11A names persons and descriptions without "only"; "includes"; "may be achieved by"), a grant or duty limited by its own wording and the case falls outside the limit ("in the case of a body corporate", "a person who has been appointed as statutory auditor"), a length fixed outside the sources (the standards of the competent authority that lengthen the bar of 9(1A) beyond the year the Act sets, the amounts the Secretary of State determines), or a borrowed question whose answer the caller does not know (an input of `NOTHING`). Each such branch carries `-- NOTHING-kind (<why>)`, <why> being one of silent, list not closed, includes, undefined term, points outside the text, limited by its own wording.
- A caller must never turn `NOTHING` into `FALSE`. `REFUSE` is not used; "not covered" is `NOTHING`, asserted in the tests.
- A borrowed term (a definition handed to another Act, an EU instrument or a part outside these ranges) is an input of type `MAYBE BOOLEAN`: its `JUST FALSE` is the other instrument's no, supplied by the caller, and its `NOTHING` means the caller does not know it.
- The inputs about judgments the text hands to the Secretary of State ("it appears to him", "such as he considers", "adequate", "fair and reasonable", "satisfactory") are plain `BOOLEAN` inputs stating the fact that the judgment is held; they are never guessed.

## Seams (coa30)

Seam inputs taken as `MAYBE BOOLEAN` and named for the answering section as PLAN.md section 4 says (the lead wires the answering part's function to each at the merge). A name that is not "s N ..." is a borrowed instrument (the Financial Services and Markets Act 2000, the Companies Act 1989, the 2016 Regulations, the 2023 Regulations), asked as a fact because its text is not among the sources.

| input | type | taken by |
| --- | --- | --- |
| `s 1217 the body is a supervisory body` | MAYBE BOOLEAN | coa30-sch10-part1.l4 |
| `s 1221 Approval of third country qualifications` | MAYBE BOOLEAN | coa30-sch10-part2-a.l4 |
| `s 474 Minor definitions` | MAYBE BOOLEAN | coa30-sch10-part2-b.l4 |
| `s 381 Companies subject to the small companies regime` | MAYBE BOOLEAN | coa30-sch10-part2-b.l4 |
| `s 382 the company qualifies as small` | MAYBE BOOLEAN | coa30-sch10-part2-b.l4 |
| `s 383 Companies qualifying as small: parent companies` | MAYBE BOOLEAN | coa30-sch10-part2-b.l4 |
| `s 465 the company qualifies as medium-sized` | MAYBE BOOLEAN | coa30-sch10-part2-b.l4 |
| `s 466 Companies qualifying as medium-sized: parent companies` | MAYBE BOOLEAN | coa30-sch10-part2-b.l4 |
| `s 1253E Working arrangements for transfer of papers: the Secretary of State directs under subsection (6) that the transfer should not take place` | MAYBE BOOLEAN | coa30-sch10-part2-b.l4 |
| `s 1253E the authority has entered into arrangements with the Secretary of State` | MAYBE BOOLEAN | coa30-sch10-part2-b.l4 |
| `regulation 2 of the Statutory Auditors and Third Country Auditors Regulations 2016 as amended from time to time: the requirement is one of the audit reporting requirements` | MAYBE BOOLEAN | coa30-sch10-part2-b.l4 |
| `section 102A(6) of the Financial Services and Markets Act 2000: the person is an issuer` | MAYBE BOOLEAN | coa30-sch10-part2-b.l4 |
| `Schedule 1 to the Recognition of Professional Qualifications and Implementation of International Recognition Agreements (Amendment) Regulations 2023: the state is one of the states specified` | MAYBE BOOLEAN | coa30-sch10-part2-b.l4 |
| `s 1220 Qualifying bodies and recognised professional qualifications` | MAYBE BOOLEAN | coa30-sch11.l4 |
| `section 285 of the Financial Services and Markets Act 2000: the body is a recognised investment exchange, a recognised clearing house or a recognised CSD` | MAYBE BOOLEAN | coa30-sch11a.l4 |
| `section 82 of the Companies Act 1989: the body is an overseas regulatory authority` | MAYBE BOOLEAN | coa30-sch11a.l4 |
| `s 1253B Requests from approved third country competent authorities` | MAYBE BOOLEAN | coa30-sch11a.l4 |
| `s 394 Duty to prepare individual accounts: the body is a company to which section 394 applies` | MAYBE BOOLEAN | coa30-sch13.l4 |

Seams that PLAN.md lists for this range and what became of them: `s 465`, `s 466` (coa10) are inputs of `sch 10 para 13(9)` (`s 465 the company qualifies as medium-sized`, as PLAN.md section 4.2 names it, and `s 466 Companies qualifying as medium-sized: parent companies`); `s 382` is `s 382 the company qualifies as small` and `s 383` (small, parent companies) the heading name; `s 381` is an input of `sch 10 para 13(3)(b)(ii)`; `s 474` (coa10) is an input of `sch 10 para 10A(7)`; `s 1221` (coa26) is an input of `sch 10 para 7A(3)`; `s 1253E` (coa27) is an input of `sch 10 para 16A(2)` and of `sch 10 para 16AB` (the fourth condition), `s 1253B` (coa27) of `sch 11A para 79`; `s 1217` (coa26) and `s 1220` (coa27) answer "supervisory body" and "qualifying body" for `sch 10 para 1(1)` and `sch 11 para 1(1)`; `s 394` (coa8) is an input of `sch 13 para 10(7)`. Cited in the text but not an input because the paragraph only says what the body's rules must say about them: `s 1224`, `s 1239`, `s 1240` (paragraph 18), `s 1217(4)` and `s 1219(13)` (Schedule 11A paragraphs 17A, 17B: asked as the choice of the paragraph), `s 1252` (Schedule 11A paragraphs 13, 17C and 59, Schedule 13: the body designated under it is a fact of the case), `s 1242` (Schedule 12: "obliged to participate" is a fact), `s 457` (Schedule 11A paragraph 18), `s 1224A` (the Schedule's own purpose: the restriction itself is in coa26). `sch 7` (coa29) is cited by paragraph 7(6); the fraction of voting rights in paragraphs 7(4) and 7(5) is the fraction after the rights have been taken into account and attributed as paragraphs 5 to 11 of Schedule 7 direct, which the person states (a seam that PLAN.md lists and that has no separate input here). A seam the plan lacks: Schedule 11A paragraphs 17A to 17D and 79 and 80 depend on Schedule 10 paragraphs 16A, 23 and 24 (paragraphs 23 and 24 are blank in this text).

## What the text turns out to say (numbered findings)

1. Schedule 10 Part 3 (paragraphs 21 to 27, the arrangements for setting standards and for independent monitoring and investigation) shows nothing but dots, under 11 headings that remain (the Part heading and the cross-headings, lines 20379-20399). The requirements those paragraphs once held survive only as cross-references: paragraph 17D of Schedule 11A still refers to "paragraph 23 (independent monitoring of certain audits) or 24 (independent investigation of public interest cases) of Schedule 10", which are blank here.
2. Inline omissions are marked `...` or `. . . .` inside surviving text, and are not encoded: paragraph 6(1)(b) ("in the case of a firm ...—"), 6(1A)(a), 9(1)(a), 9(3)(b), 13(5)(b)(i), 16AA(b) ("... the Secretary of State has approved the transfer"), Schedule 11 paragraph 9(4)(b), and two omitted definitions in 20A(1) (lines 20374 and 20377). The encoding takes the words that remain; a reader who needs the omitted words must look at an earlier version of the Act.
3. The bar on a former auditor joining the audited company's board (paragraphs 9(1A) and 10C(3)) fixes only a minimum: "a period of not less than one year (two years for a public interest entity) determined in standards set by the competent authority". The Act therefore answers JUST TRUE inside the minimum and nothing after it; the standards are outside the sources.
4. Paragraph 12(6) closes its list of four circumstances with "and" after the third (line 20251), and paragraph 12(5)(b) hands the exception back ("unless any of the circumstances mentioned in sub-paragraph (6) applies"): the identity must be published except in those four cases, so outside them the text does not bar publication (the paragraph 12(6) fork).
5. "Majority" in paragraph 7(4) and 7(5) is "a majority of the rights to vote", read as more than half; exactly half is not a majority (tested at 0.5 and 0.51). The alternative "in any other case" test (members with such rights as enable them to direct the overall policy or alter the constitution) is a plain input.
6. Paragraph 8(4) defines "controller" only "in relation to a body corporate", at 15% or more of the votes at general meetings "of the body or another body corporate of which it is a subsidiary"; the encoding answers NOTHING for a person who is not a body corporate.
7. The three-month periods of paragraphs 3(2), 3(5) and 6(3) of Schedule 10 and 3(2) and 3(5) of Schedule 11 are "the period of three months beginning with" a date, so the date itself is the first day and the last day is the day before the corresponding date three months on (1 January: 31 March). The date of effect of a revocation "must be after" that period (10 January: 10 April is the first valid day). The Act does not say how a month-end is counted (the month-end fork).
8. Paragraph 13(3)(b)(ii) sets a six-year inspection cycle for a person who audited, in any of the previous five years, "an entity not subject to the small companies regime (see section 381)", and 13(9) cites sections 382 and 383 for "small" and 465 and 466 for "medium sized": the encoding takes section 381's answer, and sections 382, 383, 465 and 466, as separate inputs, because the text names each.
9. Paragraph 16AB's third condition bites only "where the authority has made the request ... directly to the statutory auditor"; otherwise it is vacuously met. Its fourth condition is a seam (section 1253E).
10. Paragraph 5A(b) says "this Part of the Schedule" where (a) and (c) say "this Part of this Schedule" (line 20093): a drafting slip that changes nothing.
11. Schedule 11 paragraphs 6(4) and 7(2) both fix "not less than seven years' experience in a professional capacity in the fields of finance, law and accountancy"; paragraph 10(1) lets theoretical instruction of at least a year, attested by a recognised examination, be deducted from it, but "not ... by more than four years", so at least three years of experience always remain (tested at 3, 4 and 6 years of instruction). Whether the seven years are in each field or across them is not said (the paragraph 6(4) fork).
12. Schedule 11 paragraph 9(4A) conditions are defined only for a trainer outside the United Kingdom; paragraph 9(5) is blank.
13. Schedule 11A paragraphs 17A to 17D carry cross-references whose antecedent is in paragraph 17A ("as they have effect by virtue of Schedule 5 to the Local Audit and Accountability Act 2014"): 17B and 17C say "that Schedule" and 17D says "that Act" and "that Schedule" (lines 20542-20544), so the paragraphs cannot be read alone. The paragraphs numbered 39(b), 39(c), 40, 53 and 64 of Part 2 are blank; paragraphs 55, 66, 75 and 76 carry their own definitions on the same line as the description (the converter joined appended text to its line).
14. Schedule 13 paragraph 1(1) switches paragraphs on by kind of body: paragraphs 2 to 12 for a body established by the order, paragraphs 2 and 6 to 11 for an existing body (and then paragraphs 2 and 6 only for transferred functions: 1(2)), paragraph 13 only for an existing unincorporated association. Paragraph 10(4) does the same for sub-paragraphs (5) to (8).
15. Schedule 13 paragraph 8(2) gives a person who "shows" that the instrument "had not been made available as required" no contravention: a defence in effect, encoded with the ruling (b) wording of 2026-11-05.
16. In the Part 2 requirements the person's side is provided for by what the body's rules must contain (for example paragraph 14: the rules on admission and expulsion, and on the grant of eligibility and enforcement where those tasks are delegated, "must be fair and reasonable and include adequate provision for appeals"). The encoding states the relation once, between the Secretary of State (who may refuse or revoke recognition) and the body, and states a relation between the person and the body only where the text gives one (a fine "recoverable by the body as a debt due to it", 9(4) and 10C(4); the inspector's three years of independence, 13(5)(e); the report of the inspection made available to the person, 13(11)).
17. Schedules 14, 15 and 16 are 4, 19 and 63 rows of amendments and repeals of other Acts: Schedule 14 amends one section of the Companies (Audit, Investigations and Community Enterprise) Act 2004; Schedule 15 amends the Financial Services and Markets Act 2000 (paragraphs 1 to 12, of which 2 and 9 are blank) and the 2004 Act (paragraphs 13 to 15); Schedule 16 is three tables of repeals (55 table rows: "Company law repeals (Great Britain)", "Repeals and revocations relating to Northern Ireland" and "Other repeals"). All are inert (reason 2), except the blank paragraphs.

## Regulative rules: traces (coa30-tests-regulative.l4)

A `DEONTIC` value cannot be compared with `EQUALS` in an `#ASSERT` on the stable binary (measured on 1.6.110: "These were the values you tried to compare"), and a `#TRACE` prints no assertion line, so `check.sh` counts none for `coa30-tests-regulative.l4`. The results below are what the binary printed for each trace in file order, identical on 1.6.110 and 1.6.109 (compared by diffing the two outputs), and each is the result the text gives (the expectation is written above the trace in the file): the `#EVAL` of a rule prints the rule; a trace in which every limb is performed is `FULFILLED`; a `RAND` of three duties with one left undone prints `FULFILLED AND PARTY ... MUST ...` (the residual); a missed `WITHIN` is `DEONTIC BREACHED` with the `BECAUSE` reason; a `MAY` (paragraph 3(5)) lapses to `FULFILLED` whether or not the representation was made in time, so the trace cannot tell the two apart and the decision function `sch 10 para 3(5) the person may make written and oral representations` (asserted) is the test of the period.

```
Evaluation[1] FULFILLED
Evaluation[2] PARTY `sch 10 para 2(4) the Secretary of State` MUST `sch 10 para 2(4) give the applicant a written notice of the refusal` HENCE FULFILLED
Evaluation[3] FULFILLED
Evaluation[4] FULFILLED AND PARTY `sch 10 para 2(4) the Secretary of State` MUST `sch 10 para 3(3)(b) take reasonably practicable steps to bring the notice to the attention of the members` HENCE FULFILLED
Evaluation[5] FULFILLED
Evaluation[6] FULFILLED
Evaluation[7] FULFILLED
Evaluation[8] FULFILLED
Evaluation[9] DEONTIC BREACHED: BREACH BECAUSE "no summary of the results of inspections was delivered to the Secretary of State in the calendar year (sch 10 para 13(12))"
Evaluation[10] FULFILLED
Evaluation[11] FULFILLED
Evaluation[12] FULFILLED
Evaluation[13] DEONTIC BREACHED: BREACH BECAUSE "the instrument was not printed and made available to the public immediately after it was made (sch 13 para 8(1))"
Evaluation[14] FULFILLED
Evaluation[15] FULFILLED
Evaluation[16] DEONTIC BREACHED: BREACH BECAUSE "no report was made to the Secretary of State in the calendar year (sch 13 para 10(1))"
Evaluation[17] FULFILLED
```

The clock: months for paragraph 3(5) and for "at least once in every calendar year" (13(12), Schedule 13 10(1)); `WITHIN 0` for "immediately" (Schedule 13 8(1)); no deadline where the text states none.

## What the stable binary does not accept, and what it does

Measured on 2026-11-12 with `L4_BIN` (1.6.110, main, e51181d) by running one-file probes; the second list also on `L4_MAIN` (1.6.109).

Rejected (loud): `WHEN `ctor` WITH `field` THEN ...` in a pattern (a parse error, "unexpected WITH"): the positional binding `WHEN `ctor` x THEN ...` is used instead; comparing a `DEONTIC` value in an `#ASSERT` (the error above), so the regulative rules have decision-function twins (the brief's instruction). The modules use none of the constructs the brief forbids (`REFUSE`, `#ASSERT REFUSED`, `BECAUSE` except `LEST BREACH ... BECAUSE`, `YMD`, sets, `TYPICALLY`, a section `GIVEN`, an opaque `DECLARE`, `AFTER ... WITHIN`, `MAY ... LEST`).

Accepted and used: `LEST BREACH BECAUSE "..."`; `RAND`; `WAITUNTIL n` in a trace; `WITHIN 0`; backtick names with commas, parentheses and apostrophes; `Date d m y` with month overflow (`Date 31 15 2025` is 31 March 2026, measured) and `DATE_DAY`, `DATE_MONTH`, `DATE_YEAR`; `MAYBE DATE` and `MAYBE NUMBER` inputs and `CONSIDER` over them; one `§` heading per Schedule and `§§` per Part. Not silent anywhere: every `NOT` is bracketed; no `#ASSERT` continues onto a second line.

What `check.sh` cannot see: a different `#TRACE` outcome on the two builds (compared by hand above: identical), and an assertion a module does not make.

## What `check.sh` prints

Run in this folder as `L4=<L4_BIN> L4_MAIN=<L4_MAIN> ./check.sh` (target `main`: every module is run with 1.6.110 and with 1.6.109 and the four counts compared). `expected_failed` is empty: no assertion is meant to fail. The baseline it replaced: the sandbox held only the keel's `coa-core.l4` and `coa-definitions.l4` (2 modules, 0 assertions; the keel's own run, with its tests module, was 3 modules and 346 satisfied).

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.109 (main, 4c887e0, 2026-11-04)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
coa-core.l4                                    0         0       0        0         0 |      0         0       0        0  same
coa-definitions.l4                             0         0       0        0         0 |      0         0       0        0  same
coa30-cases-seat.l4                            0       135       0        0         0 |      0       135       0        0  same
coa30-regulative.l4                            0         0       0        0         0 |      0         0       0        0  same
coa30-sch10-part1.l4                           0         0       0        0         0 |      0         0       0        0  same
coa30-sch10-part2-a.l4                         0         0       0        0         0 |      0         0       0        0  same
coa30-sch10-part2-b.l4                         0         0       0        0         0 |      0         0       0        0  same
coa30-sch11.l4                                 0         0       0        0         0 |      0         0       0        0  same
coa30-sch11a.l4                                0         0       0        0         0 |      0         0       0        0  same
coa30-sch12.l4                                 0         0       0        0         0 |      0         0       0        0  same
coa30-sch13.l4                                 0         0       0        0         0 |      0         0       0        0  same
coa30-seat.l4                                  0         0       0        0         0 |      0         0       0        0  same
coa30-tests-regulative.l4                      0         0       0        0         0 |      0         0       0        0  same
coa30-tests-sch10-part1.l4                     0        95       0        0         0 |      0        95       0        0  same
coa30-tests-sch10-part2-a.l4                   0       107       0        0         0 |      0       107       0        0  same
coa30-tests-sch10-part2-b.l4                   0       263       0        0         0 |      0       263       0        0  same
coa30-tests-sch11.l4                           0       146       0        0         0 |      0       146       0        0  same
coa30-tests-sch11a.l4                          0       131       0        0         0 |      0       131       0        0  same
coa30-tests-sch12.l4                           0        34       0        0         0 |      0        34       0        0  same
coa30-tests-sch13.l4                           0       101       0        0         0 |      0       101       0        0  same
TOTAL (20 modules)                             0      1012       0        0           |      0      1012       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

## Open questions for a domain expert

1. Is a bare "The body must have ..." paragraph of Part 2 a condition of recognition (the encoding's reading: JUST FALSE when unmet), or only a duty on the body for which the Act states no consequence (NOTHING)? About 45 sites, one fork line each.
2. How is a month-end counted in "the period of three months beginning with" a date (the month-end fork)?
3. Does the bar of paragraph 9(1A) and 10C(3) continue for exactly the standards' period, and may the standards shorten it below one (two) years (the encoding says no: "not less than")?
4. Are the lists of Schedule 11A (persons, descriptions) closed by section 1224A (the encoding answers NOTHING for a person or purpose no paragraph names, JUST FALSE would follow if section 1224A closes the list)?
5. May a firm that has ceased to comply remain eligible for three months from the day it ceased (paragraph 6(3)), or from the day permission is given?
6. Is "seven years' experience ... in the fields of finance, law and accountancy" (Schedule 11 paragraphs 6(4), 7(2)) seven years across the fields or in each?
7. Is the seat as read here (the people who deal with a company as auditor, qualification-holder, member of the delegated body, holder of Part 42 information, or director asking about the auditor) the intended reading of "who deals with one" for these Schedules?

## Copied modules

None. `coa-core.l4` and `coa-definitions.l4` are the keel's, read-only, and sit in this folder unchanged; no coa30 module imports either (the modules import `prelude` and `daydate`, and each other where a helper is shared), because no core type is used. `coa30-regulative.l4` declares its own party and act types because a `DEONTIC` takes one party type and the core's `Party` lacks the supervisory body, the registered third country auditor and the delegated body (NEEDS-CORE.md).

## Peeked

Nothing. No file under `<local path>`, `<local worktrees>` or `canon`, no directory under the runs directory other than `dst-coa30/`, and nothing under `<local tool>` was opened. The memory index in the system prompt was not followed.
