# NOTES: coa8 (Companies Act 2006, United Kingdom: Part 14 and Part 15 as far as section 414B)

Range: lines 4656 to 5417 of `ukpga-2006-46.txt`: Part 14 (control of political donations and expenditure, ss 362 to 379) and Part 15 (accounts and reports) Chapters 1 to 4 and 4A as far as s 414B (ss 380 to 414B).
Written by the part agent `coa8`, run `dst-coa8`, on 2026-11-13, model Sonnet 5.5.
Status: every module and test file compiles and runs on the stable binary 1.6.110 (main, e51181d, 2026-11-11) with no error or warning diagnostic, and the numbers `check.sh` printed are in "What check.sh prints" below.
The same files give the same four counts on the second stable build, 1.6.109 (main, 4c887e0, 2026-11-04).
`srcrefs.py check --refs` and `--strict` report 0 problems.
Not reviewed by a lawyer.

**About the source.**
The text is a plain-text rendering of the Act produced by a converter from legislation.gov.uk (Open Government Licence v3.0), not the official text.
Nothing here is "verified against the official text".
Where the rendering shows a provision as dots (`. . . .`) the coverage table says "repealed or blank in this text" and says only what the text shows.

**What is in this folder (files written by coa8).**
Layer 1, the law, objectively: `coa8-helpers.l4`, `coa8-part14-meanings.l4`, `coa8-part14-authorisation.l4`, `coa8-part14-remedies.l4`, `coa8-part14-exemptions.l4`, `coa8-part15-small.l4`, `coa8-part15-records.l4`, `coa8-part15-year.l4`, `coa8-part15-accounts.l4`, `coa8-part15-group.l4`, `coa8-part15-notes.l4`, `coa8-part15-approval.l4`, `coa8-regulative.l4`.
Tests: one `coa8-tests-<module>.l4` for each of the first twelve modules (the regulative module is run with `#TRACE`, see "What the stable binary does not accept").
Layer 2, the seat: `coa8-seat.l4` (171 questions) and `coa8-cases-seat.l4`.
Notes: this file, `PROGRESS.md`, and `NEEDS-CORE.md` (one hoist candidate; nothing was blocked on it).
`coa-core.l4`, `coa-definitions.l4`, `check.sh`, `srcrefs.py`, `fetch-main-l4.sh` are the keel's and were not edited.

**How layer 1 is written.**
Each rule carries `@ref` and the source lines it implements as `-- src:N | text` lines that were copied mechanically from the text by `srcrefs.py quote`.
Every top-level name (function, type, constructor, record field, constant) begins with the label of its provision, as in `s 366(2) ...`.
A decision function answers `MAYBE BOOLEAN` (or `MAYBE DATE`, `MAYBE NUMBER`, `MAYBE Penalty`) so that "not covered" stays distinct from "no".
Three-valued composition goes through the helpers of `coa8-helpers.l4` (`s 362 helper either answer`, `both answers`, `the opposite answer`, `every answer`, `some answer`), which are strong Kleene: a limb that decides, decides, and NOTHING survives only where no limb decides.
Amounts, periods and thresholds the Act states (the small-company and micro-entity limits, the 5,000 pounds, the 28 days) are the Act's own and are constants named for their section; amounts left to regulations or to the Secretary of State (the interest rate of s 369(5)(b), the orders of s 377) are inputs.
The duties are encoded twice: as decision functions (the tested form: `check.sh` counts their assertions) and, for the principal duties, as regulative rules in `coa8-regulative.l4`.

## Rulings applied (coa8)

The brief records these rulings; each is reproduced here word for word, because this range carries `NOTHING-kind` tags and so applies them.

The fork register below says which sites each one decides.

- **E1** (bench `commons-negation-1030`; should a legal effect be one definition gathered from every section that gives it?): option B, as guidance for gathering a legal effect's routes by hand only, with no pilot run; option A (gathering by bare name) is withdrawn as a direction for the language, not deferred; option C (per-section answers) applies everywhere else; the Magna Carta pilot in the printed recommendation (chapters 2, 3, 4, 5, 37, 43, 46 and 53, with a blind second reader) is not to be run. The maintainer's lean, verbatim: "B but generally uncomfortable with this much magic because it takes the language from unopinionated to opinionated in ways that are hard to teach an l4 novice." the maintainer's note, verbatim: "Fundamentally I feel like we are trying to make the language do work that the human l4 drafter should do. Too much magic. Can’t we just decline to be this opinionated and say the programmer needs to do this thinking?" Marked 2026-11-03T23:19:02.812Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23

- **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. The maintainer's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." the maintainer's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23

- **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. The maintainer's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

- **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. The maintainer approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

- **Questions with no convention: decide case by case (the maintainer, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. The maintainer's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with the coordinator where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

How they are used here: E1 (option C, per-section answers) governs how the sections of Part 14 give their effects, one function per section; N2 (flat negatives count as a no) is the basis of every `FALSE-kind` tag on a "does not", "may not" or "is not" and the Hohfeld kinds stay in "Jural relations (coa8)"; the periods ruling decides the 28 days of s 371(2), the three or six years of s 388(4) and the six months of s 400(1) (JUST FALSE outside the period) and the scope limits of s 363(3) and s 366(1) (NOTHING); the delegated-definitions ruling decides the defences of ss 387(2) and 389(2) (JUST FALSE, "this section gives no defence on these facts") and the s 377 and s 409 orders and regulations (inputs); the case-by-case ruling is the licence for each fork below.

## Coverage (coa8)

One row per unit of the text of lines 4656 to 5417: every heading and cross-heading, every section, every subsection, paragraph and sub-paragraph, every row of a table, and every defined term, each with exactly one disposition.

A row for a paragraph or a lead-in takes the function of the block that quotes it (the narrowest `@ref`); a row for a section line takes the first encoded rule below it.

"Tests" is the number of `#ASSERT` lines in the coa8 test files that mention the rule or any rule of the same block; "Seat" gives the numbers of the seat questions that call it (see "Seat layer"); a blank seat cell means the rule asks for a typed input the seat cannot take as a plain fact, or no person-facing question was written for it.

Dispositions: `encoded`, `fork` (the row names its entry in the fork register; the rule is encoded, in the reading taken), `inert` (with its reason number 1, 2 or 3), `repealed or blank in this text`. There is no `out-of-scope` or `deferred` row.

### Counts

| disposition | rows |
| --- | --- |
| encoded | 652 |
| fork | 19 |
| inert | 51 |
| repealed or blank in this text | 11 |
| total | 733 |

Inert rows by reason: reason 1: 29, reason 2: 22 (no row is inert for reason 3: the rows that show only dots are `repealed or blank in this text`).

### Audit: the text counted, and every line placed

The audit is a script (`cov.py` in the work folder) that reads lines 4656 to 5417 of the raw text and counts units from the text alone (the table is generated from the same parse, so the independent check is that every non-blank line falls inside a unit, below): lines that begin with a tab are headings (23), lines that begin with a section number and a tab are sections (61), lines that begin with `(x)` are subsections or paragraphs (607), lines that begin `n. ... |` are table rows (9), and a defined term is a quoted term followed by "means", "includes", "has the meaning", "does not include", "are to" or "is to", or a quoted term in brackets (33).

The range has 762 non-blank lines; every one of them falls inside a unit (the script reports "lines in no unit: 0").

Rows before the audit pass (headings, sections, subsections, paragraphs, table rows): 700. Rows after adding the defined terms the audit found: 733. Text units counted: 700, plus 33 defined terms. The table has no unit the count does not have and the count has none the table lacks.

### The table

| unit | lines | disposition | L4 rule, or why not | tests | seat |
| --- | --- | --- | --- | --- | --- |
| heading: Part 14 — Control of political donations and expenditure | 4656 | inert | reason 1: heading |  |  |
| heading: Introductory | 4657 | inert | reason 1: heading |  |  |
| s 362 | 4658-4659 | inert | reason 1: states what the Part is about and creates no rule |  |  |
| s 362(a) | 4660 | inert | reason 1: states what the Part is about and creates no rule |  |  |
| s 362(b) | 4661 | inert | reason 1: states what the Part is about and creates no rule |  |  |
| heading: Donations and expenditure to which this Part applies | 4662 | inert | reason 1: heading |  |  |
| s 363 | 4663 | encoded | `s 363(1) this Part applies to the political party` | 2 | 1 |
| s 363(1) | 4664 | encoded | `s 363(1) this Part applies to the political party` | 2 | 1 |
| s 363(2) | 4665 | encoded | `s 363(2) the organisation is a political organisation` | 6 | 3 |
| s 363(2)(a) | 4666 | encoded | `s 363(2)(a) the activities are intended to affect public support for a party or candidate to which this Part applies` | 5 | 3 |
| s 363(2)(b) | 4667 | encoded | `s 363(2)(b) the activities are intended to influence voters in a referendum` | 2 | 3 |
| s 363(3) | 4668 | encoded | `s 363(3) this Part applies to the independent election candidate` | 2 | 2 |
| s 363(4) | 4669 | encoded | `s 363(4) the reference is to a party, organisation, candidate or expenditure to which this Part applies` (+1 more in the block) | 11 |  |
| s 364 | 4670 | encoded | `s 364(2)(a) the thing is a political donation to the political party or other political organisation` (+1 more in the block) | 7 | 4 |
| s 364(1) | 4671 | inert | reason 1: a lead-in ("The following provisions have effect ... as regards the meaning"), fork F1 |  |  |
| s 364(2) | 4672 | encoded | `s 364(2)(a) the thing is a political donation to the political party or other political organisation` (+1 more in the block) | 7 | 4 |
| s 364(2)(a) | 4673 | encoded | `s 364(2)(a) the thing is a political donation to the political party or other political organisation` (+1 more in the block) | 7 | 4 |
| s 364(2)(a)(i) | 4674 | encoded | `s 364(2)(a) the thing is a political donation to the political party or other political organisation` (+1 more in the block) | 7 | 4 |
| s 364(2)(a)(ii) | 4675-4676 | encoded | `s 364(2)(a) the thing is a political donation to the political party or other political organisation` (+1 more in the block) | 7 | 4 |
| s 364(2)(b) | 4677 | encoded | `s 364(2)(a) the thing is a political donation to the political party or other political organisation` (+1 more in the block) | 7 | 4 |
| s 364(3) | 4678 | encoded | `s 364(3)(a) the thing is a political donation to the independent election candidate` (+1 more in the block) | 5 | 4 |
| s 364(3)(a) | 4679-4680 | encoded | `s 364(3)(a) the thing is a political donation to the independent election candidate` (+1 more in the block) | 5 | 4 |
| s 364(3)(b) | 4681 | encoded | `s 364(3)(a) the thing is a political donation to the independent election candidate` (+1 more in the block) | 5 | 4 |
| s 364(4) | 4682 | encoded | `s 364(4) the answer under sections 50 and 53 to use for this section` | 3 | 4 |
| s 365 | 4683 | encoded | `s 365(1) the expenditure is political expenditure` | 4 | 5 |
| s 365(1) | 4684 | encoded | `s 365(1) the expenditure is political expenditure` | 4 | 5 |
| s 365(1)(a) | 4685 | encoded | `s 365(1)(a) the expenditure is on advertising or publicity material intended to affect public support` | 6 | 5 |
| s 365(1)(a)(i) | 4686 | encoded | `s 365(1)(a) the expenditure is on advertising or publicity material intended to affect public support` | 6 | 5 |
| s 365(1)(a)(ii) | 4687-4688 | encoded | `s 365(1)(a) the expenditure is on advertising or publicity material intended to affect public support` | 6 | 5 |
| s 365(1)(b) | 4689 | encoded | `s 365(1)(b) the expenditure is on activities intended to affect public support or to influence referendum voters` | 8 | 5 |
| s 365(1)(b)(i) | 4690 | encoded | `s 365(1)(b) the expenditure is on activities intended to affect public support or to influence referendum voters` | 8 | 5 |
| s 365(1)(b)(ii) | 4691 | encoded | `s 365(1)(b) the expenditure is on activities intended to affect public support or to influence referendum voters` | 8 | 5 |
| s 365(2) | 4692 | encoded | `s 365(2) the spending counts as political expenditure` | 7 | 5 |
| heading: Authorisation required for donations or expenditure | 4693 | inert | reason 1: heading |  |  |
| s 366 | 4694 | encoded | `s 366(1) the company is forbidden to make the donation or incur the expenditure` (+3 more in the block) | 5 | 6 |
| s 366(1) | 4695 | encoded | `s 366(1) the company is forbidden to make the donation or incur the expenditure` (+3 more in the block) | 5 | 6 |
| s 366(1)(a) | 4696 | encoded | `s 366(1) the company is forbidden to make the donation or incur the expenditure` (+3 more in the block) | 5 | 6 |
| s 366(1)(b) | 4697-4698 | encoded | `s 366(1) the company is forbidden to make the donation or incur the expenditure` (+3 more in the block) | 5 | 6 |
| s 366(2) | 4699 | fork | `s 366(2) the donation or expenditure is authorised as section 366(2) requires` (fork F6) | 12 | 6 |
| s 366(2)(a) | 4700 | encoded | `s 366(2) the donation or expenditure is authorised as section 366(2) requires` | 12 | 6 |
| s 366(2)(b) | 4701 | encoded | `s 366(2) the donation or expenditure is authorised as section 366(2) requires` | 12 | 6 |
| s 366(2)(b)(i) | 4702 | encoded | `s 366(2) the donation or expenditure is authorised as section 366(2) requires` | 12 | 6 |
| s 366(2)(b)(ii) | 4703 | encoded | `s 366(2) the donation or expenditure is authorised as section 366(2) requires` | 12 | 6 |
| s 366(3) | 4704 | fork | `s 366(3) no resolution is required on the part of the company` (fork F6) | 3 | 6 |
| s 366(4) | 4705 | encoded | `s 366(4) the other company is a relevant holding company` | 7 | 7 |
| s 366(4)(a) | 4706 | encoded | `s 366(4) the other company is a relevant holding company` | 7 | 7 |
| s 366(4)(b) | 4707 | encoded | `s 366(4) the other company is a relevant holding company` | 7 | 7 |
| s 366(4)(c) | 4708 | encoded | `s 366(4) the other company is a relevant holding company` | 7 | 7 |
| s 366(5) | 4709 | encoded | `s 366(5) the resolution or resolutions meet the requirements of subsection (5)` | 7 | 6 |
| s 366(5)(a) | 4710 | encoded | `s 366(5) the resolution or resolutions meet the requirements of subsection (5)` | 7 | 6 |
| s 366(5)(b) | 4711 | encoded | `s 366(5) the resolution or resolutions meet the requirements of subsection (5)` | 7 | 6 |
| s 366(6) | 4712 | encoded | `s 366(6) section 366 enables the company to be authorised to do it` | 2 | 8 |
| s 367 | 4713 | encoded | `s 367 the resolution is in the form section 367 requires` | 4 | 9 |
| s 367(1) | 4714 | encoded | `s 367(1) the resolution may relate to` | 4 | 9 |
| s 367(1)(a) | 4715 | encoded | `s 367(1) the resolution may relate to` | 4 | 9 |
| s 367(1)(b) | 4716 | encoded | `s 367(1) the resolution may relate to` | 4 | 9 |
| s 367(1)(c) | 4717 | encoded | `s 367(1) the resolution may relate to` | 4 | 9 |
| s 367(2) | 4718 | encoded | `s 367(2) the resolution may be expressed to relate to all the subsidiaries without identifying them individually` (+1 more in the block) | 3 |  |
| s 367(2)(a) | 4719 | encoded | `s 367(2) the resolution may be expressed to relate to all the subsidiaries without identifying them individually` (+1 more in the block) | 3 |  |
| s 367(2)(b) | 4720-4721 | encoded | `s 367(2) the resolution may be expressed to relate to all the subsidiaries without identifying them individually` (+1 more in the block) | 3 |  |
| s 367(3) | 4722 | encoded | `s 367(3) the resolution may authorise donations or expenditure under the head` | 4 |  |
| s 367(3)(a) | 4723 | encoded | `s 367(3) the resolution may authorise donations or expenditure under the head` | 4 |  |
| s 367(3)(b) | 4724 | encoded | `s 367(3) the resolution may authorise donations or expenditure under the head` | 4 |  |
| s 367(3)(c) | 4725 | encoded | `s 367(3) the resolution may authorise donations or expenditure under the head` | 4 |  |
| s 367(4) | 4726 | encoded | `s 367(4) the resolution specifies the head or heads as required` | 4 | 9 |
| s 367(4)(a) | 4727 | encoded | `s 367(4) the resolution specifies the head or heads as required` | 4 | 9 |
| s 367(4)(b) | 4728 | encoded | `s 367(4) the resolution specifies the head or heads as required` | 4 | 9 |
| s 367(5) | 4729 | encoded | `s 367(5) the resolution is expressed in general terms as required` | 3 | 9 |
| s 367(6) | 4730 | encoded | `s 367(6) the resolution authorises up to a specified amount for each head` | 2 | 9 |
| s 367(7) | 4731 | encoded | `s 367(7) the resolution specifies the amounts as required` | 4 | 9 |
| s 367(7)(a) | 4732 | encoded | `s 367(7) the resolution specifies the amounts as required` | 4 | 9 |
| s 367(7)(b) | 4733 | encoded | `s 367(7) the resolution specifies the amounts as required` | 4 | 9 |
| s 368 | 4734 | encoded | `s 368(1) the last day on which the resolution has effect` (+2 more in the block) | 13 | 10 |
| s 368(1) | 4735 | fork | `s 368(1) the last day on which the resolution has effect` (fork F9) | 13 | 10 |
| s 368(2) | 4736 | encoded | `s 368(2) the directors have power to determine a shorter period` (+1 more in the block) | 7 | 11 |
| heading: Remedies in case of unauthorised donations or expenditure | 4737 | inert | reason 1: heading |  |  |
| s 369 | 4738 | encoded | `s 369(1) section 369 applies` | 5 | 12 |
| s 369(1) | 4739 | encoded | `s 369(1) section 369 applies` | 5 | 12 |
| s 369(2) | 4740 | encoded | `s 369(2) the person is jointly and severally liable to make good and to compensate the company` (+2 more in the block) | 4 | 12 |
| s 369(2)(a) | 4741 | encoded | `s 369(2)(a) the amount of the unauthorised donation or expenditure still to be made good to the company` | 3 | 14 |
| s 369(2)(b) | 4742 | encoded | `s 369(2)(b) the amount to compensate the company for loss or damage` | 2 |  |
| s 369(3) | 4743 | encoded | `s 369(3) the person is one of the directors in default` | 8 | 12 |
| s 369(3)(a) | 4744 | encoded | `s 369(3) the person is one of the directors in default` | 8 | 12 |
| s 369(3)(b) | 4745 | encoded | `s 369(3) the person is one of the directors in default` | 8 | 12 |
| s 369(3)(b)(i) | 4746 | encoded | `s 369(3) the person is one of the directors in default` | 8 | 12 |
| s 369(3)(b)(ii) | 4747-4748 | encoded | `s 369(3) the person is one of the directors in default` | 8 | 12 |
| s 369(4) | 4749 | encoded | `s 369(4) the other company is a relevant holding company` | 3 |  |
| s 369(4)(a) | 4750 | encoded | `s 369(4) the other company is a relevant holding company` | 3 |  |
| s 369(4)(b) | 4751 | encoded | `s 369(4) the other company is a relevant holding company` | 3 |  |
| s 369(4)(c) | 4752 | encoded | `s 369(4) the other company is a relevant holding company` | 3 |  |
| s 369(5) | 4753 | encoded | `s 369(5) the amount on which interest runs` | 2 |  |
| s 369(5)(a) | 4754 | encoded | `s 369(5)(a) the date from which interest runs` | 2 |  |
| s 369(5)(b) | 4755-4756 | encoded | `s 369(5)(b) the rate of interest` | 2 |  |
| s 369(6) | 4757 | encoded | `s 369(6) the amount of the donation or expenditure to which this section applies` | 3 | 13 |
| s 370 | 4758 | encoded | `s 370(1)(a) the liability is enforceable in the name of the company by the group` | 4 |  |
| s 370(1) | 4759 | encoded | `s 370(1)(a) the liability is enforceable in the name of the company by the group` | 4 |  |
| s 370(1)(a) | 4760 | encoded | `s 370(1)(a) the liability is enforceable in the name of the company by the group` | 4 |  |
| s 370(1)(b) | 4761 | encoded | `s 370(1)(b) the liability is enforceable in the name of the subsidiary by the group` | 5 |  |
| s 370(1)(b)(i) | 4762 | encoded | `s 370(1)(b) the liability is enforceable in the name of the subsidiary by the group` | 5 |  |
| s 370(1)(b)(ii) | 4763 | encoded | `s 370(1)(b) the liability is enforceable in the name of the subsidiary by the group` | 5 |  |
| s 370(2) | 4764 | encoded | `s 370(2) the company may itself bring proceedings to enforce the liability` | 2 |  |
| s 370(3) | 4765 | fork | `s 370(3) the members are an authorised group` (fork F10) | 8 | 15 |
| s 370(3)(a) | 4766 | encoded | `s 370(3) the members are an authorised group` | 8 | 15 |
| s 370(3)(b) | 4767 | encoded | `s 370(3) the members are an authorised group` | 8 | 15 |
| s 370(3)(c) | 4768 | encoded | `s 370(3) the members are an authorised group` | 8 | 15 |
| s 370(4) | 4769 | encoded | `s 370(4) the group may bring proceedings under section 370` | 4 |  |
| s 370(5) | 4770 | encoded | `s 370(5) the member's right to bring or continue proceedings under Part 11 is unaffected` | 3 |  |
| s 371 | 4771 | encoded | `s 371(1) the notice requirements are met` (+3 more in the block) | 6 | 16 |
| s 371(1) | 4772 | encoded | `s 371(1) the notice requirements are met` (+3 more in the block) | 6 | 16 |
| s 371(1)(a) | 4773 | encoded | `s 371(1) the notice requirements are met` (+3 more in the block) | 6 | 16 |
| s 371(1)(a)(i) | 4774 | encoded | `s 371(1) the notice requirements are met` (+3 more in the block) | 6 | 16 |
| s 371(1)(a)(ii) | 4775 | encoded | `s 371(1) the notice requirements are met` (+3 more in the block) | 6 | 16 |
| s 371(1)(a)(iii) | 4776 | encoded | `s 371(1) the notice requirements are met` (+3 more in the block) | 6 | 16 |
| s 371(1)(b) | 4777 | encoded | `s 371(1) the notice requirements are met` (+3 more in the block) | 6 | 16 |
| s 371(2) | 4778 | fork | `s 371(2) the director may apply to the court for an order that the proposed proceedings shall not be brought` (fork F11) | 7 | 17 |
| s 371(2)(a) | 4779 | encoded | `s 371(2) the director may apply to the court for an order that the proposed proceedings shall not be brought` (+2 more in the block) | 7 | 17 |
| s 371(2)(b) | 4780 | encoded | `s 371(2) the director may apply to the court for an order that the proposed proceedings shall not be brought` (+2 more in the block) | 7 | 17 |
| s 371(2)(c) | 4781 | encoded | `s 371(2) the director may apply to the court for an order that the proposed proceedings shall not be brought` (+2 more in the block) | 7 | 17 |
| s 371(3) | 4782 | encoded | `s 371(3) the court may make the alternative directions` | 2 | 18 |
| s 371(3)(a) | 4783 | encoded | `s 371(3) the court may make the alternative directions` | 2 | 18 |
| s 371(3)(b) | 4784 | encoded | `s 371(3) the court may make the alternative directions` | 2 | 18 |
| s 371(3)(b)(i) | 4785 | encoded | `s 371(3) the court may make the alternative directions` | 2 | 18 |
| s 371(3)(b)(ii) | 4786 | encoded | `s 371(3) the court may make the alternative directions` | 2 | 18 |
| s 371(4) | 4787-4788 | encoded | `s 371(4) the members owe the company the same duties as the directors would owe` | 2 |  |
| s 371(5) | 4789 | encoded | `s 371(5) the group may discontinue or settle the proceedings` | 2 | 20 |
| s 372 | 4790 | encoded | `s 372(1) section 372 applies to the proceedings` | 2 |  |
| s 372(1) | 4791 | encoded | `s 372(1) section 372 applies to the proceedings` | 2 |  |
| s 372(2) | 4792-4793 | encoded | `s 372(2) the group may apply for an order that the company indemnify the group in respect of costs` | 3 |  |
| s 372(3) | 4794 | encoded | `s 372(3) the group is entitled to be paid costs out of the assets of the company` | 2 | 21 |
| s 372(4) | 4795 | encoded | `s 372(4)(a) the costs shall be paid to the group` | 3 | 22 |
| s 372(4)(a) | 4796 | encoded | `s 372(4)(a) the costs shall be paid to the group` | 3 | 22 |
| s 372(4)(b) | 4797 | encoded | `s 372(4)(b) the costs shall be paid by the group` | 3 | 23 |
| s 372(5) | 4798 | encoded | `s 372(5) the word to read for costs` (+1 more in the block) | 4 |  |
| s 373 | 4799 | encoded | `s 373(1) the group is entitled to require the company to provide the information` (+2 more in the block) | 4 | 24 |
| s 373(1) | 4800 | encoded | `s 373(1) the group is entitled to require the company to provide the information` (+2 more in the block) | 4 | 24 |
| s 373(2) | 4801 | encoded | `s 373(2) the court may order the company and specified officers or employees to provide the information` | 3 | 25 |
| s 373(2)(a) | 4802 | encoded | `s 373(2) the court may order the company and specified officers or employees to provide the information` | 3 | 25 |
| s 373(2)(b) | 4803-4804 | encoded | `s 373(2) the court may order the company and specified officers or employees to provide the information` | 3 | 25 |
| heading: Exemptions | 4805 | inert | reason 1: heading |  |  |
| s 374 | 4806 | encoded | `s 374(1) the donation to the trade union is a political donation for the purposes of this Part` | 5 | 26 |
| s 374(1) | 4807 | encoded | `s 374(1) the donation to the trade union is a political donation for the purposes of this Part` | 5 | 26 |
| s 374(2) | 4808 | encoded | `s 374(2) the trade union is a political organisation for the purposes of section 365` | 3 |  |
| s 374(3) | 4809-4811 | encoded | `s 374(3) the body is a trade union` | 5 |  |
| s 375 | 4812 | encoded | `s 375(1) the subscription is a political donation for the purposes of this Part` | 4 | 27 |
| s 375(1) | 4813 | encoded | `s 375(1) the subscription is a political donation for the purposes of this Part` | 4 | 27 |
| s 375(2) | 4814-4816 | encoded | `s 375(2) the organisation is a trade association` | 2 |  |
| s 376 | 4817 | encoded | `s 376(1) the group is a political organisation for the purposes of this Part` | 3 | 29 |
| s 376(1) | 4818 | encoded | `s 376(1) the group is a political organisation for the purposes of this Part` | 3 | 29 |
| s 376(2) | 4819 | encoded | `s 376(2) the group is an all-party parliamentary group` | 3 | 29 |
| s 377 | 4820 | encoded | `s 377(1) authorisation under this Part is not needed for the political expenditure` | 3 | 30 |
| s 377(1) | 4821 | encoded | `s 377(1) authorisation under this Part is not needed for the political expenditure` | 3 | 30 |
| s 377(2) | 4822 | inert | reason 2: order-making machinery (what an order may cover), fork F2 |  |  |
| s 377(2)(a) | 4823 | inert | reason 2: order-making machinery, fork F2 |  |  |
| s 377(2)(b) | 4824-4825 | inert | reason 2: order-making machinery, fork F2 |  |  |
| s 377(3) | 4826 | encoded | `s 377(3) the amount of the expenditure counted in determining what a resolution authorises` | 3 |  |
| s 377(4) | 4827 | inert | reason 2: order-making procedure (affirmative resolution), fork F2 |  |  |
| s 378 | 4828 | encoded | `s 378(1) the part of this donation for which authorisation is needed` (+1 more in the block) | 7 | 31 |
| s 378(1) | 4829 | encoded | `s 378(1) the part of this donation for which authorisation is needed` (+1 more in the block) | 7 | 31 |
| s 378(1)(a) | 4830 | encoded | `s 378(1) the part of this donation for which authorisation is needed` (+1 more in the block) | 7 | 31 |
| s 378(1)(b) | 4831-4832 | encoded | `s 378(1)(b) the other donation falls in the period of 12 months ending with the date of this donation` | 6 | 32 |
| s 378(2) | 4833-4835 | fork | `s 378(2) the payment is a donation for the purposes of this section` (fork F4) | 2 |  |
| s 378(2)(a) | 4836 | encoded | `s 378(2) the other donation is an other relevant donation` | 12 | 33 |
| s 378(2)(b) | 4837 | encoded | `s 378(2) the other donation is an other relevant donation` | 12 | 33 |
| s 378(3) | 4838 | encoded | `s 378(3) the amount of this donation counted in determining what a resolution authorises` | 2 |  |
| heading: Supplementary provisions | 4839 | inert | reason 1: heading |  |  |
| s 379 | 4840 | encoded | `s 379(1) the person is a director for the purposes of this Part` | 5 | 34 |
| s 379(1) | 4841-4843 | encoded | `s 379(1) the person is a director for the purposes of this Part` | 5 | 34 |
| s 379(2) | 4844 | encoded | `s 379(2) the time at which the donation is made or the expenditure is incurred` | 4 | 35 |
| heading: Part 15 — Accounts and reports | 4845 | inert | reason 1: heading |  |  |
| heading: Chapter 1 — Introduction | 4846 | inert | reason 1: heading |  |  |
| heading: General | 4847 | inert | reason 1: heading |  |  |
| s 380 | 4848 | encoded | `s 380(1) the requirements of this Part as to accounts and reports apply in relation to the period` | 2 | 36 |
| s 380(1) | 4849 | encoded | `s 380(1) the requirements of this Part as to accounts and reports apply in relation to the period` | 2 | 36 |
| s 380(2) | 4850 | inert | reason 1: "In certain respects different provisions apply to different kinds of company" creates no rule |  |  |
| s 380(3) | 4851 | repealed or blank in this text | the text shows only dots |  |  |
| s 380(4) | 4852 | repealed or blank in this text | the text shows only dots |  |  |
| heading: Companies subject to the small companies regime | 4853 | inert | reason 1: heading |  |  |
| s 381 | 4854-4855 | encoded | `s 381 the small companies regime applies to the company for the financial year` | 7 | 37 |
| s 381(a) | 4856 | encoded | `s 381 the small companies regime applies to the company for the financial year` | 7 | 37 |
| s 381(b) | 4857 | encoded | `s 381 the small companies regime applies to the company for the financial year` | 7 | 37 |
| s 382 | 4858 | encoded | `s 382(1) the company qualifies as small in its first financial year` | 3 | 40 |
| s 382(1) | 4859 | encoded | `s 382(1) the company qualifies as small in its first financial year` | 3 | 40 |
| s 382(1A) | 4860 | encoded | `s 382(1A) the company qualifies as small in a subsequent financial year` | 7 | 39 |
| s 382(2) | 4861 | fork | `s 382(2) the change in whether the qualifying conditions are met affects the company's qualification` (fork F14) | 5 |  |
| s 382(3) | 4862 | encoded | `s 382(3) the qualifying conditions are met in the year` | 10 | 38 |
| s 382(3) row 1 | 4863 | encoded | `s 382(3) the turnover limit, in pounds` (+1 more in the block) | 5 |  |
| s 382(3) row 2 | 4864 | encoded | `s 382(3) the balance sheet total limit, in pounds` (+1 more in the block) | 3 |  |
| s 382(3) row 3 | 4865 | encoded | `s 382(3) the employees limit` (+1 more in the block) | 4 |  |
| s 382(4) | 4866 | encoded | `s 382(4) the maximum figure for turnover adjusted to the length of the period` | 2 |  |
| s 382(5) | 4867 | encoded | `s 382(5) the balance sheet total` | 2 |  |
| s 382(6) | 4868 | encoded | `s 382(6) the number of employees` | 4 | 41 |
| s 382(6)(a) | 4869 | encoded | `s 382(6) the number of employees` | 4 | 41 |
| s 382(6)(b) | 4870 | encoded | `s 382(6) the number of employees` | 4 | 41 |
| s 382(6)(c) | 4871 | encoded | `s 382(6) the number of employees` | 4 | 41 |
| s 382(7) | 4872 | inert | reason 1: a signpost ("subject to section 383"), fork F1 |  |  |
| s 383 | 4873 | encoded | `s 383(1) the parent company qualifies as a small company` | 5 | 44 |
| s 383(1) | 4874 | encoded | `s 383(1) the parent company qualifies as a small company` | 5 | 44 |
| s 383(2) | 4875 | encoded | `s 383(2) the group qualifies as small in the parent company's first financial year` | 3 |  |
| s 383(2A) | 4876 | encoded | `s 383(2A) the group qualifies as small in a subsequent financial year` | 5 | 43 |
| s 383(3) | 4877 | fork | `s 383(3) the change in whether the group meets the qualifying conditions affects the group's qualification` (fork F14) | 3 |  |
| s 383(4) | 4878 | encoded | `s 383(4) the qualifying conditions are met by the group in the year` | 5 | 42 |
| s 383(4) row 1 | 4879 | encoded | `s 383(4) row 1 the aggregate turnover is not more than the limit` | 3 |  |
| s 383(4) row 2 | 4880 | encoded | `s 383(4) row 2 the aggregate balance sheet total is not more than the limit` | 3 |  |
| s 383(4) row 3 | 4881 | encoded | `s 383(4) row 3 the aggregate number of employees is not more than the limit` | 2 |  |
| s 383(5) | 4882 | encoded | `s 383(5) the aggregate figure` (+1 more in the block) | 2 |  |
| s 383(6) | 4883-4884 | encoded | `s 383(6) the net figure` | 4 |  |
| s 383(6)(a) | 4885 | encoded | `s 383(6) the net figure` | 4 |  |
| s 383(6)(b) | 4886-4888 | encoded | `s 383(6) the net figure` | 4 |  |
| s 383(7) | 4889 | encoded | `s 383(7) which financial year's figures are taken for the subsidiary undertaking` | 4 |  |
| s 383(7)(a) | 4890 | encoded | `s 383(7) which financial year's figures are taken for the subsidiary undertaking` | 4 |  |
| s 383(7)(b) | 4891-4892 | encoded | `s 383(7) which financial year's figures are taken for the subsidiary undertaking` | 4 |  |
| s 384 | 4893 | encoded | `s 384(1) the company is excluded from the small companies regime` | 10 | 45 |
| s 384(1) | 4894 | fork | `s 384(1) the company is excluded from the small companies regime` (fork F5) | 10 | 45 |
| s 384(1)(a) | 4895 | encoded | `s 384(1) the company is excluded from the small companies regime` | 10 | 45 |
| s 384(1)(b) | 4896 | encoded | `s 384(1) the company is excluded from the small companies regime` | 10 | 45 |
| s 384(1)(b)(i) | 4897 | encoded | `s 384(1) the company is excluded from the small companies regime` | 10 | 45 |
| s 384(1)(b)(ii) | 4898 | encoded | `s 384(1) the company is excluded from the small companies regime` | 10 | 45 |
| s 384(1)(b)(iii) | 4899 | encoded | `s 384(1) the company is excluded from the small companies regime` | 10 | 45 |
| s 384(1)(c) | 4900 | encoded | `s 384(1) the company is excluded from the small companies regime` | 10 | 45 |
| s 384(2) | 4901 | encoded | `s 384(2) the member is of a kind that makes the group ineligible` (+2 more in the block) | 31 |  |
| s 384(2)(a) | 4902 | encoded | `s 384(2) the member is of a kind that makes the group ineligible` (+2 more in the block) | 31 |  |
| s 384(2)(b) | 4903 | encoded | `s 384(2) the member is of a kind that makes the group ineligible` (+2 more in the block) | 31 |  |
| s 384(2)(c) | 4904 | encoded | `s 384(2) the member is of a kind that makes the group ineligible` (+2 more in the block) | 31 |  |
| s 384(2)(ca) | 4905 | encoded | `s 384(2) the member is of a kind that makes the group ineligible` (+2 more in the block) | 31 |  |
| s 384(2)(d) | 4906 | encoded | `s 384(2) the member is of a kind that makes the group ineligible` (+2 more in the block) | 31 |  |
| s 384(2)(e) | 4907 | encoded | `s 384(2) the member is of a kind that makes the group ineligible` (+2 more in the block) | 31 |  |
| s 384(2)(f) | 4908 | encoded | `s 384(2) the member is of a kind that makes the group ineligible` (+2 more in the block) | 31 |  |
| s 384(3) | 4909 | encoded | `s 384(3) the company is a small company for the purposes of subsection (2)` | 2 |  |
| s 384A | 4910 | encoded | `s 384A(1) the company qualifies as a micro-entity in its first financial year` | 3 |  |
| s 384A(1) | 4911 | encoded | `s 384A(1) the company qualifies as a micro-entity in its first financial year` | 3 |  |
| s 384A(2) | 4912 | encoded | `s 384A(2) the company qualifies as a micro-entity in a subsequent financial year` | 3 | 47 |
| s 384A(3) | 4913 | fork | `s 384A(3) the change in whether the qualifying conditions are met affects the company's qualification as a micro-entity` (fork F14) | 2 |  |
| s 384A(4) | 4914 | encoded | `s 384A(4) the qualifying conditions are met in the year` | 6 | 46 |
| s 384A(4) row 1 | 4915 | encoded | `s 384A(4) the turnover limit, in pounds` | 1 |  |
| s 384A(4) row 2 | 4916 | encoded | `s 384A(4) the balance sheet total limit, in pounds` | 1 |  |
| s 384A(4) row 3 | 4917 | encoded | `s 384A(4) the employees limit` | 1 |  |
| s 384A(5) | 4918 | encoded | `s 384A(5) the maximum figure for turnover adjusted to the length of the period` | 1 |  |
| s 384A(6) | 4919 | encoded | `s 384A(6) the balance sheet total` | 1 |  |
| s 384A(7) | 4920 | encoded | `s 384A(7) the number of employees` | 2 |  |
| s 384A(7)(a) | 4921 | encoded | `s 384A(7) the number of employees` | 2 |  |
| s 384A(7)(b) | 4922 | encoded | `s 384A(7) the number of employees` | 2 |  |
| s 384A(7)(c) | 4923 | encoded | `s 384A(7) the number of employees` | 2 |  |
| s 384A(8) | 4924 | encoded | `s 384A(8) the parent company qualifies as a micro-entity` | 4 |  |
| s 384A(8)(a) | 4925 | encoded | `s 384A(8) the parent company qualifies as a micro-entity` | 4 |  |
| s 384A(8)(b) | 4926 | encoded | `s 384A(8) the parent company qualifies as a micro-entity` | 4 |  |
| s 384B | 4927 | encoded | `s 384B(1) the micro-entity provisions do not apply to the company's accounts` | 9 | 48 |
| s 384B(1) | 4928 | encoded | `s 384B(1) the micro-entity provisions do not apply to the company's accounts` | 9 | 48 |
| s 384B(1)(a) | 4929 | encoded | `s 384B(1) the micro-entity provisions do not apply to the company's accounts` | 9 | 48 |
| s 384B(1)(b) | 4930 | encoded | `s 384B(1) the micro-entity provisions do not apply to the company's accounts` | 9 | 48 |
| s 384B(1)(c) | 4931 | encoded | `s 384B(1) the micro-entity provisions do not apply to the company's accounts` | 9 | 48 |
| s 384B(1)(d) | 4932 | encoded | `s 384B(1) the micro-entity provisions do not apply to the company's accounts` | 9 | 48 |
| s 384B(1)(e) | 4933 | encoded | `s 384B(1) the micro-entity provisions do not apply to the company's accounts` | 9 | 48 |
| s 384B(1)(f) | 4934 | encoded | `s 384B(1) the micro-entity provisions do not apply to the company's accounts` | 9 | 48 |
| s 384B(2) | 4935 | encoded | `s 384B(2) the micro-entity provisions also do not apply to the company's accounts` | 6 | 49 |
| s 384B(2)(a) | 4936 | encoded | `s 384B(2) the micro-entity provisions also do not apply to the company's accounts` | 6 | 49 |
| s 384B(2)(b) | 4937 | encoded | `s 384B(2) the micro-entity provisions also do not apply to the company's accounts` | 6 | 49 |
| heading: Quoted and unquoted companies | 4938 | inert | reason 1: heading |  |  |
| s 385 | 4939 | encoded | `s 385(1) the company is a quoted company in relation to the financial year` | 3 | 51 |
| s 385(1) | 4940 | encoded | `s 385(1) the company is a quoted company in relation to the financial year` | 3 | 51 |
| s 385(2) | 4941 | encoded | `s 385(2) the company is a quoted company` | 4 | 50 |
| s 385(2)(a) | 4942 | encoded | `s 385(2) the company is a quoted company` | 4 | 50 |
| s 385(2)(b) | 4943 | encoded | `s 385(2) the company is a quoted company` | 4 | 50 |
| s 385(2)(c) | 4944-4945 | encoded | `s 385(2) the company is a quoted company` | 4 | 50 |
| s 385(3) | 4946 | encoded | `s 385(3) the company is an unquoted company` | 3 | 52 |
| s 385(4) | 4947 | inert | reason 2: regulation-making power |  |  |
| s 385(5) | 4948 | inert | reason 2: regulation-making power (procedure) |  |  |
| s 385(6) | 4949 | inert | reason 2: regulation-making power (procedure) |  |  |
| heading: Chapter 2 — Accounting records | 4950 | inert | reason 1: heading |  |  |
| s 386 | 4951 | encoded | `s 386(1) the company is required to keep adequate accounting records` (+2 more in the block) | 3 | 53 |
| s 386(1) | 4952 | encoded | `s 386(1) the company is required to keep adequate accounting records` (+2 more in the block) | 3 | 53 |
| s 386(2) | 4953 | encoded | `s 386(2) the records are adequate accounting records` | 4 | 54 |
| s 386(2)(a) | 4954 | encoded | `s 386(2) the records are adequate accounting records` | 4 | 54 |
| s 386(2)(b) | 4955 | encoded | `s 386(2) the records are adequate accounting records` | 4 | 54 |
| s 386(2)(c) | 4956 | encoded | `s 386(2) the records are adequate accounting records` | 4 | 54 |
| s 386(3) | 4957 | encoded | `s 386(3) the records contain what subsection (3) requires` | 3 | 55 |
| s 386(3)(a) | 4958 | encoded | `s 386(3) the records contain what subsection (3) requires` | 3 | 55 |
| s 386(3)(b) | 4959 | encoded | `s 386(3) the records contain what subsection (3) requires` | 3 | 55 |
| s 386(4) | 4960 | fork | `s 386(4) the records are required to contain the stock and goods statements` (fork F3) | 2 | 56 |
| s 386(4)(a) | 4961 | encoded | `s 386(4) the records contain the statements subsection (4) requires` | 6 | 57 |
| s 386(4)(b) | 4962 | encoded | `s 386(4) the records contain the statements subsection (4) requires` | 6 | 57 |
| s 386(4)(c) | 4963 | encoded | `s 386(4) the records contain the statements subsection (4) requires` | 6 | 57 |
| s 386(5) | 4964 | encoded | `s 386(5) the parent company is required to take reasonable steps to secure that the subsidiary undertaking keeps accounting records` | 4 | 58 |
| s 387 | 4965 | encoded | `s 387(1) the officer commits an offence` | 5 | 59 |
| s 387(1) | 4966 | encoded | `s 387(1) the officer commits an offence` | 5 | 59 |
| s 387(2) | 4967 | encoded | `s 387(2) this subsection gives the person a defence on these facts` | 3 | 60 |
| s 387(3) | 4968 | encoded | `s 387(3) the penalty on conviction` | 5 | 61 |
| s 387(3)(a) | 4969 | encoded | `s 387(3) the penalty on conviction` | 5 | 61 |
| s 387(3)(b) | 4970 | encoded | `s 387(3) the penalty on conviction` | 5 | 61 |
| s 387(3)(b)(i) | 4971 | encoded | `s 387(3) the penalty on conviction` | 5 | 61 |
| s 387(3)(b)(ii) | 4972 | encoded | `s 387(3) the penalty on conviction` | 5 | 61 |
| s 388 | 4973 | encoded | `s 388(1) the accounting records are kept as subsection (1) requires` | 4 | 62 |
| s 388(1) | 4974 | encoded | `s 388(1) the accounting records are kept as subsection (1) requires` | 4 | 62 |
| s 388(1)(a) | 4975 | encoded | `s 388(1) the accounting records are kept as subsection (1) requires` | 4 | 62 |
| s 388(1)(b) | 4976 | encoded | `s 388(1) the accounting records are kept as subsection (1) requires` | 4 | 62 |
| s 388(2) | 4977 | fork | `s 388(2) the accounts and returns for records kept outside the United Kingdom are kept as subsection (2) requires` (fork F3) | 4 | 63 |
| s 388(3) | 4978 | fork | `s 388(3) the accounts and returns sent to the United Kingdom are such as subsection (3) requires` (fork F3) | 5 | 64 |
| s 388(3)(a) | 4979 | encoded | `s 388(3) the accounts and returns sent to the United Kingdom are such as subsection (3) requires` | 5 | 64 |
| s 388(3)(b) | 4980 | encoded | `s 388(3) the accounts and returns sent to the United Kingdom are such as subsection (3) requires` | 5 | 64 |
| s 388(4) | 4981 | fork | `s 388(4) the period for which the accounting records must be preserved` (fork F8) | 10 | 65,66 |
| s 388(4)(a) | 4982 | encoded | `s 388(4) the period for which the accounting records must be preserved` (+1 more in the block) | 10 | 65,66 |
| s 388(4)(b) | 4983 | encoded | `s 388(4) the period for which the accounting records must be preserved` (+1 more in the block) | 10 | 65,66 |
| s 388(5) | 4984 | encoded | `s 388(5) a provision of insolvency rules displaces subsection (4)` | 3 |  |
| s 389 | 4985 | encoded | `s 389(1) the officer commits an offence` | 4 | 67 |
| s 389(1) | 4986 | encoded | `s 389(1) the officer commits an offence` | 4 | 67 |
| s 389(2) | 4987 | encoded | `s 389(2) this subsection gives the person a defence on these facts` | 3 | 68 |
| s 389(3) | 4988 | encoded | `s 389(3) the officer commits an offence` | 4 | 69 |
| s 389(3)(a) | 4989 | encoded | `s 389(3) the officer commits an offence` | 4 | 69 |
| s 389(3)(b) | 4990 | encoded | `s 389(3) the officer commits an offence` | 4 | 69 |
| s 389(4) | 4991 | encoded | `s 389(4) the penalty on conviction` | 4 | 70 |
| s 389(4)(a) | 4992 | encoded | `s 389(4) the penalty on conviction` | 4 | 70 |
| s 389(4)(b) | 4993 | encoded | `s 389(4) the penalty on conviction` | 4 | 70 |
| s 389(4)(b)(i) | 4994 | encoded | `s 389(4) the penalty on conviction` | 4 | 70 |
| s 389(4)(b)(ii) | 4995 | encoded | `s 389(4) the penalty on conviction` | 4 | 70 |
| heading: Chapter 3 — A company's financial year | 4996 | inert | reason 1: heading |  |  |
| s 390 | 4997 | encoded | `s 390(2)(a) the first day of the first financial year` | 1 | 71 |
| s 390(1) | 4998 | encoded | `s 390(2)(a) the first day of the first financial year` | 1 | 71 |
| s 390(2) | 4999 | encoded | `s 390(2)(a) the first day of the first financial year` | 1 | 71 |
| s 390(2)(a) | 5000 | encoded | `s 390(2)(a) the first day of the first financial year` | 1 | 71 |
| s 390(2)(b) | 5001 | encoded | `s 390(2)(b) the last day of the first financial year` | 5 | 72 |
| s 390(3) | 5002 | encoded | `s 390(3)(a) the first day of a subsequent financial year` | 2 | 73 |
| s 390(3)(a) | 5003 | encoded | `s 390(3)(a) the first day of a subsequent financial year` | 2 | 73 |
| s 390(3)(b) | 5004 | encoded | `s 390(3)(b) the last day of a subsequent financial year` | 3 | 74 |
| s 390(4) | 5005 | encoded | `s 390(4) the period is the financial year of the undertaking that is not a company` | 2 | 75 |
| s 390(5) | 5006 | encoded | `s 390(5) the directors are required to secure that the financial year of each subsidiary undertaking coincides with the company's own` | 4 | 76 |
| s 391 | 5007 | encoded | `s 391(1) the accounting reference date in the calendar year` | 6 |  |
| s 391(1) | 5008 | encoded | `s 391(1) the accounting reference date in the calendar year` | 6 |  |
| s 391(2) | 5009 | encoded | `s 391(2) the accounting reference date of a company incorporated in Great Britain before 1st April 1996` | 8 |  |
| s 391(2)(a) | 5010 | encoded | `s 391(2) the accounting reference date of a company incorporated in Great Britain before 1st April 1996` | 8 |  |
| s 391(2)(b) | 5011 | encoded | `s 391(2) the accounting reference date of a company incorporated in Great Britain before 1st April 1996` | 8 |  |
| s 391(2)(b)(i) | 5012 | encoded | `s 391(2) the accounting reference date of a company incorporated in Great Britain before 1st April 1996` | 8 |  |
| s 391(2)(b)(ii) | 5013 | encoded | `s 391(2) the accounting reference date of a company incorporated in Great Britain before 1st April 1996` | 8 |  |
| s 391(3) | 5014 | encoded | `s 391(3) the accounting reference date of a company incorporated in Northern Ireland before 22nd August 1997` | 7 |  |
| s 391(3)(a) | 5015 | encoded | `s 391(3) the accounting reference date of a company incorporated in Northern Ireland before 22nd August 1997` | 7 |  |
| s 391(3)(b) | 5016 | encoded | `s 391(3) the accounting reference date of a company incorporated in Northern Ireland before 22nd August 1997` | 7 |  |
| s 391(3)(b)(i) | 5017 | encoded | `s 391(3) the accounting reference date of a company incorporated in Northern Ireland before 22nd August 1997` | 7 |  |
| s 391(3)(b)(ii) | 5018 | encoded | `s 391(3) the accounting reference date of a company incorporated in Northern Ireland before 22nd August 1997` | 7 |  |
| s 391(4) | 5019 | encoded | `s 391(4) the accounting reference date of a company incorporated on or after the dates in subsection (4)` | 6 |  |
| s 391(4)(a) | 5020 | encoded | `s 391(4) the accounting reference date of a company incorporated on or after the dates in subsection (4)` | 6 |  |
| s 391(4)(b) | 5021 | encoded | `s 391(4) the accounting reference date of a company incorporated on or after the dates in subsection (4)` | 6 |  |
| s 391(4)(c) | 5022-5023 | encoded | `s 391(4) the accounting reference date of a company incorporated on or after the dates in subsection (4)` | 6 |  |
| s 391(5) | 5024 | fork | `s 391(5) the last day of the first accounting reference period` (fork F7) | 7 | 77 |
| s 391(6) | 5025 | encoded | `s 391(6) the first day of the next accounting reference period` (+2 more in the block) | 6 |  |
| s 391(7) | 5026 | inert | reason 1: a signpost ("subject to section 392"), fork F1 |  |  |
| s 392 | 5027 | encoded | `s 392(1) the company may by notice to the registrar specify a new accounting reference date having effect from` | 3 |  |
| s 392(1) | 5028 | encoded | `s 392(1) the company may by notice to the registrar specify a new accounting reference date having effect from` | 3 |  |
| s 392(1)(a) | 5029 | encoded | `s 392(1) the company may by notice to the registrar specify a new accounting reference date having effect from` | 3 |  |
| s 392(1)(b) | 5030-5031 | encoded | `s 392(1) the company may by notice to the registrar specify a new accounting reference date having effect from` | 3 |  |
| s 392(2) | 5032 | encoded | `s 392(2) the last day of the shortened or extended period` | 7 |  |
| s 392(2)(a) | 5033 | encoded | `s 392(2) the last day of the shortened or extended period` | 7 |  |
| s 392(2)(b) | 5034 | encoded | `s 392(2) the last day of the shortened or extended period` | 7 |  |
| s 392(3) | 5035-5036 | encoded | `s 392(3) the notice is ineffective because it is given less than five years after an earlier extension` | 12 | 78 |
| s 392(3)(a) | 5037 | encoded | `s 392(3) the notice is ineffective because it is given less than five years after an earlier extension` | 12 | 78 |
| s 392(3)(b) | 5038 | encoded | `s 392(3) the notice is ineffective because it is given less than five years after an earlier extension` | 12 | 78 |
| s 392(3)(c) | 5039 | encoded | `s 392(3) the notice is ineffective because it is given less than five years after an earlier extension` | 12 | 78 |
| s 392(4) | 5040 | encoded | `s 392(4) a notice may be given in respect of the previous accounting reference period` | 2 | 79 |
| s 392(5) | 5041-5042 | encoded | `s 392(5) the notice is ineffective because the period as extended would exceed 18 months` | 4 | 80 |
| s 392(6) | 5043 | encoded | `s 392(6) the undertaking is a UK undertaking` | 2 | 81 |
| heading: Chapter 4 — Annual accounts | 5044 | inert | reason 1: heading |  |  |
| heading: General | 5045 | inert | reason 1: heading |  |  |
| s 393 | 5046 | encoded | `s 393(1)(b) the condition for approving the company's group accounts is met` (+2 more in the block) | 2 | 83 |
| s 393(1) | 5047 | encoded | `s 393(1)(b) the condition for approving the company's group accounts is met` (+2 more in the block) | 2 | 83 |
| s 393(1)(a) | 5048 | encoded | `s 393(1)(a) the condition for approving the company's individual accounts is met` | 2 | 82 |
| s 393(1)(b) | 5049 | encoded | `s 393(1)(b) the condition for approving the company's group accounts is met` (+2 more in the block) | 2 | 83 |
| s 393(2) | 5050 | encoded | `s 393(2) the auditor is required to have regard to the directors' duty under subsection (1)` | 2 | 84 |
| s 393(1A) | 5051 | encoded | `s 393(1A)(a) the directors must disregard an accounting standard provision requiring information additional to the micro-entity minimum accounting items` | 4 |  |
| s 393(1A)(a) | 5052 | encoded | `s 393(1A)(b) the directors must disregard an accounting standard provision requiring further information in relation to the item` | 3 |  |
| s 393(1A)(b) | 5053 | encoded | `s 393(1A)(b) the directors must disregard an accounting standard provision requiring further information in relation to the item` | 3 |  |
| s 393(1A)(c) | 5054 | encoded | `s 393(1A)(c) the directors must have regard to an accounting standard provision relating to the additional item` | 3 |  |
| heading: Individual accounts | 5055 | inert | reason 1: heading |  |  |
| s 394 | 5056-5058 | encoded | `s 394 the directors are required to prepare individual accounts for the financial year` (+2 more in the block) | 3 | 85 |
| s 394A | 5059 | encoded | `s 394A(1) the company is exempt from the requirement to prepare individual accounts for the financial year` | 6 | 86 |
| s 394A(1) | 5060 | encoded | `s 394A(1) the company is exempt from the requirement to prepare individual accounts for the financial year` | 6 | 86 |
| s 394A(1)(a) | 5061 | encoded | `s 394A(1) the company is exempt from the requirement to prepare individual accounts for the financial year` | 6 | 86 |
| s 394A(1)(b) | 5062 | encoded | `s 394A(1) the company is exempt from the requirement to prepare individual accounts for the financial year` | 6 | 86 |
| s 394A(1)(c) | 5063 | encoded | `s 394A(1) the company is exempt from the requirement to prepare individual accounts for the financial year` | 6 | 86 |
| s 394A(2) | 5064 | encoded | `s 394A(2) the conditions of the exemption are all complied with` | 13 | 87 |
| s 394A(2)(a) | 5065 | encoded | `s 394A(2) the conditions of the exemption are all complied with` | 13 | 87 |
| s 394A(2)(b) | 5066 | encoded | `s 394A(2) the conditions of the exemption are all complied with` | 13 | 87 |
| s 394A(2)(c) | 5067 | encoded | `s 394A(2) the conditions of the exemption are all complied with` | 13 | 87 |
| s 394A(2)(c)(i) | 5068 | encoded | `s 394A(2) the conditions of the exemption are all complied with` | 13 | 87 |
| s 394A(2)(c)(ii) | 5069 | encoded | `s 394A(2) the conditions of the exemption are all complied with` | 13 | 87 |
| s 394A(2)(d) | 5070 | encoded | `s 394A(2) the conditions of the exemption are all complied with` | 13 | 87 |
| s 394A(2)(e) | 5071 | encoded | `s 394A(2) the conditions of the exemption are all complied with` | 13 | 87 |
| s 394A(2)(e)(i) | 5072 | encoded | `s 394A(2) the conditions of the exemption are all complied with` | 13 | 87 |
| s 394A(2)(e)(ii) | 5073 | encoded | `s 394A(2) the conditions of the exemption are all complied with` | 13 | 87 |
| s 394A(2)(e)(iii) | 5074 | encoded | `s 394A(2) the conditions of the exemption are all complied with` | 13 | 87 |
| s 394A(2)(e)(iv) | 5075 | encoded | `s 394A(2) the conditions of the exemption are all complied with` | 13 | 87 |
| s 394A(2)(e)(v) | 5076 | encoded | `s 394A(2) the conditions of the exemption are all complied with` | 13 | 87 |
| s 394B | 5077-5078 | encoded | `s 394B the company is entitled to the exemption conferred by section 394A` | 9 | 88 |
| s 394B(a) | 5079 | encoded | `s 394B the company is entitled to the exemption conferred by section 394A` | 9 | 88 |
| s 394B(b) | 5080 | encoded | `s 394B the company is entitled to the exemption conferred by section 394A` | 9 | 88 |
| s 394B(None)(b)(i) | 5081 | encoded | `s 394B the company is entitled to the exemption conferred by section 394A` | 9 | 88 |
| s 394B(None)(b)(ii) | 5082 | encoded | `s 394B the company is entitled to the exemption conferred by section 394A` | 9 | 88 |
| s 394B(c) | 5083 | encoded | `s 394B the company is entitled to the exemption conferred by section 394A` | 9 | 88 |
| s 394C | 5084 | encoded | `s 394C(1) a guarantee is given by the parent undertaking` | 2 |  |
| s 394C(1) | 5085 | encoded | `s 394C(1) a guarantee is given by the parent undertaking` | 2 |  |
| s 394C(2) | 5086 | encoded | `s 394C(2) the statement meets the requirements of subsection (2)` | 7 | 89 |
| s 394C(2)(a) | 5087 | encoded | `s 394C(2) the statement meets the requirements of subsection (2)` | 7 | 89 |
| s 394C(2)(b) | 5088 | encoded | `s 394C(2) the statement meets the requirements of subsection (2)` | 7 | 89 |
| s 394C(2)(c) | 5089 | repealed or blank in this text | the text shows only dots |  |  |
| s 394C(2)(d) | 5090 | encoded | `s 394C(2) the statement meets the requirements of subsection (2)` | 7 | 89 |
| s 394C(2)(e) | 5091 | encoded | `s 394C(2) the statement meets the requirements of subsection (2)` | 7 | 89 |
| s 394C(2)(f) | 5092 | encoded | `s 394C(2) the statement meets the requirements of subsection (2)` | 7 | 89 |
| s 394C(3) | 5093 | encoded | `s 394C(3)(a) the parent undertaking guarantees the liability` | 6 | 90 |
| s 394C(3)(a) | 5094 | encoded | `s 394C(3)(a) the parent undertaking guarantees the liability` | 6 | 90 |
| s 394C(3)(b) | 5095 | encoded | `s 394C(3)(b) the person may enforce the guarantee against the parent undertaking` (+1 more in the block) | 4 | 91 |
| s 395 | 5096 | encoded | `s 395(1) the individual accounts may be prepared in accordance with the framework` | 7 |  |
| s 395(1) | 5097 | encoded | `s 395(1) the individual accounts may be prepared in accordance with the framework` | 7 |  |
| s 395(1)(a) | 5098 | encoded | `s 395(1) the individual accounts may be prepared in accordance with the framework` | 7 |  |
| s 395(1)(b) | 5099-5100 | encoded | `s 395(1) the individual accounts may be prepared in accordance with the framework` | 7 |  |
| s 395(2) | 5101 | encoded | `s 395(2) the individual accounts must be Companies Act individual accounts` | 2 | 92 |
| s 395(3) | 5102 | encoded | `s 395(3) the directors must prepare IAS individual accounts for the financial year` | 7 | 94 |
| s 395(4) | 5103 | encoded | `s 395(4) there is a relevant change of circumstance` (+1 more in the block) | 13 | 93 |
| s 395(4)(a) | 5104 | encoded | `s 395(4) there is a relevant change of circumstance` (+1 more in the block) | 13 | 93 |
| s 395(4)(aa) | 5105 | encoded | `s 395(4) there is a relevant change of circumstance` (+1 more in the block) | 13 | 93 |
| s 395(4)(b) | 5106 | encoded | `s 395(4) there is a relevant change of circumstance` (+1 more in the block) | 13 | 93 |
| s 395(4)(c) | 5107 | encoded | `s 395(4) there is a relevant change of circumstance` (+1 more in the block) | 13 | 93 |
| s 395(4A) | 5108 | encoded | `s 395(4A) the directors may change to Companies Act individual accounts for a reason other than a relevant change of circumstance` | 7 |  |
| s 395(4B) | 5109 | encoded | `s 395(4A) the directors may change to Companies Act individual accounts for a reason other than a relevant change of circumstance` | 7 |  |
| s 395(5) | 5110 | encoded | `s 395(5) subsections (3) and (4) apply again with the year of the new IAS accounts as the first IAS year` | 3 |  |
| s 396 | 5111 | encoded | `s 396(A1) the accounts state what subsection (A1) requires` | 7 | 95 |
| s 396(A1) | 5112 | encoded | `s 396(A1) the accounts state what subsection (A1) requires` | 7 | 95 |
| s 396(A1)(a) | 5113 | encoded | `s 396(A1) the accounts state what subsection (A1) requires` | 7 | 95 |
| s 396(A1)(b) | 5114 | encoded | `s 396(A1) the accounts state what subsection (A1) requires` | 7 | 95 |
| s 396(A1)(c) | 5115 | encoded | `s 396(A1) the accounts state what subsection (A1) requires` | 7 | 95 |
| s 396(A1)(d) | 5116 | encoded | `s 396(A1) the accounts state what subsection (A1) requires` | 7 | 95 |
| s 396(A1)(e) | 5117 | encoded | `s 396(A1) the accounts state what subsection (A1) requires` | 7 | 95 |
| s 396(1) | 5118 | encoded | `s 396(1) the accounts comprise what subsection (1) requires` | 3 | 96 |
| s 396(1)(a) | 5119 | encoded | `s 396(1) the accounts comprise what subsection (1) requires` | 3 | 96 |
| s 396(1)(b) | 5120 | encoded | `s 396(1) the accounts comprise what subsection (1) requires` | 3 | 96 |
| s 396(2) | 5121 | encoded | `s 396(2) the accounts give the true and fair view subsection (2) requires` | 3 | 97 |
| s 396(2)(a) | 5122 | encoded | `s 396(2) the accounts give the true and fair view subsection (2) requires` | 3 | 97 |
| s 396(2)(b) | 5123 | encoded | `s 396(2) the accounts give the true and fair view subsection (2) requires` | 3 | 97 |
| s 396(2A) | 5124 | encoded | `s 396(2A) the micro-entity minimum accounting items are presumed to give the true and fair view required by subsection (2)` | 3 | 98 |
| s 396(3) | 5125 | encoded | `s 396(3) the accounts comply with the regulations subsection (3) refers to` | 3 | 99 |
| s 396(3)(a) | 5126 | encoded | `s 396(3) the accounts comply with the regulations subsection (3) refers to` | 3 | 99 |
| s 396(3)(b) | 5127 | encoded | `s 396(3) the accounts comply with the regulations subsection (3) refers to` | 3 | 99 |
| s 396(4) | 5128 | encoded | `s 396(4) the necessary additional information must be given in the accounts or in a note` | 5 | 100 |
| s 396(5) | 5129-5130 | encoded | `s 396(5) the directors must depart from the provision to the extent necessary, and give particulars in a note` | 4 | 101 |
| s 396(6) | 5131 | encoded | `s 396(6) subsections (4) and (5) apply to the item` | 2 |  |
| s 397 | 5132 | encoded | `s 397(1) the IAS individual accounts state what subsection (1) requires` | 3 | 102 |
| s 397(1) | 5133 | encoded | `s 397(1) the IAS individual accounts state what subsection (1) requires` | 3 | 102 |
| s 397(1)(a) | 5134 | encoded | `s 397(1) the IAS individual accounts state what subsection (1) requires` | 3 | 102 |
| s 397(1)(b) | 5135 | encoded | `s 397(1) the IAS individual accounts state what subsection (1) requires` | 3 | 102 |
| s 397(1)(c) | 5136 | encoded | `s 397(1) the IAS individual accounts state what subsection (1) requires` | 3 | 102 |
| s 397(1)(d) | 5137 | encoded | `s 397(1) the IAS individual accounts state what subsection (1) requires` | 3 | 102 |
| s 397(1)(e) | 5138 | encoded | `s 397(1) the IAS individual accounts state what subsection (1) requires` | 3 | 102 |
| s 397(2) | 5139 | encoded | `s 397(2) the notes state that the accounts have been prepared in accordance with UK-adopted international accounting standards` | 2 | 103 |
| heading: ... | 5140 | repealed or blank in this text | a heading shown as "..." in this text |  |  |
| s 398 | 5141-5142 | repealed or blank in this text | the text shows only dots |  |  |
| heading: Group accounts ... | 5143 | inert | reason 1: heading |  |  |
| s 399 | 5144 | encoded | `s 399(2) the directors are required to prepare group accounts for the year` | 6 | 104 |
| s 399(1) | 5145 | repealed or blank in this text | the text shows only dots |  |  |
| s 399(2) | 5146 | encoded | `s 399(2) the directors are required to prepare group accounts for the year` | 6 | 104 |
| s 399(2A) | 5147 | encoded | `s 399(2A) the company is exempt from the requirement to prepare group accounts` | 8 |  |
| s 399(2A)(a) | 5148 | encoded | `s 399(2A) the company is exempt from the requirement to prepare group accounts` | 8 |  |
| s 399(2A)(a)(i) | 5149 | encoded | `s 399(2A) the company is exempt from the requirement to prepare group accounts` | 8 |  |
| s 399(2A)(a)(ii) | 5150 | encoded | `s 399(2A) the company is exempt from the requirement to prepare group accounts` | 8 |  |
| s 399(2A)(b) | 5151 | encoded | `s 399(2A) the company is exempt from the requirement to prepare group accounts` | 8 |  |
| s 399(2B) | 5152 | encoded | `s 399(2B) the undertaking falls within this subsection` | 8 | 105 |
| s 399(2B)(a) | 5153 | encoded | `s 399(2B) the undertaking falls within this subsection` | 8 | 105 |
| s 399(2B)(b) | 5154 | encoded | `s 399(2B) the undertaking falls within this subsection` | 8 | 105 |
| s 399(2B)(c) | 5155 | encoded | `s 399(2B) the undertaking falls within this subsection` | 8 | 105 |
| s 399(2B)(c)(i) | 5156 | encoded | `s 399(2B) the undertaking falls within this subsection` | 8 | 105 |
| s 399(2B)(c)(ii) | 5157 | encoded | `s 399(2B) the undertaking falls within this subsection` | 8 | 105 |
| s 399(2B)(c)(iii) | 5158 | encoded | `s 399(2B) the undertaking falls within this subsection` | 8 | 105 |
| s 399(3) | 5159-5162 | encoded | `s 399(3) the company is exempt under one of the further exemptions` | 4 | 106 |
| s 399(4) | 5163 | encoded | `s 399(4) the exempt company may prepare group accounts` | 3 | 107 |
| s 400 | 5164 | encoded | `s 400(1) the company is within one of the cases that carry the exemption` | 7 | 113 |
| s 400(1) | 5165 | fork | `s 400(1) the company is within one of the cases that carry the exemption` (fork F13) | 7 | 113 |
| s 400(1)(a) | 5166 | encoded | `s 400(1)(a) the company is a wholly-owned subsidiary of that parent undertaking` | 3 |  |
| s 400(1)(b) | 5167 | encoded | `s 400(1)(b) the parent undertaking holds 90% or more of the allotted shares and the remaining shareholders approve` | 4 | 111 |
| s 400(1)(c) | 5168-5169 | encoded | `s 400(1)(c) the parent undertaking holds more than 50% but less than 90% of the allotted shares and no sufficient notice has been served` | 5 | 112 |
| s 400(2) | 5170 | encoded | `s 400(2) the conditions of the exemption are all complied with` | 7 | 114 |
| s 400(2)(a) | 5171 | encoded | `s 400(2) the conditions of the exemption are all complied with` | 7 | 114 |
| s 400(2)(b) | 5172 | encoded | `s 400(2) the conditions of the exemption are all complied with` | 7 | 114 |
| s 400(2)(b)(i) | 5173 | encoded | `s 400(2) the conditions of the exemption are all complied with` | 7 | 114 |
| s 400(2)(b)(ii) | 5174 | encoded | `s 400(2) the conditions of the exemption are all complied with` | 7 | 114 |
| s 400(2)(c) | 5175 | encoded | `s 400(2) the conditions of the exemption are all complied with` | 7 | 114 |
| s 400(2)(d) | 5176 | encoded | `s 400(2) the conditions of the exemption are all complied with` | 7 | 114 |
| s 400(2)(d)(i) | 5177 | encoded | `s 400(2) the conditions of the exemption are all complied with` | 7 | 114 |
| s 400(2)(d)(ii) | 5178 | encoded | `s 400(2) the conditions of the exemption are all complied with` | 7 | 114 |
| s 400(2)(e) | 5179 | encoded | `s 400(2) the conditions of the exemption are all complied with` | 7 | 114 |
| s 400(2)(e)(i) | 5180 | encoded | `s 400(2) the conditions of the exemption are all complied with` | 7 | 114 |
| s 400(2)(e)(ii) | 5181-5182 | encoded | `s 400(2) the conditions of the exemption are all complied with` | 7 | 114 |
| s 400(2)(f) | 5183 | encoded | `s 400(2) the conditions of the exemption are all complied with` | 7 | 114 |
| s 400(3) | 5184 | encoded | `s 400(3) the shares attributed to the parent undertaking` | 1 | 108 |
| s 400(4) | 5185 | encoded | `s 400(4) the exemption applies to the company` | 3 | 115 |
| s 400(5) | 5186 | encoded | `s 400(5) the company is a wholly-owned subsidiary of the parent undertaking for the purposes of this section` | 3 | 109 |
| s 400(6) | 5187 | repealed or blank in this text | the text shows only dots |  |  |
| s 401 | 5188 | encoded | `s 401(1) the company is within one of the cases that carry the exemption` | 5 | 116 |
| s 401(1) | 5189 | encoded | `s 401(1) the company is within one of the cases that carry the exemption` | 5 | 116 |
| s 401(1)(a) | 5190 | encoded | `s 401(1) the company is within one of the cases that carry the exemption` | 5 | 116 |
| s 401(1)(b) | 5191 | encoded | `s 401(1) the company is within one of the cases that carry the exemption` | 5 | 116 |
| s 401(1)(c) | 5192-5193 | encoded | `s 401(1) the company is within one of the cases that carry the exemption` | 5 | 116 |
| s 401(2) | 5194 | encoded | `s 401(2) the conditions of the exemption are all complied with` | 8 | 117 |
| s 401(2)(a) | 5195 | encoded | `s 401(2) the conditions of the exemption are all complied with` | 8 | 117 |
| s 401(2)(b) | 5196 | encoded | `s 401(2) the conditions of the exemption are all complied with` | 8 | 117 |
| s 401(2)(b)(i) | 5197 | repealed or blank in this text | the text shows only dots |  |  |
| s 401(2)(b)(ii) | 5198 | encoded | `s 401(2) the conditions of the exemption are all complied with` | 8 | 117 |
| s 401(2)(b)(iii) | 5199 | encoded | `s 401(2) the conditions of the exemption are all complied with` | 8 | 117 |
| s 401(2)(b)(iv) | 5200 | encoded | `s 401(2) the conditions of the exemption are all complied with` | 8 | 117 |
| s 401(2)(c) | 5201 | encoded | `s 401(2) the conditions of the exemption are all complied with` | 8 | 117 |
| s 401(2)(d) | 5202 | encoded | `s 401(2) the conditions of the exemption are all complied with` | 8 | 117 |
| s 401(2)(e) | 5203 | encoded | `s 401(2) the conditions of the exemption are all complied with` | 8 | 117 |
| s 401(2)(e)(i) | 5204 | encoded | `s 401(2) the conditions of the exemption are all complied with` | 8 | 117 |
| s 401(2)(e)(ii) | 5205 | encoded | `s 401(2) the conditions of the exemption are all complied with` | 8 | 117 |
| s 401(2)(f) | 5206 | encoded | `s 401(2) the conditions of the exemption are all complied with` | 8 | 117 |
| s 401(2)(f)(i) | 5207 | encoded | `s 401(2) the conditions of the exemption are all complied with` | 8 | 117 |
| s 401(2)(f)(ii) | 5208-5209 | encoded | `s 401(2) the conditions of the exemption are all complied with` | 8 | 117 |
| s 401(2)(g) | 5210 | encoded | `s 401(2) the conditions of the exemption are all complied with` | 8 | 117 |
| s 401(3) | 5211 | encoded | `s 401(3) the shares attributed to the parent undertaking` | 1 |  |
| s 401(4) | 5212 | encoded | `s 401(4) the exemption applies to the company` | 2 | 118 |
| s 401(5) | 5213 | encoded | `s 401(5) the company is a wholly-owned subsidiary of the parent undertaking for the purposes of this section` | 2 |  |
| s 401(6) | 5214 | repealed or blank in this text | the text shows only dots |  |  |
| s 402 | 5215-5216 | encoded | `s 402 the parent company is exempt from the requirement to prepare group accounts` (+1 more in the block) | 4 | 119 |
| heading: Group accounts: general | 5217 | inert | reason 1: heading |  |  |
| s 403 | 5218 | encoded | `s 403(1) the group accounts must be IAS group accounts` | 2 | 120 |
| s 403(1) | 5219 | encoded | `s 403(1) the group accounts must be IAS group accounts` | 2 | 120 |
| s 403(2) | 5220 | encoded | `s 403(2) the group accounts may be prepared in accordance with the framework` | 6 |  |
| s 403(2)(a) | 5221 | encoded | `s 403(2) the group accounts may be prepared in accordance with the framework` | 6 |  |
| s 403(2)(b) | 5222-5223 | encoded | `s 403(2) the group accounts may be prepared in accordance with the framework` | 6 |  |
| s 403(3) | 5224 | encoded | `s 403(3) the group accounts must be Companies Act group accounts` | 2 | 121 |
| s 403(4) | 5225 | encoded | `s 403(4) the directors must prepare IAS group accounts for the financial year` | 4 | 123 |
| s 403(5) | 5226 | encoded | `s 403(5) there is a relevant change of circumstance` | 4 | 122 |
| s 403(5)(a) | 5227 | encoded | `s 403(5) there is a relevant change of circumstance` | 4 | 122 |
| s 403(5)(b) | 5228 | encoded | `s 403(5) there is a relevant change of circumstance` | 4 | 122 |
| s 403(5)(c) | 5229 | encoded | `s 403(5) there is a relevant change of circumstance` | 4 | 122 |
| s 403(5A) | 5230 | encoded | `s 403(5A) the directors may change to Companies Act group accounts for a reason other than a relevant change of circumstance` | 3 |  |
| s 403(5B) | 5231 | encoded | `s 403(5A) the directors may change to Companies Act group accounts for a reason other than a relevant change of circumstance` | 3 |  |
| s 403(6) | 5232 | encoded | `s 403(6) subsections (4) and (5) apply again with the year of the new IAS accounts as the first IAS year` | 2 |  |
| s 404 | 5233 | encoded | `s 404(A1) the accounts state what subsection (A1) requires` | 2 | 124 |
| s 404(A1) | 5234 | encoded | `s 404(A1) the accounts state what subsection (A1) requires` | 2 | 124 |
| s 404(A1)(a) | 5235 | encoded | `s 404(A1) the accounts state what subsection (A1) requires` | 2 | 124 |
| s 404(A1)(b) | 5236 | encoded | `s 404(A1) the accounts state what subsection (A1) requires` | 2 | 124 |
| s 404(A1)(c) | 5237 | encoded | `s 404(A1) the accounts state what subsection (A1) requires` | 2 | 124 |
| s 404(A1)(d) | 5238 | encoded | `s 404(A1) the accounts state what subsection (A1) requires` | 2 | 124 |
| s 404(A1)(e) | 5239 | encoded | `s 404(A1) the accounts state what subsection (A1) requires` | 2 | 124 |
| s 404(1) | 5240 | encoded | `s 404(1) the accounts comprise what subsection (1) requires` | 3 | 125 |
| s 404(1)(a) | 5241 | encoded | `s 404(1) the accounts comprise what subsection (1) requires` | 3 | 125 |
| s 404(1)(b) | 5242 | encoded | `s 404(1) the accounts comprise what subsection (1) requires` | 3 | 125 |
| s 404(2) | 5243 | encoded | `s 404(2) the accounts give the true and fair view subsection (2) requires` | 2 | 126 |
| s 404(3) | 5244 | encoded | `s 404(3) the accounts comply with the regulations subsection (3) refers to` | 3 | 127 |
| s 404(3)(a) | 5245 | encoded | `s 404(3) the accounts comply with the regulations subsection (3) refers to` | 3 | 127 |
| s 404(3)(b) | 5246 | encoded | `s 404(3) the accounts comply with the regulations subsection (3) refers to` | 3 | 127 |
| s 404(4) | 5247 | encoded | `s 404(4) the necessary additional information must be given in the accounts or in a note` | 2 | 128 |
| s 404(5) | 5248-5249 | encoded | `s 404(5) the directors must depart from the provision to the extent necessary, and give particulars in a note` | 2 | 129 |
| s 405 | 5250 | encoded | `s 405(1) the subsidiary undertaking must be included in the consolidation` | 6 | 130 |
| s 405(1) | 5251 | encoded | `s 405(1) the subsidiary undertaking must be included in the consolidation` | 6 | 130 |
| s 405(2) | 5252 | fork | `s 405(2) the subsidiary undertaking may be excluded from consolidation because its inclusion is not material` (fork F15) | 4 | 131 |
| s 405(3) | 5253 | encoded | `s 405(3) the subsidiary undertaking may be excluded from consolidation in one of the three cases` | 4 | 132 |
| s 405(3)(a) | 5254 | encoded | `s 405(3) the subsidiary undertaking may be excluded from consolidation in one of the three cases` | 4 | 132 |
| s 405(3)(b) | 5255 | encoded | `s 405(3) the subsidiary undertaking may be excluded from consolidation in one of the three cases` | 4 | 132 |
| s 405(3)(c) | 5256 | encoded | `s 405(3) the subsidiary undertaking may be excluded from consolidation in one of the three cases` | 4 | 132 |
| s 405(4) | 5257 | encoded | `s 405(4) the rights or interests count for subsection (3)(a) and (c)` | 3 |  |
| s 406 | 5258 | encoded | `s 406(1) the IAS group accounts state what subsection (1) requires` | 2 | 133 |
| s 406(1) | 5259 | encoded | `s 406(1) the IAS group accounts state what subsection (1) requires` | 2 | 133 |
| s 406(1)(a) | 5260 | encoded | `s 406(1) the IAS group accounts state what subsection (1) requires` | 2 | 133 |
| s 406(1)(b) | 5261 | encoded | `s 406(1) the IAS group accounts state what subsection (1) requires` | 2 | 133 |
| s 406(1)(c) | 5262 | encoded | `s 406(1) the IAS group accounts state what subsection (1) requires` | 2 | 133 |
| s 406(1)(d) | 5263 | encoded | `s 406(1) the IAS group accounts state what subsection (1) requires` | 2 | 133 |
| s 406(1)(e) | 5264 | encoded | `s 406(1) the IAS group accounts state what subsection (1) requires` | 2 | 133 |
| s 406(2) | 5265 | encoded | `s 406(2) the notes state that the accounts have been prepared in accordance with UK-adopted international accounting standards` (+1 more in the block) | 11 | 134 |
| s 407 | 5266 | encoded | `s 407(1) the directors have secured that the individual accounts are prepared using the same financial reporting framework` | 9 |  |
| s 407(1) | 5267 | encoded | `s 407(1) the directors have secured that the individual accounts are prepared using the same financial reporting framework` | 9 |  |
| s 407(1)(a) | 5268 | encoded | `s 407(1) the directors have secured that the individual accounts are prepared using the same financial reporting framework` | 9 |  |
| s 407(1)(b) | 5269-5270 | encoded | `s 407(1) the directors have secured that the individual accounts are prepared using the same financial reporting framework` | 9 |  |
| s 407(2) | 5271 | fork | `s 407(2) subsection (1) applies` (fork F3) | 2 | 135 |
| s 407(3) | 5272 | encoded | `s 407(3) subsection (1) applies to the accounts of the subsidiary undertaking` | 2 | 136 |
| s 407(4) | 5273 | encoded | `s 407(4) subsection (1) requires the charity's accounts to use the same framework as the non-charity's` | 3 | 137 |
| s 407(5) | 5274 | encoded | `s 407(5) subsection (1)(a) applies` (+1 more in the block) | 5 |  |
| s 408 | 5275 | encoded | `s 408(1) section 408 applies` | 3 | 138 |
| s 408(1) | 5276 | encoded | `s 408(1) section 408 applies` | 3 | 138 |
| s 408(1)(a) | 5277 | encoded | `s 408(1) section 408 applies` | 3 | 138 |
| s 408(1)(b) | 5278 | encoded | `s 408(1) section 408 applies` | 3 | 138 |
| s 408(2) | 5279 | repealed or blank in this text | the text shows only dots |  |  |
| s 408(3) | 5280 | encoded | `s 408(3) the individual profit and loss account may be omitted from the company's annual accounts for the purposes of the other provisions of the Companies Acts` (+1 more in the block) | 5 | 139 |
| s 408(4) | 5281 | encoded | `s 408(4) the exemption conferred by section 408 is available` | 2 | 140 |
| heading: Information to be given in notes to the accounts | 5282 | inert | reason 1: heading |  |  |
| s 409 | 5283 | encoded | `s 409(4) the conditions for non-disclosure are met` | 6 | 141 |
| s 409(1) | 5284 | inert | reason 2: regulation-making power |  |  |
| s 409(2) | 5285 | inert | reason 2: regulation-making power |  |  |
| s 409(2)(a) | 5286 | inert | reason 2: regulation-making power |  |  |
| s 409(2)(b) | 5287 | inert | reason 2: regulation-making power |  |  |
| s 409(3) | 5288 | inert | reason 2: regulation-making power |  |  |
| s 409(3)(a) | 5289 | inert | reason 2: regulation-making power |  |  |
| s 409(3)(b) | 5290-5291 | inert | reason 2: regulation-making power |  |  |
| s 409(4) | 5292 | encoded | `s 409(4) the conditions for non-disclosure are met` | 6 | 141 |
| s 409(4)(a) | 5293 | encoded | `s 409(4) the conditions for non-disclosure are met` | 6 | 141 |
| s 409(4)(a)(i) | 5294 | encoded | `s 409(4) the conditions for non-disclosure are met` | 6 | 141 |
| s 409(4)(a)(ii) | 5295 | encoded | `s 409(4) the conditions for non-disclosure are met` | 6 | 141 |
| s 409(4)(a)(iii) | 5296 | encoded | `s 409(4) the conditions for non-disclosure are met` | 6 | 141 |
| s 409(4)(a)(iv) | 5297 | encoded | `s 409(4) the conditions for non-disclosure are met` | 6 | 141 |
| s 409(4)(b) | 5298 | encoded | `s 409(4) the conditions for non-disclosure are met` | 6 | 141 |
| s 409(5) | 5299 | encoded | `s 409(5) the fact that advantage is taken of the exemption must be stated in a note to the annual accounts` | 2 | 142 |
| s 410 | 5300-5301 | repealed or blank in this text | the text shows only dots |  |  |
| s 410A | 5302 | encoded | `s 410A(1) the information required by section 410A must be given in the notes to the annual accounts` | 3 | 143 |
| s 410A(1) | 5303 | encoded | `s 410A(1) the information required by section 410A must be given in the notes to the annual accounts` | 3 | 143 |
| s 410A(1)(a) | 5304 | encoded | `s 410A(1) the information required by section 410A must be given in the notes to the annual accounts` | 3 | 143 |
| s 410A(1)(b) | 5305-5306 | encoded | `s 410A(1) the information required by section 410A must be given in the notes to the annual accounts` | 3 | 143 |
| s 410A(2) | 5307 | encoded | `s 410A(2) the item of information must be given in the notes` (+1 more in the block) | 8 |  |
| s 410A(2)(a) | 5308 | encoded | `s 410A(2) the item of information must be given in the notes` (+1 more in the block) | 8 |  |
| s 410A(2)(b) | 5309 | encoded | `s 410A(2) the item of information must be given in the notes` (+1 more in the block) | 8 |  |
| s 410A(3) | 5310 | encoded | `s 410A(2) the item of information must be given in the notes` (+1 more in the block) | 8 |  |
| s 410A(4) | 5311 | encoded | `s 410A(4) the company need not comply with subsection (2)(b)` (+1 more in the block) | 3 |  |
| s 410A(5) | 5312 | encoded | `s 410A(5) the entity whose arrangements are tested in the accounts` | 2 |  |
| s 411 | 5313 | encoded | `s 411(1) the notes must disclose the average number of persons employed by the company in the financial year` | 2 | 144 |
| s 411(1) | 5314 | encoded | `s 411(1) the notes must disclose the average number of persons employed by the company in the financial year` | 2 | 144 |
| s 411(1A) | 5315 | encoded | `s 411(1A) the notes must also disclose the average number of persons within each category` | 3 | 145 |
| s 411(2) | 5316 | encoded | `s 411(2) the categories are ones the directors may select` | 2 |  |
| s 411(3) | 5317 | encoded | `s 411(3) the average number` | 4 | 146 |
| s 411(4) | 5318 | encoded | `s 411(4)(a) the relevant annual number for subsection (1)` | 2 |  |
| s 411(4)(a) | 5319 | encoded | `s 411(4)(a) the relevant annual number for subsection (1)` | 2 |  |
| s 411(4)(b) | 5320-5321 | encoded | `s 411(4)(b) the relevant annual number for subsection (1A)` | 1 |  |
| s 411(5) | 5322 | encoded | `s 411(5) the notes or the profit and loss account must disclose the total staff costs` | 3 | 147 |
| s 411(5)(a) | 5323 | encoded | `s 411(5) the total staff costs` | 1 | 148 |
| s 411(5)(b) | 5324 | encoded | `s 411(5) the total staff costs` | 1 | 148 |
| s 411(5)(c) | 5325 | encoded | `s 411(5) the total staff costs` | 1 | 148 |
| s 411(6) | 5326-5327 | encoded | `s 411(6) the cost is a pension cost` | 4 | 149 |
| s 411(6)(a) | 5328 | encoded | `s 411(6) the cost is a pension cost` | 4 | 149 |
| s 411(6)(b) | 5329 | encoded | `s 411(6) the cost is a pension cost` | 4 | 149 |
| s 411(6)(c) | 5330-5331 | encoded | `s 411(6) the cost is a pension cost` | 4 | 149 |
| s 411(7) | 5332 | encoded | `s 411(7) the entity whose employees and staff costs are counted in the accounts` | 2 |  |
| s 412 | 5333 | encoded | `s 412(4) the amount is treated as paid to or receivable by the director` | 4 | 151 |
| s 412(1) | 5334 | inert | reason 2: regulation-making power |  |  |
| s 412(2) | 5335 | inert | reason 2: regulation-making power |  |  |
| s 412(2)(a) | 5336 | inert | reason 2: regulation-making power |  |  |
| s 412(2)(b) | 5337 | inert | reason 2: regulation-making power |  |  |
| s 412(2)(c) | 5338 | inert | reason 2: regulation-making power |  |  |
| s 412(2)(d) | 5339 | inert | reason 2: regulation-making power |  |  |
| s 412(2)(e) | 5340 | inert | reason 2: regulation-making power |  |  |
| s 412(3) | 5341 | inert | reason 2: regulation-making power |  |  |
| s 412(4) | 5342 | encoded | `s 412(4) the amount is treated as paid to or receivable by the director` | 4 | 151 |
| s 412(4)(a) | 5343 | encoded | `s 412(4) the amount is treated as paid to or receivable by the director` | 4 | 151 |
| s 412(4)(b) | 5344-5346 | encoded | `s 412(4) the amount is treated as paid to or receivable by the director` | 4 | 151 |
| s 412(5) | 5347 | fork | `s 412(5) the person is under the duty to give notice to the company of such matters relating to himself as regulations require` (fork F12) | 7 | 152 |
| s 412(5)(a) | 5348 | encoded | `s 412(5) the person is under the duty to give notice to the company of such matters relating to himself as regulations require` (+2 more in the block) | 7 | 152 |
| s 412(5)(b) | 5349-5350 | encoded | `s 412(5) the person is under the duty to give notice to the company of such matters relating to himself as regulations require` (+2 more in the block) | 7 | 152 |
| s 412(6) | 5351 | encoded | `s 412(6) the person commits an offence` (+1 more in the block) | 8 | 153,154 |
| s 413 | 5352 | encoded | `s 413(1) the details must be shown in the notes to the company's individual accounts` | 2 | 155 |
| s 413(1) | 5353 | encoded | `s 413(1) the details must be shown in the notes to the company's individual accounts` | 2 | 155 |
| s 413(1)(a) | 5354 | encoded | `s 413(1) the details must be shown in the notes to the company's individual accounts` | 2 | 155 |
| s 413(1)(b) | 5355-5356 | encoded | `s 413(1) the details must be shown in the notes to the company's individual accounts` | 2 | 155 |
| s 413(2) | 5357 | encoded | `s 413(2) the details must be shown in the notes to the group accounts` | 4 | 156 |
| s 413(2)(a) | 5358 | encoded | `s 413(2) the details must be shown in the notes to the group accounts` | 4 | 156 |
| s 413(2)(b) | 5359-5360 | encoded | `s 413(2) the details must be shown in the notes to the group accounts` | 4 | 156 |
| s 413(3) | 5361 | encoded | `s 413(3) the details of an advance or credit are given as subsection (3) requires` | 7 | 157 |
| s 413(3)(a) | 5362 | encoded | `s 413(3) the details of an advance or credit are given as subsection (3) requires` | 7 | 157 |
| s 413(3)(b) | 5363 | encoded | `s 413(3) the details of an advance or credit are given as subsection (3) requires` | 7 | 157 |
| s 413(3)(c) | 5364 | encoded | `s 413(3) the details of an advance or credit are given as subsection (3) requires` | 7 | 157 |
| s 413(3)(d) | 5365 | encoded | `s 413(3) the details of an advance or credit are given as subsection (3) requires` | 7 | 157 |
| s 413(3)(e) | 5366 | encoded | `s 413(3) the details of an advance or credit are given as subsection (3) requires` | 7 | 157 |
| s 413(3)(f) | 5367 | encoded | `s 413(3) the details of an advance or credit are given as subsection (3) requires` | 7 | 157 |
| s 413(4) | 5368 | encoded | `s 413(4) the details of a guarantee are given as subsection (4) requires` (+3 more in the block) | 8 | 158 |
| s 413(4)(a) | 5369 | encoded | `s 413(4) the details of a guarantee are given as subsection (4) requires` (+3 more in the block) | 8 | 158 |
| s 413(4)(b) | 5370 | encoded | `s 413(4) the details of a guarantee are given as subsection (4) requires` (+3 more in the block) | 8 | 158 |
| s 413(4)(c) | 5371 | encoded | `s 413(4) the details of a guarantee are given as subsection (4) requires` (+3 more in the block) | 8 | 158 |
| s 413(5) | 5372 | encoded | `s 413(5) the totals to be stated` (+1 more in the block) | 2 |  |
| s 413(5)(a) | 5373 | encoded | `s 413(5) the totals to be stated` (+1 more in the block) | 2 |  |
| s 413(5)(b) | 5374 | encoded | `s 413(5) the totals to be stated` (+1 more in the block) | 2 |  |
| s 413(5)(ba) | 5375 | encoded | `s 413(5) the totals to be stated` (+1 more in the block) | 2 |  |
| s 413(5)(bb) | 5376 | encoded | `s 413(5) the totals to be stated` (+1 more in the block) | 2 |  |
| s 413(5)(c) | 5377 | encoded | `s 413(5) the totals to be stated` (+1 more in the block) | 2 |  |
| s 413(5)(d) | 5378 | encoded | `s 413(5) the totals to be stated` (+1 more in the block) | 2 |  |
| s 413(6) | 5379 | encoded | `s 413(6) the person is one of the directors for the purposes of this section` | 2 | 159 |
| s 413(7) | 5380 | encoded | `s 413(7) the requirements of the section apply to the advance, credit or guarantee` | 2 | 160 |
| s 413(7)(a) | 5381 | encoded | `s 413(7) the requirements of the section apply to the advance, credit or guarantee` | 2 | 160 |
| s 413(7)(b) | 5382 | encoded | `s 413(7) the requirements of the section apply to the advance, credit or guarantee` | 2 | 160 |
| s 413(7)(c) | 5383 | encoded | `s 413(7) the requirements of the section apply to the advance, credit or guarantee` | 2 | 160 |
| s 413(8) | 5384 | encoded | `s 413(8) the total must be stated` | 8 |  |
| heading: Approval and signing of accounts | 5385 | inert | reason 1: heading |  |  |
| s 414 | 5386 | encoded | `s 414(1) the annual accounts are approved and signed as subsection (1) requires` (+1 more in the block) | 3 | 161 |
| s 414(1) | 5387 | encoded | `s 414(1) the annual accounts are approved and signed as subsection (1) requires` (+1 more in the block) | 3 | 161 |
| s 414(2) | 5388 | encoded | `s 414(2) the signature is placed as subsection (2) requires` (+1 more in the block) | 2 | 162 |
| s 414(3) | 5389 | encoded | `s 414(3) the statement the balance sheet must contain in a prominent position above the signature` (+1 more in the block) | 7 | 163 |
| s 414(3)(a) | 5390 | encoded | `s 414(3) the statement the balance sheet must contain in a prominent position above the signature` (+1 more in the block) | 7 | 163 |
| s 414(3)(b) | 5391 | encoded | `s 414(3) the statement the balance sheet must contain in a prominent position above the signature` (+1 more in the block) | 7 | 163 |
| s 414(4) | 5392 | encoded | `s 414(4) the director commits an offence` | 7 | 164 |
| s 414(4)(a) | 5393 | encoded | `s 414(4) the director commits an offence` | 7 | 164 |
| s 414(4)(b) | 5394-5395 | encoded | `s 414(4) the director commits an offence` | 7 | 164 |
| s 414(5) | 5396 | encoded | `s 414(5) the penalty on conviction` | 5 | 165 |
| s 414(5)(a) | 5397 | encoded | `s 414(5) the penalty on conviction` | 5 | 165 |
| s 414(5)(b) | 5398 | encoded | `s 414(5) the penalty on conviction` | 5 | 165 |
| heading: CHAPTER 4A — STRATEGIC REPORT | 5399 | inert | reason 1: heading |  |  |
| s 414A | 5400 | encoded | `s 414A(1) the directors are required to prepare a strategic report for the financial year` (+2 more in the block) | 3 | 166 |
| s 414A(1) | 5401 | encoded | `s 414A(1) the directors are required to prepare a strategic report for the financial year` (+2 more in the block) | 3 | 166 |
| s 414A(2) | 5402 | encoded | `s 414A(2) subsection (1) applies to the company` | 3 |  |
| s 414A(3) | 5403 | encoded | `s 414A(3) the strategic report must be a group strategic report relating to the undertakings included in the consolidation` | 5 | 167 |
| s 414A(3)(a) | 5404 | encoded | `s 414A(3) the strategic report must be a group strategic report relating to the undertakings included in the consolidation` | 5 | 167 |
| s 414A(3)(b) | 5405-5406 | encoded | `s 414A(3) the strategic report must be a group strategic report relating to the undertakings included in the consolidation` | 5 | 167 |
| s 414A(4) | 5407 | encoded | `s 414A(4) the group strategic report may, where appropriate, give greater emphasis to the matters that are significant to the undertakings included in the consolidation taken as a whole` | 2 | 168 |
| s 414A(5) | 5408 | encoded | `s 414A(5) the person commits an offence` | 4 | 169 |
| s 414A(5)(a) | 5409 | encoded | `s 414A(5) the person commits an offence` | 4 | 169 |
| s 414A(5)(b) | 5410 | encoded | `s 414A(5) the person commits an offence` | 4 | 169 |
| s 414A(6) | 5411 | encoded | `s 414A(6) the penalty on conviction` | 2 | 170 |
| s 414A(6)(a) | 5412 | encoded | `s 414A(6) the penalty on conviction` | 2 | 170 |
| s 414A(6)(b) | 5413 | encoded | `s 414A(6) the penalty on conviction` | 2 | 170 |
| s 414B | 5414-5415 | encoded | `s 414B the company is entitled to the small companies exemption in relation to the strategic report` | 5 | 171 |
| s 414B(a) | 5416 | encoded | `s 414B the company is entitled to the small companies exemption in relation to the strategic report` | 5 | 171 |
| s 414B(b) | 5417 | encoded | `s 414B the company is entitled to the small companies exemption in relation to the strategic report` | 5 | 171 |
| s 363(2) "political organisation" | 4665 | encoded | `s 363(2)(a) the activities are intended to affect public support for a party or candidate to which this Part applies` | 5 | 3 |
| s 364(2)(a) "political donation" | 4673 | encoded | `s 364(2)(a) the thing is a political donation to the political party or other political organisation` (+1 more in the block) | 7 | 4 |
| s 364(3)(a) "political donation" | 4679 | encoded | `s 364(3)(a) the thing is a political donation to the independent election candidate` (+1 more in the block) | 5 | 4 |
| s 366(4) "relevant holding company" | 4705 | encoded | `s 366(4) the other company is a relevant holding company` | 7 | 7 |
| s 369(4) "relevant holding company" | 4749 | encoded | `s 369(4) the other company is a relevant holding company` | 3 |  |
| s 372(1) "the company" | 4791 | encoded | `s 372(1) section 372 applies to the proceedings` | 2 |  |
| s 372(1) "the group" | 4791 | encoded | `s 372(1) section 372 applies to the proceedings` | 2 |  |
| s 374(3) "trade union" | 4810 | encoded | `s 374(3) the body is a trade union` | 5 |  |
| s 374(3) "political fund" | 4811 | encoded | `s 374(3) the fund is a political fund` | 4 |  |
| s 375(2) "trade association" | 4815 | encoded | `s 375(2) the organisation is a trade association` | 2 |  |
| s 375(2) "subscription" | 4816 | encoded | `s 375(2) the part of the payment that is a subscription` | 3 | 28 |
| s 376(2) "all-party parliamentary group" | 4819 | encoded | `s 376(2) the group is an all-party parliamentary group` | 3 | 29 |
| s 378(2) "donation" | 4834 | encoded | `s 378(2) the payment is a donation for the purposes of this section` (+1 more in the block) | 2 |  |
| s 378(2) "other relevant donations" | 4835 | encoded | `s 378(2) the other donation is an other relevant donation` | 12 | 33 |
| s 379(1) "director" | 4842 | encoded | `s 379(1) the person is a director for the purposes of this Part` | 5 | 34 |
| s 379(1) "organisation" | 4843 | encoded | `s 379(1) the body is an organisation for the purposes of this Part` | 8 |  |
| s 383(6) "net" | 4884 | encoded | `s 383(6) the net figure` | 4 |  |
| s 383(6)(b) "gross" | 4887 | encoded | `s 383(6) the gross figure` (+1 more in the block) | 1 |  |
| s 385(2) "quoted company" | 4941 | encoded | `s 385(2) the company is a quoted company` | 4 | 50 |
| s 385(2)(c) "the official list" | 4945 | encoded | `s 385(2) the company is a quoted company` | 4 | 50 |
| s 385(3) "unquoted company" | 4946 | encoded | `s 385(3) the company is an unquoted company` | 3 | 52 |
| s 392(1)(b) "previous accounting reference period" | 5031 | encoded | `s 392(1) the period is the company's previous accounting reference period` (+1 more in the block) | 2 |  |
| s 392(6) "UK undertaking" | 5043 | encoded | `s 392(6) the undertaking is a UK undertaking` | 2 | 81 |
| s 395(1)(a) "Companies Act individual accounts" | 5098 | encoded | `s 395(1) the individual accounts may be prepared in accordance with the framework` | 7 |  |
| s 395(1)(b) "IAS individual accounts" | 5099 | encoded | `s 395(1) the individual accounts may be prepared in accordance with the framework` | 7 |  |
| s 395(3) "the first IAS year" | 5102 | encoded | `s 395(3) the directors must prepare IAS individual accounts for the financial year` | 7 | 94 |
| s 403(1) "IAS group accounts" | 5219 | encoded | `s 403(1) the group accounts must be IAS group accounts` | 2 | 120 |
| s 403(2)(a) "Companies Act group accounts" | 5221 | encoded | `s 403(2) the group accounts may be prepared in accordance with the framework` | 6 |  |
| s 403(2)(b) "IAS group accounts" | 5222 | encoded | `s 403(2) the group accounts may be prepared in accordance with the framework` | 6 |  |
| s 403(4) "the first IAS year" | 5225 | encoded | `s 403(4) the directors must prepare IAS group accounts for the financial year` | 4 | 123 |
| s 411(6) "pension costs" | 5327 | encoded | `s 411(6) the cost is a pension cost` | 4 | 149 |
| s 411(6)(c) "social security costs" | 5331 | encoded | `s 411(6) the cost is a social security cost` (+1 more in the block) | 2 | 150 |
| s 414A(3)(b) "group strategic report" | 5406 | encoded | `s 414A(3) the strategic report must be a group strategic report relating to the undertakings included in the consolidation` | 5 | 167 |

## Fork register (coa8)

Each entry gives the provision, the readings seen, the one taken, and the text that licenses each.
A row of the coverage table whose disposition is `fork` names its entry here; F1 and F2 are about whether a provision is encoded at all, so their rows say `inert` and name the fork in the reason.
Every entry is for the human reviewer to overrule.
The maintainer's ruling of 2026-11-05 ("decide case by case at encoding time ... one fork line per site") is the licence for the sites it covers; it is reproduced in "Rulings applied" above.

| # | provision | function | readings seen | taken | text |
| --- | --- | --- | --- | --- | --- |
| F1 | ss 362, 364(1), 380(2), 382(7), 391(7) | none | (A) inert, reason 1: each sentence states a scope or points at another section and creates no rule of its own. (B) encode it as a limiting function (for example, "the answer of s 382 yields to s 383"). | A | s 382(7): "This section is subject to section 383 (companies qualifying as small: parent companies)." The limit is carried by s 383(1), which needs both the parent company and the group to qualify. s 391(7): "This section has effect subject to the provisions of section 392"; s 392 is encoded on its own. |
| F2 | s 377(2), (4) | none | (A) inert, reason 2: they are order-making machinery (what an order may cover; the affirmative resolution procedure). (B) encode "an order may cover companies or expenditure of a description" as a type. | A. An order's effect enters only as the input `the expenditure is exempt by virtue of an order of the Secretary of State under this section` in `s 377(1)`. | s 377(2): "An order may confer an exemption in relation to— (a) companies of any description or category specified in the order, or (b) expenditure of any description". s 377(4): "An order under this section is subject to affirmative resolution procedure." |
| F3 | s 386(4); s 388(2), (3); s 407(1) with (2) | `s 386(4) the records contain the statements subsection (4) requires`; `s 388(2) ...`; `s 388(3) ...`; `s 407(1) the directors have secured ...` | A duty whose "if" is unmet, asked whether it is complied with: (A) JUST TRUE, nothing is required; (B) NOTHING, not covered; (C) JUST FALSE, not "as required". | A for the compliance check. The question "is it required" is separate and answers JUST FALSE where the "if" fails (`s 386(4) the records are required to contain the stock and goods statements`), under the ruling on "where" conditions. | s 386(4): "If the company's business involves dealing in goods, the records must contain ...". s 407(2): "Subsection (1) does not apply if the directors do not prepare group accounts for the parent company." |
| F4 | s 378(2) | `s 378(2) the other donation is an other relevant donation` | A subsidiary of the company, where the company is itself a subsidiary: (A) counts under (b), because a subsidiary of the company is a subsidiary of its holding company; (B) counts only if it is among the donors (b) lists literally. | A | s 378(2)(a): "any other donations made by that company or by any of its subsidiaries"; (b): "by that company, by any holding company of that company or by any other subsidiary of any such holding company". |
| F5 | s 384(1) read with s 381(b) | `s 384(1) the company is excluded from the small companies regime` | A company in none of the listed kinds: (A) JUST FALSE, because s 381(b) uses the s 384 list as the whole of "excluded"; (B) NOTHING, because s 384 says only what the regime "does not apply to". | A | s 381: "...a company ... (b) is not excluded from the regime (see section 384)"; s 384: "The small companies regime does not apply to a company that ... was at any time within the financial year ..." |
| F6 | s 366(2) with (3) | `s 366(2) the donation or expenditure is authorised as section 366(2) requires` | Relief under (3) when whether the company is a wholly-owned subsidiary of a UK-registered company is not known: (A) no relief shown, so the company's own resolution is required; (B) NOTHING for the whole of (2). | A | s 366(3): "No resolution is required on the part of a company that is a wholly-owned subsidiary of a UK-registered company." The relief is stated for a case; outside it, (2)(b)(i) applies. |
| F7 | s 391(5) | `s 391(5) the last day of the first accounting reference period` | "A period of more than six months ... beginning with the date of its incorporation": (A) the day of incorporation is day one, so a period of exactly six months does not qualify and the first period runs to the next accounting reference date; (B) the six months are counted from the day after. | A | s 391(5): "A company's first accounting reference period is the period of more than six months, but not more than 18 months, beginning with the date of its incorporation and ending with its accounting reference date." Finding 1 records an expected value of mine that was wrong on exactly this point. |
| F8 | s 388(4) | `s 388(4) the accounting records must still be preserved on the day` | "for three years from the date on which they are made": is the anniversary day inside the period? (A) yes; (B) no. | Neither: before the anniversary JUST TRUE, after it JUST FALSE, on it NOTHING (silent). | s 388(4)(a): "in the case of a private company, for three years from the date on which they are made"; (b): "for six years". |
| F9 | s 368(1) | `s 368(1) the last day on which the resolution has effect` | "a period of four years beginning with the date on which it is passed": (A) the last day is the day before the fourth anniversary (passed on 1 June 2026: last day 31 May 2030); (B) the anniversary. | A | s 368(1): "has effect for a period of four years beginning with the date on which it is passed". |
| F10 | s 370(3) | `s 370(3) the members are an authorised group` | (a) 5% by nominal value of a company with nil issued share capital: (A) not met (the figure must be above 0); (B) met. (b) "if the company is not limited by shares": (A) only such a company may use the 5%-of-members limb; (B) any company may. | A for both | s 370(3)(a): "the holders of not less than 5% in nominal value of the company's issued share capital"; (b): "if the company is not limited by shares, not less than 5% of its members"; (c): "not less than 50 of the company's members". |
| F11 | s 371(1)(b) and (2) | `s 371(1) the notice requirements are met`; `s 371(2) the director may apply to the court ...` | Two counts in one section. (1)(b): "not less than 28 days have elapsed between the date of the giving of the notice ... and the bringing of the proceedings": (A) the difference between the two dates is at least 28; (B) at least 29. (2): "within the period of 28 days beginning with the date of the giving of the notice": (A) the last day is the date of the notice plus 27; (B) plus 28. | A for both, each following its own wording | s 371(1)(b) and (2), quoted in the reading column. |
| F12 | s 412(5) | `s 412(5) the person is under the duty to give notice to the company ...` | "at any time in the preceding five years been a director": (A) five years back from the day the question is asked, the same date five years earlier being inside; (B) five years back from the end of the financial year. | A | s 412(5)(b): "any person who is or has at any time in the preceding five years been a director of the company". |
| F13 | s 400(1), s 401(1) | `s 400(1) the notice was served in time` | "served at least six months before the end of the financial year": (A) on or before the day six months before the last day (`add months` -6, which clamps to the end of a shorter month); (B) at least 183 days before. | A | s 400(1), last sentence: "Such notice must be served at least six months before the end of the financial year to which it relates." |
| F14 | s 382(2), s 383(3), s 384A(3) | `s 382(2) the change in whether the qualifying conditions are met affects the company's qualification` and its twins | "affects its qualification ... only if it occurs in two consecutive financial years": (A) a change of answer takes effect in the second of two consecutive years in which the new answer holds; in the first year the previous year's status stays; (B) it takes effect in the year after the two. | A | s 382(2): "In relation to a subsequent financial year, where on its balance sheet date a company meets or ceases to meet the qualifying conditions, that affects its qualification as a small company only if it occurs in two consecutive financial years." |
| F15 | s 405(2) (name-test sweep of 2026-11-12) | `s 405(2) the subsidiary undertaking may be excluded from consolidation because its inclusion is not material` | A grant with an "if" gate: "may be excluded from consolidation if its inclusion is not material". Where the gate fails: (A) NOTHING, a grant limited by its own wording that the text does not turn into a bar; (B) JUST FALSE, a failed "if" read as the text's own no. | A for the single-undertaking limb. The bracket "two or more undertakings may be excluded only if they are not material taken together" closes its own gate with "only if" and stays JUST FALSE. The caller `s 405(1)` reads a NOTHING from the exceptions as "no exception shown", so "all the subsidiary undertakings ... must be included" stands (JUST TRUE). | s 405(2): "A subsidiary undertaking may be excluded from consolidation if its inclusion is not material for the purpose of giving a true and fair view (but two or more undertakings may be excluded only if they are not material taken together)." s 405(1): "...must be included in the consolidation, subject to the following exceptions." |

### Listed, not flipped (name-test sweep of 2026-11-12)

One row per function.
The first eight are "may" functions whose gate is "where", "when", "upon" or an equivalent condition of that kind ("so long as", "on an application", and, for the last two, a "provided" proviso): ASSUMED, NOT RULED, that the equivalents go with the listed group.
The last four are "entitled"-named.
The other reading in each row is for the maintainer or a lawyer: ruling (b) of the Guide's paragraph on periods, "where" and scope limits (and ruling (c) of the 2026-11-05 delegated ruling) says JUST FALSE where a "where" condition fails, and the Guide's line on grants points to NOTHING; the sweep does not settle it.

| function | group | gate in the text | answer now | other reading |
| --- | --- | --- | --- | --- |
| `s 371(2) the director may apply to the court ...` | (i) | "Where such a notice is given to a company" and "within the period of 28 days beginning with the date of the giving of the notice" | JUST FALSE where no notice is given or the 28 days are over | NOTHING for the "where" gate (the 28-day period stays JUST FALSE under the periods ruling (a)) |
| `s 371(3) the court may make the alternative directions` | (i) | "Where an application is made on the ground mentioned in subsection (2)(b)" | JUST FALSE where no such application is made | NOTHING |
| `s 373(2) the court may order the company and specified officers or employees to provide the information` | (i), mixed | "If the company, having been required by the group to do so, refuses ..., the court may, on an application made by the group" (an "if" and an "on an application") | JUST FALSE where there is no refusal or no application | NOTHING (the "on an application" gate is of the listed kind, so the function is not flipped on the strength of its "if") |
| `s 394C(3)(b) the person may enforce the guarantee against the parent undertaking` | (i) | "A guarantee given under this section" (the guarantee is the subject of the sentence; "in the case of a guarantee given") | JUST FALSE where no guarantee is given | NOTHING |
| `s 405(3) the subsidiary undertaking may be excluded from consolidation in one of the three cases` | (i) | "may be excluded from consolidation where— (a) ... (b) ... (c)" | JUST FALSE where none of the three holds | NOTHING |
| `s 408(3) the individual profit and loss account may be omitted from the company's annual accounts ...` | (i) | "This section applies where" (subsection (1)) | JUST FALSE where section 408 does not apply | NOTHING |
| `s 395(4A) the directors may change to Companies Act individual accounts for a reason other than a relevant change of circumstance` | (i), "provided" | "provided they have not changed to Companies Act individual accounts in the period of five years preceding the first day of that financial year" (read as "so long as") | JUST FALSE where the directors changed in the five years | NOTHING, the power stated with a proviso that is not met (it flows to the callers `s 395(3)` and `s 403(4)`, which would then need to read a NOTHING from (4A) as "relief not shown") |
| `s 403(5A) the directors may change to Companies Act group accounts for a reason other than a relevant change of circumstance` | (i), "provided" | as s 395(4A), to which it delegates | as s 395(4A) | as s 395(4A) |
| `s 372(3) the group is entitled to be paid costs out of the assets of the company` | (ii) | "is not entitled ... except by virtue of such an order" | JUST FALSE where no order has been made; NOTHING where one has | an entitlement is a claim, not a power: the Guide does not settle it |
| `s 373(1) the group is entitled to require the company to provide the information` | (ii) | "Where proceedings have been brought under section 370 ... by an authorised group, the group is entitled" | JUST FALSE where no such proceedings have been brought; NOTHING where the information is not of the kind described | as above |
| `s 394B the company is entitled to the exemption conferred by section 394A` | (ii) | "A company is not entitled ... if it was at any time within the financial year ... [an excluded kind]" | JUST FALSE where it was an excluded kind; NOTHING otherwise | as above |
| `s 414B the company is entitled to the small companies exemption in relation to the strategic report` | (ii) | "A company is entitled ... for a financial year if— (a) ... (b) ..." | JUST FALSE where neither limb holds | as above |

### Name-test sweep of 2026-11-12

Every layer-1 function whose name contains "may", "permitted", "power", "entitled" or "authorised" was read against the three tests of the sweep (the specification is `name-test-sweep.md`).
A flip changes the function's answer where its "if" gate fails, from `JUST FALSE` to `NOTHING`; the fork line is F15 in the fork register and the last row of the marginal readings.
The two "provided" sites (`s 395(4A)`, `s 403(5A)`) were first flipped and then put back and listed: a "provided" proviso is treated as the "so long as" kind, as other parts of this family treat it, and the guide does not settle it.

| flipped to NOTHING | kept JUST FALSE (gate closed by the text) | listed: "may" with where/when/upon | listed: "entitled" |
| --- | --- | --- | --- |
| 1 | 11 | 8 | 4 |

Flipped to NOTHING (1), with the other reading in the fork register:
- `s 405(2) the subsidiary undertaking may be excluded from consolidation because its inclusion is not material` (F15; the "only if" bracket for two or more undertakings stays JUST FALSE).

Its caller was checked against its own text and changed so that it still answers what it requires: `s 405(1)` reads a NOTHING from the exceptions as "no exception shown" and so keeps the duty to include (JUST TRUE).

Kept JUST FALSE (11), with why the gate is closed or why the function is not named for a grant:
- `s 366(2) the donation or expenditure is authorised as section 366(2) requires`: a duty ("must be authorised");
- `s 366(6) section 366 enables the company to be authorised to do it`: a flat negative ("Nothing in this section enables ...");
- `s 367(6) the resolution authorises up to a specified amount for each head`: a duty ("must authorise ... up to a specified amount");
- `s 368(2) the directors have power to determine a shorter period`: the text's own exception ("subject to any provision of the articles that operates to prevent them");
- `s 370(3) the members are an authorised group`: a definition ("means");
- `s 370(4) the group may bring proceedings under section 370`: "may not ... unless" (section 371(1));
- `s 371(4) the company may bring proceedings to enforce those duties`: "only with the permission of the court";
- `s 371(5) the group may discontinue or settle the proceedings`: "may not ... except with the permission of the court";
- `s 392(4) a notice may be given in respect of the previous accounting reference period`: "may not be given ... if" (a flat bar);
- `s 395(1) the individual accounts may be prepared in accordance with the framework` and `s 403(2) the group accounts may be prepared in accordance with the framework`: JUST FALSE comes from the bars of the duties ("must be Companies Act accounts", "must be IAS accounts"), not from an "if" gate on the grant.

Listed, "may" with where/when/upon (8; rows in the fork register, assumed not ruled): `s 371(2) the director may apply to the court ...`; `s 371(3) the court may make the alternative directions`; `s 373(2) the court may order the company and specified officers or employees to provide the information` (mixed: an "if" and "on an application"); `s 394C(3)(b) the person may enforce the guarantee against the parent undertaking`; `s 405(3) the subsidiary undertaking may be excluded from consolidation in one of the three cases`; `s 408(3) the individual profit and loss account may be omitted from the company's annual accounts ...`; and the two "provided" sites `s 395(4A) the directors may change to Companies Act individual accounts for a reason other than a relevant change of circumstance` and `s 403(5A) the directors may change to Companies Act group accounts for a reason other than a relevant change of circumstance`.

Listed, "entitled" (4; rows in the fork register): `s 372(3) the group is entitled to be paid costs out of the assets of the company`; `s 373(1) the group is entitled to require the company to provide the information`; `s 394B the company is entitled to the exemption conferred by section 394A`; `s 414B the company is entitled to the small companies exemption in relation to the strategic report`.

Outside the sweep, named "it is lawful": 0.

Not counted, because they never answer JUST FALSE (JUST TRUE or NOTHING only, or a number): `s 367(1) the resolution may relate to`; `s 367(2) ...`; `s 367(3) ...`; `s 370(2) the company may itself bring proceedings to enforce the liability`; `s 372(2) the group may apply for an order that the company indemnify the group ...`; `s 377(1) authorisation under this Part is not needed ...`; `s 378(1) authorisation is not needed for the whole of this donation`; `s 392(1) the company may by notice ... specify a new accounting reference date ...`; `s 399(4) the exempt company may prepare group accounts`; `s 411(2) the categories are ones the directors may select`; `s 414A(4) the group strategic report may, where appropriate, give greater emphasis ...`; and the amounts `s 369(2)(a) ...`, `s 377(3) ...`, `s 378(1) the part of this donation for which authorisation is needed`, `s 378(3) ...`.

## Jural relations (coa8)

One row per provision (or group of provisions) that creates a relation.
Kinds follow Hohfeld: right and duty, privilege and no-right, power and liability, immunity and disability.
Where the text names only the bearer (a prohibition, a duty with no named beneficiary), the holder column says so; no beneficiary is invented (ruling N2).
A provision that creates no relation (a definition, a counting rule, a signpost, a regulation-making power) is listed once as `none`.
The L4 rule column names the function (or the first of them); the coverage table gives every row.

| section | holder of the right, privilege, power or immunity | bearer of the duty, no-right, liability or disability | kind and content | L4 rule |
| --- | --- | --- | --- | --- |
| s 362 | none | none | statement of what the Part controls (inert, reason 1) | none |
| ss 363 to 365 | none | none | definitions of the parties, "political donation" and "political expenditure" | `s 363(2) the organisation is a political organisation`; `s 364(2)(a) ...`; `s 365(1) ...` |
| s 366(1) | none named | the company | duty (prohibition): not to make a political donation or incur political expenditure unless authorised | `s 366(1) the company is forbidden to make the donation or incur the expenditure`; rule `s 366(1) the company shall not make an unauthorised donation or incur unauthorised expenditure` |
| s 366(2), (3), (5) | the members of the company, and of each relevant holding company | the company (and its directors, through s 369) | power to authorise by resolution; liability of the company to the limit the resolution sets; (3): immunity of a wholly-owned subsidiary of a UK-registered company from needing its own resolution | `s 366(2) the donation or expenditure is authorised as section 366(2) requires`; `s 366(3) ...`; `s 366(5) ...` |
| s 366(4) | none | none | definition of "relevant holding company" | `s 366(4) the other company is a relevant holding company` |
| s 366(6) | none | the company | disability: a resolution cannot authorise what the company could not lawfully do | `s 366(6) section 366 enables the company to be authorised to do it` |
| s 367 | none | none | conditions on the form of the members' power under s 366 | `s 367 the resolution is in the form section 367 requires` |
| s 368 | the directors (power to determine a shorter period), the articles (limit) | the resolution's authority | power of the directors to shorten the four years, subject to the articles; the four years are a counting rule | `s 368(1) the last day on which the resolution has effect`; `s 368(2) ...` |
| s 369 | the company | the directors in default (jointly and severally) | right and duty: to make good the unauthorised amount with interest, and to compensate for loss or damage | `s 369(2) the person is jointly and severally liable to make good and to compensate the company`; rule `s 369(2) the director in default shall make good and compensate` |
| s 370 | an authorised group of members | the director liable under s 369 | power to bring proceedings in the company's name; liability of the director to be sued | `s 370(1)(a) ...`; `s 370(3) the members are an authorised group` |
| s 371(1) | the company and the director (immunity from proceedings) | the group of members | disability: the group may not bring proceedings until notice is given and 28 days have elapsed | `s 371(1) the notice requirements are met`; rule `s 371(1) the group shall not bring proceedings ...` |
| s 371(2), (3) | any director of the company (power to apply); the court (power to direct) | the group (liability to have its proceedings stopped) | powers: to apply within 28 days, and for the court to order that the proceedings not be brought or to give directions | `s 371(2) the director may apply to the court ...`; `s 371(3) ...` |
| s 371(4), (5) | the company (to sue the members, with permission); the court (permission) | the group (disability to discontinue or settle without permission) | power and disability | `s 371(4) ...`; `s 371(5) ...` |
| s 372 | the group (right to costs only if the court orders an indemnity) | the company (duty to indemnify only under the order) | right and duty by order; otherwise no-right | `s 372(3) ...`; `s 372(4)(a)`, `(b)` |
| s 373 | the group (right to information) | the company (duty); officers and employees (liability to a court order) | right and duty; power of the court | `s 373(1) ...`; `s 373(2) ...` |
| s 374 | the company (immunity) | none named | immunity: a donation to a trade union other than to its political fund is not a political donation | `s 374(1) the donation to the trade union is a political donation for the purposes of this Part` |
| s 375 | the company (immunity) | none named | immunity: a membership subscription to a trade association is not a political donation | `s 375(1) ...` |
| s 376 | the company (immunity) | none named | immunity: an all-party parliamentary group is not a political organisation | `s 376(1) ...` |
| s 377(1) | the company (privilege) and the Secretary of State (power to exempt by order) | none named | authorisation is not needed for expenditure exempted by an order; the power to make the order is machinery (inert, F2) | `s 377(1) ...` |
| s 378 | the company (privilege) | none named | privilege: donations up to 5,000 pounds in twelve months, with other relevant donations, need no authorisation | `s 378(1) authorisation is not needed for the whole of this donation`; `s 378(1) the part of this donation for which authorisation is needed` |
| s 379 | none | none | definitions and a counting rule (the date a donation is made) | `s 379(1) ...`; `s 379(2) ...` |
| ss 380 to 385 | none | none | definitions deciding which regime applies (small, micro-entity, quoted); the privileges they unlock are in later Parts outside this range | `s 381 ...`; `s 382(3) ...`; `s 383(4) ...`; `s 384(1) ...`; `s 384A(4) ...`; `s 385(2) ...` |
| s 386 | none named (the members, the regulator and creditors rely on the records through other Parts) | the company; the parent company for a subsidiary undertaking (s 386(5)) | duty to keep adequate accounting records and, for a goods business, stock statements | `s 386(1) ...`; `s 386(4) ...`; `s 386(5) ...`; rule `s 386(1) the company shall keep adequate accounting records` |
| s 387 | the prosecutor (the State) | the officer in default | liability to the offence; the officer's privilege where they acted honestly and the default was excusable (a defence, s 387(2)); penalty | `s 387(1) ...`; `s 387(2) ...`; `s 387(3) ...` |
| s 388 | the company's officers (right to inspect) | the company | duty to keep the records at the registered office or elsewhere, open to inspection; for records kept abroad, to send accounts and returns; to preserve for three or six years | `s 388(1) ...`; `s 388(2) ...`; `s 388(3) ...`; `s 388(4) ...` |
| s 389 | the prosecutor | the officer | liability for default under s 388 and for intentionally causing it; defence; penalty | `s 389(1) ...`; `s 389(2) ...`; `s 389(3) ...`; `s 389(4) ...` |
| ss 390 and 391 | none | none | counting rules for the financial year and the accounting reference period | `s 390(2)(a) ...` to `s 391(6) ...` |
| s 390(5) | none named | the directors of a parent company | duty to secure that the subsidiary undertakings' financial years coincide with the company's, unless in their opinion there are good reasons | `s 390(5) ...` |
| s 392 | the company (power to alter the accounting reference date by notice) | the company's own periods; the registrar | power; disability where the notice is ineffective (less than five years after an extension; over 18 months) | `s 392(1) ...`; `s 392(3) ...`; `s 392(5) ...` |
| s 393 | none named | the directors; the auditor (to have regard) | duty not to approve accounts unless satisfied they give a true and fair view | `s 393(1)(a) ...`; `s 393(2) ...`; rule `s 393(1) the directors shall not approve accounts ...` |
| s 394 | none named | the directors | duty to prepare individual accounts for each financial year | `s 394 the directors are required to prepare individual accounts for the financial year`; rule `s 394 ...` |
| ss 394A to 394C | a dormant subsidiary company (immunity from the duty); its members (power to agree); persons to whom it is liable (right to enforce the guarantee) | the parent undertaking (duty as guarantor); the company (disability if within s 394B) | immunity on conditions; power of members; right and duty on the guarantee | `s 394A(1) ...`; `s 394A(2) ...`; `s 394B ...`; `s 394C(1) ...`; `s 394C(3)(b) ...` |
| s 395 | the directors (power to choose Companies Act or IAS accounts; (4A) power to change back for another reason if they have not changed in the preceding five years) | the directors, after the first IAS year (duty (3) to keep preparing IAS accounts unless there is a relevant change of circumstance); a charity (duty (2) to use Companies Act accounts) | power, duty and disability | `s 395(1) ...` to `s 395(5) ...` |
| ss 396 and 397 | none named | the directors | duty as to the form and content of the accounts, to give a true and fair view, and to depart where necessary with particulars in a note | `s 396(A1) ...` to `s 397(2) ...` |
| s 399 | none named; (4): the exempt company (power to prepare group accounts anyway) | the directors of a parent company | duty to prepare group accounts; exemptions | `s 399(2) ...`; `s 399(2A) ...`; `s 399(3) ...`; `s 399(4) ...` |
| ss 400 to 402 | the company (immunity from the duty); shareholders holding 5% (power to serve notice and so defeat the exemption); the remaining shareholders (power to approve) | the company | immunity on conditions; powers of the shareholders | `s 400(1) ...`; `s 400(2) ...`; `s 401(1) ...`; `s 402 ...` |
| s 403 | the directors (power to choose and to change) | the parent company | as s 395, for group accounts | `s 403(1) ...` to `s 403(6) ...` |
| ss 404 to 406 | none named | the directors | duty as to form and content; to consolidate every subsidiary undertaking unless excluded; privilege to exclude in three cases | `s 404(1) ...`; `s 405(1) ...`; `s 405(2) ...`; `s 405(3) ...`; `s 406(1) ...` |
| s 407 | none named | the directors of a parent company | duty to secure that the same financial reporting framework is used, unless there are good reasons; immunities for charities and for IAS | `s 407(1) ...` to `s 407(5) ...` |
| s 408 | the company (privilege to omit its own profit and loss account) | none named | privilege on conditions | `s 408(1) ...`; `s 408(3) ...`; `s 408(4) ...` |
| s 409 | the Secretary of State (power by regulations); the company (privilege not to disclose with the Secretary of State's agreement) | none named | (1) to (3) machinery (inert, reason 2); (4) privilege; (5) duty to say so in a note | `s 409(4) ...`; `s 409(5) ...` |
| s 410A | none named | the company | duty to give information about off-balance sheet arrangements; small-company relief | `s 410A(1) ...`; `s 410A(2) ...`; `s 410A(4) ...` |
| s 411 | none named | the company | duty to disclose employee numbers and staff costs | `s 411(1) ...` to `s 411(7) ...` |
| s 412 | the Secretary of State (power by regulations); the company (right to the notice) | directors and former directors of the last five years (duty); the person in default (liability) | (1) to (3) machinery (inert, reason 2); (5) duty to give notice to the company; (6) offence and penalty | `s 412(5) ...`; `s 412(6) ...`; rule `s 412(5) the director shall give notice to the company` |
| s 413 | none named | the company | duty to show advances, credit and guarantees to directors; privilege for banking companies to state fewer totals | `s 413(1) ...` to `s 413(8) ...` |
| s 414 | none named; the prosecutor | the board (approve) and a director (sign); a director who approves accounts that do not comply (liability) | duty, offence and penalty | `s 414(1) ...`; `s 414(4) ...`; `s 414(5) ...`; rules `s 414(1) ...` |
| s 414A | none named; the prosecutor | the directors | duty to prepare a strategic report (a group strategic report for a parent); offence and penalty | `s 414A(1) ...` to `s 414A(6) ...` |
| s 414B | a small company (immunity from the strategic report duty) | none named | immunity on conditions | `s 414B ...` |

## Marginal readings for a lawyer (coa8)

Two readings of the rule of 2026-10-29 are for a lawyer, not for the encoder: (a) a failed "if" counts as the text's no, clause by clause, within the provision that holds the "if", and flat negatives count as the text saying no; (b) a prohibition or grant limited by its own wording does not.
Every branch below rests on one of them or on a fork, with the other reading stated.

| provision | function | answer taken | the other reading |
| --- | --- | --- | --- |
| s 363(1) | `s 363(1) this Part applies to the political party` | JUST FALSE for a party not registered, from "applies to a political party if it is registered" (a) | NOTHING: "if" does not say "only if" |
| s 363(3) | `s 363(3) this Part applies to the independent election candidate` | NOTHING for a person not standing at an election, from the limit "at any election to public office held in the United Kingdom" (b) | JUST FALSE |
| s 366(1) | `s 366(1) the company is forbidden to make the donation or incur the expenditure` | NOTHING where the company makes no donation and incurs no expenditure (the prohibition names only those), see finding 2 | JUST FALSE ("not forbidden") |
| s 366(6) | `s 366(6) section 366 enables the company to be authorised to do it` | JUST FALSE where the company could not lawfully do it apart from the section ("Nothing in this section enables ..." is a flat negative); NOTHING where it could (the negative withholds nothing there) | JUST TRUE where it could |
| ss 374, 375, 376 | `s 374(1) ...`, `s 375(1) ...`, `s 376(1) ...` | JUST FALSE inside the exemption ("is not a political donation", a flat negative); NOTHING outside it (the exemption names only the trade union, the subscription, the all-party group; section 364 decides the rest) | JUST TRUE outside the exemption |
| s 377(1) | `s 377(1) authorisation under this Part is not needed ...` | NOTHING where no order exempts the expenditure (the orders are not among the sources) | JUST FALSE |
| s 378(1) | `s 378(1) authorisation is not needed for the whole of this donation` | NOTHING above 5,000 pounds in twelve months ("except to the extent that the total ... exceeds"): the part needing authorisation is computed instead (`s 378(1) the part of this donation for which authorisation is needed`) | JUST FALSE |
| s 388(4) | `s 388(4) the accounting records must still be preserved on the day` | JUST FALSE after the period, NOTHING on the anniversary day (F8) | JUST FALSE on the anniversary, or JUST TRUE |
| s 394B | `s 394B the company is entitled to the exemption conferred by section 394A` | NOTHING where none of the excluded kinds applies (the section only withholds), see finding 3 | JUST TRUE |
| s 394C(3)(b) | `s 394C(3)(b) the person may enforce the guarantee against the parent undertaking` | NOTHING for a person to whom the subsidiary is not liable on those liabilities ("enforceable by any person to whom the subsidiary company is liable"), see finding 4 | JUST FALSE |
| s 384(1) | `s 384(1) the company is excluded from the small companies regime` | JUST FALSE for a company in none of the listed kinds, read with s 381(b) (F5) | NOTHING |
| s 386(4) | `s 386(4) the records are required to contain the stock and goods statements` | JUST FALSE where the business does not involve dealing in goods ("If" unmet, a "where" condition) | NOTHING |
| s 388(2), (3), s 407(1) | the compliance checks | JUST TRUE where the "if" is unmet (F3) | NOTHING or JUST FALSE |
| s 400(4), s 401(4) | `s 400(4) the exemption applies to the company` | JUST FALSE for a company that was a traded company ("The exemption does not apply to ..."); NOTHING otherwise | JUST TRUE otherwise |
| s 407(2) | `s 407(2) subsection (1) applies` | JUST FALSE where the directors prepare no group accounts ("does not apply if ..."); NOTHING where they do | JUST TRUE where they do |
| s 407(4) | `s 407(4) subsection (1) requires the charity's accounts to use the same framework as the non-charity's` | JUST FALSE for a charity and a non-charity ("does not require"); NOTHING otherwise | JUST TRUE otherwise |
| s 411(1A), s 411(5) | `s 411(1A) ...`, `s 411(5) ...` | NOTHING for a company subject to the small companies regime under (1A) ("In the case of a company not subject to the small companies regime" limits the grant); JUST FALSE under (5) ("Except in the case of a company subject to the small companies regime": an "except", read as the text's no) | the two should arguably agree: both JUST FALSE, or both NOTHING |
| s 414A(2) | `s 414A(2) subsection (1) applies to the company` | JUST FALSE for a company entitled to the small companies exemption ("does not apply if"); NOTHING otherwise | JUST TRUE otherwise (this one flows into `s 414A(1)`, which answers JUST TRUE for a company not so entitled, because the duty of subsection (1) stands where subsection (2) does not take it away) |
| s 369(1) | `s 369(1) section 369 applies` | JUST FALSE for a donation that was authorised ("applies where ... without the authorisation required"), a "where" condition | NOTHING |
| s 371(2) | `s 371(2) the director may apply to the court ...` | JUST FALSE outside the 28 days (a period fixed in the text's own words); NOTHING for "some other ground" and for a person who is not a director ("any director may apply" limits the grant) | JUST FALSE for both |
| s 372(3) | `s 372(3) the group is entitled to be paid costs out of the assets of the company` | JUST FALSE where no order has been made ("is not entitled ... except by virtue of such an order"); NOTHING where one has (its terms are the court's) | JUST TRUE where one has |
| s 387(2), s 389(2) | `s 387(2) this subsection gives the person a defence on these facts` | JUST FALSE where the facts proved do not make out the defence, worded "this section gives no defence on these facts", never "no defence at all" (ruling of 2026-11-05) | NOTHING |
| s 412(5) | `s 412(5) the person is under the duty to give notice ...` | NOTHING for a person who has never been a director (F12: the text speaks of a director and of one in the last five years) | JUST FALSE |
| s 405(2) | `s 405(2) the subsidiary undertaking may be excluded from consolidation because its inclusion is not material` | NOTHING where its inclusion is material and the "only if" bracket is not in play ("may be excluded ... if its inclusion is not material" is a grant with an "if" gate); JUST FALSE where two or more undertakings are excluded and are material together ("only if"), fork F15 | JUST FALSE for the single-undertaking case, a failed "if" read as the text's own no |

The exhaustive list of branches that rest on reading (a) or (b) is every `-- FALSE-kind` comment in the layer-1 modules (191 of them in `coa8-part*.l4`); the table above holds the sites where the other reading would change a person-facing answer.

### Reading a result: FALSE and NOTHING (coa8)

Every decision function in this range answers one of three things.
`JUST TRUE` means the text says yes to the case on the facts given.
`JUST FALSE` means the text says no in its own words: a definition that says "means" (a political organisation, an authorised group, a quoted company), a condition introduced with "if", "only if", "unless", "except", "where" (the "if" of s 386(4), the "where" of s 369(1), the "except" of s 411(5)), a period the text fixes (the 28 days of s 371(2), the three or six years of s 388(4), the six months of s 400(1)), or a flat negative ("must not", "may not", "does not apply", "is not entitled", "is not a political donation").
`NOTHING` means the Act does not decide the case on the facts given.
It is "not covered", and a caller must never read it as no.
In this range it arises in five ways.
It arises where the text limits a grant or a prohibition in its own wording and the case falls outside the limit (s 363(3): a person not standing at an election; s 366(1): a company that makes no donation and incurs no expenditure; s 394B: a company in none of the excluded kinds).
It arises where the text points to a power, order, rate or authority outside the sources (the orders of s 377, the interest rate of s 369(5)(b), the regulations behind ss 409 and 412, the agreement of the Secretary of State in s 409(4)).
It arises where the text lists without closing the list or says "includes" (s 379: "director includes shadow director"; s 411(6): "pension costs includes").
It arises where the text is silent (s 388(4) on the anniversary day itself).
It arises where an answer another part owns is not known: the seams of "Seams (coa8)" are `MAYBE BOOLEAN`, a `NOTHING` input makes the answer `NOTHING` (never FALSE), and the three-valued helpers let a limb that decides decide.
In the seat the same three answers are printed as `JUST TRUE`, `JUST FALSE` and `NOTHING`.
The seat asks plain true-or-false facts and passes `JUST` of each, so a person who does not know a borrowed fact cannot ask the question; that is an assumption of the seat (see "Seat layer").

## Seams (coa8)

A seam is another part's answer that this range needs.
Each is an input of the function that asks, `MAYBE BOOLEAN` by default (so that "not covered" in the answering section stays "not covered" here), named `s <answering section> <the question it answers>` as PLAN.md section 4 says.
The lead wires the answering part's function to the input by name at the merge.
The list below was produced by a script that reads the `GIVEN` lists of the layer-1 modules and keeps every input whose name begins with a section outside ss 362 to 414B; the module column says where each is asked.
Several seams were spelled more than once, because each function declares its own input and the sentence it sits in names the thing differently: the lead should wire every spelling listed, not one.

### Seams taken from other parts

| input name | type | asked in |
| --- | --- | --- |
| `s 1(1) the body is a company` | MAYBE BOOLEAN | part15-records |
| `s 3(2) the company is limited by shares` | BOOLEAN | part14-remedies |
| `s 4(2) the company is a public company` | BOOLEAN | part15-records |
| `s 4(2) the company was at any time within the financial year a public company` | BOOLEAN | part15-small |
| `s 250 the person is a director of the company` | MAYBE BOOLEAN | part15-notes |
| `s 250 the person occupies the position of director` | MAYBE BOOLEAN | part14-exemptions |
| `s 251 the person is a shadow director` | MAYBE BOOLEAN | part14-exemptions |
| `s 252 the amount is paid to or receivable by a person connected with the director` | MAYBE BOOLEAN | part15-notes |
| `s 255 the amount is paid to or receivable by a body corporate controlled by the director` | MAYBE BOOLEAN | part15-notes |
| `s 260 the member has the right to bring or continue proceedings under Part 11` | MAYBE BOOLEAN | part14-remedies |
| `s 281 a resolution of the members of the company has been passed` | MAYBE BOOLEAN | part14-authorisation |
| `s 360C the company is a traded company` | MAYBE BOOLEAN | part15-group |
| `s 360C the company was at any time within the financial year a traded company` | MAYBE BOOLEAN | part15-accounts |
| `s 442 the last day of the period for filing the company's accounts and reports for that year` | DATE | part15-accounts |
| `s 1121 the officer is in default` | MAYBE BOOLEAN | part15-records |
| `s 1158 the other company is a UK-registered company` | BOOLEAN | part14-authorisation, part14-remedies |
| `s 1159(1) the company by which the donation was made or the expenditure was incurred is a subsidiary of the other company` | MAYBE BOOLEAN | part14-authorisation, part14-remedies |
| `s 1159(1) the company is a subsidiary of another company` | MAYBE BOOLEAN | part14-authorisation |
| `s 1159(1) the company making this donation is a subsidiary of another company` | MAYBE BOOLEAN | part14-exemptions |
| `s 1159(1) the other company is a subsidiary of another UK-registered company` | MAYBE BOOLEAN | part14-authorisation, part14-remedies |
| `s 1159(2) the company is a wholly-owned subsidiary of the other company` | BOOLEAN | part14-authorisation |
| `s 1162 the company is a subsidiary undertaking` | MAYBE BOOLEAN | part15-accounts |
| `s 1162 the company is a subsidiary undertaking or parent undertaking of another UK undertaking` | MAYBE BOOLEAN | part15-year |
| `s 1162 the company is itself a subsidiary undertaking` | MAYBE BOOLEAN | part15-group |
| `s 1162 the undertaking is a subsidiary undertaking of the company` | MAYBE BOOLEAN | part15-group |
| `s 1164(2) the company is a banking company, or the holding company of a credit institution` | BOOLEAN | part15-notes |
| `s 1164(2) the company was at any time within the financial year a banking company` | BOOLEAN | part15-accounts, part15-small |
| `s 1165(2) the company was at any time within the financial year an authorised insurance company` | BOOLEAN | part15-accounts, part15-small |
| `s 1169(1) the company has been dormant throughout the whole of the year` | BOOLEAN | part15-accounts |
| `s 1173(1) at the end of the financial year the company is a parent company` | MAYBE BOOLEAN | part15-group |
| `s 1173(1) in the financial year the company is a parent company` | MAYBE BOOLEAN | part15-approval |
| `s 1173(1) the company is a parent company` | MAYBE BOOLEAN | part15-notes, part15-records, part15-small, part15-year |


The seams the PLAN's section 4 names and this range uses are: `s 4(2)` (public company), `s 3(2)` (limited by shares), `s 1(1)` (the body is a company), `s 1158` (UK-registered company), `s 1159(1)` and `(2)` (subsidiary; wholly-owned subsidiary), `s 1162` (parent and subsidiary undertaking), `s 1164(2)` and `s 1165(2)` (banking company; authorised insurance company), `s 1169(1)` (dormant), `s 1173(1)` (parent company), `s 360C`, `s 250`, `s 251`, `s 252`, `s 255`, `s 260`, `s 281`, `s 442`, `s 1121`.
Two seams are spelled in the PLAN differently from the use here: the PLAN lists `s 1159(1) the company is a subsidiary of the other company`; the Part 14 functions need the question asked of the company making the donation, and so carry four spellings of it (listed above); the PLAN's `s 1173(1) the company is a parent company` appears in three spellings (the 'at the end of the financial year' and 'in the financial year' forms follow the sentences of ss 399 and 414A).
A seam the PLAN lacks and this range needs: `s 442 the last day of the period for filing the company's accounts and reports for that year` (a `DATE`, asked in `s 394A(2)`); `s 260 the member has the right to bring or continue proceedings under Part 11` (asked in Part 14's `s 370`).

### Answers this range gives to other parts

The PLAN asks other parts to take these inputs from this range; the functions that answer them are below, with what a caller must pass.
Where this range answers in two functions (first year and later years) the caller picks by the year the question is about.

| input name the PLAN gives (asked by other parts) | function here | note |
| --- | --- | --- |
| `s 382 the company qualifies as small` | `s 382(1) the company qualifies as small in its first financial year`; `s 382(1A) the company qualifies as small in a subsequent financial year`; for a parent company `s 383(1) the parent company qualifies as a small company` | two functions by year; `s 383(1)` needs both `s 382` on the parent's own figures and the group answer |
| `s 381 ...` (the small companies regime applies) | `s 381 the small companies regime applies to the company for the financial year` | takes `s 382` and `s 384` as inputs |
| `s 384A the company qualifies as a micro-entity` | `s 384A(1)`, `s 384A(2)`, and for a parent `s 384A(8)` | `s 384B(1)` and `(2)` say when the micro-entity provisions do not apply |
| `s 385 the company is a quoted company` | `s 385(2) the company is a quoted company`; `s 385(1) the company is a quoted company in relation to the financial year`; `s 385(3) the company is an unquoted company` | |
| `s 386` (the significant accounting transaction behind "dormant", s 1169) | `s 386(2) the records are adequate accounting records`; `s 386(3) the records contain what subsection (3) requires` | the keel's PLAN note: s 1169 needs s 386 for the transaction that must be entered in the accounting records |
| `s 394B ...`, `s 400(4)`, `s 401(4)` (not a traded company) | `s 394B the company is entitled to the exemption conferred by section 394A`; `s 400(4) ...`; `s 401(4) ...` | each takes `s 360C the company is a traded company` |
| `s 414B ...` (small companies exemption from the strategic report) | `s 414B the company is entitled to the small companies exemption in relation to the strategic report` | asked by coa9 |
| the amounts and dates of Part 15 | the constants `s 382(3) the turnover limit, in pounds` and its siblings | thresholds the Act states; a substitution by regulations would change the answers |

### Core hoist candidate

`s 383(6) the accounts the figures are taken from` (Companies Act accounts or IAS accounts) is a small type that the medium-sized group tests of Part 15 Chapter 4 outside this range (coa10, ss 465 to 467) will want too.
It is kept under this range's prefix; `NEEDS-CORE.md` has one line on it.

## Seat layer (coa8)

The seat is an individual who is, or is about to become, a director, a company secretary or a member (shareholder) of a company registered under the Act, or who deals with one, asking on facts they can state what the Act requires or lets them do, what rights they have against the company or its directors, what they must disclose, file, approve or vote on and by when, and what follows if it is not done.

(Assumed, not ruled: the Act is addressed to companies, so the individual is whoever stands in a company's management or ownership.)

There is no seat for an official; the court, the registrar and the Secretary of State appear only as what the text lets them do to the person.

`coa8-seat.l4` imports the layer-1 modules and calls their rules; it restates none. It was generated by a script from the signatures of the layer-1 rules, so that every call passes its inputs in the order the rule declares them.

Every question is named "Under section N, ...", carries `@export`, and has one `@desc` for each input worded as the person would be asked; the questions are grouped under `§` headings in the text's order.

Inputs are plain: true or false, a number, a date, a list of numbers or a choice of words. A borrowed `MAYBE BOOLEAN` seam is asked as true or false and passed as `JUST` of the answer (assumed, not ruled; this is the same choice every part faces, and the lead should see it). An optional date or number (a date the directors may or may not have determined) is asked with a true-or-false input saying whether it exists (finding 11).

Penalties are asked by how the person would be convicted ("on indictment", "summary conviction", or "summary conviction in England and Wales" and so on) and answered as a sentence by four helper functions in the seat file (`s 387(3) the penalty in words` and its parts).

`coa8-cases-seat.l4` has 414 cases over all 171 questions, including cases marked NOT COVERED whose asserted answer is `NOTHING`; its assertions written equal its assertions satisfied (414 written and 414 satisfied in the last run of check.sh).

### Seat questions

| # | question | cases |
| --- | --- | --- |
| 1 | Under section 363, is this political party one to which the political donations rules apply | 2 |
| 2 | Under section 363, do the political donations rules apply to this independent election candidate | 2 |
| 3 | Under section 363, is this organisation a political organisation | 4 |
| 4 | Under section 364, is this payment or gift a political donation | 3 |
| 5 | Under section 365, is this spending political expenditure | 4 |
| 6 | Under section 366, is this company forbidden to make this political donation or incur this political expenditure | 9 |
| 7 | Under section 366, is this other company a relevant holding company of ours | 3 |
| 8 | Under section 366, does section 366 enable the company to be authorised to do this thing | 2 |
| 9 | Under section 367, does this authorising resolution have the form the Act requires | 3 |
| 10 | Under section 368, on what date does this authorising resolution stop having effect | 4 |
| 11 | Under section 368, can the directors determine a shorter period for the authorisation | 2 |
| 12 | Under section 369, am I jointly and severally liable to make good this unauthorised donation or expenditure to the company and to compensate it for loss or damage | 4 |
| 13 | Under section 369, how much of the donation or expenditure was unauthorised, in pounds | 2 |
| 14 | Under section 369, how much of the unauthorised donation or expenditure is still to be made good to the company, before interest, in pounds | 1 |
| 15 | Under section 370, are these members an authorised group | 4 |
| 16 | Under section 371, has our group met the notice requirements for bringing proceedings under section 370 | 3 |
| 17 | Under section 371, may I apply to the court for an order that the proposed proceedings are not to be brought | 5 |
| 18 | Under section 371, may the court give the alternative directions section 371(3) allows, where the application is on the ground that the company is already pursuing proceedings | 2 |
| 19 | Under section 371, may the company bring proceedings against the members who sued in its name | 2 |
| 20 | Under section 371, may our group discontinue or settle the proceedings | 2 |
| 21 | Under section 372, is our group entitled to be paid its costs out of the company's assets | 2 |
| 22 | Under section 372, will costs awarded to the company be paid to our group | 2 |
| 23 | Under section 372, must our group pay a defendant's costs | 2 |
| 24 | Under section 373, is our group entitled to require the company to give it information about the proceedings | 3 |
| 25 | Under section 373, may the court order the company and named officers or employees to give us the information | 2 |
| 26 | Under section 374, is this donation to a trade union a political donation | 3 |
| 27 | Under section 375, is this subscription to a trade association a political donation | 2 |
| 28 | Under section 375, how much of this payment is a subscription, in pounds | 1 |
| 29 | Under section 376, is this all-party parliamentary group a political organisation | 2 |
| 30 | Under section 377, is authorisation not needed for this political expenditure | 2 |
| 31 | Under section 378, how much of this donation needs authorisation, in pounds | 2 |
| 32 | Under section 378, does this earlier donation fall in the twelve months ending with the date of this donation | 2 |
| 33 | Under section 378, does another donation count towards the 5,000 pounds limit on this donation | 4 |
| 34 | Under section 379, is this person a director for the purposes of Part 14 | 3 |
| 35 | Under section 379, on what date is the donation treated as made or the expenditure as incurred | 2 |
| 36 | Under section 380, do the requirements of Part 15 on accounts and reports apply to this period | 2 |
| 37 | Under section 381, does the small companies regime apply to this company for the financial year | 3 |
| 38 | Under section 382, does this company meet the qualifying conditions for a small company in this year | 4 |
| 39 | Under section 382, does this company qualify as small in this financial year, after its first | 6 |
| 40 | Under section 382, does this company qualify as small in its first financial year | 2 |
| 41 | Under section 382, what is this company's number of employees for the year | 2 |
| 42 | Under section 383, does this group meet the qualifying conditions for a small group in this year | 3 |
| 43 | Under section 383, does this group qualify as small in this financial year of the parent company, after its first | 3 |
| 44 | Under section 383, does this parent company qualify as a small company | 2 |
| 45 | Under section 384, is this company excluded from the small companies regime | 4 |
| 46 | Under section 384A, does this company meet the qualifying conditions for a micro-entity in this year | 3 |
| 47 | Under section 384A, does this company qualify as a micro-entity in this financial year, after its first | 3 |
| 48 | Under section 384B, do the micro-entity provisions not apply to this company's accounts because of what the company is | 2 |
| 49 | Under section 384B, do the micro-entity provisions also not apply because the company is part of a group | 3 |
| 50 | Under section 385, is this company a quoted company | 2 |
| 51 | Under section 385, is this company a quoted company in relation to this financial year | 2 |
| 52 | Under section 385, is this company an unquoted company | 2 |
| 53 | Under section 386, is this company required to keep adequate accounting records | 2 |
| 54 | Under section 386, are these records adequate accounting records | 2 |
| 55 | Under section 386, do these records contain the entries and the record of assets and liabilities that the section requires | 2 |
| 56 | Under section 386, must these records contain statements of stock and of goods sold and purchased | 2 |
| 57 | Under section 386, do these records contain the stock and goods statements the section requires | 5 |
| 58 | Under section 386, must this parent company take reasonable steps to secure that its subsidiary undertaking keeps accounting records | 2 |
| 59 | Under section 387, does this officer commit an offence because the company has failed to comply with a provision of section 386 | 2 |
| 60 | Under section 387, does this officer have a defence to the accounting records offence | 2 |
| 61 | Under section 387, what is the penalty for the accounting records offence | 4 |
| 62 | Under section 388, are the accounting records kept where and as the section requires | 2 |
| 63 | Under section 388, for records kept outside the United Kingdom, are the accounts and returns kept as the section requires | 2 |
| 64 | Under section 388, are the accounts and returns sent to the United Kingdom such as the section requires | 2 |
| 65 | Under section 388, for how long must the company keep its accounting records | 2 |
| 66 | Under section 388, must the company still keep its accounting records on this day | 3 |
| 67 | Under section 389, does this officer commit an offence because the company has failed to comply with a provision of section 388(1) to (3) | 2 |
| 68 | Under section 389, does this officer have a defence to the offence under section 389(1) | 2 |
| 69 | Under section 389, does this officer commit an offence by failing to take all reasonable steps to secure that the accounting records are preserved as section 388(4) requires, or by intentionally causing a default in preserving them | 4 |
| 70 | Under section 389, what is the penalty for an offence under that section | 2 |
| 71 | Under section 390, on what date does the company's first financial year begin | 1 |
| 72 | Under section 390, on what date does the company's first financial year end | 3 |
| 73 | Under section 390, on what date does a later financial year begin | 1 |
| 74 | Under section 390, on what date does a later financial year end | 3 |
| 75 | Under section 390, is this period the financial year of an undertaking that is not a company | 2 |
| 76 | Under section 390, must the directors secure that the financial year of each subsidiary undertaking coincides with the company's own | 3 |
| 77 | Under section 391, on what date does the company's first accounting reference period end | 3 |
| 78 | Under section 392, is a notice to change the accounting reference date ineffective because an earlier extension was too recent | 4 |
| 79 | Under section 392, may a notice be given in respect of the previous accounting reference period | 2 |
| 80 | Under section 392, is a notice ineffective because the extended period would exceed 18 months | 3 |
| 81 | Under section 392, is this undertaking a UK undertaking | 2 |
| 82 | Under section 393, are the conditions for the directors to approve the individual accounts met | 2 |
| 83 | Under section 393, are the conditions for the directors to approve the group accounts met | 2 |
| 84 | Under section 393, must the auditor have regard to the directors' duty not to approve accounts that do not give a true and fair view | 2 |
| 85 | Under section 394, are the directors required to prepare individual accounts for the financial year | 2 |
| 86 | Under section 394A, is this subsidiary company exempt from the requirement to prepare individual accounts | 2 |
| 87 | Under section 394A, are all the conditions of the subsidiary company's exemption complied with | 3 |
| 88 | Under section 394B, is this company, so far as section 394B goes, entitled to the exemption conferred by section 394A | 2 |
| 89 | Under section 394C, does the parent undertaking's statement of guarantee meet the requirements of the section | 2 |
| 90 | Under section 394C, does the parent undertaking guarantee this liability of the subsidiary company | 2 |
| 91 | Under section 394C, may I enforce the parent undertaking's guarantee against the parent undertaking | 2 |
| 92 | Under section 395, must this company's individual accounts be Companies Act individual accounts | 2 |
| 93 | Under section 395, is there a relevant change of circumstance | 2 |
| 94 | Under section 395, must the directors prepare IAS individual accounts for the financial year | 3 |
| 95 | Under section 396, do the Companies Act individual accounts state what the section requires about the company | 4 |
| 96 | Under section 396, do the individual accounts comprise a balance sheet and a profit and loss account | 2 |
| 97 | Under section 396, do the individual accounts give a true and fair view | 2 |
| 98 | Under section 396, are the micro-entity minimum accounting items presumed to give a true and fair view | 2 |
| 99 | Under section 396, do the individual accounts comply with the regulations as to their form and content | 2 |
| 100 | Under section 396, must additional information be given because compliance with the regulations is not enough for a true and fair view | 3 |
| 101 | Under section 396, must the directors depart from a provision of the regulations because of special circumstances | 2 |
| 102 | Under section 397, do the IAS individual accounts state what the section requires about the company | 2 |
| 103 | Under section 397, do the notes say the accounts follow UK-adopted international accounting standards | 2 |
| 104 | Under section 399, are the directors of this parent company required to prepare group accounts for the year | 3 |
| 105 | Under section 399, does this undertaking fall within section 399(2B) | 2 |
| 106 | Under section 399, is this parent company exempt under one of the further exemptions of sections 400 to 402 | 2 |
| 107 | Under section 399, may this exempt parent company nevertheless prepare group accounts | 2 |
| 108 | Under section 400, how many shares are attributed to the parent undertaking | 1 |
| 109 | Under section 400, is this company a wholly-owned subsidiary of the parent undertaking | 3 |
| 110 | Under section 400, was the minority shareholders' notice served in time | 2 |
| 111 | Under section 400, does the parent undertaking hold 90% or more of the shares and do the remaining shareholders approve | 3 |
| 112 | Under section 400, does the parent undertaking hold more than 50% but less than 90% of the shares with no sufficient notice served | 2 |
| 113 | Under section 400, is this company within one of the cases that carry the exemption for a subsidiary of a UK-established parent undertaking | 3 |
| 114 | Under section 400, are all the conditions of the exemption complied with | 2 |
| 115 | Under section 400, does the exemption apply to this company, so far as section 400(4) goes | 2 |
| 116 | Under section 401, is this company within one of the cases that carry the exemption for a subsidiary of a parent undertaking not established in the United Kingdom | 2 |
| 117 | Under section 401, are all the conditions of the exemption complied with | 2 |
| 118 | Under section 401, does the exemption apply to this company, so far as section 401(4) goes | 2 |
| 119 | Under section 402, is this parent company exempt because all its subsidiary undertakings could be excluded from consolidation | 3 |
| 120 | Under section 403, must the group accounts be IAS group accounts | 2 |
| 121 | Under section 403, must the group accounts be Companies Act group accounts | 2 |
| 122 | Under section 403, is there a relevant change of circumstance | 2 |
| 123 | Under section 403, must the directors prepare IAS group accounts for the financial year | 4 |
| 124 | Under section 404, do the Companies Act group accounts state what the section requires about the parent company | 2 |
| 125 | Under section 404, do the group accounts comprise a consolidated balance sheet and a consolidated profit and loss account | 2 |
| 126 | Under section 404, do the group accounts give a true and fair view | 2 |
| 127 | Under section 404, do the group accounts comply with the regulations as to their form and content | 2 |
| 128 | Under section 404, must additional information be given because compliance with the regulations is not enough for a true and fair view | 2 |
| 129 | Under section 404, must the directors depart from a provision of the regulations because of special circumstances | 2 |
| 130 | Under section 405, must this subsidiary undertaking be included in the consolidation | 3 |
| 131 | Under section 405, may this subsidiary undertaking be excluded from consolidation because its inclusion is not material | 4 |
| 132 | Under section 405, may this subsidiary undertaking be excluded from consolidation in one of the three cases of subsection (3) | 2 |
| 133 | Under section 406, do the IAS group accounts state what the section requires about the parent company | 2 |
| 134 | Under section 406, do the notes say the group accounts follow UK-adopted international accounting standards | 2 |
| 135 | Under section 407, does the duty to use the same financial reporting framework apply to the individual accounts of the parent company and its subsidiary undertakings | 2 |
| 136 | Under section 407, does the duty apply to this subsidiary undertaking's accounts | 2 |
| 137 | Under section 407, must a charity's accounts use the same framework as a non-charity's | 2 |
| 138 | Under section 408, does the exemption for the company's own profit and loss account apply | 2 |
| 139 | Under section 408, has the company's own profit and loss account been approved as the section requires | 2 |
| 140 | Under section 408, is the exemption conferred by section 408 available, so far as section 408(4) goes | 2 |
| 141 | Under section 409, are the conditions for not disclosing information about an undertaking met | 3 |
| 142 | Under section 409, must the notes say that advantage is taken of the exemption from disclosure | 2 |
| 143 | Under section 410A, must the notes give information about off-balance-sheet arrangements | 2 |
| 144 | Under section 411, must the notes disclose the average number of persons employed | 2 |
| 145 | Under section 411, must the notes also disclose the average number of persons in each category | 2 |
| 146 | Under section 411, what is the average number of persons employed | 2 |
| 147 | Under section 411, must the notes or the profit and loss account disclose the total staff costs | 2 |
| 148 | Under section 411, what are the total staff costs, in pounds | 1 |
| 149 | Under section 411, is this cost a pension cost | 2 |
| 150 | Under section 411, is this cost a social security cost | 2 |
| 151 | Under section 412, is this amount treated as paid to or receivable by the director | 2 |
| 152 | Under section 412, am I under a duty to give the company notice of matters relating to myself | 4 |
| 153 | Under section 412, do I commit an offence by making default in giving the notice | 3 |
| 154 | Under section 412, what is the penalty for the offence of failing to give the company notice | 2 |
| 155 | Under section 413, must the details of advances, credit and guarantees be shown in the notes to the individual accounts | 2 |
| 156 | Under section 413, must the details be shown in the notes to the group accounts | 2 |
| 157 | Under section 413, are the details of an advance or credit given as the section requires | 2 |
| 158 | Under section 413, are the details of a guarantee given as the section requires | 2 |
| 159 | Under section 413, is this person one of the directors for the purposes of the section | 2 |
| 160 | Under section 413, do the requirements of the section apply to this advance, credit or guarantee | 2 |
| 161 | Under section 414, have the annual accounts been approved and signed as the section requires | 2 |
| 162 | Under section 414, is the signature on the balance sheet | 2 |
| 163 | Under section 414, does the balance sheet contain the required statement in a prominent position above the signature | 2 |
| 164 | Under section 414, does this director commit an offence by approving accounts that do not comply with this Act | 3 |
| 165 | Under section 414, what is the penalty for approving accounts that do not comply | 2 |
| 166 | Under section 414A, are the directors required to prepare a strategic report for the financial year | 2 |
| 167 | Under section 414A, must the strategic report be a group strategic report | 2 |
| 168 | Under section 414A, may the group strategic report give greater emphasis to the matters significant to the group as a whole | 2 |
| 169 | Under section 414A, does this director commit an offence by failing to prepare a strategic report | 2 |
| 170 | Under section 414A, what is the penalty for failing to prepare a strategic report | 1 |
| 171 | Under section 414B, is this company entitled to the small companies exemption in relation to the strategic report | 3 |

### Seat audit of 2026-11-12

All 171 seat questions were read, each name and `@export` text against the layer-1 rule its body calls and what that rule answers.

Direction mismatches (a title worded as a permission over a rule that returns the bar, or the reverse): 0. Every "may" title calls a rule of the same name and direction, every "is barred" title a rule that answers the bar, and a flat negative is asked as the thing it denies (is it a political donation, does it apply).

Subject mismatches (a premise or a consequence the rule does not compute, a question that asks more or less than the limb the body answers, or a different subject): 14, all retitled below with their `@export` text; the rule, the inputs and their order, and every fact and expected value are unchanged, and no answer was negated.

The 34 assertions of `coa8-cases-seat.l4` that call a retitled question were restated in place, each preceded by `-- RECONCILED 2026-11-12: was <the original assertion text>; ...`.

| # | was | now | why |
| --- | --- | --- | --- |
| 8 | Under section 366, can a members' resolution authorise something the company could not lawfully do | Under section 366, does section 366 enable the company to be authorised to do this thing | premise: the title assumed a thing the company could not lawfully do, but the input asks whether it could; the rule answers whether section 366 enables the authorisation |
| 12 | Under section 369, am I jointly and severally liable to make good this unauthorised donation or expenditure | Under section 369, am I jointly and severally liable to make good this unauthorised donation or expenditure to the company and to compensate it for loss or damage | asked less: the rule makes the director liable both to make good and to compensate |
| 15 | Under section 370, are these members an authorised group who may bring proceedings in the company's name against a director | Under section 370, are these members an authorised group | consequence: the rule says whether the members are an authorised group; bringing proceedings also needs the conditions of ss 370(1) and 371(1) |
| 18 | Under section 371, may the court direct that the members' proceedings go ahead and the company's be discontinued | Under section 371, may the court give the alternative directions section 371(3) allows, where the application is on the ground that the company is already pursuing proceedings | asked less: the rule covers the alternative directions of s 371(3), both limbs, not only the discontinuance of the company's proceedings |
| 59 | Under section 387, does this officer commit an offence because the company has not kept adequate accounting records | Under section 387, does this officer commit an offence because the company has failed to comply with a provision of section 386 | asked less: the rule covers a failure to comply with any provision of s 386, not only the keeping of adequate records |
| 67 | Under section 389, does this officer commit an offence because the company has not kept its accounting records as section 388 requires | Under section 389, does this officer commit an offence because the company has failed to comply with a provision of section 388(1) to (3) | asked more: the rule covers subsections (1) to (3) of s 388; the preservation period of s 388(4) is s 389(3) |
| 69 | Under section 389, does this officer commit an offence of failing to secure that accounting records are kept or of intentionally causing a default | Under section 389, does this officer commit an offence by failing to take all reasonable steps to secure that the accounting records are preserved as section 388(4) requires, or by intentionally causing a default in preserving them | wrong subject: s 389(3) is about preserving the records for the period of s 388(4), not about keeping them |
| 88 | Under section 394B, is this company entitled to the exemption conferred by section 394A | Under section 394B, is this company, so far as section 394B goes, entitled to the exemption conferred by section 394A | asked more: the rule answers only the s 394B limb of the entitlement; section 394A decides the rest |
| 93 | Under section 395, is there a relevant change of circumstance that lets the company change the kind of accounts it prepares | Under section 395, is there a relevant change of circumstance | consequence: the rule says there is a relevant change of circumstance; what the change lets the company do is s 395(3) and (4A) |
| 105 | Under section 399, does this undertaking fall within section 399(2B), so that it stops its parent company from using the small companies regime exemption | Under section 399, does this undertaking fall within section 399(2B) | consequence: the rule says whether the undertaking falls within s 399(2B); what that does to the parent company is s 399(2A)(b) |
| 115 | Under section 400, does the exemption apply to this company, given that it is not a traded company | Under section 400, does the exemption apply to this company, so far as section 400(4) goes | premise: the title assumed the company is not a traded company, but that is the input |
| 118 | Under section 401, does the exemption apply to this company, given that it is not a traded company | Under section 401, does the exemption apply to this company, so far as section 401(4) goes | premise: the title assumed the company is not a traded company, but that is the input |
| 122 | Under section 403, is there a relevant change of circumstance that lets the parent company change the kind of group accounts it prepares | Under section 403, is there a relevant change of circumstance | consequence: the rule says there is a relevant change of circumstance; what it lets the parent company do is s 403(4) and (5A) |
| 140 | Under section 408, is the exemption available because the fact is disclosed in the company's annual accounts | Under section 408, is the exemption conferred by section 408 available, so far as section 408(4) goes | premise: the title said the exemption is available "because" the fact is disclosed; disclosure is a necessary condition, one limb of the exemption |

## Numbered findings: what the text turns out to say, and what the work turned up

1. **s 391(5): "more than six months" counts the day of incorporation as day one.**
   A company incorporated on 1 September 2025 with an accounting reference date of the last day of February has a first period from 1 September 2025 to 28 February 2026, which is exactly six months, not "more than six months"; the first period therefore runs to 28 February 2027.
   An expected value I first wrote for that case was mis-derived; I corrected it from the text (not from what the code printed) and record it here rather than hide it (`coa8-tests-part15-year.l4`, the `s 391(5)` block; fork F7).
2. **s 366(1) answers NOTHING, not FALSE, for a company that makes no donation and incurs no expenditure**.
   I first wrote the expected answer as `JUST FALSE`; the encoding answers `NOTHING`, because the prohibition names only a political donation and political expenditure and the ruling of 2026-11-05 (c) gives a scope limit with no "only" the answer NOTHING.
   The case in `coa8-cases-seat.l4` was changed to NOTHING with a comment naming this finding.
3. **s 394B only withholds the exemption**.
   Where none of the excluded kinds applies the section is silent and s 394A gives the exemption, so `s 394B ...` answers NOTHING, not `JUST TRUE`; the case was first written as JUST TRUE and corrected.
4. **s 394C(3)(b) makes the guarantee enforceable by "any person to whom the subsidiary company is liable"**.
   For a person to whom it is not liable the text is silent: NOTHING, not `JUST FALSE`; first written as JUST FALSE and corrected.
5. **A regulative `MAY` that lapses unused is FULFILLED, so a trace cannot tell a late act from a timely one**.
   The `s 371(2)` rule (a director may apply within 28 days) prints `FULFILLED` for an application on day 27 and for one on day 28, on both 1.6.110 and 1.6.109.
   I had written the late case's expectation as "not a performance of the permission"; it is not what either binary prints.
   The tested form of s 371(2) is the decision function with the two dates.
6. **s 371 counts days in two ways inside one section.**
   Subsection (1)(b) says "not less than 28 days have elapsed between the date of the giving of the notice ... and the bringing of the proceedings" (a difference of at least 28), and (2) says "within the period of 28 days beginning with the date of the giving of the notice" (the last day is the notice date plus 27).
   The regulative rules use both: `SHANT ... WITHIN 27` for the group and `MAY ... WITHIN 27` for the director, with the notice as day 0 (fork F11).
7. **s 400(1)(c) and s 401(1)(c): only a notice served in time counts toward the 5%.**
   The last sentence ("Such notice must be served at least six months before the end of the financial year to which it relates") is a condition on the notice, so the shares that count are those held by shareholders who served a timely notice; `s 400(1)(c) ...` takes that figure as its third input.
8. **s 378: the twelve-month window begins the day after the same date a year earlier.**
   For a donation on 1 June 2026 a donation on 2 June 2025 is inside the window and one on 1 June 2025 is not (seat case for question 32); `add years` clamps 29 February to 28 February, so the window for a donation on 29 February 2024 begins on 1 March 2023.
9. **s 369(5) and (6): the interest runs on the amount not made good, from the day the donation was made, and only the unauthorised part is covered.**
   The last sentence of s 369(5) ("Section 379(2) ... does not apply for the purposes of this subsection") means the date is the day the donation was actually made, not the earlier day a contract for it was entered into, which s 379(2) would otherwise give; `s 369(5)(a) ...` takes the actual date and ignores the contract date.
10. **ss 411(1A) and 411(5) use different words for the same fact and so answer differently** (marginal reading, see above).
    (1A): "In the case of a company not subject to the small companies regime" limits a grant, so a company that is subject to the regime gets NOTHING; (5): "Except in the case of a company subject to the small companies regime" is an exception, so the same company gets `JUST FALSE`.
11. **Seat: "never" cannot be a plain input.**
    My first generator wrapped every `MAYBE` input of a layer-1 function in `JUST`, which cannot say "no such date" (a director who never was one; no earlier extension of the accounting reference period; no determination by the directors).
    Four questions (s 390(2)(b), s 390(3)(b), s 392(3) and s 412(5)) were rewritten by hand with a true-or-false input that says whether the date exists, and the date is then passed as `JUST` or `NOTHING`.
    For the borrowed `MAYBE BOOLEAN` seams the seat passes `JUST` of a plain answer; a person who does not know such a fact cannot ask the question (assumed, not ruled).
12. **Record fields.**
    A probe on 1.6.110 (two modules each declaring a record with a field named `shared name`, a third importing both and reading both) was accepted.
    Every record field in this range is nonetheless prefixed with its section label, as the brief asks.
13. **A bound variable named like a core field selector is ambiguous.**
    In the seat helpers the pattern variables `level` and `pounds` collided with the fields of the core's `Fine limit` constructors ("multiple definitions for the identifier"); they were renamed.

## What the stable binary does not accept (and what it accepts without saying so)

Sorted by how the failure shows up.
Measured on 1.6.110 and 1.6.109 in this run unless marked.

**Loud (the binary errors, so the problem finds you).**

- `` `WAIT UNTIL` `` in a `#TRACE` is not defined: "I could not find a definition for the identifier `WAIT UNTIL`". `(WAITUNTIL 30)` works on both builds. The skill's reference writes the backticked form; the binary governs.
- `APPEND` joins strings; to join two lists use the prelude's `append` (the type error appeared when I used `APPEND` on lists). Strings in the seat are joined with `CONCAT`.
- A name used both as a bound variable and as a field of a core type is ambiguous ("multiple definitions for the identifier"); rename the variable.
- A `CONSIDER ... WHEN ...` written on one line inside a `WHERE` binding does not parse ("unexpected WHEN"): put each `WHEN` on its own line.
- A list element built with `OF` must be parenthesised, or the list does not type-check.
- A `DEONTIC` value (the result of a regulative rule) cannot be compared with `EQUALS` in an `#ASSERT`. The principal duties are therefore also encoded as decision functions over the facts, and the regulative rules are checked by running them (`#TRACE`) and reading the outcome.
- `@export` on a function that returns `MAYBE BOOLEAN`, `MAYBE DATE`, `MAYBE NUMBER`, `MAYBE STRING` or `DATE` checks clean with `l4 check`; I did not deploy the seat to `jl4-service`.

**Silent (exit 0, an answer that looks right).**

- `NOT a AND b` reads as `NOT (a AND b)` (measured by the keel; this range brackets every `NOT`, and the helper script `lint.sh` in the work folder searches for an unbracketed one).
- `f x's y` reads as `(f x)'s y`: a field access in an argument is parenthesised, `f (x's y)`, and so is `JUST (x's y)`.
- `#TRACE` outcomes are not counted by `check.sh` (it counts error diagnostics and assertion lines only). The outcomes of the 15 traces in `coa8-regulative.l4` were read by hand on both builds and are the same; they are printed below.
- A regulative `MAY` that lapses unused is `FULFILLED`: the trace for a late use of a permission is identical to the trace for a timely one (finding 5). A `MAY` with a `LEST` is read as `FULFILLED` on main and as a breach on unstable (the dialect note in `check.sh`); this range uses no `MAY ... LEST`.
- `Date` rolls over: `Date 31 2 2026` is 3 March 2026 and `Date 1 13 2026` is 1 January 2027; nothing reports an impossible date.
- `add months` and `add years` accept negative counts and clamp the day to the end of a shorter month: `add months (Date 31 12 2026) (-6)` is 30 June 2026 and `add years (Date 29 2 2024) 1` is 28 February 2025. The deadlines of ss 368, 378, 400 and 412 depend on this.
- `l4 run` prints each result twice, so a count of "satisfied" lines by hand is double the number of assertions; `check.sh` and the work folder's `build.sh` print the true count (175 for the 175 assertions of `coa8-tests-part15-group.l4`).

**What was not used, and why.**
`REFUSE`, `#ASSERT REFUSED`, `YMD`, `TYPICALLY`, sets and a bodiless `DECLARE` are excluded by the brief; "not covered" is `NOTHING` or a constructor, asserted.
`BECAUSE` is used only in `LEST BREACH ... BECAUSE`, which the brief accepts.

**The regulative traces (coa8-regulative.l4), read by hand on both builds.**
Outcomes are identical on 1.6.110 and 1.6.109.

| line of `coa8-regulative.l4` | outcome (both builds) |
| --- | --- |
| 30 | DEONTIC BREACHED: BREACH BY Company BECAUSE "the company made a political donation or incurred political expenditure that this Part did not authorise (section 366(1))" |
| 33 | PARTY Company MUST NOT 's 366(1) make a political donation or incur political expenditure without the authorisation this Part requires' HENCE FULFILLED LEST BREACH BY Company BECAUSE "the company made a political donation or incur ... |
| 56 | FULFILLED |
| 60 | FULFILLED AND PARTY Director MUST 's 369(2)(b) compensate the company for any loss or damage resulting from the unauthorised donation or expenditure' HENCE FULFILLED LEST BREACH BY Director BECAUSE "the director in default did not ... |
| 83 | DEONTIC BREACHED: BREACH BY Member BECAUSE "the group brought proceedings under section 370 less than 28 days after giving notice (section 371(1))" |
| 86 | FULFILLED |
| 105 | FULFILLED |
| 108 | FULFILLED |
| 124 | FULFILLED |
| 140 | FULFILLED |
| 158 | DEONTIC BREACHED: BREACH BY Director BECAUSE "the director approved accounts without being satisfied that they give a true and fair view (section 393(1))" |
| 174 | FULFILLED |
| 188 | FULFILLED |
| 207 | FULFILLED |
| 223 | FULFILLED |

## What check.sh prints

Command: `L4=<L4_BIN> L4_MAIN=<L4_MAIN> ./check.sh` run in this folder, default target `main`; the output as printed:

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.109 (main, 4c887e0, 2026-11-04)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
coa-core.l4                                    0         0       0        0         0 |      0         0       0        0  same
coa-definitions.l4                             0         0       0        0         0 |      0         0       0        0  same
coa8-cases-seat.l4                             0       414       0        0         0 |      0       414       0        0  same
coa8-helpers.l4                                0         0       0        0         0 |      0         0       0        0  same
coa8-part14-authorisation.l4                   0         0       0        0         0 |      0         0       0        0  same
coa8-part14-exemptions.l4                      0         0       0        0         0 |      0         0       0        0  same
coa8-part14-meanings.l4                        0         0       0        0         0 |      0         0       0        0  same
coa8-part14-remedies.l4                        0         0       0        0         0 |      0         0       0        0  same
coa8-part15-accounts.l4                        0         0       0        0         0 |      0         0       0        0  same
coa8-part15-approval.l4                        0         0       0        0         0 |      0         0       0        0  same
coa8-part15-group.l4                           0         0       0        0         0 |      0         0       0        0  same
coa8-part15-notes.l4                           0         0       0        0         0 |      0         0       0        0  same
coa8-part15-records.l4                         0         0       0        0         0 |      0         0       0        0  same
coa8-part15-small.l4                           0         0       0        0         0 |      0         0       0        0  same
coa8-part15-year.l4                            0         0       0        0         0 |      0         0       0        0  same
coa8-regulative.l4                             0         0       0        0         0 |      0         0       0        0  same
coa8-seat.l4                                   0         0       0        0         0 |      0         0       0        0  same
coa8-tests-helpers.l4                          0        29       0        0         0 |      0        29       0        0  same
coa8-tests-part14-authorisation.l4             0        84       0        0         0 |      0        84       0        0  same
coa8-tests-part14-exemptions.l4                0        85       0        0         0 |      0        85       0        0  same
coa8-tests-part14-meanings.l4                  0        68       0        0         0 |      0        68       0        0  same
coa8-tests-part14-remedies.l4                  0       105       0        0         0 |      0       105       0        0  same
coa8-tests-part15-accounts.l4                  0       134       0        0         0 |      0       134       0        0  same
coa8-tests-part15-approval.l4                  0        48       0        0         0 |      0        48       0        0  same
coa8-tests-part15-group.l4                     0       175       0        0         0 |      0       175       0        0  same
coa8-tests-part15-notes.l4                     0       100       0        0         0 |      0       100       0        0  same
coa8-tests-part15-records.l4                   0        76       0        0         0 |      0        76       0        0  same
coa8-tests-part15-small.l4                     0       180       0        0         0 |      0       180       0        0  same
coa8-tests-part15-year.l4                      0        89       0        0         0 |      0        89       0        0  same
TOTAL (29 modules)                             0      1587       0        0           |      0      1587       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

The keel's baseline this replaces (KEEL-NOTES.md): 3 modules, 346 satisfied, 0 failed, 0 refused, 0 expected. The keel's test module `coa-definitions-tests.l4` is not in this folder, so this run has the keel's two modules (0 assertions each) and coa8's files.

No assertion is expected to fail: `expected_failed()` in `check.sh` was not edited, and no file here fails on purpose.

## Where PLAN.md and the brief differ (the brief governs)

- PLAN.md section 5 (traps on the stable binary) reports that both supplied builds check and run `REFUSE`, `#ASSERT REFUSED` and `YMD`, although the brief forbids them. None is used here; "not covered" is `NOTHING` or a constructor, asserted.
- The brief allows `LEST BREACH ... BECAUSE` and no other `BECAUSE`; the regulative rules use that form and no other.
- PLAN.md section 2 says that constructors, fields and fixtures count under the no-reuse rule, and calls that a precaution that was not measured. I measured it for fields on 1.6.110: two modules each declaring a record with a field named `shared name`, and a third importing both and reading both, was accepted. Every record field in this range is prefixed anyway (`s 384(2) ...`, `s 395 ...`, `s 407 ...`, `s 413 ...`, `s 413(5) ...`), because the merged seat imports every part. The keel's own `Period`, `Penalty` and `Fine limit` have bare field names (`unit`, `number of units`, `level`, `pounds`), which is how the seat helpers collided with them (finding 13).
- The brief tells each part to name its seam inputs "as PLAN.md section 8 names it"; PLAN.md has six sections and its seam naming is section 4, which is what was followed.
- The brief asks for a seat question for every row that has one and for cases that cover every question; the PLAN does not. The seat here has 171 questions and 414 cases.

## Honest limits

- The text is a converter rendering; nothing here is checked against the official text, and a lawyer has not reviewed any answer.

- The brief asks for all of `references/source-patterns/` to be read; I read only part of it, so a pattern in a file I did not read may have been missed.

- The seat treats a borrowed seam as a plain fact; the layer-1 rules still answer NOTHING where another part passes NOTHING.

- The regulative rules cover the principal duties only (11 rules and 15 traces); the other duties are encoded as decision functions only.

- Amounts left to regulations or orders (the interest rate of s 369(5)(b), the orders of s 377, the regulations behind ss 409 and 412) are inputs; nothing here says what they are.

- `peeked`: nothing. No other directory under `runs/`, nothing under `<local tool>` and no existing encoding was opened. One deviation from the list of allowed reads in the brief: the regulative reference was read from the l4-ide checkout (`<local path>`) rather than from the scratchpad copy of the skill; it is the same skill, not an encoding.
