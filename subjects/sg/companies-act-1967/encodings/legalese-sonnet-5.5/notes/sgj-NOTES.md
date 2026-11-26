# NOTES (sgj): Companies Act 1967 (Singapore), Part 4 Divisions 4 to 7A and Part 5 Division 1

This is the part of the encoding written by agent `sgj`.
It covers the text of `CoA1967.txt` lines 9882 to 11038 and 11493 to 11591: substantial shareholdings (ss 79 to 92), debentures (ss 93 to 106, of which ss 97 to 99 and 101 to 106 are repealed, and Divisions 5A and 6 repealed whole), title and transfers (ss 121 to 130AE, with s 128A and Division 7A repealed) and Part 5 Division 1 (ss 142 to 144).
**The L4 here is a rendering of the text, not the official text.**
Every rule quotes the lines it renders with `-- src:` lines and an `@ref` locator, so that a reader can check the wording against the file the encoding was made from; the official text is the Singapore Statutes Online version of the Act, and a lawyer must check any answer against it.
Nothing in this folder is legal advice, and no answer here has been confirmed by a lawyer.

How each claim in this file was checked is stated where it is made.
The numbers in "What check.sh prints" are the output of the last full run, described there.
Anything marked "assumed, not ruled" is a choice made by this part and recorded so that a reviewer can overrule it.

## Edition encoded

The Companies Act 1967, 2020 Revised Edition, as the Singapore Statutes Online informal consolidation in force from 6 May 2026 to 20 October 2026, which carries amendments up to Act 24 of 2025.
Source file: `CoA1967.txt`, sha256 `ea9501a3e0829a46b396aa6cb5e7369fc8c1f4c2288ede5748cf3e62c6284303` (checked with `shasum -a 256` on 2026-11-18; `inputs/SOURCES.md` records the same hash).
Ranges: lines 9882 to 11038 (Part 4 Divisions 4 to 7A) and 11493 to 11591 (Part 5 Division 1).
Amendment marks such as `[36/2014]` and `[Act 24 of 2025 wef 06/05/2026]` are not text and are not rules.
Page furniture ("Informal Consolidation - version in force ...", "2020 Ed. Companies Act 1967 NNN") is not text.
Target compiler: the stable `l4` 1.6.110 (main, e51181d, 2026-11-11), also run on 1.6.109 (main, 4c887e0, 2026-11-04); `JL4_LIBRARY_PATH` unset.

**PLAN.md and the brief.**
`inputs/PLAN.md` was written before the brief for this part, and the two differ in places; the brief governs.
The differences that mattered here:
(1) PLAN.md section 4 table A lists the s 93 seam as giving the "principal register".
The keel's `s 4(1) "branch register"` (sg-definitions.l4, source line 1235) asks for "a branch register of holders of debentures kept pursuant to section 93", and that is what this part answers, with `s 93(8) the register is a branch register of holders of debentures kept pursuant to section 93` (see Seams).
(2) PLAN.md section 7 gives shared input names with exact `@desc` wording; the seat uses those two (`the company is a private company`, `the company is a public company`) as given, and the brief's naming rule ("Under section N, ...") for every question.
(3) The brief's coverage rules (one row per section, subsection, paragraph, sub-paragraph, heading and defined term, exactly one disposition, every non-blank line in a row) are stricter than PLAN.md's row for this part, and are the ones followed.

## The files

| file | what it holds |
| --- | --- |
| `sgj-part5-office-name.l4`, `sgj-tests-part5-office-name.l4` | Part 5 Division 1: the registered office, the notice of its hours and changes, the display of the name (ss 142 to 144) |
| `sgj-div4-substantial-shareholdings.l4`, `sgj-tests-div4-substantial-shareholdings.l4` | Part 4 Division 4 (ss 79 to 91; s 92 repealed) |
| `sgj-div5-debentures.l4`, `sgj-tests-div5-debentures.l4` | Part 4 Division 5 (ss 93 to 96, 100; ss 97 to 99 and 101 to 106 repealed) and the repealed Divisions 5A and 6 |
| `sgj-div7-title.l4`, `sgj-tests-div7-title.l4` | Part 4 Division 7, shares and certificates (ss 121 to 125) |
| `sgj-div7-private-transfers.l4`, `sgj-tests-div7-private-transfers.l4` | Part 4 Division 7, private companies (ss 126 to 129; s 128A repealed) |
| `sgj-div7-public-transfers.l4`, `sgj-tests-div7-public-transfers.l4` | Part 4 Division 7, public companies and certificates (ss 130 to 130AE) and the repealed Division 7A |
| `sgj-seat.l4`, `sgj-cases-seat.l4` | the seat layer: 59 questions, each `Under section N, ...`, with `@export` and `@desc`, and 150 cases |
| `NOTES.md`, `PROGRESS.md` | this file; the progress log |

The scripts named `work/...` in this file (the coverage table builder, the tag counter, the trace checker, the mutation runner) are scratch tools of the run, kept outside this folder and not delivered; their output is reproduced here where it is cited.
Layer 1 follows the text's own structure: one function per subsection or paragraph that states a rule, named with the provision's label (`s 82(2) the last day for giving the notice`).
Layer 2 (the seat) calls layer 1 and states no rule of its own.
Every period is counted by the keel's `sg-periods.l4`; this part does no date arithmetic of its own.

**The seat** is the individual the layer asks for: a director, a company secretary or a member of a company under the Act, or someone who deals with one.
The Registrar, the Minister and the Court have no seat; what they decide appears only as what it means for that individual (for example `Under section 87, can the Registrar extend the time for my notice`).

## Coverage (sgj)

The table is built by script (`work/coverage.py`) from the text itself: it reads lines 9882 to 11038 and 11493 to 11591 of `CoA1967.txt`, finds every Part and Division heading, marginal heading, section, subsection, paragraph, sub-paragraph and repealed row by its label, and adds a row for each defined term.
Each row has exactly one disposition: `encoded` (a rule, definition or table in layer 1, with a test and an `@ref`), `fork` (the text can be read two or more ways; the row names the fork-register entry, and the L4 name is the rule that carries the reading taken), `inert` (only for reason 1, 2 or 3 of the brief) or `repealed or blank in this text`.
There is no `out-of-scope` or `deferred` row.
A section or subsection that contains a fork row takes the disposition `fork` itself, with the fork ids of the rows inside it.
A paragraph with no function of its own is read inside the rule of its subsection, and says so ("inside the rule of ...").
Page furniture and amendment marks are not rows; they lie inside the row they sit in.

**Counts.**
Rows by kind: heading 43, paragraph 68, repealed 12, section 36, sub-paragraph 2, subsection 114, term 8; total rows 283.
Rows by disposition: encoded 112, fork 115, inert (reason 1) 43, repealed or blank in this text 13.
Every `inert` row is a heading (reason 1: a heading creates no rule); no row is inert for reason 2 or 3 (machinery in this range, such as the Minister's power to exempt in s 80(3) and the Registrar's power in s 87, creates a relation for the individual and is encoded).


**Audit.**
The script checks four things on every run and printed the results above and below:
(1) every non-blank line of the two ranges lies in a row (lines in no row: 0);
(2) each non-blank line is owned by exactly one row, where a row's own lines are its lines minus those of the rows inside it, so that the rows partition the text (lines not owned by exactly one row (own lines = a row's lines minus its children's): 0);
(3) every encoded or fork row has a layer-1 name of its own or of an ancestor, a locator (`@ref`) that overlaps its lines, and a name that appears in a test or case file;
(4) the number of unit labels found by script agrees with an independent count that does no parsing (a regular expression over every line): Part and Division heading lines 9, lettered label lines 70, repealed range lines 4, roman label lines 2, section start lines 41, subsection label lines 114.
Rows in the table: the first pass of the script produced 276 rows; it missed three repealed ranges that sat on the line after a Division heading (106A to 106L, 107 to 120, 130A to 130P), took two roman sub-paragraphs of s 130AD(5)(b) for lettered paragraphs, and missed the three lettered paragraphs of s 85; after those were fixed the table has 283 rows.

| unit | text lines | the text begins | disposition | L4 names (layer 1) | fork or note |
| --- | --- | --- | --- | --- | --- |
| Division 4 | 9882-10294 | Division 4 — Substantial shareholdings | inert, reason 1 (heading, no rule) |  |  |
| heading before s 79 | 9884-9884 | Application and interpretation of Division | inert, reason 1 (heading, no rule) |  |  |
| s 79 | 9886-9915 | (1) This section has effect for the purposes of this Division but d... | fork |  | F-j79-1 (by the rows inside it) |
| s 79(1) | 9886-9887 | This section has effect for the purposes of this Division but does ... | encoded | `s 79(1) section 79 has effect for the provision` |  |
| s 79(2) | 9889-9903 | A reference to a company is a reference — | fork | `s 79(2) the body is a company for the purposes of this Division` | F-j79-1 the Minister's declarations: a body declared by neither (b) nor (c) is not covered |
| term "company" (s 79(2)) | 9889-9901 | A reference to a company is a reference to a body declared by the M... | fork | `s 79(2) the body is a company for the purposes of this Division` | F-j79-1 the Minister's declarations: a body declared by neither (b) nor (c) is not covered |
| s 79(2)(a) | 9891-9891 | [Deleted by Act 2 of 2009] | repealed or blank in this text: [Deleted by Act 2 of 2009] | `s 79(2) the body is a company for the purposes of this Division` (inside the rule of s 79(2)) | F-j79-1 the Minister's declarations: a body declared by neither (b) nor (c) is not covered |
| s 79(2)(b) | 9893-9896 | to a body corporate, being a body incorporated in Singapore, that i... | fork | `s 79(2) the body is a company for the purposes of this Division` (inside the rule of s 79(2)) | F-j79-1 the Minister's declarations: a body declared by neither (b) nor (c) is not covered |
| s 79(2)(c) | 9898-9903 | to a body, not being a body corporate formed in Singapore, that is ... | fork | `s 79(2) the body is a company for the purposes of this Division` (inside the rule of s 79(2)) | F-j79-1 the Minister's declarations: a body declared by neither (b) nor (c) is not covered |
| s 79(3) | 9905-9908 | In relation to a company the whole or a portion of the share capita... | encoded | `s 79(3) the interest in the stock is deemed to be an interest in an issued share in the company` |  |
| term "stock" (s 79(3)) | 9905-9908 | an interest in stock is deemed to be an interest in an issued share | encoded | `s 79(3) the interest in the stock is deemed to be an interest in an issued share in the company` |  |
| s 79(4) | 9910-9915 | A reference in the definition of “voting share” in section 4(1) to ... | encoded | `s 79(4) the body is within a reference to a body corporate in the definition of "voting share"` |  |
| heading before s 80 | 9917-9917 | Persons obliged to comply with Division | inert, reason 1 (heading, no rule) |  |  |
| s 80 | 9919-9929 | (1) The obligation to comply with this Division extends to all natu... | encoded |  |  |
| s 80(1) | 9919-9922 | The obligation to comply with this Division extends to all natural ... | encoded | `s 80(1) the obligation to comply with this Division extends to the person` |  |
| s 80(2) | 9924-9925 | This Division extends to acts done or omitted to be done outside Si... | encoded | `s 80(2) this Division extends to the act or omission` |  |
| s 80(3) | 9927-9929 | The Minister may, by order in the Gazette, exempt any person or any... | encoded | `s 80(3) the person is exempt from the provision of this Division` |  |
| term "substantial shareholding" (s 81(1)) | 9930-9945 | a person has a substantial shareholding in a company if | encoded | `s 81(1) the person has a substantial shareholding in the company` |  |
| heading before s 81 | 9931-9931 | Substantial shareholdings and substantial shareholders | inert, reason 1 (heading, no rule) |  |  |
| s 81 | 9933-9962 | (1) For the purposes of this Division, a person has a substantial s... | fork |  | F-j81-1 (by the rows inside it) |
| s 81(1) | 9933-9941 | For the purposes of this Division, a person has a substantial share... | encoded | `s 81(1) the person has a substantial shareholding in the company` |  |
| s 81(1)(a) | 9936-9937 | the person has an interest or interests in one or more voting share... | encoded | `s 81(1)(a) the person has an interest or interests in one or more voting shares in the company` |  |
| s 81(1)(b) | 9939-9941 | the total votes attached to that share, or those shares, is not les... | encoded | `s 81(1)(b) the votes are not less than 5% of the total votes attached to all the voting shares in the company` |  |
| s 81(2) | 9943-9952 | For the purposes of this Division, a person has a substantial share... | encoded | `s 81(2) the person has a substantial shareholding in the company, the share capital of which is divided into 2 or more classes` |  |
| s 81(2)(a) | 9947-9948 | the person has an interest or interests in one or more voting share... | encoded | `s 81(2) the person has a substantial shareholding in the company, the share capital of which is divided into 2 or more classes` (inside the rule of s 81(2)) |  |
| s 81(2)(b) | 9950-9952 | the total votes attached to that share, or those shares, is not les... | encoded | `s 81(2) the person has a substantial shareholding in the company, the share capital of which is divided into 2 or more classes` (inside the rule of s 81(2)) |  |
| s 81(3) | 9954-9956 | For the purposes of this Division, a person who has a substantial s... | fork | `s 81(3) the person is a substantial shareholder in the company` | F-j81-1 one direction only: not covered where neither (1) nor (2) holds |
| s 81(4) | 9958-9962 | In this section and section 83, “voting shares” exclude treasury sh... | encoded | `s 81(4) the share is a voting share for the purposes of section 81 and section 83` |  |
| term "voting shares" (s 81(4)) | 9958-9959 | In this section and section 83, "voting shares" exclude treasury sh... | encoded | `s 81(4) the share is a voting share for the purposes of section 81 and section 83` |  |
| heading before s 82 | 9964-9964 | Substantial shareholder to notify company of interests | inert, reason 1 (heading, no rule) |  |  |
| s 82 | 9966-9986 | (1) A person who is a substantial shareholder in a company must giv... | encoded |  |  |
| s 82(1) | 9966-9973 | A person who is a substantial shareholder in a company must give wr... | encoded | `s 82(1) the notice is the notice the subsection requires`; `s 82(1) a substantial shareholder must give notice to the company within 2 business days` |  |
| s 82(2) | 9975-9982 | The notice must be given — | encoded | `s 82(2) the last day for giving the notice`; `s 82(2) the notice was given within the time the subsection allows` |  |
| s 82(2)(a) | 9977-9978 | if the person was a substantial shareholder on 1 October 1971 — wit... | encoded | `s 82(2) the last day for giving the notice`; `s 82(2) the notice was given within the time the subsection allows` (inside the rule of s 82(2)) |  |
| s 82(2)(b) | 9980-9982 | if the person became a substantial shareholder after that date — wi... | encoded | `s 82(2) the last day for giving the notice`; `s 82(2) the notice was given within the time the subsection allows` (inside the rule of s 82(2)) |  |
| s 82(3) | 9984-9986 | The notice must be so given even though the person has ceased to be... | encoded | `s 82(3) the notice must be given although the person has ceased to be a substantial shareholder` |  |
| heading before s 83 | 9988-9989 | Substantial shareholder to notify company of change in interests | inert, reason 1 (heading, no rule) |  |  |
| s 83 | 9991-10025 | (1) Where there is a change in the percentage level of the interest... | fork |  | F-j83-1 (by the rows inside it) |
| s 83(1) | 9991-9996 | Where there is a change in the percentage level of the interest or ... | fork | `s 83(1) the substantial shareholder must give notice of a change in the percentage level`; `s 83(1) the last day for giving the notice` (+2 more) | F-j83-1 a duty whose "where" is unmet: JUST FALSE |
| s 83(2) | 9998-10005 | The information referred to in subsection (1) is — | encoded | `s 83(2) the notice states the information the subsection specifies` |  |
| s 83(2)(a) | 10000-10000 | the name and address of the substantial shareholder; | encoded | `s 83(2) the notice states the information the subsection specifies` (inside the rule of s 83(2)) |  |
| s 83(2)(b) | 10002-10003 | the date of the change and the circumstances leading to that change... | encoded | `s 83(2) the notice states the information the subsection specifies` (inside the rule of s 83(2)) |  |
| s 83(2)(c) | 10005-10005 | such other particulars as may be prescribed. | encoded | `s 83(2) the notice states the information the subsection specifies` (inside the rule of s 83(2)) |  |
| s 83(3) | 10007-10025 | In subsection (1), “percentage level”, in relation to a substantial... | encoded | `s 83(3) the percentage level` |  |
| term "percentage level" (s 83(3)) | 10007-10011 | In subsection (1), "percentage level", in relation to a substantial... | encoded | `s 83(3) the percentage level` |  |
| s 83(3)(a) | 10018-10018 | all the voting shares in the company; or | encoded | `s 83(3) the percentage level` (inside the rule of s 83(3)) |  |
| s 83(3)(b) | 10020-10025 | where the share capital of the company is divided into 2 or more cl... | encoded | `s 83(3) the percentage level` (inside the rule of s 83(3)) |  |
| heading before s 84 | 10027-10028 | Person who ceases to be substantial shareholder to notify company | inert, reason 1 (heading, no rule) |  |  |
| s 84 | 10030-10037 | (1) A person who ceases to be a substantial shareholder in a compan... | encoded | `s 84 a person who ceases to be a substantial shareholder must give notice within 2 business days` |  |
| s 84(1) | 10030-10034 | A person who ceases to be a substantial shareholder in a company mu... | encoded | `s 84(1) the notice is the notice the subsection requires` |  |
| s 84(2) | 10036-10037 | The notice must be given within 2 business days after the person ce... | encoded | `s 84(2) the last day for giving the notice`; `s 84(2) the notice was given within 2 business days after the person ceased to be a substantial shareholder` |  |
| heading before s 85 | 10039-10039 | References to operation of section 7 | inert, reason 1 (heading, no rule) |  |  |
| s 85 | 10041-10052 | The circumstances required to be stated in the notice under section... | encoded | `s 85 the circumstance is one the notice must state` |  |
| s 85(a) | 10045-10045 | a person has an interest in voting shares; | encoded | `s 85 the circumstance is one the notice must state` (inside the rule of s 85) |  |
| s 85(b) | 10047-10047 | a change has occurred in an interest in voting shares; or | encoded | `s 85 the circumstance is one the notice must state` (inside the rule of s 85) |  |
| s 85(c) | 10049-10052 | a person has ceased to be a substantial shareholder in a company, | encoded | `s 85 the circumstance is one the notice must state` (inside the rule of s 85) |  |
| heading before s 86 | 10054-10054 | Persons holding shares as trustees | inert, reason 1 (heading, no rule) |  |  |
| s 86 | 10056-10083 | (1) A person who holds voting shares in a company, being voting sha... | encoded |  |  |
| s 86(1) | 10056-10063 | A person who holds voting shares in a company, being voting shares ... | encoded | `s 86(1) the holder must give the non-resident a notice`; `s 86(1) the notice is the notice the subsection requires` (+1 more) |  |
| s 86(2) | 10065-10072 | The notice must be given — | encoded | `s 86(2) the last day for giving the notice`; `s 86(2) the notice was given within the time the subsection allows` |  |
| s 86(2)(a) | 10067-10068 | if the firstmentioned person holds the shares on 1 October 1971 — w... | encoded | `s 86(2) the last day for giving the notice`; `s 86(2) the notice was given within the time the subsection allows` (inside the rule of s 86(2)) |  |
| s 86(2)(b) | 10070-10072 | if the firstmentioned person did not hold the shares on that date —... | encoded | `s 86(2) the last day for giving the notice`; `s 86(2) the notice was given within the time the subsection allows` (inside the rule of s 86(2)) |  |
| s 86(2A) | 10074-10077 | This section does not apply to the Depository as the registered hol... | encoded | `s 86(2A) section 86 applies to the person` |  |
| s 86(3) | 10079-10081 | In this section, “non‑resident” means a person who is not resident ... | encoded | `s 86(3) "non-resident" the person is a non-resident` |  |
| term "non-resident" (s 86(3)) | 10079-10082 | In this section, "non-resident" means a person who is not resident ... | encoded | `s 86(3) "non-resident" the person is a non-resident` |  |
| s 86(4) | 10083-10083 | Nothing in this section affects the operation of section 80. | encoded | `s 86(4) section 86 affects the operation of section 80` |  |
| heading before s 87 | 10085-10085 | Registrar may extend time for giving notice under this Division | inert, reason 1 (heading, no rule) |  |  |
| s 87 | 10087-10089 | The Registrar may, on the application of a person who is required t... | fork | `s 87 the Registrar has power to extend the time for giving the notice`; `s 87 the notice was given within the time as extended` | F-j87-1 a power gated by an application: NOTHING (split site (ii)) |
| heading before s 88 | 10091-10091 | Company to keep register of substantial shareholders | inert, reason 1 (heading, no rule) |  |  |
| s 88 | 10093-10140 | (1) A company must keep a register in which it must immediately ent... | fork |  | F-j88-1 F-j88-2 (by the rows inside it) |
| s 88(1) | 10093-10101 | A company must keep a register in which it must immediately enter — | fork | `s 88(1) the company has kept the register as the subsection requires`; `s 88(1) the company must immediately enter the notice in the register` | F-j88-1 "immediately" read as a deadline of 0 days after receipt |
| s 88(1)(a) | 10096-10097 | in alphabetical order the names of persons from whom it has receive... | fork | `s 88(1) the company has kept the register as the subsection requires`; `s 88(1) the company must immediately enter the notice in the register` (inside the rule of s 88(1)) | F-j88-1 "immediately" read as a deadline of 0 days after receipt |
| s 88(1)(b) | 10099-10101 | against each name so entered, the information given in the notice a... | fork | `s 88(1) the company has kept the register as the subsection requires`; `s 88(1) the company must immediately enter the notice in the register` (inside the rule of s 88(1)) | F-j88-1 "immediately" read as a deadline of 0 days after receipt |
| s 88(2) | 10103-10112 | The register must be kept at the registered office of the company, ... | encoded | `s 88(2) the register is kept at the place the subsection requires`; `s 88(2) the most the company may require the person to pay for each inspection` |  |
| s 88(3) | 10114-10120 | A person may request the company to furnish the person with a copy ... | encoded | `s 88(3) the most the company may require to be paid in advance for the copy`; `s 88(3) the last day for the company to send the copy` (+2 more) |  |
| s 88(4) | 10122-10125 | The Registrar may at any time in writing require the company to fur... | encoded | `s 88(4) the last day for the company to furnish the copy to the Registrar`; `s 88(4) the company furnished the copy within 7 days after the day the requirement was received` (+1 more) |  |
| s 88(5) | 10127-10131 | If default is made in complying with this section, the company and ... | fork | `s 88(5) the person is guilty of the offence this subsection creates`; `s 88(5) the most the person may be sentenced to on conviction` (+1 more) | F-j88-2 offence, an element unmet: JUST FALSE (split site (i)) |
| s 88(6) | 10133-10140 | A company is not, by reason of anything done under this Division — | encoded |  |  |
| s 88(6)(a) | 10136-10136 | to be taken for any purpose to have notice of; or | encoded | `s 88(6)(a) the company is to be taken to have notice of a right of a person to or in relation to a share` |  |
| s 88(6)(b) | 10138-10140 | to be put upon inquiry as to, | encoded | `s 88(6)(b) the company is to be put upon inquiry as to a right of a person to or in relation to a share` |  |
| heading before s 89 | 10142-10142 | Offences against certain sections | inert, reason 1 (heading, no rule) |  |  |
| s 89 | 10144-10148 | A person who fails to comply with section 82, 83, 84 or 86 shall be... | fork | `s 89 the person is guilty of the offence this section creates`; `s 89 the most the person may be sentenced to on conviction` (+1 more) | F-j89-1 offence, the element unmet: JUST FALSE (split site (i)) |
| heading before s 90 | 10150-10150 | Defence to prosecutions | inert, reason 1 (heading, no rule) |  |  |
| s 90 | 10152-10182 | (1) It is a defence to a prosecution for failing to comply with sec... | encoded |  |  |
| s 90(1) | 10152-10166 | It is a defence to a prosecution for failing to comply with section... | encoded | `s 90(1) this section gives a defence on these facts` |  |
| s 90(1)(a) | 10162-10163 | the defendant was not so aware on the date of the summons; or | encoded | `s 90(1) this section gives a defence on these facts` (inside the rule of s 90(1)) |  |
| s 90(1)(b) | 10165-10166 | the defendant became so aware less than 7 days before the date of t... | encoded | `s 90(1) this section gives a defence on these facts` (inside the rule of s 90(1)) |  |
| s 90(2) | 10168-10182 | For the purposes of subsection (1), a person is conclusively presum... | encoded | `s 90(2) the person is conclusively presumed to have been aware of the fact or occurrence at that time` |  |
| s 90(2)(a) | 10172-10174 | of which the person would, if the person had acted with reasonable ... | encoded | `s 90(2) the person is conclusively presumed to have been aware of the fact or occurrence at that time` (inside the rule of s 90(2)) |  |
| s 90(2)(b) | 10176-10182 | of which an employee or agent of the person, being an employee or a... | encoded | `s 90(2) the person is conclusively presumed to have been aware of the fact or occurrence at that time` (inside the rule of s 90(2)) |  |
| heading before s 91 | 10184-10185 | Powers of Court with respect to defaulting substantial shareholders | inert, reason 1 (heading, no rule) |  |  |
| s 91 | 10187-10289 | (1) Where a person is a substantial shareholder, or at any time aft... | fork |  | F-j91-1 F-j91-2 F-j91-4 F-j91-3 (by the rows inside it) |
| s 91(1) | 10187-10229 | Where a person is a substantial shareholder, or at any time after 1... | fork | `s 91(1) the Court may make the order on the Minister's application` | F-j91-1 a "may" gated by "where": JUST FALSE (split site (ii)) |
| s 91(1)(a) | 10193-10195 | an order restraining the person from disposing of any interest in s... | fork | `s 91(1) the Court may make the order on the Minister's application` (inside the rule of s 91(1)) | F-j91-1 a "may" gated by "where": JUST FALSE (split site (ii)) |
| s 91(1)(b) | 10197-10203 | an order restraining a person who is, or is entitled to be register... | fork | `s 91(1) the Court may make the order on the Minister's application` (inside the rule of s 91(1)) | F-j91-1 a "may" gated by "where": JUST FALSE (split site (ii)) |
| s 91(1)(c) | 10205-10207 | an order restraining the exercise of any voting or other rights att... | fork | `s 91(1) the Court may make the order on the Minister's application` (inside the rule of s 91(1)) | F-j91-1 a "may" gated by "where": JUST FALSE (split site (ii)) |
| s 91(1)(d) | 10209-10212 | an order directing the company not to make payment, or to defer mak... | fork | `s 91(1) the Court may make the order on the Minister's application` (inside the rule of s 91(1)) | F-j91-1 a "may" gated by "where": JUST FALSE (split site (ii)) |
| s 91(1)(e) | 10214-10216 | an order directing the sale of all or any of the shares in the comp... | fork | `s 91(1) the Court may make the order on the Minister's application` (inside the rule of s 91(1)) | F-j91-1 a "may" gated by "where": JUST FALSE (split site (ii)) |
| s 91(1)(f) | 10218-10219 | an order directing the company not to register the transfer or tran... | fork | `s 91(1) the Court may make the order on the Minister's application` (inside the rule of s 91(1)) | F-j91-1 a "may" gated by "where": JUST FALSE (split site (ii)) |
| s 91(1)(g) | 10221-10224 | an order that any exercise of the voting or other rights attached t... | fork | `s 91(1) the Court may make the order on the Minister's application` (inside the rule of s 91(1)) | F-j91-1 a "may" gated by "where": JUST FALSE (split site (ii)) |
| s 91(1)(h) | 10226-10229 | for the purposes of securing compliance with any other order made u... | fork | `s 91(1) the Court may make the order on the Minister's application` (inside the rule of s 91(1)) | F-j91-1 a "may" gated by "where": JUST FALSE (split site (ii)) |
| s 91(2) | 10231-10232 | Any order made under this section may include such ancillary or con... | fork | `s 91(2) the order may include the provision` | F-j91-2 a grant gated by "if": NOTHING |
| s 91(3) | 10234-10239 | An order made under this section directing the sale of a share may ... | fork | `s 91(3) the sale order may provide the time and conditions of the sale` | F-j91-2 a grant gated by "if": NOTHING |
| s 91(4) | 10241-10243 | The Court may direct that, where a share is not sold in accordance ... | fork | `s 91(4) the Court may direct that the share vests in the Registrar` | F-j91-1 a "may" gated by "where": JUST FALSE (split site (ii)) |
| s 91(5) | 10245-10252 | The Court must, before making an order under this section and in de... | encoded | `s 91(5) the Court must satisfy itself that the order would not unfairly prejudice any person`; `s 91(5) the Court must satisfy itself before making an order` |  |
| s 91(6) | 10254-10264 | The Court must not make an order under this section, other than an ... | fork | `s 91(6) the Court is barred from making the order`; `s 91(6) the Court must not make an order when it is satisfied that the failure ought to be excused` | F-j91-4 a prohibition limited by its own wording, with a carve-out "(other than X)" |
| s 91(6)(a) | 10257-10261 | that the failure of the substantial shareholder to comply as mentio... | fork | `s 91(6) the Court is barred from making the order`; `s 91(6) the Court must not make an order when it is satisfied that the failure ought to be excused` (inside the rule of s 91(6)) | F-j91-4 a prohibition limited by its own wording, with a carve-out "(other than X)" |
| s 91(6)(b) | 10263-10264 | that in all the circumstances, the failure ought to be excused. | fork | `s 91(6) the Court is barred from making the order`; `s 91(6) the Court must not make an order when it is satisfied that the failure ought to be excused` (inside the rule of s 91(6)) | F-j91-4 a prohibition limited by its own wording, with a carve-out "(other than X)" |
| s 91(7) | 10266-10269 | The Court may, before making an order under this section, direct th... | fork | `s 91(7) the Court may direct that notice of the application be given or published` | F-j91-2 a grant gated by "before": NOTHING |
| s 91(8) | 10271-10272 | The Court may rescind, vary or discharge an order made by it under ... | fork | `s 91(8) the Court may rescind, vary, discharge or suspend the operation of the order` | F-j91-2 a grant gated by "if": NOTHING |
| s 91(9) | 10274-10279 | Section 214 of the Insolvency, Restructuring and Dissolution Act 20... | encoded | `s 91(9) section 214 of the Insolvency, Restructuring and Dissolution Act 2018 applies to the share` |  |
| s 91(10) | 10281-10286 | Any person who contravenes or fails to comply with an order made un... | fork | `s 91(10) the person is guilty of the offence this subsection creates`; `s 91(10) the most the person may be sentenced to on conviction` (+1 more) | F-j91-3 offence, the element unmet: JUST FALSE (split site (i)) |
| s 91(11) | 10288-10289 | Subsection (10) does not affect the powers of the Court in relation... | encoded | `s 91(11) subsection (10) affects the powers of the Court in relation to the punishment of contempt of the Court` |  |
| s 92 | 10291-10294 | [Repealed by Act 2 of 2009] | repealed or blank in this text: [Repealed by Act 2 of 2009] |  |  |
| Division 5 | 10296-10464 | Division 5 — Debentures | inert, reason 1 (heading, no rule) |  |  |
| heading before s 93 | 10298-10298 | Register of debenture holders and copies of trust deed | inert, reason 1 (heading, no rule) |  |  |
| s 93 | 10300-10362 | (1) Every company which issues debentures (not being debentures tra... | fork |  | F-j93-1 F-j93-4 F-j93-3 F-j93-5 (by the rows inside it) |
| s 93(1) | 10300-10303 | Every company which issues debentures (not being debentures transfe... | encoded | `s 93(1) the company has kept the register as the subsection requires`; `s 93(1) the company must keep a register of holders of the debentures` |  |
| s 93(2) | 10305-10309 | Every company must within 7 days after the register is first kept a... | encoded | `s 93(2) the last day for lodging notice of the place or of the change`; `s 93(2) the notice was lodged within 7 days` (+1 more) |  |
| s 93(3) | 10311-10315 | The register must except when duly closed be open to the inspection... | encoded | `s 93(3) the register must be open to the inspection of the person`; `s 93(3) the register has the content the subsection requires` (+1 more) |  |
| s 93(4) | 10317-10324 | For the purposes of this section, a register is deemed to be duly c... | fork | `s 93(4) the register is deemed to be duly closed` | F-j93-1 a deeming "if" gives a sufficient condition only |
| s 93(5) | 10326-10333 | Every registered holder of debentures and every holder of shares in... | fork | `s 93(5) the company must supply the person with a copy of the register`; `s 93(5) the most the company may require to be paid for the copy of the register` (+1 more) | F-j93-4 a duty limited by the request and the payment: NOTHING |
| s 93(6) | 10335-10344 | A copy of any trust deed relating to or securing any issue of deben... | fork | `s 93(6) the company must forward the copy of the trust deed to the holder`; `s 93(6) the most the company may require to be paid for the copy of the trust deed` (+1 more) | F-j93-4 a duty limited by the request and the payment: NOTHING |
| s 93(7) | 10346-10350 | If inspection is refused, or a copy is refused or not forwarded wit... | fork | `s 93(7) the copy was forwarded within the time the subsection allows`; `s 93(7) the person is guilty of the offence this subsection creates` (+1 more) | F-j93-3 offence element unmet: JUST FALSE (split site (i)); no fine stated here |
| s 93(8) | 10352-10357 | A company which issues debentures may cause to be kept in any place... | fork | `s 93(8) the company may cause a branch register of debenture holders to be kept outside Singapore`; `s 93(8) the register is a branch register of holders of debentures kept pursuant to section 93` (+2 more) | F-j93-5 a grant limited by its own wording: NOTHING; the "principal register" seam |
| s 93(9) | 10359-10362 | If a company fails to comply with this section, the company and eve... | fork | `s 93(9) the person is guilty of the offence this subsection creates`; `s 93(9) the most the person may be sentenced to on conviction` | F-j93-3 offence element unmet: JUST FALSE (split site (i)) |
| heading before s 94 | 10364-10364 | Specific performance of contracts | inert, reason 1 (heading, no rule) |  |  |
| s 94 | 10366-10368 | A contract with a company to take up and pay for any debentures of ... | fork | `s 94 the contract may be enforced by an order for specific performance` | F-j94-1 a grant limited by the kind of contract: NOTHING |
| heading before s 95 | 10370-10370 | Perpetual debentures | inert, reason 1 (heading, no rule) |  |  |
| s 95 | 10372-10377 | A condition in any debenture or in any deed for securing any debent... | encoded | `s 95 the condition is invalid by reason only that it makes the debentures irredeemable or redeemable only on a contingency or after a period` |  |
| heading before s 96 | 10379-10379 | Reissue of redeemed debentures | inert, reason 1 (heading, no rule) |  |  |
| s 96 | 10381-10414 | (1) Where a company has redeemed any debentures whether before or a... | fork |  | F-j96-1 (by the rows inside it) |
| s 96(1) | 10381-10404 | Where a company has redeemed any debentures whether before or after... | encoded | `s 96(1) the company has power to reissue the redeemed debentures`; `s 96(1) the reissue is regarded as the issue of a new debenture for the purpose of a provision limiting the amount or number of debentures` |  |
| s 96(1)(a) | 10387-10389 | unless any provision to the contrary, whether express or implied, i... | encoded | `s 96(1) the company has power to reissue the redeemed debentures`; `s 96(1) the reissue is regarded as the issue of a new debenture for the purpose of a provision limiting the amount or number of debentures` (inside the rule of s 96(1)) |  |
| s 96(1)(b) | 10391-10404 | unless the company has, by passing a resolution to that effect or b... | encoded | `s 96(1) the company has power to reissue the redeemed debentures`; `s 96(1) the reissue is regarded as the issue of a new debenture for the purpose of a provision limiting the amount or number of debentures` (inside the rule of s 96(1)) |  |
| s 96(2) | 10406-10408 | After the reissue the person entitled to the debentures has and is ... | fork | `s 96(2) the person entitled to the debentures has the same priorities as if the debentures had never been redeemed` | F-j96-1 an "entitled"-named function (a claim, not a power): NOTHING outside the reissue |
| s 96(3) | 10410-10414 | Where a company has either before or after 29 December 1967 deposit... | encoded | `s 96(3) the debentures are deemed to have been redeemed by reason of the account having ceased to be in debit` |  |
| s 97 | 10416-10416 | [Repealed by S 236/2002] | repealed or blank in this text: [Repealed by S 236/2002] |  |  |
| s 98 | 10418-10418 | [Repealed by S 236/2002] | repealed or blank in this text: [Repealed by S 236/2002] |  |  |
| s 99 | 10420-10420 | [Repealed by S 236/2002] | repealed or blank in this text: [Repealed by S 236/2002] |  |  |
| heading before s 100 | 10422-10422 | Power of Court in relation to certain irredeemable debentures | inert, reason 1 (heading, no rule) |  |  |
| s 100 | 10424-10462 | (1) Despite anything in any debenture or trust deed, the security f... | fork |  | F-j100-1 (by the rows inside it) |
| s 100(1) | 10424-10454 | Despite anything in any debenture or trust deed, the security for a... | fork | `s 100(1) the Court may order that the security be enforceable` | F-j100-1 a power gated by "if" and an application: NOTHING (split site (ii)) |
| s 100(1)(a) | 10435-10439 | at the time of the issue of the debentures the assets of the corpor... | fork | `s 100(1) the Court may order that the security be enforceable` (inside the rule of s 100(1)) | F-j100-1 a power gated by "if" and an application: NOTHING (split site (ii)) |
| s 100(1)(b) | 10441-10445 | the security, if realised under the circumstances existing at the t... | fork | `s 100(1) the Court may order that the security be enforceable` (inside the rule of s 100(1)) | F-j100-1 a power gated by "if" and an application: NOTHING (split site (ii)) |
| s 100(1)(c) | 10447-10454 | the assets covered by the security, on a fair valuation on the basi... | fork | `s 100(1) the Court may order that the security be enforceable` (inside the rule of s 100(1)) | F-j100-1 a power gated by "if" and an application: NOTHING (split site (ii)) |
| s 100(2) | 10456-10459 | Subsection (1) does not affect any power to vary rights or accept a... | encoded | `s 100(2) subsection (1) affects the power` |  |
| s 100(3) | 10461-10462 | Subsection (1) does not apply in relation to any debenture that is ... | encoded | `s 100(3) subsection (1) applies to the debenture` |  |
| ss 101 to 106 | 10464-10464 | 101. to 106. [Repealed by S 236/2002] | repealed or blank in this text: 101. to 106. [Repealed by S 236/2002] |  |  |
| Division 5A | 10466-10467 | Division 5A — [Repealed by S 236/2002] | repealed or blank in this text: Division 5A — [Repealed by S 236/2002] |  |  |
| ss 106A to 106L | 10467-10467 | 106A. to 106L. [Repealed by S 236/2002] | repealed or blank in this text: 106A. to 106L. [Repealed by S 236/2002] |  |  |
| Division 6 | 10469-10473 | Division 6 — [Repealed by S 236/2002] | repealed or blank in this text: Division 6 — [Repealed by S 236/2002] |  |  |
| ss 107 to 120 | 10470-10473 | 107. to 120. [Repealed by S 236/2002] | repealed or blank in this text: 107. to 120. [Repealed by S 236/2002] |  |  |
| Division 7 | 10475-11031 | Division 7 — Title and transfers | inert, reason 1 (heading, no rule) |  |  |
| heading before s 121 | 10477-10477 | Nature of shares | inert, reason 1 (heading, no rule) |  |  |
| s 121 | 10479-10483 | The shares or other interest of any member in a company is movable ... | encoded | `s 121 the share or other interest of a member is movable property`; `s 121 the share or other interest of a member is of the nature of immovable property` (+1 more) |  |
| heading before s 122 | 10485-10485 | Numbering of shares | inert, reason 1 (heading, no rule) |  |  |
| s 122 | 10487-10504 | (1) Each share in a company must be distinguished by an appropriate... | encoded |  |  |
| s 122(1) | 10487-10488 | Each share in a company must be distinguished by an appropriate num... | encoded | `s 122(1) the share must be distinguished by an appropriate number` |  |
| s 122(2) | 10490-10504 | Despite subsection (1) — | encoded |  |  |
| s 122(2)(a) | 10492-10498 | if at any time all the issued shares in a company or all the issued... | encoded | `s 122(2)(a) the shares need no distinguishing number` |  |
| s 122(2)(b) | 10500-10504 | if all the issued shares in a company are evidenced by certificates... | encoded | `s 122(2)(b) the shares need no distinguishing number` |  |
| heading before s 123 | 10506-10506 | Certificate to be evidence of title | inert, reason 1 (heading, no rule) |  |  |
| s 123 | 10508-10537 | (1) A certificate under the common or official seal of a company sp... | fork |  | F-j123-1 F-j123-2 (by the rows inside it) |
| s 123(1) | 10508-10510 | A certificate under the common or official seal of a company specif... | encoded | `s 123(1) the certificate is prima facie evidence of the title of the member to the shares` |  |
| s 123(2) | 10512-10530 | Every share certificate must be under the common seal of the compan... | encoded | `s 123(2) the share certificate is as the subsection requires`; `s 123(2) the company must issue share certificates as the subsection requires` |  |
| s 123(2)(a) | 10517-10521 | the name of the company and the authority under which the company i... | encoded | `s 123(2) the share certificate is as the subsection requires`; `s 123(2) the company must issue share certificates as the subsection requires` (inside the rule of s 123(2)) |  |
| s 123(2)(b) | 10523-10525 | the address of the registered office of the company in Singapore, o... | encoded | `s 123(2) the share certificate is as the subsection requires`; `s 123(2) the company must issue share certificates as the subsection requires` (inside the rule of s 123(2)) |  |
| s 123(2)(c) | 10527-10530 | the class of the shares, whether the shares are fully or partly pai... | encoded | `s 123(2) the share certificate is as the subsection requires`; `s 123(2) the company must issue share certificates as the subsection requires` (inside the rule of s 123(2)) |  |
| s 123(3) | 10532-10533 | Failure to comply with this section does not affect the rights of a... | encoded | `s 123(3) the failure affects the rights of a holder of shares` |  |
| s 123(4) | 10535-10537 | If default is made in complying with this section, the company and ... | fork | `s 123(4) the person is guilty of the offence this subsection creates`; `s 123(4) the most the person may be sentenced to on conviction` | F-j123-1 F-j123-2 offence element unmet: JUST FALSE (split site (i)); no fine stated |
| heading before s 124 | 10539-10539 | Company may have duplicate common seal | inert, reason 1 (heading, no rule) |  |  |
| s 124 | 10541-10547 | A company may, if authorised by its constitution, have a duplicate ... | fork | `s 124 the company may have a duplicate common seal`; `s 124 the duplicate common seal is as the section requires` (+1 more) | F-j124-1 a grant gated by "if authorised by its constitution": NOTHING |
| heading before s 125 | 10549-10549 | Loss or destruction of certificates | inert, reason 1 (heading, no rule) |  |  |
| s 125 | 10551-10602 | (1) Subject to subsection (2), where a certificate or other documen... | fork |  | F-j125-2 F-j125-1 (by the rows inside it) |
| s 125(1) | 10551-10563 | Subject to subsection (2), where a certificate or other document of... | fork | `s 125(1) the company must issue a duplicate certificate or document to the owner`; `s 125(1) the company must issue a duplicate certificate or document` (+1 more) | F-j125-2 a duty gated by "where" and a fee: NOTHING outside |
| s 125(1)(a) | 10557-10560 | a statutory declaration that the certificate or document has been l... | fork | `s 125(1) the company must issue a duplicate certificate or document to the owner`; `s 125(1) the company must issue a duplicate certificate or document` (+1 more) (inside the rule of s 125(1)) | F-j125-2 a duty gated by "where" and a fee: NOTHING outside |
| s 125(1)(b) | 10562-10563 | an undertaking in writing that if it is found or received by the ow... | fork | `s 125(1) the company must issue a duplicate certificate or document to the owner`; `s 125(1) the company must issue a duplicate certificate or document` (+1 more) (inside the rule of s 125(1)) | F-j125-2 a duty gated by "where" and a fee: NOTHING outside |
| s 125(2) | 10565-10585 | Where the value of the shares or debentures represented by the cert... | fork | `s 125(2) the directors may require the applicant to advertise or to furnish a bond, or both` | F-j125-1 a "may" gated by "where": JUST FALSE (split site (ii)) |
| s 125(2)(a) | 10573-10578 | to cause an advertisement to be inserted in a newspaper circulating... | fork | `s 125(2)(a) the owner applies after the expiration of 14 days after the publication of the advertisement` | F-j125-1 a "may" gated by "where": JUST FALSE (split site (ii)) |
| s 125(2)(b) | 10580-10585 | to furnish a bond for an amount equal to at least the current marke... | fork | `s 125(2)(b) the bond is for an amount the paragraph allows the directors to require` | F-j125-1 a "may" gated by "where": JUST FALSE (split site (ii)) |
| s 125(3) | 10587-10590 | Any duplicate certificate issued on or after 30 January 2006 in res... | encoded | `s 125(3) the duplicate must state the amount paid and the amount unpaid in place of the historical nominal value of the shares` |  |
| s 125(4) | 10592-10596 | For the purposes of this section in relation to a book‑entry securi... | encoded | `s 125(4) the owner is the Depository` |  |
| s 125(5) | 10598-10602 | Subsection (2) does not apply to documents evidencing title in rela... | encoded | `s 125(5) subsection (2) applies to the document` |  |
| heading before s 126 | 10604-10604 | Transfer of shares in private companies | inert, reason 1 (heading, no rule) |  |  |
| s 126 | 10606-10629 | (1) Despite anything in its constitution, a private company must no... | fork |  | F-j-unless F-j126-1 (by the rows inside it) |
| s 126(1) | 10606-10613 | Despite anything in its constitution, a private company must not lo... | fork | `s 126(1) the private company is barred from lodging the transfer of shares`; `s 126(1) a private company must not lodge a transfer of shares without a proper instrument of transfer` | F-j-unless an "unless" once met: JUST FALSE |
| s 126(2) | 10615-10622 | Where there has been a transfer of shares, a private company must l... | fork | `s 126(2) the private company must lodge with the Registrar notice of the transfer of shares`; `s 126(2) a private company must lodge notice of a transfer of shares with the Registrar` | F-j126-1 a duty whose "where" is unmet: JUST FALSE |
| s 126(3) | 10624-10629 | A transfer of any share in a private company on or after 3 January ... | encoded | `s 126(3) the transfer cannot yet take effect` |  |
| heading before s 127 | 10631-10631 | Transfer of debentures in private companies | inert, reason 1 (heading, no rule) |  |  |
| s 127 | 10633-10640 | Despite anything in its constitution, a private company must not re... | fork | `s 127 the private company is barred from registering the transfer of debentures`; `s 127 a private company must not register a transfer of debentures without a proper instrument of transfer` | F-j-unless an "unless" once met: JUST FALSE |
| heading before s 128 | 10642-10643 | Registration of transfer at request of transferor by private companies | inert, reason 1 (heading, no rule) |  |  |
| s 128 | 10645-10707 | (1) Subject to section 129, on the request in writing of the transf... | fork |  | F-j128-1 F-j128-2 F-j128-3 (by the rows inside it) |
| s 128(1) | 10645-10658 | Subject to section 129, on the request in writing of the transferor... | fork | `s 128(1) the private company must act on the transferor's request` | F-j128-1 a duty limited by the request and section 129: NOTHING |
| s 128(1)(a) | 10648-10650 | any share in a private company — the company must lodge with the Re... | fork | `s 128(1)(a) a private company must lodge a notice of transfer of shares on the transferor's request` | F-j128-1 a duty limited by the request and section 129: NOTHING |
| s 128(1)(b) | 10652-10658 | any debenture or other interest in a private company — the company ... | fork | `s 128(1)(b) a private company must enter the name of the transferee on the transferor's request` | F-j128-1 a duty limited by the request and section 129: NOTHING |
| s 128(2) | 10660-10665 | The transfer of any share in a private company on or after 3 Januar... | encoded | `s 128(2) the transfer cannot yet take effect` |  |
| s 128(3) | 10667-10681 | On the request in writing of the transferor of a share or debenture... | encoded | `s 128(3) the private company must by written notice require delivery or production of the documents`; `s 128(3) the period stated in the notice is a period the subsection allows` (+1 more) |  |
| s 128(4) | 10683-10689 | If any person refuses or neglects to comply with a notice given und... | fork | `s 128(4) the transferor may apply to a judge for a summons` | F-j128-2 a grant gated by "if": NOTHING |
| s 128(5) | 10691-10700 | Upon appearance of a person so summoned the Court may examine the p... | fork | `s 128(5) the Court may order the person to deliver the documents to the company` | F-j128-3 a "may" gated by "upon": JUST FALSE (split site (ii)) |
| s 128(6) | 10702-10707 | Lists of share certificates or debentures called in under this sect... | encoded | `s 128(6) the company must exhibit the list in its office and advertise it`; `s 128(6) the company must exhibit and advertise the list` |  |
| s 128A | 10709-10709 | [Repealed by Act 36 of 2014] | repealed or blank in this text: [Repealed by Act 36 of 2014] |  |  |
| heading before s 129 | 10711-10711 | Notice of refusal to register transfer by private companies | inert, reason 1 (heading, no rule) |  |  |
| s 129 | 10713-10750 | (1) If a private company refuses to lodge a notice of transfer of a... | fork |  | F-j-unless F-j129-1 (by the rows inside it) |
| s 129(1) | 10713-10718 | If a private company refuses to lodge a notice of transfer of any s... | encoded | `s 129(1) the last day for sending notice of the refusal`; `s 129(1) the notice of the refusal was sent within 30 days` (+1 more) |  |
| s 129(2) | 10720-10729 | If a private company refuses to register a transfer of any debentur... | encoded | `s 129(2) the last day for sending notice of the refusal`; `s 129(2) the notice of the refusal was sent within 30 days` (+1 more) |  |
| s 129(3) | 10731-10743 | Where an application is made to a private company to lodge with the... | fork | `s 129(3) the last day for serving the written notice`; `s 129(3) the private company is barred from refusing by virtue of a discretion in the constitution` (+1 more) | F-j-unless an "unless" once met: JUST FALSE |
| s 129(4) | 10745-10750 | If default is made in complying with this section, the private comp... | fork | `s 129(4) the person is guilty of the offence this subsection creates`; `s 129(4) the most the person may be sentenced to on conviction` | F-j129-1 offence element unmet: JUST FALSE (split site (i)) |
| heading before s 130 | 10752-10752 | Transfer of shares and debentures in public companies | inert, reason 1 (heading, no rule) |  |  |
| s 130 | 10754-10782 | (1) Despite anything in its constitution, a public company must not... | fork |  | F-j-unless F-j130-1 F-j130-2 (by the rows inside it) |
| s 130(1) | 10754-10761 | Despite anything in its constitution, a public company must not reg... | fork | `s 130(1) the public company is barred from registering the transfer of shares or debentures`; `s 130(1) a public company must not register a transfer of shares or debentures without a proper instrument of transfer` | F-j-unless an "unless" once met: JUST FALSE |
| s 130(2) | 10763-10767 | Where there has been a transfer of shares, a public company may lod... | fork | `s 130(2) the public company may lodge with the Registrar a notice of the transfer of shares in the prescribed form` | F-j130-1 a "may" gated by "where": NOTHING (S1b ruling, 2026S1bC; split site (ii)) |
| s 130(3) | 10769-10782 | The notice must state — | fork | `s 130(3) the notice states what the subsection requires` | F-j130-2 "or" between (a) and (b): either suffices |
| s 130(3)(a) | 10771-10776 | every other transfer of shares effected prior to the date of the no... | fork | `s 130(3) the notice states what the subsection requires` (inside the rule of s 130(3)) | F-j130-2 "or" between (a) and (b): either suffices |
| s 130(3)(b) | 10778-10782 | the prescribed information in relation to the shares held by each o... | fork | `s 130(3) the notice states what the subsection requires` (inside the rule of s 130(3)) | F-j130-2 "or" between (a) and (b): either suffices |
| heading before s 130AA | 10784-10785 | Registration of transfer at request of transferor by public companies | inert, reason 1 (heading, no rule) |  |  |
| s 130AA | 10787-10834 | (1) On the request in writing of the transferor of any share, deben... | fork |  | F-j130AA-1 F-j130AA-2 F-j130AA-3 (by the rows inside it) |
| s 130AA(1) | 10787-10793 | On the request in writing of the transferor of any share, debenture... | fork | `s 130AA(1) the public company must enter the name of the transferee in the appropriate register`; `s 130AA(1) a public company must enter the name of the transferee on the transferor's request` | F-j130AA-1 a duty limited by the request: NOTHING |
| s 130AA(2) | 10795-10805 | On the request in writing of the transferor of a share or debenture... | encoded | `s 130AA(2) the public company must by written notice require delivery or production of the documents`; `s 130AA(2) the period stated in the notice is a period the subsection allows` (+1 more) |  |
| s 130AA(3) | 10807-10813 | If any person refuses or neglects to comply with a notice given und... | fork | `s 130AA(3) the transferor may apply to a judge for a summons` | F-j130AA-2 a grant gated by "if": NOTHING |
| s 130AA(4) | 10815-10827 | Upon appearance of a person so summoned the Court may examine the p... | fork | `s 130AA(4) the Court may order the person to deliver the documents to the company` | F-j130AA-3 a "may" gated by "upon": JUST FALSE (split site (ii)) |
| s 130AA(5) | 10829-10834 | Lists of share certificates or debentures called in under this sect... | encoded | `s 130AA(5) the company must exhibit the list in its office and advertise it`; `s 130AA(5) the company must exhibit and advertise the list` |  |
| heading before s 130AB | 10836-10836 | Notice of refusal to register transfer by public companies | inert, reason 1 (heading, no rule) |  |  |
| s 130AB | 10838-10862 | (1) If a public company refuses to register a transfer of any share... | fork |  | F-j-unless F-j130AB-1 (by the rows inside it) |
| s 130AB(1) | 10838-10843 | If a public company refuses to register a transfer of any share, de... | encoded | `s 130AB(1) the last day for sending notice of the refusal`; `s 130AB(1) the notice of the refusal was sent within 30 days` (+1 more) |  |
| s 130AB(2) | 10845-10855 | Where an application is made to a public company for a person to be... | fork | `s 130AB(2) the last day for serving the written notice`; `s 130AB(2) the public company is barred from refusing registration by virtue of a discretion in the constitution` (+1 more) | F-j-unless an "unless" once met: JUST FALSE |
| s 130AB(3) | 10857-10862 | If default is made in complying with this section, the public compa... | fork | `s 130AB(3) the person is guilty of the offence this subsection creates`; `s 130AB(3) the most the person may be sentenced to on conviction` | F-j130AB-1 offence element unmet: JUST FALSE (split site (i)) |
| heading before s 130AC | 10864-10864 | Transfer by personal representative | inert, reason 1 (heading, no rule) |  |  |
| s 130AC | 10866-10894 | (1) A transfer of the share, debenture or other interest of a decea... | encoded |  |  |
| s 130AC(1) | 10866-10873 | A transfer of the share, debenture or other interest of a deceased ... | encoded | `s 130AC(1) the transfer is as valid as if the personal representative had been a member of the company at the time of the execution of the instrument of transfer` |  |
| s 130AC(2) | 10875-10885 | The production to a company of any document which is by law suffici... | encoded | `s 130AC(2) the company must accept the document as sufficient evidence of the grant`; `s 130AC(2) a company must accept the document as sufficient evidence of the grant` |  |
| s 130AC(3) | 10887-10894 | In this section, “instrument of transfer” includes a written applic... | encoded | `s 130AC(3) "instrument of transfer" the document is an instrument of transfer for the purposes of section 130AC` |  |
| term "instrument of transfer" (s 130AC(3)) | 10887-10889 | In this section, "instrument of transfer" includes a written applic... | encoded | `s 130AC(3) "instrument of transfer" the document is an instrument of transfer for the purposes of section 130AC` |  |
| heading before s 130AD | 10896-10896 | Certification of prima facie title | inert, reason 1 (heading, no rule) |  |  |
| s 130AD | 10898-10976 | (1) The certification by a company of any instrument of transfer of... | fork |  | F-j130AD-1 F-j130AD-3 F-j130AD-2 (by the rows inside it) |
| s 130AD(1) | 10898-10907 | The certification by a company of any instrument of transfer of sha... | encoded | `s 130AD(1) the certification is taken as a representation that documents showing a prima facie title in the transferor have been produced to the company`; `s 130AD(1) the certification is taken as a representation that the transferor has any title` |  |
| s 130AD(2) | 10909-10913 | Where any person acts on the faith of a false certification by a co... | fork | `s 130AD(2) the company is under the same liability to the person as if the certification had been made fraudulently` | F-j130AD-1 a liability whose "where" is unmet: JUST FALSE |
| s 130AD(3) | 10915-10933 | Where any certification by a private company is expressed to be lim... | fork | `s 130AD(3) the last day of the period so limited or any extension of it` | F-j130AD-3 "shall not ... be liable" limited by its own wording: NOTHING outside it |
| s 130AD(3)(a) | 10920-10924 | in respect of any transfer of shares after the expiration of the pe... | fork | `s 130AD(3)(a) the company and its officers are liable in respect of the transfer of shares` | F-j130AD-3 "shall not ... be liable" limited by its own wording: NOTHING outside it |
| s 130AD(3)(b) | 10926-10933 | in respect of the registration of any transfer of debentures or oth... | fork | `s 130AD(3)(b) the company and its officers are liable in respect of the registration of the transfer of debentures or other interests` | F-j130AD-3 "shall not ... be liable" limited by its own wording: NOTHING outside it |
| s 130AD(4) | 10935-10948 | Where any certification by a public company is expressed to be limi... | fork | `s 130AD(4) the company and its officers are liable in respect of the registration of the transfer of shares, debentures or other interests` | F-j130AD-3 "shall not ... be liable" limited by its own wording: NOTHING outside it |
| s 130AD(5) | 10950-10976 | For the purposes of this section — | fork |  | F-j130AD-2 (by the rows inside it) |
| s 130AD(5)(a) | 10952-10954 | an instrument of transfer is to be treated as certificated if it be... | fork | `s 130AD(5)(a) the instrument of transfer is treated as certificated` | F-j130AD-2 a deeming "if" gives a sufficient condition only |
| s 130AD(5)(b) | 10956-10966 | the certification of an instrument of transfer is to be treated as ... | fork | `s 130AD(5)(b) the certification of the instrument of transfer is treated as made by the company` | F-j130AD-2 a deeming "if" gives a sufficient condition only |
| s 130AD(5)(b)(i) | 10959-10961 | the person issuing the instrument is a person apparently authorised... | fork | `s 130AD(5)(b) the certification of the instrument of transfer is treated as made by the company` (inside the rule of s 130AD(5)(b)) | F-j130AD-2 a deeming "if" gives a sufficient condition only |
| s 130AD(5)(b)(ii) | 10963-10966 | the certification is signed by a person apparently authorised to ce... | fork | `s 130AD(5)(b) the certification of the instrument of transfer is treated as made by the company` (inside the rule of s 130AD(5)(b)) | F-j130AD-2 a deeming "if" gives a sufficient condition only |
| s 130AD(5)(c) | 10968-10976 | a certification that purports to be authenticated by a person’s sig... | fork | `s 130AD(5)(c) the certification is deemed to be signed by the person` | F-j130AD-2 a deeming "unless": closed by its own wording (the lettering of this paragraph is odd) |
| heading before s 130AE | 10978-10979 | Duties of company with respect to issue of certificates and default... | inert, reason 1 (heading, no rule) |  |  |
| s 130AE | 10981-11031 | (1) Every public company must within 60 days after the allotment of... | fork |  | F-j130AE-1 F-j130AE-2 F-j130AE-3 (by the rows inside it) |
| s 130AE(1) | 10981-10992 | Every public company must within 60 days after the allotment of any... | fork | `s 130AE(1) the last day for completing the certificates after an allotment`; `s 130AE(1) the public company completed the certificates in time after the allotment` (+5 more) | F-j130AE-1 "(other than X)": the carve-out answers JUST FALSE |
| s 130AE(2) | 10994-11011 | Every private company must — | fork |  | F-j130AE-1 (by the rows inside it) |
| s 130AE(2)(a) | 10996-10997 | within 60 days after the allotment of any of its shares or debentures; | encoded | `s 130AE(2)(a) the last day for completing the certificates after an allotment`; `s 130AE(2)(a) the private company completed the certificates in time after the allotment` (+1 more) |  |
| s 130AE(2)(b) | 10999-11001 | within 30 days after the date on which a notice of transfer of shar... | encoded | `s 130AE(2)(b) the last day for completing the certificates after a notice of transfer of shares was lodged`; `s 130AE(2)(b) the private company completed the certificates in time after the notice of transfer of shares was lodged` (+1 more) |  |
| s 130AE(2)(c) | 11003-11011 | within 30 days after the date on which a transfer (other than such ... | fork | `s 130AE(2)(c) the last day for completing the certificates after a transfer of debentures was lodged`; `s 130AE(2)(c) the private company must complete the certificates after the transfer of debentures` (+2 more) | F-j130AE-1 "(other than X)": the carve-out answers JUST FALSE |
| s 130AE(3) | 11013-11018 | If default is made in complying with this section, the company and ... | fork | `s 130AE(3) the person is guilty of the offence this subsection creates`; `s 130AE(3) the most the person may be sentenced to on conviction` | F-j130AE-2 offence element unmet: JUST FALSE (split site (i)) |
| s 130AE(4) | 11020-11031 | If any company on which a notice has been served requiring the comp... | fork | `s 130AE(4) the last day for the company to make good the default`; `s 130AE(4) the company failed to make good the default within 10 days after the service of the notice` (+2 more) | F-j130AE-3 a power gated by "if" and an application: NOTHING (split site (ii)) |
| Division 7A | 11033-11037 | Division 7A — [Repealed by Act 36 of 2014] | repealed or blank in this text: Division 7A — [Repealed by Act 36 of 2014] |  |  |
| ss 130A to 130P | 11034-11037 | 130A. to 130P. [Repealed by Act 36 of 2014] | repealed or blank in this text: 130A. to 130P. [Repealed by Act 36 of 2014] |  |  |
| Part 5 heading | 11493-11493 | PART 5 | inert, reason 1 (heading, no rule) |  |  |
| Part 5 title | 11495-11495 | MANAGEMENT AND ADMINISTRATION | inert, reason 1 (heading, no rule) |  |  |
| Division 1 | 11497-11590 | Division 1 — Office and name | inert, reason 1 (heading, no rule) |  |  |
| heading before s 142 | 11499-11499 | Registered office of company | inert, reason 1 (heading, no rule) |  |  |
| s 142 | 11501-11510 | (1) A company must as from the date of its incorporation have a reg... | fork |  | F-j142-1 F-j142-2 (by the rows inside it) |
| s 142(1) | 11501-11505 | A company must as from the date of its incorporation have a registe... | fork | `s 142(1) the company has a registered office as the subsection requires`; `s 142(1) the company must have a registered office from the date of its incorporation` (+1 more) | F-j142-1 "as from the date of its incorporation" read as a deadline of 0 days |
| s 142(2) | 11507-11510 | If default is made in complying with subsection (1), the company an... | fork | `s 142(2) the person is guilty of the offence this subsection creates`; `s 142(2) the most the person may be sentenced to on conviction` | F-j142-2 offence element unmet: JUST FALSE (split site (i)) |
| heading before s 143 | 11512-11512 | Office hours | inert, reason 1 (heading, no rule) |  |  |
| s 143 | 11514-11540 | (1) Notice in the prescribed form of the situation of the registere... | fork |  | F-j143-1 (by the rows inside it) |
| s 143(1) | 11514-11529 | Notice in the prescribed form of the situation of the registered of... | encoded | `s 143(1) the notice must state the days and hours during which the office is open and accessible to the public`; `s 143(1) the proposed company's notice was lodged as the subsection requires` (+3 more) |  |
| s 143(1A) | 11531-11533 | In subsection (1), the word “particulars”, in relation to the situa... | encoded | `s 143(1A) "particulars" the item is within the particulars of the situation of the registered office` |  |
| term "particulars" (s 143(1A)) | 11531-11533 | In subsection (1), the word "particulars" includes the address and ... | encoded | `s 143(1A) "particulars" the item is within the particulars of the situation of the registered office` |  |
| heading before s 143(2) | 11535-11535 | Penalty | inert, reason 1 (heading, no rule) |  |  |
| s 143(2) | 11537-11540 | If default is made in complying with this section, the company and ... | fork | `s 143(2) the person is guilty of the offence this subsection creates`; `s 143(2) the most the person may be sentenced to on conviction` | F-j143-1 offence element unmet: JUST FALSE (split site (i)); no fine stated here |
| heading before s 144 | 11542-11542 | Publication of name and registration number | inert, reason 1 (heading, no rule) |  |  |
| s 144 | 11544-11590 | (1) The name of a company must appear in legible romanised letters ... | fork |  | F-j144-1 F-j144-2 F-j144-3 F-j144-4 (by the rows inside it) |
| s 144(1) | 11544-11555 | The name of a company must appear in legible romanised letters on — | encoded | `s 144(1) the name of the company must appear on the item`; `s 144(1) the company has complied with subsection (1) as to the item` |  |
| s 144(1)(a) | 11547-11547 | its seal, if any; and | encoded | `s 144(1) the name of the company must appear on the item`; `s 144(1) the company has complied with subsection (1) as to the item` (inside the rule of s 144(1)) |  |
| s 144(1)(b) | 11549-11555 | all business letters, statements of account, invoices, official not... | encoded | `s 144(1) the name of the company must appear on the item`; `s 144(1) the company has complied with subsection (1) as to the item` (inside the rule of s 144(1)) |  |
| s 144(1A) | 11557-11560 | The registration number of a company must appear in a legible form ... | encoded | `s 144(1A) the registration number of the company must appear on the item`; `s 144(1A) the company has complied with subsection (1A) as to the item` |  |
| s 144(1B) | 11562-11566 | A company shall be guilty of an offence if default is made in compl... | fork | `s 144(1B) the person is guilty of the offence this subsection creates`; `s 144(1B) the most the company may be sentenced to on conviction` | F-j144-1 F-j144-2 offence element unmet: JUST FALSE (split site (i)); no fine stated |
| s 144(2) | 11568-11590 | If an officer of a company or any person on its behalf — | fork | `s 144(2) the person is guilty of the offence this subsection creates`; `s 144(2) the most the person may be sentenced to on conviction` (+1 more) | F-j144-2 F-j144-3 F-j144-4 offence element unmet (split site (i)); no fine stated; the liability list is not closed |
| s 144(2)(a) | 11570-11571 | uses or authorises the use of any seal purporting to be a seal of t... | fork | `s 144(2) the person is guilty of the offence this subsection creates`; `s 144(2) the most the person may be sentenced to on conviction` (+1 more) (inside the rule of s 144(2)) | F-j144-2 F-j144-3 F-j144-4 offence element unmet (split site (i)); no fine stated; the liability list is not closed |
| s 144(2)(b) | 11573-11576 | issues or authorises the issue of any business letter, statement of... | fork | `s 144(2) the person is guilty of the offence this subsection creates`; `s 144(2) the most the person may be sentenced to on conviction` (+1 more) (inside the rule of s 144(2)) | F-j144-2 F-j144-3 F-j144-4 offence element unmet (split site (i)); no fine stated; the liability list is not closed |
| s 144(2)(c) | 11578-11590 | signs, issues or authorises to be signed or issued on behalf of the... | fork | `s 144(2) the person is guilty of the offence this subsection creates`; `s 144(2) the most the person may be sentenced to on conviction` (+1 more) (inside the rule of s 144(2)) | F-j144-2 F-j144-3 F-j144-4 offence element unmet (split site (i)); no fine stated; the liability list is not closed |


## Fork register (sgj)

Each entry gives the provision, the function that carries the reading taken, every reading seen with the text that licenses it, and the one taken.
A fork is a place where the text can be read two or more ways with different outcomes, or where the Guide leaves the answer to the encoder (the rulings of 2026-11-05, 2026-11-12 and the "decide case by case" ruling of 2026-11-05T10:25Z, in `inputs/ENCODING-GUIDE.md` lines 86 and 93 to 98).
"Assumed, not ruled" applies to every entry: the reading taken is this part's, for a reviewer to overrule.
A row of the coverage table with disposition `fork` points here by id.

### Division 4 (ss 79 to 91)

- **F-j79-1**, s 79(2), `s 79(2) the body is a company for the purposes of this Division`.
  The text: "A reference to a company is a reference — (a) [Deleted by Act 2 of 2009]; (b) to a body corporate, being a body incorporated in Singapore, that is for the time being declared by the Minister ... to be a company ...; or (c) to a body, not being a body corporate formed in Singapore, that is ... declared".
  Reading 1 (taken): a body that neither (b) nor (c) declares is not covered, `NOTHING`; the list is not closed with "only", and the deleted (a) is no longer there to cover other companies.
  Reading 2: every company the Act otherwise calls a company is still one for the Division, so the answer for it is yes.
- **F-j81-1**, s 81(3), `s 81(3) the person is a substantial shareholder in the company`.
  The text: "a person who has a substantial shareholding in a company is a substantial shareholder in the company" (one direction).
  Reading 1 (taken): a person with neither a (1) nor a (2) shareholding is not covered, `NOTHING`.
  Reading 2: "is" is a definition, so such a person is not a substantial shareholder, `JUST FALSE`.
- **F-j83-1**, s 83(1), `s 83(1) the substantial shareholder must give notice of a change in the percentage level`.
  The text: "Where there is a change in the percentage level ... the substantial shareholder must give written notice".
  Reading 1 (taken): where the percentage level does not change, the duty does not arise, `JUST FALSE` (item (b) of the periods ruling of 2026-11-05, a "where" that fails).
  Reading 2: `NOTHING`, because the section does not say that nothing is due.
- **F-j87-1**, s 87, `s 87 the Registrar has power to extend the time for giving the notice`.
  The text: "The Registrar may, on the application of a person who is required to give a notice under this Division, in the Registrar's discretion, extend, or further extend, the time for giving the notice."
  Reading 1 (taken): a power whose gate (an application by a person required to give notice) is unmet answers `NOTHING` (the grant ruling of 2026-11-12, limit 1); split site (ii).
  Reading 2: `JUST FALSE`, "no application, no power".
- **F-j88-1**, s 88(1), `s 88(1) the company must immediately enter the notice in the register`.
  "immediately" is read as a deadline of 0 days after receipt of the notice, so the trace clock counts days from receipt; the other reading is "without delay", which no clock can test.
- **F-j88-2**, s 88(5) (offence of default, fine up to $5,000): the person who is neither the company nor an officer in default, or where no default is made, is not guilty, `JUST FALSE` (split site (i)); the other reading is `NOTHING`.
- **F-j89-1**, s 89 (failing to comply with ss 82, 83, 84 or 86 is an offence): where nobody has failed, `JUST FALSE` (split site (i)); the other reading is `NOTHING`.
- **F-j91-1**, s 91(1) and s 91(4), the Court's power "where" a person is or was a substantial shareholder and has failed to comply, on the Minister's application; and "where a share is not sold".
  Reading 1 (taken): where the gate fails the answer is `JUST FALSE` (item (b) of the periods ruling, "where" fails); split site (ii), listed for a lawyer as the grant ruling's limit 3 requires.
  Reading 2: `NOTHING` (the grant ruling: a grant limited by its own wording does not say no outside the limit).
- **F-j91-2**, s 91(2), (3), (7), (8): grants gated by "if" (or "before", or an order made): `NOTHING` where the gate fails (the grant ruling, limit 1); the other reading is `JUST FALSE`.
- **F-j91-3**, s 91(10): contravening or failing to comply with an order is an offence; where nobody has, `JUST FALSE` (split site (i)).
- **F-j91-4**, s 91(6), `s 91(6) the Court is barred from making the order`.
  The text: the Court must not make an order, "other than an order restraining the exercise of voting rights", if it is satisfied of two things.
  The carve-out answers `JUST FALSE` ("other than X" in the text's own words); where the Court is not so satisfied the prohibition is limited by its own wording and the answer is `NOTHING`.
  The other reading of the second branch is `JUST FALSE`: "must not ... if satisfied" would then mean "may ... if not satisfied".

### Division 5 (ss 93 to 100)

- **F-j93-1**, s 93(4): "a register is deemed to be duly closed if closed in accordance with ... (not exceeding in the aggregate 30 days in any calendar year)".
  A deeming "if" gives a sufficient condition and does not say "only": `NOTHING` where the condition is unmet (taken); the other reading is `JUST FALSE`.
- **F-j93-3**, s 93(7) and s 93(9): the offences of refusing inspection or a copy, and of failing to comply with the section.
  Where an element is unmet, `JUST FALSE` (split site (i)).
  Subsection (7) states no fine; its penalty function answers `NOTHING` (points outside the text); subsection (9) states one.
- **F-j93-4**, s 93(5) and (6): the company "must, at the request of the holder, ... on payment of $1 for every page" (and $3 for a copy of the trust deed): the duty is limited by the request and the payment, so without them `NOTHING` (taken); the other reading is `JUST FALSE`.
- **F-j93-5**, s 93(8) (the branch register): "A company which issues debentures may cause to be kept in any place outside Singapore a branch register": a grant limited by its own wording, `NOTHING` outside it; the other reading is `JUST FALSE`.
  The seam: this part answers the keel's `s 4(1) "branch register"` limb (b) with `s 93(8) the register is a branch register of holders of debentures kept pursuant to section 93`.
- **F-j94-1**, s 94: "A contract with a company to take up and pay for any debentures of the company may be enforced by an order for specific performance": a grant limited by the kind of contract, `NOTHING` for any other contract (taken); the other reading is `JUST FALSE`.
- **F-j96-1**, s 96(2), an "entitled"-named function (a claim, not a power; the Guide does not settle it): "After the reissue the person entitled to the debentures has ... the same priorities".
  `NOTHING` where the debentures have not been reissued (taken); the other reading is `JUST FALSE`.
  Count of "entitled"-named functions in this part: 1.
- **F-j100-1**, s 100(1): the Court's power to order a security enforceable "if on the application" of the trustee or holder it is satisfied of three things.
  A power whose "if" gate fails answers `NOTHING` (grant ruling, limit 1), and where subsection (3) excludes the debenture (offered to the public) the answer is `JUST FALSE`.
  The 60% test is written as "100 times the proceeds is at most 60 times the principal".

### Division 7, title (ss 121 to 125)

- **F-j123-1** and **F-j123-2**, s 123(4): the offence of default; where an element is unmet `JUST FALSE` (split site (i)); the subsection states no fine, so the penalty function answers `NOTHING` (points outside the text).
- **F-j124-1**, s 124: "A company may, if authorised by its constitution, have a duplicate common seal": a grant gated by "if", `NOTHING` where the constitution does not authorise it (grant ruling, limit 1); the other reading is `JUST FALSE`.
- **F-j125-1**, s 125(2): "Where the value of the shares or debentures represented by the certificate or document is greater than $500 the directors of the company may, before accepting an application ..., require the applicant" to advertise or to furnish a bond: a "may" gated by "where", `JUST FALSE` where the value is $500 or less (item (b)); split site (ii); the other reading is `NOTHING`.
- **F-j125-2**, s 125(1): the duty to issue a duplicate "on payment of a fee not exceeding $2", subject to subsection (2): outside the stated gates `NOTHING` (taken); the other reading is `JUST FALSE`.

### Division 7, private companies (ss 126 to 129)

- **F-j-unless**, ss 126(1), 127, 129(3), 130(1), 130AB(2): each is a prohibition with an "unless" ("must not ... unless a proper instrument of transfer has been delivered"; "must not refuse ... unless it has served ... within 30 days beginning with the day on which the application was made, a written notice").
  Once the "unless" is met the bar is closed and the answer is `JUST FALSE` (taken; the Guide's own words, line 86, are "a condition the text introduces with ... 'unless'"); the other reading is `NOTHING`, that the text does not say the act is then allowed.
  The carve-out for a person to whom the right "has been transmitted by operation of law" ("this section does not affect any power ...") is a flat negative and answers `JUST FALSE`.
- **F-j126-1**, s 126(2): "Where there has been a transfer of shares, a private company must lodge ... notice": where there has been none, `JUST FALSE` (as F-j83-1); the other reading is `NOTHING`.
  The subsection states no time, so the rule has no deadline (see "Rules with no breach path").
- **F-j128-1**, s 128(1): "Subject to section 129, on the request in writing of the transferor ... the company must": a duty limited by the request and by s 129, `NOTHING` outside (taken).
  The reason a duty gated by "on the request" is answered `NOTHING` while a duty gated by "where" is answered `JUST FALSE` (F-j83-1, F-j126-1) is the words: the periods ruling names "where" and the delegated-definitions ruling names "when", "upon" and "whenever"; "on the request" is neither.
  The other reading is `JUST FALSE` for both.
- **F-j128-2**, s 128(4) (and F-j130AA-2, s 130AA(3)): "If any person refuses or neglects to comply with a notice ..., the transferor may apply to a judge": a grant gated by "if", `NOTHING` where the gate is unmet (grant ruling, limit 1); the other reading is `JUST FALSE`.
- **F-j128-3**, s 128(5) (and F-j130AA-3, s 130AA(4)): "Upon appearance of a person so summoned ... the Court may order": a "may" gated by "upon", `JUST FALSE` where neither appearance nor non-appearance after due service has happened (item (b) of the periods ruling, "upon" counting as "where" under item (c) of the delegated-definitions ruling); split site (ii); the other reading is `NOTHING`.
- **F-j129-1**, s 129(4): the offence of default; `JUST FALSE` where an element is unmet (split site (i)); the fine is stated ($1,000 and a default penalty).

### Division 7, public companies (ss 130 to 130AE)

- **F-j130-1**, s 130(2): "Where there has been a transfer of shares, a public company may lodge ... a notice": a "may" gated by "where", `NOTHING` where there has been no transfer (S1b ruling, Guide line 101, 2026S1bC: the public company's own liberty to lodge a notice, no bar to relieve); split site (ii); the other reading is `JUST FALSE` (item (b)).
- **F-j130-2**, s 130(3): "The notice must state — (a) every other transfer ...; or (b) the prescribed information ...".
  Reading 1 (taken): the text says "or", so stating either suffices; a notice that states neither is `JUST FALSE`.
  Reading 2: "and" was meant, so both are required.
  See finding 2.
- **F-j130AA-1**, s 130AA(1): as F-j128-1 (a duty on the written request).
- **F-j130AB-1**, s 130AB(3): the offence of default; `JUST FALSE` where an element is unmet (split site (i)).
- **F-j130AD-1**, s 130AD(2): "Where any person acts on the faith of a false certification by a company made negligently, the company is under the same liability ... as if the certification had been made fraudulently": a liability whose "where" is unmet, `JUST FALSE` (item (b), as F-j83-1); the other reading is `NOTHING`.
- **F-j130AD-2**, s 130AD(5)(a), (b), (c): "is to be treated as certificated if it bears the words", "is to be treated as made by a company if", "is deemed to be signed by the person unless it is shown": the deeming "if" gives a sufficient condition and does not say "only", so `NOTHING` where it is unmet (as F-j93-1); the deeming "unless" is closed by its own wording, so `JUST FALSE` once the "unless" is met.
  The lettering of (c) is odd (finding 3); (c) is read as a free-standing deeming, the alternative being a further condition of (b).
- **F-j130AD-3**, s 130AD(3) and (4): "the company and its officers shall not, in the absence of fraud, be liable ... after the expiration of the period so limited or any extension thereof given by the company if the instrument of transfer has not ... been lodged".
  A flat negative limited by its own wording: `JUST FALSE` where every limb is met, `NOTHING` where one is not (a certification limited to fewer than 42 days, fraud, the transfer within the period, the instrument lodged in time); the other reading is `JUST FALSE` throughout.
  The period is the certification date plus the days limited to plus the days of any extension, counted by sg-periods (P1); a transfer on the last day is not "after the expiration".
- **F-j130AE-1**, s 130AE(1) and (2)(c): "(other than such a transfer as the company is for any reason entitled to refuse to register and does not register)": such a transfer is outside the duty, `JUST FALSE`, in the text's own words (the "(other than X)" question of the ruling of 2026-11-05T10:25Z); the other reading is `NOTHING`.
  Where no transfer has been lodged the duty does not start and the answer is `NOTHING` (a scope limit with no "only", item (c) of the periods ruling).
- **F-j130AE-2**, s 130AE(3): the offence of default; `JUST FALSE` where an element is unmet (split site (i)).
- **F-j130AE-3**, s 130AE(4): "If any company ... fails to make good the default within 10 days after the service of the notice, the Court may, on the application of the person entitled": a power gated by "if" and by an application, `NOTHING` where either gate is unmet (grant ruling, limit 1; split site (ii)); the other reading is `JUST FALSE`.

### Part 5, Division 1 (ss 142 to 144)

- **F-j142-1**, s 142(1): "as from the date of its incorporation" is read as a deadline of 0 days after it; the other reading is a continuing state with no deadline.
- **F-j142-2**, s 142(2) (and **F-j143-1**, s 143(2)): the offence of default; `JUST FALSE` where an element is unmet (split site (i)); a fine up to $5,000 and a default penalty is stated.
- **F-j144-1**, s 144(1B): "A company shall be guilty of an offence if default is made in complying with subsection (1) or (1A)": `JUST FALSE` where no default is made (split site (i)); **F-j144-2**: no fine is stated in s 144(1B) or (2), so both penalty functions answer `NOTHING` (points outside the text).
- **F-j144-3**, s 144(2)(a), (b), (c): "If an officer of a company or any person on its behalf ...": `JUST FALSE` where the person is neither (split site (i)); `NOTHING` where the person did something other than (a), (b) or (c).
- **F-j144-4**, s 144(2), the liability to the holder "unless it is paid by the company": the list names a bill of exchange, promissory note, other negotiable instrument, indorsement and order, and does not name a cheque, receipt or letter of credit (which appear in (c) for the offence only); the list is not closed with "only". **Changed after the wave-2 independent reader (scenarios 151b and 152), assumed, not ruled:** a cheque answers as an "other negotiable instrument" (limb (c) of the same subsection writes "cheque or other negotiable instrument", so the text itself treats a cheque as one kind of negotiable instrument); a receipt and a letter of credit still answer `NOTHING` (taken); the other reading is that "negotiable instrument ... or order" reaches them.

### Counting periods

- **F-j-periods** (assumed, not ruled; the keel's P1 to P10 in `sg-periods.l4` are the counting rules).
  A duty with a deadline is tested as "the act is done not later than the last day" (`AT MOST`): an act on the day of the event, or earlier, is in time.
  The keel's `period: the date is within a period after` would call an act on the day of the event late (P2); this part uses it nowhere, and does not decide that question.
  Affected: every function named `the last day for ...` or `... within ... days`, and every regulative rule with a `WITHIN` (the clock of a trace counts days after the event).
  The other reading: an act on the day of the event is not "within" the period.

## Jural relations (sgj)

Hohfeld's kinds, read from the text: a duty and its correlative claim; a power and its correlative liability; a privilege (the absence of a duty) and its correlative no-claim; an immunity and its correlative disability.
The kind is the text's own ("must", "may", "is liable", "shall not", "does not affect"); the column "carried by" names the layer-1 rule that carries it.
A rule that binds the Court or the Registrar is listed because it is what that decision means for the individual, and for nothing else.

| provision | holder of the advantage | the other party | kind | carried by |
| --- | --- | --- | --- | --- |
| s 80(1) | the State (the Act binds every natural person and body corporate) | any person | claim / duty | `s 80(1) the obligation to comply with this Division extends to the person` |
| s 80(3) | any person, once exempted by Gazette order | the Minister | immunity / disability (a power of the Minister creates it) | `s 80(3) the person is exempt from the provision of this Division` |
| s 82(1) | the company | the substantial shareholder | claim / duty (notice within 2 business days) | rule `s 82(1) a substantial shareholder must give notice ...` |
| s 83(1), s 84 | the company | the substantial shareholder, the person who ceases to be one | claim / duty | rules `s 83(1) ...`, `s 84 ...` |
| s 86(1) | the non-resident | the holder of the voting shares | claim / duty (notice within 2 days) | rule `s 86(1) a holder of shares ... must give the non-resident a notice ...` |
| s 86(2A) | the Depository | the Act | immunity / disability (the section does not apply) | `s 86(2A) section 86 applies to the person` |
| s 87 | the person required to give a notice | the Registrar | liability / power (the Registrar may extend the time) | `s 87 the Registrar has power to extend the time for giving the notice` |
| s 88(1), (4) | the Registrar (and the persons who may inspect) | the company | claim / duty (keep and enter immediately; furnish within 7 days) | rules `s 88(1) ...`, `s 88(4) ...` |
| s 88(2), (3) | any person, a member | the company | claim / duty (inspect; a copy within 14 days) with the company's privilege to charge the stated sums | `s 88(2) ...`, `s 88(3) ...` |
| s 88(5), s 89 | the State | the company, the officer in default, the person who fails | claim / duty; the State's power to prosecute and the person's liability to the stated fine | `s 88(5) ...`, `s 89 ...` |
| s 88(6) | the company | any person | immunity / disability (notice or inquiry is not implied by this Division alone) | `s 88(6)(a)`, `s 88(6)(b)` |
| s 90 | the defendant | the prosecution | immunity / disability (a defence on proof of unawareness) | `s 90(1) this section gives a defence on these facts` |
| s 91(1) to (4), (7), (8) | the Minister (applicant) | the defaulting substantial shareholder | power / liability (the Court's orders) | `s 91(1) ...` to `s 91(8) ...` |
| s 91(5) | any person who might be prejudiced | the Court | claim / duty | rule `s 91(5) the Court must satisfy itself ...` |
| s 91(6) | the person who failed | the Court | immunity / disability (the Court must not order unless ...) | rule `s 91(6) ...` and `s 91(6) the Court is barred from making the order` |
| s 91(10) | the State | the person who contravenes an order | claim / duty; liability to a fine | `s 91(10) ...` |
| s 93(1), (2), (3) | the holder of debentures; the Registrar | the company | claim / duty (keep the register; notice within 7 days; open to inspection) | rules `s 93(1) ...`, `s 93(2) ...`, `s 93(3) ...` |
| s 93(5), (6) | the person who asks | the company | claim / duty (a copy on payment; a copy of the trust deed within one month) | `s 93(5) ...`, `s 93(6) ...` |
| s 93(7), (9) | the State | the company and the officer in default | claim / duty; liability | `s 93(7) ...`, `s 93(9) ...` |
| s 93(8) | the company | the world | privilege / no-claim (it may keep a branch register outside Singapore) | `s 93(8) the company may cause a branch register ... to be kept outside Singapore` |
| s 94 | the other party to the contract | the company | power / liability (specific performance) | `s 94 ...` |
| s 95 | the company | a person who attacks the condition | immunity / disability | `s 95 ...` |
| s 96(1), (2), (3) | the company; the person entitled to reissued debentures; the holder of deposited debentures | any person who denies it | power / liability; claim (the same priorities); immunity | `s 96(1) ...`, `s 96(2) ...`, `s 96(3) ...` |
| s 100(1) to (3) | the holder of irredeemable debentures (through the Court) | the borrowing corporation | power / liability; s 100(2) preserves another power; s 100(3) an immunity for public offers | `s 100(1) ...`, `s 100(2) ...`, `s 100(3) ...` |
| s 121 | the member | the world | the legal nature of the share: movable, transferable under the constitution | `s 121 ...` |
| s 122(1), (2) | the member | the company | claim / duty (each share numbered) with an exception | `s 122(1) ...`, `s 122(2)(a)`, `s 122(2)(b)` |
| s 123(1) to (4) | the member | the company | claim / duty (a certificate under seal, evidence of title); liability to a fine for default | rule `s 123(2) ...`, `s 123(4) ...` |
| s 124 | the company | the world | privilege / no-claim (a duplicate common seal) | `s 124 the company may have a duplicate common seal` |
| s 125(1) | the owner of the lost certificate | the company | claim / duty (a duplicate on payment of up to $2) | rule `s 125(1) the company must issue a duplicate ...` |
| s 125(2) | the directors | the applicant | power / liability (advertise or furnish a bond above $500) | `s 125(2) ...` |
| s 126(1), s 127 | the transferor and the world | the private company | disability (the company must not lodge or register without the instrument); immunity of the person whose right is transmitted | rules `s 126(1) ...`, `s 127 ...` |
| s 126(2) | the Registrar | the private company | claim / duty (lodge notice of the transfer) | rule `s 126(2) ...` |
| s 126(3), s 128(2) | the transferor | the Registrar | the transfer does not take effect until the register is updated (an exposure, not a duty) | `s 126(3) ...`, `s 128(2) ...` |
| s 128(1), (3), (6) | the transferor | the private company | claim / duty (act on the request; require the documents in 7 to 28 days; exhibit and advertise the lists) | rules `s 128(1)(a)`, `s 128(1)(b)`, `s 128(3) ...`, `s 128(6) ...` |
| s 128(4), (5) | the transferor; the Court | the person who refuses; that person | power / liability (apply to a judge; the Court may order delivery) | `s 128(4) ...`, `s 128(5) ...` |
| s 129(1), (2) | the transferor and the transferee | the private company | claim / duty (notice of refusal within 30 days) | rules `s 129(1) ...`, `s 129(2) ...` |
| s 129(3) | the applicant | the private company | disability (must not refuse by a discretion unless a notice is served within 30 days) | rule `s 129(3) ...` |
| s 129(4) | the State | the company and the officer in default | claim / duty; liability to $1,000 and a default penalty | `s 129(4) ...` |
| s 130(1) | the transferor and the world | the public company | disability (as s 126(1)); immunity of the person whose right is transmitted | rule `s 130(1) ...` |
| s 130(2), (3) | the public company; the Registrar | the Registrar; the public company | privilege (it may lodge the notice); claim / duty (what the notice states) | `s 130(2) ...`, `s 130(3) ...` |
| s 130AA(1) to (5) | the transferor | the public company | as s 128(1), (3), (4), (5), (6) | rules `s 130AA(1) ...`, `s 130AA(2) ...`, `s 130AA(5) ...` |
| s 130AB(1), (2), (3) | the transferor and transferee; the applicant; the State | the public company and its officers | claim / duty (30 days); disability (no refusal by a discretion without a timely notice); liability | rules `s 130AB(1) ...`, `s 130AB(2) ...`, `s 130AB(3) ...` |
| s 130AC(1), (2), (3) | the personal representative; the transferee | the company | power (a valid transfer); claim / duty (accept the document as evidence of the grant); a definition | `s 130AC(1) ...`, rule `s 130AC(2) ...`, `s 130AC(3) ...` |
| s 130AD(1), (2) | the person who acts on a certification | the company | claim / liability (a representation of prima facie title only; negligence is treated as fraud) | `s 130AD(1) ...`, `s 130AD(2) ...` |
| s 130AD(3), (4) | the company and its officers | the person who acts on a certification | immunity / disability (no liability after the period, absent fraud) | `s 130AD(3)(a)`, `s 130AD(3)(b)`, `s 130AD(4)` |
| s 130AE(1), (2) | the person who awaits certificates | the company | claim / duty (complete and have ready within 60 or 30 days) | rules `s 130AE(1) ...`, `s 130AE(2)(a)`, `s 130AE(2)(b)`, `s 130AE(2)(c)` |
| s 130AE(3), (4) | the State; the person entitled to the certificates (through the Court) | the company and its officers | liability to a fine; power / liability (the Court's order after 10 days) | `s 130AE(3) ...`, `s 130AE(4) ...` |
| s 142(1), s 143(1), s 144(1), (1A) | the public; the Registrar | the company | claim / duty (a registered office open 3 hours; notice within 14 days; the name and number displayed) | rules `s 142(1) ...`, `s 143(1) ...`, functions `s 144(1) ...`, `s 144(1A) ...` |
| s 142(2), s 143(2), s 144(1B), s 144(2) | the State; the holder of an instrument | the company, the officer in default, the person acting for the company | liability to a fine; s 144(2) also a liability to the holder for the amount due | `s 142(2) ...`, `s 143(2) ...`, `s 144(1B) ...`, `s 144(2) ...` |


## Marginal readings for a lawyer (sgj)

Two readings are left for a lawyer by the rule of 2026-10-29 (assumed, not ruled): (a) a failed "if" counts as the text's no, clause by clause, within the provision that holds the "if" (an inference: "if A then B" does not itself say "if not A then not B"), and flat negatives count as the text saying no; (b) a prohibition or grant limited by its own wording does not.
This part takes both as the status quo.
**The other reading of (a):** every branch in the first table below would answer `NOTHING` instead of `JUST FALSE`.
**The other reading of (b):** every branch in the second table would answer `JUST FALSE` instead of `NOTHING`.
The branches that say no in words that need no inference ("means", a flat negative such as "does not", "shall not", "may not") are not marginal and are not listed: 40 of the 113 `JUST FALSE` branches.
The split between the two kinds of `JUST FALSE` is made by a pattern over the words quoted in each tag (`work/mkmarginal.py`), so a reviewer should read the first table and not rely on the split.
The counts of every tagged branch in layer 1, from the comment tags (`work/mkmarginal.py`):

```
73 JUST FALSE resting on reading (a)
40 JUST FALSE, flat negative or a definition (not marginal)
6 NOTHING (includes)
78 NOTHING (limited by its own wording)
10 NOTHING (list not closed)
5 NOTHING (points outside the text)
26 NOTHING (silent)
1 NOTHING (undefined term)
total tagged branches 239

```

Beyond the two readings, the sites the Guide leaves to the encoder are in the fork register with the other reading stated (the nine type (ii) split sites, the nine grants gated by "if", the "entitled"-named function, the "unless" and "(other than X)" questions).

### Reading a result: FALSE and NOTHING (sgj)

A result of type `MAYBE BOOLEAN` is read the same way everywhere in this part.
`JUST TRUE` is yes.
`JUST FALSE` is the text's own no: the text itself says no to the case in its own words (a "means" definition, a condition it introduces with "if", "unless", "while", a period it fixes in its own words, a flat negative such as "shall not", a duty or an offence's own question).
`NOTHING` is not covered: the text is silent, lists without closing the list, says "includes", leaves a term undefined, points outside the sources, or limits a grant or prohibition in its own wording and the case falls outside the limit.
A caller must never turn `NOTHING` into `FALSE`: for a bar, `NOTHING` and `JUST FALSE` are not a grant, and for a grant, `NOTHING` is not a refusal.
Each branch in layer 1 carries a comment, `-- FALSE-kind (the text says no in its own words): "..."` or `-- NOTHING-kind (silent | list not closed | includes | undefined term | points outside the text | limited by its own wording)`, with the words that decide it.
The branch counts are in the section "Marginal readings for a lawyer (sgj)".
A function that returns a plain `BOOLEAN`, `NUMBER` or `DATE` (the last day of a period; a figure the text fixes) cannot say "not covered", and a rule that can give only a yes or only a no has no case for the other answer in `sgj-cases-seat.l4`.

**Assumed, not ruled (the ruling of 2026-10-29 for what `JUST FALSE` and `NOTHING` mean):** two readings are left for a lawyer, and every branch that rests on one is listed under "Marginal readings for a lawyer (sgj)" with the other reading stated.

### Reading (a): a failed "if", "where", "unless", period or the provision's own question counts as the text's no (72 branches)

| module | line | function | the text's words |
| --- | --- | --- | --- |
| div4-substantial-shareholdings | 132 | `s 81(4) the share is a voting share for the purposes of section 81 and section 83` | "In this section and section 83, “voting shares” exclude treasury shares" |
| div4-substantial-shareholdings | 148 | `s 81(1)(a) the person has an interest or interests in one or more voting shares in the company` | "a person has a substantial shareholding in a company if (a) the person has an interest or interests in one or more voting shares in the company" -... |
| div4-substantial-shareholdings | 180 | `s 81(1) the person has a substantial shareholding in the company` | "a person has a substantial shareholding in a company if (a) ...; and (b) ..." -- a condition introduced with "if" (marginal reading (a)) |
| div4-substantial-shareholdings | 204 | `s 81(2) the person has a substantial shareholding in the company, the share capital of which is divided into 2 or more classes` | "a person has a substantial shareholding in a company, being a company the share capital of which is divided into 2 or more classes of shares, if (... |
| div4-substantial-shareholdings | 251 | `s 82(1) the notice is the notice the subsection requires` | "A person who is a substantial shareholder in a company must give written notice to the company stating ..." -- a duty: the provision's own question |
| div4-substantial-shareholdings | 283 | `s 82(2) the notice was given within the time the subsection allows` | "The notice must be given ... within 2 business days after becoming a substantial shareholder" -- a period the text fixes in its own words; outside... |
| div4-substantial-shareholdings | 376 | `s 83(1) the notice was given within 2 business days after the substantial shareholder became aware` | "within 2 business days after the substantial shareholder becomes aware of such a change" -- a period the text fixes in its own words (periods ruli... |
| div4-substantial-shareholdings | 402 | `s 83(2) the notice states the information the subsection specifies` | "must give written notice to the company stating the information specified in subsection (2)" -- a duty: the provision's own question |
| div4-substantial-shareholdings | 426 | `s 84(1) the notice is the notice the subsection requires` | "A person who ceases to be a substantial shareholder in a company must give written notice to the company stating ..." -- a duty: the provision's o... |
| div4-substantial-shareholdings | 445 | `s 84(2) the notice was given within 2 business days after the person ceased to be a substantial shareholder` | "The notice must be given within 2 business days after the person ceased to be a substantial shareholder" -- a period the text fixes in its own words |
| div4-substantial-shareholdings | 530 | `s 86(1) the holder must give the non-resident a notice` | "A person who holds voting shares in a company, being voting shares in which a non-resident has an interest, must give to the non-resident a notice... |
| div4-substantial-shareholdings | 539 | `s 86(1) the notice is the notice the subsection requires` | "must give to the non-resident a notice in the prescribed form as to the requirements of this Division" -- a duty: the provision's own question |
| div4-substantial-shareholdings | 569 | `s 86(2) the notice was given within the time the subsection allows` | "within 2 days after becoming the holder" -- a period the text fixes in its own words |
| div4-substantial-shareholdings | 590 | `s 86(4) section 86 affects the operation of section 80` | "Nothing in this section affects the operation of section 80" |
| div4-substantial-shareholdings | 615 | `s 87 the notice was given within the time as extended` | "extend, or further extend, the time for giving the notice" -- the time is the extended time; after it the notice is late |
| div4-substantial-shareholdings | 642 | `s 88(1) the company has kept the register as the subsection requires` | "A company must keep a register in which it must immediately enter" -- a duty: the provision's own question |
| div4-substantial-shareholdings | 709 | `s 88(3) the company sent the copy within the time the subsection allows` | "the company must send the copy to that person, within 14 days or such longer period as the Registrar thinks fit" -- a period the text fixes in its... |
| div4-substantial-shareholdings | 740 | `s 88(4) the company furnished the copy within 7 days after the day the requirement was received` | "the company must furnish the copy within 7 days after the day on which the requirement is received by the company" -- a period the text fixes in i... |
| div4-substantial-shareholdings | 766 | `s 88(5) the person is guilty of the offence this subsection creates` | "If default is made in complying with this section, the company and every officer of the company who is in default shall be guilty of an offence" -... |
| div4-substantial-shareholdings | 824 | `s 89 the person is guilty of the offence this section creates` | "A person who fails to comply with section 82, 83, 84 or 86 shall be guilty of an offence" -- the element is unmet (split site (i), fork line F-j89-1) |
| div4-substantial-shareholdings | 963 | `s 91(1) the Court may make the order on the Minister's application` | "Where a person is a substantial shareholder ... and has failed to comply with section 82, 83 or 84, the Court may, on the application of the Minis... |
| div4-substantial-shareholdings | 1110 | `s 91(10) the person is guilty of the offence this subsection creates` | "Any person who contravenes or fails to comply with an order made under this section that is applicable to the person shall be guilty of an offence... |
| div5-debentures | 41 | `s 93(1) the company has kept the register as the subsection requires` | "must keep a register of holders of the debentures at the registered office of the company or at some other place in Singapore" -- a duty: the prov... |
| div5-debentures | 72 | `s 93(2) the notice was lodged within 7 days` | "must within 7 days after the register is first kept at a place other than the registered office lodge with the Registrar notice" -- a period the t... |
| div5-debentures | 116 | `s 93(3) the register must be open to the inspection of the person` | "The register must except when duly closed be open to the inspection of ..." |
| div5-debentures | 128 | `s 93(3) the register has the content the subsection requires` | "must contain particulars of the names and addresses of the debenture holders and the amount of debentures held by them" -- a duty: the provision's... |
| div5-debentures | 169 | `s 93(5) the copy must include the particulars` | "the copy need not include any particulars as to any debenture holder other than the debenture holder’s name and address and the debentures held" |
| div5-debentures | 223 | `s 93(7) the copy was forwarded within the time the subsection allows` | "within a reasonable time (but not more than one month) after a request has been made" -- a period the text fixes in its own words (periods ruling ... |
| div5-debentures | 236 | `s 93(7) the person is guilty of the offence this subsection creates` | "If inspection is refused, or a copy is refused or not forwarded within a reasonable time ..., the company and every officer of the company who is ... |
| div5-debentures | 297 | `s 93(9) the person is guilty of the offence this subsection creates` | "If a company fails to comply with this section, the company and every officer of the company who is in default shall be guilty of an offence" -- a... |
| div5-debentures | 371 | `s 96(1) the company has power to reissue the redeemed debentures` | "unless any provision to the contrary ... is contained in the constitution or in any contract ...; or unless the company has ... manifested its int... |
| div5-debentures | 406 | `s 96(3) the debentures are deemed to have been redeemed by reason of the account having ceased to be in debit` | "the debentures are not deemed to have been redeemed by reason only of the account of the company having ceased to be in debit while the debentures... |
| div7-private-transfers | 214 | `s 128(3) the period stated in the notice is a period the subsection allows` | "within a stated period, being not less than 7 and not more than 28 days after the date of the notice" |
| div7-private-transfers | 310 | `s 129(1) the notice of the refusal was sent within 30 days` | "it must, within 30 days after the date on which the transfer was lodged with it, send to the transferor and the transferee notice of the refusal" ... |
| div7-private-transfers | 340 | `s 129(2) the notice of the refusal was sent within 30 days` | "it must, within 30 days after the date on which the transfer was lodged with it, send to the transferor and to the transferee notice of the refusa... |
| div7-private-transfers | 409 | `s 129(4) the person is guilty of the offence this subsection creates` | "If default is made in complying with this section, the private company and every officer of the company who is in default shall each be guilty of ... |
| div7-public-transfers | 84 | `s 130(3) the notice states what the subsection requires` | "The notice must state (a) every other transfer ...; or (b) the prescribed information ..." -- a duty: the provision's own question |
| div7-public-transfers | 142 | `s 130AA(2) the period stated in the notice is a period the subsection allows` | "within a stated period, being not less than 7 and not more than 28 days after the date of the notice" |
| div7-public-transfers | 231 | `s 130AB(1) the notice of the refusal was sent within 30 days` | "it must, within 30 days after the date on which the transfer was lodged with it, send to the transferor and to the transferee notice of the refusa... |
| div7-public-transfers | 300 | `s 130AB(3) the person is guilty of the offence this subsection creates` | "If default is made in complying with this section, the public company and every officer of the company who is in default shall each be guilty of a... |
| div7-public-transfers | 409 | `s 130AD(2) the company is under the same liability to the person as if the certification had been made fraudulently` | "Where any person acts on the faith of a false certification by a company made negligently, the company is under the same liability" -- a liability... |
| div7-public-transfers | 552 | `s 130AD(5)(c) the certification is deemed to be signed by the person` | "is deemed to be signed by the person unless it is shown that the signature or initials were not placed there by the person and were not placed the... |
| div7-public-transfers | 588 | `s 130AE(1) the public company completed the certificates in time after the allotment` | "must within 60 days after the allotment of any of its shares or debentures ... complete and have ready for delivery all the appropriate certificat... |
| div7-public-transfers | 622 | `s 130AE(1) the public company completed the certificates in time after the transfer` | "must ... within 30 days after the date on which a transfer ... is lodged with the company, complete and have ready for delivery all the appropriat... |
| div7-public-transfers | 664 | `s 130AE(2)(a) the private company completed the certificates in time after the allotment` | "must (a) within 60 days after the allotment of any of its shares or debentures ... complete and have ready for delivery all the appropriate certif... |
| div7-public-transfers | 696 | `s 130AE(2)(b) the private company completed the certificates in time after the notice of transfer of shares was lodged` | "must (b) within 30 days after the date on which a notice of transfer of shares is lodged with the Registrar under section 126(2) or 128(1)(a) ... ... |
| div7-public-transfers | 743 | `s 130AE(2)(c) the private company completed the certificates in time after the transfer of debentures` | "must (c) within 30 days after the date on which a transfer ... of any of its debentures is lodged with the company ... complete and have ready for... |
| div7-public-transfers | 768 | `s 130AE(3) the person is guilty of the offence this subsection creates` | "If default is made in complying with this section, the company and every officer of the company who is in default shall each be guilty of an offen... |
| div7-title | 87 | `s 122(1) the share must be distinguished by an appropriate number` | "Despite subsection (1) — ... none of those shares need ... have a distinguishing number" |
| div7-title | 133 | `s 123(2) the share certificate is as the subsection requires` | "Every share certificate must be under the common seal ... and must state as at the date of the issue of the certificate" -- a duty: the provision'... |
| div7-title | 165 | `s 123(4) the person is guilty of the offence this subsection creates` | "If default is made in complying with this section, the company and every officer of the company who is in default shall be guilty of an offence" -... |
| div7-title | 196 | `s 124 the duplicate common seal is as the section requires` | "a duplicate common seal which must be a facsimile of the common seal of the company with the addition on its face of the words “Share Seal”" |
| div7-title | 249 | `s 125(2) the directors may require the applicant to advertise or to furnish a bond, or both` | "Where the value of the shares or debentures represented by the certificate or document is greater than $500 the directors of the company may" -- a... |
| div7-title | 258 | `s 125(2)(a) the owner applies after the expiration of 14 days after the publication of the advertisement` | "the owner intends after the expiration of 14 days after the publication of the advertisement to apply to the company for a duplicate" -- a period ... |
| div7-title | 267 | `s 125(2)(b) the bond is for an amount the paragraph allows the directors to require` | "a bond for an amount equal to at least the current market value of the shares or debentures" |
| part5-office-name | 36 | `s 142(1) the company has a registered office as the subsection requires` | "A company must as from the date of its incorporation have a registered office within Singapore ... which must be open and accessible to the public... |
| part5-office-name | 84 | `s 142(2) the person is guilty of the offence this subsection creates` | "If default is made in complying with subsection (1), the company and every officer of the company who is in default shall be guilty of an offence"... |
| part5-office-name | 118 | `s 143(1) the notice must state the days and hours during which the office is open and accessible to the public` | "no notice of the days and hours during which the office is open and accessible to the public is required if the office is open for at least 5 hour... |
| part5-office-name | 128 | `s 143(1) the proposed company's notice was lodged as the subsection requires` | "must, in the case of a proposed company, be lodged with the Registrar together with its constitution, at the time of lodgment for the incorporatio... |
| part5-office-name | 145 | `s 143(1) the notice of the change was lodged within 14 days after the change` | "be so lodged within 14 days after any such change" -- a period the text fixes in its own words; outside it the answer is the text's no (periods ru... |
| part5-office-name | 185 | `s 143(2) the person is guilty of the offence this subsection creates` | "If default is made in complying with this section, the company and every officer of the company who is in default shall be guilty of an offence" -... |
| part5-office-name | 256 | `s 144(1) the company has complied with subsection (1) as to the item` | "The name of a company must appear in legible romanised letters on" the listed items -- a duty, the provision's own question |
| part5-office-name | 284 | `s 144(1A) the company has complied with subsection (1A) as to the item` | "The registration number of a company must appear in a legible form on" the listed items -- a duty, the provision's own question |
| part5-office-name | 297 | `s 144(1B) the person is guilty of the offence this subsection creates` | "A company shall be guilty of an offence if default is made in complying with subsection (1) or (1A)" -- an element is unmet (split site (i), fork ... |
| part5-office-name | 340 | `s 144(2) the person is guilty of the offence this subsection creates` | "If an officer of a company or any person on its behalf — (a) uses or authorises the use of any seal ... he or she shall be guilty of an offence" -... |
| part5-office-name | 342 | `s 144(2) the person is guilty of the offence this subsection creates` | paragraph (b), same element (split site (i), fork line F-j144-3) |
| part5-office-name | 344 | `s 144(2) the person is guilty of the offence this subsection creates` | paragraph (c), same element (split site (i), fork line F-j144-3) |
| part5-office-name | 377 | `s 144(2) the person is liable to the holder of the instrument for the amount due on it` | "unless it is paid by the company" |
| part5-office-name | 378 | `s 144(2) the person is liable to the holder of the instrument for the amount due on it` | "unless it is paid by the company" |
| part5-office-name | 379 | `s 144(2) the person is liable to the holder of the instrument for the amount due on it` | "unless it is paid by the company" |
| part5-office-name | 380 | `s 144(2) the person is liable to the holder of the instrument for the amount due on it` | "unless it is paid by the company" |
| part5-office-name | 381 | `s 144(2) the person is liable to the holder of the instrument for the amount due on it` | "unless it is paid by the company" |

### Reading (b): a prohibition or grant limited by its own wording does not say no (79 branches)

| module | line | function | the text's words |
| --- | --- | --- | --- |
| div4-substantial-shareholdings | 67 | `s 79(3) the interest in the stock is deemed to be an interest in an issued share in the company` | the deeming is "In relation to a company the whole or a portion of the share capital of which consists of stock"; outside it the subsection is silent |
| div4-substantial-shareholdings | 315 | `s 82(3) the notice must be given although the person has ceased to be a substantial shareholder` | "The notice must be so given even though the person has ceased to be a substantial shareholder before the expiration of whichever period ... is app... |
| div4-substantial-shareholdings | 606 | `s 87 the Registrar has power to extend the time for giving the notice` | "may, on the application of a person who is required to give a notice under this Division" -- without the application or the requirement the sectio... |
| div4-substantial-shareholdings | 786 | `s 88(5) the further fine for a continuing offence` | the further fine is "in the case of a continuing offence" |
| div4-substantial-shareholdings | 800 | `s 88(6)(a) the company is to be taken to have notice of a right of a person to or in relation to a share` | the text speaks only of "anything done under this Division" |
| div4-substantial-shareholdings | 808 | `s 88(6)(b) the company is to be put upon inquiry as to a right of a person to or in relation to a share` | the text speaks only of "anything done under this Division" |
| div4-substantial-shareholdings | 842 | `s 89 the further fine for a continuing offence` | the further fine is "in the case of a continuing offence" |
| div4-substantial-shareholdings | 975 | `s 91(2) the order may include the provision` | "may include such ancillary or consequential provisions as the Court thinks just" (a grant limited by its own wording, fork F-j91-2) |
| div4-substantial-shareholdings | 991 | `s 91(3) the sale order may provide the time and conditions of the sale` | "may provide that the sale must be made within such time and subject to such conditions (if any) as the Court thinks fit" (a grant limited by its o... |
| div4-substantial-shareholdings | 1049 | `s 91(6) the Court is barred from making the order` | "must not make an order ... if it is satisfied (a) ... and (b) ..." -- a prohibition limited by its own wording; where the Court is not so satisfie... |
| div4-substantial-shareholdings | 1071 | `s 91(7) the Court may direct that notice of the application be given or published` | "The Court may, before making an order under this section, direct that notice of the application be given ... or published" (a grant limited by its... |
| div4-substantial-shareholdings | 1082 | `s 91(8) the Court may rescind, vary, discharge or suspend the operation of the order` | "may rescind, vary or discharge an order made by it under this section or suspend the operation of such an order" (a grant limited by its own wordi... |
| div4-substantial-shareholdings | 1095 | `s 91(9) section 214 of the Insolvency, Restructuring and Dissolution Act 2018 applies to the share` | the application is "in relation to a share that vests in the Registrar under this section" |
| div4-substantial-shareholdings | 1128 | `s 91(10) the further fine for a continuing offence` | the further fine is "in the case of a continuing offence" |
| div5-debentures | 38 | `s 93(1) the company has kept the register as the subsection requires` | "Every company which issues debentures (not being debentures transferable by delivery)" -- a scope limit with no "only" |
| div5-debentures | 101 | `s 93(4) the register is deemed to be duly closed` | "a register is deemed to be duly closed if closed in accordance with ... (not exceeding in the aggregate 30 days in any calendar year)" -- a deemin... |
| div5-debentures | 156 | `s 93(5) the company must supply the person with a copy of the register` | "must, at the request of the holder, be supplied ... on payment of $1 for every page or part thereof" -- the duty is limited by the holder's reques... |
| div5-debentures | 187 | `s 93(6) the company must forward the copy of the trust deed to the holder` | "must be forwarded ... to a holder of those debentures at the holder's request on payment of the sum of $3" -- without the request and the payment ... |
| div5-debentures | 258 | `s 93(8) the company may cause a branch register of debenture holders to be kept outside Singapore` | "A company which issues debentures may cause to be kept in any place outside Singapore a branch register" -- a grant limited by its own wording (th... |
| div5-debentures | 274 | `s 93(8) the branch register is deemed to be part of the company's register of debenture holders` | "a branch register of debenture holders which is deemed to be part of the company’s register" |
| div5-debentures | 282 | `s 93(8) Division 4 of Part 5 applies, with the adaptations necessary, to the keeping of the branch register` | "Division 4 of Part 5 applies with such adaptations as are necessary to and in relation to the keeping of a branch register of debenture holders" |
| div5-debentures | 321 | `s 94 the contract may be enforced by an order for specific performance` | "A contract with a company to take up and pay for any debentures of the company may be enforced by an order for specific performance" -- a grant li... |
| div5-debentures | 339 | `s 95 the condition is invalid by reason only that it makes the debentures irredeemable or redeemable only on a contingency or after a period` | "by reason only" -- another ground of invalidity is not covered |
| div5-debentures | 368 | `s 96(1) the company has power to reissue the redeemed debentures` | "Where a company has redeemed any debentures" -- a scope limit with no "only" |
| div5-debentures | 379 | `s 96(1) the reissue is regarded as the issue of a new debenture for the purpose of a provision limiting the amount or number of debentures` | the text speaks of a reissue or substitute issue under this subsection |
| div5-debentures | 390 | `s 96(2) the person entitled to the debentures has the same priorities as if the debentures had never been redeemed` | "After the reissue" -- without a reissue the subsection is silent |
| div5-debentures | 407 | `s 96(3) the debentures are deemed to have been redeemed by reason of the account having ceased to be in debit` | "by reason only" and "while the debentures remain so deposited" |
| div5-debentures | 489 | `s 100(1) the Court may order that the security be enforceable` | "shall, if the Court so orders, be enforceable ... if on the application ... the Court is satisfied that (a) ...; (b) ...; and (c) ..." -- a power ... |
| div7-private-transfers | 34 | `s 126(1) the private company is barred from lodging the transfer of shares` | "a private company must not lodge a transfer of shares" -- a scope limit with no "only"; the public company's rule is s 130(1) |
| div7-private-transfers | 60 | `s 126(2) the private company must lodge with the Registrar notice of the transfer of shares` | "a private company must lodge" -- a scope limit with no "only"; the public company's rule is s 130(2) |
| div7-private-transfers | 89 | `s 126(3) the transfer cannot yet take effect` | "A transfer of any share in a private company on or after 3 January 2016" -- a scope limit with no "only" |
| div7-private-transfers | 109 | `s 127 the private company is barred from registering the transfer of debentures` | "a private company must not register a transfer of debentures" -- a scope limit with no "only"; the public company's rule is s 130(1) |
| div7-private-transfers | 152 | `s 128(1) the private company must act on the transferor's request` | "Subject to section 129, on the request in writing of the transferor ... the company must" -- the duty is limited by the written request and by sec... |
| div7-private-transfers | 187 | `s 128(2) the transfer cannot yet take effect` | "The transfer of any share in a private company on or after 3 January 2016" -- a scope limit with no "only" |
| div7-private-transfers | 206 | `s 128(3) the private company must by written notice require delivery or production of the documents` | "On the request in writing of the transferor of a share or debenture, the private company must" -- without the written request, or for another comp... |
| div7-private-transfers | 237 | `s 128(4) the transferor may apply to a judge for a summons` | "If any person refuses or neglects to comply with a notice given under subsection (3), the transferor may apply to a judge" -- a grant whose "if" g... |
| div7-private-transfers | 270 | `s 128(6) the company must exhibit the list in its office and advertise it` | "Lists of share certificates or debentures called in under this section and not delivered or produced" |
| div7-private-transfers | 377 | `s 129(3) the private company is barred from refusing by virtue of a discretion in the constitution` | "Where an application is made to a private company ... in respect of any share that has been transferred or transmitted to a person by act of parti... |
| div7-public-transfers | 32 | `s 130(1) the public company is barred from registering the transfer of shares or debentures` | "a public company must not register a transfer of shares or debentures" -- a scope limit with no "only"; the private company's rules are ss 126 and... |
| div7-public-transfers | 59 | `s 130(2) the public company may lodge with the Registrar a notice of the transfer of shares in the prescribed form` | "a public company may lodge" -- a scope limit with no "only"; the private company's rule is s 126(2) |
| div7-public-transfers | 62 | `s 130(2) the public company may lodge with the Registrar a notice of the transfer of shares in the prescribed form` | "Where there has been a transfer of shares, a public company may lodge" -- a failed "where" gate on the company's own liberty to lodge, no bar to relieve (the S1b ruling, 2026S1bC; listed for a lawyer) |
| div7-public-transfers | 80 | `s 130(3) the notice states what the subsection requires` | "The notice must state" -- the notice of subsection (2); another notice is outside the text |
| div7-public-transfers | 106 | `s 130AA(1) the public company must enter the name of the transferee in the appropriate register` | "On the request in writing of the transferor ... the company must" -- the duty is limited by the written request; without it, or for another compan... |
| div7-public-transfers | 134 | `s 130AA(2) the public company must by written notice require delivery or production of the documents` | "On the request in writing of the transferor of a share or debenture the public company must" -- without the written request, or for another compan... |
| div7-public-transfers | 165 | `s 130AA(3) the transferor may apply to a judge for a summons` | "If any person refuses or neglects to comply with a notice given under subsection (2), the transferor may apply to a judge" -- a grant whose "if" g... |
| div7-public-transfers | 197 | `s 130AA(5) the company must exhibit the list in its office and advertise it` | "Lists of share certificates or debentures called in under this section and not brought in" |
| div7-public-transfers | 268 | `s 130AB(2) the public company is barred from refusing registration by virtue of a discretion in the constitution` | "Where an application is made to a public company for a person to be registered as a member in respect of shares which have been transferred or tra... |
| div7-public-transfers | 331 | `s 130AC(1) the transfer is as valid as if the personal representative had been a member of the company at the time of the execution of the instrument of transfer` | "A transfer of the share, debenture or other interest of a deceased person made by the deceased person's personal representative" -- a deeming limi... |
| div7-public-transfers | 346 | `s 130AC(2) the company must accept the document as sufficient evidence of the grant` | "The production to a company of any document which is by law sufficient evidence of probate of the will, or letters of administration of the estate... |
| div7-public-transfers | 387 | `s 130AD(1) the certification is taken as a representation that documents showing a prima facie title in the transferor have been produced to the company` | "The certification by a company of any instrument of transfer ... is to be taken as a representation by the company to any person acting on the fai... |
| div7-public-transfers | 395 | `s 130AD(1) the certification is taken as a representation that the transferor has any title` | the negative is stated of the certification of an instrument of transfer |
| div7-public-transfers | 452 | `s 130AD(3)(a) the company and its officers are liable in respect of the transfer of shares` | "Where any certification by a private company is expressed to be limited to 42 days or any longer period", "in the absence of fraud", "after the ex... |
| div7-public-transfers | 470 | `s 130AD(3)(b) the company and its officers are liable in respect of the registration of the transfer of debentures or other interests` | "Where any certification by a private company is expressed to be limited to 42 days or any longer period", "in the absence of fraud", "after the ex... |
| div7-public-transfers | 496 | `s 130AD(4) the company and its officers are liable in respect of the registration of the transfer of shares, debentures or other interests` | "Where any certification by a public company is expressed to be limited to 42 days or any longer period", "in the absence of fraud", "after the exp... |
| div7-public-transfers | 510 | `s 130AD(5)(a) the instrument of transfer is treated as certificated` | "an instrument of transfer is to be treated as certificated if it bears the words" -- a deeming "if" with no "only" |
| div7-public-transfers | 532 | `s 130AD(5)(b) the certification of the instrument of transfer is treated as made by the company` | "is to be treated as made by a company if" -- a deeming "if" with no "only" |
| div7-public-transfers | 550 | `s 130AD(5)(c) the certification is deemed to be signed by the person` | "a certification that purports to be authenticated by a person's signature or initials" -- the deeming is limited to such a certification |
| div7-public-transfers | 585 | `s 130AE(1) the public company completed the certificates in time after the allotment` | "Every public company must" -- a scope limit with no "only"; the private company's rule is subsection (2) |
| div7-public-transfers | 605 | `s 130AE(1) the public company must complete the certificates after the transfer` | "Every public company must" -- a scope limit with no "only"; the private company's rule is subsection (2) |
| div7-public-transfers | 607 | `s 130AE(1) the public company must complete the certificates after the transfer` | "within 30 days after the date on which a transfer ... is lodged with the company" -- a duty that starts with a lodging; where nothing was lodged t... |
| div7-public-transfers | 619 | `s 130AE(1) the public company completed the certificates in time after the transfer` | "Every public company must" -- a scope limit with no "only"; the private company's rule is subsection (2) |
| div7-public-transfers | 661 | `s 130AE(2)(a) the private company completed the certificates in time after the allotment` | "Every private company must" -- a scope limit with no "only"; the public company's rule is subsection (1) |
| div7-public-transfers | 693 | `s 130AE(2)(b) the private company completed the certificates in time after the notice of transfer of shares was lodged` | "Every private company must" -- a scope limit with no "only"; the public company's rule is subsection (1) |
| div7-public-transfers | 726 | `s 130AE(2)(c) the private company must complete the certificates after the transfer of debentures` | "Every private company must" -- a scope limit with no "only"; the public company's rule is subsection (1) |
| div7-public-transfers | 728 | `s 130AE(2)(c) the private company must complete the certificates after the transfer of debentures` | "within 30 days after the date on which a transfer ... of any of its debentures is lodged with the company" -- a duty that starts with a lodging; w... |
| div7-public-transfers | 740 | `s 130AE(2)(c) the private company completed the certificates in time after the transfer of debentures` | "Every private company must" -- a scope limit with no "only"; the public company's rule is subsection (1) |
| div7-public-transfers | 820 | `s 130AE(4) the Court may make an order directing the company and any officer of the company to make good the default` | "If any company on which a notice has been served ... fails to make good the default within 10 days after the service of the notice, the Court may,... |
| div7-public-transfers | 828 | `s 130AE(4) the order may provide that all costs of and incidental to the application be borne by the company or by any officer of the company in default in such proportions as the Court thinks fit` | "the order may provide that all costs of and incidental to the application must be borne by the company or by any officer of the company in default... |
| div7-title | 23 | `s 121 the share or other interest of a member is movable property` | "The shares or other interest of any member in a company is movable property" -- the section speaks of a member's share or interest |
| div7-title | 31 | `s 121 the share or other interest of a member is of the nature of immovable property` | the section speaks of a member's share or interest |
| div7-title | 40 | `s 121 the share or other interest of a member is transferable in the manner provided by the constitution` | "transferable in the manner provided by the constitution" -- a transfer in another manner is not covered |
| div7-title | 60 | `s 122(2)(a) the shares need no distinguishing number` | "Despite subsection (1) — (a) if ... none of those shares need ... have a distinguishing number so long as ..." -- an exception that applies only o... |
| div7-title | 76 | `s 122(2)(b) the shares need no distinguishing number` | "or (b) if all the issued shares ... none of those shares need have a distinguishing number" -- an exception that applies only on its conditions |
| div7-title | 105 | `s 123(1) the certificate is prima facie evidence of the title of the member to the shares` | "A certificate under the common or official seal of a company specifying any shares held by any member ... is prima facie evidence" -- without the ... |
| div7-title | 187 | `s 124 the company may have a duplicate common seal` | "A company may, if authorised by its constitution, have a duplicate common seal" -- a grant whose "if" gate is unmet (grant ruling of 2026-11-12, l... |
| div7-title | 204 | `s 124 the certificate is deemed to be sealed with the common seal for the purposes of this Act` | "a certificate under such duplicate seal is deemed to be sealed with the common seal" |
| div7-title | 297 | `s 125(1) the company must issue a duplicate certificate or document to the owner` | "Subject to subsection (2), where a certificate ... is lost or destroyed, the company must on payment of a fee not exceeding $2 issue a duplicate .... |
| div7-title | 323 | `s 125(3) the duplicate must state the amount paid and the amount unpaid in place of the historical nominal value of the shares` | "Any duplicate certificate issued on or after 30 January 2006 in respect of a share certificate issued before that date" -- a scope limit with no "... |
| div7-title | 335 | `s 125(4) the owner is the Depository` | "in relation to a book‑entry security, a reference to an owner therein is to be construed as a reference to the Depository" |


## Seams (sgj)

A part cannot import another part, so a fact another part answers is an input here, named for the fact and the section it comes from (PLAN.md section 4).

**What this part takes (inputs, all `BOOLEAN` unless said).**

| asking provision | input | answered by |
| --- | --- | --- |
| s 126(3), s 128(2) | `the electronic register of members of the company has been updated by the Registrar under section 196A(5)` | s 196A(5) (sgm) |
| s 126(3), s 128(2) | `the day 3 January 2016` (a date, from `sg-core`) | the keel |
| ss 126 to 129, 130AE(2) | `the company is a private company` | s 4(1) "private company" (keel; three limb facts) |
| ss 130 to 130AE | `the company is a public company` | s 4(1) "public company" (keel) |
| s 81(1)(a) | the 14 facts of s 7 (`s 7 interest facts`) | `sg-interests` (called, not asked: `s 7 the person has an interest in the shares` with purpose `s 7(1) Division 4 of Part 4`) |
| s 79(4), s 81(1)(a) | `the shares are voting shares as section 4(1) defines the term` | `s 4(1) "voting share"` (keel; the test file composes the two) |
| s 130AE(2)(b) | `the day the notice of transfer of shares was lodged with the Registrar` | ss 126(2) and 128(1)(a) of this part: the rule's `WITHIN` clock starts there |
| s 130AD(3)(a) | `the instrument of transfer has been sent to or received by the company under section 126(1) within that period` | s 126(1) of this part, as a plain fact |
| ss 93, 100 | `the company issues debentures, as section 4(1) defines the word`, `the debenture is offered to the public ...` | `s 4(1) "debenture"` (keel) and facts |

**What this part gives (checked against `sg-definitions.l4` and the text).**
`s 93(8) the register is a branch register of holders of debentures kept pursuant to section 93` answers the keel's `s 4(1) "branch register"` limb (b) (source line 1235; the input there is named `the register is a branch register of holders of debentures kept pursuant to section 93`).
PLAN.md table A calls this seam "principal register"; the text and the keel ask for the branch register, and that is what is answered here (finding 10).
Other parts' citations of this part, from `inputs/XREFS.md`: s 88 (sgc2 line 19574, "the keeping of registers and books under sections 88, ..."; answer: `s 88(1) the company has kept the register as the subsection requires`), s 142 (sgc2 line 19571, "the maintenance of a registered office under sections 142, 143 and 144"; answers: `s 142(1) the company has a registered office as the subsection requires`, `s 143(1) the notice of the change was lodged within 14 days after the change`, `s 144(1) the company has complied with subsection (1) as to the item`) and s 126 (sgm line 17515, "section ... 126(2) or 128(1)(a)": the notices this part's rules `s 126(2) ...` and `s 128(1)(a) ...` require).
The citations by K at lines 1012 to 1025 are the table of contents of the Act, not seams.
No seam is needed that PLAN.md lacks, except the two internal ones above (s 126(1) from s 130AD(3)(a); the notice date from s 130AE(2)(b)), which are inside this part.


## Split sites (sgj)

The two questions of the brief: (i) an unmet element of an offence or a contravention: `JUST FALSE` or `NOTHING`?
(ii) a "may" gated by "where", "when", "upon", "on application", "with the consent of": `JUST FALSE` (item (b) of the periods ruling) or `NOTHING` (the grant ruling)?
Each site below is a fork line in the register above; the answer taken at each is the Guide's, not an invention of this part.

### Type (i): 13 sites, all answered `JUST FALSE`

Guide line 86: a function answers `JUST FALSE` where the text itself says no "in its own words: ... a condition the text introduces with 'if', ... a flat negative ('does not', 'shall not', 'may not')".
Guide line 98 (the grant ruling of 2026-11-12, limit 2): "keep `JUST FALSE` where the text closes the gate itself ..., and for a bar, a duty or the provision's own question".
An offence is introduced by "If default is made ..." or "A person who fails ...", and the question "is the person guilty" is the provision's own question.
The sites: s 88(5) (F-j88-2), s 89 (F-j89-1), s 91(10) (F-j91-3), s 93(7) and s 93(9) (F-j93-3), s 123(4) (F-j123-1), s 129(4) (F-j129-1), s 130AB(3) (F-j130AB-1), s 130AE(3) (F-j130AE-2), s 142(2) (F-j142-2), s 143(2) (F-j143-1), s 144(1B) (F-j144-1), s 144(2) (F-j144-3).
The other reading at each site is `NOTHING`; the penalty functions answer `NOTHING` wherever the person is not guilty, and where the text states no fine (ss 93(7), 123(4), 144(1B), 144(2)).

### Type (ii): 9 sites

Five answer `JUST FALSE` (item (b), Guide line 93: "a \"where ...\" condition: when it fails the answer is `JUST FALSE`"; line 94: "\"when\", \"upon\" and \"whenever\" count as \"where\" under rule (b)"), and the grant ruling's limit 3 (line 98) requires them to be listed for a lawyer without being changed:
s 91(1) (F-j91-1, "where" a person is or was a substantial shareholder and has failed to comply, on the Minister's application), s 91(4) (F-j91-1, "where a share is not sold"), s 125(2) (F-j125-1, "where the value ... is greater than $500"), s 128(5) (F-j128-3, "upon appearance"), s 130AA(4) (F-j130AA-3, "upon appearance").
Three answer `NOTHING` because the gate is an application (the text's "on the application of ..."), where the Guide has no line for "on application" and limit 1 of the grant ruling (line 97, "answer `NOTHING`, with one fork line each, only for a function named for a grant or a power ... whose `if` gate failed") is the nearest: s 87 (F-j87-1), s 100(1) (F-j100-1), s 130AE(4) (F-j130AE-3).
These three sit outside the Guide's lines, and are listed under Marginal readings for a lawyer.
One more answers `NOTHING` by the S1b ruling (Guide line 101, 2026S1bC), which replaces limit 3 for it: s 130(2) (F-j130-1, "where there has been a transfer of shares"), a failed "where" gate on the public company's own liberty to lodge a notice.
The other reading at each site is the opposite answer.

### Grants gated by "if" or by their own scope (not split sites of type (ii), answered `NOTHING` by limit 1)

Nine functions: s 91(2), s 91(3), s 91(7), s 91(8) (F-j91-2), s 93(8) (F-j93-5), s 94 (F-j94-1), s 124 (F-j124-1), s 128(4) (F-j128-2), s 130AA(3) (F-j130AA-2).
Guide line 96: a function named for a grant "that answers `JUST FALSE` because an `if` gate failed reads as 'may not': a grant turned into a bar".
"Entitled"-named functions (a claim, not a power; Guide line 98, limit 3): one, `s 96(2) the person entitled to the debentures has the same priorities ...` (F-j96-1), answered `NOTHING` outside the reissue.


## Rules with no breach path (sgj)

> Added 2026-11-27 (decided by Claude, assumed, not ruled): this section was written before the pass recorded in `lest-without-deadline.md`, and it is no longer true of the rules listed below.
> Each of them now takes an input-length `WITHIN` and can reach `BREACH`, so read "no time limit", "no deadline" and "no breach path" of them as the position before that pass, here and wherever else these notes say so of them:
>
> - `s 125(1) the company must issue a duplicate certificate or document`
> - `s 126(2) a private company must lodge notice of a transfer of shares with the Registrar`
> - `s 128(1)(a) a private company must lodge a notice of transfer of shares on the transferor's request`
> - `s 128(1)(b) a private company must enter the name of the transferee on the transferor's request`
> - `s 128(3) a private company must require delivery or production of the documents by written notice`
> - `s 130AA(1) a public company must enter the name of the transferee on the transferor's request`
> - `s 130AA(2) a public company must require delivery or production of the documents by written notice`
>
> The other rules named in this section are unchanged.

A regulative rule has a breach path when a trace of the passing of time, or of the wrong act, ends in `BREACH`.
**Duties with a deadline** have one: the clock passes the `WITHIN` and the rule is breached (19 rules, each with a trace for in time, late and never in the tests).
**Prohibitions** (`SHANT`) have one: the forbidden act itself is breached (6 rules: s 91(6), s 126(1), s 127, s 129(3), s 130(1), s 130AB(2)); with no act the prohibition stands, and the trace says `RESIDUAL`.
**Duties with no deadline have none**: the text states no time, so no length of time passing breaches them, and no event the model names is a breach.
The trace ends `FULFILLED` when the act is done and `RESIDUAL` when it is not; it never ends in `BREACH`.
These 15 rules are: s 91(5) (the Court's duty), s 93(1), s 93(3), s 123(2), s 125(1), s 126(2), s 128(1)(a), s 128(1)(b), s 128(3), s 128(6), s 130AA(1), s 130AA(2), s 130AA(5), s 130AC(2), s 142(1) (the open-hours rule).
Each has a trace in its test file asserting `RESIDUAL` for time passing and `FULFILLED` for the act, so the absence of a breach path is itself a tested result and not an omission.
For the other readings of s 126(2), the text could be read as "forthwith"; this part does not (see finding 5).

## What the text turns out to say

Numbered findings from reading the text closely.
Each was checked against the lines named (the line numbers are of `CoA1967.txt`).

1. **s 79(2): paragraph (a) is deleted, and the list still reads "(b) ...; or (c) ...".**
   Lines 9891 to 9901 show "(a) [Deleted by Act 2 of 2009]" and then (b) ending "; or" and (c) ending ".".
   A reader of the consolidation cannot tell from the text which companies (a) used to cover; this part answers `NOTHING` for a body that neither (b) nor (c) declares (F-j79-1).
2. **s 130(3): "(a) ...; or (b) ..." between two things the notice "must state".**
   Lines 10769 to 10780: "The notice must state — (a) every other transfer of shares effected prior to the date of the notice, other than a transfer that has been previously notified to the Registrar; or (b) the prescribed information in relation to the shares held by each of the 50 members who hold the most number of shares".
   Read as written, either suffices.
   A drafter who meant both would have written "and"; this part follows the text and lists the other reading (F-j130-2).
3. **s 130AD(5): paragraph (c) sits after the sub-paragraphs of (b), and (b)(ii) ends "; and".**
   Lines 10956 to 10974: (b)(i) "...; and", (b)(ii) "...so apparently authorised; and", then "(c) a certification that purports to be authenticated by a person's signature or initials ... is deemed to be signed by the person unless it is shown that ...".
   The "and" after (b)(ii) reads as if (c) were a third limb of (b), but (c) is a deeming provision of its own about signatures; this part treats it as a separate paragraph (F-j130AD-2).
4. **Four offences state no penalty.**
   s 93(7) ("...shall be guilty of an offence."), s 123(4), s 144(1B) ("A company shall be guilty of an offence if default is made...") and s 144(2) end without a fine.
   Their penalty functions answer `NOTHING` (points outside the text); the neighbouring offences do state fines (s 93(9): $1,000 and a default penalty; ss 88(5) and 89: $5,000 and a further $500 a day for a continuing offence).
   Whether a general penalty fills the gap is not in the ranges.
5. **s 126(2) states no time.**
   "Where there has been a transfer of shares, a private company must lodge with the Registrar notice of that transfer of shares in the prescribed form." (lines 10615 to 10617).
   The same is true of the duties in ss 123(2), 125(1), 128(1), 128(3), 128(6), 130AA(1), 130AA(2), 130AA(5) and 130AC(2).
   Such a rule cannot be breached by the passing of time (section "Rules with no breach path").
6. **ss 128(3) and 130AA(2): the company chooses the period, within a range the text sets.**
   "within a stated period, being not less than 7 and not more than 28 days after the date of the notice".
   The text fixes the range, not the date; `s 128(3) the period stated in the notice is a period the subsection allows` tests a stated number of days against 7 to 28 and nothing else.
7. **ss 126(3) and 128(2) say the same thing twice.**
   Both: a transfer of a share in a private company on or after 3 January 2016 "does not take effect until the electronic register of members of the company is updated by the Registrar under section 196A(5)".
   s 126(3) speaks of "A transfer"; s 128(2) of "The transfer ... in a private company", inside the section on the transferor's request.
   Both are encoded as bars (`JUST TRUE` before the update, `JUST FALSE` after it, `NOTHING` before 3 January 2016), following the delegated-definitions ruling's item (d).
8. **Counting differs between ss 129(1), (2), 130AB(1) and ss 129(3), 130AB(2).**
   "within 30 days after the date on which the transfer was lodged" does not count the day of lodging (the keel's P1).
   "within 30 days beginning with the day on which the application was made" counts the day of the application as day 1 (the keel's P10).
   For an event on 1 February 2026, the first ends on 3 March and the second on 2 March (checked in the tests).
9. **s 130AE(2)(b): a private company's 30 days run from the notice lodged with the Registrar, not from the transfer lodged with the company.**
   Lines 10999 to 11001: "within 30 days after the date on which a notice of transfer of shares is lodged with the Registrar under section 126(2) or 128(1)(a)".
   For debentures, (c) runs from the lodging of the transfer with the company, as s 130AE(1) does for a public company.
10. **The s 93 seam is the branch register, not the principal register.**
    PLAN.md table A names s 93 as giving the "principal register".
    The text at line 1235 (inside s 4(1) "branch register", limb (b)) says "a branch register of holders of debentures kept pursuant to section 93", and the keel's input is named for that fact.
    This part answers it with `s 93(8) the register is a branch register of holders of debentures kept pursuant to section 93`.
11. **s 125(2)(a): "after the expiration of 14 days after the publication" is easy to count wrongly.**
    Published on 1 January 2026, the 14 days are 2 to 15 January and expire at the end of 15 January, so 16 January is the first day "after the expiration".
    The author of the test first wrote 15 January as the first such day; the run failed on it, and the expected value was re-derived from the text (15 January is `JUST FALSE`, 16 January `JUST TRUE`), not copied from the output.
    The same boundary is tested for s 130AD(3), where a transfer on the last day of the period is not "after the expiration".
12. **s 130(1) says "this subsection"; ss 126(1) and 127 say "this section".**
    The carve-out ("does not affect any power to register ... any person to whom the right ... has been transmitted by operation of law") is therefore tied to the subsection in the public company's rule and to the section in the private company's.
    No outcome differs; the three functions have the same shape.
13. **s 81(4): "voting shares" excludes treasury shares only "in this section and section 83".**
    Line 9958.
    This part encodes the exclusion as stated and does not extend it to any other section: `s 81(4) the share is a voting share for the purposes of section 81 and section 83` is `JUST FALSE` for a treasury share and `NOTHING` for any other share.
14. **s 79(3) and s 79(4) reach outside this part.**
    s 79(3) deems an interest in stock to be an interest in an issued share; s 79(4) widens "body corporate" in s 4(1)'s definition of "voting share" to include a body referred to in subsection (2)(c).
    Both are encoded as stated; the keel's `s 4(1) "voting share"` is not changed (no part may edit the keel).

## What the text does not answer (sgj)

- The penalty for the offences in ss 93(7), 123(4), 144(1B) and 144(2) (finding 4).
- When a duty with no time stated (ss 123(2), 125(1), 126(2), 128(1), 128(3), 128(6), 130AA(1), (2), (5), 130AC(2)) must be done (finding 5).
- Which bodies are "companies" for Division 4 when the Minister has declared none (F-j79-1).
- Whether a person with no substantial shareholding is not a substantial shareholder (F-j81-1).
- What is a "reasonable time" in s 93(7) beyond the one-month cap; a plain input is asked.
- Whether a "may" that fails its "where" or "upon" gate means "may not" (the nine split sites of type (ii)).
- What happens to a transfer on or after 3 January 2016 that the Registrar has not yet entered: the text bars it from taking effect and says nothing more.
- Anything the text hands to regulations or the Minister: "prescribed information" (ss 83(2)(c), 130(3)(b)), the prescribed form of notices, the terms of an exemption (s 80(3)); these are plain inputs.
- The meaning of "apparently authorised" (s 130AD(5)) and "just" or "fit" (the Court's discretion in ss 91, 128(5), 130AA(4)): taken as plain facts.

## What the stable binary does not accept

Hit while writing this part (each was a parse error or a "not found", so each is loud):

- `WAIT UNTIL` (two words) is not found; the stable spelling is `WAITUNTIL`.
- `a NOT EQUALS b` is a parse error; write `NOT (a EQUALS b)`.

Listed by the brief as not accepted or easy to get wrong, and avoided here:

- `NOT a AND b` parses as `NOT (a AND b)` and gives a wrong answer without an error (silent); every `NOT` here is parenthesised.
- A continuation line inside an `#ASSERT` is rejected; every assertion is on one line.
- `REFUSE`, `#ASSERT REFUSED` and `BECAUSE` (outside `LEST BREACH ... BECAUSE`) are not used; a case outside the encoding returns `NOTHING` and is asserted.
- A year-first `YMD` is not defined here; dates are written `Date day month year`.
- `TYPICALLY` on a record field is not used.

Not a binary limit but a source-locator rule that cost several rebuilds: `srcrefs.py --strict` requires an `@ref` to lie inside the nearest quote run above it, so a second `@ref` that cites lines outside the run above needs its own quote lines (`@@QR` in the sources, not `@@REF`).
The silent failures (exit code 0, a wrong or an unseen result), as against the loud ones above, are two: a `#TRACE` that cannot fail (the `check.sh` counts do not see trace outcomes: each trace carries a `-- EXPECT` word and `work/traces.py` compares it on both builds), and a seat case equal to its own wiring (the mutations below).

## Verification

**What check.sh prints.**
The full output of the last run is below.
It was run from this folder with `L4=<L4_BIN>` and `L4_MAIN` set to the 1.6.109 build, target `main` (the default), after the last change to any `.l4` file.
There is no earlier `check.sh` baseline for this part: the keel's modules print `0 0 0 0` on both builds in the same run, and the modules of this part are new, so there is nothing that these numbers replace.

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
sgj-cases-seat.l4                              0       150       0        0         0 |      0       150       0        0  same
sgj-div4-substantial-shareholdings.l4          0         0       0        0         0 |      0         0       0        0  same
sgj-div5-debentures.l4                         0         0       0        0         0 |      0         0       0        0  same
sgj-div7-private-transfers.l4                  0         0       0        0         0 |      0         0       0        0  same
sgj-div7-public-transfers.l4                   0         0       0        0         0 |      0         0       0        0  same
sgj-div7-title.l4                              0         0       0        0         0 |      0         0       0        0  same
sgj-part5-office-name.l4                       0         0       0        0         0 |      0         0       0        0  same
sgj-seat.l4                                    0         0       0        0         0 |      0         0       0        0  same
sgj-tests-div4-substantial-shareholdings.l4       0       223       0        0         0 |      0       223       0        0  same
sgj-tests-div5-debentures.l4                   0        98       0        0         0 |      0        98       0        0  same
sgj-tests-div7-private-transfers.l4            0        70       0        0         0 |      0        70       0        0  same
sgj-tests-div7-public-transfers.l4             0       151       0        0         0 |      0       151       0        0  same
sgj-tests-div7-title.l4                        0        71       0        0         0 |      0        71       0        0  same
sgj-tests-part5-office-name.l4                 0        67       0        0         0 |      0        67       0        0  same
TOTAL (22 modules)                             0       830       0        0           |      0       830       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

**Traces.**
`check.sh` does not see a `#TRACE` outcome.
Every trace has a `-- EXPECT FULFILLED|BREACH|RESIDUAL` word, written from the text, and `work/traces.py` compared it with the outcome on 1.6.110 and 1.6.109.
```
ok   sgj-tests-div4-substantial-shareholdings.l4:136 expect=FULFILLED main110=FULFILLED main109=FULFILLED
ok   sgj-tests-div4-substantial-shareholdings.l4:140 expect=BREACH main110=BREACH main109=BREACH
ok   sgj-tests-div4-substantial-shareholdings.l4:144 expect=BREACH main110=BREACH main109=BREACH
ok   sgj-tests-div4-substantial-shareholdings.l4:148 expect=RESIDUAL main110=RESIDUAL main109=RESIDUAL
ok   sgj-tests-div4-substantial-shareholdings.l4:180 expect=FULFILLED main110=FULFILLED main109=FULFILLED
ok   sgj-tests-div4-substantial-shareholdings.l4:184 expect=BREACH main110=BREACH main109=BREACH
ok   sgj-tests-div4-substantial-shareholdings.l4:188 expect=BREACH main110=BREACH main109=BREACH
ok   sgj-tests-div4-substantial-shareholdings.l4:204 expect=FULFILLED main110=FULFILLED main109=FULFILLED
ok   sgj-tests-div4-substantial-shareholdings.l4:208 expect=BREACH main110=BREACH main109=BREACH
ok   sgj-tests-div4-substantial-shareholdings.l4:253 expect=FULFILLED main110=FULFILLED main109=FULFILLED
ok   sgj-tests-div4-substantial-shareholdings.l4:257 expect=BREACH main110=BREACH main109=BREACH
ok   sgj-tests-div4-substantial-shareholdings.l4:316 expect=FULFILLED main110=FULFILLED main109=FULFILLED
ok   sgj-tests-div4-substantial-shareholdings.l4:320 expect=BREACH main110=BREACH main109=BREACH
ok   sgj-tests-div4-substantial-shareholdings.l4:324 expect=FULFILLED main110=FULFILLED main109=FULFILLED
ok   sgj-tests-div4-substantial-shareholdings.l4:328 expect=BREACH main110=BREACH main109=BREACH
ok   sgj-tests-div4-substantial-shareholdings.l4:333 expect=FULFILLED main110=FULFILLED main109=FULFILLED
ok   sgj-tests-div4-substantial-shareholdings.l4:337 expect=BREACH main110=BREACH main109=BREACH
ok   sgj-tests-div4-substantial-shareholdings.l4:341 expect=FULFILLED main110=FULFILLED main109=FULFILLED
ok   sgj-tests-div4-substantial-shareholdings.l4:345 expect=BREACH main110=BREACH main109=BREACH
ok   sgj-tests-div4-substantial-shareholdings.l4:416 expect=FULFILLED main110=FULFILLED main109=FULFILLED
ok   sgj-tests-div4-substantial-shareholdings.l4:420 expect=RESIDUAL main110=RESIDUAL main109=RESIDUAL
ok   sgj-tests-div4-substantial-shareholdings.l4:425 expect=BREACH main110=BREACH main109=BREACH
ok   sgj-tests-div4-substantial-shareholdings.l4:429 expect=RESIDUAL main110=RESIDUAL main109=RESIDUAL
ok   sgj-tests-div5-debentures.l4:20 expect=FULFILLED main110=FULFILLED main109=FULFILLED
ok   sgj-tests-div5-debentures.l4:24 expect=RESIDUAL main110=RESIDUAL main109=RESIDUAL
ok   sgj-tests-div5-debentures.l4:34 expect=FULFILLED main110=FULFILLED main109=FULFILLED
ok   sgj-tests-div5-debentures.l4:38 expect=BREACH main110=BREACH main109=BREACH
ok   sgj-tests-div5-debentures.l4:42 expect=BREACH main110=BREACH main109=BREACH
ok   sgj-tests-div5-debentures.l4:61 expect=FULFILLED main110=FULFILLED main109=FULFILLED
ok   sgj-tests-div5-debentures.l4:65 expect=RESIDUAL main110=RESIDUAL main109=RESIDUAL
ok   sgj-tests-div5-debentures.l4:89 expect=FULFILLED main110=FULFILLED main109=FULFILLED
ok   sgj-tests-div5-debentures.l4:93 expect=BREACH main110=BREACH main109=BREACH
ok   sgj-tests-div7-private-transfers.l4:24 expect=BREACH main110=BREACH main109=BREACH
ok   sgj-tests-div7-private-transfers.l4:28 expect=RESIDUAL main110=RESIDUAL main109=RESIDUAL
ok   sgj-tests-div7-private-transfers.l4:40 expect=RESIDUAL main110=RESIDUAL main109=RESIDUAL
ok   sgj-tests-div7-private-transfers.l4:44 expect=FULFILLED main110=FULFILLED main109=FULFILLED
ok   sgj-tests-div7-private-transfers.l4:68 expect=BREACH main110=BREACH main109=BREACH
ok   sgj-tests-div7-private-transfers.l4:72 expect=RESIDUAL main110=RESIDUAL main109=RESIDUAL
ok   sgj-tests-div7-private-transfers.l4:86 expect=RESIDUAL main110=RESIDUAL main109=RESIDUAL
ok   sgj-tests-div7-private-transfers.l4:90 expect=FULFILLED main110=FULFILLED main109=FULFILLED
ok   sgj-tests-div7-private-transfers.l4:94 expect=RESIDUAL main110=RESIDUAL main109=RESIDUAL
ok   sgj-tests-div7-private-transfers.l4:98 expect=FULFILLED main110=FULFILLED main109=FULFILLED
ok   sgj-tests-div7-private-transfers.l4:121 expect=RESIDUAL main110=RESIDUAL main109=RESIDUAL
ok   sgj-tests-div7-private-transfers.l4:125 expect=FULFILLED main110=FULFILLED main109=FULFILLED
ok   sgj-tests-div7-private-transfers.l4:145 expect=RESIDUAL main110=RESIDUAL main109=RESIDUAL
ok   sgj-tests-div7-private-transfers.l4:149 expect=FULFILLED main110=FULFILLED main109=FULFILLED
ok   sgj-tests-div7-private-transfers.l4:162 expect=FULFILLED main110=FULFILLED main109=FULFILLED
ok   sgj-tests-div7-private-transfers.l4:166 expect=BREACH main110=BREACH main109=BREACH
ok   sgj-tests-div7-private-transfers.l4:170 expect=BREACH main110=BREACH main109=BREACH
ok   sgj-tests-div7-private-transfers.l4:178 expect=FULFILLED main110=FULFILLED main109=FULFILLED
ok   sgj-tests-div7-private-transfers.l4:182 expect=BREACH main110=BREACH main109=BREACH
ok   sgj-tests-div7-private-transfers.l4:186 expect=BREACH main110=BREACH main109=BREACH
ok   sgj-tests-div7-private-transfers.l4:205 expect=BREACH main110=BREACH main109=BREACH
ok   sgj-tests-div7-private-transfers.l4:209 expect=RESIDUAL main110=RESIDUAL main109=RESIDUAL
ok   sgj-tests-div7-private-transfers.l4:213 expect=RESIDUAL main110=RESIDUAL main109=RESIDUAL
ok   sgj-tests-div7-public-transfers.l4:20 expect=BREACH main110=BREACH main109=BREACH
ok   sgj-tests-div7-public-transfers.l4:24 expect=RESIDUAL main110=RESIDUAL main109=RESIDUAL
ok   sgj-tests-div7-public-transfers.l4:51 expect=RESIDUAL main110=RESIDUAL main109=RESIDUAL
ok   sgj-tests-div7-public-transfers.l4:55 expect=FULFILLED main110=FULFILLED main109=FULFILLED
ok   sgj-tests-div7-public-transfers.l4:68 expect=RESIDUAL main110=RESIDUAL main109=RESIDUAL
ok   sgj-tests-div7-public-transfers.l4:72 expect=FULFILLED main110=FULFILLED main109=FULFILLED
ok   sgj-tests-div7-public-transfers.l4:90 expect=RESIDUAL main110=RESIDUAL main109=RESIDUAL
ok   sgj-tests-div7-public-transfers.l4:94 expect=FULFILLED main110=FULFILLED main109=FULFILLED
ok   sgj-tests-div7-public-transfers.l4:105 expect=FULFILLED main110=FULFILLED main109=FULFILLED
ok   sgj-tests-div7-public-transfers.l4:109 expect=BREACH main110=BREACH main109=BREACH
ok   sgj-tests-div7-public-transfers.l4:113 expect=BREACH main110=BREACH main109=BREACH
ok   sgj-tests-div7-public-transfers.l4:127 expect=BREACH main110=BREACH main109=BREACH
ok   sgj-tests-div7-public-transfers.l4:131 expect=RESIDUAL main110=RESIDUAL main109=RESIDUAL
ok   sgj-tests-div7-public-transfers.l4:135 expect=RESIDUAL main110=RESIDUAL main109=RESIDUAL
ok   sgj-tests-div7-public-transfers.l4:157 expect=RESIDUAL main110=RESIDUAL main109=RESIDUAL
ok   sgj-tests-div7-public-transfers.l4:161 expect=FULFILLED main110=FULFILLED main109=FULFILLED
ok   sgj-tests-div7-public-transfers.l4:249 expect=FULFILLED main110=FULFILLED main109=FULFILLED
ok   sgj-tests-div7-public-transfers.l4:253 expect=BREACH main110=BREACH main109=BREACH
ok   sgj-tests-div7-public-transfers.l4:257 expect=BREACH main110=BREACH main109=BREACH
ok   sgj-tests-div7-public-transfers.l4:273 expect=FULFILLED main110=FULFILLED main109=FULFILLED
ok   sgj-tests-div7-public-transfers.l4:277 expect=BREACH main110=BREACH main109=BREACH
ok   sgj-tests-div7-public-transfers.l4:286 expect=FULFILLED main110=FULFILLED main109=FULFILLED
ok   sgj-tests-div7-public-transfers.l4:290 expect=BREACH main110=BREACH main109=BREACH
ok   sgj-tests-div7-public-transfers.l4:299 expect=FULFILLED main110=FULFILLED main109=FULFILLED
ok   sgj-tests-div7-public-transfers.l4:303 expect=BREACH main110=BREACH main109=BREACH
ok   sgj-tests-div7-public-transfers.l4:316 expect=FULFILLED main110=FULFILLED main109=FULFILLED
ok   sgj-tests-div7-public-transfers.l4:320 expect=BREACH main110=BREACH main109=BREACH
ok   sgj-tests-div7-title.l4:51 expect=RESIDUAL main110=RESIDUAL main109=RESIDUAL
ok   sgj-tests-div7-title.l4:55 expect=FULFILLED main110=FULFILLED main109=FULFILLED
ok   sgj-tests-div7-title.l4:92 expect=RESIDUAL main110=RESIDUAL main109=RESIDUAL
ok   sgj-tests-div7-title.l4:96 expect=FULFILLED main110=FULFILLED main109=FULFILLED
ok   sgj-tests-part5-office-name.l4:21 expect=FULFILLED main110=FULFILLED main109=FULFILLED
ok   sgj-tests-part5-office-name.l4:26 expect=BREACH main110=BREACH main109=BREACH
ok   sgj-tests-part5-office-name.l4:31 expect=BREACH main110=BREACH main109=BREACH
ok   sgj-tests-part5-office-name.l4:36 expect=RESIDUAL main110=RESIDUAL main109=RESIDUAL
ok   sgj-tests-part5-office-name.l4:40 expect=FULFILLED main110=FULFILLED main109=FULFILLED
ok   sgj-tests-part5-office-name.l4:80 expect=FULFILLED main110=FULFILLED main109=FULFILLED
ok   sgj-tests-part5-office-name.l4:84 expect=BREACH main110=BREACH main109=BREACH
ok   sgj-tests-part5-office-name.l4:88 expect=BREACH main110=BREACH main109=BREACH
ok   sgj-tests-part5-office-name.l4:92 expect=RESIDUAL main110=RESIDUAL main109=RESIDUAL
traces: 95, mismatches or missing: 0
```

**Source locators.**
`python3 -I srcrefs.py check --refs ../../../inputs/CoA1967.txt sgj-*.l4` and the same with `--strict`:

```
== plain
srcrefs check: 788 src: lines, 139 runs, 241 locators, 0 problems
exit 0
== strict
srcrefs check: 788 src: lines, 139 runs, 241 locators, 0 problems
exit 0
```

**Mutations (the harness can fail).**
Five single edits to copies of the modules were run against the tests, each in a scratch folder that was deleted:
(1) s 81(1)(b): `TIMES 5` changed to `TIMES 6`, 2 of 223 assertions failed;
(2) s 129(3): `period: the last day of a period beginning with` changed to `... after`, 2 of 70 failed;
(3) s 130AD(3): `AT LEAST 42` changed to `AT LEAST 41`, 1 of 151 failed;
(4) seat, s 88(5): "the person is the company" changed from FALSE to TRUE, 1 of 150 failed;
(5) seat, s 130AE(1): two date arguments swapped, 1 of 150 failed.
A sixth edit, replacing `s 83(1) the last day ...` with `s 84(2) the last day ...` in the seat, changed no result because both count 2 business days; it is an equivalent mutant, not a gap.

## The S1b ruling on failed gates (2026S1bC)

The Guide records this ruling at section 5, in the bullet that begins “Failed gates of the pure “may” functions”; it is copied here word for word, as the Guide asks of every ruling.

> - **Failed gates of the pure "may" functions of the two Singapore encodings: the split follows the background, not the holder's name (card S1b of the bench "Singapore Split Sites", option C as modified on the card; accepted by Meng).** Conditions as printed on the card: (1) It governs only the functions that stay Boolean after the protocol split, the pure gates (58 on the card's line); the type (i) sites, an unmet element of an offence, are unchanged. (2) A failed gate answers `JUST FALSE` where the function is a public body's power, a relief from an express bar or duty, or a gate the text closes (“so long as”, “only if”); it answers `NOTHING` where it states a company's or person's liberty, standard or privilege with no bar to relieve. (3) At the card's reading that changes 16 answers: 6 `NOTHING` to `JUST FALSE` at public bodies, and 10 `JUST FALSE` to `NOTHING` at liberties (C024, C046, C084, C115, C135, C138, C154, C155, C157, C159), each a fork line with the other reading and each borderline, because a relief and a liberty are a judgment. The 10 liberties that already answered `NOTHING` stay. (4) Applied one commit per part, each “assumed, not ruled” until the card was marked, flipping the branch each site's tag marks. (5) The difference between an express bar and silence stays in the code's `FALSE-kind` and `NOTHING-kind` comments and in NOTES, which is the provenance channel, and not in the truth value. (6) Recorded in this guide, with limit 3 of the grant ruling above replaced for the Singapore rows, and in the `NOTES.md` of the parts that carry limit 3 (the card's own wording; this paragraph is that record). (7) The ruling reaches the two Singapore encodings only. The UK (164 listed sites) and Israel stay on the Guide as it stands until Meng rules; until then the differential compares Singapore under C with the UK under limit 3. The sites the 16 answers belong to: the public-body powers that went from `NOTHING` to `JUST FALSE` are s 173F (C045), s 32(4) (C106), s 139(6) (F018), s 139(10) (F019), s 282AA(1) (F057), s 281(1) (F062); the liberties that went from `JUST FALSE` to `NOTHING` are s 145(1), s 202A(2), s 21(7), s 130(2), s 173J(3), s 179(2), s 387A(1), s 387B(1), s 387D, s 390(1). Meng's note, verbatim: “Suggest that the changed encodings, and future rules encoded under this ruling, be marked with a greppable string like 2026S1bC to show where this rule took effect. Then in future we can revisit and review the consequences of this rule on encodings that haven’t been done today.” Marked 2026-11-21T12:17:37.989Z (accept, option C, not blind), ruled 2026-11-21, so the commits that applied it are ruled and no longer “assumed, not ruled”. Reading of the note (assumed, not ruled): each function this ruling changed, and each function encoded later under it in these two encodings, carries the string `2026S1bC` in its `FALSE-kind` or `NOTHING-kind` comment, and on its `FORK` line where it has one, so that `grep -rn 2026S1bC` lists where the rule took effect and a later review can find its consequences. Bench: https://claude.ai/artifact/SYSny5zjFYHHcMFeNYi5RX

Sites of this part changed under it (2026S1bC): s 130(2), `s 130(2) the public company may lodge with the Registrar a notice of the transfer of shares in the prescribed form` (fork F-j130-1, `sgj-div7-public-transfers.l4:62`), from `JUST FALSE` to `NOTHING` for the failed "where" gate: the public company's own liberty with no bar to relieve. The scope branch of the same function (a company that is not public) answered `NOTHING` before and still does.
