# NOTES: Companies Act 2006 (United Kingdom), part agent coa23: Part 34 (Overseas companies) and Part 35 (The registrar of companies) to section 1092B, lines 14666-15484

Written by part agent coa23 (Claude Sonnet 5.5), 2026-11-13. Status (verified by `check.sh` below on 2026-11-13): the 11 coa23 modules and the keel's two compile on the stable binary 1.6.110 (main, e51181d, 2026-11-11) and on 1.6.109 with no `DiagnosticSeverity_Error` or `_Warning`; 1142 assertions are satisfied and none fails or is refused; no row of the coverage table is left `deferred`. Not reviewed by a lawyer. The target is the stable `l4` (`main`); no construct the stable binary rejects is used.

## Source and what "verified" means here

The only source is `ukpga-2006-46.txt`, a plain-text rendering of the Act and its Schedules from legislation.gov.uk (Open Government Licence v3.0) made by a converter script; it is not the official text, and nothing here is "verified against the official text". It is the revised text of the version stated as 2026-07-16 in `inputs/ukpga-2006-46.meta.json`, which "may carry more than one extent version of a provision, and prospective provisions, which CLML marks but this text does not distinguish": findings 2, 3 and 14 are places where that shows. Every `-- src:` quote line in the coa23 modules was written by a script that calls `srcrefs.py quote` on that file (the L4 files are generated from templates by a script that reads the text, never retyped), and the gates below report 0 problems. Line numbers are of the file as it is. The licence note is `inputs/STUB-SOURCE-LICENSE.md` (the lead writes `SOURCE-LICENSE.md`, `encoding.json`, `subject.json` and `README.md`).

## Seat (coa23)

The seat is the one the brief gives: an individual who is, or is about to become, a director, a company secretary or a member (shareholder) of a company registered under the Act, or who deals with one, asking on facts they can state what the Act requires or lets them do, what rights they have against the company or its directors, what they must disclose, file, approve or vote on and by when, and what follows (liability, offences, penalties) if it is not done. (Assumed, not ruled: the Act is addressed to companies, so the individual is whoever stands in a company's management or ownership.) There is no seat for the registrar or the Secretary of State: the provisions that address only them reach the seat only for what they mean to the person.

`coa23-seat.l4` holds 52 questions, each `@export` with a question that begins "Under section N," and each input with an `@desc` worded as the person would be asked. The questions are grouped under `§` headings in the text's order: "Part 34 - Overseas companies" (ss 1044 to 1059; only for a person whose company is incorporated outside the United Kingdom), "Part 35 - The registrar of companies" (ss 1060 to 1066), "Delivering documents to the registrar" (ss 1067A to 1076; only for a person who is delivering or has delivered a document) and "Public notice and the register" (ss 1077 to 1092B; parts of it arise only for a new director, a dissolved company, or a person asked for information). `coa23-cases-seat.l4` holds 165 assertions: at least one case in a person's own facts for every question, written from the text before the layer was run, and a "not covered" answer (NOTHING) asserted where the question has one.

Choices the person makes from a list are strings (the three parts of the United Kingdom; the kind of certificate, event or document; the paragraph of section 1087(1); the subsection and item of section 1078); a string that matches no choice answers NOTHING. Figures the Act leaves elsewhere are inputs: the general limit in a magistrates' court (ss 1092B(3)), and the fee and cost in s 1086(2). No figure is taken from memory.

Questions the layer does not ask, with the reason: sections whose answer the person never needs on facts they can state (the registrar's rule-making and the Secretary of State's regulations: inert), the registrar's own duties that have no effect on the person beyond what the questions above already give (ss 1061, 1062, 1062A, 1063(5), (6), 1066(1) to (3), 1067(1) to (3), 1068, 1073(2), 1073A(2), (3), 1076(1), (3), (4), 1077(2), (3), 1079B(1), (3), (4), 1080, 1081, 1081A, 1082, 1084(1) to (4), 1087(2), (3), 1087A(1), (4), (5), 1087B, 1088, 1089, 1090, 1091(3), (5), 1092(2), 1092A): each is a layer-1 function with tests and can be given a question on request.

**Audit of the direction of every question (repair of 2026-11-13).** Each of the 52 questions was compared with the layer-1 function its body calls, for direction ("may" or "can" against "barred" or "prevented", or the reverse) and for subject ("must I" against "have I"). Five were found and fixed (fork F27): s 1079(1) and s 1079(3) asked "can the company rely ..." and returned the bar, so they now ask "is the company barred from relying ..."; s 1070(3) asked "must my company deliver ... and has it done so" and returned the compliance answer, so it now asks "has my company delivered this document as its agreement with the registrar requires"; s 1084(1A) asked "may the registrar stop making ... available" and returned "need not make ... available", so it now asks whether the registrar is "no longer required to make" them; and s 1087A(3) asked whether the information is "protected as" relevant date of birth information and returned whether it is relevant date of birth information (the protection is s 1087A(1)), so it now asks the second. The other 47 questions name what their function answers.

## What is encoded and what is not

Encoded: every provision of lines 14666 to 15484: Part 34 (ss 1044 to 1059) and Part 35 from s 1059A to s 1092B (the sections of "the registrar" up to the power to require information and the offence of not giving it). Layer 1 is five modules (`coa23-nouns.l4`, `coa23-part34.l4`, `coa23-part35-registrar.l4`, `coa23-part35-delivery.l4`, `coa23-part35-register.l4`), four test files, and the seat layer (`coa23-seat.l4`, `coa23-cases-seat.l4`). Not covered by design: the regulations and registrar's rules that Part 34 and Part 35 empower (they are outside the sources; their mandatory limits are encoded: fork F1); the sections other parts own (Part 5 names, Part 10 addresses, ss 1093 to 1119 and the rest), which appear only as inputs (the Seams section). Amounts, levels and periods the Act leaves elsewhere are inputs, never a number from memory.

## Coverage (coa23)

Every unit of the range has a row and each row has exactly one disposition: `encoded`, `inert` (reason 1 not operative: headings and signposts; reason 2 machinery: powers to make regulations or registrar's rules, their procedure, an amendment of another Act, a transitional provision; reason 3 text shown repealed or blank), `fork` (the row points at its fork-register entry and at the rule that encodes the chosen reading), or `repealed or blank in this text`. There is no `out-of-scope` row and no `deferred` row. "Tests" counts the `#ASSERT` and `#TRACE` lines of the `coa23-tests-*` files that call the function(s) of the row (a line that calls two functions counts once for each, and a table row that shares one function with its list shows that function's count).

**Summary of dispositions.** 802 rows: encoded 492 (462 text units and 30 defined-term rows added at the end of the table), inert 274 (reason 1: 79; reason 2: 195; reason 3: 0), fork 18, repealed or blank in this text 18. The reason-3 count is 0 because text shown repealed or blank has its own disposition (`repealed or blank in this text`) in this table.

**Audit.** The script `work/units.py` read lines 14666 to 15484 of the text: 819 lines, none blank; every one of the 819 falls in a row (`lines not in a unit: 0`). Text units counted (sections, subsections, paragraphs, sub-paragraphs, table rows, list rows, cross-headings and Part headings): 716 on the first pass; the audit then added 56 rows for lines of lists that the first pass had left inside their subsection (the s 1059A lists, the lines of s 1072(1)(b), s 1081A's four objectives, s 1087(1)(gd), the Parts cited in ss 1049(2) and 1050(4), the Acts of s 1063(3A)(a)), so the table had 716 rows before the audit and 772 after, plus 30 defined-term rows (the 30 expressions this range defines or borrows, each pointing at its function) = 802 rows. Every non-blank line is in at least one row before and after. Every L4 name in the table was checked to exist in a layer-1 module.

| unit | text lines | disposition | L4 name(s) | tests | note |
| --- | --- | --- | --- | --- | --- |
| heading: Part 34 — Overseas companies | 14666 | inert (reason 1) | - | - | heading, not operative |
| heading: Introductory | 14667 | inert (reason 1) | - | - | heading, not operative |
| s 1044 | 14668-14669 | encoded | `s 1044 the company is an overseas company` | 2 | a "means" definition |
| s 1045 | 14670 | inert (reason 1) | - | - | section heading, not operative |
| s 1045(1) | 14671 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery (F1) |
| s 1045(2) | 14672 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery (F1) |
| heading: Registration of particulars | 14673 | inert (reason 1) | - | - | heading, not operative |
| s 1046 | 14674 | inert (reason 1) | - | - | section heading, not operative |
| s 1046(1) | 14675 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery (F1) |
| s 1046(1)(a) | 14676 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery (F1) |
| s 1046(1)(b) | 14677 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery (F1) |
| s 1046(2) | 14678 | encoded | `s 1046(2) the regulations must require the company to register particulars` | 4 | what the regulations must require (F1); the "(a) must ... if" limb answers JUST FALSE when its "if" fails; (b) and (c) are "may" |
| s 1046(2)(a) | 14679 | encoded | `s 1046(2) the regulations must require the company to register particulars` | 4 | what the regulations must require (F1); the "(a) must ... if" limb answers JUST FALSE when its "if" fails; (b) and (c) are "may" |
| s 1046(2)(b) | 14680 | encoded | `s 1046(2) the regulations must require the company to register particulars` | 4 | what the regulations must require (F1); the "(a) must ... if" limb answers JUST FALSE when its "if" fails; (b) and (c) are "may" |
| s 1046(2)(c) | 14681 | encoded | `s 1046(2) the regulations must require the company to register particulars` | 4 | what the regulations must require (F1); the "(a) must ... if" limb answers JUST FALSE when its "if" fails; (b) and (c) are "may" |
| s 1046(3) | 14682-14684 | encoded | `s 1046(3) the establishment is a branch`; `s 1046(3) the company is a Gibraltar company` | 5 | "branch" is borrowed from the Eleventh Company Law Directive (an input); "Gibraltar company" means |
| s 1046(4) | 14685 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery (F1) |
| s 1046(4)(a) | 14686 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery (F1) |
| s 1046(4)(b) | 14687-14688 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery (F1) |
| s 1046(5) | 14689 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery (F1) |
| s 1046(5)(a) | 14690 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery (F1) |
| s 1046(5)(b) | 14691 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery (F1) |
| s 1046(6) | 14692 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery (F1) |
| s 1046(6)(a) | 14693 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery (F1) |
| s 1046(6)(b) | 14694-14695 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery (F1) |
| s 1046(6A) | 14696 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery (F1) |
| s 1046(6A)(a) | 14697 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery (F1) |
| s 1046(6A)(b) | 14698-14699 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery (F1) |
| s 1046(6B) | 14700 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery (F1) |
| s 1046(6C) | 14701 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery (F1) |
| s 1046(7) | 14702 | encoded | `s 1046(7) the matter is specified` | 2 | "specified" means |
| s 1046(8) | 14703 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery (F1) |
| s 1047 | 14704 | inert (reason 1) | - | - | section heading, not operative |
| s 1047(1) | 14705 | encoded | `s 1047(1) the regulations must require the company to register its name` | 2 | what the regulations must require (F1) |
| s 1047(2) | 14706 | encoded | `s 1047(2) the name may be the registered name of the overseas company` | 3 | the two names that may be registered |
| s 1047(2)(a) | 14707 | encoded | `s 1047(2) the name may be the registered name of the overseas company` | 3 | the two names that may be registered |
| s 1047(2)(b) | 14708 | encoded | `s 1047(2) the name may be the registered name of the overseas company` | 3 | the two names that may be registered |
| s 1047(3) | 14709 | repealed or blank in this text | - | - | blank in this text |
| s 1047(4) | 14710 | encoded | `s 1047(4) the provision of Part 5 applies to the registration of the name of an overseas company`; `s 1047(4) the row of the list for the section of Part 5` | 42 | each listed provision of Part 5 is a constructor; the second function maps a section number to its row |
| s 1047(4)(a) | 14711 | encoded | `s 1047(4) the provision of Part 5 applies to the registration of the name of an overseas company`; `s 1047(4) the row of the list for the section of Part 5` | 42 | each listed provision of Part 5 is a constructor; the second function maps a section number to its row |
| s 1047(4)(aa) | 14712 | encoded | `s 1047(4) the provision of Part 5 applies to the registration of the name of an overseas company`; `s 1047(4) the row of the list for the section of Part 5` | 42 | each listed provision of Part 5 is a constructor; the second function maps a section number to its row |
| s 1047(4)(b) | 14713 | encoded | `s 1047(4) the provision of Part 5 applies to the registration of the name of an overseas company`; `s 1047(4) the row of the list for the section of Part 5` | 42 | each listed provision of Part 5 is a constructor; the second function maps a section number to its row |
| s 1047(4)(bza) | 14714 | encoded | `s 1047(4) the provision of Part 5 applies to the registration of the name of an overseas company`; `s 1047(4) the row of the list for the section of Part 5` | 42 | each listed provision of Part 5 is a constructor; the second function maps a section number to its row |
| s 1047(4)(ba) | 14715 | encoded | `s 1047(4) the provision of Part 5 applies to the registration of the name of an overseas company`; `s 1047(4) the row of the list for the section of Part 5` | 42 | each listed provision of Part 5 is a constructor; the second function maps a section number to its row |
| s 1047(4)(bb) | 14716 | encoded | `s 1047(4) the provision of Part 5 applies to the registration of the name of an overseas company`; `s 1047(4) the row of the list for the section of Part 5` | 42 | each listed provision of Part 5 is a constructor; the second function maps a section number to its row |
| s 1047(4)(bc) | 14717 | encoded | `s 1047(4) the provision of Part 5 applies to the registration of the name of an overseas company`; `s 1047(4) the row of the list for the section of Part 5` | 42 | each listed provision of Part 5 is a constructor; the second function maps a section number to its row |
| s 1047(4)(bd) | 14718 | encoded | `s 1047(4) the provision of Part 5 applies to the registration of the name of an overseas company`; `s 1047(4) the row of the list for the section of Part 5` | 42 | each listed provision of Part 5 is a constructor; the second function maps a section number to its row |
| s 1047(4)(c) | 14719 | encoded | `s 1047(4) the provision of Part 5 applies to the registration of the name of an overseas company`; `s 1047(4) the row of the list for the section of Part 5` | 42 | each listed provision of Part 5 is a constructor; the second function maps a section number to its row |
| s 1047(4)(d) | 14720 | encoded | `s 1047(4) the provision of Part 5 applies to the registration of the name of an overseas company`; `s 1047(4) the row of the list for the section of Part 5` | 42 | each listed provision of Part 5 is a constructor; the second function maps a section number to its row |
| s 1047(4)(e) | 14721 | encoded | `s 1047(4) the provision of Part 5 applies to the registration of the name of an overseas company`; `s 1047(4) the row of the list for the section of Part 5` | 42 | each listed provision of Part 5 is a constructor; the second function maps a section number to its row |
| s 1047(4)(f) | 14722 | encoded | `s 1047(4) the provision of Part 5 applies to the registration of the name of an overseas company`; `s 1047(4) the row of the list for the section of Part 5` | 42 | each listed provision of Part 5 is a constructor; the second function maps a section number to its row |
| s 1047(4)(g) | 14723 | encoded | `s 1047(4) the provision of Part 5 applies to the registration of the name of an overseas company`; `s 1047(4) the row of the list for the section of Part 5` | 42 | each listed provision of Part 5 is a constructor; the second function maps a section number to its row |
| s 1047(4)(h) | 14724 | encoded | `s 1047(4) the provision of Part 5 applies to the registration of the name of an overseas company`; `s 1047(4) the row of the list for the section of Part 5` | 42 | each listed provision of Part 5 is a constructor; the second function maps a section number to its row |
| s 1047(4)(i) | 14725 | encoded | `s 1047(4) the provision of Part 5 applies to the registration of the name of an overseas company`; `s 1047(4) the row of the list for the section of Part 5` | 42 | each listed provision of Part 5 is a constructor; the second function maps a section number to its row |
| s 1047(4)(j) | 14726 | encoded | `s 1047(4) the provision of Part 5 applies to the registration of the name of an overseas company`; `s 1047(4) the row of the list for the section of Part 5` | 42 | each listed provision of Part 5 is a constructor; the second function maps a section number to its row |
| s 1047(5) | 14727 | repealed or blank in this text | - | - | blank in this text |
| s 1047(6) | 14728 | encoded | `s 1047(6) the reference is read as a reference to registration of a different name under section 1048` | 2 | a rule of reading |
| s 1048 | 14729 | inert (reason 1) | - | - | section heading, not operative |
| s 1048(1) | 14730 | encoded | `s 1048(1) the company may deliver a statement of an alternative name` | 4 | a grant limited by its own wording |
| s 1048(2) | 14731 | encoded | `s 1048(2) the company may deliver a statement of a different name in substitution` | 4 | a grant limited by its own wording |
| s 1048(3) | 14732 | encoded | `s 1048(3) the name is treated for all purposes of the law applying in the United Kingdom as the company's corporate name` | 2 |  |
| s 1048(4) | 14733 | encoded | `s 1048(4) the treatment of the alternative name as the corporate name affects the matter` | 4 | three flat negatives |
| s 1048(4)(a) | 14734 | encoded | `s 1048(4) the treatment of the alternative name as the corporate name affects the matter` | 4 | three flat negatives |
| s 1048(4)(b) | 14735 | encoded | `s 1048(4) the treatment of the alternative name as the corporate name affects the matter` | 4 | three flat negatives |
| s 1048(4)(c) | 14736 | encoded | `s 1048(4) the treatment of the alternative name as the corporate name affects the matter` | 4 | three flat negatives |
| s 1048(5) | 14737 | encoded | `s 1048(5) the proceedings may be continued or commenced against the company by its name for the time being registered` | 3 |  |
| s 1048A | 14738 | inert (reason 1) | - | - | section heading, not operative |
| s 1048A(1) | 14739 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1048A(1)(a) | 14740 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1048A(1)(b) | 14741 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1048A(2) | 14742 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1048A(2)(a) | 14743 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1048A(2)(b) | 14744 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1048A(3) | 14745 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1048A(3)(a) | 14746 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1048A(3)(b) | 14747 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1048A(4) | 14748-14750 | encoded | `s 1048A(4) the address is an appropriate address`; `s 1048A(4) the email address is an appropriate email address` | 6 | both terms are defined by sections 86(2) and 88A(2) (other part's range): inputs |
| s 1048A(5) | 14751 | inert (reason 2) | - | - | procedure for regulations |
| s 1048B | 14752 | inert (reason 1) | - | - | section heading, not operative |
| s 1048B(1) | 14753 | encoded | `s 1048B(1) this section applies in relation to the overseas company` | 2 | a scope limit |
| s 1048B(2) | 14754 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1048B(3) | 14755 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1048B(3)(a) | 14756 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1048B(3)(b) | 14757 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1048B(3)(c) | 14758 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1048B(3)(d) | 14759 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1048B(4) | 14760 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| heading: Other requirements | 14761 | inert (reason 1) | - | - | heading, not operative |
| s 1049 | 14762 | inert (reason 1) | - | - | section heading, not operative |
| s 1049(1) | 14763 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1049(1)(a) | 14764 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1049(1)(b) | 14765-14766 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1049(2) | 14767-14769 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1049(2) list row 1 | 14768 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1049(2) list row 2 | 14769 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1049(3) | 14770 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1049(3)(a) | 14771 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1049(3)(b) | 14772 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1049(4) | 14773 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1050 | 14774 | inert (reason 1) | - | - | section heading, not operative |
| s 1050(1) | 14775 | encoded | `s 1050(1) this section applies to the credit or financial institution` | 4 | a scope limit |
| s 1050(1)(a) | 14776 | encoded | `s 1050(1) this section applies to the credit or financial institution` | 4 | a scope limit |
| s 1050(1)(b) | 14777 | encoded | `s 1050(1) this section applies to the credit or financial institution` | 4 | a scope limit |
| s 1050(1)(c) | 14778 | encoded | `s 1050(1) this section applies to the credit or financial institution` | 4 | a scope limit |
| s 1050(2) | 14779 | encoded | `s 1050(2) the place of business is a branch of the institution` | 4 | "branch" means |
| s 1050(3) | 14780 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1050(3)(a) | 14781 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1050(3)(b) | 14782-14783 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1050(4) | 14784-14786 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1050(4) list row 1 | 14785 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1050(4) list row 2 | 14786 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1050(5) | 14787 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1050(5)(a) | 14788 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1050(5)(b) | 14789 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1050(6) | 14790 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1051 | 14791 | inert (reason 1) | - | - | section heading, not operative |
| s 1051(1) | 14792 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1051(1)(a) | 14793 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1051(1)(b) | 14794 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1051(1)(c) | 14795 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1051(2) | 14796 | encoded | `s 1051(2)(a) the regulations must require the company to disclose the name registered by it under section 1047` | 2 | what the regulations must require (F1) |
| s 1051(2)(a) | 14797 | encoded | `s 1051(2)(a) the regulations must require the company to disclose the name registered by it under section 1047` | 2 | what the regulations must require (F1) |
| s 1051(2)(b) | 14798 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1051(3) | 14799-14801 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1051(4) | 14802 | encoded | `s 1051(4) the matter is specified` | 2 | "specified" means |
| s 1051(5) | 14803 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1052 | 14804 | inert (reason 1) | - | - | section heading, not operative |
| s 1052(1) | 14805 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1052(2) | 14806 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1052(2)(a) | 14807 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1052(2)(a)(i) | 14808 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1052(2)(a)(ii) | 14809 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1052(2)(b) | 14810 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1052(2)(c) | 14811 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1052(2)(d) | 14812 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1052(2)(e) | 14813 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1052(3) | 14814 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1052(4) | 14815 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1052(5) | 14816 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1052(6) | 14817-14819 | encoded | `s 1052(6) the overseas company is a registered overseas company`; `s 1052(6) the matter is specified` | 4 | two "means" definitions |
| s 1053 | 14820 | inert (reason 1) | - | - | section heading, not operative |
| s 1053(1) | 14821 | encoded | `s 1053(1) this section applies to the overseas company` | 2 | a scope limit |
| s 1053(2) | 14822 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1053(2)(a) | 14823 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1053(2)(a)(i) | 14824 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1053(2)(a)(ii) | 14825 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1053(2)(b) | 14826 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1053(3) | 14827 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1053(3)(a) | 14828 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1053(3)(b) | 14829 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1053(3)(c) | 14830 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1053(4) | 14831 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1053(5) | 14832 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1053(6) | 14833 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| heading: Supplementary | 14834 | inert (reason 1) | - | - | heading, not operative |
| s 1054 | 14835 | inert (reason 1) | - | - | section heading, not operative |
| s 1054(1) | 14836 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1054(2) | 14837 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1054(2)(a) | 14838 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1054(2)(b) | 14839 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1054(3) | 14840 | encoded | `s 1054(3)(a) the regulations may provide for imprisonment` | 1 | what the regulations must not provide (F1) |
| s 1054(3)(a) | 14841 | encoded | `s 1054(3)(a) the regulations may provide for imprisonment` | 1 | what the regulations must not provide (F1) |
| s 1054(3)(b) | 14842 | fork | `s 1054(3)(b) the regulations may provide for those fines` | 7 | F2: the text carries two wordings of the last limb; the later wording is taken and the limits are inputs |
| s 1054(4) | 14843 | encoded | `s 1054(4) the matter is specified` | 2 | "specified" means |
| s 1055 | 14844-14845 | encoded | `s 1055 the regulations must contain provision corresponding to that made by Chapter 8 of Part 10` | 2 | what the regulations must contain (F1); a failed "where" answers JUST FALSE |
| s 1056 | 14846-14847 | encoded | `s 1056 what the regulations under section 1046 must require the overseas company to register` | 2 | what the regulations must require (F1) |
| s 1056(a) | 14848 | encoded | `s 1056 what the regulations under section 1046 must require the overseas company to register` | 2 | what the regulations must require (F1) |
| s 1056(b) | 14849 | encoded | `s 1056 what the regulations under section 1046 must require the overseas company to register` | 2 | what the regulations must require (F1) |
| s 1057 | 14850 | inert (reason 1) | - | - | section heading, not operative |
| s 1057(1) | 14851 | encoded | `s 1057(1) this section applies to the overseas company` | 2 | a scope limit |
| s 1057(2) | 14852 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1057(2)(a) | 14853 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1057(2)(b) | 14854 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1057(3) | 14855 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1058 | 14856 | inert (reason 1) | - | - | section heading, not operative |
| s 1058(1) | 14857 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1058(1)(a) | 14858 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1058(1)(b) | 14859 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1058(2) | 14860 | encoded | `s 1058(2) the registrar to whom the regulations must provide for the notice to be given is the registrar for` | 3 | what the regulations must provide (F1) |
| s 1058(3) | 14861 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1058(4) | 14862 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1059 | 14863-14864 | encoded | `s 1059 the relocation counts as the closing of one branch and the opening of another` | 9 | a rule of reading: from one part to another counts, within one part does not |
| s 1059(a) | 14865 | encoded | `s 1059 the relocation counts as the closing of one branch and the opening of another` | 9 | a rule of reading: from one part to another counts, within one part does not |
| s 1059(b) | 14866 | encoded | `s 1059 the relocation counts as the closing of one branch and the opening of another` | 9 | a rule of reading: from one part to another counts, within one part does not |
| heading: Part 35 — The registrar of companies | 14867 | inert (reason 1) | - | - | heading, not operative |
| heading: Scheme of this Part | 14868 | inert (reason 1) | - | - | heading, not operative |
| s 1059A | 14869 | inert (reason 1) | - | - | section heading, not operative |
| s 1059A(1) | 14870 | inert (reason 1) | - | - | a lead-in that creates no rule (F6) |
| s 1059A(2) | 14871-14883 | encoded | `s 1059A(2) to (4) how the provision of this Part applies` | 93 | the three lists are one table; each list line is a row |
| s 1059A(2) list row 1 | 14872 | encoded | `s 1059A(2) to (4) how the provision of this Part applies` | 93 | the three lists are one table; each list line is a row |
| s 1059A(2) list row 2 | 14873 | fork | `s 1059A(2) to (4) how the provision of this Part applies` | 93 | F3: the line reads "sections 1068 1067A to 1071" (two versions joined); "1067A to 1071" is taken |
| s 1059A(2) list row 3 | 14874 | encoded | `s 1059A(2) to (4) how the provision of this Part applies` | 93 | the three lists are one table; each list line is a row |
| s 1059A(2) list row 4 | 14875 | encoded | `s 1059A(2) to (4) how the provision of this Part applies` | 93 | the three lists are one table; each list line is a row |
| s 1059A(2) list row 5 | 14876 | encoded | `s 1059A(2) to (4) how the provision of this Part applies` | 93 | the three lists are one table; each list line is a row |
| s 1059A(2) list row 6 | 14877 | encoded | `s 1059A(2) to (4) how the provision of this Part applies` | 93 | the three lists are one table; each list line is a row |
| s 1059A(2) list row 7 | 14878 | encoded | `s 1059A(2) to (4) how the provision of this Part applies` | 93 | the three lists are one table; each list line is a row |
| s 1059A(2) list row 8 | 14879 | encoded | `s 1059A(2) to (4) how the provision of this Part applies` | 93 | the three lists are one table; each list line is a row |
| s 1059A(2) list row 9 | 14880 | encoded | `s 1059A(2) to (4) how the provision of this Part applies` | 93 | the three lists are one table; each list line is a row |
| s 1059A(2) list row 10 | 14881 | encoded | `s 1059A(2) to (4) how the provision of this Part applies` | 93 | the three lists are one table; each list line is a row |
| s 1059A(2) list row 11 | 14882 | encoded | `s 1059A(2) to (4) how the provision of this Part applies` | 93 | the three lists are one table; each list line is a row |
| s 1059A(2) list row 12 | 14883 | encoded | `s 1059A(2) to (4) how the provision of this Part applies` | 93 | the three lists are one table; each list line is a row |
| s 1059A(3) | 14884-14895 | encoded | `s 1059A(2) to (4) how the provision of this Part applies` | 93 | see (2) |
| s 1059A(3) list row 1 | 14885 | encoded | `s 1059A(2) to (4) how the provision of this Part applies` | 93 | see (2) |
| s 1059A(3) list row 2 | 14886 | encoded | `s 1059A(2) to (4) how the provision of this Part applies` | 93 | see (2) |
| s 1059A(3) list row 3 | 14887 | encoded | `s 1059A(2) to (4) how the provision of this Part applies` | 93 | see (2) |
| s 1059A(3) list row 4 | 14888 | encoded | `s 1059A(2) to (4) how the provision of this Part applies` | 93 | see (2) |
| s 1059A(3) list row 5 | 14889 | encoded | `s 1059A(2) to (4) how the provision of this Part applies` | 93 | see (2) |
| s 1059A(3) list row 6 | 14890 | encoded | `s 1059A(2) to (4) how the provision of this Part applies` | 93 | see (2) |
| s 1059A(3) list row 7 | 14891 | encoded | `s 1059A(2) to (4) how the provision of this Part applies` | 93 | see (2) |
| s 1059A(3) list row 8 | 14892 | encoded | `s 1059A(2) to (4) how the provision of this Part applies` | 93 | see (2) |
| s 1059A(3) list row 9 | 14893 | encoded | `s 1059A(2) to (4) how the provision of this Part applies` | 93 | see (2) |
| s 1059A(3) list row 10 | 14894 | encoded | `s 1059A(2) to (4) how the provision of this Part applies` | 93 | see (2) |
| s 1059A(3) list row 11 | 14895 | encoded | `s 1059A(2) to (4) how the provision of this Part applies` | 93 | see (2) |
| s 1059A(4) | 14896-14901 | encoded | `s 1059A(2) to (4) how the provision of this Part applies` | 93 | see (2) |
| s 1059A(4) list row 1 | 14897 | encoded | `s 1059A(2) to (4) how the provision of this Part applies` | 93 | see (2) |
| s 1059A(4) list row 2 | 14898 | encoded | `s 1059A(2) to (4) how the provision of this Part applies` | 93 | see (2) |
| s 1059A(4) list row 3 | 14899 | encoded | `s 1059A(2) to (4) how the provision of this Part applies` | 93 | see (2) |
| s 1059A(4) list row 4 | 14900 | encoded | `s 1059A(2) to (4) how the provision of this Part applies` | 93 | see (2) |
| s 1059A(4) list row 5 | 14901 | encoded | `s 1059A(2) to (4) how the provision of this Part applies` | 93 | see (2) |
| s 1059A(5) | 14902 | encoded | `s 1059A(5) the provision of this Part applies to the overseas company as it applies to a company as defined in section 1` | 2 | "unless the context otherwise requires" once met answers NOTHING (F7) |
| heading: The registrar | 14903 | inert (reason 1) | - | - | heading, not operative |
| s 1060 | 14904 | inert (reason 1) | - | - | section heading, not operative |
| s 1060(1) | 14905 | encoded | `s 1060(1) there is to continue to be a registrar of companies for the place` | 3 |  |
| s 1060(1)(a) | 14906 | encoded | `s 1060(1) there is to continue to be a registrar of companies for the place` | 3 |  |
| s 1060(1)(b) | 14907 | encoded | `s 1060(1) there is to continue to be a registrar of companies for the place` | 3 |  |
| s 1060(1)(c) | 14908 | encoded | `s 1060(1) there is to continue to be a registrar of companies for the place` | 3 |  |
| s 1060(2) | 14909 | inert (reason 2) | - | - | appointment of the registrars: an office and its staffing |
| s 1060(3) | 14910 | encoded | `s 1060(3) the registrar of companies, as the case may require, for the place` | 3 | "the registrar" means the registrar for the place the case requires |
| s 1060(4) | 14911 | encoded | `s 1060(4) registration in the part of the United Kingdom is registration by` | 3 |  |
| s 1061 | 14912 | inert (reason 1) | - | - | section heading, not operative |
| s 1061(1) | 14913 | encoded | `s 1061(1) the registrar must perform the function` | 4 |  |
| s 1061(1)(a) | 14914 | encoded | `s 1061(1) the registrar must perform the function` | 4 |  |
| s 1061(1)(b) | 14915 | encoded | `s 1061(1) the registrar must perform the function` | 4 |  |
| s 1061(2) | 14916 | repealed or blank in this text | - | - | blank in this text |
| s 1061(3) | 14917 | encoded | `s 1061(3) the function is a function of the registrar for the purposes of the Act` | 3 | "are to": closed |
| s 1062 | 14918-14919 | encoded | `s 1062 the document bears the registrar's official seal` | 4 | the seam asked for by coa1, coa14 and coa19 |
| s 1062A | 14920 | inert (reason 1) | - | - | section heading, not operative |
| s 1062A(1) | 14921 | encoded | `s 1062A(1) the registrar must carry out the analysis`; `s 1062A(1) the registrar's duty to analyse information` | 6 | a duty on the registrar: decision function and regulative rule |
| s 1062A(2) | 14922 | inert (reason 1) | - | - | a cross-reference to section 1110F (F6) |
| s 1063 | 14923 | inert (reason 1) | - | - | section heading, not operative |
| s 1063(1) | 14924 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1063(1)(a) | 14925 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1063(1)(b) | 14926 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1063(2) | 14927 | encoded | `s 1063(2) fees may be charged for the matter` | 4 | "include": the three heads are not closed |
| s 1063(2)(a) | 14928 | encoded | `s 1063(2) fees may be charged for the matter` | 4 | "include": the three heads are not closed |
| s 1063(2)(b) | 14929 | encoded | `s 1063(2) fees may be charged for the matter` | 4 | "include": the three heads are not closed |
| s 1063(2)(c) | 14930 | encoded | `s 1063(2) fees may be charged for the matter` | 4 | "include": the three heads are not closed |
| s 1063(3) | 14931 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery (the list in (3A) is what the Secretary of State may take into account in making them) |
| s 1063(3)(a) | 14932 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery (the list in (3A) is what the Secretary of State may take into account in making them) |
| s 1063(3)(b) | 14933 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery (the list in (3A) is what the Secretary of State may take into account in making them) |
| s 1063(3)(c) | 14934 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery (the list in (3A) is what the Secretary of State may take into account in making them) |
| s 1063(3)(d) | 14935 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery (the list in (3A) is what the Secretary of State may take into account in making them) |
| s 1063(3A) | 14936 | inert (reason 2) | - | - | what the Secretary of State may take into account in fixing fees by regulations: part of a power to make regulations (F4) |
| s 1063(3A)(a) | 14937-14943 | inert (reason 2) | - | - | what the Secretary of State may take into account in fixing fees by regulations: part of a power to make regulations (F4) |
| s 1063(3A)(a) list row 1 | 14938 | inert (reason 2) | - | - | what the Secretary of State may take into account in fixing fees by regulations: part of a power to make regulations (F4) |
| s 1063(3A)(a) list row 2 | 14939 | inert (reason 2) | - | - | what the Secretary of State may take into account in fixing fees by regulations: part of a power to make regulations (F4) |
| s 1063(3A)(a) list row 3 | 14940 | inert (reason 2) | - | - | what the Secretary of State may take into account in fixing fees by regulations: part of a power to make regulations (F4) |
| s 1063(3A)(a) list row 4 | 14941 | inert (reason 2) | - | - | what the Secretary of State may take into account in fixing fees by regulations: part of a power to make regulations (F4) |
| s 1063(3A)(a) list row 5 | 14942 | inert (reason 2) | - | - | what the Secretary of State may take into account in fixing fees by regulations: part of a power to make regulations (F4) |
| s 1063(3A)(a) list row 6 | 14943 | inert (reason 2) | - | - | what the Secretary of State may take into account in fixing fees by regulations: part of a power to make regulations (F4) |
| s 1063(3A)(b) | 14944 | inert (reason 2) | - | - | what the Secretary of State may take into account in fixing fees by regulations: part of a power to make regulations (F4) |
| s 1063(3A)(c) | 14945 | inert (reason 2) | - | - | what the Secretary of State may take into account in fixing fees by regulations: part of a power to make regulations (F4) |
| s 1063(3A)(d) | 14946 | inert (reason 2) | - | - | what the Secretary of State may take into account in fixing fees by regulations: part of a power to make regulations (F4) |
| s 1063(3A)(e) | 14947 | inert (reason 2) | - | - | what the Secretary of State may take into account in fixing fees by regulations: part of a power to make regulations (F4) |
| s 1063(3A)(f) | 14948 | inert (reason 2) | - | - | what the Secretary of State may take into account in fixing fees by regulations: part of a power to make regulations (F4) |
| s 1063(3A)(g) | 14949 | inert (reason 2) | - | - | what the Secretary of State may take into account in fixing fees by regulations: part of a power to make regulations (F4) |
| s 1063(4) | 14950 | inert (reason 2) | - | - | procedure for regulations |
| s 1063(5) | 14951 | encoded | `s 1063(5) the registrar may determine from time to time what fees, if any, are chargeable` | 2 |  |
| s 1063(5)(a) | 14952 | encoded | `s 1063(5) the registrar may determine from time to time what fees, if any, are chargeable` | 2 |  |
| s 1063(5)(b) | 14953-14954 | encoded | `s 1063(5) the registrar may determine from time to time what fees, if any, are chargeable` | 2 |  |
| s 1063(6) | 14955 | encoded | `s 1063(6) the fee received by the registrar has been dealt with as the section requires` | 4 |  |
| s 1063(6A) | 14956 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1063(6A)(a) | 14957 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1063(6A)(b) | 14958 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1063(6B) | 14959 | inert (reason 2) | - | - | procedure for regulations |
| s 1063(7) | 14960 | inert (reason 2) | - | - | amendment of the Limited Partnerships Act 1907 |
| s 1063(7)(a) | 14961 | inert (reason 2) | - | - | amendment of the Limited Partnerships Act 1907 |
| s 1063(7)(a)(i) | 14962 | inert (reason 2) | - | - | amendment of the Limited Partnerships Act 1907 |
| s 1063(7)(a)(ii) | 14963 | inert (reason 2) | - | - | amendment of the Limited Partnerships Act 1907 |
| s 1063(7)(b) | 14964 | inert (reason 2) | - | - | amendment of the Limited Partnerships Act 1907 |
| s 1063(7)(b)(i) | 14965 | inert (reason 2) | - | - | amendment of the Limited Partnerships Act 1907 |
| s 1063(7)(b)(ii) | 14966 | inert (reason 2) | - | - | amendment of the Limited Partnerships Act 1907 |
| heading: Certificates of incorporation | 14967 | inert (reason 1) | - | - | heading, not operative |
| s 1064 | 14968 | inert (reason 1) | - | - | section heading, not operative |
| s 1064(1) | 14969 | encoded | `s 1064(1) the registrar must cause notice of the issue of the certificate to be published`; `s 1064(1) the registrar has complied by publishing the notice`; `s 1064(1) the registrar's duty to publish notice of the issue of a certificate of incorporation` | 9 |  |
| s 1064(1)(a) | 14970 | encoded | `s 1064(1) the registrar must cause notice of the issue of the certificate to be published`; `s 1064(1) the registrar has complied by publishing the notice`; `s 1064(1) the registrar's duty to publish notice of the issue of a certificate of incorporation` | 9 |  |
| s 1064(1)(b) | 14971-14972 | encoded | `s 1064(1) the registrar must cause notice of the issue of the certificate to be published`; `s 1064(1) the registrar has complied by publishing the notice`; `s 1064(1) the registrar's duty to publish notice of the issue of a certificate of incorporation` | 9 |  |
| s 1064(2) | 14973 | encoded | `s 1064(2) the notice states what it must state` | 4 |  |
| s 1064(3) | 14974 | encoded | `s 1064(3) section 1064 applies to the certificate of incorporation` | 5 |  |
| s 1064(3)(a) | 14975 | encoded | `s 1064(3) section 1064 applies to the certificate of incorporation` | 5 |  |
| s 1064(3)(b) | 14976 | encoded | `s 1064(3) section 1064 applies to the certificate of incorporation` | 5 |  |
| s 1064(3)(c) | 14977-14978 | encoded | `s 1064(3) section 1064 applies to the certificate of incorporation` | 5 |  |
| s 1065 | 14979-14980 | encoded | `s 1065 the person may require the registrar to provide a copy of the certificate of incorporation`; `s 1065 the right of any person to a copy of a certificate of incorporation` | 5 | a right of any person: decision function and regulative rule |
| heading: Registered numbers | 14981 | inert (reason 1) | - | - | heading, not operative |
| s 1066 | 14982 | inert (reason 1) | - | - | section heading, not operative |
| s 1066(1) | 14983 | encoded | `s 1066(1) the registrar must allocate a registered number to the company` | 3 |  |
| s 1066(2) | 14984 | encoded | `s 1066(2) the registered number is in the form the section requires` | 4 |  |
| s 1066(3) | 14985 | encoded | `s 1066(3) the registrar may change the existing registered number` | 4 | "on adopting" counts as "upon": a failed one answers JUST FALSE |
| s 1066(4) | 14986 | encoded | `s 1066(4) the change of registered number has effect on the day` | 4 |  |
| s 1066(5) | 14987 | encoded | `s 1066(5) the last day of the three years beginning with the date`; `s 1066(5) the requirement to disclose the registered number imposed by regulations under section 82 or section 1051 is satisfied by the number disclosed` | 8 | the three years are tested on both sides of the end (F12) |
| s 1066(6) | 14988 | encoded | `s 1066(6) the overseas company is a company for the purposes of section 1066` | 4 | "(other than X)" (F8) |
| s 1067 | 14989 | inert (reason 1) | - | - | section heading, not operative |
| s 1067(1) | 14990 | encoded | `s 1067(1) the registrar must allocate a registered number to the UK establishment` | 3 |  |
| s 1067(2) | 14991 | encoded | `s 1067(2) the registered number of the UK establishment is in the form the section requires` | 3 |  |
| s 1067(3) | 14992 | encoded | `s 1067(3) the registrar may change the existing registered number of the UK establishment` | 4 |  |
| s 1067(4) | 14993 | encoded | `s 1067(4) the change of the registered number of the UK establishment has effect on the day` | 3 |  |
| s 1067(5) | 14994 | encoded | `s 1067(5) the requirement to disclose the UK establishment's registered number imposed by regulations under section 1051 is satisfied by the number disclosed` | 4 |  |
| s 1067(6) | 14995 | encoded | `s 1067(6) the place is an establishment of the overseas company`; `s 1067(6) the establishment is a UK establishment of the overseas company` | 10 | two "means" definitions |
| s 1067(6)(a) | 14996 | encoded | `s 1067(6) the place is an establishment of the overseas company`; `s 1067(6) the establishment is a UK establishment of the overseas company` | 10 | two "means" definitions |
| s 1067(6)(b) | 14997-14998 | encoded | `s 1067(6) the place is an establishment of the overseas company`; `s 1067(6) the establishment is a UK establishment of the overseas company` | 10 | two "means" definitions |
| heading: Who may deliver documents to the registrar | 14999 | inert (reason 1) | - | - | heading, not operative |
| s 1067A | 15000 | inert (reason 1) | - | - | section heading, not operative |
| s 1067A(1) | 15001 | encoded | `s 1067A(1) the individual is barred from delivering the document to the registrar on their own behalf`; `s 1067A(1) the prohibition on an individual delivering a document on their own behalf` | 9 | an "unless" bar (F9): decision function and regulative rule |
| s 1067A(1)(a) | 15002 | encoded | `s 1067A(1) the individual is barred from delivering the document to the registrar on their own behalf`; `s 1067A(1) the prohibition on an individual delivering a document on their own behalf` | 9 | an "unless" bar (F9): decision function and regulative rule |
| s 1067A(1)(b) | 15003 | encoded | `s 1067A(1) the individual is barred from delivering the document to the registrar on their own behalf`; `s 1067A(1) the prohibition on an individual delivering a document on their own behalf` | 9 | an "unless" bar (F9): decision function and regulative rule |
| s 1067A(2) | 15004 | fork | `s 1067A(2) the individual is barred from delivering the document to the registrar on behalf of B` | 12 | F10: a firm's four rows are read as alternatives; the table rows are encoded one function each |
| s 1067A(2)(a) | 15005 | fork | `s 1067A(2) the individual is barred from delivering the document to the registrar on behalf of B` | 12 | F10: a firm's four rows are read as alternatives; the table rows are encoded one function each |
| s 1067A(2)(b) | 15006 | fork | `s 1067A(2) the individual is barred from delivering the document to the registrar on behalf of B` | 12 | F10: a firm's four rows are read as alternatives; the table rows are encoded one function each |
| s 1067A(2) table column numbers | 15007 | inert (reason 1) | - | - | table column headings, not operative |
| s 1067A(2) table column headings | 15008 | inert (reason 1) | - | - | table column headings, not operative |
| s 1067A(2) table row 1 | 15009 | encoded | `s 1067A(2) row 1 is satisfied` | 6 | the exception the row creates; B is a firm |
| s 1067A(2) table row 2 | 15010 | encoded | `s 1067A(2) row 2 is satisfied` | 5 | the exception the row creates; B is a firm |
| s 1067A(2) table row 3 | 15011 | encoded | `s 1067A(2) row 3 is satisfied` | 4 | the exception the row creates; B is a firm |
| s 1067A(2) table row 4 | 15012 | encoded | `s 1067A(2) row 4 is satisfied` | 3 | the exception the row creates; B is a firm |
| s 1067A(2) table row 5 | 15013 | encoded | `s 1067A(2) row 5 is satisfied` | 4 | the exception the row creates; B is a individual |
| s 1067A(2) table row 6 | 15014 | encoded | `s 1067A(2) row 6 is satisfied` | 4 | the exception the row creates; B is a individual |
| s 1067A(2) table row 7 | 15015 | encoded | `s 1067A(2) row 7 is satisfied` | 3 | the exception the row creates; B is a individual |
| s 1067A(3) | 15016 | encoded | `s 1067A(3) the individual is one of the officers of the corporate officer for the purposes of row 2` | 8 | recursion over a list of levels |
| s 1067A(3)(a) | 15017 | encoded | `s 1067A(3) the individual is one of the officers of the corporate officer for the purposes of row 2` | 8 | recursion over a list of levels |
| s 1067A(3)(b) | 15018-15019 | encoded | `s 1067A(3) the individual is one of the officers of the corporate officer for the purposes of row 2` | 8 | recursion over a list of levels |
| s 1067A(4) | 15020 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1067A(4)(a) | 15021 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1067A(4)(b) | 15022 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1067A(5) | 15023 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1067A(5)(a) | 15024 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1067A(5)(b) | 15025 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1067A(6) | 15026 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1067A(7) | 15027 | inert (reason 2) | - | - | procedure for regulations |
| s 1067A(8) | 15028 | encoded | `s 1067A(8) the officer is a corporate officer` | 2 | "means" |
| s 1067B | 15029 | inert (reason 1) | - | - | section heading, not operative |
| s 1067B(1) | 15030 | encoded | `s 1067B(1) the individual is barred from delivering documents to the registrar on their own behalf or on behalf of another`; `s 1067B(1) the prohibition on a disqualified individual delivering documents` | 4 |  |
| s 1067B(2) | 15031 | encoded | `s 1067B(2) the individual is barred from delivering the document to the registrar on behalf of the disqualified person` | 6 | an "unless" bar (F9) |
| s 1067B(2)(a) | 15032 | encoded | `s 1067B(2) the individual is barred from delivering the document to the registrar on behalf of the disqualified person` | 6 | an "unless" bar (F9) |
| s 1067B(2)(b) | 15033 | encoded | `s 1067B(2) the individual is barred from delivering the document to the registrar on behalf of the disqualified person` | 6 | an "unless" bar (F9) |
| s 1067B(3) | 15034 | encoded | `s 1067B(3) the document is accompanied by the two statements` | 6 |  |
| s 1067B(4) | 15035 | encoded | `s 1067B(3) the document is accompanied by the two statements` | 6 |  |
| s 1067B(5) | 15036 | encoded | `s 1067B(3) the document is accompanied by the two statements` | 6 |  |
| s 1067B(5)(a) | 15037 | encoded | `s 1067B(3) the document is accompanied by the two statements` | 6 |  |
| s 1067B(5)(b) | 15038 | encoded | `s 1067B(3) the document is accompanied by the two statements` | 6 |  |
| s 1067B(5)(c) | 15039 | encoded | `s 1067B(3) the document is accompanied by the two statements` | 6 |  |
| s 1067B(6) | 15040 | encoded | `s 1067B(6) the person is a disqualified person` | 3 | defined by section 159A(2) (input) |
| s 1067B(7) | 15041 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1067B(8) | 15042 | inert (reason 2) | - | - | procedure for regulations |
| heading: Delivery of documents to the registrar | 15043 | inert (reason 1) | - | - | heading, not operative |
| s 1068 | 15044 | inert (reason 1) | - | - | section heading, not operative |
| s 1068(1) | 15045 | encoded | `s 1068 the registrar may impose the requirement` | 10 | the heads of (2) to (4) are constructors |
| s 1068(2) | 15046 | encoded | `s 1068 the registrar may impose the requirement` | 10 |  |
| s 1068(2)(a) | 15047 | encoded | `s 1068 the registrar may impose the requirement` | 10 |  |
| s 1068(2)(b) | 15048 | encoded | `s 1068 the registrar may impose the requirement` | 10 |  |
| s 1068(3) | 15049 | encoded | `s 1068 the registrar may impose the requirement` | 10 |  |
| s 1068(3)(a) | 15050 | encoded | `s 1068 the registrar may impose the requirement` | 10 |  |
| s 1068(3)(b) | 15051 | encoded | `s 1068 the registrar may impose the requirement` | 10 |  |
| s 1068(3)(c) | 15052 | encoded | `s 1068 the registrar may impose the requirement` | 10 |  |
| s 1068(4) | 15053 | encoded | `s 1068 the registrar may impose the requirement`; `s 1068(4A) the requirement must be imposed by means of registrar's rules` | 20 |  |
| s 1068(4)(a) | 15054 | encoded | `s 1068 the registrar may impose the requirement`; `s 1068(4A) the requirement must be imposed by means of registrar's rules` | 20 |  |
| s 1068(4)(b) | 15055 | encoded | `s 1068 the registrar may impose the requirement`; `s 1068(4A) the requirement must be imposed by means of registrar's rules` | 20 |  |
| s 1068(4)(c) | 15056 | encoded | `s 1068 the registrar may impose the requirement`; `s 1068(4A) the requirement must be imposed by means of registrar's rules` | 20 |  |
| s 1068(4)(d) | 15057 | encoded | `s 1068 the registrar may impose the requirement`; `s 1068(4A) the requirement must be imposed by means of registrar's rules` | 20 |  |
| s 1068(4A) | 15058 | encoded | `s 1068(4A) the requirement must be imposed by means of registrar's rules` | 10 |  |
| s 1068(5) | 15059 | repealed or blank in this text | - | - | blank in this text |
| s 1068(6) | 15060 | repealed or blank in this text | - | - | blank in this text |
| s 1068(6A) | 15061 | repealed or blank in this text | - | - | blank in this text |
| s 1068(7) | 15062 | encoded | `s 1068(7) the registrar may impose the requirement consistently with the enactments` | 2 |  |
| s 1068A | 15063 | inert (reason 1) | - | - | section heading, not operative |
| s 1068A(1) | 15064 | inert (reason 2) | - | - | a power to make registrar's rules |
| s 1068A(1)(a) | 15065 | inert (reason 2) | - | - | a power to make registrar's rules |
| s 1068A(1)(b) | 15066 | inert (reason 2) | - | - | a power to make registrar's rules |
| s 1068A(1)(c) | 15067 | inert (reason 2) | - | - | a power to make registrar's rules |
| s 1068A(2) | 15068 | encoded | `s 1068A(2) the registrar's rules may make the provision` | 4 |  |
| s 1069 | 15069-15070 | repealed or blank in this text | - | - | blank in this text |
| s 1070 | 15071 | inert (reason 1) | - | - | section heading, not operative |
| s 1070(1) | 15072 | encoded | `s 1070(1) the registrar may make the agreement for delivery by electronic means` | 3 |  |
| s 1070(1)(a) | 15073 | encoded | `s 1070(1) the registrar may make the agreement for delivery by electronic means` | 3 |  |
| s 1070(1)(b) | 15074 | encoded | `s 1070(1) the registrar may make the agreement for delivery by electronic means` | 3 |  |
| s 1070(2) | 15075 | encoded | `s 1070(2) the agreement may relate to the documents` | 2 |  |
| s 1070(3) | 15076 | encoded | `s 1070(3) the document is delivered as the section requires`; `s 1070(3) the duty to deliver in accordance with the agreement` | 6 | the deliverer is taken to be the company (F11) |
| s 1071 | 15077 | inert (reason 1) | - | - | section heading, not operative |
| s 1071(1) | 15078 | encoded | `s 1071(1) the document cannot yet count as delivered to the registrar` | 2 | an "until" bar (ruling of 2026-11-05 (d)) |
| s 1071(2) | 15079 | inert (reason 2) | - | - | a power to make registrar's rules; the day of receipt is an input of the next function |
| heading: Requirements for proper delivery | 15080 | inert (reason 1) | - | - | heading, not operative |
| s 1072 | 15081 | inert (reason 1) | - | - | section heading, not operative |
| s 1072(1) | 15082 | encoded | `s 1072 the document meets the requirements for proper delivery`; `s 1072(1) all the requirements in the list are met` | 25 | the seam asked for by every filing section; the conjunction of the limbs |
| s 1072(1)(a) | 15083 | encoded | `s 1072 the document meets the requirements for proper delivery`; `s 1072(1) all the requirements in the list are met` | 25 | the seam asked for by every filing section; the conjunction of the limbs |
| s 1072(1)(a)(i) | 15084 | encoded | `s 1072 the document meets the requirements for proper delivery`; `s 1072(1) all the requirements in the list are met` | 25 | the seam asked for by every filing section; the conjunction of the limbs |
| s 1072(1)(a)(ii) | 15085 | encoded | `s 1072 the document meets the requirements for proper delivery`; `s 1072(1) all the requirements in the list are met` | 25 | the seam asked for by every filing section; the conjunction of the limbs |
| s 1072(1)(aa) | 15086 | encoded | `s 1072 the document meets the requirements for proper delivery`; `s 1072(1) all the requirements in the list are met` | 25 | the seam asked for by every filing section; the conjunction of the limbs |
| s 1072(1)(b) | 15087-15091 | encoded | `s 1072 the document meets the requirements for proper delivery`; `s 1072(1) all the requirements in the list are met` | 25 | the seam asked for by every filing section; the conjunction of the limbs |
| s 1072(1)(b) list row 1 | 15088 | encoded | `s 1072 the document meets the requirements for proper delivery`; `s 1072(1) all the requirements in the list are met` | 25 | the seam asked for by every filing section; the conjunction of the limbs |
| s 1072(1)(b) list row 2 | 15089 | encoded | `s 1072 the document meets the requirements for proper delivery`; `s 1072(1) all the requirements in the list are met` | 25 | the seam asked for by every filing section; the conjunction of the limbs |
| s 1072(1)(b) list row 3 | 15090 | repealed or blank in this text | - | - | the line is "..." in this text (a repealed item, section 1069) |
| s 1072(1)(b) list row 4 | 15091 | encoded | `s 1072 the document meets the requirements for proper delivery`; `s 1072(1) all the requirements in the list are met` | 25 | the seam asked for by every filing section; the conjunction of the limbs |
| s 1072(1)(c) | 15092 | encoded | `s 1072 the document meets the requirements for proper delivery`; `s 1072(1) all the requirements in the list are met` | 25 | the seam asked for by every filing section; the conjunction of the limbs |
| s 1072(1)(d) | 15093 | encoded | `s 1072 the document meets the requirements for proper delivery`; `s 1072(1) all the requirements in the list are met` | 25 | the seam asked for by every filing section; the conjunction of the limbs |
| s 1072(1)(e) | 15094 | encoded | `s 1072 the document meets the requirements for proper delivery`; `s 1072(1) all the requirements in the list are met` | 25 | the seam asked for by every filing section; the conjunction of the limbs |
| s 1072(1)(f) | 15095 | encoded | `s 1072 the document meets the requirements for proper delivery`; `s 1072(1) all the requirements in the list are met` | 25 | the seam asked for by every filing section; the conjunction of the limbs |
| s 1072(1)(g) | 15096 | encoded | `s 1072 the document meets the requirements for proper delivery`; `s 1072(1) all the requirements in the list are met` | 25 | the seam asked for by every filing section; the conjunction of the limbs |
| s 1072(2) | 15097 | encoded | `s 1072(2) the document is treated as not having been delivered` | 5 |  |
| s 1073 | 15098 | inert (reason 1) | - | - | section heading, not operative |
| s 1073(1) | 15099 | encoded | `s 1073(1) the registrar may accept and register the document` | 2 |  |
| s 1073(2) | 15100 | encoded | `s 1073(2) the document is treated as received by the registrar for the purposes of section 1077` | 2 |  |
| s 1073(3) | 15101 | encoded | `s 1073(3) an objection may be taken on that ground` | 4 |  |
| s 1073(4) | 15102 | encoded | `s 1073(4) the acceptance of the document affects the matter` | 3 | (b) "subject as follows" answers NOTHING (F13) |
| s 1073(4)(a) | 15103 | encoded | `s 1073(4) the acceptance of the document affects the matter` | 3 | (b) "subject as follows" answers NOTHING (F13) |
| s 1073(4)(b) | 15104 | encoded | `s 1073(4) the acceptance of the document affects the matter` | 3 | (b) "subject as follows" answers NOTHING (F13) |
| s 1073(5) | 15105 | encoded | `s 1073(5) the day counts as a day of default in complying with the requirements for proper delivery` | 13 |  |
| s 1073(5)(a) | 15106 | encoded | `s 1073(5) the day counts as a day of default in complying with the requirements for proper delivery` | 13 |  |
| s 1073(5)(b) | 15107-15108 | encoded | `s 1073(5) the day counts as a day of default in complying with the requirements for proper delivery` | 13 |  |
| s 1073(6) | 15109 | encoded | `s 1073(5) the day counts as a day of default in complying with the requirements for proper delivery` | 13 | (6) is the second half of the same function; 14 days tested on both sides |
| s 1073(6)(a) | 15110 | encoded | `s 1073(5) the day counts as a day of default in complying with the requirements for proper delivery` | 13 | (6) is the second half of the same function; 14 days tested on both sides |
| s 1073(6)(b) | 15111-15112 | encoded | `s 1073(5) the day counts as a day of default in complying with the requirements for proper delivery` | 13 | (6) is the second half of the same function; 14 days tested on both sides |
| s 1073A | 15113 | inert (reason 1) | - | - | section heading, not operative |
| s 1073A(1) | 15114 | fork | `s 1073A(1) the registrar may refuse to accept and register the document` | 4 | F28: a grant named "may" with an "if" gate; a failed "if" answers NOTHING (name-test sweep) |
| s 1073A(1)(a) | 15115 | fork | `s 1073A(1) the registrar may refuse to accept and register the document` | 4 | F28: a grant named "may" with an "if" gate; a failed "if" answers NOTHING (name-test sweep) |
| s 1073A(1)(b) | 15116 | fork | `s 1073A(1) the registrar may refuse to accept and register the document` | 4 | F28: a grant named "may" with an "if" gate; a failed "if" answers NOTHING (name-test sweep) |
| s 1073A(2) | 15117 | encoded | `s 1073A(2) the document is refused` | 2 |  |
| s 1073A(3) | 15118 | encoded | `s 1073A(3) the document is treated as not having been delivered` | 2 |  |
| s 1074 | 15119 | inert (reason 1) | - | - | section heading, not operative |
| s 1074(1) | 15120 | encoded | `s 1074(1) this section applies to the document` | 2 |  |
| s 1074(2) | 15121 | encoded | `s 1074(2) the material is unnecessary material` | 4 | "means" |
| s 1074(2)(a) | 15122 | encoded | `s 1074(2) the material is unnecessary material` | 4 | "means" |
| s 1074(2)(b) | 15123 | encoded | `s 1074(2) the material is unnecessary material` | 4 | "means" |
| s 1074(3) | 15124 | encoded | `s 1074(3) the obligation to deliver a document extends to the thing` | 2 |  |
| s 1074(4) | 15125 | encoded | `s 1074(4) the document is treated as not meeting the requirements for proper delivery` | 4 |  |
| s 1074(5) | 15126 | fork | `s 1074(5) the registrar may register the document either with the omission of the unnecessary material or as delivered` | 4 | F29: a grant named "may" with an "if" gate; a failed "if" answers NOTHING (name-test sweep) |
| s 1074(5)(a) | 15127 | fork | `s 1074(5) the registrar may register the document either with the omission of the unnecessary material or as delivered` | 4 | F29: a grant named "may" with an "if" gate; a failed "if" answers NOTHING (name-test sweep) |
| s 1074(5)(b) | 15128 | fork | `s 1074(5) the registrar may register the document either with the omission of the unnecessary material or as delivered` | 4 | F29: a grant named "may" with an "if" gate; a failed "if" answers NOTHING (name-test sweep) |
| s 1075 | 15129-15130 | repealed or blank in this text | - | - | blank in this text |
| s 1076 | 15131 | inert (reason 1) | - | - | section heading, not operative |
| s 1076(1) | 15132 | encoded | `s 1076(1) the registrar may accept a replacement for the document previously delivered` | 3 |  |
| s 1076(1)(a) | 15133 | encoded | `s 1076(1) the registrar may accept a replacement for the document previously delivered` | 3 |  |
| s 1076(1)(b) | 15134 | encoded | `s 1076(1) the registrar may accept a replacement for the document previously delivered` | 3 |  |
| s 1076(2) | 15135 | encoded | `s 1076(2) the replacement document must not be accepted` | 4 | an "unless" bar (F9) |
| s 1076(2)(a) | 15136 | encoded | `s 1076(2) the replacement document must not be accepted` | 4 | an "unless" bar (F9) |
| s 1076(2)(b) | 15137-15138 | encoded | `s 1076(2) the replacement document must not be accepted` | 4 | an "unless" bar (F9) |
| s 1076(3) | 15139 | encoded | `s 1076(3) the registrar's power to impose requirements as to form and manner of delivery includes power to impose the requirement` | 3 | "includes" |
| s 1076(4) | 15140 | encoded | `s 1076(4) this section applies to the original document` | 2 |  |
| heading: Public notice of receipt of certain documents | 15141 | inert (reason 1) | - | - | heading, not operative |
| s 1077 | 15142 | inert (reason 1) | - | - | section heading, not operative |
| s 1077(1) | 15143 | encoded | `s 1077(1) the registrar must cause notice of the receipt of the document to be published`; `s 1077(1) the registrar has complied by publishing the notice`; `s 1077(1) the registrar's duty to publish notice of the receipt of an enhanced disclosure document` | 10 |  |
| s 1077(1)(a) | 15144 | encoded | `s 1077(1) the registrar must cause notice of the receipt of the document to be published`; `s 1077(1) the registrar has complied by publishing the notice`; `s 1077(1) the registrar's duty to publish notice of the receipt of an enhanced disclosure document` | 10 |  |
| s 1077(1)(b) | 15145-15146 | encoded | `s 1077(1) the registrar must cause notice of the receipt of the document to be published`; `s 1077(1) the registrar has complied by publishing the notice`; `s 1077(1) the registrar's duty to publish notice of the receipt of an enhanced disclosure document` | 10 |  |
| s 1077(2) | 15147 | encoded | `s 1077(2) the notice states what it must state` | 5 |  |
| s 1077(3) | 15148 | encoded | `s 1077(3) the registrar is required to cause notice of the receipt of the document to be published on the day` | 3 |  |
| s 1078 | 15149 | inert (reason 1) | - | - | section heading, not operative |
| s 1078(1) | 15150-15151 | encoded | `s 1078 the document is an enhanced disclosure document` | 69 | the list defines the term, so a head that does not hold answers JUST FALSE (F17); the "..." line is blank in this text |
| s 1078(2) | 15152 | encoded | `s 1078 the document is an enhanced disclosure document` | 69 | every company |
| s 1078(2) group Constitutional documents | 15153 | encoded | `s 1078 the document is an enhanced disclosure document` | 69 | every company |
| s 1078(2) Constitutional documents item 1 | 15154 | encoded | `s 1078 the document is an enhanced disclosure document` | 69 | every company; constructor `s 1078(2) constitutional documents 1: the company's memorandum and articles` |
| s 1078(2) Constitutional documents item 2 | 15155 | encoded | `s 1078 the document is an enhanced disclosure document` | 69 | every company; constructor `s 1078(2) constitutional documents 2: any amendment of the company's articles (including every resolution or agreement required to be embodied ...` |
| s 1078(2) Constitutional documents item 3 | 15156 | encoded | `s 1078 the document is an enhanced disclosure document` | 69 | every company; constructor `s 1078(2) constitutional documents 3: after any amendment of the company's articles, the text of the articles as amended` |
| s 1078(2) Constitutional documents item 4 | 15157 | encoded | `s 1078 the document is an enhanced disclosure document` | 69 | every company; constructor `s 1078(2) constitutional documents 4: any notice of a change of the company's name` |
| s 1078(2) group Directors | 15158 | encoded | `s 1078 the document is an enhanced disclosure document` | 69 | every company |
| s 1078(2) Directors item 1 | 15159 | encoded | `s 1078 the document is an enhanced disclosure document` | 69 | every company; constructor `s 1078(2) directors 1: the statement of proposed officers required on formation of the company` |
| s 1078(2) Directors item 2 | 15160 | encoded | `s 1078 the document is an enhanced disclosure document` | 69 | every company; constructor `s 1078(2) directors 2: notification of any change among the company's directors` |
| s 1078(2) Directors item 3 | 15161 | encoded | `s 1078 the document is an enhanced disclosure document` | 69 | every company; constructor `s 1078(2) directors 3: notification of any change in the particulars of directors required to be delivered to the registrar` |
| s 1078(2) group Accounts and reports etc | 15162 | encoded | `s 1078 the document is an enhanced disclosure document` | 69 | every company |
| s 1078(2) Accounts and reports etc item 1 | 15163 | encoded | `s 1078 the document is an enhanced disclosure document` | 69 | every company; constructor `s 1078(2) accounts and reports etc 1: all documents required to be delivered to the registrar under section 441 (annual accounts and reports)` |
| s 1078(2) Accounts and reports etc item 1A | 15164 | encoded | `s 1078 the document is an enhanced disclosure document` | 69 | every company; constructor `s 1078(2) accounts and reports etc 1A: all documents delivered to the registrar under sections 394A(2)(e), 448A(2)(e) and 479A(2)(e) (qualifying ...` |
| s 1078(2) Accounts and reports etc item 2 | 15165 | encoded | `s 1078 the document is an enhanced disclosure document` | 69 | every company; constructor `s 1078(2) accounts and reports etc 2: any confirmation statement delivered by the company under section 853A` |
| s 1078(2) group Registered office | 15166 | encoded | `s 1078 the document is an enhanced disclosure document` | 69 | every company |
| s 1078(2) Registered office item 1 | 15167 | encoded | `s 1078 the document is an enhanced disclosure document` | 69 | every company; constructor `s 1078(2) registered office 1: notification of any change of the company's registered office` |
| s 1078(2) group Winding up | 15168 | encoded | `s 1078 the document is an enhanced disclosure document` | 69 | every company |
| s 1078(2) Winding up item 1 | 15169 | encoded | `s 1078 the document is an enhanced disclosure document` | 69 | every company; constructor `s 1078(2) winding up 1: copy of any winding-up order in respect of the company` |
| s 1078(2) Winding up item 2 | 15170 | encoded | `s 1078 the document is an enhanced disclosure document` | 69 | every company; constructor `s 1078(2) winding up 2: notice of the appointment of liquidators` |
| s 1078(2) Winding up item 3 | 15171 | encoded | `s 1078 the document is an enhanced disclosure document` | 69 | every company; constructor `s 1078(2) winding up 3: order for the dissolution of a company on a winding up` |
| s 1078(2) Winding up item 4 | 15172 | encoded | `s 1078 the document is an enhanced disclosure document` | 69 | every company; constructor `s 1078(2) winding up 4: return by a liquidator of the final meeting of a company on a winding up` |
| s 1078(3) | 15173 | encoded | `s 1078 the document is an enhanced disclosure document` | 69 | a public company |
| s 1078(3) group Share capital | 15174 | encoded | `s 1078 the document is an enhanced disclosure document` | 69 | a public company |
| s 1078(3) Share capital item 1 | 15175 | encoded | `s 1078 the document is an enhanced disclosure document` | 69 | a public company; constructor `s 1078(3) share capital 1: any statement of capital and initial shareholdings` |
| s 1078(3) Share capital item 2 | 15176 | encoded | `s 1078 the document is an enhanced disclosure document` | 69 | a public company; constructor `s 1078(3) share capital 2: any return of allotment and the statement of capital accompanying it` |
| s 1078(3) Share capital item 3 | 15177 | encoded | `s 1078 the document is an enhanced disclosure document` | 69 | a public company; constructor `s 1078(3) share capital 3: copy of any resolution under section 570 or 571 (disapplication of pre-emption rights)` |
| s 1078(3) Share capital item 4 | 15178 | encoded | `s 1078 the document is an enhanced disclosure document` | 69 | a public company; constructor `s 1078(3) share capital 4: copy of any report under section 593 or 599 as to the value of a non-cash asset` |
| s 1078(3) Share capital item 5 | 15179 | encoded | `s 1078 the document is an enhanced disclosure document` | 69 | a public company; constructor `s 1078(3) share capital 5: statement of capital accompanying notice given under section 625 (notice by company of redenomination of ...` |
| s 1078(3) Share capital item 6 | 15180 | encoded | `s 1078 the document is an enhanced disclosure document` | 69 | a public company; constructor `s 1078(3) share capital 6: statement of capital accompanying notice given under section 627 (notice by company of reduction of ...` |
| s 1078(3) Share capital item 7 | 15181 | encoded | `s 1078 the document is an enhanced disclosure document` | 69 | a public company; constructor `s 1078(3) share capital 7: notice delivered under section 636 (notice of new name of class of shares) or 637 (notice of variation of ...` |
| s 1078(3) Share capital item 8 | 15182 | encoded | `s 1078 the document is an enhanced disclosure document` | 69 | a public company; constructor `s 1078(3) share capital 8: statement of capital accompanying order delivered under section 649 (order of court confirming reduction ...` |
| s 1078(3) Share capital item 9 | 15183 | encoded | `s 1078 the document is an enhanced disclosure document` | 69 | a public company; constructor `s 1078(3) share capital 9: notification (under section 689) of the redemption of shares and the statement of capital accompanying it` |
| s 1078(3) Share capital item 10 | 15184 | encoded | `s 1078 the document is an enhanced disclosure document` | 69 | a public company; constructor `s 1078(3) share capital 10: statement of capital accompanying return delivered under section 708 (notice of cancellation of shares on ...` |
| s 1078(3) Share capital item 11 | 15185 | encoded | `s 1078 the document is an enhanced disclosure document` | 69 | a public company; constructor `s 1078(3) share capital 11: any statement of compliance delivered under section 762 (statement that company meets conditions for issue ...` |
| s 1078(3) Share capital item 12 | 15186 | encoded | `s 1078 the document is an enhanced disclosure document` | 69 | a public company; constructor `s 1078(3) share capital 12: any statement delivered under section 762(1)(e) (statement of the aggregate amount paid up on shares on ...` |
| s 1078(3) group Mergers and divisions | 15187 | encoded | `s 1078 the document is an enhanced disclosure document` | 69 | a public company |
| s 1078(3) Mergers and divisions item 1 | 15188 | encoded | `s 1078 the document is an enhanced disclosure document` | 69 | a public company; constructor `s 1078(3) mergers and divisions 1: copy of any draft of the terms of a scheme required to be delivered to the registrar under section 906 or 921` |
| s 1078(3) Mergers and divisions item 2 | 15189 | encoded | `s 1078 the document is an enhanced disclosure document` | 69 | a public company; constructor `s 1078(3) mergers and divisions 2: copy of any order under section 899, 900, 901F or 901J in respect of a compromise or arrangement to which ...` |
| s 1078(3A) | 15190 | encoded | `s 1078 the document is an enhanced disclosure document` | 69 | a private company that applies to re-register as a public company; constructor `s 1078(3A): in the case of a private company which applies to re-register as a public company, the statement delivered ...` |
| s 1078(4) | 15191 | encoded | `s 1078 the document is an enhanced disclosure document` | 69 | a private company that has re-registered |
| s 1078(4)(a) | 15192 | encoded | `s 1078 the document is an enhanced disclosure document` | 69 | a private company that has re-registered; constructor `s 1078(4)(a): where a private company re-registers as a public company, the last statement of capital relating to the ...` |
| s 1078(4)(b) | 15193 | encoded | `s 1078(4)(b) the day the last statement of capital is treated as received by the registrar for the purposes of section 1077` | 2 |  |
| s 1078(4A) | 15194 | encoded | `s 1078 the document is an enhanced disclosure document` | 69 | regulation 14 of the 2014 Regulations; constructor `s 1078(4A): where a company is required by regulation 14 of the Reports on Payments to Governments Regulations 2014 to ...` |
| s 1078(4B) | 15195 | encoded | `s 1078 the document is an enhanced disclosure document` | 69 | regulation 15 of the 2014 Regulations; constructor `s 1078(4B): where a company is required by regulation 15 of the Reports on Payments to Governments Regulations 2014 to ...` |
| s 1078(5) | 15196 | encoded | `s 1078 the document is an enhanced disclosure document` | 69 | an overseas company; the documents are those specified by regulations (an input); constructor `s 1078(5): in the case of an overseas company, such particulars, returns and other documents required to be delivered ...` |
| s 1078(6) | 15197 | inert (reason 2) | - | - | procedure for regulations |
| s 1079 | 15198 | inert (reason 1) | - | - | section heading, not operative |
| s 1079(1) | 15199 | encoded | `s 1079(1) the company is barred from relying against the person on the happening of the event` | 6 | an "unless" bar (F9) |
| s 1079(1)(a) | 15200 | encoded | `s 1079(1) the company is barred from relying against the person on the happening of the event` | 6 | an "unless" bar (F9) |
| s 1079(1)(b) | 15201 | encoded | `s 1079(1) the company is barred from relying against the person on the happening of the event` | 6 | an "unless" bar (F9) |
| s 1079(2) | 15202 | encoded | `s 1079(2) the section applies to the event` | 6 | a closed list (F18) |
| s 1079(2)(a) | 15203 | encoded | `s 1079(2) the section applies to the event` | 6 | a closed list (F18) |
| s 1079(2)(b) | 15204 | encoded | `s 1079(2) the section applies to the event` | 6 | a closed list (F18) |
| s 1079(2)(c) | 15205 | encoded | `s 1079(2) the section applies to the event` | 6 | a closed list (F18) |
| s 1079(2)(d) | 15206 | encoded | `s 1079(2) the section applies to the event` | 6 | a closed list (F18) |
| s 1079(2)(e) | 15207 | encoded | `s 1079(2) the section applies to the event` | 6 | a closed list (F18) |
| s 1079(3) | 15208 | encoded | `s 1079(3) the company is barred from relying on the happening of the event against the person`; `s 1079(3) the last day of the grace period` | 9 | 15 days, and the next working day: tested on both sides |
| s 1079(3)(a) | 15209 | encoded | `s 1079(3) the company is barred from relying on the happening of the event against the person`; `s 1079(3) the last day of the grace period` | 9 | 15 days, and the next working day: tested on both sides |
| s 1079(3)(b) | 15210-15211 | encoded | `s 1079(3) the company is barred from relying on the happening of the event against the person`; `s 1079(3) the last day of the grace period` | 9 | 15 days, and the next working day: tested on both sides |
| s 1079(4) | 15212 | encoded | `s 1079(4) the event has been officially notified` | 7 | "means" |
| s 1079(4)(a) | 15213 | encoded | `s 1079(4) the event has been officially notified` | 7 | "means" |
| s 1079(4)(b) | 15214 | encoded | `s 1079(4) the event has been officially notified` | 7 | "means" |
| s 1079(4)(c) | 15215 | encoded | `s 1079(4) the event has been officially notified` | 7 | "means" |
| s 1079A | 15216-15217 | repealed or blank in this text | - | - | blank in this text |
| heading: Notice of receipt of documents about new directors | 15218 | inert (reason 1) | - | - | heading, not operative |
| s 1079B | 15219 | inert (reason 1) | - | - | section heading, not operative |
| s 1079B(1) | 15220 | encoded | `s 1079B(1) this section applies to the registration of the document` | 3 |  |
| s 1079B(1)(a) | 15221 | encoded | `s 1079B(1) this section applies to the registration of the document` | 3 |  |
| s 1079B(1)(b) | 15222 | encoded | `s 1079B(1) this section applies to the registration of the document` | 3 |  |
| s 1079B(2) | 15223 | encoded | `s 1079B(2) the registrar must notify the person`; `s 1079B(2) the registrar has notified the person as the section requires`; `s 1079B(2) the registrar's duty to notify the person named as a director` | 10 |  |
| s 1079B(2)(a) | 15224 | encoded | `s 1079B(2) the registrar must notify the person`; `s 1079B(2) the registrar has notified the person as the section requires`; `s 1079B(2) the registrar's duty to notify the person named as a director` | 10 |  |
| s 1079B(2)(b) | 15225 | encoded | `s 1079B(2) the registrar must notify the person`; `s 1079B(2) the registrar has notified the person as the section requires`; `s 1079B(2) the registrar's duty to notify the person named as a director` | 10 |  |
| s 1079B(3) | 15226 | encoded | `s 1079B(3) the notice contains what it must` | 3 |  |
| s 1079B(3)(a) | 15227 | encoded | `s 1079B(3) the notice contains what it must` | 3 |  |
| s 1079B(3)(b) | 15228 | encoded | `s 1079B(3) the notice contains what it must` | 3 |  |
| s 1079B(4) | 15229 | encoded | `s 1079B(4) the notice may be sent in the form to the address` | 4 |  |
| heading: The register | 15230 | inert (reason 1) | - | - | heading, not operative |
| s 1080 | 15231 | inert (reason 1) | - | - | section heading, not operative |
| s 1080(1) | 15232 | encoded | `s 1080(1) the registrar must keep records of the matter`; `s 1080(1) the registrar's duty to keep records` | 5 | the double comma in (a) is a text anomaly (finding) |
| s 1080(1)(a) | 15233 | encoded | `s 1080(1) the registrar must keep records of the matter`; `s 1080(1) the registrar's duty to keep records` | 5 | the double comma in (a) is a text anomaly (finding) |
| s 1080(1)(b) | 15234 | encoded | `s 1080(1) the registrar must keep records of the matter`; `s 1080(1) the registrar's duty to keep records` | 5 | the double comma in (a) is a text anomaly (finding) |
| s 1080(2) | 15235 | encoded | `s 1080(2) the record is part of the register` | 3 | "the register" |
| s 1080(3) | 15236 | encoded | `s 1080(3) the information is kept as the subsection requires`; `s 1080(3) the registrar's duty to keep information from an enhanced disclosure document in electronic form` | 5 |  |
| s 1080(4) | 15237-15238 | encoded | `s 1080(4) the information may be recorded and kept in the form`; `s 1080(4) the recording and keeping is sufficient compliance with the registrar's duty to keep, file or register the document or to record the information` | 8 |  |
| s 1080(5) | 15239 | encoded | `s 1080(5) the records are such as the subsection requires` | 3 |  |
| s 1081 | 15240 | inert (reason 1) | - | - | section heading, not operative |
| s 1081(1) | 15241 | encoded | `s 1081(1) what the note in the register must record`; `s 1081(1) the registrar's duty to place a note in the register` | 8 |  |
| s 1081(1)(a) | 15242 | encoded | `s 1081(1) what the note in the register must record`; `s 1081(1) the registrar's duty to place a note in the register` | 8 |  |
| s 1081(1)(b) | 15243 | repealed or blank in this text | - | - | blank in this text |
| s 1081(1)(c) | 15244 | encoded | `s 1081(1) what the note in the register must record`; `s 1081(1) the registrar's duty to place a note in the register` | 8 |  |
| s 1081(1)(d) | 15245 | encoded | `s 1081(1) what the note in the register must record`; `s 1081(1) the registrar's duty to place a note in the register` | 8 |  |
| s 1081(1)(d)(i) | 15246 | encoded | `s 1081(1) what the note in the register must record`; `s 1081(1) the registrar's duty to place a note in the register` | 8 |  |
| s 1081(1)(d)(ii) | 15247 | encoded | `s 1081(1) what the note in the register must record`; `s 1081(1) the registrar's duty to place a note in the register` | 8 |  |
| s 1081(1)(d)(iii) | 15248 | encoded | `s 1081(1) what the note in the register must record`; `s 1081(1) the registrar's duty to place a note in the register` | 8 |  |
| s 1081(1)(e) | 15249 | encoded | `s 1081(1) what the note in the register must record`; `s 1081(1) the registrar's duty to place a note in the register` | 8 |  |
| s 1081(1)(f) | 15250 | encoded | `s 1081(1) what the note in the register must record`; `s 1081(1) the registrar's duty to place a note in the register` | 8 |  |
| s 1081(1A) | 15251 | repealed or blank in this text | - | - | blank in this text |
| s 1081(2) | 15252 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1081(2)(a) | 15253 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1081(2)(b) | 15254 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1081(3) | 15255 | encoded | `s 1081(3) an annotation is required for the document` | 2 |  |
| s 1081(4) | 15256 | fork | `s 1081(4) the note may be removed` | 2 | F30: a grant named "may" with an "if" gate; a failed "if" answers NOTHING (name-test sweep) |
| s 1081(5) | 15257 | encoded | `s 1081(5) the registrar's duty or power with respect to annotation yields to the court's direction` | 4 |  |
| s 1081(5)(a) | 15258 | encoded | `s 1081(5) the registrar's duty or power with respect to annotation yields to the court's direction` | 4 |  |
| s 1081(5)(b) | 15259 | encoded | `s 1081(5) the registrar's duty or power with respect to annotation yields to the court's direction` | 4 |  |
| s 1081(6) | 15260 | encoded | `s 1081(6) the note is part of the register for all purposes of the Companies Acts` | 2 |  |
| s 1081(7) | 15261 | inert (reason 2) | - | - | procedure for regulations |
| s 1081A | 15262 | inert (reason 1) | - | - | section heading, not operative |
| s 1081A(1) | 15263-15271 | encoded | `s 1081A(1) the registrar must seek to promote the objective`; `s 1081A(1) the registrar's duty to seek to promote the objectives` | 10 | the four objectives are constructors |
| s 1081A(1) Objective 1 | 15264-15265 | encoded | `s 1081A(1) the registrar must seek to promote the objective`; `s 1081A(1) the registrar's duty to seek to promote the objectives` | 10 | the four objectives are constructors |
| s 1081A(1) Objective 2 | 15266-15267 | encoded | `s 1081A(1) the registrar must seek to promote the objective`; `s 1081A(1) the registrar's duty to seek to promote the objectives` | 10 | the four objectives are constructors |
| s 1081A(1) Objective 3 | 15268-15269 | encoded | `s 1081A(1) the registrar must seek to promote the objective`; `s 1081A(1) the registrar's duty to seek to promote the objectives` | 10 | the four objectives are constructors |
| s 1081A(1) Objective 4 | 15270-15271 | encoded | `s 1081A(1) the registrar must seek to promote the objective`; `s 1081A(1) the registrar's duty to seek to promote the objectives` | 10 | the four objectives are constructors |
| s 1081A(1)(a) | 15272 | encoded | `s 1081A(1) the registrar must seek to promote the objective`; `s 1081A(1) the registrar's duty to seek to promote the objectives` | 10 | the four objectives are constructors |
| s 1081A(1)(b) | 15273 | encoded | `s 1081A(1) the registrar must seek to promote the objective`; `s 1081A(1) the registrar's duty to seek to promote the objectives` | 10 | the four objectives are constructors |
| s 1081A(2) | 15274 | encoded | `s 1081A(2) the reference to the register in Objective 2 includes the records` | 2 | "includes" |
| s 1082 | 15275 | inert (reason 1) | - | - | section heading, not operative |
| s 1082(1) | 15276 | encoded | `s 1082(1) regulations may provide for a unique identifier to identify the person` | 6 | "unique identifiers": the positions the scheme covers |
| s 1082(1)(a) | 15277 | encoded | `s 1082(1) regulations may provide for a unique identifier to identify the person` | 6 | "unique identifiers": the positions the scheme covers |
| s 1082(1)(b) | 15278 | encoded | `s 1082(1) regulations may provide for a unique identifier to identify the person` | 6 | "unique identifiers": the positions the scheme covers |
| s 1082(1)(ba) | 15279 | encoded | `s 1082(1) regulations may provide for a unique identifier to identify the person` | 6 | "unique identifiers": the positions the scheme covers |
| s 1082(1)(bb) | 15280 | encoded | `s 1082(1) regulations may provide for a unique identifier to identify the person` | 6 | "unique identifiers": the positions the scheme covers |
| s 1082(1)(c) | 15281 | encoded | `s 1082(1) regulations may provide for a unique identifier to identify the person` | 6 | "unique identifiers": the positions the scheme covers |
| s 1082(2) | 15282 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1082(2)(a) | 15283 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1082(2)(b) | 15284 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1082(2)(c) | 15285 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1082(2)(c)(i) | 15286 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1082(2)(c)(ii) | 15287 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1082(2)(d) | 15288 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1082(2)(d)(i) | 15289 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1082(2)(d)(ii) | 15290 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1082(3) | 15291 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1082(4) | 15292 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1082(5) | 15293 | inert (reason 2) | - | - | procedure for regulations |
| s 1083 | 15294 | inert (reason 1) | - | - | section heading, not operative |
| s 1083(1) | 15295-15296 | fork | `s 1083(1) the registrar may destroy the original` | 7 | F14: the text carries "This is subject to" twice (old and new wording); F15: the two years are counted to the second anniversary of receipt |
| s 1083(1)(a) | 15297 | fork | `s 1083(1) the registrar may destroy the original` | 7 | F14: the text carries "This is subject to" twice (old and new wording); F15: the two years are counted to the second anniversary of receipt |
| s 1083(1)(b) | 15298 | fork | `s 1083(1) the registrar may destroy the original` | 7 | F14: the text carries "This is subject to" twice (old and new wording); F15: the two years are counted to the second anniversary of receipt |
| s 1083(1)(c) | 15299 | fork | `s 1083(1) the registrar may destroy the original` | 7 | F14: the text carries "This is subject to" twice (old and new wording); F15: the two years are counted to the second anniversary of receipt |
| s 1083(2) | 15300 | encoded | `s 1083(2) the registrar is under no obligation to keep the original` | 4 |  |
| s 1083(3) | 15301 | inert (reason 2) | - | - | a transitional provision (documents held when the section came into force) that affects no one now |
| s 1084 | 15302 | inert (reason 1) | - | - | section heading, not operative |
| s 1084(1) | 15303 | encoded | `s 1084(1) this section applies`; `s 1084(1) the relevant date` | 8 | "the relevant date" is the date of the occasion |
| s 1084(1)(a) | 15304 | encoded | `s 1084(1) this section applies`; `s 1084(1) the relevant date` | 8 | "the relevant date" is the date of the occasion |
| s 1084(1)(b) | 15305 | encoded | `s 1084(1) this section applies`; `s 1084(1) the relevant date` | 8 | "the relevant date" is the date of the occasion |
| s 1084(1)(c) | 15306-15307 | encoded | `s 1084(1) this section applies`; `s 1084(1) the relevant date` | 8 | "the relevant date" is the date of the occasion |
| s 1084(1A) | 15308 | encoded | `s 1084(1A) the registrar need not make the information available for public inspection on the day` | 5 | 20 years (F12) |
| s 1084(2) | 15309 | encoded | `s 1084(2) the registrar of companies for England and Wales may direct that the records be removed to the Public Record Office on the day` | 5 | two years (F12) |
| s 1084(2AA) | 15310 | encoded | `s 1084(2AA) the registrar of companies for Northern Ireland may direct that the records be removed to the Public Record Office of Northern Ireland on the day` | 3 | two years (F12) |
| s 1084(3) | 15311 | fork | `s 1084(3) the records are to be disposed of under the enactments relating to the Public Record Office` | 2 | F19: refers to "subsection (2) or (2A)" and the text has (2) and (2AA) only; read as both |
| s 1084(4) | 15312 | encoded | `s 1084(4) the body is a company for the purposes of subsection (1)(a)` | 2 | "includes" |
| s 1084(4A) | 15313 | repealed or blank in this text | - | - | blank in this text |
| s 1084(5) | 15314 | repealed or blank in this text | - | - | blank in this text |
| s 1084A | 15315 | inert (reason 1) | - | - | section heading, not operative |
| s 1084A(1) | 15316 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1084A(2) | 15317 | encoded | `s 1084A(2) the information is optional information` | 4 | "means" |
| s 1084A(3) | 15318 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1084A(3)(a) | 15319 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1084A(3)(b) | 15320 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1084A(4) | 15321 | inert (reason 2) | - | - | procedure for regulations |
| heading: Inspection etc of the register | 15322 | inert (reason 1) | - | - | heading, not operative |
| s 1085 | 15323 | inert (reason 1) | - | - | section heading, not operative |
| s 1085(1) | 15324 | encoded | `s 1085(1) the person may inspect the material on the register`; `s 1085(1) the right of any person to inspect the register` | 5 | a right of any person: decision function and regulative rule |
| s 1085(2) | 15325-15326 | encoded | `s 1085(2) the right of inspection extends to the original` | 5 | "if, and only if"; the second sentence is a cross-reference to section 1083(1) (F6) |
| s 1085(3) | 15327-15330 | encoded | `s 1085(1) the person may inspect the material on the register` | 4 | the provisions named are the second input of the function above |
| s 1086 | 15331 | inert (reason 1) | - | - | section heading, not operative |
| s 1086(1) | 15332 | encoded | `s 1086(1) the person may require a copy of the material`; `s 1086(1) the right of any person to a copy of material on the register` | 4 |  |
| s 1086(2) | 15333 | encoded | `s 1086(2) the fee complies with the limit` | 4 |  |
| s 1086(3) | 15334 | repealed or blank in this text | - | - | blank in this text |
| s 1087 | 15335 | inert (reason 1) | - | - | section heading, not operative |
| s 1087(1) | 15336 | encoded | `s 1087(1) the registrar must not make the material available for public inspection`; `s 1087(1) the prohibition on making protected material available for public inspection` | 44 | each head is a constructor (the list is not closed: NOTHING for other material); (h) and the unlabelled lines of (gd) are rows |
| s 1087(1)(za) | 15337 | encoded | `s 1087(1) the registrar must not make the material available for public inspection`; `s 1087(1) the prohibition on making protected material available for public inspection` | 44 | each head is a constructor (the list is not closed: NOTHING for other material); (h) and the unlabelled lines of (gd) are rows; constructors for (za(i)), (za(ii)) |
| s 1087(1)(za)(i) | 15338 | encoded | `s 1087(1) the registrar must not make the material available for public inspection`; `s 1087(1) the prohibition on making protected material available for public inspection` | 44 | each head is a constructor (the list is not closed: NOTHING for other material); (h) and the unlabelled lines of (gd) are rows; constructor `s 1087(1)(za(i)) an email address delivered to the registrar under section 9(5)(aa) or 88B (initial registered email address and change of address)` |
| s 1087(1)(za)(ii) | 15339 | encoded | `s 1087(1) the registrar must not make the material available for public inspection`; `s 1087(1) the prohibition on making protected material available for public inspection` | 44 | each head is a constructor (the list is not closed: NOTHING for other material); (h) and the unlabelled lines of (gd) are rows; constructor `s 1087(1)(za(ii)) an email address delivered to the registrar under section 30 of the Economic Crime and Corporate Transparency Act 2023 (company's registered email address: transitional provision)` |
| s 1087(1)(a) | 15340 | encoded | `s 1087(1) the registrar must not make the material available for public inspection`; `s 1087(1) the prohibition on making protected material available for public inspection` | 44 | each head is a constructor (the list is not closed: NOTHING for other material); (h) and the unlabelled lines of (gd) are rows; constructor `s 1087(1)(a) the contents of any document sent to the registrar containing views expressed pursuant to section 56 (comments on proposal by company to use certain words or expressions in company name)` |
| s 1087(1)(aa) | 15341 | encoded | `s 1087(1) the registrar must not make the material available for public inspection`; `s 1087(1) the prohibition on making protected material available for public inspection` | 44 | each head is a constructor (the list is not closed: NOTHING for other material); (h) and the unlabelled lines of (gd) are rows; constructor `s 1087(1)(aa) any application or other document delivered to the registrar under regulations under section 120A (protection of individual membership information)` |
| s 1087(1)(b) | 15342 | encoded | `s 1087(1) the registrar must not make the material available for public inspection`; `s 1087(1) the prohibition on making protected material available for public inspection` | 44 | each head is a constructor (the list is not closed: NOTHING for other material); (h) and the unlabelled lines of (gd) are rows; constructor `s 1087(1)(b) protected information within section 242(1) (directors' residential addresses: restriction on disclosure by registrar) or any corresponding provision of regulations under section 1046 (overseas companies)` |
| s 1087(1)(ba) | 15343 | encoded | `s 1087(1) the registrar must not make the material available for public inspection`; `s 1087(1) the prohibition on making protected material available for public inspection` | 44 | each head is a constructor (the list is not closed: NOTHING for other material); (h) and the unlabelled lines of (gd) are rows; constructors for (ba(i)), (ba(ii)) |
| s 1087(1)(ba)(i) | 15344 | encoded | `s 1087(1) the registrar must not make the material available for public inspection`; `s 1087(1) the prohibition on making protected material available for public inspection` | 44 | each head is a constructor (the list is not closed: NOTHING for other material); (h) and the unlabelled lines of (gd) are rows; constructor `s 1087(1)(ba(i)) representations received by the registrar in response to a notice under section 245(2) (notice of proposal to put director's usual residential address on the public record)` |
| s 1087(1)(ba)(ii) | 15345 | encoded | `s 1087(1) the registrar must not make the material available for public inspection`; `s 1087(1) the prohibition on making protected material available for public inspection` | 44 | each head is a constructor (the list is not closed: NOTHING for other material); (h) and the unlabelled lines of (gd) are rows; constructor `s 1087(1)(ba(ii)) representations received by the registrar in response to a notice under any corresponding provision of regulations under section 1046 (overseas companies)` |
| s 1087(1)(bb) | 15346 | encoded | `s 1087(1) the registrar must not make the material available for public inspection`; `s 1087(1) the prohibition on making protected material available for public inspection` | 44 | each head is a constructor (the list is not closed: NOTHING for other material); (h) and the unlabelled lines of (gd) are rows; constructor `s 1087(1)(bb) information to which sections 240 to 244 are applied by section 790ZF(1) (residential addresses of people with significant control over the company) or any corresponding provision of regulations under section 1046 (overseas companies)` |
| s 1087(1)(bba) | 15347 | encoded | `s 1087(1) the registrar must not make the material available for public inspection`; `s 1087(1) the prohibition on making protected material available for public inspection` | 44 | each head is a constructor (the list is not closed: NOTHING for other material); (h) and the unlabelled lines of (gd) are rows; constructors for (bba(i)), (bba(ii)) |
| s 1087(1)(bba)(i) | 15348 | encoded | `s 1087(1) the registrar must not make the material available for public inspection`; `s 1087(1) the prohibition on making protected material available for public inspection` | 44 | each head is a constructor (the list is not closed: NOTHING for other material); (h) and the unlabelled lines of (gd) are rows; constructor `s 1087(1)(bba(i)) any application or other document delivered to the registrar under regulations under section 468A (regulations protecting profit and loss accounts for certain companies)` |
| s 1087(1)(bba)(ii) | 15349 | encoded | `s 1087(1) the registrar must not make the material available for public inspection`; `s 1087(1) the prohibition on making protected material available for public inspection` | 44 | each head is a constructor (the list is not closed: NOTHING for other material); (h) and the unlabelled lines of (gd) are rows; constructor `s 1087(1)(bba(ii)) any information which regulations under section 468A require not to be made available for public inspection` |
| s 1087(1)(bc) | 15350 | encoded | `s 1087(1) the registrar must not make the material available for public inspection`; `s 1087(1) the prohibition on making protected material available for public inspection` | 44 | each head is a constructor (the list is not closed: NOTHING for other material); (h) and the unlabelled lines of (gd) are rows; constructor `s 1087(1)(bc) any application or other document delivered to the registrar under regulations under section 790ZG (protection of PSC information)` |
| s 1087(1)(c) | 15351 | encoded | `s 1087(1) the registrar must not make the material available for public inspection`; `s 1087(1) the prohibition on making protected material available for public inspection` | 44 | each head is a constructor (the list is not closed: NOTHING for other material); (h) and the unlabelled lines of (gd) are rows; constructor `s 1087(1)(c) any application to the registrar under section 1024 (application for administrative restoration to the register) that has not yet been determined or was not successful` |
| s 1087(1)(d) | 15352 | encoded | `s 1087(1) the registrar must not make the material available for public inspection`; `s 1087(1) the prohibition on making protected material available for public inspection` | 44 | each head is a constructor (the list is not closed: NOTHING for other material); (h) and the unlabelled lines of (gd) are rows; constructor `s 1087(1)(d) any document received by the registrar in connection with the giving or withdrawal of consent under section 1075 (informal correction of documents) before the repeal of that section by the Economic Crime and Corporate Transparency Act 2023` |
| s 1087(1)(dza) | 15353 | encoded | `s 1087(1) the registrar must not make the material available for public inspection`; `s 1087(1) the prohibition on making protected material available for public inspection` | 44 | each head is a constructor (the list is not closed: NOTHING for other material); (h) and the unlabelled lines of (gd) are rows; constructor `s 1087(1)(dza) any statement made in accordance with regulations made by virtue of section 1082(2)(c)` |
| s 1087(1)(da) | 15354 | encoded | `s 1087(1) the registrar must not make the material available for public inspection`; `s 1087(1) the prohibition on making protected material available for public inspection` | 44 | each head is a constructor (the list is not closed: NOTHING for other material); (h) and the unlabelled lines of (gd) are rows; constructor `s 1087(1)(da) relevant date of birth information that section 1087A provides is not to be made available for public inspection` |
| s 1087(1)(e) | 15355 | encoded | `s 1087(1) the registrar must not make the material available for public inspection`; `s 1087(1) the prohibition on making protected material available for public inspection` | 44 | each head is a constructor (the list is not closed: NOTHING for other material); (h) and the unlabelled lines of (gd) are rows; constructors for (e(i)), (e(ii)) |
| s 1087(1)(e)(i) | 15356 | encoded | `s 1087(1) the registrar must not make the material available for public inspection`; `s 1087(1) the prohibition on making protected material available for public inspection` | 44 | each head is a constructor (the list is not closed: NOTHING for other material); (h) and the unlabelled lines of (gd) are rows; constructor `s 1087(1)(e(i)) any application or other document delivered to the registrar under regulations under section 1088 (regulations protecting material), other than information provided by virtue of section 1088(5)` |
| s 1087(1)(e)(ii) | 15357 | encoded | `s 1087(1) the registrar must not make the material available for public inspection`; `s 1087(1) the prohibition on making protected material available for public inspection` | 44 | each head is a constructor (the list is not closed: NOTHING for other material); (h) and the unlabelled lines of (gd) are rows; constructor `s 1087(1)(e(ii)) any information which regulations under section 1088 require not to be made available for public inspection` |
| s 1087(1)(ea) | 15358 | encoded | `s 1087(1) the registrar must not make the material available for public inspection`; `s 1087(1) the prohibition on making protected material available for public inspection` | 44 | each head is a constructor (the list is not closed: NOTHING for other material); (h) and the unlabelled lines of (gd) are rows; constructor `s 1087(1)(ea) any information provided to the registrar under section 1092A (power to require further information)` |
| s 1087(1)(f) | 15359 | encoded | `s 1087(1) the registrar must not make the material available for public inspection`; `s 1087(1) the prohibition on making protected material available for public inspection` | 44 | each head is a constructor (the list is not closed: NOTHING for other material); (h) and the unlabelled lines of (gd) are rows; constructor `s 1087(1)(f) any application or other document delivered to the registrar under section 1094 (removal of material from the register)` |
| s 1087(1)(g) | 15360 | encoded | `s 1087(1) the registrar must not make the material available for public inspection`; `s 1087(1) the prohibition on making protected material available for public inspection` | 44 | each head is a constructor (the list is not closed: NOTHING for other material); (h) and the unlabelled lines of (gd) are rows; constructor `s 1087(1)(g) any court order under section 1096 (rectification of the register under court order) that the court has directed under section 1097 is not to be made available for public inspection` |
| s 1087(1)(ga) | 15361 | encoded | `s 1087(1) the registrar must not make the material available for public inspection`; `s 1087(1) the prohibition on making protected material available for public inspection` | 44 | each head is a constructor (the list is not closed: NOTHING for other material); (h) and the unlabelled lines of (gd) are rows; constructor `s 1087(1)(ga) any application or other document delivered to the registrar under section 1097A, 1097B or 1097C (rectification of registered office, service address or principal office address) other than an order or direction of the court` |
| s 1087(1)(gb) | 15362 | encoded | `s 1087(1) the registrar must not make the material available for public inspection`; `s 1087(1) the prohibition on making protected material available for public inspection` | 44 | each head is a constructor (the list is not closed: NOTHING for other material); (h) and the unlabelled lines of (gd) are rows; constructor `s 1087(1)(gb) any application or other document delivered to the registrar under section 1098B, 1098D or 1098E or regulations under section 1098G (authorised corporate service providers)` |
| s 1087(1)(gc) | 15363 | encoded | `s 1087(1) the registrar must not make the material available for public inspection`; `s 1087(1) the prohibition on making protected material available for public inspection` | 44 | each head is a constructor (the list is not closed: NOTHING for other material); (h) and the unlabelled lines of (gd) are rows; constructor `s 1087(1)(gc) any document delivered to the registrar under regulations under section 1110B` |
| s 1087(1)(gd) | 15364-15374 | encoded | `s 1087(1) the registrar must not make the material available for public inspection`; `s 1087(1) the prohibition on making protected material available for public inspection` | 44 | each head is a constructor (the list is not closed: NOTHING for other material); (h) and the unlabelled lines of (gd) are rows |
| s 1087(1)(gd) list row 1 | 15365 | encoded | `s 1087(1) the registrar must not make the material available for public inspection`; `s 1087(1) the prohibition on making protected material available for public inspection` | 44 | each head is a constructor (the list is not closed: NOTHING for other material); (h) and the unlabelled lines of (gd) are rows; constructor `s 1087(1)(gd, section 12(2A)) a statement or other document delivered to the registrar by virtue of section 12(2A) (identity verification)` |
| s 1087(1)(gd) list row 2 | 15366 | encoded | `s 1087(1) the registrar must not make the material available for public inspection`; `s 1087(1) the prohibition on making protected material available for public inspection` | 44 | each head is a constructor (the list is not closed: NOTHING for other material); (h) and the unlabelled lines of (gd) are rows; constructor `s 1087(1)(gd, section 12B(2) to (4)) a statement or other document delivered to the registrar by virtue of section 12B(2) to (4) (identity verification)` |
| s 1087(1)(gd) list row 3 | 15367 | encoded | `s 1087(1) the registrar must not make the material available for public inspection`; `s 1087(1) the prohibition on making protected material available for public inspection` | 44 | each head is a constructor (the list is not closed: NOTHING for other material); (h) and the unlabelled lines of (gd) are rows; constructor `s 1087(1)(gd, section 167G(3)(c)) a statement or other document delivered to the registrar by virtue of section 167G(3)(c) (identity verification)` |
| s 1087(1)(gd) list row 4 | 15368 | encoded | `s 1087(1) the registrar must not make the material available for public inspection`; `s 1087(1) the prohibition on making protected material available for public inspection` | 44 | each head is a constructor (the list is not closed: NOTHING for other material); (h) and the unlabelled lines of (gd) are rows; constructor `s 1087(1)(gd, section 790LB(1) to (3)) a statement or other document delivered to the registrar by virtue of section 790LB(1) to (3) (identity verification)` |
| s 1087(1)(gd) list row 5 | 15369 | encoded | `s 1087(1) the registrar must not make the material available for public inspection`; `s 1087(1) the prohibition on making protected material available for public inspection` | 44 | each head is a constructor (the list is not closed: NOTHING for other material); (h) and the unlabelled lines of (gd) are rows; constructor `s 1087(1)(gd, section 790LM(2)) a statement or other document delivered to the registrar by virtue of section 790LM(2) (identity verification)` |
| s 1087(1)(gd) list row 6 | 15370 | encoded | `s 1087(1) the registrar must not make the material available for public inspection`; `s 1087(1) the prohibition on making protected material available for public inspection` | 44 | each head is a constructor (the list is not closed: NOTHING for other material); (h) and the unlabelled lines of (gd) are rows; constructor `s 1087(1)(gd, section 790LN(2)) a statement or other document delivered to the registrar by virtue of section 790LN(2) (identity verification)` |
| s 1087(1)(gd) list row 7 | 15371 | encoded | `s 1087(1) the registrar must not make the material available for public inspection`; `s 1087(1) the prohibition on making protected material available for public inspection` | 44 | each head is a constructor (the list is not closed: NOTHING for other material); (h) and the unlabelled lines of (gd) are rows; constructor `s 1087(1)(gd, section 790LO(2)) a statement or other document delivered to the registrar by virtue of section 790LO(2) (identity verification)` |
| s 1087(1)(gd) list row 8 | 15372 | encoded | `s 1087(1) the registrar must not make the material available for public inspection`; `s 1087(1) the prohibition on making protected material available for public inspection` | 44 | each head is a constructor (the list is not closed: NOTHING for other material); (h) and the unlabelled lines of (gd) are rows; constructor `s 1087(1)(gd, section 790LP(2)) a statement or other document delivered to the registrar by virtue of section 790LP(2) (identity verification)` |
| s 1087(1)(gd) list row 9 | 15373 | encoded | `s 1087(1) the registrar must not make the material available for public inspection`; `s 1087(1) the prohibition on making protected material available for public inspection` | 44 | each head is a constructor (the list is not closed: NOTHING for other material); (h) and the unlabelled lines of (gd) are rows; constructor `s 1087(1)(gd, section 790LS(1) to (3)) a statement or other document delivered to the registrar by virtue of section 790LS(1) to (3) (identity verification)` |
| s 1087(1)(gd) list row 10 | 15374 | encoded | `s 1087(1) the registrar must not make the material available for public inspection`; `s 1087(1) the prohibition on making protected material available for public inspection` | 44 | each head is a constructor (the list is not closed: NOTHING for other material); (h) and the unlabelled lines of (gd) are rows; constructor `s 1087(1)(gd, section 1067A) a statement or other document delivered to the registrar by virtue of section 1067A (identity verification)` |
| s 1087(1)(h) | 15375 | repealed or blank in this text | - | - | blank in this text |
| s 1087(1)(i) | 15376 | encoded | `s 1087(1) the registrar must not make the material available for public inspection`; `s 1087(1) the prohibition on making protected material available for public inspection` | 44 | each head is a constructor (the list is not closed: NOTHING for other material); (h) and the unlabelled lines of (gd) are rows; constructor `s 1087(1)(i) any e-mail address, identification code or password deriving from a document delivered for the purpose of authorising or facilitating electronic filing procedures or providing information by telephone` |
| s 1087(1)(j) | 15377 | encoded | `s 1087(1) the registrar must not make the material available for public inspection`; `s 1087(1) the prohibition on making protected material available for public inspection` | 44 | each head is a constructor (the list is not closed: NOTHING for other material); (h) and the unlabelled lines of (gd) are rows; constructors for (j(i)), (j(ii)), (j(iii)) |
| s 1087(1)(j)(i) | 15378 | encoded | `s 1087(1) the registrar must not make the material available for public inspection`; `s 1087(1) the prohibition on making protected material available for public inspection` | 44 | each head is a constructor (the list is not closed: NOTHING for other material); (h) and the unlabelled lines of (gd) are rows; constructor `s 1087(1)(j(i)) the contents of any documents held by the registrar pending a decision of the Regulator of Community Interest Companies under section 36A of the Companies (Audit, Investigations and Community Enterprise) Act 2004 (eligibility for registration as community interest company), that the registrar is not later required to record` |
| s 1087(1)(j)(ii) | 15379 | encoded | `s 1087(1) the registrar must not make the material available for public inspection`; `s 1087(1) the prohibition on making protected material available for public inspection` | 44 | each head is a constructor (the list is not closed: NOTHING for other material); (h) and the unlabelled lines of (gd) are rows; constructor `s 1087(1)(j(ii)) the contents of any documents held by the registrar pending a decision of the Regulator of Community Interest Companies under section 38 of that Act (eligibility for conversion to community interest company), that the registrar is not later required to record` |
| s 1087(1)(j)(iii) | 15380-15381 | encoded | `s 1087(1) the registrar must not make the material available for public inspection`; `s 1087(1) the prohibition on making protected material available for public inspection` | 44 | each head is a constructor (the list is not closed: NOTHING for other material); (h) and the unlabelled lines of (gd) are rows; constructor `s 1087(1)(j(iii)) the contents of any documents held by the registrar pending a decision of the Regulator of Community Interest Companies under section 55 of that Act (eligibility for conversion from community interest company to charity), that the registrar is not later required to record` |
| s 1087(1)(ja) | 15382 | encoded | `s 1087(1) the registrar must not make the material available for public inspection`; `s 1087(1) the prohibition on making protected material available for public inspection` | 44 | each head is a constructor (the list is not closed: NOTHING for other material); (h) and the unlabelled lines of (gd) are rows; constructor `s 1087(1)(ja) any record of the information contained in a document (or part of a document) mentioned in any of the previous paragraphs of this subsection` |
| s 1087(1)(k) | 15383 | encoded | `s 1087(1) the registrar must not make the material available for public inspection`; `s 1087(1) the prohibition on making protected material available for public inspection` | 44 | each head is a constructor (the list is not closed: NOTHING for other material); (h) and the unlabelled lines of (gd) are rows; constructor `s 1087(1)(k) any other material excluded from public inspection by or under any other enactment` |
| s 1087(2) | 15384 | encoded | `s 1087(2) the restriction affects the availability for public inspection of the same information in the other material` | 3 |  |
| s 1087(3) | 15385 | encoded | `s 1087(3) the registrar need not retain the material for longer` | 3 |  |
| s 1087ZA | 15386-15387 | repealed or blank in this text | - | - | blank in this text |
| s 1087A | 15388 | inert (reason 1) | - | - | section heading, not operative |
| s 1087A(1) | 15389 | encoded | `s 1087A(1) the registrar must not make the material available for public inspection`; `s 1087A(1) the prohibition on making relevant date of birth information available for public inspection` | 5 |  |
| s 1087A(1)(a) | 15390 | encoded | `s 1087A(1) the registrar must not make the material available for public inspection`; `s 1087A(1) the prohibition on making relevant date of birth information available for public inspection` | 5 |  |
| s 1087A(1)(b) | 15391 | encoded | `s 1087A(1) the registrar must not make the material available for public inspection`; `s 1087A(1) the prohibition on making relevant date of birth information available for public inspection` | 5 |  |
| s 1087A(2) | 15392 | inert (reason 1) | - | - | a signpost to section 1087B (F6) |
| s 1087A(3) | 15393 | encoded | `s 1087A(3) the information is relevant date of birth information` | 5 | "means" |
| s 1087A(3)(a) | 15394 | encoded | `s 1087A(3) the information is relevant date of birth information` | 5 | "means" |
| s 1087A(3)(b) | 15395 | encoded | `s 1087A(3) the information is relevant date of birth information` | 5 | "means" |
| s 1087A(4) | 15396 | encoded | `s 1087A(4) the information has ceased to be relevant date of birth information` | 2 |  |
| s 1087A(5) | 15397 | encoded | `s 1087A(5) subsection (1)(b) affects the availability of the same information in that material` | 2 |  |
| s 1087A(6) | 15398 | encoded | `s 1087A(6) the person is a registrable person in relation to the company` | 3 | defined by section 790C(4) (input) |
| s 1087B | 15399 | inert (reason 1) | - | - | section heading, not operative |
| s 1087B(1) | 15400 | encoded | `s 1087B section 1087A applies to the old document` | 18 | the limits of (2) to (4) are one function |
| s 1087B(2) | 15401 | encoded | `s 1087B section 1087A applies to the old document` | 18 |  |
| s 1087B(3) | 15402 | encoded | `s 1087B section 1087A applies to the old document` | 18 |  |
| s 1087B(3)(a) | 15403 | encoded | `s 1087B section 1087A applies to the old document` | 18 |  |
| s 1087B(3)(b) | 15404 | encoded | `s 1087B section 1087A applies to the old document` | 18 |  |
| s 1087B(3)(c) | 15405 | encoded | `s 1087B section 1087A applies to the old document` | 18 |  |
| s 1087B(3)(d) | 15406 | encoded | `s 1087B section 1087A applies to the old document` | 18 |  |
| s 1087B(3)(e) | 15407 | encoded | `s 1087B section 1087A applies to the old document` | 18 |  |
| s 1087B(4) | 15408 | encoded | `s 1087B section 1087A applies to the old document` | 18 | outside the limits the text is silent (F16) |
| s 1087B(4)(a) | 15409 | encoded | `s 1087B section 1087A applies to the old document` | 18 | outside the limits the text is silent (F16) |
| s 1087B(4)(a)(i) | 15410 | encoded | `s 1087B section 1087A applies to the old document` | 18 | outside the limits the text is silent (F16) |
| s 1087B(4)(a)(ii) | 15411 | encoded | `s 1087B section 1087A applies to the old document` | 18 | outside the limits the text is silent (F16) |
| s 1087B(4)(b) | 15412 | encoded | `s 1087B section 1087A applies to the old document` | 18 | outside the limits the text is silent (F16) |
| s 1087B(4)(c) | 15413 | encoded | `s 1087B section 1087A applies to the old document` | 18 | outside the limits the text is silent (F16) |
| s 1087B(5) | 15414 | encoded | `s 1087B(5) the reference is to the provision as it had effect at the time at which the document was delivered` | 2 |  |
| s 1087C | 15415 | inert (reason 1) | - | - | section heading, not operative |
| s 1087C(1) | 15416 | encoded | `s 1087C(1) the registrar is barred from disclosing the relevant date of birth information`; `s 1087C(1) the prohibition on disclosing relevant date of birth information` | 7 | an "except" bar (F9) |
| s 1087C(1)(a) | 15417 | encoded | `s 1087C(1) the registrar is barred from disclosing the relevant date of birth information`; `s 1087C(1) the prohibition on disclosing relevant date of birth information` | 7 | an "except" bar (F9) |
| s 1087C(1)(b) | 15418 | encoded | `s 1087C(1) the registrar is barred from disclosing the relevant date of birth information`; `s 1087C(1) the prohibition on disclosing relevant date of birth information` | 7 | an "except" bar (F9) |
| s 1087C(2) | 15419 | fork | `s 1087C(2) the registrar may disclose the relevant date of birth information` | 2 | F31: a grant named "may" with an "if" gate; a failed "if" answers NOTHING (name-test sweep) |
| s 1087C(3) | 15420 | encoded | `s 1087C(3) the registrar may disclose the relevant date of birth information to the recipient` | 5 |  |
| s 1087C(4) | 15421 | encoded | `s 1087C(3) the registrar may disclose the relevant date of birth information to the recipient` | 5 | the section 243 conditions are the second input of the function above |
| s 1087C(5) | 15422 | encoded | `s 1087C(5) the information is relevant date of birth information` | 3 |  |
| s 1088 | 15423 | inert (reason 1) | - | - | section heading, not operative |
| s 1088(1) | 15424 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1088(1)(a) | 15425 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1088(1)(b) | 15426 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1088(1)(c) | 15427 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1088(1)(d) | 15428 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1088(2) | 15429 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1088(2)(a) | 15430 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1088(2)(b) | 15431 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1088(3) | 15432 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1088(3)(a) | 15433 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1088(3)(b) | 15434 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1088(3)(c) | 15435 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1088(3)(d) | 15436 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1088(3)(e) | 15437 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1088(3)(f) | 15438 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1088(4) | 15439 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1088(5) | 15440 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1088(6) | 15441 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1088(7) | 15442 | encoded | `s 1088(7) regulations under subsection (1)(b) or (2)(b) may require the registrar to refrain from disclosing information under the provision` | 5 | what the regulations must not require (F1) |
| s 1088(7)(a) | 15443 | encoded | `s 1088(7) regulations under subsection (1)(b) or (2)(b) may require the registrar to refrain from disclosing information under the provision` | 5 | what the regulations must not require (F1) |
| s 1088(7)(b) | 15444 | encoded | `s 1088(7) regulations under subsection (1)(b) or (2)(b) may require the registrar to refrain from disclosing information under the provision` | 5 | what the regulations must not require (F1) |
| s 1088(7)(c) | 15445 | encoded | `s 1088(7) regulations under subsection (1)(b) or (2)(b) may require the registrar to refrain from disclosing information under the provision` | 5 | what the regulations must not require (F1) |
| s 1088(7)(d) | 15446 | encoded | `s 1088(7) regulations under subsection (1)(b) or (2)(b) may require the registrar to refrain from disclosing information under the provision` | 5 | what the regulations must not require (F1) |
| s 1088(8) | 15447 | encoded | `s 1088(8) regulations under subsection (1)(d) may require the registrar to refrain from disclosing information under the provision` | 3 | what the regulations must not require (F1) |
| s 1088(9) | 15448 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1088(10) | 15449 | inert (reason 2) | - | - | procedure for regulations |
| s 1089 | 15450 | inert (reason 1) | - | - | section heading, not operative |
| s 1089(1) | 15451 | encoded | `s 1089(1) the registrar may specify the form and manner in which the application is to be made` | 3 |  |
| s 1089(1)(a) | 15452 | encoded | `s 1089(1) the registrar may specify the form and manner in which the application is to be made` | 3 |  |
| s 1089(1)(b) | 15453 | encoded | `s 1089(1) the registrar may specify the form and manner in which the application is to be made` | 3 |  |
| s 1089(2) | 15454 | repealed or blank in this text | - | - | blank in this text |
| s 1090 | 15455-15456 | encoded | `s 1090 the registrar may determine the form and manner in which the copy is provided` | 2 |  |
| s 1091 | 15457 | inert (reason 1) | - | - | section heading, not operative |
| s 1091(1) | 15458 | encoded | `s 1091(1) the registrar must certify the copy as a true copy`; `s 1091(1) the registrar's duty to certify the copy` | 6 | an "if" (a failed one answers JUST FALSE); the text has no subsection (2) (finding) |
| s 1091(3) | 15459 | encoded | `s 1091(3)(a) the certified copy is admissible in all legal proceedings as of equal validity with the original document`; `s 1091(3)(b) what the certified copy is as evidence of the fact` | 8 | (b): evidence, or in Scotland sufficient evidence |
| s 1091(3)(a) | 15460 | encoded | `s 1091(3)(a) the certified copy is admissible in all legal proceedings as of equal validity with the original document`; `s 1091(3)(b) what the certified copy is as evidence of the fact` | 8 | (b): evidence, or in Scotland sufficient evidence |
| s 1091(3)(b) | 15461 | encoded | `s 1091(3)(a) the certified copy is admissible in all legal proceedings as of equal validity with the original document`; `s 1091(3)(b) what the certified copy is as evidence of the fact` | 8 | (b): evidence, or in Scotland sufficient evidence |
| s 1091(4) | 15462 | inert (reason 2) | - | - | a power to make regulations (or fixes how they are made): machinery |
| s 1091(5) | 15463 | encoded | `s 1091(5) the copy may be sealed with the registrar's official seal instead of being certified in writing` | 2 |  |
| s 1092 | 15464 | inert (reason 1) | - | - | section heading, not operative |
| s 1092(1) | 15465 | encoded | `s 1092(1) the issue of the process from the court is barred` | 4 | an "except" bar (F9) |
| s 1092(2) | 15466 | encoded | `s 1092(2) the process bears the statement it must bear` | 4 |  |
| heading: Additional information | 15467 | inert (reason 1) | - | - | heading, not operative |
| s 1092A | 15468 | inert (reason 1) | - | - | section heading, not operative |
| s 1092A(1) | 15469 | encoded | `s 1092A(1) the registrar may require the person to provide the information` | 5 |  |
| s 1092A(1)(a) | 15470 | encoded | `s 1092A(1) the registrar may require the person to provide the information` | 5 |  |
| s 1092A(1)(b) | 15471 | encoded | `s 1092A(1) the registrar may require the person to provide the information` | 5 |  |
| s 1092A(2) | 15472 | encoded | `s 1092A(2) a requirement under section 1092A may specify the matter` | 3 |  |
| s 1092A(2)(a) | 15473 | encoded | `s 1092A(2) a requirement under section 1092A may specify the matter` | 3 |  |
| s 1092A(2)(b) | 15474 | encoded | `s 1092A(2) a requirement under section 1092A may specify the matter` | 3 |  |
| s 1092A(3) | 15475 | encoded | `s 1092A(3) the registrar may extend the period` | 3 |  |
| s 1092B | 15476 | inert (reason 1) | - | - | section heading, not operative |
| s 1092B(1) | 15477 | encoded | `s 1092B(1) the person commits an offence` | 4 | "without reasonable excuse" is an input; a person with a reasonable excuse answers NOTHING (fork F26) |
| s 1092B(2) | 15478 | encoded | `s 1092B(2) an offence is also committed by the officer` | 5 | the officer being in default is section 1121 (input) |
| s 1092B(3) | 15479 | encoded | `s 1092B(3) the penalty for the offence` | 6 | the core's Penalty; "the general limit in a magistrates' court" is an input |
| s 1092B(3)(a) | 15480 | encoded | `s 1092B(3) the penalty for the offence` | 6 | the core's Penalty; "the general limit in a magistrates' court" is an input |
| s 1092B(3)(b) | 15481 | encoded | `s 1092B(3) the penalty for the offence` | 6 | the core's Penalty; "the general limit in a magistrates' court" is an input |
| s 1092B(3)(b)(i) | 15482 | encoded | `s 1092B(3) the penalty for the offence` | 6 | the core's Penalty; "the general limit in a magistrates' court" is an input |
| s 1092B(3)(b)(ii) | 15483 | encoded | `s 1092B(3) the penalty for the offence` | 6 | the core's Penalty; "the general limit in a magistrates' court" is an input |
| s 1092B(3)(b)(iii) | 15484 | encoded | `s 1092B(3) the penalty for the offence` | 6 | the core's Penalty; "the general limit in a magistrates' court" is an input |
| defined term: "overseas company" (s 1044) | 14669 | encoded | `s 1044 the company is an overseas company` | 2 | a defined term is a function that returns the term's meaning as the Act states it |
| defined term: "branch" (s 1046(3)) | 14683 | encoded | `s 1046(3) the establishment is a branch` | 3 | a defined term is a function that returns the term's meaning as the Act states it |
| defined term: "Gibraltar company" (s 1046(3)) | 14684 | encoded | `s 1046(3) the company is a Gibraltar company` | 2 | a defined term is a function that returns the term's meaning as the Act states it |
| defined term: "specified" (s 1046(7)) | 14702 | encoded | `s 1046(7) the matter is specified` | 2 | a defined term is a function that returns the term's meaning as the Act states it |
| defined term: "corporate name" (s 1047(2)(a)) | 14707 | encoded | `s 1047(2) the name may be the registered name of the overseas company` | 3 | a defined term is a function that returns the term's meaning as the Act states it |
| defined term: "appropriate address" (s 1048A(4)) | 14749 | encoded | `s 1048A(4) the address is an appropriate address` | 3 | a defined term is a function that returns the term's meaning as the Act states it |
| defined term: "appropriate email address" (s 1048A(4)) | 14750 | encoded | `s 1048A(4) the email address is an appropriate email address` | 3 | a defined term is a function that returns the term's meaning as the Act states it |
| defined term: "branch" (s 1050(2)) | 14779 | encoded | `s 1050(2) the place of business is a branch of the institution` | 4 | a defined term is a function that returns the term's meaning as the Act states it |
| defined term: "specified" (s 1051(4)) | 14802 | encoded | `s 1051(4) the matter is specified` | 2 | a defined term is a function that returns the term's meaning as the Act states it |
| defined term: "registered overseas company" (s 1052(6)) | 14818 | encoded | `s 1052(6) the overseas company is a registered overseas company` | 2 | a defined term is a function that returns the term's meaning as the Act states it |
| defined term: "specified" (s 1052(6)) | 14819 | encoded | `s 1052(6) the matter is specified` | 2 | a defined term is a function that returns the term's meaning as the Act states it |
| defined term: "specified" (s 1054(4)) | 14843 | encoded | `s 1054(4) the matter is specified` | 2 | a defined term is a function that returns the term's meaning as the Act states it |
| defined term: "the registrar of companies" and "the registrar" (s 1060(3)) | 14910 | encoded | `s 1060(3) the registrar of companies, as the case may require, for the place` | 3 | a defined term is a function that returns the term's meaning as the Act states it |
| defined term: "company" for section 1066 (s 1066(6)) | 14988 | encoded | `s 1066(6) the overseas company is a company for the purposes of section 1066` | 4 | a defined term is a function that returns the term's meaning as the Act states it |
| defined term: "establishment" and "UK establishment" (s 1067(6)) | 14995 | encoded | `s 1067(6) the place is an establishment of the overseas company`; `s 1067(6) the establishment is a UK establishment of the overseas company` | 10 | a defined term is a function that returns the term's meaning as the Act states it |
| defined term: "corporate officer" (s 1067A(8)) | 15028 | encoded | `s 1067A(8) the officer is a corporate officer` | 2 | a defined term is a function that returns the term's meaning as the Act states it |
| defined term: "disqualified person" (s 1067B(6)) | 15040 | encoded | `s 1067B(6) the person is a disqualified person` | 3 | a defined term is a function that returns the term's meaning as the Act states it |
| defined term: "unnecessary material" (s 1074(2)) | 15121 | encoded | `s 1074(2) the material is unnecessary material` | 4 | a defined term is a function that returns the term's meaning as the Act states it |
| defined term: "enhanced disclosure documents" (s 1078(1)) | 15150 | encoded | `s 1078 the document is an enhanced disclosure document` | 69 | a defined term is a function that returns the term's meaning as the Act states it |
| defined term: "official notification" (s 1079(4)) | 15212 | encoded | `s 1079(4) the event has been officially notified` | 7 | a defined term is a function that returns the term's meaning as the Act states it |
| defined term: "the register" (s 1080(2)) | 15235 | encoded | `s 1080(2) the record is part of the register` | 3 | a defined term is a function that returns the term's meaning as the Act states it |
| defined term: "the register" in Objective 2 (s 1081A(2)) | 15274 | encoded | `s 1081A(2) the reference to the register in Objective 2 includes the records` | 2 | a defined term is a function that returns the term's meaning as the Act states it |
| defined term: "unique identifiers" (s 1082(1)) | 15276 | encoded | `s 1082(1) regulations may provide for a unique identifier to identify the person` | 6 | a defined term is a function that returns the term's meaning as the Act states it |
| defined term: "the relevant date" (s 1084(1)) | 15307 | encoded | `s 1084(1) the relevant date` | 4 | a defined term is a function that returns the term's meaning as the Act states it |
| defined term: "company" in s 1084(1)(a) (s 1084(4)) | 15312 | encoded | `s 1084(4) the body is a company for the purposes of subsection (1)(a)` | 2 | a defined term is a function that returns the term's meaning as the Act states it |
| defined term: "optional information" (s 1084A(2)) | 15317 | encoded | `s 1084A(2) the information is optional information` | 4 | a defined term is a function that returns the term's meaning as the Act states it |
| defined term: "relevant date of birth information" (s 1087A(3)) | 15393 | encoded | `s 1087A(3) the information is relevant date of birth information` | 5 | a defined term is a function that returns the term's meaning as the Act states it |
| defined term: "registrable person" (s 1087A(6)) | 15398 | encoded | `s 1087A(6) the person is a registrable person in relation to the company` | 3 | a defined term is a function that returns the term's meaning as the Act states it |
| defined term: "old documents" (s 1087B(1)) | 15400 | encoded | `s 1087B section 1087A applies to the old document` | 18 | a defined term is a function that returns the term's meaning as the Act states it |
| defined term: "relevant date of birth information" (s 1087C(5)) | 15422 | encoded | `s 1087C(5) the information is relevant date of birth information` | 3 | a defined term is a function that returns the term's meaning as the Act states it |

## Fork register (coa23)

Each entry gives the provision, the function, the reading taken, the other reading, and the text that licenses each. Sites the 2026-11-05 ruling leaves to the encoder's judgment (an "unless" or "except" once met; a bare "must" not done; "(other than X)"; a duty whose "if" or "where" is unmet) carry one line here for the human reviewer to overrule. There is no "listed in Schedule N" site and no state-ledger site in this range.

- **F1** (regulation-making powers and what the regulations must contain; ss 1045 to 1058, 1063(1), (3), (4), (6A), (6B), 1067A(4) to (7), 1067B(7), (8), 1068A(1), 1071(2), 1078(6), 1081(2), (7), 1082(2) to (5), 1084A(1), (3), (4), 1088(1) to (6), (9), (10), 1091(4)): Taken: a provision that only confers a power to make regulations or registrar's rules, or says how they are made, is `inert`, reason 2 (the brief's "regulation-making and rule-making powers"). A provision that fixes what the regulations MUST contain or MUST NOT contain is encoded as a function over a plain description of the proposed regulation: ss 1046(2), 1047(1), 1051(2)(a), 1054(3)(a) and (b), 1055, 1056, 1058(2), 1088(7) and (8) (and the limits on the registrar's rules in ss 1068(4A), 1068(7), 1068A(2)). Licence: "The Secretary of State may make provision by regulations ..." against "The regulations ... must ...", "must not provide ...", "may not require ...". Other reading: all of it inert (the regulations are not among the sources, so a "must" inside a power says nothing about anyone's duty today), or every power encoded as a function. Why the split: the mandatory limbs are the only sentences of Part 34 that tell the person anything on the Act's own authority (for example that regulations can never impose imprisonment: s 1054(3)(a)).
- **F2** (s 1054(3)(b); `s 1054(3)(b) the regulations may provide for those fines`; coverage row: fork): The text of the paragraph joins two wordings: "...a daily default fine not exceeding one-tenth of level 5 on the standard scaleone-tenth of the greater of £5,000 or level 4 on the standard scale." (line 14842). Taken: the later wording governs ("one-tenth of the greater of £5,000 or level 4"), and the two limbs ("a fine exceeding level 5", "a daily default fine ... one-tenth of ...") are two separate bars, each a limit the regulations may not go past; "not exceeding" is read as describing the cap, not the prohibited act. A fine within both limits answers NOTHING (a prohibition limited by its own wording, marginal reading (b)). The levels are inputs in pounds (the Act does not state them). Other readings: (i) the first wording (one-tenth of level 5); (ii) the literal words, under which the regulations may not provide for a summary fine above level 5 AND a daily default fine not above the cap (a conjunction that bars only a combination and, read literally, bars every daily fine up to the cap). The text caveat in `inputs/SOURCES.md` says the file "may carry more than one extent version of a provision".
- **F3** (s 1059A(2), list row 2, line 14873; `s 1059A(2) to (4) how the provision of this Part applies`; coverage row: fork): The line reads "sections 1068 1067A to 1071 (delivery of documents to the registrar)", two versions joined. Taken: "sections 1067A to 1071". Other reading: "sections 1068 to 1071", under which ss 1067A and 1067B would be in none of the three lists. Licence for the taken reading: ss 1067A to 1071 are the sections about delivery to the registrar, and 1067A and 1067B sit directly before 1068.
- **F4** (s 1063(3A); coverage rows: inert, reason 2): the list of functions whose costs the Secretary of State may take into account in fixing fees is part of the power to make fees regulations. Other reading: encoded as a list of permitted considerations. Nothing in the seat turns on it.
- **F5** (a bare "must" or "shall" not done; ss 1063(6), 1064(1) and (2), 1066(2), 1067(2), 1067B(3), 1070(3), 1077(1) and (2), 1079B(2) and (3), 1080(3), 1080(5), 1092(2)): Taken: a function named for compliance answers JUST FALSE when the duty is not done ("The notice must state ..." not stated), and JUST TRUE when it is; the "must" itself is a separate function that answers JUST TRUE when the duty is engaged. Other reading: NOTHING, because "must" does not say what follows if it is not done (the text names no consequence). Licence: the 2026-11-05 case-by-case ruling ("a bare 'must' not done"); the keel took the same reading for s 1168(5).
- **F6** (signposts and lead-ins: ss 1059A(1), 1062A(2), 1085(2) second sentence, 1087A(2)): Taken: `inert`, reason 1 (not operative), because each only introduces a list or points at another section (the keel's F7 took the same reading). Other reading: operative scope statements, each a one-line function returning JUST TRUE.
- **F7** (s 1059A(5); `s 1059A(5) the provision of this Part applies to the overseas company as it applies to a company as defined in section 1`): "Unless the context otherwise requires" once met answers NOTHING, not JUST FALSE: the text reserves the context without saying what applies then (the keel's F3 took the same reading for s 1(1)). Other reading: JUST FALSE ("unless" counts as the text's no).
- **F8** (s 1066(6); `s 1066(6) the overseas company is a company for the purposes of section 1066`): The "(other than X)" site: an overseas company whose particulars are registered but which "appears to the registrar not to be required to register particulars" answers JUST FALSE ("other than"); an overseas company with no registered particulars answers NOTHING ("includes"). Other reading: NOTHING for the excluded company too, since "other than" only trims what "includes" adds.
- **F9** (an "unless" or "except" once met; ss 1067A(1), 1067A(2), 1067B(2), 1076(2), 1079(1), 1087C(1), 1092(1)): Taken: the function is named for the bar ("is barred from", "must not be accepted"); once the "unless" or "except" is met it answers JUST FALSE (the bar does not apply), and when it is not met, JUST TRUE. Other reading: NOTHING once met, because an exception lifts a bar and grants no permission of its own. The names never say "may deliver" or "may disclose", so a caller cannot read JUST FALSE as a permission.
- **F10** (s 1067A(2), the table; `s 1067A(2) the individual is barred from delivering the document to the registrar on behalf of B`; coverage row: fork): B being a firm has four rows (1 to 4); B an individual has three (5 to 7). The text says A must meet "the corresponding entry" without saying how a firm's four rows combine. Taken: any one row that is fully met (A's description and the statement of that row) lifts the bar; each row is its own function. Other reading: the rows are cumulative (A must meet all four rows for a firm), which no one could satisfy (rows 1 and 3 describe different people).
- **F11** (s 1070(3); `s 1070(3) the duty to deliver in accordance with the agreement`): The text says "Documents in relation to which an agreement is in force ... must be delivered in accordance with the agreement" and names no deliverer. Taken: the regulative rule is for the Company (the party to the agreement); no deliverer is invented. Other reading: any person delivering for the company.
- **F12** (periods counted from a date: ss 1066(5), 1067(5) three years; 1083(1) two years; 1084(1A) twenty years; 1084(2), (2AA) two years; 1073(6) fourteen days): Taken: "a period of N years beginning with that date" ends on the day before the Nth anniversary (`Date d m (y + N)` minus one day; a 29 February anniversary rolls forward to 1 March, so a three-year period beginning on 29 February 2020 ends on 28 February 2023); outside a period the text fixes in its own words the answer is JUST FALSE (ruling of 2026-11-05 (a)). Both sides of every end are tested. Other reading: the Interpretation Act 1978 rules for counting periods (not among the sources) could count a day differently.
- **F13** (s 1073(4)(b); `s 1073(4) the acceptance of the document affects the matter`): "(b) subject as follows, any liability for failure to comply with those requirements": answers NOTHING (a flat negative limited by "subject as follows"; subsections (5) and (6) then say when the period counts). Other reading: JUST FALSE with the exceptions of (5) and (6) as a separate function.
- **F14** (s 1083(1), lines 15295 to 15299; coverage row: fork): The text has "This is subject to section 1087(3) (extent of obligation to retain material not available for public inspection)." and then "This is subject to— (a) section 1087(3) ...; (b) section 16A(2) of the Limited Partnerships Act 1907 ...; (c) section 22(5) of the Economic Crime (Transparency and Enforcement) Act 2022 ...". Taken: the list governs; the earlier sentence is its limb (a) in old wording. The function takes one input for "a provision named in (a) to (c) limits the obligation". Other reading: the first sentence alone (no (b), (c)).
- **F15** (s 1083(1); same function): "must be kept for two years after they are received": counted to the second anniversary of the day of receipt (kept through that day; destruction allowed from the next day, if the information is recorded). Other reading: the last day is the day before the anniversary.
- **F16** (s 1087B; `s 1087B section 1087A applies to the old document`): For an old document that is registered on or after 10 October 2015 and outside the carve-outs of (3) and (4), the text does not say that section 1087A applies (subsection (1): "limits the extent to which section 1087A applies"). Taken: NOTHING (silent). Other reading: JUST TRUE (section 1087A applies in full outside the limits).
- **F17** (s 1078; `s 1078 the document is an enhanced disclosure document`): "The enhanced disclosure documents are as follows" hands the definition to the list; a head that does not hold for the company (a share-capital head for a private company, for example) and a document in no head both answer JUST FALSE (ruling of 2026-11-05, delegated definitions (a)). Other reading: NOTHING for a document in no head. The (2) heads answer JUST TRUE for every company, an overseas company included (s 1059A(5) applies the Part to an overseas company "unless the context otherwise requires"; head (5) is the overseas company's own head).
- **F18** (ss 1079(2) and 1079(4)): "The events to which this section applies are" and "“Official notification” means" are closed lists in the same way: another event answers JUST FALSE. Other reading: NOTHING.
- **F19** (s 1084(3); coverage row: fork): the text refers to "subsection (2) or (2A)" but this text has subsections (2) and (2AA) and no (2A) (line 15310 to 15311). Taken: read as both (2) and (2AA), the function takes one input "a direction was given under subsection (2) or (2A)". Other reading: only (2) (a direction by the registrar for Northern Ireland under (2AA) is not covered).
- **F20** (s 1085(1) and (3); `s 1085(1) the person may inspect the material on the register`): "Any person may inspect the register" is "subject to" the provisions of (3). Taken: the answer of the restricting provision is an input (MAYBE BOOLEAN); where it says the material is restricted the answer is NOTHING (the right is limited by its own wording), and where it says it is not, JUST TRUE. The seat passes section 1087's answer as that input. Other reading: JUST FALSE where a named provision restricts inspection.
- **F21** (s 1072; `s 1072 the document meets the requirements for proper delivery`): The text says a document "is not properly delivered unless all the following requirements are met" and never says that meeting them is delivery. Taken: the function is named for what the section lists (the requirements are met), answers JUST TRUE when every limb is met, JUST FALSE when any limb fails, and NOTHING when a limb turns on a provision outside the text and none fails. That is the answer the other parts ask for (inputs/PLAN.md 4.2). Other reading: "properly delivered" is a further fact.
- **F22** (s 1073(5) and (6)): The "period after the document is accepted" is taken to begin the day after acceptance (the acceptance day answers NOTHING), and "any subsequent period of default" to begin the day after the 14th day following the issue of the notice (the 15th day after the notice counts; the 14th does not). Other reading: the acceptance day itself is in the period.
- **F23** (s 1079(3)): The grace window is "on or before the 15th day after the date of official notification, or ... the next day that was [a working day]"; a material time before the notification is not addressed by (3). Taken: the function takes a material time and answers JUST FALSE once it is after the window; the working-day facts are inputs (section 1173(1), keel).
- **F24** (s 1087(1)(k) and the other heads; `s 1087(1) the registrar must not make the material available for public inspection`): paragraph (k) ("any other material excluded from public inspection by or under any other enactment") hands the rest to other enactments, so material in none of the heads answers NOTHING, not JUST FALSE. Other reading: JUST FALSE for material in no head.
- **F25** (the seat; assumed, not ruled): where another part of the Act decides a fact (identity verified, authorised corporate service provider, officer in default, section 1110F, public company), the seat asks a plain yes or no and passes `JUST yes` or `JUST no` to the layer-1 function, so the seat cannot answer "not covered" for that fact; the layer-1 functions still take the MAYBE BOOLEAN seams the lead wires at the merge.
- **F26** (s 1092B(1); `s 1092B(1) the person commits an offence`; a site the 2026-11-05 ruling leaves to the encoder: "without reasonable excuse"): "A person who, without reasonable excuse, fails to comply with a requirement under section 1092A commits an offence." Taken: a person who has a reasonable excuse answers NOTHING; a person who fails and has no excuse answers JUST TRUE; a person who has not failed answers NOTHING. Why: the function is named for the offence ("commits an offence"), not for a grant, so neither answer reads in the wrong direction; the brief's rule lists "without" among the wording that limits a prohibition, and the case outside the limit answers NOTHING; the text does not itself say "no offence" for an excused person. The first draft answered JUST FALSE (the excuse read as an element of the offence); it was changed on 2026-11-13, and the two assertions that changed carry `-- RECONCILED 2026-11-12`. Other reading: JUST FALSE for the excused person (the exception is the text's own no, so the person commits no offence). ss 1098E(3), 1112(1), 1203(4) and 1205(1) of other parts answer NOTHING for the same wording.
- **F27** (seat questions, repair of 2026-11-13): five seat questions were renamed so that each asks what the layer-1 function answers (the audit of all 52 is in the Seat section). The functions and their answers did not change; each renamed question carries `-- RENAMED 2026-11-12` above it in `coa23-seat.l4` and above its assertions in `coa23-cases-seat.l4`.

- **F28** (s 1073A(1), line 15114; `s 1073A(1) the registrar may refuse to accept and register the document`; name-test sweep of 2026-11-12): "The registrar may refuse to accept (and register) a document if— (a) ... and (b) ..." is a grant named "may" whose "if" gate is not met. Taken: NOTHING (the text gives the power on that gate and does not say the registrar may not refuse otherwise; the Guide's "limits a grant ... in its own wording"). Other reading: JUST FALSE (a failed "if" read as the text's own no, marginal reading (a)).
- **F29** (s 1074(5), line 15126; `s 1074(5) the registrar may register the document either with the omission of the unnecessary material or as delivered`; name-test sweep): "If the unnecessary material can readily be separated from the rest of the document, the registrar may register the document either— (a) ... or (b) ..." is a grant named "may" whose "if" gate is not met. Taken: NOTHING (a document whose unnecessary material cannot readily be separated is dealt with by subsection (4), not by this grant). Other reading: JUST FALSE (a failed "if" read as the text's own no, marginal reading (a)).
- **F30** (s 1081(4), line 15256; `s 1081(4) the note may be removed`; name-test sweep): "A note may be removed if it no longer serves any useful purpose." Taken: a note that still serves a useful purpose answers NOTHING. Other reading: JUST FALSE (a failed "if" read as the text's own no, marginal reading (a)).
- **F31** (s 1087C(2), line 15419; `s 1087C(2) the registrar may disclose the relevant date of birth information`; name-test sweep): "The registrar may disclose relevant date of birth information if the information is made available for public inspection." Taken: information not made available for public inspection answers NOTHING here (subsection (1) is the bar and is encoded in its own function, `s 1087C(1) the registrar is barred from disclosing`, which keeps its own answers). Other reading: JUST FALSE (a failed "if" read as the text's own no, marginal reading (a)).
- **F32 to F37** (name-test sweep of 2026-11-12: LISTED, NOT FLIPPED; ASSUMED, NOT RULED that these equivalents of "where", "when" and "upon" go with the listed group). Each function is named for a grant, answers JUST FALSE when its gate is not met, and the gate is not an "if". Ruling (b) of the Guide's "Periods, \"where\" and scope limits" paragraph (with ruling (c) of 2026-11-05) says JUST FALSE, and the Guide's line on grants ("limits a grant ... in its own wording") points to NOTHING, so which is right is a question for the maintainer or a lawyer, not one for a sweep. Each keeps JUST FALSE for now; the other reading is NOTHING for the case outside the gate.
  - **F32** (s 1066(3), line 14985; `s 1066(3) the registrar may change the existing registered number`): the gate is "on adopting a new form of registered number" ("on" counts as "upon", ruling of 2026-11-05 (c)); a registrar not adopting a new form answers JUST FALSE.
  - **F33** (s 1067(3), line 14992; `s 1067(3) the registrar may change the existing registered number of the UK establishment`): the same words and the same gate, "on adopting a new form of registered number"; a registrar not adopting a new form answers JUST FALSE.
  - **F34** (s 1080(4), line 15237; `s 1080(4) the information may be recorded and kept in the form`): the gate is "provided it is possible to inspect it and produce a copy of it" (a proviso, taken as "so long as"); a form in which inspection and copying are not possible answers JUST FALSE.
  - **F35** (s 1083(1), line 15295; `s 1083(1) the registrar may destroy the original`; the seat question `Under section 1083(1), may the registrar destroy the hard copy original of the document I filed` passes its answer): two gates, "after which" the two years from receipt (a day within the two years answers JUST FALSE; see also F12, F14 and F15) and "provided the information contained in them has been recorded" (information not recorded answers JUST FALSE).
  - **F36** (s 1084(2), line 15309; `s 1084(2) the registrar of companies for England and Wales may direct that the records be removed to the Public Record Office on the day`): the gate is "at any time after the period of two years beginning with the relevant date" (ruling of 2026-11-05 (a), see F12); a day within the two years answers JUST FALSE.
  - **F37** (s 1084(2AA), line 15310; `s 1084(2AA) the registrar of companies for Northern Ireland may direct that the records be removed to the Public Record Office of Northern Ireland on the day`): the same gate, "at any time after the period of two years beginning with the relevant date"; a day within the two years answers JUST FALSE.

### Name-test sweep of 2026-11-12

Scope: the 43 layer-1 functions of coa23 whose name contains "may", "permitted", "power", "entitled" or "authorised". 26 of them never answer JUST FALSE (a gate that fails answers NOTHING; one of the 26, `s 1060(3)` "as the case may require", is not a grant and returns a registrar). The other 17 are sorted below.

| flipped to NOTHING | kept JUST FALSE (gate closed by the text) | listed: "may" with where/when/upon | listed: "entitled" |
| --- | --- | --- | --- |
| 4 | 7 | 6 | 0 |

- **Flipped to NOTHING (4)**, each with one fork line in the fork register and one row in the marginal readings, its assertions restated in place with `-- RECONCILED 2026-11-12:` (10 assertions), its coverage row set to `fork`: `s 1073A(1) the registrar may refuse to accept and register the document` (F28), `s 1074(5) the registrar may register the document either with the omission of the unnecessary material or as delivered` (F29), `s 1081(4) the note may be removed` (F30), `s 1087C(2) the registrar may disclose the relevant date of birth information` (F31). Their gate is an "if" and the text does not say "only if".
- **Kept JUST FALSE, gate closed by the text (7)**: `s 1054(3)(a) the regulations may provide for imprisonment` and `s 1054(3)(b) the regulations may provide for those fines` ("The regulations must not provide"); `s 1073(3) an objection may be taken on that ground` ("No objection may be taken"); `s 1088(7) regulations under subsection (1)(b) or (2)(b) may require the registrar to refrain from disclosing information under the provision` and `s 1088(8) regulations under subsection (1)(d) may require the registrar to refrain from disclosing information under the provision` ("may not require"); `s 1068(7) the registrar may impose the requirement consistently with the enactments` ("must not be inconsistent"); `s 1068A(2) the registrar's rules may make the provision` ("may not be made"). Each is the text's own flat negative, so it is a bar and not a failed "if" (the Guide's "a flat negative"; ruling N2).
- **Listed, not flipped: "may" with where, when, upon or an equivalent (6)**, ASSUMED, NOT RULED; the other readings are in the fork register (F32 to F37): `s 1066(3) the registrar may change the existing registered number` and `s 1067(3) the registrar may change the existing registered number of the UK establishment` ("on adopting"); `s 1080(4) the information may be recorded and kept in the form` ("provided"); `s 1083(1) the registrar may destroy the original` ("after which", "provided"); `s 1084(2) the registrar of companies for England and Wales may direct that the records be removed to the Public Record Office on the day` and `s 1084(2AA) the registrar of companies for Northern Ireland may direct that the records be removed to the Public Record Office of Northern Ireland on the day` ("after the period of two years").
- **Listed, not flipped: "entitled" (0)**: no layer-1 function of this part has "entitled" in its name. The words "is not entitled" appear only in the quoted text of s 1079(1) and s 1079(3), whose functions are named for the bar (`s 1079(1) the company is barred from relying against the person on the happening of the event`, `s 1079(3) the company is barred from relying on the happening of the event against the person`) and keep JUST FALSE as bars.

Callers: none of the four flipped functions is read by another layer-1 function. The seat question `Under section 1073A(1), may the registrar refuse to accept my document because it is inconsistent with other information` passes the answer of `s 1073A(1)` through, so its two assertions that changed are restated in `coa23-cases-seat.l4` (the other three flipped functions have no seat question).

### Rulings recorded word for word

The rulings the `NOTHING-kind` tags of these modules follow, copied from the brief (they are the same text as section 5 of `inputs/ENCODING-GUIDE.md`):

- **E1** (bench `commons-negation-1030`; should a legal effect be one definition gathered from every section that gives it?): option B, as guidance for gathering a legal effect's routes by hand only, with no pilot run; option A (gathering by bare name) is withdrawn as a direction for the language, not deferred; option C (per-section answers) applies everywhere else; the Magna Carta pilot in the printed recommendation (chapters 2, 3, 4, 5, 37, 43, 46 and 53, with a blind second reader) is not to be run. The maintainer's lean, verbatim: "B but generally uncomfortable with this much magic because it takes the language from unopinionated to opinionated in ways that are hard to teach an l4 novice." the maintainer's note, verbatim: "Fundamentally I feel like we are trying to make the language do work that the human l4 drafter should do. Too much magic. Can’t we just decline to be this opinionated and say the programmer needs to do this thinking?" Marked 2026-11-03T23:19:02.812Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
- **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. The maintainer's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." the maintainer's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
- **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. The maintainer's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.
- **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. The maintainer approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.
- **Questions with no convention: decide case by case (the maintainer, typed 2026-11-05T10:25:24Z).** Six questions the rulings above leave open are decided site by site, at encoding time, on the text's own words and the encoder's best judgment: an "unless" or "except" once it is met; a bare "must" not done; "listed in Schedule N"; a duty whose "if" or "where" is unmet; "(other than X)"; a missing event in the state ledger. Each such site gets one fork line (the provision, the function, the answer taken, the other reading) for the human reviewer to overrule, and the rulings above still govern whatever they cover. The maintainer's words, asked of the session "Encodings": "re Encoding Conventions I believe I had a short discussion with the coordinator where I basically said I agreed with its \"lean\"s -- does that mean we can retire the bench card or should I go over it still? In short I feel like these decisions need to be made case-by-case at encoding time, and you should go with your gut most of the time; and if the encoding turns out to be wrong, well, that's where the human review comes in." The bench that carried the six questions ("Encoding Conventions", artifact Hpg2k9HqExJN5zdtBYiJ72, collection `encodings-conventions-1105`) was retired unmarked, so it holds no marks.

## Jural relations (coa23)

Hohfeld's correlatives, stated once per provision as a relation between two parties and named neutrally. A provision that creates no such relation (a definition, a counting rule, a heading, a procedure for regulations, a blank) is listed once as `none`. Paragraphs are carried by their subsection's row. Where the text names no holder for a duty (the registrar's duty to publish a notice, for example) the row says "none named" and does not invent one; "implied" marks a correlative the text does not state. 333 section and subsection rows; 162 of them create a relation.

| provision | holder of the right, privilege, power or immunity | bearer of the duty, no-right, liability or disability | kind | L4 rule |
| --- | --- | --- | --- | --- |
| s 1044 | none | none | none | `s 1044 the company is an overseas company` |
| s 1045 (heading) | none | none | none | (inert: heading) |
| s 1045(1) | Secretary of State | overseas companies subject to the regulations | power / liability | (inert) |
| s 1045(2) | none | none | none (procedure for regulations) | (inert) |
| s 1046 (heading) | none | none | none | (inert: heading) |
| s 1046(1) | Secretary of State | overseas companies required to register particulars | power / liability | (inert) |
| s 1046(2) | Secretary of State (must put the term into the regulations) | an overseas company that opens a branch | duty / liability | `s 1046(2) the regulations must require the company to register particulars` |
| s 1046(3) | none | none | none | `s 1046(3) the establishment is a branch`; `s 1046(3) the company is a Gibraltar company` |
| s 1046(4) | Secretary of State | overseas companies required to register particulars | power / liability | (inert) |
| s 1046(5) | Secretary of State | overseas companies required to register particulars | power / liability | (inert) |
| s 1046(6) | Secretary of State | overseas companies required to register particulars | power / liability | (inert) |
| s 1046(6A) | Secretary of State | overseas companies required to register particulars | power / liability | (inert) |
| s 1046(6B) | Secretary of State | overseas companies required to register particulars | power / liability | (inert) |
| s 1046(6C) | Secretary of State | overseas companies required to register particulars | power / liability | (inert) |
| s 1046(7) | none | none | none | `s 1046(7) the matter is specified` |
| s 1046(8) | none | none | none (procedure for regulations) | (inert) |
| s 1047 (heading) | none | none | none | (inert: heading) |
| s 1047(1) | Secretary of State (must put the term into the regulations) | an overseas company required to register particulars | duty / liability | `s 1047(1) the regulations must require the company to register its name` |
| s 1047(2) | an overseas company (permitted names) | none named | liberty / no-right | `s 1047(2) the name may be the registered name of the overseas company` |
| s 1047(3) | none | none | none | (blank in this text) |
| s 1047(4) | none | none | none | `s 1047(4) the provision of Part 5 applies to the registration of the name of an overseas company`; `s 1047(4) the row of the list for the section of Part 5` |
| s 1047(5) | none | none | none | (blank in this text) |
| s 1047(6) | none | none | none | `s 1047(6) the reference is read as a reference to registration of a different name under section 1048` |
| s 1048 (heading) | none | none | none | (inert: heading) |
| s 1048(1) | an overseas company required to register particulars | none named (the registrar must register the statement) | liberty / no-right | `s 1048(1) the company may deliver a statement of an alternative name` |
| s 1048(2) | an overseas company that has registered an alternative name | none named | liberty / no-right | `s 1048(2) the company may deliver a statement of a different name in substitution` |
| s 1048(3) | the overseas company (its registered alternative name is its corporate name in United Kingdom law) | persons dealing with it (bound to treat the name so) | power or immunity / liability or disability | `s 1048(3) the name is treated for all purposes of the law applying in the United Kingdom as the company's corporate name` |
| s 1048(4) | the overseas company (rights, obligations and proceedings unaffected) | anyone who would rely on the change of name | immunity / disability | `s 1048(4) the treatment of the alternative name as the corporate name affects the matter` |
| s 1048(5) | a person with proceedings against the overseas company | the overseas company (cannot object to the name used) | liberty / no-right | `s 1048(5) the proceedings may be continued or commenced against the company by its name for the time being registered` |
| s 1048A (heading) | none | none | none | (inert: heading) |
| s 1048A(1) | Secretary of State | overseas companies required to register particulars | power / liability | (inert) |
| s 1048A(2) | Secretary of State | overseas companies required to register particulars | power / liability | (inert) |
| s 1048A(3) | Secretary of State | overseas companies required to register particulars | power / liability | (inert) |
| s 1048A(4) | none | none | none | `s 1048A(4) the address is an appropriate address`; `s 1048A(4) the email address is an appropriate email address` |
| s 1048A(5) | none | none | none (procedure for regulations) | (inert) |
| s 1048B (heading) | none | none | none | (inert: heading) |
| s 1048B(1) | none | none | none | `s 1048B(1) this section applies in relation to the overseas company` |
| s 1048B(2) | Secretary of State | overseas companies and their directors | power / liability | (inert) |
| s 1048B(3) | Secretary of State | overseas companies and their directors | power / liability | (inert) |
| s 1048B(4) | none | none | none (procedure for regulations) | (inert) |
| s 1049 (heading) | none | none | none | (inert: heading) |
| s 1049(1) | Secretary of State | overseas companies required to register particulars | power / liability | (inert) |
| s 1049(2) | Secretary of State | overseas companies required to register particulars | power / liability | (inert) |
| s 1049(3) | Secretary of State | overseas companies required to register particulars | power / liability | (inert) |
| s 1049(4) | none | none | none (procedure for regulations) | (inert) |
| s 1050 (heading) | none | none | none | (inert: heading) |
| s 1050(1) | none | none | none | `s 1050(1) this section applies to the credit or financial institution` |
| s 1050(2) | none | none | none | `s 1050(2) the place of business is a branch of the institution` |
| s 1050(3) | Secretary of State | credit or financial institutions within section 1050 | power / liability | (inert) |
| s 1050(4) | Secretary of State | credit or financial institutions within section 1050 | power / liability | (inert) |
| s 1050(5) | Secretary of State | credit or financial institutions within section 1050 | power / liability | (inert) |
| s 1050(6) | none | none | none (procedure for regulations) | (inert) |
| s 1051 (heading) | none | none | none | (inert: heading) |
| s 1051(1) | Secretary of State | overseas companies carrying on business in the United Kingdom | power / liability | (inert) |
| s 1051(2) | Secretary of State (must put the term into the regulations) | an overseas company that has registered particulars | duty / liability | `s 1051(2)(a) the regulations must require the company to disclose the name registered by it under section 1047` |
| s 1051(3) | Secretary of State | overseas companies carrying on business in the United Kingdom | power / liability | (inert) |
| s 1051(4) | none | none | none | `s 1051(4) the matter is specified` |
| s 1051(5) | none | none | none (procedure for regulations) | (inert) |
| s 1052 (heading) | none | none | none | (inert: heading) |
| s 1052(1) | Secretary of State | registered overseas companies | power / liability | (inert) |
| s 1052(2) | Secretary of State | registered overseas companies | power / liability | (inert) |
| s 1052(3) | Secretary of State | registered overseas companies | power / liability | (inert) |
| s 1052(4) | Secretary of State | registered overseas companies | power / liability | (inert) |
| s 1052(5) | none | none | none (procedure for regulations) | (inert) |
| s 1052(6) | none | none | none | `s 1052(6) the overseas company is a registered overseas company`; `s 1052(6) the matter is specified` |
| s 1053 (heading) | none | none | none | (inert: heading) |
| s 1053(1) | none | none | none | `s 1053(1) this section applies to the overseas company` |
| s 1053(2) | Secretary of State | overseas companies (and their liquidators) required to register particulars | power / liability | (inert) |
| s 1053(3) | Secretary of State | overseas companies (and their liquidators) required to register particulars | power / liability | (inert) |
| s 1053(4) | Secretary of State | overseas companies (and their liquidators) required to register particulars | power / liability | (inert) |
| s 1053(5) | Secretary of State | overseas companies (and their liquidators) required to register particulars | power / liability | (inert) |
| s 1053(6) | none | none | none (procedure for regulations) | (inert) |
| s 1054 (heading) | none | none | none | (inert: heading) |
| s 1054(1) | Secretary of State | persons responsible for complying with the regulations | power / liability | (inert) |
| s 1054(2) | Secretary of State | persons responsible for complying with the regulations | power / liability | (inert) |
| s 1054(3) | an overseas company and the persons responsible (no imprisonment, capped fines) | the Secretary of State (disabled from providing for them) | immunity / disability | `s 1054(3)(a) the regulations may provide for imprisonment` |
| s 1054(4) | none | none | none | `s 1054(4) the matter is specified` |
| s 1055 | an individual whose residential address is registered by an overseas company | Secretary of State (must put the protection into the regulations) | claim / duty | `s 1055 the regulations must contain provision corresponding to that made by Chapter 8 of Part 10` |
| s 1056 | Secretary of State (must put the term into the regulations) | an overseas company | duty / liability | `s 1056 what the regulations under section 1046 must require the overseas company to register` |
| s 1057 (heading) | none | none | none | (inert: heading) |
| s 1057(1) | none | none | none | `s 1057(1) this section applies to the overseas company` |
| s 1057(2) | Secretary of State | overseas companies registered in more than one part of the United Kingdom | power / liability | (inert) |
| s 1057(3) | none | none | none (procedure for regulations) | (inert) |
| s 1058 (heading) | none | none | none | (inert: heading) |
| s 1058(1) | Secretary of State | overseas companies that close a branch | power / liability | (inert) |
| s 1058(2) | an overseas company that gives notice of closing a branch | Secretary of State (must provide for the registrar of the original return) | claim / duty | `s 1058(2) the registrar to whom the regulations must provide for the notice to be given is the registrar for` |
| s 1058(3) | Secretary of State | overseas companies that close a branch | power / liability | (inert) |
| s 1058(4) | none | none | none (procedure for regulations) | (inert) |
| s 1059 | none | none | none | `s 1059 the relocation counts as the closing of one branch and the opening of another` |
| s 1059A (heading) | none | none | none | (inert: heading) |
| s 1059A(1) | none | none | none | (inert) |
| s 1059A(2) | none | none | none | `s 1059A(2) to (4) how the provision of this Part applies` |
| s 1059A(3) | none | none | none | `s 1059A(2) to (4) how the provision of this Part applies` |
| s 1059A(4) | none | none | none | `s 1059A(2) to (4) how the provision of this Part applies` |
| s 1059A(5) | none | none | none | `s 1059A(5) the provision of this Part applies to the overseas company as it applies to a company as defined in section 1` |
| s 1060 (heading) | none | none | none | (inert: heading) |
| s 1060(1) | none named (the public and companies) | the Secretary of State and the registrars (there shall continue to be a registrar for each part) | duty | `s 1060(1) there is to continue to be a registrar of companies for the place` |
| s 1060(2) | Secretary of State | the registrars | power / liability (appointment) | (inert) |
| s 1060(3) | none | none | none | `s 1060(3) the registrar of companies, as the case may require, for the place` |
| s 1060(4) | none | none | none | `s 1060(4) registration in the part of the United Kingdom is registration by` |
| s 1061 (heading) | none | none | none | (inert: heading) |
| s 1061(1) | none named (companies and the Secretary of State) | the registrar (shall continue to perform the functions) | duty | `s 1061(1) the registrar must perform the function` |
| s 1061(2) | none | none | none | (blank in this text) |
| s 1061(3) | none | none | none | `s 1061(3) the function is a function of the registrar for the purposes of the Act` |
| s 1062 | none named | the registrar (shall have an official seal) | duty | `s 1062 the document bears the registrar's official seal` |
| s 1062A (heading) | none | none | none | (inert: heading) |
| s 1062A(1) | none named (the public interest) | the registrar (must analyse information) | duty | `s 1062A(1) the registrar must carry out the analysis`; `s 1062A(1) the registrar's duty to analyse information` |
| s 1062A(2) | none | none | none | (inert) |
| s 1063 (heading) | none | none | none | (inert: heading) |
| s 1063(1) | Secretary of State (fees); the registrar (determined fees) | persons who pay fees | power / liability | (inert) |
| s 1063(2) | none | none | none | `s 1063(2) fees may be charged for the matter` |
| s 1063(3) | Secretary of State (fees); the registrar (determined fees) | persons who pay fees | power / liability | (inert) |
| s 1063(3A) | Secretary of State (fees); the registrar (determined fees) | persons who pay fees | power / liability | (inert) |
| s 1063(4) | none | none | none (procedure for regulations) | (inert) |
| s 1063(5) | the registrar (may determine fees) | persons who pay fees | power / liability | `s 1063(5) the registrar may determine from time to time what fees, if any, are chargeable` |
| s 1063(6) | the Consolidated Fund | the registrar (fees are to be paid in) | claim / duty | `s 1063(6) the fee received by the registrar has been dealt with as the section requires` |
| s 1063(6A) | Secretary of State (fees); the registrar (determined fees) | persons who pay fees | power / liability | (inert) |
| s 1063(6B) | none | none | none (procedure for regulations) | (inert) |
| s 1063(7) | Secretary of State (fees); the registrar (determined fees) | persons who pay fees | power / liability | (inert) |
| s 1064 (heading) | none | none | none | (inert: heading) |
| s 1064(1) | none named (the public) | the registrar (must cause notice of the issue to be published) | duty | `s 1064(1) the registrar must cause notice of the issue of the certificate to be published`; `s 1064(1) the registrar has complied by publishing the notice`; `s 1064(1) the registrar's duty to publish notice of the issue of a certificate of incorporation` |
| s 1064(2) | none named (the public) | the registrar (the notice must state name, number and date) | duty | `s 1064(2) the notice states what it must state` |
| s 1064(3) | none | none | none | `s 1064(3) section 1064 applies to the certificate of incorporation` |
| s 1065 | any person | the registrar (must provide the copy; implied) | claim / duty | `s 1065 the person may require the registrar to provide a copy of the certificate of incorporation`; `s 1065 the right of any person to a copy of a certificate of incorporation` |
| s 1066 (heading) | none | none | none | (inert: heading) |
| s 1066(1) | a company | the registrar (shall allocate a number) | claim / duty | `s 1066(1) the registrar must allocate a registered number to the company` |
| s 1066(2) | none named | the registrar (numbers shall be in the form the registrar determines) | duty | `s 1066(2) the registered number is in the form the section requires` |
| s 1066(3) | the registrar (may change existing numbers) | the company whose number is changed | power / liability | `s 1066(3) the registrar may change the existing registered number` |
| s 1066(4) | none | none | none | `s 1066(4) the change of registered number has effect on the day` |
| s 1066(5) | a company disclosing its number (either number satisfies) | the Secretary of State's disclosure regulations (disabled from requiring more for three years) | immunity / disability | `s 1066(5) the last day of the three years beginning with the date`; `s 1066(5) the requirement to disclose the registered number imposed by regulations under section 82 or section 1051 is satisfied by the number disclosed` |
| s 1066(6) | none | none | none | `s 1066(6) the overseas company is a company for the purposes of section 1066` |
| s 1067 (heading) | none | none | none | (inert: heading) |
| s 1067(1) | an overseas company with a UK establishment | the registrar (shall allocate a number) | claim / duty | `s 1067(1) the registrar must allocate a registered number to the UK establishment` |
| s 1067(2) | none named | the registrar (numbers shall be in the form the registrar determines) | duty | `s 1067(2) the registered number of the UK establishment is in the form the section requires` |
| s 1067(3) | the registrar (may change existing numbers) | the overseas company | power / liability | `s 1067(3) the registrar may change the existing registered number of the UK establishment` |
| s 1067(4) | none | none | none | `s 1067(4) the change of the registered number of the UK establishment has effect on the day` |
| s 1067(5) | an overseas company disclosing its UK establishment's number | the Secretary of State's disclosure regulations | immunity / disability | `s 1067(5) the requirement to disclose the UK establishment's registered number imposed by regulations under section 1051 is satisfied by the number disclosed` |
| s 1067(6) | none | none | none | `s 1067(6) the place is an establishment of the overseas company`; `s 1067(6) the establishment is a UK establishment of the overseas company` |
| s 1067A (heading) | none | none | none | (inert: heading) |
| s 1067A(1) | the registrar (no document from an unverified individual) | an individual delivering on their own behalf (barred unless verified and a statement accompanies) | claim / duty (an "unless" bar) | `s 1067A(1) the individual is barred from delivering the document to the registrar on their own behalf`; `s 1067A(1) the prohibition on an individual delivering a document on their own behalf` |
| s 1067A(2) | the registrar (no document except through a listed deliverer) | an individual delivering for a firm or another individual | claim / duty (an "unless" bar) | `s 1067A(2) the individual is barred from delivering the document to the registrar on behalf of B` |
| s 1067A(3) | none | none | none | `s 1067A(3) the individual is one of the officers of the corporate officer for the purposes of row 2` |
| s 1067A(4) | Secretary of State | individuals who deliver documents | power / liability | (inert) |
| s 1067A(5) | Secretary of State | individuals who deliver documents | power / liability | (inert) |
| s 1067A(6) | Secretary of State | individuals who deliver documents | power / liability | (inert) |
| s 1067A(7) | none | none | none (procedure for regulations) | (inert) |
| s 1067A(8) | none | none | none | `s 1067A(8) the officer is a corporate officer` |
| s 1067B (heading) | none | none | none | (inert: heading) |
| s 1067B(1) | the registrar and the public (no filing by a disqualified person) | an individual who is a disqualified person | claim / duty | `s 1067B(1) the individual is barred from delivering documents to the registrar on their own behalf or on behalf of another`; `s 1067B(1) the prohibition on a disqualified individual delivering documents` |
| s 1067B(2) | the registrar | an individual delivering for a disqualified person (barred unless an authorised corporate service provider or its officer or employee) | claim / duty (an "unless" bar) | `s 1067B(2) the individual is barred from delivering the document to the registrar on behalf of the disqualified person` |
| s 1067B(3) | the registrar | the individual delivering (must include the two statements) | claim / duty | `s 1067B(3) the document is accompanied by the two statements` |
| s 1067B(4) | none | none | none | `s 1067B(3) the document is accompanied by the two statements` |
| s 1067B(5) | none | none | none | `s 1067B(3) the document is accompanied by the two statements` |
| s 1067B(6) | none | none | none | `s 1067B(6) the person is a disqualified person` |
| s 1067B(7) | Secretary of State | individuals who deliver documents for a disqualified person | power / liability | (inert) |
| s 1067B(8) | none | none | none (procedure for regulations) | (inert) |
| s 1068 (heading) | none | none | none | (inert: heading) |
| s 1068(1) | the registrar (may impose requirements) | persons delivering documents | power / liability | `s 1068 the registrar may impose the requirement` |
| s 1068(2) | none | none | none | `s 1068 the registrar may impose the requirement` |
| s 1068(3) | none | none | none | `s 1068 the registrar may impose the requirement` |
| s 1068(4) | none | none | none | `s 1068 the registrar may impose the requirement`; `s 1068(4A) the requirement must be imposed by means of registrar's rules` |
| s 1068(4A) | persons delivering documents (the requirements must be in registrar's rules) | the registrar (disabled from imposing them otherwise) | immunity / disability | `s 1068(4A) the requirement must be imposed by means of registrar's rules` |
| s 1068(5) | none | none | none | (blank in this text) |
| s 1068(6) | none | none | none | (blank in this text) |
| s 1068(6A) | none | none | none | (blank in this text) |
| s 1068(7) | persons delivering documents (no inconsistent requirement) | the registrar (disabled) | immunity / disability | `s 1068(7) the registrar may impose the requirement consistently with the enactments` |
| s 1068A (heading) | none | none | none | (inert: heading) |
| s 1068A(1) | the registrar (registrar's rules) | persons who deliver two or more documents | power / liability | (inert) |
| s 1068A(2) | persons who must deliver documents (no earlier delivery by rule) | the registrar (disabled) | immunity / disability | `s 1068A(2) the registrar's rules may make the provision` |
| s 1069 | none | none | none | (blank in this text) |
| s 1070 (heading) | none | none | none | (inert: heading) |
| s 1070(1) | the registrar and a company (may agree electronic delivery) | none named | liberty / no-right | `s 1070(1) the registrar may make the agreement for delivery by electronic means` |
| s 1070(2) | the registrar and a company | none named | liberty / no-right | `s 1070(2) the agreement may relate to the documents` |
| s 1070(3) | the registrar | the company or body bound by the agreement (taken to be the company: fork F11) | claim / duty | `s 1070(3) the document is delivered as the section requires`; `s 1070(3) the duty to deliver in accordance with the agreement` |
| s 1071 (heading) | none | none | none | (inert: heading) |
| s 1071(1) | none named (a person who has not delivered is not taken to have) | the person delivering (a document is not delivered until received) | none (a condition) | `s 1071(1) the document cannot yet count as delivered to the registrar` |
| s 1071(2) | the registrar (registrar's rules) | persons who deliver documents | power / liability | (inert) |
| s 1072 (heading) | none | none | none | (inert: heading) |
| s 1072(1) | none | none | none | `s 1072 the document meets the requirements for proper delivery`; `s 1072(1) all the requirements in the list are met` |
| s 1072(2) | the registrar and anyone relying on the filing requirement | the person who delivered the document (it counts as not delivered) | liability | `s 1072(2) the document is treated as not having been delivered` |
| s 1073 (heading) | none | none | none | (inert: heading) |
| s 1073(1) | the registrar (may accept) | the person who delivered | power / liability | `s 1073(1) the registrar may accept and register the document` |
| s 1073(2) | the person whose document is accepted | none named | immunity / disability | `s 1073(2) the document is treated as received by the registrar for the purposes of section 1077` |
| s 1073(3) | the person whose document is accepted (no objection on that ground) | anyone who would object (disabled) | immunity / disability | `s 1073(3) an objection may be taken on that ground` |
| s 1073(4) | none | none | none | `s 1073(4) the acceptance of the document affects the matter` |
| s 1073(5) | the person in default (the period after acceptance does not count) | the Secretary of State and prosecutors (daily default fine and section 453 penalty disabled) | immunity / disability | `s 1073(5) the day counts as a day of default in complying with the requirements for proper delivery` |
| s 1073(6) | the registrar (the period counts again after a removal notice and 14 days) | the person in default | power / liability | `s 1073(5) the day counts as a day of default in complying with the requirements for proper delivery` |
| s 1073A (heading) | none | none | none | (inert: heading) |
| s 1073A(1) | the registrar (may refuse) | the person who delivered | power / liability | `s 1073A(1) the registrar may refuse to accept and register the document` |
| s 1073A(2) | none | none | none | `s 1073A(2) the document is refused` |
| s 1073A(3) | none | the person who delivered (the refused document counts as not delivered) | liability | `s 1073A(3) the document is treated as not having been delivered` |
| s 1074 (heading) | none | none | none | (inert: heading) |
| s 1074(1) | none | none | none | `s 1074(1) this section applies to the document` |
| s 1074(2) | none | none | none | `s 1074(2) the material is unnecessary material` |
| s 1074(3) | none | none | none | `s 1074(3) the obligation to deliver a document extends to the thing` |
| s 1074(4) | the registrar | the person who delivered (the document counts as not meeting the requirements) | liability | `s 1074(4) the document is treated as not meeting the requirements for proper delivery` |
| s 1074(5) | the registrar (may register with or without the material) | the person who delivered | power / liability | `s 1074(5) the registrar may register the document either with the omission of the unnecessary material or as delivered` |
| s 1075 | none | none | none | (blank in this text) |
| s 1076 (heading) | none | none | none | (inert: heading) |
| s 1076(1) | the registrar (may accept a replacement) | the person who delivered the original | power / liability | `s 1076(1) the registrar may accept a replacement for the document previously delivered` |
| s 1076(2) | the person who delivered the original or the company (the replacement is not accepted from anyone else) | the registrar (must not accept unless satisfied) | claim / duty (an "unless" bar) | `s 1076(2) the replacement document must not be accepted` |
| s 1076(3) | the registrar (power to impose identification and association requirements) | the person delivering a replacement | power / liability | `s 1076(3) the registrar's power to impose requirements as to form and manner of delivery includes power to impose the requirement` |
| s 1076(4) | none | none | none | `s 1076(4) this section applies to the original document` |
| s 1077 (heading) | none | none | none | (inert: heading) |
| s 1077(1) | none named (the public) | the registrar (must cause notice of the receipt to be published) | duty | `s 1077(1) the registrar must cause notice of the receipt of the document to be published`; `s 1077(1) the registrar has complied by publishing the notice`; `s 1077(1) the registrar's duty to publish notice of the receipt of an enhanced disclosure document` |
| s 1077(2) | none named (the public) | the registrar (the notice must state the four items) | duty | `s 1077(2) the notice states what it must state` |
| s 1077(3) | the registrar (no duty before incorporation) | none named | liberty / no-right | `s 1077(3) the registrar is required to cause notice of the receipt of the document to be published on the day` |
| s 1078 (heading) | none | none | none | (inert: heading) |
| s 1078(1) | none | none | none | `s 1078 the document is an enhanced disclosure document` |
| s 1078(2) | none | none | none | `s 1078 the document is an enhanced disclosure document` |
| s 1078(3) | none | none | none | `s 1078 the document is an enhanced disclosure document` |
| s 1078(3A) | none | none | none | `s 1078 the document is an enhanced disclosure document` |
| s 1078(4) | none | none | none | `s 1078 the document is an enhanced disclosure document` |
| s 1078(4A) | none | none | none | `s 1078 the document is an enhanced disclosure document` |
| s 1078(4B) | none | none | none | `s 1078 the document is an enhanced disclosure document` |
| s 1078(5) | none | none | none | `s 1078 the document is an enhanced disclosure document` |
| s 1078(6) | none | none | none (procedure for regulations) | (inert) |
| s 1079 (heading) | none | none | none | (inert: heading) |
| s 1079(1) | a person dealing with the company (the company may not rely on an unnotified event) | the company (disabled from relying unless notified or the person knew) | immunity / disability | `s 1079(1) the company is barred from relying against the person on the happening of the event` |
| s 1079(2) | none | none | none | `s 1079(2) the section applies to the event` |
| s 1079(3) | a person unavoidably prevented from knowing (the company may not rely for 15 days) | the company (disabled) | immunity / disability | `s 1079(3) the company is barred from relying on the happening of the event against the person`; `s 1079(3) the last day of the grace period` |
| s 1079(4) | none | none | none | `s 1079(4) the event has been officially notified` |
| s 1079A | none | none | none | (blank in this text) |
| s 1079B (heading) | none | none | none | (inert: heading) |
| s 1079B(1) | none | none | none | `s 1079B(1) this section applies to the registration of the document` |
| s 1079B(2) | a person named as a director | the registrar (must notify as soon as reasonably practicable) | claim / duty | `s 1079B(2) the registrar must notify the person`; `s 1079B(2) the registrar has notified the person as the section requires`; `s 1079B(2) the registrar's duty to notify the person named as a director` |
| s 1079B(3) | a person named as a director | the registrar (the notice must state the two things) | claim / duty | `s 1079B(3) the notice contains what it must` |
| s 1079B(4) | the registrar (may send by hard copy or electronic form) | a person named as a director | power / liability | `s 1079B(4) the notice may be sent in the form to the address` |
| s 1080 (heading) | none | none | none | (inert: heading) |
| s 1080(1) | none named (the public and companies) | the registrar (shall continue to keep records) | duty | `s 1080(1) the registrar must keep records of the matter`; `s 1080(1) the registrar's duty to keep records` |
| s 1080(2) | none | none | none | `s 1080(2) the record is part of the register` |
| s 1080(3) | none named | the registrar (must keep enhanced disclosure information electronically) | duty | `s 1080(3) the information is kept as the subsection requires`; `s 1080(3) the registrar's duty to keep information from an enhanced disclosure document in electronic form` |
| s 1080(4) | the registrar (may keep in any form that can be inspected and copied) | none named | liberty / no-right | `s 1080(4) the information may be recorded and kept in the form`; `s 1080(4) the recording and keeping is sufficient compliance with the registrar's duty to keep, file or register the document or to record the information` |
| s 1080(5) | none named (the public) | the registrar (the records must be retrievable by body) | duty | `s 1080(5) the records are such as the subsection requires` |
| s 1081 (heading) | none | none | none | (inert: heading) |
| s 1081(1) | none named (the public) | the registrar (must annotate the register) | duty | `s 1081(1) what the note in the register must record`; `s 1081(1) the registrar's duty to place a note in the register` |
| s 1081(1A) | none | none | none | (blank in this text) |
| s 1081(2) | Secretary of State | the registrar; companies whose registers are annotated | power / liability | (inert) |
| s 1081(3) | the registrar (no annotation for a document treated as not delivered) | none named | liberty / no-right | `s 1081(3) an annotation is required for the document` |
| s 1081(4) | the registrar (may remove a note) | none named | liberty / no-right | `s 1081(4) the note may be removed` |
| s 1081(5) | the court (its direction prevails over annotation) | the registrar (disabled from annotating against it) | power / liability | `s 1081(5) the registrar's duty or power with respect to annotation yields to the court's direction` |
| s 1081(6) | none | none | none | `s 1081(6) the note is part of the register for all purposes of the Companies Acts` |
| s 1081(7) | none | none | none (procedure for regulations) | (inert) |
| s 1081A (heading) | none | none | none | (inert: heading) |
| s 1081A(1) | none named (the public) | the registrar (must seek to promote the four objectives) | duty | `s 1081A(1) the registrar must seek to promote the objective`; `s 1081A(1) the registrar's duty to seek to promote the objectives` |
| s 1081A(2) | none | none | none | `s 1081A(2) the reference to the register in Objective 2 includes the records` |
| s 1082 (heading) | none | none | none | (inert: heading) |
| s 1082(1) | none | none | none | `s 1082(1) regulations may provide for a unique identifier to identify the person` |
| s 1082(2) | Secretary of State | directors, secretaries, authorised corporate service providers, verified individuals | power / liability | (inert) |
| s 1082(3) | Secretary of State | directors, secretaries, authorised corporate service providers, verified individuals | power / liability | (inert) |
| s 1082(4) | Secretary of State | directors, secretaries, authorised corporate service providers, verified individuals | power / liability | (inert) |
| s 1082(5) | none | none | none (procedure for regulations) | (inert) |
| s 1083 (heading) | none | none | none | (inert: heading) |
| s 1083(1) | none named | the registrar (must keep hard copy originals for two years) | duty | `s 1083(1) the registrar may destroy the original` |
| s 1083(2) | the registrar (no obligation to keep electronic originals) | none named | liberty / no-right | `s 1083(2) the registrar is under no obligation to keep the original` |
| s 1083(3) | none | none | none (transitional) | (inert) |
| s 1084 (heading) | none | none | none | (inert: heading) |
| s 1084(1) | none | none | none | `s 1084(1) this section applies`; `s 1084(1) the relevant date` |
| s 1084(1A) | the registrar (need not make records available after 20 years) | any person who would inspect them | liberty / no-right | `s 1084(1A) the registrar need not make the information available for public inspection on the day` |
| s 1084(2) | the registrar of companies for England and Wales (may direct removal) | none named | power / liability | `s 1084(2) the registrar of companies for England and Wales may direct that the records be removed to the Public Record Office on the day` |
| s 1084(2AA) | the registrar of companies for Northern Ireland (may direct removal) | none named | power / liability | `s 1084(2AA) the registrar of companies for Northern Ireland may direct that the records be removed to the Public Record Office of Northern Ireland on the day` |
| s 1084(3) | none | none | none | `s 1084(3) the records are to be disposed of under the enactments relating to the Public Record Office` |
| s 1084(4) | none | none | none | `s 1084(4) the body is a company for the purposes of subsection (1)(a)` |
| s 1084(4A) | none | none | none | (blank in this text) |
| s 1084(5) | none | none | none | (blank in this text) |
| s 1084A (heading) | none | none | none | (inert: heading) |
| s 1084A(1) | Secretary of State | companies and other bodies that deliver optional information | power / liability | (inert) |
| s 1084A(2) | none | none | none | `s 1084A(2) the information is optional information` |
| s 1084A(3) | Secretary of State | companies and other bodies that deliver optional information | power / liability | (inert) |
| s 1084A(4) | none | none | none (procedure for regulations) | (inert) |
| s 1085 (heading) | none | none | none | (inert: heading) |
| s 1085(1) | any person | the registrar (must let them inspect) | claim / duty | `s 1085(1) the person may inspect the material on the register`; `s 1085(1) the right of any person to inspect the register` |
| s 1085(2) | any person (originals only if the record is illegible or unavailable) | the registrar | claim / duty ("if, and only if") | `s 1085(2) the right of inspection extends to the original` |
| s 1085(3) | none | none | none | `s 1085(1) the person may inspect the material on the register` |
| s 1086 (heading) | none | none | none | (inert: heading) |
| s 1086(1) | any person | the registrar (must give a copy) | claim / duty | `s 1086(1) the person may require a copy of the material`; `s 1086(1) the right of any person to a copy of material on the register` |
| s 1086(2) | a person who requests a copy of enhanced disclosure material (the fee may not exceed the administrative cost) | the registrar | immunity / disability | `s 1086(2) the fee complies with the limit` |
| s 1086(3) | none | none | none | (blank in this text) |
| s 1087 (heading) | none | none | none | (inert: heading) |
| s 1087(1) | a person whose protected material is listed (kept from public inspection) | the registrar (must not make it available) | claim / duty | `s 1087(1) the registrar must not make the material available for public inspection`; `s 1087(1) the prohibition on making protected material available for public inspection` |
| s 1087(2) | none | none | none | `s 1087(2) the restriction affects the availability for public inspection of the same information in the other material` |
| s 1087(3) | the registrar (need not retain longer than necessary) | none named | liberty / no-right | `s 1087(3) the registrar need not retain the material for longer` |
| s 1087ZA | none | none | none | (blank in this text) |
| s 1087A (heading) | none | none | none | (inert: heading) |
| s 1087A(1) | a director or registrable person (day of birth withheld) | the registrar (must not make it available) | claim / duty | `s 1087A(1) the registrar must not make the material available for public inspection`; `s 1087A(1) the prohibition on making relevant date of birth information available for public inspection` |
| s 1087A(2) | none | none | none | (inert) |
| s 1087A(3) | none | none | none | `s 1087A(3) the information is relevant date of birth information` |
| s 1087A(4) | none | none | none | `s 1087A(4) the information has ceased to be relevant date of birth information` |
| s 1087A(5) | none | none | none | `s 1087A(5) subsection (1)(b) affects the availability of the same information in that material` |
| s 1087A(6) | none | none | none | `s 1087A(6) the person is a registrable person in relation to the company` |
| s 1087B (heading) | none | none | none | (inert: heading) |
| s 1087B(1) | none | none | none | `s 1087B section 1087A applies to the old document` |
| s 1087B(2) | none | none | none | `s 1087B section 1087A applies to the old document` |
| s 1087B(3) | none | none | none | `s 1087B section 1087A applies to the old document` |
| s 1087B(4) | none | none | none | `s 1087B section 1087A applies to the old document` |
| s 1087B(5) | none | none | none | `s 1087B(5) the reference is to the provision as it had effect at the time at which the document was delivered` |
| s 1087C (heading) | none | none | none | (inert: heading) |
| s 1087C(1) | a director or registrable person (day of birth not disclosed) | the registrar (must not disclose except as (2), (3) or section 1110F permit) | claim / duty (an "except" bar) | `s 1087C(1) the registrar is barred from disclosing the relevant date of birth information`; `s 1087C(1) the prohibition on disclosing relevant date of birth information` |
| s 1087C(2) | the registrar (may disclose what is public) | none named | liberty / no-right | `s 1087C(2) the registrar may disclose the relevant date of birth information` |
| s 1087C(3) | the registrar (may disclose to a credit reference agency) | none named | liberty / no-right | `s 1087C(3) the registrar may disclose the relevant date of birth information to the recipient` |
| s 1087C(4) | none | none | none | `s 1087C(3) the registrar may disclose the relevant date of birth information to the recipient` |
| s 1087C(5) | none | none | none | `s 1087C(5) the information is relevant date of birth information` |
| s 1088 (heading) | none | none | none | (inert: heading) |
| s 1088(1) | Secretary of State | the registrar; persons whose information is protected | power / liability | (inert) |
| s 1088(2) | Secretary of State | the registrar; persons whose information is protected | power / liability | (inert) |
| s 1088(3) | Secretary of State | the registrar; persons whose information is protected | power / liability | (inert) |
| s 1088(4) | Secretary of State | the registrar; persons whose information is protected | power / liability | (inert) |
| s 1088(5) | Secretary of State | the registrar; persons whose information is protected | power / liability | (inert) |
| s 1088(6) | Secretary of State | the registrar; persons whose information is protected | power / liability | (inert) |
| s 1088(7) | the registrar (must remain free to disclose under the named provisions) | the Secretary of State (disabled from requiring otherwise) | immunity / disability | `s 1088(7) regulations under subsection (1)(b) or (2)(b) may require the registrar to refrain from disclosing information under the provision` |
| s 1088(8) | the registrar (must remain free to disclose under section 1110F) | the Secretary of State (disabled) | immunity / disability | `s 1088(8) regulations under subsection (1)(d) may require the registrar to refrain from disclosing information under the provision` |
| s 1088(9) | Secretary of State | the registrar; persons whose information is protected | power / liability | (inert) |
| s 1088(10) | none | none | none (procedure for regulations) | (inert) |
| s 1089 (heading) | none | none | none | (inert: heading) |
| s 1089(1) | the registrar (may specify the form of application) | a person who applies to inspect or copy | power / liability | `s 1089(1) the registrar may specify the form and manner in which the application is to be made` |
| s 1089(2) | none | none | none | (blank in this text) |
| s 1090 | the registrar (may determine the form of copies) | a person who requests a copy | power / liability | `s 1090 the registrar may determine the form and manner in which the copy is provided` |
| s 1091 (heading) | none | none | none | (inert: heading) |
| s 1091(1) | an applicant who expressly requests certification | the registrar (must certify) | claim / duty | `s 1091(1) the registrar must certify the copy as a true copy`; `s 1091(1) the registrar's duty to certify the copy` |
| s 1091(3) | a person relying on a certified copy in proceedings | anyone who would object to its admission | immunity / disability | `s 1091(3)(a) the certified copy is admissible in all legal proceedings as of equal validity with the original document`; `s 1091(3)(b) what the certified copy is as evidence of the fact` |
| s 1091(4) | Secretary of State | the registrar | power / liability | (inert) |
| s 1091(5) | the registrar (may seal instead of certifying) | none named | liberty / no-right | `s 1091(5) the copy may be sealed with the registrar's official seal instead of being certified in writing` |
| s 1092 (heading) | none | none | none | (inert: heading) |
| s 1092(1) | a person from whom the registrar's records are sought (no process without the court's permission) | a litigant seeking process (barred without permission) | immunity / disability (an "except" bar) | `s 1092(1) the issue of the process from the court is barred` |
| s 1092(2) | none named | the issuer of the process (must state that it is issued with permission) | duty | `s 1092(2) the process bears the statement it must bear` |
| s 1092A (heading) | none | none | none | (inert: heading) |
| s 1092A(1) | the registrar (may require information by notice) | a person required to provide it | power / liability | `s 1092A(1) the registrar may require the person to provide the information` |
| s 1092A(2) | the registrar (may specify form, manner and period) | the person required | power / liability | `s 1092A(2) a requirement under section 1092A may specify the matter` |
| s 1092A(3) | the registrar (may extend the period) | the person required | power / liability | `s 1092A(3) the registrar may extend the period` |
| s 1092B (heading) | none | none | none | (inert: heading) |
| s 1092B(1) | the Crown (the offence of failing without reasonable excuse) | a person who fails to comply with a requirement under section 1092A | claim / duty | `s 1092B(1) the person commits an offence` |
| s 1092B(2) | the Crown | an officer of a firm who is in default | claim / duty | `s 1092B(2) an offence is also committed by the officer` |
| s 1092B(3) | the Crown (penalty) | the offender | power / liability | `s 1092B(3) the penalty for the offence` |

## Marginal readings for a lawyer (coa23)

Every branch below rests on one of the two readings the brief marks "for a lawyer": (a) a failed "if" counts as the text's no, clause by clause, within the provision that holds the "if" (an inference: "if A then B" does not itself say "if not A then not B"), and flat negatives count as the text saying no; (b) a prohibition or grant limited by its own wording does not (the case outside the limit answers NOTHING). The other reading is stated for each.

| function(s) | branch | rests on | the other reading |
| --- | --- | --- | --- |
| `s 1046(2)` | JUST FALSE for a company other than a Gibraltar company that opens no branch | (a): "(a) must ... if the company opens a branch" | NOTHING ((c) lets the regulations require registration in other circumstances) |
| `s 1066(3)`, `s 1067(3)` | JUST FALSE when the registrar is not adopting a new form | (a), with "on adopting" read as "upon" (ruling of 2026-11-05 (c)) | NOTHING (limited by its own wording) |
| `s 1074(4)`, `s 1091(1)`, `s 1079(3)` | JUST FALSE when the "if" fails | (a): "If the unnecessary material ...", "must be certified ... if", "If the material time falls ..." | NOTHING ("if" does not say "only if") |
| `s 1073A(1)` (F28) | NOTHING when the "if" of "may refuse ... if" fails (name-test sweep of 2026-11-12: a grant named "may") | the Guide: a grant limited in its own wording | JUST FALSE ((a): a failed "if" read as the text's own no) |
| `s 1074(5)` (F29) | NOTHING when the "If the unnecessary material can readily be separated" gate fails (a grant named "may") | the Guide: a grant limited in its own wording | JUST FALSE ((a)) |
| `s 1081(4)` (F30) | NOTHING when the note still serves a useful purpose ("may be removed if"; a grant named "may") | the Guide: a grant limited in its own wording | JUST FALSE ((a)) |
| `s 1087C(2)` (F31) | NOTHING when the information is not made available for public inspection ("may disclose ... if"; a grant named "may") | the Guide: a grant limited in its own wording | JUST FALSE ((a)) |
| `s 1080(4)`, `s 1083(1)`, `s 1083(2)` | JUST FALSE when a "provided" condition is not met | (a): "provided it is possible to inspect it and produce a copy of it", "provided the information ... has been recorded" | NOTHING |
| `s 1048(4)`, `s 1054(3)(a)`, `s 1073(3)`, `s 1073(4)(a)`, `s 1073(5)`, `s 1081(3)`, `s 1087(2)`, `s 1087A(4)`, `s 1087A(5)`, `s 1088(7)`, `s 1088(8)`, `s 1068(7)`, `s 1068A(2)` | JUST FALSE where the flat negative fits the case | (a): flat negatives count as the text's no (ruling N2, bench `commons-negation-1030`, option A) | NOTHING |
| `s 1067A(1)`, `s 1067A(2)`, `s 1067B(2)`, `s 1076(2)`, `s 1079(1)`, `s 1087C(1)`, `s 1092(1)` | JUST FALSE for the bar once the "unless" or "except" is met | the 2026-11-05 case-by-case ruling (fork F9) | NOTHING |
| `s 1044`, `s 1046(3)`, `s 1050(2)`, `s 1052(6)`, `s 1074(2)`, `s 1080(2)`, `s 1084A(2)`, `s 1087A(3)` and the other "means" definitions | JUST FALSE when the definition's terms are not met | a definition by "means" is closed | NOTHING |
| `s 1078`, `s 1079(2)`, `s 1079(4)`, `s 1084(1)`, `s 1079B(1)` | JUST FALSE for a case in no head of the list | ruling of 2026-11-05, delegated definitions (a), and "where" (b) and (c) | NOTHING |
| `s 1048(1)`, `s 1048(2)`, `s 1048(5)`, `s 1053(1)`, `s 1048B(1)`, `s 1050(1)`, `s 1051(2)(a)`, `s 1057(1)`, `s 1062`, `s 1062A(1)`, `s 1063(5)`, `s 1064(1)`, `s 1065`, `s 1066(1)`, `s 1067(1)`, `s 1070(1)`, `s 1070(2)`, `s 1073(1)`, `s 1076(1)`, `s 1076(3)`, `s 1077(1)`, `s 1079B(2)`, `s 1080(1)`, `s 1085(1)`, `s 1086(1)`, `s 1087(1)`, `s 1087A(1)`, `s 1092A`, `s 1092B(1)` and (2) | NOTHING outside the limit each states (a relative clause, "any", "such ... as") | (b): a grant or duty limited by its own wording | JUST FALSE outside the limit |
| `s 1054(3)(b)` | NOTHING for a fine within both limits | (b), and fork F2 | JUST TRUE (the fine is permitted) |
| `s 1092B(1)` | NOTHING where the person has a reasonable excuse | the case-by-case ruling of 2026-11-05, and (b): "without reasonable excuse" limits the offence in its own wording (fork F26; ss 1098E(3), 1112(1), 1203(4) and 1205(1) of other parts answer NOTHING for the same wording) | JUST FALSE (the exception is the text's own no: the excused person commits no offence) |

### Reading a result: FALSE and NOTHING (coa23)

The rule of 2026-10-29 (assumed, not ruled by a lawyer) as it reads in Part 34 and the first half of Part 35. Nearly every function answers `MAYBE BOOLEAN`. The exceptions answer a value the text names: a `Place of registration` (s 1058(2)), what the regulations must require an overseas company to register (s 1056), the registrar for a place (ss 1060(3), (4)), a `Penalty` (s 1092B(3)), a date (ss 1071, 1066(5), 1078(4)(b)), the note a registrar must write (s 1081(1)), which row of a list a section number falls in (s 1047(4)) and the head of a list a person names (ss 1078, 1087(1)); where the text names no value for a case those answer `NOTHING` inside a `MAYBE`, or a "another ..." constructor.

- `JUST TRUE`: the Act says yes to the case: the definition is met, the duty is engaged, the right exists, the period has run, the document is delivered as required.
- `JUST FALSE` ("a no"): the Act says no in its own words: a "means" definition not met ("an “overseas company” means a company incorporated outside the United Kingdom"); a failed "if", "where", "provided" or "on adopting" (except in a function named for a grant, where a failed "if" answers NOTHING: forks F28 to F31, and F32 to F37 for the grants whose gate is not an "if"); a flat negative ("The regulations must not provide ... for imprisonment", "No objection may be taken ...", "does not affect"); a period the text fixes ("for a period of three years beginning with that date", "after the end of the period of 20 years"); a bare "must" not done in a compliance function; or, in a function named for a bar, the bar once its "unless" or "except" is met. Each such branch carries `-- FALSE-kind (the text says no in its own words): "<the quoted words>"`.
- `NOTHING` ("not covered"): the Act does not decide the case: it lists without closing the list ("include", "may specify" two matters), is silent, leaves a term undefined, points to regulations, registrar's rules, an enactment or an instrument outside the sources (the Eleventh Company Law Directive, the Insolvency Act 1986, the 2014 Regulations on payments to governments, the general limit in a magistrates' court), or limits a grant or duty in its own wording ("An overseas company that is required to register particulars ... may", "such analysis ... as the registrar considers appropriate") and the case falls outside the limit. Each such branch carries `-- NOTHING-kind (<why>)`, with <why> one of silent, list not closed, includes, undefined term, points outside the text, limited by its own wording.
- A caller must never turn `NOTHING` into `FALSE`. A seam input of another part is a `MAYBE BOOLEAN`: its `NOTHING` makes the answer `NOTHING` (points outside the text), never `FALSE`. The seat passes a person's yes or no as `JUST yes` or `JUST no` (fork F25), so a seat answer is `NOTHING` only where the Act itself says nothing.
- Four kinds of answer deserve care. In a function named for a bar ("is barred from"), `JUST FALSE` means the bar does not apply, and is not a permission (fork F9). In a function named "the regulations must ...", `JUST FALSE` means the Act does not require it of the regulations. In a regulative rule's twin, `JUST FALSE` means the duty was not done. In `s 1071(1) the document cannot yet count as delivered`, `JUST FALSE` means the bar is lifted and the text does not itself say the document has been delivered (ruling of 2026-11-05 (d)).
- `REFUSE` does not exist on the stable binary and is not used: "not covered" is `NOTHING` or a named constructor, asserted in the tests.

## Seams (coa23)

Where `inputs/PLAN.md` and the brief differ, the brief governs. They differ in two places that matter here: PLAN section 4.2 names the receipt seam `s 1071 the day the registrar received the document` (DATE) and section 6 says "the date"; the 4.2 spelling is used, and its type is `MAYBE DATE` (not `DATE`) so that "not received yet" stays `NOTHING`. PLAN section 4 says a seam is `MAYBE BOOLEAN` by default; where the keel's answer never says NOTHING (section 4(2) public company) the input is a plain `BOOLEAN`, as PLAN allows.

### Seam inputs taken (the answering part computes them; the lead wires the answer to the input at the merge)

| input (the name the GIVEN carries) | type | asked by | answered by |
| --- | --- | --- | --- |
| `s 4(2) the company is a public company` | BOOLEAN | `s 1078` (a public company's heads) | keel, `coa-definitions.l4` |
| `s 1(1) the body is a company` | MAYBE BOOLEAN | `s 1066(1)` | keel |
| `s 1110A the individual's identity is verified` | MAYBE BOOLEAN | `s 1067A(1)`; the field `s 1067A(2) A's identity is verified, the answer of section 1110A` (rows 1, 2, 5) | coa24 |
| `s 1098A the individual is an authorised corporate service provider` | MAYBE BOOLEAN | `s 1067B(2)`; the field `s 1067A(2) A is an authorised corporate service provider, the answer of section 1098A` (rows 3, 6) | coa24 (PLAN names the seam by heading: "Meaning of “authorised corporate service provider”") |
| `s 159A(2) the person is disqualified under the directors disqualification legislation` | MAYBE BOOLEAN | `s 1067B(6)` | coa4 (a seam PLAN lacks: found in the text of s 1067B(6)) |
| `s 1116 the notice was published in accordance with section 1116 (alternative means of giving public notice)` | MAYBE BOOLEAN | `s 1064(1)`, `s 1077(1)` | coa24 |
| `s 1102 the requirements of this Part as to the language of the document and any certified translation are met` | MAYBE BOOLEAN | `s 1072` limb (c) | coa24 (ss 1102 to 1107) |
| `s 1108 the requirements of this Part as to permitted characters and any certificate as to transliteration are met` | MAYBE BOOLEAN | `s 1072` limb (d) | coa24 (ss 1108 to 1110) |
| `s 1111 the applicable requirements as to certification or verification are met` | MAYBE BOOLEAN | `s 1072` limb (e) | coa24 |
| the requirements of the provision under which a document is delivered (contents; form, authentication, manner) | MAYBE BOOLEAN (two inputs) | `s 1072` limbs (a)(i), (a)(ii) | the part that owns the filing section |
| `s 1121 the officer is in default` | MAYBE BOOLEAN | `s 1092B(2)` | coa24 |
| `s 1110F the disclosure is permitted by the registrar's general powers of disclosure` | MAYBE BOOLEAN | `s 1087C(1)` | coa24 |
| `s 243(7) the recipient is a credit reference agency`, `s 243(3) to (8) the conditions of those subsections, read as section 1087C(4) says, are met` | MAYBE BOOLEAN | `s 1087C(3)` | coa5 |
| `s 790C(4) the person is a registrable person in relation to the company` | MAYBE BOOLEAN | `s 1087A(6)` | coa17 |
| `section 86(2) says the address is an appropriate address`, `section 88A(2) says the address is an appropriate email address` | MAYBE BOOLEAN | `s 1048A(4)` | coa2 |
| `the Eleventh Company Law Directive (89/666/EEC) says the establishment is a branch` and `a branch within the meaning of the Eleventh Company Law Directive (89/666/EEC)` | MAYBE BOOLEAN | `s 1046(3)`, `s 1067(6)` | no part (a Directive outside the sources) |
| `the 15th day after the date of official notification was a working day`, `the next day after that 15th day that was a working day` | BOOLEAN, DATE | `s 1079(3)` | the facts that `s 1173(1) the day is a working day for the company` (keel) answers |
| the registrar's rules as to when a document is regarded as received (`the day on which the document is regarded as received under registrar's rules`) | DATE | `s 1071` | no part (registrar's rules are outside the sources) |

### Answers coa23 gives to other parts (named as PLAN section 4.2 and section 6 name them)

| answer | name and type | asked by (PLAN) |
| --- | --- | --- |
| requirements for proper delivery | `s 1072 the document meets the requirements for proper delivery` (MAYBE BOOLEAN) | every part with a filing duty |
| the day of receipt | `s 1071 the day the registrar received the document` (MAYBE DATE) | every part with a filing duty |
| the registrar's official seal | `s 1062 the document bears the registrar's official seal` (MAYBE BOOLEAN) | coa1, coa14, coa19 |
| enhanced disclosure documents | `s 1078 the document is an enhanced disclosure document` (MAYBE BOOLEAN) | coa10, coa11, coa13 to coa16, coa18, coa20, coa2, coa8 (the Act's index entry) |
| the register | `s 1080(2) the record is part of the register` (MAYBE BOOLEAN) | every part that says "the register" |
| the registrar | `s 1060(3) the registrar of companies, as the case may require, for the place` and `s 1060(4) registration in the part of the United Kingdom is registration by` (`s 1060 registrar of companies`) | every part |
| overseas company | `s 1044 the company is an overseas company` (MAYBE BOOLEAN) | the keel (s 1(3)) and others |
| registered number (company; UK establishment) | `s 1066(1) ...`, `s 1066(5) ...`, `s 1067(1) ...`, `s 1067(5) ...` | coa2 (s 82) |
| establishment; UK establishment of an overseas company | `s 1067(6) the place is an establishment of the overseas company`, `s 1067(6) the establishment is a UK establishment of the overseas company` | the Act's index |
| unique identifier | `s 1082(1) regulations may provide for a unique identifier to identify the person` | the Act's index (Schedule 8) |

### Seams the plan lacks (found in the text of this range)

`s 1067B(6)` to s 159A(2) (coa4); `s 1087A(6)` to s 790C(4) (coa17); `s 1087C(3)` and (4) to s 243 (coa5); `s 1072(1)(c)` to (e) to ss 1102 to 1111 (coa24, named by heading as PLAN section 4 says); `s 1085(3)` to the provisions that suppress a name (ss 64(6A), 67(1A), 73(7), 75(4A), 76(5B), 76A(9), 76B(9): coa2) and to s 1087 (this range): carried as one input of `s 1085(1)`; `s 1083(1)` to s 1087(3) (this range), s 16A(2) of the Limited Partnerships Act 1907 and s 22(5) of the Economic Crime (Transparency and Enforcement) Act 2022 (outside the sources): carried as one input.

### Section 1173(1) "working day" and PLAN's naming rule

A GIVEN named exactly as another part's function (for example `s 1110A the individual's identity is verified`) shadows nothing in its own function, and a probe importing `coa-definitions.l4` with `coa23-part35-delivery.l4` ran clean (a GIVEN `s 4(2) the company is a public company` beside the keel's function of that name). No record field and no top-level name equals another part's function name: the fields that carry the section 1110A and 1098A answers are named `s 1067A(2) A's identity is verified, the answer of section 1110A` and `s 1067A(2) A is an authorised corporate service provider, the answer of section 1098A`.

## Findings: what the text turns out to say

1. **Part 34 itself puts almost no duty on an overseas company.** Every duty is one the Secretary of State "may" put into regulations that are not among the sources. What the Act itself fixes are the limits on those regulations: they "must" require a company other than a Gibraltar company that opens a branch to register particulars (s 1046(2)(a)), must require registration of a name (s 1047(1)), the disclosure of the registered name (s 1051(2)(a)), protection of a residential address (s 1055), particulars of UK-resident persons authorised to accept service or a statement that there are none (s 1056), and notice to the registrar of the part where the first return went (s 1058(2)); and they "must not" provide for imprisonment or for fines above the limits of s 1054(3). The seat questions are worded "must the regulations require ...".
2. **s 1054(3)(b) joins two wordings of its last limb** ("...one-tenth of level 5 on the standard scaleone-tenth of the greater of £5,000 or level 4 on the standard scale.", line 14842); see fork F2. The text file's own caveat says it "may carry more than one extent version of a provision".
3. **s 1059A(2) joins two wordings of one line**: "sections 1068 1067A to 1071" (line 14873); fork F3. Without the reading "1067A to 1071", ss 1067A and 1067B are in none of the three lists.
4. **"Delivered" means "received".** s 1071(1): "A document is not delivered to the registrar until it is received by the registrar", and the day of receipt is for registrar's rules (s 1071(2)). A document that is received is still not "properly delivered" unless all eleven limbs of s 1072(1) are met (contents, form, authentication, manner, who may deliver, the registrar's requirements, language, permitted characters, certification, unique identifiers, the fee), and an improperly delivered document is treated as not delivered, subject to the registrar's power to accept it (ss 1072(2), 1073(1)).
5. **Acceptance of an improper document stops the default clock** (s 1073(5)): the period after acceptance does not count as default for section 453 or for a daily default fine, until fourteen days after a notice of removal from the register issued under regulations under section 1094A(1) pass without compliance (s 1073(6)), when "any subsequent period of default does count". The 14 days and the day after are tested.
6. **Who may deliver is a table, and the identity-verification asymmetry is the Act's own** (s 1067A). An individual delivering for themselves, and any officer or employee of a firm (or of its corporate officer) delivering for the firm, must have a verified identity and say so; an authorised corporate service provider, and its officers and employees, deliver for a firm or an individual with a statement of status and of the capacity in which they deliver and no identity-verification limb (rows 3, 4, 6 and 7). The table's cells were run together by the converter ("Statement by A—that A is an officer or employee of the firm,that A is delivering the document on the firm’s behalf, andthat A’s identity is verified"): each statement is a separate item (a text anomaly, not repaired).
7. **A disqualified person is barred from delivering any document to the registrar, for themselves or anyone else** (s 1067B(1)); no one may deliver for a disqualified person unless an authorised corporate service provider or its officer or employee (s 1067B(2)); and every document carries two statements (s 1067B(3) to (5)).
8. **The company's reliance on an unnotified event is barred** (s 1079(1)): for the five events of s 1079(2) the company may not rely on the event against others unless it was officially notified at the material time or the company shows the person knew; and for fifteen days after official notification (to the next working day if the 15th is not one) it still may not as against a person who was unavoidably prevented from knowing (s 1079(3)).
9. **Public inspection is "any person", with exceptions** (s 1085(1)); the originals of hard copy documents may be inspected "if, and only if" the record is illegible or unavailable (s 1085(2)); a copy of anything available for inspection may be required (s 1086(1)), and for material from an enhanced disclosure document the fee may not exceed the administrative cost (s 1086(2)).
10. **What is kept from the public is a list of 39 items (paragraphs, sub-paragraphs and the ten provisions of paragraph (gd)) plus "any other material excluded ... by or under any other enactment"** (s 1087(1)): the email addresses, comments on names, protected residential address information and the representations about it, identity-verification statements (ten provisions), and so on.
11. **Only the day of the month of a birth is protected** (s 1087A(3)): "information as to the day of the month (but not the month or year)". The month and year are not "relevant date of birth information" under this section. It does not cease to be relevant when the person ceases to be a director (s 1087A(4)). For old documents the protection is carved back (s 1087B): none for documents registered before 10 October 2015, none for the documents of (3)(a) to (e), and none for a section 9 statement or a section 167 notice where an election was made under s 167A and the information relates to a person who was then a director.
12. **The offence of not giving the registrar information** (s 1092B): without reasonable excuse, failing to comply with a requirement under s 1092A; an officer of a firm in default commits it too. The penalty differs by place: two years or a fine (or both) on indictment; in England and Wales imprisonment up to "the general limit in a magistrates' court" (a figure the Act does not give) or a fine; in Scotland 12 months or a fine up to the statutory maximum and a daily default fine of one-fifth of it; in Northern Ireland 6 months and the same fines.
13. **s 1085, s 1086, s 1065: the text names a right of "any person" and does not name the registrar's correlative duty**; the Jural relations table marks it implied.
14. **Text anomalies, none repaired** (lines of `ukpga-2006-46.txt`): "accountsand" (14764 and 14781); "...,, and" (15233, s 1080(1)(a)); s 1083(1) says "This is subject to" twice (15296 and the list that follows; fork F14); s 1084(3) refers to "subsection (2) or (2A)" (15311) and the text has (2) and (2AA) (15309, 15310; fork F19); s 1091 has subsections (1), (3), (4), (5) and no (2) (15458 to 15463); s 1047(4) begins "... The following provisions" and its paragraphs are lettered (a), (aa), (b), (bza), (ba), (bb), (bc), (bd), (c) to (j), the (bc) line ending with a full stop (14710 to 14726); a list row of s 1072(1)(b) is "..." (15090) and a line "..." follows s 1078(1) (15151, part of that subsection's lines); the 18 coverage rows `repealed or blank in this text` are ss 1047(3), 1047(5), 1061(2), 1068(5), 1068(6), 1068(6A), 1069, 1075, 1079A, 1081(1)(b), 1081(1A), 1084(4A), 1084(5), 1086(3), 1087(1)(h), 1087ZA, 1089(2) and the "..." row of s 1072(1)(b).
15. **The only pound figure the text states for a provision in force is the "£5,000" of s 1054(3)(b)** (the other, "5p", is inside words that s 1063(7)(a)(i) omits from the Limited Partnerships Act 1907); every other amount (levels on the standard scale, the statutory maximum, fees, the magistrates' court limit) is outside the text and is an input.

## What the stable binary does not accept, and what it does (measured on 2026-11-13 with `L4_BIN`, 1.6.110 (main, e51181d, 2026-11-11), and with `L4_MAIN`, 1.6.109)

Rejected or unavailable (loud):

- `#ASSERT <deontic value> EQUALS FULFILLED` is an error: `assertion could not be evaluated: Trying to check equality on types that do not support it` (the deontic value is printed beside `FULFILLED`). So a regulative rule cannot be asserted on this binary. Every regulative rule of the modules (19 rules) is run with `#TRACE`, which prints an `eval/result` Information line that `check.sh` does not count, and is twinned with a decision function that IS asserted. The 34 traces are listed below with the outcome each `-- EXPECT:` line states; the same 34 give the same outcome on 1.6.109 and 1.6.110 (checked by running each test file with both builds and comparing the printed result with the `-- EXPECT:` line).
- `srcrefs.py` refuses a quote of a raw line that holds only punctuation (`...`): R1 "quotation has no text". The "..." lines of the text (15090, 15151) are left out of the quote runs; their `@ref` locators still span them.

Accepted although the brief says the stable line does not have them (a surprise, not a licence; none is used): `REFUSE`, `#ASSERT REFUSED`, `YMD` (the keel measured the same). `grep` finds none of the three in any `coa23-*.l4`; `BECAUSE` occurs only in `LEST BREACH BY ... BECAUSE "..."`.

Measured and used:

- `NOT a AND b` parses as `NOT (a AND b)`. Two functions written without brackets hid wrong answers: `s 1074(2)` (the case "not necessary and authorised" answered JUST TRUE) and `s 1073(5)` (a complied-with case inside the 14 days answered JUST TRUE); both were found by the tests, fixed with brackets, and have regression assertions.
- `Date d m (y + N)` rolls an impossible day forward (a 29 February anniversary becomes 1 March), which fork F12 uses for the end of a period of years; `add years` clamps to 28 February and was not used for periods.
- `elem` works on a `LIST OF MAYBE BOOLEAN` and on a list of constructors; `concat (LIST ...)` flattens a list of lists; a recursive `CONSIDER` over a `LIST OF` record works (s 1067A(3)).
- A rule applied to constructors with `PROVIDED` guards over wildcard names (`SHANT ... verified statement PROVIDED (NOT verified) OR (NOT statement)`) gives the same outcomes on both builds (dialects.md: the guard form is the portable one). A `MUST` or `SHANT` with no `WITHIN` stays a residual obligation after a `WAITUNTIL`: no deadline is invented.
- A `GIVEN` named like another part's function (`s 4(2) the company is a public company`) shadows nothing and checks clean beside the keel's function.
- A seat function with no `GIVEN` (the question on s 1054(3)(a)) checks clean with `@export`; whether the website form renders a question with no inputs, or a `MAYBE` answer, was not tried (no service is available here).

### Regulative rules: trace outcomes (not asserted; checked as stated above)

| test file | rule | events | outcome |
| --- | --- | --- | --- |
| coa23-tests-part35-delivery.l4 | `s 1077(1) the registrar's duty to publish notice of the receipt of an enhanced disclosure document` | `DOES Action of a party OF Registrar, Company, "publish notice of the receipt of the enhanced disclosure docume...` | FULFILLED |
| coa23-tests-part35-delivery.l4 | `s 1077(1) the registrar's duty to publish notice of the receipt of an enhanced disclosure document` | `(WAITUNTIL 30)` | RESIDUAL |
| coa23-tests-part35-delivery.l4 | `s 1079B(2) the registrar's duty to notify the person named as a director` | `DOES Action of a party OF Registrar, Director, "notify the person named in the document as a director of the c...` | FULFILLED |
| coa23-tests-part35-delivery.l4 | `s 1079B(2) the registrar's duty to notify the person named as a director` | `(WAITUNTIL 30)` | RESIDUAL |
| coa23-tests-part35-register.l4 | `s 1080(1) the registrar's duty to keep records` | `DOES Action of a party OF Registrar, Registrar, "keep records of the information contained in documents delive...` | FULFILLED |
| coa23-tests-part35-register.l4 | `s 1080(1) the registrar's duty to keep records` | `(WAITUNTIL 30)` | RESIDUAL |
| coa23-tests-part35-register.l4 | `s 1080(3) the registrar's duty to keep information from an enhanced disclosure document in electronic form` | `DOES Action of a party OF Registrar, Registrar, "keep the information deriving from an enhanced disclosure doc...` | FULFILLED |
| coa23-tests-part35-register.l4 | `s 1081(1) the registrar's duty to place a note in the register` | `DOES Action of a party OF Registrar, Registrar, "place a note in the register recording the matters section 10...` | FULFILLED |
| coa23-tests-part35-register.l4 | `s 1081(1) the registrar's duty to place a note in the register` | `(WAITUNTIL 30)` | RESIDUAL |
| coa23-tests-part35-register.l4 | `s 1081A(1) the registrar's duty to seek to promote the objectives` | `DOES Action of a party OF Registrar, Registrar, "seek to promote the four objectives of section 1081A(1) in pe...` | FULFILLED |
| coa23-tests-part35-register.l4 | `s 1083(1) the registrar's duty to keep the original of a hard copy document` | `DOES Action of a party OF Registrar, Registrar, "keep the original of a document delivered in hard copy form f...` | FULFILLED |
| coa23-tests-part35-register.l4 | `s 1083(1) the registrar's duty to keep the original of a hard copy document` | `(WAITUNTIL 30)` | RESIDUAL |
| coa23-tests-part35-register.l4 | `s 1085(1) the right of any person to inspect the register` | `DOES s 1085 inspect the register AT 1` | FULFILLED |
| coa23-tests-part35-register.l4 | `s 1086(1) the right of any person to a copy of material on the register` | `DOES s 1086 require a copy of material on the register AT 1` | FULFILLED |
| coa23-tests-part35-register.l4 | `s 1087(1) the prohibition on making protected material available for public inspection` | `DOES Action of a party OF Registrar, Registrar, "make material listed in section 1087(1), so far as it forms p...` | BREACH |
| coa23-tests-part35-register.l4 | `s 1087(1) the prohibition on making protected material available for public inspection` | `(WAITUNTIL 30)` | RESIDUAL |
| coa23-tests-part35-register.l4 | `s 1087A(1) the prohibition on making relevant date of birth information available for public inspection` | `DOES Action of a party OF Registrar, Registrar, "make available for public inspection any part of a document r...` | BREACH |
| coa23-tests-part35-register.l4 | `s 1087A(1) the prohibition on making relevant date of birth information available for public inspection` | `(WAITUNTIL 30)` | RESIDUAL |
| coa23-tests-part35-register.l4 | `s 1087C(1) the prohibition on disclosing relevant date of birth information` | `DOES Action of a party OF Registrar, Registrar, "disclose relevant date of birth information otherwise than as...` | BREACH |
| coa23-tests-part35-register.l4 | `s 1087C(1) the prohibition on disclosing relevant date of birth information` | `(WAITUNTIL 30)` | RESIDUAL |
| coa23-tests-part35-register.l4 | `s 1091(1) the registrar's duty to certify the copy` | `DOES Action of a party OF Registrar, Registrar, "certify the copy provided under section 1086 as a true copy" ...` | FULFILLED |
| coa23-tests-part35-register.l4 | `s 1091(1) the registrar's duty to certify the copy` | `(WAITUNTIL 30)` | RESIDUAL |
| coa23-tests-part35-registrar.l4 | `s 1062A(1) the registrar's duty to analyse information` | `DOES Action of a party OF Registrar, Registrar, "analyse information within the registrar's possession for the...` | FULFILLED |
| coa23-tests-part35-registrar.l4 | `s 1062A(1) the registrar's duty to analyse information` | `(WAITUNTIL 30)` | RESIDUAL |
| coa23-tests-part35-registrar.l4 | `s 1064(1) the registrar's duty to publish notice of the issue of a certificate of incorporation` | `DOES Action of a party OF Registrar, Company, "publish notice of the issue of the certificate of incorporation...` | FULFILLED |
| coa23-tests-part35-registrar.l4 | `s 1064(1) the registrar's duty to publish notice of the issue of a certificate of incorporation` | `(WAITUNTIL 30)` | RESIDUAL |
| coa23-tests-part35-registrar.l4 | `s 1065 the right of any person to a copy of a certificate of incorporation` | `DOES s 1065 require a copy of a certificate of incorporation AT 5` | FULFILLED |
| coa23-tests-part35-registrar.l4 | `s 1067A(1) the prohibition on an individual delivering a document on their own behalf` | `DOES s 1067A deliver a document on their own behalf FALSE TRUE AT 1` | BREACH |
| coa23-tests-part35-registrar.l4 | `s 1067A(1) the prohibition on an individual delivering a document on their own behalf` | `DOES s 1067A deliver a document on their own behalf TRUE FALSE AT 1` | BREACH |
| coa23-tests-part35-registrar.l4 | `s 1067A(1) the prohibition on an individual delivering a document on their own behalf` | `DOES s 1067A deliver a document on their own behalf TRUE TRUE AT 1` | RESIDUAL |
| coa23-tests-part35-registrar.l4 | `s 1067B(1) the prohibition on a disqualified individual delivering documents` | `DOES s 1067B deliver documents on their own behalf or on behalf of another as a disqualified person AT 1` | BREACH |
| coa23-tests-part35-registrar.l4 | `s 1067B(1) the prohibition on a disqualified individual delivering documents` | `(WAITUNTIL 30)` | RESIDUAL |
| coa23-tests-part35-registrar.l4 | `s 1070(3) the duty to deliver in accordance with the agreement` | `DOES Action of a party OF Company, Registrar, "deliver the document in accordance with the agreement" AT 4` | FULFILLED |
| coa23-tests-part35-registrar.l4 | `s 1070(3) the duty to deliver in accordance with the agreement` | `(WAITUNTIL 30)` | RESIDUAL |

## What `check.sh` printed

Run as `L4=<L4_BIN> L4_MAIN=<L4_MAIN> ./check.sh` (target `main`: every module is also run with the second build and the counts compared). `expected_failed` is empty: no assertion is meant to fail.

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.109 (main, 4c887e0, 2026-11-04)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
coa-core.l4                                    0         0       0        0         0 |      0         0       0        0  same
coa-definitions.l4                             0         0       0        0         0 |      0         0       0        0  same
coa23-cases-seat.l4                            0       165       0        0         0 |      0       165       0        0  same
coa23-nouns.l4                                 0         0       0        0         0 |      0         0       0        0  same
coa23-part34.l4                                0         0       0        0         0 |      0         0       0        0  same
coa23-part35-delivery.l4                       0         0       0        0         0 |      0         0       0        0  same
coa23-part35-register.l4                       0         0       0        0         0 |      0         0       0        0  same
coa23-part35-registrar.l4                      0         0       0        0         0 |      0         0       0        0  same
coa23-seat.l4                                  0         0       0        0         0 |      0         0       0        0  same
coa23-tests-part34.l4                          0       133       0        0         0 |      0       133       0        0  same
coa23-tests-part35-delivery.l4                 0       240       0        0         0 |      0       240       0        0  same
coa23-tests-part35-register.l4                 0       288       0        0         0 |      0       288       0        0  same
coa23-tests-part35-registrar.l4                0       316       0        0         0 |      0       316       0        0  same
TOTAL (13 modules)                             0      1142       0        0           |      0      1142       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

The baseline it replaced (the same command over the keel's `coa-core.l4` and `coa-definitions.l4` alone, the state of the folder before the coa23 files; the keel's own tests file is not in this folder):

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.109 (main, 4c887e0, 2026-11-04)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
coa-core.l4                                    0         0       0        0         0 |      0         0       0        0  same
coa-definitions.l4                             0         0       0        0         0 |      0         0       0        0  same
TOTAL (2 modules)                              0         0       0        0           |      0         0       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

After: 13 modules, 1142 assertions satisfied, 0 errors, 0 failed, 0 refused, on both builds. The two source-locator gates:

```
python3 -I srcrefs.py check --refs ukpga-2006-46.txt coa23-*.l4  ->  srcrefs check: 520 src: lines, 174 runs, 210 locators, 0 problems
python3 -I srcrefs.py check --strict ukpga-2006-46.txt coa23-*.l4  ->  srcrefs check: 520 src: lines, 174 runs, 210 locators, 0 problems
```

Traces (`-- EXPECT:` lines against the binary's output, both builds): l4-main-110: traces: 34, as expected: 34; l4-main-109: traces: 34, as expected: 34. The count of assertions by file: part 34 133, registrar 316, delivery 240, register 288, seat cases 165 (total 1142 counted from the tool).

## How the tests were written

Every expected value is typed in the test generators from the text of the section named beside the assertion, before the module was run; none is copied from the code's output. Each branch of each function has an assertion, both sides of every period's end and of every threshold are asserted (three years, two years, twenty years, fourteen days, fifteen days with the working-day roll-over, the fee equal to the cost), and each function has a case outside the encoding asserted as NOTHING where it has one. The 34 heads of s 1078 and the 39 items of s 1087(1) are asserted one by one: the expected answer follows the lead-in of the head's own list ((2) every company, (3) a public company, (3A), (4), (4A), (4B), (5); every item of s 1087(1) true when the material forms part of the register). A failing assertion would be a finding. What happened during the work, stated as it was: (1) one assertion of mine contradicted the text (I had written s 1106 as outside the s 1059A lists, and list 3.9 names it); it was removed, not made to pass; (2) two assertions for s 1074(2) failed and exposed a defect in the code (`NOT a AND NOT b` reads as `NOT (a AND NOT b)`), which was fixed with brackets in the code, and a regression assertion was added for s 1073(5), which had the same defect and had not failed; (3) three functions (s 1046(2), s 1066(3), s 1067(3)) were changed from NOTHING to JUST FALSE when the 2026-11-05 rulings on a failed "if" and "on" were re-read, and their expected values were rewritten from the rulings before the rerun. (4) on 2026-11-13 s 1092B(1) was changed from JUST FALSE to NOTHING for a person with a reasonable excuse, decided case by case (fork F26), and five seat questions were renamed at the lead's request (fork F27); the two assertions that changed value carry `-- RECONCILED 2026-11-12` beside them. No expected value was edited to match an output. No independent test pass (the encoding-a-subject skill's step 8) was run: this part has one agent and no subagents.

## Open questions for a domain expert

1. Is it right to treat the mandatory limits on regulations (ss 1046(2), 1047(1), 1051(2)(a), 1054(3), 1055, 1056, 1058(2), 1088(7), (8)) as encodable rules and the plain powers as machinery (fork F1)?
2. Which wording of s 1054(3)(b) is in force, and is "not exceeding" a limit on the daily fine or on the offence (fork F2)?
3. Does a met "unless" or "except" (the document bars of ss 1067A, 1067B, 1076; the reliance bar of s 1079; the disclosure bar of s 1087C; s 1092) make the bar's answer a no, or leave it open (fork F9)?
4. Should a bare "must" not done be a no in a compliance function (fork F5)?
5. Do the four rows of s 1067A(2) for a firm combine as alternatives (fork F10)?
6. Are two, three and twenty years counted as the code counts them, with the leap-day roll-forward (fork F12)?
7. Is "the general limit in a magistrates' court" (s 1092B(3)) a number a caller supplies, or should the encoding carry the current figure of its own source?
8. Does the website form show a `MAYBE` answer and a question with no inputs as a person expects (not tried here)?

## Files

`coa-core.l4`, `coa-definitions.l4` (the keel's, read-only, not edited); layer 1: `coa23-nouns.l4`, `coa23-part34.l4`, `coa23-part35-registrar.l4`, `coa23-part35-delivery.l4`, `coa23-part35-register.l4`; tests: `coa23-tests-part34.l4`, `coa23-tests-part35-registrar.l4`, `coa23-tests-part35-delivery.l4`, `coa23-tests-part35-register.l4`; seat: `coa23-seat.l4`, `coa23-cases-seat.l4`; `NOTES.md`, `PROGRESS.md`, `NEEDS-CORE.md`; `check.sh`, `srcrefs.py`, `fetch-main-l4.sh` (supplied). The generators (`work/`, not shipped) read the text and the test tables and write the `.l4` files.

## Copied modules

None.

## Peeked

Nothing: no existing encoding of any Act, no file under `<local path>`, `<local worktrees>` or `canon`, no other directory under the runs directory, and nothing under `<local tool>` was opened by the encoder for this part.

