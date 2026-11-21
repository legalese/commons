# NOTES (sgb1): Companies Act 1967 (Singapore), sections 145 to 160D

Written by part agent `sgb1` for lines 11592 to 13354 of `inputs/CoA1967.txt` (Part 5, Division 2, "Directors and officers": section 145 "Directors" to section 160D).
The audience is the human reviewer and the lead who merges the parts.
Where `inputs/PLAN.md` and the brief (`BRIEF.md`) differ, the brief governs, as the brief says; the differences I found are in "Seams (sgb1)" and "Assumed, not ruled (sgb1)".
`inputs/PLAN.md` in my copy has sections 1 to 6 only (694 lines).
Its own section map (line 17) says section 7 is "the seat layer and the input names every seat shares" and section 8 is "the `NOTES.md` sections you must write and the two split-site questions"; neither is in my copy.
I took the shared seat input names from the brief (`the number of directors of the company`, `the company is a private company`) and the NOTES.md sections and the two split-site questions from the brief.

## Edition encoded

- The Companies Act 1967, 2020 Revised Edition, as the Singapore Statutes Online (SSO) informal consolidation "version in force from 6/5/2026 to 20/10/2026", retrieved 2026-10-09, which carries the amendments up to Act 24 of 2025 (`inputs/SOURCES.md` records its hashes).
- A later consolidation may exist and was not read.
- The encoding is of that text only.
- The text is an SSO rendering of a PDF as plain text, not the official text (SSO's terms, clause 8, say so).
- Nothing here is "verified against the official text".
- Nothing here says that the Singapore Government or the Attorney-General's Chambers endorses, checks or is associated with this work.
- Line numbers everywhere in this file are lines of `inputs/CoA1967.txt` as it is, unless a `file.l4:N` says otherwise.

## Files written (sgb1)

All under `encodings/legalese-sonnet-5.5/`.

| file | lines | `#ASSERT` | `#TRACE` | what it is |
| --- | --- | --- | --- | --- |
| `sgb1-s145-directors.l4` | 780 | 0 | 0 | layer 1: ss 145, 145A, 146, 147 (who may be a director, nominee directors, what is filed first, the share qualification) |
| `sgb1-s148-bankrupt-unfit.l4` | 703 | 0 | 0 | layer 1: ss 148, 149, 149A (undischarged bankrupts; disqualification of unfit directors; national security) |
| `sgb1-s149b-appointment.l4` | 367 | 0 | 0 | layer 1: ss 149B, 150, 151, 152 (appointment, validity of acts, removal) |
| `sgb1-s154-convicted-default.l4` | 650 | 0 | 0 | layer 1: ss 154, 155, 155A (disqualification on conviction, persistent default, three struck-off companies) |
| `sgb1-s155b-debarment.l4` | 544 | 0 | 0 | layer 1: ss 155B, 155C, 155D, 155E (debarment; disqualification under the LLP Act and the VCC Act) |
| `sgb1-s156-interests.l4` | 518 | 0 | 0 | layer 1: s 156 (disclosure of interests in transactions, property and offices) |
| `sgb1-s157-duties.l4` | 467 | 0 | 0 | layer 1: ss 157 to 160 (duty and liability of officers, powers of directors, information and advice, disclosure, approval of disposals) |
| `sgb1-tests-s145.l4` | 339 | 130 | 8 | tests for the layer-1 module of the same section |
| `sgb1-tests-s148.l4` | 269 | 97 | 10 | tests for the layer-1 module of the same section |
| `sgb1-tests-s149b.l4` | 170 | 71 | 3 | tests for the layer-1 module of the same section |
| `sgb1-tests-s154.l4` | 245 | 97 | 6 | tests for the layer-1 module of the same section |
| `sgb1-tests-s155b.l4` | 214 | 98 | 4 | tests for the layer-1 module of the same section |
| `sgb1-tests-s156.l4` | 219 | 72 | 10 | tests for the layer-1 module of the same section |
| `sgb1-tests-s157.l4` | 224 | 86 | 6 | tests for the layer-1 module of the same section |
| `sgb1-seat.l4` | 1563 | 0 | 0 | layer 2: the seat, 197 questions, each calling one layer-1 function |
| `sgb1-cases-seat.l4` | 752 | 427 | 0 | cases that ask the seat questions (not the layer-1 functions behind them) |
| `NOTES.md`, `PROGRESS.md` | | | | this file; the progress file |

`NEEDS-CORE.md` is not written: no type or constructor was missing from the keel.

## The rulings this encoding follows, word for word

Copied by script from `inputs/ENCODING-GUIDE.md` section 5 ("Rulings on negatives and legal effects (ruled 2026-11-04)"), with the line of that file in front of each; each paragraph also occurs in `BRIEF.md`.
They govern what they cover; every `NOTHING-kind` tag in the layer-1 modules rests on the "In short" paragraph or on one of the rulings below it.

Guide line 86:

> In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").

Guide line 87:

> Everywhere else it answers `NOTHING`: where the text lists without closing the list, says "includes", leaves a term undefined, is silent, points outside the sources, or limits a grant or prohibition in its own wording and the case falls outside the limit.

Guide line 91:

> - **E1** (bench `commons-negation-1030`; should a legal effect be one definition gathered from every section that gives it?): option B, as guidance for gathering a legal effect's routes by hand only, with no pilot run; option A (gathering by bare name) is withdrawn as a direction for the language, not deferred; option C (per-section answers) applies everywhere else; the Magna Carta pilot in the printed recommendation (chapters 2, 3, 4, 5, 37, 43, 46 and 53, with a blind second reader) is not to be run. The maintainer's lean, verbatim: "B but generally uncomfortable with this much magic because it takes the language from unopinionated to opinionated in ways that are hard to teach an l4 novice." the maintainer's note, verbatim: "Fundamentally I feel like we are trying to make the language do work that the human l4 drafter should do. Too much magic. Can’t we just decline to be this opinionated and say the programmer needs to do this thinking?" Marked 2026-11-03T23:19:02.812Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23

Guide line 92:

> - **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. The maintainer's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." the maintainer's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23

Guide line 93:

> - **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. The maintainer's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.

Guide line 94:

> - **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. The maintainer approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

Guide line 95:

> - **Questions with no convention: decide case by case (the maintainer, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. The maintainer's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with the coordinator where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

Guide line 96:

> - **Functions named for a grant or a power (ruled by the coordinating session of the UK and Canada encodings on 2026-11-12; not confirmed by the maintainer).** A function named for a grant or a power ("the court may ...", "the registrar may ...") that answers `JUST FALSE` because an `if` gate failed reads as "may not": a grant turned into a bar. The ruling sets three limits:

> 1. answer `NOTHING`, with one fork line each, only for a function named for a grant or a power ("may", "is permitted to", "has power to") whose `if` gate failed;

> 2. keep `JUST FALSE` where the text closes the gate itself ("only if", "only where", "may not ... unless", a list closed with "only"), and for a bar, a duty or the provision's own question;

> 3. do not change, but list in the row's fork register for the maintainer or a lawyer, a "may" function whose gate is "where", "when" or "upon" (ruling (b) of the periods ruling above says `JUST FALSE`, and the "In short" line on grants points the other way), and an "entitled"-named function (an entitlement is a claim, not a power, and this guide does not settle it).

The two sentences that follow the grant ruling in the Guide (line 100, "The ruling and the counts it produced ...") are a pointer to another encoding's NOTES.md and are not rules.

## Coverage (sgb1)

One row per unit of the text of my range: every heading, section, subsection, paragraph, sub-paragraph, sub-sub-paragraph and defined term, in the order of the text.
The rows are made from the text by script (`work/covgen.py`, not shipped), which reads the labels `(a)`, `(i)`, `(A)`, the section numbers and the quoted defined terms and takes page furniture (the "Informal Consolidation" line, the page-number line, a bare amendment mark such as `[36/2014]`) as belonging to the unit it sits in.
Each row has exactly one disposition: `encoded`, `fork`, `inert` (with its reason number, 1, 2 or 3) or `repealed or blank in this text`.
There is no `out-of-scope` row and no `deferred` row.
A `fork` row points at its fork-register entries (ids such as `SI-01`) and names the function that encodes the reading taken; the fork lines are in "Fork register (sgb1)".
The `@ref` locators of every layer-1 rule were checked against the raw text with `srcrefs.py check --refs` and `--strict` (0 problems; the numbers are under "Tests, traces and the checks I ran").

### Counts

| disposition | rows |
| --- | --- |
| encoded | 207 |
| fork | 75 |
| inert | 29 |
| repealed or blank in this text | 8 |
| total | 319 |

Inert rows: 27 are reason 1 (not operative: headings) and 2 are reason 2 (machinery: the two transitional savings, s 149(15) and s 154(9)).
No row is inert for reason 3: the seven rows the text shows repealed or deleted are their own disposition, `repealed or blank in this text`.
The brief names three reasons for `inert`, the third being "text shown repealed or blank"; I gave those rows the separate disposition the brief also lists, so that no row has two.

### Audit counts

- Units counted by script in lines 11592-13354: 319 (27 headings, 9 whole sections, 149 subsections, 108 paragraphs, 16 sub-paragraphs, 2 sub-sub-paragraphs, 8 defined terms).
- Rows in the table: 319. Units without a row: 0. Rows without a disposition: 0.
- Non-blank lines in the range (page furniture and bare amendment marks left out): 1079. Non-blank lines in no row: 0.
- Non-blank lines quoted by a `-- src:` line in a layer-1 module: 1029; not quoted: 50, of which 33 are heading lines, 17 are the lines of the inert and repealed rows (s 145(3), s 149(15), s 153, s 154(9), s 155A(5), s 160A, s 160B, s 160C, s 160D), which have no rule to cite, and 0 lie in a row that is `encoded` or `fork`.
- The table is generated from the text and is not edited by hand, so "rows before" and "rows after" an audit are the same number; what an audit changes is what the rows point at.
  Three functions were added after an audit of which text the quote runs covered: `s 149(5) the person's conduct as a director of the company includes ...`, `s 150(5) nothing in section 150 applies ...` and `s 155A(3A) an application under subsection (3)(b) cannot be made`, each with tests; the audit was then run again.

### Inert, repealed and blank rows

- s 145(3) (lines 11607-11607): repealed or blank in this text; the text shows "[Deleted by Act 12 of 2002]".
- s 145(6)(c) (lines 11677-11677): repealed or blank in this text; the text shows "[Deleted by Act 24 of 2025 wef 06/05/2026]".
- s 149(15) (lines 12182-12186): inert; reason 2 (machinery: a transitional saving): "Any right to apply for permission ... that was subsisting immediately before 23 March 1990 is, after that date, to be treated as subsisting"; it affects no one now.
- s 153 (lines 12388-12388): repealed or blank in this text; the text shows "[Repealed by Act 36 of 2014]".
- s 154(9) (lines 12521-12525): inert; reason 2 (machinery: a transitional saving): "Any right to apply for permission ... subsisting immediately before 12 November 1993 is on or after that date to be treated as subsisting"; it affects no one now.
- s 155A(5) (lines 12699-12699): repealed or blank in this text; the text shows "[Deleted by Act 17 of 2023 wef 01/07/2023]".
- s 160A (lines 13347-13347): repealed or blank in this text; the text shows "[Repealed by Act 38 of 1998]".
- s 160B (lines 13349-13349): repealed or blank in this text; the text shows "[Repealed by Act 38 of 1998]".
- s 160C (lines 13351-13351): repealed or blank in this text; the text shows "[Repealed by Act 38 of 1998]".
- s 160D (lines 13353-13353): repealed or blank in this text; the text shows "[Repealed by Act 38 of 1998]".
- The 27 heading rows (lines 11592-11592, 11594-11594, 11724-11724, 11774-11774, 11891-11891, 11923-11923, 11966-11966, 12190-12191, 12236-12236, 12243-12243, 12276-12276, 12284-12284, 12390-12391, 12529-12530, 12612-12613, 12701-12701, 12816-12816, 12861-12861, 12906-12906, 12936-12936, 13170-13170, 13214-13214, 13227-13227, 13239-13239, 13269-13269, 13303-13304, 13317-13318): inert, reason 1.

### The table

| unit | lines | disposition | L4 name, or what the text shows | tests; seat |
| --- | --- | --- | --- | --- |
| heading, line 11592 | 11592-11592 | inert | reason 1 (not operative): a heading |  |
| heading, line 11594 | 11594-11594 | inert | reason 1 (not operative): a heading |  |
| s 145(1) | 11596-11599 | fork | fork SII-01; encoded as `s 145(1) the company has a director who is ordinarily resident in Sing...`; `s 145(1) the sole director may also be the sole member of the company` | sgb1-tests-s145.l4; seat |
| s 145(2) | 11601-11603 | fork | fork F-145-1; encoded as `s 145(2) the subsection bars the person from being a director of a com...` | sgb1-tests-s145.l4; seat |
| s 145(3) | 11607-11607 | repealed or blank in this text | the text shows "[Deleted by Act 12 of 2002]" |  |
| s 145(4) | 11609-11617 | encoded | `s 145(4) the provision is read as authorising the corporation to appoi...` | sgb1-tests-s145.l4; seat |
| s 145(4A) | 11621-11623 | fork | fork GO-01; encoded as `s 145(4A) the director may resign by giving the company a written noti...` | sgb1-tests-s145.l4; seat |
| s 145(4B) | 11627-11628 | encoded | `s 145(4B) the resignation is conditional upon the company's acceptance...` | sgb1-tests-s145.l4; seat |
| s 145(5) | 11632-11637 | encoded | `s 145(5) the subsection bars the director from resigning or vacating o...`; `s 145(5) the purported resignation or vacation of office is invalid`; `s 145(5) a director must not resign or vacate office leaving no direct...` | sgb1-tests-s145.l4; seat |
| s 145(6) | 11641-11642 | encoded | `s 145(6) subsection (5) does not apply to the director's resignation o...` | sgb1-tests-s145.l4; seat |
| s 145(6)(a) | 11644-11645 | encoded | `s 145(6) subsection (5) does not apply to the director's resignation o...` | sgb1-tests-s145.l4; seat |
| s 145(6)(b) | 11649-11671 | encoded | `s 145(6) subsection (5) does not apply to the director's resignation o...` | sgb1-tests-s145.l4; seat |
| s 145(6)(c) | 11677-11677 | repealed or blank in this text | the text shows "[Deleted by Act 24 of 2025 wef 06/05/2026]" |  |
| s 145(7) | 11681-11685 | fork | fork GI-01; encoded as `s 145(7) the Registrar may direct the members of the company to appoin...` | sgb1-tests-s145.l4; seat |
| s 145(8) | 11687-11692 | fork | fork SI-01; encoded as `s 145(8) the member is guilty of the offence this subsection creates`; `s 145(8) the most the member may be penalised on conviction` | sgb1-tests-s145.l4; seat |
| s 145(9) | 11694-11694 | fork | fork GI-02; encoded as `s 145(9) the Court may order the members of the company to make the ap...` | sgb1-tests-s145.l4; seat |
| s 145(9)(a) | 11696-11697 | encoded | `s 145(9) the Court may order the members of the company to make the ap...` | sgb1-tests-s145.l4; seat |
| s 145(9)(b) | 11699-11704 | encoded | `s 145(9) the Court may order the members of the company to make the ap...` | sgb1-tests-s145.l4; seat |
| s 145(10) | 11708-11711 | fork | fork SI-02, SI-03; encoded as `s 145(10) the member is liable for the payment of the debts of the com...` | sgb1-tests-s145.l4; seat |
| s 145(10)(a) | 11713-11713 | encoded | `s 145(10) the member is liable for the payment of the debts of the com...` | sgb1-tests-s145.l4; seat |
| s 145(10)(b) | 11715-11722 | encoded | `s 145(10) the member is liable for the payment of the debts of the com...`; `s 145(10) the debt is within the liability of the member` | sgb1-tests-s145.l4; seat |
| heading, line 11724 | 11724-11724 | inert | reason 1 (not operative): a heading |  |
| s 145A(1) | 11726-11728 | encoded | `s 145A(1) the subsection bars the person from acting as a nominee dire...`; `s 145A(1) a person must not act as a nominee director by way of busine...` | sgb1-tests-s145.l4; seat |
| s 145A(1)(a) | 11730-11732 | encoded | `s 145A(1) the subsection bars the person from acting as a nominee dire...`; `s 145A(1) a person must not act as a nominee director by way of busine...` | sgb1-tests-s145.l4; seat |
| s 145A(1)(b) | 11734-11735 | encoded | `s 145A(1) the subsection bars the person from acting as a nominee dire...`; `s 145A(1) a person must not act as a nominee director by way of busine...` | sgb1-tests-s145.l4; seat |
| s 145A(2) | 11737-11737 | encoded | `s 145A(1) the subsection bars the person from acting as a nominee dire...` | sgb1-tests-s145.l4; seat |
| s 145A(2)(a) | 11739-11740 | encoded | `s 145A(1) the subsection bars the person from acting as a nominee dire...` | sgb1-tests-s145.l4; seat |
| s 145A(2)(b) | 11742-11743 | encoded | `s 145A(1) the subsection bars the person from acting as a nominee dire...` | sgb1-tests-s145.l4; seat |
| s 145A(3) | 11745-11749 | fork | fork SI-04; encoded as `s 145A(3) the person is guilty of the offence this subsection creates`; `s 145A(3) the most the person may be fined on conviction` | sgb1-tests-s145.l4; seat |
| s 145A(4) | 11751-11751 | encoded | `s 145A(4) "affiliated company" the company is an affiliated company of...` | sgb1-tests-s145.l4; seat |
| s 145A(4) "affiliated company" | 11753-11753 | encoded | `s 145A(4) "affiliated company" the company is an affiliated company of...` | sgb1-tests-s145.l4; seat |
| s 145A(4)(a) | 11755-11755 | encoded | `s 145A(4) "affiliated company" the company is an affiliated company of...` | sgb1-tests-s145.l4; seat |
| s 145A(4)(b) | 11757-11758 | encoded | `s 145A(4) "affiliated company" the company is an affiliated company of...` | sgb1-tests-s145.l4; seat |
| s 145A(4) "appointed day" | 11760-11761 | encoded | `s 145A(4) "appointed day" the date asked is on or after the appointed ...` | sgb1-tests-s145.l4; seat |
| s 145A(4) "nominee director" | 11763-11770 | encoded | `s 145A(4) "nominee director" the person is a nominee director` | sgb1-tests-s145.l4; seat |
| heading, line 11774 | 11774-11774 | inert | reason 1 (not operative): a heading |  |
| s 146(1) | 11776-11777 | encoded | `s 146(1) the subsection bars the person from being named as a director...` | sgb1-tests-s145.l4; seat |
| s 146(1)(a) | 11779-11781 | encoded | `s 146(1) the subsection bars the person from being named as a director...` | sgb1-tests-s145.l4; seat |
| s 146(1)(b) | 11783-11786 | encoded | `s 146(1) the subsection bars the person from being named as a director...` | sgb1-tests-s145.l4; seat |
| s 146(1)(c) | 11788-11788 | encoded | `s 146(1) the subsection bars the person from being named as a director...` | sgb1-tests-s145.l4; seat |
| s 146(1)(d) | 11790-11795 | encoded | `s 146(1) the subsection bars the person from being named as a director...` | sgb1-tests-s145.l4; seat |
| s 146(1A) | 11799-11800 | encoded | `s 146(1A)(a) the person has made the filings paragraph (a) requires` | sgb1-tests-s145.l4; seat |
| s 146(1A)(a) | 11802-11804 | encoded | `s 146(1A)(a) the person has made the filings paragraph (a) requires` | sgb1-tests-s145.l4; seat |
| s 146(1A)(i) | 11806-11807 | encoded | `s 146(1A)(a) the person has made the filings paragraph (a) requires` | sgb1-tests-s145.l4; seat |
| s 146(1A)(i)(ii) | 11809-11811 | encoded | `s 146(1A)(a) the person has made the filings paragraph (a) requires` | sgb1-tests-s145.l4; seat |
| s 146(1A)(i)(iii) | 11813-11815 | encoded | `s 146(1A)(a) the person has made the filings paragraph (a) requires` | sgb1-tests-s145.l4; seat |
| s 146(1A)(b) | 11820-11821 | encoded | `s 146(1A)(b) the person has made the filing paragraph (b) requires` | sgb1-tests-s145.l4; seat |
| s 146(1A)(i) | 11823-11825 | encoded | `s 146(1A)(b) the person has made the filing paragraph (b) requires` | sgb1-tests-s145.l4; seat |
| s 146(1A)(i)(ii) | 11827-11829 | encoded | `s 146(1A)(b) the person has made the filing paragraph (b) requires` | sgb1-tests-s145.l4; seat |
| s 146(1A)(i)(iii) | 11831-11834 | encoded | `s 146(1A)(b) the person has made the filing paragraph (b) requires` | sgb1-tests-s145.l4; seat |
| s 146(1A)(i)(iv) | 11836-11841 | encoded | `s 146(1A)(b) the person has made the filing paragraph (b) requires` | sgb1-tests-s145.l4; seat |
| s 146(1A)(i)(iv)(A) | 11843-11845 | encoded | `s 146(1A)(b) the person has made the filing paragraph (b) requires` | sgb1-tests-s145.l4; seat |
| s 146(1A)(i)(iv)(B) | 11847-11851 | encoded | `s 146(1A)(b) the person has made the filing paragraph (b) requires` | sgb1-tests-s145.l4; seat |
| s 146(2) | 11855-11858 | encoded | `s 146(2) the person is, as regards those shares, in the same position ...` | sgb1-tests-s145.l4; seat |
| s 146(3) | 11862-11863 | fork | fork F-146-1; encoded as `s 146(3) the requirements of subsections (1) and (2), other than the p...` | sgb1-tests-s145.l4; seat |
| s 146(3)(a) | 11865-11865 | encoded | `s 146(3) the requirements of subsections (1) and (2), other than the p...` | sgb1-tests-s145.l4; seat |
| s 146(3)(b) | 11870-11870 | encoded | `s 146(3) the requirements of subsections (1) and (2), other than the p...` | sgb1-tests-s145.l4; seat |
| s 146(3)(c) | 11872-11876 | fork | fork F-146-2; encoded as `s 146(3)(c) the document is outside subsections (1) and (2) by reason ...`; `s 146(3) the requirements of subsections (1) and (2), other than the p...` | sgb1-tests-s145.l4; seat |
| s 146(4) | 11880-11883 | fork | fork SI-05; encoded as `s 146(4) the person is guilty of the offence this subsection creates`; `s 146(4) the most the person may be penalised on conviction` | sgb1-tests-s145.l4; seat |
| s 146(5) | 11885-11889 | encoded | `s 146(5) the restrictions apply to a director or proposed director of ...` | sgb1-tests-s145.l4; seat |
| heading, line 11891 | 11891-11891 | inert | reason 1 (not operative): a heading |  |
| s 147(1) | 11893-11897 | encoded | `s 147(1) the last day on which the director must have obtained the qua...`; `s 147(1) the director has obtained the qualification in time`; `s 147(1) a director must obtain the qualification in time` | sgb1-tests-s145.l4; seat |
| s 147(2) | 11901-11903 | encoded | `s 147(2) the way the qualification is held meets the subsection` | sgb1-tests-s145.l4; seat |
| s 147(3) | 11907-11910 | fork | fork MA-01; encoded as `s 147(3) the director must vacate office` | sgb1-tests-s145.l4; seat |
| s 147(4) | 11912-11914 | fork | fork SI-06; encoded as `s 147(4) the person is guilty of the offence this subsection creates`; `s 147(4) the most the person may be penalised on conviction` | sgb1-tests-s145.l4; seat |
| s 147(5) | 11919-11921 | encoded | `s 147(5) the person cannot yet be re-appointed as director` | sgb1-tests-s145.l4; seat |
| heading, line 11923 | 11923-11923 | inert | reason 1 (not operative): a heading |  |
| s 148(1) | 11925-11933 | fork | fork SI-07; encoded as `s 148(1) the person is guilty of the offence this subsection creates`; `s 148(1) the most the person may be penalised on conviction`; `s 148(1) an undischarged bankrupt must not act as director without per...` | sgb1-tests-s148.l4; seat |
| s 148(2) | 11939-11943 | fork | fork SII-02; encoded as `s 148(2) the Court or the Official Assignee may refuse the application...` | sgb1-tests-s148.l4; seat |
| s 148(3) | 11945-11949 | encoded | `s 148(3) the subsection bars the Court from giving permission` | sgb1-tests-s148.l4; seat |
| s 148(4) | 11953-11957 | encoded | `s 148(4) the last day for lodging the copy of the order or written per...`; `s 148(4) the person has lodged the copy within the time the subsection...`; `s 148(4) a person granted permission must lodge a copy within 14 days` | sgb1-tests-s148.l4; seat |
| heading, line 11966 | 11966-11966 | inert | reason 1 (not operative): a heading |  |
| s 149(1) | 11968-11968 | fork | fork SII-03; encoded as `s 149(1) the Court may make an order disqualifying the person` | sgb1-tests-s148.l4; seat |
| s 149(1)(a) | 11970-11971 | encoded | `s 149(1) the Court may make an order disqualifying the person` | sgb1-tests-s148.l4; seat |
| s 149(1)(b) | 11973-11980 | encoded | `s 149(1) the Court may make an order disqualifying the person`; `s 149(1) the period the order specifies is within the limit the subsec...` | sgb1-tests-s148.l4; seat |
| s 149(2) | 11982-11983 | fork | fork MA-02, F-14D; encoded as `s 149(2) the Court must make a disqualification order against the pers...` | sgb1-tests-s148.l4; seat |
| s 149(2)(a) | 11985-11986 | encoded | `s 149(2) the Court must make a disqualification order against the pers...` | sgb1-tests-s148.l4; seat |
| s 149(2)(b) | 11988-11988 | encoded | `s 149(2)(b)(i) the person is or has been a director of a company that ...`; `s 149(2) the Court must make a disqualification order against the pers...` | sgb1-tests-s148.l4; seat |
| s 149(2)(i) | 11990-11994 | encoded | `s 149(2)(b)(i) the person is or has been a director of a company that ...`; `s 149(2) the Court must make a disqualification order against the pers...` | sgb1-tests-s148.l4; seat |
| s 149(2)(i)(ii) | 11996-12001 | encoded | `s 149(2) the Court must make a disqualification order against the pers...` | sgb1-tests-s148.l4; seat |
| s 149(3) | 12003-12004 | fork | fork MA-03; encoded as `s 149(3) the Official Receiver or the liquidator must immediately repo...` | sgb1-tests-s148.l4; layer 1 only |
| s 149(3)(a) | 12006-12008 | encoded | `s 149(3) the Official Receiver or the liquidator must immediately repo...` | sgb1-tests-s148.l4; layer 1 only |
| s 149(3)(b) | 12013-12018 | encoded | `s 149(3) the Official Receiver or the liquidator must immediately repo...` | sgb1-tests-s148.l4; layer 1 only |
| s 149(4) | 12020-12021 | fork | fork SII-04; encoded as `s 149(4) the Court may order the person to make good the default` | sgb1-tests-s148.l4; layer 1 only |
| s 149(4)(a) | 12023-12024 | encoded | `s 149(4) the Court may order the person to make good the default` | sgb1-tests-s148.l4; layer 1 only |
| s 149(4)(b) | 12026-12035 | encoded | `s 149(4) the Court may order the person to make good the default` | sgb1-tests-s148.l4; layer 1 only |
| s 149(5) | 12037-12037 | encoded | `s 149(5)(a) the date on which the company has gone into liquidation` | sgb1-tests-s148.l4; seat |
| s 149(5)(a) | 12039-12039 | encoded | `s 149(5)(a) the date on which the company has gone into liquidation` | sgb1-tests-s148.l4; seat |
| s 149(5)(i) | 12041-12042 | encoded | `s 149(5)(a) the date on which the company has gone into liquidation` | sgb1-tests-s148.l4; seat |
| s 149(5)(i)(ii) | 12044-12048 | encoded | `s 149(5)(a) the date on which the company has gone into liquidation` | sgb1-tests-s148.l4; seat |
| s 149(5)(i)(iii) | 12050-12051 | encoded | `s 149(5)(a) the date on which the company has gone into liquidation` | sgb1-tests-s148.l4; seat |
| s 149(5)(b) | 12053-12065 | encoded | `s 149(5)(b) the company was insolvent at the time it went into liquida...`; `s 149(5) the person's conduct as a director of the company includes th...` | sgb1-tests-s148.l4; seat |
| s 149(6) | 12069-12077 | encoded | `s 149(6) the Court must have regard to the matter`; `s 149(6) the matter counts although the director has not been convicte...` | sgb1-tests-s148.l4; seat |
| s 149(6)(a) | 12079-12079 | encoded | `s 149(6) the Court must have regard to the matter` | sgb1-tests-s148.l4; seat |
| s 149(6)(i) | 12081-12083 | encoded | `s 149(6) the Court must have regard to the matter` | sgb1-tests-s148.l4; seat |
| s 149(6)(i)(ii) | 12085-12088 | encoded | `s 149(6) the Court must have regard to the matter` | sgb1-tests-s148.l4; seat |
| s 149(6)(i)(iii) | 12090-12092 | encoded | `s 149(6) the Court must have regard to the matter` | sgb1-tests-s148.l4; seat |
| s 149(6)(b) | 12094-12094 | encoded | `s 149(6) the Court must have regard to the matter` | sgb1-tests-s148.l4; seat |
| s 149(6)(i) | 12096-12097 | encoded | `s 149(6) the Court must have regard to the matter` | sgb1-tests-s148.l4; seat |
| s 149(6)(i)(ii) | 12099-12102 | encoded | `s 149(6) the Court must have regard to the matter` | sgb1-tests-s148.l4; seat |
| s 149(6)(i)(iii) | 12104-12111 | encoded | `s 149(6) the Court must have regard to the matter` | sgb1-tests-s148.l4; seat |
| s 149(6)(i)(iv) | 12113-12116 | encoded | `s 149(6) the Court must have regard to the matter` | sgb1-tests-s148.l4; seat |
| s 149(7) | 12120-12123 | fork | fork GO-02; encoded as `s 149(7) the Minister may add to, vary or amend the matters referred t...` | sgb1-tests-s148.l4; seat |
| s 149(8) | 12125-12128 | encoded | `s 149(8) the body is a company for the purposes of the section` | sgb1-tests-s148.l4; seat |
| s 149(9) | 12132-12136 | encoded | `s 149(9) who makes the application under the section` | sgb1-tests-s148.l4; seat |
| s 149(9A) | 12138-12138 | encoded | `s 149(9A)(a) the Minister or the Official Receiver must appear and cal...` | sgb1-tests-s148.l4; layer 1 only |
| s 149(9A)(a) | 12140-12144 | fork | fork CB-01; encoded as `s 149(9A)(a) the Minister or the Official Receiver must appear and cal...` | sgb1-tests-s148.l4; layer 1 only |
| s 149(9A)(b) | 12146-12147 | fork | fork SII-05; encoded as `s 149(9A)(a) the Minister or the Official Receiver must appear and cal...`; `s 149(9A)(b) the person against whom an order is sought may appear and...` | sgb1-tests-s148.l4; seat |
| s 149(10) | 12149-12153 | encoded | `s 149(10) the section applies to the company's liquidation`; `s 149(10) the conduct as a director of the company is conduct to which...` | sgb1-tests-s148.l4; seat |
| s 149(11) | 12158-12161 | encoded | `s 149(11) the person is liable to have a disqualification order made a...` | sgb1-tests-s148.l4; seat |
| s 149(12) | 12163-12166 | fork | fork SI-08; encoded as `s 149(12) the person is guilty of the offence this subsection creates`; `s 149(12) the most the person may be penalised on conviction`; `s 149(12) a person disqualified by an order must not act in contravent...` | sgb1-tests-s148.l4; seat |
| s 149(13) | 12168-12171 | encoded | `s 149(13) the person may apply to the Court for permission to be conce...` | sgb1-tests-s148.l4; seat |
| s 149(14) | 12175-12180 | fork | fork CB-02; encoded as `s 149(14) the Minister or the Official Receiver must appear and call t...` | sgb1-tests-s148.l4; layer 1 only |
| s 149(15) | 12182-12186 | inert | reason 2 (machinery: a transitional saving): "Any right to apply for permission ... that was subsisting immediately before 23 March 1990 is, after that date, to be treated as subsisting"; it affects no one now |  |
| heading, line 12190 | 12190-12191 | inert | reason 1 (not operative): a heading |  |
| s 149A(1) | 12193-12206 | fork | fork SII-06; encoded as `s 149A(1) the Court may make an order disqualifying the person`; `s 149A(1) the last day of the disqualification` | sgb1-tests-s148.l4; seat |
| s 149A(2) | 12210-12213 | fork | fork F-14D; encoded as `s 149A(2) the subsection bars the Court from making a disqualification...` | sgb1-tests-s148.l4; seat |
| s 149A(3) | 12215-12217 | encoded | `s 149A(3) the subsection bars the Court from making a disqualification...` | sgb1-tests-s148.l4; seat |
| s 149A(3)(a) | 12219-12221 | encoded | `s 149A(3) the subsection bars the Court from making a disqualification...` | sgb1-tests-s148.l4; seat |
| s 149A(3)(b) | 12223-12226 | encoded | `s 149A(3) the subsection bars the Court from making a disqualification...` | sgb1-tests-s148.l4; seat |
| s 149A(4) | 12228-12231 | fork | fork SI-09; encoded as `s 149A(4) the person is guilty of the offence this subsection creates`; `s 149A(4) the most the person may be penalised on conviction`; `s 149A(4) a person disqualified by an order must not act in contravent...` | sgb1-tests-s148.l4; seat |
| s 149A(5) | 12233-12234 | encoded | `s 149A(5) "foreign company" the body is a foreign company for the purp...` | sgb1-tests-s148.l4; seat |
| heading, line 12236 | 12236-12236 | inert | reason 1 (not operative): a heading |  |
| s 149B | 12238-12239 | fork | fork GO-03; encoded as `s 149B the company may appoint a director by ordinary resolution passe...` | sgb1-tests-s149b.l4; seat |
| heading, line 12243 | 12243-12243 | inert | reason 1 (not operative): a heading |  |
| s 150(1) | 12245-12249 | encoded | `s 150(1) the section bars the motion for the appointment of 2 or more ...` | sgb1-tests-s149b.l4; seat |
| s 150(2) | 12254-12256 | encoded | `s 150(2) the resolution passed pursuant to the motion is void` | sgb1-tests-s149b.l4; seat |
| s 150(3) | 12258-12261 | encoded | `s 150(3) a provision for the automatic re-appointment of retiring dire...` | sgb1-tests-s149b.l4; seat |
| s 150(4) | 12263-12265 | encoded | `s 150(4) the motion is treated as a motion for the person's appointmen...` | sgb1-tests-s149b.l4; seat |
| s 150(5) | 12267-12267 | encoded | `s 150(5) nothing in section 150 applies to the resolution or prevents ...` | sgb1-tests-s149b.l4; seat |
| s 150(5)(a) | 12269-12269 | encoded | `s 150(5) nothing in section 150 applies to the resolution or prevents ...` | sgb1-tests-s149b.l4; seat |
| s 150(5)(b) | 12271-12272 | encoded | `s 150(5) nothing in section 150 applies to the resolution or prevents ...` | sgb1-tests-s149b.l4; seat |
| heading, line 12276 | 12276-12276 | inert | reason 1 (not operative): a heading |  |
| s 151 | 12278-12280 | encoded | `s 151 the act is valid despite a defect in the appointment or qualific...` | sgb1-tests-s149b.l4; seat |
| heading, line 12284 | 12284-12284 | inert | reason 1 (not operative): a heading |  |
| s 152(1) | 12286-12292 | fork | fork GO-04; encoded as `s 152(1) the public company may remove the director by ordinary resolu...`; `s 152(1) the resolution to remove the director cannot yet take effect` | sgb1-tests-s149b.l4; seat |
| s 152(2) | 12296-12307 | fork | fork EN-01, CB-03; encoded as `s 152(2) special notice is required of the resolution`; `s 152(2) the company must immediately send a copy of the notice to the...`; `s 152(2) the director is entitled to be heard on the resolution at the...` (+1 more) | sgb1-tests-s149b.l4; seat |
| s 152(3) | 12311-12315 | fork | fork GI-03, CB-04; encoded as `s 152(3) the company must notify the members of the representations` | sgb1-tests-s149b.l4; seat |
| s 152(3)(a) | 12317-12319 | encoded | `s 152(3) the company must notify the members of the representations` | sgb1-tests-s149b.l4; seat |
| s 152(3)(b) | 12321-12329 | encoded | `s 152(3) the company must notify the members of the representations`; `s 152(3) the director may require that the representations be read out...` | sgb1-tests-s149b.l4; seat |
| s 152(4) | 12333-12341 | fork | fork GI-04, MA-04; encoded as `s 152(4) copies of the representations need not be sent out and the re...`; `s 152(4) the Court may order the company's costs to be paid in whole o...` | sgb1-tests-s149b.l4; seat |
| s 152(5) | 12345-12347 | fork | fork GI-05; encoded as `s 152(5) the vacancy may be filled as a casual vacancy` | sgb1-tests-s149b.l4; seat |
| s 152(6) | 12351-12360 | encoded | `s 152(6) the day on which the replacement is treated as having become ...` | sgb1-tests-s149b.l4; seat |
| s 152(7) | 12364-12370 | encoded | `s 152(7) the removal deprives the person of compensation or damages pa...`; `s 152(7) the section derogates from a power to remove a director which...` | sgb1-tests-s149b.l4; seat |
| s 152(8) | 12374-12377 | encoded | `s 152(8) the subsection bars the directors from removing a director of...` | sgb1-tests-s149b.l4; seat |
| s 152(9) | 12381-12384 | fork | fork GO-05; encoded as `s 152(9) the private company may remove the director by ordinary resol...` | sgb1-tests-s149b.l4; seat |
| s 153 | 12388-12388 | repealed or blank in this text | the text shows "[Repealed by Act 36 of 2014]" |  |
| heading, line 12390 | 12390-12391 | inert | reason 1 (not operative): a heading |  |
| s 154(1) | 12393-12394 | fork | fork MA-05; encoded as `s 154(1) the person is subject to the disqualifications provided in su...` | sgb1-tests-s154.l4; seat |
| s 154(1)(a) | 12396-12396 | encoded | `s 154(1) the person is subject to the disqualifications provided in su...` | sgb1-tests-s154.l4; seat |
| s 154(1)(i) | 12398-12400 | encoded | `s 154(1) the person is subject to the disqualifications provided in su...` | sgb1-tests-s154.l4; seat |
| s 154(1)(i)(ii) | 12402-12404 | encoded | `s 154(1) the person is subject to the disqualifications provided in su...` | sgb1-tests-s154.l4; seat |
| s 154(1)(i)(iii) | 12411-12416 | encoded | `s 154(1) the person is subject to the disqualifications provided in su...` | sgb1-tests-s154.l4; seat |
| s 154(1)(b) | 12420-12422 | encoded | `s 154(1) the person is subject to the disqualifications provided in su...` | sgb1-tests-s154.l4; seat |
| s 154(2) | 12426-12428 | fork | fork GO-06; encoded as `s 154(2) the court may make a disqualification order against the perso...` | sgb1-tests-s154.l4; seat |
| s 154(2)(a) | 12430-12431 | encoded | `s 154(2) the court may make a disqualification order against the perso...` | sgb1-tests-s154.l4; seat |
| s 154(2)(b) | 12433-12433 | encoded | `s 154(2) the court may make a disqualification order against the perso...` | sgb1-tests-s154.l4; seat |
| s 154(2)(c) | 12435-12436 | encoded | `s 154(2) the court may make a disqualification order against the perso...` | sgb1-tests-s154.l4; seat |
| s 154(3) | 12440-12441 | encoded | `s 154(3) the subsection bars the person from acting as a director or t...`; `s 154(3) a disqualified person must not act as a director or take part...` | sgb1-tests-s154.l4; seat |
| s 154(3)(a) | 12443-12443 | encoded | `s 154(3) the subsection bars the person from acting as a director or t...`; `s 154(3) a disqualified person must not act as a director or take part...` | sgb1-tests-s154.l4; seat |
| s 154(3)(b) | 12445-12451 | encoded | `s 154(3) the subsection bars the person from acting as a director or t...`; `s 154(3) a disqualified person must not act as a director or take part...` | sgb1-tests-s154.l4; seat |
| s 154(4) | 12457-12457 | encoded | `s 154(4) the date the disqualification takes effect`; `s 154(4) the last day of the disqualification`; `s 154(4) the date asked is within the period of the disqualification` | sgb1-tests-s154.l4; seat |
| s 154(4)(a) | 12459-12467 | encoded | `s 154(4) the date the disqualification takes effect`; `s 154(4) the last day of the disqualification`; `s 154(4) the date asked is within the period of the disqualification` | sgb1-tests-s154.l4; seat |
| s 154(4)(b) | 12469-12473 | encoded | `s 154(4) the date the disqualification takes effect`; `s 154(4) the last day of the disqualification`; `s 154(4) the date asked is within the period of the disqualification` | sgb1-tests-s154.l4; seat |
| s 154(4)(c) | 12475-12480 | encoded | `s 154(4) the date the disqualification takes effect`; `s 154(4) the last day of the disqualification`; `s 154(4) the date asked is within the period of the disqualification` | sgb1-tests-s154.l4; seat |
| s 154(5) | 12484-12487 | fork | fork SI-10; encoded as `s 154(5) the person is guilty of the offence this subsection creates`; `s 154(5) the most the person may be penalised on conviction` | sgb1-tests-s154.l4; seat |
| s 154(6) | 12491-12491 | fork | fork SII-07, F-14D; encoded as `s 154(6) the person may apply to the Court for permission to act as a ...` | sgb1-tests-s154.l4; seat |
| s 154(6)(a) | 12493-12493 | encoded | `s 154(6) the person may apply to the Court for permission to act as a ...` | sgb1-tests-s154.l4; seat |
| s 154(6)(b) | 12495-12503 | encoded | `s 154(6) the person may apply to the Court for permission to act as a ...` | sgb1-tests-s154.l4; seat |
| s 154(7) | 12509-12511 | fork | fork SII-08; encoded as `s 154(7) the Minister may be represented at the hearing and may oppose...` | sgb1-tests-s154.l4; seat |
| s 154(8) | 12518-12519 | fork | fork GO-07; encoded as `s 154(8) a District Court may make a disqualification order under the ...` | sgb1-tests-s154.l4; seat |
| s 154(9) | 12521-12525 | inert | reason 2 (machinery: a transitional saving): "Any right to apply for permission ... subsisting immediately before 12 November 1993 is on or after that date to be treated as subsisting"; it affects no one now |  |
| heading, line 12529 | 12529-12530 | inert | reason 1 (not operative): a heading |  |
| s 155(1) | 12532-12541 | fork | fork SI-11; encoded as `s 155(1) the person is guilty of the offence this subsection creates`; `s 155(1) the most the person may be penalised on conviction`; `s 155(1) a person persistently in default must not be a director or ta...` | sgb1-tests-s154.l4; seat |
| s 155(2) | 12545-12548 | encoded | `s 155(2) the provision is a relevant requirement of this Act for the p...` | sgb1-tests-s154.l4; seat |
| s 155(3) | 12550-12556 | fork | fork F-155-1; encoded as `s 155(3) the person's persistent default in relation to relevant requi...` | sgb1-tests-s154.l4; seat |
| s 155(4) | 12558-12567 | fork | fork MA-06; encoded as `s 155(4) the person is treated as being adjudged guilty of 3 or more o...` | sgb1-tests-s154.l4; seat |
| s 155(5) | 12569-12571 | encoded | `s 155(5) the conviction is treated as an offence in relation to a rele...` | sgb1-tests-s154.l4; seat |
| s 155(6) | 12573-12581 | encoded | `s 155(6) the section prevents the person from complying with the order...` | sgb1-tests-s154.l4; seat |
| s 155(7) | 12583-12587 | encoded | `s 155(7) the certificate of the Registrar is received in all courts as...` | sgb1-tests-s154.l4; seat |
| s 155(8) | 12589-12591 | encoded | `s 155(8) account is taken of the offence for the purposes of the secti...` | sgb1-tests-s154.l4; seat |
| s 155(9) | 12593-12595 | fork | fork F-14D; encoded as `s 155(9) the person has given the Minister the notice the subsection r...` | sgb1-tests-s154.l4; seat |
| s 155(10) | 12599-12601 | fork | fork SII-09; encoded as `s 155(10) the Minister may be represented and may oppose the granting ...` | sgb1-tests-s154.l4; seat |
| s 155(11) | 12603-12605 | encoded | `s 155(11) the body is a company for the purposes of the section` | sgb1-tests-s154.l4; seat |
| heading, line 12612 | 12612-12613 | inert | reason 1 (not operative): a heading |  |
| s 155A(1) | 12615-12615 | encoded | `s 155A(1) the subsection bars the person from acting as a director or ...`; `s 155A(1) a person who was a director of 3 or more companies struck of...` | sgb1-tests-s154.l4; seat |
| s 155A(1)(a) | 12617-12619 | encoded | `s 155A(1) the subsection bars the person from acting as a director or ...`; `s 155A(1) a person who was a director of 3 or more companies struck of...` | sgb1-tests-s154.l4; seat |
| s 155A(1)(b) | 12621-12629 | encoded | `s 155A(1) the subsection bars the person from acting as a director or ...`; `s 155A(1) a person who was a director of 3 or more companies struck of...` | sgb1-tests-s154.l4; seat |
| s 155A(1A) | 12633-12633 | encoded | `s 155A(1A) the last day of the period of the disqualification` | sgb1-tests-s154.l4; seat |
| s 155A(1A)(a) | 12635-12644 | encoded | `s 155A(1A) the last day of the period of the disqualification` | sgb1-tests-s154.l4; seat |
| s 155A(1A)(b) | 12646-12648 | encoded | `s 155A(1A) the last day of the period of the disqualification` | sgb1-tests-s154.l4; seat |
| s 155A(2) | 12652-12655 | fork | fork SI-12; encoded as `s 155A(2) the person is guilty of the offence this subsection creates`; `s 155A(2) the most the person may be penalised on conviction` | sgb1-tests-s154.l4; seat |
| s 155A(3) | 12662-12666 | fork | fork SII-10, F-14D; encoded as `s 155A(3) the person may apply for permission to act as a director or ...` | sgb1-tests-s154.l4; seat |
| s 155A(3)(a) | 12668-12668 | encoded | `s 155A(3) the person may apply for permission to act as a director or ...` | sgb1-tests-s154.l4; seat |
| s 155A(3)(b) | 12670-12672 | encoded | `s 155A(3) the person may apply for permission to act as a director or ...` | sgb1-tests-s154.l4; seat |
| s 155A(3A) | 12676-12678 | encoded | `s 155A(3A) an application under subsection (3)(b) cannot be made` | sgb1-tests-s154.l4; seat |
| s 155A(3B) | 12682-12684 | fork | fork GI-06; encoded as `s 155A(3B) the Registrar may grant the application under subsection (3...` | sgb1-tests-s154.l4; seat |
| s 155A(3C) | 12688-12689 | fork | fork GI-07; encoded as `s 155A(3C) the Court may grant the application under subsection (3)(b)` | sgb1-tests-s154.l4; seat |
| s 155A(4) | 12693-12695 | fork | fork SII-11; encoded as `s 155A(4) the Minister may be represented at the hearing and may oppos...` | sgb1-tests-s154.l4; seat |
| s 155A(5) | 12699-12699 | repealed or blank in this text | the text shows "[Deleted by Act 17 of 2023 wef 01/07/2023]" |  |
| heading, line 12701 | 12701-12701 | inert | reason 1 (not operative): a heading |  |
| s 155B(1) | 12703-12706 | fork | fork SII-12; encoded as `s 155B(1) the Registrar may make a debarment order against the person` | sgb1-tests-s155b.l4; seat |
| s 155B(2) | 12710-12711 | encoded | `s 155B(2) the subsection bars the person from acting as director or se...`; `s 155B(2)(a) a person with a debarment order must not act as director ...` | sgb1-tests-s155b.l4; seat |
| s 155B(2)(a) | 12716-12718 | encoded | `s 155B(2) the subsection bars the person from acting as director or se...`; `s 155B(2)(a) a person with a debarment order must not act as director ...` | sgb1-tests-s155b.l4; seat |
| s 155B(2)(b) | 12720-12722 | encoded | `s 155B(2) the subsection bars the person from acting as director or se...`; `s 155B(2)(a) a person with a debarment order must not act as director ...`; `s 155B(2)(b) a person with a debarment order must not act as secretary...` | sgb1-tests-s155b.l4; seat |
| s 155B(3) | 12726-12728 | encoded | `s 155B(3) the debarment order is in force` | sgb1-tests-s155b.l4; seat |
| s 155B(4) | 12732-12738 | fork | fork SII-13; encoded as `s 155B(4) the Registrar may cancel or suspend the debarment order` | sgb1-tests-s155b.l4; seat |
| s 155B(5) | 12742-12745 | encoded | `s 155B(5) the suspension of the debarment order operates` | sgb1-tests-s155b.l4; seat |
| s 155B(6) | 12749-12750 | fork | fork F-14D; encoded as `s 155B(6) the subsection bars the Registrar from making a debarment or...` | sgb1-tests-s155b.l4; seat |
| s 155B(6)(a) | 12752-12755 | encoded | `s 155B(6) the subsection bars the Registrar from making a debarment or...` | sgb1-tests-s155b.l4; seat |
| s 155B(6)(b) | 12757-12768 | encoded | `s 155B(6) the subsection bars the Registrar from making a debarment or...` | sgb1-tests-s155b.l4; seat |
| s 155B(7) | 12772-12774 | encoded | `s 155B(7) the Registrar must consider the representation in determinin...` | sgb1-tests-s155b.l4; seat |
| s 155B(8) | 12778-12780 | fork | fork GO-08; encoded as `s 155B(8) the person may appeal to the Minister` | sgb1-tests-s155b.l4; seat |
| s 155B(9) | 12784-12785 | encoded | `s 155B(9) the appeal suspends the effect of the debarment order` | sgb1-tests-s155b.l4; seat |
| s 155B(10) | 12789-12792 | fork | fork SI-13; encoded as `s 155B(10) the person is guilty of the offence this subsection creates`; `s 155B(10) the most the person may be penalised on conviction` | sgb1-tests-s155b.l4; seat |
| s 155B(11) | 12796-12799 | fork | fork GO-09; encoded as `s 155B(11) the Registrar may publish the name and particulars of the p...` | sgb1-tests-s155b.l4; seat |
| s 155B(12) | 12803-12803 | encoded | `s 155B(12) "debarment order" the order is a debarment order` | sgb1-tests-s155b.l4; seat |
| s 155B(12) "debarment order" | 12805-12806 | encoded | `s 155B(12) "debarment order" the order is a debarment order` | sgb1-tests-s155b.l4; seat |
| s 155B(12) "relevant requirement of this Act" | 12808-12809 | encoded | `s 155B(12) "debarment order" the order is a debarment order`; `s 155B(12) "relevant requirement of this Act" the requirement is a rel...` | sgb1-tests-s155b.l4; seat |
| s 155B(12) "secretary" | 12811-12812 | encoded | `s 155B(12) "debarment order" the order is a debarment order`; `s 155B(12) "secretary" the person is a secretary of the company` | sgb1-tests-s155b.l4; seat |
| heading, line 12816 | 12816-12816 | inert | reason 1 (not operative): a heading |  |
| s 155C(1) | 12818-12829 | encoded | `s 155C(1) the subsection bars the person from acting as a director or ...` | sgb1-tests-s155b.l4; seat |
| s 155C(2) | 12835-12838 | fork | fork SI-14; encoded as `s 155C(2) the person is guilty of the offence this subsection creates`; `s 155C(2) the most the person may be penalised on conviction` | sgb1-tests-s155b.l4; seat |
| s 155C(3) | 12842-12849 | fork | fork SII-14, F-14D; encoded as `s 155C(3) the person may apply to the Court for permission to act as a...` | sgb1-tests-s155b.l4; seat |
| s 155C(4) | 12855-12857 | fork | fork SII-15; encoded as `s 155C(4) the Minister may be represented at the hearing and may oppos...` | sgb1-tests-s155b.l4; seat |
| heading, line 12861 | 12861-12861 | inert | reason 1 (not operative): a heading |  |
| s 155D(1) | 12863-12874 | encoded | `s 155D(1) the subsection bars the person from acting as a director or ...` | sgb1-tests-s155b.l4; seat |
| s 155D(2) | 12880-12883 | fork | fork SI-15; encoded as `s 155D(2) the person is guilty of the offence this subsection creates`; `s 155D(2) the most the person may be penalised on conviction` | sgb1-tests-s155b.l4; seat |
| s 155D(3) | 12887-12894 | fork | fork SII-16, F-14D; encoded as `s 155D(3) the person may apply to the Court for permission to act as a...` | sgb1-tests-s155b.l4; seat |
| s 155D(4) | 12900-12902 | fork | fork SII-17; encoded as `s 155D(4) the Minister may be represented at the hearing and may oppos...` | sgb1-tests-s155b.l4; seat |
| heading, line 12906 | 12906-12906 | inert | reason 1 (not operative): a heading |  |
| s 155E(1) | 12908-12909 | encoded | `s 155E(1) the subsection bars the person from acting as director or se...` | sgb1-tests-s155b.l4; seat |
| s 155E(1)(a) | 12911-12913 | encoded | `s 155E(1) the subsection bars the person from acting as director or se...` | sgb1-tests-s155b.l4; seat |
| s 155E(1)(b) | 12915-12917 | encoded | `s 155E(1) the subsection bars the person from acting as director or se...` | sgb1-tests-s155b.l4; seat |
| s 155E(2) | 12921-12922 | encoded | `s 155E(2) subsection (1) applies on the date asked` | sgb1-tests-s155b.l4; seat |
| s 155E(3) | 12929-12932 | fork | fork SI-16; encoded as `s 155E(3) the person is guilty of the offence this subsection creates`; `s 155E(3) the most the person may be penalised on conviction` | sgb1-tests-s155b.l4; seat |
| heading, line 12936 | 12936-12936 | inert | reason 1 (not operative): a heading |  |
| s 156(1) | 12938-12942 | encoded | `s 156(1) the director or chief executive officer must declare the natu...`; `s 156(1) a director must declare the nature of the interest` | sgb1-tests-s156.l4; seat |
| s 156(1)(a) | 12944-12945 | encoded | `s 156(1) the director or chief executive officer must declare the natu...`; `s 156(1) the person has made the declaration or sent the written notic...`; `s 156(1) a director must declare the nature of the interest` | sgb1-tests-s156.l4; seat |
| s 156(1)(b) | 12947-12949 | encoded | `s 156(1) the director or chief executive officer must declare the natu...`; `s 156(1) the person has made the declaration or sent the written notic...`; `s 156(1) a director must declare the nature of the interest` | sgb1-tests-s156.l4; seat |
| s 156(2) | 12953-12954 | encoded | `s 156(2) the date after which the notice under subsection (1)(b) must ...` | sgb1-tests-s156.l4; seat |
| s 156(2)(a) | 12956-12958 | encoded | `s 156(2) the date after which the notice under subsection (1)(b) must ...` | sgb1-tests-s156.l4; seat |
| s 156(2)(b) | 12960-12965 | encoded | `s 156(2) the date after which the notice under subsection (1)(b) must ...` | sgb1-tests-s156.l4; seat |
| s 156(3) | 12969-12979 | encoded | `s 156(3) the requirements of subsection (1) do not apply` | sgb1-tests-s156.l4; seat |
| s 156(4) | 12983-12985 | encoded | `s 156(4) the director or chief executive officer is not deemed to be i...` | sgb1-tests-s156.l4; seat |
| s 156(4)(a) | 12987-12990 | encoded | `s 156(4) the director or chief executive officer is not deemed to be i...` | sgb1-tests-s156.l4; seat |
| s 156(4)(b) | 12992-13001 | encoded | `s 156(4) the director or chief executive officer is not deemed to be i...`; `s 156(4) the subsection has effect for the purpose` | sgb1-tests-s156.l4; seat |
| s 156(5) | 13005-13009 | fork | fork MA-07; encoded as `s 156(5) the declaration or written notice is treated as a sufficient ...` | sgb1-tests-s156.l4; seat |
| s 156(5)(a) | 13011-13015 | encoded | `s 156(5) the declaration or written notice is treated as a sufficient ...` | sgb1-tests-s156.l4; seat |
| s 156(5)(b) | 13017-13017 | encoded | `s 156(5) the declaration or written notice is treated as a sufficient ...` | sgb1-tests-s156.l4; seat |
| s 156(5)(i) | 13019-13022 | encoded | `s 156(5) the declaration or written notice is treated as a sufficient ...` | sgb1-tests-s156.l4; seat |
| s 156(5)(i)(ii) | 13027-13031 | encoded | `s 156(5) the declaration or written notice is treated as a sufficient ...` | sgb1-tests-s156.l4; seat |
| s 156(5)(c) | 13033-13035 | encoded | `s 156(5) the declaration or written notice is treated as a sufficient ...` | sgb1-tests-s156.l4; seat |
| s 156(5)(d) | 13037-13040 | encoded | `s 156(5) the declaration or written notice is treated as a sufficient ...` | sgb1-tests-s156.l4; seat |
| s 156(6) | 13046-13050 | encoded | `s 156(6) the director or chief executive officer must declare the conf...` | sgb1-tests-s156.l4; seat |
| s 156(6)(a) | 13052-13053 | encoded | `s 156(6) the director or chief executive officer must declare the conf...`; `s 156(6) the person has made the declaration or sent the written notic...` | sgb1-tests-s156.l4; seat |
| s 156(6)(b) | 13055-13056 | encoded | `s 156(6) the director or chief executive officer must declare the conf...`; `s 156(6) the person has made the declaration or sent the written notic...` | sgb1-tests-s156.l4; seat |
| s 156(7) | 13060-13061 | fork | fork F-156-2; encoded as `s 156(7) the meeting of the directors at which the declaration under s...`; `s 156(7) a director must declare the conflict at the first meeting of ...` | sgb1-tests-s156.l4; layer 1 only |
| s 156(7)(a) | 13063-13064 | encoded | `s 156(7) the meeting of the directors at which the declaration under s...`; `s 156(7) a director must declare the conflict at the first meeting of ...` | sgb1-tests-s156.l4; layer 1 only |
| s 156(7)(b) | 13066-13070 | encoded | `s 156(7) the meeting of the directors at which the declaration under s...`; `s 156(7) a director must declare the conflict at the first meeting of ...` | sgb1-tests-s156.l4; layer 1 only |
| s 156(8) | 13074-13075 | encoded | `s 156(8) the date after which the written notice under subsection (6)(...` | sgb1-tests-s156.l4; seat |
| s 156(8)(a) | 13080-13082 | encoded | `s 156(8) the date after which the written notice under subsection (6)(...` | sgb1-tests-s156.l4; seat |
| s 156(8)(b) | 13084-13088 | encoded | `s 156(8) the date after which the written notice under subsection (6)(...` | sgb1-tests-s156.l4; seat |
| s 156(9) | 13092-13094 | encoded | `s 156(9) the persons to whom the company must send a copy of the notic...` | sgb1-tests-s156.l4; seat |
| s 156(9)(a) | 13096-13097 | encoded | `s 156(9) the persons to whom the company must send a copy of the notic...` | sgb1-tests-s156.l4; seat |
| s 156(9)(b) | 13099-13100 | encoded | `s 156(9) the persons to whom the company must send a copy of the notic...` | sgb1-tests-s156.l4; seat |
| s 156(10) | 13104-13107 | encoded | `s 156(10)(a) the declaration is deemed to form part of the proceedings...`; `s 156(10)(b) section 188 applies as if the declaration had been made a...` | sgb1-tests-s156.l4; seat |
| s 156(10)(a) | 13109-13111 | encoded | `s 156(10)(a) the declaration is deemed to form part of the proceedings...`; `s 156(10)(b) section 188 applies as if the declaration had been made a...` | sgb1-tests-s156.l4; seat |
| s 156(10)(b) | 13113-13114 | encoded | `s 156(10)(b) section 188 applies as if the declaration had been made a...` | sgb1-tests-s156.l4; seat |
| s 156(11) | 13118-13121 | encoded | `s 156(11) the secretary must record the declaration in the minutes of ...`; `s 156(11) the secretary must keep a record of the written resolution`; `s 156(11) the secretary must record every declaration in the minutes` | sgb1-tests-s156.l4; seat |
| s 156(12) | 13125-13133 | fork | fork CB-05; encoded as `s 156(12) the directors must permit the chief executive officer to att...`; `s 156(12) the directors must permit the chief executive officer to att...` | sgb1-tests-s156.l4; seat |
| s 156(13) | 13137-13137 | encoded | `s 156(13) the person is a member of the director's or chief executive ...` | sgb1-tests-s156.l4; seat |
| s 156(13)(a) | 13139-13143 | encoded | `s 156(13) the person is a member of the director's or chief executive ...` | sgb1-tests-s156.l4; seat |
| s 156(13)(b) | 13145-13149 | encoded | `s 156(13) the person is a member of the director's or chief executive ...` | sgb1-tests-s156.l4; seat |
| s 156(14) | 13153-13159 | encoded | `s 156(14) the section derogates from the rule of law or the provision ...` | sgb1-tests-s156.l4; seat |
| s 156(15) | 13163-13166 | fork | fork SI-17, F-156-1; encoded as `s 156(15) the person is guilty of the offence this subsection creates`; `s 156(15) the most the person may be penalised on conviction` | sgb1-tests-s156.l4; seat |
| heading, line 13170 | 13170-13170 | inert | reason 1 (not operative): a heading |  |
| s 157(1) | 13172-13173 | encoded | `s 157(1) the director has complied with the duty to act honestly and u...`; `s 157(1) a director must at all times act honestly and use reasonable ...` | sgb1-tests-s157.l4; seat |
| s 157(2) | 13175-13184 | fork | fork SI-18; encoded as `s 157(2) the officer or agent contravenes the subsection`; `s 157(2) an officer or agent must not make improper use of the positio...` | sgb1-tests-s157.l4; seat |
| s 157(3) | 13188-13189 | fork | fork SI-19; encoded as `s 157(3) the officer or agent commits a breach of a provision of secti...` | sgb1-tests-s157.l4; seat |
| s 157(3)(a) | 13191-13193 | encoded | `s 157(3) the officer or agent commits a breach of a provision of secti...`; `s 157(3)(a) the profit for which the officer or agent is liable to the...`; `s 157(3)(a) the damage for which the officer or agent is liable to the...` | sgb1-tests-s157.l4; seat |
| s 157(3)(b) | 13195-13197 | fork | fork SI-20; encoded as `s 157(3) the officer or agent commits a breach of a provision of secti...`; `s 157(3)(b) the officer or agent is guilty of the offence this paragra...`; `s 157(3)(b) the most the officer or agent may be penalised on convicti...` | sgb1-tests-s157.l4; seat |
| s 157(4) | 13201-13203 | encoded | `s 157(4) section 157 derogates from the other written law or rule of l...` | sgb1-tests-s157.l4; seat |
| s 157(5) | 13205-13205 | encoded | `s 157(5) the person is an officer of the company for the purposes of s...` | sgb1-tests-s157.l4; seat |
| s 157(5) "officer" | 13207-13208 | encoded | `s 157(5) the person is an officer of the company for the purposes of s...` | sgb1-tests-s157.l4; seat |
| s 157(5) "agent" | 13210-13212 | encoded | `s 157(5) the person is an agent of the company for the purposes of sec...` | sgb1-tests-s157.l4; seat |
| heading, line 13214 | 13214-13214 | inert | reason 1 (not operative): a heading |  |
| s 157A(1) | 13216-13217 | fork | fork CB-06; encoded as `s 157A(1) the business of the company is managed as the subsection pro...` | sgb1-tests-s157.l4; seat |
| s 157A(2) | 13221-13223 | encoded | `s 157A(2) the directors may exercise the power of the company` | sgb1-tests-s157.l4; seat |
| heading, line 13227 | 13227-13227 | inert | reason 1 (not operative): a heading |  |
| s 157B | 13229-13237 | fork | fork SII-18; encoded as `s 157B the director may make the declaration by recording it and signi...`; `s 157B the recording and signing of the declaration satisfies the requ...` | sgb1-tests-s157.l4; seat |
| heading, line 13239 | 13239-13239 | inert | reason 1 (not operative): a heading |  |
| s 157C(1) | 13241-13245 | encoded | `s 157C(1) the director may rely on the reports, statements, financial ...` | sgb1-tests-s157.l4; seat |
| s 157C(1)(a) | 13247-13249 | encoded | `s 157C(1) the director may rely on the reports, statements, financial ...` | sgb1-tests-s157.l4; seat |
| s 157C(1)(b) | 13251-13253 | encoded | `s 157C(1) the director may rely on the reports, statements, financial ...` | sgb1-tests-s157.l4; seat |
| s 157C(1)(c) | 13255-13258 | encoded | `s 157C(1) the director may rely on the reports, statements, financial ...` | sgb1-tests-s157.l4; seat |
| s 157C(2) | 13260-13260 | encoded | `s 157C(2) subsection (1) applies to the director` | sgb1-tests-s157.l4; seat |
| s 157C(2)(a) | 13262-13262 | encoded | `s 157C(2) subsection (1) applies to the director` | sgb1-tests-s157.l4; seat |
| s 157C(2)(b) | 13264-13265 | encoded | `s 157C(2) subsection (1) applies to the director` | sgb1-tests-s157.l4; seat |
| s 157C(2)(c) | 13267-13267 | encoded | `s 157C(2) subsection (1) applies to the director` | sgb1-tests-s157.l4; seat |
| heading, line 13269 | 13269-13269 | inert | reason 1 (not operative): a heading |  |
| s 158(1) | 13271-13276 | fork | fork GI-08; encoded as `s 158(1) the director may disclose the information` | sgb1-tests-s157.l4; seat |
| s 158(2) | 13280-13281 | encoded | `s 158(2) the information may be disclosed to the person` | sgb1-tests-s157.l4; seat |
| s 158(2)(a) | 13286-13286 | encoded | `s 158(2) the information may be disclosed to the person` | sgb1-tests-s157.l4; seat |
| s 158(2)(b) | 13288-13291 | encoded | `s 158(2) the information may be disclosed to the person` | sgb1-tests-s157.l4; seat |
| s 158(3) | 13293-13294 | encoded | `s 158(3) the authorisation may be conferred in respect of the disclosu...` | sgb1-tests-s157.l4; seat |
| s 158(3)(a) | 13296-13296 | encoded | `s 158(3) the authorisation may be conferred in respect of the disclosu...` | sgb1-tests-s157.l4; seat |
| s 158(3)(b) | 13298-13299 | encoded | `s 158(3) the authorisation may be conferred in respect of the disclosu...` | sgb1-tests-s157.l4; seat |
| heading, line 13303 | 13303-13304 | inert | reason 1 (not operative): a heading |  |
| s 159 | 13306-13315 | fork | fork EN-02; encoded as `s 159 the directors are entitled to have regard to the matter in exerc...` | sgb1-tests-s157.l4; seat |
| heading, line 13317 | 13317-13318 | inert | reason 1 (not operative): a heading |  |
| s 160(1) | 13320-13324 | encoded | `s 160(1) the directors are barred from carrying the proposals into eff...`; `s 160(1) the directors must not carry into effect proposals for dispos...` | sgb1-tests-s157.l4; seat |
| s 160(2) | 13328-13330 | fork | fork SII-19; encoded as `s 160(2) the Court may restrain the directors from entering into the t...` | sgb1-tests-s157.l4; seat |
| s 160(3) | 13335-13338 | encoded | `s 160(3) the transaction is as valid as if subsection (1) had been com...` | sgb1-tests-s157.l4; seat |
| s 160(4) | 13340-13345 | encoded | `s 160(4) section 160 does not apply to the proposals` | sgb1-tests-s157.l4; seat |
| s 160A | 13347-13347 | repealed or blank in this text | the text shows "[Repealed by Act 38 of 1998]" |  |
| s 160B | 13349-13349 | repealed or blank in this text | the text shows "[Repealed by Act 38 of 1998]" |  |
| s 160C | 13351-13351 | repealed or blank in this text | the text shows "[Repealed by Act 38 of 1998]" |  |
| s 160D | 13353-13353 | repealed or blank in this text | the text shows "[Repealed by Act 38 of 1998]" |  |

## Fork register (sgb1)

Each line is one fork: the provision, the function (with the file and line of the branch it concerns), the answer taken, the other reading, the words of the text, and the line of `inputs/ENCODING-GUIDE.md` or the dated ruling it rests on.
Every Guide fragment quoted here was checked by script to occur in the Guide line it is cited against.
A fork id is also written in the coverage table, so a row marked `fork` finds its line here.
The "Marginal readings for a lawyer" section below repeats the ids of the lines that need a lawyer's eye.

### Reading a result: FALSE and NOTHING (sgb1)

This is the rule of 2026-10-29 in the terms of this range.
Every decision function answers a `MAYBE`: `JUST TRUE`, `JUST FALSE` or `NOTHING`.
`JUST TRUE` is yes in the direction the function's name asks: "is barred", "may", "must", "is guilty".
`JUST FALSE` is the text saying no in its own words.
In this range a "no" is one of: the person is not caught by a bar or an offence ("not barred by this subsection", "not guilty under this subsection": the split-site (i) reading); the Court, the Registrar or the Minister has no power on those facts because a "where", "upon" or "on" gate failed (the periods ruling and rule (c) of 2026-11-05); a condition introduced with "if", "only if" or "unless" failed; a flat negative applies ("does not apply", "is not deemed"); or a period the text fixes in its own words has run out (periods ruling (a)).
`NOTHING` is "the text does not say".
In this range that means: a bar or a grant limited in its own wording and the case outside the limit (s 145(2) for an adult natural person; s 154(8) for a court other than a District Court); a list the text leaves open ("includes": see the table below); a term the text leaves undefined ("substantially the whole" in s 160(1)); a matter the text hands to something outside the sources (the constitution in ss 145(4A), 147(2), 149B and 152(9)); or silence.
A caller must never turn `NOTHING` into `FALSE`, and `NOTHING` is neither a refusal nor a permission.
"Not covered" is always `NOTHING` or a constructor whose name says so (for example `s 159 another matter`, `s 146(1) somewhere else`), and each is asserted in the tests.
A penalty function answers `JUST (penalty record)` only for a person its offence function answers `JUST TRUE` for, and `NOTHING` for anyone else.

The branches of layer 1 that answer "no" or "not covered", counted by script from their tags:

| tag | branches | provisions |
| --- | --- | --- |
| `FALSE-kind` | 138 | |
| `NOTHING-kind` (limited by its own wording) | 93 | many (76 provisions) |
| `NOTHING-kind` (silent) | 17 | s 145A(3), s 145(8), s 146(4), s 147(4), s 148(1), s 149(12), s 149A(4), s 154(5), s 155(1), s 155B(10), s 155A(2), s 155C(2), s 155D(2), s 155E(3), s 156(15), s 156(7), s 157(3)(b) |
| `NOTHING-kind` (includes) | 7 | s 149(5), s 149(8), s 155(11), s 156(13), s 157(5), s 159 |
| `NOTHING-kind` (points outside the text) | 4 | s 145(4A), s 147(2), s 149B, s 152(9) |
| `NOTHING-kind` (list not closed) | 4 | s 149(6), s 157C(1), s 158(2), s 158(3) |

Every branch of the seven modules that answers `JUST FALSE` or `NOTHING` carries one of these tags (263 answer branches were checked by script; the one without a tag, the starting value of a fold in s 156(7), was tagged).

### Split site (i): an unmet element of an offence or a contravention (20)

Answer taken: `JUST FALSE`. Other reading: `NOTHING`.

- **SI-01** s 145(8): `s 145(8) the member is guilty of the offence this subsection creates` (sgb1-s145-directors.l4:228). Answer taken: JUST FALSE. Other reading: NOTHING. Text: "If the direction under subsection (7) is not complied with, each member in default shall be guilty of an offence". Licence: Guide line 98: "and for a bar, a duty or the provision's own question" (limit 2 of the grant ruling of 2026-11-12: the closest line, since no Guide line rules on an unmet element of an offence or a contravention); the other reading rests on Guide line 87: "or limits a grant or prohibition in its own wording and the case falls outside the limit".
- **SI-02** s 145(10): `s 145(10) the member is liable for the payment of the debts of the company` (sgb1-s145-directors.l4:285). Answer taken: JUST FALSE. Other reading: NOTHING. Text: "If a company carries on business without having at least one director who is ordinarily resident in Singapore for more than 6 months, a person who ... (a) is a member of the company; and (b) knows that it is carrying on business in that manner, shall be liable". Licence: Guide line 98: "and for a bar, a duty or the provision's own question" (limit 2 of the grant ruling of 2026-11-12: the closest line, since no Guide line rules on an unmet element of an offence or a contravention); the other reading rests on Guide line 87: "or limits a grant or prohibition in its own wording and the case falls outside the limit".
- **SI-03** s 145(10): `s 145(10) the debt is within the liability of the member` (sgb1-s145-directors.l4:298). Answer taken: JUST FALSE. Other reading: NOTHING. Text: "the member is not liable under this subsection". Licence: Guide line 98: "and for a bar, a duty or the provision's own question" (limit 2 of the grant ruling of 2026-11-12: the closest line, since no Guide line rules on an unmet element of an offence or a contravention); the other reading rests on Guide line 87: "or limits a grant or prohibition in its own wording and the case falls outside the limit".
- **SI-04** s 145A(3): `s 145A(3) the person is guilty of the offence this subsection creates` (sgb1-s145-directors.l4:423). Answer taken: JUST FALSE. Other reading: NOTHING. Text: "Any person who contravenes subsection (1) shall be guilty of an offence". Licence: Guide line 98: "and for a bar, a duty or the provision's own question" (limit 2 of the grant ruling of 2026-11-12: the closest line, since no Guide line rules on an unmet element of an offence or a contravention); the other reading rests on Guide line 87: "or limits a grant or prohibition in its own wording and the case falls outside the limit".
- **SI-05** s 146(4): `s 146(4) the person is guilty of the offence this subsection creates` (sgb1-s145-directors.l4:632). Answer taken: JUST FALSE. Other reading: NOTHING. Text: "If default is made in complying with this section, the company and every officer of the company who is in default shall be guilty of an offence". Licence: Guide line 98: "and for a bar, a duty or the provision's own question" (limit 2 of the grant ruling of 2026-11-12: the closest line, since no Guide line rules on an unmet element of an offence or a contravention); the other reading rests on Guide line 87: "or limits a grant or prohibition in its own wording and the case falls outside the limit".
- **SI-06** s 147(4): `s 147(4) the person is guilty of the offence this subsection creates` (sgb1-s145-directors.l4:734). Answer taken: JUST FALSE. Other reading: NOTHING. Text: "Any person who fails to comply with subsection (3) shall be guilty of an offence". Licence: Guide line 98: "and for a bar, a duty or the provision's own question" (limit 2 of the grant ruling of 2026-11-12: the closest line, since no Guide line rules on an unmet element of an offence or a contravention); the other reading rests on Guide line 87: "or limits a grant or prohibition in its own wording and the case falls outside the limit".
- **SI-07** s 148(1): `s 148(1) the person is guilty of the offence this subsection creates` (sgb1-s148-bankrupt-unfit.l4:48). Answer taken: JUST FALSE. Other reading: NOTHING. Text: "Every person who, being an undischarged bankrupt ..., acts as director of, or ... takes part in or is concerned in the management of, any corporation, except with the permission of the Court or the written permission of the Official Assignee, shall be guilty of an offence". Licence: Guide line 98: "and for a bar, a duty or the provision's own question" (limit 2 of the grant ruling of 2026-11-12: the closest line, since no Guide line rules on an unmet element of an offence or a contravention); the other reading rests on Guide line 87: "or limits a grant or prohibition in its own wording and the case falls outside the limit".
- **SI-08** s 149(12): `s 149(12) the person is guilty of the offence this subsection creates` (sgb1-s148-bankrupt-unfit.l4:532). Answer taken: JUST FALSE. Other reading: NOTHING. Text: "Any person who acts in contravention of a disqualification order made under this section shall be guilty of an offence". Licence: Guide line 98: "and for a bar, a duty or the provision's own question" (limit 2 of the grant ruling of 2026-11-12: the closest line, since no Guide line rules on an unmet element of an offence or a contravention); the other reading rests on Guide line 87: "or limits a grant or prohibition in its own wording and the case falls outside the limit".
- **SI-09** s 149A(4): `s 149A(4) the person is guilty of the offence this subsection creates` (sgb1-s148-bankrupt-unfit.l4:668). Answer taken: JUST FALSE. Other reading: NOTHING. Text: "Any person who acts in contravention of a disqualification order made under subsection (1) shall be guilty of an offence". Licence: Guide line 98: "and for a bar, a duty or the provision's own question" (limit 2 of the grant ruling of 2026-11-12: the closest line, since no Guide line rules on an unmet element of an offence or a contravention); the other reading rests on Guide line 87: "or limits a grant or prohibition in its own wording and the case falls outside the limit".
- **SI-10** s 154(5): `s 154(5) the person is guilty of the offence this subsection creates` (sgb1-s154-convicted-default.l4:196). Answer taken: JUST FALSE. Other reading: NOTHING. Text: "A person who contravenes subsection (3) shall be guilty of an offence". Licence: Guide line 98: "and for a bar, a duty or the provision's own question" (limit 2 of the grant ruling of 2026-11-12: the closest line, since no Guide line rules on an unmet element of an offence or a contravention); the other reading rests on Guide line 87: "or limits a grant or prohibition in its own wording and the case falls outside the limit".
- **SI-11** s 155(1): `s 155(1) the person is guilty of the offence this subsection creates` (sgb1-s154-convicted-default.l4:364). Answer taken: JUST FALSE. Other reading: NOTHING. Text: "Where a person has been persistently in default ... and that person, within a period of 5 years after ..., without the permission of the Court, is a director or promoter of ... a company, that person shall be guilty of an offence". Licence: Guide line 98: "and for a bar, a duty or the provision's own question" (limit 2 of the grant ruling of 2026-11-12: the closest line, since no Guide line rules on an unmet element of an offence or a contravention); the other reading rests on Guide line 87: "or limits a grant or prohibition in its own wording and the case falls outside the limit".
- **SI-12** s 155A(2): `s 155A(2) the person is guilty of the offence this subsection creates` (sgb1-s154-convicted-default.l4:541). Answer taken: JUST FALSE. Other reading: NOTHING. Text: "Any person who contravenes subsection (1) shall be guilty of an offence". Licence: Guide line 98: "and for a bar, a duty or the provision's own question" (limit 2 of the grant ruling of 2026-11-12: the closest line, since no Guide line rules on an unmet element of an offence or a contravention); the other reading rests on Guide line 87: "or limits a grant or prohibition in its own wording and the case falls outside the limit".
- **SI-13** s 155B(10): `s 155B(10) the person is guilty of the offence this subsection creates` (sgb1-s155b-debarment.l4:192). Answer taken: JUST FALSE. Other reading: NOTHING. Text: "Any person who contravenes subsection (2) shall be guilty of an offence". Licence: Guide line 98: "and for a bar, a duty or the provision's own question" (limit 2 of the grant ruling of 2026-11-12: the closest line, since no Guide line rules on an unmet element of an offence or a contravention); the other reading rests on Guide line 87: "or limits a grant or prohibition in its own wording and the case falls outside the limit".
- **SI-14** s 155C(2): `s 155C(2) the person is guilty of the offence this subsection creates` (sgb1-s155b-debarment.l4:326). Answer taken: JUST FALSE. Other reading: NOTHING. Text: "Any person who contravenes subsection (1) shall be guilty of an offence". Licence: Guide line 98: "and for a bar, a duty or the provision's own question" (limit 2 of the grant ruling of 2026-11-12: the closest line, since no Guide line rules on an unmet element of an offence or a contravention); the other reading rests on Guide line 87: "or limits a grant or prohibition in its own wording and the case falls outside the limit".
- **SI-15** s 155D(2): `s 155D(2) the person is guilty of the offence this subsection creates` (sgb1-s155b-debarment.l4:424). Answer taken: JUST FALSE. Other reading: NOTHING. Text: "Any person who contravenes subsection (1) shall be guilty of an offence". Licence: Guide line 98: "and for a bar, a duty or the provision's own question" (limit 2 of the grant ruling of 2026-11-12: the closest line, since no Guide line rules on an unmet element of an offence or a contravention); the other reading rests on Guide line 87: "or limits a grant or prohibition in its own wording and the case falls outside the limit".
- **SI-16** s 155E(3): `s 155E(3) the person is guilty of the offence this subsection creates` (sgb1-s155b-debarment.l4:536). Answer taken: JUST FALSE. Other reading: NOTHING. Text: "Any person who contravenes subsection (1) shall be guilty of an offence". Licence: Guide line 98: "and for a bar, a duty or the provision's own question" (limit 2 of the grant ruling of 2026-11-12: the closest line, since no Guide line rules on an unmet element of an offence or a contravention); the other reading rests on Guide line 87: "or limits a grant or prohibition in its own wording and the case falls outside the limit".
- **SI-17** s 156(15): `s 156(15) the person is guilty of the offence this subsection creates` (sgb1-s156-interests.l4:433). Answer taken: JUST FALSE. Other reading: NOTHING. Text: "Any director or chief executive officer of a company who fails to comply with any of the provisions of this section shall be guilty of an offence". Licence: Guide line 98: "and for a bar, a duty or the provision's own question" (limit 2 of the grant ruling of 2026-11-12: the closest line, since no Guide line rules on an unmet element of an offence or a contravention); the other reading rests on Guide line 87: "or limits a grant or prohibition in its own wording and the case falls outside the limit".
- **SI-18** s 157(2): `s 157(2) the officer or agent contravenes the subsection` (sgb1-s157-duties.l4:75). Answer taken: JUST FALSE. Other reading: NOTHING. Text: "An officer or agent of a company must not make improper use of his or her position as an officer or agent of the company or any information acquired by virtue of his or her position ... to gain, directly or indirectly, an advantage for himself or herself or for any other person or to cause detriment to the company". Licence: Guide line 98: "and for a bar, a duty or the provision's own question" (limit 2 of the grant ruling of 2026-11-12: the closest line, since no Guide line rules on an unmet element of an offence or a contravention); the other reading rests on Guide line 87: "or limits a grant or prohibition in its own wording and the case falls outside the limit".
- **SI-19** s 157(3): `s 157(3) the officer or agent commits a breach of a provision of section 157` (sgb1-s157-duties.l4:99). Answer taken: JUST FALSE. Other reading: NOTHING. Text: "An officer or agent who commits a breach of any of the provisions of this section". Licence: Guide line 98: "and for a bar, a duty or the provision's own question" (limit 2 of the grant ruling of 2026-11-12: the closest line, since no Guide line rules on an unmet element of an offence or a contravention); the other reading rests on Guide line 87: "or limits a grant or prohibition in its own wording and the case falls outside the limit".
- **SI-20** s 157(3)(b): `s 157(3)(b) the officer or agent is guilty of the offence this paragraph creates` (sgb1-s157-duties.l4:126). Answer taken: JUST FALSE. Other reading: NOTHING. Text: "An officer or agent who commits a breach of any of the provisions of this section shall be ... guilty of an offence". Licence: Guide line 98: "and for a bar, a duty or the provision's own question" (limit 2 of the grant ruling of 2026-11-12: the closest line, since no Guide line rules on an unmet element of an offence or a contravention); the other reading rests on Guide line 87: "or limits a grant or prohibition in its own wording and the case falls outside the limit".

### Split site (ii): a "may" gated by "where", "when", "upon" or "on application" (19)

Answer taken: `JUST FALSE`. Other reading: `NOTHING`.

- **SII-01** s 145(1): `s 145(1) the sole director may also be the sole member of the company` (sgb1-s145-directors.l4:49). Answer taken: NOTHING (S1b ruling, 2026S1bC). Other reading: JUST FALSE. Text: "where the company only has one member, that sole director may also be the sole member". Licence: Guide line 101 (the S1b ruling): a failed gate answers `NOTHING` where the function states a company's or person's liberty, standard or privilege with no bar to relieve, and a sole director's leave to be also the sole member is read as one; the other reading rests on Guide line 93: "(b) a "where ..." condition: when it fails the answer is `JUST FALSE`", which Guide line 101 replaces for the pure gates of these rows (it replaces limit 3, Guide line 99, for them); gate word: "where".
- **SII-02** s 148(2): `s 148(2) the Court or the Official Assignee may refuse the application or approve it subject to conditions` (sgb1-s148-bankrupt-unfit.l4:74). Answer taken: JUST FALSE. Other reading: NOTHING. Text: "On an application by an undischarged bankrupt under subsection (1) ... the Court or the Official Assignee may refuse the application or approve". Licence: Guide line 93: "(b) a "where ..." condition: when it fails the answer is `JUST FALSE`"; Guide line 94: "(c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above"; the other reading rests on Guide line 87: "or limits a grant or prohibition in its own wording and the case falls outside the limit"; the site is also listed for a lawyer under Guide line 99: "a "may" function whose gate is "where", "when" or "upon""; gate word: "on" (ruling (c) names "when", "upon" and "whenever" and not "on": the "on" gate was treated like "upon"; this fits no Guide line exactly).
- **SII-03** s 149(1): `s 149(1) the Court may make an order disqualifying the person` (sgb1-s148-bankrupt-unfit.l4:318). Answer taken: JUST FALSE. Other reading: NOTHING. Text: "The Court may -- (a) on the application of the Minister or the Official Receiver as provided for in subsection (9); and (b) on being satisfied as to the matters referred to in subsection (2), make an order". Licence: Guide line 93: "(b) a "where ..." condition: when it fails the answer is `JUST FALSE`"; Guide line 94: "(c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above"; the other reading rests on Guide line 87: "or limits a grant or prohibition in its own wording and the case falls outside the limit"; the site is also listed for a lawyer under Guide line 99: "a "may" function whose gate is "where", "when" or "upon""; gate word: "on" (ruling (c) names "when", "upon" and "whenever" and not "on": the "on" gate was treated like "upon"; this fits no Guide line exactly).
- **SII-04** s 149(4): `s 149(4) the Court may order the person to make good the default` (sgb1-s148-bankrupt-unfit.l4:369). Answer taken: JUST FALSE. Other reading: NOTHING. Text: "if default is made in complying with that requirement the Court may, on the application of the Minister, make an order". Licence: Guide line 93: "(b) a "where ..." condition: when it fails the answer is `JUST FALSE`"; Guide line 94: "(c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above"; the other reading rests on Guide line 87: "or limits a grant or prohibition in its own wording and the case falls outside the limit"; the site is also listed for a lawyer under Guide line 99: "a "may" function whose gate is "where", "when" or "upon""; gate word: "on" (ruling (c) names "when", "upon" and "whenever" and not "on": the "on" gate was treated like "upon"; this fits no Guide line exactly); the gate is also introduced with "if", where the grant ruling's limit 1 would give NOTHING.
- **SII-05** s 149(9A)(b): `s 149(9A)(b) the person against whom an order is sought may appear and give evidence or call witnesses` (sgb1-s148-bankrupt-unfit.l4:505). Answer taken: JUST FALSE. Other reading: NOTHING. Text: "On a hearing of an application under this section -- ... (b) the person against whom an order is sought may appear and himself or herself give evidence or call witnesses". Licence: Guide line 93: "(b) a "where ..." condition: when it fails the answer is `JUST FALSE`"; Guide line 94: "(c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above"; the other reading rests on Guide line 87: "or limits a grant or prohibition in its own wording and the case falls outside the limit"; the site is also listed for a lawyer under Guide line 99: "a "may" function whose gate is "where", "when" or "upon""; gate word: "on" (ruling (c) names "when", "upon" and "whenever" and not "on": the "on" gate was treated like "upon"; this fits no Guide line exactly).
- **SII-06** s 149A(1): `s 149A(1) the Court may make an order disqualifying the person` (sgb1-s148-bankrupt-unfit.l4:614). Answer taken: JUST FALSE. Other reading: NOTHING. Text: "where a company is ordered to be wound up by the Court under section 125(1)(n) ... the Court may, on the application of the Minister, make an order ... disqualifying any person who is a director of that company". Licence: Guide line 93: "(b) a "where ..." condition: when it fails the answer is `JUST FALSE`"; the other reading rests on Guide line 87: "or limits a grant or prohibition in its own wording and the case falls outside the limit"; the site is also listed for a lawyer under Guide line 99: "a "may" function whose gate is "where", "when" or "upon""; gate word: "where".
- **SII-07** s 154(6): `s 154(6) the person may apply to the Court for permission to act as a director or to take part in the management of a company` (sgb1-s154-convicted-default.l4:226). Answer taken: JUST FALSE. Other reading: NOTHING. Text: "may apply to the Court for permission ..., upon giving the Minister not less than 14 days' notice of his or her intention to apply". Licence: Guide line 93: "(b) a "where ..." condition: when it fails the answer is `JUST FALSE`"; Guide line 94: "(c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above"; the other reading rests on Guide line 87: "or limits a grant or prohibition in its own wording and the case falls outside the limit"; the site is also listed for a lawyer under Guide line 99: "a "may" function whose gate is "where", "when" or "upon""; gate word: "upon".
- **SII-08** s 154(7): `s 154(7) the Minister may be represented at the hearing and may oppose the granting of the application` (sgb1-s154-convicted-default.l4:238). Answer taken: JUST FALSE. Other reading: NOTHING. Text: "On the hearing of any application under subsection (6), the Minister may be represented". Licence: Guide line 93: "(b) a "where ..." condition: when it fails the answer is `JUST FALSE`"; Guide line 94: "(c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above"; the other reading rests on Guide line 87: "or limits a grant or prohibition in its own wording and the case falls outside the limit"; the site is also listed for a lawyer under Guide line 99: "a "may" function whose gate is "where", "when" or "upon""; gate word: "on" (ruling (c) names "when", "upon" and "whenever" and not "on": the "on" gate was treated like "upon"; this fits no Guide line exactly).
- **SII-09** s 155(10): `s 155(10) the Minister may be represented and may oppose the granting of the application` (sgb1-s154-convicted-default.l4:433). Answer taken: JUST FALSE. Other reading: NOTHING. Text: "On the hearing of any application under this section, the Minister may be represented and may oppose". Licence: Guide line 93: "(b) a "where ..." condition: when it fails the answer is `JUST FALSE`"; Guide line 94: "(c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above"; the other reading rests on Guide line 87: "or limits a grant or prohibition in its own wording and the case falls outside the limit"; the site is also listed for a lawyer under Guide line 99: "a "may" function whose gate is "where", "when" or "upon""; gate word: "on" (ruling (c) names "when", "upon" and "whenever" and not "on": the "on" gate was treated like "upon"; this fits no Guide line exactly).
- **SII-10** s 155A(3): `s 155A(3) the person may apply for permission to act as a director or to take part in the management of a company` (sgb1-s154-convicted-default.l4:594). Answer taken: JUST FALSE. Other reading: NOTHING. Text: "the Court, upon giving the Minister not less than 14 days' notice". Licence: Guide line 93: "(b) a "where ..." condition: when it fails the answer is `JUST FALSE`"; Guide line 94: "(c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above"; the other reading rests on Guide line 87: "or limits a grant or prohibition in its own wording and the case falls outside the limit"; the site is also listed for a lawyer under Guide line 99: "a "may" function whose gate is "where", "when" or "upon""; gate word: "upon".
- **SII-11** s 155A(4): `s 155A(4) the Minister may be represented at the hearing and may oppose the granting of the application` (sgb1-s154-convicted-default.l4:626). Answer taken: JUST FALSE. Other reading: NOTHING. Text: "On the hearing of any application under this section, the Minister may be represented". Licence: Guide line 93: "(b) a "where ..." condition: when it fails the answer is `JUST FALSE`"; Guide line 94: "(c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above"; the other reading rests on Guide line 87: "or limits a grant or prohibition in its own wording and the case falls outside the limit"; the site is also listed for a lawyer under Guide line 99: "a "may" function whose gate is "where", "when" or "upon""; gate word: "on" (ruling (c) names "when", "upon" and "whenever" and not "on": the "on" gate was treated like "upon"; this fits no Guide line exactly).
- **SII-12** s 155B(1): `s 155B(1) the Registrar may make a debarment order against the person` (sgb1-s155b-debarment.l4:32). Answer taken: JUST FALSE. Other reading: NOTHING. Text: "Where the Registrar is satisfied that a company is in default ..., the Registrar may make a debarment order against any person who, at the time the order is made, is a director or secretary of the company". Licence: Guide line 93: "(b) a "where ..." condition: when it fails the answer is `JUST FALSE`"; the other reading rests on Guide line 87: "or limits a grant or prohibition in its own wording and the case falls outside the limit"; the site is also listed for a lawyer under Guide line 99: "a "may" function whose gate is "where", "when" or "upon""; gate word: "where".
- **SII-13** s 155B(4): `s 155B(4) the Registrar may cancel or suspend the debarment order` (sgb1-s155b-debarment.l4:156). Answer taken: JUST FALSE. Other reading: NOTHING. Text: "may ... cancel or suspend such debarment order where the default ... has been rectified or on such other ground as may be prescribed". Licence: Guide line 93: "(b) a "where ..." condition: when it fails the answer is `JUST FALSE`"; the other reading rests on Guide line 87: "or limits a grant or prohibition in its own wording and the case falls outside the limit"; the site is also listed for a lawyer under Guide line 99: "a "may" function whose gate is "where", "when" or "upon""; gate word: "where".
- **SII-14** s 155C(3): `s 155C(3) the person may apply to the Court for permission to act as a director or to take part in the management of a company` (sgb1-s155b-debarment.l4:355). Answer taken: JUST FALSE. Other reading: NOTHING. Text: "may apply to the Court for permission ..., upon giving the Minister not less than 14 days' notice". Licence: Guide line 93: "(b) a "where ..." condition: when it fails the answer is `JUST FALSE`"; Guide line 94: "(c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above"; the other reading rests on Guide line 87: "or limits a grant or prohibition in its own wording and the case falls outside the limit"; the site is also listed for a lawyer under Guide line 99: "a "may" function whose gate is "where", "when" or "upon""; gate word: "upon".
- **SII-15** s 155C(4): `s 155C(4) the Minister may be represented at the hearing and may oppose the granting of the application` (sgb1-s155b-debarment.l4:372). Answer taken: JUST FALSE. Other reading: NOTHING. Text: "On the hearing of any application under subsection (3), the Minister may be represented". Licence: Guide line 93: "(b) a "where ..." condition: when it fails the answer is `JUST FALSE`"; Guide line 94: "(c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above"; the other reading rests on Guide line 87: "or limits a grant or prohibition in its own wording and the case falls outside the limit"; the site is also listed for a lawyer under Guide line 99: "a "may" function whose gate is "where", "when" or "upon""; gate word: "on" (ruling (c) names "when", "upon" and "whenever" and not "on": the "on" gate was treated like "upon"; this fits no Guide line exactly).
- **SII-16** s 155D(3): `s 155D(3) the person may apply to the Court for permission to act as a director or to take part in the management of a company` (sgb1-s155b-debarment.l4:455). Answer taken: JUST FALSE. Other reading: NOTHING. Text: "may apply to the Court for permission ..., upon giving the Minister not less than 14 days' notice". Licence: Guide line 93: "(b) a "where ..." condition: when it fails the answer is `JUST FALSE`"; Guide line 94: "(c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above"; the other reading rests on Guide line 87: "or limits a grant or prohibition in its own wording and the case falls outside the limit"; the site is also listed for a lawyer under Guide line 99: "a "may" function whose gate is "where", "when" or "upon""; gate word: "upon".
- **SII-17** s 155D(4): `s 155D(4) the Minister may be represented at the hearing and may oppose the granting of the application` (sgb1-s155b-debarment.l4:467). Answer taken: JUST FALSE. Other reading: NOTHING. Text: "On the hearing of any application under subsection (3), the Minister may be represented". Licence: Guide line 93: "(b) a "where ..." condition: when it fails the answer is `JUST FALSE`"; Guide line 94: "(c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above"; the other reading rests on Guide line 87: "or limits a grant or prohibition in its own wording and the case falls outside the limit"; the site is also listed for a lawyer under Guide line 99: "a "may" function whose gate is "where", "when" or "upon""; gate word: "on" (ruling (c) names "when", "upon" and "whenever" and not "on": the "on" gate was treated like "upon"; this fits no Guide line exactly).
- **SII-18** s 157B: `s 157B the director may make the declaration by recording it and signing the record` (sgb1-s157-duties.l4:188). Answer taken: JUST FALSE. Other reading: NOTHING. Text: "Where a company only has one director, that director may make a declaration required or authorised to be made under this Act by recording the declaration and signing the record". Licence: Guide line 93: "(b) a "where ..." condition: when it fails the answer is `JUST FALSE`"; the other reading rests on Guide line 87: "or limits a grant or prohibition in its own wording and the case falls outside the limit"; the site is also listed for a lawyer under Guide line 99: "a "may" function whose gate is "where", "when" or "upon""; gate word: "where".
- **SII-19** s 160(2): `s 160(2) the Court may restrain the directors from entering into the transaction` (sgb1-s157-duties.l4:401). Answer taken: JUST FALSE. Other reading: NOTHING. Text: "The Court may, on the application of any member of the company, restrain the directors from entering into a transaction in contravention of subsection (1)". Licence: Guide line 93: "(b) a "where ..." condition: when it fails the answer is `JUST FALSE`"; Guide line 94: "(c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above"; the other reading rests on Guide line 87: "or limits a grant or prohibition in its own wording and the case falls outside the limit"; the site is also listed for a lawyer under Guide line 99: "a "may" function whose gate is "where", "when" or "upon""; gate word: "on" (ruling (c) names "when", "upon" and "whenever" and not "on": the "on" gate was treated like "upon"; this fits no Guide line exactly).

### Grant ruling of 2026-11-12, limit 1: a "may" function whose "if" gate failed (8)

Answer taken: `NOTHING`. Other reading: `JUST FALSE`.

- **GI-01** s 145(7): `s 145(7) the Registrar may direct the members of the company to appoint a director who is ordinarily resident in Singapore` (sgb1-s145-directors.l4:211). Answer taken: NOTHING. Other reading: JUST FALSE. Text: "If there is a contravention of subsection (1), the Registrar may ... if the Registrar considers it to be in the interests of the company". Licence: Guide line 97: "answer `NOTHING`, with one fork line each, only for a function named for a grant or a power ("may", "is permitted to", "has power to") whose `if` gate failed"; the other reading rests on Guide line 86: "a condition the text introduces with "if", "only if", "as long as" or "unless"".
- **GI-02** s 145(9): `s 145(9) the Court may order the members of the company to make the appointment` (sgb1-s145-directors.l4:262). Answer taken: NOTHING. Other reading: JUST FALSE. Text: "If there is a contravention of subsection (1) and (a) ... or (b) ..., the Court may, on the application of the Registrar or any person, order ... if it considers it to be in the interests of the company". Licence: Guide line 97: "answer `NOTHING`, with one fork line each, only for a function named for a grant or a power ("may", "is permitted to", "has power to") whose `if` gate failed"; the other reading rests on Guide line 86: "a condition the text introduces with "if", "only if", "as long as" or "unless"".
- **GI-03** s 152(3): `s 152(3) the director may require that the representations be read out at the meeting` (sgb1-s149b-appointment.l4:235). Answer taken: NOTHING. Other reading: JUST FALSE. Text: "if a copy of the representations is not so sent because they were received too late or because of the company's default the director may ... require". Licence: Guide line 97: "answer `NOTHING`, with one fork line each, only for a function named for a grant or a power ("may", "is permitted to", "has power to") whose `if` gate failed"; the other reading rests on Guide line 86: "a condition the text introduces with "if", "only if", "as long as" or "unless"".
- **GI-04** s 152(4): `s 152(4) the Court may order the company's costs to be paid in whole or in part by the director` (sgb1-s149b-appointment.l4:264). Answer taken: NOTHING. Other reading: JUST FALSE. Text: "if ... the Court is satisfied ... and the Court may order the company's costs". Licence: Guide line 97: "answer `NOTHING`, with one fork line each, only for a function named for a grant or a power ("may", "is permitted to", "has power to") whose `if` gate failed"; the other reading rests on Guide line 86: "a condition the text introduces with "if", "only if", "as long as" or "unless"".
- **GI-05** s 152(5): `s 152(5) the vacancy may be filled as a casual vacancy` (sgb1-s149b-appointment.l4:277). Answer taken: NOTHING. Other reading: JUST FALSE. Text: "A vacancy created by the removal of a director of a public company under this section, if not filled at the meeting ..., may be filled as a casual vacancy". Licence: Guide line 97: "answer `NOTHING`, with one fork line each, only for a function named for a grant or a power ("may", "is permitted to", "has power to") whose `if` gate failed"; the other reading rests on Guide line 86: "a condition the text introduces with "if", "only if", "as long as" or "unless"".
- **GI-06** s 155A(3B): `s 155A(3B) the Registrar may grant the application under subsection (3)(a)` (sgb1-s154-convicted-default.l4:605). Answer taken: NOTHING. Other reading: JUST FALSE. Text: "may be granted by the Registrar if the Registrar, having regard to such considerations as may be prescribed, thinks fit". Licence: Guide line 97: "answer `NOTHING`, with one fork line each, only for a function named for a grant or a power ("may", "is permitted to", "has power to") whose `if` gate failed"; the other reading rests on Guide line 86: "a condition the text introduces with "if", "only if", "as long as" or "unless"".
- **GI-07** s 155A(3C): `s 155A(3C) the Court may grant the application under subsection (3)(b)` (sgb1-s154-convicted-default.l4:615). Answer taken: NOTHING. Other reading: JUST FALSE. Text: "may be granted by the Court if the Court thinks fit to do so". Licence: Guide line 97: "answer `NOTHING`, with one fork line each, only for a function named for a grant or a power ("may", "is permitted to", "has power to") whose `if` gate failed"; the other reading rests on Guide line 86: "a condition the text introduces with "if", "only if", "as long as" or "unless"".
- **GI-08** s 158(1): `s 158(1) the director may disclose the information` (sgb1-s157-duties.l4:321). Answer taken: NOTHING. Other reading: JUST FALSE. Text: "may disclose ... if such disclosure is not likely to prejudice the company and is made with the authorisation of the board of directors". Licence: Guide line 97: "answer `NOTHING`, with one fork line each, only for a function named for a grant or a power ("may", "is permitted to", "has power to") whose `if` gate failed"; the other reading rests on Guide line 86: "a condition the text introduces with "if", "only if", "as long as" or "unless"".

### A grant limited by its own wording or by the constitution (the "In short" line) (9)

Answer taken: `NOTHING`. Other reading: `JUST FALSE`.

- **GO-01** s 145(4A): `s 145(4A) the director may resign by giving the company a written notice of resignation` (sgb1-s145-directors.l4:178). Answer taken: NOTHING. Other reading: JUST FALSE. Text: "unless the constitution otherwise provides". Licence: Guide line 87: "or limits a grant or prohibition in its own wording and the case falls outside the limit"; Guide line 87: "points outside the sources"; the question is handed to the constitution, which is not among the sources; the other reading rests on Guide line 86: "a condition the text introduces with "if", "only if", "as long as" or "unless"".
- **GO-02** s 149(7): `s 149(7) the Minister may add to, vary or amend the matters referred to in subsection (6)` (sgb1-s148-bankrupt-unfit.l4:446). Answer taken: NOTHING. Other reading: JUST FALSE. Text: "The Minister may, by notification in the Gazette, add to, vary or amend the matters". Licence: Guide line 87: "or limits a grant or prohibition in its own wording and the case falls outside the limit"; the grant names its occasion, its person or its manner, and the case falls outside it; the other reading is that a grant limited in its own wording gives a "no" outside the limit.
- **GO-03** s 149B: `s 149B the company may appoint a director by ordinary resolution passed at a general meeting` (sgb1-s149b-appointment.l4:24). Answer taken: NOTHING. Other reading: JUST FALSE. Text: "Unless the constitution otherwise provides". Licence: Guide line 87: "or limits a grant or prohibition in its own wording and the case falls outside the limit"; Guide line 87: "points outside the sources"; the question is handed to the constitution, which is not among the sources; the other reading rests on Guide line 86: "a condition the text introduces with "if", "only if", "as long as" or "unless"".
- **GO-04** s 152(1): `s 152(1) the public company may remove the director by ordinary resolution` (sgb1-s149b-appointment.l4:147). Answer taken: NOTHING. Other reading: JUST FALSE. Text: "A public company may by ordinary resolution remove a director before the expiration of his or her period of office". Licence: Guide line 87: "or limits a grant or prohibition in its own wording and the case falls outside the limit"; the grant names its occasion, its person or its manner, and the case falls outside it; the other reading is that a grant limited in its own wording gives a "no" outside the limit.
- **GO-05** s 152(9): `s 152(9) the private company may remove the director by ordinary resolution` (sgb1-s149b-appointment.l4:346). Answer taken: NOTHING. Other reading: JUST FALSE. Text: "Subject to any provision to the contrary in the constitution". Licence: Guide line 87: "or limits a grant or prohibition in its own wording and the case falls outside the limit"; Guide line 87: "points outside the sources"; the question is handed to the constitution, which is not among the sources; the other reading rests on Guide line 86: "a condition the text introduces with "if", "only if", "as long as" or "unless"".
- **GO-06** s 154(2): `s 154(2) the court may make a disqualification order against the person` (sgb1-s154-convicted-default.l4:83). Answer taken: NOTHING. Other reading: JUST FALSE. Text: "The court may, in addition to any other sentence imposed, make a disqualification order against any person who is convicted in Singapore of any of the following offences". Licence: Guide line 87: "or limits a grant or prohibition in its own wording and the case falls outside the limit"; the grant names its occasion, its person or its manner, and the case falls outside it; the other reading is that a grant limited in its own wording gives a "no" outside the limit.
- **GO-07** s 154(8): `s 154(8) a District Court may make a disqualification order under the section` (sgb1-s154-convicted-default.l4:93). Answer taken: NOTHING. Other reading: JUST FALSE. Text: "a District Court may make a disqualification order under this section". Licence: Guide line 87: "or limits a grant or prohibition in its own wording and the case falls outside the limit"; the grant names its occasion, its person or its manner, and the case falls outside it; the other reading is that a grant limited in its own wording gives a "no" outside the limit.
- **GO-08** s 155B(8): `s 155B(8) the person may appeal to the Minister` (sgb1-s155b-debarment.l4:169). Answer taken: NOTHING. Other reading: JUST FALSE. Text: "Any person who is aggrieved by a debarment order ..., or the Registrar's refusal to cancel or suspend". Licence: Guide line 87: "or limits a grant or prohibition in its own wording and the case falls outside the limit"; the grant names its occasion, its person or its manner, and the case falls outside it; the other reading is that a grant limited in its own wording gives a "no" outside the limit.
- **GO-09** s 155B(11): `s 155B(11) the Registrar may publish the name and particulars of the person` (sgb1-s155b-debarment.l4:213). Answer taken: NOTHING. Other reading: JUST FALSE. Text: "the names and particulars of the persons against whom a debarment order has been made and which continues in force". Licence: Guide line 87: "or limits a grant or prohibition in its own wording and the case falls outside the limit"; the grant names its occasion, its person or its manner, and the case falls outside it; the other reading is that a grant limited in its own wording gives a "no" outside the limit.

### Marginal reading (a): an "if" in a provision that is neither a grant nor a bar (7)

Answer taken: `JUST FALSE`. Other reading: `NOTHING`.

- **MA-01** s 147(3): `s 147(3) the director must vacate office` (sgb1-s145-directors.l4:722). Answer taken: JUST FALSE. Other reading: NOTHING. Text: "A director must vacate his or her office if he or she has not within the period ... obtained his or her qualification or if after so obtaining it he or she ceases at any time to hold his or her qualification". Licence: Guide line 86: "a condition the text introduces with "if", "only if", "as long as" or "unless""; the other reading: "if A then B" does not itself say "if not A then not B" (the brief's reading (a) for a lawyer).
- **MA-02** s 149(2): `s 149(2) the Court must make a disqualification order against the person` (sgb1-s148-bankrupt-unfit.l4:297). Answer taken: JUST FALSE. Other reading: NOTHING. Text: "The Court must make a disqualification order under subsection (1) if it is satisfied that -- (a) ...; and (b) ...". Licence: Guide line 86: "a condition the text introduces with "if", "only if", "as long as" or "unless""; the other reading: "if A then B" does not itself say "if not A then not B" (the brief's reading (a) for a lawyer).
- **MA-03** s 149(3): `s 149(3) the Official Receiver or the liquidator must immediately report the matter to the Minister` (sgb1-s148-bankrupt-unfit.l4:346). Answer taken: JUST FALSE. Other reading: NOTHING. Text: "If in the case of a person who is or has been a director of the company which is ... being wound up ..., it appears ... that the conditions mentioned in subsection (2)(b) are satisfied ..., the Official Receiver or the liquidator ... must immediately report the matter to the Minister". Licence: Guide line 86: "a condition the text introduces with "if", "only if", "as long as" or "unless""; the other reading: "if A then B" does not itself say "if not A then not B" (the brief's reading (a) for a lawyer).
- **MA-04** s 152(4): `s 152(4) copies of the representations need not be sent out and the representations need not be read out` (sgb1-s149b-appointment.l4:255). Answer taken: JUST FALSE. Other reading: NOTHING. Text: "copies of the representations need not be sent out and the representations need not be read out if, on the application ..., the Court is satisfied that the rights ... are being abused". Licence: Guide line 86: "a condition the text introduces with "if", "only if", "as long as" or "unless""; the other reading: "if A then B" does not itself say "if not A then not B" (the brief's reading (a) for a lawyer).
- **MA-05** s 154(1): `s 154(1) the person is subject to the disqualifications provided in subsection (3)` (sgb1-s154-convicted-default.l4:59). Answer taken: JUST FALSE. Other reading: NOTHING. Text: "A person is subject to the disqualifications provided in subsection (3) if -- (a) the person is convicted of any of the following offences ...; or (b) the person is subject to the imposition of a civil penalty". Licence: Guide line 86: "a condition the text introduces with "if", "only if", "as long as" or "unless""; the other reading: "if A then B" does not itself say "if not A then not B" (the brief's reading (a) for a lawyer).
- **MA-06** s 155(4): `s 155(4) the person is treated as being adjudged guilty of 3 or more offences in relation to relevant requirements` (sgb1-s154-convicted-default.l4:318). Answer taken: JUST FALSE. Other reading: NOTHING. Text: "A person is to be treated as being adjudged guilty of 3 or more offences ... if the person is convicted of any 3 or more offences". Licence: Guide line 86: "a condition the text introduces with "if", "only if", "as long as" or "unless""; the other reading: "if A then B" does not itself say "if not A then not B" (the brief's reading (a) for a lawyer).
- **MA-07** s 156(5): `s 156(5) the declaration or written notice is treated as a sufficient declaration or written notice in relation to the transaction` (sgb1-s156-interests.l4:241). Answer taken: JUST FALSE. Other reading: NOTHING. Text: "is to be treated as a sufficient declaration or written notice ... if -- (a) ...; (b) ...; (c) ...; and (d) ...". Licence: Guide line 86: "a condition the text introduces with "if", "only if", "as long as" or "unless""; the other reading: "if A then B" does not itself say "if not A then not B" (the brief's reading (a) for a lawyer).

### Group 3 of the grant ruling: "entitled"-named functions (2)

- **EN-01** s 152(2): `s 152(2) the director is entitled to be heard on the resolution at the meeting` (sgb1-s149b-appointment.l4:194). Answer taken: JUST FALSE (the "on receipt" gate fails). Other reading: NOTHING. Text: "on receipt of notice of an intended resolution to remove a director under subsection (1) ... the director, whether or not he or she is a member of the company, is entitled to be heard". Licence: Guide line 99: "an "entitled"-named function (an entitlement is a claim, not a power, and this guide does not settle it)"; Guide line 93: "(b) a "where ..." condition: when it fails the answer is `JUST FALSE`"; Guide line 94: "(c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above" (an "on receipt" gate was treated like "upon").
- **EN-02** s 159: `s 159 the directors are entitled to have regard to the matter in exercising their powers` (sgb1-s157-duties.l4:344). Answer taken: JUST TRUE for the two matters the section lists; NOTHING for any other matter ("include" leaves the list open); the function never answers JUST FALSE. Other reading: the question could be asked as a claim of the directors against others; the answer would not change. Text: "The matters to which the directors of a company are entitled to have regard in exercising their powers include". Licence: Guide line 99: "an "entitled"-named function (an entitlement is a claim, not a power, and this guide does not settle it)"; the "includes" branch follows the "In short" line, Guide line 87: "says "includes"".

### Decided case by case (the maintainer, 2026-11-05T10:25:24Z): a duty whose "if" or "where" is unmet (6)

Answer taken: `JUST FALSE`. Other reading: `NOTHING`.

- **CB-01** s 149(9A)(a): `s 149(9A)(a) the Minister or the Official Receiver must appear and call the attention of the Court to any relevant matter` (sgb1-s148-bankrupt-unfit.l4:497). Answer taken: JUST FALSE ("the section's duty does not arise on these facts"). Other reading: NOTHING. Text: "On a hearing of an application under this section -- (a) the Minister or the Official Receiver ... must appear". Licence: Guide line 95: "a duty whose "if" or "where" is unmet"; decided at this site on the text's own words (the maintainer, 2026-11-05T10:25:24Z: "go with your gut most of the time").
- **CB-02** s 149(14): `s 149(14) the Minister or the Official Receiver must appear and call the attention of the Court to any matter relevant to the application` (sgb1-s148-bankrupt-unfit.l4:567). Answer taken: JUST FALSE ("the section's duty does not arise on these facts"). Other reading: NOTHING. Text: "On the hearing of an application made under subsection (13) or (15), the Minister or the Official Receiver must appear". Licence: Guide line 95: "a duty whose "if" or "where" is unmet"; decided at this site on the text's own words (the maintainer, 2026-11-05T10:25:24Z: "go with your gut most of the time").
- **CB-03** s 152(2): `s 152(2) the company must immediately send a copy of the notice to the director concerned` (sgb1-s149b-appointment.l4:186). Answer taken: JUST FALSE ("the section's duty does not arise on these facts"). Other reading: NOTHING. Text: "on receipt of notice of an intended resolution to remove a director under subsection (1) the company must immediately send a copy thereof to the director concerned". Licence: Guide line 95: "a duty whose "if" or "where" is unmet"; decided at this site on the text's own words (the maintainer, 2026-11-05T10:25:24Z: "go with your gut most of the time").
- **CB-04** s 152(3): `s 152(3) the company must notify the members of the representations` (sgb1-s149b-appointment.l4:226). Answer taken: JUST FALSE ("the section's duty does not arise on these facts"). Other reading: NOTHING. Text: "Where notice is given pursuant to subsection (2) and the director concerned makes ... representations ... and requests their notification to members of the company, the company must, unless the representations are received by it too late for it to do so". Licence: Guide line 95: "a duty whose "if" or "where" is unmet"; decided at this site on the text's own words (the maintainer, 2026-11-05T10:25:24Z: "go with your gut most of the time").
- **CB-05** s 156(12): `s 156(12) the directors must permit the chief executive officer to attend the meeting of the board of directors` (sgb1-s156-interests.l4:400). Answer taken: JUST FALSE ("the section's duty does not arise on these facts"). Other reading: NOTHING. Text: "must permit a chief executive officer of the company who is not a director to attend a meeting of the board of directors where such attendance is necessary". Licence: Guide line 95: "a duty whose "if" or "where" is unmet"; decided at this site on the text's own words (the maintainer, 2026-11-05T10:25:24Z: "go with your gut most of the time").
- **CB-06** s 157A(1): `s 157A(1) the business of the company is managed as the subsection provides` (sgb1-s157-duties.l4:160). Answer taken: JUST FALSE ("the section's duty does not arise on these facts"). Other reading: NOTHING. Text: "The business of a company is to be managed by, or under the direction or supervision of, the directors". Licence: Guide line 95: "a duty whose "if" or "where" is unmet" (a bare "is to be" with no "if" or "where"; the nearest of the six questions); decided at this site on the text's own words (the maintainer, 2026-11-05T10:25:24Z: "go with your gut most of the time").

### Individual forks and conventions (7)

- **F-145-1** s 145(2): `s 145(2) the subsection bars the person from being a director of a company` (sgb1-s145-directors.l4:60). Answer taken: a person outside the class (not a natural person, under 18, or without full legal capacity) is barred (JUST TRUE); a person inside the class answers NOTHING. Other reading: a person inside the class is "not barred by this subsection" (JUST FALSE), which is how the earlier pass used it: as a condition every named director must meet. Text: "No person other than a natural person who has attained the age of 18 years and who is otherwise of full legal capacity may be a director of a company". Licence: Guide line 87: "or limits a grant or prohibition in its own wording and the case falls outside the limit"; the subsection bars the others and says nothing of a person inside the class, who may still be barred by ss 148 to 155E.
- **F-146-1** s 146(3): `s 146(3) the requirements of subsections (1) and (2), other than the provisions relating to the signing of a consent to act as director, do not apply` (sgb1-s145-directors.l4:564). Answer taken: of the conditions in subsection (1A), only the consent to act, (1A)(a)(i), is a provision "relating to the signing of a consent to act as director", so for a company with no share capital or a private company the bar of subsection (1) still applies to a person who has not filed the consent, and lapses for one who has. Other reading: the whole of (1A)(a), the consent and the two statements of no disqualification and no debarment, "relates to the signing of a consent to act", so the bar needs all three filings even for a private company; or none of (1A) survives. Text: "Subsections (1) and (2) (other than the provisions relating to the signing of a consent to act as director) do not apply to". Licence: Guide line 86: "a condition the text introduces with "if", "only if", "as long as" or "unless""; reading (a) of the brief for a lawyer: the parenthesis is an exception to the exemption, and only (1A)(a)(i) is a consent.
- **F-146-2** s 146(3)(c): `s 146(3)(c) the document is outside subsections (1) and (2) by reason of paragraph (c)` (sgb1-s145-directors.l4:539). Answer taken: the one-year limit ("after the expiration of one year from the date on which the company was entitled to commence business") qualifies all three kinds of document in paragraph (c): a prospectus, a statement in lieu of prospectus, and a constitution. Other reading: the limit qualifies only "a constitution adopted by a company"; a prospectus or a statement in lieu would then be outside subsections (1) and (2) at any time (the rendering reads "issued or lodged with the Registrar by or on behalf of a company or to a constitution adopted by a company after the expiration of one year", which looks as if a word is lost between "or" and "to"). Text: "a prospectus or a statement in lieu of prospectus issued or lodged with the Registrar by or on behalf of a company or to a constitution adopted by a company after the expiration of one year from the date on which the company was entitled to commence business". Licence: no Guide line covers it; a reading of the text's grammar, in a rendering that may have lost a word.
- **F-14D** s 149(2), s 149A(2), s 154(6) and 5 more: eight functions that call the keel function "period: the date is at least a period before" with 14 Days (sg-periods.l4 (P5)). Answer taken: "not less than 14 days' notice" is counted by the keel's convention P5: the last day on which the notice may be given is the day of the hearing or application minus 14 days, the day of the notice counted and the day of the hearing not counted. Other reading: "clear days" (the keel's convention P7, "offered, never defaulted"): both the day of the notice and the day of the hearing are left out, so the notice is a day earlier. Text: "not less than 14 days' notice". Licence: the Act has no counting rule for notice except s 4(1) "business day" (the keel's sg-periods header); the choice is the keel's, not mine, and it is assumed, not ruled.
- **F-155-1** s 155(3): `s 155(3) the person's persistent default in relation to relevant requirements is conclusively proved` (sgb1-s154-convicted-default.l4:333). Answer taken: the two counts (offences adjudged, orders under s 13 or s 399, each "within a period of 5 years") are supplied by the person as numbers, each already restricted to a 5-year window; 3 or more of either is JUST TRUE; fewer is NOTHING. Other reading: the function takes the dates of each conviction and order and computes the window itself; or fewer than 3 is JUST FALSE. Text: "may, subject to subsection (8), be conclusively proved by showing that, within a period of 5 years, the person has been adjudged guilty of 3 or more offences in relation to any such requirements or has had 3 or more orders made". Licence: Guide line 87: "or limits a grant or prohibition in its own wording and the case falls outside the limit" ("may ... be conclusively proved by showing" names one way of proving it).
- **F-156-1** s 156(15): `s 156(15) the most the person may be penalised on conviction` (sgb1-s156-interests.l4:439). Answer taken: the penalty is a fine not exceeding $5,000 or imprisonment not exceeding 12 months, and the flag "the court may impose both" is FALSE, because the text says "or" and not "or to both". Other reading: both may be imposed together, as in the other penalty clauses of this range, which all say "or to both" or "and". Text: "a fine not exceeding $5,000 or to imprisonment for a term not exceeding 12 months". Licence: copied from the text; no Guide line applies.
- **F-156-2** s 156(7): `s 156(7) the first of the meetings held after the date` (sgb1-s156-interests.l4:275). Answer taken: a meeting held on the same day the person becomes a director (or commences to hold the office or property) is not "after" it: only a meeting on a later date counts. Other reading: a meeting held later the same day counts as the first meeting held after the person becomes a director. Text: "the first meeting of the directors of the company held after he or she becomes a director or chief executive officer". Licence: assumed, not ruled; compare the keel's convention P1, which leaves the day of the event out of "N days after X".

## Split sites (sgb1)

The brief asks, site by site, two questions the Guide leaves to the encoder, and says not to harmonise with other parts.
(i) An unmet element of an offence or a contravention: 20 sites, answer taken `JUST FALSE` at all 20.
(ii) A "may" gated by "where", "when", "upon", "on application" and the like: 19 sites, answer taken `JUST FALSE` at 18 and `NOTHING` at s 145(1), where the S1b ruling (Guide line 101, 2026S1bC) reads the gate as one on a liberty (5 "where" gates, 4 "upon" gates, 10 "on" gates).
No site takes `NOTHING` as its answer, so neither question has a site answered the other way.
The grant ruling of 2026-11-12 (limit 1) is a third, separate group (below): eight "may" functions whose "if" gate failed answer `NOTHING`.

### (i) Unmet element of an offence or a contravention

The Guide has no line on this.
The answer rests on the closest line, limit 2 of the grant ruling: Guide line 98: "and for a bar, a duty or the provision's own question", read as "the provision's own question is whether the person is guilty, or contravenes, under this subsection".
The other reading rests on Guide line 87: "or limits a grant or prohibition in its own wording and the case falls outside the limit".
A site that fits no Guide line says so in its fork line and is listed under "Marginal readings for a lawyer": all of these are.

| site | function | fork line |
| --- | --- | --- |
| s 145(8) | `s 145(8) the member is guilty of the offence this subsection creates` | SI-01 |
| s 145(10) | `s 145(10) the member is liable for the payment of the debts of the company` | SI-02 |
| s 145(10) | `s 145(10) the debt is within the liability of the member` | SI-03 |
| s 145A(3) | `s 145A(3) the person is guilty of the offence this subsection creates` | SI-04 |
| s 146(4) | `s 146(4) the person is guilty of the offence this subsection creates` | SI-05 |
| s 147(4) | `s 147(4) the person is guilty of the offence this subsection creates` | SI-06 |
| s 148(1) | `s 148(1) the person is guilty of the offence this subsection creates` | SI-07 |
| s 149(12) | `s 149(12) the person is guilty of the offence this subsection creates` | SI-08 |
| s 149A(4) | `s 149A(4) the person is guilty of the offence this subsection creates` | SI-09 |
| s 154(5) | `s 154(5) the person is guilty of the offence this subsection creates` | SI-10 |
| s 155(1) | `s 155(1) the person is guilty of the offence this subsection creates` | SI-11 |
| s 155A(2) | `s 155A(2) the person is guilty of the offence this subsection creates` | SI-12 |
| s 155B(10) | `s 155B(10) the person is guilty of the offence this subsection creates` | SI-13 |
| s 155C(2) | `s 155C(2) the person is guilty of the offence this subsection creates` | SI-14 |
| s 155D(2) | `s 155D(2) the person is guilty of the offence this subsection creates` | SI-15 |
| s 155E(3) | `s 155E(3) the person is guilty of the offence this subsection creates` | SI-16 |
| s 156(15) | `s 156(15) the person is guilty of the offence this subsection creates` | SI-17 |
| s 157(2) | `s 157(2) the officer or agent contravenes the subsection` | SI-18 |
| s 157(3) | `s 157(3) the officer or agent commits a breach of a provision of section 157` | SI-19 |
| s 157(3)(b) | `s 157(3)(b) the officer or agent is guilty of the offence this paragraph creates` | SI-20 |

### (ii) A "may" gated by "where", "when", "upon" or "on application"

The answer rests on the periods ruling of 2026-11-05, item (b): Guide line 93: "(b) a "where ..." condition: when it fails the answer is `JUST FALSE`"; and for "upon" and "on" gates on rule (c) of the second ruling of that date: Guide line 94: "(c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above".
The other reading rests on Guide line 87: "or limits a grant or prohibition in its own wording and the case falls outside the limit", and the Guide itself lists these sites for a lawyer: Guide line 99: "a "may" function whose gate is "where", "when" or "upon"".
The brief's question (ii) includes "on application"; rule (c) names "when", "upon" and "whenever" and does not name "on", so the sites with an "on" gate fit no Guide line exactly and are also listed under "Marginal readings for a lawyer".
s 149(4) is gated by "if default is made ... on the application of the Minister": the "if" is a limit-1 gate, which would answer `NOTHING`, and the "on application" gate is a split-site (ii) gate; the answer taken is `JUST FALSE` and the site is marginal.

| site | function | gate | fork line |
| --- | --- | --- | --- |
| s 145(1) | `s 145(1) the sole director may also be the sole member of the company` | where | SII-01 |
| s 148(2) | `s 148(2) the Court or the Official Assignee may refuse the application or approve it subje` | on | SII-02 |
| s 149(1) | `s 149(1) the Court may make an order disqualifying the person` | on | SII-03 |
| s 149(4) | `s 149(4) the Court may order the person to make good the default` | on | SII-04 |
| s 149(9A)(b) | `s 149(9A)(b) the person against whom an order is sought may appear and give evidence or ca` | on | SII-05 |
| s 149A(1) | `s 149A(1) the Court may make an order disqualifying the person` | where | SII-06 |
| s 154(6) | `s 154(6) the person may apply to the Court for permission to act as a director or to take ` | upon | SII-07 |
| s 154(7) | `s 154(7) the Minister may be represented at the hearing and may oppose the granting of the` | on | SII-08 |
| s 155(10) | `s 155(10) the Minister may be represented and may oppose the granting of the application` | on | SII-09 |
| s 155A(3) | `s 155A(3) the person may apply for permission to act as a director or to take part in the ` | upon | SII-10 |
| s 155A(4) | `s 155A(4) the Minister may be represented at the hearing and may oppose the granting of th` | on | SII-11 |
| s 155B(1) | `s 155B(1) the Registrar may make a debarment order against the person` | where | SII-12 |
| s 155B(4) | `s 155B(4) the Registrar may cancel or suspend the debarment order` | where | SII-13 |
| s 155C(3) | `s 155C(3) the person may apply to the Court for permission to act as a director or to take` | upon | SII-14 |
| s 155C(4) | `s 155C(4) the Minister may be represented at the hearing and may oppose the granting of th` | on | SII-15 |
| s 155D(3) | `s 155D(3) the person may apply to the Court for permission to act as a director or to take` | upon | SII-16 |
| s 155D(4) | `s 155D(4) the Minister may be represented at the hearing and may oppose the granting of th` | on | SII-17 |
| s 157B | `s 157B the director may make the declaration by recording it and signing the record` | where | SII-18 |
| s 160(2) | `s 160(2) the Court may restrain the directors from entering into the transaction` | on | SII-19 |

## Marginal readings for a lawyer (sgb1)

The brief names two readings it does not decide: (a) a failed "if" counts as the text's no, clause by clause, within the provision that holds the "if", and flat negatives count as the text saying no; (b) a prohibition or grant limited by its own wording does not.
I took both as the status quo.
Counts, by script: 138 branches answer `JUST FALSE`; 125 answer `NOTHING`, of which 93 are tagged "limited by its own wording" (reading (b)) and the rest are silent, include, list-not-closed or point outside the text.
Every `JUST FALSE` that rests on a failed "if", "unless" or "only if" rests on reading (a), and every `NOTHING` tagged "limited by its own wording" rests on reading (b); the other reading of each is the opposite answer.
The ones that are decisions about this range's own wording, not the generic rule, are these fork lines (the full line is in the register):

- SI-01 (s 145(8)): taken JUST FALSE; other reading NOTHING.
- SI-02 (s 145(10)): taken JUST FALSE; other reading NOTHING.
- SI-03 (s 145(10)): taken JUST FALSE; other reading NOTHING.
- SI-04 (s 145A(3)): taken JUST FALSE; other reading NOTHING.
- SI-05 (s 146(4)): taken JUST FALSE; other reading NOTHING.
- SI-06 (s 147(4)): taken JUST FALSE; other reading NOTHING.
- SI-07 (s 148(1)): taken JUST FALSE; other reading NOTHING.
- SI-08 (s 149(12)): taken JUST FALSE; other reading NOTHING.
- SI-09 (s 149A(4)): taken JUST FALSE; other reading NOTHING.
- SI-10 (s 154(5)): taken JUST FALSE; other reading NOTHING.
- SI-11 (s 155(1)): taken JUST FALSE; other reading NOTHING.
- SI-12 (s 155A(2)): taken JUST FALSE; other reading NOTHING.
- SI-13 (s 155B(10)): taken JUST FALSE; other reading NOTHING.
- SI-14 (s 155C(2)): taken JUST FALSE; other reading NOTHING.
- SI-15 (s 155D(2)): taken JUST FALSE; other reading NOTHING.
- SI-16 (s 155E(3)): taken JUST FALSE; other reading NOTHING.
- SI-17 (s 156(15)): taken JUST FALSE; other reading NOTHING.
- SI-18 (s 157(2)): taken JUST FALSE; other reading NOTHING.
- SI-19 (s 157(3)): taken JUST FALSE; other reading NOTHING.
- SI-20 (s 157(3)(b)): taken JUST FALSE; other reading NOTHING.
- SII-02 (s 148(2)): taken JUST FALSE; other reading NOTHING.
- SII-03 (s 149(1)): taken JUST FALSE; other reading NOTHING.
- SII-04 (s 149(4)): taken JUST FALSE; other reading NOTHING.
- SII-05 (s 149(9A)(b)): taken JUST FALSE; other reading NOTHING.
- SII-08 (s 154(7)): taken JUST FALSE; other reading NOTHING.
- SII-09 (s 155(10)): taken JUST FALSE; other reading NOTHING.
- SII-11 (s 155A(4)): taken JUST FALSE; other reading NOTHING.
- SII-15 (s 155C(4)): taken JUST FALSE; other reading NOTHING.
- SII-17 (s 155D(4)): taken JUST FALSE; other reading NOTHING.
- SII-19 (s 160(2)): taken JUST FALSE; other reading NOTHING.
- GI-01 (s 145(7)): taken NOTHING; other reading JUST FALSE.
- GI-02 (s 145(9)): taken NOTHING; other reading JUST FALSE.
- GI-03 (s 152(3)): taken NOTHING; other reading JUST FALSE.
- GI-04 (s 152(4)): taken NOTHING; other reading JUST FALSE.
- GI-05 (s 152(5)): taken NOTHING; other reading JUST FALSE.
- GI-06 (s 155A(3B)): taken NOTHING; other reading JUST FALSE.
- GI-07 (s 155A(3C)): taken NOTHING; other reading JUST FALSE.
- GI-08 (s 158(1)): taken NOTHING; other reading JUST FALSE.
- MA-01 (s 147(3)): taken JUST FALSE; other reading NOTHING.
- MA-02 (s 149(2)): taken JUST FALSE; other reading NOTHING.
- MA-03 (s 149(3)): taken JUST FALSE; other reading NOTHING.
- MA-04 (s 152(4)): taken JUST FALSE; other reading NOTHING.
- MA-05 (s 154(1)): taken JUST FALSE; other reading NOTHING.
- MA-06 (s 155(4)): taken JUST FALSE; other reading NOTHING.
- MA-07 (s 156(5)): taken JUST FALSE; other reading NOTHING.
- EN-01 (s 152(2)): taken JUST FALSE (the "on receipt" gate fails); other reading NOTHING.
- EN-02 (s 159): taken JUST TRUE for the two listed matters, NOTHING for any other; other reading asked as a claim; the answer would not change.
- CB-06 (s 157A(1)): taken JUST FALSE; other reading NOTHING.
- F-145-1 (s 145(2)): taken outside the class barred (JUST TRUE), inside it NOTHING; other reading inside the class "not barred" (JUST FALSE).
- F-146-1 (s 146(3)): taken only the consent to act survives s 146(3) for a private company; other reading all of (1A)(a), or none of (1A), survives.
- F-146-2 (s 146(3)(c)): taken the one-year limit qualifies all three kinds of document; other reading it qualifies only the constitution.
- F-14D (s 149(2), s 149A(2), s 154(6)): taken keel convention P5: the day of notice counted, the day of hearing not; other reading keel convention P7, clear days.
- F-156-2 (s 156(7)): taken a same-day meeting is not "after"; other reading a same-day meeting counts.

Flat negatives with a named bearer are encoded twice: as a decision function ("is barred") and as a prohibition (`SHANT`) by ruling N2 of 2026-11-04.
The 12 prohibitions are: s 145(5); s 145A(1); s 148(1); s 149(12); s 149A(4); s 154(3); s 155(1); s 155A(1); s 155B(2)(a); s 155B(2)(b); s 157(2); s 160(1).
The other reading of N2 is the one the ruling set aside (option C, the kind typed in the person-facing answer); it is not applied here.

## Jural relations (sgb1)

One row per provision that creates a relation, from the text of the Act, in Hohfeld's pairs: claim and duty, privilege and no-right, power and liability, immunity and disability.
Each rule is stated once, from the side of the party that holds the right, privilege, power or immunity, with the correlative in the next column; a provision that creates no relation (a definition, a counting rule, a saving) is listed once as `none`.
"The State" stands for the public interest that the offence provisions protect; the text names no private holder of those claims.
The last column names the L4 function or rule that encodes the provision (the first two, when there are several; the coverage table above lists the rest).

| provision | holder (what it holds) | correlative party (what it bears) | L4 rule |
| --- | --- | --- | --- |
| s 145(1) | the State, through the Registrar (claim that the company has a resident director); the sole director of a one-member company (privilege to be also the sole member) | the company (duty); the Registrar and other members (no-right as to the privilege) | `s 145(1) the company has a director who is ordinarily resident in Sing...`; `s 145(1) the sole director may also be the sole member of the company` |
| s 145(2) | the company and its members (immunity from having a director outside the class) | a person who is not a natural person of 18 or over with full legal capacity (disability to be a director) | `s 145(2) the subsection bars the person from being a director of a com...` |
| s 145(3) | none: deleted by Act 12 of 2002 | none | none |
| s 145(4) | a corporation named in an old constitution (power to appoint a natural person as director) | the company (liability to that appointment) | `s 145(4) the provision is read as authorising the corporation to appoi...` |
| s 145(4A) | a director (power to resign by written notice, unless the constitution provides otherwise) | the company (liability to the resignation) | `s 145(4A) the director may resign by giving the company a written noti...` |
| s 145(4B) | a director (immunity: the resignation needs no acceptance) | the company (disability to refuse it) | `s 145(4B) the resignation is conditional upon the company's acceptance...` |
| s 145(5) | the company and the Registrar (claim that a resident director always remains) | a director (duty not to resign or vacate; disability: a purported resignation in breach is invalid) | `s 145(5) the subsection bars the director from resigning or vacating o...`; `s 145(5) the purported resignation or vacation of office is invalid`; `s 145(5) a director must not resign or vacate office leaving no direct...` |
| s 145(6) | a director required to resign or vacate under (a) or (b) (immunity from subsection (5)) | the company and the Registrar (disability to hold the director to subsection (5)) | `s 145(6) subsection (5) does not apply to the director's resignation o...` |
| s 145(7) | the Registrar (power to direct the members to appoint a resident director) | the members (liability) | `s 145(7) the Registrar may direct the members of the company to appoin...` |
| s 145(8) | the State (claim that the members comply with the direction) | each member in default (duty; liable to the fine) | `s 145(8) the member is guilty of the offence this subsection creates`; `s 145(8) the most the member may be penalised on conviction` |
| s 145(9) | the Court (power to order the members to appoint); the Registrar or any person (power to apply) | the members (liability) | `s 145(9) the Court may order the members of the company to make the ap...` |
| s 145(10) | the creditors of the company (claim to payment of the debts) | a member who knows the company carries on business for more than 6 months with no resident director (duty to pay them) | `s 145(10) the member is liable for the payment of the debts of the com...` |
| s 145A(1) | the State (claim that no one acts as a nominee director by way of business unless a registered corporate service provider); a registered corporate service provider (privilege to act or to arrange it) | the person who so acts (duty); the State (no-right as to the provider) | `s 145A(1) the subsection bars the person from acting as a nominee dire...`; `s 145A(1) a person must not act as a nominee director by way of busine...` |
| s 145A(2) | a person acting for an affiliated company, or who began acting before the appointed day (immunity from subsection (1)) | the State (disability) | `s 145A(1) the subsection bars the person from acting as a nominee dire...` |
| s 145A(3) | the State (claim to obedience of subsection (1)) | a person who contravenes subsection (1) (duty; liable to the fine and the further daily fine) | `s 145A(3) the person is guilty of the offence this subsection creates`; `s 145A(3) the most the person may be fined on conviction` |
| s 145A(4); s 145A(4) "affiliated company"; s 145A(4) "appointed day"; s 145A(4) "nominee director" | none: definitions | none | none |
| s 146(1) | the Registrar (claim that no person is named before the conditions of subsection (1A) are met) | a person to be named, and whoever names the person (duty) | `s 146(1) the subsection bars the person from being named as a director...` |
| s 146(1A) | none: the conditions of subsection (1); the relation is subsection (1)'s | none | none |
| s 146(2) | the company (claim to the price of the shares) | a person who undertook to take and pay for qualification shares (duty; in the position of a subscriber) | `s 146(2) the person is, as regards those shares, in the same position ...` |
| s 146(3) | a company with no share capital, a private company, a prospectus or a constitution more than a year after the company could commence business (immunity from subsections (1) and (2), except the consent to act) | the Registrar (disability) | `s 146(3) the requirements of subsections (1) and (2), other than the p...` |
| s 146(4) | the State (claim) | the company and every officer in default (duty; liable to the fine and a default penalty) | `s 146(4) the person is guilty of the offence this subsection creates`; `s 146(4) the most the person may be penalised on conviction` |
| s 146(5) | none: extends subsections (1) and (4) to a director of a foreign company in relation to a prospectus; the relations are those of (1) and (4) | none | none |
| s 147(1) | the company (claim that a director holds the qualification the constitution requires) | the director (duty to obtain it within 2 months, or the shorter period the constitution fixes) | `s 147(1) the last day on which the director must have obtained the qua...`; `s 147(1) the director has obtained the qualification in time`; `s 147(1) a director must obtain the qualification in time` |
| s 147(2) | the company (claim that the qualification is held solely, not jointly, unless the constitution says otherwise) | the director (duty) | `s 147(2) the way the qualification is held meets the subsection` |
| s 147(3) | the company (claim that the director vacates office) | a director who has not qualified in time or has ceased to hold the qualification (duty to vacate) | `s 147(3) the director must vacate office` |
| s 147(4) | the State (claim) | a person who fails to vacate (duty; liable to the fine and a default penalty) | `s 147(4) the person is guilty of the offence this subsection creates`; `s 147(4) the most the person may be penalised on conviction` |
| s 147(5) | the company (immunity from re-appointing an unqualified person) | the person who vacated (disability to be re-appointed until qualified) | `s 147(5) the person cannot yet be re-appointed as director` |
| s 148(1) | the State and the creditors (claim that an undischarged bankrupt does not act as director or manage a corporation without permission) | the undischarged bankrupt (duty; liable to the fine or imprisonment) | `s 148(1) the person is guilty of the offence this subsection creates`; `s 148(1) the most the person may be penalised on conviction`; `s 148(1) an undischarged bankrupt must not act as director without per...` |
| s 148(2) | the Court or the Official Assignee (power to refuse or to approve on conditions) | the bankrupt who applies (liability) | `s 148(2) the Court or the Official Assignee may refuse the application...` |
| s 148(3) | the Minister and the Official Assignee (claim to notice; privilege to be represented and to oppose) | the Court (duty and disability: not to give permission unless notice was served); the applicant (no-right) | `s 148(3) the subsection bars the Court from giving permission` |
| s 148(4) | the Registrar (claim to a copy of the order or permission) | the person given permission (duty to lodge it within 14 days) | `s 148(4) the last day for lodging the copy of the order or written per...`; `s 148(4) the person has lodged the copy within the time the subsection...`; `s 148(4) a person granted permission must lodge a copy within 14 days` |
| s 149(1) | the Court (power to disqualify for up to 5 years); the Minister or the Official Receiver (power to apply) | the person who may be disqualified (liability) | `s 149(1) the Court may make an order disqualifying the person` |
| s 149(2) | the applicant, the Minister or the Official Receiver (claim that the Court disqualifies an unfit director) | the Court (duty to make the order when satisfied of (a) and (b)) | `s 149(2) the Court must make a disqualification order against the pers...` |
| s 149(3) | the Minister (claim to a report) | the Official Receiver or the liquidator (duty to report immediately) | `s 149(3) the Official Receiver or the liquidator must immediately repo...` |
| s 149(4) | the Minister (power to require information and records; power to apply for an order) | the Official Receiver, the liquidator or a former liquidator (liability; duty to furnish); the Court (power to order) | `s 149(4) the Court may order the person to make good the default` |
| s 149(5) | none: when a company has gone into liquidation and was insolvent, and what "conduct" includes | none | none |
| s 149(6) | the person against whom an order is sought (claim that the Court has regard to the listed matters, even without a conviction) | the Court (duty) | `s 149(6) the Court must have regard to the matter`; `s 149(6) the matter counts although the director has not been convicte...` |
| s 149(7) | the Minister (power to add to, vary or amend the matters) | a director whose conduct is judged (liability) | `s 149(7) the Minister may add to, vary or amend the matters referred t...` |
| s 149(8) | none: defines "company" for the section | none | none |
| s 149(9) | the Official Receiver or the Minister (power to apply, as the subsection allocates) | the person who may be disqualified (liability) | `s 149(9) who makes the application under the section` |
| s 149(9A) | the Court (claim that the Minister or Official Receiver appears and draws attention to relevant matters); the person against whom an order is sought (privilege to appear and give evidence) | the Minister or the Official Receiver (duty); the applicant and the Court (no-right) | `s 149(9A)(a) the Minister or the Official Receiver must appear and cal...` |
| s 149(10) | a director of a company that went into liquidation before 15 August 1984 (immunity: the section does not apply) | the Court (disability) | `s 149(10) the section applies to the company's liquidation`; `s 149(10) the conduct as a director of the company is conduct to which...` |
| s 149(11) | a judicial manager, receiver or receiver manager (immunity from an order for acts in that capacity) | the Court (disability) | `s 149(11) the person is liable to have a disqualification order made a...` |
| s 149(12) | the State (claim) | a person who acts in contravention of the order (duty; liable to the fine or imprisonment) | `s 149(12) the person is guilty of the offence this subsection creates`; `s 149(12) the most the person may be penalised on conviction`; `s 149(12) a person disqualified by an order must not act in contravent...` |
| s 149(13) | a disqualified person (privilege to apply to the Court for permission) | the Court and the Minister (no-right) | `s 149(13) the person may apply to the Court for permission to be conce...` |
| s 149(14) | the Court (claim that the Minister or the Official Receiver appears and draws attention to relevant matters) | the Minister or the Official Receiver (duty); the Minister (privilege to be represented and to give evidence) | `s 149(14) the Minister or the Official Receiver must appear and call t...` |
| s 149(15) | none: a transitional saving of a right subsisting before 23 March 1990 (inert, reason 2) | none | none |
| s 149A(1) | the Court (power to disqualify a director of a company wound up on national security grounds); the Minister (power to apply) | a director of that company (liability) | `s 149A(1) the Court may make an order disqualifying the person`; `s 149A(1) the last day of the disqualification` |
| s 149A(2) | the person against whom the order is sought (immunity from an order without 14 days' notice) | the Court (disability) | `s 149A(2) the subsection bars the Court from making a disqualification...` |
| s 149A(3) | a person who proves no consent or connivance and due diligence (immunity) | the Court (disability) | `s 149A(3) the subsection bars the Court from making a disqualification...` |
| s 149A(4) | the State (claim) | a person who acts in contravention of the order (duty; liable to the fine or imprisonment) | `s 149A(4) the person is guilty of the offence this subsection creates`; `s 149A(4) the most the person may be penalised on conviction`; `s 149A(4) a person disqualified by an order must not act in contravent...` |
| s 149A(5) | none: defines "foreign company" | none | none |
| s 149B | the members of the company in general meeting (power to appoint a director by ordinary resolution, unless the constitution provides otherwise) | the person appointed (liability) | `s 149B the company may appoint a director by ordinary resolution passe...` |
| s 150(1) | the members of a public company (claim that directors are voted on one by one) | whoever moves the motion (duty not to move it unless first agreed without a vote against) | `s 150(1) the section bars the motion for the appointment of 2 or more ...` |
| s 150(2) | the members (immunity from a void resolution being treated as valid) | the persons named in the motion (disability: not validly appointed by it) | `s 150(2) the resolution passed pursuant to the motion is void` |
| s 150(3) | the members (immunity from automatic re-appointment) | the retiring directors (disability: no automatic re-appointment) | `s 150(3) a provision for the automatic re-appointment of retiring dire...` |
| s 150(4) | none: a counting rule (a motion to approve or nominate counts as a motion to appoint) | none | none |
| s 150(5) | the members (immunity from section 150 for a resolution altering the constitution, and for election by ballot or poll) | whoever would invoke section 150 (disability) | `s 150(5) nothing in section 150 applies to the resolution or prevents ...` |
| s 151 | a person relying on the act of a director, chief executive officer or secretary (immunity from a challenge for a defect in appointment or qualification) | the company and any challenger (disability) | `s 151 the act is valid despite a defect in the appointment or qualific...` |
| s 152(1) | the members of a public company (power to remove a director before the end of the term, despite the constitution or any agreement); the class of shareholders or debenture holders a removed director was appointed to represent (claim that the removal waits until a successor is appointed) | the director (liability); the company (duty to wait for the successor) | `s 152(1) the public company may remove the director by ordinary resolu...`; `s 152(1) the resolution to remove the director cannot yet take effect` |
| s 152(2) | the director (claim to a copy of the notice; claim to be heard); the members (claim to special notice) | the company (duty to send a copy immediately); the proposer (duty to give special notice) | `s 152(2) special notice is required of the resolution`; `s 152(2) the company must immediately send a copy of the notice to the...`; `s 152(2) the director is entitled to be heard on the resolution at the...` (+1 more) |
| s 152(3) | the director (claim to have the representations notified and copied to the members; power to require them to be read out) | the company (duty to notify and send; liability to the requirement) | `s 152(3) the company must notify the members of the representations` |
| s 152(4) | the company or an aggrieved person (power to apply); the Court (power to excuse the sending and reading, and to order costs) | the director (liability, including to costs) | `s 152(4) copies of the representations need not be sent out and the re...`; `s 152(4) the Court may order the company's costs to be paid in whole o...` |
| s 152(5) | the company (privilege to fill the vacancy as a casual vacancy; the text does not say by whom) | the removed director (no-right) | `s 152(5) the vacancy may be filled as a casual vacancy` |
| s 152(6) | none: a counting rule (when a replacement is treated as having become a director) | none | none |
| s 152(7) | the removed person (immunity: compensation or damages are kept; other powers of removal are kept) | the company (disability) | `s 152(7) the removal deprives the person of compensation or damages pa...`; `s 152(7) the section derogates from a power to remove a director which...` |
| s 152(8) | a director of a public company (immunity from removal or a demand to vacate by the other directors) | the directors (disability) | `s 152(8) the subsection bars the directors from removing a director of...` |
| s 152(9) | the members of a private company (power to remove a director by ordinary resolution, subject to the constitution) | the director (liability) | `s 152(9) the private company may remove the director by ordinary resol...` |
| s 153 | none: repealed by Act 36 of 2014 | none | none |
| s 154(1) | the State (power over a convicted person) | a person convicted of a listed offence or subject to a civil penalty (liability to the disqualifications of subsection (3)) | `s 154(1) the person is subject to the disqualifications provided in su...` |
| s 154(2) | the court (power to make a disqualification order in addition to sentence) | a person convicted in Singapore of a listed offence (liability) | `s 154(2) the court may make a disqualification order against the perso...` |
| s 154(3) | the State (claim) | the disqualified person (duty not to act as a director or take part in management; disability) | `s 154(3) the subsection bars the person from acting as a director or t...`; `s 154(3) a disqualified person must not act as a director or take part...` |
| s 154(4) | none: a duration rule (when the disqualification takes effect and how long it lasts) | none | none |
| s 154(5) | the State (claim) | a person who contravenes subsection (3) (duty; liable to the fine or imprisonment) | `s 154(5) the person is guilty of the offence this subsection creates`; `s 154(5) the most the person may be penalised on conviction` |
| s 154(6) | a disqualified person (power to apply to the Court for permission, on 14 days' notice to the Minister) | the Court (liability to the application); the Minister (claim to the notice) | `s 154(6) the person may apply to the Court for permission to act as a ...` |
| s 154(7) | the Minister (privilege to be represented and to oppose) | the applicant (no-right) | `s 154(7) the Minister may be represented at the hearing and may oppose...` |
| s 154(8) | a District Court (power to make a disqualification order) | the convicted person (liability) | `s 154(8) a District Court may make a disqualification order under the ...` |
| s 154(9) | none: a transitional saving of a right subsisting before 12 November 1993 (inert, reason 2) | none | none |
| s 155(1) | the State (claim) | a person persistently in default who acts without the Court's permission within 5 years (duty; liable to the fine or imprisonment) | `s 155(1) the person is guilty of the offence this subsection creates`; `s 155(1) the most the person may be penalised on conviction`; `s 155(1) a person persistently in default must not be a director or ta...` |
| s 155(2) | none: defines "relevant requirement of this Act" | none | none |
| s 155(3) | the prosecution (privilege to prove persistent default conclusively by three convictions or three orders) | the person charged (no-right to dispute it) | `s 155(3) the person's persistent default in relation to relevant requi...` |
| s 155(4) | none: a counting rule (convictions by virtue of any contravention count as offences) | none | none |
| s 155(5) | a person convicted under section 154(2)(a) (immunity: the conviction is not counted) | the Court and the Registrar (disability) | `s 155(5) the conviction is treated as an offence in relation to a rele...` |
| s 155(6) | a person disqualified by a third or later order (privilege to comply with the order of the Court, with the status, powers and duties the person had) | the company and others (no-right) | `s 155(6) the section prevents the person from complying with the order...` |
| s 155(7) | the Registrar (privilege to rely on the certificate as prima facie evidence) | the person charged (liability to that evidence) | `s 155(7) the certificate of the Registrar is received in all courts as...` |
| s 155(8) | a person whose offence was committed or began before 15 May 1984 (immunity: not counted) | the Court (disability) | `s 155(8) account is taken of the offence for the purposes of the secti...` |
| s 155(9) | the Minister (claim to 14 days' notice) | a person intending to apply for permission (duty to give it) | `s 155(9) the person has given the Minister the notice the subsection r...` |
| s 155(10) | the Minister (privilege to be represented and to oppose) | the applicant (no-right) | `s 155(10) the Minister may be represented and may oppose the granting ...` |
| s 155(11) | none: extends "company" to an unregistered company | none | none |
| s 155A(1) | the State (claim) | a person who was a director of 3 or more companies struck off within 5 years (duty not to act or take part in management for the period) | `s 155A(1) the subsection bars the person from acting as a director or ...`; `s 155A(1) a person who was a director of 3 or more companies struck of...` |
| s 155A(1A) | none: a duration rule (3 or 5 years after the last strike-off) | none | none |
| s 155A(2) | the State (claim) | a person who contravenes subsection (1) (duty; liable to the fine or imprisonment) | `s 155A(2) the person is guilty of the offence this subsection creates`; `s 155A(2) the most the person may be penalised on conviction` |
| s 155A(3) | the disqualified person (power to apply to the Registrar or, on 14 days' notice to the Minister, to the Court) | the Registrar or the Court (liability to the application); the Minister (claim to the notice) | `s 155A(3) the person may apply for permission to act as a director or ...` |
| s 155A(3A) | the Registrar (claim that no application to the Court is made while hers is pending) | the applicant (disability) | `s 155A(3A) an application under subsection (3)(b) cannot be made` |
| s 155A(3B) | the Registrar (power to grant) | the applicant (liability) | `s 155A(3B) the Registrar may grant the application under subsection (3...` |
| s 155A(3C) | the Court (power to grant) | the applicant (liability) | `s 155A(3C) the Court may grant the application under subsection (3)(b)` |
| s 155A(4) | the Minister (privilege to be represented and to oppose) | the applicant (no-right) | `s 155A(4) the Minister may be represented at the hearing and may oppos...` |
| s 155A(5) | none: deleted by Act 17 of 2023 | none | none |
| s 155B(1) | the Registrar (power to make a debarment order against a director or secretary of a company in default) | the director or secretary (liability) | `s 155B(1) the Registrar may make a debarment order against the person` |
| s 155B(2) | the State (claim) | a person with a debarment order (duty not to act as director or secretary of another company) | `s 155B(2) the subsection bars the person from acting as director or se...`; `s 155B(2)(a) a person with a debarment order must not act as director ...` |
| s 155B(3) | none: a duration rule (the order applies from the date made until cancelled or suspended) | none | none |
| s 155B(4) | the Registrar (power to cancel or suspend); the debarred person (power to apply) | the debarred person (liability); the Registrar (liability to the application) | `s 155B(4) the Registrar may cancel or suspend the debarment order` |
| s 155B(5) | the Registrar (claim that the conditions are kept) | the person whose debarment is suspended (duty to fulfil the conditions) | `s 155B(5) the suspension of the debarment order operates` |
| s 155B(6) | a director or secretary (immunity from a debarment order without 3 months' default and 14 days' notice) | the Registrar (disability) | `s 155B(6) the subsection bars the Registrar from making a debarment or...` |
| s 155B(7) | the director or secretary (claim that the Registrar considers the representation) | the Registrar (duty) | `s 155B(7) the Registrar must consider the representation in determinin...` |
| s 155B(8) | an aggrieved person (power to appeal to the Minister) | the Minister (liability to the appeal) | `s 155B(8) the person may appeal to the Minister` |
| s 155B(9) | the Registrar (the order continues) | the appellant (no-right to suspension pending appeal) | `s 155B(9) the appeal suspends the effect of the debarment order` |
| s 155B(10) | the State (claim) | a person who contravenes subsection (2) (duty; liable to the fine or imprisonment) | `s 155B(10) the person is guilty of the offence this subsection creates`; `s 155B(10) the most the person may be penalised on conviction` |
| s 155B(11) | the Registrar (privilege to publish names and particulars) | the debarred persons (no-right) | `s 155B(11) the Registrar may publish the name and particulars of the p...` |
| s 155B(12); s 155B(12) "debarment order"; s 155B(12) "relevant requirement of this Act"; s 155B(12) "secretary" | none: definitions | none | none |
| s 155C(1) | the State (claim) | a person subject to a disqualification under the Limited Liability Partnerships Act 2005 (duty not to act as a director or take part in management) | `s 155C(1) the subsection bars the person from acting as a director or ...` |
| s 155C(2) | the State (claim) | a person who contravenes subsection (1) (duty; liable to the fine or imprisonment) | `s 155C(2) the person is guilty of the offence this subsection creates`; `s 155C(2) the most the person may be penalised on conviction` |
| s 155C(3) | a person disqualified under section 59 or 61 of that Act (power to apply to the Court, on 14 days' notice to the Minister) | the Court (liability); the Minister (claim to the notice) | `s 155C(3) the person may apply to the Court for permission to act as a...` |
| s 155C(4) | the Minister (privilege to be represented and to oppose) | the applicant (no-right) | `s 155C(4) the Minister may be represented at the hearing and may oppos...` |
| s 155D(1) | the State (claim) | a person subject to a disqualification under the VCC Act (duty not to act as a director or take part in management) | `s 155D(1) the subsection bars the person from acting as a director or ...` |
| s 155D(2) | the State (claim) | a person who contravenes subsection (1) (duty; liable to the fine or imprisonment) | `s 155D(2) the person is guilty of the offence this subsection creates`; `s 155D(2) the most the person may be penalised on conviction` |
| s 155D(3) | a person disqualified under sections 56, 58, 59 or 60 of the VCC Act (power to apply to the Court, on 14 days' notice to the Minister) | the Court (liability); the Minister (claim to the notice) | `s 155D(3) the person may apply to the Court for permission to act as a...` |
| s 155D(4) | the Minister (privilege to be represented and to oppose) | the applicant (no-right) | `s 155D(4) the Minister may be represented at the hearing and may oppos...` |
| s 155E(1) | the State (claim) | a person with a debarment order under section 59 of the VCC Act (duty not to act as director or secretary of another company) | `s 155E(1) the subsection bars the person from acting as director or se...` |
| s 155E(2) | none: a duration rule (from the date made until the Registrar cancels or suspends it) | none | none |
| s 155E(3) | the State (claim) | a person who contravenes subsection (1) (duty; liable to the fine or imprisonment) | `s 155E(3) the person is guilty of the offence this subsection creates`; `s 155E(3) the most the person may be penalised on conviction` |
| s 156(1) | the company (claim to a declaration or written notice of the interest) | a director or chief executive officer interested in a transaction (duty to declare or notify as soon as practicable) | `s 156(1) the director or chief executive officer must declare the natu...`; `s 156(1) a director must declare the nature of the interest` |
| s 156(2) | none: a timing rule for the notice under subsection (1)(b) | none | none |
| s 156(3) | a director or chief executive officer whose interest is only as a member or creditor and is not material (immunity from subsection (1)) | the company (disability) | `s 156(3) the requirements of subsection (1) do not apply` |
| s 156(4) | a director or chief executive officer who only guaranteed a loan, or is a director of a related corporation (immunity: not deemed interested) | the company (disability) | `s 156(4) the director or chief executive officer is not deemed to be i...` |
| s 156(5) | a director or chief executive officer who gives a standing declaration or notice (privilege to have it treated as sufficient) | the company (no-right) | `s 156(5) the declaration or written notice is treated as a sufficient ...` |
| s 156(6) | the company (claim to a declaration or written notice of a conflict) | a director or chief executive officer who holds a conflicting office or property (duty) | `s 156(6) the director or chief executive officer must declare the conf...` |
| s 156(7) | the company (claim to a declaration at the first meeting held after) | the director or chief executive officer (duty) | `s 156(7) the meeting of the directors at which the declaration under s...`; `s 156(7) a director must declare the conflict at the first meeting of ...` |
| s 156(8) | none: a timing rule for the notice under subsection (6)(b) | none | none |
| s 156(9) | the other directors, or all the directors where a chief executive officer gave the notice (claim to a copy) | the company (duty to send it as soon as practicable) | `s 156(9) the persons to whom the company must send a copy of the notic...` |
| s 156(10) | the director or chief executive officer who gives written notice (privilege: the notice is deemed part of the next meeting's proceedings) | the company (no-right) | `s 156(10)(a) the declaration is deemed to form part of the proceedings...`; `s 156(10)(b) section 188 applies as if the declaration had been made a...` |
| s 156(11) | the company and the directors (claim that declarations are minuted and records kept) | the secretary (duty) | `s 156(11) the secretary must record the declaration in the minutes of ...`; `s 156(11) the secretary must keep a record of the written resolution`; `s 156(11) the secretary must record every declaration in the minutes` |
| s 156(12) | a chief executive officer who is not a director (claim to attend a board meeting where needed to declare) | the directors (duty to permit) | `s 156(12) the directors must permit the chief executive officer to att...`; `s 156(12) the directors must permit the chief executive officer to att...` |
| s 156(13) | none: a counting rule (a family member's interest is treated as the director's or chief executive officer's) | none | none |
| s 156(14) | none: a saving (the section is in addition to other rules of law and the constitution) | none | none |
| s 156(15) | the State (claim) | a director or chief executive officer who fails to comply (duty; liable to the fine or imprisonment) | `s 156(15) the person is guilty of the offence this subsection creates`; `s 156(15) the most the person may be penalised on conviction` |
| s 157(1) | the company (claim to honesty and reasonable diligence) | a director (duty) | `s 157(1) the director has complied with the duty to act honestly and u...`; `s 157(1) a director must at all times act honestly and use reasonable ...` |
| s 157(2) | the company (claim that no improper use is made of position or information) | an officer or agent (duty) | `s 157(2) the officer or agent contravenes the subsection`; `s 157(2) an officer or agent must not make improper use of the positio...` |
| s 157(3) | the company (claim to the profit and the damage); the State (claim) | an officer or agent who commits a breach (duty to account; liable to the fine or imprisonment) | `s 157(3) the officer or agent commits a breach of a provision of secti...` |
| s 157(4) | none: a saving (the section is in addition to other written law and rules of law) | none | none |
| s 157(5); s 157(5) "officer"; s 157(5) "agent" | none: definitions | none | none |
| s 157A(1) | the directors (power to manage the business) | the members (liability to that management) | `s 157A(1) the business of the company is managed as the subsection pro...` |
| s 157A(2) | the directors (power to exercise all the company's powers except those reserved to general meeting) | the company (liability) | `s 157A(2) the directors may exercise the power of the company` |
| s 157B | a sole director (privilege to make a declaration by recording and signing it) | the company and the Registrar (no-right) | `s 157B the director may make the declaration by recording it and signi...`; `s 157B the recording and signing of the declaration satisfies the requ...` |
| s 157C(1) | a director (privilege to rely on reports, information and advice) | the company and anyone alleging a breach of duty (no-right) | `s 157C(1) the director may rely on the reports, statements, financial ...` |
| s 157C(2) | the company (claim that the reliance is in good faith, with proper inquiry, and without knowledge it is unwarranted) | a director (duty to meet the three conditions to have the privilege) | `s 157C(2) subsection (1) applies to the director` |
| s 158(1) | a director (privilege to disclose, with the board's authorisation, information not likely to prejudice the company) | the company (no-right) | `s 158(1) the director may disclose the information` |
| s 158(2) | none: lists to whom the disclosure in subsection (1) may be made | none | none |
| s 158(3) | the board of directors (power to authorise disclosure of all or a class of information, or specified information) | the director (liability to the extent of the authorisation) | `s 158(3) the authorisation may be conferred in respect of the disclosu...` |
| s 159 | the directors (privilege to have regard to employees' and members' interests and to rulings of the Securities Industry Council) | members and others (no-right to complain of that regard) | `s 159 the directors are entitled to have regard to the matter in exerc...` |
| s 160(1) | the members of the company in general meeting (claim that the whole or substantially the whole of the undertaking or property is not disposed of without their approval) | the directors (duty not to carry the proposals into effect) | `s 160(1) the directors are barred from carrying the proposals into eff...`; `s 160(1) the directors must not carry into effect proposals for dispos...` |
| s 160(2) | a member (power to apply); the Court (power to restrain) | the directors (liability) | `s 160(2) the Court may restrain the directors from entering into the t...` |
| s 160(3) | a person dealing for valuable consideration without actual notice (immunity: the transaction is as valid as if (1) had been complied with) | the company (disability) | `s 160(3) the transaction is as valid as if subsection (1) had been com...` |
| s 160(4) | a receiver and manager or a liquidator in a voluntary winding up (immunity from section 160) | the company's members (disability) | `s 160(4) section 160 does not apply to the proposals` |
| s 160A; s 160B; s 160C; s 160D | none: repealed by Act 38 of 1998 | none | none |

## Seams (sgb1)

A part cannot import another part, so a fact another part computes is an input here, named for the fact and the section it comes from (`inputs/PLAN.md` section 4).

### Seams I take (PLAN.md section 4 B, and my row in section 6)

| the text asks | the keel function called | where in my modules | in PLAN.md? |
| --- | --- | --- | --- |
| a company by virtue of s 6 deemed related to a corporation that employs the person (line 11757, s 145A(4) "affiliated company" (b)) | `s 4(1) "related corporation" the other corporation is a related corporation of the corporation`, taking the s 6 answer as one BOOLEAN | `sgb1-s145-directors.l4:358` | yes, seam B and my row |
| a corporation which by virtue of s 6 is deemed to be related to the company (line 12994, s 156(4)(b)) | the same | `sgb1-s156-interests.l4:91` | yes, seam B and my row |
| "public company" (ss 150(1), 152(1), 152(8)) | `s 4(1) "public company" the company is a public company`, called with the shared seat input `the company is a private company` | `sgb1-s149b-appointment.l4:62, 145, 329` | yes, "any part using ... `public company`", seam B last rows; the input name is the brief's |
| "private company" (s 152(9), s 146(3)(b)) | no keel call: the shared input `the company is a private company` is used directly, because the text asks only whether the company is private | `sgb1-s149b-appointment.l4:347`, `sgb1-s145-directors.l4:561` | yes, the input name is the brief's |
| "registered corporate service provider" (s 145A(1)) | `s 4(1) "registered corporate service provider" the person is a registered corporate service provider` | `sgb1-s145-directors.l4:405` | no: found in the keel while encoding |
| a reference to an undischarged bankrupt covers an insolvent person (s 148(1)) | `s 4(7) a reference to a person being an undischarged bankrupt covers the person being an undischarged bankrupt or insolvent`, called with its contrary-intention input FALSE | `sgb1-s148-bankrupt-unfit.l4:43` | no: found in the keel while encoding |
| every period, notice and time limit | the `period:` functions of `sg-periods.l4` | `sgb1-s145-directors.l4`, `sgb1-s148-bankrupt-unfit.l4`, `sgb1-s154-convicted-default.l4`, `sgb1-s155b-debarment.l4` | yes, "any part counting a period" |

`s 4(10)` and `s 4(11)` (the single-director functions) are in my PLAN.md row ("take the number of directors from the seat input `the number of directors of the company`") and I did not call them.
s 157B turns on whether the company "only has one director", which the shared input `the number of directors of the company` EQUALS 1 answers directly (`sgb1-s157-duties.l4`, `s 157B the director may make the declaration ...`); calling `s 4(10)` or `s 4(11)` would only say who "the directors" are when there is one, and nothing in my range turns on that.
I record this as a seam the plan lists and the encoding does not use.

### Facts from later waves and other Acts, taken as inputs named for the fact

- ss 13 and 399 (lines 12535 to 12585, s 155): "orders made under section 13 or 399" are counts, dates and facts the person states (`sgb1-s154-convicted-default.l4:331, 353, 368, 389, 404`).
- s 344 (lines 12618 to 12623, s 155A(1)): the number of companies whose names were struck off "under section 344(4) read with section 344(1)" within 5 years, and of which the person was then a director, is a number (`sgb1-s154-convicted-default.l4:516`).
- s 171 (line 12812, s 155B(12) "secretary"): `the person is a secretary of the company appointed under section 171` is a BOOLEAN (`sgb1-s155b-debarment.l4:240`).
- ss 138, 190, 191, 196B, 197, 199, 201 (line 12091, s 149(6)(a)(iii)), s 396B (line 12433, s 154(2)(b)), s 188 (line 13113, s 156(10)(b)) and s 409 (line 12518, s 154(8)): cited by number in the name or the text of a constructor or a function; I take no answer from those sections.
- Other Acts (the Insolvency, Restructuring and Dissolution Act 2018 ss 125, 130, 161, 237, 239, 245; the Securities and Futures Act 2001; the Limited Liability Partnerships Act 2005 ss 59 to 61; the VCC Act ss 56 to 60; the Corruption, Drug Trafficking and Other Serious Crimes (Confiscation of Benefits) Act 1992; the eleven Acts named in s 145(6)(b)): each is a BOOLEAN or a count the person states, named for the fact; none is read from memory.
- Two dates the text does not give: the commencement of section 56 of the Corporate and Accounting Laws (Amendment) Act 2025 (s 154(1)(a)(iii), `sgb1-s154-convicted-default.l4:49`) and of section 38(b) of the Corporate Service Providers Act 2024 (the "appointed day" of s 145A(4), `sgb1-s145-directors.l4:367`): each is a DATE the person states.
- Numbers the text leaves to the constitution or to the order of a court: the shorter qualification period in s 147(1) (days) and the shorter disqualification the court orders in s 154(4)(a) (months).

### Seams I give (what other parts cite of mine, `inputs/XREFS.md`)

| cited from | my section | the function a part would use |
| --- | --- | --- |
| `K`: line 1031 | s 145 | `s 145(1) the company has a director who is ordinarily resident in Singapore` |
| sgb2: 14961, 15118, 15174 | s 148 | `s 148(1) the person is guilty of the offence this subsection creates`; `s 148(3) the subsection bars the Court from giving permission` |
| sgb2: 14963, 15120, 15174 | s 149, s 149A | `s 149(2) the Court must make a disqualification order against the person`; `s 149A(1) the Court may make an order disqualifying the person` |
| sgb2: 14961, 14963, 15118, 15120 and others | s 154 | `s 154(1) the person is subject to the disqualifications provided in subsection (3)`; `s 154(3) the subsection bars the person from acting as a director or taking part in the management of the company` |
| sgb2: 14961, 15118, 15174 | s 155 | `s 155(1) the person is guilty of the offence this subsection creates` |
| sgb2: 15118, 15174 | s 155A, s 155C, s 155D | `s 155A(1) the subsection bars the person from acting as a director or taking part in the management of the company`; `s 155C(1)`; `s 155D(1)` |
| sgb2: 14559 | s 155B | `s 155B(2) the subsection bars the person from acting as director or secretary of the company` |
| sga2: 7798, 8088 | s 157 | `s 157(3) the officer or agent commits a breach of a provision of section 157` |

I did not read those other parts, so the pairing above is by section number only (what `XREFS.md` records), not by what they ask.

## Rules with no breach path (sgb1)

20 regulative rules are encoded (`PARTY ... MUST/SHANT ...`), 12 of them prohibitions (`SHANT`, by ruling N2) and 8 duties (`MUST`).
Each has at least one `#TRACE` with a `-- EXPECT` line directly above it (47 traces in all); every prohibition and every duty with a `WITHIN` has a trace that reaches `BREACH`.
A `MUST` with no `WITHIN` cannot be breached: a late act still reads `FULFILLED` and no act reads `RESIDUAL`.
These 5 rules are of that kind, because the text gives no time limit and no consequence for the duty itself, and I did not invent one:

| provision | rule | why there is no deadline | traces (EXPECT) |
| --- | --- | --- | --- |
| s 152(2) | `s 152(2) a public company must send a copy of the notice of an intended removal to the director` (`sgb1-s149b-appointment.l4:363`) | the text says "immediately" and gives no number, and states no consequence for the duty | FULFILLED, FULFILLED, RESIDUAL |
| s 156(1) | `s 156(1) a director must declare the nature of the interest` (`sgb1-s156-interests.l4:467`) | "as soon as is practicable" is a standard, not a number; the consequence is the offence in s 156(15), which is a separate function | FULFILLED, FULFILLED, RESIDUAL |
| s 156(11) | `s 156(11) the secretary must record every declaration in the minutes` (`sgb1-s156-interests.l4:500`) | no time is given; the secretary "must record every declaration" | FULFILLED, RESIDUAL |
| s 156(12) | `s 156(12) the directors must permit the chief executive officer to attend` (`sgb1-s156-interests.l4:514`) | no time is given; the directors "must permit" attendance | FULFILLED, RESIDUAL |
| s 157(1) | `s 157(1) a director must at all times act honestly and use reasonable diligence` (`sgb1-s157-duties.l4:433`) | "at all times" is a standing duty; the consequence is s 157(3), a separate function | FULFILLED, RESIDUAL |

The same duties are also encoded as decision functions over the facts (for example `s 156(1) the person has made the declaration or sent the written notice the subsection requires`), so a caller can ask "was it done" without a clock.
The three duties with a time (`s 147(1)`, `s 148(4)`, `s 156(7)`) have `BREACH` traces for both a late act and no act.

## Tests, traces and the checks I ran (sgb1)

- Every expected value was written from the text of the Act, beside the assertion, before the run; nothing was changed to match the code.
- Cover: every branch of each rule, the values on both sides of each threshold or date limit, every seat question, and for each rule with a gate a case outside it (an explicit `NOTHING` or "not covered" constructor, asserted).
- Assertions written and satisfied (`check.sh`): layer-1 tests 651, seat cases 427; failed 0; refused 0.
  Assertions written equal assertions satisfied: the `#ASSERT` lines are 1078 and the satisfied count is 1078.
- `work/trcheck.py` (a scratch script, not shipped) runs every test file on the stable build 1.6.110 and the main build 1.6.109, reads each `#TRACE` outcome as `FULFILLED`, `BREACH` or `RESIDUAL`, compares it with the `-- EXPECT` word above it, and compares the two builds: 47 traces in 7 files, 0 disagreements, run again after the last change to the modules and the seat.
  `check.sh` does not see a different trace outcome (its own footer says so), so this is the only comparison of the traces.
- `l4 check` was run on each of the 16 `sgb1-*.l4` files on both builds: 0 error or warning diagnostics, and 0 lines containing "follows code on its line" or "is at the end of the file".
- `srcrefs.py check --refs`: srcrefs check: 1172 src: lines, 177 runs, 221 locators, 0 problems.  `srcrefs.py check --strict`: srcrefs check: 1172 src: lines, 177 runs, 221 locators, 0 problems.
- A mutation run: one scratch copy each of the s 145 and s 148 modules was changed and the tests re-run; the s 145 tests then failed 3 assertions and the s 148 tests failed 1.
  What was changed was not kept (the scratch copies were deleted), so this shows that those tests are not vacuous for those two modules and nothing about the others.
- The seat questions are asked in `sgb1-cases-seat.l4` by their own names, so a wrong argument order or a wrong function behind a question fails there.

## The seat layer (sgb1)

`sgb1-seat.l4` has 197 questions, 468 lines carrying an `@desc`, and every question is named "Under section N, ..." and calls one layer-1 function; the inputs of a question are those of its function, with the same names and the same `@desc` wherever the same fact recurs.
The questions follow the Act's order under `§` headings.
The shared names `the number of directors of the company` and `the company is a private company` are used where the brief fixes them.
Nothing is asked of an official: the Registrar's, the Minister's, the Official Assignee's and the Court's powers appear as what they mean to the person ("may the Registrar direct the members?", "may the Court disqualify me?").

### Direction list

The brief asks for a list of every question whose name and body differ in direction or in subject, with each fixed.
I checked by script (the function name and the question each sorted into bar, grant, duty, offence or penalty): of 196 table questions, 107 have a class on both sides and 107 agree; the others ask a count, a date or a fact and have no direction.
The script reports 0 mismatches now. Two were found and fixed:

- `s 149(10)` was first asked in the opposite direction ("excluded"); it now asks "is the conduct ... conduct to which the Court is to have regard?", the direction of its function.
- `s 152(1)` was asked "can the resolution ... not yet take effect"; the function answers that it cannot yet take effect, so the question now reads "does the resolution to remove a director not yet take effect because the successor has not been appointed".

Questions whose function is a bar are titled as the bar ("is ... barred"), grants as "may", duties as "must", offences as "is ... guilty", penalties as "what is the most ...".
The questions begin: "is" 77, "may" 40, "what" 23, "does" 22, "must" 11, "has" 8, "do" 4, "on" 3, "are" 3, "from" 2, "was" 1, "who" 1, "at" 1, "to" 1.

## Compared with the earlier pass

`inputs/NAIVE-EVIDENCE/coa-formation-shares-buyback.l4` is a first pass for one scenario that touches ss 145, 146 and 157 of my range.
I read lines 117 to 147 and 180 to 205 of it and the lines a search for the section numbers of my range found in both files (its opening comment and the case lines that name ss 145, 146 and 157), and nothing else; I did not copy its code, names or expected values.
It covers ss 145(1)-(2), 146(1)-(1A) and 157(1)-(4); none of the rest of my range (ss 145(3) to 156, 157A to 160D) is in it.

| provision | the earlier pass | this encoding | cases that differ |
| --- | --- | --- | --- |
| s 145(1) | `named directors ordinarily resident in Singapore` AT LEAST 1, one conjunct of "the named directors meet sections 145 and 146" | the count at least 1 is `JUST TRUE`, fewer is `JUST FALSE` (the duty not met); the second limb (a sole director may also be the sole member) is its own function and is not in the earlier pass | a company with no resident director: both say not met; a one-member company: only this encoding answers it |
| s 145(2) | "every named director is a natural person of 18 or over of full capacity" is a condition every director must meet | a bar: outside the class `JUST TRUE` (barred); inside the class `NOTHING`, because the subsection says nothing of a person inside it (fork F-145-1) | a 17-year-old: both reject, but this encoding says "barred"; an adult natural person of full capacity: the earlier pass says "meets", this encoding says the subsection does not say |
| s 146(1), (1A) | one BOOLEAN, "every named director filed consent and the section 146(1A) statements before incorporation" | three functions: (1A)(a) the three filings, (1A)(b) the four share-qualification filings, and the bar of (1) over both, with the places where the person is named | a director who filed the consent but not the other statements: the earlier pass says "not filed"; this encoding says barred unless s 146(3) applies |
| s 146(3) | not encoded | the exemptions for a company with no share capital, a private company and the one-year documents; only the consent survives for a private company (fork F-146-1) | a private company whose named director filed only the consent: the earlier pass fails the incorporation, this encoding says the person is not barred |
| s 157(1) | `NOT (acted honestly AND used reasonable diligence)` is "in breach", over two facts only | a person who is not a director answers `NOTHING`; a director who has not done both answers `JUST FALSE` to "has complied"; a `MUST` rule with no deadline (no breach path) | a person who is not a director: the earlier pass computes a breach from the two facts alone |
| s 157(2) | "improper use AND (gain or detriment)" as a BOOLEAN | the same elements, answered `JUST TRUE` or, if one is unmet, `JUST FALSE` (split site (i), SI-18); also a `SHANT` rule | no case differs in value; the differences are the types and the rule |
| s 157(3) | the highest fine 20,000 and the longest imprisonment 12 months as two constants | the breach is a function; the liability to the company for profit and for damage is two functions returning the amount; the penalty is a function that gives the fine, the months and "both" only for a person who is an officer or agent and has committed a breach, `NOTHING` otherwise | a person with no breach: the earlier pass still returns 20,000 and 12 |
| s 157(4) | stated as not encoded ("the general law ... is not encoded") | encoded as a function (`s 157(4)`) that says the section does not derogate | |

I did not run the earlier pass (its imports are not in my folder).
The comparison is of what the code says; where two readings differ, both are in the fork register (F-145-1, F-146-1) so that the reviewer can overrule either.

## What the text turns out to say (sgb1)

Numbered, so a reviewer can cite them; each was read from the text of lines 11592-13354 and checked against the function that encodes it.

1. **Eight rows are shown repealed or deleted**: s 145(3) ("[Deleted by Act 12 of 2002]"), s 145(6)(c) ("[Deleted by Act 24 of 2025 wef 06/05/2026]", a paragraph of a live subsection), s 153 ("[Repealed by Act 36 of 2014]"), s 155A(5) ("[Deleted by Act 17 of 2023 wef 01/07/2023]") and ss 160A to 160D ("[Repealed by Act 38 of 1998]").
2. **Ten different offences carry one and the same penalty**: a fine not exceeding $10,000 or imprisonment not exceeding 2 years or both (ss 148(1), 149(12), 149A(4), 154(5), 155(1), 155A(2), 155B(10), 155C(2), 155D(2), 155E(3)); 10 of the 16 penalty functions are of that kind, counted by script. The others differ: s 145(8) $2,000 plus $1,000 a day, s 145A(3) $10,000 plus $1,000 a day, s 146(4) $10,000 and a default penalty, s 147(4) $4,000 and a default penalty, s 156(15) $5,000 or 12 months, s 157(3)(b) $20,000 or 12 months or both (the highest fine in the range).
3. **s 156(15) is the only offence in the range that offers a fine or imprisonment without "or to both"** (fork F-156-1). The offence is also drawn wide ("fails to comply with any of the provisions of this section"), so it reaches a director's or chief executive officer's failure to meet s 156(1) or (6), neither of which has a number of days; the text gives no other consequence for missing them.
4. **s 145(2) is a bar and not a grant**: "No person other than a natural person who has attained the age of 18 years and who is otherwise of full legal capacity may be a director". It says nothing of a person inside the class, who may still be barred by ss 148 to 155E, so an eligible person is `NOTHING` here (F-145-1).
5. **The resident-director floor (s 145(1), (5), (6)) has two exits.** A director may not resign or vacate office if no resident director would remain, and a purported resignation in breach is invalid (s 145(5)); the bar does not apply where the director is required to go for want of the share qualification or by virtue of disqualification, removal or revocation under ss 148, 149, 149A, 154, 155, 155A or 155C or under named sections of eleven other Acts (s 145(6)).
6. **The Act has no counting rule for notice or periods** except s 4(1) "business day", yet "not less than 14 days' notice" is used eight times in this range (F-14D). The count is the keel's convention P5.
7. **Seven doors lead to one bar.** Disqualification by the Court for insolvency (s 149), on national security grounds (s 149A), on conviction (s 154), for persistent default (s 155), for three struck-off companies (s 155A), under the LLP Act (s 155C) and under the VCC Act (s 155D) each bar the person from acting as a director or taking part in management; debarment (ss 155B, 155E) bars acting as a director or secretary of another company; and an undischarged bankrupt is barred by s 148.
   The routes out differ: the Court on 14 days' notice to the Minister (ss 154(6), 155(9) and (10), 155A(3)(b), 155C(3), 155D(3)); the Registrar with no notice (s 155A(3)(a)); the Court or the Official Assignee for a bankrupt (s 148(2)); an application to the Registrar to cancel or suspend (s 155B(4)); and, for s 149 orders only, s 149(13).
8. **The text states no route to permission for a person disqualified under s 149A**, and none for debarment under s 155E apart from the Registrar's cancelling or suspending the order (s 155E(2)); the encoding has no function for such a route, because the text gives none.
9. **s 155(3) names one way to prove persistent default** ("may ... be conclusively proved by showing" three convictions or three orders in 5 years) and does not say that default is not persistent without them: `NOTHING` below three (F-155-1).
10. **Every "as soon as is practicable" and "immediately" in the range is a standard with no number**: s 149(3), s 152(2), and s 156(1), (2), (8), (9). Only s 156(7) has a time, and it is fixed by a meeting, not by days: "at the first meeting of the directors ... held after" the person becomes a director or begins to hold the office or property.
11. **s 152(1) and s 152(9) differ in what a constitution can do.** A public company may remove a director by ordinary resolution "despite anything in its constitution or in any agreement"; a private company may do so "subject to any provision to the contrary in the constitution". For a private company whose constitution says otherwise the answer is `NOTHING` (the text points outside the sources).
12. **s 160(3) makes a transaction in breach of s 160(1) valid for an outsider** who gave value and had no actual notice, so the bar in s 160(1) ("Despite anything in a company's constitution") does not touch the transaction against such a person, and s 160(2) lets a member ask the Court to restrain it before it is entered into. "Substantially the whole" of the undertaking or property is not defined (`NOTHING`).
13. **s 157(3)(b) makes a breach of s 157(1), the director's duty of honesty and diligence, a criminal offence** as well as a liability to the company (s 157(3)(a), for the profit made and the damage suffered), because s 157(3) reaches "any of the provisions of this section".
14. **s 157C(2) closes the gate on reliance with "only if"** (good faith, proper inquiry, no knowledge that the reliance is unwarranted); a director who fails one is `JUST FALSE`, not `NOTHING`, by the Guide's "only if" line.
15. **The rendering garbles one clause**: s 146(3)(c) reads "issued or lodged with the Registrar by or on behalf of a company or to a constitution adopted by a company after the expiration of one year", which looks as if a word is lost; the two readings are F-146-2.

## What the text does not answer (sgb1)

- Who holds the claim in the offence provisions: the text says "shall be guilty of an offence" and names no private claim-holder; the table above says "the State".
- The two commencement dates (s 154(1)(a)(iii), s 145A(4) "appointed day"): inputs.
- Any number for "as soon as is practicable" or "immediately" (finding 10).
- A route to permission under s 149A and s 155E (finding 8).
- What "substantially the whole" of an undertaking is (s 160(1)), what a "material interest" is (s 156(3): "may properly be regarded as not being a material interest", a judgment taken as a BOOLEAN input), what is "improper use" and "reasonable diligence" (s 157), and "persistently in default" apart from the proof in s 155(3).
- What a company's constitution says in ss 145(4A), 147(1) and (2), 149B and 152(9): `NOTHING` or an input.
- What the other Acts say (the offences in s 154(1)(a), the disqualifications in ss 155C and 155D, the matters in s 145(6)(b)); each is a fact the person states.
- Whether a same-day meeting is "after" the day a person becomes a director (F-156-2) and how "not less than 14 days" is counted (F-14D).

## Assumed, not ruled (sgb1)

These are choices that no ruling covers and that I made so the work could go on; each can be reverted alone.

- The seat is the one the brief assumes: an individual who is, or is about to become, a director, a company secretary or a member of a company, or who deals with one.
- "The State" as the holder of the claim in every offence provision (above).
- The keel's counting conventions P1 to P9, including P5 for "not less than N days before", are taken as the keel states them (F-14D, F-156-2).
- An act done before the clock starts (a lodging or a qualification earlier than the day the period begins) is treated as in time, because the deadline functions test "not later than the last day" (`period: the date is not later than the end of a period after`); the tests of `s 147(1)` and `s 148(4)` call this fork P2 and the traces read `FULFILLED`.
- Shorter periods the constitution or the court fixes are numbers in days (s 147(1)) or months (s 154(4)(a)) that the person states.
- s 160(1) takes no constitution input: "Despite anything in a company's constitution" says the bar holds whatever the constitution says.
- s 154(1)(a)(iii) and the "appointed day" take a supplied date, because the text names the Act and section that commences them and not the date.
- A same-day meeting is not "after" (F-156-2).
- The counts in s 155(3) are supplied already restricted to the 5-year window (F-155-1).
- The `s 156(15) penalty` record says "both" is FALSE (F-156-1).

## What the stable binary does not accept (sgb1)

The binary is `l4` 1.6.110 (main, e51181d, 2026-11-11), with 1.6.109 (main, 4c887e0, 2026-11-04) as the second build; `JL4_LIBRARY_PATH` is unset.
Where the skills describe a construct the stable binary rejects, the binary governs.

Met while encoding (tried, and the binary refused it):

- `(EMPTY LIST)` is a parse error. The empty list is written `(LIST)`, and a non-empty list `(LIST (Date 1 1 2026), (Date 2 1 2026))`.

Avoided because the Guide (section 5) says the binary rejects them, and not tried again by me:

- `REFUSE`, `#ASSERT REFUSED`, and `BECAUSE` outside `LEST BREACH ... BECAUSE` (a "not covered" answer is `NOTHING` or a constructor, asserted).
- An unparenthesised `NOT` before `AND` (every `NOT` is parenthesised).
- A continuation line inside an `#ASSERT` (every `#ASSERT` is on one line).
- `YMD` (dates are `Date day month year`, and no `YMD` is defined in any file), `WAIT UNTIL` (written `WAITUNTIL`), `TYPICALLY` on a record field, and `•` bullets in a `LIST` of strings.
- `IMPORT` of a module from another folder (every module is in the one folder and the seat imports the layer-1 modules by name).

(Checked by search of the 16 `sgb1-*.l4` files: none contains `YMD`, `REFUSE`, `•` or `WAIT UNTIL`, and every `BECAUSE` is in a `LEST BREACH BY ... BECAUSE`.)
Regulative rules are run with `#TRACE`, which works on the stable binary; each trace's outcome is checked against its `-- EXPECT` word by `work/trcheck.py` on both builds.
I did not try to assert a trace outcome with `#ASSERT`, so I cannot say whether the stable binary accepts that; every duty and prohibition is also encoded as a decision function over the facts, and those are asserted.

## What check.sh prints

Run from `encodings/legalese-sonnet-5.5/` as `env -u JL4_LIBRARY_PATH L4=<l4-main-110> L4_MAIN=<l4-main-109> ./check.sh`; it exited 0.

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
sgb1-cases-seat.l4                             0       427       0        0         0 |      0       427       0        0  same
sgb1-s145-directors.l4                         0         0       0        0         0 |      0         0       0        0  same
sgb1-s148-bankrupt-unfit.l4                    0         0       0        0         0 |      0         0       0        0  same
sgb1-s149b-appointment.l4                      0         0       0        0         0 |      0         0       0        0  same
sgb1-s154-convicted-default.l4                 0         0       0        0         0 |      0         0       0        0  same
sgb1-s155b-debarment.l4                        0         0       0        0         0 |      0         0       0        0  same
sgb1-s156-interests.l4                         0         0       0        0         0 |      0         0       0        0  same
sgb1-s157-duties.l4                            0         0       0        0         0 |      0         0       0        0  same
sgb1-seat.l4                                   0         0       0        0         0 |      0         0       0        0  same
sgb1-tests-s145.l4                             0       130       0        0         0 |      0       130       0        0  same
sgb1-tests-s148.l4                             0        97       0        0         0 |      0        97       0        0  same
sgb1-tests-s149b.l4                            0        71       0        0         0 |      0        71       0        0  same
sgb1-tests-s154.l4                             0        97       0        0         0 |      0        97       0        0  same
sgb1-tests-s155b.l4                            0        98       0        0         0 |      0        98       0        0  same
sgb1-tests-s156.l4                             0        72       0        0         0 |      0        72       0        0  same
sgb1-tests-s157.l4                             0        86       0        0         0 |      0        86       0        0  same
TOTAL (24 modules)                             0      1078       0        0           |      0      1078       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

The columns are errors, satisfied, failed, refused and expected-to-fail for the stable build, then the same four for the main build and "same" when the main build's four counts equal the stable build's.
There are no assertions in the keel modules and none in the seven layer-1 modules and the seat (their tests are in the `sgb1-tests-*` files and the cases file), so those rows read 0.
The supplied `check.sh` keeps no baseline file, so there are no earlier numbers to give; the eight keel modules print 0 assertions each (their checks are the keel's), and the numbers above are the first full run of the finished set.


## The S1b ruling on failed gates (2026S1bC)

The Guide records this ruling at section 5, in the bullet that begins “Failed gates of the pure “may” functions”; it is copied here word for word, as the Guide asks of every ruling.

> - **Failed gates of the pure "may" functions of the two Singapore encodings: the split follows the background, not the holder's name (card S1b of the bench "Singapore Split Sites", option C as modified on the card; accepted by Meng).** Conditions as printed on the card: (1) It governs only the functions that stay Boolean after the protocol split, the pure gates (58 on the card's line); the type (i) sites, an unmet element of an offence, are unchanged. (2) A failed gate answers `JUST FALSE` where the function is a public body's power, a relief from an express bar or duty, or a gate the text closes (“so long as”, “only if”); it answers `NOTHING` where it states a company's or person's liberty, standard or privilege with no bar to relieve. (3) At the card's reading that changes 16 answers: 6 `NOTHING` to `JUST FALSE` at public bodies, and 10 `JUST FALSE` to `NOTHING` at liberties (C024, C046, C084, C115, C135, C138, C154, C155, C157, C159), each a fork line with the other reading and each borderline, because a relief and a liberty are a judgment. The 10 liberties that already answered `NOTHING` stay. (4) Applied one commit per part, each “assumed, not ruled” until the card was marked, flipping the branch each site's tag marks. (5) The difference between an express bar and silence stays in the code's `FALSE-kind` and `NOTHING-kind` comments and in NOTES, which is the provenance channel, and not in the truth value. (6) Recorded in this guide, with limit 3 of the grant ruling above replaced for the Singapore rows, and in the `NOTES.md` of the parts that carry limit 3 (the card's own wording; this paragraph is that record). (7) The ruling reaches the two Singapore encodings only. The UK (164 listed sites) and Israel stay on the Guide as it stands until Meng rules; until then the differential compares Singapore under C with the UK under limit 3. The sites the 16 answers belong to: the public-body powers that went from `NOTHING` to `JUST FALSE` are s 173F (C045), s 32(4) (C106), s 139(6) (F018), s 139(10) (F019), s 282AA(1) (F057), s 281(1) (F062); the liberties that went from `JUST FALSE` to `NOTHING` are s 145(1), s 202A(2), s 21(7), s 130(2), s 173J(3), s 179(2), s 387A(1), s 387B(1), s 387D, s 390(1). Meng's note, verbatim: “Suggest that the changed encodings, and future rules encoded under this ruling, be marked with a greppable string like 2026S1bC to show where this rule took effect. Then in future we can revisit and review the consequences of this rule on encodings that haven’t been done today.” Marked 2026-11-21T12:17:37.989Z (accept, option C, not blind), ruled 2026-11-21, so the commits that applied it are ruled and no longer “assumed, not ruled”. Reading of the note (assumed, not ruled): each function this ruling changed, and each function encoded later under it in these two encodings, carries the string `2026S1bC` in its `FALSE-kind` or `NOTHING-kind` comment, and on its `FORK` line where it has one, so that `grep -rn 2026S1bC` lists where the rule took effect and a later review can find its consequences. Bench: https://claude.ai/artifact/SYSny5zjFYHHcMFeNYi5RX

Sites of this part changed under it (2026S1bC): s 145(1), `s 145(1) the sole director may also be the sole member of the company` (fork SII-01, `sgb1-s145-directors.l4:49`), from `JUST FALSE` to `NOTHING`: a liberty with no bar to relieve.
