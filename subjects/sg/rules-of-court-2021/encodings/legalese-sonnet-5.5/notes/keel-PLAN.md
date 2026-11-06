# PLAN.md -- Rules of Court 2021 (Singapore): the shared vocabulary and the plan for the twelve parts

Written by the keel agent, 2026-11-05.
The text is a plain-text rendering of G.N. No. S 914/2021 (current version as at 5 November 2026) made by a converter script from Singapore Statutes Online.
It is not the official text, and nothing in this encoding is verified against the official text.

**Status of this file (rule 1, written down so it cannot be misread).**
**Both `roc-core.l4` AND `roc-definitions.l4` are distributed to every part, read-only, in its folder, and a part may import both (the lead, 2026-11-05).**
`roc-definitions-tests.l4` is NOT distributed; do not import it.
Landed and checked: `roc-core.l4`, `roc-definitions.l4` and `roc-definitions-tests.l4` compile on the main builds 1.6.109 and 1.6.108 with no error and no warning, and the 289 assertions in the tests pass on both (`check.sh` output is in `NOTES.md`).
`roc-definitions.l4` imports only `prelude`, `daydate` and `roc-core`, and compiles on both builds in a folder holding just `roc-core.l4` and `roc-definitions.l4` (`Check succeeded.`, exit 0 on each; with `roc-core.l4` missing it fails with "Module not found: roc-core", exit 1).
Proposed, not landed: everything this file says the parts will do, and every seam input it names.
No part has been written, so no seam has been wired to an answer.

## 0. Read this first

1. **What you are given.** `roc-core.l4` and `roc-definitions.l4` (both read-only; import both), this file, `RULE-INDEX.md`, the text, and the Commons guide.
   `roc-definitions.l4` encodes Order 1: Rule 3 (the general definitions: "Court", "non-court day", "working day", "solicitor" and the rest) and Rule 2 (when the Rules apply).
   **Call its functions by their exact names; never re-encode a general definition.**
   Section 4A lists every function with its arguments, and section 6.1 lists, for each part, the functions whose terms occur in its range.
   **A part takes a seam input only for an answer that lives in another part's range** (section 5), or for a fact that lives outside the sources.
2. **Where the work stops.** You encode only your own line ranges (section 6).
   Order 1 and the Table of Derivations are the keel's.
   A provision outside your range is never encoded by you: it is a seam (section 5).
3. **The text uses a NO-BREAK SPACE (U+00A0) between `Order` and its number**, and a non-breaking hyphen (U+2011) in words like `non-court`, `evidence-in-chief` and `sub-paragraph`.
   `grep 'Order 9'` with an ordinary space misses nearly every cross-reference (330 have the no-break space before the digit; 20 have a plain space).
   Search with `python3 -I` and `\s`, or `grep -P 'Order\xa0'`.
   The keel's first count of cross-references was 17 lines because of exactly this; the Appendix has 145 citation entries under "You ask" (an entry can cover several lines of the text).
4. **A part may not edit the core or the definitions module, and never waits for either.**
   A type or constructor you need that the core lacks is defined in your own module under your label prefix, recorded in `NEEDS-CORE.md` in your sandbox (one line: the name, its fields, the section that needs it), and the lead hoists it at the merge.
5. **Do not run `cabal`, do not touch git.** Write files only in your own sandbox.
6. **Start every module with these imports** (all four sit in your folder, which is where `IMPORT` looks):

   ```l4
   IMPORT prelude
   IMPORT daydate
   IMPORT `roc-core`
   IMPORT `roc-definitions`
   ```

   Import only what you use.
   Do not import another part's module (it is not in your folder).

## 1. The naming rule (binding, and the reason the merge works)

A name defined in two modules that are imported together cannot be used at all.
The whole encoding is imported together at the merge, so **no two parts may define the same name**.

- **Every top-level name a part defines begins with the label of the section it implements**, in the Act's own numbering and in lower case for `o` and `r`:
  `o 6 r 7(1) the defence is served in time`, `o 46A r 3(2) the court must order affidavits`, `o 18 r 29(6)(a) ...`.
  A schedule item is `sch 4 part 2 item 5 the fee`; a schedule paragraph is `sch 1 para 2 ...`.
  Parentheses inside a backtick name are fine on both main builds (the keel's files use them throughout).
  Keep the upper-case suffix of a lettered rule or Order: `o 8 r 4A(7)`, `o 46A r 1`.
- **This applies to everything**: functions, constants, helper functions, record types, enum types, constructors, record fields.
  A helper that serves several rules takes the label of the first rule that needs it.
  Two names inside one section must still differ.
- The label names the section the function IMPLEMENTS, not the one it is called from.
  The name must not claim more than the section says: `o 25 r 2(2)(a) the value of a liquidated claim`, not `what the claim is worth`.
- **Types and constructors shared across parts live only in the core.** Do not redeclare `Litigant`, `Period`, `Moment` and the rest.
- **Order-local definitions are yours, under your prefix.**
  Several Orders redefine words the core uses, for their own Order only: `Court` (O 4 r 3, O 37, O 42, O 69), `judgment` (O 19, O 42), `order` (O 27, O 59), `non-party` (O 22), `entity` (O 28), `claimant` and `third party` (O 63), `respondent` (O 19 r 41).
  Where your Order redefines a word, do NOT use the core's noun or O 1 Rule 3's meaning for it: define the Order's own type under your prefix.
- **Every name beginning `o 1 r ` belongs to the keel** (`roc-definitions.l4`): never define one, in any form, in a part.
  If you need a variant of a general definition, you define your own function under your own label and call the keel's inside it.
- **File names.** Every module of part `roc3` begins `roc3-`, for example `roc3-order-15.l4`, tests `roc3-order-15-tests.l4`.
  The keel's are `roc-core.l4`, `roc-definitions.l4`, `roc-definitions-tests.l4`.
- **Names that already exist, so never define them unprefixed.**
  `prelude` exports `count`, `elem`, `any`, `all` and others; `daydate` exports `Date`, `Day`, `Month`, `Year`, `Week`, `May`, `March`, `Monday` to `Sunday`, `January` to `December`, `is weekend`, `is weekday`, `Weekday of`, `add months`, `the day after`, `the earlier of` and others.
  A prefixed name cannot collide with them; an unprefixed one can, and the error ("multiple definitions", "could not find") points somewhere else.

## 2. What FALSE and NOTHING mean in your answers (the brief's rule, applied)

Every decision function answers `MAYBE BOOLEAN` unless the provision is better answered by a constructor.
`JUST TRUE`, `JUST FALSE`, `NOTHING`.
Put `-- FALSE-kind (the text says no in its own words): "<the quoted words>"` on every branch that answers JUST FALSE or a "no" constructor, and `-- NOTHING-kind (<why>)` on every branch that answers NOTHING or a "not covered" constructor, where `<why>` is one of: silent, list not closed, includes, undefined term, points outside the text, limited by its own wording.
The keel's `roc-definitions.l4` shows both comments on every branch.
A caller must never turn NOTHING into FALSE.

Three consequences the keel met in Order 1 and that every part will meet:

- **A period the text fixes in its own words answers `JUST FALSE` outside it (ruled 2026-11-05, ruling (a) in your brief; this replaces the earlier rule that said `NOTHING`).**
  "must be filed and served within one month after ..." fixes how long.
  So a function `... is filed in time` answers `JUST TRUE` inside the period and `JUST FALSE` outside it, with the FALSE-kind comment quoting the period's words.
  Where the text itself names a consequence ("the claimant may apply for judgment", "late filing fee of $50"), encode the consequence as its own rule.
  List every such branch under `## Marginal readings for a lawyer` in your `NOTES.md`, under reading (a) (a failed condition counts as the text's no).
- **"Means" closes a list; "includes" does not.**
  A closed definition gives `JUST FALSE` for a non-member, with the FALSE-kind comment quoting the "means".
  An "includes" definition gives `JUST TRUE` for a member and `NOTHING` for a non-member (list not closed).
- **A power ("the Court may") is a grant limited by its own wording.**
  A case outside what the power names answers `NOTHING`.
  A flat negative ("shall not", "is not", "no person", "do not apply") answers `JUST FALSE`, and where the text names the bearer, a prohibition (`SHANT`) is derived from that answer.
  Record the Hohfeld kind in `NOTES.md` under `## Jural relations`, not in the type of the answer.

**O 3 r 2(1) is a caveat on every answer in the Rules, and it is NOT an input.**
"all requirements in these Rules are subject to the Court's discretion to order otherwise in the interests of justice, even if they are expressed using imperative words such as 'must'".
Do not thread `the Court has ordered otherwise` through your functions.
State it once in your `NOTES.md` under `### Reading a result: FALSE and NOTHING`, and the lead will say it once in the merged file.

## 3. Writing L4 that the main builds accept (measured on 1.6.109 and 1.6.108 by the keel unless marked)

Read `dialects.md` of the `writing-l4-rules` skill first.
Each item below was run on both builds by the keel, either in the keel's three files or in a scratch probe (the daydate calls, `any`, `all`, `count` and `BRANCH` in probes; `elem`, positional patterns, the apostrophe constructor, field equality and the rest in the keel's files).

- **Calling a keel function.** Arguments are positional, in the order of the `GIVEN` block shown in section 4A: `` `o 1 r 3(1) a day is a working day` day calendar ``.
  A `MAYBE BOOLEAN` answer is handled with `CONSIDER ... WHEN JUST x THEN ... WHEN NOTHING THEN ...`, or in a `BRANCH IF f args EQUALS JUST TRUE THEN ...` (the keel's gathered `o 1 r 2` function shows both).
- **Constructor patterns bind positionally and take no `WITH`**: `CONSIDER p WHEN Entity incorporated THEN ...`; `WHEN Ctor WITH x` is a parse error on main.
  The skills show `WITH`; the binary governs.
- **List membership is `elem x xs`**, not `x IS IN xs`.
  `any`, `all`, `count` are in the prelude; a lambda is `GIVEN x YIELD x EQUALS 2`.
- **A section `GIVEN` is not accepted** (dialects.md): put a `GIVEN` on every rule that reads the input.
  `TYPICALLY` on a field, an opaque `DECLARE T` with no body, `REFUSE`, `#ASSERT REFUSED`, `BECAUSE` (except on `LEST BREACH`), sets (`SET OF`), `YMD` and `@lang` are not accepted either.
- **Parenthesise every `NOT`**: `NOT a AND b` is `NOT (a AND b)`.
- **One `#ASSERT` per line.** Write the expected value beside it, from the text.
- **Dates**: `Date day month year`, never `YMD` and never your own `YMD`.
  `d PLUS n` and `d MINUS e` (a number of days), `d AT MOST e`, and the daydate functions `is weekend`, `Weekday of` (0 is Sunday), `add months`, `the day after` and `the earlier of` all work on main; each of those five is a backtick name applied to its arguments, for example `` `the earlier of` d e ``.
  `Date 29 2 2023` rolls to 1 March 2023 (dialects.md; not re-run by the keel).
- **Equality on enum constructors, on STRING and on `MAYBE` values works** (`x EQUALS JUST (Date 1 4 2022)`, `x EQUALS NOTHING`).
  Equality on a whole record was not measured: compare fields (`p's `period length` EQUALS 14`).
- **`BRANCH IF ... THEN ... OTHERWISE ...`** works with the arms indented under `BRANCH`; a multi-line `OR` condition is fine inside brackets.
- **A constructor name with an apostrophe works** (`Magistrate's Court` in the core).
- **`#CHECK` on an overloaded name is an error**: leave no `#CHECK` in a deposited file.
- Your run must print no `DiagnosticSeverity_Error` and no `_Warning`, and `check.sh` (given) must read every module the same on both builds.
  `check.sh` counts errors and assertions only: also run `l4 check` on each module and read it for `is at the end of the file` and `follows code on its line` (an `@ref` placed wrongly).
- **Quote the text mechanically** (`python3 -I srcrefs.py quote RAW N M`) and run `python3 -I srcrefs.py check --refs RAW <your .l4 files>` to 0 problems.
  `@ref O 6 r 7(1) (src:539-545)` goes immediately above the declaration it supports, never above a `§` heading or a directive.

## 4. The core: `roc-core.l4`, one line per type

| type | members | what it is for |
| --- | --- | --- |
| `Court level` | `General Division`, `Appellate Division`, `Court of Appeal`, `District Court`, `Magistrate's Court`, `Singapore International Commercial Court`, `Family Division` | where proceedings are heard |
| `Court system` | `Supreme Court`, `State Courts` | which establishment; the Fourth Schedule has a column for each |
| `Decision maker` | `The court itself`, `A Judge`, `A District Judge`, `A Magistrate`, `The Registrar` | who takes a decision |
| `Sitting` | `sitting court level`, `sitting decision maker` | a decision-maker sitting in a court |
| `Kind of decision` | `A judgment`, `An order`, `A direction` | O 3 r 4(1): "judgment, order or direction" |
| `Role in the action` | `Claimant`, `Defendant`, `Third party`, `Fourth party`, `Appellant`, `Respondent`, `Non-party` | the position a person is in; a person in the position of a claimant in a counterclaim is `Claimant` |
| `Kind of person` | `Natural person` (age in years), `Entity` (incorporated) | O 4 r 1 sorts by age and by entity |
| `How a party acts` | `Acts in person`, `Acts by solicitor`, `Acts by litigation representative` | representation |
| `Litigant` | `litigant role`, `litigant kind`, `litigant acting` | one person in one action |
| `Document kind` | `Originating claim`, `Originating application`, `Statement of claim`, `Defence`, `Defence and counterclaim`, `Reply`, `Reply to a defence and counterclaim`, `Summons`, `Summons without notice`, `Affidavit`, `Notice of intention to contest or not contest`, `Notice of appeal` | the documents O 1, O 3 and O 6 name; any other document is a `STRING` in your module |
| `Time unit` | `Days`, `Clear days`, `Working days`, `Weeks`, `Months`, `Hours` | the units the text counts in (surveyed: days, clear days, working days, weeks, months, hours) |
| `Count direction` | `After the anchor`, `Before the anchor` | "within 14 days after" or "not less than 7 clear days before" |
| `Period` | `period length`, `period unit`, `period direction` | a period as a rule states it |
| `Court calendar` | `public holidays` (a list of dates) | the public holidays the asker states; the Rules do not list them |
| `Moment` | `day of the moment`, `minutes after midnight` | a date and a time of day; 5 p.m. is 1020 |
| `Method of service` | `Personal service`, `Ordinary service`, `Substituted service`, `Service through the electronic filing service` | O 7 and O 28 |
| `Place of service` | `Served in Singapore`, `Served out of Singapore` | O 6 periods differ by this |
| `Service event` | `service of` (a Document kind), `service method`, `service place`, `service moment` | one act of service |
| `Filing event` | `filing of`, `filing moment` | one act of filing |
| `Action` | `action commenced by`, `action commenced on`, `action court level` | the facts O 1 Rule 2 asks first |

Money is a `NUMBER` of Singapore dollars; there is no money type.
The core has **no rules**: whether service was effected, when a document counts as filed and what a period's last day is are rules, and live in the sections that say so (section 5).

## 4A. The definitions module: `roc-definitions.l4`, exact names and arguments

Generated from the file by a script; the order is the file's.
A `GIVEN` marked **[input from another part]** is an answer the keel's function cannot compute: the part that holds the answer passes its own function's result, and every other part takes it as an input (section 5.2).
All other arguments are facts a witness could state (a date, a `Sitting`, a yes/no).
`MAYBE BOOLEAN` means `JUST TRUE`, `JUST FALSE` or `NOTHING` (section 2).
The module also declares four enums for its own functions (each constructor is named for its paragraph): `o 1 r 2 kind of proceedings`, `o 1 r 2(4)(a) how the decision came to be made`, `o 1 r 2(4)(c) how the time for the permission application begins` and `o 1 r 2(5)(b) the time provided under the Rule`; a part may use them.

| name | arguments (name: type) | answers |
| --- | --- | --- |
| `o 1 r 1 the day these Rules come into operation` | none | a constant: a DATE |
| `o 1 r 2(2) a saving or transitional provision has effect` | `the provision is set out in the First Schedule as a saving or transitional provision`: A BOOLEAN  **[input from another part]** | A MAYBE BOOLEAN |
| `o 1 r 2(6) these Rules apply to the proceedings in the lower Court following the appeal` | `the decision appealed against was made in proceedings governed by the revoked Rules of Court`: A BOOLEAN; `the Court of Appeal or the Appellate Division hears the appeal under these Rules`: A BOOLEAN | A MAYBE BOOLEAN |
| `o 1 r 2(3)(a) these Rules apply to civil proceedings commenced on or after 1 April 2022` | `action`: AN Action; `kind`: A `o 1 r 2 kind of proceedings` | A MAYBE BOOLEAN |
| `o 1 r 2(3)(b) these Rules apply with modifications to an appeal or originating application to an appellate court` | `action`: AN Action; `the decision is of a lower Court and was made in proceedings to which the revoked Rules of Court apply`: A BOOLEAN | A MAYBE BOOLEAN |
| `o 1 r 2(4)(a) the date after which the one month for the notice of appeal runs` | `how`: A `o 1 r 2(4)(a) how the decision came to be made`; `the date the order was pronounced`: A DATE; `the date the appellant first had notice of the order`: A DATE; `the date of the refusal`: A DATE; `section 29B(4)(b) of the Supreme Court of Judicature Act the date mentioned`: A MAYBE DATE; `the date the judgment or order appealed against was pronounced`: A DATE | A MAYBE DATE |
| `o 1 r 2(4)(a) one month` | none | a constant: a Period |
| `o 1 r 2(4)(a) the notice of appeal is filed and served within one month` | `the date the notice of appeal is filed`: A DATE; `the date the notice of appeal is served`: A DATE; `o 3 r 3 the last day for doing the act`: A DATE  **[input from another part]** | A MAYBE BOOLEAN |
| `o 1 r 2(4)(b) the period after permission is granted` | `the application for permission to appeal was filed on`: A DATE | A Period |
| `o 1 r 2(4)(b) the notice of appeal is filed and served within the period after permission` | `the date the notice of appeal is filed`: A DATE; `the date the notice of appeal is served`: A DATE; `o 3 r 3 the last day for doing the act`: A DATE  **[input from another part]** | A MAYBE BOOLEAN |
| `o 1 r 2(4)(c) the date after which the 7 working days for the permission application run` | `how`: A `o 1 r 2(4)(c) how the time for the permission application begins`; `the date of the decision of the lower Court`: A DATE; `the date the Judge affirmed, varied or set aside the decision after further arguments`: A DATE; `the date the Judge certified, or is deemed to have certified, that no further arguments are required`: A DATE; `the time the judgment or order was extracted`: A MAYBE DATE | A DATE |
| `o 1 r 2(4)(c) seven working days` | none | a constant: a Period |
| `o 1 r 2(4)(c) the application for permission to appeal is filed and served in time with its documents` | `the date the application for permission is filed`: A DATE; `the date the application for permission is served`: A DATE; `o 3 r 3 the last day for doing the act`: A DATE  **[input from another part]**; `o 18 r 29(7) or o 19 r 26(7) the documents mentioned are filed and served with it`: A MAYBE BOOLEAN  **[input from another part]** | A MAYBE BOOLEAN |
| `o 1 r 2(5)(a) a paragraph applies to an application for permission mentioned in paragraph (4)(c)` | `order number`: A STRING; `rule number`: A STRING; `paragraph number`: A NUMBER | A MAYBE BOOLEAN |
| `o 1 r 2(5)(b) the time provided under the Rule is the time in paragraph (4)(c)(i) or (ii)` | `section 29B of the Supreme Court of Judicature Act applies`: A BOOLEAN | A `o 1 r 2(5)(b) the time provided under the Rule` |
| `o 1 r 2(7) the Court may direct that a provision applies with suitable modifications` | `order number`: A STRING; `rule number`: A STRING; `the revoked Rules of Court apply to the proceedings`: A BOOLEAN | A MAYBE BOOLEAN |
| `o 1 r 2(8) these Rules apply to proceedings under the Criminal Procedure Code 2010` | `kind`: A `o 1 r 2 kind of proceedings`; `the Criminal Procedure Code 2010 or its subsidiary legislation provides otherwise`: A MAYBE BOOLEAN | A MAYBE BOOLEAN |
| `o 1 r 2(9) these Rules apply to proceedings in the Family Division of the High Court` | `action`: AN Action | A MAYBE BOOLEAN |
| `o 1 r 2(10) the proceedings are of a kind in sub-paragraphs (a) to (d)` | `action`: AN Action; `kind`: A `o 1 r 2 kind of proceedings` | A BOOLEAN |
| `o 1 r 2(10) these Rules apply to proceedings in or relating to the Singapore International Commercial Court` | `action`: AN Action; `kind`: A `o 1 r 2 kind of proceedings`; `the Court otherwise directs`: A BOOLEAN; `any other written law otherwise provides`: A BOOLEAN | A MAYBE BOOLEAN |
| `o 1 r 2(11) the provision is in the third column for the kind of proceedings` | `kind`: A `o 1 r 2 kind of proceedings`; `order number`: A STRING; `rule number`: A STRING | A BOOLEAN |
| `o 1 r 2(11) a provision of the Rules applies to proceedings of a kind in the Table` | `kind`: A `o 1 r 2 kind of proceedings`; `order number`: A STRING; `rule number`: A STRING | A MAYBE BOOLEAN |
| `o 1 r 2(12) these Rules apply to an appeal arising from proceedings mentioned in paragraphs (9) and (11)` | `it is an appeal`: A BOOLEAN; `it arises from proceedings in the Family Division or of a kind in the Table in paragraph (11)`: A BOOLEAN | A MAYBE BOOLEAN |
| `o 1 r 2(13) specific provisions do not apply, or apply with modifications, to the case` | `second schedule the case is in a category it sets out`: A MAYBE BOOLEAN  **[input from another part]** | A MAYBE BOOLEAN |
| `o 1 r 2 these Rules apply to the proceedings` | `action`: AN Action; `kind`: A `o 1 r 2 kind of proceedings`; `the decision is of a lower Court and was made in proceedings to which the revoked Rules of Court apply`: A BOOLEAN; `the Criminal Procedure Code 2010 or its subsidiary legislation provides otherwise`: A MAYBE BOOLEAN; `the Court otherwise directs`: A BOOLEAN; `any other written law otherwise provides`: A BOOLEAN; `it is an appeal arising from proceedings in the Family Division or of a kind in the Table in paragraph (11)`: A BOOLEAN | A MAYBE BOOLEAN |
| `o 1 r 3(1) a defined term has its defined meaning` | `the context otherwise requires`: A BOOLEAN | A MAYBE BOOLEAN |
| `o 1 r 3(1) proceedings commenced by a document are an action` | `document`: A `Document kind` | A MAYBE BOOLEAN |
| `o 1 r 3(1) a court is the appellate Court` | `the court is the one to which an appeal is brought or is being brought`: A BOOLEAN | A MAYBE BOOLEAN |
| `o 1 r 3(1) a court is the Appellate Division` | `level`: A `Court level` | A MAYBE BOOLEAN |
| `o 1 r 3(1) a person attends` | `the person appears`: A BOOLEAN; `the person appears by electronic, mechanical or other means`: A BOOLEAN; `the Court permitted those means`: A BOOLEAN | A MAYBE BOOLEAN |
| `o 1 r 3(1) a person is a bailiff` | `the person is the Registrar`: A BOOLEAN; `the person is a clerk or other officer of the Court charged with the duties of a bailiff`: A BOOLEAN | A MAYBE BOOLEAN |
| `o 1 r 3(1) a meeting is a case conference` | `o 9 r 1 the meeting is a case conference as described`: A MAYBE BOOLEAN  **[input from another part]** | A MAYBE BOOLEAN |
| `o 1 r 3(1) an instrument is a Civil Procedure Convention` | `third schedule the convention is set out in the Third Schedule`: A MAYBE BOOLEAN  **[input from another part]**; `the instrument is a convention, treaty or agreement between different States relating to civil procedure in the Court`: A BOOLEAN | A MAYBE BOOLEAN |
| `o 1 r 3(1) a person is a claimant` | `role`: A `Role in the action`; `the person is in the position of a claimant in a counterclaim`: A BOOLEAN | A MAYBE BOOLEAN |
| `o 1 r 3(1) a statement is a counterclaim` | `the statement sets out the material facts which constitute the cause of action`: A BOOLEAN | A MAYBE BOOLEAN |
| `o 1 r 3(1) limb (a) the General Division or a judge sitting in it` | `sitting`: A Sitting | A BOOLEAN |
| `o 1 r 3(1) limb (b) a District Court or a District Judge` | `sitting`: A Sitting | A BOOLEAN |
| `o 1 r 3(1) limb (c) the Appellate Division or the Court of Appeal, or a judge sitting in either` | `sitting`: A Sitting; `it is appropriate for a judge sitting in the Appellate Division or the Court of Appeal to act`: A BOOLEAN | A BOOLEAN |
| `o 1 r 3(1) limb (d) in cases where empowered, a Magistrate or the Registrar` | `sitting`: A Sitting; `the Magistrate or the Registrar is empowered to act in the case`: A BOOLEAN | A BOOLEAN |
| `o 1 r 3(1) a decision-maker sitting in a court is the Court` | `sitting`: A Sitting; `it is appropriate for a judge sitting in the Appellate Division or the Court of Appeal to act`: A BOOLEAN; `the Magistrate or the Registrar is empowered to act in the case`: A BOOLEAN | A MAYBE BOOLEAN |
| `o 1 r 3(1) a payment is within court fees` | `o 25 r 1 the payment is within court fees`: A MAYBE BOOLEAN  **[input from another part]** | A MAYBE BOOLEAN |
| `o 1 r 3(1) a document is a defence` | `the document is a defence`: A BOOLEAN; `the document is a defence to a counterclaim`: A BOOLEAN | A MAYBE BOOLEAN |
| `o 1 r 3(1) a person is a defendant` | `role`: A `Role in the action`; `the person is in the position of a defendant in a counterclaim`: A BOOLEAN | A MAYBE BOOLEAN |
| `o 1 r 3(1) a person is an entity` | `person`: A `Kind of person` | A MAYBE BOOLEAN |
| `o 1 r 3(1) a court is the General Division` | `level`: A `Court level` | A MAYBE BOOLEAN |
| `o 1 r 3(1) an objective is one of the Ideals` | `o 3 r 1(2) the objective is one of the Ideals`: A MAYBE BOOLEAN  **[input from another part]** | A MAYBE BOOLEAN |
| `o 1 r 3(1) a person sitting in a court is a Judge` | `sitting`: A Sitting; `it is appropriate for a judge sitting in the Appellate Division or the Court of Appeal to act`: A BOOLEAN; `the Magistrate or the Registrar is empowered to act in the case`: A BOOLEAN | A MAYBE BOOLEAN |
| `o 1 r 3(1) a court is the lower Court` | `the court is the one against whose judgment or order an appeal is brought or being brought`: A BOOLEAN | A MAYBE BOOLEAN |
| `o 1 r 3(1) a report is a medical report` | `the report substantiates all the personal injuries alleged in the statement of claim`: A BOOLEAN; `the claimant proposes to adduce the report in evidence as part of the case at the trial`: A BOOLEAN | A MAYBE BOOLEAN |
| `o 1 r 3(1) a day is a non-court day` | `day`: A DATE; `calendar`: A `Court calendar` | A MAYBE BOOLEAN |
| `o 1 r 3(1) a person is a non-party` | `the person is a party in the action`: A BOOLEAN; `the person participates in the action because of a statutory duty`: A BOOLEAN; `the person may be affected by the Court's decision in the action and participates because of that`: A BOOLEAN | A MAYBE BOOLEAN |
| `o 1 r 3(1) a person is an officer` | `establishment`: A MAYBE `Court system` | A MAYBE BOOLEAN |
| `o 1 r 3(1) a document is an originating application` | `document`: A `Document kind`; `o 6 r 11 the document commences an action in Court as described`: A MAYBE BOOLEAN  **[input from another part]** | A MAYBE BOOLEAN |
| `o 1 r 3(1) a document is an originating claim` | `document`: A `Document kind`; `o 6 r 5 the document commences an action in Court as described`: A MAYBE BOOLEAN  **[input from another part]** | A MAYBE BOOLEAN |
| `o 1 r 3(1) a document is an originating process` | `document`: A `Document kind` | A MAYBE BOOLEAN |
| `o 1 r 3(1) a document is a pleading` | `document`: A `Document kind` | A MAYBE BOOLEAN |
| `o 1 r 3(1) directions are practice directions` | `o 26 r 2 the directions are issued under Order 26, Rule 2`: A MAYBE BOOLEAN  **[input from another part]**; `issuer`: A `Court system`; `the Chief Justice approved them`: A BOOLEAN; `the Presiding Judge of the State Courts approved them`: A BOOLEAN | A MAYBE BOOLEAN |
| `o 1 r 3(1) a person is the Registrar` | `the court system of the case`: A `Court system`; `the person is the Registrar of`: A MAYBE `Court system` | A MAYBE BOOLEAN |
| `o 1 r 3(1) a reference to the Registry is to the Registry of the Registrar of the case` | `the court system of the case`: A `Court system`; `the Registry belongs to`: A `Court system` | A MAYBE BOOLEAN |
| `o 1 r 3(1) an instrument is the Rules` | `the instrument is the Rules of Court`: A BOOLEAN | A MAYBE BOOLEAN |
| `o 1 r 3(1) a person is the Sheriff` | `the person is a bailiff of the Supreme Court or of the State Courts`: A BOOLEAN | A MAYBE BOOLEAN |
| `o 1 r 3(1) signing or sealing is signing or sealing` | `done by a Judge, the Registrar or other officer of the Supreme Court or the State Courts`: A BOOLEAN; `done by electronic or other means`: A BOOLEAN | A MAYBE BOOLEAN |
| `o 1 r 3(1) a person is a solicitor` | `legal profession act s 2 the person is a solicitor`: A MAYBE BOOLEAN  **[input from another part]**; `the person is the firm that the solicitor is in`: A BOOLEAN; `the person is the Attorney-General, a Deputy Attorney-General or a Solicitor-General who is a party to or appears in the proceedings`: A BOOLEAN | A MAYBE BOOLEAN |
| `o 1 r 3(1) a statement is a statement of claim` | `the statement sets out the material facts which constitute the cause of action`: A BOOLEAN | A MAYBE BOOLEAN |
| `o 1 r 3(1) a statement is a statement of the special damages claimed` | `the statement gives full particulars of the special damages claimed for expenses and losses already incurred`: A BOOLEAN; `the statement gives an estimate of any future expenses and losses`: A BOOLEAN | A MAYBE BOOLEAN |
| `o 1 r 3(1) an application is a summons` | `it is an application to Court in an action or appeal`: A BOOLEAN; `it has to be served on other parties or non-parties or both`: A BOOLEAN | A MAYBE BOOLEAN |
| `o 1 r 3(1) an application is a summons without notice` | `it is an application to Court in an action or appeal`: A BOOLEAN; `it has to be served on other parties or non-parties or both`: A BOOLEAN | A MAYBE BOOLEAN |
| `o 1 r 3(1) a party is a third party` | `the party was brought into the action by`: A `Role in the action`; `an indemnity or contribution is sought against the party`: A BOOLEAN | A MAYBE BOOLEAN |
| `o 1 r 3(1) a party is a fourth party` | `the party was brought into the proceedings by`: A `Role in the action` | A MAYBE BOOLEAN |
| `o 1 r 3(1) a party is a further party` | `the party was brought into the proceedings by`: A `Role in the action` | A MAYBE BOOLEAN |
| `o 1 r 3(1) a day is a working day` | `day`: A DATE; `calendar`: A `Court calendar` | A MAYBE BOOLEAN |
| `o 1 r 3(2) a reference to a numbered Form is to this form` | `the form cited is numbered`: A STRING; `the form in the practice directions is numbered`: A STRING; `the form in the practice directions is the current version`: A BOOLEAN | A MAYBE BOOLEAN |

Most rules say "the Court" only to name who acts.
Call `o 1 r 3(1) a decision-maker sitting in a court is the Court` only where a rule's outcome turns on which decision-maker sits.
Likewise `o 1 r 3(1) a person is a solicitor` only where the rule's outcome turns on whether the person is one; its input `legal profession act s 2 the person is a solicitor` is a fact the asker states (section 2 of the Legal Profession Act is not among the sources).

## 5. Seams: a provision in one part whose answer another part's provision needs

A part cannot import another part.
**The dependent part takes the answer as an INPUT fact, a `GIVEN` named for the section the answer comes from, and does not encode the answering section itself.**
The input is written in the dependent part's function, e.g.
``GIVEN `o 3 r 3 the last day for doing the act` IS A DATE``.
The answering part encodes the section as a function whose result is that input's type, and the lead wires the two at the merge.
Every seam you take goes in your `NOTES.md` under `## Seams` as one line: the asking section, the answering section, the input name, its type.

### 5.1 The seams that every part meets (implicit in the text, not listed in the appendix)

An earlier draft listed "is it a working day / a non-court day / the Court / a Judge / the Registrar / a solicitor" as seams (S-D1, S-D2).
They are not seams any more: those are functions in `roc-definitions.l4` (section 4A) and a part calls them.

| id | asked by | answered by | input name | type |
| --- | --- | --- | --- | --- |
| S-T1 | every rule with a period (all parts, and O 1 r 2(4)) | O 3 r 3 (roc1): the count, including r 3(3)-(7) | `o 3 r 3 the last day for doing the act` | `DATE` |
| S-T1b | a rule that fixes an earliest day ("not before ...") | O 3 r 3 (roc1) | `o 3 r 3 the first day on which the act may be done` | `DATE` |
| S-T2 | a rule that decides whether an act was in time | O 3 r 4 (roc1): extension, shortening, one extension by consent of up to 14 days | `o 3 r 4 the last day as extended or shortened` | `MAYBE DATE` (`NOTHING` = not extended) |
| S-F1 | every "must file ... within" | O 28 r 10(1) (roc7): when a document filed through the electronic filing service is deemed filed | `o 28 r 10 the moment the document is deemed filed` | `Moment` |
| S-F2 | rules that turn on when time for service begins | O 28 r 11 (roc7) | `o 28 r 11 the moment time for service begins to run` | `Moment` |
| S-S1 | every "must serve ... within", for service not through the electronic filing service | O 7 r 8 (roc1): before 5 p.m. is that day, after is the next | `o 7 r 8 the day service is deemed effected` | `DATE` |
| S-S2 | the same, for service through the electronic filing service | O 28 r 12(3) (roc7) | `o 28 r 12 the moment service is deemed effected` | `Moment` |
| S-V1 | Fourth Schedule fee items and every rule that sets a fee by value (roc12, roc6) | O 25 r 2 (roc6): the value of the claim for court fees | `o 25 r 2 the value of the claim` | `NUMBER`; O 25 r 2(2)(d) says a claim of none of the listed kinds "is deemed to have a value of up to $1 million", a band and not a number: roc6 answers `1000000` for it and says so in its `NOTES.md`, which puts it in the Fourth Schedule's "up to $1 million" column (assumed, not ruled) |
| S-V2 | Fourth Schedule hearing fees (roc12) | O 25 r 5 to 7 (roc6): no hearing fee for some proceedings, winding-up hearing fee, criminal-proceedings exemption | `o 25 r 5 no hearing fee is payable` | `MAYBE BOOLEAN` |
| S-V3 | any rule that says a fee is payable (the Fourth Schedule's own text cites O 9, O 13, O 18, O 19, O 20, O 21, O 23, O 28, O 33, O 34, O 42, O 45 and O 46A, per the Appendix) | the Fourth Schedule item (roc12) | `sch 4 the fee for this document` | `NUMBER` |
| S-P1 | any rule that says "the practice directions" or a numbered Form | O 26 r 2 (roc6) and O 3 r 6 (roc1) | not an input: write the Form number as a `STRING` constant | |
| S-L1 | a rule that applies "Order X, Rule Y" and CHANGES it (O 59 imports O 9 r 17; O 33 r 25 imports O 14) | the imported section | `o X r Y <what you ask of it>` | `MAYBE BOOLEAN` by default |
| S-L2 | an OVERRIDE that switches another provision off (O 59 r 11, O 62 r 10, O 1 r 2(5)(a), O 46A r 3(1)) | the overridden section, in whatever part | not an input | |

**S-L2 in full.**
The overriding section is encoded in the overriding part, as a flat statement about the overridden provision, for example ``o 59 r 11(1) Order 22 applies to an order against the Government`` answering `JUST FALSE` with its FALSE-kind comment.
The overridden part does NOT thread an input for it (that would put an input about the Government on every enforcement rule), and its functions keep saying what their own section says.
The lead gathers overrides at the merge, by hand and in plain L4 (option B of ruling E1, guidance for hand-gathering only).
Where an override CHANGES content rather than switching it off, it is S-L1: the overriding part takes the base rule's answer as an input and encodes only the change.

S-T1 in full.
A part states each period it meets as a constant of the core type `Period` named for the section, for example

```l4
`o 6 r 6(1) the period for the notice of intention to contest` MEANS Period WITH
    `period length` IS 14
    `period unit` IS Days
    `period direction` IS `After the anchor`
```

and the number appears nowhere else in the rule.
It then decides timeliness by comparing the date of the act (from S-F1 or S-S1/S-S2) with the input `o 3 r 3 the last day for doing the act`, using the extended day from S-T2 when there is one.
The count itself ("the period begins immediately after that date", clear days, non-court days excluded if six days or less, the next court day if it expires on a non-court day) is O 3 r 3, in roc1, and no other part encodes it.
Tests in a part use made-up last days; the lead's merge replaces them with calls.
`roc-definitions.l4` shows the pattern in `o 1 r 2(4)(a)` to `(c)`.

### 5.2 The seams the keel has already met in its own range

The keel's functions in `roc-definitions.l4` take these as inputs (asking section in Order 1; the answering section is in a part's range).
When a part calls one of those keel functions: **the part that holds the answering section passes the result of its own function; every other part takes the input under the name in the table**, and the lead wires it at the merge.

| asked by | answered by | input name | type |
| --- | --- | --- | --- |
| O 1 r 3(1) "case conference" | O 9 r 1 (roc2) | `o 9 r 1 the meeting is a case conference as described` | `MAYBE BOOLEAN` |
| O 1 r 3(1) "Civil Procedure Convention" | the Third Schedule (roc12): the list of conventions | `third schedule the convention is set out in the Third Schedule` | `MAYBE BOOLEAN` |
| O 1 r 3(1) "court fees" | O 25 r 1 (roc6) | `o 25 r 1 the payment is within court fees` | `MAYBE BOOLEAN` |
| O 1 r 3(1) "Ideals" | O 3 r 1(2) (roc1) | `o 3 r 1(2) the objective is one of the Ideals` | `MAYBE BOOLEAN` |
| O 1 r 3(1) "originating application" | O 6 r 11 (roc1) | `o 6 r 11 the document commences an action in Court as described` | `MAYBE BOOLEAN` |
| O 1 r 3(1) "originating claim" | O 6 r 5 (roc1) | `o 6 r 5 the document commences an action in Court as described` | `MAYBE BOOLEAN` |
| O 1 r 3(1) "practice directions" | O 26 r 2 (roc6) | `o 26 r 2 the directions are issued under Order 26, Rule 2` | `MAYBE BOOLEAN` |
| O 1 r 3(1) "solicitor" | s 2 Legal Profession Act (not among the sources) | `legal profession act s 2 the person is a solicitor` | `MAYBE BOOLEAN` |
| O 1 r 2(2) | the First Schedule (roc12) | `the provision is set out in the First Schedule as a saving or transitional provision` | `BOOLEAN` |
| O 1 r 2(4)(c) | O 18 r 29(7) (roc3) and O 19 r 26(7) (roc4) | `o 18 r 29(7) or o 19 r 26(7) the documents mentioned are filed and served with it` | `MAYBE BOOLEAN` |
| O 1 r 2(13) | the Second Schedule (roc12; a heading only in this text) | `second schedule the case is in a category it sets out` | `MAYBE BOOLEAN` |

The reverse direction: roc3 and roc4 should expose O 18 r 29(7) and O 19 r 26(7) (the documents that go with an application for permission to appeal) as functions whose answer is `MAYBE BOOLEAN`; roc12 should expose the Third Schedule list, the First Schedule paragraphs 1 to 3 and the Second Schedule as functions of the same type; roc2, roc1 and roc6 likewise for O 9 r 1, O 3 r 1(2), O 6 r 5 and r 11, O 25 r 1 and O 26 r 2.

### 5.3 Seams by part: the mechanical list of every cross-Order citation (the floor, not the ceiling)

Built by script from the text: each line below is a place where an Order in one part's range cites "Order N" or "Order N, Rule M" in another part's range.
The script reads rules cited as "Rule 3(1)" as rule 3, and "Rules 3, 4, 5 and 12" as rule 3 only; the Schedules cited as "the Fourth Schedule" and the Acts' Schedules ("the First Schedule to the Act") are not in it, and are in section 7.
Line numbers are of the text file.
For each, the dependent part writes the input ``o N r M <what you ask of it>`` of type `MAYBE BOOLEAN` unless a number or a date is what it needs, and the answering part exposes a function the lead can wire.


## 6. The parts: ranges (copied unchanged from `inputs/PARTS.md`), Orders, and what each part answers

Line numbers are 1-based and inclusive, of `SCJA1969-S914-2021.txt` (12250 lines, 182290 words).
Every line belongs to exactly one agent.
The split falls on whole-Order boundaries (checked against `RULE-INDEX.md`), so no Order is shared.

| part | line ranges | words | Orders |
| --- | --- | --- | --- |
| keel | 1-136, 8830-12250 | 14050 | O 1 CITATION, APPLICATION AND DEFINITIONS; the Table of Derivations |
| roc1 | 137-727 | 12230 | O 2 OVERVIEW; O 3 GENERAL MATTERS; O 4 PARTIES TO PROCEEDINGS AND CAUSES OF ACTION; O 5 AMICABLE RESOLUTION OF CASES; O 6 COMMENCEMENT OF PROCEEDINGS; O 7 SERVICE IN SINGAPORE; O 8 SERVICE OUT OF SINGAPORE |
| roc2 | 728-1404 | 14780 | O 9 CASE CONFERENCES, APPLICATIONS IN ACTION, ETC.; O 10 THIRD PARTY AND SIMILAR PROCEEDINGS; O 11 PRODUCTION OF DOCUMENTS; O 12 EXPERT EVIDENCE; O 13 INJUNCTIONS, SEARCH ORDERS AND OTHER INTERIM RELIEF BEFORE TRIAL; O 14 PAYMENT INTO AND OUT OF COURT |
| roc3 | 1405-2230 | 19043 | O 15 COURT HEARINGS AND EVIDENCE; O 16 WITHDRAWAL AND DISCONTINUANCE; O 17 JUDGMENTS AND ORDERS; O 18 APPEALS FROM APPLICATIONS IN ACTIONS, REGISTRAR'S DECISIONS AND TRIALS OF ORIGINATING APPLICATION BY DISTRICT JUDGE OR MAGISTRATE |
| roc4 | 2231-2875 | 11904 | O 19 APPEALS FROM JUDGMENTS AND ORDERS AFTER TRIAL AND UNDER MEDICAL REGISTRATION ACT |
| roc5 | 2876-3555 | 11336 | O 20 APPEALS FROM TRIBUNALS AND CASE STATED; O 21 COSTS; O 22 ENFORCEMENT OF JUDGMENTS AND ORDERS |
| roc6 | 3556-4193 | 12531 | O 23 CONTEMPT OF COURT; O 24 PREROGATIVE ORDERS; O 24A POST-APPEAL APPLICATIONS IN CAPITAL CASES; O 25 COURT FEES; O 26 REGISTRY AND ADMINISTRATION; O 27 LODGMENT IN COURT, MONEY IN REGISTRY AND PAYMENT TO SHERIFF |
| roc7 | 4194-5050 | 22541 | O 28 ELECTRONIC FILING SERVICE; O 29 REFERRALS ON ISSUES OF LAW; O 29A REQUESTS FOR OPINIONS ON QUESTIONS OF FOREIGN LAW; O 30 REFERENCES UNDER ARTICLE 100 OF CONSTITUTION FOR ADVISORY OPINION; O 31 CONSTITUTIONAL CASE; O 32 ADMINISTRATION AND SIMILAR ACTIONS; O 33 ADMIRALTY PROCEEDINGS AND MARINE INSURANCE CLAIMS |
| roc8 | 5051-5510 | 8343 | O 34 ARBITRAL PROCEEDINGS; O 35 BILLS OF SALE ACT; O 36 BUILDING AND CONSTRUCTION INDUSTRY SECURITY OF PAYMENT ACT; O 37 CHOICE OF COURT AGREEMENTS ACT; O 38 COMPANIES ACT |
| roc9 | 5511-6101 | 13720 | O 39 COMPETITION ACT — APPLICATIONS UNDER SECTION 85 OF COMPETITION ACT; O 40 CORRUPTION, DRUG TRAFFICKING AND OTHER SERIOUS CRIMES (CONFISCATION OF BENEFITS) ACT; O 41 DEBENTURE HOLDERS' ACTION: RECEIVER'S REGISTER; O 42 DEBTORS ACT; O 43 DEFAMATION ACTIONS; O 44 DISABILITY; O 45 DISTRESS ACT |
| roc10 | 6102-6795 | 14841 | O 46 EMPLOYMENT ACT; O 46A EXPRESS TRACK FOR ACTIONS IN GENERAL DIVISION; O 47 INCOME TAX ACT; O 48 INTERNATIONAL ARBITRATION ACT; O 49 LAND TITLES (STRATA) ACT — COLLECTIVE SALE APPLICATIONS; O 50 LIMITED LIABILITY PARTNERSHIPS ACT; O 51 MONEYLENDERS' ACTIONS; O 52 MORTGAGE ACTIONS; O 53 MUTUAL ASSISTANCE IN CRIMINAL MATTERS ACT; O 54 OATHS AND DECLARATIONS ACT; O 55 OBTAINING EVIDENCE FOR FOREIGN COURTS, ETC.; O 56 PARTNERS |
| roc11 | 6796-7399 | 12256 | O 57 PERSONAL DATA PROTECTION ACT 2012; O 58 PROCEEDINGS ARISING OUT OF HIRE-PURCHASE AGREEMENTS; O 59 PROCEEDINGS BY AND AGAINST GOVERNMENT; O 60 RECIPROCAL ENFORCEMENT OF JUDGMENTS; O 61 SECURITIES AND FUTURES ACT — CIVIL LIABILITY ACTIONS; O 62 SECURITIES AND FUTURES ACT — CIVIL PENALTY ACTIONS; O 63 SECURITIES AND FUTURES ACT — ORDER FOR DISGORGEMENT AGAINST THIRD PARTY |
| roc12 | 7400-8829 | 14715 | O 64 SERVICE OF FOREIGN PROCESS; O 65 SIMPLIFIED PROCESS FOR PROCEEDINGS IN MAGISTRATE'S COURT OR DISTRICT COURT; O 66 SUMMARY PROCEEDINGS FOR POSSESSION OF LAND; O 67 TERRORISM (SUPPRESSION OF FINANCING) ACT; O 68 VARIABLE CAPITAL COMPANIES ACT 2018; O 69 UNMERITORIOUS OR VEXATIOUS PROCEEDINGS; O 70 VEXATIOUS LITIGANTS; the First, Second, Third and Fourth Schedules |

`RULE-INDEX.md` lists every rule start in each range with its line and heading, and for each Order the rule numbers present.
Use it to build the coverage table (one row per rule, plus one for each Order heading and each Division heading) and compare your table with it before you finish.
It was built by a script and has not been read rule by rule: a line it shows as a rule start that is a list item inside a rule is a script error; say so in your `NOTES.md` rather than inventing a rule.
Every Order has all its numbers from 1 to its last, plus the lettered rules 4A (O 8, O 64), 15A (O 53) and 1A (O 60): the index shows no number absent from the text.

**What the keel knows about each part's range, and how it knows.**
Three kinds of statement follow, kept apart: *heading* (read from the rule's heading in `RULE-INDEX.md`), *read* (the keel read the rule in the text), *appendix* (mechanical: the Appendix lists every place another part cites it).
The keel read Order 1 whole, Order 3 whole, Order 4 rules 1 and 2, Order 6, Order 7, Order 20, Order 25 rules 1 to 5 and the First to Fourth Schedule beginnings; for the rest it has the headings and the Appendix, and no statement below goes further.
For what other parts need from your sections, read the Appendix under your part's heading, "You are asked": it is the floor, built by script.

- **roc1** (O 2 to 8).
  *Read*: O 3 r 3 "Calculation of time" and r 4 "Extension or shortening of time" are the answers to S-T1, S-T1b and S-T2.
  O 7 r 8 "Time for service": service effected before 5 p.m. on a day is deemed effected that day, after 5 p.m. on the following day, "Subject to any written law and these Rules (including Order 28 ...)" (S-S1).
  O 3 r 2(4)(e): the Court may "impose a late filing fee of $50 for each day that a document remains unfiled".
  O 6 r 6(7) and r 7(8): interest at 5.33% a year when giving judgment; the same rate is in O 17 r 5 (roc3), O 21 r 29 (roc5) and O 33 r 21(10) (roc7), found by searching the text for `5.33` (lines 529, 540, 1690, 3116, 4868): each part writes the number in its own rule.
  O 6 r 6(1): 14 days after the statement of claim is served on a defendant served in Singapore; O 7 r 8: see above.
  O 8 r 4A(7) defines "Hague Service Convention" and "Model Form" (lines 699 to 700); O 64 r 4A (roc12, lines 7476 and 7478) defines both by reference to it.
  *Heading*: O 3 r 1 "Ideals", r 6 "Forms", r 8 "Use of foreign documents under Apostille Convention or Civil Procedure Convention"; O 4 r 1 to 9 (parties, litigation representative r 2, solicitor r 3); O 6 r 5 "Form and service of originating claim", r 11 "Forms of originating application"; O 8 r 2 "Methods of service out of Singapore".
- **roc2** (O 9 to 14).
  *Heading*: O 9 r 1 "General matters", r 17 "Summary judgment"; O 10 r 4, r 5, r 9 (third parties); O 11 r 2 "Order for production"; O 13 r 8 "Interim payments", r 9 "Receivers"; O 14 r 3 "Acceptance of money paid into Court", r 7 "Non-disclosure of payment into Court".
  *Appendix*: cited from the keel, roc1, roc3 to roc12; the Appendix is the list.
- **roc3** (O 15 to 18).
  *Heading*: O 15 r 17 "Definitions of this Division"; O 17 r 1 "Definition of this Order", r 2 "Effective date of orders", r 5 "Interest on money payable under orders"; O 18 r 29 "Permission to appeal" (the keel asks r 29(7)).
- **roc4** (O 19).
  *Heading*: O 19 r 26 "Permission to appeal" (the keel asks r 26(7)); r 41 "Appeals under section 59G of Medical Registration Act", which defines "respondent" for its own purposes (line 2874).
- **roc5** (O 20 to 22).
  *Read*: O 20 r 2 defines "record of proceedings" and "tribunal" ("includes any authority, person or body of persons authorised to make decisions under any written law but not any Court").
  *Heading*: O 21 r 1 "Definitions and general matters of this Order", r 29 "Interest on costs"; O 22 r 1 "Definitions of this Order".
- **roc6** (O 23 to 27).
  *Read*: O 25 r 1 defines "Court ADR service", "court fees" (which "includes" the listed fees: the keel asks this) and "court officer"; O 25 r 2 "Court fees" says how the value of a claim is found for the Fourth Schedule (S-V1: liquidated demand = the amount in the originating process; unliquidated = the party's estimate; probate = the estate; none of these = deemed up to $1 million; bill of costs = the total; both = the sum; foreign currency converted at the rate on the filing date; non-contractual interest excluded).
  *Heading*: O 25 r 5 "No hearing fee for some proceedings", r 6 "Hearing fee payable for winding up applications", r 7 "Exemption where cause or matter relates to criminal proceedings" (S-V2), r 8 "Court ADR fees in District Court"; O 26 r 2 "Practice directions"; O 23 r 11 "Form of committal order"; O 24A r 4 "Appointment of solicitor in application for PACC permission or PACC application"; O 27 r 15 "Sheriff to keep account".
- **roc7** (O 28 to 33).
  *Read*: O 28 r 10(1): a document filed using the electronic filing service and accepted is deemed filed "on the date and at the time that the document becomes capable of being retrieved" (S-F1); r 10(2) and (3): caveats under O 33 r 5 and r 14 are taken out of paragraph (1) and given their own rule, both inside this range, so not seams; O 28 r 11(1) and (3): the time for service begins from the time the Registrar's notification is received, and a notification received on a non-working day is deemed received on the next working day (S-F2); O 28 r 12(3): when a document served through the electronic filing service is deemed served (S-S2).
  *Heading*: O 28 r 1 "Definitions of this Order", r 17 "Interpretation, etc."; O 33 r 5 "Caveat against arrest" (the First Schedule paragraph 3 deems a revoked-Rules caveat to be one "issued under Order 33, Rule 5 of these Rules"), r 21 "Judgment by default", r 42 "Hearing of reference".
- **roc8 to roc10**: mostly one Order per Act or subject, by title: O 34 Arbitral Proceedings; O 35 Bills of Sale Act; O 36 Building and Construction Industry Security of Payment Act; O 37 Choice of Court Agreements Act; O 38 Companies Act; O 39 Competition Act, applications under section 85; O 40 Corruption, Drug Trafficking and Other Serious Crimes (Confiscation of Benefits) Act; O 41 Debenture Holders' Action: Receiver's Register; O 42 Debtors Act; O 43 Defamation Actions; O 44 Disability; O 45 Distress Act; O 46 Employment Act; O 46A Express Track for Actions in General Division; O 47 Income Tax Act; O 48 International Arbitration Act; O 49 Land Titles (Strata) Act, collective sale applications; O 50 Limited Liability Partnerships Act; O 51 Moneylenders' Actions; O 52 Mortgage Actions; O 53 Mutual Assistance in Criminal Matters Act; O 54 Oaths and Declarations Act; O 55 Obtaining Evidence for Foreign Courts, etc.; O 56 Partners.
  *Read*: O 46A r 3(1) "This Rule applies despite Order 9, Rule 8" (line 6148); r 4(1) "Order 9, Rule 9 continues to apply" (line 6159); r 4(3) "Without affecting Order 15, Rule 3(3)" (line 6167): read each as S-L1 or S-L2, case by case; r 1(5) cites "paragraph 4(1) of the Fourth Schedule to, read with section 29(b) of, the Supreme Court of Judicature Act 1969", the Act's schedule and not these Rules'.
  *Read*: O 53 r 1: "any reference to the Third Schedule is a reference to the Third Schedule to the Act"; O 49 (lines 6362 to 6389) cites "the First Schedule to the Act" (section 7, item 8).
- **roc11** (O 57 to 63).
  *Read*: **O 59 r 11(1)**: "Nothing in Order 22, Order 23 and Order 13, Rule 9 apply in respect of any order against the Government."
  **O 62 r 10**: "Order 5 and Order 14 do not apply to a civil penalty action."
  Both are S-L2 overrides: you encode them as flat statements about the overridden provisions, and the overridden parts (roc1, roc2, roc5, roc6) do not thread an input for them.
  *Heading*: O 59 r 3 "Service on Government" (cited by O 7 r 6, line 630).
  Where O 59 or O 62 cites a general Order and changes it, that is S-L1.
- **roc12** (O 64 to 70 and the Schedules).
  *Read*: First Schedule paragraphs 1 to 3 (lines 7748 to 7760): the revoked Rules "continue to apply" to the proceedings listed in paragraph 1 "unless the Court otherwise directs and subject to any written law"; paragraph 2 continues them in the lower Court after an appeal; paragraph 3 deems a revoked-Rules caveat against arrest to be one issued under O 33 r 5 of these Rules.
  The Second Schedule is a heading only in this text (lines 7761 to 7763); the keel's O 1 r 2(13) returns `NOTHING` for it.
  The Third Schedule (line 7764 on) is the list the keel's "Civil Procedure Convention" asks.
  *Appendix*: the Fourth Schedule cites O 9 r 25, O 13 r 4, O 18 (whole, r 16, 21, 25, 29, 33, 37), O 19 (whole, r 19, 26, 32, 37, 41), O 20 (whole, r 5), O 21, O 23 r 11, O 28, O 33 r 4, 13 and 42, O 34, O 42 r 3, O 45 r 3 and O 46A r 1 and r 3.
  **The Fourth Schedule is a table the converter flattened**: section 7, item 2.

### 6.1 Definitions functions each part should expect

Built by script: a function appears under a part when its defined term occurs in that part's line range (case-sensitive match where the text capitalises the term, with the no-break space and non-breaking hyphen normalised); the number is the count of occurrences.
A mention is a prompt to look, not an obligation to call: call a function where a rule's outcome turns on the term.
The exact names are in section 4A; arguments are positional in the order shown there.
Every part also has `o 1 r 3(1) a defined term has its defined meaning` available (the opening words "unless the context otherwise requires"), which a part does not thread (section 7, item 9), and `o 1 r 2 these Rules apply to the proceedings`, which belongs to the merged top-level and is not for a part to call.

- **roc1**: `o 1 r 3(1) proceedings commenced by a document are an action` (54); `o 1 r 3(1) a court is the appellate Court` (10); `o 1 r 3(1) a court is the Appellate Division` (3); `o 1 r 3(1) a person attends` (4); `o 1 r 3(1) a meeting is a case conference` (12); `o 1 r 3(1) an instrument is a Civil Procedure Convention` (6); `o 1 r 3(1) a person is a claimant` (38); `o 1 r 3(1) a statement is a counterclaim` (16); `o 1 r 3(1) a decision-maker sitting in a court is the Court` (175); `o 1 r 3(1) a document is a defence` (34); `o 1 r 3(1) a person is a defendant` (73); `o 1 r 3(1) a person is an entity` (9); `o 1 r 3(1) a court is the General Division` (3); `o 1 r 3(1) an objective is one of the Ideals` (9); `o 1 r 3(1) a person sitting in a court is a Judge` (3); `o 1 r 3(1) a court is the lower Court` (6); `o 1 r 3(1) a report is a medical report` (2); `o 1 r 3(1) a day is a non-court day` (4); `o 1 r 3(1) a person is a non-party` (1); `o 1 r 3(1) a person is an officer` (10); `o 1 r 3(1) a document is an originating application` (46); `o 1 r 3(1) a document is an originating claim` (48); `o 1 r 3(1) a document is an originating process` (28); `o 1 r 3(1) a document is a pleading` (10); `o 1 r 3(1) directions are practice directions` (4); `o 1 r 3(1) a person is the Registrar` (16); `o 1 r 3(1) a reference to the Registry is to the Registry of the Registrar of the case` (3); `o 1 r 3(1) signing or sealing is signing or sealing` (8); `o 1 r 3(1) a person is a solicitor` (49); `o 1 r 3(1) a statement is a statement of claim` (9); `o 1 r 3(1) a statement is a statement of the special damages claimed` (2); `o 1 r 3(1) an application is a summons` (10); `o 1 r 3(1) an application is a summons without notice` (3); `o 1 r 3(1) a party is a third party` (2); `o 1 r 3(2) a reference to a numbered Form is to this form` (24).
- **roc2**: `o 1 r 3(1) proceedings commenced by a document are an action` (171); `o 1 r 3(1) a person attends` (12); `o 1 r 3(1) a meeting is a case conference` (30); `o 1 r 3(1) a person is a claimant` (97); `o 1 r 3(1) a statement is a counterclaim` (30); `o 1 r 3(1) a decision-maker sitting in a court is the Court` (275); `o 1 r 3(1) a document is a defence` (30); `o 1 r 3(1) a person is a defendant` (133); `o 1 r 3(1) a person is an entity` (4); `o 1 r 3(1) a court is the General Division` (1); `o 1 r 3(1) an objective is one of the Ideals` (3); `o 1 r 3(1) a person sitting in a court is a Judge` (10); `o 1 r 3(1) a person is a non-party` (12); `o 1 r 3(1) a person is an officer` (1); `o 1 r 3(1) a document is an originating application` (17); `o 1 r 3(1) a document is an originating claim` (26); `o 1 r 3(1) a document is an originating process` (9); `o 1 r 3(1) a document is a pleading` (25); `o 1 r 3(1) a person is the Registrar` (7); `o 1 r 3(1) a reference to the Registry is to the Registry of the Registrar of the case` (2); `o 1 r 3(1) a person is the Sheriff` (3); `o 1 r 3(1) a person is a solicitor` (9); `o 1 r 3(1) an application is a summons` (15); `o 1 r 3(1) an application is a summons without notice` (2); `o 1 r 3(1) a party is a third party` (69); `o 1 r 3(2) a reference to a numbered Form is to this form` (15).
- **roc3**: `o 1 r 3(1) proceedings commenced by a document are an action` (47); `o 1 r 3(1) a court is the appellate Court` (122); `o 1 r 3(1) a court is the Appellate Division` (30); `o 1 r 3(1) a person attends` (32); `o 1 r 3(1) a meeting is a case conference` (2); `o 1 r 3(1) a person is a claimant` (24); `o 1 r 3(1) a statement is a counterclaim` (14); `o 1 r 3(1) a decision-maker sitting in a court is the Court` (342); `o 1 r 3(1) a document is a defence` (13); `o 1 r 3(1) a person is a defendant` (40); `o 1 r 3(1) a person is an entity` (1); `o 1 r 3(1) a court is the General Division` (24); `o 1 r 3(1) a person sitting in a court is a Judge` (75); `o 1 r 3(1) a court is the lower Court` (42); `o 1 r 3(1) a person is a non-party` (5); `o 1 r 3(1) a person is an officer` (1); `o 1 r 3(1) a document is an originating application` (12); `o 1 r 3(1) a document is an originating claim` (14); `o 1 r 3(1) a document is a pleading` (2); `o 1 r 3(1) directions are practice directions` (10); `o 1 r 3(1) a person is the Registrar` (93); `o 1 r 3(1) a reference to the Registry is to the Registry of the Registrar of the case` (20); `o 1 r 3(1) signing or sealing is signing or sealing` (1); `o 1 r 3(1) a person is a solicitor` (28); `o 1 r 3(1) an application is a summons` (13); `o 1 r 3(2) a reference to a numbered Form is to this form` (24).
- **roc4**: `o 1 r 3(1) proceedings commenced by a document are an action` (5); `o 1 r 3(1) a court is the appellate Court` (115); `o 1 r 3(1) a court is the Appellate Division` (36); `o 1 r 3(1) a person attends` (4); `o 1 r 3(1) a meeting is a case conference` (2); `o 1 r 3(1) a decision-maker sitting in a court is the Court` (261); `o 1 r 3(1) a court is the General Division` (50); `o 1 r 3(1) a person sitting in a court is a Judge` (14); `o 1 r 3(1) a court is the lower Court` (63); `o 1 r 3(1) a person is a non-party` (5); `o 1 r 3(1) a document is an originating application` (6); `o 1 r 3(1) a document is an originating claim` (3); `o 1 r 3(1) a document is a pleading` (2); `o 1 r 3(1) directions are practice directions` (2); `o 1 r 3(1) a person is the Registrar` (20); `o 1 r 3(1) a reference to the Registry is to the Registry of the Registrar of the case` (9); `o 1 r 3(1) a person is a solicitor` (23); `o 1 r 3(1) an application is a summons` (5); `o 1 r 3(2) a reference to a numbered Form is to this form` (12).
- **roc5**: `o 1 r 3(1) proceedings commenced by a document are an action` (27); `o 1 r 3(1) a court is the Appellate Division` (3); `o 1 r 3(1) a person attends` (10); `o 1 r 3(1) a meeting is a case conference` (2); `o 1 r 3(1) a person is a claimant` (35); `o 1 r 3(1) a statement is a counterclaim` (4); `o 1 r 3(1) a decision-maker sitting in a court is the Court` (137); `o 1 r 3(1) a payment is within court fees` (2); `o 1 r 3(1) a document is a defence` (6); `o 1 r 3(1) a person is a defendant` (30); `o 1 r 3(1) a person is an entity` (6); `o 1 r 3(1) a court is the General Division` (7); `o 1 r 3(1) a person sitting in a court is a Judge` (11); `o 1 r 3(1) a person is a non-party` (22); `o 1 r 3(1) a person is an officer` (4); `o 1 r 3(1) a document is an originating application` (3); `o 1 r 3(1) a document is an originating claim` (5); `o 1 r 3(1) a document is a pleading` (1); `o 1 r 3(1) directions are practice directions` (4); `o 1 r 3(1) a person is the Registrar` (49); `o 1 r 3(1) a person is the Sheriff` (58); `o 1 r 3(1) signing or sealing is signing or sealing` (2); `o 1 r 3(1) a person is a solicitor` (44); `o 1 r 3(1) an application is a summons` (12); `o 1 r 3(1) an application is a summons without notice` (1); `o 1 r 3(2) a reference to a numbered Form is to this form` (4).
- **roc6**: `o 1 r 3(1) proceedings commenced by a document are an action` (17); `o 1 r 3(1) a court is the Appellate Division` (1); `o 1 r 3(1) a person attends` (3); `o 1 r 3(1) a person is a bailiff` (1); `o 1 r 3(1) an instrument is a Civil Procedure Convention` (1); `o 1 r 3(1) a person is a claimant` (2); `o 1 r 3(1) a statement is a counterclaim` (1); `o 1 r 3(1) a decision-maker sitting in a court is the Court` (178); `o 1 r 3(1) a payment is within court fees` (12); `o 1 r 3(1) a document is a defence` (2); `o 1 r 3(1) a person is a defendant` (24); `o 1 r 3(1) a person is an entity` (8); `o 1 r 3(1) a court is the General Division` (15); `o 1 r 3(1) a person sitting in a court is a Judge` (18); `o 1 r 3(1) a day is a non-court day` (1); `o 1 r 3(1) a person is a non-party` (1); `o 1 r 3(1) a person is an officer` (8); `o 1 r 3(1) a document is an originating application` (16); `o 1 r 3(1) a document is an originating process` (3); `o 1 r 3(1) directions are practice directions` (2); `o 1 r 3(1) a person is the Registrar` (37); `o 1 r 3(1) a reference to the Registry is to the Registry of the Registrar of the case` (18); `o 1 r 3(1) a person is the Sheriff` (28); `o 1 r 3(1) signing or sealing is signing or sealing` (1); `o 1 r 3(1) a person is a solicitor` (10); `o 1 r 3(1) an application is a summons` (26); `o 1 r 3(1) an application is a summons without notice` (2); `o 1 r 3(1) a day is a working day` (4); `o 1 r 3(2) a reference to a numbered Form is to this form` (10).
- **roc7**: `o 1 r 3(1) proceedings commenced by a document are an action` (177); `o 1 r 3(1) a court is the Appellate Division` (2); `o 1 r 3(1) a person attends` (4); `o 1 r 3(1) a person is a claimant` (94); `o 1 r 3(1) a statement is a counterclaim` (17); `o 1 r 3(1) a decision-maker sitting in a court is the Court` (197); `o 1 r 3(1) a document is a defence` (14); `o 1 r 3(1) a person is a defendant` (86); `o 1 r 3(1) a person is an entity` (21); `o 1 r 3(1) a court is the General Division` (15); `o 1 r 3(1) a person sitting in a court is a Judge` (22); `o 1 r 3(1) a person is an officer` (8); `o 1 r 3(1) a document is an originating application` (10); `o 1 r 3(1) a document is an originating claim` (93); `o 1 r 3(1) a document is an originating process` (2); `o 1 r 3(1) a document is a pleading` (3); `o 1 r 3(1) directions are practice directions` (13); `o 1 r 3(1) a person is the Registrar` (138); `o 1 r 3(1) a reference to the Registry is to the Registry of the Registrar of the case` (22); `o 1 r 3(1) a person is the Sheriff` (54); `o 1 r 3(1) signing or sealing is signing or sealing` (3); `o 1 r 3(1) a person is a solicitor` (49); `o 1 r 3(1) a statement is a statement of claim` (8); `o 1 r 3(1) an application is a summons` (54); `o 1 r 3(1) an application is a summons without notice` (2); `o 1 r 3(1) a day is a working day` (3); `o 1 r 3(2) a reference to a numbered Form is to this form` (17).
- **roc8**: `o 1 r 3(1) proceedings commenced by a document are an action` (5); `o 1 r 3(1) a person attends` (3); `o 1 r 3(1) a meeting is a case conference` (1); `o 1 r 3(1) a person is a claimant` (4); `o 1 r 3(1) a decision-maker sitting in a court is the Court` (89); `o 1 r 3(1) a person is a defendant` (8); `o 1 r 3(1) a court is the General Division` (6); `o 1 r 3(1) a person sitting in a court is a Judge` (7); `o 1 r 3(1) a person is an officer` (3); `o 1 r 3(1) a document is an originating application` (40); `o 1 r 3(1) a document is an originating claim` (1); `o 1 r 3(1) a document is an originating process` (2); `o 1 r 3(1) a person is the Registrar` (6); `o 1 r 3(1) a reference to the Registry is to the Registry of the Registrar of the case` (5); `o 1 r 3(1) a person is a solicitor` (6); `o 1 r 3(1) an application is a summons` (6); `o 1 r 3(1) an application is a summons without notice` (2); `o 1 r 3(2) a reference to a numbered Form is to this form` (5).
- **roc9**: `o 1 r 3(1) proceedings commenced by a document are an action` (49); `o 1 r 3(1) a person attends` (2); `o 1 r 3(1) a person is a claimant` (43); `o 1 r 3(1) a statement is a counterclaim` (7); `o 1 r 3(1) a decision-maker sitting in a court is the Court` (118); `o 1 r 3(1) a document is a defence` (6); `o 1 r 3(1) a person is a defendant` (77); `o 1 r 3(1) a person sitting in a court is a Judge` (14); `o 1 r 3(1) a person is an officer` (17); `o 1 r 3(1) a document is an originating application` (10); `o 1 r 3(1) a document is an originating claim` (6); `o 1 r 3(1) a document is a pleading` (4); `o 1 r 3(1) a person is the Registrar` (8); `o 1 r 3(1) a reference to the Registry is to the Registry of the Registrar of the case` (11); `o 1 r 3(1) a person is the Sheriff` (21); `o 1 r 3(1) signing or sealing is signing or sealing` (5); `o 1 r 3(1) a person is a solicitor` (8); `o 1 r 3(1) a statement is a statement of claim` (2); `o 1 r 3(1) an application is a summons` (28); `o 1 r 3(1) an application is a summons without notice` (3); `o 1 r 3(1) a party is a third party` (7); `o 1 r 3(2) a reference to a numbered Form is to this form` (20).
- **roc10**: `o 1 r 3(1) proceedings commenced by a document are an action` (79); `o 1 r 3(1) a person attends` (3); `o 1 r 3(1) a meeting is a case conference` (6); `o 1 r 3(1) an instrument is a Civil Procedure Convention` (2); `o 1 r 3(1) a person is a claimant` (32); `o 1 r 3(1) a decision-maker sitting in a court is the Court` (108); `o 1 r 3(1) a document is a defence` (4); `o 1 r 3(1) a person is a defendant` (69); `o 1 r 3(1) a court is the General Division` (12); `o 1 r 3(1) a person sitting in a court is a Judge` (10); `o 1 r 3(1) a person is an officer` (9); `o 1 r 3(1) a document is an originating application` (53); `o 1 r 3(1) a document is an originating claim` (26); `o 1 r 3(1) a document is an originating process` (1); `o 1 r 3(1) a document is a pleading` (10); `o 1 r 3(1) a person is the Registrar` (16); `o 1 r 3(1) signing or sealing is signing or sealing` (5); `o 1 r 3(1) a person is a solicitor` (4); `o 1 r 3(1) a statement is a statement of claim` (2); `o 1 r 3(1) an application is a summons` (25); `o 1 r 3(1) a party is a third party` (1); `o 1 r 3(2) a reference to a numbered Form is to this form` (7).
- **roc11**: `o 1 r 3(1) proceedings commenced by a document are an action` (36); `o 1 r 3(1) a person attends` (1); `o 1 r 3(1) a person is a claimant` (38); `o 1 r 3(1) a statement is a counterclaim` (4); `o 1 r 3(1) a decision-maker sitting in a court is the Court` (111); `o 1 r 3(1) a document is a defence` (4); `o 1 r 3(1) a person is a defendant` (92); `o 1 r 3(1) a court is the General Division` (5); `o 1 r 3(1) a person sitting in a court is a Judge` (5); `o 1 r 3(1) a person is a non-party` (1); `o 1 r 3(1) a person is an officer` (20); `o 1 r 3(1) a document is an originating application` (19); `o 1 r 3(1) a document is an originating claim` (21); `o 1 r 3(1) a document is a pleading` (7); `o 1 r 3(1) a person is the Registrar` (7); `o 1 r 3(1) a reference to the Registry is to the Registry of the Registrar of the case` (2); `o 1 r 3(1) signing or sealing is signing or sealing` (3); `o 1 r 3(1) a person is a solicitor` (20); `o 1 r 3(1) a statement is a statement of claim` (8); `o 1 r 3(1) an application is a summons` (23); `o 1 r 3(1) an application is a summons without notice` (2); `o 1 r 3(1) a party is a third party` (21); `o 1 r 3(2) a reference to a numbered Form is to this form` (8).
- **roc12**: `o 1 r 3(1) proceedings commenced by a document are an action` (18); `o 1 r 3(1) a court is the Appellate Division` (14); `o 1 r 3(1) a person attends` (12); `o 1 r 3(1) a person is a bailiff` (2); `o 1 r 3(1) a meeting is a case conference` (1); `o 1 r 3(1) an instrument is a Civil Procedure Convention` (4); `o 1 r 3(1) a person is a claimant` (13); `o 1 r 3(1) a statement is a counterclaim` (4); `o 1 r 3(1) a decision-maker sitting in a court is the Court` (131); `o 1 r 3(1) a document is a defence` (4); `o 1 r 3(1) a person is a defendant` (12); `o 1 r 3(1) a person is an entity` (4); `o 1 r 3(1) a court is the General Division` (30); `o 1 r 3(1) a person sitting in a court is a Judge` (16); `o 1 r 3(1) a court is the lower Court` (2); `o 1 r 3(1) a day is a non-court day` (1); `o 1 r 3(1) a person is an officer` (3); `o 1 r 3(1) a document is an originating application` (27); `o 1 r 3(1) a document is an originating claim` (5); `o 1 r 3(1) a document is an originating process` (4); `o 1 r 3(1) a document is a pleading` (11); `o 1 r 3(1) a person is the Registrar` (33); `o 1 r 3(1) a reference to the Registry is to the Registry of the Registrar of the case` (7); `o 1 r 3(1) a person is the Sheriff` (11); `o 1 r 3(1) signing or sealing is signing or sealing` (32); `o 1 r 3(1) a person is a solicitor` (2); `o 1 r 3(1) a statement is a statement of claim` (1); `o 1 r 3(1) an application is a summons` (23); `o 1 r 3(1) a party is a third party` (1); `o 1 r 3(2) a reference to a numbered Form is to this form` (12).

Functions that need an answer from another part's range (section 5.2) and so cost the caller a seam input: `o 1 r 3(1) a meeting is a case conference` (O 9 r 1), `o 1 r 3(1) an instrument is a Civil Procedure Convention` (Third Schedule), `o 1 r 3(1) a payment is within court fees` (O 25 r 1), `o 1 r 3(1) an objective is one of the Ideals` (O 3 r 1(2)), `o 1 r 3(1) a document is an originating application` (O 6 r 11), `o 1 r 3(1) a document is an originating claim` (O 6 r 5), `o 1 r 3(1) directions are practice directions` (O 26 r 2), and `o 1 r 3(1) a person is a solicitor` (the Legal Profession Act).
Every other function in section 4A needs only facts.

**Core names a part will mostly use** (the keel's guess from the headings; the whole list is section 4): roc1 `Litigant`, `Role in the action`, `Kind of person`, `How a party acts`, `Method of service`, `Place of service`, `Period`, `Moment`; roc2 to roc5 `Role in the action`, `Document kind`, `Kind of decision`, `Decision maker`, `Period`, `Moment`, `Filing event`; roc6 `Court system`, `Court level`; roc7 `Moment`, `Filing event`, `Service event`, `Method of service`; roc8 to roc11 `Litigant`, `Court level`, `Period`, `Moment`; roc12 `Court system`, `Court level`, `Method of service`, `Period`.

## 7. Difficulties the parts will meet

1. **The no-break space** (section 0, item 3).
2. **Tables lose their layout.**
   The Fourth Schedule has five Parts (lines 7788, 8452, 8561, 8715, 8765): Part 1 document fees, Part 2 hearing fees (in Tables, each with its own column headings from line 8466), Part 3 service provision fees, Part 4 search fees, Part 5 admiralty matters.
   Part 1's column headings are lines 7791-7797: Supreme Court (With value up to $1 million, With value of more than $1 million), State Courts (District Court, Magistrate's Court), Document to be stamped and remarks.
   Parts 1, 3 and 4 have those four fee columns; Part 5 has the two Supreme Court columns only (lines 8768-8771); Part 2's Tables differ.
   Each item is flattened into consecutive lines: the number, the description (sometimes with `( a )`, `( b )` sub-items), one line per fee column, then the remark.
   Read each item's amounts in column order and check the count of amounts against the columns of its Part: an item with fewer amounts than columns means fewer columns apply to it, and you must not guess which.
   The keel encoded O 1 r 2(11) (lines 62-84) from the same kind of flattened table, and tested it.
   Generate the L4 table from a script that reads the text file, and print the ruler of column names once.
3. **Headings only.** The Second Schedule has a title, a cross-reference and no table (lines 7761-7763): in the coverage table it is `repealed or blank in this text`, and the keel's O 1 r 2(13) gets `NOTHING` for it.
4. **Hard-wrapped lists.** Sub-paragraph markers `( a )`, `(i)`, `(A)`, `(CA)` sit on their own line and the item text on the next; one `N. -(1)` line often holds several paragraphs run together.
   Use `srcrefs.py quote` to cut the lines and cite line ranges; do not rely on a paragraph being one line.
5. **Amendment markers** like `[S 780/2023 wef 01/12/2023]` follow the amended provision.
   The keel counted them: 116 lines carry `wef`, and the latest date is 1 April 2026, so every provision in this text is in force on 5 November 2026: **there is no future-dated provision and no earlier version in the file.**
   Encode the current text; do not encode a marker as a rule.
6. **"Applies with changes" and "does not apply"** (S-L1 and S-L2, section 5).
   Do not encode the general Order's text again.
7. **Defined terms that differ by Order** (section 1).
8. **Schedules of Acts.** "the First Schedule to the Act" in O 49 (lines 6362 to 6389), "paragraph 7(1) of the Third Schedule" in O 53 (O 53 r 1: "the Third Schedule to the Act") and "paragraph 4(1) of the Fourth Schedule to ... the Supreme Court of Judicature Act" in O 46A r 1(5) mean the Schedule of the Act, not these Rules' Schedules.
   They are borrowed facts: ask them as inputs.
9. **Rule 3(1)'s "unless the context otherwise requires"** applies to every defined term of O 1 r 3; the keel took it as one input (`o 1 r 3(1) a defined term has its defined meaning`), and a part does not thread it.
10. **A stated period answers `JUST FALSE` outside it** (section 2, ruled 2026-11-05, ruling (a)): it is listed in your `NOTES.md` under `## Marginal readings for a lawyer`, reading (a).
11. **Time, versions and `unstable`.**
    The keel looked for a shape that the unstable dialect would express better (rule versions, rules in force on different days, deadlines counted from events) and found none in its own range: the only date logic in Order 1 is a comparison with 1 April 2022, and every `wef` marker in the whole text is on or before 1 April 2026.
    A part with deadlines counted from events has S-T1, S-F1 and S-S1 to keep that logic out of its module; a part that finds a real need for the unstable dialect says so in its own `NOTES.md` under `## Unstable dialect`, and may write the second encoding after its main one is complete and checked.

## 8. What the keel left to the parts

- Every definition in a part's own range.
  The rules whose heading contains "definition" or "interpretation", by script (a floor, not a ceiling; 45 of them): O 15 r 17, O 17 r 1, O 19 r 3, O 20 r 2, O 21 r 1, O 22 r 1, O 23 r 1, O 24 r 2, O 24A r 1, O 25 r 1, O 27 r 1, O 28 r 1, O 28 r 17, O 29 r 1, O 29A r 1, O 30 r 1, O 32 r 1, O 33 r 1, O 34 r 1, O 36 r 1, O 37 r 1, O 38 r 1, O 40 r 1, O 42 r 1, O 44 r 1, O 45 r 1, O 47 r 1, O 48 r 1, O 49 r 1, O 50 r 1, O 51 r 1, O 52 r 1, O 53 r 1, O 54 r 1, O 57 r 1, O 59 r 1, O 60 r 1, O 61 r 1, O 62 r 1, O 63 r 1, O 64 r 1, O 67 r 1, O 68 r 1, O 69 r 1, O 70 r 1.
  Each part encodes the definitions in its range in the same shape as `roc-definitions.l4`: a function over a small typed representation, `MAYBE BOOLEAN`, one test for each side of each limb.
- Rules of reading in a part's range: O 3 r 3 "Calculation of time" is roc1's; O 28 r 17 "Interpretation, etc." is roc7's; O 36 r 1 "Interpretation and mode of application" is roc8's.
- The Table of Derivations is the keel's and is not encoded: `NOTES.md` has its one `inert` row (reason 1, not operative): "It is not part of the Rules."

## Appendix: every cross-Order citation, by part

The citations are mechanical; the input names and types are the part's choice (section 5).
"You ask" means your text cites a section in another part's range; "You are asked" means another part's text cites yours.
`whole` means the Order is cited without a rule number.

### keel

You ask (the answer is in another part's range):

- O 1 l 33,45,46,48 -> O 18 r 29 [roc3]
- O 1 l 33,45,46,48 -> O 19 r 26 [roc4]
- O 1 l 50,110 -> O 3 r 8, r 1 [roc1]
- O 1 l 50 -> O 8 r 2 [roc1]
- O 1 ll 50..105 (6 lines) -> O 25 r 3, r 6, whole, r 1 [roc6]
- O 1 l 50 -> O 29A whole [roc7]
- O 1 l 50 -> O 55 whole [roc10]
- O 1 l 50 -> O 64 r 4 [roc12]
- O 1 l 71,75,79,83 -> O 28 whole [roc7]
- O 1 l 75 -> O 50 r 3 [roc10]
- O 1 l 93 -> O 9 r 1 [roc2]
- O 1 l 117,118 -> O 6 r 11, r 5 [roc1]
- O 1 l 121 -> O 26 r 2 [roc6]

You are asked (another part's text cites your sections):

- O 31 [roc7] l 4525 -> your O 1 r 2
- O 54 [roc10] l 6691 -> your O 1 r 2
- First Schedule [roc12] l 7748,7759 -> your O 1 r 2

### roc1

You ask (the answer is in another part's range):

- O 2 l 250 -> O 18 whole [roc3]
- O 4 l 419 -> O 18 whole [roc3]
- O 4 l 464 -> O 24A whole, r 4 [roc6]
- O 7 l 630 -> O 59 r 3 [roc11]
- O 7 l 635 -> O 28 whole [roc7]

You are asked (another part's text cites your sections):

- O 1 [keel] l 50,110 -> your O 3 r 8, r 1
- O 1 [keel] l 50 -> your O 8 r 2
- O 1 [keel] l 117,118 -> your O 6 r 11, r 5
- O 10 [roc2] l 1046,1050 -> your O 6 r 4
- O 10 [roc2] l 1046,1050 -> your O 7 r 4
- O 10 [roc2] l 1046,1050 -> your O 8 whole
- O 21 [roc5] l 2952 -> your O 5 whole
- O 22 [roc5] l 3474 -> your O 7 r 2
- O 28 [roc7] l 4289 -> your O 3 r 6
- O 28 [roc7] l 4371 -> your O 7 r 8
- O 33 [roc7] ll 4585..4871 (6 lines) -> your O 6 r 5, r 6, r 7, r 9
- O 33 [roc7] l 4609 -> your O 8 whole
- O 34 [roc8] l 5183,5206 -> your O 8 r 2
- O 37 [roc8] l 5376 -> your O 8 r 2
- O 39 [roc9] l 5552 -> your O 8 r 2
- O 43 [roc9] l 5954 -> your O 6 r 5
- O 44 [roc9] l 5976,6027 -> your O 4 r 1, r 5
- O 44 [roc9] l 6038 -> your O 6 r 1
- O 48 [roc10] l 6268,6289 -> your O 8 r 2
- O 49 [roc10] l 6342 -> your O 6 r 11
- O 52 [roc10] l 6516 -> your O 6 r 6
- O 53 [roc10] l 6565 -> your O 8 r 2
- O 56 [roc10] l 6767 -> your O 8 whole
- O 57 [roc11] l 6848 -> your O 8 r 2
- O 59 [roc11] l 6912,6924 -> your O 6 r 5, r 8
- O 59 [roc11] l 6918,6922 -> your O 7 whole, r 3, r 8
- O 59 [roc11] l 6918 -> your O 8 whole
- O 60 [roc11] l 7003 -> your O 8 r 2
- O 61 [roc11] l 7086,7108,7130 -> your O 6 r 11
- O 62 [roc11] ll 7171..7210 (5 lines) -> your O 6 r 2, r 6, r 5, r 7
- O 62 [roc11] l 7203,7210 -> your O 3 r 2
- O 62 [roc11] l 7291 -> your O 5 whole
- O 63 [roc11] l 7313,7367 -> your O 6 r 11
- O 64 [roc12] l 7426,7476,7478 -> your O 8 r 4A
- O 66 [roc12] l 7558 -> your O 6 r 11

### roc2

You ask (the answer is in another part's range):

- O 10 l 1046,1050 -> O 6 r 4 [roc1]
- O 10 l 1046,1050 -> O 7 r 4 [roc1]
- O 10 l 1046,1050 -> O 8 whole [roc1]
- O 13 l 1263,1285 -> O 22 whole [roc5]
- O 14 l 1371 -> O 44 r 11 [roc9]

You are asked (another part's text cites your sections):

- O 1 [keel] l 93 -> your O 9 r 1
- O 15 [roc3] l 1538 -> your O 9 r 25
- O 21 [roc5] ll 3144..3242 (5 lines) -> your O 9 r 17
- O 27 [roc6] l 4135,4166 -> your O 9 r 17
- O 27 [roc6] l 4135,4166 -> your O 14 whole
- O 33 [roc7] ll 4838..5018 (10 lines) -> your O 9 r 7, r 8, r 9, r 25, r 24
- O 33 [roc7] l 4905 -> your O 14 whole
- O 33 [roc7] l 4912,4930 -> your O 13 r 8, r 2
- O 33 [roc7] l 5050 -> your O 11 r 2
- O 38 [roc8] l 5415 -> your O 9 whole
- O 40 [roc9] l 5691,5774 -> your O 13 r 9
- O 43 [roc9] l 5954 -> your O 9 r 13
- O 43 [roc9] l 5957,5961 -> your O 14 r 3, whole, r 7
- O 44 [roc9] l 6013 -> your O 10 whole
- O 44 [roc9] l 6034,6061 -> your O 11 whole, r 7
- O 44 [roc9] l 6058 -> your O 14 r 1
- O 46A [roc10] l 6148,6159 -> your O 9 r 8, r 9
- O 47 [roc10] l 6187 -> your O 11 whole
- O 48 [roc10] l 6296 -> your O 9 r 24
- O 49 [roc10] l 6342,6423 -> your O 9 whole
- O 50 [roc10] l 6436,6440 -> your O 9 whole
- O 51 [roc10] l 6477 -> your O 9 r 17
- O 53 [roc10] l 6647 -> your O 13 r 9
- O 55 [roc10] l 6716 -> your O 9 r 24
- O 59 [roc11] l 6931,6933,6934 -> your O 9 r 17
- O 59 [roc11] l 6949,6952 -> your O 10 r 5, whole, r 9
- O 59 [roc11] l 6958,6964 -> your O 13 r 9
- O 61 [roc11] l 7086,7108,7130 -> your O 9 whole
- O 62 [roc11] l 7188,7212,7289 -> your O 9 r 9, r 10, whole
- O 62 [roc11] l 7212,7214 -> your O 10 whole, r 9
- O 62 [roc11] ll 7216..7267 (5 lines) -> your O 11 whole
- O 62 [roc11] l 7291 -> your O 14 whole
- O 63 [roc11] l 7313,7367 -> your O 9 whole
- O 65 [roc12] l 7495,7503 -> your O 11 r 2, whole
- O 65 [roc12] l 7503 -> your O 9 whole, r 17
- O 66 [roc12] l 7560 -> your O 9 r 10
- O 67 [roc12] l 7626 -> your O 13 r 9
- O 68 [roc12] l 7675 -> your O 9 whole
- Fourth Schedule [roc12] l 7965,7984 -> your O 9 r 25
- Fourth Schedule [roc12] l 8013 -> your O 13 r 4

### roc3

You ask (the answer is in another part's range):

- O 15 l 1538 -> O 9 r 25 [roc2]
- O 18 ll 1711..2082 (6 lines) -> O 19 whole [roc4]

You are asked (another part's text cites your sections):

- O 1 [keel] l 33,45,46,48 -> your O 18 r 29
- O 2 [roc1] l 250 -> your O 18 whole
- O 4 [roc1] l 419 -> your O 18 whole
- O 19 [roc4] l 2578,2579,2584 -> your O 18 whole
- O 33 [roc7] l 4592,4922 -> your O 16 r 2
- O 33 [roc7] l 4930,4944,4954,5030 -> your O 15 r 10, r 4, r 1, r 11
- O 34 [roc8] l 5187 -> your O 15 r 4
- O 43 [roc9] l 5968 -> your O 15 r 15
- O 46A [roc10] l 6167 -> your O 15 r 3
- O 48 [roc10] l 6294 -> your O 15 r 4
- O 49 [roc10] l 6342 -> your O 15 r 7
- O 61 [roc11] l 7086,7108,7130,7149 -> your O 15 r 7, whole
- O 63 [roc11] l 7313,7367,7397 -> your O 15 r 7, whole
- O 65 [roc12] l 7508,7521 -> your O 15 whole
- Fourth Schedule [roc12] ll 8062..8222 (7 lines) -> your O 18 whole, r 16, r 21, r 25, r 29, r 33, r 37

### roc4

You ask (the answer is in another part's range):

- O 19 l 2578,2579,2584 -> O 18 whole [roc3]
- O 19 l 2870 -> O 20 whole [roc5]

You are asked (another part's text cites your sections):

- O 1 [keel] l 33,45,46,48 -> your O 19 r 26
- O 18 [roc3] ll 1711..2082 (6 lines) -> your O 19 whole
- O 20 [roc5] l 2880,2904 -> your O 19 r 41, r 7
- O 30 [roc7] l 4500,4502,4511 -> your O 19 whole
- O 34 [roc8] l 5134,5171 -> your O 19 r 10
- Fourth Schedule [roc12] ll 8113..8271 (10 lines) -> your O 19 whole, r 19, r 41, r 26, r 37, r 32

### roc5

You ask (the answer is in another part's range):

- O 20 l 2880,2904 -> O 19 r 41, r 7 [roc4]
- O 21 l 2952 -> O 5 whole [roc1]
- O 21 ll 3144..3242 (5 lines) -> O 9 r 17 [roc2]
- O 21 l 3149 -> O 52 r 1 [roc10]
- O 21 l 3246 -> O 51 r 4 [roc10]
- O 22 l 3448 -> O 33 r 25 [roc7]
- O 22 l 3474 -> O 7 r 2 [roc1]

You are asked (another part's text cites your sections):

- O 13 [roc2] l 1263,1285 -> your O 22 whole
- O 19 [roc4] l 2870 -> your O 20 whole
- O 25 [roc6] l 4038 -> your O 21 whole
- O 33 [roc7] l 4900 -> your O 21 whole
- O 42 [roc9] ll 5869..5932 (5 lines) -> your O 22 whole, r 10, r 2
- O 45 [roc9] l 6079,6085 -> your O 22 whole
- O 56 [roc10] l 6780,6781 -> your O 22 r 2, r 6
- O 59 [roc11] l 6958,6962,6967 -> your O 22 whole, r 10, r 2
- O 62 [roc11] l 7295,7301 -> your O 21 whole
- Fourth Schedule [roc12] l 8190 -> your O 20 whole, r 5
- Fourth Schedule [roc12] ll 8309..8320 (5 lines) -> your O 21 whole

### roc6

You ask (the answer is in another part's range):

- O 25 l 4038 -> O 21 whole [roc5]
- O 27 l 4135,4166 -> O 9 r 17 [roc2]
- O 27 l 4135,4166 -> O 14 whole [roc2]
- O 27 l 4135,4166,4167 -> O 33 whole [roc7]

You are asked (another part's text cites your sections):

- O 1 [keel] ll 50..105 (6 lines) -> your O 25 r 3, r 6, whole, r 1
- O 1 [keel] l 121 -> your O 26 r 2
- O 4 [roc1] l 464 -> your O 24A whole, r 4
- O 28 [roc7] l 4253 -> your O 26 r 3
- O 33 [roc7] l 4580 -> your O 27 r 15
- O 33 [roc7] l 5046 -> your O 26 r 3
- O 40 [roc9] l 5804,5810 -> your O 26 r 3
- O 47 [roc10] l 6214,6215 -> your O 26 r 3
- O 53 [roc10] l 6538 -> your O 26 r 3
- O 59 [roc11] l 6958 -> your O 23 whole
- O 67 [roc12] l 7661 -> your O 26 r 3
- Fourth Schedule [roc12] l 8007 -> your O 23 r 11

### roc7

You ask (the answer is in another part's range):

- O 28 l 4253 -> O 26 r 3 [roc6]
- O 28 l 4289 -> O 3 r 6 [roc1]
- O 28 l 4371 -> O 7 r 8 [roc1]
- O 30 l 4500,4502,4511 -> O 19 whole [roc4]
- O 31 l 4525 -> O 1 r 2 [keel]
- O 33 l 4580 -> O 27 r 15 [roc6]
- O 33 ll 4585..4871 (6 lines) -> O 6 r 5, r 6, r 7, r 9 [roc1]
- O 33 l 4592,4922 -> O 16 r 2 [roc3]
- O 33 l 4609 -> O 8 whole [roc1]
- O 33 l 4830 -> O 59 r 7 [roc11]
- O 33 ll 4838..5018 (10 lines) -> O 9 r 7, r 8, r 9, r 25, r 24 [roc2]
- O 33 l 4900 -> O 21 whole [roc5]
- O 33 l 4905 -> O 14 whole [roc2]
- O 33 l 4912,4930 -> O 13 r 8, r 2 [roc2]
- O 33 l 4930,4944,4954,5030 -> O 15 r 10, r 4, r 1, r 11 [roc3]
- O 33 l 5046 -> O 26 r 3 [roc6]
- O 33 l 5050 -> O 11 r 2 [roc2]

You are asked (another part's text cites your sections):

- O 1 [keel] l 50 -> your O 29A whole
- O 1 [keel] l 71,75,79,83 -> your O 28 whole
- O 7 [roc1] l 635 -> your O 28 whole
- O 22 [roc5] l 3448 -> your O 33 r 25
- O 27 [roc6] l 4135,4166,4167 -> your O 33 whole
- O 44 [roc9] l 6056 -> your O 33 r 36
- First Schedule [roc12] l 7760 -> your O 33 r 5
- Fourth Schedule [roc12] l 8385,8408 -> your O 28 whole
- Fourth Schedule [roc12] ll 8462..8780 (5 lines) -> your O 33 r 42, r 4, r 13

### roc8

You ask (the answer is in another part's range):

- O 34 l 5134,5171 -> O 19 r 10 [roc4]
- O 34 l 5183,5206 -> O 8 r 2 [roc1]
- O 34 l 5187 -> O 15 r 4 [roc3]
- O 37 l 5376 -> O 8 r 2 [roc1]
- O 38 l 5415 -> O 9 whole [roc2]

You are asked (another part's text cites your sections):

- Fourth Schedule [roc12] l 8201,8206,8211 -> your O 34 whole

### roc9

You ask (the answer is in another part's range):

- O 39 l 5552 -> O 8 r 2 [roc1]
- O 40 l 5691,5774 -> O 13 r 9 [roc2]
- O 40 l 5797 -> O 59 r 3 [roc11]
- O 40 l 5804,5810 -> O 26 r 3 [roc6]
- O 42 ll 5869..5932 (5 lines) -> O 22 whole, r 10, r 2 [roc5]
- O 42 l 5891 -> O 56 whole [roc10]
- O 43 l 5954 -> O 6 r 5 [roc1]
- O 43 l 5954 -> O 9 r 13 [roc2]
- O 43 l 5957,5961 -> O 14 r 3, whole, r 7 [roc2]
- O 43 l 5968 -> O 15 r 15 [roc3]
- O 44 l 5976,6027 -> O 4 r 1, r 5 [roc1]
- O 44 l 6013 -> O 10 whole [roc2]
- O 44 l 6034,6061 -> O 11 whole, r 7 [roc2]
- O 44 l 6038 -> O 6 r 1 [roc1]
- O 44 l 6056 -> O 33 r 36 [roc7]
- O 44 l 6058 -> O 14 r 1 [roc2]
- O 45 l 6079,6085 -> O 22 whole [roc5]

You are asked (another part's text cites your sections):

- O 14 [roc2] l 1371 -> your O 44 r 11
- Fourth Schedule [roc12] l 8007 -> your O 45 r 3
- Fourth Schedule [roc12] l 8007 -> your O 42 r 3

### roc10

You ask (the answer is in another part's range):

- O 46A l 6148,6159 -> O 9 r 8, r 9 [roc2]
- O 46A l 6167 -> O 15 r 3 [roc3]
- O 47 l 6187 -> O 11 whole [roc2]
- O 47 l 6214,6215 -> O 26 r 3 [roc6]
- O 48 l 6268,6289 -> O 8 r 2 [roc1]
- O 48 l 6294 -> O 15 r 4 [roc3]
- O 48 l 6296 -> O 9 r 24 [roc2]
- O 49 l 6342 -> O 6 r 11 [roc1]
- O 49 l 6342,6423 -> O 9 whole [roc2]
- O 49 l 6342 -> O 15 r 7 [roc3]
- O 50 l 6436,6440 -> O 9 whole [roc2]
- O 51 l 6477 -> O 9 r 17 [roc2]
- O 52 l 6516 -> O 6 r 6 [roc1]
- O 53 l 6538 -> O 26 r 3 [roc6]
- O 53 l 6565 -> O 8 r 2 [roc1]
- O 53 l 6647 -> O 13 r 9 [roc2]
- O 54 l 6691 -> O 1 r 2 [keel]
- O 55 l 6716 -> O 9 r 24 [roc2]
- O 56 l 6767 -> O 8 whole [roc1]
- O 56 l 6780,6781 -> O 22 r 2, r 6 [roc5]

You are asked (another part's text cites your sections):

- O 1 [keel] l 50 -> your O 55 whole
- O 1 [keel] l 75 -> your O 50 r 3
- O 21 [roc5] l 3149 -> your O 52 r 1
- O 21 [roc5] l 3246 -> your O 51 r 4
- O 42 [roc9] l 5891 -> your O 56 whole
- Fourth Schedule [roc12] l 8338,8341,8345 -> your O 46A r 1, r 3

### roc11

You ask (the answer is in another part's range):

- O 57 l 6848 -> O 8 r 2 [roc1]
- O 59 l 6912,6924 -> O 6 r 5, r 8 [roc1]
- O 59 l 6918,6922 -> O 7 whole, r 3, r 8 [roc1]
- O 59 l 6918 -> O 8 whole [roc1]
- O 59 l 6931,6933,6934 -> O 9 r 17 [roc2]
- O 59 l 6949,6952 -> O 10 r 5, whole, r 9 [roc2]
- O 59 l 6958,6962,6967 -> O 22 whole, r 10, r 2 [roc5]
- O 59 l 6958 -> O 23 whole [roc6]
- O 59 l 6958,6964 -> O 13 r 9 [roc2]
- O 60 l 7003 -> O 8 r 2 [roc1]
- O 61 l 7086,7108,7130 -> O 6 r 11 [roc1]
- O 61 l 7086,7108,7130 -> O 9 whole [roc2]
- O 61 l 7086,7108,7130,7149 -> O 15 r 7, whole [roc3]
- O 62 ll 7171..7210 (5 lines) -> O 6 r 2, r 6, r 5, r 7 [roc1]
- O 62 l 7188,7212,7289 -> O 9 r 9, r 10, whole [roc2]
- O 62 l 7203,7210 -> O 3 r 2 [roc1]
- O 62 l 7212,7214 -> O 10 whole, r 9 [roc2]
- O 62 ll 7216..7267 (5 lines) -> O 11 whole [roc2]
- O 62 l 7291 -> O 5 whole [roc1]
- O 62 l 7291 -> O 14 whole [roc2]
- O 62 l 7295,7301 -> O 21 whole [roc5]
- O 63 l 7313,7367 -> O 6 r 11 [roc1]
- O 63 l 7313,7367 -> O 9 whole [roc2]
- O 63 l 7313,7367,7397 -> O 15 r 7, whole [roc3]

You are asked (another part's text cites your sections):

- O 7 [roc1] l 630 -> your O 59 r 3
- O 33 [roc7] l 4830 -> your O 59 r 7
- O 40 [roc9] l 5797 -> your O 59 r 3

### roc12

You ask (the answer is in another part's range):

- O 64 l 7426,7476,7478 -> O 8 r 4A [roc1]
- O 65 l 7495,7503 -> O 11 r 2, whole [roc2]
- O 65 l 7503 -> O 9 whole, r 17 [roc2]
- O 65 l 7508,7521 -> O 15 whole [roc3]
- O 66 l 7558 -> O 6 r 11 [roc1]
- O 66 l 7560 -> O 9 r 10 [roc2]
- O 67 l 7626 -> O 13 r 9 [roc2]
- O 67 l 7661 -> O 26 r 3 [roc6]
- O 68 l 7675 -> O 9 whole [roc2]
- First Schedule l 7748,7759 -> O 1 r 2 [keel]
- First Schedule l 7760 -> O 33 r 5 [roc7]
- Fourth Schedule l 7965,7984 -> O 9 r 25 [roc2]
- Fourth Schedule l 8007 -> O 45 r 3 [roc9]
- Fourth Schedule l 8007 -> O 23 r 11 [roc6]
- Fourth Schedule l 8007 -> O 42 r 3 [roc9]
- Fourth Schedule l 8013 -> O 13 r 4 [roc2]
- Fourth Schedule ll 8062..8222 (7 lines) -> O 18 whole, r 16, r 21, r 25, r 29, r 33, r 37 [roc3]
- Fourth Schedule ll 8113..8271 (10 lines) -> O 19 whole, r 19, r 41, r 26, r 37, r 32 [roc4]
- Fourth Schedule l 8190 -> O 20 whole, r 5 [roc5]
- Fourth Schedule l 8201,8206,8211 -> O 34 whole [roc8]
- Fourth Schedule ll 8309..8320 (5 lines) -> O 21 whole [roc5]
- Fourth Schedule l 8338,8341,8345 -> O 46A r 1, r 3 [roc10]
- Fourth Schedule l 8385,8408 -> O 28 whole [roc7]
- Fourth Schedule ll 8462..8780 (5 lines) -> O 33 r 42, r 4, r 13 [roc7]

You are asked (another part's text cites your sections):

- O 1 [keel] l 50 -> your O 64 r 4
