# NOTES -- the Canada Business Corporations Act (R.S.C. 1985, c. C-44): the keel

Written on 2026-10-22 by the keel agent cbca-g0, for the five part agents cb1 to cb5, who import the modules named here and take their facts about the whole Act from this file.
Status, and how it was checked: the four modules and four test files in this folder compile and every assertion in them is satisfied under the stable binary `l4` 1.6.98 (main, 7689b0d, 2026-10-19); the numbers are printed under "What check.sh prints", from a run made when this file was generated.
Nothing here has been checked against the official text of the Act.

The text is `R.S.C.-1985-c.-C-44.txt`: a plain-text rendering, made by a converter script, of the Department of Justice Canada consolidation current to 2026-09-30 (last amended 2026-03-26), English version only.
It is not the official text and it is not marked up.
The French version is equally authoritative and was not read.
Contains information licensed under the Open Government Licence - Canada.
`src:N` in this folder means line N of that text file.

The keel is eight files, all flat in this folder:

| file | what it holds | imports |
| --- | --- | --- |
| `cbca-core.l4` | the shared vocabulary: kinds of person, parties, offices, kinds of articles, provinces, resolutions and votes, a block of shares, time limits, the `YMD` shim | `prelude`, `daydate` |
| `cbca-core-definitions.l4` | s 2(1) (the definitions), s 2(6) and (7) (the Director's determinations), s 2(8) (infants) | `prelude`, `cbca-core` |
| `cbca-core-control.l4` | s 2(2) to (5): affiliated, control, holding body corporate, subsidiary | `prelude`, `cbca-core` |
| `cbca-core-isc.l4` | s 2.1: individuals with significant control | `prelude`, `cbca-core` |
| `cbca-core-tests-core.l4`, `cbca-core-tests-definitions.l4`, `cbca-core-tests-control.l4`, `cbca-core-tests-isc.l4` | the tests of each module, expected values written from the text | the module they test |

**Dates.**
My range (lines 13-114: the Part I heading, s 2 and s 2.1) holds no date of enactment, assent or commencement, and no commencement rule, so no date is encoded and no keel rule depends on one.
The one date in the range is 20 November 1989 (s 2(8), src:97), which dates the United Nations Convention on the Rights of the Child, not this Act, and is not carried as a value.
Any enactment or commencement date belongs to cb1 (title block, lines 1-12) and cb5 (the Related Provisions, from line 3543).

**Reading order for a piece.**
Read "Instructions to the pieces" first, then "Naming conventions", then look your terms up in "Defined terms".

## Vocabulary

Every type, enumeration constructor and rule in `cbca-core.l4`.
A record is one row; its fields are listed in its "what it is" cell.
The row for a constructor names its enumeration in "kind".
The types that only one other keel module needs are not in the core; they are in the second table below.

| name | kind | what it is | licensed by |
| --- | --- | --- | --- |
| `Kind of person or entity` | enumeration | The kinds of person and entity the Act names, in one enumeration because the two definitions overlap. | s 2(1) "person" (src:56), "entity" (src:46) |
| `an individual` | constructor of `Kind of person or entity` | A natural person. | s 2(1) "individual" (src:50), "person" (src:56) |
| `a partnership` | constructor of `Kind of person or entity` | A partnership. | s 2(1) "person" (src:56), "entity" (src:46) |
| `an association` | constructor of `Kind of person or entity` | An association; kept apart from the unincorporated association or organization of "entity" (fork F4). | s 2(1) "person" (src:56) |
| `a body corporate` | constructor of `Kind of person or entity` | A body corporate, wherever or however incorporated. | s 2(1) "body corporate" (src:31), "entity" (src:46), "person" (src:56) |
| `a personal representative` | constructor of `Kind of person or entity` | A personal representative. | s 2(1) "person" (src:56), "personal representative" (src:57) |
| `a trust` | constructor of `Kind of person or entity` | A trust. | s 2(1) "entity" (src:46) |
| `a joint venture` | constructor of `Kind of person or entity` | A joint venture. | s 2(1) "entity" (src:46) |
| `an unincorporated association or organization` | constructor of `Kind of person or entity` | An unincorporated association or organization. | s 2(1) "entity" (src:46) |
| `Party` | enumeration | The parties the Act gives powers or duties to; the PARTY of a regulative rule. | s 2(1) and the Parts named in the rows below |
| `the corporation` | constructor of `Party` | The corporation the rule is about. | s 2(1) "corporation" (src:33) |
| `an incorporator` | constructor of `Party` | A person who signs articles of incorporation. | s 2(1) "incorporator" (src:49) |
| `a director` | constructor of `Party` | A person occupying the position of director. | s 2(1) "director" (src:44) |
| `an officer` | constructor of `Party` | An officer. | s 2(1) "officer" (src:54) |
| `a shareholder` | constructor of `Party` | A shareholder (s 226(1), src:2830, only widens the word for Part XVIII). | not defined in s 2; first used at src:159 (s 6, Part II) and throughout |
| `a security holder` | constructor of `Party` | A holder of a security. | not defined in s 2; first used at src:739 (s 49, Part VII) |
| `a creditor` | constructor of `Party` | A creditor. | not defined in s 2; first used at src:272 (s 21, Part IV) |
| `the auditor` | constructor of `Party` | The corporation's auditor. | s 2(1) "auditor" (src:28) |
| `a trustee under a trust indenture` | constructor of `Party` | A trustee under a trust indenture (Part VIII). | s 82(1) "trustee" (src:1096), Part VIII |
| `a receiver or receiver-manager` | constructor of `Party` | A receiver or receiver-manager (Part IX). | Part IX heading (src:1168) |
| `a liquidator` | constructor of `Party` | A liquidator. | not defined in s 2; first used at src:825 (s 51, Part VII) and in Part XVIII |
| `a proxyholder` | constructor of `Party` | A proxyholder. | not defined in s 2; first used at src:1757 (s 141, Part XII) and in Part XIII |
| `an insider` | constructor of `Party` | An insider (Part XI); each piece defines which sense it needs. | s 126(1) "insider" (src:1555-1559) and s 131(1) (src:1584), Part XI |
| `an offeror` | constructor of `Party` | An offeror under a take-over bid. | s 206(1) "offeror" (src:2501), Part XVII |
| `a complainant` | constructor of `Party` | A complainant in a remedy proceeding. | s 238 "complainant" (src:3016), Part XX |
| `the Director` | constructor of `Party` | The Director appointed under s 260 (cb5). | s 2(1) "Director" (src:43) |
| `the Minister` | constructor of `Party` | The Minister designated by the Governor in Council. | s 2(1) "Minister" (src:53) |
| `the court` | constructor of `Party` | The court (which court is `court within s 2(1)`). | s 2(1) "court" (src:34-40) |
| `any person` | constructor of `Party` | Anyone: the party of a duty or permission that falls on every person. | s 2(1) "person" (src:56) |
| `Office` | enumeration | The offices in the definition of "officer", and the two ends of it. | s 2(1) "officer" (src:54) |
| `an officer appointed under section 121` | constructor of `Office` | An individual appointed as an officer under s 121. | src:54 |
| `the chairperson of the board of directors` | constructor of `Office` | The chairperson of the board of directors. | src:54 |
| `the president` | constructor of `Office` | The president. | src:54 |
| `a vice-president` | constructor of `Office` | A vice-president. | src:54 |
| `the secretary` | constructor of `Office` | The secretary. | src:54 |
| `the treasurer` | constructor of `Office` | The treasurer. | src:54 |
| `the comptroller` | constructor of `Office` | The comptroller. | src:54 |
| `the general counsel` | constructor of `Office` | The general counsel. | src:54 |
| `the general manager` | constructor of `Office` | The general manager. | src:54 |
| `a managing director` | constructor of `Office` | A managing director. | src:54 |
| `another individual performing functions similar to those of one of these offices` | constructor of `Office` | Any other individual who performs functions similar to those normally performed by the holder of one of these offices. | src:54 |
| `holds no office and performs no similar function` | constructor of `Office` | The answer that the individual is not an officer. | src:54 (the negative case) |
| `Kind of articles` | enumeration | The nine kinds of articles the definition lists. | s 2(1) "articles" (src:20) |
| `the original articles of incorporation` | constructor of `Kind of articles` | The original articles of incorporation. | s 2(1) "articles" (src:20) |
| `restated articles of incorporation` | constructor of `Kind of articles` | Restated articles of incorporation. | s 2(1) "articles" (src:20) |
| `articles of amendment` | constructor of `Kind of articles` | Articles of amendment. | s 2(1) "articles" (src:20) |
| `articles of amalgamation` | constructor of `Kind of articles` | Articles of amalgamation. | s 2(1) "articles" (src:20) |
| `articles of continuance` | constructor of `Kind of articles` | Articles of continuance. | s 2(1) "articles" (src:20) |
| `articles of reorganization` | constructor of `Kind of articles` | Articles of reorganization. | s 2(1) "articles" (src:20) |
| `articles of arrangement` | constructor of `Kind of articles` | Articles of arrangement. | s 2(1) "articles" (src:20) |
| `articles of dissolution` | constructor of `Kind of articles` | Articles of dissolution. | s 2(1) "articles" (src:20) |
| `articles of revival` | constructor of `Kind of articles` | Articles of revival. | s 2(1) "articles" (src:20) |
| `Province or territory` | enumeration | The thirteen provinces and territories the definition of "court" names. | s 2(1) "court" (src:34-40) |
| `Newfoundland and Labrador` | constructor of `Province or territory` | Newfoundland and Labrador. | s 2(1) "court" (src:34-40) |
| `Prince Edward Island` | constructor of `Province or territory` | Prince Edward Island. | s 2(1) "court" (src:34-40) |
| `Nova Scotia` | constructor of `Province or territory` | Nova Scotia. | s 2(1) "court" (src:34-40) |
| `New Brunswick` | constructor of `Province or territory` | New Brunswick. | s 2(1) "court" (src:34-40) |
| `Quebec` | constructor of `Province or territory` | Quebec. | s 2(1) "court" (src:34-40) |
| `Ontario` | constructor of `Province or territory` | Ontario. | s 2(1) "court" (src:34-40) |
| `Manitoba` | constructor of `Province or territory` | Manitoba. | s 2(1) "court" (src:34-40) |
| `Saskatchewan` | constructor of `Province or territory` | Saskatchewan. | s 2(1) "court" (src:34-40) |
| `Alberta` | constructor of `Province or territory` | Alberta. | s 2(1) "court" (src:34-40) |
| `British Columbia` | constructor of `Province or territory` | British Columbia. | s 2(1) "court" (src:34-40) |
| `Yukon` | constructor of `Province or territory` | Yukon. | s 2(1) "court" (src:34-40) |
| `Northwest Territories` | constructor of `Province or territory` | Northwest Territories. | s 2(1) "court" (src:34-40) |
| `Nunavut` | constructor of `Province or territory` | Nunavut. | s 2(1) "court" (src:34-40) |
| `Kind of resolution` | enumeration | Which of the two resolutions a rule asks for. | s 2(1) "ordinary resolution" (src:55), "special resolution" (src:72) |
| `an ordinary resolution` | constructor of `Kind of resolution` | A resolution passed by a majority of the votes cast. | src:55 |
| `a special resolution` | constructor of `Kind of resolution` | A resolution passed by two-thirds of the votes cast, or signed by all the shareholders entitled to vote. | src:72 |
| `Vote tally` | record | The votes on one resolution: votes cast in favour, votes cast against, and whether it was signed by all the shareholders entitled to vote. Fields: `votes cast in favour` (NUMBER); `votes cast against` (NUMBER); `signed by all the shareholders entitled to vote on the resolution` (BOOLEAN). | s 2(1) "ordinary resolution" (src:55), "special resolution" (src:72) |
| `Block of shares` | record | Shares measured both ways the Act measures them: the votes they carry and their fair market value in dollars. Fields: `votes carried` (NUMBER); `fair market value in dollars` (NUMBER). | s 2.1(3) "significant number of shares" (src:112-113) |
| `Unit of time` | enumeration | The unit of a time limit. | convention (fork F1); no provision of the range |
| `calendar days` | constructor of `Unit of time` | Days, counted on the calendar. | convention (fork F1) |
| `calendar weeks` | constructor of `Unit of time` | Weeks of seven days. | convention (fork F1) |
| `calendar months` | constructor of `Unit of time` | Months, clamped to the last day of a shorter month. | convention (fork F1) |
| `calendar years` | constructor of `Unit of time` | Years, clamped to the last day of a shorter month. | convention (fork F1) |
| `Time limit` | record | A number of units and a unit: the one way a time limit is written in the encoding. Fields: `number of units` (NUMBER); `unit of time` (`Unit of time`). | convention (fork F1); no provision of the range |
| `` `the last day of` limit `counted from` start `` | rule | The last day of a time limit that starts on a date; months and years clamp to the last day of a shorter month. | convention (fork F1) |
| `` `the earliest day allowed by` limit `counted back from` `the later date` `` | rule | The earliest day allowed by a time limit counted back from a later date. | convention (fork F1) |
| `` `done within the time limit` limit start act `` | rule | TRUE when an act on a date is not before the start and not after the last day. | convention (fork F1) |
| `` YMD y m d `` | rule | The shim for the missing stable-prelude YMD: year, month, day to a DATE. Only the core defines it. | brief ("YMD is missing from the stable prelude") |

### Types declared in the other keel modules

These are used by one keel module only, so they are not in the core; a piece that needs one imports that module.

| name | module | what it is | licensed by |
| --- | --- | --- | --- |
| `Relationship of another to a person` | `cbca-core-definitions.l4` | The facts about another party that "associate" asks of the person it is in respect of. Fields: `a body corporate` (BOOLEAN); `fraction of the voting rights in it that the person beneficially owns or controls` (NUMBER); `a partner of the person acting on behalf of the partnership` (BOOLEAN); `a trust or estate or succession in which the person has a substantial beneficial interest` (BOOLEAN); `a trust or estate or succession in respect of which the person serves as trustee, liquidator of the succession or in a similar capacity` (BOOLEAN); `a spouse of the person` (BOOLEAN); `an individual cohabiting with the person in a conjugal relationship` (BOOLEAN); `years of that cohabitation` (NUMBER); `a child of the person` (BOOLEAN); `a child of the spouse or of the individual referred to in paragraph (d)` (BOOLEAN); `a relative of the person` (BOOLEAN); `a relative of the spouse or of the individual referred to in paragraph (d)` (BOOLEAN); `having the same residence as the person` (BOOLEAN). | s 2(1) "associate" (src:21-27) |
| `Terms of an option` | `cbca-core-definitions.l4` | The terms of an option, for "call" and "put". Fields: `transferable by delivery` (BOOLEAN); `for a specified number or amount of securities` (BOOLEAN); `at a fixed price` (BOOLEAN); `within a specified time` (BOOLEAN); `to demand delivery of the securities` (BOOLEAN); `to deliver the securities` (BOOLEAN); `an option or right to acquire securities of the corporation that granted it` (BOOLEAN). | s 2(1) "call" (src:32), "put" (src:60) |
| `Court` | `cbca-core-definitions.l4` | The thirteen courts the definition of "court" names. Constructors: `the Trial Division of the Supreme Court of Newfoundland and Labrador`; `the Superior Court of Justice of Ontario`; `the Supreme Court of Nova Scotia`; `the Supreme Court of British Columbia`; `the Supreme Court of Prince Edward Island`; `the Court of Queen's Bench for Manitoba`; `the Court of Queen's Bench for Saskatchewan`; `the Court of Queen's Bench for Alberta`; `the Court of Queen's Bench for New Brunswick`; `the Superior Court of Quebec`; `the Supreme Court of Yukon`; `the Supreme Court of the Northwest Territories`; `the Nunavut Court of Justice`. | s 2(1) "court" (src:34-40) |
| `Kind of security` | `cbca-core-definitions.l4` | The kinds of instrument "debt obligation" and "security" list, with a "none of these" answer. Constructors: `a share of a class or series of shares`; `a bond`; `a debenture`; `a note`; `other evidence of indebtedness or guarantee`; `a certificate evidencing a share`; `a certificate evidencing a debt obligation`; `none of these kinds of instrument`. | s 2(1) "debt obligation" (src:42), "security" (src:68) |
| `Determination about distributing status` | `cbca-core-definitions.l4` | The Director's determination about whether a corporation is a distributing corporation. Fields: `made on the application of the corporation` (BOOLEAN); `made for a class of corporations that includes the corporation` (BOOLEAN); `the Director was satisfied that it would not be prejudicial to the public interest` (BOOLEAN); `the Director determined that the corporation is not or was not a distributing corporation` (BOOLEAN). | s 2(6) (src:93), s 2(7) (src:95) |
| `Holding in a body corporate` | `cbca-core-control.l4` | One body corporate and the votes held in it to elect directors; a list of these is the control graph. Fields: `the body corporate` (STRING); `the persons holding` (LIST OF STRING); `the persons holding are bodies corporate` (BOOLEAN); `fraction of the votes to elect directors held, other than by way of security only` (NUMBER); `the votes held are sufficient, if exercised, to elect a majority of the directors` (BOOLEAN). | s 2(3) "control" (src:80-82) |

## Naming conventions

One line each.
The keel modules follow every one, so they are the examples.

- **A rule** is named `` `<what it works out> within s N` ``, where `s N` is the provision it encodes written as the Act writes it (`s 2(1)`, `s 2.1(3)(a)`, `s 82(1)`).
  A definition is named for the term: `` `special resolution within s 2(1)` ``.
  A decision is named for what is decided: `` `the Director may determine on application within s 2(6)` ``.
  The suffix is what keeps two definitions of one word apart (the Act defines "officer", "insider", "share", "security" and "court" more than once).
- **A helper rule** that encodes no provision of its own is named for what it computes and carries no suffix: `` `the bodies corporate above directly` ``.
  It still carries the `@ref` of the provision it serves, marked `helper` in the annotation text (`@ref CBCA s 2(3) control, helper (src:80-82)`).
  The four rules in the core encode a convention, not a provision, so they carry no `@ref`; the comments above them say what they are.
- **An input** (a `GIVEN` parameter) is a backticked phrase that reads as the fact.
  A BOOLEAN is a whole clause: `` `the transaction is by a corporation` ``.
  A NUMBER or other value is a noun phrase: `` `years of that cohabitation` ``.
  A bare one-word name is used only for the argument of a small helper (`tally`, `kind`).
- **A record field** starts at the complement, with no `is` or `has` in front: `votes carried`, `fair market value in dollars`.
  Read it with the genitive: `` tally's `votes cast in favour` ``.
- **A type** is a capitalised phrase, backticked when it has more than one word (`Vote tally`, `Block of shares`).
  An enumeration whose members are kinds starts `Kind of`.
  A type that only one piece needs is declared in that piece and carries the section in its name: `` `Stated capital account (s 26)` ``.
- **An enumeration constructor** is a specific lower-case phrase that starts with an article (`a director`, `the president`), or a proper name (`Quebec`).
  A constructor must be unique across the whole Act, because a name defined in two imported modules cannot be used at all.
  A piece-local enumeration therefore puts the section in the phrase when the generic phrase could clash (`` `a notice under section 21` ``).
- **A question** (in a seat layer; the keel writes none): `@export` carries the question in the first person with the provision in brackets and a question mark, `@desc` the plain wording of the input, and the `DECIDE` name is the same words without the question mark, as in the example seat `ea-seat.l4`.
- **Money** is a NUMBER of Canadian dollars, cents as decimals; a name that holds one ends `in dollars` (`fair market value in dollars`).
- **A fraction** is a NUMBER from 0 to 1, written with the postfix `%`: `25%` is 0.25, never 25; a name that holds one starts `fraction of`.
  In argument position write it in brackets, `(25%)`: `f 60% TRUE` is a parse error.
- **Votes and counts of shares** are NUMBERs.
  A `Block of shares` pairs the votes the shares carry with their fair market value in dollars.
- **Days** are a NUMBER of calendar days.
  **A time limit in any unit** is a `Time limit` (a number of units and a `Unit of time`), turned into a date with the core's rules.
  **A date** is built `Date day month year`, or `YMD year month day` (the core's shim, the only place `YMD` is defined).
- **A fact about something outside the piece** (another provision, the regulations, a provincial law, another Act, a judgement left to the Director or a court) is a plain input, never a guess.
  Its name says whose fact it is: `` `the Director is satisfied that the determination would not be prejudicial to the public interest` ``, `` `the individual is a member of a prescribed class of persons` ``.
  Where the Act says "prescribed", the input is `` `<the thing> is prescribed by the regulations` `` (a yes or no) or `` `the prescribed <thing>` `` (an amount, a period, a form).
- **A case the text does not answer** is a `MAYBE` with `NOTHING`, or a named constructor (`holds no office and performs no similar function`, `none of these kinds of instrument`); it is never FALSE or 0, and it is asserted.
- **A name uses a straight apostrophe** where the text has a curly one (`Queen's Bench` for "Queen’s Bench"); the quoted source lines keep the curly one.
- **Every `NOT` is parenthesised** (`(NOT x)`), because `NOT a AND b` reads as `NOT (a AND b)`.
- **A rule's parameters** are listed one per line under a single `GIVEN`, never separated by commas; a parameter that is itself a list is declared `LIST OF <type>`.

## Defined terms

Every term the text defines, in the order the text defines them.
The first 47 rows are the terms my range defines: the 40 of s 2(1), then the notions of s 2(2) to (8) and s 2.1.
The next 65 rows are the terms defined elsewhere in the Act, found by scanning the whole text for the "Definitions" headings and for "In this Part", "In this section" and "For the purposes of ..." lines that give a meaning; a piece that finds a further local definition names its rule on the same pattern.
"encoded in" gives the module and rule; "by reference: encoded by piece X, section N, taken there as an input" means the definition is outside my range, the named piece encodes it, and any other piece that needs the term takes a plain input of the name given in the note, or in the table of input names below the table.
The pieces cover these lines of the text: cb1 1-12 and 115-693; cb2 694-1549; cb3 1550-2095; cb4 2096-2861; cb5 2862-3671.
By kind, in my range: 34 terms are rules in `cbca-core-definitions.l4`, 5 in `cbca-core-control.l4` and 2 in `cbca-core-isc.l4` (41 rules for 41 terms); 2 terms (Director, Minister) are constructors of `Party` in the core; 4 terms (going-private transaction, prescribed, prior legislation, unanimous shareholder agreement) are pointers, encoded nowhere here.

| term | defined at | encoded in | note |
| --- | --- | --- | --- |
| affairs | s 2(1), src:18 | `cbca-core-definitions.l4` `affairs within s 2(1)` | Two facts: it is a relationship among the corporation, its affiliates and the shareholders, directors and officers of such bodies corporate; it is the business those bodies carry on (excluded). |
| affiliate | s 2(1), src:19 | `cbca-core-control.l4` `affiliate within s 2(1)`; `cbca-core-control.l4` `affiliate within s 2(1) by the facts` | Points to s 2(2). Gives the same answer as the rules for s 2(2); the first works from a list of holdings, the second from four facts about the pair. |
| articles | s 2(1), src:20 | `cbca-core-definitions.l4` `articles within s 2(1)`; `cbca-core.l4` `Kind of articles` | The nine kinds, and "any amendment" of them as a separate fact. A kind of articles of `NOTHING` means "not a kind named in the definition". |
| associate | s 2(1), src:21-27 | `cbca-core-definitions.l4` `associate within s 2(1)`; `cbca-core-definitions.l4` `associate within s 2(1)(a)`; `cbca-core-definitions.l4` `associate within s 2(1)(b)`; `cbca-core-definitions.l4` `associate within s 2(1)(c)`; `cbca-core-definitions.l4` `associate within s 2(1)(d)`; `cbca-core-definitions.l4` `associate within s 2(1)(e)`; `cbca-core-definitions.l4` `associate within s 2(1)(f)` | Works on one record, `Relationship of another to a person`, which holds the facts about the other party; "in respect of a relationship with a person" is who the record is about. Fork F5 for paragraph (d). |
| auditor | s 2(1), src:28 | `cbca-core-definitions.l4` `auditor within s 2(1)` | "Includes": the ordinary meaning is a plain input, plus a partnership of auditors or an auditor that is incorporated. |
| beneficial interest | s 2(1), src:29 | `cbca-core-definitions.l4` `beneficial interest within s 2(1)` | One fact: the interest arises out of the beneficial ownership of securities. |
| beneficial ownership | s 2(1), src:30 | `cbca-core-definitions.l4` `beneficial ownership within s 2(1)` | "Includes": ordinary ownership is a plain input, plus ownership through a trustee, legal representative, agent or mandatary, or other intermediary. |
| body corporate | s 2(1), src:31 | `cbca-core-definitions.l4` `body corporate within s 2(1)` | "Includes a company": a body corporate wherever or however incorporated, or a company. |
| call | s 2(1), src:32 | `cbca-core-definitions.l4` `call within s 2(1)` | Works on the record `Terms of an option`. Excludes an option or right to acquire securities of the corporation that granted it. |
| corporation | s 2(1), src:33 | `cbca-core-definitions.l4` `corporation within s 2(1)` | A body corporate incorporated or continued under this Act and not discontinued under this Act. The vocabulary constructor `the corporation` in `Party` means this. |
| court | s 2(1), src:34-40 | `cbca-core-definitions.l4` `court within s 2(1)`; `cbca-core.l4` `Province or territory` | Maps each of the thirteen provinces and territories to its court (type `Court`, in the definitions module). The Act's "Queen’s Bench" is written with a straight apostrophe in the constructor names. |
| court of appeal | s 2(1), src:41 | `cbca-core-definitions.l4` `court of appeal within s 2(1)` | One fact: an appeal lies to it from an order of a court. |
| debt obligation | s 2(1), src:42 | `cbca-core-definitions.l4` `debt obligation within s 2(1)` | Takes the kind of instrument (`Kind of security`) and whether it is of a corporation. |
| Director | s 2(1), src:43 | `cbca-core.l4` `Party` constructor `the Director` | By reference: the Director appointed under s 260, encoded by cb5. The official, not the word `director`. |
| director (also directors, board of directors) | s 2(1), src:44 | `cbca-core-definitions.l4` `director within s 2(1)`; `cbca-core-definitions.l4` `board of directors within s 2(1)` | "Directors" and "board of directors" include a single director: the second rule is TRUE for one director or more. |
| distributing corporation | s 2(1), src:45, with s 2(6) and (7), src:93 and 95 | `cbca-core-definitions.l4` `distributing corporation within s 2(1)`; `cbca-core-definitions.l4` `the Director may determine on application within s 2(6)`; `cbca-core-definitions.l4` `the Director may determine for a class within s 2(7)`; `cbca-core-definitions.l4` `determination takes effect within s 2(6) and s 2(7)` | "As defined in the regulations" is a plain BOOLEAN input (the regulations are not among the sources). The Director's determination is a record, `Determination about distributing status`; a valid determination that the corporation is not one takes it out. Other pieces ask a plain BOOLEAN `the corporation is a distributing corporation` unless they need the determination. |
| entity | s 2(1), src:46 | `cbca-core-definitions.l4` `entity within s 2(1)` | Over `Kind of person or entity`. |
| going-private transaction | s 2(1), src:47 | by reference: a pure pointer to the regulations; encoded nowhere, taken as an input | Name the input `the transaction is a going-private transaction as defined in the regulations` (BOOLEAN). Used at src:2365 and 2460 (Part XV) and src:2485-2487 (Part XVI), all cb4. |
| incapable | s 2(1), src:48 | `cbca-core-definitions.l4` `incapable within s 2(1)` | Found under provincial law to be unable, other than by reason of minority, to manage their property; or declared incapable by a court outside Canada. Three facts. |
| incorporator | s 2(1), src:49 | `cbca-core-definitions.l4` `incorporator within s 2(1)` | One fact: the person signs articles of incorporation. |
| individual | s 2(1), src:50 | `cbca-core-definitions.l4` `individual within s 2(1)` | Over `Kind of person or entity`. |
| liability | s 2(1), src:51 | `cbca-core-definitions.l4` `liability within s 2(1)` | "Includes": ordinary liability is a plain input, plus a debt arising under s 40, s 190(25), or paragraph 241(3)(f) or (g). |
| mandatary | s 2(1), src:52 | `cbca-core-definitions.l4` `mandatary within s 2(1)` | "In Quebec, includes a successor": the rule takes the place; a successor counts only in Quebec. |
| Minister | s 2(1), src:53 | `cbca-core.l4` `Party` constructor `the Minister` | By reference: the member of the Privy Council designated by the Governor in Council. Nothing more can be encoded. |
| officer | s 2(1), src:54 | `cbca-core-definitions.l4` `officer within s 2(1)`; `cbca-core.l4` `Office` | An individual holding one of the listed offices or performing a similar function. Part XI has its own "officer" (s 126(1)); see the defined terms below. |
| ordinary resolution | s 2(1), src:55 | `cbca-core-definitions.l4` `ordinary resolution within s 2(1)`; `cbca-core.l4` `Vote tally` | More votes cast in favour than against, by the shareholders who voted. A tie fails. |
| person | s 2(1), src:56 | `cbca-core-definitions.l4` `person within s 2(1)` | Over `Kind of person or entity`. Fork F4. |
| personal representative | s 2(1), src:57 | `cbca-core-definitions.l4` `personal representative within s 2(1)` | One fact: the person stands in place of and represents another person. The list the definition gives ("including, but not limited to") is illustration, not a limit. |
| prescribed | s 2(1), src:58 | by reference: a pure pointer to the regulations; encoded nowhere, taken as an input | Every "prescribed" in the Act (on 98 lines of the file) is a plain input; see the convention in "Naming conventions". |
| prior legislation | s 2(1), src:59 | by reference: used only in ss 266 and 267 (src:3316, 3329), encoded by cb5 | No input is defined here. cb5 names the fact. |
| put | s 2(1), src:60 | `cbca-core-definitions.l4` `put within s 2(1)` | Same record as "call", the mirror image: an option to deliver. |
| redeemable share | s 2(1), src:61-63 | `cbca-core-definitions.l4` `redeemable share within s 2(1)` | A share issued by a corporation that the corporation may purchase or redeem on its own demand, or is required by its articles to purchase or redeem. |
| resident Canadian | s 2(1), src:64-67 | `cbca-core-definitions.l4` `resident Canadian within s 2(1)` | Three limbs; limb (b) turns on a prescribed class (plain input); limb (c) counts the years since first becoming eligible to apply for citizenship. |
| security | s 2(1), src:68 | `cbca-core-definitions.l4` `security within s 2(1)` | A share or a debt obligation of a corporation, and a certificate evidencing either. Part VII has its own "security or security certificate" (s 48(2)). |
| security interest | s 2(1), src:69 | `cbca-core-definitions.l4` `security interest within s 2(1)` | An interest in or charge on property of a corporation that secures payment of a debt or performance of another obligation. |
| send | s 2(1), src:70 | `cbca-core-definitions.l4` `send within s 2(1)` | "Includes deliver." |
| series | s 2(1), src:71 | `cbca-core-definitions.l4` `series within s 2(1)` | A division of a class of shares. |
| special resolution | s 2(1), src:72 | `cbca-core-definitions.l4` `special resolution within s 2(1)` | Two-thirds or more of the votes cast, or signed by all the shareholders entitled to vote. Fork F2. |
| squeeze-out transaction | s 2(1), src:73 | `cbca-core-definitions.l4` `squeeze-out transaction within s 2(1)` | Used in Part XVI (cb4). Seven facts; a substitution counts only if it meets all three of its limbs. |
| unanimous shareholder agreement | s 2(1), src:74 | by reference: s 146(1) and (2), encoded by cb3 | Other pieces take the plain BOOLEAN input `there is a unanimous shareholder agreement`. It is named on 25 lines of the file. |
| affiliated bodies corporate | s 2(2), src:76-78 | `cbca-core-control.l4` `affiliated within s 2(2)`; `cbca-core-control.l4` `affiliated within s 2(2)(a)`; `cbca-core-control.l4` `affiliated within s 2(2)(b)`; `cbca-core-control.l4` `affiliated by the holdings within s 2(2)` | Pairwise facts, or a list of holdings. Fork F3. |
| control (a body corporate controlled by a person or by two or more bodies corporate) | s 2(3), src:80-82 | `cbca-core-control.l4` `controlled within s 2(3)`; `cbca-core-control.l4` `controlled within s 2(3)(a)`; `cbca-core-control.l4` `controlled within s 2(3)(b)`; `cbca-core-control.l4` `Holding in a body corporate` | Over the record `Holding in a body corporate`: more than 50% of the votes to elect directors, held other than by way of security only, and votes sufficient to elect a majority of the directors. |
| holding body corporate | s 2(4), src:84 | `cbca-core-control.l4` `holding body corporate within s 2(4)` | The other body corporate is its subsidiary. |
| subsidiary body corporate | s 2(5), src:86-91 | `cbca-core-control.l4` `subsidiary within s 2(5)`; `cbca-core-control.l4` `subsidiary within s 2(5)(a)` | Limbs (a)(i) to (iii) and (b). Fork F8. |
| infant | s 2(8), src:97 | `cbca-core-definitions.l4` `infant within s 2(8)` | The applicable provincial law if there is one (`MAYBE`), otherwise the child of the Convention on the Rights of the Child (plain input; the Convention is not among the sources). |
| individual with significant control | s 2.1(1) and (2), src:99-109 | `cbca-core-isc.l4` `individual with significant control within s 2.1(1)(a)`; `cbca-core-isc.l4` `individual with significant control within s 2.1(1)(b)`; `cbca-core-isc.l4` `individual with significant control within s 2.1(1)(c)`; `cbca-core-isc.l4` `each individual with significant control within s 2.1(2)` | Limb (b) (influence that would result in control in fact) and limb (c) (prescribed circumstances) are plain BOOLEAN inputs. Fork F7 for the joint cases. |
| significant number of shares | s 2.1(3), src:111-113 | `cbca-core-isc.l4` `significant number of shares within s 2.1(3)`; `cbca-core-isc.l4` `significant number of shares within s 2.1(3)(a)`; `cbca-core-isc.l4` `significant number of shares within s 2.1(3)(b)`; `cbca-core.l4` `Block of shares` | 25% or more of the voting rights, or 25% or more of the outstanding shares by fair market value. Fork F6. |
| property | s 25(5), src:456 | by reference: encoded by piece cb1, s 25(5), taken there as an input | For s 25 only: does not include a promissory note or a promise to pay of the kinds the subsection names. |
| open-end mutual fund | s 26(12), src:488 | by reference: encoded by piece cb1, s 26(12), taken there as an input | For s 26 only: a distributing corporation that carries on only the business of investing the consideration it receives for its shares, and nearly all of whose shares are redeemable on a shareholder's demand. Take `the corporation is a distributing corporation` as an input there. |
| adverse claim | s 48(2), src:701 | by reference: encoded by piece cb2, s 48(2), taken there as an input | Part VII. |
| bearer | s 48(2), src:702 | by reference: encoded by piece cb2, s 48(2), taken there as an input |  |
| bona fide purchaser | s 48(2), src:703 | by reference: encoded by piece cb2, s 48(2), taken there as an input |  |
| broker | s 48(2), src:704 | by reference: encoded by piece cb2, s 48(2), taken there as an input |  |
| delivery | s 48(2), src:705 | by reference: encoded by piece cb2, s 48(2), taken there as an input |  |
| fiduciary | s 48(2), src:706 | by reference: encoded by piece cb2, s 48(2), taken there as an input |  |
| fungible | s 48(2), src:707 | by reference: encoded by piece cb2, s 48(2), taken there as an input |  |
| genuine | s 48(2), src:708 | by reference: encoded by piece cb2, s 48(2), taken there as an input |  |
| good faith | s 48(2), src:709 | by reference: encoded by piece cb2, s 48(2), taken there as an input |  |
| holder | s 48(2), src:710 | by reference: encoded by piece cb2, s 48(2), taken there as an input |  |
| issuer | s 48(2), src:711-714 | by reference: encoded by piece cb2, s 48(2), taken there as an input | "Includes" a corporation in three cases. |
| overissue | s 48(2), src:715 | by reference: encoded by piece cb2, s 48(2), taken there as an input |  |
| purchaser | s 48(2), src:716 | by reference: encoded by piece cb2, s 48(2), taken there as an input |  |
| security or security certificate | s 48(2), src:717-721 | by reference: encoded by piece cb2, s 48(2), taken there as an input | A different definition from s 2(1) "security" (src:68). Name the rule `security or security certificate within s 48(2)`. |
| transfer | s 48(2), src:722 | by reference: encoded by piece cb2, s 48(2), taken there as an input |  |
| trust indenture | s 48(2), src:723 | by reference: encoded by piece cb2, s 48(2), taken there as an input | Points to the definition in s 82; see below. |
| unauthorized | s 48(2), src:724 | by reference: encoded by piece cb2, s 48(2), taken there as an input | In relation to a signature or an endorsement. |
| valid | s 48(2), src:725 | by reference: encoded by piece cb2, s 48(2), taken there as an input |  |
| appropriate person | s 65(1), src:934 | by reference: encoded by piece cb2, s 65(1), taken there as an input | In s 65 only. |
| endorsement in blank | s 65(5), src:949 | by reference: encoded by piece cb2, s 65(5), taken there as an input | "Includes an endorsement to bearer." |
| guarantee of the signature | s 77(2), src:1034 | by reference: encoded by piece cb2, s 77(2), taken there as an input | For s 77(1) only. |
| evidence of appointment or incumbency | s 77(4), src:1038 | by reference: encoded by piece cb2, s 77(4), taken there as an input | In paragraph 77(1)(b) only. |
| event of default | s 82(1), src:1092-1095 | by reference: encoded by piece cb2, s 82(1), taken there as an input | Part VIII. |
| trustee | s 82(1), src:1096 | by reference: encoded by piece cb2, s 82(1), taken there as an input | Part VIII. The vocabulary constructor `a trustee under a trust indenture` is the party; the definition is encoded there. |
| trust indenture | s 82(1), src:1097 | by reference: encoded by piece cb2, s 82(1), taken there as an input | The s 48(2) term points here. |
| business combination | s 126(1), src:1553 | by reference: encoded by piece cb3, s 126(1), taken there as an input | Part XI. |
| distributing corporation [Repealed, 2001, c. 14, s. 52] | s 126(1), src:1554 | by reference: encoded by piece cb3, s 126(1), taken there as an input | Repealed in this text; Part XI uses the s 2(1) term. |
| insider | s 126(1), src:1555-1559 | by reference: encoded by piece cb3, s 126(1), taken there as an input | Not the same as s 131(1) "insider" below, which is for s 131 only. Name them `insider within s 126(1)` and `insider within s 131(1)`. |
| officer | s 126(1), src:1560 | by reference: encoded by piece cb3, s 126(1), taken there as an input | Not the same as s 2(1) "officer" (src:54). Name it `officer within s 126(1)`. |
| share | s 126(1), src:1561-1563 | by reference: encoded by piece cb3, s 126(1), taken there as an input | A share carrying voting rights, with convertible securities and exercisable options. Not the same as the "share" of s 187(10) or s 206(1). |
| insider | s 131(1), src:1584 | by reference: encoded by piece cb3, s 131(1), taken there as an input | For s 131 only. |
| form of proxy | s 147, src:1822 | by reference: encoded by piece cb3, s 147, taken there as an input | Part XIII. |
| intermediary | s 147, src:1823-1830 | by reference: encoded by piece cb3, s 147, taken there as an input |  |
| proxy | s 147, src:1831 | by reference: encoded by piece cb3, s 147, taken there as an input |  |
| registrant [Repealed, 2001, c. 14, s. 67] | s 147, src:1832 | by reference: encoded by piece cb3, s 147, taken there as an input | Repealed in this text. |
| solicit or solicitation | s 147, src:1833-1846 | by reference: encoded by piece cb3, s 147, taken there as an input |  |
| solicitation by or on behalf of the management of a corporation | s 147, src:1847 | by reference: encoded by piece cb3, s 147, taken there as an input |  |
| a person’s business partner | s 161(2.1), src:1976 | by reference: encoded by piece cb3, s 161(2.1), taken there as an input | "Includes a shareholder of that person" for the purposes of s 161(2). |
| share | s 187(10), src:2301 | by reference: encoded by piece cb4, s 187(10), taken there as an input | For s 187(8) and (9) only. |
| reorganization | s 191(1), src:2434 | by reference: encoded by piece cb4, s 191(1), taken there as an input | In s 191 only. |
| arrangement | s 192(1), src:2453 | by reference: encoded by piece cb4, s 192(1), taken there as an input | In s 192 only. |
| dissenting offeree | s 206(1), src:2497 | by reference: encoded by piece cb4, s 206(1), taken there as an input | Part XVII. |
| offer | s 206(1), src:2498 | by reference: encoded by piece cb4, s 206(1), taken there as an input |  |
| offeree | s 206(1), src:2499 | by reference: encoded by piece cb4, s 206(1), taken there as an input |  |
| offeree corporation | s 206(1), src:2500 | by reference: encoded by piece cb4, s 206(1), taken there as an input |  |
| offeror | s 206(1), src:2501-2503 | by reference: encoded by piece cb4, s 206(1), taken there as an input | The vocabulary constructor `an offeror` is the party; the definition is encoded there. |
| share | s 206(1), src:2504-2506 | by reference: encoded by piece cb4, s 206(1), taken there as an input | Not the same as the "share" of s 126(1) or s 187(10). |
| take-over bid | s 206(1), src:2507 | by reference: encoded by piece cb4, s 206(1), taken there as an input |  |
| court | s 207, src:2581 | by reference: encoded by piece cb4, s 207, taken there as an input | Part XVIII: a court having jurisdiction in the place of the registered office. Not the same as s 2(1) "court". Name it `court within s 207`. |
| interested person | s 209(6), src:2603 | by reference: encoded by piece cb4, s 209(6), taken there as an input | In s 209 only. |
| shareholder | s 226(1), src:2830 | by reference: encoded by piece cb4, s 226(1), taken there as an input | "Includes the heirs and personal representatives" for s 226 only. |
| financial interest | s 237.1, src:2939-2949 | by reference: encoded by piece cb5, s 237.1, taken there as an input | Part XIX.1. |
| financial loss | s 237.1, src:2950 | by reference: encoded by piece cb5, s 237.1, taken there as an input |  |
| third party | s 237.1, src:2951 | by reference: encoded by piece cb5, s 237.1, taken there as an input |  |
| personal body corporate; common-law partnership | s 237.5(2), src:2983-2985 | by reference: encoded by piece cb5, s 237.5(2), taken there as an input | For s 237.5 only. |
| organized market | s 237.7(4), src:3002 | by reference: encoded by piece cb5, s 237.7(4), taken there as an input | In s 237.7 only. |
| action | s 238, src:3015 | by reference: encoded by piece cb5, s 238, taken there as an input | Part XX: an action under this Act. |
| complainant | s 238, src:3016-3020 | by reference: encoded by piece cb5, s 238, taken there as an input | The vocabulary constructor `a complainant` is the party; the definition is encoded there. |
| electronic document; information system | s 252.1, src:3137-3138 | by reference: encoded by piece cb5, s 252.1, taken there as an input | Part XX.1 (except in s 252.6 for "electronic document"). |
| electronic document; secure electronic signature | s 252.6(2), src:3171 | by reference: encoded by piece cb5, s 252.6(2), taken there as an input | Both have the meaning in subsection 31(1) of the Personal Information Protection and Electronic Documents Act, which is not among the sources: take them as plain inputs. |
| statement | s 262(1), src:3251 | by reference: encoded by piece cb5, s 262(1), taken there as an input | In s 262 only. |
| wrongdoing | s 266.1(3), src:3324 | by reference: encoded by piece cb5, s 266.1(3), taken there as an input | In s 266.1 only. |
| charter | s 268(1), src:3339 | by reference: encoded by piece cb5, s 268(1), taken there as an input | In s 268 only. |

### The input names for facts that point outside the keel

Pieces that need one of these facts take a plain input of this name, so that the five pieces ask for it the same way.

| the fact | input name | type | note |
| --- | --- | --- | --- |
| the corporation is a distributing corporation | `the corporation is a distributing corporation` | BOOLEAN | The keel rule `distributing corporation within s 2(1)` takes the regulations' answer and the Director's determination separately; a piece that does not need the determination takes this one input. |
| the transaction is a going-private transaction | `the transaction is a going-private transaction as defined in the regulations` | BOOLEAN | Used in Parts XV and XVI (cb4). |
| something is prescribed | `<the thing> is prescribed by the regulations` | BOOLEAN | For an amount, a period or a form: `the prescribed <thing>` (NUMBER or STRING). |
| there is a unanimous shareholder agreement | `there is a unanimous shareholder agreement` | BOOLEAN | cb3 encodes s 146; other pieces take this. |
| the person is an infant | `the person is an infant` | BOOLEAN | Or call `infant within s 2(8)`. |
| the individual is a resident Canadian | `the individual is a resident Canadian` | BOOLEAN | Or call `resident Canadian within s 2(1)`. |
| the resolution was passed | `the resolution is an ordinary resolution`, `the resolution is a special resolution` | BOOLEAN | Or pass a `Vote tally` to `resolution passed as the kind within s 2(1)`. |
| one body corporate is a subsidiary of, or affiliated with, another | `the body corporate is a subsidiary of the other body corporate`, `the body corporate is an affiliate of the other body corporate` | BOOLEAN | Take these unless the rule turns on the holdings themselves; then use `cbca-core-control.l4`. |

### Terms the Act defines more than once

The Act gives the same word different meanings in different places.
Name each rule by the provision, so the names cannot collide, and where the Act defines the word again for your provision, use your own definition and not the rule for another provision.

| word | where defined | rule names to use |
| --- | --- | --- |
| officer | s 2(1) (keel); s 126(1) (cb3) | `officer within s 2(1)`; `officer within s 126(1)` |
| insider | s 126(1) and s 131(1) (cb3) | `insider within s 126(1)`; `insider within s 131(1)` |
| share | s 126(1) (cb3); s 187(10) (cb4); s 206(1) (cb4) | `share within s 126(1)`; `share within s 187(10)`; `share within s 206(1)` |
| security | s 2(1) (keel); "security or security certificate", s 48(2) (cb2) | `security within s 2(1)`; `security or security certificate within s 48(2)` |
| court | s 2(1) (keel); s 207 (cb4) | `court within s 2(1)`; `court within s 207` |
| trust indenture | s 48(2) (points to s 82); s 82(1) (cb2) | `trust indenture within s 82(1)` |
| electronic document | s 252.1; s 252.6(2) (cb5) | `electronic document within s 252.1`; `electronic document within s 252.6(2)` |
| shareholder | s 226(1) (cb4) widens the word for that section; Part XII (cb3) uses it undefined | `shareholder within s 226(1)`; the constructor `a shareholder` is the party in either case |

## Instructions to the pieces

Read these before you import anything.

1. **Copy the modules you use, unchanged, into your own folder.**
   `IMPORT` finds only modules in the importing file's own folder.
   `cbca-core.l4` is needed by all the others.
   Copy `cbca-core-definitions.l4`, `cbca-core-control.l4` and `cbca-core-isc.l4` only if you call them, and never copy the `cbca-core-tests-*.l4` files.
   Do not edit a keel file; if one is wrong, say so in your own report and write the fix in your piece under a different name.
2. **Import with** `IMPORT prelude` and ``IMPORT `cbca-core` ``, then the keel modules you use.
   An import is passed on: a file that imports only `prelude` and `cbca-core` can call `add months`, because the core imports `daydate` (checked with a three-line file).
   Importing `daydate` again is harmless; the earlier smoke test did both.
3. **Every top-level name must be unique across the whole Act**: rules, types, enumeration constructors and the mixfix keywords of a rule head.
   A name defined in two imported modules cannot be used at all.
   The core's names are listed under "Vocabulary"; to check a new name against all the keel's, `grep -n -F '<name>' cbca-core*.l4`.
   Do not write a rule whose head uses the keywords `counted from` or `counted back from`.
4. **`YMD` is defined only in `cbca-core.l4`.**
   Do not define it again; write `YMD year month day`.
5. **Use the vocabulary; do not redeclare it.**
   The parties of a regulative rule are the constructors of `Party`.
   A party the Act names that is not there goes in an enumeration of your own, declared in your piece, with constructors no other module can use.
   The same goes for provinces (`Province or territory`), offices (`Office`), kinds of articles, resolutions and votes (`Kind of resolution`, `Vote tally`) and shares (`Block of shares`).
6. **Where your rule turns on a term the keel defines, take the fact as a plain input, or call the keel's rule.**
   Take the plain input (the names are under "Defined terms") when the person in the seat can state the fact directly: "Is the corporation a distributing corporation?"
   Call the keel's rule when the rule works from the definition's own facts, for example `resolution passed as the kind within s 2(1)` over a `Vote tally`.
   Where the keel's rule exists, never restate its logic in your piece.
7. **Resolutions.**
   Pass a `Vote tally` (votes cast in favour, votes cast against, and whether the resolution was signed by all the shareholders entitled to vote) to `ordinary resolution within s 2(1)`, `special resolution within s 2(1)` or `resolution passed as the kind within s 2(1)`.
   A tally counts votes, not shareholders, and counts only the votes of shareholders who voted.
   A threshold the Act or the articles set differently (unanimous, a larger majority) is a rule in your piece.
8. **Control, subsidiary and affiliate.**
   Most rules in the Act only need to know that one body corporate is a subsidiary of, or affiliated with, another: take that as a plain input (the names are under "Defined terms").
   Use `cbca-core-control.l4` only when your rule turns on the holdings.
   A `Holding in a body corporate` is one record per body corporate and group of holders; the holders are names (strings), and a person who is not a body corporate (an individual) has `the persons holding are bodies corporate` FALSE.
   `subsidiary within s 2(5)` and `affiliated by the holdings within s 2(2)` follow the holdings up or across until no new body corporate is found, so a circular holding ends; give them the whole list of holdings.
   Without the holdings, `affiliated within s 2(2)` takes four facts about the pair.
9. **Time limits.**
   Write a time limit as a `Time limit` and use `the last day of ... counted from ...`, `the earliest day allowed by ... counted back from ...` and `done within the time limit`.
   A limit counted in days may also go in a regulative rule's `WITHIN`.
   The counting convention is fork F1: do not invent another.
10. **Part-local definitions get their own rule and a name with the provision.**
    Where the Act defines a word again for your Part or section, name your rule `<word> within s N`; the table "Terms the Act defines more than once" lists the known cases.
    Every `officer`, `insider`, `share`, `security`, `court` and `shareholder` in your piece is the one your own provision defines.
11. **Fractions are NUMBERs from 0 to 1 written with `%`, and in argument position are bracketed, `(25%)`.**
    Money is a NUMBER of dollars.
    Never write 25 for 25%.
12. **Build a record with `WITH` (named fields), not positional `OF`, when it has two or more fields of one type.**
    Positional `OF` is order-dependent and silent: swap two NUMBERs in the declaration and every call still compiles.
    The keel's tests build every record with `WITH` for that reason.
13. **Where the text does not answer, return `MAYBE` with `NOTHING` or a named constructor, and assert it.**
    Never FALSE and never 0.
14. **Mark your quoted lines and `@ref`s with `srcrefs.py quote`, as the keel does; `python3 -I srcrefs.py check --refs <raw> <your files>` must say 0 problems.**
    Line numbers in your quotes are lines of the raw text file, not of this one.
15. **Expect the keel's tests to stay green.**
    If you change nothing in the keel files, `cbca-core-tests-*.l4` need not be copied and cannot break.

## Coverage table

One row per provision of my range, lines 13-114 of the text: every heading line, every section, every subsection and every paragraph, and for s 2(1) every defined term and every lettered paragraph of a term.
100 rows: 73 encoded, 18 inert, 0 repealed or blank in this text, 9 fork (a fork row is encoded, in the reading its note gives, and the fork is in "Fork register").
Counted against the text: the range has 13 heading lines (13, 15, 16, 75, 79, 83, 85, 92, 94, 96, 98, 106, 110), each with a row marked inert; 2 sections (s 2 at line 17, s 2.1 at line 99); 8 subsections of s 2 and 3 of s 2.1; 40 defined terms in s 2(1).
Every non-blank line from 13 to 113 falls inside at least one row's range (checked by a script that lists any line no row covers; it listed none); line 114 is blank.
Nothing in the range is marked repealed or not in force: a search of lines 13-114 for "repeal" and "not in force" found only the words "in force" inside the definition of "prior legislation" (src:59).

| provision | source lines | disposition | where | note |
| --- | --- | --- | --- | --- |
| Part I heading: PART I Interpretation and Application | 13 | inert | - | The title of the Part that holds s 2, s 2.1, s 3 and s 4 (by the section index). It states no rule; the rest of Part I (s 3 and s 4, application, from line 115) is cb1's. |
| Heading: Interpretation | 15 | inert | - | A heading (a label for what follows); it states no rule and carries no condition, so there is nothing to encode. |
| Heading: Definitions | 16 | inert | - | A heading (a label for what follows); it states no rule and carries no condition, so there is nothing to encode. |
| s 2(1) lead-in: "In this Act," | 17 | inert | - | Says the definitions below apply throughout the Act. That scope is carried by structure, not by a rule: every piece imports the modules that encode the definitions, and each rule is named for the section it works out. The lead-in has no "unless the context otherwise requires" qualifier to model. |
| s 2(1) affairs | 18 | encoded | `cbca-core-definitions.l4` `affairs within s 2(1)` | Includes-and-excludes definition: relationships, but not the business carried on. |
| s 2(1) affiliate | 19 | encoded | `cbca-core-control.l4` `affiliate within s 2(1)`; `cbca-core-control.l4` `affiliate within s 2(1) by the facts` | Points to s 2(2). |
| s 2(1) articles | 20 | encoded | `cbca-core-definitions.l4` `articles within s 2(1)`; `cbca-core.l4` `Kind of articles` | The nine kinds and any amendment. |
| s 2(1) associate (lead-in) | 21 | encoded | `cbca-core-definitions.l4` `associate within s 2(1)` | The union of paragraphs (a) to (f), over one record of facts about the other party. |
| s 2(1) associate (a) | 22 | encoded | `cbca-core-definitions.l4` `associate within s 2(1)(a)` | More than 10% of the voting rights, counting convertible securities and exercisable options. |
| s 2(1) associate (b) | 23 | encoded | `cbca-core-definitions.l4` `associate within s 2(1)(b)` | A partner acting on behalf of the partnership. |
| s 2(1) associate (c) | 24 | encoded | `cbca-core-definitions.l4` `associate within s 2(1)(c)` | A trust, estate or succession in which the person has a substantial beneficial interest or serves as trustee or liquidator or in a similar capacity. |
| s 2(1) associate (d) | 25 | fork | `cbca-core-definitions.l4` `associate within s 2(1)(d)` | Encoded as: a spouse, or an individual cohabiting conjugally who has so cohabited for at least one year. Fork F5: the one-year period qualifies only the cohabiting individual. |
| s 2(1) associate (e) | 26 | encoded | `cbca-core-definitions.l4` `associate within s 2(1)(e)` | A child of the person or of the spouse or individual in (d). |
| s 2(1) associate (f) | 27 | encoded | `cbca-core-definitions.l4` `associate within s 2(1)(f)` | A relative of the person, or of the spouse or individual in (d), with the same residence as the person. |
| s 2(1) auditor | 28 | encoded | `cbca-core-definitions.l4` `auditor within s 2(1)` |  |
| s 2(1) beneficial interest | 29 | encoded | `cbca-core-definitions.l4` `beneficial interest within s 2(1)` |  |
| s 2(1) beneficial ownership | 30 | encoded | `cbca-core-definitions.l4` `beneficial ownership within s 2(1)` |  |
| s 2(1) body corporate | 31 | encoded | `cbca-core-definitions.l4` `body corporate within s 2(1)` |  |
| s 2(1) call | 32 | encoded | `cbca-core-definitions.l4` `call within s 2(1)` |  |
| s 2(1) corporation | 33 | encoded | `cbca-core-definitions.l4` `corporation within s 2(1)` |  |
| s 2(1) court (lead-in) | 34 | encoded | `cbca-core-definitions.l4` `court within s 2(1)`; `cbca-core.l4` `Province or territory` | One rule maps a province or territory to its court (paragraphs (a) to (e)). |
| s 2(1) court (a) | 35 | encoded | `cbca-core-definitions.l4` `court within s 2(1)` | Newfoundland and Labrador: the Trial Division of the Supreme Court. |
| s 2(1) court (a.1) | 36 | encoded | `cbca-core-definitions.l4` `court within s 2(1)` | Ontario: the Superior Court of Justice. |
| s 2(1) court (b) | 37 | encoded | `cbca-core-definitions.l4` `court within s 2(1)` | Nova Scotia, British Columbia and Prince Edward Island: the Supreme Court of the Province. |
| s 2(1) court (c) | 38 | encoded | `cbca-core-definitions.l4` `court within s 2(1)` | Manitoba, Saskatchewan, Alberta and New Brunswick: the Court of Queen’s Bench. |
| s 2(1) court (d) | 39 | encoded | `cbca-core-definitions.l4` `court within s 2(1)` | Quebec: the Superior Court. |
| s 2(1) court (e) | 40 | encoded | `cbca-core-definitions.l4` `court within s 2(1)` | Yukon, the Northwest Territories, Nunavut: their courts. |
| s 2(1) court of appeal | 41 | encoded | `cbca-core-definitions.l4` `court of appeal within s 2(1)` |  |
| s 2(1) debt obligation | 42 | encoded | `cbca-core-definitions.l4` `debt obligation within s 2(1)` |  |
| s 2(1) Director | 43 | encoded | `cbca-core.l4` `Party` constructor `the Director` | A pointer to s 260 (cb5); the vocabulary carries the official. |
| s 2(1) director, directors, board of directors | 44 | encoded | `cbca-core-definitions.l4` `director within s 2(1)`; `cbca-core-definitions.l4` `board of directors within s 2(1)` |  |
| s 2(1) distributing corporation | 45 | encoded | `cbca-core-definitions.l4` `distributing corporation within s 2(1)` | Subject to s 2(6) and (7). "As defined in the regulations" is a plain input. |
| s 2(1) entity | 46 | encoded | `cbca-core-definitions.l4` `entity within s 2(1)` |  |
| s 2(1) going-private transaction | 47 | inert | - | A pure pointer: "as defined in the regulations", which are not among the sources. Nothing to compute; other pieces take a plain BOOLEAN input (named in "Defined terms"). |
| s 2(1) incapable | 48 | encoded | `cbca-core-definitions.l4` `incapable within s 2(1)` |  |
| s 2(1) incorporator | 49 | encoded | `cbca-core-definitions.l4` `incorporator within s 2(1)` |  |
| s 2(1) individual | 50 | encoded | `cbca-core-definitions.l4` `individual within s 2(1)` |  |
| s 2(1) liability | 51 | encoded | `cbca-core-definitions.l4` `liability within s 2(1)` |  |
| s 2(1) mandatary | 52 | encoded | `cbca-core-definitions.l4` `mandatary within s 2(1)` |  |
| s 2(1) Minister | 53 | encoded | `cbca-core.l4` `Party` constructor `the Minister` | Nothing more to compute: the Minister is whoever the Governor in Council designates. |
| s 2(1) officer | 54 | encoded | `cbca-core-definitions.l4` `officer within s 2(1)`; `cbca-core.l4` `Office` |  |
| s 2(1) ordinary resolution | 55 | encoded | `cbca-core-definitions.l4` `ordinary resolution within s 2(1)` |  |
| s 2(1) person | 56 | fork | `cbca-core-definitions.l4` `person within s 2(1)` | Encoded as listed in the definition. Fork F4: "association" is not read to include the unincorporated association or organization of "entity". |
| s 2(1) personal representative | 57 | encoded | `cbca-core-definitions.l4` `personal representative within s 2(1)` |  |
| s 2(1) prescribed | 58 | inert | - | A pure pointer to the regulations, which are not among the sources. It is a convention rather than a rule: every prescribed fact, form, amount or period is a plain input (see "Naming conventions"). |
| s 2(1) prior legislation | 59 | inert | - | A pointer to the Acts that preceded this one. Used only at src:3316 and 3329 (cb5), so no input is defined here. |
| s 2(1) put | 60 | encoded | `cbca-core-definitions.l4` `put within s 2(1)` |  |
| s 2(1) redeemable share (lead-in) | 61 | encoded | `cbca-core-definitions.l4` `redeemable share within s 2(1)` | A share issued by a corporation. |
| s 2(1) redeemable share (a) | 62 | encoded | `cbca-core-definitions.l4` `redeemable share within s 2(1)` | That the corporation may purchase or redeem on its own demand. |
| s 2(1) redeemable share (b) | 63 | encoded | `cbca-core-definitions.l4` `redeemable share within s 2(1)` | That the articles require the corporation to purchase or redeem at a time or on a shareholder's demand. |
| s 2(1) resident Canadian (lead-in) | 64 | encoded | `cbca-core-definitions.l4` `resident Canadian within s 2(1)` | An individual. |
| s 2(1) resident Canadian (a) | 65 | encoded | `cbca-core-definitions.l4` `resident Canadian within s 2(1)` | A citizen ordinarily resident in Canada. |
| s 2(1) resident Canadian (b) | 66 | encoded | `cbca-core-definitions.l4` `resident Canadian within s 2(1)` | A citizen not ordinarily resident who is in a prescribed class (plain input). |
| s 2(1) resident Canadian (c) | 67 | encoded | `cbca-core-definitions.l4` `resident Canadian within s 2(1)` | A permanent resident ordinarily resident, unless for more than one year after first becoming eligible to apply for citizenship. |
| s 2(1) security | 68 | encoded | `cbca-core-definitions.l4` `security within s 2(1)` |  |
| s 2(1) security interest | 69 | encoded | `cbca-core-definitions.l4` `security interest within s 2(1)` |  |
| s 2(1) send | 70 | encoded | `cbca-core-definitions.l4` `send within s 2(1)` |  |
| s 2(1) series | 71 | encoded | `cbca-core-definitions.l4` `series within s 2(1)` |  |
| s 2(1) special resolution | 72 | fork | `cbca-core-definitions.l4` `special resolution within s 2(1)` | Encoded as: two-thirds or more of the votes cast, or signed by all the shareholders entitled to vote. Fork F2: when no votes are cast and nothing is signed, it is not passed. |
| s 2(1) squeeze-out transaction | 73 | encoded | `cbca-core-definitions.l4` `squeeze-out transaction within s 2(1)` |  |
| s 2(1) unanimous shareholder agreement | 74 | inert | - | A pointer to s 146(1) and (2) (cb3). Other pieces take a plain BOOLEAN input; cb3 encodes the agreement itself. |
| Heading: Affiliated bodies corporate | 75 | inert | - | A heading (a label for what follows); it states no rule and carries no condition, so there is nothing to encode. |
| s 2(2) lead-in | 76 | encoded | `cbca-core-control.l4` `affiliated within s 2(2)` | "For the purposes of this Act": the rule applies wherever the Act says affiliated or affiliate. |
| s 2(2)(a) | 77 | encoded | `cbca-core-control.l4` `affiliated within s 2(2)(a)`; `cbca-core-control.l4` `affiliated by the holdings within s 2(2)(a)`; `cbca-core-control.l4` `both are subsidiaries of the same body corporate by`; `cbca-core-control.l4` `each is controlled by the same person by` | Three alternatives: one is the subsidiary of the other; both are subsidiaries of the same body corporate; each is controlled by the same person. |
| s 2(2)(b) | 78 | fork | `cbca-core-control.l4` `affiliated within s 2(2)(b)`; `cbca-core-control.l4` `affiliated by the holdings within s 2(2)` | Encoded with a closure: a deemed affiliation counts as an affiliation when applying (b) again. Fork F3. |
| Heading: Control | 79 | inert | - | A heading (a label for what follows); it states no rule and carries no condition, so there is nothing to encode. |
| s 2(3) lead-in | 80 | encoded | `cbca-core-control.l4` `controlled within s 2(3)`; `cbca-core-control.l4` `Holding in a body corporate` | Controlled by a person or by two or more bodies corporate if (a) and (b). |
| s 2(3)(a) | 81 | encoded | `cbca-core-control.l4` `controlled within s 2(3)(a)` | More than fifty per cent of the votes to elect directors, held other than by way of security only. |
| s 2(3)(b) | 82 | encoded | `cbca-core-control.l4` `controlled within s 2(3)(b)` | The votes are sufficient, if exercised, to elect a majority of the directors: a fact the caller states. |
| Heading: Holding body corporate | 83 | inert | - | A heading (a label for what follows); it states no rule and carries no condition, so there is nothing to encode. |
| s 2(4) | 84 | encoded | `cbca-core-control.l4` `holding body corporate within s 2(4)` |  |
| Heading: Subsidiary body corporate | 85 | inert | - | A heading (a label for what follows); it states no rule and carries no condition, so there is nothing to encode. |
| s 2(5) lead-in | 86 | encoded | `cbca-core-control.l4` `subsidiary within s 2(5)` |  |
| s 2(5)(a) lead-in: "it is controlled by" | 87 | encoded | `cbca-core-control.l4` `subsidiary within s 2(5)(a)` |  |
| s 2(5)(a)(i) | 88 | fork | `cbca-core-control.l4` `subsidiary within s 2(5)(a)`; `cbca-core-control.l4` `the holders fit s 2(5)(a)` | Encoded as: controlled by that body corporate alone. Fork F8. |
| s 2(5)(a)(ii) | 89 | fork | `cbca-core-control.l4` `subsidiary within s 2(5)(a)`; `cbca-core-control.l4` `the holders fit s 2(5)(a)` | Encoded as: the holders are that body corporate and one or more bodies each controlled by it alone. Fork F8. |
| s 2(5)(a)(iii) | 90 | fork | `cbca-core-control.l4` `subsidiary within s 2(5)(a)`; `cbca-core-control.l4` `the holders fit s 2(5)(a)` | Encoded as: two or more holders, each controlled by that body corporate alone. Fork F8. |
| s 2(5)(b) | 91 | encoded | `cbca-core-control.l4` `subsidiary within s 2(5)`; `cbca-core-control.l4` `the bodies corporate above` | Subsidiary of a subsidiary, followed up the chain until no new body corporate is found, so a circular holding ends. |
| Heading: Exemptions — on application by corporation | 92 | inert | - | A heading (a label for what follows); it states no rule and carries no condition, so there is nothing to encode. |
| s 2(6) | 93 | encoded | `cbca-core-definitions.l4` `the Director may determine on application within s 2(6)`; `cbca-core-definitions.l4` `determination takes effect within s 2(6) and s 2(7)` | On application, if the Director is satisfied it would not be prejudicial to the public interest. |
| Heading: Exemptions — classes of corporations | 94 | inert | - | A heading (a label for what follows); it states no rule and carries no condition, so there is nothing to encode. |
| s 2(7) | 95 | encoded | `cbca-core-definitions.l4` `the Director may determine for a class within s 2(7)`; `cbca-core-definitions.l4` `determination takes effect within s 2(6) and s 2(7)` | For a class of corporations, on the same test. |
| Heading: Infants | 96 | inert | - | A heading (a label for what follows); it states no rule and carries no condition, so there is nothing to encode. |
| s 2(8) | 97 | encoded | `cbca-core-definitions.l4` `infant within s 2(8)` |  |
| Heading: Individual with significant control | 98 | inert | - | A heading (a label for what follows); it states no rule and carries no condition, so there is nothing to encode. |
| s 2.1(1) lead-in | 99 | encoded | `cbca-core-isc.l4` `individual with significant control within s 2.1(1)(a)`; `cbca-core-isc.l4` `individual with significant control within s 2.1(1)(b)`; `cbca-core-isc.l4` `individual with significant control within s 2.1(1)(c)` | Any of the three limbs. |
| s 2.1(1)(a) lead-in | 100 | encoded | `cbca-core-isc.l4` `individual with significant control within s 2.1(1)(a)` | Any of the interests or rights, or any combination, in respect of a significant number of shares. |
| s 2.1(1)(a)(i) | 101 | encoded | `cbca-core-isc.l4` `individual with significant control within s 2.1(1)(a)` | Registered holder. |
| s 2.1(1)(a)(ii) | 102 | encoded | `cbca-core-isc.l4` `individual with significant control within s 2.1(1)(a)` | Beneficial owner. |
| s 2.1(1)(a)(iii) | 103 | encoded | `cbca-core-isc.l4` `individual with significant control within s 2.1(1)(a)` | Direct or indirect control or direction. |
| s 2.1(1)(b) | 104 | encoded | `cbca-core-isc.l4` `individual with significant control within s 2.1(1)(b)` | Influence that would result in control in fact: a judgement the caller states. |
| s 2.1(1)(c) | 105 | encoded | `cbca-core-isc.l4` `individual with significant control within s 2.1(1)(c)` | Prescribed circumstances: for the regulations, a plain input. |
| Heading: Joint ownership or control | 106 | inert | - | A heading (a label for what follows); it states no rule and carries no condition, so there is nothing to encode. |
| s 2.1(2) lead-in | 107 | fork | `cbca-core-isc.l4` `each individual with significant control within s 2.1(2)` | Two or more individuals are each considered. Fork F7: each alternative is measured against its own shares. |
| s 2.1(2)(a) | 108 | encoded | `cbca-core-isc.l4` `each individual with significant control within s 2.1(2)` | Held jointly. |
| s 2.1(2)(b) | 109 | encoded | `cbca-core-isc.l4` `each individual with significant control within s 2.1(2)` | Subject to an agreement or arrangement to be exercised jointly or in concert. |
| Heading: Significant number of shares | 110 | inert | - | A heading (a label for what follows); it states no rule and carries no condition, so there is nothing to encode. |
| s 2.1(3) lead-in | 111 | encoded | `cbca-core-isc.l4` `significant number of shares within s 2.1(3)` |  |
| s 2.1(3)(a) | 112 | fork | `cbca-core-isc.l4` `significant number of shares within s 2.1(3)(a)` | Encoded as: 25% or more of the votes of the outstanding voting shares, with at least one such vote outstanding. Fork F6. |
| s 2.1(3)(b) | 113 | encoded | `cbca-core-isc.l4` `significant number of shares within s 2.1(3)(b)` | 25% or more of all the outstanding shares by fair market value; the same guard for a corporation with no value. |

## Fork register

Every ambiguity I met in the range: the readings I saw, the one I took, the text that licenses each, and how to change it.
None is resolved by a court or the regulator that I know of; none is settled by anything in the sources.
Where I looked: every definition and subsection of the range, read twice; the tests were written to sit on both sides of each boundary the words draw.

### F1: how a time limit is counted (core, `the last day of ... counted from ...`)

- The text: the Act gives time limits in days, weeks, months and years ("within twenty days after ..."), and nothing in my range says how a day is counted.
  A rule of interpretation outside the sources may settle it; this file does not claim to know it.
- Readings: (i) the start day is day 0, so the last day is the start plus N units, and the start day and the last day are both in time [taken]; (ii) the start day is day 1, so the last day is one earlier for days and weeks; (iii) a limit that falls on a holiday rolls to the next business day.
- Months and years add calendar months and years and clamp to the last day of a shorter month (31 August plus six months is 28 February), because `add months` and `add years` do.
- To change it: the three rules in `cbca-core.l4`, one place.
  Holiday roll-forward is not encoded at all.

### F2: a special resolution when no votes are cast (definitions, `special resolution within s 2(1)`)

- The text, src:72: "passed by a majority of not less than two-thirds of the votes cast by the shareholders who voted in respect of that resolution or signed by all the shareholders entitled to vote on that resolution".
- Readings: (i) two-thirds or more of the votes cast are in favour, and some votes were cast; with none cast and nothing signed, it is not passed [taken]; (ii) with no votes cast the condition holds vacuously.
- Taken also: "a majority of not less than two-thirds" is read as both at once: more votes in favour than against, and at least two-thirds in favour (the first matters only when no votes are cast); 200 of 300 passes, 199 of 300 does not.
- The ordinary resolution (src:55) is read the same way: more votes in favour than against, so a tie and no votes are both not passed.
- To change it: the "majority" conjunct of `special resolution within s 2(1)`.

### F3: deemed affiliation counts as being affiliated with the same body corporate (control, `affiliated by the holdings within s 2(2)`)

- The text, src:78: "if two bodies corporate are affiliated with the same body corporate at the same time, they are deemed to be affiliated with each other".
- Readings: (i) "affiliated" in that sentence includes an affiliation the sentence itself deems, so the relation is closed: bodies joined by any chain of affiliations are all affiliated [taken]; (ii) only an affiliation under (a) counts, so (b) applies once.
- The test `two small families under Mr X` is the case that separates them: A1 and B1 have no body corporate in common that each is affiliated with under (a), and are affiliated only on reading (i).
- To change it: use the directly affiliated bodies and their common neighbours in place of the reached list in `affiliated by the holdings within s 2(2)`.

### F4: "association" in "person" and "unincorporated association or organization" in "entity" (definitions, `person within s 2(1)`)

- The text: "person means an individual, partnership, association, body corporate, or personal representative" (src:56); "entity means a body corporate, a partnership, a trust, a joint venture or an unincorporated association or organization" (src:46).
- Readings: (i) they are two things: `an association` is a person and `an unincorporated association or organization` is an entity and not a person [taken]; (ii) an unincorporated association is an association, so it is also a person.
- Taken because the text uses two different phrases in two definitions, and a trust and a joint venture are expressly absent from "person".
- To change it: add `an unincorporated association or organization` to `person within s 2(1)`.

### F5: the one-year cohabitation in "associate" (d) (definitions, `associate within s 2(1)(d)`)

- The text, src:25: "(d) a spouse of that person or an individual who is cohabiting with that person in a conjugal relationship, having so cohabited for a period of at least one year".
- Readings: (i) "having so cohabited" qualifies only the cohabiting individual: a spouse is an associate with no cohabitation period [taken]; (ii) it qualifies both.
- Taken because "so cohabited" refers back to "cohabiting", which only the second limb uses.
- To change it: the spouse limb of that rule.

### F6: no voting shares outstanding (isc, `significant number of shares within s 2.1(3)(a)`)

- The text, src:112: "any number of shares that carry 25% or more of the voting rights attached to all of the corporation's outstanding voting shares".
- Readings: (i) with no voting shares outstanding there are no voting rights to carry 25% of, so (a) is not met [taken]; (ii) 0 is 25% or more of 0, so any number of shares meets (a).
- The same guard is on (b) when the outstanding shares have no value.
- To change it: the first conjunct of each of the two rules.

### F7: joint ownership: each alternative uses its own shares (isc, `each individual with significant control within s 2.1(2)`)

- The text, src:107-109: two or more individuals are each an individual with significant control if, "in respect of a significant number of shares", (a) an interest or right, or a combination of them, "is held jointly by them", or (b) a right, or a combination of rights, "is subject to any agreement or arrangement under which it is to be exercised jointly or in concert by them".
- Readings: (i) each alternative is measured against its own block of shares: the shares held jointly under (a), the shares subject to the agreement under (b) [taken]; (ii) the two could be added into one block and measured together.
- Taken because each alternative names its own combination and nothing in the text adds one to the other.
- To change it: the rule takes one block for each alternative; to combine them, pass the sum as both.

### F8: "controlled by that other body corporate" means controlled by it alone (control, `subsidiary within s 2(5)(a)`)

- The text, src:87-90: a body corporate is a subsidiary of another if it is controlled by (i) that other body corporate, (ii) that other body corporate and one or more bodies corporate each of which is controlled by that other body corporate, or (iii) two or more bodies corporate each of which is controlled by that other body corporate.
- Readings: (i) "controlled by that other body corporate" means that body corporate is the person that controls, as "controlled by a person" in s 2(3) [taken]; (ii) it includes control by it together with bodies it does not control.
- Taken because limbs (ii) and (iii) would be pointless on the second reading: they exist to spell out the cases where several bodies control together, and require each to be controlled by the other body corporate.
  The test `two unrelated bodies control Z` shows the consequence: Z is controlled, but is a subsidiary of neither.
- To change it: `controlled by a body corporate alone` in `the holders fit s 2(5)(a)`.

### Limits that are not forks

- The regulations, the Convention on the Rights of the Child, provincial law, and the Personal Information Protection and Electronic Documents Act are not among the sources: a fact that turns on one is a plain input.
- s 2(3)(b), "sufficient, if exercised, to elect a majority of the directors", turns on how many directors are to be elected and how the votes are cast; it is a plain input, not computed.
- s 2(3)(a), "by or for the benefit of", is read by the caller: the fraction of the votes is the fraction held by or for the benefit of the listed holders, other than by way of security only.
- s 2(1) "associate" (a) counts convertible securities and exercisable options: the fraction the caller states includes them.
- s 2(6) and (7), "is not or was not": the record says whether the Director made a determination and of what kind; it does not say for which period it holds.
  A piece that needs a date asks for one.
- The control graph identifies a body corporate by its name (a string): two holdings with the same name are the same body corporate.
- The courts of "Queen's Bench" keep the name the text gives (src:38); the text is current to 2026-09-30 and a later change of name is not read.
- The text is English only; the French version, equally authoritative, was not read.

## What the stable binary does not accept

The target is `main`, and the binary is the stable build `l4` 1.6.98 (`l4 --version` prints `1.6.98 (main, 7689b0d, 2026-10-19)`, sha256 `82ea44ad...263e`).

**What I met while writing the keel (measured with this binary).**

- **A lambda body that continues on a following line, at a column left of its first token, ends at the line break.**
  ``any (GIVEN x YIELD`` then ``x GREATER THAN 1`` then, one line below and to the left, ``AND x LESS THAN 5) xs`` fails with "The first argument of function `__AND__` is expected to be of type BOOLEAN" because the lambda has become the first argument.
  A body on the next line by itself, a body on one line, and a body in brackets that spans lines all work.
  The keel names the body as a helper rule with all its arguments and calls it from a one-line lambda.
- **A postfix `%` literal followed by another argument is a parse error:** `` `a holding in` "B" (LIST "A") TRUE 60% TRUE `` fails with "unexpected TRUE"; write `(60%)`.
- **An enumeration constructor belongs to one enumeration:** `` `an officer` `` is a `Party` and not an `Office`, and comparing it with an `Office` constructor is a type error, not FALSE.
- **Imports are transitive:** importing `cbca-core` gives you what it imports, `daydate` among it.

**What the dialects reference lists as rejected or read differently on `main`, repeated here because the pieces write regulative rules.**
These come from `writing-l4-rules/references/dialects.md` (measured on this same build, with probe numbers); I did not re-measure them, and the keel does not use any of them.

| spelling | on `main` build 98 | write instead |
| --- | --- | --- |
| a section `GIVEN` (probes 06-12) | rejects, seven different messages; it belongs to the next rule only | a `GIVEN` on every rule that reads the input |
| `TYPICALLY` on a field or a `GIVEN` (13, 14, 16) | rejects | leave the default out |
| `DECLARE T` with no body (17) | rejects | give the type one field |
| sets: `SET OF`, `setFromList`, `UNION` (18-22) | rejects | a list |
| `REFUSE`, `#ASSERT REFUSED`, `BECAUSE` (02-04) | rejects | `MAYBE` and `NOTHING` |
| the prelude `YMD` (05, 53) | rejects | `Date d m y`; the core's `YMD` shim |
| `EVERY`, `WHOSE` (28-30) | rejects | one obligation for a named party taken as an input |
| `WITHIN n OF THE DEADLINE`, `OF THE JOIN` (31) | rejects | `WITHIN n`, which counts from when the obligation is entered |
| `AFTER n WITHIN m` (32, 33) | rejects | nothing: `main` reads `AFTER n` as more arguments |
| `BREACH BY LIST ...` (34) | rejects | `BREACH BY` one party |
| the same name defined in two nested `§` sections (35) | rejects | different names |
| `RULES EFFECTIVE DATE` (36, 37) | rejects | the date as a `GIVEN` input |
| the temporal built-ins and `VALUE AT`, `EVER BETWEEN` (38-40, 57, 58) | rejects | nothing |
| field opening, a bare field name where the `GIVEN` is a record (41) | rejects | `` person's `the age` `` |
| a rule applied inside `MUST (...)` (42) | rejects | write the constructor |
| a field read in an action's argument (51) | rejects | `PROVIDED` |
| the ledger: `RECORD`, `COMMIT`, `ATTEST`, `RECALL` (23-27, 52) | rejects | nothing |
| `@lang`, `@infixl`, `@infixr`, `@infix`, `@nonassertable`, `@nonexhaustive`, an unknown `@word` (01, 45-48) | rejects | leave them out |
| `IS INTEGER`, `WAIT UNTIL`, `MUST DO` (54-56) | rejects | `ISINTEGER`, `WAITUNTIL`, `MUST` |
| an input named in an action, as `MUST Pay Borrower creditor 10` (`run-must-names-an-input`; 43) | degrades silently: `creditor` becomes a fresh name that matches any payload, so paying a stranger fulfils the obligation | `MUST Pay Borrower payee 10 PROVIDED payee EQUALS creditor` |
| `MAY ... LEST BREACH` when nothing is done in time (`run-may-lest-lapse`) | degrades silently: the `LEST` is ignored and the lapse is `FULFILLED` | a `MUST`, if inaction should be a breach; no `LEST`, if it should have no consequence |
| a language tag on `@nlg` (`degrades-nlg-language-tag`) | degrades silently | untagged `@nlg` |
| `NOT a AND b` with no brackets | accepted, and read as `NOT (a AND b)` | bracket every `NOT` |

`check.sh` does not see a different `#TRACE` outcome: it counts error diagnostics and assertion lines only.

## What check.sh prints

`check.sh` is run as the brief says, with the stable binary as `L4` and `L4_TARGET=unstable`.
It prints "the target is unstable, so the main check was skipped" because only one binary was run; that binary is the stable `main` build 1.6.98, so the one run is the `main` run, and no second binary exists to compare it with.
`JL4_LIBRARY_PATH` was unset.
The columns are, per module: error diagnostics, assertions satisfied, failed, refused, and expected (how many failed assertions `check.sh`'s own `expected_failed` table says the module should have; the table lists none, so 0 everywhere).
This is the output of a run made when this file was generated:

```
module                                    errors satisfied  failed  refused  expected
cbca-core-control.l4                           0         0       0        0         0
cbca-core-definitions.l4                       0         0       0        0         0
cbca-core-isc.l4                               0         0       0        0         0
cbca-core-tests-control.l4                     0        85       0        0         0
cbca-core-tests-core.l4                        0        24       0        0         0
cbca-core-tests-definitions.l4                 0       204       0        0         0
cbca-core-tests-isc.l4                         0        27       0        0         0
cbca-core.l4                                   0         0       0        0         0
TOTAL (8 modules)                              0       340       0        0
(a failed assertion is also an error; any other error, or any refused assertion, makes the run red)
check.sh: the target is unstable, so the main check was skipped.
```

And `python3 -I srcrefs.py check --refs <the raw text file> cbca-core*.l4` prints:

```
srcrefs check: 172 src: lines, 82 runs, 114 locators, 0 problems
```
