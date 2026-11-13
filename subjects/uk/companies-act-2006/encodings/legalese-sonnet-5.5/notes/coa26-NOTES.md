# NOTES: the Companies Act 2006 (United Kingdom), Part 42 (Statutory Auditors), ss 1209 to 1238 (coa26)

Part agent `coa26`, run `dst-coa26`. Lines 16996-17517 of `ukpga-2006-46.txt` (522 lines, 9,923 words). Encoded in L4 for the stable binary: target `main`, written and run with 1.6.110 (main, e51181d, 2026-11-11) and compared with 1.6.109.
This file follows `BRIEF.md` for coa26; where the keel's `PLAN.md` and the brief differ, the brief governs, and they did not differ in any way that changed this part's work.

**About this text.** The source is a plain-text rendering of the Act made by a converter script from legislation.gov.uk (Open Government Licence v3.0). It is not the official text, and nothing here is "verified against the official text". Quote lines were copied by `srcrefs.py quote` and are checked against that rendering by `srcrefs.py check` and `check --strict`.

## What is encoded, and what is not

All of Part 42's Chapters 1, 2 and 3 as they fall in lines 16996-17517 (the first half of Part 42; Chapters 4 and 5 are coa27's). Layer 1 is seven modules that follow the Act's own structure; layer 2 is one seat file and one case file.
Of the 504 text units in the range, 434 are `encoded`, 34 are `fork` (each pointing at a register entry and at the rule that encodes the chosen reading), 28 are `inert` and 8 are `repealed or blank in this text`. The 28 inert rows are: the 20 Part, Chapter and cross-headings and s 1209 with its paragraphs (a) and (b) (23 rows, reason 1: not operative); and ss 1210(4), 1214(7) and 1228(7) (each a negative-resolution subsection) and s 1238 with its inserted paragraph (ka) (5 rows, reason 2: machinery, an amendment of another Act). A section row (a section's number and title) is `encoded` and names the section's functions. No unit is `out-of-scope` or `deferred`.
Provisions that address only an official (the Secretary of State, the competent authority, the Independent Supervisor, the court, a recognised body) are encoded in layer 1 for what they decide; the seat layer asks only what they mean to the person.

## Seat

The individual who is, or is about to become, a director, a company secretary or a member of a company registered under the Act, or who deals with one: in Part 42, the person who is a company's statutory auditor (or is asked to be), the person who proposes to appoint one, a firm's partner, and an Auditor General (an individual). (Assumed, not ruled: the Act is addressed to companies, so the individual is whoever stands in a company's management or ownership, or deals with it.)
`coa26-seat.l4` has 38 `@export` questions, each named "Under section N, ...", each input a yes/no, a number, a date or a choice from a list, each with an `@desc`, grouped under `§` headings in the Act's order. It calls the layer-1 rules and restates none. `coa26-cases-seat.l4` asserts an answer for every question (127 assertions).
**Direction audit (repair of 2026-11-12).** Each of the 38 seat questions was compared with the rule it returns, for direction (may / can / am I barred against the opposite) and for subject (must I against have I). One mismatch was found and repaired: s 1214(1) asked "am I barred from acting as statutory auditor for lack of independence" but returns `s 1214(1) the person may act as statutory auditor of the audited person` (JUST FALSE when one of (2), (3), (4) applies, NOTHING otherwise, never a grant). It is now `Under section 1214(1), may I act as statutory auditor of the audited person, given my relationship to it`. The answer is not negated: a bar's NOTHING and JUST FALSE are not a grant. The seven assertions in `coa26-cases-seat.l4` that called it carry the same facts and expected answers and each has a `RECONCILED 2026-11-12` comment with the original text.
**Three seat questions are not pure calls to a layer-1 rule on plain facts** (recorded as the brief requires; the answers agree with the rules on every tested fact, and a merged seat layer should replace them with calls): (1) `Under section 1224A(3)` asks the six bodies of s 1224A(2) as one yes/no fact ("it is held by a body within section 1224A(2)") and passes `JUST TRUE` or `JUST FALSE` for the input of `s 1224A(1)`, so `s 1224A(2)` is not called; (2) `Under section 1224B(1)` asks the person whether the disclosure "was in contravention of section 1224A", a conclusion that `s 1224A(3)` computes, and maps it by hand to that rule's answer (`JUST FALSE` when yes, `JUST TRUE` when no); (3) `Under section 1216(3)` asks "is the successor prohibited by section 1214(1)" as a fact and maps it by hand to `JUST FALSE` or `NOTHING` for the `s 1214(1)` answer, and splits the successor into its (a) partnership and (b) other-person limbs itself.
There is never a seat for an official, and the questions the seat does not ask are listed at the top of `coa26-seat.l4`: ss 1223 to 1225G, 1228, 1229, 1231, 1234 (except the right in subsection (6)) and 1236 address officials and bodies.
The seat asks borrowed facts (what the Friendly Societies Act, a Directive, a regulation or a Schedule says) as yes/no facts the person states, so a seat answer is `NOTHING` only where the text itself leaves the case open. The layer-1 functions take such facts as `MAYBE BOOLEAN` and pass `NOTHING` through, for the merged seat layer to wire.

## Files

| file | what |
| --- | --- |
| `coa26-support.l4`, `coa26-tests-support.l4` | three-valued helpers (`coa26 support ...`), 38 assertions |
| `coa26-ch1.l4`, `coa26-tests-ch1.l4` | ss 1209-1211, 41 assertions |
| `coa26-ch2a.l4`, `coa26-tests-ch2a.l4` | ss 1212-1216, 138 assertions and 10 `#TRACE` |
| `coa26-ch2b.l4`, `coa26-tests-ch2b.l4` | ss 1217-1222, 151 assertions |
| `coa26-ch2c.l4`, `coa26-tests-ch2c.l4` | ss 1223-1224B, 109 assertions |
| `coa26-ch2d.l4`, `coa26-tests-ch2d.l4` | ss 1225-1225G, 151 assertions |
| `coa26-ch3a.l4`, `coa26-tests-ch3a.l4` | ss 1226-1231, 93 assertions |
| `coa26-ch3b.l4`, `coa26-tests-ch3b.l4` | ss 1232-1238, 84 assertions and 5 `#TRACE` |
| `coa26-seat.l4`, `coa26-cases-seat.l4` | the seat layer, 38 questions; 127 assertions |
| `NOTES.md`, `PROGRESS.md`, `NEEDS-CORE.md` | this file; the working log; constructors wanted in the core |

`check.sh`, `srcrefs.py`, `fetch-main-l4.sh`, `coa-core.l4` and `coa-definitions.l4` are the keel's or supplied, and unchanged. The source templates and generators used to write the modules (`work/tpl`, `build.py`, `gen_info.py`, `cov.py`) are in `DEPOSIT/../work/` and are not shipped; the `.l4` files are the deposit.
Every top-level name in a `coa26-ch*` module and in the seat begins with the label of the provision it implements (`s 1213(4) ...`); the helpers in `coa26-support.l4` implement no provision and begin `coa26 support`, a prefix no other part can use. Types and constructors follow the same rule (`s 1221(1B) way the declaration specifies ...`).

## How the L4 was made (method)

1. The text of the range was read in full, and the 504 units (sections, subsections, paragraphs, subparagraphs, defined terms, headings) were listed by script (`units.py`); every one of the 522 non-blank lines falls in a unit.
2. Each provision was encoded by hand in a template, with `@@Q N M label` directives that expand to quote lines copied mechanically from the text plus an `@ref ... (src:a-b)` locator. The two families that the Act repeats word for word (ss 1223, 1223ZA, 1232 and ss 1224, 1224ZA, 1233) were generated from one script, so their wording follows the text's own and their tests were generated from the same table of cases, written by hand.
3. Expected values in the tests were written from the text before each module was run. One assertion failed on its first run (`s 1228(5)`); it was a defect in the rule (the bracketing of a `NOT`), not in the test, and the rule was repaired. No expected value was changed to match output.
4. The regulative duties (ss 1213(1), 1213(2), 1214(1), 1215(1), 1235(1), 1235(2)) are encoded as `PARTY ... MUST / SHANT ... WITHIN 0 ... HENCE ... LEST BREACH BY ... BECAUSE ...` and also as decision functions; the functions are asserted and the rules are traced.


## Coverage (coa26)

One row per unit of lines 16996-17517 (sections, subsections, paragraphs, subparagraphs, defined terms and headings), each with exactly one disposition. `encoded`: a rule, definition or table in layer-1 L4 with a test and an `@ref`; `fork`: a row that points at the fork-register entry and at the rule that encodes the chosen reading; `inert`: reason 1 (not operative: headings, the purpose clause) or 2 (machinery: negative-resolution subsections, an amendment of another Act); `repealed or blank in this text`. The L4 name is the function (or the first two functions) of the module in brackets that implements the unit; a paragraph row names the function of its subsection, and a section row (number and title) names the section's functions. The 28 `inert` rows are listed in "What is encoded, and what is not" above.

**Audit.** Text units counted: 504. Rows in the table before the encoding: 504 (every unit started as `deferred` in `work/units.json`); rows after: 504. Non-blank lines of the range: 522; lines that fall in some row: 522; lines missing: 0 (checked by script, `work/units.py` against the text). Dispositions: encoded 434, fork 34, inert 28, repealed or blank in this text 8; out-of-scope 0; deferred 0.


| unit | lines | text | disposition | L4 name or reason |
| --- | --- | --- | --- | --- |
| heading | 16996 | Part 42 — Statutory Auditors | inert | reason 1: heading, not operative |
| heading | 16997 | Chapter 1 — Introductory | inert | reason 1: heading, not operative |
| s 1209 | 16998-16999 | Main purposes of Part | inert | reason 1: purposes of the Part: a purpose clause that creates no rule |
| s 1209(a) | 17000 | to secure that only persons who are properly supervised and appropriat | inert | reason 1: purposes of the Part: a purpose clause that creates no rule |
| s 1209(b) | 17001 | to secure that audits by persons so appointed are carried out properly | inert | reason 1: purposes of the Part: a purpose clause that creates no rule |
| s 1210 | 17002 | Meaning of “statutory auditor” etc | encoded | `s 1210(1) the person is a statutory auditor` (coa26-ch1); `s 1210(1) the audit is a statutory audit` (coa26-ch1) ... |
| s 1210(1) | 17003 | In this Part “statutory auditor” means— | encoded | `s 1210(1) the person is a statutory auditor` (coa26-ch1); `s 1210(1) the audit is a statutory audit` (coa26-ch1) ... |
| s 1210(1)(a) | 17004 | a person appointed as auditor under Part 16 of this Act, | encoded | `s 1210(1) the person is a statutory auditor` (coa26-ch1); `s 1210(1) the audit is a statutory audit` (coa26-ch1) ... |
| s 1210(1)(b) | 17005 | a person appointed as auditor under section 77 of or Schedule 11 to th | encoded | `s 1210(1) the person is a statutory auditor` (coa26-ch1); `s 1210(1) the audit is a statutory audit` (coa26-ch1) ... |
| s 1210(1)(c) | 17006 | a person appointed as auditor of a friendly society under section 72 o | encoded | `s 1210(1) the person is a statutory auditor` (coa26-ch1); `s 1210(1) the audit is a statutory audit` (coa26-ch1) ... |
| s 1210(1)(c)(i) | 17007 | an insurer, or | encoded | `s 1210(1) the person is a statutory auditor` (coa26-ch1); `s 1210(1) the audit is a statutory audit` (coa26-ch1) ... |
| s 1210(1)(c)(ii) | 17008 | an issuer whose transferable securities are admitted to trading on a U | encoded | `s 1210(1) the person is a statutory auditor` (coa26-ch1); `s 1210(1) the audit is a statutory audit` (coa26-ch1) ... |
| s 1210(1)(d) | 17009 | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | repealed or blank in this text | the text shows ". . . ." in place of the provision |
| s 1210(1)(e) | 17010 | a person appointed as auditor for the purposes of regulation 5 of the  | encoded | `s 1210(1) the person is a statutory auditor` (coa26-ch1); `s 1210(1) the audit is a statutory audit` (coa26-ch1) ... |
| s 1210(1)(f) | 17011 | a person appointed as auditor of an insurance undertaking for the purp | encoded | `s 1210(1) the person is a statutory auditor` (coa26-ch1); `s 1210(1) the audit is a statutory audit` (coa26-ch1) ... |
| s 1210(1)(g) | 17012 | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | repealed or blank in this text | the text shows ". . . ." in place of the provision |
| s 1210(1)(h) | 17013-17014 | a person appointed as auditor of a prescribed person under a prescribe | encoded | `s 1210(1) the person is a statutory auditor` (coa26-ch1); `s 1210(1) the audit is a statutory audit` (coa26-ch1) ... |
| s 1210(2) | 17015 | In this Part “audited person” means the person in respect of whom a st | encoded | `s 1210(2) the person is an audited person` (coa26-ch1) |
| s 1210(3) | 17016-17017 | In subsection (1)— | encoded | `s 1210(3) the body is a friendly society` (coa26-ch1); `s 1210(3) the person is an insurer` (coa26-ch1) ... |
| s 1210(3) term friendly society | 17018-17019 | “friendly society” means a friendly society within the meaning of the  | encoded | `s 1210(3) the body is a friendly society` (coa26-ch1) |
| s 1210(3) term insurer | 17020 | “insurer” means a person who would be an insurance undertaking, as def | encoded | `s 1210(3) the person is an insurer` (coa26-ch1) |
| s 1210(3) term issuer | 17021 | “issuer” has the same meaning as in Part 6 of the Financial Services a | encoded | `s 1210(3) the person is an issuer` (coa26-ch1) |
| s 1210(3) term prescribed | 17022-17023 | “prescribed” means prescribed, or of a description prescribed, by orde | encoded | `s 1210(3) the matter is prescribed` (coa26-ch1) |
| s 1210(4) | 17024 | An order under this section is subject to negative resolution procedur | inert | reason 2: machinery: an order is subject to negative resolution procedure |
| s 1211 | 17025-17026 | Eligibility for appointment as a statutory auditor: overview | fork | F20 -> `s 1211 the person is eligible for appointment as a statutory auditor` (coa26-ch1) |
| s 1211(a) | 17027 | by virtue of Chapter 2 (individuals and firms), or | encoded | `s 1211 the person is eligible for appointment as a statutory auditor` (coa26-ch1) |
| s 1211(b) | 17028 | by virtue of Chapter 3 (Comptroller and Auditor General, etc). | encoded | `s 1211 the person is eligible for appointment as a statutory auditor` (coa26-ch1) |
| heading | 17029 | Chapter 2 — Individuals and firms | inert | reason 1: heading, not operative |
| heading | 17030 | Eligibility for appointment | inert | reason 1: heading, not operative |
| s 1212 | 17031 | Individuals and firms: eligibility for appointment as a statutory audi | encoded | `s 1212(1) the individual or firm is eligible for appointment as a statutory auditor` (coa26-ch2a); `s 1212(2) the person's eligibility for appointment as a statutory auditor is restricted as mentioned in section 1222` (coa26-ch2a) |
| s 1212(1) | 17032 | An individual or firm is eligible for appointment as a statutory audit | fork | F11 -> `s 1212(1) the individual or firm is eligible for appointment as a statutory auditor` (coa26-ch2a) |
| s 1212(1)(a) | 17033 | is a member of a recognised supervisory body, and | encoded | `s 1212(1) the individual or firm is eligible for appointment as a statutory auditor` (coa26-ch2a) |
| s 1212(1)(b) | 17034 | is eligible for appointment under the rules of that body. | encoded | `s 1212(1) the individual or firm is eligible for appointment as a statutory auditor` (coa26-ch2a) |
| s 1212(2) | 17035 | In the cases to which section 1222 applies (individuals retaining only | encoded | `s 1212(2) the person's eligibility for appointment as a statutory auditor is restricted as mentioned in section 1222` (coa26-ch2a) |
| s 1213 | 17036 | Effect of ineligibility | encoded | `s 1213(1) the person may act as statutory auditor of an audited person` (coa26-ch2a); `s 1213(1) acts as statutory auditor of the audited person` (coa26-ch2a) ... |
| s 1213(1) | 17037 | No person may act as statutory auditor of an audited person if he is i | encoded | `s 1213(1) the person may act as statutory auditor of an audited person` (coa26-ch2a); `s 1213(1) acts as statutory auditor of the audited person` (coa26-ch2a) ... |
| s 1213(2) | 17038 | If at any time during his term of office a statutory auditor becomes i | fork | F8 -> `s 1213(2) the statutory auditor must immediately resign and give notice` (coa26-ch2a); `s 1213(2) the duty of a statutory auditor who becomes ineligible` (coa26-ch2a) |
| s 1213(2)(a) | 17039 | resign his office (with immediate effect), and | encoded | `s 1213(2)(a) resigns his office with immediate effect` (coa26-ch2a) |
| s 1213(2)(b) | 17040 | give notice in writing to the audited person that he has resigned by r | encoded | `s 1213(2)(b) gives notice in writing that he has resigned by reason of his becoming ineligible` (coa26-ch2a) |
| s 1213(3) | 17041 | A person is guilty of an offence if— | encoded | `s 1213(3) the person is guilty of an offence` (coa26-ch2a) |
| s 1213(3)(a) | 17042 | he acts as a statutory auditor in contravention of subsection (1), or | encoded | `s 1213(3) the person is guilty of an offence` (coa26-ch2a) |
| s 1213(3)(b) | 17043 | he fails to give the notice mentioned in paragraph (b) of subsection ( | encoded | `s 1213(3) the person is guilty of an offence` (coa26-ch2a) |
| s 1213(4) | 17044 | A person guilty of an offence under subsection (3) is liable— | encoded | `s 1213(4) the penalty for an offence under subsection (3)` (coa26-ch2a); `s 1213(4) the most the person can be fined, in pounds` (coa26-ch2a) |
| s 1213(4)(a) | 17045 | on conviction on indictment, to a fine; | encoded | `s 1213(4) the penalty for an offence under subsection (3)` (coa26-ch2a); `s 1213(4) the most the person can be fined, in pounds` (coa26-ch2a) |
| s 1213(4)(b) | 17046 | on summary conviction, to a fine not exceeding the statutory maximum. | encoded | `s 1213(4) the penalty for an offence under subsection (3)` (coa26-ch2a); `s 1213(4) the most the person can be fined, in pounds` (coa26-ch2a) |
| s 1213(5) | 17047 | A person is guilty of an offence if— | encoded | `s 1213(5) the person is guilty of an offence` (coa26-ch2a) |
| s 1213(5)(a) | 17048 | he has been convicted of an offence under subsection (3)(a) or this su | encoded | `s 1213(5) the person is guilty of an offence` (coa26-ch2a) |
| s 1213(5)(b) | 17049 | he continues to act as a statutory auditor in contravention of subsect | encoded | `s 1213(5) the person is guilty of an offence` (coa26-ch2a) |
| s 1213(6) | 17050 | A person is guilty of an offence if— | encoded | `s 1213(6) the person is guilty of an offence` (coa26-ch2a) |
| s 1213(6)(a) | 17051 | he has been convicted of an offence under subsection (3)(b) or this su | encoded | `s 1213(6) the person is guilty of an offence` (coa26-ch2a) |
| s 1213(6)(b) | 17052 | he continues, after the conviction, to fail to give the notice mention | encoded | `s 1213(6) the person is guilty of an offence` (coa26-ch2a) |
| s 1213(7) | 17053 | A person guilty of an offence under subsection (5) or (6) is liable— | fork | F1 -> `s 1213(7) the penalty for an offence under subsection (5) or (6)` (coa26-ch2a) |
| s 1213(7)(a) | 17054 | on conviction on indictment, to a fine; | encoded | `s 1213(7) the penalty for an offence under subsection (5) or (6)` (coa26-ch2a) |
| s 1213(7)(b) | 17055 | on summary conviction, to a fine not exceeding one-tenth of the statut | encoded | `s 1213(7) the penalty for an offence under subsection (5) or (6)` (coa26-ch2a) |
| s 1213(8) | 17056 | In proceedings against a person for an offence under this section it i | encoded | `s 1213(8) the defence is made out` (coa26-ch2a) |
| heading | 17057 | Independence requirement | inert | reason 1: heading, not operative |
| s 1214 | 17058 | Independence requirement | encoded | `s 1214(5) the position counts as that of an officer or employee of the audited person for the purposes of subsections (2) and (3)` (coa26-ch2a); `s 1214(2) this subsection applies to the person` (coa26-ch2a) ... |
| s 1214(1) | 17059 | A person may not act as statutory auditor of an audited person if one  | encoded | `s 1214(1) the person may act as statutory auditor of the audited person` (coa26-ch2a); `s 1214(1) acts as statutory auditor of the audited person` (coa26-ch2a) ... |
| s 1214(2) | 17060 | This subsection applies if the person is— | encoded | `s 1214(2) this subsection applies to the person` (coa26-ch2a) |
| s 1214(2)(a) | 17061 | an officer or employee of the audited person, or | encoded | `s 1214(2) this subsection applies to the person` (coa26-ch2a) |
| s 1214(2)(b) | 17062 | a partner or employee of such a person, or a partnership of which such | encoded | `s 1214(2) this subsection applies to the person` (coa26-ch2a) |
| s 1214(3) | 17063 | This subsection applies if the person is— | fork | F2 -> `s 1214(3) this subsection applies to the person` (coa26-ch2a) |
| s 1214(3)(a) | 17064 | an officer or employee of an associated undertaking of the audited per | encoded | `s 1214(3) this subsection applies to the person` (coa26-ch2a) |
| s 1214(3)(b) | 17065 | a partner or employee of such a person, or a partnership of which such | encoded | `s 1214(3) this subsection applies to the person` (coa26-ch2a) |
| s 1214(4) | 17066 | This subsection applies if there exists, between— | encoded | `s 1214(4) this subsection applies to the person` (coa26-ch2a) |
| s 1214(4)(a) | 17067 | the person or an associate of his, and | encoded | `s 1214(4) this subsection applies to the person` (coa26-ch2a) |
| s 1214(4)(b) | 17068-17069 | the audited person or an associated undertaking of the audited person, | encoded | `s 1214(4) this subsection applies to the person` (coa26-ch2a) |
| s 1214(5) | 17070 | An auditor of an audited person is not to be regarded as an officer or | fork | F2 -> `s 1214(5) the position counts as that of an officer or employee of the audited person for the purposes of subsections (2) and (3)` (coa26-ch2a) |
| s 1214(6) | 17071 | In this section “associated undertaking”, in relation to an audited pe | encoded | `s 1214(6) the undertaking is an associated undertaking of the audited person` (coa26-ch2a) |
| s 1214(6)(a) | 17072 | a parent undertaking or subsidiary undertaking of the audited person,  | encoded | `s 1214(6) the undertaking is an associated undertaking of the audited person` (coa26-ch2a) |
| s 1214(6)(b) | 17073 | a subsidiary undertaking of a parent undertaking of the audited person | encoded | `s 1214(6) the undertaking is an associated undertaking of the audited person` (coa26-ch2a) |
| s 1214(7) | 17074 | Regulations under subsection (4) are subject to negative resolution pr | inert | reason 2: machinery: regulations under subsection (4) are subject to negative resolution procedure |
| s 1215 | 17075 | Effect of lack of independence | encoded | `s 1215(1) the statutory auditor must immediately resign and give notice` (coa26-ch2a); `s 1215(1) the duty of a statutory auditor who becomes prohibited from acting` (coa26-ch2a) ... |
| s 1215(1) | 17076 | If at any time during his term of office a statutory auditor becomes p | fork | F8 -> `s 1215(1) the statutory auditor must immediately resign and give notice` (coa26-ch2a); `s 1215(1) the duty of a statutory auditor who becomes prohibited from acting` (coa26-ch2a) |
| s 1215(1)(a) | 17077 | resign his office (with immediate effect), and | encoded | `s 1215(1)(a) resigns his office with immediate effect` (coa26-ch2a) |
| s 1215(1)(b) | 17078 | give notice in writing to the audited person that he has resigned by r | encoded | `s 1215(1)(b) gives notice in writing that he has resigned by reason of his lack of independence` (coa26-ch2a) |
| s 1215(2) | 17079 | A person is guilty of an offence if— | encoded | `s 1215(2) the person is guilty of an offence` (coa26-ch2a) |
| s 1215(2)(a) | 17080 | he acts as a statutory auditor in contravention of section 1214(1), or | encoded | `s 1215(2) the person is guilty of an offence` (coa26-ch2a) |
| s 1215(2)(b) | 17081 | he fails to give the notice mentioned in paragraph (b) of subsection ( | encoded | `s 1215(2) the person is guilty of an offence` (coa26-ch2a) |
| s 1215(3) | 17082 | A person guilty of an offence under subsection (2) is liable— | encoded | `s 1215(3) the penalty for an offence under subsection (2)` (coa26-ch2a) |
| s 1215(3)(a) | 17083 | on conviction on indictment, to a fine; | encoded | `s 1215(3) the penalty for an offence under subsection (2)` (coa26-ch2a) |
| s 1215(3)(b) | 17084 | on summary conviction, to a fine not exceeding the statutory maximum. | encoded | `s 1215(3) the penalty for an offence under subsection (2)` (coa26-ch2a) |
| s 1215(4) | 17085 | A person is guilty of an offence if— | encoded | `s 1215(4) the person is guilty of an offence` (coa26-ch2a) |
| s 1215(4)(a) | 17086 | he has been convicted of an offence under subsection (2)(a) or this su | encoded | `s 1215(4) the person is guilty of an offence` (coa26-ch2a) |
| s 1215(4)(b) | 17087 | he continues to act as a statutory auditor in contravention of section | encoded | `s 1215(4) the person is guilty of an offence` (coa26-ch2a) |
| s 1215(5) | 17088 | A person is guilty of an offence if— | encoded | `s 1215(5) the person is guilty of an offence` (coa26-ch2a) |
| s 1215(5)(a) | 17089 | he has been convicted of an offence under subsection (2)(b) or this su | encoded | `s 1215(5) the person is guilty of an offence` (coa26-ch2a) |
| s 1215(5)(b) | 17090 | after the conviction, he continues to fail to give the notice mentione | encoded | `s 1215(5) the person is guilty of an offence` (coa26-ch2a) |
| s 1215(6) | 17091 | A person guilty of an offence under subsection (4) or (5) is liable— | fork | F1 -> `s 1215(6) the penalty for an offence under subsection (4) or (5)` (coa26-ch2a) |
| s 1215(6)(a) | 17092 | on conviction on indictment, to a fine; | encoded | `s 1215(6) the penalty for an offence under subsection (4) or (5)` (coa26-ch2a) |
| s 1215(6)(b) | 17093 | on summary conviction, to a fine not exceeding one-tenth of the statut | encoded | `s 1215(6) the penalty for an offence under subsection (4) or (5)` (coa26-ch2a) |
| s 1215(7) | 17094 | In proceedings against a person for an offence under this section it i | encoded | `s 1215(7) the defence is made out` (coa26-ch2a) |
| heading | 17095 | Effect of appointment of a partnership | inert | reason 1: heading, not operative |
| s 1216 | 17096 | Effect of appointment of a partnership | encoded | `s 1216(1) this section applies` (coa26-ch2a); `s 1216(2) the appointment is an appointment of the partnership as such and not of the partners` (coa26-ch2a) ... |
| s 1216(1) | 17097 | This section applies where a partnership constituted under the law of— | encoded | `s 1216(1) this section applies` (coa26-ch2a) |
| s 1216(1)(a) | 17098 | England and Wales, | encoded | `s 1216(1) this section applies` (coa26-ch2a) |
| s 1216(1)(b) | 17099 | Northern Ireland, or | encoded | `s 1216(1) this section applies` (coa26-ch2a) |
| s 1216(1)(c) | 17100-17101 | any other country or territory in which a partnership is not a legal p | encoded | `s 1216(1) this section applies` (coa26-ch2a) |
| s 1216(2) | 17102 | Unless a contrary intention appears, the appointment is an appointment | fork | F9 -> `s 1216(2) the appointment is an appointment of the partnership as such and not of the partners` (coa26-ch2a) |
| s 1216(3) | 17103 | Where the partnership ceases, the appointment is to be treated as exte | fork | F16 -> `s 1216(3) the appointment is treated as extending to the successor` (coa26-ch2a) |
| s 1216(3)(a) | 17104 | any appropriate partnership which succeeds to the practice of that par | encoded | `s 1216(3) the appointment is treated as extending to the successor` (coa26-ch2a) |
| s 1216(3)(b) | 17105 | any other appropriate person who succeeds to that practice having prev | encoded | `s 1216(3) the appointment is treated as extending to the successor` (coa26-ch2a) |
| s 1216(4) | 17106 | For the purposes of subsection (3)— | encoded | `s 1216(4)(a) the partnership is regarded as succeeding to the practice of the former partnership` (coa26-ch2a); `s 1216(4)(b) the partnership or other person is regarded as succeeding to the practice of the former partnership` (coa26-ch2a) |
| s 1216(4)(a) | 17107 | a partnership is to be regarded as succeeding to the practice of anoth | encoded | `s 1216(4)(a) the partnership is regarded as succeeding to the practice of the former partnership` (coa26-ch2a) |
| s 1216(4)(b) | 17108 | a partnership or other person is to be regarded as succeeding to the p | encoded | `s 1216(4)(b) the partnership or other person is regarded as succeeding to the practice of the former partnership` (coa26-ch2a) |
| s 1216(5) | 17109 | Where the partnership ceases and the appointment is not treated under  | encoded | `s 1216(5) the appointment may be treated as extending to the successor` (coa26-ch2a) |
| s 1216(5)(a) | 17110 | the business of the former partnership, or | encoded | `s 1216(5) the appointment may be treated as extending to the successor` (coa26-ch2a) |
| s 1216(5)(b) | 17111 | such part of it as is agreed by the audited person is to be treated as | encoded | `s 1216(5) the appointment may be treated as extending to the successor` (coa26-ch2a) |
| s 1216(6) | 17112 | For the purposes of this section, a partnership or other person is “ap | encoded | `s 1216(6) the partnership or other person is appropriate` (coa26-ch2a) |
| s 1216(6)(a) | 17113 | is eligible for appointment as a statutory auditor by virtue of this C | encoded | `s 1216(6) the partnership or other person is appropriate` (coa26-ch2a) |
| s 1216(6)(b) | 17114 | is not prohibited by section 1214(1) from acting as statutory auditor  | encoded | `s 1216(6) the partnership or other person is appropriate` (coa26-ch2a) |
| heading | 17115 | Supervisory bodies | inert | reason 1: heading, not operative |
| s 1217 | 17116 | Supervisory bodies | encoded | `s 1217(1) the body is a supervisory body` (coa26-ch2b); `s 1217(1A) the specified rules of Schedule 10 must also be binding on the person` (coa26-ch2b) ... |
| s 1217(1) | 17117 | In this Part a “supervisory body” means a body established in the Unit | encoded | `s 1217(1) the body is a supervisory body` (coa26-ch2b) |
| s 1217(1)(a) | 17118 | the eligibility of persons for appointment as a statutory auditor, and | encoded | `s 1217(1) the body is a supervisory body` (coa26-ch2b) |
| s 1217(1)(b) | 17119-17120 | the conduct of statutory audit work, | encoded | `s 1217(1) the body is a supervisory body` (coa26-ch2b) |
| s 1217(1A) | 17121 | The rules referred to in paragraphs 9(1A) and 10C(3) (bar on appointme | encoded | `s 1217(1A) the specified rules of Schedule 10 must also be binding on the person` (coa26-ch2b) |
| s 1217(1A)(a) | 17122 | have sought appointment or acted as a statutory auditor, and | encoded | `s 1217(1A) the specified rules of Schedule 10 must also be binding on the person` (coa26-ch2b) |
| s 1217(1A)(b) | 17123 | have been members of the body at any time after the commencement of th | encoded | `s 1217(1A) the specified rules of Schedule 10 must also be binding on the person` (coa26-ch2b) |
| s 1217(2) | 17124 | In this Part references to the members of a supervisory body are to th | encoded | `s 1217(2) the person is a member of the supervisory body` (coa26-ch2b) |
| s 1217(3) | 17125-17126 | In this Part references to the rules of a supervisory body are to the  | encoded | `s 1217(3) the rule is a rule of the supervisory body` (coa26-ch2b); `s 1217(3) the rule on admission or expulsion is included among the rules of the supervisory body` (coa26-ch2b) |
| s 1217(4) | 17127 | Schedule 10 has effect with respect to the recognition of supervisory  | fork | F13 -> `s 1217(4) the supervisory body is a recognised supervisory body for the purposes of Part 42` (coa26-ch2b) |
| s 1218 | 17128 | Exemption from liability for damages | encoded | `s 1218(2) the person is within subsection (2)` (coa26-ch2b); `s 1218(3) subsection (1) applies to the function of the recognised supervisory body` (coa26-ch2b) ... |
| s 1218(1) | 17129 | No person within subsection (2) is to be liable in damages for anythin | fork | F6 -> `s 1218(1) the person is liable in damages for anything done or omitted in the discharge or purported discharge of the function` (coa26-ch2b) |
| s 1218(2) | 17130 | The persons within this subsection are— | fork | F6 -> `s 1218(2) the person is within subsection (2)` (coa26-ch2b) |
| s 1218(2)(a) | 17131 | any recognised supervisory body, | encoded | `s 1218(2) the person is within subsection (2)` (coa26-ch2b) |
| s 1218(2)(b) | 17132 | any officer or employee of a recognised supervisory body, and | encoded | `s 1218(2) the person is within subsection (2)` (coa26-ch2b) |
| s 1218(2)(c) | 17133 | any member of the governing body of a recognised supervisory body. | encoded | `s 1218(2) the person is within subsection (2)` (coa26-ch2b) |
| s 1218(3) | 17134 | Subsection (1) applies to the functions of a recognised supervisory bo | encoded | `s 1218(3) subsection (1) applies to the function of the recognised supervisory body` (coa26-ch2b) |
| s 1218(3)(a) | 17135 | rules, practices, powers and arrangements of the body to which the req | encoded | `s 1218(3) subsection (1) applies to the function of the recognised supervisory body` (coa26-ch2b) |
| s 1218(3)(b) | 17136 | the obligations with which paragraph 20 of that Schedule requires the  | encoded | `s 1218(3) subsection (1) applies to the function of the recognised supervisory body` (coa26-ch2b) |
| s 1218(3)(c) | 17137 | any guidance issued by the body; | encoded | `s 1218(3) subsection (1) applies to the function of the recognised supervisory body` (coa26-ch2b) |
| s 1218(3)(d) | 17138 | the obligations imposed on the body by or by virtue of this Part or by | encoded | `s 1218(3) subsection (1) applies to the function of the recognised supervisory body` (coa26-ch2b) |
| s 1218(3)(e) | 17139 | the obligations imposed on the body by or by virtue of the Audit Regul | encoded | `s 1218(3) subsection (1) applies to the function of the recognised supervisory body` (coa26-ch2b) |
| s 1218(4) | 17140 | The reference in subsection (3)(c) to guidance issued by a recognised  | encoded | `s 1218(4) the guidance is guidance issued by the recognised supervisory body` (coa26-ch2b); `s 1218(4) the guidance on admission or expulsion is included as guidance issued by the recognised supervisory body` (coa26-ch2b) |
| s 1218(4)(a) | 17141 | issued or made by it to all or any class of its members or persons see | encoded | `s 1218(4) the guidance is guidance issued by the recognised supervisory body` (coa26-ch2b); `s 1218(4) the guidance on admission or expulsion is included as guidance issued by the recognised supervisory body` (coa26-ch2b) |
| s 1218(4)(b) | 17142-17143 | relevant for the purposes of this Part , the Statutory Auditors and Th | encoded | `s 1218(4) the guidance is guidance issued by the recognised supervisory body` (coa26-ch2b); `s 1218(4) the guidance on admission or expulsion is included as guidance issued by the recognised supervisory body` (coa26-ch2b) |
| s 1218(5) | 17144 | Subsection (1) does not apply— | encoded | `s 1218(5) subsection (1) does not apply to the act or omission` (coa26-ch2b) |
| s 1218(5)(a) | 17145 | if the act or omission is shown to have been in bad faith, or | encoded | `s 1218(5) subsection (1) does not apply to the act or omission` (coa26-ch2b) |
| s 1218(5)(b) | 17146 | so as to prevent an award of damages in respect of the act or omission | encoded | `s 1218(5) subsection (1) does not apply to the act or omission` (coa26-ch2b) |
| heading | 17147 | Professional qualifications | inert | reason 1: heading, not operative |
| s 1219 | 17148 | Appropriate qualifications | encoded | `s 1219(2) the person is within this subsection` (coa26-ch2b); `s 1219(1) the person holds an appropriate qualification` (coa26-ch2b) |
| s 1219(1) | 17149 | A person holds an appropriate qualification for the purposes of this C | encoded | `s 1219(1) the person holds an appropriate qualification` (coa26-ch2b) |
| s 1219(1)(a) | 17150 | he holds a recognised professional qualification obtained in the Unite | encoded | `s 1219(1) the person holds an appropriate qualification` (coa26-ch2b) |
| s 1219(1)(b) | 17151 | immediately before the commencement of this Chapter, he— | encoded | `s 1219(1) the person holds an appropriate qualification` (coa26-ch2b) |
| s 1219(1)(b)(i) | 17152 | held an appropriate qualification for the purposes of Part 2 of the Co | encoded | `s 1219(1) the person holds an appropriate qualification` (coa26-ch2b) |
| s 1219(1)(b)(ii) | 17153 | was treated as holding an appropriate qualification for those purposes | encoded | `s 1219(1) the person holds an appropriate qualification` (coa26-ch2b) |
| s 1219(1)(c) | 17154 | immediately before the commencement of this Chapter, he— | encoded | `s 1219(1) the person holds an appropriate qualification` (coa26-ch2b) |
| s 1219(1)(c)(i) | 17155 | held an appropriate qualification for the purposes of Part III of the  | encoded | `s 1219(1) the person holds an appropriate qualification` (coa26-ch2b) |
| s 1219(1)(c)(ii) | 17156 | was treated as holding an appropriate qualification for those purposes | encoded | `s 1219(1) the person holds an appropriate qualification` (coa26-ch2b) |
| s 1219(1)(d) | 17157 | he is within subsection (2), or | encoded | `s 1219(1) the person holds an appropriate qualification` (coa26-ch2b) |
| s 1219(1)(e) | 17158 | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | repealed or blank in this text | the text shows ". . . ." in place of the provision |
| s 1219(1)(f) | 17159 | subject to any direction under section 1221(5), he is regarded for the | fork | F12 -> `s 1219(1) the person holds an appropriate qualification` (coa26-ch2b) |
| s 1219(2) | 17160 | A person is within this subsection if— | encoded | `s 1219(2) the person is within this subsection` (coa26-ch2b) |
| s 1219(2)(a) | 17161 | before 1st January 1990, he began a course of study or practical train | encoded | `s 1219(2) the person is within this subsection` (coa26-ch2b) |
| s 1219(2)(b) | 17162 | he obtained that qualification on or after 1st January 1990 and before | encoded | `s 1219(2) the person is within this subsection` (coa26-ch2b) |
| s 1219(2)(c) | 17163 | the Secretary of State approved his qualification before 1st October 2 | encoded | `s 1219(2) the person is within this subsection` (coa26-ch2b) |
| s 1219(3) | 17164 | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | repealed or blank in this text | the text shows ". . . ." in place of the provision |
| s 1220 | 17165 | Qualifying bodies and recognised professional qualifications | encoded | `s 1220(1) the body is a qualifying body` (coa26-ch2b); `s 1220(2) the rule is a rule of the qualifying body` (coa26-ch2b) ... |
| s 1220(1) | 17166 | In this Part a “qualifying body” means a body established in the Unite | encoded | `s 1220(1) the body is a qualifying body` (coa26-ch2b) |
| s 1220(2) | 17167-17168 | In this Part references to the rules of a qualifying body are to the r | encoded | `s 1220(2) the rule is a rule of the qualifying body` (coa26-ch2b); `s 1220(2) the rule is included among the rules of the qualifying body` (coa26-ch2b) |
| s 1220(2)(a) | 17169 | admission to or expulsion from a course of study leading to a qualific | encoded | `s 1220(2) the rule is a rule of the qualifying body` (coa26-ch2b); `s 1220(2) the rule is included among the rules of the qualifying body` (coa26-ch2b) |
| s 1220(2)(b) | 17170 | the award or deprivation of a qualification, or | encoded | `s 1220(2) the rule is a rule of the qualifying body` (coa26-ch2b); `s 1220(2) the rule is included among the rules of the qualifying body` (coa26-ch2b) |
| s 1220(2)(c) | 17171 | the approval of a person for the purposes of giving practical training | encoded | `s 1220(2) the rule is a rule of the qualifying body` (coa26-ch2b); `s 1220(2) the rule is included among the rules of the qualifying body` (coa26-ch2b) |
| s 1220(3) | 17172 | Schedule 11 has effect with respect to the recognition for the purpose | fork | F13 -> `s 1220(3) the professional qualification is a recognised professional qualification for the purposes of Part 42` (coa26-ch2b) |
| s 1221 | 17173 | Approval of third country qualifications | encoded | `s 1221(3) the condition for making a declaration under subsection (1) is met` (coa26-ch2b); `s 1221(4) the condition for making a declaration under subsection (1) is met` (coa26-ch2b) ... |
| s 1221(1) | 17174 | The Secretary of State may declare that the following are to be regard | fork | F7 -> `s 1221(1) the Secretary of State may declare that the persons are regarded as holding an approved third country qualification` (coa26-ch2b) |
| s 1221(1)(a) | 17175 | persons who are qualified to audit accounts under the law of a specifi | encoded | `s 1221(1) the Secretary of State may declare that the persons are regarded as holding an approved third country qualification` (coa26-ch2b) |
| s 1221(1)(b) | 17176 | persons who hold a specified professional qualification in accountancy | encoded | `s 1221(1) the Secretary of State may declare that the persons are regarded as holding an approved third country qualification` (coa26-ch2b) |
| s 1221(1A) | 17177 | A declaration under subsection (1)(a) or (b) must contain provision to | encoded | `s 1221(1A) the person may be regarded as holding an approved third country qualification` (coa26-ch2b) |
| s 1221(1A)(a) | 17178 | already holds a professional qualification which— | encoded | `s 1221(1A) the person may be regarded as holding an approved third country qualification` (coa26-ch2b) |
| s 1221(1A)(a)(i) | 17179 | covers subjects and skills which are the same or substantially the sam | encoded | `s 1221(1A) the person may be regarded as holding an approved third country qualification` (coa26-ch2b) |
| s 1221(1A)(a)(ii) | 17180 | demonstrates knowledge of those subjects and skills to the same or sub | encoded | `s 1221(1A) the person may be regarded as holding an approved third country qualification` (coa26-ch2b) |
| s 1221(1A)(b) | 17181 | holds a professional qualification which does not comply with paragrap | encoded | `s 1221(1A) the person may be regarded as holding an approved third country qualification` (coa26-ch2b) |
| s 1221(1B) | 17182 | The declaration must specify that the condition in subsection (1A)(b)  | encoded | `s 1221(1B) the person has met the requirement the declaration specifies` (coa26-ch2b) |
| s 1221(1B)(a) | 17183 | only by passing an aptitude test in accordance with subsection (7A), | encoded | `s 1221(1B) the person has met the requirement the declaration specifies` (coa26-ch2b) |
| s 1221(1B)(b) | 17184 | only by completing an adaptation period in accordance with subsections | encoded | `s 1221(1B) the person has met the requirement the declaration specifies` (coa26-ch2b) |
| s 1221(1B)(c) | 17185 | either by passing an aptitude test in accordance with subsection (7A)  | encoded | `s 1221(1B) the person has met the requirement the declaration specifies` (coa26-ch2b) |
| s 1221(2) | 17186 | A declaration under subsection (1)(b) may be expressed to be subject t | encoded | `s 1221(2) the declaration may be expressed to be subject to the satisfaction of the requirement` (coa26-ch2b) |
| s 1221(3) | 17187 | The Secretary of State may make a declaration under subsection (1) onl | encoded | `s 1221(3) the condition for making a declaration under subsection (1) is met` (coa26-ch2b) |
| s 1221(3)(a) | 17188 | in the case of a declaration under subsection (1)(a), the fact that th | encoded | `s 1221(3) the condition for making a declaration under subsection (1) is met` (coa26-ch2b) |
| s 1221(3)(b) | 17189-17190 | in the case of a declaration under subsection (1)(b), the specified pr | encoded | `s 1221(3) the condition for making a declaration under subsection (1) is met` (coa26-ch2b) |
| s 1221(4) | 17191 | The Secretary of State may make a declaration under subsection (1) onl | encoded | `s 1221(4) the condition for making a declaration under subsection (1) is met` (coa26-ch2b) |
| s 1221(4)(a) | 17192 | in the case of a declaration under subsection (1)(a), some or all pers | encoded | `s 1221(4) the condition for making a declaration under subsection (1) is met` (coa26-ch2b) |
| s 1221(4)(b) | 17193 | in the case of a declaration under subsection (1)(b), some or all pers | encoded | `s 1221(4) the condition for making a declaration under subsection (1) is met` (coa26-ch2b) |
| s 1221(5) | 17194 | The Secretary of State may direct that persons holding an approved thi | encoded | `s 1221(5) the Secretary of State may direct that the persons are not treated as holding an appropriate qualification unless they hold the additional educational qualifications` (coa26-ch2b) |
| s 1221(6) | 17195 | The Secretary of State may give different directions in relation to di | encoded | `s 1221(6) the Secretary of State may give different directions` (coa26-ch2b) |
| s 1221(7) | 17196 | The Secretary of State may, if he thinks fit, having regard to the con | encoded | `s 1221(7) the Secretary of State may withdraw a declaration under subsection (1)` (coa26-ch2b) |
| s 1221(7)(a) | 17197 | persons becoming qualified to audit accounts under the law of the spec | encoded | `s 1221(7) the Secretary of State may withdraw a declaration under subsection (1)` (coa26-ch2b) |
| s 1221(7)(b) | 17198 | persons obtaining the specified professional qualification after such  | encoded | `s 1221(7) the Secretary of State may withdraw a declaration under subsection (1)` (coa26-ch2b) |
| s 1221(7A) | 17199 | An aptitude test required for the purposes of subsection (1B) — | encoded | `s 1221(7A) the status of the matter in an aptitude test required for the purposes of subsection (1B)` (coa26-ch2b) |
| s 1221(7A)(a) | 17200 | must test the person’s knowledge of required subjects and skills, | encoded | `s 1221(7A) the status of the matter in an aptitude test required for the purposes of subsection (1B)` (coa26-ch2b) |
| s 1221(7A)(b) | 17201 | may test the person's knowledge of rules of professional conduct; | encoded | `s 1221(7A) the status of the matter in an aptitude test required for the purposes of subsection (1B)` (coa26-ch2b) |
| s 1221(7A)(c) | 17202 | must not test the person's knowledge of any other matters. | encoded | `s 1221(7A) the status of the matter in an aptitude test required for the purposes of subsection (1B)` (coa26-ch2b) |
| s 1221(7AA) | 17203 | For the purposes of subsection (7A), a subject or skill is a required  | encoded | `s 1221(7AA) the subject or skill is a required subject or skill` (coa26-ch2b) |
| s 1221(7AA)(a) | 17204 | the professional qualification already held by the person (“the existi | encoded | `s 1221(7AA) the subject or skill is a required subject or skill` (coa26-ch2b) |
| s 1221(7AA)(b) | 17205 | the existing qualification does not demonstrate knowledge of that subj | encoded | `s 1221(7AA) the subject or skill is a required subject or skill` (coa26-ch2b) |
| s 1221(7B) | 17206 | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | repealed or blank in this text | the text shows ". . . ." in place of the provision |
| s 1221(7C) | 17207 | An adaptation period is a period, not exceeding three years, in which  | encoded | `s 1221(7C) the period is an adaptation period` (coa26-ch2b) |
| s 1221(7D) | 17208 | The adaptation period must be completed, and the ability assessment mu | encoded | `s 1221(7D) the adaptation period and the ability assessment accord with subsection (7D)` (coa26-ch2b) |
| s 1221(8) | 17209 | The Secretary of State may, if he thinks fit, having regard to the con | encoded | `s 1221(8) the Secretary of State may vary or revoke the requirement` (coa26-ch2b) |
| s 1221(9) | 17210 | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | repealed or blank in this text | the text shows ". . . ." in place of the provision |
| s 1222 | 17211 | Eligibility of individuals retaining only 1967 Act authorisation | encoded | `s 1222(2) the company is unquoted` (coa26-ch2b); `s 1222(1) the person is eligible for appointment as auditor of the company` (coa26-ch2b) ... |
| s 1222(1) | 17212 | A person whose only appropriate qualification is based on his retentio | fork | F19 -> `s 1222(1) the person is eligible for appointment as auditor of the company` (coa26-ch2b) |
| s 1222(2) | 17213 | A company is “unquoted” if, at the time of the person's appointment, n | encoded | `s 1222(2) the company is unquoted` (coa26-ch2b) |
| s 1222(3) | 17214 | References to a person eligible for appointment as a statutory auditor | encoded | `s 1222(3) the reference to a person eligible for appointment as a statutory auditor includes the person` (coa26-ch2b) |
| heading | 17215 | Information | inert | reason 1: heading, not operative |
| s 1223 | 17216 | Matters to be notified to the Secretary of State | encoded | `s 1223(1) the Secretary of State may require the body to notify or give information` (coa26-ch2c); `s 1223(2) the notice or information required is within subsection (2)` (coa26-ch2c) ... |
| s 1223(1) | 17217 | The Secretary of State may require a recognised supervisory body or a  | encoded | `s 1223(1) the Secretary of State may require the body to notify or give information` (coa26-ch2c) |
| s 1223(1)(a) | 17218 | to notify him immediately of the occurrence of such events as he may s | encoded | `s 1223(1) the Secretary of State may require the body to notify or give information` (coa26-ch2c) |
| s 1223(1)(b) | 17219 | to give him, at such times or in respect of such periods as he may spe | encoded | `s 1223(1) the Secretary of State may require the body to notify or give information` (coa26-ch2c) |
| s 1223(2) | 17220 | The notices and information required to be given must be such as the S | encoded | `s 1223(2) the notice or information required is within subsection (2)` (coa26-ch2c) |
| s 1223(3) | 17221 | The Secretary of State may require information given under this sectio | encoded | `s 1223(3) the Secretary of State may require the information to be given in a specified form or verified in a specified manner` (coa26-ch2c) |
| s 1223(4) | 17222 | Any notice or information required to be given under this section must | fork | F9 -> `s 1223(4) the notice or information must be given in writing` (coa26-ch2c) |
| s 1223ZA | 17223 | Matters to be notified to the competent authority | encoded | `s 1223ZA(1) the competent authority may require the body to notify or give information` (coa26-ch2c); `s 1223ZA(2) the notice or information required is within subsection (2)` (coa26-ch2c) ... |
| s 1223ZA(1) | 17224 | The competent authority may require a recognised supervisory body— | encoded | `s 1223ZA(1) the competent authority may require the body to notify or give information` (coa26-ch2c) |
| s 1223ZA(1)(a) | 17225 | to notify the competent authority immediately of the occurrence of suc | encoded | `s 1223ZA(1) the competent authority may require the body to notify or give information` (coa26-ch2c) |
| s 1223ZA(1)(b) | 17226 | to give the competent authority, at such times or in respect of such p | encoded | `s 1223ZA(1) the competent authority may require the body to notify or give information` (coa26-ch2c) |
| s 1223ZA(2) | 17227 | The notices and information required to be given must be such as the c | encoded | `s 1223ZA(2) the notice or information required is within subsection (2)` (coa26-ch2c) |
| s 1223ZA(3) | 17228 | The competent authority may require information given under this secti | encoded | `s 1223ZA(3) the competent authority may require the information to be given in a specified form or verified in a specified manner` (coa26-ch2c) |
| s 1223ZA(4) | 17229 | Any notice or information required to be given under this section must | fork | F9 -> `s 1223ZA(4) the notice or information must be given in writing` (coa26-ch2c) |
| s 1223A | 17230 | Notification of matters relevant to approved third country competent a | encoded | `s 1223A(3) the person is a notifiable person` (coa26-ch2c); `s 1223A(1)(a) the recognised supervisory body must notify the Secretary of State that the notifiable person has become eligible` (coa26-ch2c) ... |
| s 1223A(1) | 17231 | A recognised supervisory body must notify the Secretary of State— | encoded | `s 1223A(1)(a) the recognised supervisory body must notify the Secretary of State that the notifiable person has become eligible` (coa26-ch2c); `s 1223A(1)(b) the recognised supervisory body must notify the Secretary of State that the notifiable person's eligibility is withdrawn` (coa26-ch2c) ... |
| s 1223A(1)(a) | 17232 | if a notifiable person becomes eligible for appointment as a statutory | encoded | `s 1223A(1)(a) the recognised supervisory body must notify the Secretary of State that the notifiable person has become eligible` (coa26-ch2c) |
| s 1223A(1)(b) | 17233 | if a notifiable person’s eligibility for appointment as a statutory au | encoded | `s 1223A(1)(b) the recognised supervisory body must notify the Secretary of State that the notifiable person's eligibility is withdrawn` (coa26-ch2c) |
| s 1223A(1)(c) | 17234 | of the reasons for any such withdrawal. | encoded | `s 1223A(1)(c) the recognised supervisory body must notify the Secretary of State of the reasons for the withdrawal` (coa26-ch2c) |
| s 1223A(2) | 17235 | A recognised supervisory body must also notify the Secretary of State  | encoded | `s 1223A(2) the recognised supervisory body must notify the Secretary of State of its grounds for suspecting a contravention` (coa26-ch2c) |
| s 1223A(2)(a) | 17236 | a person has contravened the law of the United Kingdom, or an equivale | encoded | `s 1223A(2) the recognised supervisory body must notify the Secretary of State of its grounds for suspecting a contravention` (coa26-ch2c) |
| s 1223A(2)(b) | 17237 | the act or omission constituting that contravention took place on the  | encoded | `s 1223A(2) the recognised supervisory body must notify the Secretary of State of its grounds for suspecting a contravention` (coa26-ch2c) |
| s 1223A(3) | 17238 | In this section “ notifiable person ” means a member of the recognised | encoded | `s 1223A(3) the person is a notifiable person` (coa26-ch2c) |
| s 1223A(3)(a) | 17239 | who is also a third country auditor that has been approved by an appro | encoded | `s 1223A(3) the person is a notifiable person` (coa26-ch2c) |
| s 1223A(3)(b) | 17240 | in respect of whom the approved third country competent authority is n | encoded | `s 1223A(3) the person is a notifiable person` (coa26-ch2c) |
| s 1224 | 17241 | The Secretary of State's power to call for information | encoded | `s 1224(1) the Secretary of State may by notice in writing require the person to give the information` (coa26-ch2c); `s 1224(2) the person is within subsection (2)` (coa26-ch2c) ... |
| s 1224(1) | 17242 | The Secretary of State may by notice in writing require a person withi | encoded | `s 1224(1) the Secretary of State may by notice in writing require the person to give the information` (coa26-ch2c) |
| s 1224(2) | 17243 | The persons within this subsection are— | encoded | `s 1224(2) the person is within subsection (2)` (coa26-ch2c) |
| s 1224(2)(a) | 17244 | any recognised supervisory body, | encoded | `s 1224(2) the person is within subsection (2)` (coa26-ch2c) |
| s 1224(2)(b) | 17245 | any recognised qualifying body, and | encoded | `s 1224(2) the person is within subsection (2)` (coa26-ch2c) |
| s 1224(2)(c) | 17246 | any person eligible for appointment as a statutory auditor by virtue o | encoded | `s 1224(2) the person is within subsection (2)` (coa26-ch2c) |
| s 1224(3) | 17247 | The Secretary of State may require that any information which he requi | encoded | `s 1224(3) the Secretary of State may require the information to be given within a reasonable time and verified in a specified manner` (coa26-ch2c) |
| s 1224ZA | 17248 | The competent authority’s power to call for information | encoded | `s 1224ZA(1) the competent authority may by notice in writing require the person to give the information` (coa26-ch2c); `s 1224ZA(2) the competent authority may require the information to be given within a reasonable time and verified in a specified manner` (coa26-ch2c) |
| s 1224ZA(1) | 17249 | The competent authority may by notice in writing require any recognise | encoded | `s 1224ZA(1) the competent authority may by notice in writing require the person to give the information` (coa26-ch2c) |
| s 1224ZA(2) | 17250 | The competent authority may require that any information which it requ | encoded | `s 1224ZA(2) the competent authority may require the information to be given within a reasonable time and verified in a specified manner` (coa26-ch2c) |
| s 1224A | 17251 | Restrictions on disclosure | encoded | `s 1224A(2) the section applies to the body` (coa26-ch2c); `s 1224A(1) the section applies to the information` (coa26-ch2c) ... |
| s 1224A(1) | 17252 | This section applies to information (in whatever form)— | fork | F15 -> `s 1224A(1) the section applies to the information` (coa26-ch2c) |
| s 1224A(1)(a) | 17253 | relating to the private affairs of an individual, or | encoded | `s 1224A(1) the section applies to the information` (coa26-ch2c) |
| s 1224A(1)(b) | 17254-17255 | relating to any particular business, | encoded | `s 1224A(1) the section applies to the information` (coa26-ch2c) |
| s 1224A(2) | 17256 | This section applies to— | fork | F15 -> `s 1224A(2) the section applies to the body` (coa26-ch2c) |
| s 1224A(2)(a) | 17257 | a recognised supervisory body, | encoded | `s 1224A(2) the section applies to the body` (coa26-ch2c) |
| s 1224A(2)(b) | 17258 | a recognised qualifying body, | encoded | `s 1224A(2) the section applies to the body` (coa26-ch2c) |
| s 1224A(2)(c) | 17259 | the competent authority, | encoded | `s 1224A(2) the section applies to the body` (coa26-ch2c) |
| s 1224A(2)(d) | 17260 | the Independent Supervisor, | encoded | `s 1224A(2) the section applies to the body` (coa26-ch2c) |
| s 1224A(2)(e) | 17261 | the Secretary of State, and | encoded | `s 1224A(2) the section applies to the body` (coa26-ch2c) |
| s 1224A(2)(f) | 17262 | a body designated by the Secretary of State under section 1252 (delega | encoded | `s 1224A(2) the section applies to the body` (coa26-ch2c) |
| s 1224A(3) | 17263 | No such information may, during the lifetime of the individual or so l | encoded | `s 1224A(3) the information may be disclosed` (coa26-ch2c) |
| s 1224A(4) | 17264 | Subsection (3) does not apply to any disclosure of information that— | encoded | `s 1224A(4) subsection (3) does not apply to the disclosure` (coa26-ch2c) |
| s 1224A(4)(a) | 17265 | is made for the purpose of facilitating the carrying out by the body o | encoded | `s 1224A(4) subsection (3) does not apply to the disclosure` (coa26-ch2c) |
| s 1224A(4)(b) | 17266 | is made to a person specified in Part 1 of Schedule 11A, | encoded | `s 1224A(4) subsection (3) does not apply to the disclosure` (coa26-ch2c) |
| s 1224A(4)(c) | 17267 | is of a description specified in Part 2 of that Schedule, or | encoded | `s 1224A(4) subsection (3) does not apply to the disclosure` (coa26-ch2c) |
| s 1224A(4)(d) | 17268 | is made in accordance with Part 3 of that Schedule. | encoded | `s 1224A(4) subsection (3) does not apply to the disclosure` (coa26-ch2c) |
| s 1224A(5) | 17269 | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | repealed or blank in this text | the text shows ". . . ." in place of the provision |
| s 1224A(6) | 17270 | This section does not prohibit the disclosure of information if the in | encoded | `s 1224A(6) the section does not prohibit the disclosure` (coa26-ch2c) |
| s 1224A(7) | 17271 | Nothing in this section authorises the making of a disclosure in contr | encoded | `s 1224A(7) the section authorises the disclosure` (coa26-ch2c) |
| s 1224B | 17272 | Offence of disclosure in contravention of section 1224A | encoded | `s 1224B(1) the person is guilty of an offence` (coa26-ch2c); `s 1224B(2) the penalty for an offence under section 1224B` (coa26-ch2c) |
| s 1224B(1) | 17273 | A person who discloses information in contravention of section 1224A ( | fork | F9 -> `s 1224B(1) the person is guilty of an offence` (coa26-ch2c) |
| s 1224B(1)(a) | 17274 | he did not know, and had no reason to suspect, that the information ha | encoded | `s 1224B(1) the person is guilty of an offence` (coa26-ch2c) |
| s 1224B(1)(b) | 17275 | he took all reasonable steps and exercised all due diligence to avoid  | encoded | `s 1224B(1) the person is guilty of an offence` (coa26-ch2c) |
| s 1224B(2) | 17276 | A person guilty of an offence under this section is liable— | encoded | `s 1224B(2) the penalty for an offence under section 1224B` (coa26-ch2c) |
| s 1224B(2)(a) | 17277 | on conviction on indictment, to imprisonment for a term not exceeding  | encoded | `s 1224B(2) the penalty for an offence under section 1224B` (coa26-ch2c) |
| s 1224B(2)(b) | 17278 | on summary conviction— | encoded | `s 1224B(2) the penalty for an offence under section 1224B` (coa26-ch2c) |
| s 1224B(2)(b)(i) | 17279 | in Scotland, to imprisonment for a term not exceeding 12 months or to  | encoded | `s 1224B(2) the penalty for an offence under section 1224B` (coa26-ch2c) |
| s 1224B(2)(b)(ii) | 17280 | in England and Wales or Northern Ireland, to imprisonment for a term n | encoded | `s 1224B(2) the penalty for an offence under section 1224B` (coa26-ch2c) |
| heading | 17281 | Enforcement | inert | reason 1: heading, not operative |
| s 1225 | 17282 | Enforcement: general | encoded | `s 1225(1) the section applies` (coa26-ch2d); `s 1225(2) the Secretary of State may do any one or more of the things in paragraphs (a) to (c)` (coa26-ch2d) ... |
| s 1225(1) | 17283 | This section applies if at any time it appears to the Secretary of Sta | encoded | `s 1225(1) the section applies` (coa26-ch2d) |
| s 1225(1)(a) | 17284 | in the case of a recognised supervisory body, that any requirement of  | encoded | `s 1225(1) the section applies` (coa26-ch2d) |
| s 1225(1)(b) | 17285 | in the case of a recognised professional qualification offered by a re | encoded | `s 1225(1) the section applies` (coa26-ch2d) |
| s 1225(1)(c) | 17286 | that a recognised supervisory body or a recognised qualifying body has | encoded | `s 1225(1) the section applies` (coa26-ch2d) |
| s 1225(1)(d) | 17287 | that a recognised supervisory body has not complied with an obligation | encoded | `s 1225(1) the section applies` (coa26-ch2d) |
| s 1225(2) | 17288 | The Secretary of State may do any one or more of the following— | encoded | `s 1225(2) the Secretary of State may do any one or more of the things in paragraphs (a) to (c)` (coa26-ch2d) |
| s 1225(2)(a) | 17289 | give a direction to the body under section 1225A; | encoded | `s 1225(2) the Secretary of State may do any one or more of the things in paragraphs (a) to (c)` (coa26-ch2d) |
| s 1225(2)(b) | 17290 | make an application to the court in respect of the body under section  | encoded | `s 1225(2) the Secretary of State may do any one or more of the things in paragraphs (a) to (c)` (coa26-ch2d) |
| s 1225(2)(c) | 17291 | impose a financial penalty on the body under section 1225D. | encoded | `s 1225(2) the Secretary of State may do any one or more of the things in paragraphs (a) to (c)` (coa26-ch2d) |
| s 1225(3) | 17292 | Subsection (2) is without prejudice to the powers of the Secretary of  | encoded | `s 1225(3) subsection (2) is without prejudice to the power` (coa26-ch2d) |
| s 1225A | 17293 | Directions: general | encoded | `s 1225A(1) the direction is a direction under section 1225A` (coa26-ch2d); `s 1225A(2)(a) the direction may require the body to take the step` (coa26-ch2d) ... |
| s 1225A(1) | 17294 | A direction under this section is one directing a body to take such st | encoded | `s 1225A(1) the direction is a direction under section 1225A` (coa26-ch2d) |
| s 1225A(1)(a) | 17295 | secure that the requirement in question is satisfied or the obligation | encoded | `s 1225A(1) the direction is a direction under section 1225A` (coa26-ch2d) |
| s 1225A(1)(b) | 17296 | mitigate the effect, or prevent the recurrence, of the failure to sati | encoded | `s 1225A(1) the direction is a direction under section 1225A` (coa26-ch2d) |
| s 1225A(2) | 17297 | A direction under this section— | encoded | `s 1225A(2)(a) the direction may require the body to take the step` (coa26-ch2d); `s 1225A(2)(b) the direction may require the body to refrain from taking a particular course of action` (coa26-ch2d) |
| s 1225A(2)(a) | 17298 | may only require a body to take steps which it has power to take; | encoded | `s 1225A(2)(a) the direction may require the body to take the step` (coa26-ch2d) |
| s 1225A(2)(b) | 17299 | may require a body to refrain from taking a particular course of actio | encoded | `s 1225A(2)(b) the direction may require the body to refrain from taking a particular course of action` (coa26-ch2d) |
| s 1225A(3) | 17300 | The power to give a direction under this section is subject to any pro | encoded | `s 1225A(3) the power to give the direction is subject to the provision of another enactment` (coa26-ch2d) |
| s 1225A(4) | 17301 | The Secretary of State may take such steps as the Secretary of State c | encoded | `s 1225A(4) the Secretary of State may take the step` (coa26-ch2d) |
| s 1225B | 17302 | Directions: supplementary | encoded | `s 1225B(1) the notice of proposed direction was given before the direction` (coa26-ch2d); `s 1225B(2) the notice of proposed direction has the required content` (coa26-ch2d) ... |
| s 1225B(1) | 17303 | Before giving a direction to a body under section 1225A, the Secretary | encoded | `s 1225B(1) the notice of proposed direction was given before the direction` (coa26-ch2d) |
| s 1225B(2) | 17304 | A notice of proposed direction must— | encoded | `s 1225B(2) the notice of proposed direction has the required content` (coa26-ch2d) |
| s 1225B(2)(a) | 17305 | state that the Secretary of State proposes to give the body a directio | encoded | `s 1225B(2) the notice of proposed direction has the required content` (coa26-ch2d) |
| s 1225B(2)(b) | 17306 | identify the requirement or obligation in question and state why it ap | encoded | `s 1225B(2) the notice of proposed direction has the required content` (coa26-ch2d) |
| s 1225B(2)(c) | 17307 | specify a period within which the body may make written representation | encoded | `s 1225B(2) the notice of proposed direction has the required content` (coa26-ch2d) |
| s 1225B(3) | 17308 | The period specified under subsection (2)(c)— | encoded | `s 1225B(3) the period specified under subsection (2)(c) is valid` (coa26-ch2d) |
| s 1225B(3)(a) | 17309 | must begin with the date on which the notice of proposed direction is  | encoded | `s 1225B(3) the period specified under subsection (2)(c) is valid` (coa26-ch2d) |
| s 1225B(3)(b) | 17310 | must not be less than 14 days. | encoded | `s 1225B(3) the period specified under subsection (2)(c) is valid` (coa26-ch2d) |
| s 1225B(4) | 17311 | Written representations made by the body within the period specified u | encoded | `s 1225B(4) the Secretary of State has complied with the duty to consider the representations` (coa26-ch2d) |
| s 1225B(5) | 17312 | After considering any such representations or, in their absence, on th | encoded | `s 1225B(5) the Secretary of State must now decide whether to give the proposed direction` (coa26-ch2d) |
| s 1225B(6) | 17313 | The Secretary of State must give notice of the decision (a “direction  | encoded | `s 1225B(6) the Secretary of State has given notice of the decision` (coa26-ch2d) |
| s 1225B(7) | 17314 | Where the Secretary of State decides to give the proposed direction, t | encoded | `s 1225B(7) the direction decision notice has the required content` (coa26-ch2d) |
| s 1225B(7)(a) | 17315 | contain the direction, | encoded | `s 1225B(7) the direction decision notice has the required content` (coa26-ch2d) |
| s 1225B(7)(b) | 17316 | state the time at which the direction is to take effect, and | encoded | `s 1225B(7) the direction decision notice has the required content` (coa26-ch2d) |
| s 1225B(7)(c) | 17317 | specify the Secretary of State's reasons for the decision to give the  | encoded | `s 1225B(7) the direction decision notice has the required content` (coa26-ch2d) |
| s 1225B(8) | 17318 | Where the Secretary of State decides to give the proposed direction, t | encoded | `s 1225B(8) the Secretary of State has published the direction decision notice` (coa26-ch2d) |
| s 1225B(9) | 17319 | The Secretary of State may revoke a direction given to a body under se | encoded | `s 1225B(9) the revocation of the direction complies with subsection (9)` (coa26-ch2d) |
| s 1225B(9)(a) | 17320 | give the body notice of the revocation, and | encoded | `s 1225B(9) the revocation of the direction complies with subsection (9)` (coa26-ch2d) |
| s 1225B(9)(b) | 17321 | publish the notice in the same manner as the direction decision notice | encoded | `s 1225B(9) the revocation of the direction complies with subsection (9)` (coa26-ch2d) |
| s 1225C | 17322 | Compliance orders | encoded | `s 1225C(3) the court is` (coa26-ch2d); `s 1225C(1) the court may order the body to take such steps as it considers will secure that the requirement is satisfied or the obligation is complied with` (coa26-ch2d) ... |
| s 1225C(1) | 17323 | If on an application under this section in respect of a body, the cour | encoded | `s 1225C(1) the court may order the body to take such steps as it considers will secure that the requirement is satisfied or the obligation is complied with` (coa26-ch2d) |
| s 1225C(2) | 17324 | Where the obligation is an obligation to comply with a direction under | encoded | `s 1225C(2) the court may order compliance with the direction` (coa26-ch2d) |
| s 1225C(2)(a) | 17325 | the requirement in respect of which the direction was given is not sat | encoded | `s 1225C(2) the court may order compliance with the direction` (coa26-ch2d) |
| s 1225C(2)(b) | 17326 | the obligation in respect of which the direction was given has not bee | encoded | `s 1225C(2) the court may order compliance with the direction` (coa26-ch2d) |
| s 1225C(3) | 17327 | In this section, “ the court ” means the High Court or, in Scotland, t | encoded | `s 1225C(3) the court is` (coa26-ch2d) |
| s 1225D | 17328 | Financial penalties: general | encoded | `s 1225D(2) the Secretary of State has decided the amount in accordance with subsection (2)` (coa26-ch2d); `s 1225D(1) the amount is a lawful amount of financial penalty` (coa26-ch2d) ... |
| s 1225D(1) | 17329 | A financial penalty imposed on a body under this section is a financia | encoded | `s 1225D(1) the amount is a lawful amount of financial penalty` (coa26-ch2d) |
| s 1225D(2) | 17330 | In deciding what amount is appropriate the Secretary of State— | encoded | `s 1225D(2) the Secretary of State has decided the amount in accordance with subsection (2)` (coa26-ch2d) |
| s 1225D(2)(a) | 17331 | must have regard to the nature of the requirement which is not satisfi | encoded | `s 1225D(2) the Secretary of State has decided the amount in accordance with subsection (2)` (coa26-ch2d) |
| s 1225D(2)(b) | 17332 | must not take into account the Secretary of State's costs in dischargi | encoded | `s 1225D(2) the Secretary of State has decided the amount in accordance with subsection (2)` (coa26-ch2d) |
| s 1225D(3) | 17333 | A financial penalty under this section is payable to the Secretary of  | encoded | `s 1225D(3) the penalty is payable to the Secretary of State` (coa26-ch2d) |
| s 1225D(4) | 17334 | In sections 1225E to 1225G, references to a penalty are to a financial | encoded | `s 1225D(4) the reference to a penalty in sections 1225E to 1225G is to the penalty` (coa26-ch2d) |
| s 1225E | 17335 | Financial penalties: supplementary | encoded | `s 1225E(1) the notice of proposed penalty was given and has the required content` (coa26-ch2d); `s 1225E(2) the period specified under subsection (1)(c) is valid` (coa26-ch2d) ... |
| s 1225E(1) | 17336 | Before imposing a penalty on a body, the Secretary of State must give  | encoded | `s 1225E(1) the notice of proposed penalty was given and has the required content` (coa26-ch2d) |
| s 1225E(1)(a) | 17337 | stating that the Secretary of State proposes to impose a penalty and t | encoded | `s 1225E(1) the notice of proposed penalty was given and has the required content` (coa26-ch2d) |
| s 1225E(1)(b) | 17338 | identifying the requirement or obligation in question and stating why  | encoded | `s 1225E(1) the notice of proposed penalty was given and has the required content` (coa26-ch2d) |
| s 1225E(1)(c) | 17339 | specifying a period within which the body may make written representat | encoded | `s 1225E(1) the notice of proposed penalty was given and has the required content` (coa26-ch2d) |
| s 1225E(2) | 17340 | The period specified under subsection (1)(c)— | encoded | `s 1225E(2) the period specified under subsection (1)(c) is valid` (coa26-ch2d) |
| s 1225E(2)(a) | 17341 | must begin with the date on which the notice of proposed penalty is gi | encoded | `s 1225E(2) the period specified under subsection (1)(c) is valid` (coa26-ch2d) |
| s 1225E(2)(b) | 17342 | must not be less than 21 days. | encoded | `s 1225E(2) the period specified under subsection (1)(c) is valid` (coa26-ch2d) |
| s 1225E(3) | 17343 | Written representations made by the body before the end of the period  | encoded | `s 1225E(3) the Secretary of State has complied with the duty to consider the representations` (coa26-ch2d) |
| s 1225E(4) | 17344 | After considering any such representations or, in their absence, on th | encoded | `s 1225E(4) the Secretary of State must now decide whether to impose a penalty and whether to reduce the proposed amount` (coa26-ch2d) |
| s 1225E(4)(a) | 17345 | whether to impose a penalty, and | encoded | `s 1225E(4) the Secretary of State must now decide whether to impose a penalty and whether to reduce the proposed amount` (coa26-ch2d) |
| s 1225E(4)(b) | 17346 | where the Secretary of State decides to do so, whether to reduce the p | encoded | `s 1225E(4) the Secretary of State must now decide whether to impose a penalty and whether to reduce the proposed amount` (coa26-ch2d) |
| s 1225E(5) | 17347 | The Secretary of State must give notice of the decision (a “penalty de | encoded | `s 1225E(5) the Secretary of State has given notice of the decision` (coa26-ch2d) |
| s 1225E(6) | 17348 | Where the Secretary of State decides to impose a penalty, the penalty  | encoded | `s 1225E(6) the penalty decision notice has the required content` (coa26-ch2d) |
| s 1225E(6)(a) | 17349 | state that the Secretary of State has imposed a penalty on the body an | encoded | `s 1225E(6) the penalty decision notice has the required content` (coa26-ch2d) |
| s 1225E(6)(b) | 17350 | identify the requirement or obligation in question and state— | encoded | `s 1225E(6) the penalty decision notice has the required content` (coa26-ch2d) |
| s 1225E(6)(b)(i) | 17351 | why it appears to the Secretary of State that the requirement is not s | encoded | `s 1225E(6) the penalty decision notice has the required content` (coa26-ch2d) |
| s 1225E(6)(b)(ii) | 17352 | where, by that time, the requirement is satisfied or the obligation ha | encoded | `s 1225E(6) the penalty decision notice has the required content` (coa26-ch2d) |
| s 1225E(6)(c) | 17353 | specify a time by which the penalty is required to be paid. | encoded | `s 1225E(6) the penalty decision notice has the required content` (coa26-ch2d) |
| s 1225E(7) | 17354 | The time specified under subsection (6)(c) must be at least 3 months a | fork | F5 -> `s 1225E(7) the time specified for payment is valid` (coa26-ch2d) |
| s 1225E(8) | 17355 | Where the Secretary of State decides to impose a penalty, the Secretar | encoded | `s 1225E(8) the Secretary of State has published the penalty decision notice` (coa26-ch2d) |
| s 1225E(9) | 17356 | The Secretary of State may rescind a penalty imposed on a body under s | encoded | `s 1225E(9) the rescission of the penalty complies with subsection (9)` (coa26-ch2d) |
| s 1225E(9)(a) | 17357 | give the body notice of the rescission, and | encoded | `s 1225E(9) the rescission of the penalty complies with subsection (9)` (coa26-ch2d) |
| s 1225E(9)(b) | 17358 | publish the notice in the same manner as the penalty decision notice w | encoded | `s 1225E(9) the rescission of the penalty complies with subsection (9)` (coa26-ch2d) |
| s 1225F | 17359 | Appeals against financial penalties | encoded | `s 1225F(2) an appeal ground is made out` (coa26-ch2d); `s 1225F(1) the body may appeal to the court` (coa26-ch2d) ... |
| s 1225F(1) | 17360 | A body on which a penalty is imposed may appeal to the court on one or | encoded | `s 1225F(1) the body may appeal to the court` (coa26-ch2d) |
| s 1225F(2) | 17361 | The appeal grounds are— | encoded | `s 1225F(2) an appeal ground is made out` (coa26-ch2d) |
| s 1225F(2)(a) | 17362 | that, before the giving of the notice under section 1225E(1), the requ | encoded | `s 1225F(2) an appeal ground is made out` (coa26-ch2d) |
| s 1225F(2)(b) | 17363 | that, where the penalty was imposed in respect of a failure to comply  | encoded | `s 1225F(2) an appeal ground is made out` (coa26-ch2d) |
| s 1225F(2)(c) | 17364 | that any of the requirements of section 1225E have not been complied w | encoded | `s 1225F(2) an appeal ground is made out` (coa26-ch2d) |
| s 1225F(2)(d) | 17365 | that the amount of the penalty is unreasonable; | encoded | `s 1225F(2) an appeal ground is made out` (coa26-ch2d) |
| s 1225F(2)(e) | 17366 | that it was unreasonable of the Secretary of State to require the pena | encoded | `s 1225F(2) an appeal ground is made out` (coa26-ch2d) |
| s 1225F(3) | 17367 | An appeal under subsection (1) must be made within the period of 3 mon | fork | F5 -> `s 1225F(3) the appeal is made in time` (coa26-ch2d) |
| s 1225F(4) | 17368 | On any such appeal, where the court considers it appropriate to do so  | encoded | `s 1225F(4) the court may take the step` (coa26-ch2d) |
| s 1225F(4)(a) | 17369 | quash the penalty, | encoded | `s 1225F(4) the court may take the step` (coa26-ch2d) |
| s 1225F(4)(b) | 17370 | substitute a penalty of such lesser amount as the court considers appr | encoded | `s 1225F(4) the court may take the step` (coa26-ch2d) |
| s 1225F(4)(c) | 17371 | in the case of the appeal ground in subsection (2)(e), substitute a la | encoded | `s 1225F(4) the court may take the step` (coa26-ch2d) |
| s 1225F(5) | 17372 | Where the court substitutes a penalty of a lesser amount, it may requi | encoded | `s 1225F(5) the court may require the payment of interest on the substituted penalty` (coa26-ch2d) |
| s 1225F(6) | 17373 | Where the court substitutes a later time for the time specified in the | encoded | `s 1225F(6) the court may require the payment of interest on the penalty from the substituted time` (coa26-ch2d) |
| s 1225F(7) | 17374 | Where the court dismisses the appeal, it may require the payment of in | encoded | `s 1225F(7) the court may require the payment of interest on the penalty` (coa26-ch2d) |
| s 1225F(8) | 17375 | Where the court requires the payment of interest under this section, t | encoded | `s 1225F(8) the interest is payable at such rate as the court considers just and equitable` (coa26-ch2d) |
| s 1225F(9) | 17376 | Except as provided by this section, the validity of a penalty is not t | encoded | `s 1225F(9) the validity of the penalty may be questioned in the legal proceedings` (coa26-ch2d) |
| s 1225F(10) | 17377 | In this section “ the court ” means the High Court or, in Scotland, th | encoded | `s 1225F(10) the court is` (coa26-ch2d) |
| s 1225G | 17378 | Recovery of financial penalties | encoded | `s 1225G(1) the unpaid balance carries interest at the rate specified in section 17 of the Judgments Act 1838` (coa26-ch2d); `s 1225G(2) the penalty cannot yet be required to be paid` (coa26-ch2d) ... |
| s 1225G(1) | 17379 | If the whole or any part of a penalty is not paid by the time by which | encoded | `s 1225G(1) the unpaid balance carries interest at the rate specified in section 17 of the Judgments Act 1838` (coa26-ch2d) |
| s 1225G(2) | 17380 | If an appeal is made under section 1225F in relation to a penalty, the | encoded | `s 1225G(2) the penalty cannot yet be required to be paid` (coa26-ch2d) |
| s 1225G(3) | 17381 | Subsection (2) does not prevent the court from specifying that interes | encoded | `s 1225G(3) subsection (2) prevents the court from specifying that interest is to accrue from an earlier date` (coa26-ch2d) |
| s 1225G(4) | 17382 | Where a penalty, or any portion of it, has not been paid by the time w | encoded | `s 1225G(4) the Secretary of State may recover the unpaid penalty and interest from the body as a debt` (coa26-ch2d) |
| s 1225G(4)(a) | 17383 | no appeal relating to the penalty has been made under section 1225F du | encoded | `s 1225G(4) the Secretary of State may recover the unpaid penalty and interest from the body as a debt` (coa26-ch2d) |
| s 1225G(4)(b) | 17384-17385 | an appeal has been made under that section and has been determined or  | encoded | `s 1225G(4) the Secretary of State may recover the unpaid penalty and interest from the body as a debt` (coa26-ch2d) |
| heading | 17386 | Chapter 3 — Auditors General | inert | reason 1: heading, not operative |
| heading | 17387 | Eligibility for appointment | inert | reason 1: heading, not operative |
| s 1226 | 17388 | Auditors General: eligibility for appointment as a statutory auditor | encoded | `s 1226(1) the person is an Auditor General` (coa26-ch3a); `s 1226(2) the Auditor General is eligible for appointment as a statutory auditor` (coa26-ch3a) |
| s 1226(1) | 17389 | In this Part “Auditor General” means— | encoded | `s 1226(1) the person is an Auditor General` (coa26-ch3a) |
| s 1226(1)(a) | 17390 | the Comptroller and Auditor General, | encoded | `s 1226(1) the person is an Auditor General` (coa26-ch3a) |
| s 1226(1)(b) | 17391 | the Auditor General for Scotland, | encoded | `s 1226(1) the person is an Auditor General` (coa26-ch3a) |
| s 1226(1)(c) | 17392 | the Auditor General for Wales, or | encoded | `s 1226(1) the person is an Auditor General` (coa26-ch3a) |
| s 1226(1)(d) | 17393 | the Comptroller and Auditor General for Northern Ireland. | encoded | `s 1226(1) the person is an Auditor General` (coa26-ch3a) |
| s 1226(2) | 17394 | An Auditor General is eligible for appointment as a statutory auditor. | encoded | `s 1226(2) the Auditor General is eligible for appointment as a statutory auditor` (coa26-ch3a) |
| s 1226(3) | 17395 | Subsection (2) is subject to any suspension notice having effect under | encoded | `s 1226(2) the Auditor General is eligible for appointment as a statutory auditor` (coa26-ch3a) |
| heading | 17396 | Conduct of audits | inert | reason 1: heading, not operative |
| s 1227 | 17397-17398 | Individuals responsible for audit work on behalf of Auditors General | encoded | `s 1227 the Auditor General has secured that the individual is eligible for appointment as a statutory auditor by virtue of Chapter 2` (coa26-ch3a) |
| heading | 17399 | The Independent Supervisor | inert | reason 1: heading, not operative |
| s 1228 | 17400 | Appointment of the Independent Supervisor | encoded | `s 1228(1) the Secretary of State has appointed the Independent Supervisor` (coa26-ch3a); `s 1228(2) the appointment is made in the required form` (coa26-ch3a) ... |
| s 1228(1) | 17401 | The Secretary of State must appoint a body (“the Independent Superviso | encoded | `s 1228(1) the Secretary of State has appointed the Independent Supervisor` (coa26-ch3a) |
| s 1228(2) | 17402 | An appointment under this section must be made by order. | encoded | `s 1228(2) the appointment is made in the required form` (coa26-ch3a) |
| s 1228(3) | 17403 | The order has the effect of making the body appointed under subsection | encoded | `s 1228(3) the body appointed is designated under section 5 of the Freedom of Information Act 2000` (coa26-ch3a) |
| s 1228(4) | 17404 | A body may be appointed under this section only if it is a body corpor | encoded | `s 1228(4) the conditions for appointing the body are met` (coa26-ch3a) |
| s 1228(4)(a) | 17405 | to be willing and able to discharge the supervision function, and | encoded | `s 1228(4) the conditions for appointing the body are met` (coa26-ch3a) |
| s 1228(4)(b) | 17406 | to have arrangements in place relating to the discharge of that functi | encoded | `s 1228(4) the conditions for appointing the body are met` (coa26-ch3a) |
| s 1228(5) | 17407 | The conditions are— | encoded | `s 1228(5) the conditions in subsection (5) are met` (coa26-ch3a) |
| s 1228(5)(a) | 17408 | that the supervision function will be exercised effectively, and | encoded | `s 1228(5) the conditions in subsection (5) are met` (coa26-ch3a) |
| s 1228(5)(b) | 17409 | where the order is to contain any requirements or other provisions spe | encoded | `s 1228(5) the conditions in subsection (5) are met` (coa26-ch3a) |
| s 1228(6) | 17410 | An order under this section may contain such requirements or other pro | encoded | `s 1228(6) the order may contain the requirement or provision` (coa26-ch3a) |
| s 1228(7) | 17411 | An order under this section is subject to negative resolution procedur | inert | reason 2: machinery: an order under section 1228 is subject to negative resolution procedure |
| heading | 17412 | Supervision of Auditors General | inert | reason 1: heading, not operative |
| s 1229 | 17413 | Supervision of Auditors General by the Independent Supervisor | encoded | `s 1229(1) the Independent Supervisor has complied with the duty to supervise the Auditors General` (coa26-ch3a); `s 1229(2) the Independent Supervisor has discharged the duty in subsection (1)` (coa26-ch3a) ... |
| s 1229(1) | 17414 | The Independent Supervisor must supervise the performance by each Audi | encoded | `s 1229(1) the Independent Supervisor has complied with the duty to supervise the Auditors General` (coa26-ch3a) |
| s 1229(2) | 17415 | The Independent Supervisor must discharge that duty by— | encoded | `s 1229(2) the Independent Supervisor has discharged the duty in subsection (1)` (coa26-ch3a) |
| s 1229(2)(a) | 17416 | establishing supervision arrangements itself, or | encoded | `s 1229(2) the Independent Supervisor has discharged the duty in subsection (1)` (coa26-ch3a) |
| s 1229(2)(b) | 17417 | entering into supervision arrangements with one or more recognised sup | encoded | `s 1229(2) the Independent Supervisor has discharged the duty in subsection (1)` (coa26-ch3a) |
| s 1229(2A) | 17418 | If the Independent Supervisor enters into supervision arrangements wit | fork | F8 -> `s 1229(2A) the Independent Supervisor has complied with the duty to oversee the arrangements` (coa26-ch3a) |
| s 1229(3) | 17419 | For this purpose “supervision arrangements” are arrangements establish | fork | F3 -> `s 1229(3) the arrangements are supervision arrangements` (coa26-ch3a) |
| s 1229(3)(a) | 17420 | determines standards relating to professional integrity and independen | encoded | `s 1229(3) the arrangements are supervision arrangements` (coa26-ch3a) |
| s 1229(3)(b) | 17421 | determines technical standards which must be applied by an Auditor Gen | encoded | `s 1229(3) the arrangements are supervision arrangements` (coa26-ch3a) |
| s 1229(3)(c) | 17422 | monitors the performance of statutory audits carried out by an Auditor | encoded | `s 1229(3) the arrangements are supervision arrangements` (coa26-ch3a) |
| s 1229(3)(d) | 17423 | investigates any matter arising from the performance by an Auditor Gen | encoded | `s 1229(3) the arrangements are supervision arrangements` (coa26-ch3a) |
| s 1229(3)(e) | 17424 | holds disciplinary hearings in respect of an Auditor General which app | encoded | `s 1229(3) the arrangements are supervision arrangements` (coa26-ch3a) |
| s 1229(3)(f) | 17425 | decides whether (and, if so, what) disciplinary action should be taken | encoded | `s 1229(3) the arrangements are supervision arrangements` (coa26-ch3a) |
| s 1229(3A) | 17426 | The requirements of paragraphs 9 to 10C and 12 to 16 of Schedule 10 (r | encoded | `s 1229(3A) the requirement applies in relation to the supervision arrangements` (coa26-ch3a) |
| s 1229(4) | 17427 | The Independent Supervisor may enter into supervision arrangements wit | encoded | `s 1229(4) the Independent Supervisor may enter into supervision arrangements with the body` (coa26-ch3a) |
| s 1229(5) | 17428 | The Independent Supervisor must notify each Auditor General in writing | fork | F8 -> `s 1229(5) the Independent Supervisor has complied with the duty to notify each Auditor General` (coa26-ch3a) |
| s 1229(5A) | 17429 | The Independent Supervisor must, at least once in every calendar year, | encoded | `s 1229(5A) the Independent Supervisor delivered the summary in the calendar year` (coa26-ch3a) |
| s 1229(6) | 17430 | Supervision arrangements within subsection (3)(f) may, in particular,  | fork | F4 -> `s 1229(6) the arrangements may provide for payment of a fine to any person` (coa26-ch3a) |
| s 1229(7) | 17431 | Any fine received by the Independent Supervisor under supervision arra | encoded | `s 1229(7) the fine is to be paid into the Consolidated Fund` (coa26-ch3a) |
| s 1230 | 17432 | Duties of Auditors General in relation to supervision arrangements | encoded | `s 1230(1) the Auditor General has complied with the duties in subsection (1)` (coa26-ch3a); `s 1230(2) who the Auditor General must pay the proportion of the costs to` (coa26-ch3a) ... |
| s 1230(1) | 17433 | Each Auditor General must— | encoded | `s 1230(1) the Auditor General has complied with the duties in subsection (1)` (coa26-ch3a) |
| s 1230(1)(a) | 17434 | comply with any standards of the kind mentioned in subsection (3)(a) o | encoded | `s 1230(1) the Auditor General has complied with the duties in subsection (1)` (coa26-ch3a) |
| s 1230(1)(b) | 17435 | take such steps as may be reasonably required of that Auditor General  | encoded | `s 1230(1) the Auditor General has complied with the duties in subsection (1)` (coa26-ch3a) |
| s 1230(1)(c) | 17436 | comply with any decision of the kind mentioned in subsection (3)(f) of | encoded | `s 1230(1) the Auditor General has complied with the duties in subsection (1)` (coa26-ch3a) |
| s 1230(2) | 17437 | Each Auditor General must— | encoded | `s 1230(2) who the Auditor General must pay the proportion of the costs to` (coa26-ch3a); `s 1230(2) the amount the Auditor General must pay, in pounds` (coa26-ch3a) |
| s 1230(2)(a) | 17438 | if the Independent Supervisor has established supervision arrangements | encoded | `s 1230(2) who the Auditor General must pay the proportion of the costs to` (coa26-ch3a); `s 1230(2) the amount the Auditor General must pay, in pounds` (coa26-ch3a) |
| s 1230(2)(b) | 17439-17440 | if the Independent Supervisor has entered into supervision arrangement | encoded | `s 1230(2) who the Auditor General must pay the proportion of the costs to` (coa26-ch3a); `s 1230(2) the amount the Auditor General must pay, in pounds` (coa26-ch3a) |
| s 1230(3) | 17441 | Expenditure under subsection (2) is— | encoded | `s 1230(3) the expenditure is regarded as` (coa26-ch3a) |
| s 1230(3)(a) | 17442 | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | repealed or blank in this text | the text shows ". . . ." in place of the provision |
| s 1230(3)(b) | 17443 | in the case of expenditure of the Comptroller and Auditor General for  | encoded | `s 1230(3) the expenditure is regarded as` (coa26-ch3a) |
| s 1230(3)(c) | 17444 | in the case of expenditure of the Auditor General for Wales, to be reg | encoded | `s 1230(3) the expenditure is regarded as` (coa26-ch3a) |
| s 1230(4) | 17445 | In this section “the supervision arrangements” means the arrangements  | encoded | `s 1230(4) the arrangements are the supervision arrangements` (coa26-ch3a) |
| heading | 17446 | Reporting requirement | inert | reason 1: heading, not operative |
| s 1231 | 17447 | Reports by the Independent Supervisor | encoded | `s 1231(1) the Independent Supervisor prepared a report in the calendar year` (coa26-ch3a); `s 1231(2) the Independent Supervisor has given a copy of the report to each person named` (coa26-ch3a) ... |
| s 1231(1) | 17448 | The Independent Supervisor must, at least once in each calendar year,  | encoded | `s 1231(1) the Independent Supervisor prepared a report in the calendar year` (coa26-ch3a) |
| s 1231(2) | 17449 | The Independent Supervisor must give a copy of each report prepared un | encoded | `s 1231(2) the Independent Supervisor has given a copy of the report to each person named` (coa26-ch3a) |
| s 1231(2)(a) | 17450 | the Secretary of State; | encoded | `s 1231(2) the Independent Supervisor has given a copy of the report to each person named` (coa26-ch3a) |
| s 1231(2)(b) | 17451 | the First Minister in Scotland; | encoded | `s 1231(2) the Independent Supervisor has given a copy of the report to each person named` (coa26-ch3a) |
| s 1231(2)(c) | 17452 | the First Minister and the deputy First Minister in Northern Ireland; | encoded | `s 1231(2) the Independent Supervisor has given a copy of the report to each person named` (coa26-ch3a) |
| s 1231(2)(d) | 17453 | The First Minister for Wales. | encoded | `s 1231(2) the Independent Supervisor has given a copy of the report to each person named` (coa26-ch3a) |
| s 1231(3) | 17454 | The Secretary of State must lay before each House of Parliament a copy | encoded | `s 1231(3) the Secretary of State has laid a copy of the report before each House of Parliament` (coa26-ch3a) |
| s 1231(3A) | 17455 | The First Minister for Wales must lay before the National Assembly for | encoded | `s 1231(3A) the First Minister for Wales has laid a copy of the report before the National Assembly for Wales` (coa26-ch3a) |
| s 1231(4) | 17456 | In relation to a calendar year during which an appointment of a body a | encoded | `s 1231(4) the section applies with the modifications specified in the order` (coa26-ch3a) |
| heading | 17457 | Information | inert | reason 1: heading, not operative |
| s 1232 | 17458 | Matters to be notified to the Independent Supervisor | encoded | `s 1232(1) the Independent Supervisor may require the body to notify or give information` (coa26-ch3b); `s 1232(2) the notice or information required is within subsection (2)` (coa26-ch3b) ... |
| s 1232(1) | 17459 | The Independent Supervisor may require an Auditor General— | encoded | `s 1232(1) the Independent Supervisor may require the body to notify or give information` (coa26-ch3b) |
| s 1232(1)(a) | 17460 | to notify the Independent Supervisor immediately of the occurrence of  | encoded | `s 1232(1) the Independent Supervisor may require the body to notify or give information` (coa26-ch3b) |
| s 1232(1)(b) | 17461 | to give the Independent Supervisor, at such times or in respect of suc | encoded | `s 1232(1) the Independent Supervisor may require the body to notify or give information` (coa26-ch3b) |
| s 1232(2) | 17462 | The notices and information required to be given must be such as the I | encoded | `s 1232(2) the notice or information required is within subsection (2)` (coa26-ch3b) |
| s 1232(3) | 17463 | The Independent Supervisor may require information given under this se | encoded | `s 1232(3) the Independent Supervisor may require the information to be given in a specified form or verified in a specified manner` (coa26-ch3b) |
| s 1232(4) | 17464 | Any notice or information required to be given under this section must | fork | F9 -> `s 1232(4) the notice or information must be given in writing` (coa26-ch3b) |
| s 1233 | 17465 | The Independent Supervisor's power to call for information | encoded | `s 1233(1) the Independent Supervisor may by notice in writing require the person to give the information` (coa26-ch3b); `s 1233(2) the Independent Supervisor may require the information to be given within a reasonable time and verified in a specified manner` (coa26-ch3b) |
| s 1233(1) | 17466 | The Independent Supervisor may by notice in writing require an Auditor | encoded | `s 1233(1) the Independent Supervisor may by notice in writing require the person to give the information` (coa26-ch3b) |
| s 1233(2) | 17467 | The Independent Supervisor may require that any information which it r | encoded | `s 1233(2) the Independent Supervisor may require the information to be given within a reasonable time and verified in a specified manner` (coa26-ch3b) |
| heading | 17468 | Enforcement | inert | reason 1: heading, not operative |
| s 1234 | 17469 | Suspension notices | encoded | `s 1234(1) the Independent Supervisor may issue the notice` (coa26-ch3b); `s 1234(2) the Independent Supervisor has had regard to the matters in subsection (2)` (coa26-ch3b) ... |
| s 1234(1) | 17470 | The Independent Supervisor may issue— | encoded | `s 1234(1) the Independent Supervisor may issue the notice` (coa26-ch3b) |
| s 1234(1)(a) | 17471 | a notice (a “suspension notice”) suspending an Auditor General's eligi | encoded | `s 1234(1) the Independent Supervisor may issue the notice` (coa26-ch3b) |
| s 1234(1)(b) | 17472 | a notice amending or revoking a suspension notice previously issued to | encoded | `s 1234(1) the Independent Supervisor may issue the notice` (coa26-ch3b) |
| s 1234(2) | 17473 | In determining whether it is appropriate to issue a notice under subse | encoded | `s 1234(2) the Independent Supervisor has had regard to the matters in subsection (2)` (coa26-ch3b) |
| s 1234(2)(a) | 17474 | the Auditor General's performance of the obligations imposed on him by | encoded | `s 1234(2) the Independent Supervisor has had regard to the matters in subsection (2)` (coa26-ch3b) |
| s 1234(2)(b) | 17475 | the Auditor General's performance of his functions as a statutory audi | encoded | `s 1234(2) the Independent Supervisor has had regard to the matters in subsection (2)` (coa26-ch3b) |
| s 1234(3) | 17476 | A notice under subsection (1) must— | fork | F5 -> `s 1234(3) the notice meets subsection (3)` (coa26-ch3b) |
| s 1234(3)(a) | 17477 | be in writing, and | encoded | `s 1234(3) the notice meets subsection (3)` (coa26-ch3b) |
| s 1234(3)(b) | 17478 | state the date on which it takes effect (which must be after the perio | encoded | `s 1234(3) the notice meets subsection (3)` (coa26-ch3b) |
| s 1234(4) | 17479 | Before issuing a notice under subsection (1), the Independent Supervis | encoded | `s 1234(4) the Independent Supervisor has complied with the duty before issuing the notice` (coa26-ch3b) |
| s 1234(4)(a) | 17480 | give written notice of its intention to do so to the Auditor General,  | encoded | `s 1234(4) the Independent Supervisor has complied with the duty before issuing the notice` (coa26-ch3b) |
| s 1234(4)(b) | 17481 | publish the notice mentioned in paragraph (a) in such manner as it thi | encoded | `s 1234(4) the Independent Supervisor has complied with the duty before issuing the notice` (coa26-ch3b) |
| s 1234(5) | 17482 | A notice under subsection (4) must— | encoded | `s 1234(5) the notice of intention has the required content` (coa26-ch3b) |
| s 1234(5)(a) | 17483 | state the reasons for which the Independent Supervisor proposes to act | encoded | `s 1234(5) the notice of intention has the required content` (coa26-ch3b) |
| s 1234(5)(b) | 17484 | give particulars of the rights conferred by subsection (6). | encoded | `s 1234(5) the notice of intention has the required content` (coa26-ch3b) |
| s 1234(6) | 17485 | A person within subsection (7) may, within the period of three months  | fork | F5 -> `s 1234(6) the person may make written representations and, if desired, oral representations` (coa26-ch3b) |
| s 1234(7) | 17486 | The persons within this subsection are— | encoded | `s 1234(7) the person is within subsection (7)` (coa26-ch3b) |
| s 1234(7)(a) | 17487 | the Auditor General, and | encoded | `s 1234(7) the person is within subsection (7)` (coa26-ch3b) |
| s 1234(7)(b) | 17488 | any other person who appears to the Independent Supervisor to be affec | encoded | `s 1234(7) the person is within subsection (7)` (coa26-ch3b) |
| s 1234(8) | 17489 | The Independent Supervisor must have regard to any representations mad | encoded | `s 1234(8) the Independent Supervisor has complied with the duty to have regard to the representations` (coa26-ch3b) |
| s 1234(8)(a) | 17490 | whether to issue a notice under subsection (1), and | encoded | `s 1234(8) the Independent Supervisor has complied with the duty to have regard to the representations` (coa26-ch3b) |
| s 1234(8)(b) | 17491 | the terms of any such notice. | encoded | `s 1234(8) the Independent Supervisor has complied with the duty to have regard to the representations` (coa26-ch3b) |
| s 1234(9) | 17492 | If in any case the Independent Supervisor considers it appropriate to  | fork | F25 -> `s 1234(9) the Independent Supervisor may issue the notice without regard to the restriction in subsection (3)(b)` (coa26-ch3b) |
| s 1234(9)(a) | 17493 | no notice has been given or published under subsection (4), or | encoded | `s 1234(9) the Independent Supervisor may issue the notice without regard to the restriction in subsection (3)(b)` (coa26-ch3b) |
| s 1234(9)(b) | 17494 | the period of time for making representations in pursuance of such a n | encoded | `s 1234(9) the Independent Supervisor may issue the notice without regard to the restriction in subsection (3)(b)` (coa26-ch3b) |
| s 1234(10) | 17495 | On issuing a notice under subsection (1), the Independent Supervisor m | encoded | `s 1234(10) the Independent Supervisor has complied with the duty on issuing the notice` (coa26-ch3b) |
| s 1234(10)(a) | 17496 | give a copy of the notice to the Auditor General, and | encoded | `s 1234(10) the Independent Supervisor has complied with the duty on issuing the notice` (coa26-ch3b) |
| s 1234(10)(b) | 17497 | publish the notice in such manner as it thinks appropriate for bringin | encoded | `s 1234(10) the Independent Supervisor has complied with the duty on issuing the notice` (coa26-ch3b) |
| s 1234(11) | 17498 | In this section “specified” means specified in, or of a description sp | encoded | `s 1234(11) the person is specified` (coa26-ch3b) |
| s 1235 | 17499 | Effect of suspension notices | encoded | `s 1235(1) the Auditor General may act as statutory auditor of the audited person` (coa26-ch3b); `s 1235(1) acts as statutory auditor of the audited person` (coa26-ch3b) ... |
| s 1235(1) | 17500 | An Auditor General must not act as a statutory auditor at any time whe | encoded | `s 1235(1) the Auditor General may act as statutory auditor of the audited person` (coa26-ch3b); `s 1235(1) acts as statutory auditor of the audited person` (coa26-ch3b) ... |
| s 1235(2) | 17501 | If at any time during an Auditor General's term of office as a statuto | fork | F8 -> `s 1235(2) the Auditor General must immediately resign and give notice` (coa26-ch3b); `s 1235(2) the duty of an Auditor General when a suspension notice takes effect` (coa26-ch3b) |
| s 1235(2)(a) | 17502 | resign his office (with immediate effect), and | encoded | `s 1235(2)(a) resigns his office with immediate effect` (coa26-ch3b) |
| s 1235(2)(b) | 17503 | give notice in writing to the audited person that he has resigned by r | encoded | `s 1235(2)(b) gives notice in writing that he has resigned by reason of his becoming ineligible` (coa26-ch3b) |
| s 1235(3) | 17504 | A suspension notice does not make an Auditor General ineligible for ap | encoded | `s 1235(3) the suspension notice makes the Auditor General ineligible for the purposes of section 1213` (coa26-ch3b) |
| s 1236 | 17505 | Compliance orders | encoded | `s 1236(1) the Independent Supervisor may make an application to the court` (coa26-ch3b); `s 1236(2) the court may order the Auditor General to take such steps as the court directs` (coa26-ch3b) ... |
| s 1236(1) | 17506 | If at any time it appears to the Independent Supervisor that an Audito | fork | F26 -> `s 1236(1) the Independent Supervisor may make an application to the court` (coa26-ch3b) |
| s 1236(2) | 17507 | If on an application under this section the court decides that the Aud | encoded | `s 1236(2) the court may order the Auditor General to take such steps as the court directs` (coa26-ch3b) |
| s 1236(3) | 17508 | In this section “the court” means the High Court or, in Scotland, the  | encoded | `s 1236(3) the court is` (coa26-ch3b) |
| heading | 17509 | Proceedings | inert | reason 1: heading, not operative |
| s 1237 | 17510 | Proceedings involving the Independent Supervisor | encoded | `s 1237(2) the proceedings are relevant proceedings` (coa26-ch3b); `s 1237(1) the proceedings may be brought by or against the Independent Supervisor in that name` (coa26-ch3b) ... |
| s 1237(1) | 17511 | If the Independent Supervisor is an unincorporated association, any re | encoded | `s 1237(1) the proceedings may be brought by or against the Independent Supervisor in that name` (coa26-ch3b) |
| s 1237(2) | 17512 | For this purpose “relevant proceedings” means proceedings brought in o | encoded | `s 1237(2) the proceedings are relevant proceedings` (coa26-ch3b) |
| s 1237(3) | 17513 | Where an appointment under section 1228 is revoked, the revoking order | encoded | `s 1237(3) the revoking order may make the provision with respect to pending proceedings` (coa26-ch3b) |
| heading | 17514 | Grants | inert | reason 1: heading, not operative |
| s 1238 | 17515-17516 | Grants to the Independent Supervisor | inert | reason 2: machinery: an amendment of another Act (section 16 of the Companies (Audit, Investigations and Community Enterprise) Act 2004) |
| s 1238(ka) | 17517 | exercising functions of the Independent Supervisor appointed under Cha | inert | reason 2: machinery: an amendment of another Act (section 16 of the Companies (Audit, Investigations and Community Enterprise) Act 2004) |


## Fork register (coa26)

Every place where the text can be read two or more ways with different outcomes, and the places where the brief leaves the reading to the encoder ("decide case by case"; the maintainer, 2026-11-05). The reading in the third column is the one the rule encodes; a reviewer can overrule any of them.

| id | provision and rule | readings seen | reading taken | text that licenses each |
| --- | --- | --- | --- | --- |
| F1 | s 1213(7) and s 1215(6): `s 1213(7) the penalty for an offence under subsection (5) or (6)`, `s 1215(6) ...` | (A) the daily fine is one-tenth of the greater of 5,000 pounds and the level 4 amount; (B) one-tenth of the statutory maximum; (C) both limits | (A) | The text prints "one-tenth of the statutory maximumone-tenth of the greater of £5,000 or the amount corresponding to level 4 on the standard scale for summary offences for each day on which the act or the failure continues": an amendment's old and new words run together; (A) is the later words, (B) the earlier. The level 4 amount is an input. |
| F2 | s 1214(3) and (5): `s 1214(5) ...`, `s 1214(3) ...` | (A) subsection (5) takes an auditor out of "officer or employee" in (2)(a) only; (B) it takes the auditor out of (3)(a) as well | (A) | (5): "An auditor of an audited person is not to be regarded as an officer or employee of the person for the purposes of subsections (2) and (3)": "the person" is the audited person; (3)(a) concerns an associated undertaking, a different person. |
| F3 | s 1229(3): `s 1229(3) the arrangements are supervision arrangements` | (A) all six functions (a) to (f) are required; (B) any one makes the arrangements "supervision arrangements" | (A) | "in accordance with which the Independent Supervisor or the body does . . . the following— (a) ...; (b) ...; ... (f) ...": a list with no "or". |
| F4 | s 1229(6): `s 1229(6) the arrangements may provide for payment of a fine to any person` | (A) payer is the Auditor General or, for Wales, the Wales Audit Office; (B) only a payment by an Auditor General to any person | (A) | The text prints "a fine to any personor, in the case of the Auditor General for Wales, for payment by the Wales Audit Office of such a fine": old and new words joined without a break. |
| F5 | months: s 1225E(7), s 1225F(3), s 1234(3), s 1234(6) | (A) "3 months after D" is D's day three months on (`Date`), the period "of 3 months beginning with" D ends the day before; (B) the period includes that day; (C) a month-end start date (31 August) means the last day of the later month | (A) | "must be at least 3 months after the date on which the notice is given"; "within the period of 3 months beginning with the day on which the notice ... is given". `Date` rolls an impossible day forward (31 August plus 3 months is 1 December under (A), 30 November under (C)); no test uses a month-end start. |
| F6 | closed lists introduced by "are" or "means": s 1218(2), s 1224(2), s 1225F(2), s 1234(7), s 1226(1) | (A) a list closed by "are" is the text's no for anyone outside it (JUST FALSE); (B) NOTHING | (A) | "The persons within this subsection are— (a) ...", "The appeal grounds are— ...". The keel reads "are" the same way (`s 2(2)` in `coa-definitions.l4`). Listed again under Marginal readings. |
| F7 | a bare "must" not done: ss 1221(7D), 1223(2), 1225B(1)-(9), 1225D(2), 1225E(1)-(9), 1227, 1228(1), (2), 1229(1), (2), 1230(1), 1231(2), (3), (3A), 1234(2), (4), (5), (8), (10) | (A) the function that asks "has the person done what the subsection requires" answers JUST FALSE when not done; (B) NOTHING | (A) | each subsection's "must", quoted in the FALSE-kind comment on the branch. One of the six questions the maintainer left to case-by-case decision (2026-11-05). |
| F8 | a duty whose "if" or "where" is unmet: ss 1213(2), 1215(1), 1223A(1), (2), 1229(2A), (5), 1235(2) | (A) JUST FALSE ("no duty arises"); (B) NOTHING | (A) | "If at any time during his term of office a statutory auditor becomes ineligible ... he must immediately"; the keel's reading (a) of the rule of 2026-10-29. |
| F9 | an "unless" once met: ss 1216(2), 1223(4), 1223ZA(4), 1232(4), 1224B(1)(a), (b) | (A) JUST FALSE ("the default does not apply" / "no offence"); (B) NOTHING | (A) | "Unless a contrary intention appears, the appointment is an appointment of the partnership as such"; "must be given in writing unless ..."; "is guilty of an offence, unless ...". |
| F10 | a "where" or "if" on a grant that fails: ss 1225B(7), (8), 1225C(1), 1225E(6), (8), 1225F(4)-(8), 1225G(4), 1236(2), 1237(3) (s 1234(9) and s 1236(1), grants named "may" with a plain "if" gate, were moved to NOTHING by the name-test sweep: F25, F26) | (A) JUST FALSE (ruling of 2026-11-05 (b)); (B) NOTHING | (A) | the ruling "no for a and b" on "where" conditions, applied also to "if" on a power. A case that falls outside a stated limit with no "where" or "if" (for example the powers in s 1221(2), (5)-(8)) is NOTHING (ruling (c)). |
| F11 | s 1212(1): `s 1212(1) the individual or firm is eligible ...` | (A) a failed "if" is JUST FALSE; (B) NOTHING, since s 1212(1) is a sufficient and not a necessary condition | (A) | "An individual or firm is eligible for appointment as a statutory auditor if the individual or firm— (a) is a member of a recognised supervisory body, and (b) is eligible under the rules of that body", read with s 1211 "only if ... by virtue of Chapter 2". |
| F12 | s 1219(1)(f): "subject to any direction under section 1221(5)" | (A) a direction without the additional qualifications removes limb (f) (JUST FALSE for the limb); (B) the limb stays and s 1221(5) is a separate bar | (A) | "(f) subject to any direction under section 1221(5), he is regarded ... as holding an approved third country qualification"; s 1221(5): "not to be treated as holding an appropriate qualification unless they hold such additional educational qualifications". The outcomes are the same on the tested facts. |
| F13 | s 1217(4) and s 1220(3): "Schedule 10 / 11 has effect with respect to the recognition" | (A) a hand-off to a Schedule: the Schedule's answer passes through, JUST FALSE included (ruling of 2026-11-05 (a)); (B) NOTHING, because the Schedules are coa30's range | (A) | "Schedule 10 has effect with respect to the recognition of supervisory bodies for the purposes of this Part." |
| F14 | s 1210(1) closing words: `s 1210(1) the audit is a statutory audit`, `...the work is statutory audit work` | (A) NOTHING for an audit by someone who is not a statutory auditor; (B) JUST FALSE | (A) | "the expressions “statutory audit” and “statutory audit work” are to be construed accordingly": a construction rule, not a "means" definition. |
| F15 | s 1224A(1) and (2): scope lists | (A) outside the list is NOTHING (a scope limit with no "only", ruling (c)); (B) JUST FALSE | (A) | "This section applies to information ... that is provided to a body to which this section applies"; "This section applies to— (a) ... (f) ...". |
| F16 | s 1216(3) with (4)(a), (b): `s 1216(3) ...`, `s 1216(4)(a) ...`, `s 1216(4)(b) ...` | (A) (4) states only-if limits: a JUST FALSE from (4)(a) or (b) means no succession, otherwise the fact of succession decides; (B) (4) is itself the test | (A) | "a partnership is to be regarded as succeeding to the practice of another partnership only if the members of the successor partnership are substantially the same". |
| F17 | s 1210(3) "friendly society", "insurer", "issuer", "prescribed" | (A) the borrowed answer is an input and NOTHING passes through; (B) FALSE when the person cannot show it | (A) | each is handed to the Friendly Societies Act 1992, Directive 91/674/EEC, the Financial Services and Markets Act 2000 or an order, none of them among the sources. |
| F18 | s 1221(7C): "not exceeding three years" | AT MOST 36 months (taken); fewer than 36 months for "three years" counted in days | AT MOST 36 months | the period is an input in months; tests at 36 and 37. |
| F19 | s 1222(1): "is eligible only for appointment as auditor of an unquoted company" | (A) a necessary limit: JUST FALSE when the company is not unquoted, NOTHING when it is; (B) also a grant: JUST TRUE when it is | (A) | "only". The grant itself is in ss 1212 and 1219. |
| F20 | s 1211: "only if the person is so eligible" by Chapter 2 or Chapter 3 | (A) a necessary condition: JUST FALSE when neither, NOTHING otherwise; (B) JUST TRUE when either | (A) | "only if". The positive rules are ss 1212 and 1226. |
| F21 | s 1214(4): "associate" and the connections; ss 1214(2), (3): "officer" | the facts are inputs; "associate" is defined elsewhere (not in this range) and "officer" in s 1173(1) (the keel) | inputs | "a connection of any such description as may be specified by regulations made by the Secretary of State": the regulations are not among the sources. |
| F22 | s 1213(1), s 1214(1), s 1235(1): "may not act" | (A) a decision function answers JUST FALSE where the bar bites and NOTHING otherwise (never JUST TRUE) and a `SHANT` rule is derived for the named bearer (ruling N2); (B) no function | (A) | flat negatives count as the text's no (N2, 2026-11-04). |
| F23 | s 1224B(2): a summary conviction in no stated place | NOTHING (taken); the E&W / NI figure; the Scottish figure | NOTHING | "(i) in Scotland, ... (ii) in England and Wales or Northern Ireland": the generic mode `on summary conviction` has no place. |
| F24 | s 1213(1) and s 1235(1) timing: how long a trace lasts | a `SHANT` without `WITHIN` has no end; "immediately" is `WITHIN 0` days | as stated | "must immediately", counted on the trace clock in days. |
| F25 | s 1234(9): `s 1234(9) the Independent Supervisor may issue the notice without regard to the restriction in subsection (3)(b)` | (A) NOTHING when the public-interest "if" fails (a grant limited by its own wording; the Guide's "In short" line); (B) JUST FALSE (a failed "if" read as the text's own no) | (A), name-test sweep of 2026-11-12 | "If in any case the Independent Supervisor considers it appropriate to do so in the public interest it may issue a notice under subsection (1), without regard to the restriction in subsection (3)(b)". |
| F26 | s 1236(1): `s 1236(1) the Independent Supervisor may make an application to the court` | (A) NOTHING when it does not appear to the Independent Supervisor that an Auditor General has failed to comply; (B) JUST FALSE (a failed "if" read as the text's own no) | (A), name-test sweep of 2026-11-12 | "If at any time it appears to the Independent Supervisor that an Auditor General has failed to comply with an obligation imposed on him by or by virtue of this Part, the Independent Supervisor may make an application to the court under this section." |
| L1 | s 1216(5): `s 1216(5) the appointment may be treated as extending to the successor` | (A) JUST FALSE when the gate fails (ruling (b) of the periods, "where" and scope-limits paragraph, taken); (B) NOTHING (the Guide's line that a grant limited by its own wording and a case outside the limit is NOTHING) | (A), unchanged: ASSUMED, NOT RULED, that a "may" function gated by "where", "when", "upon" or an equivalent condition goes with this listed group; a question for the maintainer or a lawyer, not one to settle by sweep | "Where the partnership ceases and the appointment is not treated under subsection (3) as extending to any partnership or other person" (a "where"); its last branch also passes on JUST FALSE from `s 1216(6)` when the successor is not an "appropriate" partnership or person (a named complement) |
| L2 | s 1225C(1): `s 1225C(1) the court may order the body to take such steps as it considers will secure that the requirement is satisfied or the obligation is complied with` | (A) JUST FALSE when the gate fails (ruling (b) of the periods, "where" and scope-limits paragraph, taken); (B) NOTHING (the Guide's line that a grant limited by its own wording and a case outside the limit is NOTHING) | (A), unchanged: ASSUMED, NOT RULED, that a "may" function gated by "where", "when", "upon" or an equivalent condition goes with this listed group; a question for the maintainer or a lawyer, not one to settle by sweep | "If on an application under this section in respect of a body, the court decides that a requirement is not satisfied or an obligation has not been complied with, the court may" ("on an application") |
| L3 | s 1225F(4): `s 1225F(4) the court may take the step` | (A) JUST FALSE when the gate fails (ruling (b) of the periods, "where" and scope-limits paragraph, taken); (B) NOTHING (the Guide's line that a grant limited by its own wording and a case outside the limit is NOTHING) | (A), unchanged: ASSUMED, NOT RULED, that a "may" function gated by "where", "when", "upon" or an equivalent condition goes with this listed group; a question for the maintainer or a lawyer, not one to settle by sweep | "On any such appeal, where the court considers it appropriate to do so in all the circumstances of the case and is satisfied of one or more of the appeal grounds, the court may" ("where") |
| L4 | s 1225F(5): `s 1225F(5) the court may require the payment of interest on the substituted penalty` | (A) JUST FALSE when the gate fails (ruling (b) of the periods, "where" and scope-limits paragraph, taken); (B) NOTHING (the Guide's line that a grant limited by its own wording and a case outside the limit is NOTHING) | (A), unchanged: ASSUMED, NOT RULED, that a "may" function gated by "where", "when", "upon" or an equivalent condition goes with this listed group; a question for the maintainer or a lawyer, not one to settle by sweep | "Where the court substitutes a penalty of a lesser amount, it may require the payment of interest" ("where") |
| L5 | s 1225F(6): `s 1225F(6) the court may require the payment of interest on the penalty from the substituted time` | (A) JUST FALSE when the gate fails (ruling (b) of the periods, "where" and scope-limits paragraph, taken); (B) NOTHING (the Guide's line that a grant limited by its own wording and a case outside the limit is NOTHING) | (A), unchanged: ASSUMED, NOT RULED, that a "may" function gated by "where", "when", "upon" or an equivalent condition goes with this listed group; a question for the maintainer or a lawyer, not one to settle by sweep | "Where the court substitutes a later time for the time specified in the notice" ("where") |
| L6 | s 1225F(7): `s 1225F(7) the court may require the payment of interest on the penalty` | (A) JUST FALSE when the gate fails (ruling (b) of the periods, "where" and scope-limits paragraph, taken); (B) NOTHING (the Guide's line that a grant limited by its own wording and a case outside the limit is NOTHING) | (A), unchanged: ASSUMED, NOT RULED, that a "may" function gated by "where", "when", "upon" or an equivalent condition goes with this listed group; a question for the maintainer or a lawyer, not one to settle by sweep | "Where the court dismisses the appeal, it may require the payment of interest on the penalty" ("where") |
| L7 | s 1225G(4): `s 1225G(4) the Secretary of State may recover the unpaid penalty and interest from the body as a debt` | (A) JUST FALSE when the gate fails (ruling (b) of the periods, "where" and scope-limits paragraph, taken); (B) NOTHING (the Guide's line that a grant limited by its own wording and a case outside the limit is NOTHING) | (A), unchanged: ASSUMED, NOT RULED, that a "may" function gated by "where", "when", "upon" or an equivalent condition goes with this listed group; a question for the maintainer or a lawyer, not one to settle by sweep | "Where a penalty, or any portion of it, has not been paid by the time when it is required to be paid and— (a) ... or (b) ..., the Secretary of State may recover" ("where") |
| L8 | s 1234(6): `s 1234(6) the person may make written representations and, if desired, oral representations` | (A) JUST FALSE when the gate fails (ruling (b) of the periods, "where" and scope-limits paragraph, taken); (B) NOTHING (the Guide's line that a grant limited by its own wording and a case outside the limit is NOTHING) | (A), unchanged: ASSUMED, NOT RULED, that a "may" function gated by "where", "when", "upon" or an equivalent condition goes with this listed group; a question for the maintainer or a lawyer, not one to settle by sweep | "may, within the period of 3 months beginning with the date of service or publication of the notice under subsection (4) or such longer period as the Independent Supervisor may allow" (a stated period; ruling of 2026-11-05 (a) says JUST FALSE outside a period fixed in the text's own words, and the Guide's "In short" line lists "a stated period" under NOTHING) |
| L9 | s 1236(2): `s 1236(2) the court may order the Auditor General to take such steps as the court directs` | (A) JUST FALSE when the gate fails (ruling (b) of the periods, "where" and scope-limits paragraph, taken); (B) NOTHING (the Guide's line that a grant limited by its own wording and a case outside the limit is NOTHING) | (A), unchanged: ASSUMED, NOT RULED, that a "may" function gated by "where", "when", "upon" or an equivalent condition goes with this listed group; a question for the maintainer or a lawyer, not one to settle by sweep | "If on an application under this section the court decides that the Auditor General has failed to comply with the obligation in question, it may order" ("on an application") |
| L10 | s 1237(3): `s 1237(3) the revoking order may make the provision with respect to pending proceedings` | (A) JUST FALSE when the gate fails (ruling (b) of the periods, "where" and scope-limits paragraph, taken); (B) NOTHING (the Guide's line that a grant limited by its own wording and a case outside the limit is NOTHING) | (A), unchanged: ASSUMED, NOT RULED, that a "may" function gated by "where", "when", "upon" or an equivalent condition goes with this listed group; a question for the maintainer or a lawyer, not one to settle by sweep | "Where an appointment under section 1228 is revoked, the revoking order may make such provision as the Secretary of State thinks fit with respect to pending proceedings" ("where") |

### Name-test sweep of 2026-11-12

Every layer-1 function whose name contains "may", "permitted", "power", "entitled" or "authorised" was classified: 50 functions. Two were flipped from JUST FALSE to NOTHING (F25, F26 above); ten keep JUST FALSE because the text closes the gate itself; ten answer JUST FALSE on a "where", "when", "upon" or equivalent gate and are listed, not flipped (rows L1-L10 above); none is named "entitled". The other 28 already answer NOTHING outside the limit (they were not JUST FALSE, so they are in no column).

| flipped to NOTHING | kept JUST FALSE (gate closed by the text) | listed: "may" with where/when/upon | listed: "entitled" |
| --- | --- | --- | --- |
| 2 | 10 | 10 | 0 |

- **Flipped to NOTHING:** `s 1234(9) the Independent Supervisor may issue the notice without regard to the restriction in subsection (3)(b)`; `s 1236(1) the Independent Supervisor may make an application to the court`.
- **Kept JUST FALSE:** `s 1213(1) the person may act as statutory auditor of an audited person` and `s 1214(1) the person may act as statutory auditor of the audited person` and `s 1235(1) the Auditor General may act as statutory auditor of the audited person` (flat bars: "No person may act ... if", "must not act"); `s 1221(1) the Secretary of State may declare that the persons are regarded as holding an approved third country qualification` ("only if he is satisfied"); `s 1221(1A) the person may be regarded as holding an approved third country qualification` ("unless"); `s 1224A(3) the information may be disclosed` and `s 1224A(7) the section authorises the disclosure` (flat negatives); `s 1225A(2)(a) the direction may require the body to take the step` ("may only require"); `s 1225C(2) the court may order compliance with the direction` ("may not order ... unless"); `s 1225F(9) the validity of the penalty may be questioned in the legal proceedings` ("is not to be questioned ... Except as provided").
- **Listed, "may" with where/when/upon (or an equivalent condition):** `s 1216(5) the appointment may be treated as extending to the successor`; `s 1225C(1) the court may order the body to take such steps as it considers will secure that the requirement is satisfied or the obligation is complied with`; `s 1225F(4) the court may take the step`; `s 1225F(5) the court may require the payment of interest on the substituted penalty`; `s 1225F(6) the court may require the payment of interest on the penalty from the substituted time`; `s 1225F(7) the court may require the payment of interest on the penalty`; `s 1225G(4) the Secretary of State may recover the unpaid penalty and interest from the body as a debt`; `s 1234(6) the person may make written representations and, if desired, oral representations`; `s 1236(2) the court may order the Auditor General to take such steps as the court directs`; `s 1237(3) the revoking order may make the provision with respect to pending proceedings`.
- **Listed, "entitled":** none.


## Jural relations (coa26)

Hohfeld's correlatives: right and duty, privilege and no-right, power and liability, immunity and disability. One row per provision (or group of provisions with the same relation) that creates a relation; a provision that creates none is listed once as `none`. Each relation is stated once, as a relation between two parties, and encoded by one rule (never from each side).

| provision | holder of the right, privilege, power or immunity | bearer of the correlative duty, no-right, liability or disability | kind | L4 rule |
| --- | --- | --- | --- | --- |
| s 1209 | - | - | none | inert (purpose clause) |
| s 1210(1) | - | - | none (definition of "statutory auditor") | `s 1210(1) the person is a statutory auditor` |
| s 1210(1) closing words | - | - | none (construction rule) | `s 1210(1) the audit is a statutory audit`; `...the work is statutory audit work` |
| s 1210(2), (3) | - | - | none (definitions) | `s 1210(2) ...`; `s 1210(3) ...` x4 |
| s 1210(4) | - | - | none (negative resolution) | inert |
| s 1211 | - | - | none (overview: a necessary condition) | `s 1211 ...` |
| s 1212(1) | the individual or firm (power to be validly appointed) | the company that appoints it (liability: the appointment is effective) | power / liability | `s 1212(1) ...` |
| s 1212(2) | the Secretary of State/law (restriction) | the individual retaining only a 1967 authorisation (disability) | immunity / disability (restricted eligibility) | `s 1212(2) ...` |
| s 1213(1) | the audited person and the public | the ineligible person (duty not to act; SHANT) | claim / duty | `s 1213(1) the person may act ...`; `s 1213(1) the prohibition on acting while ineligible` |
| s 1213(2) | the audited person (claim to resignation and written notice, at once) | the statutory auditor who becomes ineligible | claim / duty | `s 1213(2) ... must immediately resign and give notice`; `s 1213(2) the duty of a statutory auditor ...` |
| s 1213(3), (5), (6) | the Crown (power to prosecute) | the person (liability to conviction) | power / liability | `s 1213(3)`, `s 1213(5)`, `s 1213(6)` `... is guilty of an offence` |
| s 1213(4), (7) | the court (power to sentence) | the person convicted (liability to the fine) | power / liability | `s 1213(4) the penalty ...`; `s 1213(4) the most ...`; `s 1213(7) ...` |
| s 1213(8) | the accused (privilege: a defence) | the prosecution (no-right to conviction on those facts) | privilege / no-right | `s 1213(8) the defence is made out` |
| s 1214(1) | the audited person and the public | the person to whom (2), (3) or (4) applies (duty not to act; SHANT) | claim / duty | `s 1214(1) ...`; `s 1214(1) the prohibition on acting without independence` |
| s 1214(2), (3), (4) | - | - | none (conditions of the bar in (1)) | `s 1214(2)`, `(3)`, `(4)` |
| s 1214(5) | the auditor (immunity: not an officer or employee by being auditor) | the audited person / the bar in (2), (3) (disability) | immunity / disability | `s 1214(5) ...` |
| s 1214(6) | - | - | none (definition of "associated undertaking") | `s 1214(6) ...` |
| s 1214(7) | - | - | none (negative resolution) | inert |
| s 1215(1) | the audited person (claim to resignation and notice) | the statutory auditor who becomes prohibited by s 1214(1) | claim / duty | `s 1215(1) ...`; `s 1215(1) the duty ...` |
| s 1215(2), (4), (5) | the Crown (power to prosecute) | the person (liability to conviction) | power / liability | `s 1215(2)`, `(4)`, `(5)` `... guilty of an offence` |
| s 1215(3), (6) | the court (power to sentence) | the person convicted (liability to the fine) | power / liability | `s 1215(3)`, `s 1215(6)` |
| s 1215(7) | the accused (privilege: a defence) | the prosecution (no-right) | privilege / no-right | `s 1215(7) ...` |
| s 1216(1) | - | - | none (scope of the section) | `s 1216(1) ...` |
| s 1216(2) | the partnership (the appointee) | the partners (no-right to the appointment, unless a contrary intention) | privilege / no-right | `s 1216(2) ...` |
| s 1216(3), (5) | the audited person and the successor (power: the appointment extends) | the successor (liability to hold the appointment); (5) needs the audited person's consent | power / liability | `s 1216(3) ...`; `s 1216(5) ...` |
| s 1216(4), (6) | - | - | none (conditions: "succeeds", "appropriate") | `s 1216(4)(a)`, `(4)(b)`, `s 1216(6)` |
| s 1217(1), (1A), (2), (3) | - | - | none (definitions); (1A): the supervisory body's rules must bind former members (duty of the body) | `s 1217(1)`, `(1A)`, `(2)`, `(3)` x2 |
| s 1217(4) | - | - | none (hand-off to Schedule 10) | `s 1217(4) ...` |
| s 1218(1) | the recognised supervisory body, its officers, employees and governors (immunity from damages) | anyone who would sue them in damages (disability) | immunity / disability | `s 1218(1) ...` |
| s 1218(2), (3), (4) | - | - | none (who and what the immunity covers) | `s 1218(2)`, `(3)`, `(4)` x2 |
| s 1218(5) | the claimant (the immunity does not apply: bad faith; Human Rights Act) | the body (no immunity) | privilege / no-right (removal of the immunity) | `s 1218(5) ...` |
| s 1219(1), (2) | - | - | none (definition of "appropriate qualification") | `s 1219(1)`, `s 1219(2)` |
| s 1220(1), (2), (3) | - | - | none (definitions; hand-off to Schedule 11) | `s 1220(1)`, `(2)` x2, `(3)` |
| s 1221(1), (2), (5), (6), (7), (8) | the Secretary of State (powers to declare, direct, withdraw, vary) | the persons declared or directed about (liability) | power / liability | `s 1221(1)`, `(2)`, `(5)`, `(6)`, `(7)`, `(8)` |
| s 1221(1A), (1B), (3), (4), (7A), (7AA), (7C), (7D) | - | - | none (conditions and counting rules); (7D): the body's rules must govern the adaptation period | `s 1221(1A)`, `(1B)`, `(3)`, `(4)`, `(7A)`, `(7AA)`, `(7C)`, `(7D)` |
| s 1222(1) | the company (the person is eligible only for unquoted companies) | the 1967-authorisation individual (disability) | immunity / disability | `s 1222(1) ...` |
| s 1222(2), (3) | - | - | none (definition; reading rule) | `s 1222(2)`, `s 1222(3)` |
| s 1223(1), (3), 1223ZA(1), (3) | the Secretary of State / the competent authority (power to require) | the recognised body (liability) | power / liability | `s 1223(1)`, `(3)`, `s 1223ZA(1)`, `(3)` |
| s 1223(2), (4), 1223ZA(2), (4) | the Secretary of State / the competent authority (claim that the notice is reasonable and in writing) | the recognised body (duty to give it in writing) | claim / duty | `s 1223(2)`, `(4)`, `s 1223ZA(2)`, `(4)` |
| s 1223A(1), (2) | the Secretary of State (claim to be notified) | the recognised supervisory body (duty to notify) | claim / duty | `s 1223A(1)(a)`, `(b)`, `(c)`, `s 1223A(2)` |
| s 1223A(3) | - | - | none (definition of "notifiable person") | `s 1223A(3)` |
| s 1224(1), (3), 1224ZA(1), (2) | the Secretary of State / the competent authority (power to call for information) | the recognised body or person eligible (liability) | power / liability | `s 1224(1)`, `(3)`, `s 1224ZA(1)`, `(2)` |
| s 1224(2) | - | - | none (who is within the power) | `s 1224(2)` |
| s 1224A(3) | the individual / the business carrier (claim to confidentiality) | the body holding the information (duty not to disclose without consent) | claim / duty | `s 1224A(3) ...` |
| s 1224A(1), (2), (4), (6), (7) | - | - | none (scope and exceptions to the claim in (3)) | `s 1224A(1)`, `(2)`, `(4)`, `(6)`, `(7)` |
| s 1224B(1), (2) | the Crown (power to prosecute; the court's power to sentence) | the person who discloses (liability), with a defence | power / liability; privilege (defence in (1)(a), (b)) | `s 1224B(1)`, `s 1224B(2)` |
| s 1225(1), (3) | - | - | none (when the section applies; powers not prejudiced) | `s 1225(1)`, `s 1225(3)` |
| s 1225(2) | the Secretary of State (power: direction, court application, penalty) | the recognised body (liability) | power / liability | `s 1225(2) ...` |
| s 1225A(1)-(4) | the Secretary of State (power to direct and monitor) | the body directed (liability); (2)(a): immunity of the body from directions it has no power to obey | power / liability; immunity / disability | `s 1225A(1)`, `(2)(a)`, `(2)(b)`, `(3)`, `(4)` |
| s 1225B(1)-(9) | the body (claim to notice, time to respond, consideration of its representations, a reasoned decision, publication) | the Secretary of State (duties) | claim / duty | `s 1225B(1)` to `(9)` |
| s 1225C(1), (2) | the Secretary of State (power to apply); the court (power to order) | the body (liability to the order) | power / liability | `s 1225C(1)`, `(2)` |
| s 1225C(3) | - | - | none (definition of "the court") | `s 1225C(3)` |
| s 1225D(1), (3) | the Secretary of State (power to impose; claim to payment) | the body (liability; duty to pay) | power / liability; claim / duty | `s 1225D(1)`, `(3)` |
| s 1225D(2) | the body (claim that the amount is fixed on proper factors) | the Secretary of State (duty) | claim / duty | `s 1225D(2)` |
| s 1225D(4) | - | - | none (definition) | `s 1225D(4)` |
| s 1225E(1)-(9) | the body (claim to notice, 21 days, consideration, a reasoned decision, 3 months to pay, publication) | the Secretary of State (duties) | claim / duty | `s 1225E(1)` to `(9)` |
| s 1225F(1), (3), (4)-(8) | the body (power to appeal); the court (power over the penalty and interest) | the Secretary of State (liability to have the penalty quashed or reduced) | power / liability | `s 1225F(1)`, `(3)`, `(4)`, `(5)` to `(8)` |
| s 1225F(2), (10) | - | - | none (the grounds; "the court") | `s 1225F(2)`, `(10)` |
| s 1225F(9) | the Secretary of State (immunity: the penalty's validity is not open to challenge except by appeal) | anyone who would challenge it (disability) | immunity / disability | `s 1225F(9)` |
| s 1225G(1), (4) | the Secretary of State (claim to interest; power to recover as a debt) | the body (duty to pay; liability to recovery) | claim / duty; power / liability | `s 1225G(1)`, `(4)` |
| s 1225G(2), (3) | the body (immunity: no payment while an appeal is pending) | the Secretary of State (disability) | immunity / disability | `s 1225G(2)`, `(3)` |
| s 1226(1) | - | - | none (definition) | `s 1226(1)` |
| s 1226(2), (3) | the Auditor General (power to be appointed), subject to a suspension notice | the audited person / company that appoints (liability) | power / liability | `s 1226(2)` |
| s 1227 | the Independent Supervisor and the public (claim) | the Auditor General (duty to secure eligible individuals) | claim / duty | `s 1227` |
| s 1228(1) | the public / Parliament (claim to an Independent Supervisor) | the Secretary of State (duty to appoint) | claim / duty | `s 1228(1)` |
| s 1228(2), (3), (6) | the Secretary of State (power to appoint by order, to designate, to set requirements) | the body appointed (liability) | power / liability | `s 1228(2)`, `(3)`, `(6)` |
| s 1228(4), (5) | - | - | none (conditions of appointment) | `s 1228(4)`, `(5)` |
| s 1228(7) | - | - | none (negative resolution) | inert |
| s 1229(1), (2), (2A), (5), (5A) | each Auditor General (claim to supervision and notice) | the Independent Supervisor (duties) | claim / duty | `s 1229(1)`, `(2)`, `(2A)`, `(5)`, `(5A)` |
| s 1229(3), (3A) | - | - | none (definition; application of Schedule 10) | `s 1229(3)`, `(3A)` |
| s 1229(4), (6), (7) | the Independent Supervisor (privilege to contract; power to fine); the Consolidated Fund (claim to fines) | the body contracted with / the Auditor General (liability to a fine) | privilege / no-right; power / liability | `s 1229(4)`, `(6)`, `(7)` |
| s 1230(1), (2) | the Independent Supervisor and the body (claims to compliance and to a share of costs) | each Auditor General (duties) | claim / duty | `s 1230(1)`, `(2)` |
| s 1230(3), (4) | - | - | none (accounting treatment; definition) | `s 1230(3)`, `(4)` |
| s 1231(1)-(3A), (4) | the Secretary of State, the First Ministers and Parliament/the Assembly (claim to a report and to its laying) | the Independent Supervisor; the Secretary of State; the First Minister for Wales (duties) | claim / duty | `s 1231(1)` to `(4)` |
| s 1232(1), (3), 1233(1), (2) | the Independent Supervisor (power to require) | the Auditor General (liability) | power / liability | `s 1232(1)`, `(3)`, `s 1233(1)`, `(2)` |
| s 1232(2), (4) | the Independent Supervisor (claim to reasonable requirements, in writing) | the Auditor General (duty) | claim / duty | `s 1232(2)`, `(4)` |
| s 1234(1), (9) | the Independent Supervisor (power to issue, amend, revoke a suspension notice) | the Auditor General (liability to suspension) | power / liability | `s 1234(1)`, `(9)` |
| s 1234(2)-(5), (8), (10) | the Auditor General (claim to regard, writing, 3 months' lead time, notice of intention, a copy and publication) | the Independent Supervisor (duties) | claim / duty | `s 1234(2)`, `(3)`, `(4)`, `(5)`, `(8)`, `(10)` |
| s 1234(6) | the Auditor General and any affected person (privilege/power to make representations) | the Independent Supervisor (duty to receive and regard them) | privilege / no-right; claim / duty | `s 1234(6)` |
| s 1234(7), (11) | - | - | none (who may make representations; "specified") | `s 1234(7)`, `(11)` |
| s 1235(1) | the audited person and the public | the Auditor General (duty not to act while a notice has effect; SHANT) | claim / duty | `s 1235(1) ...` |
| s 1235(2) | the audited person (claim to resignation and notice) | the Auditor General | claim / duty | `s 1235(2) ...` |
| s 1235(3) | the Auditor General (immunity from ss 1213 offences by the suspension itself) | the Crown (disability) | immunity / disability | `s 1235(3)` |
| s 1236(1), (2) | the Independent Supervisor (power to apply); the court (power to order) | the Auditor General (liability to the order) | power / liability | `s 1236(1)`, `(2)` |
| s 1236(3) | - | - | none (definition) | `s 1236(3)` |
| s 1237(1) | the unincorporated Independent Supervisor (power to sue and be sued in a body corporate's name) | other parties to the proceedings (liability) | power / liability | `s 1237(1)` |
| s 1237(2) | - | - | none (definition) | `s 1237(2)` |
| s 1237(3) | the Secretary of State (power to make provision about pending proceedings) | parties to pending proceedings (liability) | power / liability | `s 1237(3)` |
| s 1238 | - | - | none (amendment of another Act) | inert |

## Marginal readings for a lawyer (coa26)

The two readings the brief leaves to a lawyer: (a) a failed "if" counts as the text's no, clause by clause, within the provision that holds the "if"; flat negatives count as the text saying no; (b) a prohibition or grant limited by its own wording does not (the case outside the limit is NOTHING). Each branch that rests on one, with the other reading:

**Reading (a): JUST FALSE for a failed "if", "where", "applies if" or a closed list.** The other reading is NOTHING.
- s 1212(1) (failed "if", F11); s 1213(3), (5), (6) and s 1215(2), (4), (5) ("is guilty of an offence if"); s 1214(2), (3), (4) ("applies if"); s 1216(1) ("applies where").
- s 1217(1), (2), (3), 1220(1), (2), 1226(1), 1230(4) and the other "means" and "are the" definitions (JUST FALSE when the facts do not fit), which are not marginal.
- s 1218(2), s 1224(2), s 1225F(2), s 1234(7) (lists closed by "are", F6); s 1218(5) ("does not apply ... if"); s 1219(2) ("is within this subsection if"); s 1221(7AA) ("is a required subject or skill if").
- s 1223A(1), (2), 1229(2A), (5), 1235(2) (duties whose "if" is unmet, F8); s 1223(4), 1223ZA(4), 1232(4), 1224B(1) ("unless" met, F9); s 1216(2).
- s 1225(1) ("applies if"); s 1225C(1), s 1236(2) ("If ... the court decides ... it may"); s 1225F(4)-(8), s 1225G(1), (2), (4), s 1237(3) (a failed "where" or "if" on a power, F10; the listed functions of the name-test sweep, rows L1-L10 below).
- s 1225B(1)-(9), 1225D(2), 1225E(1)-(9), 1227, 1228(1), (2), 1229(1), (2), 1230(1), 1231(2), (3), (3A), 1234(2), (4), (5), (8), (10), 1221(7D), 1223(2) (a bare "must" not done, F7).
- Flat negatives taken as the text's no: s 1213(1), s 1214(1), s 1218(1), s 1224A(3), s 1224A(7), s 1225A(2)(a), s 1225F(9), s 1225G(3), s 1235(1), s 1235(3).

**Reading (b): NOTHING for a case outside a stated limit.** The other reading is JUST FALSE.
- Powers and permissions limited by their own wording: s 1234(9) (F25) and s 1236(1) (F26), moved from JUST FALSE by the name-test sweep of 2026-11-12 (the other reading is JUST FALSE, a failed "if" read as the text's own no); s 1221(2), (5), (6), (7), (8); s 1223(1), (3), s 1223ZA(1), (3), s 1224(1), (3), s 1224ZA(1), (2), s 1232(1), (3), s 1233(1), (2); s 1225(2), (3), s 1225A(2)(b), (3), (4), s 1225B(9), s 1225E(9), s 1228(3), (6), s 1229(3A), (4), (6), (7), s 1231(4), s 1234(1).
- Scope limits: s 1217(1A), s 1217(3) (second sentence), s 1218(3), s 1218(4) (second sentence), s 1220(2) (second sentence), s 1224A(1), (2), (4), (6); s 1226(2), (3); s 1222(3); s 1237(1).
- "only"/"unless" necessary conditions that, when met, leave the question open: s 1211, s 1216(4)(a), (b), s 1221(1A), s 1222(1); and the flat negatives s 1213(1), s 1214(1), s 1235(1), which say no only while the bar bites and answer NOTHING otherwise.
- Silence: s 1213(4) on indictment (no figure), s 1224B(2) for a summary conviction with no stated place.


### Reading a result: FALSE and NOTHING (coa26)

Part 42 is a set of rules about who may be a statutory auditor, what a person must do on becoming ineligible, what bars an auditor for lack of independence, how a partnership's appointment passes on, and how the Secretary of State, the Independent Supervisor and the recognised bodies deal with each other and with the auditors. In this subject's terms:
- **JUST TRUE** is the text saying yes: "the person is a statutory auditor", "the individual is eligible", "the person is guilty of an offence", "the auditor must resign", "the Secretary of State may declare ...".
- **JUST FALSE** is the text saying no in its own words, and each such branch says which words in a comment beginning `FALSE-kind`. In this Part that is: a "means" definition whose limbs are not met ("statutory auditor" means ..., "associated undertaking" means ...); a flat negative ("No person may act as statutory auditor ... if he is ineligible", "No person within subsection (2) is to be liable in damages", "must not act"); an "only if" that is not met ("a body may be appointed only if ..."); and, on the lawyer's readings recorded above, a failed "if" or "where", a bare "must" not done, an "unless" met. `JUST FALSE` never means "nobody could be liable under another Act or instrument": s 1218(1) answers "not liable in damages under this section's exemption", never "liable".
- **NOTHING** is "not covered": the text is silent, lists without closing, says "includes", leaves a term undefined, points outside the sources (another Act, an order, a Schedule, regulations, another part), or limits a grant or prohibition in its own wording and the case falls outside the limit. Each such branch says which in a comment beginning `NOTHING-kind`. Examples: `s 1214(1) the person may act as statutory auditor` is `NOTHING` when none of (2), (3), (4) applies, because the section forbids acting while one of them applies and grants no permission; `s 1211 ...` is `NOTHING` when the person is eligible by Chapter 2 or 3, because "only if" is a necessary condition, and the grant is in s 1212 or s 1226.
- A caller must never turn `NOTHING` into `FALSE`. Where a section needs another section's answer (the Schedule 10 recognition of a body, the s 385 "quoted company" question, the s 1162 parent and subsidiary undertakings), the answer is an input of type `MAYBE BOOLEAN`, and a `NOTHING` input gives a `NOTHING` answer (`NOTHING-kind (points outside the text)`).
- Rulings recorded word for word in the brief and applied here: E1 (option B as guidance only, option C per-section answers everywhere else: each section here answers for itself), N2 (flat negatives count as a no, and `SHANT` is derived where the text names the bearer: ss 1213(1), 1214(1), 1235(1)), the periods ruling (a period the text fixes in its own words: outside it JUST FALSE; a "where" that fails: JUST FALSE; a scope limit with no "only": NOTHING), the delegated-definitions ruling ((a) a hand-off to a Schedule, F13; (b) a defence not proved: "this section gives no defence on these facts", s 1213(8) and s 1215(7); (d) an "until" bar: s 1225G(2) answers JUST TRUE while the appeal is pending and JUST FALSE after it is determined or withdrawn), and the case-by-case decisions recorded as F7, F8, F9, F10 above.


## Seams (coa26)

Each input below is taken as a `MAYBE BOOLEAN` (JUST TRUE, JUST FALSE, NOTHING), unless said otherwise, and named as PLAN.md section 4 names it, so that the lead can wire the answering part's function to it at the merge. The seat layer states each as a yes/no fact and passes `JUST x`.

| input (as named in the module) | answering section and part | used in |
| --- | --- | --- |
| `sch 10 recognised supervisory bodies: the body is a recognised supervisory body` | Schedule 10, para 1 and the recognition order (coa30) | `s 1217(4)`, `s 1212(1)`, `s 1224A(2)`, `s 1223(1)`, `s 1223ZA(1)`, `s 1224(2)` |
| `sch 10 para 7A the supervisory body is a recognised supervisory body` | Schedule 10, para 7A (coa30) | `s 1221(7D)` |
| `sch 11 recognised professional qualifications: the qualification is a recognised professional qualification` and `...the body is a recognised qualifying body` | Schedule 11, para 1 (coa30) | `s 1220(3)`, `s 1219(1)(a)`, `s 1224A(2)` |
| Schedule 11A (specified persons, descriptions, disclosures), asked as three booleans | Schedule 11A, Parts 1, 2, 3 (coa30) | `s 1224A(4)` |
| `s 385 the company is a quoted company within the meaning of section 385(2) at the time of the person's appointment`; `s 385 each parent undertaking ... is a quoted company ...` (a list) | s 385 (coa8) | `s 1222(2)` |
| `s 1162(2) the undertaking is a parent undertaking of the audited person`; `...is a subsidiary undertaking of the audited person`; `...is a subsidiary undertaking of a parent undertaking of the audited person` | s 1162 (the keel) completed by Schedule 7 (coa29) | `s 1214(6)` |
| `s 1173(1) the holder of the position is an officer of the audited person, or an employee of it`; `s 1173(1) the person is an officer of an associated undertaking ..., or an employee of it` | s 1173(1) "officer" (the keel) | `s 1214(5)`, `s 1214(3)` |
| `s 1173(1) the body is the competent authority` (BOOLEAN) | s 1173(1) (the keel) | `s 1224A(2)` |
| `s 1239 the person is also a third country auditor that has been approved by an approved third country competent authority` | s 1239 and s 1240B (coa27) | `s 1223A(3)` |
| `s 1252 the body is designated by the Secretary of State under section 1252` | s 1252 (coa27) | `s 1224A(2)` |
| `s 1212(1) the partnership or other person is eligible ...`, `s 1212(1) the individual is eligible ... by virtue of Chapter 2`, `s 1214(1) the partnership or other person may act ...`, `s 1219(2) ...`, `s 1221(1B) ...`, `s 1224A(1)`, `(2)`, `(4)`, `(6)`, `s 1226(2)` | answered inside this part: the seat layer wires the layer-1 function to the input | `s 1216(6)`, `s 1227`, `s 1219(1)(d)`, `s 1221(1A)`, `s 1224A(3)`, `s 1224B(1)`, `s 1211` |

**Seams the plan lists that turned out not to be seams (false positives of its script).** The plan's row for coa26 says s 1210 cites s 72 and s 77 [coa2], s 1219 cites s 31 [coa1], s 1225 cites Part 2 [coa1], s 1230 cites s 20 [coa1] and s 1238 cites s 16 [coa1]. In the text those are s 72 and s 77 of the Friendly Societies Act 1992 and the Building Societies Act 1986 (s 1210(1)(b), (c)), s 31 of the Companies Act 1989 (s 1219(1)(b)), Part 2 of Schedule 10 (s 1225(1)(a), s 1218(3)(a)), s 20 of the Public Audit (Wales) Act 2013 (s 1230(3)(c)) and s 16 of the Companies (Audit, Investigations and Community Enterprise) Act 2004 (s 1238). None is another part's section. Checked by reading lines 17005-17006, 17152, 17284, 17444 and 17516.
**Seams the plan lacks.** (1) s 1224A(1) cites ss 522 to 524 [coa12] as the occasion on which information is provided; the rule takes it as a fact (`the information is provided in connection with the exercise of the body's functions under ... sections 522 to 524 ...`), not as another part's answer. (2) s 1214(4) uses "associate" (defined outside this range); the connection is an input. (3) s 1223A uses "equivalent third country", "transitional third country" and "approved third country competent authority" (coa27); the facts are inputs. (4) The Statutory Auditors and Third Country Auditors Regulations 2016 and the Audit Regulation (`s 1173(1)` in the keel) are cited in ss 1218, 1223ZA, 1224A and 1225; their content is not needed, and the facts they set are inputs. None of the offences in this Part is an "officer in default" offence, so `s 1121` (coa24) is not asked here.


## What the text turns out to say (findings)

1. **Two versions of one amendment run together in the rendering.** s 1213(7) and s 1215(6) print "one-tenth of the statutory maximumone-tenth of the greater of £5,000 or the amount corresponding to level 4 on the standard scale for summary offences for each day"; s 1229(6) prints "to any personor, in the case of the Auditor General for Wales, for payment by the Wales Audit Office of such a fine"; s 1224A(1) prints "under this Part sections 522 to 524 (notification to appropriate audit authority of resignation or removal of auditor), the Statutory Auditors and Third Country Auditors Regulations 2016 or the Audit Regulation" with the older "this Part" still in; s 1218(4) prints "this Part , the Statutory Auditors ..." with a stray space. The rule encodes the later words and says so in F1 and F4. A reader with the official text should settle each (asserted by the tests only for the chosen reading).
2. **Blank and omitted provisions.** The text shows ". . . ." for s 1210(1)(d) and (g), s 1219(1)(e), s 1219(3), s 1221(7B), s 1221(9), s 1224A(5) and s 1230(3)(a); "..." as an omission marker at lines 17017, 17023 (in s 1210(3)) and 17285 (s 1225(1)(b)); and ". . . ." inside lines 17019 (a defined term of s 1210(3)), 17120 (s 1217(1)) and 17419 (s 1229(3), "does . . . the following"). The eight blank provisions are coverage rows `repealed or blank`; the inline omissions are quoted as they are.
3. **No pound figure in this Part.** The fines are "a fine", "a fine not exceeding the statutory maximum" and, for each day, a tenth of "the greater of £5,000 or the amount corresponding to level 4": the statutory maximum and level 4 are inputs in pounds (`s 1213(4) the most ...`, `s 1213(7) ...`). The only fixed pound figure is the 5,000 in s 1213(7) and s 1215(6).
4. **Offences carry a fine only, except s 1224B.** ss 1213(3), (5), (6) and 1215(2), (4), (5) are fine-only offences (on indictment a fine; on summary conviction the statutory maximum, or the daily fine for the continuing offences). s 1224B(2) adds imprisonment: two years on indictment, 12 months on summary conviction in Scotland, three months on summary conviction in England and Wales or Northern Ireland, "or both". The text names no place for a plain "summary conviction" in s 1224B(2); the encoding answers `NOTHING` there (F23).
5. **The defences need two things.** s 1213(8) and s 1215(7): "he did not know and had no reason to believe": both must be shown. The first alone gives no defence (asserted both ways).
6. **An auditor is not an "officer or employee" by being the auditor** (s 1214(5)); but s 1214(5)'s words "of the person" do not obviously reach s 1214(3), which concerns an associated undertaking (F2).
7. **Eligibility has a second restriction.** s 1212(2) and s 1222: an individual whose only appropriate qualification is a retained authorisation under the Companies Act 1967 is eligible only for appointment as auditor of an unquoted company, and the test of "unquoted" looks at the company and at every parent undertaking of which it is a subsidiary undertaking (a list input), at the time of appointment.
8. **Dates fix the old routes.** s 1219(2): began before 1 January 1990, obtained on or after 1 January 1990 and before 1 January 1996, approved before 1 October 2018. Boundary tests: 31 December 1989 and 1 January 1990; 31 December 1995 and 1 January 1996; 30 September 2018 and 1 October 2018.
9. **Periods in this Part.** 14 days (s 1225B(3)) and 21 days (s 1225E(2)) for representations, "not less than"; three months for payment (s 1225E(7), "at least 3 months after"), for appeal (s 1225F(3), "within the period of 3 months beginning with the day"), for the lead time of a suspension notice (s 1234(3), "after the period of three months beginning with") and for representations (s 1234(6)); three years for an adaptation period (s 1221(7C)); every calendar year for the Independent Supervisor's summary (s 1229(5A)) and report (s 1231(1)). Each has a test on both sides of its end (the month-end question is F5).
10. **"Immediately" means WITHIN 0.** The duties to resign and give notice (ss 1213(2), 1215(1), 1235(2)) are "immediately"; the regulative rules count a trace in days and use `WITHIN 0`. Resigning on the day with the written notice on the same day fulfils the rule; resigning but giving no notice by day 2 is a breach for the notice; not resigning by day 1 is a breach for the resignation (traces recorded below).
11. **The cross-references that point out of the Act.** s 1210(1)(b), (c), (e), (f), (h) and (3) hand "statutory auditor" to the Building Societies Act 1986, the Friendly Societies Act 1992, two 2008 Regulations and an order; s 1219(1)(b), (c) to the Companies Act 1989 and the Companies (Northern Ireland) Order 1990. Each is a fact the person states.
12. **Section numbers.** The range runs s 1209 to s 1238 with inserted sections 1223ZA, 1223A, 1224ZA, 1224A, 1224B and 1225A to 1225G, and inserted subsections (1A), (1B), (2A), (3A), (5A), (7A), (7AA), (7C), (7D) and (3A) of ss 1217, 1221, 1229 and 1231. A line count of the rendering's headings gives 42 section headings in the range.

**Trace outcomes** (read by eye from `l4 run`, because a DEONTIC outcome cannot be asserted on the stable binary; identical on 1.6.110 and 1.6.109):
- s 1213(1): ineligible and acts at day 3: BREACH BY Auditor; not ineligible and acts: FULFILLED.
- s 1213(2): resigns and gives notice at day 0: FULFILLED; resigns but gives no notice (clock to day 2): BREACH BY Auditor ("did not give notice in writing ..."); no resignation (clock to day 1): BREACH BY Auditor ("did not resign his office immediately ...").
- s 1214(1): one of (2), (3), (4) applies and acts at day 1: BREACH; none applies: FULFILLED.
- s 1215(1): the same three outcomes as s 1213(2).
- s 1235(1): suspension notice has effect and acts at day 2: BREACH; no notice: FULFILLED. s 1235(2): the same three outcomes as s 1213(2).

## What the stable binary does not accept (or reads in a way that surprised)

Measured on 1.6.110 (main, e51181d); 1.6.109 read every file the same way (check.sh, main columns).
1. **A DEONTIC value cannot be compared in `#ASSERT`.** The six duties are therefore encoded twice: as regulative rules (traced, outcomes above) and as decision functions (asserted).
2. **`ELSE IF` chains over several lines fail with "incorrect indentation (got N, should be greater than N)"** when the `THEN` branch holds a bracketed expression; `BRANCH` or nested `IF` under `CONSIDER` read the same facts. Every multi-way decision in these modules is a `BRANCH` or a `CONSIDER`.
3. **A multi-line `LIST` as the argument of a function on the next line fails ("unexpected LIST")**; the list is a `WHERE` local (`the limbs`, `the six limbs`).
4. **`JUST term's field` is `(JUST term)'s field`**, a type error in the seat; bracket `JUST (term's field)`.
5. **`NOT a OR b` inside brackets is `NOT (a OR b)`.** One rule (`s 1228(5)`) was wrong for that reason; the test that checks the case where both limbs hold caught it. Every other `NOT` here is `IF NOT x THEN` or `(NOT x)`.
6. **A `WITH` call inside `#ASSERT` swallows a following `EQUALS`**; no assertion here uses `WITH` (calls are positional, and the inputs are listed in a comment above the assertions).
7. **A lambda `GIVEN x YIELD record WITH ...` inside `WHERE` does not parse**; a local helper that names its arguments in the head does (`the penalty term fine MEANS ...`).
8. **`REFUSE`, `#ASSERT REFUSED`, `BECAUSE` (except on `LEST BREACH`), `YMD`, sets, `TYPICALLY`, section `GIVEN`, `EVERY` and `WAIT UNTIL` were not used**, as the brief says. (`WAITUNTIL n` works in a trace on this binary and is used.)
9. **`Date` rolls an impossible day forward**, so a three-month count from a month-end date is F5.
10. A field of an input record is a name too, so the modules use plain `GIVEN` inputs (no records of their own) except the enumerations whose constructors carry a section label.


## What `check.sh` prints

Target `main`. Run as `L4=<L4_BIN> L4_MAIN=<L4_MAIN> ./check.sh` (main build compared: 1.6.109 (main, 4c887e0, 2026-11-04); the binary written with is 1.6.110 (main, e51181d, 2026-11-11)). The baseline it replaced was the folder as the lead supplied it: `coa-core.l4` and `coa-definitions.l4` only, 2 modules, 0 errors, 0 assertions. No assertion is expected to fail, `expected_failed` is unchanged (every module expects 0), and no module is red.

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.109 (main, 4c887e0, 2026-11-04)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
coa-core.l4                                    0         0       0        0         0 |      0         0       0        0  same
coa-definitions.l4                             0         0       0        0         0 |      0         0       0        0  same
coa26-cases-seat.l4                            0       127       0        0         0 |      0       127       0        0  same
coa26-ch1.l4                                   0         0       0        0         0 |      0         0       0        0  same
coa26-ch2a.l4                                  0         0       0        0         0 |      0         0       0        0  same
coa26-ch2b.l4                                  0         0       0        0         0 |      0         0       0        0  same
coa26-ch2c.l4                                  0         0       0        0         0 |      0         0       0        0  same
coa26-ch2d.l4                                  0         0       0        0         0 |      0         0       0        0  same
coa26-ch3a.l4                                  0         0       0        0         0 |      0         0       0        0  same
coa26-ch3b.l4                                  0         0       0        0         0 |      0         0       0        0  same
coa26-seat.l4                                  0         0       0        0         0 |      0         0       0        0  same
coa26-support.l4                               0         0       0        0         0 |      0         0       0        0  same
coa26-tests-ch1.l4                             0        41       0        0         0 |      0        41       0        0  same
coa26-tests-ch2a.l4                            0       138       0        0         0 |      0       138       0        0  same
coa26-tests-ch2b.l4                            0       151       0        0         0 |      0       151       0        0  same
coa26-tests-ch2c.l4                            0       109       0        0         0 |      0       109       0        0  same
coa26-tests-ch2d.l4                            0       151       0        0         0 |      0       151       0        0  same
coa26-tests-ch3a.l4                            0        93       0        0         0 |      0        93       0        0  same
coa26-tests-ch3b.l4                            0        84       0        0         0 |      0        84       0        0  same
coa26-tests-support.l4                         0        38       0        0         0 |      0        38       0        0  same
TOTAL (20 modules)                             0       932       0        0           |      0       932       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```


## Independence

Nothing under `commons`, `<local worktrees>`, `canon`, another run's directory, or `<local tool>` was read for the encoding. The inputs read were the brief, `PLAN.md`, the text, `ENCODING-GUIDE.md`, `COMMONS-CLAUDE.md`, `HEADINGS.md`, `PARTS.md`, the two skills and their references, the seat example `ea-seat.l4`, and the keel's `coa-core.l4` and `coa-definitions.l4` (for the names and the style of the FALSE-kind and NOTHING-kind comments).
Not done: the independent test pass of step 8 of the `encoding-a-subject` skill (no subagents); the expected values were written by the encoder from the text before each run.
