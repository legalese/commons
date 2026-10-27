# NOTES -- dg-core: the shared vocabulary of the Delaware General Corporation Law (8 Del. C. ch. 1)

This is the keel (agent `dg-g0`) for the encoding of the Delaware General Corporation Law, 8 Del. C. §§ 101-398, written for the stable `l4` build 1.6.98.
Eleven part agents (dg1 to dg11) each encode one contiguous piece of the text and import the module written here.
They cannot see each other, so this file is their guide: what is shared, how a name is written, which terms the text defines and who encodes each, and what the stable binary refuses.

**The source.**
The text is `de-code-t8-ch1-2026-10-01.txt`, a plain-text rendering made by a converter script from the Delaware Code Online (Delaware Division of Legislative Services; "through 85 Del. Laws, c. 550", acts enacted as of October 01, 2026; fetched 2026-10-21).
It is not the official text and is not marked up, and nothing in this folder has been verified against the official text.
Every `src:N` in this folder is a line of that file.
It has 2,111 lines: 204 sections in 18 subchapters, 202 `History:` lines (the two `[Reserved.]` sections, 246 and 392, have none), and no tables.

**The seat.**
A person who incorporates, directs or holds stock in a Delaware corporation under the General Corporation Law: an incorporator, a director or officer, a stockholder including a minority stockholder.
They ask what the Law lets them do, what it requires of them, what they may require of the corporation, and what can be done to them.
The Secretary of State, the Court of Chancery and the Attorney General get no seat: their acts are encoded only as what they mean for the person in the seat.

**What the keel has.**
No provisions of its own: the Law has no interpretation section (its definitions sit inside the sections that need them), so the keel's range is empty (lines: none, words: 0).
It writes the shared vocabulary, the naming conventions, and this table of who encodes which defined term.

**Files in this folder.**

| file | what it is |
| --- | --- |
| `dg-core.l4` | The core module. Imports `prelude` and `daydate` only. Types, constructors and 17 small rules (one dialect shim, the time-limit arithmetic, the kind predicates, the vote test). |
| `dg-core-tests-core.l4` | Its tests: expected values written by hand from the text. |
| `NOTES.md`, `PROGRESS.md` | These notes, and the progress log. |
| `check.sh`, `srcrefs.py` | The two tools the lead put here; unchanged. |

There is no `dg-core-<topic>.l4` interpretation module, because there is nothing to interpret.

**Target.**
The stable build, `1.6.98 (main, 7689b0d, 2026-10-19)`, sha256 `82ea44addf093ea4dd84c4e4416184920857ca9c762c5b31feed20541c20263e`.
The binary named in the task is itself a `main` build, so there is no second compiler to compare with: `check.sh` was run with `L4_TARGET=unstable`, as the brief says, which skips the comparison.
Everything in the core was written inside the dialect that build reads, and the probes in the writing skill that name constructs it refuses were run against it (see "What the stable binary does not accept").

## Vocabulary

Every type and every enumeration constructor in `dg-core.l4`: 10 types and 56 constructors, then the 17 rules.
The table is checked against the module by the script that wrote this file, so none is missing.
Core constructors are lowercase backticked phrases lifted from the text; a piece never redeclares or reuses them.

| name | kind | what it is | licensed by |
| --- | --- | --- | --- |
| `Time unit` | type (enumeration) | The unit a time limit is counted in. | § 213(a), § 164, § 371(b)(1), § 212(b) |
| `calendar days` | constructor of `Time unit` | A period counted in calendar days (60 days, 10 days). | § 213(a) |
| `calendar weeks` | constructor of `Time unit` | A period counted in calendar weeks (1 week); 7 days each. | § 164 |
| `calendar months` | constructor of `Time unit` | A period counted in calendar months (6 months); the date arithmetic clamps to the last day of the month. | § 371(b)(1) |
| `calendar years` | constructor of `Time unit` | A period counted in calendar years (3 years); the date arithmetic clamps 29 February to 28 February. | § 212(b) |
| `Period` | type (record) | A time limit: `how many units` (a NUMBER) of a `unit` (a Time unit). The one way a time limit is written. | § 213(a) ("not more than 60 nor less than 10 days"), § 164 ("1 week"), § 371(b)(1) ("6 months"), § 212(b) ("3 years") |
| `how many units` | field of `Period` | NUMBER: how many of the unit. | as `Period` |
| `unit` | field of `Period` | Time unit. | as `Period` |
| `Kind of corporation` | type (enumeration) | The four kinds of corporation organized under the chapter that section 114(d) tells apart: stock, and three nonstock kinds. The plain input every piece takes for "what kind of corporation is this?". The definitions that decide the kind are encoded by dg1. | § 114(d)(1) to (4) |
| `a stock corporation` | constructor of `Kind of corporation` | A corporation organized under the chapter that is authorized to issue capital stock: the complement of a nonstock corporation. | § 114(d)(4) |
| `a nonstock corporation with membership interests` | constructor of `Kind of corporation` | A nonstock corporation that has membership interests, so is not a nonprofit nonstock corporation. | § 114(d)(2), (3), (4) |
| `a nonprofit nonstock corporation that is not charitable` | constructor of `Kind of corporation` | A nonstock corporation without membership interests that is not a charitable nonstock corporation. | § 114(d)(1), (3) |
| `a charitable nonstock corporation` | constructor of `Kind of corporation` | A nonprofit nonstock corporation exempt from tax under 26 U.S.C. § 501(c)(3). | § 114(d)(1) |
| `Where an entity is formed` | type (enumeration) | Under whose law an entity was formed: this State, another jurisdiction of the United States, or a foreign jurisdiction outside the United States. | § 371(a), § 388(a)(1), § 390(a)(1) |
| `this State` | constructor of `Where an entity is formed` | Formed under the laws of Delaware. | § 371(a) |
| `another jurisdiction of the United States` | constructor of `Where an entity is formed` | Formed under the laws of another State, the District of Columbia, or a possession or territory of the United States (a jurisdiction "other than this State" that is not a "foreign jurisdiction"). | § 371(a), § 388(a)(1) |
| `a foreign jurisdiction outside the United States` | constructor of `Where an entity is formed` | Formed under the laws of a foreign country or other foreign jurisdiction (other than the United States, any state, the District of Columbia, or any possession or territory of the United States). | § 388(a)(1), § 390(a)(1) |
| `Kind of entity` | type (enumeration) | One superset of the kinds of person the text names: a natural person and the kinds of entity. Each section's own definition ("person", "other entity", "entity", "non-United States entity", "joint-stock association") is a predicate over it, encoded in that section's piece. | § 203(c)(6), § 251(h)(6)e., § 254(a), § 263(a), § 264(a), § 265(a), § 267(d)(2), § 388(a)(2) |
| `a natural person` | constructor of `Kind of entity` | A natural person ("any individual"): the first word of the definitions of "person" in § 203(c)(6), § 251(h)(6)e. and § 262(a). § 141(b) also asks that a director be a natural person. | § 203(c)(6), § 251(h)(6)e., § 262(a), § 141(b) |
| `a corporation` | constructor of `Kind of entity` | A corporation; its field `its kind` says which Kind of corporation. The one constructor of Kind of entity that carries a field. | § 203(c)(6), § 114(d) |
| `a general partnership` | constructor of `Kind of entity` | A general partnership. A section that says "partnership" ("whether general (including a limited liability partnership) or limited (including a limited liability limited partnership)", § 263(a)) covers all four partnership constructors; a section that tells them apart uses them one by one. | § 263(a), § 265(a), § 388(a)(2) |
| `a limited partnership` | constructor of `Kind of entity` | A limited partnership. | § 263(a), § 265(a), § 388(a)(2) |
| `a limited liability partnership` | constructor of `Kind of entity` | A limited liability partnership. | § 263(a), § 265(a), § 388(a)(2) |
| `a limited liability limited partnership` | constructor of `Kind of entity` | A limited liability limited partnership. | § 263(a), § 265(a), § 388(a)(2) |
| `a limited liability company` | constructor of `Kind of entity` | A limited liability company. | § 264(a), § 265(a), § 267(d)(2), § 388(a)(2) |
| `a statutory trust` | constructor of `Kind of entity` | A statutory trust. | § 265(a), § 388(a)(2) |
| `a business trust or association` | constructor of `Kind of entity` | A business trust or association. | § 265(a), § 388(a)(2) |
| `a real estate investment trust` | constructor of `Kind of entity` | A real estate investment trust. | § 265(a), § 388(a)(2) |
| `a common-law trust` | constructor of `Kind of entity` | A common-law trust. | § 265(a), § 388(a)(2) |
| `a joint-stock association` | constructor of `Kind of entity` | An association of the kind commonly known as a joint-stock association or joint-stock company, or an unincorporated association, trust or enterprise having members or outstanding shares or other evidences of financial or beneficial interest. | § 254(a), § 267(d)(2) |
| `any other unincorporated business or association` | constructor of `Kind of entity` | Any other unincorporated business, association or enterprise; the catch-all for "or other entity" and "any other unincorporated business or entity". | § 203(c)(6), § 265(a), § 388(a)(2) |
| `Entity` | type (record) | An entity: its `kind of entity` and `where formed`. `where formed` has no meaning for `a natural person`: do not build an Entity for one, pass the kind alone. | § 265(a), § 388(a)(2), § 371(a) |
| `kind of entity` | field of `Entity` | Kind of entity. | as `Entity` |
| `where formed` | field of `Entity` | Where an entity is formed. | as `Entity` |
| `Actor` | type (enumeration) | The parties that two or more pieces name, for use as the party of a rule or the performer of an action. Offices are constructors, not strings. | § 107, § 124(3), § 132(a), § 141(a), § 142(a), § 145(a), § 165, § 211(a)(2), § 212(b), § 226(a), § 231(a), § 279, § 291, § 103(a), § 114(a)(1) |
| `the corporation` | constructor of `Actor` | The corporation itself. | § 141(a), § 142(a) |
| `an incorporator` | constructor of `Actor` | A person who signs the certificate of incorporation and, until directors are elected, manages the affairs of the corporation. | § 107 |
| `a director` | constructor of `Actor` | A member of the board of directors (of the governing body, for a nonstock corporation). | § 141(a) |
| `an officer` | constructor of `Actor` | An officer of the corporation. | § 142(a) |
| `an employee` | constructor of `Actor` | An employee of the corporation. | § 145(a) |
| `a stockholder` | constructor of `Actor` | A stockholder. | § 212(b) |
| `a member of a nonstock corporation` | constructor of `Actor` | A member of a nonstock corporation (what "stockholder" is read as, § 114(a)(1)). | § 114(a)(1) |
| `a subscriber for stock` | constructor of `Actor` | A subscriber for stock (§ 165 speaks of "a subscription for stock of a corporation to be formed"). | § 165 |
| `a proxyholder` | constructor of `Actor` | A person holding a stockholder's proxy. | § 211(a)(2) |
| `the registered agent` | constructor of `Actor` | The corporation's registered agent in this State. | § 132(a) |
| `a creditor` | constructor of `Actor` | A creditor of the corporation. | § 291 |
| `a receiver` | constructor of `Actor` | A receiver appointed for the corporation. | § 291, § 279 |
| `a trustee` | constructor of `Actor` | A trustee (of a dissolved corporation, § 279; of a voting trust, § 218, is the same constructor: say which in the rule). | § 279 |
| `a custodian` | constructor of `Actor` | A custodian appointed for the corporation. | § 226(a) |
| `an inspector of election` | constructor of `Actor` | An inspector appointed to act at a meeting of stockholders. | § 231(a) |
| `the Secretary of State` | constructor of `Actor` | The Secretary of State, with whom instruments are filed. An official: no seat; what the filing means for the person. | § 103(a) |
| `the Court of Chancery` | constructor of `Actor` | The Court of Chancery. An official: no seat; its orders are conditions ("if the Court so orders"). | § 291, § 279 |
| `the Attorney General` | constructor of `Actor` | The Attorney General of the State of Delaware. An official: no seat. | § 124(3) |
| `another party named in the provision` | constructor of `Actor` | A party the core does not list. Carries the text's own words in `named as`; two spellings are two parties, so copy the words exactly from the text. | the provision using it |
| `Where a provision is made` | type (enumeration) | Where a provision that displaces the Law's default sits: the certificate of incorporation, the bylaws, a resolution of the board, or none of these (the Law's default stands). | § 141(b), § 216, § 151(a) |
| `in the certificate of incorporation` | constructor of `Where a provision is made` | The provision sits in the certificate of incorporation. | § 141(b), § 216 |
| `in the bylaws` | constructor of `Where a provision is made` | The provision sits in the bylaws. | § 141(b), § 216 |
| `in a resolution of the board of directors` | constructor of `Where a provision is made` | The provision sits in a resolution of the board of directors adopted under authority in the certificate. | § 151(a) |
| `in none of these` | constructor of `Where a provision is made` | No such provision: the Law's own default stands. | § 216 ("In the absence of such specification") |
| `Vote base` | type (enumeration) | What a vote is counted against: the thing whose size the proportion is a proportion of. | § 242(b)(1), § 216(2), § 144(a)(2), § 141(b), § 141(c)(1), § 141(c)(4), § 223(a)(1), § 241(b) |
| `the outstanding stock entitled to vote` | constructor of `Vote base` | "The outstanding stock entitled to vote thereon". For a nonstock corporation read the members entitled to vote (§ 114(a)). For a class vote, the class's outstanding stock, counted in votes (§ 212(a)). | § 242(b)(1) |
| `the shares present in person or represented by proxy and entitled to vote` | constructor of `Vote base` | The shares present at the meeting in person or by proxy and entitled to vote on the subject matter. | § 216(2) |
| `the votes cast` | constructor of `Vote base` | The votes cast (§ 144(a)(2): "by the disinterested stockholders": say so in the input's name). | § 144(a)(2) |
| `the whole board` | constructor of `Vote base` | "The whole board", which the text does not define (§ 223(c) speaks of "the whole board (as constituted immediately prior to any such increase)"). The piece supplies the count. | § 141(c)(1), § 275, § 223(c) |
| `the directors then in office` | constructor of `Vote base` | The directors in office at the time, although less than a quorum. | § 223(a)(1) |
| `the directors present at a meeting at which a quorum is present` | constructor of `Vote base` | The directors present at a board meeting that has a quorum. | § 141(b) |
| `the directors then serving on a committee` | constructor of `Vote base` | The directors then serving on a committee or subcommittee. | § 141(c)(4) |
| `the incorporators` | constructor of `Vote base` | The incorporators. | § 241(b), § 108(a) |
| `another base named in the provision` | constructor of `Vote base` | A base the core does not list. Carries the text's own words in `named as`. | the provision using it |
| `Vote requirement` | type (record) | A vote needed: `counted against` (a Vote base), `proportion` (a NUMBER, a fraction of 1) and `must be exceeded` (TRUE for "a majority", more than the proportion; FALSE for "at least", reaching it). | § 242(b)(1), § 216(2), § 203(a)(3) |
| `counted against` | field of `Vote requirement` | Vote base. | as `Vote requirement` |
| `proportion` | field of `Vote requirement` | NUMBER: a fraction of 1 (1 DIVIDED BY 2, 2 DIVIDED BY 3, 15%). | as `Vote requirement` |
| `must be exceeded` | field of `Vote requirement` | BOOLEAN: TRUE means more than the proportion ("a majority"), FALSE means at least the proportion. | as `Vote requirement` |

### Rules in the core

| rule | inputs | gives | what it does |
| --- | --- | --- | --- |
| YMD y m d | NUMBER (year), NUMBER (month), NUMBER (day) | DATE | Dialect shim for the `YMD` that the stable build lacks: `Date d m y`. Not law. Defined once, here; never redefine it. |
| `period in days` n | NUMBER | Period | n calendar days. |
| `period in weeks` n | NUMBER | Period | n calendar weeks. |
| `period in months` n | NUMBER | Period | n calendar months. |
| `period in years` n | NUMBER | Period | n calendar years. |
| `the date` p `after` d | Period, DATE | DATE | d plus p. Days and weeks add days; months and years use `add months` / `add years`, which clamp to the last day of the month. |
| `the date` p `before` d | Period, DATE | DATE | d minus p, by the same rules (31 August less 6 months is 28 February). |
| `the kind is a stock corporation` k | Kind of corporation | BOOLEAN | TRUE for `a stock corporation` only. |
| `the kind is a nonstock corporation` k | Kind of corporation | BOOLEAN | TRUE for the three nonstock kinds (§ 114(d)(4)). |
| `the kind is a nonprofit nonstock corporation` k | Kind of corporation | BOOLEAN | TRUE for the nonprofit kind and the charitable kind (§ 114(d)(3)). |
| `the kind is a charitable nonstock corporation` k | Kind of corporation | BOOLEAN | TRUE for the charitable kind only (§ 114(d)(1)). |
| `the entity was formed under the laws of this State` e | Entity | BOOLEAN | `where formed` is `this State`. |
| `the entity was formed under the laws of a jurisdiction other than this State` e | Entity | BOOLEAN | Not `this State`: the test in the definition of "foreign corporation" (§ 371(a)). |
| `the entity was formed under the laws of a foreign jurisdiction` e | Entity | BOOLEAN | `where formed` is `a foreign jurisdiction outside the United States` (§ 388(a)(1)). |
| `a majority of` b | Vote base | Vote requirement | More than 1 DIVIDED BY 2 of the base. |
| `at least` p `of` b | NUMBER, Vote base | Vote requirement | Reaching p of the base is enough ("at least 66 2/3%", "no less than 1/3"). |
| `the vote carries` r `votes in favor` `size of the base` | Vote requirement, NUMBER, NUMBER | MAYBE BOOLEAN | Whether the votes in favor meet the requirement, out of the size of the base. NOTHING (not covered) when the counts cannot be a vote: base 0 or less, votes in favor below 0 or above the base. |

## Naming conventions

These conventions exist so that eleven pieces written at the same time, and later composed, never coin the same name for different things and never write one thing two ways.
A name defined in two imported modules cannot be used at all on this binary, so the first four items are about avoiding that.

- **A rule is named with its section locator first.**
  The locator is lowercase `s`, a space, the section number, then the subsection letters and numbers in the Law's order with no spaces: `s 242(b)(1)`, `s 216`, `s 203(c)(5)`.
  After it comes one space and a plain gloss in the Law's words, all inside one pair of backticks: `` `s 242(b)(1) a proposed amendment is adopted` ``, `` `s 203(c)(5) an interested stockholder` ``.
  A rule that serves a whole section uses the bare section: `` `s 220 the right to inspect` ``.
  A helper rule keeps the locator of the provision it helps.
  Never put `--` inside a name (it is the comment marker; backticks do not protect it).
  Prefer prefix names (`` `s 213(a) the earliest record date` meeting ``).
  A mixfix name must list its parameters in the order of its `GIVEN`, and a mixfix name with exactly one argument must not end in a keyword segment.
- **A type, a constant or a record local to a piece is named with its locator or its piece id first**: `` `s 251 Agreement of merger` ``, `` `dg4 Defective corporate act` ``.
  Never redeclare a core type, and never reuse a core name (the Vocabulary table lists them all).
- **A constructor of a local enumeration is a lowercase phrase lifted from the text and long enough to be unique in the whole Law**, like the core's (`` `adopted by the stockholders under s 251(c)` ``, not `` `adopted` ``).
  A core constructor's words are never reused for anything else.
- **A field is a lowercase phrase naming the fact, with no leading `is` or `has`**: the genitive supplies the verb (`` merger's `approved by the board` ``).
  A name that contains a second `is` or `has` because the text's own words do is the one exception.
- **An input (a `GIVEN`) is a lowercase phrase naming the fact as a witness would state it**: `` `the number of votes in favor` ``, `` `the certificate of incorporation provides otherwise` ``.
  Several facts about one act or transaction go in one record parameter, not one parameter each.
  No section `GIVEN` (the stable build refuses it): put `GIVEN` on every rule that reads the input.
- **A fact about something outside the piece is an input named for the status and the section**, never recomputed and never guessed:
  `` `the instrument was executed, acknowledged and filed in accordance with § 103` `` (BOOLEAN), `` `the filing date under § 103` `` (DATE), `` `the amount payable under § 391` `` (NUMBER, dollars).
  The pattern `` `<what> in accordance with § N` `` or `` `<what> under § N` `` lets a later seat layer unify the same input taken by two pieces.
  Say in a comment which piece encodes the section.
  The same goes for statutes and rules not among the inputs (Title 6, Title 10, Title 26, 8 Del. C. ch. 5, federal law, the Court of Chancery Rules): take the outcome as an input with a comment, and list it in your NOTES.
- **A question, or the rule a seat layer would ask as one, is named as a proposition or a noun phrase**, from the person's side: `` `s 220(b) the stockholder may inspect the books and records` ``, `` `s 213(a) the earliest permitted record date` ``.
  The pieces write no seat layer and no `@export`.
  Rules the person would not ask but that others call keep their locator and a gloss.
- **A decision is a BOOLEAN named as a proposition. A figure or a date is a noun phrase. A case the text does not answer is `MAYBE T` with `NOTHING`**, asserted in a test.
  There is no `REFUSE` here, and never `FALSE`, `0` or a plausible default for an uncovered case.
- **Amounts**: a NUMBER of United States dollars, written as the text writes them ($0.01 is `0.01`, $2,500 is `2500`, ten million is `10_000_000`).
  The unit is dollars everywhere; say "in dollars" in a name only where a count or a rate sits beside it.
  Counts of shares, votes, directors and persons are NUMBERs and may be fractions (§ 155 allows fractions of shares).
- **Percentages and fractions**: exact NUMBERs, fractions of 1.
  "15%" is `15%` (the postfix `%` literal); "1/3" is `1 DIVIDED BY 3`; "66 2/3%" is `(200 DIVIDED BY 3)%`, which is exactly `2 DIVIDED BY 3`.
  Never a rounded decimal such as `0.6667`.
  "A majority" is the core's `a majority of`, not `0.5`.
- **Time limits**: a `Period`, never a bare NUMBER.
  `` `period in days` 60 ``, `` `period in weeks` 1 ``, `` `period in months` 6 ``, `` `period in years` 3 ``; the date a period after or before a date is `` `the date` p `after` d `` or `` `the date` p `before` d ``.
  Counting is calendar counting; the last day is inside "within N days after D" unless the provision says otherwise, and each such reading goes in your Fork register.
  The regulative `WITHIN n` of this build takes a bare number with no unit: use it only for a duty with a consequence whose limit is in days; otherwise compare dates.
- **Dates**: a DATE made with the core's `YMD year month day`, never with `Date day month year` for a literal (a transposition type-checks and is silently wrong).
  A date the text names (an enactment, a "prior to" date) is a named constant with an `@ref`.
  A date taken from a case is an input.
- **A displaceable default** ("unless otherwise provided in the certificate of incorporation or bylaws"): the core's `Where a provision is made` says where the displacing provision sits, a separate input carries what it says, and `in none of these` means the Law's default stands.
  Do not bake the default in as a bare constant with no way to displace it.
- **Citations**: every rule and every local type has an `@ref` above it, with `-- src:N | text` quote lines above that, copied mechanically from the text file, and `(src:N)` or `(src:N-M)` locators in the `@ref`.
  An `@ref` is never put above a `§` heading or a directive, or at the end of a file.
  The gate is `python3 -I srcrefs.py check --refs <the text file> <your .l4 files>`: it must print 0 problems.
  Lines of this text run to 4,832 characters (169 lines exceed 1,000): quote the operative words, starting and ending at word boundaries of the raw line, and end a cut quotation with ` …` (the gate accepts a prefix that ends in an ellipsis). `srcrefs.py quote RAW N` prints the whole line; copy a slice of it.
- **Files**: modules `dg<N>-<topic>.l4`, tests `dg<N>-tests-<topic>.l4`, in the piece's folder, flat, ASCII names.

## Defined terms

Every term the text defines, in the order of the text: 111 rows (a row may hold several terms that the text defines together, such as the three electronic-communication terms).
The keel's range is empty, so none is encoded here: each row names the piece and the section that encode it ("by reference: encoded by piece X, section N, taken there as an input", the brief's wording: the piece that needs the term takes it as an input).
A piece that reads a term another piece defines takes it as an input, except for the three kinds the core gives a type for (kind of corporation, where an entity is formed, kind of entity), named in the last clause of the row.
Each note opens with the scope of the definition, in square brackets, as one of five kinds. By count of rows: 11 chapter- or title-wide, 66 confined to its section, subsection or paragraph by its own words, 12 no scope stated in the definition, 17 deeming or construction rule, 5 points elsewhere (outside the inputs, or to another section).
After that the note gives the first words of the definition, copied mechanically from the text (a cut is marked by an ellipsis).
"Also read in" counts, by pattern, the occurrences of the term in other pieces' ranges, so a piece can see where a definition made elsewhere reaches it; the text is the authority.
A row is a deeming or construction rule where the text does not define the term but fixes how it is read.
Some definitions are repeated in different words in different sections (person, foreign jurisdiction, subsidiary, stockholder, affiliate): each is its own row.
The text uses "majority" throughout and defines it nowhere (Fork register, F4).

| term | defined at | encoded in | note |
| --- | --- | --- | --- |
| officer (in § 102(b)(7)) | § 102(b)(7) (src:67) | by reference: encoded by piece dg1, section 102(b)(7), taken there as an input | [confined to its section, subsection or paragraph by its own words] "All references in this paragraph (b)(7) to an officer shall mean only a person who at the time of an act or omission as to which liability is asserted is deemed to have consented to service …" Points to 10 Del. C. § 3114(b) (Title 10, not deposited): the outcome is an input. |
| facts | § 102(d), § 151(a), § 152, § 157, § 251, § 252, § 253, § 254, § 255, § 256, § 257, § 263, § 264, § 265, § 266, § 267, § 388, § 390 (src:69, 468, 487, 515, 1069, 1121, 1137, 1158, 1181, 1199, 1216, 1287, 1312, 1345, 1369, 1373, 1960, 2022) | by reference: encoded by each piece in its own sections, taken there as an input: dg1 (102); dg3 (151, 152, 157); dg6 (251, 252, 253, 254); dg7 (255, 256, 257); dg8 (263, 264, 265, 266, 267); dg11 (388, 390) | [confined to its section, subsection or paragraph by its own words] "The term “facts,” as used in this subsection, includes, but is not limited to, the occurrence of any event, including a determination or action by any person or body, including the …" The same sentence 18 times. Recommended: each piece records it as an inert row for its own sections and encodes no rule (it widens what an instrument may make a provision depend on; no case fact answers it). |
| total assets | § 102(a)(1) (src:42) | by reference: encoded by piece dg1, section 102(a)(1), taken there as an input | [points elsewhere (outside the inputs, or to another section)] "a certificate stating that its total assets, as defined in § 503(i) of this title, are not less than $10,000,000, or, in the sole discretion of the Division of Corporations in the …" "As defined in § 503(i) of this title" (8 Del. C. ch. 5, not deposited): an amount in dollars taken as an input. |
| members (of a nonstock corporation, where no criteria are stated) | § 102(a)(4) (src:45) | by reference: encoded by piece dg1, section 102(a)(4), taken there as an input | [deeming or construction rule] "If neither the certificate of incorporation nor the bylaws of a nonstock corporation state the conditions of membership, or other criteria for identifying members, the members of the …" A deeming rule, not a quoted definition. |
| filing date | § 103(c)(3) (src:93) | by reference: encoded by piece dg1, section 103(c)(3), taken there as an input | [no scope stated in the definition] "This endorsement is the “filing date” of the instrument, and is conclusive of the date and time of its filing in the absence of actual fraud. The Secretary of State shall file and index the …" |
| extraordinary condition | § 103(i)(2) (src:109) | by reference: encoded by piece dg1, section 103(i)(2), taken there as an input | [confined to its section, subsection or paragraph by its own words] "For purposes of this subsection, an “extraordinary condition” means: any emergency resulting from an attack on, invasion or occupation by foreign military forces of, or disaster, …" "For purposes of this subsection" only. |
| certificate of incorporation | § 104 (src:115) | by reference: encoded by piece dg1, section 104, taken there as an input | [chapter- or title-wide] "The term “certificate of incorporation,” as used in this chapter, unless the context requires otherwise, includes not only the original certificate of incorporation filed to create a …" Chapter-wide, "unless the context requires otherwise". Every piece takes "the certificate of incorporation" as the instrument as it now stands; none encodes § 104 itself. § 312(a) states a further inclusion for § 312 (dg9). |
| stockholders / board of directors / directors / stock, as read for a nonstock corporation | § 114(a)(1) to (4) (src:196-199) | by reference: encoded by piece dg1, section 114(a)(1) to (4), taken there as an input | [deeming or construction rule] "All references to stockholders of the corporation shall be deemed to refer to members of the corporation;" The lists of sections where the reading does not apply (§ 114(b), (c)) are, piece by piece, under Instructions to the pieces. |
| charitable nonstock corporation | § 114(d)(1) (src:209) | by reference: encoded by piece dg1, section 114(d)(1), taken there as an input; other pieces take the core type `Kind of corporation` | [chapter- or title-wide] "A “charitable nonstock corporation” is any nonprofit nonstock corporation that is exempt from taxation under § 501(c)(3) of the United States Internal Revenue Code [26 U.S.C. § 501(c)(3)], …" The tax exemption under 26 U.S.C. § 501(c)(3) is a fact dg1 takes as an input; other pieces take the core type. |
| membership interest | § 114(d)(2) (src:210) | by reference: encoded by piece dg1, section 114(d)(2), taken there as an input | [chapter- or title-wide] "A “membership interest” is, unless otherwise provided in a nonstock corporation’s certificate of incorporation, a member’s share of the profits and losses of a nonstock corporation, or a …" |
| nonprofit nonstock corporation | § 114(d)(3) (src:211) | by reference: encoded by piece dg1, section 114(d)(3), taken there as an input; other pieces take the core type `Kind of corporation` | [chapter- or title-wide] "A “nonprofit nonstock corporation” is a nonstock corporation that does not have membership interests; and" |
| nonstock corporation | § 114(d)(4) (src:212) | by reference: encoded by piece dg1, section 114(d)(4), taken there as an input; other pieces take the core type `Kind of corporation` | [chapter- or title-wide] "A “nonstock corporation” is any corporation organized under this chapter that is not authorized to issue capital stock." Chapter-wide ("for purposes of this chapter"). A stock corporation is the complement within the corporations organized under the chapter. |
| internal corporate claims | § 115(b) (src:217) | by reference: encoded by piece dg1, section 115(b), taken there as an input | [no scope stated in the definition] "“Internal corporate claims” means claims, including claims in the right of the corporation, (i) that are based upon a violation of a duty by a current or former director or officer or …" Pointed at by § 102(f) (src:76) and § 109(b) (src:142): "as defined in § 115 of this title". |
| document | § 116(a)(1) (src:223) | by reference: encoded by piece dg1, section 116(a)(1), taken there as an input | [no scope stated in the definition] "“Document” means:" |
| electronic signature | § 116(a)(2) (src:226) | by reference: encoded by piece dg1, section 116(a)(2), taken there as an input | [no scope stated in the definition] "“Electronic signature” means an electronic symbol or process that is attached to, or logically associated with, a document and executed or adopted by a person with an intent to execute, …" |
| registered office | § 131(b) (src:297) | by reference: encoded by piece dg2, section 131(b), taken there as an input | [chapter- or title-wide] "As used in this title, “registered office” means the address of the registered agent located in this State being appointed to accept service of process and otherwise perform the duties of a …" Also read in dg1 (4), dg3 (2), dg4 (3), dg5 (1), dg6 (1), dg9 (3), dg10 (5), dg11 (1). |
| Secretary (abbreviation) | § 132(b)(1)d. (src:311) | by reference: encoded by piece dg2, section 132(b)(1)d., taken there as an input | [no scope stated in the definition] "notification of same in a form satisfactory to the Secretary of State (“Secretary”); and" Within § 132. |
| virtual office | § 132(b)(2) (src:313) | by reference: encoded by piece dg2, section 132(b)(2), taken there as an input | [confined to its section, subsection or paragraph by its own words] "For purposes of this paragraph (b)(2), “virtual office” means the performance of duties or functions solely through the internet or solely through other means of remote communication." |
| commercial registered agent | § 132(c) and (c)(3) (src:314, 327) | by reference: encoded by piece dg2, section 132(c) and (c)(3), taken there as an input | [no scope stated in the definition] "Any registered agent who at any time serves as registered agent for more than 50 entities (a “commercial registered agent”), whether domestic or foreign, shall satisfy and comply with the …" |
| resident agent (and like terms) | § 132(h) (src:339) | by reference: encoded by piece dg2, section 132(h), taken there as an input | [deeming or construction rule] "Whenever the term “resident agent” or “resident agent in charge of a corporation’s principal office or place of business in this State,” or other term of like import which refers to a …" |
| committee (reference includes a subcommittee) | § 141(c)(3) (src:367) | by reference: encoded by piece dg2, section 141(c)(3), taken there as an input | [deeming or construction rule] "Except for references to committees and members of committees in subsection (c) of this section, every reference in this chapter to a committee of the board of directors or a member of a …" |
| control group | § 144(e)(1) (src:420) | by reference: encoded by piece dg2, section 144(e)(1), taken there as an input | [confined to its section, subsection or paragraph by its own words] "“Control group” means 2 or more persons that are not controlling stockholders that, by virtue of an agreement, arrangement, or understanding between or among such persons, constitute a …" § 144(e) is "for purposes of this section". |
| controlling stockholder | § 144(e)(2) (src:421) | by reference: encoded by piece dg2, section 144(e)(2), taken there as an input | [confined to its section, subsection or paragraph by its own words] "“Controlling stockholder” means any person that, together with such person’s affiliates and associates:" Uses "affiliates and associates" without defining them (§ 203(c)(1), (2) are "as used in this section only"). |
| controlling stockholder transaction | § 144(e)(3) (src:425) | by reference: encoded by piece dg2, section 144(e)(3), taken there as an input | [confined to its section, subsection or paragraph by its own words] "“Controlling stockholder transaction” means an act or transaction between the corporation or 1 or more of its subsidiaries, on the 1 hand, and a controlling stockholder or a control group, …" |
| disinterested director | § 144(e)(4) (src:426) | by reference: encoded by piece dg2, section 144(e)(4), taken there as an input | [confined to its section, subsection or paragraph by its own words] "“Disinterested director” means a director who is not a party to the act or transaction and does not have a material interest in the act or transaction or a material relationship with a …" |
| disinterested stockholder | § 144(e)(5) (src:427) | by reference: encoded by piece dg2, section 144(e)(5), taken there as an input | [confined to its section, subsection or paragraph by its own words] "“Disinterested stockholder” means any stockholder that does not have a material interest in the act or transaction at issue or, if applicable, a material relationship with the controlling …" |
| going private transaction | § 144(e)(6) (src:428-430) | by reference: encoded by piece dg2, section 144(e)(6), taken there as an input | [confined to its section, subsection or paragraph by its own words] "“Going private transaction” means:" Limb a. points to 17 CFR § 240.13e-3(a) and to the Securities Exchange Act of 1934 (federal, not deposited): inputs. |
| material interest | § 144(e)(7) (src:431) | by reference: encoded by piece dg2, section 144(e)(7), taken there as an input | [confined to its section, subsection or paragraph by its own words] "“Material interest” means an actual or potential benefit, including the avoidance of a detriment, other than 1 which would devolve on the corporation or the stockholders generally, that (i) …" |
| material relationship | § 144(e)(8) (src:432) | by reference: encoded by piece dg2, section 144(e)(8), taken there as an input | [confined to its section, subsection or paragraph by its own words] "“Material relationship” means a familial, financial, professional, employment, or other relationship that (i) in the case of a director, would reasonably be expected to impair the …" |
| officer (in § 145(c)(1) and (2)) | § 145(c)(1) (src:438) | by reference: encoded by piece dg2, section 145(c)(1), taken there as an input | [confined to its section, subsection or paragraph by its own words] "For indemnification with respect to any act or omission occurring after December 31, 2020, references to “officer” for purposes of paragraphs (c)(1) and (2) of this section shall mean only …" For an act or omission after December 31, 2020; points to 10 Del. C. § 3114(b) (Title 10, not deposited). |
| the corporation (in § 145) | § 145(h) (src:452) | by reference: encoded by piece dg2, section 145(h), taken there as an input | [deeming or construction rule] "For purposes of this section, references to “the corporation” shall include, in addition to the resulting corporation, any constituent corporation (including any constituent of a …" |
| other enterprises; fines; serving at the request of the corporation | § 145(i) (src:453) | by reference: encoded by piece dg2, section 145(i), taken there as an input | [deeming or construction rule] "For purposes of this section, references to “other enterprises” shall include employee benefit plans; references to “fines” shall include any excise taxes assessed on a person with respect …" |
| capital; surplus; net assets | § 154 (src:500) | by reference: encoded by piece dg3, section 154, taken there as an input | [no scope stated in the definition] "The excess, if any, at any given time, of the net assets of the corporation over the amount so determined to be capital shall be surplus. Net assets means the amount by which total assets …" The heading says "capital, surplus and net assets defined". Read again in § 160, § 170, § 172 and § 174 (dg3) and § 244 (dg5). |
| fully paid and nonassessable | § 152 (src:488) | by reference: encoded by piece dg3, section 152, taken there as an input | [deeming or construction rule] "The capital stock issued in accordance with this section shall be deemed to be fully paid and nonassessable stock upon receipt by the corporation of such consideration; provided, however, …" A deeming rule, not a quoted definition. |
| affiliate | § 203(c)(1) (src:650) | by reference: encoded by piece dg3, section 203(c)(1), taken there as an input | [confined to its section, subsection or paragraph by its own words] "“Affiliate” means a person that directly, or indirectly through 1 or more intermediaries, controls, or is controlled by, or is under common control with, another person." "As used in this section only" (§ 203(c)). |
| associate | § 203(c)(2) (src:651) | by reference: encoded by piece dg3, section 203(c)(2), taken there as an input | [confined to its section, subsection or paragraph by its own words] "“Associate,” when used to indicate a relationship with any person, means: (i) Any corporation, partnership, unincorporated association or other entity of which such person is a director, …" |
| business combination | § 203(c)(3) (src:652-657) | by reference: encoded by piece dg3, section 203(c)(3), taken there as an input | [confined to its section, subsection or paragraph by its own words] "“Business combination,” when used in reference to any corporation and any interested stockholder of such corporation, means:" Five limbs (i) to (v). |
| control (controlling, controlled by, under common control with) | § 203(c)(4) (src:658) | by reference: encoded by piece dg3, section 203(c)(4), taken there as an input | [confined to its section, subsection or paragraph by its own words] "“Control,” including the terms “controlling,” “controlled by” and “under common control with,” means the possession, directly or indirectly, of the power to direct or cause the direction of …" |
| interested stockholder | § 203(c)(5) (src:659) | by reference: encoded by piece dg3, section 203(c)(5), taken there as an input | [confined to its section, subsection or paragraph by its own words] "“Interested stockholder” means any person (other than the corporation and any direct or indirect majority-owned subsidiary of the corporation) that (i) is the owner of 15% or more of the …" Also read in dg2 (6), dg6 (2). |
| person | § 203(c)(6) (src:660) | by reference: encoded by piece dg3, section 203(c)(6), taken there as an input; other pieces take the core type `Kind of entity` | [confined to its section, subsection or paragraph by its own words] "“Person” means any individual, corporation, partnership, unincorporated association or other entity." Re-defined, in different words, in § 251(h)(6)e. (dg6), § 262(a) (dg7) and § 267(d)(2) (dg8, as "entity"). The core's Kind of entity is the superset those definitions are read over; its first constructor is `a natural person` (the "individual"). |
| stock | § 203(c)(7) (src:661) | by reference: encoded by piece dg3, section 203(c)(7), taken there as an input | [confined to its section, subsection or paragraph by its own words] "“Stock” means, with respect to any corporation, capital stock and, with respect to any other entity, any equity interest." |
| voting stock | § 203(c)(8) (src:662) | by reference: encoded by piece dg3, section 203(c)(8), taken there as an input | [confined to its section, subsection or paragraph by its own words] "“Voting stock” means, with respect to any corporation, stock of any class or series entitled to vote generally in the election of directors and, with respect to any entity that is not a …" Also read in dg1 (1), dg4 (2), dg5 (2). |
| owner (own, owned) | § 203(c)(9) (src:663) | by reference: encoded by piece dg3, section 203(c)(9), taken there as an input | [confined to its section, subsection or paragraph by its own words] "“Owner,” including the terms “own” and “owned,” when used with respect to any stock, means a person that individually or with or through any of its affiliates or associates:" Three limbs follow. |
| defective corporate act | § 204(h)(1) (src:715) | by reference: encoded by piece dg4, section 204(h)(1), taken there as an input | [confined to its section, subsection or paragraph by its own words] "“Defective corporate act” means an overissue, an election or appointment of directors that is void or voidable due to a failure of authorization, or any act or transaction purportedly taken …" "As used in this section and in § 205 of this title only" (§ 204(h)). |
| failure of authorization | § 204(h)(2) (src:716) | by reference: encoded by piece dg4, section 204(h)(2), taken there as an input | [confined to its section, subsection or paragraph by its own words] "“Failure of authorization” means: (i) the failure to authorize or effect an act or transaction in compliance with (A) the provisions of this title, (B) the certificate of incorporation or …" |
| overissue | § 204(h)(3) (src:717-719) | by reference: encoded by piece dg4, section 204(h)(3), taken there as an input | [confined to its section, subsection or paragraph by its own words] "“Overissue” means the purported issuance of:" |
| putative stock | § 204(h)(4) (src:720) | by reference: encoded by piece dg4, section 204(h)(4), taken there as an input | [confined to its section, subsection or paragraph by its own words] "“Putative stock” means the shares of any class or series of capital stock of the corporation (including shares issued upon exercise of options, rights, warrants or other securities …" |
| time of the defective corporate act | § 204(h)(5) (src:723) | by reference: encoded by piece dg4, section 204(h)(5), taken there as an input | [confined to its section, subsection or paragraph by its own words] "“Time of the defective corporate act” means the date and time the defective corporate act was purported to have been taken;" |
| validation effective time | § 204(h)(6) (src:724-727) | by reference: encoded by piece dg4, section 204(h)(6), taken there as an input | [confined to its section, subsection or paragraph by its own words] "“Validation effective time,” with respect to any defective corporate act ratified pursuant to this section, means the latest of:" |
| valid stock | § 204(h)(7) (src:728) | by reference: encoded by piece dg4, section 204(h)(7), taken there as an input | [confined to its section, subsection or paragraph by its own words] "“Valid stock” means the shares of any class or series of capital stock of the corporation that have been duly authorized and validly issued in accordance with this title." |
| stock ledger | § 219(c) (src:838) | by reference: encoded by piece dg4, section 219(c), taken there as an input | [chapter- or title-wide] "For purposes of this chapter, “stock ledger” means 1 or more records administered by or on behalf of the corporation in which the names of all of the corporation’s stockholders of record, …" Chapter-wide ("for purposes of this chapter"). Also read in dg1 (1), dg5 (2). |
| books and records | § 220(a)(1) (src:843) | by reference: encoded by piece dg4, section 220(a)(1), taken there as an input | [confined to its section, subsection or paragraph by its own words] "“Books and records” means all of the following:" "As used in this section" (§ 220(a)). Also read in dg3 (1), dg5 (1). |
| proper purpose | § 220(a)(2) (src:853) | by reference: encoded by piece dg4, section 220(a)(2), taken there as an input | [confined to its section, subsection or paragraph by its own words] "“Proper purpose” means a purpose reasonably related to a stockholder’s interest as a stockholder." |
| stockholder (in § 220) | § 220(a)(3) (src:854) | by reference: encoded by piece dg4, section 220(a)(3), taken there as an input | [confined to its section, subsection or paragraph by its own words] "“Stockholder” means a person who is a holder of record of stock in a stock corporation, or a person who is the beneficial owner of shares of such stock held either in a voting trust or by a …" Not the same words as "stockholder" in § 262(a) (dg7). |
| subsidiary (in § 220) | § 220(a)(4) (src:855) | by reference: encoded by piece dg4, section 220(a)(4), taken there as an input | [confined to its section, subsection or paragraph by its own words] "“Subsidiary” means any entity directly or indirectly owned, in whole or in part, by the corporation of which the stockholder is a stockholder and over the affairs of which the corporation …" Another definition in § 271(c) (dg9). |
| under oath | § 220(a)(5) (src:856) | by reference: encoded by piece dg4, section 220(a)(5), taken there as an input | [confined to its section, subsection or paragraph by its own words] "“Under oath” includes statements the declarant affirms to be true under penalty of perjury under the laws of the United States or any state." |
| holders of bonds, debentures and other obligations (as stockholders) | § 221 (src:891) | by reference: encoded by piece dg5, section 221, taken there as an input | [deeming or construction rule] "such holders of bonds, debentures or other obligations shall be deemed to be stockholders, and their bonds, debentures or other obligations shall be deemed to be shares of stock, for the …" A deeming rule, not a quoted definition. |
| consent (in § 228) | § 228(c) (src:937) | by reference: encoded by piece dg5, section 228(c), taken there as an input | [deeming or construction rule] "All references to a “consent” in this section means a consent permitted by this section." |
| electronic transmission | § 232(d)(1) (src:984) | by reference: encoded by piece dg5, section 232(d)(1), taken there as an input | [chapter- or title-wide] "“Electronic transmission” means any form of communication, not directly involving the physical transmission of paper, including the use of, or participation in, 1 or more electronic …" Chapter-wide ("for purposes of this chapter"). § 116(a)(1) makes an electronic transmission "the equivalent of a written document": take "in writing or by electronic transmission" as one fact unless the provision tells the media apart (as § 232 does). Also read in dg1 (12), dg2 (2), dg3 (1), dg4 (9), dg6 (1), dg7 (4), dg8 (3), dg9 (1), dg10 (4), dg11 (1). |
| electronic mail | § 232(d)(2) (src:985) | by reference: encoded by piece dg5, section 232(d)(2), taken there as an input | [chapter- or title-wide] "“Electronic mail” means an electronic transmission directed to a unique electronic mail address (which electronic mail shall be deemed to include any files attached thereto and any …" |
| electronic mail address; local part | § 232(d)(3) (src:986) | by reference: encoded by piece dg5, section 232(d)(3), taken there as an input | [chapter- or title-wide] "“Electronic mail address” means a destination, commonly expressed as a string of characters, consisting of a unique user name or mailbox (commonly referred to as the “local part” of the …" |
| directors (read as members of the governing body) | § 241(c) (src:1006) | by reference: encoded by piece dg5, section 241(c), taken there as an input | [deeming or construction rule] "all references to directors shall be deemed to be references to members of the governing body of the corporation." A deeming rule for nonstock corporations. |
| organizational documents | § 251(g) (src:1089) | by reference: encoded by piece dg6, section 251(g), taken there as an input | [confined to its section, subsection or paragraph by its own words] "The term “organizational documents”, as used in paragraph (g)(7) of this section and in the preceding sentence, shall, when used in reference to a corporation, mean the certificate of …" |
| holding company | § 251(g) (src:1090) | by reference: encoded by piece dg6, section 251(g), taken there as an input | [confined to its section, subsection or paragraph by its own words] "As used in this subsection only, the term “holding company” means a corporation which, from its incorporation until consummation of a merger governed by this subsection, was at all times a …" |
| affiliate (in § 251(h)) | § 251(h)(6)a. (src:1101) | by reference: encoded by piece dg6, section 251(h)(6)a., taken there as an input | [confined to its section, subsection or paragraph by its own words] "“Affiliate” means, in respect of the corporation making the offer referred to in paragraph (h)(2) of this section, any person that (i) owns, directly or indirectly, all of the outstanding …" "As used in this section only" (§ 251(h)(6)). |
| consummates (consummation, consummating) | § 251(h)(6)b. (src:1102) | by reference: encoded by piece dg6, section 251(h)(6)b., taken there as an input | [confined to its section, subsection or paragraph by its own words] "“Consummates” (and with correlative meaning, “consummation” and “consummating”) means irrevocably accepts for purchase or exchange stock tendered pursuant to an offer;" |
| depository | § 251(h)(6)c. (src:1103) | by reference: encoded by piece dg6, section 251(h)(6)c., taken there as an input | [confined to its section, subsection or paragraph by its own words] "“Depository” means an agent, including a depository, appointed to facilitate consummation of the offer referred to in paragraph (h)(2) of this section;" |
| excluded stock | § 251(h)(6)d. (src:1104) | by reference: encoded by piece dg6, section 251(h)(6)d., taken there as an input | [confined to its section, subsection or paragraph by its own words] "“Excluded stock” means (i) stock of such constituent corporation that is owned at the commencement of the offer referred to in paragraph (h)(2) of this section by such constituent …" |
| person (in § 251(h)) | § 251(h)(6)e. (src:1105) | by reference: encoded by piece dg6, section 251(h)(6)e., taken there as an input; other pieces take the core type `Kind of entity` | [confined to its section, subsection or paragraph by its own words] "“Person” means any individual, corporation, partnership, limited liability company, unincorporated association or other entity;" |
| received (in § 251(h)(3)) | § 251(h)(6)f. (src:1106) | by reference: encoded by piece dg6, section 251(h)(6)f., taken there as an input | [confined to its section, subsection or paragraph by its own words] "“Received” (solely for purposes of paragraph (h)(3) of this section) means (a) with respect to certificated shares, physical receipt of a stock certificate accompanied by an executed letter …" |
| rollover stock | § 251(h)(6)g. (src:1107) | by reference: encoded by piece dg6, section 251(h)(6)g., taken there as an input | [confined to its section, subsection or paragraph by its own words] "“Rollover stock” means any shares of stock of such constituent corporation that are the subject of a written agreement requiring such shares to be transferred, contributed or delivered to …" |
| agreement of merger (in § 253) | § 253(c) (src:1141) | by reference: encoded by piece dg6, section 253(c), taken there as an input | [deeming or construction rule] "Section § 251(d) of this title shall apply to a merger under this section, and § 251(e) of this title shall apply to a merger under this section in which the surviving corporation is the …" A construction rule, not a quoted definition. |
| joint-stock association; stockholder (in § 254) | § 254(a) (src:1148) | by reference: encoded by piece dg6, section 254(a), taken there as an input; other pieces take the core type `Kind of entity` | [confined to its section, subsection or paragraph by its own words] "The term “joint-stock association” as used in this section, includes any association of the kind commonly known as a joint-stock association or joint-stock company and any unincorporated …" Also read in dg8 (1). |
| stockholder (read as including member), board and shares in §§ 255 to 258 | § 255, § 256, § 257, § 258 (src:1182, 1184, 1200, 1203, 1217, 1219, 1226) | by reference: encoded by piece dg7, section 255, 256, 257, 258, taken there as an input | [deeming or construction rule] "and the reference therein to “stockholder” shall be deemed to include “member” hereunder." Construction rules, not quoted definitions. |
| foreign nonstock corporation | § 256(a) (src:1190) | by reference: encoded by piece dg7, section 256(a), taken there as an input | [no scope stated in the definition] "The term “foreign nonstock corporation” means a nonstock corporation organized under the laws of any jurisdiction other than this State." |
| foreign corporation (in § 258) | § 258(a) (src:1224) | by reference: encoded by piece dg7, section 258(a), taken there as an input | [confined to its section, subsection or paragraph by its own words] "For purposes of this section, the term “foreign corporation” includes a nonstock corporation organized under the laws of any jurisdiction other than this State." |
| stockholder; stock and share; depository receipt; beneficial owner; person (in § 262) | § 262(a) (src:1252) | by reference: encoded by piece dg7, section 262(a), taken there as an input; other pieces take the core type `Kind of entity` | [confined to its section, subsection or paragraph by its own words] "As used in this section, the word “stockholder” means a holder of record of stock in a corporation; the words “stock” and “share” mean and include what is ordinarily meant by those words; …" "As used in this section" (§ 262(a)). Not the same words as "stockholder" in § 220(a)(3) (dg4). |
| partnership | § 263(a) (src:1278) | by reference: encoded by piece dg8, section 263(a), taken there as an input; other pieces take the core type `Kind of entity` | [confined to its section, subsection or paragraph by its own words] "The term “partnership” as used in this section includes any partnership (whether general (including a limited liability partnership) or limited (including a limited liability limited …" |
| limited liability company | § 264(a) (src:1303) | by reference: encoded by piece dg8, section 264(a), taken there as an input; other pieces take the core type `Kind of entity` | [confined to its section, subsection or paragraph by its own words] "The term “limited liability company” as used in this section includes any limited liability company formed under the laws of this State or the laws of any other jurisdiction." |
| other entity | § 265(a) (src:1328) | by reference: encoded by piece dg8, section 265(a), taken there as an input; other pieces take the core type `Kind of entity` | [confined to its section, subsection or paragraph by its own words] "As used in this section, the term “other entity” means a limited liability company, statutory trust, business trust or association, real estate investment trust, common-law trust or any …" |
| constituent party | § 267(d)(1) (src:1377) | by reference: encoded by piece dg8, section 267(d)(1), taken there as an input | [confined to its section, subsection or paragraph by its own words] "“Constituent party” means an entity or corporation to be merged pursuant to this section;" "As used in this section only" (§ 267(d)). |
| entity (in § 267) | § 267(d)(2) (src:1378) | by reference: encoded by piece dg8, section 267(d)(2), taken there as an input; other pieces take the core type `Kind of entity` | [confined to its section, subsection or paragraph by its own words] "“Entity” means a partnership (whether general (including a limited liability partnership) or limited (including a limited liability limited partnership)), limited liability company, any …" |
| governing documents | § 267(d)(3) (src:1379) | by reference: encoded by piece dg8, section 267(d)(3), taken there as an input | [confined to its section, subsection or paragraph by its own words] "“Governing documents” means a partnership agreement, limited liability company agreement, articles of association or any other instrument containing the provisions by which an entity is …" |
| subsidiary (in § 271) | § 271(c) (src:1391) | by reference: encoded by piece dg9, section 271(c), taken there as an input | [confined to its section, subsection or paragraph by its own words] "As used in this subsection, “subsidiary” means any entity wholly-owned and controlled, directly or indirectly, by the corporation and includes, without limitation, corporations, …" |
| contractual claims | § 280(b)(1) (src:1476) | by reference: encoded by piece dg9, section 280(b)(1), taken there as an input | [confined to its section, subsection or paragraph by its own words] "Provided however, that as used in this section and in § 281 of this title, the term “contractual claims” shall not include any implied warranty as to any product manufactured, sold, …" |
| successor entity | § 280(e), § 281(d) (src:1482, 1496) | by reference: encoded by piece dg9, section 280(e), 281(d), taken there as an input | [confined to its section, subsection or paragraph by its own words] "As used in this section, the term “successor entity” shall include any trust, receivership or other legal entity governed by the laws of this State to which the remaining assets and …" § 281(d) (src:1496) points back to § 280(e). |
| priority (in § 281) | § 281(e) (src:1497) | by reference: encoded by piece dg9, section 281(e), taken there as an input | [confined to its section, subsection or paragraph by its own words] "The term “priority,” as used in this section, does not refer either to the order of payments set forth in paragraph (a)(1)-(4) of this section or to the relative times at which any claims …" |
| stockholders (in § 311) | § 311(a)(1) (src:1585) | by reference: encoded by piece dg9, section 311(a)(1), taken there as an input | [confined to its section, subsection or paragraph by its own words] "For purposes of this section, the term “stockholders” shall mean the stockholders of record on the date the dissolution became effective or the date of expiration by limitation." |
| certificate of incorporation (in § 312) | § 312(a) (src:1606) | by reference: encoded by piece dg9, section 312(a), taken there as an input | [confined to its section, subsection or paragraph by its own words] "As used in this section, the term “certificate of incorporation” includes the charter of a corporation organized under any special act or any law of this State." |
| board of directors or governing body (in § 312) | § 312(h) (src:1618) | by reference: encoded by piece dg9, section 312(h), taken there as an input | [confined to its section, subsection or paragraph by its own words] "For purposes of this section and § 502(a) of this title, the board of directors or governing body of the corporation shall be comprised of the persons, who, but for the certificate of …" Also "for purposes of" 8 Del. C. § 502(a) (ch. 5, not deposited). |
| exempt corporation (in § 313) | § 313(c) (src:1626) | by reference: encoded by piece dg9, section 313(c), taken there as an input | [points elsewhere (outside the inputs, or to another section)] "As used in this section, the term “exempt corporation” shall have the meaning given to it in § 501(b) of this title. Nothing contained in this section relieves any exempt corporation from …" "The meaning given to it in § 501(b) of this title" (8 Del. C. ch. 5, not deposited): a BOOLEAN input. The same pointer is in § 391(j). |
| transfer (in § 347) | § 347(f) (src:1727) | by reference: encoded by piece dg10, section 347(f), taken there as an input | [confined to its section, subsection or paragraph by its own words] "The term “transfer,” as used in this section, is not limited to a transfer for value." |
| close corporation | § 342(a) (src:1688-1691) | by reference: encoded by piece dg10, section 342(a), taken there as an input | [no scope stated in the definition] "A close corporation is a corporation organized under this chapter whose certificate of incorporation contains the provisions required by § 102 of this title and, in addition, provides that:" The heading says "Close corporation defined". |
| public offering (in § 342(a)(3)) | § 342(a)(3) (src:1691) | by reference: encoded by piece dg10, section 342(a)(3), taken there as an input | [points elsewhere (outside the inputs, or to another section)] "The corporation shall make no offering of any of its stock of any class which would constitute a “public offering” within the meaning of the United States Securities Act of 1933 [15 U.S.C. …" "Within the meaning of the United States Securities Act of 1933" (federal, not deposited): an input. |
| stockholders (deemed directors, in § 351) | § 351(2) (src:1749) | by reference: encoded by piece dg10, section 351(2), taken there as an input | [deeming or construction rule] "Unless the context clearly requires otherwise, the stockholders of the corporation shall be deemed to be directors for purposes of applying provisions of this chapter; and" A deeming rule, not a quoted definition. |
| public benefit corporation | § 362(a) (src:1788) | by reference: encoded by piece dg10, section 362(a), taken there as an input | [no scope stated in the definition] "A “public benefit corporation” is a for-profit corporation organized under and subject to the requirements of this chapter that is intended to produce a public benefit or public benefits …" The heading says "Public benefit corporation defined". |
| public benefit; public benefit provisions | § 362(b) (src:1791) | by reference: encoded by piece dg10, section 362(b), taken there as an input | [no scope stated in the definition] "“Public benefit” means a positive effect (or reduction of negative effects) on 1 or more categories of persons, entities, communities or interests (other than stockholders in their …" |
| public benefit corporation (name designations) | § 362(c) (src:1792) | by reference: encoded by piece dg10, section 362(c), taken there as an input | [deeming or construction rule] "The name of the public benefit corporation may contain the words “public benefit corporation,” or the abbreviation “P.B.C.,” or the designation “PBC,” which shall be deemed to satisfy the …" A deeming rule, not a quoted definition. |
| foreign corporation | § 371(a) (src:1832) | by reference: encoded by piece dg10, section 371(a), taken there as an input; other pieces take the core type `Where an entity is formed` | [chapter- or title-wide] "As used in this chapter, the words “foreign corporation” mean a corporation organized under the laws of any jurisdiction other than this State." Chapter-wide ("as used in this chapter"). The core's Where an entity is formed carries the fact for the other pieces that read the term. Also read in dg1 (10), dg2 (6), dg3 (1), dg6 (10), dg7 (7), dg8 (3), dg9 (3), dg11 (14). |
| the transaction of business; business transacted in this State | § 382(b) (src:1919) | by reference: encoded by piece dg10, section 382(b), taken there as an input | [confined to its section, subsection or paragraph by its own words] "Section 373 of this title shall not apply in determining whether any foreign corporation is transacting business in this State within the meaning of this section; and “the transaction of …" |
| foreign jurisdiction (in § 388) | § 388(a)(1) (src:1939) | by reference: encoded by piece dg11, section 388(a)(1), taken there as an input; other pieces take the core type `Where an entity is formed` | [confined to its section, subsection or paragraph by its own words] "“Foreign jurisdiction” means any foreign country or other foreign jurisdiction (other than the United States, any state, the District of Columbia, or any possession or territory of the …" Defined again, in the same words, in § 390(a)(1), and by reference in § 389(a)(2). |
| non-United States entity | § 388(a)(2) (src:1940) | by reference: encoded by piece dg11, section 388(a)(2), taken there as an input; other pieces take the core type `Kind of entity` | [confined to its section, subsection or paragraph by its own words] "“Non-United States entity” means a corporation, a limited liability company, a statutory trust, a business trust or association, a real estate investment trust, a common-law trust, or any …" Also read in dg7 (3). |
| emergency condition | § 389(a)(1) (src:1966) | by reference: encoded by piece dg11, section 389(a)(1), taken there as an input | [confined to its section, subsection or paragraph by its own words] "The term “emergency condition” shall be deemed to include but not be limited to any of the following:" A list a. to j. follows. |
| foreign jurisdiction; non-United States entity (in § 389) | § 389(a)(2) (src:1977) | by reference: encoded by piece dg11, section 389(a)(2), taken there as an input | [points elsewhere (outside the inputs, or to another section)] "The term “foreign jurisdiction” and the term “non-United States entity” shall have the same meanings as set forth in § 388(a) of this title." |
| officers and directors (in § 389) | § 389(a)(3) (src:1978) | by reference: encoded by piece dg11, section 389(a)(3), taken there as an input | [deeming or construction rule] "The terms “officers” and “directors” include, in addition to such persons, trustees, managers, partners and all other persons performing functions equivalent to those of officers and …" |
| domicile (in § 389) | § 389(b) (src:1979) | by reference: encoded by piece dg11, section 389(b), taken there as an input | [deeming or construction rule] "Any non-United States entity may, subject to and upon compliance with this section, transfer its domicile (which term, as used in this section, shall be deemed to refer in addition to the …" |
| enemy (in § 389) | § 389(g) (src:1996) | by reference: encoded by piece dg11, section 389(g), taken there as an input | [deeming or construction rule] "For purposes of any action in the courts of this State, no non-United States entity which has obtained the certificate of the Secretary of State referred to in subsection (e) of this …" |
| foreign jurisdiction (in § 390) | § 390(a)(1) (src:2005) | by reference: encoded by piece dg11, section 390(a)(1), taken there as an input; other pieces take the core type `Where an entity is formed` | [confined to its section, subsection or paragraph by its own words] "“Foreign jurisdiction” means any foreign country, or other foreign jurisdiction (other than the United States, any state, the District of Columbia, or any possession or territory of the …" |
| resulting entity | § 390(a)(2) (src:2006) | by reference: encoded by piece dg11, section 390(a)(2), taken there as an input | [confined to its section, subsection or paragraph by its own words] "“Resulting entity” means the entity formed, incorporated, created or otherwise coming into being as a consequence of the transfer of the corporation to, or its domestication or continuance …" |
| exempt corporation (in § 391) | § 391(j) (src:2078) | by reference: encoded by piece dg11, section 391(j), taken there as an input | [points elsewhere (outside the inputs, or to another section)] "As used in this section, the term “exempt corporation” shall have the meaning given to it in § 501(b) of this title." |
| General Corporation Law of the State of Delaware | § 398 (src:2110) | by reference: encoded by piece dg11, section 398, taken there as an input | [no scope stated in the definition] "This chapter shall be known and may be identified and referred to as the “General Corporation Law of the State of Delaware.”" The short title. |

## Instructions to the pieces

Read these before you import the core.
Each is here because getting it wrong in one piece would cost the other ten something.

1. **Import by file name.** Write `IMPORT prelude`, then `` IMPORT `dg-core` `` (the file is in your folder: do not copy or edit it), and `IMPORT daydate` if you use `Date`, `Day` or `add months`.
   Name your modules `dg<N>-<topic>.l4` and your tests `dg<N>-tests-<topic>.l4`.
2. **Do not define `YMD`.** The core defines it once (`YMD y m d MEANS Date d m y`), because the stable build has none.
   A second definition in your module makes `YMD` unusable ("multiple definitions").
   The brief tells you to add a local shim: here the core is that shim.
3. **Do not redeclare a core type, constructor or rule, and do not reuse a core constructor's words for anything else.** The Vocabulary table is the complete list.
   If the text names a party the `Actor` type lacks, use `another party named in the provision` with the text's own words, or (only if you need more than a few) your own type whose name begins with your locator or piece id; a rule has one party type, so do not mix the core `Actor` and your own in one `PARTY`.
4. **Name everything as the Naming conventions say**, section locator first.
   Two pieces will be composed into one folder later, and a name defined by both cannot be used.
5. **Write the dialect the stable build reads.** The table in "What the stable binary does not accept" covers every construct the skill's `dialects.md` lists as rejected (probes 01 to 58).
   The ones you will reach for most: no section `GIVEN`; put `NOT` in brackets, always; no `REFUSE`, `#ASSERT REFUSED` or `BECAUSE` (except `LEST BREACH ...
   BECAUSE`, which the brief says is accepted); no `TYPICALLY`; no body-less `DECLARE`; no `SET OF`; no `EVERY` or `WHOSE`; no `RULES EFFECTIVE DATE` or `EVAL UNDER ...` (take the version date as an input); one `#ASSERT` per line.
6. **A cross-reference into another piece is an input.** You cannot import another piece.
   Where your provision turns on a status or figure that another piece's section decides, take it as a plain input named for it, with its section (Naming conventions), and say in a comment which piece encodes that section.
   List every such input in your NOTES.
   The sections other sections cite most are in the table below; § 103 alone is cited 85 times.
7. **Statutes and rules that are not among your inputs** (Title 6, Title 10, Title 26, 8 Del. C. ch. 5, federal law, the Court of Chancery Rules) are taken as plain inputs with a comment, and listed in your NOTES.
   The places they occur are in the table below.
8. **Time limits.** Use `Period` and the core's date arithmetic.
   "Within N days after D" is `e AT MOST (`the date` p `after` d)` for the event date e and "not less than 10 nor more than 60 days before D" is two comparisons on dates, both ends inclusive (§ 213(a) is the model).
   Months and years clamp to the last day of the month (31 August plus 6 months is 28 February): that is a fork, recorded here, and you do not need to re-record it unless your provision depends on the day.
9. **Votes and quorums.** Count votes, not shares: § 212(a) says that if the certificate gives more or less than one vote per share, every reference in the chapter to a majority or other proportion of stock, voting stock or shares "shall refer to such majority or other proportion of the votes of such stock, voting stock or shares".
   Use `a majority of` for "a majority" (more than half) and `at least ... of` for "at least", "not less than", "no less than"; ask `the vote carries`.
   It answers `NOTHING` when the counts cannot be a vote; carry that `NOTHING` up, never turn it into `FALSE`.
   A plurality (§ 216(3), directors elected by a plurality of the votes) is not a proportion of a base: dg4 encodes it as a comparison between candidates.
   A quorum is a `Vote requirement` too (§ 216: "in no event shall a quorum consist of less than 1/3 of the shares entitled to vote at the meeting"): ask `the vote carries` with the count present as the first count and the shares entitled to vote as the base.
10. **"Unless otherwise provided in the certificate of incorporation or the bylaws"** is on nearly every page.
   Take the displacing provision as `Where a provision is made` plus a separate input for what it says, and let `in none of these` give the Law's default.
   Where the certificate is allowed to ask for more than the Law (§ 102(b)(4): "a larger portion of the stock ... or a larger number of the directors"), take the larger requirement as a `Vote requirement` input.
11. **Nonstock corporations.** § 114(a) reads "stockholders" as "members", "board of directors" as "governing body", "directors" as "members of the governing body" and "stock" as "memberships" or "membership interests", except where § 114(b) and (c) say otherwise.
   Take the corporation's kind as the core's `Kind of corporation`; do not invent a second flag.
   The table below gives, for each piece, the sections in its range that § 114(b) or (c) lists.
   Where a vote of "the outstanding stock entitled to vote" is read as a vote of members, use the same `Vote base`.
12. **Defined terms.** A term the text defines "as used in this section only" is encoded in your piece, under that section, as a rule from facts.
   A term defined in another piece is an input in yours.
   The core gives a type only for kind of corporation, where an entity is formed, and kind of entity.
   Where a definition of "person" begins "any individual, corporation, ..." (§ 203(c)(6), § 251(h)(6)e., § 262(a)), write it as a predicate over `Kind of entity`, whose first constructor is `a natural person`; do not invent an "is an individual" flag.
   The Defined terms table names the piece for every definition in the text.
13. **The seat, and officials.** Write for the individual.
   A provision addressed to the Secretary of State, the Court of Chancery or the Attorney General is encoded for what it means to the person: what may be done to them, what they must be given, by when.
   A judgment the Law hands to the Court or an official is an input answered conditionally ("..., if the Court of Chancery so orders"), never guessed.
   Record the seat in your NOTES.
14. **Coverage: every non-blank line of your range must fall inside the source-lines cell of some row.** That includes: for dg1, lines 1 to 33 (the file's own preamble: title, the 18 source URLs, the currency, "UNOFFICIAL VERSION" and "Kept:" notices, the rule, then "TITLE 8", "Corporations", "CHAPTER 1.
   General Corporation Law"); each subchapter heading line in your range (`inert`, a pure title); each section heading line; each `History:` line (`inert`: citations of the 1953 Code and the Laws of Delaware, not provisions); each bracketed note in a heading; and each line struck as repealed or reserved.
   Both reserved sections have no `History:` line.
15. **The "facts" sentence.** "The term 'facts,' as used in this subsection, includes, but is not limited to, the occurrence of any event, including a determination or action by any person or body, including the corporation" appears in 18 places (Defined terms table).
   Recommended disposition: `inert`, with the reason that it widens what an instrument may make a provision depend on and no case fact answers it.
16. **Bracketed application notes** in 19 section headings (listed below) point to session-law application clauses that are not among your inputs.
   They are not provisions: `inert`, naming the Laws of Delaware cite, with the reason that the clause itself is not in the text.
17. **Dates and vintages.** The text is one vintage (acts enacted as of 2026-10-01).
   The keel found no commencement rule of the Law's own among the definitions it read; each piece looks in its own range (dates are data).
   Absolute dates that appear in the text, by piece, are listed below; carry each one a rule depends on as a named constant with an `@ref`.
18. **Tests.** Expected values are written by hand from the text, never copied from your own output.
   Each directive is on one line.
   `check.sh` must show 0 errors, 0 failed, 0 refused; `srcrefs.py check --refs` must show 0 problems.
   A test that fails on purpose is allowed only if your NOTES records it as a finding.

### Sections and the pieces that encode them

| subchapter | sections | piece |
| --- | --- | --- |
| I. Formation | 101-116 | dg1 |
| II. Powers | 121-127 | dg2 |
| III. Registered Office and Registered Agent | 131-136 | dg2 |
| IV. Directors and Officers | 141-147 | dg2 |
| V. Stock and Dividends | 151-174 | dg3 |
| VI. Stock Transfers | 201-203 | dg3 |
| VI. Stock Transfers | 204-205 | dg4 |
| VII. Meetings, Elections, Voting and Notice | 211-220 | dg4 |
| VII. Meetings, Elections, Voting and Notice | 221-233 | dg5 |
| VIII. Amendment of Certificate of Incorporation; Changes in Capital and Capital Stock | 241-246 | dg5 |
| IX. Merger, Consolidation or Conversion | 251-254 | dg6 |
| IX. Merger, Consolidation or Conversion | 255-262 | dg7 |
| IX. Merger, Consolidation or Conversion | 263-268 | dg8 |
| X. Sale of Assets, Dissolution and Winding Up | 271-285 | dg9 |
| XI. Insolvency; Receivers and Trustees | 291-303 | dg9 |
| XII. Renewal, Revival, Extension and Restoration of Certificate of Incorporation or Charter | 311-314 | dg9 |
| XIII. Suits Against Corporations, Directors, Officers or Stockholders | 321-330 | dg10 |
| XIV. Close Corporations; Special Provisions | 341-356 | dg10 |
| XV. Public Benefit Corporations | 361-368 | dg10 |
| XVI. Foreign Corporations | 371-385 | dg10 |
| XVII. Domestication and Transfer | 388-390 | dg11 |
| XVIII. Miscellaneous Provisions | 391-398 | dg11 |

Section 246 (dg5) and section 392 (dg11) are printed `[Reserved.]`. Lines struck as repealed or reserved: src:234 (§ 116, dg1); src:998 (§ 233, dg5); src:1046 (§ 244, dg5); src:1057 (§ 246, dg5); src:1096 (§ 251, dg6); src:1130 (§ 252, dg6); src:1261 (§ 262, dg7); src:1352 (§ 266, dg8); src:2081 (§ 392, dg11). Disposition: `repealed or blank in this text`.

### The sections most cited

Counted as occurrences of `§ N` or `§§ N` in the text outside the `History:` lines and the preamble (a range such as `§§ 133-136` counts once, at its first number, so these are lower bounds). The count includes citations from inside the owning piece.

| section | piece | heading | times cited |
| --- | --- | --- | --- |
| § 103 | dg1 | Execution, acknowledgment, filing, recording and effective date of original certificate of incorporation and other instruments; exceptions. | 85 |
| § 251 | dg6 | Merger or consolidation of domestic corporations. | 50 |
| § 204 | dg4 | Ratification of defective corporate acts and stock. | 21 |
| § 102 | dg1 | Contents of certificate of incorporation. | 20 |
| § 391 | dg11 | Amounts payable to Secretary of State upon filing certificate or other paper. | 18 |
| § 255 | dg7 | Merger or consolidation of domestic nonstock corporations. | 15 |
| § 211 | dg4 | Meetings of stockholders. | 15 |
| § 228 | dg5 | Consent of stockholders or members in lieu of meeting. | 13 |
| § 252 | dg6 | Merger or consolidation of domestic and foreign corporations; service of process upon surviving or resulting corporation. | 13 |
| § 342 | dg10 | Close corporation defined; contents of certificate of incorporation. | 13 |
| § 371 | dg10 | Definition; qualification to do business in State; procedure. | 12 |
| § 280 | dg9 | Notice to claimants; filing of claims. | 10 |
| § 278 | dg9 | Continuation of corporation after dissolution for purposes of suit and winding up affairs. | 10 |
| § 155 | dg3 | Fractions of shares. | 9 |
| § 151 | dg3 | Classes and series of stock; redemption; rights. | 8 |
| § 202 | dg3 | Restrictions on transfer and ownership of securities. | 8 |
| § 257 | dg7 | Merger or consolidation of domestic stock and nonstock corporations. | 8 |
| § 258 | dg7 | Merger or consolidation of domestic and foreign stock and nonstock corporations. | 8 |
| § 136 | dg2 | Resignation of registered agent not coupled with appointment of successor. | 7 |
| § 263 | dg8 | Merger or consolidation of domestic corporations and partnerships; service of process upon surviving or resulting corporation or partnership. | 7 |
| § 215 | dg4 | Voting rights of members of nonstock corporations; quorum; proxies. | 7 |
| § 203 | dg3 | Business combinations with interested stockholders. | 7 |
| § 205 | dg4 | Proceedings regarding validity of defective corporate acts and stock. | 7 |
| § 242 | dg5 | Amendment of certificate of incorporation after receipt of payment for stock; nonstock corporations. | 7 |
| § 262 | dg7 | Appraisal rights. | 7 |
| § 275 | dg9 | Dissolution generally; procedure. | 7 |
| § 131 | dg2 | Registered office in State. | 6 |
| § 267 | dg8 | Merger of parent entity and subsidiary corporation or corporations. | 6 |
| § 116 | dg1 | Document form, signature and delivery. | 6 |
| § 212 | dg4 | Voting rights of stockholders; proxies; limitations. | 6 |

### Section 114: where the stockholder-to-member reading does not apply

Section 114(a) reads references to stockholders, the board, directors and stock in the way it specifies for a nonstock corporation, "except as otherwise provided in subsections (b) and (c)". Subsection (b) lists the sections and subchapters to which (a) "shall not apply" (for a nonstock corporation); subsection (c) lists further ones for a nonprofit nonstock corporation. The lists in (b)(1), (b)(2), (c)(2) and (c)(3), sorted into the pieces (the (b)(1) sections are "sections ... which apply to nonstock corporations by their terms"; the (b)(2) sections are listed without that gloss; 8 Del. C. §§ 503 and 502(a)(5) in the lists belong to chapter 5, which is not deposited):

| piece | the sections of your range that § 114(b) or (c) takes out of the § 114(a) reading |
| --- | --- |
| dg1 | (b)(1): 102(a)(4), 102(b)(1) and (2), 109(a), 114. (b)(2): 102(f), 109(b) (last sentence). (c)(2): 102(b)(3), 111(a)(2) and (3). |
| dg2 | (b)(1): 141. (c)(2): 144(a)(2). |
| dg3 | (b)(1): 154. (b)(2): 151, 152, 153, 155, 156, 157(e), 158, 161, 162, 163, 164, 165, 166, 167, 168, 203. (c)(3): Subchapter V (151 to 174) and Subchapter VI other than 204 and 205 (so 201 to 203). |
| dg4 | (b)(1): 215. (b)(2): 211, 212, 213, 214, 216, 219. (c)(2): 217, 218(a) and (b). Sections 204 and 205 are carved out of the (c)(3) exclusion of Subchapter VI. |
| dg5 | (b)(1): 228, 230(b), 241, 242. (b)(2): 222, 231, 243, 244. |
| dg6 | (b)(1): 253, 254. (b)(2): 251, 252. |
| dg7 | (b)(1): 255, 256, 257, 258. (c)(2): 262. |
| dg8 | (b)(2): 267. |
| dg9 | (b)(1): 271, 276, 311, 312, 313. (b)(2): 274, 275. |
| dg10 | (b)(2): 324, 364, 366(a). (b)(3): Subchapter XIV (341 to 356) and Subchapter XVI (371 to 385). (c)(3): Subchapter XV (361 to 368). |
| dg11 | (b)(1): 390. (b)(2): 391. |

### Heading notes

The 19 section headings that carry a bracketed application note (the two `[Reserved.]` headings are separate):

- § 110 (dg1, src:145): [For application of this section, see 82 Del. Laws, c. 256, § 23]
- § 111 (dg1, src:160): [For application of this section, see 80 Del. Laws, c. 265, § 17]
- § 122 (dg2, src:247): [For application of this section, see 84 Del. Laws, c. 309, § 6]
- § 144 (dg2, src:394): [For application of this section, see 85 Del. Laws, c. 6, § 3]
- § 147 (dg2, src:462): [For application of this section, see 84 Del. Laws, c. 309, § 6]
- § 204 (dg4, src:671): [For application of this section, see 80 Del. Laws, c. 40, § 16, and 81 Del. Laws, c. 354, § 16]
- § 205 (dg4, src:733): [For application of this section, see 80 Del. Laws, c. 40, § 16]
- § 220 (dg4, src:841): [For application of this section, see 85 Del. Laws, c. 6, § 3]
- § 228 (dg5, src:934): [For application of section, see 81 Del. Laws, c. 86, § 40]
- § 232 (dg5, src:970): [For application of this section, see 84 Del. Laws, c. 309, § 6]
- § 251 (dg6, src:1060): [For application of this section, see 79 Del. Laws, c. 327, § 8; 80 Del. Laws, c. 265, § 17; and 82 Del. Laws, c. 256, § 24]
- § 261 (dg7, src:1243): [For application of this section, see 84 Del. Laws, c. 309, § 6]
- § 262 (dg7, src:1251): [For application of this section, see 81 Del. Laws, c. 354, § 17; 82 Del. Laws, c. 45, § 23; 82 Del. Laws, c. 256, § 24; 83 Del. Laws, c. 377, § 22; and 84 Del. Laws, c. 98, § 16]
- § 265 (dg8, src:1327): [For application of this section, see 84 Del. Laws, c. 98, § 17]
- § 266 (dg8, src:1349): [For application of this section, see 84 Del. Laws, c. 98, § 16]
- § 268 (dg8, src:1382): [For application of this section, see 84 Del. Laws, c. 309, § 6]
- § 363 (dg10, src:1795): [For application of this section, see 82 Del. Laws, c. 256, § 24]
- § 388 (dg11, src:1937): [For application of section, see 83 Del. Laws, c. 377, § 24]
- § 390 (dg11, src:2003): [For application of this section, see 84 Del. Laws, c. 98, § 18]

### Absolute dates in the text

Outside the `History:` lines (dates of acts, such as "April 18, 1945", are not commencement rules; carry only those a rule of yours depends on):

- dg1: July 3, 1967 (§ 102, src:54); August 1, 2011 (§ 103, src:111)
- dg2: April 18, 1945 (§ 125, src:281); January 1, 2007 (§ 132, src:336); July 1, 1996 (§ 141, src:365); December 31, 2020 (§ 145, src:438)
- dg3: February 2, 1988 (§ 203, src:642); December 23, 1987 (§ 203, src:659)
- dg8: August 1, 2022 (§ 266, src:1368)
- dg9: August 1, 2023 (§ 272, src:1400)
- dg11: August 1, 2023 (§ 390, src:2023)

### Statutes and rules outside the inputs

Found by searching the text for "Title N", "U.S.C.", "CFR" and "chapter N of this title" (the search is a pattern, the text is the authority). Each is an input in the piece that cites it.

| source | cited in (piece: src line) |
| --- | --- |
| 8 Del. C. ch. 5 (§§ 501, 502, 503, 510; the franchise tax) | dg1: 42, 195; dg2: 311, 356; dg9: 1618, 1624, 1626; dg11: 2037, 2053, 2078 |
| Title 6 (including 6 Del. C. § 8-102, § 1-201(b), ch. 12A, Article 8) | dg1: 228; dg3: 524, 614; dg5: 911; dg9: 1397, 1399; dg10: 1649 |
| Title 10 (§§ 3114(b), 3111, 301) | dg1: 67, 97; dg2: 438; dg10: 1637 |
| Title 29 (§§ 2315, 2318) | dg11: 1992, 2057, 2067 |
| Titles 5, 14, 18, 26 | dg1: 37, 146, 157 (Titles 26, 5); dg2: 281 (Title 14), 447, 451 (Title 18); dg10: 1900 (Title 5) |
| Securities Exchange Act of 1934, Securities Act of 1933, Investment Company Act (15 U.S.C.) | dg1: 157; dg2: 429; dg3: 470; dg4: 713; dg5: 940, 1022; dg10: 1691, 1792 |
| Internal Revenue Code (26 U.S.C.), including § 501(c)(3) | dg1: 209; dg2: 291; dg3: 628, 630 |
| Bank holding company and savings and loan statutes (12 U.S.C. §§ 1841, 1467a) | dg1: 42; dg11: 2092 to 2097 |
| Bankruptcy Code (11 U.S.C. § 101) | dg9: 1574, 1575, 1577 |
| 17 CFR § 240.13e-3(a) (Rule 13e-3 transaction) | dg2: 429 |
| Electronic Signatures in Global and National Commerce Act (15 U.S.C. § 7001 et seq.) | dg1: 238 |
| Uniform Commercial Code; Rules of the Court of Chancery; Freedom of Information Act | dg9: one each; dg11: FOIA one |

## Coverage table

The keel has no range: the brief gives it "no provisions of its own" (lines: none, words: 0), because the Law has no interpretation section and its definitions sit inside the sections that need them.
So there are no headings in the keel's range to count against rows, and no source line that a row of this table must name.
Every heading, section and line of the text belongs to one of the pieces dg1 to dg11, whose own coverage tables must name them (the section-to-piece table under "Instructions to the pieces" is the allocation).
"Out of the seat's scope" is not given as a reason for anything here; the one row says why the range is empty.

| provision | source lines | disposition | where | note |
| --- | --- | --- | --- | --- |
| none: the keel's range is empty (the Law has no interpretation section) | none | inert | `dg-core.l4` carries the shared vocabulary, which is not a provision of the text | Counts: 0 provisions, 0 headings, 0 non-blank lines in the range; dispositions: 0 `encoded`, 0 `inert` provision rows, 0 `repealed or blank in this text`, 0 `fork` (the forks are in the register below, as design choices, not as provisions). |

## Fork register

Design choices taken in the core, the readings, and the text that licenses each.
There are none that bear on the keel's range, because it has none; these are choices about the shared vocabulary.

| fork | readings | taken, and why | text |
| --- | --- | --- | --- |
| **F1. One superset of entity kinds** | Each section that defines "person", "entity", "other entity", "non-United States entity" or "joint-stock association" does so in different words, each for its own section (§ 203(c) and § 251(h)(6) say "as used in this section only"; § 203(c)(6), § 251(h)(6)e., § 254(a), § 263(a), § 264(a), § 265(a), § 267(d)(2), § 388(a)(2)). (a) Each piece declares its own enumeration of entity kinds. (b) The core declares one superset, `Kind of entity`, and each piece writes its section's definition as a predicate over it. Three of the definitions of "person" begin "any individual", so the superset has `a natural person` as a constructor of its own. | (b). One namespace, so the pieces can be composed and a seat layer can pass one entity through several sections. Cost: a piece's predicate must say which constructors its definition leaves out, and an Entity record is not built for a natural person (`where formed` does not apply). | § 203(c)(6), § 251(h)(6)e., § 254(a), § 263(a), § 264(a), § 265(a), § 267(d)(2), § 388(a)(2) |
| **F2. Months and years clamp** | Six months before 31 August, or three years after 29 February: (a) clamp to the last day of the target month (28 February), as the library's `add months` and `add years` do; (b) roll forward to the 1st of the next month. The text does not say. | (a), because it is what the library's `add months` and `add years` do (measured on this build: 31 August plus 6 months is 28 February; 29 February plus 3 years is 28 February) and the text gives no other rule. A piece whose provision depends on the day must record its own reading. | § 371(b)(1) ("not earlier than 6 months prior to the filing date"), § 212(b) ("3 years from its date") |
| **F3. Counting "N days after D"** | D plus N is the last day inside the period (inclusive), or D plus N is the first day outside it. | The core only does the arithmetic (D plus N). Inclusive is the recommended reading for "within", "not more than", "not less than" and "at least" (the writing skill measures a regulative `WITHIN 30` as timely on day 30, entry 4.3; not re-measured here); each piece records the reading it takes where a provision turns on the last day. | § 213(a) ("not more than 60 nor less than 10 days before the date of such meeting") |
| **F4. "A majority" is more than half** | "A majority" as more than half of the base, or as half or more. "At least", "no less than" and "not less than" reach the proportion. | More than half for "a majority" (`must be exceeded` TRUE); reaching for "at least" and "no less than" (`must be exceeded` FALSE). The Law does not define "majority". | § 216 ("no less than 1/3"; "the majority of shares present"), § 203(a)(3) ("at least 66 2/3%"), § 242(b)(1) ("a majority of the outstanding stock") |
| **F5. Votes, not shares** | Counts of the base and of the votes in favor are (a) numbers of shares, (b) numbers of votes. | (b): where the certificate gives more or less than one vote per share, § 212(a) says every reference to a majority or other proportion of stock refers to the votes of that stock. | § 212(a) |
| **F6. Counts that cannot be a vote** | A base of 0 or less, or votes in favor below 0 or above the base: (a) FALSE; (b) not covered. | (b): `the vote carries` is `MAYBE BOOLEAN` and answers `NOTHING`. Never FALSE for a case the source does not answer. | the brief; § 216, § 203(a)(3) |
| **F7. Kind of corporation as four leaves** | Section 114(d) defines nonstock, nonprofit nonstock and charitable nonstock corporations by nesting. (a) Three BOOLEAN flags on a case record. (b) One enumeration of the four mutually exclusive kinds the definitions produce, with predicates. | (b). The four are: stock (not nonstock); nonstock with membership interests; nonprofit nonstock and not charitable; charitable. They partition the corporations organized under the chapter, and a flag combination such as "charitable but not nonprofit" is unwritable. The definitions that decide the kind stay with dg1. | § 114(d)(1) to (4) |
| **F8. One closed cast of parties** | A rule has one party type. (a) Each piece declares its own cast. (b) The core offers one `Actor` with the 18 parties that two or more pieces name, and a constructor `another party named in the provision` for the rest. | (b). Parties are constructors, not strings; the escape carries the text's own words, and two spellings are two parties, so it is for rare parties only. The Secretary of State, the Court of Chancery and the Attorney General are constructors so that a rule can say who does an act, but none has a seat. | § 107, § 124(3), § 132(a), § 141(a), § 142(a), § 145(a), § 165, § 211(a)(2), § 212(b), § 226(a), § 231(a), § 279, § 291, § 103(a), § 114(a)(1) |
| **F9. A trustee is one constructor** | `a trustee` could be split into the trustee of a voting trust (§ 218) and the trustee of a dissolved corporation (§ 279). | One constructor; the rule's name says which. The core does not tell them apart because no rule needs the difference to compose. | § 218, § 279 |
| **F10. Where a provision is made carries no content** | `Where a provision is made` could carry the provision's value (a number of directors, a quorum). | It carries only where the provision sits; the value is a separate input of the piece's own type, because the values differ in kind from section to section. | § 141(b), § 216, § 151(a) |
| **F11. A time limit is a Period, not a number of days** | The build's `WITHIN` takes a bare number of days with no unit. The Law also counts in weeks, months and years. | A `Period` with a unit, and date arithmetic. `WITHIN` stays available for a duty with a consequence whose limit is in days. | § 213(a), § 164, § 371(b)(1), § 212(b) |
| **F12. `YMD` lives in the core** | Each module adds its own `YMD` shim, or the core defines it once. | Once, in the core. Two definitions of one name make the name unusable, and eleven pieces would each have added one. | dialects.md; probe 05 on this binary |
| **F13. Nonstock corporations use the same vote bases** | A separate set of bases for members and the governing body, or the stockholder-to-member reading of § 114(a). | The reading: `the outstanding stock entitled to vote` stands for the members entitled to vote, `the whole board` for the governing body, as § 114(a) reads them. | § 114(a)(1) to (4) |
| **F14. The "facts" sentence and the application notes are inert** | The "facts" sentence (18 places) could be encoded as a rule on what a provision may depend on; the 19 bracketed application notes could be carried as dates. | Inert, with reasons. The sentence enlarges what an instrument may refer to and no case fact answers it; the notes point to session-law clauses that are not in the text. | § 102(d) and 17 other places (Defined terms); the 19 headings listed under Instructions |
| **F15. The keel's range is empty** | Treat the title block or the subchapter headings as the keel's range, so that the coverage table has rows. | No. The brief gives the keel "no provisions of its own" and lines "none"; the title block and the subchapter headings belong to the pieces that follow them (dg1 owns lines 1 to 239). | the brief |

Where I looked for more and found none: a definition of "majority" (no quoted term "majority" in the text), and a general rule on how a period of days is counted (a search of the text for "compute", "legal holiday", "Saturday", "business day", "calendar day", "first day" and "last day" finds only incidental uses). The Law carries no commencement rule among its definitions; the dates it names are listed under Instructions.

## What the stable binary does not accept

The binary is `1.6.98 (main, 7689b0d, 2026-10-19)` (`l4 --version`), sha256 `82ea44addf093ea4dd84c4e4416184920857ca9c762c5b31feed20541c20263e` (`shasum -a 256`), as the brief names it.
Measured on 2026-10-25 by running it over the files in the writing skill's `references/dialect-probes/`:

- **All 58 numbered probes (`01` to `58`) are rejected**: each produces at least one `DiagnosticSeverity_Error` under `l4 check`. That agrees with the "Status on main" tables of `dialects.md`, which say `main` rejects exactly these.
- **All 23 `alt-*` probes check clean** (no error): the spellings `dialects.md` gives as "write instead" work on this build.
- **`YMD` is missing.** `#CHECK YMD` after `IMPORT prelude` and `IMPORT daydate` gives "I could not find a definition for the identifier YMD". The core defines it: `YMD y m d MEANS Date d m y`.

The numbered probes, by cause, with what to write instead (from `dialects.md`; the probe numbers are the file names `NN-*.l4`):

| what the build refuses | probes | write instead |
| --- | --- | --- |
| A section `GIVEN` (a `GIVEN` indented under a `§` heading) | 06 to 12 | A `GIVEN` on every rule that reads the input; a record parameter for several facts |
| `@lang`, `@infixl`/`@infixr`/`@infix`, `@nonassertable`, `@nonexhaustive`, any unknown `@word` | 01, 45 to 48 | Leave them out; bracket operator chains by hand. `@export`, `@desc`, `@nlg` (untagged), `@ref`, `@ref-map`, `@ref-src` are fine |
| `REFUSE`, `#ASSERT REFUSED`, `BECAUSE` after it | 02 to 04 | `MAYBE T` with `NOTHING`, and `#ASSERT e EQUALS NOTHING`; put the reason in a comment |
| `TYPICALLY` on a field or a `GIVEN` | 13 to 16 | Leave it out; put the presumed value in the `@desc` |
| A `DECLARE` with no body (an opaque type) | 17 | Give it one field |
| Sets: `SET OF`, `setFromList`, `setSize`, `is in`, `UNION` | 18 to 22 | `LIST OF` and `elem` |
| The ledger: `RECORD`, `COMMIT`, `ATTEST`, `RECALL` | 23 to 27, 52 | Pass the facts in as inputs |
| `EVERY`, `WHOSE` | 28 to 30 | One obligation for one named party: the party as an input, `PARTY t`, a `PROVIDED` guard |
| `WITHIN n OF THE DEADLINE`, `OF THE JOIN` | 31 | `WITHIN n` (it counts from entry: say so in a comment) |
| `AFTER 3 WITHIN 30`, `AFTER 3 BEFORE d` | 32, 33 | Nothing: compare dates |
| `BREACH BY LIST a, b` | 34 | `BREACH BY` one party, or `BREACH BECAUSE "..."` |
| The same name defined in two nested `§` sections | 35 | Give them different names |
| `RULES EFFECTIVE DATE` (compared, or bare); `EVAL UNDER VALID TIME`, `EVAL AS OF SYSTEM TIME`, `EVAL UNDER RULES EFFECTIVE AT`; `VALUE AT`; `EVER BETWEEN` | 36 to 40, 57, 58 | Take the rule-version date as an input of the rule |
| `YMD` (the build has none); a library-`YMD` date compared (`__GEQ__` reported) | 05, 53 | The core's `YMD` for literals; dates made with it compare with `AT LEAST`, `AT MOST`, `GREATER THAN` and `LESS THAN` (asserted in `dg-core-tests-core.l4`) |
| A rule applied inside `MUST (...)` | 42 | Write the constructor |
| An input named in an action, read again in `HENCE` | 43 | `MUST Pay Borrower payee 10 PROVIDED payee EQUALS creditor` |
| A rule whose `GIVEN` is a record reads a field bare (field opening) | 41 | Name the input: `` person's `the age` `` |
| A field read in an action's argument | 51 | A `PROVIDED` guard |
| `\[` or `\]` inside an inline `[...]` annotation | 44 | No bracket inside an inline annotation |
| `IMPORT hierarchy`, ``IMPORT `negation-as-failure` `` | 49, 50 | Nothing; the other libraries import |
| `IS INTEGER`; ``(`WAIT UNTIL` 8)``; `MUST DO` | 54 to 56 | `FLOOR x EQUALS x`; `WAITUNTIL` or an event by another party; `MUST` |

Constructs the core uses, and this build reads (all in `dg-core.l4`, checked clean, and exercised by the assertions in `dg-core-tests-core.l4`):

- records built with `WITH`, one field per line led by a comma; an enumeration constructor that carries a field (`a corporation` with `its kind`; `another party named in the provision` with a STRING); `CONSIDER` on a field with `OTHERWISE`;
- `DATE PLUS` and `DATE MINUS` a NUMBER of days; `` `add months` `` and `` `add years` `` with a negative count (to go backward); month-end clamping (31 August less 6 months is 28 February; 29 February plus 3 years is 28 February);
- the postfix `%` on a bracketed expression: `(200 DIVIDED BY 3)%` equals `2 DIVIDED BY 3` exactly;
- a `MAYBE BOOLEAN` result compared with `EQUALS JUST TRUE`, `EQUALS JUST FALSE` and `EQUALS NOTHING`;
- `§` headings with no `GIVEN` beneath them, and backticked names that contain parentheses and digits.

Differences between this build and `unstable` that `check.sh` cannot see (from `dialects.md`, not re-measured here; they matter only to regulative rules):

- An input named in a `MUST` action matches any payload on this build, so paying a stranger fulfils the obligation. Compare in a `PROVIDED` guard.
- A `MAY` with a `LEST` lapses to FULFILLED here, to BREACH on `unstable`. If inaction should be a breach, make it a `MUST`.
- An actor may perform another's action without a diagnostic here: check the `PARTY` by eye.
- `NOT a AND b` on one line reads as `NOT (a AND b)`: always write the brackets.

## What check.sh prints

Run in this folder as `L4=<L4_BIN> L4_TARGET=unstable ./check.sh` (exit status 0); the binary is itself a `main` build, so there is no second build to compare, and the target check is skipped, as the brief directs.

```
module                                    errors satisfied  failed  refused  expected
dg-core-tests-core.l4                          0        87       0        0         0
dg-core.l4                                     0         0       0        0         0
TOTAL (2 modules)                              0        87       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
```

The same run on stderr: `check.sh: the target is unstable, so the main check was skipped.`

`python3 -I srcrefs.py check --refs <INPUTS_DIR>/de-code-t8-ch1-2026-10-01.txt dg-core.l4 dg-core-tests-core.l4` (exit status 0) printed:

```
srcrefs check: 41 src: lines, 8 runs, 68 locators, 0 problems
```

`l4 check` on each of the two modules prints `Check succeeded.`; neither prints a warning (no `follows code on its line` or `end of the file` notice, no `Unknown annotation`).
