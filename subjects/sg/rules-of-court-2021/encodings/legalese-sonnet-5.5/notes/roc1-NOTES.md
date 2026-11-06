# NOTES.md -- roc1: Rules of Court 2021 (Singapore), lines 137-727 (Orders 2 to 8)

Status header (rule 1, how each claim was verified).
- **The text.** The text encoded is a plain-text rendering made by a converter script from Singapore Statutes Online (`inputs/SOURCES.md`: "Deposited by a converter script; each text file is a plain-text rendering, not the official text"; its own caveat: "SSO reproduces an unofficial consolidation").
  It is not the official text, and nothing here is "verified against the official text".
  Every quotation in a `-- src:` line was copied from that file by a script (`work/gen.py`) and `srcrefs.py check --refs` and `--strict` report 0 problems for every layer-1 module and `roc1-duties.l4`.
- **Target.** Written and run on `l4-main-109` (1.6.109) with `JL4_LIBRARY_PATH` unset; `check.sh` runs every module a second time on `l4-main-108` (1.6.108) and compares the four counts.
- **What is measured and what is read.** The counts in this file (rows, assertions, comments) are printed by the scripts in `work/` at the time `NOTES.md` was generated; the readings (forks, jural kinds, marginal readings, findings) are mine, from the text, and are not ruled except where a bullet says "ruling".
- **What was not opened.** By my own record of this run, nothing under `commons`, `canon`, any other run's folder or `~/.claude/` was opened for the encoding (reported to the lead as `peeked: nothing`).

## Where this brief differs from PLAN.md (the brief governs)

1. **A stated period outside the period.** PLAN.md section 2 and difficulty 10 of section 7 answer `NOTHING` outside a period the text fixes ("`JUST TRUE` inside the period and `NOTHING` outside it, never `JUST FALSE`"); the brief's ruling of 2026-11-05, (a), answers `JUST FALSE`. The code follows the brief.
2. **Seat question names.** The brief says to begin "Under section N,"; this instrument has Orders and rules, so the questions begin "Under Order N, rule M," (the instrument's own numbering).
3. **Where the seam rules are.** The brief names "PLAN.md section 8" for seam inputs; the seam rules are in section 5 (section 8 is "What the keel left to the parts"), and section 5 is followed.
4. **Seam input names.** PLAN.md names an input `o N r M <what you ask of it>`; where the text cites a whole Division or Order and no single rule, the input is named for the fact asked (see Seams).
5. **A "where" or "when" or "upon" that fails.** PLAN.md section 2 does not say; the brief's ruling (b) and (c) says `JUST FALSE`, and the code follows it.

## Files

| file | what it holds | contents |
| --- | --- | --- |
| `roc1-order-2.l4` | Order 2, Overview: rules 1 to 15 | 73 `@ref`s |
| `roc1-order-3-time.l4` | Order 3, rules 3 and 4: how a period is counted, extension and shortening (seams S-T1, S-T1b, S-T2) | 18 `@ref`s |
| `roc1-order-3.l4` | Order 3, rules 1, 2 and 5 to 9: interpretation, non-compliance, applications, Forms, language, foreign documents, methods of hearing | 47 `@ref`s |
| `roc1-order-4.l4` | Order 4: parties, representation, estates, groups, solicitors on record | 76 `@ref`s |
| `roc1-order-5.l4` | Order 5: amicable resolution | 18 `@ref`s |
| `roc1-order-6.l4` | Order 6: commencing proceedings, the notice, the defence, the counterclaim, the affidavit | 87 `@ref`s |
| `roc1-order-7.l4` | Order 7: service in Singapore (seam S-S1 is rule 8) | 20 `@ref`s |
| `roc1-order-8.l4` | Order 8: service out of Singapore, rules 1 to 8 including 4A | 60 `@ref`s |
| `roc1-duties.l4` | the duties the text puts on a named party, as `PARTY ... MUST/SHANT ... WITHIN ... HENCE ... LEST`, run with `#TRACE` | 17 `@ref`s, 56 `#TRACE`s |
| `roc1-seat.l4` | layer 2: the seat of a party to a civil action (claimant, defendant, third party, appellant) | 83 `@export` questions |
| `roc1-tests-order-2.l4` | tests for Order 2 | 203 `#ASSERT`s |
| `roc1-tests-order-3-time.l4` | tests for the counting engine | 83 `#ASSERT`s |
| `roc1-tests-order-3.l4` | tests for Order 3 | 129 `#ASSERT`s |
| `roc1-tests-order-4.l4` | tests for Order 4 | 308 `#ASSERT`s |
| `roc1-tests-order-5.l4` | tests for Order 5 | 53 `#ASSERT`s |
| `roc1-tests-order-6.l4` | tests for Order 6 | 223 `#ASSERT`s |
| `roc1-tests-order-7.l4` | tests for Order 7 | 88 `#ASSERT`s |
| `roc1-tests-order-8.l4` | tests for Order 8 | 218 `#ASSERT`s |
| `roc1-cases-seat.l4` | cases for the seat: every question has at least two (checked by script) | 218 `#ASSERT`s |
| `NOTES.md`, `PROGRESS.md` | this file; the working log | |

Assertions written across the test and cases files: 1523.
The other files in the folder (`roc-core.l4`, `roc-definitions.l4`, `check.sh`, `fetch-main-l4.sh`, `srcrefs.py`) are the keel's and the supplied tools, not edited.

## About the seat (assumed, not ruled)

- The seat is a party to a civil action (claimant, defendant, third party, appellant); there is no seat for an official.
- The helper definitions that wire plain answers into the modules' inputs carry the prefix `Under Orders 2 to 8, ...` (for example `Under Orders 2 to 8, my answer`, `Under Orders 2 to 8, the public holidays I give`).
  That prefix is a convention of mine, not a provision label and not the brief's; it cannot clash with another part's names, and every question and helper in `roc1-seat.l4` carries it or "Under Order N, rule M,".
- The seat asks the public holidays that fall in or near a period as two dates (1 January 1900 for "none"), because the Rules keep no list of holidays.
- A DATE or NUMBER question has its yes/no twin beside it where layer 1 has one: the late filing fee and "may the Court impose it"; the interest and "may the Court direct it"; the last day, the first day and "can the Rules count this period"; the day of deemed service and "does this Rule deem it".
  The validity months and last day of an originating claim (O 6 r 3(1)) and the deemed address (O 4 r 8(8)) are asked without a twin question in the seat.

## Contents

Coverage (roc1); Fork register (roc1); Jural relations (roc1); Marginal readings for a lawyer (roc1); Reading a result: FALSE and NOTHING (roc1); Seams (roc1); Dependencies; Unstable dialect; What the text turns out to say; What the main binary does not accept; Checks (`check.sh` output).

## Coverage (roc1)

Status header (verification): built by `work/cov.py` and `work/covtable.py` from the text itself (lines 137-727 of `SCJA1969-S914-2021.txt`) and the `@ref` labels of the shipped modules; every one of the 591 lines of the range, none of them blank, falls in at least one row (checked by the script).
A row's disposition is `encoded` when an `@ref` label equal to the row, above it (a subrule that carries its paragraphs) or below it (the rule that carries the lead-in) names an L4 definition; `fork` when the row is one the fork register holds; `inert` otherwise, with the reason number.
Reasons for `inert`: 1 not operative; 2 machinery; 3 repealed or blank.

A row's L4 name is the first definition its label annotates, with `(+n more)` for the others; the full lists are in the `@ref` lines of the modules.

**Summary.** 510 rows: 349 encoded, 82 fork, 79 inert, 0 repealed or blank, 0 unresolved.
Inert rows: 77 headings (7 Order titles, 3 Division headings, 67 rule headings), reason 1; `O 2 r 1(1)`, reason 1 (the purpose paragraph: "This Order provides an overview"); `O 2 r 15`, reason 1 (it announces a flowchart that the text does not contain and creates no rule; the gap is stated in the row). One encoded row carries a stated gap in its L4-name cell: `O 6 r 9(3)` (no interest rate for a default judgment on a counterclaim). No row is inert for reason 2 or 3: the range holds no commencement, extent, rule-making power, savings or transitional provision, and no provision shown repealed or blank.
Fork rows by entry: F1 1; F2 1; F3 1; F4 2; F5 5; F6 27; F7 1; F8 12; F9 1; F10 2; F11 1; F12 1; F13 18; F14 3; F15 2; F16 4.

**Audit.** The units were counted a second time by a different method (regular expressions over the whole range joined, not the line-by-line parser) and compared with the rows by kind:

| kind | independent count | rows |
| --- | --- | --- |
| order headings | 7 | 7 |
| division headings | 3 | 3 |
| rule headings | 67 | 67 |
| subrules (rule-opening (1) plus every other (n)) | 243 | 242 (+1 merged into the “month” row) |
| rules with a body and no subrule | 15 | 15 |
| paragraphs ( a ) | 137 | 137 |
| sub-paragraphs (i) | 22 | 22 |
| items (A) | 2 | 2 |
| defined terms | 15 | 15 |
| total | 511 | 510 (+1 merged) = 511 |

Rows before and after: the first run of the script made 510 rows; the audit found one defined term missing (“officer” in O 4 r 3(6), which the text introduces with a dash and no "means"), so the script was fixed (511); the pair "(2) The word" and “month” in O 3 r 3(2), which the script had split in two, was then merged into one row (510).
The independent count is 511 units; the table has 510 rows because that one pair is a single row. Provisions added after the first plan (O 2 r 6(6), r 7(2), r 9(5), r 9(6), r 11(2), r 11(3); O 8 r 6(7)) were first planned as inert and are encoded; the table above is from the final state.

| lines | provision | text (first words, mechanical) | disposition | L4 name |
| --- | --- | --- | --- | --- |
| 137-138 | O 2 [heading] | ORDER 2 OVERVIEW | inert, reason 1 | heading: not operative |
| 139 | O 2 r 1 [heading] | Purpose of this Order (O. 2, r. 1) | inert, reason 1 | heading: not operative |
| 140 | O 2 r 1(1) | 1. —(1) This Order provides an overview of an action commenced under Par... | inert, reason 1 | purpose: “This Order provides an overview” creates no rule |
| 140 | O 2 r 1(2) | (2) An action does not need to proceed in precisely the same way as set ... | encoded | `o 2 r 1(2) an action needs to proceed in precisely the same way as set out in this Order` |
| 141 | O 2 r 2 [heading] | Role of Court and parties (O. 2, r. 2) | inert, reason 1 | heading: not operative |
| 142 | O 2 r 2(1) | 2. —(1) When an action is commenced under these Rules, the Court will co... | encoded | `o 2 r 2(1) the Court will conduct proceedings in a manner that will bring the action to a conclusion in keeping with the Ideals` |
| 142 | O 2 r 2(2) | (2) All parties are to assist the Court and conduct their case in a mann... | encoded | `o 2 r 2(2) a party is to assist the Court and conduct the case in a manner that will bring about such a resolution` |
| 143 | O 2 r 3 [heading] | Commencement and service of action (O. 2, r. 3) | inert, reason 1 | heading: not operative |
| 144 | O 2 r 3(1) | 3. —(1) A claimant may commence an action under these Rules by filing an... | encoded | `o 2 r 3(1) a claimant may commence an action by filing that document` |
| 144 | O 2 r 3(2) | (2) The claimant has to take reasonable steps to serve the originating c... | encoded | `o 2 r 3(2) the claimant has to take reasonable steps to serve expeditiously` (+1 more) |
| 145 | O 2 r 4 [heading] | Notice of intention to contest or not contest claim (O. 2, r. 4) | inert, reason 1 | heading: not operative |
| 146 | O 2 r 4(1) | 4. —(1) A defendant who is served an originating claim with a statement ... | encoded | `o 2 r 4(1) the defendant has to file and serve a notice of intention to contest or not contest the claim` (+1 more) |
| 146 | O 2 r 4(2) | (2) If the defendant fails to file and serve such a notice or states in ... | encoded | `o 2 r 4(2) the claimant may apply for judgment in default` |
| 147 | O 2 r 5 [heading] | Defence or affidavit and challenge to jurisdiction (O. 2, r. 5) | inert, reason 1 | heading: not operative |
| 148 | O 2 r 5(1) | 5. —(1) A defendant who wishes to contest an originating claim or an ori... | encoded | `o 2 r 5(1) the defendant has to file and serve a defence or an affidavit` |
| 148 | O 2 r 5(2) | (2) If the defendant is challenging the jurisdiction of the Court on the... | encoded | `o 2 r 5(2) the defendant need not file and serve a defence or affidavit on the merits` (+1 more) |
| 149 | O 2 r 5(3) | (3) The challenge to jurisdiction may be for the reasons that the Court ... | encoded | `o 2 r 5(3) the challenge to jurisdiction may be for that reason` |
| 149-150 | O 2 r 5(3)(a) | ( a ) has no jurisdiction to hear the action; or | encoded | `o 2 r 5(3) the challenge to jurisdiction may be for that reason` |
| 151-152 | O 2 r 5(3)(b) | ( b ) should not exercise jurisdiction to hear the action. | encoded | `o 2 r 5(3) the challenge to jurisdiction may be for that reason` |
| 153 | O 2 r 5(4) | (4) A defendant who is challenging the jurisdiction of the Court has to ... | encoded | `o 2 r 5(4) the defendant has to state the challenge in the defence or affidavit` (+1 more) |
| 154 | O 2 r 6 [heading] | Case conference (O. 2, r. 6) | inert, reason 1 | heading: not operative |
| 155 | O 2 r 6(1) | 6. —(1) A case conference will be fixed after an originating claim or an... | encoded | `o 2 r 6(1) a case conference will be fixed` |
| 155 | O 2 r 6(2) | (2) If no party attends the case conference or if the claimant is absent... | encoded | `o 2 r 6(2) the Court may dismiss the action` |
| 156 | O 2 r 6(3) | (3) If the claimant attends the case conference but has not served the c... | encoded | `o 2 r 6(3)(a) the Court may dismiss the action` (+1 more) |
| 156-157 | O 2 r 6(3)(a) | ( a ) may dismiss the action if it is not satisfied that the claimant ha... | encoded | `o 2 r 6(3)(a) the Court may dismiss the action` |
| 158-159 | O 2 r 6(3)(b) | ( b ) may order the claimant to serve the action or to apply for substit... | encoded | `o 2 r 6(3)(b) the Court may order the claimant to serve the action or to apply for substituted service, and fix another case conference` |
| 160 | O 2 r 6(4) | (4) If the claimant attends the case conference but the defendant is abs... | encoded | `o 2 r 6(4) the Court may give judgment for the claimant` |
| 161 | O 2 r 6(5) | (5) If both the claimant and defendant attend the case conference but th... | encoded | `o 2 r 6(5) the Court may take that step` |
| 162 | O 2 r 6(6) | (6) The Court will consider whether there is scope for the parties to re... | encoded | `o 2 r 6(6) the Court will consider whether there is scope for the parties to resolve their dispute other than by litigation` |
| 163 | O 2 r 6(7) | (7) If the defendant is challenging the jurisdiction of the Court, the C... | encoded | `o 2 r 6(7) the Court will direct the defendant to file and serve the necessary application with supporting affidavit` (+2 more) |
| 163-164 | O 2 r 6(7)(a) | ( a ) direct the defendant to file and serve the necessary application w... | encoded | `o 2 r 6(7) the Court will direct the defendant to file and serve the necessary application with supporting affidavit` (+2 more) |
| 165-166 | O 2 r 6(7)(b) | ( b ) direct the claimant to file and serve any affidavit in reply, with... | fork F13 | `o 2 r 6(7)(b) the Court will direct the claimant to file and serve any affidavit in reply` |
| 167-168 | O 2 r 6(7)(c) | ( c ) fix the application for hearing after all affidavits have been fil... | encoded | `o 2 r 6(7) the Court will direct the defendant to file and serve the necessary application with supporting affidavit` (+2 more) |
| 169 | O 2 r 7 [heading] | Directions for defence or affidavit on merits (O. 2, r. 7) | inert, reason 1 | heading: not operative |
| 170 | O 2 r 7(1) | 7. —(1) If the defendant challenges the jurisdiction of the Court and fa... | encoded | `o 2 r 7(1) the Court will give directions to the defendant to file the defence or affidavit on the merits` |
| 170 | O 2 r 7(2) | (2) Where there is no challenge to the jurisdiction of the Court, the Co... | encoded | `o 2 r 7(2) the Court will consider all matters necessary to bring the proceedings to a conclusion in accordance with the Ideals` |
| 171 | O 2 r 8 [heading] | Affidavits of evidence‑in‑chief (O. 2, r. 8) | inert, reason 1 | heading: not operative |
| 172 | O 2 r 8 | 8. The Court may order the parties to file and exchange affidavits of ev... | encoded | `o 2 r 8 the Court may order the parties to file and exchange affidavits of evidence-in-chief` |
| 173 | O 2 r 9 [heading] | Applications in pending proceedings (O. 2, r. 9) | inert, reason 1 | heading: not operative |
| 174 | O 2 r 9(1) | 9. —(1) Where the Court does not make any order described in Rule 8, or ... | encoded | `o 2 r 9(1) the Court will give the necessary directions in respect of that matter` |
| 174-175 | O 2 r 9(1)(a) | ( a ) addition or removal of parties; | encoded | `o 2 r 9(1) the Court will give the necessary directions in respect of that matter` |
| 176-177 | O 2 r 9(1)(b) | ( b ) consolidation of actions; | encoded | `o 2 r 9(1) the Court will give the necessary directions in respect of that matter` |
| 178-179 | O 2 r 9(1)(c) | ( c ) division of issues at trial to be heard separately; | encoded | `o 2 r 9(1) the Court will give the necessary directions in respect of that matter` |
| 180-181 | O 2 r 9(1)(d) | ( d ) security for costs; | encoded | `o 2 r 9(1) the Court will give the necessary directions in respect of that matter` |
| 182-183 | O 2 r 9(1)(e) | ( e ) further and better particulars of pleadings; | encoded | `o 2 r 9(1) the Court will give the necessary directions in respect of that matter` |
| 184-185 | O 2 r 9(1)(f) | ( f ) amendment of pleadings; | encoded | `o 2 r 9(1) the Court will give the necessary directions in respect of that matter` |
| 186-187 | O 2 r 9(1)(g) | ( g ) filing of further pleadings; | encoded | `o 2 r 9(1) the Court will give the necessary directions in respect of that matter` |
| 188-189 | O 2 r 9(1)(h) | ( h ) striking out of part of an action or of the defence; | encoded | `o 2 r 9(1) the Court will give the necessary directions in respect of that matter` |
| 190-191 | O 2 r 9(1)(i) | ( i ) judgment on admission of facts; | encoded | `o 2 r 9(1) the Court will give the necessary directions in respect of that matter` |
| 192-193 | O 2 r 9(1)(j) | ( j ) determination of questions of law or construction of documents; | encoded | `o 2 r 9(1) the Court will give the necessary directions in respect of that matter` |
| 194-195 | O 2 r 9(1)(k) | ( k ) production of documents; | encoded | `o 2 r 9(1) the Court will give the necessary directions in respect of that matter` |
| 196-197 | O 2 r 9(1)(l) | ( l ) interim relief; | encoded | `o 2 r 9(1) the Court will give the necessary directions in respect of that matter` |
| 198-199 | O 2 r 9(1)(m) | ( m ) expert evidence and assessors; | encoded | `o 2 r 9(1) the Court will give the necessary directions in respect of that matter` |
| 200-201 | O 2 r 9(1)(n) | ( n ) independent witness and interested non‑parties; | encoded | `o 2 r 9(1) the Court will give the necessary directions in respect of that matter` |
| 202-203 | O 2 r 9(1)(o) | ( o ) independent counsel. | encoded | `o 2 r 9(1) the Court will give the necessary directions in respect of that matter` |
| 204 | O 2 r 9(2) | (2) If further pleadings need to be filed, the Court will order such ple... | encoded | `o 2 r 9(2) the Court will order such pleadings to be filed and served` |
| 205 | O 2 r 9(3) | (3) Pleadings after the defence or the defence to counterclaim cannot be... | fork F13 | `o 2 r 9(3) a pleading after the defence or the defence to counterclaim can be filed` |
| 206 | O 2 r 9(4) | (4) Further affidavits cannot be filed for an originating application wi... | fork F13 | `o 2 r 9(4) a further affidavit can be filed` |
| 207 | O 2 r 9(5) | (5) As far as possible, the Court will order each party to file a single... | encoded | `o 2 r 9(5) the Court will order each party to file a single application pending trial for all the matters stated in paragraph (1)` |
| 208 | O 2 r 9(6) | (6) The Court will direct the party applying to file and serve an affida... | encoded | `o 2 r 9(6) the Court will direct the party applying to file and serve an affidavit in support and the other party to file and serve an affidavit in reply` |
| 209 | O 2 r 9(7) | (7) The application will be heard after all affidavits have been filed a... | encoded | `o 2 r 9(7) the application cannot yet be heard` |
| 210 | O 2 r 9(8) | (8) No other application may be taken out by any party at any time excep... | fork F13 | `o 2 r 9(8) the application may be taken out` |
| 210-211 | O 2 r 9(8)(a) | ( a ) an injunction or a search order which may include an application f... | encoded | `o 2 r 9(8) the application may be taken out` |
| 212-213 | O 2 r 9(8)(b) | ( b ) substituted service; | encoded | `o 2 r 9(8) the application may be taken out` |
| 214-215 | O 2 r 9(8)(c) | ( c ) service out of Singapore; | encoded | `o 2 r 9(8) the application may be taken out` |
| 216-217 | O 2 r 9(8)(d) | ( d ) setting aside service of an originating process; | encoded | `o 2 r 9(8) the application may be taken out` |
| 218-219 | O 2 r 9(8)(e) | ( e ) judgment in default of a notice of intention to contest or not con... | encoded | `o 2 r 9(8) the application may be taken out` |
| 220-221 | O 2 r 9(8)(f) | ( f ) judgment in default of defence; | encoded | `o 2 r 9(8) the application may be taken out` |
| 222-223 | O 2 r 9(8)(g) | ( g ) summary judgment; | encoded | `o 2 r 9(8) the application may be taken out` |
| 224-225 | O 2 r 9(8)(h) | ( h ) striking out the whole of an action or defence; | encoded | `o 2 r 9(8) the application may be taken out` |
| 226-227 | O 2 r 9(8)(i) | ( i ) stay of the whole action; | encoded | `o 2 r 9(8) the application may be taken out` |
| 228-229 | O 2 r 9(8)(j) | ( j ) stay of enforcement of a judgment or order; | encoded | `o 2 r 9(8) the application may be taken out` |
| 230-231 | O 2 r 9(8)(k) | ( k ) an enforcement order; | encoded | `o 2 r 9(8) the application may be taken out` |
| 232-233 | O 2 r 9(8)(l) | ( l ) permission to appeal; | encoded | `o 2 r 9(8) the application may be taken out` |
| 234-235 | O 2 r 9(8)(m) | ( m ) transfer of proceedings under the State Courts Act; | encoded | `o 2 r 9(8) the application may be taken out` |
| 236-237 | O 2 r 9(8)(n) | ( n ) setting aside third party proceedings; or | encoded | `o 2 r 9(8) the application may be taken out` |
| 238-239 | O 2 r 9(8)(o) | ( o ) permission to make an application for a committal order. | encoded | `o 2 r 9(8) the application may be taken out` |
| 240 | O 2 r 9(9) | (9) The Court’s approval to file further applications other than those d... | encoded | `o 2 r 9(9) the Court's approval has been sought as required` |
| 241 | O 2 r 9(10) | (10) Except in a special case and with the trial Judge’s approval, no ap... | fork F11 | `o 2 r 9(10) the period before the trial` (+2 more) |
| 242 | O 2 r 9(11) | (11) The trial Judge’s approval has to be sought by letter setting out t... | encoded | `o 2 r 9(11) the trial Judge's approval has been sought as required` |
| 243 | O 2 r 9(12) | (12) All applications to the Court have to be served on all other partie... | encoded | `o 2 r 9(12) the application has to be served on the other party` |
| 244 | O 2 r 10 [heading] | Appeals in applications (O. 2, r. 10) | inert, reason 1 | heading: not operative |
| 245 | O 2 r 10(1) | 10. —(1) Appeals against the Court’s decision made in an application may... | encoded | `o 2 r 10(1) an appeal against the Court's decision made in an application may be filed` |
| 245 | O 2 r 10(2) | (2) If any party appeals against the Court’s decision made in an applica... | encoded | `o 2 r 10(2) the matter will proceed on appeal before the appropriate appellate Court` |
| 246 | O 2 r 10(3) | (3) The appellant has to file and serve a notice of appeal on all partie... | encoded | `o 2 r 10(3) the appellant has to file and serve a notice of appeal on all parties who have an interest` |
| 247 | O 2 r 10(4) | (4) Where permission to appeal is required, the appellant has to apply t... | encoded | `o 2 r 10(4) the appellant has to apply for permission and serve the application on all parties who have an interest` |
| 248 | O 2 r 10(5) | (5) If the lower Court (where applicable) does not grant permission to a... | encoded | `o 2 r 10(5) the party may apply to the appropriate appellate Court for permission` |
| 249 | O 2 r 10(6) | (6) If permission to appeal is granted, the appellant has to file and se... | encoded | `o 2 r 10(6) the appellant has to file and serve a notice of appeal after permission is granted` |
| 250 | O 2 r 10(7) | (7) Save for appeals filed under Divisions 2 and 4 of Order 18, the appe... | encoded | `o 2 r 10(7) the appellant has to provide security for the costs of the appeal` (+1 more) |
| 251 | O 2 r 10(8) | (8) The appeal will proceed before the appropriate appellate Court by wa... | encoded | `o 2 r 10(8) the appeal will proceed by way of rehearing on the documents` |
| 252 | O 2 r 10(9) | (9) The parties have to file and serve on all parties who have an intere... | encoded | `o 2 r 10(9) the parties have to file and serve written submissions` |
| 253 | O 2 r 10(10) | (10) No document other than the parties’ written submissions (including ... | fork F13 | `o 2 r 10(10) the document may be filed in the appeal` |
| 254 | O 2 r 10(11) | (11) No further evidence may be admitted without the approval of the app... | fork F13 | `o 2 r 10(11) further evidence may be admitted` |
| 255 | O 2 r 11 [heading] | Directions for trial or hearing (O. 2, r. 11) | inert, reason 1 | heading: not operative |
| 256 | O 2 r 11(1) | 11. —(1) The Court will give directions for the trial or hearing, after ... | encoded | `o 2 r 11(1) the Court will give directions for the trial or hearing` |
| 256 | O 2 r 11(2) | (2) An action commenced by originating claim will generally be decided a... | encoded | `o 2 r 11(2) the action will generally be decided at a trial involving oral evidence and cross examination` |
| 257 | O 2 r 11(3) | (3) An action commenced by originating application will generally be dec... | encoded | `o 2 r 11(3) the action will generally be decided at a hearing based on affidavits` |
| 258 | O 2 r 12 [heading] | Appeals after trial or hearing (O. 2, r. 12) | inert, reason 1 | heading: not operative |
| 259 | O 2 r 12(1) | 12. —(1) Appeals against the Court’s decision after trial or after an or... | encoded | `o 2 r 12(1) an appeal against the Court's decision after trial or after an originating application is heard may be filed` |
| 259 | O 2 r 12(2) | (2) If any party appeals against the Court’s decision after trial or aft... | encoded | `o 2 r 12(2) the case will proceed on appeal before the appropriate appellate Court` |
| 260 | O 2 r 12(3) | (3) The appellant has to file and serve a notice of appeal on all partie... | encoded | `o 2 r 12(3) the appellant has to file and serve a notice of appeal on all parties who have an interest` |
| 261 | O 2 r 12(4) | (4) Where permission to appeal is required, the party who intends to app... | encoded | `o 2 r 12(4) the party who intends to appeal has to apply for permission and serve the application on all parties who have an interest` |
| 262 | O 2 r 12(5) | (5) If the lower Court (where applicable) does not grant permission to a... | encoded | `o 2 r 12(5) the party may apply to the appropriate appellate Court for permission` |
| 263 | O 2 r 12(6) | (6) That party has to serve the application for permission to appeal on ... | encoded | `o 2 r 12(6) the party has to serve the application for permission on all parties who have an interest` |
| 264 | O 2 r 12(7) | (7) If permission to appeal is granted, that party has to file and serve... | encoded | `o 2 r 12(7) the party has to file and serve a notice of appeal after permission is granted` |
| 265 | O 2 r 12(8) | (8) The appellant has to provide security for the costs of the appeal of... | encoded | `o 2 r 12(8) the appellant has to provide security for the costs of the appeal` (+1 more) |
| 266 | O 2 r 12(9) | (9) The appellant and the respondent have to file and serve the relevant... | encoded | `o 2 r 12(9) the appellant and the respondent have to file and serve the relevant appeal documents` |
| 267 | O 2 r 12(10) | (10) No further evidence may be admitted without the approval of the app... | fork F13 | `o 2 r 12(10) further evidence may be admitted` |
| 268 | O 2 r 13 [heading] | Costs (O. 2, r. 13) | inert, reason 1 | heading: not operative |
| 269 | O 2 r 13(1) | 13. —(1) Costs are in the discretion of the Court and the Court has the ... | encoded | `o 2 r 13(1) the Court has the power to determine the issue relating to costs` |
| 269 | O 2 r 13(2) | (2) The Court which heard a matter must fix the costs of the matter, unl... | encoded | `o 2 r 13(2) the Court which heard the matter must fix the costs of the matter` |
| 270 | O 2 r 13(3) | (3) In the cases to which fixed costs apply under these Rules, the amoun... | encoded | `o 2 r 13(3) the amount of costs allowed is as set out in these Rules` |
| 271 | O 2 r 14 [heading] | Enforcement (O. 2, r. 14) | inert, reason 1 | heading: not operative |
| 272 | O 2 r 14 | 14. To enforce a judgment, a party takes out a single application for on... | encoded | `o 2 r 14 the party takes out a single application for one or more methods of enforcement` |
| 273 | O 2 r 15 [heading] | Flowchart (O. 2, r. 15) | inert, reason 1 | heading: not operative |
| 274 | O 2 r 15 | 15. The following flowchart gives an overview of the progress of an acti... | inert, reason 1 | it introduces a flowchart (not in the text) and creates no rule; gap: the flowchart is announced and absent from the text, so there is no function |
| 275-276 | O 3 [heading] | ORDER 3 GENERAL MATTERS | inert, reason 1 | heading: not operative |
| 277 | O 3 r 1 [heading] | Ideals (O. 3, r. 1) | inert, reason 1 | heading: not operative |
| 278 | O 3 r 1(1) | 1. —(1) These Rules are to be given a purposive interpretation. | encoded | `o 3 r 1(1) the provision is to be given a purposive interpretation` |
| 278 | O 3 r 1(2) | (2) These Rules seek to achieve the following Ideals in civil procedure: | encoded | `o 3 r 1(2) the objective is one of the Ideals` (+2 more) |
| 278-279 | O 3 r 1(2)(a) | ( a ) fair access to justice; | encoded | `o 3 r 1(2) the objective is one of the Ideals` (+2 more) |
| 280-281 | O 3 r 1(2)(b) | ( b ) expeditious proceedings; | encoded | `o 3 r 1(2) the objective is one of the Ideals` (+2 more) |
| 282-283 | O 3 r 1(2)(c) | ( c ) cost‑effective work proportionate to — | encoded | `o 3 r 1(2) the objective is one of the Ideals` (+2 more) |
| 283-284 | O 3 r 1(2)(c)(i) | (i) the nature and importance of the action; | encoded | `o 3 r 1(2) the objective is one of the Ideals` (+2 more) |
| 285-286 | O 3 r 1(2)(c)(ii) | (ii) the complexity of the claim as well as the difficulty or novelty of... | encoded | `o 3 r 1(2) the objective is one of the Ideals` (+2 more) |
| 287-288 | O 3 r 1(2)(c)(iii) | (iii) the amount or value of the claim; | encoded | `o 3 r 1(2) the objective is one of the Ideals` (+2 more) |
| 289-290 | O 3 r 1(2)(d) | ( d ) efficient use of court resources; | encoded | `o 3 r 1(2) the objective is one of the Ideals` (+2 more) |
| 291-292 | O 3 r 1(2)(e) | ( e ) fair and practical results suited to the needs of the parties. | encoded | `o 3 r 1(2) the objective is one of the Ideals` (+2 more) |
| 293 | O 3 r 1(3) | (3) The Court must seek to achieve the Ideals in all its orders or direc... | encoded | `o 3 r 1(3) the Court must seek to achieve the Ideals in the decision` |
| 294 | O 3 r 1(4) | (4) All parties have the duty to assist the Court and to conduct their c... | encoded | `o 3 r 1(4) the person has the duty to assist the Court and conduct the case to help achieve the Ideals` (+1 more) |
| 295 | O 3 r 2 [heading] | General powers of Court (O. 3, r. 2) | inert, reason 1 | heading: not operative |
| 296 | O 3 r 2(1) | 2. —(1) Unless the context otherwise requires and subject to any other w... | encoded | `o 3 r 2(1) the requirement is subject to the Court's discretion to order otherwise` |
| 296 | O 3 r 2(2) | (2) Where there is no express provision in these Rules or any other writ... | encoded | `o 3 r 2(2) the Court may do what it considers necessary` |
| 297 | O 3 r 2(3) | (3) In exercising any power, the Court may impose any condition or give ... | encoded | `o 3 r 2(3) the Court may impose a condition or give a direction` |
| 298 | O 3 r 2(4) | (4) Where there is non‑compliance with these Rules, any other written la... | encoded | `o 3 r 2(4) the Court may exercise the powers in paragraph (4)` |
| 298-299 | O 3 r 2(4)(a) | ( a ) subject to paragraph (5), waive the non‑compliance of the Rule, wr... | encoded | `o 3 r 2(4)(a) the Court may waive the non-compliance` |
| 300-301 | O 3 r 2(4)(b) | ( b ) disallow or reject the filing or use of any document; | encoded | `o 3 r 2(4)(b) the Court may disallow or reject the filing or use of a document` |
| 302-303 | O 3 r 2(4)(c) | ( c ) refuse to hear any matter or dismiss it without a hearing; | encoded | `o 3 r 2(4)(c) the Court may refuse to hear a matter or dismiss it without a hearing` |
| 304-305 | O 3 r 2(4)(d) | ( d ) dismiss, stay or set aside any proceedings and give the appropriat... | encoded | `o 3 r 2(4)(d) the Court may dismiss, stay or set aside the proceedings` |
| 306-307 | O 3 r 2(4)(e) | ( e ) impose a late filing fee of $50 for each day that a document remai... | fork F3 | `o 3 r 2(4)(e) the Court may impose a late filing fee` (+2 more) |
| 308-309 | O 3 r 2(4)(f) | ( f ) make costs orders or any other orders that are appropriate. | encoded | `o 3 r 2(4)(f) the Court may make a costs order or any other order` |
| 310 | O 3 r 2(5) | (5) Where the non‑compliance is in respect of any written law other than... | encoded | `o 3 r 2(5) the Court may waive the non-compliance with a written law other than these Rules` |
| 311 | O 3 r 2(6) | (6) The powers of the Court under this Rule do not affect any other powe... | encoded | `o 3 r 2(6) the powers under this Rule affect another power of the Court under a written law` |
| 312 | O 3 r 2(7) | (7) The Court may give directions by letter or by electronic or other me... | encoded | `o 3 r 2(7) the Court may give directions by those means` |
| 313 | O 3 r 2(8) | (8) The Court may, on its own accord or upon application, if it is in th... | encoded | `o 3 r 2(8) the Court may revoke a judgment or order obtained or set aside what was done` |
| 313-314 | O 3 r 2(8)(a) | ( a ) without notice to, or in the absence of, the party affected; | encoded | `o 3 r 2(8) the Court may revoke a judgment or order obtained or set aside what was done` |
| 315-316 | O 3 r 2(8)(b) | ( b ) without complying with these Rules or any order of Court; | encoded | `o 3 r 2(8) the Court may revoke a judgment or order obtained or set aside what was done` |
| 317-318 | O 3 r 2(8)(c) | ( c ) contrary to any written law; or | encoded | `o 3 r 2(8) the Court may revoke a judgment or order obtained or set aside what was done` |
| 319-320 | O 3 r 2(8)(d) | ( d ) by fraud or misrepresentation. | encoded | `o 3 r 2(8) the Court may revoke a judgment or order obtained or set aside what was done` |
| 321 | O 3 r 2(9) | (9) An application under paragraph (8) may be made by or on behalf of th... | encoded | `o 3 r 2(9) the application under paragraph (8) may be made by the applicant` |
| 322 | O 3 r 2(10) | (10) An application under paragraph (8) must be taken out within 14 days... | encoded | `o 3 r 2(10) the period for the application under paragraph (8)` (+1 more) |
| 323 | O 3 r 3 [heading] | Calculation of time (O. 3, r. 3) | inert, reason 1 | heading: not operative |
| 324 | O 3 r 3(1) | 3. —(1) The Interpretation Act does not apply to the calculation of time... | encoded | `o 3 r 3(1) the Interpretation Act applies to the calculation of time in these Rules` |
| 324 | O 3 r 3(2) “month” | (2) The word “month” means a calendar month unless the context otherwise... | encoded | `o 3 r 3(2) the word month is read as a calendar month` (+1 more) |
| 325 | O 3 r 3(3) | (3) Where an act is required to be done within a specified period after ... | encoded | `o 3 r 3(2) a period of calendar months from a date ends on the corresponding day` (+6 more) |
| 326 | O 3 r 3(4) | (4) Where an act is required to be done within or not less than a specif... | encoded | `o 3 r 3(6) the day reached by counting court days` (+3 more) |
| 327 | O 3 r 3(5) | (5) Where an act is required to be done a specified number of clear days... | fork F2 | `o 3 r 3 the last day for doing the act` (+1 more) |
| 328 | O 3 r 3(6) | (6) If the period in question is 6 days or less, any day that is a non‑c... | encoded | `o 3 r 3(6) the day is a non-court day to be left out` (+3 more) |
| 329 | O 3 r 3(7) | (7) Where the time prescribed by these Rules, or by any judgment, order ... | fork F1 | `o 3 r 3(7) the last day moved past non-court days` (+1 more) |
| 330 | O 3 r 4 [heading] | Extension or shortening of time (O. 3, r. 4) | inert, reason 1 | heading: not operative |
| 331 | O 3 r 4(1) | 4. —(1) The Court may extend or shorten the period within which a person... | encoded | `o 3 r 4(1) the Court may extend or shorten the period` |
| 331 | O 3 r 4(2) | (2) Unless these Rules otherwise provide, the Court may extend the perio... | encoded | `o 3 r 4(2) the Court may extend the period whether the application is made before or after it expires` |
| 332 | O 3 r 4(3) | (3) The period within which a person is required by these Rules, or by a... | fork F15 | `o 3 r 4(3) the period may be extended by consent in writing without an order of the Court` |
| 333 | O 3 r 5 [heading] | Applications to Court in an action (O. 3, r. 5) | inert, reason 1 | heading: not operative |
| 334 | O 3 r 5(1) | 5. —(1) Subject to these Rules, all applications to the Court in an acti... | encoded | `o 3 r 5(1) the application to the Court in an action is made as the Rule requires` |
| 334 | O 3 r 5(2) | (2) Form 1 is to be used when the summons has to be served. | encoded | `o 3 r 5(2) Form 1 is to be used` |
| 335 | O 3 r 5(3) | (3) Form 2 is to be used when the summons need not be served on anyone a... | encoded | `o 3 r 5(3) Form 2 is to be used` |
| 336 | O 3 r 5(4) | (4) The applicant must serve the summons and the affidavit at least 14 d... | fork F16 | `o 3 r 5(4) the period before the hearing for serving the summons and affidavit` (+1 more) |
| 337 | O 3 r 5(5) | (5) If any party wishes to contest the application, the party must file ... | encoded | `o 3 r 5(5) the duty` (+3 more) |
| 338 | O 3 r 5(6) | (6) Except in a special case, the Court will not allow further affidavit... | fork F13 | `o 3 r 5(6) the Court allows a further affidavit` |
| 339 | O 3 r 5(7) | (7) An affidavit must contain all necessary evidence in support of or in... | encoded | `o 3 r 5(7) the affidavit has the content the Rule requires` |
| 340 | O 3 r 5(8) | (8) All applications must be served on all other parties to the applicat... | encoded | `o 3 r 5(8) the application must be served on the other party` |
| 341 | O 3 r 6 [heading] | Forms (O. 3, r. 6) | inert, reason 1 | heading: not operative |
| 342 | O 3 r 6(1) | 6. —(1) The Forms as set out in the practice directions must be used wit... | encoded | `o 3 r 6(1) the Form must be used with the variations the circumstances require` |
| 342 | O 3 r 6(2) | (2) The Forms may be varied by practice directions issued with the appro... | encoded | `o 3 r 6(2) the Forms are varied by practice directions` |
| 343 | O 3 r 6(3) | (3) Where a Form states “Seal of the Court”, a document in that Form mus... | encoded | `o 3 r 6(3) the document must bear the seal of the Court` |
| 344 | O 3 r 7 [heading] | Language of documents (O. 3, r. 7) | inert, reason 1 | heading: not operative |
| 345 | O 3 r 7(1) | 7. —(1) All documents filed or used in Court must be in the English lang... | encoded | `o 3 r 7(1) the document filed or used in Court is in the English language as required` |
| 345 | O 3 r 7(2) | (2) A document which is not in the English language must be accompanied ... | encoded | `o 3 r 7(2) the document not in English is accompanied by a certified or verified translation` |
| 346 | O 3 r 8 [heading] | Use of foreign documents under Apostille Convention or Civil Procedure C... | inert, reason 1 | heading: not operative |
| 347 | O 3 r 8(1) | 8. —(1) Despite anything in these Rules, the following documents may be ... | encoded | `o 3 r 8(1)(a) the document may be received, filed or used in the Court as a foreign public document with an apostille` (+1 more) |
| 347-348 | O 3 r 8(1)(a) | ( a ) a foreign public document with an apostille placed on or attached ... | encoded | `o 3 r 8(1)(a) the document may be received, filed or used in the Court as a foreign public document with an apostille` |
| 349-350 | O 3 r 8(1)(b) | ( b ) a document or a translation of the document that has been drawn up... | encoded | `o 3 r 8(1)(b) the document may be received, filed or used in the Court under a Civil Procedure Convention` |
| 351 | O 3 r 8(2) | (2) In this Rule — | encoded | `o 3 r 8(2) the certificate is an apostille` (+1 more) |
| 351 | O 3 r 8(2) “apostille” | “apostille” means a Convention certificate as defined by section 10 of t... | encoded | `o 3 r 8(2) the certificate is an apostille` (+1 more) |
| 352 | O 3 r 8(2) “foreign public document” | “foreign public document” has the meaning given by section 6 of the Apos... | encoded | `o 3 r 8(2) the certificate is an apostille` (+1 more) |
| 353 | O 3 r 9 [heading] | Methods of hearing (O. 3, r. 9) | inert, reason 1 | heading: not operative |
| 354 | O 3 r 9 | 9. Subject to any written law, the Court may conduct a case conference o... | encoded | `o 3 r 9 the Court may conduct a hearing by electronic, mechanical or other means` |
| 355-356 | O 4 [heading] | ORDER 4 PARTIES TO PROCEEDINGS AND CAUSES OF ACTION | inert, reason 1 | heading: not operative |
| 357 | O 4 r 1 [heading] | Parties to proceedings in own name (O. 4, r. 1) | inert, reason 1 | heading: not operative |
| 358 | O 4 r 1 | 1. The following may be parties to proceedings in their own name, whethe... | encoded | `o 4 r 1 the person may be a party to proceedings in their own name` |
| 358-359 | O 4 r 1(a) | ( a ) a person who is 18 years of age or older but below 21 years of age... | encoded | `o 4 r 1(a) a person aged 18 or older but below 21 may be a party in their own name` |
| 360-361 | O 4 r 1(b) | ( b ) a person who is 21 years of age or older; | encoded | `o 4 r 1(b) a person aged 21 or older may be a party in their own name` |
| 362-363 | O 4 r 1(c) | ( c ) any entity with the capacity to sue or be sued under any law in Si... | encoded | `o 4 r 1(c) an entity with the capacity to sue or be sued may be a party in its own name` |
| 364 | O 4 r 2 [heading] | Representation by litigation representative (O. 4, r. 2) | inert, reason 1 | heading: not operative |
| 365 | O 4 r 2(1) | 2. —(1) The following persons must be represented by a litigation repres... | encoded | `o 4 r 2(1) the person must be represented by a litigation representative` |
| 365-366 | O 4 r 2(1)(a) | ( a ) a person who is below 21 years of age and who does not come under ... | encoded | `o 4 r 2(1)(a) a person below 21 who does not come under Rule 1(a) must be represented by a litigation representative` |
| 367-368 | O 4 r 2(1)(b) | ( b ) a person who lacks capacity within the meaning of the Mental Capac... | encoded | `o 4 r 2(1)(b) a person who lacks capacity must be represented by a litigation representative` |
| 369 | O 4 r 2(2) | (2) A litigation representative must be a person who can be a party to p... | fork F12 | `o 4 r 2(2) the person can be a litigation representative` |
| 370 | O 4 r 2(3) | (3) A litigation representative must not have any interest adverse to th... | encoded | `o 4 r 2(3) the litigation representative may have an interest adverse to that of the person represented` |
| 371 | O 4 r 3 [heading] | Representation by solicitor, etc. (O. 4, r. 3) | inert, reason 1 | heading: not operative |
| 372 | O 4 r 3(1) | 3. —(1) The following must be represented by a solicitor in proceedings: | encoded | `o 4 r 3(1) the person must be represented by a solicitor` |
| 372-373 | O 4 r 3(1)(a) | ( a ) a person who is represented by a litigation representative under R... | encoded | `o 4 r 3(1)(a) a person represented by a litigation representative under Rule 2(1)(b) must be represented by a solicitor` |
| 374-375 | O 4 r 3(1)(b) | ( b ) subject to paragraphs (2), (3) and (4), any entity with the capaci... | encoded | `o 4 r 3(1)(b) an entity with the capacity to sue or be sued must be represented by a solicitor` |
| 376 | O 4 r 3(2) | (2) A registered trade union may be represented by an officer of the tra... | encoded | `o 4 r 3(2) a registered trade union may be represented by an officer of the trade union` |
| 377 | O 4 r 3(3) | (3) For the purposes of section 34(1)( ea ) of the Legal Profession Act,... | encoded | `o 4 r 3(3) the Court may give permission for an officer to act on behalf of the applicant` |
| 377-378 | O 4 r 3(3)(a) | ( a ) the officer has been duly authorised by the company, variable capi... | encoded | `o 4 r 3(3) the Court may give permission for an officer to act on behalf of the applicant` |
| 379-380 | O 4 r 3(3)(b) | ( b ) the officer has sufficient executive or administrative capacity or... | encoded | `o 4 r 3(3) the Court may give permission for an officer to act on behalf of the applicant` |
| 381 | O 4 r 3(4) | (4) For the purposes of section 34(1)( eb ) of the Legal Profession Act,... | fork F14 | `o 4 r 3(4) the Court may give permission for an officer to act on behalf of the unincorporated association` |
| 381-382 | O 4 r 3(4)(a) | ( a ) the officer has been duly authorised by the unincorporated associa... | encoded | `o 4 r 3(4) the Court may give permission for an officer to act on behalf of the unincorporated association` |
| 383-384 | O 4 r 3(4)(b) | ( b ) the officer has sufficient executive or administrative capacity or... | encoded | `o 4 r 3(4) the Court may give permission for an officer to act on behalf of the unincorporated association` |
| 385 | O 4 r 3(5) | (5) For the purposes of section 34(1)( ea ) and ( eb ) and (3) of the Le... | encoded | `o 4 r 3(5) the matter or proceeding is a relevant matter or proceeding` |
| 385-386 | O 4 r 3(5)(a) | ( a ) any matter or proceeding commenced in, or any appeal under any wri... | encoded | `o 4 r 3(5) the matter or proceeding is a relevant matter or proceeding` |
| 387-388 | O 4 r 3(5)(b) | ( b ) any matter or proceeding commenced in, or any appeal under any wri... | encoded | `o 4 r 3(5) the matter or proceeding is a relevant matter or proceeding` |
| 389-390 | O 4 r 3(5)(c) | ( c ) any matter or proceeding commenced in the General Division and any... | encoded | `o 4 r 3(5) the matter or proceeding is a relevant matter or proceeding` |
| 391-392 | O 4 r 3(5)(d) | ( d ) any matter or proceeding commenced in a Family Court and any appea... | encoded | `o 4 r 3(5) the matter or proceeding is a relevant matter or proceeding` |
| 393-394 | O 4 r 3(5)(e) | ( e ) any matter or proceeding commenced in a District Court and any app... | encoded | `o 4 r 3(5) the matter or proceeding is a relevant matter or proceeding` |
| 395-396 | O 4 r 3(5)(f) | ( f ) any matter or proceeding commenced in a Magistrate’s Court and any... | encoded | `o 4 r 3(5) the matter or proceeding is a relevant matter or proceeding` |
| 397 | O 4 r 3(6) | (6) In this Rule — | fork F6 | `o 4 r 3(6) a body is a company` (+8 more) |
| 397 | O 4 r 3(6) “company” | “company” means a company incorporated under the Companies Act; | fork F6 | `o 4 r 3(6) a body is a company` (+8 more) |
| 398 | O 4 r 3(6) “Court” | “Court” means — | fork F6 | `o 4 r 3(6) a body is a company` (+8 more) |
| 398-399 | O 4 r 3(6) “Court”(a) | ( a ) the Court of Appeal, if the relevant matter or proceeding is — | fork F6 | `o 4 r 3(6) a body is a company` (+8 more) |
| 399-400 | O 4 r 3(6) “Court”(a)(i) | (i) any matter, proceeding or appeal mentioned in paragraph (5)( a ); or | fork F6 | `o 4 r 3(6) a body is a company` (+8 more) |
| 401-402 | O 4 r 3(6) “Court”(a)(ii) | (ii) any appeal mentioned in paragraph (5)( c ), ( e ) or ( f ) to the C... | fork F6 | `o 4 r 3(6) a body is a company` (+8 more) |
| 403-404 | O 4 r 3(6) “Court”(b) | ( b ) the Appellate Division, if the relevant matter or proceeding is — | fork F6 | `o 4 r 3(6) a body is a company` (+8 more) |
| 404-405 | O 4 r 3(6) “Court”(b)(i) | (i) any matter, proceeding or appeal mentioned in paragraph (5)( b ); or | fork F6 | `o 4 r 3(6) a body is a company` (+8 more) |
| 406-407 | O 4 r 3(6) “Court”(b)(ii) | (ii) any appeal mentioned in paragraph (5)( c ), ( e ) or ( f ) to the A... | fork F6 | `o 4 r 3(6) a body is a company` (+8 more) |
| 408-409 | O 4 r 3(6) “Court”(c) | ( c ) the General Division, if the matter or proceeding is — | fork F6 | `o 4 r 3(6) a body is a company` (+8 more) |
| 409-410 | O 4 r 3(6) “Court”(c)(i) | (i) any matter, proceeding or appeal mentioned in paragraph (5)( c ); or | fork F6 | `o 4 r 3(6) a body is a company` (+8 more) |
| 411-412 | O 4 r 3(6) “Court”(c)(ii) | (ii) any appeal mentioned in paragraph (5)( e ) or ( f ) to the General ... | fork F6 | `o 4 r 3(6) a body is a company` (+8 more) |
| 413-414 | O 4 r 3(6) “Court”(d) | ( d ) a Family Court, if the relevant matter or proceeding is any matter... | fork F6 | `o 4 r 3(6) a body is a company` (+8 more) |
| 415-416 | O 4 r 3(6) “Court”(e) | ( e ) a District Court, if the relevant matter or proceeding is — | fork F6 | `o 4 r 3(6) a body is a company` (+8 more) |
| 416-417 | O 4 r 3(6) “Court”(e)(i) | (i) any matter, proceeding or appeal mentioned in paragraph (5)( e ); or | fork F6 | `o 4 r 3(6) a body is a company` (+8 more) |
| 418-419 | O 4 r 3(6) “Court”(e)(ii) | (ii) any appeal mentioned in paragraph (5)( f ) under Division 2 of Orde... | fork F6 | `o 4 r 3(6) a body is a company` (+8 more) |
| 420-421 | O 4 r 3(6) “Court”(f) | ( f ) a Magistrate’s Court, if the relevant matter or proceeding is any ... | fork F6 | `o 4 r 3(6) a body is a company` (+8 more) |
| 422 | O 4 r 3(6) “limited liability partnership” | “limited liability partnership” means a limited liability partnership re... | fork F6 | `o 4 r 3(6) a body is a company` (+8 more) |
| 423 | O 4 r 3(6) “manager” | “manager”, in relation to a limited liability partnership, has the meani... | fork F6 | `o 4 r 3(6) a body is a company` (+8 more) |
| 424 | O 4 r 3(6) “officer” | “officer” — | fork F6 | `o 4 r 3(6) a body is a company` (+8 more) |
| 424-425 | O 4 r 3(6) “officer”(a) | ( a ) in relation to a company or variable capital company, means any di... | fork F6 | `o 4 r 3(6) a body is a company` (+8 more) |
| 426-427 | O 4 r 3(6) “officer”(b) | ( b ) in relation to a limited liability partnership, means any partner ... | fork F6 | `o 4 r 3(6) a body is a company` (+8 more) |
| 428-429 | O 4 r 3(6) “officer”(c) | ( c ) in relation to an unincorporated association (other than a partner... | fork F6 | `o 4 r 3(6) a body is a company` (+8 more) |
| 430-431 | O 4 r 3(6) “officer”(d) | ( d ) in relation to a registered trade union, has the meaning given by ... | fork F6 | `o 4 r 3(6) a body is a company` (+8 more) |
| 432 | O 4 r 3(6) “partner” | “partner”, in relation to a limited liability partnership, has the meani... | fork F6 | `o 4 r 3(6) a body is a company` (+8 more) |
| 433 | O 4 r 3(6) “registered trade union” | “registered trade union” has the meaning given by the Trade Unions Act; | fork F6 | `o 4 r 3(6) a body is a company` (+8 more) |
| 434 | O 4 r 3(6) “variable capital company” | “variable capital company” has the meaning given by section 2(1) of the ... | fork F6 | `o 4 r 3(6) a body is a company` (+8 more) |
| 435 | O 4 r 4 [heading] | Representation of estates (O. 4, r. 4) | inert, reason 1 | heading: not operative |
| 436 | O 4 r 4(1) | 4. —(1) Where any defendant has died but a cause of action against him o... | encoded | `o 4 r 4(1) the action may be brought against the estate of the deceased` (+1 more) |
| 436 | O 4 r 4(2) | (2) In any action brought against the estate of a deceased person — | encoded | `o 4 r 4(2)(a) the claimant must apply to the Court for an order during the period of validity for service` (+3 more) |
| 436-437 | O 4 r 4(2)(a) | ( a ) the claimant must, during the period of validity for service of th... | encoded | `o 4 r 4(2)(a) the claimant must apply to the Court for an order during the period of validity for service` (+2 more) |
| 437-438 | O 4 r 4(2)(a)(i) | (i) an order appointing a person to represent the deceased’s estate for ... | encoded | `o 4 r 4(2)(a) the claimant must apply to the Court for an order during the period of validity for service` (+2 more) |
| 439-441 | O 4 r 4(2)(a)(ii) | (ii) if a grant of probate or letters of administration has been made — ... | encoded | `o 4 r 4(2)(a) the claimant must apply to the Court for an order during the period of validity for service` (+2 more) |
| 442-443 | O 4 r 4(2)(b) | ( b ) the Court may, at any stage of the proceedings and on any terms th... | encoded | `o 4 r 4(2)(b) the Court may make the order` |
| 444 | O 4 r 4(3) | (3) Where the Public Trustee has been appointed by an order under paragr... | fork F13 | `o 4 r 4(3) the originating claim or originating application must be served on the Public Trustee` (+1 more) |
| 445 | O 4 r 4(4) | (4) Where no grant of probate or letters of administration has been made... | encoded | `o 4 r 4(4) the judgment or order binds the estate as if a grant had been made` |
| 446 | O 4 r 5 [heading] | Representation of parties who die or become bankrupt (O. 4, r. 5) | inert, reason 1 | heading: not operative |
| 447 | O 4 r 5(1) | 5. —(1) Where a party to an action dies or becomes bankrupt after the ac... | encoded | `o 4 r 5(1) the action continues despite the death or bankruptcy` |
| 447 | O 4 r 5(2) | (2) At the case conference, the Court must give directions for the furth... | encoded | `o 4 r 5(2) the Court must give directions at the case conference for the further conduct of the action` |
| 448 | O 4 r 6 [heading] | Representative proceedings (O. 4, r. 6) | inert, reason 1 | heading: not operative |
| 449 | O 4 r 6(1) | 6. —(1) Where numerous persons have a common interest in any proceedings... | encoded | `o 4 r 6(1) the persons may sue or be sued as a group with one or more representing the group` |
| 449 | O 4 r 6(2) | (2) Where a group of persons is suing under this Rule, all members in th... | encoded | `o 4 r 6(2) all members of the group must consent in writing and be included in a list of claimants` (+1 more) |
| 450 | O 4 r 6(3) | (3) Where a group of persons is being sued under this Rule, the Court ma... | encoded | `o 4 r 6(3) the Court may appoint one or more of them as representative` (+1 more) |
| 451 | O 4 r 6(4) | (4) Where there is a class of persons and all or any member of the class... | encoded | `o 4 r 6(4) the Court may appoint one or more persons to represent the class` (+1 more) |
| 452 | O 4 r 6(5) | (5) A judgment or order given in such an action is binding on all the pe... | fork F7 | `o 4 r 6(5) the judgment or order is binding on the person or class` |
| 453 | O 4 r 7 [heading] | Claim for declaration without other relief (O. 4, r. 7) | inert, reason 1 | heading: not operative |
| 454 | O 4 r 7 | 7. The Court may make a declaratory judgment or order whether or not any... | encoded | `o 4 r 7 the Court may make a declaratory judgment or order` |
| 455 | O 4 r 8 [heading] | Appointment, change and discharge of solicitor (O. 4, r. 8) | inert, reason 1 | heading: not operative |
| 456 | O 4 r 8(1) | 8. —(1) Where a party who was not represented by a solicitor decides to ... | encoded | `o 4 r 8(1) the duty` (+2 more) |
| 456 | O 4 r 8(2) | (2) Unless notice is given according to this Rule, a solicitor who is ap... | fork F13 | `o 4 r 8(2) the solicitor is deemed to be acting for the party` (+2 more) |
| 457 | O 4 r 8(3) | (3) A party who intends to change his or her solicitor must file and ser... | encoded | `o 4 r 8(3) the duty` (+2 more) |
| 458 | O 4 r 8(4) | (4) A party who after having sued or defended by a solicitor, intends an... | encoded | `o 4 r 8(4) the party must file and serve a notice of intention to act in person in Form 4 on all the parties` (+1 more) |
| 459 | O 4 r 8(5) | (5) Where a solicitor has died, has ceased practice for any reason or ca... | encoded | `o 4 r 8(5) any other party may apply to the Court for an order declaring that the solicitor has ceased to be the solicitor` |
| 460 | O 4 r 8(6) | (6) Notice given under this Rule takes effect from the time of service o... | encoded | `o 4 r 8(6) the notice has taken effect` (+1 more) |
| 461 | O 4 r 8(7) | (7) Where a party has no solicitor acting for the party on record, the p... | encoded | `o 4 r 8(7) the party must give notice by letter to all the parties stating an address in Singapore for service` (+1 more) |
| 462 | O 4 r 8(8) | (8) Where a party fails to comply with paragraph (7), the party’s last k... | encoded | `o 4 r 8(8) the address deemed to be the party's address for service` (+1 more) |
| 463 | O 4 r 8(9) | (9) Where a party has no address in Singapore, the party may give notice... | encoded | `o 4 r 8(9) the party may give notice by letter stating an electronic mail address for service` (+1 more) |
| 464 | O 4 r 8(10) | (10) In any application to which Order 24A applies, the requirements in ... | encoded | `o 4 r 8(10) the requirements in Order 24A, Rule 4 apply in addition` |
| 465 | O 4 r 9 [heading] | Withdrawal of solicitor who has ceased to act for party (O. 4, r. 9) | inert, reason 1 | heading: not operative |
| 466 | O 4 r 9(1) | 9. —(1) Where a solicitor who has acted for a party in a cause or matter... | encoded | `o 4 r 9(1) the solicitor may apply to the Court for an order declaring that the solicitor has ceased to act` (+3 more) |
| 466 | O 4 r 9(2) | (2) An application for an order under this Rule must be made by summons ... | fork F13 | `o 4 r 9(2) the application is made by summons in Form 6` (+1 more) |
| 467 | O 4 r 9(3) | (3) The application mentioned in paragraph (2) must be supported by an a... | encoded | `o 4 r 9(3) the application is supported by an affidavit as required` |
| 468 | O 4 r 9(4) | (4) An order in Form 7 made under this Rule does not affect the rights o... | encoded | `o 4 r 9(4) the order affects the rights of the solicitor and the party as between themselves` |
| 469 | O 4 r 9(5) | (5) Despite anything in paragraph (1), where the legal aid certificate o... | encoded | `o 4 r 9(5) the solicitor who acted for the assisted person ceases to be the solicitor acting` (+1 more) |
| 470 | O 4 r 9(6) | (6) Notice that a solicitor has ceased to act for an assisted person pur... | encoded | `o 4 r 9(6) notice must be served in the manner prescribed by the Legal Aid and Advice Act` (+1 more) |
| 471-472 | O 5 [heading] | ORDER 5 AMICABLE RESOLUTION OF CASES | inert, reason 1 | heading: not operative |
| 473 | O 5 r 1 [heading] | Duty to consider amicable resolution of disputes (O. 5, r. 1) | inert, reason 1 | heading: not operative |
| 474 | O 5 r 1(1) | 1. —(1) A party to any proceedings has the duty to consider amicable res... | encoded | `o 5 r 1(1) the party has the duty to consider amicable resolution of the dispute` (+1 more) |
| 474 | O 5 r 1(2) | (2) A party is to make an offer of amicable resolution before commencing... | fork F13 | `o 5 r 1(2) the party is to make an offer of amicable resolution before commencing the action` (+1 more) |
| 475 | O 5 r 1(3) | (3) An offer of amicable resolution in this Order means making an offer ... | encoded | `o 5 r 1(3) an act is an offer of amicable resolution` |
| 476 | O 5 r 1(4) | (4) A party to any proceedings must not reject an offer of amicable reso... | fork F13 | `o 5 r 1(4) the duty` (+1 more) |
| 477 | O 5 r 2 [heading] | Terms of amicable resolution (O. 5, r. 2) | inert, reason 1 | heading: not operative |
| 478 | O 5 r 2(1) | 2. —(1) An offer of amicable resolution and any rejection must be in wri... | encoded | `o 5 r 2(1) the offer or rejection is in writing as required` |
| 478 | O 5 r 2(2) | (2) An offer of amicable resolution must be open for acceptance within a... | fork F13 | `o 5 r 2(2) the least number of days an offer must be open for acceptance` (+1 more) |
| 479 | O 5 r 2(3) | (3) The terms of an offer that has been made and not accepted must not b... | encoded | `o 5 r 2(3) the terms cannot yet be relied upon or made known to the Court` |
| 480 | O 5 r 2(4) | (4) Any offer of amicable resolution which does not state an expiry date... | fork F13 | `o 5 r 2(4) the offer has expired under this paragraph` |
| 481 | O 5 r 3 [heading] | Powers of Court (O. 5, r. 3) | inert, reason 1 | heading: not operative |
| 482 | O 5 r 3(1) | 3. —(1) The Court may order the parties to attempt to resolve the disput... | encoded | `o 5 r 3(1) the Court may order the parties to attempt to resolve the dispute by amicable resolution` |
| 482 | O 5 r 3(2) | (2) In deciding whether to exercise its power under paragraph (1), the C... | encoded | `o 5 r 3(2) the Court must have regard to the Ideals and all other relevant circumstances` (+1 more) |
| 483 | O 5 r 3(3) | (3) Without affecting the Court’s power under paragraph (1), if a party ... | encoded | `o 5 r 3(3) the Court may order the party to submit a sealed document setting out the reasons for the refusal` |
| 484 | O 5 r 3(4) | (4) The sealed document will only be opened by the Court after the deter... | encoded | `o 5 r 3(4) the sealed document may be opened by the Court` (+1 more) |
| 485 | O 5 r 3(5) | (5) The Court may suggest solutions for the amicable resolution of the d... | encoded | `o 5 r 3(5) the Court may suggest solutions for the amicable resolution of the dispute` |
| 486-487 | O 6 [heading] | ORDER 6 COMMENCEMENT OF PROCEEDINGS | inert, reason 1 | heading: not operative |
| 488 | O 6 Division 1 [heading] | Division 1 — General | inert, reason 1 | heading: not operative |
| 489 | O 6 r 1 [heading] | Mode of commencing proceedings (O. 6, r. 1) | inert, reason 1 | heading: not operative |
| 490 | O 6 r 1(1) | 1. —(1) Unless these Rules or any written law otherwise provide, a claim... | encoded | `o 6 r 1(1) a claimant may commence proceedings by an originating claim or an originating application` |
| 490 | O 6 r 1(2) | (2) A claimant must commence proceedings by an originating claim where t... | fork F5 | `o 6 r 1(2) the claimant must commence proceedings by an originating claim` |
| 491 | O 6 r 1(3) | (3) A claimant must commence proceedings by an originating application w... | fork F5 | `o 6 r 1(3) the claimant must commence proceedings by an originating application` |
| 491-492 | O 6 r 1(3)(a) | ( a ) these Rules or any written law require it; | fork F5 | `o 6 r 1(3) the claimant must commence proceedings by an originating application` |
| 493-494 | O 6 r 1(3)(b) | ( b ) the proceedings concern an application made to the Court under any... | fork F5 | `o 6 r 1(3) the claimant must commence proceedings by an originating application` |
| 495-496 | O 6 r 1(3)(c) | ( c ) the proceedings concern solely or primarily the construction of an... | fork F5 | `o 6 r 1(3) the claimant must commence proceedings by an originating application` |
| 497 | O 6 r 2 [heading] | Issue of originating claim or originating application (O. 6, r. 2) | inert, reason 1 | heading: not operative |
| 498 | O 6 r 2 | 2. An originating claim or an originating application is deemed issued w... | encoded | `o 6 r 2 the originating claim or originating application is deemed issued` |
| 499 | O 6 r 3 [heading] | Duration and renewal of originating claim or originating application (O.... | inert, reason 1 | heading: not operative |
| 500 | O 6 r 3(1) | 3. —(1) Subject to this Rule, an originating claim or an originating app... | fork F16 | `o 6 r 3(1) the number of months for which it is valid for service` (+2 more) |
| 500-501 | O 6 r 3(1)(a) | ( a ) where the originating claim or originating application is to be se... | encoded | `o 6 r 3(1) the number of months for which it is valid for service` (+2 more) |
| 501-502 | O 6 r 3(1)(a)(i) | (i) with the court’s approval under Order 8, Rule 1(2); or | encoded | `o 6 r 3(1) the number of months for which it is valid for service` (+2 more) |
| 503-505 | O 6 r 3(1)(a)(ii) | (ii) where the court’s approval is not required under Order 8, Rule 1(3)... | encoded | `o 6 r 3(1) the number of months for which it is valid for service` (+2 more) |
| 506-507 | O 6 r 3(1)(b) | ( b ) in any other case — for 3 months beginning with the date of its is... | encoded | `o 6 r 3(1) the number of months for which it is valid for service` (+2 more) |
| 508 | O 6 r 3(2) | (2) An application may be made to extend the validity of the originating... | encoded | `o 6 r 3(2) an application may be made to extend the validity` |
| 509 | O 6 r 3(3) | (3) The Court may order the validity of the originating claim or origina... | encoded | `o 6 r 3(3) the day on which an extension of the validity begins` |
| 510 | O 6 r 3(4) | (4) Except in a special case, the Court may extend the validity of the o... | fork F15 | `o 6 r 3(4) the Court may extend the validity` |
| 511 | O 6 r 3(5) | (5) The originating claim or originating application in respect of which... | encoded | `o 6 r 3(5) the renewed originating claim or originating application is endorsed as required` |
| 512 | O 6 r 3(6) | (6) Paragraphs (1) and (4) do not apply to an originating claim relating... | encoded | `o 6 r 3(6) paragraphs (1) and (4) apply to the originating claim` |
| 513 | O 6 r 4 [heading] | Personal service of originating claim or originating application (O. 6, ... | inert, reason 1 | heading: not operative |
| 514 | O 6 r 4 | 4. Subject to the provisions of any written law and these Rules, an orig... | fork F4 | `o 6 r 4 the originating claim or originating application is served personally on the defendant as required` |
| 515 | O 6 Division 2 [heading] | Division 2 — Originating claim | inert, reason 1 | heading: not operative |
| 516 | O 6 r 5 [heading] | Form and service of originating claim (O. 6, r. 5) | inert, reason 1 | heading: not operative |
| 517 | O 6 r 5(1) | 5. —(1) An originating claim must be in Form 8. | encoded | `o 6 r 5(1) the originating claim is in Form 8` |
| 517 | O 6 r 5(2) | (2) If the claim is for personal injuries, the claimant must annex a med... | encoded | `o 6 r 5(2) the claimant must annex a medical report and a statement of the special damages claimed` (+1 more) |
| 518 | O 6 r 5(3) | (3) An originating claim may be endorsed generally with a concise descri... | encoded | `o 6 r 5(3) the originating claim may be endorsed in that way` |
| 519 | O 6 r 5(4) | (4) Except in a special case, an originating claim may be endorsed gener... | fork F13 | `o 6 r 5(4) the period for the limitation to expire after issue` (+1 more) |
| 520 | O 6 r 5(5) | (5) Where the originating claim is endorsed generally, a statement of cl... | encoded | `o 6 r 5(5) the duty` (+3 more) |
| 521 | O 6 r 5(6) | (6) If the originating claim is to be served in Singapore, reasonable st... | encoded | `o 6 r 5(6) the period for taking reasonable steps to serve in Singapore` (+1 more) |
| 522 | O 6 r 5(7) | (7) If the originating claim is to be served out of Singapore, reasonabl... | encoded | `o 6 r 5(7) the period for taking reasonable steps to serve out of Singapore` (+1 more) |
| 523 | O 6 r 6 [heading] | Form and service of notice of intention to contest or not contest (O. 6,... | inert, reason 1 | heading: not operative |
| 524 | O 6 r 6(1) | 6. —(1) A defendant who is served an originating claim in Singapore must... | encoded | `o 6 r 6(1) the duty` (+2 more) |
| 524 | O 6 r 6(2) | (2) A defendant who is served out of Singapore must file and serve such ... | encoded | `o 6 r 6(2) the duty` (+2 more) |
| 525 | O 6 r 6(3) | (3) The notice of intention to contest or not contest the originating cl... | encoded | `o 6 r 6(3) the notice of intention to contest or not contest is in Form 10` |
| 526 | O 6 r 6(4) | (4) The filing and service of such a notice is not treated as a submissi... | encoded | `o 6 r 6(4) filing and serving the notice is treated as a submission to jurisdiction or a waiver of improper service` |
| 527 | O 6 r 6(5) | (5) If the defendant fails to file and serve such a notice within the pr... | encoded | `o 6 r 6(5) the claimant may apply for judgment against the defendant in Form 11` |
| 528 | O 6 r 6(6) | (6) The claimant must file a memorandum of service in Form 12 when the c... | encoded | `o 6 r 6(6) the claimant must file a memorandum of service in Form 12` |
| 529 | O 6 r 6(7) | (7) The Court may, when giving judgment under this Rule, direct the paym... | fork F16 | `o 6 r 6(7) the yearly rate of interest the Court may direct` (+2 more) |
| 530 | O 6 r 7 [heading] | Form and service of defence (O. 6, r. 7) | inert, reason 1 | heading: not operative |
| 531 | O 6 r 7(1) | 7. —(1) A defendant who is served in Singapore must file and serve a def... | encoded | `o 6 r 7(1) the duty` (+2 more) |
| 531 | O 6 r 7(2) | (2) A defendant who is served out of Singapore must file and serve a def... | encoded | `o 6 r 7(2) the duty` (+2 more) |
| 532 | O 6 r 7(3) | (3) The defence must be in Form 13. | encoded | `o 6 r 7(3) the defence is in Form 13` |
| 533 | O 6 r 7(4) | (4) If the defendant is challenging the jurisdiction of the Court on the... | encoded | `o 6 r 7(4) the defendant need not file and serve a defence on the merits` (+1 more) |
| 534 | O 6 r 7(5) | (5) The challenge to jurisdiction may be for the reason that — | encoded | `o 6 r 7(5) the challenge to jurisdiction may be for that reason` |
| 534-535 | O 6 r 7(5)(a) | ( a ) the Court has no jurisdiction to hear the action; or | encoded | `o 6 r 7(5) the challenge to jurisdiction may be for that reason` |
| 536-537 | O 6 r 7(5)(b) | ( b ) the Court should not exercise jurisdiction to hear the action. | encoded | `o 6 r 7(5) the challenge to jurisdiction may be for that reason` |
| 538 | O 6 r 7(6) | (6) A defence filed under paragraph (4) is not treated as a submission t... | encoded | `o 6 r 7(6) a defence filed under paragraph (4) is treated as a submission to jurisdiction` |
| 539 | O 6 r 7(7) | (7) If the defendant fails to file and serve a defence within the prescr... | encoded | `o 6 r 7(7) the claimant may apply for judgment in default of defence in Form 14` |
| 540 | O 6 r 7(8) | (8) The Court may, when giving judgment under this Rule, direct the paym... | fork F16 | `o 6 r 7(8) the yearly rate of interest the Court may direct` (+2 more) |
| 541 | O 6 r 8 [heading] | Form and service of counterclaim (O. 6, r. 8) | inert, reason 1 | heading: not operative |
| 542 | O 6 r 8(1) | 8. —(1) If the defendant intends to counterclaim against the claimant, t... | encoded | `o 6 r 8(1) the defendant must file and serve the counterclaim with the defence` (+1 more) |
| 542 | O 6 r 8(2) | (2) The counterclaim must be in Form 13. | encoded | `o 6 r 8(2) the counterclaim is in Form 13` |
| 543 | O 6 r 8(3) | (3) If the counterclaim is for personal injuries, the defendant must ann... | encoded | `o 6 r 8(3) the defendant must annex a medical report and a statement of the special damages claimed` |
| 544 | O 6 r 9 [heading] | Form and service of defence to counterclaim (O. 6, r. 9) | inert, reason 1 | heading: not operative |
| 545 | O 6 r 9(1) | 9. —(1) The claimant need not file a reply to the defence if the claiman... | encoded | `o 6 r 9(1) the duty` (+3 more) |
| 545 | O 6 r 9(2) | (2) The claimant’s defence to the counterclaim must be in Form 13. | encoded | `o 6 r 9(2) the claimant's defence to the counterclaim is in Form 13` |
| 546 | O 6 r 9(3) | (3) If the claimant fails to file and serve a defence to the counterclai... | encoded | `o 6 r 9(3) the defendant may apply for judgment in default of defence in respect of the counterclaim in Form 14` (gap: the text states no rate of interest for a default judgment on a counterclaim (r 6(7) and r 7(8) state 5.33% for judgments under r 6 and r 7 only); no function) |
| 547 | O 6 r 10 [heading] | Further pleadings (O. 6, r. 10) | inert, reason 1 | heading: not operative |
| 548 | O 6 r 10(1) | 10. —(1) Parties must seek the approval of the Court at the case confere... | encoded | `o 6 r 10(1) the parties must seek the approval of the Court at the case conference to file a further pleading` |
| 548 | O 6 r 10(2) | (2) No further pleadings may be filed unless the Court otherwise orders ... | encoded | `o 6 r 10(2) a further pleading may be filed` |
| 549 | O 6 Division 3 [heading] | Division 3 — Originating application | inert, reason 1 | heading: not operative |
| 550 | O 6 r 11 [heading] | Forms of originating application (O. 6, r. 11) | inert, reason 1 | heading: not operative |
| 551 | O 6 r 11(1) | 11. —(1) Subject to these Rules and any other written law, an originatin... | encoded | `o 6 r 11(1) the originating application is in Form 15 or Form 16 and supported by affidavit` |
| 551 | O 6 r 11(2) | (2) Form 15 is to be used when the originating application has to be ser... | encoded | `o 6 r 11(2) Form 15 is to be used` |
| 552 | O 6 r 11(3) | (3) Form 16 is to be used when the originating application need not be s... | encoded | `o 6 r 11(3) Form 16 is to be used` |
| 553 | O 6 r 11(4) | (4) If the originating application is to be served in Singapore, reasona... | encoded | `o 6 r 11(4) the period for taking reasonable steps to serve in Singapore` (+1 more) |
| 554 | O 6 r 11(5) | (5) If the originating application is to be served out of Singapore, rea... | encoded | `o 6 r 11(5) the period for taking reasonable steps to serve out of Singapore` (+1 more) |
| 555 | O 6 r 12 [heading] | Form and service of defendant’s affidavit (O. 6, r. 12) | inert, reason 1 | heading: not operative |
| 556 | O 6 r 12(1) | 12. —(1) A defendant who is served in Singapore must file and serve the ... | encoded | `o 6 r 12(1) the duty` (+3 more) |
| 556 | O 6 r 12(2) | (2) A defendant who is served out of Singapore must file and serve the d... | encoded | `o 6 r 12(2) the duty` (+3 more) |
| 557 | O 6 r 12(3) | (3) If the defendant is challenging the jurisdiction of the Court on the... | encoded | `o 6 r 12(3) the defendant need not file and serve an affidavit on the merits` |
| 558 | O 6 r 12(4) | (4) The challenge to jurisdiction may be for the reason that — | encoded | `o 6 r 12(4) the challenge to jurisdiction may be for that reason` |
| 558-559 | O 6 r 12(4)(a) | ( a ) the Court has no jurisdiction to hear the action; or | encoded | `o 6 r 12(4) the challenge to jurisdiction may be for that reason` |
| 560-561 | O 6 r 12(4)(b) | ( b ) the Court should not exercise jurisdiction because it is not the a... | encoded | `o 6 r 12(4) the challenge to jurisdiction may be for that reason` |
| 562 | O 6 r 12(5) | (5) An affidavit filed under paragraph (3) is not treated as a submissio... | encoded | `o 6 r 12(5) an affidavit filed under paragraph (3) is treated as a submission to jurisdiction` |
| 563 | O 6 r 12(6) | (6) Except in a special case, no further affidavits may be filed after t... | fork F13 | `o 6 r 12(6) a further affidavit may be filed` |
| 564 | O 6 r 13 [heading] | Contents of affidavit (O. 6, r. 13) | inert, reason 1 | heading: not operative |
| 565 | O 6 r 13 | 13. An affidavit filed in an originating application must contain all th... | encoded | `o 6 r 13 the affidavit has the content the Rule requires` |
| 566 | O 6 r 14 [heading] | Counterclaim (O. 6, r. 14) | inert, reason 1 | heading: not operative |
| 567 | O 6 r 14 | 14. If a defendant intends to make a counterclaim in the originating app... | encoded | `o 6 r 14 the defendant must include the counterclaim in the defendant's affidavit with all the evidence that is necessary for it` (+1 more) |
| 568-569 | O 7 [heading] | ORDER 7 SERVICE IN SINGAPORE | inert, reason 1 | heading: not operative |
| 570 | O 7 r 1 [heading] | Methods of service generally (O. 7, r. 1) | inert, reason 1 | heading: not operative |
| 571 | O 7 r 1(1) | 1. —(1) Any document that is required to be served under these Rules may... | encoded | `o 7 r 1(1)(a) a document may be served by personal service` (+1 more) |
| 571-572 | O 7 r 1(1)(a) | ( a ) personal service, where expressly required by these Rules or any w... | encoded | `o 7 r 1(1)(a) a document may be served by personal service` |
| 573-574 | O 7 r 1(1)(b) | ( b ) ordinary service. | fork F4 | `o 7 r 1(1)(b) a document may be served by ordinary service` |
| 575 | O 7 r 1(2) | (2) The Court may, in an appropriate case, dispense with personal servic... | encoded | `o 7 r 1(2) the Court may dispense with personal service, ordinary service or service altogether` |
| 576 | O 7 r 2 [heading] | Personal service (O. 7, r. 2) | inert, reason 1 | heading: not operative |
| 577 | O 7 r 2(1) | 2. —(1) Personal service of a document is effected — | encoded | `o 7 r 2(1) personal service is effected` |
| 577-578 | O 7 r 2(1)(a) | ( a ) on a natural person by leaving a copy of the document with that pe... | encoded | `o 7 r 2(1) personal service is effected` |
| 579-580 | O 7 r 2(1)(b) | ( b ) on any entity by leaving a copy of the document with the chairpers... | encoded | `o 7 r 2(1) personal service is effected` |
| 581-582 | O 7 r 2(1)(c) | ( c ) on any person or entity according to the requirements of any writt... | encoded | `o 7 r 2(1) personal service is effected` |
| 583-584 | O 7 r 2(1)(d) | ( d ) in any manner agreed with the person or the entity to be served. | encoded | `o 7 r 2(1) personal service is effected` |
| 585 | O 7 r 2(2) | (2) The following persons may effect personal service: | encoded | `o 7 r 2(2) the person may effect personal service` |
| 585-586 | O 7 r 2(2)(a) | ( a ) a process server of the Court; | encoded | `o 7 r 2(2) the person may effect personal service` |
| 587-588 | O 7 r 2(2)(b) | ( b ) a solicitor; | encoded | `o 7 r 2(2) the person may effect personal service` |
| 589-590 | O 7 r 2(2)(c) | ( c ) a solicitor’s employee; | encoded | `o 7 r 2(2) the person may effect personal service` |
| 591-592 | O 7 r 2(2)(d) | ( d ) a litigant who is not legally represented or such a person’s emplo... | encoded | `o 7 r 2(2) the person may effect personal service` |
| 593-594 | O 7 r 2(2)(e) | ( e ) any other person that the Registrar may allow in a particular case... | encoded | `o 7 r 2(2) the person may effect personal service` |
| 595 | O 7 r 2(3) | (3) If the process server of the Court effects service, the Registrar mu... | encoded | `o 7 r 2(3) the Registrar must notify the requesting person of the fact and manner of service` |
| 596 | O 7 r 3 [heading] | Ordinary service (O. 7, r. 3) | inert, reason 1 | heading: not operative |
| 597 | O 7 r 3 | 3. Ordinary service of a document may be effected — | encoded | `o 7 r 3 ordinary service may be effected in that manner` |
| 597-598 | O 7 r 3(a) | ( a ) by leaving the document at or posting it to — | encoded | `o 7 r 3 ordinary service may be effected in that manner` |
| 598-599 | O 7 r 3(a)(i) | (i) in the case of a natural person, the person’s usual or last known ad... | encoded | `o 7 r 3 ordinary service may be effected in that manner` |
| 600-601 | O 7 r 3(a)(ii) | (ii) in the case of an entity, its registered or principal office or, if... | encoded | `o 7 r 3 ordinary service may be effected in that manner` |
| 602-603 | O 7 r 3(b) | ( b ) by electronic mail at the electronic mail address provided by the ... | encoded | `o 7 r 3 ordinary service may be effected in that manner` |
| 604-605 | O 7 r 3(c) | ( c ) by fax, but only if — | encoded | `o 7 r 3 ordinary service may be effected in that manner` |
| 605-606 | O 7 r 3(c)(i) | (i) both the serving party and the party to be served act by solicitor; ... | encoded | `o 7 r 3 ordinary service may be effected in that manner` |
| 607-608 | O 7 r 3(c)(ii) | (ii) the solicitor acting for the party to be served indicates to the so... | encoded | `o 7 r 3 ordinary service may be effected in that manner` |
| 609-610 | O 7 r 3(d) | ( d ) in any manner agreed between the parties; | encoded | `o 7 r 3 ordinary service may be effected in that manner` |
| 611-612 | O 7 r 3(e) | ( e ) in any manner which the Court may direct, including the use of ele... | encoded | `o 7 r 3 ordinary service may be effected in that manner` |
| 613-614 | O 7 r 3(f) | ( f ) in any manner provided under any written law. | encoded | `o 7 r 3 ordinary service may be effected in that manner` |
| 615 | O 7 r 4 [heading] | Service on agent of overseas principal (O. 7, r. 4) | inert, reason 1 | heading: not operative |
| 616 | O 7 r 4(1) | 4. —(1) The Court may, on a summons without notice, direct service to be... | encoded | `o 7 r 4(1) the Court may direct service on an agent or manager of a principal` |
| 616-617 | O 7 r 4(1)(a) | ( a ) an action, including the administration of an estate, is against a... | encoded | `o 7 r 4(1) the Court may direct service on an agent or manager of a principal` |
| 618-619 | O 7 r 4(1)(b) | ( b ) the agent or manager has personal control or management within Sin... | encoded | `o 7 r 4(1) the Court may direct service on an agent or manager of a principal` |
| 620-621 | O 7 r 4(1)(c) | ( c ) either the authority of the agent or manager has not been terminat... | encoded | `o 7 r 4(1) the Court may direct service on an agent or manager of a principal` |
| 622 | O 7 r 4(2) | (2) An agent of a ship is deemed to be the agent of the owner or of the ... | encoded | `o 7 r 4(2) the person is deemed the agent of the owner or of the charterer of the ship` |
| 623 | O 7 r 4(3) | (3) The claimant must send a copy of the order of Court authorising serv... | encoded | `o 7 r 4(3) the duty` (+3 more) |
| 624 | O 7 r 5 [heading] | Service in certain actions for possession of immovable property (O. 7, r... | inert, reason 1 | heading: not operative |
| 625 | O 7 r 5 | 5. Where there is a claim for possession of immovable property, the Cour... | encoded | `o 7 r 5 the Court may authorise service by placing the document on a conspicuous part of the property` |
| 625-626 | O 7 r 5(a) | ( a ) no person appears to be in possession of the immovable property; a... | encoded | `o 7 r 5 the Court may authorise service by placing the document on a conspicuous part of the property` |
| 627-628 | O 7 r 5(b) | ( b ) service cannot otherwise be effected on any party to be served. | encoded | `o 7 r 5 the Court may authorise service by placing the document on a conspicuous part of the property` |
| 629 | O 7 r 6 [heading] | Service on Minister, etc., in proceedings which are not by or against Go... | inert, reason 1 | heading: not operative |
| 630 | O 7 r 6 | 6. Where for the purpose of or in connection with any proceedings, not b... | encoded | `o 7 r 6 section 20 of the Government Proceedings Act and Order 59, Rule 3 apply to the service` |
| 631 | O 7 r 7 [heading] | Substituted service (O. 7, r. 7) | inert, reason 1 | heading: not operative |
| 632 | O 7 r 7(1) | 7. —(1) If a document is required to be served personally and it is impr... | encoded | `o 7 r 7(1) a party may apply to serve the document by substituted service` |
| 632 | O 7 r 7(2) | (2) The Court may order any method of substituted service that is effect... | encoded | `o 7 r 7(2) the Court may order that method of substituted service` |
| 633 | O 7 r 7(3) | (3) Substituted service is to be effected within 14 days after the order... | encoded | `o 7 r 7(3) the period for substituted service` (+1 more) |
| 634 | O 7 r 8 [heading] | Time for service (O. 7, r. 8) | inert, reason 1 | heading: not operative |
| 635 | O 7 r 8(1) | 8. —(1) Subject to any written law and these Rules (including Order 28 r... | fork F10 | `o 7 r 8 the day service is deemed effected` (+1 more) |
| 635 | O 7 r 8(2) | (2) When service is effected after 5 p.m. on any particular day, service... | fork F10 | `o 7 r 8 the day service is deemed effected` (+1 more) |
| 636-637 | O 8 [heading] | ORDER 8 SERVICE OUT OF SINGAPORE | inert, reason 1 | heading: not operative |
| 638 | O 8 r 1 [heading] | Service out of Singapore with Court’s approval (O. 8, r. 1) | inert, reason 1 | heading: not operative |
| 639 | O 8 r 1(1) | 1. —(1) An originating process or other court document may be served out... | encoded | `o 8 r 1(1) the document may be served out of Singapore with the Court's approval` |
| 639 | O 8 r 1(2) | (2) To obtain the Court’s approval, the claimant must apply to the Court... | encoded | `o 8 r 1(2) the claimant must apply to the Court by summons without notice, supported by affidavit` (+1 more) |
| 639-640 | O 8 r 1(2)(a) | ( a ) why the Court has the jurisdiction or is the appropriate court to ... | encoded | `o 8 r 1(2) the claimant must apply to the Court by summons without notice, supported by affidavit` (+1 more) |
| 641-642 | O 8 r 1(2)(b) | ( b ) in which country or place the defendant is, or probably may be fou... | encoded | `o 8 r 1(2) the claimant must apply to the Court by summons without notice, supported by affidavit` (+1 more) |
| 643-644 | O 8 r 1(2)(c) | ( c ) whether the validity of the originating process needs to be extend... | encoded | `o 8 r 1(2) the claimant must apply to the Court by summons without notice, supported by affidavit` (+1 more) |
| 645 | O 8 r 1(3) | (3) The Court’s approval is not required if service out of Singapore is ... | encoded | `o 8 r 1(3) the Court's approval is not required` |
| 646 | O 8 r 1(4) | (4) The Court’s approval is not required for service of court documents ... | encoded | `o 8 r 1(4) the Court's approval is not required for service of the document` |
| 647 | O 8 r 2 [heading] | Methods of service out of Singapore (O. 8, r. 2) | inert, reason 1 | heading: not operative |
| 648 | O 8 r 2(1) | 2. —(1) Where the Court’s approval has been obtained under Rule 1(2), se... | fork F8 | `o 8 r 2(1) service out of Singapore may be effected in that manner` |
| 648-649 | O 8 r 2(1)(a) | ( a ) according to the manner contractually agreed between the parties; | fork F8 | `o 8 r 2(1) service out of Singapore may be effected in that manner` |
| 650-651 | O 8 r 2(1)(b) | ( b ) where there is a Civil Procedure Convention governing service in t... | fork F8 | `o 8 r 2(1) service out of Singapore may be effected in that manner` |
| 651-652 | O 8 r 2(1)(b)(i) | (i) in the case of the Hague Service Convention as defined in Rule 4A(7)... | fork F8 | `o 8 r 2(1) service out of Singapore may be effected in that manner` |
| 652-653 | O 8 r 2(1)(b)(i)(A) | (A) in accordance with Rule 4A or 6, whichever is applicable; or | fork F8 | `o 8 r 2(1) service out of Singapore may be effected in that manner` |
| 654-655 | O 8 r 2(1)(b)(i)(B) | (B) subject to any objection made by the receiving Contracting State, in... | fork F8 | `o 8 r 2(1) service out of Singapore may be effected in that manner` |
| 656-657 | O 8 r 2(1)(b)(ii) | (ii) in the case of any other Civil Procedure Convention — according to ... | fork F8 | `o 8 r 2(1) service out of Singapore may be effected in that manner` |
| 658-659 | O 8 r 2(1)(b)(iii) | (iii) in the case where both the Hague Service Convention and another Ci... | fork F8 | `o 8 r 2(1) service out of Singapore may be effected in that manner` |
| 660-661 | O 8 r 2(1)(c) | ( c ) through the government of the foreign country if that government i... | fork F8 | `o 8 r 2(1) service out of Singapore may be effected in that manner` |
| 662-663 | O 8 r 2(1)(d) | ( d ) through the judicial authority of the foreign country if that auth... | fork F8 | `o 8 r 2(1) service out of Singapore may be effected in that manner` |
| 664-665 | O 8 r 2(1)(e) | ( e ) through a Singapore consular authority in the foreign country seek... | fork F8 | `o 8 r 2(1) service out of Singapore may be effected in that manner` |
| 666-667 | O 8 r 2(1)(f) | ( f ) according to the manner provided by the law of that foreign countr... | fork F8 | `o 8 r 2(1) service out of Singapore may be effected in that manner` |
| 668 | O 8 r 2(2) | (2) Unless any Civil Procedure Convention, treaty, government or judicia... | encoded | `o 8 r 2(2) the documents may be sent to the entity by the serving party` (+2 more) |
| 669 | O 8 r 2(3) | (3) Where the originating process or other court documents have to be se... | encoded | `o 8 r 2(3) the solicitor for the serving party must send them to the Registrar with a letter` (+1 more) |
| 670 | O 8 r 2(4) | (4) Every originating process or court document which is to be served ou... | fork F13 | `o 8 r 2(4) the document must be accompanied by a translation` (+1 more) |
| 671 | O 8 r 2(5) | (5) The translation must be certified by a person qualified to do so and... | encoded | `o 8 r 2(5) the translation is certified as required` |
| 672 | O 8 r 2(6) | (6) Nothing is to be done under this Rule that is contrary to the laws o... | encoded | `o 8 r 2(6) it may be done under this Rule` |
| 673 | O 8 r 3 [heading] | Service of originating process on person in Malaysia or Brunei Darussala... | inert, reason 1 | heading: not operative |
| 674 | O 8 r 3 | 3. Where the defendant is in Malaysia or Brunei Darussalam, the originat... | encoded | `o 8 r 3 the originating process may be served in that manner` |
| 674-675 | O 8 r 3(a) | ( a ) may be served in accordance with Rule 2; or | encoded | `o 8 r 3 the originating process may be served in that manner` |
| 676-677 | O 8 r 3(b) | ( b ) may be sent by post or otherwise by the Registrar to the Magistrat... | encoded | `o 8 r 3(b) the originating process is deemed to have been duly served` |
| 678 | O 8 r 4 [heading] | Service of originating process issued in State Courts on person in any j... | inert, reason 1 | heading: not operative |
| 679 | O 8 r 4(1) | 4. —(1) An originating process issued in the State Courts which is to be... | fork F14 | `o 8 r 4(1) the Registrar of the State Courts must send the originating process to the Registrar of the Supreme Court` (+2 more) |
| 679-680 | O 8 r 4(1)(a) | ( a ) must be sent by the Registrar of the State Courts to the Registrar... | encoded | `o 8 r 4(1)(a) the duty` |
| 681-682 | O 8 r 4(1)(b) | ( b ) must be served in accordance with these Rules relating to the serv... | encoded | `o 8 r 4(1) the Registrar of the State Courts must send the originating process to the Registrar of the Supreme Court` (+2 more) |
| 683 | O 8 r 4(2) | (2) Every certificate of service received by the Registrar of the Suprem... | encoded | `o 8 r 4(2) the duty` (+2 more) |
| 684 | O 8 r 4A [heading] | Service of originating process, etc., out of Singapore on person under A... | inert, reason 1 | heading: not operative |
| 685 | O 8 r 4A(1) | 4A. —(1) This Rule applies to the service out of Singapore, under Articl... | fork F14 | `o 8 r 4A(1) this Rule applies to the service` |
| 685 | O 8 r 4A(2) | (2) If any provision in this Rule is inconsistent with any other provisi... | encoded | `o 8 r 4A(2) the provision in Rule 4A prevails over the other provision in this Order` |
| 686 | O 8 r 4A(3) | (3) The person mentioned in paragraph (1) must have a known address in t... | encoded | `o 8 r 4A(3) the person has a known address as required` |
| 687 | O 8 r 4A(4) | (4) A person who wishes to serve any document mentioned in paragraph (1)... | encoded | `o 8 r 4A(4) the person must file in the Registry a request for service in the current version of Part 1 of the Model Form` (+1 more) |
| 687-688 | O 8 r 4A(4)(a) | ( a ) a sealed copy of the document to be served; | encoded | `o 8 r 4A(4) the person must file in the Registry a request for service in the current version of Part 1 of the Model Form` (+1 more) |
| 689-690 | O 8 r 4A(4)(b) | ( b ) a summary of the document to be served, in accordance with Part 3 ... | encoded | `o 8 r 4A(4) the person must file in the Registry a request for service in the current version of Part 1 of the Model Form` (+1 more) |
| 691-692 | O 8 r 4A(4)(c) | ( c ) a translation of the documents mentioned in sub-paragraphs ( a ) a... | encoded | `o 8 r 4A(4) the person must file in the Registry a request for service in the current version of Part 1 of the Model Form` (+1 more) |
| 693-694 | O 8 r 4A(4)(d) | ( d ) a copy each of the request and the documents mentioned in sub-para... | encoded | `o 8 r 4A(4)(d) the copies may be in electronic form` |
| 695 | O 8 r 4A(5) | (5) The Registrar must send the documents filed under paragraph (4) to t... | encoded | `o 8 r 4A(5) the Registrar must send the documents to the central authority` (+1 more) |
| 696 | O 8 r 4A(6) | (6) Rule 2(3) does not apply in relation to any service under this Rule. | encoded | `o 8 r 4A(6) Rule 2(3) applies to the service` |
| 697 | O 8 r 4A(7) | (7) In this Rule — | encoded | `o 8 r 4A(7) an authority is a central authority` (+3 more) |
| 697 | O 8 r 4A(7) “central authority” | “central authority”, in relation to a Contracting State, means an author... | encoded | `o 8 r 4A(7) an authority is a central authority` (+3 more) |
| 698 | O 8 r 4A(7) “Contracting State” | “Contracting State” means a State (other than Singapore) which is a part... | encoded | `o 8 r 4A(7) an authority is a central authority` (+3 more) |
| 699 | O 8 r 4A(7) “Hague Service Convention” | “Hague Service Convention” means the Convention on the Service Abroad of... | encoded | `o 8 r 4A(7) an authority is a central authority` (+3 more) |
| 700 | O 8 r 4A(7) “Model Form” | “Model Form” means the model form, in 3 parts, annexed to the Hague Serv... | encoded | `o 8 r 4A(7) an authority is a central authority` (+3 more) |
| 701 | O 8 r 5 [heading] | Service of originating process on High Contracting Party to Warsaw Conve... | inert, reason 1 | heading: not operative |
| 702 | O 8 r 5(1) | 5. —(1) Upon obtaining the Court’s approval under Rule 1(2), a person wh... | encoded | `o 8 r 5(1) the person must file in the Registry the request, the sealed copy and the translation` (+1 more) |
| 702-703 | O 8 r 5(1)(a) | ( a ) a request for the Ministry of Foreign Affairs to arrange service; | encoded | `o 8 r 5(1) the person must file in the Registry the request, the sealed copy and the translation` (+1 more) |
| 704-705 | O 8 r 5(1)(b) | ( b ) a sealed copy of the originating process; and | encoded | `o 8 r 5(1) the person must file in the Registry the request, the sealed copy and the translation` (+1 more) |
| 706-707 | O 8 r 5(1)(c) | ( c ) a translation of the originating process in the official language ... | encoded | `o 8 r 5(1) the person must file in the Registry the request, the sealed copy and the translation` (+1 more) |
| 708 | O 8 r 5(2) | (2) Every translation filed under paragraph (1)( c ) must be certified b... | encoded | `o 8 r 5(2) the translation is certified as required` |
| 709 | O 8 r 5(3) | (3) The serving party must engage a solicitor for the purposes of filing... | encoded | `o 8 r 5(3) the serving party must engage a solicitor` (+1 more) |
| 710 | O 8 r 5(4) | (4) The Registrar must send the documents filed under paragraph (1) to t... | encoded | `o 8 r 5(4) the Registrar must send the documents to the Ministry of Foreign Affairs` (+1 more) |
| 711 | O 8 r 6 [heading] | Service of process on foreign State (O. 8, r. 6) | inert, reason 1 | heading: not operative |
| 712 | O 8 r 6(1) | 6. —(1) Upon obtaining the Court’s approval under Rule 1(2), a person wh... | encoded | `o 8 r 6(1) the person must file in the Registry the request, the sealed copy and the translation` (+1 more) |
| 712-713 | O 8 r 6(1)(a) | ( a ) a request for the Ministry of Foreign Affairs to arrange service; | encoded | `o 8 r 6(1) the person must file in the Registry the request, the sealed copy and the translation` (+1 more) |
| 714-715 | O 8 r 6(1)(b) | ( b ) a sealed copy of the originating process; and | encoded | `o 8 r 6(1) the person must file in the Registry the request, the sealed copy and the translation` (+1 more) |
| 716-717 | O 8 r 6(1)(c) | ( c ) a translation of the originating process in the official language ... | encoded | `o 8 r 6(1) the person must file in the Registry the request, the sealed copy and the translation` (+1 more) |
| 718 | O 8 r 6(2) | (2) Every translation filed under paragraph (1)( c ) must be certified b... | encoded | `o 8 r 6(2) the translation is certified as required` |
| 719 | O 8 r 6(3) | (3) The serving party must engage a solicitor for the purposes of filing... | encoded | `o 8 r 6(3) the serving party must engage a solicitor` (+1 more) |
| 720 | O 8 r 6(4) | (4) The Registrar must send the documents filed under paragraph (1) to t... | encoded | `o 8 r 6(4) the Registrar must send the documents to the Ministry of Foreign Affairs` (+1 more) |
| 721 | O 8 r 6(5) | (5) Where section 14(6) of the State Immunity Act applies and the State ... | encoded | `o 8 r 6(5) the originating process may be served by that method` |
| 722 | O 8 r 6(6) | (6) Where the State is a Contracting State to the Hague Service Conventi... | encoded | `o 8 r 6(6) the request must be accompanied by a summary of the document` (+1 more) |
| 723 | O 8 r 6(7) | (7) In paragraph (6), “Contracting State”, “Hague Service Convention” an... | encoded | `o 8 r 6(7) the term in paragraph (6) has the meaning given by Rule 4A(7)` |
| 724 | O 8 r 7 [heading] | Undertaking to pay expenses of service (O. 8, r. 7) | inert, reason 1 | heading: not operative |
| 725 | O 8 r 7(1) | 7. —(1) The solicitor for the serving party must give an undertaking in ... | fork F9 | `o 8 r 7(1) the duty` (+2 more) |
| 725 | O 8 r 7(2) | (2) Upon request to pay the expenses whether before or after the service... | encoded | `o 8 r 7(2) the duty` (+3 more) |
| 726 | O 8 r 8 [heading] | Certificate of service (O. 8, r. 8) | inert, reason 1 | heading: not operative |
| 727 | O 8 r 8 | 8. An official certificate or letter by the agency or person who effecte... | encoded | `o 8 r 8 the certificate or letter is evidence of the service and its date` |

## Fork register (roc1)

Status header (verification): the rulings below are copied word for word from BRIEF.md lines 70-77 by a script (`work/notesgen.py` reads the file and prints the four bullets).
The forks F1 to F19 and G1 were found by reading the text and the layer-1 code in this run (F12 to F19 after an independent test author's scenarios came back); each names the L4 function that carries the reading taken, or the sites it covers.
A fork row in the coverage table points here by its id.
"Taken" is the reading the code follows; "other" is the reading it does not.
Nothing here is ruled by Meng except the four bullets at the top; every F-entry is an assumption for a lawyer to confirm.

### The rulings that bind this row (word for word from BRIEF.md)

- **E1** (bench `commons-negation-1030`; should a legal effect be one definition gathered from every section that gives it?): option B, as guidance for gathering a legal effect's routes by hand only, with no pilot run; option A (gathering by bare name) is withdrawn as a direction for the language, not deferred; option C (per-section answers) applies everywhere else; the Magna Carta pilot in the printed recommendation (chapters 2, 3, 4, 5, 37, 43, 46 and 53, with a blind second reader) is not to be run. Meng's lean, verbatim: "B but generally uncomfortable with this much magic because it takes the language from unopinionated to opinionated in ways that are hard to teach an l4 novice." Meng's note, verbatim: "Fundamentally I feel like we are trying to make the language do work that the human l4 drafter should do. Too much magic. Can’t we just decline to be this opinionated and say the programmer needs to do this thinking?" Marked 2026-11-03T23:19:02.812Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
- **N2** (bench `commons-negation-1030`; does a flat negative count as the text's no?): option A as printed: flat negatives count as a no, and where the text names the bearer the prohibition (`SHANT`) is derived from that answer; the Hohfeld kinds stay in each row's "Jural relations" table; option C's wording (the kind typed in the person-facing answer) comes only after a lawyer confirms the typing, decided together with the S/E choice for how "not covered" is said. Meng's lean, verbatim: "Why are we even trying to do this work? Some of these rules are metatextual and require more homoiconicity than we currently have in L4." Meng's note: none written. Marked 2026-11-03T23:22:49.971Z, ruled 2026-11-04. Bench: https://claude.ai/artifact/49q6k2H5xtuJqy5ttkwZ23
- **Periods, "where" and scope limits** (a question raised on 2026-11-05 while checking an encoding of the Retirement and Re-employment Act 1993, not a bench): (a) a period the text fixes in its own words ("within one month", "begins from ... until the employee attains the age", "on the last day of employment"): outside the period the answer is `JUST FALSE`; (b) a "where ..." condition: when it fails the answer is `JUST FALSE`; (c) a scope limit with no "only" (for example "below" the minimum age): outside the scope the answer is `NOTHING`. Meng's words, verbatim apart from the trigger word that ended the message: "i agree with your lean: no for a and b; nothing for c." Typed 2026-11-05T04:30:00.322Z, ruled 2026-11-05.
- **Delegated definitions, defences and "until" bars** (questions raised on 2026-11-05 while checking encodings of the Proceeds of Crime Act 2002, the Terrorism Act 2000 and the Singapore Sale of Goods Act 1979, not a bench): (a) a definition the text itself hands to a list ("Schedule 9 has effect for determining what is a business in the regulated sector"): when no head in the list holds, the answer is `JUST FALSE`; a bare list with no such hand-off still answers `NOTHING`; (b) "it is a defence ... to prove that X": when X is not proved, the answer is `JUST FALSE` for that provision's defence, worded "this section gives no defence on these facts" and never "no defence at all"; (c) "when", "upon" and "whenever" count as "where" under rule (b) of the periods ruling above; (d) "the property does not pass until X": encode the bar ("the property cannot yet pass": `JUST TRUE` before X, `JUST FALSE` after X) and never claim that the property has passed. Meng approved these four readings as put to him by the general-manager session, in the word NOTHINGBURGER; his note on (d), verbatim apart from the bracket and the trigger word that ended the message: "in the case of Q5 [the "until" bar] i hope we are using the deontic mechanisms to examine a trace." The note is a request about how (d) is modelled, not part of the ruling. Typed 2026-11-05T06:04:54.553Z, ruled 2026-11-05.

The two rulings of 2026-11-05 in my words, with the times Meng typed them (the bullets above are the guide's text, and the lead may replace them with its exact copy):
- Typed 04:30:00.322Z, periods and "where": outside a period the text fixes in its own words the answer is JUST FALSE; a "where ..." condition that is not met is JUST FALSE, like "if"; a scope limit with no "only" is NOTHING outside the scope.
- Typed 06:04:54.553Z, delegated definitions, defences and "until" bars: a definition the text hands to a list is JUST FALSE when no head holds, and a bare list stays NOTHING; "it is a defence ... to prove that X" is JUST FALSE for that provision's defence when X is not proved; "when", "upon" and "whenever" count as "where"; "does not pass until X" is asked as a yes/no bar (JUST TRUE before X, JUST FALSE after X) and never claims the thing has happened.
- Assumed, not ruled, in this range: "once" and "in the event of" count as "where"; a function that returns a number, a date or a record cannot carry JUST FALSE, so where a ruling calls for a no there is a yes/no twin (fork F18).

### Forks taken

**F1. O 3 r 3(7): a deadline counted backwards also moves to the next court day.**
- Text: r 3(7) "Where the time prescribed by these Rules, or by any judgment, order or direction, for doing any act expires on a non‑court day, the act is in time if done on the next day, not being a non‑court day"; r 3(4) "within or not less than a specified period before a specified date, the period ends immediately before that date".
- Taken: r 3(7) is read literally, so a last day found by counting backwards from a date ("not less than 14 days before the hearing") that falls on a non-court day moves forward to the next court day, which is later than the stated last day.
- Other: r 3(7) moves only deadlines counted forwards; a deadline counted backwards stays where it is, because moving it forward lets the party act later than "not less than" allows.
- Licence: r 3(7) says "any act" and "expires", with no direction; nothing in r 3(4) excepts it.
- What the literal reading does to the notice: a deadline of "not less than 10 days before" Tuesday 17 Nov falls on Saturday 7 Nov and moves LATER to Monday 9 Nov, so the notice that satisfies the Rule can be 8 days instead of 10, which is less than the minimum the text states.
- Carried by: `o 3 r 3(7) the last day moved past non-court days`, applied in both directions inside `o 3 r 3 the last day for doing the act`; tested in `roc1-tests-order-3-time.l4` ("14 days before Monday 7 Dec is Monday 23 Nov, the fixture holiday: Rule 3(7) moves it to Tuesday 24 Nov"); the two sides of the rule are pinned there: 10 days before Tuesday 17 Nov is Saturday 7 Nov and moves to Monday 9 Nov (an act done on 9 Nov is in time, on 10 Nov is not), and 10 days before Monday 16 Nov is Friday 6 Nov, a court day, which stays.

**F2. O 3 r 3(5): "clear days" after a date state a minimum gap, not a period.**
- Text: r 3(5) "Where an act is required to be done a specified number of clear days before or after a specified date, at least that number of days must intervene between the day on which the act is done and that date."
- Taken: for clear days AFTER a date the rule fixes the earliest day the act may be done; `o 3 r 3 the last day for doing the act` returns that earliest day (a DATE cannot say "no last day") and `o 3 r 3 the first day on which the act may be done` returns the same day; `o 3 r 3 the act is in time` answers JUST FALSE for an act before that day (the minimum gap is a bar the text states in its own words, ruling of 2026-11-05 (a)) and JUST TRUE on or after it (changed in the period audit; before it, the function answered NOTHING on both sides).
- Other reading: JUST FALSE before the earliest day as taken, and NOTHING on or after it (the answer before the period audit, on both sides), because r 3(5) gives no period within which the act must be done and no last day, so "in time" has nothing to be tested against once the gap is met. JUST TRUE on or after it was taken so that the function says yes where the minimum is met, as the until-bars do. The DATE functions cannot say "no last day", which is why the yes/no function carries the answer.
- Licence: r 3(5) says "at least that number of days must intervene", which is met by every later day.
- Carried by: the two DATE functions above and the clear-days-after branch of `o 3 r 3 the act is in time` (tested on both sides of 13 November).
- No rule in Orders 2 to 8 uses clear days after a date (grep of the range: 0 hits); other parts will meet it.

**F3. O 3 r 2(4)(e): how the $50 a day counts.**
- Text: "impose a late filing fee of $50 for each day that a document remains unfiled after the expiry of the period within which the document is required to be filed, excluding non‑court days".
- Taken: the fee is $50 times the number of court days after the last day for filing, up to and including the day the document is filed.
- Other: the day of filing is not counted (the document is no longer "unfiled" on it); or the day after expiry is the first day only when the period expired at the end of the day.
- The power itself, `o 3 r 2(4)(e) the Court may impose a late filing fee`, answers NOTHING for a document that was not required within a period or has not stayed unfiled after it expired: the fee is the power's own limit ("for each day that a document remains unfiled after the expiry"). Other reading: JUST FALSE for a document filed in time.
- Reviewer's reading of the same sentence (A2) is the one taken: the court days are counted from the day after expiry to the filing day inclusive.
- Carried by: `o 3 r 2(4)(e) the number of court days of delay` and `o 3 r 2(4)(e) the late filing fee the Court may impose`; the power itself is `o 3 r 2(4)(e) the Court may impose a late filing fee`.

**F4. O 7 r 1(1)(b) and O 6 r 4: may an originating claim be served by ordinary service.**
- Text: O 7 r 1(1) "Any document that is required to be served under these Rules may be served by way of ... (b) ordinary service"; O 6 r 4 "Subject to the provisions of any written law and these Rules, an originating claim or an originating application must be served personally on each defendant".
- Taken: option C of ruling E1 (each section answered on its own words): `o 7 r 1(1)(b) a document may be served by ordinary service` says yes for any document required to be served; `o 6 r 4 the originating claim or originating application is served personally on the defendant as required` says an originating process must be served personally; no function combines them.
- Other: O 6 r 4 is the specific rule and displaces r 1(1)(b) for originating process (so ordinary service of an originating claim is not allowed); or r 1(1)(b) is one of "these Rules" to which r 4 is "subject".
- Carried by: `o 7 r 1(1)(b) a document may be served by ordinary service`, `o 6 r 4 the originating claim or originating application is served personally on the defendant as required`.

**F5. O 6 r 1(2) and r 1(3): both mandatory modes can hold at once.**
- Text: r 1(2) "A claimant must commence proceedings by an originating claim where the material facts are in dispute"; r 1(3) "A claimant must commence proceedings by an originating application where ... (c) the proceedings concern solely or primarily a question of law ...".
- Taken: where r 1(2) and r 1(3)(a), (b) or (c) both hold, the text does not choose; `o 6 r 1 how the claimant commences proceedings` returns the explicit value `o 6 r 1 the text does not choose between the two modes` (hand-gathered, ruling E1 option B).
- Other: r 1(3) prevails because it is the more specific; or r 1(2) prevails because a dispute of fact needs a trial.
- Carried by: `o 6 r 1 how the claimant commences proceedings`; the paragraphs are also answered on their own (`o 6 r 1(2) the claimant must commence proceedings by an originating claim`, `o 6 r 1(3) the claimant must commence proceedings by an originating application`).

**F6. O 4 r 3(6) "Court": the heads overlap and no precedence is stated.**
- Text: "Court" means (a) the Court of Appeal if the matter is (i) a matter, proceeding or appeal mentioned in paragraph (5)(a), or (ii) an appeal mentioned in (5)(c), (e) or (f) to the Court of Appeal for which no permission has been given by a court below; (b) the Appellate Division ...; (c) the General Division, if the matter is (i) a matter, proceeding or appeal mentioned in (5)(c) ...
- Taken: an appeal from a General Division matter to the Court of Appeal, with no permission given below, is within both (a)(ii) and (c)(i); `o 4 r 3(6) the number of heads of the definition of Court that hold` counts the heads and `o 4 r 3(6) the Court is that court` answers JUST TRUE for each head that holds and says nothing about precedence.
- Second instance: an appeal from a Magistrate's Court to the General Division, with no permission given below, is within head (c)(ii) (an appeal mentioned in (5)(e) or (f) to the General Division) and within head (f) (a Magistrate's Court, for a matter or appeal mentioned in (5)(f)); the text does not pick one.
- Other: head (a) prevails because the appeal is to the Court of Appeal; or head (c) prevails because the matter was commenced in the General Division; for the second instance, head (c)(ii) prevails because the appeal is to the General Division, or head (f) prevails because the matter is a Magistrate's Court matter.
- Reviewer expected JUST FALSE; open question.
- Carried by: the functions named above.

**F7. O 4 r 6(5): which lists bind.**
- Text: r 6(5) "A judgment or order given in such an action is binding on all the persons and the class named in the respective lists stated in paragraphs (3) and (4)."
- Taken: the judgment binds the persons in the lists of paragraphs (3) and (4), and the text says nothing of the list of claimants of paragraph (2).
- Other: the list of paragraph (2) is also meant ("such an action" is any representative action).
- Carried by: `o 4 r 6(5) the judgment or order is binding on the person or class`.

**F8. O 8 r 2(1): methods of service only where approval was obtained.**
- Text: r 2(1) "Where the Court's approval has been obtained under Rule 1(2), service ... may be effected out of Singapore in the following manner"; r 1(3) and (4) say approval is not required in two cases.
- Taken: the list of methods is given where approval was obtained under r 1(2); where approval was not required (r 1(3), (4)) the text gives no method list, so `o 8 r 2(1) service out of Singapore may be effected in that manner` answers JUST FALSE under the "where" ruling (b).
- Other: the list of methods applies to every service out of Singapore, with or without approval.
- Carried by: `o 8 r 2(1) service out of Singapore may be effected in that manner` and `o 8 r 1 the Court's approval is not required to serve the document out of Singapore`.

**F9. O 8 r 7(1): the undertaking has no stated trigger or time.**
- Text: "The solicitor for the serving party must give an undertaking in writing to the Ministry of Foreign Affairs, the Registrar and the serving authority or person in the foreign country to pay all expenses incurred in effecting the service requested."
- Taken: the duty arises when service out of Singapore under the Order has been requested (an input); the text names no time for giving the undertaking, so the duty has no WITHIN.
- Other: the undertaking is given before the request is made, or with the request filed under r 5(1) or r 6(1).
- Carried by: `o 8 r 7(1) the solicitor for the serving party must give an undertaking in writing`, `o 8 r 7(1) the solicitor has given the undertaking in writing as required`, and the duty in `roc1-duties.l4`.

**F10. O 7 r 8: service at exactly 5 p.m.**
- Text: r 8(1) "when service is effected before 5 p.m. on any particular day, service is deemed to have been effected on that day"; r 8(2) "When service is effected after 5 p.m. ... the following day".
- Taken: at exactly 5 p.m. (1,020 minutes after midnight) neither limb applies; `o 7 r 8 the day service is deemed effected` answers NOTHING (a date cannot say no), and its yes/no twin `o 7 r 8 this Rule deems the day of service` answers JUST FALSE, because both "when" conditions are unmet and "when" counts as "where" (ruling of 2026-11-05 (c), applied to the twin in this pass; before it, the twin passed the NOTHING straight through).
- Other: 5 p.m. is "before" 5 p.m. (the working day ends at 5 p.m.); or it is "after".
- Carried by: the function named above and `o 7 r 8 this Rule deems the day of service`; tested at 1,019, 1,020 and 1,021, and in the seat (`Under Order 7, rule 8, does this Rule deem the day of service`).

**F11. O 2 r 9(10): where the 14 days before the trial start.**
- Text: "no application may be taken out during the period starting 14 days before the commencement of the trial and ending when the Court has made its decision".
- Taken: the period starts on the day 14 days before the first day of the trial (that day is inside it), counted back with `o 3 r 3(4) the first day of a window within a period before a date`; the end is the day of the decision.
- Other: the period starts the day after that (the 13th day before), by analogy with r 3(3) "begins immediately after that date".
- Reviewer's note on the same sentence (A4): does the window start on the trial date minus 14, inclusive; the reading taken is yes (the first day of the window is the sixth for a trial on the twentieth), and the last day is the day of the decision, also inclusive.
- Outside the period the answer to "may an application be taken out" is NOTHING (the flat negative says nothing of other days); the period itself is a yes/no, `o 2 r 9(10) the day falls in the period in which no application may be taken out`, which is JUST FALSE outside it (ruling of 2026-11-05 (a); added in this pass).
- Other reading of the function that asks whether an application MAY be taken out: ruling (a) applied to it directly, so that outside the period it answers JUST FALSE. Not taken, because it would forbid every application outside the window; the period function above is where ruling (a) is applied.
- Carried by: `o 2 r 9(10) an application may be taken out on that day` and the period function above.

**F12. O 4 r 2(2) with r 2(1)(a): a person aged 18 to 20 without section 36 of the Civil Law Act.**
- Text: r 1 "The following may be parties to proceedings in their own name ...: (a) a person who is 18 years of age or older but below 21 years of age and where section 36 of the Civil Law Act applies; (b) a person who is 21 years of age or older; (c) any entity with the capacity to sue or be sued"; r 2(1)(a) "The following persons must be represented by a litigation representative in proceedings: a person who is below 21 years of age and who does not come under Rule 1( a )"; r 2(2) "A litigation representative must be a person who can be a party to proceedings in his or her own name."
- The question (scenario S104): may a 19-year-old to whom section 36 does not apply be a litigation representative?
- Taken: NOTHING. r 1 has no "only", so it does not say that a person outside its three heads cannot be a party in their own name; r 2(1)(a) says such a person "must be represented", and "must be represented" is not the text saying in its own words that the person cannot be a party in their own name (no "shall not", "may not" or "only"). The function answers JUST TRUE for a person who comes under r 1 and NOTHING for anyone else.
- Other: JUST FALSE, reading r 1 as the whole list of who may be a party in their own name, with r 2(1)(a) drawing its line at "does not come under Rule 1(a)".
- reviewer expected JUST FALSE; open question.
- Carried by: `o 4 r 2(2) the person can be a litigation representative`, tested with a person aged 19 (`o 4 test aged 19`).

**F13. "Unless", "except" and "without approval": does a lift that is met grant a permission, or only lift the bar?**
- Taken: a lift that is met only lifts the bar, so the answer is NOTHING (the text does not then say the thing is allowed); a bar whose lift is not met is JUST FALSE (a flat negative, ruling N2).
- Other: a lift that is met grants the permission, so the answer is JUST TRUE (or, for a requirement lifted, no requirement).
- Meng has not ruled this. The five sites the independent test author named, with the encoding's answer and what that author expected:
  - O 2 r 9(8) (scenarios S29, S31, S33, S34, S35 and seat S29), `o 2 r 9(8) the application may be taken out`: NOTHING for an application directed at the case conference or approved by the Court, and NOTHING for each of the fifteen listed applications; reviewer expected JUST TRUE; open question.
  - O 2 r 9(10) (S39), `o 2 r 9(10) an application may be taken out on that day`: NOTHING inside the period for a special case with the trial Judge's approval; reviewer expected JUST TRUE; open question.
  - O 5 r 1(4) (S147), `o 5 r 1(4) the party may reject an offer of amicable resolution`: NOTHING where the party has reasonable grounds to reject; reviewer expected JUST TRUE; open question.
  - O 5 r 2(2) (S151), `o 5 r 2(2) the offer is open for acceptance as required`: NOTHING where the parties otherwise agree; reviewer expected JUST TRUE; open question.
  - O 5 r 2(4) (S155), `o 5 r 2(4) the offer has expired under this paragraph`: NOTHING where the offeror has stated otherwise; reviewer expected JUST FALSE; open question. This is the strongest of the five, and r 2(4) was re-read for it: "Any offer of amicable resolution which does not state an expiry date expires once the Court has determined the merits of the action or appeal to which it relates unless the offeror has stated otherwise." The function asks whether the offer has expired UNDER THIS PARAGRAPH. On that scoping, a met "unless" means the paragraph does not expire the offer, and the question has no answer but no: the scope reading holds, and it points to JUST FALSE, not NOTHING. NOTHING would be right only for the wider question "has the offer expired by any route", which this function does not ask. The other NOTHING at the same site ("the offer states an expiry date") is a scope limit of the paragraph ("which does not state an expiry date") and stays NOTHING under ruling (c). Not changed here, because the same shape stands at the sites below and the choice is one for all of them together.
- The same shape stands at these sites, which the independent author did not name; found by a script over the NOTHING-kind comments that say "lifts": O 2 r 6(7)(b) (`o 2 r 6(7)(b) a further affidavit may be filed`), O 2 r 9(3), O 2 r 9(4), O 2 r 10(10), O 2 r 10(11), O 2 r 12(10), O 3 r 5(6), O 4 r 4(3), O 4 r 8(2) (the bar `o 4 r 8(2) the deeming of the solicitor cannot yet end`, "Unless notice is given"), O 4 r 9(2) (the service of the summons), O 5 r 1(2), O 6 r 3(4) (F15), O 6 r 5(4), O 6 r 12(6); and, with "except where", O 8 r 2(4) (the compliance function, NOTHING where the official language is English). A decision on this fork should sweep all of them.
- Not the same shape: O 2 r 10(7) "Save for appeals filed under Divisions 2 and 4 of Order 18, the appellant has to provide security" lifts a DUTY, not a bar, and answers JUST FALSE for those appeals.

**F14. "Other than": the text's no, or a scope limit?**
- Taken: not one reading. Two sites are read as scope limits (NOTHING outside) and one as the text's no (JUST FALSE for the excluded case).
- O 8 r 4A(1) "on a person, other than a State, in a Contracting State": JUST FALSE for a State. The other reading: a State is outside the Rule (O 8 r 6 is the Rule for a State), so NOTHING. This site passed the independent author's assertions.
- O 4 r 3(4) "an unincorporated association (other than a partnership or a registered trade union)" (S113): NOTHING for a partnership, as a scope limit. The other reading: JUST FALSE, because "other than" is the text's own exclusion. reviewer expected JUST FALSE; open question.
- O 8 r 4(1) "any jurisdiction (other than Malaysia or Brunei Darussalam)" (S249): NOTHING for service in Brunei Darussalam, as a scope limit (O 8 r 3 is the Rule for Malaysia and Brunei). The other reading: JUST FALSE. reviewer expected JUST FALSE; open question.
- The three are not answered alike. Meng has not ruled this; making them alike is a decision for the lead.
- Carried by: `o 8 r 4A(1) this Rule applies to the service`, `o 4 r 3(4) the Court may give permission for an officer to act on behalf of the unincorporated association`, `o 8 r 4(1) the Registrar of the State Courts must send the originating process to the Registrar of the Supreme Court` and its (a) and (b).

**F15. The limits of an extension: "once", "only twice", "a maximum".**
- O 3 r 4(3) "may be extended once by consent in writing for a maximum period of 14 days without an order of the Court" (scenarios S81 to S83): JUST TRUE for a first extension by consent in writing of up to 14 days; NOTHING for a second extension, an oral consent, or 15 days, because "once" and "a maximum" have no "only" (ruling (c)). Other reading: JUST FALSE, because the text fixes the limit in its own words (ruling (a)). reviewer expected JUST FALSE; open question. The word "once" here is a count, not a trigger, so the "once" as "where" assumption of F18 does not touch it.
- O 6 r 3(4) "Except in a special case, the Court may extend the validity ... only twice and by not more than 3 months each time": JUST FALSE for a third extension, or one of more than 3 months, when it is not a special case, because the text says "only". reviewer expected JUST FALSE; open question.
- O 6 r 3(4) in a special case: NOTHING. Readings: a third extension (or a longer one) is then permitted, or it is only not barred; not asserted either way, and it is the F13 shape. reviewer expected JUST FALSE; open question.
- Why the two differ: O 6 r 3(4) says "only twice" and "not more than", a closed limit with "only" and a negative cap, so a third or longer extension is JUST FALSE; O 3 r 4(3) says "may be extended once ... for a maximum period of 14 days", a grant whose limit is its own wording with no "only" and no negative, so a second or longer extension is NOTHING. The other reading is the same answer at both sites: both JUST FALSE, or both NOTHING.
- Carried by: `o 3 r 4(3) the period may be extended by consent in writing without an order of the Court` and `o 3 r 4 the last day as extended or shortened` (the date, which cannot say no); `o 6 r 3(4) the Court may extend the validity`.

**F16. Counting readings the independent author recorded (A1, A3, A5; A2 is F3 and A4 is F11).**
- A1. O 6 r 3(1) "for 6 months beginning with the date of its issue" (and the 3-month limb): the day of issue is the first day, so the last day is the day before the corresponding date (issued 5 November 2026: 4 February 2027 for 3 months and 4 May 2027 for 6 months). The other reading: the period ends on the corresponding date. Carried by `o 6 r 3(1) the last day of validity for service`; finding 3 below.
- A1, the month-end case: when the later month has no corresponding day (issued 31 August 2026, 3 months) the Rules do not give the last day, so `o 6 r 3(1) the originating claim or originating application is valid for service on the day` answers NOTHING for every day asked about, including a day long after any reading of the end. The text does not fix the period in that case, so it is not an outside-the-period NOTHING under ruling (a). Other reading: bracket the end between the clamped month end and the first of the next month, and answer JUST TRUE before the bracket and JUST FALSE after it.
- A3. O 3 r 5(4) "at least 14 days before the hearing of the summons": service on the day 14 days before the hearing is in time (hearing 30 November, served 16 November: in time; 17 November: not). The other reading: "at least 14 days" means 14 clear days, so the 15th day before. Carried by `o 3 r 5(4) the summons and the affidavit are served at least 14 days before the hearing`.
- A5. O 6 r 6(7) and r 7(8) "computed from the date of the originating process to the date on which judgment is given, at the rate of 5.33% per year": simple interest, with the length of that period given by the asker in years because the Rules state no day count. The other readings: compound interest, or a day count of 365 or of the actual year. Carried by `o 6 r 6(7) the interest the Court may direct` and `o 6 r 7(8) the interest the Court may direct`.

**F17. A subject named by a relative clause, or a scope opened by "in doing X".**
- Text: "A defendant who is served an originating claim with a statement of claim has to file and serve a notice" (O 2 r 4(1)); "A defendant who wishes to contest" (O 2 r 5(1)); "A party to any proceedings" (O 5 r 1(1)); "The claimant" (O 2 r 3(2)); "In exercising any power" (O 3 r 2(3)); "In deciding whether to exercise its power under paragraph (1)" (O 5 r 3(2)); "In any action brought against the estate of a deceased person" (O 4 r 4(2)); and many more.
- Taken: each is a scope limit with no "only" (ruling (c), the ruling's own example is "an employee of" an employer), so outside the scope the answer is NOTHING. The reading-B rows of the marginal-readings table below (176 of them) are these branches and the flat negatives that reach their own words only.
- Other: such a clause is a condition, ruling (b), and outside it the answer is JUST FALSE.
- Why this is a fork and not a ruling: ruling (b) names "where"; "who is served", "who wishes" and "in doing X" are not in it, and ruling (c)'s examples are of the same grammatical shape as the first. The sweep for this pass looked at every such branch (see the decision table below) and did not find one to move.

**F18. Assumed, not ruled: "once", "in the event of", and the yes/no twins.**
- "once" as a trigger: O 5 r 2(4) "expires once the Court has determined the merits" is read as "where": merits not determined, JUST FALSE. The other use of "once" in the range, O 3 r 4(3) "extended once", is a count and is F15.
- "in the event of": no occurrence in lines 137 to 727 (grep). "whenever": none. "upon" and "when" are in the 2026-11-05 ruling and are read as "where": for example O 8 r 5(1) and r 6(1) "Upon obtaining the Court's approval", O 8 r 7(2) "Upon request", O 2 r 2(1), O 6 r 6(6) and O 7 r 8 "when".
- A function that returns a number, a date or a record cannot say JUST FALSE, so where a ruling calls for a no there is a yes/no twin beside it: `o 7 r 8 this Rule deems the day of service` (the day, changed in this pass: it now answers JUST FALSE at exactly 5 p.m.); `o 2 r 9(10) the day falls in the period in which no application may be taken out` (the period, added in this pass); `o 3 r 3 the act is in time` and `o 3 r 3 the period can be counted under this Rule` (the last day); `o 6 r 3(1) the originating claim or originating application is valid for service on the day` (the last day of validity); `o 5 r 2(2) the offer is open for acceptance as required` (the number of days); `o 6 r 6(7) the Court may direct the payment of interest` and `o 6 r 7(8) the Court may direct the payment of interest` (the rate and the sum); `o 2 r 10(7) the appellant has to provide security for the costs of the appeal` and `o 2 r 12(8) the appellant has to provide security for the costs of the appeal` (the number of sets); `o 3 r 1(2) the objective is one of the Ideals` (the number of Ideals).

**F19. A duty that does not arise: a note for the merge.**
- A duty in this range can have up to three functions: the "must" function (does the duty exist), the compliance function (has it been done as required), and, for a timed duty, the in-time function.
- The "must" function answers JUST FALSE when a trigger of the duty ("if", "where", "when", "upon") is unmet (rulings (b) and (c)), and NOTHING when the bearer is outside the class the paragraph names (F17). For example `o 6 r 12(1) the defendant must file and serve the defendant's affidavit` (added in this pass), `o 7 r 4(3) the claimant must send a copy of the order and of the document to the principal's overseas address` (added in this pass), `o 4 r 8(1) the party must file and serve a notice of appointment of solicitor in Form 3 on all the parties`.
- "The duty does not arise" is therefore answered through the companion "must" function, not through the compliance function. A compliance function (for example `o 4 r 8(1) the party has given the notice of appointment as required`, `o 8 r 5(1) the person has filed in the Registry what the Rule requires`) answers NOTHING when the duty did not arise, and never JUST TRUE.
- One exception to say plainly: the timed functions that fold an "if" into the timing question (`o 6 r 12(1)` and `(2)` "within 21 days" and "within 5 weeks", `o 7 r 4(3) the claimant has sent the copy to the principal as required`, `o 3 r 5(5)`, `o 6 r 5(6)` and `(7)`, `o 6 r 11(4)` and `(5)`) answer JUST FALSE when the "if" is unmet, because they state the Rule's own words ("if the defendant wishes to introduce evidence ... within 21 days") and ruling (b) makes an unmet "if" a no. So two shapes sit side by side in this range, and a merged encoding that wants one shape has to choose; this is not ruled.
- Where a paragraph names a duty and only the compliance function exists (no "must" function), the duty not arising is answered by the compliance function's NOTHING alone; the lead may want a companion there.

### Gathered functions (ruling E1, option B, by hand)

**G1.** These functions gather several sections' answers into one for a reader, in plain L4, with no language construct: `o 6 r 1 how the claimant commences proceedings` (r 1(1) to (3)); `o 6 r 6 the notice of intention to contest or not contest is filed and served in time` (r 6(1) or (2), by place of service); `o 6 r 7 the defence is filed and served in time` (r 7(1) or (2)); `o 6 r 12 the defendant's affidavit is filed and served in time` (r 12(1) or (2)); `o 8 r 1 the Court's approval is not required to serve the document out of Singapore` (r 1(3), (4)); `o 4 r 1 the person may be a party to proceedings in their own name` (r 1(a) to (c)); `o 4 r 2(1) the person must be represented by a litigation representative` (r 2(1)(a), (b)); `o 4 r 3(1) the person must be represented by a solicitor` (r 3(1)(a), (b)).
Each section's own answer is also encoded on its own (option C), so a reader can use either.

### The second pass: what an independent test author's scenarios changed

Status header (verification): every change below is pinned by an assertion in the tests file named beside it, and the whole folder was run by `check.sh` on both builds after the last edit (output at the end of this file).
"Changed" is an answer that moved; "added" is a new function; "left alone" is a site read again and not moved.
Nothing here is a ruling by Meng except where a ruling of 2026-11-05 is cited.

**Changed answers.**
1. `o 4 r 9(1) the solicitor is still considered the solicitor of the party` (tests-order-4): the "Where" of the paragraph unmet, NOTHING to JUST FALSE (ruling (b); the same condition already answered JUST FALSE in `o 4 r 9(1) the solicitor may apply to the Court for an order declaring that the solicitor has ceased to act`).
2. `o 7 r 8 this Rule deems the day of service` (tests-order-7, and the seat case `Under Order 7, rule 8, does this Rule deem the day of service`): at exactly 5 p.m., NOTHING to JUST FALSE ("when" counts as "where", ruling (c); the twin used to pass the date function's NOTHING straight through). The date function `o 7 r 8 the day service is deemed effected` is unchanged (a date cannot say no).

3. `o 3 r 3 the act is in time` (tests-order-3-time), the clear-days-after branch (period audit, ruling (a)): an act before the earliest day, NOTHING to JUST FALSE; on or after the earliest day, NOTHING to JUST TRUE (fork F2 gives NOTHING inside as the other reading).

**Added.**
- Yes/no and count functions: `o 2 r 6(7)(b) the Court will direct the claimant to file and serve any affidavit in reply`; `o 2 r 9(10) the day falls in the period in which no application may be taken out`; `o 2 r 10(7) the number of sets of respondents for which security is to be provided` and `o 2 r 12(8) the number of sets of respondents for which security is to be provided`; `o 3 r 1(2) the Ideals` and `o 3 r 1(2) the number of Ideals`; `o 4 r 9(1) the notice of having ceased to act is in the Form the text names`; `o 6 r 12(1) the defendant must file and serve the defendant's affidavit` and its `o 6 r 12(2)` twin; `o 7 r 4(3) the claimant must send a copy of the order and of the document to the principal's overseas address`.
- Tests with no function change: a backwards deadline on a Saturday and on a court day (fork F1, tests-order-3-time); a person aged 19 for `o 4 r 2(2)` (fork F12).
- Forks F12 to F19, and sentences added to F1, F3, F6, F10 and F11.

**Left alone, on purpose.** The "unless", "except" and "without approval" lifts (F13); the three "other than" sites (F14); O 3 r 4(3) and O 6 r 3(4) (F15); the head overlap of "Court" (F6); `o 4 r 2(2)` (F12).

**The sweep.** Every NOTHING-kind comment in the layer-1 modules and every opening of "Where", "When", "Upon", "Whenever", "Once", "In the event of", "If", "While", "Unless", "Except" and every period the text fixes in its own words in lines 137 to 727 was read against its function:
- an unmet "if", "where", "when" or "upon" in a function that says what the Rule gives or requires already answered JUST FALSE, apart from the two changes above;
- of the ten NOTHING-kind comments that still quote a "Where", "Upon" or "Unless", nine are compliance functions that answer NOTHING when the duty did not arise (F19) and one is the lift in `o 4 r 8(2) the deeming of the solicitor cannot yet end` (F13);
- every period fixed in the text's own words answers JUST FALSE outside it, in a function whose name says so ("is filed and served within 14 days"); the one period of a prohibition, O 2 r 9(10), now has its own yes/no (above);
- the "until" bars (O 4 r 8(2), O 4 r 9(1), O 5 r 2(3)) were already asked as "is it barred yet" (JUST TRUE before, JUST FALSE after) and never claim that the thing has happened;
- the delegated definition of ruling (a) occurs once in the range, "Ideals" (O 1 r 3(1) to O 3 r 1(2)), already JUST FALSE for an objective not on the list; "it is a defence ... to prove that" does not occur in the range (grep, 0 hits).

## Jural relations (roc1)

Status header (verification): written by reading the text of each provision named; no tool checks a Hohfeld kind.
The kinds are kept here and not in the type of any answer (ruling N2).
A "duty" below is a flat "must" or "has to" with a named bearer; "claim" is its correlative in the person it is owed to.
"Power" is an ability to change a legal position by an act (applying, consenting, ordering); "liability" is its correlative.
"Liberty" is a "may" that is not a power; "disability" is the lack of a power ("cannot ... without the Court's approval"); "immunity" is the correlative of a disability.
"Bearer not named" marks a provision whose actor the text does not name, so no PARTY is written for it.

| provision | kind | held by | against or owed to | content |
| --- | --- | --- | --- | --- |
| O 2 r 3(1); O 6 r 1(1) | liberty | claimant | the Court | commence an action by originating claim or originating application |
| O 2 r 3(2) | duty | claimant | defendant | take reasonable steps to serve the originating claim expeditiously |
| O 6 r 1(2), (3) | duty | claimant | the Court | commence by originating claim where the material facts are in dispute; by originating application in the three cases |
| O 6 r 3(2), (4) | power | an applicant (to apply); the Court (to extend) | defendant (liability) | extend the validity of the originating claim or application for service |
| O 6 r 4 | duty | claimant | each defendant | serve the originating claim or originating application personally |
| O 6 r 5(5) | duty | claimant | defendant | serve the statement of claim within 14 days after the originating claim is served, where generally endorsed |
| O 2 r 4(1); O 6 r 6(1), (2) | duty | defendant | claimant | file and serve a notice of intention to contest or not contest within 14 days (served in Singapore) or 21 days (served out of Singapore) |
| O 6 r 6(5), (6) | power (and duty to file a memorandum of service) | claimant | defendant (liability) | apply for judgment in Form 11 on default or on a notice that the claim is not contested |
| O 6 r 6(4); O 6 r 7(6); O 6 r 12(5); O 2 r 5(4) | immunity | defendant | claimant | filing the notice, defence or affidavit is not treated as submission to jurisdiction |
| O 6 r 7(1), (2); O 2 r 5(1) | duty | defendant | claimant | file and serve a defence within 21 days (Singapore) or 5 weeks (out of Singapore) |
| O 6 r 7(4); O 2 r 5(2) | liberty | defendant | claimant | not file a defence on the merits where challenging jurisdiction, but must file one stating the ground |
| O 6 r 7(7) | power | claimant | defendant (liability) | apply for judgment in default of defence in Form 14 |
| O 6 r 8(1) | duty | defendant | claimant | file and serve the counterclaim with the defence |
| O 6 r 9(1) | duty; liberty | claimant | defendant | file and serve a defence to the counterclaim within 14 days; need not file a reply if merely denying |
| O 6 r 9(3) | power | defendant | claimant (liability) | apply for judgment in default of defence to the counterclaim |
| O 6 r 12(1), (2) | duty | defendant (originating application) | claimant | file and serve an affidavit if the defendant wishes to introduce evidence |
| O 7 r 1(1) | liberty | serving party | the party served | serve personally or by ordinary service |
| O 7 r 1(2) | power | the Court | the parties (liability) | dispense with personal service, ordinary service or service altogether |
| O 7 r 4(3) | duty | claimant | the principal overseas | send a copy of the order and document by prepaid registered post within 14 days after service on the agent |
| O 7 r 7(1) | power | a party | the Court; the party to be served | apply for substituted service |
| O 7 r 7(3) | duty, bearer not named | not named | the Court (order) | effect substituted service within 14 days after the order |
| O 8 r 1(1), (2) | power | claimant (to apply); the Court (to approve) | defendant (liability) | serve out of Singapore with approval |
| O 8 r 1(3), (4) | liberty | the serving party | the Court | serve out of Singapore without approval in the two cases |
| O 8 r 4(1), (2); r 4A(5); r 5(4); r 6(4) | duty | the Registrars; the Registrar | the serving party | send, transmit and forward documents |
| O 8 r 5(1), (3); r 6(1), (3) | duty | the person serving | the Court | file the request, translation and copies; engage a solicitor |
| O 8 r 7(1) | duty | solicitor for the serving party | Ministry of Foreign Affairs, the Registrar, the serving authority | give an undertaking in writing to pay the expenses |
| O 8 r 7(2) | duty | solicitor for the serving party | the requester | pay the expenses within 14 days on request |
| O 4 r 1 | liberty (capacity) | persons 18 or older; entities with capacity | the Court | be parties in their own names |
| O 4 r 2(1) | disability; duty | persons below 21 (not within r 1(a)); persons lacking capacity | the Court | must be represented by a litigation representative |
| O 4 r 2(3) | duty | litigation representative | the person represented | not have an interest adverse to that person |
| O 4 r 3(1) | duty | a person with a litigation representative; an entity | the Court | be represented by a solicitor |
| O 4 r 3(2) | liberty | registered trade union | the Court | be represented by an officer |
| O 4 r 3(3), (4) | power | the Court | the entity (liability) | give permission for an officer to act |
| O 4 r 4(2)(a) | duty | claimant | the Court | apply during the period of validity for an order appointing a representative of the estate |
| O 4 r 5(1) | immunity | the other parties | the death or bankruptcy of a party | the action does not terminate by reason of it |
| O 4 r 6(1) | liberty | numerous persons with a common interest | the Court | sue or be sued as a group |
| O 4 r 8(1), (3), (4), (7) | duty | the party | all the other parties (claim) | file and serve a notice of appointment, of change, of intention to act in person, or give notice of an address |
| O 4 r 8(5) | power | any other party | the Court | apply for an order declaring the solicitor ceased to act |
| O 4 r 9(1) | power | the solicitor | the Court | apply for an order declaring that the solicitor has ceased to act |
| O 5 r 1(2) | duty | the party | the other party | make an offer of amicable resolution before commencing |
| O 5 r 1(4) | duty (a prohibition) | the party | the offeror | not reject an offer without reasonable grounds |
| O 5 r 2(3) | disability | the Court | the offeror | terms of an offer not accepted cannot be relied on or made known to the Court yet |
| O 3 r 1(3), (4) | duty | the Court; every person | the parties | seek to achieve the Ideals; assist the Court |
| O 3 r 2(4), (8), (9) | power | the Court (to waive, reject, dismiss, fee, costs, revoke); the applicant (to apply) | the party in default (liability) | the consequences of non-compliance |
| O 3 r 4(1), (2) | power | the Court | the parties (liability) | extend or shorten a period |
| O 3 r 4(3) | power | the parties together | the Court (no order needed) | extend once by consent in writing by at most 14 days |
| O 3 r 6, r 7 | duty | the person filing | the Court | use the Forms; file documents in English with a certified translation |
| O 2 r 6(2) to (5) | power | the Court | the claimant or defendant (liability) | dismiss, give judgment, direct service, take the step |
| O 2 r 9(3), (4), (8), (10) | disability | any party | the Court | cannot file the pleading, affidavit or application without the Court's (or the trial Judge's) approval |
| O 2 r 10(1); r 12(1) | power (conditional) | a party | the Court | appeal only if the law allows |
| O 2 r 10(3), (7); r 12(3), (8) | duty | the appellant | parties with an interest | file and serve a notice of appeal; provide security for costs |

Four rows have no counterparty the text names in so many words; the counterparty is the natural correlative and is marked "(liability)" or "the Court".

## Marginal readings for a lawyer (roc1)

Status header (verification): the list is generated by `work/fk.py` and `work/notesgen.py` from the FALSE-kind and NOTHING-kind comments in the shipped layer-1 modules; a branch is listed when its comment shows one of the readings below.
Line numbers are not given because they move when a module is regenerated; the function name and the provision label find the branch.

**The readings (the status quo of the brief; for a lawyer, not for me).**
- **A. A failed "if", "where", "when", "upon" or "whenever" counts as the text's no**, clause by clause, inside the provision that holds it. The other reading: "if A then B" does not itself say "if not A then not B", so a failed condition leaves the text silent (`NOTHING`).
- **C. A flat negative counts as the text's no** (ruling N2). The other reading: a negative with a scope ("no application may be taken out during the period ...") says nothing outside it.
- **D. "Unless", "except", "without the Court's approval", "only if", "subject to".** A lift answers `NOTHING` (the bar is lifted and nothing is granted); a necessary condition that fails answers `JUST FALSE`; a necessary condition that is met answers `NOTHING`. The other readings are shown row by row.
- **B. A power or a grant limited by its own wording answers `NOTHING` outside what it names, not `JUST FALSE`** (each commented `NOTHING-kind (limited by its own wording)`, and listed below with the words that limit it). The other reading: a power given for named cases denies the power in every other case.
- Left out on purpose, because they are not readings but plain applications of the text: a duty the text states and the party has not done ("must file ... within 14 days"); a definition that "means" a closed list and the thing is not on it; a period the text fixes (rulings of 2026-11-05). Their FALSE-kind comments are in the modules.

Counts: A 143 branches, C 23, D 55, B 176; 397 rows in all.

**Period audit (ruling (a) of 2026-11-05).** Every function that tests a time against a period, deadline or window the text states was read (the list is in `work/audit_periods.py`, which also checks that each function exists and that a test of its JUST FALSE side is written; I read the cases in the other tests myself for the functions that are not "in time" calls). 33 answer JUST TRUE inside and JUST FALSE outside (checked, no change; this counts the "in time" and "within N days" functions, the minimum-length and cap tests, the windows of events and the three "until" bars), 1 was changed from NOTHING to JUST FALSE outside (`o 3 r 3 the act is in time`, the clear-days-after branch, fork F2; the same branch now answers JUST TRUE from the earliest day, where it answered NOTHING, and F2 gives NOTHING there as the other reading), and 3 keep NOTHING outside with a fork line giving JUST FALSE as the other reading (`o 3 r 4(3)` F15, `o 3 r 2(4)(e)` the late filing fee F3, `o 2 r 9(10) an application may be taken out on that day` F11). Not counted: 4 functions that take the "in time" verdict as an input (`o 4 r 4(2)(a)`, `o 6 r 6(5)`, `o 6 r 7(7)`, `o 6 r 9(3)`) answer definitely whenever the verdict is definite and NOTHING only when it is NOTHING; Period constructors and DATE functions (they cannot say JUST FALSE; their yes/no twins are counted); and name matches that are not time tests. One silent gap inside the counted: `o 6 r 3(1) ... valid for service on the day` answers NOTHING when the Rules give no last day (a period of months with no corresponding day, fork F16 A1), which is not an outside-the-period answer. The keel functions `o 1 r 2(4)(a)`, `(b)` and `(c)` answer NOTHING outside their periods; they are not this part's and were not changed. Not changed either: the shared in-time function tests the last day only, so an act done before the day a period starts answers JUST TRUE (measured 2026-11-05: 14 days after 5 November, done on 1 November: JUST TRUE).

| provision label | function | answer | quoted words (cut) | the other reading |
| --- | --- | --- | --- | --- |
| A O 2 r 2(1) | `o 2 r 2(1) the Court will conduct proceedings in a manner that will bring the action to a conclusion in keeping with the Ideals` | JUST FALSE | "When an action is commenced under these Rules" ("when" counts as "where") | the text is silent when the condition fails (`NOTHING`) |
| A O 2 r 4(2) | `o 2 r 4(2) the claimant may apply for judgment in default` | JUST FALSE | "If the defendant fails to file and serve such a notice or states in the notice that the defendant d... | the text is silent when the condition fails (`NOTHING`) |
| A O 2 r 4(2) | `o 2 r 4(2) the claimant may apply for judgment in default` | JUST FALSE | "upon proving that the originating claim with a statement of claim has been served on the defendant"... | the text is silent when the condition fails (`NOTHING`) |
| A O 2 r 5(1) | `o 2 r 5(1) the defendant has to file and serve a defence or an affidavit` | JUST FALSE | "his or her affidavit if he or she wishes to introduce evidence in the originating application" | the text is silent when the condition fails (`NOTHING`) |
| A O 2 r 5(2) | `o 2 r 5(2) the defendant need not file and serve a defence or affidavit on the merits` | JUST FALSE | "If the defendant is challenging the jurisdiction of the Court" | the text is silent when the condition fails (`NOTHING`) |
| A O 2 r 5(2) | `o 2 r 5(2) the defendant must file and serve a defence or affidavit stating the ground of the challenge` | JUST FALSE | "If the defendant is challenging the jurisdiction of the Court" | the text is silent when the condition fails (`NOTHING`) |
| A O 2 r 6(1) | `o 2 r 6(1) a case conference will be fixed` | JUST FALSE | "after an originating claim or an originating application is issued" (a stated time, read as a "wher... | the text is silent when the condition fails (`NOTHING`) |
| A O 2 r 6(2) | `o 2 r 6(2) the Court may dismiss the action` | JUST FALSE | "If no party attends the case conference or if the claimant is absent" | the text is silent when the condition fails (`NOTHING`) |
| A O 2 r 6(3)(a) | `o 2 r 6(3)(a) the Court may dismiss the action` | JUST FALSE | "If the claimant attends the case conference but has not served ... the Court may dismiss the action... | the text is silent when the condition fails (`NOTHING`) |
| A O 2 r 6(3)(b) | `o 2 r 6(3)(b) the Court may order the claimant to serve the action or to apply for substituted service, and fix another case conference` | JUST FALSE | "If the claimant attends the case conference but has not served the claimant’s originating claim or ... | the text is silent when the condition fails (`NOTHING`) |
| A O 2 r 6(4) | `o 2 r 6(4) the Court may give judgment for the claimant` | JUST FALSE | "If the claimant attends the case conference but the defendant is absent, the Court may give judgmen... | the text is silent when the condition fails (`NOTHING`) |
| A O 2 r 6(5) | `o 2 r 6(5) the Court may take that step` | JUST FALSE | "If both the claimant and defendant attend the case conference but the defendant has not filed and s... | the text is silent when the condition fails (`NOTHING`) |
| A O 2 r 6(7) | `o 2 r 6(7) the Court will direct the defendant to file and serve the necessary application with supporting affidavit` | JUST FALSE | "If the defendant is challenging the jurisdiction of the Court" | the text is silent when the condition fails (`NOTHING`) |
| A O 2 r 6(7)(b) | `o 2 r 6(7)(b) the Court will direct the claimant to file and serve any affidavit in reply` | JUST FALSE | "If the defendant is challenging the jurisdiction of the Court" | the text is silent when the condition fails (`NOTHING`) |
| A O 2 r 6(7) | `o 2 r 6(7)(c) the Court will fix the application for hearing` | JUST FALSE | "fix the application for hearing after all affidavits have been filed and served" ("after" read as a... | the text is silent when the condition fails (`NOTHING`) |
| A O 2 r 7(1) | `o 2 r 7(1) the Court will give directions to the defendant to file the defence or affidavit on the merits` | JUST FALSE | "If the defendant challenges the jurisdiction of the Court and fails" | the text is silent when the condition fails (`NOTHING`) |
| A O 2 r 7(2) | `o 2 r 7(2) the Court will consider all matters necessary to bring the proceedings to a conclusion in accordance with the Ideals` | JUST FALSE | "Where there is no challenge to the jurisdiction of the Court" (a failed "where"; paragraph (1) has ... | the text is silent when the condition fails (`NOTHING`) |
| A O 2 r 8 | `o 2 r 8 the Court may order the parties to file and exchange affidavits of evidence-in-chief` | JUST FALSE | "after pleadings have been filed and served but before any exchange of documents and before the Cour... | the text is silent when the condition fails (`NOTHING`) |
| A O 2 r 9(1) | `o 2 r 9(1) the Court will give the necessary directions in respect of that matter` | JUST FALSE | "Where the Court does not make any order described in Rule 8, or where the Court has made an order a... | the text is silent when the condition fails (`NOTHING`) |
| A O 2 r 9(2) | `o 2 r 9(2) the Court will order such pleadings to be filed and served` | JUST FALSE | "If further pleadings need to be filed" | the text is silent when the condition fails (`NOTHING`) |
| A O 2 r 9(10) | `o 2 r 9(10) an application may be taken out on that day` | JUST FALSE | "no application may be taken out during the period starting 14 days before the commencement of the t... | the text is silent when the condition fails (`NOTHING`) |
| A O 2 r 9(10) | `o 2 r 9(10) the day falls in the period in which no application may be taken out` | JUST FALSE | "the period starting 14 days before the commencement of the trial and ending when the Court has made... | the text is silent when the condition fails (`NOTHING`) |
| A O 2 r 9(12) | `o 2 r 9(12) the application has to be served on the other party` | JUST FALSE | "except where the other party cannot or need not be served" | the text is silent when the condition fails (`NOTHING`) |
| A O 2 r 10(2) | `o 2 r 10(2) the matter will proceed on appeal before the appropriate appellate Court` | JUST FALSE | "If any party appeals against the Court’s decision made in an application" | the text is silent when the condition fails (`NOTHING`) |
| A O 2 r 10(4) | `o 2 r 10(4) the appellant has to apply for permission and serve the application on all parties who have an interest` | JUST FALSE | "Where permission to appeal is required" | the text is silent when the condition fails (`NOTHING`) |
| A O 2 r 10(5) | `o 2 r 10(5) the party may apply to the appropriate appellate Court for permission` | JUST FALSE | "If the lower Court (where applicable) does not grant permission to appeal" | the text is silent when the condition fails (`NOTHING`) |
| A O 2 r 10(6) | `o 2 r 10(6) the appellant has to file and serve a notice of appeal after permission is granted` | JUST FALSE | "If permission to appeal is granted" | the text is silent when the condition fails (`NOTHING`) |
| A O 2 r 11(1) | `o 2 r 11(1) the Court will give directions for the trial or hearing` | JUST FALSE | "after the single application pending trial has been filed or after it has determined all applicatio... | the text is silent when the condition fails (`NOTHING`) |
| A O 2 r 12(2) | `o 2 r 12(2) the case will proceed on appeal before the appropriate appellate Court` | JUST FALSE | "If any party appeals against the Court’s decision after trial or after an originating application i... | the text is silent when the condition fails (`NOTHING`) |
| A O 2 r 12(4) | `o 2 r 12(4) the party who intends to appeal has to apply for permission and serve the application on all parties who have an interest` | JUST FALSE | "Where permission to appeal is required" | the text is silent when the condition fails (`NOTHING`) |
| A O 2 r 12(5) | `o 2 r 12(5) the party may apply to the appropriate appellate Court for permission` | JUST FALSE | "If the lower Court (where applicable) does not grant permission to appeal, that party may apply to ... | the text is silent when the condition fails (`NOTHING`) |
| A O 2 r 12(7) | `o 2 r 12(7) the party has to file and serve a notice of appeal after permission is granted` | JUST FALSE | "If permission to appeal is granted" | the text is silent when the condition fails (`NOTHING`) |
| A O 3 r 2(2) | `o 3 r 2(2) the Court may do what it considers necessary` | JUST FALSE | "Where there is no express provision in these Rules or any other written law on any matter" | the text is silent when the condition fails (`NOTHING`) |
| A O 3 r 2(4) | `o 3 r 2(4) the Court may exercise the powers in paragraph (4)` | JUST FALSE | "Where there is non‑compliance with these Rules, any other written law, the Court’s orders or direct... | the text is silent when the condition fails (`NOTHING`) |
| A O 3 r 2(4)(a) | `o 3 r 2(4)(a) the Court may waive the non-compliance` | JUST FALSE | "Where there is non‑compliance" | the text is silent when the condition fails (`NOTHING`) |
| A O 3 r 2(4)(b) | `o 3 r 2(4)(b) the Court may disallow or reject the filing or use of a document` | JUST FALSE | "Where there is non‑compliance" | the text is silent when the condition fails (`NOTHING`) |
| A O 3 r 2(4)(c) | `o 3 r 2(4)(c) the Court may refuse to hear a matter or dismiss it without a hearing` | JUST FALSE | "Where there is non‑compliance" | the text is silent when the condition fails (`NOTHING`) |
| A O 3 r 2(4)(d) | `o 3 r 2(4)(d) the Court may dismiss, stay or set aside the proceedings` | JUST FALSE | "Where there is non‑compliance" | the text is silent when the condition fails (`NOTHING`) |
| A O 3 r 2(4)(d) | `o 3 r 2(4)(d) the Court may dismiss, stay or set aside the proceedings` | JUST FALSE | "if the non‑compliance is inconsistent with any of the Ideals in a material way" | the text is silent when the condition fails (`NOTHING`) |
| A O 3 r 2(4)(f) | `o 3 r 2(4)(f) the Court may make a costs order or any other order` | JUST FALSE | "Where there is non‑compliance" | the text is silent when the condition fails (`NOTHING`) |
| A O 3 r 2(5) | `o 3 r 2(5) the Court may waive the non-compliance with a written law other than these Rules` | JUST FALSE | "Where the non‑compliance is in respect of any written law other than these Rules" | the text is silent when the condition fails (`NOTHING`) |
| A O 3 r 2(8) | `o 3 r 2(8) the Court may revoke a judgment or order obtained or set aside what was done` | JUST FALSE | "if it is in the interests of justice" | the text is silent when the condition fails (`NOTHING`) |
| A O 3 r 5(2) | `o 3 r 5(2) Form 1 is to be used` | JUST FALSE | "Form 1 is to be used when the summons has to be served" ("when" counts as "where") | the text is silent when the condition fails (`NOTHING`) |
| A O 3 r 5(3) | `o 3 r 5(3) Form 2 is to be used` | JUST FALSE | "when the summons need not be served on anyone and only where these Rules allow" | the text is silent when the condition fails (`NOTHING`) |
| A O 3 r 5(5) | `o 3 r 5(5) the party must file and serve an affidavit` | JUST FALSE | "If any party wishes to contest the application" | the text is silent when the condition fails (`NOTHING`) |
| A O 3 r 5(5) | `o 3 r 5(5) the affidavit is filed and served within 14 days after service of the application` | JUST FALSE | "If any party wishes to contest the application" | the text is silent when the condition fails (`NOTHING`) |
| A O 3 r 5(8) | `o 3 r 5(8) the application must be served on the other party` | JUST FALSE | "except where the other party cannot or need not be served" | the text is silent when the condition fails (`NOTHING`) |
| A O 3 r 6(3) | `o 3 r 6(3) the document must bear the seal of the Court` | JUST FALSE | "Where a Form states “Seal of the Court”" | the text is silent when the condition fails (`NOTHING`) |
| A O 4 r 1(a) | `o 4 r 1(a) a person aged 18 or older but below 21 may be a party in their own name` | JUST FALSE | "and where section 36 of the Civil Law Act applies" | the text is silent when the condition fails (`NOTHING`) |
| A O 4 r 3(3) | `o 4 r 3(3) the Court may give permission for an officer to act on behalf of the applicant` | JUST FALSE | "if the Court is satisfied that (a) the officer has been duly authorised ...; and (b) the officer ha... | the text is silent when the condition fails (`NOTHING`) |
| A O 4 r 3(4) | `o 4 r 3(4) the Court may give permission for an officer to act on behalf of the unincorporated association` | JUST FALSE | "if the Court is satisfied that (a) the officer has been duly authorised ...; and (b) the officer ha... | the text is silent when the condition fails (`NOTHING`) |
| A O 4 r 4(1) | `o 4 r 4(1) the action may be brought against the estate of the deceased` | JUST FALSE | "Where any defendant has died but a cause of action against him or her survives and no grant of prob... | the text is silent when the condition fails (`NOTHING`) |
| A O 4 r 4(2)(a) | `o 4 r 4(2)(a) the claimant may apply for that order` | JUST FALSE | "if a grant of probate or letters of administration has been made — an order that the personal repre... | the text is silent when the condition fails (`NOTHING`) |
| A O 4 r 4(3) | `o 4 r 4(3) the originating claim or originating application must be served on the Public Trustee` | JUST FALSE | "Where the Public Trustee has been appointed by an order under paragraph (2) to represent the deceas... | the text is silent when the condition fails (`NOTHING`) |
| A O 4 r 4(3) | `o 4 r 4(3) the Public Trustee's appointment extends beyond accepting service` | JUST FALSE | "Where the Public Trustee has been appointed by an order under paragraph (2) to represent the deceas... | the text is silent when the condition fails (`NOTHING`) |
| A O 4 r 4(4) | `o 4 r 4(4) the judgment or order binds the estate as if a grant had been made` | JUST FALSE | "Where no grant of probate or letters of administration has been made" | the text is silent when the condition fails (`NOTHING`) |
| A O 4 r 5(1) | `o 4 r 5(1) the action continues despite the death or bankruptcy` | JUST FALSE | "Where a party to an action dies or becomes bankrupt after the action has been commenced but the cau... | the text is silent when the condition fails (`NOTHING`) |
| A O 4 r 6(1) | `o 4 r 6(1) the persons may sue or be sued as a group with one or more representing the group` | JUST FALSE | "Where numerous persons have a common interest in any proceedings" | the text is silent when the condition fails (`NOTHING`) |
| A O 4 r 6(2) | `o 4 r 6(2) all members of the group must consent in writing and be included in a list of claimants` | JUST FALSE | "Where a group of persons is suing under this Rule" | the text is silent when the condition fails (`NOTHING`) |
| A O 4 r 6(3) | `o 4 r 6(3) the Court may appoint one or more of them as representative` | JUST FALSE | "Where a group of persons is being sued under this Rule" | the text is silent when the condition fails (`NOTHING`) |
| A O 4 r 6(4) | `o 4 r 6(4) the Court may appoint one or more persons to represent the class` | JUST FALSE | "Where there is a class of persons and all or any member of the class cannot be ascertained or canno... | the text is silent when the condition fails (`NOTHING`) |
| A O 4 r 8(1) | `o 4 r 8(1) the party must file and serve a notice of appointment of solicitor in Form 3 on all the parties` | JUST FALSE | "Where a party who was not represented by a solicitor decides to appoint a solicitor" | the text is silent when the condition fails (`NOTHING`) |
| A O 4 r 8(2) | `o 4 r 8(2) the deeming of the solicitor cannot yet end` | JUST FALSE | "until the final conclusion of the action in the Court" (the bar has lifted) | the text is silent when the condition fails (`NOTHING`) |
| A O 4 r 8(5) | `o 4 r 8(5) any other party may apply to the Court for an order declaring that the solicitor has ceased to be the solicitor` | JUST FALSE | "Where a solicitor has died, has ceased practice for any reason or cannot be contacted, and the part... | the text is silent when the condition fails (`NOTHING`) |
| A O 4 r 8(7) | `o 4 r 8(7) the party must give notice by letter to all the parties stating an address in Singapore for service` | JUST FALSE | "Where a party has no solicitor acting for the party on record" | the text is silent when the condition fails (`NOTHING`) |
| A O 4 r 8(8) | `o 4 r 8(8) an address is deemed to be the party's address for service` | JUST FALSE | "Where a party fails to comply with paragraph (7)" | the text is silent when the condition fails (`NOTHING`) |
| A O 4 r 8(9) | `o 4 r 8(9) the party may give notice by letter stating an electronic mail address for service` | JUST FALSE | "Where a party has no address in Singapore" | the text is silent when the condition fails (`NOTHING`) |
| A O 4 r 8(9) | `o 4 r 8(9) the party is deemed to agree that ordinary service and personal service may be effected by that electronic mail address` | JUST FALSE | "Where a party has no address in Singapore ... and by doing so, the party is deemed to agree" | the text is silent when the condition fails (`NOTHING`) |
| A O 4 r 9(1) | `o 4 r 9(1) the solicitor may apply to the Court for an order declaring that the solicitor has ceased to act` | JUST FALSE | "Where a solicitor who has acted for a party in a cause or matter has ceased so to act and the party... | the text is silent when the condition fails (`NOTHING`) |
| A O 4 r 9(1) | `o 4 r 9(1) the Court may make an order declaring that the solicitor has ceased to act` | JUST FALSE | "Where a solicitor who has acted for a party in a cause or matter has ceased so to act and the party... | the text is silent when the condition fails (`NOTHING`) |
| A O 4 r 9(1) | `o 4 r 9(1) the solicitor is still considered the solicitor of the party` | JUST FALSE | "Where a solicitor who has acted for a party in a cause or matter has ceased so to act and the party... | the text is silent when the condition fails (`NOTHING`) |
| A O 4 r 9(1) | `o 4 r 9(1) the solicitor is still considered the solicitor of the party` | JUST FALSE | "until the solicitor serves ... a copy of the order and files a notice in Form 5 ... till the final ... | the text is silent when the condition fails (`NOTHING`) |
| A O 4 r 9(5) | `o 4 r 9(5) the solicitor who acted for the assisted person ceases to be the solicitor acting` | JUST FALSE | "where the legal aid certificate of an assisted person within the meaning of the Legal Aid and Advic... | the text is silent when the condition fails (`NOTHING`) |
| A O 4 r 9(5) | `o 4 r 9(5) Rule 8(1) applies as if the party had previously sued or defended in person` | JUST FALSE | "if the assisted person whose certificate has been revoked or discharged desires to proceed with the... | the text is silent when the condition fails (`NOTHING`) |
| A O 5 r 2(3) | `o 5 r 2(3) the terms cannot yet be relied upon or made known to the Court` | JUST FALSE | "until after the Court has determined the merits of the action or appeal and is dealing with the iss... | the text is silent when the condition fails (`NOTHING`) |
| A O 5 r 2(4) | `o 5 r 2(4) the offer has expired under this paragraph` | JUST FALSE | "expires once the Court has determined the merits" ("once" counts as "when") | the text is silent when the condition fails (`NOTHING`) |
| A O 5 r 3(3) | `o 5 r 3(3) the Court may order the party to submit a sealed document setting out the reasons for the refusal` | JUST FALSE | "if a party informs the Court that the party does not wish to attempt to resolve the dispute by amic... | the text is silent when the condition fails (`NOTHING`) |
| A O 6 r 1(2) | `o 6 r 1(2) the claimant must commence proceedings by an originating claim` | JUST FALSE | "where the material facts are in dispute" | the text is silent when the condition fails (`NOTHING`) |
| A O 6 r 1(3) | `o 6 r 1(3) the claimant must commence proceedings by an originating application` | JUST FALSE | "where (a) these Rules or any written law require it; (b) the proceedings concern an application mad... | the text is silent when the condition fails (`NOTHING`) |
| A O 6 r 2 | `o 6 r 2 the originating claim or originating application is deemed issued` | JUST FALSE | "is deemed issued when the Registrar numbers, signs, seals and dates it" ("when" counts as "where") | the text is silent when the condition fails (`NOTHING`) |
| A O 6 r 3(2) | `o 6 r 3(2) an application may be made to extend the validity` | JUST FALSE | "if it has not been served on all or any of the defendants" | the text is silent when the condition fails (`NOTHING`) |
| A O 6 r 5(2) | `o 6 r 5(2) the claimant must annex a medical report and a statement of the special damages claimed` | JUST FALSE | "If the claim is for personal injuries" | the text is silent when the condition fails (`NOTHING`) |
| A O 6 r 5(5) | `o 6 r 5(5) a statement of claim must be served after the originating claim` | JUST FALSE | "Where the originating claim is endorsed generally" | the text is silent when the condition fails (`NOTHING`) |
| A O 6 r 5(5) | `o 6 r 5(5) the statement of claim is served within 14 days after the originating claim was served` | JUST FALSE | "Where the originating claim is endorsed generally" | the text is silent when the condition fails (`NOTHING`) |
| A O 6 r 5(6) | `o 6 r 5(6) reasonable steps to serve in Singapore are made in time` | JUST FALSE | "If the originating claim is to be served in Singapore" | the text is silent when the condition fails (`NOTHING`) |
| A O 6 r 5(7) | `o 6 r 5(7) reasonable steps to serve out of Singapore are made in time` | JUST FALSE | "If the originating claim is to be served out of Singapore" | the text is silent when the condition fails (`NOTHING`) |
| A O 6 r 6(5) | `o 6 r 6(5) the claimant may apply for judgment against the defendant in Form 11` | JUST FALSE | "If the defendant fails to file and serve such a notice within the prescribed time or states in the ... | the text is silent when the condition fails (`NOTHING`) |
| A O 6 r 6(6) | `o 6 r 6(6) the claimant must file a memorandum of service in Form 12` | JUST FALSE | "when the claimant applies for judgment to be given against the defendant pursuant to paragraph (5)"... | the text is silent when the condition fails (`NOTHING`) |
| A O 6 r 6(7) | `o 6 r 6(7) the Court may direct the payment of interest` | JUST FALSE | "when giving judgment under this Rule" ("when" counts as "where") | the text is silent when the condition fails (`NOTHING`) |
| A O 6 r 7(4) | `o 6 r 7(4) the defendant need not file and serve a defence on the merits` | JUST FALSE | "If the defendant is challenging the jurisdiction of the Court" | the text is silent when the condition fails (`NOTHING`) |
| A O 6 r 7(4) | `o 6 r 7(4) the defendant must file and serve a defence stating the ground of the challenge` | JUST FALSE | "If the defendant is challenging the jurisdiction of the Court" | the text is silent when the condition fails (`NOTHING`) |
| A O 6 r 7(7) | `o 6 r 7(7) the claimant may apply for judgment in default of defence in Form 14` | JUST FALSE | "If the defendant fails to file and serve a defence within the prescribed time" | the text is silent when the condition fails (`NOTHING`) |
| A O 6 r 7(8) | `o 6 r 7(8) the Court may direct the payment of interest` | JUST FALSE | "when giving judgment under this Rule" ("when" counts as "where") | the text is silent when the condition fails (`NOTHING`) |
| A O 6 r 8(1) | `o 6 r 8(1) the defendant must file and serve the counterclaim with the defence` | JUST FALSE | "If the defendant intends to counterclaim against the claimant" | the text is silent when the condition fails (`NOTHING`) |
| A O 6 r 8(3) | `o 6 r 8(3) the defendant must annex a medical report and a statement of the special damages claimed` | JUST FALSE | "If the counterclaim is for personal injuries" | the text is silent when the condition fails (`NOTHING`) |
| A O 6 r 9(1) | `o 6 r 9(1) the claimant need not file a reply to the defence` | JUST FALSE | "if the claimant merely wishes to deny assertions without adding anything material" | the text is silent when the condition fails (`NOTHING`) |
| A O 6 r 9(3) | `o 6 r 9(3) the defendant may apply for judgment in default of defence in respect of the counterclaim in Form 14` | JUST FALSE | "If the claimant fails to file and serve a defence to the counterclaim within the prescribed time" | the text is silent when the condition fails (`NOTHING`) |
| A O 6 r 10(1) | `o 6 r 10(1) the parties must seek the approval of the Court at the case conference to file a further pleading` | JUST FALSE | "in cases where it is necessary for certain matters to be pleaded" ("where" not met) | the text is silent when the condition fails (`NOTHING`) |
| A O 6 r 11(2) | `o 6 r 11(2) Form 15 is to be used` | JUST FALSE | "Form 15 is to be used when the originating application has to be served" ("when" counts as "where") | the text is silent when the condition fails (`NOTHING`) |
| A O 6 r 11(3) | `o 6 r 11(3) Form 16 is to be used` | JUST FALSE | "Form 16 is to be used when the originating application need not be served on anyone, where permitte... | the text is silent when the condition fails (`NOTHING`) |
| A O 6 r 11(4) | `o 6 r 11(4) reasonable steps to serve in Singapore are made in time` | JUST FALSE | "If the originating application is to be served in Singapore" | the text is silent when the condition fails (`NOTHING`) |
| A O 6 r 11(5) | `o 6 r 11(5) reasonable steps to serve out of Singapore are made in time` | JUST FALSE | "If the originating application is to be served out of Singapore" | the text is silent when the condition fails (`NOTHING`) |
| A O 6 r 12(1) | `o 6 r 12(1) the defendant must file and serve the defendant's affidavit` | JUST FALSE | "if the defendant wishes to introduce evidence in respect of the originating application" (an "if" n... | the text is silent when the condition fails (`NOTHING`) |
| A O 6 r 12(2) | `o 6 r 12(2) the defendant must file and serve the defendant's affidavit` | JUST FALSE | "if the defendant wishes to introduce evidence in respect of the originating application" (an "if" n... | the text is silent when the condition fails (`NOTHING`) |
| A O 6 r 12(1) | `o 6 r 12(1) the defendant's affidavit is filed and served within 21 days after service of the originating application` | JUST FALSE | "if the defendant wishes to introduce evidence in respect of the originating application" | the text is silent when the condition fails (`NOTHING`) |
| A O 6 r 12(2) | `o 6 r 12(2) the defendant's affidavit is filed and served within 5 weeks after service of the originating application` | JUST FALSE | "if the defendant wishes to introduce evidence in respect of the originating application" | the text is silent when the condition fails (`NOTHING`) |
| A O 6 r 12(3) | `o 6 r 12(3) the defendant need not file and serve an affidavit on the merits` | JUST FALSE | "If the defendant is challenging the jurisdiction of the Court" | the text is silent when the condition fails (`NOTHING`) |
| A O 6 r 14 | `o 6 r 14 the defendant must include the counterclaim in the defendant's affidavit with all the evidence that is necessary for it` | JUST FALSE | "If a defendant intends to make a counterclaim in the originating application against the claimant" | the text is silent when the condition fails (`NOTHING`) |
| A O 7 r 1(1)(a) | `o 7 r 1(1)(a) a document may be served by personal service` | JUST FALSE | "personal service, where expressly required by these Rules or any written law, or where the Court or... | the text is silent when the condition fails (`NOTHING`) |
| A O 7 r 2(3) | `o 7 r 2(3) the Registrar must notify the requesting person of the fact and manner of service` | JUST FALSE | "If the process server of the Court effects service" | the text is silent when the condition fails (`NOTHING`) |
| A O 7 r 3 | `o 7 r 3 ordinary service may be effected in that manner` | JUST FALSE | "its registered or principal office or, if none exists, its last known place of business" | the text is silent when the condition fails (`NOTHING`) |
| A O 7 r 4(1) | `o 7 r 4(1) the Court may direct service on an agent or manager of a principal` | JUST FALSE | "if it is satisfied that (a) ... (b) ...; and (c) either the authority of the agent or manager has n... | the text is silent when the condition fails (`NOTHING`) |
| A O 7 r 4(3) | `o 7 r 4(3) the claimant must send a copy of the order and of the document to the principal's overseas address` | JUST FALSE | "if the claimant knows that address" (an "if" not met, ruling of 2026-11-05 (b)) | the text is silent when the condition fails (`NOTHING`) |
| A O 7 r 4(3) | `o 7 r 4(3) the claimant has sent the copy to the principal as required` | JUST FALSE | "if the claimant knows that address" | the text is silent when the condition fails (`NOTHING`) |
| A O 7 r 5 | `o 7 r 5 the Court may authorise service by placing the document on a conspicuous part of the property` | JUST FALSE | "Where there is a claim for possession of immovable property ... if the Court is satisfied that (a) ... | the text is silent when the condition fails (`NOTHING`) |
| A O 7 r 6 | `o 7 r 6 section 20 of the Government Proceedings Act and Order 59, Rule 3 apply to the service` | JUST FALSE | "Where ... not being civil proceedings by or against the Government ... any document is required ...... | the text is silent when the condition fails (`NOTHING`) |
| A O 7 r 7(1) | `o 7 r 7(1) a party may apply to serve the document by substituted service` | JUST FALSE | "If a document is required to be served personally and it is impractical to serve it personally" | the text is silent when the condition fails (`NOTHING`) |
| A O 7 r 8 | `o 7 r 8 this Rule deems the day of service` | JUST FALSE | "when service is effected before 5 p.m." and "When service is effected after 5 p.m." are both unmet ... | the text is silent when the condition fails (`NOTHING`) |
| A O 8 r 1(1) | `o 8 r 1(1) the document may be served out of Singapore with the Court's approval` | JUST FALSE | "if it can be shown that the Court has the jurisdiction or is the appropriate court to hear the acti... | the text is silent when the condition fails (`NOTHING`) |
| A O 8 r 1(3) | `o 8 r 1(3) the Court's approval is not required` | JUST FALSE | "The Court’s approval is not required if service out of Singapore is allowed under a contract betwee... | the text is silent when the condition fails (`NOTHING`) |
| A O 8 r 1(4) | `o 8 r 1(4) the Court's approval is not required for service of the document` | JUST FALSE | "if the Court’s approval has been granted for service of the originating process out of Singapore" (... | the text is silent when the condition fails (`NOTHING`) |
| A O 8 r 2(1) | `o 8 r 2(1) service out of Singapore may be effected in that manner` | JUST FALSE | "Where the Court’s approval has been obtained under Rule 1(2)" | the text is silent when the condition fails (`NOTHING`) |
| A O 8 r 2(1) | `o 8 r 2(1) service out of Singapore may be effected in that manner` | JUST FALSE | "where there is a Civil Procedure Convention governing service in the foreign country ... in the cas... | the text is silent when the condition fails (`NOTHING`) |
| A O 8 r 2(1) | `o 8 r 2(1) service out of Singapore may be effected in that manner` | JUST FALSE | "where there is a Civil Procedure Convention governing service in the foreign country ... in the cas... | the text is silent when the condition fails (`NOTHING`) |
| A O 8 r 2(1) | `o 8 r 2(1) service out of Singapore may be effected in that manner` | JUST FALSE | "where there is a Civil Procedure Convention governing service in the foreign country ... in the cas... | the text is silent when the condition fails (`NOTHING`) |
| A O 8 r 2(1) | `o 8 r 2(1) service out of Singapore may be effected in that manner` | JUST FALSE | "in the case where both the Hague Service Convention and another Civil Procedure Convention govern s... | the text is silent when the condition fails (`NOTHING`) |
| A O 8 r 2(1) | `o 8 r 2(1) service out of Singapore may be effected in that manner` | JUST FALSE | "through the government of the foreign country if that government is willing to effect service" | the text is silent when the condition fails (`NOTHING`) |
| A O 8 r 2(1) | `o 8 r 2(1) service out of Singapore may be effected in that manner` | JUST FALSE | "through the judicial authority of the foreign country if that authority is willing to effect servic... | the text is silent when the condition fails (`NOTHING`) |
| A O 8 r 2(3) | `o 8 r 2(3) the solicitor for the serving party must send them to the Registrar with a letter` | JUST FALSE | "Where the originating process or other court documents have to be sent from the Government of Singa... | the text is silent when the condition fails (`NOTHING`) |
| A O 8 r 2(4) | `o 8 r 2(4) the document must be accompanied by a translation` | JUST FALSE | "except where the official language or one of the official languages is English" | the text is silent when the condition fails (`NOTHING`) |
| A O 8 r 3 | `o 8 r 3 the originating process may be served in that manner` | JUST FALSE | "Where the defendant is in Malaysia or Brunei Darussalam" | the text is silent when the condition fails (`NOTHING`) |
| A O 8 r 3(b) | `o 8 r 3(b) the originating process is deemed to have been duly served` | JUST FALSE | "if it is returned with an endorsement of service and with an affidavit of such service, it is deeme... | the text is silent when the condition fails (`NOTHING`) |
| A O 8 r 4A(1) | `o 8 r 4A(1) this Rule applies to the service` | JUST FALSE | "on a person, other than a State, in a Contracting State" | the text is silent when the condition fails (`NOTHING`) |
| A O 8 r 4A(2) | `o 8 r 4A(2) the provision in Rule 4A prevails over the other provision in this Order` | JUST FALSE | "If any provision in this Rule is inconsistent with any other provision in this Order" (a failed "if... | the text is silent when the condition fails (`NOTHING`) |
| A O 8 r 4A(4)(d) | `o 8 r 4A(4)(d) the copies may be in electronic form` | JUST FALSE | "which may be in electronic form if agreed to by the central authority" (a failed "if", marginal rea... | the text is silent when the condition fails (`NOTHING`) |
| A O 8 r 5(1) | `o 8 r 5(1) the person must file in the Registry the request, the sealed copy and the translation` | JUST FALSE | "Upon obtaining the Court’s approval under Rule 1(2)" ("upon" counts as "where") | the text is silent when the condition fails (`NOTHING`) |
| A O 8 r 5(1) | `o 8 r 5(1) the person has filed in the Registry what the Rule requires` | JUST FALSE | "must file in the Registry (a) a request for the Ministry of Foreign Affairs to arrange service; (b)... | the text is silent when the condition fails (`NOTHING`) |
| A O 8 r 6(1) | `o 8 r 6(1) the person must file in the Registry the request, the sealed copy and the translation` | JUST FALSE | "Upon obtaining the Court’s approval under Rule 1(2)" ("upon" counts as "where") | the text is silent when the condition fails (`NOTHING`) |
| A O 8 r 6(1) | `o 8 r 6(1) the person has filed in the Registry what the Rule requires` | JUST FALSE | "must file in the Registry (a) a request for the Ministry of Foreign Affairs to arrange service; (b)... | the text is silent when the condition fails (`NOTHING`) |
| A O 8 r 6(5) | `o 8 r 6(5) the originating process may be served by that method` | JUST FALSE | "Where section 14(6) of the State Immunity Act applies and the State has agreed to a method of servi... | the text is silent when the condition fails (`NOTHING`) |
| A O 8 r 6(6) | `o 8 r 6(6) the request must be accompanied by a summary of the document` | JUST FALSE | "Where the State is a Contracting State to the Hague Service Convention" | the text is silent when the condition fails (`NOTHING`) |
| A O 8 r 7(2) | `o 8 r 7(2) the solicitor for the serving party must pay the expenses` | JUST FALSE | "Upon request to pay the expenses" ("upon" counts as "where") | the text is silent when the condition fails (`NOTHING`) |
| A O 8 r 7(2) | `o 8 r 7(2) the expenses are paid within 14 days after the request` | JUST FALSE | "Upon request to pay the expenses" ("upon" counts as "where") | the text is silent when the condition fails (`NOTHING`) |
| C O 2 r 1(2) | `o 2 r 1(2) an action needs to proceed in precisely the same way as set out in this Order` | JUST FALSE | "An action does not need to proceed in precisely the same way as set out in this Order" | the negative is a scope limit and says nothing outside its scope (`NOTHING`) |
| C O 2 r 5(4) | `o 2 r 5(4) the filing and service of the defence or affidavit is treated as submission to the jurisdiction of the Court` | JUST FALSE | "the filing and service of such a defence or affidavit will not be treated as submission to the juri... | the negative is a scope limit and says nothing outside its scope (`NOTHING`) |
| C O 2 r 9(3) | `o 2 r 9(3) a pleading after the defence or the defence to counterclaim can be filed` | JUST FALSE | "cannot be filed without the Court’s approval" | the negative is a scope limit and says nothing outside its scope (`NOTHING`) |
| C O 2 r 9(4) | `o 2 r 9(4) a further affidavit can be filed` | JUST FALSE | "Further affidavits cannot be filed for an originating application without the Court’s approval" | the negative is a scope limit and says nothing outside its scope (`NOTHING`) |
| C O 2 r 9(8) | `o 2 r 9(8) the application may be taken out` | JUST FALSE | "No other application may be taken out by any party at any time" | the negative is a scope limit and says nothing outside its scope (`NOTHING`) |
| C O 2 r 10(11) | `o 2 r 10(11) further evidence may be admitted` | JUST FALSE | "No further evidence may be admitted without the approval of the appellate Court" | the negative is a scope limit and says nothing outside its scope (`NOTHING`) |
| C O 2 r 12(10) | `o 2 r 12(10) further evidence may be admitted` | JUST FALSE | "No further evidence may be admitted without the approval of the appellate Court" | the negative is a scope limit and says nothing outside its scope (`NOTHING`) |
| C O 3 r 3(1) | `o 3 r 3(1) the Interpretation Act applies to the calculation of time in these Rules` | JUST FALSE | "The Interpretation Act does not apply to the calculation of time in these Rules" | the negative is a scope limit and says nothing outside its scope (`NOTHING`) |
| C O 3 r 2(2) | `o 3 r 2(2) the Court may do what it considers necessary` | JUST FALSE | "so long as it is not prohibited by law and is consistent with the Ideals" | the negative is a scope limit and says nothing outside its scope (`NOTHING`) |
| C O 3 r 2(6) | `o 3 r 2(6) the powers under this Rule affect another power of the Court under a written law` | JUST FALSE | "do not affect any other powers of the Court under any written law" | the negative is a scope limit and says nothing outside its scope (`NOTHING`) |
| C O 4 r 2(3) | `o 4 r 2(3) the litigation representative may have an interest adverse to that of the person represented` | JUST FALSE | "A litigation representative must not have any interest adverse to that of the person he or she is r... | the negative is a scope limit and says nothing outside its scope (`NOTHING`) |
| C O 4 r 3(6) “Court” | `o 4 r 3(6) the Court is that court` | JUST FALSE | head (d) of "“Court” means" does not hold | the negative is a scope limit and says nothing outside its scope (`NOTHING`) |
| C O 4 r 3(6) “Court” | `o 4 r 3(6) the Court is that court` | JUST FALSE | head (f) of "“Court” means" does not hold | the negative is a scope limit and says nothing outside its scope (`NOTHING`) |
| C O 4 r 8(6) | `o 4 r 8(6) the notice affects the rights of the solicitor and the party as between themselves` | JUST FALSE | "does not affect the rights of the solicitor and the party who appointed the solicitor as between th... | the negative is a scope limit and says nothing outside its scope (`NOTHING`) |
| C O 4 r 9(4) | `o 4 r 9(4) the order affects the rights of the solicitor and the party as between themselves` | JUST FALSE | "An order in Form 7 made under this Rule does not affect the rights of the solicitor and the party f... | the negative is a scope limit and says nothing outside its scope (`NOTHING`) |
| C O 5 r 1(4) | `o 5 r 1(4) the party may reject an offer of amicable resolution` | JUST FALSE | "must not reject an offer of amicable resolution" | the negative is a scope limit and says nothing outside its scope (`NOTHING`) |
| C O 6 r 3(6) | `o 6 r 3(6) paragraphs (1) and (4) apply to the originating claim` | JUST FALSE | "Paragraphs (1) and (4) do not apply to an originating claim relating to Admiralty causes and matter... | the negative is a scope limit and says nothing outside its scope (`NOTHING`) |
| C O 6 r 6(4) | `o 6 r 6(4) filing and serving the notice is treated as a submission to jurisdiction or a waiver of improper service` | JUST FALSE | "is not treated as a submission to jurisdiction or a waiver of any improper service of the originati... | the negative is a scope limit and says nothing outside its scope (`NOTHING`) |
| C O 6 r 7(6) | `o 6 r 7(6) a defence filed under paragraph (4) is treated as a submission to jurisdiction` | JUST FALSE | "A defence filed under paragraph (4) is not treated as a submission to jurisdiction" | the negative is a scope limit and says nothing outside its scope (`NOTHING`) |
| C O 6 r 10(2) | `o 6 r 10(2) a further pleading may be filed` | JUST FALSE | "No further pleadings may be filed unless the Court otherwise orders at the case conference" | the negative is a scope limit and says nothing outside its scope (`NOTHING`) |
| C O 6 r 12(5) | `o 6 r 12(5) an affidavit filed under paragraph (3) is treated as a submission to jurisdiction` | JUST FALSE | "An affidavit filed under paragraph (3) is not treated as a submission to jurisdiction" | the negative is a scope limit and says nothing outside its scope (`NOTHING`) |
| C O 6 r 12(6) | `o 6 r 12(6) a further affidavit may be filed` | JUST FALSE | "no further affidavits may be filed" | the negative is a scope limit and says nothing outside its scope (`NOTHING`) |
| C O 8 r 4A(6) | `o 8 r 4A(6) Rule 2(3) applies to the service` | JUST FALSE | "Rule 2(3) does not apply in relation to any service under this Rule" | the negative is a scope limit and says nothing outside its scope (`NOTHING`) |
| D O 2 r 6(7) | `o 2 r 6(7)(b) a further affidavit may be filed` | NOTHING | "with no further affidavits to be filed without the Court’s approval" lifts the negative and does no... | the lift is itself a grant (`JUST TRUE`) |
| D O 2 r 6(7) | `o 2 r 6(7)(b) a further affidavit may be filed` | JUST FALSE | "with no further affidavits to be filed without the Court’s approval" | failing the condition is not a no (`NOTHING`) |
| D O 2 r 9(3) | `o 2 r 9(3) a pleading after the defence or the defence to counterclaim can be filed` | NOTHING | "without the Court’s approval" lifts the negative and does not grant a permission | the lift is itself a grant (`JUST TRUE`) |
| D O 2 r 9(4) | `o 2 r 9(4) a further affidavit can be filed` | NOTHING | "without the Court’s approval" lifts the negative and does not grant a permission | the lift is itself a grant (`JUST TRUE`) |
| D O 2 r 9(8) | `o 2 r 9(8) the application may be taken out` | NOTHING | "except as directed at the case conference or with the Court’s approval" lifts the negative and does... | the lift is itself a grant (`JUST TRUE`) |
| D O 2 r 9(8) | `o 2 r 9(8) the application may be taken out` | NOTHING | "unless it is an application for" one of the fifteen listed lifts the negative and does not grant a ... | the lift is itself a grant (`JUST TRUE`) |
| D O 2 r 9(10) | `o 2 r 9(10) an application may be taken out on that day` | NOTHING | "Except in a special case and with the trial Judge’s approval" lifts the negative and does not grant... | the lift is itself a grant (`JUST TRUE`) |
| D O 2 r 10(1) | `o 2 r 10(1) an appeal against the Court's decision made in an application may be filed` | NOTHING | "only if the law allows" states a necessary condition and does not say the appeal may be filed | the lift is itself a grant (`JUST TRUE`) |
| D O 2 r 10(1) | `o 2 r 10(1) an appeal against the Court's decision made in an application may be filed` | JUST FALSE | "may be filed only if the law allows" | failing the condition is not a no (`NOTHING`) |
| D O 2 r 10(7) | `o 2 r 10(7) the appellant has to provide security for the costs of the appeal` | JUST FALSE | "Save for appeals filed under Divisions 2 and 4 of Order 18" | failing the condition is not a no (`NOTHING`) |
| D O 2 r 10(10) | `o 2 r 10(10) the document may be filed in the appeal` | NOTHING | "without the approval of the appellate Court" lifts the negative and does not grant a permission | the lift is itself a grant (`JUST TRUE`) |
| D O 2 r 10(10) | `o 2 r 10(10) the document may be filed in the appeal` | JUST FALSE | "No document other than the parties’ written submissions ... may be filed in the appeal without the ... | failing the condition is not a no (`NOTHING`) |
| D O 2 r 10(11) | `o 2 r 10(11) further evidence may be admitted` | NOTHING | "without the approval of the appellate Court" lifts the negative and does not grant a permission | the lift is itself a grant (`JUST TRUE`) |
| D O 2 r 12(1) | `o 2 r 12(1) an appeal against the Court's decision after trial or after an originating application is heard may be filed` | NOTHING | "only if the law allows" states a necessary condition and does not say the appeal may be filed | the lift is itself a grant (`JUST TRUE`) |
| D O 2 r 12(1) | `o 2 r 12(1) an appeal against the Court's decision after trial or after an originating application is heard may be filed` | JUST FALSE | "may be filed only if the law allows" | failing the condition is not a no (`NOTHING`) |
| D O 2 r 12(10) | `o 2 r 12(10) further evidence may be admitted` | NOTHING | "without the approval of the appellate Court" lifts the negative and does not grant a permission | the lift is itself a grant (`JUST TRUE`) |
| D O 2 r 13(2) | `o 2 r 13(2) the Court which heard the matter must fix the costs of the matter` | JUST FALSE | "unless the Court thinks fit to direct an assessment of the costs" | failing the condition is not a no (`NOTHING`) |
| D O 2 r 13(3) | `o 2 r 13(3) the amount of costs allowed is as set out in these Rules` | JUST FALSE | "unless the Court otherwise orders" | failing the condition is not a no (`NOTHING`) |
| D O 3 r 3(2) | `o 3 r 3(2) the word month is read as a calendar month` | JUST FALSE | "unless the context otherwise requires" | failing the condition is not a no (`NOTHING`) |
| D O 3 r 4(2) | `o 3 r 4(2) the Court may extend the period whether the application is made before or after it expires` | JUST FALSE | "Unless these Rules otherwise provide" | failing the condition is not a no (`NOTHING`) |
| D O 3 r 4(3) | `o 3 r 4(3) the period may be extended by consent in writing without an order of the Court` | NOTHING | "may be extended once by consent in writing for a maximum period of 14 days without an order of the ... | the lift is itself a grant (`JUST TRUE`) |
| D O 3 r 2(1) | `o 3 r 2(1) the requirement is subject to the Court's discretion to order otherwise` | JUST FALSE | "Unless the context otherwise requires" | failing the condition is not a no (`NOTHING`) |
| D O 3 r 2(1) | `o 3 r 2(1) the requirement is subject to the Court's discretion to order otherwise` | NOTHING | "subject to any other written law" | the lift is itself a grant (`JUST TRUE`) |
| D O 3 r 2(4)(a) | `o 3 r 2(4)(a) the Court may waive the non-compliance` | JUST FALSE | "the Court may waive the non‑compliance only if the written law allows such waiver" (paragraph (5)) | failing the condition is not a no (`NOTHING`) |
| D O 3 r 2(5) | `o 3 r 2(5) the Court may waive the non-compliance with a written law other than these Rules` | JUST FALSE | "only if the written law allows such waiver" | failing the condition is not a no (`NOTHING`) |
| D O 3 r 5(1) | `o 3 r 5(1) the application to the Court in an action is made as the Rule requires` | NOTHING | "Subject to these Rules" | the lift is itself a grant (`JUST TRUE`) |
| D O 3 r 5(6) | `o 3 r 5(6) the Court allows a further affidavit` | NOTHING | "Except in a special case" lifts the negative and does not say the Court will allow | the lift is itself a grant (`JUST TRUE`) |
| D O 3 r 9 | `o 3 r 9 the Court may conduct a hearing by electronic, mechanical or other means` | NOTHING | "Subject to any written law" | the lift is itself a grant (`JUST TRUE`) |
| D O 4 r 3(1)(b) | `o 4 r 3(1)(b) an entity with the capacity to sue or be sued must be represented by a solicitor` | JUST FALSE | "subject to paragraphs (2), (3) and (4)" (a marginal reading: the paragraphs lift the duty) | failing the condition is not a no (`NOTHING`) |
| D O 4 r 4(3) | `o 4 r 4(3) the Public Trustee's appointment extends beyond accepting service` | NOTHING | "unless the Public Trustee consents to take further steps" lifts the limit and does not say how far ... | the lift is itself a grant (`JUST TRUE`) |
| D O 4 r 8(2) | `o 4 r 8(2) the solicitor is deemed to be acting for the party` | JUST FALSE | "Unless notice is given according to this Rule" | failing the condition is not a no (`NOTHING`) |
| D O 4 r 8(2) | `o 4 r 8(2) the solicitor's business address is deemed to be the address for service of all documents` | JUST FALSE | "Unless notice is given according to this Rule" | failing the condition is not a no (`NOTHING`) |
| D O 4 r 8(2) | `o 4 r 8(2) the deeming of the solicitor cannot yet end` | NOTHING | the deeming applies to a solicitor appointed at any stage "Unless notice is given according to this ... | the lift is itself a grant (`JUST TRUE`) |
| D O 4 r 9(1) | `o 4 r 9(1) the solicitor is still considered the solicitor of the party` | NOTHING | "subject to Rule 8" | the lift is itself a grant (`JUST TRUE`) |
| D O 4 r 9(2) | `o 4 r 9(2) the summons has been served on the party for whom the solicitor acted as required` | NOTHING | "unless the Court otherwise directs" lifts the requirement and does not say what then applies | the lift is itself a grant (`JUST TRUE`) |
| D O 4 r 9(2) | `o 4 r 9(2) the summons has been served on the party for whom the solicitor acted as required` | JUST FALSE | "the summons must, unless the Court otherwise directs, be served on the party for whom the solicitor... | failing the condition is not a no (`NOTHING`) |
| D O 5 r 1(2) | `o 5 r 1(2) the party is to make an offer of amicable resolution before commencing the action` | JUST FALSE | "unless the party has reasonable grounds not to do so" | failing the condition is not a no (`NOTHING`) |
| D O 5 r 1(2) | `o 5 r 1(2) the party has complied before commencing the action` | NOTHING | "unless the party has reasonable grounds not to do so" lifts the duty and does not say what then fol... | the lift is itself a grant (`JUST TRUE`) |
| D O 5 r 1(4) | `o 5 r 1(4) the party may reject an offer of amicable resolution` | NOTHING | "unless the party has reasonable grounds to do so" lifts the negative and does not grant a permissio... | the lift is itself a grant (`JUST TRUE`) |
| D O 5 r 2(2) | `o 5 r 2(2) the offer is open for acceptance as required` | NOTHING | "unless the parties otherwise agree" lifts the requirement and does not say what then applies | the lift is itself a grant (`JUST TRUE`) |
| D O 5 r 2(4) | `o 5 r 2(4) the offer has expired under this paragraph` | NOTHING | "unless the offeror has stated otherwise" lifts the expiry and does not say what then applies | the lift is itself a grant (`JUST TRUE`) |
| D O 6 r 1(1) | `o 6 r 1(1) a claimant may commence proceedings by an originating claim or an originating application` | JUST FALSE | "Unless these Rules or any written law otherwise provide" | failing the condition is not a no (`NOTHING`) |
| D O 6 r 3(4) | `o 6 r 3(4) the Court may extend the validity` | NOTHING | "Except in a special case" lifts the limits and does not say what the Court may then do | the lift is itself a grant (`JUST TRUE`) |
| D O 6 r 4 | `o 6 r 4 the originating claim or originating application is served personally on the defendant as required` | NOTHING | "Subject to the provisions of any written law and these Rules" | the lift is itself a grant (`JUST TRUE`) |
| D O 6 r 5(4) | `o 6 r 5(4) the originating claim may be endorsed generally` | NOTHING | "Except in a special case" lifts the limit and does not say that endorsing generally is then allowed | the lift is itself a grant (`JUST TRUE`) |
| D O 6 r 5(4) | `o 6 r 5(4) the originating claim may be endorsed generally` | JUST FALSE | "may be endorsed generally only if the limitation period for the cause of action will expire within ... | failing the condition is not a no (`NOTHING`) |
| D O 6 r 11(1) | `o 6 r 11(1) the originating application is in Form 15 or Form 16 and supported by affidavit` | NOTHING | "Subject to these Rules and any other written law" | the lift is itself a grant (`JUST TRUE`) |
| D O 6 r 12(6) | `o 6 r 12(6) a further affidavit may be filed` | NOTHING | "Except in a special case" lifts the negative and does not say a further affidavit may then be filed | the lift is itself a grant (`JUST TRUE`) |
| D O 7 r 3 | `o 7 r 3 ordinary service may be effected in that manner` | JUST FALSE | "by fax, but only if (i) both the serving party and the party to be served act by solicitor; and (ii... | failing the condition is not a no (`NOTHING`) |
| D O 7 r 8 | `o 7 r 8 the day service is deemed effected` | NOTHING | "Subject to any written law and these Rules (including Order 28 regulating the electronic filing ser... | the lift is itself a grant (`JUST TRUE`) |
| D O 7 r 8 | `o 7 r 8 this Rule deems the day of service` | NOTHING | "Subject to any written law and these Rules (including Order 28 regulating the electronic filing ser... | the lift is itself a grant (`JUST TRUE`) |
| D O 8 r 1(2) | `o 8 r 1(2) the application for the Court's approval is made as required` | JUST FALSE | "the claimant must apply to the Court by summons without notice and supported by affidavit which mus... | failing the condition is not a no (`NOTHING`) |
| D O 8 r 2(1) | `o 8 r 2(1) service out of Singapore may be effected in that manner` | NOTHING | "subject to any objection made by the receiving Contracting State" depends on what the State objecte... | the lift is itself a grant (`JUST TRUE`) |
| D O 8 r 2(2) | `o 8 r 2(2) the documents may be sent to the entity by the serving party` | JUST FALSE | "Unless any Civil Procedure Convention, treaty, government or judicial authority of a foreign countr... | failing the condition is not a no (`NOTHING`) |
| D O 8 r 2(4) | `o 8 r 2(4) the document is accompanied by the translation as required` | NOTHING | "except where the official language or one of the official languages is English" lifts the duty and ... | the lift is itself a grant (`JUST TRUE`) |
| B O 2 r 2(2) | `o 2 r 2(2) a party is to assist the Court and conduct the case in a manner that will bring about such a resolution` | NOTHING | the duty is of "All parties" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 2 r 3(2) | `o 2 r 3(2) the claimant has to take reasonable steps to serve expeditiously` | NOTHING | the duty is of "The claimant" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 2 r 3(2) | `o 2 r 3(2) the claimant has taken reasonable steps to serve expeditiously as required` | NOTHING | the duty is of "The claimant" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 2 r 4(1) | `o 2 r 4(1) the defendant has to file and serve a notice of intention to contest or not contest the claim` | NOTHING | the duty is of "A defendant who is served an originating claim with a statement of claim" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 2 r 4(1) | `o 2 r 4(1) the defendant has filed and served the notice as required` | NOTHING | the duty is of "A defendant who is served an originating claim with a statement of claim" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 2 r 5(1) | `o 2 r 5(1) the defendant has to file and serve a defence or an affidavit` | NOTHING | the duty is of "A defendant who wishes to contest" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 2 r 5(1) | `o 2 r 5(1) the defendant has to file and serve a defence or an affidavit` | NOTHING | the rule is of "an originating claim or an originating application" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 2 r 5(4) | `o 2 r 5(4) the defendant has to state the challenge in the defence or affidavit` | NOTHING | the duty is of "A defendant who is challenging the jurisdiction of the Court" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 2 r 5(4) | `o 2 r 5(4) the filing and service of the defence or affidavit is treated as submission to the jurisdiction of the Court` | NOTHING | the flat negative is of "such a defence or affidavit" that states the challenge | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 2 r 6(5) | `o 2 r 6(5) the Court may take that step` | NOTHING | the power to give judgment is "in an originating claim" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 2 r 6(7) | `o 2 r 6(7)(b) a further affidavit may be filed` | NOTHING | the sub-paragraph is of a defendant "challenging the jurisdiction of the Court" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 2 r 9(3) | `o 2 r 9(3) a pleading after the defence or the defence to counterclaim can be filed` | NOTHING | the flat negative is of "Pleadings after the defence or the defence to counterclaim" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 2 r 9(4) | `o 2 r 9(4) a further affidavit can be filed` | NOTHING | the flat negative is of further affidavits "for an originating application" "after the defendant fil... | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 2 r 9(5) | `o 2 r 9(5) the Court will order each party to file a single application pending trial for all the matters stated in paragraph (1)` | NOTHING | "As far as possible" states what the Court does when it can and says nothing of what it does when it... | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 2 r 9(9) | `o 2 r 9(9) the Court's approval has been sought as required` | NOTHING | the requirement is for approval "to file further applications other than those directed at a case co... | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 2 r 9(10) | `o 2 r 9(10) an application may be taken out on that day` | NOTHING | the flat negative reaches "the period starting 14 days before the commencement of the trial and endi... | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 2 r 9(11) | `o 2 r 9(11) the trial Judge's approval has been sought as required` | NOTHING | the requirement is for "The trial Judge’s approval" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 2 r 9(12) | `o 2 r 9(12) the application has to be served on the other party` | NOTHING | the duty is for "All applications to the Court" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 2 r 10(3) | `o 2 r 10(3) the appellant has to file and serve a notice of appeal on all parties who have an interest` | NOTHING | the duty is of "The appellant" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 2 r 10(8) | `o 2 r 10(8) the appeal will proceed by way of rehearing on the documents` | NOTHING | the paragraph is of "The appeal" in this Rule | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 2 r 10(9) | `o 2 r 10(9) the parties have to file and serve written submissions` | NOTHING | the duty is of "The parties" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 2 r 10(10) | `o 2 r 10(10) the document may be filed in the appeal` | NOTHING | the flat negative is of a "document other than the parties’ written submissions" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 2 r 11(2) | `o 2 r 11(2) the action will generally be decided at a trial involving oral evidence and cross examination` | NOTHING | paragraph (2) is of "An action commenced by originating claim"; paragraph (3) has the originating ap... | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 2 r 11(3) | `o 2 r 11(3) the action will generally be decided at a hearing based on affidavits` | NOTHING | paragraph (3) is of "An action commenced by originating application"; paragraph (2) has the originat... | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 2 r 12(3) | `o 2 r 12(3) the appellant has to file and serve a notice of appeal on all parties who have an interest` | NOTHING | the duty is of "The appellant" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 2 r 12(6) | `o 2 r 12(6) the party has to serve the application for permission on all parties who have an interest` | NOTHING | the duty is of "That party" who applies for permission | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 2 r 12(8) | `o 2 r 12(8) the appellant has to provide security for the costs of the appeal` | NOTHING | the duty is of "The appellant" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 2 r 12(9) | `o 2 r 12(9) the appellant and the respondent have to file and serve the relevant appeal documents` | NOTHING | the duty is of "The appellant and the respondent" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 2 r 13(1) | `o 2 r 13(1) the Court has the power to determine the issue relating to costs` | NOTHING | the power is over "all issues relating to the costs of or incidental to all proceedings" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 2 r 13(2) | `o 2 r 13(2) the Court which heard the matter must fix the costs of the matter` | NOTHING | the duty is of "The Court which heard a matter" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 2 r 13(3) | `o 2 r 13(3) the amount of costs allowed is as set out in these Rules` | NOTHING | the rule is of "the cases to which fixed costs apply under these Rules" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 2 r 14 | `o 2 r 14 the party takes out a single application for one or more methods of enforcement` | NOTHING | the rule is "To enforce a judgment" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 3 r 3(1) | `o 3 r 3(1) the Interpretation Act applies to the calculation of time in these Rules` | NOTHING | the flat negative reaches "the calculation of time in these Rules" only | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 3 r 4(1) | `o 3 r 4(1) the Court may extend or shorten the period` | NOTHING | the power reaches "the period within which a person is required by these Rules or by any judgment, o... | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 3 r 4(3) | `o 3 r 4(3) the period may be extended by consent in writing without an order of the Court` | NOTHING | the paragraph reaches a period "to serve, file or amend any pleading or other document" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 3 r 4 | `o 3 r 4 the last day as extended or shortened` | NOTHING | "once ... for a maximum period of 14 days" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 3 r 1(1) | `o 3 r 1(1) the provision is to be given a purposive interpretation` | NOTHING | the sentence reaches "These Rules" only; nothing is said of any other text | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 3 r 1(3) | `o 3 r 1(3) the Court must seek to achieve the Ideals in the decision` | NOTHING | the duty is stated for "all its orders or directions" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 3 r 1(4) | `o 3 r 1(4) the person has the duty to assist the Court and conduct the case to help achieve the Ideals` | NOTHING | the duty is stated for "All parties" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 3 r 1(4) | `o 3 r 1(4) the party has done what the duty requires` | NOTHING | the duty is stated for "All parties" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 3 r 2(2) | `o 3 r 2(2) the Court may do what it considers necessary` | NOTHING | the power is "whatever the Court considers necessary ... to ensure that justice is done or to preven... | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 3 r 2(3) | `o 3 r 2(3) the Court may impose a condition or give a direction` | NOTHING | "In exercising any power" and "such directions that are appropriate" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 3 r 2(4)(e) | `o 3 r 2(4)(e) the Court may impose a late filing fee` | NOTHING | the fee is for "each day that a document remains unfiled after the expiry of the period within which... | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 3 r 2(4)(f) | `o 3 r 2(4)(f) the Court may make a costs order or any other order` | NOTHING | "orders that are appropriate" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 3 r 2(6) | `o 3 r 2(6) the powers under this Rule affect another power of the Court under a written law` | NOTHING | the flat negative reaches "any other powers of the Court under any written law" only | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 3 r 2(9) | `o 3 r 2(9) the application under paragraph (8) may be made by the applicant` | NOTHING | "may be made by or on behalf of the party affected" says who may, not who may not | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 3 r 5(6) | `o 3 r 5(6) the Court allows a further affidavit` | NOTHING | the flat negative applies "after the other party files his or her affidavit under paragraph (5)" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 3 r 6(1) | `o 3 r 6(1) the Form must be used with the variations the circumstances require` | NOTHING | "The Forms as set out in the practice directions ... with such variations as the circumstances requi... | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 3 r 6(2) | `o 3 r 6(2) the Forms are varied by practice directions` | NOTHING | "as the case may be" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 3 r 6(2) | `o 3 r 6(2) the Forms are varied by practice directions` | NOTHING | "as the case may be" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 3 r 6(2) | `o 3 r 6(2) the Forms are varied by practice directions` | NOTHING | "may be varied by practice directions issued with the approval of the Chief Justice or ... the Presi... | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 3 r 7(1) | `o 3 r 7(1) the document filed or used in Court is in the English language as required` | NOTHING | the requirement is for "All documents filed or used in Court" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 3 r 7(2) | `o 3 r 7(2) the document not in English is accompanied by a certified or verified translation` | NOTHING | the requirement is for "A document which is not in the English language" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 4 r 1(a) | `o 4 r 1(a) a person aged 18 or older but below 21 may be a party in their own name` | NOTHING | limb (a) is "a person who is 18 years of age or older but below 21 years of age" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 4 r 1(a) | `o 4 r 1(a) a person aged 18 or older but below 21 may be a party in their own name` | NOTHING | limb (a) is "a person who is 18 years of age or older but below 21 years of age" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 4 r 1(b) | `o 4 r 1(b) a person aged 21 or older may be a party in their own name` | NOTHING | limb (b) is "a person who is 21 years of age or older" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 4 r 1(b) | `o 4 r 1(b) a person aged 21 or older may be a party in their own name` | NOTHING | limb (b) is "a person who is 21 years of age or older" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 4 r 1(c) | `o 4 r 1(c) an entity with the capacity to sue or be sued may be a party in its own name` | NOTHING | limb (c) is "any entity with the capacity to sue or be sued" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 4 r 1(c) | `o 4 r 1(c) an entity with the capacity to sue or be sued may be a party in its own name` | NOTHING | limb (c) is "any entity" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 4 r 2(1)(a) | `o 4 r 2(1)(a) a person below 21 who does not come under Rule 1(a) must be represented by a litigation representative` | NOTHING | limb (a) is "a person who is below 21 years of age and who does not come under Rule 1( a )" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 4 r 2(1)(a) | `o 4 r 2(1)(a) a person below 21 who does not come under Rule 1(a) must be represented by a litigation representative` | NOTHING | limb (a) is "a person who is below 21 years of age" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 4 r 2(1)(b) | `o 4 r 2(1)(b) a person who lacks capacity must be represented by a litigation representative` | NOTHING | limb (b) is "a person who lacks capacity within the meaning of the Mental Capacity Act" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 4 r 2(3) | `o 4 r 2(3) the litigation representative may have an interest adverse to that of the person represented` | NOTHING | the flat negative is of an "interest adverse to that of the person he or she is representing" only | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 4 r 3(1)(a) | `o 4 r 3(1)(a) a person represented by a litigation representative under Rule 2(1)(b) must be represented by a solicitor` | NOTHING | limb (a) is "a person who is represented by a litigation representative under Rule 2(1)( b )" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 4 r 3(1)(b) | `o 4 r 3(1)(b) an entity with the capacity to sue or be sued must be represented by a solicitor` | NOTHING | limb (b) is "any entity with the capacity to sue or be sued" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 4 r 3(1)(b) | `o 4 r 3(1)(b) an entity with the capacity to sue or be sued must be represented by a solicitor` | NOTHING | limb (b) is "any entity" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 4 r 3(2) | `o 4 r 3(2) a registered trade union may be represented by an officer of the trade union` | NOTHING | the grant is of "A registered trade union" represented by "an officer of the trade union" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 4 r 3(3) | `o 4 r 3(3) the Court may give permission for an officer to act on behalf of the applicant` | NOTHING | the grant is "on an application by a company, variable capital company or limited liability partners... | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 4 r 3(4) | `o 4 r 3(4) the Court may give permission for an officer to act on behalf of the unincorporated association` | NOTHING | the grant is "on an application by an unincorporated association (other than a partnership or a regi... | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 4 r 3(6) “officer” | `o 4 r 3(6) a person is an officer of the body` | NOTHING | the definition of "officer" is "in relation to" the four bodies it names | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 4 r 4(2)(a) | `o 4 r 4(2)(a) the claimant must apply to the Court for an order during the period of validity for service` | NOTHING | the duty is "In any action brought against the estate of a deceased person" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 4 r 4(2)(a) | `o 4 r 4(2)(a) the claimant has applied to the Court as required` | NOTHING | the duty is "In any action brought against the estate of a deceased person" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 4 r 4(2)(b) | `o 4 r 4(2)(b) the Court may make the order` | NOTHING | the power is "In any action brought against the estate of a deceased person" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 4 r 4(2)(b) | `o 4 r 4(2)(b) the Court may make the order` | NOTHING | the sub-paragraph names the orders the Court may make and has no "only" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 4 r 4(4) | `o 4 r 4(4) the judgment or order binds the estate as if a grant had been made` | NOTHING | the effect is of "any judgment or order given or made in the action" brought against the estate | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 4 r 5(2) | `o 4 r 5(2) the Court must give directions at the case conference for the further conduct of the action` | NOTHING | paragraph (2) follows paragraph (1) and reaches the action that paragraph (1) keeps alive | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 4 r 6(2) | `o 4 r 6(2) the group has complied` | NOTHING | the duty is "Where a group of persons is suing under this Rule" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 4 r 6(3) | `o 4 r 6(3) the persons represented have been included as required` | NOTHING | the paragraph is "Where a group of persons is being sued under this Rule" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 4 r 6(4) | `o 4 r 6(4) the known members and the class have been included as required` | NOTHING | the paragraph is "Where there is a class of persons and all or any member of the class cannot be asc... | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 4 r 6(5) | `o 4 r 6(5) the judgment or order is binding on the person or class` | NOTHING | the paragraph says who is bound ("all the persons and the class named in the respective lists stated... | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 4 r 7 | `o 4 r 7 the Court may make a declaratory judgment or order` | NOTHING | the power is to make "a declaratory judgment or order" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 4 r 8(1) | `o 4 r 8(1) the party has given the notice of appointment as required` | NOTHING | the duty arises "Where a party who was not represented by a solicitor decides to appoint a solicitor... | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 4 r 8(2) | `o 4 r 8(2) the solicitor is deemed to be acting for the party` | NOTHING | the deeming is of "a solicitor who is appointed by a party at any stage of an action" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 4 r 8(2) | `o 4 r 8(2) the solicitor's business address is deemed to be the address for service of all documents` | NOTHING | the deeming is of the business address of "a solicitor who is appointed by a party at any stage of a... | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 4 r 8(3) | `o 4 r 8(3) the party must file and serve a notice of change of solicitor in Form 3 on all the parties` | NOTHING | the duty is of "A party who intends to change his or her solicitor" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 4 r 8(3) | `o 4 r 8(3) the party has given the notice of change as required` | NOTHING | the duty is of "A party who intends to change his or her solicitor" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 4 r 8(4) | `o 4 r 8(4) the party must file and serve a notice of intention to act in person in Form 4 on all the parties` | NOTHING | the duty is of "A party who after having sued or defended by a solicitor, intends and is entitled to... | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 4 r 8(4) | `o 4 r 8(4) the party has given the notice of intention to act in person as required` | NOTHING | the duty is of "A party who after having sued or defended by a solicitor, intends and is entitled to... | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 4 r 8(6) | `o 4 r 8(6) the notice has taken effect` | NOTHING | the paragraph is of "Notice given under this Rule" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 4 r 8(6) | `o 4 r 8(6) the notice affects the rights of the solicitor and the party as between themselves` | NOTHING | the flat negative is of "Notice given under this Rule" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 4 r 8(7) | `o 4 r 8(7) the party has given notice of an address for service as required` | NOTHING | the duty arises "Where a party has no solicitor acting for the party on record" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 4 r 8(10) | `o 4 r 8(10) the requirements in Order 24A, Rule 4 apply in addition` | NOTHING | the paragraph is "In any application to which Order 24A applies" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 4 r 9(2) | `o 4 r 9(2) the application is made by summons in Form 6` | NOTHING | the requirement is for "An application for an order under this Rule" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 4 r 9(2) | `o 4 r 9(2) the summons has been served on the party for whom the solicitor acted as required` | NOTHING | the requirement is for "An application for an order under this Rule" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 4 r 9(3) | `o 4 r 9(3) the application is supported by an affidavit as required` | NOTHING | the requirement is for "The application mentioned in paragraph (2)" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 4 r 9(4) | `o 4 r 9(4) the order affects the rights of the solicitor and the party as between themselves` | NOTHING | the flat negative is of "An order in Form 7 made under this Rule" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 4 r 9(6) | `o 4 r 9(6) notice must be served in the manner prescribed by the Legal Aid and Advice Act` | NOTHING | the duty is of the "Notice that a solicitor has ceased to act for an assisted person pursuant to par... | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 4 r 9(6) | `o 4 r 9(6) the notice has been served as required` | NOTHING | the duty is of the "Notice that a solicitor has ceased to act for an assisted person pursuant to par... | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 5 r 1(1) | `o 5 r 1(1) the party has the duty to consider amicable resolution of the dispute` | NOTHING | the duty is of "A party to any proceedings" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 5 r 1(1) | `o 5 r 1(1) the party has considered amicable resolution as the duty requires` | NOTHING | the duty is of "A party to any proceedings" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 5 r 1(2) | `o 5 r 1(2) the party is to make an offer of amicable resolution before commencing the action` | NOTHING | the duty is for a party who is "commencing the action" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 5 r 1(2) | `o 5 r 1(2) the party has complied before commencing the action` | NOTHING | the duty is for a party who is "commencing the action" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 5 r 1(4) | `o 5 r 1(4) the party may reject an offer of amicable resolution` | NOTHING | the flat negative is of "A party to any proceedings" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 5 r 2(1) | `o 5 r 2(1) the offer or rejection is in writing as required` | NOTHING | the requirement is for "An offer of amicable resolution and any rejection" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 5 r 2(3) | `o 5 r 2(3) the terms cannot yet be relied upon or made known to the Court` | NOTHING | the bar is of "The terms of an offer that has been made and not accepted" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 5 r 2(4) | `o 5 r 2(4) the offer has expired under this paragraph` | NOTHING | the paragraph is of an offer "which does not state an expiry date" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 5 r 3(1) | `o 5 r 3(1) the Court may order the parties to attempt to resolve the dispute by amicable resolution` | NOTHING | the power is over "the parties" and "the dispute" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 5 r 3(2) | `o 5 r 3(2) the Court must have regard to the Ideals and all other relevant circumstances` | NOTHING | the duty is "In deciding whether to exercise its power under paragraph (1)" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 5 r 3(2) | `o 5 r 3(2) the Court has had regard as required` | NOTHING | the duty is "In deciding whether to exercise its power under paragraph (1)" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 5 r 3(4) | `o 5 r 3(4) the contents of the sealed document may be referred to` | NOTHING | "its contents may be referred to on any issue of costs" has no "only" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 5 r 3(5) | `o 5 r 3(5) the Court may suggest solutions for the amicable resolution of the dispute` | NOTHING | the power is over "the dispute" between "the parties" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 6 r 3(5) | `o 6 r 3(5) the renewed originating claim or originating application is endorsed as required` | NOTHING | the requirement is for one "in respect of which validity has been extended" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 6 r 3(6) | `o 6 r 3(6) paragraphs (1) and (4) apply to the originating claim` | NOTHING | the flat negative reaches "an originating claim relating to Admiralty causes and matters" only | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 6 r 5(2) | `o 6 r 5(2) the originating claim has the medical report and the statement of special damages annexed` | NOTHING | the requirement is for a claim "for personal injuries" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 6 r 5(3) | `o 6 r 5(3) the originating claim may be endorsed in that way` | NOTHING | "may be endorsed generally ... or with a statement of claim in Form 9" says how it may, not how it m... | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 6 r 6(1) | `o 6 r 6(1) the notice is filed and served within 14 days after the statement of claim is served` | NOTHING | the paragraph reaches "A defendant who is served an originating claim in Singapore" only; paragraph ... | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 6 r 6(2) | `o 6 r 6(2) the notice is filed and served within 21 days after the statement of claim is served` | NOTHING | the paragraph reaches "A defendant who is served out of Singapore" only; paragraph (1) has the defen... | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 6 r 6(4) | `o 6 r 6(4) filing and serving the notice is treated as a submission to jurisdiction or a waiver of improper service` | NOTHING | the flat negative reaches "such a notice" only | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 6 r 7(1) | `o 6 r 7(1) the defence is filed and served within 21 days after the statement of claim is served` | NOTHING | the paragraph reaches "A defendant who is served in Singapore" only; paragraph (2) has the defendant... | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 6 r 7(2) | `o 6 r 7(2) the defence is filed and served within 5 weeks after the statement of claim is served` | NOTHING | the paragraph reaches "A defendant who is served out of Singapore" only; paragraph (1) has the defen... | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 6 r 7(6) | `o 6 r 7(6) a defence filed under paragraph (4) is treated as a submission to jurisdiction` | NOTHING | the flat negative reaches "A defence filed under paragraph (4)" only | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 6 r 8(1) | `o 6 r 8(1) the counterclaim is filed and served with the defence as required` | NOTHING | the requirement is for a defendant who "intends to counterclaim" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 6 r 12(1) | `o 6 r 12(1) the defendant must file and serve the defendant's affidavit` | NOTHING | the paragraph reaches "A defendant who is served in Singapore" only; paragraph (2) has the defendant... | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 6 r 12(2) | `o 6 r 12(2) the defendant must file and serve the defendant's affidavit` | NOTHING | the paragraph reaches "A defendant who is served out of Singapore" only; paragraph (1) has the defen... | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 6 r 12(1) | `o 6 r 12(1) the defendant's affidavit is filed and served within 21 days after service of the originating application` | NOTHING | the paragraph reaches "A defendant who is served in Singapore" only; paragraph (2) has the defendant... | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 6 r 12(2) | `o 6 r 12(2) the defendant's affidavit is filed and served within 5 weeks after service of the originating application` | NOTHING | the paragraph reaches "A defendant who is served out of Singapore" only; paragraph (1) has the defen... | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 6 r 12(5) | `o 6 r 12(5) an affidavit filed under paragraph (3) is treated as a submission to jurisdiction` | NOTHING | the flat negative reaches "An affidavit filed under paragraph (3)" only | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 6 r 12(6) | `o 6 r 12(6) a further affidavit may be filed` | NOTHING | the flat negative applies "after the defendant files the defendant’s affidavit on the merits" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 6 r 14 | `o 6 r 14 the counterclaim is included in the defendant's affidavit as required` | NOTHING | the requirement is for a defendant who "intends to make a counterclaim" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 7 r 1(1)(b) | `o 7 r 1(1)(b) a document may be served by ordinary service` | NOTHING | the paragraph reaches "Any document that is required to be served under these Rules" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 7 r 1(2) | `o 7 r 1(2) the Court may dispense with personal service, ordinary service or service altogether` | NOTHING | "in an appropriate case" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 7 r 2(2) | `o 7 r 2(2) the person may effect personal service` | NOTHING | "The following persons may effect personal service" names who may and does not say who may not | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 7 r 4(2) | `o 7 r 4(2) the person is deemed the agent of the owner or of the charterer of the ship` | NOTHING | the deeming is for "An agent of a ship" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 7 r 7(2) | `o 7 r 7(2) the Court may order that method of substituted service` | NOTHING | "any method of substituted service that is effective in bringing the document to the notice of the p... | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 8 r 1(2) | `o 8 r 1(2) the claimant must apply to the Court by summons without notice, supported by affidavit` | NOTHING | the requirement is for a claimant who applies "To obtain the Court’s approval" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 8 r 1(2) | `o 8 r 1(2) the application for the Court's approval is made as required` | NOTHING | the requirement is for a claimant who applies "To obtain the Court’s approval" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 8 r 1(4) | `o 8 r 1(4) the Court's approval is not required for service of the document` | NOTHING | paragraph (4) reaches "court documents other than the originating process" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 8 r 2(2) | `o 8 r 2(2) the documents may be sent to the entity by the serving party` | NOTHING | paragraph (2) reaches sending "to the entities in paragraph (1)(c), (d) and (e) by the serving party... | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 8 r 2(2) | `o 8 r 2(2) the serving party must engage a solicitor` | NOTHING | the duty is of "the serving party who" sends the documents under this paragraph | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 8 r 2(2) | `o 8 r 2(2) the serving party has engaged a solicitor as required` | NOTHING | the duty is of "the serving party who" sends the documents under this paragraph | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 8 r 2(3) | `o 8 r 2(3) the solicitor has sent them to the Registrar with a letter as required` | NOTHING | the duty arises only "Where" the documents have to be sent from the Government of Singapore | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 8 r 2(4) | `o 8 r 2(4) the document must be accompanied by a translation` | NOTHING | the duty is for a document "which is to be served outside Singapore" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 8 r 2(4) | `o 8 r 2(4) the document is accompanied by the translation as required` | NOTHING | the duty is for a document "which is to be served outside Singapore" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 8 r 2(5) | `o 8 r 2(5) the translation is certified as required` | NOTHING | the duty is for "The translation" of paragraph (4) | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 8 r 2(6) | `o 8 r 2(6) it may be done under this Rule` | NOTHING | the flat negative reaches what is done "under this Rule" that is "contrary to the laws of the foreig... | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 8 r 3(b) | `o 8 r 3(b) the originating process is deemed to have been duly served` | NOTHING | the deeming is of an originating process sent under sub-paragraph (b) | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 8 r 4(1) | `o 8 r 4(1) the Registrar of the State Courts must send the originating process to the Registrar of the Supreme Court` | NOTHING | paragraph (1) reaches an originating process "issued in the State Courts which is to be served out o... | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 8 r 4(1) | `o 8 r 4(1)(a) it has been sent by the Registrar of the State Courts to the Registrar of the Supreme Court` | NOTHING | paragraph (1) reaches an originating process "issued in the State Courts which is to be served out o... | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 8 r 4(1) | `o 8 r 4(1)(b) it has been served in accordance with the Rules for an originating process issued in the Supreme Court` | NOTHING | paragraph (1) reaches an originating process "issued in the State Courts which is to be served out o... | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 8 r 4(2) | `o 8 r 4(2) the Registrar of the Supreme Court must transmit the certificate to the Registrar of the State Courts` | NOTHING | the duty is for "Every certificate of service received ... in respect of such service" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 8 r 4(2) | `o 8 r 4(2) the certificate has been transmitted as required` | NOTHING | the duty is for "Every certificate of service received ... in respect of such service" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 8 r 4A(1) | `o 8 r 4A(1) this Rule applies to the service` | NOTHING | "This Rule applies to the service out of Singapore, under Article 3 of the Hague Service Convention"... | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 8 r 4A(3) | `o 8 r 4A(3) the person has a known address as required` | NOTHING | the requirement is of "The person mentioned in paragraph (1)" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 8 r 4A(4) | `o 8 r 4A(4) the person must file in the Registry a request for service in the current version of Part 1 of the Model Form` | NOTHING | the duty is of "A person who wishes to serve any document mentioned in paragraph (1) out of Singapor... | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 8 r 4A(4) | `o 8 r 4A(4) the request has been filed with the documents the Rule requires` | NOTHING | the duty is of "A person who wishes to serve any document mentioned in paragraph (1) out of Singapor... | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 8 r 4A(5) | `o 8 r 4A(5) the Registrar must send the documents to the central authority` | NOTHING | the duty is for "the documents filed under paragraph (4)" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 8 r 4A(5) | `o 8 r 4A(5) the Registrar has sent the documents as required` | NOTHING | the duty is for "the documents filed under paragraph (4)" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 8 r 4A(6) | `o 8 r 4A(6) Rule 2(3) applies to the service` | NOTHING | the flat negative reaches "any service under this Rule" only | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 8 r 5(1) | `o 8 r 5(1) the person must file in the Registry the request, the sealed copy and the translation` | NOTHING | the duty is of "a person who wishes to serve an originating process on a High Contracting Party to t... | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 8 r 5(1) | `o 8 r 5(1) the person has filed in the Registry what the Rule requires` | NOTHING | the duty is of a person who wishes to serve on a High Contracting Party, "Upon obtaining the Court’s... | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 8 r 5(2) | `o 8 r 5(2) the translation is certified as required` | NOTHING | the duty is for "Every translation filed under paragraph (1)( c )" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 8 r 5(3) | `o 8 r 5(3) the serving party must engage a solicitor` | NOTHING | the duty is "for the purposes of filing the necessary documents under paragraph (1)" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 8 r 5(3) | `o 8 r 5(3) the serving party has engaged a solicitor as required` | NOTHING | the duty is "for the purposes of filing the necessary documents under paragraph (1)" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 8 r 5(4) | `o 8 r 5(4) the Registrar must send the documents to the Ministry of Foreign Affairs` | NOTHING | the duty is for "the documents filed under paragraph (1)" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 8 r 5(4) | `o 8 r 5(4) the Registrar has sent the documents as required` | NOTHING | the duty is for "the documents filed under paragraph (1)" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 8 r 6(1) | `o 8 r 6(1) the person must file in the Registry the request, the sealed copy and the translation` | NOTHING | the duty is of "a person who wishes to serve an originating process on a State, as defined in sectio... | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 8 r 6(1) | `o 8 r 6(1) the person has filed in the Registry what the Rule requires` | NOTHING | the duty is of a person who wishes to serve on a State, "Upon obtaining the Court’s approval under R... | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 8 r 6(2) | `o 8 r 6(2) the translation is certified as required` | NOTHING | the duty is for "Every translation filed under paragraph (1)( c )" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 8 r 6(3) | `o 8 r 6(3) the serving party must engage a solicitor` | NOTHING | the duty is "for the purposes of filing the necessary documents under paragraph (1)" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 8 r 6(3) | `o 8 r 6(3) the serving party has engaged a solicitor as required` | NOTHING | the duty is "for the purposes of filing the necessary documents under paragraph (1)" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 8 r 6(4) | `o 8 r 6(4) the Registrar must send the documents to the Ministry of Foreign Affairs` | NOTHING | the duty is for "the documents filed under paragraph (1)" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 8 r 6(4) | `o 8 r 6(4) the Registrar has sent the documents as required` | NOTHING | the duty is for "the documents filed under paragraph (1)" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 8 r 6(6) | `o 8 r 6(6) the request is accompanied by the summary as required` | NOTHING | the duty arises "Where the State is a Contracting State to the Hague Service Convention" | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 8 r 7(1) | `o 8 r 7(1) the solicitor for the serving party must give an undertaking in writing` | NOTHING | the duty is of the solicitor "for the serving party" in respect of "the service requested" under thi... | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 8 r 7(1) | `o 8 r 7(1) the solicitor has given the undertaking in writing as required` | NOTHING | the duty is of the solicitor "for the serving party" in respect of "the service requested" under thi... | a power given for named cases denies it in every other case (`JUST FALSE`) |
| B O 8 r 8 | `o 8 r 8 the certificate or letter is evidence of the service and its date` | NOTHING | "is evidence of those facts" says what such a certificate or letter proves and does not say that no ... | a power given for named cases denies it in every other case (`JUST FALSE`) |

### Reading a result: FALSE and NOTHING (roc1)

Status header (verification): this is how the code in this folder answers, read from the FALSE-kind and NOTHING-kind comments (542 of them in the layer-1 modules at the time of writing: 281 FALSE-kind, 261 NOTHING-kind, counted by `work/fk.py`); it is not a statement about what a court would do.

**Caveat on every answer, stated once (O 3 r 2(1)).**
"Unless the context otherwise requires and subject to any other written law, all requirements in these Rules are subject to the Court's discretion to order otherwise in the interests of justice, even if they are expressed using imperative words such as 'must', 'is to' or 'shall'."
So a `JUST TRUE` or `JUST FALSE` below says what the Rules say, and the Court may order otherwise.
The Court's own order is not threaded through the functions as an input.

**What a "no" (`JUST FALSE`) is in this part.**
- A duty the text states in its own words and the party has not done: "must file and serve ... within 14 days" and it was not filed and served in time.
- A period the text fixes in its own words, once it has passed (ruling (a) of 2026-11-05); the code checks the last day only, and a day before the period begins is not tested.
- A "where", "if", "when", "upon" or "whenever" condition that is not met (ruling (b) and (c)); for example the Court's power to dismiss "if no party attends" when someone attends.
- A flat negative ("cannot", "may not", "does not need", "is not treated as"): ruling N2.
- A definition that "means" a closed list, for something not on the list.

**What "not covered" (`NOTHING`) is in this part.**
- A power the text gives for named cases, asked about a case it does not name ("the Court may ..." in a case outside those named, with no "only").
- A scope limit with no "only": paragraph (1) of O 6 r 6 reaches "a defendant who is served an originating claim in Singapore"; asked of a defendant served out of Singapore it answers NOTHING, because paragraph (2) is the one that reaches that defendant.
- An "unless", "except" or "without the Court's approval" that lifts a bar: the bar is lifted, and the text does not then grant the thing (so the answer is NOTHING, not YES).
- An "only if": the condition is necessary; when it is met the answer is NOTHING (the text does not say the thing is allowed), when it is not met the answer is JUST FALSE.
- A list the text does not close, a term the Rules leave to another Act (the Trade Unions Act, the Companies Act, the Apostille Act 2020), and a case the text does not reach: service at exactly 5 p.m., the end of a period of months in a shorter month, a period of hours.
- Never read `NOTHING` as no.

**A date, a number or a choice cannot be `NOTHING`.**
Where a result is a DATE, a NUMBER or a constructor of a list, the function has a yes/no twin that can say "not covered" (for example `o 3 r 3 the period can be counted under this Rule` beside the last day).
A caller must never turn `NOTHING` into `FALSE`.

## Seams (roc1)

Status header (verification): read off the layer-1 modules and the PLAN.md tables (section 5 and the roc1 appendix) in this run.
The brief says to name seam inputs "as PLAN.md section 8 names it"; PLAN.md section 8 is "What the keel left to the parts" and the seam rules are in its section 5, which is what is followed.

**Seams this part answers (the lead wires them at the merge).**

| asked by | answered here | function | type |
| --- | --- | --- | --- |
| every rule with a period (S-T1) | O 3 r 3 | `o 3 r 3 the last day for doing the act` | DATE |
| a rule with an earliest day (S-T1b) | O 3 r 3 | `o 3 r 3 the first day on which the act may be done` | DATE |
| a rule that decides whether an act was in time (S-T2) | O 3 r 4 | `o 3 r 4 the last day as extended or shortened` | MAYBE DATE (`NOTHING` = not extended or shortened) |
| every "must serve ... within" for service not through the electronic filing service (S-S1) | O 7 r 8 | `o 7 r 8 the day service is deemed effected` (twin: `o 7 r 8 this Rule deems the day of service`) | MAYBE DATE |
| O 1 r 3(1) "Ideals" | O 3 r 1(2) | `o 3 r 1(2) the objective is one of the Ideals` | MAYBE BOOLEAN |
| O 1 r 3(1) "originating claim" | O 6 r 5 | `o 6 r 5 the document commences an action in Court as described` | MAYBE BOOLEAN |
| O 1 r 3(1) "originating application" | O 6 r 11 | `o 6 r 11 the document commences an action in Court as described` | MAYBE BOOLEAN |

**Seams this part takes as inputs (an answer that lives in another part's range or outside the sources).**

| asking section | answering section | input as named in the function | type |
| --- | --- | --- | --- |
| O 2 r 10(7); O 2 r 12(8) | O 18 Divisions 2 and 4 (roc3) | `the appeal is filed under Division 2 or Division 4 of Order 18` | BOOLEAN |
| O 4 r 3(6) "Court", head (e)(ii) | O 18 Division 2 (roc3) | the constructor `o 4 r 3(6) an appeal to a District Court under Division 2 of Order 18` | choice from a list |
| O 4 r 8(10) | O 24A r 4 (roc6) | `Order 24A applies to the application` | BOOLEAN |
| O 7 r 6 | O 59 r 3 (roc11) and s 20 of the Government Proceedings Act | the rule only says that they apply, so the function returns that; no input is taken for what they then provide | |
| O 7 r 8 | O 28 (roc7), written law | `a written law or another Rule provides otherwise` | BOOLEAN |
| O 4 r 8, r 9; O 7 r 3(c) | "solicitor" (the Legal Profession Act, through the keel) | stated as a fact (for example `a party who was not represented by a solicitor decides to appoint a solicitor`), not through the keel's `legal profession act s 2 the person is a solicitor` | BOOLEAN |
| O 4 r 3(6) "company", "limited liability partnership", "manager", "partner", "registered trade union", "variable capital company"; O 3 r 8(2) "apostille", "foreign public document" | the Companies Act, the Limited Liability Partnerships Act, the Trade Unions Act, the Variable Capital Companies Act 2018, the Apostille Act 2020 (not among the sources) | a MAYBE BOOLEAN input for what the other Act says, passed through; NOTHING-kind (points outside the text) | MAYBE BOOLEAN |
| O 8 r 2(1)(b) | the Third Schedule (roc12), the list of Civil Procedure Conventions | `the Hague Service Convention governs service in the foreign country`, `another Civil Procedure Convention governs ...` (facts) | BOOLEAN |

The appendix also lists the sections of other parts that cite this part's sections (O 3 r 2, r 6, r 8; O 4 r 1, r 5; O 5; O 6 r 1, r 2, r 4, r 5, r 6, r 7, r 8, r 9, r 11; O 7 r 2, r 3, r 4, r 8; O 8 as a whole, r 2, r 4A); each is answered by the function that carries the cited label, listed in the coverage table.

**Seams I found that PLAN.md lacks or names differently.**
- PLAN.md names a seam input `o N r M <what you ask of it>`; for citations of a whole Division or Order (O 18 Divisions 2 and 4, O 24A, O 28) no single rule is named in the text, so the input is named for the fact asked (the table above) and the lead may rename it when wiring.
- O 2 repeats O 6 on the notice of intention to contest and the defence (see finding 5); the overview rules are answered on their own words, and the lead decides whether the merged file calls the Order 6 function from the Order 2 one.
- I did not call the keel's `o 1 r 3(1) a person is a claimant`, `... a defendant`, `a decision-maker sitting in a court is the Court` and the other terms PLAN.md section 6.1 lists for roc1 (the Court alone occurs 175 times): my functions take the role or the fact as the person states it (for example `the defendant is served the originating claim in Singapore`), which is a choice (assumed, not ruled), not a re-encoding of the definition.
  The only keel functions called are `o 1 r 3(1) a day is a non-court day`, `o 1 r 3(1) a report is a medical report` and `o 1 r 3(1) a statement is a statement of the special damages claimed`.

## Dependencies

Status header (verification): `grep '^IMPORT'` over the shipped modules, this run.
- Every layer-1 module imports `prelude`, `daydate`, `roc-core` and `roc-definitions`, the keel's read-only files in this folder; `daydate` is used for `add months` (O 3 r 3) and the date arithmetic.
- Within this part: the Order modules that decide timeliness import `roc1-order-3-time` (Orders 2, 3, 4, 6, 7 and 8); `roc1-order-4` also imports `roc1-order-6`; `roc1-seat` imports every `roc1-order-N` module; each test file imports the module it tests; `roc1-duties.l4` imports only the keel.
- No module from `DEPENDENCIES/sg-interpretation-act/` is copied or imported: O 3 r 3(1) says the Interpretation Act does not apply to the calculation of time in these Rules, and the Rules count their own periods in r 3 ("none copied, none needed").
- No other Singapore Act is staged; each term borrowed from another Act is an input (see Seams).
- `NEEDS-CORE.md` is not written: no core type was lacking (the types this part declares carry their provision's label, for example `o 4 r 8(8) the deemed address for service`, `o 6 r 1 the mode of commencing proceedings`, `o 7 r 3 the manner of ordinary service`, and the duty types in `roc1-duties.l4`).

## Unstable dialect

None found in this range, and no unstable binary was run: every deadline here counts from one anchor, which `WITHIN n` states directly on main, and the step from a missed duty to the other party's power (O 6 r 6(5), r 7(7), r 9(3)) is held as a decision function, so no second encoding was written.

## What the text turns out to say

Status header (verification): each finding was read off the text lines cited and checked against the function named; the assertion that pins it is in the tests of the same module.
"Not an answer" means the code returns `NOTHING` there and a lawyer may read the text differently.

1. **Five o'clock is neither "before" nor "after".** O 7 r 8(1) deems service before 5 p.m. effected on that day and r 8(2) deems service after 5 p.m. effected the next day; service at exactly 5 p.m. falls in neither.
   `o 7 r 8 the day service is deemed effected` answers `NOTHING` at 1,020 minutes after midnight (a date cannot say no), and its yes/no twin `o 7 r 8 this Rule deems the day of service` answers `JUST FALSE` there, since neither "when" holds (fork F10).
2. **A period of months can have no last day.** O 3 r 3(2) reads "month" as a calendar month and the Rules do not say where a period of months ends when the later month has no corresponding day (31 August plus 3 months).
   `o 3 r 3(2) a period of calendar months from a date ends on the corresponding day` answers `NOTHING` there, and `daydate`'s `add months`, which clamps to the end of the shorter month, is not used to fill the gap.
   `roc1-cases-seat.l4` pins it through O 6 r 3(1) (an originating claim issued on 31 August 2026).
3. **"Beginning with the date of its issue" counts the day of issue; "after a date" does not.** O 6 r 3(1) makes an originating claim valid for service for 3 or 6 months "beginning with the date of its issue", so the last day is the day before the corresponding date (issued 5 November 2026: 4 February 2027 for 3 months, 4 May 2027 for 6).
   O 3 r 3(3) says a period "after or from" a date "begins immediately after that date", so the same length counted by r 3(3) ends a day later.
4. **A deadline counted backwards also moves forward** (fork F1), **and clear days "after" a date have no last day** (fork F2).
5. **Order 2 restates Order 6 and does not match it.** O 2 r 4(1) says a defendant "has to file and serve" a notice of intention to contest and gives no period, where O 6 r 6(1), (2) give 14 days (served in Singapore) or 21 days (out of Singapore); O 2 r 4(2) lets the claimant apply for judgment "upon proving that the originating claim with a statement of claim has been served", where O 6 r 6(5), (6) require Form 11 and a memorandum of service in Form 12.
   O 2 r 5 and O 6 r 7 likewise: O 2 r 5(1) has no period, O 6 r 7(1), (2) give 21 days or 5 weeks.
   Each is answered on its own words (`o 2 r 4(1) the defendant has to file and serve a notice of intention to contest or not contest the claim` has no period; `o 6 r 6(1) the notice is filed and served within 14 days after the statement of claim is served` has), and the merged file should not make one call the other without a ruling.
6. **Two modes of commencement can both be mandatory** (fork F5): O 6 r 1(2) and r 1(3)(c) can hold on the same facts, and the text does not choose.
7. **"Court" has overlapping heads** (fork F6): an appeal from a General Division matter to the Court of Appeal with no permission given below is within O 4 r 3(6)"Court"(a)(ii) and (c)(i), and the definition states no precedence.
8. **O 4 r 6(5) names two of the three lists.** The judgment binds the persons "named in the respective lists stated in paragraphs (3) and (4)"; the list of claimants of paragraph (2) is not mentioned (fork F7).
9. **O 8 r 2(1) has no method list where approval is not required** (fork F8): its opening words are "Where the Court's approval has been obtained under Rule 1(2)", and r 1(3), (4) say approval is not required in two cases.
10. **O 8 r 7(1) gives the undertaking no time and no trigger** beyond "the service requested" (fork F9); r 7(2) does give 14 days for paying on request.
11. **O 7 r 7(3) names no actor.** "Substituted service is to be effected within 14 days after the order of the Court" is a duty without a bearer, so it has a decision function (`o 7 r 7(3) substituted service is effected within 14 days after the order`) and no PARTY in `roc1-duties.l4`.
12. **O 4 r 2(3) is a state, not an act.** "A litigation representative must not have any interest adverse to that of the person he or she is representing" cannot be traced as an act at a time; it is `o 4 r 2(3) the litigation representative may have an interest adverse to that of the person represented` (JUST FALSE, a flat negative) and a row in the Jural relations table.
13. **The rate of interest is stated, so it is not an input.** O 6 r 6(7) and r 7(8) fix 5.33% per year from the date of the originating process to the date of judgment; `o 6 r 6(7) the yearly rate of interest the Court may direct` is that constant.
    The fee in O 3 r 2(4)(e) ($50 a day) is likewise stated and is a constant.
    O 2 r 10(7) and r 12(8) require security for the costs of an appeal and state no amount; no function here computes one (the duty is yes or no), and the numbers asked of the person are facts (days, dates, the sum on which interest is computed).
    What the two paragraphs do state is how many securities: one for each respondent or one for each set of respondents represented by the same firm of solicitors; `o 2 r 10(7) the number of sets of respondents for which security is to be provided` and `o 2 r 12(8) the number of sets of respondents for which security is to be provided` count the sets, and the text does not say who chooses between the two counts.
14. **Definitions that point at other Acts stay open.** "company" (Companies Act), "limited liability partnership", "manager" and "partner" (Limited Liability Partnerships Act), "registered trade union" (Trade Unions Act), "variable capital company" (Variable Capital Companies Act 2018), "apostille" and "foreign public document" (Apostille Act 2020) take a `MAYBE BOOLEAN` for what the other Act says and pass it through; none is encoded from memory.
15. **No table, form or flowchart in the range carries content.** The Forms of O 3 r 6 are cited, not set out; the flowchart of O 2 r 15 is announced and absent from the text.
    Amendment notes ("[S 780/2023 wef 01/12/2023]") follow some provisions and are not rules.
16. **Not every duty with a named bearer is a PARTY rule.** `roc1-duties.l4` traces 17 duties (the ones with a named bearer, an act, and one period in days from one anchor or no time).
    The other "must" or "has to" provisions with a named bearer (for example O 2 r 3(2), r 4(1), r 5(1); O 2 r 10(3), (7), (9) and r 12(3), (8), (9); O 4 r 4(2)(a), r 8(4), r 8(7); O 5 r 1(2); O 6 r 8(1), r 10(1); O 8 r 1(2), r 2(3), r 5(1), (3), r 6(1), (3); the list is not exhaustive) are decision functions in their Order modules and are not traced.
    A passive "must" with no named bearer (O 6 r 4, O 6 r 5(6), (7), O 6 r 11(4), (5), O 7 r 7(3)) has no PARTY by design.

### What the text does not answer

- Service at exactly 5 p.m. (finding 1); the end of a period of months in a shorter month (finding 2); a period of hours (Rule 3 counts days, weeks and months only).
- Whether an originating claim may be served by ordinary service despite O 6 r 4 (F4); which mode of commencement prevails when both are mandatory (F5); which head of "Court" prevails (F6).
- What the Court does after a party's "without the Court's approval" is satisfied: the bar is lifted and no grant follows (O 2 r 9(3), (4), (8); O 6 r 3(4)).
- Whether the claimants' list of O 4 r 6(2) is bound by the judgment (F7); how the methods of O 8 r 2(1) apply where approval is not required (F8); when the undertaking of O 8 r 7(1) is given (F9).
- The consequence, other than the claimant's power, of failing to file a notice, defence or affidavit in time (the text states only the power to apply for judgment).
- The rate of interest on a judgment by default on a counterclaim: O 6 r 9(3) lets the defendant apply for that judgment and says nothing of interest, while r 6(7) and r 7(8) give 5.33% a year for judgments under r 6 and r 7 only; there is no function for it, and the coverage row for O 6 r 9(3) says so.
- The flowchart announced by O 2 r 15: the text announces it and does not contain it, so there is no function and the coverage row is inert with the gap stated.
- Who chooses between security for each respondent and security for each set of respondents represented by one firm (O 2 r 10(7), r 12(8)).

## What the main binary does not accept

Status header (verification): each item was met in this run on `l4-main-109` (1.6.109) and is shown with how it presents.
**Loud** failures print an error; the **silent** one returns a wrong answer with exit code 0.

Loud.
1. `#ASSERT <a duty> EQUALS FULFILLED` is refused: "Trying to check equality on types that do not support it".
   A regulative rule (`PARTY ... MUST ... WITHIN ... HENCE ... LEST ...`) can only be run with `#TRACE`, and the outcome read by eye.
   Each duty in `roc1-duties.l4` therefore has its expected outcome in a comment beside the `#TRACE`, and the same duty is also a decision function in layer 1 that the tests do assert.
2. `` `WAIT UNTIL` n `` in a `#TRACE` body is "could not find a definition": main 1.6.109 spells the clock advance `WAITUNTIL n`.
3. A nested `GIVEN ... MEANS` inside a test file is "unexpected GIVETH": test fixtures must be top-level definitions.
4. `CONCAT "a" name " b"` (no commas) does not parse; `CONCAT "a", name, " b"` does, and nesting or parenthesising a `CONCAT` as an argument failed in the same way.
5. An `ELSE` followed on the next line by an `IF` at the same indentation is a parse error; indent the inner `IF`.
6. `IMPORT` finds only modules in the importing file's own folder, so a cases file cannot sit in a subfolder.

Silent.
7. `NOT a AND b` means `NOT (a AND b)`.
   A 15-day consent extension once came back `JUST TRUE` through this; every `NOT` in the shipped files is parenthesised.
8. `l4 run` exits 0 when an assertion fails or is refused; `check.sh` counts the assertion lines instead of trusting the exit code.
9. A `#TRACE` of a `MUST` with no `WITHIN` that is simply waited out prints the duty back (still owed) and not a breach; that is the intended reading for a duty with no time in the text (O 4 r 8, O 8 r 4 and r 7(1)).

## Checks (`check.sh` output)

Status header (verification): printed by `check.sh` in this folder at the end of the run, pasted unedited.

Baseline it replaced: the keel's own run (`inputs/KEEL-NOTES.md`) printed `TOTAL (3 modules)` with 0 errors and 278 satisfied; the keel's tests file (`roc-definitions-tests.l4`) is not in this folder, so here the two keel modules contribute 0 satisfied.

```
target: main. Each module is run with your l4 and with the main build below; the main columns must match.
main build: 1.6.108 (main, 2ae7c9b, 2026-11-02)
module                                    errors satisfied  failed  refused  expected | errors satisfied  failed  refused  main
roc-core.l4                                    0         0       0        0         0 |      0         0       0        0  same
roc-definitions.l4                             0         0       0        0         0 |      0         0       0        0  same
roc1-cases-seat.l4                             0       218       0        0         0 |      0       218       0        0  same
roc1-duties.l4                                 0         0       0        0         0 |      0         0       0        0  same
roc1-order-2.l4                                0         0       0        0         0 |      0         0       0        0  same
roc1-order-3-time.l4                           0         0       0        0         0 |      0         0       0        0  same
roc1-order-3.l4                                0         0       0        0         0 |      0         0       0        0  same
roc1-order-4.l4                                0         0       0        0         0 |      0         0       0        0  same
roc1-order-5.l4                                0         0       0        0         0 |      0         0       0        0  same
roc1-order-6.l4                                0         0       0        0         0 |      0         0       0        0  same
roc1-order-7.l4                                0         0       0        0         0 |      0         0       0        0  same
roc1-order-8.l4                                0         0       0        0         0 |      0         0       0        0  same
roc1-seat.l4                                   0         0       0        0         0 |      0         0       0        0  same
roc1-tests-order-2.l4                          0       203       0        0         0 |      0       203       0        0  same
roc1-tests-order-3-time.l4                     0        83       0        0         0 |      0        83       0        0  same
roc1-tests-order-3.l4                          0       129       0        0         0 |      0       129       0        0  same
roc1-tests-order-4.l4                          0       308       0        0         0 |      0       308       0        0  same
roc1-tests-order-5.l4                          0        53       0        0         0 |      0        53       0        0  same
roc1-tests-order-6.l4                          0       223       0        0         0 |      0       223       0        0  same
roc1-tests-order-7.l4                          0        88       0        0         0 |      0        88       0        0  same
roc1-tests-order-8.l4                          0       218       0        0         0 |      0       218       0        0  same
TOTAL (21 modules)                             0      1523       0        0           |      0      1523       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
(target main: every module has the same four counts on the main build. That rules out a module main rejects and a difference an assertion shows; it does not see a different TRACE outcome, or any difference no assertion exercises)
```

What `check.sh` does not see, checked by hand on 2026-11-05 by `work/checkextra.py` (which stops if any of these fails):
- **Traces.** `roc1-duties.l4` holds 56 `#TRACE`s of 17 duties: 16 end FULFILLED, 23 end in BREACH and 17 print the duty back as still owed.
  Each trace's outcome matches the "expected ..." comment written beside it (a script compared the 56 outcomes with the 56 comments), and the output printed by `l4-main-109` and `l4-main-108` is identical, line for line.
- **Layout diagnostics.** No module prints "is at the end of the file" or "follows code on its line".
- **Citations.** `srcrefs.py check --strict` over all `roc1-*.l4` files: 913 src: lines, 416 runs, 416 locators, 0 problems.
- **Assertions written equal assertions satisfied** for every test and cases file: 1,523 written (grep of `^#ASSERT`), 1523 satisfied, 0 failed, 0 refused, on both builds (21 modules in all).
