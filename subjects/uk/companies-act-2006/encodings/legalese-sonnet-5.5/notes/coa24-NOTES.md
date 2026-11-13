# NOTES.md: coa24, the Companies Act 2006 (United Kingdom), ss 1092C to 1133

Status (2026-11-13, written by part agent `coa24`, model Sonnet 5.5): a draft. Counts, names and quotations below were checked by the commands named beside them; the readings of the text are the encoder's. No domain expert has read the encoding against the official text.
Ranges: lines 15485-16189 of `ukpga-2006-46.txt` (13,015 words): the second half of Part 35, "The registrar of companies" (from s 1092C to s 1120), and Part 36, "Offences under the Companies Acts and financial penalties" (ss 1121 to 1133).
Target: the stable `l4`: 1.6.110 (main, e51181d, 2026-11-11), whose sha256 is the one the brief gives (`9c7656f7...016c7`, checked with `shasum -a 256`), and a second main build, 1.6.109 (main, 4c887e0, 2026-11-04), for the target check.

## The source, and what this is not

- The text is a plain-text rendering of the Act made by a converter script from legislation.gov.uk (Open Government Licence v3.0); it is not the official text, and nothing here is "verified against the official text".
- `inputs/SOURCES.md`: version 2026-07-16 (a point in time of the latest revised version), text sha256 `959c95c8...a63c` (checked with `shasum -a 256`). Its caveat says the text "may carry more than one extent version of a provision, and prospective provisions"; finding 1 below is that caveat showing in s 1093(4).
- Amounts the Act leaves to other instruments (the pounds of a level on the standard scale, the statutory maximum, the general limit in a magistrates' court) are inputs. No such number is taken from memory; the figures in the tests are labelled test figures.

## Seat

An individual who is, or is about to become, a director, a company secretary or a member (shareholder) of a company registered under the Act, or who deals with one, asking on facts they can state what the Act requires or lets them do, what rights they have against the company or its directors, what they must disclose, file, approve or vote on and by when, and what follows (liability, offences, penalties) if it is not done. (Assumed, not ruled: the Act is addressed to companies, so the individual is whoever stands in a company's management or ownership.)
There is no seat for the registrar, the Secretary of State or a court. A provision that addresses only one of them is encoded in layer 1 for what it decides and, in `coa24-seat.l4`, only for what it means to this person (for example s 1096, the registrar's duty to remove material, is asked as "must the registrar remove it?" by the person who needs it removed).

## Method

1. Read the text of the range, the keel's `PLAN.md`, the Commons guide, both skills and the dialect page; `work/coverage.py` built the coverage rows from the text (below).
2. Layer 1: eleven modules, one per cluster of sections, in dependency order: `coa24-officers` (ss 1121-1123), `coa24-penalty` (ss 1125, 1131), `coa24-identity` (ss 1110A-1110D), `coa24-register` (ss 1092C-1098), `coa24-acsp` (ss 1098A-1098H), `coa24-index` (ss 1099-1101), `coa24-language` (ss 1102-1110), `coa24-disclosure` (ss 1110E-1110G), `coa24-delivery` (ss 1111, 1113-1120), `coa24-false-statements` (ss 1112-1112B), `coa24-prosecution` (ss 1126-1130, 1132-1133; s 1124 and the powers in s 1132A are inert).
   Each rule has an `@ref` with `src:` locators, and its quotation was copied from the text by `srcrefs.py quote` (a build script expands a marker into the quote lines, so no text was typed from memory).
3. Tests: one tests file per module, with expected values decided from the text before the run; three regulative rules (ss 1093(3), 1098E(1), 1113(3)) were also run with `#TRACE`.
4. Layer 2: `coa24-seat.l4` (70 questions, each beginning "Under section N,") and `coa24-cases-seat.l4` (186 cases).
5. Scratch tools: the scripts named in this file (`work/coverage.py`, `work/dispositions.py`, `work/build.py`, `work/checkquotes.py`, `work/traces.sh`, `work/gen_cases.py`) and the templates they read live in `DEPOSIT/../work/`, which is not shipped; the `.l4` files in this folder are the built output of `work/tpl/`.
6. Checks: `check.sh` (target main, both builds), `srcrefs.py check --refs` and `--strict`, and a script that reads every `-- FALSE-kind` and `-- NOTHING-kind` comment and checks its quotation against the text.

## Where `PLAN.md` and the brief differ (the brief governs)

- `PLAN.md` section 4.1 says parts cannot import the keel's `coa-definitions` module and take its answers as inputs; the brief says layer 1 imports both keel modules. Measured on 1.6.110 only: two files that both import `coa-definitions`, imported together by a third that asserts through a keel function, run with no "multiple definitions" error (a scratch probe, not shipped). So `coa24-acsp`, `coa24-false-statements` and the seat import `coa-definitions` and call `s 1173(1) the entity is a firm` (ss 1098E(4), 1112(2), 1112A(2)); the other modules import only `coa-core`.
- The brief refers to "PLAN.md section 8"; the plan has no section 8 (its seams are in section 4). The seams are recorded below under `## Seams (coa24)`.
- The plan names the seam `s 1121 the officer is in default`. Here it is two functions: `s 1121(3) the officer is in default` (limb (3), with the three limbs as inputs) and `s 1121 the person is an officer in default` (both limbs: s 1121(2) and (3)). Wire the seam to whichever the asking part needs.

## Files

`coa-core.l4`, `coa-definitions.l4` (the keel's, read-only copies), `coa24-officers.l4`, `coa24-penalty.l4`, `coa24-identity.l4`, `coa24-register.l4`, `coa24-acsp.l4`, `coa24-index.l4`, `coa24-language.l4`, `coa24-disclosure.l4`, `coa24-delivery.l4`, `coa24-false-statements.l4`, `coa24-prosecution.l4`; tests `coa24-tests-<module>.l4` for each of those eleven; `coa24-seat.l4`, `coa24-cases-seat.l4`; `NOTES.md`, `PROGRESS.md`, `NEEDS-CORE.md`; `check.sh`, `srcrefs.py`, `fetch-main-l4.sh` (supplied).

## Coverage (coa24)

Built by `work/coverage.py` from the text itself: one row per cross-heading, section heading, section text, subsection, paragraph, sub-paragraph, piece of closing words, table row and blank-text line (the primary rows, which tile the range), and one extra row per defined term (which overlap the rows that hold them). Dispositions are hand-written in `work/dispositions.py`; the script checks that every row has one and that every L4 name in it is defined in a module.

Summary, counts per disposition (all 713 rows): encoded 375, fork 50, inert (1) 83, inert (2) 198, repealed or blank in this text 7.

Audit counts: 705 non-blank lines in lines 15485-16189, and every one falls in exactly one primary row (0 in none, 0 in more than one). Text units counted by an independent pattern (a heading, a section number, `(n)`, `(a)`, `(i)` or a table row at the start of a line): 651. Primary rows: 673 = those 651 plus 22 rows the pattern does not count (closing words 11, section text 8, blank text 3). Defined-term rows added: 40. Rows in the table: 713. Before the audit: the first skeleton had 662 primary rows (702 with the 40 defined terms). The audit found that the unnumbered body lines of eight sections had been folded into their heading rows and three lines of dots into the row before them, so that a text unit would have carried a heading's disposition (inert (1)) or a neighbour's; they became rows of their own, giving the 673 primary rows above and 713 rows in all.

There is no `out-of-scope` and no `deferred` row. `inert (1)` is a heading (not operative). `inert (2)` is machinery: a power or duty of the Secretary of State to make regulations, a rule-making power of the registrar, the amendment of another Act (s 1124), or an order- or regulation-procedure subsection. `inert (3)` is not used: the text's own blank lines are rows of `repealed or blank in this text`.

| unit | lines | kind | text (opening words) | disposition | L4 name(s) | note |
| --- | --- | --- | --- | --- | --- | --- |
| s 1092C (heading) | 15485 | section heading | 1092C Privilege against self-incrimination | inert (1) | - | heading: not operative |
| s 1092C(1) | 15486 | subsection | (1) A statement made by a person in response to a requirement under se | encoded | `s 1092C(1) the statement may not be used against the person in the criminal proceedings` |  |
| s 1092C(2) | 15487 | subsection | (2) Subsection (1) applies to any offence other than— | encoded | `s 1092C(2) subsection (1) applies to the offence` | the "other than" exceptions: fork line F9 in NOTES.md |
| s 1092C(2)(a) | 15488 | paragraph | (a) an offence under one of the following provisions (which concern fa | encoded | `s 1092C(2) subsection (1) applies to the offence` | the "other than" exceptions: fork line F9 in NOTES.md |
| s 1092C(2)(a)(i) | 15489 | sub-paragraph | (i) section 1112 or 1112A; | encoded | `s 1092C(2) subsection (1) applies to the offence` | the "other than" exceptions: fork line F9 in NOTES.md |
| s 1092C(2)(a)(ii) | 15490 | sub-paragraph | (ii) section 5 of the Perjury Act 1911; | encoded | `s 1092C(2) subsection (1) applies to the offence` | the "other than" exceptions: fork line F9 in NOTES.md |
| s 1092C(2)(a)(iii) | 15491 | sub-paragraph | (iii) section 44(2) of the Criminal Law (Consolidation) (Scotland) Act | encoded | `s 1092C(2) subsection (1) applies to the offence` | the "other than" exceptions: fork line F9 in NOTES.md |
| s 1092C(2)(a)(iv) | 15492 | sub-paragraph | (iv) Article 10 of the Perjury (Northern Ireland) Order 1979 (S.I. 197 | encoded | `s 1092C(2) subsection (1) applies to the offence` | the "other than" exceptions: fork line F9 in NOTES.md |
| s 1092C(2)(a)(v) | 15493 | sub-paragraph | (v) section 32 or 32A of the Economic Crime (Transparency and Enforcem | encoded | `s 1092C(2) subsection (1) applies to the offence` | the "other than" exceptions: fork line F9 in NOTES.md |
| s 1092C(2)(a)(vi) | 15494 | sub-paragraph | (vi) section 34 or 35 of the Limited Partnerships Act 1907; | encoded | `s 1092C(2) subsection (1) applies to the offence` | the "other than" exceptions: fork line F9 in NOTES.md |
| s 1092C(2)(b) | 15495 | paragraph | (b) any offence, not within paragraph (a), an element of which is the  | encoded | `s 1092C(2) subsection (1) applies to the offence` | the "other than" exceptions: fork line F9 in NOTES.md |
| heading:15496 | 15496 | cross-heading | Correction or removal of material on the register | inert (1) | - | heading: not operative |
| s 1093 (heading) | 15497 | section heading | 1093 Registrar's notice to resolve inconsistency ... | inert (1) | - | heading: not operative |
| s 1093(1) | 15498 | subsection | (1) Where it appears to the registrar that the information contained i | encoded | `s 1093(1) the registrar may give notice to the company`; `s 1093(1)(a)-(b) the notice is a notice of the kind subsection (1) describes` |  |
| s 1093(1)(a) | 15499 | paragraph | (a) stating in what respects the information contained in it appears t | encoded | `s 1093(1) the registrar may give notice to the company`; `s 1093(1)(a)-(b) the notice is a notice of the kind subsection (1) describes` |  |
| s 1093(1)(b) | 15500 | paragraph | (b) requiring the company, within the period of 14 days beginning with | encoded | `s 1093(1)(b) the last day of the period for resolving the inconsistency`; `s 1093(1)(a)-(b) the notice is a notice of the kind subsection (1) describes` | 14 days beginning with the day of issue: last day = day + 13 |
| s 1093(2) | 15501 | subsection | (2) The notice must state the date on which it is issued. | encoded | `s 1093(2) the notice meets the requirement of s 1093(2)` | bare "must": fork line F10 |
| s 1093(3) | 15502 | subsection | (3) If the necessary documents are not delivered within the period spe | encoded | `s 1093(3)(a) the company commits an offence`; `s 1093(3)(b) the officer of the company commits an offence`; `s 1093(3) the company's duty to deliver the necessary documents` |  |
| s 1093(3)(a) | 15503 | paragraph | (a) the company, and | encoded | `s 1093(3)(a) the company commits an offence`; `s 1093(3) the company's duty to deliver the necessary documents` |  |
| s 1093(3)(b) | 15504 | paragraph | (b) every officer of the company who is in default. | encoded | `s 1093(3)(b) the officer of the company commits an offence`; `s 1121 the person is an officer in default` |  |
| s 1093(4) | 15505 | subsection | (4) A person guilty of an offence under subsection (3) is liable on su | fork | `s 1093(4) the punishment for the offence under subsection (3)` | fork F1: two versions of the daily default fine run together in the text; both encoded, and a third constructor answers NOTHING |
| s 1094 (heading) | 15506 | section heading | 1094 Removal of material from the register | inert (1) | - | heading: not operative |
| s 1094(1) | 15507 | subsection | (1) The registrar may remove from the register anything that appears t | encoded | `s 1094(1) the registrar may remove the material from the register`; `s 1094(1) and (3) the registrar may remove the material from the register` |  |
| s 1094(1)(a) | 15508 | paragraph | (a) a document, or material derived from a document, accepted under se | encoded | `s 1094(1) the registrar may remove the material from the register`; `s 1094(1) and (3) the registrar may remove the material from the register` |  |
| s 1094(1)(b) | 15509 | paragraph | (b) unnecessary material as defined by section 1074. | encoded | `s 1094(1) the registrar may remove the material from the register`; `s 1094(1) and (3) the registrar may remove the material from the register` |  |
| s 1094(2) | 15510 | subsection | (2) The power to remove material from the register under this section  | encoded | `s 1094(2) the power to remove material may be exercised` |  |
| s 1094(2)(a) | 15511 | paragraph | (a) on the registrar’s own motion, or | encoded | `s 1094(2) the power to remove material may be exercised` |  |
| s 1094(2)(b) | 15512 | paragraph | (b) on an application made in accordance with regulations under sectio | encoded | `s 1094(2) the power to remove material may be exercised` |  |
| s 1094(3) | 15513 | subsection | (3) The registrar may exercise the power to remove from the register a | encoded | `s 1094(3) the registrar may exercise the power to remove the material`; `s 1094(1) and (3) the registrar may remove the material from the register` | only-if bar once met: fork line F3 |
| s 1094(4) | 15514 | subsection | (4) The Secretary of State may by regulations provide that the registr | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (limits on the registrar's power following an application) |
| s 1094(5) | 15515 | subsection | (5) Regulations under this section are subject to the negative resolut | inert (2) | - | machinery (reason 2): regulations are subject to the negative resolution procedure |
| s 1094A (heading) | 15516 | section heading | 1094A Further provision about removal of material from the register | inert (1) | - | heading: not operative |
| s 1094A(1) | 15517 | subsection | (1) The Secretary of State must by regulations make provision for noti | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (notice of removal; applications for removal; their contents; discretion; negative resolution) |
| s 1094A(2) | 15518 | subsection | (2) The Secretary of State must by regulations make provision in conne | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (notice of removal; applications for removal; their contents; discretion; negative resolution) |
| s 1094A(3) | 15519 | subsection | (3) The provision that may be made under subsection (2) includes provi | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (notice of removal; applications for removal; their contents; discretion; negative resolution) |
| s 1094A(3)(a) | 15520 | paragraph | (a) who may make an application, | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (notice of removal; applications for removal; their contents; discretion; negative resolution) |
| s 1094A(3)(b) | 15521 | paragraph | (b) the information to be included in and documents to accompany an ap | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (notice of removal; applications for removal; their contents; discretion; negative resolution) |
| s 1094A(3)(c) | 15522 | paragraph | (c) the notice to be given of an application and of its outcome, | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (notice of removal; applications for removal; their contents; discretion; negative resolution) |
| s 1094A(3)(d) | 15523 | paragraph | (d) a period in which objections to an application may be made, and | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (notice of removal; applications for removal; their contents; discretion; negative resolution) |
| s 1094A(3)(e) | 15524 | paragraph | (e) how an application is to be determined, including provision as to  | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (notice of removal; applications for removal; their contents; discretion; negative resolution) |
| s 1094A(4) | 15525 | subsection | (4) The provision that may be made by virtue of subsection (3)(e) incl | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (notice of removal; applications for removal; their contents; discretion; negative resolution) |
| s 1094A(4)(a) | 15526 | paragraph | (a) evidence is to be treated by the registrar as conclusive proof tha | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (notice of removal; applications for removal; their contents; discretion; negative resolution) |
| s 1094A(4)(b) | 15527 | paragraph | (b) the power of removal must be exercised. | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (notice of removal; applications for removal; their contents; discretion; negative resolution) |
| s 1094A(5) | 15528 | subsection | (5) Regulations under this section may in particular confer a discreti | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (notice of removal; applications for removal; their contents; discretion; negative resolution) |
| s 1094A(6) | 15529 | subsection | (6) Regulations under this section are subject to the negative resolut | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (notice of removal; applications for removal; their contents; discretion; negative resolution) |
| s 1094AB (heading) | 15530 | section heading | 1094AB Power of court to make consequential orders following removal | inert (1) | - | heading: not operative |
| s 1094AB(1) | 15531 | subsection | (1) Where the registrar removes anything from the register otherwise t | encoded | `s 1094AB(1) the court may make consequential orders on the application` |  |
| s 1094AB(2) | 15532 | subsection | (2) In this section the reference to the registrar removing material f | encoded | `s 1094AB(2) the registrar is treated as having removed material from the register` |  |
| s 1095 (heading) | 15533 | section heading | 1095 Rectification of register on application to registrar | inert (1) | - | heading: not operative |
| s 1095 (blank text) | 15534 | blank text | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | repealed or blank in this text | - | the text shows a row of dots where the provision stood (omitted or repealed) |
| s 1095A (heading) | 15535 | section heading | 1095A Rectification of register to resolve a discrepancy | inert (1) | - | heading: not operative |
| s 1095A (blank text) | 15536 | blank text | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | repealed or blank in this text | - | the text shows a row of dots where the provision stood (omitted or repealed) |
| s 1096 (heading) | 15537 | section heading | 1096 Rectification of the register under court order | inert (1) | - | heading: not operative |
| s 1096(1) | 15538 | subsection | (1) The registrar shall remove from the register any material— | encoded | `s 1096(1) the registrar must remove the material from the register`; `s 1096 the registrar must remove the material from the register under a court order` |  |
| s 1096(1)(a) | 15539 | paragraph | (a) that derives from anything that the court has declared to be inval | encoded | `s 1096(1) the registrar must remove the material from the register`; `s 1096 the registrar must remove the material from the register under a court order` |  |
| s 1096(1)(b) | 15540 | paragraph | (b) that a court declares to be factually inaccurate, or to be derived | encoded | `s 1096(1) the registrar must remove the material from the register`; `s 1096 the registrar must remove the material from the register under a court order` |  |
| s 1096(1) closing words | 15541 | closing words | and that the court directs should be removed from the register. | encoded | `s 1096(1) the registrar must remove the material from the register`; `s 1096 the registrar must remove the material from the register under a court order` |  |
| s 1096(2) | 15542 | subsection | (2) The court order must specify what is to be removed from the regist | encoded | `s 1096(2) the court order meets the requirement of s 1096(2)` | bare "must": fork line F10 |
| s 1096(3) | 15543 | subsection | (3) The court may make an order for the removal from the register of a | encoded | `s 1096(3) the court may make an order for the removal of the material` | a sentence that grants the power and says "only if satisfied": JUST TRUE once met (fork line F3) |
| s 1096(4) | 15544 | subsection | (4) Where in such a case the court does make an order for removal, it  | encoded | `s 1096(4) the court may make consequential orders` |  |
| s 1096(5) | 15545 | subsection | (5) A copy of the court's order must be sent to the registrar for regi | encoded | `s 1096(5) the copy of the order meets the requirement of s 1096(5)` | bare "must": fork line F10 |
| s 1096(5A) | 15546 | subsection | (5A) This section does not apply to any material delivered to the regi | encoded | `s 1096(5A) and (6) section 1096 applies to the material`; `s 1096 the registrar must remove the material from the register under a court order` |  |
| s 1096(6) | 15547 | subsection | (6) This section does not apply where the court has other, specific, p | encoded | `s 1096(5A) and (6) section 1096 applies to the material`; `s 1096 the registrar must remove the material from the register under a court order` |  |
| s 1096(6)(a) | 15548 | paragraph | (a) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | repealed or blank in this text | - | the text shows a row of dots where the provision stood (omitted or repealed) |
| s 1096(6)(b) | 15549 | paragraph | (b) section 859M (rectification of register). | encoded | `s 1096(5A) and (6) section 1096 applies to the material`; `s 1096 the registrar must remove the material from the register under a court order` |  |
| s 1097 (heading) | 15550 | section heading | 1097 Powers of court on ordering removal of material from the register | inert (1) | - | heading: not operative |
| s 1097(1) | 15551 | subsection | (1) Where the court makes an order for the removal of anything from th | encoded | `s 1097(1)-(4) the court may give the direction`; `s 1097(1)-(5) the court may give the direction on these facts` |  |
| s 1097(2) | 15552 | subsection | (2) It may direct that any note on the register that is related to the | encoded | `s 1097(1)-(4) the court may give the direction` |  |
| s 1097(3) | 15553 | subsection | (3) It may direct that its order shall not be available for public ins | encoded | `s 1097(1)-(4) the court may give the direction` |  |
| s 1097(4) | 15554 | subsection | (4) It may direct— | encoded | `s 1097(1)-(4) the court may give the direction` |  |
| s 1097(4)(a) | 15555 | paragraph | (a) that no note shall be made on the register as a result of its orde | encoded | `s 1097(1)-(4) the court may give the direction` |  |
| s 1097(4)(b) | 15556 | paragraph | (b) that any such note shall be restricted to such matters as may be s | encoded | `s 1097(1)-(4) the court may give the direction` |  |
| s 1097(5) | 15557 | subsection | (5) The court shall not give any direction under this section unless i | fork | `s 1097(5) the court may give a direction`; `s 1097(1)-(5) the court may give the direction on these facts` | fork F4: whether limb (a)(i) belongs to note directions and (a)(ii) to the order direction |
| s 1097(5)(a) | 15558 | paragraph | (a) that— | fork | `s 1097(5) the court may give a direction`; `s 1097(1)-(5) the court may give the direction on these facts` | fork F4: whether limb (a)(i) belongs to note directions and (a)(ii) to the order direction |
| s 1097(5)(a)(i) | 15559 | sub-paragraph | (i) the presence on the register of the note or, as the case may be, o | fork | `s 1097(5) the court may give a direction`; `s 1097(1)-(5) the court may give the direction on these facts` | fork F4: whether limb (a)(i) belongs to note directions and (a)(ii) to the order direction |
| s 1097(5)(a)(ii) | 15560 | sub-paragraph | (ii) the availability for public inspection of the court's order, | fork | `s 1097(5) the court may give a direction`; `s 1097(1)-(5) the court may give the direction on these facts` | fork F4: whether limb (a)(i) belongs to note directions and (a)(ii) to the order direction |
| s 1097(5) closing words | 15561 | closing words | may cause damage to the company, and | fork | `s 1097(5) the court may give a direction`; `s 1097(1)-(5) the court may give the direction on these facts` | fork F4: whether limb (a)(i) belongs to note directions and (a)(ii) to the order direction |
| s 1097(5)(b) | 15562 | paragraph | (b) that the company's interest in non-disclosure outweighs any intere | fork | `s 1097(5) the court may give a direction`; `s 1097(1)-(5) the court may give the direction on these facts` | fork F4: whether limb (a)(i) belongs to note directions and (a)(ii) to the order direction |
| s 1097A (heading) | 15563 | section heading | 1097A Rectification of register relating to company registered office | inert (1) | - | heading: not operative |
| s 1097A(1) | 15564 | subsection | (1) The Secretary of State may by regulations make provision authorisi | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (change of registered office; default address; appeal; consequential amendments) |
| s 1097A(1A) | 15565 | subsection | (1A) The regulations may authorise or require the address to be change | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (change of registered office; default address; appeal; consequential amendments) |
| s 1097A(2) | 15566 | subsection | (2) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | repealed or blank in this text | - | the text shows a row of dots where the provision stood (omitted or repealed) |
| s 1097A(3) | 15567 | subsection | (3) The regulations may make provision as to— | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (change of registered office; default address; appeal; consequential amendments) |
| s 1097A(3)(a) | 15568 | paragraph | (a) who may make an application, | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (change of registered office; default address; appeal; consequential amendments) |
| s 1097A(3)(b) | 15569 | paragraph | (b) the information to be included in and documents to accompany an ap | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (change of registered office; default address; appeal; consequential amendments) |
| s 1097A(3)(ba) | 15570 | paragraph | (ba) the registrar requiring the company or an applicant to provide in | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (change of registered office; default address; appeal; consequential amendments) |
| s 1097A(3)(c) | 15571 | paragraph | (c) the notice to be given of an application or that the registrar is  | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (change of registered office; default address; appeal; consequential amendments) |
| s 1097A(3)(ca) | 15572 | paragraph | (ca) the notice to be given of any decision under the regulations, | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (change of registered office; default address; appeal; consequential amendments) |
| s 1097A(3)(d) | 15573 | paragraph | (d) the period in which objections to an application may be made, | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (change of registered office; default address; appeal; consequential amendments) |
| s 1097A(3)(e) | 15574 | paragraph | (e) how the registrar is to determine whether a company’s registered o | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (change of registered office; default address; appeal; consequential amendments) |
| s 1097A(3)(f) | 15575 | paragraph | (f) the referral by the registrar of any question for determination by | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (change of registered office; default address; appeal; consequential amendments) |
| s 1097A(3)(g) | 15576 | paragraph | (g) the registrar requiring a company to provide an address to be the  | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (change of registered office; default address; appeal; consequential amendments) |
| s 1097A(3)(h) | 15577 | paragraph | (h) the nomination by the registrar of an address (a “default address” | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (change of registered office; default address; appeal; consequential amendments) |
| def:s 1097A(3)(h):default address | 15577 | defined term | (h) the nomination by the registrar of an address (a “default address” | inert (2) | - | machinery (reason 2): a label for an address the registrar nominates under regulations; it carries no rule of its own |
| s 1097A(3)(ha) | 15578 | paragraph | (ha) the period for which a company is permitted to have the default a | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (change of registered office; default address; appeal; consequential amendments) |
| s 1097A(3)(i) | 15579 | paragraph | (i) when the change of address takes effect and the consequences of re | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (change of registered office; default address; appeal; consequential amendments) |
| s 1097A(4) | 15580 | subsection | (4) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | repealed or blank in this text | - | the text shows a row of dots where the provision stood (omitted or repealed) |
| s 1097A(4A) | 15581 | subsection | (4A) Provision made by virtue of subsection (3)(ha) may in particular  | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (what the regulations may provide) |
| s 1097A(4A)(a) | 15582 | paragraph | (a) provision creating summary offences punishable with a fine not exc | encoded | `s 1097A(4A)(a) the punishment for a summary offence in the regulations` |  |
| s 1097A(4A)(b) | 15583 | paragraph | (b) provision— | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (strike-off and restoration where a default address is not changed) |
| s 1097A(4A)(b)(i) | 15584 | sub-paragraph | (i) for the registrar to strike a company’s name off the register if t | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (strike-off and restoration where a default address is not changed) |
| s 1097A(4A)(b)(ii) | 15585 | sub-paragraph | (ii) for the restoration of a company to the register, in such circums | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (strike-off and restoration where a default address is not changed) |
| s 1097A(4B) | 15586 | subsection | (4B) The provision that may be made by virtue of subsection (4A) inclu | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (change of registered office; default address; appeal; consequential amendments) |
| s 1097A(4C) | 15587 | subsection | (4C) Regulations under this section may in particular confer a discret | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (change of registered office; default address; appeal; consequential amendments) |
| s 1097A(5) | 15588 | subsection | (5) Provision made by virtue of subsection (3)(i) may in particular in | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (what the regulations may provide as to a default address) |
| s 1097A(5)(a) | 15589 | paragraph | (a) for the suspension, for up to 28 days beginning with the date on w | encoded | `s 1097A(5)(a) the regulations may provide for a suspension of this length`; `s 1097A(5)(a) the last day of a suspension of 28 days` |  |
| s 1097A(5)(b) | 15590 | paragraph | (b) that the default address may not be used for the purpose of keepin | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (what the regulations may provide as to a default address) |
| s 1097A(5)(c) | 15591 | paragraph | (c) for there to be no requirement that documents delivered to the def | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (what the regulations may provide as to a default address) |
| s 1097A(5)(d) | 15592 | paragraph | (d) for the collection of such documents by the company, or the forwar | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (what the regulations may provide as to a default address) |
| s 1097A(5)(e) | 15593 | paragraph | (e) for the circumstances in which, and the period of time after which | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (what the regulations may provide as to a default address) |
| s 1097A(5)(f) | 15594 | paragraph | (f) about evidence, or descriptions of evidence, that the registrar ma | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (what the regulations may provide as to a default address) |
| s 1097A(6) | 15595 | subsection | (6) The regulations must confer a right on a company to appeal to the  | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (change of registered office; default address; appeal; consequential amendments) |
| s 1097A(6A) | 15596 | subsection | (6A) If the regulations enable a person to apply for a company’s regis | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (change of registered office; default address; appeal; consequential amendments) |
| s 1097A(7) | 15597 | subsection | (7) On an appeal, the court must direct the registrar to register such | encoded | `s 1097A(7) the court must direct the registrar to register such address as the registered office as the court considers appropriate` |  |
| s 1097A(8) | 15598 | subsection | (8) The regulations may make further provision about an appeal and in  | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (change of registered office; default address; appeal; consequential amendments) |
| s 1097A(8)(a) | 15599 | paragraph | (a) provision about the time within which an appeal must be brought an | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (change of registered office; default address; appeal; consequential amendments) |
| s 1097A(8)(b) | 15600 | paragraph | (b) provision for the suspension, pending the outcome of an appeal, of | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (change of registered office; default address; appeal; consequential amendments) |
| s 1097A(8)(c) | 15601 | paragraph | (c) further provision about directions by virtue of subsection (7). | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (change of registered office; default address; appeal; consequential amendments) |
| s 1097A(9) | 15602 | subsection | (9) The regulations may include such provision applying (including app | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (change of registered office; default address; appeal; consequential amendments) |
| s 1097A(10) | 15603 | subsection | (10) Regulations under this section are subject to affirmative resolut | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (change of registered office; default address; appeal; consequential amendments) |
| s 1097B (heading) | 15604 | section heading | 1097B Rectification of register: service addresses | inert (1) | - | heading: not operative |
| s 1097B(1) | 15605 | subsection | (1) The Secretary of State may by regulations make provision authorisi | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (change of a registered service address; default address; appeal; consequential amendments) |
| s 1097B(2) | 15606-15608 | subsection | (2) In this section— “registered service address”, in relation to a re | encoded | `s 1097B(2) the address is the registered service address of the relevant person`; `s 1097B(2) the person is a relevant person` |  |
| def:s 1097B(2):registered service address | 15607 | defined term | “registered service address”, in relation to a relevant person, means  | encoded | `s 1097B(2) the address is the registered service address of the relevant person` |  |
| def:s 1097B(2):relevant person | 15608 | defined term | “relevant person” means— | encoded | `s 1097B(2) the person is a relevant person` |  |
| s 1097B(2)(a) | 15609 | paragraph | (a) a director of a company that is not an overseas company, | encoded | `s 1097B(2) the address is the registered service address of the relevant person`; `s 1097B(2) the person is a relevant person` |  |
| s 1097B(2)(b) | 15610 | paragraph | (b) a secretary or one of the joint secretaries of a company that is n | encoded | `s 1097B(2) the address is the registered service address of the relevant person`; `s 1097B(2) the person is a relevant person` |  |
| s 1097B(2)(c) | 15611 | paragraph | (c) a registrable person or registrable relevant legal entity in relat | encoded | `s 1097B(2) the address is the registered service address of the relevant person`; `s 1097B(2) the person is a relevant person` |  |
| s 1097B(3) | 15612 | subsection | (3) The regulations may authorise or require the address to be changed | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (change of a registered service address; default address; appeal; consequential amendments) |
| s 1097B(4) | 15613 | subsection | (4) The regulations must provide for the change in the address to be e | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (change of a registered service address; default address; appeal; consequential amendments) |
| s 1097B(5) | 15614 | subsection | (5) The regulations may make provision as to— | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (change of a registered service address; default address; appeal; consequential amendments) |
| s 1097B(5)(a) | 15615 | paragraph | (a) who may make an application, | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (change of a registered service address; default address; appeal; consequential amendments) |
| s 1097B(5)(b) | 15616 | paragraph | (b) the information to be included in and documents to accompany an ap | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (change of a registered service address; default address; appeal; consequential amendments) |
| s 1097B(5)(c) | 15617 | paragraph | (c) the registrar requiring the company or an applicant to provide inf | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (change of a registered service address; default address; appeal; consequential amendments) |
| s 1097B(5)(d) | 15618 | paragraph | (d) the notice to be given of an application or that the registrar is  | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (change of a registered service address; default address; appeal; consequential amendments) |
| s 1097B(5)(e) | 15619 | paragraph | (e) the notice to be given of any decision under the regulations, | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (change of a registered service address; default address; appeal; consequential amendments) |
| s 1097B(5)(f) | 15620 | paragraph | (f) the period in which objections to an application may be made, | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (change of a registered service address; default address; appeal; consequential amendments) |
| s 1097B(5)(g) | 15621 | paragraph | (g) how the registrar is to determine whether a registered service add | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (change of a registered service address; default address; appeal; consequential amendments) |
| s 1097B(5)(h) | 15622 | paragraph | (h) the referral by the registrar of any question for determination by | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (change of a registered service address; default address; appeal; consequential amendments) |
| s 1097B(5)(i) | 15623 | paragraph | (i) the registrar requiring the company to provide an address to be re | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (change of a registered service address; default address; appeal; consequential amendments) |
| s 1097B(5)(j) | 15624 | paragraph | (j) the nomination by the registrar of an address (a “default address” | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (change of a registered service address; default address; appeal; consequential amendments) |
| def:s 1097B(5)(j):default address | 15624 | defined term | (j) the nomination by the registrar of an address (a “default address” | inert (2) | - | machinery (reason 2): a label for an address the registrar nominates under regulations; it carries no rule of its own |
| s 1097B(5)(k) | 15625 | paragraph | (k) the period for which the default address is permitted to be the re | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (change of a registered service address; default address; appeal; consequential amendments) |
| s 1097B(5)(l) | 15626 | paragraph | (l) when the change of address takes effect and the consequences of re | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (change of a registered service address; default address; appeal; consequential amendments) |
| s 1097B(6) | 15627 | subsection | (6) The provision made by virtue of subsection (5)(k) may in particula | encoded | `s 1097B(6) the punishment for a summary offence in the regulations` |  |
| s 1097B(7) | 15628 | subsection | (7) The regulations must confer a right on the company to appeal to th | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (change of a registered service address; default address; appeal; consequential amendments) |
| s 1097B(8) | 15629 | subsection | (8) If the regulations enable a person to apply for a registered servi | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (change of a registered service address; default address; appeal; consequential amendments) |
| s 1097B(9) | 15630 | subsection | (9) On an appeal, the court must direct the registrar to register such | encoded | `s 1097B(9) the court must direct the registrar to register such address as the relevant person's registered service address as the court considers appropriate` |  |
| s 1097B(10) | 15631 | subsection | (10) The regulations may make further provision about an appeal and in | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (change of a registered service address; default address; appeal; consequential amendments) |
| s 1097B(10)(a) | 15632 | paragraph | (a) provision about the time within which an appeal must be brought an | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (change of a registered service address; default address; appeal; consequential amendments) |
| s 1097B(10)(b) | 15633 | paragraph | (b) further provision about directions by virtue of subsection (9). | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (change of a registered service address; default address; appeal; consequential amendments) |
| s 1097B(11) | 15634 | subsection | (11) The regulations may include such provision applying (including ap | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (change of a registered service address; default address; appeal; consequential amendments) |
| s 1097B(12) | 15635 | subsection | (12) Regulations under this section may in particular confer a discret | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (change of a registered service address; default address; appeal; consequential amendments) |
| s 1097B(13) | 15636 | subsection | (13) Regulations under this section are subject to affirmative resolut | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (change of a registered service address; default address; appeal; consequential amendments) |
| s 1097C (heading) | 15637 | section heading | 1097C Rectification of register: principal office addresses | inert (1) | - | heading: not operative |
| s 1097C(1) | 15638 | subsection | (1) The Secretary of State may by regulations make provision authorisi | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (change of a principal office address; default address; appeal; consequential amendments) |
| s 1097C(2) | 15639-15641 | subsection | (2) In this section— “address registered as the principal office”, in  | encoded | `s 1097C(2) the address is the address registered as the principal office of the relevant person`; `s 1097C(2) the person is a relevant person` |  |
| def:s 1097C(2):address registered as the principal office | 15640 | defined term | “address registered as the principal office”, in relation to a relevan | encoded | `s 1097C(2) the address is the address registered as the principal office of the relevant person` |  |
| def:s 1097C(2):relevant person | 15641 | defined term | “relevant person” means— | encoded | `s 1097C(2) the person is a relevant person` |  |
| s 1097C(2)(a) | 15642 | paragraph | (a) a director of a company that is not an overseas company, | encoded | `s 1097C(2) the address is the address registered as the principal office of the relevant person`; `s 1097C(2) the person is a relevant person` |  |
| s 1097C(2)(b) | 15643 | paragraph | (b) a secretary or one of the joint secretaries of a company that is n | encoded | `s 1097C(2) the address is the address registered as the principal office of the relevant person`; `s 1097C(2) the person is a relevant person` |  |
| s 1097C(2)(c) | 15644 | paragraph | (c) a registrable relevant legal entity in relation to a company (with | encoded | `s 1097C(2) the address is the address registered as the principal office of the relevant person`; `s 1097C(2) the person is a relevant person` |  |
| s 1097C(2)(d) | 15645 | paragraph | (d) a registrable person in relation to a company (within the meaning  | encoded | `s 1097C(2) the address is the address registered as the principal office of the relevant person`; `s 1097C(2) the person is a relevant person` |  |
| s 1097C(3) | 15646 | subsection | (3) The regulations may authorise or require the address to be changed | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (change of a principal office address; default address; appeal; consequential amendments) |
| s 1097C(4) | 15647 | subsection | (4) The regulations must provide for the change in the address to be e | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (change of a principal office address; default address; appeal; consequential amendments) |
| s 1097C(5) | 15648 | subsection | (5) The regulations may make provision as to— | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (change of a principal office address; default address; appeal; consequential amendments) |
| s 1097C(5)(a) | 15649 | paragraph | (a) who may make an application, | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (change of a principal office address; default address; appeal; consequential amendments) |
| s 1097C(5)(b) | 15650 | paragraph | (b) the information to be included in and documents to accompany an ap | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (change of a principal office address; default address; appeal; consequential amendments) |
| s 1097C(5)(c) | 15651 | paragraph | (c) the registrar requiring the company or an applicant to provide inf | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (change of a principal office address; default address; appeal; consequential amendments) |
| s 1097C(5)(d) | 15652 | paragraph | (d) the notice to be given of an application or that the registrar is  | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (change of a principal office address; default address; appeal; consequential amendments) |
| s 1097C(5)(e) | 15653 | paragraph | (e) the notice to be given of any decision under the regulations, | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (change of a principal office address; default address; appeal; consequential amendments) |
| s 1097C(5)(f) | 15654 | paragraph | (f) the period in which objections to an application may be made, | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (change of a principal office address; default address; appeal; consequential amendments) |
| s 1097C(5)(g) | 15655 | paragraph | (g) how the registrar is to determine whether an address registered as | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (change of a principal office address; default address; appeal; consequential amendments) |
| s 1097C(5)(h) | 15656 | paragraph | (h) the referral by the registrar of any question for determination by | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (change of a principal office address; default address; appeal; consequential amendments) |
| s 1097C(5)(i) | 15657 | paragraph | (i) the registrar requiring the company to provide an address to be re | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (change of a principal office address; default address; appeal; consequential amendments) |
| s 1097C(5)(j) | 15658 | paragraph | (j) the nomination by the registrar of an address (a “default address” | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (change of a principal office address; default address; appeal; consequential amendments) |
| def:s 1097C(5)(j):default address | 15658 | defined term | (j) the nomination by the registrar of an address (a “default address” | inert (2) | - | machinery (reason 2): a label for an address the registrar nominates under regulations; it carries no rule of its own |
| s 1097C(5)(k) | 15659 | paragraph | (k) the period for which the default address is permitted to be the ad | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (change of a principal office address; default address; appeal; consequential amendments) |
| s 1097C(5)(l) | 15660 | paragraph | (l) when the change of address takes effect and the consequences of re | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (change of a principal office address; default address; appeal; consequential amendments) |
| s 1097C(6) | 15661 | subsection | (6) The provision made by virtue of subsection (5)(k) may in particula | encoded | `s 1097C(6) the punishment for a summary offence in the regulations` |  |
| s 1097C(7) | 15662 | subsection | (7) The regulations must confer a right on the company to appeal to th | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (change of a principal office address; default address; appeal; consequential amendments) |
| s 1097C(8) | 15663 | subsection | (8) If the regulations enable a person to apply for the address regist | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (change of a principal office address; default address; appeal; consequential amendments) |
| s 1097C(9) | 15664 | subsection | (9) On an appeal, the court must direct the registrar to register such | encoded | `s 1097C(9) the court must direct the registrar to register such address as the principal office of the relevant person as the court considers appropriate` |  |
| s 1097C(10) | 15665 | subsection | (10) The regulations may make further provision about an appeal and in | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (change of a principal office address; default address; appeal; consequential amendments) |
| s 1097C(10)(a) | 15666 | paragraph | (a) provision about the time within which an appeal must be brought an | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (change of a principal office address; default address; appeal; consequential amendments) |
| s 1097C(10)(b) | 15667 | paragraph | (b) further provision about directions by virtue of subsection (9). | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (change of a principal office address; default address; appeal; consequential amendments) |
| s 1097C(11) | 15668 | subsection | (11) The regulations may include such provision applying (including ap | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (change of a principal office address; default address; appeal; consequential amendments) |
| s 1097C(12) | 15669 | subsection | (12) Regulations under this section may in particular confer a discret | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (change of a principal office address; default address; appeal; consequential amendments) |
| s 1097C(13) | 15670 | subsection | (13) Regulations under this section are subject to affirmative resolut | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (change of a principal office address; default address; appeal; consequential amendments) |
| s 1098 (heading) | 15671 | section heading | 1098 Public notice of removal of certain material from the register | inert (1) | - | heading: not operative |
| s 1098(1) | 15672 | subsection | (1) The registrar must cause to be published— | encoded | `s 1098(1) the registrar must cause notice of the removal to be published`; `s 1098(1) the publication meets the requirement of s 1098(1)` |  |
| s 1098(1)(a) | 15673 | paragraph | (a) in the Gazette, or | encoded | `s 1098(1) the registrar must cause notice of the removal to be published`; `s 1098(1) the publication meets the requirement of s 1098(1)` |  |
| s 1098(1)(b) | 15674 | paragraph | (b) in accordance with section 1116 (alternative means of giving publi | encoded | `s 1098(1) the registrar must cause notice of the removal to be published`; `s 1098(1) the publication meets the requirement of s 1098(1)` |  |
| s 1098(1) closing words | 15675 | closing words | notice of the removal from the register of an enhanced disclosure docu | encoded | `s 1098(1) the registrar must cause notice of the removal to be published`; `s 1098(1) the publication meets the requirement of s 1098(1)` |  |
| s 1098(2) | 15676 | subsection | (2) The notice must state the name and registered number of the compan | encoded | `s 1098(2) the notice meets the requirement of s 1098(2)` | bare "must": fork line F10 |
| heading:15677 | 15677 | cross-heading | Authorised corporate service providers | inert (1) | - | heading: not operative |
| s 1098A (heading) | 15678 | section heading | 1098A Meaning of “authorised corporate service provider” | inert (1) | - | heading: not operative |
| s 1098A | 15679 | section text | In this Act “authorised corporate service provider” means a person— | encoded | `s 1098A the person is an authorised corporate service provider` |  |
| def:s 1098A:authorised corporate service provider | 15679 | defined term | In this Act “authorised corporate service provider” means a person— | encoded | `s 1098A the person is an authorised corporate service provider` |  |
| s 1098A(a) | 15680 | paragraph | (a) whose application to the registrar to become an authorised corpora | encoded | `s 1098A the person is an authorised corporate service provider` |  |
| s 1098A(b) | 15681 | paragraph | (b) who has not since ceased to be an authorised corporate service pro | encoded | `s 1098A the person is an authorised corporate service provider` |  |
| s 1098A(c) | 15682 | paragraph | (c) whose status as an authorised corporate service provider is not fo | encoded | `s 1098A the person is an authorised corporate service provider` |  |
| s 1098B (heading) | 15683 | section heading | 1098B Application to become authorised corporate service provider | inert (1) | - | heading: not operative |
| s 1098B(1) | 15684 | subsection | (1) A person may apply to the registrar to become an authorised corpor | fork | `s 1098B(1) the person may apply to become an authorised corporate service provider` | fork F19: a failed "if" gate of a function named for a grant answers NOTHING (name-test sweep) |
| s 1098B(1)(a) | 15685 | paragraph | (a) the person is a relevant person as defined by regulation 8(1) of t | fork | `s 1098B(1) the person may apply to become an authorised corporate service provider` | fork F19: a failed "if" gate of a function named for a grant answers NOTHING (name-test sweep) |
| s 1098B(1)(b) | 15686 | paragraph | (b) in the case of an individual, their identity is verified (see sect | fork | `s 1098B(1) the person may apply to become an authorised corporate service provider` | fork F19: a failed "if" gate of a function named for a grant answers NOTHING (name-test sweep) |
| s 1098B(1)(c) | 15687 | paragraph | (c) the person meets any other requirements imposed by regulations mad | fork | `s 1098B(1) the person may apply to become an authorised corporate service provider` | fork F19: a failed "if" gate of a function named for a grant answers NOTHING (name-test sweep) |
| s 1098B(2) | 15688 | subsection | (2) An application under this section must contain— | encoded | `s 1098B(2) the application meets the requirement of s 1098B(2)` | bare "must": fork line F10 |
| s 1098B(2)(a) | 15689 | paragraph | (a) the name of the applicant’s supervisory authority or authorities f | encoded | `s 1098B(2) the application meets the requirement of s 1098B(2)` | bare "must": fork line F10 |
| s 1098B(2)(b) | 15690 | paragraph | (b) the required information about the applicant (see section 1098C),  | encoded | `s 1098B(2) the application meets the requirement of s 1098B(2)` | bare "must": fork line F10 |
| s 1098B(2)(c) | 15691 | paragraph | (c) in the case of an application by an individual, a statement that t | encoded | `s 1098B(2) the application meets the requirement of s 1098B(2)` | bare "must": fork line F10 |
| s 1098B(2) closing words | 15692 | closing words | (See also section 1098D, which imposes restrictions on who may deliver | encoded | `s 1098B(2) the application meets the requirement of s 1098B(2)` | bare "must": fork line F10 |
| s 1098B(3) | 15693 | subsection | (3) Where an application is made under this section, the registrar mus | encoded | `s 1098B(3) the registrar must check with the supervisory authority` |  |
| s 1098B(4) | 15694 | subsection | (4) Having carried out that check, the registrar must grant the applic | encoded | `s 1098B(4) the registrar must grant the application` | "must ... if": marginal reading (a) |
| s 1098B(4)(a) | 15695 | paragraph | (a) the supervisory authority, or at least one of the supervisory auth | encoded | `s 1098B(4) the registrar must grant the application` | "must ... if": marginal reading (a) |
| s 1098B(4)(b) | 15696 | paragraph | (b) where the applicant is an individual, the registrar is satisfied t | encoded | `s 1098B(4) the registrar must grant the application` | "must ... if": marginal reading (a) |
| s 1098B(4)(c) | 15697 | paragraph | (c) any other conditions that may be specified by regulations made by  | encoded | `s 1098B(4) the registrar must grant the application` | "must ... if": marginal reading (a) |
| s 1098B(4)(d) | 15698 | paragraph | (d) the registrar is not required by subsection (5) to refuse the appl | encoded | `s 1098B(4) the registrar must grant the application` | "must ... if": marginal reading (a) |
| s 1098B(5) | 15699 | subsection | (5) The registrar must refuse the application if it appears to the reg | encoded | `s 1098B(5) the registrar must refuse the application` | "must ... if": marginal reading (a) |
| s 1098B(6) | 15700 | subsection | (6) The provision that can be made in regulations under subsection (4) | inert (2) | - | machinery (reason 2): regulations may confer a discretion on the registrar |
| s 1098B(7) | 15701 | subsection | (7) Regulations under subsection (1)(c) or (4)(c) are subject to affir | inert (2) | - | machinery (reason 2): regulations are subject to the affirmative resolution procedure |
| s 1098B(8) | 15702-15705 | subsection | (8) For the purposes of this section— “Money Laundering Regulations” m | encoded | `s 1098B(8) the Money Laundering Regulations`; `s 1098B(8) the person is supervised by the supervisory authority`; `s 1098B(8) the authority is a supervisory authority` |  |
| def:s 1098B(8):Money Laundering Regulations | 15703 | defined term | “Money Laundering Regulations” means the Money Laundering, Terrorist F | encoded | `s 1098B(8) the Money Laundering Regulations` |  |
| def:s 1098B(8):supervised | 15704 | defined term | “supervised”: a person is supervised by a supervisory authority if reg | encoded | `s 1098B(8) the person is supervised by the supervisory authority` |  |
| def:s 1098B(8):supervisory authority | 15705 | defined term | “supervisory authority” means an authority that is a supervisory autho | encoded | `s 1098B(8) the authority is a supervisory authority` |  |
| s 1098C (heading) | 15706 | section heading | 1098C The required information about an applicant | inert (1) | - | heading: not operative |
| s 1098C(1) | 15707 | subsection | (1) The “required information” about the applicant, in the case of a f | encoded | `s 1098C(1) the application contains the required information about the firm` |  |
| def:s 1098C(1):required information | 15707 | defined term | (1) The “required information” about the applicant, in the case of a f | encoded | `s 1098C(1) the application contains the required information about the firm` |  |
| s 1098C(1)(a) | 15708 | paragraph | (a) firm name, | encoded | `s 1098C(1) the application contains the required information about the firm` |  |
| s 1098C(1)(b) | 15709 | paragraph | (b) principal office, | encoded | `s 1098C(1) the application contains the required information about the firm` |  |
| s 1098C(1)(c) | 15710 | paragraph | (c) a service address, | encoded | `s 1098C(1) the application contains the required information about the firm` |  |
| s 1098C(1)(d) | 15711 | paragraph | (d) an email address, | encoded | `s 1098C(1) the application contains the required information about the firm` |  |
| s 1098C(1)(e) | 15712 | paragraph | (e) the legal form of the firm and the law by which it is governed, .. | encoded | `s 1098C(1) the application contains the required information about the firm` |  |
| s 1098C(1)(ea) | 15713 | paragraph | (ea) any registration number allocated to the firm in respect of its r | encoded | `s 1098C(1) the application contains the required information about the firm` |  |
| s 1098C(1)(f) | 15714 | paragraph | (f) if applicable, any other register in which it is entered (includin | encoded | `s 1098C(1) the application contains the required information about the firm` |  |
| s 1098C(2) | 15715 | subsection | (2) The “required information” about the applicant, in the case of an  | encoded | `s 1098C(2) the application contains the required information about the individual` |  |
| def:s 1098C(2):required information | 15715 | defined term | (2) The “required information” about the applicant, in the case of an  | encoded | `s 1098C(2) the application contains the required information about the individual` |  |
| s 1098C(2)(a) | 15716 | paragraph | (a) name, nationality and date of birth, | encoded | `s 1098C(2) the application contains the required information about the individual` |  |
| s 1098C(2)(b) | 15717 | paragraph | (b) a service address, | encoded | `s 1098C(2) the application contains the required information about the individual` |  |
| s 1098C(2)(c) | 15718 | paragraph | (c) an email address, ... | encoded | `s 1098C(2) the application contains the required information about the individual` |  |
| s 1098C(2)(d) | 15719 | paragraph | (d) the part of the United Kingdom in which the person is usually resi | encoded | `s 1098C(2) the application contains the required information about the individual` |  |
| s 1098C(2)(e) | 15720 | paragraph | (e) any registration number allocated to the individual in respect of  | encoded | `s 1098C(2) the application contains the required information about the individual` |  |
| s 1098C(3) | 15721 | subsection | (3) In subsection (2)(a) “name” means forename and surname. | encoded | `s 1098C(3) the name supplied meets the requirement to contain the applicant's name` |  |
| def:s 1098C(3):name | 15721 | defined term | (3) In subsection (2)(a) “name” means forename and surname. | encoded | `s 1098C(3) the name supplied meets the requirement to contain the applicant's name` |  |
| s 1098C(4) | 15722 | subsection | (4) Where the applicant is a peer or an individual usually known by a  | encoded | `s 1098C(3) the name supplied meets the requirement to contain the applicant's name` |  |
| s 1098C(4A) | 15723 | subsection | (4A) For the purposes of this section “Money Laundering Regulations” h | encoded | `s 1098C(4A) the meaning of "Money Laundering Regulations"` |  |
| s 1098C(5) | 15724 | subsection | (5) The Secretary of State may by regulations— | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (amend the required information; repeal subsection (4)) |
| s 1098C(5)(a) | 15725 | paragraph | (a) amend this section so as to change the required information about  | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (amend the required information; repeal subsection (4)) |
| s 1098C(5)(b) | 15726 | paragraph | (b) repeal subsection (4). | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (amend the required information; repeal subsection (4)) |
| s 1098C(6) | 15727 | subsection | (6) Regulations under this section are subject to affirmative resoluti | inert (2) | - | machinery (reason 2): regulations are subject to the affirmative resolution procedure |
| s 1098D (heading) | 15728 | section heading | 1098D Delivery of applications under section 1098B on behalf of a firm | inert (1) | - | heading: not operative |
| s 1098D | 15729 | section text | An application under section 1098B by a firm mentioned in the first co | encoded | `s 1098D table the position is a relevant officer of the firm`; `s 1098D the application meets the delivery requirements of s 1098D` |  |
| s 1098D(a) | 15730 | paragraph | (a) must be delivered to the registrar on its behalf by a relevant off | encoded | `s 1098D table the position is a relevant officer of the firm`; `s 1098D the application meets the delivery requirements of s 1098D` |  |
| s 1098D(b) | 15731 | paragraph | (b) must be accompanied by a statement by the individual confirming th | encoded | `s 1098D table the position is a relevant officer of the firm`; `s 1098D the application meets the delivery requirements of s 1098D` |  |
| s 1098D table row 1 | 15732 | table row | Firm / Relevant officer | inert (1) | - | the table's header row (column titles): not operative |
| s 1098D table row 2 | 15733 | table row | company / director | encoded | `s 1098D table the position is a relevant officer of the firm` |  |
| s 1098D table row 3 | 15734 | table row | body corporate other than a company / where the body’s affairs are man | encoded | `s 1098D table the position is a relevant officer of the firm` |  |
| s 1098D table row 4 | 15735 | table row | partnership / in relation to a limited partnership, a general partner  | encoded | `s 1098D table the position is a relevant officer of the firm` |  |
| s 1098D table row 5 | 15736 | table row | unincorporated body other than a partnership / where the body’s affair | encoded | `s 1098D table the position is a relevant officer of the firm` |  |
| s 1098E (heading) | 15737 | section heading | 1098E Updating duties of authorised corporate service providers | inert (1) | - | heading: not operative |
| s 1098E(1) | 15738 | subsection | (1) A person who is an authorised corporate service provider must noti | encoded | `s 1098E(1)-(2) the last day for notifying the registrar of the change`; `s 1098E(1) the provider's duty to notify the registrar of the change` |  |
| s 1098E(2) | 15739 | subsection | (2) Where the change is the result of an agreement under regulation 7( | fork | `s 1098E(2) the change cannot yet be treated as having occurred`; `s 1098E(1)-(2) the last day for notifying the registrar of the change` | fork F5: the "until" bar: whether the day of the authority's notice is itself a day on which the change is treated as having occurred |
| s 1098E(3) | 15740 | subsection | (3) A person who, without reasonable excuse, fails to comply with this | encoded | `s 1098E(3) the person commits an offence`; `s 1098E(1)-(3) the person commits an offence by failing to notify the registrar in time` |  |
| s 1098E(4) | 15741 | subsection | (4) Where the offence is committed by a firm, every officer of the fir | encoded | `s 1098E(4) the officer of the firm who is in default also commits the offence` |  |
| s 1098E(5) | 15742 | subsection | (5) A person guilty of an offence under this section is liable on summ | encoded | `s 1098E(5) the punishment on summary conviction` |  |
| s 1098E(5)(a) | 15743 | paragraph | (a) in England and Wales, to a fine; | encoded | `s 1098E(5) the punishment on summary conviction` |  |
| s 1098E(5)(b) | 15744 | paragraph | (b) in Scotland or Northern Ireland, to a fine not exceeding level 5 o | encoded | `s 1098E(5) the punishment on summary conviction` |  |
| s 1098E(6) | 15745 | subsection | (6) In this section “Money Laundering Regulations” and “supervisory au | encoded | `s 1098E(6) the section that gives the meaning of "Money Laundering Regulations" and "supervisory authority"` |  |
| s 1098F (heading) | 15746 | section heading | 1098F Ceasing to be an authorised corporate service provider | inert (1) | - | heading: not operative |
| s 1098F(1) | 15747 | subsection | (1) A person ceases to be an authorised corporate service provider if  | fork | `s 1098F(1) the person ceases to be an authorised corporate service provider` | fork F7: an "if" with other routes in subsection (2): NOTHING taken, JUST FALSE the other reading |
| s 1098F(2) | 15748 | subsection | (2) The Secretary of State may by regulations— | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (other circumstances of ceasing; suspension) |
| s 1098F(2)(a) | 15749 | paragraph | (a) provide for other circumstances in which a person ceases to be an  | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (other circumstances of ceasing; suspension) |
| s 1098F(2)(b) | 15750 | paragraph | (b) provide for circumstances in which the registrar may suspend a per | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (other circumstances of ceasing; suspension) |
| s 1098F(3) | 15751 | subsection | (3) The provision that can be made under subsection (2) includes provi | inert (2) | - | machinery (reason 2): what the regulations may include |
| s 1098F(3)(a) | 15752 | paragraph | (a) procedure; | inert (2) | - | machinery (reason 2): what the regulations may include |
| s 1098F(3)(b) | 15753 | paragraph | (b) the period of a suspension; | inert (2) | - | machinery (reason 2): what the regulations may include |
| s 1098F(3)(c) | 15754 | paragraph | (c) the revocation of a suspension. | inert (2) | - | machinery (reason 2): what the regulations may include |
| s 1098F(4) | 15755 | subsection | (4) The provision that can be made in regulations under subsection (2) | inert (2) | - | machinery (reason 2): regulations may confer a discretion on the registrar |
| s 1098F(5) | 15756 | subsection | (5) Regulations under subsection (2) are subject to affirmative resolu | inert (2) | - | machinery (reason 2): regulations are subject to the affirmative resolution procedure |
| s 1098F(6) | 15757 | subsection | (6) In this section “Money Laundering Regulations” has the meaning giv | encoded | `s 1098F(6) the section that gives the meaning of "Money Laundering Regulations"` |  |
| s 1098G (heading) | 15758 | section heading | 1098G Power to impose duties to provide information | inert (1) | - | heading: not operative |
| s 1098G(1) | 15759 | subsection | (1) The Secretary of State may by regulations require a person who is  | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (duties of providers to give information) |
| s 1098G(2) | 15760 | subsection | (2) The provision that may be made by regulations under subsection (1) | inert (2) | - | machinery (reason 2): what the regulations may include |
| s 1098G(3) | 15761 | subsection | (3) The circumstances that may be specified under section 1098F(2) inc | inert (2) | - | machinery (reason 2): circumstances the regulations under s 1098F(2) may specify |
| s 1098G(4) | 15762 | subsection | (4) Regulations under this section may create offences in relation to  | inert (2) | - | machinery (reason 2): regulations may create offences |
| s 1098G(5) | 15763 | subsection | (5) The regulations must provide for any such offence to be punishable | encoded | `s 1098G(5) the punishment the regulations must provide for an offence` |  |
| s 1098G(5)(a) | 15764 | paragraph | (a) in England and Wales with a fine; | encoded | `s 1098G(5) the punishment the regulations must provide for an offence` |  |
| s 1098G(5)(b) | 15765 | paragraph | (b) in Scotland or Northern Ireland, with a fine not exceeding level 5 | encoded | `s 1098G(5) the punishment the regulations must provide for an offence` |  |
| s 1098G(6) | 15766 | subsection | (6) The provision that can be made in regulations under this section i | inert (2) | - | machinery (reason 2): regulations may confer a discretion on the registrar |
| s 1098G(7) | 15767 | subsection | (7) Regulations under this section are subject to affirmative resoluti | inert (2) | - | machinery (reason 2): regulations are subject to the affirmative resolution procedure |
| s 1098H (heading) | 15768 | section heading | 1098H Power to enable authorisation of foreign corporate service provi | inert (1) | - | heading: not operative |
| s 1098H(1) | 15769 | subsection | (1) The Secretary of State may by regulations make provision for the p | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (authorisation of foreign corporate service providers) |
| s 1098H(2) | 15770 | subsection | (2) In subsection (1) “relevant regulatory regime” means a regulatory  | encoded | `s 1098H(2) the regime is a relevant regulatory regime` |  |
| s 1098H(3) | 15771 | subsection | (3) Regulations under this section— | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (authorisation of foreign corporate service providers) |
| s 1098H(3)(a) | 15772 | paragraph | (a) may amend any of sections 1098B to 1098G or insert new sections in | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (authorisation of foreign corporate service providers) |
| s 1098H(3)(b) | 15773 | paragraph | (b) may make consequential amendments or repeals in other provisions o | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (authorisation of foreign corporate service providers) |
| s 1098H(4) | 15774 | subsection | (4) Regulations under this section are subject to affirmative resoluti | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (authorisation of foreign corporate service providers) |
| s 1098H(5) | 15775 | subsection | (5) In this section “Money Laundering Regulations” has the meaning giv | encoded | `s 1098H(5) the section that gives the meaning of "Money Laundering Regulations"` |  |
| heading:15776 | 15776 | cross-heading | The registrar's index of company names | inert (1) | - | heading: not operative |
| s 1099 (heading) | 15777 | section heading | 1099 The registrar's index of company names | inert (1) | - | heading: not operative |
| s 1099(1) | 15778-15779 | subsection | (1) The registrar of companies must keep an index of the names of the  | encoded | `s 1099(1) the registrar must keep the body's name in the index`; `s 1099(1) the index is the registrar's index of company names` |  |
| def:s 1099(1):the registrar's index of company names | 15779 | defined term | This is “the registrar's index of company names”. | encoded | `s 1099(1) the index is the registrar's index of company names` |  |
| s 1099(2) | 15780 | subsection | (2) This section applies to— | encoded | `s 1099(2)-(3) the section applies to the body` |  |
| s 1099(2)(a) | 15781 | paragraph | (a) UK-registered companies; | encoded | `s 1099(2)-(3) the section applies to the body` |  |
| s 1099(2)(b) | 15782 | paragraph | (b) any body to which any provision of the Companies Acts applies by v | encoded | `s 1099(2)-(3) the section applies to the body` |  |
| s 1099(2)(c) | 15783 | paragraph | (c) overseas companies that have registered particulars with the regis | encoded | `s 1099(2)-(3) the section applies to the body` |  |
| s 1099(3) | 15784 | subsection | (3) This section also applies to— | encoded | `s 1099(2)-(3) the section applies to the body` | the text shows two paragraphs lettered (f): both encoded (finding in NOTES.md) |
| s 1099(3)(a) | 15785 | paragraph | (a) limited partnerships registered in the United Kingdom (within the  | encoded | `s 1099(2)-(3) the section applies to the body` | the text shows two paragraphs lettered (f): both encoded (finding in NOTES.md) |
| s 1099(3)(b) | 15786 | paragraph | (b) limited liability partnerships incorporated in the United Kingdom; | encoded | `s 1099(2)-(3) the section applies to the body` | the text shows two paragraphs lettered (f): both encoded (finding in NOTES.md) |
| s 1099(3)(c) | 15787 | paragraph | (c) UK Economic Interest Groupings; | encoded | `s 1099(2)-(3) the section applies to the body` | the text shows two paragraphs lettered (f): both encoded (finding in NOTES.md) |
| s 1099(3)(ca) | 15788 | paragraph | (ca) EEIG establishments, within the meaning of regulation 2(1) of the | encoded | `s 1099(2)-(3) the section applies to the body` | the text shows two paragraphs lettered (f): both encoded (finding in NOTES.md) |
| s 1099(3)(d) | 15789 | paragraph | (d) open-ended investment companies authorised in the United Kingdom; | encoded | `s 1099(2)-(3) the section applies to the body` | the text shows two paragraphs lettered (f): both encoded (finding in NOTES.md) |
| s 1099(3)(e) | 15790 | paragraph | (e) societies registered under the Industrial and Provident Societies  | encoded | `s 1099(2)-(3) the section applies to the body` | the text shows two paragraphs lettered (f): both encoded (finding in NOTES.md) |
| s 1099(3)(f) | 15791 | paragraph | (f) protected cell companies registered under Part 4 of the Risk Trans | encoded | `s 1099(2)-(3) the section applies to the body` | the text shows two paragraphs lettered (f): both encoded (finding in NOTES.md) |
| s 1099(3)(f) | 15792 | paragraph | (f) charitable incorporated organisations within the meaning of Part 1 | encoded | `s 1099(2)-(3) the section applies to the body` | the text shows two paragraphs lettered (f): both encoded (finding in NOTES.md) |
| s 1099(3)(g) | 15793 | paragraph | (g) Scottish charitable incorporated organisations within the meaning  | encoded | `s 1099(2)-(3) the section applies to the body` | the text shows two paragraphs lettered (f): both encoded (finding in NOTES.md) |
| s 1099(4) | 15794 | subsection | (4) The Secretary of State may by order amend subsection (3)— | inert (2) | - | machinery (reason 2): power of the Secretary of State to amend subsection (3) by order |
| s 1099(4)(a) | 15795 | paragraph | (a) by the addition of any description of body; | inert (2) | - | machinery (reason 2): power of the Secretary of State to amend subsection (3) by order |
| s 1099(4)(b) | 15796 | paragraph | (b) by the deletion of any description of body. | inert (2) | - | machinery (reason 2): power of the Secretary of State to amend subsection (3) by order |
| s 1099(5) | 15797 | subsection | (5) Any such order is subject to negative resolution procedure. | inert (2) | - | machinery (reason 2): order subject to the negative resolution procedure |
| s 1100 (heading) | 15798 | section heading | 1100 Right to inspect index | inert (1) | - | heading: not operative |
| s 1100 | 15799 | section text | Any person may inspect the registrar's index of company names. | encoded | `s 1100 the person may inspect the registrar's index of company names` |  |
| s 1101 (heading) | 15800 | section heading | 1101 Power to amend enactments relating to bodies other than companies | inert (1) | - | heading: not operative |
| s 1101(1) | 15801 | subsection | (1) The Secretary of State may by regulations amend the enactments rel | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (amend enactments relating to bodies other than companies) |
| s 1101(1)(a) | 15802 | paragraph | (a) require the registrar to be provided with information as to the na | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (amend enactments relating to bodies other than companies) |
| s 1101(1)(b) | 15803-15805 | paragraph | (b) make provision in relation to such bodies corresponding to that ma | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (amend enactments relating to bodies other than companies) |
| s 1101(2) | 15806 | subsection | (2) Regulations under this section are subject to affirmative resoluti | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (amend enactments relating to bodies other than companies) |
| heading:15807 | 15807 | cross-heading | Language requirements: translation | inert (1) | - | heading: not operative |
| s 1102 (heading) | 15808 | section heading | 1102 Application of language requirements | inert (1) | - | heading: not operative |
| s 1102(1) | 15809 | subsection | (1) The provisions listed below apply to all documents required to be  | encoded | `s 1102(1) the language provisions apply to the document` |  |
| s 1102(1)(a) | 15810 | paragraph | (a) the Companies Acts, or | encoded | `s 1102(1) the language provisions apply to the document` |  |
| s 1102(1)(b) | 15811 | paragraph | (b) the Insolvency Act 1986 (c. 45) or the Insolvency (Northern Irelan | encoded | `s 1102(1) the language provisions apply to the document` |  |
| s 1102(2) | 15812 | subsection | (2) The Secretary of State may make provision by regulations applying  | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (apply the provisions to documents delivered under other enactments) |
| s 1102(3) | 15813-15817 | subsection | (3) The provisions are— section 1103 (documents to be drawn up and del | encoded | `s 1102(3) the provisions that apply under subsection (1)` |  |
| s 1102(4) | 15818 | subsection | (4) Regulations under this section are subject to negative resolution  | inert (2) | - | machinery (reason 2): regulations are subject to the negative resolution procedure |
| s 1103 (heading) | 15819 | section heading | 1103 Documents to be drawn up and delivered in English | inert (1) | - | heading: not operative |
| s 1103(1) | 15820 | subsection | (1) The general rule is that all documents required to be delivered to | encoded | `s 1103 the document must be drawn up and delivered in English` |  |
| s 1103(2) | 15821-15823 | subsection | (2) This is subject to— section 1104 (documents relating to Welsh comp | encoded | `s 1103 the document must be drawn up and delivered in English` |  |
| s 1104 (heading) | 15824 | section heading | 1104 Documents relating to Welsh companies | inert (1) | - | heading: not operative |
| s 1104(1) | 15825 | subsection | (1) Documents relating to a Welsh company may be drawn up and delivere | encoded | `s 1104(1) the document may be drawn up and delivered in Welsh` |  |
| s 1104(2) | 15826 | subsection | (2) On delivery to the registrar any such document must be accompanied | encoded | `s 1104(2) the document must be accompanied by a certified translation into English`; `s 1104(2) the delivery meets the requirement of s 1104(2)` |  |
| s 1104(2)(a) | 15827 | paragraph | (a) of a description excepted from that requirement by regulations mad | encoded | `s 1104(2) the document must be accompanied by a certified translation into English`; `s 1104(2) the delivery meets the requirement of s 1104(2)` |  |
| s 1104(2)(b) | 15828 | paragraph | (b) in a form prescribed in Welsh (or partly in Welsh and partly in En | encoded | `s 1104(2) the document must be accompanied by a certified translation into English`; `s 1104(2) the delivery meets the requirement of s 1104(2)` |  |
| s 1104(3) | 15829-15830 | subsection | (3) Where a document is properly delivered to the registrar in Welsh w | encoded | `s 1104(3) the registrar must obtain a translation into English`; `s 1104(3) the translation is treated as delivered in accordance with the same provision as the original` |  |
| s 1104(4) | 15831 | subsection | (4) A Welsh company may deliver to the registrar a certified translati | encoded | `s 1104(4) the company may deliver a certified translation into Welsh of the document` |  |
| s 1104(5) | 15832 | subsection | (5) Section 1105 (which requires certified translations into English o | encoded | `s 1104(5) section 1105 applies to the document` |  |
| s 1105 (heading) | 15833 | section heading | 1105 Documents that may be drawn up and delivered in other languages | inert (1) | - | heading: not operative |
| s 1105(1) | 15834 | subsection | (1) Documents to which this section applies may be drawn up and delive | encoded | `s 1105(1) the document may be drawn up and delivered in a language other than English`; `s 1105(1) the delivery meets the requirement of s 1105(1)` |  |
| s 1105(2) | 15835 | subsection | (2) This section applies to— | encoded | `s 1105(2) the section applies to the document` |  |
| s 1105(2)(a) | 15836 | paragraph | (a) agreements required to be forwarded to the registrar under Chapter | encoded | `s 1105(2) the section applies to the document` |  |
| s 1105(2)(b) | 15837 | paragraph | (b) documents required to be delivered under section 400(2)(e) or sect | encoded | `s 1105(2) the section applies to the document` |  |
| s 1105(2)(c) | 15838 | paragraph | (c) certified copies delivered under Part 25 (company charges); | encoded | `s 1105(2) the section applies to the document` |  |
| s 1105(2)(d) | 15839 | paragraph | (d) documents of any other description specified in regulations made b | encoded | `s 1105(2) the section applies to the document` |  |
| s 1105(3) | 15840 | subsection | (3) Regulations under this section are subject to negative resolution  | inert (2) | - | machinery (reason 2): regulations are subject to the negative resolution procedure |
| s 1106 (heading) | 15841 | section heading | 1106 Voluntary filing of translations | inert (1) | - | heading: not operative |
| s 1106(1) | 15842 | subsection | (1) A company may deliver to the registrar one or more certified trans | encoded | `s 1106(1) the company may deliver certified translations of the document` |  |
| s 1106(2) | 15843 | subsection | (2) The Secretary of State may by regulations specify— | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (the languages and descriptions of document for the voluntary facility) |
| s 1106(2)(a) | 15844 | paragraph | (a) the languages, and | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (the languages and descriptions of document for the voluntary facility) |
| s 1106(2)(b) | 15845 | paragraph | (b) the descriptions of document, | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (the languages and descriptions of document for the voluntary facility) |
| s 1106(2) closing words | 15846 | closing words | in relation to which this facility is available. | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (the languages and descriptions of document for the voluntary facility) |
| s 1106(3) | 15847 | subsection | (3) The regulations must provide that it is available as from 1st Janu | encoded | `s 1106(3) the regulations must provide that the facility is available` |  |
| s 1106(3)(a) | 15848 | paragraph | (a) in relation to all the official languages of the European Union, a | encoded | `s 1106(3) the regulations must provide that the facility is available` |  |
| s 1106(3)(b) | 15849 | paragraph | (b) in relation to all documents subject to the Directive disclosure r | encoded | `s 1106(3) the regulations must provide that the facility is available` |  |
| s 1106(4) | 15850 | subsection | (4) The power of the registrar to impose requirements as to the form a | encoded | `s 1106(4) the power of the registrar to impose requirements includes power to impose the requirement` |  |
| s 1106(5) | 15851 | subsection | (5) Regulations under this section are subject to negative resolution  | inert (2) | - | machinery (reason 2): regulations are subject to the negative resolution procedure |
| s 1106(6) | 15852 | subsection | (6) This section does not apply where the original document was delive | encoded | `s 1106(6) section 1106 applies` |  |
| s 1107 (heading) | 15853 | section heading | 1107 Certified translations | inert (1) | - | heading: not operative |
| s 1107(1) | 15854 | subsection | (1) In this Part a “certified translation” means a translation certifi | encoded | `s 1107(1) the translation is a certified translation` |  |
| def:s 1107(1):certified translation | 15854 | defined term | (1) In this Part a “certified translation” means a translation certifi | encoded | `s 1107(1) the translation is a certified translation` |  |
| s 1107(2) | 15855 | subsection | (2) In the case of any discrepancy between the original language versi | encoded | `s 1107(2)(a) the company may rely on the translation as against a third party`; `s 1107(2)(b) the third party may rely on the translation` |  |
| s 1107(2)(a) | 15856 | paragraph | (a) the company may not rely on the translation as against a third par | encoded | `s 1107(2)(a) the company may rely on the translation as against a third party`; `s 1107(2)(b) the third party may rely on the translation` |  |
| s 1107(2)(b) | 15857 | paragraph | (b) a third party may rely on the translation unless the company shows | encoded | `s 1107(2)(a) the company may rely on the translation as against a third party`; `s 1107(2)(b) the third party may rely on the translation` |  |
| s 1107(3) | 15858 | subsection | (3) A “third party” means a person other than the company or the regis | encoded | `s 1107(3) the person is a third party` |  |
| def:s 1107(3):third party | 15858 | defined term | (3) A “third party” means a person other than the company or the regis | encoded | `s 1107(3) the person is a third party` |  |
| heading:15859 | 15859 | cross-heading | Language requirements: transliteration | inert (1) | - | heading: not operative |
| s 1108 (heading) | 15860 | section heading | 1108 Transliteration of names and addresses: permitted characters | inert (1) | - | heading: not operative |
| s 1108(1) | 15861 | subsection | (1) Names and addresses in a document delivered to the registrar must  | encoded | `s 1108(1) the names and addresses meet the requirement of s 1108(1)` |  |
| s 1108(2) | 15862 | subsection | (2) The Secretary of State may make provision by regulations— | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (permitted characters; delivery without transliteration) |
| s 1108(2)(a) | 15863 | paragraph | (a) as to the letters, characters and symbols (including accents and o | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (permitted characters; delivery without transliteration) |
| s 1108(2)(b) | 15864 | paragraph | (b) permitting or requiring the delivery of documents in which names a | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (permitted characters; delivery without transliteration) |
| s 1108(3) | 15865 | subsection | (3) Regulations under this section are subject to negative resolution  | inert (2) | - | machinery (reason 2): regulations are subject to the negative resolution procedure |
| s 1109 (heading) | 15866 | section heading | 1109 Transliteration of names and addresses: voluntary transliteration | inert (1) | - | heading: not operative |
| s 1109(1) | 15867 | subsection | (1) Where a name or address is or has been delivered to the registrar  | encoded | `s 1109(1) the company or other body may deliver a transliteration into Roman characters` |  |
| s 1109(2) | 15868 | subsection | (2) The power of the registrar to impose requirements as to the form a | encoded | `s 1109(2) the power of the registrar to impose requirements includes power to impose the requirement` |  |
| s 1110 (heading) | 15869 | section heading | 1110 Transliteration of names and addresses: certification | inert (1) | - | heading: not operative |
| s 1110(1) | 15870 | subsection | (1) The Secretary of State may make provision by regulations requiring | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (certification of transliterations) |
| s 1110(2) | 15871 | subsection | (2) Different provision may be made for compulsory and voluntary trans | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (certification of transliterations) |
| s 1110(3) | 15872 | subsection | (3) Regulations under this section are subject to negative resolution  | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (certification of transliterations) |
| heading:15873 | 15873 | cross-heading | Identity verification | inert (1) | - | heading: not operative |
| s 1110A (heading) | 15874 | section heading | 1110A Meaning of “identity is verified” | inert (1) | - | heading: not operative |
| s 1110A(1) | 15875 | subsection | (1) For the purposes of this Act an individual’s “identity is verified | encoded | `s 1110A(1) the individual's identity is verified` |  |
| def:s 1110A(1):identity is verified | 15875 | defined term | (1) For the purposes of this Act an individual’s “identity is verified | encoded | `s 1110A(1) the individual's identity is verified` |  |
| s 1110A(1)(a) | 15876 | paragraph | (a) the individual’s identity has been verified by the registrar in ac | encoded | `s 1110A(1) the individual's identity is verified` |  |
| s 1110A(1)(b) | 15877 | paragraph | (b) a verification statement in respect of the individual has been del | encoded | `s 1110A(1) the individual's identity is verified` |  |
| s 1110A(1) closing words | 15878 | closing words | and the individual has not, since then, ceased to be an individual who | encoded | `s 1110A(1) the individual's identity is verified` |  |
| s 1110A(2) | 15879 | subsection | (2) A verification statement is a statement by an authorised corporate | encoded | `s 1110A(2) the statement is a verification statement` |  |
| def:s 1110A(2):verification statement | 15879 | defined term | (2) A verification statement is a statement by an authorised corporate | encoded | `s 1110A(2) the statement is a verification statement` |  |
| s 1110A(3) | 15880 | subsection | (3) A verification statement must also specify the authorised corporat | encoded | `s 1110A(3) the verification statement meets the requirement to specify the supervisory authority` | bare "must": fork line F10 |
| s 1110A(4) | 15881 | subsection | (4) The Secretary of State may by regulations make further provision a | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (the contents of verification statements) |
| s 1110A(5) | 15882 | subsection | (5) Where a person is required or authorised by any other provision to | encoded | `s 1110A(5) the statement may be delivered at the same time as the verification statement` |  |
| s 1110A(6) | 15883 | subsection | (6) The Secretary of State may by regulations provide for circumstance | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (circumstances in which someone ceases to be verified) |
| s 1110A(7) | 15884 | subsection | (7) The provision that can be made under subsection (6) includes— | inert (2) | - | machinery (reason 2): what the regulations under subsection (6) may include |
| s 1110A(7)(a) | 15885 | paragraph | (a) provision to confer a discretion on the registrar; | inert (2) | - | machinery (reason 2): what the regulations under subsection (6) may include |
| s 1110A(7)(b) | 15886 | paragraph | (b) provision that someone ceases to be an individual whose identity i | inert (2) | - | machinery (reason 2): what the regulations under subsection (6) may include |
| s 1110A(7)(b)(i) | 15887 | sub-paragraph | (i) their identity is reverified by the registrar in accordance with r | inert (2) | - | machinery (reason 2): what the regulations under subsection (6) may include |
| s 1110A(7)(b)(ii) | 15888 | sub-paragraph | (ii) an authorised corporate service provider delivers to the registra | inert (2) | - | machinery (reason 2): what the regulations under subsection (6) may include |
| s 1110A(8) | 15889 | subsection | (8) Regulations under this section are subject to affirmative resoluti | inert (2) | - | machinery (reason 2): regulations are subject to the affirmative resolution procedure |
| s 1110A(9) | 15890-15892 | subsection | (9) In this section— “Money Laundering Regulations” means the Money La | encoded | `s 1110A(9) the Money Laundering Regulations`; `s 1110A(9) the authority is a supervisory authority` |  |
| def:s 1110A(9):Money Laundering Regulations | 15891 | defined term | “Money Laundering Regulations” means the Money Laundering, Terrorist F | encoded | `s 1110A(9) the Money Laundering Regulations` |  |
| def:s 1110A(9):supervisory authority | 15892 | defined term | “supervisory authority” means an authority that is a supervisory autho | encoded | `s 1110A(9) the authority is a supervisory authority` |  |
| s 1110B (heading) | 15893 | section heading | 1110B Verification requirements | inert (1) | - | heading: not operative |
| s 1110B(1) | 15894 | subsection | (1) The Secretary of State may by regulations make provision for and i | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (verification or reverification of identity) |
| s 1110B(2) | 15895 | subsection | (2) The regulations may, in particular, make provision about— | inert (2) | - | machinery (reason 2): what the regulations may provide about procedure and records |
| s 1110B(2)(a) | 15896 | paragraph | (a) the procedure for verifying or reverifying an individual’s identit | inert (2) | - | machinery (reason 2): what the regulations may provide about procedure and records |
| s 1110B(2)(b) | 15897 | paragraph | (b) the records that a person who is or has been an authorised corpora | inert (2) | - | machinery (reason 2): what the regulations may provide about procedure and records |
| s 1110B(3) | 15898 | subsection | (3) The regulations may create offences in relation to failures to com | inert (2) | - | machinery (reason 2): regulations may create offences |
| s 1110B(4) | 15899 | subsection | (4) The regulations must provide for any such offence to be punishable | encoded | `s 1110B(4) the punishment the regulations must provide for an offence` |  |
| s 1110B(4)(a) | 15900 | paragraph | (a) on conviction on indictment, by imprisonment for a term not exceed | encoded | `s 1110B(4) the punishment the regulations must provide for an offence` |  |
| s 1110B(4)(b) | 15901 | paragraph | (b) on summary conviction— | encoded | `s 1110B(4) the punishment the regulations must provide for an offence` |  |
| s 1110B(4)(b)(i) | 15902 | sub-paragraph | (i) in England and Wales, by imprisonment for a term not exceeding the | encoded | `s 1110B(4) the punishment the regulations must provide for an offence` |  |
| s 1110B(4)(b)(ii) | 15903 | sub-paragraph | (ii) in Scotland, by imprisonment for a term not exceeding 12 months o | encoded | `s 1110B(4) the punishment the regulations must provide for an offence` |  |
| s 1110B(4)(b)(iii) | 15904 | sub-paragraph | (iii) in Northern Ireland, by imprisonment for a term not exceeding 6  | encoded | `s 1110B(4) the punishment the regulations must provide for an offence` |  |
| s 1110B(5) | 15905 | subsection | (5) The provision that can be made in regulations under this section i | inert (2) | - | machinery (reason 2): regulations may confer a discretion on the registrar |
| s 1110B(6) | 15906 | subsection | (6) Regulations under this section are subject to affirmative resoluti | inert (2) | - | machinery (reason 2): regulations are subject to the affirmative resolution procedure |
| s 1110C (heading) | 15907 | section heading | 1110C Identity verification: exemption on national security grounds et | inert (1) | - | heading: not operative |
| s 1110C(1) | 15908 | subsection | (1) The Secretary of State may, by written notice given to a person, p | fork | `s 1110C(1) the Secretary of State may give the notice` | fork F21: a failed "if" gate of a function named for a power answers NOTHING (name-test sweep) |
| s 1110C(1)(a) | 15909 | paragraph | (a) in the interests of national security, or | fork | `s 1110C(1) the Secretary of State may give the notice` | fork F21: a failed "if" gate of a function named for a power answers NOTHING (name-test sweep) |
| s 1110C(1)(b) | 15910 | paragraph | (b) for the purposes of preventing or detecting serious crime. | fork | `s 1110C(1) the Secretary of State may give the notice` | fork F21: a failed "if" gate of a function named for a power answers NOTHING (name-test sweep) |
| s 1110C(2) | 15911 | subsection | (2) The effects for which the notice may provide are that— | encoded | `s 1110C(2) the effect applies in relation to the person`; `s 1110C(2) the provision the effect concerns` |  |
| s 1110C(2)(a) | 15912 | paragraph | (a) where a statement of proposed officers names the person as a direc | encoded | `s 1110C(2) the effect applies in relation to the person`; `s 1110C(2) the provision the effect concerns` |  |
| s 1110C(2)(b) | 15913 | paragraph | (b) section 167G(3)(c) does not apply in relation to a notice of the p | encoded | `s 1110C(2) the effect applies in relation to the person`; `s 1110C(2) the provision the effect concerns` |  |
| s 1110C(2)(c) | 15914 | paragraph | (c) section 167M(1) does not apply in relation to the person and secti | encoded | `s 1110C(2) the effect applies in relation to the person`; `s 1110C(2) the provision the effect concerns` |  |
| s 1110C(2)(d) | 15915 | paragraph | (d) section 167N(1) does not apply in relation to the person; | encoded | `s 1110C(2) the effect applies in relation to the person`; `s 1110C(2) the provision the effect concerns` |  |
| s 1110C(2)(e) | 15916 | paragraph | (e) section 1067A does not apply in relation to the delivery of docume | encoded | `s 1110C(2) the effect applies in relation to the person`; `s 1110C(2) the provision the effect concerns` |  |
| s 1110C(2)(f) | 15917 | paragraph | (f) section 1098B(2)(c) does not apply in relation to the person. | encoded | `s 1110C(2) the effect applies in relation to the person`; `s 1110C(2) the provision the effect concerns` |  |
| s 1110C(3) | 15918 | subsection | (3) For the purposes of subsection (1)(b)— | encoded | `s 1110C(3)(a) the conduct is crime`; `s 1110C(3)(b) the crime is serious` |  |
| s 1110C(3)(a) | 15919 | paragraph | (a) “crime” means conduct which— | encoded | `s 1110C(3)(a) the conduct is crime`; `s 1110C(3)(b) the crime is serious` |  |
| def:s 1110C(3)(a):crime | 15919 | defined term | (a) “crime” means conduct which— | encoded | `s 1110C(3)(a) the conduct is crime` |  |
| s 1110C(3)(a)(i) | 15920 | sub-paragraph | (i) constitutes a criminal offence, or | encoded | `s 1110C(3)(a) the conduct is crime`; `s 1110C(3)(b) the crime is serious` |  |
| s 1110C(3)(a)(ii) | 15921 | sub-paragraph | (ii) is, or corresponds to, any conduct which, if it all took place in | encoded | `s 1110C(3)(a) the conduct is crime`; `s 1110C(3)(b) the crime is serious` |  |
| s 1110C(3)(b) | 15922 | paragraph | (b) crime is “serious” if— | encoded | `s 1110C(3)(a) the conduct is crime`; `s 1110C(3)(b) the crime is serious` |  |
| def:s 1110C(3)(b):serious | 15922 | defined term | (b) crime is “serious” if— | encoded | `s 1110C(3)(b) the crime is serious` |  |
| s 1110C(3)(b)(i) | 15923 | sub-paragraph | (i) the offence which is or would be constituted by the conduct is an  | encoded | `s 1110C(3)(a) the conduct is crime`; `s 1110C(3)(b) the crime is serious` |  |
| s 1110C(3)(b)(ii) | 15924 | sub-paragraph | (ii) the conduct involves the use of violence, results in substantial  | encoded | `s 1110C(3)(a) the conduct is crime`; `s 1110C(3)(b) the crime is serious` |  |
| heading:15925 | 15925 | cross-heading | Discrepancy reporting | inert (1) | - | heading: not operative |
| s 1110D (heading) | 15926 | section heading | 1110D Power to require businesses to report discrepancies | inert (1) | - | heading: not operative |
| s 1110D(1) | 15927 | subsection | (1) The Secretary of State may by regulations impose requirements on a | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (requirements on persons carrying on business to report discrepancies) |
| def:s 1110D(1):relevant person | 15927 | defined term | (1) The Secretary of State may by regulations impose requirements on a | encoded | `s 1110D(1) the person is a relevant person` |  |
| s 1110D(1)(a) | 15928 | paragraph | (a) to obtain specified information about a customer (or prospective c | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (requirements on persons carrying on business to report discrepancies) |
| s 1110D(1)(a)(i) | 15929 | sub-paragraph | (i) before entering into a business relationship with them, or | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (requirements on persons carrying on business to report discrepancies) |
| s 1110D(1)(a)(ii) | 15930 | sub-paragraph | (ii) during a business relationship with them, | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (requirements on persons carrying on business to report discrepancies) |
| s 1110D(1)(b) | 15931 | paragraph | (b) to identify discrepancies between information so obtained and info | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (requirements on persons carrying on business to report discrepancies) |
| s 1110D(1)(c) | 15932 | paragraph | (c) to report any discrepancies to the registrar. | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (requirements on persons carrying on business to report discrepancies) |
| s 1110D(2) | 15933 | subsection | (2) The regulations may require the relevant person, when reporting di | inert (2) | - | machinery (reason 2): what the regulations may require |
| s 1110D(3) | 15934 | subsection | (3) The regulations may provide for reports or other information deliv | inert (2) | - | machinery (reason 2): regulations may provide for reports to be withheld from public inspection |
| s 1110D(4) | 15935 | subsection | (4) The regulations may create offences in relation to failures to com | inert (2) | - | machinery (reason 2): regulations may create offences |
| s 1110D(5) | 15936 | subsection | (5) The regulations may not provide for an offence created by the regu | encoded | `s 1110D(5) the regulations may provide for imprisonment of this term` |  |
| s 1110D(5)(a) | 15937 | paragraph | (a) in the case of conviction on indictment, 2 years; | encoded | `s 1110D(5) the regulations may provide for imprisonment of this term` |  |
| s 1110D(5)(b) | 15938 | paragraph | (b) in the case of summary conviction, 3 months. | encoded | `s 1110D(5) the regulations may provide for imprisonment of this term` |  |
| s 1110D(6) | 15939 | subsection | (6) In this section “customer”, in relation to a person carrying out e | encoded | `s 1110D(6) the person is a customer` |  |
| def:s 1110D(6):customer | 15939 | defined term | (6) In this section “customer”, in relation to a person carrying out e | encoded | `s 1110D(6) the person is a customer` |  |
| s 1110D(7) | 15940 | subsection | (7) Regulations under this section are subject to affirmative resoluti | inert (2) | - | machinery (reason 2): regulations are subject to the affirmative resolution procedure |
| heading:15941 | 15941 | cross-heading | Disclosure of information | inert (1) | - | heading: not operative |
| s 1110E (heading) | 15942 | section heading | 1110E Disclosure to the registrar | inert (1) | - | heading: not operative |
| s 1110E | 15943 | section text | Any person may disclose information to the registrar for the purposes  | encoded | `s 1110E the person may disclose the information to the registrar` |  |
| s 1110F (heading) | 15944 | section heading | 1110F Disclosure by the registrar | inert (1) | - | heading: not operative |
| s 1110F(1) | 15945 | subsection | (1) The registrar may disclose information— | encoded | `s 1110F(1) the registrar may disclose the information` |  |
| s 1110F(1)(a) | 15946 | paragraph | (a) to any person for purposes connected with the exercise of any of t | encoded | `s 1110F(1) the registrar may disclose the information` |  |
| s 1110F(1)(b) | 15947 | paragraph | (b) to a public authority for purposes connected with the exercise of  | encoded | `s 1110F(1) the registrar may disclose the information` |  |
| s 1110F(1)(c) | 15948 | paragraph | (c) to a person of a description, and for a purpose, specified in regu | encoded | `s 1110F(1) the registrar may disclose the information` |  |
| s 1110F(2) | 15949 | subsection | (2) Regulations under subsection (1)(c) are subject to affirmative res | inert (2) | - | machinery (reason 2): regulations are subject to the affirmative resolution procedure |
| s 1110F(3) | 15950 | subsection | (3) In this section “public authority” includes any person or body hav | encoded | `s 1110F(3) the person or body is a public authority` |  |
| def:s 1110F(3):public authority | 15950 | defined term | (3) In this section “public authority” includes any person or body hav | encoded | `s 1110F(3) the person or body is a public authority` |  |
| s 1110G (heading) | 15951 | section heading | 1110G Disclosure: supplementary | inert (1) | - | heading: not operative |
| s 1110G(1) | 15952 | subsection | (1) Except as provided by subsection (2), the disclosure of informatio | encoded | `s 1110G(1) the disclosure breaches an obligation of confidence or any other restriction on the disclosure of information` |  |
| s 1110G(1)(a) | 15953 | paragraph | (a) any obligation of confidence owed by the person making the disclos | encoded | `s 1110G(1) the disclosure breaches an obligation of confidence or any other restriction on the disclosure of information` |  |
| s 1110G(1)(b) | 15954 | paragraph | (b) any other restriction on the disclosure of information (however im | encoded | `s 1110G(1) the disclosure breaches an obligation of confidence or any other restriction on the disclosure of information` |  |
| s 1110G(2) | 15955 | subsection | (2) Sections 1110E and 1110F do not authorise a disclosure of informat | encoded | `s 1110G(2) sections 1110E and 1110F authorise the disclosure` |  |
| s 1110G(3) | 15956 | subsection | (3) HMRC information may not be disclosed by the registrar under secti | encoded | `s 1110G(3) the registrar may disclose the information under section 1110F` |  |
| s 1110G(4) | 15957 | subsection | (4) If the registrar discloses HMRC information under section 1110F, t | encoded | `s 1110G(4) the recipient, or a person obtaining the information from the recipient, may disclose the information` |  |
| s 1110G(5) | 15958 | subsection | (5) It is an offence for a person to disclose, in contravention of sub | encoded | `s 1110G(5) the person commits an offence` |  |
| s 1110G(5)(a) | 15959 | paragraph | (a) is specified in the disclosure, or | encoded | `s 1110G(5) the person commits an offence` |  |
| s 1110G(5)(b) | 15960 | paragraph | (b) can be deduced from it. | encoded | `s 1110G(5) the person commits an offence` |  |
| s 1110G(6) | 15961 | subsection | (6) It is a defence for a person charged with an offence under subsect | encoded | `s 1110G(6) this section gives a defence` |  |
| s 1110G(6)(a) | 15962 | paragraph | (a) that the disclosure was lawful, or | encoded | `s 1110G(6) this section gives a defence` |  |
| s 1110G(6)(b) | 15963 | paragraph | (b) that the information had already lawfully been made available to t | encoded | `s 1110G(6) this section gives a defence` |  |
| s 1110G(7) | 15964 | subsection | (7) Subsections (4) to (7) of section 19 of the Commissioners for Reve | encoded | `s 1110G(7) subsections (4) to (7) of section 19 of the Commissioners for Revenue and Customs Act 2005 apply to the offence` |  |
| s 1110G(8) | 15965-15969 | subsection | (8) In this section— “the data protection legislation” has the same me | encoded | `s 1110G(8) the information is HMRC information`; `s 1110G(8) the body is HMRC` |  |
| def:s 1110G(8):the data protection legislation | 15966 | defined term | “the data protection legislation” has the same meaning as in the Data  | encoded | `s 1110G(8) the provision that gives the meaning of "the data protection legislation"` |  |
| def:s 1110G(8):HMRC | 15967 | defined term | “HMRC” means the Commissioners for His Majesty’s Revenue and Customs; | encoded | `s 1110G(8) the body is HMRC` |  |
| def:s 1110G(8):HMRC information | 15968 | defined term | “HMRC information” means information disclosed to the registrar under  | encoded | `s 1110G(8) the information is HMRC information` |  |
| def:s 1110G(8):revenue and customs information relating to a person | 15969 | defined term | “revenue and customs information relating to a person” has the meaning | encoded | `s 1110G(8) the provision that gives the meaning of "revenue and customs information relating to a person"` |  |
| heading:15970 | 15970 | cross-heading | Supplementary provisions | inert (1) | - | heading: not operative |
| s 1111 (heading) | 15971 | section heading | 1111 Registrar's requirements as to certification or verification | inert (1) | - | heading: not operative |
| s 1111(1) | 15972 | subsection | (1) Where a document required or authorised to be delivered to the reg | encoded | `s 1111(1) the registrar may impose requirements as to the person by whom the certificate or verification is to be given` |  |
| s 1111(1)(a) | 15973 | paragraph | (a) to be certified as an accurate translation or transliteration, or | encoded | `s 1111(1) the registrar may impose requirements as to the person by whom the certificate or verification is to be given` |  |
| s 1111(1)(b) | 15974 | paragraph | (b) to be certified as a correct copy or verified, | encoded | `s 1111(1) the registrar may impose requirements as to the person by whom the certificate or verification is to be given` |  |
| s 1111(1) closing words | 15975 | closing words | the registrar may impose requirements as to the person, or description | encoded | `s 1111(1) the registrar may impose requirements as to the person by whom the certificate or verification is to be given` |  |
| s 1111(2) | 15976 | subsection | (2) The power conferred by section 1068 (registrar's requirements as t | encoded | `s 1111(2) the power conferred by section 1068 is exercisable in relation to the certificate or verification as if it were a separate document` |  |
| s 1111(3) | 15977 | subsection | (3) Requirements imposed under this section must not be inconsistent w | encoded | `s 1111(3) the registrar may impose the requirement` |  |
| s 1112 (heading) | 15978 | section heading | 1112 False statements: basic offence | inert (1) | - | heading: not operative |
| s 1112(1) | 15979 | subsection | (1) It is an offence for a person, without reasonable excuse, to— | encoded | `s 1112(1) the person commits the offence` | "without reasonable excuse" limits the offence: marginal reading (b) |
| s 1112(1)(a) | 15980 | paragraph | (a) deliver or cause to be delivered to the registrar, for any purpose | encoded | `s 1112(1) the person commits the offence` | "without reasonable excuse" limits the offence: marginal reading (b) |
| s 1112(1)(b) | 15981 | paragraph | (b) make to the registrar, for any purpose of the Companies Acts, a st | encoded | `s 1112(1) the person commits the offence` | "without reasonable excuse" limits the offence: marginal reading (b) |
| s 1112(2) | 15982 | subsection | (2) Where the offence is committed by a firm, every officer of the fir | encoded | `s 1112(2) the officer of the firm who is in default also commits the offence` |  |
| s 1112(3) | 15983 | subsection | (3) A person guilty of an offence under this section is liable— | encoded | `s 1112(3) the punishment on summary conviction` |  |
| s 1112(3)(a) | 15984 | paragraph | (a) on summary conviction in England and Wales, to a fine; | encoded | `s 1112(3) the punishment on summary conviction` |  |
| s 1112(3)(b) | 15985 | paragraph | (b) on summary conviction in Scotland, to a fine not exceeding level 5 | encoded | `s 1112(3) the punishment on summary conviction` |  |
| s 1112(3)(c) | 15986 | paragraph | (c) on summary conviction in Northern Ireland, to a fine not exceeding | encoded | `s 1112(3) the punishment on summary conviction` |  |
| s 1112A (heading) | 15987 | section heading | 1112A False statements: aggravated offence | inert (1) | - | heading: not operative |
| s 1112A(1) | 15988 | subsection | (1) It is an offence for a person knowingly to— | encoded | `s 1112A(1) the person commits the offence` |  |
| s 1112A(1)(a) | 15989 | paragraph | (a) deliver or cause to be delivered to the registrar, for any purpose | encoded | `s 1112A(1) the person commits the offence` |  |
| s 1112A(1)(b) | 15990 | paragraph | (b) make to the registrar, for any purpose of the Companies Acts, a st | encoded | `s 1112A(1) the person commits the offence` |  |
| s 1112A(2) | 15991 | subsection | (2) Where the offence is committed by a firm, every officer of the fir | encoded | `s 1112A(2) the officer of the firm who is in default also commits the offence` |  |
| s 1112A(3) | 15992 | subsection | (3) A person guilty of an offence under this section is liable— | encoded | `s 1112A(3) the punishment for the offence`; `s 1131(2) the term of imprisonment the provision refers to` |  |
| s 1112A(3)(a) | 15993 | paragraph | (a) on conviction on indictment, to imprisonment for a term not exceed | encoded | `s 1112A(3) the punishment for the offence`; `s 1131(2) the term of imprisonment the provision refers to` |  |
| s 1112A(3)(b) | 15994 | paragraph | (b) on summary conviction— | encoded | `s 1112A(3) the punishment for the offence`; `s 1131(2) the term of imprisonment the provision refers to` |  |
| s 1112A(3)(b)(i) | 15995 | sub-paragraph | (i) in England and Wales, to imprisonment for a term not exceeding the | encoded | `s 1112A(3) the punishment for the offence`; `s 1131(2) the term of imprisonment the provision refers to` |  |
| s 1112A(3)(b)(ii) | 15996 | sub-paragraph | (ii) in Scotland, to imprisonment for a term not exceeding 12 months o | encoded | `s 1112A(3) the punishment for the offence`; `s 1131(2) the term of imprisonment the provision refers to` |  |
| s 1112A(3)(b)(iii) | 15997 | sub-paragraph | (iii) in Northern Ireland, to imprisonment for a term not exceeding 6  | encoded | `s 1112A(3) the punishment for the offence`; `s 1131(2) the term of imprisonment the provision refers to` |  |
| s 1112B (heading) | 15998 | section heading | 1112B False statements offences: national security etc defence | inert (1) | - | heading: not operative |
| s 1112B(1) | 15999 | subsection | (1) A person to whom a certificate is issued by the Secretary of State | encoded | `s 1112B(1) the person is liable for the commission of the offence` |  |
| s 1112B(2) | 16000 | subsection | (2) The Secretary of State may issue a certificate to a person for the | encoded | `s 1112B(2) the Secretary of State may issue the certificate` |  |
| s 1112B(2)(a) | 16001 | paragraph | (a) in the interests of national security, or | encoded | `s 1112B(2) the Secretary of State may issue the certificate` |  |
| s 1112B(2)(b) | 16002 | paragraph | (b) for the purposes of preventing or detecting serious crime. | encoded | `s 1112B(2) the Secretary of State may issue the certificate` |  |
| s 1112B(3) | 16003 | subsection | (3) A certificate under this section may be revoked by the Secretary o | encoded | `s 1112B(3) the Secretary of State may revoke the certificate` |  |
| s 1112B(4) | 16004 | subsection | (4) For the purposes of subsection (2)(b)— | encoded | `s 1112B(4)(a) the conduct is crime`; `s 1112B(4)(b) the crime is serious` |  |
| s 1112B(4)(a) | 16005 | paragraph | (a) “crime” means conduct which— | encoded | `s 1112B(4)(a) the conduct is crime`; `s 1112B(4)(b) the crime is serious` |  |
| def:s 1112B(4)(a):crime | 16005 | defined term | (a) “crime” means conduct which— | encoded | `s 1112B(4)(a) the conduct is crime` |  |
| s 1112B(4)(a)(i) | 16006 | sub-paragraph | (i) constitutes a criminal offence, or | encoded | `s 1112B(4)(a) the conduct is crime`; `s 1112B(4)(b) the crime is serious` |  |
| s 1112B(4)(a)(ii) | 16007 | sub-paragraph | (ii) is, or corresponds to, any conduct which, if it all took place in | encoded | `s 1112B(4)(a) the conduct is crime`; `s 1112B(4)(b) the crime is serious` |  |
| s 1112B(4)(b) | 16008 | paragraph | (b) crime is “serious” if— | encoded | `s 1112B(4)(a) the conduct is crime`; `s 1112B(4)(b) the crime is serious` |  |
| def:s 1112B(4)(b):serious | 16008 | defined term | (b) crime is “serious” if— | encoded | `s 1112B(4)(b) the crime is serious` |  |
| s 1112B(4)(b)(i) | 16009 | sub-paragraph | (i) the offence which is or would be constituted by the conduct is an  | encoded | `s 1112B(4)(a) the conduct is crime`; `s 1112B(4)(b) the crime is serious` |  |
| s 1112B(4)(b)(ii) | 16010 | sub-paragraph | (ii) the conduct involves the use of violence, results in substantial  | encoded | `s 1112B(4)(a) the conduct is crime`; `s 1112B(4)(b) the crime is serious` |  |
| s 1113 (heading) | 16011 | section heading | 1113 Enforcement of company's filing obligations | inert (1) | - | heading: not operative |
| s 1113(1) | 16012 | subsection | (1) This section applies where a company has made default in complying | encoded | `s 1113(1) the section applies` |  |
| s 1113(1)(a) | 16013 | paragraph | (a) to deliver a document to the registrar, or | encoded | `s 1113(1) the section applies` |  |
| s 1113(1)(b) | 16014 | paragraph | (b) to give notice to the registrar of any matter. | encoded | `s 1113(1) the section applies` |  |
| s 1113(2) | 16015 | subsection | (2) The registrar, or any member or creditor of the company, may give  | encoded | `s 1113(2) the person may give notice to the company requiring it to comply with the obligation` |  |
| s 1113(3) | 16016 | subsection | (3) If the company fails to make good the default within 14 days after | fork | `s 1113(3) the last day for the company to make good the default`; `s 1113(3) the person may apply to the court for an order`; `s 1113(3) the company's duty to make good the default` | fork F20: the may-apply function: a failed "if" gate answers NOTHING (name-test sweep) |
| s 1113(4) | 16017 | subsection | (4) The court's order may provide that all costs (in Scotland, expense | encoded | `s 1113(4) the court's order may provide that costs are borne by the company or by officers of it responsible for the default` |  |
| s 1113(5) | 16018 | subsection | (5) This section does not affect the operation of any enactment making | encoded | `s 1113(5) section 1113 affects the operation of the enactment` |  |
| s 1114 (heading) | 16019 | section heading | 1114 Application of provisions about documents and delivery | inert (1) | - | heading: not operative |
| s 1114(1) | 16020 | subsection | (1) In this Part— | encoded | `s 1114(1)(a) the thing is a document in Part 35`; `s 1114(1)(b) the act is delivering a document` |  |
| s 1114(1)(a) | 16021 | paragraph | (a) “document” means information recorded in any form, and | encoded | `s 1114(1)(a) the thing is a document in Part 35`; `s 1114(1)(b) the act is delivering a document` |  |
| def:s 1114(1)(a):document | 16021 | defined term | (a) “document” means information recorded in any form, and | encoded | `s 1114(1)(a) the thing is a document in Part 35` |  |
| s 1114(1)(b) | 16022 | paragraph | (b) references to delivering a document include forwarding, lodging, r | encoded | `s 1114(1)(a) the thing is a document in Part 35`; `s 1114(1)(b) the act is delivering a document` |  |
| def:s 1114(1)(b):delivering a document | 16022 | defined term | (b) references to delivering a document include forwarding, lodging, r | encoded | `s 1114(1)(b) the act is delivering a document` |  |
| s 1114(2) | 16023 | subsection | (2) Except as otherwise provided, this Part applies in relation to the | encoded | `s 1114(2) Part 35 applies to the supply of the information as it applies to the delivery of a document` |  |
| s 1115 (heading) | 16024 | section heading | 1115 Supplementary provisions relating to electronic communications | inert (1) | - | heading: not operative |
| s 1115(1) | 16025 | subsection | (1) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | repealed or blank in this text | - | the text shows a row of dots where the provision stood (omitted or repealed) |
| s 1115(2) | 16026 | subsection | (2) A document that is required to be signed by the registrar or authe | encoded | `s 1115(2) the document must be authenticated in the manner specified by registrar's rules` |  |
| s 1116 (heading) | 16027 | section heading | 1116 Alternative to publication in the Gazette | inert (1) | - | heading: not operative |
| s 1116(1) | 16028 | subsection | (1) Notices that would otherwise need to be published by the registrar | encoded | `s 1116(1) the notice may instead be published by the approved means` |  |
| s 1116(2) | 16029 | subsection | (2) The Secretary of State may make provision by regulations as to wha | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (what alternative means may be approved) |
| s 1116(3) | 16030 | subsection | (3) The regulations may, in particular— | inert (2) | - | machinery (reason 2): what the regulations may require |
| s 1116(3)(a) | 16031 | paragraph | (a) require the use of electronic means; | inert (2) | - | machinery (reason 2): what the regulations may require |
| s 1116(3)(b) | 16032 | paragraph | (b) require the same means to be used— | inert (2) | - | machinery (reason 2): what the regulations may require |
| s 1116(3)(b)(i) | 16033 | sub-paragraph | (i) for all notices or for all notices of specified descriptions, and | inert (2) | - | machinery (reason 2): what the regulations may require |
| s 1116(3)(b)(ii) | 16034 | sub-paragraph | (ii) whether the company (or other body) to which the notice relates i | inert (2) | - | machinery (reason 2): what the regulations may require |
| s 1116(3)(c) | 16035 | paragraph | (c) impose conditions as to the manner in which access to the notices  | inert (2) | - | machinery (reason 2): what the regulations may require |
| s 1116(4) | 16036 | subsection | (4) Regulations under this section are subject to negative resolution  | inert (2) | - | machinery (reason 2): regulations are subject to the negative resolution procedure |
| s 1116(5) | 16037 | subsection | (5) Before starting to publish notices by means approved under this se | encoded | `s 1116(5) the registrar meets the requirement of s 1116(5)` | bare "must": fork line F10 |
| s 1116(6) | 16038-16039 | subsection | (6) Nothing in this section prevents the registrar from giving public  | encoded | `s 1116(6) this section prevents the registrar from giving public notice both in the Gazette and by approved means`; `s 1116(6) the day on which the requirement of public notice is met` |  |
| s 1117 (heading) | 16040 | section heading | 1117 Registrar's rules | inert (1) | - | heading: not operative |
| s 1117(1) | 16041-16042 | subsection | (1) Where any provision of this Part enables the registrar to make pro | inert (2) | - | machinery (reason 2): rule-making power of the registrar (registrar's rules) |
| s 1117(2) | 16043 | subsection | (2) Registrar's rules— | inert (2) | - | machinery (reason 2): what the registrar's rules may provide |
| s 1117(2)(a) | 16044 | paragraph | (a) may make different provision for different cases, and | inert (2) | - | machinery (reason 2): what the registrar's rules may provide |
| s 1117(2)(b) | 16045 | paragraph | (b) may allow the registrar to disapply or modify any of the rules. | inert (2) | - | machinery (reason 2): what the registrar's rules may provide |
| s 1117(3) | 16046 | subsection | (3) The registrar must— | encoded | `s 1117(3)(a) the registrar meets the requirement to publicise the rules`; `s 1117(3)(b) the registrar must make copies of the rules available to the public in the form` |  |
| s 1117(3)(a) | 16047 | paragraph | (a) publicise the rules in a manner appropriate to bring them to the n | encoded | `s 1117(3)(a) the registrar meets the requirement to publicise the rules`; `s 1117(3)(b) the registrar must make copies of the rules available to the public in the form` |  |
| s 1117(3)(b) | 16048 | paragraph | (b) make copies of the rules available to the public (in hard copy or  | encoded | `s 1117(3)(a) the registrar meets the requirement to publicise the rules`; `s 1117(3)(b) the registrar must make copies of the rules available to the public in the form` |  |
| s 1118 (heading) | 16049 | section heading | 1118 Payments into the Consolidated Fund | inert (1) | - | heading: not operative |
| s 1118 | 16050 | section text | Nothing in the Companies Acts or any other enactment as to the payment | encoded | `s 1118 the provision affects the operation in relation to the registrar of section 3(1) of the Government Trading Funds Act 1973` |  |
| s 1119 (heading) | 16051 | section heading | 1119 Contracting out of registrar's functions | inert (1) | - | heading: not operative |
| s 1119(1) | 16052-16053 | subsection | (1) Where by virtue of an order made under section 69 of the Deregulat | encoded | `s 1119(1) the registrar may direct that documents of the class be delivered to a specified address of the authorised person`; `s 1119(1) the direction meets the requirement of s 1119(1)` |  |
| s 1119(2) | 16054 | subsection | (2) A document of that class that is delivered to an address other tha | encoded | `s 1119(2) the document is treated as delivered` |  |
| s 1119(3) | 16055 | subsection | (3) Registrar's rules are not subordinate legislation for the purposes | encoded | `s 1119(3) the provision is subordinate legislation for the purposes of section 71 of the Deregulation and Contracting Out Act 1994` |  |
| s 1120 (heading) | 16056 | section heading | 1120 Application of this Part to overseas companies | inert (1) | - | heading: not operative |
| s 1120 (blank text) | 16057 | blank text | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | repealed or blank in this text | - | the text shows a row of dots where the provision stood (omitted or repealed) |
| heading:16058 | 16058 | cross-heading | Part 36 — Offences under the Companies Acts and financial penalties | inert (1) | - | heading: not operative |
| heading:16059 | 16059 | cross-heading | Liability of officer in default | inert (1) | - | heading: not operative |
| s 1121 (heading) | 16060 | section heading | 1121 Liability of officer in default | inert (1) | - | heading: not operative |
| s 1121(1) | 16061 | subsection | (1) This section has effect for the purposes of any provision of the C | encoded | `s 1121(1) the section has effect for the provision` |  |
| s 1121(2) | 16062 | subsection | (2) For this purpose “officer” includes— | encoded | `s 1121(2) the person is an officer of the company`; `s 1121 the person is an officer in default` |  |
| def:s 1121(2):officer | 16062 | defined term | (2) For this purpose “officer” includes— | encoded | `s 1121(2) the person is an officer of the company` |  |
| s 1121(2)(a) | 16063 | paragraph | (a) any director, manager or secretary, and | encoded | `s 1121(2) the person is an officer of the company`; `s 1121 the person is an officer in default` |  |
| s 1121(2)(b) | 16064 | paragraph | (b) any person who is to be treated as an officer of the company for t | encoded | `s 1121(2) the person is an officer of the company`; `s 1121 the person is an officer in default` |  |
| s 1121(3) | 16065 | subsection | (3) An officer is “in default” for the purposes of the provision if he | encoded | `s 1121(3) the officer is in default`; `s 1121 the person is an officer in default` | "if" definition: marginal reading (a) |
| def:s 1121(3):in default | 16065 | defined term | (3) An officer is “in default” for the purposes of the provision if he | encoded | `s 1121(3) the officer is in default` |  |
| s 1122 (heading) | 16066 | section heading | 1122 Liability of company as officer in default | inert (1) | - | heading: not operative |
| s 1122(1) | 16067 | subsection | (1) Where a company is an officer of another company, it does not comm | fork | `s 1122(1) the company commits an offence as an officer in default` | fork F3: the "unless" once met |
| s 1122(2) | 16068 | subsection | (2) Where any such offence is committed by a company the officer in qu | encoded | `s 1122(2) the officer in question also commits the offence` |  |
| s 1122(3) | 16069 | subsection | (3) In this section “officer” and “in default” have the meanings given | encoded | `s 1122(3) the section that gives the meaning of the term` |  |
| s 1123 (heading) | 16070 | section heading | 1123 Application to bodies other than companies | inert (1) | - | heading: not operative |
| s 1123(1) | 16071 | subsection | (1) Section 1121 (liability of officers in default) applies to a body  | encoded | `s 1123(1) section 1121 applies to the body` |  |
| s 1123(2) | 16072 | subsection | (2) As it applies in relation to a body corporate other than a company | encoded | `s 1123 the person is read as a director for the purposes of section 1121(2)(a)`; `s 1123 the person is read as a manager or secretary for the purposes of section 1121(2)(a)` |  |
| s 1123(2)(a) | 16073 | paragraph | (a) the reference to a director of the company shall be read as referr | encoded | `s 1123 the person is read as a director for the purposes of section 1121(2)(a)`; `s 1123 the person is read as a manager or secretary for the purposes of section 1121(2)(a)` |  |
| s 1123(2)(a)(i) | 16074 | sub-paragraph | (i) where the body's affairs are managed by its members, to a member o | encoded | `s 1123 the person is read as a director for the purposes of section 1121(2)(a)`; `s 1123 the person is read as a manager or secretary for the purposes of section 1121(2)(a)` |  |
| s 1123(2)(a)(ii) | 16075 | sub-paragraph | (ii) in any other case, to any corresponding officer of the body, and | encoded | `s 1123 the person is read as a director for the purposes of section 1121(2)(a)`; `s 1123 the person is read as a manager or secretary for the purposes of section 1121(2)(a)` |  |
| s 1123(2)(b) | 16076 | paragraph | (b) the reference to a manager or secretary of the company shall be re | encoded | `s 1123 the person is read as a director for the purposes of section 1121(2)(a)`; `s 1123 the person is read as a manager or secretary for the purposes of section 1121(2)(a)` |  |
| s 1123(3) | 16077 | subsection | (3) As it applies in relation to a partnership— | encoded | `s 1123 the person is read as a director for the purposes of section 1121(2)(a)`; `s 1123 the person is read as a manager or secretary for the purposes of section 1121(2)(a)` |  |
| s 1123(3)(a) | 16078 | paragraph | (a) the reference to a director of the company shall be read as referr | encoded | `s 1123 the person is read as a director for the purposes of section 1121(2)(a)`; `s 1123 the person is read as a manager or secretary for the purposes of section 1121(2)(a)` |  |
| s 1123(3)(b) | 16079 | paragraph | (b) the reference to a manager or secretary of the company shall be re | encoded | `s 1123 the person is read as a director for the purposes of section 1121(2)(a)`; `s 1123 the person is read as a manager or secretary for the purposes of section 1121(2)(a)` |  |
| s 1123(4) | 16080 | subsection | (4) As it applies in relation to an unincorporated body other than a p | encoded | `s 1123 the person is read as a director for the purposes of section 1121(2)(a)`; `s 1123 the person is read as a manager or secretary for the purposes of section 1121(2)(a)` |  |
| s 1123(4)(a) | 16081 | paragraph | (a) the reference to a director of the company shall be read as referr | encoded | `s 1123 the person is read as a director for the purposes of section 1121(2)(a)`; `s 1123 the person is read as a manager or secretary for the purposes of section 1121(2)(a)` |  |
| s 1123(4)(a)(i) | 16082 | sub-paragraph | (i) where the body's affairs are managed by its members, to a member o | encoded | `s 1123 the person is read as a director for the purposes of section 1121(2)(a)`; `s 1123 the person is read as a manager or secretary for the purposes of section 1121(2)(a)` |  |
| s 1123(4)(a)(ii) | 16083 | sub-paragraph | (ii) in any other case, to a member of the governing body, and | encoded | `s 1123 the person is read as a director for the purposes of section 1121(2)(a)`; `s 1123 the person is read as a manager or secretary for the purposes of section 1121(2)(a)` |  |
| s 1123(4)(b) | 16084 | paragraph | (b) the reference to a manager or secretary of the company shall be re | encoded | `s 1123 the person is read as a director for the purposes of section 1121(2)(a)`; `s 1123 the person is read as a manager or secretary for the purposes of section 1121(2)(a)` |  |
| heading:16085 | 16085 | cross-heading | Offences under the Companies Act 1985 | inert (1) | - | heading: not operative |
| s 1124 (heading) | 16086 | section heading | 1124 Amendments of the Companies Act 1985 | inert (1) | - | heading: not operative |
| s 1124 | 16087 | section text | Schedule 3 contains amendments of the Companies Act 1985 (c. 6) relati | inert (2) | - | machinery (reason 2): Schedule 3 amends the Companies Act 1985 (an amendment of another Act) |
| heading:16088 | 16088 | cross-heading | General provisions | inert (1) | - | heading: not operative |
| s 1125 (heading) | 16089 | section heading | 1125 Meaning of “daily default fine” | inert (1) | - | heading: not operative |
| s 1125(1) | 16090 | subsection | (1) This section defines what is meant in the Companies Acts where it  | encoded | `s 1125(1) the section defines the daily default fine for the offence provision`; `s 1125(1) the fine limit in pounds` |  |
| def:s 1125(1):daily default fine | 16090 | defined term | (1) This section defines what is meant in the Companies Acts where it  | encoded | `s 1125(1) the section defines the daily default fine for the offence provision`; `s 1125(2) the fine limit that applies on this conviction` |  |
| s 1125(2) | 16091 | subsection | (2) This means that the person is liable on a second or subsequent sum | encoded | `s 1125(2) the fine limit that applies on this conviction`; `s 1125(2) the limit applies for each day`; `s 1125(2) the most the person can be fined on this conviction, in pounds` |  |
| s 1126 (heading) | 16092 | section heading | 1126 Consents required for certain prosecutions | inert (1) | - | heading: not operative |
| s 1126(1) | 16093-16099 | subsection | (1) This section applies to proceedings for an offence under any of th | encoded | `s 1126(2)-(3) the consent required for the proceedings` |  |
| s 1126(2) | 16100 | subsection | (2) No such proceedings are to be brought in England and Wales except  | fork | `s 1126(2)-(3) the consent required for the proceedings`; `s 1126(2)-(3) the proceedings may be brought` | fork F8: the "except" once met: NOTHING taken |
| s 1126(2)(a) | 16101 | paragraph | (a) in the case of an offence under— | fork | `s 1126(2)-(3) the consent required for the proceedings`; `s 1126(2)-(3) the proceedings may be brought` | fork F8: the "except" once met: NOTHING taken |
| s 1126(2)(a)(i) | 16102 | sub-paragraph | (i) section 458, 460 or 949 of this Act, | fork | `s 1126(2)-(3) the consent required for the proceedings`; `s 1126(2)-(3) the proceedings may be brought` | fork F8: the "except" once met: NOTHING taken |
| s 1126(2)(a)(ii) | 16103 | sub-paragraph | (ii) section 953 of this Act, ... | fork | `s 1126(2)-(3) the consent required for the proceedings`; `s 1126(2)-(3) the proceedings may be brought` | fork F8: the "except" once met: NOTHING taken |
| s 1126(2)(a)(iii) | 16104 | sub-paragraph | (iii) section 448, 449, 450, 451 or 453A of the Companies Act 1985, or | fork | `s 1126(2)-(3) the consent required for the proceedings`; `s 1126(2)-(3) the proceedings may be brought` | fork F8: the "except" once met: NOTHING taken |
| s 1126(2)(a)(iv) | 16105 | sub-paragraph | (iv) section 1112 or 1112A of this Act, | fork | `s 1126(2)-(3) the consent required for the proceedings`; `s 1126(2)-(3) the proceedings may be brought` | fork F8: the "except" once met: NOTHING taken |
| s 1126(2) closing words | 16106 | closing words | the Secretary of State or the Director of Public Prosecutions; | fork | `s 1126(2)-(3) the consent required for the proceedings`; `s 1126(2)-(3) the proceedings may be brought` | fork F8: the "except" once met: NOTHING taken |
| s 1126(2)(b) | 16107 | paragraph | (b) in the case of an offence under section 798 of , or paragraph 5 or | fork | `s 1126(2)-(3) the consent required for the proceedings`; `s 1126(2)-(3) the proceedings may be brought` | fork F8: the "except" once met: NOTHING taken |
| s 1126(3) | 16108 | subsection | (3) No such proceedings are to be brought in Northern Ireland except b | fork | `s 1126(2)-(3) the consent required for the proceedings`; `s 1126(2)-(3) the proceedings may be brought` | fork F8: the "except" once met: NOTHING taken |
| s 1126(3)(a) | 16109 | paragraph | (a) in the case of an offence under— | fork | `s 1126(2)-(3) the consent required for the proceedings`; `s 1126(2)-(3) the proceedings may be brought` | fork F8: the "except" once met: NOTHING taken |
| s 1126(3)(a)(i) | 16110 | sub-paragraph | (i) section 458, 460 or 949 of this Act, | fork | `s 1126(2)-(3) the consent required for the proceedings`; `s 1126(2)-(3) the proceedings may be brought` | fork F8: the "except" once met: NOTHING taken |
| s 1126(3)(a)(ii) | 16111 | sub-paragraph | (ii) section 953 of this Act, ... | fork | `s 1126(2)-(3) the consent required for the proceedings`; `s 1126(2)-(3) the proceedings may be brought` | fork F8: the "except" once met: NOTHING taken |
| s 1126(3)(a)(iii) | 16112 | sub-paragraph | (iii) section 448, 449, 450, 451 or 453A of the Companies Act 1985, or | fork | `s 1126(2)-(3) the consent required for the proceedings`; `s 1126(2)-(3) the proceedings may be brought` | fork F8: the "except" once met: NOTHING taken |
| s 1126(3)(a)(iv) | 16113 | sub-paragraph | (iv) section 1112 or 1112A of this Act, | fork | `s 1126(2)-(3) the consent required for the proceedings`; `s 1126(2)-(3) the proceedings may be brought` | fork F8: the "except" once met: NOTHING taken |
| s 1126(3) closing words | 16114 | closing words | the Secretary of State or the Director of Public Prosecutions for Nort | fork | `s 1126(2)-(3) the consent required for the proceedings`; `s 1126(2)-(3) the proceedings may be brought` | fork F8: the "except" once met: NOTHING taken |
| s 1126(3)(b) | 16115 | paragraph | (b) in the case of an offence under section 798 of , or paragraph 5 or | fork | `s 1126(2)-(3) the consent required for the proceedings`; `s 1126(2)-(3) the proceedings may be brought` | fork F8: the "except" once met: NOTHING taken |
| s 1127 (heading) | 16116 | section heading | 1127 Summary proceedings: venue | inert (1) | - | heading: not operative |
| s 1127(1) | 16117 | subsection | (1) Summary proceedings for any offence under the Companies Acts may b | encoded | `s 1127(1) summary proceedings for the offence may be taken at the place` |  |
| s 1127(1)(a) | 16118 | paragraph | (a) against a body corporate, at any place at which the body has a pla | encoded | `s 1127(1) summary proceedings for the offence may be taken at the place` |  |
| s 1127(1)(b) | 16119 | paragraph | (b) against any other person, at any place at which he is for the time | encoded | `s 1127(1) summary proceedings for the offence may be taken at the place` |  |
| s 1127(2) | 16120 | subsection | (2) This is without prejudice to any jurisdiction exercisable apart fr | encoded | `s 1127(2) section 1127(1) prejudices the jurisdiction` |  |
| s 1128 (heading) | 16121 | section heading | 1128 Summary proceedings: time limit for proceedings | inert (1) | - | heading: not operative |
| s 1128(1) | 16122 | subsection | (1) An information relating to an offence under the Companies Acts tha | fork | `s 1128(1) the information was laid in time` | fork F6: three years and twelve months are counted with add years and add months, which clamp the day of the month |
| s 1128(1)(a) | 16123 | paragraph | (a) at any time within three years after the commission of the offence | fork | `s 1128(1) the information was laid in time` | fork F6: three years and twelve months are counted with add years and add months, which clamp the day of the month |
| s 1128(1)(b) | 16124 | paragraph | (b) within twelve months after the date on which evidence sufficient i | fork | `s 1128(1) the information was laid in time` | fork F6: three years and twelve months are counted with add years and add months, which clamp the day of the month |
| s 1128(2) | 16125 | subsection | (2) Summary proceedings in Scotland for an offence under the Companies | fork | `s 1128(2) the proceedings in Scotland were commenced in time` | fork F6: as for subsection (1) |
| s 1128(2)(a) | 16126 | paragraph | (a) must not be commenced after the expiration of three years from the | fork | `s 1128(2) the proceedings in Scotland were commenced in time` | fork F6: as for subsection (1) |
| s 1128(2)(b) | 16127 | paragraph | (b) subject to that, may be commenced at any time— | fork | `s 1128(2) the proceedings in Scotland were commenced in time` | fork F6: as for subsection (1) |
| s 1128(2)(b)(i) | 16128 | sub-paragraph | (i) within twelve months after the date on which evidence sufficient i | fork | `s 1128(2) the proceedings in Scotland were commenced in time` | fork F6: as for subsection (1) |
| s 1128(2)(b)(ii) | 16129 | sub-paragraph | (ii) where such evidence was reported to him by the Secretary of State | fork | `s 1128(2) the proceedings in Scotland were commenced in time` | fork F6: as for subsection (1) |
| s 1128(2) closing words | 16130 | closing words | Section 136(3) of the Criminal Procedure (Scotland) Act 1995 (c. 46) ( | fork | `s 1128(2) the proceedings in Scotland were commenced in time` | fork F6: as for subsection (1) |
| s 1128(3) | 16131 | subsection | (3) A magistrates' court in Northern Ireland has jurisdiction to hear  | fork | `s 1128(3) the complaint was made in time` | fork F6: as for subsection (1) |
| s 1128(3)(a) | 16132 | paragraph | (a) within three years from the time when the offence was committed, a | fork | `s 1128(3) the complaint was made in time` | fork F6: as for subsection (1) |
| s 1128(3)(b) | 16133 | paragraph | (b) within twelve months from the date on which evidence sufficient in | fork | `s 1128(3) the complaint was made in time` | fork F6: as for subsection (1) |
| s 1128(4) | 16134 | subsection | (4) For the purposes of this section a certificate of the Director of  | encoded | `s 1128(4) the date on which the evidence came to notice, as the certificate conclusively shows` |  |
| s 1129 (heading) | 16135 | section heading | 1129 Legal professional privilege | inert (1) | - | heading: not operative |
| s 1129 | 16136 | section text | In proceedings against a person for an offence under the Companies Act | encoded | `s 1129 the Companies Acts require the person to disclose the information` |  |
| s 1130 (heading) | 16137 | section heading | 1130 Proceedings against unincorporated bodies | inert (1) | - | heading: not operative |
| s 1130(1) | 16138 | subsection | (1) Proceedings for an offence under the Companies Acts alleged to hav | encoded | `s 1130(1) the proceedings meet the requirement of s 1130(1)` |  |
| s 1130(2) | 16139 | subsection | (2) For the purposes of such proceedings— | encoded | `s 1130(2) the rules of court as to service, and the listed provisions, apply as if the body were a body corporate`; `s 1130(2)(b) the provisions that apply as they apply in relation to a body corporate` |  |
| s 1130(2)(a) | 16140 | paragraph | (a) any rules of court relating to the service of documents have effec | encoded | `s 1130(2) the rules of court as to service, and the listed provisions, apply as if the body were a body corporate`; `s 1130(2)(b) the provisions that apply as they apply in relation to a body corporate` |  |
| s 1130(2)(b) | 16141 | paragraph | (b) the following provisions apply as they apply in relation to a body | encoded | `s 1130(2) the rules of court as to service, and the listed provisions, apply as if the body were a body corporate`; `s 1130(2)(b) the provisions that apply as they apply in relation to a body corporate` |  |
| s 1130(2)(b)(i) | 16142 | sub-paragraph | (i) in England and Wales, section 33 of the Criminal Justice Act 1925  | encoded | `s 1130(2) the rules of court as to service, and the listed provisions, apply as if the body were a body corporate`; `s 1130(2)(b) the provisions that apply as they apply in relation to a body corporate` |  |
| s 1130(2)(b)(ii) | 16143 | sub-paragraph | (ii) in Scotland, sections 70 and 143 of the Criminal Procedure (Scotl | encoded | `s 1130(2) the rules of court as to service, and the listed provisions, apply as if the body were a body corporate`; `s 1130(2)(b) the provisions that apply as they apply in relation to a body corporate` |  |
| s 1130(2)(b)(iii) | 16144 | sub-paragraph | (iii) in Northern Ireland, section 18 of the Criminal Justice Act (Nor | encoded | `s 1130(2) the rules of court as to service, and the listed provisions, apply as if the body were a body corporate`; `s 1130(2)(b) the provisions that apply as they apply in relation to a body corporate` |  |
| s 1130(3) | 16145 | subsection | (3) A fine imposed on an unincorporated body on its conviction of an o | encoded | `s 1130(3) the fine is paid as the subsection requires` |  |
| s 1131 (heading) | 16146 | section heading | 1131 Imprisonment on summary conviction in England and Wales: transito | inert (1) | - | heading: not operative |
| s 1131(1) | 16147 | subsection | (1) This section applies to any provision of the Companies Acts that p | encoded | `s 1131(1) the section applies to the provision` |  |
| s 1131(2) | 16148 | subsection | (2) In relation to an offence committed before 2 May 2022, for “the ge | encoded | `s 1131(2) the term of imprisonment the provision refers to` |  |
| heading:16149 | 16149 | cross-heading | Production and inspection of documents | inert (1) | - | heading: not operative |
| s 1132 (heading) | 16150 | section heading | 1132 Production and inspection of documents where offence suspected | inert (1) | - | heading: not operative |
| s 1132(1) | 16151 | subsection | (1) An application under this section may be made— | encoded | `s 1132(1) the person may apply for an order under this section`; `s 1132(1) the court to which the application is made` |  |
| s 1132(1)(a) | 16152 | paragraph | (a) in England and Wales, to a judge of the High Court by the Director | encoded | `s 1132(1) the person may apply for an order under this section`; `s 1132(1) the court to which the application is made` |  |
| s 1132(1)(b) | 16153 | paragraph | (b) in Scotland, to one of the Lords Commissioners of Justiciary by th | encoded | `s 1132(1) the person may apply for an order under this section`; `s 1132(1) the court to which the application is made` |  |
| s 1132(1)(c) | 16154 | paragraph | (c) in Northern Ireland, to the High Court by the Director of Public P | encoded | `s 1132(1) the person may apply for an order under this section`; `s 1132(1) the court to which the application is made` |  |
| s 1132(2) | 16155 | subsection | (2) If on an application under this section there is shown to be reaso | fork | `s 1132(2) an order under this section may be made` | fork F22: a failed "if" gate of a function named for a power answers NOTHING (name-test sweep) |
| s 1132(2)(a) | 16156 | paragraph | (a) that any person has, while an officer of a company, committed an o | fork | `s 1132(2) an order under this section may be made` | fork F22: a failed "if" gate of a function named for a power answers NOTHING (name-test sweep) |
| s 1132(2)(b) | 16157 | paragraph | (b) that evidence of the commission of the offence is to be found in a | fork | `s 1132(2) an order under this section may be made` | fork F22: a failed "if" gate of a function named for a power answers NOTHING (name-test sweep) |
| s 1132(2) closing words | 16158 | closing words | an order under this section may be made. | fork | `s 1132(2) an order under this section may be made` | fork F22: a failed "if" gate of a function named for a power answers NOTHING (name-test sweep) |
| s 1132(3) | 16159 | subsection | (3) The order may— | encoded | `s 1132(3)-(4) the order may contain the provision` |  |
| s 1132(3)(a) | 16160 | paragraph | (a) authorise any person named in it to inspect the documents in quest | encoded | `s 1132(3)-(4) the order may contain the provision` |  |
| s 1132(3)(b) | 16161 | paragraph | (b) require the secretary of the company, or such other officer of it  | encoded | `s 1132(3)-(4) the order may contain the provision` |  |
| s 1132(4) | 16162 | subsection | (4) This section applies also in relation to documents in the possessi | encoded | `s 1132(3)-(4) the order may contain the provision` |  |
| s 1132(5) | 16163 | subsection | (5) The decision under this section of a judge of the High Court, any  | encoded | `s 1132(5) the decision may be appealed` |  |
| s 1132(6) | 16164 | subsection | (6) In this section “document” includes information recorded in any fo | encoded | `s 1132(6) the thing is a document` |  |
| def:s 1132(6):document | 16164 | defined term | (6) In this section “document” includes information recorded in any fo | encoded | `s 1132(6) the thing is a document` |  |
| heading:16165 | 16165 | cross-heading | Financial penalties | inert (1) | - | heading: not operative |
| s 1132A (heading) | 16166 | section heading | 1132A Power to make provision for financial penalties | inert (1) | - | heading: not operative |
| s 1132A(1) | 16167 | subsection | (1) The Secretary of State may by regulations make provision conferrin | inert (2) | - | machinery (reason 2): power or duty of the Secretary of State to make regulations (financial penalties imposed by the registrar) |
| s 1132A(2) | 16168 | subsection | (2) “Relevant offence under this Act” means any offence under this Act | encoded | `s 1132A(2) the offence is a relevant offence under this Act` |  |
| def:s 1132A(2):Relevant offence under this Act | 16168 | defined term | (2) “Relevant offence under this Act” means any offence under this Act | encoded | `s 1132A(2) the offence is a relevant offence under this Act` |  |
| s 1132A(2)(a) | 16169 | paragraph | (a) Part 12 (company secretaries); | encoded | `s 1132A(2) the offence is a relevant offence under this Act` |  |
| s 1132A(2)(b) | 16170 | paragraph | (b) Part 13 (resolutions and meetings); | encoded | `s 1132A(2) the offence is a relevant offence under this Act` |  |
| s 1132A(2)(c) | 16171 | paragraph | (c) Part 16 (audit). | encoded | `s 1132A(2) the offence is a relevant offence under this Act` |  |
| s 1132A(3) | 16172 | subsection | (3) The regulations may include provision— | inert (2) | - | machinery (reason 2): what the regulations may include (procedure, amount, interest, appeals, enforcement) |
| s 1132A(3)(a) | 16173 | paragraph | (a) about the procedure to be followed in imposing penalties; | inert (2) | - | machinery (reason 2): what the regulations may include (procedure, amount, interest, appeals, enforcement) |
| s 1132A(3)(b) | 16174 | paragraph | (b) about the amount of penalties; | inert (2) | - | machinery (reason 2): what the regulations may include (procedure, amount, interest, appeals, enforcement) |
| s 1132A(3)(c) | 16175 | paragraph | (c) for the imposition of interest or additional penalties for late pa | inert (2) | - | machinery (reason 2): what the regulations may include (procedure, amount, interest, appeals, enforcement) |
| s 1132A(3)(d) | 16176 | paragraph | (d) conferring rights of appeal against penalties; | inert (2) | - | machinery (reason 2): what the regulations may include (procedure, amount, interest, appeals, enforcement) |
| s 1132A(3)(e) | 16177 | paragraph | (e) about the enforcement of penalties. | inert (2) | - | machinery (reason 2): what the regulations may include (procedure, amount, interest, appeals, enforcement) |
| s 1132A(4) | 16178 | subsection | (4) Provision made under subsection (3)(b) must ensure that the maximu | encoded | `s 1132A(4) the regulations may provide for this maximum financial penalty` |  |
| s 1132A(5) | 16179 | subsection | (5) The regulations must provide that— | encoded | `s 1132A(5)(a) the regulations must provide that no financial penalty may be imposed on the person`; `s 1132A(5)(b) the regulations must provide that no proceedings may be brought against the person` |  |
| s 1132A(5)(a) | 16180 | paragraph | (a) no financial penalty may be imposed under the regulations on a per | encoded | `s 1132A(5)(a) the regulations must provide that no financial penalty may be imposed on the person`; `s 1132A(5)(b) the regulations must provide that no proceedings may be brought against the person` |  |
| s 1132A(5)(a)(i) | 16181 | sub-paragraph | (i) proceedings have been brought against the person for that offence  | encoded | `s 1132A(5)(a) the regulations must provide that no financial penalty may be imposed on the person`; `s 1132A(5)(b) the regulations must provide that no proceedings may be brought against the person` |  |
| s 1132A(5)(a)(ii) | 16182 | sub-paragraph | (ii) the person has been convicted of that offence in respect of that  | encoded | `s 1132A(5)(a) the regulations must provide that no financial penalty may be imposed on the person`; `s 1132A(5)(b) the regulations must provide that no proceedings may be brought against the person` |  |
| s 1132A(5)(b) | 16183 | paragraph | (b) no proceedings may be brought against a person in respect of condu | encoded | `s 1132A(5)(a) the regulations must provide that no financial penalty may be imposed on the person`; `s 1132A(5)(b) the regulations must provide that no proceedings may be brought against the person` |  |
| s 1132A(6) | 16184 | subsection | (6) Amounts recovered by the registrar under the regulations are to be | inert (2) | - | machinery (reason 2): amounts recovered are paid into the Consolidated Fund |
| s 1132A(7) | 16185 | subsection | (7) Regulations under this section are subject to affirmative resoluti | inert (2) | - | machinery (reason 2): regulations are subject to the affirmative resolution procedure |
| s 1132A(8) | 16186 | subsection | (8) In this section “conduct” means an act or omission. | encoded | `s 1132A(8) the thing is conduct` |  |
| def:s 1132A(8):conduct | 16186 | defined term | (8) In this section “conduct” means an act or omission. | encoded | `s 1132A(8) the thing is conduct` |  |
| heading:16187 | 16187 | cross-heading | Supplementary | inert (1) | - | heading: not operative |
| s 1133 (heading) | 16188 | section heading | 1133 Transitional provision | inert (1) | - | heading: not operative |
| s 1133 | 16189 | section text | The provisions of this Part except section 1132 do not apply to offenc | encoded | `s 1133 the provision of Part 36 applies to the offence` |  |

## Fork register (coa24)

Where a row says "taken", the other reading is the one a reviewer may prefer; each is a one-line change at the function named. The text quoted is the text that licenses the reading.

| id | provision | function | readings | taken | text that licenses each |
| --- | --- | --- | --- | --- | --- |
| F1 | s 1093(4), the daily default fine | `s 1093(4) the punishment for the offence under subsection (3)` | (A) daily default fine not exceeding one-tenth of level 5; (B) not exceeding one-tenth of the greater of £5,000 or level 4; (C) the text does not say which | Both encoded, chosen by an input; the third value answers NOTHING, and the seat asks the person to choose or to leave it open | "a daily default fine not exceeding one-tenth of level 5 on the standard scaleone-tenth of the greater of £5,000 or level 4 on the standard scale": the rendering runs two versions together with no separator (finding 1) |
| F2 | s 1099(3), two paragraphs lettered (f) | `s 1099(2)-(3) the section applies to the body` | the text has two (f)s; both bodies are in the list | Both encoded as separate constructors (`first paragraph (f)` and `second paragraph (f)`); no outcome differs | "(f) protected cell companies registered under Part 4 of the Risk Transformation Regulations 2017." and "(f) charitable incorporated organisations within the meaning of Part 11 of the Charities Act 2011;" |
| F3 | ss 1094(3), 1122(1), 1097(5): a bare bar ("may exercise the power ... only if", "does not commit ... unless", "shall not ... unless") once the condition is met; s 1096(3) is the exception and answers JUST TRUE once met. The discriminator: s 1094(3) only restricts the exercise of a power that s 1094(1) confers, so once its bar is met the grant lies in another sentence; s 1096(3) is the one sentence in this range that gives the court the power ("The court may make an order") for legally consequential material, since s 1096(1) speaks of what the registrar must do on a direction the court has already given. A reviewer who treats the two alike changes one branch of `s 1096(3)` and its test | `s 1094(3)`, `s 1122(1)`, `s 1097(5)` (and `s 1096(3)`) | (i) the bar lifts and the text says no more: NOTHING; (ii) the bar lifts and the thing is allowed or done: JUST TRUE | (i): the grant or the offence is in another provision (ss 1094(1), 1096(1) and (4), 1121, 1097(1)-(4)); the composites `s 1094(1) and (3)` and `s 1097(1)-(5)` combine them and answer JUST TRUE | "only if satisfied that the interest of the company", "does not commit an offence as an officer in default unless one of its officers is in default", "shall not give any direction under this section unless it is satisfied" |
| F4 | s 1097(5)(a), limbs (i) and (ii) | `s 1097(5) the court may give a direction` | (i) damage from the note belongs to the note directions of (2) and (4), damage from inspection of the order to the direction of (3); (ii) either limb suffices for every direction | (ii): the text says only "(i) ... or (ii) ... may cause damage to the company" | "(a) that— (i) the presence on the register of the note or, as the case may be, of an unrestricted note, or (ii) the availability for public inspection of the court's order, may cause damage to the company" |
| F5 | s 1098E(2), "until" | `s 1098E(2) the change cannot yet be treated as having occurred` | (i) on the day the authority notifies or publishes, the change is treated as having occurred; (ii) only from the next day | (i): "until" read as "before that day"; JUST TRUE before the day, JUST FALSE on and after it; no date yet is JUST TRUE | "the change is not to be treated as having occurred until the authority that has agreed to act notifies the person or publishes the agreement under regulation 7(3)" (ruling of 2026-11-05 (d): encode the bar) |
| F6 | s 1128(1)-(3), "three years after", "twelve months after" | `s 1128(1)`, `(2)`, `(3)` | on 29 February and on a month-end date, the last day is (i) the clamped date (`add years` of 29 February 2024 by 3 is 28 February 2027) or (ii) the first day of the next month | (i): daydate's `add years` and `add months` clamp the day of the month; tests assert both sides of 28 February 2027 and 28 February 2025 | "within three years after the commission of the offence", "within twelve months after the date on which evidence" |
| F7 | s 1098F(1), "if" with other routes | `s 1098F(1) the person ceases to be an authorised corporate service provider` | (i) NOTHING when the person has not ceased to be a relevant person; (ii) JUST FALSE ("if" read as "only if") | (i): subsection (2)(a) lets regulations provide "other circumstances in which a person ceases to be an authorised corporate service provider" | "A person ceases to be an authorised corporate service provider if the person ceases to be a relevant person" |
| F8 | s 1126(2)-(3), "except by or with the consent of" | `s 1126(2)-(3) the proceedings may be brought` | with the named consent: (i) NOTHING, the section bars proceedings without it and does not itself allow them; (ii) JUST TRUE | (i); without the named consent JUST FALSE | "No such proceedings are to be brought in England and Wales except by or with the consent of" |
| F9 | s 1092C(2), "other than" | `s 1092C(2) subsection (1) applies to the offence`, `s 1092C(1) the statement may not be used against the person in the criminal proceedings` | for a listed offence: (i) subsection (1) applies is JUST FALSE, and "may not be used" is NOTHING (the text does not say the statement may be used); (ii) both JUST FALSE | (i) | "Subsection (1) applies to any offence other than—" |
| F10 | every bare "must" that is not done (the six open questions of 2026-11-05, "a bare 'must' not done") | the functions named "... meets the requirement of s N": `s 1093(2)`, `s 1096(2)`, `s 1096(5)`, `s 1098(1)`, `s 1098(2)`, `s 1098B(2)`, `s 1098D`, `s 1104(2)`, `s 1105(1)`, `s 1108(1)`, `s 1110A(3)`, `s 1116(5)`, `s 1117(3)(a)`, `s 1119(1)`, `s 1130(1)` | (i) JUST FALSE: the requirement is not met; (ii) NOTHING: the text does not say what follows | (i), because each function is named for the requirement ("meets the requirement of s N") and claims nothing about what follows; the consequence of a breach is not encoded unless the text states one | e.g. "The notice must state the date on which it is issued"; "The court order must specify what is to be removed from the register and indicate where on the register it is" |
| F11 | s 1093(3)(a), "if ... not delivered within the period" before the period ends | `s 1093(3)(a) the company commits an offence` | before the last day, with nothing yet done: (i) JUST FALSE (no failure yet); (ii) NOTHING (cannot say yet) | (i), by the ruling of 2026-11-05 (a): inside the period the answer is no; this is an offence, not a grant, so the name test of F19 to F22 does not touch it | "If the necessary documents are not delivered within the period specified, an offence is committed" |
| F12 | s 1103: "subject to" ss 1104 and 1105 | `s 1103 the document must be drawn up and delivered in English` | when neither exception is made out (including when ss 1104(1) and 1105(1) answer NOTHING because the company is not Welsh and the document is not on the s 1105(2) list): (i) JUST TRUE, the general rule stands; (ii) NOTHING | (i) | "The general rule is that all documents required to be delivered to the registrar must be drawn up and delivered in English." |
| F13 | s 1123, "in any other case" | `s 1123 the person is read as a director for the purposes of section 1121(2)(a)` | a role other than the one the substitution names: (i) NOTHING; (ii) JUST FALSE | (i): s 1121(2) says "officer" "includes" and the list is not closed | "(i) where the body's affairs are managed by its members, to a member of the body, (ii) in any other case, to any corresponding officer of the body" |
| F14 | s 1098D, the table: "a relevant officer mentioned in the second column" | `s 1098D table the position is a relevant officer of the firm` | a position the table does not name: (i) JUST FALSE; (ii) NOTHING | (i), by the ruling of 2026-11-05 (a) (a definition the text itself hands to a list) | "must be delivered to the registrar on its behalf by a relevant officer mentioned in the second column who is an individual" |
| F15 | s 1096(5): who sends the copy of the order | `s 1096(5) the copy of the order meets the requirement of s 1096(5)` | the text names no one; (i) leave the bearer unnamed; (ii) assume the party who obtained the order | (i): "Do not invent an actor" | "A copy of the court's order must be sent to the registrar for registration." |
| F16 | s 1122(2): who "the officer in question" is | `s 1122(2) the officer in question also commits the offence` | (i) the officer of the company who is in default (read with subsection (1)); (ii) any officer | (i), as an input the person states | "Where any such offence is committed by a company the officer in question also commits the offence" |
| F17 | s 1102(1): documents delivered under other enactments | `s 1102(1) the language provisions apply to the document` | NOTHING (subsection (2) lets regulations extend the provisions to documents delivered under any other enactment) or JUST FALSE | NOTHING | "The Secretary of State may make provision by regulations applying all or any of the listed provisions" |
| F18 | the "general limit in a magistrates' court" | `s 1112A(3)`, `s 1110B(4)`, `s 1131(2)` | the Act does not state the number: (i) an input (`MAYBE Period`); (ii) a number from outside the sources | (i) | "imprisonment for a term not exceeding the general limit in a magistrates’ court" and, in s 1131(2), "In relation to an offence committed before 2 May 2022, for “the general limit in a magistrates’ court” substitute “six months”" |
| F19 | s 1098B(1), a power with an "if" gate: "A person may apply ... if" (name-test sweep of 2026-11-12) | `s 1098B(1) the person may apply to become an authorised corporate service provider` | when limb (a), (b) or (c) is not met: (i) NOTHING; (ii) JUST FALSE, a failed "if" read as the text's own no | (i): a function named for a grant answers NOTHING when its "if" gate fails (the Guide's section 5, "In short"); the other reading is a one-word change at each of the three branches | "A person may apply to the registrar to become an authorised corporate service provider for the purposes of this Act if—" |
| F20 | s 1113(3), a power with an "if" gate (name-test sweep of 2026-11-12) | `s 1113(3) the person may apply to the court for an order` | when the company made good the default within the 14 days, or the 14 days have not yet ended: (i) NOTHING; (ii) JUST FALSE | (i), as for F19 | "If the company fails to make good the default within 14 days after service of the notice, the registrar, or any member or creditor of the company, may apply to the court for an order" |
| F21 | s 1110C(1), a power with an "if" gate (name-test sweep of 2026-11-12) | `s 1110C(1) the Secretary of State may give the notice` | when the Secretary of State is not satisfied of either ground: (i) NOTHING; (ii) JUST FALSE | (i), as for F19 | "if satisfied that to do so is necessary—" |
| F22 | s 1132(2), a power with an "if" gate (name-test sweep of 2026-11-12) | `s 1132(2) an order under this section may be made` | when reasonable cause is not shown for both limbs: (i) NOTHING; (ii) JUST FALSE | (i), as for F19 | "If on an application under this section there is shown to be reasonable cause to believe" |

### Jural-relation forks and rulings applied

The rulings of 2026-10-29, 2026-11-04 and 2026-11-05 are recorded word for word in `## Rulings applied (coa24)` below. Sites that rest on a ruling's reading, and not on a new fork, are listed under `## Marginal readings for a lawyer (coa24)`.

## Jural relations (coa24)

One row per provision that creates a relation, giving the party holding the right (a claim), privilege (a liberty), power or immunity, the party bearing the correlative duty, no-right, liability or disability, the section and the L4 rule. A provision that creates no such relation (a definition, a counting rule, a saving) is listed once as `none`. Each relation is stated once in layer 1, neutrally named, and never written from both sides. Offences are a claim of the State against the person who must not do the act; the prosecuting authority is not named in the text and is not a `Party` of the core, so none is invented.

| provision | holder | holds | bearer | correlative | L4 rule |
| --- | --- | --- | --- | --- | --- |
| s 1092C(1) | a person who made a statement in response to a s 1092A requirement | immunity | the prosecution and the court | disability (may not use the statement against the person) | `s 1092C(1) the statement may not be used against the person in the criminal proceedings` |
| s 1092C(2) | none: it takes the listed offences out of subsection (1), and creates no relation of its own |  |  |  | `s 1092C(2) subsection (1) applies to the offence` |
| s 1093(1) | the registrar | power (to give notice) | the company | liability (to be given notice) | `s 1093(1) the registrar may give notice to the company` |
| s 1093(2) | the company | claim (to be told the date of issue) | the registrar | duty (state the date) | `s 1093(2) the notice meets the requirement of s 1093(2)` |
| s 1093(3)(a) | the State (the prosecuting authority) | claim | the company | duty (deliver the necessary documents within the period) | `s 1093(3)(a) the company commits an offence`, `s 1093(3) the company's duty to deliver the necessary documents` |
| s 1093(3)(b) | the State | claim | every officer of the company in default | duty (see that the documents are delivered) | `s 1093(3)(b) the officer of the company commits an offence` |
| s 1093(4) | the court | power (to fine up to the limit) | the person convicted | liability | `s 1093(4) the punishment for the offence under subsection (3)` |
| s 1094(1) | the registrar | power (to remove material) | the company and anyone interested in the material | liability | `s 1094(1) and (3) the registrar may remove the material from the register` |
| s 1094(3) | a person interested in material whose registration had legal consequences | immunity (from removal unless the registrar is satisfied) | the registrar | disability | `s 1094(3) the registrar may exercise the power to remove the material` |
| s 1094AB(1) | the court | power (consequential orders) | those whose legal position the entry or its removal affected | liability | `s 1094AB(1) the court may make consequential orders on the application` |
| s 1096(1) | the person for whom the court directed removal | claim | the registrar | duty (remove the material) | `s 1096 the registrar must remove the material from the register under a court order` |
| s 1096(3) | persons relying on legally consequential material | immunity (from an order unless the court is satisfied) | the court | disability | `s 1096(3) the court may make an order for the removal of the material` |
| s 1096(4) | the court | power (consequential orders) | those affected | liability | `s 1096(4) the court may make consequential orders` |
| s 1096(5) | the registrar | claim (to a copy of the order) | unnamed: the text does not say who sends it (F15) | duty | `s 1096(5) the copy of the order meets the requirement of s 1096(5)` |
| s 1097(1)-(4) | the court | power (to direct) | the public, whose access to the register is affected | liability | `s 1097(1)-(4) the court may give the direction` |
| s 1097(5) | persons with an interest in disclosure | immunity (from a direction unless the court is satisfied) | the court | disability | `s 1097(5) the court may give a direction` |
| s 1097A(7), 1097B(9), 1097C(9) | the company (or the applicant) on appeal | claim | the court | duty (direct the registrar to register an appropriate address) | `s 1097A(7) ...`, `s 1097B(9) ...`, `s 1097C(9) ...` |
| s 1098(1) | the public | claim | the registrar | duty (publish notice of removal) | `s 1098(1) the registrar must cause notice of the removal to be published` |
| s 1098(2) | the public | claim | the registrar | duty (state what the notice must state) | `s 1098(2) the notice meets the requirement of s 1098(2)` |
| s 1098A | none: a definition |  |  |  | `s 1098A the person is an authorised corporate service provider` |
| s 1098B(1) | a person who is eligible | power (to apply) | the registrar | liability (to have the application considered) | `s 1098B(1) the person may apply to become an authorised corporate service provider` |
| s 1098B(2) | the registrar | claim | the applicant | duty (the application must contain the matters) | `s 1098B(2) the application meets the requirement of s 1098B(2)` |
| s 1098B(3) | the applicant | claim | the registrar | duty (check with the supervisory authority) | `s 1098B(3) the registrar must check with the supervisory authority` |
| s 1098B(4) | the applicant | claim | the registrar | duty (grant the application) | `s 1098B(4) the registrar must grant the application` |
| s 1098B(5) | those who rely on providers being fit and proper | claim | the registrar | duty (refuse the application) | `s 1098B(5) the registrar must refuse the application` |
| s 1098B(8), 1098C | none: definitions (the Money Laundering Regulations; supervised; "required information" and "name") |  |  |  | `s 1098B(8) ...`, `s 1098C(1) ...`, `s 1098C(2) ...`, `s 1098C(3) ...` |
| s 1098D | the registrar | claim | the firm applying | duty (deliver through a relevant officer who is an individual, with a statement of status) | `s 1098D the application meets the delivery requirements of s 1098D` |
| s 1098E(1)-(2) | the registrar | claim | an authorised corporate service provider | duty (notify a change of supervisory authority within 14 days) | `s 1098E(1) the provider's duty to notify the registrar of the change` |
| s 1098E(3)-(4) | the State | claim | the provider, and every officer of a firm in default | duty (offence) | `s 1098E(3) the person commits an offence`, `s 1098E(4) ...` |
| s 1098E(5) | the court | power (to fine) | the person convicted | liability | `s 1098E(5) the punishment on summary conviction` |
| s 1098F(1) | none: a status rule (a person ceases to be a provider) |  |  |  | `s 1098F(1) the person ceases to be an authorised corporate service provider` |
| s 1098G(5) | the court (as the regulations must provide) | power (to punish) | the person convicted of a regulations offence | liability | `s 1098G(5) the punishment the regulations must provide for an offence` |
| s 1098H(2) | none: a definition |  |  |  | `s 1098H(2) the regime is a relevant regulatory regime` |
| ss 1095, 1095A, 1120 | none: the text shows a row of dots where the provision stood (omitted or repealed) |  |  |  | (repealed or blank in this text) |
| s 1099(1) | the public and the bodies named | claim | the registrar | duty (keep the index) | `s 1099(1) the registrar must keep the body's name in the index` |
| s 1100 | any person | privilege (to inspect) | the registrar and the bodies | no-right | `s 1100 the person may inspect the registrar's index of company names` |
| s 1102(1), (3) | none: it says which provisions apply |  |  |  | `s 1102(1) ...`, `s 1102(3) ...` |
| s 1103 | the registrar | claim | a person delivering a document | duty (draw up and deliver in English) | `s 1103 the document must be drawn up and delivered in English` |
| s 1104(1) | a person delivering a document of a Welsh company | privilege (to use Welsh) | the registrar | no-right | `s 1104(1) the document may be drawn up and delivered in Welsh` |
| s 1104(2) | the registrar | claim | the person delivering the Welsh document | duty (accompany it with a certified English translation) | `s 1104(2) the document must be accompanied by a certified translation into English` |
| s 1104(3) | the public | claim | the registrar | duty (obtain a translation where the document is to be open to inspection) | `s 1104(3) the registrar must obtain a translation into English` |
| s 1104(4) | a Welsh company | privilege (to deliver a Welsh translation) | the registrar | no-right | `s 1104(4) the company may deliver a certified translation into Welsh of the document` |
| s 1104(5) | a person delivering a Welsh document of a Welsh company | immunity (from s 1105) | the registrar | disability | `s 1104(5) section 1105 applies to the document` |
| s 1105(1) | a person delivering a document on the list; the registrar | privilege (to use another language); claim (to a translation) | the registrar; the person delivering | no-right; duty | `s 1105(1) the document may be drawn up and delivered in a language other than English`, `s 1105(1) the delivery meets the requirement of s 1105(1)` |
| s 1106(1) | a company | privilege (to file a translation) | the registrar | no-right | `s 1106(1) the company may deliver certified translations of the document` |
| s 1106(3), (4), (6) | none: what the regulations must provide; the registrar's power as to form; a saving |  |  |  | `s 1106(3) ...`, `s 1106(4) ...`, `s 1106(6) ...` |
| s 1107(1), (3) | none: definitions |  |  |  | `s 1107(1) ...`, `s 1107(3) ...` |
| s 1107(2)(a) | a third party | immunity (from the company relying on a differing translation) | the company | disability | `s 1107(2)(a) the company may rely on the translation as against a third party` |
| s 1107(2)(b) | a third party | privilege (to rely on the translation) | the company | no-right (to deny it, unless it shows knowledge of the original) | `s 1107(2)(b) the third party may rely on the translation` |
| s 1108(1) | the registrar | claim | a person delivering a document | duty (permitted letters, characters and symbols only) | `s 1108(1) the names and addresses meet the requirement of s 1108(1)` |
| s 1109(1), (2) | the company; the registrar | privilege (to transliterate); power (to impose requirements as to form) | the registrar; the company | no-right; liability | `s 1109(1) ...`, `s 1109(2) ...` |
| s 1110A(1)-(3), (9) | none: definitions of "identity is verified" and "verification statement" |  |  |  | `s 1110A(1) ...`, `s 1110A(2) ...`, `s 1110A(3) ...`, `s 1110A(9) ...` |
| s 1110A(3) | the registrar | claim | the authorised corporate service provider | duty (specify the supervisory authority) | `s 1110A(3) the verification statement meets the requirement to specify the supervisory authority` |
| s 1110A(5) | a person required to deliver a statement of verified identity | privilege (deliver it at the same time) | the registrar | no-right | `s 1110A(5) the statement may be delivered at the same time as the verification statement` |
| s 1110B(4) | a person liable under a regulations offence | immunity (from a heavier punishment than the Act's scale) | the Secretary of State, making the regulations | disability | `s 1110B(4) the punishment the regulations must provide for an offence` |
| s 1110C(1) | the Secretary of State | power (to give a notice) | the person | liability | `s 1110C(1) the Secretary of State may give the notice` |
| s 1110C(2) | the person given the notice | immunity (from the listed requirements) | the company and the registrar | disability | `s 1110C(2) the effect applies in relation to the person` |
| s 1110C(3), 1110D(6) | none: definitions ("crime", "serious", "customer") |  |  |  | `s 1110C(3)(a)`, `s 1110C(3)(b)`, `s 1110D(6) ...` |
| s 1110D(5) | a person liable under a regulations offence | immunity (from imprisonment above the ceilings) | the Secretary of State, making the regulations | disability | `s 1110D(5) the regulations may provide for imprisonment of this term` |
| s 1110E | any person | privilege (to disclose to the registrar) | the registrar | no-right (to refuse) | `s 1110E the person may disclose the information to the registrar` |
| s 1110F(1) | the registrar | privilege (to disclose) | the person whose information is disclosed | no-right | `s 1110F(1) the registrar may disclose the information` |
| s 1110F(3) | none: "public authority" includes |  |  |  | `s 1110F(3) the person or body is a public authority` |
| s 1110G(1) | a person who discloses under s 1110E or 1110F | immunity (from breach of confidence) | the person to whom the confidence is owed | disability | `s 1110G(1) the disclosure breaches an obligation of confidence or any other restriction on the disclosure of information` |
| s 1110G(2) | none: it limits the privilege of ss 1110E and 1110F |  |  |  | `s 1110G(2) sections 1110E and 1110F authorise the disclosure` |
| s 1110G(3) | HMRC | claim | the registrar | duty (no disclosure of HMRC information without authorisation) | `s 1110G(3) the registrar may disclose the information under section 1110F` |
| s 1110G(4) | HMRC | claim | the recipient and anyone obtaining the information from them | duty | `s 1110G(4) the recipient, or a person obtaining the information from the recipient, may disclose the information` |
| s 1110G(5) | the State | claim | any person who discloses in contravention | duty (offence) | `s 1110G(5) the person commits an offence` |
| s 1110G(6) | the person charged | immunity (a defence) | the court | disability (to convict) | `s 1110G(6) this section gives a defence` |
| s 1110G(7), (8) | none: an incorporation of another Act's provisions; definitions |  |  |  | `s 1110G(7) ...`, `s 1110G(8) ...` |
| s 1111(1) | the registrar | power (requirements as to who gives a certificate) | persons giving certificates | liability | `s 1111(1) the registrar may impose requirements as to the person by whom the certificate or verification is to be given` |
| s 1111(2)-(3) | persons giving certificates | immunity (from requirements inconsistent with an enactment) | the registrar | disability | `s 1111(3) the registrar may impose the requirement` |
| s 1112(1) | the State | claim | any person who delivers a false document or makes a false statement to the registrar | duty (offence) | `s 1112(1) the person commits the offence` |
| s 1112(2) | the State | claim | every officer of a firm in default | duty (offence) | `s 1112(2) the officer of the firm who is in default also commits the offence` |
| s 1112(3) | the court | power (to fine) | the person convicted | liability | `s 1112(3) the punishment on summary conviction` |
| s 1112A(1)-(3) | the State; the court | claim; power (to imprison or fine) | any person who knowingly delivers or makes a false statement; the person convicted | duty (offence); liability | `s 1112A(1) ...`, `s 1112A(2) ...`, `s 1112A(3) the punishment for the offence` |
| s 1112B(1) | a person holding a certificate | immunity | the State and the court | disability (to hold the person liable) | `s 1112B(1) the person is liable for the commission of the offence` |
| s 1112B(2)-(3) | the Secretary of State | power (to issue and to revoke a certificate) | the person | liability | `s 1112B(2) the Secretary of State may issue the certificate`, `s 1112B(3) ...` |
| s 1112B(4) | none: definitions ("crime", "serious") |  |  |  | `s 1112B(4)(a) ...`, `s 1112B(4)(b) ...` |
| s 1113(2) | the registrar, a member or a creditor | power (to give notice) | the company | liability | `s 1113(2) the person may give notice to the company requiring it to comply with the obligation` |
| s 1113(3) | the person who gave the notice; the registrar, a member or a creditor | claim (that the default be made good within 14 days); power (to apply to the court) | the company; the company and any specified officer | duty; liability | `s 1113(3) the company's duty to make good the default`, `s 1113(3) the person may apply to the court for an order` |
| s 1113(4) | the court | power (costs) | the company and the officers responsible | liability | `s 1113(4) the court's order may provide that costs are borne by the company or by officers of it responsible for the default` |
| s 1113(5) | none: a saving for offences and civil penalties |  |  |  | `s 1113(5) section 1113 affects the operation of the enactment` |
| s 1114 | none: definitions and an extension to information not in documentary form |  |  |  | `s 1114(1)(a) ...`, `s 1114(1)(b) ...`, `s 1114(2) ...` |
| s 1115(2) | the recipient of an electronic document | claim | the registrar | duty (authenticate in the way the registrar's rules specify) | `s 1115(2) the document must be authenticated in the manner specified by registrar's rules` |
| s 1116(1) | the registrar | privilege (to publish by approved means) | the public | no-right (to Gazette publication) | `s 1116(1) the notice may instead be published by the approved means` |
| s 1116(5) | the public | claim | the registrar | duty (publish a first notice in the Gazette) | `s 1116(5) the registrar meets the requirement of s 1116(5)` |
| s 1116(6) | none: the registrar may give notice both ways; the day the requirement is met |  |  |  | `s 1116(6) ...` |
| s 1117(3) | the public | claim | the registrar | duty (publicise the rules and make copies available) | `s 1117(3)(a) ...`, `s 1117(3)(b) ...` |
| s 1118 | none: a saving for the Government Trading Funds Act 1973 |  |  |  | `s 1118 ...` |
| s 1119(1) | the registrar; the public | power (to direct); claim (that the direction be printed and available) | persons delivering documents of the class; the registrar | liability; duty | `s 1119(1) the registrar may direct ...`, `s 1119(1) the direction meets the requirement of s 1119(1)` |
| s 1119(2) | the registrar | immunity (a document delivered elsewhere is treated as not delivered) | the person who delivered it | disability | `s 1119(2) the document is treated as delivered` |
| s 1119(3) | none: registrar's rules are not subordinate legislation for s 71 of the 1994 Act |  |  |  | `s 1119(3) ...` |
| s 1121(1)-(3) | none: definitions of "officer" and "in default" for the offences of other sections |  |  |  | `s 1121(1) ...`, `s 1121(2) ...`, `s 1121(3) ...`, `s 1121 the person is an officer in default` |
| s 1122(1) | a company that is an officer of another company | immunity (from the offence unless one of its officers is in default) | the State | disability | `s 1122(1) the company commits an offence as an officer in default` |
| s 1122(2) | the State | power (to proceed against and punish the officer in question) | the officer in question | liability | `s 1122(2) the officer in question also commits the offence` |
| s 1122(3), 1123 | none: a cross-reference and rules of reading |  |  |  | `s 1122(3) ...`, `s 1123(1) ...`, `s 1123 the person is read as ...` |
| s 1124 | none: amendments of the Companies Act 1985 (machinery) |  |  |  | (inert) |
| s 1125 | none: a definition of "daily default fine" and a counting rule for the fine on a later conviction |  |  |  | `s 1125(1) ...`, `s 1125(2) ...` |
| s 1126 | a person accused of one of the listed offences | immunity (from proceedings without the named consent) | the prosecutor | disability | `s 1126(2)-(3) the proceedings may be brought` |
| s 1126(2)-(3) consent | the Secretary of State or the Director of Public Prosecutions | power (to consent or bring proceedings) | the accused | liability | `s 1126(2)-(3) the consent required for the proceedings` |
| s 1127(1) | the prosecutor | power (to take summary proceedings at a place) | the defendant | liability | `s 1127(1) summary proceedings for the offence may be taken at the place` |
| s 1127(2) | none: a saving for other jurisdiction |  |  |  | `s 1127(2) ...` |
| s 1128 | the accused | immunity (from proceedings out of time) | the prosecutor and the court | disability | `s 1128(1) the information was laid in time`, `s 1128(2) ...`, `s 1128(3) ...` |
| s 1128(4) | none: a rule of evidence (the certificate is conclusive) |  |  |  | `s 1128(4) ...` |
| s 1129 | a person entitled to refuse to disclose privileged information | immunity | those enforcing the Companies Acts | disability | `s 1129 the Companies Acts require the person to disclose the information` |
| s 1130(1) | the members of an unincorporated body | immunity (from being named in the proceedings) | the prosecutor | disability | `s 1130(1) the proceedings meet the requirement of s 1130(1)` |
| s 1130(2) | none: it applies service rules and listed provisions as for a body corporate |  |  |  | `s 1130(2) ...` |
| s 1130(3) | the members of an unincorporated body | immunity (their own funds are not liable for the fine) | the prosecutor and the court | disability | `s 1130(3) the fine is paid as the subsection requires` |
| s 1131 | none: a transitional counting rule (six months before 2 May 2022) |  |  |  | `s 1131(1) ...`, `s 1131(2) ...` |
| s 1132(1)-(3) | the Director of Public Prosecutions, the Secretary of State, a chief officer of police, the Lord Advocate, the Department of Enterprise, Trade and Investment, a chief superintendent of the PSNI; the court | power (to apply); power (to order inspection or production) | the company, its secretary and its officers (and, for inspection only, a banker); the company, its secretary and its officers | liability; liability | `s 1132(1) ...`, `s 1132(2) an order under this section may be made`, `s 1132(3)-(4) the order may contain the provision` |
| s 1132(3)(b) | the person named in the order | claim (to production of the documents) | the secretary or the named officer | duty (produce) | `s 1132(3)-(4) the order may contain the provision` |
| s 1132(5) | the applicant for the order | immunity (from appeal) | the appellate courts | disability | `s 1132(5) the decision may be appealed` |
| s 1132(6) | none: "document" includes |  |  |  | `s 1132(6) ...` |
| s 1132A(2), (8) | none: definitions ("relevant offence", "conduct") |  |  |  | `s 1132A(2) ...`, `s 1132A(8) ...` |
| s 1132A(4) | a person liable to a financial penalty | immunity (from a penalty above £10,000) | the Secretary of State, making the regulations | disability | `s 1132A(4) the regulations may provide for this maximum financial penalty` |
| s 1132A(5) | a person who has been prosecuted or convicted, or given a financial penalty | immunity (double jeopardy) | the registrar and the prosecutor | disability | `s 1132A(5)(a) ...`, `s 1132A(5)(b) ...` |
| s 1133 | a person who committed an offence before the commencement of the relevant provision | immunity (from the Part 36 provisions other than s 1132) | the prosecutor | disability | `s 1133 the provision of Part 36 applies to the offence` |
| ss 1094(4)-(5), 1094A, 1097A (apart from (4A)(a), (5)(a), (7)), 1097B and 1097C (apart from (2), (6), (9)), 1098B(6)-(7), 1098C(5)-(6), 1098F(2)-(5), 1098G (apart from (5)), 1098H(1), (3)-(4), 1099(4)-(5), 1101, 1102(2), (4), 1105(3), 1106(2), (5), 1108(2)-(3), 1110, 1110A(4), (6)-(8), 1110B (apart from (4)), 1110D (apart from (5), (6)), 1110F(2), 1116(2)-(4), 1117(1)-(2), 1132A(1), (3), (6), (7) | the Secretary of State (or, for s 1117, the registrar) | power (to make regulations, orders or rules) | the persons the regulations, orders or rules affect | liability | (inert, reason 2: no L4 rule) |

## Marginal readings for a lawyer (coa24)

The brief leaves two readings "for a lawyer, not for you to decide":
- Reading (a): a failed "if" counts as the text's no, clause by clause, within the provision that holds the "if" (an inference: "if A then B" does not itself say "if not A then not B"), and flat negatives count as the text saying no.
- Reading (b): a prohibition or grant limited by its own wording does not count as the text saying no.

Every branch of the layer-1 modules that rests on either reading carries a `-- FALSE-kind` or `-- NOTHING-kind` comment with the quoted words, so the table below is generated from those comments (`work/branches.py --md2`: 305 comments in the eleven layer-1 modules; the 319 that `work/checkquotes.py` counts in the check section below are these plus the 14 in `coa24-seat.l4`, whose NOTHING branches carry the same tags) and not written from memory.
A reviewer who prefers the other reading changes the branch in the function named, and the tests beside it.
How the columns were sorted: each FALSE-kind comment is placed by the words it quotes (the script's heuristic, not a lawyer's judgment): a quote containing "if", "where", "while", "until", "unless", "only if", "except" or "provided that" is counted under reading (a); otherwise a quote containing "means" is a definition; otherwise it is a flat negative or other (a period the text fixes, or a defence).
The NOTHING-kind comments are counted by the reason they give; "limited by its own wording" is reading (b), and the five other reasons are those of the brief's list.

- Reading (a) rests on 42 branches: the other reading, where the text's "if" would not close the case, is NOTHING at each of them.
- Reading (b) rests on 124 branches: the other reading, where the text's wording would be taken as saying no, is JUST FALSE at each of them.
- Definitions (22) and flat negatives or other (61) are the text's own no under either reading, with the exceptions in the fork register (F3, F8, F9, F11, F12, F14).

| module | function | FALSE-kind: an "if"-type word, reading (a) | FALSE-kind: a "means" definition | FALSE-kind: a flat negative or other | NOTHING-kind: limited by its own wording, reading (b) | NOTHING-kind: other reasons |
| --- | --- | --- | --- | --- | --- | --- |
| acsp | `s 1098A the person is an authorised corporate service provider` |  | 1 |  |  |  |
| acsp | `s 1098B(1) the person may apply to become an authorised corporate service provider` |  |  |  | 3 | 2 points outside the text |
| acsp | `s 1098B(2) the application meets the requirement of s 1098B(2)` |  |  | 1 |  |  |
| acsp | `s 1098B(3) the registrar must check with the supervisory authority` |  |  |  | 1 |  |
| acsp | `s 1098B(5) the registrar must refuse the application` | 1 |  |  |  |  |
| acsp | `s 1098B(4) the registrar must grant the application` | 2 |  | 2 |  | 1 points outside the text |
| acsp | `s 1098B(8) the person is supervised by the supervisory authority` | 1 |  |  |  |  |
| acsp | `s 1098B(8) the authority is a supervisory authority` |  | 1 |  |  |  |
| acsp | `s 1098C(1) the application contains the required information about the firm` |  | 1 |  |  |  |
| acsp | `s 1098C(3) the name supplied meets the requirement to contain the applicant's name` |  | 1 |  |  |  |
| acsp | `s 1098C(2) the application contains the required information about the individual` |  | 1 |  |  |  |
| acsp | `s 1098D table the position is a relevant officer of the firm` | 2 |  | 5 |  |  |
| acsp | `s 1098D the application meets the delivery requirements of s 1098D` |  |  | 1 |  |  |
| acsp | `s 1098E(1)-(2) the last day for notifying the registrar of the change` |  |  |  |  | 1 silent |
| acsp | `s 1098E(2) the change cannot yet be treated as having occurred` | 1 |  |  | 1 |  |
| acsp | `s 1098E(3) the person commits an offence` |  |  |  | 1 |  |
| acsp | `s 1098E(1)-(3) the person commits an offence by failing to notify the registrar in time` |  |  |  |  | 1 silent |
| acsp | `s 1098E(4) the officer of the firm who is in default also commits the offence` |  |  |  | 2 |  |
| acsp | `s 1098F(1) the person ceases to be an authorised corporate service provider` |  |  |  |  | 1 points outside the text |
| acsp | `s 1098H(2) the regime is a relevant regulatory regime` |  | 1 |  |  |  |
| delivery | `s 1111(1) the registrar may impose requirements as to the person by whom the certificate or verification is to be given` |  |  |  | 1 |  |
| delivery | `s 1111(2) the power conferred by section 1068 is exercisable in relation to the certificate or verification as if it were a separate document` |  |  |  | 1 |  |
| delivery | `s 1111(3) the registrar may impose the requirement` |  |  | 1 | 1 |  |
| delivery | `s 1113(1) the section applies` |  |  |  | 1 |  |
| delivery | `s 1113(2) the person may give notice to the company requiring it to comply with the obligation` |  |  |  | 2 |  |
| delivery | `s 1113(3) the person may apply to the court for an order` |  |  |  | 4 |  |
| delivery | `s 1113(4) the court's order may provide that costs are borne by the company or by officers of it responsible for the default` |  |  |  | 1 |  |
| delivery | `s 1113(5) section 1113 affects the operation of the enactment` |  |  | 1 | 1 |  |
| delivery | `s 1114(1)(a) the thing is a document in Part 35` |  | 1 |  |  |  |
| delivery | `s 1114(1)(b) the act is delivering a document` |  |  | 1 |  | 1 includes |
| delivery | `s 1114(2) Part 35 applies to the supply of the information as it applies to the delivery of a document` |  |  |  | 1 |  |
| delivery | `s 1115(2) the document must be authenticated in the manner specified by registrar's rules` |  |  |  | 1 |  |
| delivery | `s 1116(1) the notice may instead be published by the approved means` |  |  |  | 1 |  |
| delivery | `s 1116(5) the registrar meets the requirement of s 1116(5)` |  | 1 |  | 1 |  |
| delivery | `s 1116(6) this section prevents the registrar from giving public notice both in the Gazette and by approved means` |  | 1 |  | 1 |  |
| delivery | `s 1117(3)(a) the registrar meets the requirement to publicise the rules` |  |  | 1 |  |  |
| delivery | `s 1118 the provision affects the operation in relation to the registrar of section 3(1) of the Government Trading Funds Act 1973` |  |  | 1 | 1 |  |
| delivery | `s 1119(1) the registrar may direct that documents of the class be delivered to a specified address of the authorised person` |  |  |  | 1 |  |
| delivery | `s 1119(1) the direction meets the requirement of s 1119(1)` |  |  | 1 |  |  |
| delivery | `s 1119(2) the document is treated as delivered` |  |  | 1 | 1 |  |
| delivery | `s 1119(3) the provision is subordinate legislation for the purposes of section 71 of the Deregulation and Contracting Out Act 1994` |  |  | 1 | 1 |  |
| disclosure | `s 1110E the person may disclose the information to the registrar` |  |  |  | 1 |  |
| disclosure | `s 1110F(1) the registrar may disclose the information` |  |  |  |  | 1 list not closed |
| disclosure | `s 1110F(3) the person or body is a public authority` |  |  |  |  | 1 includes |
| disclosure | `s 1110G(1) the disclosure breaches an obligation of confidence or any other restriction on the disclosure of information` |  |  | 1 | 1 |  |
| disclosure | `s 1110G(2) sections 1110E and 1110F authorise the disclosure` | 1 |  |  |  | 1 silent |
| disclosure | `s 1110G(3) the registrar may disclose the information under section 1110F` |  |  | 1 | 1 |  |
| disclosure | `s 1110G(4) the recipient, or a person obtaining the information from the recipient, may disclose the information` |  |  | 1 | 1 |  |
| disclosure | `s 1110G(5) the person commits an offence` |  |  |  | 1 |  |
| disclosure | `s 1110G(6) this section gives a defence` |  |  | 1 |  |  |
| disclosure | `s 1110G(7) subsections (4) to (7) of section 19 of the Commissioners for Revenue and Customs Act 2005 apply to the offence` |  |  |  | 1 |  |
| disclosure | `s 1110G(8) the information is HMRC information` |  | 1 |  |  |  |
| disclosure | `s 1110G(8) the body is HMRC` |  | 1 |  |  |  |
| false-statements | `s 1112(1) the person commits the offence` |  |  |  | 1 |  |
| false-statements | `s 1112(2) the officer of the firm who is in default also commits the offence` |  |  |  | 2 |  |
| false-statements | `s 1112A(1) the person commits the offence` |  |  |  | 1 |  |
| false-statements | `s 1112A(2) the officer of the firm who is in default also commits the offence` |  |  |  | 2 |  |
| false-statements | `s 1112A(3) the punishment for the offence` |  |  |  | 1 | 1 points outside the text |
| false-statements | `s 1112B(1) the person is liable for the commission of the offence` |  |  | 1 | 1 |  |
| false-statements | `s 1112B(2) the Secretary of State may issue the certificate` | 1 |  |  |  |  |
| false-statements | `s 1112B(3) the Secretary of State may revoke the certificate` |  |  |  | 1 |  |
| false-statements | `s 1112B(4)(a) the conduct is crime` | 1 |  |  |  |  |
| false-statements | `s 1112B(4)(b) the crime is serious` | 1 |  |  |  |  |
| identity | `s 1110A(1) the individual's identity is verified` | 1 |  | 1 |  | 1 points outside the text |
| identity | `s 1110A(2) the statement is a verification statement` |  |  | 1 |  |  |
| identity | `s 1110A(3) the verification statement meets the requirement to specify the supervisory authority` |  |  | 1 |  |  |
| identity | `s 1110A(5) the statement may be delivered at the same time as the verification statement` |  |  |  | 1 |  |
| identity | `s 1110A(9) the authority is a supervisory authority` |  | 1 |  |  |  |
| identity | `s 1110B(4) the punishment the regulations must provide for an offence` |  |  |  | 1 | 1 points outside the text |
| identity | `s 1110C(1) the Secretary of State may give the notice` |  |  |  | 1 |  |
| identity | `s 1110C(2) the effect applies in relation to the person` |  |  |  | 1 |  |
| identity | `s 1110C(3)(a) the conduct is crime` | 1 |  |  |  |  |
| identity | `s 1110C(3)(b) the crime is serious` | 1 |  |  |  |  |
| identity | `s 1110D(1) the person is a relevant person` |  |  | 1 |  |  |
| identity | `s 1110D(5) the regulations may provide for imprisonment of this term` |  |  | 2 | 2 |  |
| identity | `s 1110D(6) the person is a customer` |  |  |  |  | 1 includes |
| index | `s 1099(2)-(3) the section applies to the body` |  |  | 1 |  | 1 list not closed |
| index | `s 1099(1) the registrar must keep the body's name in the index` |  |  |  | 1 | 1 list not closed |
| index | `s 1099(1) the index is the registrar's index of company names` |  |  | 1 |  |  |
| language | `s 1102(1) the language provisions apply to the document` |  |  |  |  | 1 points outside the text |
| language | `s 1103 the document must be drawn up and delivered in English` |  |  | 2 |  |  |
| language | `s 1104(1) the document may be drawn up and delivered in Welsh` |  |  |  | 1 | 1 points outside the text |
| language | `s 1104(2) the document must be accompanied by a certified translation into English` | 2 |  |  | 1 | 1 points outside the text |
| language | `s 1104(2) the delivery meets the requirement of s 1104(2)` |  |  | 1 |  | 1 points outside the text |
| language | `s 1104(3) the registrar must obtain a translation into English` | 2 |  |  |  |  |
| language | `s 1104(3) the translation is treated as delivered in accordance with the same provision as the original` |  |  |  | 1 |  |
| language | `s 1104(4) the company may deliver a certified translation into Welsh of the document` |  |  |  | 2 | 1 points outside the text |
| language | `s 1104(5) section 1105 applies to the document` |  |  | 1 | 2 |  |
| language | `s 1105(2) the section applies to the document` |  |  |  |  | 1 points outside the text |
| language | `s 1105(1) the document may be drawn up and delivered in a language other than English` |  |  |  | 1 |  |
| language | `s 1105(1) the delivery meets the requirement of s 1105(1)` |  |  | 1 | 2 |  |
| language | `s 1106(1) the company may deliver certified translations of the document` |  |  |  | 2 | 1 points outside the text |
| language | `s 1106(3) the regulations must provide that the facility is available` |  |  |  | 1 |  |
| language | `s 1106(4) the power of the registrar to impose requirements includes power to impose the requirement` |  |  |  |  | 1 includes |
| language | `s 1106(6) section 1106 applies` | 1 |  |  |  | 1 silent |
| language | `s 1107(1) the translation is a certified translation` |  | 1 |  |  |  |
| language | `s 1107(2)(a) the company may rely on the translation as against a third party` |  |  | 1 | 1 |  |
| language | `s 1107(2)(b) the third party may rely on the translation` | 1 |  |  | 1 |  |
| language | `s 1107(3) the person is a third party` |  | 1 |  |  |  |
| language | `s 1108(1) the names and addresses meet the requirement of s 1108(1)` |  |  | 1 |  | 1 points outside the text |
| language | `s 1109(1) the company or other body may deliver a transliteration into Roman characters` |  |  |  | 1 |  |
| language | `s 1109(2) the power of the registrar to impose requirements includes power to impose the requirement` |  |  |  |  | 1 includes |
| officers | `s 1121(1) the section has effect for the provision` |  |  |  | 1 |  |
| officers | `s 1121(2) the person is an officer of the company` |  |  |  |  | 1 includes |
| officers | `s 1121(3) the officer is in default` | 1 |  |  |  |  |
| officers | `s 1121 the person is an officer in default` | 1 |  |  |  | 1 silent |
| officers | `s 1122(1) the company commits an offence as an officer in default` | 1 |  |  | 2 |  |
| officers | `s 1122(2) the officer in question also commits the offence` |  |  |  | 1 |  |
| officers | `s 1123(1) section 1121 applies to the body` |  |  |  |  | 1 silent |
| officers | `s 1123 the person is read as a director for the purposes of section 1121(2)(a)` |  |  |  | 5 | 1 silent |
| officers | `s 1123 the person is read as a manager or secretary for the purposes of section 1121(2)(a)` |  |  |  | 1 | 1 silent |
| penalty | `s 1125(1) the section defines the daily default fine for the offence provision` |  |  |  | 1 |  |
| penalty | `s 1125(1) the fine limit in pounds` |  |  |  |  | 1 silent; 1 undefined term |
| penalty | `s 1125(2) the fine limit that applies on this conviction` |  |  |  |  | 1 silent |
| penalty | `s 1125(2) the limit applies for each day` |  |  | 1 |  | 1 silent |
| penalty | `s 1125(2) the most the person can be fined on this conviction, in pounds` |  |  |  |  | 4 silent |
| penalty | `s 1131(1) the section applies to the provision` |  |  |  | 1 |  |
| penalty | `s 1131(2) the term of imprisonment the provision refers to` |  |  |  |  | 1 points outside the text |
| prosecution | `s 1126(2)-(3) the consent required for the proceedings` |  |  |  | 2 | 1 silent |
| prosecution | `s 1126(2)-(3) the proceedings may be brought` | 3 |  |  | 4 |  |
| prosecution | `s 1127(1) summary proceedings for the offence may be taken at the place` |  |  |  | 2 |  |
| prosecution | `s 1127(2) section 1127(1) prejudices the jurisdiction` |  |  | 1 | 1 |  |
| prosecution | `s 1128(1) the information was laid in time` | 1 |  | 1 |  | 1 points outside the text |
| prosecution | `s 1128(2) the proceedings in Scotland were commenced in time` | 1 |  | 2 |  | 4 points outside the text |
| prosecution | `s 1128(3) the complaint was made in time` | 1 |  | 1 |  | 1 points outside the text |
| prosecution | `s 1128(4) the date on which the evidence came to notice, as the certificate conclusively shows` |  |  |  | 1 |  |
| prosecution | `s 1129 the Companies Acts require the person to disclose the information` |  |  | 1 | 1 |  |
| prosecution | `s 1130(1) the proceedings meet the requirement of s 1130(1)` |  |  | 1 | 1 |  |
| prosecution | `s 1130(2) the rules of court as to service, and the listed provisions, apply as if the body were a body corporate` |  |  |  | 1 |  |
| prosecution | `s 1130(3) the fine is paid as the subsection requires` |  |  | 1 | 1 |  |
| prosecution | `s 1132(1) the person may apply for an order under this section` |  |  |  | 1 |  |
| prosecution | `s 1132(2) an order under this section may be made` |  |  |  | 1 |  |
| prosecution | `s 1132(3)-(4) the order may contain the provision` | 1 |  |  | 1 |  |
| prosecution | `s 1132(5) the decision may be appealed` |  |  | 1 | 1 |  |
| prosecution | `s 1132(6) the thing is a document` |  |  |  |  | 1 includes |
| prosecution | `s 1132A(2) the offence is a relevant offence under this Act` |  | 2 | 2 |  |  |
| prosecution | `s 1132A(4) the regulations may provide for this maximum financial penalty` |  |  | 1 | 1 |  |
| prosecution | `s 1132A(5)(a) the regulations must provide that no financial penalty may be imposed on the person` |  |  |  | 1 |  |
| prosecution | `s 1132A(5)(b) the regulations must provide that no proceedings may be brought against the person` |  |  |  | 1 |  |
| prosecution | `s 1132A(8) the thing is conduct` |  | 1 |  |  |  |
| prosecution | `s 1133 the provision of Part 36 applies to the offence` | 1 |  |  | 1 | 1 silent |
| register | `s 1092C(2) subsection (1) applies to the offence` |  |  | 7 |  |  |
| register | `s 1092C(1) the statement may not be used against the person in the criminal proceedings` |  |  |  | 2 |  |
| register | `s 1093(1) the registrar may give notice to the company` |  |  |  | 1 |  |
| register | `s 1093(1)(a)-(b) the notice is a notice of the kind subsection (1) describes` |  |  |  | 1 |  |
| register | `s 1093(2) the notice meets the requirement of s 1093(2)` |  |  | 1 |  |  |
| register | `s 1093(3)(a) the company commits an offence` | 2 |  |  | 2 |  |
| register | `s 1093(3)(b) the officer of the company commits an offence` | 1 |  |  | 1 |  |
| register | `s 1093(4) the punishment for the offence under subsection (3)` |  |  |  |  | 1 silent |
| register | `s 1094(1) the registrar may remove the material from the register` |  |  |  | 1 |  |
| register | `s 1094(2) the power to remove material may be exercised` |  |  |  | 1 |  |
| register | `s 1094(3) the registrar may exercise the power to remove the material` | 1 |  |  | 2 |  |
| register | `s 1094(1) and (3) the registrar may remove the material from the register` | 1 |  |  |  |  |
| register | `s 1094AB(2) the registrar is treated as having removed material from the register` |  |  |  |  | 1 includes |
| register | `s 1094AB(1) the court may make consequential orders on the application` |  |  |  | 1 |  |
| register | `s 1096(1) the registrar must remove the material from the register` |  |  |  | 1 |  |
| register | `s 1096(2) the court order meets the requirement of s 1096(2)` | 1 |  |  |  |  |
| register | `s 1096(3) the court may make an order for the removal of the material` | 1 |  |  | 1 |  |
| register | `s 1096(4) the court may make consequential orders` |  |  |  | 1 |  |
| register | `s 1096(5) the copy of the order meets the requirement of s 1096(5)` |  |  | 1 |  |  |
| register | `s 1096(5A) and (6) section 1096 applies to the material` | 1 |  | 1 |  | 1 silent |
| register | `s 1096 the registrar must remove the material from the register under a court order` | 1 |  |  |  |  |
| register | `s 1097(1)-(4) the court may give the direction` |  |  |  | 1 |  |
| register | `s 1097(5) the court may give a direction` | 1 |  |  | 1 |  |
| register | `s 1097(1)-(5) the court may give the direction on these facts` | 1 |  |  | 1 |  |
| register | `s 1097A(5)(a) the regulations may provide for a suspension of this length` |  |  |  | 1 |  |
| register | `s 1097A(7) the court must direct the registrar to register such address as the registered office as the court considers appropriate` |  |  |  | 1 |  |
| register | `s 1097B(9) the court must direct the registrar to register such address as the relevant person's registered service address as the court considers appropriate` |  |  |  | 1 |  |
| register | `s 1097C(9) the court must direct the registrar to register such address as the principal office of the relevant person as the court considers appropriate` |  |  |  | 1 |  |
| register | `s 1097B(2) the address is the registered service address of the relevant person` |  | 1 |  |  |  |
| register | `s 1097B(2) the person is a relevant person` |  | 1 |  |  | 1 points outside the text |
| register | `s 1097C(2) the address is the address registered as the principal office of the relevant person` |  | 1 |  |  |  |
| register | `s 1097C(2) the person is a relevant person` |  | 1 |  |  | 2 points outside the text |
| register | `s 1098(1) the registrar must cause notice of the removal to be published` |  |  |  | 1 |  |
| register | `s 1098(1) the publication meets the requirement of s 1098(1)` |  | 1 |  |  |  |
| register | `s 1098(2) the notice meets the requirement of s 1098(2)` |  |  | 1 |  |  |

### Where the readings are not the whole story

- A "must" not done (`meets the requirement of s N`) is JUST FALSE by fork F10, and appears in the "flat negative or other" column.
- An "except", "only if" or "unless" once met is NOTHING at forks F3, F8 and F9 (and JUST TRUE at `s 1096(3)`, whose sentence itself says the court "may make an order").
- "Without reasonable excuse" and "knowingly" (ss 1112, 1112A) and "any member or creditor" (s 1113) limit the offence or the power by their own wording: reading (b).

### Name-test flips (sweep of 2026-11-12)

Four functions are named for a grant or a power and used to answer JUST FALSE when an "if" gate failed, which reads as "may not".
Each now answers NOTHING there, with one fork line in the fork register; the other reading, JUST FALSE with a failed "if" read as the text's own no, is a one-word change at the branches named.
- F19, `s 1098B(1) the person may apply to become an authorised corporate service provider`: NOTHING when limb (a), (b) or (c) of the "if" is not met (3 branches); the other reading is JUST FALSE.
- F20, `s 1113(3) the person may apply to the court for an order`: NOTHING when the company made good the default in time or the 14 days have not ended (2 branches); the other reading is JUST FALSE.
- F21, `s 1110C(1) the Secretary of State may give the notice`: NOTHING when the Secretary of State is not satisfied of either ground (1 branch); the other reading is JUST FALSE.
- F22, `s 1132(2) an order under this section may be made`: NOTHING when reasonable cause is not shown for both limbs (1 branch); the other reading is JUST FALSE.

### Reading a result: FALSE and NOTHING (coa24)

In this part of the Act almost every provision is a power, a duty, an offence, a penalty or a time limit addressed to the registrar, a company, an officer or a court, so a result is read as follows.
- JUST TRUE: the text says yes to the case (the offence is committed, the person may apply, the notice must be published).
- JUST FALSE: the text itself says no to the case in its own words. In this row that happens in five ways: a "means" definition not met ("authorised corporate service provider" means ...); an "if" that is not met, by marginal reading (a), except in a function named for a grant or a power, which answers NOTHING when its "if" gate fails (F19 to F22); a flat negative that applies (a person "is not liable", a document "is treated as not having been delivered", a decision "is not appealable", HMRC information "may not be disclosed" without authorisation); a period the text fixes ("within three years after the commission of the offence") that has run; and a defence not proved (ruling (b) of 2026-11-05: "this section gives no defence on these facts", never "no defence at all").
- NOTHING ("not covered"): the text does not decide the case. In this row that means: a grant or offence limited by its own wording and the case outside the limit ("without reasonable excuse", "knowingly", "any member or creditor"); a list that "includes" or is not closed; a power the Secretary of State exercises by regulations that are not in the sources (the amount of a level on the standard scale, the characters permitted in names, the descriptions of document excepted from translation); a date or fact that someone else holds (the day evidence came to the Director of Public Prosecutions's knowledge); and an "except", "only if" or "unless" once it is met, where the thing allowed is in another provision (F3, F8).
- A caller must never turn NOTHING into FALSE. "No offence is shown on these facts" is NOTHING; "the Act says there is no offence" is JUST FALSE. The seat layer answers `MAYBE BOOLEAN`, `MAYBE NUMBER` or `MAYBE DATE`, and its `@desc` says that NOTHING is "the Act does not decide this".
- A function whose name ends "meets the requirement of s N" answers JUST FALSE when the "must" it cites is not done (F10). It claims nothing about what follows.

### Name-test sweep of 2026-11-12

The lead's sweep took every layer-1 function whose name contains "may", "permitted", "power", "entitled" or "authorised" (53 functions, found by `grep` over the eleven modules) and asked of each whether it is named for a grant or a power and answers JUST FALSE because an "if" gate failed.
Such a failed gate reads as "may not", so it now answers NOTHING (the Guide's section 5, "In short": a grant limited by its own wording and the case outside the limit).
Where the text closes the gate itself ("only if", "unless", "except", "may not", "must not", "do not authorise", "is not appealable") or the function is a bar, a duty or a definition, JUST FALSE is kept.

| flipped to NOTHING | kept JUST FALSE (gate closed by the text) | listed: "may" with where/when/upon | listed: "entitled" |
| --- | --- | --- | --- |
| 4 | 18 | 0 | 0 |

Flipped, one fork line each in the fork register (F19 to F22) and in the marginal readings above; the other reading, JUST FALSE with a failed "if" read as the text's own no, is named at each:
- `s 1098B(1) the person may apply to become an authorised corporate service provider`
- `s 1113(3) the person may apply to the court for an order`
- `s 1110C(1) the Secretary of State may give the notice`
- `s 1132(2) an order under this section may be made`

Kept JUST FALSE, with the text that closes the gate:
- `s 1098A the person is an authorised corporate service provider`: not named for a grant: a status definition ("means")
- `s 1111(3) the registrar may impose the requirement`: "must not be inconsistent" (a bar in the text's own words)
- `s 1110G(2) sections 1110E and 1110F authorise the disclosure`: "do not authorise" (a flat negative)
- `s 1110G(3) the registrar may disclose the information under section 1110F`: "may not be disclosed ... without authorisation" (a bar)
- `s 1110G(4) the recipient, or a person obtaining the information from the recipient, may disclose the information`: "must not be disclosed ... without authorisation" (a bar)
- `s 1112B(2) the Secretary of State may issue the certificate`: "only if satisfied" (closed by the text)
- `s 1110D(5) the regulations may provide for imprisonment of this term`: "may not provide for ... exceeding" (a bar)
- `s 1107(2)(a) the company may rely on the translation as against a third party`: "may not rely" (a flat negative)
- `s 1107(2)(b) the third party may rely on the translation`: "unless the company shows" (closed by the text)
- `s 1126(2)-(3) the proceedings may be brought`: "except by or with the consent of" (closed by the text)
- `s 1132(3)-(4) the order may contain the provision`: "except that no such order ... may be made" (closed by the text)
- `s 1132(5) the decision may be appealed`: "is not appealable" (a flat negative)
- `s 1132A(4) the regulations may provide for this maximum financial penalty`: "does not exceed £10,000" (a cap on the regulations)
- `s 1094(3) the registrar may exercise the power to remove the material`: "only if satisfied" (closed by the text)
- `s 1094(1) and (3) the registrar may remove the material from the register`: a composite; its JUST FALSE is the "only if" of subsection (3)
- `s 1096(3) the court may make an order for the removal of the material`: "only if satisfied" (closed by the text)
- `s 1097(5) the court may give a direction`: "shall not ... unless" (closed by the text)
- `s 1097(1)-(5) the court may give the direction on these facts`: a composite; its JUST FALSE is the "shall not ... unless" of subsection (5)

Listed, "may" with where/when/upon: none. Every function of the class that answered JUST FALSE had either a plain "if" gate (flipped), a gate the text closes, or no grant in its name (kept); the functions with a "where" or "on application" gate, such as `s 1094AB(1)`, already answered NOTHING.
Listed, "entitled": none. No function name of the eleven modules contains "entitled".

Assertions restated: 10 in the tests files (4 in `coa24-tests-acsp.l4`, 2 in `coa24-tests-delivery.l4`, 1 in `coa24-tests-identity.l4`, 3 in `coa24-tests-prosecution.l4`) and 5 in `coa24-cases-seat.l4`, each with `-- RECONCILED 2026-11-12: was <the original assertion>; <reason>` above it.
No other function of the eleven modules reads the four flipped functions; only `coa24-seat.l4` calls them (`s 1098B(1)` in the s 1098B(1) question, `s 1113(3)` in the second s 1113(3) question, `s 1132(2)` in the s 1132(2) question), and it returns their answer unchanged.

## Seat questions (coa24)

All 70 questions of `coa24-seat.l4` in the order of the text, each with the layer-1 rule it returns (generated from the file).

| # | question | returns |
| --- | --- | --- |
| 1 | Under section 1092C(1), is a statement I made in response to the registrar's requirement protected from use against me in criminal proceedings? | `s 1092C(1) the statement may not be used against the person in the criminal proceedings` |
| 2 | Under section 1093(1)(b), by what date must my company resolve the inconsistency the registrar has told it about? | `s 1093(1)(b) the last day of the period for resolving the inconsistency` |
| 3 | Under section 1093(3), has my company committed an offence by not resolving the inconsistency in time? | `s 1093(3)(a) the company commits an offence` |
| 4 | Under section 1093(3)(b), have I committed an offence as an officer of my company that did not resolve the inconsistency in time? | `s 1093(3)(b) the officer of the company commits an offence` |
| 5 | Under section 1093(4), what is the most I can be fined for the offence of not resolving the inconsistency? | `?` |
| 6 | Under section 1094, may the registrar remove this material from the register? | `s 1094(1) and (3) the registrar may remove the material from the register` |
| 7 | Under section 1094AB(1), may the court make consequential orders on my application now that the registrar has removed material from the register? | `s 1094AB(1) the court may make consequential orders on the application` |
| 8 | Under section 1096, must the registrar remove material from the register under a court order? | `s 1096 the registrar must remove the material from the register under a court order` |
| 9 | Under section 1097, may the court direct that its removal order, or a note about it, be kept from the public register? | `s 1097(1)-(5) the court may give the direction on these facts` |
| 10 | Under section 1098(1), must the registrar publish notice that an enhanced disclosure document has been removed from the register? | `s 1098(1) the registrar must cause notice of the removal to be published` |
| 11 | Under section 1098A, am I an authorised corporate service provider? | `s 1098A the person is an authorised corporate service provider` |
| 12 | Under section 1098B(1), may I apply to become an authorised corporate service provider? | `s 1098B(1) the person may apply to become an authorised corporate service provider` |
| 13 | Under section 1098B(4), must the registrar grant my application to become an authorised corporate service provider? | `s 1098B(4) the registrar must grant the application` |
| 14 | Under section 1098C(1), does my firm's application contain the required information about the firm? | `s 1098C(1) the application contains the required information about the firm` |
| 15 | Under section 1098C(2), does my application contain the required information about me as an individual? | `s 1098C(2) the application contains the required information about the individual` |
| 16 | Under section 1098D, is my firm's application delivered in the way the Act requires? | `s 1098D the application meets the delivery requirements of s 1098D` |
| 17 | Under section 1098E(1), by what date must I notify the registrar of the change in my supervisory authority? | `s 1098E(1)-(2) the last day for notifying the registrar of the change` |
| 18 | Under section 1098E(3), have I committed an offence by not notifying the registrar of the change in my supervisory authority in time? | `s 1098E(1)-(3) the person commits an offence by failing to notify the registrar in time` |
| 19 | Under section 1098E(4), as an officer of an authorised corporate service provider that is a firm, have I also committed the offence? | `s 1098E(4) the officer of the firm who is in default also commits the offence` |
| 20 | Under section 1098E(5), what is the most I can be fined on summary conviction for failing to notify the registrar of the change? | `s 1125(2) the most the person can be fined on this conviction, in pounds` |
| 21 | Under section 1098F(1), do I cease to be an authorised corporate service provider? | `s 1098F(1) the person ceases to be an authorised corporate service provider` |
| 22 | Under section 1099, must the registrar keep my body's name in the index of company names? | `s 1099(1) the registrar must keep the body's name in the index` |
| 23 | Under section 1100, may I inspect the registrar's index of company names? | `s 1100 the person may inspect the registrar's index of company names` |
| 24 | Under section 1103, must my document be drawn up and delivered in English? | `s 1103 the document must be drawn up and delivered in English` |
| 25 | Under section 1104(2), must my Welsh-language document be accompanied by a certified translation into English? | `s 1104(2) the document must be accompanied by a certified translation into English` |
| 26 | Under section 1105(1), may I deliver my document to the registrar in a language other than English? | `s 1105(1) the document may be drawn up and delivered in a language other than English` |
| 27 | Under section 1105(1), does my delivery in another language meet the requirement of a certified translation into English? | `s 1105(1) the delivery meets the requirement of s 1105(1)` |
| 28 | Under section 1106(1), may my company deliver a certified translation of a document it has already delivered? | `s 1106(1) the company may deliver certified translations of the document` |
| 29 | Under section 1107(2)(a), may my company rely on a certified translation against a third party where it differs from the original? | `s 1107(2)(a) the company may rely on the translation as against a third party` |
| 30 | Under section 1107(2)(b), may I, as a third party, rely on a certified translation that differs from the original? | `s 1107(2)(b) the third party may rely on the translation` |
| 31 | Under section 1108(1), do the names and addresses in my document use only permitted letters, characters and symbols? | `s 1108(1) the names and addresses meet the requirement of s 1108(1)` |
| 32 | Under section 1109(1), may my company deliver a transliteration of a name or address into Roman characters? | `s 1109(1) the company or other body may deliver a transliteration into Roman characters` |
| 33 | Under section 1110A(1), is my identity verified? | `s 1110A(1) the individual's identity is verified` |
| 34 | Under section 1110C(2), does the Secretary of State's notice relieve me of this identity-verification requirement? | `s 1110C(2) the effect applies in relation to the person` |
| 35 | Under section 1110E, may I disclose information to the registrar? | `s 1110E the person may disclose the information to the registrar` |
| 36 | Under section 1110G(1), does my disclosure to the registrar breach a duty of confidence or another restriction on disclosure? | `s 1110G(1) the disclosure breaches an obligation of confidence or any other restriction on the disclosure of information` |
| 37 | Under section 1110G(5), have I committed an offence by disclosing HMRC information? | `s 1110G(5) the person commits an offence` |
| 38 | Under section 1110G(6), do I have a defence to the offence of disclosing HMRC information? | `s 1110G(6) this section gives a defence` |
| 39 | Under section 1112(1), have I committed an offence by giving the registrar a false, misleading or deceptive document or statement? | `s 1112(1) the person commits the offence` |
| 40 | Under section 1112(2), as an officer of a firm that gave the registrar a false document or statement, have I also committed the offence? | `s 1112(2) the officer of the firm who is in default also commits the offence` |
| 41 | Under section 1112(3), what is the most I can be fined on summary conviction for giving the registrar a false statement? | `?` |
| 42 | Under section 1112A(1), have I committed the offence of knowingly giving the registrar a false, misleading or deceptive document or statement? | `s 1112A(1) the person commits the offence` |
| 43 | Under section 1112A(3), what is the longest I can be imprisoned, in months, for knowingly giving the registrar a false document or statement? | `?` |
| 44 | Under section 1112B(1), am I liable for a false-statement offence if the Secretary of State has issued me a certificate? | `s 1112B(1) the person is liable for the commission of the offence` |
| 45 | Under section 1113(2), may I, as a member or creditor, give my company notice requiring it to deliver a document it has failed to deliver? | `s 1113(2) the person may give notice to the company requiring it to comply with the obligation` |
| 46 | Under section 1113(3), by what date must my company make good its default after I served notice? | `s 1113(3) the last day for the company to make good the default` |
| 47 | Under section 1113(3), may I apply to the court for an order making my company file the document? | `s 1113(3) the person may apply to the court for an order` |
| 48 | Under section 1114(1)(b), does what I am doing count as delivering a document to the registrar? | `s 1114(1)(b) the act is delivering a document` |
| 49 | Under section 1119(2), is a document I delivered to the wrong address treated as delivered? | `s 1119(2) the document is treated as delivered` |
| 50 | Under section 1121, am I an officer in default? | `s 1121 the person is an officer in default` |
| 51 | Under section 1122(1), does my company commit an offence as an officer in default of another company? | `s 1122(1) the company commits an offence as an officer in default` |
| 52 | Under section 1123, am I treated as a director of this body for the purposes of the offence of an officer in default? | `s 1123 the person is read as a director for the purposes of section 1121(2)(a)` |
| 53 | Under section 1125(2), what is the most I can be fined on a second or later conviction for continuing the contravention? | `s 1125(2) the most the person can be fined on this conviction, in pounds` |
| 54 | Under section 1126, whose consent is needed before I can be prosecuted for this offence? | `s 1126(2)-(3) the consent required for the proceedings` |
| 55 | Under section 1126, may the proceedings against me be brought with the consent that has been given? | `s 1126(2)-(3) the proceedings may be brought` |
| 56 | Under section 1127(1), may summary proceedings for the offence be taken against me at this place? | `s 1127(1) summary proceedings for the offence may be taken at the place` |
| 57 | Under section 1128(1), is an information laid on this date within the time the section allows for it to be tried in a magistrates' court in England and Wales? | `s 1128(1) the information was laid in time` |
| 58 | Under section 1128(2), are summary proceedings in Scotland commenced on this date within the time the section allows? | `s 1128(2) the proceedings in Scotland were commenced in time` |
| 59 | Under section 1128(3), is a complaint made on this date within the time the section allows for a magistrates' court in Northern Ireland to hear it? | `s 1128(3) the complaint was made in time` |
| 60 | Under section 1129, must I disclose information I am entitled to refuse to disclose on grounds of legal professional privilege? | `s 1129 the Companies Acts require the person to disclose the information` |
| 61 | Under section 1130(1), may proceedings against my unincorporated body be brought in my name as one of its members? | `s 1130(1) the proceedings meet the requirement of s 1130(1)` |
| 62 | Under section 1130(3), may a fine imposed on my unincorporated body be taken from my own funds? | `s 1130(3) the fine is paid as the subsection requires` |
| 63 | Under section 1131(2), what term of imprisonment on summary conviction in England and Wales applies to an offence committed on this date? | `s 1131(2) the term shown in months` |
| 64 | Under section 1132(2), may a court order my company's documents to be inspected or produced? | `s 1132(2) an order under this section may be made` |
| 65 | Under section 1132(3), may the order require me, as secretary or an officer of the company, to produce its documents? | `s 1132(3)-(4) the order may contain the provision` |
| 66 | Under section 1132(5), may I appeal against the decision to make an order for inspection or production of documents? | `s 1132(5) the decision may be appealed` |
| 67 | Under section 1132A(2), is this offence one for which the registrar could be given power to impose a financial penalty? | `s 1132A(2) the offence is a relevant offence under this Act` |
| 68 | Under section 1132A(4), may regulations giving the registrar power to impose a financial penalty provide for a maximum penalty of this amount? | `s 1132A(4) the regulations may provide for this maximum financial penalty` |
| 69 | Under section 1132A(5), must the regulations provide that no proceedings may be brought against me for conduct for which I have been given a financial penalty? | `s 1132A(5)(b) the regulations must provide that no proceedings may be brought against the person` |
| 70 | Under section 1133, do the provisions of Part 36 apply to an offence I committed before they came into force? | `s 1133 the provision of Part 36 applies to the offence` |

### Seat audit of 2026-11-12

The lead asked every part to read each seat question's name and `@export` text against the layer-1 function its body returns, because a question can ask one thing while its function answers another (a direction mismatch: a permission asked, a bar returned, so JUST TRUE is misread; or a subject mismatch: "may I ask" against "may the court make", "can ... still be laid" against "was laid in time").
Result for coa24: 70 questions read, 6 mismatched (1 direction, 5 subject).
Nothing was fixed by negating an answer; each question was retitled to ask what the function answers, with its `@export` text, its DECIDE name and the affected input `@desc`s, and the form "Under section N," kept.

| question (section) | kind | was | now | why |
| --- | --- | --- | --- | --- |
| s 1094AB(1) | subject | Under section 1094AB(1), may I ask the court for consequential orders now that the registrar has removed material from the register? | Under section 1094AB(1), may the court make consequential orders on my application now that the registrar has removed material from the register? | the function is `s 1094AB(1) the court may make consequential orders on the application`; whether I may ask is a different question from whether the court may make the orders |
| s 1128(1) | subject | Under section 1128(1), can the information still be laid against me in a magistrates' court in England and Wales? | Under section 1128(1), is an information laid on this date within the time the section allows for it to be tried in a magistrates' court in England and Wales? | the function is `s 1128(1) the information was laid in time`; it tests a stated date and does not say whether an information can still be laid |
| s 1128(2) | subject | Under section 1128(2), can summary proceedings against me still be commenced in Scotland? | Under section 1128(2), are summary proceedings in Scotland commenced on this date within the time the section allows? | the function is `s 1128(2) the proceedings in Scotland were commenced in time` |
| s 1128(3) | subject | Under section 1128(3), can a complaint against me still be made in a magistrates' court in Northern Ireland? | Under section 1128(3), is a complaint made on this date within the time the section allows for a magistrates' court in Northern Ireland to hear it? | the function is `s 1128(3) the complaint was made in time` |
| s 1132A(4) | subject | Under section 1132A(4), may the registrar's financial penalty be as much as this amount? | Under section 1132A(4), may regulations giving the registrar power to impose a financial penalty provide for a maximum penalty of this amount? | the function is `s 1132A(4) the regulations may provide for this maximum financial penalty`; it limits what regulations may provide and says nothing about a penalty the registrar imposes |
| s 1132A(5) | direction | Under section 1132A(5), if I have been given a financial penalty for conduct, can I still be prosecuted for that conduct? | Under section 1132A(5), must the regulations provide that no proceedings may be brought against me for conduct for which I have been given a financial penalty? | the function is `s 1132A(5)(b) the regulations must provide that no proceedings may be brought against the person`; its JUST TRUE is a bar, so under the old title it read as "yes, I can be prosecuted", the opposite of the text |

Seventeen assertions in `coa24-cases-seat.l4` called these questions by their old names; each is restated in place with a `-- RECONCILED 2026-11-12: was <the original assertion>; <reason>` comment above it. The facts and the expected values did not change.
The expected values were not re-derived from the code: a case that was JUST TRUE under the old title is JUST TRUE under the new one because the function is the same.

Questions read and left alone, where the title and the function use different words but ask the same thing, so JUST TRUE, JUST FALSE and NOTHING mean what the title says:
- Flat negatives, where the function is written in the positive and JUST FALSE is the text's "no": s 1107(2)(a) ("may my company rely"), s 1110G(1) ("does my disclosure breach"), s 1112B(1) ("am I liable"), s 1119(2) ("is it treated as delivered"), s 1129 ("must I disclose"), s 1130(1) and (3) ("may ... be brought in my name", "may ... be taken from my own funds": the function is a compliance test fed the forbidden name or fund, so it can only answer JUST FALSE or NOTHING), s 1132(5) ("may I appeal"), s 1133 ("do the provisions apply").
- s 1092C(1): the function is a bar ("may not be used against the person") and the title asks whether the statement is protected, so JUST TRUE is "yes, protected".

## Seams (coa24)

Format: the input as named in the code, the section that answers it, the type, and where it is asked. `PLAN.md` section 4 gives the naming rule (the plan has no section 8; see the head of this file). Every input below is `MAYBE BOOLEAN` unless stated, so that NOTHING passes through.

### Inputs this part takes from another part

| input (as named in the code) | answering section (part) | type | asked in |
| --- | --- | --- | --- |
| `s 1074 it appears to the registrar to be unnecessary material as defined by section 1074` | s 1074 (coa23) | MAYBE BOOLEAN | `s 1094(1)`, `s 1094(1) and (3)` |
| `s 1078 the material removed is an enhanced disclosure document, or material derived from such a document` | s 1078 (coa23) | MAYBE BOOLEAN | `s 1098(1)` |
| `s 790C the person is a registrable person or registrable relevant legal entity in relation to a company` | s 790C (coa17) | MAYBE BOOLEAN | `s 1097B(2) the person is a relevant person` |
| `s 790C the person is a registrable relevant legal entity in relation to a company`, `s 790C(12) the person is a registrable person in relation to a company who falls within section 790C(12)` | s 790C, s 790C(12) (coa17) | MAYBE BOOLEAN each | `s 1097C(2) the person is a relevant person` |
| `s 88 the company is a Welsh company` | s 88 (coa2) | MAYBE BOOLEAN | `s 1104(1)`, `s 1104(4)`, `s 1104(5)` |
| `s 1110A the individual's identity is verified` | s 1110A (this part: `s 1110A(1) the individual's identity is verified`) | MAYBE BOOLEAN | `s 1098B(1)`; the seat asks the fact plainly and does not wire the two modules |
| `the offence was committed by` (a core `Kind of person`) with the keel's `s 1173(1) the entity is a firm` | s 1173(1) (keel) | imported and called, not an input | `s 1098E(4)`, `s 1112(2)`, `s 1112A(2)` |

### Answers this part gives to other parts

| the plan's seam | the function that answers it | note |
| --- | --- | --- |
| `s 1121 the officer is in default` | `s 1121(3) the officer is in default` (limb (3)) and `s 1121 the person is an officer in default` (both limbs) | MAYBE BOOLEAN; a record `s 1121(3) conduct of the officer` carries the three limbs |
| `s 1110A the individual's identity is verified` | `s 1110A(1) the individual's identity is verified` | MAYBE BOOLEAN |
| `s 1125` (daily default fine; the core `Penalty`) | `s 1125(2) the fine limit that applies on this conviction`, `s 1125(2) the most the person can be fined on this conviction, in pounds`, `s 1125(1) the fine limit in pounds` | the pounds are inputs (`s 1125 amounts the Act leaves to other instruments`) |
| `s 1128 the information was laid in time` | `s 1128(1) the information was laid in time` (England and Wales), `s 1128(2) the proceedings in Scotland were commenced in time`, `s 1128(3) the complaint was made in time` | MAYBE BOOLEAN; the date evidence came to a prosecutor's knowledge is an input, MAYBE DATE |
| authorised corporate service provider (Schedule 8: s 1098A) | `s 1098A the person is an authorised corporate service provider` | MAYBE BOOLEAN |
| document in Part 35 (s 1114(1)) | `s 1114(1)(a) the thing is a document in Part 35` | MAYBE BOOLEAN |
| registrar's index of company names (s 1099) | `s 1099(1) the index is the registrar's index of company names`, `s 1099(2)-(3) the section applies to the body` | MAYBE BOOLEAN |
| registrar's rules (s 1117) | `s 1117(3)(a)`, `s 1117(3)(b)` (the duties); ss 1117(1)-(2), the rule-making power, are inert | the label "registrar's rules" has no definition sentence of its own in s 1117 |

### Seams the plan lacks, found in this range

Cross-references that this part carries as constructors, strings or inputs and does not encode: s 1043 (unregistered companies, in `s 1099(2)(b)`), s 1046 (overseas companies' particulars, in `s 1099(2)(c)`), s 1068 (in `s 1111(2)`), s 1073 and s 1074 (in `s 1094`), s 1080 (in `s 1093`), s 859M and Part 15 (in `s 1096`), ss 12(2A), 167G(3)(c), 167M, 167N(1), 1067A and 1098B(2)(c) (in `s 1110C(2)`, named as strings), Chapter 3 of Part 3, ss 400(2)(e) and 401(2)(f) and Part 25 (in `s 1105(2)`), s 86(2), s 87, s 1141 and ss 167H, 279H and 790LD (only in the regulation-making powers of ss 1097A to 1097C, which are inert).
The Money Laundering Regulations 2017, the Data Protection Act 2018 and the Commissioners for Revenue and Customs Act 2005 are named by string only; they are not among the sources.

## Findings: what the text turns out to say

1. **The rendering runs two versions of a sentence together in s 1093(4).** Line 15505 reads "a daily default fine not exceeding one-tenth of level 5 on the standard scaleone-tenth of the greater of £5,000 or level 4 on the standard scale". The converter's own caveat ("may carry more than one extent version of a provision") is the likely cause. The text does not say which applies, so both are encoded (fork F1) and the function can answer NOTHING. The core `Fine limit` has no "one-tenth of the greater of £5,000 or level 4" constructor (`NEEDS-CORE.md`).
2. **s 1099(3) has two paragraphs lettered (f).** Lines 15791 and 15792: the protected cell companies of the Risk Transformation Regulations 2017, and charitable incorporated organisations. Paragraph (e) ends in a full stop and not a semicolon. Both bodies are encoded (fork F2).
3. **s 1126's list has no "or" and some subsections carry the omission mark "..." mid-line** (lines 16103 and 16111, "(ii) section 953 of this Act, ..."; lines 16107 and 16115, "section 798 of , or paragraph 5 or 6"). The consents are the same in the list (1) and in (2) and (3): the Secretary of State or the Director of Public Prosecutions (the Director of Public Prosecutions for Northern Ireland in Northern Ireland) for ss 458, 460, 949, 953, the 1985 Act's ss 448-453A and ss 1112 and 1112A; the Secretary of State alone for s 798, s 455 of the 1985 Act and paragraphs 5 and 6 of Schedule 1B. Scotland is not mentioned in (2) or (3).
4. **The offence in s 1112 carries no imprisonment and no daily default fine; s 1112A carries imprisonment.** s 1112(3): England and Wales "a fine" (no stated limit), Scotland and Northern Ireland a fine not exceeding level 5. s 1112A(3): on indictment two years or a fine (or both); on summary conviction a term "not exceeding the general limit in a magistrates’ court" or a fine (England and Wales), 12 months or a fine not exceeding the statutory maximum (Scotland), 6 months or a fine not exceeding the statutory maximum (Northern Ireland).
5. **The summary-conviction penalties are not the same in the three places.** In s 1098E(5) and s 1098G(5) England and Wales has "a fine" and Scotland and Northern Ireland have a fine not exceeding level 5 and a daily default fine not exceeding one-tenth of level 5: the daily default fine is a feature of the Scottish and Northern Irish limbs only. In s 1110B(4)(b)(ii) and (iii) the daily default fine is one-fifth of the statutory maximum.
6. **The "general limit in a magistrates' court" is not a number in the Act.** s 1131(2) substitutes "six months" for an offence committed before 2 May 2022; for an offence on or after that day the number is outside the sources. The test boundary is 1 May 2022 (six months) against 2 May 2022 (the input).
7. **s 1128 counts three different ways and borrows a fourth.** England and Wales: an information laid within three years after the offence and within twelve months after the Director of Public Prosecutions or the Secretary of State had sufficient evidence ("and" joins the two limbs). Scotland: never after three years from the offence; within that, within twelve months of the Lord Advocate's knowledge, or, where the Secretary of State reported the evidence, within twelve months of the Secretary of State's knowledge; the date proceedings are "deemed to be commenced" comes from s 136(3) of the Criminal Procedure (Scotland) Act 1995, which is not in the sources. Northern Ireland: a complaint within three years and twelve months as in England and Wales. s 1128(4) makes a certificate conclusive of the date.
8. **s 1121(2) "officer" "includes" and the keel's s 1173(1) "officer" "includes" overlap** (a director, manager or secretary appear in both). Neither closes the list, so a person outside both is NOTHING, not JUST FALSE. The two are separate functions: `s 1121(2)` takes the person's position as an input.
9. **s 1096(5) names no one to send the copy of the order** ("A copy of the court's order must be sent to the registrar for registration", fork F15). s 1122(2) says "the officer in question" without saying who that is (F16).
10. **Part 35's second half is mostly regulation-making machinery.** 198 of the 713 coverage rows are inert (reason 2): the Secretary of State's powers to make regulations on removal of material (s 1094A), on the registered office, service address and principal office (ss 1097A to 1097C), on authorised corporate service providers (ss 1098B to 1098H), on language and transliteration, on identity verification and discrepancy reporting (ss 1110B, 1110D), and on financial penalties (s 1132A). What the Act itself lays down for those regulations is encoded: the penalties they may or must provide (ss 1097A(4A), 1097B(6), 1097C(6), 1098G(5), 1110B(4)), the ceilings (s 1097A(5)(a) 28 days, s 1110D(5) 2 years on indictment and 3 months on summary conviction, s 1132A(4) £10,000), what the court must do on an appeal (ss 1097A(7), 1097B(9), 1097C(9)) and the double-jeopardy bars (s 1132A(5)).
11. **The three "14 days" periods count differently.** ss 1093(1)(b) and 1098E(1) say "the period of 14 days beginning with the date on which" something happens, so the day itself is the first and the last day is 13 days later (tests: issue on 1 March 2026, last day 14 March; delivery on 14 March is in time, on 15 March is late). s 1113(3) says "within 14 days after service", so the day of service is not counted and the last day is 14 days later (service on 1 March 2026, last day 15 March). The traces use `WITHIN 13` for the first two and `WITHIN 14` for the third.
12. **A test caught a precedence trap.** In `s 1098A` the first draft read `granted AND NOT ceased AND NOT suspended`; on this binary `NOT` binds over everything to its right, so it read `granted AND NOT (ceased AND NOT suspended)`, and two assertions failed (a provider whose status is suspended came out JUST TRUE). `s 1098B(2)` had the same trap with `NOT individual OR statement`, and one more assertion failed. Every `NOT` that sits in a conjunction is now bracketed. This is the silent failure the brief names, caught here by a boundary test that was written from the text before the run.
13. **s 1110C(3) and s 1112B(4) say the same thing twice**, with separate definitions of "crime" and "serious"; they are encoded as separate functions with the same content and tests.
14. **s 1103's "subject to" does not mean the exceptions always apply.** For an ordinary company's ordinary document neither s 1104(1) nor s 1105(1) grants anything (both answer NOTHING), and the general rule stands (F12).
15. **s 1116(6) is two rules.** The first sentence says nothing in the section prevents notice both in the Gazette and by approved means; the second says the requirement of public notice "is met when notice is first given by either means": encoded as a flat negative and as the earlier of the two dates.
16. **The Part 36 offence sections that this part answers for are definitions only.** ss 1121 to 1123 create no offence themselves; every "officer in default" offence elsewhere in the Act takes the answer of `s 1121 the person is an officer in default`. 

## What the stable binary does not accept (and what it accepts that the brief forbids)

Loud (the binary errors, so it is found at once):
- `length` is not a prelude name: a list length is `count` (an unknown-identifier error).
- A `CONSIDER ... WHEN ...` written on one line inside parentheses as an argument does not parse ("unexpected ("): write the `CONSIDER` on its own lines.
- A `#TRACE` cannot be an operand of `#ASSERT` ("unexpected #TRACE"); and a `DEONTIC` value cannot be compared with `EQUALS` (`drafting-patterns.md`). So the three regulative rules (ss 1093(3), 1098E(1), 1113(3)) are run with `#TRACE` and their outcomes are read from the run (below), and the same duties are encoded as decision functions that are asserted: `s 1093(3)(a)`, `s 1098E(1)-(3)` and `s 1113(3)`.

Silent (exit 0, wrong answer):
- `a AND NOT b AND NOT c` reads `a AND NOT (b AND NOT c)` (finding 12): bracket every `NOT`.
- `check.sh` compares four counts only; it does not see a `#TRACE` outcome. The nine traces were run on both builds and printed the same: on time on the last day, FULFILLED; one day late, `DEONTIC BREACHED`; never done, `DEONTIC BREACHED` (`work/traces.sh`; the dates are in each tests file).

Accepted although the brief forbids it: the two supplied builds (1.6.109 and 1.6.110) check and run `REFUSE`, `#ASSERT REFUSED` and `YMD` (`PLAN.md` section 5). None of them is used here: "not covered" is `NOTHING` or a constructor, and dates are `Date day month year`.
`add years` and `add months` (daydate) are used in s 1128 and are in both builds; they clamp the day of the month (fork F6).
`IMPORT` of a module that itself imports `coa-definitions`, alongside another that does the same, works on 1.6.110 (measured by a scratch probe).
Constructs used and found acceptable on both builds: enum, record and `MAYBE` inputs to `@export` functions; `LIST OF STRING` as a vertical `LIST` block; a record built with `WITH`; a `WHERE` block under a `DECIDE`; `@ref` before `@export`.

## Rulings applied (coa24)

Copied word for word from the brief (the rules of 2026-10-29 and the rulings of 2026-11-04 and 2026-11-05 govern every row carrying a `NOTHING-kind` tag here). Where this encoding applied a ruling, the function and the site are in the fork register and in `## Marginal readings for a lawyer (coa24)`.

### Rulings on negatives and legal effects (ruled 2026-11-04), as the brief gives them

These rulings set this corpus's drafting conventions, which each row follows and flags; L4 itself takes no position on them.
The rule of 2026-10-29 for what `JUST FALSE` and `NOTHING` mean is the convention the rows written since then follow (applied in legalese/commons#30 and #37); it was assumed, not ruled as a whole, and the rulings below settle parts of it.
In short, a function answers `JUST FALSE` only where the text itself says no to the case in its own words: a "means" definition, a condition the text introduces with "if", "only if", "as long as" or "unless" (and plain variants such as "while", "until" and "except"), a list the text closes with "only", a flat negative ("does not", "shall not", "may not").
Everywhere else it answers `NOTHING`: where the text lists without closing the list, says "includes", leaves a term undefined, is silent, points outside the sources, or limits a grant or prohibition in its own wording and the case falls outside the limit.
The wording is copied from section 2 of `docs/design-question-false-or-nothing.md`, which also states the two readings left open for a lawyer.
Each ruling is recorded again, word for word, in the `NOTES.md` of each row that carries that rule's `NOTHING-kind` tags: in its fork register where it has one, and in a section of its own where it has none.

- **E1** (bench `commons-negation-1030`; should a legal effect be one definition gathered from every section that gives it?): option B, as guidance for gathering a legal effect's routes by hand only, with no pilot run; option A (gathering by bare name) is withdrawn as a direction for the language, not deferred; option C (per-section answers) applies everywhere else; the Magna Carta pilot in the printed recommendation (chapters 2, 3, 4, 5, 37, 43, 46 and 53, with a blind second reader) is not to be run. The maintainer's lean, verbatim: "B but generally uncomfortable with this much magic because it takes the language from unopinionated to opinionated in ways that are hard to teach an l4 novice." the maintainer's note, verbatim: "Fundamentally I feel like we are trying to make the language do work that the human l4 drafter should do. Too much magic. Can’t we just decline to be this opinionated and say the programmer needs to do this thinking?" Marked 2026-11-03T23:19:02.812Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
- **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. The maintainer's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." the maintainer's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
- **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. The maintainer's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.
- **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. The maintainer approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.
- **Questions with no convention: decide case by case (the maintainer, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. The maintainer's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with the coordinator where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.
- **Lists:** write a list of strings as a vertical `LIST` block, one string per line, not with `•` bullets (those are a parse error on the stable binary).

The rule of 2026-10-29 (assumed, not ruled by a lawyer), as the brief gives it:

This rule is in force for every row the family has filed since 2026-10-29. Follow it exactly, and flag, do not decide, the two readings marked "for a lawyer".
- A decision function answers `JUST FALSE` (a `BOOLEAN` that is `MAYBE`-wrapped), or a constructor whose meaning is "the text says no" (for example `s 39 not entitled`, `s 39 not barred`, `s 39 not obliged`: **every constructor and type you declare begins with the section label, like every function**, so that no two parts declare the same name; the merged seat layer imports all the parts at once, and a name defined in two modules cannot be used at all), **only** where the text itself says no to the case in its own words: a definition that says "means"; a condition the text introduces with "if", "only if", "as long as" or "unless" (and their plain variants: "so long as", "while", "until", "except", "save", "provided that"); a list the text closes with "only" or "nothing but"; a flat negative ("does not", "shall not", "may not", "is not entitled").
- Everywhere else the function answers `NOTHING` (a `MAYBE` result) or a named "... not covered" constructor: where the text lists without closing the list, says "includes", leaves a term undefined, is silent, points to a power, regulation, rate or authority outside your sources, or limits a grant or prohibition in its own wording ("without", "against the will of", "when", a stated period, a named complement) and the case falls outside the limit.
- Every branch that answers a "no" carries a comment `-- FALSE-kind (the text says no in its own words): "<the quoted words>"`, and every branch that answers "not covered" carries `-- NOTHING-kind (<why>)` where <why> is one of: silent, list not closed, includes, undefined term, points outside the text, limited by its own wording.
- The function's name carries the section it implements, in this form: `s 47(2) the instrument is valid`, `s 4(2)(a) the claimant has reached the qualifying age`, `sch 3 para 2 the amount is reduced` (the Act's own numbering; parentheses inside a backtick name are fine on the stable binary, checked). Not `is the instrument valid`, not `may I ...`: the name must not claim more than the section says. A caller must never turn `NOTHING` into `FALSE`.
- **For a lawyer, not for you to decide:** (a) a failed "if" counts as the text's no, clause by clause, within the provision that holds the "if" (an inference: "if A then B" does not itself say "if not A then not B"), and flat negatives count as the text saying no; (b) a prohibition or grant limited by its own wording does not. Take these readings as the status quo, and list every branch that rests on one under a heading `## Marginal readings for a lawyer` in `NOTES.md`, with the other reading stated.
- Put a short section `### Reading a result: FALSE and NOTHING` in `NOTES.md` saying this in your own subject's terms: what a "no" is in this row, and what "not covered" is.
- `REFUSE` does not exist on the stable binary: "not covered" is `NOTHING` or a constructor, asserted.

## What `check.sh` prints

Command: `L4=<l4-main-110> L4_MAIN=<l4-main-109> ./check.sh` (target main). Output, verbatim:

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.109 (main, 4c887e0, 2026-11-04)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
coa-core.l4                                    0         0       0        0         0 |      0         0       0        0  same
coa-definitions.l4                             0         0       0        0         0 |      0         0       0        0  same
coa24-acsp.l4                                  0         0       0        0         0 |      0         0       0        0  same
coa24-cases-seat.l4                            0       186       0        0         0 |      0       186       0        0  same
coa24-delivery.l4                              0         0       0        0         0 |      0         0       0        0  same
coa24-disclosure.l4                            0         0       0        0         0 |      0         0       0        0  same
coa24-false-statements.l4                      0         0       0        0         0 |      0         0       0        0  same
coa24-identity.l4                              0         0       0        0         0 |      0         0       0        0  same
coa24-index.l4                                 0         0       0        0         0 |      0         0       0        0  same
coa24-language.l4                              0         0       0        0         0 |      0         0       0        0  same
coa24-officers.l4                              0         0       0        0         0 |      0         0       0        0  same
coa24-penalty.l4                               0         0       0        0         0 |      0         0       0        0  same
coa24-prosecution.l4                           0         0       0        0         0 |      0         0       0        0  same
coa24-register.l4                              0         0       0        0         0 |      0         0       0        0  same
coa24-seat.l4                                  0         0       0        0         0 |      0         0       0        0  same
coa24-tests-acsp.l4                            0       119       0        0         0 |      0       119       0        0  same
coa24-tests-delivery.l4                        0        76       0        0         0 |      0        76       0        0  same
coa24-tests-disclosure.l4                      0        35       0        0         0 |      0        35       0        0  same
coa24-tests-false-statements.l4                0        47       0        0         0 |      0        47       0        0  same
coa24-tests-identity.l4                        0        63       0        0         0 |      0        63       0        0  same
coa24-tests-index.l4                           0        23       0        0         0 |      0        23       0        0  same
coa24-tests-language.l4                        0        88       0        0         0 |      0        88       0        0  same
coa24-tests-officers.l4                        0        50       0        0         0 |      0        50       0        0  same
coa24-tests-penalty.l4                         0        33       0        0         0 |      0        33       0        0  same
coa24-tests-prosecution.l4                     0       129       0        0         0 |      0       129       0        0  same
coa24-tests-register.l4                        0       152       0        0         0 |      0       152       0        0  same
TOTAL (26 modules)                             0      1001       0        0           |      0      1001       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

The baseline it replaced: with only the keel's two modules (`coa-core.l4`, `coa-definitions.l4`) in the folder, `check.sh` printed 2 modules, 0 errors and 0 assertions on both builds (the keel's own tests file is not in this folder). Every assertion of this part is new: the tests files and the seat cases total the assertions shown above, written equal to satisfied, with 0 expected failures (`expected_failed` is unchanged, and `coa24` has no file that is meant to fail).

Other checks (commands run from the folder, outputs as printed):

- `python3 -I srcrefs.py check --refs ../../../inputs/ukpga-2006-46.txt coa24-*.l4` and with `--strict`:

```
srcrefs check: 456 src: lines, 167 runs, 209 locators, 0 problems
srcrefs check: 456 src: lines, 167 runs, 209 locators, 0 problems
```

- `work/checkquotes.py` (every quoted piece of every `-- FALSE-kind` and `-- NOTHING-kind` comment occurs in the text; every NOTHING reason is one of the six):

```
FALSE/NOTHING comments: 319 (FALSE 125, NOTHING 194); quoted pieces not in the range: 0
```

- `work/traces.sh` on the three tests files that hold a `#TRACE` (read on both builds):

```
== coa24-tests-register.l4 : trace/eval results on main-110
Evaluation[41] @ coa24-tests-register.l4:118:1-119:106
  FULFILLED
Evaluation[42] @ coa24-tests-register.l4:121:1-122:106
  DEONTIC BREACHED:
Evaluation[43] @ coa24-tests-register.l4:124:1-125:19
  DEONTIC BREACHED:
   (main-109 prints the same)
== coa24-tests-acsp.l4 : trace/eval results on main-110
Evaluation[111] @ coa24-tests-acsp.l4:225:1-226:149
  FULFILLED
Evaluation[112] @ coa24-tests-acsp.l4:228:1-229:149
  DEONTIC BREACHED:
Evaluation[113] @ coa24-tests-acsp.l4:231:1-232:19
  DEONTIC BREACHED:
   (main-109 prints the same)
== coa24-tests-delivery.l4 : trace/eval results on main-110
Evaluation[26] @ coa24-tests-delivery.l4:51:1-52:79
  FULFILLED
Evaluation[27] @ coa24-tests-delivery.l4:54:1-55:79
  DEONTIC BREACHED:
Evaluation[28] @ coa24-tests-delivery.l4:57:1-58:19
  DEONTIC BREACHED:
   (main-109 prints the same)
```

## What the text does not answer, and what to do before relying on this

- The amounts: the pounds of levels 1 to 5 on the standard scale and of the statutory maximum, and the "general limit in a magistrates' court" are not in the Act; the seat asks the person for them and returns NOTHING for a limit with no stated amount (England and Wales "a fine").
- The regulations: nothing made under ss 1094A, 1097A-1097C, 1098B-1098H, 1102, 1105, 1106, 1108, 1110A-1110D, 1116 or 1132A is in the sources, so which documents are excepted from translation, which characters are permitted in names, what further conditions apply to an authorised corporate service provider, and whether the registrar has a power to impose a financial penalty, are inputs or NOTHING.
- The borrowed instruments: the Money Laundering Regulations 2017, the Data Protection Act 2018, the Commissioners for Revenue and Customs Act 2005, the Criminal Procedure (Scotland) Act 1995 s 136(3), the Welsh Language Act 1993 and the Deregulation and Contracting Out Act 1994 are named, not encoded.
- Who bears a duty the text states in the passive: s 1096(5) (F15), and which officer "the officer in question" is in s 1122(2) (F16).
- Which version of the daily default fine applies in s 1093(4) (F1).
- Before this is worth relying on: a lawyer should read the two sections of marginal readings, the fork register's F1 and F3, and the 50 rows marked `fork` in the coverage table; the independent test pass of the encoding skill (step 8) has not been done.
